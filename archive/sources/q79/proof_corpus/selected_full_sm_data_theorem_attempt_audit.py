"""Audit the selected full-SM-data theorem execution attempt."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "selected_full_sm_data_theorem_attempt_certificate.json"
FULL_SM_CERT = CERT_DIR / "full_sm_closure_attempt_certificate.json"
OVERLAP_TEMPLATE = CERT_DIR / "yukawa_overlap_kernel_certificate.template.json"
RG_TEMPLATE = CERT_DIR / "flavor_rg_matching_certificate.template.json"
WEIGHT_CERT = CERT_DIR / "selected_channel_weight_extraction_protocol_certificate.json"
C1_RANK_CERT = CERT_DIR / "c1_alpha1_rank_lift_criterion_certificate.json"
CKM_NONCOMM_CERT = CERT_DIR / "ckm_leading_noncommutation_criterion_certificate.json"
PAPER = ROOT / "Selected_Full_SM_Data_Theorem_Execution_Attempt_v1.md"
EXEC_II = ROOT / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md"


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


def det2(block: list[list[int]]) -> int:
    return block[0][0] * block[1][1] - block[0][1] * block[1][0]


def main() -> None:
    cert = load_json(CERT)
    full_sm = load_json(FULL_SM_CERT)
    overlap = load_json(OVERLAP_TEMPLATE)
    rg = load_json(RG_TEMPLATE)
    weight = load_json(WEIGHT_CERT)
    c1_rank = load_json(C1_RANK_CERT)
    ckm_noncomm = load_json(CKM_NONCOMM_CERT)
    paper = read(PAPER)
    exec_ii = read(EXEC_II)

    attempt = cert.get("attempt_result", {})
    missing = cert.get("missing_selected_inputs", {})
    rejected = cert.get("rejected_proxy_inputs_found", {})
    witness = cert.get("underdetermination_witness", {})
    rank_witnesses = witness.get("rank_lift_minor_completions", [])
    orientation_witnesses = witness.get("ckm_orientation_completions", [])

    computed_minors = [
        det2(item["light_block"])
        for item in rank_witnesses
        if "light_block" in item
    ]
    supplied_minors = [item.get("minor_C33") for item in rank_witnesses]
    orientations_nonzero = [
        any(component != 0 for component in item.get("Delta_v", []))
        for item in orientation_witnesses
    ]

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status") == "SELECTED_FULL_SM_DATA_THEOREM_NOT_PROVED_SELECTED_DATA_ABSENT"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "full SM closure dependency",
            "BLOCKED"
            if full_sm.get("status") == "FULL_SM_CLOSURE_BLOCKED_MISSING_NO_PROXY_SELECTED_DATA"
            else "FAIL",
            str(full_sm.get("status")),
        ),
        Gate(
            "actual matrices not claimed",
            "PASS"
            if attempt.get("actual_selected_raw_matrices_computed") is False
            and attempt.get("actual_selected_canonical_matrices_computed") is False
            else "FAIL",
            str(attempt),
        ),
        Gate(
            "theorem not claimed",
            "PASS" if attempt.get("safe_to_claim_theorem") is False else "FAIL",
            f"safe_to_claim_theorem={attempt.get('safe_to_claim_theorem')}",
        ),
        Gate(
            "overlap template still open",
            "OPEN" if overlap.get("status") == "OPEN" else "FAIL",
            str(overlap.get("status")),
        ),
        Gate(
            "RG template still open",
            "OPEN" if rg.get("status") == "OPEN" else "FAIL",
            str(rg.get("status")),
        ),
        Gate(
            "weight protocol forbids benchmark inputs",
            "PASS"
            if "Execution II benchmark matrix entries"
            in weight.get("forbidden_inputs", [])
            else "FAIL",
            "Execution II benchmark matrix entries forbidden",
        ),
        Gate(
            "C1 rank criterion only",
            "CRITERION-CLOSED"
            if c1_rank.get("status") == "C1_ALPHA1_RANK_LIFT_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(c1_rank.get("status")),
        ),
        Gate(
            "CKM noncommutation criterion only",
            "CRITERION-CLOSED"
            if ckm_noncomm.get("status") == "CKM_LEADING_NONCOMMUTATION_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(ckm_noncomm.get("status")),
        ),
        Gate(
            "proxy benchmark detected but rejected",
            "PASS"
            if "benchmark" in exec_ii.lower()
            and rejected.get("execution_ii_yukawa_matrices") == "BENCHMARK_NOT_SELECTED_DATA"
            else "FAIL",
            "Execution II matrices exist but are rejected as theorem inputs",
        ),
        Gate(
            "missing input groups listed",
            "EXPECTED" if len(missing) == 5 else "FAIL",
            ", ".join(sorted(missing)),
        ),
        Gate(
            "rank witness minors computed",
            "PASS"
            if computed_minors == supplied_minors
            and len(set(computed_minors)) == 2
            and all(value != 0 for value in computed_minors)
            else "FAIL",
            f"computed={computed_minors}, supplied={supplied_minors}",
        ),
        Gate(
            "CKM witness orientations nonzero",
            "PASS"
            if len(orientation_witnesses) == 2 and all(orientations_nonzero)
            else "FAIL",
            str([item.get("Delta_v") for item in orientation_witnesses]),
        ),
        Gate(
            "paper states underdetermination",
            "PASS" if "underdetermination result" in paper else "FAIL",
            "paper names the obstruction",
        ),
        Gate(
            "paper names next certificate",
            "PASS" if "SelectedOverlapKernelAndMetricDataCertificate" in paper else "FAIL",
            "next selected-data certificate named",
        ),
    ]

    print("Selected full-SM-data theorem execution attempt audit")
    print("=====================================================")
    print()
    print(f"status={cert.get('status')}")
    print(f"rank_witness_minors={computed_minors}")
    print(f"orientation_witnesses={[item.get('Delta_v') for item in orientation_witnesses]}")
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
