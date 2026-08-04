"""Audit CONST-EW-02 B15 electroweak product-map factorization."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b15_ew_product_map_factorization"
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
    paper = load(BASE / "theta_weak_mixing_paper_input_audit.packet.json")
    factor = load(BASE / "source_product_map_factorization.packet.json")
    exits = load(BASE / "operator_or_torsion_exit_matrix.packet.json")
    rejections = load(BASE / "shortcut_rejection.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("paper", paper),
        ("factor", factor),
        ("exits", exits),
        ("rejections", rejections),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B15 theorem did not prove")
    require(candidate["strict_xL_emitted_now"] is False, "xL incorrectly emitted")
    require(candidate["strict_no_knob_payload_required"] is True, "strict payload requirement missing")
    require(candidate["one_universal_primitive_lane_available"] is True, "one-primitive lane missing")
    require(cert["product_map_factorized"] is True, "product map not factorized")
    require(cert["threshold_payload_required"] is True, "threshold payload not required")
    require(cert["strict_xL_emitted_now"] is False, "certificate overclaims xL")

    require(paper["strict_no_knob_closure_from_paper"] is False, "paper promoted as strict closure")
    require(any("mu_Theta=5 TeV" in item for item in paper["paper_level_inputs_that_are_not_strict_source_outputs"]), "missing 5 TeV audit")
    require(any("g2 extracted" in item for item in paper["paper_level_inputs_that_are_not_strict_source_outputs"]), "missing g2 input audit")

    source_verified = factor["source_verified_inputs"]
    require(source_verified["selected_H2_scale_law"] is True, "H2 not source verified")
    require(source_verified["selected_G_11"] == 1.0, "G11 not imported")
    require(source_verified["selected_d_Q"] == 1.0, "d_Q not imported")
    require(source_verified["selected_Qa_finite_response_chi_Qa"] == 1, "chi_Qa not imported")
    require(factor["emits_xL"] is False, "factorization emitted xL")
    require("paper-level 5 TeV RG replay" in factor["not_enough_by_itself"], "paper replay not guarded")
    require(any("Phi_EW" in item for item in factor["allowed_strict_forms"]), "Phi_EW strict form missing")

    require(exits["primary_exit"]["name"] == "C_hym_monad_threshold_operator", "wrong primary exit")
    require(exits["parallel_exit"]["name"] == "B_ray_singer_or_reidemeister_local_system", "wrong parallel exit")
    require(exits["one_primitive_lane"]["status"] == "AVAILABLE_BUT_NOT_STRICT_NO_KNOB", "one-primitive lane mislabeled")
    require(any("P_perp" in item for item in exits["primary_exit"]["must_emit"]), "P_perp missing from primary payload")

    shortcuts = [row["shortcut"] for row in rejections["rejected_shortcuts"]]
    require("xL = f(R_star) chosen by closeness" in shortcuts, "R_star shortcut not rejected")
    require("xL = f(rho_UV) without threshold payload" in shortcuts, "rho shortcut not rejected")
    require("use Theta V 5 TeV result as no-knob closure" in shortcuts, "Theta V shortcut not rejected")

    print("CONST-EW-02 B15 product-map factorization audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
