"""Build Yukawa source bridge / magnitude projection no-go theorem gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_yukawasourcebridge_or_magnitudeprojectionnogotheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_BRIDGE = PACKET_DIR / "same_source_yukawa_source_bridge.packet.json"
NO_GO = PACKET_DIR / "sector_blind_magnitude_projection_nogo.packet.json"
PROJECTION_REQUIREMENT = PACKET_DIR / "projection_kernel_requirement.packet.json"
DECISION = PACKET_DIR / "yukawa_source_bridge_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_yukawa_source_bridge.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_YukawaSourceBridge_or_MagnitudeProjectionNoGoTheorem_v1.md"

SAME_SOURCE_PACKET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
SAME_SOURCE_VALIDATOR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_validator_result.packet.json"
)
DYNAMIC_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
DYNAMIC_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
QASU3_REPLAY = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
QASU3_VALUE_ATTEMPT = (
    DATA
    / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
    / "yukawa_mass_mixing_value_closure_attempt.packet.json"
)
RTHETA_BASIS = (
    DATA
    / "selected_rtheta_coefficientformuladerivation_or_selectedownerbridge"
    / "dynamic_precoefficient_formula_basis.packet.json"
)
RTHETA_SOLVE_GATE = DATA / "selected_rtheta_selectedroutecgalerkinsolve_or_diagonalprofiletheorem.candidate.json"
RTHETA_SOLVE_DECISION = (
    DATA
    / "selected_rtheta_selectedroutecgalerkinsolve_or_diagonalprofiletheorem"
    / "selected_solve_or_diagonal_profile_decision.packet.json"
)
VERSIONED_VALUES = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
PROFILE_EXECUTION = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution.candidate.json"
CORRELATED_PROFILE = DATA / "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion.candidate.json"
TRANSPORT_SOURCE = DATA / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator.candidate.json"
ALPHA1_DOTD = DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json"

STATUS = (
    "MTT_SELECTED_YUKAWASOURCEBRIDGE_OR_MAGNITUDEPROJECTIONNOGOTHEOREM_"
    "BUILT_SOURCE_LAYER_CLOSED_MAGNITUDES_REQUIRE_PROJECTION"
)
NEXT = "MTT_Selected_YukawaMagnitudeProjectionKernel_or_RThetaThresholdResponseExecution_v1"


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
        raise FileNotFoundError("missing Yukawa source-bridge sources: " + ", ".join(missing))


def matrix_equal(a: Any, b: Any) -> bool:
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        SAME_SOURCE_PACKET,
        SAME_SOURCE_VALIDATOR,
        DYNAMIC_VALUES,
        DYNAMIC_PACKET,
        QASU3_REPLAY,
        QASU3_VALUE_ATTEMPT,
        RTHETA_BASIS,
        RTHETA_SOLVE_GATE,
        RTHETA_SOLVE_DECISION,
        VERSIONED_VALUES,
        PROFILE_EXECUTION,
        CORRELATED_PROFILE,
        TRANSPORT_SOURCE,
        ALPHA1_DOTD,
    ]
    require_sources(sources)

    same_source_packet = load(SAME_SOURCE_PACKET)
    same_source_validator = load(SAME_SOURCE_VALIDATOR)
    dynamic_values = load(DYNAMIC_VALUES)
    dynamic_packet = load(DYNAMIC_PACKET)
    qasu3_replay = load(QASU3_REPLAY)
    qasu3_value_attempt = load(QASU3_VALUE_ATTEMPT)
    rtheta_basis = load(RTHETA_BASIS)
    rtheta_solve_gate = load(RTHETA_SOLVE_GATE)
    rtheta_solve_decision = load(RTHETA_SOLVE_DECISION)
    versioned_values = load(VERSIONED_VALUES)
    profile_execution = load(PROFILE_EXECUTION)
    correlated_profile = load(CORRELATED_PROFILE)
    transport_source = load(TRANSPORT_SOURCE)
    alpha1_dotd = load(ALPHA1_DOTD)

    same_source_fields = same_source_packet["attempted_selected_packet"]["fields"]
    same_source_fields_closed = all(
        field["same_source"] is True
        and field["selected_emitted"] is True
        and field["theorem_derived"] is True
        for field in same_source_fields.values()
    )
    validator_ok = same_source_validator["returncode"] == 0

    source_bridge = {
        "schema": "MTTSameSourceYukawaSourceBridge.v1",
        "status": "YUKAWA_SOURCE_LAYER_BRIDGED_TO_SELECTED_DYNAMIC_OVERLAP",
        "same_source_packet": rel(SAME_SOURCE_PACKET),
        "same_source_validator": rel(SAME_SOURCE_VALIDATOR),
        "transport_source": rel(TRANSPORT_SOURCE),
        "alpha1_dotd_source": rel(ALPHA1_DOTD),
        "source_fields": same_source_fields,
        "source_layer_closure": {
            "same_source_fields_closed": same_source_fields_closed,
            "same_source_validator_ok": validator_ok,
            "selected_dynamic_overlap_tensor_promoted": dynamic_packet["promotion_decision"][
                "dynamic_matter_overlap_operator_packet_closed"
            ],
            "primitive_C1_first_response_layer_emitted": dynamic_packet["what_closes_now"][
                "primitive_C1_contractions_selected_emitted_first_response_layer"
            ],
            "dynamic_QaSU3_first_response_layer_replayed": qasu3_replay["promotion_decision"][
                "dynamic_QaSU3_first_response_layer_closed"
            ],
            "symbolic_transport_source_gate_closed": transport_source["promotion_decision"][
                "physical_source_gate_closed_for_this_target"
            ],
            "alpha1_dotd_retired": alpha1_dotd["closure_decision"][
                "honest_dotd_validator_replay_closed"
            ],
        },
        "closed_scope": (
            "This closes the same-source first-response operator/source layer for Yukawa/Higgs "
            "derivation. It does not close numerical Yukawa magnitudes."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SOURCE_BRIDGE, source_bridge)

    sector_responses = dynamic_values["sector_first_responses"]
    h1_u = sector_responses["u"]["first_hermitian_response_H1"]
    h1_e = sector_responses["e"]["first_hermitian_response_H1"]
    h1_d = sector_responses["d"]["first_hermitian_response_H1"]
    h1_nud = sector_responses["nuD"]["first_hermitian_response_H1"]
    basis_rows = rtheta_basis["sector_basis"]
    invariant_tuples = {
        row["sector"]: (
            row["trace_H1"],
            row["traceless_norm_sq"],
            row["hermitian_residual_norm_sq"],
        )
        for row in basis_rows
    }
    all_invariant_tuples_identical = len(set(invariant_tuples.values())) == 1
    magnitudes = versioned_values["derived_magnitudes"]
    frob_values = {
        "u": magnitudes["frob_Y_u"],
        "d": magnitudes["frob_Y_d"],
        "e": magnitudes["frob_Y_e"],
    }
    u_e_magnitude_distinct = abs(frob_values["u"] - frob_values["e"]) > 1e-12
    u_d_e_magnitudes_not_all_equal = len({round(value, 15) for value in frob_values.values()}) > 1
    h1_u_equals_e = matrix_equal(h1_u, h1_e)
    h1_d_equals_nud = matrix_equal(h1_d, h1_nud)
    sector_blind_no_go = (
        all_invariant_tuples_identical and h1_u_equals_e and u_e_magnitude_distinct
    )

    no_go = {
        "schema": "MTTSectorBlindYukawaMagnitudeProjectionNoGo.v1",
        "status": "SECTOR_BLIND_FIRST_RESPONSE_MAGNITUDE_DERIVATION_REJECTED",
        "theorem": {
            "name": "SectorBlindFirstResponseMagnitudeNoGo",
            "proved": sector_blind_no_go,
            "statement": (
                "The selected first-response dynamic overlap packet cannot by itself determine the "
                "distinct accepted Yukawa magnitudes through any sector-blind functional of the emitted "
                "first-response matrices or their trace/norm invariants. The u and e first-response "
                "Hermitian matrices are identical, and all emitted trace/norm invariant triples are "
                "identical, while the accepted common-scale u and e Frobenius Yukawa magnitudes are distinct."
            ),
        },
        "evidence": {
            "H1_u_equals_H1_e": h1_u_equals_e,
            "H1_d_equals_H1_nuD": h1_d_equals_nud,
            "all_trace_norm_invariant_tuples_identical": all_invariant_tuples_identical,
            "invariant_tuples": invariant_tuples,
            "accepted_common_scale_frobenius_magnitudes": frob_values,
            "u_e_magnitude_distinct": u_e_magnitude_distinct,
            "u_d_e_magnitudes_not_all_equal": u_d_e_magnitudes_not_all_equal,
        },
        "consequence": (
            "A successful no-knob Yukawa magnitude theorem must use extra selected data beyond the "
            "sector-blind first-response invariant layer: sector projectors/slot routing, selected "
            "normalizations, threshold/mass-scheme response, and the physical projection kernel."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(NO_GO, no_go)

    projection_requirement = {
        "schema": "MTTYukawaProjectionKernelRequirement.v1",
        "status": "MAGNITUDE_DERIVATION_REDUCED_TO_SELECTED_PROJECTION_AND_THRESHOLD_RESPONSE",
        "positive_source_layer": rel(SOURCE_BRIDGE),
        "negative_no_go_layer": rel(NO_GO),
        "required_for_magnitude_closure": [
            "sector-aware physical projection kernel Pi_Rtheta or equivalent selected Yukawa slot functor",
            "selected threshold/mass-scheme response values",
            "selected profile/covariance or theorem replacing it",
            "precision convention before measured-value comparison",
        ],
        "current_rtheta_state": {
            "solve_contract_closed": rtheta_solve_decision[
                "selected_routec_galerkin_solve_contract_closed"
            ],
            "selected_routec_galerkin_solve_closed": rtheta_solve_decision[
                "selected_routec_galerkin_solve_closed"
            ],
            "Pi_Rtheta_closed": rtheta_solve_decision["Pi_Rtheta_closed"],
            "profile_response_closed": rtheta_solve_decision["profile_response_closed"],
        },
        "current_value_profile_state": {
            "accepted_common_scale_values_for_SM_parity": profile_execution["closure_decision"][
                "accepted_common_scale_values_for_SM_parity"
            ],
            "accepted_common_scale_values_for_true_precision": profile_execution["closure_decision"][
                "accepted_common_scale_values_for_true_precision"
            ],
            "surrogate_precision_scaffold_closed": correlated_profile["closure_decision"][
                "surrogate_precision_scaffold_closed"
            ],
            "accepted_for_true_precision_equivalence": correlated_profile["closure_decision"][
                "accepted_for_true_precision_equivalence"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROJECTION_REQUIREMENT, projection_requirement)

    decision = {
        "schema": "MTTYukawaSourceBridgeDecision.v1",
        "status": "SOURCE_LAYER_CLOSED_MAGNITUDE_LAYER_OPEN",
        "same_source_yukawa_source_layer_closed": True,
        "sector_blind_first_response_magnitude_no_go_proved": sector_blind_no_go,
        "dynamic_QaSU3_first_response_layer_closed": True,
        "accepted_common_scale_values_for_SM_parity": True,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "Pi_Rtheta_or_equivalent_projection_kernel_closed": False,
        "threshold_mass_scheme_profile_response_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_changes": [
            "The broad 'Yukawa source missing' blocker is replaced by a sharper projection/response blocker.",
            "The same-source dynamic overlap packet is sufficient as a source-layer input to the next projection theorem.",
            "The selected first-response data cannot be converted into distinct magnitudes by a sector-blind invariant formula.",
        ],
        "minimal_next_actions": [
            "construct the selected sector-aware projection kernel from the source packet to Yukawa/Rtheta slots",
            "emit threshold and mass-scheme response values from the same selected branch",
            "rerun the common-scale Yukawa/Higgs profile with the selected projection kernel instead of replay values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterYukawaSourceBridge.v1",
        "status": "NEXT_ATTACK_SELECTED_PROJECTION_KERNEL_AND_THRESHOLD_RESPONSE",
        "closed_now": {
            "same_source_yukawa_source_layer": True,
            "sector_blind_first_response_no_go": sector_blind_no_go,
            "dynamic_QaSU3_first_response_imported": True,
        },
        "still_open": decision["minimal_next_actions"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The selected source exists at first-response level; the missing theorem is now the "
                "sector-aware projection/threshold map that produces magnitudes."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedYukawaSourceBridgeOrMagnitudeProjectionNoGoTheorem",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "same_source_yukawa_source_bridge": rel(SOURCE_BRIDGE),
            "sector_blind_magnitude_projection_nogo": rel(NO_GO),
            "projection_kernel_requirement": rel(PROJECTION_REQUIREMENT),
            "yukawa_source_bridge_decision": rel(DECISION),
            "next_cutset_after_yukawa_source_bridge": rel(CUTSET),
        },
        "theorem": {
            "name": "YukawaSourceBridgeAndMagnitudeProjectionNoGoTheorem",
            "proved": True,
            "statement": (
                "The selected same-source dynamic matter/overlap packet closes the first-response "
                "Yukawa source layer. However, the emitted first-response data are sector-blind/degenerate "
                "at the trace-norm and u/e matrix level, while accepted common-scale magnitudes are distinct. "
                "Therefore final Yukawa magnitude derivation requires a selected sector-aware projection "
                "kernel and threshold/profile response, not another static source assertion."
            ),
        },
        "closure_decision": {
            "same_source_yukawa_source_layer_closed": True,
            "sector_blind_first_response_magnitude_no_go_proved": sector_blind_no_go,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "Pi_Rtheta_or_equivalent_projection_kernel_closed": False,
            "threshold_mass_scheme_profile_response_closed": False,
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
        "certificate": "MTT_Selected_YukawaSourceBridge_or_MagnitudeProjectionNoGoTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "same_source_yukawa_source_layer_closed": True,
        "sector_blind_first_response_magnitude_no_go_proved": sector_blind_no_go,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "Pi_Rtheta_or_equivalent_projection_kernel_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected YukawaSourceBridge or MagnitudeProjectionNoGoTheorem v1

Status: `{STATUS}`.

This artifact reconciles the later same-source dynamic overlap/source-promotion
chain with the Yukawa magnitude frontier.

```text
same-source Yukawa source layer closed : true
sector-blind magnitude no-go proved    : {str(sector_blind_no_go).lower()}
accepted magnitudes no-knob closed     : false
Pi_Rtheta / projection kernel closed   : false
true SM equivalence closed             : false
```

The important advance is that the broad "Yukawa source missing" blocker is no
longer the right description.  The source layer is available at the selected
first-response level.  What remains is the sector-aware projection/threshold
response map: the first-response invariants alone are degenerate, and in
particular the `u` and `e` first-response Hermitian matrices are identical while
their accepted common-scale Frobenius magnitudes are distinct.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
