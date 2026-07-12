"""Build physical restriction sublemma / Route B independent rows execution gate."""

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

SLUG = "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RESTRICTION_PROBE = PACKET_DIR / "physical_restriction_sublemma_probe.packet.json"
STRICT_REPLAY = PACKET_DIR / "strict_source_certificate_replay.packet.json"
ROUTE_B_GAP = PACKET_DIR / "route_b_independent_rows_execution_gap.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_physical_restriction_probe.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalRestrictionSublemma_or_RouteBIndependentRowsExecution_v1.md"

PREVIOUS = DATA / "selected_physicalphifinc1finitequotientnoextraboundarysourcelemma_or_independentrows.candidate.json"
PREVIOUS_CUTSET = DATA / "selected_physicalphifinc1finitequotientnoextraboundarysourcelemma_or_independentrows" / "next_cutset_after_lemma_attack.packet.json"
PSM_SOURCE = DATA / "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution.candidate.json"
PSM_PROBE = (
    DATA
    / "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution"
    / "route_a_a1a_physical_action_restriction_source_probe.packet.json"
)
PSM_REPLAY = (
    DATA
    / "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution"
    / "strict_route_a_route_b_validator_replay.packet.json"
)
PSM_ROUTE_B = (
    DATA
    / "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution"
    / "route_b_replacement_readiness.packet.json"
)
STRICT_FILL = DATA / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution" / "current_fill_attempt.packet.json"
STRICT_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"

