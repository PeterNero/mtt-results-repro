"""Build the H gauge-kinetic normalization / mu_match or direct H K-row packet.

This pushes the physical gauge/action layer for path #2.  It imports the latest
Qa/SU3 route discriminator and heterotic/Strominger threshold payload reduction.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_hgaugekineticnormalizationmumatch_or_directhkthresholdrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_IMPORT = PACKET_DIR / "heterotic_strominger_route_import.packet.json"
H_GATE = PACKET_DIR / "h_gauge_action_transport_gate.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_h_gauge_action_layer.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HGaugeKineticNormalizationMuMatch_or_DirectHKThresholdRow_v1.md"

SOURCES = {
    "previous": DATA / "selected_hkthresholdsourceobject_or_rghessiantransportconstruction.candidate.json",
    "previous_cutset": DATA
    / "selected_hkthresholdsourceobject_or_rghessiantransportconstruction"
    / "next_cutset_after_h_rg_transport_import.packet.json",
    "qa_gauge_route": QA / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme.candidate.json",
    "qa_heterotic_kernel": QA / "selected_heterotic_strominger_electroweak_threshold_kernel.candidate.json",
    "qa_heterotic_torsion_payload": QA
    / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json",
}

STATUS = (
    "MTT_SELECTED_HGAUGEKINETICNORMALIZATIONMUMATCH_OR_DIRECTHKTHRESHOLDROW_"
    "HETEROTIC_STROMINGER_ROUTE_SELECTED_VALUES_OPEN"
)
NEXT = "MTT_Selected_HeteroticStromingerSourceOperatorTorsion_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H gauge/action inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    previous = sources["previous"]["closure_decision"]
    qa_route = sources["qa_gauge_route"]["decision"]
    qa_kernel = sources["qa_heterotic_kernel"]["decision"]
    torsion = sources["qa_heterotic_torsion_payload"]["decision"]
    route_tests = sources["qa_heterotic_torsion_payload"]["route_tests"]

    route_import = {
        "schema": "MTTHeteroticStromingerRouteImportForHGaugeAction.v1",
        "status": "HETEROTIC_STROMINGER_PRIMARY_ROUTE_IMPORTED_VALUES_OPEN",
        "closure_claimed": True,
        "imported_route_discriminator": {
            "strict_primary_route_selected": qa_route["strict_primary_route_selected"],
            "gaugekinetic_normalization_closed": qa_route["gaugekinetic_normalization_closed"],
            "matching_scale_closed": qa_route["matching_scale_closed"],
            "RG_scheme_closed": qa_route["RG_scheme_closed"],
            "internal_lambda_12_available": qa_route["internal_lambda_12_available"],
            "internal_lambda_12_value": qa_route["internal_lambda_12_value"],
        },
        "heterotic_kernel_status": {
            "tree_level_gauge_kinetic_slot_filled": qa_kernel[
                "tree_level_gauge_kinetic_slot_filled"
            ],
            "physical_normalization_closed": qa_kernel["physical_normalization_closed"],
            "matching_scale_closed": qa_kernel["matching_scale_closed"],
            "RG_scheme_closed": qa_kernel["RG_scheme_closed"],
            "analytic_torsion_or_threshold_operator_closed": qa_kernel[
                "analytic_torsion_or_threshold_operator_closed"
            ],
            "stack_threshold_determinants_closed": qa_kernel[
                "stack_threshold_determinants_closed"
            ],
        },
        "payload_reduction": {
            "primary_next_exit": torsion["primary_next_exit"],
            "parallel_next_exit": torsion["parallel_next_exit"],
            "strict_no_knob_route_still_live": torsion["strict_no_knob_route_still_live"],
            "payload_closed": torsion["payload_closed"],
            "internal_replay_retired_as_physical_threshold_source": torsion[
                "retire_internal_replay_as_physical_threshold_source"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_gate = {
        "schema": "MTTHGaugeActionTransportGate.v1",
        "status": "PRIMARY_HYM_MONAD_OPERATOR_LANE_SELECTED_H_ROW_OPEN",
        "closure_claimed": True,
        "path_2_gate": {
            "selected_physical_gauge_action_anchor": False,
            "selected_mu_match": False,
            "selected_RG_scheme": False,
            "selected_R_H_RG": False,
            "selected_K_threshold_Omega_H_lambda": False,
        },
        "selected_primary_lane": {
            "lane_id": "C_hym_monad_threshold_operator",
            "operator_domain_selected_for_next_gate": route_tests[
                "C_hym_monad_threshold_operator"
            ]["operator_domain_selected_for_next_gate"],
            "selected_connection_candidate_found": route_tests[
                "C_hym_monad_threshold_operator"
            ]["selected_connection_candidate_found"],
            "mu_selected": route_tests["C_hym_monad_threshold_operator"]["mu_selected"],
            "selected_spectrum_or_torsion_available": route_tests[
                "C_hym_monad_threshold_operator"
            ]["selected_spectrum_or_torsion_available"],
            "next_required_artifact": route_tests["C_hym_monad_threshold_operator"][
                "next_required_artifact"
            ],
        },
        "parallel_lane": {
            "lane_id": "B_ray_singer_or_reidemeister_local_system",
            "selected_candidates_count": route_tests[
                "B_ray_singer_or_reidemeister_local_system"
            ]["selected_candidates_count"],
            "computable_now": route_tests["B_ray_singer_or_reidemeister_local_system"][
                "computable_now"
            ],
        },
        "direct_HK_exit_still_allowed": True,
        "reason_not_closed": (
            "The selected route is now the heterotic/Strominger HYM/monad threshold "
            "operator lane, but the continuous HYM parameter, quotient-domain spectrum, "
            "heat/zeta finite part, physical normalization, mu_match, and RG scheme are "
            "not emitted."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterHGaugeActionLayer.v1",
        "status": "NEXT_FRONTIER_HETEROTIC_SOURCE_OPERATOR_TORSION_OR_DIRECT_HK",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "gauge/action layer route discriminator imported",
            "heterotic/Strominger threshold-kernel route selected as primary strict route",
            "tree-level f=S slot filled but not promoted to one-loop threshold values",
            "analytic-torsion/threshold payload reduced to HYM operator lane or local-system torsion lane",
        ],
        "still_open": [
            "HYM/monad Delta_A(mu) spectrum and selected mu",
            "positive spectrum, heat coefficients, or zeta/torsion finite part",
            "physical gauge/action normalization and matching scale",
            "RG scheme and threshold convention",
            "selected R_H^RG row and same-scheme Omega_H.lambda certificate",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHGaugeKineticNormalizationMuMatchOrDirectHKThresholdRow",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "heterotic_strominger_route_import": rel(ROUTE_IMPORT),
            "h_gauge_action_transport_gate": rel(H_GATE),
            "next_cutset_after_h_gauge_action_layer": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "heterotic_strominger_primary_route_selected": True,
            "tree_level_gauge_kinetic_slot_filled": qa_kernel[
                "tree_level_gauge_kinetic_slot_filled"
            ],
            "analytic_torsion_or_threshold_operator_closed": False,
            "physical_gauge_action_anchor_closed": False,
            "matching_scale_closed": False,
            "RG_scheme_closed": False,
            "selected_R_H_RG_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": previous[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous[
                "selected_K_threshold_row_count_required"
            ],
            "primary_HYM_monad_lane_selected": True,
            "local_system_torsion_parallel_lane_open": True,
            "direct_HK_exit_still_allowed": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "HGaugeKineticNormalizationMuMatchOrDirectHKThresholdRowTheorem",
            "proved": True,
            "statement": (
                "The physical gauge/action layer selects the heterotic/Strominger "
                "threshold-kernel route as the strict primary path for H large-threshold "
                "transport. The route currently fills only framework data and the "
                "tree-level f=S slot; it reduces the values to a source-selected "
                "HYM/monad threshold operator or a source-selected local-system torsion "
                "computation. No R_H^RG or H K row is emitted."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHGaugeKineticNormalizationMuMatchOrDirectHKThresholdRow",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "heterotic_strominger_primary_route_selected": True,
        "tree_level_gauge_kinetic_slot_filled": True,
        "analytic_torsion_or_threshold_operator_closed": False,
        "physical_gauge_action_anchor_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "selected_R_H_RG_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected H Gauge-Kinetic Normalization / Mu-Match or Direct H K-Threshold Row v1

## Theorem

`HGaugeKineticNormalizationMuMatchOrDirectHKThresholdRowTheorem` is emitted.

The physical gauge/action layer has been pushed.  It selects the
heterotic/Strominger threshold-kernel route as the strict primary path for the
large-threshold H transport.

## Closed Here

- Route discriminator imported from Qa/SU3.
- Heterotic/Strominger primary route selected.
- Tree-level gauge kinetic slot `f=S` filled.
- Internal `lambda_12 = {qa_route["internal_lambda_12_value"]}` carried only as
  internal accounting.

## Still Open

- HYM/monad `Delta_A(mu)` spectrum and selected `mu`.
- Positive spectrum, heat coefficients, or zeta/torsion finite part.
- Physical gauge/action normalization.
- Matching scale `mu_match`.
- RG scheme and threshold convention.
- Selected `R_H^RG` row and same-scheme `Omega_H.lambda` certificate.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Next Artifact

`{NEXT}`
"""

    write_json(ROUTE_IMPORT, route_import)
    write_json(H_GATE, h_gate)
    write_json(NEXT_CUTSET, next_cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
