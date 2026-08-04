"""Audit the primitive C1 source-value theorem / noninvariant tensor gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor_certificate.json"
CONTRACT = REPO / "candidate_data" / "selected_u1y_routec_primitive_c1_sourcevalue_closure_contract.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Primitive_C1_SourceValue_Theorem_or_NonInvariantTensor_v1.md"

STATUS = "U1Y_ROUTEC_PRIMITIVE_C1_SOURCEVALUE_THEOREM_OR_NONINVARIANT_TENSOR_GATE_BUILT_OPEN"
NEXT = "Selected_U1Y_RouteC_CanonicalZeroSelection_or_NonInvariantC1Tensor_Fill_v1"


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
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    guards = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("contract built", cert["sourcevalue_contract_built"] is True and contract["status"] == "OPEN_SOURCE_VALUE_THEOREM_REQUIRED", contract["status"]),
        check("canonical zero not selected", cert["canonical_zero_diagnostic_imported"] is True and contract["canonical_zero_selection"]["currently_closed"] is False, contract["canonical_zero_selection"]),
        check("noninvariant primary", cert["noninvariant_tensor_route_kept_primary"] is True and data["route_ranking"][0]["route"] == "selected_noninvariant_tensor", data["route_ranking"]),
        check("typed route live", cert["typed_connection_derivation_route_kept_live"] is True and contract["typed_connection_derivation"]["currently_closed"] is False, contract["typed_connection_derivation"]),
        check("missing count carried", cert["missing_leaf_count"] == 40 and data["missing_leaf_counts"]["primitive_c1_atom_matrix"] == 24, data["missing_leaf_counts"]),
        check("no downstream computation", cert["A_selected_computable"] is False and cert["b_selected_computable"] is False and cert["lambda_12_computable"] is False, cert),
        check("guardrails hold", all(value is False for value in guards.values()) and data["target_fitting_used"] is False, guards),
        check("note records route consequence", "If canonical zero is selected" in note and "noninvariant tensor route" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C primitive C1 source-value theorem/noninvariant tensor audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
