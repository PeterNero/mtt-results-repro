"""Build the section-ring/twisted-module operator-row gate for U1/hypercharge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "u1_operator_source_packet": DATA / "selected_u1_hypercharge_operator_spectrum_source_packet.candidate.json",
    "iwasawa_section_ring_interface": DATA / "iwasawa_line_bundle_section_ring_interface.candidate.json",
    "iwasawa_automorphy_nogo": DATA / "iwasawa_automorphy_cocycle_data_or_nogo.candidate.json",
    "twisted_section_ring_gate": DATA / "twisted_section_ring_and_gerbe_source_gate.candidate.json",
    "gerbe_response_fill": DATA / "gerbe_twisted_local_system_response_fill_attempt.candidate.json",
    "u1_projector": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1_hypercharge_section_ring_or_twisted_module_operator_row.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1_hypercharge_section_ring_or_twisted_module_operator_row_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_Hypercharge_Section_Ring_or_Twisted_Module_Operator_Row_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    source_packet = load(INPUTS["u1_operator_source_packet"])
    section_ring = load(INPUTS["iwasawa_section_ring_interface"])
    automorphy_nogo = load(INPUTS["iwasawa_automorphy_nogo"])
    twisted_gate = load(INPUTS["twisted_section_ring_gate"])
    gerbe_fill = load(INPUTS["gerbe_response_fill"])
    u1_projector = load(INPUTS["u1_projector"])

    lanes = {
        "ordinary_iwasawa_section_ring": {
            "status": "BLOCKED_CURRENT_SOURCE_NO_AUTOMORPHY_OR_SECTION_BASES",
            "support": [
                "line-bundle charge typing interface exists",
                "literal scalar constants are rejected, correctly forcing charged automorphic frames",
            ],
            "blockers": [
                "factor-of-automorphy cocycle data",
                "selected section bases for U1/Y charge spaces",
                "multiplication constants",
                "operator row derived from the section-ring connection/Laplacian",
            ],
            "input_status": {
                "section_ring": section_ring["status"],
                "automorphy": automorphy_nogo["status"],
            },
        },
        "projective_gerbe_or_twisted_module": {
            "status": "BLOCKED_CURRENT_SOURCE_NO_LOCAL_SYSTEM_RESPONSE_OR_OPERATOR_ROW",
            "support": [
                "twisted-module typing repairs the nonclosed c-axis obstruction",
                "gerbe response fill attempt carries source family, Bianchi support, primitive central support, and twist cancellation",
            ],
            "blockers": [
                "selected representative-to-central-cocycle map for U1/Y",
                "projective local-system matrices or D_E/rho_E response",
                "positive threshold spectrum or zeta/heat/torsion finite part",
                "proof the U1/Y row uses P_perp on V/<s>",
            ],
            "input_status": {
                "twisted_gate": twisted_gate["status"],
                "gerbe_fill": gerbe_fill["status"],
            },
        },
        "finite_qutrit_projector_lane": {
            "status": "CLOSED_FOR_QUOTIENT_INDEX_ONLY_NOT_OPERATOR_ROW",
            "support": [
                "P_perp is selected with rank two on the rank-three U1 carrier",
                "trace index Tr(P_perp)/Tr(I_3)=2/3 is closed",
            ],
            "blockers": [
                "P_perp does not emit positive eigenvalues",
                "the quotient trace does not determine the U1/Y threshold finite part",
            ],
            "input_status": u1_projector["status"],
        },
        "minimal_source_amendment": {
            "status": "REQUIRED_TO_CLOSE",
            "packet_fields": [
                "U1/Y charge object: ordinary line bundle, projective gerbe module, or local system",
                "selected transition/automorphy/cocycle data and compact quotient domain",
                "connection or operator formula for the threshold row",
                "P_perp compatibility and zero-mode quotient policy",
                "positive spectrum with multiplicities and hypercharge/index weights",
                "finite determinant prescription and no-target-fit certificate",
            ],
        },
    }

    decision = {
        "section_ring_or_twisted_module_operator_row_found": False,
        "ordinary_section_ring_lane_open": True,
        "twisted_module_lane_open": True,
        "finite_qutrit_lane_closes_only_index": True,
        "lambda_12_closed": False,
        "primary_next_object": "Selected_U1_Hypercharge_Minimal_Source_Amendment_or_Direct_Operator_Row_v1",
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedU1HyperchargeSectionRingOrTwistedModuleOperatorRow",
        "status": "U1_HYPERCHARGE_SECTION_RING_OR_TWISTED_MODULE_ROW_REDUCED_SOURCE_AMENDMENT_REQUIRED",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "prior_source_packet_status": source_packet["status"],
        "lanes": lanes,
        "decision": decision,
        "closure_claimed": True,
        "closure_scope": "route_reduction_and_required_source_amendment_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1HyperchargeSectionRingOrTwistedModuleOperatorRow",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "ordinary_section_ring_blockers_identified": True,
            "twisted_module_blockers_identified": True,
            "finite_qutrit_lane_scoped_to_index_only": True,
            "minimal_source_amendment_packet_specified": True,
            "no_target_fit_used": True,
        },
        "open": {
            "u1_y_operator_row": True,
            "selected_automorphy_or_twisted_cocycle_data": True,
            "selected_connection_or_local_system_response": True,
            "positive_spectrum_and_finite_part": True,
            "lambda_12": True,
        },
        "next_required_object": decision["primary_next_object"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    lanes = candidate["lanes"]
    amend = "\n".join(f"- {x}" for x in lanes["minimal_source_amendment"]["packet_fields"])
    return f"""# Selected U1 Hypercharge Section Ring or Twisted Module Operator Row v1

## Result

```text
section_ring_or_twisted_module_operator_row_found = false
lambda_12_closed = false
target_fitting_used = false
```

The current source state has enough structure to say what the U1/Y row must be,
but not enough to emit the row.

## Lane Status

```text
ordinary_iwasawa_section_ring = {lanes["ordinary_iwasawa_section_ring"]["status"]}
projective_gerbe_or_twisted_module = {lanes["projective_gerbe_or_twisted_module"]["status"]}
finite_qutrit_projector_lane = {lanes["finite_qutrit_projector_lane"]["status"]}
```

The ordinary section-ring lane is blocked at automorphy factors, section bases,
multiplication constants, and the operator row derived from those data.

The projective/twisted lane has the right typing discipline, but is blocked at
the selected cocycle/local-system response and determinant finite part.

The finite qutrit lane remains valid only for the quotient index `2/3`; it does
not create a local determinant operator.

## Minimal Source Amendment

To close this gate, the next source packet must supply:

{amend}

## Decision

```text
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
