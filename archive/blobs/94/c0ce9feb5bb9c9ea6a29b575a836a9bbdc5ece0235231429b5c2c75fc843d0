"""Audit primitive monad value selector theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_primitivemonadvalueselector_theorem_or_fulldeoperatorvalues.py"

SLUG = "selected_primitivemonadvalueselector_theorem_or_fulldeoperatorvalues"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveMonadValueSelectorTheorem_or_FullDEOperatorValues_v1.md"
PROOF_PACKET = PACKET_DIR / "primitive_terminal_cancellation_selector_proof.packet.json"
ACCEPTANCE_PACKET = PACKET_DIR / "selector_value_promotion_acceptance.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cech_hym_representative_or_fullde_values_contract.packet.json"

STATUS = (
    "MTT_SELECTED_PRIMITIVEMONADVALUESELECTORTHEOREM_OR_FULLDEOPERATORVALUES_"
    "SCALAR_SELECTOR_PROVED_IN_PATCHED_SPINE_FULL_VALUES_OPEN"
)
NEXT = "MTT_Selected_TerminalCechHYMRepresentative_or_FullDEOperatorValues_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    proof = load(PROOF_PACKET)
    acceptance = load(ACCEPTANCE_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, proof, acceptance, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["primitive_monad_value_selector_theorem_proved"] is True, "selector theorem not proved")
    require(decision["proved_in_patched_proof_spine"] is True, "patched-spine proof missing")
    require(decision["derived_without_terminal_axiom"] is False, "pre-axiom derivation overclaimed")
    require(decision["selected_f_g_scalar_values_accepted_as_strict_source"] is True, "f/g scalars not promoted")
    require(decision["selected_mu_scalar_values_accepted_as_strict_source"] is True, "mu scalars not promoted")
    require(decision["accepted_selector_scalar_rows"] == 3, "selector scalar row count mismatch")
    require(decision["candidate_g_after_f_zero_exact"] is True, "gf exact check failed")
    require(decision["terminal_lane_selected_compensator"] is True, "terminal compensator not selected")
    require(decision["final_same_source_connection_tables_accepted"] == 0, "final tables overaccepted")
    for key in [
        "actual_cech_hym_representative_values_emitted",
        "full_DE_operator_values_selected",
        "direct_H_K_row_emitted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclaim in decision: {key}")
        require(cert[key] is False, f"overclaim in cert: {key}")

    require(proof["selector_theorem_proved_in_patched_spine"] is True, "proof packet selector flag")
    require(proof["selector_theorem_derived_without_terminal_axiom"] is False, "proof packet overderived")
    axiom = proof["axiom_source"]
    require(axiom["applied_to_local_proof_spine"] is True, "axiom not applied locally")
    require(axiom["derived_from_prior_axioms"] is False, "axiom provenance mismatch")
    terminal = proof["terminal_source_inputs"]
    require(terminal["source_label"] == "g3 / L3-K2", "terminal label mismatch")
    require(terminal["selected_L"] == [1, -2, 0], "selected L mismatch")
    require(terminal["selected_L2"] == [2, -4, 0], "selected L2 mismatch")
    require(terminal["selected_c2"] == [4, 0, 0], "selected c2 mismatch")
    require(terminal["unique_zero_central"] is True, "zero-central uniqueness missing")
    require(terminal["unique_visible_c2"] is True, "visible c2 uniqueness missing")

    values = proof["selected_scalar_values"]
    require(values["f_entries"] == {f"a_{i}": 1 for i in range(1, 6)}, "f values mismatch")
    require(values["g_entries"] == {f"b_{i}": 1 for i in range(1, 6)}, "g values mismatch")
    require(values["multiplication_constants_mu"] == [1, 1, 1, 1, -4], "mu mismatch")
    require(values["gf_terms"] == [1, 1, 1, 1, -4], "gf terms mismatch")
    require(values["gf_sum"] == 0, "gf sum mismatch")
    require(values["gf_zero_exact"] is True, "gf exact flag mismatch")
    require(values["primitive_gcd_mu"] == 1, "primitive gcd mismatch")
    require(values["matches_prior_candidate_packet"] is True, "prior packet mismatch")
    require(proof["typing_checks"]["all_product_charge_typings_pass"] is True, "charge typing failed")
    require(proof["typing_checks"]["all_ctwist_product_typings_pass"] is True, "ctwist typing failed")
    require(proof["typing_checks"]["pure_convenience_solve_rejected_upstream"] is True, "guardrail missing")

    promoted = acceptance["promoted_now"]
    require(promoted["primitive_selector_theorem_proved_in_patched_spine"] is True, "acceptance theorem flag")
    require(promoted["selected_f_scalar_entries_promoted"] is True, "f scalar not promoted")
    require(promoted["selected_g_scalar_entries_promoted"] is True, "g scalar not promoted")
    require(promoted["selected_mu_scalar_entries_promoted"] is True, "mu scalar not promoted")
    require(promoted["accepted_selector_scalar_rows"] == 3, "promoted row count")
    still = acceptance["still_not_promoted"]
    for key in [
        "actual_11space_cochain_bases",
        "actual_Deligne_Cech_good_cover_and_cocycles",
        "selected_HYM_or_projective_connection_coefficients",
        "full_same_source_DE_or_rhoE_operator_values",
        "direct_H_K_row",
    ]:
        require(still[key] is True, f"missing remaining blocker: {key}")
    table_status = acceptance["connection_table_status"]
    require(table_status["final_same_source_connection_tables_accepted"] == 0, "accepted final tables")
    require(table_status["required_final_same_source_connection_tables"] == 8, "required final tables")

    require("Primitive monad value selector theorem: `true`" in note, "note missing theorem result")
    require("Final same-source connection tables accepted: `0/8`" in note, "note missing table boundary")
    require(NEXT in note, "note missing next artifact")

    print("Primitive monad value selector theorem audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
