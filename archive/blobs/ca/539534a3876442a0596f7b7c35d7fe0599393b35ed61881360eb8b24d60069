"""Audit PSM-C1-02 pre-residual Weyl normal form / honest quadrature gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
NORMAL_FORM = PACKET_DIR / "psm_c1_02_preresidual_weyl_normal_form.packet.json"
ROUTE_A = PACKET_DIR / "route_a_physical_selection_lemma_attempt.packet.json"
ROUTE_A_RESULT = PACKET_DIR / "route_a_physical_selection_lemma_validator_result.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_quadrature_source_contract.packet.json"
EXIT = PACKET_DIR / "psm_c1_02_two_route_exit_matrix.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PreResidualWeylVariationSelectionLemma_or_HonestQuadratureSource_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"

STATUS = "MTT_SELECTED_PRERESIDUALWEYLVARIATIONSELECTIONLEMMA_OR_HONESTQUADRATURESOURCE_BUILT_NORMAL_FORM_SELECTION_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    normal = load(NORMAL_FORM)
    route_a = load(ROUTE_A)
    route_a_result = load(ROUTE_A_RESULT)
    route_b = load(ROUTE_B)
    exit_matrix = load(EXIT)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ROUTE_A)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    require(data["status"] == STATUS, "status mismatch")
    require(data["active_post_sm_parity_label"] == "PSM-C1-02", "active label mismatch")
    require(data["post_sm_parity_label_context"]["closed_boundary"] == "DONE-PARITY-00", "frozen boundary missing")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["PSM_C1_02_closed_unpatched"] is False, "PSM-C1-02 overclosed")
    require(normal["active_label"] == "PSM-C1-02", "normal form label mismatch")
    require(normal["normal_form_checks"]["R_Z_reconstruction_error_norm_sq"] < 1e-24, "R_Z reconstruction too large")
    require(normal["normal_form_checks"]["R_X_reconstruction_error_norm_sq"] < 1e-24, "R_X reconstruction too large")
    require("R_Z" in normal["exact_polynomial_form"], "R_Z formula missing")
    require("R_X" in normal["exact_polynomial_form"], "R_X formula missing")
    require(route_a["route_label"] == "ROUTE-A", "Route A label mismatch")
    require(route_a["physical_action_equals_c1_defect_functional"] is False, "action identity overclaimed")
    require(route_a["same_source_rz_rx_bselected_emitted"] is False, "same source emission overclaimed")
    require(route_a_result["passes"] is False and proc.returncode == 1, "Route A should fail strict validator")
    require(any("physical_action_equals_c1_defect_functional" in line for line in route_a_result["stderr_lines"]), "missing action identity failure")
    require(route_b["route_label"] == "ROUTE-B", "Route B label mismatch")
    require(route_b["honest_quadrature_source_emitted_now"] is False, "honest quadrature overclaimed")
    require(exit_matrix["route_A"]["normal_form_candidates_ready"] is True, "exit matrix missing normal form")
    require(exit_matrix["route_B"]["honest_quadrature_source_emitted_now"] is False, "exit matrix overclaims Route B")
    require(next_work["active_label"] == "PSM-C1-02", "next work active label mismatch")
    require(next_work["primary"]["route_label"] == "ROUTE-A", "next primary route mismatch")
    require(next_work["secondary"]["route_label"] == "ROUTE-B", "next secondary route mismatch")
    require(cert["closure_claimed"] is False, "cert overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("Active post-SM-parity label: `PSM-C1-02`" in note, "note missing label")
    require("not an SM-parity blocker" in note, "note missing boundary language")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
