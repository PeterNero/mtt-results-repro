"""Audit selected threshold response functional derivation / likelihood acquisition gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FUNCTIONAL_CONTRACT = PACKET_DIR / "selected_threshold_response_functional_contract.packet.json"
INSTANTIATION_AUDIT = PACKET_DIR / "current_repo_functional_instantiation_audit.packet.json"
LIKELIHOOD_GATE = PACKET_DIR / "profile_likelihood_acquisition_gate.packet.json"
DECISION = PACKET_DIR / "threshold_response_functional_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_response_functional_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThresholdResponseFunctionalDerivation_or_ProfileLikelihoodAcquisition_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_THRESHOLDRESPONSEFUNCTIONALDERIVATION_OR_PROFILELIKELIHOODACQUISITION_"
    "BUILT_CONTRACT_INSTANTIATION_OPEN"
)
NEXT = "MTT_Selected_ResponseFunctionalInstantiation_or_ExternalWorkspaceIngest_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    contract = load(FUNCTIONAL_CONTRACT)
    instantiation = load(INSTANTIATION_AUDIT)
    likelihood = load(LIKELIHOOD_GATE)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(
        contract["status"] == "SELECTED_THRESHOLD_RESPONSE_FUNCTIONAL_CONTRACT_EMITTED",
        "functional contract status mismatch",
    )
    require(contract["functional_symbol"] == "R_theta", "functional symbol mismatch")
    require(len(contract["domain_required"]) >= 5, "domain contract too small")
    require(len(contract["codomain_required"]) >= 5, "codomain contract too small")
    require("threshold_matching" in contract["row_outputs_required"], "threshold row contract missing")
    require("mass_scheme_conversion" in contract["row_outputs_required"], "mass-scheme row contract missing")
    require("profile_response" in contract["row_outputs_required"], "profile row contract missing")
    require(
        "Residual tables may validate R_theta outputs but cannot define R_theta."
        in contract["acceptance_equations"],
        "residual/source guard missing",
    )
    require(contract["closure_claimed"] is True, "contract should close")
    require(contract["observed_data_used_as_selector"] is False, "contract selector guard failed")
    require(contract["target_fitting_used"] is False, "contract fitting guard failed")

    require(
        instantiation["status"]
        == "CURRENT_REPO_INSTANTIATION_AUDITED_FUNCTIONAL_NOT_INSTANTIATED",
        "instantiation status mismatch",
    )
    require(instantiation["requirement_count"] == 7, "wrong instantiation requirement count")
    require(instantiation["present_count"] >= 1, "positive support unexpectedly absent")
    require(
        instantiation["accepted_threshold_response_functional_instantiated"] is False,
        "functional overinstantiated",
    )
    for required_blocker in [
        "selected_dynamic_operator_source_owner",
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]:
        require(
            required_blocker in instantiation["blocking_failures"],
            f"missing blocker: {required_blocker}",
        )
    for row in instantiation["requirements"]:
        if not row["present"]:
            require(row["missing_for_acceptance"], f"missing reason absent for {row['id']}")
    require(instantiation["closure_claimed"] is False, "instantiation overclaimed")

    require(
        likelihood["status"] == "PROFILE_LIKELIHOOD_ACQUISITION_GATE_BUILT_FULL_WORKSPACE_ABSENT",
        "likelihood gate status mismatch",
    )
    require(likelihood["full_profile_likelihood_imported_now"] is False, "likelihood overimported")
    require(likelihood["accepted_as_external_escape_hatch"] is False, "external route overaccepted")
    require(likelihood["partial_rows_present"]["higgs_decay_covariance_candidate"]["present"] is True, "partial Higgs support missing")
    require(likelihood["reason_not_accepted"], "likelihood rejection reasons missing")
    require(likelihood["closure_claimed"] is False, "likelihood gate overclaimed")

    require(
        decision["status"] == "FUNCTIONAL_CONTRACT_CLOSED_INSTANTIATION_AND_LIKELIHOOD_OPEN",
        "decision status mismatch",
    )
    require(decision["functional_contract_closed"] is True, "functional contract not closed")
    require(decision["current_repo_instantiation_audited"] is True, "instantiation audit not closed")
    for key in [
        "selected_threshold_response_functional_instantiated",
        "profile_likelihood_workspace_acquired",
        "accepted_vsd02_source_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    for key in [
        "selected_response_functional_contract",
        "current_repo_instantiation_audit",
        "profile_likelihood_acquisition_gate",
        "old_proxy_routes_rejected_again_under_functional_contract",
    ]:
        require(decision["what_closes_now"][key] is True, f"close flag missing: {key}")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(len(cutset["recommended_next"]["internal_route"]) >= 4, "internal next route too small")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["functional_contract_closed"] is True, "candidate final contract not closed")
    for key in [
        "selected_threshold_response_functional_instantiated",
        "external_likelihood_workspace_acquired",
        "accepted_vsd02_source_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("R_theta instantiated              : false" in note, "note missing R_theta guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
