"""Build the minimal smooth-closure source request or direct no-go artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "source_search": DATA / "selected_heterotic_projectiverhoe_exactcomplementfactorization_or_goodcovertransitiontables_sourcesearch.candidate.json",
    "minimal_request": DATA / "selected_heterotic_projectiverhoe_minimal_smooth_closure_source_request.json",
    "value_packet": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
    "smooth_trace_lift": DATA / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json",
    "smooth_source_fill": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_minimalsmoothclosure_sourcerequest_or_directnogo.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_minimalsmoothclosure_sourcerequest_or_directnogo_certificate.json"
OUTPUT_OPEN = DATA / "selected_heterotic_projectiverhoe_minimal_smooth_closure_open_gate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_MinimalSmoothClosure_SourceRequest_or_DirectNoGo_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_MINIMAL_SMOOTH_CLOSURE_CURRENT_CORPUS_NOGO_SOURCE_REQUEST_LOCKED"
NEXT = "Selected_Heterotic_ProjectiveRhoE_NewSourceInsertion_GoodCoverTables_or_ExactFactorization_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def all_false(mapping: dict[str, bool]) -> bool:
    return all(value is False for value in mapping.values())


def main() -> dict[str, Any]:
    source_search = load(INPUTS["source_search"])
    minimal_request = load(INPUTS["minimal_request"])
    value_packet = load(INPUTS["value_packet"])
    trace_lift = load(INPUTS["smooth_trace_lift"])
    smooth_source_fill = load(INPUTS["smooth_source_fill"])

    blockers = minimal_request["current_blockers"]
    already_closed = minimal_request["already_closed"]

    no_go_conditions = {
        "finite_internal_packet_closed": all(already_closed.values()),
        "current_blockers_all_absent": all_false(blockers),
        "source_search_found_no_values": source_search["decision"]["goodcover_transition_values_found"] is False
        and source_search["decision"]["exact_complement_factorization_found"] is False,
        "smooth_trace_lift_current_source_nogo": trace_lift["decision"]["current_source_no_go_for_trace_lift"] is True,
        "smooth_operator_source_packet_values_absent": smooth_source_fill["decision"]["smooth_operator_source_packet_filled"] is False,
    }

    open_gate = {
        "schema": "SelectedHeteroticProjectiveRhoEMinimalSmoothClosureOpenGate.v1",
        "status": "OPEN_REQUIRES_NEW_SOURCE_INSERTION",
        "closed_without_new_source": {
            "finite_internal_projection_packet": already_closed["finite_internal_projection_packet"],
            "finite_tau_rhoE_DE_Green_Riesz_chi_logdet": already_closed["finite_tau_rhoE_DE_Green_Riesz_chi_logdet"],
            "no_double_count_policy": already_closed["no_double_count_policy"],
            "internal_value_packet_status": value_packet["status"],
        },
        "cannot_close_without_new_source": blockers,
        "two_legal_new_source_insertions": minimal_request["minimal_acceptable_payloads"],
        "acceptance_tests_after_insertion": [
            "re-run focused source-request audit with all current blockers true for one payload lane",
            "re-run smooth source-packet fill with selected transition/factorization values present",
            "prove either smooth_transition_tables_emitted or exact_smooth_complement_quotient_closed",
            "derive E_Qa or finite_part_value only after one source lane closes",
            "full python scripts\\verify.py must pass without target fitting",
        ],
        "forbidden_shortcuts": minimal_request["forbidden_shortcuts"],
    }

    decision = {
        "direct_current_corpus_nogo_proved": all(no_go_conditions.values()),
        "source_request_locked": True,
        "finite_internal_closure_preserved": True,
        "smooth_finitepart_can_close_now": False,
        "requires_new_source_insertion": True,
        "goodcover_transition_tables_required_or": "exact_complement_factorization_required",
        "next_required_artifact": NEXT,
        "open_gate_path": rel(OUTPUT_OPEN),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEMinimalSmoothClosureSourceRequestOrDirectNoGo",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "no_go_conditions": no_go_conditions,
        "decision": decision,
        "closed_internal_value_summary": {
            "labels": value_packet["finite_internal_values"]["labels"],
            "finite_internal_part": value_packet["finite_internal_values"]["finite_internal_part"],
            "chi_Qa": value_packet["finite_internal_values"]["chi_Qa"],
            "no_double_count_policy_closed": value_packet["lane_B_exact_complement_quotient"]["BRST_FP_gauge_quotient_counted_once"]["closed"],
        },
        "remaining_source_values": blockers,
        "guardrails": {
            "does_not_claim_smooth_finitepart": True,
            "does_not_claim_E_Qa": True,
            "does_not_promote_support_to_source_values": True,
            "does_not_promote_finite_packet_to_smooth_tables": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "MinimalSmoothClosureCurrentCorpusNoGo",
            "proved": True,
            "statement": (
                "Given the current repository and scanned corpus, smooth closure of the "
                "heterotic projective rho_E branch cannot be completed without a new "
                "source insertion. The finite internal packet, finite representative, "
                "internal projection, and no-double-count policy are closed; however "
                "the selected smooth good-cover/transition-table payload and the exact "
                "heat/zeta/torsion complement-factorization payload are both absent. "
                "Therefore any further closure must add one of those source payloads "
                "and pass the listed audits, not normalize or target-fit the existing "
                "finite packet."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_OPEN.write_text(json.dumps(open_gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "open_gate_path": rel(OUTPUT_OPEN),
        "note_path": rel(OUTPUT_NOTE),
        "direct_current_corpus_nogo_proved": decision["direct_current_corpus_nogo_proved"],
        "source_request_locked": True,
        "requires_new_source_insertion": True,
        "smooth_finitepart_can_close_now": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE MinimalSmoothClosure SourceRequest or DirectNoGo v1

## Result

```text
status = {STATUS}
direct_current_corpus_nogo_proved = true
source_request_locked = true
requires_new_source_insertion = true
smooth_finitepart_can_close_now = false
next_required_artifact = {NEXT}
```

## Closed Before This Gate

- finite internal projection packet
- finite `tau/rho_E/D_E/Green/Riesz/chi_Qa/log(2008)` value packet
- no-double-count policy

## Direct No-Go

The current corpus does not contain either selected smooth good-cover/projective
transition tables or an exact Qa/SU3 heat/zeta/torsion complement-factorization
theorem. Smooth closure therefore requires a new source insertion, recorded in:

```text
{rel(OUTPUT_OPEN)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_OPEN)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
