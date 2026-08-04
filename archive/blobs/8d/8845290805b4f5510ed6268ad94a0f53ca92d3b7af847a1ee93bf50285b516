"""Audit the U1/Y Route-C selected source certificate or typed D_E gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_selected_source_certificate_or_typed_de_construction.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SelectedSourceCertificate_or_TypedDEConstruction_v1.md"

STATUS = "U1Y_ROUTEC_SELECTED_SOURCE_OR_TYPED_DE_REDUCED_CONNECTION_WITNESS_OPEN"
NEXT = "Selected_U1Y_RouteC_TypedMonadCech_or_HYMConnectionWitness_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    reduction = data["reduction"]
    guardrails = data["guardrails"]
    finite = reduction["finite_connection_prefix"]
    witness = reduction["q79_witness_search"]
    audit_checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("q79 source reduction imported", reduction["q79_source_or_typed_DE_reduction"]["status"] == "Q79_ROUTEC_SELECTED_SOURCE_OR_TYPED_DE_CONSTRUCTION_OPEN_WITNESS_CONTRACT_CREATED", reduction["q79_source_or_typed_DE_reduction"]["status"]),
        check("q79 witness absent", decision["selected_connection_witness_values_absent"] is True and witness["selected_D_E_source_found"] is False, witness),
        check("smoke rejected", decision["identity_rhoE_smoke_promoted"] is False and witness["routec_smoke_promotion_nogo"]["status"] == "CANNOT_PROMOTE_SMOKE_TO_SELECTED_WITNESS" and witness["routec_smoke_promotion_nogo"]["verdict"]["constructs_selected_connection_witness"] is False, witness["routec_smoke_promotion_nogo"]),
        check("finite prefix present", decision["finite_connection_prefix_values_present"] is True and finite["DE"]["D_E_matrix_on_27_mode_BN_emitted"] is True and finite["dotD"]["dotD_alpha1_matrix_in_same_basis_emitted"] is True, finite["status"]),
        check("C1 engine not C1 values", finite["C1"]["primitive_C1_contraction_engine_built"] is True and decision["primitive_C1_values_computed"] is False, finite["C1"]),
        check("no source closure", decision["selected_routec_source_certificate_closed"] is False and decision["typed_DE_construction_closed"] is False and decision["selected_finite_connection_solve_closed"] is False, decision),
        check("no downstream closure", data["closure_claimed"] is False and decision["A_selected_or_b_selected_emitted"] is False and decision["lambda_12_computable"] is False, decision),
        check("guardrails", guardrails["promotes_diagnostic_selected_flags"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents witness", "Missing Witness Values" in note and "Do not promote finite prefix values" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C selected source or typed D_E audit")
    return 0 if all(audit_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
