"""Audit the Qa/SU3 c-twist transgression pairing computation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "ctwist_transgression_pairing_computation_certificate.json"
DATA = REPO / "candidate_data" / "ctwist_transgression_pairing_computation.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_CTwist_Transgression_Pairing_Computation_v1.md"
SCRIPT = REPO / "scripts" / "build_ctwist_transgression_pairing_computation.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    slants = data["slant_pairings"]
    checks = [
        check("status", cert["status"] == "QA_SU3_CTWIST_TRANSGRESSION_PAIRING_COMPUTED_COMPLEX_ROTATED_CENTRAL_SUPPORT", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("H form nonzero", bool(data["H_scaled_real_form"]), data["H_scaled_real_form"]),
        check("four slants", len(slants) == 4, slants),
        check("all slants central nonzero", gates["all_four_base_slants_are_nonzero_and_central"] is True, slants),
        check("direct axis mismatch recorded", gates["direct_nil_commutator_axis_match"] is False and gates["complex_rotated_central_support_detected"] is True, gates),
        check("no zero-pairing no-go", gates["transgression_axis_supports_c_twist"] is True and gates["gerbe_route_retired"] is False, gates),
        check("normalization still open", gates["integral_generator_normalization_proved_from_selected_flux"] is False and cert["what_remains_open"]["selected_integral_generator_normalization"] is True, gates),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifact", cert["next_required_artifact"] in note, NOTE),
    ]
    print("\nSelected Qa/SU3 c-twist transgression pairing computation audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
