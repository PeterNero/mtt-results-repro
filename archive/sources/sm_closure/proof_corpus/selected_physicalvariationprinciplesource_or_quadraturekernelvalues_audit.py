"""Audit selected physical variation-principle source / quadrature-kernel values gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_physical_source_theorem_template.packet.json"
ROUTE_B = PACKET_DIR / "route_b_quadrature_kernel_value_manifest.packet.json"
CONTRACT = PACKET_DIR / "source_or_kernel_acceptance_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalVariationPrincipleSource_or_QuadratureKernelValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALVARIATIONPRINCIPLESOURCE_OR_QUADRATUREKERNELVALUES_BUILT_VALUE_SLOTS_OPEN"
NEXT = "MTT_Selected_C1KernelValuesExecution_or_PhysicalSourcePromotion_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(route_a["status"] == "PHYSICAL_SOURCE_THEOREM_TEMPLATE_BUILT_NOT_PROMOTED", "route A status mismatch")
    require(route_a["theorem_name"] == "SelectedPhiFinC1PhysicalVariationSourceTheorem", "theorem name mismatch")
    require(len(route_a["required_clauses"]) == 4, "route A clause count mismatch")
    require(route_a["formal_support_available"]["finite_euler_projection_derived"] is True, "finite Euler support missing")
    require(route_a["formal_support_available"]["least_norm_completion_selects_Q_residual"] is True, "least-norm support missing")
    require(route_a["formal_support_available"]["conditional_PhiFinC1_application"] is True, "conditional support missing")
    require(route_a["source_promoted_now"] is False, "route A source overclaimed")
    require(route_a["observed_data_used"] is False and route_a["target_fitting_used"] is False, "route A data guardrail violated")

    require(route_b["status"] == "KERNEL_VALUE_MANIFEST_BUILT_VALUES_OPEN", "route B status mismatch")
    counts = route_b["counts"]
    require(counts["primitive_kernel_slots"] == 72, "primitive slot count mismatch")
    require(counts["hessian_source_slots"] == 2, "hessian slot count mismatch")
    require(counts["sector_matrix_slots"] == 36, "sector slot count mismatch")
    require(counts["total_value_slots"] == 110, "total slot count mismatch")
    require(counts["independent_values_emitted"] == 0, "independent values overclaimed")
    require(counts["replay_rows_available_as_checks"] == 36, "replay check count mismatch")
    require(len(route_b["primitive_kernel_slots"]) == 72, "primitive slot list mismatch")
    require(len(route_b["hessian_source_slots"]) == 2, "hessian slot list mismatch")
    require(len(route_b["sector_matrix_slots"]) == 36, "sector slot list mismatch")
    require(all(slot["independent_value_emitted"] is False for slot in route_b["primitive_kernel_slots"]), "primitive slot overclaim")
    require(route_b["selected_measure_pairing_defined"] is False, "measure pairing overclaimed")
    require(route_b["exactness_or_error_bound_certificate"] is False, "exactness certificate overclaimed")
    require(route_b["run_executed_now"] is False, "engine run overclaimed")

    require(contract["status"] == "ACCEPTANCE_CONTRACT_FIXED_VALUES_OPEN", "contract status mismatch")
    require(contract["accept_if_route_B"]["all_primitive_kernel_values_independent"] == 72, "contract primitive mismatch")
    require(contract["accept_if_route_B"]["all_hessian_source_values_independent"] == 2, "contract hessian mismatch")
    require(contract["accept_if_route_B"]["all_sector_matrix_values_independent"] == 36, "contract sector mismatch")
    require(contract["locked_target_check"]["passes_locked_target_by_replay"] is True, "locked target check missing")
    require(contract["current_result"]["route_A_accepts_now"] is False, "contract route A overclaim")
    require(contract["current_result"]["route_B_accepts_now"] is False, "contract route B overclaim")
    require(contract["current_result"]["closure_claimed"] is False, "contract closure overclaim")
    require("using observed masses, CKM/PMNS, or CP as selectors" in contract["forbidden_shortcuts"], "selector guardrail missing")

    for key in [
        "physical_source_theorem_template_built",
        "quadrature_kernel_value_manifest_built",
        "all_value_slots_enumerated",
        "acceptance_contract_fixed",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "prove_physical_source_theorem",
        "define_selected_measure_pairing",
        "emit_72_independent_primitive_kernel_values",
        "emit_2_independent_hessian_source_values",
        "emit_36_independent_sector_matrix_values",
        "exactness_or_error_bound_certificate",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("primitive kernel value slots             = 72" in note, "note missing primitive slots")
    require("independent values emitted               = 0" in note, "note missing no-overclaim line")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
