"""Build R_theta source-owner/row-coefficient packet attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OWNER_MATRIX = PACKET_DIR / "rtheta_source_owner_candidate_matrix.packet.json"
COEFFICIENT_MANIFEST = PACKET_DIR / "rtheta_row_coefficient_slot_manifest.packet.json"
CONSTRUCTION_ATTEMPT = PACKET_DIR / "rtheta_source_owner_row_coefficient_construction_attempt.packet.json"
DECISION = PACKET_DIR / "rtheta_blocker_contraction_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rtheta_owner_coefficient_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaSourceOwnerRowCoefficientPacket_or_BlockerContraction_v1.md"

PREVIOUS = DATA / "selected_rtheta_supportreevaluation_or_sourcepromotionattempt.candidate.json"
RTHETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
SUPPORT_DECISION = (
    DATA
    / "selected_rtheta_supportreevaluation_or_sourcepromotionattempt"
    / "rtheta_support_reevaluation_decision.packet.json"
)
ACTUAL_SM_PACKET = DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"
QASU3_PARITY = DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"
DYNAMIC_C1_OWNER = DATA / "selected_dynamicc1_sourceowner_theorem_or_independentconnectiontables.candidate.json"
DYNAMIC_MATTER_PACKET = (
    DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
)
SMSLOT_SIX_ARROW = DATA / "selected_smslotfunctor_sixarrow_source_emission.candidate.json"
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
EXTERNAL_MANIFEST = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "external_likelihood_import_manifest.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETA_SOURCEOWNER_ROWCOEFFICIENTPACKET_OR_BLOCKERCONTRACTION_"
    "BUILT_PRECURSORS_ACCEPTED_PACKET_OPEN"
)
NEXT = "MTT_Selected_RThetaCoefficientFormulaDerivation_or_SelectedOwnerBridge_v1"


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
        raise FileNotFoundError("missing R_theta source owner/coefficient sources: " + ", ".join(missing))


def candidate_row(
    candidate_id: str,
    source: Path,
    scope: str,
    precursor: bool,
    accepted: bool,
    closes: list[str],
    missing: list[str],
) -> dict[str, Any]:
    return {
        "candidate_id": candidate_id,
        "source": rel(source),
        "scope": scope,
        "accepted_as_rtheta_source_owner": accepted,
        "accepted_as_rtheta_precursor": precursor,
        "closes_or_supports": closes,
        "missing_for_rtheta_source_owner": missing if not accepted else [],
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        RTHETA_CONTRACT,
        SUPPORT_DECISION,
        ACTUAL_SM_PACKET,
        QASU3_PARITY,
        DYNAMIC_C1_OWNER,
        DYNAMIC_MATTER_PACKET,
        SMSLOT_SIX_ARROW,
        VALUE_PACKET,
        EXTERNAL_MANIFEST,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    contract = load(RTHETA_CONTRACT)
    support_decision = load(SUPPORT_DECISION)
    actual_sm = load(ACTUAL_SM_PACKET)
    qasu3 = load(QASU3_PARITY)
    dynamic_c1 = load(DYNAMIC_C1_OWNER)
    dynamic_matter = load(DYNAMIC_MATTER_PACKET)
    smslot = load(SMSLOT_SIX_ARROW)
    value_packet = load(VALUE_PACKET)
    external = load(EXTERNAL_MANIFEST)

    owner_candidates = [
        candidate_row(
            "actual_selected_sm_packet_anomaly_audit",
            ACTUAL_SM_PACKET,
            "selected SM representation and anomaly packet",
            precursor=actual_sm["gate_results"]["topology_only_sm_structure_supported"],
            accepted=actual_sm["gate_results"]["actual_selected_representation_packet_supplied"]
            and actual_sm["gate_results"]["qa_su3_operator_packet_supplied"],
            closes=[
                "topology-only SM structure support",
                "anomaly structure support",
            ],
            missing=[
                "actual selected representation packet",
                "actual selected anomaly table on that packet",
                "Qa/SU3 operator packet",
                "typed monad or section-ring values",
            ],
        ),
        candidate_row(
            "qasu3_parity_interface",
            QASU3_PARITY,
            "SM-parity source-interface packet",
            precursor=qasu3["closure_decision"]["SM_parity_closed"],
            accepted=qasu3["actual_selected_operator_packet_claimed"],
            closes=list(qasu3["what_closes_now"].keys()),
            missing=list(qasu3["what_remains_open"].keys()),
        ),
        candidate_row(
            "dynamic_c1_source_owner_template",
            DYNAMIC_C1_OWNER,
            "dynamic C1 source-owner strict template",
            precursor=dynamic_c1["closure_decision"]["strict_source_owner_template_built"],
            accepted=dynamic_c1["closure_decision"]["dynamic_C1_source_owner_theorem_proved_as_hypothesis"],
            closes=list(dynamic_c1["what_closes_now"].keys()),
            missing=list(dynamic_c1["what_remains_open"].keys()),
        ),
        candidate_row(
            "same_source_dynamic_matter_overlap_packet",
            DYNAMIC_MATTER_PACKET,
            "selected first-response dynamic matter/overlap packet",
            precursor=dynamic_matter["promotion_decision"][
                "selected_dynamic_QaSU3_operator_packet_first_response_layer_closed"
            ],
            accepted=False,
            closes=list(dynamic_matter["what_closes_now"].keys()),
            missing=[
                "does not emit VSD02 threshold row coefficients",
                "does not emit mass-scheme conversion coefficients",
                "Yukawa magnitudes and running mass ratios remain open",
                "not accepted as full SM no-knob closure",
            ],
        ),
        candidate_row(
            "terminal_smslot_functor_A1_A3",
            SMSLOT_SIX_ARROW,
            "terminal section-ring matter-slot arrows",
            precursor=smslot["selected_SMSlotFunctor_first_three_arrows_claimed"],
            accepted=smslot["selected_SMSlotFunctor_all_six_arrows_claimed"],
            closes=list(smslot["what_closes_now"].keys()),
            missing=list(smslot["what_remains_open"].keys()),
        ),
    ]

    owner_matrix = {
        "schema": "MTTRThetaSourceOwnerCandidateMatrix.v1",
        "status": "SOURCE_OWNER_CANDIDATES_AUDITED_PRECURSORS_ONLY",
        "candidate_rows": owner_candidates,
        "candidate_count": len(owner_candidates),
        "accepted_precursor_count": sum(1 for row in owner_candidates if row["accepted_as_rtheta_precursor"]),
        "accepted_rtheta_source_owner_count": sum(
            1 for row in owner_candidates if row["accepted_as_rtheta_source_owner"]
        ),
        "best_current_precursor": "same_source_dynamic_matter_overlap_packet",
        "why_best_precursor": (
            "It is the strongest same-source dynamic/operator layer currently closed, but it still lacks "
            "threshold and mass-scheme coefficient emission."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(OWNER_MATRIX, owner_matrix)

    threshold_slots = ["top", "bottom", "charm", "tau", "W_Z_H"]
    mass_scheme_slots = [
        "top_direct_pole_running",
        "bottom_MSbar_native_scale_transport",
        "charm_MSbar_native_scale_transport",
        "tau_pole_rest_to_running_lepton",
        "Higgs_pole_running_lambda",
    ]
    coefficient_slots = [
        {
            "slot_id": f"threshold::{slot}",
            "row_family": "threshold_matching",
            "coefficient_or_formula_emitted": False,
            "basis_map_emitted": False,
            "precision_convention_emitted": False,
        }
        for slot in threshold_slots
    ] + [
        {
            "slot_id": f"mass_scheme::{slot}",
            "row_family": "mass_scheme_conversion",
            "coefficient_or_formula_emitted": False,
            "basis_map_emitted": False,
            "precision_convention_emitted": False,
        }
        for slot in mass_scheme_slots
    ]

    coefficient_manifest = {
        "schema": "MTTRThetaRowCoefficientSlotManifest.v1",
        "status": "ROW_COEFFICIENT_SLOT_MANIFEST_BUILT_VALUES_OPEN",
        "contract_source": rel(RTHETA_CONTRACT),
        "value_packet_source": rel(VALUE_PACKET),
        "reference_scale": value_packet["reference_scale"],
        "reference_scheme": value_packet["reference_scheme"],
        "coefficient_slots": coefficient_slots,
        "slot_count": len(coefficient_slots),
        "filled_slot_count": sum(1 for row in coefficient_slots if row["coefficient_or_formula_emitted"]),
        "manifest_closed": True,
        "row_coefficients_closed": False,
        "basis_map_closed": False,
        "precision_convention_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(COEFFICIENT_MANIFEST, coefficient_manifest)

    construction_attempt = {
        "schema": "MTTRThetaSourceOwnerRowCoefficientConstructionAttempt.v1",
        "status": "RTHETA_PACKET_CONSTRUCTION_ATTEMPTED_SOURCE_OWNER_AND_COEFFICIENTS_OPEN",
        "functional_symbol": contract["functional_symbol"],
        "source_owner_candidate_matrix": rel(OWNER_MATRIX),
        "row_coefficient_manifest": rel(COEFFICIENT_MANIFEST),
        "accepted_source_owner": None,
        "accepted_threshold_coefficients": [],
        "accepted_mass_scheme_coefficients": [],
        "basis_map_to_value_packet": None,
        "selected_precision_convention": None,
        "profile_response": None,
        "external_profile_workspace_imported": external["accepted_external_likelihood_imported_now"],
        "construction_successful": False,
        "why_not_successful": [
            "all source-owner candidates are precursors only",
            "row coefficient/formula slots are manifest but unfilled",
            "basis map and precision convention are not selected as source data",
            "full profile workspace or diagonal limitation theorem is still absent",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CONSTRUCTION_ATTEMPT, construction_attempt)

    decision = {
        "schema": "MTTRThetaBlockerContractionDecision.v1",
        "status": "PRECURSOR_AND_SLOT_MANIFEST_CLOSED_RTHETA_PACKET_OPEN",
        "previous_status": previous["status"],
        "support_decision_status": support_decision["status"],
        "source_owner_candidate_matrix_closed": True,
        "best_current_precursor_identified": True,
        "row_coefficient_slot_manifest_closed": True,
        "accepted_rtheta_source_owner": False,
        "row_coefficients_filled": False,
        "rtheta_packet_constructed": False,
        "selected_threshold_response_functional_instantiated": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "contracted_frontier": [
            "bridge same-source dynamic matter/overlap packet to VSD02 threshold response owner",
            "derive threshold and mass-scheme coefficient formulas",
            "select precision convention before measured-value comparison",
            "attach full profile response or diagonal limitation theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterRThetaOwnerCoefficientAttempt.v1",
        "status": "NEXT_ATTACK_COEFFICIENT_FORMULAS_OR_SELECTED_OWNER_BRIDGE",
        "closed_now": {
            "source_owner_candidate_matrix": True,
            "best_precursor_identified": True,
            "row_coefficient_slot_manifest": True,
            "construction_attempt_without_overclaim": True,
        },
        "still_open": decision["contracted_frontier"],
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive coefficient formulas from same-source dynamic matter/overlap packet",
            "route_B": "prove bridge theorem from first-response operator layer to VSD02 threshold owner",
            "route_C": "ingest full external profile workspace and keep source rows internal",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaSourceOwnerRowCoefficientPacketOrBlockerContraction",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_source_owner_candidate_matrix": rel(OWNER_MATRIX),
            "rtheta_row_coefficient_slot_manifest": rel(COEFFICIENT_MANIFEST),
            "rtheta_source_owner_row_coefficient_construction_attempt": rel(CONSTRUCTION_ATTEMPT),
            "rtheta_blocker_contraction_decision": rel(DECISION),
            "next_cutset_after_rtheta_owner_coefficient_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaSourceOwnerPrecursorAndCoefficientSlotManifestTheorem",
            "proved": True,
            "statement": (
                "Existing source-owner-like artifacts can be audited against the R_theta owner requirement. "
                "The same-source dynamic matter/overlap packet is the strongest current precursor, and the "
                "terminal SM-slot functor plus Qa/SU3 parity packet remain useful support. None is an accepted "
                "VSD02 threshold response source owner. The required threshold and mass-scheme row coefficient "
                "slots can be listed exactly, but no slot is filled yet."
            ),
        },
        "closure_decision": {
            "source_owner_candidate_matrix_closed": True,
            "row_coefficient_slot_manifest_closed": True,
            "accepted_rtheta_source_owner_closed": False,
            "row_coefficients_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RThetaSourceOwnerRowCoefficientPacket_or_BlockerContraction_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_owner_candidate_matrix_closed": True,
        "row_coefficient_slot_manifest_closed": True,
        "accepted_rtheta_source_owner_count": owner_matrix["accepted_rtheta_source_owner_count"],
        "filled_coefficient_slot_count": coefficient_manifest["filled_slot_count"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaSourceOwnerRowCoefficientPacket or BlockerContraction v1

Status: `{STATUS}`.

This artifact tests whether the newly relevant source-owner-like packets can
instantiate `R_theta`.

```text
source-owner candidates audited : {owner_matrix["candidate_count"]}
accepted R_theta source owners  : 0
row coefficient slots listed    : {coefficient_manifest["slot_count"]}
row coefficient slots filled    : 0
best current precursor          : same_source_dynamic_matter_overlap_packet
```

The same-source dynamic matter/overlap packet is the strongest precursor, but
it does not yet emit VSD02 threshold or mass-scheme coefficient formulas.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
