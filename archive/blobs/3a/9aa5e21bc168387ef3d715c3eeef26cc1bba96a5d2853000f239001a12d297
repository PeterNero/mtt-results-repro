"""Build the selected U1/hypercharge operator-spectrum source packet gate.

This follows the U1/hypercharge local determinant attempt.  The goal is to test
whether the current corpus/repo state emits the actual U1/hypercharge threshold
operator spectrum on V/<s>, rather than only structural hypercharge data,
diagnostic scalar spectra, or already-counted Qa/SU3 internal determinants.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "u1_hypercharge_attempt": DATA / "selected_u1_hypercharge_local_determinant_spectrum_attempt.candidate.json",
    "qa_response": DATA / "selected_response_functional_chi_qa.candidate.json",
    "hypercharge_embedding": NONSM / "certificates" / "hypercharge_embedding_gate_certificate.json",
    "hypercharge_interface": NONSM / "certificates" / "selected_hypercharge_normalized_threshold_interface_certificate.json",
    "spectral_template": NONSM / "certificates" / "selected_local_determinant_spectrum.template.json",
    "diagnostic_spectral_table": NONSM / "certificates" / "selected_gauge_factor_spectral_table_candidate_certificate.json",
    "sm_structural_packet": SM / "candidate_data" / "actual_selected_sm_packet_anomaly_audit.candidate.json",
}

SOURCE_TEXTS = {
    "topology_only_hypercharge": TEXPAPERS / "13 Standard Model & Topology-Only Constraints" / "_md" / "Topology__Only_Constraints_in_Modal_Triplet_Theory.md",
    "heterotic_flux_monad": TEXPAPERS / "16 Strings, Flux, & M-Theory Encodings" / "_md" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "theta_gauge_couplings": TEXPAPERS / "18 Theta-Closure & Execution Program" / "_md_v3_corrected" / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md",
}

OUTPUT_DATA = DATA / "selected_u1_hypercharge_operator_spectrum_source_packet.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1_hypercharge_operator_spectrum_source_packet_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_Hypercharge_Operator_Spectrum_Source_Packet_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def text_terms(path: Path, terms: list[str]) -> dict[str, bool]:
    if not path.exists():
        return {term: False for term in terms}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {term: term.lower() in text for term in terms}


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    attempt = load(INPUTS["u1_hypercharge_attempt"])
    qa_response = load(INPUTS["qa_response"])
    hyper = load(INPUTS["hypercharge_embedding"])
    interface = load(INPUTS["hypercharge_interface"])
    template = load(INPUTS["spectral_template"])
    diagnostic = load(INPUTS["diagnostic_spectral_table"])
    sm_packet = load(INPUTS["sm_structural_packet"])

    closed = attempt["hypercharge_gate"]["closed_part"]
    p_qc = float(closed["Qc_circle_block"])
    p_su2 = float(closed["SU2_block"])
    p_qa_internal = math.log(2008.0)
    p_y_if_qa_logdet_reused = p_qa_internal / 36.0 + p_qc / 4.0
    lambda_12_if_qa_logdet_reused = p_y_if_qa_logdet_reused - p_su2
    target_witness = attempt["hypercharge_gate"]["target_witness_not_used"]

    source_scans = {
        "topology_only_hypercharge": {
            "path": str(SOURCE_TEXTS["topology_only_hypercharge"]),
            "present": SOURCE_TEXTS["topology_only_hypercharge"].exists(),
            "terms": text_terms(SOURCE_TEXTS["topology_only_hypercharge"], ["hypercharge", "difference charges", "anomaly", "Dirac operator"]),
            "classification": "STRUCTURAL_CHARGE_AND_ANOMALY_SUPPORT_ONLY",
        },
        "heterotic_flux_monad": {
            "path": str(SOURCE_TEXTS["heterotic_flux_monad"]),
            "present": SOURCE_TEXTS["heterotic_flux_monad"].exists(),
            "terms": text_terms(SOURCE_TEXTS["heterotic_flux_monad"], ["monad", "line bundles", "HYM", "spectrum", "threshold"]),
            "classification": "BUNDLE_AND_HYM_CONTEXT_NOT_U1_SPECTRUM",
        },
        "theta_gauge_couplings": {
            "path": str(SOURCE_TEXTS["theta_gauge_couplings"]),
            "present": SOURCE_TEXTS["theta_gauge_couplings"].exists(),
            "terms": text_terms(SOURCE_TEXTS["theta_gauge_couplings"], ["GUT-normalized", "hypercharge", "g_1", "threshold"]),
            "classification": "PHENOMENOLOGICAL_GAUGE_SCAFFOLD_NOT_SOURCE_SPECTRUM",
        },
    }

    route_tests = {
        "topology_only_hypercharge_embedding": {
            "status": "REJECTED_AS_SPECTRUM_SOURCE",
            "what_it_supplies": [
                "SM hypercharge/difference-charge structure",
                "anomaly and representation-selection constraints",
                "normalization convention clues",
            ],
            "missing_for_operator_spectrum": [
                "positive eigenvalues on V/<s>",
                "operator domain or boundary conditions",
                "multiplicities and threshold index weights",
                "heat/zeta/torsion finite part",
            ],
            "reason": "Topology-only hypercharge selects charges and consistency constraints, but deliberately avoids metric or harmonic spectral data.",
        },
        "diagnostic_scalar_spectral_table": {
            "status": "REJECTED_PROXY_NOT_SELECTED_OPERATOR",
            "source_status": diagnostic["status"],
            "reason": "The non-SM spectral-table pipeline is reproducible, but its own certificate marks final spectra open and uses proxy scalar Laplacians/unit weights.",
        },
        "qa_log2008_hypercharge_injection": {
            "status": "REJECTED_WRONG_SCHEME_AND_DOUBLE_PROMOTION",
            "p_Qa_internal_log2008": p_qa_internal,
            "p_Qc_closed": p_qc,
            "p_SU2_closed": p_su2,
            "p_Y_if_reused": p_y_if_qa_logdet_reused,
            "lambda_12_if_reused": lambda_12_if_qa_logdet_reused,
            "target_witness_not_used": target_witness,
            "absolute_residual_to_witness": abs(lambda_12_if_qa_logdet_reused - target_witness),
            "reason": "Delta_Qa=log(2008) is a selected internal reduced Qa/SU3 determinant, not the emitted hypercharge U1 threshold operator spectrum or same-scheme stack determinant row.",
        },
        "same_source_operator_spectrum_packet": {
            "status": "OPEN_PRIMARY_ROUTE",
            "required_fields": [
                "operator identity: Laplace/Dirac/Weitzenbock/BRST threshold operator for U1/Y on V/<s>",
                "domain: selected compact quotient, boundary condition, zero-mode policy, and quotient projector P_perp",
                "spectrum: positive eigenvalues with multiplicities",
                "weights: hypercharge/index/Dynkin weights selected before electroweak comparison",
                "finite part: zeta/heat/torsion regularization and scale convention",
                "source proof: emitted from topology/heterotic section-ring/twisted-module data, not from lambda_12",
            ],
        },
    }

    acceptance_contract = {
        "must_be_same_source_as": [
            "selected U1 quotient carrier V/<s>",
            "hypercharge embedding Y=(1/6)Q_a-(1/2)Q_c if physical hypercharge is used",
            "closed Qc and SU2 blocks already used in lambda_12 accounting",
        ],
        "must_not_use": [
            "observed sin^2(theta_W), alpha_EM, gauge couplings, or lambda_12 residual",
            "P_perp identity spectrum",
            "central-circle determinant reused after quotient",
            "Qa log(2008) as a substitute for a U1/Y operator row",
            "diagnostic scalar-proxy spectral table as final threshold data",
        ],
        "closed_now": {
            "source_packet_acceptance_contract": True,
            "three_bad_fill_routes_rejected": True,
            "hypercharge_structural_support_confirmed": True,
            "selected_spectrum_emitted": False,
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
        },
    }

    candidate = {
        "candidate": "SelectedU1HyperchargeOperatorSpectrumSourcePacket",
        "status": "U1_HYPERCHARGE_OPERATOR_SPECTRUM_SOURCE_PACKET_BUILT_SPECTRUM_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "source_scans": source_scans,
        "source_status": {
            "hypercharge_embedding_status": hyper["status"],
            "hypercharge_interface_status": interface["status"],
            "spectral_template_status": template["status"],
            "sm_structural_packet_status": sm_packet["status"],
            "qa_response_status": qa_response["status"],
        },
        "route_tests": route_tests,
        "acceptance_contract": acceptance_contract,
        "decision": {
            "operator_spectrum_source_packet_built": True,
            "selected_U1_hypercharge_operator_spectrum_found": False,
            "selected_lambda_12_found": False,
            "primary_next_object": "Selected_U1_Hypercharge_Section_Ring_or_Twisted_Module_Operator_Row_v1",
            "target_fitting_used": False,
        },
        "closure_claimed": True,
        "closure_scope": "interface_contract_and_current_source_no_go_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1HyperchargeOperatorSpectrumSourcePacket",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "acceptance_contract": True,
            "topology_only_route_rejected_as_spectrum_source": True,
            "diagnostic_scalar_spectral_table_rejected_as_final_source": True,
            "qa_log2008_injection_rejected_as_hypercharge_operator_row": True,
            "no_target_fit_used": True,
        },
        "open": {
            "selected_U1_hypercharge_operator_identity": True,
            "selected_domain_boundary_zero_mode_policy": True,
            "selected_positive_spectrum_and_multiplicities": True,
            "selected_hypercharge_index_weights": True,
            "selected_zeta_heat_torsion_finite_part": True,
            "lambda_12": True,
        },
        "next_required_object": candidate["decision"]["primary_next_object"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    tests = candidate["route_tests"]
    contract = candidate["acceptance_contract"]
    required = "\n".join(f"- {x}" for x in tests["same_source_operator_spectrum_packet"]["required_fields"])
    forbidden = "\n".join(f"- {x}" for x in contract["must_not_use"])
    scans = "\n".join(
        f"- `{name}`: {scan['classification']} (present={str(scan['present']).lower()}, terms={scan['terms']})"
        for name, scan in candidate["source_scans"].items()
    )
    qa_diag = tests["qa_log2008_hypercharge_injection"]
    return f"""# Selected U1 Hypercharge Operator Spectrum Source Packet v1

