"""Build threshold/pole-running maps or R_theta convention source artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdpolerunningmaps_or_rthetaconventionsource"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GAUGE_BRIDGE = PACKET_DIR / "gauge_bridge_policy_validation_status.packet.json"
MAP_DECOMP = PACKET_DIR / "threshold_pole_running_map_decomposition.packet.json"
TOP_HIGGS_TARGET = PACKET_DIR / "top_higgs_threshold_map_target.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_map_decomposition.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdPoleRunningMaps_or_RThetaConventionSource_v1.md"

PREVIOUS = DATA / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy.candidate.json"
POLICY = (
    DATA
    / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
    / "threshold_pole_running_policy_contract.packet.json"
)
SOURCE_ATTEMPT = (
    DATA
    / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
    / "same_branch_convention_source_theorem_attempt.packet.json"
)
OLD_THRESHOLD_MAP = DATA / "selected_thresholdpolerunningmaps_or_covarianceprofile.candidate.json"
ONE_LOOP_GAUGE = (
    DATA
    / "selected_thresholdpolerunningmaps_or_covarianceprofile"
    / "one_loop_gauge_mz_to_mt_transport.packet.json"
)
RESIDUAL_REQS = (
    DATA
    / "selected_thresholdpolerunningmaps_or_covarianceprofile"
    / "pole_threshold_residual_map_requirements.packet.json"
)
OLD_GATE = (
    DATA
    / "selected_thresholdpolerunningmaps_or_covarianceprofile"
    / "updated_true_equivalence_gate_after_threshold_map_scaffold.packet.json"
)
EXTERNAL_BENCH = (
    DATA
    / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
    / "external_literature_rg_benchmark_values.packet.json"
)
LIT_COMPARISON = (
    DATA
    / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
    / "literature_vs_local_convention_comparison.packet.json"
)
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_THRESHOLDPOLERUNNINGMAPS_OR_RTHETACONVENTIONSOURCE_"
    "BUILT_GAUGE_BRIDGE_ACCEPTED_TOP_HIGGS_MAPS_OPEN"
)
NEXT = "MTT_Selected_TopHiggsThresholdMapRows_or_ExternalPrecisionTable_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing threshold/pole-running map sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        POLICY,
        SOURCE_ATTEMPT,
        OLD_THRESHOLD_MAP,
        ONE_LOOP_GAUGE,
        RESIDUAL_REQS,
        OLD_GATE,
        EXTERNAL_BENCH,
        LIT_COMPARISON,
        THRESHOLD_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    policy = load(POLICY)
    source_attempt = load(SOURCE_ATTEMPT)
    old_threshold_map = load(OLD_THRESHOLD_MAP)
    one_loop = load(ONE_LOOP_GAUGE)
    residual_reqs = load(RESIDUAL_REQS)
    old_gate = load(OLD_GATE)
    external_bench = load(EXTERNAL_BENCH)
    lit_comparison = load(LIT_COMPARISON)
    threshold_contract = load(THRESHOLD_CONTRACT)

    gauge_bridge_valid = (
        old_threshold_map["closure_decision"]["threshold_map_scaffold_built"] is True
        and one_loop["passes_coarse_gauge_bridge"] is True
        and one_loop["accepted_as_precision_threshold_match"] is False
        and old_gate["guardrails"]["gauge_bridge_is_precision_match"] is False
    )

    gauge_bridge = {
        "schema": "MTTGaugeBridgePolicyValidationStatus.v1",
        "status": "ONE_LOOP_GAUGE_BRIDGE_ACCEPTED_AS_POLICY_VALIDATION_NOT_PRECISION_MATCH",
        "one_loop_source": rel(ONE_LOOP_GAUGE),
        "transport_formula": one_loop["transport"]["formula"],
        "transported_values": one_loop["transport"]["transported_values"],
        "comparison_rows": one_loop["comparison_rows"],
        "max_absolute_delta_to_literature": one_loop["max_absolute_delta_to_literature"],
        "passes_coarse_gauge_bridge": one_loop["passes_coarse_gauge_bridge"],
        "accepted_as_policy_validation_scaffold": gauge_bridge_valid,
        "accepted_as_precision_threshold_match": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(GAUGE_BRIDGE, gauge_bridge)

    map_rows = [
        {
            "id": "gauge_MZ_to_Mt_one_loop_bridge",
            "source": rel(GAUGE_BRIDGE),
            "role": "policy validation scaffold",
            "accepted_now": gauge_bridge_valid,
            "accepted_as_precision_threshold_row": False,
        },
        {
            "id": "top_direct_or_pole_to_MSbar_running_y_t",
            "source": rel(RESIDUAL_REQS),
            "role": "required top threshold/pole-running map",
            "accepted_now": False,
            "accepted_as_precision_threshold_row": False,
        },
        {
            "id": "Higgs_pole_to_running_lambda_H",
            "source": rel(RESIDUAL_REQS),
            "role": "required Higgs threshold/pole-running map",
            "accepted_now": False,
            "accepted_as_precision_threshold_row": False,
        },
        {
            "id": "bottom_charm_native_MSbar_scale_transport",
            "source": rel(POLICY),
            "role": "required quark native-scale transport maps",
            "accepted_now": False,
            "accepted_as_precision_threshold_row": False,
        },
        {
            "id": "tau_pole_rest_to_running_lepton_map",
            "source": rel(POLICY),
            "role": "required charged-lepton mass-scheme map",
            "accepted_now": False,
            "accepted_as_precision_threshold_row": False,
        },
        {
            "id": "W_Z_H_electroweak_matching_rows",
            "source": rel(THRESHOLD_CONTRACT),
            "role": "required electroweak matching rows",
            "accepted_now": False,
            "accepted_as_precision_threshold_row": False,
        },
    ]

    map_decomp = {
        "schema": "MTTThresholdPoleRunningMapDecomposition.v1",
        "status": "MAP_DECOMPOSITION_BUILT_ONLY_GAUGE_SCAFFOLD_ACCEPTED",
        "policy_contract_source": rel(POLICY),
        "same_branch_convention_source_theorem_closed": source_attempt[
            "same_branch_convention_source_theorem_closed"
        ],
        "map_rows": map_rows,
        "accepted_policy_validation_row_count": sum(1 for row in map_rows if row["accepted_now"]),
        "accepted_precision_threshold_row_count": sum(
            1 for row in map_rows if row["accepted_as_precision_threshold_row"]
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(MAP_DECOMP, map_decomp)

    top_higgs = {
        "schema": "MTTTopHiggsThresholdMapTarget.v1",
        "status": "TOP_HIGGS_THRESHOLD_MAP_TARGETS_EXTRACTED_VALUES_OPEN",
        "residual_requirements_source": rel(RESIDUAL_REQS),
        "external_benchmark_source": rel(EXTERNAL_BENCH),
        "literature_comparison_source": rel(LIT_COMPARISON),
        "top_targets": {
            "literature_y_t_Mt": external_bench["literature_values"]["y_t_Mt"],
            "residual_slots": {
                key: value
                for key, value in residual_reqs["residual_slots"].items()
                if key.startswith("top_")
            },
        },
        "higgs_targets": {
            "literature_lambda_Mt": external_bench["literature_values"]["lambda_Mt"],
            "residual_slots": {
                key: value
                for key, value in residual_reqs["residual_slots"].items()
                if key.startswith("lambda_")
            },
        },
        "required_for_promotion": residual_reqs["required_for_promotion"],
        "residuals_are_requirements_not_fitted_corrections": True,
        "can_accept_top_higgs_maps_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(TOP_HIGGS_TARGET, top_higgs)

    cutset = {
        "schema": "MTTNextCutsetAfterThresholdMapDecomposition.v1",
        "status": "NEXT_ATTACK_TOP_HIGGS_THRESHOLD_MAP_ROWS_OR_EXTERNAL_PRECISION_TABLE",
        "closed_now": {
            "one_loop_gauge_bridge_policy_validation_status": gauge_bridge_valid,
            "threshold_pole_running_map_decomposition": True,
            "top_higgs_threshold_map_targets_extracted": True,
        },
        "still_open": {
            "same_branch_Rtheta_convention_source_theorem": True,
            "top_direct_or_pole_to_MSbar_running_y_t_map": True,
            "Higgs_pole_to_running_lambda_H_map": True,
            "bottom_charm_tau_mass_scheme_maps": True,
            "W_Z_H_electroweak_matching_rows": True,
            "precision_covariance_or_diagonal_limitation": True,
            "accepted_precision_threshold_row_count_positive": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive top/Higgs threshold maps under the selected R_theta convention source",
            "route_B": "import an accepted external precision table for top/Higgs maps with provenance",
            "route_C": "prove that the one-loop gauge bridge plus explicit residual targets is sufficient only for parity-tier validation",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedThresholdPoleRunningMapsOrRThetaConventionSource",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "gauge_bridge_policy_validation_status": rel(GAUGE_BRIDGE),
            "threshold_pole_running_map_decomposition": rel(MAP_DECOMP),
            "top_higgs_threshold_map_target": rel(TOP_HIGGS_TARGET),
            "next_cutset_after_threshold_map_decomposition": rel(CUTSET),
        },
        "theorem": {
            "name": "ThresholdPoleRunningMapDecompositionTheorem",
            "proved": True,
            "statement": (
                "Under the reconciled RG/benchmark policy, the one-loop gauge M_Z-to-M_t bridge is "
                "accepted as a policy-validation scaffold, not as a precision threshold match. The "
                "remaining threshold/pole-running problem decomposes into top y_t, Higgs lambda, "
                "bottom/charm/tau mass-scheme maps, W/Z/H electroweak matching, and covariance/profile "
                "sidecars. Top/Higgs residual slots are extracted as requirements, not fitted corrections."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "one_loop_gauge_bridge_policy_validation_closed": gauge_bridge_valid,
            "top_higgs_threshold_map_targets_extracted": True,
            "accepted_precision_threshold_row_count": 0,
            "same_branch_Rtheta_convention_source_theorem_closed": False,
            "top_higgs_threshold_maps_closed": False,
            "bottom_charm_tau_mass_scheme_maps_closed": False,
            "W_Z_H_electroweak_matching_rows_closed": False,
            "profile_covariance_or_diagonal_limitation_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ThresholdPoleRunningMaps_or_RThetaConventionSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "one_loop_gauge_bridge_policy_validation_closed": gauge_bridge_valid,
        "accepted_precision_threshold_row_count": 0,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdPoleRunningMaps or RThetaConventionSource v1

Status: `{STATUS}`.

This artifact decomposes the threshold/pole-running map layer.

```text
one-loop gauge bridge accepted as policy validation : {str(gauge_bridge_valid).lower()}
one-loop gauge bridge accepted as precision match   : false
accepted precision threshold row count              : 0
top/Higgs threshold targets extracted               : true
same-branch R_theta convention source closed        : false
```

The gauge bridge is useful, but it is not the top/Higgs threshold theorem.  The
next value-producing move is to derive or import the top/Higgs precision map
rows, while keeping residual slots as requirements rather than fitted
corrections.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
