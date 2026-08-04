"""Audit CONST-EW-02 B18 source lift / selected values proof attempt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b18_source_lift_or_selected_values"
DATA = ROOT / "candidate_data"
BASE = DATA / SLUG
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    lift = load(BASE / "ende_bn_source_lift_attempt.packet.json")
    stability = load(BASE / "stability_hym_residual_attempt.packet.json")
    params = load(BASE / "free_parameter_tightening.packet.json")
    external = load(BASE / "external_inspiration_guardrail.packet.json")
    boundary = load(BASE / "weak_mixing_b18_boundary.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("lift", lift),
        ("stability", stability),
        ("params", params),
        ("external", external),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B18 theorem did not prove")
    require(candidate["strict_xL_emitted_now"] is False, "xL incorrectly emitted")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclaimed")
    require(candidate["free_parameter_frontier_tightened"] is True, "frontier not tightened")
    require(cert["free_parameter_frontier_tightened"] is True, "certificate missing tightened frontier")

    require(lift["closed_or_constructed"]["finite_internal_packet_remains_closed"] is True, "finite internal packet not preserved")
    require(lift["closed_or_constructed"]["label_embedding_candidate_built"] is True, "label embedding not built")
    require(lift["closed_or_constructed"]["rhoE_character_intertwines"] is True, "rhoE character does not intertwine")
    require(lift["closed_or_constructed"]["source_certificate_leaves_closed"] is True, "source certificate leaves not closed")
    require(lift["failed_closure_tests"]["D_E_or_EQa_intertwines"] is False, "DE/EQa intertwinement overclosed")
    require(lift["failed_closure_tests"]["finitepart_regularization_same_scheme"] is False, "finite part same-scheme overclosed")
    require(lift["failed_closure_tests"]["same_source_identity_proved"] is False, "same-source identity overclosed")

    require(stability["what_closes"]["selected_AH_goodcover_stability_layer_proved"] is True, "AH/goodcover layer not closed")
    require(stability["what_closes"]["formal_lift_shortcut_rejected"] is True, "formal lift shortcut not rejected")
    require(stability["still_open"]["terminal_principle_unconditional"] is False, "terminal principle wrongly unconditional")
    require(stability["still_open"]["lambda_12_closed"] is False, "lambda_12 overclosed")

    require(params["strict_no_knob_state"] == "OPEN", "strict no-knob state overclosed")
    require(params["one_universal_parameter_lane"]["available"] is True, "one-universal lane missing")
    require(params["one_universal_parameter_lane"]["not_no_knob"] is True, "one-universal lane mislabeled")
    require("arbitrary covariance denominator: q64=15 branch gives G11=dQ=1" in params["removed_false_free_parameters"], "covariance removed knob missing")
    require("selected finite End(E) domain basis" in params["tightened_source_leaves"], "EndE basis leaf missing")

    require(external["guardrail"] == "External theory can justify route shape, not source-selected MTT values.", "external guardrail wrong")
    require(len(external["external_references"]) >= 3, "external references missing")

    require(boundary["closed_now"]["free_parameter_frontier_tightened"] is True, "boundary frontier not tightened")
    require(boundary["still_open"]["finite_EndE_domain_basis_or_nonidentity_rhoE"] is True, "EndE/rhoE leaf not left open")
    require(boundary["still_open"]["D_E_or_EQa_intertwines"] is True, "DE/EQa not left open")
    require(boundary["still_open"]["actual_xL_source_emission"] is True, "xL not left open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle not left open")

    print("CONST-EW-02 B18 source lift / selected values audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
