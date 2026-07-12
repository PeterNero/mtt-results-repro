from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import tempfile
from pathlib import Path


OUTPUTS = [
    "SMDR_yb_in",
    "SMDR_yc_in",
    "SMDR_ytau_in",
    "SMDR_lambda_in",
    "SMDR_yt_in",
    "SMDR_g_in",
    "SMDR_gp_in",
    "SMDR_g3_in",
]


def parse_value_file(path: Path) -> dict[str, float]:
    values: dict[str, float] = {}
    pattern = re.compile(r"^\s*([A-Za-z0-9_]+)\s*=\s*([^;]+);")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            values[match.group(1)] = float(eval(match.group(2), {"__builtins__": {}}, {}))
    return values


def input_rows(root: Path) -> list[dict]:
    reference = json.loads(
        (root / "candidate_data" / "sm_equivalence_reference_data_values_fill.candidate.json").read_text()
    )["reference_values"]
    masses = reference["masses"]
    constants = reference["constants"]

    def mass(name: str) -> tuple[float, float]:
        row = masses[name]
        factor = 0.001 if row["units"] == "MeV" else 1.0
        return row["central_value"] * factor, row["uncertainty"]["plus"] * factor

    rows = []
    for key, name in [
        ("SMDR_Mt_pole", "t"),
        ("SMDR_Mh_pole", "H"),
        ("SMDR_MZ_PDG", "Z"),
    ]:
        value, sigma = mass(name)
        rows.append({"id": key, "value": value, "sigma": sigma, "source": f"repo reference mass {name}"})
    rows.extend(
        [
            {"id": "SMDR_alphaS_5_MZ", "value": 0.118, "sigma": 0.0009, "source": "repo PDG-2025 alpha_s(MZ) replay"},
            {"id": "SMDR_alpha", "value": constants["alpha"]["central_value"], "sigma": constants["alpha"]["uncertainty"]["plus"], "source": "repo CODATA-2022 alpha"},
            {"id": "SMDR_Delta_alpha_had_5_MZ_in", "value": 0.02783, "sigma": 0.00011, "source": "SMDR v1.3 reference nuisance input"},
            {"id": "SMDR_GFermi", "value": constants["G_F"]["central_value"], "sigma": constants["G_F"]["uncertainty"]["plus"], "source": "repo CODATA-2022 G_F"},
        ]
    )
    for key, name in [
        ("SMDR_mbmb", "b"),
        ("SMDR_mcmc", "c"),
        ("SMDR_ms_2GeV", "s"),
        ("SMDR_md_2GeV", "d"),
        ("SMDR_mu_2GeV", "u"),
        ("SMDR_Mtau_pole", "tau"),
        ("SMDR_Mmuon_pole", "mu"),
        ("SMDR_Melectron_pole", "e"),
    ]:
        value, sigma = mass(name)
        rows.append({"id": key, "value": value, "sigma": sigma, "source": f"repo reference mass {name}"})
    for row in rows:
        row["finite_difference_step"] = max(row["sigma"], abs(row["value"]) * 1e-5, 1e-12)
    return rows


def write_input(path: Path, rows: list[dict], overrides: dict[str, float]) -> None:
    lines = ["# Generated MTT locked-input SMDR finite-difference point"]
    for row in rows:
        value = overrides.get(row["id"], row["value"])
        lines.append(f"{row['id']} = {value:.17g};")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_fit(executable: Path, work: Path, rows: list[dict], overrides: dict[str, float], scale: float, tag: str) -> dict[str, float]:
    input_path = work / f"input_{tag}.dat"
    output_path = work / f"output_{tag}.dat"
    write_input(input_path, rows, overrides)
    subprocess.run(
        [str(executable), "-i", input_path.name, "-o", output_path.name, "-Q", str(scale), "-e", "1e-10"],
        cwd=work,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )
    values = parse_value_file(output_path)
    return {name: values[name] for name in OUTPUTS}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smdr-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    smdr_root = args.smdr_root.resolve()
    executable = smdr_root / "calc_fit"
    if not executable.exists():
        raise FileNotFoundError(executable)
    reference = smdr_root / "ReferenceModel.dat"
    if not reference.exists():
        reference.write_bytes((smdr_root / "benchmark_data" / "ReferenceModel.dat").read_bytes())

    rows = input_rows(root)
    scale = next(row["value"] for row in rows if row["id"] == "SMDR_Mt_pole")
    with tempfile.TemporaryDirectory(prefix="mtt-smdr-", dir=smdr_root) as temporary:
        work = Path(temporary)
        (work / "ReferenceModel.dat").write_bytes(reference.read_bytes())
        central = run_fit(executable, work, rows, {}, scale, "central")
        jacobian: list[list[float]] = [[0.0] * len(rows) for _ in OUTPUTS]
        convergence_rows = []
        for column, row in enumerate(rows):
            step = row["finite_difference_step"]
            plus = run_fit(executable, work, rows, {row["id"]: row["value"] + step}, scale, f"{column}_plus")
            minus = run_fit(executable, work, rows, {row["id"]: row["value"] - step}, scale, f"{column}_minus")
            for output_index, output_name in enumerate(OUTPUTS):
                jacobian[output_index][column] = (plus[output_name] - minus[output_name]) / (2.0 * step)
            convergence_rows.append({
                "input": row["id"],
                "step": step,
                "max_symmetric_shift": max(abs(plus[name] - minus[name]) / 2.0 for name in OUTPUTS),
            })

    covariance = [[0.0] * len(OUTPUTS) for _ in OUTPUTS]
    for i in range(len(OUTPUTS)):
        for j in range(len(OUTPUTS)):
            covariance[i][j] = sum(
                jacobian[i][k] * jacobian[j][k] * rows[k]["sigma"] ** 2
                for k in range(len(rows))
            )

    payload = {
        "schema": "MTTSMDRMultiLoopCommonSourceTransportRaw.v1",
        "status": "SMDR_V1_3_MULTILOOP_COMMON_SOURCE_TRANSPORT_EXECUTED",
        "runtime": {
            "name": "SMDR",
            "version": "1.3",
            "repository": "https://github.com/davidgrobertson/SMDR",
            "scheme": "tadpole-free pure MSbar Standard Model",
            "running": "all known SM multi-loop RG contributions in SMDR v1.3",
            "matching": "multi-loop on-shell to MSbar fit implemented by SMDR v1.3",
        },
        "target_scale_GeV": scale,
        "output_basis": OUTPUTS,
        "central_output": central,
        "source_inputs": rows,
        "source_covariance_policy": "diagonal measured-input covariance; no input correlations available in the locked repo packet",
        "jacobian_rows_output_by_source": jacobian,
        "covariance_matrix": covariance,
        "finite_difference_diagnostics": convergence_rows,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
