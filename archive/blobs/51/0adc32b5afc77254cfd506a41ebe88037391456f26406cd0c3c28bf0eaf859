"""Consolidated audit for the current selected-flavor frontier."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(name: str) -> str:
    path = ROOT / name
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    terminal = read("Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md")
    phase = read("Minimal_Selected_Kernel_Packet_and_Phase_Rigidity_v1.md")
    loc = read("Minimal_Selected_Localization_Packet_v1.md")
    bridge = read("Bridge_Reduced_Yukawa_Packet_v1.md")
    kinetic = read("Selected_Kinetic_Family_Breaking_Gate_v1.md")
    anchored = read("Anchored_Kinetic_Metric_Source_Candidate_v1.md")
    anchor_order = read("ProtoSpinor_Anchor_Ordering_Lemma_for_Family_Metric_v1.md")
    universal = read("Universal_Anchored_Metric_CKM_Escape_Theorem_v1.md")
    seed = read("Canonical_Anchored_Bridge_Seed_Diagnostic_v1.md")
    scalar_stiffness = read("Scalar_Quark_Stiffness_Diagnostic_NoGo_v1.md")
    quark_breakdown = read("Quark_Second_Order_Breakdown_Hypothesis_v1.md")
    quark_operator = read("Quark_Second_Order_Breakdown_Operator_Candidate_v1.md")
    color_source = read("Color_Singlet_Redundancy_Source_for_Bq_v1.md")
    reduced_gap = read("Bq_Reduced_Color_Gap_Branch_Diagnostic_v1.md")
    orientation_lock = read("Bq_Retarded_Predecessor_Orientation_Lock_v1.md")
    gap_selection = read("Bq_No_Double_Counting_Gap_Selection_Lemma_v1.md")
    stiffness_target = read("Bq_UpDown_Stiffness_Hessian_Extraction_Target_v1.md")
    stiffness_source = read("Bq_Hypercharge_Square_Stiffness_Source_v1.md")
    selected_bq = read("Selected_Finite_Bq_Branch_Theorem_v1.md")
    mass_diag = read("Selected_Finite_Bq_Mass_Hierarchy_Diagnostic_v1.md")
    mass_req = read("Selected_Mass_Layer_Requirements_after_Bq_v1.md")
    right_mass = read("Right_Eigenchannel_Mass_Layer_Theorem_Target_v1.md")
    mass_source_candidates = read("Weighted_Right_Eigenchannel_Action_Source_Candidates_v1.md")
    mass_source_battery = read("Mass_Action_Source_Theory_Battery_v1.md")
    finite_label_mass = read("Finite_Label_Right_Channel_Mass_Operator_Candidate_v1.md")
    finite_label_source = read("Finite_Label_Right_Channel_Source_Operator_Schema_v1.md")
    projector_reduction = read("Right_Channel_Projector_Selection_Reduction_v1.md")
    up_label = read("Up_Retarded_Spinorial_Right_Channel_Label_Theorem_v1.md")
    down_label = read("Down_Dyadic_Nil_Right_Channel_Label_Theorem_v1.md")
    assignment_target = read("Finite_Right_Channel_Assignment_Extraction_Target_v1.md")
    observable_scan = read("Right_Channel_Label_Observable_Dictionary_Scan_v1.md")
    commutant_projection = read("Schur_Riesz_Commutant_Projection_for_Right_Channel_Labels_v1.md")
    external_import = read("External_Source_Packet_Import_for_Right_Channel_Label_Assignment_v1.md")
    row_contract = read("Right_Channel_Label_Row_Emission_Contract_v1.md")
    cross_repo_adapter = read("Cross_Repo_Primitive_Row_Adapter_for_Right_Channel_Labels_v1.md")
    adapter_contract = read("Primitive_C1_to_Right_Label_Adapter_Payload_Contract_v1.md")
    promotion_attempt = read("Primitive_C1_Right_Label_Source_Promotion_Theorem_Attempt_v1.md")
    source_payload_schema = read("Selected_Primitive_Kernel_Source_Payload_Schema_v1.md")
    source_payload_workorder = read("Selected_Primitive_Kernel_Source_Theorem_Workorder_v1.md")
    static_selector_import = read("Static_Source_Selector_Import_for_Primitive_Kernel_Payload_v1.md")
    formal_routeb_import = read("Formal_RouteB_Right_Label_Value_Import_v1.md")
    local_premise_promotion = read("Selected_FiniteTraceQuadrature_Equals_PhysicalPhiFinC1Action_LocalPremise_Theorem_v1.md")
    unpatched_reduction = read("Unpatched_WeylVariation_Principle_Current_NoGo_and_Minimal_Bridge_v1.md")
    routec_cutset = read("RouteC_Source_Selector_and_Basis_Cutset_Import_v1.md")
    routec_operator_frontier = read("RouteC_Operator_Source_Frontier_Import_v1.md")
    routec_hym_frontier = read("RouteC_HYM_OperatorValues_Frontier_Import_v1.md")
    routec_dynamic_frontier = read("RouteC_HYM_to_DynamicC1_SourceRule_Frontier_Import_v1.md")
    dynamic_wallbreak = read("DynamicC1_WallBreak_Status_Import_v1.md")
    finitec1_source_fork = read("FiniteC1_SourceIdentity_TheoremProof_or_ExplicitSourcePrinciplePatch_v1.md")
    psm_c1_source_frontier = read("PSM_C1_02_SourceIdentity_Unpatched_Frontier_Import_v1.md")
    primitive_kernel_frontier = read("PrimitiveKernelSourceTheorem_RouteB_Frontier_Import_v1.md")
    psm_a1a_cutset = read("PSM_C1_02_UnpatchedA1a_Cutset_or_RouteB_RowSource_Import_v1.md")
    enriched_weylpair_static = read("EnrichedWeylPair_StaticProvenance_DynamicC1_Open_Import_v1.md")
    dynamicc1_breakthrough = read("DynamicC1_Breakthrough_Attempt_Axiom_or_Galerkin_Decision_v1.md")
    dynamicc1_duallane = read("DynamicC1_DualLane_DerivationAndGalerkin_Progress_Import_v1.md")
    cert = read("Selected_Overlap_Kernel_Certificate_v1.md")

    gates = [
        Gate(
            "q79 CP branch",
            "CLOSED" if "selected exact/charge MTT branch proves q=79 mod 448" in terminal else "FAIL",
            "finite CP label selected",
        ),
        Gate(
            "phase rigidity",
            "PROVED" if "Phase Rigidity" in phase and "Magnitude Under-Determination" in phase else "FAIL",
            "future CP phases lie in q79 Z448 character algebra",
        ),
        Gate(
            "rank-three family skeleton",
            "CONSTRUCTED" if "rank-three retained family cluster                  PROVED" in loc else "FAIL",
            "q79 CP sector tensored with family Z3",
        ),
        Gate(
            "Gamma_u/Gamma_d skeleton",
            "CONSTRUCTED" if "finite Gamma_u/Gamma_d channel skeleton             CONSTRUCTED" in loc else "FAIL",
            "one Z3 bridge per family pair",
        ),
        Gate(
            "bridge entry reduction",
            "PROVED" if "9 entries per quark sector -> 3 bridge weights" in bridge else "FAIL",
            "no entry-wise raw quark matrices in the packet",
        ),
        Gate(
            "pure bridge no-go",
            "PROVED" if "pure bridge Hermitian forms commute" in bridge else "FAIL",
            "CKM angles require extra selected family breaking",
        ),
        Gate(
            "kinetic breaking sufficiency",
            "PROVED-SCHEMA" if "Kinetic Breaking Can Generate Nontrivial Left Mixing" in kinetic else "FAIL",
            "non-circulant selected metrics can break common family basis",
        ),
        Gate(
            "anchored metric candidate",
            "FORMULATED" if "lambda_nil/lambda_lens" in anchored and "positive non-circulant metric" in anchored else "FAIL",
            "lens/nil gap hierarchy gives a candidate family anisotropy",
        ),
        Gate(
            "anchor role ordering",
            "PROVED-SCHEMA" if "transport < lens < nil" in anchor_order else "FAIL",
            "family cost order fixed by proto-spinor roles up to relabeling",
        ),
        Gate(
            "universal metric escape",
            "PROVED/CHECKED" if "independent up/down metric scales not structurally needed" in universal else "FAIL",
            "one anchored metric can break the pure bridge common basis",
        ),
        Gate(
            "canonical seed diagnostic",
            "NOT-QUARK-CLOSED" if "seed is not CKM-quark closed" in seed or "Universal Seed Is Not Quark-Closed" in seed else "FAIL",
            "lean q79/J seed gives large, not CKM-like, mixing",
        ),
        Gate(
            "scalar stiffness rescue",
            "TESTED-NO-GO" if "Scalar Quark-Stiffness Diagnostic No-Go" in scalar_stiffness else "FAIL",
            "one/two scalar stiffness multipliers remain too mixed",
        ),
        Gate(
            "quark second breakdown",
            "FORMULATED" if "Quark Second-Order Breakdown" in quark_breakdown and "B_q" in quark_breakdown else "FAIL",
            "quarks require an extra composite/redundancy layer beyond leptons",
        ),
        Gate(
            "B_q operator candidate",
            "CONSTRUCTED" if "explicit B_q candidate" in quark_operator else "FAIL",
            "retarded next-role redundancy cost gives CKM-shaped diagnostic",
        ),
        Gate(
            "B_q color source",
            "PROVED-SCHEMA" if "Color-Singlet Completion Lemma" in color_source and "delta^2/2" in color_source else "FAIL",
            "two hidden color-redundancy channels give the 1/2 Schur coefficient",
        ),
        Gate(
            "B_q finite branch",
            "DIAGNOSTIC" if "remaining finite branch-selection problem" in reduced_gap else "FAIL",
            "reduced color-gap branch improves diagnostics but constants/orientation remain open",
        ),
        Gate(
            "B_q orientation lock",
            "PROVED-CONDITIONAL" if "sigma = -1" in orientation_lock and "Orientation-Lock Theorem" in orientation_lock else "FAIL",
            "same retarded predecessor convention selects the B_q adjacent role",
        ),
        Gate(
            "B_q gap selection",
            "PROVED-CONDITIONAL" if "Lambda_q = lambda_lens - lambda_nil" in gap_selection and "double counts" in gap_selection else "FAIL",
            "internal Schur color completion selects the primitive lens-nil gap",
        ),
        Gate(
            "B_q stiffness target",
            "DEFINED" if "Hessian Extraction Definition" in stiffness_target and "H_x^cl" in stiffness_target else "FAIL",
            "mu_u and mu_d reduced to sector Hessian curvature ratios",
        ),
        Gate(
            "B_q stiffness source",
            "PROVED-CONDITIONAL" if "mu_u = 2 * 2^2 = 8" in stiffness_source and "mu_d = 2 * 1^2 = 2" in stiffness_source else "FAIL",
            "topology-only hypercharge-square Hessian selects mu_u=8, mu_d=2",
        ),
        Gate(
            "selected finite B_q branch",
            "SELECTED-CONDITIONAL" if "sigma=-1" in selected_bq and "mu_u=8" in selected_bq and "mu_d=2" in selected_bq else "FAIL",
            "finite quark CKM branch assembled without CKM/mass inputs",
        ),
        Gate(
            "full Hessian verification",
            "OPEN" if "extract full H_u^cl,H_d^cl,H_anchor" in selected_bq else "FAIL",
            "verify selected Sigma_MTT Hessian realizes the conditional sources",
        ),
        Gate(
            "mass hierarchy diagnostic",
            "NOT-CLOSED" if "does not close masses" in mass_diag else "FAIL",
            "selected B_q branch is CKM-shaped but too shallow for quark masses",
        ),
        Gate(
            "mass layer requirements",
            "DEFINED" if "A_u ~= 4.55" in mass_req and "simple family-basis prefactor rejected" in mass_req else "FAIL",
            "extra light-mode actions quantified; blunt prefactor rejected",
        ),
        Gate(
            "right-channel mass target",
            "PROVED-TARGET" if "Y G_A^{-1/2}" in right_mass and "preserves:" in right_mass else "FAIL",
            "weighted right-eigenchannel actions can change masses without changing left CKM",
        ),
        Gate(
            "mass action source candidates",
            "EXTRACTED" if "localized zero-mode overlap actions" in mass_source_candidates and "q_x^2 log(pi)" in mass_source_candidates else "FAIL",
            "allowed no-proxy source classes listed; log(pi) primitive tested but not closed",
        ),
        Gate(
            "mass source theory battery",
            "CHECKED" if "finite right-channel operator route selected" in mass_source_battery else "FAIL",
            "multiple source theories tested; finite right-channel operator is the next target",
        ),
        Gate(
            "finite-label mass candidate",
            "CANDIDATE" if "eig(R_u) = (-3/2 J, +1/2 J, 0)" in finite_label_mass else "FAIL",
            "compact residual labels found; source derivation still open",
        ),
        Gate(
            "finite-label source schema",
            "PROVED-SCHEMA" if "R_u = J(-1/2 I_u^light + Xi_u)" in finite_label_source and "R_d = (1/64) P_dyad" in finite_label_source else "FAIL",
            "projector operator form commutes with right Gram; projector selection remains open",
        ),
        Gate(
            "right projector reduction",
            "PROVED" if "projectors are not" in projector_reduction and "free parameters" in projector_reduction else "FAIL",
            "simple right spectrum makes projectors unique once labels are selected",
        ),
        Gate(
            "up finite label theorem",
            "PROVED-CONDITIONAL" if "spec_light(R_u) = (-3/2 J, +1/2 J)" in up_label else "FAIL",
            "spinorial parity plus retarded half-step gives up labels",
        ),
        Gate(
            "down finite label theorem",
            "PROVED-CONDITIONAL" if "spec_light(R_d) = (1/64, 3/2 lambda_nil)" in down_label else "FAIL",
            "dyadic projector plus nil half-channel gives down labels",
        ),
        Gate(
            "right-label assignment target",
            "DEFINED" if "Tr(P_{u,1} S_u^spin) = -1" in assignment_target and "Tr(P_{d,1} S_d^dyad) = 1" in assignment_target else "FAIL",
            "remaining source extraction reduced to trace/projector tests",
        ),
        Gate(
            "raw label observable scan",
            "TESTED-NO-GO" if "raw family-basis assignment source             TESTED-NO-GO" in observable_scan else "FAIL",
            "simple family-basis labels do not supply the assignment source",
        ),
        Gate(
            "right-label commutant projection",
            "PROVED-SCHEMA" if "E_K(A)=sum_a P_a A P_a" in commutant_projection else "FAIL",
            "Schur/Riesz projection turns raw labels into commuting observables",
        ),
        Gate(
            "external source-packet import",
            "CHECKED" if "selected basis support imported" in external_import and "primitive row/source emission still missing" in external_import else "FAIL",
            "sibling repos provide proof standard and selected-basis support, not flavor rows",
        ),
        Gate(
            "right-label row contract",
            "DEFINED" if "MTTFlavorRightChannelLabelRowEmission.v1" in row_contract else "FAIL",
            "exact payload needed to promote finite mass labels",
        ),
        Gate(
            "cross-repo row adapter",
            "DIAGNOSTIC" if "MTTPrimitiveC1ToRightLabelAdapter.v1" in cross_repo_adapter and "strong construction clue" in cross_repo_adapter else "FAIL",
            "SM-parity primitive rows match label shape after affine normalization but remain support-only",
        ),
        Gate(
            "primitive C1 adapter contract",
            "DEFINED" if "PrimitiveC1RightLabelSourcePromotionTheorem" in adapter_contract and "residual_replay_dependency=false" in adapter_contract else "FAIL",
            "exact promotion theorem and acceptance fields named",
        ),
        Gate(
            "primitive C1 source promotion",
            "PROVED-CONDITIONAL" if "CONDITIONAL_PROMOTION_PROVED" in promotion_attempt and "UNCONDITIONAL_PROMOTION_OPEN" in promotion_attempt else "FAIL",
            "right-label promotion follows once source-owner primitive rows are emitted",
        ),
        Gate(
            "static source selector import",
            "CHECKED" if "static source selector       closed" in static_selector_import and "d_shift = X/shift row routed to d" in static_selector_import else "FAIL",
            "Z/clock -> u,e and X/shift -> d,nuD imported; d row corrected to d_shift",
        ),
        Gate(
            "formal Route-B right labels",
            "FORMAL-SUPPORT" if "u:phase spectrum" in formal_routeb_import and "physical_source_promoted=false" in formal_routeb_import else "FAIL",
            "finite trace rows compute the right-label values; physical promotion remains open",
        ),
        Gate(
            "local-premise source closure",
            "CLOSED-CONDITIONAL" if "LOCAL-PREMISE PROVED" in local_premise_promotion and "UNPATCHED DERIVATION OPEN" in local_premise_promotion else "FAIL",
            "finite trace = physical Phi_fin^C1 action under accepted local Weyl-variation premise",
        ),
        Gate(
            "unpatched Weyl principle",
            "OPEN-SHARP" if "SUPPORT-ONLY PROOF REFUTED" in unpatched_reduction and "SelectedFiniteC1VariationalProjectionBridge" in unpatched_reduction else "FAIL",
            "closed finite support cannot prove source ownership; bridge or independent row-source execution needed",
        ),
        Gate(
            "Route-C source/basis cutset",
            "LOCKED-OPEN" if "36` total root/formal differences" in routec_cutset and "C1_source_selector_condition" in routec_cutset else "FAIL",
            "finite matrices match under formal lift; source provenance and quotient-valid basis remain open",
        ),
        Gate(
            "Route-C operator source frontier",
            "SOURCE-CLOSED/OPERATOR-OPEN" if "source-level gerbe/Weyl carrier is closed" in routec_operator_frontier and "Rank-2 non-split" in routec_operator_frontier else "FAIL",
            "Weyl carrier and alpha1 progress imported; selected operator identity reduced to rank2 L2 or Route-C residual fill",
        ),
        Gate(
            "Route-C HYM operator-values frontier",
            "HYM-BRIDGE-CLOSED/VALUES-OPEN" if "rank-2 L2/cohomology input closes" in routec_hym_frontier and "selected HYM connection/operator values" in routec_hym_frontier else "FAIL",
            "rank2 L2 and reduced stability bridge imported; concrete HYM-derived operator matrices remain open",
        ),
        Gate(
            "Route-C dynamic C1 source-rule frontier",
            "VALUES-READY/SOURCE-RULE-OPEN" if "dynamic C1 value gate emits exact phase/shift candidate tables" in routec_dynamic_frontier and "prove differentiated PhiFin-C1 source rule" in routec_dynamic_frontier else "FAIL",
            "HYM/End0/Green/dotD support imported; final dynamic gate is source rule or honest Galerkin C1 export",
        ),
        Gate(
            "Dynamic C1 wall break status",
            "PATCHED-BROKEN/UNPATCHED-OPEN" if "patched dynamic C1 wall is broken" in dynamic_wallbreak and "not correct to say that full no-knob SM closure is proved" in dynamic_wallbreak else "FAIL",
            "source-identity patch closes declared SM-parity replay; unpatched/no-knob source theorem remains open",
        ),
        Gate(
            "Finite C1 source-identity fork",
            "PATCH-READY/THEOREM-OPEN" if "SelectedFiniteC1SourceIdentityTheorem" in finitec1_source_fork and "This construction does not choose Route B as a proof" in finitec1_source_fork else "FAIL",
            "explicit source-principle patch formulated; unpatched physical-action or independent-row proof remains open",
        ),
        Gate(
            "PSM-C1-02 source frontier",
            "LOCAL-CLOSED/A1A-PROBED-OPEN" if "local/premise-conditioned source-identity spine is coherent" in psm_c1_source_frontier and "restriction row is emitted" in psm_c1_source_frontier else "FAIL",
            "local packet validates and measure sublemma is derived; A1a support is real but rejected until a physical action restriction row is emitted",
        ),
        Gate(
            "Route-B primitive kernel frontier",
            "REDUCED-TO-SOURCE-THEOREM" if "Route B is no longer a vague" in primitive_kernel_frontier and "SelectedPrimitiveKernelSourceTheorem" in primitive_kernel_frontier else "FAIL",
            "independent route reduced to five concrete primitive-kernel source fields and no residual replay as source",
        ),
        Gate(
            "PSM A1a / Route-B cutset",
            "ROUTEB-ONE-FIELD-OPEN" if "rejects Route B on exactly one field" in psm_a1a_cutset and "SelectedRowSourceIndependenceFromResidualProjectorReplayTheorem" in psm_a1a_cutset else "FAIL",
            "PSM strict validator reduces Route B to row-source independence from residual-projector replay",
        ),
        Gate(
            "enriched Weyl-pair static provenance",
            "STATIC-CLOSED/DYNAMIC-OPEN" if "static enriched Weyl-pair provenance is closed" in enriched_weylpair_static and "dynamic C1 transfer values are still open" in enriched_weylpair_static else "FAIL",
            "Z->u,e and X->d,nuD static source routing is closed; dynamic A,b,deltaTheta emission remains open",
        ),
        Gate(
            "Dynamic C1 breakthrough decision",
            "AXIOM-READY/UNPATCHED-OPEN" if "closest available breakthrough" in dynamicc1_breakthrough and "DifferentiatedPhiFinC1ResidualProjectorAxiom" in dynamicc1_breakthrough else "FAIL",
            "local/principle axiom would emit dynamic values; strict route needs derivation or honest Galerkin execution",
        ),
        Gate(
            "Dynamic C1 dual-lane progress",
            "PATCHED-CLOSED/STRICT-OPEN" if "local/patched proof spine closes" in dynamicc1_duallane and "not yet an honest independent Galerkin computation" in dynamicc1_duallane else "FAIL",
            "axiom patch closes local spine; Galerkin replay passes but independent selected contractions remain open",
        ),
        Gate(
            "primitive source payload",
            "DEFINED/OPEN" if "MTTSelectedPrimitiveKernelSourcePayload.v1" in source_payload_schema and "strict source validation  PASS" in source_payload_workorder else "FAIL",
            "strict source-owner packet/template created; current attempt expected-rejects",
        ),
        Gate(
            "full no-proxy masses",
            "OPEN" if "full no-proxy SM flavor closure                 OPEN" in cert else "FAIL",
            "needs action costs, prefactors, metrics, neutral sector, RG",
        ),
    ]

    print("Selected flavor frontier chain audit")
    print("====================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
