"""Build the next heterotic Phi_fin source-identity / bundle solve gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUT_ATTEMPT = DATA / "selected_heterotic_phifin_direct_operator_emission_attempt.candidate.json"
INPUT_RPLUS = DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json"
INPUT_MONAD = DATA / "ext_stability_source_search.candidate.json"
OUTPUT_DATA = DATA / "selected_heterotic_phifin_sourceidentity_or_bundleconnection_solve_gate.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_phifin_sourceidentity_or_bundleconnection_solve_gate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_PhiFin_SourceIdentity_or_BundleConnection_Solve_Gate_v1.md"

STATUS = "HETEROTIC_PHIFIN_SOURCEIDENTITY_OR_BUNDLECONNECTION_SOLVE_GATE_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_BundleConnection_ValueSolve_or_PhiFin_SourceIdentity_Proof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    attempt = load(INPUT_ATTEMPT)
    rplus = load(INPUT_RPLUS)
    monad = load(INPUT_MONAD)["monad_computation"]

    lane_a_source_identity = {
        "name": "PhiFin_source_identity_theorem",
        "goal": (
            "prove that the selected rank-three Iwasawa SU(3) monad/End(E) "
            "threshold branch emits the same finite Phi_fin packet whose 27-mode "
            "D_E/Riesz/Green layer is already selected in the Route-C ladder"
        ),
        "required_subclaims": {
            "same_branch_source_certificate": False,
            "monad_EndE_to_BN_functor": False,
            "rho_E_or_transition_data_nonidentity": False,
            "commuting_projection_to_27mode_basis": False,
            "D_E_trace_equality_on_QaSU3_domain": False,
            "Riesz_Green_gap_preserved": True,
            "trace_weights_and_threshold_convention": False,
            "finite_part_regularization": False,
        },
        "currently_importable": [
            "selected monad topology c1=0,c2=0,c3=6",
            "selected R+ geometric curvature block",
            "U1/Y Route-C selected 27-mode D_E/Riesz/Green support",
        ],
        "closes_now": False,
    }

    lane_b_bundle_solve = {
        "name": "explicit_selected_bundle_connection_solve",
        "goal": (
            "solve or source-emit the selected heterotic Qa/SU3 bundle connection "
            "and finite threshold operator directly, without importing the U1/Y "
            "Phi_fin packet as proof"
        ),
        "required_payload": {
            "A_components_or_rho_E": False,
            "F_A_components": False,
            "HYM_or_Strominger_residual_certificate": False,
            "representation_action_on_uE_one_forms": False,
            "Weitzenbock_E_Qa_matrix": False,
            "kernel_and_quotient_policy": False,
            "positive_spectrum_or_gap": False,
            "heat_zeta_torsion_finite_part": False,
            "trace_normalization": False,
        },
        "known_geometric_inputs": {
            "R_plus_summary": rplus["rplus_payload"]["R_plus_summary"],
            "monad_topology": {
                "rank": 3,
                "c1_zero": monad["c1_zero"],
                "c2_zero": monad["c2_zero"],
                "c3_integral": monad["c3_integral"],
                "c3_integral_equals_6": monad["c3_integral_equals_6"],
            },
        },
        "closes_now": False,
    }

    acceptance_kernel = {
        "forbidden": [
            "identity rho_E smoke",
            "standard embedding A=GammaPlus without a selector",
            "U1/Y 27-mode gap support promoted as heterotic threshold",
            "Chern classes alone as operator data",
            "observed electroweak constants or residual target scans",
        ],
        "success_if_any_lane": [
            "Lane A proves all source-identity subclaims and exports selected rho_E/D_E/Riesz/Green/E_Qa/finite-part data",
            "Lane B emits an explicit selected bundle connection/operator payload with residual, quotient, spectrum, and finite part",
        ],
    }

    candidate = {
        "candidate": "SelectedHeteroticPhiFinSourceIdentityOrBundleConnectionSolveGate",
        "status": STATUS,
        "inputs": {
            "phifin_attempt": rel(INPUT_ATTEMPT),
            "rplus": rel(INPUT_RPLUS),
            "monad": rel(INPUT_MONAD),
        },
        "input_statuses": {
            "phifin_attempt": attempt["status"],
            "rplus": rplus["status"],
            "monad": load(INPUT_MONAD)["status"],
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "lanes": {
            "A_source_identity": lane_a_source_identity,
            "B_explicit_bundle_solve": lane_b_bundle_solve,
        },
        "acceptance_kernel": acceptance_kernel,
        "decision": {
            "source_identity_gate_built": True,
            "explicit_bundle_solve_gate_built": True,
            "same_source_identity_proved": False,
            "explicit_bundle_connection_solved": False,
            "direct_finite_operator_emitted": False,
            "E_Qa_computed": False,
            "computed_threshold_value": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "guardrails": {
            "promotes_gap_support_as_threshold": False,
            "promotes_standard_embedding_without_selector": False,
            "promotes_chern_classes_as_operator": False,
            "promotes_identity_rhoE_smoke": False,
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "HeteroticPhiFinSourceIdentityOrBundleConnectionSolveAcceptanceTheorem",
            "proved": True,
            "statement": (
                "After importing finite Route-C gap support without promotion, the "
                "heterotic Qa/SU3 threshold can close only by proving a same-source "
                "Phi_fin identity for the selected monad/End(E) branch or by emitting "
                "an explicit selected bundle connection/operator payload. This gate "
                "fixes the acceptance kernel and forbids identity rho_E smoke, "
                "unselected standard embedding, Chern-class-only promotion, and target fitting."
            ),
        },
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "source_identity_gate_built": True,
        "explicit_bundle_solve_gate_built": True,
        "same_source_identity_proved": False,
        "explicit_bundle_connection_solved": False,
        "direct_finite_operator_emitted": False,
        "E_Qa_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic PhiFin SourceIdentity or BundleConnection Solve Gate v1

## Result

```text
status = {STATUS}
same_source_identity_proved = false
explicit_bundle_connection_solved = false
direct_finite_operator_emitted = false
E_Qa_computed = false
next_required_artifact = {NEXT}
```

## Lane A: Source Identity

```json
{json.dumps(lane_a_source_identity["required_subclaims"], indent=2, sort_keys=True)}
```

## Lane B: Explicit Bundle Solve

```json
{json.dumps(lane_b_bundle_solve["required_payload"], indent=2, sort_keys=True)}
```

## Acceptance Kernel

```json
{json.dumps(acceptance_kernel, indent=2, sort_keys=True)}
```

This artifact closes no physical threshold value. It makes the next executable
step precise: either prove the same-source `Phi_fin` identity for the selected
monad/`End(E)` branch, or emit the selected bundle connection/operator directly.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
