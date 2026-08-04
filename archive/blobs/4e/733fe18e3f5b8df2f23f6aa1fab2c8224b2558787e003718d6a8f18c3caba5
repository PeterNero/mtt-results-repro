"""Audit selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
OBLIGATIONS = PACKET_DIR / "minimal_lemma_obligation_status.packet.json"
SUBLEMMA = PACKET_DIR / "typed_row_functor_sublemma.packet.json"
COUNTERMODEL = PACKET_DIR / "closed_support_not_enough_countermodel.packet.json"
NEXT_KERNEL = PACKET_DIR / "next_source_promotion_kernel.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "countermodel_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MinimalFiniteC1SourcePromotionLemma_Proof_or_Countermodel_v1.md"
CURRENT = (
    ROOT
    / "candidate_data"
    / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
    / "current_two_exit_source_attempt.packet.json"
)
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validator_returncode(path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.returncode


def main() -> int:
    data = load(DATA)
    obligations = load(OBLIGATIONS)
    sublemma = load(SUBLEMMA)
    countermodel = load(COUNTERMODEL)
    next_kernel = load(NEXT_KERNEL)
    validator_result = load(VALIDATOR_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_MINIMALFINITEC1SOURCEPROMOTIONLEMMA_PARTIAL_PROOF_COUNTERMODEL_BUILT", "status mismatch")
    require(data["theorem"]["proved"] is True, "partial/countermodel theorem not proved")
    require(data["full_minimal_lemma_proved"] is False, "full lemma should remain open")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(sublemma["proved"] is True, "typed row functor sublemma should be proved")
    require(sublemma["row_counts"]["primitive_rows"] == 72, "primitive row count mismatch")
    require(sublemma["row_counts"]["sector_matrix_rows"] == 36, "sector row count mismatch")
    require(sublemma["row_counts"]["hessian_source_rows"] == 2, "hessian row count mismatch")
    require(sublemma["closure_claimed"] is False, "sublemma closure overclaimed")

    require(obligations["full_lemma_proved"] is False, "obligations should keep full lemma open")
    proved_obligations = [item for item in obligations["obligations"] if item["proved"] is True]
    require(len(proved_obligations) == 1, "only typed basis-to-rows obligation should be proved")
    require(proved_obligations[0]["id"] == "basis_to_rows", "wrong proved obligation")

    require(countermodel["closed_support_facts_true"]["all_110_values"] is True, "countermodel missing closed support")
    require(countermodel["source_promotion_fields_false"]["pre_residual_phase_shift_source"] is False, "pre-residual source should remain false")
    require(countermodel["source_promotion_fields_false"]["hessian_b_selected_source"] is False, "hessian source should remain false")
    require(countermodel["source_promotion_fields_false"]["primitive_rows_provenance_independent_of_residual_projector"] is False, "primitive provenance should remain false")
    require(countermodel["closure_claimed"] is False, "countermodel closure overclaimed")

    require(len(next_kernel["must_emit"]) == 4, "next kernel must have four emission requirements")
    require("reuse exact R_Z/R_X decomposition as source selection" in next_kernel["rejected_routes"], "rejected shortcut missing")
    require(validator_result["returncode"] == 1, "recorded validator should reject countermodel/current packet")
    require(validator_returncode(CURRENT) == 1, "current packet should still fail strict validator")
    require(cert["typed_row_functor_sublemma_proved"] is True, "cert should record typed sublemma")
    require(cert["full_minimal_lemma_proved"] is False, "cert should keep full lemma open")
    require(cert["countermodel_validator_rejects"] is True, "cert should record validator rejection")
    require("full source-promotion lemma proved      = False" in note, "note missing open full-lemma statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
