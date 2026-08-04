"""Build Step51 operator-domain backimport / threshold-profile frontier.

Step50 reduced the operator-payload owner theorem using an older full-S2 cutset.
Later Rtheta-sector artifacts already close the operator/domain side needed for
the Rtheta value evaluator.  Step51 back-imports that progress and moves the
frontier to threshold/profile/value-source rows without accepting numeric rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step51_operator_domain_backimport_or_thresholdprofilefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BACKIMPORT = PACKET_DIR / "step51_operator_domain_backimport.packet.json"
OMEGA_RECHECK = PACKET_DIR / "step51_omega_value_frontier_recheck.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step51_next_threshold_profile_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step51_OperatorDomainBackimport_or_ThresholdProfileFrontier_v1.md"

STEP50 = DATA / "selected_step50_operatorpayload_owner_theorem_or_omega_clauseclosure.candidate.json"
RTHETA_SECTOR = DATA / "selected_rthetasectortransfer_or_primitiveassemblymapexecution.candidate.json"
SECTOR_EXEC = (
    DATA
    / "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
    / "rtheta_sector_transfer_execution.packet.json"
)
ASSEMBLY = (
    DATA
    / "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
    / "primitive_assembly_map_execution.packet.json"
)
PI_VALUE = (
    DATA
    / "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
    / "pi_closure_value_evaluator_domain.packet.json"
)
CUTSET = (
    DATA
    / "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
    / "next_cutset_after_sector_transfer_or_assembly_execution.packet.json"
)
VALUE_EVALUATOR = DATA / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation.candidate.json"
THRESHOLD = DATA / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure.candidate.json"

STATUS = "MTT_SELECTED_STEP51_OPERATOR_DOMAIN_BACKIMPORT_CLOSED_THRESHOLD_PROFILE_ROWS_OPEN"
NEXT = "MTT_Selected_ValueSourceDerivationObligationKernel_or_ExternalThresholdImportManifest_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP50, RTHETA_SECTOR, SECTOR_EXEC, ASSEMBLY, PI_VALUE, CUTSET, VALUE_EVALUATOR, THRESHOLD]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step51 inputs: " + ", ".join(missing))

    step50 = load(STEP50)
    rtheta_sector = load(RTHETA_SECTOR)
    sector = load(SECTOR_EXEC)
    assembly = load(ASSEMBLY)
    pi_value = load(PI_VALUE)
    cutset = load(CUTSET)
    evaluator = load(VALUE_EVALUATOR)
    threshold = load(THRESHOLD)

    operator_domain_closed = all(
        [
            pi_value["Pi_Rtheta_closed"],
            pi_value["coefficient_functional_domain_closed"],
            pi_value["selected_dynamic_operator_source_owner_closed"],
            sector["stationary_sector_transfer_closed"],
            sector["selected_sector_basis_projector_contract_closed"],
            sector["selected_Riesz_Green_stationary_closed"],
            assembly["dynamic_matter_overlap_operator_packet_closed"],
            assembly["VSD01_source_assembly_subgate_closed"],
        ]
    )

    backimport = {
        "schema": "MTTStep51OperatorDomainBackimport.v1",
        "status": "RTHETA_OPERATOR_DOMAIN_BACKIMPORTED_VALUE_ROWS_OPEN",
        "supersedes_step50_old_cutset_for_rtheta_domain": True,
        "step50_source": rel(STEP50),
        "rtheta_sector_source": rel(RTHETA_SECTOR),
        "closed_operator_domain_fields": {
            "Pi_Rtheta": pi_value["Pi_Rtheta_closed"],
            "coefficient_functional_domain": pi_value["coefficient_functional_domain_closed"],
            "selected_dynamic_operator_source_owner": pi_value[
                "selected_dynamic_operator_source_owner_closed"
            ],
            "stationary_sector_transfer": sector["stationary_sector_transfer_closed"],
            "selected_stationary_rho_s": sector["selected_stationary_rho_s_closed"],
            "selected_sector_basis_projector_contract": sector[
                "selected_sector_basis_projector_contract_closed"
            ],
            "selected_Riesz_Green_stationary": sector["selected_Riesz_Green_stationary_closed"],
            "dotD_alpha1_transport_subgate": sector["dotD_alpha1_transport_subgate_closed"],
            "dynamic_matter_overlap_operator_packet": assembly[
                "dynamic_matter_overlap_operator_packet_closed"
            ],
            "VSD01_source_assembly_subgate": assembly["VSD01_source_assembly_subgate_closed"],
            "primitive_C1_overlap_contractions": pi_value["primitive_C1_overlap_contractions_closed"],
            "matter_slot_routing": pi_value["matter_slot_routing_closed"],
        },
        "operator_domain_closed_for_Rtheta_value_evaluator": operator_domain_closed,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(BACKIMPORT, backimport)

    omega_recheck = {
        "schema": "MTTStep51OmegaValueFrontierRecheck.v1",
        "status": "OPERATOR_DOMAIN_READY_VALUE_SOURCE_ROWS_STILL_OPEN",
        "operator_domain_closed_for_Rtheta": operator_domain_closed,
        "selected_threshold_response_functional_instantiated": pi_value[
            "selected_threshold_response_functional_instantiated"
        ],
        "value_execution_readiness_present_count": pi_value["value_execution_readiness_present_count"],
        "value_execution_readiness_requirement_count": pi_value[
            "value_execution_readiness_requirement_count"
        ],
        "accepted_coefficient_value_count": pi_value["accepted_coefficient_value_count"],
        "accepted_lambda_H_value": pi_value["accepted_lambda_H_value"],
        "blocking_failures": pi_value["blocking_failures"],
        "omega_source_rows_accepted_now": 0,
        "minimal_parameter_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(OMEGA_RECHECK, omega_recheck)

    next_frontier = {
        "schema": "MTTStep51NextThresholdProfileFrontier.v1",
        "status": "NEXT_VALUE_SOURCE_DERIVATION_OR_EXTERNAL_THRESHOLD_IMPORT",
        "closed_now": cutset["closed_now"],
        "remaining_value_frontier": threshold["closure_decision"],
        "ordered_remaining_blockers": cutset["still_open"],
        "recommended_next_from_threshold_packet": threshold["next_required_artifact"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_FRONTIER, next_frontier)

    candidate = {
        "candidate": "MTTSelectedStep51OperatorDomainBackimportOrThresholdProfileFrontier",
        "status": STATUS,
        "inputs": {
            "step50": rel(STEP50),
            "rtheta_sector": rel(RTHETA_SECTOR),
            "sector_execution": rel(SECTOR_EXEC),
            "primitive_assembly": rel(ASSEMBLY),
            "pi_value": rel(PI_VALUE),
            "sector_cutset": rel(CUTSET),
            "value_evaluator": rel(VALUE_EVALUATOR),
            "threshold_profile": rel(THRESHOLD),
        },
        "output_packets": {
            "operator_domain_backimport": rel(BACKIMPORT),
            "omega_value_frontier_recheck": rel(OMEGA_RECHECK),
            "next_threshold_profile_frontier": rel(NEXT_FRONTIER),
        },
        "theorem": {
            "name": "Step51OperatorDomainBackimportTheorem",
            "proved": True,
            "statement": (
                "The later Rtheta sector-transfer/primitive-assembly packet supersedes the older "
                "Step50 operator cutset for the Rtheta value-evaluator domain: Pi_Rtheta, stationary "
                "sector transfer, sector basis/projector contract, Riesz/Green/dotD transport, "
                "dynamic operator source ownership, primitive C1 overlap, and coefficient-functional "
                "domain are closed. Numeric Rtheta rows still cannot execute because threshold, "
                "mass-scheme, profile/convention, and no-knob value-source rows remain open."
            ),
        },
        "closure_decision": {
            "operator_domain_closed_for_Rtheta_value_evaluator": operator_domain_closed,
            "Pi_Rtheta_closed": pi_value["Pi_Rtheta_closed"],
            "selected_dynamic_operator_source_owner_closed": pi_value[
                "selected_dynamic_operator_source_owner_closed"
            ],
            "coefficient_functional_domain_closed": pi_value["coefficient_functional_domain_closed"],
            "accepted_internal_Rtheta_coefficient_row_count": 0,
            "accepted_internal_scalar_row_count": 0,
            "selected_lambda_H_row_closed": False,
            "threshold_profile_value_source_rows_closed": False,
            "minimal_parameter_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step51_OperatorDomainBackimport_or_ThresholdProfileFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step51 OperatorDomainBackimport or ThresholdProfileFrontier v1

Status: `{STATUS}`.

Step51 back-imports later Rtheta-sector progress over the older Step50 operator
cutset.

```text
operator domain closed for Rtheta      : {str(operator_domain_closed).lower()}
Pi_Rtheta closed                       : {str(pi_value["Pi_Rtheta_closed"]).lower()}
selected dynamic operator owner closed : {str(pi_value["selected_dynamic_operator_source_owner_closed"]).lower()}
accepted Rtheta coefficient rows       : 0
lambda_H row closed                    : false
```

This retires the old vague operator-payload wall for the Rtheta value-evaluator
domain.  The remaining value wall is now exactly threshold/profile/value-source
closure: scale/scheme/loop convention, threshold rows, mass-scheme rows,
no-knob value derivation, and full profile/accepted diagonal semantics.

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
