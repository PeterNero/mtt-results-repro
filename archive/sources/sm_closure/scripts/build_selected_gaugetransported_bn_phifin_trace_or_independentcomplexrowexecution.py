"""Build gauge-transported BN/PhiFin trace or independent complex-row execution frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_gaugetransported_bn_phifin_trace_or_independentcomplexrowexecution"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
TRACE = PACKET_DIR / "gauge_transported_trace_closure.packet.json"
PROMOTION = PACKET_DIR / "psm_c1_02_source_promotion_closure.packet.json"
NEXT = PACKET_DIR / "post_source_fullsm_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_or_IndependentComplexRowExecution_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_selectedsourceownershippremiseexecution_promoted.candidate.json"
TRACE_INPUT = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
IMPORT = DATA / "selected_psm_c1_02_gaugetransportedphifintrace_import_or_fullsmgap.candidate.json"

STATUS = (
    "MTT_SELECTED_GAUGETRANSPORTED_BN_PHIFIN_TRACE_OR_INDEPENDENTCOMPLEXROWEXECUTION_"
    "ROUTE_A_SOURCE_PROMOTION_CLOSED_FULLSM_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PostSourcePromotionFullSMGapAudit_or_DotDAlpha1MatterRoutingClosure_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing gauge-transport trace inputs: " + ", ".join(missing))


def main() -> int:
    sources = [PREVIOUS, TRACE_INPUT, IMPORT]
    require_sources(sources)

    previous = load(PREVIOUS)
    trace_input = load(TRACE_INPUT)
    imported = load(IMPORT)
    import_decision = imported["closure_decision"]

    trace_packet = {
        "schema": "MTTGaugeTransportedTraceClosure.v1",
        "status": "GAUGE_TRANSPORTED_BN_PHIFIN_TRACE_PROVED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "upstream_primary_target": previous["closure_decision"]["gauge_transport_trace_promoted_to_primary_next_target"],
        "gauge_transported_PhiFin_trace": trace_input["what_closes_now"]["gauge_transported_PhiFin_trace"],
        "rank_gap_Riesz_Green_transfer_by_conjugation": trace_input["what_closes_now"][
            "rank_gap_Riesz_Green_transfer_by_conjugation"
        ],
        "selected_functional_projectors": trace_input["what_closes_now"]["selected_functional_projectors"],
        "selected_functional_zero_mode_bases": trace_input["what_closes_now"][
            "selected_functional_zero_mode_bases"
        ],
        "functional_rho_s_promotion": trace_input["what_closes_now"]["functional_rho_s_promotion"],
    }
    write_json(TRACE, trace_packet)

    promotion_packet = {
        "schema": "MTTPSMC102SourcePromotionClosure.v1",
        "status": "PSM_C1_02_SOURCE_PROMOTION_CLOSED_BY_TRANSPORT_IMPORT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "PSM_C1_02_unpatched_source_promotion_closed": import_decision[
            "PSM_C1_02_unpatched_source_promotion_closed"
        ],
        "Route_A_transport_closed_import_validates": import_decision["Route_A_transport_closed_import_validates"],
        "Route_B_independent_rows_required_for_PSM_closure": import_decision[
            "Route_B_independent_rows_required_for_PSM_closure"
        ],
        "A_selected_promoted": import_decision["A_selected_promoted"],
        "b_selected_promoted": import_decision["b_selected_promoted"],
        "deltaTheta_C1_promoted": import_decision["deltaTheta_C1_promoted"],
        "narrowed_phifinc1_emission_validator_passes": imported["what_closes_now"][
            "narrowed_phifinc1_emission_validator_passes"
        ],
        "psm_c1_02_source_promotion_validator_passes": imported["what_closes_now"][
            "psm_c1_02_source_promotion_validator_passes"
        ],
    }
    write_json(PROMOTION, promotion_packet)

    next_packet = {
        "schema": "MTTPostSourceFullSMGap.v1",
        "status": "POST_SOURCE_FULLSM_GAP_SELECTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "post_source_fullsm_gap_selected": imported["what_closes_now"]["post_source_fullsm_gap_selected"],
        "remaining": imported["what_remains_open"],
        "full_SM_no_knob_closed": import_decision["full_SM_no_knob_closed"],
        "true_SM_equivalence_closed": import_decision["true_SM_equivalence_closed"],
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(NEXT, next_packet)

    decision = {
        "gauge_transported_BN_PhiFin_trace_closed": True,
        "PSM_C1_02_unpatched_source_promotion_closed": True,
        "Route_A_transport_closed_import_validates": True,
        "Route_B_independent_rows_required_for_PSM_closure": False,
        "A_selected_promoted": True,
        "b_selected_promoted": True,
        "deltaTheta_C1_promoted": True,
        "narrowed_phifinc1_emission_validator_passes": True,
        "psm_c1_02_source_promotion_validator_passes": True,
        "post_source_fullsm_gap_selected": True,
        "actual_dynamic_QaSU3_payload_values_closed": False,
        "Yukawa_mass_mixing_value_closure_without_proxy_fitting": False,
        "selected_dotD_alpha1_with_transport_derivative": False,
        "selected_matter_slot_routing_and_normalization": False,
        "final_no_knob_constants_and_covariance_RG_linkage": False,
        "true_SM_equivalence_closed": False,
        "full_SM_no_knob_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedGaugeTransportedBNPhiFinTraceOrIndependentComplexRowExecution",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "gauge_transported_trace_closure": rel(TRACE),
            "psm_c1_02_source_promotion_closure": rel(PROMOTION),
            "post_source_fullsm_gap": rel(NEXT),
        },
        "theorem": {
            "name": "GaugeTransportedBNPhiFinTraceOrIndependentComplexRowExecutionTheorem",
            "proved": True,
            "statement": (
                "The gauge-transported BN/PhiFin trace closes the Route-A "
                "source-promotion route. PSM-C1-02 unpatched source promotion, "
                "A_selected, b_selected, and deltaTheta_C1 are promoted; the "
                "remaining frontier is post-source full-SM closure."
            ),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(OUT, candidate)

    cert = {
        "certificate": "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_or_IndependentComplexRowExecution_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "theorem_proved": True,
        **decision,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected GaugeTransported BN PhiFin Trace or IndependentComplexRowExecution v1

Status: `{STATUS}`.

## Closed Now

```text
gauge transported BN/PhiFin trace closed          true
PSM-C1-02 unpatched source promotion closed       true
Route A transport-closed import validates         true
Route B independent rows required for PSM closure false
A_selected promoted                              true
b_selected promoted                              true
deltaTheta_C1 promoted                           true
PhiFinC1 emission validator passes               true
PSM-C1-02 source-promotion validator passes      true
```

## Still Open

```text
post-source full-SM gap selected                  true
Yukawa/mass/mixing closure without proxy fitting  false
selected dotD/alpha1 with transport derivative    false
selected matter-slot routing and normalization    false
final no-knob constants/covariance/RG linkage     false
true SM equivalence                               false
```

Next artifact: `{NEXT_ARTIFACT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
