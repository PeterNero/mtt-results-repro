"""Audit torsional Weitzenbock / OU source-derivation reduction."""

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
BUILDER = ROOT / "scripts" / "build_selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation.py"

SLUG = "selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TorsionalWeitzenbockEndomorphism_or_OUWeightsSourceDerivation_v1.md"

ROUTE_REDUCTION = PACKET_DIR / "torsional_or_ou_route_reduction.packet.json"
FINITE_IMPORT = PACKET_DIR / "finite_quotient_identity_route_import.packet.json"
EXACT_VALUES = PACKET_DIR / "exact_oriented_finitepart_values.packet.json"
NEXT_CONTRACT = PACKET_DIR / "source_owned_positive_operator_or_eqapayload_contract.packet.json"

STATUS = (
    "MTT_SELECTED_TORSIONALWEITZENBOCKENDOMORPHISM_OR_OUWEIGHTSSOURCEDERIVATION_"
    "BUILT_FINITE_QUOTIENT_IDENTITY_PRIMARY_SOURCEOWNED_OPERATOR_OPEN"
)
NEXT = "MTT_Selected_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def product(values: list[int]) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    route = load(ROUTE_REDUCTION)
    finite_import = load(FINITE_IMPORT)
    exact = load(EXACT_VALUES)
    next_contract = load(NEXT_CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_contract["next_required_artifact"] == NEXT, "next contract mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, route, finite_import, exact, next_contract]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["previous_frontier_honored"] is True, "previous frontier not honored")
    require(decision["torsional_E_Qa_computed"] is False, "torsional E_Qa overcomputed")
    require(decision["OU_weights_computed"] is False, "OU weights overcomputed")
    require(decision["smooth_finite_heat_zeta_torsion_computed"] is False, "smooth finitepart overcomputed")
    require(decision["finite_quotient_identity_route_selected_primary"] is True, "finite route not primary")
    require(decision["smooth_EQa_route_retained_secondary"] is True, "smooth route not retained")
    require(decision["oriented_table_values_exactly_computed"] is True, "exact table lost")
    require(decision["oriented_abs_sector_logdet_exact"] == "log(92160000)", "oriented logdet mismatch")
    require(decision["full_positive_logdet_exact"] == "log(884736000000)", "full logdet mismatch")
    require(decision["oriented_values_promoted_to_threshold"] is False, "oriented values overpromoted")
    require(decision["source_owned_positive_operator_closed"] is False, "source-owned operator overclosed")
    require(decision["smooth_EQa_payload_closed"] is False, "smooth E_Qa overclosed")
    require(decision["strict_P_EW_source_rows"] == 0, "strict P_EW overaccepted")
    require(decision["strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K overaccepted")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(route["status"] == "TORSIONAL_E_OR_OU_REDUCED_TO_FINITE_QUOTIENT_IDENTITY_PRIMARY", "route status mismatch")
    require(route["route_selection"]["primary"] == "finite_quotient_identity", "primary route mismatch")
    require(route["route_selection"]["secondary"] == "smooth_EQa_payload", "secondary route mismatch")
    for key in [
        "same_branch_source_certificate",
        "full_fixed_gauge_domain",
        "Weitzenbock_E_Qa",
        "OU_gamma_nk_weights",
        "finite_heat_zeta_torsion_part",
        "computed_threshold_value",
    ]:
        require(route["torsional_route_status"][key] is False, f"torsional blocker overclosed: {key}")
    for value in route["accepted_final_rows"].values():
        require(value == 0, "route final row overaccepted")

    require(finite_import["status"] == "EXACT_ORIENTED_TABLE_IMPORTED_SOURCE_OWNERSHIP_OPEN", "finite import status mismatch")
    require(finite_import["filled_support"]["same_branch_certificate"] is True, "same-branch support missing")
    require(finite_import["filled_support"]["orientation_binding"] is True, "orientation binding missing")
    require(finite_import["filled_support"]["no_double_count_shared_circle_policy"] is True, "shared-circle policy missing")
    for value in finite_import["accepted_final_rows"].values():
        require(value == 0, "finite import final row overaccepted")
    for value in finite_import["open_source_fields"].values():
        require(value is False, "open source field unexpectedly closed")
    require(
        "identify log(92160000) with log(2008)" in finite_import["forbidden_shortcuts"],
        "logdet identification guard missing",
    )

    values = exact["finitepart_values"]
    require(product(values["plus_sector_positive_eigenvalues"]) == 9600, "plus product mismatch")
    require(product(values["minus_sector_positive_eigenvalues"]) == 9600, "minus product mismatch")
    require(product(values["full_positive_eigenvalues"]) == 884736000000, "full product mismatch")
    require(values["oriented_abs_sector_product"] == 92160000, "oriented abs product mismatch")
    require(exact["support_only_not_promoted"] is True, "exact values promoted")
    require(values["oriented_abs_sector_logdet_exact"] == "log(92160000)", "exact oriented string mismatch")
    require(
        math.isclose(values["oriented_abs_sector_logdet_numeric"], math.log(92160000), rel_tol=0.0, abs_tol=1e-12),
        "oriented numeric log mismatch",
    )

    require(
        next_contract["status"] == "NEXT_IS_SOURCEOWNED_POSITIVE_OPERATOR_OR_EQA_PAYLOAD_FILL",
        "next contract status mismatch",
    )
    require(any("source-owned positive Phi_fin" in item for item in next_contract["must_emit_one_of"]), "source-owned target missing")
    require(any("smooth E_Qa" in item for item in next_contract["must_emit_one_of"]), "smooth E_Qa target missing")
    require("declare the oriented 27-mode table source-owned by naming alone" in next_contract["must_not_use"], "naming guard missing")

    require("oriented abs finitepart" in note, "note missing finitepart summary")
    require(NEXT in note, "note missing next artifact")

    print("Torsional Weitzenbock / OU source-derivation audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
