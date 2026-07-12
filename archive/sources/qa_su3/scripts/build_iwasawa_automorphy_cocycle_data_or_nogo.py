"""Build the Iwasawa automorphy cocycle data/no-go gate for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

SELECTED_SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
THETA_HEISENBERG_SOURCE = OBSIDIAN / "18 Theta-Closure & Execution Program" / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md"
PREVIOUS = CERTS / "iwasawa_automorphy_or_section_ring_construction_certificate.json"
TEMPLATE = CERTS / "iwasawa_automorphy_cocycle_data.template.json"
OUTPUT_DATA = DATA / "iwasawa_automorphy_cocycle_data_or_nogo.candidate.json"
OUTPUT_CERT = CERTS / "iwasawa_automorphy_cocycle_data_or_nogo_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_Qa_SU3_Iwasawa_Automorphy_Cocycle_Data_or_NoGo_v1.md"


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore")
    return {
        "path": str(path),
        "present": True,
        "terms": {key: term in text for key, term in terms.items()},
    }


def nonzero_charges(charges: list[list[int]]) -> list[list[int]]:
    return [charge for charge in charges if any(x != 0 for x in charge)]


def build() -> tuple[dict[str, object], dict[str, object], str]:
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    charges = template["factors_required_for_charges"]
    nz_charges = nonzero_charges(charges)
    selected_scan = scan(
        SELECTED_SOURCE,
        {
            "H3C": "H_3(\\mathbb{C})",
            "Gamma_subset": "\\Gamma\\subset H_3(\\mathbb{C})",
            "cocompact": "cocompact",
            "left_invariant_frame": "left-invariant",
            "lattice_generators": "lattice generators",
            "factor_of_automorphy": "factor of automorphy",
            "automorphy": "automorphy",
            "transition": "transition",
            "charge_to_factor": "charge-to-factor",
            "Appell_Humbert": "Appell-Humbert",
        },
    )
    theta_scan = scan(
        THETA_HEISENBERG_SOURCE,
        {
            "real_heisenberg_nilmanifold": "compact Heisenberg nilmanifold",
            "global_coordinates": "global coordinates",
            "lattice": "lattice",
            "left_invariant_metric": "left-invariant metric",
            "complex_iwasawa": "H_3(\\mathbb{C})",
            "factor_of_automorphy": "factor of automorphy",
        },
    )
    missing_selected_data = [
        "complex coordinate action of each Gamma generator",
        "left/right quotient convention for section equivariance",
        "charge-to-factor map q -> a_q(gamma,z)",
        "cocycle check for a_q",
        "proof that c1(a_q) equals q in the (a,b,c) basis",
        "section-space solver for s_q(gamma.z)=a_q(gamma,z)s_q(z)",
    ]
    flat_character_test = {
        "ansatz": "a_q(gamma,z)=chi_q(gamma)",
        "cocycle_passes_formally": True,
        "multiplicative_charge_law_passes_formally": True,
        "realizes_nonzero_c1_charges": False,
        "nonzero_charges_count": len(nz_charges),
        "verdict": "FAIL_FLAT_CHARACTER_ONLY_FACTORS_CANNOT_REALIZE_NONZERO_MONAD_CHARGES",
    }
    theta_adjacent_result = {
        "source_has_real_heisenberg_coordinates": theta_scan["terms"].get("global_coordinates", False),
        "usable_for_complex_iwasawa_line_bundle_automorphy": False,
        "reason": "real Heisenberg nilmanifold spectral/metric data do not provide holomorphic H_3(C) line-bundle factors",
    }
    nogo_result = {
        "current_source_cocycle_data_sufficient": False,
        "literal_constant_route_rejected": True,
        "flat_character_route_rejected_for_nonzero_charges": True,
        "theta_real_heisenberg_import_rejected": True,
        "automorphy_route_retired": False,
        "source_augmentation_required": True,
        "explicit_f_g_constructed": False,
        "g_f_zero_proved": False,
        "qa_su3_closed": False,
        "target_fitting_used": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3IwasawaAutomorphyCocycleDataOrNoGo",
        "status": "QA_SU3_IWASAWA_AUTOMORPHY_COCYCLE_DATA_CURRENT_SOURCE_NO_GO",
        "input_status": {"automorphy_construction": previous["status"]},
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "selected_source_scan": selected_scan,
        "theta_adjacent_scan": theta_scan,
        "required_charges": charges,
        "flat_character_test": flat_character_test,
        "theta_adjacent_result": theta_adjacent_result,
        "missing_selected_data": missing_selected_data,
        "gate_results": {
            "selected_source_identifies_H3C_and_Gamma": "PASS_PARTIAL_GEOMETRY_SOURCE"
            if selected_scan["terms"]["H3C"] and selected_scan["terms"]["Gamma_subset"]
            else "FAIL_H3C_GAMMA_NOT_FOUND",
            "lattice_generator_action": "FAIL_NOT_PRINTED",
            "charge_to_factor_map": "FAIL_NOT_PRINTED",
            "cocycle_data": "FAIL_NOT_PRINTED",
            "flat_character_shortcut": flat_character_test["verdict"],
            "theta_heisenberg_import": "FAIL_ADJACENT_REAL_NIL_DATA_NOT_COMPLEX_IWASAWA_AUTOMORPHY",
            "automorphy_route": "OPEN_REQUIRES_NEW_DATA_NOT_CURRENT_SOURCE",
            "qa_su3_closure": "FAIL_NO_EXPLICIT_SECTIONS_OR_OPERATOR_EXIT",
        },
        "nogo_result": nogo_result,
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Source_Augmentation_Packet_for_Iwasawa_Monad_Maps_v1",
            "must_supply": missing_selected_data,
            "minimal_closure_payload": [
                "two nonzero product constants m_i, or full multiplication table",
                "nonzero section representatives in matching F_i and G_i spaces",
                "coefficient choice satisfying the symbolic relation",
                "local-freeness/stability certificate for those exact maps",
            ],
        },
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "template_path": candidate["template_path"],
        "selected_source_scan": selected_scan,
        "theta_adjacent_scan": theta_scan,
        "required_charges": charges,
        "flat_character_test": flat_character_test,
        "theta_adjacent_result": theta_adjacent_result,
        "missing_selected_data": missing_selected_data,
        "gate_results": candidate["gate_results"],
        "nogo_result": nogo_result,
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    return f"""# Selected Qa/SU3 Iwasawa Automorphy Cocycle Data or NoGo v1

