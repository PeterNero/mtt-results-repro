from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREVIOUS = ROOT / "certificates" / "selected_end0_basis_table_or_bn_identification_import_certificate.json"
SM_CANDIDATE = SM / "candidate_data" / "selected_end0_direct_differential_table_from_ah_ext_forms.candidate.json"
SM_CERT = SM / "certificates" / "selected_end0_direct_differential_table_from_ah_ext_forms_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_end0_direct_ah_ext_form_table_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_end0_direct_ah_ext_form_table_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_End0_Direct_AH_Ext_Form_Table_Import_v1.md"

STATUS = "SELECTED_END0_DIRECT_AH_EXT_FORM_TABLE_IMPORTED_NORMALIZED_EXT_TABLE_OPEN"
NEXT = "MTT_Selected_Normalized_Ext_Local_Form_Table_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    sm_candidate = load(SM_CANDIDATE)
    sm_cert = load(SM_CERT)

    ext_template = sm_candidate["Ext_local_form_template"]
    end0_table = sm_candidate["partial_End0_differential_table"]
    newton = sm_candidate["newton_readiness"]
    source = sm_candidate["selected_source_boundary"]

    packet = {
        "theorem": {
            "name": "SelectedEnd0DirectAHExtFormTableImport",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The direct End_0(V_alpha) route is advanced from a path choice "
                "to a symbolic AH/Ext local-form operator template. The selected "
                "ordered AH layer, Appell-Humbert L^2 transition seed, and closed "
                "non-exact first Ext slot supply eta = theta_plus_0(z1) tensor "
                "eta_minus_0(z2) dbar_z2. This is not a Newton-ready numerical "
                "table; the next required object is the normalized selected Ext "
                "local-form table and the HYM/Hodge/quadrature/projector data."
            ),
        },
        "imported_statuses": {
            "previous_gate": previous["status"],
            "sm_direct_ah_ext": sm_cert["status"],
        },
        "selected_source_boundary": source,
        "AH_transition_seed": sm_candidate["AH_transition_seed"],
        "Ext_local_form_template": ext_template,
        "partial_End0_differential_table": end0_table,
        "newton_readiness": newton,
        "what_closes_now": {
            "previous_gate_reduced_to_direct_AH_Ext_route": previous["next_required_artifact"]
            == "MTT_Selected_End0_Direct_Differential_Table_From_AH_Ext_Forms_v1",
            "selected_AH_source_layer_imported": source["selected_AH_source_layer_imported"] is True,
            "appell_humbert_L2_transition_seed_recorded": sm_candidate["what_closes_now"][
                "AH_transition_seed_for_L2_recorded"
            ]
            is True,
            "selected_symbolic_Ext_local_form_template_built": sm_cert[
                "selected_symbolic_Ext_local_form_template_built"
            ]
            is True,
            "direct_End0_operator_template_built": sm_candidate["what_closes_now"][
                "direct_End0_operator_template_built"
            ]
            is True,
            "newton_first_blocker_identified": sm_cert["first_blocker"]
            == "selected_normalized_local_form_table_for_theta_plus_0_tensor_eta_minus_0",
            "target_fitting_excluded": sm_cert["target_fitting_used"] is False
            and sm_candidate["target_fitting_used"] is False,
        },
        "what_remains_open": {
            "normalized_theta_eta_local_form_table": sm_candidate["what_remains_open"][
                "normalized_theta_eta_local_form_table"
            ],
            "raw_good_cover_transition_functions_or_equivalent_Dolbeault_representative": sm_candidate[
                "what_remains_open"
            ]["raw_good_cover_transition_functions_or_equivalent_Dolbeault_representative"],
            "selected_HYM_metric_connection_correction": sm_candidate["what_remains_open"][
                "selected_HYM_metric_connection_correction"
            ],
            "Hodge_Lambda_quadrature_gauge_projector_tables": sm_candidate["what_remains_open"][
                "Hodge_Lambda_quadrature_gauge_projector_tables"
            ],
            "selected_Newton_Galerkin_coefficients": sm_candidate["what_remains_open"][
                "selected_Newton_Galerkin_coefficients"
            ],
        },
        "guardrails": {
            "symbolic_ext_form_not_used_as_numeric_table": ext_template["not_yet_numeric_local_form"] is True,
            "newton_not_claimed_ready": newton["ready"] is False and end0_table["safe_to_use_for_newton"] is False,
            "B_N_remains_scaffold_only": True,
            "no_observed_or_benchmark_data": True,
        },
        "next_required_artifact": NEXT,
        "input_certificates": {
            "previous": str(PREVIOUS),
            "sm_direct_ah_ext": str(SM_CERT),
        },
    }

    checks = {
        "previous_status_matches": previous["status"]
        == "SELECTED_END0_BN_IDENTIFICATION_REJECTED_DIRECT_TABLE_REDUCED_TO_AH_EXT_LOCAL_FORMS",
        "sm_status_matches": sm_cert["status"]
        == "MTT_SELECTED_END0_DIRECT_TABLE_PARTIAL_AH_EXT_FORM_TEMPLATE_BUILT_HYM_TABLES_OPEN",
        "symbolic_ext_slot_correct": ext_template["selected_basis_slot"] == "theta_plus_0_tensor_eta_minus_0",
        "symbolic_ext_form_correct": ext_template["symbolic_representative"]
        == "theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2",
        "central_shared_circle_degree_zero": sm_candidate["AH_transition_seed"][
            "central_shared_circle_degree_zero"
        ]
        is True,
        "newton_blocked": newton["ready"] is False,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_end0_direct_ah_ext_form_table_import",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected End0 Direct AH/Ext Form Table Import v1

## Result

The direct `End_0(V_alpha)` route advances one step.

The selected symbolic local-form bridge is:

```text
eta = theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2
```

This is the first Ext slot `theta_plus_0_tensor_eta_minus_0` in the selected
`H^1(X,L^2)` packet, with Appell-Humbert transition seed `L^2=(2,-4,0)` and
central shared-circle degree zero.

The partial operator template is:

```text
barpartial_End0 = barpartial_Iwasawa + ad(A_split_AH + eta_offdiag + HYM_correction)
```

This is not yet a Newton-ready numerical table. The Ext representative is still
symbolic and must be normalized into an overlap-compatible local table before it
can supply selected coefficients.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
