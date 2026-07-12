"""Build the minimal closing source-data request for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUT_A01 = DATA / "printed_a01_integrability_or_closure.candidate.json"
INPUT_MATRIX_HUNT = DATA / "selected_de_or_rhoe_matrix_source_hunt.candidate.json"
OUTPUT_DATA = DATA / "minimal_closing_source_data_request.candidate.json"
OUTPUT_CERT = CERTS / "minimal_closing_source_data_request_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Minimal_Closing_Source_Data_Request_v1.md"


def main() -> None:
    a01 = json.loads(INPUT_A01.read_text(encoding="utf-8"))
    hunt = json.loads(INPUT_MATRIX_HUNT.read_text(encoding="utf-8"))
    required_fields = {
        "source_identity": [
            "source certificate and branch id",
            "selection rule independent of Qa/SU3 residuals",
            "statement that no observed constants/masses/couplings are used",
        ],
        "typed_monad_maps": [
            "global typed f: K1 -> direct_sum_i L_i",
            "global typed g: direct_sum_i L_i -> K2",
            "basis or cochain representation for each nonzero charged entry",
            "machine-checkable g*f=0",
            "local-freeness and stability/HYM certificate",
        ],
        "operator_exit": [
            "D_E with principal symbol, connection data, endomorphism_E, and finite heat/spectrum/zeta/torsion object",
            "or rho_E with generator matrices, cocycle/metric compatibility, selected bundle origin, and validator pass",
            "or Cech/Dolbeault cochain matrices d0,d1 with d1*d0=0 plus selected finite response",
        ],
        "admissibility": [
            "Green-Schwarz/Bianchi check on the same branch",
            "Freed-Witten/gerbe check if using twisted modules",
            "projector retention and zero-mode policy",
            "trace normalization and representation choice",
        ],
    }
    forbidden_fields = [
        "target residual or observed constants as input",
        "generic existence of holomorphic maps without entries",
        "constant local-frame prose without transition/automorphy data",
        "printed A01 unless repaired and source-certified",
        "direct q79 finite torsion or rho_E import without same-branch map",
        "identity rho_E or scalar phase table as threshold operator",
    ]
    validator_plan = [
        "run validate_typed_monad_packet.py on the filled packet",
        "run A01/Maurer-Cartan integrability if a corrected A01 is supplied",
        "run rho_E/projective cocycle validator if finite transitions are supplied",
        "run heat/spectrum/zeta/torsion finite-part calculator from the same operator",
    ]
    candidate = {
        "candidate": "SelectedQaSU3MinimalClosingSourceDataRequest",
        "status": "MINIMAL_CLOSING_SOURCE_DATA_REQUEST_BUILT_CURRENT_CORPUS_OPEN",
        "input_statuses": {
            "printed_A01": a01["status"],
            "matrix_hunt": hunt["status"],
        },
        "required_fields": required_fields,
        "forbidden_fields": forbidden_fields,
        "validator_plan": validator_plan,
        "acceptance_result": {
            "current_corpus_satisfies_request": False,
            "printed_A01_rejected": a01["gate_results"]["integrability_fails"],
            "selected_matrix_source_missing": not hunt["gate_results"]["selected_matrix_source_found"],
            "qa_su3_packet_closed": False,
            "closure_claimed": False,
        },
        "minimal_new_source_text_needed": {
            "option_A_corrected_A01_DE": "Print a corrected integrable A01/D_E matrix, its selection rule, endomorphism_E, and finite response.",
            "option_B_typed_monad_sections": "Print the typed section/cochain bases and exact f,g maps with g*f=0, then derive D_E/rho_E.",
            "option_C_twisted_rhoE": "Print the selected gerbe/twisted rho_E cocycle, projector retention, and finite determinant response.",
        },
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3MinimalClosingSourceDataRequest",
        "status": "QA_SU3_MINIMAL_CLOSING_SOURCE_DATA_REQUEST_BUILT_CURRENT_CORPUS_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "minimal_required_source_packet_specified": True,
            "forbidden_shortcuts_specified": True,
            "printed_A01_rejection_included": True,
            "validator_plan_specified": True,
        },
        "what_remains_open": {
            "filled_source_packet": True,
            "selected_D_E_or_rho_E_or_cochain_finite_response": True,
            "qa_su3_packet_closed": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = """# Selected Qa/SU3 Minimal Closing Source Data Request v1

This is the exact closing packet now required by the proof program.

## Required

1. Source identity: selected branch, source certificate, and a selection rule not
   using observed constants or Qa/SU3 residuals.
2. Typed monad maps: global typed `f,g` entries, bases/cochains for charged
   entries, `g*f=0`, local-freeness, and stability/HYM.
3. Operator exit: same-source `D_E`, `rho_E`, or Cech/Dolbeault finite response.
4. Admissibility: Bianchi, Freed-Witten/gerbe if twisted, projector retention,
   trace normalization, representation, and zero-mode policy.

## Current Corpus Result

The current corpus does not fill this request.  The printed `A01` matrix is
rejected by the integrability audit, and no selected same-branch `D_E/rho_E`
matrix source is printed.

## Minimal Ways to Close

```text
A. corrected source-certified A01/D_E matrix + finite response
B. typed section/cochain bases and exact f,g with g*f=0, then D_E/rho_E
C. selected gerbe/twisted rho_E cocycle + finite determinant response
```

closure claimed: no
target fitting used: no
"""
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
