"""Audit static lambda-orbit quotient / dynamic orientation frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_staticlambdaorbitquotient_or_dynamicorientationfrontier"
DATA = ROOT / "candidate_data"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
ORBIT = PACKET_DIR / "selected_static_lambda_orbit.packet.json"
NO_SELECTOR = PACKET_DIR / "static_representative_no_selector.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_static_lambda_orbit.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StaticLambdaOrbitQuotient_or_DynamicOrientationFrontier_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_staticlambdaorbitquotient_or_dynamicorientationfrontier.py"

STATUS = "MTT_SELECTED_STATIC_LAMBDA_ORBIT_QUOTIENT_BUILT_REPRESENTATIVE_SELECTION_OPEN"
NEXT = "MTT_Selected_DynamicOrientation_or_PhysicalMatrixPromotion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")
    require(payload["closure_claimed"] is False, f"{label}: closure overclaimed")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    orbit = load(ORBIT)
    no_selector = load(NO_SELECTOR)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for label, payload in [
        ("candidate", candidate),
        ("orbit", orbit),
        ("no_selector", no_selector),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    require(
        orbit["status"] == "STATIC_SOURCE_SELECTS_TWO_ELEMENT_LAMBDA_ORBIT_NOT_REPRESENTATIVE",
        "orbit status mismatch",
    )
    require(orbit["selected_static_lambda_orbit"] == ["1+omega", "1+omega2"], "lambda orbit mismatch")
    require(len(orbit["survivor_branch_ids"]) == 2, "survivor count mismatch")
    require(
        orbit["survivor_branch_ids"]
        == [
            "phase_lambda_1+omega__shift_lambda_1+omega",
            "phase_lambda_1+omega2__shift_lambda_1+omega2",
        ],
        "survivor ids mismatch",
    )
    require(
        orbit["static_invariant_signature_identical_across_survivors"] is True,
        "static signature not identical",
    )
    require(
        orbit["matrix_formulas_identical_across_survivors"] is False,
        "matrix formulas unexpectedly identical",
    )
    require(
        orbit["static_invariant_signature"]["cp_odd_orientation"] == "positive",
        "static CP signature mismatch",
    )
    require(
        orbit["static_invariant_signature"]["cp_odd_exact_magnitude"] == "972*sqrt(3)",
        "static CP magnitude mismatch",
    )

    checks = no_selector["checks"]
    require(
        no_selector["status"] == "NO_STATIC_REPRESENTATIVE_SELECTOR_EMITTED",
        "no-selector status mismatch",
    )
    require(checks["selected_static_transfer_rule_emitted"] is True, "static transfer missing")
    require(checks["selected_specific_lambda_value_emitted"] is False, "lambda value overemitted")
    require(
        checks["selected_complex_orientation_or_universe_branch_rule_emitted"] is False,
        "orientation selector overemitted",
    )
    require(checks["selected_physical_CKM_or_PMNS_CP_orientation_emitted"] is False, "physical CP overemitted")
    require(checks["selected_physical_matrices_promoted"] is False, "physical matrices overpromoted")
    require(no_selector["physical_coexistence_claimed"] is False, "physical coexistence overclaimed")
    require(no_selector["individual_universe_branch_selected"] is False, "individual branch overselected")

    closed = candidate["what_closes_now"]
    require(closed["selected_static_lambda_orbit_quotient"] is True, "static orbit not closed")
    require(
        closed["representative_selection_not_required_at_static_tier"] is True,
        "representative-selection static decision missing",
    )
    require(
        closed["static_invariant_signature_exhausted_for_survivors"] is True,
        "static signature exhaustion missing",
    )

    remaining = candidate["what_remains_open"]
    for key in [
        "individual_lambda_representative_selection",
        "physical_coexistence_or_equivalence_of_representatives",
        "selected_dynamic_orientation_or_time_arrow_rule",
        "selected_dynamic_C1_or_Aselected_matrix_promotion",
        "physical_CKM_PMNS_Yukawa_value_closure",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remaining[key] is True, f"remaining gate overclosed: {key}")

    decision = candidate["closure_decision"]
    require(decision["static_lambda_orbit_selected"] is True, "static orbit decision missing")
    require(decision["individual_lambda_value_selected"] is False, "individual lambda overselected")
    require(decision["physical_coexistence_claimed"] is False, "coexistence overclaimed")
    require(decision["selected_physical_matrices_promoted"] is False, "physical matrices overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("static signature identical : true" in note, "note missing static signature")
    require("individual lambda selected : false" in note, "note missing lambda guard")
    require("physical coexistence claimed : false" in note, "note missing coexistence guard")
    require("full SM closure : false" in note, "note missing closure guard")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
