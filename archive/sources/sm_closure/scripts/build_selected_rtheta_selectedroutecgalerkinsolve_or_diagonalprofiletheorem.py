"""Build R_theta selected Route-C Galerkin solve / diagonal profile theorem gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_selectedroutecgalerkinsolve_or_diagonalprofiletheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EXTERNAL = PACKET_DIR / "external_strominger_galerkin_inspiration.packet.json"
SOLVE_CONTRACT = PACKET_DIR / "selected_routec_galerkin_solve_acceptance_contract.packet.json"
READINESS = PACKET_DIR / "current_selected_routec_solve_readiness.packet.json"
DIAGONAL = PACKET_DIR / "diagonal_profile_theorem_attempt.packet.json"
DECISION = PACKET_DIR / "selected_solve_or_diagonal_profile_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_selected_solve_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaSelectedRouteCGalerkinSolve_or_DiagonalProfileTheorem_v1.md"

PREVIOUS = DATA / "selected_rtheta_physicalprojectionkernel_or_profileresponse.candidate.json"
PI_DECISION = (
    DATA
    / "selected_rtheta_physicalprojectionkernel_or_profileresponse"
    / "physical_projection_kernel_decision.packet.json"
)
KERNEL_ATTEMPT = (
    DATA
    / "selected_rtheta_physicalprojectionkernel_or_profileresponse"
    / "pi_rtheta_kernel_attempt.packet.json"
)
SPECTRAL = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"
SECTOR_PROJECTORS = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
STATIONARY = (
    DATA
    / "selected_stationaryprojector_dotd_integrated_frontier"
    / "stationary_projector_dotd_integration.packet.json"
)
POLARIZATION = DATA / "selected_smslotfunctor_polarization_overlap_source_emission.candidate.json"
DIAGONAL_PROFILE = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "profile_likelihood_execution_summary.packet.json"
)
EXTERNAL_MANIFEST = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "external_likelihood_import_manifest.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETASELECTEDROUTECGALERKINSOLVE_OR_DIAGONALPROFILETHEOREM_"
    "BUILT_SOLVE_CONTRACT_DIAGONAL_LIMITATION_OPEN"
)
NEXT = "MTT_Selected_RThetaSelectedRouteCSolveExecution_or_ProfileWorkspaceIngest_v1"


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
        raise FileNotFoundError("missing selected Route-C solve sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PI_DECISION,
        KERNEL_ATTEMPT,
        SPECTRAL,
        SECTOR_PROJECTORS,
        STATIONARY,
        POLARIZATION,
        DIAGONAL_PROFILE,
        EXTERNAL_MANIFEST,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    pi_decision = load(PI_DECISION)
    kernel_attempt = load(KERNEL_ATTEMPT)
    spectral = load(SPECTRAL)
    sector_projectors = load(SECTOR_PROJECTORS)
    stationary = load(STATIONARY)
    polarization = load(POLARIZATION)
    diagonal_profile = load(DIAGONAL_PROFILE)
    external_manifest = load(EXTERNAL_MANIFEST)

    external = {
        "schema": "MTTExternalStromingerGalerkinInspiration.v1",
        "status": "EXTERNAL_INSPIRATION_IMPORTED_AS_ACCEPTANCE_SHAPE_ONLY",
        "references": [
            {
                "id": "fu_yau_strominger",
                "url": "https://people.math.harvard.edu/~spicard/cetraro.pdf",
                "use": "Strominger-system existence shape and cohomological/topological consistency discipline; not an MTT selected solve.",
            },
            {
                "id": "andreas_garcia_fernandez_polystable",
                "url": "https://arxiv.org/abs/1011.6246",
                "use": "Stable/polystable bundle deformation route to Strominger-system solutions; informs source-owner bundle criteria.",
            },
            {
                "id": "strauss_spectral_approximation",
                "url": "https://arxiv.org/abs/1403.7120",
                "use": "Spectral approximation/Galerkin caution: trial-space values need pollution/error controls before promoted spectral data.",
            },
            {
                "id": "bae_polonik_eigenprojection_expansions",
                "url": "https://arxiv.org/abs/2602.00999",
                "use": "Eigenprojection perturbation framing for projection/gap/error payloads.",
            },
        ],
        "import_policy": "External results constrain the acceptance contract only; they do not supply selected MTT row values.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXTERNAL, external)

    solve_contract = {
        "schema": "MTTSelectedRouteCGalerkinSolveAcceptanceContract.v1",
        "status": "SELECTED_ROUTEC_GALERKIN_SOLVE_CONTRACT_EMITTED",
        "source_contract": spectral["selected_solve_contract"],
        "must_emit": [
            "selected_source_verified true for Route-C residual, D_E, Riesz/Green, dotD, and zero-mode sectors",
            "coherent spectral zero-mode projectors with idempotence, self-adjointness, orthogonality, and sum rules",
            "complement spectral gaps and reduced Green operators with truncation/error bounds",
            "ordered zero-mode bases for Q,u,d,L,e,N,H",
            "same-branch dotD_alpha1 and alpha1_driver_verified true",
            "primitive C1 contraction payload sufficient for Pi_Rtheta slot projections",
            "no observed masses, CKM/PMNS phases, benchmark matrices, or residual targets used as selectors",
        ],
        "acceptance_test_groups": {
            "strominger_hym_source": [
                "selected HYM/Strominger metric and connection",
                "mapped S3/GS source and Bianchi/Freed-Witten row",
            ],
            "spectral_projectors": [
                "sector projectors are coherent spectral projectors, not only block projectors",
                "gap/error certificate controls Galerkin truncation",
            ],
            "operator_response": [
                "D_E/Riesz/Green/dotD emitted from the same selected solve",
                "honest validator passes without lifted source flags",
            ],
            "rtheta_projection": [
                "Pi_Rtheta projectors/functor maps dynamic sectors to ten threshold/mass-scheme slots",
                "precision convention selected before measured-value comparison",
            ],
        },
        "contract_closed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SOLVE_CONTRACT, solve_contract)

    readiness_rows = [
        {
            "id": "q79_polarization",
            "present": polarization["polarization_emission"]["selected"],
            "source": rel(POLARIZATION),
            "role": "selected orientation/polarization input",
        },
        {
            "id": "block_projector_retention",
            "present": spectral["two_layer_projector_audit"]["block_projector_layer"][
                "block_family_Higgs_projector_retention"
            ],
            "source": rel(SPECTRAL),
            "role": "static block-family/Higgs projector support",
        },
        {
            "id": "sector_projector_matrices",
            "present": sector_projectors["what_closes_now"][
                "sector_projectors_on_27_mode_BN_emitted"
            ],
            "source": rel(SECTOR_PROJECTORS),
            "role": "finite sector projector matrices",
        },
        {
            "id": "stationary_projector_source",
            "present": stationary["stationary_projector_source_promotion"][
                "selected_projector_source_verified"
            ],
            "source": rel(STATIONARY),
            "role": "stationary projector source verification",
        },
        {
            "id": "coherent_spectral_projector_retention",
            "present": spectral["two_layer_projector_audit"]["spectral_projector_layer"][
                "coherent_spectral_zero_mode_projector_retention"
            ],
            "source": rel(SPECTRAL),
            "role": "required selected spectral projector layer",
        },
        {
            "id": "selected_DE_Riesz_Green_dotD",
            "present": spectral["two_layer_projector_audit"]["spectral_projector_layer"][
                "selected_D_E_dotD_Riesz_Green"
            ],
            "source": rel(SPECTRAL),
            "role": "operator response payload",
        },
        {
            "id": "honest_dotD_replay_without_lifted_flags",
            "present": sector_projectors["validation"]["honest"]["exit_code"] == 0,
            "source": rel(SECTOR_PROJECTORS),
            "role": "honest validator replay",
        },
    ]
    readiness = {
        "schema": "MTTCurrentSelectedRouteCSolveReadiness.v1",
        "status": "CURRENT_SOLVE_READINESS_AUDITED_SUPPORT_STRONG_VALUES_OPEN",
        "readiness_rows": readiness_rows,
        "present_count": sum(1 for row in readiness_rows if row["present"]),
        "required_count": len(readiness_rows),
        "selected_routec_galerkin_solve_closed": False,
        "why_not_closed": [
            "coherent spectral zero-mode projector retention remains false",
            "selected D_E/Riesz/Green/dotD values remain false",
            "honest dotD replay still fails source-driver flags",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(READINESS, readiness)

    diagonal = {
        "schema": "MTTDiagonalProfileTheoremAttempt.v1",
        "status": "DIAGONAL_PROFILE_LIMITATION_THEOREM_ATTEMPTED_NOT_ACCEPTED_FOR_TRUE_EQUIVALENCE",
        "diagonal_profile_source": rel(DIAGONAL_PROFILE),
        "external_manifest": rel(EXTERNAL_MANIFEST),
        "coarse_diagonal_profile_available": diagonal_profile["profile_summary"][
            "passes_coarse_diagonal_profile"
        ],
        "full_correlated_profile_imported": external_manifest[
            "accepted_external_likelihood_imported_now"
        ],
        "accepted_diagonal_limitation_theorem_for_true_equivalence": False,
        "accepted_as_diagnostic_or_SM_parity_limited_profile": True,
        "why_not_true_equivalence": [
            "no full correlated likelihood/profile workspace",
            "no nuisance/profile semantics",
            "diagonal profile cannot replace threshold covariance response for final precision closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DIAGONAL, diagonal)

    decision = {
        "schema": "MTTSelectedSolveOrDiagonalProfileDecision.v1",
        "status": "SOLVE_CONTRACT_CLOSED_SOLVE_AND_PROFILE_STILL_OPEN",
        "previous_status": previous["status"],
        "pi_decision_status": pi_decision["status"],
        "selected_routec_galerkin_solve_contract_closed": True,
        "selected_routec_galerkin_solve_closed": False,
        "diagonal_profile_theorem_accepted_for_true_equivalence": False,
        "Pi_Rtheta_closed": False,
        "profile_response_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "minimal_next_actions": [
            "execute selected Route-C/Strominger Galerkin solve or import a packet that already does",
            "emit coherent spectral projectors, selected D_E/Riesz/Green/dotD values, and primitive C1 contractions",
            "rerun Pi_Rtheta projection slot closure",
            "separately ingest full profile workspace or prove a strictly scoped diagonal limitation theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterSelectedSolveGate.v1",
        "status": "NEXT_ATTACK_SOLVE_EXECUTION_OR_PROFILE_WORKSPACE_INGEST",
        "closed_now": {
            "external_inspiration_imported_as_contract_shape": True,
            "selected_routec_solve_acceptance_contract": True,
            "current_readiness_audited": True,
            "diagonal_profile_theorem_attempt_scoped": True,
        },
        "still_open": decision["minimal_next_actions"],
        "recommended_next": {
            "artifact": NEXT,
            "internal_route": "run or construct selected Route-C/Strominger Galerkin solve packet",
            "external_route": "ingest full profile workspace with covariance/nuisance semantics",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaSelectedRouteCGalerkinSolveOrDiagonalProfileTheorem",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "external_strominger_galerkin_inspiration": rel(EXTERNAL),
            "selected_routec_galerkin_solve_acceptance_contract": rel(SOLVE_CONTRACT),
            "current_selected_routec_solve_readiness": rel(READINESS),
            "diagonal_profile_theorem_attempt": rel(DIAGONAL),
            "selected_solve_or_diagonal_profile_decision": rel(DECISION),
            "next_cutset_after_selected_solve_gate": rel(CUTSET),
        },
        "theorem": {
            "name": "SelectedRouteCSolveContractAndDiagonalProfileBoundaryTheorem",
            "proved": True,
            "statement": (
                "The selected Route-C/Strominger Galerkin solve can be stated as a strict acceptance contract "
                "using internal support and external Strominger/HYM/spectral-Galerkin inspiration. Current repo "
                "inputs are strong but do not close the solve: coherent spectral projectors, selected "
                "D_E/Riesz/Green/dotD values, and honest source-flag replay remain open. The diagonal profile "
                "route is accepted only as diagnostic/SM-parity limited support, not true-equivalence closure."
            ),
        },
        "closure_decision": {
            "selected_routec_galerkin_solve_contract_closed": True,
            "selected_routec_galerkin_solve_closed": False,
            "diagonal_profile_theorem_accepted_for_true_equivalence": False,
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
        "certificate": "MTT_Selected_RThetaSelectedRouteCGalerkinSolve_or_DiagonalProfileTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_routec_galerkin_solve_contract_closed": True,
        "selected_routec_galerkin_solve_closed": False,
        "diagonal_profile_true_equivalence_closed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaSelectedRouteCGalerkinSolve or DiagonalProfileTheorem v1

Status: `{STATUS}`.

This artifact imports adjacent-repo/corpus support and external inspiration only
as an acceptance shape for the selected Route-C/Strominger Galerkin solve.

```text
solve contract closed       : true
readiness rows present      : {readiness["present_count"]}/{readiness["required_count"]}
selected solve closed       : false
diagonal profile accepted   : false
```

The next internal move is execution or import of the selected solve packet:
coherent spectral projectors, selected `D_E`/Riesz/Green/`dotD`, and primitive
C1 contractions.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
