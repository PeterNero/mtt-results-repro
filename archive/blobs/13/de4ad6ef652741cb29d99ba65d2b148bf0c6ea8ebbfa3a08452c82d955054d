"""Audit the shared-knob cross-encoding ledger."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "shared_knob_cross_encoding_ledger_certificate.json"
PAPER = ROOT / "Shared_Knob_Cross_Encoding_Ledger_for_MTT_MMT_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def knob_map(cert: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {knob["id"]: knob for knob in cert.get("shared_knobs", [])}


def main() -> None:
    cert = load_json(CERT)
    knobs = knob_map(cert)
    paper = read(PAPER)

    z64 = load_json(CERT_DIR / "z64_exact_branch_certificate.json")
    z7 = load_json(CERT_DIR / "z7_fuyau_mukai_charge_sector_certificate.json")
    theta = load_json(CERT_DIR / "theta_flavor_kernel_skeleton_certificate.json")
    seed = load_json(CERT_DIR / "iwasawa_rank_one_yukawa_seed_certificate.json")
    higgs = load_json(CERT_DIR / "single_higgs_channel_projection_certificate.json")
    weights = load_json(CERT_DIR / "selected_channel_weight_extraction_protocol_certificate.json")
    c1 = load_json(CERT_DIR / "c1_iwasawa_rplus_support_certificate.json")
    c1_reduce = load_json(CERT_DIR / "c1_finite_response_matrix_reduction_certificate.json")

    expected_ids = {
        "q79_cp_character",
        "z64_exact_central_circle_carrier",
        "z7_mukai_fuyau_charge_block",
        "theta_overlap_scaffold",
        "iwasawa_rank_one_yukawa_seed",
        "single_higgs_projection",
        "channel_weight_formula",
        "c1_alpha1_curvature_driver",
        "finite_c1_response_assembly",
    }

    q79 = knobs.get("q79_cp_character", {}).get("selected_data", {})
    z64_data = knobs.get("z64_exact_central_circle_carrier", {}).get("selected_data", {})
    z7_data = knobs.get("z7_mukai_fuyau_charge_block", {}).get("selected_data", {})
    theta_data = knobs.get("theta_overlap_scaffold", {}).get("selected_data", {})
    seed_data = knobs.get("iwasawa_rank_one_yukawa_seed", {}).get("selected_data", {})
    higgs_data = knobs.get("single_higgs_projection", {}).get("selected_data", {})
    weight_data = knobs.get("channel_weight_formula", {}).get("selected_data", {})
    c1_data = knobs.get("c1_alpha1_curvature_driver", {}).get("selected_data", {})
    c1_reduce_data = knobs.get("finite_c1_response_assembly", {}).get("selected_data", {})

    all_have_sources = all(knob.get("source_certificates") for knob in knobs.values())
    all_have_multiple_roles = all(len(knob.get("cross_encoding_roles", {})) >= 3 for knob in knobs.values())
    all_have_open_observable_lists = all("open_observables" in knob for knob in knobs.values())

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "SHARED_KNOB_LEDGER_FORMULATED_CROSS_ENCODINGS_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "expected knob ids",
            "PASS" if set(knobs) == expected_ids else "FAIL",
            ", ".join(sorted(knobs)),
        ),
        Gate(
            "source certificates recorded",
            "PASS" if all_have_sources else "FAIL",
            "every knob cites at least one source certificate",
        ),
        Gate(
            "cross-encoding roles recorded",
            "PASS" if all_have_multiple_roles else "FAIL",
            "each knob has at least three encoding roles",
        ),
        Gate(
            "open observables separated",
            "PASS" if all_have_open_observable_lists else "FAIL",
            "no shared knob silently closes target observables",
        ),
        Gate(
            "q79 agrees with terminal inputs",
            "PASS"
            if q79.get("q_mod_448") == 79
            and z64.get("conclusion", {}).get("q_mod_448") == 79
            and z7.get("conclusion", {}).get("q_mod_448") == 79
            and theta.get("cp_character", {}).get("q_mod_448") == 79
            else "FAIL",
            f"q={q79.get('q_mod_448')}",
        ),
        Gate(
            "Z64 carrier agrees",
            "PASS"
            if z64_data.get("primitive_shift_order") == 64
            and z64_data.get("tower_spectral_gap") == 9
            and z64.get("carrier", {}).get("verified_order") == 64
            and z64.get("hessian_block", {}).get("spectral_gap") == 9
            else "FAIL",
            str(z64_data),
        ),
        Gate(
            "Z7 Mukai block agrees",
            "PASS"
            if z7_data.get("determinant") == 7
            and z7.get("charge_data", {}).get("determinant") == 7
            and z7.get("charge_data", {}).get("verified_snf") == [7]
            else "FAIL",
            str(z7_data),
        ),
        Gate(
            "Theta scaffold agrees",
            "PASS"
            if theta_data.get("mu_theta_TeV") == 5.0
            and theta_data.get("I2_over_I1") == 0.56
            and theta_data.get("I3_over_I1") == 0.229
            and theta.get("gap", {}).get("lambda_star_floor") == 0.25
            else "FAIL",
            str(theta_data),
        ),
        Gate(
            "Iwasawa seed agrees",
            "PASS"
            if seed_data.get("lambda_123_after_rephasing") == 1
            and seed_data.get("rank") == 1
            and seed.get("tree_level_seed", {}).get("rank") == 1
            else "FAIL",
            str(seed_data),
        ),
        Gate(
            "single Higgs projection agrees",
            "PASS"
            if higgs_data.get("H_u") == "H"
            and higgs_data.get("H_d") == "H^dagger"
            and higgs.get("higgs_doublet_embedding", {}).get("H_u") == "H"
            and higgs.get("higgs_doublet_embedding", {}).get("H_d") == "H^dagger"
            else "FAIL",
            str(higgs_data),
        ),
        Gate(
            "channel formula agrees",
            "PASS"
            if "exp(-S" in weight_data.get("formula", "")
            and "exp(-S" in weights.get("weight_formula", {}).get("channel_weight", "")
            and weight_data.get("channels_per_sector") == 7
            else "FAIL",
            weight_data.get("formula", ""),
        ),
        Gate(
            "C1 alpha1 driver agrees",
            "PASS"
            if "alpha_1" in c1_data.get("formula", "")
            and c1_data.get("alpha_2_component") == 0
            and c1_data.get("alpha_3_component") == 0
            and c1.get("rplus_support", {}).get("alpha_2_component") == 0
            and c1.get("rplus_support", {}).get("alpha_3_component") == 0
            else "FAIL",
            c1_data.get("formula", ""),
        ),
        Gate(
            "finite C1 reduction agrees",
            "PASS"
            if "B_s,Theta" in c1_reduce_data.get("formula", "")
            and c1_reduce_data.get("primitive_blocks_per_sector") == 6
            and "B_s,Theta" in c1_reduce.get("finite_reduction_theorem", {}).get("matrix_formula", "")
            else "FAIL",
            c1_reduce_data.get("formula", ""),
        ),
        Gate(
            "discipline forbids overclaim",
            "PASS"
            if cert.get("discipline", {}).get("claims_full_sm_closure") is False
            and cert.get("discipline", {}).get("uses_observed_masses_or_mixings_as_inputs") is False
            and cert.get("discipline", {}).get("allows_shared_knob_to_override_open_encoding_data") is False
            else "FAIL",
            str(cert.get("discipline", {})),
        ),
        Gate(
            "paper records ledger",
            "PASS"
            if "Shared Knob Ledger" in paper
            and "selected shared data" in paper
            and "encoding-specific open observables" in paper
            else "FAIL",
            "ledger paper is written",
        ),
    ]

    print("Shared knob cross-encoding ledger audit")
    print("=======================================")
    print()
    print(f"knob_count={len(knobs)}")
    print(f"encoding_domains={', '.join(cert.get('encoding_domains', []))}")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
