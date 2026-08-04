"""Analyze the q79 stability/HYM or Route-C residual source gate.

This imports the SM-side stability attempt and checks it against the q79
V_alpha stability chain.  The result is a central-neutral destabilizer
subtheorem, not full stability/HYM closure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

OUT_DIR = CANDIDATES / "q79_stability_hym_or_routec_residual_source"
OUT_TABLE = OUT_DIR / "central_neutral_destabilizer_summary.json"
OUT_CANDIDATE = CANDIDATES / "q79_stability_hym_or_routec_residual_source.candidate.json"
OUT_CERT = CERTS / "q79_stability_hym_or_routec_residual_source_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1.md"

STATUS = "Q79_SELECTED_ROUTEC_STABILITY_ATTEMPT_CENTRAL_NEUTRAL_CLOSED_GLOBAL_ENUMERATION_OPEN"
NEXT = "Q79_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1"

Q79_INPUTS = {
    "same_source_fill_nogo": CERTS / "q79_samesource_operatorpacket_fill_or_nogo_certificate.json",
    "stability_filter": CANDIDATES / "valpha_extension_stability_filter_attempt.candidate.json",
    "zero_slope_reduction": CANDIDATES / "valpha_zero_slope_yoneda_reduction.candidate.json",
    "kunneth_yoneda_scalar": CANDIDATES / "valpha_kunneth_yoneda_scalar_proof.candidate.json",
    "central_neutral_destabilizer_reduction": CANDIDATES
    / "valpha_central_neutral_destabilizer_reduction.candidate.json",
    "appell_humbert_yoneda_promotion": CANDIDATES
    / "valpha_appell_humbert_yoneda_promotion.candidate.json",
    "source_origin_finite_emission_bridge": CANDIDATES
    / "q79_valpha_source_origin_finite_emission_bridge.candidate.json",
}

SM_INPUTS = {
    "stability_source_certificate": SM
    / "certificates"
    / "selected_routec_stability_hym_or_routec_residual_source_certificate.json",
    "stability_source_candidate": SM
    / "candidate_data"
    / "selected_routec_stability_hym_or_routec_residual_source.candidate.json",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": str(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
        "what_closes": data.get("what_closes") or data.get("what_closes_now") or data.get("closed_by_this_attempt") or {},
        "what_remains_open": data.get("what_remains_open") or data.get("still_open") or {},
    }


def build_central_summary(central: dict[str, Any], sm: dict[str, Any]) -> dict[str, Any]:
    central_table = central["central_neutral_destabilizer_table"]
    sm_central = sm["central_neutral_destabilizer_theorem"]
    return {
        "lane": sm_central["lane"],
        "candidate_count": sm_central["candidate_count"],
        "candidate_list": sm_central["candidate_list"],
        "hom_to_L_destabilizers_empty": sm_central["hom_to_L_destabilizers_empty"],
        "hom_to_Q_nonnegative_candidates_finite_six": sm_central[
            "hom_to_Q_nonnegative_candidates_finite_six"
        ],
        "all_candidate_boundaries_injective": sm_central["all_candidate_boundaries_injective"],
        "all_candidates_obstructed": sm_central["all_candidates_obstructed"],
        "central_shared_circle_degree_zero": sm_central["central_shared_circle_degree_zero"],
        "q79_table_status": central["status"],
        "q79_table_candidate_count": len(central_table["candidate_rows"]),
        "bounded_scan_matches": central_table["bounded_scan_check"][
            "matches_inequality_candidate_list"
        ],
    }


def build_candidate() -> dict[str, Any]:
    q79 = {name: load(path) for name, path in Q79_INPUTS.items()}
    sm = {name: load(path) for name, path in SM_INPUTS.items()}
    sm_candidate = sm["stability_source_candidate"]
    central_summary = build_central_summary(
        q79["central_neutral_destabilizer_reduction"], sm_candidate
    )

    return {
        "certificate": "Q79SelectedRouteCStabilityHYMOrRouteCResidualSource",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "q79_input_statuses": {name: status_record(path) for name, path in Q79_INPUTS.items()},
        "sm_input_statuses": {name: status_record(path) for name, path in SM_INPUTS.items()},
        "rank2_stability_attempt": sm_candidate["rank2_stability_attempt"],
        "zero_slope_closure": sm_candidate["zero_slope_closure"],
        "central_neutral_destabilizer_theorem": central_summary,
        "appell_humbert_promotion": sm_candidate["appell_humbert_promotion"],
        "route_c_residual_lane": sm_candidate["route_c_residual_lane"],
        "q79_proof_verdict": {
            "central_neutral_stability_subtheorem_proved": True,
            "full_stability_proved": False,
            "hym_existence_proved": False,
            "route_c_residual_selected": False,
            "why_full_gate_not_closed": sm_candidate["proof_verdict"][
                "why_full_gate_not_closed"
            ],
        },
        "what_closes_now": sm_candidate["what_closes_now"],
        "what_remains_open": sm_candidate["what_remains_open"],
        "guardrails": {
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "uses_locked_target_columns_as_selector": False,
            "claims_full_stability": False,
            "claims_hym_existence": False,
            "claims_selected_RouteC_residual": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79SelectedRouteCStabilityCentralNeutralSubtheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "For the selected q79/F,m=1 rank-two V_alpha extension with "
                "L=(1,-2,0), selected nonzero Ext class, and slope chamber "
                "p=(1,2,1), all central-neutral base-pullback rank-one "
                "destabilizer candidates are obstructed in the reduced "
                "Kunneth/Appell-Humbert Yoneda model. This proves the "
                "central-neutral stability subtheorem, not full stability/HYM."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }


def render_bool_map(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def build_paper(data: dict[str, Any]) -> str:
    central = data["central_neutral_destabilizer_theorem"]
    verdict = data["q79_proof_verdict"]
    return f"""# Q79 Selected Route-C Stability/HYM or Route-C Residual Source v1

## Result

This closes the **central-neutral destabilizer subtheorem** for the q79/F,m=1
rank-two `V_alpha` lane. It does not close full stability/HYM.

## Central-Neutral Theorem

- lane: `{central["lane"]}`
- candidate count: `{central["candidate_count"]}`
- candidates: `{central["candidate_list"]}`
- Hom-to-`L` destabilizers empty: `{central["hom_to_L_destabilizers_empty"]}`
- Hom-to-`Q=L^-1` candidates finite six: `{central["hom_to_Q_nonnegative_candidates_finite_six"]}`
- all candidate boundaries injective: `{central["all_candidate_boundaries_injective"]}`
- all candidates obstructed: `{central["all_candidates_obstructed"]}`
- shared-circle degree zero preserved: `{central["central_shared_circle_degree_zero"]}`

## Still Not Full HYM

{chr(10).join(f"- {item}" for item in verdict["why_full_gate_not_closed"])}

## What This Closes

{render_bool_map(data["what_closes_now"])}

## What Remains Open

{render_bool_map(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as a subtheorem.

{data["theorem"]["statement"]}

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_TABLE, data["central_neutral_destabilizer_theorem"])
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 stability/HYM or Route-C residual source")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
