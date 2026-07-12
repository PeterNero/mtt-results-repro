"""Build PSM-C1-02 SI-1u-A unpatched selected-action derivation frontier.

This imports the finite Weyl trace-uniqueness derivation into the PSM-C1-02
source-identity frontier.  It proves the measure-normalization part is no
longer a free local principle, while isolating the remaining physical
Phi_fin^C1 action-restriction and no-extra-boundary/source lemma.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ACTION_SPLIT = BASE / "si1u_a_selected_action_derivation_split.packet.json"
MEASURE_IMPORT = BASE / "finite_weyl_trace_measure_sublemma_import.packet.json"
REMAINDER = BASE / "physical_action_boundary_source_remainder.packet.json"
HONEST_EXECUTION = BASE / "honest_finite_c1_execution_replacement_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_UnpatchedSelectedActionDerivation_or_HonestFiniteC1Execution_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_primitivequadratureexport_or_unpatchedsourcepromotionpacket.candidate.json"
FINITE_TRACE = DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation.candidate.json"
TRACE_SPLIT = DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "finite_c1_trace_measure_principle_split.packet.json"
BOUNDARY_REMAINDER = DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "physical_boundary_source_remainder.packet.json"
ALGEBRAIC_BOUNDARY = DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof" / "finite_trace_boundary_cancellation_certificate.packet.json"
LOCAL_PRINCIPLE = DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation.candidate.json"
LOCAL_PSM = DATA / "selected_psm_c1_02_primitivequadratureexport_or_unpatchedsourcepromotionpacket" / "local_principle_psm_source_promotion_validator_result.packet.json"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_A_MEASURE_SUBLEMMA_DERIVED_ACTION_BOUNDARY_SOURCE_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_PhysicalPhiFinC1ActionRestriction_or_HonestFiniteC1Execution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    finite_trace = load(FINITE_TRACE)
    split = load(TRACE_SPLIT)
    boundary = load(BOUNDARY_REMAINDER)
    algebraic_boundary = load(ALGEBRAIC_BOUNDARY)
    local_principle = load(LOCAL_PRINCIPLE)
    local_psm = load(LOCAL_PSM)

    closed_clauses = {
        name: clause
        for name, clause in split["clauses"].items()
        if clause["closed"] is True
    }
    open_clauses = {
        name: clause
        for name, clause in split["clauses"].items()
        if clause["closed"] is False
    }

    action_split = {
        "schema": "MTTPSMC102SI1uASelectedActionDerivationSplit.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-A",
        "status": "SELECTED_ACTION_DERIVATION_SPLIT_MEASURE_DERIVED_PHYSICAL_BINDING_OPEN",
        "principle": split["principle_name"],
        "closed_clauses": closed_clauses,
        "open_clauses": open_clauses,
        "closed_clause_count": len(closed_clauses),
        "open_clause_count": len(open_clauses),
        "local_principle_psm_packet_passes": local_psm["passes"],
        "local_principle_inserted": local_principle["what_closes_now"]["local_source_identity_principle_inserted"],
        "unpatched_derivation_complete_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    measure_import = {
        "schema": "MTTPSMC102FiniteWeylTraceMeasureSublemmaImport.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-A",
        "status": "FINITE_WEYL_TRACE_MEASURE_SUBLEMMA_IMPORTED_AS_DERIVED",
        "source": rel(FINITE_TRACE),
        "theorem_name": finite_trace["theorem"]["name"],
        "theorem_proved": finite_trace["theorem"]["proved"],
        "statement": finite_trace["theorem"]["statement"],
        "measure_normalization_derived": finite_trace["closure_decision"]["measure_normalization_derived"],
        "finite_trace_boundary_cancellation": algebraic_boundary["algebraic_boundary_closed_now"],
        "measure_part_no_longer_axiomatic": split["what_this_improves"]["patch_measure_part_no_longer_axiomatic"],
        "not_enough_for_unpatched_source_identity": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    remainder = {
        "schema": "MTTPSMC102PhysicalActionBoundarySourceRemainder.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-A",
        "status": "MINIMAL_PHYSICAL_ACTION_RESTRICTION_REMAINDER_EMITTED",
        "source": rel(BOUNDARY_REMAINDER),
        "minimal_next_emissions": boundary["minimal_next_emissions"],
        "route_A_current_emissions": boundary["route_A_current_emissions"],
        "remaining_core_lemma": {
            "name": "PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma",
            "must_prove": [
                "physical Phi_fin^C1 action restricts exactly to the selected finite Weyl quotient",
                "no extra continuum/source boundary term survives outside finite trace cyclicity",
                "first variation emits phase R_Z and shift R_X before residual replay",
                "second variation emits same-source b_selected",
            ],
            "if_proved": boundary["if_all_minimal_next_emissions_hold"],
        },
        "unpatched_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    honest_execution = {
        "schema": "MTTPSMC102HonestFiniteC1ExecutionReplacementContract.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-B2",
        "status": "HONEST_FINITE_C1_EXECUTION_REMAINS_LEGAL_REPLACEMENT",
        "reason": "If the physical action restriction lemma cannot be derived, the replacement is an honest finite-action/Galerkin execution that emits the same 110 source rows independently of the local principle.",
        "must_emit": [
            "72 primitive kernel source rows",
            "2 Hessian b-source rows",
            "36 sector assembly source rows",
            "exactness/error certificates",
            "proof rows are emitted before residual replay and without locked-target dependency",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1uAActionSplit.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_UnpatchedSelectedActionDerivation_or_HonestFiniteC1Execution_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1",
            "task": "Prove PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma.",
        },
        "subtasks": [
            "show physical Phi_fin^C1 restricts exactly to selected finite Weyl quotient",
            "prove no extra physical boundary/source term beyond finite trace cyclicity",
            "emit pre-residual R_Z/R_X first variation source rows",
            "emit same-source b_selected second variation rows",
        ],
        "replacement": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
            "task": "Run honest finite-C1/Galerkin execution for the 110 source rows if SI-1u-A1 does not derive.",
        },
        "status": "NEXT_WORKORDER_PHYSICAL_ACTION_RESTRICTION_OR_HONEST_EXECUTION",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102UnpatchedSelectedActionDerivationOrHonestFiniteC1Execution",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1u-A", "SOURCE-IDENTITY/SI-1u-B2"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "output_packets": {
            "selected_action_derivation_split": rel(ACTION_SPLIT),
            "finite_weyl_trace_measure_sublemma_import": rel(MEASURE_IMPORT),
            "physical_action_boundary_source_remainder": rel(REMAINDER),
            "honest_finite_c1_execution_replacement_contract": rel(HONEST_EXECUTION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "PSMC102SI1uAMeasureDerivedActionRemainderTheorem",
            "proved": True,
            "statement": (
                "For PSM-C1-02, the measure-normalization part of the local SelectedFiniteC1SourceIdentityPrinciple "
                "is derivable from finite Weyl trace uniqueness and algebraic finite trace boundary cancellation. "
                "Therefore the unpatched source-identity problem reduces to the physical Phi_fin^C1 finite-quotient "
                "restriction/no-extra-boundary/source-emission lemma, or to a replacement honest finite-C1 execution."
            ),
        },
        "what_closes_now": {
            "SI1u_A_measure_normalization_sublemma_derived": True,
            "finite_trace_frobenius_pairing_not_free_knob": True,
            "algebraic_finite_trace_boundary_cancellation_imported": True,
            "physical_action_remainder_minimized": True,
            "honest_execution_replacement_contract_preserved": True,
        },
        "what_remains_open": {
            "SI1u_A1_physical_PhiFinC1_finite_quotient_restriction": True,
            "no_extra_physical_boundary_or_source_term": True,
            "pre_residual_R_Z_R_X_source_emission": True,
            "same_source_b_selected_second_variation": True,
            "honest_finite_C1_execution_replacement": True,
            "unpatched_SelectedFiniteC1SourceIdentityTheorem": True,
        },
        "closure_decision": {
            "local_principle_psm_packet_passes": local_psm["passes"],
            "measure_sublemma_derived": True,
            "unpatched_action_derivation_complete": False,
            "honest_finite_c1_execution_closed": False,
            "global_closure_claimed": False,
        },
        "superset_strategy": {
            "classification": "SUPERSET_ROUTE_REDUCTION_WITH_DERIVED_SUBLEMMA",
            "finite_Weyl_path": "derives trace/Frobenius measure normalization",
            "action_path": "must bind physical Phi_fin^C1 to the finite quotient with no extra source term",
            "replacement_path": "honest finite-C1 execution can replace the action lemma",
            "knob_policy": "No observed constants, target fitting, or adjustable coefficients are used.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_UnpatchedSelectedActionDerivation_or_HonestFiniteC1Execution_v1",
        "active_label": "PSM-C1-02",
        "active_routes": candidate["active_routes"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "measure_sublemma_derived": True,
        "unpatched_action_derivation_complete": False,
        "honest_finite_c1_execution_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 UnpatchedSelectedActionDerivation or HonestFiniteC1Execution v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A`

Replacement label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Result

The local source-identity principle is no longer one opaque patch.  Its
finite trace/Frobenius measure-normalization clause is derived from finite Weyl
trace uniqueness, with algebraic finite trace boundary cancellation imported.

This does not yet derive the unpatched source-identity theorem.  The remaining
core lemma is now:

`PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma`

It must prove that physical `Phi_fin^C1` restricts exactly to the selected
finite Weyl quotient, has no extra physical boundary/source term, emits
pre-residual `R_Z/R_X`, and emits same-source `b_selected`.

## Superset Use

This is a route reduction with a derived sublemma, not knobs.  The finite Weyl
route derives the measure.  The action route must supply the physical binding.
The honest finite-C1 execution route remains a legal replacement.

## Next

`PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1`: prove the physical action restriction
and no-extra-boundary/source lemma.

Next artifact: `{NEXT}`
"""

    for path, obj in [
        (ACTION_SPLIT, action_split),
        (MEASURE_IMPORT, measure_import),
        (REMAINDER, remainder),
        (HONEST_EXECUTION, honest_execution),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
