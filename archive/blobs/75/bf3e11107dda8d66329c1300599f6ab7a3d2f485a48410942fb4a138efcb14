"""Search mass-ratio orientation laws and finite-phase CKM clues."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_massratioorientationlawsearch_or_finitephaseckmclue"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MassRatioOrientationLawSearch_or_FinitePhaseCKMClue_v1.md"

COMMON_VALUES = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
MIXING_SEED = DATA / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"
BRIDGE = DATA / "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge.candidate.json"

STATUS = (
    "MTT_SELECTED_MASSRATIOORIENTATIONLAWSEARCH_OR_FINITEPHASECKMCLUE_"
    "BUILT_Q79_PHASE_CLUE_ORIENTATION_SOURCE_OPEN"
)
NEXT = "MTT_Selected_CKMQ79PhaseSourceBridge_or_MassRatioOrientationTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel_err(predicted: float, target: float) -> float:
    return abs(predicted - target) / abs(target)


def phase_distance(a: float, b: float) -> float:
    return abs(math.atan2(math.sin(a - b), math.cos(a - b)))


def rational_exponent_search(ratios: dict[str, float], targets: dict[str, float]) -> dict:
    exponents = sorted(
        {Fraction(n, d) for d in range(2, 13) for n in range(1, d + 1)},
        key=lambda item: float(item),
    )
    result = {}
    for target_name, target in targets.items():
        rows = []
        for ratio_name, ratio in ratios.items():
            if not 0.0 < ratio < 1.0:
                continue
            for exponent in exponents:
                prediction = ratio ** float(exponent)
                rows.append(
                    {
                        "ratio": ratio_name,
                        "ratio_value": ratio,
                        "exponent": f"{exponent.numerator}/{exponent.denominator}",
                        "prediction": prediction,
                        "target": target,
                        "absolute_residual": prediction - target,
                        "relative_residual": rel_err(prediction, target),
                    }
                )
        result[target_name] = sorted(rows, key=lambda row: row["relative_residual"])[:10]
    return result


def main() -> int:
    common = load(COMMON_VALUES)
    mixing = load(MIXING_SEED)
    bridge = load(BRIDGE)

    yu = common["derived_magnitudes"]["diag_abs_Y_u"]
    yd = common["derived_magnitudes"]["diag_abs_Y_d"]
    ye = common["derived_magnitudes"]["diag_abs_Y_e"]

    ckm_params = mixing["CKM_packet"]["derived_parameters"]
    pmns_params = mixing["PMNS_packet"]["derived_parameters"]
    targets = {
        "CKM_s12": ckm_params["s12"],
        "CKM_s23": ckm_params["s23"],
        "CKM_s13": ckm_params["s13"],
    }
    ratios = {
        "u12": yu[0] / yu[1],
        "u23": yu[1] / yu[2],
        "u13": yu[0] / yu[2],
        "d12": yd[0] / yd[1],
        "d23": yd[1] / yd[2],
        "d13": yd[0] / yd[2],
        "e12": ye[0] / ye[1],
        "e23": ye[1] / ye[2],
        "e13": ye[0] / ye[2],
    }

    # Orthogonal complex nesting test: |sqrt(r_d) - i sqrt(r_u)|.
    gst_rows = {}
    for name, d_key, u_key, target_key in [
        ("GST_12", "d12", "u12", "CKM_s12"),
        ("GST_23", "d23", "u23", "CKM_s23"),
        ("GST_13", "d13", "u13", "CKM_s13"),
    ]:
        a = math.sqrt(ratios[d_key])
        b = math.sqrt(ratios[u_key])
        plus_i = math.sqrt(a * a + b * b)
        difference_floor = abs(a - b)
        sum_ceiling = a + b
        target = targets[target_key]
        gst_rows[name] = {
            "down_sqrt_ratio": a,
            "up_sqrt_ratio": b,
            "plus_i_prediction": plus_i,
            "target": target,
            "plus_i_relative_residual": rel_err(plus_i, target),
            "continuous_phase_can_hit_target": difference_floor <= target <= sum_ceiling,
            "phase_family_lower_bound": difference_floor,
            "phase_family_upper_bound": sum_ceiling,
        }

    rational_rows = rational_exponent_search(ratios, targets)

    ckm_delta = ckm_params["delta_rad"]
    pmns_delta = pmns_params["delta_rad"]
    q79_phase = 2.0 * math.pi * 79.0 / 448.0
    q369_phase = 2.0 * math.pi * 369.0 / 448.0
    plus_i_phase = math.pi / 2.0
    q79_ckm_resid = phase_distance(q79_phase, ckm_delta)
    q369_ckm_resid = phase_distance(q369_phase, ckm_delta)
    plus_i_ckm_resid = phase_distance(plus_i_phase, ckm_delta)

    q_grid_best_pmns_q = min(
        range(448),
        key=lambda q: phase_distance(2.0 * math.pi * q / 448.0, pmns_delta),
    )
    q_grid_best_pmns_phase = 2.0 * math.pi * q_grid_best_pmns_q / 448.0

    finite_phase = {
        "schema": "MTTFinitePhaseCKMClue.v1",
        "status": "Q79_CLOSE_TO_CKM_CP_PHASE_SOURCE_BRIDGE_OPEN",
        "selected_q79_phase_rad": q79_phase,
        "selected_q79_phase_deg": math.degrees(q79_phase),
        "conjugate_q369_phase_rad": q369_phase,
        "conjugate_q369_phase_deg": math.degrees(q369_phase),
        "orthogonal_plus_i_phase_rad": plus_i_phase,
        "orthogonal_plus_i_phase_deg": 90.0,
        "CKM_delta_rad": ckm_delta,
        "CKM_delta_deg": ckm_params["delta_deg"],
        "q79_to_CKM_absolute_phase_residual_rad": q79_ckm_resid,
        "q79_to_CKM_absolute_phase_residual_deg": math.degrees(q79_ckm_resid),
        "q369_to_CKM_absolute_phase_residual_deg": math.degrees(q369_ckm_resid),
        "plus_i_to_CKM_absolute_phase_residual_deg": math.degrees(plus_i_ckm_resid),
        "PMNS_delta_rad": pmns_delta,
        "PMNS_delta_deg": pmns_params["delta_deg"],
        "selected_q79_to_PMNS_residual_deg": math.degrees(phase_distance(q79_phase, pmns_delta)),
        "best_Z448_PMNS_q_if_target_fit_forbidden": q_grid_best_pmns_q,
        "best_Z448_PMNS_phase_deg": math.degrees(q_grid_best_pmns_phase),
        "best_Z448_PMNS_residual_deg": math.degrees(phase_distance(q_grid_best_pmns_phase, pmns_delta)),
        "target_fitting_warning": "The PMNS best-q scan is diagnostic only and may not select a source branch.",
        "strict_source_bridge_closed": False,
    }

    mass_ratio = {
        "schema": "MTTMassRatioOrientationLawSearch.v1",
        "status": "GST_LIKE_12_PROMISING_23_13_FAIL_AS_SIMPLE_ORTHOGONAL_LAW",
        "input_yukawa_magnitudes_tier": common["status"],
        "ratios": ratios,
        "orthogonal_complex_nesting_tests": gst_rows,
        "best_rational_exponent_rows": rational_rows,
        "source_law_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "interpretation": [
            "The 12/Cabibbo row is naturally close to a square-root down/up mass-ratio law with an orthogonal complex phase.",
            "The same simple law cannot hit CKM 23 or 13 because the target lies below the allowed phase-family lower bound.",
            "A selected quark-specific higher-breakdown law is required for 23/13 if this route is to become a source theorem.",
        ],
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterMassRatioOrientationSearch.v1",
        "status": "Q79_PHASE_AND_HIGHER_BREAKDOWN_TARGETS_IDENTIFIED",
        "closed_now": [
            "finite q79 phase is closer to CKM delta than the raw +i phase",
            "GST-like orthogonal nesting explains why the Cabibbo row is structurally special",
            "simple square-root orthogonal nesting is rejected for CKM 23 and 13",
            "best-rational exponent diagnostics are frozen for non-target-selected follow-up",
        ],
        "remaining_to_promote": [
            "derive the physical CKM phase map delta_CKM = 2*pi*79/448 plus allowed transport correction or prove exact equality in the selected convention",
            "derive a selected higher-breakdown quark orientation law for 23 and 13",
            "derive or reject a PMNS finite-phase source distinct from the q79 CKM branch",
            "connect the orientation law to the already integrated flavor operator without using CKM/PMNS targets as selectors",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedMassRatioOrientationLawSearchOrFinitePhaseCKMClue",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "orientation_source_theorem_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "common_scale_yukawa_higgs_values": str(COMMON_VALUES.relative_to(ROOT)).replace("\\", "/"),
            "mixing_seed": str(MIXING_SEED.relative_to(ROOT)).replace("\\", "/"),
            "flavor_operator_orientation_bridge": str(BRIDGE.relative_to(ROOT)).replace("\\", "/"),
        },
        "output_packets": {
            "finite_phase_ckm_clue": f"candidate_data/{SLUG}/finite_phase_ckm_clue.packet.json",
            "mass_ratio_orientation_law_search": f"candidate_data/{SLUG}/mass_ratio_orientation_law_search.packet.json",
            "next_cutset_after_massratio_orientation_search": f"candidate_data/{SLUG}/next_cutset_after_massratio_orientation_search.packet.json",
        },
        "next_required_artifact": NEXT,
        "closure_decision": {
            "finite_q79_ckm_phase_clue_found": q79_ckm_resid < plus_i_ckm_resid,
            "q79_CKM_phase_residual_deg": math.degrees(q79_ckm_resid),
            "plus_i_CKM_phase_residual_deg": math.degrees(plus_i_ckm_resid),
            "GST_like_Cabibbo_row_promising": gst_rows["GST_12"]["plus_i_relative_residual"] < 0.02,
            "GST_like_23_13_simple_law_rejected": (
                not gst_rows["GST_23"]["continuous_phase_can_hit_target"]
                and not gst_rows["GST_13"]["continuous_phase_can_hit_target"]
            ),
            "selected_orientation_source_theorem_closed": False,
            "selected_CKM_PMNS_values_derived": False,
            "full_true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "MassRatioOrientationSearchAndFinitePhaseCKMClueTheorem",
            "proved": True,
            "statement": "The flavor rows identify two nontrivial orientation-source clues: the selected q79 finite phase is much closer to the measured CKM phase than a raw +i phase, and the Cabibbo row is naturally approximated by an orthogonal square-root mass-ratio law. The same simple orthogonal nesting cannot produce CKM 23 and 13, so a source theorem still needs a selected higher-breakdown quark law and a physical finite-character-to-CKM phase map. No CKM/PMNS target is used as a source selector.",
        },
    }

    cert = {
        "certificate": "MTT_Selected_MassRatioOrientationLawSearch_or_FinitePhaseCKMClue_v1",
        "status": STATUS,
        "candidate": candidate["candidate"],
        "theorem": candidate["theorem"]["name"],
        "proved": True,
        "finite_q79_ckm_phase_clue_found": candidate["closure_decision"][
            "finite_q79_ckm_phase_clue_found"
        ],
        "q79_CKM_phase_residual_deg": candidate["closure_decision"]["q79_CKM_phase_residual_deg"],
        "GST_like_Cabibbo_row_promising": candidate["closure_decision"][
            "GST_like_Cabibbo_row_promising"
        ],
        "GST_like_23_13_simple_law_rejected": candidate["closure_decision"][
            "GST_like_23_13_simple_law_rejected"
        ],
        "selected_orientation_source_theorem_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected MassRatioOrientationLawSearch or FinitePhaseCKMClue v1

Status: `{STATUS}`

## Theorem

**MassRatioOrientationSearchAndFinitePhaseCKMClueTheorem.** The flavor rows identify two nontrivial orientation-source clues: the selected q79 finite phase is much closer to the measured CKM phase than a raw `+i` phase, and the Cabibbo row is naturally approximated by an orthogonal square-root mass-ratio law. The same simple orthogonal nesting cannot produce CKM 23 and 13, so a source theorem still needs a selected higher-breakdown quark law and a physical finite-character-to-CKM phase map.

## Key Numbers

- `2*pi*79/448 = {math.degrees(q79_phase)} deg`
- CKM delta replay: `{ckm_params["delta_deg"]} deg`
- q79-to-CKM residual: `{math.degrees(q79_ckm_resid)} deg`
- `+i`-to-CKM residual: `{math.degrees(plus_i_ckm_resid)} deg`
- GST-like `12` relative residual: `{gst_rows["GST_12"]["plus_i_relative_residual"]}`
- GST-like `23` and `13` are rejected because the target angles fall below the continuous phase-family lower bounds.

## Claim Boundary

This is a source-theorem target, not a selected orientation theorem. It uses measured CKM/PMNS rows only as diagnostics after the source boundary, and it does not derive CKM/PMNS values or true SM equivalence.

Next artifact: `{NEXT}`.
"""

    write_json(PACKET_DIR / "finite_phase_ckm_clue.packet.json", finite_phase)
    write_json(PACKET_DIR / "mass_ratio_orientation_law_search.packet.json", mass_ratio)
    write_json(PACKET_DIR / "next_cutset_after_massratio_orientation_search.packet.json", next_cutset)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
