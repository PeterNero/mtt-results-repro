"""Import the q79 selected K_CKM principle and isolate the remaining Pi trace rule."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_kckmtraceassemblyrule_or_oneprincipleckmclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
KERNEL_IMPORT = PACKET_DIR / "q79_selected_kckm_kernel_principle_import.packet.json"
SCOPE = PACKET_DIR / "kckm_trace_assembly_scope_separation.packet.json"
NEXT_GATE = PACKET_DIR / "pickm_closurecost_trace_functional_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_KCKMTraceAssemblyRule_or_OnePrincipleCKMClosure_v1.md"

PREVIOUS = DATA / "selected_eckmweightrowcertificates_or_ckmangleclosuredecision.candidate.json"
Q79_KERNEL_NOTE = (
    ROOT.parent
    / "mtt-q79-proof-repro"
    / "proof_corpus"
    / "Selected_Kernel_Principle_for_CKM_CP_in_MTT_v1.md"
)

STATUS = "MTT_SELECTED_KCKM_KERNEL_PRINCIPLE_IMPORTED_PI_TRACE_FUNCTIONAL_OPEN"
NEXT = "MTT_Selected_PiCKMClosureCostTraceFunctional_or_AngleWeightRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    if previous["status"] != "MTT_SELECTED_ECKM_WEIGHT_ROW_CERTIFICATE_ATTEMPT_EXECUTED_KCKM_RULE_OPEN":
        raise ValueError("previous E_CKM weight-row gate is not the current frontier")

    q79_text = Q79_KERNEL_NOTE.read_text(encoding="utf-8")
    required_strings = ["K_CKM^phys = K_sel", "E_CP", "J_sel(g)"]
    missing = [needle for needle in required_strings if needle not in q79_text]
    if missing:
        raise ValueError(f"q79 selected kernel principle note is missing markers: {missing}")

    kernel_import = {
        "schema": "MTTQ79SelectedKCKMKernelPrincipleImport.v1",
        "status": "Q79_SELECTED_KCKM_KERNEL_PRINCIPLE_IMPORTED_FOR_CP_SCOPE",
        "source_note": rel(Q79_KERNEL_NOTE),
        "source_markers_verified": required_strings,
        "imported_principle": "K_CKM^phys = K_sel at selected finite CP quotient scope",
        "selected_kernel_scope": "CP quotient / q79 phase kernel",
        "kernel_ownership_promoted": True,
        "does_not_emit_angle_magnitude_trace_rows": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    scope = {
        "schema": "MTTKCKMTraceAssemblyScopeSeparation.v1",
        "status": "KCKM_KERNEL_SELECTED_TRACE_ASSEMBLY_FOR_MAGNITUDES_STILL_OPEN",
        "closed_subclaim": {
            "selected_K_CKM_kernel_principle_available": True,
            "source": "q79 selected finite CP kernel principle",
            "scope": "CP phase/Jarlskog contact kernel ownership",
        },
        "not_closed_by_kernel_principle": {
            "selected_K_CKM_trace_assembly_rule_for_weights": False,
            "selected_Pi_CKM_12_row_certificate": False,
            "selected_Pi_CKM_23_row_certificate": False,
            "selected_Pi_CKM_13_row_certificate": False,
            "closure_cost_minimizer_evaluated_on_angle_projectors": False,
        },
        "reason": (
            "The selected-kernel principle identifies the physical CP kernel with the selected finite "
            "quotient kernel, but it does not specify the three sector-pair trace projectors or the "
            "closure-cost scalar functional whose traces are W12,W23,W13."
        ),
        "accepted_weight_rows": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_gate = {
        "schema": "MTTPiCKMClosureCostTraceFunctionalGate.v1",
        "status": "PICKM_CLOSURECOST_TRACE_FUNCTIONAL_REQUIRED",
        "next_required_artifact": NEXT,
        "remaining_object": (
            "Define and execute Pi_CKM^ij as selected sector-pair closure-cost projectors on K_sel, "
            "then certify Tr_N(Pi_CKM^ij K_sel)=W_ij without using observed CKM magnitudes as selectors."
        ),
        "must_emit": {
            "Pi_CKM^12": "row certificate for W12",
            "Pi_CKM^23": "row certificate for W23",
            "Pi_CKM^13": "row certificate for W13",
        },
        "allowed_source_inputs": [
            "selected q79/K_sel CP kernel principle",
            "selected Delta_v heavy-link packet",
            "selected orbit/lambda rows",
            "stationary zero-mode basis and Gram/trace convention",
            "finite Hessian/C1 sector contraction matrices M_u=M_e=R_Z, M_d=M_nuD=R_X",
        ],
        "forbidden_inputs": [
            "measured CKM angles as selectors",
            "choosing coefficients by residual minimization against W12,W23,W13",
            "promoting near-hit invariant scans without row certificates",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "KCKMKernelPrincipleScopeSeparationTheorem",
        "proved": True,
        "statement": (
            "The q79 selected-kernel theorem can be imported as source ownership for the CP-scope "
            "K_CKM kernel, but it does not by itself close the E_CKM angle-magnitude trace assembly. "
            "The final missing object is therefore narrower than before: a selected Pi_CKM closure-cost "
            "trace functional emitting the three W_ij row certificates."
        ),
    }

    data = {
        "candidate": "MTTSelectedKCKMTraceAssemblyRuleOrOnePrincipleCKMClosure",
        "status": STATUS,
        "inputs": {
            "previous_eckm_weight_gate": rel(PREVIOUS),
            "q79_selected_kernel_principle": rel(Q79_KERNEL_NOTE),
        },
        "output_packets": {
            "q79_selected_kckm_kernel_principle_import": rel(KERNEL_IMPORT),
            "kckm_trace_assembly_scope_separation": rel(SCOPE),
            "pickm_closurecost_trace_functional_gate": rel(NEXT_GATE),
        },
        "closure_decision": {
            "selected_K_CKM_kernel_principle_imported": True,
            "selected_K_CKM_trace_assembly_rule_for_weights_emitted": False,
            "selected_Pi_CKM_row_certificates": 0,
            "accepted_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "domain_readiness": "7/8 plus K_CKM CP-kernel ownership",
            "accepted_eckm_weight_rows": 0,
            "remaining_pi_row_certificates": 3,
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_KCKMTraceAssemblyRule_or_OnePrincipleCKMClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "selected_K_CKM_kernel_principle_imported": True,
        "selected_K_CKM_trace_assembly_rule_for_weights_emitted": False,
        "selected_Pi_CKM_row_certificates": 0,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected KCKMTraceAssemblyRule or OnePrincipleCKMClosure v1

Status: `{STATUS}`.

## Theorem

`KCKMKernelPrincipleScopeSeparationTheorem` is proved.

The q79 proof repo supplies the selected-kernel principle
`K_CKM^phys = K_sel` at CP-quotient scope. This imports real source ownership
for the CKM CP kernel, but it does not yet define the three angle-magnitude
projectors or their closure-cost trace rows.

```text
K_CKM CP-kernel ownership imported : true
accepted W rows                    : 0/3
remaining Pi_CKM row certificates  : 3
```

The remaining proof object is now sharper than the previous gate:

```text
Pi_CKM^ij closure-cost trace functional on K_sel
Tr_N(Pi_CKM^12 K_sel), Tr_N(Pi_CKM^23 K_sel), Tr_N(Pi_CKM^13 K_sel)
```

CKM angle closure and true SM equivalence are not claimed.

Next artifact: `{NEXT}`.
"""

    write_json(KERNEL_IMPORT, kernel_import)
    write_json(SCOPE, scope)
    write_json(NEXT_GATE, next_gate)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
