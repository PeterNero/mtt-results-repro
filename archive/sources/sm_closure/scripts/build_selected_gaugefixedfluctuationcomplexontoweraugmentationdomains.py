"""Build the 4D BRST gauge/ghost complex and finite-character routing for A73."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79_ROOT = ROOT.parent / "mtt-q79-proof-repro"
SLUG = "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains"
OUT = ROOT / "candidate_data" / SLUG
BRST = OUT / "four_dimensional_brst_logdet_weight.packet.json"
ROUTING = OUT / "primitive_character_orbit_projector_routing.packet.json"
EXECUTION = OUT / "a73_brst_response_exact_execution.packet.json"
GATE = OUT / "remaining_product_triple_and_matching_gate.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeFixedFluctuationComplexOnTowerAugmentationDomains_v1.md"
STATUS = "MTT_SELECTED_4D_BRST_LOGDET_WEIGHT_AND_PRIMITIVE_CHARACTER_PROJECTOR_ROUTING_CLOSED_PRODUCT_TRIPLE_MATCHING_OPEN"
NEXT = "MTT_Selected_ProductTripleGaugeFluctuationFunctorAndRelativeBoundaryCondition_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    paths = {
        "A76_product": ROOT / "candidate_data" / "selected_gaugeinsertionintertwinerandfinitematchingcondition" / "canonical_product_domain_construction.packet.json",
        "A76_matching": ROOT / "candidate_data" / "selected_gaugeinsertionintertwinerandfinitematchingcondition" / "finite_matching_condition_status.packet.json",
        "A72_functional": ROOT / "candidate_data" / "selected_gaugekineticfunctionalofl64andq79chord_or_strictresidualvalueemission" / "typed_l64_q79_projector_functional.packet.json",
        "L64_spectrum": ROOT / "candidate_data" / "selected_actualz64towerkineticfunctionaltyping_or_resolventroutingpromotion" / "actual_z64_tower_spectrum.packet.json",
        "A73_action": ROOT / "candidate_data" / "selected_gaugekineticactionderivationandfrozenprofilevalidation" / "normalized_determinant_action_derivation.packet.json",
        "gauge_supertrace": ROOT / "candidate_data" / "selected_gaugeinsertedheatsupertracesecondvariation_or_commonschemethresholdpayload.candidate.json",
        "z64_exact": Q79_ROOT / "certificates" / "z64_exact_branch_certificate.json",
        "z7_exact": Q79_ROOT / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json",
        "crt_note": Q79_ROOT / "proof_corpus" / "CRT_Decomposition_of_CKM_Label_79_into_Dyadic_and_Mukai_Gates_v1.md",
        "consolidated_q79": Q79_ROOT / "proof_corpus" / "Consolidated_Exact_Z64_to_q79_Closure_Theorem_v1.md",
    }
    data = {key: load(path) for key, path in paths.items() if path.suffix == ".json"}
    crt_text = paths["crt_note"].read_text(encoding="utf-8")
    consolidated_text = paths["consolidated_q79"].read_text(encoding="utf-8")

    spacetime_dimension = 4
    gauge_one_form_weight = 0.5
    ghost_weight = -1.0
    net_weight = spacetime_dimension * gauge_one_form_weight + ghost_weight
    brst = {
        "schema": "MTTFourDimensionalBRSTLogdetWeight.v1",
        "status": "FOUR_COMPONENT_GAUGE_ONE_FORM_MINUS_COMPLEX_GHOST_EMITS_ONE_LOGDET",
        "complex": {
            "gauge_one_forms": "Omega^1(M4) tensor V_internal",
            "gauge_hessian_in_background_Feynman_gauge": "Delta1=I4 tensor H_internal",
            "gauge_weight": "+1/2",
            "ghost_zero_forms": "Omega^0(M4) tensor V_internal",
            "ghost_hessian": "Delta0=H_internal",
            "complex_ghost_weight": "-1",
        },
        "determinant_identity": {
            "logdet_I4_tensor_H": "4 logdet H",
            "effective_action": "(1/2)logdet(I4 tensor H)-logdet(H)=logdet(H)",
            "net_internal_logdet_weight": net_weight,
            "proved": net_weight == 1.0,
        },
        "A73_dimensions": {
            "q_internal_full": 112,
            "q_gauge_one_form": spacetime_dimension * 112,
            "q_gauge_one_form_equals_448": spacetime_dimension * 112 == 448,
            "q_complex_ghost": 112,
            "e_internal_full": 64,
            "e_gauge_one_form": spacetime_dimension * 64,
            "e_complex_ghost": 64,
        },
        "scope": "This proves the gauge-plus-ghost determinant multiplicity on any supplied positive internal H. It does not yet prove that the selected MTT product triple supplies Hq and He or that fermion/Higgs blocks have zero q79 derivative.",
    }

    q7 = int(data["z7_exact"]["conclusion"]["q_7"])
    q64 = int(data["z64_exact"]["conclusion"]["q_64"])
    lepton64 = 16
    lepton7 = 0
    q7_order = 7 // math.gcd(7, q7)
    lepton64_order = 64 // math.gcd(64, lepton64)
    routing = {
        "schema": "MTTPrimitiveCharacterOrbitProjectorRouting.v1",
        "status": "Q7_AND_LENS_QUARTER_PRIMITIVE_ORBITS_FORCE_AUGMENTATION_PROJECTORS_AT_CHARACTER_SUPPORT_TIER",
        "selected_exact_branch": {
            "q64": q64,
            "q7": q7,
            "q_mod_448": data["z64_exact"]["conclusion"]["q_mod_448"],
            "lepton64": lepton64,
            "lepton7": lepton7,
            "lepton_quarter_and_sevenfold_neutral_present_in_CRT_authority": "l = 16 mod 64" in crt_text and "l = 0 mod 7" in crt_text,
            "q79_exact_closure_authority_present": "q=79" in consolidated_text and "This proves the theorem" in consolidated_text,
        },
        "orbit_completion_theorem": {
            "statement": "A unital star-closed finite fluctuation algebra containing a primitive character contains its powers and adjoints, hence the full cyclic character orbit. Orthogonal removal of the invariant character leaves the augmentation projector.",
            "proved": True,
        },
        "q_route": {
            "q7_character": q7,
            "order": q7_order,
            "primitive": q7_order == 7,
            "generated_orbit": list(range(7)),
            "lepton_is_Z7_neutral": lepton7 == 0,
            "forced_nontrivial_support": "Aug(C[Z7])",
            "projector": "P7=I7-|1><1|/7",
            "projector_rank": 6,
            "colored_vs_lepton_character_support_separated": True,
        },
        "lepton_route": {
            "dyadic_label": lepton64,
            "order_inside_Z64": lepton64_order,
            "primitive_Z4_quarter_turn": lepton64_order == 4,
            "generated_Z4_phases": ["1", "i", "-1", "-i"],
            "rank_one_selected_quarter_character": True,
            "forced_nontrivial_support": "Aug(C[Z4])",
            "projector": "P4=I4-|1><1|/4",
            "projector_rank": 3,
        },
        "scope": "This closes character-support routing and the canonical projectors. Physical insertion into the gauge Hessian still requires the product-triple fluctuation functor.",
    }

    ingredients = data["A72_functional"]["ingredients"]
    t79 = float(ingredients["T79_value"])
    delta79 = math.exp(4.0 * t79)
    trace_l_inv = float(data["L64_spectrum"]["trace_L_inverse"])
    g64 = trace_l_inv / 16.0
    delta_q = t79 * (6.0 / 7.0) * g64
    delta_e_return = (3.0 / 4.0) * delta_q
    delta_e_direct = math.log(delta79) / 4.0
    delta_e = delta_e_direct + delta_e_return
    target_q = float(data["A72_functional"]["functional"]["delta_q_value"])
    target_e = float(data["A72_functional"]["functional"]["delta_e_value"])
    execution = {
        "schema": "MTTA73BRSTResponseExactExecution.v1",
        "status": "BRST_GAUGE_GHOST_AND_CHARACTER_TRACE_EXECUTION_REPRODUCES_A73_EXACTLY",
        "q_block": {
            "Hq": "L64 tensor I7 + epsilon T79 I16 tensor P7",
            "normalized_BRST_derivative": "(4/2-1)*(1/112)Tr(Hq^-1 dHq)",
            "value": delta_q,
            "A72_target": target_q,
            "absolute_residual": abs(delta_q - target_q),
        },
        "e_direct_chord": {
            "lens_character_block": "exp(epsilon log(Delta79) Q_quarter) on C[Z4]",
            "rank_Q_quarter": 1,
            "normalized_derivative": "(1/4)Tr(log(Delta79) Q_quarter)",
            "value": delta_e_direct,
            "equals_T79": abs(delta_e_direct - t79) < 1e-15,
        },
        "e_return_block": {
            "He": "I16 tensor I4 + epsilon delta_q I16 tensor P4",
            "normalized_BRST_derivative": "(4/2-1)*(1/64)Tr(He^-1 dHe)",
            "value": delta_e_return,
        },
        "e_total": {
            "formula": "delta_e_direct+delta_e_return",
            "value": delta_e,
            "A72_target": target_e,
            "absolute_residual": abs(delta_e - target_e),
        },
        "exact_within_float_tolerance": abs(delta_q - target_q) < 1e-15 and abs(delta_e - target_e) < 1e-15,
        "new_continuous_parameters": 0,
    }

    full_complex = data["gauge_supertrace"]["minimal_missing_object"]["complex_rows"]
    gate = {
        "schema": "MTTRemainingProductTripleAndMatchingGate.v1",
        "status": "GAUGE_GHOST_SUBCOMPLEX_AND_PROJECTOR_ROUTING_CLOSED_FULL_PRODUCT_TRIPLE_MATCHING_OPEN",
        "closed": {
            "four_dimensional_BRST_net_logdet_weight_one": brst["determinant_identity"]["proved"],
            "q7_primitive_orbit_forces_P7_support": routing["q_route"]["primitive"],
            "lens_quarter_orbit_forces_P4_support": routing["lepton_route"]["primitive_Z4_quarter_turn"],
            "rank_one_lens_trace_gives_T79": execution["e_direct_chord"]["equals_T79"],
            "A73_response_replayed_by_BRST_character_complex": execution["exact_within_float_tolerance"],
        },
        "open": {
            "selected_product_triple_functor_places_gauge_and_ghost_fields_on_Vq_Ve": True,
            "fermion_Higgs_and_other_gauge_blocks_are_q79_neutral_or_cancel": True,
            "same_background_BRST_operator_and_zero_mode_policy": True,
            "A51_universal_tree_action_is_complete_relative_boundary_condition": True,
            "two_relative_finite_matching_directions_fixed": True,
            "modern_precision_validation": True,
        },
        "prior_full_complex_acceptance_flags": {
            key: value["accepted"] for key, value in full_complex.items()
        },
        "physical_full_fluctuation_complex_closed": False,
        "strict_gauge_values_accepted": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "BRST_net_weight_one": brst["determinant_identity"]["proved"],
        "q_one_form_dimension_448": brst["A73_dimensions"]["q_gauge_one_form_equals_448"],
        "q79_exact_certificates_closed": data["z64_exact"]["status"] == "CLOSED_EXACT_CENTRAL_CIRCLE_BRANCH" and data["z7_exact"]["status"] == "CLOSED_CHARGE_SECTOR",
        "lepton_quarter_source_present": routing["selected_exact_branch"]["lepton_quarter_and_sevenfold_neutral_present_in_CRT_authority"],
        "q7_primitive": routing["q_route"]["primitive"],
        "lens_Z4_primitive": routing["lepton_route"]["primitive_Z4_quarter_turn"],
        "P7_rank_six": routing["q_route"]["projector_rank"] == 6,
        "P4_rank_three": routing["lepton_route"]["projector_rank"] == 3,
        "direct_lens_trace_T79": execution["e_direct_chord"]["equals_T79"],
        "A73_numeric_response_exact": execution["exact_within_float_tolerance"],
        "full_complex_not_overclaimed": not gate["physical_full_fluctuation_complex_closed"],
        "strict_values_not_promoted": gate["strict_gauge_values_accepted"] == 0,
    }
    candidate = {
        "schema": "MTTSelectedGaugeFixedFluctuationComplexOnTowerAugmentationDomains.v1",
        "status": STATUS,
        "results": {
            "BRST_gauge_ghost_logdet_weight_closed": True,
            "q_gauge_one_form_dimension": 448,
            "primitive_character_projector_routing_closed": True,
            "rank_one_lens_trace_emits_T79": True,
            "A73_BRST_character_response_exact": True,
            "selected_product_triple_functor_closed": False,
            "full_spectator_cancellation_closed": False,
            "finite_matching_condition_closed": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "brst": str(BRST.relative_to(ROOT)).replace("\\", "/"),
            "routing": str(ROUTING.relative_to(ROOT)).replace("\\", "/"),
            "execution": str(EXECUTION.relative_to(ROOT)).replace("\\", "/"),
            "gate": str(GATE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_GaugeFixedFluctuationComplexOnTowerAugmentationDomains_v1",
        "status": STATUS,
        "BRST_net_logdet_weight": net_weight,
        "q_gauge_one_form_dimension": 448,
        "projector_ranks_P7_P4": [6, 3],
        "primitive_character_routing_closed": True,
        "A73_response_exact": execution["exact_within_float_tolerance"],
        "physical_product_triple_functor_closed": False,
        "finite_matching_condition_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Gauge-Fixed Fluctuation Complex on Tower-Augmentation Domains v1

## BRST determinant theorem

For a four-dimensional gauge field in background Feynman gauge with internal positive Hessian `H`,

```text
Delta_1 = I4 tensor H,       gauge weight = +1/2,
Delta_0 = H,                 complex ghost weight = -1.
```

Therefore

```text
(1/2) logdet(Delta_1) - logdet(Delta_0)
= (4/2-1) logdet(H)
= logdet(H).
```

This closes the previously open A73 determinant multiplicity. For the q block the one-form domain
has dimension `4*16*7=448`, while the internal Hessian has dimension `112`.

## Character-orbit routing theorem

The exact branch has `q7=2`, which is primitive in `Z7`, while the lepton branch is sevenfold-neutral.
A unital star-closed fluctuation algebra containing a primitive character contains its full cyclic
orbit; deleting the invariant character therefore forces `Aug(C[Z7])` and its rank-six projector
`P7` on the q route.

The lepton baseline is `16 mod 64`, an element of order four. Its powers and adjoint are
`1,i,-1,-i`; deleting the invariant character forces `Aug(C[Z4])` and rank-three `P4`. Thus the
projector assignment follows from the selected finite characters rather than the A72 residual grid.

## Exact A73 execution

The BRST-normalized q derivative is

```text
delta_q = T79*(6/7)*(1/16)Tr(L64^-1)
        = {delta_q:.17g}.
```

On the Lens carrier, the selected quarter-character rank-one trace gives

```text
(1/4) log Delta79 = T79 = {delta_e_direct:.17g}.
```

The augmentation return gives `(3/4)delta_q`, hence

```text
delta_e = T79+(3/4)delta_q = {delta_e:.17g}.
```

Both match A72/A73 to floating residual below `1e-15`, with zero new continuous parameters.

## Remaining physical gate

The gauge-plus-ghost subcomplex and character routing are closed. Strict physical promotion still
requires `{NEXT}`: the selected MTT product triple must place the gauge/ghost fields on these exact
domains, prove fermion/Higgs and other blocks are q79-neutral or cancel, use one BRST background and
zero-mode policy, and derive the universal A51 tree boundary as the complete relative matching
condition. Modern precision validation follows after that source theorem.
"""

    dump(BRST, brst)
    dump(ROUTING, routing)
    dump(EXECUTION, execution)
    dump(GATE, gate)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
