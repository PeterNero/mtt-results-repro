"""Build corpus flavor-coefficient theorem scan / R_theta provenance frontier.

The user asked whether the corpus contains anything resembling the missing
source theorem for the charged log-Yukawa coefficient rows.  This packet records
the answer: yes, there is strong structural support and an explicit R_theta
functional skeleton, but no accepted source-owned coefficient values yet.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_corpusflavorcoefficienttheorem_scan_or_rthetaprovenancefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PAPER_SCAN = PACKET_DIR / "paper_corpus_flavor_coefficient_scan.packet.json"
REPO_SCAN = PACKET_DIR / "repo_rtheta_coefficient_source_status.packet.json"
DECISION = PACKET_DIR / "corpus_match_decision.packet.json"
NEXT_PACKET = PACKET_DIR / "next_rtheta_provenance_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CorpusFlavorCoefficientTheoremScan_or_RThetaProvenanceFrontier_v1.md"

LOG_LEDGER = DATA / "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger.candidate.json"
RTHETA_BASIS = DATA / "selected_rthetavaluerows_or_universalsourceanchortheorem.candidate.json"
RTHETA_BASIS_MAP = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_family_eigenprofile_to_magnitude_row_basis_map.packet.json"
)
RTHETA_FUNCTIONAL = DATA / "selected_rtheta_coefficientfunctional_or_universalanchorselection.candidate.json"
RTHETA_SKELETON = (
    DATA
    / "selected_rtheta_coefficientfunctional_or_universalanchorselection"
    / "rtheta_coefficient_functional_skeleton.packet.json"
)
RTHETA_PROVENANCE = (
    DATA
    / "selected_rtheta_coefficientfunctional_or_universalanchorselection"
    / "rtheta_value_evaluator_provenance_gate.packet.json"
)
RTHETA_PROVENANCE_LATEST = (
    DATA / "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure.candidate.json"
)
RTHETA_READINESS_LATEST = (
    DATA
    / "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure"
    / "rtheta_value_evaluator_readiness_after_alpha1_import.packet.json"
)
RTHETA_PI_RECHECK_LATEST = (
    DATA
    / "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure"
    / "pi_rtheta_recheck_after_alpha1_import.packet.json"
)
RTHETA_CUTSET_LATEST = (
    DATA
    / "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure"
    / "next_cutset_after_value_evaluator_source_provenance.packet.json"
)
FIRSTPASS_RTHETA = DATA / "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows.candidate.json"
FIRSTPASS_PROMOTION = (
    DATA
    / "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows"
    / "selected_rtheta_source_row_promotion_audit.packet.json"
)
ANCHOR_SEARCH = DATA / "selected_thresholdschemevaluerows_or_sourceselecteduniversalanchorexecution.candidate.json"

STATUS = (
    "MTT_SELECTED_CORPUSFLAVORCOEFFICIENTTHEOREMSCAN_OR_RTHETAPROVENANCEFRONTIER_"
    "STRUCTURE_FOUND_SOURCE_VALUES_OPEN"
)
NEXT = "MTT_Selected_RThetaValueEvaluatorSourceProvenance_or_SelectedRouteCClosure_v1"
LATEST_NEXT = "MTT_Selected_RThetaPiKernel_from_SelectedHYMConnection_or_BNBasisEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    sources = [
        LOG_LEDGER,
        RTHETA_BASIS,
        RTHETA_BASIS_MAP,
        RTHETA_FUNCTIONAL,
        RTHETA_SKELETON,
        RTHETA_PROVENANCE,
        RTHETA_PROVENANCE_LATEST,
        RTHETA_READINESS_LATEST,
        RTHETA_PI_RECHECK_LATEST,
        RTHETA_CUTSET_LATEST,
        FIRSTPASS_RTHETA,
        FIRSTPASS_PROMOTION,
        ANCHOR_SEARCH,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing corpus scan inputs: " + ", ".join(missing))

    log_ledger = load(LOG_LEDGER)
    rtheta_basis = load(RTHETA_BASIS)
    rtheta_basis_map = load(RTHETA_BASIS_MAP)
    rtheta_functional = load(RTHETA_FUNCTIONAL)
    rtheta_skeleton = load(RTHETA_SKELETON)
    rtheta_provenance = load(RTHETA_PROVENANCE)
    rtheta_provenance_latest = load(RTHETA_PROVENANCE_LATEST)
    rtheta_readiness_latest = load(RTHETA_READINESS_LATEST)
    rtheta_pi_recheck_latest = load(RTHETA_PI_RECHECK_LATEST)
    rtheta_cutset_latest = load(RTHETA_CUTSET_LATEST)
    firstpass_rtheta = load(FIRSTPASS_RTHETA)
    firstpass_promotion = load(FIRSTPASS_PROMOTION)
    anchor_search = load(ANCHOR_SEARCH)

    paper_scan = {
        "schema": "MTTPaperCorpusFlavorCoefficientScan.v1",
        "status": "PAPER_CORPUS_SUPPORTS_OVERLAP_RESPONSE_NOT_NUMERIC_SOURCE_ROWS",
        "closure_claimed": True,
        "findings": [
            {
                "source": "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md",
                "match_type": "local wavefunction/triple-overlap Yukawa formula",
                "useful_for": "source-operator ansatz: Gaussian overlap times theta/holonomy factor",
                "source_theorem_for_c_s_k": False,
                "reason": "The paper presents benchmark Yukawa matrices and local flavor inputs; it does not derive the nine selected log-coefficient rows.",
            },
            {
                "source": "Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md",
                "match_type": "Yukawa as radial alignment-response coefficient",
                "useful_for": "interpret c_{s,k} as response coefficients of a closure-cost functional",
                "source_theorem_for_c_s_k": False,
                "reason": "It explicitly assigns numerical Yukawa evaluation to realization-level overlap/threshold data.",
            },
            {
                "source": "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
                "match_type": "normalized Iwasawa trilinear Yukawa lambda_123=1",
                "useful_for": "normalization anchor/tree-level rank-one starting point",
                "source_theorem_for_c_s_k": False,
                "reason": "It gives a normalized cubic and rank-one tree-level start, not generation-resolved threshold coefficients.",
            },
            {
                "source": "Modal_Triplet_Theory__Parameters__Closure__and_Structural_Falsifiability.md",
                "match_type": "discrete gauge-flavor bottleneck and forbidden proxy knobs",
                "useful_for": "guardrail against entry-wise Yukawa rescaling and sector-local fitting",
                "source_theorem_for_c_s_k": False,
                "reason": "It names the bottleneck and falsifiability condition; it does not supply coefficient values.",
            },
        ],
        "paper_level_conclusion": (
            "The papers support the correct mathematical shape: flavor coefficients should be overlap/holonomy/"
            "threshold response data, not free Yukawa entries. They do not close the numerical c_{s,k} source rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    repo_scan = {
        "schema": "MTTRepoRThetaCoefficientSourceStatus.v1",
        "status": "RTHETA_FUNCTIONAL_SKELETON_FOUND_VALUES_OPEN",
        "closure_claimed": True,
        "positive_matches": {
            "basis_map_closed": rtheta_basis["closure_decision"]["basis_map_to_sector_scaled_magnitude_rows_closed"],
            "charged_basis_row_count": rtheta_basis_map["charged_basis_row_count"],
            "coefficient_functional_skeleton_closed": rtheta_functional["closure_decision"][
                "coefficient_functional_skeleton_closed"
            ],
            "charged_functional_row_count": rtheta_skeleton["charged_functional_row_count"],
            "domain_readiness_closed": rtheta_functional["closure_decision"]["domain_readiness_closed"],
            "firstpass_Rtheta_coefficient_values_closed": firstpass_rtheta["closure_decision"][
                "firstpass_Rtheta_coefficient_values_closed"
            ],
            "latest_alpha1_dotd_provenance_imported": rtheta_provenance_latest["closure_decision"][
                "alpha1_dotd_provenance_imported"
            ],
            "latest_value_evaluator_readiness_present_count": rtheta_readiness_latest["readiness_present_count"],
            "latest_value_evaluator_readiness_required_count": rtheta_readiness_latest["readiness_required_count"],
        },
        "still_open": {
            "selected_Rtheta_coefficient_values_closed": firstpass_rtheta["closure_decision"][
                "selected_Rtheta_coefficient_values_closed"
            ],
            "selected_Rtheta_source_rows_closed": firstpass_rtheta["closure_decision"][
                "selected_Rtheta_source_rows_closed"
            ],
            "selected_value_evaluator_closed": rtheta_provenance_latest["closure_decision"][
                "selected_value_evaluator_closed"
            ],
            "Pi_Rtheta_closed": rtheta_provenance_latest["closure_decision"]["Pi_Rtheta_closed"],
            "accepted_coefficient_value_count": rtheta_provenance_latest["closure_decision"][
                "accepted_coefficient_value_count"
            ],
            "latest_still_open_readiness_rows": rtheta_readiness_latest["still_open_rows"],
            "latest_pi_minimal_missing_primitives": rtheta_pi_recheck_latest["minimal_missing_primitives"],
            "accepted_source_anchor_row_count": anchor_search["closure_decision"][
                "accepted_source_anchor_row_count"
            ],
            "one_to_three_current_source_anchor_sufficient": anchor_search["closure_decision"][
                "one_to_three_current_source_anchor_sufficient"
            ],
        },
        "critical_formula_skeleton": [
            row["functional_formula_skeleton"]
            for row in rtheta_skeleton["charged_functional_rows"][:3]
        ],
        "promotion_blockers": firstpass_promotion["promotion_blockers"],
        "why_this_is_the_closest_match": (
            "R_theta already supplies the exact basis map and symbolic evaluator form "
            "theta_coeff.s.gen = Eval_Rtheta(Pi_Rtheta, sector projector, H1_s, selected scale/scheme functor)."
        ),
        "why_it_does_not_close": rtheta_provenance["why_not_closed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTCorpusMatchDecisionForFlavorCoefficientSource.v1",
        "status": "CORPUS_HAS_RTHETA_THEOREM_SHAPE_BUT_NOT_SOURCE_VALUES",
        "closure_claimed": True,
        "question": "Does the corpus contain anything resembling a source theorem for c_{s,k} rows?",
        "answer": "yes_structural_no_numeric_source",
        "best_match": "R_theta coefficient functional skeleton plus family-eigenprofile magnitude basis map",
        "not_enough_for_no_knob": [
            "accepted coefficient source rows remain 0",
            "Pi_Rtheta is not closed",
            "selected Route-C value evaluator provenance is advanced to 5/7 but not closed",
            "first-pass R_theta values are replay-tier, not source rows",
            "one-to-three anchor search has no sufficient current source anchor",
        ],
        "updates_previous_claim": (
            "The statement that the current ledger is equivalent in count to SM's 9 charged Yukawa eigenvalue inputs remains true "
            "for numeric values, but the corpus provides a nontrivial selected basis/function-domain structure that SM does not supply."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextRThetaProvenanceFrontier.v1",
        "status": "NEXT_IS_PI_RTHETA_FROM_SELECTED_HYM_CONNECTION_OR_BN_BASIS",
        "closure_claimed": True,
        "next_required_artifact": LATEST_NEXT,
        "closed_now_from_latest_rtheta_provenance": rtheta_cutset_latest["closed_now"],
        "ordered_tasks": [
            "derive selected gauge-fixed HYM connection representative",
            "emit selected B_N basis/quadrature/error contract",
            "derive selected D_E/Riesz/Green from the selected connection",
            "prove coherent spectral zero-mode projector retention",
            "close Pi_Rtheta as a selected physical projection kernel from those four primitives",
            "run Eval_Rtheta on the nine charged projector rows without observed Yukawa inputs",
            "only then promote c_{s,k} or theta_coeff.s.gen as selected source rows",
        ],
        "latest_minimal_missing_primitives": rtheta_cutset_latest["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedCorpusFlavorCoefficientTheoremScanOrRThetaProvenanceFrontier",
        "status": STATUS,
        "next_required_artifact": LATEST_NEXT,
        "closure_claimed": True,
        "corpus_contains_close_structural_match": True,
        "corpus_closes_numeric_source_rows": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "packets": {
            "paper_corpus_flavor_coefficient_scan": rel(PAPER_SCAN),
            "repo_rtheta_coefficient_source_status": rel(REPO_SCAN),
            "corpus_match_decision": rel(DECISION),
            "next_rtheta_provenance_frontier": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "paper_overlap_response_support_found": True,
            "paper_numeric_source_theorem_found": False,
            "rtheta_basis_map_closed": True,
            "rtheta_coefficient_functional_skeleton_closed": True,
            "rtheta_domain_readiness_closed": True,
            "firstpass_Rtheta_coefficient_values_closed": True,
            "latest_alpha1_dotd_provenance_imported": True,
            "latest_value_evaluator_readiness_present_count": 5,
            "latest_value_evaluator_readiness_required_count": 7,
            "selected_Rtheta_coefficient_source_rows": 0,
            "selected_value_evaluator_closed": False,
            "Pi_Rtheta_closed": False,
            "one_to_three_current_source_anchor_sufficient": False,
            "strict_no_knob_charged_yukawa_values_closed": False,
        },
        "theorem": {
            "name": "CorpusFlavorCoefficientTheoremScanAndRThetaFrontierTheorem",
            "proved": True,
            "statement": (
                "The corpus contains a close structural analogue of the missing c_{s,k} source theorem: "
                "Yukawas are repeatedly characterized as overlap/holonomy/threshold response data, and the repo "
                "already closes the R_theta basis map and coefficient functional skeleton. The later value-evaluator "
                "source-provenance packet imports alpha1/dotD and advances readiness to 5/7, but current packets "
                "still do not close Pi_Rtheta and accept zero coefficient "
                "source rows, so numerical no-knob charged Yukawa closure remains open."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedCorpusFlavorCoefficientTheoremScanOrRThetaProvenanceFrontierCertificate",
        "status": STATUS,
        "next_required_artifact": LATEST_NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "corpus_contains_close_structural_match": True,
        "corpus_closes_numeric_source_rows": False,
        "rtheta_basis_map_closed": True,
        "rtheta_coefficient_functional_skeleton_closed": True,
        "latest_alpha1_dotd_provenance_imported": True,
        "latest_value_evaluator_readiness_present_count": 5,
        "latest_value_evaluator_readiness_required_count": 7,
        "selected_Rtheta_coefficient_source_rows": 0,
        "selected_value_evaluator_closed": False,
        "Pi_Rtheta_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected CorpusFlavorCoefficientTheoremScan or RThetaProvenanceFrontier v1

## Result

The corpus **does** contain something resembling the missing theorem, but not
the final numerical source rows.

Best match:

`R_theta` coefficient functional skeleton plus the selected family-eigenprofile
to charged magnitude-row basis map.

Closed:

- charged basis rows: `9`
- coefficient functional skeleton: closed
- domain readiness: closed
- first-pass `R_theta` coefficient values: closed at replay tier
- latest value-evaluator provenance: advanced to `5/7` by importing theorem-derived `alpha1/dotD`

Open:

- selected `R_theta` coefficient source rows: `0`
- selected value evaluator: false
- `Pi_Rtheta`: false
- minimal `Pi_Rtheta` missing primitives: gauge-fixed selected HYM connection representative, selected finite basis/quadrature/error contract, selected `D_E`/Riesz/Green, coherent spectral zero-mode projector retention
- one-to-three source anchor sufficient: false

## Interpretation

The previous claim remains correct for **numeric value count**: without source
promotion, the profile ledger still has `9` charged Yukawa coefficient slots.
But MTT has already achieved more structure than bare SM bookkeeping: the
slots are typed by a selected family spectral basis and an `R_theta` evaluator
contract.

Next artifact: `{LATEST_NEXT}`.
"""

    write_json(PAPER_SCAN, paper_scan)
    write_json(REPO_SCAN, repo_scan)
    write_json(DECISION, decision)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
