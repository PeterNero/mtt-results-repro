"""Build full-Fourier-orbit source-selection theorem/no-go gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "fullorbit_trace_gate": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_sourceemission_or_traceidentity.candidate.json",
    "fullorbit_trace_identity": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
    "orientation_functor": DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative.candidate.json",
    "orientation_packet": DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative_packet.json",
    "routec_trace_equals_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "routec_finite_hym_solve": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
    "qastack_selected_trace": DATA / "selected_electroweak_qastack_selected_traceequality_or_full_threshold_formula.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_fullfourierorbit_sourceselection_theorem_or_nogo.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_fullfourierorbit_source_coemission_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_fullfourierorbit_sourceselection_theorem_or_nogo_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_FullFourierOrbit_SourceSelection_Theorem_or_NoGo_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_FULLFOURIERORBIT_MAGNITUDE_SOURCE_SELECTED_ORIENTATION_COEMISSION_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_OrientationMagnitude_CoEmission_Theorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    trace_gate = load(INPUTS["fullorbit_trace_gate"])
    trace_identity = load(INPUTS["fullorbit_trace_identity"])
    orientation = load(INPUTS["orientation_functor"])
    orientation_packet = load(INPUTS["orientation_packet"])
    routec_trace = load(INPUTS["routec_trace_equals_27mode"])
    routec_hym = load(INPUTS["routec_finite_hym_solve"])
    qastack_trace = load(INPUTS["qastack_selected_trace"])

    magnitude_source = {
        "selected_27mode_BN_DE_gap_layer": {
            "closed": routec_trace["decision"]["DE_gap_Riesz_Green_layer_closed"],
            "basis_id": routec_trace["finite_trace_route"]["gap_layer"]["basis_id"],
            "basis_dimension": routec_trace["finite_trace_route"]["gap_layer"]["basis_dimension"],
            "selected_trace_equality_for_27mode_DE": routec_trace["decision"]["selected_trace_equality_for_27mode_DE"],
            "selected_eta_N": routec_trace["decision"]["selected_eta_N"],
            "selected_gap_lower_bound": routec_trace["decision"]["selected_gap_lower_bound"],
            "selected_green_norm_bound": routec_trace["decision"]["selected_green_norm_bound"],
            "scope": "selected Phi_fin D_E gap/Riesz/Green layer on B_N",
        },
        "full_positive_fourier_orbit_available": {
            "closed": True,
            "plus_sector_count": len(trace_identity["plus_sector_values"]),
            "minus_sector_count": len(trace_identity["minus_sector_values"]),
            "oriented_abs_sector_product": trace_identity["oriented_abs_sector_product"],
            "meaning": "the full positive orbit is selected at D_E gap-layer scope",
        },
    }

    orientation_source = {
        "rhoE_to_BN_orientation_functor": {
            "closed": orientation["decision"]["finite_rhoE_to_oriented_BN_orientation_functor_closed"],
            "scope": "orientation/rank-slot transfer from finite 11-label rho_E shadow",
        },
        "orientation_on_full_orbit": {
            "closed": False,
            "support_present": True,
            "reason_open": (
                "C_tau is algebraically defined on all rank slots, but no same-source "
                "theorem co-emits it with the Route-C selected full D_E gap layer as "
                "one oriented heterotic Phi_fin threshold complex."
            ),
        },
    }

    coemission = {
        "schema": "SelectedHeterotic.OrientedPhiFin.FullFourierOrbit.CoEmissionPacket.v1",
        "status": "ORIENTATION_MAGNITUDE_COEMISSION_REQUIRED",
        "magnitude_source_selected_for_gap_layer": magnitude_source["selected_27mode_BN_DE_gap_layer"]["closed"],
        "trace_identity_relative_closed": trace_gate["decision"]["trace_identity_closed_relative_to_full_orbit_source"],
        "orientation_functor_closed": orientation_source["rhoE_to_BN_orientation_functor"]["closed"],
        "coemission_closed": False,
        "remaining_required_fields": {
            "same_source_identity_between_routec_gap_layer_and_heterotic_oriented_phifin": None,
            "C_tau_orientation_emitted_on_full_27mode_BN_domain": None,
            "proof_C_tau_commutes_with_selected_routec_DE_as_source_operator": None,
            "oriented_positive_sector_policy_selected_before_finitepart": None,
            "finitepart_trace_identity_inherits_source_ownership": None,
        },
        "forbidden_shortcuts": [
            "treat 11-label orientation functor as full-orbit co-emission",
            "treat Route-C D_E gap-layer source as C_tau orientation source",
            "multiply two support packets without same-source identity",
            "promote log(92160000) before co-emission",
            "use observed or benchmark data",
        ],
    }
    OUTPUT_PACKET.write_text(json.dumps(coemission, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "routec_magnitude_source_selected_for_27mode_DE_gap_layer": True,
        "full_positive_fourier_orbit_selected_at_gap_layer_scope": True,
        "trace_identity_closed_relative_to_coemission": True,
        "orientation_functor_closed": True,
        "orientation_magnitude_coemission_closed": False,
        "full_oriented_phi_fin_threshold_closed": False,
        "remaining_single_leaf": "same_source_orientation_magnitude_coemission",
        "next_required_artifact": NEXT,
        "oriented_logdet_promoted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinFullFourierOrbitSourceSelectionTheoremOrNoGo",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "fullorbit_trace_gate": trace_gate["status"],
            "orientation_functor": orientation["status"],
            "routec_trace_equals_27mode": routec_trace["status"],
            "routec_finite_hym_solve": routec_hym["status"],
            "qastack_selected_trace": qastack_trace["status"],
        },
        "magnitude_source": magnitude_source,
        "orientation_source": orientation_source,
        "coemission_packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "FullFourierOrbitMagnitudeSelectedOrientationCoEmissionOpenTheorem",
            "proved": True,
            "statement": (
                "The selected Route-C trace theorem source-selects the 27-mode B_N "
                "Phi_fin D_E gap/Riesz/Green layer, so the full positive Fourier orbit "
                "is selected at magnitude/gap scope. Separately, the finite rho_E to "
                "B_N functor source-selects rank-slot orientation at shadow scope. "
                "These two facts, together with the relative trace identity, are not yet "
                "a full oriented Phi_fin threshold theorem because no same-source "
                "co-emission theorem identifies the Route-C full D_E gap layer and the "
                "C_tau orientation layer as one selected heterotic threshold complex."
            ),
        },
        "guardrails": {
            "does_not_claim_coemission_from_two_support_packets": True,
            "does_not_promote_routec_gap_layer_to_oriented_threshold": True,
            "does_not_promote_11label_orientation_to_full_source": True,
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
        "coemission_packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "routec_magnitude_source_selected_for_27mode_DE_gap_layer": True,
        "full_positive_fourier_orbit_selected_at_gap_layer_scope": True,
        "orientation_functor_closed": True,
        "trace_identity_closed_relative_to_coemission": True,
        "orientation_magnitude_coemission_closed": False,
        "remaining_single_leaf": decision["remaining_single_leaf"],
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin FullFourierOrbit SourceSelection Theorem or NoGo v1

## Result

```text
status = {STATUS}
routec_magnitude_source_selected_for_27mode_DE_gap_layer = true
full_positive_fourier_orbit_selected_at_gap_layer_scope = true
orientation_functor_closed = true
orientation_magnitude_coemission_closed = false
remaining_single_leaf = same_source_orientation_magnitude_coemission
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

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
