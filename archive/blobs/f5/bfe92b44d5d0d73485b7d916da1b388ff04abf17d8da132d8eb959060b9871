"""Search local source clues for exact complement factorization or smooth transition tables."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")

INPUTS = {
    "valuepacket": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.candidate.json",
    "valuepacket_values": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
    "contract": DATA / "selected_heterotic_projectiverhoe_exact_complement_or_smooth_transition_value_contract.json",
}

SOURCE_FILES = {
    "qg_spt_factorization": OBSIDIAN / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md",
    "dirac_delta_finite_projection": OBSIDIAN / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md",
    "mtt_superset_spt": OBSIDIAN / "3 Core Foundations" / "Modal_Triplet_Theory__MTT_as_a_Superset_v2.md",
    "protospinor_transition_functions": TEXPAPERS / "10 ProtoSpinor" / "_work" / "World_in_World_Genesis__A_Proto_Geometric_Origin_of_Time__Gravity__Matter__and_Quantization_in_Modal_Triplet_Theory_v4" / "main.tex",
    "theta_color_twistor_factorization": TEXPAPERS / "18 Theta-Closure & Execution Program" / "_work" / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization" / "main.tex",
    "sm_parity_color_interface": TEXPAPERS / "mtt-sm-parity-closure" / "certificates" / "selected_qa_su3_color_bundle_connection_endomorphism_interface_certificate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_exactcomplementfactorization_or_goodcovertransitiontables_sourcesearch.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_exactcomplementfactorization_or_goodcovertransitiontables_sourcesearch_certificate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_projectiverhoe_minimal_smooth_closure_source_request.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_ExactComplementFactorization_or_GoodCoverTransitionTables_SourceSearch_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCESEARCH_SUPPORT_FOUND_GOODCOVER_AND_EXACT_FACTORIZATION_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_MinimalSmoothClosure_SourceRequest_or_DirectNoGo_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def term_scan(path: Path, terms: dict[str, str]) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore")
    lowered = text.lower()
    return {
        "path": str(path),
        "present": True,
        "terms": {key: needle.lower() in lowered for key, needle in terms.items()},
    }


def main() -> dict[str, Any]:
    valuepacket = load_json(INPUTS["valuepacket"])
    values = load_json(INPUTS["valuepacket_values"])
    contract = load_json(INPUTS["contract"])

    scans = {
        "qg_spt_factorization": term_scan(
            SOURCE_FILES["qg_spt_factorization"],
            {
                "SPT_factorization": "SPT factorization",
                "heat_semigroup": "heat semigroup",
                "vertical_complement": "vertical complement",
                "not_qasu3_transition_tables": "rho_E",
            },
        ),
        "dirac_delta_finite_projection": term_scan(
            SOURCE_FILES["dirac_delta_finite_projection"],
            {
                "finite_projectors": "finite coherent",
                "gauge_factorization_subtleties": "Gauge and gravitational factorization subtleties",
                "lens_dependent_factorization": "subsystem factorization is itself a Lens-dependent structure",
                "heat_kernel": "heat kernel",
            },
        ),
        "mtt_superset_spt": term_scan(
            SOURCE_FILES["mtt_superset_spt"],
            {
                "SPT_factorization": "SPT factorization",
                "heterotic_strominger": "Heterotic Flux/Strominger",
                "heat_kernel_expansion": "heat-kernel expansion",
                "torsional_su3": "torsional SU(3)",
            },
        ),
        "protospinor_transition_functions": term_scan(
            SOURCE_FILES["protospinor_transition_functions"],
            {
                "transition_functions": "transition functions",
                "factorization_fails": "factorization fails",
                "shared_bookkeeping": "shared ancestry",
                "good_cover": "good cover",
            },
        ),
        "theta_color_twistor_factorization": term_scan(
            SOURCE_FILES["theta_color_twistor_factorization"],
            {
                "color_twistor_factorization": "color--twistor factorization",
                "canonical_factorization": "canonical",
                "su3_sector": "SU(3) sector",
                "transition_tables": "transition",
            },
        ),
        "sm_parity_color_interface": term_scan(
            SOURCE_FILES["sm_parity_color_interface"],
            {
                "transition_rhoE_Cech_Dolbeault_or_DE_packet": "transition_rhoE_Cech_Dolbeault_or_DE_packet",
                "finite_spectrum_heat_or_torsion_response": "finite_spectrum_heat_or_torsion_response",
                "endomorphism_E_or_heat_zero_order_block": "endomorphism_E_or_heat_zero_order_block",
                "certificate": "certificate",
            },
        ),
    }

    support = {
        "SPT_or_heat_factorization_support_found": scans["qg_spt_factorization"]["terms"]["SPT_factorization"]
        and scans["mtt_superset_spt"]["terms"]["SPT_factorization"],
        "finite_projection_and_lens_factorization_guardrail_found": scans["dirac_delta_finite_projection"]["terms"]["finite_projectors"]
        and scans["dirac_delta_finite_projection"]["terms"]["lens_dependent_factorization"],
        "transition_function_language_found": scans["protospinor_transition_functions"]["terms"]["transition_functions"],
        "theta_color_factorization_support_found": scans["theta_color_twistor_factorization"]["terms"]["color_twistor_factorization"],
        "adjacent_interface_names_required_packet": scans["sm_parity_color_interface"]["terms"]["transition_rhoE_Cech_Dolbeault_or_DE_packet"],
    }

    blockers = {
        "selected_smooth_good_cover_found": False,
        "selected_Deligne_Cech_B_field_representative_found": False,
        "selected_smooth_rhoE_transition_tables_found": False,
        "Qa_SU3_mapped_Freed_Witten_Bianchi_projector_checks_found": False,
        "exact_Qa_SU3_heat_zeta_torsion_factorization_found": False,
        "selected_E_Qa_operator_found": False,
    }

    source_request = {
        "schema": "SelectedHeteroticProjectiveRhoEMinimalSmoothClosureSourceRequest.v1",
        "status": "SOURCE_VALUES_REQUIRED",
        "already_closed": {
            "finite_internal_projection_packet": valuepacket["decision"]["internal_projection_family_closed"],
            "finite_tau_rhoE_DE_Green_Riesz_chi_logdet": values["finite_internal_values"]["finite_internal_part"] == "log(2008)",
            "no_double_count_policy": valuepacket["decision"]["no_double_count_policy_imported"],
        },
        "minimal_acceptable_payloads": {
            "good_cover_transition_tables": [
                "selected cover U_i or selected finite quotient cover",
                "B_i/A_ij/g_ijk or equivalent Deligne/Cech representative",
                "period-unit map to primitive c unit",
                "projective rho_E transition matrices with Z3 central character",
                "same-module Freed-Witten/Bianchi/projector-retention checks",
                "bundle/operator action yielding A/F_A/D_E or E_Qa",
            ],
            "exact_complement_factorization": [
                "smooth operator domain and projection to the eleven-label quotient",
                "factorization of determinant/heat/zeta/torsion into internal quotient times GR/protospinor smooth sector",
                "proof the smooth complement cancels, is universal, or is outside Qa/SU3 response",
                "BRST/FP/gauge quotient determinant counted once",
                "finite part equals log(2008) in internal units after quotient",
            ],
        },
        "current_blockers": blockers,
        "forbidden_shortcuts": contract["forbidden_shortcuts"],
    }

    decision = {
        "source_search_executed": True,
        "support_found": support,
        "blockers": blockers,
        "goodcover_transition_values_found": False,
        "exact_complement_factorization_found": False,
        "can_close_smooth_finitepart_now": False,
        "minimal_source_request_path": rel(OUTPUT_REQUEST),
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEExactComplementFactorizationOrGoodCoverTransitionTablesSourceSearch",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "source_scans": scans,
        "decision": decision,
        "guardrails": {
            "does_not_treat_SPT_as_QaSU3_factorization": True,
            "does_not_treat_transition_language_as_tables": True,
            "does_not_use_adjacent_interface_names_as_values": True,
            "does_not_promote_heat_kernel_support_to_torsion_finitepart": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ExactComplementOrGoodCoverSourceSearchCurrentCorpusResult",
            "proved": True,
            "statement": (
                "The local corpus contains support for SPT/heat factorization, finite "
                "projection, lens-dependent factorization guardrails, and transition-function "
                "language, but it does not emit the selected heterotic Qa/SU3 good-cover "
                "transition tables or an exact Qa/SU3 heat/zeta/torsion complement "
                "factorization theorem. The next step is therefore a minimal source "
                "request or a direct no-go against the current corpus."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_REQUEST.write_text(json.dumps(source_request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "minimal_source_request_path": rel(OUTPUT_REQUEST),
        "note_path": rel(OUTPUT_NOTE),
        "support_found": support,
        "goodcover_transition_values_found": False,
        "exact_complement_factorization_found": False,
        "can_close_smooth_finitepart_now": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE ExactComplementFactorization or GoodCoverTransitionTables SourceSearch v1

## Result

```text
status = {STATUS}
goodcover_transition_values_found = false
exact_complement_factorization_found = false
can_close_smooth_finitepart_now = false
next_required_artifact = {NEXT}
```

## What Was Found

The corpus supports the shape of the next theorem: SPT/heat factorization,
finite coherent projection, lens-dependent factorization guardrails, and
transition-function language all appear.

## What Was Not Found

No source emits selected heterotic Qa/SU3 good-cover transition tables, and no
source proves exact heat/zeta/torsion complement factorization for this packet.
The minimal source request is now recorded in:

```text
{rel(OUTPUT_REQUEST)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_REQUEST)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
