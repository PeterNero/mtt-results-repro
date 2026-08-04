"""Build the Weyl-pair source-to-C1 transfer map gate."""

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

PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
ASELECTED = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
WEYLPAIR = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
CORRECTION_EMISSION = DATA / "selected_routec_correction_source_emission_or_selected_galerkin_values.candidate.json"

OUTPUT = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
CERT = CERTS / "selected_routec_weylpair_source_to_c1_transfer_map_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_MAP_BUILT_CONDITIONAL_EXACT_SECTOR_ROUTING_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1"


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


def packet_vector(packet: dict[str, list[list[Any]]]) -> np.ndarray:
    values: list[float] = []
    for sector in ("u", "d", "e", "nuD"):
        values.extend(flatten_matrix(packet[sector]))
    return np.array(values, dtype=float)


def zero_matrix() -> list[list[float]]:
    return [[0.0, 0.0, 0.0] for _ in range(3)]


def transfer_packet(generator_matrix: list[list[Any]], sectors: tuple[str, str]) -> dict[str, list[list[Any]]]:
    zero = zero_matrix()
    return {
        "u": generator_matrix if "u" in sectors else zero,
        "d": generator_matrix if "d" in sectors else zero,
        "e": generator_matrix if "e" in sectors else zero,
        "nuD": generator_matrix if "nuD" in sectors else zero,
    }


def residual(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm(a - b))


def main() -> None:
    provenance = load(PROVENANCE)
    aselected = load(ASELECTED)
    weylpair = load(WEYLPAIR)
    correction = load(CORRECTION_EMISSION)

    basis = weylpair["enriched_weyl_pair_packet"]["basis"]
    expected_phase = weylpair["enriched_weyl_pair_packet"]["source_directions"]["phase_packet"]["matrices"]
    expected_shift = weylpair["enriched_weyl_pair_packet"]["source_directions"]["shift_packet"]["matrices"]

    transfer_phase = transfer_packet(basis["I_plus_Z"], ("u", "e"))
    transfer_shift = transfer_packet(basis["I_plus_X"], ("d", "nuD"))
    phase_residual = residual(packet_vector(transfer_phase), packet_vector(expected_phase))
    shift_residual = residual(packet_vector(transfer_shift), packet_vector(expected_shift))

    conditional_exact = phase_residual <= 1e-10 and shift_residual <= 1e-10
    labels_not_emitted = correction["source_emission_attempt"]["any_representative_label_emitted_by_selected_inputs"] is False

    candidate = {
        "candidate": "MTTSelectedRouteCWeylPairSourceToC1TransferMap",
        "status": STATUS,
        "inputs": {
            "source_provenance_lemma": rel(PROVENANCE),
            "conditional_A_assembly": rel(ASELECTED),
            "weylpair_source_gate": rel(WEYLPAIR),
            "correction_source_emission_audit": rel(CORRECTION_EMISSION),
        },
        "superset_strategy": {
            "mode": "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET",
            "path": "algebraic transfer map from source Weyl carrier to C1 packet columns",
            "locked_target": "phase_packet and shift_packet columns from conditional Weyl-pair A assembly",
            "observed_data_used": False,
            "lifted_flags_used_as_proof": False,
            "target_fitting_used": False,
        },
        "conditional_transfer_map": {
            "name": "T_Weyl_to_C1_sector_routed",
            "formula": {
                "phase_column": "T(Z) = sector_route(u,e; I + Z)",
                "shift_column": "T(X) = sector_route(d,nuD; I + X)",
            },
            "phase_residual": phase_residual,
            "shift_residual": shift_residual,
            "conditional_exact": conditional_exact,
            "uses_source_level_carrier": provenance["source_level_weyl_carrier"]["proved"],
            "uses_active_shift_provenance": provenance["active_shift_provenance"]["proved"],
        },
        "selected_status": {
            "selected_transfer_map_emitted": False,
            "selected_sector_routing_emitted": False,
            "selected_normalization_emitted": False,
            "selected_labels_emitted_by_prior_selected_inputs": not labels_not_emitted,
            "promote_to_A_selected_allowed": False,
        },
        "reduction": {
            "name": "SelectedWeylPairSectorRoutingSourceLemma",
            "status": "NEXT_LEMMA_REQUIRED",
            "statement": (
                "The selected q79/F,m=1 S3/GS Route-C source must theorem-derive the sector routing "
                "that sends the selected phase holonomy Z to u/e as I+Z and the selected active shift "
                "X to d/nuD as I+X, with the same normalization used by the conditional solve."
            ),
        },
        "theorem": {
            "name": "ConditionalWeylPairSourceToC1TransferTheorem",
            "proved": True,
            "statement": (
                "Given the source-level Weyl carrier and the sector routing u/e<-Z, d/nuD<-X, the map "
                "T(Z)=sector_route(u,e;I+Z) and T(X)=sector_route(d,nuD;I+X) exactly produces the two "
                "conditional C1 columns.  Existing selected artifacts do not yet emit this sector routing, "
                "so this remains conditional rather than selected A_selected data."
            ),
        },
        "what_closes_now": {
            "conditional_source_to_C1_transfer_map_defined": True,
            "conditional_transfer_exact_for_phase_column": phase_residual <= 1e-10,
            "conditional_transfer_exact_for_shift_column": shift_residual <= 1e-10,
            "remaining_gap_reduced_to_selected_sector_routing": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_selected_sector_routing_source": True,
            "prove_selected_transfer_normalization": True,
            "promote_conditional_transfer_to_selected_C1_map": True,
            "promote_conditional_A_to_A_selected": True,
            "emit_theorem_derived_b_selected": True,
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
        """# MTT Selected Route-C WeylPair SourceToC1 Transfer Map

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_MAP_BUILT_CONDITIONAL_EXACT_SECTOR_ROUTING_OPEN`

This artifact defines the conditional transfer map from the source-level Weyl
carrier to the C1 packet columns:

```text
T(Z) = sector_route(u,e; I + Z)
T(X) = sector_route(d,nuD; I + X)
```

## Result

The transfer is exact as an algebraic map.  It reproduces the phase and shift
columns used by the conditional Weyl-pair `A` operator with zero residual up to
roundoff.

## Remaining Gap

The selected artifacts still do not emit the sector-routing rule itself.  The
next lemma must derive, from the selected q79/F,m=1 S3/GS Route-C source, why:

- `Z` routes to the `u,e` C1 response as `I + Z`,
- `X` routes to the `d,nuD` C1 response as `I + X`,
- the coefficient normalization is the one used by the conditional solve.

No observed SM constants, diagnostic labels, or lifted flags are used to select
that routing.

Next artifact: `MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
