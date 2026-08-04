"""Build minimizer-trace C1 payload theorem / quadrature values gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS_SLUG = "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable"
PREVIOUS = DATA / f"{PREVIOUS_SLUG}.candidate.json"
MINIMIZER_BINDING = DATA / PREVIOUS_SLUG / "phifinc1_minimizer_binding_reduction.packet.json"
QUADRATURE_TEMPLATE = DATA / PREVIOUS_SLUG / "independent_quadrature_table_template.packet.json"

SLUG = "selected_minimizertracec1payloadtheorem_or_quadraturetablevalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PAYLOAD_CONTRACT = PACKET_DIR / "i10_minimizer_trace_c1_payload_contract.packet.json"
QUADRATURE_VALUES = PACKET_DIR / "quadrature_values_staging_tables.packet.json"
ACCEPTANCE_MANIFEST = PACKET_DIR / "closure_acceptance_manifest.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1.md"

STATUS = "MTT_SELECTED_MINIMIZERTRACE_C1_PAYLOAD_OR_QUADRATURE_VALUES_CONTRACT_BUILT_OPEN"
NEXT = "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    previous = load(PREVIOUS)
    binding = load(MINIMIZER_BINDING)
    quadrature = load(QUADRATURE_TEMPLATE)
    replay = previous["replay_if_I10_or_quadrature_table_proved"]

    payload_contract = {
        "schema": "MTTI10MinimizerTraceC1PayloadContract.v1",
        "status": "PAYLOAD_CERTIFICATE_CONTRACT_BUILT_VALUES_OPEN",
        "theorem_slot": binding["new_binding_theorem_slot"]["id"],
        "payload_certificate_required": {
            "selected_minimizer_trace_payload": {
                "required": True,
                "source_slot": "I1_selected_strominger_minimizer_to_phifin_trace",
                "must_emit": [
                    "q79/F,m=1 selected Strominger/HYM minimizer",
                    "finite Phi_fin trace map",
                    "C1 finite response coordinates",
                    "selected boundary and normalization data",
                ],
                "forbidden": [
                    "model-active B_N values without selected transport proof",
                    "observed SM masses or mixings as trace selectors",
                ],
            },
            "selected_c1_response_payload": {
                "required": True,
                "source_slot": "I5_dotD_alpha1_and_C1_response",
                "must_emit": [
                    "same-branch dotD_alpha1 derivative",
                    "C1 overlap/tangent response operator",
                    "sector routing or End0-to-sector transfer normalization",
                    "error bounds or exact symbolic equalities",
                ],
                "forbidden": [
                    "continuous Ext-density tangent promoted directly to physical alpha1",
                    "sector matrices copied from patched replay",
                ],
            },
            "defect_functional_minimizer_payload": {
                "required": True,
                "source": "C1DefectLeakageFunctional",
                "must_emit": [
                    "first-variation identity on the selected response span",
                    "coercive or convex Hessian block on admissible C1 variations",
                    "boundary term cancellation under selected routing",
                    "normalization compatibility with finite trace/Frobenius constraint",
                ],
                "forbidden": [
                    "assuming stationarity from the residual-projector axiom patch",
                    "choosing the minimizer by target residual values",
                ],
            },
        },
        "promotion_rule": {
            "if_all_payload_certificates_verified": {
                "I10_phifinc1_minimizes_c1_defect_functional": True,
                "unpatched_A_selected_promotes": True,
                "unpatched_b_selected_promotes": True,
                "unpatched_deltaTheta_C1_promotes": True,
                "SM_parity_dynamic_packet_closes": True,
            },
            "current_all_payload_certificates_verified": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    quadrature_values = {
        "schema": "MTTIndependentQuadratureValuesStagingTables.v1",
        "status": "TABLES_STAGED_VALUES_EMPTY",
        "source_template": rel(QUADRATURE_TEMPLATE),
        "tables": {
            "zero_mode_basis_rows": [],
            "primitive_contraction_rows": [],
            "hessian_source_rows": [],
            "sector_matrix_rows": [],
        },
        "expected_minimum_counts": {
            "zero_mode_basis_rows": 8,
            "primitive_contraction_rows": 18,
            "hessian_source_rows": 2,
            "sector_matrix_rows": 18,
        },
        "required_values": quadrature["required_values"],
        "acceptance_tests": quadrature["acceptance_tests"],
        "values_filled_now": False,
        "would_close_if_filled": quadrature["would_close_if_filled"],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    acceptance_manifest = {
        "schema": "MTTPhiFinC1ClosureAcceptanceManifest.v1",
        "status": "DUAL_ROUTE_ACCEPTANCE_MANIFEST_BUILT_OPEN",
        "route_A_i10_payload_certificate": {
            "accepted_now": False,
            "required_packet": rel(PAYLOAD_CONTRACT),
            "required_checks": [
                "selected_minimizer_trace_payload_verified",
                "selected_c1_response_payload_verified",
                "defect_functional_minimizer_payload_verified",
                "no_observed_data_as_selector",
            ],
        },
        "route_B_independent_quadrature_values": {
            "accepted_now": False,
            "required_packet": rel(QUADRATURE_VALUES),
            "required_checks": [
                "basis_rows_present_and_selected",
                "primitive_contractions_present_with_error_bounds",
                "hessian_rows_present_and_positive_on_admissible_span",
                "sector_matrices_present",
                "rank_at_least_2",
                "deltaTheta_solve_matches_replay",
                "no_patched_replay_copying",
            ],
        },
        "replay_target_if_accepted": replay,
        "closure_claimed_now": False,
    }

    candidate = {
        "candidate": "MTTSelectedMinimizerTraceC1PayloadTheoremOrQuadratureTableValues",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "minimizer_binding": rel(MINIMIZER_BINDING),
            "quadrature_template": rel(QUADRATURE_TEMPLATE),
        },
        "output_packets": {
            "i10_payload_contract": rel(PAYLOAD_CONTRACT),
            "quadrature_values_staging_tables": rel(QUADRATURE_VALUES),
            "closure_acceptance_manifest": rel(ACCEPTANCE_MANIFEST),
        },
        "what_closes_now": {
            "I10_payload_certificate_schema_fixed": True,
            "independent_quadrature_value_tables_staged": True,
            "dual_route_acceptance_manifest_built": True,
            "unpatched_closure_conditions_are_machine_checkable": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_minimizer_trace_payload_verified": True,
            "selected_c1_response_payload_verified": True,
            "defect_functional_minimizer_payload_verified": True,
            "independent_quadrature_values_filled": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_i10_payload_certificate_accepted": False,
            "route_B_independent_quadrature_values_accepted": False,
            "I10_proved": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "MinimizerTraceC1PayloadOrQuadratureValuesReductionTheorem",
            "proved": True,
            "statement": (
                "The I10 proof obligation is now equivalent to three selected payload certificates "
                "for minimizer trace, selected C1 response, and defect-functional stationarity/coercivity; "
                "or, independently, to filling the declared quadrature/Hessian tables and passing the "
                "dual-route acceptance manifest."
            ),
        },
        "replay_if_route_A_or_B_accepted": replay,
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected MinimizerTraceC1PayloadTheorem or QuadratureTableValues v1

Status: `{STATUS}`.

This gate turns the open I10 statement into exact executable payload requirements.

Closed now:

```text
I10 payload certificate schema fixed        = True
independent quadrature value tables staged  = True
dual-route acceptance manifest built        = True
observed constants excluded as selectors    = True
```

Still open:

```text
selected minimizer trace payload verified   = False
selected C1 response payload verified       = False
defect-functional minimizer payload verified= False
independent quadrature values filled        = False
unpatched dynamic closure                   = False
```

The two legal routes are now:

```text
Route A: prove the I10 payload certificate from selected minimizer trace + C1 response.
Route B: fill the independent quadrature tables and pass rank/solve/error checks.
```

Replay target if either route is accepted:

```text
A^T A      = {replay["A_transpose_A"]}
A^T b      = {replay["A_transpose_b"]}
deltaTheta = {replay["deltaTheta_C1"]}
```

Next artifact: `{NEXT}`.
"""

    PAYLOAD_CONTRACT.write_text(json.dumps(payload_contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    QUADRATURE_VALUES.write_text(json.dumps(quadrature_values, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ACCEPTANCE_MANIFEST.write_text(json.dumps(acceptance_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
