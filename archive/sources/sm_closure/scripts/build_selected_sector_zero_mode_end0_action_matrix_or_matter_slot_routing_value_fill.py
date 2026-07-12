"""Attempt to fill selected End0 sector action matrices or routing values.

The previous theorem proved that once a selected sector zero-mode End0 action
exists, the matter triplets are forced to be adjoint and the Higgs is forced to
be a singlet.  This artifact tries to fill the actual selected values.

Current result:
* the universal model matrices are available and pass all representation tests;
* no selected source map rho_s on actual sector zero modes is emitted;
* no selected matter-slot routing replaces rho_s;
* conditional invariant-Gram normalization is proved once rho_s is emitted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

ADJOINT_THEOREM = DATA / "selected_sector_zero_mode_adjointtriplet_realization_theorem.candidate.json"
CARRIER = DATA / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct.candidate.json"
SPECTRAL = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"
SECTOR_DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
HYBRID = DATA / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json"
SAME_SOURCE = DATA / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"
SLOT_CHARGE = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"

OUTPUT = DATA / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill.candidate.json"
CERT = CERTS / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorZeroMode_End0Action_Matrix_or_MatterSlotRouting_Value_Fill_v1.md"

STATUS = "MTT_SELECTED_SECTOR_END0_ACTION_VALUE_FILL_ATTEMPTED_RHOS_AND_ROUTING_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_SourceAction_or_SelectedMatterSlotRouting_Source_Theorem_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matsub(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def comm(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return matsub(matmul(a, b), matmul(b, a))


def neg(a: list[list[float]]) -> list[list[float]]:
    return [[-value for value in row] for row in a]


def add(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def eye(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def scalar_mul(s: float, a: list[list[float]]) -> list[list[float]]:
    return [[s * value for value in row] for row in a]


def close(a: list[list[float]], b: list[list[float]], eps: float = 1e-12) -> bool:
    return all(abs(a[i][j] - b[i][j]) <= eps for i in range(len(a)) for j in range(len(a[0])))


def model_source_map(t1: list[list[float]], t2: list[list[float]], t3: list[list[float]]) -> dict[str, Any]:
    source_map: dict[str, Any] = {}
    for sector in MATTER_SECTORS:
        source_map[sector] = {
            "source_selected": False,
            "carrier": "model adjoint triplet K_s=span(T1,T2,T3)",
            "rho": {"T1": t1, "T2": t2, "T3": t3},
        }
    source_map["H"] = {
        "source_selected": False,
        "carrier": "model Higgs singlet K_H",
        "rho": {"T1": [[0.0]], "T2": [[0.0]], "T3": [[0.0]]},
    }
    return source_map


def main() -> int:
    adjoint = load(ADJOINT_THEOREM)
    carrier = load(CARRIER)
    spectral = load(SPECTRAL)
    sector_dotd = load(SECTOR_DOTD)
    hybrid = load(HYBRID)
    same_source = load(SAME_SOURCE)
    slot_charge = load(SLOT_CHARGE)

    basis = carrier["constructed_End0_tensor_product_carrier"]["domain_ad_matrices"]
    t1 = [[float(x) for x in row] for row in basis["T1"]]
    t2 = [[float(x) for x in row] for row in basis["T2"]]
    t3 = [[float(x) for x in row] for row in basis["T3"]]
    casimir = scalar_mul(-1.0, add(add(matmul(t1, t1), matmul(t2, t2)), matmul(t3, t3)))

    model_matrix_tests = {
        "model_rho_T1": t1,
        "model_rho_T2": t2,
        "model_rho_T3": t3,
        "lie_brackets_pass": {
            "[T1,T2]=T3": close(comm(t1, t2), t3),
            "[T2,T3]=T1": close(comm(t2, t3), t1),
            "[T3,T1]=T2": close(comm(t3, t1), t2),
        },
        "skew_for_identity_gram": {
            "T1": close(transpose(t1), neg(t1)),
            "T2": close(transpose(t2), neg(t2)),
            "T3": close(transpose(t3), neg(t3)),
        },
        "negative_casimir": casimir,
        "negative_casimir_equals_2I": close(casimir, scalar_mul(2.0, eye(3))),
        "H_action_zero": True,
    }
    rho_model = model_source_map(t1, t2, t3)
    source_map_validation = {
        "matter_sector_maps_present": all(sector in rho_model for sector in MATTER_SECTORS),
        "H_map_present": "H" in rho_model,
        "all_source_selected_flags_false": all(not row["source_selected"] for row in rho_model.values()),
        "all_matter_maps_use_same_adjoint_matrices": all(
            rho_model[sector]["rho"]["T1"] == t1
            and rho_model[sector]["rho"]["T2"] == t2
            and rho_model[sector]["rho"]["T3"] == t3
            for sector in MATTER_SECTORS
        ),
        "H_map_zero": rho_model["H"]["rho"] == {"T1": [[0.0]], "T2": [[0.0]], "T3": [[0.0]]},
        "model_map_passes_representation_tests": (
            all(model_matrix_tests["lie_brackets_pass"].values())
            and all(model_matrix_tests["skew_for_identity_gram"].values())
            and model_matrix_tests["negative_casimir_equals_2I"]
            and model_matrix_tests["H_action_zero"]
        ),
    }

    direct_value_fill = {
        "candidate_values_exist_as_universal_model": True,
        "constructed_model_source_map": rho_model,
        "model_source_map_validation": source_map_validation,
        "candidate_values_selected_on_actual_zero_modes": False,
        "why_not_selected": [
            "selected zero-mode bases K_s are not emitted",
            "selected source map rho_s(T_i) on K_s is not emitted",
            "coherent spectral zero-mode projector retention remains open",
            "sector Gram/inner-product normalization is not selected",
            "using the universal carrier matrices directly would promote support to selected values",
        ],
        "model_matrix_tests": model_matrix_tests,
    }

    routing_fill = {
        "selected_matter_slot_routing_present": False,
        "selected_1M_Dirac_neutrino_rule_present": False,
        "support_sources": {
            "hybrid_shape_scaffold_present": hybrid["selection_verdict"]["shape_scaffold_present"],
            "hybrid_selected_matter_slot_transport_present": hybrid["selection_verdict"]["selected_matter_slot_transport_present"],
            "hybrid_selected_1M_rule_present": hybrid["selection_verdict"]["selected_1M_neutrino_shift_rule_present"],
            "same_source_packet_status": same_source["status"],
            "slot_charge_status": slot_charge["status"],
        },
        "why_not_selected": [
            "current family bases give identity relative transport",
            "Z/X routing remains conditional on locked C1 columns",
            "1_M singlet-neutrino routing is absent",
            "same-source packet fields remain support-only rather than selected emissions",
        ],
    }

    gram_theorem = {
        "name": "ConditionalSectorInvariantGramNormalizationLemma",
        "proved": True,
        "statement": (
            "If selected rho_s is the irreducible adjoint End0 action on a real "
            "three-dimensional matter zero-mode carrier and G_s is a selected "
            "positive invariant Gram matrix satisfying rho_s(T_i)^T G_s + "
            "G_s rho_s(T_i)=0, then G_s is a positive scalar multiple of identity. "
            "The trace convention tr(G_s)=3 fixes G_s=I_3 and gives ||rho_s(T_i)||_F^2=2."
        ),
        "proof_idea": [
            "Invariant Gram matrices identify End0-intertwiners K_s -> K_s^*.",
            "The real adjoint representation is irreducible of real type, so Schur's lemma leaves only scalar intertwiners.",
            "Positivity fixes the scalar to be positive; trace normalization fixes the scalar to one.",
        ],
        "closes_conditionally": [
            "sector Gram ambiguity after selected rho_s is emitted",
            "common matter-sector normalization convention",
        ],
        "does_not_emit": [
            "selected rho_s matrices",
            "selected physical dotD_alpha1",
            "selected matter-slot routing",
        ],
    }

    selected_source_gates = {
        "selected_zero_mode_bases": adjoint["hypotheses_still_to_emit"]["selected_zero_mode_carriers_K_s"],
        "selected_rho_s_source_map": adjoint["hypotheses_still_to_emit"]["selected_End0_action_source_map_rho_s"],
        "coherent_spectral_zero_mode_retention": spectral["two_layer_projector_audit"]["spectral_projector_layer"]["coherent_spectral_zero_mode_projector_retention"],
        "sector_projectors_dotd_honest_source_driver_flags": not sector_dotd["validation"]["honest_validator_fails_only_by_source_driver_flags"],
        "selected_matter_slot_routing": adjoint["hypotheses_still_to_emit"]["selected_matter_slot_routing"],
        "selected_1M_Dirac_neutrino_rule": adjoint["hypotheses_still_to_emit"]["selected_1M_Dirac_neutrino_rule"],
        "selected_sector_Gram_inner_product": adjoint["hypotheses_still_to_emit"]["selected_sector_Gram_inner_product"],
    }

    data = {
        "candidate": "MTTSelectedSectorZeroModeEnd0ActionMatrixOrMatterSlotRoutingValueFill",
        "status": STATUS,
        "inputs": {
            "adjoint_theorem": rel(ADJOINT_THEOREM),
            "carrier": rel(CARRIER),
            "spectral": rel(SPECTRAL),
            "sector_dotd": rel(SECTOR_DOTD),
            "hybrid_matter_slot": rel(HYBRID),
            "same_source_packet": rel(SAME_SOURCE),
            "slot_charge": rel(SLOT_CHARGE),
        },
        "direct_End0_action_value_fill": direct_value_fill,
        "matter_slot_routing_value_fill": routing_fill,
        "conditional_gram_normalization_theorem": gram_theorem,
        "selected_source_gates": selected_source_gates,
        "what_closes_now": {
            "universal_model_matrices_checked": True,
            "conditional_invariant_Gram_normalization_proved": True,
            "selected_value_gap_localized_to_rho_s_or_routing_source": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_rho_s_matrix_values": True,
            "selected_zero_mode_bases": True,
            "selected_matter_slot_routing": True,
            "selected_1M_Dirac_neutrino_rule": True,
            "selected_physical_dotD_alpha1": True,
            "full_SM_or_no_knob_closure": True,
        },
        "decision": {
            "selected_End0_action_values_filled": False,
            "selected_matter_slot_routing_filled": False,
            "conditional_Gram_theorem_added": True,
            "next_required_artifact": NEXT,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SectorZeroMode_End0Action_Matrix_or_MatterSlotRouting_Value_Fill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selected_End0_action_values_filled": False,
        "selected_matter_slot_routing_filled": False,
        "conditional_Gram_theorem_added": True,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Sector ZeroMode End0Action Matrix or MatterSlotRouting Value Fill v1

Status: `{STATUS}`.

## Result

The value-fill attempt constructs the canonical model source map
`rho_model,s : End0(V_alpha) -> so(K_s)` for every sector:

```text
rho_model,s(T_i)=ad(T_i) for s in Q,u,d,L,e,N
rho_model,H(T_i)=0
```

This does not yet emit selected `rho_s(T_i)` matrices on actual sector
zero-mode bases, and it does not emit selected matter-slot routing.  The
universal model matrices pass the finite representation tests, but using them
directly would still promote a support carrier into selected physical data.

## Conditional Lemma Closed

If selected `rho_s` is emitted and is the real irreducible adjoint action, then
any selected invariant positive Gram matrix is a positive scalar multiple of
identity.  With `tr(G_s)=3`, this fixes `G_s=I_3` and
`||rho_s(T_i)||_F^2=2`.

This closes the Gram-normalization ambiguity conditionally.  It does not emit
the selected `rho_s` source map.

## Straight Path

The straight End0 path now requires:

- selected zero-mode bases `K_s`,
- selected matrices `rho_s(T1), rho_s(T2), rho_s(T3)` on each `K_s`,
- bracket preservation and irreducibility/rank-two checks,
- selected Gram convention or trace normalization.

## Superset Path

The combined superset path is still constrained but not closed:

- Route-C supplies compatible rank/projector/dotD scaffold,
- SU(5)/E6 supports the expected matter-slot split,
- no selected `Z/X/1_M` routing theorem is emitted.

No observed constants, benchmark matrices, or target residuals are used.

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
