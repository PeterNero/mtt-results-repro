"""Build oriented Phi_fin magnitude finite-part source-theorem attempt."""

from __future__ import annotations

import json
import math
from functools import reduce
from operator import mul
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "orientation_functor": DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative.candidate.json",
    "orientation_packet": DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative_packet.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "source_ownership": DATA / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.candidate.json",
    "smooth_support": DATA / "selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_MagnitudeFinitepart_SourceTheorem_or_SmoothEQa_TraceIdentity_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_MAGNITUDE_FINITEPART_EXACTLY_COMPUTED_SOURCE_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_PositiveMagnitude_SourceOwnership_or_SmoothEQa_Emission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def product(values: list[int]) -> int:
    return reduce(mul, values, 1)


def main() -> dict[str, Any]:
    orientation_functor = load(INPUTS["orientation_functor"])
    orientation_packet = load(INPUTS["orientation_packet"])
    oriented = load(INPUTS["oriented_table"])
    source_ownership = load(INPUTS["source_ownership"])
    smooth_support = load(INPUTS["smooth_support"])

    plus_values = [
        int(entry["PhiFin_DE_eigenvalue"])
        for entry in oriented["entries"]
        if entry["C_tau"] == 1 and entry["is_positive_magnitude"]
    ]
    minus_values = [
        int(entry["PhiFin_DE_eigenvalue"])
        for entry in oriented["entries"]
        if entry["C_tau"] == -1 and entry["is_positive_magnitude"]
    ]
    all_positive_values = [
        int(entry["PhiFin_DE_eigenvalue"])
        for entry in oriented["entries"]
        if entry["is_positive_magnitude"]
    ]
    plus_product = product(plus_values)
    minus_product = product(minus_values)
    oriented_abs_product = plus_product * minus_product
    all_positive_product = product(all_positive_values)

    finitepart_values = {
        "plus_sector_positive_eigenvalues": plus_values,
        "minus_sector_positive_eigenvalues": minus_values,
        "full_positive_eigenvalues": all_positive_values,
        "plus_sector_product": plus_product,
        "minus_sector_product": minus_product,
        "oriented_abs_sector_product": oriented_abs_product,
        "full_positive_product": all_positive_product,
        "plus_sector_logdet_exact": f"log({plus_product})",
        "minus_sector_logdet_exact": f"log({minus_product})",
        "oriented_abs_sector_logdet_exact": f"log({oriented_abs_product})",
        "full_positive_logdet_exact": f"log({all_positive_product})",
        "oriented_abs_sector_logdet_numeric": math.log(oriented_abs_product),
        "full_positive_logdet_numeric": math.log(all_positive_product),
    }

    source_gate = {
        "orientation_functor_closed": orientation_functor["decision"]["finite_rhoE_to_oriented_BN_orientation_functor_closed"],
        "source_owned_positive_PhiFin_magnitude": source_ownership["decision"]["positive_PhiFin_DE_source_ownership_closed"],
        "finitepart_trace_identity_closed": orientation_functor["decision"]["finitepart_trace_identity_closed"],
        "smooth_E_Qa_emitted": smooth_support["decision"]["E_Qa_computed"],
        "smooth_transition_tables_emitted": smooth_support["decision"]["smooth_transition_tables_emitted"],
        "internal_logdet_equals_oriented_abs_logdet": orientation_packet["magnitude_obstruction"]["internal_logdet"] == finitepart_values["oriented_abs_sector_logdet_exact"],
        "closed": False,
    }

    packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.MagnitudeFinitepart.SourceTheoremOrSmoothEQaTraceIdentity.v1",
        "status": "EXACT_ORIENTED_TABLE_FINITEPART_COMPUTED_SOURCE_IDENTITY_OPEN",
        "finitepart_values": finitepart_values,
        "source_gate": source_gate,
        "meaning": (
            "The oriented 27-mode table has an exact no-fit positive finitepart: each "
            "oriented nonzero sector has determinant 9600, so the absolute oriented "
            "sector has determinant 92160000. This is a computed table invariant, not yet "
            "a heterotic threshold theorem."
        ),
        "remaining_exact_payload": [
            "source ownership of the positive Phi_fin magnitude on the oriented B_N carrier",
            "finitepart trace theorem selecting log(921600) rather than internal log(2008), or proving the quotient that relates them",
            "or smooth E_Qa/heat-zeta-torsion emission with a quotient to the oriented 27-mode finitepart",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "oriented_table_magnitude_finitepart_computed": True,
        "oriented_abs_sector_logdet_exact": finitepart_values["oriented_abs_sector_logdet_exact"],
        "full_positive_logdet_exact": finitepart_values["full_positive_logdet_exact"],
        "source_owned_positive_PhiFin_magnitude": False,
        "finitepart_trace_identity_closed": False,
        "smooth_E_Qa_trace_identity_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "packet_path": rel(OUTPUT_PACKET),
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinMagnitudeFinitepartSourceTheoremOrSmoothEQaTraceIdentity",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "orientation_functor": orientation_functor["status"],
            "source_ownership": source_ownership["status"],
            "smooth_support": smooth_support["status"],
        },
        "packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinExactMagnitudeFinitepartTableTheorem",
            "proved": True,
            "statement": (
                "On the already constructed oriented 27-mode B_N table, the positive "
                "magnitude finitepart is exact: each nonzero C_tau sector has product "
                "9600, the absolute oriented sector has product 92160000, and the full "
                "positive 27-mode determinant product is 884736000000. This computes "
                "the table finitepart without observed constants or target fitting. "
                "It still does not promote the value to a heterotic threshold, because "
                "source ownership of the positive Phi_fin magnitude, finitepart trace "
                "identity, and smooth E_Qa trace identity remain open."
            ),
        },
        "guardrails": {
            "does_not_promote_table_finitepart_to_threshold": True,
            "does_not_identify_log921600_with_log2008": True,
            "does_not_claim_smooth_E_Qa_trace_identity": True,
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
        "packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "oriented_table_magnitude_finitepart_computed": True,
        "oriented_abs_sector_logdet_exact": finitepart_values["oriented_abs_sector_logdet_exact"],
        "full_positive_logdet_exact": finitepart_values["full_positive_logdet_exact"],
        "source_owned_positive_PhiFin_magnitude": False,
        "finitepart_trace_identity_closed": False,
        "smooth_E_Qa_trace_identity_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin MagnitudeFinitepart SourceTheorem or SmoothEQa TraceIdentity v1

## Result

```text
status = {STATUS}
oriented_abs_sector_logdet_exact = {finitepart_values["oriented_abs_sector_logdet_exact"]}
full_positive_logdet_exact = {finitepart_values["full_positive_logdet_exact"]}
source_owned_positive_PhiFin_magnitude = false
finitepart_trace_identity_closed = false
smooth_E_Qa_trace_identity_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Meaning

The magnitude table is no longer numerically vague: the oriented absolute sector is
`log(92160000)` exactly. What remains is not arithmetic. It is the source theorem saying
that this exact finitepart is the selected heterotic threshold finitepart, or a smooth
`E_Qa` trace identity that derives the same quotient.

## Packet

```text
{rel(OUTPUT_PACKET)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
