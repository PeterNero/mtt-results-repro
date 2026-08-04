"""Audit const_em_01_alpha1_convention_map."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_convention_map"
CANDIDATE = DATA / "const_em_01_alpha1_convention_map.candidate.json"
FORMULA_MAP = BASE / "electroweak_formula_map.packet.json"
NORMALIZATION = BASE / "normalization_slots.packet.json"
COMPARISON = BASE / "comparison_protocol.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_convention_map_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_ConventionMap_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_convention_map.py"
STATUS = "MTT_CONST_EM_01_ALPHA1_CONVENTION_MAP_BUILT_NUMERICAL_ALPHA_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    formula = load(FORMULA_MAP)
    normalization = load(NORMALIZATION)
    comparison = load(COMPARISON)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["source_to_observable_formula_map_built"] is True, "formula map not built")
    require(candidate["what_closes_now"]["hypercharge_GUT_and_em_alpha_conventions_separated"] is True, "conventions not separated")
    require(candidate["what_remains_open"]["C_Y_source_to_hypercharge_coupling"] is True, "C_Y closed too early")
    require(candidate["what_remains_open"]["alpha_zero_value"] is True, "alpha0 closed too early")
    require(candidate["what_remains_open"]["alpha_MZ_value"] is True, "alphaMZ closed too early")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")

    equations = formula["convention_equations"]
    require(equations["GUT_normalized_alpha1"] == "alpha_1^GUT(mu) = (5/3) alpha_Y(mu)", "GUT equation mismatch")
    require("alpha_Y(mu)*alpha_2(mu)" in equations["direct_tree_electromagnetic"], "EM equation missing")
    require(formula["source_to_convention_symbols"]["alpha_Y(mu_source)"] == "C_Y(mu_source) * N_alpha1(h_ext)", "source slot mismatch")

    require(normalization["closed_slots"]["source_side_N_alpha1_h_ext"] is True, "source-side N not closed")
    require(normalization["open_slots"]["C_Y_source_to_hypercharge_coupling"]["selected_now"] is False, "C_Y selected too early")
    require(normalization["open_slots"]["C_Y_source_to_hypercharge_coupling"]["allowed_to_fit_from_alpha"] is False, "C_Y fit allowed")
    require(normalization["universal_parameter_policy"]["selected_universal_parameters_now"] == 0, "universal parameter count mismatch")

    require(comparison["allowed_modes"]["SM_parity_replay"]["source_selector_allowed"] is False, "SM replay selector allowed")
    require(comparison["allowed_modes"]["no_knob_derivation"]["can_claim_constant_derivation"] is True, "no-knob mode mismatch")
    require("backfit_alpha_to_C_Y" in comparison["blocked_modes"], "backfit block missing")
    require(len(comparison["external_guardrail_sources"]) == 4, "external guardrail count mismatch")

    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY", "next primary mismatch")
    require(cert["physical_alpha_value_claimed"] is False, "cert physical alpha overclaim")
    require(cert["selected_universal_parameters_now"] == 0, "cert universal parameter count mismatch")
    require("alpha_em(mu)" in note, "note formula missing")
    require("A3-FIND-CY" in note, "note next label missing")

    for packet in [candidate, formula, normalization, comparison, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
