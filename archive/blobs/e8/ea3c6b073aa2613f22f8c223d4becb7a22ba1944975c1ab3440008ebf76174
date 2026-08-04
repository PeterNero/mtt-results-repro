"""Audit the U1/Y Route-C operator-emission/overlap gate from terminal slot map."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_OperatorEmission_and_OverlapNormalization_from_TerminalSlotMap_v1.md"

STATUS = "U1Y_ROUTEC_OPERATOR_EMISSION_OVERLAP_FUNCTIONAL_CLOSED_ALPHA1_DRIVER_OPEN"
NEXT = "Selected_U1Y_RouteC_Alpha1_Driver_Replay_from_OrientedOverlap_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    blocks = data["emitted_operator_blocks"]
    norm = data["overlap_normalization"]
    alpha = data["alpha_boundary"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("functional emission closed", cert["same_branch_functional_operator_emission_closed"] is True, cert),
        check("U10 and 1M emitted", cert["selected_U10_Ubar5_operator_blocks_emitted"] is True and cert["selected_1M_Dirac_operator_block_emitted"] is True, cert),
        check("sector keys exact", sorted(blocks) == ["d", "e", "nuD", "u"], sorted(blocks)),
        check("nuD maps to N", blocks["nuD"]["functional_key"] == "N" and blocks["nuD"]["projector_rank"] == 3, blocks["nuD"]),
        check("all grams I3", all(row["basis_Gram"] == "I_3" for row in blocks.values()), blocks),
        check("sqrt2 norms", all(abs(row["rho_s_T3_frobenius_norm"] - 2 ** 0.5) < 1e-12 for row in blocks.values()), norm),
        check("normalization emitted", cert["selected_overlap_normalization_emitted"] is True and norm["normalization"] == "rho_s(T_i)/sqrt(2)", norm),
        check("alpha remains open", alpha["selected_dotD_source_formula_closed"] is True and cert["alpha1_driver_verified"] is False and cert["honest_dotD_validator_closed"] is False, alpha),
        check("Pic0 remains open", cert["operator_layer_Pic0_closed"] is False and data["pic0_boundary"]["operator_layer_Pic0_closed"] is False, data["pic0_boundary"]),
        check("guardrails hold", guardrails["claims_lambda12"] is False and guardrails["uses_observed_data"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records boundary", "does not by itself prove `du/dalpha1=h_ext`" in note and "Functional stationary operator emission" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C operator-emission/overlap-from-terminal-slotmap audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
