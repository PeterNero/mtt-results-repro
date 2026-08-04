"""Audit the imported static enriched Weyl-pair provenance frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / "selected_enriched_weylpair_static_provenance_dynamicc1_open.import.json"
MD_PATH = ROOT / "EnrichedWeylPair_StaticProvenance_DynamicC1_Open_Import_v1.md"

EXPECTED_STATUS = "IMPORTED_STATIC_WEYLPAIR_PROVENANCE_CLOSED_DYNAMIC_C1_VALUES_OPEN"
EXPECTED_NEXT = "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1"


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

    closes = data["what_closes_now"]
    for key in [
        "static_enriched_weylpair_source_provenance",
        "static_Z_to_u_e_X_to_d_nuD_route",
        "static_1M_Dirac_neutrino_shift_rule",
        "static_finite_trace_transfer_normalization",
    ]:
        require(closes[key] is True, f"missing closed static provenance field: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_dynamic_source_to_C1_transfer_tensor",
        "theorem_derived_A_selected",
        "theorem_derived_b_selected",
        "selected_deltaTheta_C1",
        "honest_selected_Galerkin_C1_execution_values",
    ]:
        require(remains[key] is True, f"missing open dynamic field: {key}")

    for phrase in [
        "static enriched Weyl-pair provenance is closed",
        "dynamic C1 transfer values are still open",
        "emits `A_selected`",
    ]:
        require(phrase in text, f"missing markdown phrase: {phrase}")

    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    print("PASS selected_enriched_weylpair_static_provenance_dynamicc1_open.import.json")


if __name__ == "__main__":
    main()
