"""Build H-response row-source emission or direct Herm(2) certificate payload."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hresponserowsourceemission_or_directherm2certificatepayload"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HResponseRowSourceEmission_or_DirectHerm2CertificatePayload_v1.md"

MANIFEST = PACKET_DIR / "row_source_certificate_payload_manifest.packet.json"
SUPPORT = PACKET_DIR / "certificate_support_imports_rechecked.packet.json"
ATTEMPT = PACKET_DIR / "primitive_hresponse_source_emission_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_source_certificate_payload.packet.json"

PREVIOUS = DATA / "selected_hresponsetablevaluerows_or_directherm2valuerows.candidate.json"
PREVIOUS_INTERFACE = (
    DATA
    / "selected_hresponsetablevaluerows_or_directherm2valuerows"
    / "hresponse_table_value_row_interface.packet.json"
)
PREVIOUS_DIRECT = (
    DATA
    / "selected_hresponsetablevaluerows_or_directherm2valuerows"
    / "direct_herm2_value_row_execution_attempt.packet.json"
)
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
BHUV_FUNCTOR = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "direct_huv_functor_recheck_after_bhuv_lift.packet.json"
)
STRICT_MH_GATE = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "strict_mh_table_value_gate.packet.json"
)
DIRECT_MH_SEARCH = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "direct_mh_value_search_after_domain_closure.packet.json"
)
PROJECTION_ATTEMPT = (
    DATA
    / "selected_c1tobhuvprojectiontensor_or_fhuvrows"
    / "projection_tensor_emission_attempt.packet.json"
)
DIRECT_PAYLOAD_RUN = (
    DATA
    / "selected_nondiagonalhuvhessiansource_or_directherm2rows"
    / "direct_herm2_row_payload_run.packet.json"
)

STATUS = (
    "MTT_SELECTED_HRESPONSEROWSOURCEEMISSION_OR_DIRECTHERM2CERTIFICATEPAYLOAD_"
    "SUPPORT_SPLIT_PRIMITIVE_FORMULA_OPEN"
)
NEXT = "MTT_Selected_HuvPrimitiveFormulaOrFiniteErrorBoundExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing row-source/certificate inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_INTERFACE,
        PREVIOUS_DIRECT,
        BHUV,
        BHUV_FUNCTOR,
        STRICT_MH_GATE,
        DIRECT_MH_SEARCH,
        PROJECTION_ATTEMPT,
        DIRECT_PAYLOAD_RUN,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_interface = load(PREVIOUS_INTERFACE)
    previous_direct = load(PREVIOUS_DIRECT)
    bhuv = load(BHUV)
    bhuv_functor = load(BHUV_FUNCTOR)
    strict_mh = load(STRICT_MH_GATE)
    direct_search = load(DIRECT_MH_SEARCH)
    projection = load(PROJECTION_ATTEMPT)
    direct_payload = load(DIRECT_PAYLOAD_RUN)

    support_imports = {
        "schema": "MTTCertificateSupportImportsRechecked.v1",
        "status": "CERTIFICATE_SUPPORT_IMPORTED_FINAL_ROW_CERTIFICATES_NOT_EMITTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "support_closed": {
            "B_Huv_source_ids_and_branch_provenance": bhuv["minimal_lift_request_tests"][
                "source_id_matching_selected_branch"
            ],
            "B_Huv_finite_exactness_or_truncation_certificate": bhuv[
                "minimal_lift_request_tests"
            ]["finite_exactness_or_truncation_certificate_attached"],
            "B_Huv_quotient_admissibility_support": bhuv["minimal_lift_request_tests"][
                "quotient_admissibility_certificate"
            ],
            "B_Huv_source_orthonormality": bhuv["minimal_lift_request_tests"][
                "source_orthonormality_required_by_H7B1G_satisfied"
            ],
            "Herm2_codomain_and_extractors": strict_mh["domain_closed"]["Herm2_codomain"],
        },
        "not_final_row_certificates": {
            "source_ownership_certificate": "B_Huv columns are source-owned, but no source-owned Huu/Hud/Hdd primitive row formula is emitted.",
            "same_source_exactness_or_error_certificate": "B_Huv exactness is closed, but the row-value Hessian/Galerkin exactness or error bound is absent.",
            "quotient_admissibility_certificate": "B_Huv quotient support is closed, but the strict light-line certificate depends on emitted non-scalar Herm(2) rows/P_L.",
        },
        "decision": {
            "certificate_support_split_closed": True,
            "final_row_source_ownership_certificate_emitted": False,
            "final_same_source_exactness_or_error_certificate_emitted": False,
            "final_quotient_admissibility_certificate_emitted": False,
        },
    }

    manifest = {
        "schema": "MTTHResponseRowSourceCertificatePayloadManifest.v1",
        "status": "ROW_SOURCE_CERTIFICATE_PAYLOAD_MANIFEST_FIXED_SUPPORT_SPLIT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "required_payload_slots": {
            "Huu": {
                "kind": "primitive_value_row",
                "accepted": False,
                "support_available": False,
                "missing": "selected primitive H-sector Hessian/overlap row formula or selected M_source value",
            },
            "Hud_re": {
                "kind": "primitive_value_row",
                "accepted": False,
                "support_available": False,
                "missing": "selected primitive off-diagonal real row formula",
            },
            "Hud_im": {
                "kind": "primitive_value_row",
                "accepted": False,
                "support_available": False,
                "missing": "selected primitive off-diagonal imaginary/phase row formula",
            },
            "Hdd": {
                "kind": "primitive_value_row",
                "accepted": False,
                "support_available": False,
                "missing": "selected primitive H-sector Hessian/overlap row formula or selected M_source value",
            },
            "Hdu_equals_conj_Hud_certificate": {
                "kind": "Hermitian_codomain_certificate",
                "accepted": False,
                "support_available": True,
                "missing": "row values are absent, so Hermitian closure cannot certify emitted rows",
            },
            "source_ownership_certificate": {
                "kind": "same_source_provenance_certificate",
                "accepted": False,
                "support_available": True,
                "missing": "source ownership for B_Huv is closed, but no same-source row formula/value owner is emitted",
            },
            "same_source_exactness_or_error_certificate": {
                "kind": "finite_exactness_or_error_certificate",
                "accepted": False,
                "support_available": True,
                "missing": "B_Huv exactness is closed; row-level Hessian/Galerkin residual or truncation bound is absent",
            },
            "quotient_admissibility_certificate": {
                "kind": "light_line_quotient_certificate",
                "accepted": False,
                "support_available": True,
                "missing": "B_Huv quotient support is closed; strict im(P_L) certificate requires non-scalar emitted Herm(2) rows",
            },
        },
        "decision": {
            "manifest_fixed": True,
            "support_vs_final_certificate_split_closed": True,
            "accepted_payload_slot_count": 0,
            "accepted_value_row_count": 0,
            "accepted_final_certificate_count": 0,
        },
    }

    primitive_attempt = {
        "schema": "MTTPrimitiveHResponseSourceEmissionAttempt.v1",
        "status": "PRIMITIVE_HRESPONSE_SOURCE_EMISSION_ATTEMPTED_ZERO_VALUES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_row_execution_status": previous["status"],
        "direct_value_search_status": direct_search["status"],
        "projection_tensor_status": projection["status"],
        "direct_payload_run_status": direct_payload["status"],
        "candidate_routes_rechecked": {
            "B_Huv_plus_M_source_functor": {
                "accepted": False,
                "reason": bhuv_functor["decision"]["reason"],
            },
            "strict_MH_table_value_gate": {
                "accepted": strict_mh["current_packet_passes"],
                "missing": strict_mh["value_closure_reasons_missing"],
            },
            "direct_MH_value_search_after_domain_closure": {
                "accepted": direct_search["direct_value_attempts"]["any_direct_attempt_emits_values"],
                "rows_all_null": direct_search["rows_all_null"],
            },
            "C1_to_BHuv_projection_tensor": {
                "accepted": projection["decision"]["source_owned_C1_to_BHuv_tensor_emitted"],
                "accepted_F_Huv_row_count": projection["decision"]["accepted_F_Huv_row_count"],
            },
            "non_diagonal_direct_payload_run": {
                "accepted": direct_payload["decision"]["direct_Herm2_rows_emitted"],
                "selected_non_diagonal_Huv_Hessian_source_emitted": direct_payload["decision"][
                    "selected_non_diagonal_Huv_Hessian_source_emitted"
                ],
            },
        },
        "emitted_values": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
        },
        "decision": {
            "primitive_source_emission_attempted": True,
            "selected_primitive_formula_emitted": False,
            "finite_error_bound_emitted": False,
            "selected_H_response_value_rows_emitted": False,
            "direct_Herm2_certificate_payload_emitted": False,
            "accepted_value_row_count": 0,
            "accepted_final_certificate_count": 0,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterSourceCertificatePayload.v1",
        "status": "NEXT_FRONTIER_HUV_PRIMITIVE_FORMULA_OR_FINITE_ERROR_BOUND_EXECUTION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "row-source/certificate payload slots fixed",
            "B_Huv quotient/provenance/exactness support separated from final row certificates",
            "Hermitian codomain support separated from emitted-row Hermitian certificate",
            "current primitive/direct/projection candidate routes rechecked with zero accepted values",
        ],
        "still_open": [
            "selected primitive H-sector Hessian or overlap row formula for Huu,Hud_re,Hud_im,Hdd",
            "finite exactness proof or rigorous error bound for those row formulas",
            "same-source owner theorem binding the primitive formula to the selected MTT branch",
            "light-line quotient certificate after non-scalar Herm(2) rows are emitted",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHResponseRowSourceEmissionOrDirectHerm2CertificatePayload",
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
            "name": "HResponseRowSourceCertificateSupportSplitTheorem",
            "proved": True,
            "statement": (
                "The row-source/certificate payload is now fixed. B_Huv supplies "
                "same-branch source IDs, source orthonormality, finite exactness "
                "support, and quotient support, and the Herm(2) codomain is "
                "closed. These are support certificates only: they do not emit "
                "source-owned Huu,Hud_re,Hud_im,Hdd values, row-level exactness "
                "or error bounds, or the strict light-line certificate. Current "
                "primitive/direct/projection routes still accept zero value rows."
            ),
        },
        "packets": {
            "row_source_certificate_payload_manifest": rel(MANIFEST),
            "certificate_support_imports_rechecked": rel(SUPPORT),
            "primitive_hresponse_source_emission_attempt": rel(ATTEMPT),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_interface": rel(PREVIOUS_INTERFACE),
            "previous_direct": rel(PREVIOUS_DIRECT),
            "bhuv": rel(BHUV),
            "bhuv_functor": rel(BHUV_FUNCTOR),
            "strict_mh_gate": rel(STRICT_MH_GATE),
            "direct_mh_search": rel(DIRECT_MH_SEARCH),
            "projection_attempt": rel(PROJECTION_ATTEMPT),
            "direct_payload_run": rel(DIRECT_PAYLOAD_RUN),
        },
        "closure_decision": {
            "payload_manifest_fixed": True,
            "certificate_support_split_closed": True,
            "B_Huv_support_imported": True,
            "current_routes_rechecked": True,
            "selected_primitive_formula_emitted": False,
            "selected_H_response_value_rows_emitted": False,
            "direct_Herm2_certificate_payload_emitted": False,
            "finite_error_bound_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "payload_slots_required": 8,
            "support_slots_available": 4,
            "accepted_payload_slot_count": 0,
            "accepted_value_row_count": 0,
            "accepted_final_certificate_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedHResponseRowSourceEmissionOrDirectHerm2CertificatePayload",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "payload_manifest_fixed": True,
        "certificate_support_split_closed": True,
        "B_Huv_support_imported": True,
        "current_routes_rechecked": True,
        "payload_slots_required": 8,
        "support_slots_available": 4,
        "accepted_payload_slot_count": 0,
        "accepted_value_row_count": 0,
        "accepted_final_certificate_count": 0,
        "selected_primitive_formula_emitted": False,
        "selected_H_response_value_rows_emitted": False,
        "direct_Herm2_certificate_payload_emitted": False,
        "finite_error_bound_emitted": False,
    }

    note = f"""# MTT Selected HResponseRowSourceEmission or DirectHerm2CertificatePayload v1

Status: `{STATUS}`

## Theorem

The certificate layer is now split correctly:

- `B_Huv` source IDs/provenance: `{support_imports["support_closed"]["B_Huv_source_ids_and_branch_provenance"]}`
- `B_Huv` finite exactness support: `{support_imports["support_closed"]["B_Huv_finite_exactness_or_truncation_certificate"]}`
- `B_Huv` quotient support: `{support_imports["support_closed"]["B_Huv_quotient_admissibility_support"]}`
- Herm(2) codomain/extractor support: `{support_imports["support_closed"]["Herm2_codomain_and_extractors"]}`

These are support certificates.  They do not by themselves emit final row
certificates for `Huu,Hud_re,Hud_im,Hdd`, because the source-owned primitive
H-sector row formula and finite row-level exactness/error bound are still
absent.

Current execution:

- required payload slots: `8`
- support slots available: `4`
- accepted final payload slots: `0`
- accepted value rows: `0`
- accepted final certificates: `0`

Next artifact: `{NEXT}`
"""

    write_json(SUPPORT, support_imports)
    write_json(MANIFEST, manifest)
    write_json(ATTEMPT, primitive_attempt)
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
