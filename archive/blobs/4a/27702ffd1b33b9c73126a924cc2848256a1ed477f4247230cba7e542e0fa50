"""Build appendix-ready paper drafts for theorem-derived selected-source flags.

The integration manifest identifies every current "not theorem-derived" gate.
This artifact turns those gates into conservative appendix sections that can be
inserted into the relevant papers without promoting any open selected-source
flag.  The sections are proof slots: they strengthen rigor by naming the exact
theorem needed, its dependencies, validation artifacts, and the wording that is
safe before the theorem is proved.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
DRAFT_DIR = CORPUS / "paper_appendix_drafts" / "selected_source"
MANIFEST = DATA / "selected_source_paper_integration_manifest.candidate.json"
OUTPUT = DATA / "selected_source_paper_appendix_drafts.candidate.json"
CERT = CERTS / "selected_source_paper_appendix_drafts_certificate.json"
NOTE = CORPUS / "MTT_Selected_Source_Paper_Appendix_Drafts_v1.md"

PRIOR_REPO_PATTERNS = [
    {
        "repo": "mtt-q79-proof-repro",
        "evidence": "Iwasawa Route-C branch smoke attempt reports Route-C, D_E, and Riesz/Green failing only because selected_source_verified is false.",
        "lesson": "Algebraic validator success under lifted flags is a diagnostic, not selected-source proof.",
    },
    {
        "repo": "mtt-nonsm-constants-no-knob",
        "evidence": "Finite selected-connection source attempts reject packets whose downstream algebra works only after selected flags are lifted.",
        "lesson": "The same theorem-derived flag policy must govern constants outside the SM packet as well.",
    },
]

INSERTION_DEPENDENCIES = {
    "I1_selected_strominger_minimizer_to_phifin_trace": [],
    "I2_projective_rhoe_source_promotion": [
        "I1_selected_strominger_minimizer_to_phifin_trace",
    ],
    "I3_smooth_bn_galerkin_lift_theorem": [
        "I1_selected_strominger_minimizer_to_phifin_trace",
        "I2_projective_rhoe_source_promotion",
    ],
    "I4_selected_DE_action_and_source_flags": [
        "I1_selected_strominger_minimizer_to_phifin_trace",
        "I3_smooth_bn_galerkin_lift_theorem",
    ],
    "I5_dotD_alpha1_and_C1_response": [
        "I4_selected_DE_action_and_source_flags",
    ],
    "I6_parameter_policy_appendix_update": [],
}

VALIDATION_ARTIFACTS = {
    "I1_selected_strominger_minimizer_to_phifin_trace": [
        "candidate_data/finite_emission_morphism_phifin.candidate.json",
        "candidate_data/routec_selected_source_origin_lemma.candidate.json",
    ],
    "I2_projective_rhoe_source_promotion": [
        "candidate_data/selected_routec_nonidentity_rhoe_bn_construction.candidate.json",
        "candidate_data/projective_gerbe_rhoe_source_promotion.candidate.json",
    ],
    "I3_smooth_bn_galerkin_lift_theorem": [
        "candidate_data/selected_routec_smooth_bn_galerkin_lift.candidate.json",
    ],
    "I4_selected_DE_action_and_source_flags": [
        "candidate_data/selected_routec_de_action_on_smooth_bn.candidate.json",
    ],
    "I5_dotD_alpha1_and_C1_response": [
        "candidate_data/selected_source_origin_and_alpha1_driver.candidate.json",
        "candidate_data/selected_phifin_alpha1_payload.candidate.json",
    ],
    "I6_parameter_policy_appendix_update": [
        "candidate_data/selected_source_paper_integration_manifest.candidate.json",
    ],
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def slug(name: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "_" for ch in name).strip("_")


def theorem_label(insertion_id: str) -> str:
    return "Theorem slot " + insertion_id.split("_", 1)[0].upper()


def draft_text(item: dict, manifest: dict, target_key: str) -> str:
    dependencies = INSERTION_DEPENDENCIES[item["id"]]
    artifacts = VALIDATION_ARTIFACTS[item["id"]]
    dependency_text = (
        "None. This section is a root policy/source-selection section."
        if not dependencies
        else "\n".join(f"- `{dep}`" for dep in dependencies)
    )
    artifact_text = "\n".join(f"- `{artifact}`" for artifact in artifacts)
    blockers = "\n".join(f"- `{blocker}`" for blocker in item["current_blockers_resolved_if_proved"])
    obligations = "\n".join(f"- {obligation}" for obligation in item["proof_obligations"])
    prior_text = "\n".join(
        f"- `{entry['repo']}`: {entry['lesson']} Evidence: {entry['evidence']}"
        for entry in PRIOR_REPO_PATTERNS
    )
    paper_path = manifest["papers"][target_key]

    return (
        f"## {item['section_title']}\n\n"
        f"Target paper: `{paper_path}`\n\n"
        f"Status: `APPENDIX_DRAFT_PROOF_SLOT_OPEN`\n\n"
        f"Proof label: **{theorem_label(item['id'])}**\n\n"
        "Purpose: convert a current selected-source caveat into an explicit theorem slot. "
        "This section does not promote any lifted diagnostic flag.\n\n"
        "Statement to add:\n\n"
        f"> {item['theorem_statement']}\n\n"
        "Current blockers closed if and only if the statement is proved:\n"
        f"{blockers}\n\n"
        "Proof obligations:\n"
        f"{obligations}\n\n"
        "Dependencies inside the selected-source appendix chain:\n"
        f"{dependency_text}\n\n"
        "Executable or corpus artifacts to cite while proving this section:\n"
        f"{artifact_text}\n\n"
        "Safe wording before proof:\n\n"
        f"> {item['safe_wording']}\n\n"
        "Required guardrail sentence:\n\n"
        "> No observed masses, mixings, thresholds, or fitted constants are used to select the source, branch, cover, operator, or promotion flag in this section.\n\n"
        "Cross-repo consistency note:\n"
        f"{prior_text}\n"
    )


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)

    drafts_by_paper: dict[str, list[dict]] = defaultdict(list)
    insertion_index = {}
    for item in manifest["insertions"]:
        insertion_index[item["id"]] = {
            "section_title": item["section_title"],
            "status": "APPENDIX_DRAFT_PROOF_SLOT_OPEN",
            "dependencies": INSERTION_DEPENDENCIES[item["id"]],
            "validation_artifacts": VALIDATION_ARTIFACTS[item["id"]],
            "target_papers": item["target_papers"],
            "promotes_selected_flags_now": False,
        }
        for target in item["target_papers"]:
            text = draft_text(item, manifest, target)
            filename = f"{target}__{slug(item['id'])}.md"
            path = DRAFT_DIR / filename
            path.write_text(text, encoding="utf-8")
            drafts_by_paper[target].append(
                {
                    "insertion_id": item["id"],
                    "draft_path": rel(path),
                    "paper_path": manifest["papers"][target],
                    "section_title": item["section_title"],
                }
            )

    packet = {
        "candidate": "MTTSelectedSourcePaperAppendixDrafts",
        "status": "MTT_SELECTED_SOURCE_PAPER_APPENDIX_DRAFTS_BUILT_PROOF_SLOTS_OPEN",
        "source_manifest": rel(MANIFEST),
        "draft_directory": rel(DRAFT_DIR),
        "drafts_by_paper": dict(sorted(drafts_by_paper.items())),
        "insertion_index": insertion_index,
        "policy": {
            "appendix_sections_are_proof_slots": True,
            "selected_flags_promoted_now": False,
            "diagnostic_lifts_remain_diagnostic_only": True,
            "target_fitting_used": False,
            "observed_constants_as_selectors": False,
        },
        "prior_repo_patterns": PRIOR_REPO_PATTERNS,
        "what_closes_now": {
            "actual_appendix_draft_text_created": True,
            "each_not_theorem_derived_gate_has_paper_home": True,
            "safe_wording_made_insertable": True,
            "dependencies_between_theorem_slots_recorded": True,
            "cross_repo_flag_policy_aligned": True,
        },
        "what_remains_open": {
            "appendix_text_inserted_into_corpus_papers": True,
            "theorem_proofs_completed": True,
            "selected_source_flags_promoted": True,
            "honest_replay_without_lifted_flags": True,
        },
        "next_required_artifact": "MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1",
        "closure_claimed": False,
    }

    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": packet["status"],
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "draft_directory": rel(DRAFT_DIR),
                "draft_count": sum(len(v) for v in drafts_by_paper.values()),
                "what_closes": packet["what_closes_now"],
                "what_remains_open": packet["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    rows = []
    for target, entries in sorted(drafts_by_paper.items()):
        rows.append(f"## {target}\n")
        rows.append(f"Paper: `{manifest['papers'][target]}`\n")
        for entry in entries:
            rows.append(
                f"- `{entry['insertion_id']}` -> `{entry['draft_path']}` "
                f"({entry['section_title']})"
            )
        rows.append("")

    NOTE.write_text(
        "# MTT Selected Source Paper Appendix Drafts\n\n"
        f"Status: `{packet['status']}`\n\n"
        "These drafts are insertion-ready proof slots for every current selected-source caveat. "
        "They extend the papers rigorously by adding theorem labels, dependencies, proof obligations, validation artifacts, and safe wording. "
        "They do not claim the theorems are proved.\n\n"
        "Policy: diagnostic source-lift packets remain algebraic smoke tests only. "
        "A selected flag can be set true only after the matching theorem slot is proved and cited.\n\n"
        + "\n".join(rows)
        + "\nNext numerical artifact: `MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1`.\n",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": packet["status"]}, indent=2))


if __name__ == "__main__":
    main()
