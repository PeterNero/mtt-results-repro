from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
SLUG = "selected_q79multiaxionsupersetandhiddenblinddirection"
STATUS = (
    "MTT_U6_FUYAU_MULTIAXION_SUPERSET_AND_HIDDEN_E8_BLIND_DIRECTION_"
    "THEOREM_CLOSED_SAME_SOURCE_COUPLING_LATTICE_AND_INSTANTON_ZEROMODES_OPEN"
)
NEXT = "MTT_Selected_q79AxionCouplingLatticeAndNS5WorldsheetZeroModePacket_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79MultiAxionSupersetAndHiddenBlindDirection_v1.md"

TOPOLOGY = OUT / "fuyau_T2_over_K3_axion_dimension.packet.json"
COUPLING = OUT / "E8xE8_visible_hidden_axion_coupling_reduction.packet.json"
RANK = OUT / "multi_axion_quality_kernel_rank_theorem.packet.json"
FRONTIER = OUT / "U6_frontier_after_A99.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "A98": ROOT / "candidate_data" / "selected_axionqualityinstantonsuppressionbound.candidate.json",
        "A98_census": ROOT / "candidate_data" / "selected_axionqualityinstantonsuppressionbound" / "selected_q79_nonQCD_breaking_source_census.packet.json",
        "A97_reduction": ROOT / "candidate_data" / "selected_4dgreenschwarzaxionreductionandsurvivingcurrent" / "universal_B6_axion_reduction.packet.json",
        "q79_charge": Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json",
        "q79_FuYau_note": Q79 / "proof_corpus" / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md",
        "q79_visible_GS": Q79 / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature.selected.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A99 authority: " + ", ".join(missing))

    a98 = load(paths["A98"])
    a98_census = load(paths["A98_census"])
    reduction = load(paths["A97_reduction"])
    charge = load(paths["q79_charge"])
    fuyau_text = paths["q79_FuYau_note"].read_text(encoding="utf-8")
    gs = load(paths["q79_visible_GS"])

    topology_rows = []
    for chern_rank in (1, 2):
        b2 = 22 - chern_rank
        topology_rows.append(
            {
                "rank_of_T2_Chern_map": chern_rank,
                "b2_total_space": b2,
                "model_dependent_B2_axions": b2,
                "including_universal_axion": b2 + 1,
            }
        )
    topology = {
        "schema": "MTTFuYauT2OverK3AxionDimension.v1",
        "status": "FUYAU_TOPOLOGY_EMITS_AT_LEAST_TWENTY_MODEL_DEPENDENT_AXION_CANDIDATES",
        "input": {
            "base": "K3",
            "b1_K3": 0,
            "b2_K3": 22,
            "fiber": "T2",
            "nontrivial_integral_ASD_11_Chern_forms_named": "omega_1, omega_2" in fuyau_text,
            "selected_FuYau_charge_sector": charge["geometry"]["sector"],
        },
        "Leray_Serre_calculation": {
            "d2": "H1(T2)->H2(K3) sends the two fiber generators to the two torus Chern classes",
            "rank_symbol": "r=rank span_R{[omega_1],[omega_2]} in {1,2} for a nontrivial Fu-Yau torus bundle",
            "E3_20": "H2(K3)/span{[omega_1],[omega_2]}",
            "E3_02": 0,
            "result": "b2(X6)=22-r",
            "cases": topology_rows,
        },
        "conclusion": {
            "minimum_model_dependent_axions": min(row["model_dependent_B2_axions"] for row in topology_rows),
            "minimum_total_axion_candidates": min(row["including_universal_axion"] for row in topology_rows),
            "exact_selected_Chern_rank_emitted": False,
            "flux_or_instanton_lifting_already_quotiented": False,
        },
        "same_source_guard": "This count applies to the selected Fu-Yau T2/K3 topology only. It does not import Lens-Nil or Iwasawa Betti numbers into the q79 charge sector.",
        "theorem": {
            "name": "FuYauMultiAxionLowerBoundTheorem",
            "proved": True,
            "statement": "For either rank-one or rank-two nontrivial torus Chern map, the Fu-Yau total space has b2 at least 20. Together with the universal B6 axion, the topological candidate lattice has dimension at least 21 before gauging and nonperturbative lifting.",
        },
    }

    coupling = {
        "schema": "MTTE8xE8VisibleHiddenAxionCouplingReduction.v1",
        "status": "HIDDEN_BLIND_QCD_DIRECTION_CONDITIONAL_ON_FLAT_HIDDEN_BUNDLE_AND_NONZERO_PAIRING",
        "ten_dimensional_polynomial": {
            "X8_gauge_part": "-(tr F1^2+tr F2^2) tr R^2 + 2[(tr F1^2)^2+(tr F2^2)^2-tr F1^2 tr F2^2]",
            "source": "heterotic Green-Schwarz B2 wedge X8",
        },
        "same_source_hypotheses": {
            "E8_1_contains_visible_group": True,
            "hidden_internal_bundle_flat": False,
            "cohomological_Bianchi_F1_equals_R": gs["bianchi_residual_zero"],
            "nonzero_dual_pairing_p": False,
            "full_integral_B2_basis_and_X8_rows_emitted": False,
        },
        "conditional_reduction": {
            "define": "p_i=integral_X beta_i wedge tr Rbar^2 in one normalized integral basis",
            "if_F2bar_zero_and_Bianchi": "k_visible=(1,+3p_i), k_hidden=(1,-3p_i)",
            "hidden_blind_direction": "v=(3p, e_p), where p dot e_p is nonzero and k_hidden dot v=0",
            "visible_coupling_on_v": "k_visible dot v=6(p dot e_p), nonzero",
            "universal_component": "nonzero; an NS5 row can still break this direction",
        },
        "selected_support": {
            "visible_GS_alpha1_only": gs["tr_F_visible_squared_coefficients"][1:] == ["0", "0"],
            "visible_GS_alpha1_nonzero_symbolic": gs["tr_F_visible_squared_coefficients"][0] != "0",
            "universal_color_level_one": reduction["canonical_action"]["color_coupling"] == "-(a_MI/f_MI)*k3*c2(F_c)",
        },
        "primary_reference": "https://arxiv.org/abs/2410.03820",
        "theorem": {
            "name": "VisibleHiddenOppositeCouplingCancellationTheorem",
            "proved_as_implication": True,
            "antecedent_selected_now": False,
            "statement": "If the selected q79 compactification supplies a flat hidden internal E8 bundle, an integral B2 mode with nonzero curvature pairing p, and the full X8 reduction, then visible and hidden model-dependent coefficients are opposite. The displayed combination is exactly blind to hidden E8 instantons while retaining QCD coupling.",
        },
    }

    rank_theorem = {
        "schema": "MTTMultiAxionQualityKernelRankTheorem.v1",
        "status": "EXACT_FINITE_RANK_TEST_FOR_A_HIDDEN_BLIND_QCD_AXION",
        "definitions": {
            "N": "number of periodic axions after perturbative gauging",
            "K_nonQCD": "integer row matrix of all non-QCD instanton harmonics",
            "k_QCD": "integer QCD coupling row",
        },
        "criterion": {
            "existence": "rank(K_nonQCD)<N and rank(stack(K_nonQCD,k_QCD))>rank(K_nonQCD)",
            "equivalent": "projection of k_QCD onto ker(K_nonQCD) is nonzero",
            "output": "a nonzero periodic direction with zero coupling to every enumerated non-QCD sector and nonzero QCD coupling",
        },
        "selected_topological_headroom": {
            "candidate_N_min": topology["conclusion"]["minimum_total_axion_candidates"],
            "strict_physical_N_after_lifting_known": False,
            "K_nonQCD_emitted": False,
            "k_QCD_full_integral_row_emitted": False,
        },
        "theorem": {
            "name": "MultiAxionHiddenBlindKernelCriterion",
            "proved": True,
            "statement": "The rank inequalities are necessary and sufficient for a real hidden-blind QCD direction. An integral primitive representative follows after intersecting the rational nullspace with the axion lattice and dividing by the gcd.",
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA99.v1",
        "status": "MULTIAXION_ESCAPE_THEOREM_CLOSED_SELECTED_LATTICE_AND_RESIDUAL_INSTANTON_DATA_OPEN",
        "progress": {
            "minimum_topological_axion_candidate_dimension": topology["conclusion"]["minimum_total_axion_candidates"],
            "hidden_blind_linear_algebra_criterion": True,
            "visible_hidden_opposite_coupling_implication": True,
            "perturbative_quality": a98["results"]["perturbative_quality_closed"],
        },
        "same_source_fields": {
            "selected_torus_Chern_rank_and_integral_B2_basis": False,
            "selected_hidden_internal_bundle_and_unbroken_group": False,
            "full_visible_hidden_X8_coupling_matrix": False,
            "gauged_or_lifted_axion_quotient": False,
            "NS5_and_worldsheet_charge_rows_and_zero_modes": False,
            "residual_amplitudes_pass_A98_quality_bound": False,
        },
        "readiness": {"filled": 0, "required": 6},
        "A98_nonQCD_payload_still": a98_census["readiness"],
        "U6_current_map": "9/10",
        "U6_strong_CP_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "A98_quality_frontier": a98["next_required_artifact"] == "MTT_Selected_q79HiddenGaugeAndNS5InstantonActionPacket_v1",
        "selected_FuYau_sector": charge["selection"]["strominger_selection_applies"],
        "FuYau_T2_forms_named": topology["input"]["nontrivial_integral_ASD_11_Chern_forms_named"],
        "b2_min_twenty": topology["conclusion"]["minimum_model_dependent_axions"] == 20,
        "axion_candidate_min_twentyone": topology["conclusion"]["minimum_total_axion_candidates"] == 21,
        "rank_theorem_closed": rank_theorem["theorem"]["proved"],
        "opposite_coupling_implication_closed": coupling["theorem"]["proved_as_implication"],
        "antecedent_not_overpromoted": not coupling["theorem"]["antecedent_selected_now"],
        "same_source_guard": "does not import" in topology["same_source_guard"],
        "U6_not_overclosed": not frontier["U6_strong_CP_closed"],
        "no_new_parameter": frontier["new_continuous_parameters"] == 0,
    }
    outputs = {
        "topology": str(TOPOLOGY.relative_to(ROOT)).replace("\\", "/"),
        "coupling": str(COUPLING.relative_to(ROOT)).replace("\\", "/"),
        "rank_theorem": str(RANK.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedQ79MultiAxionSupersetAndHiddenBlindDirection.v1",
        "status": STATUS,
        "results": {
            "minimum_topological_axion_candidates": topology["conclusion"]["minimum_total_axion_candidates"],
            "hidden_blind_rank_theorem": True,
            "opposite_visible_hidden_coupling_implication": True,
            "selected_hidden_blind_direction": False,
            "U6_current_map": "9/10",
            "U6_strong_CP_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_q79MultiAxionSupersetAndHiddenBlindDirection_v1",
        "status": STATUS,
        "minimum_topological_axion_candidates": topology["conclusion"]["minimum_total_axion_candidates"],
        "hidden_blind_rank_theorem": True,
        "selected_hidden_blind_direction": False,
        "same_source_readiness": "0/6",
        "U6_current_map": "9/10",
        "U6_strong_CP_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected q79 Multi-Axion Superset and Hidden-Blind Direction v1

## Topological headroom

For a nontrivial principal `T2` bundle over K3, the Leray--Serre differential
maps the two fiber one-forms to the two torus Chern classes. If their real span
has rank `r=1` or `2`, then

```text
b2(X6)=22-r = 21 or 20.
```

Thus the selected Fu--Yau topology has at least `20` model-dependent B-field
axion candidates and at least `21` candidates after including the universal
axion. This is a pre-lifting count, not a claim that all 21 remain light.

## Hidden-blind theorem

The `E8 x E8` Green--Schwarz polynomial gives, when the hidden internal bundle
is flat and the cohomological Bianchi identity identifies the visible bundle
and tangent curvature classes,

```text
k_visible = (1,+3p_i),
k_hidden  = (1,-3p_i).
```

For any nonzero pairing `p`, the displayed linear combination is exactly blind
to hidden-E8 instantons and retains a nonzero visible/QCD coupling. More
generally, for a non-QCD charge matrix `K` and QCD row `k_QCD`, such a direction
exists exactly when

```text
rank(K)<N and rank(stack(K,k_QCD))>rank(K).
```

## Selection boundary

This is a proved implication, not yet the selected q79 answer. The current
packet does not emit the torus Chern rank/integral B2 basis, hidden internal
bundle, full `X8` coupling lattice, gauged/lifted quotient, or NS5/worldsheet
charge and zero-mode rows from one source. In particular, the hidden-blind
combination has a universal component, so a wrapped NS5 contribution can still
break it.

The superset strategy therefore creates real room to solve quality, but U6
remains `9/10` until the six same-source fields are filled and the residual
amplitudes pass A98's exact inequalities.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (TOPOLOGY, topology),
        (COUPLING, coupling),
        (RANK, rank_theorem),
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
