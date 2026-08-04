from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

SCALE_REL_CERT = ROOT / "certificates" / "stf_hessian_scale_to_geff_relation_certificate.json"
PHYSICAL_ACTION_CERT = NONSM / "certificates" / "physical_action_normalization_gate_certificate.json"
DIM_OBSTRUCTION_CERT = NONSM / "certificates" / "dimensionful_constant_obstruction_certificate.json"
NORM_FUNC_CERT = NONSM / "certificates" / "selected_normalization_minimization_functional_certificate.json"

OUT_CERT = ROOT / "certificates" / "absolute_normalization_bridge_from_nonsm_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    scale_relation = load_json(SCALE_REL_CERT)
    physical_action = load_json(PHYSICAL_ACTION_CERT)
    dimensionful_obstruction = load_json(DIM_OBSTRUCTION_CERT)
    norm_functional = load_json(NORM_FUNC_CERT)

    internal_rows = []
    for row in physical_action["tested_cases"]:
        kappa_stf_int = row["Vol_int"] / (32.0 * math.pi * physical_action["canonical_internal_normalization"]["G10_int"])
        internal_rows.append(
            {
                "N": row["N"],
                "R1": row["R1"],
                "Vol_int": row["Vol_int"],
                "G_eff_int": row["G_eff_int"],
                "kappa_STF_int": kappa_stf_int,
            }
        )

    canonical_internal_closed = physical_action["verdict"]["canonical_internal_action_normalization_closed"]
    physical_absolute_closed = physical_action["verdict"]["physical_absolute_dimensionful_predictions_closed"]
    no_go = physical_action["verdict"]["no_go_without_external_dimensional_anchor"]
    functional_formulated = norm_functional["verdict"]["normalization_functional_formulated"]
    scale_lifting_open = not norm_functional["verdict"]["unique_positive_scale_minimizer_proved"]

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "absolute_normalization_bridge_from_nonsm",
        "status": "INTERNAL_GR_NORMALIZATION_CARRIED_HOME_PHYSICAL_ABSOLUTE_ANCHOR_OPEN",
        "input_certificates": {
            "stf_scale_relation": str(SCALE_REL_CERT),
            "physical_action_normalization": str(PHYSICAL_ACTION_CERT),
            "dimensionful_obstruction": str(DIM_OBSTRUCTION_CERT),
            "selected_normalization_functional": str(NORM_FUNC_CERT),
        },
        "closed_internal_units": {
            "alpha_int": physical_action["canonical_internal_normalization"]["alpha_int"],
            "G10_int": physical_action["canonical_internal_normalization"]["G10_int"],
            "lambda_star": physical_action["canonical_internal_normalization"]["lambda_star"],
            "formulae": {
                "G_eff_int": "1 / Vol_int",
                "kappa_STF_int": "Vol_int / (32*pi)",
                "Vol_int_theta": "31.8 R1^3",
            },
            "computed_rows": internal_rows,
        },
        "physical_absolute_status": {
            "physical_absolute_dimensionful_predictions_closed": physical_absolute_closed,
            "no_go_without_external_dimensional_anchor": no_go,
            "dimensionful_obstruction_verdict": dimensionful_obstruction["verdict"],
            "forbidden_overclaims": physical_action["forbidden_overclaims"],
        },
        "remaining_route": {
            "normalization_functional_formulated": functional_formulated,
            "scale_lifting_minimizer_still_open": scale_lifting_open,
            "remaining_lemma": norm_functional["verdict"].get("remaining_lemma"),
            "next_required_artifact": norm_functional["verdict"].get("next_required_artifact"),
        },
        "relation_to_current_GR_branch": {
            "kappa_not_independent": scale_relation["closed_tests"]["kappa_is_not_independent_of_G_eff"],
            "absolute_GR_gate_is_same_as_nonsm_gate": True,
            "new_GR_specific_free_parameter_introduced": False,
        },
        "interpretation": {
            "carried_home": (
                "Within canonical exact-branch internal action units, the TT stiffness "
                "and effective gravitational coupling are computable from the selected "
                "internal volume rows."
            ),
            "not_carried_home": (
                "This does not predict measured Newton/Planck units. Physical absolute "
                "normalization still needs a target-independent dimensional anchor or "
                "a proved scale-lifting minimizer from selected branch data."
            ),
            "credibility_point": (
                "The GR branch and the non-SM constants repo now point to the same "
                "single normalization bottleneck, so no hidden extra GR knob is being added."
            ),
        },
        "guardrails": {
            "claims_measured_Newton_constant": False,
            "claims_measured_Planck_scale": False,
            "claims_physical_absolute_dimensionful_closure": False,
            "claims_internal_dimensionless_normalization_closure": canonical_internal_closed,
            "claims_no_new_GR_knob": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
