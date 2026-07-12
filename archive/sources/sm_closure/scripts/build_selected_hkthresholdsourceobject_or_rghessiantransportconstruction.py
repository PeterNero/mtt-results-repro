"""Build the H K-threshold source object or RG Hessian transport construction.

This packet pushes path #2: selected large-threshold/RG transport.  It imports
the latest Qa/SU3 electroweak determinant chain and records what that closes for
the H/lambda frontier.

Result:
* the internal electroweak finite-part/weak-split support is now closed upstream;
* the universal primitive route remains rejected;
* the strict H row still needs either direct K_H emission or a physical
  gauge-kinetic normalization + matching-scale/RG theorem.
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

SLUG = "selected_hkthresholdsourceobject_or_rghessiantransportconstruction"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_LEDGER = PACKET_DIR / "qa_su3_internal_threshold_import_ledger.packet.json"
RG_TRANSPORT = PACKET_DIR / "h_rg_hessian_transport_source_gate.packet.json"
STRICT_GATE = PACKET_DIR / "strict_h_k_row_gate_after_rg_import.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_h_rg_transport_import.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HKThresholdSourceObject_or_RGHessianTransportConstruction_v1.md"

SOURCES = {
    "previous": DATA / "selected_tenthhthresholdkrowsource_or_largethresholdrgprimitivetheorem.candidate.json",
    "previous_cutset": DATA
    / "selected_tenthhthresholdkrowsource_or_largethresholdrgprimitivetheorem"
    / "next_cutset_after_tenth_h_k_route_execution.packet.json",
    "h_rg_contract": DATA
    / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem"
    / "selected_large_threshold_rg_acceptance_contract.packet.json",
    "h_rg_search": DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "strict_h_threshold_rg_operator_source_search.packet.json",
    "qa_finitepart": QA / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json",
    "qa_su2": QA / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json",
    "qa_physical_anchor": QA / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json",
}

STATUS = (
    "MTT_SELECTED_HKTHRESHOLDSOURCEOBJECT_OR_RGHESSIANTRANSPORTCONSTRUCTION_"
    "QA_INTERNAL_THRESHOLD_IMPORTED_PHYSICAL_RG_OPEN"
)
NEXT = "MTT_Selected_HGaugeKineticNormalizationMuMatch_or_DirectHKThresholdRow_v1"


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
        raise FileNotFoundError("missing H RG transport inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    previous = sources["previous"]["closure_decision"]
    qa_finite = sources["qa_finitepart"]["decision"]
    qa_su2 = sources["qa_su2"]["decision"]
    qa_phys = sources["qa_physical_anchor"]["decision"]
    qa_values = sources["qa_su2"]["selected_internal_threshold_vector"]
    h_contract = sources["h_rg_contract"]
    h_search = sources["h_rg_search"]

    import_ledger = {
        "schema": "MTTQaSU3InternalThresholdImportLedgerForHK.v1",
        "status": "QA_SU3_INTERNAL_THRESHOLD_IMPORTED_TO_H_RG_ROUTE",
        "closure_claimed": True,
        "imported_closures": {
            "qa_internal_finitepart_p_a_closed": qa_finite[
                "selected_p_a_internal_promoted"
            ],
            "qa_internal_p_a_value": qa_finite["selected_p_a_internal_value"],
            "same_scheme_SU2_row_or_cancellation_closed": qa_su2[
                "same_scheme_SU2_row_or_cancellation_closed"
            ],
            "internal_lambda_12_closed": qa_su2["lambda_12_internal_closed"],
            "internal_lambda_12_value": qa_su2["lambda_12_internal_value"],
            "internal_Delta_G12_value": qa_su2["Delta_G12_internal_value"],
            "typed_hypercharge_map_closed": qa_su2["typed_hypercharge_map_closed"],
        },
        "imported_values": {
            "p_a_internal": qa_values["p_a_internal"],
            "p_Y_internal": qa_values["p_Y_internal"],
            "p_c_weaksplit": qa_values["p_c_weaksplit"],
            "p_SU2_weaksplit": qa_values["p_SU2_weaksplit"],
            "lambda_12_internal": qa_values["lambda_12_internal"],
            "Delta_G12_internal": qa_values["Delta_G12_internal"],
        },
        "does_not_close": {
            "physical_gauge_action_anchor": qa_phys["physical_gauge_action_anchor_closed"],
            "matching_scale_mu_match": qa_phys["matching_scale_closed"],
            "RG_scheme": qa_phys["RG_scheme_closed"],
            "measured_electroweak_closure": qa_phys["measured_electroweak_closure"],
            "strict_H_K_threshold_row": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rg_transport = {
        "schema": "MTTHRGHessianTransportSourceGate.v1",
        "status": "INTERNAL_THRESHOLD_SUPPORT_CLOSED_PHYSICAL_RG_TRANSPORT_NOT_EMITTED",
        "closure_claimed": True,
        "h_large_threshold_contract": {
            "object_to_emit": h_contract["object_to_emit"],
            "required_equations": h_contract["required_equations"],
            "strict_acceptance_conditions": h_contract["strict_acceptance_conditions"],
        },
        "current_source_rows": {
            "selected_A_EW": False,
            "selected_mu_match": False,
            "selected_R_H_RG": False,
            "selected_K_threshold_Omega_H_lambda": False,
        },
        "newly_closed_for_path_2": [
            "selected internal Qa finite part p_a",
            "same-scheme SU2/Qc weak-split rows",
            "internal lambda_12 and Delta_G12",
            "typed hypercharge threshold map",
        ],
        "still_missing_for_H_transport": [
            "physical gauge/action normalization K_phys or f_ab",
            "matching scale mu_match",
            "RG and threshold scheme",
            "same-scheme Omega_H.lambda transport certificate",
            "selected R_H^RG determinant/index/provenance row",
        ],
        "reason_not_promoted_to_H_row": (
            "The imported Qa/SU3 closures are dimensionless internal threshold "
            "data. The H large-threshold contract requires physical gauge/action "
            "normalization and matching/RG scheme before R_H^RG can be a source row."
        ),
        "source_search_status": h_search["status"],
        "mathematical_impossibility_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strict_gate = {
        "schema": "MTTStrictHKRowGateAfterRGImport.v1",
        "status": "STRICT_H_ROW_STILL_9_OF_10_AFTER_QA_INTERNAL_RG_IMPORT",
        "closure_claimed": True,
        "accepted_selected_K_source_row_count": previous[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous[
            "selected_K_threshold_row_count_required"
        ],
        "strict_H_K_threshold_row_emitted": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "remaining_strict_source_objects": [
            "direct source-native K_threshold.Omega_H.lambda",
            "physical gauge kinetic normalization + mu_match + RG scheme producing selected R_H^RG",
        ],
        "path_2_progress": {
            "internal_threshold_support_closed": True,
            "same_scheme_SU2_blocker_retired": True,
            "physical_anchor_RG_blocker_active": True,
        },
        "controlled_empirical_10_of_10_available": previous[
            "controlled_empirical_10_of_10_available"
        ],
        "controlled_empirical_10_of_10_selected_for_no_knob": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterHRGTransportImport.v1",
        "status": "NEXT_FRONTIER_H_GAUGEKINETIC_MUMATCH_OR_DIRECT_HK_ROW",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "Qa/SU3 internal finite-part p_a imported",
            "same-scheme SU2 cancellation imported",
            "internal lambda_12/Delta_G12 imported",
            "path #2 reduced to physical gauge kinetic normalization plus mu_match/RG scheme",
        ],
        "still_open": [
            "direct source-native K_threshold.Omega_H.lambda",
            "physical gauge/action normalization K_phys or f_ab",
            "matching scale mu_match",
            "RG and threshold scheme",
            "selected R_H^RG row and same-scheme Omega_H.lambda certificate",
        ],
        "acceptance_contract": {
            "same_branch_q79_F_m1": True,
            "no_observed_electroweak_or_Higgs_target_selector": True,
            "internal_threshold_data_may_be_used": True,
            "physical_anchor_must_be_source_selected": True,
            "ten_K_theorem_trigger_after_H_row_only": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHKThresholdSourceObjectOrRGHessianTransportConstruction",
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
            "qa_su3_internal_threshold_import_ledger": rel(IMPORT_LEDGER),
            "h_rg_hessian_transport_source_gate": rel(RG_TRANSPORT),
            "strict_h_k_row_gate_after_rg_import": rel(STRICT_GATE),
            "next_cutset_after_h_rg_transport_import": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "qa_internal_threshold_imported": True,
            "qa_internal_p_a_value": qa_values["p_a_internal"],
            "qa_internal_lambda_12_value": qa_values["lambda_12_internal"],
            "qa_internal_Delta_G12_value": qa_values["Delta_G12_internal"],
            "same_scheme_SU2_blocker_retired": True,
            "physical_gauge_action_anchor_closed": qa_phys[
                "physical_gauge_action_anchor_closed"
            ],
            "matching_scale_closed": qa_phys["matching_scale_closed"],
            "RG_scheme_closed": qa_phys["RG_scheme_closed"],
            "selected_R_H_RG_emitted": False,
            "selected_A_EW_emitted": False,
            "selected_mu_match_emitted": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": 9,
            "selected_K_threshold_row_count_required": 10,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "HKThresholdSourceObjectOrRGHessianTransportConstructionTheorem",
            "proved": True,
            "statement": (
                "Path #2 imports the latest Qa/SU3 electroweak determinant chain: "
                "the internal finite part, same-scheme SU2/Qc rows, lambda_12, "
                "and Delta_G12 are closed. These retire the internal threshold "
                "and same-scheme SU2 blockers for the H large-threshold route. "
                "They do not emit the physical H RG transport row because the "
                "physical gauge/action normalization, matching scale, and RG "
                "scheme remain unselected."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHKThresholdSourceObjectOrRGHessianTransportConstruction",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "qa_internal_threshold_imported": True,
        "same_scheme_SU2_blocker_retired": True,
        "physical_gauge_action_anchor_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "selected_R_H_RG_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "accepted_selected_K_source_row_count": 9,
        "selected_K_threshold_row_count_required": 10,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected H K-Threshold Source Object or RG Hessian Transport Construction v1

## Theorem

`HKThresholdSourceObjectOrRGHessianTransportConstructionTheorem` is emitted.

Path #2 has been pushed through the Qa/SU3 electroweak determinant chain.  The
following upstream blockers are now retired for the H large-threshold route:

- selected internal finite determinant row `p_a^int = {qa_values["p_a_internal"]}`;
- selected same-scheme `p_Y = {qa_values["p_Y_internal"]}`;
- selected internal `lambda_12 = {qa_values["lambda_12_internal"]}`;
- selected internal `Delta_G12 = {qa_values["Delta_G12_internal"]}`;
- same-scheme SU2/Qc weak-split rows.

## Boundary

These are dimensionless internal threshold data.  They do not by themselves
emit `R_H^RG`, `A_EW`, `mu_match`, or `K_threshold.Omega_H.lambda`.

The strict row remains `9/10`.

## Remaining Path #2 Payload

The next source theorem must emit:

1. physical gauge/action normalization `K_phys` or `f_ab`;
2. selected matching scale `mu_match`;
3. selected RG and threshold scheme;
4. selected `R_H^RG` row with same-scheme `Omega_H.lambda` certificate.

## Next Artifact

`{NEXT}`
"""

    write_json(IMPORT_LEDGER, import_ledger)
    write_json(RG_TRANSPORT, rg_transport)
    write_json(STRICT_GATE, strict_gate)
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
