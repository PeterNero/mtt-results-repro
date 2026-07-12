from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraldimensionfulblocksandnormalization"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
PACKET = ROOT / "candidate_data" / SLUG / "neutral_dimensionful_blocks_normal_form.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralDimensionfulBlocksAndNormalization_v1.md"

STATUS = "MTT_SELECTED_NEUTRALDIMENSIONFULBLOCKS_NORMALFORM_REDUCED_VALUE_SOURCE_OPEN"
NEXT = "MTT_Selected_NeutralOverlapKernelPhysicalUnitOrActionCompleteness_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    packet = load(PACKET)
    candidate = load(CANDIDATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == STATUS, "packet status changed")
    require(cert["status"] == STATUS, "certificate status changed")
    require(packet["next_required_artifact"] == NEXT, "packet next artifact changed")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact changed")
    require(packet["normal_form_theorem"]["proved"] is True, "normal-form theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(packet["observed_data_used_as_selector"] is False, "observed selector used")
    require(packet["target_fitting_used"] is False, "target fitting used")
    require(cert["observed_data_used_as_selector"] is False, "cert observed selector used")
    require(cert["target_fitting_used"] is False, "cert target fitting used")

    closes = packet["what_closes_here"]
    require(closes["dimensionful_block_normal_form_theorem"] is True, "normal form not closed")
    require(closes["benchmark_and_physical_anchor_shortcuts_rejected"] is True, "shortcuts not rejected")
    require(closes["remaining_fields_contracted_to_value_source"] is True, "remaining fields not contracted")
    require(closes["three_lawful_exit_routes"] == [
        "A_dirac_dimensionful_MD",
        "B_majorana_or_seesaw_blocks",
        "C_nil_boundary_effective_spectrum",
    ], "lawful routes changed")

    sources = packet["source_imports"]
    require(sources["U5_predecessor_fields"] == "4/8", "A23 predecessor not imported")
    require(sources["selected_branch"] is True, "selected branch not imported")
    require(sources["nil_boundary_formula_closed"] is True, "nil boundary theorem not imported")
    require(sources["physical_unit_bridge_status"] == "CONDITIONAL_MAP_CLOSED_PHYSICAL_UNIT_COEFFICIENT_OPEN", "physical unit status changed")
    require(sources["physical_unit_selected"] is False, "physical unit overselected")
    corpus = sources["corpus_sources"]
    for key in [
        "overlap_kernel_certificate_schema_present",
        "neutral_majorana_formula_present",
        "majorana_branch_criterion_present",
        "no_proxy_failure_theorem_present",
        "benchmark_majorana_scale_declared_open",
    ]:
        require(corpus[key] is True, f"corpus import missing {key}")

    routes = packet["lawful_routes"]
    require(len(routes) == 3, "route count changed")
    require(cert["lawful_exit_route_count"] == 3, "cert route count changed")
    require(cert["accepted_lawful_exit_route_count"] == 0, "route overaccepted")
    expected_ids = {"A_dirac_dimensionful_MD", "B_majorana_or_seesaw_blocks", "C_nil_boundary_effective_spectrum"}
    require({route["id"] for route in routes} == expected_ids, "route IDs changed")
    for route in routes:
        require(route["accepted_now"] is False, f"{route['id']} overaccepted")
        require(route["missing"], f"{route['id']} missing list empty")
        require(route["would_close"], f"{route['id']} closure list empty")

    fields = packet["required_field_acceptance"]
    require(packet["required_fields_total"] == 8, "field total changed")
    require(packet["required_fields_closed"] == 4, "field count changed")
    require(cert["required_fields_closed"] == 4, "cert field count changed")
    require(packet["new_value_fields_closed_here"] == 0, "new value fields overclosed")
    require(cert["new_value_fields_closed_here"] == 0, "cert new value fields overclosed")
    for field in [
        "source_id",
        "neutral_basis_L_and_Nc",
        "Dirac_U1_or_selected_self_character_k",
        "same_source_no_observed_selector_certificate",
    ]:
        require(fields[field] is True, f"previous field lost: {field}")
    for field in [
        "dimensionful_M_D_3x3",
        "dimensionful_M_L_3x3",
        "dimensionful_M_R_3x3",
        "absolute_normalization_and_scheme",
    ]:
        require(fields[field] is False, f"value field overclosed: {field}")
        require(cert[f"{field}_closed"] is False, f"cert value field overclosed: {field}")

    rejected = packet["rejected_shortcuts"]
    require(set(rejected) == {
        "dimensionless_C1_nuD_shape",
        "corrected_execution_II_benchmark_seesaw",
        "observed_neutrino_splittings_or_cosmology",
        "Planck_Newton_TeV_or_modal_gap_physical_unit",
    }, "shortcut set changed")
    for key, value in rejected.items():
        require(value["accepted"] is False, f"shortcut accepted: {key}")
        require(value["reason"], f"shortcut reason missing: {key}")
    require(cert["benchmark_seesaw_rejected_as_source"] is True, "benchmark rejection missing")
    require(cert["observed_splittings_rejected_as_selector"] is True, "observed split rejection missing")
    require(cert["conditional_physical_unit_rejected_as_normalization"] is True, "physical unit rejection missing")

    require(packet["selected_neutral_operator_accepted"] is False, "neutral operator overaccepted")
    require(packet["U5_closed"] is False, "U5 overclosed")
    require(cert["selected_neutral_operator_accepted"] is False, "cert neutral operator overaccepted")
    require(cert["U5_closed"] is False, "cert U5 overclosed")

    for phrase in [
        "neutral operator remains `4/8`",
        "Dirac-complete route",
        "Majorana/seesaw route",
        "Effective nil-boundary route",
        "Corrected Execution II seesaw matrices are benchmark/existence data",
        "Planck/Newton/TeV/modal-gap physical-unit bridges are conditional",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(json.dumps({
        "U5_required_fields": "4/8",
        "lawful_exit_routes": 3,
        "accepted_routes": 0,
        "new_value_fields_closed": 0,
        "next": NEXT,
    }, indent=2))
    print("selected neutral dimensionful blocks and normalization audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
