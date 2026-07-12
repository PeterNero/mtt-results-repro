"""Audit the selected canonical trace formula source lemma proof."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "prove_selected_canonical_trace_formula_source_lemma.py"
PACKET = DATA / "selected_canonical_trace_formula_source_lemma_proof.candidate.json"
CERT = CERTS / "selected_canonical_trace_formula_source_lemma_proof_certificate.json"
NOTE = ROOT / "proof_corpus" / "Prove_SelectedCanonicalTraceFormulaSourceLemma_v1.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load_json(PACKET)
    cert = load_json(CERT)
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

    expected = "SELECTED_CANONICAL_TRACE_FORMULA_SOURCE_LEMMA_PROVED_GAP_LAYER_CLOSES"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem proved", cert["theorem"]["proved"] is True, cert["theorem"])
    check(
        "every proof step proved",
        all(step["proved"] is True for step in cert["proof_steps"].values()),
        cert["proof_steps"],
    )

    metric = packet["metric_checks"]
    check(
        "canonical finite metric source",
        metric["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3"
        and metric["dimension"] == 27
        and metric["basis_count"] == 27
        and metric["uniform_f3x_f3_fourier_basis"]
        and metric["gram_identity"]
        and metric["stiffness_matches_fourier_formula"],
        metric,
    )
    check(
        "zero cluster retained",
        metric["zero_cluster_indices"] == [12, 13, 14]
        and metric["zero_cluster_basis_ids"]
        == ["phi_(0,0)_e0", "phi_(0,0)_e1", "phi_(0,0)_e2"],
        metric,
    )

    phase = packet["qutrit_phase_checks"]
    check(
        "projective qutrit phase complement",
        phase["metric_status"] == "PROJECTIVE_UNITARY_METRIC_COMPATIBLE"
        and phase["clock_generator_present"]
        and phase["shift_generator_present"]
        and phase["nontrivial_qutrit_phase_complement_indices"] == [13, 14]
        and phase["nontrivial_qutrit_phase_complement_rank"] == 2,
        phase,
    )

    equality = packet["selected_trace_equality"]
    check(
        "selected trace equality promoted only for D_E",
        equality["proved"]
        and equality["family_sectors"] == "canonical F3xF3 Fourier Laplacian"
        and "rank-two projector on indices 13,14" in equality["H_sector"],
        equality,
    )

    gap = cert["gap_layer_consequence"]
    check(
        "gap layer closes",
        gap["D_E_source_flags_may_be_theorem_derived"]
        and gap["selected_eta_N"] == 1.0
        and gap["eta_threshold"] > gap["selected_eta_N"]
        and gap["gap_Riesz_Green_closes"],
        gap,
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"]
        and cert["guardrails"]["does_not_claim_dotD_C1"]
        and cert["guardrails"]["does_not_claim_full_SM_closure"]
        and cert["guardrails"]["source_flags_only_for_D_E_gap_layer"],
        cert["guardrails"],
    )
    check(
        "downstream layers still separate",
        cert["still_separate"]["dotD_alpha1_C1_response"]
        and cert["still_separate"]["Yukawa_or_SM_closure"]
        and cert["still_separate"]["full_selected_operator_payload_beyond_gap_layer"],
        cert["still_separate"],
    )

    note = NOTE.read_text(encoding="utf-8")
    check("note records theorem", "Selected Trace Equality" in note, NOTE)

    print("\nSelected canonical trace formula source lemma proof audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
