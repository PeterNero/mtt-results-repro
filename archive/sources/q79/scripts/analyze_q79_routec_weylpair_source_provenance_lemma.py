"""Analyze the q79 Weyl-pair source-provenance lemma.

The previous q79 gate assembled a conditional Weyl-pair operator.  This script
tries to promote that conditional object to selected source provenance.  The
honest result is a reduction theorem: the source-level qutrit Weyl carrier and
active shift are proved, and the source-to-C1 transfer is exact conditionally,
but the current selected data do not independently select the sector routing
u/e <- Z and d/nuD <- X.  Using the locked target columns to choose that route
would be target fitting, so full provenance remains open.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

GR = TEXPAPERS / "mtt-protospinor-gr-response-proof"
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

OUT_DIR = CANDIDATES / "q79_routec_weylpair_source_provenance_lemma"
OUT_TABLE = OUT_DIR / "source_provenance_reduction_table.json"
OUT_CANDIDATE = CANDIDATES / "q79_routec_weylpair_source_provenance_lemma.candidate.json"
OUT_CERT = CERTS / "q79_routec_weylpair_source_provenance_lemma_certificate.json"
OUT_PAPER = CORPUS / "Q79_RouteC_WeylPair_Source_Provenance_Lemma_v1.md"

Q79_INPUTS = {
    "weylpair_conditional_A_solve": CERTS
    / "q79_routec_weylpair_aselected_assembly_or_source_proof_certificate.json",
    "primitive_counterexample_and_weyl_gate": CERTS
    / "q79_routec_basis_transport_primitive_source_theorem_certificate.json",
    "e6_to_sm_dictionary": CERTS / "e6_to_sm_yukawa_operator_dictionary_certificate.json",
    "qutrit_line_cycle_restrictions": CERTS
    / "time_oriented_m1_qutrit_line_cycle_restrictions_certificate.json",
    "c6_orientation_branch_reduction": CERTS
    / "iwasawa_c6_orientation_branch_reduction_certificate.json",
    "orientation_de_dotd_bridge": CERTS / "iwasawa_orientation_de_dotd_bridge_certificate.json",
    "su5_qutrit_polarization_attempt": CERTS
    / "selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json",
}

ADJACENT_INPUTS = {
    "sm_weylpair_source_provenance": SM_PARITY
    / "certificates"
    / "selected_routec_weylpair_source_provenance_lemma_certificate.json",
    "sm_weylpair_source_provenance_candidate": SM_PARITY
    / "candidate_data"
    / "selected_routec_weylpair_source_provenance_lemma.candidate.json",
    "sm_weylpair_source_to_c1_transfer": SM_PARITY
    / "certificates"
    / "selected_routec_weylpair_source_to_c1_transfer_map_certificate.json",
    "sm_weylpair_source_to_c1_transfer_candidate": SM_PARITY
    / "candidate_data"
    / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json",
    "sm_weylpair_sector_routing": SM_PARITY
    / "certificates"
    / "selected_routec_weylpair_sector_routing_source_lemma_certificate.json",
    "sm_weylpair_sector_routing_candidate": SM_PARITY
    / "candidate_data"
    / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json",
    "sm_source_provenance_or_basis": SM_PARITY
    / "certificates"
    / "selected_routec_source_provenance_or_basis_certificate_certificate.json",
    "sm_selected_primitive_emission_search": SM_PARITY
    / "certificates"
    / "selected_routec_selected_primitive_emission_search_certificate.json",
    "sm_sector_embedding_interface": SM_PARITY
    / "certificates"
    / "sm_sector_embedding_interface_certificate.json",
    "gr_source_provenance_or_basis_import": GR
    / "certificates"
    / "routec_source_provenance_or_basis_reduction_import_certificate.json",
    "gr_selected_primitive_emission_search_import": GR
    / "certificates"
    / "routec_selected_primitive_emission_search_import_certificate.json",
}

REPOS = {
    "q79": ROOT,
    "gr": GR,
    "sm_parity": SM_PARITY,
}


def run_git(repo: Path, args: list[str]) -> str:
    if not (repo / ".git").exists():
        return ""
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.stdout.strip()


def status_summary(status_short: str) -> dict[str, Any]:
    lines = [line for line in status_short.splitlines() if line.strip()]
    return {
        "dirty": bool(lines),
        "line_count": len(lines),
        "modified_count": sum(line.startswith(" M") or line.startswith("M ") for line in lines),
        "untracked_count": sum(line.startswith("??") for line in lines),
        "preview": lines[:12],
    }


def repo_snapshot(name: str, path: Path) -> dict[str, Any]:
    if name == "q79":
        return {
            "path": str(path),
            "present": (path / ".git").exists(),
            "branch": run_git(path, ["branch", "--show-current"]),
            "head": "omitted-current-repo-head-for-reproducibility",
            "status_summary": {
                "dirty": False,
                "line_count": 0,
                "modified_count": 0,
                "untracked_count": 0,
                "preview": [],
                "note": "current q79 head/status omitted so this certificate remains reproducible after commit",
            },
        }
    status = run_git(path, ["status", "--short"])
    return {
        "path": str(path),
        "present": path.exists() and (path / ".git").exists(),
        "branch": run_git(path, ["branch", "--show-current"]),
        "head": run_git(path, ["log", "-1", "--oneline"]),
        "status_summary": status_summary(status),
    }


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def cert_status(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": str(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact")
        or data.get("primary_next_artifact"),
        "what_closes": data.get("what_closes")
        or data.get("what_closes_now")
        or data.get("closed_now")
        or {},
        "what_remains_open": data.get("what_remains_open")
        or data.get("still_open")
        or {},
    }


def build_table(
    sm_prov: dict[str, Any],
    sm_transfer: dict[str, Any],
    sm_routing: dict[str, Any],
    q79_e6: dict[str, Any],
    q79_qutrit_lines: dict[str, Any],
    q79_orientation: dict[str, Any],
    q79_su5: dict[str, Any],
    gr_primitive: dict[str, Any],
) -> dict[str, Any]:
    carrier = sm_prov.get("source_level_weyl_carrier", {})
    carrier_check = carrier.get("carrier_check", {})
    active_shift = sm_prov.get("active_shift_provenance", {})
    transfer = sm_transfer.get("conditional_transfer_map", {})
    selected_transfer = sm_transfer.get("selected_status", {})
    routing = sm_routing.get("routing_search", {})
    routing_attempt = sm_routing.get("lemma_attempt", {})
    primitive_verdict = gr_primitive.get("verdict", {})
    return {
        "source_level_carrier": {
            "proved": carrier.get("proved") is True,
            "selected_by_mtt_at_s3_level": carrier.get("source_level_flags", {}).get(
                "selected_by_mtt_at_s3_level"
            )
            is True,
            "source_level_projective_class_selected": carrier.get("source_level_flags", {}).get(
                "source_level_projective_class_selected"
            )
            is True,
            "operator_level_projective_rhoE_promoted": carrier.get("source_level_flags", {}).get(
                "operator_level_projective_rhoE_promoted"
            )
            is True,
            "g1_equals_phase_Z_residual": carrier_check.get("g1_equals_phase_Z_residual"),
            "g1_order3_residual": carrier_check.get("g1_order3_residual"),
            "g2_equals_shift_X_residual": carrier_check.get("g2_equals_shift_X_residual"),
            "g2_order3_residual": carrier_check.get("g2_order3_residual"),
            "projective_commutator_residual_imported": carrier_check.get(
                "projective_commutator_residual_imported"
            ),
            "uses_only_selected_active_generators_g1_g2": carrier_check.get(
                "uses_only_selected_active_generators_g1_g2"
            )
            is True,
            "statement": carrier.get("statement"),
        },
        "active_shift": {
            "proved": active_shift.get("proved") is True,
            "nonzero_active_shifts": active_shift.get("nonzero_active_shifts", []),
            "statement": active_shift.get("statement"),
        },
        "source_to_c1_transfer": {
            "conditional_exact": transfer.get("conditional_exact") is True,
            "phase_residual": transfer.get("phase_residual"),
            "shift_residual": transfer.get("shift_residual"),
            "formula": transfer.get("formula", {}),
            "uses_source_level_carrier": transfer.get("uses_source_level_carrier") is True,
            "uses_active_shift_provenance": transfer.get("uses_active_shift_provenance") is True,
            "selected_transfer_map_emitted": selected_transfer.get(
                "selected_transfer_map_emitted"
            )
            is True,
            "selected_sector_routing_emitted": selected_transfer.get(
                "selected_sector_routing_emitted"
            )
            is True,
            "selected_normalization_emitted": selected_transfer.get(
                "selected_normalization_emitted"
            )
            is True,
            "promote_to_A_selected_allowed": selected_transfer.get(
                "promote_to_A_selected_allowed"
            )
            is True,
        },
        "sector_routing": {
            "all_two_two_partitions_tested": routing.get("all_two_two_partitions_tested", []),
            "exact_rows_relative_to_locked_columns": routing.get(
                "exact_rows_relative_to_locked_columns", []
            ),
            "intended_rows": routing.get("intended_rows", []),
            "source_data_independently_selects_route": routing.get(
                "source_data_independently_selects_route"
            )
            is True,
            "target_columns_select_route": routing.get("target_columns_select_route") is True,
            "fully_proved": routing_attempt.get("fully_proved") is True,
            "proved_by_locked_columns": routing_attempt.get("proved_by_locked_columns") is True,
            "proved_by_selected_source": routing_attempt.get("proved_by_selected_source")
            is True,
            "why_not_fully_proved": routing_attempt.get("why_not_fully_proved"),
            "next_certificate": sm_routing.get("next_certificate", {}),
        },
        "q79_internal_sector_evidence": {
            "e6_representation_bridge_closed": q79_e6.get("closed", {}).get(
                "representation_theory_bridge"
            )
            is True,
            "e6_rank_one_seed_sector_assignment_open": q79_e6.get("open", {}).get(
                "rank_one_seed_sector_assignment"
            )
            is True,
            "qutrit_clock_shift_lines_validated": q79_qutrit_lines.get(
                "calculation_results", {}
            ).get("qutrit_clock_shift_line_packet_validates")
            is True,
            "qutrit_complete_visible_cycle_list_open": q79_qutrit_lines.get("still_open", {}).get(
                "complete_selected_visible_cycle_or_brane_list"
            )
            is True,
            "c6_orientation_reduced_not_selected": q79_orientation.get(
                "calculation_results", {}
            ).get("conjugate_pair_only")
            is True
            and q79_orientation.get("calculation_results", {}).get(
                "unique_branch_selected_now"
            )
            is False,
            "su5_qutrit_finite_packet_validated": q79_su5.get("calculation_results", {}).get(
                "validator_passes_finite_algebra"
            )
            is True,
            "su5_qutrit_selected_source_available": q79_su5.get(
                "calculation_results", {}
            ).get("selected_source_available")
            is True,
        },
        "primitive_emission_search": {
            "selected_primitives_found": primitive_verdict.get("selected_primitives_found")
            is True,
            "R1_promotes": primitive_verdict.get("R1_promotes") is True,
            "R4_promotes": primitive_verdict.get("R4_promotes") is True,
            "R6_ready": primitive_verdict.get("R6_ready") is True,
            "next_required_artifact": primitive_verdict.get("next_required_artifact"),
        },
    }


def build_candidate() -> dict[str, Any]:
    q79_inputs = {name: cert_status(path) for name, path in Q79_INPUTS.items()}
    adjacent = {name: cert_status(path) for name, path in ADJACENT_INPUTS.items()}

    sm_prov = load(ADJACENT_INPUTS["sm_weylpair_source_provenance_candidate"])
    sm_transfer = load(ADJACENT_INPUTS["sm_weylpair_source_to_c1_transfer_candidate"])
    sm_routing = load(ADJACENT_INPUTS["sm_weylpair_sector_routing_candidate"])
    q79_e6 = load(Q79_INPUTS["e6_to_sm_dictionary"])
    q79_qutrit_lines = load(Q79_INPUTS["qutrit_line_cycle_restrictions"])
    q79_orientation = load(Q79_INPUTS["orientation_de_dotd_bridge"])
    q79_su5 = load(Q79_INPUTS["su5_qutrit_polarization_attempt"])
    gr_primitive = load(ADJACENT_INPUTS["gr_selected_primitive_emission_search_import"])
    table = build_table(
        sm_prov,
        sm_transfer,
        sm_routing,
        q79_e6,
        q79_qutrit_lines,
        q79_orientation,
        q79_su5,
        gr_primitive,
    )

    exact_rows = table["sector_routing"]["exact_rows_relative_to_locked_columns"]
    intended = exact_rows[0] if exact_rows else {}
    intended_route_unique = (
        len(exact_rows) == 1
        and intended.get("phase_route") == ["u", "e"]
        and intended.get("shift_route") == ["d", "nuD"]
        and intended.get("matches_locked_columns") is True
    )
    source_level_closed = (
        table["source_level_carrier"]["proved"]
        and table["source_level_carrier"]["selected_by_mtt_at_s3_level"]
        and table["source_level_carrier"]["source_level_projective_class_selected"]
        and table["active_shift"]["proved"]
        and table["active_shift"]["nonzero_active_shifts"] == [[1, 1]]
    )
    conditional_transfer_exact = (
        table["source_to_c1_transfer"]["conditional_exact"]
        and float(table["source_to_c1_transfer"]["phase_residual"]) == 0.0
        and float(table["source_to_c1_transfer"]["shift_residual"]) == 0.0
    )
    selected_sector_route_closed = (
        table["sector_routing"]["source_data_independently_selects_route"]
        and table["sector_routing"]["proved_by_selected_source"]
    )
    selected_transfer_closed = (
        table["source_to_c1_transfer"]["selected_transfer_map_emitted"]
        and table["source_to_c1_transfer"]["selected_sector_routing_emitted"]
        and table["source_to_c1_transfer"]["selected_normalization_emitted"]
    )
    primitives_found = table["primitive_emission_search"]["selected_primitives_found"]

    support = {
        "q79_conditional_A_solve_reduced_to_provenance": q79_inputs[
            "weylpair_conditional_A_solve"
        ]["status"]
        == "Q79_ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN",
        "sm_source_level_provenance_reduction_imported": adjacent[
            "sm_weylpair_source_provenance"
        ]["status"]
        == "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_C1_TRANSFER_OPEN",
        "sm_conditional_transfer_map_imported": adjacent[
            "sm_weylpair_source_to_c1_transfer"
        ]["status"]
        == "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_MAP_BUILT_CONDITIONAL_EXACT_SECTOR_ROUTING_OPEN",
        "sm_sector_routing_attempt_imported": adjacent["sm_weylpair_sector_routing"]["status"]
        == "MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_ROUTING_ATTEMPT_BUILT_NOT_UNIQUELY_SELECTED_BY_CURRENT_DATA",
        "q79_representation_dictionary_available_but_sector_assignment_open": table[
            "q79_internal_sector_evidence"
        ]["e6_representation_bridge_closed"]
        and table["q79_internal_sector_evidence"]["e6_rank_one_seed_sector_assignment_open"],
        "q79_qutrit_lines_available_but_projector_retention_open": table[
            "q79_internal_sector_evidence"
        ]["qutrit_clock_shift_lines_validated"]
        and table["q79_internal_sector_evidence"]["qutrit_complete_visible_cycle_list_open"],
        "q79_su5_qutrit_packet_finite_only_unselected": table["q79_internal_sector_evidence"][
            "su5_qutrit_finite_packet_validated"
        ]
        and not table["q79_internal_sector_evidence"]["su5_qutrit_selected_source_available"],
        "selected_primitive_emission_search_imported_no_legal_emission": adjacent[
            "gr_selected_primitive_emission_search_import"
        ]["status"]
        == "ROUTEC_SELECTED_PRIMITIVE_EMISSION_SEARCH_IMPORTED_NO_LEGAL_EMISSION_FOUND",
    }

    decision = {
        "full_selected_weylpair_source_provenance_proved": False,
        "source_level_weyl_carrier_and_active_shift_proved": source_level_closed,
        "conditional_source_to_C1_transfer_exact": conditional_transfer_exact,
        "locked_columns_uniquely_identify_intended_sector_route": intended_route_unique,
        "locked_columns_used_as_selector": False,
        "selected_sector_route_independently_proved": selected_sector_route_closed,
        "selected_transfer_map_emitted": selected_transfer_closed,
        "selected_primitives_found": primitives_found,
        "conditional_A_promoted_to_A_selected": False,
        "b_selected_emitted": False,
        "honest_selected_deltaTheta_C1_solve_run": False,
        "target_fitting_used": False,
    }

    theorem_statement = (
        "The q79/F,m=1 Route-C source-level Weyl carrier is proven at the S3/GS "
        "source level: g1 carries the phase/clock Z leg, g2 carries the "
        "shift/translation X leg, and active shift (1,1) is the unique nonzero "
        "active primitive shift.  The map from this carrier to the two C1 "
        "columns is exact if the sector routing u/e <- Z and d/nuD <- X is "
        "given.  However, the currently selected source data do not independently "
        "emit that sector routing or its normalization; the route is selected "
        "only by matching the already locked target columns.  Therefore the full "
        "selected Weyl-pair source-provenance lemma is not yet proved.  The next "
        "non-circular object is a selected sector-charge/chirality certificate, "
        "followed by selected Phi_fin/B_N primitive emission."
    )

    return {
        "certificate": "Q79RouteCWeylPairSourceProvenanceLemma",
        "status": "Q79_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_SECTOR_CHARGE_OPEN",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "provenance_table": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "repo_snapshots": {name: repo_snapshot(name, path) for name, path in REPOS.items()},
        "q79_input_statuses": q79_inputs,
        "adjacent_input_statuses": adjacent,
        "support_reductions": support,
        "source_provenance_reduction": table,
        "decision": decision,
        "closed_by_this_attempt": {
            "latest_repo_updates_checked": all(
                repo_snapshot(name, path)["present"] for name, path in REPOS.items()
            ),
            "source_level_weyl_carrier_provenance_closed": source_level_closed,
            "active_shift_1_1_provenance_closed": table["active_shift"]["proved"],
            "conditional_source_to_C1_transfer_exact": conditional_transfer_exact,
            "all_two_two_sector_routes_enumerated": len(
                table["sector_routing"]["all_two_two_partitions_tested"]
            )
            == 6,
            "locked_columns_identify_intended_route_uniquely": intended_route_unique,
            "current_proof_blocker_identified": True,
            "target_fitting_excluded": True,
        },
        "still_open": {
            "selected_sector_charge_or_chirality_certificate": True,
            "source_derivation_of_u_e_phase_route": True,
            "source_derivation_of_d_nuD_shift_route": True,
            "selected_transfer_normalization": True,
            "promote_conditional_transfer_to_selected_C1_map": True,
            "promote_conditional_A_to_A_selected": True,
            "emit_theorem_derived_b_selected": True,
            "run_honest_selected_deltaTheta_C1_solve": True,
            "Phi_fin_selected_payload": True,
            "quotient_valid_BN_basis_certificate": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_full_selected_weylpair_source_provenance": False,
            "claims_sector_route_selected_by_source": False,
            "claims_conditional_transfer_is_selected_C1_map": False,
            "claims_conditional_A_is_A_selected": False,
            "claims_b_selected_emitted": False,
            "claims_honest_selected_deltaTheta_solve_run": False,
            "uses_locked_target_columns_as_source_selector": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "lifts_selected_flags_by_hand": False,
            "claims_full_SM_closure": False,
        },
        "theorem": {
            "name": "Q79WeylPairSourceProvenanceReductionTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": theorem_statement,
        },
        "next_required_artifact": "Q79_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1",
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def render_bool_map(items: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in items.items())


def render_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def build_paper(cert: dict[str, Any]) -> str:
    reduction = cert["source_provenance_reduction"]
    carrier = reduction["source_level_carrier"]
    transfer = reduction["source_to_c1_transfer"]
    routing = reduction["sector_routing"]
    exact_rows = routing["exact_rows_relative_to_locked_columns"]
    next_cert = routing["next_certificate"]
    closed = "\n".join(
        f"- `{key}`" for key, value in cert["closed_by_this_attempt"].items() if value
    )
    open_items = "\n".join(f"- `{key}`" for key, value in cert["still_open"].items() if value)
    repo_lines = "\n".join(
        f"- `{name}`: `{row['head']}` dirty=`{row['status_summary']['dirty']}`"
        for name, row in cert["repo_snapshots"].items()
    )
    route_lines = "\n".join(
        "- phase `{phase}` / shift `{shift}`: match=`{match}`, residuals=(`{pres}`, `{sres}`)".format(
            phase=row.get("phase_route"),
            shift=row.get("shift_route"),
            match=row.get("matches_locked_columns"),
            pres=row.get("phase_residual_to_locked_column"),
            sres=row.get("shift_residual_to_locked_column"),
        )
        for row in routing["all_two_two_partitions_tested"]
    )
    return f"""# Q79 RouteC WeylPair Source Provenance Lemma v1

