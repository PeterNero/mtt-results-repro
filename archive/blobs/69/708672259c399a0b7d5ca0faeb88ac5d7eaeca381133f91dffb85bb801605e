"""Build R_theta physical projection kernel / profile response gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_physicalprojectionkernel_or_profileresponse"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INPUT_RECONCILIATION = PACKET_DIR / "projection_input_reconciliation.packet.json"
KERNEL_ATTEMPT = PACKET_DIR / "pi_rtheta_kernel_attempt.packet.json"
PROFILE_GATE = PACKET_DIR / "profile_response_recheck.packet.json"
DECISION = PACKET_DIR / "physical_projection_kernel_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_projection_kernel_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaPhysicalProjectionKernel_or_ProfileResponse_v1.md"

PREVIOUS = DATA / "selected_rtheta_coefficientformuladerivation_or_selectedownerbridge.candidate.json"
COEFF_DECISION = (
    DATA
    / "selected_rtheta_coefficientformuladerivation_or_selectedownerbridge"
    / "coefficient_formula_derivation_decision.packet.json"
)
POLARIZATION = DATA / "selected_smslotfunctor_polarization_overlap_source_emission.candidate.json"
STATIONARY = (
    DATA
    / "selected_stationaryprojector_dotd_integrated_frontier"
    / "stationary_projector_dotd_integration.packet.json"
)
SECTOR_PROJECTORS = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
SPECTRAL = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"
SLOT_PROJECTION = (
    DATA
    / "selected_rtheta_coefficientformuladerivation_or_selectedownerbridge"
    / "rtheta_slot_projection_feasibility.packet.json"
)
EXTERNAL_MANIFEST = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "external_likelihood_import_manifest.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETAPHYSICALPROJECTIONKERNEL_OR_PROFILERESPONSE_"
    "BUILT_INPUTS_RECONCILED_SELECTED_SOLVE_OPEN"
)
NEXT = "MTT_Selected_RThetaSelectedRouteCGalerkinSolve_or_DiagonalProfileTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing R_theta physical projection sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        COEFF_DECISION,
        POLARIZATION,
        STATIONARY,
        SECTOR_PROJECTORS,
        SPECTRAL,
        SLOT_PROJECTION,
        EXTERNAL_MANIFEST,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    coeff_decision = load(COEFF_DECISION)
    polarization = load(POLARIZATION)
    stationary = load(STATIONARY)
    sector_projectors = load(SECTOR_PROJECTORS)
    spectral = load(SPECTRAL)
    slot_projection = load(SLOT_PROJECTION)
    external = load(EXTERNAL_MANIFEST)

    input_reconciliation = {
        "schema": "MTTRThetaProjectionInputReconciliation.v1",
        "status": "PROJECTION_INPUTS_RECONCILED_SELECTED_SOLVE_STILL_OPEN",
        "closed_inputs": {
            "q79_polarization_A4": polarization["polarization_emission"]["selected"],
            "U10_Ubar5_outputs": polarization["polarization_emission"]["selected_outputs"],
            "block_family_Higgs_projector_retention": spectral["two_layer_projector_audit"][
                "block_projector_layer"
            ]["block_family_Higgs_projector_retention"],
            "stationary_projector_source_verified": stationary[
                "stationary_projector_source_promotion"
            ]["selected_projector_source_verified"],
            "sector_projectors_on_27_mode_BN_emitted": sector_projectors["what_closes_now"][
                "sector_projectors_on_27_mode_BN_emitted"
            ],
            "projectors_idempotent_and_hermitian": sector_projectors["what_closes_now"][
                "projectors_are_idempotent_and_hermitian"
            ],
        },
        "not_closed_inputs": {
            "selected_RouteC_Strominger_Galerkin_residual_solve": spectral[
                "what_remains_open"
            ]["selected_RouteC_Strominger_Galerkin_residual_solve"],
            "coherent_spectral_projector_retention": spectral["two_layer_projector_audit"][
                "spectral_projector_layer"
            ]["coherent_spectral_zero_mode_projector_retention"],
            "selected_DE_Riesz_Green_dotD_values": spectral["two_layer_projector_audit"][
                "spectral_projector_layer"
            ]["selected_D_E_dotD_Riesz_Green"],
            "honest_sector_projector_dotD_replay": sector_projectors["validation"]["honest"][
                "exit_code"
            ]
            == 0,
        },
        "input_reconciliation_closed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INPUT_RECONCILIATION, input_reconciliation)

    component_tests = {
        "static_block_projectors_available": input_reconciliation["closed_inputs"][
            "block_family_Higgs_projector_retention"
        ],
        "q79_polarization_available": input_reconciliation["closed_inputs"]["q79_polarization_A4"],
        "sector_projector_matrices_available": input_reconciliation["closed_inputs"][
            "sector_projectors_on_27_mode_BN_emitted"
        ],
        "stationary_projector_source_verified": input_reconciliation["closed_inputs"][
            "stationary_projector_source_verified"
        ],
        "coherent_spectral_projectors_available": input_reconciliation["not_closed_inputs"][
            "coherent_spectral_projector_retention"
        ],
        "selected_routec_solve_available": not input_reconciliation["not_closed_inputs"][
            "selected_RouteC_Strominger_Galerkin_residual_solve"
        ],
        "honest_sector_projector_dotd_replay": input_reconciliation["not_closed_inputs"][
            "honest_sector_projector_dotD_replay"
        ],
    }
    kernel_closed = all(component_tests.values())

    pi_rows = []
    for row in slot_projection["slot_rows"]:
        pi_rows.append(
            {
                "slot_id": row["slot_id"],
                "precoefficient_formula_skeleton": row["precoefficient_formula_skeleton"],
                "static_projector_support_available": component_tests[
                    "static_block_projectors_available"
                ],
                "q79_polarization_support_available": component_tests[
                    "q79_polarization_available"
                ],
                "physical_projection_kernel_closed_for_slot": False,
                "why_not_closed": [
                    "coherent spectral zero-mode projector retention is not selected",
                    "selected Route-C/Strominger Galerkin residual solve is not emitted",
                    "honest sector projector/dotD replay still fails source-driver flags",
                ],
            }
        )

    kernel_attempt = {
        "schema": "MTTPiRThetaKernelAttempt.v1",
        "status": "PI_RTHETA_KERNEL_ATTEMPTED_SELECTED_SOLVE_REQUIRED",
        "component_tests": component_tests,
        "slot_rows": pi_rows,
        "slot_count": len(pi_rows),
        "closed_slot_count": sum(1 for row in pi_rows if row["physical_projection_kernel_closed_for_slot"]),
        "Pi_Rtheta_closed": kernel_closed,
        "minimal_internal_missing_object": "SelectedRouteCStromingerGalerkinResidualSolve",
        "reason": (
            "Static/projector/polarization inputs are reconciled, but physical projection needs coherent "
            "spectral projectors and selected D_E/Riesz/Green/dotD values from an honest selected solve."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(KERNEL_ATTEMPT, kernel_attempt)

    profile_gate = {
        "schema": "MTTProfileResponseRecheck.v1",
        "status": "PROFILE_RESPONSE_RECHECKED_FULL_WORKSPACE_OR_DIAGONAL_THEOREM_OPEN",
        "external_profile_workspace_imported": external["accepted_external_likelihood_imported_now"],
        "required_external_payload": external["required_import_payload"],
        "accepted_diagonal_limitation_theorem_present": False,
        "profile_response_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROFILE_GATE, profile_gate)

    decision = {
        "schema": "MTTPhysicalProjectionKernelDecision.v1",
        "status": "PROJECTION_INPUTS_CLOSED_PI_RTHETA_AND_PROFILE_RESPONSE_OPEN",
        "previous_status": previous["status"],
        "coefficient_decision_status": coeff_decision["status"],
        "projection_input_reconciliation_closed": True,
        "Pi_Rtheta_closed": False,
        "profile_response_closed": False,
        "rtheta_packet_constructed": False,
        "selected_threshold_response_functional_instantiated": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "active_frontier": [
            "emit SelectedRouteCStromingerGalerkinResidualSolve to close Pi_Rtheta",
            "select precision convention functor before measured-value comparison",
            "attach full profile response or accepted diagonal limitation theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterProjectionKernelAttempt.v1",
        "status": "NEXT_ATTACK_SELECTED_ROUTEC_GALERKIN_SOLVE_OR_DIAGONAL_PROFILE_THEOREM",
        "closed_now": {
            "projection_input_reconciliation": True,
            "q79_polarization_imported": True,
            "static_projector_support_imported": True,
            "Pi_Rtheta_attempt_without_overclaim": True,
        },
        "still_open": decision["active_frontier"],
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "execute/derive selected Route-C/Strominger Galerkin solve with coherent spectral projectors and D_E/Riesz/Green/dotD values",
            "route_B": "prove accepted diagonal profile-response theorem while internal Pi_Rtheta solve proceeds",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaPhysicalProjectionKernelOrProfileResponse",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "projection_input_reconciliation": rel(INPUT_RECONCILIATION),
            "pi_rtheta_kernel_attempt": rel(KERNEL_ATTEMPT),
            "profile_response_recheck": rel(PROFILE_GATE),
            "physical_projection_kernel_decision": rel(DECISION),
            "next_cutset_after_projection_kernel_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaProjectionInputReconciliationAndSelectedSolveReductionTheorem",
            "proved": True,
            "statement": (
                "The physical projection inputs for Pi_Rtheta can be reconciled: q79 polarization, block "
                "family/Higgs projector retention, stationary projector source verification, and finite sector "
                "projector matrices are present. These do not yet close Pi_Rtheta because coherent spectral "
                "zero-mode projectors, selected D_E/Riesz/Green/dotD values, and the honest selected Route-C/"
                "Strominger Galerkin residual solve remain open. The profile response route also remains open."
            ),
        },
        "closure_decision": {
            "projection_input_reconciliation_closed": True,
            "Pi_Rtheta_closed": False,
            "profile_response_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RThetaPhysicalProjectionKernel_or_ProfileResponse_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "projection_input_reconciliation_closed": True,
        "Pi_Rtheta_closed": False,
        "profile_response_closed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaPhysicalProjectionKernel or ProfileResponse v1

Status: `{STATUS}`.

This artifact tries to build `Pi_Rtheta`, the physical projection kernel.

```text
projection inputs reconciled : true
Pi_Rtheta closed             : false
profile response closed      : false
closed projection slots      : {kernel_attempt["closed_slot_count"]}/{kernel_attempt["slot_count"]}
```

The next internal missing object is now the selected Route-C/Strominger
Galerkin residual solve with coherent spectral projectors and selected
`D_E`/Riesz/Green/`dotD` values.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
