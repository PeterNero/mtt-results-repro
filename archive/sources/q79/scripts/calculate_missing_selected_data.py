"""Calculate the currently missing selected data for no-proxy SM closure.

The script does not invent physics input. It scans the proof-repro certificates
and reports which finite data atoms are still absent before the selected C1
response matrices, Yukawa matrices, and full SM data can be computed.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"

DATA_KEYS = (
    "operator_slots",
    "spectral_slots",
    "green_slots",
    "dotd_response_slots",
)
PRIMITIVE_TERMS = (
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
)
PRIMITIVE_SECTORS = ("u", "d", "e", "nuD")


def load_json(name: str) -> dict[str, Any]:
    path = CERTIFICATES / name
    return json.loads(path.read_text(encoding="utf-8"))


def null_paths(value: Any, prefix: str = "") -> list[str]:
    if value is None:
        return [prefix]
    if isinstance(value, dict):
        paths: list[str] = []
        for key, item in value.items():
            child = f"{prefix}.{key}" if prefix else str(key)
            paths.extend(null_paths(item, child))
        return paths
    if isinstance(value, list):
        paths = []
        for index, item in enumerate(value):
            child = f"{prefix}[{index}]"
            paths.extend(null_paths(item, child))
        return paths
    return []


def false_paths(value: Any, prefix: str = "") -> list[str]:
    if value is False:
        return [prefix]
    if isinstance(value, dict):
        paths: list[str] = []
        for key, item in value.items():
            child = f"{prefix}.{key}" if prefix else str(key)
            paths.extend(false_paths(item, child))
        return paths
    if isinstance(value, list):
        paths = []
        for index, item in enumerate(value):
            child = f"{prefix}[{index}]"
            paths.extend(false_paths(item, child))
        return paths
    return []


def find_key_paths(value: Any, key_name: str, prefix: str = "") -> list[str]:
    paths: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            child = f"{prefix}.{key}" if prefix else str(key)
            if key == key_name:
                paths.append(child)
            paths.extend(find_key_paths(item, key_name, child))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            child = f"{prefix}[{index}]"
            paths.extend(find_key_paths(item, key_name, child))
    return paths


def scan_data_key_files() -> dict[str, list[str]]:
    hits = {key: [] for key in DATA_KEYS}
    for path in sorted(CERTIFICATES.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for key in DATA_KEYS:
            key_paths = find_key_paths(data, key)
            for key_path in key_paths:
                # Validator certificates and open templates describe formats; they
                # are not filled selected operator data.
                if path.name.endswith("_validator_certificate.json") or path.name.endswith(
                    ".template.json"
                ):
                    continue
                hits[key].append(f"{path.name}:{key_path}")
    return hits


def primitive_missing(template: dict[str, Any]) -> list[str]:
    sectors = template.get("sectors", {})
    missing: list[str] = []
    for sector in PRIMITIVE_SECTORS:
        sector_data = sectors.get(sector, {})
        for term in PRIMITIVE_TERMS:
            if sector_data.get(term) is None:
                missing.append(f"sectors.{sector}.{term}")
    return missing


def first_blocking_layer(data_key_hits: dict[str, list[str]], selected_de: dict[str, Any]) -> str:
    selected_de_constructed = selected_de.get("verdict", {}).get("selected_D_E_constructed")
    if selected_de_constructed is not True:
        return "selected_operator_source"
    if not data_key_hits["operator_slots"]:
        return "finite_D_E_operator_slots"
    if not data_key_hits["spectral_slots"]:
        return "finite_Riesz_spectral_slots"
    if not data_key_hits["green_slots"]:
        return "finite_reduced_Green_slots"
    if not data_key_hits["dotd_response_slots"]:
        return "finite_dotD_response_slots"
    return "primitive_C1_overlap_contractions"


def build_report() -> dict[str, Any]:
    selected_de = load_json("iwasawa_selected_de_construction_attempt_certificate.json")
    spectral_template = load_json("iwasawa_spectral_galerkin_data.template.json")
    cohomology_template = load_json("iwasawa_selected_cohomology_data.template.json")
    c1_template = load_json("selected_c1_response_data_certificate.template.json")
    primitive_template = load_json("selected_c1_primitive_contractions.template.json")
    yukawa_template = load_json("yukawa_overlap_kernel_certificate.template.json")
    rg_template = load_json("flavor_rg_matching_certificate.template.json")
    full_sm = load_json("selected_full_sm_data_theorem_attempt_certificate.json")

    data_key_hits = scan_data_key_files()
    primitive_missing_paths = primitive_missing(primitive_template)
    selected_de_routes = selected_de.get("route_evaluation", {})
    first_blocker = first_blocking_layer(data_key_hits, selected_de)

    missing_validator_layers = {
        "operator_slots_Q_u_d_L_e_N_H": not bool(data_key_hits["operator_slots"]),
        "spectral_slots_Q_u_d_L_e_N_H": not bool(data_key_hits["spectral_slots"]),
        "green_slots_Q_u_d_L_e_N_H": not bool(data_key_hits["green_slots"]),
        "dotd_response_slots_Q_u_d_L_e_N_H": not bool(data_key_hits["dotd_response_slots"]),
    }

    report = {
        "calculation": "SelectedMissingDataCalculation",
        "status": "SELECTED_DATA_CALCULATION_BLOCKED_BY_ABSENT_SELECTED_OPERATOR_SOURCE",
        "first_blocking_layer": first_blocker,
        "selected_D_E_constructed": selected_de.get("verdict", {}).get("selected_D_E_constructed"),
        "selected_D_E_routes": {
            key: {
                "status": value.get("status"),
                "reason": value.get("reason"),
            }
            for key, value in selected_de_routes.items()
        },
        "filled_selected_slot_data_found": data_key_hits,
        "missing_validator_layers": missing_validator_layers,
        "null_counts": {
            "iwasawa_spectral_galerkin_data": len(null_paths(spectral_template)),
            "iwasawa_selected_cohomology_data": len(null_paths(cohomology_template)),
            "selected_c1_response_data": len(null_paths(c1_template)),
            "selected_c1_primitive_contractions": len(primitive_missing_paths),
            "yukawa_overlap_kernel": len(null_paths(yukawa_template)),
            "flavor_rg_matching": len(null_paths(rg_template)),
        },
        "false_success_gate_counts": {
            "iwasawa_spectral_galerkin_data": len(false_paths(spectral_template.get("success_gates", {}))),
            "iwasawa_selected_cohomology_data": len(false_paths(cohomology_template.get("success_gates", {}))),
        },
        "missing_primitive_contractions": primitive_missing_paths,
        "minimal_new_selected_data_to_compute_c1": [
            "one selected D_E source: corrected non-invariant A^(0,1), typed monad/Cech data, or direct HYM/Strominger solve",
            "finite basis B_N and Gram/stiffness matrices for Q,u,d,L,e,N,H",
            "validated Riesz projectors and complement gaps for Q,u,d,L,e,N,H",
            "validated reduced Green operators for Q,u,d,L,e,N,H",
            "selected dotD_alpha1 matrices and horizontal responses for Q,u,d,L,e,N,H",
            "the 24 selected primitive 3x3 C1 contraction matrices",
        ],
        "minimal_new_selected_data_to_compute_full_sm": full_sm.get("missing_selected_inputs", {}),
        "rejected_shortcuts": {
            "diagnostic_h1_three_candidate": "pipeline test only, not selected D_E",
            "rank_one_E33_seed": "closed tree seed only, not full sector-resolved matrices",
            "execution_ii_benchmarks": "benchmark/comparison data, not selected no-proxy inputs",
            "observed_masses_mixings": "comparison targets only",
        },
        "can_compute_now": {
            "terminal_q79_exact_charge_branch": True,
            "CKM_phase_bridge_from_q79": True,
            "rank_one_tree_seed": True,
            "finite_C1_assembly_formula": True,
            "actual_selected_C1_matrices": False,
            "actual_selected_Yukawa_matrices": False,
            "full_SM_closure": False,
        },
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-report",
        type=Path,
        help="optional path for writing the JSON report",
    )
    args = parser.parse_args()

    report = build_report()
    encoded = json.dumps(report, indent=2, sort_keys=True)
    if args.write_report is not None:
        target = args.write_report
        if not target.is_absolute():
            target = ROOT / target
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
