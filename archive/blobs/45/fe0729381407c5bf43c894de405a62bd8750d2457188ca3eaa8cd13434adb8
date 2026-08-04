from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRANSPORT_ENGINE = ROOT / "scripts" / "certify_q79_selected_side_beta_defect_transport.py"
MAIN_ENGINE = (
    ROOT
    / "scripts"
    / "certify_q79_selected_alignment_single_E32_thimble_main_interval.py"
)
FULL_BUILDER = ROOT / "scripts" / "build_selected_q79_single_E32_thimble_full_interval.py"
POLYGONAL_MAIN_ENGINE = (
    ROOT
    / "scripts"
    / "certify_q79_selected_alignment_E32_thimble_polygonal_main_interval.py"
)

HISTORICAL_TRANSPORT_SHA256 = (
    "1b99c9920f60936ba2ce600ebbdb19645122643e2bd81f7d321e2f4449cfb33b"
)
CURRENT_TRANSPORT_SHA256 = (
    "2b96ca4ffba10106c75822ee0b2ca13e2455cb435d008294d70d5ae19703099b"
)
HISTORICAL_MAIN_SHA256 = (
    "13702262eaa3463cb628acab1d703e949b5c4663be077bfadfbf3000bf244a98"
)
CURRENT_MAIN_SHA256 = (
    "aa743ed209dcc2861fdf6c5e0694f1c5aa8784771558b5bca87fdb76947d9081"
)
HISTORICAL_FULL_SHA256 = (
    "b1dc64fb1b8c961897209ca38fbf15949da4942a5547230a58b2ab16b4cbb3c9"
)
CURRENT_FULL_SHA256 = (
    "5670d9485567f49f8ad11975d435d38271181ae65eecb320173784637a115c84"
)
HISTORICAL_POLYGONAL_MAIN_SHA256 = (
    "e6b2d311a2c44e39544979fbc7a60200af6f3984b23566253436d0c269efad5c"
)
CURRENT_POLYGONAL_MAIN_SHA256 = (
    "8e895e260bc17daa66c7b9836ba7804ff93b797cb775da34ef641effa44fea03"
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def replace_exact(text: str, old: str, new: str, *, count: int = 1) -> str:
    actual = text.count(old)
    if actual != count:
        raise AssertionError(
            f"source specialization block count changed: expected {count}, found {actual}"
        )
    return text.replace(old, new)


def historical_transport_y_specialization() -> str:
    text = TRANSPORT_ENGINE.read_text(encoding="utf-8")
    text = replace_exact(
        text,
        '''    def __init__(self, *, dps: int, line_chart: str = "y") -> None:
        ctx.dps = dps
        if line_chart not in {"y", "z"}:
            raise ValueError("selected line chart must be y or z")
        self.line_chart = line_chart
        self.line_chart_denominator_index = 1 if line_chart == "y" else 2
''',
        '''    def __init__(self, *, dps: int) -> None:
        ctx.dps = dps
''',
    )
    text = replace_exact(
        text,
        '''        self.diagnostics.minimum_chart_scale_lower = min(
            self.diagnostics.minimum_chart_scale_lower,
            lower(abs(line[self.line_chart_denominator_index])),
        )
''',
        '''        self.diagnostics.minimum_chart_scale_lower = min(
            self.diagnostics.minimum_chart_scale_lower, lower(abs(line[1]))
        )
''',
    )
    text = replace_exact(
        text,
        "chart=self.line_chart,",
        'chart="y",',
        count=3,
    )
    text = replace_exact(
        text,
        "chart=system.line_chart,",
        'chart="y",',
        count=3,
    )
    for table, target in (("F6", "f_coefficients, f_derivative"), ("G3", "g_coefficients, _"), ("Q2", "q_coefficients, q_derivative")):
        text = replace_exact(
            text,
            f'''    {target} = aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["{table}"],
        line,
        line_derivative,
        chart="y",
    )
''',
            f'''    {target} = aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["{table}"], line, line_derivative, chart="y"
    )
''',
        )
    text = replace_exact(
        text,
        '''            if self.line_chart == "z":
                constant = line[2] * (
                    variation[0] * line[2] - variation[2] * line[0]
                )
                linear = line[2] * (
                    variation[1] * line[2] - variation[2] * line[1]
                )
            else:
                constant = -line[1] * (
                    variation[0] * line[1] - variation[1] * line[0]
                )
                linear = -line[1] * (
                    variation[2] * line[1] - variation[1] * line[2]
                )
''',
        '''            constant = -line[1] * (
                variation[0] * line[1] - variation[1] * line[0]
            )
            linear = -line[1] * (
                variation[2] * line[1] - variation[1] * line[2]
            )
''',
    )
    text = replace_exact(
        text,
        '''        if system.line_chart == "z":
            constant = line[2] * (
                variation[0] * line[2] - variation[2] * line[0]
            )
            linear = line[2] * (
                variation[1] * line[2] - variation[2] * line[1]
            )
        else:
            constant = -line[1] * (
                variation[0] * line[1] - variation[1] * line[0]
            )
            linear = -line[1] * (
                variation[2] * line[1] - variation[1] * line[2]
            )
''',
        '''        constant = -line[1] * (
            variation[0] * line[1] - variation[1] * line[0]
        )
        linear = -line[1] * (
            variation[2] * line[1] - variation[1] * line[2]
        )
''',
    )
    return text


def historical_main_y_specialization() -> str:
    text = MAIN_ENGINE.read_text(encoding="utf-8")
    text = replace_exact(
        text,
        '''    coefficients, _derivative = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
''',
        '''    coefficients, _derivative = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"], line, line_derivative, chart="y"
    )
''',
    )
    text = replace_exact(
        text,
        '''    source_path = candidate_path(arguments.distinguished_index)
    source = load(source_path)
    critical = handle.complex_value(source["critical_center"])
''',
        '''    source_path = candidate_path(arguments.distinguished_index)
    source = load(source_path)
    if source["line_chart"] != "y":
        raise ValueError("pilot interval engine currently requires a selected y-chart thimble")
    critical = handle.complex_value(source["critical_center"])
''',
    )
    text = replace_exact(
        text,
        '''    system = validated.SelectedQ79IntervalSystem(
        dps=arguments.dps, line_chart=source["line_chart"]
    )
''',
        "    system = validated.SelectedQ79IntervalSystem(dps=arguments.dps)\n",
    )
    return text


def historical_full_y_specialization() -> str:
    text = FULL_BUILDER.read_text(encoding="utf-8")
    text = replace_exact(
        text,
        '''    if main_packet["selected_thimble"]["line_chart"] != source["line_chart"]:
        raise AssertionError("main interval and floating source charts differ")
    if tail_packet["selected_thimble"].get("line_chart", "y") != source["line_chart"]:
        raise AssertionError("tail interval and floating source charts differ")
''',
        "",
    )
    text = replace_exact(
        text,
        '            "line_chart": source["line_chart"],\n',
        "",
    )
    return text


def historical_polygonal_main_y_specialization() -> str:
    text = POLYGONAL_MAIN_ENGINE.read_text(encoding="utf-8")
    text = replace_exact(
        text,
        'Z_WALL = DIRECTORY / "selected_alignment_zchart_wall.interval.packet.json"\n',
        "",
    )
    text = replace_exact(
        text,
        '''def certify_detour(
    path: list[complex],
    dual: dict,
    selected_root: str,
    *,
    line_chart: str = "y",
    z_wall: dict | None = None,
) -> dict:
    if line_chart not in {"y", "z"}:
        raise ValueError("selected line chart must be y or z")
    critical_rows = source_points(dual, "critical_points_on_E")
    chart_source = dual if line_chart == "y" else z_wall
    if chart_source is None:
        raise ValueError("z-chart detour certification requires the z-wall packet")
    chart_key = f"selected_{line_chart}_line_chart_zeros"
    chart_rows = source_points(chart_source, chart_key)
''',
        '''def certify_detour(path: list[complex], dual: dict, selected_root: str) -> dict:
    critical_rows = source_points(dual, "critical_points_on_E")
    chart_rows = source_points(dual, "selected_y_line_chart_zeros")
''',
    )
    text = replace_exact(
        text,
        '''        f"selected_{line_chart}_chart_zero_clearance_lower": path_clearance(
            path, chart_points
        ),
''',
        '        "selected_y_chart_zero_clearance_lower": path_clearance(path, chart_points),\n',
    )
    text = replace_exact(
        text,
        '        result[f"selected_{line_chart}_chart_zero_clearance_lower"],\n',
        '        result["selected_y_chart_zero_clearance_lower"],\n',
    )
    text = replace_exact(
        text,
        '''    source_path = pilot.candidate_path(arguments.distinguished_index)
    source = load(source_path)
    critical = handle.complex_value(source["critical_center"])
''',
        '''    source_path = pilot.candidate_path(arguments.distinguished_index)
    source = load(source_path)
    if source["line_chart"] != "y":
        raise ValueError("polygonal pilot currently certifies y-chart thimbles")
    critical = handle.complex_value(source["critical_center"])
''',
    )
    text = replace_exact(
        text,
        '''    dual = load(DUAL)
    z_wall = load(Z_WALL) if source["line_chart"] == "z" else None
    geometry = certify_detour(
        path_w,
        dual,
        source["root_id"],
        line_chart=source["line_chart"],
        z_wall=z_wall,
    )
''',
        '''    dual = load(DUAL)
    geometry = certify_detour(path_w, dual, source["root_id"])
''',
    )
    text = replace_exact(
        text,
        '''    system = validated.SelectedQ79IntervalSystem(
        dps=arguments.dps, line_chart=source["line_chart"]
    )
''',
        "    system = validated.SelectedQ79IntervalSystem(dps=arguments.dps)\n",
    )
    text = replace_exact(
        text,
        '''            "z_chart_wall": (
                relative(Z_WALL) if source["line_chart"] == "z" else None
            ),
            "z_chart_wall_sha256": (
                sha256(Z_WALL) if source["line_chart"] == "z" else None
            ),
''',
        "",
    )
    text = replace_exact(
        text,
        '''            "A123_projective_line_chart_covariance_consumed": (
                source["line_chart"] == "z"
            ),
''',
        "",
    )
    return text


def audit_source_compatibility() -> dict[str, object]:
    current_hashes = {
        "transport_engine": sha256(TRANSPORT_ENGINE),
        "augmented_main_engine": sha256(MAIN_ENGINE),
        "full_splice_builder": sha256(FULL_BUILDER),
        "polygonal_main_engine": sha256(POLYGONAL_MAIN_ENGINE),
    }
    assert current_hashes == {
        "transport_engine": CURRENT_TRANSPORT_SHA256,
        "augmented_main_engine": CURRENT_MAIN_SHA256,
        "full_splice_builder": CURRENT_FULL_SHA256,
        "polygonal_main_engine": CURRENT_POLYGONAL_MAIN_SHA256,
    }
    reconstructed_hashes = {
        "transport_engine": sha256_bytes(
            historical_transport_y_specialization().encode("utf-8")
        ),
        "augmented_main_engine": sha256_bytes(
            historical_main_y_specialization().encode("utf-8")
        ),
        "full_splice_builder": sha256_bytes(
            historical_full_y_specialization().encode("utf-8")
        ),
        "polygonal_main_engine": sha256_bytes(
            historical_polygonal_main_y_specialization().encode("utf-8")
        ),
    }
    assert reconstructed_hashes == {
        "transport_engine": HISTORICAL_TRANSPORT_SHA256,
        "augmented_main_engine": HISTORICAL_MAIN_SHA256,
        "full_splice_builder": HISTORICAL_FULL_SHA256,
        "polygonal_main_engine": HISTORICAL_POLYGONAL_MAIN_SHA256,
    }
    return {
        "method": (
            "reverse only the explicit y/z chart parameterization and strict chart guards; "
            "hash the canonical-LF y specialization"
        ),
        "current_source_hashes": current_hashes,
        "reconstructed_historical_y_hashes": reconstructed_hashes,
        "byte_exact_historical_y_specialization_closed": True,
        "historical_packets_relabelled_as_new_runs": False,
    }


def compatible_source_hash(path: Path, expected_hash: str) -> bool:
    if sha256(path) == expected_hash:
        return True
    compatibility = audit_source_compatibility()
    relative = str(path.resolve().relative_to(ROOT)).replace("\\", "/")
    aliases = {
        "scripts/certify_q79_selected_side_beta_defect_transport.py": (
            "transport_engine"
        ),
        "scripts/certify_q79_selected_alignment_single_E32_thimble_main_interval.py": (
            "augmented_main_engine"
        ),
        "scripts/build_selected_q79_single_E32_thimble_full_interval.py": (
            "full_splice_builder"
        ),
        "scripts/certify_q79_selected_alignment_E32_thimble_polygonal_main_interval.py": (
            "polygonal_main_engine"
        ),
    }
    key = aliases.get(relative)
    if key is None:
        return False
    return (
        expected_hash
        == compatibility["reconstructed_historical_y_hashes"][key]
        and sha256(path) == compatibility["current_source_hashes"][key]
    )


if __name__ == "__main__":
    audit_source_compatibility()
    print("q79 y-chart byte-exact conservative extension audit: PASS")
