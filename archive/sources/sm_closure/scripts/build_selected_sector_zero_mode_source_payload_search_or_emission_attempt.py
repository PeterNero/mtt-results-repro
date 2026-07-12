"""Build a concrete sector source-payload attempt.

This artifact emits the canonical per-sector End0 source-map candidate as
finite data, then audits whether existing selected-source artifacts are enough
to promote it to the physical selected rho_s.  The answer is still no: the map
is constructed and checked, but selected zero-mode bases/coherent projector
retention are still the missing promotion theorem.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

VALUE_FILL = DATA / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill.candidate.json"
CUTSET = DATA / "selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem.candidate.json"
ADJOINT_THEOREM = DATA / "selected_sector_zero_mode_adjointtriplet_realization_theorem.candidate.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
EXT_OVERLAP = DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
SPECTRAL = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"

OUTPUT = DATA / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json"
CERT = CERTS / "selected_sector_zero_mode_source_payload_search_or_emission_attempt_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorZeroMode_SourcePayload_Search_or_Emission_Attempt_v1.md"

STATUS = "MTT_SELECTED_SECTOR_SOURCEPAYLOAD_ATTEMPT_CANONICAL_RHO_CONSTRUCTED_SELECTION_OPEN"
NEXT = "MTT_Selected_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]
ALL_SECTORS = MATTER_SECTORS + ["H"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matter_basis(sector: str) -> dict[str, Any]:
    return {
        "candidate_basis_labels": [f"{sector}:T1", f"{sector}:T2", f"{sector}:T3"],
        "candidate_identification": "K_s ~= End0(V_alpha)_ad",
        "basis_source": "canonical End0 adjoint basis T1,T2,T3",
        "dimension": 3,
        "source_selected": False,
    }


def main() -> int:
    value_fill = load(VALUE_FILL)
    cutset = load(CUTSET)
    adjoint_theorem = load(ADJOINT_THEOREM)
    end0_de = load(END0_DE)
    ext_overlap = load(EXT_OVERLAP)
    spectral = load(SPECTRAL)

    direct = value_fill["direct_End0_action_value_fill"]
    rho_candidate = direct["constructed_model_source_map"]
    model_validation = direct["model_source_map_validation"]
    model_tests = direct["model_matrix_tests"]

    candidate_zero_mode_bases = {sector: matter_basis(sector) for sector in MATTER_SECTORS}
    candidate_zero_mode_bases["H"] = {
        "candidate_basis_labels": ["H:h0"],
        "candidate_identification": "K_H ~= trivial End0 singlet",
        "basis_source": "canonical Higgs singlet slot",
        "dimension": 1,
        "source_selected": False,
    }

    source_chain = {
        "cutset_route_A_required": cutset["route_A"]["required_payload"],
        "cutset_route_A_passes_now": cutset["route_A"]["passes_now"],
        "selected_End0_adjoint_basis_available": end0_de["selected_End0_basis"]["rank"] == 3,
        "selected_End0_basis_labels": end0_de["selected_End0_basis"]["basis"],
        "diagonal_End0_DE_formula_extracted": end0_de["what_closes_now"]["diagonal_End0_connection_formula"],
        "End0_DE_T3_matrix_matches_rho_candidate": (
            end0_de["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"]
            == rho_candidate["Q"]["rho"]["T3"]
        ),
        "eta00_harmonic_row_closed": ext_overlap["global_Dolbeault_harmonic_representative"]["closed_at_row_level"],
        "eta00_row_level_source_not_full_sector_basis": ext_overlap["HYM_correction_status"][
            "nonlinear_non_split_HYM_metric_correction_closed"
        ]
        is False,
        "coherent_spectral_zero_mode_retention": spectral["two_layer_projector_audit"]["spectral_projector_layer"][
            "coherent_spectral_zero_mode_projector_retention"
        ],
        "zero_mode_slot_values_filled": spectral["two_layer_projector_audit"]["spectral_projector_layer"][
            "zero_mode_slot_values_filled"
        ],
    }

    construction_checks = {
        "all_sector_maps_present": all(sector in rho_candidate for sector in ALL_SECTORS),
        "matter_maps_are_adjoint_triplets": all(
            rho_candidate[sector]["carrier"] == "model adjoint triplet K_s=span(T1,T2,T3)"
            for sector in MATTER_SECTORS
        ),
        "H_map_is_trivial_singlet": rho_candidate["H"]["rho"] == {"T1": [[0.0]], "T2": [[0.0]], "T3": [[0.0]]},
        "source_flags_remain_false": all(row["source_selected"] is False for row in rho_candidate.values()),
        "bracket_skew_casimir_tests_pass": model_validation["model_map_passes_representation_tests"],
        "adjoint_theorem_hypothesis_rho_still_open": adjoint_theorem["hypotheses_still_to_emit"][
            "selected_End0_action_source_map_rho_s"
        ]
        is False,
        "selected_zero_mode_bases_still_open": adjoint_theorem["hypotheses_still_to_emit"][
            "selected_zero_mode_carriers_K_s"
        ]
        is False,
    }

    promotion_decision = {
        "canonical_source_map_constructed": True,
        "selected_source_map_emitted": False,
        "selected_zero_mode_bases_emitted": False,
        "can_promote_without_new_theorem": False,
        "minimal_new_theorem_needed": NEXT,
        "why_not_promoted": [
            "rho_candidate is defined on canonical model carriers, not on emitted selected sector zero-mode bases K_s",
            "coherent spectral zero-mode projector retention is still false",
            "the eta_00/HYM chain reaches a selected End0 diagonal source lane but not all sector zero modes",
            "the cutset theorem forbids promoting universal carrier matrices without same-source zero-mode/projector data",
        ],
    }

    conditional_promotion_rule = {
        "recorded": True,
        "statement": (
            "If a selected HYM/Strominger projector theorem emits ordered sector zero-mode bases K_s "
            "and proves K_s is the retained End0(V_alpha) adjoint zero-mode carrier for Q,u,d,L,e,N "
            "and the trivial singlet for H, then the constructed rho_candidate promotes uniquely to "
            "selected rho_s up to the already-fixed orthogonal/trace convention."
        ),
        "proof_obligation_remaining": [
            "selected ordered zero-mode bases K_s",
            "coherent spectral projector retention P_s End0-equivariant on the same source",
            "End0 action preserves ker(D_E_s) and bracket on retained modes",
            "trace/Gram convention inherited from the conditional invariant-Gram lemma",
        ],
        "proved_now": False,
    }

    data = {
        "candidate": "MTTSelectedSectorZeroModeSourcePayloadSearchOrEmissionAttempt",
        "status": STATUS,
        "inputs": {
            "value_fill": rel(VALUE_FILL),
            "cutset": rel(CUTSET),
            "adjoint_theorem": rel(ADJOINT_THEOREM),
            "end0_de": rel(END0_DE),
            "ext_overlap": rel(EXT_OVERLAP),
            "spectral": rel(SPECTRAL),
        },
        "source_map_candidate": {
            "domain": "End0(V_alpha) real adjoint basis T1,T2,T3",
            "sector_zero_mode_basis_candidate": candidate_zero_mode_bases,
            "rho_candidate": rho_candidate,
            "model_matrix_tests": model_tests,
        },
        "source_chain": source_chain,
        "construction_checks": construction_checks,
        "promotion_decision": promotion_decision,
        "conditional_promotion_rule": conditional_promotion_rule,
        "what_closes_now": {
            "canonical_per_sector_rho_candidate_emitted": True,
            "same_End0_T3_matrix_matches_selected_diagonal_DE_payload": source_chain[
                "End0_DE_T3_matrix_matches_rho_candidate"
            ],
            "finite_representation_tests_pass": model_validation["model_map_passes_representation_tests"],
            "Higgs_singlet_action_zero": construction_checks["H_map_is_trivial_singlet"],
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_zero_mode_bases_K_s": True,
            "coherent_spectral_projector_retention": True,
            "selected_rho_s_promotion_theorem": True,
            "selected_matter_slot_routing": True,
            "selected_physical_dotD_alpha1": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SectorZeroMode_SourcePayload_Search_or_Emission_Attempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "canonical_source_map_constructed": True,
        "selected_source_map_emitted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Sector ZeroMode SourcePayload Search or Emission Attempt v1

Status: `{STATUS}`.

## Constructed Map

The canonical finite source-map candidate is now emitted:

```text
rho_candidate,s(T_i)=ad(T_i) for s in Q,u,d,L,e,N
rho_candidate,H(T_i)=0
```

It matches the selected diagonal End0 `D_E=d+ad(du*T3)` payload on the `T3`
lane and passes the finite Lie bracket, skew-adjointness, Casimir, and Higgs
singlet checks.

## Why It Is Not Yet Selected

The map is still a candidate, not selected physical `rho_s`, because the repo
does not yet emit ordered selected sector zero-mode bases `K_s` or coherent
spectral projector retention for those bases.  The eta00/HYM chain supplies a
selected End0 diagonal source lane, but not the full sector zero-mode projector
theorem.

## Correct Next Theorem

Prove that the selected HYM/Strominger projector retains sector zero modes as
the End0 adjoint carriers for `Q,u,d,L,e,N` and the trivial singlet for `H`.
Once that is proved, the already-constructed `rho_candidate` promotes uniquely
to selected `rho_s` up to the trace/Gram convention already fixed
conditionally.

No observed constants, benchmark matrices, or locked C1 columns are used.

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
