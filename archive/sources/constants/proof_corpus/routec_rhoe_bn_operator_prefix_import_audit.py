"""Audit RouteC_RhoE_BN_Operator_Prefix_Import_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "routec_rhoe_bn_operator_prefix_import_certificate.json"
SCRIPT = REPO / "scripts" / "import_routec_rhoe_bn_operator_prefix.py"
NOTE = REPO / "proof_corpus" / "RouteC_RhoE_BN_Operator_Prefix_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    script_cert = json.loads(proc.stdout)
    closed = cert["closed_now"]
    finite = cert["finite_prefix_summary"]
    not_closed = cert["not_closed"]
    guards = cert["guardrails"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "ROUTEC_RHOE_BN_OPERATOR_PREFIX_IMPORTED_NONINVARIANT_C1_PRIMITIVE_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "finite prefix closes",
        closed["nonidentity_projective_rhoE_candidate_built"] is True
        and closed["smooth_BN_27_mode_scaffold_built"] is True
        and closed["D_E_matrix_on_27_mode_BN_emitted"] is True
        and closed["sector_projectors_and_dotD_same_basis_emitted"] is True,
        closed,
    )
    ok &= check(
        "canonical C1 zero-response no-go retained",
        closed["canonical_C1_contraction_engine_built"] is True
        and closed["canonical_C1_zero_response_no_go_proved"] is True
        and finite["C1"]["all_c1_matrices_zero_for_canonical_tensor"] is True,
        finite["C1"],
    )
    ok &= check(
        "numerical spine sane",
        finite["rho_E"]["rank"] == 3
        and finite["B_N"]["dimension"] == 27
        and finite["B_N"]["zero_cluster_dimension"] == 3
        and finite["D_E"]["family_kernel_dimension"] == 3
        and finite["D_E"]["higgs_kernel_dimension"] == 1,
        finite,
    )
    ok &= check(
        "true gates remain open",
        not_closed["selected_noninvariant_C1_primitive_or_vertex"] is True
        and not_closed["selected_basis_transport_between_zero_and_response_modes"] is True
        and not_closed["nonzero_C1_response_matrices"] is True
        and not_closed["yukawa_CKM_PMNS_magnitudes"] is True,
        not_closed,
    )
    ok &= check(
        "guardrails prevent overclaim",
        guards["claims_selected_source_flags_promoted"] is False
        and guards["claims_nonzero_C1_response"] is False
        and guards["claims_yukawa_CKM_PMNS_magnitudes"] is False
        and guards["claims_full_SM_closure"] is False,
        guards,
    )
    ok &= check(
        "note records next gate",
        "Selected_RouteC_NonInvariant_C1_Primitive_or_BasisTransport_Search_v1" in note
        and "canonical C1 response matrices: zero" in note,
        NOTE,
    )

    print("\nRouteC rhoE/BN operator prefix import audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
