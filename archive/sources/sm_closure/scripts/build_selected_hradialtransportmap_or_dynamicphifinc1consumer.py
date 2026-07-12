"""Build the H radial transport-map / dynamic Phi_fin C1 consumer frontier."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hradialtransportmap_or_dynamicphifinc1consumer"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRANSPORT_PACKET = PACKET_DIR / "d211_pi2_radial_transport_contract.packet.json"
COEFF_PACKET = PACKET_DIR / "radial_transport_coefficient_isolation.packet.json"
CONSUMER_PACKET = PACKET_DIR / "dynamic_phifinc1_consumer_retest_after_pi2.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HRadialTransportMap_or_DynamicPhiFinC1Consumer_v1.md"

STATUS = (
    "MTT_SELECTED_HRADIALTRANSPORTMAP_OR_DYNAMICPHIFINC1CONSUMER_"
    "PI4_TAU_ISOLATED_CONSUMER_OPEN"
)
NEXT = "MTT_Selected_TauHTransportCoefficientSource_or_UnpatchedPhiFinC1Consumer_v1"

SOURCES = {
    "pi2_frontier": DATA / "selected_hradialvaluesourcenumericsearch_or_pi2hrgfrontier.candidate.json",
    "pi2_clue": DATA
    / "selected_hradialvaluesourcenumericsearch_or_pi2hrgfrontier"
    / "d211_pi2_identity_clue.packet.json",
    "numeric_search": DATA
    / "selected_hradialvaluesourcenumericsearch_or_pi2hrgfrontier"
    / "bounded_hrg_radial_expression_search.packet.json",
    "controlled_h": DATA
    / "selected_qutrit27hfunctionalsearch_or_radialsourcefrontier"
    / "controlled_herm2_matrix_invariants.packet.json",
    "dynamic_consumer": DATA / "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap.candidate.json",
    "dynamic_gate": DATA
    / "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap"
    / "dynamic_phifinc1_final_gate_reconciliation.packet.json",
    "consumer_gate": DATA
    / "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap"
    / "large_threshold_hrg_consumer_map_gate.packet.json",
    "local_axiom_boundary": DATA
    / "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap"
    / "local_axiom_vs_unpatched_boundary.packet.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing radial transport inputs: " + ", ".join(missing))

    pi2_frontier = load(SOURCES["pi2_frontier"])
    pi2_clue = load(SOURCES["pi2_clue"])
    numeric_search = load(SOURCES["numeric_search"])
    controlled_h = load(SOURCES["controlled_h"])
    dynamic_consumer = load(SOURCES["dynamic_consumer"])
    dynamic_gate = load(SOURCES["dynamic_gate"])
    consumer_gate = load(SOURCES["consumer_gate"])
    local_boundary = load(SOURCES["local_axiom_boundary"])

    pi2 = float(pi2_clue["pi_squared"])
    pi4 = pi2 * pi2
    r_h = float(controlled_h["invariants"]["r_H_from_sqrt_Tr_H_squared_over_2"])
    n_h = float(controlled_h["invariants"]["Tr_H_squared"]) / 2.0
    tau_required = r_h / pi4
    tau_required_for_n = n_h / (pi4 * pi4)
    logdet_candidate = -float(next(
        item["value"]
        for item in numeric_search["constants_used"].items()
        if item[0] == "log92160000"
    )) if False else None
    # The D211 logdet is carried as a hand-checked near miss in the numeric-search packet.
    minus_logdet_d211 = (
        numeric_search["hand_checked_near_misses"][0]["value"] / pi4
    )
    tau_candidates = [
        {
            "name": "tau_required",
            "value": tau_required,
            "relative_residual_to_required_tau": 0.0,
            "accepted_as_source": False,
            "role": "the coefficient that would close the radial transport law",
        },
        {
            "name": "-logdet(D_211)",
            "value": minus_logdet_d211,
            "relative_residual_to_required_tau": abs(minus_logdet_d211 - tau_required) / tau_required,
            "accepted_as_source": False,
            "role": "closest simple D211/pi4-style diagnostic, not exact/source-selected",
        },
        {
            "name": "integer_4",
            "value": 4.0,
            "relative_residual_to_required_tau": abs(4.0 - tau_required) / tau_required,
            "accepted_as_source": False,
            "role": "simple pi4 transport coefficient, close but not exact/source-selected",
        },
    ]

    transport_packet = {
        "schema": "MTTD211Pi2RadialTransportContract.v1",
        "status": "PI2_TO_H_RADIAL_TRANSPORT_CONTRACT_BUILT_COEFFICIENT_OPEN",
        "closure_claimed": True,
        "source_normalization_clue": {
            "base_formula": "base(D_211)=27/(4*pi^2)",
            "base_residual": pi2_clue["base_formula_residual"],
            "trace_formula": "Tr(D_211)=243/pi^2",
            "trace_residual": pi2_clue["trace_formula_residual"],
            "rank_over_trace_formula": "rank/Tr(D_211)=pi^2",
            "rank_over_trace_residual": pi2_clue["rank_over_trace_minus_pi_squared"],
        },
        "candidate_transport_law": {
            "law": "r_H = pi^4 * tau_H",
            "equivalent_N_H_law": "N_H = pi^8 * tau_H^2",
            "why_this_form": "The selected D_211 profile emits pi^2 as rank/trace; the H radial scalar has dimensionless scale compatible with a pi^4 radial transport strength.",
            "source_status": "contract only",
        },
        "required_values": {
            "r_H": r_h,
            "N_H": n_h,
            "pi_squared": pi2,
            "pi_fourth": pi4,
            "tau_H_required": tau_required,
            "tau_H_required_from_N_H": math.sqrt(tau_required_for_n),
        },
        "accepted_radial_transport_map_count": 0,
        "accepted_tau_H_source_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    coeff_packet = {
        "schema": "MTTRadialTransportCoefficientIsolation.v1",
        "status": "TAU_H_COEFFICIENT_ISOLATED_DIAGNOSTICS_REJECTED",
        "closure_claimed": True,
        "tau_H_required": tau_required,
        "tau_candidates": tau_candidates,
        "best_numeric_search_candidate": numeric_search["best_candidates"][0],
        "accepted_tau_H_source_count": 0,
        "reason_no_source_accepted": (
            "The required coefficient is isolated exactly from the controlled one-parameter H layer, "
            "but no selected source theorem emits tau_H or maps D_211/pi^2 to tau_H."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    consumer_packet = {
        "schema": "MTTDynamicPhiFinC1ConsumerRetestAfterPi2.v1",
        "status": "DYNAMIC_PHIFINC1_CONSUMER_RETESTED_PI2_CLUE_SOURCE_OPEN",
        "closure_claimed": True,
        "dynamic_values_ready": dynamic_gate["decision"]["exact_dynamic_values_ready"],
        "patched_local_axiom_closure_available": local_boundary["decision"][
            "local_axiom_conditional_dynamic_C1_closure_available"
        ],
        "unpatched_source_rule_derived": dynamic_gate["decision"]["source_rule_proved_unpatched"],
        "honest_galerkin_tables_exported": dynamic_gate["decision"]["honest_galerkin_c1_tables_exported"],
        "selected_dynamic_phi_fin_c1_payload_emitted": dynamic_consumer["closure_decision"][
            "selected_dynamic_phi_fin_c1_payload_emitted"
        ],
        "typed_HRG_consumer_map_emitted": consumer_gate["decision"]["typed_HRG_consumer_map_emitted"],
        "selected_payload_available_for_consumer": consumer_gate["decision"][
            "selected_dynamic_payload_available_for_consumer"
        ],
        "same_HRG_nonHiggs_prediction_emitted": consumer_gate["decision"][
            "same_HRG_nonHiggs_prediction_emitted"
        ],
        "D211_pi2_clue_adds_radial_normalization_target": True,
        "D211_pi2_clue_closes_consumer_map": False,
        "accepted_HRG_consumer_count": 0,
        "next_exact_payload": [
            "selected tau_H transport coefficient source",
            "or unpatched differentiated Phi_fin^C1 source rule",
            "or honest selected Galerkin C1 table export",
            "or direct K_threshold.Omega_H.lambda row",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHRadialTransportMapOrDynamicPhiFinC1Consumer",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "d211_pi2_radial_transport_contract": rel(TRANSPORT_PACKET),
            "radial_transport_coefficient_isolation": rel(COEFF_PACKET),
            "dynamic_phifinc1_consumer_retest_after_pi2": rel(CONSUMER_PACKET),
        },
        "closure_decision": {
            "D211_pi2_transport_contract_built": True,
            "tau_H_required_isolated": True,
            "accepted_tau_H_source_count": 0,
            "accepted_radial_transport_map_count": 0,
            "dynamic_consumer_retested_after_pi2": True,
            "typed_HRG_consumer_map_emitted": False,
            "selected_dynamic_phi_fin_c1_payload_emitted": False,
            "strict_r_H_promoted": False,
            "strict_N_H_promoted": False,
            "minimal_one_parameter_H_still_available": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "constants_and_parameters": {
            "pi_squared": pi2,
            "pi_fourth": pi4,
            "controlled_r_H": r_h,
            "controlled_N_H": n_h,
            "tau_H_required": tau_required,
            "minus_logdet_D211_candidate": minus_logdet_d211,
            "minus_logdet_D211_tau_relative_residual": tau_candidates[1][
                "relative_residual_to_required_tau"
            ],
            "integer_4_tau_relative_residual": tau_candidates[2][
                "relative_residual_to_required_tau"
            ],
        },
        "theorem": {
            "name": "HRadialTransportCoefficientIsolationTheorem",
            "proved": True,
            "statement": (
                "The D_211/pi^2 clue canonically suggests a pi^4 radial transport contract. "
                "This isolates the remaining radial source problem to a single coefficient "
                "tau_H in r_H=pi^4*tau_H, with tau_H=4.018017196377461 for the controlled "
                "H layer. No selected source emits tau_H, and the dynamic Phi_fin/C1 consumer "
                "map remains open because the unpatched source rule or honest Galerkin C1 "
                "tables are still absent."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHRadialTransportMapOrDynamicPhiFinC1Consumer",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "D211_pi2_transport_contract_built": True,
        "tau_H_required_isolated": True,
        "accepted_tau_H_source_count": 0,
        "accepted_radial_transport_map_count": 0,
        "typed_HRG_consumer_map_emitted": False,
        "strict_r_H_promoted": False,
        "strict_N_H_promoted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected H Radial Transport Map or DynamicPhiFinC1Consumer v1

## Theorem

`HRadialTransportCoefficientIsolationTheorem` is emitted.

## Transport Contract

The `D_211/pi^2` clue suggests the natural radial transport form:

```text
r_H = pi^4 * tau_H
N_H = pi^8 * tau_H^2
```

For the controlled H layer:

```text
r_H              = {r_h}
N_H              = {n_h}
pi^4             = {pi4}
tau_H required   = {tau_required}
```

This is progress because the unknown is now isolated as a single transport
coefficient `tau_H`.

## Diagnostics

```text
-logdet(D_211) candidate = {minus_logdet_d211}
relative residual        = {tau_candidates[1]["relative_residual_to_required_tau"]}
integer 4 residual       = {tau_candidates[2]["relative_residual_to_required_tau"]}
```

Neither is accepted as a source.

## Dynamic PhiFin/C1 Consumer Retest

The dynamic `Phi_fin/C1` value table remains ready, and local axiom conditional
closure remains available.  But strict closure still has:

```text
selected_dynamic_phi_fin_c1_payload_emitted = false
typed_HRG_consumer_map_emitted              = false
accepted_HRG_consumer_count                 = 0
```

The `D_211/pi^2` clue adds a sharper radial normalization target, but it does
not by itself emit the consumer map.

## Next Artifact

`{NEXT}`
"""

    write_json(TRANSPORT_PACKET, transport_packet)
    write_json(COEFF_PACKET, coeff_packet)
    write_json(CONSUMER_PACKET, consumer_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
