"""Audit the determinant-only reduction for the electroweak C1 response."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_C1_Determinant_Reduction_v1.md"
CERT = REPO / "certificates" / "selected_electroweak_c1_determinant_reduction_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_electroweak_c1_response_determinant_only.template.json"
CALCULATOR = REPO / "scripts" / "compute_electroweak_c1_response.py"
HETEROTIC = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
TOPOLOGY = OBSIDIAN / "13 Standard Model & Topology-Only Constraints" / "Topology__Only_Constraints_in_Modal_Triplet_Theory.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run_template() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CALCULATOR), str(TEMPLATE)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = load_json(CERT)
    template = load_json(TEMPLATE)
    note = read(NOTE)
    heterotic = read(HETEROTIC)
    topology = read(TOPOLOGY)
    run = run_template()
    terms = template["raw_response_per_v1"]["terms"]

    zero_terms = {"torsion_curvature", "bundle_index", "scheme_counterterm", "basis_transport"}
    checks = [
        check(
            "certificate status",
            cert["status"] == "PEW_ALPHA1_REDUCED_TO_SELECTED_LOCAL_DETERMINANT",
            cert["status"],
        ),
        check(
            "only local determinant remains open",
            terms["local_determinant"] is None
            and all(terms[term] == [0.0, 0.0, 0.0] for term in zero_terms),
            terms,
        ),
        check(
            "calculator refuses only determinant",
            run.returncode == 2
            and "raw_response_per_v1.terms.local_determinant" in run.stdout
            and "raw_response_per_v1.terms.torsion_curvature" not in run.stdout
            and "raw_response_per_v1.terms.bundle_index" not in run.stdout,
            run.stdout.splitlines(),
        ),
        check(
            "heterotic source supports universal tree kinetic plus uncomputed thresholds",
            contains_all(heterotic, ["g^{-2}=\\mathrm{Re}\\,S", "threshold corrections", "we do not attempt to compute here"]),
            "f=S and thresholds open",
        ),
        check(
            "topology source supports representation bookkeeping not threshold amplitude",
            contains_all(topology, ["Dynkin indices", "multiplicities", "No geometry enters"]),
            "group indices/bookkeeping",
        ),
        check(
            "closed zero terms recorded",
            set(cert["closed_zero_terms"].keys()) == zero_terms
            and cert["verdict"]["reduced_to_single_physical_source"] is True,
            cert["closed_zero_terms"],
        ),
        check(
            "weak split gate is single scalar",
            cert["weak_split_gate"]["lambda_12"] == "p_det,U1 - p_det,SU2"
            and "p_U1 - p_SU2" in note,
            cert["weak_split_gate"],
        ),
        check(
            "no numeric electroweak closure",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        ),
    ]

    print("\nSelected electroweak C1 determinant reduction audit")
    print("===================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())

