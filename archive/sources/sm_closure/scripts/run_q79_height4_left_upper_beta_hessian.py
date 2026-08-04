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
OUTPUT = VALIDATED / "n3.betaH.left_upper.a391.json"
CHECKPOINT = VALIDATED / "n3.betaH.left_upper.a391.ckpt.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourLeftUpperBetaHessian_A391_v1.md"
HOMOTOPY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_left_upper_0p05_homotopy.a390h.interval.json"
)
A379 = VALIDATED / "n3.beta_hessian.interval.json"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
STABLE_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79stableaffinehessianruntime_inclusion_audit.py"
)
WAYPOINTS = [
    0 + 0j,
    0 + 0.05j,
    0.65 + 0.05j,
    0.65 - 0.1j,
    0.82 - 0.1j,
    0.82 + 0j,
    1 + 0j,
]
ARTIFACT = "A391"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def require_homotopy() -> dict:
    if not HOMOTOPY.exists():
        raise FileNotFoundError("A390H must finish before A391 can run")
    packet = json.loads(HOMOTOPY.read_text(encoding="utf-8"))
    if (
        packet.get("artifact") != "A390H"
        or packet.get("status") != "LEFT_UPPER_CONTOUR_HOMOTOPY_INTERVAL_CERTIFIED"
        or packet.get("decision", {}).get(
            "A379_to_left_upper_route_homotopy_certified"
        )
        is not True
    ):
        raise AssertionError("A390H does not certify the A391 route")
    return packet


def main() -> int:
    require_homotopy()
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
                "route_id": "A390H_certified_left_upper_0p05",
                "A390H_sha256": sha256(HOMOTOPY),
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
    selected = json.loads(A379.read_text(encoding="utf-8"))
    beta_factor = float(
        selected["summary"]["maximum_beta_component_radius_upper"]
    ) / float(packet["summary"]["maximum_beta_component_radius_upper"])
    hessian_factor = float(
        selected["summary"]["maximum_Hessian_component_radius_upper"]
    ) / float(packet["summary"]["maximum_Hessian_component_radius_upper"])
    packet["status"] = "N3_LEFT_UPPER_SELECTED_ROUTE_BETA_HESSIAN_INTERVAL_EXECUTED"
    packet["route"] = {
        "route_id": "A390H_certified_left_upper_0p05",
        "waypoints": [beta_hessian.pair(value) for value in WAYPOINTS],
        "same_start_and_endpoint_as_A379": True,
        "homotopy_to_A379_selected_route_interval_certified": True,
        "homotopy_certificate": relative(HOMOTOPY),
        "homotopy_certificate_sha256": sha256(HOMOTOPY),
    }
    packet["comparison_to_A379"] = {
        "A379_maximum_beta_component_radius_upper": float(
            selected["summary"]["maximum_beta_component_radius_upper"]
        ),
        "A391_maximum_beta_component_radius_upper": float(
            packet["summary"]["maximum_beta_component_radius_upper"]
        ),
        "beta_radius_tightening_factor": beta_factor,
        "A379_maximum_Hessian_component_radius_upper": float(
            selected["summary"]["maximum_Hessian_component_radius_upper"]
        ),
        "A391_maximum_Hessian_component_radius_upper": float(
            packet["summary"]["maximum_Hessian_component_radius_upper"]
        ),
        "Hessian_radius_tightening_factor": hessian_factor,
        "both_maximum_radii_tighter_than_A379": beta_factor > 1.0
        and hessian_factor > 1.0,
    }
    packet["execution"]["stable_accelerated_runtime"] = {
        "C_backed_Taylor_products": True,
        "growth_integral_majorant": "A*h*exp(L*h)",
        "zero_containing_linear_defect_interval_supported": True,
    }
    packet["authority"].update(
        {
            "A390H_left_upper_homotopy": authority(HOMOTOPY),
            "A379_comparison_source": authority(A379),
            "C_backed_Taylor_runtime": authority(fast_runtime),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "stable_affine_Hessian_runtime": authority(stable_runtime),
            "stable_affine_Hessian_inclusion_audit": authority(STABLE_AUDIT),
            "left_upper_route_runner": authority(Path(__file__).resolve()),
        }
    )
    packet["strict_scope"].update(
        {
            "A390H_selected_branch_homotopy_consumed": True,
            "left_upper_route_beta_Hessian_interval_executed": True,
            "all_step_bounds_finite": True,
            "both_maximum_radii_tighter_than_A379": beta_factor > 1.0
            and hessian_factor > 1.0,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        }
    )
    packet["next_required_artifact"] = (
        "rebuild the aligned residual interval from A391 and test the A385S "
        "Krawczyk self-map"
        if beta_factor > 1.0 and hessian_factor > 1.0
        else "retain A379 and pursue dependency-preserving residual evaluation"
    )
    OUTPUT.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    NOTE.write_text(
        "# MTT q79 Height-Four Left-Upper Beta Hessian (A391) v1\n\n"
        "A391 consumes the A390H interval homotopy and executes the same validated "
        "beta/Hessian system on the selected left-upper contour.\n\n"
        f"The beta-radius tightening factor relative to A379 is `{beta_factor:.12g}`; "
        f"the Hessian-radius factor is `{hessian_factor:.12g}`.\n\n"
        "This route execution does not by itself establish a Krawczyk self-map or "
        "a covariant zero.\n",
        encoding="utf-8",
    )
    print(f"promoted {relative(OUTPUT)} with A390H route authority", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
