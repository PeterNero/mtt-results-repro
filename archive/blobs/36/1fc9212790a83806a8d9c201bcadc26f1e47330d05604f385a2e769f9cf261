"""Promote Route B quadrature independence while keeping selected basis/source gaps open."""

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

SLUG = "selected_routeb_quadratureindependencefill_or_selectedbasisgap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
QUAD = PACKET_DIR / "route_b_quadrature_independence_fill.packet.json"
VALIDATION = PACKET_DIR / "strict_validator_result.packet.json"
GAP = PACKET_DIR / "selected_basis_source_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_RouteBQuadratureIndependenceFill_or_SelectedBasisGap_v1.md"

PREVIOUS = DATA / "selected_routeb_partialindependentprovenancefill_or_basisquadraturegap.candidate.json"
PARTIAL = (
    DATA
    / "selected_routeb_partialindependentprovenancefill_or_basisquadraturegap"
    / "route_b_partial_independent_provenance_fill.packet.json"
)
FINITE_WEYL = (
    DATA
    / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
    / "finite_weyl_trace_uniqueness_derivation.packet.json"
)
FINITE_WEYL_CANDIDATE = DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation.candidate.json"
ZERO_MODE_THEOREM = DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"
ZERO_MODE_SUPPORT = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "inputs"
    / "zero_mode_basis.packet.json"
)
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"

