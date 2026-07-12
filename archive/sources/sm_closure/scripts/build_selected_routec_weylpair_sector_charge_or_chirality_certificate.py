"""Audit the missing Weyl-pair sector charge/chirality certificate.

This imports the q79 SU(5)/qutrit artifacts and the local Route-C projector
payload to test whether current selected data independently force
Z -> (u,e) and X -> (d,nuD).
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro" / "candidate_data"

PHIFIN = DATA / "finite_emission_morphism_phifin.candidate.json"
PROJECTORS = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
PROJECTORS_HONEST = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn" / "sector_projectors_dotd_on_smooth_bn.honest.json"
SM_INTERFACE = DATA / "sm_sector_embedding_interface.candidate.json"
SECTOR_ROUTING = DATA / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json"

SU5_SOURCE_ATTEMPT = Q79 / "selected_su5_source_proof_attempt.candidate.json"
SU5_TRANSVERSALITY = Q79 / "su5_matter_slot_transversality.candidate.json"
SU5_BLOCK_SPLIT = Q79 / "su5_block_orientation_route_split.candidate.json"
SU5_PROJECTION = Q79 / "su5_projection_tensor_derivation_attempt.candidate.json"
GERBE_FOURIER = Q79 / "selected_gerbe_fourier_type_theorem.candidate.json"
SU5_FIXTURE = Q79 / "selected_su5_qutrit_polarization.unselected_fixture.json"

OUTPUT = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
CERT = CERTS / "selected_routec_weylpair_sector_charge_or_chirality_certificate_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_CERTIFICATE_BUILT_SOURCE_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_MatterSlot_or_BlockSector_Source_Theorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def flatten_numeric(value: Any) -> list[float]:
    out: list[float] = []
    if isinstance(value, (int, float)):
        out.append(float(value))
    elif isinstance(value, list):
        if len(value) == 2 and all(isinstance(x, (int, float)) for x in value):
            out.extend([float(value[0]), float(value[1])])
        else:
            for item in value:
                out.extend(flatten_numeric(item))
    elif isinstance(value, dict):
        for key in sorted(value):
            out.extend(flatten_numeric(value[key]))
    return out


def norm_delta(left: Any, right: Any) -> float:
    a = np.array(flatten_numeric(left), dtype=float)
    b = np.array(flatten_numeric(right), dtype=float)
    if a.shape != b.shape:
        return math.inf
    return float(np.linalg.norm(a - b))


def right_sector_uniformity(honest: dict[str, Any]) -> dict[str, Any]:
    slots = honest["dotd_response_slots"]
    keys = [
        "dotD_alpha1_matrix",
        "source_vectors",
        "ordered_zero_mode_basis",
        "reduced_green_operator",
        "horizontal_response_vectors",
    ]
    pairs = [("u", "e"), ("d", "N"), ("u", "d"), ("e", "N")]
    rows = []
    for pair in pairs:
        deltas = {key: norm_delta(slots[pair[0]][key], slots[pair[1]][key]) for key in keys}
        rows.append(
            {
                "pair": list(pair),
                "max_delta": max(deltas.values()),
                "component_deltas": deltas,
                "identical_at_current_payload": max(deltas.values()) <= 1e-12,
            }
        )
    return {
        "fields_checked": keys,
        "right_family_pairs": rows,
        "all_right_family_payloads_identical": all(row["identical_at_current_payload"] for row in rows),
    }


def main() -> None:
    phifin = load(PHIFIN)
    projectors = load(PROJECTORS)
    honest = load(PROJECTORS_HONEST)
    sm_interface = load(SM_INTERFACE)
    sector_routing = load(SECTOR_ROUTING)
    su5_source = load(SU5_SOURCE_ATTEMPT)
    su5_trans = load(SU5_TRANSVERSALITY)
    su5_block = load(SU5_BLOCK_SPLIT)
    su5_projection = load(SU5_PROJECTION)
    gerbe = load(GERBE_FOURIER)
    fixture = load(SU5_FIXTURE)

    branch_packet = phifin["imported_results"]["branch_packet"]
    sector_orientations = branch_packet["sector_orientations"]
    right_orientations = {k: sector_orientations[k] for k in ("u", "d", "e", "N")}
    right_orientation_values = set(right_orientations.values())
    uniformity = right_sector_uniformity(honest)

    su5_slot_dictionary = {
        "u": {"slot": "10_M", "reason": "u^c is in the SU(5) 10_M packet"},
        "e": {"slot": "10_M", "reason": "e^c is in the SU(5) 10_M packet"},
        "d": {"slot": "bar5_M", "reason": "d^c is in the SU(5) bar5_M packet"},
        "nuD": {"slot": "1_M", "reason": "Dirac neutrino uses the singlet N^c leg"},
    }
    su5_induced_phase = sorted(k for k, v in su5_slot_dictionary.items() if v["slot"] == "10_M")
    su5_induced_non10 = sorted(k for k, v in su5_slot_dictionary.items() if v["slot"] != "10_M")
    target_phase = sorted(["e", "u"])
    target_shift = sorted(["d", "nuD"])

    route_a = {
        "name": "Route_A_high_scale_SU5_E6_matter_slot_transversality",
        "superset_path_kind": "single structural path, conditional source",
        "evidence": {
            "finite_su5_transversality_closed": su5_trans["calculation_results"]["finite_transversality_theorem_closed"],
            "retarded_q79_orientation_closed_inside_conditional_packet": su5_trans["calculation_results"]["retarded_q79_orientation_closed"],
            "conditional_projection_tensor_closed": su5_projection["calculation_results"]["finite_projection_tensor_derived"],
            "selected_su5_source_present": su5_trans["calculation_results"]["selected_mtt_source_present"],
            "selected_source_attempt_closed_routes": su5_source["calculation_results"]["closed_source_routes"],
            "fixture_selected_by_mtt": fixture["source"]["selected_by_mtt"],
        },
        "sector_implication": {
            "phase_like_clock_side_from_10M": su5_induced_phase,
            "non10_shift_side_candidate": su5_induced_non10,
            "matches_required_partition": su5_induced_phase == target_phase and su5_induced_non10 == target_shift,
            "nuD_caveat": "nuD is a singlet 1_M leg, not a bar5_M leg; it needs a selected Dirac-neutrino/singlet routing rule.",
        },
        "verdict": "Supports the intended partition structurally, but remains conditional because the selected U_10/U_bar5 source and singlet-neutrino rule are open.",
    }

    route_b = {
        "name": "Route_B_block_factorized_sector_resolved_route",
        "superset_path_kind": "straight selected block path currently available, but insufficient for pair split",
        "evidence": {
            "block_route_requires_conjugate_pairs": su5_block["calculation_results"]["block_rule_requires_conjugate_pairs"],
            "left_right_sector_split_coherent": su5_block["calculation_results"]["left_right_sector_split_coherent_under_current_branch_packets"],
            "right_singlet_or_conjugates": su5_block["branches"][0]["left_right_orientation_uniformity"]["right_singlet_or_conjugates"],
            "sector_orientations_from_phifin": right_orientations,
            "right_orientation_values": sorted(right_orientation_values),
            "all_right_orientations_uniform": len(right_orientation_values) == 1,
            "current_projector_dotd_payload_uniform": uniformity["all_right_family_payloads_identical"],
        },
        "verdict": "This is the honest selected block evidence, but it treats u,d,e,N uniformly at the current layer and does not derive {u,e}|{d,nuD}.",
    }

    selected_certificate_closed = False
    candidate = {
        "candidate": "MTTSelectedRouteCWeylPairSectorChargeOrChiralityCertificate",
        "status": STATUS,
        "inputs": {
            "finite_emission_morphism_phifin": rel(PHIFIN),
            "sector_projectors_dotd_summary": rel(PROJECTORS),
            "sector_projectors_dotd_honest_payload": rel(PROJECTORS_HONEST),
            "sm_sector_embedding_interface": rel(SM_INTERFACE),
            "previous_sector_routing_attempt": rel(SECTOR_ROUTING),
            "q79_selected_su5_source_attempt": rel(SU5_SOURCE_ATTEMPT),
            "q79_su5_matter_slot_transversality": rel(SU5_TRANSVERSALITY),
            "q79_su5_block_orientation_route_split": rel(SU5_BLOCK_SPLIT),
            "q79_su5_projection_tensor": rel(SU5_PROJECTION),
            "q79_selected_gerbe_fourier_type": rel(GERBE_FOURIER),
            "q79_selected_su5_qutrit_fixture": rel(SU5_FIXTURE),
        },
        "external_research_inspiration": {
            "finite_heisenberg_theta_weil": {
                "url": "https://arxiv.org/search/?query=finite+Heisenberg+group+theta+functions+Weil+representation&searchtype=all",
                "used_as_proof": False,
                "lesson": "Treat clock/phase and shift/translation as distinct finite Weyl polarizations.",
            },
            "heterotic_yukawa_selection_rules": {
                "urls": [
                    "https://arxiv.org/abs/hep-th/0601204",
                    "https://arxiv.org/abs/1107.2137",
                    "https://arxiv.org/abs/1401.6162",
                ],
                "used_as_proof": False,
                "lesson": "Discrete sector charges and holonomy rules are natural proof objects for Yukawa routing.",
            },
        },
        "current_mtt_data_tests": {
            "phifin_right_sector_orientations": right_orientations,
            "phifin_distinguishes_u_e_from_d_N": len(right_orientation_values) > 1,
            "projector_dotd_uniformity": uniformity,
            "selected_dotD_source_verified": honest["selected_dotD_source_verified"],
            "alpha1_driver_verified": honest["alpha1_driver_verified"],
            "representations_are_source_data_required": sm_interface["sm_required_components"]["fermion_representations"]["status"],
        },
        "superset_paths": {
            "route_A": route_a,
            "route_B": route_b,
            "combined_locked_target_use": {
                "classification": "constrained superset comparison, not source promotion",
                "locked_columns_uniquely_pick_partition": sector_routing["routing_search"]["target_columns_select_route"],
                "source_data_independently_selects_route": sector_routing["routing_search"]["source_data_independently_selects_route"],
                "allowed_use": "Ranks and localizes the required source theorem.",
                "forbidden_use": "Cannot promote the conditional Weyl-pair transfer to A_selected.",
            },
        },
        "certificate_result": {
            "selected_certificate_closed": selected_certificate_closed,
            "phase_route_required": ["u", "e"],
            "shift_route_required": ["d", "nuD"],
            "strongest_structural_match": "SU(5)/E6 matter-slot dictionary gives u,e on 10_M and d,nuD on the non-10 side.",
            "why_not_closed": [
                "Current Phi_fin right-family orientations are uniform: u,d,e,N all carry the same orientation.",
                "Current honest Route-C projector/dotD payload is identical across u,d,e,N at the checked fields.",
                "The q79 SU(5) finite tensor is conditional on selected 10_M clock and bar5_M shift source data.",
                "nuD is a singlet leg and needs an additional selected rule tying 1_M to the shift/Dirac-neutrino side.",
            ],
        },
        "what_closes_now": {
            "existing_selected_block_data_do_not_prove_pair_split": True,
            "su5_matter_slot_path_identified_as_structural_candidate": True,
            "nuD_singlet_gap_identified": True,
            "superset_paths_separated_from_locked_target_promotion": True,
            "external_inspiration_recorded_without_importing_as_proof": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_sector_charge_or_chirality_table": True,
            "selected_10M_clock_source_or_sector_resolved_replacement": True,
            "selected_bar5M_shift_source_or_sector_resolved_replacement": True,
            "selected_singlet_neutrino_shift_rule": True,
            "selected_transfer_normalization": True,
            "promote_conditional_weylpair_A_to_A_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "selected_certificate_closed": selected_certificate_closed,
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
        """# MTT Selected Route-C WeylPair Sector Charge or Chirality Certificate

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_CERTIFICATE_BUILT_SOURCE_OPEN`

This artifact tests whether current selected MTT data independently force the
Weyl-pair sector routing

```text
Z -> u,e
X -> d,nuD
```

The answer is no, not yet.

## Superset Paths

Route A is the high-scale SU(5)/E6 matter-slot path.  It gives the strongest
structural match: `u,e` live on the `10_M` side, while `d,nuD` live on the
non-`10_M` side.  This matches the desired partition, but it is still
conditional because the q79 SU(5) artifacts explicitly leave selected
`U_10=I_3`, `U_bar5=F` source data open.  Also, `nuD` is a singlet `1_M` leg,
so it needs a selected Dirac-neutrino/singlet routing rule.

Route B is the block-factorized selected sector path currently available from
Phi_fin/Route-C.  It is the honest selected direction, but it treats the right
family sectors uniformly at this layer: `u,d,e,N` carry the same orientation,
and the checked honest projector/dotD fields are identical across them.  That
cannot independently prove `{u,e}|{d,nuD}`.

Using the locked Weyl-pair target together with these routes is a constrained
superset localization step only.  It may identify the missing theorem, but it
cannot promote the conditional transfer to selected `A_selected`.

## External Inspiration

Finite Heisenberg/theta/Weil systems support the clock/phase versus
shift/translation split, and heterotic Yukawa literature supports the idea that
discrete sector charges and holonomy rules route allowed couplings.  These are
used as inspiration only, not as MTT proof.

## Remaining Theorem

The next object must prove one of two things:

- a selected high-scale matter-slot theorem: `10_M` is the clock/phase slot,
  `bar5_M` is the shift slot, and the singlet neutrino `1_M` follows the
  Dirac-neutrino shift side; or
- a selected sector-resolved block theorem deriving separate sector bases and
  C1/dotD responses that route `Z` to `u,e` and `X` to `d,nuD`.

Next artifact: `MTT_Selected_RouteC_WeylPair_MatterSlot_or_BlockSector_Source_Theorem_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
