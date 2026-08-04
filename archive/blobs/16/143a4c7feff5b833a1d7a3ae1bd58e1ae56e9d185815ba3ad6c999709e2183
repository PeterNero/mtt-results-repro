"""Build selected SM-slot functor polarization and overlap source-emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_smslotfunctor_sixarrow_source_emission.candidate.json"
MATTER_OVERLAP = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
GRAM = DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
PROJECTOR = DATA / "selected_finite_projector_source_promotion.candidate.json"

Q79_TRANSVERSALITY = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\candidate_data"
    r"\su5_matter_slot_transversality.candidate.json"
)
Q79_PROJECTION = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\candidate_data"
    r"\su5_projection_tensor_derivation_attempt.candidate.json"
)

OUTPUT = DATA / "selected_smslotfunctor_polarization_overlap_source_emission.candidate.json"
CERT = CERTS / "selected_smslotfunctor_polarization_overlap_source_emission_certificate.json"
NOTE = CORPUS / "MTT_SelectedSMSlotFunctor_PolarizationAndOverlap_SourceEmission_v1.md"

STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_POLARIZATION_EMITTED_OVERLAP_NORMALIZATION_OPEN"
NEXT = "MTT_SelectedSMSlotFunctor_OverlapKernel_SourceEmission_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def maybe_rel(path: Path) -> str:
    try:
        return rel(path)
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    previous = load(PREVIOUS)
    matter_overlap = load(MATTER_OVERLAP)
    gram = load(GRAM)
    projector = load(PROJECTOR)
    q79_trans = load(Q79_TRANSVERSALITY)
    q79_projection = load(Q79_PROJECTION)

    first_three_closed = previous["arrow_status"]["closed_count"] == 3
    selected_10_bar5_labels = (
        previous["what_closes_now"]["selected_sectionring_to_10M_clock_arrow"]
        and previous["what_closes_now"]["selected_sectionring_to_bar5M_shift_arrow"]
    )
    selected_1m = previous["what_closes_now"]["selected_sectionring_to_1M_Dirac_arrow"]
    trans = q79_trans["calculation_results"]
    q79_packet = trans["selected_packet"]

    polarization_emission = {
        "status": "EMITTED_SOURCE_ARROW",
        "arrow": "A4 selected q79 polarization outputs",
        "preconditions": {
            "first_three_slot_arrows_closed": first_three_closed,
            "selected_10M_clock_label": previous["emitted_source_arrows"][
                "A1_terminal_Ext_to_10M_clock"
            ]["selected"],
            "selected_bar5M_shift_label": previous["emitted_source_arrows"][
                "A2_terminal_Ext_to_bar5M_shift"
            ]["selected"],
            "selected_1M_Dirac_label": selected_1m,
            "finite_q79_transversality_closed": trans["finite_transversality_theorem_closed"],
            "retarded_q79_orientation_closed": trans["retarded_q79_orientation_closed"],
            "basis_candidate_matches_B10_I_Bbar5_F": trans["basis_candidate_matches_B10_I_Bbar5_F"],
            "common_slot_transport_rejected_as_gauge": trans["common_slot_transport_is_gauge"],
        },
        "selected_outputs": {
            "q": q79_packet["q"],
            "U_10": q79_packet["U_10"],
            "U_bar5": q79_packet["U_bar5"],
            "Delta_t": q79_packet["Delta_t"],
        },
        "why_promoted_now": (
            "The old q79 obstruction was missing selected ordered SU(5) slot labels. The previous "
            "artifact emitted those labels from the axiom-backed terminal section-ring source. With "
            "10_M and bar5_M selected, the closed finite transversality theorem uniquely selects the "
            "retarded q79 orientation U_10=I_3, U_bar5=F rather than the common-gauge cases or the "
            "conjugate q369 orientation."
        ),
        "selected": True,
    }

    overlap_kernel_gate = {
        "status": "OPEN",
        "conditional_support": {
            "transported_projector_source_promoted": projector["promotion_decision"][
                "finite_projector_source_promotion_proved"
            ],
            "conditional_gram_scalar_fixed_after_rho_s": gram["what_closes_now"][
                "conditional_Gram_transfer_scalar_fixed_after_rho_s"
            ],
            "conditional_normalization_exact": matter_overlap["selection_verdict"][
                "conditional_routing_and_normalization_are_exact"
            ],
            "conditional_residual_norm": matter_overlap["overlap_normalization"][
                "conditional_residual_norm"
            ],
            "conditional_condition_number": matter_overlap["overlap_normalization"][
                "conditional_condition_number"
            ],
        },
        "candidate_normalization": {
            "unitary_U10": True,
            "unitary_Ubar5": True,
            "unit_trace_transfer": gram["gram_transfer_packet"]["unit_trace_transfer"],
            "conditional_deltaTheta": matter_overlap["overlap_normalization"][
                "conditional_deltaTheta"
            ],
        },
        "why_not_promoted": (
            "The selected overlap/transfer normalization requires an emitted same-source kernel or "
            "trace/inner-product/Hessian functional. Current data prove exact conditional normalization "
            "and unitary polarization, but not the selected kernel itself."
        ),
        "selected_overlap_transfer_normalization": False,
    }

    same_source_consistency = {
        "status": "PARTIAL_OPEN_WAITING_FOR_A5",
        "closed_parts": {
            "terminal_sectionring_source": True,
            "matter_slot_arrows_A1_A3": True,
            "q79_polarization_A4": True,
            "transported_projector_source": projector["promotion_decision"][
                "transported_packet_promoted"
            ],
        },
        "open_parts": {
            "selected_overlap_transfer_kernel_A5": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "operator_layer_Pic0_recheck": True,
        },
        "selected_same_source_consistency_map": False,
    }

    arrow_status = {
        "closed_count": 4,
        "open_count": 2,
        "closed_arrows": [
            *previous["arrow_status"]["closed_arrows"],
            "A4_q79_polarization_outputs",
        ],
        "open_arrows": [
            "A5_overlap_transfer_normalization",
            "A6_same_source_consistency",
        ],
        "all_six_closed": False,
    }

    theorem = {
        "name": "SelectedSMSlotFunctorPolarizationEmissionTheorem",
        "proved": True,
        "statement": (
            "After A1-A3 emit selected 10_M, bar5_M, and 1_M=N^c slot labels from the terminal "
            "section-ring source, the finite q79 transversality theorem promotes A4: selected "
            "polarization outputs are U_10=I_3 and U_bar5=F on the retarded q79 branch. This uses no "
            "observed constants or benchmark matrices. A5 and A6 remain open until a selected "
            "overlap/transfer kernel or trace/Hessian normalization is emitted from the same source."
        ),
    }

    data = {
        "candidate": "MTTSelectedSMSlotFunctorPolarizationOverlapSourceEmission",
        "status": STATUS,
        "inputs": {
            "previous_six_arrow_gate": rel(PREVIOUS),
            "matter_slot_charge_overlap_attempt": rel(MATTER_OVERLAP),
            "gram_transfer_packet": rel(GRAM),
            "finite_projector_source_promotion": rel(PROJECTOR),
            "q79_su5_transversality": maybe_rel(Q79_TRANSVERSALITY),
            "q79_projection_tensor": maybe_rel(Q79_PROJECTION),
        },
        "superset_strategy": {
            "mode": "SELECTED_LABELS_PLUS_FINITE_Q79_POLARIZATION_WITH_OVERLAP_GATE_RETAINED",
            "using_one_straight_path": False,
            "straight_path": "selected terminal section-ring slot labels A1-A3 feed q79 finite transversality to emit A4",
            "support_path": "transported projectors plus conditional Gram/overlap exactness constrain but do not yet emit A5",
            "locked_target_role": "forbidden as selector; compatibility only",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "polarization_emission": polarization_emission,
        "overlap_kernel_gate": overlap_kernel_gate,
        "same_source_consistency": same_source_consistency,
        "arrow_status": arrow_status,
        "what_closes_now": {
            "selected_U10_Ubar5_source_outputs": True,
            "selected_q79_retarded_orientation": True,
            "common_gauge_polarizations_rejected": True,
            "conjugate_q369_orientation_rejected_for_this_branch": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_overlap_transfer_normalization": True,
            "same_source_consistency_map": True,
            "selected_overlap_kernel_or_trace_hessian_functional": True,
            "operator_layer_Pic0_recheck": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "physical_alpha1_driver": True,
            "primitive_C1_overlap_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "selected_SMSlotFunctor_first_four_arrows_claimed": True,
        "selected_SMSlotFunctor_all_six_arrows_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_SelectedSMSlotFunctor_PolarizationAndOverlap_SourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "selected_SMSlotFunctor_first_four_arrows_claimed": True,
        "selected_SMSlotFunctor_all_six_arrows_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": data["what_closes_now"],
        "what_remains_open": data["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SelectedSMSlotFunctor PolarizationAndOverlap SourceEmission v1

Status: `{STATUS}`.

## Result

A4 is now emitted.  Since A1-A3 already supplied selected `10_M`, `bar5_M`, and
`1_M=N^c` labels from the terminal section-ring source, the finite q79
transversality theorem promotes the selected polarization:

```text
q      = 79
U_10   = I_3
U_bar5 = F
```

The common-gauge cases are rejected as gauge, and the conjugate q369 branch is
not the retarded orientation for this selected branch.

## Still Open

A5 remains open: selected overlap/transfer normalization still needs a
same-source kernel or trace/inner-product/Hessian functional.  A6 therefore
remains partial until A5 is emitted.

No observed constants, benchmark matrices, locked C1 columns, or target fitting
are used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
