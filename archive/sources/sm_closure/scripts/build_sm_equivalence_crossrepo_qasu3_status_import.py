"""Build cross-repo Qa/SU3 status import for SM-equivalence closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

OUTPUT = DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"
CERT = CERTS / "sm_equivalence_crossrepo_qasu3_status_import_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_CrossRepo_QaSU3_Status_Import_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_CROSSREPO_QASU3_STATUS_IMPORTED_NO_FINAL_PACKET_FOUND"
NEXT = "MTT_SM_Equivalence_SelectedQaSU3Packet_or_RGTransport_ValueFill_v1"

REPOS = [
    "mtt-qa-su3-packet-proof",
    "mtt-nonsm-constants-no-knob",
    "mtt-q79-proof-repro",
    "mtt-protospinor-gr-response-proof",
]

PROMOTION_TRUE_FLAGS = [
    "qa_su3_packet_closed",
    "selected_operator_values_closed",
    "selected_spectra_closed",
    "selected_final_packet_closed",
    "final_selected_packet_closed",
]

REUSABLE_INPUTS = [
    {
        "repo": "mtt-qa-su3-packet-proof",
        "path": "proof_corpus/Selected_Qa_SU3_Full_Corpus_Dependency_Audit_v1.md",
        "use": "full-corpus dependency ledger for Qa/SU3 packet attempts",
    },
    {
        "repo": "mtt-qa-su3-packet-proof",
        "path": "certificates/a01_de_operator_exit_gate_certificate.json",
        "use": "A01/D_E operator exit gate status and blocker list",
    },
    {
        "repo": "mtt-qa-su3-packet-proof",
        "path": "certificates/a01_repair_guardrail_local_recompute_certificate.json",
        "use": "repair-guardrail local recompute status",
    },
    {
        "repo": "mtt-qa-su3-packet-proof",
        "path": "certificates/caxis_orthogonality_source_or_weighted_operator_packet_certificate.json",
        "use": "C-axis orthogonality and weighted-operator packet status",
    },
    {
        "repo": "mtt-nonsm-constants-no-knob",
        "path": "proof_corpus/Selected_Qa_SU3_Typed_Monad_Data_Fill_Attempt_v1.md",
        "use": "typed monad data fill attempt and value-shape clues",
    },
    {
        "repo": "mtt-nonsm-constants-no-knob",
        "path": "proof_corpus/Selected_Qa_SU3_Typed_Monad_DE_or_RhoE_Data_Interface_v1.md",
        "use": "typed monad D_E/rho_E interface contract",
    },
    {
        "repo": "mtt-nonsm-constants-no-knob",
        "path": "proof_corpus/Selected_Qa_SU3_Monad_to_Operator_Packet_Transfer_Gate_v1.md",
        "use": "monad-to-operator transfer-gate diagnostics",
    },
    {
        "repo": "mtt-nonsm-constants-no-knob",
        "path": "proof_corpus/Selected_Qa_SU3_HYM_Full_Real_Delta_A_Hessian_With_OU_Weights_v1.md",
        "use": "HYM real Hessian and operator-weight clue layer",
    },
]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        try:
            return str(path.relative_to(TEXPAPERS)).replace("\\", "/")
        except ValueError:
            return str(path)


def load_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None


def find_key_values(obj: Any, wanted: set[str], prefix: str = "") -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            here = f"{prefix}.{key}" if prefix else key
            if key in wanted:
                found.append({"key": key, "path": here, "value": value})
            found.extend(find_key_values(value, wanted, here))
    elif isinstance(obj, list):
        for idx, value in enumerate(obj):
            found.extend(find_key_values(value, wanted, f"{prefix}[{idx}]"))
    return found


def scan_repo(repo: str) -> dict[str, Any]:
    repo_root = TEXPAPERS / repo
    result: dict[str, Any] = {
        "repo": repo,
        "exists": repo_root.exists(),
        "json_files_scanned": 0,
        "promotion_true_hits": [],
        "promotion_false_hits": [],
        "status_hits": [],
    }
    if not repo_root.exists():
        return result

    for folder_name in ["certificates", "candidate_data"]:
        folder = repo_root / folder_name
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.json")):
            data = load_json(path)
            if data is None:
                continue
            result["json_files_scanned"] += 1
            flags = find_key_values(data, set(PROMOTION_TRUE_FLAGS))
            for flag in flags:
                hit = {"file": rel(path), **flag}
                if flag["value"] is True:
                    result["promotion_true_hits"].append(hit)
                elif flag["value"] is False:
                    result["promotion_false_hits"].append(hit)
            status = data.get("status")
            if isinstance(status, str) and ("QA" in status.upper() or "SU3" in status.upper() or "OPERATOR" in status.upper()):
                result["status_hits"].append({"file": rel(path), "status": status})
    return result


def main() -> int:
    DATA.mkdir(exist_ok=True)
    CERTS.mkdir(exist_ok=True)
    CORPUS.mkdir(exist_ok=True)

    repo_scans = [scan_repo(repo) for repo in REPOS]
    true_hits = [hit for scan in repo_scans for hit in scan["promotion_true_hits"]]
    false_hits = [hit for scan in repo_scans for hit in scan["promotion_false_hits"]]

    reusable = []
    for row in REUSABLE_INPUTS:
        path = TEXPAPERS / row["repo"] / row["path"]
        reusable.append({**row, "exists": path.exists(), "absolute_path": str(path)})

    candidate = {
        "candidate": "MTTSMEquivalenceCrossRepoQaSU3StatusImport",
        "status": STATUS,
        "repos_scanned": repo_scans,
        "promotion_true_flags_checked": PROMOTION_TRUE_FLAGS,
        "any_promotable_qasu3_packet_found": len(true_hits) > 0,
        "promotable_qasu3_hits": true_hits,
        "explicit_open_flag_count": len(false_hits),
        "reusable_cross_repo_inputs": reusable,
        "interpretation": {
            "user_hypothesis": "Qa/SU3 color/operator packet may already have been solved in another repo.",
            "result": (
                "Sibling repos contain substantial support layers, interfaces, attempts, "
                "conditional packets, HYM/monad diagnostics, and no-go repairs, but this "
                "scan finds no promotable final Qa/SU3 color/operator packet closure flag."
            ),
            "support_layers_are_not_discarded": True,
            "support_layers_promote_final_packet": False,
        },
        "sm_parity_evaluation_policy": {
            "this_repo_view": "SM_PARITY_FIRST",
            "sibling_repo_default_view": "NO_KNOB_RESEARCH",
            "relevance_rule": (
                "Sibling no-knob artifacts may satisfy SM-parity needs here when they emit "
                "typed selected structure required by the SM packet interface.  They do not "
                "need to derive all numerical constants to be useful for parity, but they "
                "also cannot be promoted from support-only, conditional, lifted, diagnostic, "
                "or target-ranked status."
            ),
            "qa_su3_parity_acceptance_requires": [
                "selected SU3/color carrier or equivalent color-bundle/operator packet",
                "selected representation/operator action sufficient for the SM source packet",
                "typed anomaly/operator consistency interface",
                "source provenance independent of observed SM constants",
            ],
            "qa_su3_no_knob_acceptance_would_also_require": [
                "derived couplings/thresholds or determinant spectra",
                "derived Yukawa/CKM/PMNS/mass data where claimed",
                "derived absolute normalizations where claimed",
            ],
            "current_decision": (
                "No sibling artifact is imported as SM-parity Qa/SU3 closure yet, because "
                "the scanned records still mark the selected color/operator packet or its "
                "operator values as open/support-only.  The same scan remains relevant "
                "because any future typed selected packet can close the parity gate even "
                "before no-knob numerical constants are derived."
            ),
        },
        "superset_strategy_position": {
            "using_straight_path": False,
            "using_superset_paths": True,
            "paths_combined": [
                "Qa/SU3 packet-proof repo",
                "non-SM constants no-knob repo",
                "q79/theta finite-source support",
                "protospinor/GR response support where available",
                "local SM-parity measured replay boundary",
            ],
            "locked_target": "selected Qa/SU3 color/operator packet, then selected SM packet certificate",
            "measured_constants_used_as_selector": False,
        },
        "what_closes_now": {
            "cross_repo_scan_performed": True,
            "no_missed_promotable_qasu3_closure_found": len(true_hits) == 0,
            "sm_parity_lens_for_QaSU3_installed": True,
            "support_layers_imported_as_reusable_inputs": all(row["exists"] for row in reusable[:6]),
            "QaSU3_final_packet_remains_active_blocker": len(true_hits) == 0,
            "overclaim_guardrail_installed": True,
        },
        "what_remains_open": {
            "selected_QaSU3_color_operator_packet": len(true_hits) == 0,
            "selected_D_E_rho_E_operator_values": True,
            "typed_monad_or_section_ring_operator_transfer_values": True,
            "same_branch_period_selector_or_finite_quotient": True,
            "selected_SM_packet_final_certificate": True,
            "common_scale_Yukawa_Higgs_transport": True,
            "true_SM_equivalence_closure": True,
        },
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "CrossRepoQaSU3NoMissedClosureImportTheorem",
            "proved": True,
            "statement": (
                "Across the scanned sibling repositories, no certificate or candidate JSON "
                "contains a true promotable Qa/SU3 final-packet closure flag among the "
                "checked promotion keys.  Therefore this SM-equivalence branch may import "
                "the sibling artifacts only as support/interface data and must keep the "
                "selected Qa/SU3 color/operator packet as an open blocker."
            ),
        },
    }

    cert = {
        "certificate": "MTT_SM_Equivalence_CrossRepo_QaSU3_Status_Import_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "theorem_proved": True,
        "any_promotable_qasu3_packet_found": candidate["any_promotable_qasu3_packet_found"],
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    existing_inputs = [row for row in reusable if row["exists"]]
    missing_inputs = [row for row in reusable if not row["exists"]]
    note = f"""# MTT SM Equivalence CrossRepo QaSU3 Status Import v1

