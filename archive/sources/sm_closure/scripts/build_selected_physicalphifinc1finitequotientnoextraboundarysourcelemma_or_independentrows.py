"""Attack the physical Phi_fin^C1 finite-quotient/no-extra-source lemma.

The previous gate reduced the unpatched Weyl-variation frontier to the
PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma.  This artifact
attacks that lemma with the strict two-exit validator:

* current unpatched Route A: rejected on the live physical source fields;
* local-principle Route A witness: validates, proving sufficiency;
* Route B independent row-source exit: still open.

No unpatched closure is claimed here.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalphifinc1finitequotientnoextraboundarysourcelemma_or_independentrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CLAUSE_ATTACK = PACKET_DIR / "three_clause_direct_attack.packet.json"
CURRENT_TWO_EXIT = PACKET_DIR / "current_two_exit_source_packet.packet.json"
CURRENT_TWO_EXIT_RESULT = PACKET_DIR / "current_two_exit_source_validator_result.packet.json"
LOCAL_TWO_EXIT = PACKET_DIR / "local_principle_two_exit_source_witness.packet.json"
LOCAL_TWO_EXIT_RESULT = PACKET_DIR / "local_principle_two_exit_source_validator_result.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_lemma_attack.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma_or_IndependentRows_v1.md"

PREVIOUS = DATA / "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill.candidate.json"
REMAINDER = DATA / "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill" / "physical_finite_quotient_remainder.packet.json"
PSM_CERT = (
    DATA
    / "selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution"
    / "si1u_a1_three_field_physical_source_certificate.packet.json"
)
ROUTE_A_TEMPLATE = (
    DATA
    / "selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution"
    / "route_a_physical_source_theorem_template_import.packet.json"
)
ROUTE_B_SPEC = (
    DATA
    / "selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution"
    / "route_b_honest_finite_c1_execution_spec_import.packet.json"
)
LOCAL_ACTION = DATA / "selected_lastsourcelemmaproof_or_independentc1kernelsourcerows" / "local_principle_action_kernel_witness.packet.json"
LOCAL_PHYSICAL = DATA / "selected_lastsourcelemmaproof_or_independentc1kernelsourcerows" / "local_principle_physical_source_witness.packet.json"
MEASURE_REDUCTION = DATA / "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill" / "finite_trace_measure_reduction.packet.json"
SUPPORT_COUNTERMODEL = DATA / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel" / "closed_support_not_enough_countermodel.packet.json"
TWO_EXIT_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"

STATUS = "MTT_SELECTED_PHYSICALPHIFINC1FINITEQUOTIENTNOEXTRABOUNDARYSOURCELEMMA_OR_INDEPENDENTROWS_BUILT_LOCAL_SUFFICIENCY_UNPATCHED_OPEN"
NEXT = "MTT_Selected_PhysicalRestrictionSublemma_or_RouteBIndependentRowsExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(payload: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(TWO_EXIT_VALIDATOR), str(payload)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(TWO_EXIT_VALIDATOR),
        "payload": rel(payload),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    remainder = load(REMAINDER)
    psm_cert = load(PSM_CERT)
    route_a_template = load(ROUTE_A_TEMPLATE)
    route_b_spec = load(ROUTE_B_SPEC)
    local_action = load(LOCAL_ACTION)
    local_physical = load(LOCAL_PHYSICAL)
    measure = load(MEASURE_REDUCTION)
    countermodel = load(SUPPORT_COUNTERMODEL)

    evidence = [
        {"source": rel(PREVIOUS), "closes": "measure-derived frontier and exact remainder"},
        {"source": rel(REMAINDER), "closes": "four-part lemma statement"},
        {"source": rel(PSM_CERT), "closes": "three-field physical source certificate reduction"},
        {"source": rel(ROUTE_A_TEMPLATE), "closes": "Route A source theorem template"},
        {"source": rel(MEASURE_REDUCTION), "closes": "finite trace/Frobenius measure sublemma"},
        {"source": rel(SUPPORT_COUNTERMODEL), "closes": "closed support cannot promote source fields"},
    ]

    clause_attack = {
        "schema": "MTTPhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemmaAttack.v1",
        "status": "DIRECT_ATTACK_REDUCED_TO_THREE_LIVE_PHYSICAL_SOURCE_FIELDS",
        "lemma_name": remainder["lemma_name"],
        "already_removed_from_blocker": remainder["already_removed_from_blocker"],
        "three_field_certificate": psm_cert["fields"],
        "same_source_emission_subfields": psm_cert["same_source_emission_subfields"],
        "clause_results": {
            "physical_action_restricts_to_selected_finite_Weyl_quotient": {
                "proved_now": False,
                "closest_support": [
                    "selected finite C1/Weyl quotient exists",
                    "finite trace/Frobenius measure is derived",
                    "local principle witness validates if accepted",
                ],
                "why_not_proved": "No unpatched physical action restriction/source map is emitted by the current corpus packet.",
            },
            "no_extra_physical_boundary_or_source_term": {
                "proved_now": False,
                "closest_support": [
                    "algebraic finite trace boundary cancellation",
                    "finite quotient cyclicity",
                ],
                "why_not_proved": "Algebraic cancellation inside the quotient is not a same-branch physical no-extra-source theorem.",
            },
            "same_source_R_Z_R_X_b_selected_emission": {
                "proved_now": False,
                "closest_support": [
                    "formal R_Z/R_X/b_selected values",
                    "local-principle action and physical witnesses",
                ],
                "why_not_proved": "Formal/replay values are not same-source physical emissions before residual replay.",
            },
        },
        "support_only_countermodel_blocks_closure": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b_current = {
        "same_branch": True,
        "selected_basis_feeds_all_72_row_functionals": False,
        "pre_residual_phase_shift_variation_operators": False,
        "independent_hessian_counterterm_source_rows": False,
        "sector_rows_assembled_from_source_rows": False,
        "no_residual_projector_replay_or_locked_target_as_source": False,
        "attached_source_evidence": [
            {"source": rel(ROUTE_B_SPEC), "closes": "Route B required outputs"},
            {"source": rel(SUPPORT_COUNTERMODEL), "closes": "replay is not independent source"},
            {"source": rel(PREVIOUS), "closes": "Route B remains parallel legal exit"},
            {"source": rel(PSM_CERT), "closes": "Route A/Route B shared target"},
            {"source": rel(REMAINDER), "closes": "same locked physical source packet"},
        ],
    }

    current_two_exit = {
        "schema": "MTTCurrentPhysicalFiniteQuotientOrIndependentRowsTwoExitPacket.v1",
        "status": "CURRENT_TWO_EXIT_PACKET_REJECTED_SOURCE_FIELDS_OPEN",
        "route_A_physical_action_restriction": {
            "same_branch": True,
            "physical_action_restricts_to_finite_weyl_quotient": False,
            "zero_extra_boundary_or_source_term": False,
            "phase_R_Z_source_selection": False,
            "shift_R_X_source_selection": False,
            "same_source_b_selected_emission": False,
            "attached_source_evidence": evidence,
        },
        "route_B_independent_rowkernel_source": route_b_current,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "closure_claimed": False,
    }

    local_two_exit = json.loads(json.dumps(current_two_exit))
    local_two_exit.update(
        {
            "schema": "MTTLocalPrinciplePhysicalFiniteQuotientTwoExitWitness.v1",
            "status": "ROUTE_A_VALIDATES_UNDER_LOCAL_WEYLVARIATION_PRINCIPLE",
        }
    )
    local_route_a = local_two_exit["route_A_physical_action_restriction"]
    local_route_a.update(
        {
            "physical_action_restricts_to_finite_weyl_quotient": True,
            "zero_extra_boundary_or_source_term": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "local_principle_used": True,
            "accepted_as": local_action["accepted_as"],
            "attached_source_evidence": [
                *evidence,
                {"source": rel(LOCAL_ACTION), "closes": "local action-kernel witness"},
                {"source": rel(LOCAL_PHYSICAL), "closes": "local physical-source witness"},
            ],
        }
    )
    local_two_exit["route_B_independent_rowkernel_source"] = route_b_current
    local_two_exit["closure_claimed"] = False
    local_two_exit["unpatched_theorem_claimed"] = False

    write_json(CLAUSE_ATTACK, clause_attack)
    write_json(CURRENT_TWO_EXIT, current_two_exit)
    write_json(LOCAL_TWO_EXIT, local_two_exit)

    current_result = run_validator(CURRENT_TWO_EXIT)
    local_result = run_validator(LOCAL_TWO_EXIT)
    write_json(CURRENT_TWO_EXIT_RESULT, current_result)
    write_json(LOCAL_TWO_EXIT_RESULT, local_result)

    next_cutset = {
        "schema": "MTTNextCutsetAfterPhysicalFiniteQuotientLemmaAttack.v1",
        "status": "LOCAL_SUFFICIENCY_PROVED_UNPATCHED_THREE_FIELD_CERTIFICATE_OPEN",
        "closed_now": [
            "strict two-exit validator confirms current unpatched packet is incomplete",
            "strict two-exit validator confirms local principle is sufficient for Route A",
            "support-only countermodel blocks proof from closed formal data alone",
        ],
        "remaining_route_A_fields": [
            "physical_action_restricts_to_selected_finite_Weyl_quotient",
            "no_extra_physical_boundary_or_source_term",
            "same_source_R_Z_R_X_b_selected_emission",
        ],
        "remaining_route_B_fields": route_b_spec["required_outputs"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": "Attack SI-1u-A1a first: derive the physical restriction map, or execute Route B independent row-source run.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedPhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemmaOrIndependentRows",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "physical_finite_quotient_remainder": rel(REMAINDER),
            "three_field_certificate": rel(PSM_CERT),
            "route_A_template": rel(ROUTE_A_TEMPLATE),
            "route_B_spec": rel(ROUTE_B_SPEC),
            "local_action_witness": rel(LOCAL_ACTION),
            "local_physical_witness": rel(LOCAL_PHYSICAL),
            "support_countermodel": rel(SUPPORT_COUNTERMODEL),
        },
        "output_packets": {
            "three_clause_direct_attack": rel(CLAUSE_ATTACK),
            "current_two_exit_source_packet": rel(CURRENT_TWO_EXIT),
            "current_two_exit_source_validator_result": rel(CURRENT_TWO_EXIT_RESULT),
            "local_principle_two_exit_source_witness": rel(LOCAL_TWO_EXIT),
            "local_principle_two_exit_source_validator_result": rel(LOCAL_TWO_EXIT_RESULT),
            "next_cutset_after_lemma_attack": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "physical_finite_quotient_lemma_attacked": True,
            "current_unpatched_two_exit_packet_rejected": current_result["returncode"] == 1,
            "local_principle_route_A_two_exit_witness_validates": local_result["returncode"] == 0,
            "support_only_closure_blocked": True,
            "three_field_certificate_is_exact_remaining_route_A": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "physical_action_restricts_to_selected_finite_Weyl_quotient": True,
            "no_extra_physical_boundary_or_source_term": True,
            "same_source_R_Z_R_X_b_selected_emission": True,
            "route_B_independent_row_source_execution": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": {
            "local_conditional_route_A_validated": local_result["returncode"] == 0,
            "unpatched_physical_finite_quotient_lemma_proved": False,
            "route_B_independent_rows_executed": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "theorem": {
            "name": "PhysicalFiniteQuotientLemmaAttackAndLocalSufficiencyTheorem",
            "proved": local_result["returncode"] == 0 and current_result["returncode"] == 1,
            "statement": (
                "The strict two-exit validator rejects the current unpatched physical finite-quotient source packet, "
                "but accepts the same Route A certificate under the accepted local Weyl-variation principle. "
                "Therefore the local principle is sufficient for the PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma, "
                "while the unpatched proof still requires the three-field same-branch certificate or Route B independent rows."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "patched_SM_parity_closure_preserved": previous["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma_or_IndependentRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": candidate["theorem"]["proved"],
        "current_unpatched_two_exit_packet_rejected": current_result["returncode"] == 1,
        "local_principle_route_A_two_exit_witness_validates": local_result["returncode"] == 0,
        "unpatched_physical_finite_quotient_lemma_proved": False,
        "route_B_independent_rows_executed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma or IndependentRows v1

Status: `{STATUS}`.

The lemma was attacked with the strict two-exit validator.

```text
current unpatched two-exit packet validates = {current_result["returncode"] == 0}
local-principle Route A witness validates   = {local_result["returncode"] == 0}
```

Result: the local Weyl-variation principle is sufficient, but the unpatched
three-field physical source certificate is still not filled.

Remaining Route A fields:

```text
physical action restricts to selected finite Weyl quotient
no extra physical boundary/source term
same-source R_Z/R_X/b_selected emission
```

Route B remains independent row-source execution. No observed constants,
locked target values, or fitted SM data are used as selectors.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
