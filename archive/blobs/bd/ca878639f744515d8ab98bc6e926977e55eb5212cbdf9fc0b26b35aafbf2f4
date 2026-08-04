"""Audit the attempted full Standard Model closure status."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "full_sm_closure_attempt_certificate.json"
PAPER = ROOT / "Full_SM_Closure_Attempt_and_Exact_Blockers_v1.md"

RANK_ONE_CERT = CERT_DIR / "rank_one_lift_operator_attempt_certificate.json"
JARLSKOG_CERT = CERT_DIR / "jarlskog_closure_criterion_certificate.json"
CKM_NONCOMM_CERT = CERT_DIR / "ckm_leading_noncommutation_criterion_certificate.json"
C1_RANK_CERT = CERT_DIR / "c1_alpha1_rank_lift_criterion_certificate.json"
RG_TEMPLATE = CERT_DIR / "flavor_rg_matching_certificate.template.json"
OVERLAP_TEMPLATE = CERT_DIR / "yukawa_overlap_kernel_certificate.template.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    cert = load_json(CERT)
    rank_one = load_json(RANK_ONE_CERT)
    jarlskog = load_json(JARLSKOG_CERT)
    ckm_noncomm = load_json(CKM_NONCOMM_CERT)
    c1_rank = load_json(C1_RANK_CERT)
    rg_template = load_json(RG_TEMPLATE)
    overlap_template = load_json(OVERLAP_TEMPLATE)
    paper = read(PAPER)

    requirements = cert.get("full_sm_closure_requirements", {})
    open_requirements = [
        name
        for name, item in requirements.items()
        if isinstance(item, dict) and item.get("status") == "OPEN"
    ]

    forbidden = cert.get("forbidden_closure_shortcuts", [])
    claim = cert.get("claim", {})

    required_open = {
        "selected_raw_yukawa_matrices",
        "selected_rank_lift_data",
        "selected_channel_weights",
        "canonical_normalization",
        "quark_observables",
        "charged_lepton_observables",
        "neutral_lepton_sector",
        "higgs_sector",
        "rg_threshold_matching",
    }

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status") == "FULL_SM_CLOSURE_BLOCKED_MISSING_NO_PROXY_SELECTED_DATA"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "no full closure overclaim",
            "PASS" if claim.get("full_standard_model_closure_claimed") is False else "FAIL",
            f"full_standard_model_closure_claimed={claim.get('full_standard_model_closure_claimed')}",
        ),
        Gate(
            "structural embedding support",
            "PASS" if claim.get("standard_model_structural_embedding_supported") is True else "FAIL",
            f"standard_model_structural_embedding_supported={claim.get('standard_model_structural_embedding_supported')}",
        ),
        Gate(
            "no no-proxy flavor overclaim",
            "PASS" if claim.get("no_proxy_flavor_prediction_claimed") is False else "FAIL",
            f"no_proxy_flavor_prediction_claimed={claim.get('no_proxy_flavor_prediction_claimed')}",
        ),
        Gate(
            "rank-one hard-leap dependency",
            "BLOCKED"
            if rank_one.get("status") == "BLOCKED_MISSING_SELECTED_COEFFICIENTS"
            else "FAIL",
            str(rank_one.get("status")),
        ),
        Gate(
            "C1 rank criterion dependency",
            "CRITERION-CLOSED"
            if c1_rank.get("status") == "C1_ALPHA1_RANK_LIFT_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(c1_rank.get("status")),
        ),
        Gate(
            "CKM noncommutation dependency",
            "CRITERION-CLOSED"
            if ckm_noncomm.get("status") == "CKM_LEADING_NONCOMMUTATION_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(ckm_noncomm.get("status")),
        ),
        Gate(
            "Jarlskog dependency",
            "CRITERION-CLOSED"
            if jarlskog.get("status") == "JARLSKOG_CLOSURE_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(jarlskog.get("status")),
        ),
        Gate(
            "overlap-kernel template remains open",
            "OPEN" if overlap_template.get("status") == "OPEN" else "FAIL",
            str(overlap_template.get("status")),
        ),
        Gate(
            "RG template remains open",
            "OPEN" if rg_template.get("status") == "OPEN" else "FAIL",
            str(rg_template.get("status")),
        ),
        Gate(
            "required open objects listed",
            "EXPECTED"
            if required_open.issubset(set(open_requirements))
            else "FAIL",
            ", ".join(open_requirements),
        ),
        Gate(
            "forbidden shortcuts listed",
            "PASS" if len(forbidden) >= 6 else "FAIL",
            f"{len(forbidden)} forbidden shortcuts",
        ),
        Gate(
            "paper states not proved",
            "PASS" if "Full SM closure is not proved yet." in paper else "FAIL",
            "explicit no-overclaim sentence present",
        ),
        Gate(
            "paper states selected-data theorem",
            "PASS" if "Selected Full SM Data Theorem" in paper else "FAIL",
            "next theorem named",
        ),
    ]

    print("Full SM closure attempt audit")
    print("=============================")
    print()
    print(f"status={cert.get('status')}")
    print(f"open_requirement_count={len(open_requirements)}")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
