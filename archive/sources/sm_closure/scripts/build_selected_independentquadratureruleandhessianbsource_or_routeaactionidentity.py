"""Attempt to derive independent quadrature rule/Hessian b-source or Route-A action identity."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_independentquadratureruleandhessianbsource_or_routeaactionidentity"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DERIVATION = PACKET_DIR / "derivation_attempt.packet.json"
PARTIAL_IDS = PACKET_DIR / "partial_measure_quadrature_source_id_attempt.packet.json"
PARTIAL_VALIDATION = PACKET_DIR / "partial_measure_quadrature_source_id_validator_result.packet.json"
CONDITIONAL_WITNESS = PACKET_DIR / "conditional_source_identity_theorem_witness.packet.json"
CONDITIONAL_VALIDATION = PACKET_DIR / "conditional_source_identity_validator_result.packet.json"
OBSTRUCTION = PACKET_DIR / "remaining_derivation_obstruction.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_IndependentQuadratureRuleAndHessianBSource_or_RouteAActionIdentity_v1.md"

PREVIOUS = DATA / "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof.candidate.json"
CURRENT_IDS = (
    DATA
    / "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof"
    / "current_rowkernel_source_id_attempt.packet.json"
)
CONDITIONAL_IDS = (
    DATA
    / "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof"
    / "conditional_independent_rowkernel_source_id_witness.packet.json"
)
TRACE_SUPPORT = (
    DATA
    / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
    / "selected_trace_map_and_measure_support.packet.json"
)
SOURCE_LEMMA = (
    DATA
    / "selected_sourcetheorem_push_attempt_or_minimalnewlemma"
    / "minimal_selected_finitec1_source_promotion_lemma.packet.json"
)
SOURCE_IDENTITY_CUTSET = (
    DATA
    / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun"
    / "shared_source_theorem_cutset.packet.json"
)
WEYL_PRINCIPLE = (
    DATA
    / "selected_routec_weylvariation_sourceprinciple_or_kernelclosure"
    / "routec_weyl_variation_principle_candidate.packet.json"
)
CLAUSE_PROOF = (
    DATA
    / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission"
    / "finite_weyl_trace_assembly_clause_proof.packet.json"
)
SOURCE_ID_VALIDATOR = ROOT / "scripts" / "validate_selected_independentc1_rowkernel_source_ids.py"

STATUS = "MTT_SELECTED_INDEPENDENT_QUADRATURE_RULE_AND_HESSIAN_BSOURCE_DERIVATION_ATTEMPT_REDUCED_TO_SOURCE_IDENTITY"
NEXT = "MTT_Selected_FiniteC1SourceIdentityTheoremProof_or_ExplicitSourcePrinciplePatch_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SOURCE_ID_VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "validator": rel(SOURCE_ID_VALIDATOR),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    current_ids = load(CURRENT_IDS)
    conditional_ids = load(CONDITIONAL_IDS)
    trace_support = load(TRACE_SUPPORT)
    source_lemma = load(SOURCE_LEMMA)
    source_identity = load(SOURCE_IDENTITY_CUTSET)
    weyl = load(WEYL_PRINCIPLE)
    clause = load(CLAUSE_PROOF)

    derivation = {
        "schema": "MTTIndependentQuadratureRuleAndHessianBSourceDerivationAttempt.v1",
        "status": "DERIVATION_ATTEMPTED_CURRENT_SUPPORT_INSUFFICIENT",
        "route_B_target": [
            "selected independent quadrature rule source",
            "selected measure pairing as source, not postcheck",
            "Hessian/b_selected source rows independent of A^T b target",
            "primitive and sector source ids theorem-derived",
        ],
        "route_A_parallel_target": [
            "physical Phi_fin^C1 action restriction",
            "no extra physical boundary/source term",
            "same-source R_Z/R_X/b_selected",
        ],
        "support_imported": {
            "finite_trace_measure_normalization": clause["proved_subclaim"]["trace_assembly_closed"],
            "formal_36_sector_rows_assembled": clause["proved_subclaim"]["sector_rows_assembled_formally"],
            "formal_2_hessian_rows_assembled": clause["proved_subclaim"]["hessian_source_rows_assembled_formally"],
            "trace_map_support": trace_support["support_imported"],
            "minimal_source_lemma_sufficient_if_proved": source_lemma["sufficient_for_strict_validator"],
            "weyl_principle_candidate_support": weyl["support_imported"],
        },
        "derivation_result": {
            "selected_measure_pairing_as_source": False,
            "selected_independent_quadrature_rule_as_source": False,
            "selected_variation_space_as_source": False,
            "selected_hessian_b_source": False,
            "primitive_and_sector_ids_promoted": False,
            "reason": (
                "Closed support proves the finite trace/Frobenius normal form and formal row assembly, "
                "but does not prove that the selected physical/source rule owns the quadrature rule, "
                "primitive kernels, sector assembly, and Hessian b_selected rows independently of residual replay."
            ),
        },
        "source_identity_theorem_needed": {
            "theorem_name": source_identity["theorem_name"],
            "statement": source_identity["statement"],
            "required_clauses": source_identity["required_clauses"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DERIVATION, derivation)

    partial_ids = json.loads(json.dumps(current_ids))
    partial_ids["schema"] = "MTTPartialMeasureQuadratureSourceIdAttempt.v1"
    partial_ids["status"] = "MEASURE_QUADRATURE_FORMAL_SUPPORT_IMPORTED_HESSIAN_AND_SOURCE_OWNERSHIP_OPEN"
    partial_ids["global_sources"]["selected_measure_pairing"].update(
        {
            "selected_emitted": False,
            "theorem_derived": False,
            "independent_of_residual_replay": False,
            "provenance": "finite_trace_formal_support_not_source_ownership",
            "support_source": rel(TRACE_SUPPORT),
        }
    )
    partial_ids["global_sources"]["selected_quadrature_rule"].update(
        {
            "selected_emitted": False,
            "theorem_derived": False,
            "independent_of_residual_replay": False,
            "provenance": "finite_trace_rule_support_not_independent_quadrature_source",
            "support_source": rel(CLAUSE_PROOF),
        }
    )
    partial_ids["global_sources"]["selected_variation_space"].update(
        {
            "selected_emitted": False,
            "theorem_derived": False,
            "independent_of_residual_replay": False,
            "provenance": "weyl_principle_candidate_not_derived",
            "support_source": rel(WEYL_PRINCIPLE),
        }
    )
    write_json(PARTIAL_IDS, partial_ids)
    partial_validation = run_validator(PARTIAL_IDS)
    write_json(PARTIAL_VALIDATION, partial_validation)

    conditional_witness = json.loads(json.dumps(conditional_ids))
    conditional_witness["schema"] = "MTTConditionalFiniteC1SourceIdentityTheoremWitness.v1"
    conditional_witness["status"] = "CONDITIONAL_WITNESS_VALIDATES_IF_SOURCE_IDENTITY_THEOREM_PROVED"
    conditional_witness["conditional_on"] = source_identity["theorem_name"]
    write_json(CONDITIONAL_WITNESS, conditional_witness)
    conditional_validation = run_validator(CONDITIONAL_WITNESS)
    write_json(CONDITIONAL_VALIDATION, conditional_validation)

    obstruction = {
        "schema": "MTTIndependentQuadratureHessianBSourceDerivationObstruction.v1",
        "status": "NOT_DERIVED_FROM_CLOSED_SUPPORT_ALONE",
        "partial_validator_ok": partial_validation["ok"],
        "conditional_validator_ok": conditional_validation["ok"],
        "minimal_missing_clause_family": {
            "name": "SelectedFiniteC1SourceIdentityTheorem",
            "must_promote": [
                "finite trace/Frobenius measure from support to selected source rule",
                "pre-residual R_Z/R_X variation operators as source, not residual decomposition",
                "same-source Hessian/b_selected rows",
                "sector rows assembled from primitive source rows",
                "independence from residual projector replay and locked targets",
            ],
        },
        "why_no_value_search_remains": (
            "The 110-row table, source-id namespace, exact R_Z/R_X polynomials, trace measure, "
            "and conditional validator witness are all present. The missing step is source ownership."
        ),
        "route_A_equivalent_exit": source_identity["why_this_is_shared"]["route_A"],
        "route_B_equivalent_exit": source_identity["why_this_is_shared"]["route_B"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(OBSTRUCTION, obstruction)

    candidate = {
        "candidate": "MTTSelectedIndependentQuadratureRuleAndHessianBSourceOrRouteAActionIdentity",
        "status": STATUS,
        "inputs": {
            "previous": rel(PREVIOUS),
            "current_source_ids": rel(CURRENT_IDS),
            "conditional_source_ids": rel(CONDITIONAL_IDS),
            "trace_support": rel(TRACE_SUPPORT),
            "minimal_source_lemma": rel(SOURCE_LEMMA),
            "shared_source_identity_cutset": rel(SOURCE_IDENTITY_CUTSET),
            "weyl_principle_candidate": rel(WEYL_PRINCIPLE),
            "trace_assembly_clause_proof": rel(CLAUSE_PROOF),
        },
        "output_packets": {
            "derivation_attempt": rel(DERIVATION),
            "partial_measure_quadrature_source_id_attempt": rel(PARTIAL_IDS),
            "partial_measure_quadrature_source_id_validator_result": rel(PARTIAL_VALIDATION),
            "conditional_source_identity_theorem_witness": rel(CONDITIONAL_WITNESS),
            "conditional_source_identity_validator_result": rel(CONDITIONAL_VALIDATION),
            "remaining_derivation_obstruction": rel(OBSTRUCTION),
        },
        "theorem": {
            "name": "IndependentQuadratureRuleAndHessianBSourceDerivationReduction",
            "proved": True,
            "statement": (
                "The current corpus proves finite trace/Frobenius support and formal row assembly, but does not derive "
                "selected independent quadrature/measure/Hessian b-source ownership. The conditional source-identity "
                "witness validates, so proving SelectedFiniteC1SourceIdentityTheorem is sufficient and now necessary "
                "for this branch unless an explicit source principle patch is accepted."
            ),
        },
        "what_closes_now": {
            "derivation_attempt_executed": True,
            "formal_measure_support_imported": True,
            "partial_source_id_packet_rejected_honestly": partial_validation["ok"] is False,
            "conditional_source_identity_witness_passes": conditional_validation["ok"],
            "remaining_source_ownership_obstruction_named": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourceIdentityTheorem": True,
            "selected_independent_quadrature_rule_source": True,
            "selected_hessian_b_source": True,
            "route_A_physical_action_identity": True,
            "explicit_source_principle_patch_if_chosen": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_IndependentQuadratureRuleAndHessianBSource_or_RouteAActionIdentity_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "partial_validator_ok": partial_validation["ok"],
        "conditional_validator_ok": conditional_validation["ok"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected IndependentQuadratureRuleAndHessianBSource or RouteAActionIdentity v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "I attempted the derivation using the strongest closed support: finite qutrit Weyl "
        "trace uniqueness, trace/Frobenius measure support, formal `36+2` row assembly, the "
        "minimal source-promotion lemma, and the Route-C Weyl variation principle candidate.\n\n"
        "Result: this does not yet derive the selected independent quadrature rule or "
        "Hessian/`b_selected` source. The partial source-id packet still fails because support "
        "is not the same thing as theorem-derived source ownership. The conditional witness "
        "passes if `SelectedFiniteC1SourceIdentityTheorem` is proved.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
