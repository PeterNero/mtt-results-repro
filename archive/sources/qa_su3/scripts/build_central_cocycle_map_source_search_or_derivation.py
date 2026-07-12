"""Search for, or reduce to derivation of, the Qa/SU3 central-cocycle map."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

REQUEST = DATA / "central_cocycle_map_source_augmentation_request.candidate.json"
PROMOTION_FILL = DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json"

OUTPUT_DATA = DATA / "central_cocycle_map_source_search_or_derivation.candidate.json"
OUTPUT_CERT = CERTS / "central_cocycle_map_source_search_or_derivation_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Central_Cocycle_Map_Source_Search_or_Derivation_v1.md"

SOURCES = {
    "qa_su3_strominger": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "qa_su3_iwasawa_flux": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "mtt_qft_hessian": OBSIDIAN
    / "7 Quantum Field Theory"
    / "Modal_Diagrammatics__The_Origin_of_Feynman_Rules_from_Coherent_Modal_Geometry.md",
    "protospinor_hessian": OBSIDIAN
    / "10 ProtoSpinor"
    / "Proto_Spinor_Closure_and_Worldsheet_Encoding_in_Modal_Triplet_Theory_v3.md",
    "q79_visible_s3_closure": Q79 / "proof_corpus" / "Visible_Twisted_S3_Class_Restriction_Closure_v1.md",
    "q79_visible_s3_source_attempt": Q79 / "proof_corpus" / "Visible_Twisted_S3_Source_Packet_Attempt_v1.md",
    "q79_visible_rhoe_ansatz": Q79 / "proof_corpus" / "Visible_RhoE_Source_Ansatz_Search_v1.md",
    "q79_z64_hessian_kernel": Q79 / "proof_corpus" / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md",
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


def build() -> tuple[dict[str, object], dict[str, object], str]:
    request = load(REQUEST)
    promotion = load(PROMOTION_FILL)
    scans = {
        "qa_su3_strominger": scan(
            SOURCES["qa_su3_strominger"],
            {
                "fixed_differential_class": "fixed differential cohomology class",
                "Deligne_B_field": "Deligne 2-gerbe",
                "Bianchi": "Bianchi",
                "positive_Hessian": "Positive Hessian",
                "central_cocycle": "central cocycle",
                "selected_D_E": "D_E",
                "retarded_overlap": "retarded overlap",
            },
        ),
        "qa_su3_iwasawa_flux": scan(
            SOURCES["qa_su3_iwasawa_flux"],
            {
                "Iwasawa": "Iwasawa",
                "integral_periods": "integral periods",
                "Bianchi_componentwise": "Bianchi identity is solved componentwise",
                "central_cocycle": "central cocycle",
                "selected_D_E": "D_E",
            },
        ),
        "mtt_qft_hessian": scan(
            SOURCES["mtt_qft_hessian"],
            {
                "coherent_Hessian": "coherent Hessian",
                "modal_propagator": "modal propagator",
                "retarded": "retarded",
                "sector_response": "restricted to the coherent",
                "central_cocycle": "central cocycle",
            },
        ),
        "protospinor_hessian": scan(
            SOURCES["protospinor_hessian"],
            {
                "anchored_Hessian": "anchored Hessian",
                "circle_block": "circle block",
                "overlap_slab": "overlap slab",
                "central_cocycle": "central cocycle",
                "retarded": "retarded",
            },
        ),
        "q79_visible_s3_closure": scan(
            SOURCES["q79_visible_s3_closure"],
            {
                "selected_flat_Deligne_class": "selected q79/F,m=1 flat Deligne class",
                "qutrit_central_cocycle": "qutrit central cocycle",
                "Freed_Witten": "Freed-Witten",
                "projector_retention": "projector retention",
                "selected_D_E_open": "D_E/dotD",
            },
        ),
        "q79_visible_s3_source_attempt": scan(
            SOURCES["q79_visible_s3_source_attempt"],
            {
                "period_denominator_3": "finite period denominator = 3",
                "maps_to_zeta3": "zeta_3",
                "source_not_selected": "source",
                "selected_D_E_open": "selected D_E/dotD",
            },
        ),
        "q79_visible_rhoe_ansatz": scan(
            SOURCES["q79_visible_rhoe_ansatz"],
            {
                "fixed_gerbe_or_DE": "selected D_E/dotD response data or a fixed selected gerbe/B-field representative",
                "ordinary_rhoe_retired": "not another constant ordinary rho_E table",
                "projective_rhoe": "rho_E",
            },
        ),
        "q79_z64_hessian_kernel": scan(
            SOURCES["q79_z64_hessian_kernel"],
            {
                "selected_hessian": "selected Hessian",
                "retarded_kernel": "retarded kernel",
                "central_circle": "central-circle",
                "not_qasu3": "larger non-exact MTT Hessian",
            },
        ),
    }

    route_results = [
        {
            "route": "same_branch_corpus_source_packet",
            "promotes": False,
            "evidence": [
                "Strominger/Iwasawa sources contain fixed differential-class, B-field/gerbe, Bianchi, and positive-Hessian context.",
                "They do not print the selected Qa/SU3 representative, period unit, central-cocycle action, or same-source response matrices.",
            ],
            "missing": [
                "selected representative",
                "representative -> c-twist cocycle/action",
                "period denominator or smooth unit",
                "D_E/dotD or projective rho_E response",
            ],
        },
        {
            "route": "q79_visible_s3_transfer",
            "promotes": False,
            "evidence": [
                "q79 visible S3 has the strongest finite Deligne/central-cocycle pattern.",
                "It supplies finite denominator and qutrit central-cocycle language, but is off-branch for Qa/SU3 and keeps D_E/dotD open.",
            ],
            "missing": [
                "same-branch Qa/SU3 map",
                "same-source operator response",
            ],
        },
        {
            "route": "hessian_kernel_derivation_lane",
            "promotes": False,
            "evidence": [
                "MTT/QFT/ProtoSpinor/Z64 artifacts justify using selected Hessian blocks and retarded kernels as a derivation lane.",
                "No current artifact gives the actual Qa/SU3 selected Hessian block, retarded overlap kernel, or projection map.",
            ],
            "missing": [
                "selected Qa/SU3 Hessian block",
                "retarded overlap or Green kernel",
                "projection from kernel phases to Deligne/central cocycle",
                "finite/projective response payload",
            ],
        },
    ]
    derivation_interface = {
        "objects_to_supply": {
            "H_sel": "selected Hessian restricted to the Qa/SU3 c-twist/source sector",
            "G_ret": "retarded overlap/Green kernel or inverse on the admissible complement",
            "Pi_tw": "projector from Hessian/kernel sector to the twisted module labels",
            "tau": "integral or finite central 2-cocycle/action extracted from H_sel and G_ret",
            "response": "projective rho_E tables or D_E/dotD/Riesz/Green/heat/zeta/torsion finite part",
        },
        "acceptance_equations": [
            "delta tau = 0, or projective rho_E(gamma) rho_E(delta) = zeta^{tau(gamma,delta)} rho_E(gamma delta)",
            "tau(F_i) + tau(G_i) = 0 for i=1..5 and tau(P)=0",
            "period(tau) is selected by H_sel/G_ret, not by observed Qa/SU3 residuals",
            "Freed-Witten/Bianchi/projector checks are evaluated on the same tau and same module",
            "D_E/dotD or rho_E response is computed from the same selected packet",
        ],
        "current_status": "INTERFACE_ONLY_VALUES_OPEN",
    }
    source_search_result = {
        "selected_Qa_SU3_source_packet_found": False,
        "q79_guardrail_packet_found": True,
        "same_branch_hessian_language_found": True,
        "actual_selected_H_sel_found": False,
        "actual_retarded_kernel_found": False,
        "central_cocycle_map_verified": False,
        "response_payload_found": False,
        "target_fitting_used": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3CentralCocycleMapSourceSearchOrDerivation",
        "status": "QA_SU3_CENTRAL_COCYCLE_MAP_SOURCE_SEARCH_DONE_DERIVATION_GATE_BUILT_VALUES_OPEN",
        "input_status": {
            "request": request["status"],
            "promotion_fill": promotion["status"],
        },
        "source_scans": scans,
        "route_results": route_results,
        "source_search_result": source_search_result,
        "derivation_interface": derivation_interface,
        "decision": {
            "result": "No same-branch filled central-cocycle map or response packet found.",
            "why": "The same-branch corpus has the correct differential-cohomology and Hessian container, while q79 has the best finite central-cocycle guardrail, but neither supplies the selected Qa/SU3 map plus response payload.",
            "next_move": "Build the Hessian/kernel central-cocycle derivation interface and require actual H_sel, G_ret, Pi_tw, tau, and response data.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Hessian_Kernel_Central_Cocycle_Derivation_Interface_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "same_branch_source_search_executed": True,
            "q79_guardrail_identified": True,
            "hessian_kernel_derivation_lane_formalized": True,
            "forbidden_direct_transfer_rejected": True,
        },
        "what_remains_open": {
            "selected_Qa_SU3_source_packet_found": source_search_result["selected_Qa_SU3_source_packet_found"],
            "actual_selected_H_sel_found": source_search_result["actual_selected_H_sel_found"],
            "actual_retarded_kernel_found": source_search_result["actual_retarded_kernel_found"],
            "central_cocycle_map_verified": source_search_result["central_cocycle_map_verified"],
            "response_payload_found": source_search_result["response_payload_found"],
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 Central Cocycle Map Source Search or Derivation v1

## Search Result

The exact same-branch source packet was not found.

```text
same-branch selected representative: no
verified central-cocycle map: no
selected period denominator or smooth unit: no
same-source projective rho_E or D_E/dotD response: no
target fitting used: no
```

The strongest positive clue is still q79 visible S3: it has an explicit finite
Deligne/central-cocycle pattern and denominator-3 guardrail. It cannot be
imported as Qa/SU3 proof because it is off-branch and still leaves the selected
operator response open.

## Derivation Lane

The corpus does support a rigorous derivation lane through Hessian and retarded
kernel data. A closing derivation must supply:

```text
H_sel   = selected Hessian restricted to the Qa/SU3 c-twist/source sector
G_ret   = retarded overlap/Green kernel on the admissible complement
Pi_tw   = projection from Hessian/kernel sector to twisted module labels
tau     = integral or finite central 2-cocycle/action extracted from H_sel,G_ret
response = projective rho_E or D_E/dotD/Riesz/Green/heat/zeta/torsion payload
```

and then check:

```text
delta tau = 0,
rho_E(gamma) rho_E(delta) = zeta^tau(gamma,delta) rho_E(gamma delta),
tau(F_i)+tau(G_i)=0 and tau(P)=0,
period(tau) is selected by H_sel/G_ret,
Freed-Witten/Bianchi/projector checks use the same tau,
the response payload comes from the same source.
```

## Decision

The source-search lane does not close. The next artifact should make the
Hessian/kernel derivation interface executable:

```text
{candidate["next_required_artifact"]}
```

closure claimed: no
target fitting used: no
"""
    return candidate, certificate, note


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
