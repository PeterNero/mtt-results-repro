from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraluniversale0attenuationcandidate_or_sourcelawfrontier"
STATUS = "MTT_SELECTED_NEUTRAL_SHARED_E0_ATTENUATION_CANDIDATE_NUMERICALLY_COMPATIBLE_SOURCE_LAW_OPEN"
NEXT = "MTT_Selected_NeutralElevenFoldAttenuationAndProperTimeNormalizationTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_universal_e0_attenuation_discrimination.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralUniversalE0AttenuationCandidate_or_SourceLawFrontier_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "discrimination theorem failed")
    require(cert["dimension_11_unique_in_scan"] is True, "11D candidate not unique in scan")
    require(abs(cert["A_nu_relative_residual"]) < 2e-5, "neutral amplitude compatibility changed")
    require(cert["universal_metrology_primitive_count"] == 1, "metrology count changed")
    require(cert["new_neutrino_specific_continuous_parameter_count"] == 0, "neutrino knob added")
    require(cert["strict_neutral_scale_source_closed"] is False, "candidate overpromoted")
    boundary = packet["source_law_boundary"]
    for key in [
        "elevenfold_attenuation_derived_from_selected_operator",
        "quarter_proper_time_normalization_derived",
        "one_plus_ratio_normalization_derived_from_selected_action",
        "physical_APS_phase_identification_closed",
        "strict_neutral_scale_source_closed",
    ]:
        require(boundary[key] is False, f"open source clause overclosed: {key}")
    require(boundary["target_used_to_rank_formula"] is True, "target-ranked discovery hidden")
    require(boundary["native_MTT_dimension"] == 10, "native MTT dimension changed")
    require(boundary["M_theory_lift_dimension"] == 11, "M-theory lift dimension changed")
    require(boundary["neutral_operator_proved_to_live_on_11D_lift"] is False, "11D neutral lift overclosed")
    require(all(not row["admissible"] for row in packet["rejected_nearby_coefficients"].values()), "mistyped coefficient promoted")
    for phrase in ["about 18 ppm", "Native MTT is `Y^4 x X^6`, hence 10D", "lift identification is currently open", "Three nearby decimals are rejected", "not a pre-registered prediction", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("neutral universal-E0 attenuation candidate audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
