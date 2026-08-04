from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_basis_transport_gate_reduction_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "ROUTEC_BASISTRANSPORT_GATE_REDUCED_SOURCE_PROOF_OPEN", "unexpected status")
    require(cert["theorem"]["proved"] is True, "gate reduction theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now reductions should pass")
    require(all(cert["still_open"].values()), "source proof gates should remain open")
    require(cert["reduction"]["active_shift"] == [1, 1], "active shift should be forced to (1,1)")
    require(cert["reduction"]["fixed_qutrit_fiber_shifts"] == ["0", "1", "2"], "fixed fiber shifts should be 0,1,2")
    for shift, ranks in cert["reduction"]["fixed_fiber_rank_by_sector"].items():
        require(all(rank == 3 for rank in ranks.values()), f"fixed shift {shift} should be rank 3")
    require(packet["basis_transport_theorem_slot"]["status"] == "THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN", "basis theorem slot boundary changed")
    require(cert["verdict"]["selected_basis_transport_source_proved"] is False, "selected basis transport must remain unproved")
    require(cert["verdict"]["selected_C1_primitive_promoted"] is False, "C1 primitive must not be promoted")
    require(cert["verdict"]["nondegenerate_yukawa_or_CKM_PMNS_closed"] is False, "flavor closure must remain open")
    require("does not prove operator-level basis transport" in note, "note must state source boundary")
    require(all(cert["guardrails"].values()), "all guardrails must hold")

    print("AUDIT_PASS: Route-C basis-transport gate reduced; source proof remains open")


if __name__ == "__main__":
    main()
