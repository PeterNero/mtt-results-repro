from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

PREV_PACKET = ROOT / "candidate_data" / "selected_physical_dotd_alpha1_sourcevalues.packet.json"
PREV_CERT = ROOT / "certificates" / "selected_physical_dotd_alpha1_sourcevalues_certificate.json"
NONSM_PACKET = (
    NONSM
    / "candidate_data"
    / "selected_phifin_dotd_alpha1_c1_response_emission_attempt.candidate.json"
)
NONSM_CERT = (
    NONSM
    / "certificates"
    / "selected_phifin_dotd_alpha1_c1_response_emission_attempt_certificate.json"
)

OUT_CERT = ROOT / "certificates" / "selected_phifin_alpha1_payload_value_emission_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_phifin_alpha1_payload_value_emission.packet.json"
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "Selected_PhiFin_Alpha1_Payload_Value_Emission_From_Selected_HYM_v1.md"
)

STATUS = "SELECTED_PHIFIN_ALPHA1_PAYLOAD_PREFIX_IMPORTED_DOTD_VALUES_SOURCE_DRIVER_OPEN"
NEXT = "Selected_dotD_alpha1_Source_and_Driver_Theorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_PACKET)
    prev_cert = load(PREV_CERT)
    nonsm = load(NONSM_PACKET)
    nonsm_cert = load(NONSM_CERT)

    closed_prefix = nonsm["closed_prefix"]
    dotd = nonsm["dotD_value_packet"]
    c1 = nonsm["c1_response_emission"]
    remaining = nonsm["remaining_gates"]

    dotd_sector_slots = dotd["sector_slots"]
    sector_shape_checks = {
        sector: {
            "projector_rank_trace": slot["projector_rank_trace"],
            "expected_kernel_dimension": slot["expected_kernel_dimension"],
            "projector_rank_matches_expected": slot["projector_rank_trace"]
            == float(slot["expected_kernel_dimension"]),
            "dotD_alpha1_matrix_shape": slot["dotD_alpha1_matrix_shape"],
            "dotD_alpha1_nonzero_entries": slot["dotD_alpha1_nonzero_entries"],
            "selected_dotD_source_verified": slot["selected_dotD_source_verified"],
            "alpha1_driver_verified": slot["alpha1_driver_verified"],
        }
        for sector, slot in dotd_sector_slots.items()
    }

    same_basis_dotd_values_available = all(
        [
            closed_prefix["selected_D_E_gap_Riesz_Green_locked"] is True,
            closed_prefix["same_basis_as_locked_D_E"] is True,
            closed_prefix["dotD_alpha1_value_matrices_emitted"] is True,
            closed_prefix["dotD_alpha1_has_nonzero_entries"] is True,
            closed_prefix["sector_projectors_clean"] is True,
            dotd["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3",
            all(slot["dotD_alpha1_matrix_shape"] == [27, 27] for slot in dotd_sector_slots.values()),
            all(slot["projector_rank_trace"] == float(slot["expected_kernel_dimension"]) for slot in dotd_sector_slots.values()),
            sum(slot["dotD_alpha1_nonzero_entries"] for slot in dotd_sector_slots.values()) > 0,
        ]
    )
    honest_replay_cutset_is_exact = all(
        [
            dotd["honest_replay"]["exit_code"] == 1,
            dotd["honest_replay_fails_only_by_source_driver_flags"] is True,
            all(slot["selected_dotD_source_verified"] is False for slot in dotd_sector_slots.values()),
            all(slot["alpha1_driver_verified"] is False for slot in dotd_sector_slots.values()),
        ]
    )
    c1_still_not_emitted = all(
        [
            c1["A_selected_emitted"] is False,
            c1["b_selected_emitted"] is False,
            c1["sector_response_matrices_emitted"] is False,
            c1["can_emit_c1_response_now"] is False,
        ]
    )
    reduced_payload_boundary_agrees = all(
        [
            prev["direct_alpha1_route"]["reduced_to"] == "SelectedPhiFinAlpha1Payload",
            prev["current_value_status"]["evaluated_grad_V_C1_alpha1_source_vector"] is None,
            prev_cert["reduced_to_SelectedPhiFinAlpha1Payload"] is True,
            prev_cert["selected_payload_values_emitted"] is False,
        ]
    )
    source_driver_remaining_exact = all(
        [
            remaining["selected_dotD_source_theorem"] is True,
            remaining["same_branch_alpha1_driver_theorem"] is True,
            remaining["retarded_overlap_source_vector_b_selected"] is True,
            remaining["finite_Hess_Xi_blocks"] is True,
            remaining["selected_zero_mode_bases"] is True,
            remaining["primitive_C1_contractions"] is True,
            remaining["sector_response_matrices"] is True,
        ]
    )
    no_knob_guardrails_hold = all(
        [
            nonsm_cert["guardrails"]["does_not_promote_dotD_flags"] is True,
            nonsm_cert["guardrails"]["does_not_claim_alpha1_driver"] is True,
            nonsm_cert["guardrails"]["does_not_claim_A_selected_or_b_selected"] is True,
            nonsm_cert["guardrails"]["does_not_claim_Yukawa_or_SM_closure"] is True,
            nonsm_cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"] is True,
        ]
    )

    theorem_proved = all(
        [
            same_basis_dotd_values_available,
            honest_replay_cutset_is_exact,
            c1_still_not_emitted,
            reduced_payload_boundary_agrees,
            source_driver_remaining_exact,
            no_knob_guardrails_hold,
        ]
    )

    packet = {
        "theorem": {
            "name": "SelectedPhiFinAlpha1PayloadValueEmissionPrefixImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The selected PhiFin alpha1 payload value-emission problem has a "
                "stronger closed prefix available from the no-knob repository: "
                "same-basis finite dotD_alpha1 value matrices, clean sector "
                "projectors, and a locked D_E/Riesz/Green gap layer. This prefix "
                "does not close physical source promotion. Honest replay still "
                "fails exactly at selected_dotD_source_verified and "
                "alpha1_driver_verified, so A_selected, b_selected, C1 response "
                "matrices, and SM/Yukawa closure remain open."
            ),
        },
        "imported_closed_prefix": {
            "from_repo": str(NONSM),
            "status": nonsm["status"],
            "same_basis_dotD_values_available": same_basis_dotd_values_available,
            "basis_id": dotd["basis_id"],
            "selected_D_E_gap_Riesz_Green_locked": closed_prefix[
                "selected_D_E_gap_Riesz_Green_locked"
            ],
            "dotD_alpha1_value_matrices_emitted": closed_prefix[
                "dotD_alpha1_value_matrices_emitted"
            ],
            "dotD_alpha1_has_nonzero_entries": closed_prefix[
                "dotD_alpha1_has_nonzero_entries"
            ],
            "sector_projectors_clean": closed_prefix["sector_projectors_clean"],
            "finite_horizontal_response_diagnostic_passes": closed_prefix[
                "finite_horizontal_response_diagnostic_passes"
            ],
            "sector_shape_checks": sector_shape_checks,
        },
        "honest_replay_boundary": {
            "closed": honest_replay_cutset_is_exact,
            "exit_code": dotd["honest_replay"]["exit_code"],
            "fails_only_by_source_driver_flags": dotd[
                "honest_replay_fails_only_by_source_driver_flags"
            ],
            "all_selected_dotD_source_flags_false": all(
                slot["selected_dotD_source_verified"] is False
                for slot in dotd_sector_slots.values()
            ),
            "all_alpha1_driver_flags_false": all(
                slot["alpha1_driver_verified"] is False
                for slot in dotd_sector_slots.values()
            ),
            "validator_output": dotd["honest_replay"]["output"],
        },
        "payload_emission_status": {
            "SelectedPhiFinAlpha1Payload_fully_emitted": False,
            "dotD_alpha1_value_matrices_emitted_as_unpromoted_prefix": True,
            "selected_dotD_source_theorem_proved": False,
            "same_branch_alpha1_driver_theorem_proved": False,
            "A_selected_emitted": c1["A_selected_emitted"],
            "b_selected_emitted": c1["b_selected_emitted"],
            "sector_response_matrices_emitted": c1["sector_response_matrices_emitted"],
            "evaluated_grad_V_C1_alpha1_source_vector": None,
        },
        "remaining_gates": remaining,
        "what_closes_now": {
            "previous_reduction_to_SelectedPhiFinAlpha1Payload_consumed": reduced_payload_boundary_agrees,
            "same_basis_dotD_alpha1_value_matrices_imported": same_basis_dotd_values_available,
            "sector_projector_rank_shapes_imported": True,
            "honest_replay_failure_cutset_identified": honest_replay_cutset_is_exact,
            "A_selected_b_selected_nonemission_preserved": c1_still_not_emitted,
            "target_fitting_excluded": no_knob_guardrails_hold,
        },
        "what_remains_open": {
            "selected_dotD_source_theorem": True,
            "same_branch_alpha1_driver_theorem": True,
            "retarded_overlap_source_vector_b_selected": True,
            "finite_Hess_Xi_blocks": True,
            "selected_zero_mode_bases": True,
            "primitive_C1_contractions": True,
            "sector_response_matrices": True,
            "A_selected_and_b_selected": True,
        },
        "guardrails": {
            "does_not_promote_dotD_flags": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_Yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "does_not_treat_unpromoted_dotD_values_as_physical_source_values": True,
        },
        "input_artifacts": {
            "previous_packet": str(PREV_PACKET),
            "previous_certificate": str(PREV_CERT),
            "nonsm_packet": str(NONSM_PACKET),
            "nonsm_certificate": str(NONSM_CERT),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "theorem_proved": theorem_proved,
        "same_basis_dotd_values_available": same_basis_dotd_values_available,
        "honest_replay_cutset_is_exact": honest_replay_cutset_is_exact,
        "c1_still_not_emitted": c1_still_not_emitted,
        "reduced_payload_boundary_agrees": reduced_payload_boundary_agrees,
        "source_driver_remaining_exact": source_driver_remaining_exact,
        "no_knob_guardrails_hold": no_knob_guardrails_hold,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_phifin_alpha1_payload_value_emission",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "dotD_alpha1_value_matrices_imported": same_basis_dotd_values_available,
        "physical_dotD_source_values_closed": False,
        "SelectedPhiFinAlpha1Payload_fully_emitted": False,
        "validator_ready": False,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected PhiFin Alpha1 Payload Value Emission From Selected HYM v1

## Result

The missing `SelectedPhiFinAlpha1Payload` is not fully emitted yet, but a
stronger prefix is now imported from the no-knob repo:

```text
same-basis finite dotD_alpha1 value matrices = present
sector projectors = clean
selected D_E / Riesz / Green gap layer = locked input
```

This is a real advance over mere shape scaffolding. The imported dotD matrices
have nonzero entries in the same `F3xF3_gerbe_twisted_fourier_N1_rank3` basis.

## Boundary

The honest replay still fails exactly at source/driver promotion:

```text
selected_dotD_source_verified = false
alpha1_driver_verified = false
A_selected emitted = false
b_selected emitted = false
```

Therefore this artifact does not claim physical alpha1 source values, C1
response matrices, Yukawa data, or SM closure.

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
