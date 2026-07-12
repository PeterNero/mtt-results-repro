"""Build finite H functional candidate or direct Herm(2) row emission run."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitehfunctionalcandidate_or_directherm2rowemissionrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteHFunctionalCandidate_or_DirectHerm2RowEmissionRun_v1.md"

RUN = PACKET_DIR / "finite_h_functional_candidate_emission_run.packet.json"
DIRECT = PACKET_DIR / "direct_herm2_rows_after_candidate_run.packet.json"
REDUCTION = PACKET_DIR / "sbeta_radial_phase_reduction.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_finite_h_candidate_run.packet.json"

PREVIOUS = DATA / "selected_hresponsevaluesourcefunctional_or_directherm2rows.candidate.json"
VALUE_FUNCTIONAL = (
    DATA
    / "selected_hresponsevaluesourcefunctional_or_directherm2rows"
    / "hresponse_value_source_functional.packet.json"
)
DIRECT_HQUARTIC = DATA / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows.candidate.json"
STRAIN_KERNEL = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof.candidate.json"
HYM_BRIDGE = DATA / "selected_higgshymsectionringquadraturebridge_or_directhuvpayload.candidate.json"
STRICT_MH = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "strict_mh_table_value_gate.packet.json"
)

STATUS = (
    "MTT_SELECTED_FINITEHFUNCTIONALCANDIDATE_OR_DIRECTHERM2ROWEMISSIONRUN_"
    "EXECUTED_SBETA_REDUCTION_ONLY_VALUES_OPEN"
)
NEXT = "MTT_Selected_HRadialScalePhaseSource_or_Herm2HessianRows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing finite H functional inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, VALUE_FUNCTIONAL, DIRECT_HQUARTIC, STRAIN_KERNEL, HYM_BRIDGE, STRICT_MH]
    require_sources(sources)

    previous = load(PREVIOUS)
    value_functional = load(VALUE_FUNCTIONAL)
    direct_hquartic = load(DIRECT_HQUARTIC)
    strain = load(STRAIN_KERNEL)
    hym_bridge = load(HYM_BRIDGE)
    strict_mh = load(STRICT_MH)

    s_beta = direct_hquartic["closure_decision"]["selected_s_beta_value"]
    required_table = strict_mh["required_values"]

    candidate_attempts = [
        {
            "candidate_id": "metric_quotient_functional",
            "source": "B_Huv^* G_Q B_Huv",
            "emitted": False,
            "accepted": False,
            "rejection_reason": "metric-only Hessian is explicitly forbidden and has no selected dynamic H action source",
        },
        {
            "candidate_id": "finite_projection_sbeta_reduction",
            "source": rel(STRAIN_KERNEL),
            "emitted": True,
            "accepted": False,
            "emitted_values": {"s_beta": s_beta},
            "rejection_reason": "s_beta fixes the Herm(2) polar angle but not radial scale, phase/sign, or source-owned Hessian rows",
        },
        {
            "candidate_id": "direct_hquartic_radial_collapse",
            "source": rel(DIRECT_HQUARTIC),
            "emitted": True,
            "accepted": False,
            "emitted_values": {"s_beta": s_beta},
            "rejection_reason": "radial-collapse theorem reduces the problem to one scalar source but emits no selected r_H or H rows",
        },
        {
            "candidate_id": "hym_section_ring_c2_basis",
            "source": rel(HYM_BRIDGE),
            "emitted": True,
            "accepted": False,
            "rejection_reason": "finite quotient basis is typed but C3-C6/value payload is absent in this bridge packet",
        },
    ]

    run = {
        "schema": "MTTFiniteHFunctionalCandidateEmissionRun.v1",
        "status": "FINITE_H_FUNCTIONAL_CANDIDATE_RUN_EXECUTED_NO_ACCEPTED_FUNCTIONAL",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "value_source_contract_ref": rel(VALUE_FUNCTIONAL),
        "acceptance_requirements": value_functional["accepted_value_source_contract"][
            "direct_F_H_second_variation"
        ],
        "candidate_attempts": candidate_attempts,
        "decision": {
            "candidate_attempt_count": len(candidate_attempts),
            "accepted_finite_H_functional_count": 0,
            "selected_F_H_functional_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "selected_nonzero_tracefree_Herm2_hessian_emitted": False,
            "finite_exactness_or_residual_certificate_emitted": False,
            "only_s_beta_reduction_available": True,
        },
    }

    direct = {
        "schema": "MTTDirectHerm2RowsAfterFiniteHCandidateRun.v1",
        "status": "DIRECT_HERM2_ROWS_STILL_NULL_AFTER_FINITE_H_CANDIDATE_RUN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "required_rows": [
            {"row_id": key, "value": value, "emitted": value is not None, "accepted": False}
            for key, value in required_table.items()
        ],
        "decision": {
            "required_row_or_certificate_count": len(required_table),
            "emitted_row_or_certificate_count": sum(1 for value in required_table.values() if value is not None),
            "accepted_row_or_certificate_count": 0,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
        },
    }

    reduction = {
        "schema": "MTTSBetaRadialPhaseReduction.v1",
        "status": "SBETA_POLAR_ANGLE_AVAILABLE_RADIAL_PHASE_SOURCE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_selected_scalar_support": {
            "selected_s_beta_value": s_beta,
            "selected_s_beta_polar_angle_closed": direct_hquartic["closure_decision"][
                "selected_s_beta_polar_angle_closed"
            ],
            "H_scalar_threshold_reduced_to_one_radial_source": direct_hquartic[
                "closure_decision"
            ]["H_scalar_threshold_reduced_to_one_radial_source"],
            "Herm2_radial_collapse_closed": direct_hquartic["closure_decision"][
                "Herm2_radial_collapse_closed"
            ],
        },
        "missing_for_Herm2_values": [
            "selected radial scale r_H or equivalent threshold scalar",
            "selected phase/sign convention for Omega",
            "same-source Hessian/source ownership certificate",
            "same-source exactness/error certificate",
        ],
        "decision": {
            "s_beta_available": True,
            "radial_scale_source_emitted": False,
            "phase_source_emitted": False,
            "Herm2_values_determined": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterFiniteHFunctionalCandidateRun.v1",
        "status": "NEXT_FRONTIER_H_RADIAL_SCALE_PHASE_SOURCE_OR_HERM2_HESSIAN_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "finite H functional candidate emission run executed",
            "s_beta/radial-collapse support separated from full Herm(2) values",
            "direct Herm(2) row table rechecked after candidate run",
        ],
        "still_open": [
            "selected radial scale r_H or equivalent threshold scalar",
            "selected Omega phase/sign source",
            "selected F_H Hessian/source ownership certificate",
            "direct Huu,Hud_re,Hud_im,Hdd values",
            "selected H-response spectrum/logdet",
            "R_H^RG/lambda_H value execution",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedFiniteHFunctionalCandidateOrDirectHerm2RowEmissionRun",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "FiniteHFunctionalCandidateOrDirectHerm2RowEmissionRunTheorem",
            "proved": True,
            "statement": (
                "The first selected finite H functional/direct Herm(2) emission run "
                "accepts no current candidate. Existing support does select the "
                "s_beta polar-angle reduction and radial-collapse theorem, but it "
                "does not emit the radial scale, Omega phase/sign, source ownership, "
                "or exactness certificates needed to determine Huu,Hud,Hdd."
            ),
        },
        "packets": {
            "finite_h_functional_candidate_emission_run": rel(RUN),
            "direct_herm2_rows_after_candidate_run": rel(DIRECT),
            "sbeta_radial_phase_reduction": rel(REDUCTION),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "value_functional": rel(VALUE_FUNCTIONAL),
            "direct_hquartic": rel(DIRECT_HQUARTIC),
            "strain_kernel": rel(STRAIN_KERNEL),
            "hym_bridge": rel(HYM_BRIDGE),
            "strict_mh": rel(STRICT_MH),
        },
        "closure_decision": {
            "finite_H_functional_candidate_run_executed": True,
            "selected_s_beta_polar_angle_closed": True,
            "Herm2_radial_collapse_closed": True,
            "selected_F_H_functional_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "selected_radial_scale_source_emitted": False,
            "selected_phase_source_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "R_H_RG_logdet_value_executed": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_predicted": False,
            "accepted_finite_H_functional_count": 0,
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "candidate_attempt_count": len(candidate_attempts),
            "accepted_finite_H_functional_count": 0,
            "selected_s_beta_value": s_beta,
            "required_direct_Herm2_row_or_certificate_count": len(required_table),
            "emitted_direct_Herm2_row_or_certificate_count": sum(
                1 for value in required_table.values() if value is not None
            ),
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "selected_K_source_rows": previous["key_numbers"]["selected_K_source_rows"],
            "selected_K_rows_required": previous["key_numbers"]["selected_K_rows_required"],
        },
    }

    cert = {
        "certificate": "MTTSelectedFiniteHFunctionalCandidateOrDirectHerm2RowEmissionRun",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "finite_H_functional_candidate_run_executed": True,
        "selected_s_beta_polar_angle_closed": True,
        "Herm2_radial_collapse_closed": True,
        "selected_F_H_functional_emitted": False,
        "selected_radial_scale_source_emitted": False,
        "selected_phase_source_emitted": False,
        "direct_Herm2_rows_emitted": False,
        "R_H_RG_value_emitted": False,
        "lambda_H_predicted": False,
        "accepted_finite_H_functional_count": 0,
        "accepted_H_response_source_row_count": 0,
        "accepted_R_H_RG_source_count": 0,
    }

    note = f"""# MTT Selected Finite H Functional Candidate or Direct Herm(2) Row Emission Run v1

Status: `{STATUS}`

## Theorem

The first finite H functional/direct Herm(2) emission run has now been executed
against the current selected support.  The run accepts no finite `F_H` candidate
and emits no direct Herm(2) value rows.

## What Did Move

The selected `s_beta` polar-angle reduction is retained:

```text
s_beta = {s_beta}
```

The Herm(2) problem is reduced to the missing radial scale/threshold scalar plus
the phase/sign and source certificates needed to determine `Huu`, `Hud`, and
`Hdd`.

## What Remains

Accepted finite H functionals: `0`.

Accepted H-response source rows: `0`.

Next artifact: `{NEXT}`
"""

    write_json(RUN, run)
    write_json(DIRECT, direct)
    write_json(REDUCTION, reduction)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
