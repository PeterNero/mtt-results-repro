"""Audit Route-C Weyl-pair basis-transport / vertex source theorem gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
CERT = REPO / "certificates" / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_WeylPair_BasisTransport_or_Vertex_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_BASISTRANSPORT_OR_VERTEX_SOURCE_GATE_BUILT_ALGEBRAICALLY_SUFFICIENT_SOURCE_PROOF_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    strategy = data["superset_strategy"]
    theorem = data["theorem_gate"]
    packet = data["enriched_weyl_pair_packet"]
    span = data["span_test"]
    source = data["source_contract"]
    paper = data["paper_update_record"]
    draft_texts = {
        key: (REPO / path).read_text(encoding="utf-8")
        for key, path in paper["draft_paths"].items()
    }

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "superset guardrails",
            strategy["mode"] == "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET"
            and strategy["observed_data_used"] is False
            and strategy["lifted_flags_used_as_proof"] is False
            and strategy["target_fitting_used"] is False,
            strategy,
        ),
        check(
            "theorem gate named and guarded",
            theorem["name"] == "SelectedWeylPairBasisTransportOrVertexSourceTheorem"
            and theorem["status"] == "ALGEBRAIC_GATE_BUILT_SOURCE_PROOF_OPEN"
            and theorem["proved_now"]["primitive_only_span_insufficient_imported"] is True
            and theorem["proved_now"]["minimal_weyl_pair_reconstructs_locked_splitter"] is True
            and theorem["not_proved_now"]["same_branch_weyl_pair_source_provenance"] is True,
            theorem,
        ),
        check(
            "weyl packet contains required components",
            "X" in packet["basis"]
            and "Z" in packet["basis"]
            and "phase_packet" in packet["source_directions"]
            and "shift_packet" in packet["source_directions"],
            packet["source_directions"],
        ),
        check(
            "span exactly reaches locked target",
            span["target_dimension"] == 72
            and span["target_in_span"] is True
            and span["residual_norm"] <= 1e-10
            and span["direct_packet_sum_residual_norm"] <= 1e-10
            and span["columns"] == ["phase_packet", "shift_packet"],
            span,
        ),
        check(
            "selected operator still not emitted",
            source["operator_emission_status_imported"]["A_selected_currently_emitted"] is False
            and source["operator_emission_status_imported"]["b_selected_currently_emitted"] is False,
            source["operator_emission_status_imported"],
        ),
        check(
            "paper drafts guarded",
            paper["id"] == "I8_weylpair_basis_transport_or_vertex_source_theorem"
            and len(paper["draft_paths"]) == 3
            and all("Safe Wording Before Proof" in text for text in draft_texts.values())
            and all("not yet a selected source proof" in text for text in draft_texts.values()),
            paper,
        ),
        check(
            "what closes and remains",
            data["what_closes_now"]["locked_splitter_reconstructed_by_weyl_pair"] is True
            and data["what_remains_open"]["assemble_theorem_derived_A_selected"] is True
            and data["what_remains_open"]["solve_or_reject_locked_deltaTheta_C1_equation"] is True,
            {"closes": data["what_closes_now"], "open": data["what_remains_open"]},
        ),
        check(
            "no closure or fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records result",
            "minimal enriched Weyl-pair packet exactly reconstructs" in note
            and "No SM closure is claimed" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C Weyl-pair source theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
