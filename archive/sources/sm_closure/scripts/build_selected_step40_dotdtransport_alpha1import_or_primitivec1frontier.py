"""Build Step 40 dotD transport/alpha1 import and primitive-C1 frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT = PACKET_DIR / "step40_dotd_transport_alpha1_import.packet.json"
FRONTIER = PACKET_DIR / "step40_primitive_c1_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step40_dotDTransportAlpha1Import_or_PrimitiveC1Frontier_v1.md"

STEP39 = DATA / "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier.candidate.json"
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
CROSSREPO_ALPHA1 = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
C1_FRONTIER = DATA / "selected_c1_frontier_after_alpha1_import.candidate.json"
RTHETA_DYNAMIC = DATA / "selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure.candidate.json"

STATUS = "MTT_SELECTED_STEP40_DOTD_TRANSPORT_ALPHA1_IMPORTED_PRIMITIVE_C1_FRONTIER_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_FullSectorC1ValueEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP39, DOTD_PROBE, CROSSREPO_ALPHA1, C1_FRONTIER, RTHETA_DYNAMIC]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 40 inputs: " + ", ".join(missing))

    step39 = load(STEP39)
    dotd = load(DOTD_PROBE)
    alpha1 = load(CROSSREPO_ALPHA1)
    c1_frontier = load(C1_FRONTIER)
    rtheta_dynamic = load(RTHETA_DYNAMIC)

    alpha_import = alpha1["alpha1_driver_replay_import"]
    dotd_checks = {
        "step39_diagonal_end0_de_closed": step39["closure_decision"]["selected_diagonal_End0_covariant_D_E_closed"]
        is True,
        "transport_derivative_formula_closed": dotd["what_closes_now"]["transport_derivative_formula"] is True,
        "selected_dotD_source_algebra_closed": dotd["what_closes_now"]["selected_dotD_source_algebra"] is True,
        "validator_math_passes_when_flags_theorem_derived": dotd["validator_boundary"][
            "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"
        ]
        is True,
        "local_gap_was_only_alpha1_driver": dotd["validator_boundary"]["source_only_fails_only_by_alpha1_driver"]
        is True,
        "crossrepo_alpha1_driver_verified": alpha_import["alpha1_driver_verified"] is True,
        "crossrepo_selected_dotD_source_verified": alpha_import["selected_dotD_source_verified"] is True,
        "crossrepo_honest_dotD_replay": alpha_import["honest_dotD_alpha1_replay"] is True,
        "crossrepo_same_branch_du_dalpha": alpha_import["du_dalpha1_equals_h_ext"] is True
        and alpha_import["tangent_residual_l2"] == 0.0,
        "rtheta_dotd_transport_subgate_closed": rtheta_dynamic["closure_decision"][
            "dotD_alpha1_transport_subgate_closed"
        ]
        is True,
        "no_target_fitting": step39["target_fitting_used"] is False
        and dotd["target_fitting_used"] is False
        and alpha1["target_fitting_used"] is False,
    }
    dotd_transport_closes = all(dotd_checks.values())

    import_packet = {
        "schema": "MTTStep40DotDTransportAlpha1Import.v1",
        "status": "DOTD_ALPHA1_TRANSPORT_REPLAY_IMPORTED",
        "inputs": {
            "step39": rel(STEP39),
            "local_dotd_transport_probe": rel(DOTD_PROBE),
            "crossrepo_alpha1_driver_import": rel(CROSSREPO_ALPHA1),
            "c1_frontier_after_alpha1": rel(C1_FRONTIER),
            "rtheta_dynamic_pi": rel(RTHETA_DYNAMIC),
        },
        "proof_checks": dotd_checks,
        "transport_formula": dotd["transport_derivative_formula"],
        "alpha1_driver_import": alpha_import,
        "closure_result": {
            "selected_dotD_transport_derivative_formula_closed": dotd_transport_closes,
            "selected_alpha1_driver_normalization_closed": dotd_transport_closes,
            "same_branch_dotD_alpha1_values_closed": dotd_transport_closes,
            "honest_dotD_alpha1_replay_closed": dotd_transport_closes,
            "primitive_C1_contractions_from_operator_values_closed": False,
            "full_sector_C1_value_emission_closed": False,
            "internal_R_theta_scalar_rows_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "guardrail": (
            "This closes dotD/alpha1 as a transported-packet subgate. It does not emit primitive "
            "C1 contractions, Yukawa/CKM/PMNS values, Higgs rows, or no-knob scalar rows."
        ),
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(IMPORT, import_packet)

    frontier = {
        "schema": "MTTStep40PrimitiveC1Frontier.v1",
        "status": "DOTD_RETIRED_PRIMITIVE_C1_AND_FULL_SECTOR_C1_VALUES_OPEN",
        "closed_now": {
            "selected_S3_qutrit_rhoE": True,
            "diagonal_End0_covariant_D_E": True,
            "stationary_transport_Riesz_Green": True,
            "selected_dotD_alpha1_transport_subgate": dotd_transport_closes,
            "alpha1_driver_normalization": dotd_transport_closes,
        },
        "still_missing_for_true_value_closure": {
            "rank2_to_rank3_sector_transfer_values": step39["closure_decision"][
                "rank2_to_rank3_sector_transfer_values_closed"
            ]
            is False,
            "offdiagonal_End0_control": step39["closure_decision"]["offdiagonal_End0_control_closed"] is False,
            "coherent_spectral_zero_mode_projectors": step39["closure_decision"][
                "coherent_spectral_zero_mode_projectors_closed"
            ]
            is False,
            "primitive_C1_contractions": c1_frontier["what_remains_open"]["primitive_C1_contractions"],
            "selected_A_selected": c1_frontier["what_remains_open"]["selected_A_selected"],
            "selected_b_selected": c1_frontier["what_remains_open"]["selected_b_selected"],
            "internal_R_theta_scalar_rows": True,
            "Yukawa_CKM_PMNS_masses": c1_frontier["what_remains_open"]["Yukawa_CKM_PMNS_masses_Higgs_RG"],
        },
        "next_required_payload": {
            "target": NEXT,
            "minimum_fields": [
                "primitive C1 contractions from transported zero modes, Green response, and dotD",
                "sector routing or theorem showing primitive C1 no-need",
                "A_selected and b_selected promotion from the same selected source",
                "internal R_theta scalar rows only after primitive/full-sector C1 value closure",
            ],
        },
        "accepted_internal_scalar_row_count": 0,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(FRONTIER, frontier)

    candidate = {
        "candidate": "MTTSelectedStep40DotDTransportAlpha1ImportOrPrimitiveC1Frontier",
        "status": STATUS,
        "inputs": import_packet["inputs"],
        "output_packets": {
            "dotd_transport_alpha1_import": rel(IMPORT),
            "primitive_c1_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "Step40DotDTransportAlpha1ImportTheorem",
            "proved": dotd_transport_closes,
            "statement": (
                "The local transport-derivative theorem supplies the selected dotD_alpha1 source "
                "formula for U=exp(-u ad(T3)), and the sibling same-branch alpha1 replay imports "
                "du/dalpha1=h_ext, selected_dotD_source_verified, alpha1_driver_verified, and an "
                "honest dotD validator replay. Thus dotD/alpha1 is retired as an active blocker. "
                "The remaining live frontier is primitive/full-sector C1 value emission and then "
                "internal R_theta scalar rows."
            ),
        },
        "closure_decision": {
            "selected_diagonal_End0_covariant_D_E_closed": True,
            "selected_stationary_projector_Riesz_Green_transport_closed": True,
            "selected_dotD_transport_derivative_formula_closed": dotd_transport_closes,
            "selected_alpha1_driver_normalization_closed": dotd_transport_closes,
            "same_branch_dotD_alpha1_values_closed": dotd_transport_closes,
            "honest_dotD_alpha1_replay_closed": dotd_transport_closes,
            "primitive_C1_contractions_from_operator_values_closed": False,
            "selected_A_selected_closed": False,
            "selected_b_selected_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": dotd_transport_closes,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step40_dotDTransportAlpha1Import_or_PrimitiveC1Frontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selected_dotD_transport_derivative_formula_closed": dotd_transport_closes,
        "selected_alpha1_driver_normalization_closed": dotd_transport_closes,
        "same_branch_dotD_alpha1_values_closed": dotd_transport_closes,
        "honest_dotD_alpha1_replay_closed": dotd_transport_closes,
        "primitive_C1_contractions_from_operator_values_closed": False,
        "selected_A_selected_closed": False,
        "selected_b_selected_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step40 dotDTransportAlpha1Import or PrimitiveC1Frontier v1

Status: `{STATUS}`.

Step40 reconciles two already-proved pieces:

- local transport derivative:
  `dU/dalpha = -(du/dalpha) ad(T3) U`
- same-branch alpha1 import:
  `du/dalpha1 = h_ext`, `selected_dotD_source_verified = true`,
  `alpha1_driver_verified = true`

This retires `dotD_alpha1` as an active blocker for the transported packet.

Still open:

- primitive C1 contractions from the transported zero modes, Green response,
  and `dotD`
- full-sector C1 value emission or a theorem that primitive C1 is not needed
- `A_selected`, `b_selected`
- internal `R_theta` scalar rows and true no-knob SM equivalence

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
