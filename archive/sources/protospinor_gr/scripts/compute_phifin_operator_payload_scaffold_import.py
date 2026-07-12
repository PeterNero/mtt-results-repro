from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

RHOE_CERT = ROOT / "certificates" / "phifin_finite_rhoe_trace_construction_certificate.json"
DE_CERT = SM / "certificates" / "selected_routec_de_action_on_smooth_bn_certificate.json"
DE_DATA = SM / "candidate_data" / "selected_routec_de_action_on_smooth_bn" / "de_action_on_smooth_bn.honest.json"
DOTD_CERT = SM / "certificates" / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json"
DOTD_DATA = SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn" / "sector_projectors_dotd_on_smooth_bn.honest.json"
C1_CERT = SM / "certificates" / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json"
C1_DATA = SM / "candidate_data" / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json"
C1_SOURCE_CERT = SM / "certificates" / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild_certificate.json"

OUT_CERT = ROOT / "certificates" / "phifin_operator_payload_scaffold_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "phifin_operator_payload_scaffold_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PhiFin_Operator_Payload_Scaffold_Import_v1.md"
OUT_INSERTION = ROOT / "proof_corpus" / "paper_insertions" / "PhiFin_Operator_Payload_Scaffold_for_Strominger_Paper.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def shape(matrix: list) -> list[int]:
    return [len(matrix), len(matrix[0]) if matrix else 0]


def summarize_de(data: dict) -> dict:
    summary = {}
    for name, slot in sorted(data["operator_slots"].items()):
        matrix_shape = shape(slot["D_E_matrix"])
        summary[name] = {
            "domain_dimension": slot["domain_dimension"],
            "expected_kernel_dimension": slot["expected_kernel_dimension"],
            "zero_mode_count": len(slot["ordered_zero_mode_basis"]),
            "D_E_matrix_shape": matrix_shape,
            "matrix_shape_matches_complement_to_domain": (
                matrix_shape == [
                    slot["domain_dimension"] - slot["expected_kernel_dimension"],
                    slot["domain_dimension"],
                ]
            ),
            "zero_mode_count_matches_expected_kernel": (
                len(slot["ordered_zero_mode_basis"]) == slot["expected_kernel_dimension"]
            ),
        }
    return summary


def summarize_dotd(data: dict) -> dict:
    summary = {}
    for name, slot in sorted(data["dotd_response_slots"].items()):
        projector = data["sector_projectors_on_BN"][name]["projector_matrix"]
        summary[name] = {
            "dimension": slot["dimension"],
            "expected_kernel_dimension": slot["expected_kernel_dimension"],
            "zero_mode_count": len(slot["ordered_zero_mode_basis"]),
            "dotD_alpha1_matrix_shape": shape(slot["dotD_alpha1_matrix"]),
            "sector_projector_shape": shape(projector),
            "horizontal_gauge_verified": slot["horizontal_gauge_verified"],
            "green_operator_verified": slot["green_operator_verified"],
            "selected_dotD_source_verified": slot["selected_dotD_source_verified"],
            "alpha1_driver_verified": slot["alpha1_driver_verified"],
        }
    return summary


