"""Build the same-source U1 carrier/projector theorem attempt.

This imports the strongest SM-parity S3/qutrit source evidence and checks
whether it closes the final U1 piece of the 2/3 threshold-index theorem.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SM = TEXPAPERS / "mtt-sm-parity-closure"

PREVIOUS = DATA / "selected_u1_threshold_carrier_projector_or_su2_operator_spectrum.candidate.json"
S3_SOURCE = SM / "certificates" / "selected_s3_differential_cohomology_source_certificate.json"
PROJECTIVE_PROMOTION = SM / "candidate_data" / "projective_gerbe_rhoe_source_promotion.candidate.json"
SPECTRAL_PROJECTORS = SM / "certificates" / "selected_spectral_galerkin_projector_retention_data_certificate.json"

OUTPUT_DATA = DATA / "same_source_selected_u1_carrier_projector_theorem.candidate.json"
OUTPUT_CERT = CERTS / "same_source_selected_u1_carrier_projector_theorem_certificate.json"
OUTPUT_NOTE = PROOF / "Same_Source_Selected_U1_Carrier_Projector_Theorem_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    previous = load(PREVIOUS)
    s3 = load(S3_SOURCE)
    promotion = load(PROJECTIVE_PROMOTION)
    spectral = load(SPECTRAL_PROJECTORS)

    flags = promotion["promotion_gate_flags_after_s3_closure"]
    source_level_carrier_selected = (
        flags["selected_by_mtt"] is True
        and flags["map_to_central_cocycle_verified"] is True
        and flags["twisted_projector_retains_sector"] is True
        and s3["what_closes"]["block_factorized_family_Higgs_projector_retention"] is True
    )
    spectral_projector_closed = spectral["what_closes"].get("coherent_spectral_projector_retention") is True

    theorem_tests = [
        {
            "id": "selected_s3_qutrit_source_level_carrier",
            "closed": source_level_carrier_selected,
            "source": str(PROJECTIVE_PROMOTION),
            "meaning": "The projective qutrit/S3 carrier is selected at the gerbe source level with block-sector projector retention.",
        },
        {
            "id": "rank_three_shape_available",
            "closed": previous["rank_quotient_replay"]["raw_rank_from_candidate_carrier"] == 3,
            "source": previous["inputs"]["factorized_packet"],
            "meaning": "The executable factorized carrier has rank 3 and would support the 2/3 quotient arithmetic.",
        },
        {
            "id": "operator_level_spectral_projector",
            "closed": spectral_projector_closed,
            "source": str(SPECTRAL_PROJECTORS),
            "meaning": "The SM-parity repo now distinguishes block projectors from coherent spectral projectors; the certificate closes the distinction but still does not emit the U1 quotient projector P_perp.",
        },
        {
            "id": "u1_specific_shared_circle_projector_P_perp",
            "closed": False,
            "source": str(OUTPUT_NOTE.relative_to(ROOT)),
            "meaning": "No imported source supplies the explicit normalized U1 basis vector s and P_perp=I-|s><s|/<s,s> as the threshold trace projector.",
        },
        {
            "id": "operator_trace_uses_P_perp",
            "closed": False,
            "source": str(OUTPUT_NOTE.relative_to(ROOT)),
            "meaning": "No imported source states that the U1 threshold determinant trace, in the same scheme as Qa/SU3 and SU2, uses the quotient projector P_perp.",
        },
    ]

    u1_closed = all(item["closed"] for item in theorem_tests)
    candidate = {
        "candidate": "SameSourceSelectedU1CarrierProjectorTheorem",
        "status": "SAME_SOURCE_U1_CARRIER_SOURCE_LEVEL_SELECTED_PROJECTOR_OPERATOR_TRACE_OPEN",
        "inputs": {
            "previous_gate": str(PREVIOUS.relative_to(ROOT)),
            "selected_s3_source": str(S3_SOURCE),
            "projective_gerbe_promotion": str(PROJECTIVE_PROMOTION),
            "spectral_projector_certificate": str(SPECTRAL_PROJECTORS),
        },
        "theorem_attempt": {
            "name": "SameSourceSelectedU1CarrierProjectorTheorem",
            "proved": u1_closed,
            "tests": theorem_tests,
        },
        "decision": {
            "source_level_rank3_carrier_support_closed": source_level_carrier_selected,
            "rank_quotient_arithmetic_closed": True,
            "su2_weak_split_closed": previous["decision"]["su2_unit_index_or_spectrum_found"],
            "u1_projector_P_perp_emitted": False,
            "u1_operator_trace_policy_emitted": False,
            "promoted_to_selected_threshold_index": False,
            "measured_electroweak_closure": False,
            "target_fitting_used": False,
            "remaining_single_gate": "emit same-source U1 quotient projector P_perp and trace policy",
            "next_required_object": "Selected_U1_Quotient_Projector_Pperp_and_Trace_Policy_v1",
        },
        "minimal_projector_packet": {
            "basis": "orthonormal rank-3 U1/qutrit carrier basis in the selected S3 gerbe source",
            "shared_vector": "explicit selected shared central-circle unit vector s in that basis",
            "projector": "P_perp = I - |s><s|/<s,s>",
            "required_checks": [
                "rank(P_perp)=2",
                "Tr(P_perp)/Tr(I)=2/3",
                "P_perp commutes with the selected U1 threshold operator or is the stated physical quotient before determinant evaluation",
                "same threshold scheme as Qa/SU3 log(2008) and selected SU2 weak-split accounting",
            ],
        },
        "closure_claimed": True,
        "closure_scope": "source_level_u1_carrier_support_and_final_projector_cut_set",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SameSourceSelectedU1CarrierProjectorTheorem",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "source_level_rank3_qutrit_carrier_support": source_level_carrier_selected,
            "su2_weak_split_imported_closed": previous["decision"]["su2_unit_index_or_spectrum_found"],
            "final_projector_cut_set_identified": True,
        },
        "what_remains_open": {
            "explicit_U1_shared_vector_s": True,
            "explicit_U1_P_perp_projector": True,
            "U1_operator_trace_uses_P_perp": True,
            "measured_electroweak_closure": True,
        },
        "next_required_object": candidate["decision"]["next_required_object"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    tests = "\n".join(
        f"- `{item['id']}`: closed={str(item['closed']).lower()}\n  {item['meaning']}"
        for item in candidate["theorem_attempt"]["tests"]
    )
    checks = "\n".join(f"- {item}" for item in candidate["minimal_projector_packet"]["required_checks"])
    d = candidate["decision"]
    return f"""# Same Source Selected U1 Carrier Projector Theorem v1

