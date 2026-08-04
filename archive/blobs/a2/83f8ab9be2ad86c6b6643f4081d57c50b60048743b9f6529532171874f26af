from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_noninvariant_c1_primitive_search_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_primitive_source_selection_audit_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_primitive_source_selection_audit.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_primitive_source_selection_audit_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_primitive_source_selection_audit_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Primitive_Source_Selection_Audit_Import_v1.md"

STATUS = "ROUTEC_PRIMITIVE_SOURCE_SELECTION_AUDIT_IMPORTED_ACTIVE_SHIFT_FORCED_FIBER_CLASS_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_FiberClass_Observable_Invariance_or_GaugeFix_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)

    active_enum = src["active_shift_theorem"]["enumeration"]
    fixed = src["fiber_class_theorem"]["fixed_fiber_shifts"]
    envelope = src["fiber_class_theorem"]["all_fiber_envelope"]
    source_implication = src["source_implication"]

    closed_now = {
        "previous_noninvariant_C1_search_imported": prev["theorem"]["proved"],
        "source_theorem_proved": src["theorem"]["proved"],
        "active_shift_1_1_forced_by_finite_support": src_cert["what_closes"][
            "active_shift_1_1_forced_by_finite_support"
        ],
        "fixed_fiber_shifts_reduced_to_one_qutrit_gauge_class": src_cert["what_closes"][
            "fixed_fiber_shifts_reduced_to_one_qutrit_gauge_class"
        ],
        "all_fiber_envelope_retired_as_fixed_single_charge_candidate": src_cert["what_closes"][
            "all_fiber_envelope_retired_as_fixed_single_charge_candidate"
        ],
        "no_observed_flavor_data_used": src_cert["what_closes"]["no_observed_flavor_data_used"],
    }

    active_shift_checks = {
        "all_nine_active_shifts_tested": len(active_enum["all_active_shifts_tested"]) == 9,
        "only_nonzero_active_shift_is_1_1": active_enum["nonzero_active_shifts"] == [[1, 1]],
        "active_shift_necessary_and_sufficient": active_enum[
            "active_shift_necessary_and_sufficient_for_nonzero"
        ]
        is True,
    }

    fixed_shifts = {"0", "1", "2"}
    fixed_fiber_checks = {
        "fixed_shift_keys_are_0_1_2": set(fixed["ranks"]) == fixed_shifts,
        "fixed_shifts_all_rank_three_all_sectors": all(
            all(rank == 3 for rank in ranks.values()) for ranks in fixed["ranks"].values()
        ),
        "fixed_shifts_same_frobenius_norms_all_sectors": all(
            all(abs(value - 0.5922903530864667) < 1e-15 for value in norms.values())
            for norms in fixed["frobenius_norms"].values()
        ),
        "fixed_shifts_equivalent_to_shift_0": all(
            item["equivalent"] is True for item in fixed["equivalence_to_shift_0_on_u"].values()
        ),
    }

    envelope_checks = {
        "all_fiber_envelope_rank_one_all_sectors": all(rank == 1 for rank in envelope["rank"].values()),
        "all_fiber_envelope_not_gauge_equivalent": envelope[
            "not_gauge_equivalent_to_fixed_fiber_class"
        ]
        is True,
        "all_fiber_envelope_all_ones_support": envelope["support_pattern_u"]
        == [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    }

    open_gate_checks = {
        "absolute_fiber_origin_still_unselected": source_implication["absolute_fiber_shift_selected"] is False,
        "observable_invariance_not_proved": source_implication[
            "observable_invariance_under_fiber_class_proved"
        ]
        is False,
        "selected_noninvariant_primitive_source_not_proved": source_implication[
            "selected_noninvariant_primitive_source_proved"
        ]
        is False,
        "operator_level_projective_class_not_selected": source_implication["qutrit_source_support"][
            "operator_level_projective_class_selected"
        ]
        is False,
        "source_level_projective_class_selected": source_implication["qutrit_source_support"][
            "source_level_projective_class_selected"
        ]
        is True,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "next_artifact_is_fiberclass_observable_or_gaugefix": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    still_open_checks = {
        key: value is True for key, value in src["what_remains_open"].items()
    }

    theorem = {
        "name": "RouteCPrimitiveSourceSelectionAuditImportTheorem",
        "proved": all(closed_now.values())
        and all(active_shift_checks.values())
        and all(fixed_fiber_checks.values())
        and all(envelope_checks.values())
        and all(open_gate_checks.values())
        and all(still_open_checks.values()),
        "statement": (
            "The imported Route-C source-selection audit proves that finite support "
            "forces active shift (1,1), that fixed qutrit fiber shifts 0,1,2 form "
            "one cyclic gauge class with rank-three C1 matrices, and that the "
            "all-fiber envelope is a structurally distinct rank-one object. The "
            "selected C1 gate is therefore reduced to a selected fiber-origin "
            "gauge fix, observable invariance under the fixed-fiber class, or an "
            "equivalent selected primitive/basis-transport source theorem."
        ),
    }

    verdict = {
        "active_shift_forced": True,
        "forced_active_shift": [1, 1],
        "fixed_fiber_class_reduced": True,
        "fixed_fiber_shifts": [0, 1, 2],
        "all_fiber_envelope_retired": True,
        "all_fiber_envelope_rank": 1,
        "absolute_fiber_origin_selected": False,
        "observable_invariance_proved": False,
        "selected_C1_source_closed": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "closed_now": closed_now,
        "active_shift_checks": active_shift_checks,
        "fixed_fiber_checks": fixed_fiber_checks,
        "envelope_checks": envelope_checks,
        "open_gate_checks": open_gate_checks,
        "still_open_checks": still_open_checks,
        "active_shift_theorem": src["active_shift_theorem"],
        "fiber_class_theorem": src["fiber_class_theorem"],
        "source_implication": source_implication,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Primitive Source Selection Audit Import v1

## Result

The Route-C primitive source-selection / fiber-rule audit is now imported.

It proves three finite, target-independent facts:

1. Active shift `(1,1)` is forced by exhaustive finite-support enumeration.
2. Fixed qutrit fiber shifts `0`, `1`, and `2` form one cyclic fiber gauge class.
3. The `all` fiber envelope is rank one and is retired as a fixed single-charge primitive.

The fixed-fiber class gives rank-three `u,d,e,nuD` candidate matrices. The
all-fiber envelope gives rank-one all-ones support, so it is structurally
different from a fixed qutrit-charge primitive.

## Boundary

This still does not select an absolute fiber origin and does not close selected
C1. The imported source data select the period-three projective qutrit class,
not a unique operator-level primitive.

No observed Yukawa, CKM, PMNS, or mass data were used.

## Status

```text
ROUTEC_PRIMITIVE_SOURCE_SELECTION_AUDIT_IMPORTED_ACTIVE_SHIFT_FORCED_FIBER_CLASS_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_FiberClass_Observable_Invariance_or_GaugeFix_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_primitive_source_selection_audit_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_noninvariant_c1_primitive_search_import": str(PREV_IMPORT),
                    "selected_routec_primitive_source_selection_audit": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "active_shift_checks": active_shift_checks,
                "fixed_fiber_checks": fixed_fiber_checks,
                "envelope_checks": envelope_checks,
                "open_gate_checks": open_gate_checks,
                "still_open_checks": still_open_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
