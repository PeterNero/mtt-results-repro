from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_globalhymchernsequence_aposterioricertificate"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(f"candidate_data/{SLUG}/global_hym_chern_sequence_aposteriori.packet.json")
    cert = load(f"certificates/{SLUG}_certificate.json")
    finite = packet["finite_aposteriori_certificate"]

    require(packet["global_Chern_connection_sequence"]["offdiagonal_component_is_free_parameter"] is False, "offdiagonal free")
    require(packet["global_Chern_connection_sequence"]["offdiagonal_component_source"].startswith("selected eta_00"), "offdiagonal source")
    require(math.isclose(finite["zero_mean_Poincare_lambda1"], 4 * math.pi**2), "Poincare")
    require(finite["linearized_coercivity_lower_bound"] > 26.0, "coercivity")
    require(finite["HYM_residual_L2"] < 1e-12, "residual")
    require(finite["residual_over_coercivity_error_indicator"] < 4e-14, "error indicator")
    require(finite["finite_projected_solution_locally_unique_and_stable"] is True, "finite stability")
    require(packet["decision"]["continuum_uniform_truncation_bound_closed"] is False, "continuum overclaim")
    require(packet["decision"]["literal_global_HYM_witness_closed"] is False, "global HYM overclaim")
    require(all(value is False for value in packet["guards"].values()), "guard")
    require(cert["finite_projected_HYM_aposteriori_stability_closed"] is True, "certificate finite")

    print(json.dumps({
        "global_Chern_sequence_typed": True,
        "HYM_residual_L2": finite["HYM_residual_L2"],
        "coercivity_lower_bound": finite["linearized_coercivity_lower_bound"],
        "error_indicator": finite["residual_over_coercivity_error_indicator"],
        "finite_projected_HYM_stable": True,
        "continuum_literal_global_HYM": False,
    }, indent=2))
    print("global HYM Chern-sequence a-posteriori audit passed")


if __name__ == "__main__":
    main()
