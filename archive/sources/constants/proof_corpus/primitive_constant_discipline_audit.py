"""Audit primitive-constant discipline."""

from __future__ import annotations

import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Primitive_Constant_Discipline_for_No_Knob_Program_v1.md"
CERT = REPO / "certificates" / "primitive_constant_discipline_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    checks = [
        check("certificate status", cert["status"] == "PRIMITIVE_CONSTANT_POLICY_FORMULATED", cert["status"]),
        check("fit knob forbidden", "forbidden knob" in note.lower() and "backsolves" in note.lower(), "target backsolve rejected"),
        check("primitive tests stated", all(item in note for item in ["Universality", "Prior selection", "Auditability", "Predictive surplus"]), "primitive criteria"),
        check("rho policy stated", "R chosen to make rho_UV" in note and "prove the Selected Horizontal-Scale Lemma" in note, cert["rho_uv_policy"]),
        check("allowed in principle", cert["verdict"]["primitive_constants_allowed_in_principle"] is True, cert["verdict"]),
        check("target-fit counts as knob", cert["verdict"]["primitive_constants_count_as_knobs_if_target_fit"] is True, cert["verdict"]),
    ]
    print("\nPrimitive constant discipline audit")
    print("===================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
