"""Build CONST-EW-02 B16 source operator or torsion payload.

B16 constructs the next weak-mixing threshold payload from the strongest current
sibling-repo source state.  It imports the now-closed U1 quotient projector
P_perp and the internal Qa-stack finite-part policy/value, then separates those
closed internal/index ingredients from the still-open same-source operator-table
and physical matching gates.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b16_source_operator_or_torsion_payload"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROJECTOR = BASE / "pperp_projector_and_index_import.packet.json"
FINITEPART = BASE / "internal_finitepart_policy_import.packet.json"
HYM = BASE / "hym_operator_payload_status.packet.json"
TORSION = BASE / "torsion_route_status.packet.json"
BOUNDARY = BASE / "weak_mixing_b16_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B16_SourceOperatorOrTorsionPayload_v1.md"

STATUS = "MTT_CONST_EW_02_B16_PROJECTOR_AND_INTERNAL_FINITEPART_IMPORTED_OPERATOR_TABLES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b15_path = DATA / "const_ew_02_weak_mixing_b15_ew_product_map_factorization.candidate.json"
    b15_exits_path = DATA / "const_ew_02_weak_mixing_b15_ew_product_map_factorization" / "operator_or_torsion_exit_matrix.packet.json"

    pperp_note = QA / "proof_corpus" / "Selected_U1_Quotient_Projector_Pperp_and_Trace_Policy_v1.md"
    pperp_cert_path = QA / "certificates" / "selected_u1_quotient_projector_pperp_and_trace_policy_certificate.json"
    finite_note = QA / "proof_corpus" / "Selected_Electroweak_QaStack_FinitePartPolicy_and_IndexScale_SourceTheorem_v1.md"
    finite_cert_path = QA / "certificates" / "selected_electroweak_qastack_finitepart_policy_and_indexscale_certificate.json"
    hym_mu_note = QA / "proof_corpus" / "Selected_Heterotic_HYM_Mu_Selection_or_Full_DeltaA_Spectrum_v1.md"
    hym_packet_note = QA / "proof_corpus" / "Selected_Heterotic_HYM_FullQuotientSpectrum_or_OUHessianScale_SourcePacket_v1.md"
    hym_fill_note = QA / "proof_corpus" / "Selected_Heterotic_HYM_FullQuotientSpectrum_or_OUHessianScale_FillAttempt_v1.md"
    hym_fill_cert_path = QA / "certificates" / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_fillattempt_certificate.json"
    same_source_note = QA / "proof_corpus" / "Selected_U1Y_Same_Source_Nonabelian_or_RouteC_Operator_Payload_v1.md"
    same_source_cert_path = QA / "certificates" / "selected_u1y_same_source_nonabelian_or_routec_operator_payload_certificate.json"
    torsion_note = QA / "proof_corpus" / "Selected_Heterotic_LocalSystemTorsion_or_NewOperatorSource_Attack_v1.md"
    torsion_cert_path = QA / "certificates" / "selected_heterotic_local_system_torsion_or_new_operator_attack_certificate.json"

    b15 = load(b15_path)
    b15_exits = load(b15_exits_path)
    pperp_cert = load(pperp_cert_path)
    finite_cert = load(finite_cert_path)
    hym_fill_cert = load(hym_fill_cert_path)
    same_source_cert = load(same_source_cert_path)
    torsion_cert = load(torsion_cert_path)

    pperp_matrix = [
        ["2/3", "-1/3", "-1/3"],
        ["-1/3", "2/3", "-1/3"],
        ["-1/3", "-1/3", "2/3"],
    ]
    p_a_internal_formula_value = 8.0 * math.log((2.0 * math.pi / 3.0) ** 2) + 8.0 * math.log(2.0 * (2.0 * math.pi / 3.0) ** 2)

    projector = {
        "schema": "MTTConstEW02B16PperpProjectorAndIndexImport.v1",
        "status": "SELECTED_PPERP_PROJECTOR_AND_U1_SU2_INDEX_PAIR_IMPORTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B16-PPERP-INDEX-IMPORT",
        "inputs": {
            "B15_candidate": rel(b15_path),
            "u1_projector_note": rel(pperp_note),
            "u1_projector_certificate": rel(pperp_cert_path),
        },
        "imported_projector": {
            "shared_vector": ["1/sqrt(3)", "1/sqrt(3)", "1/sqrt(3)"],
            "P_perp": pperp_matrix,
            "rank_P_perp": pperp_cert["what_closes"]["rank_P_perp"],
            "trace_P_perp": "2",
            "trace_identity": "3",
            "normalized_trace": pperp_cert["what_closes"]["normalized_trace"],
            "selected_U1_index": "2/3",
            "selected_SU2_index": "1/1",
            "selected_U1_SU2_threshold_index_pair": pperp_cert["what_closes"]["selected_U1_SU2_threshold_index_pair"],
        },
        "scope": pperp_cert["closure_scope"],
        "what_this_closes_from_B15": [
            "P_perp shared-circle quotient projector for U1 carrier",
            "U1 threshold trace policy uses P_perp",
            "dimensionless U1/SU2 threshold-index pair",
        ],
        "what_it_does_not_close": [
            "K_gauge physical anchor",
            "matching scale and running scheme",
            "measured electroweak closure",
            "positive spectrum or finite part for the remaining same-source U1Y/SU2 operator tables",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    finitepart = {
        "schema": "MTTConstEW02B16InternalFinitePartPolicyImport.v1",
        "status": "INTERNAL_QASTACK_FINITEPART_IMPORTED_PHYSICAL_EW_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B16-INTERNAL-FINITEPART-IMPORT",
        "inputs": {
            "finitepart_note": rel(finite_note),
            "finitepart_certificate": rel(finite_cert_path),
        },
        "imported_internal_row": {
            "selected_p_a_internal_promoted": finite_cert["selected_p_a_internal_promoted"],
            "selected_p_a_internal_value": finite_cert["selected_p_a_internal_value"],
            "recomputed_value": p_a_internal_formula_value,
            "formula": "8*log((2*pi/3)^2) + 8*log(2*(2*pi/3)^2)",
            "determinant_scale_mu_internal": "1",
            "regularization": "finite positive zeta/logdet accounting on V/<s>",
        },
        "scope": "selected internal finite determinant row on V/<s>; not measured electroweak closure",
        "lambda_12_closed": finite_cert["lambda_12_closed"],
        "measured_electroweak_closure": finite_cert["measured_electroweak_closure"],
        "what_remains": [
            "same-scheme SU2 row or cancellation",
            "physical gauge/action anchor",
            "matching scale and RG/threshold scheme",
            "selected U1Y operator tables or equivalent full threshold finite part",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    hym = {
        "schema": "MTTConstEW02B16HYMOperatorPayloadStatus.v1",
        "status": "HYM_OPERATOR_PAYLOAD_REDUCED_BUNDLE_CONNECTION_OR_PHIFIN_IDENTITY_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B16-HYM-MONAD-THRESHOLD-OPERATOR",
        "inputs": {
            "B15_exit_matrix": rel(b15_exits_path),
            "hym_mu_selection_note": rel(hym_mu_note),
            "hym_fullquotient_sourcepacket_note": rel(hym_packet_note),
            "hym_fill_attempt_note": rel(hym_fill_note),
            "hym_fill_attempt_certificate": rel(hym_fill_cert_path),
            "same_source_u1y_payload_note": rel(same_source_note),
            "same_source_u1y_payload_certificate": rel(same_source_cert_path),
        },
        "closed_support": {
            "P_perp_projector_compatibility_available": same_source_cert["closed"]["u1_pperp_projector_compatibility_available"],
            "internal_p_a_finitepart_available": finite_cert["selected_p_a_internal_promoted"],
            "HYM_mu_stationary_selection_rejected": True,
            "standard_embedding_retired_as_current_proof_source": hym_fill_cert["standard_embedding_retired_as_current_proof_source"],
        },
        "open_payload_leaves": {
            "selected_operator_tables": same_source_cert["open"]["selected_operator_tables"],
            "selected_U1Y_operator_row": same_source_cert["open"]["selected_U1Y_operator_row"],
            "selected_D_E_Riesz_Green_dotD": same_source_cert["open"]["selected_D_E_Riesz_Green_dotD"],
            "selected_positive_spectrum_or_zeta_heat_torsion": same_source_cert["open"]["selected_positive_spectrum_or_zeta_heat_torsion"],
            "explicit_bundle_connection_solved": not hym_fill_cert["explicit_bundle_connection_solved"],
            "E_Qa_computed": hym_fill_cert["E_Qa_computed"],
            "heterotic_QaSU3_source_identity_proved": hym_fill_cert["heterotic_QaSU3_source_identity_proved"],
        },
        "next_required_object": "Selected_Heterotic_BundleConnection_ValueSolve_or_PhiFin_SourceIdentity_Proof_v1",
        "operator_payload_closed": False,
        "emits_xL": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    torsion = {
        "schema": "MTTConstEW02B16TorsionRouteStatus.v1",
        "status": "ORDINARY_LOCAL_SYSTEM_NEGATIVE_PROJECTIVE_OR_ENDOMORPHISM_ROUTE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B16-LOCAL-SYSTEM-TORSION",
        "inputs": {
            "torsion_attack_note": rel(torsion_note),
            "torsion_attack_certificate": rel(torsion_cert_path),
        },
        "closed_negative": {
            "ordinary_rank_one_torsion_route_closed_negative_for_q64": torsion_cert["ordinary_rank_one_torsion_route_closed_negative_for_q64"],
        },
        "still_open": {
            "q64_projective_route_open_auxiliary": torsion_cert["q64_projective_route_open_auxiliary"],
            "selected_primary_route": torsion_cert["selected_primary_route"],
            "projective_torsion_finite_part": True,
            "operator_domain_bridge_to_Qa_SU3_threshold_complex": True,
        },
        "route_decision": "ordinary rank-one local-system torsion is rejected; source-certified endomorphism_E/full operator is primary",
        "torsion_payload_closed": False,
        "emits_xL": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B16Boundary.v1",
        "status": "PROJECTOR_AND_INTERNAL_FINITEPART_CLOSED_OPERATOR_TABLES_AND_PHYSICAL_MATCHING_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B16-BOUNDARY",
        "closed_now": {
            "P_perp_projector_and_trace_policy": True,
            "dimensionless_U1_SU2_threshold_index_pair": True,
            "internal_Qa_stack_finitepart_policy": True,
            "internal_p_a_value": True,
            "ordinary_rank_one_q64_torsion_route_rejected": True,
        },
        "still_open": {
            "selected_U1Y_operator_tables": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_positive_spectrum_or_zeta_heat_torsion": True,
            "same_scheme_SU2_row_or_cancellation": True,
            "physical_K_gauge_anchor": True,
            "matching_scale_and_RG_threshold_scheme": True,
            "actual_xL_source_emission": True,
            "physical_weak_angle_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B16NextWork.v1",
        "status": "NEXT_WORKORDER_SELECTED_OPERATOR_TABLES_OR_PHYSICAL_MATCHING",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B17-OPERATOR-TABLES-OR-PHYSICAL-MATCHING",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B17-HETEROTIC-BUNDLECONNECTION-OR-PHIFIN-IDENTITY",
            "task": "Prove selected same-source Phi_fin identity or solve explicit selected bundle connection/operator payload with A/F_A, representation action, E_Qa, quotient, trace weights, and finite-part data.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B17-U1Y-ROUTEC-OR-PROJECTIVE-RHOE-OPERATOR-TABLES",
            "task": "Emit selected U1Y operator tables, D_E/Riesz/Green/dotD, and primitive C1 or finite threshold part from the same source.",
        },
        "physical_matching_lane": {
            "label": "CONST-EW-02 / WEAK-MIXING / B17-KGAUGE-MUMATCH-RG-SCHEME",
            "task": "If no strict finite-part table appears, formulate the one-universal-primitive physical matching lane without using observed weak-angle data as selector.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB16SourceOperatorOrTorsionPayload",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B16-SOURCE-OPERATOR-OR-TORSION-PAYLOAD",
        "output_packets": {
            "pperp_projector_and_index_import": rel(PROJECTOR),
            "internal_finitepart_policy_import": rel(FINITEPART),
            "hym_operator_payload_status": rel(HYM),
            "torsion_route_status": rel(TORSION),
            "weak_mixing_b16_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B16SourceOperatorOrTorsionPayloadTheorem",
            "proved": True,
            "statement": (
                "The current source record closes the U1 shared-circle quotient "
                "projector P_perp, the dimensionless U1/SU2 threshold-index pair, "
                "and the internal Qa-stack finite-positive determinant row. It also "
                "rejects ordinary rank-one q64 torsion. These are necessary threshold "
                "payload ingredients, but they do not emit xL. Strict weak-mixing "
                "closure still requires selected same-source U1Y/operator tables or "
                "an explicit heterotic bundle-connection/Phi_fin source identity plus "
                "physical matching."
            ),
        },
        "strict_xL_emitted_now": False,
        "operator_payload_closed": False,
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B16_SourceOperatorOrTorsionPayload_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "input_candidate": rel(b15_path),
        "P_perp_projector_imported": True,
        "dimensionless_U1_SU2_index_pair_imported": True,
        "internal_finitepart_policy_imported": True,
        "selected_p_a_internal_value": finite_cert["selected_p_a_internal_value"],
        "ordinary_rank_one_q64_torsion_rejected": True,
        "operator_payload_closed": False,
        "strict_xL_emitted_now": False,
        "physical_weak_angle_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B16 Source Operator Or Torsion Payload v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B16-SOURCE-OPERATOR-OR-TORSION-PAYLOAD`

## Result

B16 imports the current strongest threshold-payload ingredients.

Closed now:

```text
P_perp = I - (1/3)J on the selected rank-3 U1 carrier
Tr(P_perp)/Tr(I_3) = 2/3
selected SU2 index = 1
internal p_a = {finite_cert["selected_p_a_internal_value"]}
ordinary rank-one q64 torsion route = rejected
```

The internal finite-part value is:

```text
8*log((2*pi/3)^2) + 8*log(2*(2*pi/3)^2)
```

## What Still Blocks Weak Mixing Closure

This still does not emit `xL`.  The missing strict source objects are:

```text
selected U1Y operator tables
selected D_E/Riesz/Green/dotD or equivalent response data
selected positive spectrum, zeta/heat/torsion finite part
same-scheme SU2 row or cancellation
physical K_gauge anchor
matching scale and RG/threshold scheme
```

## Next

`CONST-EW-02 / WEAK-MIXING / B17-OPERATOR-TABLES-OR-PHYSICAL-MATCHING`
"""

    for path, payload in [
        (PROJECTOR, projector),
        (FINITEPART, finitepart),
        (HYM, hym),
        (TORSION, torsion),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
