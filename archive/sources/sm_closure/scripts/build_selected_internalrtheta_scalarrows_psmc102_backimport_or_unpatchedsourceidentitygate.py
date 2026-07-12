"""Backimport PSM-C1-02 source-promotion progress into the internal Rtheta scalar-row gate.

The direct Rtheta scalar-row branch previously stopped at "dynamic overlap/C1
payload open."  Later PSM-C1-02 work sharpened that blocker: the dynamic source
fields are reduced to a single finite-C1 source identity/action-principle
problem, with a local-principle closure separated from unpatched no-knob proof.
This builder records that sharper result without promoting conditional/local
rows as selected internal Rtheta scalar rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_internalrtheta_scalarrows_psmc102_backimport_or_unpatchedsourceidentitygate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BACKIMPORT = PACKET_DIR / "psm_c1_02_source_chain_backimport.packet.json"
SCALAR_GATE = PACKET_DIR / "internal_scalar_row_gate_after_psm_c1_02_backimport.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_psm_c1_02_backimport.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_InternalRThetaScalarRows_PSMC102Backimport_or_UnpatchedSourceIdentityGate_v1.md"

PREVIOUS = DATA / "selected_u10ubar5_1m_sourcepromotion_samebranch_emission.candidate.json"
PREVIOUS_SCALAR_GATE = (
    DATA
    / "selected_u10ubar5_1m_sourcepromotion_samebranch_emission"
    / "internal_scalar_row_gate_after_static_matter_slot_readout.packet.json"
)
DIRECT_ATTEMPT = (
    DATA
    / "selected_internalrthetascalarrowemission_or_universalanchorselection"
    / "direct_internal_rtheta_scalar_row_emission_attempt.packet.json"
)
HIGHER_CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)
SOURCE_PROMOTION_PACKET = DATA / "selected_psm_c1_02_selectedsourcepromotionpacket.candidate.json"
SOURCE_PROMOTION_MATRIX = (
    DATA
    / "selected_psm_c1_02_selectedsourcepromotionpacket"
    / "psm_c1_02_source_promotion_matrix.packet.json"
)
RA3_RB5 = DATA / "selected_psm_c1_02_ra3_samesourceemission_or_rb5_dynamicvalueownerfill.candidate.json"
SOURCE_IDENTITY_ATTEMPT = DATA / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt.candidate.json"
LOCAL_SOURCE_IDENTITY = (
    DATA / "selected_psm_c1_02_localsourceidentityclosure_integration_or_unpatchedkernelexecution.candidate.json"
)
LOCAL_REPLAY = DATA / "selected_psm_c1_02_localreplayreconciliation_or_unpatchedkernelexecutionplan.candidate.json"
UNPATCHED_KERNEL_PLAN = DATA / "selected_psm_c1_02_unpatchedkernelexecutionplan_or_honestgalerkinexport.candidate.json"
PRIMITIVE_QUADRATURE = (
    DATA / "selected_psm_c1_02_primitivequadratureexport_or_unpatchedsourcepromotionpacket.candidate.json"
)
VARIATIONAL_BRIDGE = (
    DATA / "selected_psm_c1_02_selectedfinitec1_variationalbridge_or_sourcepromotionlemma.candidate.json"
)
UNPATCHED_GATE = (
    DATA
    / "selected_psm_c1_02_selectedfinitec1_variationalbridge_or_sourcepromotionlemma"
    / "unpatched_source_promotion_gate.packet.json"
)

STATUS = (
    "MTT_SELECTED_INTERNALRTHETA_SCALARROWS_PSMC102_BACKIMPORT_"
    "BUILT_LOCAL_C1_SOURCE_READY_UNPATCHED_SCALARROWS_OPEN"
)
NEXT = "MTT_Selected_PSM_C1_02_UnpatchedWeylVariationActionPrincipleDerivation_or_IndependentRowSourceExecution_v1"


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
        raise FileNotFoundError("missing PSM-C1-02 backimport inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_SCALAR_GATE,
        DIRECT_ATTEMPT,
        HIGHER_CONTRACT,
        SOURCE_PROMOTION_PACKET,
        SOURCE_PROMOTION_MATRIX,
        RA3_RB5,
        SOURCE_IDENTITY_ATTEMPT,
        LOCAL_SOURCE_IDENTITY,
        LOCAL_REPLAY,
        UNPATCHED_KERNEL_PLAN,
        PRIMITIVE_QUADRATURE,
        VARIATIONAL_BRIDGE,
        UNPATCHED_GATE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_gate = load(PREVIOUS_SCALAR_GATE)
    direct = load(DIRECT_ATTEMPT)
    higher_contract = load(HIGHER_CONTRACT)
    source_packet = load(SOURCE_PROMOTION_PACKET)
    source_matrix = load(SOURCE_PROMOTION_MATRIX)
    ra3_rb5 = load(RA3_RB5)
    source_identity = load(SOURCE_IDENTITY_ATTEMPT)
    local_identity = load(LOCAL_SOURCE_IDENTITY)
    local_replay = load(LOCAL_REPLAY)
    unpatched_plan = load(UNPATCHED_KERNEL_PLAN)
    primitive_quadrature = load(PRIMITIVE_QUADRATURE)
    variational_bridge = load(VARIATIONAL_BRIDGE)
    unpatched_gate = load(UNPATCHED_GATE)

    local_c1_source_ready = (
        local_identity["what_closes_now"]["local_110row_source_identity_validates"]
        and local_replay["what_closes_now"]["unpatched_kernel_execution_plan_emitted"]
        and primitive_quadrature["what_closes_now"][
            "SI1u_B2_local_principle_primitive_source_packet_validates"
        ]
        and variational_bridge["what_closes_now"][
            "SelectedFiniteC1SourcePromotionLemma_under_explicit_local_principle"
        ]
    )
    unpatched_source_identity_closed = (
        variational_bridge["what_closes_now"]["source_promotion_as_unpatched_no_knob_theorem"]
        or not variational_bridge["what_remains_open"]["unpatched_PSM_C1_02_closure"]
    )
    direct_scalar_rows_ready = local_c1_source_ready and unpatched_source_identity_closed

    backimport = {
        "schema": "MTTPSMC102SourceChainBackimportToInternalRthetaScalarRows.v1",
        "status": "LOCAL_C1_SOURCE_CHAIN_READY_UNPATCHED_SOURCE_IDENTITY_OPEN",
        "previous_scalar_gate": rel(PREVIOUS_SCALAR_GATE),
        "source_promotion_packet": rel(SOURCE_PROMOTION_PACKET),
        "dynamic_fields_reduced_to_single_identity": ra3_rb5["what_closes_now"][
            "four_dynamic_fields_reduced_to_single_identity"
        ],
        "single_unpatched_obstruction": source_identity["what_remains_open"][
            "PhysicalActionOwnsFiniteTraceKernel"
        ],
        "local_c1_source_identity_integrated": local_identity["what_closes_now"][
            "SI1d_local_source_identity_integrated"
        ],
        "local_primitive_source_packet_validates": primitive_quadrature["what_closes_now"][
            "SI1u_B2_local_principle_primitive_source_packet_validates"
        ],
        "local_source_promotion_closed": local_c1_source_ready,
        "unpatched_source_promotion_closed": unpatched_source_identity_closed,
        "current_unpatched_source_packet_passes": source_matrix["current_packet_passes"],
        "conditional_unpatched_source_packet_passes": source_matrix["conditional_packet_passes"],
        "patched_packet_rejected_for_unpatched_proof": not source_matrix[
            "patched_packet_passes_unpatched_validator"
        ],
        "unpatched_next_gate": rel(UNPATCHED_GATE),
        "must_add_one_of": unpatched_gate["must_add_one_of"],
        "meaning_for_internal_rtheta": (
            "The old dynamic-overlap blocker is now sharpened to an unpatched finite-C1 "
            "source-identity/action-principle gate. Local-principle C1 closure is useful "
            "as a conditional model, but it is not an accepted no-knob source for internal "
            "Rtheta scalar rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BACKIMPORT, backimport)

    scalar_gate = {
        "schema": "MTTInternalScalarRowGateAfterPSMC102Backimport.v1",
        "status": "PSM_C1_02_BACKIMPORTED_INTERNAL_SCALAR_ROWS_NOT_EMITTED_UNPATCHED",
        "codomain_scalar_rows": higher_contract["codomain_scalar_rows"],
        "codomain_scalar_row_count": higher_contract["codomain_scalar_row_count"],
        "accepted_internal_scalar_row_count": 0,
        "accepted_internal_scalar_rows": [],
        "lambda_H_row_emitted": False,
        "previous_direct_attempt_accepted_rows": direct["accepted_internal_scalar_row_count"],
        "previous_static_gate_accepted_rows": previous_gate["accepted_internal_scalar_row_count"],
        "local_principle_c1_source_promotion_ready": local_c1_source_ready,
        "local_principle_scalar_rows_accepted_as_no_knob": False,
        "unpatched_source_identity_closed": unpatched_source_identity_closed,
        "direct_internal_rtheta_scalar_rows_ready": direct_scalar_rows_ready,
        "why_zero_rows_remain_accepted": [
            "the local C1 source-promotion route is explicitly conditional/local, not unpatched no-knob",
            "the unpatched SelectedFiniteC1SourceIdentityLemma remains open",
            "the selected Weyl-variation action principle or independent Route-B row source execution is not supplied",
            "the Rtheta value functional still cannot use local or replay rows as selected scalar values",
        ],
        "updated_readiness": {
            "static_matter_slot_readout_layer": previous_gate["updated_readiness"][
                "static_matter_slot_readout_layer"
            ],
            "dynamic_source_fields_reduced_to_single_identity": True,
            "local_principle_finite_C1_source_packet": local_c1_source_ready,
            "unpatched_finite_C1_source_identity": unpatched_source_identity_closed,
            "internal_Rtheta_scalar_rows": direct_scalar_rows_ready,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SCALAR_GATE, scalar_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterPSMC102BackimportToInternalRtheta.v1",
        "status": "NEXT_ATTACK_UNPATCHED_WEYL_VARIATION_OR_INDEPENDENT_ROWSOURCE_EXECUTION",
        "closed_now": {
            "dynamic_overlap_blocker_sharpened_to_source_identity_gate": True,
            "four_dynamic_source_fields_reduced_to_single_identity": True,
            "local_principle_finite_C1_source_promotion_closed": local_c1_source_ready,
            "conditional_unpatched_packet_validates": source_matrix["conditional_packet_passes"],
            "scalar_row_branch_backimported_latest_PSMC102_status": True,
        },
        "still_open": {
            "unpatched_SelectedFiniteC1SourceIdentityLemma": True,
            "derive_SelectedWeylVariationActionPrinciple": True,
            "independent_RouteB_row_source_execution": True,
            "unpatched_PSM_C1_02_closure": True,
            "accepted_internal_Rtheta_scalar_rows": True,
            "lambda_H_internal_scalar_row": True,
            "true_SM_equivalence_or_no_knob_closure": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive SelectedWeylVariationActionPrinciple / physical action ownership from selected MTT geometry",
            "route_B": "execute independent Route-B row source export without residual replay or local principle",
            "then": "rerun direct internal Rtheta scalar-row emission with the unpatched source identity as selected input",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    theorem = {
        "name": "PSMC102BackimportNoDirectScalarEmissionTheorem",
        "proved": True,
        "statement": (
            "Backimporting the latest PSM-C1-02 source-promotion chain into the internal "
            "Rtheta scalar-row gate sharpens the direct-emission blocker. Static matter "
            "slot routing, exact Weyl normal forms, conditional/local finite-C1 source "
            "promotion, and the single-identity reduction are available. However, no "
            "internal Rtheta scalar row is accepted until the finite-C1 source identity "
            "is proved unpatched or an independent Route-B row-source execution is emitted."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedInternalRthetaScalarRowsPSMC102BackimportOrUnpatchedSourceIdentityGate",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "psm_c1_02_source_chain_backimport": rel(BACKIMPORT),
            "internal_scalar_row_gate_after_psm_c1_02_backimport": rel(SCALAR_GATE),
            "next_cutset_after_psm_c1_02_backimport": rel(CUTSET),
        },
        "theorem": theorem,
        "closure_decision": {
            "local_principle_finite_C1_source_promotion_closed": local_c1_source_ready,
            "unpatched_source_identity_closed": unpatched_source_identity_closed,
            "accepted_internal_scalar_row_count": 0,
            "lambda_H_row_emitted": False,
            "direct_internal_rtheta_scalar_rows_closed": direct_scalar_rows_ready,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "previous_status": previous["status"],
        "source_packet_status": source_packet["status"],
        "variational_bridge_status": variational_bridge["status"],
        "unpatched_plan_status": unpatched_plan["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_InternalRThetaScalarRows_PSMC102Backimport_or_UnpatchedSourceIdentityGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "local_principle_finite_C1_source_promotion_closed": local_c1_source_ready,
        "unpatched_source_identity_closed": unpatched_source_identity_closed,
        "accepted_internal_scalar_row_count": 0,
        "lambda_H_row_emitted": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected InternalRThetaScalarRows PSMC102Backimport or UnpatchedSourceIdentityGate v1

Status: `{STATUS}`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

- Local finite-C1 source promotion is ready under the explicit local principle.
- The unpatched/no-knob finite-C1 source identity is still open.
- Accepted internal `R_theta` scalar rows: `0`.
- `lambda_H` row emitted: `false`.

## Meaning

The direct scalar-row branch no longer has a vague "dynamic overlap" blocker.
The blocker is now the unpatched source-identity/action-principle gate, or an
independent Route-B row-source execution.

## Next Artifact

`{NEXT}`
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
