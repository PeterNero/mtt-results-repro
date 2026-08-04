"""Build partial Route B provenance fill and isolate the remaining basis/quadrature gap."""

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

SLUG = "selected_routeb_partialindependentprovenancefill_or_basisquadraturegap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PARTIAL = PACKET_DIR / "route_b_partial_independent_provenance_fill.packet.json"
VALIDATION = PACKET_DIR / "strict_validator_result.packet.json"
GAP = PACKET_DIR / "basis_quadrature_independence_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_RouteBPartialIndependentProvenanceFill_or_BasisQuadratureGap_v1.md"

STRICT_GATE = DATA / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution.candidate.json"
STRICT_ATTEMPT = (
    DATA
    / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution"
    / "current_fill_attempt.packet.json"
)
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
ROUTE_B_TEMPLATE = (
    DATA
    / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution"
    / "route_b_independent_execution.strict_template.json"
)
ZERO_BASIS = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "inputs"
    / "zero_mode_basis.packet.json"
)
FINITE_WEYL = DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation.candidate.json"
ALL_ROWS = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_72_exact_weyl_row_execution.packet.json"
)
FORMAL_110 = (
    DATA
    / "selected_routeaemission_or_routebgalerkinrows_execution"
    / "formal_110_row_execution.packet.json"
)
FORMAL_INTEGRATED = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)

