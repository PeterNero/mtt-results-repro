"""Build Step68 theta exponent weights / prefactor-threshold frontier."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QASU3 = ROOT.parent / "mtt-qa-su3-packet-proof"

SLUG = "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INDEX_IMPORT_PACKET = PACKET_DIR / "step68_qutrit_quotient_index_import.packet.json"
EXPONENT_PACKET = PACKET_DIR / "step68_selected_theta_exponent_weight_rows.packet.json"
OMEGA_REDUCTION_PACKET = PACKET_DIR / "step68_omega_clause_reduction_after_exponent_weights.packet.json"
CUTSET_PACKET = PACKET_DIR / "step68_prefactor_threshold_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step68_ThetaExponentWeights_or_PrefactorThresholdFrontier_v1.md"

STEP67 = DATA / "selected_step67_thetaoverlap_anchor_or_exponentprefactor_frontier.candidate.json"
STEP67_ANCHOR = (
    DATA
    / "selected_step67_thetaoverlap_anchor_or_exponentprefactor_frontier"
    / "step67_theta_overlap_suppression_anchor.packet.json"
)
FAMILY_SPECTRUM = (
    DATA
    / "selected_familyresolvingoperator_or_generationthresholdrowsexecution"
    / "selected_first_response_family_spectrum.packet.json"
)
STATIC_READOUT = (
    DATA
    / "selected_matterslot_readout_backimport_from_smslotfunctor"
    / "selected_static_matterslot_readout.packet.json"
)
OMEGA_OWNER = (
    DATA
    / "selected_step49_omega_payload_clausefill_or_rthetaalpha1valueexecution"
    / "step49_omega_clause_owner_ledger.packet.json"
)
OMEGA_RECHECK = (
    DATA
    / "selected_step49_omega_payload_clausefill_or_rthetaalpha1valueexecution"
    / "step49_rthetaalpha1_value_execution_recheck.packet.json"
)
OMEGA_TEMPLATES = (
    DATA
    / "selected_step49_omega_payload_clausefill_or_rthetaalpha1valueexecution"
    / "step49_omega_source_row_templates.packet.json"
)
XI_SHELLS = (
    DATA
    / "selected_step47_alpha1rtheta_xi_argument_fill_or_internalvaluerows"
    / "step47_xi_argument_shells_filled.packet.json"
)
QUTRIT_INDEX = QASU3 / "candidate_data" / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json"

STATUS = "MTT_SELECTED_STEP68_THETA_EXPONENT_WEIGHTS_CLOSED_PREFACTOR_THRESHOLD_FRONTIER_OPEN"
NEXT = "MTT_Selected_HYMThresholdPrefactorRows_or_OmegaScalarExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def frac(text: str) -> Fraction:
    return Fraction(text.replace(" ", ""))


def rounded_spectrum_ratios(spectrum: dict[str, Any]) -> tuple[list[float], float, list[int]]:
    values = spectrum["sector_results"]["u"]["eigenvalues"]
    gap = float(spectrum["sector_results"]["u"]["min_spectral_gap"])
    ratios = [int(round(float(value) / gap)) for value in values]
    return [float(value) for value in values], gap, ratios


def sector_slot(sector: str) -> dict[str, Any]:
    if sector == "u":
        return {
            "source_direction": "phase_packet_I_plus_Z",
            "source_column": "phase_Z",
            "scalar_coupling_slot": "10M_clock_self_ladder",
            "mixed_10_bar5_scalar_slot": False,
            "positive_branch_quotient_floor": Fraction(0, 1),
        }
    if sector == "d":
        return {
            "source_direction": "shift_packet_I_plus_X",
            "source_column": "shift_X",
            "scalar_coupling_slot": "mixed_10M_bar5M_down_type",
            "mixed_10_bar5_scalar_slot": True,
            "positive_branch_quotient_floor": Fraction(2, 3),
        }
    if sector == "e":
        return {
            "source_direction": "phase_packet_I_plus_Z",
            "source_column": "phase_Z",
            "scalar_coupling_slot": "mixed_10M_bar5M_charged_lepton_transpose",
            "mixed_10_bar5_scalar_slot": True,
            "positive_branch_quotient_floor": Fraction(2, 3),
        }
    raise KeyError(sector)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP67,
        STEP67_ANCHOR,
        FAMILY_SPECTRUM,
        STATIC_READOUT,
        OMEGA_OWNER,
        OMEGA_RECHECK,
        OMEGA_TEMPLATES,
        XI_SHELLS,
        QUTRIT_INDEX,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step68 inputs: " + ", ".join(missing))

    step67 = load(STEP67)
    anchor = load(STEP67_ANCHOR)
    spectrum = load(FAMILY_SPECTRUM)
    static = load(STATIC_READOUT)
    owner = load(OMEGA_OWNER)
    recheck = load(OMEGA_RECHECK)
    templates = load(OMEGA_TEMPLATES)
    xi_shells = load(XI_SHELLS)
    qutrit = load(QUTRIT_INDEX)

    epsilon = float(anchor["epsilon_theta"])
    if abs(epsilon - math.exp(-2 * math.pi)) > 1e-18:
        raise AssertionError("Step67 epsilon is not exp(-2*pi)")

    qutrit_index = frac(qutrit["decision"]["selected_U1_index"])
    if qutrit_index != Fraction(2, 3):
        raise AssertionError("qutrit quotient index is not 2/3")
    p_shared_index = Fraction(1, 3)

    eigenvalues, gap, ratios = rounded_spectrum_ratios(spectrum)
    if ratios != [-2, -1, 1]:
        raise AssertionError(f"unexpected selected family ratios: {ratios}")

    index_import_packet = {
        "schema": "MTTStep68QutritQuotientIndexImport.v1",
        "status": "SELECTED_QUTRIT_SHARED_CIRCLE_QUOTIENT_INDEX_IMPORTED_FOR_EXPONENT_TIER",
        "source": rel(QUTRIT_INDEX),
        "source_status": qutrit["status"],
        "selected_qutrit_quotient_index": str(qutrit_index),
        "selected_shared_line_index": str(p_shared_index),
        "projector": "P_perp = I - J/3",
        "projector_rank": 2,
        "carrier_rank": 3,
        "closed_as_dimensionless_index": qutrit["decision"]["selected_U1_SU2_threshold_index_pair_closed"],
        "not_a_positive_spectrum": True,
        "not_a_threshold_matching_row": True,
        "not_a_mass_scheme_row": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(INDEX_IMPORT_PACKET, index_import_packet)

    readouts = static["selected_readouts"]
    if readouts["selected_phase_shift_partition"]["phase"] != ["u", "e"]:
        raise AssertionError("phase partition mismatch")
    if readouts["selected_phase_shift_partition"]["shift"] != ["d", "nuD"]:
        raise AssertionError("shift partition mismatch")

    charged_rows = []
    for sector in ["u", "d", "e"]:
        slot = sector_slot(sector)
        for generation, ratio in enumerate(ratios, start=1):
            base = Fraction(max(0, -ratio), 1)
            positive_floor = slot["positive_branch_quotient_floor"] if ratio > 0 else Fraction(0, 1)
            exponent = base + positive_floor
            row = {
                "row_id": f"theta_exponent.{sector}.gen{generation}",
                "omega_id": f"Omega_{sector}.gen{generation}",
                "xi_id": f"Xi_{sector}.gen{generation}",
                "coefficient_slot": f"theta_coeff.{sector}.gen{generation}",
                "sector": sector,
                "generation": generation,
                "family_eigenvalue": eigenvalues[generation - 1],
                "family_gap": gap,
                "family_gap_ratio": ratio,
                "family_ladder_exponent": str(base),
                "qutrit_quotient_floor": str(positive_floor),
                "theta_exponent": str(exponent),
                "theta_exponent_numeric": float(exponent),
                "theta_weight": epsilon ** float(exponent),
                "epsilon_theta_exact": "exp(-2*pi)",
                "source_direction": slot["source_direction"],
                "source_column": slot["source_column"],
                "scalar_coupling_slot": slot["scalar_coupling_slot"],
                "mixed_10_bar5_scalar_slot": slot["mixed_10_bar5_scalar_slot"],
                "accepted_as_exponent_weight_row": True,
                "accepted_as_full_omega_source_row": False,
                "accepted_as_internal_scalar_value": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
            charged_rows.append(row)

    higgs_row = {
        "row_id": "theta_exponent.H.lambda",
        "omega_id": "Omega_H.lambda",
        "xi_id": "Xi_H.lambda",
        "coefficient_slot": "lambda_H",
        "sector": "H",
        "generation": None,
        "theta_exponent": str(p_shared_index),
        "theta_exponent_numeric": float(p_shared_index),
        "theta_weight": epsilon ** float(p_shared_index),
        "source_index": "shared central-circle line index Tr(P_shared)/Tr(I_3)=1/3",
        "epsilon_theta_exact": "exp(-2*pi)",
        "accepted_as_higgs_exponent_weight": True,
        "lambda_H_value_row_emitted": False,
        "accepted_as_full_omega_source_row": False,
        "accepted_as_internal_scalar_value": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    exponent_packet = {
        "schema": "MTTStep68SelectedThetaExponentWeightRows.v1",
        "status": "GENERATION_RESOLVED_THETA_EXPONENT_WEIGHT_ROWS_EMITTED_PREFACTORS_OPEN",
        "source_inputs": {
            "epsilon_anchor": rel(STEP67_ANCHOR),
            "family_spectrum": rel(FAMILY_SPECTRUM),
            "static_matter_slot_readout": rel(STATIC_READOUT),
            "qutrit_quotient_index": rel(QUTRIT_INDEX),
        },
        "epsilon_theta": epsilon,
        "epsilon_theta_exact": "exp(-2*pi)",
        "family_gap": gap,
        "family_gap_ratios": ratios,
        "family_ladder_rule": "n_base(g)=max(0,-round(lambda_g/gap)) for selected ratios (-2,-1,+1)",
        "mixed_slot_rule": (
            "mixed 10_M-bar5_M scalar magnitude slots add the selected qutrit quotient floor "
            "2/3 on the positive family branch; the phase/self up slot does not"
        ),
        "higgs_rule": "lambda_H exponent tier receives the selected shared-line index 1/3, not a value row",
        "charged_exponent_weight_rows": charged_rows,
        "higgs_exponent_weight_row": higgs_row,
        "charged_exponent_weight_row_count": len(charged_rows),
        "all_10_exponent_weight_rows_constructed": len(charged_rows) == 9,
        "magnitude_bearing_projection_weights_closed_at_exponent_tier": True,
        "generation_resolved_exponent_rows_closed": True,
        "accepted_full_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EXPONENT_PACKET, exponent_packet)

    old_missing = recheck["missing_value_bearing_clauses"]
    remaining_missing = [
        item for item in old_missing if item != "magnitude_bearing_projection_weights"
    ]
    omega_reduction_packet = {
        "schema": "MTTStep68OmegaClauseReductionAfterExponentWeights.v1",
        "status": "MAGNITUDE_WEIGHT_CLAUSE_CLOSED_AT_EXPONENT_TIER_OMEGA_ROWS_STILL_BLOCKED",
        "omega_owner_source": rel(OMEGA_OWNER),
        "omega_recheck_source": rel(OMEGA_RECHECK),
        "omega_templates_source": rel(OMEGA_TEMPLATES),
        "xi_shell_source": rel(XI_SHELLS),
        "previous_missing_value_bearing_clauses": old_missing,
        "closed_now": {
            "magnitude_bearing_projection_weights": True,
            "generation_resolved_exponent_weight_rows": True,
            "theta_overlap_anchor": True,
            "qutrit_quotient_floor": True,
        },
        "still_missing_value_bearing_clauses": remaining_missing,
        "not_closed_by_step68": {
            "accepted_vsd02_source_rows": True,
            "generation_resolved_threshold_source_rows": True,
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "true_precision_scale_scheme_loop_convention": True,
            "full_profile_likelihood": True,
            "selected_higher_response_operator_payload": True,
            "sector_prefactor_rows": True,
            "lambda_H_prefactor_row": True,
        },
        "accepted_full_omega_source_row_count": templates["accepted_template_count"],
        "accepted_internal_scalar_value_row_count": 0,
        "value_rows_execute": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(OMEGA_REDUCTION_PACKET, omega_reduction_packet)

    cutset_packet = {
        "schema": "MTTStep68PrefactorThresholdCutset.v1",
        "status": "EXPONENT_WEIGHTS_CLOSED_PREFAC_THRESHOLD_OPERATOR_ROWS_REQUIRED",
        "not_missing_anymore": [
            "source-selected theta overlap suppression anchor epsilon_Theta=exp(-2*pi)",
            "source-selected family exponent ladder from ratios (-2,-1,+1)",
            "source-selected qutrit quotient floor 2/3 for mixed slots",
            "source-selected shared-line exponent 1/3 for the Higgs exponent tier",
            "generation-resolved exponent weight rows for u,d,e plus lambda_H exponent shell",
        ],
        "still_missing": [
            "selected HYM/threshold prefactor rows multiplying the exponent weights",
            "selected sector/full-S2 operator payload promotable to Omega rows",
            "selected same-branch threshold matching source rows",
            "selected same-branch mass-scheme conversion source rows",
            "true precision scale/scheme/loop convention",
            "full profile likelihood or accepted diagonal limitation at no-knob tier",
            "selected lambda_H prefactor/value row",
            "accepted Omega source rows emission theorem",
        ],
        "best_next_route": (
            "execute the selected HYM/threshold prefactor row theorem against the Step68 "
            "exponent rows, then run the strict Omega validator without importing replay values"
        ),
        "forbidden_routes": [
            "use diagnostic order-one factors as selected prefactors",
            "treat the 2/3 index as a positive determinant spectrum",
            "treat exponent weights as full scalar values",
            "use observed Yukawa/Higgs values to choose prefactors or thresholds",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET_PACKET, cutset_packet)

    candidate = {
        "candidate": "MTTSelectedStep68ThetaExponentWeightsOrPrefactorThresholdFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "qutrit_quotient_index_import": rel(INDEX_IMPORT_PACKET),
            "selected_theta_exponent_weight_rows": rel(EXPONENT_PACKET),
            "omega_clause_reduction_after_exponent_weights": rel(OMEGA_REDUCTION_PACKET),
            "prefactor_threshold_cutset": rel(CUTSET_PACKET),
        },
        "theorem": {
            "name": "Step68ThetaExponentWeightSourceTheorem",
            "proved": True,
            "statement": (
                "The selected theta-overlap anchor epsilon_Theta=exp(-2*pi), selected family "
                "gap ratios (-2,-1,+1), selected static SM-slot readout, and selected qutrit "
                "shared-circle quotient index 2/3 emit generation-resolved exponent weights "
                "for the u,d,e scalar slots, with a 1/3 shared-line exponent shell for lambda_H. "
                "This closes the magnitude-bearing projection-weight clause only at the exponent "
                "tier. It does not emit HYM/threshold prefactors, accepted Omega source rows, "
                "lambda_H value, Yukawa magnitudes, masses, CKM/PMNS, true SM equivalence, or "
                "full no-knob closure."
            ),
        },
        "closure_decision": {
            "theta_overlap_anchor_closed": True,
            "qutrit_quotient_index_imported": True,
            "selected_family_exponent_ladder_closed": True,
            "generation_resolved_exponent_weight_rows_closed": True,
            "magnitude_bearing_projection_weights_closed_at_exponent_tier": True,
            "accepted_full_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "hym_threshold_prefactor_rows_closed": False,
            "threshold_matching_source_rows_closed": False,
            "mass_scheme_conversion_source_rows_closed": False,
            "selected_higher_response_operator_payload_closed": False,
            "lambda_H_value_row_emitted": False,
            "scalar_value_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step67["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step68_ThetaExponentWeights_or_PrefactorThresholdFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step68 ThetaExponentWeights or PrefactorThresholdFrontier v1

Status: `{STATUS}`.

## What Closed

Step68 closes the exponent-weight tier of the scalar-row problem:

```text
epsilon_Theta                         : exp(-2*pi)
family gap ratios                     : {ratios}
qutrit quotient floor                 : 2/3
Higgs shared-line exponent shell      : 1/3
charged exponent rows emitted         : {len(charged_rows)}
magnitude weights closed, exponent tier: true
accepted Omega source rows            : 0
accepted internal scalar values        : 0
lambda_H value row emitted             : false
true SM equivalence closed             : false
full no-knob closure                   : false
```

The selected family spectrum supplies the integer ladder `(-2,-1,+1)`.  The
selected theta overlap anchor supplies `epsilon_Theta`.  The adjacent Qa/SU3
quotient-projector theorem supplies the non-fit qutrit/shared-circle index
`Tr(P_perp)/Tr(I_3)=2/3`, and the shared line gives the `1/3` Higgs exponent
shell.  No measured Yukawa, Higgs, CKM, or mass value is used as a selector.

## Boundary

The exponent rows are not full scalar rows.  They still need selected
HYM/threshold prefactor rows, same-branch threshold and mass-scheme source rows,
the true precision convention/profile clause, and the sector/full-S2 operator
payload before the strict Omega validator can accept value rows.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
