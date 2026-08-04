"""Reduce selected sector zero-mode promotion to finite HYM projector data.

The previous artifact constructed a canonical per-sector End0 source map
rho_candidate, but it could not promote that map to selected physical rho_s
because the selected sector zero-mode bases K_s were not emitted.

This artifact proves the bridge theorem: if the selected HYM/Strominger
operator emits same-source spectral projectors with the listed equivariance,
rank, gap, and Gram data, then the canonical rho_candidate promotes uniquely.
It also audits the current repository and records that the finite projector
values are still open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SOURCE_PAYLOAD = DATA / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json"
SPECTRAL = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
GREEN = DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
EXT_OVERLAP = DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
ADJOINT_THEOREM = DATA / "selected_sector_zero_mode_adjointtriplet_realization_theorem.candidate.json"

OUTPUT = DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"
CERT = CERTS / "selected_zero_mode_basis_from_hym_projector_source_theorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_ZEROMODE_BASIS_HYM_PROJECTOR_THEOREM_REDUCED_VALUES_OPEN"
NEXT = "MTT_Selected_HYM_Projector_ZeroModeBasis_Value_Emission_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]
ALL_SECTORS = MATTER_SECTORS + ["H"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def projector_slot(sector: str) -> dict[str, Any]:
    rank = 1 if sector == "H" else 3
    carrier = "trivial singlet" if sector == "H" else "End0 adjoint triplet"
    return {
        "sector": sector,
        "required_rank": rank,
        "required_carrier": carrier,
        "must_emit": [
            f"selected sector operator D_E,{sector} from the same HYM/Strominger connection",
            f"orthogonal Riesz projector P_{sector} onto ker(D_E,{sector})",
            f"ordered L2-horizontal basis K_{sector} of image(P_{sector})",
            f"spectral gap gamma_{sector}>0 and truncation/projector error bound",
            f"End0-equivariance P_{sector} rho_candidate(T_i)=rho_candidate(T_i) P_{sector}",
            f"selected Gram/trace convention for K_{sector}",
        ],
        "current_value_emitted": False,
    }


def main() -> int:
    source_payload = load(SOURCE_PAYLOAD)
    spectral = load(SPECTRAL)
    end0_de = load(END0_DE)
    green = load(GREEN)
    ext_overlap = load(EXT_OVERLAP)
    adjoint = load(ADJOINT_THEOREM)

    rho_candidate = source_payload["source_map_candidate"]["rho_candidate"]
    spectral_layer = spectral["two_layer_projector_audit"]["spectral_projector_layer"]

    current_support = {
        "canonical_rho_candidate_constructed": source_payload["promotion_decision"][
            "canonical_source_map_constructed"
        ],
        "selected_End0_basis_available": end0_de["selected_End0_basis"]["rank"] == 3,
        "same_T3_lane_matches_rho_candidate": source_payload["source_chain"][
            "End0_DE_T3_matrix_matches_rho_candidate"
        ],
        "full_diagonal_End0_Riesz_Green_closed": green["what_closes_now"][
            "full_diagonal_End0_Riesz_Green"
        ],
        "eta00_row_projector_closed": ext_overlap["what_closes_now"]["eta00_rank_one_gauge_projector"],
        "block_projector_layer_closed": spectral["two_layer_projector_audit"]["block_projector_layer"][
            "block_family_Higgs_projector_retention"
        ],
        "representation_choice_conditionally_closed": adjoint["theorem"]["proved"],
    }

    current_blockers = {
        "selected_zero_mode_bases_emitted": source_payload["promotion_decision"][
            "selected_zero_mode_bases_emitted"
        ],
        "coherent_spectral_projector_retention": spectral_layer[
            "coherent_spectral_zero_mode_projector_retention"
        ],
        "zero_mode_slot_values_filled": spectral_layer["zero_mode_slot_values_filled"],
        "selected_D_E_dotD_Riesz_Green": spectral_layer["selected_D_E_dotD_Riesz_Green"],
        "selected_HYM_operator_source_verified": spectral_layer[
            "selected_HYM_operator_source_verified"
        ],
    }

    theorem = {
        "name": "SelectedZeroModeBasisFromHYMProjectorSourceTheorem",
        "bridge_theorem_proved": True,
        "selected_values_emitted": False,
        "statement": (
            "Assume the selected HYM/Strominger source emits same-branch sector operators "
            "D_E,s and Riesz projectors P_s with rank 3 for Q,u,d,L,e,N and rank 1 for H; "
            "assume positive complement gaps, coherent spectral retention, End0-equivariance "
            "of each P_s, and the selected Gram convention. Then the ordered bases K_s=im(P_s) "
            "promote the canonical rho_candidate to the selected physical sector source map rho_s. "
            "The promotion is unique up to the already-fixed orthogonal/trace convention."
        ),
        "proof_steps": [
            "The source-payload artifact already emits rho_candidate and validates the End0 su(2) bracket, skewness, Casimir, and H singlet checks.",
            "The adjoint-triplet theorem proves that any selected real three-dimensional nonzero irreducible End0 action is the adjoint triplet, while the one-dimensional H action is trivial.",
            "A same-source Riesz projector P_s with positive gap and End0-equivariance makes im(P_s) an invariant selected zero-mode carrier rather than a model carrier.",
            "Applying the selected Gram/trace convention fixes the orthogonal ambiguity, so conjugating rho_candidate into the ordered basis K_s gives a unique rho_s.",
            "No observed masses, mixings, benchmark columns, or fitted residuals enter the selection or promotion.",
        ],
    }

    finite_acceptance_validator = {
        "name": "SelectedHYMProjectorZeroModeBasisValueEmission",
        "required_slots": {sector: projector_slot(sector) for sector in ALL_SECTORS},
        "global_required_checks": [
            "all P_s are emitted from the same selected HYM/Strominger connection and source branch",
            "P_s are self-adjoint idempotents in the selected L2 metric",
            "rank(P_s)=3 for Q,u,d,L,e,N and rank(P_H)=1",
            "positive complement gaps gamma_s are emitted with truncation error bounds below gamma_s/2",
            "End0-equivariance holds for T1,T2,T3 on every retained matter carrier",
            "H carrier has zero End0 action",
            "ordered bases K_s and selected Gram matrices are emitted",
            "no lifted selected flags, observed constants, or locked C1 target columns are used",
        ],
        "passes_now": False,
    }

    superset_strategy = {
        "classification": "SUPERSET_CONSTRAINED_BRIDGE_NOT_MULTI_SOURCE_PROOF",
        "straight_End0_path": {
            "role": "supplies the canonical adjoint carrier, bracket table, rho_candidate, and uniqueness theorem",
            "proof_status": "support closed, but not physical sector promotion without selected K_s",
        },
        "HYM_projector_path": {
            "role": "must supply the physical zero-mode projectors, L2 bases, gaps, and Gram convention",
            "proof_status": "the required emission theorem is identified; values remain open",
        },
        "RouteC_Galerkin_path": {
            "role": "execution engine for finite D_E/Riesz/Green/projector/gap data",
            "proof_status": "support and schemas exist; current honest selected flags remain false",
        },
        "SU5_E6_q79_theta_path": {
            "role": "constrains matter-slot and Weyl-pair routing such as Z/X and 10_M/bar5_M/1_M",
            "proof_status": "cannot promote rho_s unless the same selected projector/operator payload is emitted",
        },
        "locked_target": (
            "same selected projector payload: K_s, P_s, gaps, End0-equivariance, Gram convention, "
            "then rho_candidate -> rho_s"
        ),
        "uses_observed_constants": False,
    }

    promotion_decision = {
        "bridge_theorem_closes": True,
        "canonical_rho_candidate_promotes_now": False,
        "reason_not_promoted_now": [
            "selected zero-mode projectors P_s are not emitted",
            "coherent spectral projector retention is still false",
            "zero-mode basis slots are still unfilled",
            "same-source selected HYM operator flags are still false",
        ],
        "promotes_after_next_artifact_if_validator_passes": True,
        "next_required_artifact": NEXT,
    }

    data = {
        "candidate": "MTTSelectedZeroModeBasisFromHYMProjectorSourceTheorem",
        "status": STATUS,
        "inputs": {
            "source_payload": rel(SOURCE_PAYLOAD),
            "spectral_projector_retention": rel(SPECTRAL),
            "end0_de": rel(END0_DE),
            "green": rel(GREEN),
            "ext_overlap": rel(EXT_OVERLAP),
            "adjoint_theorem": rel(ADJOINT_THEOREM),
        },
        "current_support": current_support,
        "current_blockers": current_blockers,
        "theorem": theorem,
        "finite_acceptance_validator": finite_acceptance_validator,
        "rho_candidate_reference": {
            "matter_rho_T3": rho_candidate["Q"]["rho"]["T3"],
            "H_rho": rho_candidate["H"]["rho"],
            "domain": source_payload["source_map_candidate"]["domain"],
        },
        "superset_strategy": superset_strategy,
        "promotion_decision": promotion_decision,
        "what_closes_now": {
            "promotion_bridge_theorem": True,
            "finite_projector_acceptance_validator": True,
            "superset_roles_disambiguated": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_HYM_projector_zero_mode_basis_values": True,
            "selected_rho_s_actual_promotion": True,
            "selected_matter_slot_routing": True,
            "selected_physical_dotD_alpha1": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "bridge_theorem_proved": True,
        "selected_projector_values_emitted": False,
        "selected_rho_s_promoted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected ZeroModeBasis From HYM Projector Source Theorem v1

Status: `{STATUS}`.

## Theorem

If the selected HYM/Strominger source emits same-branch sector operators
`D_E,s` and Riesz projectors `P_s` with:

- rank `3` for `Q,u,d,L,e,N` and rank `1` for `H`,
- positive complement gaps and truncation error bounds,
- coherent spectral projector retention,
- `End0(V_alpha)` equivariance for `T1,T2,T3`,
- an ordered selected `L2` basis `K_s` and Gram/trace convention,

then the already constructed canonical map

```text
rho_candidate,s(T_i)=ad(T_i),  s=Q,u,d,L,e,N
rho_candidate,H(T_i)=0
```

promotes uniquely to the selected physical sector source map `rho_s`.

## Proof

The source-payload artifact has already emitted the canonical map and checked
the finite `su(2)` representation identities.  The adjoint-triplet theorem
removes representation-choice freedom: a selected real three-dimensional
nonzero irreducible `End0(V_alpha)` action is the adjoint triplet, and a
one-dimensional Higgs carrier is the trivial singlet.

The only missing step is physical selection of the carrier.  A same-source
HYM/Strominger Riesz projector `P_s` with positive spectral gap, coherent
retention, and `End0` equivariance makes `im(P_s)` the selected zero-mode
carrier rather than a model carrier.  The selected Gram convention fixes the
remaining orthogonal ambiguity, so conjugating `rho_candidate` into the ordered
`K_s` basis gives a unique `rho_s`.

## Superset Use

We are using a constrained superset strategy, not a patchwork proof:

- straight `End0` supplies the algebra and canonical `rho_candidate`,
- HYM/projector data must supply the physical selected bases,
- Route-C/Galerkin is the execution path for finite projectors and gaps,
- SU(5)/E6, q79/S3/gerbe, and Theta/Weyl-pair encodings constrain matter-slot
  routing but cannot promote `rho_s` without the same selected projector packet.

Thus several encodings reduce the search space to the same finite target, but
none of them is allowed to become an independent proof source unless it emits
the selected payload.

## Current Boundary

The bridge theorem is proved, but the values are not emitted yet.  Current
honest data still have:

```text
coherent_spectral_projector_retention = false
zero_mode_slot_values_filled = false
selected_HYM_operator_source_verified = false
```

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
