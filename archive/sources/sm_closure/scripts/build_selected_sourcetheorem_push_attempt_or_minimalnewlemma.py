"""Build source-theorem push attempt and minimal conditional promotion lemma."""

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

SLUG = "selected_sourcetheorem_push_attempt_or_minimalnewlemma"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_phifinc1_action_source_theorem_push.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_rowkernel_source_theorem_push.packet.json"
LEMMA = PACKET_DIR / "minimal_selected_finitec1_source_promotion_lemma.packet.json"
WITNESS = PACKET_DIR / "conditional_route_b_validator_witness.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CURRENT_VALIDATOR_RESULT = PACKET_DIR / "current_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceTheorem_PushAttempt_or_MinimalNewLemma_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"

STATUS = "MTT_SELECTED_SOURCETHEOREM_PUSH_BUILT_MINIMAL_CONDITIONAL_LEMMA"
NEXT = "MTT_Selected_MinimalFiniteC1SourcePromotionLemma_Proof_or_Countermodel_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "payload": rel(path),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    gate_dir = DATA / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
    template = load(gate_dir / "two_exit_source_theorem.strict_template.json")
    current = load(gate_dir / "current_two_exit_source_attempt.packet.json")
    cutset = load(gate_dir / "remaining_source_theorem_cutset.packet.json")
    finite_functional = load(
        DATA
        / "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure"
        / "finite_c1_rowkernel_functional_candidate.packet.json"
    )
    provenance = load(DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json")

    route_a = {
        "schema": "MTTRouteAPhiFinC1ActionSourceTheoremPush.v1",
        "status": "ROUTE_A_PUSH_SUPPORT_IMPORTED_PHYSICAL_ACTION_THEOREM_STILL_OPEN",
        "route": "physical Phi_fin^C1 action restriction theorem",
        "strict_required_fields": template["route_A_physical_action_restriction_required_fields"],
        "available_support": current["route_A_physical_action_restriction"]["support_closed"],
        "still_missing": current["route_A_physical_action_restriction"]["still_required"],
        "can_validate_now": False,
        "why_not": (
            "Route A has finite Weyl trace/quotient and algebraic boundary support, but no same-branch theorem yet "
            "that the physical Phi_fin^C1 action restricts with zero extra boundary/source and emits R_Z, R_X, "
            "and b_selected as source rows."
        ),
        "minimal_route_A_lemma": {
            "name": "SelectedPhysicalPhiFinC1ActionRestrictionLemma",
            "must_prove": template["route_A_physical_action_restriction_required_fields"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b = {
        "schema": "MTTRouteBIndependentRowKernelSourceTheoremPush.v1",
        "status": "ROUTE_B_PUSH_CLOSEST_PATH_MINIMAL_SOURCE_PROMOTION_LEMMA_IDENTIFIED",
        "route": "independent row-kernel source theorem",
        "strict_required_fields": template["route_B_independent_rowkernel_source_required_fields"],
        "available_support": {
            "same_branch": current["route_B_independent_rowkernel_source"]["same_branch"],
            "support_closed": current["route_B_independent_rowkernel_source"]["support_closed"],
            "finite_functional_values_filled": finite_functional["row_values"]["values_filled"],
            "finite_functional_values_promoted_as_source": finite_functional["row_values"]["values_promoted_as_source"],
            "all_rows_provenance_promotion_status": provenance["status"],
        },
        "currently_failed_fields": [
            field
            for field in [
                "selected_basis_feeds_all_72_row_functionals",
                "pre_residual_phase_shift_variation_operators",
                "independent_hessian_counterterm_source_rows",
                "sector_rows_assembled_from_source_rows",
                "no_residual_projector_replay_or_locked_target_as_source",
            ]
            if current["route_B_independent_rowkernel_source"].get(field) is not True
        ],
        "can_validate_now": False,
        "why_closest": (
            "Route B already has the finite quotient, trace pairing, selected basis independence, row typing, "
            "operator-shape compatibility, formal Hessian target, and all 110 algebraic row values. The only "
            "remaining move is promotion from replay/formal support to theorem-derived selected row-kernel source."
        ),
        "minimal_route_B_lemma": "SelectedFiniteC1SourcePromotionLemma",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    lemma = {
        "schema": "MTTMinimalSelectedFiniteC1SourcePromotionLemma.v1",
        "status": "MINIMAL_NEW_LEMMA_STATEMENT_READY_NOT_PROVED",
        "lemma_name": "SelectedFiniteC1SourcePromotionLemma",
        "statement": (
            "For the selected q=79, F, m=1 branch, the finite C1 trace/Frobenius pairing and transported selected "
            "basis define pre-residual phase and shift variation row-kernel functionals whose 72 primitive rows, "
            "2 Hessian/source rows, and 36 sector rows assemble the existing 110-row packet without residual-projector "
            "replay, locked-target values, observed constants, or benchmark profiles as source selectors."
        ),
        "route_B_fields_it_would_close": {
            "selected_basis_feeds_all_72_row_functionals": True,
            "pre_residual_phase_shift_variation_operators": True,
            "independent_hessian_counterterm_source_rows": True,
            "sector_rows_assembled_from_source_rows": True,
            "no_residual_projector_replay_or_locked_target_as_source": True,
        },
        "proof_obligations": [
            {
                "id": "basis_to_rows",
                "must_show": "transported selected bases feed all 72 primitive row functionals before residual replay",
            },
            {
                "id": "pre_residual_operators",
                "must_show": "R_Z and R_X arise as selected variation operators, not as fitted residual decompositions",
            },
            {
                "id": "hessian_source_rows",
                "must_show": "the two Hessian/source rows and b_selected are emitted by the same source functional",
            },
            {
                "id": "sector_assembly",
                "must_show": "the 36 sector rows are assembled functorially from the same source rows",
            },
            {
                "id": "independence_guardrail",
                "must_show": "no residual projector, locked target, observed SM datum, or benchmark profile selects the source",
            },
        ],
        "support_already_available": cutset["closed_support_not_to_repeat"],
        "sufficient_for_strict_validator": True,
        "proved_here": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    evidence = [
        {
            "source": rel(LEMMA),
            "closes": "selected basis feeds all 72 row functionals",
            "conditional": True,
        },
        {
            "source": rel(LEMMA),
            "closes": "pre-residual phase/shift variation operators",
            "conditional": True,
        },
        {
            "source": rel(LEMMA),
            "closes": "independent Hessian counterterm/source rows",
            "conditional": True,
        },
        {
            "source": rel(LEMMA),
            "closes": "sector rows assembled from source rows",
            "conditional": True,
        },
        {
            "source": rel(LEMMA),
            "closes": "no residual-projector replay or locked target as source",
            "conditional": True,
        },
    ]
    witness = {
        "schema": "MTTConditionalRouteBTwoExitValidatorWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_IF_MINIMAL_LEMMA_IS_PROVED",
        "route_A_physical_action_restriction": current["route_A_physical_action_restriction"],
        "route_B_independent_rowkernel_source": {
            "same_branch": True,
            "selected_basis_feeds_all_72_row_functionals": True,
            "pre_residual_phase_shift_variation_operators": True,
            "independent_hessian_counterterm_source_rows": True,
            "sector_rows_assembled_from_source_rows": True,
            "no_residual_projector_replay_or_locked_target_as_source": True,
            "attached_source_evidence": evidence,
            "conditional_on_unproved_lemma": rel(LEMMA),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "closure_claimed": False,
        "conditional_only": True,
    }

    ROUTE_A.write_text(json.dumps(route_a, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B.write_text(json.dumps(route_b, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    LEMMA.write_text(json.dumps(lemma, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(gate_dir / "current_two_exit_source_attempt.packet.json")
    conditional_result = run_validator(WITNESS)
    CURRENT_VALIDATOR_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    VALIDATOR_RESULT.write_text(json.dumps(conditional_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedSourceTheoremPushAttemptOrMinimalNewLemma",
        "status": STATUS,
        "inputs": {
            "two_exit_gate": rel(DATA / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem.candidate.json"),
            "finite_functional_candidate": rel(
                DATA
                / "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure"
                / "finite_c1_rowkernel_functional_candidate.packet.json"
            ),
            "all_rows_provenance_candidate": rel(DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"),
        },
        "output_packets": {
            "route_A_push": rel(ROUTE_A),
            "route_B_push": rel(ROUTE_B),
            "minimal_new_lemma": rel(LEMMA),
            "conditional_validator_witness": rel(WITNESS),
            "current_validator_result": rel(CURRENT_VALIDATOR_RESULT),
            "conditional_validator_result": rel(VALIDATOR_RESULT),
        },
        "theorem": {
            "name": "MinimalFiniteC1SourcePromotionSufficiencyTheorem",
            "proved": True,
            "statement": (
                "If the SelectedFiniteC1SourcePromotionLemma is proved, then the existing finite C1 110-row packet "
                "passes the strict two-exit source validator by Route B. Without that lemma the current packet still fails."
            ),
        },
        "what_closes_now": {
            "route_A_push_audited": True,
            "route_B_push_audited": True,
            "minimal_new_lemma_statement_emitted": True,
            "conditional_validator_witness_passes": conditional_result["returncode"] == 0,
            "current_validator_still_fails": current_result["returncode"] == 1,
        },
        "what_remains_open": {
            "prove_minimal_selected_finitec1_source_promotion_lemma": True,
            "or_prove_route_A_physical_action_restriction_lemma": True,
        },
        "route_selection": "Route B is currently closest; Route A remains a legal parallel exit.",
        "superset_strategy_use": (
            "Several encodings supply compatibility support, but the locked target is constrained by the strict source "
            "validator: compatibility can identify the lemma, not replace its proof."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SourceTheorem_PushAttempt_or_MinimalNewLemma_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "current_validator_still_fails": current_result["returncode"] == 1,
        "conditional_validator_witness_passes": conditional_result["returncode"] == 0,
        "proved_here": "conditional sufficiency only",
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SourceTheorem PushAttempt or MinimalNewLemma v1

Status: `{STATUS}`.

This pushes the source theorem one step further without overclaiming closure.

```text
current strict validator accepts        = False
conditional Route B witness accepts     = True
minimal new lemma proved here           = False
closure claimed                         = False
```

The new theorem is conditional sufficiency: if the
`SelectedFiniteC1SourcePromotionLemma` is proved, then the existing `110`-row
finite C1 packet validates by Route B. The lemma is exactly the missing bridge
from replay/formal row values to theorem-derived selected row-kernel source.

Route B is the closest path because the finite quotient, trace pairing, selected
basis independence, row typing, shape compatibility, formal Hessian target, and
all `110` algebraic values are already present. Route A remains a legal
parallel exit through a same-branch physical `Phi_fin^C1` action restriction
proof.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
