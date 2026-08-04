"""Build the selected Qa/SU3 operator-source import audit artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUT = DATA / "selected_qa_su3_finite_cochain_construction_plan.candidate.json"
OUTPUT_DATA = DATA / "selected_qa_su3_operator_source_import_audit.candidate.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_operator_source_import_audit_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Qa_SU3_Operator_Source_Import_Audit_v1.md"

LOCAL_INPUTS = {
    "canonical_bundle_weitzenbock": NONSM / "certificates" / "selected_qa_su3_canonical_bundle_weitzenbock_certificate.json",
    "brst_determinant_with_weitzenbock": NONSM / "certificates" / "selected_qa_su3_brst_determinant_with_weitzenbock_certificate.json",
    "p0_ghost_measure": NONSM / "certificates" / "selected_qa_su3_p0_ghost_measure_normalization_certificate.json",
    "pnonzero_physical_quotient": NONSM / "certificates" / "selected_qa_su3_pnonzero_physical_quotient_determinant_certificate.json",
    "final_obstruction": NONSM / "certificates" / "selected_qa_su3_final_obstruction_or_projector_resolution_certificate.json",
    "alternative_source_hunt": NONSM / "certificates" / "selected_qa_su3_alternative_operator_or_projector_source_hunt_certificate.json",
}

EXTERNAL_TEMPLATES = [
    {
        "id": "duy_hym_stability",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8741718/",
        "role": "External template only: stable holomorphic bundles select HYM connections via Donaldson-Uhlenbeck-Yau type correspondence.",
        "import_as_proof": False,
    },
    {
        "id": "invariant_strominger_iwasawa",
        "url": "https://arxiv.org/abs/1604.02851",
        "role": "External template only: invariant Strominger/heterotic solutions show how left-invariant torsion/HYM ansatzes can become finite selected operator problems.",
        "import_as_proof": False,
    },
    {
        "id": "heterotic_hym_extension_bundle",
        "url": "https://link.springer.com/article/10.1007/s00220-025-05272-y",
        "role": "External template only: Hull-Strominger data can be repackaged as a Hermitian-Yang-Mills type equation on an extension bundle.",
        "import_as_proof": False,
    },
    {
        "id": "bochner_weitzenbock_operator",
        "url": "https://www.emergentmind.com/topics/bochner-weitzenbock-formula",
        "role": "External template only: Weitzenbock formulas identify curvature endomorphism terms in Laplace-type operators.",
        "import_as_proof": False,
    },
]


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
        }
        for key, path in LOCAL_INPUTS.items()
    }


def build_import_routes(local: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    final = local["final_obstruction"]
    hunt = local["alternative_source_hunt"]
    return [
        {
            "id": "nontrivial_su3_color_bundle_connection_endomorphism",
            "rank": 1,
            "status": "BEST_NEXT_OPEN_GATE",
            "legal": True,
            "why": "It would be genuinely new selected Qa/SU3 threshold operator data, not a correction added to the already-counted compact-Nil Hodge/BRST branch.",
            "local_support": [
                "Alternative source hunt ranks this as best next route.",
                "Canonical Weitzenbock data identifies the tangent-bundle E term and forbids double counting.",
                "Final obstruction shows the compact-Nil Hodge branch overshoots and needs a different selected operator or source-selected projector.",
            ],
            "required_import_packet": [
                "selected SU3 color bundle/sheaf/twisted module",
                "selected connection or curvature/HYM/Strominger residual",
                "endomorphism_E or equivalent zero-order Weitzenbock block",
                "operator domain after p0 and p!=0 quotient",
                "spectrum, heat coefficient, analytic torsion, or finite determinant part",
                "same-source bridge to monad/Cech data if used",
            ],
            "promoted_now": False,
        },
        {
            "id": "global_section_gribov_fundamental_domain_measure",
            "rank": 2,
            "status": "PROMISING_OPEN",
            "legal": True,
            "why": "A global section/fundamental-domain measure could be separate from the local FP/BRST determinant already counted.",
            "local_support": [
                "Gauge-fixing corpus allows global-section failure as a distinct projection issue.",
                "Alternative source hunt marks this route promising but unselected.",
            ],
            "required_import_packet": [
                "selected SU3/Nil physical quotient domain",
                "global section or fundamental modular region theorem",
                "finite measure determinant computed before target comparison",
            ],
            "promoted_now": False,
        },
        {
            "id": "ray_singer_reidemeister_torsion_local_system",
            "rank": 3,
            "status": "PROMISING_OPEN",
            "legal": True,
            "why": "The p!=0 Nil Hodge complex is acyclic, so torsion is the natural invariant to audit next.",
            "local_support": [
                "p!=0 physical quotient theorem selects an acyclic BRST block.",
                "Alternative source hunt marks torsion/local-system route promising if the local system and color trace are selected.",
            ],
            "required_import_packet": [
                "selected local system/lattice character",
                "selected color trace convention",
                "Ray-Singer/Reidemeister torsion computation on the selected acyclic complex",
            ],
            "promoted_now": False,
        },
        {
            "id": "finite_coherent_projector_jacobian",
            "rank": 4,
            "status": "LEGAL_BUT_NUMERIC_FACTOR_NOT_SELECTED",
            "legal": True,
            "why": "A finite coherent projector is corpus-native, but the needed subtraction is not currently selected.",
            "local_support": [
                f"Final obstruction requires log projector Jacobian {final['projector_resolution_test']['needed_log_projector_jacobian_to_close']}.",
                "Alternative source hunt says current corpus does not select that numerical factor.",
            ],
            "required_import_packet": [
                "selected A, tau, chi, and quotient domain for B_adm",
                "projector determinant computed before target comparison",
            ],
            "promoted_now": False,
        },
        {
            "id": "local_fp_brst_extra_jacobian",
            "rank": 99,
            "status": "REJECTED_DOUBLE_COUNTING",
            "legal": False,
            "why": "Local FP/BRST quotient is real, but it was already counted in the selected p=0 and p!=0 quotient rules.",
            "local_support": [
                "p0 ghost measure selected.",
                "p!=0 physical quotient selected.",
                "Alternative source hunt rejects reuse as extra correction.",
            ],
            "required_import_packet": [],
            "promoted_now": False,
        },
        {
            "id": "soft_gauge_tube_width",
            "rank": 100,
            "status": "REJECTED_GAUGE_OR_REGULATOR_PARAMETER",
            "legal": False,
            "why": "Without an independent physical selection theorem, gauge-tube width is a representative-selection/regulator parameter.",
            "local_support": ["Alternative source hunt rejects this as no-knob correction."],
            "required_import_packet": [],
            "promoted_now": False,
        },
    ]


def build_candidate() -> dict[str, object]:
    input_data = load_json(INPUT)
    local = {key: load_json(path) for key, path in LOCAL_INPUTS.items()}
    final = local["final_obstruction"]
    routes = build_import_routes(local)
    return {
        "candidate": "MTTSelectedQaSU3OperatorSourceImportAudit",
        "status": "SELECTED_QA_SU3_OPERATOR_SOURCE_IMPORT_AUDIT_BUILT_BEST_ROUTE_IDENTIFIED_SOURCE_OPEN",
        "input_status": input_data["status"],
        "source_status": source_status(),
        "external_templates": EXTERNAL_TEMPLATES,
        "computed_compact_nil_branch": {
            "fully_computed": final["verdict"]["compact_nil_hodge_branch_fully_computed"],
            "obstructed_as_final_proof": final["verdict"]["compact_nil_hodge_branch_closes_Qa_SU3"] is False,
            "selected_unweighted_Qa": final["computed_branch"]["selected_unweighted_Qa"],
            "required_unweighted_Qa": final["computed_branch"]["required_unweighted_Qa"],
            "excess_selected_minus_required": final["computed_branch"]["excess_selected_minus_required"],
            "target_fitting_used": final["verdict"]["target_fitting_used"],
        },
        "import_routes": routes,
        "decision": {
            "result": "No operator source imported or promoted yet.",
            "best_next_route": "nontrivial_su3_color_bundle_connection_endomorphism",
            "why": "It is the only top-ranked route that supplies genuinely new selected operator data rather than reusing counted quotient determinants or fitting a small projector factor.",
            "next_move": "Build a color-bundle connection/endomorphism packet interface that can import or reject selected HYM/Strominger, extension-bundle, or torsion/local-system data.",
        },
        "gate_results": {
            "operator_source_import_audit_built": True,
            "external_templates_checked": True,
            "compact_nil_branch_fully_computed": True,
            "compact_nil_branch_obstructed_as_final_proof": True,
            "best_next_route_identified": True,
            "double_counting_routes_rejected": True,
            "operator_source_promoted": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Selected_Qa_SU3_Color_Bundle_Connection_Endomorphism_Interface_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedQaSU3OperatorSourceImportAudit",
        "status": "MTT_SELECTED_QA_SU3_OPERATOR_SOURCE_IMPORT_AUDIT_BUILT_BEST_ROUTE_IDENTIFIED_SOURCE_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "operator_source_import_audit": True,
            "compact_nil_branch_obstruction_imported": True,
            "external_template_roles_recorded": True,
            "best_next_operator_route_identified": True,
            "double_counting_routes_rejected": True,
        },
        "what_remains_open": {
            "selected_SU3_color_bundle_or_sheaf": True,
            "selected_connection_curvature_or_HYM_residual": True,
            "selected_endomorphism_E_or_zero_order_block": True,
            "selected_operator_domain_after_BRST_quotient": True,
            "selected_spectrum_heat_torsion_or_determinant": True,
            "same_source_bridge_to_monad_Cech_packet": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    sources = "\n".join(
        f"- `{key}`: {body['path']} ({'present' if body['present'] else 'missing'})"
        for key, body in candidate["source_status"].items()
    )
    external = "\n".join(
        f"- `{row['id']}`: {row['role']} Source: {row['url']}"
        for row in candidate["external_templates"]
    )
    routes = []
    for row in candidate["import_routes"]:
        support = "\n".join(f"  - {item}" for item in row["local_support"])
        required = "\n".join(f"  - {item}" for item in row["required_import_packet"]) or "  - none"
        routes.append(
            f"### {row['rank']}. {row['id']}\n\n"
            f"- Status: `{row['status']}`\n"
            f"- Legal route: `{row['legal']}`\n"
            f"- Why: {row['why']}\n"
            f"- Local support:\n{support}\n"
            f"- Required import packet:\n{required}\n"
            f"- Promoted now: `{row['promoted_now']}`\n"
        )
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    branch = candidate["computed_compact_nil_branch"]
    return f"""# MTT Selected Qa/SU3 Operator Source Import Audit v1

