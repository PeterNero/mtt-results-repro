"""Audit the index-to-three-family upgrade gate."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "index_to_three_family_upgrade_gate_certificate.json"
PAPER = ROOT / "Index_to_Three_Family_Upgrade_Gate_for_Iwasawa_Bundle_v1.md"
FLUX = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    flux = read(FLUX)

    source_claims = cert.get("source_claims", {})
    index_implication = cert.get("index_implication", {})
    requirements = cert.get("upgrade_requirements", {})
    consequence = cert.get("consequence_for_sm_closure", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status") == "INDEX_TO_THREE_FAMILY_UPGRADE_BLOCKED_BY_MIDDLE_COHOMOLOGY_DATA"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source c3 six",
            "PASS" if "int_X c_3(E)=6" in flux or "\\int_X c_3(E)=6" in flux else "FAIL",
            str(FLUX),
        ),
        Gate(
            "source net generations",
            "PASS" if "three net chiral generations" in flux else "FAIL",
            "source states net chirality",
        ),
        Gate(
            "source assumes Psi_i",
            "PASS" if "\\Psi_i\\in H^1(X,E)" in flux and "i=1,2,3" in flux else "FAIL",
            "source uses three representatives",
        ),
        Gate(
            "source claims recorded",
            "PASS"
            if source_claims.get("integral_c3") == 6
            and source_claims.get("source_states_three_net_chiral_generations") is True
            and source_claims.get("source_uses_three_H1_representatives") is True
            else "FAIL",
            str(source_claims),
        ),
        Gate(
            "index distinction",
            "PASS"
            if index_implication.get("net_chirality_absolute_value") == 3
            and index_implication.get("fixes_difference_not_individual_dimensions") is True
            else "FAIL",
            str(index_implication),
        ),
        Gate(
            "upgrade requirements open",
            "PASS"
            if requirements.get("selected_integrable_dolbeault_or_monad_complex") is False
            and requirements.get("anti_family_middle_cohomology_vanishes") is False
            and requirements.get("h1_X_E_equals_three") is False
            else "FAIL",
            str(requirements),
        ),
        Gate(
            "SM consequence",
            "PASS"
            if consequence.get("net_three_family_target_supported") is True
            and consequence.get("three_family_zero_mode_basis_constructed") is False
            and consequence.get("full_sm_closure_claim_allowed") is False
            else "FAIL",
            str(consequence),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("uses_index_as_basis") is False
            and guardrails.get("uses_net_chirality_as_h1_dimension") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("topological_index_gate_supported") is True
            and verdict.get("cohomology_upgrade_open") is True
            and "anti-family vanishing" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records upgrade gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "The first is topological",
                    "requires cohomology computation",
                    "fixes the difference",
                    "anti-generation",
                    "constructed rather than assumed",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Index-to-three-family upgrade gate audit")
    print("========================================")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