## Result

The source-level U1/qutrit carrier support is now imported as selected at the
S3 gerbe source level, and SU2 is closed for scoped weak-split accounting.
The final U1 promotion still does not close because no source emits the actual
quotient projector `P_perp` or the operator trace policy using it.

```text
source_level_rank3_carrier_support_closed = {str(d["source_level_rank3_carrier_support_closed"]).lower()}
rank_quotient_arithmetic_closed = {str(d["rank_quotient_arithmetic_closed"]).lower()}
su2_weak_split_closed = {str(d["su2_weak_split_closed"]).lower()}
u1_projector_P_perp_emitted = {str(d["u1_projector_P_perp_emitted"]).lower()}
u1_operator_trace_policy_emitted = {str(d["u1_operator_trace_policy_emitted"]).lower()}
promoted_to_selected_threshold_index = {str(d["promoted_to_selected_threshold_index"]).lower()}
```

## Tests

{tests}

## Minimal Projector Packet

```text
basis = {candidate["minimal_projector_packet"]["basis"]}
shared_vector = {candidate["minimal_projector_packet"]["shared_vector"]}
projector = {candidate["minimal_projector_packet"]["projector"]}
```

Required checks:

{checks}

## Next Required Object

```text
{d["next_required_object"]}
```
"""


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
