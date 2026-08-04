"""Validate a block-factorized Iwasawa twisted packet candidate.

This validator is intentionally weaker than selected-source promotion.  It
checks the finite architecture forced by the qutrit obstruction:

* a rank-three family block with nontrivial projective rho_E gluing,
* a separate rank-one ordinary Higgs line,
* a complete SM-sector partition across those blocks,
* guardrails that prevent the packet from being mistaken for selected D_E,
  primitive C1, or full SM data.

Exit codes:
  0: block-factorized candidate schema passes implemented checks
  1: complete candidate fails a mathematical/schema/guardrail check
  2: candidate is incomplete/open in a way that prevents validation
"""

from __future__ import annotations

import json
import math
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCHEMA = "IwasawaBlockFactorizedTwistedPacket.v1"
FAMILY_SECTORS = {"Q", "u", "d", "L", "e", "N"}
HIGGS_SECTORS = {"H"}
ALL_SECTORS = FAMILY_SECTORS | HIGGS_SECTORS
GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
EXPECTED_COCYCLE = {
    "base_group": "F_3^2",
    "omega_order": 3,
    "commutator_rank_over_F3": 2,
    "finite_heisenberg_extension_order": 27,
    "center_order": 3,
    "ordinary_bundle_coboundary_possible": False,
}
TOL = 1e-9


class IncompleteData(ValueError):
    """Raised when a required candidate field is absent."""


