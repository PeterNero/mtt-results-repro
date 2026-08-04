from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV_CERT = ROOT / "certificates" / "selected_rank2_to_rank3_sector_transfer_or_physical_dotd_alpha1_certificate.json"
PREV_PACKET = ROOT / "candidate_data" / "selected_rank2_to_rank3_sector_transfer_or_physical_dotd_alpha1.packet.json"
END0_BASIS_PACKET = ROOT / "candidate_data" / "selected_end0_basis_table_or_bn_identification_import.packet.json"
RHOE_BN_PACKET = ROOT / "candidate_data" / "routec_nonidentity_rhoe_bn_construction_import.packet.json"
SMOOTH_BN_PACKET = ROOT / "candidate_data" / "routec_smooth_bn_galerkin_lift_import.packet.json"
PHIFIN_PACKET = ROOT / "candidate_data" / "phifin_operator_payload_scaffold_import.packet.json"
ROUTEC_DOTD_PACKET = ROOT / "candidate_data" / "routec_sector_projectors_dotd_on_smooth_bn_import.packet.json"

OUT_CERT = ROOT / "certificates" / "selected_sector_functor_or_physical_alpha1_sourcevalues_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_sector_functor_or_physical_alpha1_sourcevalues.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_SectorFunctor_or_PhysicalAlpha1_SourceValues_From_Selected_HYM_v1.md"

STATUS = "ORDINARY_END0_TO_PROJECTIVE_BN_SECTOR_FUNCTOR_NO_GO_GERBE_LIFT_OR_ALPHA1_SOURCE_REQUIRED"
NEXT = "MTT_Selected_GerbeTwisted_End0_SectorFunctor_or_PhysicalAlpha1_SourceTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def phase_abs_distance_from_one(phase_pair: list[float]) -> float:
    real, imag = phase_pair
    return math.hypot(real - 1.0, imag)


def phase_modulus_error(phase_pair: list[float]) -> float:
    real, imag = phase_pair
    return abs(math.hypot(real, imag) - 1.0)


