"""Attempt to close the selected Weyl-pair sector-routing source lemma.

The transfer map is exact once the routing Z->(u,e) and X->(d,nuD) is supplied.
This artifact tests whether current selected artifacts choose that routing
uniquely, and records the remaining source certificate if they do not.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

TRANSFER = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
WEYLPAIR = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
PROJECTORS = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
SM_INTERFACE = DATA / "sm_sector_embedding_interface.candidate.json"

OUTPUT = DATA / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json"
CERT = CERTS / "selected_routec_weylpair_sector_routing_source_lemma_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_ROUTING_ATTEMPT_BUILT_NOT_UNIQUELY_SELECTED_BY_CURRENT_DATA"
NEXT = "MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1"

SECTORS = ("u", "d", "e", "nuD")
TARGET_PHASE = ("u", "e")
TARGET_SHIFT = ("d", "nuD")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_parts(value: Any) -> tuple[float, float]:
    if isinstance(value, list):
        return float(value[0]), float(value[1])
    return float(value), 0.0


def flatten_matrix(matrix: list[list[Any]]) -> list[float]:
    values: list[float] = []
    for row in matrix:
        for entry in row:
            real, imag = complex_parts(entry)
            values.extend([real, imag])
    return values


def zero_matrix() -> list[list[float]]:
    return [[0.0, 0.0, 0.0] for _ in range(3)]


def packet(generator: list[list[Any]], routed: tuple[str, str]) -> dict[str, list[list[Any]]]:
    zero = zero_matrix()
    return {sector: generator if sector in routed else zero for sector in SECTORS}


def packet_vector(packet_data: dict[str, list[list[Any]]]) -> np.ndarray:
    values: list[float] = []
    for sector in SECTORS:
        values.extend(flatten_matrix(packet_data[sector]))
    return np.array(values, dtype=float)


def route_candidates() -> list[dict[str, Any]]:
    candidates = []
    for phase in itertools.combinations(SECTORS, 2):
        shift = tuple(sector for sector in SECTORS if sector not in phase)
        candidates.append({"phase": tuple(phase), "shift": shift})
    return candidates


def main() -> None:
    transfer = load(TRANSFER)
    weylpair = load(WEYLPAIR)
    projectors = load(PROJECTORS)
    sm_interface = load(SM_INTERFACE)

    basis = weylpair["enriched_weyl_pair_packet"]["basis"]
    expected_phase = weylpair["enriched_weyl_pair_packet"]["source_directions"]["phase_packet"]["matrices"]
    expected_shift = weylpair["enriched_weyl_pair_packet"]["source_directions"]["shift_packet"]["matrices"]
    target_phase_vec = packet_vector(expected_phase)
    target_shift_vec = packet_vector(expected_shift)

    rows = []
    for item in route_candidates():
        phase_packet = packet(basis["I_plus_Z"], item["phase"])
        shift_packet = packet(basis["I_plus_X"], item["shift"])
        phase_residual = float(np.linalg.norm(packet_vector(phase_packet) - target_phase_vec))
        shift_residual = float(np.linalg.norm(packet_vector(shift_packet) - target_shift_vec))
        exact_target = phase_residual <= 1e-10 and shift_residual <= 1e-10
        corpus_selected = item["phase"] == TARGET_PHASE and item["shift"] == TARGET_SHIFT
        rows.append(
            {
                "phase_route": list(item["phase"]),
                "shift_route": list(item["shift"]),
                "phase_residual_to_locked_column": phase_residual,
                "shift_residual_to_locked_column": shift_residual,
                "matches_locked_columns": exact_target,
                "is_intended_route": corpus_selected,
            }
        )

    exact_rows = [row for row in rows if row["matches_locked_columns"]]
    intended_rows = [row for row in rows if row["is_intended_route"]]
    projector_validation = projectors["what_closes_now"]
    source_projector_open = projectors["what_remains_open"]
    source_classification = {
        key: value["status"]
        for key, value in sm_interface["sm_required_components"].items()
        if value["status"] == "SELECTED_SOURCE_DATA_REQUIRED"
    }

    current_data_selects_route = False
    reason = (
        "The locked columns identify the intended route uniquely relative to the target columns, but current "
        "selected source data do not contain an independent sector-charge/chirality certificate that derives "
        "the partition {u,e}|{d,nuD}. Sector projectors retain family kernels uniformly, and the SM interface "
        "classifies representations as required source data rather than already selected no-knob data."
    )

    candidate = {
        "candidate": "MTTSelectedRouteCWeylPairSectorRoutingSourceLemma",
        "status": STATUS,
        "inputs": {
            "source_to_c1_transfer_map": rel(TRANSFER),
            "weylpair_source_gate": rel(WEYLPAIR),
            "sector_projectors_dotd": rel(PROJECTORS),
            "sm_sector_embedding_interface": rel(SM_INTERFACE),
        },
        "external_research_inspiration": {
            "finite_heisenberg_theta_weil": (
                "Clock/phase and shift/translation operators are the canonical finite Heisenberg/Weyl pair "
                "acting on theta-function state spaces."
            ),
            "heterotic_orbifold_selection_rules": (
                "String compactification Yukawa textures are commonly routed by discrete selection rules, "
                "Wilson-line/holonomy data, and sector charges."
            ),
            "used_as_proof": False,
        },
        "routing_search": {
            "all_two_two_partitions_tested": rows,
            "exact_rows_relative_to_locked_columns": exact_rows,
            "intended_rows": intended_rows,
            "target_columns_select_route": len(exact_rows) == 1,
            "source_data_independently_selects_route": current_data_selects_route,
        },
        "current_selected_support": {
            "conditional_transfer_exact": transfer["conditional_transfer_map"]["conditional_exact"],
            "sector_projectors_built": projector_validation["sector_projectors_on_27_mode_BN_emitted"],
            "family_kernel_dimension_three_retained": projector_validation["family_kernel_dimension_three_retained"],
            "selected_dotD_source_verified_open": source_projector_open["selected_dotD_source_verified"],
            "alpha1_driver_verified_open": source_projector_open["alpha1_driver_verified"],
            "representation_source_data_required": source_classification,
        },
        "lemma_attempt": {
            "name": "SelectedWeylPairSectorRoutingSourceLemma",
            "fully_proved": False,
            "proved_by_locked_columns": len(exact_rows) == 1 and exact_rows[0]["is_intended_route"],
            "proved_by_selected_source": False,
            "why_not_fully_proved": reason,
        },
        "next_certificate": {
            "name": "SelectedWeylPairSectorChargeOrChiralityCertificate",
            "must_supply": [
                "a theorem-derived sector charge, chirality, or conjugation table for u,d,e,nuD",
                "a rule assigning the clock/phase leg Z to the u/e sector pair",
                "a rule assigning the shift/translation leg X to the d/nuD sector pair",
                "normalization compatibility with the selected dotD/Hessian/C1 response basis",
            ],
        },
        "what_closes_now": {
            "all_two_two_sector_routes_enumerated": True,
            "locked_columns_pick_intended_route_uniquely": len(exact_rows) == 1 and exact_rows[0]["is_intended_route"],
            "external_selection_rule_analogy_recorded": True,
            "missing_source_object_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_sector_charge_or_chirality_certificate": True,
            "source_derivation_of_u_e_phase_route": True,
            "source_derivation_of_d_nuD_shift_route": True,
            "selected_transfer_normalization": True,
            "promote_conditional_A_to_A_selected": True,
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
        """# MTT Selected Route-C WeylPair SectorRouting Source Lemma

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_ROUTING_ATTEMPT_BUILT_NOT_UNIQUELY_SELECTED_BY_CURRENT_DATA`

This artifact tries to close the selected sector-routing source lemma.

## External Inspiration

External theta/Heisenberg and heterotic-orbifold literature supports the shape
of the needed rule: finite Weyl pairs naturally split clock/phase and
shift/translation actions, while heterotic Yukawa textures are routed by
discrete selection rules, Wilson-line/holonomy data, and sector charges.  This
is used only as inspiration, not as MTT proof.

## Result

All two-two routings of `{u,d,e,nuD}` were enumerated.  Relative to the locked
C1 packet columns, the intended route is uniquely selected:

```text
Z -> u,e as I+Z
X -> d,nuD as I+X
```

But this is still target-column selection, not independent selected-source selection.

## Remaining Gap

Current selected artifacts do not yet contain an independent theorem-derived
sector charge, chirality, or conjugation table that forces `{u,e}|{d,nuD}`.
The sector projectors retain family kernels, but they treat the family sectors
uniformly and leave selected dotD/alpha1 source verification open.

The next certificate must supply:

- a selected sector charge/chirality/conjugation table for `u,d,e,nuD`,
- a rule assigning `Z` to `u,e`,
- a rule assigning `X` to `d,nuD`,
- normalization compatibility with the selected C1 response basis.

Next artifact: `MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
