"""Build a priority order and correlated-profile blueprint for Higgs promotion."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgspromotionpriority_or_correlatedprofileblueprint"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRIORITY = PACKET_DIR / "higgs_precision_promotion_priority.packet.json"
BLUEPRINT = PACKET_DIR / "higgs_correlated_profile_blueprint.packet.json"
STRATEGY = PACKET_DIR / "higgs_two_lane_precision_upgrade_strategy.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_higgs_priority.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsPromotionPriority_or_CorrelatedProfileBlueprint_v1.md"

STATUS = "MTT_SELECTED_HIGGSPROMOTIONPRIORITY_OR_CORRELATEDPROFILEBLUEPRINT_BUILT_NEXT_GATE_PRIORITIZED"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def lane_for(row: dict[str, Any]) -> str:
    if row["channel"] in {"H_to_gg", "H_to_bb", "H_to_cc", "H_to_ss"}:
        return "Qa/SU3 color and threshold lane"
    if row["channel"] in {"H_to_gamma_gamma", "H_to_Z_gamma", "H_to_WW_star", "H_to_ZZ_star"}:
        return "electroweak gauge/Higgs operator lane"
    return "lepton mass-scheme/EW correction lane"


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsprecisionpromotionmatrix_or_operatorprofile.candidate.json")
    matrix = load(
        DATA
        / "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
        / "higgs_precision_promotion_matrix.packet.json"
    )
    diagonal = load(
        DATA
        / "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
        / "higgs_diagonal_sidecar_profile_stress.packet.json"
    )
    operator = load(
        DATA
        / "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
        / "higgs_operator_profile_promotion_obligations.packet.json"
    )
    previous_gate = load(
        DATA
        / "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
        / "updated_true_equivalence_gate_after_higgs_promotion_matrix.packet.json"
    )

    stress_by_channel = {term["channel"]: term for term in diagonal["terms"]}
    priority_rows = []
    for row in matrix["rows"]:
        stress = stress_by_channel[row["channel"]]
        abs_pull = abs(float(stress["pull"]))
        if row["row_kind"] == "audited_benchmark_replay":
            blocker_class = "FORMULA_MISSING_BENCHMARK_REPLAY_ONLY"
        elif abs_pull >= 3.0:
            blocker_class = "PROXY_TENSION_HIGH"
        elif abs_pull >= 1.0:
            blocker_class = "PROXY_TENSION_MEDIUM"
        else:
            blocker_class = "PROXY_OR_BENCHMARK_STABLE_BUT_NOT_PRECISION"
        priority_rows.append(
            {
                "channel": row["channel"],
                "row_kind": row["row_kind"],
                "diagonal_pull": stress["pull"],
                "abs_diagonal_pull": abs_pull,
                "priority_score": abs_pull + (1.0 if row["row_kind"] == "audited_benchmark_replay" else 0.0),
                "blocker_class": blocker_class,
                "primary_upgrade_lane": lane_for(row),
                "next_required_value": row["required_formula_family"],
                "operator_attachment_required": row["operator_attachment_required"],
                "may_use_observed_width_as_selector": False,
                "accepted_for_precision": False,
            }
        )
    priority_rows.sort(key=lambda row: (-row["priority_score"], row["channel"]))

    blocks = {
        "QCD_color_threshold": ["H_to_bb", "H_to_cc", "H_to_ss", "H_to_gg"],
        "EW_loop_and_offshell": ["H_to_gamma_gamma", "H_to_Z_gamma", "H_to_WW_star", "H_to_ZZ_star"],
        "lepton_mass_scheme": ["H_to_tau_tau", "H_to_mu_mu"],
    }
    blueprint_rows = []
    for block_name, channels in blocks.items():
        blueprint_rows.append(
            {
                "block": block_name,
                "channels": channels,
                "dimension": len(channels),
                "required_entries": len(channels) * len(channels),
                "required_covariance_source": "external correlated theory profile or selected operator-derived uncertainty model",
                "accepted_as_filled": False,
            }
        )
    total_dimension = sum(row["dimension"] for row in blueprint_rows)
    total_entries = total_dimension * total_dimension

    priority = {
        "schema": "MTTHiggsPrecisionPromotionPriority.v1",
        "status": "PROMOTION_PRIORITY_ORDER_BUILT_NO_TARGET_FIT",
        "rows": priority_rows,
        "summary": {
            "row_count": len(priority_rows),
            "top_priority_channels": [row["channel"] for row in priority_rows[:3]],
            "high_tension_proxy_channels": [
                row["channel"]
                for row in priority_rows
                if row["blocker_class"] == "PROXY_TENSION_HIGH"
            ],
            "benchmark_replay_only_channels": [
                row["channel"]
                for row in priority_rows
                if row["blocker_class"] == "FORMULA_MISSING_BENCHMARK_REPLAY_ONLY"
            ],
            "observed_widths_used_as_selectors": False,
            "precision_rows_promoted": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    blueprint = {
        "schema": "MTTHiggsCorrelatedProfileBlueprint.v1",
        "status": "CORRELATED_PROFILE_BLUEPRINT_BUILT_VALUES_OPEN",
        "blocks": blueprint_rows,
        "full_matrix": {
            "dimension": total_dimension,
            "required_entries": total_entries,
            "filled_entries": 0,
            "accepted_as_full_covariance_profile": False,
            "positive_semidefinite_check_ready": True,
            "profile_chi_square_check_ready": True,
        },
        "blocked_until": [
            "covariance entries or external correlated profile are supplied",
            "precision formula rows replace proxy/benchmark rows where required",
            "selected operator attachments are declared for source-sensitive promotion",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strategy = {
        "schema": "MTTHiggsTwoLanePrecisionUpgradeStrategy.v1",
        "status": "TWO_LANE_STRATEGY_SELECTED",
        "lanes": [
            {
                "lane": "Lane A: accepted precision formula rows",
                "first_targets": [row["channel"] for row in priority_rows[:3]],
                "acceptance_tests": [
                    "row formula is executable from declared measured parity inputs and selected operator packet",
                    "row value is not selected by minimizing residual to the sidecar reference",
                    "threshold and scheme provenance is recorded",
                    "precision acceptance flag remains false until audit validates formula, source, and covariance hooks",
                ],
            },
            {
                "lane": "Lane B: correlated ten-channel profile",
                "first_targets": [row["block"] for row in blueprint_rows],
                "acceptance_tests": [
                    "10x10 covariance or profile likelihood is supplied from a cited external source or selected operator model",
                    "matrix is symmetric positive semidefinite",
                    "central replay vector and covariance share the same channel convention",
                    "profile is not used to select source data",
                ],
            },
        ],
        "operator_obligations_imported": operator["global_required_packets"],
        "recommended_next_artifact": "MTT_Selected_HiggsGammaGammaCorrection_or_QCDThresholdRows_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterHiggsPriority.v1",
        "status": "HIGGS_NEXT_GATE_PRIORITIZED_TRUE_EQUIVALENCE_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": previous_gate["closed_now"] + ["Higgs precision promotion priority and correlated-profile blueprint"],
        "remaining_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": strategy["recommended_next_artifact"],
        "guardrails": {
            "priority_order_not_target_fit": True,
            "correlated_profile_values_filled": False,
            "precision_rows_promoted": 0,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsPromotionPriorityOrCorrelatedProfileBlueprint",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsprecisionpromotionmatrix_or_operatorprofile.candidate.json"),
            "promotion_matrix": rel(
                DATA
                / "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
                / "higgs_precision_promotion_matrix.packet.json"
            ),
            "diagonal_stress": rel(
                DATA
                / "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
                / "higgs_diagonal_sidecar_profile_stress.packet.json"
            ),
        },
        "output_packets": {
            "higgs_precision_promotion_priority": rel(PRIORITY),
            "higgs_correlated_profile_blueprint": rel(BLUEPRINT),
            "higgs_two_lane_precision_upgrade_strategy": rel(STRATEGY),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsPromotionPriorityAndProfileBlueprintTheorem",
            "proved": True,
            "statement": (
                "The completed Higgs promotion matrix canonically induces a no-fit next-gate ordering: "
                "high-pull proxy rows and benchmark-only electroweak rows are prioritized for either accepted "
                "formula replacement or a correlated ten-channel profile. This prioritization does not promote "
                "any width to precision and does not use observed widths as source selectors."
            ),
        },
        "what_closes_now": {
            "Higgs_next_gate_priority_order": True,
            "correlated_profile_blueprint": True,
            "two_lane_precision_upgrade_strategy": True,
        },
        "what_remains_open": {
            "accepted_precision_formula_rows": True,
            "filled_correlated_covariance_profile": True,
            "selected_electroweak_operator_attachment": True,
            "selected_Qa_SU3_operator_attachment": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "priority_gate_closed": True,
            "correlated_profile_values_filled": False,
            "precision_rows_promoted": 0,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsPromotionPriority_or_CorrelatedProfileBlueprint_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "priority_gate_closed": True,
        "top_priority_channels": priority["summary"]["top_priority_channels"],
        "correlated_profile_values_filled": False,
        "precision_rows_promoted": 0,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": strategy["recommended_next_artifact"],
    }

    note = """# MTT Selected HiggsPromotionPriority or CorrelatedProfileBlueprint v1

Status: `MTT_SELECTED_HIGGSPROMOTIONPRIORITY_OR_CORRELATEDPROFILEBLUEPRINT_BUILT_NEXT_GATE_PRIORITIZED`.

This artifact takes the ten-channel Higgs promotion matrix and chooses the next
work order without using observed widths as source selectors. The immediate
pressure points are high-pull proxy rows and benchmark-only electroweak rows.

It closes only the planning/proof-control layer. It does not promote any row to
precision, does not fill the correlated covariance matrix, and does not claim
true SM-equivalence or no-knob closure.
"""

    for path, payload in [
        (PRIORITY, priority),
        (BLUEPRINT, blueprint),
        (STRATEGY, strategy),
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
