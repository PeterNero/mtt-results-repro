"""Audit post-AH8 literal-witness and precision-value route selection."""

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
BUILDER = ROOT / "scripts" / "build_selected_literalwitness_or_precisionvalues_afterah8.py"

SLUG = "selected_literalwitness_or_precisionvalues_afterah8"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LiteralGoodCoverHYMGlobalWitness_or_PrecisionValueSourceAfterAH8_v1.md"
LITERAL_ATTEMPT = PACKET_DIR / "literal_witness_attempt_after_ah8.packet.json"
VALUE_ROUTE = PACKET_DIR / "precision_value_route_after_ah8.packet.json"
NEXT_PACKET = PACKET_DIR / "next_internal_value_source_execution_after_ah8.packet.json"

STATUS = "MTT_SELECTED_LITERALWITNESS_OR_PRECISIONVALUES_AFTERAH8_LITERAL_ZERO_VALUE_ROUTE_SELECTED"
NEXT = "MTT_Selected_InternalValueSourceRowsAfterAH8_or_LiteralGlobalWitnessConstruction_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    literal = load(LITERAL_ATTEMPT)
    value = load(VALUE_ROUTE)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, literal, value, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["literal_global_witness_families_required"] == 2, "literal family requirement")
    require(decision["literal_global_witness_families_accepted_now"] == 0, "literal family overaccepted")
    require(decision["strict_global_closed"] is False, "strict global overclosed")
    require(decision["source_layer_closed"] is True, "source layer not closed")
    require(decision["external_admitted_replay_rows"] == 10, "external replay row count")
    require(decision["internal_selected_value_rows"] == 0, "internal rows overaccepted")
    require(decision["rowlocal_internal_scalar_rows"] == 0, "rowlocal rows overaccepted")
    require(decision["full_s2_accepted_scalar_rows"] == 0, "full-S2 rows overaccepted")
    require(decision["precision_value_route_selected"] is True, "precision route not selected")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(literal["literal_witness_families_required"] == 2, "literal packet required")
    require(literal["literal_witness_families_accepted_now"] == 0, "literal packet accepted")
    require(literal["strict_global_closed"] is False, "literal strict overclosed")
    require("literal_good_cover_Deligne_Cech_data" in literal["remaining_family_names"], "missing Cech family")
    require("literal_global_HYM_or_projective_connection_coefficients" in literal["remaining_family_names"], "missing HYM family")

    require(value["source_layer_closed"] is True, "value source layer")
    for key in ["A_selected", "b_selected", "deltaTheta_C1", "dotD_alpha1", "primitive_C1_first_response"]:
        require(value["closed_source_inputs"][key] is True, f"source input not closed: {key}")
    require(value["external_admitted_replay_rows"] == 10, "value external rows")
    require(value["internal_selected_value_rows"] == 0, "value internal rows")
    require(value["rowlocal_internal_scalar_rows"] == 0, "value rowlocal rows")
    require(value["full_s2_accepted_scalar_rows"] == 0, "value full-S2 rows")
    require(value["precision_value_route_selected"] is True, "value route selected")
    require(value["true_SM_equivalence_closed"] is False, "value true SM")

    for item in [
        "AH-equivalent BN27 8/8 matrix row",
        "selected dotD/C1/A/b/deltaTheta source layer",
        "external admitted replay row tier",
    ]:
        require(item in next_packet["do_not_reopen"], f"non-reopen missing: {item}")
    for item in [
        "selected internal R_theta threshold-response rows",
        "rowwise scalar retarded-overlap values",
        "Delta_S2 / full-S2 scalar correction values",
        "lambda_H/H-threshold payload transport",
    ]:
        require(item in next_packet["execute_next"], f"execute-next missing: {item}")

    require(cert["literal_global_witness_families_accepted_now"] == 0, "cert literal")
    require(cert["source_layer_closed"] is True, "cert source layer")
    require(cert["precision_value_route_selected"] is True, "cert route")
    require(cert["strict_global_closed"] is False, "cert strict")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("currently accepts `0/2` witness families" in note, "note literal")
    require("internal value-source rows are the next" in note, "note route")
    require(NEXT in note, "note next")

    print("Post-AH8 literal-witness / precision-value route audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
