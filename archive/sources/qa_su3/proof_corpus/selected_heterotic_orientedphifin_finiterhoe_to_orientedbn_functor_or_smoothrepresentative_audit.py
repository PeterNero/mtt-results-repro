"""Audit finite-rhoE to oriented-BN functor / smooth-representative split."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_FiniteRhoE_to_OrientedBN_Functor_or_SmoothRepresentative_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_FINITERHOE_TO_ORIENTEDBN_ORIENTATION_FUNCTOR_CLOSED_MAGNITUDE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_MagnitudeFinitepart_SourceTheorem_or_SmoothEQa_TraceIdentity_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    packet = load(PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    orientation = packet["orientation_functor"]
    magnitude = packet["magnitude_obstruction"]
    smooth = packet["smooth_representative_lane"]
    compressed = packet["compressed_label_values"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("orientation functor closes", decision["finite_rhoE_to_oriented_BN_orientation_functor_closed"] is True and orientation["closed"] is True, orientation)
    check("projection and rho checks", orientation["projection_pair_valid"] is True and orientation["rho_character_intertwines"] is True, orientation)
    check("compressed C_tau equals tau", orientation["compressed_C_tau_equals_internal_tau_for_all_labels"] is True and all(row["orientation_value_matches"] for row in compressed.values()), compressed)
    check("magnitude remains open", decision["threshold_magnitude_functor_closed"] is False and magnitude["closed"] is False, magnitude)
    check("DE and finitepart mismatch retained", magnitude["D_E_intertwines_with_oriented_BN"] is False and magnitude["finitepart_matches_oriented_BN"] is False, magnitude)
    check("smooth lane remains open", smooth["support_prefilter_closed"] is True and smooth["smooth_transition_tables_emitted"] is False and smooth["smooth_finitepart_computed"] is False and smooth["E_Qa_computed"] is False, smooth)
    check("no logdet promotion", decision["finitepart_trace_identity_closed"] is False and decision["oriented_logdet_promoted"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records packet", str(PACKET.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin finite-rhoE to oriented-BN audit passed")


if __name__ == "__main__":
    main()
