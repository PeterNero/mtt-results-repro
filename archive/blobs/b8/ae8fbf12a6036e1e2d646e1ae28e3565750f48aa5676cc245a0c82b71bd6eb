"""Attempt to prove selection of the visible L^2 pullback-Cech packet.

The previous packet gave an exact conditional H^1 calculation with h1=8 but
kept the data as UNSELECTED_FIXTURE.  This script checks whether the remaining
gap is mathematical or purely source-selection:

1. validate the actual unselected packet;
2. validate the same matrices under the minimal hypothetical SELECTED_DATA
   source metadata;
3. inspect the nearby source certificates for an existing MTT selection
   certificate for this pullback representative.

The result is intentionally honest.  If the hypothetical selected packet
promotes but the source certificate is absent, the theorem is reduced to the
single missing selection certificate rather than overclosed.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
VALIDATOR = ROOT / "scripts" / "validate_visible_rank2_l2_cohomology.py"

PULLBACK_CERT = CERTIFICATES / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
PULLBACK_PACKET = CANDIDATE_DATA / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
SOURCE_HUNT = CERTIFICATES / "visible_rank2_l2_cohomology_source_hunt_certificate.json"
DECK_SCAFFOLD = CERTIFICATES / "iwasawa_standard_lattice_deck_scaffold_certificate.json"
GERBE_DECK = CERTIFICATES / "time_oriented_m1_deck_cech_lift_certificate.json"
S3_CLOSURE = CERTIFICATES / "visible_twisted_s3_class_restriction_closure_certificate.json"
CONSTANTS_LINE_INTERFACE = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob"
) / "certificates" / "selected_qa_su3_iwasawa_line_bundle_section_ring_interface_certificate.json"
CONSTANTS_AUTOMORPHY_ATTEMPT = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob"
) / "certificates" / "selected_qa_su3_iwasawa_automorphy_or_section_ring_construction_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_pullback_selection_attempt.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_pullback_selection_attempt_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def maybe_load_json(path: Path) -> dict[str, Any]:
    return load_json(path) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(packet: dict[str, Any]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "visible_l2_packet.json"
        path.write_text(json.dumps(packet, indent=2, sort_keys=True), encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR), str(path)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    parsed_report: dict[str, Any] | None = None
    prefix = "visible_rank2_l2_h1_report="
    for line in proc.stdout.splitlines():
        if line.startswith(prefix):
            parsed_report = json.loads(line[len(prefix) :])
            break
    return {
        "returncode": proc.returncode,
        "passes": proc.returncode == 0 and "validation PASS" in proc.stdout,
        "promotes_to_non_split_V_alpha_input": (
            parsed_report or {}
        ).get("promotes_to_non_split_V_alpha_input"),
        "selected_source_promotes": (parsed_report or {}).get("selected_source_promotes"),
        "h1": (parsed_report or {}).get("h1"),
        "nonzero_ext_class": (parsed_report or {}).get("nonzero_ext_class"),
        "stdout": proc.stdout,
    }


def selected_hypothesis(packet: dict[str, Any]) -> dict[str, Any]:
    selected = copy.deepcopy(packet)
    selected["candidate_role"] = "SELECTED_DATA"
    selected["status"] = "COMPLETE_SELECTED_PULLBACK_HYPOTHESIS"
    selected["source"]["selected_by_mtt"] = True
    selected["source"]["fixture_only"] = False
    selected["source"]["source_certificate"] = (
        "MISSING_SELECTED_PULLBACK_L2_SOURCE_CERTIFICATE"
    )
    return selected


def status(path: Path) -> str | None:
    data = maybe_load_json(path)
    return data.get("status")


def analyze() -> dict[str, Any]:
    pullback_cert = load_json(PULLBACK_CERT)
    packet = load_json(PULLBACK_PACKET)
    source_hunt = maybe_load_json(SOURCE_HUNT)
    constants_line = maybe_load_json(CONSTANTS_LINE_INTERFACE)
    constants_automorphy = maybe_load_json(CONSTANTS_AUTOMORPHY_ATTEMPT)

    actual_validation = run_validator(packet)
    hypothetical_packet = selected_hypothesis(packet)
    hypothetical_validation = run_validator(hypothetical_packet)

    evidence = {
        "pullback_packet_conditional_h1_positive": pullback_cert.get("status")
        == "VISIBLE_RANK2_L2_PULLBACK_CECH_ATTEMPT_CONDITIONAL_H1_POSITIVE_SELECTION_OPEN",
        "actual_unselected_packet_validates": actual_validation["passes"],
        "actual_packet_does_not_promote": actual_validation[
            "promotes_to_non_split_V_alpha_input"
        ]
        is False,
        "hypothetical_selected_same_matrices_promote": hypothetical_validation[
            "promotes_to_non_split_V_alpha_input"
        ]
        is True,
        "hypothetical_h1_stays_8": hypothetical_validation["h1"] == 8,
        "source_hunt_still_reports_selected_data_absent": status(SOURCE_HUNT)
        == "VISIBLE_RANK2_L2_COHOMOLOGY_SOURCE_HUNT_BLOCKED_SELECTED_DATA_ABSENT",
        "standard_deck_scaffold_selection_still_open": status(DECK_SCAFFOLD)
        == "STANDARD_IWASAWA_DECK_SCAFFOLD_FORMULATED_SELECTION_OPEN",
        "finite_gerbe_deck_pullback_closed_but_not_L2_source": status(GERBE_DECK)
        == "TIME_ORIENTED_M1_DECK_CECH_LIFT_CLOSED_GEOMETRIC_OPERATOR_SOURCE_OPEN",
        "s3_class_restriction_closed_but_not_L2_source": status(S3_CLOSURE)
        == "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_CLOSED_OPERATOR_SOURCE_OPEN",
        "constants_line_section_ring_interface_still_open": constants_line.get("status")
        == "QA_SU3_IWASAWA_LINE_BUNDLE_SECTION_RING_INTERFACE_BUILT_VALUES_OPEN",
        "constants_automorphy_attempt_symbolic_only_values_open": constants_automorphy.get(
            "status"
        )
        == "QA_SU3_IWASAWA_AUTOMORPHY_SECTION_RING_CONSTRUCTION_SYMBOLIC_ONLY_VALUES_OPEN",
    }

    missing_source_fields = [
        "source certificate selecting the base-pullback L^2 representative",
        "raw good-cover transition functions or equivalent selected automorphy factors",
        "proof the standard Iwasawa deck scaffold and projection pi are selected for this visible line bundle",
        "proof no extra flat/torsion twist changes the selected representative",
        "same-branch stability and HYM/Route-C source continuation",
    ]

    relative_theorem_proved = (
        evidence["pullback_packet_conditional_h1_positive"]
        and evidence["actual_unselected_packet_validates"]
        and evidence["actual_packet_does_not_promote"]
        and evidence["hypothetical_selected_same_matrices_promote"]
        and evidence["hypothetical_h1_stays_8"]
    )
    unconditional_selection_proved = (
        relative_theorem_proved
        and not evidence["source_hunt_still_reports_selected_data_absent"]
        and not evidence["standard_deck_scaffold_selection_still_open"]
    )
    status_value = (
        "VISIBLE_RANK2_L2_PULLBACK_SELECTION_PROVED"
        if unconditional_selection_proved
        else "VISIBLE_RANK2_L2_PULLBACK_SELECTION_REDUCED_TO_SOURCE_CERTIFICATE"
    )

    return {
        "calculation": "VisibleRank2L2PullbackSelectionAttempt",
        "status": status_value,
        "generated_by": "scripts/prove_visible_rank2_l2_pullback_selection_attempt.py",
        "input_certificates": {
            "pullback_cech_attempt": PULLBACK_CERT.name,
            "pullback_cohomology_packet": "candidate_data/visible_rank2_l2_pullback_cech_attempt.cohomology.json",
            "source_hunt": SOURCE_HUNT.name,
            "standard_deck_scaffold": DECK_SCAFFOLD.name,
            "time_oriented_m1_deck_cech_lift": GERBE_DECK.name,
            "visible_twisted_s3_class_restriction_closure": S3_CLOSURE.name,
            "constants_line_section_ring_interface": str(CONSTANTS_LINE_INTERFACE),
            "constants_automorphy_attempt": str(CONSTANTS_AUTOMORPHY_ATTEMPT),
        },
        "selection_evidence": evidence,
        "actual_unselected_validation": actual_validation,
        "hypothetical_selected_validation": hypothetical_validation,
        "relative_selection_theorem": {
            "proved": relative_theorem_proved,
            "statement": (
                "If MTT supplies a source certificate selecting the base-pullback "
                "typed Cech line bundle with the already-computed transition class, "
                "then the unchanged finite packet is SELECTED_DATA, h1=8, and the "
                "validator promotes it to a non-split V_alpha input."
            ),
            "matrices_changed_between_actual_and_hypothetical": False,
            "changed_only_source_metadata": [
                "candidate_role",
                "status",
                "source.selected_by_mtt",
                "source.fixture_only",
                "source.source_certificate",
            ],
        },
        "unconditional_selection_theorem": {
            "proved": unconditional_selection_proved,
            "blocked_by": missing_source_fields if not unconditional_selection_proved else [],
            "reason": (
                "The repo proves the conditional H1/Ext mathematics, but no "
                "audited source currently selects the base-pullback L^2 "
                "representative. Existing gerbe/S3 pullback closures are source "
                "evidence for adjacent twisted sectors, not this line bundle; "
                "the constants automorphy attempt is symbolic-only and also "
                "does not supply factors for this packet."
            )
            if not unconditional_selection_proved
            else "Selected source certificate is present.",
        },
        "what_this_closes": {
            "mathematical_gap_between_pullback_packet_and_selected_packet": relative_theorem_proved,
            "h1_and_nonzero_Ext_would_promote_if_selection_certificate_exists": relative_theorem_proved,
            "unconditional_MTT_selection_of_L2_pullback": unconditional_selection_proved,
        },
        "still_open": {
            "write_or_find_selected_pullback_L2_source_certificate": not unconditional_selection_proved,
            "supply_raw_transition_or_automorphy_data_from_selected_source": not unconditional_selection_proved,
            "prove_no_extra_flat_or_torsion_twist_selected": not unconditional_selection_proved,
            "promote_packet_to_SELECTED_DATA": not unconditional_selection_proved,
            "prove_non_split_extension_stability": True,
            "prove_HYM_or_Route_C_residual": True,
            "derive_same_total_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_unconditional_MTT_selection": unconditional_selection_proved,
            "claims_selected_packet_written": False,
            "claims_raw_good_cover_transitions_supplied": False,
            "claims_stability_proved": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The selection theorem is not unconditionally proved from current "
                "sources. What is proved is sharper: selection is the only remaining "
                "gap for the L^2 Ext packet. With identical matrices, the validator "
                "promotes the h1=8 packet as soon as source.selected_by_mtt is supplied."
            ),
            "next_action": (
                "Prove or source-print the selected base-pullback L^2 automorphy "
                "certificate. It must select pi^*M, rule out extra flat/torsion "
                "twists, and attach the representative to the same visible V_alpha branch."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2PullbackSelectionAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_pullback_selection_attempt.candidate.json",
        "input_certificates": report["input_certificates"],
        "selection_evidence": report["selection_evidence"],
        "relative_selection_theorem": report["relative_selection_theorem"],
        "unconditional_selection_theorem": report["unconditional_selection_theorem"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["relative_selection_theorem"]["proved"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
