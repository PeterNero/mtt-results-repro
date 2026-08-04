"""Audit selected T_scheme/lambda_H source rows or K_threshold closure attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
READINESS = PACKET_DIR / "post_charged_lrowlocal_threshold_readiness_recheck.packet.json"
IDENTITY_TRIAL = PACKET_DIR / "identity_tscheme_neutral_trial.packet.json"
LAMBDA_GATE = PACKET_DIR / "lambda_h_payload_gate_after_charged_lrows.packet.json"
K_GATE = PACKET_DIR / "kthreshold_gate_after_tscheme_lambdah_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_tscheme_lambdah_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TSchemeLambdaHSourceRows_or_KThresholdRowClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_TSCHEMELAMBDAH_SOURCEROWS_OR_KTHRESHOLDROWCLOSURE_"
    "BUILT_IDENTITY_TRIAL_NEEDS_SOURCE_THEOREM_LAMBDAH_OPEN"
)
NEXT = "MTT_Selected_NeutralTSchemeSourcePrinciple_or_LambdaHSectorPayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_close(value: float, expected: float, message: str) -> None:
    require(abs(float(value) - expected) < 1e-12, message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local theorem/gate")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    readiness = load(READINESS)
    identity = load(IDENTITY_TRIAL)
    lambda_gate = load(LAMBDA_GATE)
    k_gate = load(K_GATE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("readiness", readiness),
        ("identity trial", identity),
        ("lambda gate", lambda_gate),
        ("K gate", k_gate),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["charged_strict_Lrowlocal_row_count"] == 9, "charged L count mismatch")
    require(decision["identity_T_scheme_trial_row_count"] == 9, "identity trial count mismatch")
    require(decision["identity_T_scheme_selected"] is False, "identity T_scheme overselected")
    require(decision["selected_T_scheme_source_row_count"] == 0, "T_scheme rows overemitted")
    require(
        decision["conditional_charged_K_row_count_if_identity_T_scheme_selected"] == 9,
        "conditional charged K count mismatch",
    )
    require(decision["selected_lambda_H_payload_emitted"] is False, "lambda_H overemitted")
    require(decision["accepted_selected_K_source_row_count"] == 0, "K rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(
        decision["external_threshold_mass_profile_rows_are_support_not_selectors"] is True,
        "external support classification missing",
    )
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclaimed")

    support = readiness["closed_support"]
    for key in [
        "retarded_overlap_spectral_pairing_lemma_proved",
        "strict_charged_Lrowlocal_rows_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "admitted_external_threshold_matching_rows_closed",
        "admitted_external_mass_scheme_rows_closed",
        "accepted_diagonal_profile_theorem_closed",
        "combined_K_threshold_product_grammar_closed",
        "finite_heat_torsion_prefactor_subsource_closed",
    ]:
        require(support[key] is True, f"readiness support missing {key}")
    require(
        readiness["support_classification"][
            "external_threshold_mass_profile_rows_are_admitted_replay_not_internal_selectors"
        ]
        is True,
        "external replay classification missing",
    )
    require(readiness["support_classification"]["samebranch_readiness_8_of_9_retained"] is True, "8/9 lost")
    require(
        readiness["support_classification"]["only_remaining_readiness_blocker_from_step56"]
        == "no_knob_value_derivation",
        "step56 blocker mismatch",
    )
    require(readiness["still_open"]["selected_T_scheme_source_row_count"] == 0, "readiness T overclosed")
    require(readiness["still_open"]["selected_lambda_H_payload_emitted"] is False, "readiness lambda overclosed")
    require(readiness["still_open"]["accepted_selected_K_source_row_count"] == 0, "readiness K overclosed")

    require(
        identity["status"]
        == "IDENTITY_TSCHEME_TRIAL_BUILDS_NINE_CONDITIONAL_CHARGED_K_ROWS_BUT_IS_NOT_SELECTED",
        "identity status mismatch",
    )
    require(identity["trial_formula"] == "T_scheme_i = 1", "identity formula mismatch")
    require(identity["preconditions"]["strict_charged_Lrowlocal_rows_closed"] is True, "charged L precondition")
    require(identity["preconditions"]["combined_K_threshold_product_grammar_closed"] is True, "K grammar")
    require(identity["preconditions"]["observed_values_used"] is False, "observed values used")
    require(identity["row_count"] == 9, "identity row count mismatch")
    require(identity["conditional_charged_K_row_count_if_selected"] == 9, "conditional K count mismatch")
    require(identity["selected_T_scheme_source_row_count"] == 0, "identity T rows overemitted")
    require(identity["identity_T_scheme_selected"] is False, "identity selected")
    for phrase in [
        "no same-branch source theorem currently emits neutral T_scheme_i=1",
        "Step55 threshold/mass rows are admitted-external replay support, not internal no-knob selectors",
        "promoting identity by default would insert an unselected convention as a hidden knob",
    ]:
        require(phrase in identity["why_not_selected"], f"identity reason missing {phrase}")

    expected_by_gen = {1: 1.367835979172, 2: 0.683917989586, 3: 0.683917989586}
    seen = {(row["sector"], row["generation"]) for row in identity["rows"]}
    require(seen == {(sector, gen) for sector in ["u", "d", "e"] for gen in [1, 2, 3]}, "identity rows missing")
    for row in identity["rows"]:
        require(row["identity_T_scheme_candidate_value"] == 1.0, "identity value mismatch")
        require(row["accepted_as_selected_T_scheme_source_row"] is False, "identity row overaccepted")
        require(row["accepted_as_selected_K_threshold_row"] is False, "K row overaccepted")
        require(row["identity_T_scheme_selected"] is False, "identity row selected")
        require(row["observed_data_used_as_selector"] is False, "identity observed selector")
        require(row["target_fitting_used"] is False, "identity target fitting")
        require_close(
            row["conditional_K_threshold_value_if_identity_selected"],
            expected_by_gen[row["generation"]],
            f"{row['omega_id']} conditional K mismatch",
        )

    require(
        lambda_gate["status"] == "H_SECTOR_LAMBDAH_PAYLOAD_STILL_OPEN_AFTER_CHARGED_LROWS",
        "lambda gate status mismatch",
    )
    require(lambda_gate["omega_id"] == "Omega_H.lambda", "lambda omega mismatch")
    require(lambda_gate["H_sector_Lrowlocal_available"] is False, "H L row overemitted")
    require(lambda_gate["selected_lambda_H_payload_emitted"] is False, "lambda payload overemitted")
    require(lambda_gate["lambda_H_value_row_emitted"] is False, "lambda value overemitted")
    require(lambda_gate["T_scheme_Omega_H_lambda_source_row_emitted"] is False, "H T_scheme overemitted")
    require(lambda_gate["combined_K_threshold_H_lambda_emitted"] is False, "H K overemitted")
    require(lambda_gate["accepted_as_no_knob_source_row"] is False, "lambda no-knob overaccepted")
    for phrase in [
        "charged spectral-pairing lemma covers u,d,e only",
        "no H-sector row-local overlap/quartic payload is emitted",
        "external Higgs replay values remain postchecks and cannot select lambda_H",
    ]:
        require(phrase in lambda_gate["blocking_reasons"], f"lambda reason missing {phrase}")

    require(
        k_gate["status"] == "CONDITIONAL_CHARGED_K_ROWS_BUILT_IDENTITY_TSCHEME_AND_LAMBDAH_NOT_SELECTED",
        "K gate status mismatch",
    )
    require(k_gate["row_count"] == 10, "K gate row count mismatch")
    require(k_gate["strict_charged_Lrowlocal_row_count"] == 9, "K gate charged count mismatch")
    require(k_gate["identity_T_scheme_trial_row_count"] == 9, "K gate identity count mismatch")
    require(k_gate["conditional_identity_charged_K_rows_if_selected"] == 9, "K gate conditional count mismatch")
    require(k_gate["selected_T_scheme_source_row_count"] == 0, "K gate T overemitted")
    require(k_gate["selected_lambda_H_payload_emitted"] is False, "K gate lambda overemitted")
    require(k_gate["accepted_selected_K_source_row_count"] == 0, "K gate K overaccepted")
    require(k_gate["accepted_internal_scalar_value_row_count"] == 0, "K gate scalar overaccepted")
    for row in k_gate["rows"]:
        if row["sector"] == "H":
            require(row["strict_L_rowlocal_available"] is False, "H strict L overemitted")
            require(row["identity_T_scheme_candidate_available"] is False, "H identity overemitted")
            require(row["conditional_K_threshold_value_if_identity_selected"] is None, "H conditional K")
            require(row["selected_lambda_H_payload_emitted"] is False, "H lambda overemitted")
            require("selected lambda_H H-sector payload is not emitted" in row["blocking_reasons"], "H blocker")
        else:
            require(row["strict_L_rowlocal_available"] is True, "charged L missing")
            require(row["identity_T_scheme_candidate_available"] is True, "charged identity missing")
            require(row["identity_T_scheme_candidate_value"] == 1.0, "charged identity value")
            require(row["identity_T_scheme_selected"] is False, "charged identity selected")
            require(row["conditional_K_threshold_value_if_identity_selected"] is not None, "charged conditional K")
            require("neutral identity T_scheme is only a trial, not a selected source theorem" in row["blocking_reasons"], "charged blocker")
        require(row["selected_T_scheme_source_row_emitted"] is False, "row T overemitted")
        require(row["selected_K_threshold_row_emitted"] is False, "row K overemitted")
        require(row["accepted_as_no_knob_source_row"] is False, "row no-knob overaccepted")
        require(row["observed_data_used_as_selector"] is False, "row observed selector")
        require(row["target_fitting_used"] is False, "row target fitting")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "charged strict L_rowlocal rows imported as closed source rows",
        "neutral identity T_scheme trial executed without observed data",
        "nine conditional charged K_threshold values built if identity T_scheme is later selected",
        "H/lambda_H obstruction isolated from the charged L_rowlocal closure",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected neutral/identity T_scheme source theorem or nontrivial internal T_scheme rows",
        "selected lambda_H H-sector quartic/threshold payload",
        "ten selected K_threshold rows",
        "strict Omega/lambda_H scalar execution",
        "matrix-level mixing extension and true SM equivalence",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "neutral identity `T_scheme_i=1` trial rows built: `9`",
        "conditional charged `K_threshold` rows if identity is later selected: `9`",
        "selected `T_scheme.*` source rows emitted: `false`",
        "selected `lambda_H` payload emitted: `false`",
        "accepted selected `K_threshold` rows: `0`",
        "- u.gen1: 1.367835979172",
        "- d.gen2: 0.683917989586",
        "- e.gen3: 0.683917989586",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