STATUS = "MTT_SELECTED_ROUTEB_QUADRATUREINDEPENDENCEFILL_BUILT_SELECTED_BASIS_SOURCE_GAP_OPEN"
NEXT = "MTT_Selected_RouteBSelectedBasisSourceEmission_or_RouteAPhysicalSourceFill_v1"


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


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    partial = load(PARTIAL)
    finite_weyl = load(FINITE_WEYL)
    finite_weyl_candidate = load(FINITE_WEYL_CANDIDATE)
    zero_mode_theorem = load(ZERO_MODE_THEOREM)
    zero_mode_support = load(ZERO_MODE_SUPPORT)

    route_b = dict(partial["route_B_independent_execution"])
    route_b.update(
        {
            "schema": "MTTRouteBQuadratureIndependenceFill.v1",
            "status": "QUADRATURE_INDEPENDENCE_FILLED_SELECTED_BASIS_SOURCE_OPEN",
            "quadrature_rule_independent_of_locked_target": True,
            "selected_basis_independent_of_residual_projector": False,
            "source_independent_of_residual_projector_replay": False,
            "quadrature_independence_certificate": {
                "source": rel(FINITE_WEYL),
                "theorem": "FiniteWeylTraceUniquenessDerivationTheorem",
                "reason": (
                    "The normalized trace/Frobenius rule is forced by selected qutrit Weyl "
                    "irreducibility and Weyl-conjugation invariance, before any locked C1 target "
                    "row value is used."
                ),
                "uses_locked_target_values": False,
                "uses_observed_constants": False,
            },
        }
    )
    route_b["attached_independent_provenance_sources"] = list(
        route_b["attached_independent_provenance_sources"]
    ) + [
        {
            "source": rel(FINITE_WEYL),
            "closes": "quadrature rule independent of locked target values",
            "independence_level": "selected finite Weyl trace uniqueness",
            "promotes_independence": True,
        }
    ]

    attempt = dict(partial)
    attempt["status"] = "ROUTE_B_QUADRATURE_INDEPENDENCE_FILL_FAILS_STRICT_VALIDATOR_ON_BASIS_SOURCE_ONLY"
    attempt["route_B_independent_execution"] = route_b
    attempt["promotion_allowed_now"] = False
    write_json(QUAD, attempt)

    validation = run_validator(QUAD)

    source_gap = {
        "schema": "MTTRouteBSelectedBasisSourceGap.v1",
        "status": "QUADRATURE_CLOSED_SELECTED_BASIS_SOURCE_OPEN",
        "closed_now": {
            "quadrature_rule_independent_of_locked_target": True,
            "finite_Weyl_trace_measure_derived": finite_weyl_candidate["what_closes_now"][
                "finite_Weyl_invariant_trace_measure_derived"
            ],
            "all_72_primitive_rows_executed": route_b["all_72_primitive_rows_executed"],
            "formal_110_rows_executed": route_b["formal_110_rows_executed"],
            "exactness_or_error_certificates_attached": route_b[
                "exactness_or_error_certificates_attached"
            ],
        },
        "not_closed": {
            "selected_basis_independent_of_residual_projector": True,
            "source_independent_of_residual_projector_replay": True,
        },
        "why_selected_basis_not_closed": [
            zero_mode_support["why_not_honest_selected_yet"],
            "The HYM projector bridge theorem identifies sufficient conditions, but its selected_values_emitted flag is false.",
            "A canonical qutrit coordinate basis is not the same as a same-source selected HYM/Galerkin zero-mode basis K_s.",
        ],
        "next_source_object": {
            "name": "SelectedRouteBSelectedBasisSourceEmission",
            "must_emit": [
                "same-source selected projectors P_s or equivalent selected finite Galerkin basis source",
                "ordered bases K_s with Gram/trace convention before residual target replay",
                "proof that all 110 row evaluations use this selected basis and the already-derived finite Weyl trace rule",
            ],
        },
        "zero_mode_bridge_status": zero_mode_theorem["status"],
        "zero_mode_bridge_selected_values_emitted": zero_mode_theorem["theorem"][
            "selected_values_emitted"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRouteBQuadratureIndependenceFillOrSelectedBasisGap",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "partial_route_b_fill": rel(PARTIAL),
            "finite_weyl_trace_uniqueness": rel(FINITE_WEYL),
            "finite_weyl_candidate": rel(FINITE_WEYL_CANDIDATE),
            "zero_mode_hym_bridge": rel(ZERO_MODE_THEOREM),
            "zero_mode_support_basis": rel(ZERO_MODE_SUPPORT),
        },
        "output_packets": {
            "route_b_quadrature_independence_fill": rel(QUAD),
            "strict_validator_result": rel(VALIDATION),
            "selected_basis_source_gap": rel(GAP),
        },
        "what_closes_now": {
            "route_B_quadrature_rule_independent_of_locked_target": True,
            "finite_Weyl_trace_rule_promoted_as_independent_quadrature": True,
            "strict_validator_rejection_reduced_to_basis_and_source_independence": True,
        },
        "what_remains_open": {
            "selected_basis_independent_of_residual_projector": True,
            "source_independent_of_residual_projector_replay": True,
            "Route_A_physical_source_fill": True,
            "unpatched_dynamic_C1_packet_closure": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "strict_validation": validation,
        "theorem": {
            "name": "FiniteWeylQuadratureIndependencePromotionTheorem",
            "proved": True,
            "statement": (
                "The finite qutrit Weyl trace/Frobenius quadrature rule is selected by "
                "irreducibility and Weyl-conjugation invariance, not by the locked C1 target "
                "values. Therefore the Route B quadrature-independence clause may be filled, "
                "while selected basis/source independence remains open."
            ),
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_gate_status": previous["status"],
    }

    cert = {
        "certificate": "MTT_Selected_RouteBQuadratureIndependenceFill_or_SelectedBasisGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "strict_validator_exit_code": validation["exit_code"],
        "strict_validator_still_rejects": validation["exit_code"] == 1,
        "quadrature_independence_closed": True,
        "selected_basis_independence_closed": False,
        "source_independence_closed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected RouteBQuadratureIndependenceFill or SelectedBasisGap v1

Status: `{STATUS}`

This step fills one more strict Route B clause.

The finite qutrit Weyl trace/Frobenius quadrature rule is selected by Weyl
irreducibility and conjugation invariance, so it is independent of the locked C1
target values. This closes the quadrature-independence clause.

The strict validator still rejects the packet because the selected basis/source
side is not yet emitted. The canonical qutrit coordinate basis is support, but
not a same-source selected HYM/Galerkin zero-mode basis `K_s`.

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
QUAD = PACKET_DIR / "route_b_quadrature_independence_fill.packet.json"
GAP = PACKET_DIR / "selected_basis_source_gap.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBQuadratureIndependenceFill_or_SelectedBasisGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    quad = load(QUAD)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    route_b = quad["route_B_independent_execution"]
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(QUAD)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(route_b["quadrature_rule_independent_of_locked_target"] is True, "quadrature not closed")
    require(route_b["selected_basis_independent_of_residual_projector"] is False, "basis overclosed")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "source overclosed")
    require(route_b["quadrature_independence_certificate"]["uses_locked_target_values"] is False, "target values used")
    require(gap["closed_now"]["quadrature_rule_independent_of_locked_target"] is True, "gap packet mismatch")
    require(gap["zero_mode_bridge_selected_values_emitted"] is False, "zero-mode bridge overemitted")
    require(proc.returncode == 1, "strict validator should still reject")
    require(any("Route B missing: selected_basis_independent_of_residual_projector, source_independent_of_residual_projector_replay" in line for line in proc.stderr.splitlines()), "unexpected Route B rejection")
    require(cert["quadrature_independence_closed"] is True, "cert quadrature missing")
    require(cert["selected_basis_independence_closed"] is False, "cert basis overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("strict validator still rejects" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(QUAD, attempt)
    write_json(VALIDATION, validation)
    write_json(GAP, source_gap)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"wrote {rel(OUTPUT)}")
    print(f"status {STATUS}")
    print(f"validator_quadrature_fill_exit {validation['exit_code']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
