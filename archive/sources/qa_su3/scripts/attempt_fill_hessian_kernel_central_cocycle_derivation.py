"""Attempt to fill the Hessian/kernel central-cocycle derivation packet."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

INTERFACE = DATA / "hessian_kernel_central_cocycle_derivation_interface.candidate.json"
TEMPLATE = CERTS / "hessian_kernel_central_cocycle_derivation.template.json"
VALIDATOR = ROOT / "scripts" / "validate_hessian_kernel_central_cocycle_derivation.py"

Q79_S3 = Q79 / "candidate_data" / "visible_twisted_s3_class_restriction_closure.candidate.json"
Q79_ORIENTATION_DEDOTD = Q79 / "candidate_data" / "selected_qa_su3_orientation_dedotd_source_attempt.candidate.json"
Q79_VALPHA_S3 = Q79 / "candidate_data" / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt.candidate.json"
Q79_Z64 = Q79 / "certificates" / "z64_exact_branch_certificate.json"
Q79_THETA_KERNEL = Q79 / "certificates" / "theta_flavor_kernel_skeleton_certificate.json"

OUTPUT_DATA = DATA / "hessian_kernel_central_cocycle_fill_attempt.candidate.json"
OUTPUT_PACKET = DATA / "hessian_kernel_central_cocycle_fill_attempt.current_packet.json"
OUTPUT_CERT = CERTS / "hessian_kernel_central_cocycle_fill_attempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Hessian_Kernel_Central_Cocycle_Fill_Attempt_v1.md"

SOURCES = {
    "strominger": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "qft_diagrammatics": OBSIDIAN
    / "7 Quantum Field Theory"
    / "Modal_Diagrammatics__The_Origin_of_Feynman_Rules_from_Coherent_Modal_Geometry.md",
    "protospinor": OBSIDIAN
    / "10 ProtoSpinor"
    / "Proto_Spinor_Closure_and_Worldsheet_Encoding_in_Modal_Triplet_Theory_v3.md",
    "central_circle": OBSIDIAN
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md",
}


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {
        "path": str(path),
        "present": True,
        "terms": {key: needle.lower() in text for key, needle in terms.items()},
    }


def run_validator(path: Path) -> dict[str, object]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {"exit_code": proc.returncode, "output": proc.stdout.strip()}


def module_twists(charge_table: dict[str, list[int]]) -> dict[str, int]:
    return {label: int(charge[2]) for label, charge in charge_table.items()}


def all_twists_cancel(twists: dict[str, int]) -> bool:
    return all(twists[f"F{idx}"] + twists[f"G{idx}"] == 0 for idx in range(1, 6)) and twists["P"] == 0


def build() -> tuple[dict[str, object], dict[str, object], str, dict[str, object]]:
    interface = load(INTERFACE)
    template = load(TEMPLATE)
    s3 = load(Q79_S3)
    orientation_dedotd = load(Q79_ORIENTATION_DEDOTD)
    valpha_s3 = load(Q79_VALPHA_S3)
    z64 = load(Q79_Z64)
    theta_kernel = load(Q79_THETA_KERNEL)

    packet = copy.deepcopy(template)
    charge_table = packet["twist_projection"]["charge_table"]
    twists = module_twists(charge_table)
    packet["status"] = "PARTIAL_QA_SU3_HESSIAN_KERNEL_CENTRAL_COCYCLE_DERIVATION_BLOCKED"
    packet["source_identity"] = {
        "branch": "Qa/SU3 Strominger/Iwasawa gerbe-twist branch",
        "selection_rule": "PARTIAL: source family selected, but no selected Qa/SU3 H_sel/G_ret derivation is printed",
        "source_certificate": "current corpus plus Qa/SU3 proof repo audits; no closure certificate",
    }
    packet["hessian_block"] = {
        "H_sel_basis": None,
        "H_sel_matrix": None,
        "gauge_nullspace_policy": "CONTEXT_ONLY: Strominger/QFT/ProtoSpinor papers define Hessian/gauge-complement discipline",
        "positive_on_complement": "CONTEXT_ONLY: positive Hessian theorem exists for Strominger fixed point; no Qa/SU3 c-twist block matrix",
        "sector_restriction": None,
    }
    packet["retarded_kernel"] = {
        "G_ret_or_Green_matrix": None,
        "retarded_orientation_rule": "GUARDRAIL_ONLY: q79 Z64 has S^-1 retarded lag; not Qa/SU3 c-twist source",
        "complement_projector": None,
        "kernel_identity_checked": False,
    }
    packet["twist_projection"]["Pi_tw_matrix_or_rule"] = "PARTIAL_ALGEBRAIC: take the third monad charge coordinate as c-gerbe twist label; not derived from H_sel/G_ret"
    packet["tau_extraction"] = {
        "extraction_formula": "PARTIAL_ALGEBRAIC: tau_label(L)=c(L), the third charge coordinate",
        "module_twist_values": twists,
        "central_2_cocycle_table": None,
        "period_denominator_or_smooth_unit": None,
        "cocycle_law_checked": all_twists_cancel(twists),
        "period_selected_by_H_sel_G_ret": False,
    }
    packet["admissibility"] = {
        "Green_Schwarz_Bianchi_checked": "PARTIAL_CONTEXT_ONLY: Strominger/Iwasawa Bianchi support exists; not mapped to selected tau",
        "Freed_Witten_checked": False,
        "projector_retention_checked": False,
        "zero_mode_policy": None,
        "stability_or_HYM_policy": "PARTIAL_CONTEXT_ONLY: HYM/Strominger existence context; no selected response source",
    }
    packet["response_payload"] = {
        "projective_rhoE": None,
        "D_E": None,
        "dotD": None,
        "Riesz_projector": None,
        "Green_operator": None,
        "heat_zeta_or_torsion_finite_part": None,
        "trace_normalization": None,
    }
    packet["guardrails"] = {
        "no_target_fitting": True,
        "no_q79_direct_import": True,
        "source_selected": False,
    }
    packet_validator = run_validator(OUTPUT_PACKET) if OUTPUT_PACKET.exists() else {"exit_code": None, "output": "not run before write"}

    source_scans = {
        "strominger": scan(
            SOURCES["strominger"],
            {
                "fixed_differential_class": "fixed differential cohomology class",
                "B_field": "Deligne 2-gerbe",
                "Bianchi": "Bianchi",
                "positive_Hessian": "Positive Hessian",
            },
        ),
        "qft_diagrammatics": scan(
            SOURCES["qft_diagrammatics"],
            {
                "coherent_Hessian": "coherent Hessian",
                "modal_propagator": "modal propagator",
                "admissible_inverse": "admissible inverse",
            },
        ),
        "protospinor": scan(
            SOURCES["protospinor"],
            {
                "anchored_Hessian": "anchored Hessian",
                "circle_block": "circle block",
                "overlap_slab": "overlap slab",
            },
        ),
        "central_circle": scan(
            SOURCES["central_circle"],
            {
                "central_circle": "Central Circle",
                "shared_coherence": "shared coherence",
                "z3": "Z_3",
            },
        ),
    }

    q79_evidence = {
        "visible_s3_status": s3["status"],
        "visible_s3_source_level_closed": s3["calculation_results"],
        "visible_s3_still_open": s3["still_open"],
        "orientation_dedotd_status": orientation_dedotd["status"],
        "orientation_dedotd_results": orientation_dedotd["calculation_results"],
        "orientation_dedotd_open_items": orientation_dedotd["first_open_items"],
        "valpha_s3_status": valpha_s3["status"],
        "valpha_s3_open_item_count": valpha_s3["open_item_count"],
        "z64_status": z64["status"],
        "z64_hessian_block": z64["hessian_block"],
        "z64_retarded_kernel": z64["retarded_kernel"],
        "theta_kernel_status": theta_kernel["status"],
        "theta_open_kernel_data": theta_kernel["open_kernel_data"],
    }
    fill_result = {
        "source_family_context_filled": True,
        "generic_hessian_discipline_found": True,
        "generic_retarded_or_green_discipline_found": True,
        "algebraic_Pi_tw_rule_filled": True,
        "module_tau_labels_filled_from_c_charge": True,
        "tau_twist_cancellation_passes": all_twists_cancel(twists),
        "q79_s3_guardrail_source_packet_closed": True,
        "q79_z64_hessian_kernel_guardrail_closed": True,
        "route_c_response_shape_available_unselected": True,
        "selected_Qa_SU3_H_sel_matrix_found": False,
        "selected_Qa_SU3_G_ret_found": False,
        "tau_extracted_from_H_sel_G_ret": False,
        "period_or_smooth_unit_selected_by_H_sel_G_ret": False,
        "admissibility_mapped_to_selected_tau": False,
        "same_source_response_payload_filled": False,
        "validator_passed": False,
        "qa_su3_packet_closed": False,
        "target_fitting_used": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3HessianKernelCentralCocycleFillAttempt",
        "status": "QA_SU3_HESSIAN_KERNEL_CENTRAL_COCYCLE_FILL_ATTEMPT_PARTIAL_TAU_BLOCKED_SELECTED_HESSIAN_KERNEL",
        "input_status": interface["status"],
        "source_scans": source_scans,
        "q79_evidence": q79_evidence,
        "attempt_packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "attempt_packet_validator_result": packet_validator,
        "fill_result": fill_result,
        "partial_packet": packet,
        "what_promotes": [
            "algebraic c-charge projection Pi_tw is available",
            "module twist labels satisfy tau(F_i)+tau(G_i)=0 and tau(P)=0",
            "same-branch corpus supports the abstract Hessian/Green discipline",
            "q79/S3 and Z64 provide strong guardrail examples of central cocycles and retarded kernels",
        ],
        "what_blocks": [
            "no selected Qa/SU3 H_sel matrix or basis",
            "no selected Qa/SU3 G_ret or Green kernel",
            "tau is not extracted from H_sel/G_ret",
            "no selected period denominator or smooth unit",
            "Freed-Witten/projector/zero-mode checks are not mapped to selected tau",
            "Route C D_E/Green/dotD response packets are unselected smoke data",
            "q79/S3 and Z64 data remain off-branch guardrails",
        ],
        "decision": {
            "result": "Partial tau typing fills; Hessian/kernel derivation does not close.",
            "why": "The current corpus supplies abstract Hessian discipline and off-branch guardrails, but not the actual selected Qa/SU3 H_sel/G_ret data needed to select tau and the response payload.",
            "next_move": "Build a minimal selected-H_sel/G_ret source request, or compute an explicit finite Galerkin/Hessian candidate and require a source-selection proof before promotion.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Minimal_Hsel_Gret_Source_Request_or_Finite_Galerkin_Candidate_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "attempt_packet_path": candidate["attempt_packet_path"],
        "what_closes": {
            "algebraic_Pi_tw_rule_filled": fill_result["algebraic_Pi_tw_rule_filled"],
            "module_tau_labels_filled_from_c_charge": fill_result["module_tau_labels_filled_from_c_charge"],
            "tau_twist_cancellation_passes": fill_result["tau_twist_cancellation_passes"],
            "generic_hessian_and_green_discipline_found": fill_result["generic_hessian_discipline_found"]
            and fill_result["generic_retarded_or_green_discipline_found"],
            "q79_guardrails_identified": fill_result["q79_s3_guardrail_source_packet_closed"]
            and fill_result["q79_z64_hessian_kernel_guardrail_closed"],
        },
        "what_remains_open": {
            "selected_Qa_SU3_H_sel_matrix_found": fill_result["selected_Qa_SU3_H_sel_matrix_found"],
            "selected_Qa_SU3_G_ret_found": fill_result["selected_Qa_SU3_G_ret_found"],
            "tau_extracted_from_H_sel_G_ret": fill_result["tau_extracted_from_H_sel_G_ret"],
            "period_or_smooth_unit_selected_by_H_sel_G_ret": fill_result["period_or_smooth_unit_selected_by_H_sel_G_ret"],
            "admissibility_mapped_to_selected_tau": fill_result["admissibility_mapped_to_selected_tau"],
            "same_source_response_payload_filled": fill_result["same_source_response_payload_filled"],
            "validator_passed": fill_result["validator_passed"],
            "qa_su3_packet_closed": fill_result["qa_su3_packet_closed"],
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 Hessian Kernel Central Cocycle Fill Attempt v1

## What Filled

The attempt fills the algebraic part of the derivation interface:

```text
Pi_tw rule: third monad charge coordinate c
tau(F1..F5):  1, -1, 0, -1, 1
tau(G1..G5): -1,  1, 0,  1,-1
tau(P): 0
tau(F_i)+tau(G_i)=0: yes
target fitting used: no
```

This is a real consistency check: the typed gerbe/twist bookkeeping is coherent.

## What Did Not Fill

The attempted packet still does not pass the Hessian/kernel derivation validator.
The current corpus does not supply:

```text
selected Qa/SU3 H_sel basis and matrix,
selected Qa/SU3 retarded overlap or Green kernel G_ret,
extraction of tau from H_sel and G_ret,
period denominator or smooth unit selected by H_sel/G_ret,
Freed-Witten/projector/zero-mode checks mapped to that tau,
same-source projective rho_E or D_E/dotD/Riesz/Green response.
```

## Guardrail Evidence

q79/S3 closes a finite Deligne/central-cocycle source pattern, and Z64 closes an
exact central-circle Hessian/retarded-kernel pattern. These are strong
templates. They are not Qa/SU3 proof sources here.

Route C finite `D_E`, reduced Green, and `dotD` packets reach the validator
layer, but they are still marked unselected at the source flags.

## Decision

The next move is no longer broad search. It is the minimal selected `H_sel/G_ret`
source request, or a finite Galerkin candidate whose source-selection proof is
checked before promotion.

Next artifact:

```text
{candidate["next_required_artifact"]}
```

closure claimed: no
target fitting used: no
"""
    return candidate, certificate, note, packet


def main() -> None:
    candidate, certificate, note, packet = build()
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        validator_result = run_validator(OUTPUT_PACKET)
        candidate["attempt_packet_validator_result"] = validator_result
        candidate["fill_result"]["validator_passed"] = validator_result["exit_code"] == 0
        certificate["attempt_packet_validator_result"] = validator_result
        OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
        print(json.dumps(certificate, indent=2, sort_keys=True))
        return
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
