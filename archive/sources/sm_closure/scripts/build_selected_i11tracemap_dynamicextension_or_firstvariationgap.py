"""Build selected I11 trace-map dynamic extension gate or first-variation gap."""

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

SLUG = "selected_i11tracemap_dynamicextension_or_firstvariationgap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TEMPLATE = PACKET_DIR / "i11_selected_trace_map.strict_template.json"
CURRENT = PACKET_DIR / "current_trace_map_dynamic_extension_attempt.packet.json"
STATIONARY = PACKET_DIR / "stationary_trace_map_sublemma.packet.json"
WITNESS = PACKET_DIR / "conditional_dynamic_trace_map_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_dynamic_trace_map_frontier.packet.json"
PLUG = PACKET_DIR / "trace_map_field_plug_into_i11.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I11TraceMap_DynamicExtension_or_FirstVariationGap_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"

STATUS = "MTT_SELECTED_I11TRACEMAP_DYNAMICEXTENSION_BUILT_STATIONARY_TRACE_CLOSED_DYNAMIC_OPEN"
NEXT = "MTT_Selected_GaugeTransportedBNPhiFinTrace_DynamicC1Extension_v1"


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


def all_expected_sectors(trace_values: dict[str, Any]) -> bool:
    return set(trace_values) == {"Q", "u", "d", "L", "e", "N", "H"}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    route_a = load(
        DATA
        / "selected_tracemapandbasisvalues_or_primitiverowsexecution"
        / "route_a_trace_map_value_fill.packet.json"
    )
    phifin_trace = load(DATA / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json")
    i11_frontier = load(
        DATA
        / "selected_i11firstvariationcertificate_fill_or_quadraturetable"
        / "remaining_i11_first_variation_frontier.packet.json"
    )
    normalization = load(
        DATA
        / "selected_i11firstvariationcertificate_fill_or_quadraturetable"
        / "normalization_compatibility_sublemma.packet.json"
    )

    trace_values = route_a["trace_values"]
    filled_flags = route_a["filled_flags"]
    dynamic_flags = route_a["remaining_dynamic_flags"]
    stationary_closed = (
        route_a["accepted_for_stationary_trace"]
        and filled_flags["selected_trace_map_values"]
        and filled_flags["selected_projector_source_verified"]
        and filled_flags["selected_source_verified_for_functional_End0_trace"]
        and all_expected_sectors(trace_values)
        and normalization["proved"]
    )
    any_dynamic_open = any(value is False for value in dynamic_flags.values())

    template = {
        "schema": "MTTI11SelectedTraceMapStrictTemplate.v1",
        "status": "STRICT_TRACE_MAP_TEMPLATE_READY",
        "required_fields": [
            "selected_minimizer_identifier",
            "finite_phi_fin_trace_operator",
            "c1_response_coordinate_map",
            "selected_normalization_boundary_clause",
            "dynamic_c1_flags_verified",
        ],
        "field_contract": {
            "selected_minimizer_identifier": "Emit the same-branch selected minimizer or prove the transported BN trace is the selected minimizer trace.",
            "finite_phi_fin_trace_operator": "Emit finite Phi_fin trace operator on the selected transported zero-mode/projector packet.",
            "c1_response_coordinate_map": "Emit the admissible C1 response coordinates, including primitive row response slots, from selected source data.",
            "selected_normalization_boundary_clause": "Combine normalized trace compatibility with physical boundary cancellation, not merely algebraic cancellation.",
            "dynamic_c1_flags_verified": "Verify alpha1, dotD, physical first variation, finite replay, and boundary flags on the selected dynamic C1 branch.",
        },
        "validator": rel(VALIDATOR),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    stationary = {
        "schema": "MTTI11StationaryTraceMapSublemma.v1",
        "status": "STATIONARY_TRACE_MAP_VALUES_PROVED_DYNAMIC_C1_NOT_PROMOTED",
        "proved": stationary_closed,
        "statement": (
            "The stationary finite trace-map values are selected on the transported End0/projector support "
            "for sectors Q,u,d,L,e,N,H, with normalized trace compatibility. This proves the stationary "
            "trace-value sublemma only."
        ),
        "selected_sectors": sorted(trace_values),
        "filled_flags": filled_flags,
        "dynamic_flags_retained_open": dynamic_flags,
        "does_not_close": [
            "selected minimizer identifier",
            "finite Phi_fin dynamic trace operator",
            "C1 response coordinate map",
            "physical boundary cancellation",
            "I11 first-variation identity",
        ],
        "sources": [
            rel(
                DATA
                / "selected_tracemapandbasisvalues_or_primitiverowsexecution"
                / "route_a_trace_map_value_fill.packet.json"
            ),
            rel(
                DATA
                / "selected_i11firstvariationcertificate_fill_or_quadraturetable"
                / "normalization_compatibility_sublemma.packet.json"
            ),
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    current = {
        "schema": "MTTCurrentI11TraceMapDynamicExtensionAttempt.v1",
        "status": "CURRENT_TRACE_MAP_DYNAMIC_EXTENSION_FAILS_VALIDATOR",
        "same_branch": True,
        "selected_minimizer_identifier": False,
        "finite_phi_fin_trace_operator": False,
        "c1_response_coordinate_map": False,
        "selected_normalization_boundary_clause": False,
        "dynamic_c1_flags_verified": False,
        "stationary_trace_map_values_proved": stationary_closed,
        "gauge_transport_repair_required": phifin_trace["gauge_transport_repair"]["must_emit_next"],
        "remaining_dynamic_flags": dynamic_flags,
        "attached_certificate_evidence": [
            {
                "source": rel(STATIONARY),
                "closes": "stationary trace-map values only",
            },
            {
                "source": rel(DATA / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"),
                "closes": "untransported trace no-go and gauge-transport repair target",
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
                    / "selected_i11firstvariationcertificate_fill_or_quadraturetable"
                    / "remaining_i11_first_variation_frontier.packet.json"
                ),
                "closes": "frontier identification only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_tracemapandbasisvalues_or_primitiverowsexecution"
                    / "route_a_trace_map_value_fill.packet.json"
                ),
                "closes": "functional End0 trace values only",
            },
        ],
        "why_rejected": [
            "selected minimizer trace is explicitly not emitted by the untransported BN packet",
            "finite Phi_fin dynamic trace operator is a next artifact, not current source",
            "accepted_for_dynamic_C1_primitive_rows remains false",
            "normalization is closed, but the combined normalization/boundary clause needs physical boundary cancellation",
            "dynamic alpha1/dotD/first-variation/boundary flags are not all verified in this packet",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    witness = {
        "schema": "MTTConditionalI11TraceMapDynamicWitness.v1",
        "status": "CONDITIONAL_TRACE_MAP_WITNESS_VALIDATES_IF_DYNAMIC_EXTENSION_EMITS",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": True,
        "selected_normalization_boundary_clause": True,
        "dynamic_c1_flags_verified": True,
        "attached_certificate_evidence": [
            {
                "source": rel(FRONTIER),
                "closes": "selected minimizer identifier",
                "conditional": True,
            },
            {
                "source": rel(FRONTIER),
                "closes": "finite Phi_fin trace operator",
                "conditional": True,
            },
            {
                "source": rel(FRONTIER),
                "closes": "C1 response coordinate map",
                "conditional": True,
            },
            {
                "source": rel(FRONTIER),
                "closes": "selected normalization/boundary clause",
                "conditional": True,
            },
            {
                "source": rel(FRONTIER),
                "closes": "dynamic C1 flags",
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
        "schema": "MTTRemainingI11TraceMapDynamicFrontier.v1",
        "status": "STATIONARY_TRACE_MAP_CLOSED_DYNAMIC_TRACE_MAP_OPEN",
        "closed_now": {
            "stationary_trace_map_sublemma": stationary_closed,
            "finite_trace_normalization_compatibility": normalization["proved"],
        },
        "still_open": {
            "selected_minimizer_identifier": {
                "current_support": phifin_trace["promotion_decision"]["selected_minimizer_trace_emitted"],
                "needs": "selected gauge-transported BN/Phi_fin trace or replacement selected minimizer trace",
            },
            "finite_phi_fin_trace_operator": {
                "current_support": route_a["accepted_for_stationary_trace"],
                "needs": phifin_trace["next_required_artifact"],
            },
            "c1_response_coordinate_map": {
                "current_support": route_a["accepted_for_dynamic_C1_primitive_rows"],
                "needs": "selected primitive rows or finite C1 response coordinate map",
            },
            "selected_normalization_boundary_clause": {
                "normalization_closed": normalization["proved"],
                "boundary_closed": False,
                "needs": "physical boundary cancellation/no-extra-boundary source term",
            },
            "dynamic_c1_flags_verified": {
                "current_flags": dynamic_flags,
                "needs": "all dynamic flags true on the selected branch",
            },
        },
        "superset_strategy": {
            "straight_route": "stationary transported trace values are accepted as a strict sublemma",
            "combined_route": "BN finite model-active support plus HYM selected transport points to the dynamic repair target",
            "locked_target": "I11 selected-trace-map field only; first-variation, Hessian, and boundary fields remain separate",
            "uses_observed_constants": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    STATIONARY.write_text(json.dumps(stationary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(CURRENT)
    witness_result = run_validator(WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    plug = {
        "schema": "MTTI11TraceMapFieldPlugIntoCertificate.v1",
        "status": "TRACE_MAP_FIELD_CONDITIONAL_PLUG_READY_I11_STILL_OPEN",
        "conditional_trace_map_witness": rel(WITNESS),
        "trace_map_validator_returncode": witness_result["returncode"],
        "would_close_i11_field": "selected_trace_map",
        "does_not_close_i11_fields": [
            "first_variation_identity",
            "hessian_or_coercivity",
            "boundary_cancellation",
        ],
        "i11_frontier_reference": rel(
            DATA
            / "selected_i11firstvariationcertificate_fill_or_quadraturetable"
            / "remaining_i11_first_variation_frontier.packet.json"
        ),
        "current_i11_still_open": list(i11_frontier["still_open"].keys()),
        "closure_claimed": False,
    }
    PLUG.write_text(json.dumps(plug, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI11TraceMapDynamicExtensionOrFirstVariationGap",
        "status": STATUS,
        "inputs": {
            "route_a_trace_map_value_fill": rel(
                DATA
                / "selected_tracemapandbasisvalues_or_primitiverowsexecution"
                / "route_a_trace_map_value_fill.packet.json"
            ),
            "phifin_bn_modelactive_no_go": rel(DATA / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"),
            "i11_frontier": rel(
                DATA
                / "selected_i11firstvariationcertificate_fill_or_quadraturetable"
                / "remaining_i11_first_variation_frontier.packet.json"
            ),
        },
        "output_packets": {
            "strict_template": rel(TEMPLATE),
            "stationary_trace_map_sublemma": rel(STATIONARY),
            "current_attempt": rel(CURRENT),
            "conditional_trace_map_witness": rel(WITNESS),
            "remaining_dynamic_frontier": rel(FRONTIER),
            "trace_map_field_plug": rel(PLUG),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
        },
        "theorem": {
            "name": "I11StationaryTraceMapAndDynamicExtensionFrontierTheorem",
            "proved": True,
            "statement": (
                "The selected stationary finite trace-map values are closed for the transported End0/projector "
                "support and normalized trace pairing. The dynamic I11 trace-map field remains open until the "
                "same branch emits the selected minimizer identifier, finite Phi_fin trace operator, C1 response "
                "coordinate map, physical boundary clause, and dynamic C1 verification flags."
            ),
        },
        "what_closes_now": {
            "trace_map_validator_built": True,
            "stationary_trace_map_sublemma_proved": stationary_closed,
            "current_dynamic_attempt_rejected": current_result["returncode"] == 1,
            "conditional_dynamic_witness_passes": witness_result["returncode"] == 0,
            "dynamic_flags_remain_open": any_dynamic_open,
        },
        "what_remains_open": frontier["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_I11TraceMap_DynamicExtension_or_FirstVariationGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "stationary_trace_map_sublemma_proved": stationary_closed,
        "current_dynamic_attempt_rejected": current_result["returncode"] == 1,
        "conditional_dynamic_witness_passes": witness_result["returncode"] == 0,
        "trace_map_field_plug_ready": plug["trace_map_validator_returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I11TraceMap DynamicExtension or FirstVariationGap v1

Status: `{STATUS}`.

This gate promotes exactly one honest subresult: the stationary trace-map values
are selected on the transported End0/projector support and compatible with the
finite normalized trace. It does not promote the dynamic I11 trace map.

```text
stationary trace-map sublemma proved = {stationary_closed}
current dynamic trace-map validates  = False
conditional trace-map validates      = True
closure claimed                      = False
```

The superset strategy is used in a constrained way: finite BN support and HYM
transport identify the dynamic repair target, while the stationary End0 trace
values are kept as a strict sublemma. The locked target is only the I11
selected-trace-map field. First variation, Hessian/coercivity, and physical
boundary cancellation remain separate I11 proof obligations.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
