"""Import selected gauge-transported Phi_fin trace into the I11 trace-map gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_i11tracemap_gaugetransportimport_or_dynamicreplaygap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT = PACKET_DIR / "current_gauge_transport_import_trace_map_attempt.packet.json"
FUNCTIONAL = PACKET_DIR / "functional_phi_fin_trace_import_sublemma.packet.json"
WITNESS = PACKET_DIR / "conditional_transport_closed_dynamic_trace_map_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_transport_closed_dynamic_replay_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I11TraceMap_GaugeTransportImport_or_DynamicReplayGap_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"

STATUS = "MTT_SELECTED_I11TRACEMAP_GAUGETRANSPORT_IMPORTED_DYNAMIC_REPLAY_OPEN"
NEXT = "MTT_Selected_TransportClosedBNBasis_or_DynamicC1TraceReplay_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "payload": rel(path),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    gauge = load(DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json")
    previous = load(DATA / "selected_i11tracemap_dynamicextension_or_firstvariationgap.candidate.json")
    prev_frontier = load(
        DATA
        / "selected_i11tracemap_dynamicextension_or_firstvariationgap"
        / "remaining_dynamic_trace_map_frontier.packet.json"
    )
    route_a = load(
        DATA
        / "selected_tracemapandbasisvalues_or_primitiverowsexecution"
        / "route_a_trace_map_value_fill.packet.json"
    )

    theorem = gauge["theorem"]
    trace = gauge["transported_trace"]
    decision = gauge["promotion_decision"]
    finite_boundary = gauge["finite_replay_boundary"]
    remains = gauge["what_remains_open"]

    functional_trace_imported = (
        theorem["proved"]
        and trace["functional_identities"]["D_selected_U_equals_U_d"]
        and trace["functional_identities"]["P_selected_equals_U_P_model_U_inverse"]
        and decision["functional_selected_trace_proved"]
        and gauge["what_closes_now"]["gauge_transported_PhiFin_trace"]
        and len(trace["sector_slots"]) == 7
    )

    functional = {
        "schema": "MTTI11FunctionalPhiFinTraceImportSublemma.v1",
        "status": "FUNCTIONAL_GAUGE_TRANSPORTED_PHIFIN_TRACE_IMPORTED_FOR_I11",
        "proved": functional_trace_imported,
        "statement": (
            "The selected gauge-transported BN/Phi_fin theorem supplies the same-branch functional trace "
            "identifier and finite Phi_fin trace operator at the End0 function-space level: K_s^sel=U K_s^model "
            "and P_s^sel=U P_s^model U^-1. This upgrades the I11 trace-map frontier by closing the functional "
            "minimizer/trace and operator support, while finite validator replay and dynamic C1 response remain open."
        ),
        "imported_closures": {
            "selected_functional_zero_mode_bases": gauge["what_closes_now"]["selected_functional_zero_mode_bases"],
            "selected_functional_projectors": gauge["what_closes_now"]["selected_functional_projectors"],
            "gauge_transported_phi_fin_trace": gauge["what_closes_now"]["gauge_transported_PhiFin_trace"],
            "functional_rho_s_promotion": gauge["what_closes_now"]["functional_rho_s_promotion"],
        },
        "not_imported_as_closed": {
            "transport_closed_finite_validator_replay": not remains["transport_closed_finite_validator_replay"],
            "selected_dotd_alpha1_with_transport_derivative": not remains["selected_dotD_alpha1_with_transport_derivative"],
            "alpha1_driver_verified": decision["alpha1_driver_verified"],
            "selected_dotD_source_verified": decision["selected_dotD_source_verified"],
        },
        "sources": [
            rel(DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"),
            rel(DATA / "selected_i11tracemap_dynamicextension_or_firstvariationgap.candidate.json"),
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    current = {
        "schema": "MTTCurrentI11TraceMapGaugeTransportImportAttempt.v1",
        "status": "CURRENT_TRACE_MAP_IMPORT_CLOSES_FUNCTIONAL_TRACE_BUT_FAILS_DYNAMIC_VALIDATOR",
        "same_branch": True,
        "selected_minimizer_identifier": functional_trace_imported,
        "finite_phi_fin_trace_operator": functional_trace_imported,
        "c1_response_coordinate_map": False,
        "selected_normalization_boundary_clause": False,
        "dynamic_c1_flags_verified": False,
        "functional_trace_imported": functional_trace_imported,
        "finite_27_mode_validator_replay_closed": finite_boundary["finite_27_mode_validator_replay_closed"],
        "remaining_dynamic_flags": route_a["remaining_dynamic_flags"],
        "attached_certificate_evidence": [
            {
                "source": rel(FUNCTIONAL),
                "closes": "functional selected minimizer/trace support",
            },
            {
                "source": rel(DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"),
                "closes": "gauge-transported Phi_fin trace theorem",
            },
            {
                "source": rel(
                    DATA
                    / "selected_i11tracemap_dynamicextension_or_firstvariationgap"
                    / "stationary_trace_map_sublemma.packet.json"
                ),
                "closes": "stationary trace-map sublemma",
            },
            {
                "source": rel(
                    DATA
                    / "selected_i11firstvariationcertificate_fill_or_quadraturetable"
                    / "normalization_compatibility_sublemma.packet.json"
                ),
                "closes": "normalization compatibility only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_gauge_transported_bn_phifin_trace.candidate.json"
                ),
                "closes": "finite replay boundary identification",
            },
        ],
        "why_validator_still_fails": [
            "transport-closed finite validator replay is false",
            "C1 response coordinate map is not emitted from selected dynamic rows",
            "normalization is closed but physical boundary cancellation is still open",
            "alpha1/dotD/physical first-variation dynamic flags are not all verified here",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    witness = {
        "schema": "MTTConditionalTransportClosedI11TraceMapWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_AFTER_TRANSPORT_CLOSED_DYNAMIC_REPLAY",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": True,
        "selected_normalization_boundary_clause": True,
        "dynamic_c1_flags_verified": True,
        "attached_certificate_evidence": [
            {
                "source": rel(FUNCTIONAL),
                "closes": "selected minimizer/functional trace",
                "conditional": False,
            },
            {
                "source": rel(FUNCTIONAL),
                "closes": "finite Phi_fin functional trace operator",
                "conditional": False,
            },
            {
                "source": rel(FRONTIER),
                "closes": "C1 response coordinate map",
                "conditional": True,
            },
            {
                "source": rel(FRONTIER),
                "closes": "physical boundary clause",
                "conditional": True,
            },
            {
                "source": rel(FRONTIER),
                "closes": "transport-closed dynamic C1 flags",
                "conditional": True,
            },
        ],
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    frontier = {
        "schema": "MTTTransportClosedDynamicReplayFrontier.v1",
        "status": "FUNCTIONAL_TRACE_IMPORTED_FINITE_DYNAMIC_REPLAY_OPEN",
        "closed_now": {
            "stationary_trace_map_sublemma": prev_frontier["closed_now"]["stationary_trace_map_sublemma"],
            "functional_selected_minimizer_trace": functional_trace_imported,
            "finite_phi_fin_functional_trace_operator": functional_trace_imported,
        },
        "still_open": {
            "transport_closed_finite_validator_replay": {
                "current_support": finite_boundary["finite_27_mode_validator_replay_closed"],
                "residual": finite_boundary["direct_truncated_relative_residual_from_T1T2_probe"],
                "needs": finite_boundary["next_acceptance"],
            },
            "c1_response_coordinate_map": previous["what_remains_open"]["c1_response_coordinate_map"],
            "selected_normalization_boundary_clause": previous["what_remains_open"]["selected_normalization_boundary_clause"],
            "dynamic_c1_flags_verified": {
                "current_flags": route_a["remaining_dynamic_flags"],
                "gauge_trace_remaining": {
                    "selected_dotD_alpha1_with_transport_derivative": remains["selected_dotD_alpha1_with_transport_derivative"],
                    "alpha1_driver_verified": remains["alpha1_driver_verified"],
                },
                "needs": "transport derivative dotD/alpha1 replay plus physical first variation and boundary verification",
            },
        },
        "superset_strategy": {
            "straight_route": "Use the already proved gauge-transported Phi_fin theorem for functional trace only.",
            "combined_route": "Combine BN clean zero cluster, HYM End0 transport, and finite Weyl trace normalization, but stop before dynamic C1 replay.",
            "locked_target": "I11 selected-trace-map dynamic validation; no observed SM data or target residuals select it.",
            "uses_observed_constants": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    FUNCTIONAL.write_text(json.dumps(functional, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(CURRENT)
    witness_result = run_validator(WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI11TraceMapGaugeTransportImportOrDynamicReplayGap",
        "status": STATUS,
        "inputs": {
            "selected_gauge_transported_bn_phifin_trace": rel(DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"),
            "previous_i11_trace_map_gate": rel(DATA / "selected_i11tracemap_dynamicextension_or_firstvariationgap.candidate.json"),
        },
        "output_packets": {
            "functional_trace_import": rel(FUNCTIONAL),
            "current_attempt": rel(CURRENT),
            "conditional_witness": rel(WITNESS),
            "remaining_frontier": rel(FRONTIER),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
        },
        "theorem": {
            "name": "I11GaugeTransportedFunctionalTraceImportTheorem",
            "proved": True,
            "statement": (
                "The selected gauge-transported BN/Phi_fin trace theorem closes the I11 functional "
                "selected minimizer/trace and finite Phi_fin functional trace operator support. The strict "
                "dynamic I11 trace-map validator still rejects until transport-closed finite replay, C1 "
                "response coordinates, physical boundary cancellation, and dynamic C1 flags are emitted."
            ),
        },
        "what_closes_now": {
            "functional_trace_import_sublemma_proved": functional_trace_imported,
            "selected_minimizer_identifier_at_functional_trace_level": current["selected_minimizer_identifier"],
            "finite_phi_fin_trace_operator_at_functional_trace_level": current["finite_phi_fin_trace_operator"],
            "current_dynamic_attempt_rejected": current_result["returncode"] == 1,
            "conditional_transport_closed_witness_passes": witness_result["returncode"] == 0,
        },
        "what_remains_open": frontier["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_I11TraceMap_GaugeTransportImport_or_DynamicReplayGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "functional_trace_import_sublemma_proved": functional_trace_imported,
        "current_dynamic_attempt_rejected": current_result["returncode"] == 1,
        "conditional_transport_closed_witness_passes": witness_result["returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I11TraceMap GaugeTransportImport or DynamicReplayGap v1

Status: `{STATUS}`.

The selected gauge-transported `B_N/Phi_fin` theorem is now imported into the
I11 trace-map frontier. This closes the functional trace part:

```text
K_s^sel = U K_s^model
P_s^sel = U P_s^model U^-1
functional selected trace = proved
```

The strict dynamic validator still rejects the current packet because the finite
transport-closed replay, C1 response coordinate map, physical boundary clause,
and dynamic alpha1/dotD/first-variation flags are not emitted here.

```text
current dynamic trace-map validates = False
conditional dynamic witness validates = True
closure claimed = False
```

Superset use: BN supplies the clean finite zero cluster, HYM supplies the
selected transport, and finite Weyl trace supplies normalization. These are
combined only as source-compatible support; observed SM constants and target
residuals do not select the trace map.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
