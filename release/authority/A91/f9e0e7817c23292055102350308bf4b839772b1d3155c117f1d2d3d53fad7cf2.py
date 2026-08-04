from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SLUG = "selected_neutraldeterminantlineapsoperator_and_native10dmassscale"
STATUS = (
    "MTT_NEUTRAL_DEDEKIND_ARITHMETIC_RETAINED_LENS15_16_SOURCE_ROUTE_REJECTED_"
    "NATIVE10D_NUMERIC_SOURCE_OPEN_OPERATOR_CONTRACT_SHARPENED"
)
NEXT = "MTT_Selected_NeutralDiracFamilyAndDeterminantHolonomy_On_S1xL31xNil3_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralDeterminantLineAPSOperator_and_Native10DMassScale_v1.md"

TOPOLOGY = OUT / "selected_topology_vs_retarded_label_typing.packet.json"
ARITHMETIC = OUT / "dedekind_reciprocity_and_eta_normalization_audit.packet.json"
MONODROMY = OUT / "sl2z_monodromy_family_and_rademacher_ambiguity.packet.json"
OPERATOR = OUT / "dai_freed_operator_source_contract.packet.json"
ACTION = OUT / "native_10d_action_neutral_source_audit.packet.json"
FRONTIER = OUT / "U5_frontier_after_A91.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def exact(value: Fraction) -> dict:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
    }


def sawtooth(n: int, k: int) -> Fraction:
    residue = n % k
    if residue == 0:
        return Fraction(0)
    return Fraction(residue, k) - Fraction(1, 2)


def dedekind_sum(h: int, k: int) -> Fraction:
    return sum(
        (sawtooth(n, k) * sawtooth(h * n, k) for n in range(1, k)),
        Fraction(0),
    )


