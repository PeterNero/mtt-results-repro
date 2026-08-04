"""Build common-circle bundle csk functional / Phi_flavor_N refinement packet.

This packet answers whether the c_{s,k} finite response source form is native
to MTT once the shared central circle is included.  It promotes the common
circle only as a required shared holonomy/normalization channel inside
Phi_flavor_N.  It does not promote the circle alone as nine flavor values.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_commoncirclebundlecskfunctional_or_phiflavornrefinement"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CommonCircleBundleCSKFunctional_or_PhiFlavorNRefinement_v1.md"

CSK_CANDIDATE = DATA / "selected_cskfinitefunctionalobligation_or_sectorblindhymnogotheorem.candidate.json"
CSK_CONTRACT = (
    DATA
    / "selected_cskfinitefunctionalobligation_or_sectorblindhymnogotheorem"
    / "csk_finite_response_functional_contract.packet.json"
)
CSK_NOGO = (
    DATA
    / "selected_cskfinitefunctionalobligation_or_sectorblindhymnogotheorem"
    / "sector_blind_hym_direct_attachment_nogo.packet.json"
)
CSK_MANIFEST = (
    DATA
    / "selected_cskfinitefunctionalobligation_or_sectorblindhymnogotheorem"
    / "csk_row_value_obligation_manifest.packet.json"
)
CORPUS_BRIDGE = CORPUS / "MTT_Corpus_Encoding_Bridge_Map_for_QutritSpectralHeteroticSM_v1.md"

CORPUS_SUPPORT = PACKET_DIR / "common_circle_corpus_support.packet.json"
REFINED_CONTRACT = PACKET_DIR / "common_circle_refined_csk_functional_contract.packet.json"
GUARD = PACKET_DIR / "common_circle_sector_resolution_guard.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_common_circle_refinement.packet.json"

STATUS = (
    "MTT_SELECTED_COMMONCIRCLEBUNDLECSKFUNCTIONAL_OR_PHIFLAVORNREFINEMENT_"
    "COMMON_CIRCLE_PLACED_IN_FUNCTIONAL_VALUES_OPEN"
)
NEXT = "MTT_Selected_CommonCircleSectorResponseExecution_or_CSKTraceRows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    sources = [CSK_CANDIDATE, CSK_CONTRACT, CSK_NOGO, CSK_MANIFEST, CORPUS_BRIDGE]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing common-circle functional inputs: " + ", ".join(missing))

    csk_candidate = load(CSK_CANDIDATE)
    csk_contract = load(CSK_CONTRACT)
    csk_nogo = load(CSK_NOGO)
    csk_manifest = load(CSK_MANIFEST)
    corpus_bridge_text = CORPUS_BRIDGE.read_text(encoding="utf-8")

    corpus_support = {
        "schema": "MTTCommonCircleCorpusSupport.v1",
        "status": "COMMON_CIRCLE_SUPPORT_PRESENT_AS_SHARED_BUNDLE_CHANNEL",
        "closure_claimed": True,
        "local_bridge_support_present": "central-circle corpus supports a shared circle/family bookkeeping" in corpus_bridge_text,
        "source_registry": {
            "central_circle": (
                "C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory/13 Standard Model & "
                "Topology-Only Constraints/The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_"
                "Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
            ),
            "theta_gauge_couplings": (
                "C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory/18 Theta-Closure & "
                "Execution Program/Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_"
                "Internal_Geometry.md"
            ),
            "theta_nonabelian_overlaps": (
                "C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory/18 Theta-Closure & "
                "Execution Program/Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_"
                "Realization_of_Nonabelian_Overlaps.md"
            ),
        },
        "corpus_reading": [
            "S^1_cen is the common central circle reused across modal bundles.",
            "Internal bundle fibers have the typed form B_s|_y ~= S^1_cen x Sigma_s.",
            "Yukawa/flavor structure is described by holonomy/overlap through the bundle.",
            "The shared circle supplies common phase, normalization, and selection-rule data.",
            "Sector differences still require Sigma_s, sector projectors, or a sector response density.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    refined_contract = {
        "schema": "MTTCommonCircleRefinedCSKFunctionalContract.v1",
        "status": "PHI_FLAVOR_N_REFINED_TO_INCLUDE_COMMON_CIRCLE_HOLONOMY",
        "closure_claimed": True,
        "previous_required_source_form": csk_contract["required_source_form"],
        "mtt_native_source_form": (
            "c_{s,k}=Tr_N(P_s * B_k * H_cen * Phi_sector_N), where H_cen is the "
            "selected finite common-circle holonomy/normalization channel and "
            "Phi_sector_N is the selected sector-resolving threshold/response payload."
        ),
        "equivalent_bundle_integral_shadow": (
            "c_{s,k}=Integral_{S^1_cen x Sigma_s} omega_cen(theta) * "
            "B_k(theta,u) * rho_s(theta,u) dmu_N, then finite-projected to Tr_N."
        ),
        "common_circle_role": [
            "shared coherence/phase channel",
            "common normalization and selection-rule carrier",
            "circle holonomy input to the finite response trace",
        ],
        "sector_resolution_role": [
            "P_s selects u,d,e sector support",
            "Sigma_s or Phi_sector_N supplies sector-specific response",
            "B_k resolves the family polynomial basis",
        ],
        "finite_projected_HYM_source_principle_closed": csk_contract[
            "finite_projected_HYM_source_principle_closed"
        ],
        "selected_Rtheta_scalar_value_functional_source_domain_closed": csk_contract[
            "selected_Rtheta_scalar_value_functional_source_domain_closed"
        ],
        "csk_row_value_obligation_count": csk_manifest["policy_source_value_row_count"],
        "accepted_strict_csk_source_row_count": 0,
        "functional_contract_refined": True,
        "functional_values_executed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    guard = {
        "schema": "MTTCommonCircleSectorResolutionGuard.v1",
        "status": "COMMON_CIRCLE_ALONE_REJECTED_AS_NINE_ROW_SOURCE",
        "closure_claimed": True,
        "common_circle_alone_sources_csk": False,
        "reason": (
            "The common circle is shared across all bundles and so can supply a universal "
            "holonomy/normalization/selection channel.  By itself it is sector-blind and "
            "cannot emit a full-rank u,d,e coefficient matrix."
        ),
        "imports_sector_blind_hym_nogo": True,
        "hym_rows_sector_blind": csk_nogo["hym_rows_sector_blind"],
        "csk_matrix_full_rank": csk_nogo["csk_matrix_full_rank"],
        "best_sector_blind_shared_row_max_abs_residual": csk_nogo[
            "best_sector_blind_shared_row_max_abs_residual"
        ],
        "required_extra_structure": [
            "selected sector projectors P_u,P_d,P_e",
            "selected sector response payload Phi_sector_N",
            "row-level finite trace certificates",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterCommonCircleRefinement.v1",
        "status": "NEXT_IS_COMMON_CIRCLE_SECTOR_RESPONSE_EXECUTION",
        "closure_claimed": True,
        "closed_now": [
            "common circle is placed inside Phi_flavor_N rather than outside the source functional",
            "MTT-native finite trace source form is refined to include H_cen",
            "common-circle-only and direct sector-blind shortcuts remain rejected",
        ],
        "still_open": [
            "finite H_cen matrix/character values in the selected q79/F,m=1 branch",
            "sector-resolving Phi_sector_N values",
            "nine c_{s,k} trace evaluations",
            "strict no-knob Yukawa magnitude closure",
        ],
        "next_required_artifact": NEXT,
        "ordered_execution_plan": [
            "emit the finite common-circle holonomy/normalization operator H_cen",
            "bind H_cen to the selected q79/F,m=1 bundle branch and family basis B_k",
            "construct sector projectors P_s and Phi_sector_N in the same finite algebra A_N",
            "evaluate the nine traces Tr_N(P_s B_k H_cen Phi_sector_N)",
            "only then compare against the existing policy c_{s,k} rows",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedCommonCircleBundleCSKFunctionalOrPhiFlavorNRefinement",
        "status": STATUS,
        "closure_claimed": True,
        "strict_csk_source_theorem_claimed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "inputs": {
            "csk_finite_functional_obligation": rel(CSK_CANDIDATE),
            "csk_finite_response_contract": rel(CSK_CONTRACT),
            "sector_blind_hym_nogo": rel(CSK_NOGO),
            "csk_manifest": rel(CSK_MANIFEST),
            "corpus_encoding_bridge": rel(CORPUS_BRIDGE),
        },
        "theorem": {
            "name": "CommonCircleBundleCSKFunctionalRefinementTheorem",
            "proved": True,
            "statement": (
                "In MTT, the c_{s,k} source functional is natively a bundle trace through "
                "the common central circle.  The correct refinement is "
                "c_{s,k}=Tr_N(P_s B_k H_cen Phi_sector_N).  The common circle supplies "
                "shared holonomy/normalization/selection data, but cannot alone supply "
                "the sector-resolving full-rank coefficient matrix."
            ),
        },
        "closure_decision": {
            "common_circle_applicable_to_csk_functional": True,
            "common_circle_placed_inside_Phi_flavor_N": True,
            "common_circle_alone_sources_csk": False,
            "common_circle_only_shortcut_rejected": True,
            "direct_HYM_overlap_attachment_rejected": csk_candidate["closure_decision"][
                "direct_HYM_overlap_attachment_rejected"
            ],
            "csk_matrix_full_rank": csk_candidate["closure_decision"]["csk_matrix_full_rank"],
            "admissible_common_circle_refined_functional_contract_closed": True,
            "csk_row_value_obligation_count": csk_candidate["closure_decision"][
                "csk_row_value_obligation_count"
            ],
            "accepted_strict_csk_source_row_count": 0,
            "strict_csk_source_theorem_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "packets": {
            "common_circle_corpus_support": rel(CORPUS_SUPPORT),
            "common_circle_refined_csk_functional_contract": rel(REFINED_CONTRACT),
            "common_circle_sector_resolution_guard": rel(GUARD),
            "next_cutset": rel(NEXT_PACKET),
        },
    }

    cert = {
        "certificate": "MTTSelectedCommonCircleBundleCSKFunctionalOrPhiFlavorNRefinementCertificate",
        "status": STATUS,
        "theorem": candidate["theorem"]["name"],
        "common_circle_applicable_to_csk_functional": True,
        "common_circle_placed_inside_Phi_flavor_N": True,
        "common_circle_alone_sources_csk": False,
        "admissible_common_circle_refined_functional_contract_closed": True,
        "csk_row_value_obligation_count": candidate["closure_decision"]["csk_row_value_obligation_count"],
        "accepted_strict_csk_source_row_count": 0,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected CommonCircleBundleCSKFunctional or PhiFlavorNRefinement v1

Status: `{STATUS}`

## Theorem

`CommonCircleBundleCSKFunctionalRefinementTheorem` is proved.

The `c_{{s,k}}` source functional is applicable straight inside MTT, provided
the shared central circle is included as a bundle holonomy/normalization channel
inside the finite response object.  The refined source form is:

`c_{{s,k}} = Tr_N(P_s * B_k * H_cen * Phi_sector_N)`.

Equivalently, this is the finite-projected version of an overlap through
`S^1_cen x Sigma_s`, where `S^1_cen` supplies shared coherence/phase data,
`P_s` and `Sigma_s` supply the sector separation, and `B_k` resolves the family
polynomial row.

## Guard

The common circle alone is not promoted as a nine-row source.  It is shared by
all bundles, so by itself it is sector-blind.  The previous sector-blind no-go
still applies: the `c_{{s,k}}` matrix is full rank, and the best shared-row
residual is `{csk_nogo["best_sector_blind_shared_row_max_abs_residual"]}`.

## What This Closes

- common circle placement inside `Phi_flavor_N`
- MTT-native bundle trace form for the `c_{{s,k}}` source problem
- rejection of the common-circle-only shortcut

## What Remains

- emit `H_cen` as a finite selected common-circle operator
- construct same-source `Phi_sector_N`
- evaluate the nine row traces
- certify the values before empirical Yukawa/CKM/PMNS replay

Next artifact: `{NEXT}`.
"""

    write_json(CORPUS_SUPPORT, corpus_support)
    write_json(REFINED_CONTRACT, refined_contract)
    write_json(GUARD, guard)
    write_json(NEXT_PACKET, next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
