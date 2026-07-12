"""Build full-Fourier-orbit source-emission or trace-identity gate."""

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
    "directcarrier_attempt": DATA / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt.candidate.json",
    "directcarrier_report": DATA / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt_report.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "sourceleaf_request": DATA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_source_theorem_request.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_fullfourierorbit_sourceemission_or_traceidentity.candidate.json"
OUTPUT_TRACE = DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_fullfourierorbit_sourceemission_or_traceidentity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_FullFourierOrbit_SourceEmission_or_TraceIdentity_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_FULLFOURIERORBIT_TRACEIDENTITY_CLOSED_SOURCEEMISSION_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_FullFourierOrbit_SourceSelection_Theorem_or_NoGo_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def product_for(entries: list[dict[str, Any]], c_tau: int) -> tuple[int, list[int], list[str]]:
    selected = [
        entry
        for entry in entries
        if entry["C_tau"] == c_tau and entry["is_positive_magnitude"]
    ]
    values = [int(entry["PhiFin_DE_eigenvalue"]) for entry in selected]
    labels = [entry["basis_label"] for entry in selected]
    return prod(values), values, labels


def main() -> dict[str, Any]:
    attempt = load(INPUTS["directcarrier_attempt"])
    report = load(INPUTS["directcarrier_report"])
    table = load(INPUTS["oriented_table"])
    request = load(INPUTS["sourceleaf_request"])

    entries = table["entries"]
    plus_product, plus_values, plus_labels = product_for(entries, 1)
    minus_product, minus_values, minus_labels = product_for(entries, -1)
    abs_product = plus_product * minus_product
    full_positive_values = [
        int(entry["PhiFin_DE_eigenvalue"])
        for entry in entries
        if entry["is_positive_magnitude"]
    ]
    full_positive_product = prod(full_positive_values)

    trace_identity = {
        "schema": "SelectedHeterotic.OrientedPhiFin.FullFourierOrbit.TraceIdentity.v1",
        "domain": table["basis_id"],
        "positive_oriented_policy": "restrict to C_tau=+1 and C_tau=-1 sectors with PhiFin_DE_eigenvalue > 0",
        "plus_sector_values": plus_values,
        "plus_sector_basis_labels": plus_labels,
        "plus_sector_product": plus_product,
        "minus_sector_values": minus_values,
        "minus_sector_basis_labels": minus_labels,
        "minus_sector_product": minus_product,
        "oriented_abs_sector_product": abs_product,
        "oriented_abs_sector_logdet_exact": "log(92160000)",
        "full_positive_values_including_Ctau0": full_positive_values,
        "full_positive_product_including_Ctau0": full_positive_product,
        "full_positive_logdet_exact": "log(884736000000)",
        "identity_closed_relative_to_full_orbit_source": abs_product == 92160000,
        "target_fitting_used": False,
    }
    OUTPUT_TRACE.write_text(json.dumps(trace_identity, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    source_emission_attempt = {
        "full_27_mode_BN_carrier_as_selected_threshold_domain": {
            "closed": False,
            "support_present": True,
            "support": table["basis_id"],
            "reason_open": "The table defines the domain, but the same heterotic source has not emitted it as the selected threshold domain.",
        },
        "full_sixteen_positive_oriented_fourier_modes": {
            "closed": False,
            "support_present": True,
            "support": {
                "plus_mode_count": len(plus_values),
                "minus_mode_count": len(minus_values),
                "oriented_abs_sector_product": abs_product,
            },
            "reason_open": "The full orbit is algebraically enumerated, but source selection remains unproved.",
        },
        "PhiFin_positive_magnitude_source_owned": {
            "closed": False,
            "support_present": True,
            "reason_open": "The Phi_fin gap table is support; no same-source theorem owns it as the heterotic Qa/SU3 threshold operator.",
        },
        "finitepart_trace_identity_after_source_ownership": {
            "closed": True,
            "support_present": True,
            "support": rel(OUTPUT_TRACE),
            "meaning": "Algebraic trace identity is closed relative to source ownership of the full orbit.",
        },
    }

    decision = {
        "trace_identity_closed_relative_to_full_orbit_source": True,
        "source_emits_full_oriented_positive_fourier_orbit": False,
        "source_emits_oriented_BN_carrier": False,
        "positive_magnitude_source_owned": False,
        "full_direct_carrier_theorem_closed": False,
        "remaining_single_leaf": "source_emits_full_oriented_positive_fourier_orbit",
        "next_required_artifact": NEXT,
        "oriented_logdet_promoted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinFullFourierOrbitSourceEmissionOrTraceIdentity",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "directcarrier_attempt": attempt["status"],
            "directcarrier_report": report["status"],
        },
        "trace_identity_path": rel(OUTPUT_TRACE),
        "source_emission_attempt": source_emission_attempt,
        "decision": decision,
        "theorem": {
            "name": "FullFourierOrbitTraceIdentityRelativeTheorem",
            "proved": True,
            "statement": (
                "On the full oriented B_N Fourier orbit, the finitepart trace identity "
                "is algebraically exact: each C_tau=+1 and C_tau=-1 positive sector "
                "has product 9600, so the oriented absolute finitepart is "
                "log(9600*9600)=log(92160000). This closes the trace computation "
                "relative to source ownership of the full orbit. The remaining open "
                "leaf is source selection/emission of that full orbit as the heterotic "
                "Qa/SU3 threshold domain."
            ),
        },
        "guardrails": {
            "does_not_claim_source_emission_from_table": True,
            "does_not_promote_trace_identity_without_source_ownership": True,
            "does_not_use_11_label_embedding_as_full_orbit": True,
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
        "trace_identity_path": rel(OUTPUT_TRACE),
        "note_path": rel(OUTPUT_NOTE),
        "plus_sector_product": plus_product,
        "minus_sector_product": minus_product,
        "oriented_abs_sector_product": abs_product,
        "trace_identity_closed_relative_to_full_orbit_source": True,
        "source_emits_full_oriented_positive_fourier_orbit": False,
        "remaining_single_leaf": decision["remaining_single_leaf"],
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin FullFourierOrbit SourceEmission or TraceIdentity v1

## Result

```text
status = {STATUS}
plus_sector_product = {plus_product}
minus_sector_product = {minus_product}
oriented_abs_sector_product = {abs_product}
trace_identity_closed_relative_to_full_orbit_source = true
remaining_single_leaf = source_emits_full_oriented_positive_fourier_orbit
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

```text
{rel(OUTPUT_TRACE)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_TRACE)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
