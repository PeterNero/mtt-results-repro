from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

RUN_CERT = ROOT / "certificates" / "selected_hym_connection_to_finite_operator_extraction_run_certificate.json"
INSERTION_CERT = ROOT / "certificates" / "selected_hym_extraction_theorem_insertions_certificate.json"
SM_SOLVE_CERT = SM / "certificates" / "selected_hym_gaugefixed_connection_or_galerkin_solve_certificate.json"
SM_SOLVE_PACKET = SM / "candidate_data" / "selected_hym_gaugefixed_connection_or_galerkin_solve.candidate.json"
SM_SOURCE_ALPHA1 = SM / "candidate_data" / "selected_source_origin_and_alpha1_driver.candidate.json"
Q79_PHIFIN_CERT = Q79 / "certificates" / "q79_selected_phifin_alpha1_payload_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_hym_value_solve_attempt_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_hym_value_solve_attempt.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_HYM_Value_Solve_Attempt_v1.md"

STATUS = "SELECTED_HYM_VALUE_SOLVE_ATTEMPT_BLOCKED_COEFFICIENTS_AND_RANK2_SECTOR_FUNCTOR_OPEN"
NEXT = "MTT_Selected_HYM_NewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    run = load(RUN_CERT)
    insertion = load(INSERTION_CERT)
    sm_solve = load(SM_SOLVE_CERT)
    sm_packet = load(SM_SOLVE_PACKET)
    source_alpha1 = load(SM_SOURCE_ALPHA1)
    q79_phifin = load(Q79_PHIFIN_CERT)

    finite_contract = sm_packet["finite_newton_galerkin_contract"]
    first_attempt = sm_packet["first_solve_attempt"]
    hym_problem = sm_packet["gauge_fixed_hym_problem"]
    q79_test = q79_phifin["closure_test"]
    q79_flags = q79_phifin["closure_gate_table"]["selected_payload_flags"]

    attempted_routes = {
        "direct_selected_hym_connection": {
            "attempted": True,
            "closed": False,
            "reason": first_attempt["direct_cause"],
            "missing": [
                "selected A_HYM or Hermitian endomorphism coefficient vector",
                "gauge-fixed HYM residual vector",
                "coercivity and truncation certificate",
            ],
        },
        "finite_newton_galerkin": {
            "attempted": True,
            "closed": False,
            "basis_dimension": finite_contract["basis_dimension"],
            "basis_id": finite_contract["basis_id"],
            "complement_gap_from_scaffold": finite_contract["complement_gap_from_scaffold"],
            "values_emitted": finite_contract["values_emitted"],
            "posteriori_error_certificate_emitted": finite_contract["posteriori_error_certificate_emitted"],
            "reason": "The finite solve contract exists, but no selected coefficient vector or residual/error certificate is emitted.",
        },
        "route_c_residual_bypass": {
            "attempted": True,
            "closed": False,
            "honest_run_passes": False,
            "formal_lift_rejected": True,
            "reason": "The formal residual lift can satisfy shape validators only by setting selected_source_verified without a source theorem.",
        },
        "phifin_alpha1_payload": {
            "attempted": True,
            "closed": q79_test["can_close_selected_phifin_alpha1_payload_now"],
            "finite_shape_pass": q79_test["finite_shape_pass"],
            "selected_payload_flags_all_true": q79_test["selected_payload_flags_all_true"],
            "selected_payload_flags": q79_flags,
            "reason": "The q79 Phi_fin alpha1 gate closes negatively: shapes and alpha1 support exist, but selected payload values are not emitted.",
        },
        "rank2_to_sector_transfer": {
            "attempted": True,
            "closed": sm_solve["rank2_to_sector_functor_emitted"],
            "reason": first_attempt["secondary_cause"],
        },
    }

    legal_value_solve_closed = all(
        [
            insertion["theorem"]["proved"] is True,
            sm_solve["first_solve_closed"] is True,
            finite_contract["values_emitted"] is True,
            finite_contract["posteriori_error_certificate_emitted"] is True,
            sm_solve["rank2_to_sector_functor_emitted"] is True,
            run["verdict"]["selected_values_emitted"] is True,
            q79_test["can_close_selected_phifin_alpha1_payload_now"] is True,
        ]
    )

    theorem = {
        "name": "SelectedHYMValueSolveAttemptNoGo",
        "proved": True,
        "closure_claimed": False,
        "statement": (
            "The selected HYM value solve has been attempted against the current "
            "cross-repo evidence. The extraction criterion is known, the gauge-fixed "
            "rank-2 HYM equations and finite Newton/Galerkin contract are formulated, "
            "and the q79 Phi_fin alpha1 codomain is present. However no selected "
            "A_HYM/H coefficient vector, no selected residual/error certificate, no "
            "rank-2-to-sector transfer functor, and no proof-usable selected "
            "Route-C/Phi_fin payload values are emitted. Therefore A_selected and "
            "b_selected remain unpromoted."
        ),
    }

    what_closes_now = {
        "value_solve_attempt_executed": True,
        "direct_hym_solve_checked": True,
        "finite_newton_contract_imported": finite_contract["built"] is True,
        "rank2_vs_sector_type_blocker_imported": sm_packet["what_closes_now"]["rank2_vs_rank3_type_mismatch_exposed"],
        "q79_phifin_alpha1_negative_gate_imported": q79_phifin["theorem"]["proved"] is True,
        "formal_lift_rejected_as_proof": True,
        "target_fitting_excluded": (
            run["verdict"]["observed_flavor_data_used"] is False
            and sm_solve["target_fitting_used"] is False
            and q79_phifin["target_fitting_used"] is False
        ),
    }

    what_remains_open = {
        "selected_A_HYM_or_H_coefficients": True,
        "selected_gauge_fixed_residual_values": True,
        "coercivity_and_truncation_certificate": True,
        "rank2_to_sector_operator_functor": True,
        "selected_DE_Riesz_Green_dotD_values": True,
        "selected_zero_mode_bases_and_primitive_C1_contractions": True,
        "selected_A_selected_and_b_selected_emission": True,
    }

    guardrails = {
        "does_not_use_observed_flavor_data": True,
        "does_not_use_benchmark_entries": True,
        "does_not_promote_formal_lift_flags": True,
        "does_not_use_abstract_hym_existence_as_values": True,
        "does_not_promote_identity_smoke_rhoE": True,
        "does_not_claim_full_sm_closure": True,
    }

    packet = {
        "theorem": theorem,
        "attempted_routes": attempted_routes,
        "legal_value_solve_closed": legal_value_solve_closed,
        "gauge_fixed_problem": {
            "rank": hym_problem["rank"],
            "bundle": hym_problem["bundle"],
            "unknown": hym_problem["unknown"],
            "residual_equations": hym_problem["residual_equations"],
        },
        "finite_newton_galerkin_contract": finite_contract,
        "source_alpha1_reduction": {
            "status": source_alpha1["status"],
            "repair_object": source_alpha1["superset_mode"]["superset_repair"]["repair_object"],
            "selected_phifin_alpha1_payload_open": source_alpha1["what_remains_open"]["selected_PhiFin_alpha1_payload"],
        },
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "guardrails": guardrails,
        "next_required_artifact": NEXT,
        "input_certificates": {
            "extraction_run": str(RUN_CERT),
            "theorem_insertions": str(INSERTION_CERT),
            "sm_gaugefixed_solve": str(SM_SOLVE_CERT),
            "q79_phifin_alpha1": str(Q79_PHIFIN_CERT),
        },
    }

    checks = {
        "extraction_criterion_available": insertion["theorem"]["proved"] is True,
        "current_run_still_no_values": run["verdict"]["selected_values_emitted"] is False,
        "sm_solve_contract_built": sm_solve["finite_newton_galerkin_contract_built"] is True,
        "sm_first_solve_not_closed": sm_solve["first_solve_closed"] is False,
        "rank2_sector_functor_not_emitted": sm_solve["rank2_to_sector_functor_emitted"] is False,
        "q79_phifin_gate_negative": q79_test["can_close_selected_phifin_alpha1_payload_now"] is False,
        "q79_selected_flags_not_all_true": q79_test["selected_payload_flags_all_true"] is False,
        "no_target_fitting": what_closes_now["target_fitting_excluded"] is True,
        "legal_solve_not_closed": legal_value_solve_closed is False,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_hym_value_solve_attempt",
        "status": STATUS,
        "theorem": theorem,
        "checks": checks,
        "attempted_routes": attempted_routes,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "guardrails": guardrails,
        "legal_value_solve_closed": legal_value_solve_closed,
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected HYM Value Solve Attempt v1

## Result

The value solve was attempted, but it does not close with the current corpus and
repo artifacts.

What is now available:

```text
selected extraction criterion
gauge-fixed rank-2 HYM equation system
finite Newton/Galerkin solve contract
27-mode execution scaffold
q79 Phi_fin alpha1 finite codomain and support checks
```

What is still absent:

```text
selected A_HYM or H coefficient vector
selected gauge-fixed residual and truncation/error certificate
rank-2-to-sector transfer functor
selected D_E, Riesz/Green, dotD, and primitive C1 payload values
A_selected and b_selected
```

The legal value solve is therefore not closed. Formal lifted flags and smoke
packets are again rejected as proof.

## Theorem

`SelectedHYMValueSolveAttemptNoGo` is proved.

The exact status is:

```text
{STATUS}
```

The next executable artifact is:

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
