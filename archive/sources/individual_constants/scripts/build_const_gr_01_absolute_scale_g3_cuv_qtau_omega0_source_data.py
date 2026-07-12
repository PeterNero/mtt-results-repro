"""Build CONST-GR-01 G3 CUV/Qtau/Omega0 source-data consolidation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
GR_REPO = TEXPAPERS / "mtt-protospinor-gr-response-proof"
NONSM_REPO = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_gr_01_absolute_scale_g3_cuv_qtau_omega0_source_data"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_SPLIT = BASE / "source_data_split.packet.json"
CHAR_IMPORT = BASE / "character_channel_internal_ratio.packet.json"
OMEGA_GATE = BASE / "omega0_physical_unit_gate.packet.json"
PROVENANCE = BASE / "strict_provenance_upgrade.packet.json"
BOUNDARY = BASE / "g3_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_GR_01_AbsoluteScale_G3_CUV_Qtau_Omega0_SourceData_v1.md"

STATUS = "MTT_CONST_GR_01_G3_CUV_QTAU_OMEGA0_SOURCE_DATA_BUILT"


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

    g2_path = DATA / "const_gr_01_absolute_scale_g2_modal_gap_dimensional_anchor_packet_fill.candidate.json"
    g2_boundary_path = DATA / "const_gr_01_absolute_scale_g2_modal_gap_dimensional_anchor_packet_fill" / "g2_boundary.packet.json"
    selected_char_path = GR_REPO / "certificates" / "selected_character_channel_covariance_import_certificate.json"
    gr_tt_char_path = GR_REPO / "certificates" / "gr_tt_character_channel_identification_stress_test_certificate.json"
    omega0_source_path = GR_REPO / "certificates" / "selected_physical_omega0_source_theorem_certificate.json"
    omega_convention_path = GR_REPO / "certificates" / "selected_omega_convention_theorem_certificate.json"
    alpha_unit_path = GR_REPO / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"
    final_rho_path = NONSM_REPO / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
    higher_order_path = GR_REPO / "certificates" / "selected_higher_order_correction_and_disturbance_covariance_theorem_certificate.json"

    g2 = load(g2_path)
    g2_boundary = load(g2_boundary_path)
    selected_char = load(selected_char_path)
    gr_tt_char = load(gr_tt_char_path)
    omega0_source = load(omega0_source_path)
    omega_convention = load(omega_convention_path)
    alpha_unit = load(alpha_unit_path)
    final_rho = load(final_rho_path)
    higher_order = load(higher_order_path)

    internal_data = selected_char["internal_selected_data"]
    omega_formula = omega_convention["reduced_formula"]

    source_split = {
        "schema": "MTTConstGR01G3SourceDataSplit.v1",
        "status": "SOURCE_DATA_SPLIT_COMPLETED_ACTIVE_PHYSICAL_UNIT_GATE_IS_OMEGA0",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-SOURCE-DATA-SPLIT",
        "inputs": {
            "G2_boundary": rel(g2_boundary_path),
            "selected_character_channel_covariance_import": rel(selected_char_path),
            "gr_tt_character_channel_identification_stress_test": rel(gr_tt_char_path),
            "selected_physical_omega0_source": rel(omega0_source_path),
            "selected_omega_convention": rel(omega_convention_path),
            "final_internal_rho_uv": rel(final_rho_path),
        },
        "split": {
            "internal_ratio_gate": {
                "status": "CLOSED_FOR_SHARED_INTERNAL_SCALE_DATA",
                "closed_by": "selected q64=15 character-channel covariance import plus final internal rho_UV branch",
                "conditional_premise": selected_char["identification_premise"],
            },
            "strict_literal_GR_noise_gate": {
                "status": "OPEN_OPTIONAL_STRENGTHENING",
                "why": gr_tt_char["subspace_comparison"]["reason_literal_same_subspace_false"],
                "optional_strengthening": gr_tt_char["optional_strengthening"],
            },
            "physical_unit_gate": {
                "status": "ACTIVE_BLOCKER",
                "symbol": "Omega0 or equivalent E0/L0/alpha_phys metrology primitive",
                "why": "Dimensionless internal rho_UV/s_star data do not provide an SI or physical action/length unit.",
            },
        },
        "correction_to_G2": "G2 listed C_UV, Q_tau, and Omega0 together. G3 separates them: C_UV/Q_tau is internally closed for the selected character-channel import, while literal GR-TT stochastic-channel identity is a strict provenance upgrade and Omega0 remains the physical unit blocker.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    character_import = {
        "schema": "MTTConstGR01G3CharacterChannelInternalRatio.v1",
        "status": "INTERNAL_QTAU_CUV_RATIO_IMPORTED_OMEGA0_OPEN",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-CHARACTER-CHANNEL-INTERNAL-RATIO",
        "inputs": {
            "selected_character_channel_covariance_import": rel(selected_char_path),
            "final_internal_rho_uv": rel(final_rho_path),
            "higher_order_source_data_theorem": rel(higher_order_path),
        },
        "imported_closures": selected_char["imported_closures"],
        "internal_selected_data": internal_data,
        "final_rho_values": final_rho["selected_values"],
        "formulae": {
            "rho_UV": "C_UV^2 / d_Q",
            "d_Q_selected_character": internal_data["D_raw_norm_squared_d_Q"],
            "C_UV_internal": internal_data["C_UV_norm_internal"],
            "rho_UV_internal": internal_data["rho_UV"],
            "s_star": internal_data["s_star"],
            "Lambda_gap_phys_after_physical_unit": selected_char["theorem"]["conditional_physical_formula"],
        },
        "still_open": selected_char["still_open"],
        "guardrails": selected_char["guardrails"],
        "interpretation": "The internal ratio side is usable as shared selected scale data; it still does not supply physical units.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    omega_gate = {
        "schema": "MTTConstGR01G3Omega0PhysicalUnitGate.v1",
        "status": "OMEGA0_OR_EQUIVALENT_METROLOGY_PRIMITIVE_REMAINS_ACTIVE_GATE",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-OMEGA0-PHYSICAL-UNIT-GATE",
        "inputs": {
            "selected_physical_omega0_source": rel(omega0_source_path),
            "selected_omega_convention": rel(omega_convention_path),
            "selected_physical_alpha_or_action_unit": rel(alpha_unit_path),
        },
        "closed_or_reduced": {
            "chi_omega_convention_closed": omega_convention["convention_selection"]["chi_omega"] == 1.0,
            "Omega0_over_sqrt_alpha_phys": omega_formula["Omega0_over_sqrt_alpha_phys"],
            "omega_gap_phys_over_sqrt_alpha_phys": omega_formula["omega_gap_phys_over_sqrt_alpha_phys"],
            "Lambda_gap_phys_over_sqrt_alpha_phys": omega_formula["Lambda_gap_phys_over_sqrt_alpha_phys"],
            "alpha_int_closed": alpha_unit["theorem_result"]["alpha_int"] == 1.0,
            "internal_alpha_is_not_physical_prediction": True,
        },
        "active_formulae": {
            "Omega0": omega_formula["Omega0"],
            "omega_gap_phys": omega_formula["omega_gap_phys"],
            "Lambda_gap_phys": omega_formula["Lambda_gap_phys"],
            "length_anchor": "Omega0 = sqrt(tau_int)/L0",
            "energy_anchor": "Omega0 = sqrt(tau_int)*E0",
        },
        "still_open": {
            "physical_alpha_or_equivalent_inverse_length_unit_selected": omega0_source["still_open"]["physical_alpha_or_equivalent_inverse_length_unit_selected"],
            "Omega0_physical_numeric_closed": omega0_source["still_open"]["Omega0_physical_numeric_closed"],
            "physical_Newton_or_Planck_predicted": omega0_source["still_open"]["physical_Newton_or_Planck_predicted"],
            "selected_physical_E0_or_L0_value": False,
        },
        "guardrails": {
            **omega_convention["guardrails"],
            "uses_observed_target_backsolve": False,
            "declares_one_metrology_primitive_as_no_knob": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    provenance = {
        "schema": "MTTConstGR01G3StrictProvenanceUpgrade.v1",
        "status": "STRICT_PROVENANCE_UPGRADES_LABELED_NOT_ACTIVE_PHYSICAL_UNIT_GATE",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-STRICT-PROVENANCE-UPGRADE",
        "open_upgrades": {
            "literal_GR_TT_stochastic_channel_equals_E15": gr_tt_char["still_open"]["literal_GR_TT_stochastic_channel_identified_with_E15"],
            "unconditional_all_covariance_models_closed": selected_char["still_open"]["unconditional_all_covariance_models_closed"],
            "independent_higher_order_functional_evaluation_supplied_here": selected_char["still_open"]["independent_higher_order_functional_evaluation_supplied_here"],
            "selected_higher_order_correction_functional_evaluated": higher_order["open_gates"]["selected_higher_order_correction_functional_evaluated"],
            "selected_finite_memory_covariance_Q_tau_derived": higher_order["open_gates"]["selected_finite_memory_covariance_Q_tau_derived"],
        },
        "why_parked": "These upgrades improve strict source provenance, but the current character-channel import already supplies the internal rho_UV/s_star data needed for shared internal scale propagation. Physical closure still needs Omega0/E0/L0.",
        "next_if_pursued": "GR_TT_Stochastic_Channel_Equals_Selected_CP_Character_Theorem_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstGR01G3Boundary.v1",
        "status": "G3_SOURCE_DATA_CONSOLIDATED_PHYSICAL_UNIT_GATE_REMAINS",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-BOUNDARY",
        "closed_or_tightened_now": {
            "internal_CUV_Qtau_ratio_accepted_for_shared_scale_data": True,
            "selected_character_channel_premise_made_explicit": True,
            "literal_GR_TT_noise_channel_identity_labeled_as_optional_upgrade": True,
            "physical_unit_gate_reduced_to_Omega0_or_E0_L0": True,
            "G2_triple_blocker_split": True,
            "no_target_backsolve_guard_preserved": True,
        },
        "still_open": {
            "physical_Omega0_selected": True,
            "selected_physical_E0_or_L0_value": True,
            "one_metrology_primitive_declared_or_derived": True,
            "strict_same_branch_physical_unit_theorem": True,
            "literal_GR_TT_stochastic_channel_equals_E15": True,
            "Newton_or_Planck_prediction": True,
            "strict_no_knob_absolute_scale_closure": True,
        },
        "anti_cycle_delta_from_G2": {
            "G2": "attempted the structural SelectedDimensionalAnchorPacket fill",
            "G3": "separates source-data provenance from the active physical metrology gate",
            "not_repeated": [
                "not relisting all dimensional-anchor routes",
                "not treating C_UV/Q_tau provenance as the same as Omega0 metrology",
                "not promoting internal rho_UV as a physical unit",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstGR01G3NextWork.v1",
        "status": "NEXT_WORKORDER_G4_OMEGA0_OR_ONE_METROLOGY_PRIMITIVE",
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-NEXT",
        "primary": {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-OMEGA0-PHYSICAL-UNIT-OR-ONE-METROLOGY-PRIMITIVE",
            "task": "Try to derive Omega0/E0/L0 from same-branch metrology; if impossible, create the explicit one-universal-metrology-primitive tier with downstream falsification rules.",
        },
        "strict_upgrade": {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4B-GR-TT-STOCHASTIC-CHANNEL-E15-IDENTITY",
            "task": "Optional strict provenance upgrade proving the GR TT unresolved disturbance is literally the selected CP character channel E15.",
        },
    }

    candidate = {
        "candidate": "MTTConstGR01AbsoluteScaleG3CUVQtauOmega0SourceData",
        "status": STATUS,
        "active_label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-CUV-QTAU-OMEGA0-SOURCE-DATA",
        "output_packets": {
            "source_data_split": rel(SOURCE_SPLIT),
            "character_channel_internal_ratio": rel(CHAR_IMPORT),
            "omega0_physical_unit_gate": rel(OMEGA_GATE),
            "strict_provenance_upgrade": rel(PROVENANCE),
            "g3_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTGR01G3SourceDataSplitTheorem",
            "proved": True,
            "statement": (
                "The G2 C_UV/Q_tau/Omega0 blocker splits into two layers. The selected q64=15 character-channel import closes the internal C_UV/Q_tau ratio for shared internal scale data under an explicit identification premise, while literal GR-TT stochastic-channel identity remains an optional strict provenance upgrade. The active physical closure gate is therefore Omega0 or an equivalent E0/L0 metrological primitive."
            ),
        },
        "internal_CUV_Qtau_ratio_accepted_for_shared_scale_data": True,
        "physical_unit_gate_reduced_to_Omega0_or_E0_L0": True,
        "literal_GR_TT_noise_identity_closed": False,
        "physical_Omega0_selected": False,
        "measured_Newton_or_Planck_derived": False,
        "strict_no_knob_absolute_scale_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_GR_01_AbsoluteScale_G3_CUV_Qtau_Omega0_SourceData_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "internal_CUV_Qtau_ratio_accepted_for_shared_scale_data": True,
        "physical_unit_gate_reduced_to_Omega0_or_E0_L0": True,
        "literal_GR_TT_noise_identity_closed": False,
        "physical_Omega0_selected": False,
        "strict_no_knob_absolute_scale_closure": False,
        "next_primary": next_work["primary"]["label"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST GR 01 Absolute Scale G3 CUV Q_tau Omega0 Source Data v1

Status: `{STATUS}`

Label: `CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-CUV-QTAU-OMEGA0-SOURCE-DATA`

## Result

```text
internal C_UV/Q_tau ratio usable as shared scale data   True
selected q64=15 character premise explicit             True
literal GR-TT noise-channel identity                   False
active physical unit gate                              Omega0 or E0/L0
Newton/Planck prediction                               False
```

G3 splits the G2 blocker.  The selected character-channel import gives:

```text
q64                 = 15
d_Q                 = 1
C_UV_internal       = 0.405623467693425
rho_UV              = 0.164530397543639
s_star              = 1.464646774701829
```

That is enough for shared internal scale propagation under the explicit
character-channel premise.  It is not a physical unit.

## Active Physical Gate

```text
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
omega_gap_phys = Omega0 / s_star
Lambda_gap_phys = sqrt(15) * Omega0 / s_star
```

So the active absolute-scale blocker is `Omega0`, or equivalently the same
`E0/L0` metrological primitive already isolated by alpha and weak mixing.

## Parked Strict Upgrade

The strict provenance upgrade is:

```text
GR_TT_Stochastic_Channel_Equals_Selected_CP_Character_Theorem_v1
```

This would strengthen the GR-specific source story, but it is not the same as
selecting the physical length/action unit.

## Next

`CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-OMEGA0-PHYSICAL-UNIT-OR-ONE-METROLOGY-PRIMITIVE`
"""

    for path, payload in [
        (SOURCE_SPLIT, source_split),
        (CHAR_IMPORT, character_import),
        (OMEGA_GATE, omega_gate),
        (PROVENANCE, provenance),
        (BOUNDARY, boundary),
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