def main() -> None:
    rhoe_cert = load(RHOE_CERT)
    de_cert = load(DE_CERT)
    de_data = load(DE_DATA)
    dotd_cert = load(DOTD_CERT)
    dotd_data = load(DOTD_DATA)
    c1_cert = load(C1_CERT)
    c1_data = load(C1_DATA)
    c1_source_cert = load(C1_SOURCE_CERT)

    de_summary = summarize_de(de_data)
    dotd_summary = summarize_dotd(dotd_data)

    basis_ids = {
        "D_E": de_data["basis_id"],
        "dotD": dotd_data["basis_id"],
    }
    same_basis = len(set(basis_ids.values())) == 1
    expected_sectors = ["H", "L", "N", "Q", "d", "e", "u"]

    de_matrix_layer_valid = (
        de_data["schema"] == "MTTSelectedRouteCDEActionOnSmoothBN.v1"
        and sorted(de_summary) == expected_sectors
        and all(item["matrix_shape_matches_complement_to_domain"] for item in de_summary.values())
        and all(item["zero_mode_count_matches_expected_kernel"] for item in de_summary.values())
    )
    dotd_layer_valid = (
        dotd_data["schema"] == "MTTSelectedRouteCSectorProjectorsDotDOnSmoothBN.v1"
        and sorted(dotd_summary) == expected_sectors
        and all(item["dotD_alpha1_matrix_shape"] == [27, 27] for item in dotd_summary.values())
        and all(item["sector_projector_shape"] == [27, 27] for item in dotd_summary.values())
        and all(item["horizontal_gauge_verified"] for item in dotd_summary.values())
        and all(item["green_operator_verified"] for item in dotd_summary.values())
    )

    c1_no_go_valid = (
        c1_data["theorem"]["proved"] is True
        and c1_data["what_closes_now"]["primitive_C1_contraction_engine_built"] is True
        and c1_data["what_closes_now"]["canonical_tensor_zero_response_result_proved_finitely"] is True
        and c1_data["closure_claimed"] is False
    )

    source_flags = {
        "D_E_selected_source_verified": de_data["selected_source_verified"],
        "dotD_selected_source_verified": dotd_data["selected_dotD_source_verified"],
        "dotD_alpha1_driver_verified": dotd_data["alpha1_driver_verified"],
    }

    closed_now = {
        "finite_rhoE_trace_already_constructed": rhoe_cert["verdict"]["finite_rhoE_trace_piece_constructed"],
        "same_BN_basis_for_DE_and_dotD": same_basis,
        "DE_matrix_layer_imported_and_shape_checked": de_matrix_layer_valid,
        "family_zero_mode_dimension_three_retained": all(
            de_summary[name]["expected_kernel_dimension"] == 3
            for name in ["L", "N", "Q", "d", "e", "u"]
        ),
        "Higgs_zero_mode_dimension_one_retained": de_summary["H"]["expected_kernel_dimension"] == 1,
        "sector_projectors_dotD_layer_imported_and_shape_checked": dotd_layer_valid,
        "canonical_C1_contraction_engine_imported": c1_no_go_valid,
        "canonical_C1_zero_response_no_go_preserved": c1_no_go_valid,
        "target_fitting_excluded": (
            de_cert["what_closes"]["target_fitting_excluded"] is True
            and dotd_cert["what_closes"]["target_fitting_excluded"] is True
            and c1_cert["what_closes"]["target_fitting_excluded"] is True
        ),
    }

    still_open = {
        "selected_Strominger_HYM_source_certificate": de_cert["what_remains_open"]["R1_selected_source_certificate"],
        "source_promotion_for_rhoE": rhoe_cert["still_open"]["R2_source_promotion_for_rhoE"],
        "selected_D_E_source_promotion": de_cert["what_remains_open"]["selected_D_E_source_promotion"],
        "selected_dotD_source_verified": dotd_cert["what_remains_open"]["selected_dotD_source_verified"],
        "alpha1_driver_verified": dotd_cert["what_remains_open"]["alpha1_driver_verified"],
        "nonzero_C1_response_matrices": c1_cert["what_remains_open"]["nonzero_C1_response_matrices"],
        "selected_basis_transport_or_noninvariant_C1_primitive": c1_source_cert["what_remains_open"]["prove_selected_basis_transport_or_vertex_source_theorem"],
        "honest_replay_without_lifted_flags": de_cert["what_remains_open"]["R6_replay_without_lifted_flags"],
        "full_selected_Phi_fin_payload_emission": True,
    }

    theorem = {
        "name": "PhiFinOperatorPayloadScaffoldImportTheorem",
        "proved": all(closed_now.values()) and all(value is False for value in source_flags.values()),
        "statement": (
            "Given the previously constructed finite rho_E trace, the Route-C smooth "
            "B_N payload supplies a concrete finite operator scaffold in the same "
            "F3xF3 gerbe-twisted Fourier rank-3 basis: D_E matrices, sector "
            "projectors, dotD_alpha1 matrices, family zero modes of dimension 3, "
            "and a Higgs zero mode of dimension 1. The canonical C1 primitive "
            "contraction engine is also present and proves a zero-response no-go "
            "for the translation-invariant primitive. This imports the operator "
            "scaffold only; it does not promote any selected-source flag."
        ),
    }

    verdict = {
        "phi_fin_finite_operator_scaffold_imported": theorem["proved"],
        "phi_fin_full_selected_payload_emitted": False,
        "selected_source_flags_may_be_set_true": False,
        "selected_matter_stress_coefficients_closed": False,
        "nonzero_C1_payload_closed": False,
        "next_required_artifact": "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1",
    }

    guardrails = {
        "does_not_claim_full_phi_fin": True,
        "does_not_claim_selected_source_promotion": True,
        "does_not_claim_nonzero_C1": True,
        "does_not_claim_SM_yukawa_or_mass_closure": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_lift_flags_by_hand": True,
    }

    packet = {
        "theorem": theorem,
        "basis_ids": basis_ids,
        "D_E_summary": de_summary,
        "dotD_projector_summary": dotd_summary,
        "C1_summary": {
            "status": c1_data["status"],
            "theorem": c1_data["theorem"],
            "matrix_slots": sorted(c1_data["c1_response_matrices"]),
            "what_closes_now": c1_data["what_closes_now"],
            "what_remains_open": c1_data["what_remains_open"],
        },
        "source_flags": source_flags,
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
    }

    note = f"""# Phi_fin Operator Payload Scaffold Import v1

## Result

The finite `Phi_fin` payload now has a concrete operator scaffold imported from
the Route-C smooth `B_N` packets, in the same basis:

```text
{basis_ids["D_E"]}
```

This scaffold contains:

- `D_E` matrices for `H,L,N,Q,d,e,u`.
- Sector projectors and `dotD_alpha1` matrices for the same sectors.
- Family zero-mode dimension `3` for `L,N,Q,d,e,u`.
- Higgs zero-mode dimension `1` for `H`.
- A finite C1 primitive contraction engine.

## Exact Boundary

This is not yet full selected `Phi_fin` payload emission. The imported matrix
layers are honest unpromoted model-active payloads:

```text
D_E selected_source_verified = {source_flags["D_E_selected_source_verified"]}
dotD selected_dotD_source_verified = {source_flags["dotD_selected_source_verified"]}
dotD alpha1_driver_verified = {source_flags["dotD_alpha1_driver_verified"]}
```

The canonical translation-invariant C1 primitive has also been tested and gives
zero response. Therefore the next true gate is not another bookkeeping import;
it is the selected basis-transport/non-invariant primitive/source theorem that
emits nonzero C1 response from the same selected branch.

## Status

```text
PHIFIN_OPERATOR_PAYLOAD_SCAFFOLD_IMPORTED_SOURCE_PROMOTION_AND_C1_OPEN
```
"""

    insertion = """# Phi_fin Operator Payload Scaffold Insert

Target paper:

```text
Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md
```

Suggested location:

```text
Appendix: Finite Phi_fin Emission Payload
```

## Proposition: Finite Operator Scaffold

After the finite projective `rho_E` trace is fixed, the Route-C smooth `B_N`
payload supplies an explicit finite operator scaffold in the common
`F3xF3_gerbe_twisted_fourier_N1_rank3` basis. The scaffold contains `D_E`,
sector projectors, and `dotD_alpha1` matrices for the sectors
`H,L,N,Q,d,e,u`. It also retains the zero-mode counts required by the branch:
dimension `3` for the family sectors and dimension `1` for the Higgs sector.

The same finite payload includes a C1 primitive contraction engine. For the
canonical translation-invariant primitive, the response matrices vanish. Hence
nonzero C1 data require a selected non-invariant primitive, a vertex correction,
basis transport, or a source theorem deriving a different selected trilinear
tensor.

## Proof Boundary

This proposition imports the finite scaffold only. It does not assert selected
source promotion, full selected `Phi_fin` payload emission, nonzero Yukawa/CKM
data, or fitted Standard Model masses. No observed constants or benchmark
matrices are used to set the source flags.
"""

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "phifin_operator_payload_scaffold_import",
        "status": "PHIFIN_OPERATOR_PAYLOAD_SCAFFOLD_IMPORTED_SOURCE_PROMOTION_AND_C1_OPEN",
        "input_certificates": {
            "phifin_finite_rhoe_trace_construction": str(RHOE_CERT),
            "selected_routec_de_action_on_smooth_bn": str(DE_CERT),
            "selected_routec_sector_projectors_dotd_on_smooth_bn": str(DOTD_CERT),
            "selected_routec_c1_primitive_response_on_smooth_bn": str(C1_CERT),
            "selected_routec_selected_c1_operator_source_or_galerkin_rebuild": str(C1_SOURCE_CERT),
        },
        "theorem": theorem,
        "basis_ids": basis_ids,
        "D_E_summary": de_summary,
        "dotD_projector_summary": dotd_summary,
        "C1_summary": packet["C1_summary"],
        "source_flags": source_flags,
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
        "paper_insertion_written": str(OUT_INSERTION),
    }

    OUT_INSERTION.parent.mkdir(parents=True, exist_ok=True)
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_INSERTION.write_text(insertion, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_INSERTION}")
    print("STATUS: PHIFIN_OPERATOR_PAYLOAD_SCAFFOLD_IMPORTED_SOURCE_PROMOTION_AND_C1_OPEN")


if __name__ == "__main__":
    main()
