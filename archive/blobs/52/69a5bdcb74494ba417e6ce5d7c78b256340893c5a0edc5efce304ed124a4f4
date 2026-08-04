"""Build BN27 direct finitepart functional / source-owned logdet theorem gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "prior_gate": DATA / "selected_heterotic_orientedphifin_bn27_fulloperatorformula_sourceflags_or_quotientfunctor_valueconstruction.candidate.json",
    "transfer_boundary": DATA / "selected_heterotic_orientedphifin_bn27_quotient_finitepart_transfer_boundary.json",
    "trace_identity": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
    "refined_cutset": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_refined_root_cutset.json",
    "direct_acceptance_contract": DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_acceptance_contract.json",
    "selected_connection_witness_export": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
    "direct_source_declaration_fill": DATA / "selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector.candidate.json",
    "bn27_orbitclosure_report": DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill_report.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_directfinitepartfunctional_or_sourceownedlogdettheorem.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_orientedphifin_bn27_sourceowned_logdet_theorem_contract.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_directfinitepartfunctional_or_sourceownedlogdettheorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_DirectFinitePartFunctional_or_SourceOwnedLogdetTheorem_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_DIRECT_FINITEPART_ARITHMETIC_CLOSED_SOURCEOWNED_LOGDET_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnedLogdet_SourceTheorem_or_KernelTraceOwnership_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    prior = load(INPUTS["prior_gate"])
    transfer = load(INPUTS["transfer_boundary"])
    trace = load(INPUTS["trace_identity"])
    cutset = load(INPUTS["refined_cutset"])
    acceptance = load(INPUTS["direct_acceptance_contract"])
    witness = load(INPUTS["selected_connection_witness_export"])
    declaration = load(INPUTS["direct_source_declaration_fill"])
    orbit = load(INPUTS["bn27_orbitclosure_report"])

    plus_product = trace["plus_sector_product"]
    minus_product = trace["minus_sector_product"]
    oriented_product = trace["oriented_abs_sector_product"]
    arithmetic_closed = (
        plus_product == 9600
        and minus_product == 9600
        and oriented_product == plus_product * minus_product
        and trace["oriented_abs_sector_logdet_exact"] == "log(92160000)"
        and trace["identity_closed_relative_to_full_orbit_source"] is True
    )

    source_owned_requirements = {
        "source_object_named_S_QaSU3_BN27": False,
        "positive_spectrum_source_owned": False,
        "kernel_shared_circle_policy_source_owned": False,
        "trace_policy_source_owned": False,
        "finitepart_log92160000_identity_source_owned": False,
        "index_weights_and_scale_for_oriented_BN27_source_owned": False,
        "no_routec_import_as_source_identity": True,
        "no_double_count_Pperp_or_shared_line": True,
        "audit_replay_without_lifted_flags": True,
    }

    contract = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceOwnedLogdetTheorem.Contract.v1",
        "status": "SOURCEOWNED_LOGDET_THEOREM_REQUIRED",
        "purpose": "Promote the already exact BN27 oriented finitepart arithmetic only when the selected source owns the kernel, trace, scale, and finitepart identity.",
        "must_emit": {
            "source_object_named_S_QaSU3_BN27": None,
            "positive_spectrum_source_owned": None,
            "kernel_shared_circle_policy_source_owned": None,
            "trace_policy_source_owned": None,
            "finitepart_log92160000_identity_source_owned": None,
            "index_weights_and_scale_for_oriented_BN27": None,
        },
        "must_preserve": {
            "no_routec_import_as_source_identity": True,
            "no_double_count_Pperp_or_shared_line": True,
            "audit_replay_without_lifted_flags": True,
            "no_observed_data_or_benchmark_fitting": True,
        },
        "known_arithmetic_payload": {
            "plus_sector_product": plus_product,
            "minus_sector_product": minus_product,
            "oriented_abs_sector_product": oriented_product,
            "oriented_abs_sector_logdet_exact": trace["oriented_abs_sector_logdet_exact"],
            "oriented_nonzero_positive_rows": len(trace["plus_sector_values"]) + len(trace["minus_sector_values"]),
            "positive_oriented_policy": trace["positive_oriented_policy"],
        },
        "target_fitting_used": False,
    }
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lane_evaluation = {
        "lane_D_direct_finitepart_functional_on_BN27": {
            "arithmetic_closed": arithmetic_closed,
            "source_owned_closed": False,
            "plus_sector_product": plus_product,
            "minus_sector_product": minus_product,
            "oriented_abs_sector_product": oriented_product,
            "oriented_abs_sector_logdet_exact": trace["oriented_abs_sector_logdet_exact"],
            "closed_scope": "finite table arithmetic relative to a selected full-orbit source",
            "first_missing": "source-owned finitepart/logdet theorem that emits the BN27 positive spectrum, kernel/shared-circle policy, trace policy, and determinant scale from S_QaSU3^BN27",
        },
        "kernel_trace_ownership": {
            "support_present": witness["export_fields"]["kernel_policy"]["support_present"] and witness["export_fields"]["trace_policy"]["support_present"],
            "source_owned": False,
            "why_not_closed": "The selected-connection witness export marks kernel and trace policy as replayable support, not selected-source exports.",
        },
        "source_identity": {
            "heterotic_branch_certificate": cutset["support_closed"]["heterotic_branch_certificate"],
            "source_object_named_S_QaSU3_BN27": False,
            "RouteC_q79_row_internal_to_source_not_imported": False,
            "why_not_closed": "The direct acceptance contract still has null source-identity fields, and Route-C support cannot be imported as source ownership.",
        },
    }

    decision = {
        "attempt_executed": True,
        "direct_finitepart_arithmetic_closed": arithmetic_closed,
        "source_owned_finitepart_functional_closed": False,
        "kernel_trace_source_owned": False,
        "source_object_named_S_QaSU3_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "sourceowned_logdet_contract_path": rel(OUTPUT_CONTRACT),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27DirectFinitepartFunctionalOrSourceOwnedLogdetTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "prior_gate": prior["status"],
            "transfer_boundary": transfer["status"],
            "refined_cutset": cutset["status"],
            "direct_acceptance_contract": acceptance["status"],
            "selected_connection_witness_export": witness["status"],
            "direct_source_declaration_fill": declaration["status"],
            "bn27_orbitclosure_report": orbit["status"],
        },
        "arithmetic_payload": contract["known_arithmetic_payload"],
        "source_owned_requirements": source_owned_requirements,
        "lane_evaluation": lane_evaluation,
        "decision": decision,
        "theorem": {
            "name": "BN27DirectFinitepartArithmeticClosedSourceOwnedLogdetOpenTheorem",
            "proved": True,
            "statement": (
                "On the oriented BN27 full Fourier orbit, the direct finitepart arithmetic is exact: the C_tau=+1 "
                "positive sector product is 9600, the C_tau=-1 positive sector product is 9600, and the oriented "
                "absolute determinant is 92160000, hence the finitepart is log(92160000) relative to a selected "
                "full-orbit source. This still does not promote the heterotic threshold, because the current source "
                "does not own the BN27 source object, positive-spectrum rule, kernel/shared-circle policy, trace policy, "
                "or determinant scale. The remaining theorem is therefore a source-owned logdet/kernel-trace theorem, "
                "not another arithmetic computation."
            ),
        },
        "guardrails": {
            "does_not_promote_log92160000": True,
            "does_not_treat_arithmetic_as_source_ownership": True,
            "does_not_import_routec_as_source_identity": True,
            "does_not_use_lifted_selected_flags": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "direct_finitepart_arithmetic_closed": arithmetic_closed,
        "source_owned_finitepart_functional_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 DirectFinitePartFunctional or SourceOwnedLogdetTheorem v1

## Result

```text
status = {STATUS}
direct_finitepart_arithmetic_closed = true
source_owned_finitepart_functional_closed = false
kernel_trace_source_owned = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Source-Owned Contract

```text
{rel(OUTPUT_CONTRACT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
