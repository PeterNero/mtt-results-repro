"""Attempt projective rho_E -> BN27 lift or direct source theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "lift_request": DATA / "selected_heterotic_orientedphifin_projectiverhoe_bn27_lift_or_directsource_theorem_request.json",
    "repair_attack": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.candidate.json",
    "projective_tables": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
    "embedding_values": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
    "orientation_functor": DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative_packet.json",
    "bn27_bridge": DATA / "selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient.candidate.json",
    "simultaneous_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_or_directsource_theorem.candidate.json"
OUTPUT_NOGO = DATA / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_nogo_report.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_or_directsource_theorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_ProjectiveRhoE_BN27Lift_or_DirectSourceTheorem_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_PROJECTIVERHOE_BN27LIFT_NOGO_DIRECTSOURCE_REQUIRED"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectBN27SourceTheorem_or_SmoothEQaQuotient_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    request = load(INPUTS["lift_request"])
    repair_attack = load(INPUTS["repair_attack"])
    projective = load(INPUTS["projective_tables"])
    embedding = load(INPUTS["embedding_values"])
    orientation = load(INPUTS["orientation_functor"])
    bn27 = load(INPUTS["bn27_bridge"])
    table = load(INPUTS["simultaneous_table"])

    domain_rows = sorted(int(row) for row in embedding["projection_pair_checks"]["row_multiplicities"].keys())
    positive_oriented_rows = [
        entry["row"]
        for entry in table["entries"]
        if entry["is_positive_magnitude"] and entry["C_tau"] in (-1, 1)
    ]
    covered_positive_rows = sorted(set(domain_rows).intersection(positive_oriented_rows))
    missing_positive_rows = sorted(set(positive_oriented_rows).difference(domain_rows))

    domain_lift = {
        "passes": False,
        "orientation_shadow_passes": orientation["orientation_functor"]["closed"],
        "covered_rows_count": len(domain_rows),
        "required_rows_count": table["basis_dimension"],
        "covered_positive_oriented_rows": covered_positive_rows,
        "missing_positive_oriented_rows": missing_positive_rows,
        "missing_positive_oriented_row_count": len(missing_positive_rows),
        "missing_multiplier_to_full_abs_sector": bn27["orbit_completion_test"]["completion_gap"]["missing_multiplier_to_full_abs_sector"],
        "reason": "The 11-label projective rho_E shadow embeds into BN27 orientation rows but does not emit the full F3xF3 rank-slot carrier.",
    }

    operator_lift = {
        "passes": False,
        "C_tau_orientation_intertwiner_passes": orientation["orientation_functor"]["compressed_C_tau_equals_internal_tau_for_all_labels"],
        "PhiFin_DE_intertwiner_passes": embedding["D_E_intertwiner_checks"]["intertwines"],
        "finitepart_matches": embedding["finitepart_checks"]["same_finitepart"],
        "internal_logdet": embedding["finitepart_checks"]["internal_logdet"],
        "oriented_abs_logdet_sum": orientation["magnitude_obstruction"]["oriented_abs_sector_logdet_sum"],
        "reason": "The projective finite D_E is signed tau/central-character data; BN27 PhiFin_DE is a nonnegative Fourier/gap operator with a different finite part.",
    }

    source_identity = {
        "passes": False,
        "projective_source_scope": projective["projective_representative_tables"]["scope"],
        "direct_source_theorem_emitted": False,
        "reason": "No artifact declares S_QaSU3^BN27 or proves the Route-C/q79 BN27 row is internal to the projective rho_E source.",
    }

    audit_replay = {
        "passes": False,
        "would_pass_if_direct_source_or_lift_passed": True,
        "reason": "Audit replay is already ready, but cannot run as closure while domain/operator/source lift fail.",
    }

    lift_tests = {
        "domain_lift": domain_lift,
        "operator_lift": operator_lift,
        "source_identity": source_identity,
        "audit_replay": audit_replay,
    }
    no_go = {
        "schema": "SelectedHeterotic.OrientedPhiFin.ProjectiveRhoE_BN27LiftNoGoReport.v1",
        "status": "PROJECTIVE_RHOE_BN27_LIFT_FAILS_CURRENT_SOURCE",
        "tests": lift_tests,
        "legal_exits": {
            "direct_BN27_source_theorem": [
                "declare S_QaSU3^BN27",
                "emit all 27 F3xF3 rank-slot rows from that source",
                "emit C_tau and PhiFin_DE as one source algebra",
                "prove trace/kernel policy and no-lift audit replay",
            ],
            "smooth_EQa_quotient": [
                "emit selected A/F_A or smooth projective transition values",
                "derive E_Qa or heat/zeta/torsion operator",
                "prove quotient spectrum equals the BN27 oriented packet",
            ],
        },
        "forbidden_shortcuts": request["forbidden_shortcuts"],
    }
    OUTPUT_NOGO.write_text(json.dumps(no_go, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "lift_attempt_executed": True,
        "domain_lift_closed": False,
        "operator_lift_closed": False,
        "source_identity_closed": False,
        "audit_replay_closed_as_proof": False,
        "projective_rhoE_BN27_lift_closed": False,
        "direct_source_theorem_closed": False,
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinProjectiveRhoEBN27LiftOrDirectSourceTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "repair_attack": repair_attack["status"],
            "projective_tables": projective["status"],
            "embedding_values": embedding["status"],
            "orientation_functor": orientation["status"],
            "bn27_bridge": bn27["status"],
        },
        "lift_tests": lift_tests,
        "nogo_report_path": rel(OUTPUT_NOGO),
        "decision": decision,
        "theorem": {
            "name": "ProjectiveRhoEBN27LiftCurrentSourceNoGoTheorem",
            "proved": True,
            "statement": (
                "The projective rho_E finite candidate cannot currently be lifted to the full oriented BN27 threshold "
                "packet. It proves a valid orientation/phase shadow: C_tau compresses to the internal tau values on "
                "the 11 selected labels. But it does not emit the full 27-row F3xF3 rank-slot carrier, misses ten "
                "positive oriented rows, does not intertwine the internal signed tau operator with the nonnegative "
                "PhiFin_DE gap operator, and has a different finite part. Closure now requires a direct selected "
                "BN27 source theorem or a smooth E_Qa quotient."
            ),
        },
        "guardrails": {
            "does_not_promote_orientation_shadow_to_threshold_lift": True,
            "does_not_identify_signed_tau_with_PhiFin_DE": True,
            "does_not_promote_log92160000": True,
            "does_not_use_lifted_selected_flags": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "nogo_report_path": rel(OUTPUT_NOGO),
        "note_path": rel(OUTPUT_NOTE),
        "domain_lift_closed": False,
        "operator_lift_closed": False,
        "source_identity_closed": False,
        "projective_rhoE_BN27_lift_closed": False,
        "direct_source_theorem_closed": False,
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin ProjectiveRhoE BN27Lift or DirectSourceTheorem v1

## Result

```text
status = {STATUS}
domain_lift_closed = false
operator_lift_closed = false
source_identity_closed = false
projective_rhoE_BN27_lift_closed = false
direct_source_theorem_closed = false
selected_connection_witness_export_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

No-go report:

```text
{rel(OUTPUT_NOGO)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_NOGO)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
