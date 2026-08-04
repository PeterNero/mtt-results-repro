from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

GR_SOURCE_CERT = ROOT / "certificates" / "selected_gr_hessian_block_source_theorem_certificate.json"
Z64_QG_BRIDGE = ROOT / "certificates" / "conditional_z64_qg_gap_bridge_certificate.json"

GR = OBSIDIAN / "11 General Relativity & Geometry" / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md"
QG = OBSIDIAN / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
CENTRAL_CIRCLE = (
    OBSIDIAN
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)

OUT_CERT = ROOT / "certificates" / "gr_tt_aint_z64_identity_source_hunt_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    gr_cert = json.loads(GR_SOURCE_CERT.read_text(encoding="utf-8"))
    bridge = json.loads(Z64_QG_BRIDGE.read_text(encoding="utf-8"))
    gr = read(GR)
    qg = read(QG)
    central = read(CENTRAL_CIRCLE)

    source_tests = {
        "gr_reduction_has_einstein_normalization": has(gr, "G_{\\rm eff}^{-1}", "Einstein--Hilbert"),
        "qg_has_graviton_tt_or_projected_graviton": has(qg, "graviton propagator", "projected"),
        "qg_has_aint_gap_but_not_z64_identity": has(qg, "A_{\\rm int}", "\\lambda_\\ast") and "Z_64" not in qg and "Z64" not in qg,
        "central_circle_links_gravity_structurally": has(central, "Mass, Gravity, and Time", "central circle"),
        "central_circle_does_not_supply_tt_aint_z64_formula": not has(
            central,
            "TT",
            "Z_64",
            "A_int",
        ),
        "existing_gr_cert_rejects_z64_as_gr_substitute": gr_cert["closure_conditions"]["z64_allowed_as_gr_substitute"] is False,
        "conditional_bridge_not_usable_as_gr_gap": bridge["verdict"]["usable_now_as_GR_modal_gap"] is False,
    }

    findings = {
        "positive_clues": [
            "central circle is repeatedly described as shared coherence/bookkeeping for mass, gravity, and time",
            "QG supplies an A_int gap-controlled projected graviton framework",
            "Z64 exact branch supplies a strong internal central-circle tower gap",
            "conditional Z64/QG bridge closes when the excluded block is the QG noncoherent complement",
        ],
        "blocking_facts": [
            "no source formula identifies the GR TT response A_int complement with the exact Z64 tower",
            "existing GR source audit identifies TT/Lichnerowicz as target but says Z64 is not a GR substitute",
            "closure-strain to TT remains the selected GR route in this repo",
            "conditional Z64 bridge is scoped to exact flavor/CP or any later branch proven to share the same complement",
        ],
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "gr_tt_aint_z64_identity_source_hunt",
        "status": "GR_TT_AINT_Z64_IDENTITY_NOT_SOURCED_CLOSURE_STRAIN_ROUTE_REMAINS",
        "input_certificates": {
            "selected_gr_hessian_block_source_theorem": str(GR_SOURCE_CERT),
            "conditional_z64_qg_gap_bridge": str(Z64_QG_BRIDGE),
        },
        "source_files": {
            "gr": str(GR),
            "qg": str(QG),
            "central_circle": str(CENTRAL_CIRCLE),
        },
        "source_tests": source_tests,
        "findings": findings,
        "next_required_object": {
            "name": "GR_TT_Selected_Aint_Identity_or_New_Complement_Theorem",
            "must_either": [
                "prove GR TT closure-strain A_int is the same exact Z64 central-circle tower quotient",
                "or compute a distinct selected GR TT A_int complement and its gap",
            ],
            "minimum_data": [
                "domain of GR TT closure-strain operator",
                "projector/quotient removing diffeomorphism and scalar zero modes",
                "explicit relation, or non-relation, to the shared central-circle tower",
                "lowest positive eigenvalue in internal units",
            ],
        },
        "verdict": {
            "z64_is_best_structural_clue": True,
            "z64_closes_gr_gap_now": False,
            "closure_strain_route_still_primary_for_gr": True,
            "most_honest_current_claim": (
                "The exact Z64 branch is a powerful shared-coherence clue, but the "
                "GR TT modal gap is not closed until the TT closure-strain operator "
                "is either identified with that branch or computed separately."
            ),
        },
        "guardrails": {
            "claims_GR_TT_Aint_equals_Z64": False,
            "claims_GR_modal_gap_closed": False,
            "claims_physical_GN_or_MPl": False,
            "forbids_structural_central_circle_language_as_operator_identity": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
