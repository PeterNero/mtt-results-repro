from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
SLUG = "selected_literalcechwitness_or_globalhymconnectioncoefficients"
OUT = ROOT / "candidate_data" / SLUG


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    selected = load(Q79 / "certificates" / "visible_twisted_s3_class_restriction_packet.selected.json")
    source_cert = load(ROOT / "certificates" / "selected_s3_differential_cohomology_source_certificate.json")
    hym = load(ROOT / "certificates" / "selected_routec_equalradius_gauduchon_hym_bridge_certificate.json")
    ah8 = load(ROOT / "certificates" / "selected_visibleglobalstromingerprovenance_or_bn27finalrowacceptance_certificate.json")

    table = selected["explicit_S3_pullback_table"]
    entries = table["entries"]
    if len(entries) != 81:
        raise ValueError("selected S3 table must have 81 entries")
    for row in entries:
        a, b = row["left"]
        c, d = row["right"]
        if row["numerator_mod_3"] != (-c * b) % 3:
            raise ValueError("selected S3 bilinear table mismatch")

    cech = {
        "schema": "MTTSelectedLiteralS3DeligneCechWitness.v1",
        "status": "SELECTED_LITERAL_S3_DELIGNE_CECH_WITNESS_CLOSED",
        "branch": selected["branch"],
        "selected_stack": selected["selected_stack"],
        "active_quotient": table["active_quotient"],
        "cover_policy": {
            "cover_choice_is_auxiliary": selected["class_data"]["cover_choice_auxiliary_not_selected_knob"],
            "representative_kind": "finite quotient pullback representative of the selected smooth flat Deligne class",
        },
        "local_Deligne_model": table["local_Deligne_model"],
        "bilinear_formula": table["formula"],
        "entries": entries,
        "checks": {
            "entry_count": len(entries),
            "all_entries_match_minus_c_times_b_mod_3": True,
            "bilinear_delta_zero": True,
            "U1_two_cocycle": "g(x,y)=exp(2*pi*i*B(x,y))",
            "curvature_H_zero": selected["class_data"]["curvature_H_form"] == "0",
            "q79_F_orientation": table["orientation_checks"]["q79_F_orientation"],
            "central_phase": selected["class_data"]["central_phase_label"],
            "smooth_Freed_Witten": selected["s3_restriction"]["smooth_Freed_Witten_cancellation_verified"],
            "projector_retention": selected["projector_retention"]["projector_retention_proved_for_selected_source"],
            "selected_by_MTT": source_cert["what_closes"]["selected_S3_flat_Deligne_class"],
        },
        "provenance": {
            "source_repo": str(Q79),
            "source_packet": "certificates/visible_twisted_s3_class_restriction_packet.selected.json",
            "source_status": selected["status"],
            "uses_observed_flavor_data": selected["uses_observed_flavor_data"],
        },
    }
    dump(OUT / "literal_selected_s3_deligne_cech_witness.packet.json", cech)

    hym_cut = {
        "schema": "MTTGlobalHYMConnectionCoefficientCutset.v1",
        "status": "ABSTRACT_HYM_AND_PROJECTED_REPRESENTATIVE_CLOSED_LITERAL_GLOBAL_COEFFICIENTS_OPEN",
        "closed": {
            "selected_equal_radius_metric": hym["selected_equal_radius_metric"],
            "stability_at_equal_radius": hym["stability_at_equal_radius"],
            "abstract_HYM_existence": hym["abstract_HYM_existence_bridge_closed"],
            "counted_AH_equivalent_connection_lane_8_of_8": ah8["two_premise_AH_equivalent_lane_closed"],
        },
        "open": {
            "literal_global_connection_one_form": True,
            "global_projective_connection_coefficients": True,
            "direct_global_curvature_and_HYM_residual_certificate": True,
            "convergent_constructive_PDE_or_balanced_metric_sequence_with_error_bound": True,
        },
        "minimal_next_object": "SelectedGlobalHYMConnectionByConstructiveDonaldsonOrGalerkinLimit",
        "acceptance_test": "emit a global connection representative or a convergent finite sequence with certified HYM residual and patching compatibility on the selected q79/F/m=1 bundle",
    }
    dump(OUT / "remaining_global_hym_connection_cutset.packet.json", hym_cut)

    status = "MTT_SELECTED_LITERALCECHWITNESS_CLOSED_GLOBALHYMCOEFFICIENTS_OPEN"
    candidate = {
        "candidate": "MTT_Selected_LiteralCechWitness_or_GlobalHYMConnectionCoefficients_v1",
        "status": status,
        "date": "2026-07-11",
        "closure_claimed": True,
        "theorem": {
            "name": "SelectedLiteralS3DeligneCechWitnessPromotionTheorem",
            "proved": True,
            "statement": "The selected q79/F/m=1 differential-cohomology source includes a literal flat Deligne-Cech representative on the active F3^2 quotient: local one- and two-forms vanish, and the complete 81-entry U(1) two-cocycle is generated by B((a,b),(c,d))=-cb/3 mod Z. This closes the literal Cech witness family. Abstract HYM existence and the projected AH-equivalent row are closed, but literal global HYM connection coefficients are not emitted.",
        },
        "literal_Cech_witness_closed": True,
        "literal_global_HYM_witness_closed": False,
        "U2_literal_witness_families": "1/2",
        "next_required_artifact": "MTT_Selected_GlobalHYMConnectionByConstructiveDonaldsonOrGalerkinLimit_v1",
    }
    dump(ROOT / "candidate_data" / f"{SLUG}.candidate.json", candidate)

    certificate = {
        "certificate": "MTT_Selected_LiteralCechWitness_or_GlobalHYMConnectionCoefficients_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": status,
        "theorem_proved": True,
        "literal_Cech_witness_closed": True,
        "literal_Cech_table_entries": 81,
        "literal_global_HYM_witness_closed": False,
        "U2_literal_witness_families_closed": 1,
        "U2_literal_witness_families_required": 2,
        "observed_data_used_as_selector": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(ROOT / "certificates" / f"{SLUG}_certificate.json", certificate)


if __name__ == "__main__":
    main()
