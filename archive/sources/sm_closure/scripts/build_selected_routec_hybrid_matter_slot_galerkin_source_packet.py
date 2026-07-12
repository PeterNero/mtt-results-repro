"""Attempt the hybrid matter-slot Galerkin source packet.

The previous artifact reduced Weyl-pair routing to a hybrid selected
HYM/Strominger source followed by Galerkin zero-mode matter-slot data.  This
builder tests whether the current Route-C/Galerkin payload can instantiate that
packet honestly, and records the exact remaining fields if it cannot.
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

PREVIOUS = DATA / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem.candidate.json"
SMOOTH_BN = DATA / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
PROJECTORS = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
PROJECTORS_HONEST = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn" / "sector_projectors_dotd_on_smooth_bn.honest.json"
DE_ACTION = DATA / "selected_routec_de_action_on_smooth_bn.candidate.json"
C1_DEP = Q79 / "iwasawa_route_c_smoke_c1_dependency.candidate.json"
MATTER_ATTEMPT = Q79 / "selected_matter_slot_transversality_source_attempt.candidate.json"
SU5_FIXTURE = Q79 / "selected_su5_qutrit_polarization.unselected_fixture.json"

OUTPUT = DATA / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json"
CERT = CERTS / "selected_routec_hybrid_matter_slot_galerkin_source_packet_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_HYBRID_MATTERSLOT_GALERKIN_PACKET_ATTEMPT_BUILT_SELECTED_SOURCE_AND_OVERLAP_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1"


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


def identity3() -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]


def main() -> None:
    previous = load(PREVIOUS)
    smooth_bn = load(SMOOTH_BN)
    projectors = load(PROJECTORS)
    honest = load(PROJECTORS_HONEST)
    de_action = load(DE_ACTION)
    c1_dep = load(C1_DEP)
    matter_attempt = load(MATTER_ATTEMPT)
    su5_fixture = load(SU5_FIXTURE)

    slots = honest["dotd_response_slots"]
    sector_pairs = [("u", "e"), ("d", "N"), ("u", "d"), ("e", "N"), ("Q", "L")]
    basis_deltas = [
        {
            "pair": list(pair),
            "ordered_zero_mode_basis_delta": norm_delta(slots[pair[0]]["ordered_zero_mode_basis"], slots[pair[1]]["ordered_zero_mode_basis"]),
            "gram_delta": norm_delta(slots[pair[0]]["gram_matrix"], slots[pair[1]]["gram_matrix"]),
        }
        for pair in sector_pairs
    ]
    current_transport = {
        "basis_pair_deltas": basis_deltas,
        "all_checked_family_bases_identical": all(row["ordered_zero_mode_basis_delta"] <= 1e-12 for row in basis_deltas),
        "current_relative_transport": "I_3",
        "current_relative_transport_matrix": identity3(),
        "desired_high_scale_transport": "U_10=I_3 and U_bar5=F plus 1_M singlet routing",
        "current_payload_reaches_desired_transport": False,
    }

    smooth_gates = smooth_bn["gates"]
    honest_flags = {
        "selected_dotD_source_verified": honest["selected_dotD_source_verified"],
        "alpha1_driver_verified": honest["alpha1_driver_verified"],
        "selected_DE_source_verified": not de_action["validation"]["matrix_consistency"]["honest_validator_fails_only_by_selected_source_flags"],
        "matter_slot_source_verified": matter_attempt["calculation_results"]["selected_source_verified"],
    }

    q79_branch = c1_dep["branches"]["current_q79_orientation"]
    c1_boundary = {
        "route_c_smoke_dotD_alone_closes_ckm_heavy_link": c1_dep["calculation_results"]["route_c_smoke_dotD_alone_closes_ckm_heavy_link"],
        "universal_tensor_case_gives_Delta_t_zero": c1_dep["calculation_results"]["universal_tensor_case_gives_Delta_t_zero"],
        "family_dotD_coefficients_identical_for_Q_u_d": q79_branch["sectors"]["u"]["unknown_complex_overlap_slots_if_theta_vertex_basis_absent"]["full_matrix"]
        == q79_branch["sectors"]["d"]["unknown_complex_overlap_slots_if_theta_vertex_basis_absent"]["full_matrix"]
        and q79_branch["response_coefficients"]["family_slots_identical"],
        "heavy_link_overlap_unknowns_per_sector": c1_dep["calculation_results"]["heavy_link_overlap_unknowns_per_sector"],
        "new_required_selected_data": c1_dep["calculation_results"]["new_required_selected_data"],
    }

    honest_routec_fill = {
        "classification": "honest_shape_payload_source_open",
        "closes_hybrid_packet": False,
        "fields_present": {
            "three_dimensional_model_zero_cluster": smooth_bn["B_N_lift"]["zero_cluster"]["dimension"] == 3,
            "positive_model_gap": smooth_bn["B_N_lift"]["complement_gap"] > 0,
            "Riesz_and_reduced_Green_model_emitted": smooth_bn["what_closes_now"]["Riesz_and_reduced_Green_emitted_for_model_active_laplacian"],
            "sector_projectors_emitted": projectors["what_closes_now"]["sector_projectors_on_27_mode_BN_emitted"],
            "dotD_alpha1_matrix_emitted": projectors["what_closes_now"]["dotD_alpha1_matrix_in_same_basis_emitted"],
        },
        "source_flags": honest_flags,
        "basis_transport": current_transport,
        "why_not_selected": [
            "selected D_E/source flags are not theorem-derived",
            "selected dotD source and alpha1 driver are false",
            "current family bases are identical and only give identity relative transport",
            "sector-resolved overlap tensors or selected SU(5) basis transport remain absent",
        ],
    }

    fixture_fill = {
        "classification": "conditional_su5_fixture",
        "closes_hybrid_packet": False,
        "selected_by_mtt": su5_fixture["source"]["selected_by_mtt"],
        "fixture_only": su5_fixture["source"]["fixture_only"],
        "has_10M_clock": su5_fixture["sector_basis_data"]["10_M"]["polarization"] == "clock",
        "has_bar5M_shift": su5_fixture["sector_basis_data"]["bar5_M"]["polarization"] == "shift",
        "has_1M_singlet_neutrino_rule": False,
        "why_not_selected": "This fixture gives the right finite SU(5) I/F shape but has source.selected_by_mtt=false and no 1_M singlet routing packet.",
    }

    candidate = {
        "candidate": "MTTSelectedRouteCHybridMatterSlotGalerkinSourcePacket",
        "status": STATUS,
        "inputs": {
            "previous_reduction": rel(PREVIOUS),
            "smooth_bn_galerkin_lift": rel(SMOOTH_BN),
            "sector_projectors_dotd_summary": rel(PROJECTORS),
            "sector_projectors_dotd_honest_payload": rel(PROJECTORS_HONEST),
            "de_action_on_smooth_bn": rel(DE_ACTION),
            "q79_c1_dependency": rel(C1_DEP),
            "q79_matter_slot_source_attempt": rel(MATTER_ATTEMPT),
            "q79_su5_qutrit_fixture": rel(SU5_FIXTURE),
        },
        "packet_goal": {
            "goal": "selected HYM/Strominger source -> selected D_E/Riesz/Green/dotD -> selected Galerkin matter-slot bases -> Weyl-pair A_selected",
            "closed_now": False,
            "previous_frontier": previous["next_required_artifact"],
        },
        "attempts": {
            "honest_routec_galerkin_fill": honest_routec_fill,
            "conditional_su5_fixture_fill": fixture_fill,
        },
        "c1_overlap_boundary": c1_boundary,
        "selection_verdict": {
            "hybrid_packet_selected": False,
            "shape_scaffold_present": True,
            "selected_operator_source_present": False,
            "selected_matter_slot_transport_present": False,
            "selected_1M_neutrino_shift_rule_present": False,
            "selected_overlap_tensor_present": False,
            "best_next_object": NEXT,
        },
        "what_closes_now": {
            "hybrid_packet_schema_instantiated": True,
            "current_routec_galerkin_shape_payload_checked": True,
            "current_payload_identity_transport_no_go_recorded": True,
            "conditional_su5_fixture_not_promoted": True,
            "dotD_to_C1_overlap_boundary_imported": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_operator_source_D_E": True,
            "selected_dotD_alpha1_driver": True,
            "selected_matter_slot_transport": True,
            "selected_1M_singlet_neutrino_shift_rule": True,
            "selected_sector_overlap_tensors_or_basis_transport": True,
            "selected_weylpair_A_and_b": True,
            "full_SM_or_no_knob_closure": True,
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
        """# MTT Selected Route-C Hybrid MatterSlot Galerkin Source Packet

