"""Audit the SM-equivalence reference-source registry."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_reference_source_registry.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_reference_source_registry_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_Reference_Source_Registry_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_reference_source_registry.py"

STATUS = "MTT_SM_EQUIVALENCE_REFERENCE_SOURCE_REGISTRY_BUILT_VALUES_OPEN"
NEXT = "MTT_SM_Equivalence_Reference_Data_Values_Fill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    registry = data["source_registry"]
    for key in ["PDG_2025", "NIST_CODATA_2022", "NuFIT_6_0"]:
        require(key in registry, f"source missing: {key}")
        require(registry[key]["source_url"].startswith("https://"), f"source URL missing: {key}")
        require(
            registry[key]["source_status"] == "APPROVED_REFERENCE_SOURCE_VALUES_NOT_COPIED",
            f"wrong source status: {key}",
        )

    slot_map = data["slot_source_map"]
    for slot in [
        "gauge.alpha_1_alpha_2_alpha_3",
        "yukawa.Y_u_Y_d_Y_e",
        "mixing.CKM",
        "mixing.PMNS",
        "higgs.v_mh_lambda_or_potential",
        "neutrino.yukawa_or_mass_splittings",
    ]:
        require(slot in slot_map, f"slot source map missing: {slot}")
        require(slot_map[slot], f"slot source map empty: {slot}")

    contract = data["fill_contract"]
    require(contract["values_filled_here"] is False, "values copied too early")
    must = " ".join(contract["next_values_fill_must"])
    for phrase in ["retrieval date", "units", "uncertainty", "conversion formulas"]:
        require(phrase in must, f"fill requirement missing: {phrase}")
    disallowed = " ".join(contract["disallowed_sources"])
    for phrase in ["uncited", "inverse-fit", "residual"]:
        require(phrase in disallowed, f"disallowed source missing: {phrase}")

    closes = data["what_closes_now"]
    for key in [
        "approved_reference_source_registry",
        "slot_to_source_mapping",
        "values_fill_contract",
        "source_selection_guardrails_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "numeric_reference_values",
        "value_conversion_formulas",
        "actual_numeric_tree_level_replay",
        "full_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["sm_equivalence_claimed"] is False, "SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    compact_note = " ".join(note.split())
    require("no numeric values are copied" in compact_note, "note value guard missing")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
