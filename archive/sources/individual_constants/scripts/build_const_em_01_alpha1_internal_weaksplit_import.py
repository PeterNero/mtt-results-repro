"""Build CONST-EM-01 internal weak-split import.

This supersedes the prior source-emission-open state for the scoped internal
dimensionless row by importing the newer QA finite-part/index-scale and
same-scheme weak-split theorems.  It still does not claim physical alpha.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_internal_weaksplit_import"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT = BASE / "qa_internal_weaksplit_import.packet.json"
PROMOTION = BASE / "internal_threshold_promotion.packet.json"
BOUNDARY = BASE / "physical_alpha_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_InternalWeakSplitImport_v1.md"

STATUS = "MTT_CONST_EM_01_INTERNAL_WEAKSPLIT_IMPORTED_PHYSICAL_ALPHA_OPEN"


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
    BASE.mkdir(parents=True, exist_ok=True)

    finitepart_path = QA_SU3 / "candidate_data" / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json"
    weaksplit_path = QA_SU3 / "candidate_data" / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json"
    finitepart_cert_path = QA_SU3 / "certificates" / "selected_electroweak_qastack_finitepart_policy_and_indexscale_certificate.json"
    weaksplit_cert_path = QA_SU3 / "certificates" / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor_certificate.json"
    prior_path = DATA / "const_em_01_alpha1_u1y_factorized_operator_source.candidate.json"

    finitepart = load(finitepart_path)
    weaksplit = load(weaksplit_path)
    finitepart_cert = load(finitepart_cert_path)
    weaksplit_cert = load(weaksplit_cert_path)
    prior = load(prior_path)

    selected = weaksplit["selected_internal_threshold_vector"]
    import_checks = {
        "finitepart_theorem_proved": finitepart["theorem"]["proved"] is True,
        "selected_p_a_internal_promoted": finitepart["decision"]["selected_p_a_internal_promoted"] is True,
        "selected_p_a_internal_value_matches": abs(finitepart["decision"]["selected_p_a_internal_value"] - 29.201650332199108) < 1e-12,
        "finitepart_lambda12_still_open": finitepart["decision"]["lambda_12_closed"] is False,
        "weaksplit_theorem_proved": weaksplit["theorem"]["proved"] is True,
        "qa_stack_p_a_source_closed": weaksplit["decision"]["Qa_stack_p_a_source_closed"] is True,
        "typed_hypercharge_map_closed": weaksplit["decision"]["typed_hypercharge_map_closed"] is True,
        "same_scheme_SU2_row_closed": weaksplit["decision"]["same_scheme_SU2_row_or_cancellation_closed"] is True,
        "lambda12_internal_closed": weaksplit["decision"]["lambda_12_internal_closed"] is True,
        "physical_K_gauge_anchor_open": weaksplit["decision"]["physical_K_gauge_anchor_closed"] is False,
        "measured_electroweak_closure_open": weaksplit["decision"]["measured_electroweak_closure"] is False,
        "target_fitting_excluded": weaksplit["target_fitting_used"] is False and finitepart["target_fitting_used"] is False,
        "no_observed_electroweak_data": weaksplit["guardrails"]["uses_observed_electroweak_data"] is False,
    }
    internal_import_ok = all(import_checks.values())

    import_packet = {
        "schema": "MTTConstEM01QAInternalWeakSplitImport.v1",
        "status": "QA_INTERNAL_WEAKSPLIT_IMPORT_PASS" if internal_import_ok else "QA_INTERNAL_WEAKSPLIT_IMPORT_FAIL",
        "active_label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A6-SOURCE-EMISSION-THEOREM",
        "inputs": {
            "finitepart_policy_indexscale": rel(finitepart_path),
            "finitepart_certificate": rel(finitepart_cert_path),
            "weaksplit_threshold": rel(weaksplit_path),
            "weaksplit_certificate": rel(weaksplit_cert_path),
            "prior_local_replay": rel(prior_path),
        },
        "import_checks": import_checks,
        "supersedes_prior_open_item": {
            "prior_status": prior["status"],
            "prior_open_item": "selected_source_emission_of_A_base_tensor_I3",
            "superseding_route": "direct finite-part/index-scale source theorem on the quotiented table plus same-scheme SU2 weak-split row",
            "scope": "internal dimensionless weak-split only",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    promotion = {
        "schema": "MTTConstEM01InternalThresholdPromotion.v1",
        "status": "INTERNAL_P_A_P_Y_LAMBDA12_PROMOTED",
        "active_label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A6-SOURCE-EMISSION-THEOREM",
        "promoted_internal_values": {
            "p_a_internal": selected["p_a_internal"],
            "p_c_weaksplit": selected["p_c_weaksplit"],
            "p_SU2_weaksplit": selected["p_SU2_weaksplit"],
            "p_Y_internal": selected["p_Y_internal"],
            "lambda_12_internal": selected["lambda_12_internal"],
            "Delta_G12_internal": selected["Delta_G12_internal"],
            "v1_tilde": selected["v1_tilde"],
        },
        "formulae": selected["formulae"],
        "same_scheme_argument": weaksplit["same_scheme_argument"],
        "scope": "dimensionless internal weak-split threshold; not physical electroweak matching",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "internal_closure_claimed": internal_import_ok,
    }

    boundary = {
        "schema": "MTTConstEM01PhysicalAlphaBoundaryAfterInternalWeakSplit.v1",
        "status": "PHYSICAL_ALPHA_STILL_OPEN_AFTER_INTERNAL_WEAKSPLIT",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS",
        "closed_internal": {
            "p_a_internal": True,
            "p_Y_internal": True,
            "lambda_12_internal": True,
            "Delta_G12_internal": True,
        },
        "open_physical": {
            "physical_K_gauge_or_action_unit": True,
            "matching_scale": True,
            "RG_threshold_scheme": True,
            "alpha_zero": True,
            "alpha_MZ": True,
            "measured_electroweak_closure": True,
        },
        "why_not_alpha_yet": [
            "The imported closure is dimensionless internal weak-split threshold data.",
            "It does not select the physical gauge/action anchor K_phys.",
            "It does not select the matching scale or RG/threshold scheme.",
            "It does not compute alpha(0), alpha(M_Z), or a measured electroweak input scheme.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterInternalWeakSplitImport.v1",
        "status": "NEXT_WORKORDER_PHYSICAL_ANCHOR",
        "primary": {
            "label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS",
            "task": "Search GR/M-theory/dimensional-anchor branches for the target-independent physical gauge/action anchor K_phys or equivalent action unit.",
        },
        "secondary": {
            "label": "CONST-EM-01 / ALPHA1-RG-SCHEME / A6-MATCHING-RUNNING",
            "task": "After K_phys, construct matching scale and RG/threshold scheme to compare internal weak-split data to alpha(M_Z) or alpha(0).",
        },
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1InternalWeakSplitImport",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A6-SOURCE-EMISSION-THEOREM",
        "output_packets": {
            "qa_internal_weaksplit_import": rel(IMPORT),
            "internal_threshold_promotion": rel(PROMOTION),
            "physical_alpha_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "selected_p_a_internal": internal_import_ok,
            "selected_p_Y_internal": internal_import_ok,
            "selected_lambda_12_internal": internal_import_ok,
            "selected_Delta_G12_internal": internal_import_ok,
            "same_scheme_SU2_row_or_cancellation_for_internal_weaksplit": internal_import_ok,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "physical_K_gauge_or_action_unit": True,
            "matching_scale": True,
            "RG_threshold_scheme": True,
            "alpha_zero_or_MZ_value": True,
            "measured_electroweak_closure": True,
            "full_constants_closure": True,
        },
        "theorem": {
            "name": "CONSTEM01InternalWeakSplitImportTheorem",
            "proved": internal_import_ok,
            "statement": (
                "The newer QA finite-part/index-scale theorem promotes the quotient logdet only as internal p_a, "
                "and the same-scheme SU2/typed-hypercharge theorem then closes p_Y, lambda_12, and Delta_G12 "
                "in dimensionless internal weak-split units. This supersedes the earlier local source-emission-open "
                "state for internal p_a, but does not close physical alpha because K_phys, matching scale, and RG/threshold scheme remain open."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "internal_closure_claimed": internal_import_ok,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_InternalWeakSplitImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "p_a_internal": selected["p_a_internal"],
        "p_Y_internal": selected["p_Y_internal"],
        "lambda_12_internal": selected["lambda_12_internal"],
        "Delta_G12_internal": selected["Delta_G12_internal"],
        "physical_alpha_value_claimed": False,
        "physical_K_gauge_anchor_closed": False,
        "next_primary": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Internal WeakSplit Import v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-U1Y-ROW / A6-SOURCE-EMISSION-THEOREM`

## Result

The newer QA-SU3 electroweak stack artifacts supersede the prior local
source-emission-open state, but only in the scoped internal dimensionless
threshold sense.

Promoted internal values:

- `p_a_internal = 29.201650332199108`,
- `p_Y_internal = 1.4217420994950278`,
- `lambda_12_internal = 2.6179362173268497`,
- `Delta_G12_internal = 0.08450302790361214`.

This is not the forbidden shortcut `p_a = p_Y`; it uses the typed map
`p_Y = p_a/36 + p_c/4` with selected Qc and SU2 weak-split rows.

## Boundary

Still open:

- physical `K_gauge` / action anchor,
- matching scale,
- RG/threshold scheme,
- `alpha(0)`,
- `alpha(M_Z)`,
- measured electroweak closure.

No observed electroweak value or target witness is used.

## Next

Next label: `CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS`
"""

    for path, payload in [
        (IMPORT, import_packet),
        (PROMOTION, promotion),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
