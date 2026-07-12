"""Build the heterotic/Strominger electroweak threshold-kernel fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

INPUTS = {
    "kernel_route": DATA / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme.candidate.json",
    "kernel_template": DATA / "selected_heterotic_strominger_electroweak_threshold_kernel.template.json",
    "stack_status": NONSM / "certificates" / "selected_stack_determinant_source_status_certificate.json",
    "qa_su3_strominger_search": NONSM / "certificates" / "selected_qa_su3_strominger_hym_source_packet_search_certificate.json",
    "z7_fuyau_mukai": Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json",
    "heterotic_selection_paper": OBSIDIAN / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
    "heterotic_flux_paper": OBSIDIAN / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "strominger_system_paper": OBSIDIAN / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
}

OUTPUT_DATA = DATA / "selected_heterotic_strominger_electroweak_threshold_kernel.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_strominger_electroweak_threshold_kernel_certificate.json"
OUTPUT_PAYLOAD = DATA / "selected_heterotic_strominger_electroweak_threshold_kernel_minimal_payload.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_Strominger_Electroweak_Threshold_Kernel_v1.md"

STATUS = "HETEROTIC_STROMINGER_EW_KERNEL_FILL_ATTEMPT_SOURCE_VALUES_OPEN"
NEXT = "Selected_Heterotic_Strominger_AnalyticTorsion_or_ThresholdOperator_Payload_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def terms(path: Path, needles: list[str]) -> dict[str, bool]:
    text = read_text(path).lower()
    return {needle: needle.lower() in text for needle in needles}


def build_minimal_payload(template: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "SelectedHeteroticStromingerAnalyticTorsionOrThresholdOperatorPayload.v1",
        "status": "OPEN_SELECTED_THRESHOLD_OPERATOR_OR_TORSION_REQUIRED",
        "inherits_known_internal_weak_split": template["threshold_payload"]["known_internal_weak_split"],
        "must_emit": {
            "source_identity": {
                "selected_by_mtt": None,
                "fixed_topological_sector": None,
                "same_branch_as_electroweak_Qa_Qc_SU2_stacks": None,
                "computed_before_electroweak_comparison": None,
            },
            "geometric_background": {
                "complex_threefold_or_nilmanifold": None,
                "SU3_structure": None,
                "balanced_or_conformally_balanced_metric": None,
                "dilaton_or_tree_level_S": None,
                "B_field_gerbe_class": None,
                "Bianchi_identity_verified": None,
            },
            "bundle_and_trace_data": {
                "Qa_stack_bundle_or_sheaf": None,
                "Qc_stack_bundle_or_circle_source": None,
                "SU2_stack_bundle_or_sheaf": None,
                "hypercharge_trace_weights": "Y=(1/6)Qa-(1/2)Qc",
                "trace_normalization": None,
                "index_Dynkin_weights": None,
            },
            "threshold_operator_or_torsion": {
                "operator_type": "analytic torsion, finite heat/zeta determinant, or one-loop threshold operator",
                "positive_spectrum_or_torsion_finite_part": None,
                "p_a_physical_threshold_scheme": None,
                "p_c_physical_threshold_scheme": None,
                "p_SU2_physical_threshold_scheme": None,
                "regularization_scheme": None,
            },
            "matching_and_running": {
                "mu_match": None,
                "RG_scheme": None,
                "beta_coefficients": None,
                "threshold_convention": None,
            },
        },
        "forbidden": [
            "reuse the closed internal p_a as the physical threshold row without a physical threshold scheme",
            "use q79 Fu-Yau/Mukai charge-sector data as electroweak threshold determinants",
            "use Theta 5 TeV as derived mu_match",
            "choose torsion/operator entries from measured electroweak residuals",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    route = load(INPUTS["kernel_route"])
    template = load(INPUTS["kernel_template"])
    stack = load(INPUTS["stack_status"])
    qa_search = load(INPUTS["qa_su3_strominger_search"])
    fuyau = load(INPUTS["z7_fuyau_mukai"])
    minimal_payload = build_minimal_payload(template)

    source_scan = {
        "heterotic_selection_paper": {
            "path": str(INPUTS["heterotic_selection_paper"]),
            "present": INPUTS["heterotic_selection_paper"].exists(),
            "terms": terms(INPUTS["heterotic_selection_paper"], ["Strominger", "Hermitian Yang", "Bianchi", "gauge kinetic", "one-loop thresholds"]),
        },
        "heterotic_flux_paper": {
            "path": str(INPUTS["heterotic_flux_paper"]),
            "present": INPUTS["heterotic_flux_paper"].exists(),
            "terms": terms(INPUTS["heterotic_flux_paper"], ["Iwasawa", "Lens", "Nil", "HYM", "Bianchi", "left-invariant", "threshold"]),
        },
        "strominger_system_paper": {
            "path": str(INPUTS["strominger_system_paper"]),
            "present": INPUTS["strominger_system_paper"].exists(),
            "terms": terms(INPUTS["strominger_system_paper"], ["fixed topological sector", "positive Hessian", "unique local minimizer", "HYM", "Bianchi"]),
        },
    }

    fill_tests = {
        "source_identity": {
            "status": "PARTIAL_FRAMEWORK_ONLY",
            "selected_by_mtt": False,
            "filled": [
                "general Strominger fixed-sector selection framework",
                "q79 Fu-Yau charge-sector support",
            ],
            "missing": [
                "same-branch electroweak Qa/Qc/SU2 threshold-kernel source certificate",
                "source-selected threshold operator or analytic torsion payload",
            ],
        },
        "gauge_kinetic_payload": {
            "status": "TREE_LEVEL_SLOT_FILLED_VALUES_OPEN",
            "tree_level_universal_function": "f=S; g^{-2}=Re S up to threshold corrections",
            "physical_normalization_closed": False,
            "same_source_as_GR_anchor_closed": False,
            "reason_open": "The heterotic source explicitly leaves alpha-prime and one-loop thresholds uncomputed; M-theory dimensional value is also open.",
        },
        "threshold_payload": {
            "status": "INTERNAL_WEAK_SPLIT_CARRIED_PHYSICAL_THRESHOLDS_OPEN",
            "known_internal_weak_split": template["threshold_payload"]["known_internal_weak_split"],
            "stack_determinant_source_certified": stack["verdict"]["stack_determinant_values_source_certified"],
            "required_stack_determinants": template["threshold_payload"]["required_stack_determinants"],
            "one_loop_or_analytic_torsion_operator_found": False,
            "positive_spectrum_or_torsion_finite_part_found": False,
        },
        "matching_payload": {
            "status": "OPEN",
            "mu_match_closed": False,
            "RG_scheme_closed": False,
            "threshold_convention_closed": False,
        },
        "q79_fuyau_import": {
            "status": "CHARGE_SECTOR_SUPPORT_ONLY",
            "charge_sector_closed": fuyau["status"] == "CLOSED_CHARGE_SECTOR",
            "green_schwarz_bianchi_identity_verified": fuyau["geometry"]["green_schwarz_bianchi_identity_verified"],
            "usable_as_electroweak_threshold_kernel": False,
            "reason": "It certifies a Fu-Yau/Mukai charge sector and CP/Z7 support, not Qa/Qc/SU2 electroweak analytic torsion or threshold determinants.",
        },
    }

    decision = {
        "selected_heterotic_strominger_kernel_closed": False,
        "source_identity_selected_for_EW_kernel": False,
        "tree_level_gauge_kinetic_slot_filled": True,
        "physical_normalization_closed": False,
        "stack_threshold_determinants_closed": False,
        "analytic_torsion_or_threshold_operator_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "measured_electroweak_closure": False,
        "internal_lambda_12_carried": True,
        "internal_lambda_12_value": template["threshold_payload"]["known_internal_weak_split"]["lambda_12"],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticStromingerElectroweakThresholdKernel",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "route": route["status"],
            "stack_status": stack["status"],
            "qa_su3_strominger_search": qa_search["status"],
            "z7_fuyau_mukai": fuyau["status"],
        },
        "source_scan": source_scan,
        "fill_tests": fill_tests,
        "minimal_payload_path": rel(OUTPUT_PAYLOAD),
        "decision": decision,
        "theorem": {
            "name": "HeteroticStromingerEWKernelCurrentSourceFillAttempt",
            "proved": True,
            "statement": (
                "The current corpus fills the heterotic/Strominger framework, the "
                "tree-level universal gauge kinetic slot f=S, Bianchi/HYM support, "
                "and the already closed internal weak-split threshold. It does not "
                "emit the selected electroweak threshold kernel: no same-branch "
                "Qa/Qc/SU2 analytic torsion, finite zeta determinant, one-loop "
                "threshold operator, physical normalization, mu_match, or RG scheme "
                "is source-certified. Therefore the strict no-knob primary route "
                "remains live but value-open."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "promotes_q79_charge_sector_to_thresholds": False,
            "promotes_tree_level_fS_to_one_loop_thresholds": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedHeteroticStromingerElectroweakThresholdKernel",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "minimal_payload_path": rel(OUTPUT_PAYLOAD),
        "note_path": rel(OUTPUT_NOTE),
        "tree_level_gauge_kinetic_slot_filled": True,
        "selected_heterotic_strominger_kernel_closed": False,
        "analytic_torsion_or_threshold_operator_closed": False,
        "physical_normalization_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "internal_lambda_12_value": decision["internal_lambda_12_value"],
        "measured_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, minimal_payload, render_note(candidate, cert, minimal_payload)


def render_note(candidate: dict[str, Any], cert: dict[str, Any], minimal_payload: dict[str, Any]) -> str:
    return f"""# Selected Heterotic Strominger Electroweak Threshold Kernel v1

## Result

```text
status = {candidate["status"]}
tree_level_gauge_kinetic_slot_filled = true
selected_heterotic_strominger_kernel_closed = false
analytic_torsion_or_threshold_operator_closed = false
physical_normalization_closed = false
matching_scale_closed = false
RG_scheme_closed = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Fill Tests

```json
{json.dumps(candidate["fill_tests"], indent=2, sort_keys=True)}
```

## Source Scan

```json
{json.dumps(candidate["source_scan"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Minimal Payload

```json
{json.dumps(minimal_payload, indent=2, sort_keys=True)}
```

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, payload, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_PAYLOAD, payload)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_PAYLOAD, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
