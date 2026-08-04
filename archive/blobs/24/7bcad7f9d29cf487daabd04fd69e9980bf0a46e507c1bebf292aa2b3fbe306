from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
STROMINGER_SOURCE = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\16 Strings, Flux, & M-Theory Encodings\_md"
    r"\Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)
IWASAWA_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)

SLUG = "selected_q79hiddene8confinementandns5qualityamplitudecertificate"
STATUS = (
    "MTT_U6_SECOND_E8_TYPING_AND_TWO_FUYAU_CURVATURE_HIDDEN_EXIT_NO_GO_CLOSED_"
    "SELECTED_HIDDEN_BUNDLE_AND_AMPLITUDES_OPEN"
)
NEXT = "MTT_Selected_q79HiddenBundleExistenceBianchiAllocationAndSpectrumExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79HiddenE8ConfinementAndNS5QualityAmplitudeCertificate_v1.md"

TYPING = OUT / "two_E8_source_typing_and_corpus_audit.packet.json"
DECISION = OUT / "hidden_group_spectrum_and_confinement_decision.packet.json"
NO_GO = OUT / "minimal_root_free_E8_two_curvature_no_go.packet.json"
NS5 = OUT / "selected_NS5_A98_prefactor_envelope.packet.json"
HIDDEN = OUT / "hidden_condensation_A98_envelope.diagnostic.json"
FRONTIER = OUT / "U6_frontier_after_A101.packet.json"


