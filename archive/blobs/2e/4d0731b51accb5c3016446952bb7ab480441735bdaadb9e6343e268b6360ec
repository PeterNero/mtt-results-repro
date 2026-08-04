from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import ctx

import certify_q79_height4_target_main_hessian_interval as main_hessian
import q79_fast_taylor_runtime as fast


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"


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
    value.add_argument("--order", type=int, default=40)
    value.add_argument("--maximum-step", type=float, default=0.015)
    value.add_argument("--minimum-step", type=float, default=1.0e-12)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-lift-correction", type=float, default=2.0e-7)
    value.add_argument("--maximum-output-increment", type=float, default=5.0e-5)
    value.add_argument("--maximum-output-radius", type=float, default=0.01)
    value.add_argument("--resume", action="store_true")
    value.add_argument("--smoke-only", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    ctx.dps = arguments.dps
    runtime = Path(fast.__file__).resolve()
    original_configuration = main_hessian.configuration

    def accelerated_configuration(*args, **kwargs) -> dict:
        value = original_configuration(*args, **kwargs)
        value["C_backed_Taylor_runtime_sha256"] = sha256(runtime)
        value["C_backed_Taylor_equivalence_audit_sha256"] = sha256(AUDIT)
        return value

    main_hessian.configuration = accelerated_configuration
    try:
        fast.install()
        packet = main_hessian.execute(arguments)
    finally:
        fast.uninstall()
        main_hessian.configuration = original_configuration
    if arguments.smoke_only:
        return 0

    selected = main_hessian.target_paths(arguments.index)
    packet = load(selected["output"])
    packet["execution"]["C_backed_Taylor_runtime"] = {
        "installed": True,
        "reference_engine_retained": relative(Path(main_hessian.validated.__file__).resolve()),
        "equivalence_gate": relative(AUDIT),
    }
    packet["authority"]["C_backed_Taylor_runtime"] = authority(runtime)
    packet["authority"]["C_backed_Taylor_equivalence_audit"] = authority(AUDIT)
    packet["authority"]["accelerated_runner"] = authority(Path(__file__).resolve())
    packet["strict_scope"]["C_backed_polynomial_acceleration_equivalence_audited"] = True
    dump(selected["output"], packet)
    print(
        f"promoted {relative(selected['output'])} with separately hashed "
        "C-backed Taylor runtime"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
