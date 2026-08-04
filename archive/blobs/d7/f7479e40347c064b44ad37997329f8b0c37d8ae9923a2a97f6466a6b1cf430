"""Audit primitive-C1 / Weyl-pair sector-routing import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "primitivec1_or_weylpair_sectorrouting_sourceemission_import.candidate.json"
CERT = ROOT / "certificates" / "primitivec1_or_weylpair_sectorrouting_sourceemission_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "PrimitiveC1_or_WeylPair_SectorRouting_SourceEmission_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_primitivec1_or_weylpair_sectorrouting_sourceemission.py"

STATUS = "PRIMITIVEC1_OR_WEYLPAIR_ROUTING_IMPORTED_STATIC_ROUTE_CLOSED_DYNAMIC_CONTRACTIONS_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1Contractions_or_DynamicOverlapTensor_SourceEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    static = data["static_routing_source_emission"]
    retired = static["retired_sector_routing"]
    require(static["proved"] is True, "static routing not proved")
    require(
        retired["selected_static_sector_route_Z_to_u_e_X_to_d_nuD"] is True,
        "static sector route missing",
    )
    require(retired["phase_route"] == ["u", "e"], "phase route mismatch")
    require(retired["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(
        retired["selected_static_1M_Dirac_neutrino_shift_rule"] is True,
        "1M shift rule missing",
    )
    require(
        retired["selected_static_finite_trace_transfer_normalization"] is True,
        "finite trace normalization missing",
    )
    require(retired["all_six_static_sm_slot_arrows_closed"] is True, "SM-slot arrows open")
    require(retired["source_level_ZX_carrier_closed"] is True, "ZX carrier open")

    transfer = data["conditional_transfer_reclassification"]
    require(transfer["conditional_weyl_transfer_exact"] is True, "conditional transfer not exact")
    require(transfer["static_sector_route_now_selected"] is True, "static route not selected")
    require(
        transfer["conditional_A_promoted_to_A_selected"] is False,
        "conditional transfer overpromoted",
    )

    dynamic = data["dynamic_blockers"]
    for key in [
        "dynamic_visible_routec_operator_source_identity",
        "selected_D_E_Riesz_Green_dotD",
        "selected_dynamic_overlap_tensor_or_transfer_functor",
        "selected_primitive_C1_contractions",
        "selected_b_selected_and_Hessian_normalization",
        "selected_A_selected",
        "selected_sector_response_matrices",
    ]:
        require(dynamic[key] is True, f"dynamic blocker missing: {key}")

    boundary = data["proof_boundary"]
    require(boundary["static_routing_not_enough_for_A_selected"] is True, "A boundary missing")
    require(boundary["dynamic_overlap_tensor_not_emitted"] is True, "dynamic tensor overclaimed")
    require(boundary["primitive_C1_contractions_not_emitted"] is True, "primitive contractions overclaimed")
    require(boundary["observed_data_used"] is False, "observed data used")
    require(boundary["target_fitting_used"] is False, "target fitting used")
    require(boundary["full_SM_closure_claimed"] is False, "full closure overclaimed")

    guardrails = data["guardrails"]
    require(guardrails["static_weyl_sector_route_emitted"] is True, "route not emitted")
    require(guardrails["conditional_weyl_transfer_exact"] is True, "transfer not exact")
    require(
        guardrails["conditional_transfer_promoted_to_A_selected"] is False,
        "conditional transfer promoted",
    )
    require(guardrails["dynamic_overlap_tensor_emitted"] is False, "dynamic tensor emitted")
    require(guardrails["primitive_C1_contractions_emitted"] is False, "primitive contractions emitted")
    require(guardrails["A_selected_claimed"] is False, "A_selected claimed")
    require(guardrails["b_selected_claimed"] is False, "b_selected claimed")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")
    require(guardrails["full_SM_closure_claimed"] is False, "full closure claimed")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
