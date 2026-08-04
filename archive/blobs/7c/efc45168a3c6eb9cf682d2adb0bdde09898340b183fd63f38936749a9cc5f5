"""Build E_Qa or threshold finite-part theorem for selected projective rho_E packet."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "selected_packet_emission": DATA / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity.candidate.json",
    "selected_finite_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "smooth_determinant_table": DATA / "smooth_determinant_spectral_table_or_source_operator.candidate.json",
    "gr_internal_separation": DATA / "gr_surface_internal_quantum_separation_theorem.candidate.json",
    "chi_qa": DATA / "selected_response_functional_chi_qa.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_EQa_or_ThresholdFinitePart_v1.md"
OUTPUT_VALUE = DATA / "selected_heterotic_projectiverhoe_internal_threshold_finitepart.json"

STATUS = "HETEROTIC_PROJECTIVERHOE_INTERNAL_THRESHOLD_FINITEPART_CLOSED_EQA_SMOOTH_PHYSICAL_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_PhysicalThresholdNormalization_or_SmoothOperatorIdentity_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def det3(matrix: list[list[int]]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def main() -> dict[str, Any]:
    emission = load(INPUTS["selected_packet_emission"])
    packet = load(INPUTS["selected_finite_packet"])
    determinant_table = load(INPUTS["smooth_determinant_table"])
    gr_sep = load(INPUTS["gr_internal_separation"])
    chi_qa = load(INPUTS["chi_qa"])

    h_sel = packet["H_sel"]
    determinant = det3(h_sel)
    logdet = math.log(determinant)
    chi_value = float(chi_qa["derivation"]["result"]["chi_Qa_numeric"])
    internal_threshold = chi_value * logdet

    finitepart_checks = {
        "selected_finite_packet_emitted": emission["decision"]["selected_finite_internal_packet_emitted"],
        "packet_scope_is_internal_finite": packet["scope"] == "selected_finite_internal_Qa_SU3_projective_response_only",
        "H_sel_positive_determinant": determinant == 2008,
        "determinant_table_agrees": determinant_table["finite_hessian_determinant"]["determinant_exact"] == 2008,
        "finite_logdet_agrees": determinant_table["finite_hessian_determinant"]["zeta_regularized_finite_rank_logdet"] == "log(2008)",
        "chi_Qa_is_one": chi_qa["decision"]["selected_chi_Qa"] == "1",
        "smooth_complement_routed_to_GR": gr_sep["theorem"]["conclusions"]["smooth_complement_policy"] == "routed_to_GR_protospinor_surface_sector_not_a_Qa_SU3_internal_determinant",
        "no_target_fitting": not emission["target_fitting_used"] and not packet["target_fitting_used"] and not chi_qa["target_fitting_used"],
    }

    selected_internal_threshold_finitepart_closed = all(finitepart_checks.values())

    value_packet = {
        "schema": "SelectedHeteroticProjectiveRhoEInternalThresholdFinitePart.v1",
        "scope": "selected_internal_finite_Qa_SU3_projective_threshold_units",
        "selected": selected_internal_threshold_finitepart_closed,
        "regularization": "finite-rank zeta/logdet on selected H_sel after GR/internal quotient",
        "H_sel": h_sel,
        "spectrum": ["8", "18 - sqrt(73)", "18 + sqrt(73)"],
        "determinant": determinant,
        "logdet_exact": "log(2008)",
        "logdet_numeric": logdet,
        "chi_Qa": "1",
        "Delta_selected_internal_exact": "log(2008)",
        "Delta_selected_internal_numeric": internal_threshold,
        "zero_mode_policy": "finite quotient H_sel has no zero eigenvalues; smooth/GR complement is routed away before internal threshold",
        "target_fitting_used": False,
    }

    decision = {
        "selected_internal_threshold_finitepart_closed": selected_internal_threshold_finitepart_closed,
        "E_Qa_computed": False,
        "smooth_operator_identity_proved": False,
        "smooth_transition_matrices_emitted": False,
        "physical_threshold_normalization_closed": False,
        "measured_coupling_match_claimed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEEQaOrThresholdFinitePart",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "selected_packet_emission": emission["status"],
            "gr_internal_separation": gr_sep["status"],
            "chi_qa": chi_qa["status"],
        },
        "finitepart_checks": finitepart_checks,
        "internal_threshold_finitepart_path": rel(OUTPUT_VALUE),
        "decision": decision,
        "remaining_after_finitepart": {
            "E_Qa_or_smooth_Weitzenbock_block": True,
            "smooth_heterotic_operator_identity": True,
            "physical_threshold_normalization": True,
            "measured_electroweak_or_running_coupling_match": True,
        },
        "guardrails": {
            "does_not_claim_E_Qa": True,
            "does_not_claim_smooth_operator_identity": True,
            "does_not_claim_physical_threshold_normalization": True,
            "does_not_claim_measured_coupling_match": True,
            "does_not_double_count_GR_smooth_complement": True,
            "does_not_use_observed_data_or_target_fitting": True,
        },
        "theorem": {
            "name": "SelectedInternalProjectiveRhoEThresholdFinitePart",
            "proved": selected_internal_threshold_finitepart_closed,
            "statement": (
                "For the selected finite internal Qa/SU3 projective rho_E packet, the "
                "threshold finite part in internal determinant units is log(2008). "
                "It is the finite-rank zeta/logdet of H_sel, multiplied by the selected "
                "finite response normalization chi_Qa=1, after the GR/protospinor smooth "
                "complement is routed away. This closes the internal finite-part route, "
                "but not E_Qa, smooth heterotic operator identity, or physical coupling "
                "normalization."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_VALUE.write_text(json.dumps(value_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "internal_threshold_finitepart_path": rel(OUTPUT_VALUE),
        "selected_internal_threshold_finitepart_closed": selected_internal_threshold_finitepart_closed,
        "Delta_selected_internal_exact": "log(2008)",
        "Delta_selected_internal_numeric": internal_threshold,
        "E_Qa_computed": False,
        "smooth_operator_identity_proved": False,
        "physical_threshold_normalization_closed": False,
        "measured_coupling_match_claimed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE E_Qa or ThresholdFinitePart v1

## Result

```text
status = {STATUS}
selected_internal_threshold_finitepart_closed = {str(selected_internal_threshold_finitepart_closed).lower()}
Delta_selected_internal = log(2008)
E_Qa_computed = false
physical_threshold_normalization_closed = false
next_required_artifact = {NEXT}
```

## Closed Here

The selected finite projective `rho_E` packet now has its internal threshold
finite part:

```text
Delta_selected_internal = chi_Qa * logdet(H_sel) = 1 * log(2008)
```

The value packet is:

```text
{rel(OUTPUT_VALUE)}
```

## Still Open

This is an internal determinant-unit finite part. It is not yet the physical
heterotic threshold normalization and it does not compute a smooth `E_Qa`
Weitzenbock block. The next gate must connect this selected internal finite
part to physical threshold normalization, or replace it with a same-source
smooth operator identity.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_VALUE)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
