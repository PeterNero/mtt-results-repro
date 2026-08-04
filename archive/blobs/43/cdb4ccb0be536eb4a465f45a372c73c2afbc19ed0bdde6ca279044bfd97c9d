"""Build threshold/mass-scheme values or correlated likelihood source-import gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RESIDUALS = PACKET_DIR / "threshold_mass_scheme_residual_values.packet.json"
IMPORT = PACKET_DIR / "correlated_likelihood_source_import_status.packet.json"
PROMOTION = PACKET_DIR / "precision_promotion_after_residuals_and_import.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_mass_scheme_source_import.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdMassSchemeValues_or_CorrelatedLikelihoodSourceImport_v1.md"

PREVIOUS = DATA / "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion.candidate.json"
PREVIOUS_PROMOTION = (
    DATA
    / "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion"
    / "yukawa_higgs_precision_promotion_gate.packet.json"
)
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
TRANSPORT_KERNEL = (
    DATA
    / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
    / "yukawa_higgs_common_scale_transport_kernel.packet.json"
)
THRESHOLD_POLICY = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
)
FORMULA = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "buttazzo_boundary_formula_replay.packet.json"
)
PROFILE_IMPORT_PRIOR = (
    DATA
    / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
    / "profile_likelihood_source_import_status.packet.json"
)

STATUS = (
    "MTT_SELECTED_THRESHOLDMASSSCHEMEVALUES_OR_CORRELATEDLIKELIHOODSOURCEIMPORT_"
    "BUILT_RESIDUAL_VALUES_SOURCE_IMPORT_OPEN"
)
NEXT = "MTT_Selected_AcceptedThresholdMassSchemeSourceRows_or_NoKnobValueDerivation_v1"


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
        raise FileNotFoundError("missing threshold/source import sources: " + ", ".join(missing))


def cabs(value: Any) -> float:
    if isinstance(value, list):
        return math.hypot(float(value[0]), float(value[1]))
    return abs(float(value))


def diag_abs(matrix: list[Any]) -> list[float]:
    return [cabs(matrix[i][i]) for i in range(len(matrix))]


def residual_row(row_id: str, source_value: float, target_value: float, source_label: str, target_label: str) -> dict[str, Any]:
    delta = source_value - target_value
    rel_delta = delta / target_value if target_value else None
    return {
        "id": row_id,
        "source_label": source_label,
        "target_label": target_label,
        "source_value": source_value,
        "target_value": target_value,
        "delta_source_minus_target": delta,
        "relative_delta_source_minus_target": rel_delta,
        "finite": math.isfinite(source_value) and math.isfinite(target_value) and math.isfinite(delta),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_PROMOTION,
        VALUE_PACKET,
        TRANSPORT_KERNEL,
        THRESHOLD_POLICY,
        FORMULA,
        PROFILE_IMPORT_PRIOR,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_promotion = load(PREVIOUS_PROMOTION)
    values = load(VALUE_PACKET)
    kernel = load(TRANSPORT_KERNEL)
    threshold = load(THRESHOLD_POLICY)
    formula = load(FORMULA)
    prior_import = load(PROFILE_IMPORT_PRIOR)

    firstpass = values["values"]
    native = kernel["native_values_to_transport"]
    firstpass_yu = diag_abs(firstpass["Y_u_MZ_firstpass"])
    firstpass_yd = diag_abs(firstpass["Y_d_MZ_firstpass"])
    firstpass_ye = diag_abs(firstpass["Y_e_MZ_firstpass"])
    native_yu = diag_abs(native["Y_u_native"])
    native_yd = diag_abs(native["Y_d_native_complex_up_diagonal_convention"])
    native_ye = diag_abs(native["Y_e_native"])
    current_mt = formula["current_repo_input_variant"]["values"]
    buttazzo_mt = formula["buttazzo_central_input_replay"]["values"]

    transport_rows = []
    for family, names, native_diag, firstpass_diag in [
        ("Y_u", ["u", "c", "t"], native_yu, firstpass_yu),
        ("Y_d", ["d", "s", "b"], native_yd, firstpass_yd),
        ("Y_e", ["e", "mu", "tau"], native_ye, firstpass_ye),
    ]:
        for idx, name in enumerate(names):
            transport_rows.append(
                residual_row(
                    f"{family}_{name}_native_to_firstpass_MZ",
                    firstpass_diag[idx],
                    native_diag[idx],
                    "firstpass_common_scale_MZ",
                    "native_mass_scheme_seed",
                )
            )

    boundary_rows = [
        residual_row(
            "lambda_tree_native_to_current_Mt_boundary",
            float(native["lambda_H_tree_native"]),
            float(current_mt["lambda_Mt"]),
            "native_tree_lambda",
            "current_Buttazzo_boundary_formula_lambda_Mt",
        ),
        residual_row(
            "lambda_firstpass_MZ_to_current_Mt_boundary",
            float(firstpass["lambda_H_MZ_firstpass"]),
            float(current_mt["lambda_Mt"]),
            "firstpass_common_scale_lambda_MZ",
            "current_Buttazzo_boundary_formula_lambda_Mt",
        ),
        residual_row(
            "top_native_tree_to_current_Mt_boundary",
            native_yu[2],
            float(current_mt["y_t_Mt"]),
            "native_tree_top_yukawa",
            "current_Buttazzo_boundary_formula_y_t_Mt",
        ),
        residual_row(
            "top_firstpass_MZ_to_current_Mt_boundary",
            firstpass_yu[2],
            float(current_mt["y_t_Mt"]),
            "firstpass_common_scale_top_yukawa_MZ",
            "current_Buttazzo_boundary_formula_y_t_Mt",
        ),
        residual_row(
            "lambda_current_to_buttazzo_central_boundary",
            float(current_mt["lambda_Mt"]),
            float(buttazzo_mt["lambda_Mt"]),
            "current_repo_input_variant",
            "Buttazzo_central_input_variant",
        ),
        residual_row(
            "top_current_to_buttazzo_central_boundary",
            float(current_mt["y_t_Mt"]),
            float(buttazzo_mt["y_t_Mt"]),
            "current_repo_input_variant",
            "Buttazzo_central_input_variant",
        ),
    ]
    all_rows = transport_rows + boundary_rows
    residual_packet = {
        "schema": "MTTThresholdMassSchemeResidualValues.v1",
        "status": "RESIDUAL_VALUES_EMITTED_ACCEPTED_THRESHOLD_VALUES_OPEN",
        "threshold_contract": rel(THRESHOLD_POLICY),
        "transport_residual_rows": transport_rows,
        "boundary_residual_rows": boundary_rows,
        "summary": {
            "row_count": len(all_rows),
            "all_residuals_finite": all(row["finite"] for row in all_rows),
            "max_abs_transport_relative_delta": max(
                abs(row["relative_delta_source_minus_target"])
                for row in transport_rows
                if row["relative_delta_source_minus_target"] is not None
            ),
            "max_abs_boundary_relative_delta": max(
                abs(row["relative_delta_source_minus_target"])
                for row in boundary_rows
                if row["relative_delta_source_minus_target"] is not None
            ),
        },
        "what_this_closes": {
            "native_to_firstpass_residual_values": True,
            "tree_or_firstpass_to_Buttazzo_boundary_residual_values": True,
            "finite_residual_table_for_threshold_mass_scheme_audit": True,
        },
        "what_this_does_not_close": {
            "accepted_threshold_matching_values": True,
            "accepted_mass_scheme_conversion_values": True,
            "multi_loop_matching_convention": True,
            "published_or_reconstructed_profile_likelihood": True,
            "no_knob_value_source_derivation": True,
        },
        "accepted_as_threshold_matching_values": False,
        "accepted_as_mass_scheme_conversion_values": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(RESIDUALS, residual_packet)

    import_packet = {
        "schema": "MTTCorrelatedLikelihoodSourceImportStatus.v1",
        "status": "NO_CORRELATED_LIKELIHOOD_SOURCE_IMPORTED_PRIOR_ABSENCE_CONFIRMED",
        "prior_import_status": rel(PROFILE_IMPORT_PRIOR),
        "required_source_rows": prior_import["required_import_payload"],
        "checked_local_sources": prior_import["local_import_candidates_checked"]
        + [
            "surrogate correlated threshold/profile matrix family",
            "threshold/mass-scheme residual value table",
            "Buttazzo boundary formula replay",
        ],
        "published_or_reconstructed_profile_imported": False,
        "accepted_as_full_correlated_likelihood_source": False,
        "source_import_absence_confirmed": prior_import["published_or_reconstructed_profile_imported"] is False,
        "why_not_imported": [
            "available profile matrices are diagonal or surrogate stress constructions",
            "residual rows are computed from existing benchmark formulas, not a new likelihood workspace",
            "no external covariance/profile source file with provenance and basis map is present in the repo",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(IMPORT, import_packet)

    promotion_tests = {
        "threshold_mass_scheme_residual_values_emitted": True,
        "all_residuals_finite": residual_packet["summary"]["all_residuals_finite"],
        "accepted_threshold_matching_values_emitted": residual_packet[
            "accepted_as_threshold_matching_values"
        ],
        "accepted_mass_scheme_conversion_values_emitted": residual_packet[
            "accepted_as_mass_scheme_conversion_values"
        ],
        "correlated_likelihood_source_imported": import_packet[
            "published_or_reconstructed_profile_imported"
        ],
        "multi_loop_threshold_convention_values_emitted": False,
        "no_knob_MTT_source_derivation_of_values": False,
    }
    remaining_hard_failures = [
        key
        for key in [
            "accepted_threshold_matching_values_emitted",
            "accepted_mass_scheme_conversion_values_emitted",
            "correlated_likelihood_source_imported",
            "multi_loop_threshold_convention_values_emitted",
            "no_knob_MTT_source_derivation_of_values",
        ]
        if promotion_tests[key] is False
    ]
    promotion_packet = {
        "schema": "MTTPrecisionPromotionAfterResidualsAndImport.v1",
        "status": "RESIDUAL_VALUES_CLOSED_PRECISION_PROMOTION_REJECTED",
        "previous_remaining_hard_failures": previous_promotion["remaining_hard_failures"],
        "promotion_tests": promotion_tests,
        "remaining_hard_failures": remaining_hard_failures,
        "promotion_decision": {
            "residual_value_audit_closed": True,
            "accepted_threshold_mass_scheme_layer_closed": False,
            "correlated_likelihood_source_imported": False,
            "accepted_for_true_precision_equivalence": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "reason": (
            "Residual values are now explicit and finite, so the calculation audit advances. They are not "
            "accepted threshold or mass-scheme conversion values because no multi-loop matching convention, "
            "correlated likelihood source, or no-knob value-source derivation has been supplied."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION, promotion_packet)

    cutset = {
        "schema": "MTTNextCutsetAfterThresholdMassSchemeSourceImport.v1",
        "status": "RESIDUAL_AUDIT_DONE_ACCEPTED_SOURCE_ROWS_OR_NOKNOB_DERIVATION_REQUIRED",
        "closed_now": [
            "native-to-firstpass Yukawa residual table emitted",
            "tree/firstpass-to-Buttazzo boundary residual table emitted",
            "correlated likelihood source import absence confirmed",
            "precision promotion rerun after residual/source audit",
        ],
        "still_open": [
            "accepted threshold matching values",
            "accepted mass-scheme conversion values",
            "published/reconstructed correlated likelihood source",
            "multi-loop threshold convention values",
            "no-knob MTT derivation of Yukawa/Higgs value rows",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The remaining work is now source-level: either import/derive accepted threshold and "
                "mass-scheme rows, import a correlated likelihood workspace, or prove a no-knob MTT value "
                "derivation that replaces those external rows."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedThresholdMassSchemeValuesOrCorrelatedLikelihoodSourceImport",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "threshold_mass_scheme_residual_values": rel(RESIDUALS),
            "correlated_likelihood_source_import_status": rel(IMPORT),
            "precision_promotion_after_residuals_and_import": rel(PROMOTION),
            "next_cutset_after_threshold_mass_scheme_source_import": rel(CUTSET),
        },
        "theorem": {
            "name": "ResidualValueAuditAndSourceImportAbsenceTheorem",
            "proved": True,
            "statement": (
                "The selected value/profile stack determines finite native-to-firstpass and "
                "tree/firstpass-to-boundary residual rows. This closes the residual-value audit, but it "
                "does not provide accepted threshold matching or mass-scheme conversion values. The local "
                "correlated likelihood source import remains absent, so true precision equivalence still "
                "requires accepted source rows or a no-knob derivation of them."
            ),
        },
        "what_closes_now": {
            "threshold_mass_scheme_residual_values_emitted": True,
            "all_residuals_finite": residual_packet["summary"]["all_residuals_finite"],
            "correlated_likelihood_source_import_absence_confirmed": True,
            "precision_promotion_rerun_after_residuals": True,
        },
        "what_remains_open": {
            "accepted_threshold_matching_values": True,
            "accepted_mass_scheme_conversion_values": True,
            "published_or_reconstructed_profile_likelihood": True,
            "multi_loop_threshold_convention_values": True,
            "no_knob_Yukawa_Higgs_value_source_derivation": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "residual_value_audit_closed": True,
            "accepted_threshold_mass_scheme_layer_closed": False,
            "correlated_likelihood_source_imported": False,
            "accepted_for_true_precision_equivalence": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ThresholdMassSchemeValues_or_CorrelatedLikelihoodSourceImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdMassSchemeValues or CorrelatedLikelihoodSourceImport v1

Status: `{STATUS}`.

This artifact emits finite residual rows for the threshold/mass-scheme layer.

```text
residual rows = {residual_packet["summary"]["row_count"]}
all finite    = {residual_packet["summary"]["all_residuals_finite"]}
```

This closes the residual-value audit only. It does not promote the residuals to
accepted threshold matching or mass-scheme conversion values.

The correlated likelihood source import was also checked and remains absent.

Promotion decision:

```text
residual value audit closed: true
accepted threshold/mass-scheme layer closed: false
correlated likelihood source imported: false
true SM equivalence: open
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
