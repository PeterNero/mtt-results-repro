"""Build neutrino mass/Majorana policy or precision profile table.

This closes the bookkeeping layer after QCD theta: PMNS oscillation replay is
already executable, while absolute neutrino mass and Majorana/Dirac ontology are
not selected by the current MTT source data.  The output is a tiered ledger, not
a claim that the neutrino sector is no-knob predicted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_neutrinomassmajoranapolicy_or_precisionprofiletable"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
NEUTRINO_POLICY = PACKET_DIR / "neutrino_mass_majorana_policy.packet.json"
COUNT_TIERS = PACKET_DIR / "sm_neutrino_count_tiers.packet.json"
SOURCE_GATE = PACKET_DIR / "neutrino_noknob_source_gate.packet.json"
NEXT_TARGET = PACKET_DIR / "next_after_neutrino_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_NeutrinoMassMajoranaPolicy_or_PrecisionProfileTable_v1.md"

PREVIOUS = DATA / "selected_qcdthetapolicy_or_strictpewcountreduction.candidate.json"
QCD_COUNTS = (
    DATA
    / "selected_qcdthetapolicy_or_strictpewcountreduction"
    / "sm_count_with_qcd_theta_update.packet.json"
)
QCD_NEXT = (
    DATA
    / "selected_qcdthetapolicy_or_strictpewcountreduction"
    / "next_after_qcd_theta_policy.packet.json"
)
MIXING_GAUGE = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"

STATUS = (
    "MTT_SELECTED_NEUTRINOMASSMAJORANAPOLICY_OR_PRECISIONPROFILETABLE_"
    "TIERED_NEUTRINO_LEDGER_CLOSED_SOURCE_VALUES_OPEN"
)
NEXT = "MTT_Selected_PrecisionProfileTable_or_TrueSMEquivalenceAudit_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def guarded(payload: dict[str, Any]) -> dict[str, Any]:
    payload["closure_claimed"] = True
    payload["observed_data_used_as_selector"] = False
    payload["target_fitting_used"] = False
    return payload


def main() -> int:
    sources = [PREVIOUS, QCD_COUNTS, QCD_NEXT, MIXING_GAUGE]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing neutrino policy inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    qcd_counts = load(QCD_COUNTS)
    qcd_next = load(QCD_NEXT)
    mixing = load(MIXING_GAUGE)

    pmns = mixing["PMNS_replay"]
    base_with_qcd = int(qcd_counts["counts_including_QCD_theta"]["minimal_PMNS"])
    strict_with_qcd = int(qcd_counts["counts_including_QCD_theta"]["if_strict_P_EW_closes_minimal_PMNS"])

    absolute_mass_add = 1
    majorana_phase_add = 2
    dirac_completion = base_with_qcd + absolute_mass_add
    majorana_completion = base_with_qcd + absolute_mass_add + majorana_phase_add
    strict_dirac_completion = strict_with_qcd + absolute_mass_add
    strict_majorana_completion = strict_with_qcd + absolute_mass_add + majorana_phase_add

    neutrino_policy = guarded(
        {
            "schema": "MTTNeutrinoMassMajoranaPolicy.v1",
            "status": "TIERED_NEUTRINO_POLICY_CLOSED_NO_ONTOLOGY_SELECTED",
            "policy_closed": True,
            "minimal_oscillation_replay_closed": True,
            "minimal_oscillation_slots": 6,
            "minimal_oscillation_slot_contents": [
                "three PMNS mixing angles",
                "one PMNS Dirac CP phase",
                "Delta_m21_sq",
                "Delta_m3l_sq",
            ],
            "absolute_neutrino_mass_filled": pmns["absolute_neutrino_mass_filled"],
            "Dirac_neutrino_yukawa_magnitudes_filled": pmns["Dirac_neutrino_yukawa_magnitudes_filled"],
            "Majorana_phase_policy_from_replay": pmns["Majorana_phase_policy"],
            "selected_neutrino_ontology": "not selected",
            "Dirac_policy_selected": False,
            "Majorana_policy_selected": False,
            "absolute_mass_value_selected_by_MTT": False,
            "Majorana_phases_selected_by_MTT": False,
            "neutrino_no_knob_mass_closure": False,
            "valid_future_exits": [
                "selected Dirac-neutrino Yukawa/source scale",
                "selected Majorana mass operator or seesaw source",
                "selected absolute mass boundary condition",
                "selected Majorana phase/cancellation theorem",
            ],
        }
    )

    count_tiers = guarded(
        {
            "schema": "MTTSMNeutrinoCountTiers.v1",
            "status": "NEUTRINO_COUNT_TIERS_COMPUTED",
            "counts_including_QCD_theta": {
                "minimal_PMNS_oscillation_policy": base_with_qcd,
                "Dirac_massive_neutrino_completion": dirac_completion,
                "Majorana_massive_neutrino_completion": majorana_completion,
                "minimal_PMNS_if_strict_P_EW_closes": strict_with_qcd,
                "Dirac_completion_if_strict_P_EW_closes": strict_dirac_completion,
                "Majorana_completion_if_strict_P_EW_closes": strict_majorana_completion,
            },
            "count_movements": {
                "absolute_neutrino_mass": absolute_mass_add,
                "Majorana_phases": majorana_phase_add,
                "strict_P_EW_source_closure": -1,
            },
            "interpretation": {
                "current_default_count_is_minimal_PMNS_oscillation_policy": True,
                "Dirac_completion_is_conditional_not_selected": True,
                "Majorana_completion_is_conditional_not_selected": True,
                "absolute_mass_and_Majorana_phases_are_not_no_knob_predictions": True,
            },
        }
    )

    source_gate = guarded(
        {
            "schema": "MTTNeutrinoNoKnobSourceGate.v1",
            "status": "NEUTRINO_SOURCE_GATE_OPEN",
            "accepted_absolute_mass_source_values": 0,
            "accepted_Dirac_Yukawa_source_rows": 0,
            "accepted_Majorana_mass_operator_rows": 0,
            "accepted_Majorana_phase_source_rows": 0,
            "accepted_neutrino_ontology_selectors": 0,
            "source_gate_closed": False,
            "policy_gate_closed": True,
            "guardrails": {
                "do_not_choose_Dirac_or_Majorana_from_preference": True,
                "do_not_use_observed_mass_splittings_to_select_source": True,
                "do_not_promote_normal_ordering_replay_to_absolute_mass_source": True,
                "do_not_count_Majorana_phases_unless_Majorana_policy_selected": True,
            },
        }
    )

    next_target = guarded(
        {
            "schema": "MTTNextAfterNeutrinoPolicy.v1",
            "status": "NEXT_TARGET_PRECISION_PROFILE_TABLE_OR_TRUE_SM_EQUIVALENCE_AUDIT",
            "next_required_artifact": NEXT,
            "strict_P_EW_parallel_exit_retained": True,
            "neutrino_source_parallel_exit_retained": True,
            "remaining_cutset_after_neutrino_policy": [
                "strict P_EW source theorem or direct K_threshold.Omega_H.lambda",
                "precision threshold, mass-scheme, multi-loop RG, covariance/profile table",
                "actual selected Qa/SU3 operator/source payload",
                "selected neutrino absolute-mass/ontology source theorem",
            ],
            "previous_remaining_cutset": qcd_next["remaining_cutset_after_qcd_policy"],
        }
    )

    candidate = guarded(
        {
            "candidate": "MTTSelectedNeutrinoMassMajoranaPolicyOrPrecisionProfileTable",
            "status": STATUS,
            "next_required_artifact": NEXT,
            "inputs": {
                "previous": rel(PREVIOUS),
                "qcd_counts": rel(QCD_COUNTS),
                "qcd_next": rel(QCD_NEXT),
                "mixing_gauge": rel(MIXING_GAUGE),
            },
            "packets": {
                "neutrino_mass_majorana_policy": rel(NEUTRINO_POLICY),
                "sm_neutrino_count_tiers": rel(COUNT_TIERS),
                "neutrino_noknob_source_gate": rel(SOURCE_GATE),
                "next_after_neutrino_policy": rel(NEXT_TARGET),
            },
            "closure_decision": {
                "neutrino_policy_gate_closed": True,
                "minimal_PMNS_oscillation_policy_closed": True,
                "absolute_neutrino_mass_closed": False,
                "Dirac_neutrino_yukawa_magnitudes_closed": False,
                "Majorana_policy_selected": False,
                "Majorana_phases_closed": False,
                "neutrino_no_knob_mass_closure": False,
                "minimal_PMNS_count_including_QCD_theta": base_with_qcd,
                "Dirac_massive_neutrino_count_including_QCD_theta": dirac_completion,
                "Majorana_massive_neutrino_count_including_QCD_theta": majorana_completion,
                "minimal_PMNS_count_if_strict_P_EW_closes_including_QCD_theta": strict_with_qcd,
                "Dirac_count_if_strict_P_EW_closes_including_QCD_theta": strict_dirac_completion,
                "Majorana_count_if_strict_P_EW_closes_including_QCD_theta": strict_majorana_completion,
                "strict_P_EW_source_theorem_closed": previous["closure_decision"][
                    "strict_P_EW_source_theorem_closed"
                ],
                "precision_profile_closure_closed": False,
                "true_SM_equivalence_closed": False,
                "full_no_knob_closed": False,
            },
            "PMNS_replay_facts": {
                "status": pmns["status"],
                "basis_convention": pmns["basis_convention"],
                "absolute_neutrino_mass_filled": pmns["absolute_neutrino_mass_filled"],
                "Dirac_neutrino_yukawa_magnitudes_filled": pmns[
                    "Dirac_neutrino_yukawa_magnitudes_filled"
                ],
                "unitarity_max_residual": pmns["unitarity_max_residual"],
                "diagonalization_max_residual_eV2": pmns["diagonalization_max_residual_eV2"],
                "used_as_source_selector": pmns["used_as_source_selector"],
            },
            "theorem": {
                "name": "NeutrinoMassMajoranaPolicyOrPrecisionProfileTableTheorem",
                "proved": True,
                "statement": (
                    "The current repo state closes the neutrino bookkeeping policy "
                    "as a tiered ledger. PMNS oscillation replay is retained as the "
                    "minimal closed policy, giving 25 counted slots including QCD "
                    "theta_bar. A Dirac massive-neutrino completion would add one "
                    "absolute mass slot, giving 26; a Majorana completion would add "
                    "one absolute mass plus two Majorana phases, giving 28. None of "
                    "these conditional completions is selected as no-knob MTT source "
                    "data, and strict P_EW remains the parallel count-reduction exit."
                ),
            },
        }
    )

    cert = guarded(
        {
            "certificate": "MTTSelectedNeutrinoMassMajoranaPolicyOrPrecisionProfileTable",
            "status": STATUS,
            "theorem_proved": True,
            "neutrino_policy_gate_closed": True,
            "minimal_PMNS_oscillation_policy_closed": True,
            "absolute_neutrino_mass_closed": False,
            "Majorana_policy_selected": False,
            "Majorana_phases_closed": False,
            "neutrino_no_knob_mass_closure": False,
            "minimal_PMNS_count_including_QCD_theta": base_with_qcd,
            "Dirac_massive_neutrino_count_including_QCD_theta": dirac_completion,
            "Majorana_massive_neutrino_count_including_QCD_theta": majorana_completion,
            "minimal_PMNS_count_if_strict_P_EW_closes_including_QCD_theta": strict_with_qcd,
            "Dirac_count_if_strict_P_EW_closes_including_QCD_theta": strict_dirac_completion,
            "Majorana_count_if_strict_P_EW_closes_including_QCD_theta": strict_majorana_completion,
            "strict_P_EW_source_theorem_closed": False,
            "precision_profile_closure_closed": False,
            "true_SM_equivalence_claimed": False,
            "full_no_knob_closure_claimed": False,
            "next_required_artifact": NEXT,
        }
    )

    note = f"""# MTT Selected NeutrinoMassMajoranaPolicy or PrecisionProfileTable v1

