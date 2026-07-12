"""Attempt the selected Qa/SU3 visible operator-source packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "selected_qa_su3_finite_selected_connection_source_solve_attempt_certificate.json"
Q79_SELECTED_HYM_TEMPLATE = Q79_REPO / "certificates" / "selected_hym_operator_source.template.json"
Q79_SELECTED_HYM_ATTEMPT = Q79_REPO / "certificates" / "selected_hym_operator_source.attempt.json"
Q79_SELECTED_HYM_ATTEMPT_CERT = Q79_REPO / "certificates" / "selected_hym_operator_source_attempt_certificate.json"
Q79_SELECTED_HYM_VALIDATOR = Q79_REPO / "scripts" / "validate_selected_hym_operator_source.py"
Q79_VISIBLE_AFTER_S3 = Q79_REPO / "certificates" / "visible_operator_source_after_s3_closure_certificate.json"
Q79_VISIBLE_GS_SOURCE = Q79_REPO / "certificates" / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
Q79_S3_CLOSURE = Q79_REPO / "certificates" / "visible_twisted_s3_class_restriction_closure_certificate.json"
Q79_GS_CURVATURE = Q79_REPO / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_visible_operator_source_packet.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_visible_operator_source_packet_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_hym_validator() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_SELECTED_HYM_VALIDATOR), str(Q79_SELECTED_HYM_ATTEMPT)],
        cwd=Q79_REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    lines = [line for line in proc.stdout.strip().splitlines() if line]
    failures = [line.removeprefix("- ") for line in lines if line.startswith("- ")]
    report = None
    for line in lines:
        if line.startswith("hym_operator_source_validation_report="):
            report = json.loads(line.removeprefix("hym_operator_source_validation_report="))
    return {
        "exit_code": proc.returncode,
        "output_head": lines[:40],
        "failures": failures,
        "report": report,
    }


def make_template(q79_template: dict[str, Any]) -> dict[str, Any]:
    template = dict(q79_template)
    template["schema"] = "SelectedQaSU3VisibleOperatorSourcePacket.v1"
    template["status"] = "OPEN_SELECTED_QA_SU3_VISIBLE_OPERATOR_SOURCE_PACKET_REQUIRED"
    template["purpose"] = (
        "Fill-in slot for the selected q79/F,m=1 visible bundle/sheaf or "
        "Route-C operator source that must derive the visible Chern-Weil row "
        "and honestly pass selected HYM/Route-C operator validators."
    )
    template["must_consume"] = [
        "visible_twisted_s3_class_restriction_closure_certificate.json",
        "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json",
        "selected_qa_su3_finite_selected_connection_source_solve_attempt_certificate.json",
    ]
    template["must_supply"] = {
        "selected_visible_bundle_or_sheaf_model": None,
        "chern_weil_row_derived_from_selected_source": None,
        "visible_green_schwarz_source_verified": None,
        "route_c_residual_selected_source_verified": None,
        "selected_source_promotion_passes": None,
        "selected_D_E_constructed": None,
        "selected_dotD_constructed": None,
        "selected_riesz_green_constructed": None,
        "coherent_zero_mode_projector_retention": None,
        "primitive_C1_contractions": None,
    }
    return template


def main() -> None:
    previous = load(PREVIOUS)
    q79_template = load(Q79_SELECTED_HYM_TEMPLATE)
    q79_attempt_cert = load(Q79_SELECTED_HYM_ATTEMPT_CERT)
    visible_after_s3 = load(Q79_VISIBLE_AFTER_S3)
    visible_gs_source = load(Q79_VISIBLE_GS_SOURCE)
    s3 = load(Q79_S3_CLOSURE)
    gs_curvature = load(Q79_GS_CURVATURE)
    hym_validation = run_hym_validator()
    template = make_template(q79_template)

    selected_s3_closed = all(
        s3["what_this_closes"].get(key) is True
        for key in (
            "selected_S3_flat_Deligne_class",
            "selected_S3_pullback_restriction_table",
            "smooth_S3_twisted_Freed_Witten_cancellation",
            "block_factorized_family_Higgs_projector_retention_for_this_source",
        )
    )
    visible_curvature_closed = (
        gs_curvature["calculation_results"]["visible_green_schwarz_curvature_verified"] is True
        and gs_curvature["calculation_results"]["required_visible_TrF_row_inserted"] is True
        and gs_curvature["calculation_results"]["symbolic_iwasawa_row_validated"] is True
    )
    current_hym_attempt_rejected = (
        hym_validation["exit_code"] == 1
        and q79_attempt_cert["calculation_results"]["selected_hym_operator_source_verified"] is False
    )
    visible_source_row_inserted_not_derived = (
        visible_gs_source["calculation_results"]["required_visible_TrF_row_inserted"] is True
        and visible_gs_source["attempted_source"]["chern_weil_row_from_source"] is False
        and visible_gs_source["attempted_source"]["selected_visible_bundle_model"] is False
    )

    output = {
        "certificate": "SelectedQaSU3VisibleOperatorSourcePacketAttempt",
        "status": "QA_SU3_VISIBLE_OPERATOR_SOURCE_PACKET_ATTEMPT_BUILT_SELECTED_BUNDLE_SOURCE_OPEN",
        "inputs": {
            "previous_source_solve_attempt": str(PREVIOUS.relative_to(ROOT)),
            "q79_selected_hym_template": str(Q79_SELECTED_HYM_TEMPLATE),
            "q79_selected_hym_attempt": str(Q79_SELECTED_HYM_ATTEMPT),
            "q79_selected_hym_attempt_certificate": str(Q79_SELECTED_HYM_ATTEMPT_CERT),
            "q79_visible_operator_after_s3": str(Q79_VISIBLE_AFTER_S3),
            "q79_visible_gs_source_attempt": str(Q79_VISIBLE_GS_SOURCE),
            "q79_selected_s3_closure": str(Q79_S3_CLOSURE),
            "q79_visible_gs_curvature": str(Q79_GS_CURVATURE),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "validator_result": hym_validation,
        "closed_now": {
            "selected_s3_gerbe_fw_projector_support": selected_s3_closed,
            "visible_green_schwarz_curvature_row": visible_curvature_closed,
            "projective_and_block_factorized_non_source_blockers_reduced": previous["gate_result"][
                "all_current_non_source_blockers_reduced"
            ]
            is True,
            "selected_hym_operator_validator_instantiated": q79_attempt_cert["what_this_closes"][
                "hym_operator_source_gate_instantiated"
            ]
            is True,
            "current_attempt_rejected_honestly": current_hym_attempt_rejected,
        },
        "attempted_but_not_closed": {
            "visible_gs_row_inserted_but_not_derived": visible_source_row_inserted_not_derived,
            "selected_hym_operator_source_verified": q79_attempt_cert["calculation_results"][
                "selected_hym_operator_source_verified"
            ],
            "route_c_honest_operator_pipeline_pass": q79_attempt_cert["calculation_results"][
                "route_c_honest_operator_pipeline_pass"
            ],
            "validator_failures": hym_validation["failures"],
        },
        "not_closed": {
            "selected_visible_bundle_or_sheaf_model": visible_after_s3["still_open_cut_set"][
                "selected_visible_bundle_or_sheaf_model"
            ],
            "Chern_Weil_row_derived_from_selected_source": visible_after_s3["still_open_cut_set"][
                "Chern_Weil_row_derived_from_selected_source"
            ],
            "HYM_or_Route_C_residual_for_visible_source": visible_after_s3["still_open_cut_set"][
                "HYM_or_Route_C_residual_for_visible_source"
            ],
            "selected_D_E_dotD_Riesz_Green": visible_after_s3["still_open_cut_set"][
                "selected_D_E_dotD_Riesz_Green"
            ],
            "coherent_spectral_zero_mode_projectors": visible_after_s3["still_open_cut_set"][
                "coherent_spectral_zero_mode_projectors"
            ],
            "primitive_C1_contractions": visible_after_s3["still_open_cut_set"][
                "primitive_C1_contractions"
            ],
            "full_SM_closure": True,
        },
        "minimal_next_object": {
            "name": "selected_q79_visible_bundle_or_route_c_operator_source",
            "must_do": visible_after_s3["operator_source_target"]["must_supply_next"],
            "validator_to_pass": "validate_selected_hym_operator_source.py plus selected-source promotion validators",
        },
        "guardrails": {
            "claims_selected_visible_operator_source_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "promotes_visible_gs_row_insertion_to_source": False,
            "promotes_route_c_smoke_to_selected_source": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "gate_result": {
            "visible_operator_source_packet_closed": False,
            "template_ready": True,
            "all_prior_non_source_support_available": selected_s3_closed
            and visible_curvature_closed
            and previous["gate_result"]["all_current_non_source_blockers_reduced"] is True,
            "remaining_gate_is_selected_bundle_or_operator_source": True,
            "target_fitting_used": False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    template_text = json.dumps(template, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(template_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
