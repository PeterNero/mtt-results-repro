"""Audit post-AH8 internal value-row promotion."""

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
BUILDER = ROOT / "scripts" / "build_selected_internalvaluerows_afterah8_or_literalglobalwitness.py"

SLUG = "selected_internalvaluerows_afterah8_or_literalglobalwitness"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_InternalValueSourceRowsAfterAH8_or_LiteralGlobalWitnessConstruction_v1.md"
DYNAMIC_IMPORT = PACKET_DIR / "post_ah8_first_dynamic_value_row_import.packet.json"
PROJECTION_IMPORT = PACKET_DIR / "post_ah8_projection_weight_import.packet.json"
SCALAR_GATE = PACKET_DIR / "post_ah8_scalar_magnitude_value_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_magnitude_bearing_rows_after_post_ah8_dynamic_import.packet.json"

STATUS = "MTT_SELECTED_INTERNALVALUEROWS_AFTERAH8_FIRST_DYNAMIC_ROWS_IMPORTED_MAGNITUDES_OPEN"
NEXT = "MTT_Selected_MagnitudeBearingRowsAfterPostAH8DynamicImport_or_ThresholdResponseDerivation_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    dynamic = load(DYNAMIC_IMPORT)
    projection = load(PROJECTION_IMPORT)
    scalar = load(SCALAR_GATE)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, dynamic, projection, scalar, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["post_AH8_first_dynamic_value_rows_imported"] is True, "dynamic rows not imported")
    require(decision["accepted_selected_dynamic_value_row_count"] == 2, "dynamic row count")
    require(decision["source_normalized_projection_weights_closed"] is True, "projection weights not closed")
    require(decision["magnitude_bearing_projection_weights_closed"] is False, "magnitude weights overclosed")
    require(decision["selected_threshold_response_rows_closed"] is False, "threshold rows overclosed")
    require(decision["accepted_internal_selected_scalar_rows"] == 0, "internal scalar rows overaccepted")
    require(decision["accepted_rowlocal_scalar_rows"] == 0, "rowlocal scalar rows overaccepted")
    require(decision["accepted_full_s2_scalar_rows"] == 0, "full-S2 rows overaccepted")
    require(decision["accepted_yukawa_magnitude_rows"] == 0, "Yukawa magnitude rows overaccepted")
    require(decision["strict_global_closed"] is False, "strict global overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(dynamic["accepted_selected_dynamic_value_row_count"] == 2, "dynamic packet count")
    require(dynamic["selected_by_MTT"] is True, "dynamic not selected")
    require(dynamic["accepted_row_ids"] == [
        "VSD-01.phase.I_plus_Z.u.first_dynamic_row",
        "VSD-01.phase.I_plus_Z.e.first_dynamic_row",
    ], "dynamic row ids")
    for not_accepted in [
        "Yukawa magnitudes",
        "threshold/mass-scheme scalar rows",
        "full-S2 scalar value rows",
        "true SM equivalence rows",
    ]:
        require(not_accepted in dynamic["not_accepted_as"], f"dynamic boundary missing: {not_accepted}")

    require(projection["source_normalized_sector_projection_weights_closed"] is True, "projection packet")
    require(projection["first_dynamic_row_repromoted_as_source_normalized"] is True, "first row not repromoted")
    require(projection["magnitude_bearing_projection_weights_closed"] is False, "projection magnitude overclosed")
    require(projection["selected_threshold_response_rows_closed"] is False, "projection threshold overclosed")

    require(scalar["accepted_non_scalar_dynamic_rows"] == 2, "scalar gate dynamic")
    require(scalar["accepted_internal_selected_scalar_rows"] == 0, "scalar gate internal")
    require(scalar["accepted_rowlocal_scalar_rows"] == 0, "scalar gate rowlocal")
    require(scalar["accepted_full_s2_scalar_rows"] == 0, "scalar gate full-S2")
    require(scalar["accepted_yukawa_magnitude_rows"] == 0, "scalar gate Yukawa")
    require(scalar["true_SM_equivalence_closed"] is False, "scalar gate true SM")

    for item in [
        "AH-equivalent BN27 8/8 matrix row",
        "post-AH8 route selection",
        "first selected dynamic non-scalar value rows",
        "source-normalized projection weights",
    ]:
        require(item in next_packet["do_not_reopen"], f"non-reopen missing: {item}")
    for item in [
        "magnitude-bearing projection weights",
        "selected threshold response rows",
        "rowlocal scalar retarded-overlap values",
        "full-S2 / Delta_S2 scalar correction rows",
        "lambda_H/H-threshold payload transport",
    ]:
        require(item in next_packet["remaining_value_targets"], f"remaining target missing: {item}")

    require(cert["post_AH8_first_dynamic_value_rows_imported"] is True, "cert import")
    require(cert["accepted_selected_dynamic_value_row_count"] == 2, "cert count")
    require(cert["source_normalized_projection_weights_closed"] is True, "cert weights")
    require(cert["magnitude_bearing_projection_weights_closed"] is False, "cert magnitude")
    require(cert["accepted_yukawa_magnitude_rows"] == 0, "cert Yukawa")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("imports `2` accepted selected dynamic non-scalar value" in note, "note dynamic")
    require("They are not Yukawa" in note, "note boundary")
    require(NEXT in note, "note next")

    print("Post-AH8 internal value-row promotion audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
