from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "candidate_data" / "selected_hymvalidatedfourierresidualtailbound" / "wiener_contraction.packet.json"
CERT = ROOT / "certificates" / "selected_hymvalidatedfourierresidualtailbound_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def close(left: float, right: float, tolerance: float = 1e-13) -> bool:
    return abs(left - right) <= tolerance * max(1.0, abs(left), abs(right))


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    density = packet["exact_density_formula"]
    center = packet["finite_center"]
    residual = packet["residual_bound"]
    contraction = packet["contraction"]

    require(density["rho_truncated_coefficient_count"] == 6175, "rho truncation size changed")
    require(density["rho_tail_bound"] < 1.1e-10, "theta-density tail regressed")
    require(density["retained_coefficient_roundoff_allowance"] == 1e-10, "rho coefficient guard changed")
    require(center["source_cutoff"] == 28, "center cutoff changed")
    require(center["retained_coefficient_count"] == 336, "center sparsity changed")
    require(center["wiener_norm"] < 0.095, "center Wiener norm regressed")
    require(residual["conservative_IEEE_roundoff_envelope"] == 1e-6, "roundoff guard changed")
    require(residual["full_continuous_residual_upper"] < 0.217, "continuous residual bound regressed")

    lambda1 = 4.0 * math.pi**2
    expected_y = residual["full_continuous_residual_upper"] / lambda1
    expected_z = (
        2.0
        * density["rho_full_wiener_norm_upper"]
        * math.exp(2.0 * (center["wiener_norm"] + contraction["radius"]))
        / lambda1
    )
    expected_lhs = expected_y + expected_z * contraction["radius"]
    require(close(contraction["lambda1"], lambda1), "lambda1 changed")
    require(close(contraction["Y"], expected_y), "Y arithmetic changed")
    require(close(contraction["Z_at_radius"], expected_z), "Z arithmetic changed")
    require(close(contraction["Y_plus_Zr"], expected_lhs), "radii inequality arithmetic changed")
    require(contraction["Z_at_radius"] < 0.386 < 1.0, "contraction constant regressed")
    require(contraction["Y_plus_Zr"] < contraction["radius"], "ball does not map into itself")
    require(contraction["strict_margin"] > 6e-4, "contraction margin too small")
    require(contraction["passes"] is True, "contraction theorem not promoted")

    require(packet["patching_import"]["global_HYM_patching_closed"] is True, "patching import missing")
    require(packet["theorem"]["proved"] is True, "continuum theorem not proved")
    require(packet["U2_literal_global_HYM_closed"] is True, "literal global HYM not closed")
    require(packet["U2_literal_witness_families"] == "2/2", "U2 witness count changed")
    require(cert["continuum_HYM_existence_closed"] is True, "certificate existence missing")
    require(cert["continuum_HYM_local_uniqueness_closed"] is True, "certificate uniqueness missing")
    require(cert["U2_literal_witness_families_closed"] == cert["U2_literal_witness_families_required"] == 2, "certificate witness count changed")
    require(all(value is False for value in packet["scope_guards"].values()), "scope guard violated")

    print(
        json.dumps(
            {
                "rho_Wiener_upper": density["rho_full_wiener_norm_upper"],
                "continuous_residual_upper": residual["full_continuous_residual_upper"],
                "radius": contraction["radius"],
                "Z": contraction["Z_at_radius"],
                "Y_plus_Zr": contraction["Y_plus_Zr"],
                "strict_margin": contraction["strict_margin"],
                "U2_literal_witness_families": packet["U2_literal_witness_families"],
            },
            indent=2,
        )
    )
    print("selected HYM validated Fourier residual-tail audit passed")


if __name__ == "__main__":
    main()
