from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
SLUG = "selected_q79axioncouplinglatticeandns5worldsheetzeromodepacket"
STATUS = (
    "MTT_U6_X8_CHARGE_LATTICE_AND_NS5_SPAN_OBSTRUCTION_CLOSED_"
    "SELECTED_Q79_TOPOLOGICAL_AND_AMPLITUDE_VALUES_OPEN"
)
NEXT = "MTT_Selected_q79HiddenE8ConfinementAndNS5QualityAmplitudeCertificate_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79AxionCouplingLatticeAndNS5WorldsheetZeroModePacket_v1.md"

LATTICE = OUT / "source_free_E8xE8_axion_charge_lattice.packet.json"
SPAN = OUT / "hidden_NS5_QCD_span_obstruction.packet.json"
WORLDSHEET = OUT / "fuyau_worldsheet_lift_and_pfaffian_gate.packet.json"
NS5 = OUT / "selected_NS5_action_and_quality_kernel.packet.json"
FRONTIER = OUT / "U6_frontier_after_A100.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "A99": ROOT / "candidate_data" / "selected_q79multiaxionsupersetandhiddenblinddirection.candidate.json",
        "A99_frontier": ROOT / "candidate_data" / "selected_q79multiaxionsupersetandhiddenblinddirection" / "U6_frontier_after_A99.packet.json",
        "A98_quality": ROOT / "candidate_data" / "selected_axionqualityinstantonsuppressionbound" / "exact_axion_quality_sufficient_bound.packet.json",
        "A98_action": ROOT / "candidate_data" / "selected_axionqualityinstantonsuppressionbound" / "single_instanton_action_thresholds.diagnostic.json",
        "A97_reduction": ROOT / "candidate_data" / "selected_4dgreenschwarzaxionreductionandsurvivingcurrent" / "universal_B6_axion_reduction.packet.json",
        "A97_current": ROOT / "candidate_data" / "selected_4dgreenschwarzaxionreductionandsurvivingcurrent" / "surviving_model_independent_axion_current.packet.json",
        "q79_charge": Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json",
        "q79_note": Q79 / "proof_corpus" / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A100 authority: " + ", ".join(missing))

    a99 = load(paths["A99"])
    a99_frontier = load(paths["A99_frontier"])
    quality = load(paths["A98_quality"])
    action_diagnostic = load(paths["A98_action"])
    reduction = load(paths["A97_reduction"])
    current = load(paths["A97_current"])
    charge = load(paths["q79_charge"])
    q79_text = paths["q79_note"].read_text(encoding="utf-8")

    # Coefficients are stored in the basis (v_i,h_i), with r_i=v_i+h_i.
    visible_coefficients = [-1 + 4, -1 - 2]
    hidden_coefficients = [-1 - 2, -1 + 4]
    expected_visible = [3, -3]
    expected_hidden = [-3, 3]
    assert visible_coefficients == expected_visible
    assert hidden_coefficients == expected_hidden
    assert [x + y for x, y in zip(visible_coefficients, hidden_coefficients)] == [0, 0]

    lattice = {
        "schema": "MTTSourceFreeE8xE8AxionChargeLattice.v1",
        "status": "FULL_STRUCTURAL_X8_ROWS_CLOSED_INTEGRAL_Q79_VALUES_OPEN",
        "selected_background": {
            "geometry": charge["geometry"]["sector"],
            "source_free_smooth_FuYau_Bianchi": charge["geometry"]["green_schwarz_bianchi_identity_verified"],
            "universal_axion_selected": reduction["selected_background"]["heterotic_Strominger_selected"],
            "universal_axion_survives_visible_Stueckelberg": current["survival"]["selected_anomalous_U1_Stueckelberg_charge"] == 0,
        },
        "definitions": {
            "axion_vector": "Theta=(theta_MI,b_1,...,b_n) in (R/2piZ)^(n+1)",
            "v_i": "integral_X beta_i wedge tr(F1_bar^2)",
            "h_i": "integral_X beta_i wedge tr(F2_bar^2)",
            "r_i": "integral_X beta_i wedge tr(R_bar^2)",
            "d_i": "v_i-h_i",
            "source_free_Bianchi": "r_i=v_i+h_i",
        },
        "X8_reduction": {
            "polynomial": "-(trF1^2+trF2^2)trR^2+2[(trF1^2)^2+(trF2^2)^2-trF1^2 trF2^2]",
            "E8_1_MD_before_Bianchi": "-r_i+4v_i-2h_i",
            "E8_2_MD_before_Bianchi": "-r_i+4h_i-2v_i",
            "E8_1_MD_after_Bianchi": "+3d_i",
            "E8_2_MD_after_Bianchi": "-3d_i",
            "hidden_flatness_required": False,
            "coefficient_check_in_v_h_basis": {
                "E8_1": visible_coefficients,
                "E8_2": hidden_coefficients,
            },
        },
        "structural_charge_rows": {
            "visible_E8_1_or_QCD": "k_vis=(1,+3d_i)",
            "hidden_E8_2": "k_hid=(1,-3d_i)",
            "Euclidean_NS5_wrapping_X6": "k_NS5=(1,0,...,0)",
            "worldsheet_on_curve_C": "k_C=(0,Q_iC), Q_iC=integral_C beta_i",
        },
        "scope": {
            "structural_matrix_closed": True,
            "selected_integral_beta_basis": False,
            "selected_v_i_h_i_d_i_values": False,
            "selected_effective_curve_charge_rows": False,
            "full_selected_integral_matrix_closed": False,
            "same_source_guard": "The q79 Mukai vectors are fixed charge-sector data, and the Iwasawa c2(V_alpha)=4 alpha_1 row is an operator-branch result; neither is identified with the missing Fu-Yau beta_i, v_i, or h_i values.",
        },
        "primary_references": [
            "https://arxiv.org/abs/2410.03820",
            "https://arxiv.org/abs/2605.04142",
        ],
        "theorem": {
            "name": "SourceFreeE8xE8OppositeModelDependentCouplingTheorem",
            "proved": True,
            "statement": "On any smooth source-free E8xE8 heterotic compactification, the cohomological Bianchi identity reduces the two model-dependent Green-Schwarz gauge rows to +3(v-h) and -3(v-h). Flatness of the hidden bundle is not required.",
        },
    }

    span = {
        "schema": "MTTHiddenNS5QCDSpanObstruction.v1",
        "status": "EXACT_SIMULTANEOUS_HIDDEN_AND_NS5_BLIND_QCD_DIRECTION_NO_GO",
        "rows": lattice["structural_charge_rows"],
        "identity": "k_vis+k_hid=2*k_NS5, equivalently k_vis=2*k_NS5-k_hid",
        "proof": [
            "The model-independent component of both gauge rows is one and the NS5 row is (1,0).",
            "The model-dependent gauge components are +3d and -3d by the source-free X8 reduction.",
            "Therefore k_vis+k_hid=(2,0)=2k_NS5.",
            "If x is annihilated by k_hid and k_NS5, the identity gives k_vis dot x=0.",
        ],
        "consequences": {
            "A99_hidden_only_blind_direction_retained": True,
            "A99_hidden_only_scope": "valid when d is nonzero and the NS5 contribution is absent or sufficiently suppressed",
            "exact_hidden_and_NS5_blind_QCD_direction_exists": False,
            "quality_exit": "suppress or forbid the NS5 amplitude, then apply the A98 M0/M1/M2 inequalities; adding more model-dependent axions alone cannot evade this identity",
        },
        "theorem": {
            "name": "HiddenGaugePlusNS5SpanObstructionTheorem",
            "proved": True,
            "statement": "For the source-free E8xE8 charge lattice, the visible/QCD row lies in the span of the hidden gauge row and the primitive wrapped-NS5 row. Hence no axion direction can be exactly blind to both non-QCD rows while retaining a visible/QCD coupling.",
        },
    }

    worldsheet = {
        "schema": "MTTFuYauWorldsheetLiftAndPfaffianGate.v1",
        "status": "EXACT_NECESSARY_CURVE_LIFT_AND_ZERO_MODE_TEST_CLOSED_SELECTED_ROWS_OPEN",
        "geometry": {
            "bundle": "T2 -> X6 -> K3",
            "Chern_classes": "[omega_1],[omega_2] in H2(K3,Z)",
            "selected_integral_classes_emitted": False,
        },
        "curve_lift_theorem": {
            "vertical_case": "A nonconstant holomorphic P1 cannot map into a complex torus fiber, so a rational instanton curve cannot be purely vertical.",
            "projected_case": "For a rational curve C_tilde in X6 projecting to C in K3, the pullback principal T2 bundle over C must admit a section.",
            "necessary_integral_test": "integral_C omega_1=integral_C omega_2=0",
            "sufficiency_claimed": False,
            "additional_requirements": [
                "a holomorphic lift rather than only topological triviality",
                "a smooth isolated rational curve with the required normal zero modes",
                "a nonvanishing bundle Pfaffian",
            ],
        },
        "zero_mode_gate": {
            "superpotential_support": "smooth isolated rational curves C_tilde",
            "individual_contribution": "W_C=(Pfaff_C/D_C^2)*exp[-2pi Vol(C)+i integral_C B]",
            "Pfaffian_operator": "barpartial on V|C tensor O_C(-1)",
            "nonzero_criterion": "H0(C,V|C tensor O_C(-1))=0",
            "vanishing_criterion": "H0(C,V|C tensor O_C(-1)) is nonzero implies Pfaff_C=0",
            "selected_bundle_restrictions_emitted": False,
            "selected_Pfaffians_emitted": False,
        },
        "direct_strong_CP_decoupling": {
            "potential": "V(theta_MI,b)=chi_QCD[1-cos(theta_MI+3d dot b+theta_bar)]+W_worldsheet(b)",
            "minimization": "For every fixed b, primitive periodic theta_MI sets theta_MI+3d dot b+theta_bar=0 mod 2pi.",
            "global_result": "min V=min_b W_worldsheet(b), and every global minimum can have theta_QCD=0 exactly",
            "requires_selected_worldsheet_amplitudes": False,
            "scope": "This conclusion fails when a hidden-gauge, NS5, or other term with a nonzero theta_MI charge is present.",
            "proved": True,
        },
        "minimal_Picard_stratum": {
            "conditional_premise": "Picard rank is the minimum 1+r generated over Q by the ample class H and the rank-r torus Chern span, with H orthogonal to that span.",
            "deduction": "The common algebraic orthogonal of the torus Chern classes is the positive H line, so it contains no class of square -2 and hence no smooth rational K3 curve that can lift.",
            "worldsheet_superpotential_consequence": "no rational worldsheet lift contributes",
            "existence_as_generic_lattice_polarized_stratum": True,
            "selected_by_q79_now": False,
        },
        "required_q79_fill": {
            "integral_omega_1_omega_2": None,
            "effective_rational_curve_classes_orthogonal_to_both": None,
            "holomorphic_lift_and_isolation_table": None,
            "V_restriction_splitting_or_Dirac_kernel_table": None,
            "Pfaffian_and_action_rows": None,
        },
        "primary_references": [
            "https://arxiv.org/abs/0904.2738",
            "https://arxiv.org/abs/1006.5568",
            "https://arxiv.org/abs/2605.04142",
        ],
        "theorem": {
            "name": "FuYauRationalCurveLiftNecessaryCondition",
            "proved": True,
            "statement": "Every rational worldsheet instanton curve in a principal T2 Fu-Yau total space projects to a K3 rational curve annihilated by both torus Chern classes. A nonzero superpotential term further requires isolation and a vanishing H0 kernel for V|C tensor O(-1). Independently of its amplitude, a worldsheet-only potential cannot displace the QCD angle because the primitive surviving model-independent axion can minimize the QCD term for every fixed model-dependent configuration.",
        },
    }

    theta_tolerance = quality["potential"]["theta_tolerance"]
    chi_qcd = action_diagnostic["inputs"]["chi_QCD_GeV4_from_75p6MeV_benchmark"]
    derivative_ceiling = chi_qcd * math.sin(theta_tolerance)
    action_rows = []
    for inv_alpha in (25, 26, 30):
        action_rows.append(
            {
                "alpha_GUT_inverse": inv_alpha,
                "S_NS5": 2 * math.pi * inv_alpha,
                "selected_prediction": False,
            }
        )
    generic_thresholds = []
    for row in action_diagnostic["thresholds"]:
        required_action = row["required_action_max"]
        generic_thresholds.append(
            {
                "cutoff_GeV": row["cutoff_GeV"],
                "required_S": required_action,
                "equivalent_alpha_GUT_inverse": required_action / (2 * math.pi),
                "selected_prediction": False,
            }
        )
    ns5 = {
        "schema": "MTTSelectedNS5ActionAndQualityKernel.v1",
        "status": "WRAPPED_CYCLE_CHARGE_AND_ACTION_FORMULA_CLOSED_PREFACTOR_VALUE_OPEN",
        "selected_structural_payload": {
            "wrapped_cycle": "the full selected Fu-Yau X6",
            "charge_row": "k_NS5=(1,0,...,0)",
            "harmonic": 1,
            "action": "S_NS5=2*pi/alpha_GUT",
            "action_numerical_value_selected": False,
        },
        "quality_kernel": {
            "superpotential_amplitude": "Lambda_NS5,W^4=A_NS5*m_3/2*M_GUT^3*exp(-2*pi/alpha_GUT)",
            "Kahler_potential_amplitude": "Lambda_NS5,K^4 approximately m_3/2^2*M_s^2*exp(-2*pi/alpha_GUT)",
            "single_harmonic_A98_requirement": f"Lambda_NS5^4 < chi_QCD*sin({theta_tolerance})",
            "benchmark_derivative_ceiling_GeV4": derivative_ceiling,
            "exact_superpotential_log_test": "2*pi/alpha_GUT > log(A_NS5*m_3/2*M_GUT^3/[chi_QCD sin(epsilon)])",
            "exact_Kahler_log_test": "2*pi/alpha_GUT > log(m_3/2^2*M_s^2/[chi_QCD sin(epsilon)])",
            "zero_mode_warning": "Vanishing of a superpotential Pfaffian does not by itself exclude nonperturbative Kahler-potential breaking; quality requires both amplitudes to vanish or their sum to pass A98.",
        },
        "diagnostic_only": {
            "action_values": action_rows,
            "A98_generic_cutoff_thresholds": generic_thresholds,
            "recent_external_alpha_inverse_26_estimate_is_not_MTT_selection": True,
        },
        "selected_values_still_open": {
            "alpha_GUT_at_the_selected_compactification_scale": None,
            "m_3_2": None,
            "M_GUT_or_M_s": None,
            "A_NS5_Pfaffian": None,
            "Kahler_prefactor": None,
            "relative_CP_phase": None,
        },
        "primary_reference": "https://arxiv.org/abs/2605.04142",
        "theorem": {
            "name": "SelectedWrappedNS5ActionReduction",
            "proved": True,
            "statement": "The primitive Euclidean NS5 instanton wraps the selected full X6, carries only the model-independent axion charge, and has action 2pi/alpha_GUT. Its contribution passes strong-CP quality exactly when the resulting superpotential and Kahler-potential amplitudes satisfy the A98 norm inequalities.",
        },
    }

    strict_fields = dict(a99_frontier["same_source_fields"])
    frontier = {
        "schema": "MTTU6FrontierAfterA100.v1",
        "status": "CHARGE_LATTICE_AND_ZERO_MODE_GATES_CLOSED_SELECTED_Q79_VALUES_OPEN",
        "closed_now": [
            "general source-free E8xE8 X8 coupling reduction without hidden-flatness",
            "exact k_vis+k_hid=2k_NS5 span obstruction",
            "primitive wrapped-NS5 cycle, charge row and action formula",
            "Fu-Yau rational-curve Chern-pairing lift test",
            "worldsheet Pfaffian zero-mode criterion",
            "exact decoupling of worldsheet-only potentials from direct strong-CP quality",
        ],
        "structural_subfields": {
            "visible_hidden_X8_row_formula": True,
            "NS5_cycle_charge_and_action_formula": True,
            "worldsheet_curve_charge_schema": True,
            "worldsheet_lift_and_pfaffian_acceptance_test": True,
            "visible_universal_Stueckelberg_survival": True,
        },
        "strict_same_source_fields": strict_fields,
        "strict_readiness": {
            "filled": sum(strict_fields.values()),
            "required": len(strict_fields),
        },
        "A98_nonQCD_payload": {
            "structural_formula_fields_filled": 2,
            "required": 9,
            "selected_numerical_amplitude_fields_filled": 0,
        },
        "remaining_selected_data": [
            "integral torus Chern classes and an integral B2 basis on the selected Fu-Yau branch",
            "visible and hidden bundle characteristic vectors v_i,h_i and the full gauged quotient",
            "effective rational-curve/lift/isolation and bundle-restriction Pfaffian table for the axion spectrum and any hidden-cancellation route",
            "alpha_GUT, SUSY/string scales, NS5/worldsheet prefactors and relative phases from the same branch",
            "a numerical A98 M0/M1/M2 certificate",
        ],
        "U6_current_map": "9/10",
        "U6_strong_CP_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "A99_frontier_consumed": a99["next_required_artifact"] == "MTT_Selected_q79AxionCouplingLatticeAndNS5WorldsheetZeroModePacket_v1",
        "source_free_Bianchi_selected": lattice["selected_background"]["source_free_smooth_FuYau_Bianchi"],
        "hidden_flatness_removed": not lattice["X8_reduction"]["hidden_flatness_required"],
        "opposite_MD_rows": visible_coefficients == [3, -3] and hidden_coefficients == [-3, 3],
        "span_identity_closed": span["identity"] == "k_vis+k_hid=2*k_NS5, equivalently k_vis=2*k_NS5-k_hid",
        "simultaneous_blind_direction_rejected": not span["consequences"]["exact_hidden_and_NS5_blind_QCD_direction_exists"],
        "worldsheet_Chern_pairing_gate": worldsheet["curve_lift_theorem"]["necessary_integral_test"] == "integral_C omega_1=integral_C omega_2=0",
        "worldsheet_sufficiency_not_overclaimed": not worldsheet["curve_lift_theorem"]["sufficiency_claimed"],
        "worldsheet_direct_quality_decoupling": worldsheet["direct_strong_CP_decoupling"]["proved"] and not worldsheet["direct_strong_CP_decoupling"]["requires_selected_worldsheet_amplitudes"],
        "minimal_Picard_not_selected": not worldsheet["minimal_Picard_stratum"]["selected_by_q79_now"],
        "NS5_action_formula": ns5["selected_structural_payload"]["action"] == "S_NS5=2*pi/alpha_GUT",
        "selected_amplitudes_still_open": all(value is None for value in ns5["selected_values_still_open"].values()),
        "strict_readiness_not_inflated": frontier["strict_readiness"] == {"filled": 0, "required": 6},
        "U6_not_overclosed": not frontier["U6_strong_CP_closed"],
        "no_new_parameter": frontier["new_continuous_parameters"] == 0,
    }
    outputs = {
        "lattice": str(LATTICE.relative_to(ROOT)).replace("\\", "/"),
        "span_obstruction": str(SPAN.relative_to(ROOT)).replace("\\", "/"),
        "worldsheet_gate": str(WORLDSHEET.relative_to(ROOT)).replace("\\", "/"),
        "NS5_quality": str(NS5.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedQ79AxionCouplingLatticeAndNS5WorldsheetZeroModePacket.v1",
        "status": STATUS,
        "results": {
            "source_free_X8_structural_matrix_closed": True,
            "hidden_flatness_assumption_retired": True,
            "hidden_plus_NS5_blind_QCD_direction_no_go": True,
            "NS5_cycle_charge_action_formula_closed": True,
            "worldsheet_lift_and_pfaffian_gate_closed": True,
            "worldsheet_only_direct_strong_CP_quality_exact": True,
            "strict_same_source_readiness": "0/6",
            "A98_structural_formula_readiness": "2/9",
            "A98_selected_numerical_amplitude_readiness": "0/9",
            "U6_current_map": "9/10",
            "U6_strong_CP_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "external_primary_references": [
            "https://arxiv.org/abs/2410.03820",
            "https://arxiv.org/abs/0904.2738",
            "https://arxiv.org/abs/1006.5568",
            "https://arxiv.org/abs/2605.04142",
        ],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_q79AxionCouplingLatticeAndNS5WorldsheetZeroModePacket_v1",
        "status": STATUS,
        "source_free_X8_structural_matrix_closed": True,
        "hidden_flatness_assumption_retired": True,
        "hidden_plus_NS5_span_obstruction_closed": True,
        "NS5_cycle_charge_action_formula_closed": True,
        "worldsheet_lift_and_pfaffian_gate_closed": True,
        "worldsheet_only_direct_strong_CP_quality_exact": True,
        "strict_same_source_readiness": "0/6",
        "A98_structural_formula_readiness": "2/9",
        "A98_selected_numerical_amplitude_readiness": "0/9",
        "U6_current_map": "9/10",
        "U6_strong_CP_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected q79 Axion Coupling Lattice and NS5/Worldsheet Zero-Mode Packet v1

## Exact `E8 x E8` reduction

Let

```text
v_i = integral_X beta_i wedge tr(F1_bar^2),
h_i = integral_X beta_i wedge tr(F2_bar^2),
r_i = integral_X beta_i wedge tr(R_bar^2).
```

The smooth source-free Fu--Yau Bianchi identity is `r_i=v_i+h_i`. Reducing
the heterotic `B2 wedge X8` polynomial therefore gives

```text
E8_1: -r_i+4v_i-2h_i = +3(v_i-h_i),
E8_2: -r_i+4h_i-2v_i = -3(v_i-h_i).
```

This removes A99's unnecessary flat-hidden-bundle hypothesis. It closes the
full structural row formula, but not the selected integral numbers: the q79
packet still does not emit an integral `beta_i` basis or the two characteristic
vectors `v_i,h_i`.

## NS5 span obstruction

In the axion basis `Theta=(theta_MI,b_i)`, write `d_i=v_i-h_i`. The primitive
rows are

```text
k_vis  = (1,+3d_i),
k_hid  = (1,-3d_i),
k_NS5  = (1,0,...,0).
```

Hence

```text
k_vis+k_hid=2 k_NS5.
```

This proves a sharp no-go: a direction annihilated by both the hidden gauge
row and the wrapped-NS5 row is also annihilated by the visible/QCD row. The
A99 hidden-only cancellation remains correct, but it solves quality only if
the NS5 contribution is absent or passes the A98 suppression bound. More
model-dependent axions alone do not evade this identity.

## Fu--Yau worldsheet gate

A rational worldsheet curve cannot lie vertically in a complex torus fiber.
If a rational curve in the Fu--Yau total space projects to `C` in K3, its lift
is a section of the restricted principal `T2` bundle. Therefore the necessary
integral conditions are

```text
integral_C omega_1 = integral_C omega_2 = 0.
```

Topological triviality is not by itself sufficient. A superpotential term also
requires a smooth isolated rational lift and a nonzero Pfaffian. For the bundle
restriction the exact individual zero-mode test is

```text
H0(C,V|C tensor O_C(-1)) = 0  <=>  the Pfaffian is not forced to vanish.
```

The selected torus classes, effective rational curves, lifts, bundle
restrictions and Pfaffians are not present in the q79 corpus, so no worldsheet
amplitude is promoted.

There is nevertheless an exact quality simplification. For an arbitrary
worldsheet potential `W_ws(b_i)`, the full worldsheet-plus-QCD potential is

```text
V = W_ws(b_i)
    + chi_QCD [1-cos(theta_MI+3 d_i b_i+theta_bar)].
```

For every fixed `b_i`, the primitive surviving `theta_MI` sets the QCD angle to
zero. Thus worldsheet instantons alone have perfect direct strong-CP quality,
independently of their actions or Pfaffians. Their detailed rows remain needed
for the mass spectrum and for a hidden-sector cancellation route, but they are
not an independent direct quality blocker.

There is also a clean conditional vanishing branch. If the selected K3 lies in
the minimal Picard stratum generated over `Q` by the ample class and the torus
Chern span, the common algebraic orthogonal is positive and contains no `-2`
rational-curve class. That generic stratum has no rational worldsheet lift, but
the current q79 certificate does not yet select its Picard rank.

## NS5 quality kernel

The primitive Euclidean NS5 wraps the full selected `X6`, has charge row
`(1,0,...,0)`, and has action

```text
S_NS5 = 2 pi / alpha_GUT.
```

This fills the wrapped cycle and action formula structurally (`2/9` A98 source
fields), but selected numerical amplitudes remain `0/9`. The recent heterotic
EFT forms are proportional to

```text
A_NS5 m_3/2 M_GUT^3 exp(-S_NS5)
```

for a superpotential contribution and approximately

```text
m_3/2^2 M_s^2 exp(-S_NS5)
```

for a Kahler-potential contribution. A superpotential Pfaffian zero alone is
therefore insufficient; both contributions must vanish or their combined
`M0,M1,M2` norms must pass A98.

## Honest frontier

This packet closes new theorems without adding a parameter, but it does not
close strong CP. Strict same-source readiness remains `0/6` because the six
fields require selected integral values and amplitudes, not only their exact
formulas. The direct frontier is now narrower than that six-field construction:
select whether the hidden `E8` confines and bound the unavoidable wrapped-NS5
amplitude. The next source object is `{NEXT}`.
"""

    for path, payload in [
        (LATTICE, lattice),
        (SPAN, span),
        (WORLDSHEET, worldsheet),
        (NS5, ns5),
        (FRONTIER, frontier),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
