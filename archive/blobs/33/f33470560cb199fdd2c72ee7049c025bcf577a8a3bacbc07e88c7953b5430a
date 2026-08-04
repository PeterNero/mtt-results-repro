"""Audit the reduced Kunneth proof of the remaining V_alpha Yoneda scalar."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "prove_valpha_kunneth_yoneda_scalar.py"
CERT = ROOT / "certificates" / "valpha_kunneth_yoneda_scalar_proof_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "valpha_kunneth_yoneda_scalar_proof.candidate.json"
MATRIX = (
    ROOT
    / "candidate_data"
    / "valpha_kunneth_yoneda_scalar"
    / "reduced_kunneth_yoneda_matrix.json"
)
PAPER = CORPUS / "VAlpha_Kunneth_Yoneda_Scalar_Proof_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: object


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    matrix = load(MATRIX)
    paper = read(PAPER)

    proof = cert.get("reduced_kunneth_yoneda_scalar", {})
    closed = cert.get("closed_by_this_attempt", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    expected_status = "VALPHA_KUNNETH_YONEDA_SCALAR_PROVED_REDUCED_MODEL_FULL_STABILITY_OPEN"
    expected_matrix = [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("matrix exists", "PASS" if MATRIX.exists() else "FAIL", MATRIX),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status expected",
            "PASS" if cert.get("status") == expected_status else "FAIL",
            cert.get("status"),
        ),
        Gate("candidate mirrors cert", "PASS" if candidate == cert else "FAIL", candidate.get("status")),
        Gate("matrix mirrors embedded", "PASS" if matrix == proof else "FAIL", matrix.get("status")),
        Gate(
            "factor matrices",
            "PASS"
            if proof.get("positive_factor", {}).get("matrix") == [[1, 0], [0, 1], [0, 0]]
            and proof.get("positive_factor", {}).get("rank") == 2
            and proof.get("negative_factor", {}).get("matrix")
            == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
            and proof.get("negative_factor", {}).get("rank") == 3
            else "FAIL",
            {"positive": proof.get("positive_factor"), "negative": proof.get("negative_factor")},
        ),
        Gate(
            "Kronecker matrix exact",
            "PASS"
            if proof.get("kunneth_matrix") == expected_matrix
            and proof.get("matrix_rank") == 6
            else "FAIL",
            proof.get("kunneth_matrix"),
        ),
        Gate(
            "selected vector nonzero",
            "PASS"
            if proof.get("selected_ext_label") == "theta_plus_0_tensor_eta_minus_0"
            and proof.get("selected_ext_vector") == [1, 0, 0, 0, 0, 0, 0, 0]
            and proof.get("target_vector") == [1, 0, 0, 0, 0, 0, 0, 0, 0]
            and proof.get("target_vector_nonzero") is True
            else "FAIL",
            proof.get("target_vector"),
        ),
        Gate(
            "kernel labels",
            "PASS"
            if proof.get("kernel_basis_labels_in_this_order")
            == ["theta_plus_0_tensor_eta_minus_3", "theta_plus_1_tensor_eta_minus_3"]
            else "FAIL",
            proof.get("kernel_basis_labels_in_this_order"),
        ),
        Gate(
            "prior scalar attempt matched",
            "PASS"
            if closed.get("canonical_ladder_derived_from_kunneth_serre_duality") is True
            and closed.get("prior_canonical_packet_matched") is True
            and closed.get("selected_reduced_kunneth_scalar_nonzero") is True
            and closed.get("finite_branch_candidate_M_minus2_1_0_obstructed_in_reduced_model")
            is True
            else "FAIL",
            closed,
        ),
        Gate(
            "still open guarded",
            "OPEN"
            if still_open.get("complete_destabilizing_subsheaf_enumeration") is True
            and still_open.get(
                "promote_reduced_kunneth_to_raw_good_cover_cech_or_appell_humbert_multiplication"
            )
            is True
            and still_open.get("selected_hym_or_strominger_existence_certificate") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            still_open,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records proof and caveats",
            "PASS"
            if contains_all(
                paper,
                [
                    "VAlpha Kunneth Yoneda Scalar Proof",
                    "Serre-dual transpose",
                    "Kronecker product",
                    "target vector is nonzero",
                    "selected reduced Kunneth model",
                    "not full V_alpha stability",
                    "does not prove HYM existence or full SM closure",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("V_alpha Kunneth Yoneda scalar proof audit")
    print("=========================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:<{width}}  {gate.status:<{status_width}}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        print("\nFailures")
        print("--------")
        for failure in failures:
            print(f"- {failure.label}: {failure.detail}")
        return 1

    print("\nResult: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
