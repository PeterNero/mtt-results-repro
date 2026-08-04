from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraldeterminantlineapsoperator_and_native10dmassscale"
STATUS = (
    "MTT_NEUTRAL_DEDEKIND_ARITHMETIC_RETAINED_LENS15_16_SOURCE_ROUTE_REJECTED_"
    "NATIVE10D_NUMERIC_SOURCE_OPEN_OPERATOR_CONTRACT_SHARPENED"
)
NEXT = "MTT_Selected_NeutralDiracFamilyAndDeterminantHolonomy_On_S1xL31xNil3_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralDeterminantLineAPSOperator_and_Native10DMassScale_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    topology = outputs["topology_typing"]
    arithmetic = outputs["arithmetic_audit"]
    monodromy = outputs["monodromy_ambiguity"]
    operator = outputs["operator_contract"]
    action = outputs["native_10D_audit"]
    frontier = outputs["U5_frontier"]

    require(candidate["status"] == cert["status"] == STATUS, "A91 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A91 next changed")
    require(all(candidate["checks"].values()), "one or more A91 checks failed")
    require(topology["selected_internal_topology"]["symbolic"] == "S1_cen x L(3,1) x (Gamma\\Nil3)", "selected topology changed")
    require(topology["retarded_arithmetic_labels"]["selected_as_lens_parameters"] is False, "15/16 overpromoted")
    require(arithmetic["exact_values"]["A41_mixed_remainder"]["text"] == "1/240", "A41 arithmetic lost")
    require(arithmetic["universal_identity"]["selects_a_physical_operator"] is False, "reciprocity overpromoted")
    require(arithmetic["exact_values"]["s_1_3_for_selected_L31"]["text"] == "1/18", "L31 sum changed")
    require(arithmetic["exact_values"]["ordinary_signature_eta_L31_standard_orientation"]["text"] == "-2/9", "L31 eta changed")
    require(monodromy["selection_result"]["integer_ambiguity_count"] == "infinite", "monodromy ambiguity lost")
    require(monodromy["selection_result"]["pi_over_120_phase_derived"] is False, "phase overclosed")
    require(all(row["determinant"] == 1 and row["equals_15_plus_t"] for row in monodromy["general_family"]["sample_rows"]), "SL2Z samples failed")
    require(operator["readiness"] == {"filled": 2, "required": 10, "strict_phase_value_emitted": False, "observed_oscillation_data_allowed_as_selector": False}, "operator contract count changed")
    require(all(action["source_markers"].values()), "10D source marker missing")
    require(action["source_theorem"]["native_action_selects_absolute_neutral_scale"] is False, "10D scale overclosed")
    require(frontier["corrected_status"]["minimal_PMNS_profile_coordinate_count_remains"] == 6, "PMNS count changed")
    require(frontier["new_continuous_parameters_added"] == 0, "A91 added a parameter")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A91 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A91 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["universal reciprocity remainder", "infinite", "2/10", "minimal PMNS profile count remains six", NEXT]:
        require(phrase in note, f"A91 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("neutral determinant-line and native-10D source audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
