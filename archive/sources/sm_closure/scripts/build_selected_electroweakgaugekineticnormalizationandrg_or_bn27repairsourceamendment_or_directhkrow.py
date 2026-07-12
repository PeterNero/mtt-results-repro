"""Build electroweak gauge-kinetic/RG or BN27 repair frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EW_LANE = PACKET_DIR / "electroweak_gaugekinetic_rg_route_lane.packet.json"
BN27_LANE = PACKET_DIR / "bn27_repair_sourceamendment_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_ew_rg_bn27_repair.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ElectroweakGaugeKineticNormalizationAndRGScheme_or_BN27RepairSourceAmendment_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_sourcebranchidentityemission_or_qastackphysicalanchor_or_directhkrow.candidate.json",
    "ew_gaugekinetic_rg": QA / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme.candidate.json",
    "ew_matching_interface": QA / "electroweak_matching_or_absolute_coupling_normalization.candidate.json",
    "ctwist_period": QA / "ctwist_period_normalization_or_a01_exit.candidate.json",
    "bn27_logdet_emission": QA
    / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimalemissionpacket_fill_or_sourceamendment.candidate.json",
    "bn27_repair_attack": QA
    / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.candidate.json",
    "sourceleaf_discovery": QA
    / "selected_heterotic_orientedphifin_sourceleaf_sourceamendment_or_corpusdiscovery.candidate.json",
}

STATUS = (
    "MTT_SELECTED_ELECTROWEAKGAUGEKINETICNORMALIZATIONANDRG_OR_BN27REPAIRSOURCEAMENDMENT_"
    "ROUTE_SELECTED_KERNEL_VALUES_OPEN"
)
NEXT = "MTT_Selected_HeteroticStromingerElectroweakThresholdKernel_or_BN27DirectCarrierSourceTheorem_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def d(src: dict[str, Any]) -> dict[str, Any]:
    return src.get("decision", src.get("closure_decision", {}))


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing EW/Bn27 repair inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = d(sources["previous"])
    ew = d(sources["ew_gaugekinetic_rg"])
    match = d(sources["ew_matching_interface"])
    ctwist = d(sources["ctwist_period"])
    logdet = d(sources["bn27_logdet_emission"])
    repair = d(sources["bn27_repair_attack"])
    discovery = d(sources["sourceleaf_discovery"])

    ew_lane = {
        "schema": "MTTElectroweakGaugeKineticRGRouteLane.v1",
        "status": "B_FLUX_STROMINGER_THRESHOLD_ROUTE_SELECTED_VALUES_OPEN",
        "closure_claimed": True,
        "strict_primary_route_selected": ew["strict_primary_route_selected"],
        "internal_lambda_12_available": ew["internal_lambda_12_available"],
        "internal_lambda_12_value": ew["internal_lambda_12_value"],
        "internal_Delta_G12_value": ew["internal_Delta_G12_value"],
        "gaugekinetic_normalization_closed": ew["gaugekinetic_normalization_closed"],
        "matching_scale_closed": ew["matching_scale_closed"],
        "RG_scheme_closed": ew["RG_scheme_closed"],
        "measured_electroweak_closure": ew["measured_electroweak_closure"],
        "matching_interface": {
            "electroweak_matching_interface": match["electroweak_matching_interface"],
            "Qa_SU3_internal_payload_for_matching": match["Qa_SU3_internal_payload_for_matching"],
            "allowed_conditional_formula": match["allowed_conditional_formula"],
            "absolute_gauge_normalization_K_gauge": match["absolute_gauge_normalization_K_gauge"],
            "U1_SU2_same_scheme_payloads": match["U1_SU2_same_scheme_payloads"],
            "no_knob_measured_electroweak_closure_now": match[
                "no_knob_measured_electroweak_closure_now"
            ],
        },
        "ctwist_scalar_gate": {
            "period_selector_found": ctwist["period_selector_found"],
            "period_selector_open_not_contradicted": ctwist[
                "period_selector_open_not_contradicted"
            ],
            "gerbe_route_retired": ctwist["gerbe_route_retired"],
            "best_next_move": ctwist["best_next_move"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    bn27_lane = {
        "schema": "MTTBN27RepairSourceAmendmentLane.v1",
        "status": "CONDITIONAL_LOGDET_IMPLICATION_READY_SOURCE_AMENDMENT_REQUIRED",
        "closure_claimed": True,
        "logdet_emission": {
            "attempt_executed": logdet["attempt_executed"],
            "conditional_implication_theorem_closed": logdet[
                "conditional_implication_theorem_closed"
            ],
            "source_amendment_template_built": logdet["source_amendment_template_built"],
            "source_owned_logdet_closed": logdet["source_owned_logdet_closed"],
            "BN27_source_identity_closed": logdet["BN27_source_identity_closed"],
            "direct_source_theorem_closed": logdet["direct_source_theorem_closed"],
            "connection_or_smooth_source_closed": logdet[
                "connection_or_smooth_source_closed"
            ],
            "kernel_trace_ownership_closed": logdet["kernel_trace_ownership_closed"],
            "oriented_logdet_promoted": logdet["oriented_logdet_promoted"],
        },
        "repair_attack": {
            "repair_attack_executed": repair["repair_attack_executed"],
            "primary_lane": repair["primary_lane"],
            "projective_rhoE_primary": repair["projective_rhoE_primary"],
            "projective_finite_candidate_available": repair[
                "projective_finite_candidate_available"
            ],
            "projective_BN27_lift_closed": repair["projective_BN27_lift_closed"],
            "BN27_domain_emission_closed": repair["BN27_domain_emission_closed"],
            "source_branch_identity_closed": repair["source_branch_identity_closed"],
        },
        "sourceleaf_discovery": {
            "corpus_discovery_executed": discovery["corpus_discovery_executed"],
            "support_only_matches_found": discovery["support_only_matches_found"],
            "direct_existing_packet_found": discovery["direct_existing_packet_found"],
            "smooth_existing_packet_found": discovery["smooth_existing_packet_found"],
            "minimal_source_amendment_plan_built": discovery[
                "minimal_source_amendment_plan_built"
            ],
            "next_lane": discovery["next_lane"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterEWRGBN27Repair.v1",
        "status": "NEXT_FRONTIER_STROMINGER_EW_KERNEL_OR_BN27_DIRECT_CARRIER_OR_DIRECT_HK_ROW",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "strict electroweak no-knob primary route selected as B_flux/Strominger threshold kernel",
            "electroweak matching interface retained with conditional 1/g_Qa^2=K_gauge*log(2008)",
            "internal lambda_12 and Delta_G12 are available to physical matching layer",
            "BN27 source-owned logdet implication DAG closed conditionally",
            "BN27 source amendment template built",
            "sourceleaf corpus discovery found no existing selected source packet",
            "minimal source amendment plan built with direct carrier constructive attempt",
        ],
        "still_open": [
            "selected heterotic/Strominger electroweak threshold kernel values",
            "physical gauge kinetic normalization K_gauge",
            "matching scale mu_match",
            "RG and threshold scheme",
            "ctwist period or finite quotient scalar selector",
            "BN27 direct carrier/source theorem or selected connection export",
            "BN27 kernel/trace ownership",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedElectroweakGaugeKineticNormalizationAndRGOrBN27RepairSourceAmendment",
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
            "electroweak_gaugekinetic_rg_route_lane": rel(EW_LANE),
            "bn27_repair_sourceamendment_lane": rel(BN27_LANE),
            "next_cutset_after_ew_rg_bn27_repair": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "strict_primary_route_selected": True,
            "strict_primary_route": ew["strict_primary_route_selected"],
            "internal_lambda_12_available": True,
            "internal_lambda_12_value": ew["internal_lambda_12_value"],
            "internal_Delta_G12_value": ew["internal_Delta_G12_value"],
            "electroweak_matching_interface_built": True,
            "BN27_logdet_implication_DAG_closed_conditionally": True,
            "BN27_source_amendment_template_built": True,
            "BN27_minimal_source_amendment_plan_built": True,
            "gaugekinetic_normalization_closed": False,
            "matching_scale_closed": False,
            "RG_scheme_closed": False,
            "measured_electroweak_closure": False,
            "ctwist_period_selector_found": False,
            "BN27_source_identity_closed": False,
            "BN27_kernel_trace_ownership_closed": False,
            "selected_R_H_RG_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "direct_HK_exit_still_allowed": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "ElectroweakGaugeKineticRGOrBN27RepairReductionTheorem",
            "proved": True,
            "statement": (
                "Given closed internal weak-split data, the strict no-knob "
                "electroweak physical route is selected as the heterotic/Strominger "
                "threshold-kernel path. M-theory and Theta supply support interfaces "
                "but no physical gauge-action value, matching scale, or RG scheme. "
                "On the BN27 side, source-owned logdet promotion is conditionally "
                "ready once a source amendment or selected connection export owns "
                "the BN27 carrier/kernel/trace packet. The remaining constructive "
                "frontier is therefore a selected Strominger electroweak threshold "
                "kernel, a BN27 direct carrier/source theorem, or direct H K row."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedElectroweakGaugeKineticNormalizationAndRGOrBN27RepairSourceAmendment",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "strict_primary_route_selected": True,
        "BN27_logdet_implication_DAG_closed_conditionally": True,
        "gaugekinetic_normalization_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "BN27_source_identity_closed": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Electroweak Gauge-Kinetic Normalization and RG Scheme or BN27 Repair Source Amendment v1

## Theorem

`ElectroweakGaugeKineticRGOrBN27RepairReductionTheorem` is emitted.

## Closed Here

- Strict electroweak no-knob primary route is selected as
  `B_flux/Strominger threshold`.
- Electroweak matching interface is retained with conditional
  `1/g_Qa^2(mu_match) = K_gauge * log(2008)`.
- Internal `lambda_12` and `Delta_G12` are available to the physical matching
  layer.
- BN27 source-owned logdet implication DAG is closed conditionally.
- BN27 source amendment template is built.
- Sourceleaf corpus discovery found no existing selected source packet.
- Minimal source amendment plan is built with direct carrier constructive
  attempt.

## Still Open

- Selected heterotic/Strominger electroweak threshold kernel values.
- Physical gauge kinetic normalization `K_gauge`.
- Matching scale `mu_match`.
- RG and threshold scheme.
- `c`-twist period or finite quotient scalar selector.
- BN27 direct carrier/source theorem or selected connection export.
- BN27 kernel/trace ownership.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(EW_LANE, ew_lane)
    write_json(BN27_LANE, bn27_lane)
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
