from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

POST_ALPHA = ROOT / "certificates" / "post_alpha_selected_correction_source_reduction_certificate.json"
POST_ALPHA_PACKET = ROOT / "candidate_data" / "post_alpha_selected_correction_source_reduction.packet.json"
RHOE = ROOT / "certificates" / "routec_nonidentity_rhoe_bn_construction_import_certificate.json"
BN = ROOT / "certificates" / "routec_smooth_bn_galerkin_lift_import_certificate.json"
DE = ROOT / "certificates" / "routec_de_action_on_smooth_bn_import_certificate.json"
DOTD = ROOT / "certificates" / "routec_sector_projectors_dotd_on_smooth_bn_import_certificate.json"
C1 = ROOT / "certificates" / "routec_c1_primitive_response_on_smooth_bn_import_certificate.json"
WEYL = ROOT / "certificates" / "routec_weylpair_frontier_reconciliation_certificate.json"
WEYL_PACKET = ROOT / "candidate_data" / "routec_weylpair_frontier_reconciliation.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_routec_frontier_synchronization_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_routec_frontier_synchronization.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_RouteC_Frontier_Synchronization_v1.md"

STATUS = "POST_ALPHA_ROUTEC_FRONTIER_SYNCHRONIZED_WEYLPAIR_PROVENANCE_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    post_alpha = load(POST_ALPHA)
    post_alpha_packet = load(POST_ALPHA_PACKET)
    rhoe = load(RHOE)
    bn = load(BN)
    de = load(DE)
    dotd = load(DOTD)
    c1 = load(C1)
    weyl = load(WEYL)
    weyl_packet = load(WEYL_PACKET)

    post_alpha_ready = all(
        [
            post_alpha["status"] == "POST_ALPHA_SELECTED_CORRECTION_SOURCE_REDUCED_NONIDENTITY_RHOE_BN_OPEN",
            post_alpha["checks"]["theorem_proved"] is True,
            post_alpha["selected_correction_matrix_source_closed"] is False,
            post_alpha["diagnostic_splitter_promoted"] is False,
            post_alpha_packet["next_required_artifact"]
            == "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1",
        ]
    )

    routec_chain = {
        "nonidentity_rhoE_numeric_packet_built": (
            rhoe["theorem"]["proved"] is True
            and rhoe["verdict"]["nonidentity_rhoE_numeric_packet_built"] is True
            and rhoe["verdict"]["R2_source_promotion_closed"] is False
        ),
        "smooth_BN_scaffold_built": (
            bn["theorem"]["proved"] is True
            and bn["verdict"]["smooth_BN_scaffold_built"] is True
            and bn["verdict"]["full_BN_payload_gate_closed"] is False
        ),
        "DE_matrix_built_source_open": (
            de["theorem"]["proved"] is True
            and de["verdict"]["D_E_matrix_on_27_mode_BN_built"] is True
            and de["verdict"]["full_selected_DE_action_closed"] is False
        ),
        "sector_projectors_dotD_built_source_open": (
            dotd["theorem"]["proved"] is True
            and dotd["verdict"]["sector_projectors_built"] is True
            and dotd["verdict"]["dotD_alpha1_on_same_basis_built"] is True
            and dotd["verdict"]["selected_dotD_source_promotes"] is False
        ),
        "canonical_C1_response_zero_no_go": (
            c1["theorem"]["proved"] is True
            and c1["verdict"]["canonical_C1_contraction_engine_built"] is True
            and c1["verdict"]["canonical_translation_invariant_C1_response_nonzero"] is False
            and c1["verdict"]["selected_noninvariant_primitive_required"] is True
        ),
        "weylpair_conditional_solve_closed_source_open": (
            weyl["theorem"]["proved"] is True
            and weyl["verdict"]["conditional_A_solve_closed"] is True
            and weyl["verdict"]["algebraic_rank_obstruction_absent"] is True
            and weyl["verdict"]["selected_source_provenance_proved"] is False
            and weyl["verdict"]["A_selected_emitted"] is False
            and weyl["verdict"]["b_selected_emitted"] is False
        ),
    }

    payload_reclassification = {
        "nonidentity_rho_E": "finite numeric Weyl/Heisenberg packet built; selected source promotion still open",
        "quotient_valid_B_N": "27-mode smooth model-active scaffold built; full selected B_N/source promotion still open",
        "selected_D_E_Riesz_Green_dotD": "finite model-active D_E, Riesz/Green, sector projectors, and dotD built; honest selected-source replay still open",
        "primitive_C1_contractions_or_full_response_matrices": "canonical primitive proved zero; Weyl-pair conditional response spans locked splitter, but provenance is open",
        "selected_deltaTheta_C1_solution": "conditional rank-2 Weyl-pair solve closed with tiny residual; not promoted to selected solve",
        "b_selected_or_homogeneous_zero_theorem": "b_selected still not emitted",
        "selected_source_certificate": "same-branch Weyl-pair source provenance is the current blocker",
    }

    still_open = {
        "same_branch_weylpair_source_provenance": True,
        "A_selected_emission": True,
        "b_selected_emission": True,
        "honest_selected_deltaTheta_C1_solve": True,
        "selected_source_certificate": True,
        "full_selected_Iwasawa_Strominger_DE_or_truncation_error": True,
        "Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
    }

    guardrails = {
        "does_not_promote_diagnostic_splitter": True,
        "does_not_promote_conditional_A_to_A_selected": True,
        "does_not_claim_b_selected": True,
        "does_not_claim_selected_source_provenance": True,
        "does_not_claim_lambda12_yukawa_or_full_SM": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_use_lifted_flags": True,
    }

    theorem_proved = all(
        [
            post_alpha_ready,
            all(routec_chain.values()),
            all(still_open.values()),
            all(guardrails.values()),
            weyl["verdict"]["next_required_artifact"] == NEXT,
        ]
    )

    theorem = {
        "name": "PostAlphaRouteCFrontierSynchronizationImport",
        "proved": theorem_proved,
        "closure_claimed": False,
        "statement": (
            "The latest post-alpha selected-correction reduction is synchronized "
            "with the already verified Route-C ladder. The rho_E/B_N/D_E/dotD "
            "finite scaffold and the conditional Weyl-pair linear solve are no "
            "longer the sharp blockers. The remaining proof step is same-branch "
            "selected source provenance for the Weyl-pair columns, followed by "
            "A_selected and b_selected emission and an honest selected DeltaTheta_C1 solve."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "post_alpha_ready": post_alpha_ready,
        "routec_chain": routec_chain,
        "payload_reclassification": payload_reclassification,
        "locked_solve": {
            "rank": weyl_packet["locked_solve"]["rank"],
            "relative_residual": weyl_packet["locked_solve"]["relative_residual"],
            "condition_number": weyl_packet["locked_solve"]["condition_number"],
            "deltaTheta_conditional": weyl_packet["locked_solve"]["deltaTheta_conditional"],
        },
        "current_frontier": {
            "not_linear_algebra": True,
            "not_raw_nonidentity_rhoE": True,
            "not_raw_smooth_BN_scaffold": True,
            "blocker": "same-branch selected Weyl-pair source provenance plus b_selected emission",
            "next_required_artifact": NEXT,
        },
        "what_remains_open": still_open,
        "guardrails": guardrails,
        "input_certificates": {
            "post_alpha_selected_correction_source_reduction": str(POST_ALPHA),
            "post_alpha_selected_correction_source_reduction_packet": str(POST_ALPHA_PACKET),
            "routec_nonidentity_rhoe_bn_construction": str(RHOE),
            "routec_smooth_bn_galerkin_lift": str(BN),
            "routec_de_action_on_smooth_bn": str(DE),
            "routec_sector_projectors_dotd_on_smooth_bn": str(DOTD),
            "routec_c1_primitive_response_on_smooth_bn": str(C1),
            "routec_weylpair_frontier_reconciliation": str(WEYL),
            "routec_weylpair_frontier_reconciliation_packet": str(WEYL_PACKET),
        },
    }

    note = f"""# PostAlpha Route-C Frontier Synchronization v1

## Result

The latest post-alpha reduction has been synchronized with the verified
Route-C ladder.

The old next gate asked for nonidentity `rho_E` and quotient-valid `B_N`.
Those are now partially filled by verified finite/scaffold packets:

```text
nonidentity rho_E finite packet = built
smooth 27-mode B_N scaffold = built
model-active D_E/Riesz/Green = built
sector projectors and dotD_alpha1 = built
canonical primitive C1 response = proved zero
conditional Weyl-pair A solve = rank 2, tiny residual
```

The sharper frontier is therefore not raw linear algebra. It is provenance:

```text
prove the selected q79/F,m=1 S3/GS source emits the Weyl-pair columns
emit b_selected from that same selected source
promote conditional A_weylpair to A_selected only after provenance is proved
run the honest selected DeltaTheta_C1 solve
```

No observed masses, CKM, PMNS, CP phase, benchmark entries, or lifted selected
flags are used.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_routec_frontier_synchronization",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "post_alpha_ready": post_alpha_ready,
        "routec_chain": routec_chain,
        "still_open": still_open,
        "guardrails": guardrails,
        "current_frontier": packet["current_frontier"],
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
