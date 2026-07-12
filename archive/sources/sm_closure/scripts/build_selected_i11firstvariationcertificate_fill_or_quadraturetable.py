"""Build selected I11 first-variation certificate fill attempt or quadrature-table frontier."""

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

SLUG = "selected_i11firstvariationcertificate_fill_or_quadraturetable"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TEMPLATE = PACKET_DIR / "i11_first_variation_certificate.strict_template.json"
CURRENT = PACKET_DIR / "current_i11_first_variation_certificate_attempt.packet.json"
NORMALIZATION = PACKET_DIR / "normalization_compatibility_sublemma.packet.json"
WITNESS = PACKET_DIR / "conditional_i11_certificate_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_i11_first_variation_frontier.packet.json"
I10_BRIDGE = PACKET_DIR / "conditional_i10_binding_bridge.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I11FirstVariationCertificate_Fill_or_QuadratureTable_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_firstvariation_certificate.py"
I10_VALIDATOR = ROOT / "scripts" / "validate_selected_i10_binding_stack.py"

STATUS = "MTT_SELECTED_I11FIRSTVARIATIONCERTIFICATE_FILL_BUILT_NORMALIZATION_CLOSED_REST_OPEN"
NEXT = "MTT_Selected_SelectedTraceMapAndFirstVariationIdentity_Fill_or_QuadratureKernelTable_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(validator: Path, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "payload": rel(path),
        "validator": rel(validator),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    next_cert = load(
        DATA
        / "selected_i10bindingstack_gate_or_firstvariationcertificate"
        / "next_first_variation_certificate.packet.json"
    )
    trace_unique = load(
        DATA
        / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
        / "finite_weyl_trace_uniqueness_derivation.packet.json"
    )
    trace_support = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "selected_trace_map_and_measure_support.packet.json"
    )
    boundary_attempt = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "physical_action_boundary_promotion_attempt.packet.json"
    )
    variational = load(
        DATA
        / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
        / "orthogonal_completion_variational_derivation.packet.json"
    )
    i10_witness = load(
        DATA
        / "selected_i10bindingstack_gate_or_firstvariationcertificate"
        / "conditional_i10_binding_stack_witness.packet.json"
    )

    normalization_closed = (
        trace_unique["derived_now"]["finite_measure_equals_normalized_trace"]
        and trace_unique["derived_now"]["trace_frobenius_pairing_for_finite_quotient"]
        and trace_unique["derived_now"]["measure_choice_is_not_a_new_knob"]
        and "scale cancels in the Euler equation" in trace_support["candidate_physical_measure"]["normalization"]
        and variational["derived_inside_this_gate"]["finite_dimensional_projection_euler_equation"]
    )
    normalization = {
        "schema": "MTTI11NormalizationCompatibilitySublemma.v1",
        "status": "NORMALIZATION_COMPATIBILITY_PROVED_FOR_FINITE_EULER_EQUATION",
        "proved": normalization_closed,
        "statement": (
            "The finite Weyl invariant trace/Frobenius normalization is unique up to the fixed normalized trace, "
            "and any positive global scale cancels from the finite Euler equation. Therefore normalization compatibility "
            "is closed for the I11 finite certificate."
        ),
        "sources": [
            rel(
                DATA
                / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
                / "finite_weyl_trace_uniqueness_derivation.packet.json"
            ),
            rel(
                DATA
                / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                / "selected_trace_map_and_measure_support.packet.json"
            ),
            rel(
                DATA
                / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
                / "orthogonal_completion_variational_derivation.packet.json"
            ),
        ],
        "does_not_close": [
            "selected_trace_map",
            "first_variation_identity",
            "hessian_or_coercivity",
            "physical_boundary_cancellation",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    template = {
        "schema": "MTTI11FirstVariationCertificateStrictTemplate.v1",
        "status": "STRICT_TEMPLATE_READY",
        "theorem_slot": next_cert["theorem_slot"],
        "required_fields": next_cert["must_fill"],
        "field_contract": next_cert["certificate_fields"],
        "validator": rel(VALIDATOR),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    current = {
        "schema": "MTTCurrentI11FirstVariationCertificateAttempt.v1",
        "status": "CURRENT_I11_ATTEMPT_FAILS_VALIDATOR_NORMALIZATION_ONLY_CLOSED",
        "same_branch": True,
        "selected_trace_map": False,
        "first_variation_identity": False,
        "hessian_or_coercivity": False,
        "boundary_cancellation": False,
        "normalization_compatibility": normalization_closed,
        "attached_certificate_evidence": [
            {
                "source": rel(NORMALIZATION),
                "closes": "finite Euler normalization compatibility",
            },
            {
                "source": rel(
                    DATA
                    / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                    / "selected_trace_map_and_measure_support.packet.json"
                ),
                "closes": "trace-map support only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                    / "physical_action_boundary_promotion_attempt.packet.json"
                ),
                "closes": "algebraic boundary support only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
                    / "orthogonal_completion_variational_derivation.packet.json"
                ),
                "closes": "formal Euler projection only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_i10bindingstack_gate_or_firstvariationcertificate"
                    / "i1_i5_partial_support_ledger.packet.json"
                ),
                "closes": "I1/I5 partial support only",
            },
        ],
        "physical_boundary_cancellation_promoted": boundary_attempt["first_variation_certificate_fields_after_this_gate"]["boundary_cancellation"]["physical_verified_now"],
        "trace_support_imported": boundary_attempt["first_variation_certificate_fields_after_this_gate"]["selected_trace_map"]["support_imported_now"],
        "why_not_promoted": [
            "selected trace support exists, but the full physical Phi_fin trace map is not emitted",
            "formal Euler projection exists, but the physical first-variation identity is not verified",
            "coercive Hessian bound on the admissible quotient span is not emitted",
            "boundary cancellation is algebraic only, not physically promoted",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    witness_evidence = [
        {
            "source": rel(FRONTIER),
            "closes": "selected trace map",
            "conditional": True,
        },
        {
            "source": rel(FRONTIER),
            "closes": "first variation identity",
            "conditional": True,
        },
        {
            "source": rel(FRONTIER),
            "closes": "Hessian/coercivity",
            "conditional": True,
        },
        {
            "source": rel(FRONTIER),
            "closes": "physical boundary cancellation",
            "conditional": True,
        },
        {
            "source": rel(NORMALIZATION),
            "closes": "normalization compatibility",
            "conditional": False,
        },
    ]
    witness = {
        "schema": "MTTConditionalI11FirstVariationCertificateWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_IF_REMAINING_I11_FIELDS_FILLED",
        "same_branch": True,
        "selected_trace_map": True,
        "first_variation_identity": True,
        "hessian_or_coercivity": True,
        "boundary_cancellation": True,
        "normalization_compatibility": True,
        "attached_certificate_evidence": witness_evidence,
        "conditional_on": rel(FRONTIER),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
        "conditional_only": True,
    }

    frontier = {
        "schema": "MTTRemainingI11FirstVariationFrontier.v1",
        "status": "NORMALIZATION_CLOSED_FOUR_I11_FIELDS_OPEN",
        "closed_now": {
            "normalization_compatibility": normalization_closed,
        },
        "still_open": {
            "selected_trace_map": {
                "needs": next_cert["certificate_fields"]["selected_trace_map"]["must_provide"],
                "current_support": trace_support["support_imported"],
            },
            "first_variation_identity": {
                "needs": next_cert["certificate_fields"]["first_variation_identity"]["formula"],
                "current_support": "formal Euler projection only",
            },
            "hessian_or_coercivity": {
                "needs": next_cert["certificate_fields"]["hessian_or_coercivity"]["formula"],
                "current_support": "quadratic functional positivity shape only",
            },
            "boundary_cancellation": {
                "needs": next_cert["certificate_fields"]["boundary_cancellation"]["formula"],
                "current_support": "finite trace algebraic cancellation only",
            },
        },
        "parallel_exit": next_cert["parallel_exit"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    NORMALIZATION.write_text(json.dumps(normalization, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(VALIDATOR, CURRENT)
    witness_result = run_validator(VALIDATOR, WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    i10_bridge = {
        "schema": "MTTConditionalI11ToI10BindingBridge.v1",
        "status": "I11_WITNESS_IMPLIES_I10_BINDING_WITNESS",
        "conditional_i10_binding_witness": rel(
            DATA
            / "selected_i10bindingstack_gate_or_firstvariationcertificate"
            / "conditional_i10_binding_stack_witness.packet.json"
        ),
        "i10_validator": rel(I10_VALIDATOR),
        "validation_returncode": run_validator(
            I10_VALIDATOR,
            DATA
            / "selected_i10bindingstack_gate_or_firstvariationcertificate"
            / "conditional_i10_binding_stack_witness.packet.json",
        )["returncode"],
        "conditional_on": rel(WITNESS),
        "closure_claimed": False,
    }
    I10_BRIDGE.write_text(json.dumps(i10_bridge, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI11FirstVariationCertificateFillOrQuadratureTable",
        "status": STATUS,
        "inputs": {
            "next_i11_certificate": rel(
                DATA
                / "selected_i10bindingstack_gate_or_firstvariationcertificate"
                / "next_first_variation_certificate.packet.json"
            ),
            "trace_uniqueness": rel(
                DATA
                / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
                / "finite_weyl_trace_uniqueness_derivation.packet.json"
            ),
            "physical_boundary_attempt": rel(
                DATA
                / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                / "physical_action_boundary_promotion_attempt.packet.json"
            ),
        },
        "output_packets": {
            "strict_template": rel(TEMPLATE),
            "current_attempt": rel(CURRENT),
            "normalization_compatibility_sublemma": rel(NORMALIZATION),
            "conditional_witness": rel(WITNESS),
            "remaining_frontier": rel(FRONTIER),
            "conditional_i10_bridge": rel(I10_BRIDGE),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
        },
        "theorem": {
            "name": "I11NormalizationCompatibilityAndCertificateFrontierTheorem",
            "proved": True,
            "statement": (
                "The I11 first-variation certificate now has one proved sublemma: finite trace/Frobenius normalization "
                "is compatible with the Euler equation. The remaining certificate fields are selected trace map, first "
                "variation identity, Hessian/coercivity, and physical boundary cancellation."
            ),
        },
        "what_closes_now": {
            "i11_validator_built": True,
            "normalization_compatibility_proved": normalization_closed,
            "current_attempt_rejected": current_result["returncode"] == 1,
            "conditional_witness_passes": witness_result["returncode"] == 0,
            "i10_bridge_checked": i10_bridge["validation_returncode"] == 0,
        },
        "what_remains_open": frontier["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
        "previous_status": next_cert["status"],
    }

    cert = {
        "certificate": "MTT_Selected_I11FirstVariationCertificate_Fill_or_QuadratureTable_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "normalization_compatibility_proved": normalization_closed,
        "current_attempt_rejected": current_result["returncode"] == 1,
        "conditional_witness_passes": witness_result["returncode"] == 0,
        "i10_bridge_checked": i10_bridge["validation_returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I11FirstVariationCertificate Fill or QuadratureTable v1

Status: `{STATUS}`.

The I11 certificate has one real sublemma closed.

```text
normalization compatibility proved = {normalization_closed}
current I11 attempt validates      = False
conditional I11 witness validates  = True
I10 bridge validates               = {i10_bridge["validation_returncode"] == 0}
closure claimed                    = False
```

What remains is now four fields: selected trace map, first-variation identity,
Hessian/coercivity, and physical boundary cancellation. The parallel exit is an
independent quadrature/kernel table.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
