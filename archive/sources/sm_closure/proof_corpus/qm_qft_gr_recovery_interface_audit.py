"""Audit the MTT QM/QFT/GR recovery interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "qm_qft_gr_recovery_interface_certificate.json"
DATA = REPO / "candidate_data" / "qm_qft_gr_recovery_interface.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_QM_QFT_GR_Recovery_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_qm_qft_gr_recovery_interface.py"

REQUIRED_INTERFACES = {"QM", "QFT", "GR", "Units"}
REQUIRED_INTERFACE_FIELDS = {"required_maps", "parity_acceptance", "forbidden_shortcut", "no_knob_target"}
REQUIRED_CROSS_CHECKS = {"qm_to_qft", "qft_to_sm", "qft_to_gr", "gr_to_units", "measurement_to_empirical_ledger"}


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
    interfaces = data["recovery_interfaces"]
    interface_fields_ok = all(REQUIRED_INTERFACE_FIELDS.issubset(interfaces[name].keys()) for name in REQUIRED_INTERFACES)
    forbidden_text = " ".join(data["forbidden_shortcuts"]).lower()
    checks = [
        check("status", cert["status"] == "MTT_QM_QFT_GR_RECOVERY_INTERFACE_BUILT_EMPIRICAL_LEDGER_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("interfaces complete", REQUIRED_INTERFACES.issubset(interfaces.keys()), interfaces.keys()),
        check("interface fields complete", interface_fields_ok, interfaces),
        check("cross checks complete", REQUIRED_CROSS_CHECKS.issubset(data["cross_sector_consistency_checks"].keys()), data["cross_sector_consistency_checks"].keys()),
        check("qm gate", gates["qm_recovery_interface_declared"] is True, gates),
        check("qft gate", gates["qft_recovery_interface_declared"] is True, gates),
        check("gr gate", gates["gr_recovery_interface_declared"] is True, gates),
        check("units gate", gates["units_interface_declared"] is True, gates),
        check("measured downstream", gates["measured_values_downstream_of_recovery_maps"] is True, gates),
        check("no hidden no-knob recovery", gates["no_knob_recovery_claimed"] is False, gates),
        check("forbids born overclaim", "born" in forbidden_text and "no-knob derived" in forbidden_text, data["forbidden_shortcuts"]),
        check("forbids measured newton derivation", "newton" in forbidden_text and "derived" in forbidden_text, data["forbidden_shortcuts"]),
        check("forbids hidden unit constants", "unit conventions" in forbidden_text and "hidden" in forbidden_text, data["forbidden_shortcuts"]),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", gates["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note records recovery boundary", "all measured values are downstream" in note and "no-knob targets as open" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Empirical_Equivalence_Ledger_v1", data["next_required_artifact"]),
    ]
    print("\nMTT QM/QFT/GR recovery interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
