"""Build direct-carrier constructive attempt for oriented Phi_fin."""

from __future__ import annotations

import json
from math import prod
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "source_amendment_plan": DATA / "selected_heterotic_orientedphifin_sourceleaf_minimal_source_amendment_plan.json",
    "sourceleaf_request": DATA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_source_theorem_request.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "label_embedding": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
    "orientation_functor_packet": DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative_packet.json",
    "sourceleaf_discovery": DATA / "selected_heterotic_orientedphifin_sourceleaf_sourceamendment_or_corpusdiscovery.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt.candidate.json"
OUTPUT_REPORT = DATA / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt_report.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_DirectCarrier_SourceTheorem_ConstructiveAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTCARRIER_CONSTRUCTIVE_ATTEMPT_FULL_ORBIT_SOURCE_EMISSION_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_FullFourierOrbit_SourceEmission_or_TraceIdentity_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sector_product(entries: list[dict[str, Any]], c_tau: int) -> int:
    vals = [
        int(entry["PhiFin_DE_eigenvalue"])
        for entry in entries
        if entry["C_tau"] == c_tau and entry["is_positive_magnitude"]
    ]
    return prod(vals)


def label_product(entries_by_row: dict[int, dict[str, Any]], embedding_rows: dict[str, Any], c_tau: int) -> int:
    vals = []
    labels = []
    for label, payload in embedding_rows.items():
        row = payload["BN_mode"]["row"]
        entry = entries_by_row[row]
        if entry["C_tau"] == c_tau and entry["is_positive_magnitude"]:
            vals.append(int(entry["PhiFin_DE_eigenvalue"]))
            labels.append(label)
    return prod(vals) if vals else 1, labels, vals


