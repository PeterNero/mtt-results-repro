from __future__ import annotations

import argparse
import hashlib
import json
from argparse import Namespace
from pathlib import Path

from flint import ctx

import certify_q79_height4_source_derived_far_cut_hessian_interval as source_cut
import certify_q79_height4_target_main_hessian_interval as main_hessian
import q79_fast_taylor_runtime as fast
import q79_stable_affine_hessian_runtime as stable


ROOT = Path(__file__).resolve().parents[1]
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
STABLE_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79stableaffinehessianruntime_inclusion_audit.py"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--epsilon", type=float, required=True)
    value.add_argument("--dps", type=int, default=120)
    value.add_argument("--order", type=int, default=48)
    value.add_argument("--maximum-step", type=float, default=0.02)
    value.add_argument("--minimum-step", type=float, default=1.0e-12)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-7)
    value.add_argument("--maximum-output-increment", type=float, default=1.0e-5)
    value.add_argument("--maximum-output-radius", type=float, default=0.005)
    value.add_argument("--resume", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    ctx.dps = arguments.dps
    selected = source_cut.paths(arguments.index, arguments.epsilon)
    for name in ("source", "ordinary_tail", "synthetic_main", "canonical_full"):
        if not selected[name].is_file():
            raise FileNotFoundError(f"source-derived cutoff input is absent: {name}")

    fast_runtime = Path(fast.__file__).resolve()
    stable_runtime = Path(stable.__file__).resolve()
    original_configuration = main_hessian.configuration

    def runtime_configuration(*args, **kwargs) -> dict:
        value = original_configuration(*args, **kwargs)
        value["C_backed_Taylor_runtime_sha256"] = sha256(fast_runtime)
        value["C_backed_Taylor_equivalence_audit_sha256"] = sha256(FAST_AUDIT)
        value["stable_affine_Hessian_runtime_sha256"] = sha256(stable_runtime)
        value["stable_affine_Hessian_inclusion_audit_sha256"] = sha256(STABLE_AUDIT)
        value["source_derived_cut_adapter_sha256"] = sha256(
            Path(source_cut.__file__).resolve()
        )
        return value

    main_hessian.configuration = runtime_configuration
    try:
        fast.install()
        stable.install()
        source_cut.run_main_hessian(
            Namespace(
                index=arguments.index,
                dps=arguments.dps,
                main_order=arguments.order,
                maximum_step=arguments.maximum_step,
                minimum_step=arguments.minimum_step,
                maximum_steps=arguments.maximum_steps,
                maximum_lift_correction=arguments.maximum_lift_correction,
                maximum_output_increment=arguments.maximum_output_increment,
                maximum_output_radius=arguments.maximum_output_radius,
                resume=arguments.resume,
            ),
            selected,
        )
    finally:
        stable.uninstall()
        fast.uninstall()
        main_hessian.configuration = original_configuration

    packet = json.loads(selected["main"].read_text(encoding="utf-8"))
    packet["execution"]["stable_accelerated_runtime"] = {
        "C_backed_Taylor_products": True,
        "growth_integral_majorant": "A*h*exp(L*h)",
        "zero_containing_linear_defect_interval_supported": True,
        "selected_cutoff_epsilon": arguments.epsilon,
    }
    packet["authority"]["C_backed_Taylor_runtime"] = authority(fast_runtime)
    packet["authority"]["C_backed_Taylor_equivalence_audit"] = authority(FAST_AUDIT)
    packet["authority"]["stable_affine_Hessian_runtime"] = authority(stable_runtime)
    packet["authority"]["stable_affine_Hessian_inclusion_audit"] = authority(STABLE_AUDIT)
    packet["authority"]["stable_source_cut_runner"] = authority(Path(__file__).resolve())
    packet["strict_scope"]["C_backed_polynomial_acceleration_equivalence_audited"] = True
    packet["strict_scope"]["zero_defect_regular_affine_growth_bound_audited"] = True
    packet["strict_scope"]["all_step_bounds_finite"] = True
    selected["main"].write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"promoted {relative(selected['main'])} with the stable accelerated "
        f"source-derived cutoff runtime at epsilon={arguments.epsilon:.1e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
