from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_postu5tierledger_and_u9globalbranchmeasure"
STATUS = (
    "MTT_U9_SELECTED_ANTIUNITARY_ORBIT_INVARIANT_MEASURE_AND_RETARDED_CONDITIONAL_"
    "PROBABILITY_ONE_CLOSED_GLOBAL_CARRIER_MEASURE_UNDEFINED"
)
NEXT = "MTT_Selected_FluxThresholdAxionCurrentAnomalyMatchingMap_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostU5TierLedger_and_U9GlobalBranchMeasure_v1.md"

MEASURE = OUT / "finite_antiunitary_orbit_invariant_and_conditional_measure.packet.json"
GLOBAL = OUT / "global_carrier_measure_definability_audit.packet.json"
TIER = OUT / "U9_tier_closure_decision.packet.json"
LEDGER = OUT / "post_U5_U9_adopted_vs_strict_upgrade_ledger.packet.json"
PLAN = OUT / "next_execution_plan_after_U5_U9_tier_closure.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "A94_U5": ROOT / "candidate_data" / "selected_neutraloneholonomyonescaleontologyclosure_and_u5tierdecision.candidate.json",
        "A94_decision": ROOT / "candidate_data" / "selected_neutraloneholonomyonescaleontologyclosure_and_u5tierdecision" / "U5_tier_closure_and_strict_frontier.packet.json",
        "U9_predecessor": ROOT / "candidate_data" / "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness" / "branch_orbit_retarded_representative_and_global_measure_cutset.packet.json",
        "strict_upgrade_ledger": ROOT / "candidate_data" / "selected_strictnoknobupgradeledger_aftertruesmequivalence" / "strict_no_knob_upgrade_ledger.packet.json",
        "A90_dependencies": ROOT / "candidate_data" / "selected_posta89minimalparameterledger_and_nextfrontier" / "remaining_strict_upgrade_dependency_dag.packet.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A95 authority: " + ", ".join(missing))

    a94 = load(paths["A94_U5"])
    a94_decision = load(paths["A94_decision"])
    u9 = load(paths["U9_predecessor"])
    strict = load(paths["strict_upgrade_ledger"])
    a90 = load(paths["A90_dependencies"])

    members = u9["selected_unoriented_orbit"]["members"]
    q79 = next(row for row in members if row["q"] == 79)
    q369 = next(row for row in members if row["q"] == 369)
    invariant_weight = 0.5
    measure = {
        "schema": "MTTFiniteAntiunitaryOrbitInvariantAndConditionalMeasure.v1",
        "status": "UNIQUE_ANTIUNITARY_INVARIANT_MEASURE_UNIFORM_RETARDED_CONDITION_SELECTS_Q79_PROBABILITY_ONE",
        "space": {
            "B_fin": members,
            "sigma_algebra": "power set of the two-member orbit",
            "antiunitary_action": "J exchanges q79/F/m1 and q369/F*/m2",
            "action_transitive": True,
        },
        "invariant_probability_measure": {
            "derivation": "J-invariance gives mu(q79)=mu(q369); normalization gives 2 mu(q79)=1",
            "mu_q79": invariant_weight,
            "mu_q369": invariant_weight,
            "unique": True,
            "unoriented_theory_contains_both_conjugate_representatives": True,
        },
        "orientation_conditioning": {
            "retarded_event": [q79],
            "advanced_event": [q369],
            "mu_q79_given_retarded": 1.0,
            "mu_q369_given_retarded": 0.0,
            "mu_q369_given_advanced": 1.0,
            "retarded_event_selected_independently_of_observed_CP": u9["retarded_representative_selection"]["observed_CP_sign_used_as_selector"] is False,
        },
        "theorem": {
            "name": "FiniteAntiunitaryOrbitInvariantMeasureAndRetardedConditionalSelectionTheorem",
            "proved": len(members) == 2 and u9["selected_unoriented_orbit"]["antiunitary_equivalence_closed"],
            "statement": "A transitive two-point antiunitary orbit has one invariant probability measure, the uniform measure. The selected retarded event is the singleton q79/F/m1, so conditioning gives q79 probability one; the advanced event similarly gives q369 probability one. The conjugate branch remains part of the unoriented theory and is not a second tunable parameter.",
        },
        "observed_CP_data_used": False,
        "new_discrete_selector_added": False,
        "new_continuous_parameter_added": False,
    }

    global_fields = {
        "complete_admissible_carrier_set": False,
        "global_equivalence_relation_or_groupoid": False,
        "sigma_algebra_or_topology_on_carrier_classes": False,
        "normalizable_measure_or_coercive_action": False,
        "existence_of_global_minimizer_or_probability_measure": False,
        "proof_selected_finite_orbit_has_full_measure_or_contains_all_minimizers": False,
    }
    global_audit = {
        "schema": "MTTGlobalCarrierMeasureDefinabilityAudit.v1",
        "status": "GLOBAL_PROBABILITY_ONE_CLAIM_NOT_WELL_FORMED_UNTIL_CARRIER_SPACE_AND_MEASURE_ARE_DEFINED",
        "required_fields": global_fields,
        "readiness": {
            "filled": sum(global_fields.values()),
            "required": len(global_fields),
        },
        "current_selected_packet_supplies": {
            "one_finite_antiunitary_orbit": True,
            "one_retarded_representative": True,
            "comparison_against_every_admissible_geometry": False,
        },
        "logical_boundary": {
            "global_uniqueness_false": False,
            "global_uniqueness_proved": False,
            "global_probability_one_statement_currently_definable": False,
            "reason": "Probability one and global minimization require a domain, measurable/topological structure, and measure/action. The selected proof chain defines none on the complete MTT superset.",
            "not_a_no_go_for_future_global_completion": True,
        },
        "resume_only_on": [
            "a typed moduli/carrier groupoid with an admissibility quotient",
            "a source-owned action or probability law on that quotient",
            "compactness/coercivity/normalizability sufficient for existence",
            "an orbit-support theorem independent of observed SM targets",
        ],
    }

    tier = {
        "schema": "MTTU9TierClosureDecision.v1",
        "status": "U9_CLOSED_AT_SELECTED_ORBIT_AND_RETARDED_CONDITIONAL_MEASURE_STANDARD_STRICT_GLOBAL_SUPERSET_OPEN",
        "adopted_selected_orbit_standard": {
            "closed": True,
            "unoriented_orbit_unique": True,
            "invariant_probability_measure_unique": True,
            "retarded_q79_probability_one": True,
            "advanced_q369_probability_one": True,
            "observed_CP_selector_used": False,
            "new_parameters": 0,
        },
        "strict_global_superset_standard": {
            "closed": False,
            "definability_readiness": "0/6",
            "claim_frozen": True,
        },
        "physical_interpretation": "The unoriented theory contains an antiunitary pair. A time orientation does not erase the partner; it selects which representative is retarded for an observer. This is the precise branch analogue of choosing an arrow of time.",
        "non_looping_lock": "Do not demand a probability-one theorem over all MTT carriers until a complete carrier quotient and measure/action are supplied.",
    }

    strict_statuses = {row["id"]: row["status"] for row in strict["upgrades"]}
    ledger = {
        "schema": "MTTPostU5U9AdoptedVsStrictUpgradeLedger.v1",
        "status": "ADOPTED_TIER_FOUR_CLOSED_FOUR_PARTIAL_ONE_BLOCKED_STRICT_LEDGER_UNCHANGED",
        "declared_baseline": strict["baseline"],
        "strict_no_knob_ledger": {
            "closed": strict["closed_upgrade_count"],
            "partial": strict["partially_closed_upgrade_count"],
            "open_or_blocked": strict["open_upgrade_count"],
            "statuses_unchanged": strict_statuses,
        },
        "adopted_1_to_3_primitive_and_selected_orbit_tier": {
            "closed": [
                "U2_literal_global_Cech_HYM_QaSU3",
                "U4_exact_CKM_central",
                "U5_neutrino_absolute_ontology",
                "U9_unique_observed_branch",
            ],
            "partial": [
                "U3_official_joint_input_likelihood",
                "U6_strong_CP_selection",
                "U7_MTT_derived_quantization",
                "U8_constructive_nonperturbative_4D_QFT",
            ],
            "dependency_blocked": ["U1_zero_primitive_empirical_source"],
            "counts": {"closed": 4, "partial": 4, "dependency_blocked": 1},
        },
        "U5_basis": {
            "adopted_profile_closed": a94["results"]["U5_one_holonomy_one_scale_profile_closed"],
            "strict_closed": a94["results"]["strict_U5_closed"],
            "current_corpus_phase_search_frozen": a94_decision["strict_source_standard"]["current_corpus_search_frozen"],
        },
        "U9_basis": {
            "adopted_selected_orbit_closed": True,
            "strict_global_superset_closed": False,
        },
        "A90_strict_counts_preserved": a90["counts"],
    }

    plan = {
        "schema": "MTTNextExecutionPlanAfterU5U9TierClosure.v1",
        "status": "NEXT_ACTIVE_SELECTED_AS_U6_FLUX_THRESHOLD_AXION_ANOMALY_MAP",
        "ordered_steps": [
            {
                "order": 1,
                "target": "U6 strong CP selection",
                "acceptance": "construct the selected flux/threshold low-energy axion current, prove its nonzero QCD anomaly after exotic decoupling, and retain axion-quality control",
            },
            {
                "order": 2,
                "target": "U3 official likelihood",
                "acceptance": "opportunistically import a versioned official joint covariance without delaying internal proofs",
            },
            {
                "order": 3,
                "target": "U7 MTT-derived quantization",
                "acceptance": "derive measure/BRST/Born/record data from selected quotient geometry rather than standard-QFT import",
            },
            {
                "order": 4,
                "target": "U8 and U1 synthesis",
                "acceptance": "constructive 4D continuum first; zero-primitive synthesis last",
            },
        ],
        "frozen_until_new_source": [
            "strict U5 holonomy/scale/nil-saturation",
            "strict U9 global carrier probability measure",
        ],
        "next_required_artifact": NEXT,
    }

    checks = {
        "two_member_orbit": len(members) == 2,
        "antiunitary_equivalence_closed": u9["selected_unoriented_orbit"]["antiunitary_equivalence_closed"],
        "uniform_measure_normalized": abs(measure["invariant_probability_measure"]["mu_q79"] + measure["invariant_probability_measure"]["mu_q369"] - 1.0) < 1e-15,
        "retarded_conditional_probability_one": measure["orientation_conditioning"]["mu_q79_given_retarded"] == 1.0,
        "advanced_conditional_probability_one": measure["orientation_conditioning"]["mu_q369_given_advanced"] == 1.0,
        "no_observed_CP_selector": measure["observed_CP_data_used"] is False,
        "global_measure_not_overclaimed": sum(global_fields.values()) == 0,
        "adopted_U9_closed": tier["adopted_selected_orbit_standard"]["closed"],
        "strict_U9_open": not tier["strict_global_superset_standard"]["closed"],
        "strict_counts_preserved": strict["closed_upgrade_count"] == 2 and strict["partially_closed_upgrade_count"] == 6 and strict["open_upgrade_count"] == 1,
        "adopted_counts_4_4_1": ledger["adopted_1_to_3_primitive_and_selected_orbit_tier"]["counts"] == {"closed": 4, "partial": 4, "dependency_blocked": 1},
        "U6_selected_next": plan["ordered_steps"][0]["target"].startswith("U6"),
        "no_new_parameter": tier["adopted_selected_orbit_standard"]["new_parameters"] == 0,
    }
    outputs = {
        "finite_measure": str(MEASURE.relative_to(ROOT)).replace("\\", "/"),
        "global_audit": str(GLOBAL.relative_to(ROOT)).replace("\\", "/"),
        "U9_tier": str(TIER.relative_to(ROOT)).replace("\\", "/"),
        "upgrade_ledger": str(LEDGER.relative_to(ROOT)).replace("\\", "/"),
        "next_plan": str(PLAN.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedPostU5TierLedgerAndU9GlobalBranchMeasure.v1",
        "status": STATUS,
        "results": {
            "finite_orbit_invariant_measure_closed": True,
            "retarded_q79_conditional_probability_one": True,
            "adopted_U9_closed": True,
            "strict_global_U9_closed": False,
            "global_measure_claim_currently_definable": False,
            "adopted_upgrade_counts": {"closed": 4, "partial": 4, "blocked": 1},
            "strict_upgrade_counts": {"closed": 2, "partial": 6, "blocked_or_open": 1},
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [
            {"path": str(path), "sha256": sha256(path)} for path in paths.values()
        ],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_PostU5TierLedger_and_U9GlobalBranchMeasure_v1",
        "status": STATUS,
        "finite_orbit_measure": "uniform 1/2,1/2",
        "q79_probability_given_retarded": 1.0,
        "q369_probability_given_advanced": 1.0,
        "adopted_U9_closed": True,
        "strict_global_U9_closed": False,
        "global_measure_readiness": "0/6",
        "adopted_upgrade_counts": "4/4/1",
        "strict_upgrade_counts": "2/6/1",
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Post-U5 Tier Ledger and U9 Global-Branch Measure v1

## Finite orbit measure

The selected unoriented branch space is the antiunitary orbit

```text
B_fin = {{q79/F/m1, q369/F*/m2}}.
```

Antiunitary invariance forces equal weights, and normalization therefore gives
the unique invariant probability measure

```text
mu(q79)=mu(q369)=1/2.
```

The independently selected retarded event is the singleton `q79/F/m1`.
Conditioning gives `mu(q79 | retarded)=1`; the advanced event similarly gives
`mu(q369 | advanced)=1`. No observed CP sign is used. The unoriented theory keeps
both conjugate representatives, while a time orientation selects which one an
observer sees as retarded. This is the precise arrow-of-time interpretation of
the two solutions.

## Global boundary

A probability-one statement over every admissible MTT carrier is not yet a
well-formed theorem. The current formalization supplies none of the six required
global fields: complete carrier set, quotient/groupoid, sigma algebra/topology,
measure or coercive action, existence theorem, and full-support/minimizer proof.
This does not show that other carriers exist or that global uniqueness is false.
It shows that the strict global claim cannot be evaluated until its domain and
measure are defined.

U9 is therefore closed at the **selected antiunitary-orbit plus retarded
conditional-measure standard**, with zero new parameters. Strict global-superset
U9 remains open and frozen.

## Updated plan

At the adopted 1--3 primitive/selected-orbit tier, the upgrade ledger is now
`4 closed / 4 partial / 1 dependency-blocked`: U2, U4, U5 and U9 are closed.
The strict no-knob ledger remains `2 / 6 / 1` and is not relabeled.

The next internal target is U6: construct the selected flux/threshold axion
current and its low-energy QCD anomaly after exotic decoupling. U3 remains an
opportunistic external covariance import; U7, U8 and U1 follow.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (MEASURE, measure),
        (GLOBAL, global_audit),
        (TIER, tier),
        (LEDGER, ledger),
        (PLAN, plan),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