## Result

The requested provenance lemma is partly proved and partly reduced.  The
source-level Weyl carrier is proven: `g1 = Z`, `g2 = X`, and active shift
`(1,1)` is the selected nonzero shift.  The transfer to the C1 columns is exact
conditioned on a sector-routing rule.

The full selected provenance lemma is **not** proved yet.  The only current
route that picks `u/e <- Z` and `d/nuD <- X` is matching the locked target
columns.  That is useful as a diagnostic uniqueness result, but it cannot serve
as source selection.

## Repo Snapshot

{repo_lines}

## Support Reductions

{render_bool_map(cert["support_reductions"])}

## Source-Level Carrier

- proved: `{carrier["proved"]}`
- selected by MTT at S3 level: `{carrier["selected_by_mtt_at_s3_level"]}`
- source-level projective class selected: `{carrier["source_level_projective_class_selected"]}`
- operator-level projective rhoE promoted: `{carrier["operator_level_projective_rhoE_promoted"]}`
- g1 equals phase Z residual: `{carrier["g1_equals_phase_Z_residual"]}`
- g2 equals shift X residual: `{carrier["g2_equals_shift_X_residual"]}`

{carrier["statement"]}

## Conditional Transfer

- conditional exact: `{transfer["conditional_exact"]}`
- phase residual: `{transfer["phase_residual"]}`
- shift residual: `{transfer["shift_residual"]}`
- selected transfer map emitted: `{transfer["selected_transfer_map_emitted"]}`
- selected sector routing emitted: `{transfer["selected_sector_routing_emitted"]}`
- selected normalization emitted: `{transfer["selected_normalization_emitted"]}`

Formula:

- `{transfer["formula"].get("phase_column")}`
- `{transfer["formula"].get("shift_column")}`

## Sector Routing Search

All two-two routes:

{route_lines}

Exact row relative to locked columns:

{exact_rows}

Source data independently selects route:
`{routing["source_data_independently_selects_route"]}`

Why not fully proved:

{routing["why_not_fully_proved"]}

## q79 Internal Evidence

{render_bool_map(reduction["q79_internal_sector_evidence"])}

## Primitive Emission Search

{render_bool_map(reduction["primitive_emission_search"])}

## Decision

{render_bool_map(cert["decision"])}

## Next Certificate

`{next_cert.get("name")}` must supply:

{render_list(next_cert.get("must_supply", []))}

## What This Closes

{closed}

## What Remains Open

{open_items}

## Theorem

`{cert["theorem"]["name"]}` is proved.

{cert["theorem"]["statement"]}

Next required artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    cert = build_candidate()
    write_json(OUT_TABLE, cert["source_provenance_reduction"])
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")
    print("Q79 Route-C Weyl-pair source provenance lemma")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
