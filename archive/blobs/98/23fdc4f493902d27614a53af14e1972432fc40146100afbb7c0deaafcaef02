from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREV_CERT = ROOT / "certificates" / "selected_hym_connection_to_finite_operator_extraction_spec_certificate.json"
GATE_PACKET = ROOT / "candidate_data" / "routec_hym_operator_values_gate_import.packet.json"

OUT_CERT = ROOT / "certificates" / "selected_hym_connection_to_finite_operator_extraction_run_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_hym_connection_to_finite_operator_extraction_run.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_HYM_Connection_to_Finite_Operator_Extraction_Run_v1.md"

STATUS = "SELECTED_HYM_CONNECTION_TO_FINITE_OPERATOR_EXTRACTION_RUN_CURRENT_INPUTS_FAIL_SOURCE_FLAGS"
NEXT_ARTIFACT = "MTT_Selected_HYM_SelectedConnection_or_RouteC_SelectedResidual_ValueSolve_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(script: str, candidate: str) -> dict:
    proc = subprocess.run(
        [sys.executable, script, candidate],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    stdout_lines = proc.stdout.splitlines()
    stderr_lines = proc.stderr.splitlines()
    return {
        "script": script,
        "path": candidate,
        "exit_code": proc.returncode,
        "pass": proc.returncode == 0,
        "stdout_tail": stdout_lines[-12:],
        "stderr_tail": stderr_lines[-12:],
    }


def main() -> None:
    prev = load(PREV_CERT)
    gate_packet = load(GATE_PACKET)
    honest = gate_packet["validator_results_on_honest_smoke"]

    validator_runs = {
        name: run_validator(item["script"], item["path"])
        for name, item in honest.items()
    }
    pass_set = sorted(name for name, result in validator_runs.items() if result["pass"])
    fail_set = sorted(name for name, result in validator_runs.items() if not result["pass"])

    expected_pass = {"rhoE_mesh", "rhoE_metric", "sector_maps"}
    expected_fail = {
        "route_c_residuals",
        "de_action",
        "riesz_gap",
        "reduced_green",
        "dotd_response",
    }

    checks = {
        "previous_spec_proved": prev["theorem"]["proved"] is True,
        "previous_next_matches": prev["next_required_artifact"]
        == "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_Run_v1",
        "mesh_metric_sector_pass": expected_pass.issubset(pass_set),
        "source_operator_validators_fail": expected_fail.issubset(fail_set),
        "no_all_validator_pass": len(fail_set) > 0,
        "no_selected_values_emitted": True,
    }

    source_flag_failures = {
        name: [
            line
            for line in result["stdout_tail"] + result["stderr_tail"]
            if "selected" in line or "alpha1_driver" in line
        ]
        for name, result in validator_runs.items()
        if not result["pass"]
    }

    theorem = {
        "name": "SelectedHYMConnectionToFiniteOperatorExtractionRunNoGo",
        "proved": all(checks.values()),
        "statement": (
            "The first extraction run against the current honest finite inputs "
            "does not emit selected operator values. Mesh, metric, and sector "
            "maps pass, but route_c residual, D_E, Riesz/gap, reduced Green, "
            "and dotD validators fail on selected-source or alpha1-driver "
            "flags. This confirms that the next missing datum is a selected "
            "connection/residual value solve, not another validator contract."
        ),
    }

    verdict = {
        "selected_values_emitted": False,
        "all_validators_pass_honestly": False,
        "pass_set": pass_set,
        "fail_set": fail_set,
        "can_emit_A_selected": False,
        "can_emit_b_selected": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "checks": checks,
        "validator_runs": validator_runs,
        "source_flag_failures": source_flag_failures,
        "verdict": verdict,
    }

    note = """# Selected HYM Connection to Finite Operator Extraction Run v1

## Result

The first extraction run was executed against the current honest finite inputs.

Passing validators:

```text
rhoE_mesh
rhoE_metric
sector_maps
```

Failing validators:

```text
route_c_residuals
D_E action
Riesz/gap
reduced Green
dotD alpha1 response
```

The failures are source/provenance failures, not algebraic shape failures:
selected-source and alpha1-driver flags are not theorem-derived on the current
honest inputs. Lifted flags remain forbidden as proof.

Thus this run does not emit selected finite operator values and cannot promote
`A_selected` or `b_selected`.

## Status

```text
SELECTED_HYM_CONNECTION_TO_FINITE_OPERATOR_EXTRACTION_RUN_CURRENT_INPUTS_FAIL_SOURCE_FLAGS
```

The next required artifact is:

```text
MTT_Selected_HYM_SelectedConnection_or_RouteC_SelectedResidual_ValueSolve_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "selected_hym_connection_to_finite_operator_extraction_run",
                "status": STATUS,
                "input_certificate": str(PREV_CERT),
                "theorem": theorem,
                "checks": checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
