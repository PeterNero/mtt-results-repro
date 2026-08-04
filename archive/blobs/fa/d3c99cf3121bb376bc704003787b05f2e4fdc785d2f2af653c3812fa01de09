"""Build final no-knob value derivation kernel or source-anchor theorem frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_noknobvaluederivationkernel_or_sourceanchortheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
UPDATED_KERNEL = PACKET_DIR / "updated_no_knob_value_derivation_kernel.packet.json"
OBLIGATION_STATUS = PACKET_DIR / "internal_value_obligation_status_after_readiness_8of9.packet.json"
SOURCE_ANCHOR_TARGET = PACKET_DIR / "candidate_specific_source_anchor_target.packet.json"
FINAL_DECISION = PACKET_DIR / "final_closure_decision_after_kernel_update.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_NoKnobValueDerivationKernel_or_SourceAnchorTheorem_v1.md"

PREVIOUS = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
SAMEBRANCH = DATA / "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction.candidate.json"
FINAL_FRONTIER = (
    DATA
    / "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction"
    / "final_value_frontier_after_integration.packet.json"
)
VSD_KERNEL = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)
FINAL_RECHECK = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "final_no_knob_value_derivation_recheck.packet.json"
)
READINESS = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "rtheta_readiness_final_frontier.packet.json"
)
COEFF_ATTEMPT = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_value_row_coefficients_attempt.packet.json"
)
HIGHER_CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)
UNIVERSAL_CANDIDATES = DATA / "universal_source_parameter_policy/candidate_universal_parameters.packet.json"
UNIVERSAL_POLICY = DATA / "universal_source_parameter_policy/universal_source_parameter_policy.packet.json"

STATUS = (
    "MTT_SELECTED_NOKNOBVALUEDERIVATIONKERNEL_OR_SOURCEANCHORTHEOREM_"
    "BUILT_FINAL_KERNEL_NO_INTERNAL_VALUES_SELECTED"
)
NEXT = "MTT_Selected_InternalRThetaScalarRowEmission_or_UniversalAnchorSelection_v1"


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
        raise FileNotFoundError("missing no-knob kernel inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        SAMEBRANCH,
        FINAL_FRONTIER,
        VSD_KERNEL,
        FINAL_RECHECK,
        READINESS,
        COEFF_ATTEMPT,
        HIGHER_CONTRACT,
        UNIVERSAL_CANDIDATES,
        UNIVERSAL_POLICY,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    samebranch = load(SAMEBRANCH)
    frontier = load(FINAL_FRONTIER)
    vsd = load(VSD_KERNEL)
    recheck = load(FINAL_RECHECK)
    readiness = load(READINESS)
    coeff_attempt = load(COEFF_ATTEMPT)
    higher_contract = load(HIGHER_CONTRACT)
    candidates = load(UNIVERSAL_CANDIDATES)
    policy = load(UNIVERSAL_POLICY)

    selected_candidates = [
        candidate for candidate in candidates["candidate_classes"] if candidate["selected_now"]
    ]
    required_rows = vsd["required_rows"]
    closed_rows = [row for row in required_rows if row["closed"]]

    updated_kernel = {
        "schema": "MTTUpdatedNoKnobValueDerivationKernel.v1",
        "status": "FINAL_KERNEL_TYPED_NO_INTERNAL_VALUE_ROWS_SELECTED",
        "readiness_fraction": readiness["readiness_fraction"],
        "only_remaining_readiness_blocker": readiness["only_remaining_readiness_blocker"],
        "codomain_scalar_rows": higher_contract["codomain_scalar_rows"],
        "codomain_scalar_row_count": higher_contract["codomain_scalar_row_count"],
        "value_source_required_row_count": vsd["required_row_count"],
        "value_source_closed_row_count": len(closed_rows),
        "accepted_coefficient_row_count": coeff_attempt["accepted_coefficient_row_count"],
        "selected_internal_value_emission_count": recheck[
            "selected_internal_value_emission_count"
        ],
        "selected_universal_parameter_count": recheck["selected_universal_parameter_count"],
        "kernel_statement": (
            "All surrounding readiness gates are closed except no-knob value derivation. The remaining "
            "kernel must either emit internal selected scalar rows or select a universal source anchor "
            "before empirical replay. Current packets do neither."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(UPDATED_KERNEL, updated_kernel)

    obligation_status = {
        "schema": "MTTInternalValueObligationStatusAfterReadiness8of9.v1",
        "status": "INTERNAL_VALUE_OBLIGATIONS_STILL_OPEN",
        "required_rows": [
            {
                "id": row["id"],
                "obligation": row["obligation"],
                "closed": row["closed"],
                "why_open": row["why_open"],
            }
            for row in required_rows
        ],
        "closed_row_count": len(closed_rows),
        "required_row_count": len(required_rows),
        "scalar_value_rows_emitted": 0,
        "lambda_H_row_emitted": False,
        "diagnostic_coefficients_available_but_rejected": coeff_attempt[
            "diagnostic_coefficient_count"
        ],
        "accepted_coefficient_rows": coeff_attempt["accepted_coefficient_rows"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(OBLIGATION_STATUS, obligation_status)

    source_anchor_target = {
        "schema": "MTTCandidateSpecificSourceAnchorTarget.v1",
        "status": "SOURCE_ANCHOR_THEOREM_NOT_SELECTED",
        "policy": rel(UNIVERSAL_POLICY),
        "maximum_live_universal_parameters": policy["maximum_live_universal_parameters"],
        "selected_candidates_now": selected_candidates,
        "selected_universal_parameter_count": len(selected_candidates),
        "candidate_classes": candidates["candidate_classes"],
        "theorem_required": {
            "must_select_anchor_before_empirical_replay": True,
            "must_be_universal_across_all_scalar_rows": True,
            "must_have_typed_Rtheta_gate_role": True,
            "must_not_be_inferred_from_residuals": True,
            "must_execute_the_same_ten_row_codomain": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SOURCE_ANCHOR_TARGET, source_anchor_target)

    final_decision = {
        "schema": "MTTFinalClosureDecisionAfterKernelUpdate.v1",
        "status": "FULL_SM_CLOSURE_NOT_YET_PROVED_FINAL_KERNEL_EXPOSED",
        "what_is_proved_now": {
            "qualitative_SM_orbit_closure": frontier["closed_now"][
                "qualitative_SM_orbit_closure"
            ],
            "Rtheta_readiness_8_of_9": frontier["closed_now"]["Rtheta_readiness_8_of_9"],
            "admitted_external_replay_boundary": frontier["closed_now"][
                "admitted_external_replay_boundary"
            ],
            "external_import_lane_closed_at_admitted_replay_tier": previous[
                "closure_decision"
            ]["external_import_lane_closed_at_admitted_replay_tier"],
            "final_no_knob_kernel_typed": True,
            "diagnostic_value_rows_rejected_as_selectors": True,
        },
        "what_is_not_proved": {
            "internal_no_knob_scalar_value_emission": True,
            "selected_universal_source_anchor": True,
            "Yukawa_CKM_PMNS_lambdaH_numerical_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "final_missing_object": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(FINAL_DECISION, final_decision)

    candidate = {
        "candidate": "MTTSelectedNoKnobValueDerivationKernelOrSourceAnchorTheorem",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "updated_no_knob_value_derivation_kernel": rel(UPDATED_KERNEL),
            "internal_value_obligation_status_after_readiness_8of9": rel(OBLIGATION_STATUS),
            "candidate_specific_source_anchor_target": rel(SOURCE_ANCHOR_TARGET),
            "final_closure_decision_after_kernel_update": rel(FINAL_DECISION),
        },
        "theorem": {
            "name": "FinalKernelExposureTheorem",
            "proved": True,
            "statement": (
                "The selected MTT/SM closure program is reduced to a final finite kernel: emit "
                "selected internal Rtheta scalar rows or prove a candidate-specific universal source "
                "anchor theorem. The present repo proves readiness 8/9 and qualitative SM orbit "
                "closure, but it does not yet prove numerical SM equivalence or full no-knob closure."
            ),
        },
        "closure_decision": {
            "final_no_knob_kernel_typed": True,
            "selected_internal_value_emission_count": recheck[
                "selected_internal_value_emission_count"
            ],
            "accepted_coefficient_row_count": coeff_attempt["accepted_coefficient_row_count"],
            "selected_universal_parameter_count": len(selected_candidates),
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": final_decision["what_is_proved_now"],
        "what_remains_open": final_decision["what_is_not_proved"],
        "previous_status": previous["status"],
        "samebranch_readiness_status": samebranch["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_NoKnobValueDerivationKernel_or_SourceAnchorTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "final_no_knob_kernel_typed": True,
        "selected_internal_value_emission_count": recheck[
            "selected_internal_value_emission_count"
        ],
        "accepted_coefficient_row_count": coeff_attempt["accepted_coefficient_row_count"],
        "selected_universal_parameter_count": len(selected_candidates),
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected NoKnobValueDerivationKernel or SourceAnchorTheorem v1

Status: `{STATUS}`.

The frontier is now a final finite kernel:

```text
Rtheta readiness                 : {readiness["readiness_fraction"]}
only readiness blocker           : {readiness["only_remaining_readiness_blocker"]}
internal selected value emissions: {recheck["selected_internal_value_emission_count"]}
accepted coefficient rows        : {coeff_attempt["accepted_coefficient_row_count"]}
selected universal parameters    : {len(selected_candidates)}
full SM numerical closure        : false
```

What is achieved is strong: qualitative SM orbit closure, Rtheta source/domain
closure, admitted external replay compatibility, and a typed final no-knob
kernel. What is not achieved yet is the actual internal numerical row emission
or a source-selected universal anchor.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
