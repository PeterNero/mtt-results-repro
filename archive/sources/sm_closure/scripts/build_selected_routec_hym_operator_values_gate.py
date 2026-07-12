"""Build the selected HYM operator-values gate after abstract HYM existence."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
Q79_SCRIPTS = Q79 / "scripts"
SMOKE = Q79 / "candidate_data" / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
LIFTED = Q79 / "candidate_data" / "selected_valpha_operator_source_sufficiency" / "route_c_lifted_flags"

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_routec_hym_operator_values_gate.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_routec_hym_operator_values_gate_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1.md"


VALIDATORS = {
    "route_c_residuals": ("validate_iwasawa_route_c_residuals.py", SMOKE / "route_c_residual.candidate.json"),
    "rhoE_mesh": ("validate_iwasawa_rhoE_mesh.py", SMOKE / "rhoE_mesh.candidate.json"),
    "rhoE_metric": ("validate_iwasawa_rhoE_metric.py", SMOKE / "rhoE_metric.candidate.json"),
    "sector_maps": ("validate_iwasawa_sector_maps.py", SMOKE / "sector_maps.candidate.json"),
    "de_action": ("validate_iwasawa_de_action.py", SMOKE / "de_action.candidate.json"),
    "riesz_gap": ("validate_iwasawa_riesz_gap.py", SMOKE / "riesz_gap.candidate.json"),
    "reduced_green": ("validate_iwasawa_reduced_green.py", SMOKE / "reduced_green.candidate.json"),
    "dotd_response": ("validate_iwasawa_dotd_response.py", SMOKE / "dotd_response.candidate.json"),
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(script_name: str, path: Path) -> dict:
    proc = subprocess.run(
        [sys.executable, str(Q79_SCRIPTS / script_name), str(path)],
        cwd=Q79,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "script": str(Q79_SCRIPTS / script_name),
        "path": str(path),
        "exit_code": proc.returncode,
        "pass": proc.returncode == 0,
        "stdout_tail": proc.stdout.strip().splitlines()[-12:],
    }


def all_slot_flag(path: Path, container: str, flag: str) -> bool:
    data = load(path)
    slots = data[container]
    return all(slot.get(flag) is True for slot in slots.values())


def dotd_flags(path: Path) -> dict:
    data = load(path)
    slots = data["dotd_response_slots"]
    return {
        "selected_dotD_source_verified": all(slot.get("selected_dotD_source_verified") is True for slot in slots.values()),
        "alpha1_driver_verified": all(slot.get("alpha1_driver_verified") is True for slot in slots.values()),
    }


def main() -> int:
    hym_bridge_path = ROOT / "candidate_data" / "selected_routec_equalradius_gauduchon_hym_bridge.candidate.json"
    ah_layer_path = ROOT / "candidate_data" / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json"
    routec_residual = load(SMOKE / "route_c_residual.candidate.json")
    hym_bridge = load(hym_bridge_path)
    ah_layer = load(ah_layer_path)

    validator_results = {
        name: run_validator(script, path)
        for name, (script, path) in VALIDATORS.items()
    }

    smoke_flags = {
        "route_c_residual_selected_source_verified": routec_residual.get("selected_source_verified") is True,
        "rhoE_mesh_selected_by_mtt": load(SMOKE / "rhoE_mesh.candidate.json").get("selected_by_mtt") is True,
        "de_action_all_selected_source_verified": all_slot_flag(SMOKE / "de_action.candidate.json", "operator_slots", "selected_source_verified"),
        "riesz_gap_all_selected_source_verified": all_slot_flag(SMOKE / "riesz_gap.candidate.json", "spectral_slots", "selected_source_verified"),
        "reduced_green_all_selected_source_verified": all_slot_flag(SMOKE / "reduced_green.candidate.json", "green_slots", "selected_source_verified"),
        **dotd_flags(SMOKE / "dotd_response.candidate.json"),
    }

    lifted_validators = {
        "de_action": run_validator("validate_iwasawa_de_action.py", LIFTED / "de_action.hypothetical_selected.json"),
        "riesz_gap": run_validator("validate_iwasawa_riesz_gap.py", LIFTED / "riesz_gap.hypothetical_selected.json"),
        "reduced_green": run_validator("validate_iwasawa_reduced_green.py", LIFTED / "reduced_green.hypothetical_selected.json"),
        "dotd_response": run_validator("validate_iwasawa_dotd_response.py", LIFTED / "dotd_response.hypothetical_selected.json"),
    }

    shape_support = {
        "honest_smoke_has_zero_residuals": all(
            abs(row["value"]) <= row["tolerance"]
            for row in routec_residual["residuals"].values()
        ),
        "lifted_flag_matrices_pass_lower_validators": all(row["pass"] for row in lifted_validators.values()),
        "honest_smoke_has_mixed_lower_validator_status": any(row["pass"] for row in validator_results.values())
        and any(not row["pass"] for row in validator_results.values()),
        "honest_smoke_blocked_by_selected_source_flags": not all(smoke_flags.values()),
    }

    selected_operator_values_closed = (
        hym_bridge["HYM_existence_bridge"]["abstract_HYM_existence_for_selected_bundle_metric"] is True
        and all(smoke_flags.values())
        and all(row["pass"] for row in validator_results.values())
    )

    candidate = {
        "candidate": "MTTSelectedRouteCHYMOperatorValuesOrDERieszGreenDotDSource",
        "status": "MTT_SELECTED_ROUTEC_HYM_OPERATOR_VALUES_GATE_BUILT_VALUES_NOT_EMITTED",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "equalradius_HYM_bridge": str(hym_bridge_path),
            "selected_AH_source_layer": str(ah_layer_path),
            "route_c_smoke_dir": str(SMOKE),
            "lifted_flags_dir": str(LIFTED),
        },
        "abstract_HYM_import": {
            "selected_AH_source_layer": ah_layer["selected_AH_goodcover_stability_layer"]["proved"],
            "selected_equalradius_HYM_existence": hym_bridge["HYM_existence_bridge"]["abstract_HYM_existence_for_selected_bundle_metric"],
            "what_it_entitles": "existence of a unique unitary-gauge class of HYM connection for the selected holomorphic bundle and metric",
            "what_it_does_not_entitle": "finite rho_E, D_E, Riesz/Green, dotD, C1, or overlap matrices without an extraction theorem",
        },
        "validator_results_on_honest_smoke": validator_results,
        "source_flags_on_honest_smoke": smoke_flags,
        "lifted_flag_diagnostic": {
            "validators": lifted_validators,
            "guardrail": "lifted selected flags prove schema sufficiency only; they are not theorem-derived values",
        },
        "shape_support": shape_support,
        "selected_operator_values_closed": selected_operator_values_closed,
        "needed_extraction_theorem": {
            "name": "Selected_HYM_Connection_to_Finite_Operator_Extraction.v1",
            "statement": "From the selected AH/Cech V_alpha bundle, selected equal-radius Gauduchon metric, selected HYM connection, and selected finite cover/basis/quadrature, derive the finite rho_E, metric, D_E, Riesz/Green, dotD, and C1/overlap matrices accepted by the validators.",
            "must_emit": [
                "transition/connection representative for the HYM connection in the selected good-cover or AH basis",
                "finite quotient/basis/truncation map with error bounds",
                "rho_E and metric tables derived from the connection, not copied from smoke",
                "D_E action matrices and stiffness matrices from the same connection",
                "Riesz projectors, complement gaps, and reduced Green operators with truncation proof",
                "dotD_alpha1 as the same-branch derivative of the selected D_E package",
                "C1/overlap primitive contractions derived from the same response data",
            ],
            "minimum_validator_target": "all honest route_c_residual, rhoE, metric, sector, D_E, Riesz, Green, and dotD validators pass with source flags true and no lifted-flag provenance",
        },
        "superset_strategy": {
            "straight_path": "extract finite operators from the selected HYM connection",
            "combined_paths": [
                "abstract HYM existence gives the connection class",
                "Route-C smoke supplies schema/support shapes only",
                "lifted flags show validator sufficiency only",
                "Galerkin/spectral route remains the legal extraction mechanism",
            ],
            "locked_target": "selected equal-radius q79/F,m=1 V_alpha branch",
            "target_fitting_used": False,
        },
        "what_closes_now": {
            "operator_value_gate_instantiated_after_HYM_existence": True,
            "abstract_HYM_no_longer_blocker": True,
            "exact_missing_extraction_theorem_identified": True,
            "lifted_flag_reuse_rejected": True,
        },
        "what_remains_open": {
            "selected_HYM_connection_values": True,
            "selected_rho_E_metric_tables": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_C1_overlap_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_v1",
    }

    cert = {
        "certificate": "MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "abstract_HYM_no_longer_blocker": True,
        "selected_operator_values_closed": selected_operator_values_closed,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected Route-C HYM Operator Values or D_E/Riesz/Green/dotD Source v1

## Claim

The abstract HYM existence blocker is now removed, but concrete finite operator
values are not emitted yet.  The old Route-C files remain support data because
their selected-source flags are false, and the lifted-flag files remain
diagnostic because the flags are not theorem-derived.

## What Is Needed

The next theorem must extract finite data from the selected HYM connection:

```text
selected V_alpha + selected equal-radius metric + selected HYM connection
  -> selected cover/basis/quadrature
  -> rho_E, metric, D_E, Riesz/Green, dotD, C1/overlap matrices
```

The validators already define the acceptance boundary.  Passing matrices are
not enough; the source fields must be derived from the selected HYM connection
or an equivalent same-source Galerkin/Strominger extraction.

## Superset Status

This uses the straight HYM extraction path, with Route-C/Galerkin retained as
the execution route and diagnostic smoke retained only as support.  No observed
constants or target fitting are used.
"""

    OUT_CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_PROOF.parent.mkdir(parents=True, exist_ok=True)
    OUT_CANDIDATE.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_PROOF.write_text(proof, encoding="utf-8")
    print(f"Wrote {OUT_CANDIDATE}")
    print(f"Wrote {OUT_CERT}")
    print(f"Wrote {OUT_PROOF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
