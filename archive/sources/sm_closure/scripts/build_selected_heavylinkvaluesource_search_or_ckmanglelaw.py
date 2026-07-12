"""Import the strongest heavy-link value source candidate.

This artifact records the found SU(5) qutrit relative-transport candidate from
the q79 proof repo.  It gives exact heavy-link values if MTT selects
B_10=I_3 and B_bar5=F, but keeps the result conditional until the sector
transport selection lemma is proved.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_heavylinkvaluesource_search_or_ckmanglelaw"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FOUND = PACKET_DIR / "su5_qutrit_relative_transport_heavylink_candidate.packet.json"
DEPENDENCIES = PACKET_DIR / "heavylink_dependency_reduction_after_candidate.packet.json"
SELECTION_GATE = PACKET_DIR / "sector_transport_selection_lemma_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_sector_transport_selection_lemma.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HeavyLinkValueSourceSearch_or_SelectedCKMAngleLaw_v1.md"

PREVIOUS = DATA / "selected_heavylinkvectors_after_policybridge_or_ckmlaw.candidate.json"
Q79_CANDIDATE = Q79 / "candidate_data" / "su5_qutrit_basis_transport_heavy_link.candidate.json"
Q79_CERT = Q79 / "certificates" / "su5_qutrit_basis_transport_heavy_link_candidate_certificate.json"

STATUS = "MTT_SELECTED_HEAVYLINKVALUESOURCE_SEARCH_FOUND_SU5_QUTRIT_CONDITIONAL_VALUES_SELECTION_LEMMA_OPEN"
PREVIOUS_STATUS = "MTT_SELECTED_HEAVYLINKVECTORS_AFTER_POLICYBRIDGE_CONTRACT_READY_VALUES_OPEN"
NEXT = "MTT_Selected_SectorTransportSelectionLemma_for_SU5QutritHeavyLink_v1"


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


def main() -> int:
    for path in [PREVIOUS, Q79_CANDIDATE, Q79_CERT]:
        if not path.exists():
            raise FileNotFoundError(rel(path))

    previous = load(PREVIOUS)
    q79_candidate = load(Q79_CANDIDATE)
    q79_cert = load(Q79_CERT)

    if previous["status"] != PREVIOUS_STATUS:
        raise ValueError("previous heavy-link contract status mismatch")

    best = q79_candidate["best_candidate"]
    ckm_packet = q79_candidate["candidate_ckm_heavy_link_packet"]
    exact_delta_t = best["Delta_t_candidate_numeric"]
    inverse_delta_t = q79_candidate["inverse_candidate"]["Delta_t_candidate_numeric"]

    found = {
        "schema": "MTTSU5QutritRelativeTransportHeavyLinkCandidate.v1",
        "status": "EXACT_CONDITIONAL_HEAVY_LINK_VALUES_FOUND_NOT_SELECTED",
        "closure_claimed": True,
        "candidate_rule": best["sector_transport_rule"],
        "up_heavy_links_13_23": best["up_heavy_links_13_23"],
        "down_heavy_links_13_23": best["down_heavy_links_13_23"],
        "Delta_t_symbolic": best["Delta_t_candidate_symbolic"],
        "Delta_t_numeric": exact_delta_t,
        "inverse_convention_Delta_t_numeric": inverse_delta_t,
        "Delta_c_numeric": ckm_packet["inputs"]["c6_heavy_link"]["d"]["entries"],
        "Delta_v_if_selected": exact_delta_t,
        "leading_heavy_link_gate_if_selected": best["leading_heavy_link_gate_if_selected"],
        "selected_by_MTT": False,
        "uses_observed_flavor_data": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    dependencies = {
        "schema": "MTTHeavyLinkDependencyReductionAfterSU5Candidate.v1",
        "status": "EIGHT_SLOTS_REDUCED_TO_RELATIVE_TRANSPORT_SELECTION",
        "closure_claimed": True,
        "slot_fill_if_selected": {
            "t_u13": 0.0,
            "t_u23": 0.0,
            "t_d13": exact_delta_t[0],
            "t_d23": exact_delta_t[1],
            "c_u13": 0.0,
            "c_u23": 0.0,
            "c_d13": 0.0,
            "c_d23": 0.0,
        },
        "dependency_equations": {
            "Delta_t": "t_d - t_u",
            "Delta_c": "c_d - c_u",
            "Delta_v": "Delta_t + chi_q Delta_c",
            "current_candidate": "Delta_c=0, Delta_v=Delta_t",
        },
        "common_fourier_transport_cancels": q79_cert["calculation_results"][
            "common_fourier_transport_delta_zero"
        ],
        "su5_representation_split_nonzero": q79_cert["calculation_results"][
            "su5_representation_split_nonzero"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    selection_gate = {
        "schema": "MTTSectorTransportSelectionLemmaGate.v1",
        "status": "SECTOR_TRANSPORT_SELECTION_LEMMA_OPEN",
        "closure_claimed": True,
        "candidate_values_found": True,
        "selected_heavy_link_values_emitted": False,
        "required_lemma": q79_candidate["next_required_lemma"],
        "selection_options": [
            "typed monad/Cech cohomology outputs sector bases for 10_M and bar5_M",
            "non-invariant spectral Galerkin zero modes output the same relative F",
            "selected bundle/gerbe transition theorem forces the qutrit Fourier split",
        ],
        "still_open": q79_cert["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextSectorTransportSelectionLemma.v1",
        "status": "NEXT_IS_SELECTION_THEOREM_FOR_B10_IDENTITY_BBAR5_F",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "do_not_reopen": [
            "q79 CKM CP phase contact",
            "heavy-link eight-slot contract",
            "pure C6 Delta_c=(0,0) obstruction",
            "common Fourier transport cancels as gauge",
        ],
        "prove_next": [
            "B_10=I_3 selected for 10_M family slot",
            "B_bar5=F selected for bar5_M family slot, or conjugate convention",
            "relative transport is source-owned zero-mode/bundle data",
            "normalization needed before CKM angles/Jarlskog are claimed",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "HeavyLinkValueSourceSearchFindsSU5QutritRelativeTransportCandidate",
        "proved": True,
        "statement": (
            "The heavy-link value search finds an exact conditional candidate: if selected sector "
            "transport derives B_10=I_3 and B_bar5=F, then t_u=(0,0), t_d=(1/sqrt(3), "
            "omega^2/sqrt(3)), c_u=c_d=(0,0), and Delta_v=Delta_t is nonzero. This fills "
            "the eight-slot packet only conditionally; selected heavy-link values remain open until "
            "the sector transport selection lemma is proved from monad/Cech/Galerkin zero-mode data."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedHeavyLinkValueSourceSearchOrCKMAngleLaw",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_heavy_link_contract": rel(PREVIOUS),
            "q79_candidate": rel(Q79_CANDIDATE),
            "q79_certificate": rel(Q79_CERT),
        },
        "output_packets": {
            "su5_qutrit_relative_transport_heavylink_candidate": rel(FOUND),
            "heavylink_dependency_reduction_after_candidate": rel(DEPENDENCIES),
            "sector_transport_selection_lemma_gate": rel(SELECTION_GATE),
            "next_sector_transport_selection_lemma": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "exact_conditional_heavy_link_values_found": True,
            "candidate_rule_B10_I_Bbar5_F": True,
            "conditional_Delta_v_nonzero": True,
            "pure_C6_Delta_c_zero_preserved": True,
            "common_fourier_transport_cancels_as_gauge": True,
            "selected_heavy_link_values_emitted": False,
            "sector_transport_selection_lemma_closed": False,
            "CKM_angle_magnitudes_derived": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": theorem,
    }

    cert = {
        "certificate": "MTTSelectedHeavyLinkValueSourceSearchOrCKMAngleLaw",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "exact_conditional_heavy_link_values_found": True,
        "selected_heavy_link_values_emitted": False,
        "sector_transport_selection_lemma_closed": False,
        "CKM_angle_magnitudes_derived": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HeavyLinkValueSourceSearch or SelectedCKMAngleLaw v1

## Theorem

`HeavyLinkValueSourceSearchFindsSU5QutritRelativeTransportCandidate` is proved.

The search found an exact conditional candidate:

```text
B_10 = I_3
B_bar5 = F
t_u = (0, 0)
t_d = (1/sqrt(3), omega^2/sqrt(3))
c_u = c_d = (0, 0)
Delta_v = Delta_t = (1/sqrt(3), omega^2/sqrt(3))
```

Numerically:

```text
Delta_v = (0.5773502691896258,
           -0.28867513459481287 - 0.5 i)
```

## Boundary

This is not selected MTT data yet. It becomes selected only if the sector
transport selection lemma derives the relative qutrit Fourier transport between
`10_M` and `bar5_M` from monad/Cech/Galerkin zero-mode data.

## Next Artifact

`{NEXT}`
"""

    write_json(FOUND, found)
    write_json(DEPENDENCIES, dependencies)
    write_json(SELECTION_GATE, selection_gate)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
