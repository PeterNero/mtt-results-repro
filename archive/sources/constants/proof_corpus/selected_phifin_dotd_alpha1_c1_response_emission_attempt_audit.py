"""Audit the selected Phi_fin dotD/alpha1/C1 response emission attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "attempt_selected_phifin_dotd_alpha1_c1_response_emission.py"
PACKET = DATA / "selected_phifin_dotd_alpha1_c1_response_emission_attempt.candidate.json"
CERT = CERTS / "selected_phifin_dotd_alpha1_c1_response_emission_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_PhiFin_dotD_alpha1_C1_Response_Emission_Attempt_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
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

    expected = "SELECTED_PHIFIN_DOTD_ALPHA1_C1_RESPONSE_FRONTIER_SHARPENED"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])

    prefix = packet["closed_prefix"]
    check(
        "closed prefix consumes D_E lock",
        prefix["selected_D_E_gap_Riesz_Green_locked"]
        and prefix["same_basis_as_locked_D_E"]
        and prefix["dotD_alpha1_value_matrices_emitted"]
        and prefix["sector_projectors_clean"]
        and prefix["finite_horizontal_response_diagnostic_passes"]
        and prefix["dotD_alpha1_has_nonzero_entries"]
        and prefix["target_fitting_excluded"],
        prefix,
    )

    dotd = packet["dotD_value_packet"]
    check(
        "dotD packet same basis and honest cutset",
        dotd["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3"
        and dotd["honest_replay"]["exit_code"] == 1
        and dotd["honest_replay_fails_only_by_source_driver_flags"],
        dotd["honest_replay"],
    )
    check(
        "sector projectors and dotD shapes",
        dotd["sector_slots"]["Q"]["dotD_alpha1_matrix_shape"] == [27, 27]
        and dotd["sector_slots"]["Q"]["projector_rank_trace"] == 3.0
        and dotd["sector_slots"]["H"]["projector_rank_trace"] == 1.0
        and dotd["sector_slots"]["H"]["dotD_alpha1_nonzero_entries"] > 0,
        {
            "Q": dotd["sector_slots"]["Q"],
            "H": dotd["sector_slots"]["H"],
        },
    )

    c1 = packet["c1_response_emission"]
    check(
        "C1 not emitted",
        c1["A_selected_emitted"] is False
        and c1["b_selected_emitted"] is False
        and c1["sector_response_matrices_emitted"] is False
        and c1["can_emit_c1_response_now"] is False,
        c1,
    )
    remaining = packet["remaining_gates"]
    check(
        "remaining gates are exact",
        remaining["selected_dotD_source_theorem"]
        and remaining["same_branch_alpha1_driver_theorem"]
        and remaining["retarded_overlap_source_vector_b_selected"]
        and remaining["finite_Hess_Xi_blocks"]
        and remaining["selected_zero_mode_bases"]
        and remaining["primitive_C1_contractions"]
        and remaining["sector_response_matrices"],
        remaining,
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_promote_dotD_flags"]
        and cert["guardrails"]["does_not_claim_alpha1_driver"]
        and cert["guardrails"]["does_not_claim_A_selected_or_b_selected"]
        and cert["guardrails"]["does_not_claim_Yukawa_or_SM_closure"]
        and cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"]
        and cert["guardrails"]["uses_locked_D_E_only_as_gap_layer_input"],
        cert["guardrails"],
    )
    check(
        "next artifact named",
        cert["verdict"]["next_required_artifact"]
        == "Selected_dotD_alpha1_Source_and_Driver_Theorem_v1",
        cert["verdict"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records boundary", "does not promote `dotD` flags" in note, NOTE)

    print("\nSelected PhiFin dotD alpha1 C1 response emission attempt audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
