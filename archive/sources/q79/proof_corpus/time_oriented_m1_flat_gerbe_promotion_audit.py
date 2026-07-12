"""Audit the conditional flat gerbe promotion for the m=1 deck cocycle."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "promote_time_oriented_m1_deck_cech_to_flat_gerbe.py"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_flat_gerbe_promotion.candidate.json"
CERT = REPO / "certificates" / "time_oriented_m1_flat_gerbe_promotion_certificate.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_Flat_Gerbe_Promotion_v1.md"


@dataclass
class Gate:
    name: str
    passed: bool
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_constructor() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    proc = run_constructor()
    gates: list[Gate] = [
        Gate("constructor exits 0", proc.returncode == 0, proc.stdout[:1000]),
        Gate("candidate exists", CANDIDATE.exists(), str(CANDIDATE)),
        Gate("certificate exists", CERT.exists(), str(CERT)),
        Gate("paper exists", PAPER.exists(), str(PAPER)),
    ]

    if CANDIDATE.exists() and CERT.exists() and PAPER.exists():
        candidate = load_json(CANDIDATE)
        cert = load_json(CERT)
        route = cert.get("aspherical_nilmanifold_route", {})
        flat = cert.get("flat_gerbe_model", {})
        projectors = cert.get("projective_bundle_and_projector_retention", {})
        fw = cert.get("freed_witten_reduction", {})
        calc = cert.get("calculation_results", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        paper = PAPER.read_text(encoding="utf-8")

        gates.extend(
            [
                Gate(
                    "status conditional closed selection open",
                    cert.get("status")
                    == "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_CONDITIONAL_CLOSED_SELECTION_OPEN",
                    cert.get("status", ""),
                ),
                Gate(
                    "aspherical route valid but not selected",
                    route.get("contractible_universal_cover") is True
                    and route.get("quotient_is_K_Gamma_1_if_candidate_lattice_selected")
                    is True
                    and route.get("standard_deck_scaffold_valid") is True
                    and route.get("standard_deck_scaffold_selected_by_current_certificates")
                    is False,
                    str(route),
                ),
                Gate(
                    "flat torsion gerbe model",
                    flat.get("torsion_order") == 3
                    and flat.get("curvature_H_form") == "0"
                    and flat.get("dixmier_douady_class", {}).get("type")
                    == "flat torsion",
                    str(flat),
                ),
                Gate(
                    "projective module and finite projectors compatible",
                    projectors.get("qutrit_projective_carrier_matched") is True
                    and projectors.get("finite_block_factorized_sector_projectors_valid")
                    is True
                    and projectors.get("selected_projector_retention_verified")
                    is False,
                    str(projectors),
                ),
                Gate(
                    "Freed-Witten reduced not verified",
                    fw.get("flat_gerbe_torsion_order") == 3
                    and fw.get("W3_is_two_primary") is True
                    and fw.get("three_torsion_cannot_cancel_two_primary_W3") is True
                    and fw.get("selected_cycles_supplied") is False
                    and fw.get("freed_witten_verified") is False,
                    str(fw),
                ),
                Gate(
                    "calculation closes conditional only",
                    calc.get("conditional_flat_gerbe_representative_exists") is True
                    and calc.get("selected_flat_gerbe_representative_closed") is False
                    and calc.get("selected_D_E_dotD_constructed") is False,
                    str(calc),
                ),
                Gate(
                    "what closes and what remains",
                    closes.get("conditional_group_cocycle_to_flat_Deligne_Cech_gerbe_promotion")
                    is True
                    and closes.get("Freed_Witten_reduced_to_cycle_restriction_and_W3_checks")
                    is True
                    and still_open.get("MTT_selection_of_standard_deck_scaffold_or_equivalent_cover")
                    is True
                    and still_open.get("selected_D_E_dotD_Riesz_Green_files_from_same_branch")
                    is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                Gate(
                    "guardrails no overclaim",
                    guardrails.get("claims_Gamma0_is_MTT_selected") is False
                    and guardrails.get("claims_unconditional_selected_geometric_representative")
                    is False
                    and guardrails.get("claims_Freed_Witten_verified") is False
                    and guardrails.get("claims_selected_D_E_dotD_constructed") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                Gate(
                    "paper records sharp next blocker",
                    "selected cover/cycle restrictions and W3 checks" in paper
                    and "direct selected HYM/Strominger operator-source packet" in paper,
                    "next blocker text present",
                ),
                Gate(
                    "candidate mirrors certificate status",
                    candidate.get("status") == cert.get("status"),
                    candidate.get("status", ""),
                ),
            ]
        )

    for gate in gates:
        status = "PASS" if gate.passed else "FAIL"
        print(f"[{status}] {gate.name}: {gate.detail}")

    return 0 if all(gate.passed for gate in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
