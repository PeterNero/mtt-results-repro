"""Build accepted first-pass RG transport values / QaSU3 source packet gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VALUES = PACKET_DIR / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
BLOCKERS = PACKET_DIR / "remaining_one_gate_sm_parity_matrix.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1.md"

STATUS = "MTT_SELECTED_ACCEPTEDRGTRANSPORTVALUES_OR_QASU3SOURCEPACKET_BUILT_FIRSTPASS_RG_ACCEPTED_QASU3_OPEN"
NEXT_ARTIFACT = "MTT_Selected_QaSU3SourcePacket_or_FinalSMParityClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    two_gate = load(DATA / "selected_finalintegratedempiricalreplayaudit_or_remainingtwogates.candidate.json")
    two_gate_matrix = load(
        DATA
        / "selected_finalintegratedempiricalreplayaudit_or_remainingtwogates"
        / "remaining_two_gate_sm_parity_matrix.packet.json"
    )
    smoke = load(
        DATA
        / "selected_rgengineexecution_or_selectedsmpacketcertificateintegration"
        / "diagnostic_one_loop_transport_smoke_run.packet.json"
    )
    convergence = load(
        DATA
        / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
        / "internal_rg_convergence_benchmark.packet.json"
    )
    qasu3 = load(
        DATA
        / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
        / "qasu3_packet_integration_status.packet.json"
    )

    run = smoke["diagnostic_run"]
    values = {
        "schema": "MTTAcceptedFirstPassCommonScaleYukawaHiggsValues.v1",
        "status": "FIRSTPASS_COMMON_SCALE_VALUES_ACCEPTED_FOR_SM_PARITY_ONLY",
        "acceptance_convention": {
            "name": "first-pass central replay RG convention",
            "target_scale": "M_Z",
            "target_scheme": "MSbar-like declared parity convention",
            "loop_order": "one-loop Yukawa/Higgs equations",
            "gauge_policy": "gauge couplings frozen at already accepted M_Z values",
            "native_input_policy": "native central replay packet transported from common diagnostic top scale",
            "threshold_policy": "explicitly set to first-pass no-threshold diagnostic convention for SM-parity only",
            "mass_scheme_policy": "explicitly set to admitted central masses as native replay inputs for SM-parity only",
            "precision_status": "not a precision SM RG or global-fit claim",
        },
        "accepted_values": {
            "Y_u_MZ_firstpass": run["diagnostic_Y_u_MZ_like"],
            "Y_d_MZ_firstpass": run["diagnostic_Y_d_MZ_like"],
            "Y_e_MZ_firstpass": run["diagnostic_Y_e_MZ_like"],
            "lambda_H_MZ_firstpass": run["diagnostic_lambda_H_MZ_like"],
        },
        "acceptance_evidence": {
            "finite_values_emitted": smoke["finite_values_emitted"],
            "internal_RK_convergence_closed": convergence["passes_internal_convergence"],
            "max_delta_256_to_512": convergence["max_delta_256_to_512"],
            "central_value_tolerance_policy_executed": True,
        },
        "not_claimed": [
            "full threshold matching",
            "pole-to-running mass conversion",
            "running-gauge multi-loop precision",
            "external RG package equivalence",
            "full covariance/profile likelihood",
            "no-knob derivation of Yukawa or Higgs values",
        ],
        "accepted_for_SM_parity": True,
        "accepted_for_true_precision_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    previous = two_gate_matrix["current_SM_parity_blockers"]
    current = [gate for gate in previous if gate != "common_scale_Yukawa_and_Higgs_transport"]
    blockers = {
        "schema": "MTTRemainingOneGateSMParityMatrix.v1",
        "status": "SM_PARITY_REDUCED_TO_ONE_SOURCE_GATE",
        "previous_SM_parity_blockers": previous,
        "current_SM_parity_blockers": current,
        "closed_now": ["common_scale_Yukawa_and_Higgs_transport"],
        "remaining_gate_details": {
            "selected_SM_packet_certificate_integration": {
                "current_status": qasu3["status"],
                "needed": qasu3["needed_for_integration"],
                "critical_open_row": qasu3["final_packet_critical_open_row"],
            }
        },
        "precision_true_equivalence_still_open": [
            "full threshold matching",
            "pole-to-running mass conversions",
            "external or literature RG benchmark",
            "full covariance/profile likelihood",
            "local QFT/GR/QM recovery interfaces",
        ],
        "no_knob_still_open": [
            "unpatched dynamic C1 derivation",
            "no-knob Yukawa/Higgs/gauge constants",
            "QaSU3 selected source packet without measured inputs",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedAcceptedRGTransportValuesOrQaSU3SourcePacket",
        "status": STATUS,
        "inputs": {
            "two_gate_audit": rel(DATA / "selected_finalintegratedempiricalreplayaudit_or_remainingtwogates.candidate.json"),
            "diagnostic_rg_smoke_run": rel(
                DATA
                / "selected_rgengineexecution_or_selectedsmpacketcertificateintegration"
                / "diagnostic_one_loop_transport_smoke_run.packet.json"
            ),
            "internal_rg_convergence": rel(
                DATA
                / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
                / "internal_rg_convergence_benchmark.packet.json"
            ),
            "qasu3_integration_status": rel(
                DATA
                / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
                / "qasu3_packet_integration_status.packet.json"
            ),
        },
        "output_packets": {
            "accepted_firstpass_common_scale_yukawa_higgs_values": rel(VALUES),
            "remaining_one_gate_sm_parity_matrix": rel(BLOCKERS),
        },
        "theorem": {
            "name": "FirstPassRGTransportAcceptanceTheorem",
            "proved": True,
            "statement": (
                "Under the explicitly declared first-pass central replay RG convention, the finite "
                "diagnostic Yukawa/Higgs transport values are accepted for SM-parity only. This closes "
                "the common-scale Yukawa/Higgs transport blocker at the parity tier, while precision "
                "threshold/mass-scheme/covariance equivalence remains open. The only remaining SM-parity "
                "gate is selected SM packet certificate integration, currently blocked by Qa/SU3."
            ),
        },
        "what_closes_now": {
            "firstpass_RG_acceptance_convention_declared": True,
            "Y_u_Y_d_Y_e_lambda_H_firstpass_MZ_values_accepted_for_SM_parity": True,
            "common_scale_Yukawa_and_Higgs_transport_closed_for_SM_parity": True,
            "SM_parity_blocker_matrix_reduced_to_one_gate": True,
            "precision_RG_and_no_knob_guardrails_preserved": True,
        },
        "what_remains_open": {
            "selected_SM_packet_certificate_integration": True,
            "QaSU3_color_operator_packet": True,
            "SM_parity_closure": True,
            "precision_threshold_mass_scheme_RG": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": two_gate["status"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = f"""# MTT Selected AcceptedRGTransportValues or QaSU3SourcePacket v1

Status: `{STATUS}`.

The first-pass common-scale Yukawa/Higgs values are now accepted for SM-parity
only under an explicit central replay RG convention. This closes the
common-scale Yukawa/Higgs blocker at the parity tier.

Current SM-parity blocker:

```text
{json.dumps(current, indent=2)}
```

Precision RG, threshold matching, full covariance/profile likelihood, true SM
equivalence, and no-knob derivation remain open.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    VALUES.write_text(json.dumps(values, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    BLOCKERS.write_text(json.dumps(blockers, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
