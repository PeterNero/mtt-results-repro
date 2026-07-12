"""Audit Strominger threshold-operator value / metrology-unit source frontier."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_stromingerthresholdoperatorvalue_or_metrologyunitsource.py"

SLUG = "selected_stromingerthresholdoperatorvalue_or_metrologyunitsource"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StromingerThresholdOperatorValue_or_MetrologyUnitSource_v1.md"

STROMINGER_ROUTE = PACKET_DIR / "strominger_threshold_value_route_import.packet.json"
METROLOGY_ROUTE = PACKET_DIR / "metrology_unit_source_route.packet.json"
EXIT_DECISION = PACKET_DIR / "strict_exit_decision_after_strominger_and_metrology.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_torsional_operator_value_contract.packet.json"

STATUS = (
    "MTT_SELECTED_STROMINGERTHRESHOLDOPERATORVALUE_OR_METROLOGYUNITSOURCE_"
    "BUILT_PARTIAL_TORSIONAL_GEOMETRY_METROLOGY_PRIMITIVE_STRICT_VALUES_OPEN"
)
NEXT = "MTT_Selected_TorsionalWeitzenbockEndomorphism_or_OUWeightsSourceDerivation_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    strominger = load(STROMINGER_ROUTE)
    metrology = load(METROLOGY_ROUTE)
    exit_decision = load(EXIT_DECISION)
    next_contract = load(NEXT_CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_contract["next_required_artifact"] == NEXT, "next contract mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, strominger, metrology, exit_decision, next_contract]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["previous_frontier_honored"] is True, "previous frontier not honored")
    require(decision["qasu3_torsional_geometry_imported"] is True, "qasu3 torsional import missing")
    require(decision["selected_radii_imported"] is True, "selected radii missing")
    require(decision["relative_one_form_weights_imported"] is True, "relative weights missing")
    require(decision["bismut_trace_coefficient_8A2_imported"] is True, "8A2 missing")
    require(decision["metric_logdet_monotone_no_mu_selection"] is True, "monotone/no-mu fact missing")
    require(decision["strict_strominger_threshold_value_rows"] == 0, "threshold row overaccepted")
    require(decision["selected_local_system_torsion_rows"] == 0, "torsion row overaccepted")
    require(decision["strict_metrology_unit_source_rows"] == 0, "metrology row overaccepted")
    require(decision["one_universal_primitive_extension_ready"] is True, "unit primitive readiness lost")
    require(decision["one_universal_primitive_adopted_here"] is False, "unit primitive silently adopted")
    require(decision["strict_P_EW_source_rows"] == 0, "strict P_EW overaccepted")
    require(decision["strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K overaccepted")
    require(decision["premised_one_primitive_lane_preserved"] is True, "premised lane lost")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(strominger["status"] == "PARTIAL_TORSIONAL_GEOMETRY_IMPORTED_THRESHOLD_VALUE_OPEN", "strominger status mismatch")
    support = strominger["selected_support_values"]
    radii = support["selected_radii"]
    recomputed_A = radii["r3"] / (radii["r1"] * radii["r2"])
    require(math.isclose(support["A_r3_over_r1r2"], recomputed_A, rel_tol=0.0, abs_tol=1e-15), "A recompute mismatch")
    require(
        math.isclose(support["eight_A_squared"], 8.0 * recomputed_A * recomputed_A, rel_tol=0.0, abs_tol=1e-15),
        "8A2 recompute mismatch",
    )
    samples = support["metric_weighted_logdet_samples"]
    require(samples["mu_0.25"] < samples["mu_1"] < samples["mu_4"], "logdet samples not monotone")
    require(support["metric_weighted_logdet_monotone_on_samples"] is True, "monotone flag mismatch")
    for value in strominger["accepted_final_rows"].values():
        require(value == 0, "strominger final row overaccepted")
    require(
        any("promote selected radii or 8A^2 support" in item for item in strominger["forbidden_promotions"]),
        "8A2 guard missing",
    )
    require(
        any("use monotone sampled logdet values to choose mu by convenience" in item for item in strominger["forbidden_promotions"]),
        "mu guard missing",
    )

    require(metrology["status"] == "ONE_UNIVERSAL_PRIMITIVE_READY_STRICT_SCALE_SOURCE_OPEN", "metrology status mismatch")
    require(metrology["one_universal_primitive_extension_ready"] is True, "primitive readiness mismatch")
    require(metrology["strict_no_knob_alpha_phys_closed"] is False, "alpha strict overclosed")
    require(metrology["strict_current_corpus_nogo"] is True, "strict scale no-go missing")
    require(metrology["accepted_final_rows"]["strict_metrology_unit_source_rows"] == 0, "metrology strict row overaccepted")
    require(
        metrology["accepted_final_rows"]["one_universal_primitive_rows_available_if_adopted"] == 1,
        "primitive option count mismatch",
    )
    require(metrology["crossuse_admission"]["admitted_now"] is False, "crossuse silently admitted")

    require(
        exit_decision["status"] == "STRICT_EXIT_REDUCED_TO_TORSIONAL_OPERATOR_VALUE_OR_ADOPTED_UNIT_PRIMITIVE",
        "exit decision status mismatch",
    )
    require(exit_decision["strict_no_knob_closed"] is False, "exit no-knob overclosed")
    require(exit_decision["true_SM_equivalence_closed"] is False, "exit true SM overclosed")
    require(exit_decision["if_next_operator_value_closes"]["selected_strominger_threshold_operator_finite_part_rows"] == 1, "conditional operator row mismatch")
    require(exit_decision["if_one_universal_primitive_is_adopted"]["adds_counted_shared_physical_parameter"] == 1, "conditional primitive count mismatch")
    for value in exit_decision["new_final_rows_accepted"].values():
        require(value == 0, "exit final row overaccepted")

    require(
        next_contract["status"] == "NEXT_IS_TORSIONAL_WEITZENBOCK_OR_OU_WEIGHT_SOURCE_DERIVATION",
        "next contract status mismatch",
    )
    require(any("torsional Weitzenbock" in item for item in next_contract["must_emit_one_of"]), "E_Qa target missing")
    require(any("OU gamma" in item for item in next_contract["must_emit_one_of"]), "OU target missing")
    require("selected radii, relative weights, or 8A^2 alone as the final threshold finite part" in next_contract["must_not_use"], "support guard missing")

    require("Strominger threshold finite part    : 0" in note, "note missing threshold row")
    require("direct K_threshold.Omega_H.lambda   : 0" in note, "note missing direct K row")
    require(NEXT in note, "note missing next artifact")

    print("Strominger threshold/metrology source frontier audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
