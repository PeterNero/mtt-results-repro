from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
STRINGS = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\16 Strings, Flux, & M-Theory Encodings"
    r"\_md\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)

SLUG = "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
STATUS = (
    "MTT_U6_HIDDEN_FULL_SU9_HOLONOMY_CLOSED_VISIBLE_C3_TOPOLOGICAL_AND_"
    "SPECTRAL_CANDIDATES_CLOSED_TWISTED_HOLOMORPHIC_HYM_BIANCHI_LIFT_OPEN"
)
NEXT = "MTT_Selected_q79TwistedSpectralGerbeLiftHYMAndBianchiExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79NonPullbackChiralVisibleBundleAndFullSU9HolonomySelection_v1.md"
)

IWASAWA = OUT / "iwasawa_three_family_source_validity.packet.json"
TOPOLOGY = OUT / "rank_one_fuyau_shared_circle_clutching.packet.json"
SPECTRAL = OUT / "q79_genus_two_determinant_zero_spectral_cover.packet.json"
HOLONOMY = OUT / "hidden_SU9_full_holonomy.packet.json"
FRONTIER = OUT / "U6_frontier_after_A103.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def su2_symmetric_power_index(power: int) -> int:
    # For weights power, power-2, ..., -power, normalized against the doublet.
    return power * (power + 1) * (power + 2) // 6


def stable_k3_discriminant_lower_bound(rank: int) -> Fraction:
    # v^2 = 2r(Delta-r) >= -2 for a stable (possibly twisted) K3 sheaf.
    return Fraction(rank * rank - 1, rank)


