"""Audit the c-axis orthogonality source / weighted operator packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "caxis_orthogonality_source_or_weighted_operator_packet_certificate.json"
DATA = REPO / "candidate_data" / "caxis_orthogonality_source_or_weighted_operator_packet.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_CAxis_Orthogonality_Source_or_Weighted_Operator_Packet_v1.md"
SCRIPT = REPO / "scripts" / "build_caxis_orthogonality_source_or_weighted_operator_packet.py"


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
    sample = data["sample_non_unit_packet"]
    status = data["current_source_status"]
    checks = [
        check("status", cert["status"] == "QA_SU3_CAXIS_ORTHOGONALITY_PROVED_UNDER_CENTRAL_TWIST_ORBIT_DEMOCRACY_SOURCE_WEIGHT_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("symbolic H has zero c couplings", data["symbolic_weighted_hessian"]["matrix"][0][2] == 0 and data["symbolic_weighted_hessian"]["matrix"][1][2] == 0, data["symbolic_weighted_hessian"]),
        check("positive determinant formula", data["symbolic_weighted_hessian"]["base_determinant"] == "91*a^2 + 133*a*b + 29*a*p + b*p", data["symbolic_weighted_hessian"]),
        check("non-unit example preserves c axis", sample["weights"]["F3"] == "7/5" and sample["weights"]["P"] == "6/5" and sample["H13_H23_zero"] is True, sample),
        check("sample Pi/tau stable", sample["Pi_tw"] == [0, 0, 1] and sample["tau"]["P"] == 0 and sample["tau"]["F1"] + sample["tau"]["G1"] == 0, sample),
        check("source theorem conclusion", "H13=H23=0" in data["source_theorem"]["conclusion"], data["source_theorem"]),
        check("closed source pieces recorded", status["central_twist_orbit_partition"] == "CLOSED_FROM_TAU_TABLE" and status["opposite_twist_product_cancellation"] == "CLOSED_FROM_TYPED_MONAD_PRODUCTS", status),
        check("operator weight remains open", status["orbit_democracy_weight_invariance"] == "CONDITIONAL_NOT_SOURCE_SELECTED_AS_OPERATOR_WEIGHT", status),
        check("not full closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "central-twist orbit democracy" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 c-axis orthogonality source or weighted operator packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
