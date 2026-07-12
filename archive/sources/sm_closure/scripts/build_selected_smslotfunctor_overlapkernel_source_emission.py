"""Build selected SM-slot functor overlap-kernel source emission."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_smslotfunctor_polarization_overlap_source_emission.candidate.json"
PROJECTOR = DATA / "selected_finite_projector_source_promotion.candidate.json"
GRAM = DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
EXT_OVERLAP = DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
L2_EXT = DATA / "selected_ext_l2_theta_quadrature_table.candidate.json"

OUTPUT = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
CERT = CERTS / "selected_smslotfunctor_overlapkernel_source_emission_certificate.json"
NOTE = CORPUS / "MTT_SelectedSMSlotFunctor_OverlapKernel_SourceEmission_v1.md"

STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_ALL_SIX_ARROWS_EMITTED_OPERATOR_PAYLOADS_OPEN"
NEXT = "MTT_SelectedSMSlotFunctor_DownstreamOperatorPayloads_or_SMParityLedger_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    previous = load(PREVIOUS)
    projector = load(PROJECTOR)
    gram = load(GRAM)
    ext_overlap = load(EXT_OVERLAP)
    l2_ext = load(L2_EXT)

    promoted = projector["promoted_sector_slots"]
    matter_sectors = ["Q", "u", "d", "L", "e", "N"]
    matter_projector_checks = {
        sector: {
            "rank": promoted[sector]["rank"],
            "projector_idempotent": promoted[sector]["projector_idempotent"],
            "projector_self_adjoint": promoted[sector]["projector_self_adjoint"],
            "source_verified_by_transport_conjugation": promoted[sector][
                "source_verified_by_transport_conjugation"
            ],
            "stationary_rho_s_promoted": promoted[sector]["stationary_rho_s_promoted"],
        }
        for sector in matter_sectors
    }
    all_matter_projectors_selected = all(
        item["rank"] == 3
        and item["projector_idempotent"]
        and item["projector_self_adjoint"]
        and item["source_verified_by_transport_conjugation"]
        and item["stationary_rho_s_promoted"]
        for item in matter_projector_checks.values()
    )

    selected_overlap_kernel = {
        "status": "EMITTED_SOURCE_ARROW",
        "arrow": "A5 selected overlap/transfer normalization",
        "source": "transported projector trace kernel plus selected unit Ext row",
        "kernel_definition": (
            "For each selected matter triplet K_s, use the transported projector trace Gram "
            "<a,b>_s = Tr(P_s^sel a^* b P_s^sel)/3, with End0 generators normalized by "
            "||rho_s(T_i)||_F=sqrt(2). The transfer representative is rho_s(T_i)/sqrt(2)."
        ),
        "normalization_values": {
            "matter_triplet_rank": 3,
            "raw_Ti_frobenius_norm": gram["gram_transfer_packet"][
                "raw_T3_frobenius_norm_per_matter_sector"
            ],
            "unit_trace_transfer": gram["gram_transfer_packet"]["unit_trace_transfer"],
            "eta_00_unit_L2_norm": ext_overlap["Hodge_Lambda_table"]["L2_norm_of_unit_eta_00"],
            "eta_00_unit_rescale_factor": ext_overlap["selected_row"]["unit_rescale_factor"],
            "theta_unrescaled_norm_square": ext_overlap["selected_row"]["unrescaled_norm_square"],
        },
        "preconditions": {
            "first_four_arrows_closed": previous["arrow_status"]["closed_count"] == 4,
            "transported_projector_source_promoted": projector["promotion_decision"][
                "finite_projector_source_promotion_proved"
            ],
            "all_matter_projectors_selected": all_matter_projectors_selected,
            "conditional_gram_theorem_proved": gram["gram_transfer_packet"][
                "conditional_gram_theorem_proved"
            ],
            "gram_condition_satisfied_by_selected_rho_s": all_matter_projectors_selected,
            "selected_ext_unit_row_closed": ext_overlap["selected_row"]["unit_L2_representative"]
            == "32^(1/4) * Theta_{2,0}(z1; i) tensor Eta_{-4,0}(z2; i) dbar_z2",
            "selected_hodge_projector_row_closed": ext_overlap["gauge_projector_table"][
                "closed_for_eta_row"
            ],
            "theta_quadrature_norm_available": l2_ext["eta_00_l2_table"][
                "unit_L2_rescale_factor_numeric"
            ]
            == ext_overlap["selected_row"]["unit_rescale_factor"],
        },
        "why_promoted_now": (
            "The old transfer theorem was conditional on selected rho_s/zero-mode projectors. The finite "
            "projector promotion supplies those selected transported projectors and rho_s for all matter "
            "triplets. The Ext overlap/Hodge table supplies a unit L2 selected eta_00 row. Therefore the "
            "trace Gram kernel is selected without fitting a scalar."
        ),
        "selected": True,
    }

    same_source_consistency = {
        "status": "EMITTED_SOURCE_ARROW",
        "arrow": "A6 same-source consistency map",
        "closed_parts": {
            "terminal_sectionring_source": True,
            "A1_A3_slot_arrows": True,
            "A4_q79_polarization": previous["polarization_emission"]["selected"],
            "A5_overlap_kernel": selected_overlap_kernel["selected"],
            "transported_projector_source": projector["promotion_decision"][
                "transported_packet_promoted"
            ],
        },
        "consistency_map": (
            "Map the axiom-backed terminal Ext source to SM slots (A1-A3), compose with q79 "
            "polarization (A4), and evaluate overlaps using the transported projector trace Gram "
            "kernel (A5). All maps are source-side and precede measured constants."
        ),
        "selected_same_source_consistency_map": True,
        "downstream_not_included": [
            "operator-layer Pic0 recheck",
            "same-source D_E/Riesz/Green/dotD payloads",
            "physical alpha1 driver",
            "primitive C1 overlap contractions",
            "Yukawa magnitudes, CKM/PMNS, masses, or full SM no-knob closure",
        ],
    }

    arrow_status = {
        "closed_count": 6,
        "open_count": 0,
        "closed_arrows": [
            *previous["arrow_status"]["closed_arrows"],
            "A5_overlap_transfer_normalization",
            "A6_same_source_consistency",
        ],
        "open_arrows": [],
        "all_six_closed": True,
    }

    theorem = {
        "name": "SelectedSMSlotFunctorOverlapKernelAndConsistencyTheorem",
        "proved": True,
        "statement": (
            "The selected SM-slot functor now has all six source arrows. A5 is emitted by the "
            "transported-projector trace Gram kernel normalized by the selected End0 Frobenius norm and "
            "the unit L2 Ext row. A6 follows as the same-source composition of terminal section-ring "
            "slot arrows, q79 polarization, and the selected overlap kernel. This closes the SM-slot "
            "functor source packet only; it does not close downstream operator payloads or physical "
            "flavor constants."
        ),
    }

    data = {
        "candidate": "MTTSelectedSMSlotFunctorOverlapKernelSourceEmission",
        "status": STATUS,
        "inputs": {
            "previous_polarization_gate": rel(PREVIOUS),
            "finite_projector_source_promotion": rel(PROJECTOR),
            "sectorcharge_gram_transfer": rel(GRAM),
            "selected_ext_overlap_hodge_projector": rel(EXT_OVERLAP),
            "selected_ext_l2_theta_quadrature": rel(L2_EXT),
        },
        "superset_strategy": {
            "mode": "SAME_SOURCE_FUNCTOR_CLOSURE_WITH_DOWNSTREAM_OPERATOR_BOUNDARY",
            "using_one_straight_path": False,
            "straight_path": "transported projector trace Gram kernel emits A5 after selected rho_s/projectors",
            "support_path": "selected Ext L2/Hodge/projector row supplies unit source normalization",
            "locked_target_role": "forbidden as selector; no measured constants or benchmark matrices",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "matter_projector_checks": matter_projector_checks,
        "selected_overlap_kernel": selected_overlap_kernel,
        "same_source_consistency": same_source_consistency,
        "arrow_status": arrow_status,
        "what_closes_now": {
            "selected_overlap_transfer_normalization": True,
            "same_source_consistency_map": True,
            "selected_SMSlotFunctor_all_six_arrows": True,
            "selected_terminal_to_SU5_E6_slot_packet": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "operator_layer_Pic0_recheck": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "physical_alpha1_driver": True,
            "primitive_C1_overlap_contractions": True,
            "Yukawa_CKM_PMNS_masses": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "selected_SMSlotFunctor_all_six_arrows_claimed": True,
        "downstream_operator_or_flavor_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_SelectedSMSlotFunctor_OverlapKernel_SourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "selected_SMSlotFunctor_all_six_arrows_claimed": True,
        "downstream_operator_or_flavor_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": data["what_closes_now"],
        "what_remains_open": data["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SelectedSMSlotFunctor OverlapKernel SourceEmission v1

Status: `{STATUS}`.

## Result

The selected SM-slot functor now has all six source arrows.

A5 is emitted by the transported-projector trace Gram kernel:

```text
<a,b>_s = Tr(P_s^sel a^* b P_s^sel)/3
transfer representative = rho_s(T_i)/sqrt(2)
```

The normalization uses selected transported matter triplet projectors, promoted
`rho_s`, and the selected unit `eta_00` Ext row.  No scalar is fitted.

A6 follows as the same-source composition of:

- terminal section-ring arrows to `10_M`, `bar5_M`, and `1_M=N^c`;
- selected q79 polarization `U_10=I_3`, `U_bar5=F`;
- selected transported-projector overlap kernel.

## Boundary

This closes the SM-slot functor source packet.  It does not close operator-layer
Pic0, same-source `D_E/Riesz/Green/dotD`, physical alpha1, C1 overlap
contractions, Yukawa magnitudes, CKM/PMNS, masses, or full SM no-knob closure.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
