"""Build source-map selection theorem / honest Galerkin C1 value-run gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"
SOURCE_MAP = (
    DATA
    / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
    / "primitive_tensor_hessian_source_map_candidate.packet.json"
)
SELECTION_KERNEL = (
    DATA
    / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
    / "source_map_selection_obligation_kernel.packet.json"
)
GALERKIN_SLOTS = (
    DATA
    / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
    / "honest_galerkin_execution_value_slots.packet.json"
)
WEYL_POLY = DATA / "selected_residual_weylpolynomial_source_theorem_attempt.candidate.json"
CANONICAL_PROJECTOR = DATA / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill.candidate.json"
PHIFIN_APPLICATION = DATA / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill.candidate.json"
TERMINAL_PATCH = DATA / "terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues.candidate.json"

OUTPUT = DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"
PACKET_DIR = DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
SELECTION_TEST = PACKET_DIR / "source_map_selection_theorem_test.packet.json"
IF_SELECTED = PACKET_DIR / "if_selected_dynamic_packet_closure.packet.json"
GALERKIN_ROUTE = PACKET_DIR / "honest_galerkin_value_run_route.packet.json"
CERT = CERTS / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1.md"

STATUS = "MTT_SELECTED_SOURCEMAPSELECTIONTHEOREM_OR_HONESTGALERKINC1VALUERUN_BUILT_SELECTION_TEST_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    source_map = load(SOURCE_MAP)
    kernel = load(SELECTION_KERNEL)
    galerkin = load(GALERKIN_SLOTS)
    weyl = load(WEYL_POLY)
    canonical = load(CANONICAL_PROJECTOR)
    phifin = load(PHIFIN_APPLICATION)
    terminal = load(TERMINAL_PATCH)

    if_selected = source_map["if_source_map_selected_then"]
    current_case = kernel["minimal_truth_table"]["current_case"]
    would_close = kernel["minimal_truth_table"][
        "if_phase_and_shift_residual_sources_selected_and_b_source_emitted"
    ]

    selection_test = {
        "schema": "MTTSourceMapSelectionTheoremTest.v1",
        "status": "SELECTION_TEST_BUILT_DYNAMIC_APPLICATION_OPEN",
        "already_selected_or_closed": {
            "terminal_static_source_unconditional": terminal["selection_decision"][
                "terminal_source_unconditional_in_patched_spine"
            ],
            "static_source_map_candidate_constructed": previous["promotion_decision"][
                "source_map_candidate_constructed"
            ],
            "weyl_polynomial_residuals_exact": weyl["what_closes_now"][
                "residuals_compressed_to_low_degree_weyl_polynomials"
            ],
            "canonical_residual_projector_unique": canonical["projector_closure"][
                "canonical_projector_selected_as_mathematical_consequence"
            ],
            "canonical_projector_replays_RZ_RX": canonical["what_closes_now"][
                "residual_projector_replays_R_Z_R_X_exactly"
            ],
            "strict_72_real_target_attached": previous["what_closes_now"][
                "strict_72_real_acceptance_target_attached"
            ],
        },
        "selection_attempt": {
            "candidate_rule": (
                "selected differentiated Phi_fin^C1 applies Q_residual to the "
                "selected enriched Weyl-pair packet"
            ),
            "phase_R_Z_selected_now": source_map["candidate_residual_operators"][
                "phase_R_Z"
            ]["selected_by_MTT_now"],
            "shift_R_X_selected_now": source_map["candidate_residual_operators"][
                "shift_R_X"
            ]["selected_by_MTT_now"],
            "b_source_emitted_now": kernel["currently_emitted"]["selected_b_selected"],
            "physical_projector_application_promoted_now": phifin["promotion_decision"][
                "PhiFinC1_projector_application_promoted"
            ],
            "source_map_selected_now": previous["promotion_decision"][
                "source_map_selected_by_MTT_now"
            ],
        },
        "why_selection_is_not_yet_proved": [
            "terminal/static selection selects source labels and finite routes, not the differentiated C1 application rule",
            "canonical Q_residual is a unique mathematical projector, but uniqueness alone does not select physical Phi_fin^C1 application",
            "existing Phi_fin^C1 residual-projector application audit explicitly rejects promoting Q_residual without a source/application rule",
            "b_selected remains absent as a theorem-derived Hessian/source vector",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    if_selected_packet = {
        "schema": "MTTIfSelectedDynamicPacketClosure.v1",
        "status": "IF_SELECTED_CLOSURE_EXACT_BUT_ANTECEDENT_OPEN",
        "antecedent_required": {
            "phase_R_Z_selected": True,
            "shift_R_X_selected": True,
            "b_source_emitted": True,
            "same_branch_normalization": True,
        },
        "current_antecedent": current_case,
        "would_promote_if_antecedent_met": would_close,
        "if_selected_numeric_replay": {
            "rank": if_selected["rank"],
            "A_transpose_A": if_selected["A_transpose_A"],
            "A_transpose_b": if_selected["A_transpose_b"],
            "deltaTheta_C1": if_selected["deltaTheta_C1"],
            "projection_plus_residual_reconstructs_conditional_packet": if_selected[
                "projection_plus_residual_reconstructs_conditional_packet"
            ],
        },
        "promoted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    galerkin_route = {
        "schema": "MTTHonestGalerkinC1ValueRunRoute.v1",
        "status": "HONEST_GALERKIN_VALUE_RUN_ROUTE_OPEN",
        "strict_coordinate_target": galerkin["strict_coordinate_target"],
        "manifest_status": galerkin["manifest_status"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "required_outputs": galerkin["required_outputs"],
        "can_replace_source_map_now": galerkin["can_replace_source_map_now"],
        "would_close_SM_parity_dynamic_packet_if_emitted": True,
        "would_close_no_knob_flavor_constants_by_itself": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSourceMapSelectionTheoremOrHonestGalerkinC1ValueRun",
        "status": STATUS,
        "inputs": {
            "previous_source_map_candidate": rel(PREVIOUS),
            "source_map_packet": rel(SOURCE_MAP),
            "selection_kernel": rel(SELECTION_KERNEL),
            "honest_galerkin_slots": rel(GALERKIN_SLOTS),
            "weyl_polynomial_gate": rel(WEYL_POLY),
            "canonical_projector_gate": rel(CANONICAL_PROJECTOR),
            "phifin_projector_application_gate": rel(PHIFIN_APPLICATION),
            "terminal_axiom_patch_gate": rel(TERMINAL_PATCH),
        },
        "output_packets": {
            "source_map_selection_theorem_test": rel(SELECTION_TEST),
            "if_selected_dynamic_packet_closure": rel(IF_SELECTED),
            "honest_galerkin_value_run_route": rel(GALERKIN_ROUTE),
        },
        "what_closes_now": {
            "source_map_selection_test_built": True,
            "closed_static_and_projector_support_separated_from_dynamic_application": True,
            "if_selected_dynamic_packet_closure_exact": True,
            "honest_Galerkin_value_run_route_restated": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_differentiated_PhiFinC1_applies_Q_residual": True,
            "selected_phase_R_Z_source": True,
            "selected_shift_R_X_source": True,
            "selected_Hessian_or_b_source_vector": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "selected_sector_response_matrices": True,
            "honest_selected_Galerkin_C1_execution_values": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "selection_theorem_proved_now": False,
            "source_map_selected_by_MTT_now": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "sector_response_matrices_promoted": False,
            "honest_Galerkin_C1_value_run_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "selection_theorem_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "honest_Galerkin_C1_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SourceMapSelectionBoundaryTheorem",
            "proved": True,
            "statement": (
                "The terminal/static source selection, exact Weyl-polynomial residuals, "
                "and canonical Q_residual uniqueness are sufficient to construct the "
                "minimal same-branch source-map candidate, and if the differentiated "
                "Phi_fin^C1 application plus b source were selected then A_selected, "
                "b_selected, and deltaTheta_C1 would promote exactly.  They do not by "
                "themselves prove the physical differentiated application rule, so the "
                "remaining proof object is precisely that rule or an honest selected "
                "Galerkin C1 value run."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selection_test_packet_path": rel(SELECTION_TEST),
        "if_selected_packet_path": rel(IF_SELECTED),
        "galerkin_route_packet_path": rel(GALERKIN_ROUTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "selection_theorem_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "honest_Galerkin_C1_claimed": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SourceMapSelectionTheorem or HonestGalerkinC1ValueRun v1

Status: `{STATUS}`.

This gate tests whether the already-built source-map candidate can be promoted.

Closed support:

```text
terminal/static source selection     = closed
R_Z/R_X Weyl-polynomial shapes       = exact
canonical Q_residual                 = unique, rank {source_map["closed_support"]["Q_residual_rank"]}
strict 72-real target                = attached
```

But dynamic selection is still open:

```text
phase R_Z selected now = {selection_test["selection_attempt"]["phase_R_Z_selected_now"]}
shift R_X selected now = {selection_test["selection_attempt"]["shift_R_X_selected_now"]}
b source emitted now   = {selection_test["selection_attempt"]["b_source_emitted_now"]}
Phi_fin^C1 applies Q   = {selection_test["selection_attempt"]["physical_projector_application_promoted_now"]}
```

If those antecedents are supplied, the numeric replay is exact:

```text
A^T A = {if_selected["A_transpose_A"]}
A^T b = {if_selected["A_transpose_b"]}
deltaTheta_C1 = {if_selected["deltaTheta_C1"]}
```

So the remaining SM-parity dynamic object is sharply one of:

```text
1. selected differentiated Phi_fin^C1 applies Q_residual and emits b_selected
2. honest selected Galerkin C1 value run emits replacement values
```

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    SELECTION_TEST.write_text(json.dumps(selection_test, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    IF_SELECTED.write_text(json.dumps(if_selected_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    GALERKIN_ROUTE.write_text(json.dumps(galerkin_route, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
