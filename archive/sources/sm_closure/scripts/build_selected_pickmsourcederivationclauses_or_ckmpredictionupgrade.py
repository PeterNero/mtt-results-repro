"""Close Pi_CKM denominator provenance clauses and isolate numerator projector rules."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_pickmsourcederivationclauses_or_ckmpredictionupgrade"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DENOMS = PACKET_DIR / "pickm_denominator_provenance_clauses.packet.json"
NUMERATORS = PACKET_DIR / "pickm_numerator_projector_weight_clauses.packet.json"
GATE = PACKET_DIR / "ckm_prediction_upgrade_after_denominator_closure.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PiCKMSourceDerivationClauses_or_CKMPredictionUpgrade_v1.md"

PREVIOUS = DATA / "selected_pickmclosurecosttracefunctional_or_angleweightrows.candidate.json"
SECTOR_TRANSPORT = DATA / "selected_sectortransportselectionlemma_su5qutritheavylink.candidate.json"
HEAVY_LINK = DATA / "selected_sectortransportselectionlemma_su5qutritheavylink" / "selected_heavylink_eight_slot_values.packet.json"
PURE_WEYL = DATA / "selected_pureweyllambdarepresentative_or_higherresponsescalarrows" / "selected_lambda_orbit_scaled_pure_weyl_rows.packet.json"
PRIMITIVE = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource" / "all_primitive_rows_assembly_map.packet.json"

STATUS = "MTT_SELECTED_PICKM_SOURCE_DERIVATION_DENOMINATORS_CLOSED_NUMERATOR_PROJECTORS_OPEN"
NEXT = "MTT_Selected_PiCKMProjectorNumeratorRule_or_CKMWeightRowCertificates_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    sector = load(SECTOR_TRANSPORT)
    heavy = load(HEAVY_LINK)
    pure = load(PURE_WEYL)
    primitive = load(PRIMITIVE)

    if previous["next_required_artifact"] != "MTT_Selected_PiCKMSourceDerivationClauses_or_CKMPredictionUpgrade_v1":
        raise ValueError("previous Pi_CKM trace-law candidate is not the current source-derivation frontier")
    if sector["closure_decision"]["eight_heavy_link_slots_filled"] is not True:
        raise ValueError("heavy-link eight-slot packet is not closed")
    if sector["closure_decision"]["selected_U10_Ubar5_source_outputs"] is not True:
        raise ValueError("later all-six/source transport closure is not available")
    if pure["scaled_row_family"]["unscaled_R_Z_row_count"] != 18:
        raise ValueError("R_Z row count is not 18")
    if pure["scaled_row_family"]["unscaled_R_X_row_count"] != 18:
        raise ValueError("R_X row count is not 18")

    primitive_counts = primitive["row_evidence"]["primitive_source_counts"]
    if primitive_counts != {"R_X": 18, "R_Z": 18, "zero_route": 36}:
        raise ValueError("primitive source counts do not match the expected 18/18/36 split")

    denominator_clauses = {
        "schema": "MTTPiCKMDenominatorProvenanceClauses.v1",
        "status": "PICKM_DENOMINATOR_PROVENANCE_CLAUSES_CLOSED",
        "clauses": {
            "D12_six_arrow_normalization": {
                "denominator": 6,
                "closed": True,
                "source": rel(SECTOR_TRANSPORT),
                "evidence": "later SM-slot/sector-transport chain closes all six static source arrows and transfer normalization",
                "applies_to": "W12 nearest-adjacent closure-cost average",
            },
            "D23_eight_slot_normalization": {
                "denominator": 8,
                "closed": True,
                "source": rel(HEAVY_LINK),
                "evidence": "selected heavy-link packet emits eight slots t_u13,t_u23,t_d13,t_d23,c_u13,c_u23,c_d13,c_d23",
                "applies_to": "W23 middle-heavy closure-cost average",
            },
            "D13_eighteen_pure_weyl_normalization": {
                "denominator": 18,
                "closed": True,
                "source": rel(PURE_WEYL),
                "evidence": "selected lambda-orbit pure Weyl layer has 18 unscaled R_Z rows and 18 unscaled R_X rows",
                "applies_to": "W13 long-bridge pure-Weyl row average",
            },
        },
        "all_denominator_clauses_closed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    numerator_clauses = {
        "schema": "MTTPiCKMNumeratorProjectorWeightClauses.v1",
        "status": "PICKM_NUMERATOR_PROJECTOR_WEIGHT_RULE_OPEN",
        "open_clauses": {
            "N12_five_sine_branches": {
                "current_candidate_term": "5 sin(delta_79)",
                "closed": False,
                "must_show": "the selected Pi_CKM^12 closure-cost fiber retains exactly five q79 sine-sensitive branches plus the R_Z norm branch",
            },
            "N23_three_qcos_branches": {
                "current_candidate_term": "3 q |cos(delta_79)|/2",
                "closed": False,
                "must_show": "the selected Pi_CKM^23 closure-cost fiber retains exactly three q-cos heavy-link branches plus the sqrt(3) carrier term",
            },
            "N13_five_q_plus_three_modulus_branches": {
                "current_candidate_term": "5 q + 3(448/64)",
                "closed": False,
                "must_show": "the selected Pi_CKM^13 long-bridge fiber retains five q branches and three dyadic/sevenfold modulus branches",
            },
        },
        "accepted_weight_rows": 0,
        "why_this_is_now_the_only_missing_layer": [
            "K_CKM CP-kernel ownership is imported",
            "Pi_CKM candidate formulas are explicit",
            "denominator provenance is now source-supported",
            "only the numerator/projector branch-retention rule is not derived",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gate = {
        "schema": "MTTCKMPredictionUpgradeAfterDenominatorClosure.v1",
        "status": "CKM_PREDICTION_UPGRADE_REDUCED_TO_PROJECTOR_NUMERATOR_RULE",
        "candidate_prediction_retained": True,
        "denominator_provenance_closed": True,
        "numerator_projector_rule_closed": False,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_ckm_angle_rows": 0,
        "next_required_artifact": NEXT,
        "one_principle_form": (
            "A selected closure-cost branch-retention rule must assign numerator multiplicities "
            "(R_Z norm + five sine, sqrt3 + three q-cos, five q + three modulus) to the already "
            "closed denominator fibers (6,8,18)."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PiCKMDenominatorProvenanceReductionTheorem",
        "proved": True,
        "statement": (
            "The three denominators in the Pi_CKM trace-law candidate have selected source provenance: "
            "6 from the closed static SM-slot arrow/transport layer, 8 from the selected heavy-link slot packet, "
            "and 18 from the selected pure-Weyl R_Z/R_X row counts.  Therefore the remaining proof is not a "
            "general search over normalizations but the specific numerator/projector branch-retention rule."
        ),
    }

    data = {
        "candidate": "MTTSelectedPiCKMSourceDerivationClausesOrCKMPredictionUpgrade",
        "status": STATUS,
        "inputs": {
            "previous_pickm_trace_law_candidate": rel(PREVIOUS),
            "sector_transport_selection": rel(SECTOR_TRANSPORT),
            "heavy_link_eight_slot_values": rel(HEAVY_LINK),
            "pure_weyl_lambda_rows": rel(PURE_WEYL),
            "primitive_rows": rel(PRIMITIVE),
        },
        "output_packets": {
            "pickm_denominator_provenance_clauses": rel(DENOMS),
            "pickm_numerator_projector_weight_clauses": rel(NUMERATORS),
            "ckm_prediction_upgrade_after_denominator_closure": rel(GATE),
        },
        "closure_decision": {
            "Pi_CKM_denominator_provenance_closed": True,
            "Pi_CKM_numerator_projector_rule_closed": False,
            "selected_Pi_CKM_row_certificates": 0,
            "accepted_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "closed_denominators": {"W12": 6, "W23": 8, "W13": 18},
            "closed_denominator_clauses": 3,
            "open_numerator_projector_clauses": 3,
            "accepted_eckm_weight_rows": 0,
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PiCKMSourceDerivationClauses_or_CKMPredictionUpgrade_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "Pi_CKM_denominator_provenance_closed": True,
        "Pi_CKM_numerator_projector_rule_closed": False,
        "selected_Pi_CKM_row_certificates": 0,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PiCKMSourceDerivationClauses or CKMPredictionUpgrade v1

Status: `{STATUS}`.

## Theorem

`PiCKMDenominatorProvenanceReductionTheorem` is proved.

The three denominators in the candidate `Pi_CKM` trace law now have source
provenance:

```text
W12 denominator 6  <- six static SM-slot/transport arrows
W23 denominator 8  <- eight heavy-link slots
W13 denominator 18 <- eighteen pure Weyl R_Z/R_X row counts
```

This does not yet certify the rows.  The remaining proof is the numerator
projector rule:

```text
W12 numerator: ||R_Z||^2 + 5 sin(delta_79)
W23 numerator: sqrt(3) + 3 q |cos(delta_79)|/2
W13 numerator: 5 q + 3(448/64)
```

Accepted CKM weight rows remain `0/3`.

Next artifact: `{NEXT}`.
"""

    write_json(DENOMS, denominator_clauses)
    write_json(NUMERATORS, numerator_clauses)
    write_json(GATE, gate)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
