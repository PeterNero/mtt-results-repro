"""Build corpus paper-revision packet after one-primitive closure adoption."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_corpuspaperrevisionpacket_or_strictnoknobupgradeexecution"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
REVISION_PACKET = PACKET_DIR / "corpus_paper_revision_packet.packet.json"
LEGACY_AUDIT = PACKET_DIR / "legacy_claim_surface_audit.packet.json"
STRICT_ROUTE = PACKET_DIR / "strict_noknob_route01_execution_packet.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CorpusPaperRevisionPacket_or_StrictNoKnobUpgradeExecution_v1.md"

PREVIOUS = DATA / "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram.candidate.json"
PAPER_UPDATE = (
    DATA
    / "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram"
    / "paper_update_claims_and_wording.packet.json"
)
UPGRADE = (
    DATA
    / "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram"
    / "strict_noknob_upgrade_program.packet.json"
)
DECISION = (
    DATA
    / "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram"
    / "publication_ready_closure_standard_decision.packet.json"
)
GUARDRAILS = (
    DATA
    / "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision"
    / "strict_noknob_upgrade_guardrails.packet.json"
)

STATUS = (
    "MTT_SELECTED_CORPUSPAPERREVISIONPACKET_OR_STRICTNOKNOBUPGRADEEXECUTION_"
    "BUILT_REVISION_PACKET_AND_ROUTE01_EXECUTION"
)
NEXT = "MTT_Selected_CorpusPaperRevisionExecution_or_StrictNoKnobUpgradeRoute01_v1"

RISK_PATTERNS = {
    "strict_no_knob_as_current": r"strict\s+(?:zero-primitive/)?no-knob\s+SM\s+closure",
    "zero_primitive_as_current": r"zero-primitive(?:/no-knob)?\s+(?:SM\s+)?closure",
    "lambda_H_independent": r"lambda_H\s+(?:is\s+)?(?:an\s+)?independent",
    "P_EW_derived_source_row": r"P_EW.*derived.*source\s+row",
    "observed_selector": r"observed\s+(?:lambda_H|SM\s+values?).*(?:select|selector)",
}


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def count_legacy_surfaces() -> dict:
    counts = {name: 0 for name in RISK_PATTERNS}
    files = {name: [] for name in RISK_PATTERNS}
    compiled = {name: re.compile(pattern, re.IGNORECASE) for name, pattern in RISK_PATTERNS.items()}

    for path in sorted(CORPUS.glob("*.md")):
        if path == NOTE:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in compiled.items():
            hits = len(pattern.findall(text))
            if hits:
                counts[name] += hits
                if len(files[name]) < 12:
                    files[name].append({"file": rel(path), "hit_count": hits})

    return {
        "schema": "MTTLegacyClaimSurfaceAudit.v1",
        "status": "LEGACY_SURFACE_AUDITED_FOR_REVISION",
        "risk_phrase_counts": counts,
        "sample_files_requiring_context_review": files,
        "interpretation": (
            "Hits are revision surfaces, not automatic errors. Historical artifacts may "
            "describe attempted strict no-knob routes; current papers must not present "
            "those routes as closed."
        ),
    }


def main() -> int:
    previous = load(PREVIOUS)
    paper = load(PAPER_UPDATE)
    upgrade = load(UPGRADE)
    decision = load(DECISION)
    guardrails = load(GUARDRAILS)
    legacy = count_legacy_surfaces()

    priority_targets = [
        "README.md",
        "proof_corpus/MTT_Selected_OnePrimitiveClosurePaperUpdate_or_StrictNoKnobUpgradeProgram_v1.md",
        "proof_corpus/MTT_Selected_PhysicalNormalizationAxiomDerivation_or_OnePrimitiveAdoptionDecision_v1.md",
        "proof_corpus/MTT_Selected_StrictPEWDirectKSourceRows_or_FinalSMNoKnobAudit_v1.md",
        "proof_corpus/MTT_Selected_HiggsThresholdStrictPEWExit_or_SelectedSourceRows_v1.md",
        "proof_corpus/MTT_Selected_PhysicalNormalizationSourceAxiom_or_DirectKCertificate_v1.md",
        "proof_corpus/MTT_Selected_FullSMMinimalParameterLedger_or_StrictPEWSourceTheorem_v1.md",
        "proof_corpus/MTT_Selected_Qutrit27MatrixMinimalClosure_or_StrictPEWUpgrade_v1.md",
        "proof_corpus/MTT_Selected_FinalYukawaReplayResidualExactness_or_StrictSMNoKnobClosure_v1.md",
        "proof_corpus/MTT_TrueSMClosure_CurrentStatus_Step42_v1.md",
    ]

    replacement_table = [
        {
            "old_surface": "strict zero-primitive/no-knob SM closure",
            "replacement": "one-shared-physical-primitive SM closure",
            "condition": "Use when describing the current proved closure standard.",
        },
        {
            "old_surface": "full no-knob closure",
            "replacement": "strict no-knob upgrade target",
            "condition": "Use unless a strict P_EW/direct-K selected row is actually accepted.",
        },
        {
            "old_surface": "lambda_H as an independent H-specific parameter",
            "replacement": "lambda_H is downstream of the shared P_EW primitive and is not H-specific",
            "condition": "Use in parameter-count ledgers.",
        },
        {
            "old_surface": "P_EW is a derived strict selected source row",
            "replacement": "P_EW is the one shared physical normalization primitive",
            "condition": "Use until strict source rows are nonzero.",
        },
        {
            "old_surface": "observed values select the source operator",
            "replacement": "observed values enter only downstream of the selected source boundary",
            "condition": "Use in all source/provenance sections.",
        },
        {
            "old_surface": "SM closure without a stated standard",
            "replacement": paper["short_claim"],
            "condition": "Use in abstracts, theorem statements, and status summaries.",
        },
    ]

    revision_packet = {
        "schema": "MTTCorpusPaperRevisionPacketAfterOnePrimitiveAdoption.v1",
        "status": "CORPUS_PAPER_REVISION_PACKET_READY",
        "previous_candidate": rel(PREVIOUS),
        "current_closure_standard": "one_shared_physical_primitive",
        "canonical_claim": paper["canonical_claim"],
        "short_claim": paper["short_claim"],
        "paper_abstract_sentence": paper["paper_abstract_sentence"],
        "paper_limitations_sentence": paper["paper_limitations_sentence"],
        "allowed_claims": paper["allowed_claims"],
        "forbidden_claims": paper["forbidden_claims"],
        "required_paper_edits": paper["required_paper_edits"],
        "priority_revision_targets": priority_targets,
        "replacement_table": replacement_table,
        "source_boundary_policy": {
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "accepted_statement": (
                "Observed SM values may be replayed or compared only after the selected "
                "MTT source/operator boundary is fixed."
            ),
        },
        "strict_status_to_preserve": {
            "strict_no_knob_closure": False,
            "accepted_strict_P_EW_source_rows": guardrails["accepted_strict_P_EW_source_rows"],
            "accepted_direct_K_threshold_Omega_H_lambda_rows": guardrails[
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "accepted_strict_derivation_route_count": guardrails[
                "accepted_strict_derivation_route_count"
            ],
        },
        "revision_complete_when": [
            "All current manuscripts use the canonical one-shared-primitive closure claim.",
            "Every strict no-knob claim is explicitly marked as an upgrade target.",
            "P_EW is counted once and lambda_H is not counted as H-specific.",
            "No observed SM number is described as selecting the source.",
            "The strict upgrade program is cited as the next theorem sequence.",
        ],
    }

    strict_route = {
        "schema": "MTTStrictNoKnobRoute01ExecutionAfterRevisionPacket.v1",
        "status": "STRICT_NOKNOB_ROUTE01_READY_TO_ATTACK",
        "route": "derive physical-normalization axiom from same-branch source data",
        "route_id": "UPG-01",
        "blocked_quantities": {
            "physical_normalization_axiom_derived": False,
            "accepted_strict_P_EW_source_rows": 0,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
        },
        "execution_tests": [
            {
                "id": "R01-T1",
                "test": "construct finite projected physical measure functional M_phys",
                "success_condition": "M_phys emits P_EW normalization before observed replay",
            },
            {
                "id": "R01-T2",
                "test": "show same-branch equality between M_phys and K_threshold.Omega_H.lambda",
                "success_condition": "direct-K row certificate count becomes positive",
            },
            {
                "id": "R01-T3",
                "test": "show invariance under allowed lens/circle/bundle gauge reparameterizations",
                "success_condition": "normalization is selected, not convention-chosen",
            },
            {
                "id": "R01-T4",
                "test": "replay 27-matrix/H/Yukawa ledgers with P_EW source replaced by derived row",
                "success_condition": "one shared primitive count drops from one to zero",
            },
        ],
        "do_not_repeat": [
            "Do not re-open the already accepted one-shared-primitive closure standard.",
            "Do not count finite-support rows as final scalar rows unless value rows are emitted.",
            "Do not use external measured Higgs quartic data to select the normalization.",
        ],
        "next_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedCorpusPaperRevisionPacketOrStrictNoKnobUpgradeExecution",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "paper_update_claims": rel(PAPER_UPDATE),
            "strict_upgrade_program": rel(UPGRADE),
            "publication_decision": rel(DECISION),
            "guardrails": rel(GUARDRAILS),
        },
        "output_packets": {
            "corpus_paper_revision_packet": rel(REVISION_PACKET),
            "legacy_claim_surface_audit": rel(LEGACY_AUDIT),
            "strict_noknob_route01_execution_packet": rel(STRICT_ROUTE),
        },
        "theorem": {
            "name": "CorpusPaperRevisionPacketAndRoute01ExecutionTheorem",
            "proved": True,
            "statement": (
                "The one-shared-physical-primitive closure standard is now converted "
                "into a corpus-revision packet and the next strict no-knob route is "
                "made executable. This closes the paper-wording/provenance layer and "
                "keeps the strict PEW/direct-K source theorem as the only route that "
                "can reduce the shared primitive count from one to zero."
            ),
        },
        "closed_now": [
            "Corpus revision targets are named.",
            "Allowed and forbidden paper claims are copied into an executable packet.",
            "Legacy claim surfaces are audited as revision surfaces.",
            "Strict no-knob Route 01 has explicit execution tests.",
        ],
        "not_closed": [
            "The external manuscript corpus has not been rewritten by this artifact.",
            "The physical-normalization axiom is not yet derived.",
            "Strict PEW/direct-K rows remain zero.",
        ],
        "key_numbers": {
            "priority_revision_target_count": len(priority_targets),
            "replacement_rule_count": len(replacement_table),
            "allowed_claim_count": len(paper["allowed_claims"]),
            "forbidden_claim_count": len(paper["forbidden_claims"]),
            "strict_route_execution_test_count": len(strict_route["execution_tests"]),
            "strict_P_EW_source_rows": 0,
            "strict_direct_K_rows": 0,
            "shared_physical_primitive_count": previous["key_numbers"][
                "shared_physical_primitive_count"
            ],
            "H_specific_parameter_count": previous["key_numbers"]["H_specific_parameter_count"],
        },
        "closure_decision": {
            "corpus_revision_packet_ready": True,
            "legacy_surface_audit_ready": True,
            "strict_route01_execution_ready": True,
            "current_closure_standard": "one_shared_physical_primitive",
            "one_shared_primitive_tier_closed": True,
            "strict_no_knob_closure": False,
            "true_precision_equivalence_closed": False,
            "global_true_SM_no_knob_closure": False,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_CorpusPaperRevisionPacket_or_StrictNoKnobUpgradeExecution_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "corpus_revision_packet_ready": True,
        "legacy_surface_audit_ready": True,
        "strict_route01_execution_ready": True,
        "current_closure_standard": "one_shared_physical_primitive",
        "one_shared_primitive_tier_closed": True,
        "strict_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected CorpusPaperRevisionPacket or StrictNoKnobUpgradeExecution v1

Status: `{STATUS}`

## What This Closes

The current result is now locked as:

`{paper["short_claim"]}`

This artifact converts that result into a paper-revision packet. It names the
files to review, the exact replacement rules, the allowed claims, and the
forbidden claims.

## Required Replacement

Use:

`{paper["canonical_claim"]}`

Do not state strict zero-primitive/no-knob closure as the current result.

## Strict Route 01

Next proof route: derive the physical-normalization axiom from same-branch
source data.

Success requires:

1. a finite projected physical measure functional emitting `P_EW`;
2. a same-branch equality to `K_threshold.Omega_H.lambda`;
3. gauge/lens/circle invariance of the emitted normalization;
4. replay of the 27-matrix/H/Yukawa ledgers with zero shared primitives.

Current strict rows:

- strict `P_EW` source rows: `0`
- strict direct-K rows: `0`

Next required artifact: `{NEXT}`.
"""

    write_json(REVISION_PACKET, revision_packet)
    write_json(LEGACY_AUDIT, legacy)
    write_json(STRICT_ROUTE, strict_route)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