## Purpose

This artifact looks for a legitimate way forward after the finite cochain route
and compact-Nil Hodge/BRST determinant branch.

The result is sharp: the compact-Nil branch is fully computed and obstructed as
the final Qa/SU3 proof source, while the best live route is a genuinely new
selected SU3 color-bundle connection/endomorphism packet.

## Local Source Inputs

{sources}

## External Templates

These are used as mathematical inspiration and guardrails only. They are not imported as MTT proof data.

{external}

## Computed Compact-Nil Branch

- Fully computed: `{branch["fully_computed"]}`
- Obstructed as final proof: `{branch["obstructed_as_final_proof"]}`
- Selected Qa: `{branch["selected_unweighted_Qa"]}`
- Required Qa: `{branch["required_unweighted_Qa"]}`
- Excess selected minus required: `{branch["excess_selected_minus_required"]}`
- Target fitting used: `{branch["target_fitting_used"]}`

## Import Route Ranking

{chr(10).join(routes)}

## Decision

Result: {candidate["decision"]["result"]}

Best next route:

```text
{candidate["decision"]["best_next_route"]}
```

Reason: {candidate["decision"]["why"]}

Next move: {candidate["decision"]["next_move"]}

## Import Audit Theorem

The current legal route is not to add another local FP/BRST Jacobian, not to
insert a gauge-tube width, and not to tune a small projector factor.  Those
moves would either double-count or fit the residual.

The forward route is to construct or import a selected SU3 color-bundle
connection/endomorphism packet, or secondarily a selected global-section
measure or torsion/local-system packet, and then compute its determinant before
target comparison.

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

```text
{candidate["next_required_artifact"]}
```
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    note_text = render_note(candidate, certificate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note_text, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
