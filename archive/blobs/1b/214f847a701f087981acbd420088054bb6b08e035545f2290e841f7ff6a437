from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure"
STATUS = "MTT_FINITE_ONEFORM_EXECUTED_RAW_THREE_DOUBLET_SPACE_SELECTED_SINGLE_HIGGS_PROJECTION_AND_TRACE_COEFFICIENTS_CLOSED_SPECTRAL_MOMENTS_OPEN"
NEXT = "MTT_Selected_SpectralCutoffMomentsAndSpacetimeProductTriple_or_BosonicActionNormalization_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "finite_inner_fluctuation_and_spectral_traces.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_FiniteSpectralActionAndHiggsInnerFluctuation_or_DirectGenerativeSMActionClosure_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(cert["unrestricted_inner_fluctuation_real_rank"] == 12, "raw fluctuation rank changed")
    require(cert["unrestricted_scalar_doublet_count"] == 3, "raw doublet count changed")
    require(cert["raw_one_Higgs_SM_closed"] is False, "raw triple overclaimed")
    require(cert["selected_single_Higgs_projection_closed"] is True, "single-Higgs projection open")
    require(cert["selected_single_Higgs_real_rank"] == 4, "selected Higgs rank changed")
    require(cert["removed_extra_scalar_real_dimensions"] == 8, "extra scalar removal changed")
    require(cert["finite_gauge_trace_relation_closed"] is True, "gauge traces open")
    require(cert["finite_Yukawa_trace_invariants_closed_at_profile_tier"] is True, "Yukawa traces open")
    require(cert["bosonic_SM_operator_content_closed_via_standard_heat_kernel_theorem"] is True, "bosonic operator content open")
    require(cert["absolute_spectral_action_normalization_closed"] is False, "spectral moments overclaimed")
    require(cert["new_continuous_knobs"] == 0, "new continuous knob introduced")
    require(packet["single_Higgs_projection"]["oneform_containment_residual"] < 1e-10, "single-Higgs image outside one-forms")
    require(packet["single_Higgs_projection"]["projector_idempotence_residual"] < 1e-12, "projector not idempotent")
    require(packet["finite_spectral_traces"]["GUT_normalized_coefficients_three_families"] == {"SU2": 6, "SU3": 6, "U1_GUT": 6.0}, "gauge trace ratio changed")
    for phrase in ["rank `12`, not `4`", "three-Higgs-doublet", "rank `4`", "dimension `8`", "10:6:6", "Absolute spectral-action normalization is not closed", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("finite spectral action and Higgs inner-fluctuation audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
