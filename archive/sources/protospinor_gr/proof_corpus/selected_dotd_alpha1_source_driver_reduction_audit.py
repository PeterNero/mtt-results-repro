from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_dotd_alpha1_source_driver_reduction_certificate.json"
STATUS = "SELECTED_DOTD_ALPHA1_SOURCE_DRIVER_REDUCED_TO_TANGENT_OR_RETARDED_KERNEL"
NEXT = "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["source_driver_theorem_proved"] is False, "source/driver theorem must remain open")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    support = packet["closed_support"]
    require(all(support.values()), "all closed-support flags should be true")
    missing = packet["exact_missing_object"]
    require(missing["name"] == "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel", "wrong missing object")
    require(len(missing["must_emit"]) == 5, "missing-object contract should have five fields")

    require(all(packet["what_closes_now"].values()), "closure reduction flags should be true")
    require(all(packet["what_remains_open"].values()), "remaining blockers should be true")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "diagnostic source-lift" in note, "note missing essentials")

    print("AUDIT_PASS: dotD alpha1 source/driver reduced to selected tangent or retarded kernel")


if __name__ == "__main__":
    main()
