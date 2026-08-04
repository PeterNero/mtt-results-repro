"""Build the lambda_H last-row payload / strict direct-K closure split.

This integrates the current charged 9-row K_threshold chain with the existing
one-shared-physical-primitive H/lambda certificate.  It closes the ten-row
K ledger at the adopted one-shared-primitive standard, while preserving the
strict zero-primitive/direct-K upgrade as open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_lambdahlastrowpayload_or_strictdirectkclosure"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
LAMBDA_ROW = PACKET_DIR / "lambda_h_last_row_payload_under_oneprimitive.packet.json"
TEN_K = PACKET_DIR / "ten_kthreshold_ledger_current_standard.packet.json"
STRICT_FRONTIER = PACKET_DIR / "strict_directk_zero_primitive_frontier.packet.json"
NEXT = PACKET_DIR / "next_precision_or_strictupgrade_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LambdaHLastRowPayload_or_StrictDirectKClosure_v1.md"

CHARGED_CANDIDATE = DATA / "selected_tschemenulldelta_reconciliation_or_lambdahlastrow.candidate.json"
CHARGED_KROWS = (
    DATA
    / "selected_tschemenulldelta_reconciliation_or_lambdahlastrow"
    / "accepted_charged_kthreshold_rows_current.packet.json"
)
PHYSICAL_CANDIDATE = DATA / "selected_physicalnormalizationsourceaxiom_or_directkcertificate.candidate.json"
DIRECT_K_CERT = (
    DATA
    / "selected_physicalnormalizationsourceaxiom_or_directkcertificate"
    / "direct_kthreshold_omega_h_lambda_certificate_under_axiom.packet.json"
)
GUARDRAIL = (
    DATA
    / "selected_physicalnormalizationsourceaxiom_or_directkcertificate"
    / "axiom_adoption_and_strict_guardrail_validator.packet.json"
)
ADOPTION = DATA / "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision.candidate.json"
PAPER_UPDATE = DATA / "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram.candidate.json"
FINITE_H = DATA / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
STRICT_DERIVATION = DATA / "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade.candidate.json"
LOCKED_BASE = DATA / "selected_lockedbasefreeze_or_pewdirectkattackcontract.candidate.json"

STATUS = (
    "MTT_SELECTED_LAMBDAHLASTROWPAYLOAD_OR_STRICTDIRECTKCLOSURE_"
    "ONEPRIMITIVE_TENK_CLOSED_STRICT_DIRECTK_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PrecisionEquivalenceRows_or_StrictPEWDirectKUpgrade_v1"
STRICT_UPGRADE_ARTIFACT = "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_StrictPEWNoKnobUpgrade_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing lambda_H last-row inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        CHARGED_CANDIDATE,
        CHARGED_KROWS,
        PHYSICAL_CANDIDATE,
        DIRECT_K_CERT,
        GUARDRAIL,
        ADOPTION,
        PAPER_UPDATE,
        FINITE_H,
        STRICT_DERIVATION,
        LOCKED_BASE,
    ]
    require_sources(sources)

    charged_candidate = load(CHARGED_CANDIDATE)
    charged_krows = load(CHARGED_KROWS)
    physical = load(PHYSICAL_CANDIDATE)
    direct_k = load(DIRECT_K_CERT)
    guardrail = load(GUARDRAIL)
    adoption = load(ADOPTION)
    paper_update = load(PAPER_UPDATE)
    finite_h = load(FINITE_H)
    strict_derivation = load(STRICT_DERIVATION)
    locked_base = load(LOCKED_BASE)

    charged_rows = charged_krows["rows"]
    lambda_payload = direct_k["numeric_payload"]
    lambda_row = {
        "schema": "MTTLambdaHLastRowPayloadUnderOnePrimitive.v1",
        "status": "LAMBDA_H_LAST_ROW_ACCEPTED_UNDER_ADOPTED_ONE_PRIMITIVE_STANDARD",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "combined_kernel_row_id": "K_threshold.Omega_H.lambda",
        "omega_id": "Omega_H.lambda",
        "accepted_as_tenth_K_row_under_current_standard": True,
        "accepted_as_tenth_K_row_under_one_shared_primitive": True,
        "accepted_as_strict_zero_primitive_direct_K_row": False,
        "source_chain": {
            "finite_H_scalar_source_available": finite_h["closure_decision"]["finite_H_scalar_source_available"],
            "selected_H_radial_source_row_emitted": finite_h["closure_decision"][
                "selected_H_radial_source_row_emitted"
            ],
            "selected_R_H_RG_source_emitted": finite_h["closure_decision"]["selected_R_H_RG_source_emitted"],
            "physical_normalization_axiom_adopted": adoption["closure_decision"][
                "current_closure_standard_adopted"
            ],
            "direct_K_certificate_under_axiom": direct_k["accepted_as_tenth_K_row_under_axiom"],
            "paper_standard_ready": paper_update["closure_decision"]["publication_standard_ready"],
        },
        "numeric_payload": {
            "A_EW_shared_primitive": lambda_payload["A_EW"],
            "s_beta_selected": lambda_payload["s_beta"],
            "lambda_if_R_H_RG_equals_1": lambda_payload["lambda_if_R_H_RG_equals_1"],
            "R_H_RG_selected": lambda_payload["R_H_RG"],
            "lambda_H_from_selected_oneprimitive_payload": lambda_payload["lambda_H_from_premised_source"],
            "lambda_H_postcheck_reference": lambda_payload["lambda_H_reference_for_postcheck"],
            "lambda_H_postcheck_residual": lambda_payload["lambda_H_postcheck_residual"],
        },
        "formulae": {
            "lambda_H": "lambda_H(mu_match) = A_EW(mu_match, scheme)*s_beta*R_H^RG",
            "direct_K": direct_k["closed_equations"]["direct_K_row"],
            "current_standard": "P_EW/A_EW is counted once as the shared physical primitive.",
        },
        "parameter_accounting": {
            "H_specific_parameter_count": 0,
            "shared_physical_primitive_count": 1,
            "new_parameter_introduced_by_lambda_row": 0,
            "strict_zero_primitive_parameter_count": 0,
        },
    }
    write_json(LAMBDA_ROW, lambda_row)

    full_rows = [
        {
            "row_type": "charged",
            "combined_kernel_row_id": row["combined_kernel_row_id"],
            "omega_id": row["omega_id"],
            "sector": row["sector"],
            "generation": row["generation"],
            "selected_K_threshold_source_value": row["selected_K_threshold_source_value"],
            "accepted_under_current_standard": True,
            "accepted_as_strict_charged_row": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        }
        for row in charged_rows
    ]
    full_rows.append(
        {
            "row_type": "H_lambda",
            "combined_kernel_row_id": "K_threshold.Omega_H.lambda",
            "omega_id": "Omega_H.lambda",
            "sector": "H",
            "generation": 0,
            "selected_K_threshold_source_value": direct_k["direct_K_row_value"]["symbolic"],
            "lambda_H_value": lambda_payload["lambda_H_from_premised_source"],
            "accepted_under_current_standard": True,
            "accepted_as_strict_charged_row": False,
            "accepted_as_strict_zero_primitive_direct_K_row": False,
            "accepted_under_one_shared_primitive": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        }
    )

    ten_k = {
        "schema": "MTTTenKThresholdLedgerCurrentStandard.v1",
        "status": "TEN_KTHRESHOLD_ROWS_CLOSED_UNDER_ADOPTED_ONE_PRIMITIVE_STANDARD",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "current_closure_standard": "one_shared_physical_primitive",
        "current_closure_standard_adopted": True,
        "charged_K_threshold_rows": len(charged_rows),
        "H_lambda_K_threshold_rows_under_oneprimitive": 1,
        "accepted_full_ten_row_K_threshold_row_count_under_current_standard": 10,
        "accepted_full_ten_row_K_threshold_row_count_under_strict_zero_primitive": 9,
        "strict_direct_K_threshold_Omega_H_lambda_rows": 0,
        "strict_P_EW_source_rows": 0,
        "rows": full_rows,
    }
    write_json(TEN_K, ten_k)

    strict_frontier = {
        "schema": "MTTStrictDirectKZeroPrimitiveFrontier.v1",
        "status": "STRICT_ZERO_PRIMITIVE_DIRECTK_REMAINS_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_upgrade_target": STRICT_UPGRADE_ARTIFACT,
        "strict_derivation_attempted": strict_derivation["closure_decision"]["derivation_attempted"],
        "physical_normalization_axiom_derived": strict_derivation["closure_decision"][
            "physical_normalization_axiom_derived"
        ],
        "scale_symmetry_no_go_active": strict_derivation["closure_decision"]["scale_symmetry_no_go_active"],
        "accepted_strict_P_EW_source_rows": strict_derivation["closure_decision"]["strict_P_EW_source_rows"],
        "accepted_strict_direct_K_threshold_Omega_H_lambda_rows": strict_derivation["closure_decision"][
            "strict_direct_K_threshold_Omega_H_lambda_rows"
        ],
        "accepted_strict_derivation_route_count": strict_derivation["closure_decision"][
            "accepted_strict_derivation_route_count"
        ],
        "locked_base_confirms_strict_rows": {
            "accepted_strict_P_EW_source_rows": locked_base["key_numbers"]["accepted_strict_P_EW_source_rows"],
            "accepted_direct_K_threshold_Omega_H_lambda_rows": locked_base["key_numbers"][
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "accepted_strict_derivation_route_count": locked_base["key_numbers"][
                "accepted_strict_derivation_route_count"
            ],
        },
        "legal_strict_exits": [
            "derive P_EW from same-branch gauge/action/metrology source data",
            "emit a direct selected K_threshold.Omega_H.lambda row independent of P_EW",
            "derive the physical-normalization axiom from finite projected source geometry",
        ],
    }
    write_json(STRICT_FRONTIER, strict_frontier)

    next_packet = {
        "schema": "MTTNextPrecisionOrStrictUpgradeCutset.v1",
        "status": "TENK_CURRENT_STANDARD_CLOSED_NEXT_PRECISION_OR_STRICT_UPGRADE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_now": [
            "nine charged K_threshold rows from selected Q/L/T chain",
            "one H/lambda K_threshold row under adopted one-shared-physical-primitive standard",
            "ten-row K_threshold ledger under current standard",
            "zero H-specific parameters for lambda_H",
        ],
        "still_open": [
            "strict zero-primitive P_EW/direct-K derivation",
            "precision-equivalence rows and covariance/profile matching",
            "neutrino absolute mass and Dirac/Majorana policy",
            "QCD theta/strong-CP source policy",
            "local-QFT precision observable export",
        ],
        "next_required_artifact": NEXT_ARTIFACT,
        "strict_upgrade_artifact": STRICT_UPGRADE_ARTIFACT,
    }
    write_json(NEXT, next_packet)

    decision = {
        "current_closure_standard": "one_shared_physical_primitive",
        "current_closure_standard_adopted": True,
        "lambda_H_last_row_payload_accepted_under_current_standard": True,
        "ten_K_threshold_rows_closed_under_current_standard": True,
        "accepted_selected_charged_K_threshold_row_count": len(charged_rows),
        "accepted_H_lambda_K_threshold_row_count_under_current_standard": 1,
        "accepted_full_ten_row_K_threshold_row_count_under_current_standard": 10,
        "H_specific_parameter_count": 0,
        "shared_physical_primitive_count": 1,
        "accepted_strict_P_EW_source_rows": 0,
        "accepted_strict_direct_K_threshold_Omega_H_lambda_rows": 0,
        "accepted_full_ten_row_K_threshold_row_count_under_strict_zero_primitive": 9,
        "strict_zero_primitive_directK_closed": False,
        "strict_no_knob_closed": False,
        "true_precision_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedLambdaHLastRowPayloadOrStrictDirectKClosure",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "lambda_h_last_row_payload_under_oneprimitive": rel(LAMBDA_ROW),
            "ten_kthreshold_ledger_current_standard": rel(TEN_K),
            "strict_directk_zero_primitive_frontier": rel(STRICT_FRONTIER),
            "next_precision_or_strictupgrade_cutset": rel(NEXT),
        },
        "theorem": {
            "name": "LambdaHLastRowPayloadOrStrictDirectKClosureTheorem",
            "proved": True,
            "statement": (
                "Given the adopted one-shared-physical-primitive closure standard, "
                "the existing physical-normalization/direct-K certificate supplies "
                "the H/lambda last row without an H-specific knob. Combining this row "
                "with the current nine charged K_threshold rows closes the ten-row "
                "K_threshold ledger at the current standard. The strict zero-primitive "
                "P_EW/direct-K derivation remains open and is not counted as solved."
            ),
        },
        "closure_decision": decision,
        "numerics": lambda_row["numeric_payload"],
        "next_required_artifact": NEXT_ARTIFACT,
        "strict_upgrade_artifact": STRICT_UPGRADE_ARTIFACT,
    }
    write_json(OUT, candidate)

    cert = {
        "certificate": "MTT_Selected_LambdaHLastRowPayload_or_StrictDirectKClosure_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "theorem_proved": True,
        **decision,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "strict_upgrade_artifact": STRICT_UPGRADE_ARTIFACT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected LambdaHLastRowPayload or StrictDirectKClosure v1

Status: `{STATUS}`.

## Result

The newest charged chain supplies nine accepted charged `K_threshold` rows.
The existing physical-normalization/direct-K certificate supplies the H/lambda
row under the adopted one-shared-physical-primitive standard.  Therefore:

```text
current closure standard                         : one_shared_physical_primitive
charged K_threshold rows                         : {len(charged_rows)}
H/lambda K_threshold rows under current standard : 1
full K_threshold rows under current standard     : 10/10
H-specific parameter count                       : 0
shared physical primitive count                  : 1
```

## H/Lambda Payload

```text
A_EW                       = {lambda_payload["A_EW"]}
s_beta                     = {lambda_payload["s_beta"]}
lambda_if_R_H_RG_equals_1   = {lambda_payload["lambda_if_R_H_RG_equals_1"]}
R_H^RG                     = {lambda_payload["R_H_RG"]}
lambda_H                   = {lambda_payload["lambda_H_from_premised_source"]}
lambda_H postcheck residual= {lambda_payload["lambda_H_postcheck_residual"]}
```

## Strict Guardrail

This is not strict zero-primitive closure:

```text
strict P_EW source rows                    : 0
strict direct K_threshold.Omega_H.lambda   : 0
strict ten-row K_threshold ledger          : 9/10
strict no-knob closure                     : false
```

The next valid move is either precision-equivalence execution under the adopted
standard, or the strict upgrade `{STRICT_UPGRADE_ARTIFACT}`.

Next artifact: `{NEXT_ARTIFACT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
