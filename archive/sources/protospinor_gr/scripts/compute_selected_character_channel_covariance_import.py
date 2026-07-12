from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

SOURCE_DATA = ROOT / "certificates" / "selected_higher_order_correction_and_disturbance_covariance_theorem_certificate.json"
CHAR_COV = NONSM / "certificates" / "selected_character_channel_covariance_closure_certificate.json"
FINAL_RHO = NONSM / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
FINAL_CHAR_RHO = NONSM / "certificates" / "final_selected_character_rho_uv_theorem_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_character_channel_covariance_import_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Character_Channel_Covariance_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    source_data = load(SOURCE_DATA)
    char_cov = load(CHAR_COV)
    final_rho = load(FINAL_RHO)
    final_char_rho = load(FINAL_CHAR_RHO)

    selected_values = final_rho["selected_values"]
    closed_on_branch = char_cov["closed_on_branch"]
    closed_formula = final_char_rho["closed_formula"]

    d_q = float(closed_on_branch["D_raw_norm_squared"])
    rho_uv = float(selected_values["rho_UV"])
    c_uv_norm = math.sqrt(rho_uv * d_q)

    imported_closures = {
        "source_data_gate_reduced": source_data["status"] == "SOURCE_DATA_THEOREM_REDUCED_TO_QTAU_CUV_AND_OMEGA0",
        "character_channel_covariance_closed": char_cov["verdict"]["character_channel_covariance_closed"],
        "D_raw_norm_squared_selected_character_branch": d_q == 1.0,
        "rho_uv_branch_function_closed": final_char_rho["verdict"]["rho_uv_branch_function_closed"],
        "final_internal_radius_closed": final_rho["closed"]["selected_internal_radius"],
        "final_internal_rho_uv_closed": final_rho["closed"]["selected_internal_rho_uv"],
        "selected_character_channel_covariance_used_by_final_branch": final_rho["closed"][
            "selected_character_channel_covariance"
        ],
    }

    internal_selected_data = {
        "selected_character": closed_on_branch["selected_character"],
        "selected_channel": closed_on_branch["selected_channel"],
        "covariance": closed_on_branch["covariance"],
        "retarded_kernel_action": closed_on_branch["retarded_kernel_action"],
        "D_raw_norm_squared_d_Q": d_q,
        "G_11": closed_on_branch["G_11"],
        "R_star": selected_values["R_star"],
        "v1_tilde": selected_values["v1_tilde"],
        "C_UV_norm_internal": c_uv_norm,
        "rho_UV": rho_uv,
        "s_star": selected_values["s_star_from_rho"],
        "rho_uv_R": final_rho["selected_branch"]["rho_uv_R"],
    }

    still_open = {
        "physical_Omega_0_selected": False,
        "physical_omega_gap_selected": False,
        "physical_Newton_or_Planck_predicted": False,
        "unconditional_all_covariance_models_closed": char_cov["verdict"][
            "unconditional_all_covariance_models_closed"
        ],
        "independent_higher_order_functional_evaluation_supplied_here": False,
    }

    guardrails = {
        "uses_unit_covariance_shortcut": False,
        "uses_rank_one_selected_character_projector": True,
        "imports_threshold_delta_as_covariance": False,
        "uses_observed_target_constant": False,
        "claims_unconditional_covariance_model": False,
        "claims_physical_units": False,
    }

    theorem_ready = all(imported_closures.values())
    physical_closed = theorem_ready and still_open["physical_Omega_0_selected"]
    status = (
        "INTERNAL_CHARACTER_CHANNEL_QTAU_AND_CUV_IMPORTED_OMEGA0_OPEN"
        if theorem_ready and not physical_closed
        else "PHYSICAL_SOURCE_DATA_CLOSED"
        if physical_closed
        else "CHARACTER_CHANNEL_IMPORT_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_character_channel_covariance_import",
        "status": status,
        "input_certificates": {
            "selected_higher_order_correction_and_disturbance_covariance_theorem": str(SOURCE_DATA),
            "selected_character_channel_covariance_closure": str(CHAR_COV),
            "final_selected_character_rho_uv_theorem": str(FINAL_CHAR_RHO),
            "final_internal_rho_uv_selected_radius_theorem": str(FINAL_RHO),
        },
        "imported_closures": imported_closures,
        "identification_premise": char_cov["identification_premise"],
        "internal_selected_data": internal_selected_data,
        "still_open": still_open,
        "guardrails": guardrails,
        "theorem": {
            "name": "Selected_Character_Channel_Covariance_Import.v1",
            "status": "INTERNAL_CLOSURE_IMPORTED_PHYSICAL_UNIT_OPEN",
            "statement": (
                "On the selected q64=15 character-channel branch, the unresolved "
                "finite-memory covariance denominator is d_Q=1 and the selected "
                "internal rho_UV branch is closed at R_star. Therefore the internal "
                "source-data pair (d_Q, ||U||) can be imported into the GR/protospinor "
                "normalization chain, conditional on the character-channel identification "
                "premise. This still does not supply the physical unit Omega_0."
            ),
            "conditional_physical_formula": (
                "Lambda_gap_phys = sqrt(15) * Omega_0 / s_star with "
                f"s_star={selected_values['s_star_from_rho']:.15g}; only Omega_0 remains."
            ),
        },
        "next_required_artifact": "Selected_Physical_Omega0_Source_Theorem_v1",
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Character-Channel Covariance Import v1

## Result

The selected internal covariance gate can be imported from the non-SM constants
repo, with the branch caveat kept explicit.

Closed on the selected character-channel branch:

```text
selected character = {closed_on_branch["selected_character"]}
selected channel   = {closed_on_branch["selected_channel"]}
Q_char             = E_15 = |15><15|
K_ret action       = unit phase on |15>
d_Q                = ||D_raw||^2 = {d_q:.1f}
G_11               = {closed_on_branch["G_11"]:.1f}
```

At the final selected internal radius:

```text
R_star   = {selected_values["R_star"]:.15g}
||U||    = C_UV_internal = {c_uv_norm:.15g}
rho_UV   = {rho_uv:.15g}
s_star   = {selected_values["s_star_from_rho"]:.15g}
```

So the GR/protospinor physical normalization chain no longer has an internal
`Q_tau` blocker on this selected branch. The remaining physical formula is:

```text
Lambda_gap_phys = sqrt(15) * Omega_0 / s_star
```

## Caveat

This import is conditional on the same premise as the non-SM certificate:

```text
{char_cov["identification_premise"]["statement"]}
```

It does not claim closure for all covariance models, deck-position covariance,
or trace-one mixtures over all 64 characters.

## Remaining Gate

Only the physical unit remains:

```text
Omega_0
```

No observed Newton, Planck, cosmological, TeV, or particle-mass value is used.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
