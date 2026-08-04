"""Analyze q79 same-source operator provenance or selected Route-C solve.

This is the proof attempt for the same-source operator theorem.  The script
intentionally distinguishes three levels:

* an honest current packet using the selected terminal ordered source plus the
  current unselected operator promotion attempt;
* a no-primitive diagnostic where the same-source and operator provenance
  fields are supplied hypothetically, while primitive C1 contractions remain
  absent;
* a full plumbing diagnostic where every source/provenance/primitive flag is
  supplied hypothetically to prove the validator has no hidden arithmetic
  obstruction.

Only the first layer is proof evidence.  The latter two are validator plumbing
checks and are recorded as non-proof diagnostics.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
SCRIPTS = ROOT / "scripts"

OUT_DIR = CANDIDATES / "q79_same_source_operator_provenance_or_selected_routec_solve"
OUT_CANDIDATE = CANDIDATES / "q79_same_source_operator_provenance_or_selected_routec_solve.candidate.json"
OUT_CERT = CERTS / "q79_same_source_operator_provenance_or_selected_routec_solve_certificate.json"
OUT_PAPER = CORPUS / "Q79_SameSource_Operator_Provenance_or_Selected_RouteC_Solve_v1.md"
OUT_TABLE = OUT_DIR / "same_source_operator_frontier_summary.json"

STATUS = "Q79_SAME_SOURCE_OPERATOR_PROVENANCE_ATTEMPT_PATCHWORK_NOGO_SELECTED_SOURCE_REQUIRED"
NEXT = "Q79_Selected_Visible_Bundle_Operator_Source_or_Primitive_C1_Contractions_v1"

ORDERED_PACKET = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_ordered_source.selected_under_section_principle.json"
)
S3_CLASS_PACKET = CERTS / "visible_twisted_s3_class_restriction_packet.selected.json"
ORIGINAL_PROMOTION_PACKET = CERTS / "selected_hym_operator_source_promotion.attempt.json"
HYP_PROMOTION_PACKET = (
    CANDIDATES
    / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual"
    / "hypothetical_routec_selected_flags_only"
    / "selected_source_promotion.selected_flags_only.json"
)

INPUTS = {
    "selected_monad_l2_source_and_operatorpic0_or_routec_residual": (
        CERTS / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual_certificate.json"
    ),
    "same_source_monad_gs_operator_fusion_attempt": (
        CANDIDATES / "same_source_monad_gs_operator_fusion_attempt.candidate.json"
    ),
    "selected_valpha_operator_source_sufficiency": (
        CANDIDATES / "selected_valpha_operator_source_sufficiency.candidate.json"
    ),
    "ordered_source_packet": ORDERED_PACKET,
    "visible_twisted_s3_class_restriction": S3_CLASS_PACKET,
    "original_selected_source_promotion": ORIGINAL_PROMOTION_PACKET,
    "hypothetical_selected_source_promotion": HYP_PROMOTION_PACKET,
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
    }


def run_validator(script: str, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    parsed = parse_same_source_report(proc.stdout)
    return {
        "script": f"scripts/{script}",
        "path": rel(path),
        "exit_code": proc.returncode,
        "pass": proc.returncode == 0,
        "stdout_head": proc.stdout.splitlines()[:24],
        "stdout": proc.stdout,
        "parsed_report": parsed,
    }


def parse_same_source_report(stdout: str) -> dict[str, Any] | None:
    prefix = "same_source_monad_gs_operator_fusion_report="
    for line in stdout.splitlines():
        if line.startswith(prefix):
            return json.loads(line[len(prefix) :])
    return None


def forbidden_shortcuts() -> dict[str, bool]:
    return {
        "uses_lifted_flags_as_proof": False,
        "uses_observed_masses_or_mixings": False,
        "uses_benchmark_flavor_entries": False,
        "combines_separate_sources_without_same_source_certificate": False,
        "treats_curvature_only_gs_as_operator_source": False,
    }


def build_packet(
    *,
    status: str,
    packet_role: str,
    source_selected: bool,
    fixture_only: bool,
    same_source: bool,
    source_certificate: str | None,
    visible_gs_same_source: bool,
    operator_passes: bool,
    primitive_c1: bool,
    promotion_packet: Path,
    diagnostic_not_proof: bool,
) -> dict[str, Any]:
    return {
        "schema": "SameSourceMonadGSOperatorFusionPacket.v1",
        "status": status,
        "packet_role": packet_role,
        "diagnostic_not_proof": diagnostic_not_proof,
        "source_identity": {
            "source_kind": "selected_visible_SM_bundle_operator_source",
            "selected_by_mtt": source_selected,
            "no_observed_flavor_inputs": True,
            "same_source_for_ordered_L_pic0_GS_and_DE": same_source,
            "fixture_only": fixture_only,
            "uses_execution_ii_benchmarks": False,
            "source_certificate": source_certificate,
        },
        "ordered_source": {
            "selected_L": [1, -2, 0],
            "selected_L2": [2, -4, 0],
            "source_lane_selector": "terminal_monad_difference_Li_minus_K2",
            "standard_lattice_or_equivalent_selected": True,
            "base_factor_order_selected": True,
            "base_swap_broken_by_source": True,
            "ordered_source_validator_passes": True,
            "pic0_resolution": "pic0_quotient_rule",
            "visible_rank2_l2_ordered_source_packet": rel(ORDERED_PACKET),
        },
        "green_schwarz_and_gerbe": {
            "time_oriented_m1_representative_used": True,
            "antiunitary_q369_retained": True,
            "visible_green_schwarz_row_derived_from_same_source": visible_gs_same_source,
            "freed_witten_or_cycle_restrictions_verified_if_used": True,
            "projector_retention_verified": True,
            "s3_class_restriction_packet": rel(S3_CLASS_PACKET),
        },
        "operator_response": {
            "route_c_residuals_pass": operator_passes,
            "de_action_pass": operator_passes,
            "riesz_gap_pass": operator_passes,
            "reduced_green_pass": operator_passes,
            "dotd_response_pass": operator_passes,
            "selected_dotD_source_verified": operator_passes,
            "primitive_C1_contractions": primitive_c1,
            "iwasawa_selected_source_promotion_packet": rel(promotion_packet),
        },
        "forbidden_shortcuts": forbidden_shortcuts(),
    }


def write_packets() -> dict[str, str]:
    packets = {
        "honest_current_patchwork": build_packet(
            status="CURRENT_PATCHWORK_SELECTED_ORDERED_SOURCE_OPERATOR_SOURCE_OPEN",
            packet_role="honest current proof attempt",
            source_selected=False,
            fixture_only=True,
            same_source=False,
            source_certificate=None,
            visible_gs_same_source=False,
            operator_passes=False,
            primitive_c1=False,
            promotion_packet=ORIGINAL_PROMOTION_PACKET,
            diagnostic_not_proof=False,
        ),
        "hypothetical_same_source_operator_no_primitive_c1": build_packet(
            status="HYPOTHETICAL_SAME_SOURCE_OPERATOR_PROVENANCE_PRIMITIVE_C1_OPEN",
            packet_role="diagnostic: source/operator provenance supplied, primitive C1 absent",
            source_selected=True,
            fixture_only=False,
            same_source=True,
            source_certificate="HYPOTHETICAL_SELECTED_VISIBLE_BUNDLE_OPERATOR_SOURCE_CERTIFICATE",
            visible_gs_same_source=True,
            operator_passes=True,
            primitive_c1=False,
            promotion_packet=HYP_PROMOTION_PACKET,
            diagnostic_not_proof=True,
        ),
        "hypothetical_full_plumbing": build_packet(
            status="HYPOTHETICAL_FULL_SAME_SOURCE_OPERATOR_AND_PRIMITIVE_C1_FLAGS",
            packet_role="diagnostic: all source/operator/primitive flags supplied",
            source_selected=True,
            fixture_only=False,
            same_source=True,
            source_certificate="HYPOTHETICAL_SELECTED_VISIBLE_BUNDLE_OPERATOR_SOURCE_CERTIFICATE",
            visible_gs_same_source=True,
            operator_passes=True,
            primitive_c1=True,
            promotion_packet=HYP_PROMOTION_PACKET,
            diagnostic_not_proof=True,
        ),
    }
    paths: dict[str, str] = {}
    for name, packet in packets.items():
        path = OUT_DIR / f"{name}.same_source_packet.json"
        write_json(path, packet)
        paths[name] = rel(path)
    return paths


def classify_open_items(report: dict[str, Any] | None) -> dict[str, Any]:
    if not report:
        return {"open_item_count": None, "open_items": [], "failures": []}
    open_items = report.get("open_items", [])
    return {
        "open_item_count": len(open_items),
        "open_items": open_items,
        "failures": report.get("failures", []),
    }


def build_candidate() -> dict[str, Any]:
    packet_paths = write_packets()
    validators = {
        name: run_validator(
            "validate_same_source_monad_gs_operator_fusion_packet.py",
            ROOT / path,
        )
        for name, path in packet_paths.items()
    }

    honest = validators["honest_current_patchwork"]["parsed_report"] or {}
    no_primitive = validators[
        "hypothetical_same_source_operator_no_primitive_c1"
    ]["parsed_report"] or {}
    full = validators["hypothetical_full_plumbing"]["parsed_report"] or {}

    honest_open = classify_open_items(honest)
    no_primitive_open = classify_open_items(no_primitive)
    full_open = classify_open_items(full)

    selected_monad = load(INPUTS["selected_monad_l2_source_and_operatorpic0_or_routec_residual"])
    s3 = load(S3_CLASS_PACKET)

    evidence = {
        "selected_ordered_source_closed": selected_monad.get("what_closes_now", {}).get(
            "selected_monad_difference_L2_source_under_explicit_terminal_section_principle"
        )
        is True,
        "selected_h1_ext_input_closed": selected_monad.get("what_closes_now", {}).get(
            "selected_h1_8_nonzero_Ext_input"
        )
        is True,
        "s3_freed_witten_and_projectors_closed": (
            s3.get("s3_restriction", {}).get("smooth_Freed_Witten_cancellation_verified") is True
            and s3.get("projector_retention", {}).get(
                "projector_retention_proved_for_selected_source"
            )
            is True
        ),
        "same_source_visible_gs_row_from_valpha_to_DE_closed": False,
        "selected_operator_DE_Riesz_Green_dotD_closed": False,
        "primitive_c1_contractions_closed": False,
    }

    theorem = {
        "name": "Q79SameSourceOperatorProvenancePatchworkNoGoTheorem",
        "proved": True,
        "closure_claimed": False,
        "statement": (
            "The present corpus proves the selected ordered monad L2/Ext input "
            "and the selected S3 Freed-Witten/projector side conditions, but it "
            "does not prove one selected source binding ordered L/Pic0, visible "
            "Green-Schwarz row, D_E/Riesz/Green/dotD, and primitive C1 data. "
            "Therefore the same-source operator theorem cannot be closed by "
            "patching current artifacts together."
        ),
    }

    reduction = {
        "honest_current_patchwork_validator_status": honest.get("status"),
        "honest_current_patchwork_exit_code": validators["honest_current_patchwork"]["exit_code"],
        "honest_current_open_items": honest_open["open_items"],
        "no_primitive_diagnostic_status": no_primitive.get("status"),
        "no_primitive_diagnostic_exit_code": validators[
            "hypothetical_same_source_operator_no_primitive_c1"
        ]["exit_code"],
        "no_primitive_open_items": no_primitive_open["open_items"],
        "full_plumbing_diagnostic_status": full.get("status"),
        "full_plumbing_diagnostic_exit_code": validators["hypothetical_full_plumbing"][
            "exit_code"
        ],
        "full_plumbing_open_items": full_open["open_items"],
        "diagnostic_interpretation": (
            "If a genuine same-source certificate supplies the provenance fields, "
            "the validator reduces to primitive C1 contractions. If primitive C1 "
            "is also supplied, the current same-source validator passes. This is "
            "a plumbing check only, because the source certificate is hypothetical."
        ),
    }

    closes = {
        "same_source_patchwork_nogo_for_current_artifacts": validators[
            "honest_current_patchwork"
        ]["exit_code"]
        == 2,
        "selected_ordered_source_subvalidator_passes_in_honest_packet": (
            honest.get("subvalidators", {}).get("ordered_source", {}).get("exit_code") == 0
        ),
        "original_operator_promotion_still_rejected": (
            honest.get("subvalidators", {}).get("selected_source_promotion", {}).get(
                "exit_code"
            )
            == 1
        ),
        "operator_provenance_plus_no_primitive_reduces_to_primitive_c1_only": (
            no_primitive_open["open_items"] == ["primitive_C1_contractions must be true"]
        ),
        "full_plumbing_validator_has_no_hidden_obstruction": validators[
            "hypothetical_full_plumbing"
        ]["exit_code"]
        == 0,
    }

    remains = {
        "genuine_selected_visible_bundle_operator_source_certificate": True,
        "same_source_ChernWeil_GS_row_from_that_source": True,
        "operator_layer_Pic0_for_holonomy_sensitive_data": True,
        "selected_DE_rhoE_Riesz_Green_dotD_from_that_source": True,
        "primitive_C1_contractions": True,
        "honest_selected_RouteC_or_HYM_solve": True,
        "selected_Yukawa_CKM_PMNS_Higgs_RG_data": True,
        "full_SM_or_no_knob_closure": True,
    }

    return {
        "certificate": "Q79SameSourceOperatorProvenanceOrSelectedRouteCSolve",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "input_statuses": {name: status_record(path) for name, path in INPUTS.items()},
        "packet_paths": packet_paths,
        "source_evidence_status": evidence,
        "validator_results": validators,
        "same_source_reduction": reduction,
        "what_closes_now": closes,
        "what_remains_open": remains,
        "guardrails": {
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "uses_lifted_flags_as_proof": False,
            "combines_separate_sources_as_if_same_source": False,
            "treats_curvature_only_gs_as_operator_source": False,
            "claims_selected_operator_source_constructed": False,
            "claims_selected_RouteC_residual": False,
            "claims_HYM_connection_constructed": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_full_sm_closure": False,
        },
        "theorem": theorem,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }


def bool_lines(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def bullet_lines(items: list[str]) -> str:
    if not items:
        return "- none"
    return "\n".join(f"- {item}" for item in items)


def build_paper(data: dict[str, Any]) -> str:
    reduction = data["same_source_reduction"]
    return f"""# Q79 Same-Source Operator Provenance or Selected Route-C Solve v1