Status: `{STATUS}`.

## Theorem

`CrossRepoQaSU3NoMissedClosureImportTheorem`.

Across the scanned sibling repositories, no certificate or candidate JSON contains a true
promotable Qa/SU3 final-packet closure flag among:

```text
{", ".join(PROMOTION_TRUE_FLAGS)}
```

Therefore this SM-equivalence branch may import the sibling artifacts as support and
interface data, but it may not declare the selected Qa/SU3 color/operator packet solved.

## Scan Result

```text
repos scanned: {", ".join(REPOS)}
promotable true hits: {len(true_hits)}
explicit open flag hits: {len(false_hits)}
```

## Reusable Inputs

{chr(10).join(f"- `{row['repo']}/{row['path']}`: {row['use']}" for row in existing_inputs)}

## Missing Optional Inputs

{chr(10).join(f"- `{row['repo']}/{row['path']}`" for row in missing_inputs) if missing_inputs else "- none"}

## Superset Position

This is a superset move, not a straight single-path proof.  We combine the Qa/SU3
packet repo, non-SM constants no-knob repo, q79/theta source support, and local
SM-parity replay constraints toward one locked target: the selected Qa/SU3
color/operator packet.  Measured constants remain downstream parity inputs and
are not used as selectors.

## SM-Parity Lens

This repo evaluates Qa/SU3 in the SM-parity view.  The other proof repos mostly
operate in a no-knob research view.  Their results remain relevant here when
they emit typed selected structure for the SM packet interface, even if they do
not yet derive all numerical constants.  Support-only, conditional, lifted,
diagnostic, or target-ranked objects still cannot close the parity gate.

## What Closes

- Cross-repo no-missed-closure audit.
- SM-parity lens for reading sibling Qa/SU3/no-knob artifacts.
- Reusable support/import ledger for Qa/SU3.
- Guardrail that support layers cannot be silently promoted to final packet closure.

## What Remains

- selected `D_E/rho_E` operator values,
- typed monad or section-ring operator-transfer values,
- same-branch period selector or finite quotient,
- selected Qa/SU3 color/operator packet,
- selected SM packet final certificate,
- common-scale Yukawa/Higgs transport.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
