"""Build the Qa/SU3 internal-packet alignment theorem for older determinant trails."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
QA_REPO = ROOT.parent / "mtt-qa-su3-packet-proof"

QA_CERT = QA_REPO / "certificates" / "gr_surface_internal_quantum_separation_theorem_certificate.json"
OUTPUT_DATA = DATA / "qa_su3_internal_packet_alignment.candidate.json"
OUTPUT_CERT = CERTS / "qa_su3_internal_packet_alignment_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Internal_Packet_Alignment_v1.md"


LOCAL_DIAGNOSTIC_NOTES = [
    PROOF / "Compact_Nil_Scalar_Hurwitz_Zeta_Candidate_v1.md",
    PROOF / "Selected_Qa_SU3_BRST_Determinant_With_Weitzenbock_E_v1.md",
    PROOF / "Selected_Qa_SU3_PNonzero_Physical_Quotient_Determinant_Theorem_v1.md",
    PROOF / "Selected_Qa_SU3_Local_System_Torsion_Source_Extraction_v1.md",
]


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"missing": str(path)}


def build() -> tuple[dict[str, object], dict[str, object], str]:
    qa_cert = load_json(QA_CERT)
    diagnostics = {
        note.name: {
            "path": str(note.relative_to(ROOT)),
            "present": note.exists(),
            "already_blocks_closure": (
                "does not close" in note.read_text(encoding="utf-8", errors="ignore")
                or "not the selected Qa/SU3" in note.read_text(encoding="utf-8", errors="ignore")
                if note.exists()
                else False
            ),
        }
        for note in LOCAL_DIAGNOSTIC_NOTES
    }
    candidate = {
        "candidate": "SelectedQaSU3InternalPacketAlignment",
        "status": "QA_SU3_INTERNAL_PACKET_ALIGNMENT_BUILT_OLD_NIL_TRAIL_DIAGNOSTIC_ONLY",
        "inputs": {
            "qa_surface_internal_theorem": str(QA_CERT),
            "qa_surface_internal_status": qa_cert.get("status"),
            "local_diagnostic_notes": diagnostics,
            "target_fitting_used": False,
        },
        "alignment_theorem": {
            "name": "OlderQaSU3NilDeterminantTrailDiagnosticOnly",
            "statement": (
                "Under the selected Qa/SU3 GR-surface/internal-quantum separation, "
                "the real smooth elastic continuum is routed to the GR/protospinor sector. "
                "The selected Qa/SU3 determinant source is the finite internal coherent packet, "
                "whose reduced logdet is log(2008). Therefore the older compact Nil scalar, "
                "BRST, Hodge, Weitzenbock, and local-system torsion computations in this repo "
                "remain diagnostic or route-finding artifacts, not the proof source for the "
                "selected internal Qa/SU3 determinant."
            ),
            "closed_value_imported_as_status_only": "log(2008)",
            "old_trail_role": "diagnostic_only_not_selected_internal_determinant",
        },
        "reclassification": {
            "compact_nil_scalar_hurwitz_zeta": "diagnostic_near_miss",
            "hodge_oneform_brs_weitzebock": "diagnostic_operator_bookkeeping",
            "p_nonzero_physical_quotient": "diagnostic_retired_as_final_source",
            "local_system_torsion": "still_open_as_alternative_only_if_same_source_character_is_supplied",
        },
        "guardrails": [
            "do not use compact Nil scalar zeta as the selected Qa/SU3 determinant",
            "do not add a smooth internal complement determinant on top of log(2008)",
            "do not route the GR/protospinor smooth surface determinant into Qa/SU3",
            "do not use observed gauge residuals to select the packet",
            "do not claim full electroweak, Qa/SU3 physical threshold, or SM closure from this alignment",
        ],
        "decision": {
            "old_nil_smooth_determinant_trail_in_danger": False,
            "old_nil_smooth_determinant_trail_role": "retained_as_diagnostics_and_no_go_evidence",
            "selected_internal_reduced_Qa_SU3_determinant": "log(2008)",
            "full_electroweak_or_SM_closure_now": False,
            "next_required_bridge": "internal_reduced_logdet_to_coupling_or_threshold_response_without_double_counting",
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3InternalPacketAlignment",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "older_nil_determinant_trail_reclassified": True,
            "qa_su3_internal_reduced_logdet_imported_as_status": "log(2008)",
            "smooth_GR_surface_routed_away_from_Qa_SU3": True,
        },
        "what_remains_open": {
            "coupling_bridge": True,
            "full_electroweak_closure": True,
            "full_SM_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    theorem = candidate["alignment_theorem"]
    diagnostics = candidate["inputs"]["local_diagnostic_notes"]
    rows = "\n".join(
        f"- `{name}`: {data['path']} -> {'diagnostic/blocked' if data['already_blocks_closure'] else 'check wording'}"
        for name, data in diagnostics.items()
    )
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    return f"""# Selected Qa/SU3 Internal Packet Alignment v1

## Result

The older compact Nil / scalar zeta / BRST / Weitzenbock / torsion trail is not
wrong. It is reclassified.

```text
role = diagnostic and no-go evidence
selected internal reduced Qa/SU3 determinant = {theorem["closed_value_imported_as_status_only"]}
full electroweak or SM closure = not claimed
```

## Theorem

{theorem["statement"]}

## Local Trail Status

{rows}

## Guardrails

{guardrails}

## Next Bridge

The next no-knob task is not another smooth Nil determinant. It is the bridge:

```text
internal reduced logdet log(2008)
-> selected coupling / threshold response rule
```

with no GR-surface double count and no observed-residual selection.
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_CERT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
