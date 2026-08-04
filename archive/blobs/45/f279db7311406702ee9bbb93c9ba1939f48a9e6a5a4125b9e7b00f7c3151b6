"""Build the true-SM-equivalence frontier after SM-parity closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_true_sm_equivalence_frontier_after_smparityclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FRONTIER = PACKET_DIR / "true_sm_equivalence_frontier_matrix.packet.json"
PLAN = PACKET_DIR / "next_executable_superset_plan.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TrueSMEquivalenceFrontier_AfterSMParityClosure_v1.md"

STATUS = "MTT_SELECTED_TRUE_SM_EQUIVALENCE_FRONTIER_AFTER_SMPARITYCLOSURE_BUILT"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    closure = load(DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json")
    decision = load(
        DATA
        / "selected_qasu3sourcepacket_or_finalsmparityclosure"
        / "sm_parity_closure_decision.packet.json"
    )

    frontier = {
        "schema": "MTTTrueSMEquivalenceFrontierAfterSMParityClosure.v1",
        "status": "TRUE_SM_EQUIVALENCE_FRONTIER_OPEN_AFTER_SM_PARITY_CLOSURE",
        "starting_point": {
            "SM_parity_closed": decision["SM_parity_closed"],
            "true_SM_equivalence_closed": decision["true_SM_equivalence_closed"],
            "no_knob_closed": decision["no_knob_closed"],
            "current_SM_parity_blockers": decision["current_SM_parity_blockers"],
        },
        "true_equivalence_gates": [
            {
                "id": "precision_empirical_replay_suite",
                "tier": "true_SM_equivalence",
                "status": "OPEN_PRIMARY_NEXT",
                "goal": "Replace first-pass central replay with a declared precision replay suite: scale policy, pole-to-running maps, threshold policy, benchmark RG transport, and covariance/profile handling.",
                "why_next": "This is the most external-reviewable gap and does not require no-knob constants.",
                "superset_strategy": "combine measured-SM replay lane with external SM/QFT RG conventions and local MTT typed parameter slots; lock to benchmark reproducibility, not source selection",
            },
            {
                "id": "local_qft_observable_functor",
                "tier": "true_SM_equivalence",
                "status": "OPEN",
                "goal": "Emit a typed functor from MTT sector packets and admitted parameters to local QFT observables/correlation amplitudes.",
                "why_not_first": "More conceptual than the precision replay suite; should be constrained by the empirical replay interface first.",
                "superset_strategy": "combine QFT formalism, MTT operator-exit ledgers, and selected source packets into a functorial interface",
            },
            {
                "id": "qm_gr_measurement_and_born_record_interfaces",
                "tier": "true_SM_equivalence",
                "status": "OPEN",
                "goal": "State and audit the QM measurement/Born-record and GR response interfaces used when comparing to actual observables.",
                "why_not_first": "Needed for complete physics equivalence, but the SM numerical sector can be tightened first.",
                "superset_strategy": "combine corpus fixed-point/projection language, protospinor GR-response artifacts, and measured boundary-condition policy",
            },
            {
                "id": "actual_qasu3_operator_packet_upgrade",
                "tier": "true_SM_equivalence_to_no_knob_bridge",
                "status": "OPEN",
                "goal": "Replace the parity-interface Qa/SU3 replacement with actual selected D_E/rho_E operator maps and Bianchi/Freed-Witten/anomaly certificate.",
                "why_not_first": "Harder source-selection problem; keep active as parallel superset lane while precision replay is made externally reproducible.",
                "superset_strategy": "combine typed monad/section-ring data, same-source visible/color packet, HYM/Route-C, and finite cochain lanes",
            },
            {
                "id": "no_knob_constants",
                "tier": "beyond_true_SM_equivalence",
                "status": "OPEN_SEPARATE",
                "goal": "Derive SM constants instead of admitting measured values.",
                "why_not_first": "This exceeds SM-equivalence because the SM itself admits these as measured inputs.",
                "superset_strategy": "use no-knob repos and constant-specific encodings only after true-equivalence replay is tight",
            },
        ],
        "not_blocking_true_equivalence": [
            "no-knob derivation of measured SM constants",
            "full cosmological parameter derivation",
            "absolute dimensionful normalization beyond the declared comparison convention",
        ],
        "guardrails": {
            "SM_parity_already_closed": True,
            "do_not_reopen_SM_parity_as_if_failed": True,
            "measured_values_remain_downstream_inputs": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "no_knob_claimed": False,
        },
    }

    plan = {
        "schema": "MTTNextExecutableSupersetPlan.v1",
        "status": "NEXT_EXECUTABLE_PLAN_SELECTED_PRECISION_EMPIRICAL_REPLAY_SUITE",
        "selected_next_gate": "precision_empirical_replay_suite",
        "reason": (
            "After SM-parity closure, the cleanest route toward true SM equivalence is to make the "
            "measured replay layer precision-grade and externally benchmarkable before attacking the "
            "harder no-knob/source-operator upgrade."
        ),
        "work_items": [
            {
                "id": "P1_rg_scheme_lock",
                "output": "declared scheme/scale/loop-order/threshold convention packet",
                "success_condition": "all masses, Yukawas, Higgs, gauge values, CKM/PMNS slots have declared reference scales and schemes",
            },
            {
                "id": "P2_pole_running_threshold_tables",
                "output": "machine-readable mass-scheme and threshold table with provenance sidecars",
                "success_condition": "native replay values can be transported or explicitly held under a justified convention",
            },
            {
                "id": "P3_external_rg_benchmark",
                "output": "benchmark comparison contract against a named SM/QFT convention or independent implementation",
                "success_condition": "local RG transport is reproducible and deviations are bounded under the declared first precision tier",
            },
            {
                "id": "P4_covariance_profile_policy",
                "output": "central-value plus covariance/profile likelihood policy packet",
                "success_condition": "central replay, uncertainty sidecars, and correlated-fit limits are separated",
            },
            {
                "id": "P5_true_equivalence_audit",
                "output": "sector-by-sector true-SM-equivalence audit",
                "success_condition": "remaining true-equivalence blockers are local QFT/QM/GR interfaces and actual source upgrade, not numerical replay bookkeeping",
            },
        ],
        "parallel_superset_lane": {
            "id": "actual_qasu3_operator_packet_upgrade",
            "keep_active": True,
            "rule": "Use typed monad/section-ring, HYM/Route-C, and same-source visible/color artifacts for source upgrade, but do not let this block precision replay work.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTrueSMEquivalenceFrontierAfterSMParityClosure",
        "status": STATUS,
        "inputs": {
            "final_sm_parity_closure": rel(DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"),
            "sm_parity_closure_decision": rel(
                DATA
                / "selected_qasu3sourcepacket_or_finalsmparityclosure"
                / "sm_parity_closure_decision.packet.json"
            ),
        },
        "output_packets": {
            "true_sm_equivalence_frontier_matrix": rel(FRONTIER),
            "next_executable_superset_plan": rel(PLAN),
        },
        "theorem": {
            "name": "TrueSMEquivalenceFrontierAfterSMParityClosureTheorem",
            "proved": True,
            "statement": (
                "Once SM-parity is closed, true SM equivalence reduces to precision replay, local "
                "QFT/QM/GR observable interfaces, and replacing parity-interface source packets with "
                "actual selected source/operator packets. No-knob derivation of measured constants is "
                "a stronger separate goal and must not be confused with true SM equivalence."
            ),
        },
        "what_closes_now": {
            "post_SM_parity_frontier_identified": True,
            "true_equivalence_gates_ranked": True,
            "precision_empirical_replay_suite_selected_as_next_gate": True,
            "superset_strategy_explicitly_locked": True,
        },
        "what_remains_open": {
            "precision_empirical_replay_suite": True,
            "local_qft_observable_functor": True,
            "qm_gr_measurement_and_born_record_interfaces": True,
            "actual_qasu3_operator_packet_upgrade": True,
            "no_knob_constants": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_TrueSMEquivalenceFrontier_AfterSMParityClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "selected_next_gate": "precision_empirical_replay_suite",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = """# MTT Selected TrueSMEquivalenceFrontier After SMParityClosure v1

Status: `MTT_SELECTED_TRUE_SM_EQUIVALENCE_FRONTIER_AFTER_SMPARITYCLOSURE_BUILT`.

SM-parity is closed under the declared parity-interface standard. The next
target is not to redo that closure; it is to push from parity to true SM
equivalence.

## Next Gate

The selected next gate is `precision_empirical_replay_suite`.

This uses a superset strategy: combine measured-SM replay conventions, QFT/RG
benchmark practice, and MTT typed parameter slots, then lock the target to
external reproducibility. This is not a no-knob constants claim and does not use
observed values as source selectors.

## Parallel Lane

Keep the actual Qa/SU3 operator upgrade active in parallel through typed
monad/section-ring, HYM/Route-C, finite cochain, and same-source visible/color
lanes. That lane is essential for no-knob/source strengthening, but it should
not block the precision replay suite.
"""

    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PLAN.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
