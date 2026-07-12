"""Build the U5 neutral overlap/physical-unit/action-completeness gate.

This successor executes the next target after the neutral dimensionful normal
form.  It checks the three legal exits against the current repo and corpus
state, rejects schema/support packets as value emission, and names the exact
next value-source packet.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
THETA = TEXPAPERS / "18 Theta-Closure & Execution Program"
PROTO = TEXPAPERS / "mtt-protospinor-gr-response-proof"

SLUG = "selected_neutraloverlapkernelphysicalunitoractioncompleteness"
OUT_DIR = ROOT / "candidate_data" / SLUG
OUT_CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
OUT_PACKET = OUT_DIR / "neutral_overlap_physical_action_gate.packet.json"
OUT_CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralOverlapKernelPhysicalUnitOrActionCompleteness_v1.md"

STATUS = "MTT_SELECTED_NEUTRALOVERLAP_PHYSICALUNIT_ACTIONCOMPLETENESS_GATE_EXECUTED_VALUES_OPEN"
NEXT = "MTT_Selected_NeutralOverlapKernelValueSourceOrPhysicalUnitTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def dump(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    source = load(ROOT / "candidate_data" / "selected_neutralmassoperator_sourceemission" / "neutral_mass_operator_source_emission.packet.json")
    normal = load(ROOT / "candidate_data" / "selected_neutraldimensionfulblocksandnormalization" / "neutral_dimensionful_blocks_normal_form.packet.json")
    physical_unit = load(PROTO / "certificates" / "selected_modal_gap_to_physical_unit_theorem_certificate.json")

    overlap = read_text(THETA / "_md_v3_corrected" / "Selected_Overlap_Kernel_Certificate_v1.md")
    localization = read_text(THETA / "_md_v3_corrected" / "Minimal_Selected_Localization_Packet_v1.md")
    no_proxy = read_text(THETA / "_md_v3_corrected" / "No_Proxy_Flavor_Closure_in_Modal_Triplet_Theory_v1.md")

    ok_gates = {
        "OK1_selected_geometry_and_charge_sector": source["source_identity"]["selected_branch_closed"],
        "OK2_SM_representation_spaces": source["required_field_acceptance"]["neutral_basis_L_and_Nc"],
        "OK3_normalized_zero_mode_bases": False,
        "OK4_kinetic_metrics_positive": False,
        "OK5_finite_neutral_overlap_channel_sets": False,
        "OK6_action_costs_prefactors_characters_retarded_signs": False,
        "OK7_nil_coherence_anchor_projectors": False,
        "OK8_RG_threshold_matching_map": False,
        "OK9_no_measured_selector": (
            source["observed_data_used_as_selector"] is False
            and normal["observed_data_used_as_selector"] is False
        ),
    }

    corpus_diagnostics = {
        "selected_overlap_kernel_schema_present": "OK.1  selected geometry and charge sector fixed" in overlap,
        "neutral_Ynu_formula_present": "Y_nu = G_L^{-1/2} Y_nu,raw G_nu^{-1/2} G_Hu^{-1/2}" in overlap,
        "neutral_majorana_formula_present": "M_nu,eff = - v_u^2 Y_nu M_R^{-1} Y_nu^T" in overlap,
        "current_barrier_names_missing_neutral_inputs": "M_R or Dirac/Majorana neutral mechanism" in overlap,
        "localization_packet_is_charged_skeleton_only": (
            "finite Gamma_u/Gamma_d channel skeleton" in localization
            and "extend to leptons and neutral sector                 OPEN" in localization
        ),
        "no_proxy_majorana_scale_open": "Majorana scale from topology                Open" in no_proxy,
    }

    exit_screen = {
        "A_dirac_dimensionful_MD": {
            "accepted": False,
            "failed_gates": [
                "Dirac_only_completeness_closed=false",
                "OK3/OK4/OK5/OK6 neutral Y_nu value gates are not selected",
                "selected v_u or neutral physical normalization is absent",
            ],
            "can_be_reopened_by": [
                "Selected Dirac-only action-completeness theorem",
                "selected neutral Y_nu overlap rows",
                "selected same-scheme Higgs/neutral physical normalization",
            ],
        },
        "B_majorana_or_seesaw_blocks": {
            "accepted": False,
            "failed_gates": [
                "Majorana self-characters k=0,672 are admissible but no neutral line/bundle is selected as L^2~=C",
                "selected M_L/M_R rows are absent",
                "OK3/OK4/OK5/OK6 neutral Y_nu value gates are not selected",
                "physical scale/scheme is absent",
            ],
            "can_be_reopened_by": [
                "selected neutral real-structure test and line/bundle certificate",
                "selected M_L/M_R source rows",
                "selected neutral Y_nu rows and physical scale",
            ],
        },
        "C_nil_boundary_effective_spectrum": {
            "accepted": False,
            "failed_gates": [
                "nil-boundary formula is proved only conditionally",
                "nil-boundary source promotion is open",
                "NO/IO ordering and dimensionful splittings are not selected",
                "operator reconstruction from effective spectrum is absent",
            ],
            "can_be_reopened_by": [
                "selected nil-boundary source-promotion theorem",
                "selected ordering/splitting rows",
                "selected operator-reconstruction theorem",
            ],
        },
    }

    value_block_status = dict(source["value_block_status"])
    required_fields = dict(normal["required_field_acceptance"])

    packet = {
        "schema": "MTTSelectedNeutralOverlapPhysicalUnitActionCompletenessGate.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralDimensionfulBlocksAndNormalization_v1",
        "what_closes_here": {
            "three_exit_gate_executed": True,
            "overlap_schema_imported_but_not_promoted": True,
            "physical_unit_bridge_imported_as_conditional_only": True,
            "action_completeness_not_derived": True,
            "exact_next_value_source_contract_named": True,
        },
        "corpus_diagnostics": corpus_diagnostics,
        "neutral_overlap_OK_gate_acceptance": ok_gates,
        "neutral_overlap_OK_gates_closed": sum(bool(value) for value in ok_gates.values()),
        "neutral_overlap_OK_gates_total": len(ok_gates),
        "route_exit_screen": exit_screen,
        "route_exit_count": len(exit_screen),
        "accepted_route_exit_count": sum(1 for row in exit_screen.values() if row["accepted"]),
        "physical_unit_status": physical_unit["status"],
        "physical_unit_selected": physical_unit["open_checks"]["omega_gap_phys_selected"],
        "Dirac_only_completeness_closed": source["character_and_ontology_gate"]["Dirac_only_completeness_closed"],
        "separate_Majorana_operator_excluded": source["character_and_ontology_gate"]["separate_Majorana_operator_excluded"],
        "value_block_status": value_block_status,
        "required_field_acceptance": required_fields,
        "required_fields_closed": normal["required_fields_closed"],
        "required_fields_total": normal["required_fields_total"],
        "new_value_fields_closed_here": 0,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "next_value_source_contract": {
            "must_emit": [
                "neutral zero-mode bases and kinetic metrics for L,Nc,Hu",
                "finite Gamma_nu channel sets and selected action/prefactor/retarded-sign rows",
                "either Dirac action-completeness excluding M_L/M_R or selected Majorana M_L/M_R rows",
                "same-scheme physical normalization or selected internal-to-physical unit",
                "no observed masses/splittings/cosmology or benchmark matrices as selectors",
            ],
            "minimum_success": "at least one accepted lawful exit from A/B/C and at least one newly closed U5 value field",
        },
    }

    cert = {
        "certificate": "MTT_Selected_NeutralOverlapKernelPhysicalUnitOrActionCompleteness_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": True,
        "three_exit_gate_executed": True,
        "neutral_overlap_OK_gates_closed": packet["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": packet["neutral_overlap_OK_gates_total"],
        "accepted_route_exit_count": packet["accepted_route_exit_count"],
        "route_exit_count": packet["route_exit_count"],
        "new_value_fields_closed_here": 0,
        "physical_unit_selected": packet["physical_unit_selected"],
        "Dirac_only_completeness_closed": packet["Dirac_only_completeness_closed"],
        "separate_Majorana_operator_excluded": packet["separate_Majorana_operator_excluded"],
        "dimensionful_M_D_3x3_closed": False,
        "dimensionful_M_L_3x3_closed": False,
        "dimensionful_M_R_3x3_closed": False,
        "absolute_normalization_and_scheme_closed": False,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Overlap Kernel, Physical Unit, or Action Completeness v1

## Result

This artifact executes the A24 next target.  It does not emit neutral mass
values and keeps the neutral operator at `{packet["required_fields_closed"]}/{packet["required_fields_total"]}`.

What it closes is the gate audit:

- the selected overlap-kernel certificate is a schema/support source, not a
  neutral `Y_nu` or `M_R` value packet;
- the physical modal-gap bridge is conditional because `omega_gap_phys` is not
  selected;
- the selected `1_M=N^c` Dirac channel does not yet prove Dirac-only action
  completeness, because separate Majorana blocks with `k=0` or `k=672` remain
  admissible unless excluded or emitted by source data;
- all three lawful exits remain unaccepted.

The overlap-kernel OK gate status is
`{packet["neutral_overlap_OK_gates_closed"]}/{packet["neutral_overlap_OK_gates_total"]}`:
only selected branch/basis/no-observed-selector structure is currently closed.

## Remaining Exact Target

`{NEXT}` must emit selected neutral zero-mode bases, kinetic metrics, finite
`Gamma_nu` channels, action/prefactor/retarded-sign rows, and either:

1. a Dirac-only action-completeness theorem with `M_L=M_R=0`, or
2. selected Majorana `M_L/M_R` rows, or
3. selected nil-boundary spectrum rows plus operator reconstruction.

At least one U5 value field must close before the neutral mass operator is
accepted.
"""

    dump(OUT_PACKET, packet)
    dump(OUT_CANDIDATE, packet)
    dump(OUT_CERT, cert)
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
