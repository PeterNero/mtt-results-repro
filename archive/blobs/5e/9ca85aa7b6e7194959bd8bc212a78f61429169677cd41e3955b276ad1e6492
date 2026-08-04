"""Audit PSM-C1-02 source-chain backimport into internal Rtheta scalar rows."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_internalrtheta_scalarrows_psmc102_backimport_or_unpatchedsourceidentitygate"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BACKIMPORT = PACKET_DIR / "psm_c1_02_source_chain_backimport.packet.json"
SCALAR_GATE = PACKET_DIR / "internal_scalar_row_gate_after_psm_c1_02_backimport.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_psm_c1_02_backimport.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_InternalRThetaScalarRows_PSMC102Backimport_or_UnpatchedSourceIdentityGate_v1.md"
)

STATUS = (
    "MTT_SELECTED_INTERNALRTHETA_SCALARROWS_PSMC102_BACKIMPORT_"
    "BUILT_LOCAL_C1_SOURCE_READY_UNPATCHED_SCALARROWS_OPEN"
)
NEXT = "MTT_Selected_PSM_C1_02_UnpatchedWeylVariationActionPrincipleDerivation_or_IndependentRowSourceExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict, errors: list[str], label: str, *, closure: bool = False) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    backimport = load(BACKIMPORT)
    scalar = load(SCALAR_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "theorem should be proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem should be proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(backimport, errors, "backimport", closure=False)
    guard(scalar, errors, "scalar gate", closure=False)
    guard(cutset, errors, "cutset", closure=False)
    guard(cert, errors, "certificate", closure=False)

    expect(backimport.get("dynamic_fields_reduced_to_single_identity") is True, "dynamic fields not reduced", errors)
    expect(backimport.get("local_source_promotion_closed") is True, "local source promotion not imported", errors)
    expect(backimport.get("unpatched_source_promotion_closed") is False, "unpatched source overclosed", errors)
    expect(backimport.get("current_unpatched_source_packet_passes") is False, "current unpatched packet unexpectedly passes", errors)
    expect(backimport.get("conditional_unpatched_source_packet_passes") is True, "conditional packet should pass", errors)
    expect(backimport.get("patched_packet_rejected_for_unpatched_proof") is True, "patched packet guard missing", errors)
    expect(len(backimport.get("must_add_one_of", [])) == 2, "unpatched two-route gate missing", errors)

    expect(scalar.get("codomain_scalar_row_count") == 10, "scalar codomain count mismatch", errors)
    expect(scalar.get("accepted_internal_scalar_row_count") == 0, "scalar rows overaccepted", errors)
    expect(scalar.get("accepted_internal_scalar_rows") == [], "accepted scalar rows should be empty", errors)
    expect(scalar.get("lambda_H_row_emitted") is False, "lambda_H overemitted", errors)
    expect(scalar.get("local_principle_c1_source_promotion_ready") is True, "local C1 readiness missing", errors)
    expect(scalar.get("local_principle_scalar_rows_accepted_as_no_knob") is False, "local rows overaccepted", errors)
    expect(scalar.get("unpatched_source_identity_closed") is False, "unpatched identity overclosed", errors)
    expect(scalar.get("direct_internal_rtheta_scalar_rows_ready") is False, "direct scalar rows overclosed", errors)
    readiness = scalar.get("updated_readiness", {})
    expect(readiness.get("dynamic_source_fields_reduced_to_single_identity") is True, "readiness reduction missing", errors)
    expect(readiness.get("local_principle_finite_C1_source_packet") is True, "readiness local packet missing", errors)
    expect(readiness.get("unpatched_finite_C1_source_identity") is False, "readiness unpatched overclosed", errors)
    expect(readiness.get("internal_Rtheta_scalar_rows") is False, "readiness scalar rows overclosed", errors)

    closed = cutset.get("closed_now", {})
    for key in [
        "dynamic_overlap_blocker_sharpened_to_source_identity_gate",
        "four_dynamic_source_fields_reduced_to_single_identity",
        "local_principle_finite_C1_source_promotion_closed",
        "conditional_unpatched_packet_validates",
        "scalar_row_branch_backimported_latest_PSMC102_status",
    ]:
        expect(closed.get(key) is True, f"cutset close missing: {key}", errors)

    remains = cutset.get("still_open", {})
    for key in [
        "unpatched_SelectedFiniteC1SourceIdentityLemma",
        "derive_SelectedWeylVariationActionPrinciple",
        "independent_RouteB_row_source_execution",
        "accepted_internal_Rtheta_scalar_rows",
        "lambda_H_internal_scalar_row",
        "true_SM_equivalence_or_no_knob_closure",
    ]:
        expect(remains.get(key) is True, f"cutset blocker missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("local_principle_finite_C1_source_promotion_closed") is True, "decision local closure missing", errors)
    expect(decision.get("unpatched_source_identity_closed") is False, "decision unpatched overclosed", errors)
    expect(decision.get("accepted_internal_scalar_row_count") == 0, "decision scalar rows overaccepted", errors)
    expect(decision.get("lambda_H_row_emitted") is False, "decision lambda_H overemitted", errors)
    expect(decision.get("direct_internal_rtheta_scalar_rows_closed") is False, "decision scalar closure overclaimed", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "decision true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "decision no-knob overclosed", errors)

    expect("Accepted internal `R_theta` scalar rows: `0`" in note, "note missing zero scalar rows", errors)
    expect("The blocker is now the unpatched source-identity/action-principle gate" in note, "note missing blocker", errors)

    if errors:
        print("PSM-C1-02 backimport scalar-row audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PSM-C1-02 backimport scalar-row audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
