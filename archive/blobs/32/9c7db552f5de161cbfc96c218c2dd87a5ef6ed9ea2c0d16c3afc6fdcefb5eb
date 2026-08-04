"""Audit full-Fourier-orbit source-selection theorem/no-go gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_fullfourierorbit_sourceselection_theorem_or_nogo.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_fullfourierorbit_sourceselection_theorem_or_nogo.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_fullfourierorbit_source_coemission_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_fullfourierorbit_sourceselection_theorem_or_nogo_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_FullFourierOrbit_SourceSelection_Theorem_or_NoGo_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_FULLFOURIERORBIT_MAGNITUDE_SOURCE_SELECTED_ORIENTATION_COEMISSION_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_OrientationMagnitude_CoEmission_Theorem_v1"


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
    magnitude = data["magnitude_source"]
    orientation = data["orientation_source"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("magnitude selected", decision["routec_magnitude_source_selected_for_27mode_DE_gap_layer"] is True and magnitude["selected_27mode_BN_DE_gap_layer"]["closed"] is True, magnitude)
    check("full orbit selected at gap scope", decision["full_positive_fourier_orbit_selected_at_gap_layer_scope"] is True and magnitude["full_positive_fourier_orbit_available"]["closed"] is True, magnitude)
    check("routec basis exact", magnitude["selected_27mode_BN_DE_gap_layer"]["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3" and magnitude["selected_27mode_BN_DE_gap_layer"]["basis_dimension"] == 27, magnitude)
    check("orientation functor closed", decision["orientation_functor_closed"] is True and orientation["rhoE_to_BN_orientation_functor"]["closed"] is True, orientation)
    check("coemission open", decision["orientation_magnitude_coemission_closed"] is False and packet["coemission_closed"] is False, packet)
    check("remaining leaf", decision["remaining_single_leaf"] == "same_source_orientation_magnitude_coemission" and cert["remaining_single_leaf"] == decision["remaining_single_leaf"], decision)
    check("coemission packet fields", set(packet["remaining_required_fields"]) == {"same_source_identity_between_routec_gap_layer_and_heterotic_oriented_phifin", "C_tau_orientation_emitted_on_full_27mode_BN_domain", "proof_C_tau_commutes_with_selected_routec_DE_as_source_operator", "oriented_positive_sector_policy_selected_before_finitepart", "finitepart_trace_identity_inherits_source_ownership"}, packet["remaining_required_fields"])
    check("trace relative", decision["trace_identity_closed_relative_to_coemission"] is True and packet["trace_identity_relative_closed"] is True, packet)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records packet", str(PACKET.relative_to(ROOT)) in note and NEXT in note and "orientation_magnitude_coemission_closed = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin full-Fourier-orbit source-selection audit passed")


if __name__ == "__main__":
    main()
