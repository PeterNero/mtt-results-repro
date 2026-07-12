"""Audit the imported Route-B primitive kernel source theorem frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / "selected_primitive_kernel_source_theorem_routeb_frontier.import.json"
MD_PATH = ROOT / "PrimitiveKernelSourceTheorem_RouteB_Frontier_Import_v1.md"

EXPECTED_STATUS = "IMPORTED_ROUTEB_REDUCED_TO_PRIMITIVE_KERNEL_SOURCE_THEOREM_OPEN"
EXPECTED_NEXT = "MTT_Selected_PrimitiveKernelSourceTheorem_or_PhysicalPhiFinC1SourceEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    text = MD_PATH.read_text(encoding="utf-8", errors="ignore")

    require(data["status"] == EXPECTED_STATUS, "unexpected status")
    require(data["next_required_artifact"] == EXPECTED_NEXT, "unexpected next artifact")
    require(data["closure_claimed"] is False, "closure must not be claimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    route_a = data["route_A_status"]
    require(route_a["physical_action_restriction_source_row_emitted"] is False, "Route A should remain unfilled")
    require(route_a["support_only_probe_rejected"] is True, "Route A rejection not recorded")

    closed = data["route_B_closed_support"]
    for key in [
        "finite_weyl_trace_pairing_source",
        "stationary_selected_basis_support",
        "strict_row_source_validator_available",
        "primitive_kernel_source_theorem_template_emitted",
    ]:
        require(closed[key] is True, f"missing Route-B support: {key}")

    theorem = data["selected_primitive_kernel_source_theorem"]
    require(theorem["theorem_name"] == "SelectedPrimitiveKernelSourceTheorem", "wrong theorem name")
    require(theorem["coordinate_system"]["codomain_real_dimension"] == 72, "wrong coordinate dimension")
    require(theorem["coordinate_system"]["sector_order"] == ["u", "d", "e", "nuD"], "wrong sector order")

    missing = theorem["remaining_unclosed_fields"]
    require(len(missing) == 5, "expected five remaining fields")
    require(all(value is True for value in missing.values()), "remaining fields must be marked open")

    for phrase in [
        "Route B is no longer a vague",
        "SelectedPrimitiveKernelSourceTheorem",
        "no residual-projector replay is used as source",
    ]:
        require(phrase in text, f"missing markdown phrase: {phrase}")

    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    print("PASS selected_primitive_kernel_source_theorem_routeb_frontier.import.json")


if __name__ == "__main__":
    main()
