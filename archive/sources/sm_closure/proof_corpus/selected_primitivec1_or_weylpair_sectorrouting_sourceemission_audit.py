"""Audit primitive-C1 / Weyl-pair sector-routing source-emission reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
CERT = ROOT / "certificates" / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveC1_or_WeylPairSectorRouting_SourceEmission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_primitivec1_or_weylpair_sectorrouting_sourceemission.py"

STATUS = "MTT_SELECTED_PRIMITIVEC1_OR_WEYLPAIR_SECTORROUTING_SOURCEEMISSION_STATIC_ROUTING_CLOSED_DYNAMIC_CONTRACTIONS_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_DynamicOverlapTensor_SourceEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    static = data["static_routing_source_emission"]
    require(static["proved"] is True, "static routing theorem not proved")
    retired = static["retired_sector_routing"]
    require(
        retired["selected_static_sector_route_Z_to_u_e_X_to_d_nuD"] is True,
        "static sector route not closed",
    )
    require(
        retired["selected_static_1M_Dirac_neutrino_shift_rule"] is True,
        "1M Dirac-neutrino shift rule not closed",
    )
    require(
        retired["selected_static_finite_trace_transfer_normalization"] is True,
        "static trace transfer normalization not closed",
    )
    require(retired["all_six_static_sm_slot_arrows_closed"] is True, "SM-slot arrows not closed")
    require(retired["phase_route"] == ["u", "e"], "phase route mismatch")
    require(retired["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(retired["source_level_ZX_carrier_closed"] is True, "ZX carrier not closed")
    require(
        retired["sector_charge_old_artifact_still_open_but_superseded_at_static_tier"] is True,
        "old sector-charge boundary not recorded",
    )

    transfer = data["conditional_transfer_reclassification"]
    require(transfer["conditional_weyl_transfer_exact"] is True, "conditional Weyl transfer not exact")
    require(transfer["static_sector_route_now_selected"] is True, "static route not selected")
    require(
        transfer["conditional_A_promoted_to_A_selected"] is False,
        "conditional A overpromoted",
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
    require(boundary["dynamic_overlap_tensor_not_emitted"] is True, "dynamic overlap overclaimed")
    require(boundary["primitive_C1_contractions_not_emitted"] is True, "primitive contractions overclaimed")
    require(boundary["observed_data_used"] is False, "observed data used")
    require(boundary["target_fitting_used"] is False, "target fitting used")
    require(boundary["full_SM_closure_claimed"] is False, "full closure overclaimed")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["A_selected_claimed"] is False, "A_selected claimed")
    require(data["b_selected_claimed"] is False, "b_selected claimed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
