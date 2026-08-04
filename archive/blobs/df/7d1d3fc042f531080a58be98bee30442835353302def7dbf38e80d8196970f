"""Audit primitive C1 fiberclass higher-order frontier import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_primitive_c1_fiberclass_higherorder_frontier.py"
PACKET = ROOT / "candidate_data" / "primitive_c1_fiberclass_higherorder_frontier_import.candidate.json"
CERT = ROOT / "certificates" / "primitive_c1_fiberclass_higherorder_frontier_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Primitive_C1_Fiberclass_HigherOrder_Frontier_Import_v1.md"

STATUS = "PRIMITIVE_C1_FIBERCLASS_QUOTIENT_CLOSED_HIGHERORDER_FULLRESPONSE_FRONTIER_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    print(f"{'PASS' if condition else 'FAIL'}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    check("status", cert["status"] == STATUS, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem proved", packet["theorem"]["proved"] is True, packet["theorem"])
    check("all checks pass", all(packet["checks"].values()), packet["checks"])

    atom = packet["primitive_atom_chain"]
    check(
        "atom interface and no-go retained",
        atom["interface_certificate"]["missing_atom_count"] == 24
        and atom["fill_nogo_certificate"]["missing_leaf_count"] == 40
        and atom["fill_nogo_certificate"]["current_corpus_supplies_selected_atom_payload"] is False
        and atom["sourcevalue_certificate"]["sourcevalue_contract_built"],
        atom,
    )

    reduction = packet["noninvariant_and_fiberclass_reduction"]
    check(
        "noninvariant and fiberclass reduction imported",
        reduction["external_certificate"]["minimal_active_shift_required"] == [1, 1]
        and reduction["external_certificate"]["nonzero_unselected_candidate_count"] == 4
        and reduction["fiberclass_certificate"]["fiberclass_quotient_for_current_C1_spectral_observables_closed"]
        and reduction["fiberclass_certificate"]["selected_matrix_representative_for_full_C1_operator"] is False,
        reduction["fiberclass_certificate"],
    )

    tests = packet["primitiveclass_higherorder_frontier"]["packet"]["primitive_layer_tests"]
    check(
        "primitive class scalar-degenerate",
        tests["all_yy_star_scalar_identity"]
        and tests["max_traceless_norm_sq"] == 0.0
        and tests["max_commutator_norm_sq"] == 0.0
        and tests["mass_splitting_test_passes"] is False
        and tests["mixing_commutator_test_passes"] is False
        and tests["cp_odd_test_passes"] is False,
        tests,
    )

    update = packet["frontier_update"]
    check(
        "frontier advances to correction/full-response source",
        update["old_next"] == "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1"
        and update["current_next"] == NEXT,
        update,
    )
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "active shift = (1,1)",
        "Y_s Y_s^* = c I",
        "selected correction/full-response matrices",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nPrimitive C1 fiberclass higher-order frontier import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
