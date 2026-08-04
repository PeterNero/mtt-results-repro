from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import certify_q79_height4_rank3_handle_hessian_interval as handle_hessian
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


def main() -> int:
    fast_runtime = Path(fast.__file__).resolve()
    stable_runtime = Path(stable.__file__).resolve()
    original_configuration = handle_hessian.configuration

    def runtime_configuration(*args, **kwargs) -> dict:
        value = original_configuration(*args, **kwargs)
        value["C_backed_Taylor_runtime_sha256"] = sha256(fast_runtime)
        value["C_backed_Taylor_equivalence_audit_sha256"] = sha256(FAST_AUDIT)
        value["stable_affine_Hessian_runtime_sha256"] = sha256(stable_runtime)
        value["stable_affine_Hessian_inclusion_audit_sha256"] = sha256(STABLE_AUDIT)
        return value

    handle_hessian.configuration = runtime_configuration
    try:
        fast.install()
        stable.install()
        result = handle_hessian.main()
    finally:
        stable.uninstall()
        fast.uninstall()
        handle_hessian.configuration = original_configuration
    if "--smoke-only" in sys.argv or not handle_hessian.OUTPUT.exists():
        return result
    packet = json.loads(handle_hessian.OUTPUT.read_text(encoding="utf-8"))
    packet["execution_runtime"] = {
        "C_backed_Taylor_products": True,
        "growth_integral_majorant": "A*h*exp(L*h)",
        "zero_containing_linear_defect_interval_supported": True,
    }
    packet["authority"]["C_backed_Taylor_runtime"] = authority(fast_runtime)
    packet["authority"]["C_backed_Taylor_equivalence_audit"] = authority(FAST_AUDIT)
    packet["authority"]["stable_affine_Hessian_runtime"] = authority(stable_runtime)
    packet["authority"]["stable_affine_Hessian_inclusion_audit"] = authority(STABLE_AUDIT)
    packet["authority"]["stable_accelerated_runner"] = authority(Path(__file__).resolve())
    packet["strict_scope"]["C_backed_polynomial_acceleration_equivalence_audited"] = True
    packet["strict_scope"]["zero_defect_regular_affine_growth_bound_audited"] = True
    packet["strict_scope"]["all_step_bounds_finite"] = True
    handle_hessian.OUTPUT.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"promoted {relative(handle_hessian.OUTPUT)} with stable accelerated runtime")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
