from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import certify_q79_height4_rank3_beta_hessian_interval as beta_hessian
import q79_fast_taylor_runtime as fast
import q79_stable_affine_hessian_runtime as stable


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = beta_hessian.VALIDATED
OUTPUT = VALIDATED / "n3.betaH.full_lower.a390.json"
CHECKPOINT = VALIDATED / "n3.betaH.full_lower.a390.ckpt.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourFullLowerBetaHessian_A390B_v1.md"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
STABLE_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79stableaffinehessianruntime_inclusion_audit.py"
)
WAYPOINTS = [0 + 0j, -0.1j, 1 - 0.1j, 1 + 0j]
ARTIFACT = "A390B"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def main() -> int:
    original = {
        "OUTPUT": beta_hessian.OUTPUT,
        "CHECKPOINT": beta_hessian.CHECKPOINT,
        "NOTE": beta_hessian.NOTE,
        "ARTIFACT": beta_hessian.ARTIFACT,
        "WAYPOINTS": beta_hessian.WAYPOINTS,
        "configuration": beta_hessian.configuration,
    }
    fast_runtime = Path(fast.__file__).resolve()
    stable_runtime = Path(stable.__file__).resolve()

    def route_configuration(arguments) -> dict:
        value = original["configuration"](arguments)
        value.update(
            {
                "route_id": "endpoint_fixed_full_lower_minus_0p1i",
                "route_runner_sha256": sha256(Path(__file__).resolve()),
                "C_backed_Taylor_runtime_sha256": sha256(fast_runtime),
                "C_backed_Taylor_equivalence_audit_sha256": sha256(FAST_AUDIT),
                "stable_affine_Hessian_runtime_sha256": sha256(stable_runtime),
                "stable_affine_Hessian_inclusion_audit_sha256": sha256(STABLE_AUDIT),
            }
        )
        return value

    beta_hessian.OUTPUT = OUTPUT
    beta_hessian.CHECKPOINT = CHECKPOINT
    beta_hessian.NOTE = NOTE
    beta_hessian.ARTIFACT = ARTIFACT
    beta_hessian.WAYPOINTS = WAYPOINTS
    beta_hessian.configuration = route_configuration
    try:
        fast.install()
        stable.install()
        result = beta_hessian.main()
    finally:
        stable.uninstall()
        fast.uninstall()
        for name, value in original.items():
            setattr(beta_hessian, name, value)

    if "--smoke-only" in sys.argv or not OUTPUT.exists():
        return result
    packet = json.loads(OUTPUT.read_text(encoding="utf-8"))
    packet["status"] = "N3_FULL_LOWER_ROUTE_BETA_HESSIAN_INTERVAL_EXECUTED_HOMOTOPY_OPEN"
    packet["route"] = {
        "route_id": "endpoint_fixed_full_lower_minus_0p1i",
        "waypoints": [beta_hessian.pair(value) for value in WAYPOINTS],
        "same_start_and_endpoint_as_A379": True,
        "floating_same_branch_evidence_exists": True,
        "homotopy_to_A379_selected_route_interval_certified": False,
    }
    packet["execution"]["stable_accelerated_runtime"] = {
        "C_backed_Taylor_products": True,
        "growth_integral_majorant": "A*h*exp(L*h)",
        "zero_containing_linear_defect_interval_supported": True,
    }
    packet["authority"].update(
        {
            "C_backed_Taylor_runtime": authority(fast_runtime),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "stable_affine_Hessian_runtime": authority(stable_runtime),
            "stable_affine_Hessian_inclusion_audit": authority(STABLE_AUDIT),
            "full_lower_route_runner": authority(Path(__file__).resolve()),
        }
    )
    packet["strict_scope"].update(
        {
            "endpoint_fixed_full_lower_route_interval_executed": True,
            "C_backed_polynomial_acceleration_equivalence_audited": True,
            "zero_defect_regular_affine_growth_bound_audited": True,
            "all_step_bounds_finite": True,
            "homotopy_to_A379_selected_route_interval_certified": False,
            "full_lower_route_promoted_to_selected_beta_branch": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        }
    )
    packet["next_required_artifact"] = (
        "compare the full-lower radius with A379, then certify a discriminant-free "
        "homotopy to the selected route before using this endpoint in A386"
    )
    OUTPUT.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    NOTE.write_text(
        "# MTT q79 Height-Four Full-Lower Beta Hessian (A390B) v1\n\n"
        "A390B executes the validated beta/Hessian system on the endpoint-fixed "
        "contour `0 -> -0.1i -> 1-0.1i -> 1`. Floating precursor work found "
        "substantially better reduction conditioning on this route.\n\n"
        f"The maximum certified beta-row radius is "
        f"`{packet['summary']['maximum_beta_component_radius_upper']:.12g}` and "
        f"the maximum Hessian-entry radius is "
        f"`{packet['summary']['maximum_Hessian_component_radius_upper']:.12g}`.\n\n"
        "The path has the selected endpoints, but its homotopy to the current A379 "
        "route is not yet interval-certified. This packet is therefore a rigorous "
        "route execution, not yet a selected-branch replacement.\n",
        encoding="utf-8",
    )
    print(f"promoted {relative(OUTPUT)} with full-lower route metadata", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
