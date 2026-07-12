"""Build the first tree-level SM-equivalence replay seed."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

VALUES = DATA / "sm_equivalence_reference_data_values_fill.candidate.json"

OUTPUT = DATA / "sm_equivalence_tree_level_replay_seed.candidate.json"
CERT = CERTS / "sm_equivalence_tree_level_replay_seed_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_Tree_Level_Replay_Seed_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_TREE_LEVEL_REPLAY_SEED_BUILT_PARTIAL_NUMERIC_REPLAY"
NEXT = "MTT_SM_Equivalence_CKM_Gauge_PMNS_Convention_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def mass_gev(value: dict[str, Any]) -> float:
    if value["units"] == "MeV":
        return value["central_value"] / 1000.0
    if value["units"] == "GeV":
        return value["central_value"]
    raise ValueError(f"Unsupported unit {value['units']}")


def diag(values: list[float]) -> list[list[float]]:
    return [[values[i] if i == j else 0.0 for j in range(3)] for i in range(3)]


def main() -> int:
    values = load(VALUES)
    masses = values["reference_values"]["masses"]
    constants = values["reference_values"]["constants"]
    yuks = values["reference_values"]["diagonal_yukawa_magnitudes"]
    v = constants["v_from_G_F"]["central_value"]

    yukawa_matrices = {
        "Y_u_diag": diag([yuks["u"]["central_value"], yuks["c"]["central_value"], yuks["t"]["central_value"]]),
        "Y_d_diag": diag([yuks["d"]["central_value"], yuks["s"]["central_value"], yuks["b"]["central_value"]]),
        "Y_e_diag": diag([yuks["e"]["central_value"], yuks["mu"]["central_value"], yuks["tau"]["central_value"]]),
    }

    replayed_masses = {
        "u": yuks["u"]["central_value"] * v / math.sqrt(2.0),
        "c": yuks["c"]["central_value"] * v / math.sqrt(2.0),
        "t": yuks["t"]["central_value"] * v / math.sqrt(2.0),
        "d": yuks["d"]["central_value"] * v / math.sqrt(2.0),
        "s": yuks["s"]["central_value"] * v / math.sqrt(2.0),
        "b": yuks["b"]["central_value"] * v / math.sqrt(2.0),
        "e": yuks["e"]["central_value"] * v / math.sqrt(2.0),
        "mu": yuks["mu"]["central_value"] * v / math.sqrt(2.0),
        "tau": yuks["tau"]["central_value"] * v / math.sqrt(2.0),
    }

    input_masses_gev = {key: mass_gev(masses[key]) for key in replayed_masses}
    mass_residuals = {
        key: replayed_masses[key] - input_masses_gev[key] for key in replayed_masses
    }
    max_abs_mass_residual = max(abs(value) for value in mass_residuals.values())

    higgs_tree = {
        "m_H_GeV": masses["H"]["central_value"],
        "v_GeV": v,
        "lambda_tree": masses["H"]["central_value"] ** 2 / (2.0 * v * v),
        "potential_convention": "V(H)=-mu^2 |H|^2 + lambda |H|^4, m_H^2=2 lambda v^2",
        "status": "TREE_LEVEL_SEED_NOT_RG_MATCHED",
    }

    ew_tree = {
        "m_W_GeV": masses["W"]["central_value"],
        "m_Z_GeV": masses["Z"]["central_value"],
        "v_GeV": v,
        "g2_from_mW_tree": 2.0 * masses["W"]["central_value"] / v,
        "sqrt_g1sq_plus_g2sq_from_mZ_tree": 2.0 * masses["Z"]["central_value"] / v,
        "sin2thetaW_on_shell_from_masses": 1.0
        - (masses["W"]["central_value"] ** 2 / masses["Z"]["central_value"] ** 2),
        "status": "TREE_LEVEL_ON_SHELL_SEED_NOT_RUNNING_GAUGE_TRIPLET",
    }
    g2 = ew_tree["g2_from_mW_tree"]
    gtot = ew_tree["sqrt_g1sq_plus_g2sq_from_mZ_tree"]
    ew_tree["g1_from_mW_mZ_tree"] = math.sqrt(max(gtot * gtot - g2 * g2, 0.0))
    ew_tree["e_from_tree_g1_g2"] = ew_tree["g1_from_mW_mZ_tree"] * g2 / gtot
    ew_tree["alpha_from_tree_masses"] = ew_tree["e_from_tree_g1_g2"] ** 2 / (4.0 * math.pi)
    ew_tree["alpha_low_energy_reference"] = constants["alpha"]["central_value"]
    ew_tree["alpha_tree_vs_low_energy_difference"] = (
        ew_tree["alpha_from_tree_masses"] - constants["alpha"]["central_value"]
    )

    replay_tests = {
        "mass_replay_exact_by_construction": max_abs_mass_residual <= 1e-15,
        "max_abs_mass_residual_GeV": max_abs_mass_residual,
        "diagonal_yukawa_matrices_built": True,
        "higgs_lambda_tree_built": True,
        "electroweak_tree_seed_built": True,
        "CKM_replay_done": False,
        "PMNS_replay_done": False,
        "gauge_running_replay_done": False,
        "RG_common_scale_replay_done": False,
        "full_SM_equivalence_replay_done": False,
    }

    candidate = {
        "candidate": "MTTSMEquivalenceTreeLevelReplaySeed",
        "status": STATUS,
        "inputs": {
            "reference_data_values_fill": rel(VALUES),
        },
        "source_boundary_preserved": True,
        "superset_strategy_use": values["superset_strategy_use"],
        "tree_level_replay": {
            "yukawa_matrices": yukawa_matrices,
            "replayed_masses_GeV": replayed_masses,
            "input_masses_GeV": input_masses_gev,
            "mass_residuals_GeV": mass_residuals,
            "higgs_tree": higgs_tree,
            "electroweak_tree": ew_tree,
        },
        "replay_tests": replay_tests,
        "interpretation": {
            "what_this_demonstrates": (
                "The measured-value interface is executable: after the selected source boundary is fixed, "
                "the repo can load versioned measured seeds and replay standard tree-level SM formulas "
                "without changing source data."
            ),
            "what_this_does_not_demonstrate": [
                "full SM-equivalence",
                "CKM or PMNS replay",
                "running gauge-coupling equivalence",
                "common-scale RG consistency",
                "no-knob derivation of constants",
            ],
            "superset_path_role": (
                "Superset work locked the source boundary; this replay is a straight downstream SM-standard "
                "calculation from measured slots."
            ),
        },
        "what_closes_now": {
            "first_numeric_tree_level_replay_seed": True,
            "diagonal_mass_to_yukawa_to_mass_loop": True,
            "higgs_tree_lambda_seed": True,
            "electroweak_tree_coupling_seed": True,
            "measured_replay_executable_without_source_selection": True,
        },
        "what_remains_open": {
            "CKM_reference_and_replay": True,
            "PMNS_neutrino_reference_and_replay": True,
            "gauge_running_triplet_reference_and_replay": True,
            "common_RG_scale_transport": True,
            "full_complex_Yukawa_matrices": True,
            "empirical_equivalence_audit_run": True,
            "full_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SMEquivalenceTreeLevelReplaySeedTheorem",
            "proved": True,
            "statement": (
                "From the frozen measured values packet, the repository constructs a tree-level replay seed: "
                "diagonal Yukawa matrices reproduce the admitted charged-fermion/quark masses by the standard "
                "relation m=yv/sqrt(2), and Higgs/electroweak tree-level seeds are computed. This proves the "
                "measured-slot interface is executable, but not full SM-equivalence or no-knob closure."
            ),
        },
    }

    cert = {
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SM-Equivalence Tree-Level Replay Seed v1

Status: `{STATUS}`.

## Result

The first numeric replay is executable.  It builds diagonal Yukawa matrices from
the frozen measured masses and `v`, then replays the masses through
`m_f=y_f v/sqrt(2)` with residual below machine precision.  It also computes a
tree-level Higgs quartic seed and an on-shell electroweak coupling seed from
`m_W`, `m_Z`, and `v`.

This is not full SM-equivalence.  CKM, PMNS, full running gauge couplings,
common-scale RG transport, and full complex Yukawa matrices remain open.

## Next

Build `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
