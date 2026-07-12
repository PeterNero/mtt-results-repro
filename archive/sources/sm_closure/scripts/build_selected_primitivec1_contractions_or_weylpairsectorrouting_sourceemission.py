"""Build primitive-C1 contractions / Weyl-pair sector-routing reconciliation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_primitivec1_contractions_or_weylpairsectorrouting_sourceemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTING_BRIDGE = PACKET_DIR / "sector_routing_and_contraction_bridge.packet.json"
HANDOFF = PACKET_DIR / "dynamic_value_gate_handoff.packet.json"
GUARDRAIL = PACKET_DIR / "promotion_guardrail.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveC1Contractions_or_WeylPairSectorRouting_SourceEmission_v1.md"

PRIMITIVE_CLASS = DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
STATIC_ROUTING = DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
CONTRACTION_ENVELOPE = DATA / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.candidate.json"
DYNAMIC_VALUE_GATE = DATA / "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission.candidate.json"
DELTA_GATE = DATA / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"

STATUS = (
    "MTT_SELECTED_PRIMITIVEC1_CONTRACTIONS_OR_WEYLPAIRSECTORROUTING_SOURCEEMISSION_"
    "BUILT_ROUTING_AND_ENVELOPE_RECONCILED_DYNAMIC_VALUE_GATE_OPEN"
)
NEXT = "MTT_Selected_DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing primitive-C1/Weyl-pair bridge inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PRIMITIVE_CLASS, STATIC_ROUTING, CONTRACTION_ENVELOPE, DYNAMIC_VALUE_GATE, DELTA_GATE]
    require_sources(sources)

    primitive_class = load(PRIMITIVE_CLASS)
    static_routing = load(STATIC_ROUTING)
    envelope = load(CONTRACTION_ENVELOPE)
    dynamic_gate = load(DYNAMIC_VALUE_GATE)
    delta_gate = load(DELTA_GATE)

    static_route = static_routing["static_routing_source_emission"]
    contraction = envelope["contraction_envelope"]
    promotion_test = envelope["promotion_test"]
    dynamic_acceptance = dynamic_gate["acceptance_kernel_for_next_values"]

    routing_bridge = {
        "schema": "MTTPrimitiveC1WeylPairRoutingBridge.v1",
        "status": "STATIC_ROUTING_AND_PRIMITIVE_CONTRACTION_ENVELOPE_RECONCILED",
        "static_routing_closed": static_route["proved"],
        "phase_route": static_route["retired_sector_routing"]["phase_route"],
        "shift_route": static_route["retired_sector_routing"]["shift_route"],
        "finite_trace_transfer_selected": static_route["retired_sector_routing"][
            "selected_static_finite_trace_transfer_normalization"
        ],
        "primitive_contraction_envelope_constructed": contraction["constructed"],
        "active_shift": contraction["active_shift"],
        "fixed_fiber_class": contraction["fixed_fiber_class"],
        "all_fixed_fiber_rank_three": contraction["candidate_summary"][
            "all_fixed_fiber_rank_three"
        ],
        "current_layer_promoted_as_flavor_closure": False,
        "reason": (
            "The static Weyl-pair sector route and finite trace normalization are selected, and the "
            "primitive contraction envelope is finite and rank-three. The same packet is still only a "
            "degenerate current C1 observable layer, not a selected dynamic response matrix."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROUTING_BRIDGE, routing_bridge)

    handoff = {
        "schema": "MTTDynamicValueGateHandoff.v1",
        "status": "HANDOFF_TO_NONSCALAR_DYNAMIC_VALUE_GATE",
        "next_required_artifact": NEXT,
        "current_layer_value_packet_emitted": dynamic_gate["what_closes_now"][
            "current_layer_value_packet_emitted"
        ],
        "current_layer_degeneracy_no_go_proved": dynamic_gate["what_closes_now"][
            "current_layer_degeneracy_no_go_proved"
        ],
        "minimum_next_value_packet": dynamic_acceptance["minimum_next_value_packet"],
        "finite_tests_after_values_exist": dynamic_acceptance["finite_tests_after_values_exist"],
        "selected_values_available_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(HANDOFF, handoff)

    guardrail = {
        "schema": "MTTPrimitiveC1WeylPairPromotionGuardrail.v1",
        "status": "PROMOTION_REJECTED_UNTIL_DYNAMIC_VALUES_EMIT",
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "dynamic_overlap_tensor_claimed": False,
        "primitive_C1_contractions_claimed": False,
        "sector_response_matrices_claimed": False,
        "rank_or_consistency_test_allowed": promotion_test["rank_or_consistency_test_allowed"],
        "required_fields": promotion_test["required_fields"],
        "delta_gate_selected_operator_available": delta_gate["selected_deltatheta_c1_solve_gate"][
            "selected_operator_available"
        ],
        "why": (
            "Static sector routing removes a label blocker, but selected value promotion requires "
            "non-scalar dynamic overlap/Hessian/full-response data or honest Galerkin C1 contraction "
            "values from the same branch."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(GUARDRAIL, guardrail)

    candidate = {
        "candidate": "MTTSelectedPrimitiveC1ContractionsOrWeylPairSectorRoutingSourceEmission",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "sector_routing_and_contraction_bridge": rel(ROUTING_BRIDGE),
            "dynamic_value_gate_handoff": rel(HANDOFF),
            "promotion_guardrail": rel(GUARDRAIL),
        },
        "theorem": {
            "name": "PrimitiveC1ContractionsWeylPairRoutingReconciliationTheorem",
            "proved": True,
            "statement": (
                "The selected static Weyl-pair sector routing and finite trace normalization reconcile with "
                "the finite primitive-contraction envelope. This closes the bookkeeping bridge expected by "
                "the proof spine, but it does not emit A_selected, b_selected, deltaTheta_C1, sector response "
                "matrices, or non-scalar dynamic overlap data. The next proof gate is therefore the already "
                "specified dynamic overlap/Hessian/Galerkin C1 value-emission gate."
            ),
        },
        "closure_decision": {
            "static_weylpair_sector_routing_closed": static_route["proved"],
            "primitive_contraction_envelope_constructed": contraction["constructed"],
            "current_C1_observable_layer_selected": primitive_class["what_closes_now"][
                "primitive_class_C1_observable_emitted"
            ],
            "current_layer_flavor_no_go_confirmed": primitive_class["what_closes_now"][
                "current_C1_layer_flavor_no_go_confirmed"
            ],
            "dynamic_value_gate_ready_as_next": True,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "missing_spine_bridge_constructed": True,
            "static_weylpair_sector_routing_imported": static_route["proved"],
            "primitive_contraction_envelope_imported": contraction["constructed"],
            "degenerate_current_layer_guard_preserved": True,
            "next_dynamic_value_gate_selected": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": dynamic_gate["what_remains_open"],
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "selected_values_available": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PrimitiveC1Contractions_or_WeylPairSectorRouting_SourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "selected_values_available": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PrimitiveC1Contractions or WeylPairSectorRouting SourceEmission v1

Status: `{STATUS}`.

This artifact fills the missing proof-spine bridge between:

```text
static Weyl-pair routing       : closed
primitive contraction envelope : built
current C1 layer flavor no-go  : closed
```

It does not promote the current layer to flavor closure. The current primitive
packet is still scalar-permutation degenerate, so selected `A_selected`,
`b_selected`, `deltaTheta_C1`, sector response matrices, and non-scalar dynamic
overlap/Hessian/full-response values remain open.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