Status: `MTT_SELECTED_ROUTEC_HYBRID_MATTERSLOT_GALERKIN_PACKET_ATTEMPT_BUILT_SELECTED_SOURCE_AND_OVERLAP_OPEN`

This artifact attempts the hybrid packet:

```text
selected HYM/Strominger source
  -> selected D_E/Riesz/Green/dotD
  -> selected Galerkin matter-slot bases
  -> selected Weyl-pair A_selected
```

The packet is not closed.

## Honest Route-C/Galerkin Fill

The current smooth `B_N` scaffold supplies a three-dimensional model zero
cluster, positive complement gap, Riesz projector, reduced Green operator,
sector projectors, and dotD alpha1 matrix shapes.

But the honest selected flags are still false:

```text
selected D_E source
selected dotD source
alpha1 driver
selected matter-slot source
```

Moreover, the current family zero-mode bases are identical across the checked
family sectors.  Their relative transport is the identity, not the selected
`10_M/bar5_M/1_M` matter-slot transport needed for the Weyl-pair routing.

## Conditional SU(5) Fixture Fill

The q79 SU(5) fixture has the desired finite shape:

```text
10_M  -> clock
bar5_M -> shift
```

but it is explicitly unselected, and it has no selected `1_M` singlet-neutrino
shift rule.

## C1 Boundary

The q79 C1 dependency audit says the current smoke dotD alone cannot close the
heavy-link or Weyl-pair routing.  The next selected data must include either
sector-resolved trilinear overlap tensors, selected SU(5) basis transport, or
selected theta/vertex/basis primitive terms.

Next artifact: `MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
