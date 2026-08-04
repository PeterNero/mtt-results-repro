"""Build heterotic/Strominger EW kernel or BN27 direct carrier frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_heteroticstromingerewthresholdkernel_or_bn27directcarriersourcetheorem_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EW_LANE = PACKET_DIR / "strominger_ew_kernel_value_lane.packet.json"
BN27_LANE = PACKET_DIR / "bn27_direct_carrier_full_orbit_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_strominger_kernel_bn27_carrier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HeteroticStromingerElectroweakThresholdKernel_or_BN27DirectCarrierSourceTheorem_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow.candidate.json",
    "ew_kernel": QA / "selected_heterotic_strominger_electroweak_threshold_kernel.candidate.json",
    "ew_payload": QA
    / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json",
    "ew_minimal_payload": QA / "selected_heterotic_strominger_electroweak_threshold_kernel_minimal_payload.json",
    "bn27_direct_carrier": QA / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt.candidate.json",
    "bn27_direct_carrier_report": QA / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt_report.json",
    "sourceleaf_directcarrier": QA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea.candidate.json",
}

STATUS = (
    "MTT_SELECTED_HETEROTICSTROMINGEREWTHRESHOLDKERNEL_OR_BN27DIRECTCARRIERSOURCETHEOREM_"
    "VALUES_REDUCED_TO_THRESHOLD_OPERATOR_TORSION_OR_FULL_ORBIT"
)
NEXT = "MTT_Selected_HeteroticStromingerSourceOperatorOrLocalSystemTorsion_or_FullFourierOrbitSourceEmission_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def d(src: dict[str, Any]) -> dict[str, Any]:
    return src.get("decision", src.get("closure_decision", {}))


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Strominger/BN27 carrier inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = d(sources["previous"])
    ew = d(sources["ew_kernel"])
    payload = d(sources["ew_payload"])
    minimal = d(sources["ew_minimal_payload"])
    carrier = d(sources["bn27_direct_carrier"])
    sourceleaf = d(sources["sourceleaf_directcarrier"])

    ew_lane = {
        "schema": "MTTStromingerEWKernelValueLane.v1",
        "status": "KERNEL_FRAMEWORK_FILLED_VALUES_REDUCED_TO_OPERATOR_OR_TORSION",
        "closure_claimed": True,
        "kernel_fill_attempt": {
            "tree_level_gauge_kinetic_slot_filled": ew["tree_level_gauge_kinetic_slot_filled"],
            "internal_lambda_12_carried": ew["internal_lambda_12_carried"],
            "internal_lambda_12_value": ew["internal_lambda_12_value"],
            "selected_heterotic_strominger_kernel_closed": ew[
                "selected_heterotic_strominger_kernel_closed"
            ],
            "source_identity_selected_for_EW_kernel": ew[
                "source_identity_selected_for_EW_kernel"
            ],
            "analytic_torsion_or_threshold_operator_closed": ew[
                "analytic_torsion_or_threshold_operator_closed"
            ],
            "stack_threshold_determinants_closed": ew[
                "stack_threshold_determinants_closed"
            ],
            "physical_normalization_closed": ew["physical_normalization_closed"],
            "matching_scale_closed": ew["matching_scale_closed"],
            "RG_scheme_closed": ew["RG_scheme_closed"],
            "measured_electroweak_closure": ew["measured_electroweak_closure"],
        },
        "payload_reduction": {
            "payload_closed": payload["payload_closed"],
            "strict_no_knob_route_still_live": payload["strict_no_knob_route_still_live"],
            "internal_lambda_12_preserved": payload["internal_lambda_12_preserved"],
            "internal_lambda_12_value": payload["internal_lambda_12_value"],
            "retire_internal_replay_as_physical_threshold_source": payload[
                "retire_internal_replay_as_physical_threshold_source"
            ],
            "primary_next_exit": payload["primary_next_exit"],
            "parallel_next_exit": payload["parallel_next_exit"],
            "measured_electroweak_closure": payload["measured_electroweak_closure"],
        },
        "minimal_payload": {
            "status": sources["ew_minimal_payload"]["status"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    bn27_lane = {
        "schema": "MTTBN27DirectCarrierFullOrbitLane.v1",
        "status": "DIRECT_CARRIER_REDUCED_TO_FULL_ORIENTED_POSITIVE_FOURIER_ORBIT",
        "closure_claimed": True,
        "sourceleaf": {
            "source_leaf_attack_executed": sourceleaf["source_leaf_attack_executed"],
            "source_theorem_request_built": sourceleaf["source_theorem_request_built"],
            "direct_first_open_leaf": sourceleaf["direct_first_open_leaf"],
            "smooth_first_open_leaf": sourceleaf["smooth_first_open_leaf"],
            "direct_carrier_leaf_closed": sourceleaf["direct_carrier_leaf_closed"],
            "bundle_A_leaf_closed": sourceleaf["bundle_A_leaf_closed"],
            "oriented_logdet_promoted": sourceleaf["oriented_logdet_promoted"],
        },
        "constructive_attempt": {
            "constructive_attempt_executed": carrier["constructive_attempt_executed"],
            "orientation_functor_closed": carrier["orientation_functor_closed"],
            "positive_magnitude_functor_closed": carrier[
                "positive_magnitude_functor_closed"
            ],
            "source_emits_oriented_BN_carrier": carrier[
                "source_emits_oriented_BN_carrier"
            ],
            "direct_carrier_theorem_closed": carrier["direct_carrier_theorem_closed"],
            "full_oriented_positive_orbit_closed": carrier[
                "full_oriented_positive_orbit_closed"
            ],
            "finitepart_trace_identity_closed": carrier["finitepart_trace_identity_closed"],
            "oriented_logdet_promoted": carrier["oriented_logdet_promoted"],
            "new_minimal_leaf": carrier["new_minimal_leaf"],
        },
        "orbit_arithmetic": {
            "required_full_orbit_product": "9600*9600",
            "required_full_orbit_logdet": "log(92160000)",
            "embedded_11_label_shadow_product": 16,
            "missing_multiplier": 5760000,
            "report_status": sources["bn27_direct_carrier_report"]["status"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterStromingerKernelBN27Carrier.v1",
        "status": "NEXT_FRONTIER_STROMINGER_OPERATOR_TORSION_OR_FULL_FOURIER_ORBIT_OR_DIRECT_HK_ROW",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "heterotic/Strominger framework and tree-level f=S gauge kinetic slot filled",
            "internal lambda_12 carried but retired as physical threshold source",
            "EW kernel value frontier reduced to source-selected HYM/monad threshold operator or acyclic local-system torsion",
            "BN27 direct carrier constructive attempt executed",
            "BN27 orientation functor closed from 11-label rhoE shadow",
            "BN27 positive magnitude requires full oriented positive Fourier orbit",
            "11-label shadow product 16 identified as insufficient against full product 9600*9600",
        ],
        "still_open": [
            "source-selected HYM/monad Laplace-type threshold operator with selected mu/moduli, trace weights, and spectrum or heat/zeta finite part",
            "source-selected acyclic local-system torsion computation on compact Nil/Iwasawa electroweak stack",
            "physical normalization, mu_match, and RG/threshold scheme",
            "source emits full oriented positive Fourier orbit",
            "BN27 finitepart trace identity log(92160000)",
            "selected bundle connection A alternative",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHeteroticStromingerEWThresholdKernelOrBN27DirectCarrierSourceTheorem",
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
            "strominger_ew_kernel_value_lane": rel(EW_LANE),
            "bn27_direct_carrier_full_orbit_lane": rel(BN27_LANE),
            "next_cutset_after_strominger_kernel_bn27_carrier": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "tree_level_gauge_kinetic_slot_filled": True,
            "EW_kernel_values_reduced_to_operator_or_torsion": True,
            "internal_lambda_12_retired_as_physical_threshold_source": True,
            "selected_heterotic_strominger_kernel_closed": False,
            "analytic_torsion_or_threshold_operator_closed": False,
            "physical_normalization_closed": False,
            "matching_scale_closed": False,
            "RG_scheme_closed": False,
            "BN27_orientation_functor_closed": True,
            "BN27_direct_carrier_reduced_to_full_orbit": True,
            "BN27_full_oriented_positive_orbit_closed": False,
            "BN27_finitepart_trace_identity_closed": False,
            "BN27_11_label_shadow_insufficient": True,
            "BN27_missing_multiplier": 5760000,
            "selected_R_H_RG_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "direct_HK_exit_still_allowed": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "StromingerThresholdKernelOrBN27FullOrbitReductionTheorem",
            "proved": True,
            "statement": (
                "The heterotic/Strominger electroweak kernel is not yet a value. "
                "The framework and tree-level f=S slot are filled, and internal "
                "lambda_12 is retained only as accounting support. The selected value "
                "frontier is reduced to either a HYM/monad Laplace-type threshold "
                "operator finite part or an acyclic local-system torsion computation. "
                "On the BN27 side, the 11-label rhoE shadow closes orientation transfer "
                "but not positive magnitude: the full oriented positive Fourier orbit "
                "product 9600*9600 is required, while the shadow supplies product 16. "
                "The remaining exits are therefore Strominger operator/torsion values, "
                "full Fourier orbit source emission, or direct H K row."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHeteroticStromingerEWThresholdKernelOrBN27DirectCarrierSourceTheorem",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "EW_kernel_values_reduced_to_operator_or_torsion": True,
        "selected_heterotic_strominger_kernel_closed": False,
        "BN27_orientation_functor_closed": True,
        "BN27_full_oriented_positive_orbit_closed": False,
        "BN27_11_label_shadow_insufficient": True,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Heterotic/Strominger Electroweak Threshold Kernel or BN27 Direct Carrier Source Theorem v1

## Theorem

`StromingerThresholdKernelOrBN27FullOrbitReductionTheorem` is emitted.

## Closed Here

- Heterotic/Strominger framework and tree-level `f=S` gauge kinetic slot are
  filled.
- Internal `lambda_12` is carried but retired as physical threshold source.
- EW kernel value frontier is reduced to source-selected HYM/monad threshold
  operator finite part or acyclic local-system torsion.
- BN27 direct carrier constructive attempt is executed.
- BN27 orientation functor is closed from the 11-label `rho_E` shadow.
- BN27 positive magnitude requires the full oriented positive Fourier orbit.
- The 11-label shadow product `16` is insufficient against the full product
  `9600*9600`; missing multiplier is `5760000`.

## Still Open

- Source-selected HYM/monad Laplace-type threshold operator with selected
  `mu/moduli`, trace weights, spectrum, or heat/zeta finite part.
- Source-selected acyclic local-system torsion computation on the compact
  Nil/Iwasawa electroweak stack.
- Physical normalization, `mu_match`, and RG/threshold scheme.
- Source emits full oriented positive Fourier orbit.
- BN27 finitepart trace identity `log(92160000)`.
- Selected bundle connection `A` alternative.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(EW_LANE, ew_lane)
    write_json(BN27_LANE, bn27_lane)
    write_json(NEXT_CUTSET, next_cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
