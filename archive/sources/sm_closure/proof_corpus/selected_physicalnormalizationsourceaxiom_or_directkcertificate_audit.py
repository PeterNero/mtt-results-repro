"""Audit physical-normalization source axiom / direct-K certificate."""

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
BUILDER = ROOT / "scripts" / "build_selected_physicalnormalizationsourceaxiom_or_directkcertificate.py"

SLUG = "selected_physicalnormalizationsourceaxiom_or_directkcertificate"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalNormalizationSourceAxiom_or_DirectKCertificate_v1.md"

AXIOM_PACKET = PACKET_DIR / "physical_normalization_source_axiom.packet.json"
DIRECT_K_PACKET = PACKET_DIR / "direct_kthreshold_omega_h_lambda_certificate_under_axiom.packet.json"
VALIDATOR_PACKET = PACKET_DIR / "axiom_adoption_and_strict_guardrail_validator.packet.json"
NEXT_PACKET = PACKET_DIR / "next_derivation_or_paper_insertion_contract.packet.json"

STATUS = (
    "MTT_SELECTED_PHYSICALNORMALIZATIONSOURCEAXIOM_OR_DIRECTKCERTIFICATE_"
    "CONSTRUCTED_PREMISED_HK_CLOSURE_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_StrictPEWNoKnobUpgrade_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    axiom = load(AXIOM_PACKET)
    direct_k = load(DIRECT_K_PACKET)
    validator = load(VALIDATOR_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, axiom, direct_k, validator, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["physical_normalization_source_axiom_constructed"] is True, "axiom not constructed")
    require(
        decision["direct_K_threshold_Omega_H_lambda_certificate_constructed_under_axiom"] is True,
        "direct K certificate not constructed",
    )
    require(decision["premised_P_EW_source_rows"] == 1, "premised P_EW row count mismatch")
    require(decision["premised_direct_K_threshold_Omega_H_lambda_rows"] == 1, "premised K row mismatch")
    require(decision["premised_selected_K_row_count"] == 10, "premised ten-row count mismatch")
    require(decision["H_specific_parameter_count_under_axiom"] == 0, "H-specific parameter introduced")
    require(decision["shared_physical_primitive_count_under_axiom"] == 1, "shared primitive count mismatch")
    require(decision["accepted_strict_P_EW_source_rows"] == 0, "strict P_EW overaccepted")
    require(decision["accepted_strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "strict K overaccepted")
    require(decision["strict_no_knob_ten_row_closure"] is False, "strict ten-row overclosed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(
        axiom["status"] == "PHYSICAL_NORMALIZATION_SOURCE_AXIOM_CONSTRUCTED_NOT_DERIVED",
        "axiom status mismatch",
    )
    require(axiom["accepted_as_premised_source_axiom"] is True, "axiom premise not accepted")
    require(axiom["accepted_as_strict_no_knob_source"] is False, "axiom promoted as no-knob")
    require(axiom["parameter_increment_if_adopted"] == 1, "axiom parameter count mismatch")
    require("do not call this strict no-knob closure" in axiom["forbidden_uses"], "axiom guard missing")

    require(
        direct_k["status"] == "DIRECT_K_CERTIFICATE_CONSTRUCTED_UNDER_PHYSICAL_NORMALIZATION_AXIOM",
        "direct K status mismatch",
    )
    require(direct_k["accepted_as_tenth_K_row_under_axiom"] is True, "premised K row not accepted")
    require(direct_k["accepted_as_strict_no_knob_tenth_K_row"] is False, "strict K overaccepted")
    require(direct_k["ten_K_ledger_closed_under_axiom"] is True, "ten-row ledger not closed under axiom")
    require(direct_k["strict_no_knob_ten_K_closed"] is False, "strict ten-row overclosed")
    require(direct_k["premises"]["selected_s_beta_closed"] is True, "s_beta premise lost")
    require(direct_k["premises"]["selected_R_H_RG_closed"] is True, "R_H premise lost")
    require(direct_k["premises"]["D_fin_H_subfactor_closed"] is True, "D_fin support lost")
    require(direct_k["premises"]["theta_exponent_closed"] is True, "theta support lost")
    require(
        direct_k["direct_K_row_value"]["symbolic"] == "(A_EW*s_beta)/(D_fin.H*epsilon_Theta^(1/3))",
        "direct K symbolic formula mismatch",
    )

    require(
        validator["status"] == "PREMISED_CLOSURE_VALIDATED_STRICT_NOKNOB_GUARD_PRESERVED",
        "validator status mismatch",
    )
    require(validator["under_axiom"]["premised_selected_K_row_count"] == 10, "validator ten-row mismatch")
    require(validator["without_axiom"]["accepted_strict_P_EW_source_rows"] == 0, "validator P_EW overaccepted")
    require(
        validator["without_axiom"]["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0,
        "validator K overaccepted",
    )
    require(validator["without_axiom"]["strict_no_knob_ten_row_closure"] is False, "validator no-knob overclosed")

    require("premised selected K row count              : 10/10" in note, "note missing premised closure")
    require("strict no-knob ten-row closure             : false" in note, "note missing strict guard")
    require(NEXT in note, "note missing next artifact")

    print("Physical-normalization source axiom / direct-K certificate audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
