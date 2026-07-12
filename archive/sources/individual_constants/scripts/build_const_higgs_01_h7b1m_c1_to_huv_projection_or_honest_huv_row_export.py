"""Build CONST-HIGGS-01 H7B1M C1-to-Huv projection route decision."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1m_c1_to_huv_projection_or_honest_huv_row_export"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
C1_TARGET_AUDIT = BASE / "c1_target_sector_support_audit.packet.json"
PROJECTION_DECISION = BASE / "c1_to_huv_projection_route_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1M_C1ToHuvProjectionRouteDecision_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1M_C1_TO_HUV_PROJECTION_TEST_BUILT_HSECTOR_EXTENSION_REQUIRED"


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


def clean_flags() -> dict[str, bool]:
    return {
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1l_path = DATA / "const_higgs_01_h7b1l_dynamic_phifinc1_huv_response_or_independent_huv_hessian.candidate.json"
    h7b1l_gap_path = DATA / "const_higgs_01_h7b1l_dynamic_phifinc1_huv_response_or_independent_huv_hessian" / "huv_projection_gap.packet.json"
    h7b1c_request_path = DATA / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian" / "minimal_two_by_two_hessian_payload_request.packet.json"
    h7b1f_contract_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet" / "nonsplit_to_huv_reduction_contract.packet.json"
    h7b1f_functor_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet" / "basis_invariant_huv_functor_theorem.packet.json"
    dynamic_identity_path = (
        SM_PARITY_REPO
        / "candidate_data"
        / "selected_samesourcedynamictransferidentity_or_independentrowformulaexecution"
        / "same_source_dynamic_transfer_identity_current_gate.packet.json"
    )

    h7b1l = load(h7b1l_path)
    h7b1l_gap = load(h7b1l_gap_path)
    h7b1c_request = load(h7b1c_request_path)
    h7b1f_contract = load(h7b1f_contract_path)
    h7b1f_functor = load(h7b1f_functor_path)
    dynamic_identity = load(dynamic_identity_path)

    sector_norms = dynamic_identity["finite_values_if_identity_proved"]["sector_norm_sq"]
    c1_target_sectors = sorted(sector_norms.keys())
    expected_dim = len(c1_target_sectors) * 3 * 3 * 2
    h_required_basis = h7b1c_request["basis_required"]["ordered_basis"]

    c1_target_audit = {
        "schema": "MTTConstHiggs01H7B1MC1TargetSectorSupportAudit.v1",
        "status": "C1_TARGET_HAS_MATTER_SECTORS_NO_HUV_SECTOR",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1M-C1-TARGET-SECTOR-SUPPORT-AUDIT",
        "input_sources": {
            "H7B1L_candidate": rel(h7b1l_path),
            "H7B1L_projection_gap": rel(h7b1l_gap_path),
            "H7B1C_Huv_payload_request": rel(h7b1c_request_path),
            "H7B1F_Huv_reduction_contract": rel(h7b1f_contract_path),
            "H7B1F_basis_invariant_functor": rel(h7b1f_functor_path),
            "same_source_dynamic_transfer_identity_current_gate": rel(dynamic_identity_path),
        },
        "c1_response_target": {
            "sector_norm_sq_keys": c1_target_sectors,
            "sector_norm_sq": sector_norms,
            "inferred_real_dimension": expected_dim,
            "dimension_formula": "len(sectors) * 3 * 3 * 2",
            "contains_H_sector": "H" in c1_target_sectors,
            "contains_Hu_sector": "H_u" in c1_target_sectors,
            "contains_Hd_dagger_sector": "H_d^dagger" in c1_target_sectors,
            "selected_A_selected_emitted": dynamic_identity["selected_status"]["selected_A_selected_emitted"],
            "selected_b_selected_emitted": dynamic_identity["selected_status"]["selected_b_selected_emitted"],
            "conditional_Gram_exact": dynamic_identity["closed_support"]["conditional_Gram_exact"],
        },
        "huv_required_target": {
            "ordered_basis": h_required_basis,
            "basis_labels_currently_emitted": h7b1c_request["basis_required"]["basis_labels_currently_emitted"],
            "matrix_values_currently_emitted": h7b1c_request["matrix_required"]["values_currently_emitted"],
            "B_Huv_required": h7b1f_contract["required_payload"]["B_Huv"],
            "M_source_required": h7b1f_contract["required_payload"]["M_source"],
            "basis_invariant_functor_proved_conditionally": h7b1f_functor["theorem"]["proved"],
            "conditional_values_open": h7b1f_functor["conditional_values_open"],
        },
        "target_mismatch_result": {
            "plain_C1_target_can_supply_Huv_projection_now": False,
            "reason": "The current 72-real C1 response target enumerates u,d,e,nuD sector matrices, not H, H_u, or H_d^dagger rows. Huv needs a separate UV two-Higgs basis/lift and Hermitian mass-strain target.",
        },
        **clean_flags(),
    }

    projection_decision = {
        "schema": "MTTConstHiggs01H7B1MC1ToHuvProjectionRouteDecision.v1",
        "status": "PLAIN_C1_TO_HUV_PROJECTION_ROUTE_RETIRED_CURRENT_TARGET",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1M-C1-TO-HUV-PROJECTION-ROUTE-DECISION",
        "route_A_plain_C1_projection": {
            "tested": True,
            "passes": False,
            "retired_for_current_target": True,
            "why": [
                "current C1 target sector set is u,d,e,nuD",
                "no H-sector or UV two-Higgs coordinates are present",
                "selected C1 response values are still unpromoted in the strict unpatched tier",
                "even local/patched C1 support lacks the codomain map Pi_Huv or R_H",
            ],
        },
        "route_A_refined": {
            "label": "H-sector dynamic C1 extension",
            "must_emit": [
                "selected H/Huv response coordinates in the dynamic Phi_fin^C1 target",
                "projection/restriction Pi_Huv or R_H from source response to (H_u,H_d^dagger)",
                "Hermitian Huv mass-strain entries with exactness certificate",
                "coefficient and normalization convention",
            ],
        },
        "route_B_still_live": {
            "label": "honest source-owned Huv row export",
            "must_emit": [
                "ordered UV basis (H_u,H_d^dagger)",
                "B_Huv two-column lift or equivalent",
                "M_source Hermitian mass/strain operator or direct Huv table",
                "finite residual/truncation/source certificate",
            ],
        },
        "strict_outputs": {
            "Pi_Huv": None,
            "H_response": None,
            "R_H": None,
            "B_Huv": None,
            "M_source": None,
            "Huv": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "superset_strategy": {
            "combining_paths": True,
            "locked_target": "Huv source row or selected H-sector extension",
            "support_retained": [
                "post-SM-parity C1 normal forms",
                "local/patched C1 source identity as conditional scaffolding",
                "H7B1F conditional Huv functor",
            ],
            "promotion_guardrail": "No generic matter-sector C1 response may be promoted to Huv without an emitted H-sector codomain map.",
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1MNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1N_HSECTOR_DYNAMIC_EXTENSION_OR_HONEST_HUV_ROWS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1M-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1N-HSECTOR-DYNAMIC-EXTENSION-OR-HONEST-HUV-ROWS",
            "task": "Either extend the selected dynamic Phi_fin^C1 target with H/Huv sector response rows, or bypass C1 and emit the source-owned Huv Hermitian mass-strain rows directly.",
        },
        "two_legal_exits": [
            {
                "id": "H7B1N-A",
                "label": "H-sector dynamic C1 extension",
                "must_emit": "selected H/Huv response rows and Pi_Huv/R_H exactness, extending beyond the current u,d,e,nuD 72-real target",
            },
            {
                "id": "H7B1N-B",
                "label": "honest Huv row export",
                "must_emit": "B_Huv and M_source or direct Huv entries, with exactness/error certificates and no observed selectors",
            },
        ],
        "do_not_repeat": [
            "Do not search the existing 72-real matter-sector C1 target as if it contained Huv rows.",
            "Do not promote local/patched C1 closure into strict Huv closure.",
            "Do not use rank-one H:h0 as the UV two-Higgs basis.",
            "Do not backsolve from Higgs mass, lambda_H, beta, threshold residual, Yukawas, CKM, or PMNS.",
        ],
        **clean_flags(),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1MC1ToHuvProjectionRouteDecision",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1M-C1-TO-HUV-PROJECTION-OR-HONEST-HUV-ROW-EXPORT",
        "output_packets": {
            "c1_target_sector_support_audit": rel(C1_TARGET_AUDIT),
            "c1_to_huv_projection_route_decision": rel(PROJECTION_DECISION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "H7B1MCurrentC1TargetHasNoHuvCodomainTheorem",
            "proved": True,
            "statement": (
                "The current dynamic C1 response target is the 72-real matter-sector target over u,d,e,nuD. "
                "It contains no H, H_u, or H_d^dagger sector coordinates and does not emit a codomain map to the Huv Hermitian mass-strain block. "
                "Therefore the plain C1-to-Huv projection route is retired for the current target. "
                "The live exits are an H-sector dynamic C1 extension or an honest Huv row export."
            ),
        },
        "H7B1L_gate_imported": h7b1l["strict_dynamic_Huv_gate_passes"] is False,
        "current_C1_target_sector_set": c1_target_sectors,
        "current_C1_target_contains_H_sector": False,
        "plain_C1_to_Huv_projection_route_passes": False,
        "plain_C1_to_Huv_projection_route_retired_current_target": True,
        "H_sector_dynamic_C1_extension_required": True,
        "honest_Huv_row_export_still_live": True,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1N_HSectorDynamicExtensionOrHonestHuvRows_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1M_C1ToHuvProjectionRouteDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "current_C1_target_contains_H_sector": False,
        "plain_C1_to_Huv_projection_route_passes": False,
        "plain_C1_to_Huv_projection_route_retired_current_target": True,
        "H_sector_dynamic_C1_extension_required": True,
        "honest_Huv_row_export_still_live": True,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1M C1 To Huv Projection Route Decision v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1M-C1-TO-HUV-PROJECTION-OR-HONEST-HUV-ROW-EXPORT`

## Result

```text
current C1 target sectors                  {', '.join(c1_target_sectors)}
current C1 target contains H sector         False
plain C1-to-Huv projection route passes     False
plain route retired for current target      True
H-sector dynamic C1 extension required      True
honest Huv row export still live            True
Huv / Omega / s_beta / lambda_H             False
```

## Route Decision

The current C1 target is the four-sector matter response target
`u,d,e,nuD`, giving `4*3*3*2 = 72` real coordinates.  It contains no H-sector
coordinate and no UV two-Higgs `(H_u,H_d^dagger)` codomain.

This retires the plain projection idea for the current target.  The C1 path is
still useful, but only after a selected H-sector dynamic extension emits the
missing codomain map.  Otherwise the clean route is to export Huv rows directly.

Next label:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1N-HSECTOR-DYNAMIC-EXTENSION-OR-HONEST-HUV-ROWS`
"""

    for path, payload in [
        (C1_TARGET_AUDIT, c1_target_audit),
        (PROJECTION_DECISION, projection_decision),
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