def resolve_path(value: Any, packet_path: Path, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise IncompleteData(f"MISSING {label}")
    raw = Path(value)
    candidates = []
    if raw.is_absolute():
        candidates.append(raw)
    else:
        candidates.append((packet_path.parent / raw).resolve())
        candidates.append((ROOT / raw).resolve())
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise IncompleteData(f"MISSING file for {label}: {value}")


def run_validator(script_name: str, data_path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script_name), str(data_path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def parse_projective_report(output: str) -> dict[str, Any]:
    match = re.search(r"projective_report=(\{.*\})", output)
    if not match:
        raise ValueError("missing projective_report in projective validator output")
    return json.loads(match.group(1))


def parse_complex(value: Any) -> complex:
    if isinstance(value, bool):
        raise ValueError(f"invalid complex scalar {value!r}")
    if isinstance(value, (int, float)):
        return complex(float(value), 0.0)
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) and not isinstance(part, bool) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise ValueError(f"invalid complex scalar {value!r}")


def matrix_rank_1x1(matrix: Any) -> int:
    if matrix != [[1]]:
        return 0
    return 1


def validate_top_flags(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if data.get("schema") != SCHEMA:
        failures.append(f"schema must be {SCHEMA}")
    if data.get("status") != "CANDIDATE_BLOCK_FACTORIZED_VALIDATED_SELECTION_OPEN":
        failures.append("status must record candidate validation with selection open")
    if data.get("selected_by_mtt") is not False:
        failures.append("selected_by_mtt must remain false for this candidate packet")
    if data.get("fixed_topological_sector") is not False:
        failures.append("fixed_topological_sector must remain false until selected source data exist")
    if data.get("no_observed_flavor_inputs") is not True:
        failures.append("no_observed_flavor_inputs must be true")
    for key in (
        "uses_execution_ii_benchmarks",
        "uses_observed_masses_or_mixings",
        "uses_naive_rank4_direct_sum",
        "uses_zeta3_twist_as_q79_replacement",
    ):
        if data.get(key) is not False:
            failures.append(f"{key} must be false")
    return failures


def validate_family_block(
    packet_path: Path,
    data: dict[str, Any],
) -> tuple[list[str], dict[str, Any]]:
    family = data.get("family_twist_block")
    if not isinstance(family, dict):
        raise IncompleteData("MISSING family_twist_block object")

    failures: list[str] = []
    if family.get("rank") != 3:
        failures.append("family_twist_block.rank must equal 3")
    if set(family.get("sectors", [])) != FAMILY_SECTORS:
        failures.append("family_twist_block.sectors must be Q,u,d,L,e,N")

    cocycle = family.get("central_cocycle")
    if not isinstance(cocycle, dict):
        raise IncompleteData("MISSING family_twist_block.central_cocycle")
    for key, expected in EXPECTED_COCYCLE.items():
        if cocycle.get(key) != expected:
            failures.append(f"family_twist_block.central_cocycle.{key} must be {expected!r}")

    if family.get("selected_gerbe_source_verified") is not False:
        failures.append("selected_gerbe_source_verified must remain false in this packet")

    gerbe_cert = resolve_path(
        family.get("gerbe_holonomy_candidate"),
        packet_path,
        "family_twist_block.gerbe_holonomy_candidate",
    )
    gerbe_data = json.loads(gerbe_cert.read_text(encoding="utf-8"))
    if (
        gerbe_data.get("status")
        != "IWASAWA_DISCRETE_GERBE_HOLONOMY_CANDIDATE_MAP_CLOSED_SELECTION_OPEN"
    ):
        failures.append("gerbe holonomy candidate certificate has unexpected status")

    mesh_path = resolve_path(
        family.get("projective_rhoE_mesh"),
        packet_path,
        "family_twist_block.projective_rhoE_mesh",
    )
    code, output = run_validator("validate_iwasawa_projective_rhoE_mesh.py", mesh_path)
    if code == 2:
        raise IncompleteData(f"family projective rho_E mesh incomplete: {output.strip()}")
    if code != 0:
        failures.append(f"family projective rho_E mesh validator failed with exit {code}")
        report: dict[str, Any] = {}
    else:
        report = parse_projective_report(output)
        if report.get("projective_gerbe_gluing_passes") is not True:
            failures.append("family projective gerbe gluing must pass")
        if report.get("central_twist_is_nontrivial") is not True:
            failures.append("family central twist must be nontrivial")
        histogram = report.get("central_phase_histogram", {})
        if not any(label in histogram for label in ("zeta_3^1", "zeta_3^2")):
            failures.append("family central phase histogram must contain a nontrivial zeta_3 phase")

    return failures, {
        "mesh_path": str(mesh_path),
        "projective_validator_exit": code,
        "projective_report": report,
        "gerbe_holonomy_candidate": str(gerbe_cert),
    }


def validate_higgs_line(data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    higgs = data.get("higgs_line_block")
    if not isinstance(higgs, dict):
        raise IncompleteData("MISSING higgs_line_block object")

    failures: list[str] = []
    if higgs.get("rank") != 1:
        failures.append("higgs_line_block.rank must equal 1")
    if set(higgs.get("sectors", [])) != HIGGS_SECTORS:
        failures.append("higgs_line_block.sectors must be exactly H")
    if higgs.get("kind") != "ordinary_trivial_line":
        failures.append("higgs_line_block.kind must be ordinary_trivial_line")
    if matrix_rank_1x1(higgs.get("projector")) != 1:
        failures.append("higgs_line_block.projector must be the rank-one 1x1 identity")

    scalars = higgs.get("transition_scalars")
    if not isinstance(scalars, dict):
        raise IncompleteData("MISSING higgs_line_block.transition_scalars")

    parsed: dict[str, complex] = {}
    for generator in GENERATORS:
        if generator not in scalars:
            raise IncompleteData(f"MISSING higgs_line_block.transition_scalars.{generator}")
        scalar = parse_complex(scalars[generator])
        parsed[generator] = scalar
        if abs(abs(scalar) - 1.0) > TOL:
            failures.append(f"higgs scalar {generator} is not unitary")
        if abs(scalar - 1.0) > TOL:
            failures.append(f"higgs scalar {generator} must be trivial identity in this candidate")

    strict_corner_gluing = all(abs(value - 1.0) <= TOL for value in parsed.values())
    return failures, {
        "rank_one_projector": True,
        "transition_scalars": {key: [value.real, value.imag] for key, value in parsed.items()},
        "ordinary_line_strict_gluing_passes": strict_corner_gluing,
    }


def validate_sector_partition(data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    family = data.get("family_twist_block", {})
    higgs = data.get("higgs_line_block", {})
    family_sectors = set(family.get("sectors", [])) if isinstance(family, dict) else set()
    higgs_sectors = set(higgs.get("sectors", [])) if isinstance(higgs, dict) else set()
    overlap = sorted(family_sectors & higgs_sectors)
    union = family_sectors | higgs_sectors
    failures = []
    if overlap:
        failures.append(f"sector partition overlap: {overlap}")
    if union != ALL_SECTORS:
        failures.append(f"sector partition must cover {sorted(ALL_SECTORS)}")
    return failures, {
        "family_sectors": sorted(family_sectors),
        "higgs_sectors": sorted(higgs_sectors),
        "overlap": overlap,
        "covers_all_sm_slots": union == ALL_SECTORS and not overlap,
    }


def validate_coupling_rule(data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    coupling = data.get("coupling_rule")
    if not isinstance(coupling, dict):
        raise IncompleteData("MISSING coupling_rule object")

    failures: list[str] = []
    if coupling.get("status") != "OPEN":
        failures.append("coupling_rule.status must remain OPEN")
    if coupling.get("block_factorized_tensor_coupling_formulated") is not True:
        failures.append("block_factorized_tensor_coupling_formulated must be true")
    if coupling.get("finite_invariant_pairing_rule") != (
        "s_left+s_right=0 mod 3 for trivial-Higgs SM pairs"
    ):
        failures.append("finite_invariant_pairing_rule must record the qutrit pair rule")
    if coupling.get("same_twist_all_family_allowed_for_trivial_Higgs") is not False:
        failures.append("same_twist_all_family_allowed_for_trivial_Higgs must be false")
    if coupling.get("conjugate_orientation_pairing_required") is not True:
        failures.append("conjugate_orientation_pairing_required must be true")
    if coupling.get("selected_sector_orientation_assignment_supplied") is not False:
        failures.append("selected_sector_orientation_assignment_supplied must be false")
    if coupling.get("single_rank4_scalar_projective_carrier_allowed") is not False:
        failures.append("single_rank4_scalar_projective_carrier_allowed must be false")
    for key in (
        "selected_D_E_supplied",
        "selected_dotD_supplied",
        "primitive_C1_contractions_supplied",
        "yukawa_overlap_weights_supplied",
    ):
        if coupling.get(key) is not False:
            failures.append(f"{key} must be false in this candidate packet")

    return failures, {
        "status": coupling.get("status"),
        "single_rank4_scalar_projective_carrier_allowed": coupling.get(
            "single_rank4_scalar_projective_carrier_allowed"
        ),
        "finite_invariant_pairing_rule": coupling.get("finite_invariant_pairing_rule"),
        "same_twist_all_family_allowed_for_trivial_Higgs": coupling.get(
            "same_twist_all_family_allowed_for_trivial_Higgs"
        ),
        "conjugate_orientation_pairing_required": coupling.get(
            "conjugate_orientation_pairing_required"
        ),
        "selected_sector_orientation_assignment_supplied": coupling.get(
            "selected_sector_orientation_assignment_supplied"
        ),
        "selected_D_E_supplied": coupling.get("selected_D_E_supplied"),
        "selected_dotD_supplied": coupling.get("selected_dotD_supplied"),
        "primitive_C1_contractions_supplied": coupling.get(
            "primitive_C1_contractions_supplied"
        ),
        "yukawa_overlap_weights_supplied": coupling.get("yukawa_overlap_weights_supplied"),
    }


def validate_packet(packet_path: Path, data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    failures = validate_top_flags(data)
    family_failures, family_report = validate_family_block(packet_path, data)
    higgs_failures, higgs_report = validate_higgs_line(data)
    sector_failures, sector_report = validate_sector_partition(data)
    coupling_failures, coupling_report = validate_coupling_rule(data)
    failures.extend(family_failures)
    failures.extend(higgs_failures)
    failures.extend(sector_failures)
    failures.extend(coupling_failures)

    report = {
        "schema": data.get("schema"),
        "status": data.get("status"),
        "family_twist_block": family_report,
        "higgs_line_block": higgs_report,
        "sector_partition": sector_report,
        "coupling_rule": coupling_report,
        "block_factorized_candidate_valid": not failures,
        "selected_source_promotion_ready": False,
        "full_sm_data_ready": False,
    }
    return failures, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_block_factorized_twisted_packet.py <packet.json>")
        return 1

    packet_path = Path(argv[1]).resolve()
    try:
        data = json.loads(packet_path.read_text(encoding="utf-8"))
        failures, report = validate_packet(packet_path, data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID block-factorized twisted packet: {exc}")
        return 1

    print(f"block_factorized_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("block-factorized twisted packet validation FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("block-factorized twisted packet validation PASS")
    print("finite family twist and separate Higgs line validate; selected D_E/C1 data remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