## Purpose

This artifact tests whether the current corpus contains enough automorphy data to realize the Iwasawa monad maps as global holomorphic sections.

## Source Scan

The selected heterotic source does identify:

```text
H_3(C)
Gamma subset H_3(C)
Gamma cocompact
left-invariant frame
```

It does not print:

```text
lattice generators
complex coordinate action of Gamma
factor of automorphy
charge-to-factor map
transition functions
section-space solver
```

The adjacent Theta Heisenberg nilmanifold source has real Heisenberg coordinate and lattice data, but it is not a holomorphic `H_3(C)` line-bundle automorphy packet and cannot be imported as such.

## Flat Character Test

A character-only ansatz

```text
a_q(gamma,z) = chi_q(gamma)
```

formally satisfies the group-cocycle shape and multiplicative law, but it is flat. It therefore cannot realize the eleven nonzero Chern-charge classes needed by the monad maps.

```text
nonzero required charges: {candidate["flat_character_test"]["nonzero_charges_count"]}
flat character route rejected: yes
```

## NoGo

Current source data are insufficient to construct the automorphy cocycle. This does not retire the automorphy route; it says the current papers must be augmented with the missing non-flat factor-of-automorphy data.

## Minimal Missing Data

```text
complex coordinate action of each Gamma generator
left/right quotient convention for section equivariance
charge-to-factor map q -> a_q(gamma,z)
cocycle check for a_q
proof that c1(a_q) equals q in the (a,b,c) basis
section-space solver for s_q(gamma.z)=a_q(gamma,z)s_q(z)
```

## Verdict

```text
current source cocycle data sufficient: no
literal constant route rejected: yes
flat character route rejected for nonzero charges: yes
Theta real Heisenberg import rejected: yes
automorphy route retired: no
source augmentation required: yes
explicit f,g constructed: no
g*f=0 proved: no
Qa/SU3 closed: no
target fitting used: no
```

Next artifact:

```text
{candidate["next_required_artifact"]["name"]}
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