def main() -> int:
    paths = {
        "A38_common_circle": ROOT / "candidate_data" / "selected_neutralcommoncirclefactorizationandholonomyscalarreduction.candidate.json",
        "A41_dedekind": ROOT / "candidate_data" / "selected_neutrallensdedekindtransgression_or_oneprimitiveprofile.candidate.json",
        "A43_attenuation": ROOT / "candidate_data" / "selected_neutralcompositespectralattenuationreduction_or_branchbridgetheorem.candidate.json",
        "A90_plan": ROOT / "candidate_data" / "selected_posta89minimalparameterledger_and_nextfrontier" / "next_execution_plan_after_parameter_reconciliation.packet.json",
        "theta_topology": CORPUS / "18 Theta-Closure & Execution Program" / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md",
        "native_10D_action": CORPUS / "10 ProtoSpinor" / "Closure_Geometry_and_Unified_Dynamics__A_Ten_Dimensional_Action_for_Mass__Scalar_Relaxation__Quantization__and_Curvature_v3.md",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A91 authority: " + ", ".join(missing))

    a38 = load(paths["A38_common_circle"])
    a41 = load(paths["A41_dedekind"])
    a43 = load(paths["A43_attenuation"])
    a90 = load(paths["A90_plan"])
    topology_text = paths["theta_topology"].read_text(encoding="utf-8")
    action_text = paths["native_10D_action"].read_text(encoding="utf-8")

    selected_cost = int(a41["selected_arithmetic"]["Z64_selected_cost"])
    quarter_anchor = int(a41["selected_arithmetic"]["quarter_turn_anchor"])
    s_15_16 = dedekind_sum(selected_cost, quarter_anchor)
    s_16_15 = dedekind_sum(quarter_anchor, selected_cost)
    mixed = (
        12 * (s_15_16 + s_16_15)
        + 3
        - Fraction(selected_cost, quarter_anchor)
        - Fraction(quarter_anchor, selected_cost)
    )
    generic_remainder = Fraction(1, selected_cost * quarter_anchor)
    selected_lens_sum = dedekind_sum(1, 3)
    selected_lens_signature_eta = -4 * selected_lens_sum

    topology_marker = r"S^1_{\mathrm{cen}}\times L(3,1)\times\Gamma\backslash\mathrm{Nil}_3"
    topology_packet = {
        "schema": "MTTSelectedTopologyVsRetardedLabelTyping.v1",
        "status": "ACTUAL_INTERNAL_TOPOLOGY_AND_RETARDED_LABELS_TYPE_SEPARATED",
        "selected_internal_topology": {
            "symbolic": "S1_cen x L(3,1) x (Gamma\\Nil3)",
            "dimension_census": "1+2+3=6 internal; Y4 x X6 gives native 10D",
            "source_marker": topology_marker,
            "source_marker_found": topology_marker in topology_text,
        },
        "retarded_arithmetic_labels": {
            "15": "selected Z64 Hessian/closure cost",
            "16": "quarter-turn anchor and retarded carrier label",
            "ordered_lag": a41["selected_arithmetic"]["retarded_lag"],
            "selected_as_lens_parameters": False,
            "selected_as_mapping_torus_bottom_row": False,
        },
        "typing_theorem": {
            "statement": "The corpus-selected internal Lens factor is L(3,1). The integers 15 and 16 are selected in the Z64 cost/retarded calculation, but no current theorem promotes them to a Lens-space pair L(16,15), an SL(2,Z) monodromy row, or an APS boundary datum.",
            "proved": topology_marker in topology_text and selected_cost == 15 and quarter_anchor == 16,
        },
        "consequence": "Any determinant-line construction must begin on the actual S1_cen x L(3,1) x Nil3 bundle or separately prove a mapping-torus functor from the retarded labels.",
    }

    arithmetic_packet = {
        "schema": "MTTDedekindReciprocityAndEtaNormalizationAudit.v1",
        "status": "ONE_OVER_240_EXACT_BUT_GENERIC_RECIPROCITY_REMAINDER_NOT_SELECTED_ETA_VALUE",
        "exact_values": {
            "s_15_16": exact(s_15_16),
            "s_16_15": exact(s_16_15),
            "A41_mixed_remainder": exact(mixed),
            "one_over_15_times_16": exact(generic_remainder),
            "s_1_3_for_selected_L31": exact(selected_lens_sum),
            "ordinary_signature_eta_L31_standard_orientation": exact(selected_lens_signature_eta),
        },
        "universal_identity": {
            "formula": "for coprime h,k: 12(s(h,k)+s(k,h))+3-h/k-k/h=1/(h*k)",
            "A41_specialization": "h=15,k=16 gives 1/240",
            "exactly_verified": mixed == generic_remainder == Fraction(1, 240),
            "selects_a_physical_operator": False,
        },
        "selected_lens_comparison": {
            "selected_lens": "L(3,1)",
            "reference_operator": "odd-signature eta in the standard orientation convention",
            "reference_value": exact(selected_lens_signature_eta),
            "equals_A41_remainder": selected_lens_signature_eta == mixed,
            "orientation_or_operator_changes_may_change_value": True,
            "requires_explicit_twisted_Dirac_family": True,
        },
        "retained_result": "The exact arithmetic and the conditional pi/120 compatibility calculation remain valid.",
        "retired_claim": "The arithmetic alone does not identify 1/240 with the eta/rho invariant of the selected MTT internal space.",
    }

    monodromy_rows = []
    for t in range(-3, 4):
        a = 15 + 16 * t
        b = 14 + 15 * t
        c = 16
        d = 15
        determinant = a * d - b * c
        rademacher = Fraction(a + d, c) - 12 * dedekind_sum(d, c)
        monodromy_rows.append(
            {
                "t": t,
                "matrix": [[a, b], [c, d]],
                "determinant": determinant,
                "rademacher_Phi": exact(rademacher),
                "equals_15_plus_t": rademacher == 15 + t,
            }
        )
    monodromy_packet = {
        "schema": "MTTSL2ZMonodromyFamilyAndRademacherAmbiguity.v1",
        "status": "BOTTOM_ROW_16_15_HAS_INFINITE_SL2Z_LIFTS_MONODROMY_AND_PHASE_UNSELECTED",
        "general_family": {
            "formula": "gamma_t=[[15+16t,14+15t],[16,15]], t in Z",
            "determinant_identity": "(15+16t)*15-(14+15t)*16=1",
            "rademacher_identity": "Phi(gamma_t)=(a+d)/c-12s(d,c)=15+t",
            "sample_rows": monodromy_rows,
        },
        "selection_result": {
            "bottom_row_uniquely_selects_monodromy": False,
            "integer_ambiguity_count": "infinite",
            "t_selected_by_current_MTT_source": False,
            "t0_gives_Phi_15": monodromy_rows[3]["rademacher_Phi"]["text"] == "15",
            "Phi_15_matches_selected_Z64_cost": selected_cost == 15,
            "classification_of_match": "arithmetic clue only; no selected t or multiplier-to-neutral-holonomy normalization",
            "pi_over_120_phase_derived": False,
        },
    }

    operator_fields = {
        "actual_internal_topology": True,
        "selected_relative_family_holonomy_Hcen": bool(a38["theorem"]["proved"]),
        "smooth_neutral_Dirac_or_signature_family": False,
        "internal_metric_and_bundle_connection": False,
        "base_loop_or_mapping_torus": False,
        "spin_or_spinC_structure_and_orientation": False,
        "boundary_condition_or_taming": False,
        "reduced_eta_and_determinant_line_normalization": False,
        "local_counterterm_cancellation_rule": False,
        "holonomy_to_det_Hnu_identification": False,
    }
    operator_packet = {
        "schema": "MTTDaiFreedOperatorSourceContract.v1",
        "status": "DETERMINANT_LINE_FRAMEWORK_APPLICABLE_ONLY_AFTER_EXPLICIT_OPERATOR_FAMILY_SOURCE",
        "primary_framework": {
            "Dai_Freed": "https://arxiv.org/abs/hep-th/9405012",
            "Freed_determinant_lines": "https://arxiv.org/abs/dg-ga/9505002",
            "scope": "Exponentiated eta invariants define determinant-line data and its holonomy only for a specified family of Dirac-type operators with the required geometric structures.",
        },
        "required_source_fields": operator_fields,
        "readiness": {
            "filled": sum(operator_fields.values()),
            "required": len(operator_fields),
            "strict_phase_value_emitted": False,
            "observed_oscillation_data_allowed_as_selector": False,
        },
        "minimal_closing_object": {
            "operator": "D_nu(phi) on S1_cen x L(3,1) x (Gamma\\Nil3), twisted by the selected q79/F,m=1 bundle and Hcen family action",
            "calculation": "compute determinant-line holonomy around a source-selected loop and prove arg hol=3*phi_nu modulo 2*pi",
            "normalization": "derive reduced-eta, orientation and local-term subtraction from the same action",
            "acceptance": "exact phase or certified controlled approximation, with no oscillation datum used to choose operator, loop, spin structure or branch",
        },
    }

    action_markers = {
        "native_product_Y4_x_X6": r"Y_4 \times X_6" in action_text,
        "general_self_adjoint_elliptic_operator": "self-adjoint elliptic operator" in action_text,
        "phase_data_are_Wilson_line_parameters": "Phase data from circle-holonomy parameters (Wilson lines) encoded in $A$." in action_text,
        "regime_local_not_global_microscopic_law": "not asserted to be globally valid on $M_{10}$" in action_text,
        "internal_spectra_left_for_future_computation": "Compute internal Laplacian/Dirac spectra" in action_text,
    }
    native = a43["native_10D_counterfactual"]
    action_packet = {
        "schema": "MTTNative10DActionNeutralSourceAudit.v1",
        "status": "NATIVE10D_ACTION_SUPPORTS_OPERATOR_CONSTRUCTION_BUT_DOES_NOT_SELECT_NEUTRAL_VALUES",
        "source_markers": action_markers,
        "action_scope": {
            "dimension": 10,
            "decomposition": "Y4 x X6",
            "internal_topology_candidate": "S1_cen x L(3,1) x Nil3",
            "operator_in_paper": "an assumed general self-adjoint elliptic L",
            "phase_source_in_paper": "an uncomputed U(1) connection/Wilson line A",
            "claim_tier": "regime-local structural encoding, explicitly not numerically unique",
        },
        "neutral_numeric_source_inventory": {
            "selected_internal_metric": False,
            "selected_neutral_Dirac_operator": False,
            "selected_spectrum": False,
            "selected_Wilson_line_value": False,
            "selected_neutral_overlap": False,
            "selected_absolute_mass_response": False,
        },
        "native_10D_counterfactual": {
            "A_nu_eV2": native["A_nu_eV2"],
            "mu_nu_eV": native["mu_nu_eV"],
            "ratio_to_A40_A_nu": native["ratio_to_A40_A_nu"],
            "matches_profile": native["native_10D_matches_neutral_profile"],
        },
        "source_theorem": {
            "dimension_count_selects_number_of_cost15_operator_blocks": False,
            "native_action_selects_A41_phase": False,
            "native_action_selects_absolute_neutral_scale": False,
            "rejected_11D_shortcut_may_be_reused": False,
            "native_action_is_valid_starting_domain_for_explicit_Dnu": True,
            "statement": "The 10D action supplies the correct Y4 x X6 domain and allows Dirac spectra, overlaps and Wilson-line phases, but leaves the internal metric, operator, connection and numerical overlaps unspecified. Therefore dimension 10 alone cannot emit the attenuation exponent, phase or mass scale.",
        },
    }

    frontier_packet = {
        "schema": "MTTU5FrontierAfterA91.v1",
        "status": "U5_REDUCED_TO_EXPLICIT_NEUTRAL_OPERATOR_FAMILY_PLUS_ONE_ABSOLUTE_SCALE",
        "locked_results": {
            "A38_one_shape_scalar_reduction": True,
            "A40_two_measured_primitive_profile_rows": True,
            "A41_exact_reciprocity_arithmetic": True,
            "A41_conditional_one_scale_compatibility": True,
            "A43_11D_source_route_rejected": True,
            "A90_baseline_non_looping_locks_preserved": a90["non_looping_locks"],
        },
        "corrected_status": {
            "A41_L15_16_selected_lens_source": False,
            "A41_pi_over_120_strict_prediction": False,
            "native_10D_absolute_scale_selected": False,
            "strict_neutral_source_closed": False,
            "minimal_PMNS_profile_coordinate_count_remains": 6,
            "conditional_one_scale_profile_may_be_reported": True,
        },
        "ordered_next_execution": [
            "Fix the spin/spinC structures and left-invariant metric family on the actual S1 x L(3,1) x Nil3 internal space.",
            "Construct the q79/F,m=1-twisted neutral Dirac family D_nu(phi) and its determinant line.",
            "Compute holonomy/reduced eta for every source-admissible spin, orientation and retarded branch; test whether MTT selects one orbit or conjugate pair.",
            "Only after phase selection, contract the same operator Hessian against the 10D action and one universal metrology primitive to emit the absolute scale.",
            "Use the resulting real structure and kernel to decide Dirac versus Majorana and normal versus inverted ordering.",
        ],
        "falsification_or_finality_exit": "If the actual selected-topology determinant calculation leaves a continuous Wilson-line modulus or multiple inequivalent spin branches, prove one-scale profile finality instead of promoting pi/120.",
        "new_continuous_parameters_added": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "selected_topology_marker_found": topology_packet["selected_internal_topology"]["source_marker_found"],
        "retarded_labels_not_promoted_to_lens": not topology_packet["retarded_arithmetic_labels"]["selected_as_lens_parameters"],
        "A41_remainder_reproduced_exactly": mixed == Fraction(1, 240),
        "A41_remainder_is_generic_one_over_hk": mixed == generic_remainder,
        "selected_L31_reference_eta_differs": selected_lens_signature_eta != mixed,
        "all_sample_monodromies_are_SL2Z": all(row["determinant"] == 1 for row in monodromy_rows),
        "rademacher_family_exact": all(row["equals_15_plus_t"] for row in monodromy_rows),
        "operator_contract_not_overclosed": not operator_packet["readiness"]["strict_phase_value_emitted"],
        "all_10D_source_markers_found": all(action_markers.values()),
        "native_10D_near_hit_rejected": native["native_10D_matches_neutral_profile"] is False,
        "U5_profile_count_not_artificially_reduced": frontier_packet["corrected_status"]["minimal_PMNS_profile_coordinate_count_remains"] == 6,
        "no_new_parameter": frontier_packet["new_continuous_parameters_added"] == 0,
    }
    outputs = {
        "topology_typing": str(TOPOLOGY.relative_to(ROOT)).replace("\\", "/"),
        "arithmetic_audit": str(ARITHMETIC.relative_to(ROOT)).replace("\\", "/"),
        "monodromy_ambiguity": str(MONODROMY.relative_to(ROOT)).replace("\\", "/"),
        "operator_contract": str(OPERATOR.relative_to(ROOT)).replace("\\", "/"),
        "native_10D_audit": str(ACTION.relative_to(ROOT)).replace("\\", "/"),
        "U5_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedNeutralDeterminantLineAPSOperatorAndNative10DMassScale.v1",
        "status": STATUS,
        "results": {
            "A41_exact_arithmetic_retained": True,
            "A41_selected_lens_interpretation_rejected": True,
            "pi_over_120_strict_phase_source_closed": False,
            "native_10D_numeric_scale_source_closed": False,
            "explicit_operator_contract_filled": operator_packet["readiness"]["filled"],
            "explicit_operator_contract_required": operator_packet["readiness"]["required"],
            "strict_neutral_U5_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [
            {"path": str(path), "sha256": sha256(path)} for path in paths.values()
        ],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_NeutralDeterminantLineAPSOperator_and_Native10DMassScale_v1",
        "status": STATUS,
        "selected_internal_topology": "S1_cen x L(3,1) x Nil3",
        "A41_remainder_exact": "1/240",
        "A41_remainder_is_generic_reciprocity_term": True,
        "L15_16_selected_by_MTT": False,
        "monodromy_bottom_row_has_infinite_lifts": True,
        "operator_contract_readiness": f"{operator_packet['readiness']['filled']}/{operator_packet['readiness']['required']}",
        "strict_phase_source_closed": False,
        "strict_scale_source_closed": False,
        "strict_U5_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Neutral Determinant-Line APS Operator and Native 10D Mass Scale v1

## Exact correction

The selected internal space used by the Theta program is

```text
S1_cen x L(3,1) x (Gamma\\Nil3), with internal dimension 1+2+3=6.
```

The integers `15` and `16` are selected as a Z64 Hessian cost and a
quarter-turn/retarded label. No current source theorem identifies them with a
Lens space `L(16,15)` or with a mapping-torus monodromy. A41's arithmetic remains
exact:

```text
12(s(15,16)+s(16,15))+3-15/16-16/15 = 1/240.
```

But this is the universal reciprocity remainder `1/(h*k)` at `h=15,k=16`.
For the selected ordinary Lens factor, `s(1,3)=1/18`; the reference
odd-signature eta value in the standard orientation convention is `-2/9`, not
`1/240`. This comparison does not rule out a twisted neutral Dirac invariant;
it proves that the operator and twist must be constructed explicitly.

## Monodromy ambiguity

Even if `(16,15)` is provisionally read as the bottom row of an `SL(2,Z)`
matrix, it admits the infinite family

```text
gamma_t = [[15+16t, 14+15t], [16,15]],  t in Z
```

have determinant one. Their Rademacher invariant is exactly `15+t`. The `t=0`
value `15` is an interesting contact with the selected cost, but the bottom row
does not select `t`, and no multiplier normalization currently turns it into
`phi_nu=pi/120`.

## Native 10D action

The ProtoSpinor action supplies a valid structural domain `Y4 x X6`, a general
self-adjoint elliptic operator, and Wilson-line phase variables. It explicitly
leaves the internal metric, spectrum and overlap computation open. The native
10D attenuation counterfactual gives `A_nu={native['A_nu_eV2']} eV^2`, a factor
`{native['ratio_to_A40_A_nu']}` from the A40 profile, so dimension counting is
not a numerical source law. The old target-ranked 11D near-hit remains retired
as a proof source.

## Sharpened U5 frontier

The determinant-line contract is currently
`{operator_packet['readiness']['filled']}/{operator_packet['readiness']['required']}`:
the actual topology and relative `H_cen` family action are available. The next
object must specify the smooth neutral Dirac family, metric/connection, base
loop or mapping torus, spin structure, orientation, boundary/taming,
eta/determinant normalization, counterterm cancellation and the map to
`det H_nu`.

A40's two-primitive neutral profile remains closed. A41's one-scale profile may
be reported only as target-ranked conditional compatibility. No parameter is
added here and the minimal PMNS profile count remains six.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (TOPOLOGY, topology_packet),
        (ARITHMETIC, arithmetic_packet),
        (MONODROMY, monodromy_packet),
        (OPERATOR, operator_packet),
        (ACTION, action_packet),
        (FRONTIER, frontier_packet),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
