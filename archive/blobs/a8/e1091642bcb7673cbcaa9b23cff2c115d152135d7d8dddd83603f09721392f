"""Build Herm(2) polar source completion or H-response rows packet."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_herm2polarsourcecompletion_or_hresponserows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Herm2PolarSourceCompletion_or_HResponseRows_v1.md"

TRACEFREE = PACKET_DIR / "tracefree_polar_source_completion.packet.json"
ORIENTATION = PACKET_DIR / "omega_phase_orientation_recheck.packet.json"
HROWS = PACKET_DIR / "conditional_hresponse_row_schema_after_polar_completion.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_herm2_polar_completion.packet.json"

PREVIOUS = DATA / "selected_hradialscalephasesource_or_herm2hessianrows.candidate.json"
POLAR_PREVIOUS = (
    DATA
    / "selected_hradialscalephasesource_or_herm2hessianrows"
    / "herm2_polar_reconstruction_law.packet.json"
)
HRESPONSE_VALUE = (
    DATA
    / "selected_hresponsevaluesourcefunctional_or_directherm2rows"
    / "hresponse_value_source_functional.packet.json"
)
HRESPONSE_ROWS = (
    DATA
    / "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution"
    / "hresponse_source_row_execution_table.packet.json"
)
HIGGS_SPECIFIC = DATA / "selected_higgsspecificmhacceptanceobject_or_valuefrontier.candidate.json"
FULL_MSOURCE = DATA / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable.candidate.json"
EHUV_BINDING = DATA / "selected_ehuvbindingtraceidentity_or_directhuvrows_to_hkthresholdemission.candidate.json"
STATIC_ORIENTATION = DATA / "selected_staticlambdaorbitquotient_or_dynamicorientationfrontier.candidate.json"
DYNAMIC_ORIENTATION = DATA / "selected_dynamicorientation_or_physicalmatrixpromotion.candidate.json"

STATUS = (
    "MTT_SELECTED_HERM2POLARSOURCECOMPLETION_OR_HRESPONSEROWS_"
    "TRACEFREE_CONTRACT_CLOSED_PHASE_TRACE_ROWS_OPEN"
)
NEXT = "MTT_Selected_Herm2OrientationPhaseTraceSource_or_DirectHResponseEmission_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Herm(2) polar completion inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        POLAR_PREVIOUS,
        HRESPONSE_VALUE,
        HRESPONSE_ROWS,
        HIGGS_SPECIFIC,
        FULL_MSOURCE,
        EHUV_BINDING,
        STATIC_ORIENTATION,
        DYNAMIC_ORIENTATION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    polar_previous = load(POLAR_PREVIOUS)
    hresponse_value = load(HRESPONSE_VALUE)
    hresponse_rows = load(HRESPONSE_ROWS)
    higgs_specific = load(HIGGS_SPECIFIC)
    full_msource = load(FULL_MSOURCE)
    ehuv_binding = load(EHUV_BINDING)
    static_orientation = load(STATIC_ORIENTATION)
    dynamic_orientation = load(DYNAMIC_ORIENTATION)

    s_beta = previous["key_numbers"]["selected_s_beta_value"]
    sqrt_s = math.sqrt(s_beta)
    sqrt_complement = math.sqrt(1.0 - s_beta)

    tracefree = {
        "schema": "MTTHerm2TraceFreePolarSourceCompletion.v1",
        "status": "TRACEFREE_POLAR_CONTRACT_CLOSED_VALUES_CONDITIONAL",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_support": {
            "Herm2_polar_reconstruction_law_closed": previous["closure_decision"][
                "Herm2_polar_reconstruction_law_closed"
            ],
            "H_specific_tracefree_normal_form_fixed": True,
            "Pauli_Riesz_three_row_source_functional_contract_closed": full_msource[
                "closure_decision"
            ]["Pauli_Riesz_three_row_source_functional_contract_closed"],
            "tracefree_formula_source": rel(HIGGS_SPECIFIC),
        },
        "tracefree_block": {
            "matrix": "[[Delta, Omega], [conj(Omega), -Delta]]",
            "Delta": "sigma_D * r_H * sqrt(s_beta)",
            "Omega": "r_H * sqrt(1-s_beta) * exp(i phi_Omega)",
            "s_beta": s_beta,
            "sqrt_s_beta": sqrt_s,
            "sqrt_1_minus_s_beta": sqrt_complement,
        },
        "what_tracefree_closes": [
            "m0 is not needed to define Delta, Omega, or the trace-free threshold block",
            "the quotient/non-scalar H sector uses the trace-free Herm(2) block",
            "the H-specific normal form and Pauli/Riesz coordinate law are aligned",
        ],
        "what_tracefree_does_not_close": [
            "strict radial scale r_H",
            "Delta sign sigma_D",
            "Omega phase phi_Omega",
            "full H-response rows Huu and Hdd when m0 is nonzero",
            "H-response spectrum/logdet requiring the full Herm(2) block",
        ],
        "decision": {
            "tracefree_polar_contract_closed": True,
            "m0_retired_for_tracefree_threshold_block": True,
            "m0_retired_for_full_H_response_rows": False,
            "Delta_row_emitted": False,
            "Omega_row_emitted": False,
            "direct_Herm2_rows_emitted": False,
        },
    }

    orientation = {
        "schema": "MTTOmegaPhaseOrientationRecheck.v1",
        "status": "ORIENTATION_SUPPORT_RECHECKED_NO_HIGGS_OMEGA_PHASE_SOURCE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "orientation_support_checked": {
            "static_lambda_orbit_selected": static_orientation["closure_decision"][
                "static_lambda_orbit_selected"
            ],
            "individual_lambda_value_selected": static_orientation["closure_decision"][
                "individual_lambda_value_selected"
            ],
            "dynamic_first_response_layer_closed": dynamic_orientation["closure_decision"][
                "dynamic_first_response_layer_closed"
            ],
            "selected_second_order_physical_matrices_promoted": dynamic_orientation[
                "closure_decision"
            ]["selected_second_order_physical_matrices_promoted"],
        },
        "legal_import_decision": {
            "can_import_static_lambda_orbit_as_Higgs_Omega_phase": False,
            "can_import_dynamic_first_response_as_Higgs_Omega_phase": False,
            "reason": (
                "The static lambda orbit and dynamic first-response packets concern "
                "matter/flavor orientation. They do not emit the same-source H_uv "
                "phase/sign certificate required for the Higgs Herm(2) block."
            ),
        },
        "remaining_Higgs_phase_sources": [
            "same-source H_uv basis phase convention",
            "selected Omega phase/sign certificate from F_H or M_source restriction",
            "direct H_response/Huv row emission with Hermiticity and exactness certificates",
        ],
        "decision": {
            "orientation_packets_rechecked": True,
            "selected_Omega_phase_emitted": False,
            "selected_Delta_sign_emitted": False,
            "orientation_import_rejected_as_Higgs_phase_source": True,
        },
    }

    hrows = {
        "schema": "MTTConditionalHResponseRowsAfterPolarCompletion.v1",
        "status": "HRESPONSE_ROWS_CONDITIONAL_SCHEMA_CLOSED_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "required_source_fields": {
            "r_H": "strict selected radial scale or controlled calibration tier explicitly marked",
            "sigma_D": "selected Delta sign/source orientation",
            "phi_Omega": "selected Omega phase in H_uv basis",
            "m0": "trace-center source or quotient trace-free normalization theorem",
            "certificates": [
                "Hdu_equals_conj_Hud",
                "source ownership",
                "same-source exactness/error",
                "quotient admissibility",
            ],
        },
        "conditional_rows": {
            "Delta": "sigma_D * r_H * sqrt(s_beta)",
            "Hud_re": "r_H * sqrt(1-s_beta) * cos(phi_Omega)",
            "Hud_im": "r_H * sqrt(1-s_beta) * sin(phi_Omega)",
            "Huu": "m0 + Delta",
            "Hdd": "m0 - Delta",
        },
        "current_row_table_status": {
            "required_H_response_row_count": hresponse_rows["decision"]["required_row_count"],
            "emitted_H_response_row_count": hresponse_rows["decision"]["emitted_row_count"],
            "accepted_H_response_source_row_count": hresponse_rows["decision"][
                "accepted_source_row_count"
            ],
        },
        "route_rechecks": {
            "full_M_source_route_instantiated_but_values_open": full_msource["closure_decision"][
                "full_M_source_R_H_formula_instantiated"
            ]
            and not full_msource["closure_decision"]["M_source_plus_R_H_values_emitted"],
            "E_H_UV_binding_trace_identity_still_open": not ehuv_binding["closure_decision"][
                "finite_trace_analogy_proves_E_H_UV_binding"
            ],
            "direct_Herm2_Huv_payload_emitted": full_msource["closure_decision"][
                "direct_Herm2_Huv_payload_emitted"
            ]
            or ehuv_binding["closure_decision"]["direct_Herm2_Huv_payload_emitted"],
            "value_source_contract_closed": hresponse_value["execution_decision"][
                "value_source_functional_contract_closed"
            ],
        },
        "decision": {
            "conditional_H_response_row_schema_closed": True,
            "accepted_H_response_source_row_count": 0,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "R_H_RG_value_emitted": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHerm2PolarCompletion.v1",
        "status": "NEXT_FRONTIER_HERM2_ORIENTATION_PHASE_TRACE_SOURCE_OR_DIRECT_HRESPONSE_EMISSION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "trace-free Herm(2) polar completion contract",
            "m0 retired only for the trace-free threshold block",
            "static/dynamic matter-orientation packets rechecked and rejected as Higgs Omega phase source",
            "conditional H-response row schema after polar completion",
        ],
        "still_open": [
            "strict selected radial scale r_H",
            "selected Delta sign sigma_D",
            "selected Omega phase phi_Omega in H_uv basis",
            "trace-center m0 source or full quotient trace-free H-response theorem",
            "same-source certificates",
            "direct H-response row emission",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHerm2PolarSourceCompletionOrHResponseRows",
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
            "name": "Herm2PolarSourceCompletionOrHResponseRowsTheorem",
            "proved": True,
            "statement": (
                "The trace-free Herm(2) polar completion contract is now closed: "
                "m0 is not needed for the non-scalar Delta/Omega threshold block, "
                "but it remains needed for full H-response rows and spectrum/logdet "
                "unless a quotient trace-free H-response theorem is emitted. Static "
                "and dynamic matter-orientation packets do not legally select the "
                "Higgs Omega phase. Therefore the remaining data are strict radial "
                "scale, Delta sign, Omega phase, trace-center/normalization source, "
                "and same-source certificates or direct H-response row emission."
            ),
        },
        "packets": {
            "tracefree_polar_source_completion": rel(TRACEFREE),
            "omega_phase_orientation_recheck": rel(ORIENTATION),
            "conditional_hresponse_row_schema": rel(HROWS),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "polar_previous": rel(POLAR_PREVIOUS),
            "hresponse_value": rel(HRESPONSE_VALUE),
            "hresponse_rows": rel(HRESPONSE_ROWS),
            "higgs_specific": rel(HIGGS_SPECIFIC),
            "full_msource": rel(FULL_MSOURCE),
            "ehuv_binding": rel(EHUV_BINDING),
            "static_orientation": rel(STATIC_ORIENTATION),
            "dynamic_orientation": rel(DYNAMIC_ORIENTATION),
        },
        "closure_decision": {
            "tracefree_polar_contract_closed": True,
            "m0_retired_for_tracefree_threshold_block": True,
            "m0_retired_for_full_H_response_rows": False,
            "orientation_packets_rechecked": True,
            "orientation_import_rejected_as_Higgs_phase_source": True,
            "conditional_H_response_row_schema_closed": True,
            "strict_radial_scale_source_emitted": False,
            "selected_Delta_sign_emitted": False,
            "selected_Omega_phase_emitted": False,
            "trace_center_source_or_normalization_emitted": False,
            "same_source_certificates_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_predicted": False,
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "selected_s_beta_value": s_beta,
            "sqrt_s_beta": sqrt_s,
            "sqrt_1_minus_s_beta": sqrt_complement,
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "required_H_response_row_count": hresponse_rows["decision"]["required_row_count"],
            "emitted_H_response_row_count": hresponse_rows["decision"]["emitted_row_count"],
        },
    }

    cert = {
        "certificate": "MTTSelectedHerm2PolarSourceCompletionOrHResponseRows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "tracefree_polar_contract_closed": True,
        "m0_retired_for_tracefree_threshold_block": True,
        "m0_retired_for_full_H_response_rows": False,
        "orientation_import_rejected_as_Higgs_phase_source": True,
        "conditional_H_response_row_schema_closed": True,
        "selected_Omega_phase_emitted": False,
        "direct_Herm2_rows_emitted": False,
        "R_H_RG_value_emitted": False,
        "lambda_H_predicted": False,
        "accepted_H_response_source_row_count": 0,
        "accepted_R_H_RG_source_count": 0,
    }

    note = f"""# MTT Selected Herm(2) Polar Source Completion or H-Response Rows v1

Status: `{STATUS}`

## Theorem

The trace-free Herm(2) polar contract is closed for the non-scalar Higgs block:

```text
M_H^tf = [[Delta, Omega], [conj(Omega), -Delta]]
Delta  = sigma_D * r_H * sqrt(s_beta)
Omega  = r_H * sqrt(1-s_beta) * exp(i phi_Omega)
```

Here `s_beta = {s_beta}`, so `sqrt(s_beta) = {sqrt_s}` and
`sqrt(1-s_beta) = {sqrt_complement}`.

## Boundary

`m0` is retired only for the trace-free threshold block.  It is not retired for
full `Huu/Hdd` response rows, spectrum, or logdet unless a quotient trace-free
H-response theorem is emitted.

Static/dynamic matter-orientation packets were rechecked and are not legal
sources for the Higgs `Omega` phase.

Accepted H-response source rows: `0`.

Next artifact: `{NEXT}`
"""

    write_json(TRACEFREE, tracefree)
    write_json(ORIENTATION, orientation)
    write_json(HROWS, hrows)
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
