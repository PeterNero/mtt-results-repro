"""Audit Yukawa magnitude/RG closure attempt or final true-SM equivalence audit."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
VALUE_LEDGER = PACKET_DIR / "accepted_value_layer_ledger.packet.json"
RG_CLOSURE_ATTEMPT = PACKET_DIR / "yukawa_rg_closure_attempt.packet.json"
FINAL_AUDIT = PACKET_DIR / "final_true_sm_equivalence_audit.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_final_value_audit.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_YukawaMagnitudeRGClosure_or_FinalTrueSMEquivalenceAudit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_YUKAWAMAGNITUDERGCLOSURE_OR_FINALTRUESMEQUIVALENCEAUDIT_"
    "BUILT_FINAL_VALUE_AUDIT_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_AcceptedCommonScaleYukawaHiggsValues_or_ProfileLikelihoodExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    ledger = load(VALUE_LEDGER)
    rg_attempt = load(RG_CLOSURE_ATTEMPT)
    final_audit = load(FINAL_AUDIT)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    closed = ledger["closed_layers"]
    require(closed["SM_parity_closed"] is True, "SM parity not closed")
    require(closed["dynamic_QaSU3_first_response_layer"] is True, "dynamic Qa/SU3 first response missing")
    require(closed["common_scale_gauge_values_at_MZ"] is True, "gauge common-scale layer missing")
    require(closed["diagnostic_RG_smoke_run"] is True, "diagnostic RG missing")
    require(ledger["closure_claimed"] is False, "ledger overclaims closure")

    open_values = ledger["open_accepted_value_layers"]
    for key in [
        "common_scale_yukawa_higgs_values",
        "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values",
        "accepted_lambda_H_MZ_value",
        "threshold_matching_values",
        "mass_scheme_conversion_values",
        "full_correlated_covariance_profile",
        "local_QFT_precision_values",
    ]:
        require(open_values[key] is True, f"open value layer missing: {key}")

    decision = rg_attempt["attempted_closure"]
    for key, value in decision.items():
        require(value is False, f"RG attempt overclosed {key}")
    final_decision = final_audit["closure_decision"]
    for key in [
        "accepted_Yukawa_magnitudes_closed",
        "running_mass_ratios_closed",
        "CKM_PMNS_measured_value_closure",
        "true_SM_equivalence_closed",
        "full_SM_no_knob_closed",
    ]:
        require(final_decision[key] is False, f"final audit overclosed {key}")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("does not close measured Yukawa magnitudes" in " ".join(note.split()), "note missing value guardrail")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
