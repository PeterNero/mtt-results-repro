"""Audit the H polar-field promotion / finite-H action derivation packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hpolarfieldpromotion_or_finitehactionderivation"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    candidate = read_json(f"candidate_data/{SLUG}.candidate.json")
    promotion = read_json(f"candidate_data/{SLUG}/partial_polar_field_promotion.packet.json")
    action = read_json(f"candidate_data/{SLUG}/controlled_finite_h_action_derivation.packet.json")
    gap = read_json(f"candidate_data/{SLUG}/strict_gap_after_partial_promotion.packet.json")
    cert = read_json(f"certificates/{SLUG}_certificate.json")

    require(candidate["theorem"]["proved"] is True, "theorem must be proved")
    require(candidate["decision"]["m0_tracefree_quotient_promoted"] is True, "m0 trace-free quotient not promoted")
    require(candidate["decision"]["sigma_D_orientation_promoted"] is True, "sigma orientation not promoted")
    require(candidate["decision"]["controlled_finite_H_action_emitted"] is True, "controlled action not emitted")
    require(candidate["decision"]["strict_selected_finite_H_action_emitted"] is False, "strict action must remain open")
    require(candidate["decision"]["strict_r_H_promoted"] is False, "r_H must not be promoted")
    require(candidate["decision"]["strict_phi_Omega_promoted"] is False, "phi must not be promoted")
    require(candidate["key_numbers"]["remaining_strict_promotion_count"] == 2, "remaining strict promotion count mismatch")

    require(promotion["promoted_now"]["m0_tracefree_quotient"]["promoted"] is True, "m0 packet mismatch")
    require(promotion["promoted_now"]["sigma_D_orientation"]["value"] == 1, "sigma value mismatch")
    require(promotion["not_promoted_now"]["phi_Omega"]["phase_certificate_emitted"] is False, "phase must remain open")
    require(promotion["not_promoted_now"]["r_H"]["strict_radial_certificate_emitted"] is False, "radial must remain open")
    require(promotion["counts"]["promoted_polar_certificates"] == 2, "promoted certificate count mismatch")

    second = action["second_variation"]
    require(second["d2F_dconjz_dz_equals_H_controlled"] is True, "controlled action second variation mismatch")
    require(second["Hermitian"] is True, "controlled action not Hermitian")
    require(second["tracefree"] is True, "controlled action not trace-free")
    require(second["non_scalar"] is True, "controlled action not non-scalar")
    require(second["s_beta_recovered"] is True, "controlled action does not recover s_beta")
    require(action["tier"]["strict_selected_finite_H_action_emitted"] is False, "strict action tier mismatch")

    require(gap["status"] == "STRICT_GAP_REDUCED_TO_RADIAL_SOURCE_AND_PHASE_CERTIFICATE", "gap status mismatch")
    require(set(gap["still_open"]) == {"strict_r_H", "strict_phi_Omega", "row_certificates"}, "gap keys mismatch")
    require(cert["checks"]["remaining_strict_promotion_count"] == 2, "cert gap count mismatch")

    print("selected_hpolarfieldpromotion_or_finitehactionderivation audit: PASS")


if __name__ == "__main__":
    main()