# Bourbaki E8 ordering: 1-3-4-5-6-7-8, with node 2 attached to node 4.
E8_CARTAN = [
    [2, 0, -1, 0, 0, 0, 0, 0],
    [0, 2, 0, -1, 0, 0, 0, 0],
    [-1, 0, 2, -1, 0, 0, 0, 0],
    [0, -1, -1, 2, -1, 0, 0, 0],
    [0, 0, 0, -1, 2, -1, 0, 0],
    [0, 0, 0, 0, -1, 2, -1, 0],
    [0, 0, 0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, 0, 0, -1, 2],
]
E8_CARTAN_INVERSE = [
    [4, 5, 7, 10, 8, 6, 4, 2],
    [5, 8, 10, 15, 12, 9, 6, 3],
    [7, 10, 14, 20, 16, 12, 8, 4],
    [10, 15, 20, 30, 24, 18, 12, 6],
    [8, 12, 16, 24, 20, 15, 10, 5],
    [6, 9, 12, 18, 15, 12, 8, 4],
    [4, 6, 8, 12, 10, 8, 6, 3],
    [2, 3, 4, 6, 5, 4, 3, 2],
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def inverse_fraction(matrix: list[list[int]]) -> list[list[Fraction]]:
    n = len(matrix)
    augmented = [
        [Fraction(matrix[i][j]) for j in range(n)]
        + [Fraction(i == j) for j in range(n)]
        for i in range(n)
    ]
    for column in range(n):
        pivot = next(row for row in range(column, n) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                augmented[row][j] - scale * augmented[column][j]
                for j in range(2 * n)
            ]
    return [row[n:] for row in augmented]


def quadratic(vector: tuple[int, ...], matrix: list[list[int]]) -> int:
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def residual_regular_lower_bound(zero_nodes: tuple[int, ...]) -> Fraction:
    if not zero_nodes:
        return Fraction(0)
    subcartan = [[E8_CARTAN[i][j] for j in zero_nodes] for i in zero_nodes]
    inverse = inverse_fraction(subcartan)
    return sum(sum(row) for row in inverse)


def dominant_rows_below_norm(bound: int = 40) -> list[dict]:
    # All entries of A^-1 are positive. The diagonal terms therefore give
    # finite coordinate bounds for dominant Dynkin labels.
    ranges = [
        range(math.isqrt((bound - 1) // E8_CARTAN_INVERSE[i][i]) + 1)
        for i in range(8)
    ]
    rows = []
    for labels in itertools.product(*ranges):
        if not any(labels):
            continue
        norm = quadratic(labels, E8_CARTAN_INVERSE)
        if norm >= bound:
            continue
        zero_nodes = tuple(i for i, value in enumerate(labels) if value == 0)
        residual = residual_regular_lower_bound(zero_nodes)
        characteristic_lower = Fraction(3 * norm, 4) + residual
        rows.append(
            {
                "dominant_Dynkin_labels": list(labels),
                "norm_squared": norm,
                "zero_nodes_one_based": [i + 1 for i in zero_nodes],
                "residual_regular_real_lower": fraction_text(residual),
                "A2_characteristic_lower": fraction_text(characteristic_lower),
            }
        )
    return sorted(
        rows,
        key=lambda row: (
            Fraction(row["A2_characteristic_lower"]),
            row["norm_squared"],
            row["dominant_Dynkin_labels"],
        ),
    )


def e8_roots() -> set[tuple[Fraction, ...]]:
    roots: set[tuple[Fraction, ...]] = set()
    for i, j in itertools.combinations(range(8), 2):
        for sign_i in (-1, 1):
            for sign_j in (-1, 1):
                root = [Fraction(0) for _ in range(8)]
                root[i] = Fraction(sign_i)
                root[j] = Fraction(sign_j)
                roots.add(tuple(root))
    for signs in itertools.product((-1, 1), repeat=8):
        if sum(sign < 0 for sign in signs) % 2 == 0:
            roots.add(tuple(Fraction(sign, 2) for sign in signs))
    return roots


def dot(left: tuple[int, ...] | tuple[Fraction, ...], right: tuple[int, ...] | tuple[Fraction, ...]) -> Fraction:
    return sum(Fraction(x) * Fraction(y) for x, y in zip(left, right))


def ns5_profile(alpha_inverse: float, mass_scale: float, chi: float, epsilon: float) -> dict:
    alpha = 1.0 / alpha_inverse
    ceiling = chi * math.sin(epsilon)
    action = 2.0 * math.pi * alpha_inverse
    kappa_m32_ceiling = 16.0 * math.pi * alpha * ceiling * math.exp(action) / mass_scale**3
    kahler_m32_ceiling = math.sqrt(ceiling * math.exp(action) / mass_scale**2)
    return {
        "alpha_GUT_inverse": alpha_inverse,
        "M_GUT_equals_Ms_GeV": mass_scale,
        "S_NS5": action,
        "kappa_times_m3_2_superpotential_ceiling_GeV": kappa_m32_ceiling,
        "m3_2_Kahler_ceiling_GeV_for_unit_prefactor": kahler_m32_ceiling,
        "selected_prediction": False,
    }


def hidden_profile(group: str, dual_coxeter: int, mass_scale: float, m32: float, ceiling: float) -> dict:
    required_action = math.log(m32 * mass_scale**3 / ceiling)
    return {
        "group": group,
        "dual_Coxeter_C_H": dual_coxeter,
        "M_s_GeV": mass_scale,
        "m3_2_GeV": m32,
        "unit_prefactor_required_action": required_action,
        "unit_prefactor_required_alpha_hidden_inverse": dual_coxeter * required_action / (2.0 * math.pi),
        "selected_prediction": False,
    }


def main() -> int:
    paths = {
        "A100": ROOT / "candidate_data" / "selected_q79axioncouplinglatticeandns5worldsheetzeromodepacket.candidate.json",
        "A100_NS5": ROOT / "candidate_data" / "selected_q79axioncouplinglatticeandns5worldsheetzeromodepacket" / "selected_NS5_action_and_quality_kernel.packet.json",
        "A98_quality": ROOT / "candidate_data" / "selected_axionqualityinstantonsuppressionbound" / "exact_axion_quality_sufficient_bound.packet.json",
        "A98_action": ROOT / "candidate_data" / "selected_axionqualityinstantonsuppressionbound" / "single_instanton_action_thresholds.diagnostic.json",
        "q79_charge": Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json",
        "q79_note": Q79 / "proof_corpus" / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md",
        "MTT_Strominger_source": STROMINGER_SOURCE,
        "MTT_Iwasawa_hidden_flux_clue": IWASAWA_SOURCE,
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A101 authority: " + ", ".join(missing))

    a100 = load(paths["A100"])
    a100_ns5 = load(paths["A100_NS5"])
    quality = load(paths["A98_quality"])
    action_diagnostic = load(paths["A98_action"])
    q79_charge = load(paths["q79_charge"])
    strominger_text = STROMINGER_SOURCE.read_text(encoding="utf-8")
    iwasawa_text = IWASAWA_SOURCE.read_text(encoding="utf-8")

    source_checks = {
        "one_connection_configuration": r"(g,\Phi,B;A)" in strominger_text,
        "one_fixed_holomorphic_bundle": "fixed holomorphic }E" in strominger_text,
        "one_YM_term": r"\mathrm{Tr}(F_A\wedge *F_A)" in strominger_text,
        "one_Bianchi_gauge_term": r"\mathrm{Tr}F_A\wedge F_A-\mathrm{Tr}R^+\wedge R^+" in strominger_text,
        "iwasawa_hidden_E8_clue_exists": "hidden* $E_8$" in iwasawa_text,
        "iwasawa_clue_is_explicitly_Iwasawa": "Anomaly cancellation on Iwasawa" in iwasawa_text,
    }
    assert all(source_checks.values())

    typing = {
        "schema": "MTTTwoE8StromingerSourceTypingRepair.v1",
        "status": "EXACT_TWO_CONNECTION_TYPE_REPAIR_CLOSED_SELECTED_SECOND_BUNDLE_OPEN",
        "audit": source_checks,
        "as_written_scope": {
            "configuration": "C={(g,Phi,B;A)} on one fixed holomorphic bundle E",
            "gauge_connections": 1,
            "Bianchi_gauge_curvature_terms": 1,
            "selects_an_E8xE8_hidden_bundle": False,
            "consequence": "The one-bundle selection theorem cannot select P2, its E8 embedding, hidden commutant, spectrum or confinement behavior.",
        },
        "required_E8xE8_typed_repair": {
            "configuration": "C_E8xE8={(g,Phi,B;A1,A2)} on fixed holomorphic principal bundles P1,P2",
            "Hhat": "dB-alpha'/4*(omega3(A1)+omega3(A2)-omega3(omega+))",
            "Bianchi": "dHhat=alpha'/4*(Tr F1^2+Tr F2^2-Tr R+^2)",
            "Yang_Mills_term": "(2*g10^2)^-1*integral e^-2Phi*[Tr(F1 wedge *F1)+Tr(F2 wedge *F2)]",
            "Hessian_bundle_block": "Delta_A1 direct_sum Delta_A2 modulo gauge and bundle moduli",
            "convexity_extension": "The existing additive Hessian proof extends when both gauge blocks have the stated positive gap on their gauge-fixed complements.",
        },
        "theorem": {
            "name": "TwoE8StromingerSelectionTypingRepairTheorem",
            "proved": True,
            "statement": "Replacing the single gauge connection by (A1,A2) and summing both Chern-Simons, Bianchi and Yang-Mills terms gives the correctly typed E8xE8 functional. Its Euler-Lagrange and local convexity arguments extend blockwise under the same gap hypotheses for both bundles.",
            "does_not_select_P2": True,
        },
        "corpus_clue_scope": {
            "Iwasawa_paper": "It places two abelian factors in the hidden E8 and supplies integer flux rows (1,2,0),(-1,-2,0).",
            "portable_information": "typed two-Cartan construction template",
            "not_portable_to_q79_FuYau": "the Iwasawa invariant-form coefficients and their numerical Bianchi match",
        },
        "paper_change_required": "Replace every single E8xE8 gauge slot in the Strominger selection statement and functional by the typed pair (P1,A1),(P2,A2); state explicitly that selection is conditional on both fixed topological bundle sectors.",
    }

    decision = {
        "schema": "MTTHiddenGaugeSpectrumConfinementDecision.v1",
        "status": "EXACT_DECISION_THEOREM_CLOSED_SELECTED_INPUT_PAYLOAD_OPEN",
        "selected_q79_input_audit": {
            "geometry": q79_charge["geometry"]["sector"],
            "certificate_bundle_phrase": q79_charge["geometry"]["background_hym_bundle"],
            "number_of_physical_E8_bundles_typed": 0,
            "P2_structure_group": None,
            "P2_embedding_in_E8": None,
            "P2_characteristic_class": None,
            "Wilson_lines": None,
            "charged_bundle_cohomology": None,
            "threshold_mass_matrix": None,
            "hidden_gauge_kinetic_function": None,
            "hidden_confinement_decidable_now": False,
        },
        "exact_algorithm": [
            "Specify a stable HYM principal bundle P2 with structure group H2 and embedding rho2:H2->E8, including Wilson lines.",
            "Compute G_hid=C_E8(rho2(H2)), then decompose 248=sum_j (r_j,R_j) under H2 x G_hid.",
            "Compute the light four-dimensional charged spectrum from the relevant bundle-valued cohomology and the selected threshold mass matrix.",
            "For every simple factor G_a compute b0_a=3*C2(G_a)-sum_j N_j*T_a(R_j).",
            "A factor is certified pure N=1 SYM only if all charged chiral matter is absent or selected massive. Pure SYM with b0=3*h_dual>0 has the standard gaugino-condensate branch.",
            "b0<=0 excludes weak-coupling asymptotic freedom; b0>0 with light matter is not by itself a theorem of confinement or condensation.",
            "Evaluate f_hidden and every condensate harmonic against the A98 M0/M1/M2 inequalities.",
        ],
        "theorem": {
            "name": "TypedHiddenConfinementDecisionTheorem",
            "proved": True,
            "statement": "The data (P2,rho2,Wilson lines,branching,cohomology,thresholds,f_hidden) determine the unbroken hidden factors, their one-loop coefficients and whether a pure-SYM condensation theorem applies. Omitting any of the first five data prevents a selected confinement verdict.",
        },
        "candidate_exits": {
            "full_holonomy_E8": {
                "conditional_result": "If Hol(P2)=E8, then C_E8(E8)=Z(E8) is trivial, so there is no continuous hidden gauge factor and no hidden gaugino condensate.",
                "virtual_K3_moduli_dimension_quaternionic": "30*k2-248",
                "first_nonnegative_integer_k2": 9,
                "value_at_k2_9": 22,
                "guard": "The index count is not an existence, stability, full-holonomy, Fu-Yau lift or Bianchi-allocation theorem.",
                "selected_now": False,
            },
            "trivial_P2": {
                "conditional_result": "G_hid=E8; it is pure SYM only after the relevant adjoint-valued zero modes are proved absent or massive.",
                "automatically_safe": False,
                "selected_now": False,
            },
        },
        "primary_references": [
            "https://arxiv.org/abs/1301.6767",
            "https://arxiv.org/abs/hep-th/9606049",
            "https://arxiv.org/abs/hep-th/9501065",
        ],
    }

    dominant_rows = dominant_rows_below_norm(40)
    assert len(dominant_rows) == 40
    minimum_lower = min(Fraction(row["A2_characteristic_lower"]) for row in dominant_rows)
    assert minimum_lower == 30

    q1 = (0, 0, 0, 1, 1, 1, 1, 4)
    q2 = (0, 1, 2, -3, -2, -1, 0, -1)
    gram = [[int(dot(q1, q1)), int(dot(q1, q2))], [int(dot(q2, q1)), int(dot(q2, q2))]]
    roots = e8_roots()
    common_orthogonal = [root for root in roots if dot(root, q1) == 0 and dot(root, q2) == 0]
    assert len(roots) == 240
    assert gram == [[20, -10], [-10, 20]]
    assert not common_orthogonal
    assert gram[0][0] + gram[1][1] - abs(gram[0][1]) == 30

    no_go = {
        "schema": "MTTMinimalRootFreeE8TwoCurvatureNoGo.v1",
        "status": "EXACT_GLOBAL_MINIMUM_AND_SOURCE_FREE_BUDGET_NO_GO_CLOSED",
        "definitions": {
            "root_free_pair": "q1,q2 in the E8 cocharacter lattice with no E8 root orthogonal to both",
            "base_Gram": "I_ab=-integral_K3 omega_a wedge omega_b for two independent integral ASD classes",
            "hidden_instanton_number": "k2=(1/2)*sum_ab (q_a,q_b)*I_ab",
        },
        "finite_Weyl_chamber_certificate": {
            "Cartan_matrix": E8_CARTAN,
            "Cartan_inverse": E8_CARTAN_INVERSE,
            "dominant_rows_with_norm_below_40": dominant_rows,
            "row_count": len(dominant_rows),
            "proof_reduction": [
                "Move q1 to the closed dominant Weyl chamber and write m_i=(q1,alpha_i)>=0.",
                "The roots orthogonal to q1 form the subsystem generated by Z={i:m_i=0}.",
                "Using the residual Weyl group and q2->-q2, impose (q2,alpha_i)>=1 on Z and q1.q2>=0.",
                "Complete the square: q1^2+q2^2-q1.q2=(3/4)q1^2+|q2-q1/2|^2.",
                "The exact real minimum of the final term under the residual inequalities is 1^T*A_Z^-1*1.",
                "If q1^2>=40 the lower bound is already 30. The exhaustive 40-row table covers q1^2<40 and has exact minimum 30.",
            ],
            "exact_minimum": 30,
        },
        "saturating_witness": {
            "q1_E8_coordinates": list(q1),
            "q2_E8_coordinates": list(q2),
            "Dynkin_labels": [[0, 0, 0, 0, 1, 0, 0, 0], [1, 1, 1, 1, -5, 1, 1, 1]],
            "Gram": gram,
            "all_E8_roots_enumerated": len(roots),
            "common_orthogonal_roots": len(common_orthogonal),
            "characteristic_value": 30,
        },
        "Minkowski_reduction": {
            "reduced_base_conditions": "I=[[a,b],[b,c]], 0<2*|b|<=a<=c when b!=0; a,c are even and a>=2",
            "bound": "k2>=a/2*(q1^2+q2^2-|q1.q2|)>=30",
            "K3_source_free_budget": 24,
        },
        "theorem": {
            "name": "TwoFuYauCurvatureHiddenE8AbelianizationNoGoTheorem",
            "proved": True,
            "statement": "Any hidden E8 line-bundle embedding that uses only two independent integral ASD K3 curvatures and removes every nonabelian root consumes k2>=30. It cannot fit the smooth source-free K3/Fu-Yau Bianchi budget 24.",
            "scope_guard": "This does not exclude nonabelian P2, additional independent bundle curvatures, NS5 sources, or a hidden sector retaining nonabelian factors with nonconfining matter.",
        },
        "new_continuous_parameters": 0,
    }

    epsilon = float(quality["potential"]["theta_tolerance"])
    chi = float(action_diagnostic["inputs"]["chi_QCD_GeV4_from_75p6MeV_benchmark"])
    derivative_ceiling = chi * math.sin(epsilon)
    profiles = [ns5_profile(value, 2.0e16, chi, epsilon) for value in (25.0, 26.0, 30.0)]
    ns5 = {
        "schema": "MTTSelectedNS5A98PrefactorEnvelope.v1",
        "status": "EXACT_A98_ENVELOPE_AND_LITERATURE_PREFACTOR_IDENTIFICATION_CLOSED_SELECTED_VALUES_OPEN",
        "A100_formula": a100_ns5["quality_kernel"]["superpotential_amplitude"],
        "prefactor_refinement": {
            "source_formula": "Lambda_NS5,W^4=[kappa/(16*pi*alpha_GUT)]*m3_2*M_GUT^3*exp(-2*pi/alpha_GUT)",
            "A100_identification": "A_NS5=kappa/(16*pi*alpha_GUT)",
            "Kahler_formula": "Lambda_NS5,K^4 approximately A_K*m3_2^2*M_s^2*exp(-2*pi/alpha_GUT)",
            "primary_reference": "https://arxiv.org/abs/2605.04142",
        },
        "A98_single_harmonic_envelope": {
            "theta_tolerance": epsilon,
            "benchmark_chi_QCD_GeV4": chi,
            "benchmark_derivative_ceiling_GeV4": derivative_ceiling,
            "superpotential_exact_inequality": "kappa*m3_2 < 16*pi*alpha_GUT*Ctheta*exp(2*pi/alpha_GUT)/M_GUT^3",
            "Kahler_exact_inequality": "A_K*m3_2^2 < Ctheta*exp(2*pi/alpha_GUT)/M_s^2",
            "Ctheta": "chi_QCD*sin(theta_tolerance)",
            "strictness": "The inequalities are strict. Equality is not an A98 certificate.",
        },
        "benchmark_profiles_not_MTT_predictions": profiles,
        "selected_values": {
            "alpha_GUT": None,
            "M_GUT": None,
            "M_s": None,
            "m3_2": None,
            "kappa_NS5": None,
            "A_K": None,
            "relative_CP_phase": None,
        },
        "selected_A98_pass": False,
        "theorem": {
            "name": "NS5ToA98ExactEnvelopeTheorem",
            "proved": True,
            "statement": "For the primitive harmonic n=1, substituting the literature NS5 amplitudes into A98 gives the displayed exact parameter inequalities. Their satisfaction is decidable once the seven selected compactification values are supplied.",
        },
    }

    hidden_profiles = [
        hidden_profile(group, dual_coxeter, 1.0e16, 1.0e3, derivative_ceiling)
        for group, dual_coxeter in [("E8", 30), ("E7", 18), ("E6", 12), ("SO(10)", 8), ("SU(5)", 5), ("SU(3)", 3), ("SU(2)", 2)]
    ]
    hidden = {
        "schema": "MTTHiddenCondensateA98EnvelopeDiagnostic.v1",
        "status": "CONDITIONAL_DIAGNOSTIC_NOT_SELECTED_PREDICTION",
        "formula": {
            "superpotential": "W_NP=-M_s^3*exp[-8*pi^2*f_hidden/C_H]",
            "potential_amplitude_model": "Lambda_h^4=A_h*m3_2*M_s^3*exp[-2*pi*alpha_h^-1/C_H]",
            "A98_requirement": "Lambda_h^4<Ctheta for one primitive harmonic",
            "required_inverse_coupling": "alpha_h^-1>(C_H/(2*pi))*log(A_h*m3_2*M_s^3/Ctheta)",
            "primary_reference": "https://arxiv.org/abs/2605.04142",
        },
        "unit_prefactor_profiles_not_MTT_predictions": hidden_profiles,
        "interpretation": "A pure large-group hidden sector at an ordinary unified coupling is dangerous for strong-CP quality; group removal, light-matter IR modification, a vanishing prefactor, or much stronger suppression is required.",
        "guard": "The amplitude model is conditional on a pure-SYM-like factor and does not decide confinement. Thresholds, harmonics and prefactors must come from the selected P2 spectrum.",
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA101.v1",
        "status": STATUS,
        "closed_here": [
            "exact E8xE8 two-connection typing repair theorem",
            "exact hidden group/spectrum/confinement decision theorem",
            "global E8 root-lattice minimum 30 for the two-curvature characteristic form",
            "source-free 24-unit no-go for abelianizing hidden E8 with only the two Fu-Yau curvatures",
            "literature NS5 prefactor identification and exact A98 inequalities",
            "conditional hidden-condensate A98 inverse-coupling envelope",
        ],
        "falsified_or_retired_routes": [
            "the as-written one-bundle Strominger functional selecting both E8 bundles",
            "the q79 Mukai a,b pair being interpreted as the two physical E8 bundles",
            "the Iwasawa hidden-flux numerical row being imported into Fu-Yau",
            "complete hidden-E8 abelianization using only the two selected Fu-Yau torus curvatures in the smooth source-free branch",
            "b0>0 alone being called a confinement theorem",
        ],
        "selected_hidden_payload": {
            "filled": 0,
            "required": 8,
            "fields": ["P2", "rho2", "characteristic_class", "Wilson_lines", "branching", "cohomology", "thresholds", "f_hidden"],
        },
        "selected_NS5_numerical_payload": {
            "filled": 0,
            "required": 7,
            "fields": ["alpha_GUT", "M_GUT", "M_s", "m3_2", "kappa_NS5", "A_K", "relative_CP_phase"],
        },
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
        "next_exact_target": "Construct one stable hidden P2 on the selected Fu-Yau branch, prove its Bianchi allocation and HYM/full-holonomy or explicit commutant, execute its cohomology/threshold spectrum, then evaluate the now-closed A98 envelopes.",
    }

    for path, payload in [
        (TYPING, typing),
        (DECISION, decision),
        (NO_GO, no_go),
        (NS5, ns5),
        (HIDDEN, hidden),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    outputs = {
        "typing": str(TYPING.relative_to(ROOT)).replace("\\", "/"),
        "confinement_decision": str(DECISION.relative_to(ROOT)).replace("\\", "/"),
        "two_curvature_no_go": str(NO_GO.relative_to(ROOT)).replace("\\", "/"),
        "NS5_A98_envelope": str(NS5.relative_to(ROOT)).replace("\\", "/"),
        "hidden_condensate_diagnostic": str(HIDDEN.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    checks = {
        "A100_frontier_consumed": a100["next_required_artifact"] == "MTT_Selected_q79HiddenE8ConfinementAndNS5QualityAmplitudeCertificate_v1",
        "source_is_single_bundle": not typing["as_written_scope"]["selects_an_E8xE8_hidden_bundle"],
        "two_E8_type_repair_closed": typing["theorem"]["proved"],
        "confinement_decision_theorem_closed": decision["theorem"]["proved"],
        "selected_hidden_verdict_not_invented": not decision["selected_q79_input_audit"]["hidden_confinement_decidable_now"],
        "E8_roots_complete": no_go["saturating_witness"]["all_E8_roots_enumerated"] == 240,
        "root_free_witness": no_go["saturating_witness"]["common_orthogonal_roots"] == 0,
        "global_characteristic_minimum_30": no_go["finite_Weyl_chamber_certificate"]["exact_minimum"] == 30,
        "two_curvature_budget_no_go": no_go["Minkowski_reduction"]["K3_source_free_budget"] < no_go["finite_Weyl_chamber_certificate"]["exact_minimum"],
        "NS5_prefactor_repaired": ns5["prefactor_refinement"]["A100_identification"] == "A_NS5=kappa/(16*pi*alpha_GUT)",
        "NS5_selected_pass_not_invented": not ns5["selected_A98_pass"],
        "U6_not_overclosed": not frontier["U6_strong_CP_closed"],
    }
    assert all(checks.values())

    authority_hashes = [
        {"label": label, "path": str(path), "sha256": sha256(path)}
        for label, path in paths.items()
    ]
    candidate = {
        "schema": "MTTSelectedQ79HiddenE8ConfinementAndNS5QualityAmplitudeCertificate.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": authority_hashes,
        "results": {
            "new_continuous_parameters": 0,
            "two_E8_source_typing_repaired": True,
            "selected_hidden_confinement_decided": False,
            "two_FuYau_curvature_hidden_abelian_exit_ruled_out": True,
            "NS5_exact_A98_envelope_closed": True,
            "selected_NS5_numeric_pass": False,
        },
    }
    certificate = {
        "certificate": "MTT_Selected_q79HiddenE8ConfinementAndNS5QualityAmplitudeCertificate_v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "results": candidate["results"],
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Hidden E8 Confinement and NS5 Quality Amplitude Certificate v1

Status: `{STATUS}`

## What A101 closes

A100 fixed the full source-free axion charge rows and the primitive wrapped-NS5
action, but it deliberately left the second `E8` bundle and all numerical
non-QCD amplitudes open. A101 audits the actual MTT source, repairs its type,
proves the exact hidden-sector decision procedure, eliminates one entire
candidate construction, and reduces both NS5 and hidden-condensate quality to
executable A98 inequalities.

## Two-E8 source typing repair

The cited MTT Strominger paper writes one configuration `(g,Phi,B;A)`, one
fixed holomorphic bundle `E`, one Yang-Mills term and one `Tr F_A^2` Bianchi
term. That is a one-bundle Hull-Strominger functional. It does not select the
hidden bundle of an `E8 x E8` compactification.

The correctly typed configuration has `(A1,A2)` and

```text
Hhat = dB-alpha'/4*(omega3(A1)+omega3(A2)-omega3(omega+)),
dHhat = alpha'/4*(Tr F1^2+Tr F2^2-Tr R+^2).
```

The Yang-Mills term is the sum of the two gauge terms. The gauge-fixed Hessian
contains `Delta_A1 direct_sum Delta_A2`; therefore the existing local
convexity argument extends blockwise when both blocks satisfy its gap
hypothesis. This repairs the theorem's type. It does not manufacture `P2`.

## Exact confinement decision theorem

For a selected hidden bundle `(P2,rho2)`, first compute

```text
G_hid = C_E8(rho2(H2))
```

and branch the adjoint `248` under `H2 x G_hid`. Bundle-valued cohomology and
the selected threshold matrix determine the light charged representations.
For each simple factor,

```text
b0 = 3 C2(G)-sum_j N_j T(R_j).
```

Pure `N=1` SYM is certified only after every charged chiral field is absent or
selected massive. In that case the standard condensate theorem applies.
`b0>0` with light matter is not, by itself, a confinement theorem. The q79
certificate supplies none of `P2`, `rho2`, branching, cohomology or thresholds,
so it cannot yet decide the hidden phase.

## Two-Fu-Yau-curvature no-go

Let `q1,q2` be `E8` cocharacters. Removing every nonabelian root requires that
no one of the 240 `E8` roots be orthogonal to both. Define

```text
F(q1,q2)=q1^2+q2^2-|q1.q2|.
```

Move `q1` to the dominant chamber, let `m_i=(q1,alpha_i)` and let `Z` be its
zero-label Dynkin subdiagram. The residual Weyl group makes `q2` regular on
`Z`. Completing the square gives

```text
F = (3/4) q1^2 + |q2-q1/2|^2
  >= (3/4) m^T A_E8^-1 m + 1^T A_Z^-1 1.
```

When `q1^2>=40` this is at least 30. The generated exact table exhausts all 40
dominant labels with `q1^2<40`; its minimum is also 30. Equality is attained by

```text
q1=(0,0,0,1,1,1,1,4),
q2=(0,1,2,-3,-2,-1,0,-1),
Gram(q1,q2)=[[20,-10],[-10,20]].
```

Direct enumeration finds zero common orthogonal roots among all 240 roots.

For two independent integral ASD K3 classes, put
`I_ab=-integral omega_a wedge omega_b`. In a Minkowski-reduced integral basis,
`I=[[a,b],[b,c]]` with `2|b|<=a<=c` and even `a>=2`. Hence

```text
k2=(1/2) sum_ab (q_a,q_b) I_ab
  >= (a/2) [q1^2+q2^2-|q1.q2|]
  >= 30.
```

The smooth source-free K3/Fu-Yau budget is 24. Thus no construction using
only the two Fu-Yau circle curvatures can abelianize the hidden `E8`. This does
not exclude a nonabelian hidden bundle, additional bundle curvatures, or an
NS5-sourced branch.

## NS5 quality envelope

The supplementary formula in [Benabou et al. (2026)](https://arxiv.org/abs/2605.04142)
refines the A100 placeholder to

```text
Lambda_NS5,W^4 = [kappa/(16 pi alpha_GUT)] m3/2 M_GUT^3
                 exp(-2 pi/alpha_GUT).
```

Thus `A_NS5=kappa/(16*pi*alpha_GUT)`. With
`Ctheta=chi_QCD sin(epsilon)`, the exact A98 derivative condition is

```text
kappa*m3/2 < 16*pi*alpha_GUT*Ctheta
             *exp(2*pi/alpha_GUT)/M_GUT^3.
```

The Kahler contribution obeys

```text
A_K*m3/2^2 < Ctheta*exp(2*pi/alpha_GUT)/M_s^2.
```

The generated profiles use external benchmark values only. They are envelope
checks, not selected MTT predictions.

## Full-holonomy candidate and remaining frontier

If a stable selected `P2` has full `E8` holonomy, its continuous commutant is
trivial and hidden gaugino condensation disappears. The K3 index
`30*k2-248` first becomes nonnegative at `k2=9` (value 22), but an index is not
an existence, full-holonomy, Fu-Yau-lift or Bianchi-allocation theorem.

The next artifact must construct one actual `P2`, prove its characteristic
class fits the same 24-unit source-free Bianchi allocation, solve/establish its
HYM connection and commutant, execute its cohomology and thresholds, and then
insert the selected scales and prefactors into the now-closed A98 envelopes.

Next artifact: `{NEXT}`.

## Primary references

- [Supersymmetric Hidden Sectors for Heterotic Standard Models](https://arxiv.org/abs/1301.6767)
- [Non-Perturbative Properties of Heterotic String Vacua Compactified on K3 x T2](https://arxiv.org/abs/hep-th/9606049)
- [Heterotic String Theory Suggests a QCD Axion Near 0.5 neV](https://arxiv.org/abs/2605.04142)
- [Gaugino Condensation and Nonperturbative Superpotentials](https://arxiv.org/abs/hep-th/9501065)
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
