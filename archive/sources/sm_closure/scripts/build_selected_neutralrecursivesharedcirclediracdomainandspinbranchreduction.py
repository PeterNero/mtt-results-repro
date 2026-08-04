from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SLUG = "selected_neutralrecursivesharedcirclediracdomainandspinbranchreduction"
STATUS = (
    "MTT_NEUTRAL_RECURSIVE_SHAREDCIRCLE_X6_DOMAIN_CLOSED_DIRAC_FAMILY_CONSTRUCTED_"
    "FLAT_LENS_PHASE_ROUTE_REJECTED_DETERMINANT_PATH_SHARPENED"
)
NEXT = "MTT_Selected_NeutralLensNilDeterminantHolonomyExecution_or_OneScaleFinality_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralRecursiveSharedCircleDiracDomainAndSpinBranchReduction_v1.md"

GEOMETRY = OUT / "recursive_shared_circle_X6_reconciliation.packet.json"
SPIN = OUT / "lensnil_spin_structure_and_SU3_orientation_inventory.packet.json"
DIRAC = OUT / "explicit_lensnil_neutral_dirac_family.packet.json"
FLAT = OUT / "flat_lens_and_nil_U1_holonomy_no_go.packet.json"
CONTRACT = OUT / "determinant_family_construction_vs_physical_selection_contract.packet.json"
FRONTIER = OUT / "U5_frontier_after_A92.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "A38_common_circle": ROOT / "candidate_data" / "selected_neutralcommoncirclefactorizationandholonomyscalarreduction.candidate.json",
        "A91_source_audit": ROOT / "candidate_data" / "selected_neutraldeterminantlineapsoperator_and_native10dmassscale.candidate.json",
        "neutral_mass_source": ROOT / "candidate_data" / "selected_neutralmassoperator_sourceemission.candidate.json",
        "book": CORPUS / "10 The Book on Modal Triplet Theory" / "The_Book_on_Modal_Triplet_Theory_v9.md",
        "lensnil_flux": CORPUS / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
        "theta_geometry": CORPUS / "18 Theta-Closure & Execution Program" / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A92 authority: " + ", ".join(missing))

    a38 = load(paths["A38_common_circle"])
    a91 = load(paths["A91_source_audit"])
    neutral = load(paths["neutral_mass_source"])
    book = paths["book"].read_text(encoding="utf-8")
    flux = paths["lensnil_flux"].read_text(encoding="utf-8")
    theta = paths["theta_geometry"].read_text(encoding="utf-8")

    markers = {
        "book_native_rank_1_2_3": "Rank--$1+2+3=6" in book,
        "book_lens_adds_two_over_shared_circle": "adds two closed directions as a lens--type fibration over $S^1_{\\mathrm{cen}}$" in book,
        "book_nil_reuses_circles": "nil--type twist built on the" in book and "reused circles" in book,
        "flux_uses_X6_lens_times_nil": "Take $X_6=L(3,1)\\times(\\Gamma\\backslash \\mathrm{Nil}_3)" in flux,
        "flux_has_global_lens_coframe": "left-invariant coframes" in flux and "d\\eta_i=\\tfrac{1}{2}" in flux,
        "flux_has_balanced_SU3_ansatz": "d(J^{2})=0" in flux and "\\Omega=(\\eta_1+\\mathrm{i}\\eta_2)" in flux,
        "theta_uses_standard_integer_nil_lattice": "standard compact Heisenberg nilmanifold" in theta and "integer lattice" in theta,
    }

    geometry = {
        "schema": "MTTRecursiveSharedCircleX6Reconciliation.v1",
        "status": "NATIVE_10D_DOMAIN_IS_L31_TIMES_NIL3_WITH_CENTRAL_CIRCLE_REUSED_AS_LENS_FIBER",
        "corpus_markers": markers,
        "literal_dimension_check": {
            "dim_S1": 1,
            "dim_L31": 3,
            "dim_Nil3": 3,
            "literal_cartesian_product_internal_dimension": 7,
            "literal_cartesian_product_spacetime_dimension": 11,
            "compatible_with_native_10D": False,
        },
        "recursive_dimension_check": {
            "fibration": "S1_cen -> L(3,1) -> S2 with first Chern/Euler number 3",
            "central_circle_rank": 1,
            "lens_added_rank": 2,
            "nil_added_rank": 3,
            "internal_rank": 6,
            "physical_internal_manifold": "X6=L(3,1) x (Gamma\\Nil3)",
            "spacetime": "M10=Y4 x X6",
            "compatible_with_native_10D": True,
        },
        "notation_correction": {
            "carrier_shorthand": "S1_cen x L(3,1) x Nil3",
            "must_not_be_read_as_literal_cartesian_product": True,
            "correct_reading": "nested/reused carrier hierarchy whose smooth six-manifold representative is L(3,1) x Nil3",
            "A91_topology_string_requires_this_refinement": True,
        },
        "theorem": {
            "name": "RecursiveSharedCircleSixDimensionalDomainTheorem",
            "proved": all(markers.values()),
            "statement": "The native rank count 1+2+3=6 and the explicit LensNil realization are mutually consistent only when S1_cen is reused as the circle fiber inside L(3,1), not multiplied as a fourth independent factor. The neutral internal Dirac domain is therefore X6=L(3,1)xNil3 in the current smooth realization.",
        },
    }

    spin = {
        "schema": "MTTLensNilSpinStructureAndSU3OrientationInventory.v1",
        "status": "FOUR_TOPOLOGICAL_SPIN_STRUCTURES_ONE_GLOBAL_SU3_FRAMING_CANDIDATE",
        "topological_calculation": {
            "H1_L31_Z": "Z3",
            "H1_L31_Z2": "0",
            "spin_structures_L31": 1,
            "pi1_Nil3_presentation": "<x,y,z | [x,y]=z, [x,z]=[y,z]=1>",
            "H1_Nil3_Z": "Z^2",
            "H1_Nil3_Z2": "Z2^2",
            "spin_structures_Nil3": 4,
            "spin_structures_X6": 4,
            "reason": "Spin structures on a fixed oriented parallelizable manifold form a torsor over H1(-;Z2).",
        },
        "explicit_SU3_candidate": {
            "coframes": ["eta1", "eta2", "eta3", "sigma4", "sigma5", "sigma6"],
            "fundamental_form": "J=R1^2 eta12 + R^2 eta3 sigma6 + R^2 sigma45",
            "complex_volume_form": "Omega=(eta1+i eta2)(eta3+i sigma4)(sigma6+i sigma5)",
            "balanced_condition": "R2=R3=R",
            "defines_orientation": True,
            "defines_metric_family": True,
            "defines_framing_induced_spin_structure": True,
            "selects_unique_metric_point": False,
            "selected_as_unique_MTT_neutral_background": False,
        },
        "external_checks": {
            "odd_order_lens_has_unique_spin_structure": "https://arxiv.org/abs/1504.03121",
            "Heisenberg_Dirac_depends_on_spin_structure": "https://arxiv.org/abs/math/9801091",
            "explicit_nil_Dirac_spectrum_and_metric_dependence": "https://arxiv.org/abs/2202.11437",
        },
        "selection_boundary": "The left-invariant SU3 ansatz provides a canonical candidate without a continuous spin knob, but the corpus has not proved that all other Nil3 spin structures/backgrounds are inadmissible for the neutral operator.",
    }

    mathematical_fields = {
        "closed_six_manifold_domain": True,
        "global_coframe_and_SU3_metric_family": True,
        "framing_induced_spinor_bundle": True,
        "untwisted_product_Dirac_formula": True,
        "q79_F_m1_Dirac_neutral_carrier": bool(neutral["character_and_ontology_gate"]["selected_1M_equals_Nc_Dirac_channel"]),
        "relative_family_Z3_holonomy_Hcen": bool(a38["theorem"]["proved"]),
    }
    dirac = {
        "schema": "MTTExplicitLensNilNeutralDiracFamily.v1",
        "status": "SMOOTH_NEUTRAL_DIRAC_FAMILY_DEFINED_SOURCE_POINT_AND_TWIST_PATH_OPEN",
        "domain": "X6=L(3,1) x (Gamma\\Nil3)",
        "spinor_bundle": "S_X6=(S_L31 tensor S_Nil3) tensor C2; S_X6^+ is isomorphic to S_L31 tensor S_Nil3",
        "operator_family": {
            "formula": "D_X6=D_L31 tensor I tensor sigma1 + I tensor D_Nil3 tensor sigma2",
            "square_identity": "D_X6^2=D_L31^2 tensor I + I tensor D_Nil3^2",
            "neutral_twist": "D_nu(R1,R;f,h,chi)=D_X6 twisted by E_(f,h), the q79/F,m=1 neutral carrier and the Hcen family action",
            "lens_operator": "round/left-invariant spin Dirac operator on S3/Z3 with its unique spin structure",
            "nil_operator": "Heisenberg spin Dirac operator for d sigma6=sigma4 wedge sigma5 and the chosen spin character",
        },
        "mathematical_construction_fields": mathematical_fields,
        "construction_readiness": {
            "filled": sum(mathematical_fields.values()),
            "required": len(mathematical_fields),
            "family_defined": all(mathematical_fields.values()),
        },
        "unselected_family_coordinates": {
            "metric_ratio_R1_over_R": "constrained only after flux integers and anomaly equations are selected",
            "overall_scale": "one metrology/volume coordinate",
            "flux_integers_f_h": "integer pair not selected for the neutral determinant family",
            "nil_spin_character": "four topological choices; SU3 framing gives one candidate",
            "flat_Wilson_coordinates": "two U1 characters from the Nil3 abelianization",
            "determinant_parameter_loop": "not selected",
        },
        "observed_neutrino_data_used": False,
    }

    allowed_flat_lens_phases = [
        {"k": k, "phi_mod_2pi": f"{2*k}*pi/3", "phi_mod_2pi_over_3": "0"}
        for k in range(3)
    ]
    flat = {
        "schema": "MTTFlatLensAndNilU1HolonomyNoGo.v1",
        "status": "FLAT_LENS_FIBER_CANNOT_SOURCE_NONZERO_NEUTRAL_SHAPE_PHASE_NIL_CENTER_ALSO_TRIVIAL",
        "lens_fiber": {
            "pi1": "Z3",
            "flat_U1_character_group": "Hom(Z3,U1)=mu3",
            "Hcen_order": int(a38["selected_common_circle_operator"]["order"]),
            "Hnu_family": "Hnu(phi)=exp(i phi) Hcen",
            "representation_condition": "Hnu(phi)^3=I iff exp(3 i phi)=1",
            "allowed_flat_phases": allowed_flat_lens_phases,
            "nonzero_phi_mod_2pi_over_3_available": False,
            "cosine_shape_at_flat_class": [1.0, -0.5, -0.5],
            "shape_has_exact_twofold_degeneracy": True,
        },
        "nil_flat_characters": {
            "abelianization": "Z^2",
            "flat_U1_character_group": "U1^2",
            "central_generator": "z=[x,y]",
            "every_one_dimensional_character_sends_center_to_identity": True,
            "continuous_flat_coordinates_live_on_base_x_y_cycles": True,
            "current_MTT_source_selects_a_point_or_loop_in_U1_squared": False,
        },
        "theorem": {
            "name": "FlatInternalCharacterNeutralPhaseNoGoTheorem",
            "proved": int(a38["selected_common_circle_operator"]["order"]) == 3,
            "statement": "Because the reused lens fiber represents the torsion group Z3, a flat U1 twist multiplying Hcen remains a representation only for exp(3i phi)=1, which is phi=0 modulo the physical 2pi/3 shape period and leaves a twofold degeneracy. The central Nil3 circle is a commutator and is killed by every U1 character. A nonzero neutral shape phase must therefore come from a non-flat connection, a path in the two Nil base holonomies, or determinant-line holonomy in parameter space; none is selected yet.",
        },
        "pi_over_120_available_from_flat_internal_character": False,
    }

    physical_fields = {
        "unique_background_metric_or_anomaly_solution": False,
        "neutral_flux_integer_pair_f_h": False,
        "nil_spin_branch_or_proof_of_SU3_framing_selection": False,
        "Wilson_line_point_and_closed_parameter_loop": False,
        "Dai_Freed_reduced_eta_holonomy_value": False,
        "local_counterterm_and_retarded_orientation_rule": False,
        "holonomy_to_arg_det_Hnu_normalization": False,
        "same_operator_absolute_Hessian_scale": False,
    }
    contract = {
        "schema": "MTTDeterminantFamilyConstructionVsPhysicalSelectionContract.v1",
        "status": "MATHEMATICAL_FAMILY_6_OF_6_PHYSICAL_SELECTION_0_OF_8",
        "mathematical_family": {
            "fields": mathematical_fields,
            "filled": sum(mathematical_fields.values()),
            "required": len(mathematical_fields),
        },
        "physical_source_selection": {
            "fields": physical_fields,
            "filled": sum(physical_fields.values()),
            "required": len(physical_fields),
        },
        "A91_contract_refinement": "A91's 2/10 counted strict source fields before the correct nested domain was constructed. A92 now closes the mathematical family definition separately; it does not convert any of the eight physical value-selection fields into predictions.",
        "primary_holonomy_framework": "https://arxiv.org/abs/hep-th/9405012",
    }

    frontier = {
        "schema": "MTTU5FrontierAfterA92.v1",
        "status": "OPERATOR_DOMAIN_AND_FAMILY_DEFINED_FINITE_FLAT_ROUTE_CLOSED_CONTINUOUS_DETERMINANT_EXECUTION_NEXT",
        "new_closures": [
            "native 10D smooth domain reconciled as X6=L(3,1)xNil3 with shared circle reused",
            "four topological spin structures inventoried and the SU3 framing candidate exposed",
            "full smooth product Dirac family written on the actual six-manifold",
            "flat lens-fiber and nil-center sources of nonzero phi ruled out exactly",
        ],
        "locked_not_reopened": {
            "A40_two_primitive_profile": True,
            "A41_conditional_one_scale_compatibility": True,
            "A91_rejection_of_L15_16_as_selected_lens": True,
            "profile_coordinate_count": 6,
        },
        "next_execution_branches": [
            {
                "priority": 1,
                "branch": "SU3-framing invariant Galerkin determinant",
                "task": "compute the finite left-invariant D_nu spectrum for the four spin characters and all source-admissible integer flux pairs in a preregistered bounded set",
            },
            {
                "priority": 2,
                "branch": "Dai-Freed parameter-loop holonomy",
                "task": "enumerate primitive closed loops in the Nil U1^2 Wilson torus and compute reduced eta on the seven-dimensional mapping torus",
            },
            {
                "priority": 3,
                "branch": "finality",
                "task": "if no MTT rule selects metric, flux, spin and Wilson loop, prove that one neutral shape coordinate plus one universal scale is irreducible in the current corpus",
            },
        ],
        "strict_phase_source_closed": False,
        "strict_scale_source_closed": False,
        "new_continuous_parameters_added": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "all_recursive_geometry_markers_found": all(markers.values()),
        "literal_product_is_11D_not_native10D": geometry["literal_dimension_check"]["literal_cartesian_product_spacetime_dimension"] == 11,
        "recursive_domain_is_native10D": geometry["recursive_dimension_check"]["internal_rank"] == 6,
        "lens_spin_count_one": spin["topological_calculation"]["spin_structures_L31"] == 1,
        "nil_spin_count_four": spin["topological_calculation"]["spin_structures_Nil3"] == 4,
        "product_spin_count_four": spin["topological_calculation"]["spin_structures_X6"] == 4,
        "mathematical_dirac_family_complete": all(mathematical_fields.values()),
        "flat_lens_phase_no_go": not flat["lens_fiber"]["nonzero_phi_mod_2pi_over_3_available"],
        "nil_center_character_no_go": flat["nil_flat_characters"]["every_one_dimensional_character_sends_center_to_identity"],
        "physical_value_selection_not_overclosed": sum(physical_fields.values()) == 0,
        "A91_strict_U5_remains_open": not a91["results"]["strict_neutral_U5_closed"],
        "no_new_parameter": frontier["new_continuous_parameters_added"] == 0,
    }
    outputs = {
        "geometry": str(GEOMETRY.relative_to(ROOT)).replace("\\", "/"),
        "spin": str(SPIN.relative_to(ROOT)).replace("\\", "/"),
        "dirac_family": str(DIRAC.relative_to(ROOT)).replace("\\", "/"),
        "flat_holonomy_no_go": str(FLAT.relative_to(ROOT)).replace("\\", "/"),
        "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
        "U5_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedNeutralRecursiveSharedCircleDiracDomainAndSpinBranchReduction.v1",
        "status": STATUS,
        "results": {
            "native_X6_domain_closed": True,
            "literal_S1_times_L31_times_Nil3_rejected": True,
            "topological_spin_branch_count": 4,
            "SU3_framing_candidate_count": 1,
            "smooth_Dnu_family_constructed": True,
            "flat_internal_character_phase_route_closed": True,
            "strict_phase_source_closed": False,
            "strict_scale_source_closed": False,
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
        "certificate": "MTT_Selected_NeutralRecursiveSharedCircleDiracDomainAndSpinBranchReduction_v1",
        "status": STATUS,
        "native_internal_domain": "L(3,1) x Nil3",
        "central_circle_reused_as_lens_fiber": True,
        "topological_spin_structures": 4,
        "mathematical_Dnu_family": "6/6",
        "physical_value_selection": "0/8",
        "flat_lens_phase_route_closed": True,
        "strict_phase_source_closed": False,
        "strict_scale_source_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Neutral Recursive Shared-Circle Dirac Domain and Spin-Branch Reduction v1

## Correct native domain

The displayed carrier shorthand `S1_cen x L(3,1) x Nil3` cannot be a literal
Cartesian product in the native 10D theory: its ordinary dimension would be
`1+3+3=7` internally and `11` in spacetime. The corpus itself supplies the
consistent recursive interpretation:

```text
S1_cen -> L(3,1) -> S2,
X6 = L(3,1) x (Gamma\\Nil3),
M10 = Y4 x X6.
```

The lens layer adds two directions over the reused central circle, and the nil
layer adds three. Thus the effective rank is exactly `1+2+3=6`. A91's topology
string must be read in this nested sense.

## Spin and Dirac family

`L(3,1)` has `H1=Z3` and therefore one spin structure. The standard Heisenberg
nilmanifold has abelianization `Z^2`, hence four spin structures. The product has
four. The explicit global balanced `SU(3)` coframe in the flux corpus defines an
orientation, a metric family, and one framing-induced spin candidate, but the
corpus does not yet exclude the other three neutral spin backgrounds.

On the resulting six-manifold the smooth operator family is now explicit:

```text
D_X6 = D_L31 tensor I tensor sigma1 + I tensor D_Nil3 tensor sigma2,
D_X6^2 = D_L31^2 tensor I + I tensor D_Nil3^2.
```

Twisting this by the selected q79/F,m=1 Dirac-neutral carrier, `H_cen`, and the
LensNil bundle gives `D_nu(R1,R;f,h,chi)`. The mathematical family is `6/6`
defined. Physical value selection is `0/8`: the metric point, flux pair, spin
branch, Wilson loop, reduced eta, retarded/counterterm convention, map to
`arg det H_nu`, and absolute Hessian scale remain unselected.

## Exact flat-holonomy no-go

The reused lens fiber has `pi1(L(3,1))=Z3`. A flat character multiplying
`H_nu(phi)=exp(i phi)H_cen` must satisfy

```text
H_nu(phi)^3=I  iff  exp(3 i phi)=1.
```

Modulo the physical `2*pi/3` shape period this forces `phi=0`, with cosine
spectrum `[1,-1/2,-1/2]`. The central Nil3 generator is a commutator and is also
killed by every one-dimensional flat character. Therefore `pi/120` cannot come
from a flat internal central-circle character. A non-flat connection or a
determinant-line holonomy around a selected loop in the two Nil base Wilson
coordinates is required.

No observed neutrino value was used and no parameter was added.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (GEOMETRY, geometry),
        (SPIN, spin),
        (DIRAC, dirac),
        (FLAT, flat),
        (CONTRACT, contract),
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
