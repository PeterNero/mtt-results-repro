"""Import gerbe-twisted source-class and local-system response gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")

PREVIOUS = CERTS / "end0_model_packet_and_projective_nogo_import_certificate.json"
SM_PIC0 = SM / "candidate_data" / "selected_pic0_invariance_or_gerbe_twisted_de_source.candidate.json"
QA_INTERFACE = QA / "candidate_data" / "gerbe_twisted_local_system_response_interface.candidate.json"
QA_FILL = QA / "candidate_data" / "gerbe_twisted_local_system_response_fill_attempt.candidate.json"

OUTPUT_PACKET = DATA / "gerbe_twisted_source_class_response_gate_import.candidate.json"
OUTPUT_CERT = CERTS / "gerbe_twisted_source_class_response_gate_import_certificate.json"
OUTPUT_NOTE = CORPUS / "GerbeTwisted_SourceClass_ResponseGate_Import_v1.md"

STATUS = "GERBE_TWISTED_SOURCE_CLASS_RESPONSE_GATE_IMPORTED_VALUES_OPEN"
PREVIOUS_STATUS = "END0_MODEL_PACKET_IMPORTED_PROJECTIVE_ORDINARY_FUNCTOR_NOGO_OPEN"
NEXT = "MTT_Selected_S3_Class_Restriction_Projector_Retention_v1"
PARALLEL_NEXT = "Selected_Qa_SU3_Projective_RhoE_or_DE_Response_Source_Hunt_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_pic0 = load(SM_PIC0)
    qa_interface = load(QA_INTERFACE)
    qa_fill = load(QA_FILL)

    checks = {
        "M0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "M1_pic0_retired_gerbe_primary": sm_pic0["route_decision"]["direct_pic0_invariance"]["status"]
        == "RETIRED_FOR_NOW"
        and sm_pic0["route_decision"]["gerbe_twisted_de_source"]["status"] == "PRIMARY_EXECUTION_ROUTE"
        and sm_pic0["gate_results"]["good_cover_knob_removed"] is True
        and sm_pic0["gate_results"]["selected_smooth_s3_source_constructed"] is False
        and sm_pic0["next_required_artifact"] == NEXT,
        "M2_finite_gerbe_support_closed_but_smooth_open": sm_pic0["imported_results"][
            "deck_cech_lift"
        ]["qutrit_projective_commutator_matched"]
        is True
        and sm_pic0["imported_results"]["finite_s3_cp_cancellation"][
            "finite_S3_CP_cancellation_closed"
        ]
        is True
        and sm_pic0["imported_results"]["visible_gs_curvature"][
            "visible_green_schwarz_curvature_verified"
        ]
        is True
        and sm_pic0["imported_results"]["smooth_s3_lift_attempt"][
            "selected_smooth_S3_source_constructed"
        ]
        is False,
        "M3_qa_interface_built_open": qa_interface["status"]
        == "QA_SU3_GERBE_TWISTED_LOCAL_SYSTEM_RESPONSE_INTERFACE_BUILT_VALUES_OPEN"
        and qa_interface["interface_checks"]["all_pair_twists_cancel"] is True
        and qa_interface["interface_checks"]["all_products_land_in_P"] is True
        and qa_interface["interface_checks"]["template_requires_finite_response"] is True
        and qa_interface["closure_claimed"] is False,
        "M4_qa_fill_partial_blocked": qa_fill["status"]
        == "QA_SU3_GERBE_TWISTED_LOCAL_SYSTEM_RESPONSE_FILL_ATTEMPT_PARTIAL_SOURCE_BLOCKED"
        and qa_fill["fill_result"]["source_family_filled"] is True
        and qa_fill["fill_result"]["twist_cancellation_table_filled"] is True
        and qa_fill["fill_result"]["finite_response_filled"] is False
        and qa_fill["fill_result"]["same_branch_representative_filled"] is False
        and qa_fill["fill_result"]["section_bases_and_constants_filled"] is False,
        "M5_no_target_or_closure_overclaim": sm_pic0["target_fitting_used"] is False
        and sm_pic0["gate_results"]["no_knob_closure_claimed"] is False
        and qa_fill["target_fitting_used"] is False
        and qa_fill["closure_claimed"] is False
        and qa_interface["target_fitting_used"] is False,
    }

    return {
        "packet": "GerbeTwisted_SourceClass_ResponseGate_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_pic0_or_gerbe_source": str(SM_PIC0),
            "qa_gerbe_response_interface": str(QA_INTERFACE),
            "qa_gerbe_response_fill_attempt": str(QA_FILL),
        },
        "theorem": {
            "name": "GerbeTwistedSourceClassResponseGateImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "Direct Pic0 invariance is not a legal closure path with current "
                "operator data. The primary route is the selected q79/F,m=1 "
                "gerbe-twisted differential source: finite deck/Cech, finite S3 "
                "Chan-Paton cancellation, and visible Green-Schwarz curvature are "
                "available, but smooth S3 class restriction, Freed-Witten/projector "
                "retention, and same-branch D_E/dotD/Riesz/Green response remain open. "
                "The Qa/SU3 gerbe-local-system interface has correct twist typing, "
                "but no selected representative, section constants, or finite response."
            ),
        },
        "checks": checks,
        "sm_pic0_or_gerbe_source": sm_pic0,
        "qa_gerbe_response_interface": qa_interface,
        "qa_gerbe_response_fill_attempt": qa_fill,
        "selected_s3_class_packet_contract": sm_pic0["selected_s3_class_packet_contract"],
        "qa_required_packet": qa_interface["required_packet"],
        "what_closes_now": {
            "direct_Pic0_invariance_retired_for_now": True,
            "good_cover_knob_removed": True,
            "gerbe_twisted_route_selected_as_primary": True,
            "finite_q79_F_m1_gerbe_support_imported": True,
            "qa_su3_gerbe_twist_interface_built": True,
            "qa_su3_partial_source_support_filled": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_smooth_S3_class_restriction": True,
            "smooth_S3_Freed_Witten_cancellation": True,
            "twisted_projector_retention_for_block_factorized_sectors": True,
            "same_branch_DE_dotD_Riesz_Green_response": True,
            "qa_su3_same_branch_representative": True,
            "qa_su3_section_bases_and_twisted_constants": True,
            "qa_su3_projective_rhoE_or_DE_response": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_direct_Pic0_invariance": False,
            "claims_selected_smooth_S3_source": False,
            "claims_selected_DE_dotD_Riesz_Green": False,
            "claims_qa_su3_packet_closed": False,
            "claims_finite_response_filled": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
        "parallel_next_required_artifact": PARALLEL_NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "GerbeTwistedSourceClassResponseGateImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "selected_s3_class_packet_contract": packet["selected_s3_class_packet_contract"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
        "parallel_next_required_artifact": packet["parallel_next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    return f"""# GerbeTwisted SourceClass ResponseGate Import v1

Status: `{cert["status"]}`.

Direct Pic0 invariance is retired for now.  The primary route is the selected
q79/F,m=1 gerbe-twisted differential source, with the good-cover choice reduced
to execution scaffold rather than a physical knob.

Closed support:

```text
finite deck/Cech gerbe support
finite S3 Chan-Paton cancellation
visible Green-Schwarz curvature
Qa/SU3 gerbe twist typing interface
```

Still open:

```text
smooth S3 class restriction
Freed-Witten and projector retention
same-branch D_E/dotD/Riesz/Green response
Qa/SU3 projective rho_E or D_E finite response
```

No observed masses, CKM/PMNS data, benchmark matrices, or target residuals are
used as selectors.

Next artifact: `{cert["next_required_artifact"]}`.
Parallel QA/SU3 artifact: `{cert["parallel_next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
