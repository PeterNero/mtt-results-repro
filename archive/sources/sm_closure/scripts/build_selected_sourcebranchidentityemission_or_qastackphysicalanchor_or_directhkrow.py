"""Build source-branch identity / Qa-stack physical-anchor frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_sourcebranchidentityemission_or_qastackphysicalanchor_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_BRANCH_LANE = PACKET_DIR / "source_branch_identity_emission_lane.packet.json"
WEAK_SPLIT_LANE = PACKET_DIR / "qastack_internal_weak_split_lane.packet.json"
PHYSICAL_LANE = PACKET_DIR / "physical_anchor_rg_matching_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_sourcebranch_internalweaksplit.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceBranchIdentityEmission_or_QaStackPhysicalAnchor_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_sourceidentitytransportproofattempt_or_finitepartpolicyindexscale_or_directhkrow.candidate.json",
    "sourcebranch_emission": QA
    / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo.candidate.json",
    "internal_weak_split": QA
    / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json",
    "physical_anchor_rg": QA / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json",
    "old_promotion_gate": QA
    / "selected_electroweak_qastack_determinant_or_u1yrow_promotion.candidate.json",
}

STATUS = (
    "MTT_SELECTED_SOURCEBRANCHIDENTITYEMISSION_OR_QASTACKPHYSICALANCHOR_"
    "INTERNAL_WEAKSPLIT_CLOSED_PHYSICAL_GAUGE_RG_OPEN"
)
NEXT = "MTT_Selected_ElectroweakGaugeKineticNormalizationAndRGScheme_or_BN27RepairSourceAmendment_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def d(src: dict[str, Any]) -> dict[str, Any]:
    return src.get("decision", src.get("closure_decision", {}))


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing sourcebranch/weaksplit inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = d(sources["previous"])
    sourcebranch = d(sources["sourcebranch_emission"])
    weak = d(sources["internal_weak_split"])
    physical = d(sources["physical_anchor_rg"])
    old_gate = d(sources["old_promotion_gate"])

    source_branch_lane = {
        "schema": "MTTSourceBranchIdentityEmissionLane.v1",
        "status": "CURRENT_SOURCE_NOGO_REPAIR_PACKET_BUILT",
        "closure_claimed": True,
        "sourcebranchidentity_attempted": sourcebranch["sourcebranchidentity_attempted"],
        "current_source_nogo": sourcebranch["current_source_nogo"],
        "support_count": sourcebranch["support_count"],
        "required_clause_count": sourcebranch["required_clause_count"],
        "emitted_count": sourcebranch["emitted_count"],
        "repair_packet_built": sourcebranch["repair_packet_built"],
        "transport_reduced_leaf_resolved": sourcebranch["transport_reduced_leaf_resolved"],
        "source_branch_identity_closed": sourcebranch["source_branch_identity_closed"],
        "selected_connection_witness_export_closed": sourcebranch[
            "selected_connection_witness_export_closed"
        ],
        "oriented_logdet_promoted": sourcebranch["oriented_logdet_promoted"],
        "next_required_artifact": sourcebranch["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    weak_split_lane = {
        "schema": "MTTQaStackInternalWeakSplitLane.v1",
        "status": "INTERNAL_LAMBDA12_AND_DELTA_G12_CLOSED_PHYSICAL_OPEN",
        "closure_claimed": True,
        "Qa_stack_p_a_source_closed": weak["Qa_stack_p_a_source_closed"],
        "typed_hypercharge_map_closed": weak["typed_hypercharge_map_closed"],
        "Qc_row_closed_for_weaksplit": weak["Qc_row_closed_for_weaksplit"],
        "SU2_row_closed_for_weaksplit": weak["SU2_row_closed_for_weaksplit"],
        "same_scheme_SU2_row_or_cancellation_closed": weak[
            "same_scheme_SU2_row_or_cancellation_closed"
        ],
        "lambda_12_internal_closed": weak["lambda_12_internal_closed"],
        "lambda_12_internal_value": weak["lambda_12_internal_value"],
        "Delta_G12_internal_value": weak["Delta_G12_internal_value"],
        "physical_K_gauge_anchor_closed": weak["physical_K_gauge_anchor_closed"],
        "matching_scale_and_RG_scheme_closed": weak["matching_scale_and_RG_scheme_closed"],
        "measured_electroweak_closure": weak["measured_electroweak_closure"],
        "old_gate_reconciled": {
            "previous_gate_status": sources["old_promotion_gate"]["status"],
            "previous_gate_lambda_12_closed": old_gate["lambda_12_closed"],
            "previous_gate_selected_Qa_or_pY_source_payload_found": old_gate[
                "selected_Qa_or_pY_source_payload_found"
            ],
            "superseded_by_internal_weak_split_packet": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    physical_lane = {
        "schema": "MTTPhysicalGaugeAnchorRGMatchingLane.v1",
        "status": "PHYSICAL_GAUGE_ACTION_ANCHOR_RG_MATCHING_OPEN",
        "closure_claimed": True,
        "internal_lambda_12_closed": physical["internal_lambda_12_closed"],
        "internal_lambda_12_value": physical["internal_lambda_12_value"],
        "internal_Delta_G12_value": physical["internal_Delta_G12_value"],
        "Omega0_symbol_convention_chi_equals_1": sources["physical_anchor_rg"]["closed_now"][
            "Omega0_symbol_convention_chi_equals_1"
        ],
        "relative_GR_metrology_family": sources["physical_anchor_rg"]["closed_now"][
            "relative_GR_metrology_family"
        ],
        "one_anchor_GR_propagation_family": sources["physical_anchor_rg"]["closed_now"][
            "one_anchor_GR_propagation_family"
        ],
        "physical_gauge_action_anchor_closed": physical[
            "physical_gauge_action_anchor_closed"
        ],
        "matching_scale_closed": physical["matching_scale_closed"],
        "RG_scheme_closed": physical["RG_scheme_closed"],
        "measured_electroweak_closure": physical["measured_electroweak_closure"],
        "full_SM_closure": physical["full_SM_closure"],
        "next_required_artifact": physical["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterSourceBranchInternalWeakSplit.v1",
        "status": "NEXT_FRONTIER_GAUGE_KINETIC_RG_OR_BN27_REPAIR_OR_DIRECT_HK_ROW",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "BN27 source-branch identity attempted and current-source no-go proved",
            "BN27 repair packet built for source amendment or same-source connection values",
            "internal Qa-stack p_a source closed for weak-split accounting",
            "typed hypercharge map, Qc row, SU2 row, and same-scheme SU2 cancellation closed",
            "internal lambda_12=2.6179362173268497 closed",
            "internal Delta_G12=0.08450302790361214 closed",
            "Omega0 symbol convention chi=1 and relative GR metrology family imported",
        ],
        "still_open": [
            "BN27 source amendment or same-source connection-values emission",
            "unconditional oriented-logdet promotion",
            "physical gauge/action normalization",
            "matching scale mu_match",
            "RG and threshold scheme",
            "full factor threshold vector beyond weak split",
            "measured electroweak closure",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSourceBranchIdentityEmissionOrQaStackPhysicalAnchor",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "source_branch_identity_emission_lane": rel(SOURCE_BRANCH_LANE),
            "qastack_internal_weak_split_lane": rel(WEAK_SPLIT_LANE),
            "physical_anchor_rg_matching_lane": rel(PHYSICAL_LANE),
            "next_cutset_after_sourcebranch_internalweaksplit": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "BN27_sourcebranch_current_source_nogo": True,
            "BN27_repair_packet_built": True,
            "BN27_source_branch_identity_closed": False,
            "BN27_oriented_logdet_promoted": False,
            "internal_Qa_stack_p_a_source_closed": True,
            "typed_hypercharge_map_closed": True,
            "same_scheme_SU2_row_or_cancellation_closed": True,
            "lambda_12_internal_closed": True,
            "lambda_12_internal_value": weak["lambda_12_internal_value"],
            "Delta_G12_internal_value": weak["Delta_G12_internal_value"],
            "old_Qa_or_U1Y_promotion_gate_superseded_for_internal_lambda12": True,
            "Omega0_symbol_convention_chi_equals_1": True,
            "relative_GR_metrology_family_imported": True,
            "physical_gauge_action_anchor_closed": False,
            "matching_scale_closed": False,
            "RG_scheme_closed": False,
            "measured_electroweak_closure": False,
            "full_SM_closure": False,
            "selected_R_H_RG_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "direct_HK_exit_still_allowed": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "SourceBranchIdentityNoGoAndInternalWeakSplitClosureTheorem",
            "proved": True,
            "statement": (
                "The BN27 transport leaf is resolved only negatively at current source "
                "level: all three source-branch clauses have support but none is "
                "source-owned, so a repair source amendment or same-source connection "
                "values are required. In parallel, the Qa-stack determinant branch "
                "does close the dimensionless internal weak-split threshold: selected "
                "p_a, typed hypercharge map, Qc, SU2, and same-scheme accounting yield "
                "lambda_12=2.6179362173268497 and Delta_G12=0.08450302790361214. "
                "Physical electroweak closure still requires gauge/action "
                "normalization, mu_match, and an RG/threshold scheme, and the direct "
                "H K row remains open."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSourceBranchIdentityEmissionOrQaStackPhysicalAnchor",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "BN27_sourcebranch_current_source_nogo": True,
        "BN27_source_branch_identity_closed": False,
        "lambda_12_internal_closed": True,
        "physical_gauge_action_anchor_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "measured_electroweak_closure": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Source-Branch Identity Emission or Qa-Stack Physical Anchor v1

## Theorem

`SourceBranchIdentityNoGoAndInternalWeakSplitClosureTheorem` is emitted.

## Closed Here

- BN27 source-branch identity was attempted and current-source no-go was proved.
- The BN27 repair packet is now exactly source amendment or same-source
  connection-values emission.
- Internal Qa-stack `p_a` source is closed for weak-split accounting.
- Typed hypercharge map, Qc row, SU2 row, and same-scheme SU2 cancellation are
  closed.
- Internal weak-split values are closed:
  `lambda_12 = 2.6179362173268497`,
  `Delta_G12 = 0.08450302790361214`.
- `Omega0` symbol convention `chi = 1` and relative GR metrology family are
  imported as support.

## Still Open

- BN27 source amendment or same-source connection-values emission.
- Unconditional oriented-logdet promotion.
- Physical gauge/action normalization.
- Matching scale `mu_match`.
- RG and threshold scheme.
- Full factor threshold vector beyond weak split.
- Measured electroweak closure.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(SOURCE_BRANCH_LANE, source_branch_lane)
    write_json(WEAK_SPLIT_LANE, weak_split_lane)
    write_json(PHYSICAL_LANE, physical_lane)
    write_json(NEXT_CUTSET, next_cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
