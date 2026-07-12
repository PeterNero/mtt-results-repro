"""Build the Qa/SU3 gerbe-twisted local-system response interface."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

DECISION = DATA / "endomorphism_or_local_system_torsion_decision.candidate.json"
GERBE_TWIST = DATA / "gerbe_twist_cancellation_packet.candidate.json"
MINIMAL = DATA / "minimal_closing_source_data_request.candidate.json"

OUTPUT_DATA = DATA / "gerbe_twisted_local_system_response_interface.candidate.json"
OUTPUT_CERT = CERTS / "gerbe_twisted_local_system_response_interface_certificate.json"
OUTPUT_TEMPLATE = CERTS / "gerbe_twisted_local_system_response.template.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Gerbe_Twisted_Local_System_Response_Interface_v1.md"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def open_template(pair_results: list[dict[str, object]], p_sector: dict[str, object]) -> dict[str, object]:
    return {
        "status": "OPEN_SELECTED_QA_SU3_GERBE_TWISTED_LOCAL_SYSTEM_RESPONSE_REQUIRED",
        "source_certificate": {
            "source_identity": None,
            "same_branch_Qa_SU3_selection_rule": None,
            "forbidden_target_fitting_absent": None,
        },
        "gerbe_or_local_system": {
            "Deligne_Cech_or_B_field_representative": None,
            "finite_quotient_or_smooth_lift": None,
            "rho_E_local_system_representation": None,
            "c_twist_generator_action": None,
        },
        "twisted_sections": {
            "P_sector": p_sector,
            "pair_results_expected": pair_results,
            "section_bases_FG_P": None,
            "twisted_multiplication_constants": None,
            "machine_check_g_f_zero": None,
        },
        "admissibility": {
            "Freed_Witten_check": None,
            "Green_Schwarz_Bianchi_check": None,
            "stability_or_HYM_policy": None,
            "projector_retention_policy": None,
            "zero_mode_policy": None,
        },
        "finite_response": {
            "D_E": None,
            "rho_E": None,
            "heat_or_zeta_finite_part": None,
            "analytic_or_Reidemeister_torsion": None,
            "trace_normalization": None,
        },
    }


def build() -> tuple[dict[str, object], dict[str, object], dict[str, object], str]:
    decision = load(DECISION)
    gerbe = load(GERBE_TWIST)
    minimal = load(MINIMAL)
    template = open_template(gerbe["pair_results"], gerbe["P"])
    interface_checks = {
        "primary_route_confirmed": decision["decision"]["primary_next_lane"] == "projective_gerbe_twisted_module_response",
        "all_pair_twists_cancel": all(item["gerbe_twist_cancels"] for item in gerbe["pair_results"]),
        "all_products_land_in_P": all(item["product_matches_P"] for item in gerbe["pair_results"]),
        "template_requires_source_identity": template["source_certificate"]["source_identity"] is None,
        "template_requires_finite_response": all(value is None for value in template["finite_response"].values()),
        "minimal_request_included": minimal["status"],
    }
    candidate = {
        "candidate": "SelectedQaSU3GerbeTwistedLocalSystemResponseInterface",
        "status": "QA_SU3_GERBE_TWISTED_LOCAL_SYSTEM_RESPONSE_INTERFACE_BUILT_VALUES_OPEN",
        "input_status": {
            "decision": decision["status"],
            "gerbe_twist": gerbe["status"],
            "minimal_request": minimal["status"],
        },
        "interface_checks": interface_checks,
        "template_path": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "required_packet": template,
        "acceptance_rule": [
            "fill source_certificate without target residuals",
            "supply selected Deligne/Cech, B-field, or rho_E local-system data",
            "supply section bases and twisted multiplication constants for all F_i,G_i,P",
            "machine-check c-twist cancellation and g*f=0",
            "pass Freed-Witten, Bianchi, projector, zero-mode, and trace policies",
            "compute one finite response from D_E, rho_E, heat/zeta, or torsion",
        ],
        "rejected_shortcuts": [
            "using q79 torsion as direct Qa/SU3 data",
            "using Repair B as proof without source erratum",
            "choosing multiplication constants to fit a target threshold",
            "claiming gerbe existence without a representative and module action",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "Selected_Qa_SU3_Gerbe_Twisted_Local_System_Response_Fill_Attempt_v1",
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "template_path": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "what_closes": {
            "strict_interface_built": True,
            "twist_cancellation_table_imported": True,
            "minimal_finite_response_requirements_imported": True,
        },
        "what_remains_open": {
            "selected_source_identity": True,
            "selected_gerbe_or_local_system_data": True,
            "twisted_section_bases_and_constants": True,
            "finite_response": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 Gerbe-Twisted Local-System Response Interface v1

This interface is the concrete packet required by the route decision.

## What Is Already Fixed

The c-twist bookkeeping is not arbitrary:

```text
c(F_i) + c(G_i) = c(P) = 0
```

for all five monad products. Thus the literal nonclosed `c` obstruction is
handled by twisted-module typing rather than by pretending `c` is an ordinary
closed line-bundle class.

## What Must Be Filled

The open template requires:

```text
source identity and same-branch selection rule,
selected Deligne/Cech, B-field, or rho_E local-system data,
section bases for F_i, G_i, and P,
twisted multiplication constants,
machine-check of g*f=0,
Freed-Witten and Green-Schwarz/Bianchi checks,
projector and zero-mode policy,
trace normalization,
and one finite response: D_E, rho_E, heat/zeta, or torsion.
```

## Guardrail

The interface rejects q79 torsion import, unsourced Repair B, and fitted
constants. The next step is a fill attempt against the corpus or an amended
source packet.

Next required artifact:

```text
{candidate["next_required_artifact"]}
```

closure claimed: no
target fitting used: no
"""
    return candidate, certificate, template, note


def main() -> None:
    candidate, certificate, template, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    template_text = json.dumps(template, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(template_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