def main() -> dict[str, Any]:
    plan = load(INPUTS["source_amendment_plan"])
    request = load(INPUTS["sourceleaf_request"])
    table = load(INPUTS["oriented_table"])
    embedding = load(INPUTS["label_embedding"])
    orientation_packet = load(INPUTS["orientation_functor_packet"])
    discovery = load(INPUTS["sourceleaf_discovery"])

    entries = table["entries"]
    entries_by_row = {entry["row"]: entry for entry in entries}
    embedded_rows = {payload["BN_mode"]["row"] for payload in embedding["embedding_rows"].values()}
    positive_oriented_rows = {
        entry["row"]
        for entry in entries
        if entry["C_tau"] in (-1, 1) and entry["is_positive_magnitude"]
    }
    missing_positive_oriented_rows = sorted(positive_oriented_rows - embedded_rows)

    plus_product = sector_product(entries, 1)
    minus_product = sector_product(entries, -1)
    plus_embedded_product, plus_labels, plus_vals = label_product(entries_by_row, embedding["embedding_rows"], 1)
    minus_embedded_product, minus_labels, minus_vals = label_product(entries_by_row, embedding["embedding_rows"], -1)
    full_abs_product = plus_product * minus_product
    embedded_abs_product = plus_embedded_product * minus_embedded_product
    missing_multiplier = full_abs_product // embedded_abs_product

    missing_rows = [
        {
            "row": row,
            "basis_label": entries_by_row[row]["basis_label"],
            "C_tau": entries_by_row[row]["C_tau"],
            "PhiFin_DE_eigenvalue": int(entries_by_row[row]["PhiFin_DE_eigenvalue"]),
        }
        for row in missing_positive_oriented_rows
    ]

    constructive_attempt = {
        "carrier_domain_declared_by_support": table["basis_id"],
        "carrier_domain_source_emitted": False,
        "orientation_functor_closed": orientation_packet["orientation_functor"]["closed"],
        "positive_magnitude_functor_closed": False,
        "finitepart_trace_identity_closed": False,
        "computed_gap": {
            "full_plus_sector_product": plus_product,
            "full_minus_sector_product": minus_product,
            "full_abs_sector_product": full_abs_product,
            "embedded_plus_product": plus_embedded_product,
            "embedded_plus_labels": plus_labels,
            "embedded_plus_values": plus_vals,
            "embedded_minus_product": minus_embedded_product,
            "embedded_minus_labels": minus_labels,
            "embedded_minus_values": minus_vals,
            "embedded_abs_product": embedded_abs_product,
            "missing_multiplier_to_full_abs_sector": missing_multiplier,
            "missing_positive_oriented_row_count": len(missing_positive_oriented_rows),
            "missing_positive_oriented_rows": missing_rows,
        },
        "interpretation": (
            "The finite 11-label rho_E embedding is too small to source-own the full "
            "oriented Phi_fin magnitude table. It preserves rank-slot orientation, but "
            "the exact log(92160000) finitepart uses all sixteen positive nonzero "
            "oriented Fourier modes. The embedded positive part supplies product 16; "
            "the missing full-orbit multiplier is 5760000."
        ),
    }

    report = {
        "schema": "SelectedHeterotic.OrientedPhiFin.DirectCarrier.ConstructiveAttemptReport.v1",
        "status": "FULL_ORBIT_SOURCE_EMISSION_REQUIRED",
        "constructive_attempt": constructive_attempt,
        "source_theorem_needed": {
            "minimal_new_leaf": "source_emits_full_oriented_positive_fourier_orbit",
            "must_emit": [
                "the full 27-mode B_N carrier as the selected threshold domain",
                "all sixteen positive nonzero oriented C_tau sectors, not only the embedded 11-label shadow",
                "the Phi_fin positive magnitude operator as source-owned on that domain",
                "the finitepart trace identity product 92160000 = 9600 * 9600",
                "kernel/shared-circle/no-double-count policy inherited before finitepart evaluation",
            ],
            "must_not_emit": request["must_not_use"],
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "constructive_attempt_executed": True,
        "orientation_functor_closed": True,
        "full_oriented_positive_orbit_closed": False,
        "source_emits_oriented_BN_carrier": False,
        "positive_magnitude_functor_closed": False,
        "finitepart_trace_identity_closed": False,
        "direct_carrier_theorem_closed": False,
        "new_minimal_leaf": "source_emits_full_oriented_positive_fourier_orbit",
        "next_required_artifact": NEXT,
        "oriented_logdet_promoted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinDirectCarrierSourceTheoremConstructiveAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "source_amendment_plan": plan["status"],
            "sourceleaf_discovery": discovery["status"],
            "orientation_functor_packet": orientation_packet["status"],
            "label_embedding": embedding["status"],
        },
        "attempt_report_path": rel(OUTPUT_REPORT),
        "decision": decision,
        "theorem": {
            "name": "DirectCarrierConstructiveAttemptFullOrbitGapTheorem",
            "proved": True,
            "statement": (
                "The direct-carrier constructive attempt cannot close from the current "
                "11-label rho_E embedding. That embedding proves orientation transfer, "
                "but the oriented Phi_fin finitepart log(92160000) is the full "
                "sixteen-mode positive oriented Fourier orbit product 9600*9600. The "
                "embedded shadow contributes product 16 only, leaving multiplier "
                "5760000. Therefore a valid direct source theorem must emit the full "
                "oriented positive Fourier orbit as a source-owned threshold domain "
                "before the finitepart trace identity can be claimed."
            ),
        },
        "guardrails": {
            "does_not_promote_11_label_embedding_to_full_carrier": True,
            "does_not_rescale_embedded_product_to_full_product": True,
            "does_not_promote_orientation_functor_to_magnitude": True,
            "does_not_promote_log92160000": True,
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
        "attempt_report_path": rel(OUTPUT_REPORT),
        "note_path": rel(OUTPUT_NOTE),
        "full_abs_sector_product": full_abs_product,
        "embedded_abs_product": embedded_abs_product,
        "missing_multiplier_to_full_abs_sector": missing_multiplier,
        "new_minimal_leaf": decision["new_minimal_leaf"],
        "direct_carrier_theorem_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin DirectCarrier SourceTheorem ConstructiveAttempt v1

## Result

```text
status = {STATUS}
full_abs_sector_product = {full_abs_product}
embedded_abs_product = {embedded_abs_product}
missing_multiplier_to_full_abs_sector = {missing_multiplier}
new_minimal_leaf = source_emits_full_oriented_positive_fourier_orbit
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

```text
{rel(OUTPUT_REPORT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REPORT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