## Result

```text
selected_U1_hypercharge_operator_spectrum_found = false
selected_lambda_12_found = false
target_fitting_used = false
closure_scope = interface_contract_and_current_source_no_go_only
```

This packet is the strict successor to the local determinant spectrum attempt.
It asks whether the current source state emits the actual U1/hypercharge
threshold operator spectrum on `V/<s>`. It does not.

## Source Scan

{scans}

## Rejected Fill Routes

### Topology-Only Hypercharge

```text
status = {tests["topology_only_hypercharge_embedding"]["status"]}
reason = {tests["topology_only_hypercharge_embedding"]["reason"]}
```

Topology-only hypercharge and anomaly cancellation are structural support, not
positive determinant eigenvalues.

### Diagnostic Scalar Spectral Table

```text
status = {tests["diagnostic_scalar_spectral_table"]["status"]}
source_status = {tests["diagnostic_scalar_spectral_table"]["source_status"]}
reason = {tests["diagnostic_scalar_spectral_table"]["reason"]}
```

### Qa log(2008) Hypercharge Injection

```text
status = {qa_diag["status"]}
p_Qa_internal_log2008 = {qa_diag["p_Qa_internal_log2008"]}
p_Qc_closed = {qa_diag["p_Qc_closed"]}
p_SU2_closed = {qa_diag["p_SU2_closed"]}
p_Y_if_reused = {qa_diag["p_Y_if_reused"]}
lambda_12_if_reused = {qa_diag["lambda_12_if_reused"]}
target_witness_not_used = {qa_diag["target_witness_not_used"]}
absolute_residual_to_witness = {qa_diag["absolute_residual_to_witness"]}
reason = {qa_diag["reason"]}
```

This diagnostic is useful because it shows the closed Qa branch is numerically
near the needed hypercharge row, but it is not legal proof data: it is an
internal reduced Qa/SU3 determinant, not the same-scheme U1/Y threshold
operator spectrum.

## Acceptance Contract

The next object must provide:

{required}

Forbidden inputs:

{forbidden}

## Decision

```text
operator_spectrum_source_packet_built = true
selected_U1_hypercharge_operator_spectrum_found = false
selected_lambda_12_found = false
primary_next_object = {candidate["decision"]["primary_next_object"]}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, certificate, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"Wrote {OUTPUT_DATA}")
    print(f"Wrote {OUTPUT_CERT}")
    print(f"Wrote {OUTPUT_NOTE}")
    print(certificate["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
