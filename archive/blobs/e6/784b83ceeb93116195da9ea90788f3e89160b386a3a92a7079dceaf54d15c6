"""Build CONST-EM-01 alpha1 normalization frontier.

Search and classify the strongest corpus/repo candidates for C_Y after the
source-side alpha1 driver and electroweak convention map.  The key guardrail is
that the closed U1=2/3 result is an internal inverse-kernel/index statement,
not automatically a physical alpha_Y coupling multiplier.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_normalization_frontier"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORTS = BASE / "cy_candidate_imports.packet.json"
SUPSET = BASE / "superset_path_decision.packet.json"
NO_GO = BASE / "physical_cy_nogo.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_NormalizationFrontier_v1.md"

STATUS = "MTT_CONST_EM_01_ALPHA1_NORMALIZATION_FRONTIER_BUILT_INTERNAL_INDEX_SUPPORT_PHYSICAL_CY_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def maybe(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return load(path)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def status_of(path: Path) -> str | None:
    data = maybe(path)
    if data is None:
        return None
    return data.get("status")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    qa_k_gauge = QA_SU3 / "candidate_data" / "selected_k_gauge_anchor_or_full_electroweak_matching.candidate.json"
    qa_same_scheme = QA_SU3 / "candidate_data" / "u1_su2_same_scheme_payloads_or_k_gauge_anchor.candidate.json"
    qa_gauge_rg = QA_SU3 / "candidate_data" / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme.candidate.json"
    qa_two_key = QA_SU3 / "candidate_data" / "selected_electroweak_two_key_frontier_interface.candidate.json"
    qa_u1_projector = QA_SU3 / "candidate_data" / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json"
    qa_u1_factorized = QA_SU3 / "candidate_data" / "selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate.candidate.json"
    nonsm_exhaustion = NONSM / "certificates" / "electroweak_no_knob_source_exhaustion_certificate.json"
    nonsm_kernel = NONSM / "certificates" / "selected_electroweak_kernel_interface_certificate.json"

    k = load(qa_k_gauge)
    same = load(qa_same_scheme)
    rg = load(qa_gauge_rg)
    two = load(qa_two_key)
    u1_projector = maybe(qa_u1_projector)
    u1_factorized = maybe(qa_u1_factorized)

    internal_vector = k["decision"]["selected_internal_kernel_vector"]
    u1_index = internal_vector["U1"]
    su2_index = internal_vector["SU2"]
    qa_index = internal_vector["Qa_or_SU3"]

    imports = {
        "schema": "MTTConstEM01CYCandidateImports.v1",
        "status": "CY_CANDIDATES_IMPORTED_AND_CLASSIFIED",
        "active_label": "CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY",
        "imports": [
            {
                "id": "QA-K-GAUGE-INTERNAL-ANCHOR",
                "path": rel(qa_k_gauge),
                "present": qa_k_gauge.exists(),
                "status": k["status"],
                "verdict": "INTERNAL_INVERSE_KERNEL_NORMALIZATION_SUPPORT_NOT_PHYSICAL_CY",
                "usable_now": "K_gauge,int=1 and internal vector (U1,SU2,Qa)=(2/3,1,log(2008))",
                "blocked_promotion": "physical K_gauge/action anchor, thresholds, matching scale, and scheme remain open",
            },
            {
                "id": "QA-U1-SU2-SAME-SCHEME-CONTRACT",
                "path": rel(qa_same_scheme),
                "present": qa_same_scheme.exists(),
                "status": same["status"],
                "verdict": "ACCEPTANCE_CONTRACT_AND_OLD_NO_GO",
                "usable_now": "names exact same-scheme fields for U1, SU2, hypercharge policy, K_gauge, mu_match, and RGE scheme",
                "blocked_promotion": "this older artifact keeps U1/SU2/K open and is superseded by later internal-index progress",
            },
            {
                "id": "QA-GAUGEKINETIC-RG-SCHEME",
                "path": rel(qa_gauge_rg),
                "present": qa_gauge_rg.exists(),
                "status": rg["status"],
                "verdict": "ROUTE_DISCRIMINATOR_AND_INTERNAL_WEAK_SPLIT_SUPPORT",
                "usable_now": "hypercharge source formula, internal lambda_12, and strict no-knob route selection",
                "blocked_promotion": "gaugekinetic normalization, RG scheme, matching scale, and measured closure remain open",
            },
            {
                "id": "QA-TWO-KEY-FRONTIER",
                "path": rel(qa_two_key),
                "present": qa_two_key.exists(),
                "status": two["status"],
                "verdict": "CURRENT_FRONTIER_KEYS",
                "usable_now": "separates dimensionless U1/Y determinant key from physical action-anchor key",
                "blocked_promotion": "both keys plus typed convention/RG remain required before measured alpha",
            },
            {
                "id": "QA-U1-PERP-PROJECTOR",
                "path": rel(qa_u1_projector),
                "present": qa_u1_projector.exists(),
                "status": status_of(qa_u1_projector),
                "verdict": "INTERNAL_U1_INDEX_SUPPORT",
                "usable_now": "selected rank-3 quotient projector support for Tr(P_perp)/Tr(I)=2/3",
                "blocked_promotion": "P_perp is an index/projector, not by itself a coupling or determinant spectrum",
            },
            {
                "id": "QA-U1Y-FACTORIZED-OPERATOR-GATE",
                "path": rel(qa_u1_factorized),
                "present": qa_u1_factorized.exists(),
                "status": status_of(qa_u1_factorized),
                "verdict": "NEXT_DIMENSIONLESS_DETERMINANT_GATE",
                "usable_now": "points to factorized U1/Y threshold operator source emission as the next dimensionless row",
                "blocked_promotion": "source must emit operator, bind to P_perp, and supply hypercharge/index weights",
            },
            {
                "id": "NONSM-ELECTROWEAK-SOURCE-EXHAUSTION",
                "path": rel(nonsm_exhaustion),
                "present": nonsm_exhaustion.exists(),
                "status": status_of(nonsm_exhaustion),
                "verdict": "NEGATIVE_CLOSURE_GUARDRAIL",
                "usable_now": "proves absolute electroweak observables are underdetermined without selected normalization/threshold kernel",
                "blocked_promotion": "forbids turning overlap ratios or measured values into no-knob constants",
            },
            {
                "id": "NONSM-ELECTROWEAK-KERNEL-INTERFACE",
                "path": rel(nonsm_kernel),
                "present": nonsm_kernel.exists(),
                "status": status_of(nonsm_kernel),
                "verdict": "KERNEL_INTERFACE_SUPPORT",
                "usable_now": "supports electroweak kernel/interface language used by QA route discriminator",
                "blocked_promotion": "interface is not itself a selected physical numeric kernel",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    superset = {
        "schema": "MTTConstEM01SupersetCYPathDecision.v1",
        "status": "SUPERSET_PATH_REDUCED_TO_TYPED_INTERNAL_INDEX_AND_PHYSICAL_ANCHOR_SPLIT",
        "active_label": "CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY",
        "combined_paths": {
            "source_side_alpha1": "N_alpha1(h_ext)=1 from QA replay in this repo",
            "internal_index_kernel": {
                "K_gauge_int": "1",
                "I_U1": u1_index,
                "I_SU2": su2_index,
                "I_Qa_or_SU3": qa_index,
            },
            "quotient_projector": "P_perp rank ratio 2/3 supports the U1 internal index",
            "gaugekinetic_route": rg["decision"]["strict_primary_route_selected"],
            "frontier_split": "dimensionless U1/Y determinant key and physical action-anchor key are independent",
        },
        "locked_target": "C_Y search only; no measured alpha and no physical electroweak closure",
        "promotable_now": {
            "source_side_alpha1_unit": True,
            "internal_inverse_kernel_U1_index": True,
            "internal_K_gauge_action_unit": True,
            "physical_C_Y_coupling_multiplier": False,
            "alpha_Y_numeric": False,
            "alpha_em_numeric": False,
        },
        "why_physical_CY_not_closed": [
            "The internal U1=2/3 result is an inverse-kernel/index statement, not a declared alpha_Y coupling multiplier.",
            "The typed convention has not selected whether C_Y uses the index, its inverse, a 3/5 or 5/3 hypercharge convention, or a determinant finite part.",
            "The U1/Y local determinant row and physical action anchor are independent keys in the latest QA frontier.",
            "Running, threshold, matching-scale, and scheme data remain open for comparison to alpha(0) or alpha(M_Z).",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    no_go = {
        "schema": "MTTConstEM01PhysicalCYNoGo.v1",
        "status": "PHYSICAL_CY_CURRENT_SOURCE_NOGO_PROVED",
        "active_label": "CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY",
        "theorem": {
            "name": "CurrentSourcePhysicalCYNoGo",
            "proved": True,
            "statement": (
                "Given the current repo/corpus state, a physical source-to-hypercharge multiplier C_Y cannot be promoted. "
                "The available source data close a source-side alpha1 unit and an internal inverse-kernel U1 index, but do not "
                "select the typed map from that index to alpha_Y, do not emit the U1/Y local determinant row in the same scheme, "
                "and do not select the physical action anchor or RG/threshold scheme."
            ),
        },
        "minimal_repair_objects": {
            "dimensionless_first": "Selected_Electroweak_U1Y_FactorizedThresholdOperator_SourceEmission_v1",
            "physical_anchor": "Selected_Electroweak_DimensionalActionAnchor_SourcePacket_v1",
            "typed_convention": "CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION",
            "shared_SU2_packet": "CONST-EM-01 / ALPHA1-SU2-MIXING / A4-SHARED-GAUGE-PACKET",
        },
        "forbidden_shortcuts": [
            "Set C_Y=2/3 directly as alpha_Y multiplier.",
            "Set C_Y=3/5 or 5/3 because GUT normalization is familiar.",
            "Use measured alpha(0), alpha(M_Z), sin^2(theta_W), or g2 to solve for C_Y.",
            "Identify internal K_gauge,int=1 with physical K_phys.",
            "Use P_perp as a full U1/Y determinant spectrum.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterConstEM01NormalizationFrontier.v1",
        "status": "NEXT_WORKORDER_TYPED_CY_CONVENTION_OR_U1Y_OPERATOR_ROW",
        "primary": {
            "label": "CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION",
            "task": "Build the typed convention theorem deciding how the internal U1 index 2/3, GUT hypercharge factors, and determinant finite parts map into the C_Y slot without using measured alpha.",
        },
        "secondary": {
            "label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A4-FACTORIZED-OPERATOR",
            "task": "Import or construct the selected U1/Y factorized threshold operator source emission on V/<s>, with P_perp binding and hypercharge/index weights.",
        },
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1NormalizationFrontier",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY",
        "output_packets": {
            "cy_candidate_imports": rel(IMPORTS),
            "superset_path_decision": rel(SUPSET),
            "physical_cy_nogo": rel(NO_GO),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "corpus_repo_CY_search_executed": True,
            "internal_K_gauge_int_unit_imported": True,
            "internal_U1_index_two_thirds_imported": True,
            "superset_paths_classified": True,
            "physical_CY_no_go_proved_for_current_sources": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "physical_C_Y_source_to_hypercharge_multiplier": True,
            "typed_index_to_coupling_convention": True,
            "U1Y_local_determinant_row": True,
            "physical_action_anchor": True,
            "SU2_same_scheme_packet": True,
            "RG_threshold_scheme_and_matching_scale": True,
            "alpha_zero_or_MZ_value": True,
        },
        "current_best_candidate": {
            "name": "internal inverse-kernel U1 index",
            "value": "2/3",
            "scope": "selected internal action/index units only",
            "not_a_physical_CY": True,
        },
        "theorem": no_go["theorem"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_NormalizationFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "internal_U1_index_support_value": "2/3",
        "internal_K_gauge_int": "1",
        "physical_CY_claimed": False,
        "selected_universal_parameters_now": 0,
        "next_primary": "CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Normalization Frontier v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY`

## Result

The corpus/repo search found strong normalization support, but not yet a
physical `C_Y` value.

Promotable now:

- source-side `N_alpha1(h_ext)=1`,
- internal `K_gauge,int=1`,
- selected internal kernel vector `(U1, SU2, Qa/SU3)=(2/3, 1, log(2008))`.

Not promotable yet:

- physical `C_Y` in `alpha_Y = C_Y * N_alpha1(h_ext)`,
- `alpha_Y`,
- `alpha_em`,
- `alpha(0)` or `alpha(M_Z)`.

## Superset Strategy

We combine four source paths but lock the target:

- QA alpha1 driver replay gives the source-side unit.
- QA quotient-projector/U1-SU2 path gives the internal U1 index `2/3`.
- QA gauge-kinetic route gives internal `K_gauge,int=1`.
- non-SM exhaustion theorem forbids physical electroweak closure without a
  selected normalization/threshold kernel.

This gives a clean current-source no-go for physical `C_Y`: the best current
candidate is internal and inverse-kernel/index scoped, while the physical
coupling multiplier still needs a typed convention and source row.

## Forbidden Shortcuts

- Do not set `C_Y=2/3` as a physical coupling multiplier.
- Do not set `C_Y=3/5` or `5/3` merely by convention.
- Do not solve `C_Y` from measured `alpha`, `sin^2(theta_W)`, or `g2`.
- Do not identify internal `K_gauge,int=1` with physical `K_phys`.

## Next

Next label: `CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION`

Decide how the internal U1 index, GUT hypercharge factors, and determinant
finite parts legally map into the `C_Y` slot.
"""

    for path, payload in [
        (IMPORTS, imports),
        (SUPSET, superset),
        (NO_GO, no_go),
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
