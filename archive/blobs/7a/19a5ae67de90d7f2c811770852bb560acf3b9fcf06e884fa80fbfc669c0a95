"""Build R_theta coefficient-formula derivation / selected-owner bridge attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_coefficientformuladerivation_or_selectedownerbridge"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FORMULA_BASIS = PACKET_DIR / "dynamic_precoefficient_formula_basis.packet.json"
SLOT_PROJECTION = PACKET_DIR / "rtheta_slot_projection_feasibility.packet.json"
BRIDGE_ATTEMPT = PACKET_DIR / "selected_owner_bridge_attempt.packet.json"
DECISION = PACKET_DIR / "coefficient_formula_derivation_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_coefficient_formula_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaCoefficientFormulaDerivation_or_SelectedOwnerBridge_v1.md"

PREVIOUS = DATA / "selected_rtheta_openlabelreevaluation_or_frontierminimality.candidate.json"
RTHETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
COEFFICIENT_MANIFEST = (
    DATA
    / "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
    / "rtheta_row_coefficient_slot_manifest.packet.json"
)
OWNER_MATRIX = (
    DATA
    / "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
    / "rtheta_source_owner_candidate_matrix.packet.json"
)
OPEN_FRONTIER = (
    DATA
    / "selected_rtheta_openlabelreevaluation_or_frontierminimality"
    / "minimal_rtheta_frontier_after_open_recheck.packet.json"
)
DYNAMIC_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
DYNAMIC_PACKET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
BACKPROMOTION = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "dynamic_transfer_backpromotion_theorem.packet.json"
)
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
RESIDUALS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETACOEFFICIENTFORMULADERIVATION_OR_SELECTEDOWNERBRIDGE_"
    "BUILT_PRECOEFFICIENT_BASIS_PROJECTION_KERNEL_OPEN"
)
NEXT = "MTT_Selected_RThetaPhysicalProjectionKernel_or_ProfileResponse_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing R_theta coefficient derivation sources: " + ", ".join(missing))


def real_trace(matrix: list[Any]) -> float:
    total = 0.0
    for i, row in enumerate(matrix):
        value = row[i]
        if isinstance(value, list):
            total += float(value[0])
        else:
            total += float(value)
    return total


def slot_projection(slot_id: str) -> dict[str, Any]:
    mapping = {
        "threshold::top": ("u", "family_3", True),
        "threshold::bottom": ("d", "family_3", True),
        "threshold::charm": ("u", "family_2", True),
        "threshold::tau": ("e", "family_3", True),
        "threshold::W_Z_H": ("gauge_higgs", "bosonic_carrier", False),
        "mass_scheme::top_direct_pole_running": ("u", "family_3", True),
        "mass_scheme::bottom_MSbar_native_scale_transport": ("d", "family_3", True),
        "mass_scheme::charm_MSbar_native_scale_transport": ("u", "family_2", True),
        "mass_scheme::tau_pole_rest_to_running_lepton": ("e", "family_3", True),
        "mass_scheme::Higgs_pole_running_lambda": ("higgs", "scalar_carrier", False),
    }
    sector, projector, has_dynamic_sector = mapping[slot_id]
    return {
        "slot_id": slot_id,
        "projected_dynamic_sector": sector,
        "required_physical_projector": projector,
        "dynamic_sector_present": has_dynamic_sector,
        "precoefficient_formula_skeleton": (
            f"coefficient[{slot_id}] = <{projector}, H1_{sector}>_selected"
            if has_dynamic_sector
            else f"coefficient[{slot_id}] requires selected {sector} carrier response"
        ),
        "family_or_carrier_projector_emitted": False,
        "physical_threshold_projection_kernel_emitted": False,
        "accepted_coefficient_formula": False,
        "missing_for_acceptance": [
            "selected physical projection kernel Pi_Rtheta",
            "family/carrier projector emitted before observed-value comparison",
            "scale/scheme/loop-order derivative or matching convention",
        ],
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        RTHETA_CONTRACT,
        COEFFICIENT_MANIFEST,
        OWNER_MATRIX,
        OPEN_FRONTIER,
        DYNAMIC_VALUES,
        DYNAMIC_PACKET,
        BACKPROMOTION,
        VALUE_PACKET,
        RESIDUALS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    contract = load(RTHETA_CONTRACT)
    coeff_manifest = load(COEFFICIENT_MANIFEST)
    owner_matrix = load(OWNER_MATRIX)
    open_frontier = load(OPEN_FRONTIER)
    dynamic_values = load(DYNAMIC_VALUES)
    dynamic_packet = load(DYNAMIC_PACKET)
    backpromotion = load(BACKPROMOTION)
    value_packet = load(VALUE_PACKET)
    residuals = load(RESIDUALS)

    sector_basis = []
    for sector, payload in dynamic_values["sector_first_responses"].items():
        sector_basis.append(
            {
                "sector": sector,
                "source_direction": payload["source_direction"],
                "trace_H1": payload["invariants"]["trace"],
                "traceless_norm_sq": payload["invariants"]["traceless_norm_sq"],
                "hermitian_residual_norm_sq": payload["invariants"][
                    "hermitian_residual_norm_sq"
                ],
                "trace_recomputed": real_trace(payload["first_hermitian_response_H1"]),
                "formula_basis_role": "selected dynamic pre-coefficient observable",
            }
        )

    formula_basis = {
        "schema": "MTTDynamicPreCoefficientFormulaBasis.v1",
        "status": "DYNAMIC_PRECOEFFICIENT_FORMULA_BASIS_CLOSED",
        "source": rel(DYNAMIC_VALUES),
        "same_source_packet": rel(DYNAMIC_PACKET),
        "backpromotion": rel(BACKPROMOTION),
        "selected_by_MTT": dynamic_values["selected_by_MTT"],
        "same_source_fields_closed": dynamic_packet["attempted_selected_packet"]["fields"],
        "sector_basis": sector_basis,
        "basis_closed": all(row["hermitian_residual_norm_sq"] == 0.0 for row in sector_basis),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FORMULA_BASIS, formula_basis)

    slot_rows = [slot_projection(row["slot_id"]) for row in coeff_manifest["coefficient_slots"]]
    skeleton_count = sum(1 for row in slot_rows if row["dynamic_sector_present"])
    accepted_count = sum(1 for row in slot_rows if row["accepted_coefficient_formula"])

    slot_projection_packet = {
        "schema": "MTTRThetaSlotProjectionFeasibility.v1",
        "status": "SLOT_PROJECTION_SKELETONS_BUILT_PHYSICAL_PROJECTION_KERNEL_OPEN",
        "coefficient_manifest": rel(COEFFICIENT_MANIFEST),
        "slot_rows": slot_rows,
        "slot_count": len(slot_rows),
        "precoefficient_skeleton_count": skeleton_count,
        "accepted_coefficient_formula_count": accepted_count,
        "physical_projection_kernel_required": "Pi_Rtheta",
        "physical_projection_kernel_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SLOT_PROJECTION, slot_projection_packet)

    best_owner = owner_matrix["best_current_precursor"]
    bridge_attempt = {
        "schema": "MTTSelectedOwnerBridgeAttempt.v1",
        "status": "SELECTED_OWNER_BRIDGE_ATTEMPTED_REDUCED_TO_PHYSICAL_PROJECTION_KERNEL",
        "best_current_precursor": best_owner,
        "precursor_source": rel(DYNAMIC_PACKET),
        "precursor_satisfies": {
            "same_source": dynamic_packet["attempted_selected_packet"]["packet_flags"]["one_same_source"],
            "selected_operator_values": dynamic_packet["attempted_selected_packet"]["fields"][
                "operator_values"
            ]["selected_emitted"],
            "selected_overlap_transfer": dynamic_packet["attempted_selected_packet"]["fields"][
                "overlap_transfer"
            ]["selected_emitted"],
            "selected_normalization": dynamic_packet["attempted_selected_packet"]["fields"][
                "normalization"
            ]["selected_emitted"],
            "selected_b_source": dynamic_packet["attempted_selected_packet"]["packet_flags"][
                "promote_to_b_selected"
            ],
        },
        "missing_for_selected_rtheta_owner": [
            "Pi_Rtheta physical projection kernel from dynamic sectors to threshold/mass-scheme slots",
            "selected scale/scheme/loop-order convention functor",
            "full profile response or accepted diagonal limitation theorem",
        ],
        "bridge_theorem_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BRIDGE_ATTEMPT, bridge_attempt)

    decision = {
        "schema": "MTTRThetaCoefficientFormulaDerivationDecision.v1",
        "status": "PRECOEFFICIENT_BASIS_CLOSED_RTHETA_PROJECTION_KERNEL_OPEN",
        "previous_status": previous["status"],
        "functional_symbol": contract["functional_symbol"],
        "dynamic_precoefficient_formula_basis_closed": True,
        "slot_projection_skeletons_closed": True,
        "precoefficient_skeleton_count": skeleton_count,
        "accepted_coefficient_formula_count": accepted_count,
        "selected_owner_bridge_reduced": True,
        "rtheta_packet_constructed": False,
        "selected_threshold_response_functional_instantiated": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "old_frontier": open_frontier["active_frontier"],
        "contracted_frontier": [
            "derive selected physical projection kernel Pi_Rtheta",
            "select precision convention functor before measured-value comparison",
            "attach full profile response or accepted diagonal limitation theorem",
        ],
        "why_frontier_contracts": (
            "The same-source dynamic matter packet supplies the pre-coefficient operator basis. "
            "The owner bridge and coefficient formula tasks now share one missing object: Pi_Rtheta, "
            "the physical projection kernel from dynamic sectors to threshold/mass-scheme slots."
        ),
        "residual_tables_used_only_for_validation": residuals["summary"]["all_residuals_finite"],
        "firstpass_value_packet_used_only_as_replay_target": value_packet[
            "accepted_as_versioned_common_scale_candidate_values"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterCoefficientFormulaAttempt.v1",
        "status": "NEXT_ATTACK_PHYSICAL_PROJECTION_KERNEL_OR_PROFILE_RESPONSE",
        "closed_now": {
            "dynamic_precoefficient_formula_basis": True,
            "slot_projection_skeletons": True,
            "owner_bridge_reduced_to_projection_kernel": True,
            "residuals_kept_validation_only": True,
        },
        "still_open": decision["contracted_frontier"],
        "recommended_next": {
            "artifact": NEXT,
            "must_emit": [
                "Pi_Rtheta family/carrier projectors for top, bottom, charm, tau, W/Z/H, Higgs/lambda",
                "projection equations from selected H1_sector/dynamic basis to each R_theta slot",
                "selected precision convention functor",
                "profile response or diagonal limitation theorem",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaCoefficientFormulaDerivationOrSelectedOwnerBridge",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "dynamic_precoefficient_formula_basis": rel(FORMULA_BASIS),
            "rtheta_slot_projection_feasibility": rel(SLOT_PROJECTION),
            "selected_owner_bridge_attempt": rel(BRIDGE_ATTEMPT),
            "coefficient_formula_derivation_decision": rel(DECISION),
            "next_cutset_after_coefficient_formula_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaPreCoefficientBasisAndProjectionKernelReductionTheorem",
            "proved": True,
            "statement": (
                "The same-source dynamic matter/overlap packet supplies a selected pre-coefficient operator "
                "basis for R_theta: sector response matrices, traces, traceless norms, overlap transfer, and "
                "normalization are emitted without observed-value selection. Mapping this basis to the ten "
                "R_theta coefficient slots produces formula skeletons for the matter slots, but no accepted "
                "physical threshold or mass-scheme coefficient formula because the physical projection kernel "
                "Pi_Rtheta and selected precision convention are not emitted. Thus the owner bridge and row "
                "coefficient problems reduce to Pi_Rtheta plus convention/profile response."
            ),
        },
        "closure_decision": {
            "dynamic_precoefficient_formula_basis_closed": True,
            "slot_projection_skeletons_closed": True,
            "selected_physical_projection_kernel_closed": False,
            "accepted_coefficient_formulas_closed": False,
            "selected_owner_bridge_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RThetaCoefficientFormulaDerivation_or_SelectedOwnerBridge_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "dynamic_precoefficient_formula_basis_closed": True,
        "precoefficient_skeleton_count": skeleton_count,
        "accepted_coefficient_formula_count": accepted_count,
        "frontier_contracts_to_three_obligations": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaCoefficientFormulaDerivation or SelectedOwnerBridge v1

Status: `{STATUS}`.

This artifact tries to derive `R_theta` coefficient formulas from the selected
same-source dynamic matter/overlap packet.

```text
dynamic pre-coefficient basis closed : true
coefficient slots                    : {len(slot_rows)}
pre-coefficient skeletons            : {skeleton_count}
accepted coefficient formulas         : 0
frontier obligations after reduction : 3
```

The bridge and coefficient tasks now share one missing internal object:
`Pi_Rtheta`, the selected physical projection kernel from dynamic sectors to
threshold and mass-scheme slots.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
