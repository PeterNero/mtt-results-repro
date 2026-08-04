"""Reduce the twisted D7 choice using qutrit clock/shift symmetry.

The volume selector singled out S3 as the unique anisotropic/small-volume
candidate, but left open the rule selecting that candidate.  This script tests
the stronger finite-geometric reduction:

1. the selected gerbe-Fourier type supplies the nontrivial qutrit phase space;
2. the selected qutrit cycle packet supplies the clock and shift lines;
3. clock and shift are Fourier-dual, hence symmetric before a selected
   orientation/source breaks that symmetry;
4. a coordinate embedding that preserves this qutrit symmetry can map the two
   active generators only to equal-scale coordinate factors;
5. in the executed CY corner the only equal-scale pair is T1,T2;
6. the finite twisted Chan-Paton rescue then forces the twisted D7 stack to be
   S3.

This is still a reduction, not a final source theorem: the symmetry-preserving
embedding rule must be proved from the selected MTT source or replaced by an
explicit geometric Deligne/Cech/worldvolume-flux source.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FOURIER_TYPE_CERT = ROOT / "certificates" / "selected_gerbe_fourier_type_theorem_certificate.json"
QUTRIT_TRANSPORT_CERT = ROOT / "certificates" / "qutrit_polarization_transport_lemma_certificate.json"
QUTRIT_LINES_CERT = ROOT / "certificates" / "time_oriented_m1_qutrit_line_cycle_restrictions_certificate.json"
RESCUE_CERT = ROOT / "certificates" / "visible_twisted_chan_paton_rescue_certificate.json"
VOLUME_SELECTOR_CERT = ROOT / "certificates" / "visible_twisted_d7_volume_selector_attempt_certificate.json"
OUT_CANDIDATE = ROOT / "candidate_data" / "visible_twisted_d7_qutrit_symmetry_selector.candidate.json"
OUT_CERT = ROOT / "certificates" / "visible_twisted_d7_qutrit_symmetry_selector_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def pair_key(a: str, b: str) -> str:
    return ",".join(sorted([a, b]))


def build_certificate() -> dict[str, Any]:
    fourier = load_json(FOURIER_TYPE_CERT)
    transport = load_json(QUTRIT_TRANSPORT_CERT)
    lines = load_json(QUTRIT_LINES_CERT)
    rescue = load_json(RESCUE_CERT)
    volume = load_json(VOLUME_SELECTOR_CERT)

    vol_data = volume.get("executed_volume_data", {}).get("computed_from_tier3", {})
    t_values = {
        "T1": vol_data.get("t1"),
        "T2": vol_data.get("t2"),
        "T3": vol_data.get("t3"),
    }
    equal_scale_pairs: list[dict[str, Any]] = []
    factors = list(t_values)
    for i, left in enumerate(factors):
        for right in factors[i + 1 :]:
            delta = abs(float(t_values[left]) - float(t_values[right]))
            if delta < 1e-12:
                equal_scale_pairs.append({"pair": [left, right], "delta": delta})

    assignments = rescue.get("coordinate_rescue_enumeration", {}).get(
        "minimal_rescue_assignments", []
    )
    allowed_by_symmetry = []
    for assignment in assignments:
        factors_for_generators = assignment.get("generator_factor_assignment", {})
        e1_factor = factors_for_generators.get("e1")
        e2_factor = factors_for_generators.get("e2")
        if pair_key(e1_factor, e2_factor) == "T1,T2":
            allowed_by_symmetry.append(assignment)

    selected_stacks = sorted(
        {
            item.get("twisted_projective_D7_stack_required")
            for item in allowed_by_symmetry
            if item.get("twisted_projective_D7_stack_required")
        }
    )
    source_hits = {
        "selected_gerbe_fourier_type_closed": fourier.get("status")
        == "SELECTED_GERBE_FOURIER_TYPE_PROVED_SU5_PACKET_OPEN",
        "nontrivial_qutrit_type_selected": fourier.get("what_this_proves", {}).get(
            "nontrivial_Z3_flat_gerbe_type_selected_as_MTT_family_phase_space"
        )
        is True,
        "clock_shift_transport_proved": transport.get("what_this_closes", {}).get(
            "finite_qutrit_clock_shift_transport"
        )
        is True,
        "clock_shift_unique_up_to_orientation": transport.get("what_this_closes", {}).get(
            "uniqueness_up_to_conjugate_orientation_and_rephasing"
        )
        is True,
        "selected_clock_shift_lines_validate": lines.get("calculation_results", {}).get(
            "qutrit_clock_shift_line_packet_validates"
        )
        is True,
        "s3_volume_selector_available": volume.get("status")
        == "VISIBLE_TWISTED_D7_VOLUME_SELECTOR_ATTEMPT_S3_CONDITIONAL_SELECTION_OPEN",
        "rescue_family_reduced": rescue.get("status")
        == "VISIBLE_TWISTED_CP_MINIMAL_COORDINATE_RESCUE_REDUCED_SELECTION_OPEN",
    }
    symmetry_reduction_works = (
        all(source_hits.values())
        and equal_scale_pairs == [{"pair": ["T1", "T2"], "delta": 0.0}]
        and selected_stacks == ["S3"]
        and len(allowed_by_symmetry) == 2
    )
    status = (
        "VISIBLE_TWISTED_D7_QUTRIT_SYMMETRY_SELECTOR_REDUCES_TO_S3_EMBEDDING_RULE_OPEN"
        if symmetry_reduction_works
        else "VISIBLE_TWISTED_D7_QUTRIT_SYMMETRY_SELECTOR_INCONCLUSIVE"
    )
    return {
        "certificate": "VisibleTwistedD7QutritSymmetrySelector",
        "status": status,
        "generated_by": "scripts/derive_s3_selector_from_qutrit_symmetry.py",
        "depends_on": [
            str(FOURIER_TYPE_CERT.relative_to(ROOT)),
            str(QUTRIT_TRANSPORT_CERT.relative_to(ROOT)),
            str(QUTRIT_LINES_CERT.relative_to(ROOT)),
            str(RESCUE_CERT.relative_to(ROOT)),
            str(VOLUME_SELECTOR_CERT.relative_to(ROOT)),
        ],
        "source_hits": source_hits,
        "qutrit_symmetry_input": {
            "selected_lines": ["clock <e1>", "shift <e2>"],
            "finite_transport": "clock and shift are related by the qutrit Fourier matrix",
            "orientation_status": "global F versus F-conjugate orientation remains open upstream",
            "embedding_principle_still_to_prove": "a selected coordinate embedding must preserve the clock/shift exchange symmetry unless the selected source supplies an orientation-breaking datum",
        },
        "executed_coordinate_scales": t_values,
        "equal_scale_pairs": equal_scale_pairs,
        "allowed_generator_factor_assignments_under_symmetry": allowed_by_symmetry,
        "forced_twisted_stack_if_embedding_rule_is_proved": selected_stacks[0]
        if len(selected_stacks) == 1
        else None,
        "notation_guard": {
            "central_phase_zeta3_root_and_tier3_zeta_ratio_are_distinct_data": True,
            "uses_symbol_collision_as_proof": False,
            "uses_common_numeric_0_229_only_after_volume_map": True,
        },
        "what_this_closes": {
            "three_stack_choice_reduced_to_S3_under_symmetry_embedding_rule": symmetry_reduction_works,
            "S1_S2_rejected_under_symmetry_embedding_rule": symmetry_reduction_works,
            "unconditional_selected_geometric_source_for_S3": False,
        },
        "still_open": {
            "prove_symmetry_preserving_F3_squared_to_CY_coordinate_embedding_from_MTT_source": True,
            "construct_selected_S3_Deligne_Cech_or_worldvolume_flux_source": True,
            "Freed_Witten_for_selected_S3_source": True,
            "selected_visible_operator_source": True,
            "projector_retention_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions_and_SM_closure": True,
        },
        "guardrails": {
            "claims_unconditional_S3_source": False,
            "claims_embedding_rule_already_proved": False,
            "claims_complete_Freed_Witten_closed": False,
            "claims_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": "Current certificates reduce the D7 choice to S3 if the selected finite qutrit clock/shift pair must embed into the unique equal-scale CY coordinate pair T1,T2. This is stronger than a bare volume hunch, but the embedding rule itself remains the next theorem or source packet to prove.",
            "next_closing_object": "Prove the symmetry-preserving F_3^2 -> CY coordinate embedding from the selected MTT source, or construct an explicit selected S3 Deligne/Cech/worldvolume-flux packet that makes the embedding unnecessary.",
        },
    }


def main() -> int:
    data = build_certificate()
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0 if "INCONCLUSIVE" not in data["status"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