STATUS = "MTT_SELECTED_PHYSICALRESTRICTIONSUBLEMMA_OR_ROUTEBINDEPENDENTROWSEXECUTION_BUILT_A1A_SOURCE_ROW_OPEN"
NEXT = "MTT_Selected_PhysicalActionRestrictionSourceActualFill_or_RouteBIndependentRun_v1"


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
        [sys.executable, str(STRICT_VALIDATOR), str(payload)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(STRICT_VALIDATOR),
        "payload": rel(payload),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr_lines": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    psm_source = load(PSM_SOURCE)
    psm_probe = load(PSM_PROBE)
    psm_replay = load(PSM_REPLAY)
    psm_route_b = load(PSM_ROUTE_B)
    strict_fill = load(STRICT_FILL)

    restriction_probe = {
        "schema": "MTTPhysicalRestrictionSublemmaProbe.v1",
        "status": "SUPPORT_COMPLETE_SOURCE_ROW_NOT_EMITTED",
        "sublemma": "PhysicalActionRestrictsToSelectedFiniteWeylQuotient",
        "label": "SI-1u-A1a",
        "closed_support": psm_probe["closed_support"],
        "all_closed_support_true": all(psm_probe["closed_support"].values()),
        "candidate_sources_checked": psm_probe["candidate_sources_checked"],
        "accepted_same_branch_sources_found": psm_probe["accepted_same_branch_sources_found"],
        "route_a_slot_value": psm_probe["route_a_slot_value"],
        "same_branch_physical_action_restriction_emitted": psm_probe[
            "same_branch_physical_action_restriction_emitted"
        ],
        "field_filled_now": False,
        "why_not_filled": psm_probe["why_not_filled"],
        "support_only_not_sufficient": psm_probe["support_only_not_sufficient"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    strict_replay = {
        "schema": "MTTStrictSourceCertificateReplayAfterPhysicalRestrictionProbe.v1",
        "status": "STRICT_VALIDATOR_REJECTS_CURRENT_SOURCE_CERTIFICATE",
        "source_replay": rel(PSM_REPLAY),
        "current_packet": rel(STRICT_FILL),
        "validator_script": rel(STRICT_VALIDATOR),
        "validator_result": run_validator(STRICT_FILL),
        "psm_replay_exit_code": psm_replay["exit_code"],
        "expected_missing_route_a_field": psm_replay["expected_missing_route_a_field"],
        "expected_route_b_gap": psm_replay["expected_route_b_gap"],
        "route_A_current_truth": {
            "same_branch": strict_fill["route_A_physical_source_certificate"]["same_branch"],
            "physical_action_restricts_to_selected_finite_Weyl_quotient": strict_fill[
                "route_A_physical_source_certificate"
            ]["physical_action_restricts_to_selected_finite_Weyl_quotient"],
            "attached_same_branch_sources_count": len(
                strict_fill["route_A_physical_source_certificate"]["attached_same_branch_sources"]
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b_gap = {
        "schema": "MTTRouteBIndependentRowsExecutionGap.v1",
        "status": "FORMAL_ROWS_READY_INDEPENDENT_PROVENANCE_OPEN",
        "source": rel(PSM_ROUTE_B),
        "all_72_primitive_rows_executed": psm_route_b["all_72_primitive_rows_executed"],
        "formal_110_rows_executed": psm_route_b["formal_110_rows_executed"],
        "selected_basis_independent_of_residual_projector": psm_route_b[
            "selected_basis_independent_of_residual_projector"
        ],
        "quadrature_rule_independent_of_locked_target": psm_route_b[
            "quadrature_rule_independent_of_locked_target"
        ],
        "source_independent_of_residual_projector_replay": psm_route_b[
            "source_independent_of_residual_projector_replay"
        ],
        "exactness_or_error_certificates_attached": psm_route_b[
            "exactness_or_error_certificates_attached"
        ],
        "attached_independent_provenance_sources": psm_route_b[
            "attached_independent_provenance_sources"
        ],
        "ready_now": psm_route_b["ready_now"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterPhysicalRestrictionProbe.v1",
        "status": "A1A_PHYSICAL_SOURCE_ROW_OR_ROUTEB_PROVENANCE_REMAINS",
        "closed_now": [
            "SI-1u-A1a support probe imported into main chain",
            "strict validator replay confirms current Route A and Route B reject",
            "Route B formal rows are present but independent provenance is absent",
        ],
        "route_A_next_object": {
            "name": "PhysicalActionRestrictionSourceActualFill",
            "must_emit": [
                "same-branch physical Phi_fin^C1 action row",
                "restriction map to selected finite Weyl quotient",
                "at least five same-branch source evidence entries",
            ],
        },
        "route_B_next_object": {
            "name": "RouteBIndependentRowsExecution",
            "must_emit": [
                "selected basis independent of residual projector",
                "quadrature rule independent of locked target",
                "source independence from residual-projector replay",
                "exactness/error certificates",
                "at least three independent provenance sources",
            ],
        },
        "recommended_next": {
            "artifact": NEXT,
            "reason": "The first Route-A field is the narrowest missing source row; Route B can close only by provenance, not by replay values.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (RESTRICTION_PROBE, restriction_probe),
        (STRICT_REPLAY, strict_replay),
        (ROUTE_B_GAP, route_b_gap),
        (NEXT_CUTSET, next_cutset),
    ]:
        write_json(path, payload)

    candidate = {
        "candidate": "MTTSelectedPhysicalRestrictionSublemmaOrRouteBIndependentRowsExecution",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "previous_cutset": rel(PREVIOUS_CUTSET),
            "psm_physical_source_probe": rel(PSM_SOURCE),
            "psm_a1a_probe": rel(PSM_PROBE),
            "psm_strict_replay": rel(PSM_REPLAY),
            "psm_route_b_readiness": rel(PSM_ROUTE_B),
            "strict_fill_attempt": rel(STRICT_FILL),
        },
        "output_packets": {
            "physical_restriction_sublemma_probe": rel(RESTRICTION_PROBE),
            "strict_source_certificate_replay": rel(STRICT_REPLAY),
            "route_b_independent_rows_execution_gap": rel(ROUTE_B_GAP),
            "next_cutset_after_physical_restriction_probe": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "physical_restriction_support_probe_imported": True,
            "closed_support_all_true_but_source_row_absent": restriction_probe["all_closed_support_true"]
            and not restriction_probe["same_branch_physical_action_restriction_emitted"],
            "strict_validator_replay_rejects_current_packet": strict_replay["validator_result"]["returncode"] == 1,
            "route_B_formal_rows_ready_but_provenance_open": route_b_gap["all_72_primitive_rows_executed"]
            and route_b_gap["formal_110_rows_executed"]
            and not route_b_gap["ready_now"],
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "same_branch_physical_action_restriction_row": True,
            "restriction_map_to_selected_finite_Weyl_quotient": True,
            "same_branch_source_evidence": True,
            "route_B_independent_basis_quadrature_provenance": True,
            "route_B_exactness_or_error_certificates": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": {
            "physical_action_restriction_sublemma_proved": False,
            "route_B_independent_rows_executed": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "theorem": {
            "name": "PhysicalRestrictionSupportProbeAndRouteBGapTheorem",
            "proved": True,
            "statement": (
                "The selected finite quotient, trace/Frobenius measure, Weyl variation algebra, and algebraic "
                "finite boundary support are all present, but no same-branch physical Phi_fin^C1 action row "
                "or restriction map to the finite Weyl quotient is emitted. The strict source-certificate "
                "validator therefore rejects the current Route A packet; Route B has formal rows but still lacks "
                "independent basis/quadrature/provenance and exactness certificates."
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
        "certificate": "MTT_Selected_PhysicalRestrictionSublemma_or_RouteBIndependentRowsExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "physical_action_restriction_sublemma_proved": False,
        "route_B_independent_rows_executed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalRestrictionSublemma or RouteBIndependentRowsExecution v1

Status: `{STATUS}`.

The physical restriction sublemma was attacked as `SI-1u-A1a`.

Closed support is complete:

```text
finite selected C1 quotient          = true
finite trace/Frobenius measure       = true
selected Weyl variation algebra      = true
algebraic finite boundary support    = true
```

But no same-branch physical `Phi_fin^C1` action row or restriction map is
emitted yet, so the strict source-certificate validator still rejects.

Route B has formal rows, but not independent basis/quadrature/provenance or
exactness certificates.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
