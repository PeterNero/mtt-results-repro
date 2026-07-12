"""Build BN27 source-domain bridge or smooth E_Qa quotient gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "branch_fill": DATA / "selected_heterotic_orientedphifin_branchidentity_minimalsourcecertificate_fill.candidate.json",
    "fill_report": DATA / "selected_heterotic_orientedphifin_branchidentity_fill_attempt_report.json",
    "embedding_values": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
    "directcarrier_report": DATA / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt_report.json",
    "simultaneous_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "sourceleaf_discovery": DATA / "selected_heterotic_orientedphifin_sourceleaf_corpus_discovery_report.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_source_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceDomainBridge_or_SmoothEQa_Quotient_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_BRIDGE_CURRENT_SOURCE_OPEN_ORBITCLOSURE_REQUEST_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_OrbitClosure_SourceFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    branch_fill = load(INPUTS["branch_fill"])
    fill_report = load(INPUTS["fill_report"])
    embedding = load(INPUTS["embedding_values"])
    direct = load(INPUTS["directcarrier_report"])
    table = load(INPUTS["simultaneous_table"])
    discovery = load(INPUTS["sourceleaf_discovery"])

    gap = direct["constructive_attempt"]["computed_gap"]
    shadow_rows = sorted(int(row) for row in embedding["projection_pair_checks"]["row_multiplicities"])
    full_rows = list(range(table["basis_dimension"]))
    missing_rows = [row for row in full_rows if row not in shadow_rows]
    missing_oriented_rows = [entry["row"] for entry in gap["missing_positive_oriented_rows"]]

    orbit_completion_test = {
        "full_BN27_domain": {
            "basis_id": table["basis_id"],
            "basis_dimension": table["basis_dimension"],
            "all_rows_count": len(full_rows),
            "oriented_nonzero_Ctau_positive_magnitude_count": table["counts"]["oriented_nonzero_Ctau_positive_magnitude_count"],
        },
        "embedded_11_shadow": {
            "domain_label_count": len(embedding["domain_labels"]),
            "row_count": len(shadow_rows),
            "rows": shadow_rows,
            "rho_intertwines": embedding["rho_checks"]["all_labels_preserve_tau_mod3_rank_slot"],
            "projection_isometry": embedding["projection_pair_checks"]["P_transpose_P_equals_identity_11"],
        },
        "completion_gap": {
            "missing_rows_count": len(missing_rows),
            "missing_rows": missing_rows,
            "missing_positive_oriented_row_count": gap["missing_positive_oriented_row_count"],
            "missing_positive_oriented_rows": missing_oriented_rows,
            "embedded_abs_product": gap["embedded_abs_product"],
            "full_abs_sector_product": gap["full_abs_sector_product"],
            "missing_multiplier_to_full_abs_sector": gap["missing_multiplier_to_full_abs_sector"],
        },
        "verdict": "EMBEDDING_SUPPORT_INSUFFICIENT_FOR_SOURCE_BRIDGE",
    }

    required_orbitclosure = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27OrbitClosureSourceRequest.v1",
        "status": "SOURCE_ORBIT_CLOSURE_REQUIRED",
        "purpose": (
            "Promote the 11-label finite quotient shadow to the full 27-mode oriented B_N "
            "threshold source-domain only if the selected heterotic source emits Fourier-deck "
            "orbit closure, not merely the sparse phase-preserving embedding."
        ),
        "must_emit": {
            "selected_deck_action": "the F3xF3 Fourier deck action on the heterotic Qa/SU3 threshold carrier",
            "rank_slot_completion": "all rank slots r=0,1,2 are source-retained over each deck point",
            "orbit_closure_rule": "if one selected row in a deck/rank orbit is retained, the source threshold domain retains the whole selected orbit required by B_N",
            "kernel_policy": "C_tau=0 rank and PhiFin zero cluster are removed or retained exactly as in the finitepart policy before trace",
            "trace_weight_policy": "uniform trace weights on the 27-mode B_N deck, with no multiplier fitted from log(92160000)",
            "compatibility": "the existing 11-label quotient is recovered by the rho/tau shadow projection without identifying its determinant with the full orbit determinant",
            "audit_replay": "recompute 16 oriented nonzero positive rows, product 92160000, and missing multiplier 5760000 under source-selected flags",
        },
        "smooth_EQa_fallback_must_emit": {
            "selected_A_or_F_A": "smooth connection/curvature owned by the same heterotic Qa/SU3 source",
            "quotient_functor_to_BN27": "finite spectral quotient of E_Qa lands on the full oriented B_N packet",
            "finitepart_reduction": "heat/zeta/torsion finitepart reduces to log(92160000) with the same kernel policy",
        },
        "forbidden_shortcuts": [
            "promote sparse 27x11 embedding as the source-domain bridge",
            "treat Route-C 27-mode closure as heterotic source ownership without bridge",
            "fill missing multiplier 5760000 by hand",
            "select full orbit because it matches a desired threshold",
            "use observed or benchmark data",
        ],
    }
    OUTPUT_REQUEST.write_text(json.dumps(required_orbitclosure, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    direct_route = {
        "route": "BN27_orbitclosure_source_bridge",
        "closed": False,
        "support": {
            "rho_shadow_embedding_isometric": orbit_completion_test["embedded_11_shadow"]["projection_isometry"],
            "rho_shadow_preserves_rank_slot_phase": orbit_completion_test["embedded_11_shadow"]["rho_intertwines"],
            "full_BN27_table_materialized": table["basis_dimension"] == 27,
            "full_oriented_product_computed": gap["full_abs_sector_product"] == 92160000,
        },
        "missing": {
            "selected_deck_action_on_heterotic_threshold_carrier": True,
            "source_retains_full_F3xF3_rank_slot_orbit": True,
            "uniform_BN27_trace_weight_policy_source_owned": True,
            "kernel_policy_source_owned_before_finitepart": True,
        },
        "reason_open": "Current data has a faithful 11-label rho/tau shadow but not a selected orbit-closure theorem for the full BN27 threshold carrier.",
    }

    smooth_route = {
        "route": "smooth_EQa_quotient_to_BN27",
        "closed": False,
        "support": {
            "smooth_support_only_matches_found": discovery["classification"]["support_only_matches_found"],
            "smooth_selected_bundle_A_packet_found": discovery["classification"]["smooth_selected_bundle_A_packet_found"],
        },
        "missing": required_orbitclosure["smooth_EQa_fallback_must_emit"],
        "reason_open": "The smooth lane still lacks selected A/F_A or quotient-to-BN27 data.",
    }

    decision = {
        "BN27_bridge_gate_executed": True,
        "embedding_support_insufficient": True,
        "BN27_orbitclosure_source_bridge_closed": False,
        "smooth_EQa_quotient_to_BN27_closed": False,
        "orbitclosure_source_request_built": True,
        "minimal_next_leaf": "selected_BN27_orbitclosure_source_fill",
        "branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceDomainBridgeOrSmoothEQaQuotient",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "branch_fill": branch_fill["status"],
            "fill_report": fill_report["status"],
            "embedding_values": embedding["status"],
            "directcarrier_report": direct["status"],
            "sourceleaf_discovery": discovery["status"],
        },
        "orbit_completion_test": orbit_completion_test,
        "routes": {
            "BN27_orbitclosure_source_bridge": direct_route,
            "smooth_EQa_quotient_to_BN27": smooth_route,
        },
        "orbitclosure_source_request_path": rel(OUTPUT_REQUEST),
        "decision": decision,
        "theorem": {
            "name": "BN27BridgeCurrentSourceNoGoAndOrbitClosureRequestTheorem",
            "proved": True,
            "statement": (
                "The sparse 27x11 embedding faithfully preserves the finite rho/tau shadow, "
                "but it covers only 11 rows and only product 16 of the full oriented product "
                "92160000. Therefore it cannot be the selected BN27 source-domain bridge. "
                "Closure now requires an explicit source-selected Fourier-deck orbit-closure "
                "theorem, or a smooth E_Qa quotient theorem emitting the same full 27-mode "
                "oriented B_N packet."
            ),
        },
        "guardrails": {
            "does_not_promote_embedding_to_bridge": True,
            "does_not_import_routec_ownership_without_bridge": True,
            "does_not_promote_log92160000": True,
            "does_not_fill_missing_multiplier_by_hand": True,
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
        "orbitclosure_source_request_path": rel(OUTPUT_REQUEST),
        "note_path": rel(OUTPUT_NOTE),
        "BN27_bridge_gate_executed": True,
        "embedding_support_insufficient": True,
        "BN27_orbitclosure_source_bridge_closed": False,
        "smooth_EQa_quotient_to_BN27_closed": False,
        "branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceDomainBridge or SmoothEQa Quotient v1

## Result

```text
status = {STATUS}
embedding_support_insufficient = true
BN27_orbitclosure_source_bridge_closed = false
smooth_EQa_quotient_to_BN27_closed = false
branch_identity_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Gap

```text
embedded_abs_product = {gap["embedded_abs_product"]}
full_abs_sector_product = {gap["full_abs_sector_product"]}
missing_multiplier_to_full_abs_sector = {gap["missing_multiplier_to_full_abs_sector"]}
missing_positive_oriented_row_count = {gap["missing_positive_oriented_row_count"]}
```

Request:

```text
{rel(OUTPUT_REQUEST)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REQUEST)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
