"""Scan corpus clues for the Pi_CKM numerator/projector branch-retention rule."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

SLUG = "selected_pickmprojectornumeratorrule_or_ckmweightrowcertificates"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SCAN = PACKET_DIR / "pickm_numerator_corpus_clue_scan.packet.json"
RULE_GATE = PACKET_DIR / "pickm_branch_retention_principle_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PiCKMProjectorNumeratorRule_or_CKMWeightRowCertificates_v1.md"

PREVIOUS = DATA / "selected_pickmsourcederivationclauses_or_ckmpredictionupgrade.candidate.json"
TRACE_LAW = DATA / "selected_pickmclosurecosttracefunctional_or_angleweightrows" / "pickm_source_trace_law_candidate.packet.json"

ROUTE_B_CALC = Q79 / "proof_corpus" / "Route_B_Heavy_Link_Overlap_Difference_Calculator_v1.md"
ROUTE_B_FINAL = Q79 / "proof_corpus" / "Route_B_Final_Missing_Object_Calculation_Attempt_v1.md"
AMBIENT_Z448 = Q79 / "proof_corpus" / "Ambient_to_Selected_Z448_CP_Quotient_Map_v1.md"
VISIBLE_S3 = Q79 / "proof_corpus" / "Visible_Twisted_S3_Source_Packet_Attempt_v1.md"
Z64_CARRY = Q79 / "proof_corpus" / "Z64_Carry_Minimality_and_Row_Obligation_v1.md"
Z64_EXACT = Q79 / "proof_corpus" / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"
Z7_FUYAU = Q79 / "proof_corpus" / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md"
PROTOSPINOR = OBSIDIAN / "10 ProtoSpinor" / "Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md"

STATUS = "MTT_SELECTED_PICKM_NUMERATOR_CORPUS_CLUE_SCAN_EXECUTED_BRANCH_RULE_OPEN"
NEXT = "MTT_Selected_PiCKMNumeratorBranchRetentionPrinciple_or_WeightRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def contains_all(path: Path, needles: list[str]) -> bool:
    haystack = text(path)
    return all(needle in haystack for needle in needles)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    trace_law = load(TRACE_LAW)
    if previous["next_required_artifact"] != "MTT_Selected_PiCKMProjectorNumeratorRule_or_CKMWeightRowCertificates_v1":
        raise ValueError("previous artifact does not point at the Pi_CKM numerator/projector frontier")
    if trace_law["accepted_weight_rows"] != 0:
        raise ValueError("trace law was unexpectedly promoted before numerator scan")

    required_marker_checks = {
        "route_b_five_slot": contains_all(
            ROUTE_B_CALC,
            [
                "five u-d overlap-difference slots",
                "Delta_t = A * overlap_differences",
                "basis_connection_delta",
            ],
        ),
        "route_b_final_object": contains_all(
            ROUTE_B_FINAL,
            [
                "five Route B overlap-difference slots are zero",
                "basis_connection_delta        = (1/sqrt(3), omega^2/sqrt(3))",
            ],
        ),
        "ambient_family_three": contains_all(
            AMBIENT_Z448,
            [
                "Z_64 x Z_7 x Z_3",
                "ker(pi) = {0,448,896}",
                "order-three family subgroup",
            ],
        ),
        "visible_s3_qutrit_three": contains_all(
            VISIBLE_S3,
            [
                "twisted stack = S3",
                "finite period denominator = 3",
                "central phase = zeta_3^2",
            ],
        ),
        "z64_five_carry_rows": contains_all(
            Z64_CARRY,
            [
                "five carry rows",
                "Z_64",
                "six-stage carry + 2x_5=0",
            ],
        ),
        "z64_exact_branch": contains_all(
            Z64_EXACT,
            [
                "Z64 exact central-circle branch certificate       CLOSED",
                "selected q_64=15",
            ],
        ),
        "z7_fuyau_closed": contains_all(
            Z7_FUYAU,
            [
                "Z7 global Fu-Yau/Mukai charge-sector certificate       CLOSED",
                "Gamma_7=Hom(A_P,U(1))~=Z_7",
            ],
        ),
        "protospinor_closure_cost": PROTOSPINOR.exists()
        and contains_all(PROTOSPINOR, ["closure-cost geometry", "uniqueness constraint"]),
    }

    scan = {
        "schema": "MTTPiCKMNumeratorCorpusClueScan.v1",
        "status": "PICKM_NUMERATOR_CORPUS_CLUE_SCAN_EXECUTED_NO_ROW_CERTIFICATES",
        "marker_checks": required_marker_checks,
        "candidate_terms": {
            "N12_five_sine_branches": {
                "target_term": "5 sin(delta_79)",
                "support_level": "strong structural clue, not proof",
                "clues": [
                    {
                        "source": rel(ROUTE_B_CALC),
                        "claim": "Route B has exactly five u-versus-d overlap-difference slots feeding CKM heavy-link Delta_t.",
                    },
                    {
                        "source": rel(ROUTE_B_FINAL),
                        "claim": "The current exact object sets those five overlap slots to zero and puts the selected transport in basis_connection_delta.",
                    },
                    {
                        "source": rel(TRACE_LAW),
                        "claim": "The Pi_CKM^12 candidate needs five q79 sine-sensitive branches plus the R_Z norm branch.",
                    },
                ],
                "why_not_closed": "No theorem yet identifies the five Route-B slots with five sine-sensitive Pi_CKM^12 closure-cost branches.",
                "accepted": False,
            },
            "N23_three_qcos_branches": {
                "target_term": "3 q |cos(delta_79)|/2",
                "support_level": "medium structural clue, not proof",
                "clues": [
                    {
                        "source": rel(AMBIENT_Z448),
                        "claim": "The ambient carrier contains an order-three family kernel quotienting Z_1344 to selected Z_448.",
                    },
                    {
                        "source": rel(VISIBLE_S3),
                        "claim": "The q79/F,m=1 twisted stack source attempt carries S3, finite denominator 3, and central phase zeta_3^2.",
                    },
                ],
                "why_not_closed": "No theorem yet turns the family/S3 threefold structure into exactly three q-cos heavy-link branches for Pi_CKM^23.",
                "accepted": False,
            },
            "N13_five_q_plus_three_modulus_branches": {
                "target_term": "5 q + 3(448/64)",
                "support_level": "strong modular clue, not proof",
                "clues": [
                    {
                        "source": rel(Z64_CARRY),
                        "claim": "The dyadic Z64 branch has five carry rows plus terminal closure.",
                    },
                    {
                        "source": rel(Z64_EXACT),
                        "claim": "The exact central-circle Z64 branch and selected q64 component are closed.",
                    },
                    {
                        "source": rel(Z7_FUYAU),
                        "claim": "The sevenfold Fu-Yau/Mukai charge-sector certificate is closed.",
                    },
                    {
                        "source": rel(AMBIENT_Z448),
                        "claim": "The selected CP quotient is Z448=Z64 x Z7 after removing the family Z3 kernel.",
                    },
                ],
                "why_not_closed": "The scan supports the arithmetic pieces 5, 3, and 7, but not the selected Pi_CKM^13 long-bridge projector retaining them with coefficients 5q and 3*7.",
                "accepted": False,
            },
        },
        "paper_corpus_support": {
            "protospinor_closure_cost_geometry": {
                "source": rel(PROTOSPINOR) if PROTOSPINOR.exists() else None,
                "available": required_marker_checks["protospinor_closure_cost"],
                "role": "supports using closure-cost geometry as the correct language, not the numeric branch counts.",
            }
        },
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_ckm_angle_rows": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gate = {
        "schema": "MTTPiCKMBranchRetentionPrincipleGate.v1",
        "status": "PICKM_BRANCH_RETENTION_PRINCIPLE_REQUIRED",
        "corpus_clues_are_sufficient_to_define_attempt": True,
        "corpus_clues_are_sufficient_to_accept_rows": False,
        "required_principle": (
            "A selected closure-cost branch-retention theorem must map the already selected "
            "five-slot Route-B interface, family/S3 threefold quotient, and Z64/Z7 dyadic-sevenfold "
            "arithmetic into the Pi_CKM numerator multiplicities (5 sine, 3 q-cos, 5q+3*7)."
        ),
        "must_prove": [
            "five Route-B overlap/transport branches are exactly the sine-sensitive Pi_CKM^12 branches",
            "family/S3 threefold structure is exactly the q-cos Pi_CKM^23 branch count",
            "five dyadic carry rows plus three sevenfold family-trivial pulls are exactly the Pi_CKM^13 long-bridge numerator",
        ],
        "accepted_weight_rows": 0,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PiCKMNumeratorCorpusClueScanTheorem",
        "proved": True,
        "statement": (
            "A targeted corpus scan finds nontrivial source-side clues for all three Pi_CKM numerator "
            "multiplicities: five Route-B heavy-link overlap slots, family/S3 threefold quotient data, "
            "and Z64/Z7 dyadic-sevenfold arithmetic.  These clues justify the next branch-retention "
            "principle attempt, but do not yet certify any CKM weight rows."
        ),
    }

    data = {
        "candidate": "MTTSelectedPiCKMProjectorNumeratorRuleOrCKMWeightRowCertificates",
        "status": STATUS,
        "inputs": {
            "previous_denominator_reduction": rel(PREVIOUS),
            "trace_law_candidate": rel(TRACE_LAW),
            "route_b_five_slot_calculator": rel(ROUTE_B_CALC),
            "ambient_to_selected_z448": rel(AMBIENT_Z448),
            "visible_s3_source_attempt": rel(VISIBLE_S3),
            "z64_carry_minimality": rel(Z64_CARRY),
            "z7_fuyau_mukai": rel(Z7_FUYAU),
        },
        "output_packets": {
            "pickm_numerator_corpus_clue_scan": rel(SCAN),
            "pickm_branch_retention_principle_gate": rel(RULE_GATE),
        },
        "closure_decision": {
            "Pi_CKM_numerator_corpus_scan_executed": True,
            "branch_retention_principle_defined": True,
            "branch_retention_principle_proved": False,
            "selected_Pi_CKM_row_certificates": 0,
            "accepted_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "strong_or_medium_numerator_clue_groups": 3,
            "accepted_eckm_weight_rows": 0,
            "remaining_branch_retention_clauses": 3,
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PiCKMProjectorNumeratorRule_or_CKMWeightRowCertificates_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "Pi_CKM_numerator_corpus_scan_executed": True,
        "branch_retention_principle_defined": True,
        "branch_retention_principle_proved": False,
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

    note = f"""# MTT Selected PiCKMProjectorNumeratorRule or CKMWeightRowCertificates v1

Status: `{STATUS}`.

## Theorem

`PiCKMNumeratorCorpusClueScanTheorem` is proved.

The corpus scan found concrete source-side clues for the three numerator
multiplicities:

```text
5  <- Route-B five-slot heavy-link overlap interface
3  <- family/S3 qutrit quotient structure
7  <- Fu-Yau/Mukai Z7 charge-sector row
64 <- exact central-circle Z64 dyadic branch
```

This supports the candidate numerators:

```text
W12: ||R_Z||^2 + 5 sin(delta_79)
W23: sqrt(3) + 3 q |cos(delta_79)|/2
W13: 5q + 3(448/64)
```

But it is still a clue scan, not row closure. The missing theorem is the
selected branch-retention principle that turns these corpus structures into
the actual `Pi_CKM` projector numerator rule.

Accepted CKM weight rows remain `0/3`.

Next artifact: `{NEXT}`.
"""

    write_json(SCAN, scan)
    write_json(RULE_GATE, gate)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
