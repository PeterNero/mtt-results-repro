"""Audit the MTT SM sector embedding interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "sm_sector_embedding_interface_certificate.json"
DATA = REPO / "candidate_data" / "sm_sector_embedding_interface.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_SM_Sector_Embedding_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_sm_sector_embedding_interface.py"

REQUIRED_PACKET_FIELDS = {
    "sector_name",
    "gauge_carrier",
    "representation_packet",
    "family_index",
    "operator_packet",
    "anomaly_conditions",
    "locality_limit",
    "renormalization_interface",
    "measured_slot_boundary",
}
SOURCE_COMPONENTS = {"gauge_group", "fermion_representations", "three_generations", "higgs_carrier"}
MEASURED_COMPONENTS = {"gauge_couplings", "yukawa_matrices", "cp_phases", "higgs_parameters"}


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
    components = data["sm_required_components"]
    forbidden_text = " ".join(data["forbidden_imports"]).lower()
    source_ok = all(components[name]["status"] == "SELECTED_SOURCE_DATA_REQUIRED" for name in SOURCE_COMPONENTS)
    measured_ok = all("MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION" == components[name]["status"] for name in MEASURED_COMPONENTS)
    checks = [
        check("status", cert["status"] == "MTT_SM_SECTOR_EMBEDDING_INTERFACE_BUILT_RECOVERY_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("packet fields complete", REQUIRED_PACKET_FIELDS.issubset(data["selected_packet_fields"].keys()), data["selected_packet_fields"].keys()),
        check("source components classified", source_ok, {name: components[name]["status"] for name in SOURCE_COMPONENTS}),
        check("measured components classified", measured_ok, {name: components[name]["status"] for name in MEASURED_COMPONENTS}),
        check("source/measured separated", gates["source_data_separated_from_measured_slots"] is True, gates),
        check("measured cannot select packet", gates["measured_values_do_not_select_sm_packet"] is True, gates),
        check("anomaly and observable required", gates["anomaly_and_observable_map_required"] is True, gates),
        check("forbidden mass-to-family", "masses" in forbidden_text and "family" in forbidden_text, data["forbidden_imports"]),
        check("forbidden coupling-to-gauge", "gauge coupling" in forbidden_text and "su3" in forbidden_text, data["forbidden_imports"]),
        check("forbidden benchmark matrices", "benchmark" in forbidden_text and "matrices" in forbidden_text, data["forbidden_imports"]),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", gates["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note records boundary", "Measured values may then enter only downstream" in note and "They may not select the SM packet" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_QM_QFT_GR_Recovery_Interface_v1", data["next_required_artifact"]),
    ]
    print("\nMTT SM sector embedding interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
