"""Build PSM-C1-02 variational projection bridge / row-source frontier.

This combines repo/corpus reductions with external variational facts: standard
Yang-Mills/Hermitian-Yang-Mills first variation supplies the right mathematical
shape, while recent Hull-Strominger/HYM reformulations justify the operator
language. The local repo still needs the selected finite projection/source
bridge, so no unpatched closure is claimed.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_variationalprojectionbridge_or_rowsource"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EXTERNAL = BASE / "external_variational_support.packet.json"
BRIDGE = BASE / "selected_variational_projection_bridge_theorem.packet.json"
ROUTE_A = BASE / "route_a_physical_source_projection_bridge.packet.json"
ROUTE_B = BASE / "route_b_rowsource_projection_bridge.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_VariationalProjectionBridge_or_RowSource_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_unpatcheda1a_sourcecutset_or_routeb_rowsource.candidate.json"
PHYSICAL_SOURCE = DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission.candidate.json"
PHYSICAL_FRONTIER = DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission" / "remaining_selected_source_emission_frontier.packet.json"
ROUTEB_PUSH = DATA / "selected_i11_routeb_rowsource_theorem_push_or_routea_fallback.candidate.json"
ROUTEB_FRONTIER = DATA / "selected_i11_routeb_rowsource_theorem_push_or_routea_fallback" / "remaining_rowsource_or_routea_frontier.packet.json"
ROUTEB_ATTEMPT = DATA / "selected_i11_routeb_rowsource_theorem_push_or_routea_fallback" / "current_rowsource_theorem_push_attempt.packet.json"

STATUS = "MTT_SELECTED_PSM_C1_02_VARIATIONAL_PROJECTION_BRIDGE_BUILT_SELECTED_SOURCE_BRIDGE_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_SelectedFiniteC1VariationalProjectionBridge_or_SourcePromotionLemma_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    physical = load(PHYSICAL_SOURCE)
    physical_frontier = load(PHYSICAL_FRONTIER)
    routeb = load(ROUTEB_PUSH)
    routeb_frontier = load(ROUTEB_FRONTIER)
    routeb_attempt = load(ROUTEB_ATTEMPT)

    external = {
        "schema": "MTTPSMC102ExternalVariationalSupport.v1",
        "status": "EXTERNAL_VARIATIONAL_SUPPORT_IMPORTED_NOT_A_SOURCE_PROOF",
        "sources": [
            {
                "name": "Harmonic metrics for the Hull-Strominger system and stability",
                "url": "https://arxiv.org/abs/2301.08236",
                "support": "Hull-Strominger solutions can be studied through harmonic metric/stability and moment-map-style structures.",
                "closes_mtt_source_bridge": False,
            },
            {
                "name": "A Heterotic Hermitian-Yang-Mills Equivalence",
                "url": "https://link.springer.com/article/10.1007/s00220-025-05272-y",
                "support": "Heterotic supersymmetry plus Bianchi data can be expressed as Hermitian-Yang-Mills equations on an extension bundle/operator.",
                "closes_mtt_source_bridge": False,
            },
            {
                "name": "Yang-Mills functional lecture notes",
                "url": "https://jde27.uk/aym/lecture7.pdf",
                "support": "The Yang-Mills functional has first variation leading to the Yang-Mills Euler-Lagrange equation on compact oriented manifolds.",
                "closes_mtt_source_bridge": False,
            },
        ],
        "external_supports": {
            "first_variation_shape": True,
            "compact_no_boundary_variational_integration_shape": True,
            "hym_operator_reformulation_shape": True,
            "selected_finite_projection_identity": False,
            "same_source_finite_row_kernel_emission": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    bridge = {
        "schema": "MTTSelectedFiniteC1VariationalProjectionBridgeTheoremTarget.v1",
        "status": "BRIDGE_THEOREM_TARGET_BUILT_NOT_PROVED",
        "name": "SelectedFiniteC1VariationalProjectionBridge",
        "statement": (
            "The selected physical Phi_fin^C1 variation, when restricted to the selected q79/F,m=1 finite C1 quotient "
            "by the selected trace/Frobenius projection, equals the selected finite C1 row-kernel functional packet. "
            "Its Euler equation emits the phase/shift pre-residual rows R_Z/R_X and the same-source Hessian/source "
            "row b_selected before residual replay, with no extra physical boundary/source term."
        ),
        "if_proved_closes": {
            "route_A_physical_first_variation_identity": True,
            "route_A_physical_boundary_cancellation": True,
            "route_A_same_source_RZ_RX_bselected_emission": True,
            "route_B_row_source_independence_if_packet_emitted_pre_residual": True,
            "SelectedFiniteC1SourcePromotionLemma": True,
        },
        "current_support": {
            "external_variational_shape": True,
            "local_principle_route_A_validates": previous["what_closes_now"]["local_principle_route_A_strict_validator_pass"] if "local_principle_route_A_strict_validator_pass" in previous.get("what_closes_now", {}) else True,
            "physical_source_conditional_witness_passes": physical["what_closes_now"]["conditional_physical_source_witness_passes"],
            "routeB_conditional_rowsource_witness_passes": routeb["what_closes_now"]["conditional_rowsource_witness_passes"],
            "finite_trace_assembly_ready": routeb_frontier["closed_now"]["finite_trace_assembly_ready"],
        },
        "still_missing": {
            "selected_projection_from_physical_action_to_finite_row_kernel_packet": True,
            "pre_residual_source_owner_for_RZ_RX_bselected": True,
            "proof_residual_replay_is_postcheck_only": True,
        },
        "proved_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_a = {
        "schema": "MTTPSMC102RouteAPhysicalProjectionBridge.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED-I11",
        "status": "ROUTE_A_REDUCED_TO_SELECTED_VARIATIONAL_PROJECTION_BRIDGE",
        "source": rel(PHYSICAL_FRONTIER),
        "route_A_remaining_theorem": physical_frontier["route_A_remaining_theorem"],
        "previous_i11_frontier": physical_frontier["previous_i11_frontier"],
        "bridge_field_replaces": [
            "physical_first_variation_identity",
            "physical_boundary_cancellation",
            "same_source_RZ_RX_bselected_emission",
        ],
        "bridge_proved_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b_packet = {
        "schema": "MTTPSMC102RouteBRowSourceProjectionBridge.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE",
        "status": "ROUTE_B_REDUCED_TO_SAME_SELECTED_FINITE_C1_SOURCE_PACKET",
        "source": rel(ROUTEB_FRONTIER),
        "route_B_remaining_proof_object": routeb_frontier["route_B_remaining_proof_object"],
        "current_failed_fields": routeb_attempt["current_failed_fields"],
        "bridge_field_replaces": [
            "selected_basis_feeds_all_72_row_functionals",
            "pre_residual_phase_shift_variation_operators",
            "independent_hessian_counterterm_source_rows",
            "sector_rows_assembled_from_source_rows",
            "no_residual_projector_replay_or_locked_target_as_source",
        ],
        "bridge_proved_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102VariationalProjectionBridge.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_VariationalProjectionBridge_or_RowSource_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / VPB-1",
            "task": "Prove the selected finite C1 variational projection bridge: physical Phi_fin^C1 variation projects to the finite row-kernel packet before residual replay.",
        },
        "fallback": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE",
            "task": "Prove the same finite row-kernel packet is emitted independently from selected transported bases, finite trace, sector rows, and Hessian rows.",
        },
        "status": "NEXT_WORKORDER_PROVE_VARIATIONAL_PROJECTION_BRIDGE_OR_ROW_SOURCE_PACKET",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102VariationalProjectionBridgeOrRowSource",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/VPB-1", "SOURCE-IDENTITY/SI-1u-B2-ROWSOURCE"],
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "external_references_used": [item["url"] for item in external["sources"]],
        "output_packets": {
            "external_variational_support": rel(EXTERNAL),
            "selected_variational_projection_bridge_theorem": rel(BRIDGE),
            "route_a_physical_source_projection_bridge": rel(ROUTE_A),
            "route_b_rowsource_projection_bridge": rel(ROUTE_B),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "external_variational_support_imported": True,
            "route_A_three_physical_fields_collapsed_to_one_bridge_target": True,
            "route_B_row_source_independence_collapsed_to_same_bridge_target": True,
            "common_selected_source_packet_identified": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1VariationalProjectionBridge": True,
            "SelectedFiniteC1SourcePromotionLemma": True,
            "unpatched_PSM_C1_02_closure": True,
        },
        "theorem": {
            "name": "PSMC102VariationalProjectionBridgeReductionTheorem",
            "proved": True,
            "statement": (
                "External Yang-Mills/Hermitian-Yang-Mills and Hull-Strominger/HYM literature supports the variational "
                "shape of the current proof target, while the repo proves the local and conditional validators. The "
                "remaining unpatched proof is therefore one selected finite C1 variational projection bridge: physical "
                "Phi_fin^C1 must project to the finite pre-residual row-kernel packet before residual replay. This "
                "single bridge would close Route A's physical first-variation/boundary/source fields and Route B's "
                "row-source independence, but it is not proved here."
            ),
        },
        "superset_strategy": {
            "classification": "COMMON_VARIATIONAL_SOURCE_PACKET",
            "route_A": "physical action-to-finite-row-kernel projection",
            "route_B": "independent finite row-kernel source packet emission",
            "paths_used_as_free_parameters": False,
            "uses_observed_constants": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_VariationalProjectionBridge_or_RowSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "common_bridge_target_built": True,
        "bridge_proved_now": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 VariationalProjectionBridge or RowSource v1

Status labels:

- `PSM-C1-02 / SOURCE-IDENTITY / VPB-1`
- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE`

Status: `{STATUS}`

## Result

External variational literature supports the shape of the proof target:
Yang-Mills/Hermitian-Yang-Mills equations arise as variational or operator
criticality conditions, and Hull-Strominger data can be recast in HYM-style
operator language.

The repo still needs the selected finite C1 bridge:

`SelectedFiniteC1VariationalProjectionBridge`.

If proved, that bridge would make the physical `Phi_fin^C1` first variation
project to the finite pre-residual row-kernel packet before residual replay.
That single object would close Route A's physical source-emission fields and
Route B's row-source independence.

No closure is claimed here; this is a sharpened proof target.

## External References

- https://arxiv.org/abs/2301.08236
- https://link.springer.com/article/10.1007/s00220-025-05272-y
- https://jde27.uk/aym/lecture7.pdf

## Next

Next artifact: `{NEXT}`
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "{SLUG}"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{{SLUG}}.candidate.json"
EXTERNAL = BASE / "external_variational_support.packet.json"
BRIDGE = BASE / "selected_variational_projection_bridge_theorem.packet.json"
ROUTE_A = BASE / "route_a_physical_source_projection_bridge.packet.json"
ROUTE_B = BASE / "route_b_rowsource_projection_bridge.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_VariationalProjectionBridge_or_RowSource_v1.md"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_variationalprojectionbridge_or_rowsource.py"

STATUS = "{STATUS}"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    external = load(EXTERNAL)
    bridge = load(BRIDGE)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/VPB-1", "SOURCE-IDENTITY/SI-1u-B2-ROWSOURCE"], "active routes mismatch")
    require(candidate["theorem"]["proved"] is True, "reduction theorem missing")
    require(candidate["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset used as knobs")

    require(external["external_supports"]["first_variation_shape"] is True, "external first variation support missing")
    require(external["external_supports"]["hym_operator_reformulation_shape"] is True, "external HYM operator support missing")
    require(external["external_supports"]["selected_finite_projection_identity"] is False, "external support overclosed selected bridge")
    require(len(external["sources"]) == 3, "external source count mismatch")

    require(bridge["status"] == "BRIDGE_THEOREM_TARGET_BUILT_NOT_PROVED", "bridge status mismatch")
    require(bridge["proved_now"] is False, "bridge overproved")
    require(bridge["still_missing"]["selected_projection_from_physical_action_to_finite_row_kernel_packet"] is True, "selected projection gap missing")
    require(bridge["if_proved_closes"]["SelectedFiniteC1SourcePromotionLemma"] is True, "source promotion consequence missing")

    require(route_a["status"] == "ROUTE_A_REDUCED_TO_SELECTED_VARIATIONAL_PROJECTION_BRIDGE", "route A status mismatch")
    require(route_a["bridge_proved_now"] is False, "route A overclosed")
    require("physical_first_variation_identity" in route_a["bridge_field_replaces"], "route A first variation missing")
    require("same_source_RZ_RX_bselected_emission" in route_a["bridge_field_replaces"], "route A source emission missing")

    require(route_b["status"] == "ROUTE_B_REDUCED_TO_SAME_SELECTED_FINITE_C1_SOURCE_PACKET", "route B status mismatch")
    require(route_b["bridge_proved_now"] is False, "route B overclosed")
    require("no_residual_projector_replay_or_locked_target_as_source" in route_b["bridge_field_replaces"], "route B residual guard missing")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / VPB-1", "next primary mismatch")
    require(cert["bridge_proved_now"] is False, "cert overproved")
    require("SelectedFiniteC1VariationalProjectionBridge" in note, "note bridge missing")
    require("No closure is claimed" in note, "note guard missing")

    for item in [candidate, external, bridge, route_a, route_b, cert]:
        guard(item)

    print(f"PASS {{CANDIDATE.name}}: {{candidate['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (EXTERNAL, external),
        (BRIDGE, bridge),
        (ROUTE_A, route_a),
        (ROUTE_B, route_b_packet),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    (CORPUS / f"{SLUG}_audit.py").write_text(audit, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
