"""Reduce the U5 neutrino frontier to explicit neutral source clauses."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralnilboundarymassfunctional"
OUT_DIR = ROOT / "candidate_data" / SLUG
OUT_CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
OUT_PACKET = OUT_DIR / "neutral_nil_boundary_mass_functional.packet.json"
OUT_CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralNilBoundaryMassFunctional_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    prior = load(
        ROOT
        / "candidate_data"
        / "selected_neutrinoandstrongcp_strictupgradeattack"
        / "neutrino_operator_ontology_and_absolute_scale_cutset.packet.json"
    )
    slot = load(
        ROOT / "certificates" / "selected_smslotfunctor_overlapkernel_source_emission_certificate.json"
    )
    policy = load(
        ROOT
        / "candidate_data"
        / "selected_neutrinomassmajoranapolicy_or_precisionprofiletable"
        / "neutrino_noknob_source_gate.packet.json"
    )
    replay = load(ROOT / "candidate_data" / "sm_equivalence_mixing_and_gauge_replay.candidate.json")
    pmns = replay["PMNS_replay"]
    delta21 = float(pmns["Delta_m21_sq_replayed_eV2"])
    delta3 = abs(float(pmns["Delta_m3l_sq_replayed_eV2"]))

    no_masses = [0.0, math.sqrt(delta21), math.sqrt(delta3)]
    io_masses = [math.sqrt(delta3), math.sqrt(delta3 + delta21), 0.0]

    packet = {
        "schema": "MTTSelectedNeutralNilBoundaryMassFunctional.v1",
        "status": "NEUTRAL_MINIMAL_TRACE_FUNCTIONAL_PROVED_SOURCE_PROMOTION_AND_ORDERING_OPEN",
        "selected_static_action": {
            "all_six_SM_slot_arrows": slot["selected_SMSlotFunctor_all_six_arrows_claimed"],
            "selected_Dirac_channel": prior["closed"]["selected_1M_equals_Nc_Dirac_channel"],
            "accepted_Dirac_Yukawa_source_rows": policy["accepted_Dirac_Yukawa_source_rows"],
            "accepted_Majorana_mass_operator_rows": policy["accepted_Majorana_mass_operator_rows"],
            "effective_ontology_of_current_selected_action": "Dirac channel only",
            "fundamental_Majorana_extension_excluded": False,
            "reason": "The selected static action emits 1_M=N^c -> nuD and no Majorana operator row. Absence from the current action does not prove that every admissible successor action forbids a separate neutral self-character operator.",
        },
        "neutral_character_cut": {
            "ambient_group_order": 1344,
            "self_character_equation": "2k=0 mod 1344",
            "solutions": prior["closed"]["ambient_Z1344_Majorana_characters"],
            "selected_character": None,
        },
        "minimal_trace_mass_functional": {
            "three_basin_spectrum": "lambda_k=x+A*cos(phi+2*pi*k/3)",
            "positivity_domain": "x >= -min_k A*cos(phi+2*pi*k/3)",
            "trace_identity": "sum_k lambda_k = 3x because sum_k cos(phi+2*pi*k/3)=0",
            "objective": "minimize Tr(M_nu^dagger M_nu)=sum_k lambda_k over the positivity domain",
            "unique_minimizer": "x_*=-min_k A*cos(phi+2*pi*k/3)",
            "consequence": "min_k lambda_k=0, hence the lightest neutrino mass is zero",
            "mathematical_theorem_proved": True,
            "selected_MTT_neutral_source_principle_proved": False,
            "missing_promotion_clause": "prove that neutral nil-survivor selection minimizes this trace functional, rather than merely selecting an arbitrary positive offset",
        },
        "ordering_candidates_postcheck_only": {
            "input_role": "measured oscillation splittings are downstream postchecks, not source selectors",
            "normal_ordering": {
                "masses_eV": no_masses,
                "sum_masses_eV": sum(no_masses),
                "lightest_mass_eV": 0.0,
            },
            "inverted_ordering": {
                "masses_eV": io_masses,
                "sum_masses_eV": sum(io_masses),
                "lightest_mass_eV": 0.0,
            },
            "ordering_selected_by_MTT": False,
        },
        "U5_reduced_source_clauses": [
            "NeutralNilBoundarySaturation: bind nil-survivor minimization to the neutral mass-squared trace functional",
            "SelectedNeutralOrderingPhaseMap: map selected retarded/nil phase data to the NO or IO degeneracy branch",
            "NeutralActionCompleteness: prove Dirac-only completeness or emit/select a separate k=0 or k=672 Majorana operator",
        ],
        "U5_absolute_mass_functional_formula_closed": True,
        "U5_absolute_mass_source_promoted": False,
        "U5_ordering_selected": False,
        "U5_fundamental_ontology_selected": False,
        "observed_data_used_as_selector": False,
        "theorem": {
            "name": "NeutralThreeBasinMinimalTraceBoundaryTheorem",
            "proved": True,
            "statement": "For the nil-phase three-basin mass-squared orbit, the unique trace-minimizing positive-semidefinite offset places one eigenvalue at zero. This removes the continuous absolute offset once neutral nil-boundary saturation is selected. The repository has not yet proved that source premise, selected NO versus IO, or excluded a separate Majorana extension.",
        },
        "next_required_artifact": "MTT_Selected_NeutralNilBoundarySaturation_OrderingPhase_AndActionCompleteness_v1",
    }

    cert = {
        "certificate": "MTT_Selected_NeutralNilBoundaryMassFunctional_v1",
        "status": packet["status"],
        "selected_Dirac_channel": True,
        "accepted_Majorana_operator_rows": 0,
        "minimal_trace_boundary_theorem_proved": True,
        "conditional_lightest_mass_eV": 0.0,
        "normal_ordering_sum_postcheck_eV": sum(no_masses),
        "inverted_ordering_sum_postcheck_eV": sum(io_masses),
        "neutral_source_promotion_closed": False,
        "ordering_selected": False,
        "fundamental_ontology_selected": False,
        "remaining_source_clause_count": 3,
        "next_required_artifact": packet["next_required_artifact"],
    }

    note = f"""# MTT Selected Neutral Nil-Boundary Mass Functional v1

## Mathematical advance

For

```text
lambda_k = x + A cos(phi + 2*pi*k/3),   k=0,1,2,
```

the cosine sum vanishes, so `Tr(M_nu^dagger M_nu)=3x`. Positivity requires
`x >= -min_k A cos(...)`. Therefore minimizing the trace over the positive
domain has the unique solution

```text
x_* = -min_k A cos(phi + 2*pi*k/3),
min_k lambda_k = 0.
```

Thus neutral nil-boundary saturation would select `m_lightest=0` without a
continuous absolute-mass parameter.

Using the existing measured splittings only as downstream postchecks gives
`sum m_nu={sum(no_masses):.12g} eV` for NO and
`sum m_nu={sum(io_masses):.12g} eV` for IO.

## Honest source boundary

The formula is proved, but source promotion is not. Three clauses remain:

1. bind nil-survivor minimization specifically to the neutral mass trace;
2. map selected retarded/nil phase data to NO or IO;
3. prove the selected action is Dirac-complete, or emit a separate Majorana
   operator with neutral character `k=0` or `k=672`.

The current selected action is Dirac-only; this is not yet a theorem that every
admissible extension forbids Majorana neutrinos.
"""

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PACKET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    OUT_CANDIDATE.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