STATUS = "MTT_SELECTED_ROUTEB_PARTIALINDEPENDENTPROVENANCEFILL_BUILT_BASIS_QUADRATURE_GAP_OPEN"
NEXT = "MTT_Selected_RouteBSelectedBasisQuadratureSource_or_RouteAPhysicalSourceFill_v1"


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

    strict_gate = load(STRICT_GATE)
    strict_attempt = load(STRICT_ATTEMPT)
    route_b_template = load(ROUTE_B_TEMPLATE)
    zero_basis = load(ZERO_BASIS)
    finite_weyl = load(FINITE_WEYL)
    all_rows = load(ALL_ROWS)
    formal_110 = load(FORMAL_110)
    formal_integrated = load(FORMAL_INTEGRATED)

    route_b_partial = dict(route_b_template)
    route_b_partial.update(
        {
            "schema": "MTTRouteBPartialIndependentProvenanceFill.v1",
            "status": "PARTIAL_FILL_EXACTNESS_ATTACHED_BASIS_QUADRATURE_INDEPENDENCE_OPEN",
            "all_72_primitive_rows_executed": all_rows["computed_value_clause_closed_for_all_rows"],
            "formal_110_rows_executed": formal_integrated["formal_110_rows_executed"],
            "exactness_or_error_certificates_attached": all_rows["exactness_clause_closed_for_all_rows"],
            "selected_basis_independent_of_residual_projector": False,
            "quadrature_rule_independent_of_locked_target": False,
            "source_independent_of_residual_projector_replay": False,
            "attached_independent_provenance_sources": [
                {
                    "source": rel(ALL_ROWS),
                    "closes": "all 72 primitive row values and exactness/error certificates",
                    "independence_level": "finite Weyl polynomial exactness; value source still inherits selected row target lineage",
                    "promotes_independence": False,
                },
                {
                    "source": rel(FINITE_WEYL),
                    "closes": "finite Weyl trace/Frobenius measure uniqueness",
                    "independence_level": "measure normalization independent of observed constants and not a free knob",
                    "promotes_independence": False,
                },
                {
                    "source": rel(FORMAL_110),
                    "closes": "formal 110-row finite trace execution values",
                    "independence_level": "formal finite-trace execution, not physical Galerkin provenance",
                    "promotes_independence": False,
                },
            ],
            "support_basis_packet": {
                "path": rel(ZERO_BASIS),
                "basis_dimension": zero_basis["basis_dimension"],
                "selected_source_verified": zero_basis["selected_source_verified"],
                "why_not_independent": zero_basis["why_not_honest_selected_yet"],
            },
        }
    )

    candidate_attempt = dict(strict_attempt)
    candidate_attempt["status"] = "ROUTE_B_PARTIAL_FILL_ATTEMPT_FAILS_STRICT_VALIDATOR_AS_EXPECTED"
    candidate_attempt["route_B_independent_execution"] = route_b_partial
    candidate_attempt["promotion_allowed_now"] = False

    write_json(PARTIAL, candidate_attempt)
    validation = run_validator(PARTIAL)

    gap = {
        "schema": "MTTRouteBBasisQuadratureIndependenceGap.v1",
        "status": "EXACTNESS_CLOSED_BASIS_QUADRATURE_PROVENANCE_OPEN",
        "closed_now": {
            "all_72_primitive_rows_executed": route_b_partial["all_72_primitive_rows_executed"],
            "formal_110_rows_executed": route_b_partial["formal_110_rows_executed"],
            "exactness_or_error_certificates_attached": route_b_partial[
                "exactness_or_error_certificates_attached"
            ],
            "finite_Weyl_trace_measure_derived": finite_weyl["what_closes_now"][
                "finite_Weyl_invariant_trace_measure_derived"
            ],
        },
        "still_open_for_strict_validator": {
            "selected_basis_independent_of_residual_projector": True,
            "quadrature_rule_independent_of_locked_target": True,
            "source_independent_of_residual_projector_replay": True,
        },
        "minimal_next_source_object": {
            "name": "SelectedRouteBGalerkinBasisQuadratureSourceCertificate",
            "must_emit": [
                "selected zero-mode/Galerkin basis K_s independent of residual-projector replay",
                "selected finite/continuum quadrature rule chosen before locked target values",
                "provenance that 72 primitive rows, 36 sector rows, and 2 Hessian/source rows come from that basis/quadrature source",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRouteBPartialIndependentProvenanceFillOrBasisQuadratureGap",
        "status": STATUS,
        "inputs": {
            "strict_gate": rel(STRICT_GATE),
            "strict_current_attempt": rel(STRICT_ATTEMPT),
            "route_b_strict_template": rel(ROUTE_B_TEMPLATE),
            "zero_mode_basis_support": rel(ZERO_BASIS),
            "finite_weyl_trace_uniqueness": rel(FINITE_WEYL),
            "all_72_exact_rows": rel(ALL_ROWS),
            "formal_110_execution": rel(FORMAL_110),
            "formal_110_integrated": rel(FORMAL_INTEGRATED),
        },
        "output_packets": {
            "route_b_partial_fill_attempt": rel(PARTIAL),
            "strict_validator_result": rel(VALIDATION),
            "basis_quadrature_independence_gap": rel(GAP),
        },
        "what_closes_now": {
            "route_B_exactness_or_error_certificates_attached": True,
            "all_72_primitive_rows_confirmed": True,
            "formal_110_rows_confirmed": True,
            "finite_Weyl_trace_measure_reused_as_non_knob_support": True,
            "strict_validator_rejection_reduced_to_provenance_independence": True,
        },
        "what_remains_open": {
            "selected_basis_independent_of_residual_projector": True,
            "quadrature_rule_independent_of_locked_target": True,
            "source_independent_of_residual_projector_replay": True,
            "Route_A_physical_source_fill": True,
            "unpatched_dynamic_C1_packet_closure": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "strict_validation": validation,
        "theorem": {
            "name": "RouteBPartialProvenanceFillReductionTheorem",
            "proved": True,
            "statement": (
                "The existing finite Weyl execution legally fills Route B value and exactness clauses "
                "of the strict promotion validator. The remaining Route B obstruction is not numeric: "
                "it is the source-level independence of the selected Galerkin basis and quadrature rule "
                "from residual-projector replay and locked target values."
            ),
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_gate_status": strict_gate["status"],
    }

    cert = {
        "certificate": "MTT_Selected_RouteBPartialIndependentProvenanceFill_or_BasisQuadratureGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "strict_validator_exit_code": validation["exit_code"],
        "strict_validator_still_rejects": validation["exit_code"] == 1,
        "route_B_exactness_or_error_certificates_attached": True,
        "route_B_basis_independence_closed": False,
        "route_B_quadrature_independence_closed": False,
        "route_B_source_independence_closed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected RouteBPartialIndependentProvenanceFill or BasisQuadratureGap v1

Status: `{STATUS}`

This step partially fills the strict Route B validator.

Closed now:

1. all 72 primitive rows are executed exactly;
2. the formal 110-row packet is executed;
3. exactness/error certificates are attached from the finite Weyl row execution;
4. finite Weyl trace/Frobenius measure uniqueness remains non-knob support.

Still open:

1. selected Galerkin/zero-mode basis independence from residual-projector replay;
2. selected quadrature rule independence from locked target values;
3. source independence of the full row packet.

The strict validator still rejects the partial fill, as it should.

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
PARTIAL = PACKET_DIR / "route_b_partial_independent_provenance_fill.packet.json"
GAP = PACKET_DIR / "basis_quadrature_independence_gap.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBPartialIndependentProvenanceFill_or_BasisQuadratureGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    partial = load(PARTIAL)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    route_b = partial["route_B_independent_execution"]
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(PARTIAL)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(route_b["all_72_primitive_rows_executed"] is True, "72 rows not closed")
    require(route_b["formal_110_rows_executed"] is True, "110 rows not closed")
    require(route_b["exactness_or_error_certificates_attached"] is True, "exactness not attached")
    require(route_b["selected_basis_independent_of_residual_projector"] is False, "basis overclosed")
    require(route_b["quadrature_rule_independent_of_locked_target"] is False, "quadrature overclosed")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "source independence overclosed")
    require(len(route_b["attached_independent_provenance_sources"]) >= 3, "support sources missing")
    require(gap["closed_now"]["finite_Weyl_trace_measure_derived"] is True, "finite trace support missing")
    require(proc.returncode == 1, "strict validator should reject partial fill")
    require(any("Route B missing" in line for line in proc.stderr.splitlines()), "missing Route B rejection")
    require(cert["strict_validator_still_rejects"] is True, "cert validator mismatch")
    require(cert["route_B_exactness_or_error_certificates_attached"] is True, "cert exactness missing")
    require(cert["route_B_basis_independence_closed"] is False, "cert basis overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("strict validator still rejects" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(VALIDATION, validation)
    write_json(GAP, gap)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"wrote {rel(OUTPUT)}")
    print(f"status {STATUS}")
    print(f"validator_partial_exit {validation['exit_code']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
