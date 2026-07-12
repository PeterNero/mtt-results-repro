"""Build the initial Qa/SU3 superset route-map certificate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
OUTPUT = CERTS / "initial_superset_route_map_certificate.json"


def load_status(path: Path) -> str:
    if not path.exists():
        return "MISSING"
    return json.loads(path.read_text(encoding="utf-8")).get("status", "UNKNOWN")


def scan(path: Path, terms: dict[str, str]) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {"path": str(path), "present": True, "terms": {key: term.lower() in text for key, term in terms.items()}}


def main() -> None:
    input_status = {
        "nonsm_route_map": load_status(NONSM / "certificates" / "selected_qa_su3_superset_source_route_map_certificate.json"),
        "nonsm_automorphy_nogo": load_status(NONSM / "certificates" / "selected_qa_su3_iwasawa_automorphy_cocycle_data_or_nogo_certificate.json"),
        "nonsm_monad_transfer": load_status(NONSM / "certificates" / "selected_qa_su3_monad_to_operator_packet_transfer_gate_certificate.json"),
        "q79_full_sm_closure": load_status(Q79 / "certificates" / "full_sm_closure_attempt_certificate.json"),
        "gr_dependency": load_status(GR / "certificates" / "gr_dependency_matrix_certificate.json"),
    }
    sources = {
        "flux_iwasawa": scan(
            OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
            {
                "iwasawa": "Iwasawa",
                "h3c": "H_3(\\mathbb{C})",
                "monad": "monad",
                "generic_maps": "generic holomorphic maps",
                "hym": "Hermitian--Yang--Mills",
                "a01": "A}^{(0,1)",
                "transition": "transition",
                "automorphy": "automorphy",
            },
        ),
        "theta_color": scan(
            OBSIDIAN
            / "18 Theta-Closure & Execution Program"
            / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization.md",
            {"color_fiber": "color fiber", "color_harmonic": "color harmonic", "su3": "SU(3)"},
        ),
        "q79_twisted": scan(
            Q79 / "proof_corpus" / "Visible_Twisted_Chan_Paton_Rescue_v1.md",
            {"twisted": "twisted", "chan_paton": "Chan", "b_field": "B-field", "hym": "HYM"},
        ),
    }
    output = {
        "certificate": "InitialQaSU3SupersetRouteMap",
        "status": "QA_SU3_PACKET_REPO_INITIALIZED_PRIMARY_SOURCE_AUGMENTATION_ROUTE",
        "input_status": input_status,
        "source_scans": sources,
        "selected_packet_schema": [
            "source_certificate",
            "bundle_sheaf_local_system_or_twisted_module",
            "representation_and_physical_quotient",
            "D_E_or_rho_E_data",
            "heat_spectrum_zeta_or_torsion_finite_part",
        ],
        "route_ranking": [
            "source_augmented_iwasawa_automorphy_section_ring",
            "projective_gerbe_chan_paton_twisted_packet",
            "direct_galerkin_operator_packet",
            "theta_color_harmonic_representation_selector",
            "m_theory_g2_pushdown",
            "source_certified_a01_erratum",
        ],
        "first_experiment": "Selected_Qa_SU3_Source_Augmentation_Packet_for_Iwasawa_Monad_Maps_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
