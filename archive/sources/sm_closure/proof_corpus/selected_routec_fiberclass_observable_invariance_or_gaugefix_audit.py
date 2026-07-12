"""Audit the fiber-class observable invariance / gauge-fix attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_fiberclass_observable_invariance_or_gaugefix.candidate.json"
CERT = REPO / "certificates" / "selected_routec_fiberclass_observable_invariance_or_gaugefix_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_FiberClass_Observable_Invariance_or_GaugeFix_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    path_a = data["path_A_observable_invariance"]
    path_b = data["path_B_absolute_gauge_fix"]
    combined = data["combined_result"]
    obs = path_a["fixed_shift_observables"]

    base = obs["0"]
    all_same = obs["1"] == base and obs["2"] == base
    all_scalar_identity = all(
        sector["YYstar_is_scalar_identity"] is True
        for by_shift in obs.values()
        for sector in by_shift.values()
    )
    all_rank3 = all(
        sector["rank"] == 3
        for by_shift in obs.values()
        for sector in by_shift.values()
    )

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_FIBERCLASS_OBSERVABLE_INVARIANCE_PROVED_GAUGEFIX_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "path A proved scoped invariance",
            path_a["proved_for_current_finite_C1_layer"] is True and all_same and all_scalar_identity and all_rank3,
            path_a,
        ),
        check(
            "path A does not overclaim flavor closure",
            path_a["does_not_prove_physical_flavor_closure"] is True
            and "degenerate" in path_a["why_not_physical_flavor_closure"],
            path_a,
        ),
        check(
            "path B remains open",
            path_b["attempted"] is True
            and path_b["proved"] is False
            and path_b["physical_absolute_origin_selected"] is False
            and path_b["canonical_computation_gauge"] == "fiber_shift_0",
            path_b,
        ),
        check(
            "combined result scoped",
            combined["selected_C1_observable_class_proved_at_current_layer"] is True
            and combined["selected_unique_C1_matrix_proved"] is False,
            combined,
        ),
        check(
            "open higher flavor splitting",
            data["what_remains_open"]["nondegenerate_yukawa_hierarchy"] is True
            and data["what_remains_open"]["CKM_PMNS_CP_from_selected_matrices"] is True,
            data["what_remains_open"],
        ),
        check(
            "no closure claim or target fit",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_HigherOrder_or_FullResponse_FlavorSplitting_v1",
            data["next_required_artifact"],
        ),
        check(
            "note records both paths",
            "Path A: Observable Invariance" in note
            and "Path B: Absolute Gauge Fix" in note
            and "does not close physical flavor" in note
            and "Shift `0` is therefore legal as a computation gauge" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C fiber-class observable invariance / gauge-fix audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
