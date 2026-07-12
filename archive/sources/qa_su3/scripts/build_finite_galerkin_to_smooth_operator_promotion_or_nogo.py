"""Build the finite-Galerkin-to-smooth-operator promotion/no-go artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SM_PARITY = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

FINITE = DATA / "minimal_hsel_gret_finite_galerkin_candidate.candidate.json"
PACKET = DATA / "hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json"
SM_INTERFACE = SM_PARITY / "candidate_data" / "selected_qa_su3_color_bundle_connection_endomorphism_interface.candidate.json"
SM_IMPORT = SM_PARITY / "candidate_data" / "selected_qa_su3_operator_source_import_audit.candidate.json"

OUTPUT_DATA = DATA / "finite_galerkin_to_smooth_operator_promotion_or_nogo.candidate.json"
OUTPUT_CERT = CERTS / "finite_galerkin_to_smooth_operator_promotion_or_nogo_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Finite_Galerkin_to_Smooth_Operator_Promotion_or_NoGo_v1.md"


def load_optional(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"present": False, "path": str(path)}
    data = json.loads(path.read_text(encoding="utf-8"))
    data["present"] = True
    data["path"] = str(path)
    return data


def weighted_hessian_coefficients(charges: dict[str, list[int]]) -> dict[str, dict[str, int]]:
    entries = {
        "H11": (0, 0),
        "H12": (0, 1),
        "H13": (0, 2),
        "H22": (1, 1),
        "H23": (1, 2),
        "H33": (2, 2),
    }
    return {
        entry: {label: q[i] * q[j] for label, q in charges.items()}
        for entry, (i, j) in entries.items()
    }


def evaluate_sources(sm_interface: dict[str, object], sm_import: dict[str, object]) -> dict[str, object]:
    imported = sm_interface.get("imported_evidence", {}) if sm_interface.get("present") else {}
    source_payload = sm_interface.get("selected_interface", {}).get("source_payload_required", []) if sm_interface.get("present") else []
    routec = imported.get("routec_gate", {})
    spectral = imported.get("spectral_fallback", {})
    compact_nil = imported.get("compact_nil_operator_packet_fill", {})
    import_routes = sm_import.get("import_routes", []) if sm_import.get("present") else []
    best_route = next((row for row in import_routes if row.get("rank") == 1), {})
    return {
        "sm_interface_present": sm_interface.get("present", False),
        "sm_import_audit_present": sm_import.get("present", False),
        "same_source_operator_packet_promoted": sm_interface.get("gate_results", {}).get("operator_packet_promoted") is True,
        "compact_nil_same_branch_source_found": compact_nil.get("same_branch_source_found") is True,
        "routec_current_source_exhausted": routec.get("status") == "QA_SU3_ROUTEC_SOURCE_SOLVE_GATE_CURRENT_SOURCE_EXHAUSTED_NEW_SOURCE_REQUIRED",
        "spectral_fallback_source_solve_open": spectral.get("status") == "QA_SU3_SPECTRAL_FALLBACK_REDUCED_TO_SELECTED_SOURCE_SOLVE",
        "best_operator_route": best_route.get("id"),
        "best_operator_route_promoted": best_route.get("promoted_now") is True,
        "source_payload_required": source_payload,
    }


def build() -> tuple[dict[str, object], dict[str, object], str]:
    finite = json.loads(FINITE.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    sm_interface = load_optional(SM_INTERFACE)
    sm_import = load_optional(SM_IMPORT)
    charges = packet["twist_projection"]["charge_table"]
    coefficients = weighted_hessian_coefficients(charges)
    source_eval = evaluate_sources(sm_interface, sm_import)
    weighted_gate = {
        "general_formula": "H_smooth|charge = Q^T W Q plus any off-charge/operator corrections; W must be supplied by the selected smooth/operator source.",
        "unweighted_candidate": "W=I gives the finite Galerkin H_sel already validated.",
        "entry_coefficients_for_H_QT_W_Q": coefficients,
        "unit_weight_equations": {
            "H11": 26,
            "H12": -3,
            "H13": 0,
            "H22": 10,
            "H23": 0,
            "H33": 8,
        },
        "why_weights_matter": [
            "arbitrary positive weights generally change H_sel and G_ret",
            "arbitrary weights can couple the c-axis to K1/K2 through H13/H23",
            "the primitive +e3 selector is proved for the validated unweighted block, not for an arbitrary smooth operator block",
        ],
    }
    source_theorem_tests = [
        {
            "id": "same_source_smooth_operator",
            "required": "selected Qa/SU3 D_E/rho_E/HYM/Strominger operator on the same twisted module",
            "current_result": source_eval["same_source_operator_packet_promoted"],
            "verdict": "OPEN",
        },
        {
            "id": "charge_factorization",
            "required": "smooth Hessian restricted to the selected sector factors through the typed charge map Q",
            "current_result": False,
            "verdict": "NOT_FOUND_IN_CURRENT_SOURCE",
        },
        {
            "id": "unit_weight_or_selected_weight_metric",
            "required": "W=I by same-source modal democracy, or exact selected W with recomputed H/G/tau",
            "current_result": False,
            "verdict": "MODAL_DEMOCRACY_FOUND_ONLY_AS_TIER2_ASSUMPTION",
        },
        {
            "id": "admissibility_and_projector",
            "required": "Freed-Witten, Bianchi, projector retention, zero-mode policy on the smooth source",
            "current_result": False,
            "verdict": "PARTIAL_CONTEXT_ONLY",
        },
        {
            "id": "determinant_finite_part",
            "required": "heat/zeta/torsion/spectrum finite response from the same operator",
            "current_result": False,
            "verdict": "OPEN",
        },
    ]
    current_promotes = all(test["current_result"] is True for test in source_theorem_tests)
    candidate = {
        "candidate": "SelectedQaSU3FiniteGalerkinToSmoothOperatorPromotionOrNoGo",
        "status": "QA_SU3_FINITE_GALERKIN_TO_SMOOTH_OPERATOR_PROMOTION_CURRENT_SOURCE_NO_GO_CONDITIONAL_THEOREM_BUILT",
        "input_finite_candidate": str(FINITE.relative_to(ROOT)),
        "input_filled_packet": str(PACKET.relative_to(ROOT)),
        "finite_result_reused": {
            "H_sel": finite["hessian"]["matrix"],
            "G_ret": finite["green"]["matrix"],
            "Pi_tw": finite["selection_proof"]["selected_covector"],
            "tau": finite["tau"]["values"],
            "validator_passed": finite["validator_result"]["exit_code"] == 0,
        },
        "conditional_promotion_theorem": {
            "statement": "If the selected smooth Qa/SU3 Hessian on the twisted source sector factors as Q^T W Q with source-selected W=I on the eleven typed labels, and the smooth operator supplies the same admissibility and determinant response, then the finite Galerkin packet promotes to the smooth/operator Hessian block.",
            "proof_skeleton": [
                "The charge map Q sends the eleven selected module labels to the three charge coordinates.",
                "For W=I, Q^T W Q is exactly the computed positive block [[26,-3,0],[-3,10,0],[0,0,8]].",
                "The exact inverse is the computed G_ret, so the retarded kernel identity holds on the Galerkin block.",
                "The P-annihilator twisted primitive minimization selects +e3, giving the tau table and twist cancellation.",
                "A same-source smooth operator with the same projected Hessian and finite response transfers these finite identities to the selected operator packet.",
            ],
            "not_a_closure_without": [
                "same-source proof of the factorization",
                "source-selected W=I or exact W with recomputation",
                "smooth D_E/rho_E or HYM/Strominger operator",
                "admissibility and determinant finite part",
            ],
        },
        "weighted_hessian_gate": weighted_gate,
        "source_theorem_tests": source_theorem_tests,
        "source_evaluation": source_eval,
        "decision": {
            "promotes_now": current_promotes,
            "current_source_no_go": not current_promotes,
            "reason": "The finite candidate is validated, but the current corpus/repo set does not source-select the smooth operator, charge-factorization theorem, or unit/selected weight metric required to promote it.",
            "best_next_artifact": "Selected_Qa_SU3_Weighted_Hessian_Source_or_Same_Source_Operator_Solve_v1",
        },
        "what_this_closes": [
            "exact conditional theorem for promoting the finite candidate",
            "explicit weighted-Hessian obstruction gate",
            "current-source no-go for promotion without extra source data",
            "clean separation between Tier-2 modal democracy and proof-level same-source selection",
        ],
        "what_remains_open": [
            "selected same-source operator packet",
            "selected weight metric W or proof W=I",
            "smooth admissibility/projector checks",
            "determinant finite part",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3FiniteGalerkinToSmoothOperatorPromotionOrNoGo",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "conditional_promotion_theorem_built": True,
            "weighted_hessian_gate_built": True,
            "current_source_promotion_no_go": True,
            "finite_candidate_preserved": True,
        },
        "what_remains_open": {
            "same_source_smooth_operator": True,
            "charge_factorization_proof": True,
            "selected_weight_metric_or_unit_democracy": True,
            "full_admissibility_packet": True,
            "determinant_finite_part": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["decision"]["best_next_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = render_note(candidate)
    return candidate, certificate, note


def render_note(candidate: dict[str, object]) -> str:
    return f"""# Selected Qa/SU3 Finite Galerkin to Smooth Operator Promotion or No-Go v1

