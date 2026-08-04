from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
SLUG = "selected_fluxthresholdaxioncurrentanomalymatchingmap"
STATUS = (
    "MTT_U6_THRESHOLD_ONLY_EXOTIC_DECOUPLING_REJECTED_BY_ANOMALY_MATCHING_"
    "GREEN_SCHWARZ_4D_AXION_CURRENT_CONTRACT_SHARPENED"
)
NEXT = "MTT_Selected_4DGreenSchwarzAxionReductionAndSurvivingCurrent_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FluxThresholdAxionCurrentAnomalyMatchingMap_v1.md"

MATCHING = OUT / "E6_Qpsi_UV_IR_anomaly_matching_and_threshold_no_go.packet.json"
GS = OUT / "selected_green_schwarz_support_vs_4D_axion_source.packet.json"
MAP = OUT / "lawful_surviving_axion_current_map_contract.packet.json"
FRONTIER = OUT / "U6_frontier_after_A96.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "A95_plan": ROOT / "candidate_data" / "selected_postu5tierledger_and_u9globalbranchmeasure" / "next_execution_plan_after_U5_U9_tier_closure.packet.json",
        "E6_anomaly": ROOT / "candidate_data" / "selected_e6centralgeneratorqcdanomalyaudit.candidate.json",
        "strong_CP_cutset": ROOT / "candidate_data" / "selected_neutrinoandstrongcp_strictupgradeattack" / "strong_cp_central_charge_anomaly_cutset.packet.json",
        "q79_GS_curvature": Q79 / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json",
        "q79_flat_gerbe": Q79 / "candidate_data" / "time_oriented_m1_flat_gerbe_promotion.candidate.json",
        "q79_charge_sector": Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A96 authority: " + ", ".join(missing))

    plan = load(paths["A95_plan"])
    e6 = load(paths["E6_anomaly"])
    cp = load(paths["strong_CP_cutset"])
    gs = load(paths["q79_GS_curvature"])
    flat = load(paths["q79_flat_gerbe"])
    charge = load(paths["q79_charge_sector"])

    anomaly = e6["colored_anomaly_trace"]
    a_light = int(anomaly["matter_anomaly_total"])
    a_heavy = int(anomaly["exotic_anomaly_total_for_three_27s"])
    a_uv = int(anomaly["complete_three_27_anomaly"])
    matching = {
        "schema": "MTTE6QpsiUVIRAnomalyMatchingAndThresholdNoGo.v1",
        "status": "SYMMETRY_PRESERVING_HEAVY_THRESHOLD_CANNOT_CREATE_A_QCD_ANOMALY_FROM_ANOMALY_FREE_QPSI",
        "UV_trace": {
            "light_16_1_contribution": a_light,
            "heavy_10_minus2_contribution": a_heavy,
            "complete_three_27_Qpsi_anomaly": a_uv,
        },
        "symmetry_preserving_exotic_mass": {
            "representative_operator": "1_4 * 10_-2 * 10_-2",
            "Qpsi_charge_sum": 4 - 2 - 2,
            "preserves_Qpsi": True,
        },
        "IR_matching": {
            "light_fermion_measure_anomaly": a_light,
            "heavy_threshold_Wess_Zumino_coefficient": a_heavy,
            "matched_total": a_light + a_heavy,
            "threshold_removes_heavy_particles_but_not_their_anomaly": True,
            "matter_only_trace_is_full_IR_anomaly": False,
        },
        "lawful_exits": [
            "select a surviving current that is not pure anomaly-free Qpsi",
            "project to an incomplete chiral spectrum together with the required Green-Schwarz/Wess-Zumino inflow",
            "derive a four-dimensional Green-Schwarz axion whose shift and G tilde G coefficient are computed from the selected compactification",
        ],
        "primary_references": [
            "https://arxiv.org/abs/hep-th/9311038",
            "https://arxiv.org/abs/hep-th/0001205",
        ],
        "theorem": {
            "name": "SymmetryPreservingExoticThresholdAnomalyMatchingNoGoTheorem",
            "proved": a_light + a_heavy == a_uv == 0,
            "statement": "Pure Qpsi is QCD-anomaly free on the complete three-27 spectrum. If the 10_-2 exotics acquire Qpsi-preserving masses, integrating them out leaves a Wess-Zumino term carrying their -12 contribution, which cancels the +12 light-fermion measure anomaly. Threshold decoupling alone therefore cannot promote the matter-only trace to a PQ anomaly.",
        },
    }

    gs_support = {
        "schema": "MTTSelectedGreenSchwarzSupportVs4DAxionSource.v1",
        "status": "TEN_DIMENSIONAL_GS_BIANCHI_SUPPORT_CLOSED_FOUR_DIMENSIONAL_AXION_CURRENT_COEFFICIENT_OPEN",
        "selected_support": {
            "q79_time_oriented_charge_sector": charge["conclusion"]["q_mod_448"] == 79,
            "FuYau_Strominger_selection": charge["selection"]["strominger_selection_applies"],
            "Green_Schwarz_Bianchi_identity": charge["geometry"]["green_schwarz_bianchi_identity_verified"],
            "visible_GS_curvature_packet": gs["calculation_results"]["visible_green_schwarz_curvature_verified"],
            "zero_Bianchi_residual": gs["what_this_closes"]["zero_Bianchi_residual_for_required_symbolic_row"],
        },
        "flat_torsion_gerbe_boundary": {
            "torsion_order": flat["flat_gerbe_model"]["torsion_order"],
            "de_Rham_H_curvature": flat["flat_gerbe_model"]["curvature_H_form"],
            "adds_continuous_de_Rham_axion_mode": False,
            "role": "discrete projective/gerbe data; not by itself the continuous PQ Goldstone",
        },
        "not_yet_emitted": {
            "selected_4D_axion_mode": False,
            "harmonic_or_dual_B_field_reduction_form": False,
            "canonically_normalized_decay_constant": False,
            "G_tilde_G_coefficient": False,
            "surviving_current_mixing_coefficients": False,
            "heavy_threshold_WZ_matching_table": False,
            "axion_quality_operator_bound": False,
        },
        "typing_theorem": "A ten-dimensional Bianchi identity and a flat torsion gerbe are support for anomaly consistency, but neither is the four-dimensional coefficient multiplying a/f_a times Tr(G wedge G). That coefficient requires dimensional reduction and current matching.",
    }

    fields = {
        "selected_axion_mode_a": False,
        "selected_current_J_PQ_not_equal_pure_Qpsi": False,
        "current_mixing_coefficients": False,
        "light_chiral_spectrum_and_heavy_mass_map": False,
        "Wess_Zumino_threshold_terms": False,
        "Green_Schwarz_inflow_coefficient": False,
        "nonzero_matched_SU3c_squared_PQ_anomaly": False,
        "PQ_breaking_charge_and_domain_wall_quotient": False,
        "canonical_f_a_normalization": False,
        "quality_breaking_bound": False,
    }
    map_packet = {
        "schema": "MTTLawfulSurvivingAxionCurrentMapContract.v1",
        "status": "FOUR_DIMENSIONAL_CURRENT_MAP_CONTRACT_ZERO_OF_TEN_FINAL_FIELDS",
        "required_map": {
            "current": "J_PQ=J_psi+sum_I c_I J_I+f_a d a_GS",
            "matched_anomaly": "A_eff=A_light+A_WZ+A_GS",
            "strong_CP_acceptance": "A_eff nonzero, axion potential minimized at theta_eff=0, quality corrections below the neutron-EDM tolerance",
        },
        "final_fields": fields,
        "readiness": {"filled": sum(fields.values()), "required": len(fields)},
        "support_not_counted_as_final_fields": [
            "conditional PQ relaxation theorem",
            "axion decay-constant ratios conditional on selected moduli",
            "E6 charge and anomaly trace table",
            "selected q79 GS/Bianchi curvature packet",
        ],
        "observed_theta_or_EDM_used_as_selector": False,
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA96.v1",
        "status": "U6_REDUCED_TO_4D_GS_AXION_REDUCTION_AND_SURVIVING_CURRENT_NOT_EXOTIC_DECOUPLING",
        "closed_now": [
            "pure Qpsi UV anomaly cancellation",
            "symmetry-preserving threshold anomaly-matching no-go",
            "ten-dimensional selected GS/Bianchi support inventory",
            "minimal ten-field four-dimensional current-map contract",
        ],
        "retained_diagnostics": {
            "matter_only_anomaly": a_light,
            "matter_only_singlet_N_DW": e6["domain_wall_diagnostic"]["naive_N_DW_after_singlet_identification"],
            "selected_prediction": False,
        },
        "U6_selected_QCD_anomaly_closed": False,
        "U6_strong_CP_closed": False,
        "new_continuous_parameters_added": 0,
        "non_looping_lock": "Do not promote exotic decoupling or the matter-only N_DW=3 trace unless the WZ/GS matching terms and surviving current are included.",
        "next_required_artifact": NEXT,
    }

    checks = {
        "U6_selected_next_from_A95": plan["ordered_steps"][0]["target"] == "U6 strong CP selection",
        "complete_Qpsi_anomaly_zero": a_uv == 0,
        "light_heavy_cancel": a_light == 12 and a_heavy == -12,
        "Qpsi_preserving_mass_neutral": matching["symmetry_preserving_exotic_mass"]["Qpsi_charge_sum"] == 0,
        "IR_matched_total_zero": matching["IR_matching"]["matched_total"] == 0,
        "selected_GS_support_present": all(gs_support["selected_support"].values()),
        "flat_gerbe_curvature_zero": gs_support["flat_torsion_gerbe_boundary"]["de_Rham_H_curvature"] == "0",
        "no_4D_final_field_overpromoted": sum(fields.values()) == 0,
        "matter_only_NDW_not_promoted": not frontier["retained_diagnostics"]["selected_prediction"],
        "strong_CP_not_overclosed": not frontier["U6_strong_CP_closed"],
        "conditional_PQ_support_retained": cp["closed"]["conditional_PQ_relaxation_theorem"],
        "no_new_parameter": frontier["new_continuous_parameters_added"] == 0,
    }
    outputs = {
        "anomaly_matching": str(MATCHING.relative_to(ROOT)).replace("\\", "/"),
        "GS_support": str(GS.relative_to(ROOT)).replace("\\", "/"),
        "current_map": str(MAP.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedFluxThresholdAxionCurrentAnomalyMatchingMap.v1",
        "status": STATUS,
        "results": {
            "threshold_only_Qpsi_route_rejected": True,
            "selected_10D_GS_support_closed": True,
            "selected_4D_axion_current_map_closed": False,
            "U6_selected_anomaly_closed": False,
            "U6_strong_CP_closed": False,
            "current_map_readiness": "0/10",
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [
            {"path": str(path), "sha256": sha256(path)} for path in paths.values()
        ],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_FluxThresholdAxionCurrentAnomalyMatchingMap_v1",
        "status": STATUS,
        "Qpsi_UV_anomaly": a_uv,
        "light_anomaly": a_light,
        "heavy_WZ_match": a_heavy,
        "threshold_only_route_rejected": True,
        "selected_10D_GS_support": True,
        "four_dimensional_current_map": "0/10",
        "U6_strong_CP_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Flux-Threshold Axion-Current Anomaly-Matching Map v1

## Threshold no-go

For pure `Q_psi`, the exact colored anomaly is

```text
three light 16_1 families:  +{a_light}
three heavy 10_-2 sectors:  {a_heavy}
complete three 27s:          {a_uv}
```

The mass operator `1_4 10_-2 10_-2` has charge `4-2-2=0`, so making the
exotics heavy preserves `Q_psi`. Integrating them out cannot erase their
anomaly: it emits a Wess--Zumino term with coefficient `{a_heavy}`. The light
fermion measure contributes `+{a_light}`, and the matched IR total remains zero.
Therefore exotic threshold decoupling alone cannot turn pure `Q_psi` into the
anomalous PQ current required by the strong-CP mechanism.

## Green-Schwarz route

The q79 branch does supply real support: the Fu--Yau/Strominger charge sector
passes the Green--Schwarz Bianchi identity, and the selected visible curvature
packet has zero symbolic residual. But the selected order-three gerbe candidate
is flat with de Rham curvature `H=0`. It supplies discrete projective data, not
by itself a continuous four-dimensional axion mode or its `G tilde G`
coefficient.

The lawful next map is

```text
J_PQ = J_psi + sum_I c_I J_I + f_a d a_GS,
A_eff = A_light + A_WZ + A_GS.
```

It must derive a nonzero `A_eff`, the surviving current, heavy-threshold WZ
terms, GS inflow, breaking quotient, normalization and quality bound from one
selected compactification. The final map is currently `0/10`; the existing PQ,
ratio, E6 and Bianchi results are support, not substitutes.

The old matter-only `N_DW=3` remains a useful diagnostic but is not a selected
prediction. U6 is not closed, and no parameter is added here.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (MATCHING, matching),
        (GS, gs_support),
        (MAP, map_packet),
        (FRONTIER, frontier),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
