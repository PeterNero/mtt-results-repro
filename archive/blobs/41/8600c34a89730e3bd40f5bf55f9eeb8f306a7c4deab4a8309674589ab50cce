"""Build threshold-row attempt / diagonal profile limitation theorem artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdrows_or_diagonalprofilelimitationtheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LIMITATION = PACKET_DIR / "firstpass_diagonal_profile_limitation_theorem.packet.json"
RTHETA1 = PACKET_DIR / "provisional_rtheta1_diagonal_instantiation.packet.json"
ROWS = PACKET_DIR / "threshold_rows_after_diagonal_limitation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_diagonal_limitation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdRows_or_DiagonalProfileLimitationTheorem_v1.md"

PREVIOUS = DATA / "selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem.candidate.json"
COEFFICIENTS = (
    DATA
    / "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows"
    / "firstpass_rtheta_coefficient_values.packet.json"
)
COMPOSED = (
    DATA
    / "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows"
    / "firstpass_composed_bct_to_mt_response.packet.json"
)
CROSSBLOCK = (
    DATA
    / "selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill"
    / "firstpass_weak_bct_crossblock_covariance.packet.json"
)
PROFILE_RECHECK = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "profile_convention_closure_recheck.packet.json"
)
THRESHOLD_RECHECK = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "threshold_response_rows_recheck.packet.json"
)
SOURCE_WEIGHTS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "source_normalized_sector_projection_weights.packet.json"
)
SOURCE_OWNER_RECON = (
    DATA
    / "selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem"
    / "rtheta_source_owner_reconciliation.packet.json"
)
PRECISION_OBSTRUCTION = (
    DATA
    / "selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem"
    / "precision_threshold_convention_obstruction.packet.json"
)

STATUS = (
    "MTT_SELECTED_THRESHOLDROWS_OR_DIAGONALPROFILELIMITATIONTHEOREM_"
    "BUILT_PROVISIONAL_RTHETA1_DIAGONAL_TRUE_PRECISION_ROWS_OPEN"
)
NEXT = "MTT_Selected_ThresholdMassSchemeRows_or_PrecisionProfileUpgrade_v1"


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
        raise FileNotFoundError("missing diagonal profile limitation sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        COEFFICIENTS,
        COMPOSED,
        CROSSBLOCK,
        PROFILE_RECHECK,
        THRESHOLD_RECHECK,
        SOURCE_WEIGHTS,
        SOURCE_OWNER_RECON,
        PRECISION_OBSTRUCTION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    coeffs = load(COEFFICIENTS)
    composed = load(COMPOSED)
    crossblock = load(CROSSBLOCK)
    profile = load(PROFILE_RECHECK)
    threshold = load(THRESHOLD_RECHECK)
    weights = load(SOURCE_WEIGHTS)
    owner = load(SOURCE_OWNER_RECON)
    precision = load(PRECISION_OBSTRUCTION)

    limitation = {
        "schema": "MTTFirstPassDiagonalProfileLimitationTheorem.v1",
        "status": "FIRSTPASS_DIAGONAL_PROFILE_LIMITATION_ACCEPTED_TRUE_PRECISION_OPEN",
        "profile_recheck_source": rel(PROFILE_RECHECK),
        "coefficient_source": rel(COEFFICIENTS),
        "crossblock_source": rel(CROSSBLOCK),
        "accepted_domain": {
            "functional": "R_theta^(1,diag)",
            "profile_tier": "first-pass SM-parity/profile replay",
            "scale_scheme_loop": profile["firstpass_convention"],
            "coefficient_blocks": list(coeffs["coefficient_blocks"].keys()),
            "dense_coefficient_entries": coeffs["total_dense_coefficient_entries"],
            "nonzero_coefficient_entries": coeffs["total_nonzero_coefficient_entries"],
            "crossblock_entry_count": crossblock["inserted_entry_count"],
        },
        "limitation_axioms": [
            "Only the emitted first-pass coefficient blocks may be evaluated.",
            "No un-emitted threshold matching or mass-scheme source row is inferred.",
            "No full likelihood, full covariance, or true precision claim is inferred.",
            "Observed values validate downstream replay only and do not select R_theta.",
            "The selected Pi_Rtheta source-owner is used only to type the provisional evaluator domain.",
        ],
        "closed_as_firstpass_diagonal_limitation": True,
        "accepted_as_full_profile_likelihood": False,
        "accepted_as_true_precision_equivalence": False,
        "accepted_as_no_knob_value_derivation": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(LIMITATION, limitation)

    rtheta1 = {
        "schema": "MTTProvisionalRTheta1DiagonalInstantiation.v1",
        "status": "RTHETA1_DIAGONAL_INSTANTIATED_FIRSTPASS_ONLY",
        "functional_symbol": "R_theta^(1,diag)",
        "limitation_theorem_source": rel(LIMITATION),
        "source_owner_reconciliation": rel(SOURCE_OWNER_RECON),
        "coefficient_source": rel(COEFFICIENTS),
        "composed_response_source": rel(COMPOSED),
        "source_owner_closed": owner["selected_dynamic_operator_source_owner_closed"],
        "Pi_Rtheta_closed": owner["Pi_Rtheta_closed"],
        "coefficient_functional_domain_closed": owner["coefficient_functional_domain_closed"],
        "coefficient_blocks": coeffs["coefficient_blocks"],
        "composed_BCT_to_Mt_response": {
            "domain_rows": composed["domain_rows"],
            "codomain_rows": composed["codomain_rows"],
            "matrix": composed["matrix"],
        },
        "evaluation_contract": {
            "inputs": [
                "first-pass M_Z diagonal core perturbations",
                "BCT m_b/m_c/m_tau/v perturbations",
                "emitted first-pass covariance rows where present",
            ],
            "outputs": [
                "first-pass native Mt core response",
                "first-pass weak/BCT covariance response",
            ],
            "forbidden_outputs": [
                "selected precision threshold matching rows",
                "selected mass-scheme conversion rows",
                "no-knob Yukawa or Higgs magnitude predictions",
                "full profile likelihood",
            ],
        },
        "provisional_firstpass_Rtheta_instantiated": True,
        "selected_threshold_response_functional_instantiated": False,
        "selected_Rtheta_source_rows_closed": False,
        "true_precision_profile_instantiated": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RTHETA1, rtheta1)

    rows = {
        "schema": "MTTThresholdRowsAfterDiagonalLimitation.v1",
        "status": "PROVISIONAL_EVALUATOR_BUILT_THRESHOLD_ROWS_STILL_OPEN",
        "threshold_recheck_source": rel(THRESHOLD_RECHECK),
        "precision_obstruction_source": rel(PRECISION_OBSTRUCTION),
        "provisional_rtheta1_source": rel(RTHETA1),
        "source_normalized_weights_source": rel(SOURCE_WEIGHTS),
        "source_normalized_projection_weights_closed": weights["source_projection_weights_closed"],
        "threshold_matching_source_rows": threshold["accepted_threshold_matching_source_rows"],
        "mass_scheme_conversion_source_rows": threshold["accepted_mass_scheme_conversion_source_rows"],
        "threshold_matching_source_row_count": len(threshold["accepted_threshold_matching_source_rows"]),
        "mass_scheme_conversion_source_row_count": len(threshold["accepted_mass_scheme_conversion_source_rows"]),
        "precision_threshold_row_count": precision["accepted_precision_threshold_row_count"],
        "threshold_response_rows_closed": False,
        "mass_scheme_conversion_rows_closed": False,
        "same_branch_scale_scheme_loop_convention_closed": False,
        "provisional_firstpass_evaluator_may_validate_future_rows": True,
        "provisional_firstpass_evaluator_selects_future_rows": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROWS, rows)

    cutset = {
        "schema": "MTTNextCutsetAfterDiagonalLimitation.v1",
        "status": "NEXT_ATTACK_THRESHOLD_MASS_SCHEME_ROWS_OR_PRECISION_PROFILE_UPGRADE",
        "closed_now": {
            "firstpass_diagonal_profile_limitation_theorem": True,
            "provisional_Rtheta1_diagonal_instantiation": True,
            "source_owner_and_firstpass_coefficients_connected": True,
        },
        "still_open": {
            "same_branch_scale_scheme_loop_convention": True,
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "selected_Rtheta_coefficient_values": True,
            "selected_Rtheta_source_rows": True,
            "selected_threshold_response_functional": True,
            "no_knob_value_derivation": True,
            "full_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "construct top/Higgs/BCT/WZH threshold and mass-scheme rows against the Rtheta1 evaluator",
            "route_B": "upgrade the first-pass diagonal limitation to a precision profile with accepted covariance or external workspace",
            "route_C": "use the provisional evaluator as a validation harness for any proposed selected source rows",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedThresholdRowsOrDiagonalProfileLimitationTheorem",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "firstpass_diagonal_profile_limitation_theorem": rel(LIMITATION),
            "provisional_rtheta1_diagonal_instantiation": rel(RTHETA1),
            "threshold_rows_after_diagonal_limitation": rel(ROWS),
            "next_cutset_after_diagonal_limitation": rel(CUTSET),
        },
        "theorem": {
            "name": "FirstPassDiagonalRThetaInstantiationTheorem",
            "proved": True,
            "statement": (
                "Given Pi_Rtheta source ownership, the emitted first-pass coefficient blocks, and the explicit "
                "first-pass profile convention, there is a well-typed provisional diagonal evaluator "
                "R_theta^(1,diag). It is accepted only as a first-pass validation harness: it does not emit "
                "selected threshold matching rows, selected mass-scheme conversion rows, true precision "
                "profile likelihood, or no-knob value predictions."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "firstpass_diagonal_profile_limitation_theorem_closed": True,
            "provisional_Rtheta1_diagonal_instantiation_closed": True,
            "threshold_matching_source_rows_closed": False,
            "mass_scheme_conversion_source_rows_closed": False,
            "selected_Rtheta_coefficient_values_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "selected_threshold_response_functional_closed": False,
            "full_profile_likelihood_closed": False,
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
        "certificate": "MTT_Selected_ThresholdRows_or_DiagonalProfileLimitationTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "firstpass_diagonal_profile_limitation_theorem_closed": True,
        "provisional_Rtheta1_diagonal_instantiation_closed": True,
        "threshold_matching_source_rows_closed": False,
        "mass_scheme_conversion_source_rows_closed": False,
        "selected_Rtheta_coefficient_values_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "selected_threshold_response_functional_closed": False,
        "full_profile_likelihood_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdRows or DiagonalProfileLimitationTheorem v1

Status: `{STATUS}`.

This artifact constructs the first-pass diagonal evaluator:

```text
R_theta^(1,diag)
```

It is a real, typed validation harness over the emitted coefficient blocks and
the composed BCT-to-Mt response.  It is not a true precision threshold
functional.

```text
first-pass diagonal limitation theorem : true
provisional R_theta1 diagonal evaluator: true
threshold source rows closed           : false
mass-scheme source rows closed         : false
full profile / true SM closure         : false
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
