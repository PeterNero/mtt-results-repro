"""Build q79 retarded/source boundary selector reduction."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = CERTS / "q79_routec_phifin_dotd_alpha1_source_identity_attempt_certificate.json"
ORBIT = CERTS / "visible_representative_selection_orbit_certificate.json"
FUNCTIONAL = CERTS / "selected_visible_source_functional_on_orbit_classification_certificate.json"
CUTSET = CERTS / "selected_qa_su3_m1_operator_cutset_certificate.json"
CW_ATTEMPT = CERTS / "selected_qa_su3_m1_cw_operator_source_attempt_certificate.json"
CW_PROOF = CERTS / "selected_qa_su3_m1_cw_operator_source_proof_attempt_certificate.json"
COMMON_MAP = CERTS / "common_de_dotd_riesz_green_payload_map_certificate.json"
ANTIUNITARY = CERTS / "antiunitary_dedotd_equivalence_test_certificate.json"

OUT_PACKET = DATA / "q79_retarded_source_boundary_selector_or_source_origin.candidate.json"
OUT_CERT = CERTS / "q79_retarded_source_boundary_selector_or_source_origin_certificate.json"
OUT_NOTE = CORPUS / "Q79_Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1.md"

STATUS = "Q79_RETARDED_SOURCE_SELECTOR_REDUCED_TO_SAMESOURCE_CW_OPERATOR_FUNCTIONAL"
NEXT = "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def local(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    orbit = load(ORBIT)
    functional = load(FUNCTIONAL)
    cutset = load(CUTSET)
    cw_attempt = load(CW_ATTEMPT)
    cw_proof = load(CW_PROOF)
    common = load(COMMON_MAP)
    anti = load(ANTIUNITARY)

    checks = {
        "previous_names_this_gate": previous["verdict"]["next_required_artifact"]
        == "Q79_Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1",
        "antiunitary_orbit_retained": orbit["closed_now"]["antiunitary_orbit_is_the_correct_current_object"]
        is True
        and orbit["guardrails"]["claims_q79_visible_selected"] is False,
        "selector_still_open": orbit["still_open"]["selected_retarded_source_functional_on_orbit"]
        is True
        and orbit["still_open"]["which_representative_is_visible"] is True,
        "functional_classification_points_to_CW": functional["next_closing_object"]["name"]
        == NEXT
        and functional["guardrails"]["claims_visible_q79_selected_now"] is False,
        "cutset_points_to_CW": cutset["next_object"]["name"] == NEXT
        and cutset["cut_set"]["antiunitary_equivalence_or_retarded_branch_selection"] is True,
        "common_payload_map_points_to_CW": common["path_decision"][
            "construct_Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1_is_correct"
        ]
        is True,
        "CW_attempt_not_closed": cw_attempt["attempt_result"]["cw_operator_source_constructed"]
        is False
        and cw_attempt["not_closed"]["derive_same_total_source_D_E_dotD_Riesz_Green"]
        is True,
        "CW_prefix_closed_full_theorem_open": cw_proof["theorem_proved"] is False
        and cw_proof["status"]
        == "CW_OPERATOR_SOURCE_PREFIX_CLOSED_FULL_THEOREM_SOURCE_CERTIFICATE_OPEN",
        "antiunitary_equivalence_passes_selector_open": anti["closed_now"][
            "operator_level_antiunitary_equivalence_for_current_finite_packets"
        ]
        is True
        and anti["not_closed"]["retarded_or_source_boundary_selector_for_one_representative"]
        is True,
    }
    proved = all(checks.values())

    selector_reduction = {
        "orbit_policy": "retain q79/q369 as one selected antiunitary orbit",
        "forbidden_shortcut": "do not choose q79 by observed CP sign, hand preference, or lifted source flags",
        "direct_retarded_selector_status": "not constructed",
        "best_current_visible_representative_clue": "q79/F,m=1",
        "why_not_enough": (
            "q79/F,m=1 is coherent support, but not a source theorem that "
            "acts on the orbit and emits selected D_E/dotD/C1 data."
        ),
        "correct_reduction": (
            "build the same-source Chern-Weil/operator functional; if it derives "
            "the visible row and same-source operator payload on q79/F,m=1, the "
            "visible representative is selected by source data rather than by hand."
        ),
    }

    acceptance_contract = {
        "must_prove": [
            "selected visible bundle/sheaf/Route-C source origin on the q79/q369 orbit",
            "visible Chern-Weil or equivalent operator row from that same source",
            "Pic0/quotient policy harmless for the row",
            "same-source D_E/Riesz/Green payload with theorem-derived flags",
            "same-branch dotD/alpha1 driver without lifted flags",
            "primitive C1 or target-overlap contractions from the same source",
        ],
        "must_not_use": [
            "observed CP sign",
            "observed masses or mixings",
            "benchmark flavor entries",
            "manual q79-over-q369 selection",
            "lifted selected-source flags",
        ],
    }

    return {
        "packet": "Q79_Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1",
        "status": STATUS if proved else "Q79_RETARDED_SOURCE_SELECTOR_REDUCTION_FAILED",
        "inputs": {
            "previous": local(PREVIOUS),
            "orbit": local(ORBIT),
            "functional": local(FUNCTIONAL),
            "cutset": local(CUTSET),
            "CW_attempt": local(CW_ATTEMPT),
            "CW_proof_attempt": local(CW_PROOF),
            "common_payload_map": local(COMMON_MAP),
            "antiunitary_equivalence": local(ANTIUNITARY),
        },
        "selector_checks": checks,
        "theorem": {
            "name": "Q79RetardedSourceBoundarySelectorReductionTheorem",
            "proved": proved,
            "closure_claimed": False,
            "statement": (
                "The q79/q369 visible-representative selector is reduced to the "
                "same-source Chern-Weil/operator functional. The current finite "
                "operator packets form one antiunitary orbit and cannot be treated "
                "as independent knobs. A direct retarded selector is not yet "
                "constructed; the correct next proof is a selected source origin "
                "that derives the visible Chern-Weil/operator row and same-source "
                "D_E/Riesz/Green/dotD/C1 payload without observed data or lifted flags."
            ),
        },
        "selector_reduction": selector_reduction,
        "acceptance_contract": acceptance_contract,
        "what_closes_now": {
            "retarded_selector_route_triaged": True,
            "manual_q79_selection_forbidden": True,
            "q79_q369_orbit_retained": True,
            "same_source_CW_operator_functional_selected_as_next": True,
            "acceptance_contract_for_visible_selector_written": True,
        },
        "what_remains_open": {
            "direct_retarded_boundary_functional": True,
            "selected_visible_source_origin": True,
            "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1": True,
            "same_branch_dotD_alpha1_driver": True,
            "primitive_C1_or_target_overlap_contractions": True,
            "visible_representative_selected_by_theorem": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_direct_retarded_selector_constructed": False,
            "claims_q79_selected_over_q369": False,
            "claims_CW_operator_source_closed": False,
            "claims_selected_D_E_dotD": False,
            "claims_C1_or_Yukawa_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_lifted_selected_flags": False,
        },
        "verdict": {
            "selector_closed": False,
            "reduction_proved": proved,
            "next_required_artifact": NEXT,
            "why_next": (
                "This is the first artifact that can both act on the antiunitary "
                "orbit and emit source-derived operator data. A purely formal "
                "retarded selector would still be insufficient unless it produces "
                "the same payload."
            ),
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return f"""# Q79 Retarded Source Boundary Selector or Selected Source Origin v1

## Result

Status: `{packet["status"]}`

The direct retarded/source selector is not closed.  The selector problem now
reduces to the same-source Chern-Weil/operator functional: it must act on the
q79/q369 antiunitary orbit and derive the visible representative from source
data, not from observed CP or lifted selected flags.

## Selector Reduction

```json
{json.dumps(packet["selector_reduction"], indent=2, sort_keys=True)}
```

## Acceptance Contract

```json
{json.dumps(packet["acceptance_contract"], indent=2, sort_keys=True)}
```

## Remaining Open

```json
{json.dumps(packet["what_remains_open"], indent=2, sort_keys=True)}
```

Next: `{packet["verdict"]["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    if "--write" in sys.argv:
        OUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUT_CERT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUT_NOTE.write_text(render_note(packet), encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
