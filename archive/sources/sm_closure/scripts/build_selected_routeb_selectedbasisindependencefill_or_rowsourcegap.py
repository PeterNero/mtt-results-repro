"""Promote Route B selected basis independence and isolate final row-source gap."""

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

SLUG = "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BASIS_FILL = PACKET_DIR / "route_b_selected_basis_independence_fill.packet.json"
VALIDATION = PACKET_DIR / "strict_validator_result.packet.json"
ROW_GAP = PACKET_DIR / "row_source_independence_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_RouteBSelectedBasisIndependenceFill_or_RowSourceGap_v1.md"

PREVIOUS = DATA / "selected_routeb_quadratureindependencefill_or_selectedbasisgap.candidate.json"
QUAD_FILL = (
    DATA
    / "selected_routeb_quadratureindependencefill_or_selectedbasisgap"
    / "route_b_quadrature_independence_fill.packet.json"
)
FINITE_PROJECTOR = DATA / "selected_finite_projector_source_promotion.candidate.json"
TRANSPORT = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
HYM_VALUES = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"

STATUS = "MTT_SELECTED_ROUTEB_SELECTEDBASISINDEPENDENCEFILL_BUILT_ROW_SOURCE_GAP_OPEN"
NEXT = "MTT_Selected_RouteBRowSourceIndependenceProof_or_RouteAPhysicalSourceFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def promoted_basis_summary(projector: dict[str, Any]) -> dict[str, Any]:
    slots = projector["promoted_sector_slots"]
    return {
        sector: {
            "rank": slot["rank"],
            "selected_basis_labels": slot["selected_basis_labels"],
            "selected_projector_formula": slot["selected_projector_formula"],
            "source_verified_by_transport_conjugation": slot[
                "source_verified_by_transport_conjugation"
            ],
            "finite_raw_truncation_replay_used": slot["finite_raw_truncation_replay_used"],
        }
        for sector, slot in slots.items()
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    quad_fill = load(QUAD_FILL)
    finite_projector = load(FINITE_PROJECTOR)
    transport = load(TRANSPORT)
    hym_values = load(HYM_VALUES)

    all_slots_source_verified = all(
        slot["source_verified_by_transport_conjugation"] is True
        for slot in finite_projector["promoted_sector_slots"].values()
    )
    all_raw_not_used = all(
        slot["finite_raw_truncation_replay_used"] is False
        for slot in finite_projector["promoted_sector_slots"].values()
    )
    all_model_values_unpromoted_before_transport = all(
        slot["selected_source_verified"] is False
        and slot["value_emitted_as_selected_HYM_projector"] is False
        for slot in hym_values["finite_value_payload"]["sector_slots"].values()
    )

    route_b = dict(quad_fill["route_B_independent_execution"])
    route_b.update(
        {
            "schema": "MTTRouteBSelectedBasisIndependenceFill.v1",
            "status": "SELECTED_BASIS_INDEPENDENCE_FILLED_ROW_SOURCE_INDEPENDENCE_OPEN",
            "selected_basis_independent_of_residual_projector": True,
            "source_independent_of_residual_projector_replay": False,
            "selected_basis_independence_certificate": {
                "source": rel(FINITE_PROJECTOR),
                "transport_source": rel(TRANSPORT),
                "basis_summary": promoted_basis_summary(finite_projector),
                "all_sector_sources_verified_by_transport_conjugation": all_slots_source_verified,
                "finite_raw_truncation_replay_used": not all_raw_not_used,
                "model_values_unpromoted_before_transport": all_model_values_unpromoted_before_transport,
                "uses_residual_projector_replay": False,
                "uses_locked_C1_target_values": False,
                "uses_observed_constants": False,
            },
        }
    )
    route_b["attached_independent_provenance_sources"] = list(
        route_b["attached_independent_provenance_sources"]
    ) + [
        {
            "source": rel(FINITE_PROJECTOR),
            "closes": "selected basis/projector independence from residual-projector replay",
            "independence_level": "stationary selected source verified by symbolic transport conjugation",
            "promotes_independence": True,
        },
        {
            "source": rel(TRANSPORT),
            "closes": "transport-conjugation proof for selected stationary projectors/Riesz/Green",
            "independence_level": "symbolic source replay, not locked C1 target replay",
            "promotes_independence": True,
        },
    ]

    attempt = dict(quad_fill)
    attempt["status"] = "ROUTE_B_SELECTED_BASIS_FILL_FAILS_STRICT_VALIDATOR_ON_ROW_SOURCE_ONLY"
    attempt["route_B_independent_execution"] = route_b
    attempt["promotion_allowed_now"] = False
    write_json(BASIS_FILL, attempt)
    validation = run_validator(BASIS_FILL)

    row_gap = {
        "schema": "MTTRouteBRowSourceIndependenceGap.v1",
        "status": "VALUES_QUADRATURE_BASIS_CLOSED_ROW_SOURCE_INDEPENDENCE_OPEN",
        "closed_now": {
            "all_72_primitive_rows_executed": route_b["all_72_primitive_rows_executed"],
            "formal_110_rows_executed": route_b["formal_110_rows_executed"],
            "exactness_or_error_certificates_attached": route_b[
                "exactness_or_error_certificates_attached"
            ],
            "quadrature_rule_independent_of_locked_target": route_b[
                "quadrature_rule_independent_of_locked_target"
            ],
            "selected_basis_independent_of_residual_projector": route_b[
                "selected_basis_independent_of_residual_projector"
            ],
        },
        "not_closed": {
            "source_independent_of_residual_projector_replay": True,
        },
        "why_row_source_not_closed": [
            "The stationary selected basis/projector source is verified, but the dynamic C1 primitive rows still inherit the Weyl/residual-row lineage.",
            "The validator needs a proof that the 72 primitive rows, 36 sector rows, and 2 Hessian/source rows are evaluated from the transported selected basis and finite Weyl trace rule rather than from residual-projector replay.",
            "No physical Phi_fin^C1 action-source theorem or independent dynamic Galerkin row-source theorem is emitted in this step.",
        ],
        "minimal_next_source_object": {
            "name": "RouteBRowSourceIndependenceProof",
            "must_prove": [
                "the selected transported bases K_s feed the 72 primitive C1 row kernels",
                "the 36 sector rows and 2 Hessian/source rows are assembled from those row kernels and the finite Weyl trace rule",
                "no residual-projector replay or locked target values are used to select the row source",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRouteBSelectedBasisIndependenceFillOrRowSourceGap",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "quadrature_fill": rel(QUAD_FILL),
            "finite_projector_source_promotion": rel(FINITE_PROJECTOR),
            "transport_conjugation_validator": rel(TRANSPORT),
            "hym_projector_model_values": rel(HYM_VALUES),
        },
        "output_packets": {
            "route_b_selected_basis_independence_fill": rel(BASIS_FILL),
            "strict_validator_result": rel(VALIDATION),
            "row_source_independence_gap": rel(ROW_GAP),
        },
        "what_closes_now": {
            "route_B_selected_basis_independent_of_residual_projector": True,
            "stationary_selected_projector_basis_source_imported": True,
            "strict_validator_rejection_reduced_to_row_source_independence": True,
        },
        "what_remains_open": {
            "source_independent_of_residual_projector_replay": True,
            "Route_A_physical_source_fill": True,
            "unpatched_dynamic_C1_packet_closure": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "strict_validation": validation,
        "theorem": {
            "name": "TransportedSelectedBasisIndependencePromotionTheorem",
            "proved": True,
            "statement": (
                "The finite projector source-promotion and symbolic transport-conjugation artifacts "
                "emit selected stationary projectors and ordered bases independently of residual-projector "
                "replay and locked C1 target values. Therefore Route B's selected-basis independence "
                "clause may be filled. This does not yet prove that the dynamic 110-row C1 packet is "
                "sourced from those bases."
            ),
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_gate_status": previous["status"],
    }

    cert = {
        "certificate": "MTT_Selected_RouteBSelectedBasisIndependenceFill_or_RowSourceGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "strict_validator_exit_code": validation["exit_code"],
        "strict_validator_still_rejects": validation["exit_code"] == 1,
        "selected_basis_independence_closed": True,
        "source_independence_closed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected RouteBSelectedBasisIndependenceFill or RowSourceGap v1

Status: `{STATUS}`

This step fills the Route B selected-basis independence clause.

The selected stationary projectors and ordered bases are imported from the
finite projector source-promotion chain: model-active B_N values are not copied;
they are promoted only after symbolic transport conjugation
`P_s^sel = U P_s^model U^-1`.

The strict validator still rejects the packet on one remaining Route B field:
`source_independent_of_residual_projector_replay`. The row values, finite trace
quadrature, and selected basis are ready, but we still need the theorem that the
dynamic 110-row C1 packet is evaluated from that selected basis rather than
inherited from residual-projector replay.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "{SLUG}"
BASIS_FILL = PACKET_DIR / "route_b_selected_basis_independence_fill.packet.json"
ROW_GAP = PACKET_DIR / "row_source_independence_gap.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBSelectedBasisIndependenceFill_or_RowSourceGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    fill = load(BASIS_FILL)
    gap = load(ROW_GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    route_b = fill["route_B_independent_execution"]
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(BASIS_FILL)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(route_b["selected_basis_independent_of_residual_projector"] is True, "basis not closed")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "source overclosed")
    cert_packet = route_b["selected_basis_independence_certificate"]
    require(cert_packet["uses_residual_projector_replay"] is False, "basis uses residual replay")
    require(cert_packet["uses_locked_C1_target_values"] is False, "basis uses locked target")
    require(cert_packet["all_sector_sources_verified_by_transport_conjugation"] is True, "transport sources not verified")
    require(gap["closed_now"]["selected_basis_independent_of_residual_projector"] is True, "gap basis mismatch")
    require(gap["not_closed"]["source_independent_of_residual_projector_replay"] is True, "gap source mismatch")
    require(proc.returncode == 1, "strict validator should still reject")
    require(any("Route B missing: source_independent_of_residual_projector_replay" in line for line in proc.stderr.splitlines()), "unexpected Route B rejection")
    require(cert["selected_basis_independence_closed"] is True, "cert basis missing")
    require(cert["source_independence_closed"] is False, "cert source overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("strict validator still rejects" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(BASIS_FILL, attempt)
    write_json(VALIDATION, validation)
    write_json(ROW_GAP, row_gap)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"wrote {rel(OUTPUT)}")
    print(f"status {STATUS}")
    print(f"validator_basis_fill_exit {validation['exit_code']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