## Verdict

The finite Galerkin candidate is preserved, but it does not yet promote to full
smooth Qa/SU3 closure.

```text
promotes now: {candidate["decision"]["promotes_now"]}
current-source no-go: {candidate["decision"]["current_source_no_go"]}
```

## Conditional Promotion Theorem

If the selected smooth Qa/SU3 Hessian on the twisted source sector factors as:

```text
H_smooth|charge = Q^T W Q
```

and the same source selects `W=I` on the eleven typed labels, then the validated
finite block promotes:

```text
H_sel = {candidate["finite_result_reused"]["H_sel"]}
G_ret = {candidate["finite_result_reused"]["G_ret"]}
Pi_tw = {candidate["finite_result_reused"]["Pi_tw"]}
```

The proof is now exact and short: `Q^T Q` is the computed block, its inverse is
the computed retarded Green kernel, and the primitive twisted `P`-annihilator
minimization selects `+e3`, which gives the existing `tau` table.

## Why It Does Not Promote Yet

The current corpus supports Galerkin approximation, positive Hessian/coercivity,
and Tier-2 modal-democracy language.  But those do not by themselves prove that
the Qa/SU3 smooth threshold operator has:

```text
same-source operator: no
charge factorization Q^T W Q: no
source-selected W=I or exact W: no
determinant finite part: no
```

Modal democracy is useful as a candidate symmetry assumption, but in the current
source record it is not a same-branch Qa/SU3 operator-source theorem.

## Weighted Hessian Gate

The correct next object is not just another unweighted calculation.  A smooth
operator can change the block to:

```text
H(W)=Q^T W Q
```

with source-selected weights `W`.  Arbitrary weights can change `G_ret` and mix
the `c` axis with `K1/K2`, so the `+e3` selector must either be rederived for
the selected `W`, or `W=I` must be proved from the same source.

## Next Artifact

```text
{candidate["decision"]["best_next_artifact"]}
```

That artifact should either supply a selected weight metric/operator packet and
recompute the weighted Hessian, or prove that no current source can provide it.
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
