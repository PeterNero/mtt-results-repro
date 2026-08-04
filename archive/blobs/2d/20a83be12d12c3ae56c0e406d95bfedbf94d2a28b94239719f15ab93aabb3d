"""Build the selected sector-charge / 1_M Dirac-neutrino rule attempt.

This artifact tests the cleanest structural route for the currently open
sector-routing sublemma:

  10_M -> u,e on the phase/clock side,
  bar5_M plus 1_M -> d,nuD on the non-10/shift side.

It imports the E6/SU(5) dictionary as structural support only.  The selected
MTT source proof remains open until the same branch emits the selected
U_10/U_bar5 polarization and the 1_M Dirac-neutrino source rule.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

GRAM_PACKET = DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
SECTOR_CHARGE_CERT = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
MATTER_SLOT_THEOREM = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
WEYLPAIR_PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
E6_DICTIONARY = Q79 / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"
SINGLE_HIGGS = Q79 / "certificates" / "single_higgs_channel_projection_certificate.json"
FINITE_CHANNELS = Q79 / "certificates" / "finite_channel_sets_certificate.json"
TIME_ORIENTED = Q79 / "certificates" / "time_oriented_conjugate_branch_selection_certificate.json"
SU5_SOURCE_ATTEMPT = Q79 / "certificates" / "selected_su5_source_proof_attempt_certificate.json"
SU5_TRANSVERSALITY = Q79 / "certificates" / "su5_matter_slot_transversality_certificate.json"

OUTPUT = DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json"
CERT = CERTS / "selected_sectorcharge_1m_dirac_rule_attempt_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorCharge_1M_DiracRule_Attempt_v1.md"

STATUS = "MTT_SELECTED_SECTORCHARGE_1M_DIRAC_RULE_ATTEMPT_BUILT_SOURCE_POLARIZATION_OPEN"
NEXT = "MTT_Selected_1M_DiracNeutrino_Source_or_SelectedU10Ubar5Polarization_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def maybe_load(path: Path) -> dict[str, Any]:
    if path.exists():
        return load(path)
    return {"missing": True, "path": str(path)}


def contains(text: str, needle: str) -> bool:
    return needle.replace(" ", "") in text.replace(" ", "")


def main() -> None:
    gram = load(GRAM_PACKET)
    sector_cert = load(SECTOR_CHARGE_CERT)
    matter = load(MATTER_SLOT_THEOREM)
    weyl = load(WEYLPAIR_PROVENANCE)
    e6 = load(E6_DICTIONARY)
    single_higgs = maybe_load(SINGLE_HIGGS)
    finite_channels = maybe_load(FINITE_CHANNELS)
    time_oriented = maybe_load(TIME_ORIENTED)
    su5_source = maybe_load(SU5_SOURCE_ATTEMPT)
    su5_transversality = maybe_load(SU5_TRANSVERSALITY)

    rep = e6["representation_dictionary"]
    assignments = rep["sm_assignments"]
    channels = rep["operator_channels"]
    dirac_operator = channels["dirac_neutrino"]

    one_m_maps_to_nc = assignments.get("1_M") == "N^c"
    dirac_uses_bar5_1m = contains(dirac_operator, "bar5_M 1_M 5_H")
    dirac_ends_in_l_nc_hu = contains(dirac_operator, "L N^c H_u")
    ten_contains_ue = assignments.get("10_M") == "Q + u^c + e^c"
    bar5_contains_d_l = assignments.get("bar5_M") == "d^c + L"

    proposed_phase = ["u", "e"]
    proposed_shift = ["d", "nuD"]
    required_phase = gram["sector_charge_packet"]["required_phase_route"]
    required_shift = gram["sector_charge_packet"]["required_shift_route"]

    structural_rule_candidate = {
        "e6_dictionary_loaded": True,
        "one_M_maps_to_Nc": one_m_maps_to_nc,
        "ten_M_contains_u_and_e_slots": ten_contains_ue,
        "bar5_M_contains_d_and_L_slots": bar5_contains_d_l,
        "dirac_operator": dirac_operator,
        "dirac_operator_uses_bar5_1M_5H": dirac_uses_bar5_1m,
        "dirac_operator_outputs_L_Nc_Hu": dirac_ends_in_l_nc_hu,
        "proposed_phase_route": proposed_phase,
        "proposed_shift_route": proposed_shift,
        "matches_required_route": proposed_phase == required_phase and proposed_shift == required_shift,
        "rationale": [
            "u and e are the matter slots involving the 10_M representation in the SU(5)/E6 dictionary.",
            "d is non-10 because it uses bar5_M in the down operator.",
            "nuD is also non-10/shift-side in the Dirac operator because 1_M=N^c appears only through bar5_M 1_M 5_H -> L N^c H_u.",
            "Thus the structural 1_M Dirac-neutrino rule puts nuD with d on the non-10/shift candidate side.",
        ],
    }

    selected_u10_ubar5 = matter["finite_matter_slot"]["projection_tensor_promoted_to_selected"]
    selected_charge_closed = matter["matter_slot_charge"]["selected_charge_table_closed"]
    selected_1m_rule = False
    route_b_uniform = matter["matter_slot_charge"]["routeB_current_selected_block_uniform"]
    q79_transversality_source_hypothesis_only = (
        matter["finite_matter_slot"]["under_transversality_closed"] is True
        and matter["finite_matter_slot"]["selected_mtt_source_present"] is False
    )

    selected_proof_tests = {
        "selected_U10_Ubar5_source": selected_u10_ubar5,
        "selected_sector_charge_table": selected_charge_closed,
        "selected_1M_Dirac_neutrino_rule": selected_1m_rule,
        "routeB_current_selected_block_uniform": route_b_uniform,
        "q79_transversality_source_hypothesis_only": q79_transversality_source_hypothesis_only,
        "source_level_weyl_carrier_closed": weyl["source_level_weyl_carrier"]["proved"],
        "source_to_C1_transfer_map_open": weyl["c1_transfer_map"]["selected_source_to_C1_response_map_emitted"] is False,
        "su5_source_attempt_claims_selected_U10_Ubar5": su5_source.get("claims_selected_U10_Ubar5", False),
    }

    candidate_closed = (
        structural_rule_candidate["matches_required_route"] is True
        and structural_rule_candidate["one_M_maps_to_Nc"] is True
        and structural_rule_candidate["dirac_operator_uses_bar5_1M_5H"] is True
        and structural_rule_candidate["dirac_operator_outputs_L_Nc_Hu"] is True
    )

    candidate = {
        "candidate": "MTTSelectedSectorCharge1MDiracRuleAttempt",
        "status": STATUS,
        "inputs": {
            "sectorcharge_gram_transfer_packet": rel(GRAM_PACKET),
            "sector_charge_or_chirality_certificate": rel(SECTOR_CHARGE_CERT),
            "matter_slot_charge_overlap_theorem": rel(MATTER_SLOT_THEOREM),
            "weylpair_source_provenance": rel(WEYLPAIR_PROVENANCE),
            "q79_e6_dictionary_certificate": rel(E6_DICTIONARY),
            "q79_single_higgs_channel_projection": rel(SINGLE_HIGGS),
            "q79_finite_channel_sets": rel(FINITE_CHANNELS),
            "q79_time_oriented_branch_selection": rel(TIME_ORIENTED),
            "q79_selected_su5_source_attempt": rel(SU5_SOURCE_ATTEMPT),
            "q79_su5_matter_slot_transversality": rel(SU5_TRANSVERSALITY),
        },
        "superset_strategy": {
            "mode": "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET",
            "using_one_straight_path": False,
            "straight_path": "E6/SU(5) matter-slot dictionary plus the Dirac-neutrino operator.",
            "support_path": "q79 retarded/transversality support and selected source-level Weyl carrier.",
            "locked_target": "selected sector charge/chirality route u,e | d,nuD without observed-data fitting",
            "observed_data_used": False,
            "target_fitting_used": False,
            "diagnostic_lift_used_as_proof": False,
        },
        "structural_rule_candidate": structural_rule_candidate,
        "imported_support": {
            "single_higgs_certificate_present": "missing" not in single_higgs,
            "finite_channels_certificate_present": "missing" not in finite_channels,
            "time_oriented_certificate_present": "missing" not in time_oriented,
            "su5_transversality_certificate_present": "missing" not in su5_transversality,
            "source_level_weyl_carrier_provenance_closed": weyl["what_closes_now"]["source_level_phase_Z_carrier_provenance"],
            "matter_slot_routeA_matches_required_partition": matter["matter_slot_charge"]["routeA_matches_required_partition"],
        },
        "selected_proof_tests": selected_proof_tests,
        "decision": {
            "structural_1M_Dirac_rule_candidate_closed": candidate_closed,
            "selected_sector_charge_closed": False,
            "selected_1M_Dirac_rule_closed": False,
            "selected_U10_Ubar5_polarization_closed": False,
            "transfer_normalization_promoted": False,
            "alpha1_driver_promoted": False,
            "why": (
                "The E6/SU(5) dictionary gives a clean structural 1_M=N^c Dirac-neutrino rule, "
                "but current selected MTT data still do not emit the ordered U_10/U_bar5 polarization "
                "or the selected 1_M shift-side source rule."
            ),
        },
        "what_closes_now": {
            "structural_E6_dictionary_support": True,
            "structural_1M_Dirac_rule_candidate": candidate_closed,
            "route_partition_rederived_without_observed_data": True,
            "selected_gap_localized_to_U10_Ubar5_and_1M_source": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_U10_clock_source": True,
            "selected_Ubar5_shift_source": True,
            "selected_1M_Dirac_neutrino_shift_rule": True,
            "selected_sector_charge_or_chirality_table": True,
            "selected_source_to_C1_transfer_map": True,
            "selected_overlap_and_transfer_normalization": True,
            "emit_selected_A_selected_and_b_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem_attempt": {
            "name": "SelectedSectorCharge1MDiracRuleAttempt",
            "fully_proved": False,
            "proved_subresult": "E6/SU(5) structural 1_M Dirac-neutrino rule candidate",
            "open_sublemma": "SelectedU10Ubar5PolarizationAnd1MDiracNeutrinoSourceRule",
            "next_required_artifact": NEXT,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "closure_claimed": False,
                "target_fitting_used": False,
                "structural_1M_Dirac_rule_candidate": candidate_closed,
                "selected_sector_charge_closed": False,
                "selected_1M_Dirac_rule_closed": False,
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected SectorCharge / 1_M Dirac Rule Attempt

Status: `MTT_SELECTED_SECTORCHARGE_1M_DIRAC_RULE_ATTEMPT_BUILT_SOURCE_POLARIZATION_OPEN`

This artifact tries the sector charge/chirality route requested by the current
frontier, including the `1_M` Dirac-neutrino rule.

## What Closes

The E6/SU(5) representation dictionary gives the structural rule:

- `10_M = Q + u^c + e^c`,
- `bar5_M = d^c + L`,
- `1_M = N^c`,
- `dirac_neutrino: bar5_M 1_M 5_H -> L N^c H_u`.

So the natural structural partition is:

- phase/clock candidate side: `u,e`,
- non-10/shift candidate side: `d,nuD`.

The `nuD` entry is not forced by treating `1_M` as another `bar5_M`; it is
forced by the Dirac operator itself.  Since `1_M=N^c` appears in
`bar5_M 1_M 5_H`, the `1_M` neutrino slot is attached to the same non-10
Dirac-neutrino channel as `bar5_M`, hence to the shift-side candidate with
`d`.

No observed constants, measured masses, CKM/PMNS data, or lifted diagnostic
flags are used.

## What Does Not Close Yet

This is still not a selected MTT theorem.  It imports a correct structural
dictionary, but the repo does not yet emit the same-branch selected source
packet proving:

- selected `U_10` clock/polarization source,
- selected `U_bar5` shift/polarization source,
- selected `1_M` Dirac-neutrino shift rule,
- selected source-to-C1 transfer and overlap normalization.

Therefore the sector charge/chirality table and the alpha1 transfer
normalization remain unpromoted.

## Superset Use

This uses a constrained superset strategy.  The straight path is the E6/SU(5)
matter-slot dictionary.  The support path is the q79 retarded/transversality
and source-level Weyl-carrier work.  These paths are combined only to localize
the remaining selected-source object; they are not used as a numerical fit.

Next artifact: `MTT_Selected_1M_DiracNeutrino_Source_or_SelectedU10Ubar5Polarization_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
