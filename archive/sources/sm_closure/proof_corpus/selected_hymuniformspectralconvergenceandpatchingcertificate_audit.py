from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_hymuniformspectralconvergenceandpatchingcertificate_certificate.json"
PACKET = ROOT / "candidate_data" / "selected_hymuniformspectralconvergenceandpatchingcertificate" / "nested_spectral_and_patching.packet.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))

    require(cert["cutoffs_checked"] == [12, 16, 20, 24, 28], "cutoff sequence changed")
    differences = cert["successive_difference_l2"]
    require(len(differences) == 4, "successive-difference count changed")
    require(all(right < left for left, right in zip(differences, differences[1:])), "nested differences are not decreasing")
    require(differences[-1] < 2.1e-14, "cutoff 24-to-28 difference regressed")
    require(cert["maximum_observed_successive_ratio"] < 0.007, "observed spectral ratio regressed")
    require(cert["dealiased_residual_l2_at_mesh36"] < 1.2e-10, "dealiased residual regressed")
    require(cert["coercivity_lower_bound_at_mesh36"] > 25.8, "coercivity margin regressed")
    require(cert["residual_over_coercivity_at_mesh36"] < 4.5e-12, "a-posteriori indicator regressed")

    patching = packet["patching"]
    require(patching["global_extension_form_eta00"] is True, "global eta source missing")
    require(patching["positive_determinant_one_metric_H"] is True, "global metric missing")
    require(patching["patching_theorem_closed"] is True, "Chern patching theorem not closed")
    require(packet["U2_global_HYM_patching_closed"] is True, "U2 patching not promoted")
    require(packet["U2_continuum_HYM_closed"] is False, "finite data overpromoted to continuum")
    require(packet["validated_numerics_contract"]["radii_polynomial_or_interval_tail_executed"] is False, "unexecuted interval tail claimed")
    require(cert["remaining_scalar_bound_count"] == 1, "remaining HYM bound count changed")
    require(cert["next_required_artifact"] == "MTT_Selected_HYMValidatedFourierResidualTailBound_v1", "next HYM artifact changed")

    print(
        json.dumps(
            {
                "cutoffs": cert["cutoffs_checked"],
                "last_nested_difference_l2": differences[-1],
                "dealiased_residual_l2": cert["dealiased_residual_l2_at_mesh36"],
                "coercivity_lower_bound": cert["coercivity_lower_bound_at_mesh36"],
                "patching_closed": cert["global_HYM_patching_closed"],
                "continuum_tail_bound_open": not cert["continuum_HYM_closed"],
            },
            indent=2,
        )
    )
    print("selected HYM uniform spectral convergence and patching audit passed")


if __name__ == "__main__":
    main()
