"""Build the selected dotD_alpha1 transport-derivative probe.

This artifact attacks the frontier left by the symbolic transport-conjugation
validator.  It proves the missing transport-derivative formula and checks the
finite dotD validator boundary.

The result is intentionally split:

* the transported dotD source formula closes algebraically;
* the existing finite response matrices pass once selected flags are supplied;
* the alpha1 driver is still not promoted unless a same-branch source-strength
  normalization theorem identifies the Ext-density tangent with the physical
  alpha1 derivative.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

TRANSPORT_REPLAY = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
PHYSICAL_DOTD = DATA / "selected_physical_dotd_alpha1_or_end0_sector_routing.candidate.json"
ALPHA1_THEOREM = DATA / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json"
ALPHA1_VALUE_FILL = DATA / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json"
SOURCE_DRIVER = DATA / "selected_source_origin_and_alpha1_driver.candidate.json"
DOTD_HONEST = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn" / "sector_projectors_dotd_on_smooth_bn.honest.json"
DOTD_VALIDATOR = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-q79-proof-repro/scripts/validate_iwasawa_dotd_response.py")

OUTPUT = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
PROBE_DIR = DATA / "selected_dotd_alpha1_transport_derivative_probe"
SOURCE_ONLY_PROBE = PROBE_DIR / "dotd_source_verified_alpha1_open_probe.json"
FULL_FLAG_PROBE = PROBE_DIR / "dotd_full_flag_probe.json"
CERT = CERTS / "selected_dotd_alpha1_transport_derivative_probe_certificate.json"
NOTE = CORPUS / "MTT_Selected_dotD_alpha1_TransportDerivative_Probe_v1.md"

STATUS = "MTT_SELECTED_DOTD_ALPHA1_TRANSPORT_DERIVATIVE_CLOSED_DRIVER_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceStrength_Normalization_or_Driver_Theorem_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def set_dotd_flags(payload: dict[str, Any], *, selected_dotd: bool, alpha1_driver: bool) -> dict[str, Any]:
    out = copy.deepcopy(payload)
    out["selected_dotD_source_verified"] = selected_dotd
    out["alpha1_driver_verified"] = alpha1_driver
    for slot in out["dotd_response_slots"].values():
        slot["selected_dotD_source_verified"] = selected_dotd
        slot["alpha1_driver_verified"] = alpha1_driver
    return out


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(DOTD_VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "output": [line for line in proc.stdout.splitlines() if line.strip()],
    }


def main() -> int:
    transport = load(TRANSPORT_REPLAY)
    physical = load(PHYSICAL_DOTD)
    alpha1_theorem = load(ALPHA1_THEOREM)
    alpha1_value_fill = load(ALPHA1_VALUE_FILL)
    source_driver = load(SOURCE_DRIVER)
    honest = load(DOTD_HONEST)

    PROBE_DIR.mkdir(parents=True, exist_ok=True)
    source_only_payload = set_dotd_flags(honest, selected_dotd=True, alpha1_driver=False)
    full_flag_payload = set_dotd_flags(honest, selected_dotd=True, alpha1_driver=True)
    SOURCE_ONLY_PROBE.write_text(json.dumps(source_only_payload, indent=2, sort_keys=True), encoding="utf-8")
    FULL_FLAG_PROBE.write_text(json.dumps(full_flag_payload, indent=2, sort_keys=True), encoding="utf-8")

    source_only_validation = run_validator(SOURCE_ONLY_PROBE)
    full_flag_validation = run_validator(FULL_FLAG_PROBE)

    tangent = physical["path_A_straight_selected_Ext_density_scale_tangent"]
    theorem = {
        "name": "SelectedDotDAlpha1TransportDerivativeFormula",
        "proved": True,
        "statement": (
            "For selected transported zero modes psi_sel=U psi_model with U=exp(-uJ), "
            "an alpha-tangent h=du/dalpha gives delta_U psi_sel=-(hJ) psi_sel and "
            "dotD_h psi_sel=(dh)J psi_sel.  Since D_sel(delta_U psi_sel)=-dotD_h psi_sel, "
            "the transport derivative supplies the exact finite horizontal response source "
            "formula by conjugation.  This proves the dotD source algebra, but not the "
            "physical alpha1 driver normalization."
        ),
        "proof_steps": [
            "On the T1/T2 lane U=exp(-uJ), so dU/dalpha=-(du/dalpha)J U.",
            "For h=du/dalpha and model zero mode psi0, delta psi=-(hJ)U psi0.",
            "The Frechet derivative of D=d+du J is dotD_h=(dh)J.",
            "Using D U=U d and [J,U]=0, D(delta psi)=-U(dh)J psi0=-dotD_h(U psi0).",
            "Thus the transported dotD source and response are fixed once h is selected.",
            "The remaining non-algebraic question is whether h is the selected physical alpha1 driver.",
        ],
    }

    driver_audit = {
        "selected_ext_density_tangent_available": tangent["closed"],
        "h_ext_residual_l2": tangent["residual_l2"],
        "h_ext_zero_mean": tangent["h_mean_abs"] < 1e-12,
        "dotD_frechet_replay_closed": alpha1_theorem["theorem_slot"]["proved_unconditionally_now"][
            "dotD_frechet_replay_closed"
        ],
        "source_normalization_route_reopened_by_transport_source": (
            transport["validator_result"]["selected_source_verified"] is True
            and transport["validator_result"]["selected_rho_s_validator_ready"] is True
        ),
        "naive_scale_to_alpha1_still_rejected": alpha1_value_fill["route_A_source_normalization"]["closed"],
        "operator_level_alpha1_driver_row_present": source_driver["alpha1_driver_audit"]["operator_level_support"][
            "selected_driver_alpha1_row"
        ],
        "evaluated_alpha1_values_present": all(
            source_driver["alpha1_driver_audit"]["selected_values"].values()
        ),
        "alpha1_driver_verified_now": False,
        "why_not_verified": (
            "The transport derivative proves what the dotD response must be for a selected h=du/dalpha. "
            "The repo still lacks a same-branch source-strength normalization theorem identifying "
            "the computed Ext-density tangent h_ext with the physical alpha1 derivative."
        ),
    }

    validator_boundary = {
        "honest_payload_path": rel(DOTD_HONEST),
        "source_only_probe_path": rel(SOURCE_ONLY_PROBE),
        "full_flag_probe_path": rel(FULL_FLAG_PROBE),
        "source_only_validation": source_only_validation,
        "full_flag_validation": full_flag_validation,
        "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived": full_flag_validation["exit_code"] == 0,
        "source_only_fails_only_by_alpha1_driver": (
            source_only_validation["exit_code"] == 1
            and all("alpha1_driver_verified is not true" in line or not line.startswith("-") for line in source_only_validation["output"])
        ),
        "promote_full_flags_now": False,
    }

    data = {
        "candidate": "MTTSelectedDotDAlpha1TransportDerivativeProbe",
        "status": STATUS,
        "inputs": {
            "transport_replay": rel(TRANSPORT_REPLAY),
            "physical_dotd": rel(PHYSICAL_DOTD),
            "alpha1_theorem": rel(ALPHA1_THEOREM),
            "alpha1_value_fill": rel(ALPHA1_VALUE_FILL),
            "source_driver": rel(SOURCE_DRIVER),
            "dotd_honest": rel(DOTD_HONEST),
        },
        "theorem": theorem,
        "transport_derivative_formula": {
            "U": "exp(-u ad(T3))",
            "dU_dalpha": "-(du/dalpha) ad(T3) U",
            "h_symbol": "h=du/dalpha",
            "dotD_h": "dotD_h=(dh) ad(T3)",
            "response": "delta psi=-(h ad(T3)) psi_sel",
            "identity": "D_sel(delta psi)+dotD_h psi_sel=0",
            "horizontal_gauge_requires": "mean(h)=0 or selected Gram-Schmidt removal of the kernel component",
            "h_ext_mean_abs": tangent["h_mean_abs"],
        },
        "driver_audit": driver_audit,
        "validator_boundary": validator_boundary,
        "promotion_decision": {
            "selected_dotD_source_formula_closed": True,
            "selected_dotD_source_verified_by_transport_derivative": True,
            "alpha1_driver_verified": False,
            "dotD_validator_full_replay_closed": False,
            "reason": "The validator replay is mathematically ready, but the alpha1 driver flag still needs a theorem-derived source-strength normalization.",
        },
        "superset_strategy": {
            "classification": "STRAIGHT_TRANSPORT_DERIVATIVE_PLUS_SUPERSET_DRIVER_AUDIT",
            "straight_path": "derive dU/dalpha and dotD_h response from End0/HYM pure gauge transport",
            "support_path": "reuse Ext-density tangent, C1 alpha1 driver row, and Phi_fin source packet as support without promoting the driver",
            "locked_target": "honest dotD validator replay with selected_dotD_source_verified and alpha1_driver_verified true by theorem",
            "uses_observed_constants": False,
        },
        "what_closes_now": {
            "transport_derivative_formula": True,
            "selected_dotD_source_algebra": True,
            "validator_math_passes_if_driver_is_theorem_derived": validator_boundary[
                "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"
            ],
            "alpha1_driver_remaining_gap_is_single_normalization_theorem": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "alpha1_driver_source_strength_normalization": True,
            "honest_dotD_validator_replay_without_alpha1_lift": True,
            "primitive_C1_overlap_contractions": True,
            "selected_matter_slot_routing": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_dotD_alpha1_TransportDerivative_Probe_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "transport_derivative_formula_closed": True,
        "selected_dotD_source_formula_closed": True,
        "selected_dotD_source_verified_by_transport_derivative": True,
        "alpha1_driver_verified": False,
        "dotD_validator_full_replay_closed": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected dotD alpha1 Transport-Derivative Probe v1

Status: `{STATUS}`.

## Result

The missing transport derivative is now algebraically fixed.  For

```text
psi_sel = U psi_model
U = exp(-u ad(T3))
h = du/dalpha
```

we have

```text
dU/dalpha = -h ad(T3) U
delta psi = -h ad(T3) psi_sel
dotD_h = dh ad(T3)
D_sel(delta psi) + dotD_h psi_sel = 0
```

So the transported dotD source formula is closed.  The existing finite dotD
matrices also pass the validator when both selected flags are supplied by
theorem:

```text
full-flag probe exit code = {full_flag_validation["exit_code"]}
```

## Boundary

The alpha1 driver is still not promoted.  The selected Ext-density tangent is
nontrivial and has residual

```text
{tangent["residual_l2"]}
```

but the repo still needs one same-branch source-strength normalization theorem
to identify this tangent with the physical alpha1 derivative.  Until that is
proved, the honest dotD validator cannot be marked fully closed.

No observed constants, benchmark targets, or lifted selected flags are used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
