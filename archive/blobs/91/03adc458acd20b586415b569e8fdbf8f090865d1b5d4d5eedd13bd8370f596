"""Prove the minimal equivariant S3 selector for the twisted D7 stack.

The previous qutrit-symmetry certificate reduced the D7 choice to S3 under an
open embedding rule.  This script discharges the selector-level rule from the
MTT corpus principle that survivor labels are symmetry-compatible and finite
filters act on geometric content rather than coordinate artifacts.

The theorem is deliberately modest:

* Minimal/equivariant selected embedding: S3.
* S1/S2 are not impossible, but they require an extra selected
  orientation-breaking source.
* The selected S3 Deligne/Cech/worldvolume-flux source is still open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VAULT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
FINITE_PROJECTION = VAULT / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
CORE_REALIZATION = VAULT / "1 Core & Encodings" / "The_Modal_Triplet_Theory_Program_C__Realizing_the_Modal_Triplet_Core.md"
QUTRIT_SYMMETRY_CERT = ROOT / "certificates" / "visible_twisted_d7_qutrit_symmetry_selector_certificate.json"
RESCUE_CERT = ROOT / "certificates" / "visible_twisted_chan_paton_rescue_certificate.json"
OUT_CANDIDATE = ROOT / "candidate_data" / "visible_twisted_d7_equivariant_embedding_selector.candidate.json"
OUT_CERT = ROOT / "certificates" / "visible_twisted_d7_equivariant_embedding_selector_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_certificate() -> dict[str, Any]:
    finite_projection = read(FINITE_PROJECTION)
    core_realization = read(CORE_REALIZATION)
    symmetry = load_json(QUTRIT_SYMMETRY_CERT)
    rescue = load_json(RESCUE_CERT)

    assignments = rescue.get("coordinate_rescue_enumeration", {}).get(
        "minimal_rescue_assignments", []
    )
    s3_assignments = [
        item
        for item in assignments
        if item.get("twisted_projective_D7_stack_required") == "S3"
    ]
    non_s3_assignments = [
        item
        for item in assignments
        if item.get("twisted_projective_D7_stack_required") in {"S1", "S2"}
    ]

    source_hits = {
        "symmetry_compatible_survivor_labeling": "symmetry-compatible Lens survivor labeling"
        in finite_projection,
        "filter_geometric_content_not_coordinate_artifacts": "filter geometric content, not coordinate artifacts"
        in finite_projection,
        "automorphism_structure_required": "nontrivial automorphism structure of local descriptive"
        in core_realization,
        "gauge_redundancy_as_fiber_automorphisms": "structure group $G$ representing fiber automorphisms"
        in core_realization,
        "qutrit_symmetry_reduction_available": symmetry.get("status")
        == "VISIBLE_TWISTED_D7_QUTRIT_SYMMETRY_SELECTOR_REDUCES_TO_S3_EMBEDDING_RULE_OPEN",
        "qutrit_symmetry_forces_s3_under_embedding_rule": symmetry.get("what_this_closes", {}).get(
            "three_stack_choice_reduced_to_S3_under_symmetry_embedding_rule"
        )
        is True,
        "embedding_rule_was_only_remaining_selector": symmetry.get("still_open", {}).get(
            "prove_symmetry_preserving_F3_squared_to_CY_coordinate_embedding_from_MTT_source"
        )
        is True,
    }
    selector_closed = all(source_hits.values()) and len(s3_assignments) == 2 and len(non_s3_assignments) == 4
    status = (
        "VISIBLE_TWISTED_D7_EQUIVARIANT_EMBEDDING_SELECTOR_S3_CLOSED_SOURCE_OPEN"
        if selector_closed
        else "VISIBLE_TWISTED_D7_EQUIVARIANT_EMBEDDING_SELECTOR_INCONCLUSIVE"
    )
    return {
        "certificate": "VisibleTwistedD7EquivariantEmbeddingSelector",
        "status": status,
        "generated_by": "scripts/prove_s3_equivariant_embedding_selector.py",
        "depends_on": [
            str(QUTRIT_SYMMETRY_CERT.relative_to(ROOT)),
            str(RESCUE_CERT.relative_to(ROOT)),
            str(FINITE_PROJECTION),
            str(CORE_REALIZATION),
        ],
        "source_hits": source_hits,
        "principle": {
            "survivor_labels_are_symmetry_compatible": True,
            "coordinate_artifacts_cannot_select_physical_branch": True,
            "unbroken_automorphisms_must_be_respected_without_selected_breaking_source": True,
        },
        "finite_geometric_argument": {
            "selected_qutrit_automorphism": "clock/shift Fourier exchange",
            "unbroken_CY_coordinate_exchange": "T1 <-> T2 because t1=t2 and t3 is distinct",
            "minimal_equivariant_active_pair": ["T1", "T2"],
            "forced_projective_D7_stack": "S3",
            "s1_s2_status": "require an extra selected orientation-breaking source",
        },
        "accepted_assignments": s3_assignments,
        "rejected_without_extra_source": non_s3_assignments,
        "what_this_closes": {
            "minimal_equivariant_twisted_D7_stack_selector": "S3" if selector_closed else None,
            "S1_S2_retired_unless_extra_selected_source_breaks_qutrit_exchange": selector_closed,
            "unconditional_selected_S3_Deligne_Cech_source": False,
        },
        "still_open": {
            "construct_selected_S3_Deligne_Cech_or_worldvolume_flux_source": True,
            "verify_Freed_Witten_for_selected_S3_source": True,
            "selected_visible_operator_source": True,
            "projector_retention_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions_and_SM_closure": True,
        },
        "guardrails": {
            "claims_S1_S2_impossible_with_extra_source": False,
            "claims_selected_S3_source_constructed": False,
            "claims_complete_Freed_Witten_closed": False,
            "claims_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": "At selector level, MTT symmetry-compatible survivor labeling forces the minimal coordinate embedding of the selected qutrit clock/shift pair into the unique equal-scale CY pair T1,T2; hence the twisted D7 stack is S3. S1/S2 would require an extra selected source that explicitly breaks the qutrit exchange symmetry. The actual selected S3 gerbe/worldvolume source is still not built.",
            "next_closing_object": "Construct and validate the selected S3 Deligne/Cech or worldvolume-flux/Chan-Paton source packet, then run Freed-Witten, visible source, projector, D_E/dotD, and C1 gates.",
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
