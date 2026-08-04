"""Audit visible Route-C PhiFin alpha1 derivative fill reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_visible_routec_phifin_alpha1_derivative_fill_reduction.py"
PACKET = ROOT / "candidate_data" / "visible_routec_phifin_alpha1_derivative_fill_reduction.candidate.json"
CERT = ROOT / "certificates" / "visible_routec_phifin_alpha1_derivative_fill_reduction_certificate.json"
NOTE = ROOT / "proof_corpus" / "Visible_RouteC_PhiFin_Alpha1_Derivative_Fill_Reduction_v1.md"
STATUS = "VISIBLE_ROUTEC_PHIFIN_ALPHA1_DERIVATIVE_FILL_REDUCED_TO_SELECTED_ROUTEC_GALERKIN_SOLVE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    print(f"{'PASS' if condition else 'FAIL'}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)

    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    check("status", cert["status"] == STATUS, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem proved", packet["theorem"]["proved"] is True, packet["theorem"])
    check("all checks pass", all(packet["checks"].values()), packet["checks"])

    phifin = packet["phifin_value_state"]
    check(
        "PhiFin support is not selected payload",
        phifin["all_support_shapes_present"]
        and phifin["all_selected_values_emitted"] is False
        and all(value is False for value in phifin["selected_payload_flags"].values()),
        phifin,
    )

    layers = packet["projector_layer_separation"]
    spectral = layers["spectral_projector_layer"]
    check(
        "block and spectral projectors separated",
        layers["layer_separation_honest"]
        and layers["block_projector_layer"]["block_family_Higgs_projector_retention"]
        and spectral["coherent_spectral_zero_mode_projector_retention"] is False
        and spectral["selected_D_E_dotD_Riesz_Green"] is False,
        layers,
    )

    contract = packet["selected_solve_contract"]
    check(
        "solve contract is Route-C Strominger Galerkin",
        contract["name"] == "SelectedRouteCStromingerGalerkinResidualSolve"
        and "same-branch dotD_alpha1 = dD_E(deltaTheta_C1)/depsilon at epsilon=0"
        in contract["unknowns"],
        contract,
    )

    update = packet["frontier_update"]
    check(
        "frontier moved to selected Route-C Galerkin solve spec",
        update["old_next"] == "MTT_Visible_RouteC_PhiFinAlpha1Derivative_Fill_v1"
        and update["intermediate_next"]
        == "MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1"
        and update["current_next"]
        == "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1",
        update,
    )
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "no selected payload values",
        "selected Route-C/Strominger Galerkin residual solve",
        "Projector Layer Separation",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nVisible Route-C PhiFin alpha1 derivative fill reduction audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
