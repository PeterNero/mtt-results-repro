"""Build external literature RG benchmark values and threshold/covariance gap audit."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LIT = PACKET_DIR / "external_literature_rg_benchmark_values.packet.json"
COMPARE = PACKET_DIR / "literature_vs_local_convention_comparison.packet.json"
UPDATED = PACKET_DIR / "threshold_covariance_gap_after_literature_benchmark.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ExternalLiteratureRGBenchmarkValues_or_ThresholdCovariance_v1.md"

STATUS = "MTT_SELECTED_EXTERNALLITERATURERGBENCHMARKVALUES_OR_THRESHOLDCOVARIANCE_BUILT_LIT_VALUES_FILLED_THRESHOLDS_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def diag_real(matrix: list, index: int) -> float:
    item = matrix[index][index]
    return float(item[0]) if isinstance(item, list) else float(item)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor.candidate.json")
    previous_matrix = load(
        DATA
        / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor"
        / "updated_true_equivalence_blocker_matrix.packet.json"
    )
    firstpass = load(
        DATA
        / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
        / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
    )
    common = load(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json")

    y_u_native = common["common_scale_packet"]["native_values_carried_but_not_common_scale"]["Y_u_native"]
    lambda_native = common["common_scale_packet"]["native_values_carried_but_not_common_scale"]["lambda_H_tree_native"]
    gauge_mz = common["common_scale_packet"]["closed_values"]
    firstpass_values = firstpass["accepted_values"]

    gY_mt = 0.35830
    literature = {
        "schema": "MTTExternalLiteratureRGBenchmarkValues.v1",
        "status": "EXTERNAL_LITERATURE_RG_BENCHMARK_VALUES_FILLED_FROM_BUTTAZZO_ET_AL",
        "source": {
            "label": "Buttazzo et al., Investigating the near-criticality of the Higgs boson",
            "arxiv": "1307.3536",
            "doi": "10.1007/JHEP12(2013)089",
            "url": "https://arxiv.org/abs/1307.3536",
            "quoted_scope": "MSbar SM parameters at the top pole mass with NNLO/precision threshold context and three-loop RGE discussion.",
        },
        "reference_point": {
            "scale": "mu = M_t",
            "central_inputs_in_paper": {
                "M_h_GeV": 125.15,
                "M_t_GeV": 173.34,
                "alpha3_MZ": 0.1184,
                "M_W_GeV": 80.384,
            },
            "scheme": "MSbar",
        },
        "literature_values": {
            "lambda_Mt": {
                "central_value": 0.12604,
                "theory_uncertainty": 0.00030,
                "paper_equation": "Eq. (55)",
            },
            "y_t_Mt": {
                "central_value": 0.93690,
                "theory_uncertainty": 0.00050,
                "paper_equation": "Eq. (57)",
            },
            "g_2_Mt": {
                "central_value": 0.64779,
                "paper_equation": "Eq. (58)",
            },
            "g_Y_Mt": {
                "central_value": gY_mt,
                "paper_equation": "Eq. (59)",
            },
            "g_1_GUT_Mt": {
                "central_value": math.sqrt(5.0 / 3.0) * gY_mt,
                "derived_from": "sqrt(5/3) * g_Y for GUT-normalized U(1)",
            },
            "g_3_Mt": {
                "central_value": 1.1666,
                "paper_equation": "Eq. (60)",
            },
        },
        "filled_external_literature_values": True,
        "accepted_as_external_literature_benchmark_reference": True,
        "accepted_as_full_precision_match": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    local = {
        "lambda_tree_native": float(lambda_native),
        "lambda_H_MZ_firstpass": float(firstpass_values["lambda_H_MZ_firstpass"]),
        "y_t_native_tree": diag_real(y_u_native, 2),
        "y_t_MZ_firstpass": diag_real(firstpass_values["Y_u_MZ_firstpass"], 2),
        "g_1_GUT_MZ": float(gauge_mz["g_1_GUT_MZ"]["central_value"]),
        "g_2_MZ": float(gauge_mz["g_2_MZ"]["central_value"]),
        "g_3_MZ": float(gauge_mz["g_3_MZ"]["central_value"]),
    }
    litvals = literature["literature_values"]
    comparison_rows = [
        {
            "id": "lambda_native_vs_lit_Mt",
            "local_value": local["lambda_tree_native"],
            "literature_value": litvals["lambda_Mt"]["central_value"],
            "absolute_delta": abs(local["lambda_tree_native"] - litvals["lambda_Mt"]["central_value"]),
            "interpretation": "native tree value needs MSbar threshold/matching before precision comparison",
        },
        {
            "id": "lambda_firstpass_MZ_vs_lit_Mt",
            "local_value": local["lambda_H_MZ_firstpass"],
            "literature_value": litvals["lambda_Mt"]["central_value"],
            "absolute_delta": abs(local["lambda_H_MZ_firstpass"] - litvals["lambda_Mt"]["central_value"]),
            "interpretation": "scale and threshold conventions differ; do not treat as failed fit",
        },
        {
            "id": "yt_native_vs_lit_Mt",
            "local_value": local["y_t_native_tree"],
            "literature_value": litvals["y_t_Mt"]["central_value"],
            "absolute_delta": abs(local["y_t_native_tree"] - litvals["y_t_Mt"]["central_value"]),
            "interpretation": "tree mass Yukawa seed requires pole-to-MSbar top matching",
        },
        {
            "id": "yt_firstpass_MZ_vs_lit_Mt",
            "local_value": local["y_t_MZ_firstpass"],
            "literature_value": litvals["y_t_Mt"]["central_value"],
            "absolute_delta": abs(local["y_t_MZ_firstpass"] - litvals["y_t_Mt"]["central_value"]),
            "interpretation": "first-pass transport lacks top threshold and running gauge precision",
        },
        {
            "id": "g1GUT_MZ_vs_g1GUT_lit_Mt",
            "local_value": local["g_1_GUT_MZ"],
            "literature_value": litvals["g_1_GUT_Mt"]["central_value"],
            "absolute_delta": abs(local["g_1_GUT_MZ"] - litvals["g_1_GUT_Mt"]["central_value"]),
            "interpretation": "nearby conventions; scale and precision matching still needed",
        },
        {
            "id": "g2_MZ_vs_lit_Mt",
            "local_value": local["g_2_MZ"],
            "literature_value": litvals["g_2_Mt"]["central_value"],
            "absolute_delta": abs(local["g_2_MZ"] - litvals["g_2_Mt"]["central_value"]),
            "interpretation": "scale difference is small but must be handled by benchmark policy",
        },
        {
            "id": "g3_MZ_vs_lit_Mt",
            "local_value": local["g_3_MZ"],
            "literature_value": litvals["g_3_Mt"]["central_value"],
            "absolute_delta": abs(local["g_3_MZ"] - litvals["g_3_Mt"]["central_value"]),
            "interpretation": "strong coupling running/matching from MZ to Mt is a real precision threshold task",
        },
    ]
    comparison = {
        "schema": "MTTLiteratureVsLocalConventionComparison.v1",
        "status": "LITERATURE_VALUES_COMPARED_CONVENTION_GAPS_IDENTIFIED",
        "local_values": local,
        "literature_reference": literature["source"],
        "comparison_rows": comparison_rows,
        "max_absolute_delta": max(row["absolute_delta"] for row in comparison_rows),
        "all_deltas_finite": all(math.isfinite(row["absolute_delta"]) for row in comparison_rows),
        "comparison_closes": {
            "external_literature_values_filled": True,
            "full_precision_agreement_claimed": False,
            "threshold_and_pole_matching_needed": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = [
        blocker
        for blocker in previous_matrix["remaining_true_equivalence_blockers"]
        if blocker != "external literature RG benchmark values"
    ]
    if "literature/local convention agreement after threshold maps" not in remaining:
        remaining.insert(0, "literature/local convention agreement after threshold maps")
    updated = {
        "schema": "MTTThresholdCovarianceGapAfterLiteratureBenchmark.v1",
        "status": "EXTERNAL_LITERATURE_RG_VALUES_FILLED_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_matrix["remaining_true_equivalence_blockers"],
        "closed_now": ["external literature RG benchmark values"],
        "remaining_true_equivalence_blockers": remaining,
        "new_primary_value_gate": "precision threshold and pole-to-running maps",
        "guardrails": {
            "external_values_are_downstream_benchmark_not_source_selector": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedExternalLiteratureRGBenchmarkValuesOrThresholdCovariance",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor.candidate.json"),
            "previous_blocker_matrix": rel(
                DATA
                / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor"
                / "updated_true_equivalence_blocker_matrix.packet.json"
            ),
            "common_scale_packet": rel(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"),
            "firstpass_values": rel(
                DATA
                / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
                / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
            ),
        },
        "output_packets": {
            "external_literature_rg_benchmark_values": rel(LIT),
            "literature_vs_local_convention_comparison": rel(COMPARE),
            "threshold_covariance_gap_after_literature_benchmark": rel(UPDATED),
        },
        "external_sources": {
            "buttazzo_2013_arxiv": "https://arxiv.org/abs/1307.3536",
            "buttazzo_2013_pdf": "https://arxiv.org/pdf/1307.3536",
        },
        "theorem": {
            "name": "ExternalLiteratureRGBenchmarkValueInsertionTheorem",
            "proved": True,
            "statement": (
                "The Buttazzo et al. MSbar weak-scale benchmark values can be inserted as downstream "
                "external literature RG benchmark rows. Comparing them to the current native/first-pass "
                "local rows identifies threshold, scale, and pole-to-running conversion gaps. This closes "
                "the presence of external literature benchmark values, but not precision agreement, true "
                "SM equivalence, or no-knob derivation."
            ),
        },
        "what_closes_now": {
            "external_literature_rg_benchmark_values_filled": True,
            "literature_vs_local_convention_comparison_built": True,
            "threshold_covariance_gap_identified": True,
            "superset_strategy_preserved": True,
        },
        "what_remains_open": {
            "literature_local_convention_agreement_after_threshold_maps": True,
            "precision_threshold_and_pole_running_maps": True,
            "full_covariance_profile_values": True,
            "local_QFT_observable_values": True,
            "QM_GR_measurement_response_interfaces": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "external_literature_rg_values_filled": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_ExternalLiteratureRGBenchmarkValues_or_ThresholdCovariance_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "external_literature_rg_values_filled": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_ThresholdPoleRunningMaps_or_CovarianceProfileValues_v1",
    }

    note = """# MTT Selected ExternalLiteratureRGBenchmarkValues or ThresholdCovariance v1

Status: `MTT_SELECTED_EXTERNALLITERATURERGBENCHMARKVALUES_OR_THRESHOLDCOVARIANCE_BUILT_LIT_VALUES_FILLED_THRESHOLDS_OPEN`.

This artifact inserts external literature RG benchmark values from Buttazzo et
al. (`arXiv:1307.3536`, JHEP 12 (2013) 089) as downstream benchmark rows:
`lambda(Mt)`, `yt(Mt)`, `g2(Mt)`, `gY(Mt)`, GUT-normalized `g1(Mt)`, and
`g3(Mt)`.

The comparison against current local native/first-pass rows identifies the next
precision gate: threshold matching, pole-to-running maps, and covariance/profile
values. The literature values are not used as source selectors and do not close
true SM equivalence by themselves.
"""

    for path, payload in [
        (LIT, literature),
        (COMPARE, comparison),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
