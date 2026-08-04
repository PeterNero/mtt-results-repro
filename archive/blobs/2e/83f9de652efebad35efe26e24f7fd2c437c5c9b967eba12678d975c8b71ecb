"""Audit CONST-EW-02 B28 patched C1/minimal source-certificate import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b28_patched_c1_and_minimal_source_certificate"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
PATCHED = BASE / "patched_sm_parity_c1_import.packet.json"
MINIMAL = BASE / "minimal_source_certificate_import.packet.json"
GAUGE = BASE / "gaugekinetic_edge_status.packet.json"
BOUNDARY = BASE / "weak_mixing_b28_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B28_PatchedC1AndMinimalSourceCertificate_v1.md"

STATUS = "MTT_CONST_EW_02_B28_PATCHED_C1_IMPORTED_MINIMAL_SOURCE_CERT_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    patched = load(PATCHED)
    minimal = load(MINIMAL)
    gauge = load(GAUGE)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("patched", patched),
        ("minimal", minimal),
        ("gauge", gauge),
        ("boundary", boundary),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["patched_SM_parity_dynamic_C1_closed"] is True, "patched C1 not imported")
    require(candidate["unpatched_no_knob_dynamic_C1_closed"] is False, "unpatched C1 overclosed")
    require(candidate["minimal_route_A_source_certificate_identified"] is True, "minimal cert not identified")
    require(candidate["route_A_minimal_certificate_filled"] is False, "route A overfilled")
    require(candidate["route_B_run_executed"] is False, "route B overexecuted")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    patched_result = patched["patched_result"]
    require(patched_result["SM_parity_closed"] is True, "SM parity not closed")
    require(patched_result["patched_SM_parity_dynamic_C1_source_and_value_interface_closed"] is True, "patched interface not closed")
    require(patched["unpatched_result"]["unpatched_no_knob_dynamic_C1_closed"] is False, "patched packet overcloses no-knob")
    require("support only" in patched["local_interpretation"], "patched interpretation missing support guardrail")

    three = minimal["three_field_certificate"]
    require(set(three) == {
        "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "no_extra_physical_boundary_or_source_term",
        "same_source_R_Z_R_X_b_selected_emission",
    }, "three-field certificate changed")
    require(all(three.values()), "three-field openness not preserved")
    decision = minimal["decision"]
    require(decision["route_A_minimal_certificate_built"] is True, "route A template missing")
    require(decision["route_A_minimal_certificate_filled"] is False, "route A filled")
    require(decision["route_B_run_spec_built"] is True, "route B spec missing")
    require(decision["route_B_run_executed"] is False, "route B executed")

    local = gauge["local_decision"]
    require(local["K_phys_or_f_ab_closed"] is False, "K closed")
    require(local["mu_match_closed"] is False, "mu closed")
    require(local["RG_threshold_scheme_closed"] is False, "RG closed")
    require(gauge["oriented_phifin_sourceownership_status"]["same_branch_source_certificate_closed"] is True, "branch cert support missing")
    require(gauge["oriented_phifin_sourceownership_status"]["oriented_BN_carrier_emission_closed"] is False, "oriented carrier overclosed")

    advanced = boundary["advanced_now"]
    require(advanced["patched_SM_parity_dynamic_C1_source_value_interface_closed"] is True, "boundary patched missing")
    require(advanced["minimal_three_field_source_certificate_identified"] is True, "boundary minimal missing")
    require(boundary["still_open"]["unpatched_no_knob_dynamic_C1"] is True, "boundary unpatched missing")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "boundary weak-angle missing")
    require(boundary["still_open"]["K_phys_or_f_ab"] is True, "boundary gauge edge missing")

    require(cert["status"] == STATUS, "cert status")
    require(cert["patched_SM_parity_dynamic_C1_closed"] is True, "cert patched")
    require(cert["unpatched_no_knob_dynamic_C1_closed"] is False, "cert no-knob overclosed")
    require(cert["route_A_minimal_certificate_filled"] is False, "cert route A overclosed")
    require(cert["route_B_run_executed"] is False, "cert route B overclosed")
    require(cert["physical_weak_angle_closure"] is False, "cert weak angle")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B29-THREE-FIELD-PHYSICAL-SOURCE-CERTIFICATE-FILL", "next primary")
    require("minimal Route-A certificate built   = True" in note, "note missing minimal route")

    print("CONST-EW-02 B28 patched C1/minimal source-certificate audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
