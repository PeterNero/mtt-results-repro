"""Audit the time-oriented m=1 deck/Cech lift."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "construct_time_oriented_m1_deck_cech_lift.py"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_deck_cech_lift.candidate.json"
CERT = REPO / "certificates" / "time_oriented_m1_deck_cech_lift_certificate.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_Deck_Cech_Lift_v1.md"


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
        deck_map = cert.get("deck_quotient_map", {})
        calc = cert.get("calculation_results", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        cech = candidate.get("pulled_back_deck_cech_data", {})
        carrier = candidate.get("qutrit_projective_carrier_match", {})
        periods = cech.get("generator_period_table_mod3", {})
        paper = PAPER.read_text(encoding="utf-8")

        gates.extend(
            [
                Gate(
                    "status closed deck lift only",
                    cert.get("status")
                    == "TIME_ORIENTED_M1_DECK_CECH_LIFT_CLOSED_GEOMETRIC_OPERATOR_SOURCE_OPEN",
                    cert.get("status", ""),
                ),
                Gate(
                    "quotient map active on g1 g2 only",
                    deck_map.get("map", {}).get("g1") == [1, 0]
                    and deck_map.get("map", {}).get("g2") == [0, 1]
                    and all(
                        deck_map.get("map", {}).get(gen) == [0, 0]
                        for gen in ("g3", "g4", "g5", "g6")
                    ),
                    str(deck_map.get("map")),
                ),
                Gate(
                    "generator periods match qutrit orientation",
                    periods.get("g1|g2") == 0
                    and periods.get("g2|g1") == 2
                    and carrier.get("g1g2_commutator_mod3_from_cech_pullback") == 1
                    and carrier.get("g2g1_commutator_mod3_from_cech_pullback") == 2,
                    str(
                        {
                            "g1g2": periods.get("g1|g2"),
                            "g2g1": periods.get("g2|g1"),
                        }
                    ),
                ),
                Gate(
                    "generator and active quotient bianchi",
                    cech.get("generator_coboundary_checked_triples") == 216
                    and cech.get("generator_nonzero_coboundary_deltas_mod3") == {}
                    and cech.get("active_quotient_coboundary_checked_triples") == 729
                    and cech.get("active_quotient_nonzero_coboundary_deltas_mod3") == {},
                    str(
                        {
                            "generator_triples": cech.get("generator_coboundary_checked_triples"),
                            "active_triples": cech.get(
                                "active_quotient_coboundary_checked_triples"
                            ),
                        }
                    ),
                ),
                Gate(
                    "matches qutrit carrier",
                    calc.get("qutrit_projective_commutator_matched") is True
                    and carrier.get("rho_g1_rho_g2_numeric_phase_relation", {}).get(
                        "best_exponent_mod3"
                    )
                    == 1
                    and carrier.get("inactive_generators_identity") is True,
                    str(carrier.get("rho_g1_rho_g2_numeric_phase_relation")),
                ),
                Gate(
                    "finite deck Cech closes not geometry",
                    closes.get("finite_Cech_two_cocycle_on_active_deck_quotient")
                    is True
                    and closes.get("deck_pullback_of_time_oriented_m1_period_table")
                    is True
                    and still_open.get("smooth_geometric_Deligne_Cech_representative_on_selected_cover")
                    is True
                    and still_open.get("selected_D_E_dotD_Riesz_Green_files_from_same_branch")
                    is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                Gate(
                    "guardrails no overclaim",
                    guardrails.get("claims_smooth_geometric_Deligne_Cech_representative")
                    is False
                    and guardrails.get("claims_Freed_Witten_verified") is False
                    and guardrails.get("claims_projector_retention") is False
                    and guardrails.get("claims_selected_D_E_dotD_constructed") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                Gate(
                    "paper records operator-source bridge",
                    "finite deck/Cech pullback" in paper
                    and "selected D_E/dotD/Riesz/Green files" in paper,
                    "bridge text present",
                ),
            ]
        )

    for gate in gates:
        status = "PASS" if gate.passed else "FAIL"
        print(f"[{status}] {gate.name}: {gate.detail}")

    return 0 if all(gate.passed for gate in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