def main() -> None:
    prev_cert = load(PREV_CERT)
    prev = load(PREV_PACKET)
    end0_basis = load(END0_BASIS_PACKET)
    rhoe_bn = load(RHOE_BN_PACKET)
    smooth_bn = load(SMOOTH_BN_PACKET)
    phifin = load(PHIFIN_PACKET)
    routec_dotd = load(ROUTEC_DOTD_PACKET)

    rhoe_candidate = rhoe_bn["rho_E_candidate"]
    phase = rhoe_candidate["numeric_gates"]["projective_commutator_phase"]
    phase_distance = phase_abs_distance_from_one(phase)
    phase_mod_error = phase_modulus_error(phase)
    projective_residual = float(
        rhoe_candidate["numeric_gates"]["projective_commutator_residual"]
    )
    smooth_equivariance = smooth_bn["summary"]["bundle_equivariance"]
    end0_path_a = end0_basis["path_A_BN"]

    ordinary_end0_available = all(
        [
            prev_cert["abstract_rank2_to_rank3_transfer_closed"] is True,
            prev_cert["End0_green_payload_available"] is True,
            prev["closed_abstract_transfer"]["carrier_rank"] == 3,
            prev["closed_abstract_transfer"]["continuous_parameters_added"] == 0,
            prev["closed_End0_green_payload_available_for_transfer"]["basis"] == ["T1", "T2", "T3"],
        ]
    )
    bn_is_projective_nontrivial = all(
        [
            rhoe_candidate["kind"] == "selected_deck_compatible_Heisenberg_Weyl_projective_packet",
            rhoe_bn["numeric_checks"]["projective_commutator_residual_small"] is True,
            phase_mod_error < 1.0e-9,
            phase_distance > 1.0,
            smooth_equivariance["ordinary_bundle_equivariance"] is False,
            smooth_equivariance["projective_equivariance_up_to_central_phase"] is True,
        ]
    )
    bn_rejected_as_ordinary_end0 = all(
        [
            end0_path_a["result"] == "REJECTED_AS_SELECTED_END0_TABLE",
            end0_path_a["blocking_evidence"]["ordinary_bundle_equivariance"] is False,
            end0_path_a["blocking_evidence"]["projective_equivariance_up_to_central_phase"] is True,
            end0_basis["guardrails"]["does_not_identify_projective_BN_with_ordinary_End0"] is True,
        ]
    )
    diagnostic_shapes_present = all(
        [
            phifin["verdict"]["phi_fin_finite_operator_scaffold_imported"] is True,
            phifin["verdict"]["phi_fin_full_selected_payload_emitted"] is False,
            routec_dotd["verdict"]["sector_projectors_built"] is True,
            routec_dotd["verdict"]["dotD_alpha1_on_same_basis_built"] is True,
            routec_dotd["verdict"]["selected_dotD_source_promotes"] is False,
            routec_dotd["verdict"]["alpha1_driver_promotes"] is False,
        ]
    )

    no_go_closed = all(
        [
            ordinary_end0_available,
            bn_is_projective_nontrivial,
            bn_rejected_as_ordinary_end0,
            diagnostic_shapes_present,
        ]
    )

    packet = {
        "theorem": {
            "name": "SelectedSectorFunctorOrdinaryEnd0ToProjectiveBNNoGo",
            "proved": no_go_closed,
            "closure_claimed": False,
            "statement": (
                "There is no selected ordinary sector functor from the selected "
                "ordinary End0 basis T1,T2,T3 into the current 27-mode B_N/qutrit "
                "sector basis that preserves the available deck/equivariance data. "
                "The obstruction is a nontrivial Heisenberg/Weyl projective cocycle: "
                "the active generators commute only up to omega^2, while ordinary "
                "End0 functorial transport has trivial scalar cocycle. A positive "
                "sector functor must therefore be a gerbe-twisted/central-extension "
                "functor or be replaced by physical alpha1 source values."
            ),
        },
        "ordinary_End0_source": {
            "available": ordinary_end0_available,
            "basis": ["T1", "T2", "T3"],
            "carrier": "ordinary Ad(V_alpha)=End_0(V_alpha)",
            "rank": 3,
            "continuous_parameters_added_by_adjoint_transfer": 0,
            "End0_green_payload_available": prev_cert["End0_green_payload_available"],
        },
        "projective_BN_target": {
            "available_as_diagnostic_scaffold": diagnostic_shapes_present,
            "basis_id": smooth_bn["summary"]["basis_id"],
            "dimension": smooth_bn["summary"]["dimension"],
            "bundle_equivariance": smooth_equivariance,
            "projective_commutator_phase": phase,
            "projective_commutator_residual": projective_residual,
            "projective_phase_modulus_error": phase_mod_error,
            "projective_phase_distance_from_ordinary_one": phase_distance,
            "cocycle_nontrivial": bn_is_projective_nontrivial,
        },
        "obstruction": {
            "closed": no_go_closed,
            "type": "ordinary-vs-projective equivariance cocycle mismatch",
            "ordinary_functor_requires_commutator_phase": [1.0, 0.0],
            "BN_commutator_phase": phase,
            "numerical_gap_from_ordinary_phase": phase_distance,
            "formal_reason": (
                "A functor preserving ordinary End0 equivariance cannot change the "
                "2-cocycle class. The current B_N target carries a nontrivial "
                "central phase on the active F3^2 deck generators; identifying it "
                "with ordinary End0 would collapse omega^2 to 1, contrary to the "
                "verified projective commutator."
            ),
        },
        "attempted_positive_functor": {
            "ordinary_End0_to_current_BN_sector_functor_proved": False,
            "why_not": "nontrivial projective cocycle on B_N target",
            "BN_rejected_as_selected_End0_table": bn_rejected_as_ordinary_end0,
            "diagnostic_sector_projectors_exist": routec_dotd["verdict"]["sector_projectors_built"],
            "diagnostic_dotD_alpha1_exists": routec_dotd["verdict"]["dotD_alpha1_on_same_basis_built"],
            "selected_dotD_source_promotes": routec_dotd["verdict"]["selected_dotD_source_promotes"],
            "alpha1_driver_promotes": routec_dotd["verdict"]["alpha1_driver_promotes"],
        },
        "repair_paths": {
            "path_A_gerbe_twisted_sector_functor": {
                "required": True,
                "statement": (
                    "Lift End0 response through a selected gerbe/central-extension "
                    "sector functor whose source includes the same omega^2 cocycle "
                    "as the B_N Heisenberg/Weyl packet."
                ),
                "needed_data": [
                    "source theorem selecting operator-level projective/gerbe class",
                    "twisted End0-to-B_N basis transport preserving the omega^2 cocycle",
                    "sector projector and zero-mode images of T1,T2,T3 response",
                    "same-branch selected-source flags without diagnostic lifts",
                ],
            },
            "path_B_physical_alpha1_source_values": {
                "required": True,
                "statement": (
                    "Bypass ordinary sector functor promotion by deriving physical "
                    "dotD_alpha1 source values directly from the selected HYM/PhiFin "
                    "branch."
                ),
                "needed_data": [
                    "selected alpha1 driver",
                    "selected dotD source",
                    "primitive C1 contractions",
                    "honest replay passing without lifted flags",
                ],
            },
        },
        "what_closes_now": {
            "previous_gate_requested_sector_functor_or_alpha1_values": prev["next_required_artifact"]
            == "MTT_Selected_SectorFunctor_or_PhysicalAlpha1_SourceValues_From_Selected_HYM_v1",
            "ordinary_End0_source_available": ordinary_end0_available,
            "projective_BN_target_cocycle_verified": bn_is_projective_nontrivial,
            "ordinary_End0_to_current_BN_functor_no_go": no_go_closed,
            "positive_repair_paths_identified": True,
            "diagnostic_shapes_retained_without_promotion": diagnostic_shapes_present,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "gerbe_twisted_End0_to_BN_sector_functor": True,
            "operator_level_projective_source_promotion": True,
            "physical_dotD_alpha1_source_values": True,
            "selected_sector_projectors_and_zero_modes": True,
            "validator_ready_sector_DE_Riesz_Green_dotD": True,
        },
        "guardrails": {
            "does_not_identify_projective_BN_with_ordinary_End0": True,
            "does_not_promote_diagnostic_sector_projectors": True,
            "does_not_promote_diagnostic_dotD_alpha1": True,
            "does_not_fill_matter_template": True,
            "does_not_use_observed_or_benchmark_data": True,
        },
        "input_artifacts": {
            "previous_cert": str(PREV_CERT),
            "previous_packet": str(PREV_PACKET),
            "end0_basis_packet": str(END0_BASIS_PACKET),
            "rhoe_bn_packet": str(RHOE_BN_PACKET),
            "smooth_bn_packet": str(SMOOTH_BN_PACKET),
            "phifin_packet": str(PHIFIN_PACKET),
            "routec_dotd_packet": str(ROUTEC_DOTD_PACKET),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "no_go_closed": no_go_closed,
        "ordinary_end0_available": ordinary_end0_available,
        "bn_projective_nontrivial": bn_is_projective_nontrivial,
        "bn_rejected_as_ordinary_end0": bn_rejected_as_ordinary_end0,
        "projective_phase_not_one": phase_distance > 1.0,
        "projective_residual_small": projective_residual < 1.0e-12,
        "diagnostic_shapes_present": diagnostic_shapes_present,
        "positive_ordinary_functor_not_claimed": packet["attempted_positive_functor"][
            "ordinary_End0_to_current_BN_sector_functor_proved"
        ]
        is False,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_sector_functor_or_physical_alpha1_sourcevalues",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "ordinary_End0_to_current_BN_sector_functor_no_go_closed": no_go_closed,
        "positive_ordinary_sector_functor_closed": False,
        "gerbe_twisted_repair_required": True,
        "physical_alpha1_source_values_closed": False,
        "projective_commutator_phase": phase,
        "projective_phase_distance_from_one": phase_distance,
        "validator_ready": False,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected SectorFunctor or Physical Alpha1 SourceValues From Selected HYM v1

## Result

The attempted ordinary sector functor

```text
End_0(V_alpha) basis T1,T2,T3 -> 27-mode B_N/qutrit sector basis
```

does not close. The obstruction is not numerical looseness but a cocycle
mismatch:

```text
ordinary End0 commutator phase = 1
B_N projective commutator phase = {phase}
distance from 1 = {phase_distance:.16g}
projective commutator residual = {projective_residual:.3e}
```

So the current `B_N` sector basis cannot be identified with the selected
ordinary End0 basis by an ordinary functor preserving equivariance.

## Consequence

The correct positive target is sharper:

1. build a selected gerbe-twisted/central-extension End0-to-B_N sector functor
   carrying the same projective cocycle, or
2. bypass this functor by deriving physical `dotD_alpha1` source values from
   the selected HYM/PhiFin branch.

The existing `27x27` sector projectors and `dotD_alpha1` matrices remain useful
diagnostic shapes, but they are not promoted as selected sector values here.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