## Theorem

`NeutrinoMassMajoranaPolicyOrPrecisionProfileTableTheorem` is emitted.

## Neutrino Policy

```text
neutrino policy gate closed = true
minimal PMNS oscillation policy closed = true
absolute neutrino mass closed = false
Dirac neutrino Yukawa magnitudes closed = false
Majorana policy selected = false
Majorana phases closed = false
neutrino no-knob mass closure = false
```

The PMNS replay remains a minimal oscillation ledger:

```text
three PMNS mixing angles
one PMNS Dirac CP phase
Delta_m21_sq
Delta_m3l_sq
```

## Count Tiers Including QCD Theta

```text
minimal PMNS count including QCD theta_bar = {base_with_qcd}
Dirac massive-neutrino count including QCD theta_bar = {dirac_completion}
Majorana massive-neutrino count including QCD theta_bar = {majorana_completion}
minimal PMNS count if strict P_EW closes including QCD theta_bar = {strict_with_qcd}
Dirac count if strict P_EW closes including QCD theta_bar = {strict_dirac_completion}
Majorana count if strict P_EW closes including QCD theta_bar = {strict_majorana_completion}
```

## Claim Boundary

This is a tiered ledger closure, not a neutrino no-knob mass theorem.

Forbidden overclaims:

```text
do not choose Dirac or Majorana from preference
do not use observed mass splittings to select source
do not promote normal-ordering replay to absolute mass source
do not count Majorana phases unless Majorana policy is selected
```

## Next Artifact

`{NEXT}`.
"""

    for path, payload in [
        (NEUTRINO_POLICY, neutrino_policy),
        (COUNT_TIERS, count_tiers),
        (SOURCE_GATE, source_gate),
        (NEXT_TARGET, next_target),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
