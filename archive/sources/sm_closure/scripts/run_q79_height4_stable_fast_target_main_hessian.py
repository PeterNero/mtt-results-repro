from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import ctx

import certify_q79_height4_target_main_hessian_interval as main_hessian
import q79_fast_taylor_runtime as fast
import q79_stable_affine_hessian_runtime as stable


ROOT = Path(__file__).resolve().parents[1]
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
STABLE_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79stableaffinehessianruntime_inclusion_audit.py"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--dps", type=int, default=100)
    value.add_argument("--order", type=int, default=48)
    value.add_argument("--maximum-step", type=float, default=0.02)
    value.add_argument("--minimum-step", type=float, default=1.0e-12)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-7)
    value.add_argument("--maximum-output-increment", type=float, default=1.0e-5)
    value.add_argument("--maximum-output-radius", type=float, default=0.005)
    value.add_argument("--resume", action="store_true")
    value.add_argument("--smoke-only", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    ctx.dps = arguments.dps
    fast_runtime = Path(fast.__file__).resolve()
    stable_runtime = Path(stable.__file__).resolve()
    original_configuration = main_hessian.configuration

    def accelerated_configuration(*args, **kwargs) -> dict:
        value = original_configuration(*args, **kwargs)
        value["C_backed_Taylor_runtime_sha256"] = sha256(fast_runtime)
        value["C_backed_Taylor_equivalence_audit_sha256"] = sha256(FAST_AUDIT)
        value["stable_affine_Hessian_runtime_sha256"] = sha256(stable_runtime)
        value["stable_affine_Hessian_inclusion_audit_sha256"] = sha256(STABLE_AUDIT)
        return value

    main_hessian.configuration = accelerated_configuration
    try:
        fast.install()
        stable.install()
        main_hessian.execute(arguments)
    finally:
        stable.uninstall()
        fast.uninstall()
        main_hessian.configuration = original_configuration
    if arguments.smoke_only:
        return 0

    selected = main_hessian.target_paths(arguments.index)
    packet = load(selected["output"])
    packet["execution"]["stable_affine_Hessian_runtime"] = {
        "installed": True,
        "growth_integral_majorant": "A*h*exp(L*h)",
        "zero_containing_linear_defect_interval_supported": True,
        "inclusion_gate": relative(STABLE_AUDIT),
    }
    packet["authority"]["C_backed_Taylor_runtime"] = authority(fast_runtime)
    packet["authority"]["C_backed_Taylor_equivalence_audit"] = authority(FAST_AUDIT)
    packet["authority"]["stable_affine_Hessian_runtime"] = authority(stable_runtime)
    packet["authority"]["stable_affine_Hessian_inclusion_audit"] = authority(
        STABLE_AUDIT
    )
    packet["authority"]["stable_accelerated_runner"] = authority(
        Path(__file__).resolve()
    )
    packet["strict_scope"]["C_backed_polynomial_acceleration_equivalence_audited"] = True
    packet["strict_scope"]["zero_defect_regular_affine_growth_bound_audited"] = True
    packet["strict_scope"]["all_step_bounds_finite"] = True
    dump(selected["output"], packet)
    print(
        f"promoted {relative(selected['output'])} with separately hashed C-backed "
        "Taylor and zero-defect-stable affine-Hessian runtimes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
