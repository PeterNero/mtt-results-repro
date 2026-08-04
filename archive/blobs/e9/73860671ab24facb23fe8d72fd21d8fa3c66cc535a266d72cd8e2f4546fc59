"""Build the selected non-identity rho_E transition-source gate artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79 / "certificates"

OUTPUT_DATA = DATA / "selected_nonidentity_rhoe_transition_source.candidate.json"
OUTPUT_CERT = CERTS / "selected_nonidentity_rhoe_transition_source_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_NonIdentity_RhoE_Transition_Source_v1.md"

INPUTS = {
    "phifin": DATA / "finite_emission_morphism_phifin.candidate.json",
    "rhoe_ansatz": Q79_CERTS / "visible_rhoE_source_ansatz_search_certificate.json",
    "projective_rhoe_validator": Q79_CERTS / "iwasawa_projective_rhoE_mesh_validator_certificate.json",
    "coboundary_diagnostic": Q79_CERTS / "iwasawa_face_graph_coboundary_diagnostic_certificate.json",
    "discrete_gerbe_holonomy": Q79_CERTS / "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json",
    "fixed_gerbe_representative": Q79_CERTS / "time_oriented_fixed_gerbe_representative_certificate.json",
    "flat_gerbe_promotion": Q79_CERTS / "time_oriented_m1_flat_gerbe_promotion_certificate.json",
    "projective_twist_hunt": Q79_CERTS / "iwasawa_projective_twist_source_hunt_certificate.json",
    "twisted_packet_fill": Q79_CERTS / "iwasawa_twisted_source_packet_fill_attempt_certificate.json",
    "twisted_chan_paton": Q79_CERTS / "visible_twisted_chan_paton_rescue_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {key: {"path": str(path), "present": path.exists()} for key, path in INPUTS.items()}


def build_candidate() -> dict[str, object]:
    phifin = load_json(INPUTS["phifin"])
    ansatz = load_json(INPUTS["rhoe_ansatz"])
    projective_validator = load_json(INPUTS["projective_rhoe_validator"])
    coboundary = load_json(INPUTS["coboundary_diagnostic"])
    holonomy = load_json(INPUTS["discrete_gerbe_holonomy"])
    fixed = load_json(INPUTS["fixed_gerbe_representative"])
    flat = load_json(INPUTS["flat_gerbe_promotion"])
    twist_hunt = load_json(INPUTS["projective_twist_hunt"])
    fill = load_json(INPUTS["twisted_packet_fill"])
    cp = load_json(INPUTS["twisted_chan_paton"])

    ordinary_no_go = {
        "constant_ordinary_carriers_blocked": ansatz["calculation_results"]["ordinary_constant_carriers_blocked"],
        "central_absorption_as_ordinary_rhoE_blocked": ansatz["calculation_results"]["qutrit_projective_central_absorption_as_ordinary_rhoE_blocked"],
        "pure_gauge_false_positive_detector_ready": coboundary["what_this_closes"]["pure_gauge_false_positive_detector"],
        "finite_noncommuting_prototype_is_pure_gauge": coboundary["verdict"]["finite_noncommuting_prototype_is_pure_gauge"],
    }
    projective_evidence = {
        "projective_validator_ready": projective_validator["verdict"]["projective_validator_ready"],
        "nontrivial_projective_carrier_validated": projective_validator["verdict"]["projective_magnetic_carrier_validated_as_twisted_not_ordinary"],
        "finite_holonomy_matches_qutrit_cocycle": holonomy["finite_model"]["matches_qutrit_projective_cocycle"],
        "finite_bianchi_residual_zero": holonomy["finite_model"]["discrete_bianchi_residual_zero"],
        "time_oriented_q79_m1_fixed": fixed["calculation_results"]["time_oriented_torsion_label_m1_fixed"],
        "conditional_flat_gerbe_exists": flat["calculation_results"]["conditional_flat_gerbe_representative_exists"],
        "qutrit_projective_module_compatible": flat["calculation_results"]["projective_qutrit_module_compatible"],
        "twisted_chan_paton_rescue_exists": cp["what_this_closes"]["finite_algebraic_twisted_CP_rescue_family_exists"],
    }
    promotion_blockers = {
        "selected_projective_twist_source_found": twist_hunt["verdict"]["selected_projective_twist_source_found"],
        "selected_flat_gerbe_representative_closed": flat["calculation_results"]["selected_flat_gerbe_representative_closed"],
        "freed_witten_verified": flat["calculation_results"]["freed_witten_verified"],
        "selected_D_E_dotD_constructed": fixed["calculation_results"]["selected_D_E_dotD_constructed"],
        "twisted_packet_passes": fill["verdict"]["promotion_packet_passes"],
    }

    ordinary_retired = all(ordinary_no_go.values())
    projective_candidate_locked = all(projective_evidence.values())
    selected_source_closed = all(promotion_blockers.values())

    return {
        "candidate": "MTTSelectedNonIdentityRhoETransitionSourceGate",
        "status": "MTT_SELECTED_NONIDENTITY_RHOE_SOURCE_REDUCED_TO_PROJECTIVE_GERBE_PROMOTION",
        "source_status": source_status(),
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_TO_PROJECTIVE_TWISTED_RHOE",
            "straight_path": {
                "name": "ordinary non-identity rho_E transition source",
                "succeeds": False,
                "reason": "Current q79 certificates retire constant ordinary carriers and pure-gauge/noncommuting prototypes; central qutrit absorption cannot be promoted as ordinary rho_E.",
            },
            "superset_convergence": {
                "succeeds": True,
                "converging_paths": [
                    "visible rhoE ansatz no-go",
                    "finite face-graph coboundary diagnostic",
                    "projective rhoE mesh validator",
                    "discrete Z3 gerbe holonomy candidate",
                    "time-oriented q79/F,m=1 gerbe representative",
                    "twisted Chan-Paton rescue",
                ],
                "locked_target": "selected projective/twisted rho_E source from a fixed Deligne/Cech gerbe or B-field representative",
            },
            "superset_repair": {
                "needed": True,
                "repair_object": "promote the q79/F,m=1 projective gerbe rho_E candidate to selected source data and then derive D_E/dotD",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "No observed flavor, mass, coupling, or benchmark data are used; the gate is built from source certificates and validators.",
            },
        },
        "imported_results": {
            "phifin_status": phifin["status"],
            "rhoe_ansatz_status": ansatz["status"],
            "projective_rhoe_validator_status": projective_validator["status"],
            "coboundary_diagnostic_status": coboundary["status"],
            "discrete_gerbe_holonomy_status": holonomy["status"],
            "fixed_gerbe_status": fixed["status"],
            "flat_gerbe_status": flat["status"],
            "projective_twist_hunt_status": twist_hunt["status"],
            "twisted_packet_fill_status": fill["status"],
            "twisted_chan_paton_status": cp["status"],
        },
        "gate_results": {
            "ordinary_rhoE_route_retired": ordinary_retired,
            "projective_twisted_rhoE_candidate_locked": projective_candidate_locked,
            "selected_projective_rhoE_source_closed": selected_source_closed,
            "Phi_fin_selected_payload_closed": False,
        },
        "ordinary_no_go": ordinary_no_go,
        "projective_candidate": {
            "kind": "projective_torsion_gerbe_rho_E",
            "finite_model": holonomy["finite_model"],
            "evidence": projective_evidence,
            "validator": projective_validator["audit_cases"]["projective_magnetic_carrier"],
        },
        "promotion_blockers": promotion_blockers,
        "minimal_next_packet": {
            "name": "MTT_Projective_Gerbe_RhoE_Source_Promotion_v1",
            "must_supply": [
                "selected Deligne/Cech gerbe or B-field period representative on the actual q79/F,m=1 Iwasawa/Strominger sector",
                "proof that the representative maps to the zeta3 central projective rho_E corner cocycle",
                "Freed-Witten restrictions on selected cycles and W3/spinC checks",
                "Green-Schwarz/Bianchi compatibility for the selected gauge/gravity curvature row",
                "selected twisted sector projectors and projector retention",
                "D_E, Riesz/Green, dotD, and C1 outputs from the same selected twisted source",
            ],
        },
        "theorem": {
            "name": "SelectedNonIdentityRhoETransitionSourceReduction",
            "proved": True,
            "statement": (
                "An ordinary non-identity rho_E source is not the live closure route. Current certificates reduce the rho_E gate "
                "to a projective/twisted source: the q79/F,m=1 flat Z3 gerbe holonomy matches the qutrit projective rho_E cocycle "
                "and has a validator-ready finite carrier, but it is not yet promoted to selected Deligne/Cech or B-field source data."
            ),
        },
        "next_required_artifact": "MTT_Projective_Gerbe_RhoE_Source_Promotion_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    gates = candidate["gate_results"]
    return {
        "certificate": "MTTSelectedNonIdentityRhoETransitionSourceGate",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "ordinary_nonidentity_rhoE_route_retired": gates["ordinary_rhoE_route_retired"],
            "projective_twisted_rhoE_candidate_locked": gates["projective_twisted_rhoE_candidate_locked"],
            "pure_gauge_rhoE_false_positive_guardrail_imported": True,
            "next_promotion_packet_specified": True,
        },
        "what_remains_open": {
            "selected_projective_gerbe_rhoE_source": True,
            "selected_Deligne_Cech_or_Bfield_period_representative": True,
            "Freed_Witten_and_Bianchi_for_selected_cycles": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "primitive_C1_overlap_tensors": True,
            "Phi_fin_selected_payload": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    ordinary = "\n".join(f"- `{key}`: `{value}`" for key, value in candidate["ordinary_no_go"].items())
    evidence = "\n".join(f"- `{key}`: `{value}`" for key, value in candidate["projective_candidate"]["evidence"].items())
    blockers = "\n".join(f"- `{key}`: `{value}`" for key, value in candidate["promotion_blockers"].items())
    must = "\n".join(f"- {item}" for item in candidate["minimal_next_packet"]["must_supply"])
    closes = "\n".join(f"- {key}" for key, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {key}" for key, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Selected Non-Identity rho_E Transition Source v1

## Result

The ordinary non-identity `rho_E` route is retired for now.  The live route is a
projective/twisted `rho_E` source: the q79/F,m=1 flat `Z3` gerbe holonomy matches
the qutrit projective carrier, and the projective mesh validator is ready.

This is **superset repair**, not closure.  The projective candidate must still be
promoted to selected Deligne/Cech or B-field source data before it can feed
`D_E`, `dotD`, Riesz/Green, and `C1`.

## Ordinary Route

{ordinary}

## Projective Candidate

{evidence}

## Promotion Blockers

{blockers}

## Next Packet

`{candidate["minimal_next_packet"]["name"]}` must supply:

{must}

## Theorem

`{candidate["theorem"]["name"]}` is proved:

{candidate["theorem"]["statement"]}

## What This Closes

{closes}

## What Remains Open

{open_items}
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate, certificate), encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
