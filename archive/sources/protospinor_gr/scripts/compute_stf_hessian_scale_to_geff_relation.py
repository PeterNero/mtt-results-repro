from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FORM_CERT = ROOT / "certificates" / "selected_stf_hessian_form_certificate.json"
KERNEL_CERT = ROOT / "certificates" / "selected_gr_hessian_kernel_candidate_certificate.json"
BLOCK_CERT = ROOT / "certificates" / "selected_gr_hessian_block_source_theorem_certificate.json"
BLOCK_TEMPLATE = ROOT / "candidate_data" / "selected_gr_hessian_block_source.template.json"
OUT_CERT = ROOT / "certificates" / "stf_hessian_scale_to_geff_relation_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    form = load_json(FORM_CERT)
    kernel = load_json(KERNEL_CERT)
    block = load_json(BLOCK_CERT)
    template = load_json(BLOCK_TEMPLATE)

    target = kernel["target_kernel"]

    geff_relation_available = (
        target["quadratic_action_target"]
        == "(32*pi*G_eff)^(-1) <h_TT, E_TT h_TT> plus gauge-fixing/ghost blocks"
    )
    geff_inverse_template_available = template["normalization"]["G_eff_inverse"] == "V_int/G_10"
    form_closed = form["closed_tests"]["hessian_form_closed"]

    relation_closed = form_closed and geff_relation_available and geff_inverse_template_available

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "stf_hessian_scale_to_geff_relation",
        "status": "STF_HESSIAN_SCALE_TIED_TO_GEFF_ABSOLUTE_NORMALIZATION_OPEN",
        "input_certificates": {
            "selected_stf_hessian_form": form["status"],
            "selected_gr_hessian_kernel_candidate": kernel["status"],
            "selected_gr_hessian_block_source_theorem": block["status"],
        },
        "relation": {
            "hessian_form": "H_TT = kappa_STF I_2",
            "quadratic_action_convention": target["quadratic_action_target"],
            "kappa_STF_relation": "kappa_STF = (32*pi*G_eff)^(-1)",
            "G_eff_inverse_relation": "G_eff^(-1) = V_int/G_10",
            "combined_relation": "kappa_STF = V_int/(32*pi*G_10)",
            "convention_note": (
                "The numerical 32*pi factor follows the repository's existing "
                "TT quadratic-action target convention. Changing the normalization "
                "of h_TT rescales kappa_STF and the TT inner product together."
            ),
        },
        "closed_tests": {
            "hessian_form_closed": form_closed,
            "kernel_target_supplies_quadratic_action_convention": geff_relation_available,
            "block_template_supplies_G_eff_inverse_relation": geff_inverse_template_available,
            "kappa_is_not_independent_of_G_eff": relation_closed,
        },
        "open_tests": {
            "V_int_selected_numerically": False,
            "G_10_selected_numerically": False,
            "absolute_G_eff_computed_without_observed_Newton_input": False,
            "absolute_kappa_STF_computed_without_observed_GR_input": False,
        },
        "interpretation": {
            "closed": (
                "The TT Hessian stiffness is not an additional knob. In the selected "
                "Einstein-Hilbert target convention it is the same normalization as "
                "G_eff, equivalently V_int/G_10."
            ),
            "not_closed": (
                "The absolute value of V_int/G_10 is still not computed from selected "
                "MTT data in this repository."
            ),
            "next_gate": "absolute_G_eff_or_Vint_over_G10_selection_certificate",
        },
        "guardrails": {
            "claims_numeric_G_eff": False,
            "claims_numeric_kappa_STF": False,
            "claims_new_independent_GR_knob": False,
            "claims_full_GR_closed": False,
            "claims_scale_relation_closed": relation_closed,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
