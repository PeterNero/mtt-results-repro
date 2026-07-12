"""Build CONST-EM-01 dimensional-anchor packet gate.

This freezes the exact A6 packet needed after the K_phys source hunt.  It does
not fill the physical value; it makes the remaining promotion criteria
machine-auditable.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
PROTO = TEXPAPERS / "mtt-protospinor-gr-response-proof"
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_dimensional_anchor_packet_gate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ACCEPTANCE = BASE / "acceptance_criteria.packet.json"
ROUTES = BASE / "route_matrix.packet.json"
PROMOTION = BASE / "promotion_tests.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_DimensionalAnchorPacketGate_v1.md"

STATUS = "MTT_CONST_EM_01_DIMENSIONAL_ANCHOR_PACKET_GATE_BUILT_VALUE_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    kphys_path = DATA / "const_em_01_alpha1_kphys_source_hunt.candidate.json"
    template_path = PROTO / "candidate_data" / "selected_dimensional_anchor_packet.template.json"
    mtheory_attempt_path = PROTO / "candidate_data" / "selected_dimensional_anchor_packet.mtheory_attempt.json"
    anchor_search_path = PROTO / "certificates" / "target_independent_dimensional_anchor_search_certificate.json"
    alpha_phys_path = PROTO / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"
    ew_anchor_path = QA_SU3 / "candidate_data" / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json"

    kphys = load(kphys_path)
    template = load(template_path)
    mtheory_attempt = load(mtheory_attempt_path)
    anchor_search = load(anchor_search_path)
    alpha_phys = load(alpha_phys_path)
    ew_anchor = load(ew_anchor_path)

    import_checks = {
        "kphys_reduction_available": kphys["what_closes_now"]["K_phys_reduced_to_alpha_phys_or_action_unit"] is True,
        "template_ready": template["packet"] == "SelectedDimensionalAnchorPacket" and template["status"] == "TEMPLATE_UNFILLED",
        "mtheory_attempt_same_branch": mtheory_attempt["source_certification"]["same_branch_as_rho_uv_and_z448"] is True,
        "mtheory_attempt_value_open": mtheory_attempt["dimensionful_quantity"]["value"] is None,
        "anchor_search_exhausted": anchor_search["status"] == "DIMENSIONAL_ANCHOR_SEARCH_EXHAUSTED_PACKET_GATE_READY",
        "best_route_is_mtheory": anchor_search["verdict"]["best_route"] == "m_theory_modal_gap_planck_anchor",
        "alpha_phys_single_anchor": alpha_phys["theorem_result"]["alpha_phys_status"] == "SOLE_REMAINING_EXTERNAL_DIMENSIONFUL_ANCHOR",
        "ew_anchor_needs_same_packet": ew_anchor["decision"]["physical_gauge_action_anchor_closed"] is False,
    }

    acceptance = {
        "schema": "MTTConstEM01DimensionalAnchorAcceptanceCriteria.v1",
        "status": "ACCEPTANCE_GATE_BUILT_VALUE_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A6-DIMENSIONAL-ANCHOR-PACKET",
        "required_fields": {
            "candidate_id": "non-null selected branch id",
            "source_branch": "same selected branch as rho_UV/Z448/q79 and the U1Y weak-split row",
            "dimensionful_quantity.symbol": "one of Omega0, ell_p, kappa_11, alpha_prime, or equivalent modal-gap unit",
            "dimensionful_quantity.value": "target-independent physical value with units",
            "source_certification.selected_by_mtt": True,
            "source_certification.computed_before_target_comparison": True,
            "source_certification.same_branch_as_rho_uv_and_z448": True,
            "map_to_alpha_phys.formula": "declared convention map to alpha_phys",
            "map_to_alpha_phys.alpha_phys_value": "computed from the selected anchor, not backsolved",
            "map_to_alpha_phys.dimensional_analysis_checked": True,
            "map_to_alpha_phys.convention_factors_declared": True,
        },
        "forbidden_inputs_absent_must_be_true": [
            "observed_Newton_or_Planck",
            "observed_Omega0_H0_rhoDE",
            "observed_particle_masses_or_TeV_calibration",
            "unit_convention_only",
            "observed_alpha_EM_or_weak_angle",
            "observed_alpha_s_or_SM_fit",
        ],
        "import_checks": import_checks,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    routes = {
        "schema": "MTTConstEM01DimensionalAnchorRouteMatrix.v1",
        "status": "BEST_ROUTE_SELECTED_VALUE_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A6-DIMENSIONAL-ANCHOR-PACKET",
        "route_matrix": anchor_search["route_table"],
        "selected_route_for_next_attack": "m_theory_modal_gap_planck_anchor",
        "reason": (
            "It is the only imported route that already aligns the selected compactification/modal branch "
            "with both the Planck/action slot and gauge kinetic normalization slot."
        ),
        "superset_strategy": {
            "combined_paths": [
                "individual constants alpha1 gate",
                "QA/SU3 electroweak weak-split gate",
                "protospinor GR one-anchor/metrology gate",
                "M-theory modal-gap compactification slot",
            ],
            "locked_target": "a single selected dimensional anchor packet, not separately tuned constants",
            "not_allowed": "using measured alpha, Newton, Planck, masses, or cosmology to choose the packet",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    promotion = {
        "schema": "MTTConstEM01DimensionalAnchorPromotionTests.v1",
        "status": "PROMOTION_TESTS_BUILT_VALUE_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A6-DIMENSIONAL-ANCHOR-PACKET",
        "current_packet": {
            "candidate_id": mtheory_attempt["candidate_id"],
            "structural_slot_filled": True,
            "value_present": mtheory_attempt["dimensionful_quantity"]["value"] is not None,
            "selected_by_mtt": mtheory_attempt["source_certification"]["selected_by_mtt"],
            "computed_before_target_comparison": mtheory_attempt["source_certification"]["computed_before_target_comparison"],
            "alpha_phys_value_present": mtheory_attempt["map_to_alpha_phys"]["alpha_phys_value"] is not None,
        },
        "must_be_true_for_promotion": [
            "dimensionful_quantity.value is not null",
            "source_certification.selected_by_mtt is true",
            "source_certification.computed_before_target_comparison is true",
            "map_to_alpha_phys.alpha_phys_value is not null",
            "all forbidden_inputs_absent entries are true",
            "same-branch electroweak gauge kinetic map is declared before measured comparison",
        ],
        "promotion_now": False,
        "why_not": "The structural M-theory packet exists, but the physical modal-gap/ell_p/kappa11 value is not selected by current sources.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1DimensionalAnchorPacketGate",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A6-DIMENSIONAL-ANCHOR-PACKET",
        "output_packets": {
            "acceptance_criteria": rel(ACCEPTANCE),
            "route_matrix": rel(ROUTES),
            "promotion_tests": rel(PROMOTION),
        },
        "theorem": {
            "name": "CONSTEM01DimensionalAnchorPacketGateTheorem",
            "proved": all(import_checks.values()),
            "statement": (
                "The post-K_phys alpha1 physical-normalization problem is equivalent to filling a SelectedDimensionalAnchorPacket "
                "with a same-branch target-independent physical unit. The M-theory modal-gap Planck/action route is the selected "
                "structural route, but current sources do not supply the required dimensionful value."
            ),
        },
        "what_closes_now": {
            "acceptance_gate": True,
            "route_selection_for_next_attack": "m_theory_modal_gap_planck_anchor",
            "promotion_tests": True,
            "superset_paths_unified": True,
        },
        "what_remains_open": {
            "dimensionful_anchor_value": True,
            "alpha_phys_value": True,
            "K_phys_value": True,
            "electroweak_matching_scale": True,
            "RG_threshold_scheme": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_DimensionalAnchorPacketGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selected_route_for_next_attack": "m_theory_modal_gap_planck_anchor",
        "acceptance_gate_built": True,
        "physical_value_claimed": False,
        "alpha_phys_value_claimed": False,
        "K_phys_value_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Dimensional Anchor Packet Gate v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A6-DIMENSIONAL-ANCHOR-PACKET`

## Result

The next gate is now exact: alpha1 physical normalization can promote only if a
`SelectedDimensionalAnchorPacket` supplies a same-branch target-independent
physical unit and maps it to `alpha_phys`.

Selected route for the next attack:

`m_theory_modal_gap_planck_anchor`

This uses the superset strategy in a constrained way: the individual-constant
alpha1 row, QA/SU3 electroweak row, GR one-anchor metrology row, and M-theory
modal-gap row are combined only into one locked target: the selected dimensional
anchor packet. They are not independent knobs.

## Promotion Tests

The packet must supply:

- `dimensionful_quantity.value`,
- `source_certification.selected_by_mtt = true`,
- `source_certification.computed_before_target_comparison = true`,
- `map_to_alpha_phys.alpha_phys_value`,
- all no-backsolve forbidden-input checks.

## Boundary

The current M-theory packet fills the structural slot but not the physical
value. Therefore no value is claimed for `alpha_phys`, `K_phys`, `Omega0`,
`ell_p`, `kappa_11`, `alpha(0)`, or `alpha(M_Z)`.
"""

    for path, payload in [(ACCEPTANCE, acceptance), (ROUTES, routes), (PROMOTION, promotion), (OUTPUT, candidate), (CERT, cert)]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
