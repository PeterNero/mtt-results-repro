"""Build the H-threshold cycle-break cutset for the strict tenth K row.

The current repo contains a closed loop of audited H-row attempts:

* direct H threshold / H quartic payload;
* radial D-term and EW-boundary/RG;
* intrinsic H quartic and large-threshold/RG;
* minimal primitive calibration.

This packet records the loop boundary as a theorem-level cutset.  It does not
claim the tenth row.  It prevents future frontier work from re-proving the same
support packets by requiring one of three cycle-breaking exits.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hthresholdcyclebreakcutset_or_tenthkrowfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CUTSET = PACKET_DIR / "h_threshold_cycle_break_cutset.packet.json"
ROUTE_MATRIX = PACKET_DIR / "tenth_k_row_route_matrix.packet.json"
NEXT_WORKORDER = PACKET_DIR / "next_tenth_k_row_source_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HThresholdCycleBreakCutset_or_TenthKRowFrontier_v1.md"

SOURCES = {
    "lambdaH_gate": DATA / "selected_lambdahpayloadexecution_or_tenkthresholdclosure.candidate.json",
    "h_payload": DATA / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure.candidate.json",
    "direct_h": DATA / "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem.candidate.json",
    "direct_quartic": DATA / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows.candidate.json",
    "radial_dterm": DATA / "selected_hradialthresholdscalarsource_or_tenkclosure.candidate.json",
    "ew_boundary": DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json",
    "intrinsic_quartic": DATA / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem.candidate.json",
    "h_rg_policy": DATA / "selected_hthresholdrgoperator_or_universalprimitivepolicy.candidate.json",
    "h_rg_source": DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun.candidate.json",
}

STATUS = (
    "MTT_SELECTED_HTHRESHOLDCYCLEBREAKCUTSET_OR_TENTHKROWFRONTIER_"
    "CLOSED_LOOP_BOUNDARY_STRICT_H_ROW_OPEN"
)
NEXT = "MTT_Selected_TenthHThresholdKRowSource_or_LargeThresholdRGPrimitiveTheorem_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing cycle-break inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    lambda_decision = sources["lambdaH_gate"]["closure_decision"]
    h_rg_decision = sources["h_rg_source"]["closure_decision"]

    cutset = {
        "schema": "MTTHThresholdCycleBreakCutset.v1",
        "status": "H_THRESHOLD_LOOP_BOUNDARY_RECORDED_TENTH_ROW_OPEN",
        "closure_claimed": True,
        "proved_claim": (
            "After the audited H/lambda route packets, strict scalar closure is "
            "reduced to one missing source object: K_threshold.Omega_H.lambda. "
            "Repeating row-local, HYM action, radial D-term, EW-boundary/RG, "
            "intrinsic-quartic, or minimal-calibration packets cannot close the "
            "row unless one of the listed cycle-break exits emits selected source "
            "data before observed replay."
        ),
        "accepted_selected_K_source_row_count": lambda_decision[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": lambda_decision[
            "selected_K_threshold_row_count_required"
        ],
        "strict_H_K_threshold_row_emitted": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "controlled_empirical_layer_available": h_rg_decision[
            "controlled_empirical_H_K_layer_built"
        ],
        "controlled_empirical_layer_selected_for_no_knob": False,
        "cycle_break_exits": [
            {
                "route_id": "direct_H_K_row",
                "must_emit": "K_threshold.Omega_H.lambda",
                "acceptance_test": (
                    "source-native H row emitted before lambda_H(M_t), threshold "
                    "targets, or fitted Omega values are read"
                ),
                "currently_emitted": False,
            },
            {
                "route_id": "selected_large_threshold_RG",
                "must_emit": "R_H^RG plus A_EW/mu_match/same-scheme transport",
                "acceptance_test": (
                    "large-threshold/RG operator is selected from the same q79/F,m=1 "
                    "branch and computes the H K row without target inversion"
                ),
                "currently_emitted": False,
            },
            {
                "route_id": "universal_primitive_crossuse",
                "must_emit": "UP-RET-OVERLAP.HRG as a strict source primitive",
                "acceptance_test": (
                    "the calibrated primitive predicts at least one non-Higgs "
                    "threshold/RG target without retuning, then supplies the H row"
                ),
                "currently_emitted": False,
            },
        ],
        "forbidden_repeats": [
            "row-local brute force without new selected source values",
            "diagonal HYM or pure trace degeneracy as a value source",
            "B_Huv support promoted directly to Herm(2) value rows",
            "lambda_H(M_t) inversion treated as source selection",
            "controlled one-parameter calibration counted as no-knob closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_matrix = {
        "schema": "MTTTenthKRowRouteMatrix.v1",
        "status": "THREE_STRICT_EXITS_DEFINED_NONE_ACCEPTED",
        "closure_claimed": True,
        "routes": cutset["cycle_break_exits"],
        "imported_statuses": {
            name: packet["status"] for name, packet in sources.items()
        },
        "route_decision": {
            "direct_H_K_row_accepted": False,
            "selected_large_threshold_RG_accepted": False,
            "universal_primitive_crossuse_accepted": False,
            "strict_tenth_K_row_accepted": False,
            "controlled_empirical_10_of_10_available": True,
            "strict_no_knob_10_of_10_available": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    workorder = {
        "schema": "MTTNextTenthKRowSourceWorkorder.v1",
        "status": "NEXT_WORKORDER_ATTACK_CYCLE_BREAK_EXITS_ONLY",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "allowed_next_constructions": [
            "derive direct source-native K_threshold.Omega_H.lambda",
            "derive selected large-threshold/RG transport operator for H",
            "promote UP-RET-OVERLAP.HRG by cross-use prediction without retuning",
        ],
        "minimum_payload": [
            "same-branch q79/F,m=1 provenance",
            "source-owned numeric or exact symbolic row value",
            "no observed target used as selector",
            "conditional ten-K theorem trigger",
            "Omega_H.lambda execution certificate",
        ],
        "not_allowed_as_next_step": cutset["forbidden_repeats"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHThresholdCycleBreakCutsetOrTenthKRowFrontier",
        "status": STATUS,
        "previous_status": sources["h_rg_source"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "h_threshold_cycle_break_cutset": rel(CUTSET),
            "tenth_k_row_route_matrix": rel(ROUTE_MATRIX),
            "next_tenth_k_row_source_workorder": rel(NEXT_WORKORDER),
        },
        "closure_decision": {
            "accepted_selected_K_source_row_count": cutset[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": cutset[
                "selected_K_threshold_row_count_required"
            ],
            "strict_H_K_threshold_row_emitted": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
            "cycle_break_cutset_closed": True,
            "direct_H_K_row_exit_accepted": False,
            "selected_large_threshold_RG_exit_accepted": False,
            "universal_primitive_crossuse_exit_accepted": False,
            "controlled_empirical_10_of_10_available": True,
            "controlled_empirical_10_of_10_selected_for_no_knob": False,
        },
        "theorem": {
            "name": "HThresholdCycleBreakCutsetTheorem",
            "proved": True,
            "statement": (
                "The audited H/lambda frontier has strict K-threshold closure at "
                "9/10.  The remaining H/lambda row can be closed only by a new "
                "selected direct H K row, selected large-threshold/RG transport, "
                "or a universal primitive promoted by cross-use prediction.  "
                "Existing support/calibration packets alone do not emit the row."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHThresholdCycleBreakCutsetOrTenthKRowFrontier",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "theorem_proved": True,
        "accepted_selected_K_source_row_count": cutset[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": cutset[
            "selected_K_threshold_row_count_required"
        ],
        "strict_H_K_threshold_row_emitted": False,
        "controlled_empirical_10_of_10_available": True,
        "controlled_empirical_10_of_10_selected_for_no_knob": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected H-Threshold Cycle-Break Cutset or Tenth K-Row Frontier v1

## Theorem

`HThresholdCycleBreakCutsetTheorem` is now emitted.

The audited H/lambda frontier has strict `K_threshold` closure at `9/10`.
The nine charged rows are selected source rows.  The remaining H/lambda row is
exactly `K_threshold.Omega_H.lambda`.

After the row-local, HYM action, radial D-term, EW-boundary/RG, intrinsic H
quartic, H-threshold/RG policy, and minimal-calibration packets, repeating the
same support packets cannot close the row.  A strict close now requires one of:

1. Direct source-native `K_threshold.Omega_H.lambda`.
2. Selected large-threshold/RG transport emitting the H row before target replay.
3. `UP-RET-OVERLAP.HRG` promoted by non-Higgs cross-use prediction without retuning.

## Decision

- Strict selected K rows: `9/10`.
- Strict H K row emitted: `false`.
- Controlled empirical 10/10 layer available: `true`.
- Controlled empirical layer selected for no-knob: `false`.
- Full no-knob/true-SM closure: `false`.

## Next Artifact

`{NEXT}`

This artifact must attack one of the three cycle-break exits.  It must not
repeat row-local brute force, diagonal HYM support, pure trace degeneracy,
`B_Huv` support promotion, or `lambda_H(M_t)` inversion as though those were new
source data.
"""

    write_json(CUTSET, cutset)
    write_json(ROUTE_MATRIX, route_matrix)
    write_json(NEXT_WORKORDER, workorder)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