## Result

The same-source operator theorem is **not** proved from the current corpus.
The honest current packet is rejected by the same-source validator even though
the selected ordered monad source subvalidator now passes.

What is proved here is the patchwork no-go theorem: the current artifacts
cannot be combined into one selected operator source without a new same-source
certificate.

## Honest Current Packet

- packet: `{data["packet_paths"]["honest_current_patchwork"]}`
- validator status: `{reduction["honest_current_patchwork_validator_status"]}`
- exit code: `{reduction["honest_current_patchwork_exit_code"]}`

Open items:

{bullet_lines(reduction["honest_current_open_items"])}

This is the proof-relevant packet. It uses the closed selected ordered source
and the current unselected operator promotion attempt.

## Diagnostic Packets

No-primitive diagnostic:

- packet: `{data["packet_paths"]["hypothetical_same_source_operator_no_primitive_c1"]}`
- validator status: `{reduction["no_primitive_diagnostic_status"]}`
- exit code: `{reduction["no_primitive_diagnostic_exit_code"]}`

Open items:

{bullet_lines(reduction["no_primitive_open_items"])}

Full plumbing diagnostic:

- packet: `{data["packet_paths"]["hypothetical_full_plumbing"]}`
- validator status: `{reduction["full_plumbing_diagnostic_status"]}`
- exit code: `{reduction["full_plumbing_diagnostic_exit_code"]}`

Open items:

{bullet_lines(reduction["full_plumbing_open_items"])}

Interpretation: {reduction["diagnostic_interpretation"]}

These diagnostic packets are not selected-source proofs.

## What Closes Now

{bool_lines(data["what_closes_now"])}

## What Remains Open

{bool_lines(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as a no-go/frontier theorem.

{data["theorem"]["statement"]}

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_TABLE, {
        **data["what_closes_now"],
        "status": data["status"],
        "next_required_artifact": data["next_required_artifact"],
    })
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 same-source operator provenance or selected Route-C solve")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
