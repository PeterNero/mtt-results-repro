"""Audit neutral T_scheme source-principle or lambda_H payload normal form."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraltschemesourceprinciple_or_lambdahsectorpayload"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ZERO_DELTA = PACKET_DIR / "neutral_tscheme_zero_delta_requirement.packet.json"
IDENTITY_DECISION = PACKET_DIR / "neutral_identity_route_decision.packet.json"
LAMBDA_NORMAL = PACKET_DIR / "h_sector_lambda_payload_normal_form.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_neutral_tscheme_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralTSchemeSourcePrinciple_or_LambdaHSectorPayload_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_NEUTRALTSCHEMESOURCEPRINCIPLE_OR_LAMBDAHSECTORPAYLOAD_"
    "BUILT_ZERO_DELTA_GATE_IDENTITY_NOT_SELECTED"
)
NEXT = "MTT_Selected_ThresholdDeltaRows_or_LambdaHPayloadExecution_v1"


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
    zero_delta = load(ZERO_DELTA)
    identity = load(IDENTITY_DECISION)
    lambda_normal = load(LAMBDA_NORMAL)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("zero_delta", zero_delta),
        ("identity decision", identity),
        ("lambda normal", lambda_normal),
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
    require(decision["charged_zero_delta_row_count_required_for_identity"] == 9, "zero-delta count mismatch")
    require(decision["selected_zero_delta_row_count_emitted"] == 0, "zero-delta rows overemitted")
    require(decision["selected_zero_delta_sum_theorem_emitted"] is False, "zero-delta theorem overemitted")
    require(decision["identity_T_scheme_selected"] is False, "identity T_scheme overselected")
    require(decision["selected_T_scheme_source_row_count"] == 0, "T_scheme rows overemitted")
    require(
        decision["conditional_charged_K_rows_preserved_if_zero_delta_later_selected"] == 9,
        "conditional K preservation mismatch",
    )
    require(decision["accepted_selected_K_source_row_count"] == 0, "K rows overaccepted")
    require(decision["selected_lambda_H_payload_emitted"] is False, "lambda overemitted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclaimed")

    support = zero_delta["closed_support"]
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "post_pi_formal_convention_source_contract_closed",
        "threshold_functional_contract_emitted",
        "charged_strict_Lrowlocal_rows_closed",
        "combined_K_product_gate_available",
    ]:
        require(support[key] is True, f"zero-delta support missing {key}")
    requirement = zero_delta["zero_delta_requirement"]
    require(requirement["charged_zero_delta_row_count_required_for_identity"] == 9, "zero requirement count")
    require(requirement["selected_zero_delta_row_count_emitted"] == 0, "zero rows overemitted")
    require(requirement["selected_zero_delta_sum_theorem_emitted"] is False, "zero theorem overemitted")
    require(requirement["identity_T_scheme_selected"] is False, "identity overselected")
    require("Missing rows do not equal zero rows." in requirement["reason"], "missing-zero guard absent")

    expected_by_gen = {1: 1.367835979172, 2: 0.683917989586, 3: 0.683917989586}
    seen = {(row["sector"], row["generation"]) for row in zero_delta["rows"]}
    require(seen == {(sector, gen) for sector in ["u", "d", "e"] for gen in [1, 2, 3]}, "zero rows missing")
    for row in zero_delta["rows"]:
        require(row["T_scheme_formula"] == "T_scheme = exp(Delta_threshold + Delta_mass + Delta_profile)", "formula mismatch")
        require(row["selected_Delta_threshold_row_emitted"] is False, "threshold delta overemitted")
        require(row["selected_Delta_mass_row_emitted"] is False, "mass delta overemitted")
        require(row["selected_Delta_profile_row_emitted"] is False, "profile delta overemitted")
        require(row["selected_zero_delta_sum_theorem_emitted"] is False, "zero theorem row overemitted")
        require(row["identity_T_scheme_selected"] is False, "row identity selected")
        require(row["accepted_as_selected_T_scheme_source_row"] is False, "T row accepted")
        require(row["accepted_as_selected_K_threshold_row"] is False, "K row accepted")
        require(row["observed_data_used_as_selector"] is False, "row observed selector")
        require(row["target_fitting_used"] is False, "row target fitting")
        require_close(
            row["conditional_K_threshold_value_if_zero_delta_selected"],
            expected_by_gen[row["generation"]],
            f"{row['omega_id']} conditional K mismatch",
        )

    require(
        identity["status"] == "IDENTITY_BY_SILENCE_REJECTED_ZERO_DELTA_THEOREM_REQUIRED",
        "identity status mismatch",
    )
    dec = identity["decision"]
    require(dec["neutral_identity_T_scheme_candidate_tested"] is True, "identity not tested")
    require(dec["neutral_identity_T_scheme_promoted_as_selected"] is False, "identity promoted")
    require(dec["selected_T_scheme_source_row_count"] == 0, "identity T rows overemitted")
    require(dec["conditional_charged_K_rows_preserved_if_zero_delta_later_selected"] == 9, "identity conditional count")
    require(dec["accepted_selected_K_source_row_count"] == 0, "identity K rows overaccepted")
    for phrase in [
        "the selected threshold response functional contract defines T_scheme by exponentiated delta rows",
        "absence of emitted delta rows is not a selected zero-delta theorem",
        "promoting T_scheme=1 without zero-delta source rows would introduce an unselected hidden convention",
    ]:
        require(phrase in identity["why_identity_not_promoted"], f"identity reason missing {phrase}")
    require("NullThresholdDeltaTheorem" in identity["legal_reentry_condition"], "reentry theorem missing")

    require(
        lambda_normal["status"] == "LAMBDAH_PAYLOAD_NORMAL_FORM_BUILT_SOURCE_PAYLOAD_OPEN",
        "lambda status mismatch",
    )
    req = lambda_normal["normal_form_requirement"]
    for key in [
        "H_sector_Lrowlocal_or_quartic_payload_required",
        "T_scheme_Omega_H_lambda_required",
        "selected_lambda_H_payload_required",
        "combined_K_threshold_H_lambda_required",
    ]:
        require(req[key] is True, f"lambda requirement missing {key}")
    cur = lambda_normal["current_emission"]
    require(cur["H_sector_Lrowlocal_available"] is False, "H L overemitted")
    require(cur["T_scheme_Omega_H_lambda_source_row_emitted"] is False, "H T overemitted")
    require(cur["selected_lambda_H_payload_emitted"] is False, "lambda payload overemitted")
    require(cur["lambda_H_value_row_emitted"] is False, "lambda value overemitted")
    require(cur["combined_K_threshold_H_lambda_emitted"] is False, "H K overemitted")
    for phrase in [
        "charged spectral-pairing lemma covers u,d,e only",
        "the charged zero-delta route cannot supply the H/lambda row",
        "the H formula shell and D_fin.H support are not a quartic/threshold payload value",
    ]:
        require(phrase in lambda_normal["why_still_open"], f"lambda reason missing {phrase}")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "neutral identity T_scheme route converted into nine selected zero-delta obligations",
        "identity-by-silence rejected as a no-knob proof step",
        "conditional nine charged K_threshold rows preserved if zero-delta theorem is later selected",
        "H/lambda_H normal form isolated from charged threshold-scheme closure",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected NullThresholdDeltaTheorem or explicit Delta_threshold/Delta_mass/Delta_profile rows",
        "selected nontrivial internal T_scheme rows if the neutral theorem fails",
        "selected lambda_H H-sector quartic/threshold payload",
        "ten selected K_threshold rows",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "charged zero-delta rows required for identity: `9`",
        "selected zero-delta rows emitted: `0`",
        "selected zero-delta theorem emitted: `false`",
        "identity `T_scheme` selected: `false`",
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
