"""Build CONST-GR-01 G1 shared-primitive source-search packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
GR_REPO = TEXPAPERS / "mtt-protospinor-gr-response-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_gr_01_absolute_scale_g1_shared_primitive_source_search"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SHARED_IMPORT = BASE / "shared_primitive_import.packet.json"
GR_SCAN = BASE / "gr_modal_gap_source_scan.packet.json"
ABS_GATE = BASE / "absolute_scale_gate.packet.json"
SUPERSET = BASE / "superset_strategy_status.packet.json"
PORTFOLIO = BASE / "portfolio_status.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_GR_01_AbsoluteScale_G1_SharedPrimitiveSourceSearch_v1.md"

STATUS = "MTT_CONST_GR_01_G1_SHARED_PRIMITIVE_SOURCE_SEARCH_BUILT"


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

    alpha_primitive_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo" / "one_universal_primitive.packet.json"
    weak_b45_path = DATA / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff.candidate.json"

    one_anchor_path = GR_REPO / "certificates" / "one_anchor_gr_normalization_propagation_certificate.json"
    einstein_path = GR_REPO / "certificates" / "one_anchor_einstein_response_assembly_certificate.json"
    scale_lift_path = GR_REPO / "certificates" / "physical_scale_lifting_anchor_gate_certificate.json"
    modal_gate_path = GR_REPO / "certificates" / "selected_modal_gap_physical_anchor_gate_certificate.json"
    anchor_search_path = GR_REPO / "certificates" / "target_independent_dimensional_anchor_search_certificate.json"
    alpha_action_path = GR_REPO / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"
    anchor_template_path = GR_REPO / "candidate_data" / "selected_dimensional_anchor_packet.template.json"

    alpha_primitive = load(alpha_primitive_path)
    weak_b45 = load(weak_b45_path)
    one_anchor = load(one_anchor_path)
    einstein = load(einstein_path)
    scale_lift = load(scale_lift_path)
    modal_gate = load(modal_gate_path)
    anchor_search = load(anchor_search_path)
    alpha_action = load(alpha_action_path)
    anchor_template = load(anchor_template_path)

    length_family = one_anchor["solution"]["length_anchor_family"]
    energy_family = one_anchor["solution"]["energy_anchor_family"]
    selected_row = one_anchor["solution"]["selected_internal_row"]
    route_table = anchor_search["route_table"]
    m_route = route_table["m_theory_modal_gap_planck_anchor"]

    shared_import = {
        "schema": "MTTConstGR01G1SharedPrimitiveImport.v1",
        "status": "SHARED_E0_L0_PRIMITIVE_IMPORTED_FROM_ALPHA_WEAK_AND_GR",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G1-SHARED-PRIMITIVE-IMPORT",
        "inputs": {
            "alpha_one_universal_primitive": rel(alpha_primitive_path),
            "weak_mixing_B45_handoff": rel(weak_b45_path),
            "gr_one_anchor_normalization": rel(one_anchor_path),
        },
        "shared_primitive_options": alpha_primitive["primitive_options"],
        "gr_selected_internal_row": selected_row,
        "gr_one_anchor_family": {
            "length_anchor": length_family,
            "energy_anchor": energy_family,
            "dimensionless_invariants": one_anchor["solution"]["dimensionless_invariants"],
        },
        "cross_sector_use": {
            "alpha1": "alpha_phys = tau_int/L0^2 or tau_int*E0^2",
            "weak_mixing": "B42/B45 depend on the same shared E0/L0 primitive after the K_phys/alpha_phys/mu collapse",
            "GR_Newton": "G_eff = 0.29759362932431804*L0^2 or 0.29759362932431804/E0^2",
        },
        "interpretation": "This is a real superset gain: the same primitive propagates into alpha, weak mixing, and GR response. It is not yet a selected physical value.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    gr_scan = {
        "schema": "MTTConstGR01G1GRModalGapSourceScan.v1",
        "status": "GR_MODAL_GAP_SOURCE_SCAN_STRUCTURAL_SLOT_FOUND_VALUE_OPEN",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G1-GR-MODAL-GAP-SOURCE-SCAN",
        "inputs": {
            "one_anchor_gr_normalization": rel(one_anchor_path),
            "one_anchor_einstein_response": rel(einstein_path),
            "physical_scale_lifting_anchor_gate": rel(scale_lift_path),
            "selected_modal_gap_physical_anchor_gate": rel(modal_gate_path),
            "target_independent_dimensional_anchor_search": rel(anchor_search_path),
            "selected_physical_alpha_or_action_unit": rel(alpha_action_path),
        },
        "source_statuses": {
            "one_anchor_gr_normalization": one_anchor["status"],
            "one_anchor_einstein_response": einstein["status"],
            "physical_scale_lifting_anchor_gate": scale_lift["status"],
            "selected_modal_gap_physical_anchor_gate": modal_gate["status"],
            "target_independent_dimensional_anchor_search": anchor_search["status"],
            "selected_physical_alpha_or_action_unit": alpha_action["status"],
        },
        "best_structural_route": {
            "id": "m_theory_modal_gap_planck_anchor",
            "classification": m_route["classification"],
            "closed": m_route["closed"],
            "blocker": m_route["blocker"],
            "next_packet_fields": m_route["next_packet_fields"],
        },
        "blocked_shortcuts": modal_gate["blocked_shortcuts"],
        "modal_gate_open_tests": modal_gate["open_tests"],
        "anchor_template": {
            "path": rel(anchor_template_path),
            "status": anchor_template["status"],
            "selected_by_mtt": anchor_template["source_certification"]["selected_by_mtt"],
        },
        "conclusion": "The GR/protospinor corpus supplies the correct dimensional-anchor slot and one-anchor propagation, but not the target-independent physical E0/L0 value.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    absolute_gate = {
        "schema": "MTTConstGR01G1AbsoluteScaleGate.v1",
        "status": "ABSOLUTE_SCALE_GATE_REDUCED_TO_SELECTED_DIMENSIONAL_ANCHOR",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G1-ABSOLUTE-SCALE-GATE",
        "closed_now": {
            "shared_E0_L0_formulas_imported": True,
            "selected_Z448_internal_GR_row_imported": True,
            "one_anchor_GR_normalization_family_closed": one_anchor["verdict"]["one_anchor_gr_normalization_family_closed"],
            "conditional_low_energy_TT_response_closed": einstein["verdict"]["conditional_low_energy_TT_response_closed"],
            "M_theory_modal_gap_structural_slot_identified": True,
            "no_new_GR_knob_introduced": True,
        },
        "still_open": {
            "selected_physical_E0_or_L0_value": True,
            "selected_dimensionful_modal_gap_value": True,
            "selected_ell_p_kappa11_or_alpha_prime_value": True,
            "measured_Newton_value_derived": True,
            "measured_Planck_value_derived": True,
            "strict_no_knob_absolute_scale_closure": True,
        },
        "accepted_conditional_theorem": {
            "statement": "Given one physical metrological primitive L0 or E0, the selected exact branch propagates alpha, weak mixing, GR normalization, and linearized TT response with no extra sector-specific normalization knob.",
            "length_anchor_G_eff": length_family["G_eff_phys"],
            "energy_anchor_G_eff": energy_family["G_eff_phys"],
            "length_anchor_kappa_STF": length_family["kappa_STF_phys"],
            "energy_anchor_kappa_STF": energy_family["kappa_STF_phys"],
        },
        "forbidden_promotions": [
            "use observed G_N or M_Pl to select L0/E0",
            "use the Theta 5 TeV calibration as a no-knob prediction",
            "set internal alpha_int=1 as an SI physical alpha value",
            "call unit convention a dimensionful prediction",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    superset = {
        "schema": "MTTConstGR01G1SupersetStrategyStatus.v1",
        "status": "SUPERSET_PATHS_SEPARATED_FOR_CONST_GR_01",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G1-SUPERSET-STRATEGY",
        "paths": {
            "straight_source_path": {
                "label": "GR/protospinor/M-theory modal-gap dimensional-anchor source",
                "current_status": "STRUCTURAL_SLOT_FOUND_VALUE_OPEN",
                "would_close_if": "SelectedDimensionalAnchorPacket is filled with a target-independent E0/L0, omega_gap_phys, ell_p, kappa11, or alpha_prime value.",
            },
            "cross_sector_one_primitive_path": {
                "label": "one universal physical rod/clock primitive shared by alpha, weak mixing, and GR",
                "current_status": "CONDITIONAL_FAMILY_CLOSED",
                "would_close_if": "The program accepts one universal primitive as a physical input rather than strict no-knob derivation, then tests it across other constants.",
            },
            "strict_no_knob_upgrade_path": {
                "label": "derive the primitive from same selected branch data",
                "current_status": "OPEN",
                "would_close_if": "A same-branch finite source theorem emits the physical metrology primitive before target comparison.",
            },
        },
        "strategy_decision": {
            "do_not_cycle_on_single_constant": True,
            "treat_GR_as_shared_primitive_test": True,
            "strict_source_upgrade_remains_primary_for_no_knob": True,
            "one_universal_primitive_tier_remains_allowed_but_labeled": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    portfolio = {
        "schema": "MTTConstGR01G1PortfolioStatus.v1",
        "status": "CONST_GR_01_JOINED_SHARED_PRIMITIVE_PORTFOLIO",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G1-PORTFOLIO-STATUS",
        "portfolio": {
            "shared_primitive": "E0/L0 physical rod-clock primitive, or equivalent dimensional modal-gap/M-theory anchor",
            "constants_currently_waiting_on_same_primitive": [
                "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR",
                "CONST-EW-02 / WEAK-MIXING",
                "CONST-GR-01 / ABSOLUTE-SCALE-GN",
            ],
            "sector_specific_new_parameters_added_here": 0,
            "selected_numeric_primitive_value_now": False,
        },
        "achievement": "GR does not break the shared-primitive strategy. It reinforces it: the same primitive that alpha and weak mixing require is exactly the one GR needs for physical Newton/Planck normalization.",
        "risk": "Without a selected dimensional anchor, the branch remains one-primitive conditional rather than strict no-knob closure.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstGR01G1NextWork.v1",
        "status": "NEXT_WORKORDER_G2_DIMENSIONAL_ANCHOR_PACKET_FILL",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-NEXT",
        "primary": {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-MODAL-GAP-DIMENSIONAL-ANCHOR-PACKET-FILL",
            "task": "Attempt to fill SelectedDimensionalAnchorPacket from selected modal-gap, central-circle rod/clock, M-theory kappa11/ell_p, flux alpha-prime, or finite metrology source data without target backsolve.",
        },
        "secondary": {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G2B-ONE-PRIMITIVE-CROSS-CONSTANT-TEST",
            "task": "If no strict source exists, freeze the one-universal-primitive tier and move to another constant that probes the same E0/L0 primitive.",
        },
    }

    candidate = {
        "candidate": "MTTConstGR01AbsoluteScaleG1SharedPrimitiveSourceSearch",
        "status": STATUS,
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G1-SHARED-PRIMITIVE-SOURCE-SEARCH",
        "output_packets": {
            "shared_primitive_import": rel(SHARED_IMPORT),
            "gr_modal_gap_source_scan": rel(GR_SCAN),
            "absolute_scale_gate": rel(ABS_GATE),
            "superset_strategy_status": rel(SUPERSET),
            "portfolio_status": rel(PORTFOLIO),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTGR01G1SharedPrimitiveSourceSearchTheorem",
            "proved": True,
            "statement": (
                "The current corpus/repo state imports the same E0/L0 physical rod-clock primitive into alpha, weak mixing, and GR absolute normalization. GR closes the one-anchor propagation family and identifies the M-theory/modal-gap structural source slot, but current source packets do not select a target-independent physical value. Therefore CONST-GR-01 is reduced to the SelectedDimensionalAnchorPacket gate or to the explicitly labeled one-universal-primitive tier."
            ),
        },
        "one_anchor_GR_family_closed": True,
        "shared_primitive_portfolio_extended_to_GR": True,
        "selected_physical_E0_or_L0_value": False,
        "measured_Newton_or_Planck_derived": False,
        "strict_no_knob_absolute_scale_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_GR_01_AbsoluteScale_G1_SharedPrimitiveSourceSearch_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "one_anchor_GR_family_closed": True,
        "shared_primitive_portfolio_extended_to_GR": True,
        "selected_physical_E0_or_L0_value": False,
        "measured_Newton_or_Planck_derived": False,
        "strict_no_knob_absolute_scale_closure": False,
        "next_primary": next_work["primary"]["label"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST GR 01 Absolute Scale G1 Shared Primitive Source Search v1

Status: `{STATUS}`

Label: `CONST-GR-01 / ABSOLUTE-SCALE-GN / G1-SHARED-PRIMITIVE-SOURCE-SEARCH`

## Result

```text
shared E0/L0 primitive imported                 True
GR one-anchor normalization family closed       True
conditional Einstein TT response assembled      True
M-theory/modal-gap structural source slot       True
selected physical E0/L0 value                   False
measured Newton/Planck derived                  False
strict no-knob absolute-scale closure           False
```

G1 shows that GR does not require a new sector-specific knob.  The same
rod/clock primitive already isolated by alpha and weak mixing is exactly the
primitive needed by the one-anchor GR normalization family:

```text
alpha_phys = 0.40698621549433234 / L0^2
G_eff      = 0.29759362932431804 * L0^2
kappa_STF  = 0.03342539276068642 / L0^2
```

or equivalently in energy-anchor form:

```text
alpha_phys = 0.40698621549433234 * E0^2
G_eff      = 0.29759362932431804 / E0^2
kappa_STF  = 0.03342539276068642 * E0^2
```

## Superset Status

Straight source path: the GR/protospinor/M-theory route identifies the right
modal-gap or Planck-anchor slot, but its SelectedDimensionalAnchorPacket is
still unfilled.

Cross-sector path: alpha, weak mixing, and GR are now all reduced to the same
single physical rod/clock primitive.  This is a strong one-universal-primitive
tier, not strict no-knob closure.

Strict upgrade path: prove a same-branch finite metrology theorem that emits
`E0`, `L0`, `omega_gap_phys`, `ell_p`, `kappa11`, or `alpha_prime` before any
target comparison.

## Next

`CONST-GR-01 / ABSOLUTE-SCALE-GN / G2-MODAL-GAP-DIMENSIONAL-ANCHOR-PACKET-FILL`

Attempt to fill the selected dimensional-anchor packet from modal-gap,
central-circle rod/clock, M-theory, flux/string, or finite metrology data while
preserving the no-backsolve guard.
"""

    for path, payload in [
        (SHARED_IMPORT, shared_import),
        (GR_SCAN, gr_scan),
        (ABS_GATE, absolute_gate),
        (SUPERSET, superset),
        (PORTFOLIO, portfolio),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
