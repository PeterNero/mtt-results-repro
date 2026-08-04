from __future__ import annotations

import json
import sys
from pathlib import Path

import certify_q79_height4_interior_affine_chain_basis_reanchor as ordinary
import certify_q79_height4_target_main_hessian_interval as base


def argument_path(name: str) -> Path:
    try:
        return Path(sys.argv[sys.argv.index(name) + 1]).resolve()
    except (ValueError, IndexError) as error:
        raise ValueError(f"adaptive affine reanchor requires {name}") from error


def authority(path: Path) -> dict[str, str]:
    return {"path": base.relative(path), "sha256": base.sha256(path)}


def main() -> int:
    output = argument_path("--output")
    reanchored_checkpoint = argument_path("--reanchored-checkpoint")
    original = base.handle.direct_cut_periods

    def adaptive_direct_cut_periods(
        roots,
        leading,
        pair,
        *,
        segments: int,
        tolerance: float,
    ):
        failures: list[str] = []
        for multiplier in (1, 2, 4, 8, 16):
            selected_segments = segments * multiplier
            try:
                values, diagnostics = original(
                    roots,
                    leading,
                    pair,
                    segments=selected_segments,
                    tolerance=tolerance,
                )
                diagnostics = {
                    **diagnostics,
                    "adaptive_requested_segments": segments,
                    "adaptive_selected_segments": selected_segments,
                    "adaptive_subdivision_multiplier": multiplier,
                    "rejected_coarser_attempts": failures,
                }
                return values, diagnostics
            except AssertionError as error:
                message = str(error)
                if message not in {
                    "cut remainder does not fit a square-root half-plane",
                    "cut square-root sign is not interval-separated",
                }:
                    raise
                failures.append(f"{selected_segments}: {message}")
        raise AssertionError(
            "adaptive direct-cut subdivision failed through multiplier 16: "
            + "; ".join(failures)
        )

    base.handle.direct_cut_periods = adaptive_direct_cut_periods
    try:
        result = ordinary.main()
    finally:
        base.handle.direct_cut_periods = original
    if result != 0:
        return result

    certificate = base.load(output)
    certificate["artifact"] = "A380ABIA"
    certificate["authority"]["adaptive_cut_subdivision_wrapper"] = authority(
        Path(__file__).resolve()
    )
    certificate["strict_scope"]["adaptive_cut_subdivision_only"] = True
    certificate["strict_scope"]["cycle_or_source_changed_by_adaptation"] = False
    selected_multipliers = [
        int(row.get("adaptive_subdivision_multiplier", 1))
        for row in certificate["cut_system"]["direct_cut_diagnostics"]
    ]
    certificate["adaptive_cut_subdivision"] = {
        "rule": "retry the same direct arc at 2^k times the canonical theta subdivision",
        "maximum_allowed_multiplier": 16,
        "selected_multipliers_by_adjacent_arc": selected_multipliers,
        "maximum_selected_multiplier": max(selected_multipliers),
        "same_interval_half_plane_and_sign_tests_used": True,
        "same_quadrature_tolerance_used": True,
    }
    base.dump(output, certificate)

    checkpoint = base.load(reanchored_checkpoint)
    checkpoint["affine_chain_basis_reanchor"]["certificate"] = authority(output)
    checkpoint["affine_chain_basis_reanchor"][
        "adaptive_cut_subdivision_used"
    ] = max(selected_multipliers) > 1
    base.dump(reanchored_checkpoint, checkpoint)
    print(
        json.dumps(
            {
                "adaptive_selected_multipliers": selected_multipliers,
                "certificate": authority(output),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