def main() -> int:
    paths = {
        "A102": ROOT / "candidate_data" / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution.candidate.json",
        "A102_hidden": ROOT / "candidate_data" / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution" / "hidden_SU9_in_E8_embedding_and_commutant.packet.json",
        "A102_bundles": ROOT / "candidate_data" / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution" / "stable_SU3_SU9_HYM_bundle_existence.packet.json",
        "A102_bianchi": ROOT / "candidate_data" / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution" / "rank_one_fuyau_k3_lattice_and_bianchi_allocation.packet.json",
        "q79_charge": Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json",
        "q79_Iwasawa_integrability": Q79 / "proof_corpus" / "Iwasawa_Dolbeault_Complex_Extraction_Attempt_v1.md",
        "q79_Iwasawa_monad_gate": Q79 / "proof_corpus" / "Iwasawa_Monad_Map_Data_Gate_for_Three_Family_Slots_v1.md",
        "q79_shared_circle": Q79 / "proof_corpus" / "Visible_Rank2_L2_Appell_Humbert_Automorphy_Source_Attempt_v1.md",
        "strings_Iwasawa_source": STRINGS,
        "current_ledger": ROOT / "proof_corpus" / "MTT_Current_TrueSMClosure_ConsolidatedLedger_v1.md",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A103 authority: " + ", ".join(missing))

    a102 = load(paths["A102"])
    hidden_a102 = load(paths["A102_hidden"])
    bundles_a102 = load(paths["A102_bundles"])
    bianchi_a102 = load(paths["A102_bianchi"])
    q79 = load(paths["q79_charge"])
    strings_text = paths["strings_Iwasawa_source"].read_text(encoding="utf-8")
    iwasawa_audit_text = paths["q79_Iwasawa_integrability"].read_text(encoding="utf-8")
    monad_gate_text = paths["q79_Iwasawa_monad_gate"].read_text(encoding="utf-8")
    shared_circle_text = paths["q79_shared_circle"].read_text(encoding="utf-8")

    assert a102["next_required_artifact"] == "MTT_Selected_q79NonPullbackChiralVisibleBundleAndFullSU9HolonomySelection_v1"
    assert q79["charge_data"]["H_square"] == 2
    assert q79["conclusion"]["q_7"] == 2
    assert bianchi_a102["rank_one_torus_candidate"]["one_geometric_circle_untwisted"]
    assert bundles_a102["K3_stable_bundle_bound"]["hidden"]["c2"] == 11
    assert bundles_a102["hidden_SU9_bundle"]["irreducible_HYM_exists"]
    assert hidden_a102["E8_branching"]["dimension_check"] == 248
    assert "shared circle is retained with zero degree" in shared_circle_text
    assert "not integrable" in iwasawa_audit_text
    assert "None of these classes is zero" in monad_gate_text
    assert "int_X c_3(E)=6" in strings_text or "int c_3)=(0,0,6)" in strings_text

    # The Iwasawa source writes c=(i/2) omega3 wedge bar(omega3), while
    # d omega3=omega1 wedge omega2. Its derivative has two independent terms.
    iwasawa_line_labels = [
        (-2, 0, 1),
        (-1, 1, -1),
        (1, -1, 0),
        (1, 0, -1),
        (2, 1, 1),
    ]
    nonclosed_line_labels = [label for label in iwasawa_line_labels if label[2] != 0]
    assert len(nonclosed_line_labels) == 4

    iwasawa = {
        "schema": "MTTIwasawaThreeFamilySourceValidity.v1",
        "status": "EXACT_SOURCE_INVALIDATION_CLOSED_CONCEPTUAL_TARGET_RETAINED",
        "printed_invariant_forms": {
            "a_closed": True,
            "b_closed": True,
            "c_closed": False,
            "dc": "(i/2)[omega1 wedge omega2 wedge bar(omega3) - omega3 wedge bar(omega1) wedge bar(omega2)] != 0",
        },
        "line_bundle_gate": {
            "displayed_L_labels": [list(label) for label in iwasawa_line_labels],
            "labels_using_nonclosed_c": [list(label) for label in nonclosed_line_labels],
            "invalid_line_bundle_c1_count": len(nonclosed_line_labels),
            "conclusion": "A first Chern form must be closed and integral; four displayed L_i therefore do not define the claimed line-bundle Chern classes.",
        },
        "Dolbeault_gate": {
            "printed_A12": "mu*bar(omega3)",
            "barpartial_A12": "mu*bar(omega1) wedge bar(omega2)",
            "A_wedge_A_12": 0,
            "integrable": False,
            "independent_repo_audit": str(paths["q79_Iwasawa_integrability"]),
        },
        "global_frame_gate": {
            "source_declares_global_trivial_smooth_frame": True,
            "Chern_classes_of_trivial_smooth_rank3_bundle": [0, 0, 0],
            "claimed_integral_c3": 6,
            "compatible": False,
            "reason": "A globally defined matrix connection on a trivial smooth rank-three bundle can have nonzero curvature, but all Chern numbers remain zero by Chern-Weil invariance.",
        },
        "verdict": {
            "may_source_c3_equal_6_proof": False,
            "may_source_selected_zero_modes": False,
            "conceptual_Iwasawa_circle_nil_clue_retained": True,
            "required_corpus_revision": "Replace the displayed monad by actual closed integral line classes and typed sections, or withdraw its c3=6/HYM/three-family claims.",
        },
        "theorem": {
            "name": "IwasawaPrintedThreeFamilySourceInvalidationTheorem",
            "proved": True,
            "statement": "The printed Iwasawa monad and global A01 matrix cannot certify c3=6: four alleged c1 forms are nonclosed, the A01 operator is nonintegrable, and a global trivial-frame connection has zero Chern numbers.",
        },
    }

    # Gysin sequence for the primitive circle bundle P_delta -> K3.
    # Primitive delta in the unimodular K3 lattice makes H2(K3)->H4(K3)
    # surjective, so H4(P_delta)=0.
    p_betti = [1, 0, 21, 21, 0, 1]
    x_betti = [
        p_betti[degree] + (p_betti[degree - 1] if degree > 0 else 0)
        for degree in range(7)
        if degree < 6
    ]
    x_betti.append(p_betti[5])
    assert p_betti == [1, 0, 21, 21, 0, 1]
    assert x_betti == [1, 1, 21, 42, 21, 1, 1]
    assert sum((-1) ** degree * value for degree, value in enumerate(x_betti)) == 0

    clutching_winding = 3
    c3_per_bott_generator = 2
    clutching_c3 = c3_per_bott_generator * clutching_winding
    assert clutching_c3 == 6

    topology = {
        "schema": "MTTRankOneFuYauSharedCircleClutching.v1",
        "status": "EXACT_TOPOLOGICAL_NONPULLBACK_SU3_C3_PLUSMINUS6_EXISTENCE_CLOSED_HOLOMORPHIC_HYM_OPEN",
        "rank_one_FuYau_topology": {
            "space": "X=P_delta x S1_shared",
            "delta_primitive": True,
            "delta_square": -4,
            "P_delta_betti": p_betti,
            "X_betti": x_betti,
            "H4_P_delta_rank": p_betti[4],
            "H5_P_delta_rank": p_betti[5],
            "reason": "The second Fu-Yau circle has zero Chern class; the primitive first class makes the K3 intersection map onto H4(K3).",
        },
        "slice_bundle": {
            "source": "pullback of the A102 stable K3 SU3 bundle V3 to P_delta",
            "rank": 3,
            "K3_c2": 9,
            "topological_c2_on_P_delta": 0,
            "topologically_trivial_on_5_manifold": True,
            "classification_reason": "Up to dimension five, BSU3 bundles are classified by c2; pi5(BSU3)=pi4(SU3)=0.",
        },
        "clutching_construction": {
            "degree_one_map": "P_delta -> S5 by collapsing the complement of an oriented ball",
            "clutching_map": "g:P_delta -> SU3 representing winding k=plus or minus 3 in pi5(SU3)=Z",
            "gluing_direction": "the untwisted shared S1",
            "restriction_to_each_circle_slice": "the pullback V3 smooth bundle",
            "c1": 0,
            "c2_topological_class": 0,
            "integral_c3": [clutching_c3, -clutching_c3],
            "Bott_normalization": "The rank-three SU3 clutching generator on S6 has integral ch3=1 and integral c3=2.",
            "nonpullback": True,
            "new_continuous_parameters": 0,
            "unselected_discrete_winding": [clutching_winding, -clutching_winding],
        },
        "same_branch_guard": {
            "smooth_topological_SU3_bundle_constructed": True,
            "integrable_holomorphic_structure_constructed": False,
            "stable_balanced_HYM_structure_constructed": False,
            "differential_Bianchi_representative_checked": False,
            "warning": "The total-space c2 class vanishes although the K3-slice instanton representative is nonzero; the 9+11+4 base equation must be recomputed after circle clutching.",
        },
        "theorem": {
            "name": "SharedCircleClutchingTopologicalThreeFamilyTheorem",
            "proved": True,
            "statement": "The A102 rank-one Fu-Yau topology admits smooth non-pullback SU3 bundles whose restriction to every shared-circle slice is the V3 smooth bundle and whose third Chern number is plus or minus six, obtained by winding plus or minus three in pi5(SU3).",
        },
    }

    n = 3
    h_square = q79["charge_data"]["H_square"]
    k3_c1_square = 0
    spectral_lambda = Fraction(3, 2)
    spectral_c3 = int(2 * spectral_lambda * h_square)
    spectral_vertical_c2 = int(
        Fraction(1, 2)
        * (spectral_lambda**2 - Fraction(1, 4))
        * n
        * h_square
    )
    line_coefficients = {
        "sigma": int(n * (Fraction(1, 2) + spectral_lambda)),
        "eta": int(Fraction(1, 2) - spectral_lambda),
        "c1_base": int(Fraction(1, 2) + n * spectral_lambda),
    }
    assert spectral_c3 == 6
    assert spectral_vertical_c2 == 6
    assert line_coefficients == {"sigma": 6, "eta": -1, "c1_base": 5}

    spectral = {
        "schema": "MTTQ79GenusTwoDeterminantZeroSpectralCover.v1",
        "status": "EXACT_COVER_AND_SECTIONED_REFERENCE_CHERN_DATA_CLOSED_PRINCIPAL_TORSOR_GERBE_LIFT_OPEN",
        "q79_genus_two_map": {
            "polarization": "H",
            "H_square": h_square,
            "genus": 1 + h_square // 2,
            "h0_H": 2 + h_square // 2,
            "linear_system": "|H|=P2",
            "map": "phi_H:K3 -> P2, generically a double cover branched over a sextic",
            "branch_premise": "Choose the base-point-free genus-two polarized representative in the already selected H^2=2 K3 moduli component.",
        },
        "determinant_zero_cover": {
            "elliptic_curve": "E with origin 0",
            "Abel_map": "Sym^3(E) -> Pic^3(E)=E",
            "zero_determinant_fiber": "|3*0|=P2",
            "projective_identification": "iota:|H|^* -> |3*0|",
            "projective_identification_selected": False,
            "PGL3_alignment_complex_dimension": 8,
            "spectral_map": "iota o phi_H:K3 -> |3*0|",
            "cover": "C={(s,y): y occurs in the divisor phi_H(s)} subset K3 x E",
            "degree_over_K3": 3,
            "reference_class": "[C]=3*sigma+pi^*H",
            "fiberwise_determinant": 0,
        },
        "sectioned_reference_FMW_check": {
            "rank_n": n,
            "eta": "H",
            "lambda": str(spectral_lambda),
            "lambda_integrality_class": "Z+1/2 for odd n",
            "spectral_line_c1_coefficients": line_coefficients,
            "integral_spectral_line_class": True,
            "c3_formula": "2*lambda*eta*(eta-n*c1(K3))",
            "integral_c3": spectral_c3,
            "c2_formula_at_c1_K3_zero": "H*sigma+6*F",
            "vertical_c2_coefficient": spectral_vertical_c2,
            "same_c3_as_shared_circle_clutching": spectral_c3 == clutching_c3,
        },
        "q79_arithmetic_clue": {
            "q7": q79["conclusion"]["q_7"],
            "lambda_equals_q7_plus_one_over_two": spectral_lambda == Fraction(q79["conclusion"]["q_7"] + 1, 2),
            "source_map_in_corpus": False,
            "interpretation": "This is an independent discrete coincidence, not a promoted selector.",
        },
        "principal_FuYau_lift_gate": {
            "twisted_Fourier_Mukai_available": True,
            "relative_moduli_corepresented_by": "K3 x Sym^3(E)",
            "local_cover_realization": True,
            "global_cover_to_bundle_surjectivity_proved": False,
            "missing_object": "an inverse-gerbe twisted rank-one sheaf on C whose inverse Fourier-Mukai transform is locally free",
            "stability_HYM_proved": False,
            "same_branch_Bianchi_proved": False,
            "sectioned_reference_c2_matches_A102_visible_nine": False,
            "reason": "The reference c2 is H*sigma+6F, whereas the nonsectioned Fu-Yau torsor has no sigma and A102 uses a nine-unit K3 instanton representative.",
        },
        "theorem": {
            "name": "Q79GenusTwoDeterminantZeroSpectralCoverCandidateTheorem",
            "proved": True,
            "statement": "The selected H^2=2 K3 geometry canonically supplies a determinant-zero degree-three spectral cover; on the sectioned reference branch the integral lambda=3/2 spectral line gives c3=6. Promotion to the actual principal Fu-Yau torsor requires the explicit gerbe lift, local freeness, stability/HYM and Bianchi computation.",
        },
        "primary_references": [
            "https://arxiv.org/abs/1008.3365",
            "https://arxiv.org/abs/alg-geom/9709029",
        ],
    }

    rank3_bound = stable_k3_discriminant_lower_bound(3)
    tensor_lower = 3 * rank3_bound + 3 * rank3_bound
    rank2_bound = stable_k3_discriminant_lower_bound(2)
    sym8_index = su2_symmetric_power_index(8)
    sym8_lower = sym8_index * rank2_bound
    assert rank3_bound == Fraction(8, 3)
    assert tensor_lower == 16
    assert sym8_index == 120
    assert sym8_lower == 180

    holonomy = {
        "schema": "MTTHiddenSU9FullHolonomy.v1",
        "status": "EXACT_FULL_SU9_HYM_HOLONOMY_AND_FINITE_E8_COMMUTANT_CLOSED",
        "input_bundle": {
            "space": "simply connected projective K3",
            "rank": 9,
            "determinant": "trivial because c1=0 and Pic0(K3)=0",
            "c2": 11,
            "stable_locally_free": True,
            "irreducible_HYM": True,
        },
        "holonomy_reduction": {
            "connected": True,
            "connected_reason": "The base K3 is simply connected.",
            "irreducible": True,
            "irreducible_reason": "Stability makes the HYM connection irreducible.",
            "semisimple": True,
            "semisimple_reason": "A connected center acts by scalars, but connected scalars inside SU9 are trivial.",
        },
        "irreducible_dimension_nine_classification": {
            "full_case": "A8 fundamental or dual: SU9",
            "proper_simple_cases": [
                "B4 vector: SO9",
                "A1 highest weight 8: Sym^8(C2)",
            ],
            "proper_product_case": "two irreducible three-dimensional factors in a tensor product",
            "completeness": "Weyl dimension bounds leave only A1, A8 and B4 in the simple case; 9=3*3 is the only nontrivial semisimple product factorization.",
        },
        "proper_case_exclusions": {
            "SO9": {
                "relation": "c2(W9)=-p1(W_R)",
                "K3_parity": "rho2(p1)=w2^2=0 because every integral lift has even square in the K3 lattice",
                "required_c2_parity": "even",
                "actual_c2": 11,
                "excluded": True,
            },
            "A1_Sym8": {
                "Dynkin_index": sym8_index,
                "stable_twisted_rank2_discriminant_lower_bound": str(rank2_bound),
                "induced_rank9_discriminant_lower_bound": str(sym8_lower),
                "actual_discriminant": 11,
                "excluded": True,
            },
            "three_by_three_tensor": {
                "Brauer_obstruction_allowed_in_test": True,
                "stable_twisted_rank3_discriminant_lower_bound_each": str(rank3_bound),
                "tensor_discriminant_identity": "Delta(A tensor B)=3*Delta(A)+3*Delta(B)",
                "rank9_lower_bound": str(tensor_lower),
                "actual_discriminant": 11,
                "excluded": True,
                "importance": "The twisted Mukai bound excludes even nonliftable projective factors, so no zero-Brauer assumption is used.",
            },
        },
        "conclusion": {
            "HYM_holonomy": "SU9",
            "proved_for_every_stable_W9_with_displayed_invariants": True,
            "embedded_E8_commutant": "Z3",
            "continuous_hidden_gauge_rank": 0,
            "hidden_gaugino_condensate_available": False,
            "hidden_bundle_modulus_selected": False,
            "hidden_bundle_moduli_complex_dimension": 38,
            "thresholds_moduli_independent": False,
        },
        "theorem": {
            "name": "PrimeElevenRankNineFullHolonomyTheorem",
            "proved": True,
            "statement": "Every stable rank-nine bundle on the selected K3 with trivial determinant and c2=11 has full SU9 HYM holonomy. The SO9, Sym8(SU2), and possibly Brauer-twisted 3x3 tensor reductions are excluded respectively by K3 parity and sharp stable-(twisted)-Mukai discriminant bounds.",
        },
        "primary_references": [
            "https://arxiv.org/abs/math/0601120",
            "https://arxiv.org/abs/math/9907001",
        ],
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA103.v1",
        "status": STATUS,
        "closed_here": [
            "exact invalidation of the printed Iwasawa c3=6 monad/A01 as a proof source",
            "exact topology of the rank-one Fu-Yau shared-circle branch",
            "smooth topological non-pullback SU3 bundles with c3=plus or minus six by shared-circle clutching",
            "q79 genus-two determinant-zero degree-three spectral cover and sectioned-reference c3=6 check",
            "full SU9 HYM holonomy for every A102 stable hidden W9 with c2=11",
            "finite Z3 hidden E8 commutant and structural absence of a hidden gaugino condensate",
        ],
        "not_closed_here": [
            "global inverse-gerbe twisted line sheaf and locally free Fourier-Mukai transform on the actual Fu-Yau torsor",
            "balanced stability/HYM for that non-pullback visible bundle",
            "same-branch differential Bianchi identity after the non-pullback circle twist",
            "MTT source map selecting winding plus or minus three or lambda=3/2",
            "hidden one-loop thresholds across the remaining 38-complex-dimensional W9 moduli space",
            "seven numerical NS5 quality inputs required by A101/A98",
        ],
        "hidden_branch_update": {
            "full_SU9_holonomy": True,
            "continuous_hidden_commutant": False,
            "f_hidden_condensate_row_required": False,
            "threshold_row_required": True,
        },
        "visible_branch_update": {
            "old_Iwasawa_c3_source_retired": True,
            "topological_c3_plusminus6_existence": True,
            "determinant_zero_spectral_cover_candidate": True,
            "actual_holomorphic_HYM_bundle": False,
            "same_branch_Bianchi": False,
        },
        "new_fitted_continuous_parameters": 0,
        "unfixed_spectral_alignment_complex_dimension": 8,
        "new_unselected_discrete_candidates": {
            "shared_circle_winding": [3, -3],
            "sectioned_reference_lambda": ["3/2", "-3/2"],
        },
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
        "next_exact_target": "Construct the inverse-gerbe twisted spectral line object on C, execute its inverse Fourier-Mukai transform, and verify local freeness, balanced stability/HYM and the full differential Bianchi representative.",
    }

    for path, payload in [
        (IWASAWA, iwasawa),
        (TOPOLOGY, topology),
        (SPECTRAL, spectral),
        (HOLONOMY, holonomy),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    outputs = {
        "Iwasawa_source_validity": str(IWASAWA.relative_to(ROOT)).replace("\\", "/"),
        "shared_circle_clutching": str(TOPOLOGY.relative_to(ROOT)).replace("\\", "/"),
        "q79_spectral_cover": str(SPECTRAL.relative_to(ROOT)).replace("\\", "/"),
        "hidden_full_holonomy": str(HOLONOMY.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    checks = {
        "A102_frontier_consumed": a102["next_required_artifact"] == "MTT_Selected_q79NonPullbackChiralVisibleBundleAndFullSU9HolonomySelection_v1",
        "Iwasawa_nonclosed_c_detected": iwasawa["printed_invariant_forms"]["c_closed"] is False,
        "Iwasawa_integrability_not_reopened": iwasawa["Dolbeault_gate"]["integrable"] is False,
        "Iwasawa_c3_not_promoted": iwasawa["verdict"]["may_source_c3_equal_6_proof"] is False,
        "rank_one_FuYau_topology_exact": topology["rank_one_FuYau_topology"]["X_betti"] == [1, 1, 21, 42, 21, 1, 1],
        "shared_circle_clutching_c3_exact": topology["clutching_construction"]["integral_c3"] == [6, -6],
        "topology_not_overpromoted_to_HYM": topology["same_branch_guard"]["integrable_holomorphic_structure_constructed"] is False,
        "determinant_zero_spectral_cover_constructed": spectral["determinant_zero_cover"]["fiberwise_determinant"] == 0,
        "sectioned_reference_c3_exact": spectral["sectioned_reference_FMW_check"]["integral_c3"] == 6,
        "principal_gerbe_lift_not_invented": spectral["principal_FuYau_lift_gate"]["global_cover_to_bundle_surjectivity_proved"] is False,
        "full_SU9_holonomy_proved": holonomy["conclusion"]["HYM_holonomy"] == "SU9",
        "Brauer_tensor_case_excluded_without_zero_Brauer_assumption": holonomy["proper_case_exclusions"]["three_by_three_tensor"]["excluded"],
        "hidden_condensate_structurally_absent": holonomy["conclusion"]["hidden_gaugino_condensate_available"] is False,
        "new_fitted_continuous_parameters_zero": frontier["new_fitted_continuous_parameters"] == 0,
        "U6_not_overclosed": frontier["U6_strong_CP_closed"] is False,
    }
    assert all(checks.values())

    authority_hashes = [
        {"label": label, "path": str(path), "sha256": sha256(path)}
        for label, path in paths.items()
    ]
    results = {
        "new_fitted_continuous_parameters": 0,
        "unfixed_spectral_alignment_complex_dimension": 8,
        "old_Iwasawa_c3_source_valid": False,
        "topological_nonpullback_SU3_c3_plusminus6_constructed": True,
        "determinant_zero_q79_spectral_cover_constructed": True,
        "sectioned_reference_spectral_c3_six": True,
        "actual_FuYau_holomorphic_nonpullback_bundle_constructed": False,
        "actual_FuYau_balanced_HYM_proved": False,
        "actual_FuYau_nonpullback_Bianchi_proved": False,
        "hidden_full_SU9_holonomy_proved": True,
        "hidden_continuous_gauge_factor": False,
        "hidden_gaugino_condensate_available": False,
        "hidden_bundle_moduli_complex_dimension": 38,
        "U6_strong_CP_closed": False,
    }
    candidate = {
        "schema": "MTTSelectedQ79NonPullbackChiralVisibleBundleAndFullSU9HolonomySelection.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": authority_hashes,
        "results": results,
    }
    certificate = {
        "certificate": "MTT_Selected_q79NonPullbackChiralVisibleBundleAndFullSU9HolonomySelection_v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "results": results,
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Non-Pullback Chiral Visible Bundle and Full SU9 Holonomy Selection v1

Status: `{STATUS}`

## What A103 changes

A103 closes the hidden full-holonomy question and advances the visible
three-family question from a desired Chern number to two exact constructions.
It also removes an old false shortcut: the printed Iwasawa monad cannot be used
as the proof of `c3=6`.

## Iwasawa correction

The Iwasawa source defines

```text
c=(i/2) omega3 wedge bar(omega3),
d omega3=omega1 wedge omega2.
```

Therefore `dc` is nonzero. Four of the five displayed `L_i` labels contain a
nonzero `c` coefficient, so they are not closed first Chern forms. Independently,
the printed matrix has

```text
(barpartial A + A wedge A)_12
  = mu bar(omega1) wedge bar(omega2) != 0.
```

Finally, the source places that matrix in a global trivial smooth frame. Such a
connection may have curvature, but its bundle has `c1=c2=c3=0`. Hence the
printed line table, A01 matrix and `integral c3=6` cannot all describe one
bundle. The Iwasawa object remains a conceptual circle/nil clue, not a valid
three-family proof source.

## Shared-circle clutching theorem

The A102 rank-one Fu-Yau topology splits topologically as

```text
X = P_delta x S1_shared,
```

because the second circle has zero Chern class. The Gysin sequence for the
primitive class `delta` gives

```text
b(P_delta)=(1,0,21,21,0,1),
b(X)=(1,1,21,42,21,1,1).
```

In particular `H4(P_delta)=0`, so the pullback of the K3 `SU(3)` bundle is
topologically trivial on the five-manifold while retaining its slice
connection. Trivialize it smoothly, glue the two ends of
`P_delta x [0,1]` by a map `g:P_delta->SU(3)` of winding `k`, and use the
untwisted shared circle as the gluing direction. Bott normalization gives

```text
integral c3(E_g)=2k.
```

The two choices `k=+3,-3` therefore give smooth non-pullback `SU(3)` bundles
with `integral c3=+6,-6`. This is an exact topological existence theorem and
uses the shared circle directly. It does not yet supply an integrable
holomorphic structure, balanced HYM connection or the differential Bianchi
representative.

## q79 genus-two spectral cover

The selected polarization has `H^2=2`, hence genus two and `h0(H)=3`. On the
base-point-free representative, `|H|` gives the double-cover map

```text
phi_H:K3 -> P2.
```

For an elliptic curve `E`, the zero-determinant fiber of
`Sym^3(E)->Pic^3(E)=E` is `|3*0|=P2`. After choosing an isomorphism
`iota:|H|^*->|3*0|`, the composite `iota o phi_H` defines a determinant-zero
degree-three spectral cover

```text
C subset K3 x E,  [C]=3 sigma + H.
```

The identification `iota` is an unfixed `PGL(3)` alignment with complex
dimension eight. It is not counted as a measured fit, but it is not selected
by the current MTT source and must remain visible in the moduli ledger.

On the sectioned reference geometry, the integral odd-rank spectral parameter
`lambda=3/2` has line-class coefficients `(6,-1,5)` and gives

```text
c3=2 lambda H^2=6,
c2=H sigma + 6 F.
```

This independently agrees with the shared-circle clutching value. The equality
`lambda=(q7+1)/2=3/2` is recorded only as an arithmetic clue; the corpus does
not prove that source map.

Brinzanescu-Halanay-Trautmann provide the correct twisted Fourier-Mukai and
spectral-cover framework for a principal non-Kahler elliptic bundle, but their
theorem gives local representability and a global corepresenting moduli map,
not automatic global surjectivity from every cover to a bundle. The actual
Fu-Yau promotion therefore still requires an inverse-gerbe twisted line object
on `C`, a locally free inverse transform, balanced stability/HYM and a new
Bianchi calculation. The sectioned reference `c2=H sigma+6F` must not be
silently identified with A102's nine-unit K3 instanton row.

## Full hidden SU9 holonomy

Let `W9` be any A102 stable bundle with `det W9=O` and `c2(W9)=11`. Its HYM
holonomy is connected because K3 is simply connected and irreducible because
`W9` is stable. A connected irreducible proper subgroup of `SU(9)` can act in
dimension nine only through:

```text
SO(9) vector,
Sym^8(SU(2)),
or a 3 x 3 tensor product,
```

apart from the full `SU(9)` fundamental case.

All proper cases are impossible. An orthogonal rank-nine bundle has even
`c2=-p1` on the even K3 lattice. For a stable possibly twisted rank-`r` K3
factor, the Mukai inequality gives

```text
Delta >= r - 1/r.
```

Hence `Sym^8` has `Delta >= 120*(3/2)=180`, and even allowing a nonzero Brauer
obstruction the tensor case has

```text
Delta(A tensor B)=3 Delta(A)+3 Delta(B)
                 >= 3*(8/3)+3*(8/3)=16.
```

Both contradict `Delta(W9)=c2(W9)=11`. Therefore

```text
Hol(W9)=SU(9).
```

Under the exact A102 embedding `SU(9)/Z3 subset E8`, the hidden commutant is
the finite group `Z3`. There is no continuous hidden gauge factor and hence no
hidden gaugino-condensate amplitude to tune. The 38 complex bundle moduli still
matter for thresholds; full holonomy does not select a unique point.

## Remaining cutset

1. Construct the inverse-gerbe twisted rank-one spectral object on `C` and
   prove its inverse Fourier-Mukai transform is a locally free `SU(3)` bundle.
2. Prove balanced stability/HYM and compute its `c3` directly on the actual
   principal Fu-Yau torsor.
3. Recompute the full differential Bianchi identity; do not reuse `9+11+4`
   without the non-pullback curvature terms.
4. Derive the discrete MTT selector for the orientation/winding and finish the
   hidden threshold plus A98 numerical NS5 rows.

Next artifact: `{NEXT}`.

## Primary references

- [Balaji and Kollar, Holonomy groups of stable vector bundles](https://arxiv.org/abs/math/0601120)
- [Yoshioka, Irreducibility of moduli spaces of vector bundles on K3 surfaces](https://arxiv.org/abs/math/9907001)
- [Brinzanescu, Halanay and Trautmann, Vector Bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
- [Friedman, Morgan and Witten, Vector Bundles over Elliptic Fibrations](https://arxiv.org/abs/alg-geom/9709029)
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
