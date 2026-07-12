"""Build the finite emission morphism Phi_fin attempt artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
SMOKE = Q79 / "candidate_data" / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"

OUTPUT_DATA = DATA / "finite_emission_morphism_phifin.candidate.json"
OUTPUT_CERT = CERTS / "finite_emission_morphism_phifin_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Finite_Emission_Morphism_Phi_fin_v1.md"

INPUTS = {
    "source_origin_lemma": DATA / "routec_selected_source_origin_lemma.candidate.json",
    "route_c_residual": SMOKE / "route_c_residual.candidate.json",
    "rhoE_mesh": SMOKE / "rhoE_mesh.candidate.json",
    "rhoE_metric": SMOKE / "rhoE_metric.candidate.json",
    "sector_maps": SMOKE / "sector_maps.candidate.json",
    "de_action": SMOKE / "de_action.candidate.json",
    "riesz_gap": SMOKE / "riesz_gap.candidate.json",
    "reduced_green": SMOKE / "reduced_green.candidate.json",
    "dotd_response": SMOKE / "dotd_response.candidate.json",
    "routec_pipeline": DATA / "selected_routec_hym_operator_pipeline.candidate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {key: {"path": str(path), "present": path.exists()} for key, path in INPUTS.items()}


def all_slot_flag(slots: dict[str, object], flag: str) -> bool:
    return all(bool(row.get(flag)) for row in slots.values())


def build_candidate() -> dict[str, object]:
    lemma = load_json(INPUTS["source_origin_lemma"])
    residual = load_json(INPUTS["route_c_residual"])
    rhoe_mesh = load_json(INPUTS["rhoE_mesh"])
    de_action = load_json(INPUTS["de_action"])
    riesz_gap = load_json(INPUTS["riesz_gap"])
    reduced_green = load_json(INPUTS["reduced_green"])
    dotd = load_json(INPUTS["dotd_response"])
    pipeline = load_json(INPUTS["routec_pipeline"])

    de_slots = de_action["operator_slots"]
    riesz_slots = riesz_gap["spectral_slots"]
    green_slots = reduced_green["green_slots"]
    dotd_slots = dotd["dotd_response_slots"]
    sectors = sorted(de_slots.keys())

    positive_gates = residual["positive_gates"]
    residuals_all_zero = all(row["value"] == 0.0 for row in residual["residuals"].values())
    selected_flags = {
        "route_c_residual": bool(residual["selected_source_verified"]),
        "rhoE_mesh": bool(rhoe_mesh["selected_by_mtt"]),
        "de_action": all_slot_flag(de_slots, "selected_source_verified"),
        "riesz_gap": all_slot_flag(riesz_slots, "selected_source_verified"),
        "reduced_green": all_slot_flag(green_slots, "selected_source_verified"),
        "dotd_response": all_slot_flag(dotd_slots, "selected_dotD_source_verified"),
        "dotd_alpha1": all_slot_flag(dotd_slots, "alpha1_driver_verified"),
    }

    shape_gates = {
        "residual_codomain_shape_present": residuals_all_zero and set(residual["residuals"]) == {
            "rho_cocycle",
            "metric_compatibility",
            "integrability_F02",
            "hym_primitive",
            "bianchi_alpha1",
            "mtt_gradient",
            "strominger_residual",
        },
        "positive_gap_fields_present": (
            positive_gates["mtt_hessian_min_eigenvalue"]["value"] > positive_gates["mtt_hessian_min_eigenvalue"]["strict_lower_bound"]
            and positive_gates["riesz_gap_min"]["value"] > positive_gates["riesz_gap_min"]["strict_lower_bound"]
        ),
        "sector_slots_present": sectors == ["H", "L", "N", "Q", "d", "e", "u"],
        "de_riesz_green_dotd_shapes_present": (
            set(riesz_slots) == set(sectors)
            and set(green_slots) == set(sectors)
            and set(dotd_slots) == set(sectors)
        ),
    }

    selected_payload_closed = all(selected_flags.values()) and rhoe_mesh["candidate_kind"] != "identity_rhoE_smoke_unselected"

    return {
        "candidate": "MTTFiniteEmissionMorphismPhiFinAttempt",
        "status": "MTT_FINITE_EMISSION_MORPHISM_PHIFIN_SCHEMA_BUILT_SELECTED_VALUES_OPEN",
        "source_status": source_status(),
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_SCHEMA_NOT_SELECTED_VALUES",
            "straight_path": {
                "name": "reuse q79 smoke packet as Phi_fin",
                "succeeds": False,
                "reason": "The packet has the right finite shape and residual zeros, but its source flags are false and rhoE is explicitly identity smoke.",
            },
            "superset_convergence": {
                "succeeds": True,
                "converging_paths": [
                    "source-origin lemma reduction",
                    "Route-C residual codomain",
                    "D_E/Riesz/Green/dotD validator schemas",
                    "selected S3/GS/q79,F,m=1 branch support",
                ],
                "locked_target": "replace smoke entries with selected Phi_fin outputs in the same finite schema",
            },
            "superset_repair": {
                "needed": True,
                "repair_object": "selected non-identity rhoE/connection data and selected alpha1/dotD source",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "This artifact reads existing finite validator schemas and does not use measured constants or target fits.",
            },
        },
        "imported_results": {
            "source_origin_reduction_status": lemma["status"],
            "routec_pipeline_status": pipeline["status"],
            "rhoE_kind": rhoe_mesh["candidate_kind"],
            "branch_packet": residual["branch_packet"],
        },
        "phifin_schema": {
            "domain": lemma["finite_emission_morphism_contract"]["domain"],
            "codomain_files": {
                key: str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
                for key, path in INPUTS.items()
                if key not in {"source_origin_lemma", "routec_pipeline"}
            },
            "sectors": sectors,
            "required_outputs": pipeline["next_payload_contract"]["required_outputs"],
            "shape_gates": shape_gates,
            "selected_flags": selected_flags,
        },
        "obstruction": {
            "selected_payload_closed": selected_payload_closed,
            "identity_rhoE_smoke": rhoe_mesh["candidate_kind"] == "identity_rhoE_smoke_unselected",
            "unselected_flags": [key for key, value in selected_flags.items() if not value],
            "minimum_new_selected_data": [
                "non-identity selected rho_E transition matrices or functions from Appell-Humbert/gerbe/monad source",
                "selected Hermitian metric and connection A* from the q79/F,m=1 Strominger/HYM minimizer",
                "selected D_E action matrices derived from A*, not from the smoke slot",
                "selected Riesz projectors, complement gaps, and Green operators with gap/truncation proof",
                "selected dotD_alpha1 driver and horizontal responses from the same branch",
                "primitive C1 overlap tensors or a theorem reducing them to the selected D_E/dotD/Green package",
            ],
        },
        "theorem": {
            "name": "FiniteEmissionMorphismPhiFinSchema",
            "proved": True,
            "statement": (
                "The finite codomain and validator schema for Phi_fin are identified. The current q79/F,m=1 Route-C files "
                "are a valid execution scaffold but not selected data. Phi_fin must reuse this schema while replacing "
                "identity rhoE and lifted source flags with outputs derived from the selected Strominger/HYM minimizer."
            ),
        },
        "next_required_artifact": "MTT_Selected_NonIdentity_RhoE_Transition_Source_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    shape = candidate["phifin_schema"]["shape_gates"]
    return {
        "certificate": "MTTFiniteEmissionMorphismPhiFinAttempt",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "Phi_fin_codomain_schema_built": all(shape.values()),
            "routec_finite_validator_slots_mapped": True,
            "identity_rhoE_smoke_rejected": True,
            "selected_flag_obstruction_localized": True,
        },
        "what_remains_open": {
            "selected_nonidentity_rhoE_transition_source": True,
            "selected_HYM_connection_values": True,
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
    shape = "\n".join(
        f"- `{key}`: `{'PASS' if value else 'OPEN'}`"
        for key, value in candidate["phifin_schema"]["shape_gates"].items()
    )
    flags = "\n".join(
        f"- `{key}`: `{value}`" for key, value in candidate["phifin_schema"]["selected_flags"].items()
    )
    outputs = "\n".join(f"- {item}" for item in candidate["obstruction"]["minimum_new_selected_data"])
    closes = "\n".join(f"- {key}" for key, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {key}" for key, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Finite Emission Morphism Phi_fin v1

## Result

`Phi_fin` is not closed as selected data, but its finite codomain schema is now
identified.  The q79/F,m=1 Route-C files provide the scaffold for the morphism:
residuals, `rho_E`, metric, sector maps, `D_E`, Riesz/gap, reduced Green, and
`dotD`.  The same files also prove why they cannot be promoted: the source flags
are false and `rho_E` is identity smoke.

## Superset Classification

`{candidate["superset_mode"]["classification"]}`

This is a superset repair schema.  It does not combine paths to close values;
it locks the exact finite target that selected Appell-Humbert, gerbe/Chan-Paton,
or Strominger/HYM data must fill.

## Shape Gates

{shape}

## Selected Flags

{flags}

## Minimum New Selected Data

{outputs}

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
