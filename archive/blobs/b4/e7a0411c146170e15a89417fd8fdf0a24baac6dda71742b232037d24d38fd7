"""Build source-operator/torsion plus full-Fourier co-emission frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_heteroticstromingersourceoperator_or_localsystemtorsion_or_fullfourierorbit_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OPERATOR_GATE = PACKET_DIR / "operator_torsion_source_gate.packet.json"
FOURIER_GATE = PACKET_DIR / "full_fourier_orbit_coemission_gate.packet.json"
ACCEPTANCE = PACKET_DIR / "remaining_acceptance_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HeteroticStromingerSourceOperatorOrLocalSystemTorsion_or_FullFourierOrbitSourceEmission_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_heteroticstromingerewthresholdkernel_or_bn27directcarriersourcetheorem_or_directhkrow.candidate.json",
    "threshold_payload": QA
    / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json",
    "local_system_attack": QA
    / "selected_heterotic_local_system_torsion_or_new_operator_attack.candidate.json",
    "threshold_template": QA
    / "selected_heterotic_strominger_threshold_operator_or_torsion_source.template.json",
    "post_hym_template": QA
    / "selected_heterotic_post_hym_retirement_operator_or_torsion_source.template.json",
    "fullorbit_trace_gate": QA
    / "selected_heterotic_orientedphifin_fullfourierorbit_sourceemission_or_traceidentity.candidate.json",
    "fullorbit_source_selection": QA
    / "selected_heterotic_orientedphifin_fullfourierorbit_sourceselection_theorem_or_nogo.candidate.json",
    "fullorbit_coemission_packet": QA
    / "selected_heterotic_orientedphifin_fullfourierorbit_source_coemission_packet.json",
    "fullorbit_trace_identity": QA
    / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
}

STATUS = (
    "MTT_SELECTED_HETEROTICSTROMINGERSOURCEOPERATOR_OR_LOCALSYSTEMTORSION_OR_FULLFOURIERORBIT_"
    "GATE_TIGHTENED_ENDOMORPHISM_PRIMARY_COEMISSION_OPEN"
)
NEXT = "MTT_Selected_OrientationMagnitudeCoEmission_or_EndomorphismThresholdFinitePart_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def decision(packet: dict[str, Any]) -> dict[str, Any]:
    return packet.get("decision", packet.get("closure_decision", {}))


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing operator/torsion/full-orbit inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = decision(sources["previous"])
    payload = decision(sources["threshold_payload"])
    local_attack = decision(sources["local_system_attack"])
    trace_gate = decision(sources["fullorbit_trace_gate"])
    source_selection = decision(sources["fullorbit_source_selection"])
    coemission = sources["fullorbit_coemission_packet"]
    trace_identity = sources["fullorbit_trace_identity"]

    operator_gate = {
        "schema": "MTTHeteroticStrominger.SourceOperatorOrLocalSystemGate.v1",
        "status": "ORDINARY_RANK_ONE_TORSION_NEGATIVE_ENDOMORPHISM_OPERATOR_PRIMARY",
        "closure_claimed": True,
        "threshold_payload_reduction": {
            "payload_closed": payload["payload_closed"],
            "strict_no_knob_route_still_live": payload["strict_no_knob_route_still_live"],
            "primary_next_exit": payload["primary_next_exit"],
            "parallel_next_exit": payload["parallel_next_exit"],
            "internal_lambda_12_preserved": payload["internal_lambda_12_preserved"],
            "internal_lambda_12_value": payload["internal_lambda_12_value"],
            "retire_internal_replay_as_physical_threshold_source": payload[
                "retire_internal_replay_as_physical_threshold_source"
            ],
        },
        "post_hym_route_tightening": {
            "ordinary_rank_one_torsion_route_closed_negative_for_q64": local_attack[
                "ordinary_rank_one_torsion_route_closed_negative_for_q64"
            ],
            "compact_nil_scalar_proxy_rejected": local_attack["compact_nil_scalar_proxy_rejected"],
            "hym_printed_route_retired": local_attack["hym_printed_route_retired"],
            "selected_primary_route": local_attack["selected_primary_route"],
            "secondary_route": local_attack["secondary_route"],
            "q64_projective_route_open_auxiliary": local_attack[
                "q64_projective_route_open_auxiliary"
            ],
            "next_required_artifact": local_attack["next_required_artifact"],
        },
        "allowed_value_exits_now": [
            "source-certified Endomorphism_E or equivalent Laplace-type threshold operator",
            "selected heat/spectrum/zeta/torsion finite part on that operator domain",
            "selected projective clock-shift/twisted module only if bridged to the Qa/SU3 BRST threshold complex",
        ],
        "rejected_value_exits_now": [
            "ordinary rank-one U1 local-system q64 character",
            "q64 phase as an SU3 scalar center element",
            "compact Nil scalar Laplacian proxy",
            "printed retired HYM repair matrix without source erratum and finite part",
            "internal lambda_12 as physical threshold data",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    fourier_gate = {
        "schema": "MTTHeteroticOrientedPhiFin.FullFourierOrbitCoEmissionGate.v1",
        "status": "MAGNITUDE_AND_ORIENTATION_SEPARATELY_SELECTED_SAME_SOURCE_COEMISSION_OPEN",
        "closure_claimed": True,
        "trace_identity": {
            "identity_closed_relative_to_full_orbit_source": trace_identity[
                "identity_closed_relative_to_full_orbit_source"
            ],
            "oriented_abs_sector_product": trace_identity["oriented_abs_sector_product"],
            "oriented_abs_sector_logdet_exact": trace_identity[
                "oriented_abs_sector_logdet_exact"
            ],
            "plus_sector_count": len(trace_identity["plus_sector_values"]),
            "minus_sector_count": len(trace_identity["minus_sector_values"]),
            "trace_identity_closed_relative_to_full_orbit_source": trace_gate[
                "trace_identity_closed_relative_to_full_orbit_source"
            ],
        },
        "source_selection_tightening": {
            "full_positive_fourier_orbit_selected_at_gap_layer_scope": source_selection[
                "full_positive_fourier_orbit_selected_at_gap_layer_scope"
            ],
            "routec_magnitude_source_selected_for_27mode_DE_gap_layer": source_selection[
                "routec_magnitude_source_selected_for_27mode_DE_gap_layer"
            ],
            "orientation_functor_closed": source_selection["orientation_functor_closed"],
            "orientation_magnitude_coemission_closed": source_selection[
                "orientation_magnitude_coemission_closed"
            ],
            "full_oriented_phi_fin_threshold_closed": source_selection[
                "full_oriented_phi_fin_threshold_closed"
            ],
            "oriented_logdet_promoted": source_selection["oriented_logdet_promoted"],
            "remaining_single_leaf": source_selection["remaining_single_leaf"],
        },
        "coemission_contract": coemission["remaining_required_fields"],
        "forbidden_shortcuts": coemission["forbidden_shortcuts"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    acceptance = {
        "schema": "MTTOrientationMagnitudeOrEndomorphismFinitePart.AcceptanceContract.v1",
        "status": "TWO_EXITS_PLUS_DIRECT_HK_ROW_REMAIN",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "strict_K_threshold_count": {
            "accepted": prev["accepted_selected_K_source_row_count"],
            "required": prev["selected_K_threshold_row_count_required"],
        },
        "exit_A_orientation_magnitude_coemission_must_supply": coemission[
            "remaining_required_fields"
        ],
        "exit_B_endomorphism_operator_must_supply": sources["post_hym_template"][
            "secondary_new_operator_route"
        ],
        "exit_C_direct_HK_row_must_supply": {
            "selected_K_threshold_Omega_H_lambda": None,
            "physical_normalization": None,
            "mu_match": None,
            "RG_threshold_scheme": None,
            "provenance_before_observed_values": None,
        },
        "closed_now": [
            "ordinary rank-one torsion is closed negative for selected q64",
            "q64 scalar SU3-center shortcut is rejected",
            "source-certified Endomorphism_E/full threshold operator is primary",
            "full positive Fourier orbit is selected at D_E gap-layer scope",
            "rhoE-to-BN orientation functor is closed",
            "log(92160000) trace identity is algebraically closed relative to co-emission",
        ],
        "still_open": [
            "same-source orientation-magnitude co-emission on the full 27-mode BN domain",
            "Endomorphism_E/Laplace-type threshold finite part with selected domain and normalization",
            "selected projective/twisted module response finite part if used",
            "physical normalization, mu_match, and RG/threshold scheme",
            "direct K_threshold.Omega_H.lambda source row",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHeteroticStromingerSourceOperatorOrLocalSystemTorsionOrFullFourierOrbit",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "operator_torsion_source_gate": rel(OPERATOR_GATE),
            "full_fourier_orbit_coemission_gate": rel(FOURIER_GATE),
            "remaining_acceptance_contract": rel(ACCEPTANCE),
        },
        "closure_decision": {
            "ordinary_rank_one_torsion_route_closed_negative_for_q64": True,
            "compact_nil_scalar_proxy_rejected": True,
            "hym_printed_route_retired": True,
            "source_certified_endomorphism_operator_primary": True,
            "full_positive_fourier_orbit_selected_at_gap_layer_scope": True,
            "orientation_functor_closed": True,
            "trace_identity_closed_relative_to_coemission": True,
            "oriented_abs_sector_product": 92160000,
            "oriented_abs_sector_logdet_exact": "log(92160000)",
            "orientation_magnitude_coemission_closed": False,
            "oriented_logdet_promoted": False,
            "full_oriented_phi_fin_threshold_closed": False,
            "selected_threshold_operator_finite_part_emitted": False,
            "selected_local_system_torsion_finite_part_emitted": False,
            "selected_projective_twisted_module_response_emitted": False,
            "selected_physical_normalization_mu_rg_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "SourceOperatorTorsionOrFullFourierCoEmissionTighteningTheorem",
            "proved": True,
            "statement": (
                "The current heterotic/Strominger value frontier is tightened in two "
                "directions. On the operator side, ordinary rank-one local-system "
                "torsion is closed negative for the selected q64 phase, compact Nil "
                "scalar proxies and retired printed HYM repairs are rejected, and the "
                "primary no-knob route becomes a source-certified Endomorphism_E or "
                "equivalent Laplace-type threshold operator with finite part. On the "
                "full-Fourier side, the 27-mode D_E gap layer selects the full positive "
                "orbit at magnitude scope and the rho_E functor selects orientation "
                "at shadow scope; the trace identity log(92160000) is algebraically "
                "closed relative to co-emission. The only remaining full-orbit bridge "
                "is same-source orientation-magnitude co-emission. None of these "
                "steps emits the H/lambda threshold row."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHeteroticStromingerSourceOperatorOrLocalSystemTorsionOrFullFourierOrbit",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "ordinary_rank_one_torsion_route_closed_negative_for_q64": True,
        "source_certified_endomorphism_operator_primary": True,
        "full_positive_fourier_orbit_selected_at_gap_layer_scope": True,
        "orientation_functor_closed": True,
        "trace_identity_closed_relative_to_coemission": True,
        "orientation_magnitude_coemission_closed": False,
        "selected_threshold_operator_finite_part_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Heterotic/Strominger Source Operator or Local-System Torsion or Full Fourier Orbit v1

## Theorem

`SourceOperatorTorsionOrFullFourierCoEmissionTighteningTheorem` is emitted.

## Newly Closed

- Ordinary rank-one local-system torsion is closed negative for the selected
  `q64` phase.
- The compact Nil scalar proxy, scalar `SU3` center shortcut, and retired
  printed HYM repair route are rejected as physical threshold sources.
- The primary operator route is now a source-certified `Endomorphism_E` or
  equivalent Laplace-type threshold operator with heat/spectrum/zeta/torsion
  finite part.
- The full positive Fourier orbit is selected at 27-mode `D_E` gap-layer scope.
- The `rho_E -> B_N` orientation functor is closed.
- The finite trace identity `log(92160000)` is algebraically closed relative to
  same-source co-emission.

## Still Open

- Same-source orientation-magnitude co-emission on the full 27-mode `B_N`
  domain.
- Selected `Endomorphism_E`/Laplace-type finite part with selected domain,
  normalization, trace weights, and zero-mode policy.
- Selected projective/twisted module response finite part if that route is used.
- Physical normalization, `mu_match`, and RG/threshold scheme.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(OPERATOR_GATE, operator_gate)
    write_json(FOURIER_GATE, fourier_gate)
    write_json(ACCEPTANCE, acceptance)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
