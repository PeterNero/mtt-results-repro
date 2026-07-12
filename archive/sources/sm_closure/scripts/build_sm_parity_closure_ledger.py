"""Build the MTT SM-parity closure ledger."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

OUTPUT_DATA = DATA / "sm_parity_closure_ledger.candidate.json"
OUTPUT_CERT = CERTS / "sm_parity_closure_ledger_certificate.json"

SOURCES = {
    "qa_su3_full_corpus": TEXPAPERS
    / "mtt-qa-su3-packet-proof"
    / "proof_corpus"
    / "Selected_Qa_SU3_Full_Corpus_Dependency_Audit_v1.md",
    "q79_full_sm": TEXPAPERS
    / "mtt-q79-proof-repro"
    / "proof_corpus"
    / "Selected_Full_SM_Data_Theorem_Attempt_v1.md",
    "nonsm_status": TEXPAPERS / "mtt-nonsm-constants-no-knob" / "certificates" / "nonsm_constants_status_matrix_certificate.json",
    "gr_dependency": TEXPAPERS
    / "mtt-protospinor-gr-response-proof"
    / "certificates"
    / "gr_dependency_matrix_certificate.json",
    "theta_gauge": OBSIDIAN
    / "18 Theta-Closure & Execution Program"
    / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md",
    "qft": OBSIDIAN / "7 Quantum Field Theory",
    "qm": OBSIDIAN / "6 Quantum Mechanics",
    "gr": OBSIDIAN / "11 General Relativity & Geometry",
}


def exists(path: Path) -> bool:
    return path.exists()


def ledger_row(
    physics_object: str,
    sm_status: str,
    mtt_parity_status: str,
    measured_input_allowed: bool,
    no_knob_target: str,
    current_evidence: list[str],
    remaining_gap: str,
    priority: str,
) -> dict[str, object]:
    return {
        "physics_object": physics_object,
        "sm_status": sm_status,
        "mtt_parity_status": mtt_parity_status,
        "measured_input_allowed_for_sm_parity": measured_input_allowed,
        "no_knob_upgrade_target": no_knob_target,
        "current_evidence": current_evidence,
        "remaining_gap": remaining_gap,
        "priority": priority,
    }


def main() -> None:
    source_presence = {key: str(path) for key, path in SOURCES.items() if exists(path)}
    source_missing = {key: str(path) for key, path in SOURCES.items() if not exists(path)}
    ledger = [
        ledger_row(
            "quantum state and measurement interface",
            "QM takes Hilbert space, observables, Born rule, and state-update/measurement structure as core formal data.",
            "SUPPORTED_STRUCTURE_OPEN_FORMALIZATION",
            True,
            "derive Born/record selection from MTT coherence/admissibility fixed-point rule",
            ["local QM corpus present", "fixed-point and projection language present in proof repos"],
            "Need one compact axiomatized MTT measurement theorem with typed record/projection map.",
            "P0",
        ),
        ledger_row(
            "local QFT sector",
            "SM/QFT takes field content, gauge group, couplings, and renormalized parameters as measured or specified inputs.",
            "SUPPORTED_STRUCTURE_OPEN_AXIOMS",
            True,
            "derive allowed local fields and couplings from selected modal/operator packets",
            ["QFT corpus present", "operator-exit ledgers in q79 and Qa/SU3 repos"],
            "Need a formal MTT-to-local-QFT functor or equivalence limit.",
            "P0",
        ),
        ledger_row(
            "SM gauge group SU3xSU2xU1",
            "SM specifies the gauge group and representations.",
            "PARTIAL_STRUCTURE_OPEN_SELECTION",
            True,
            "select SU3xSU2xU1 and representations from finite/topological MTT packet",
            ["q79 finite-sector results", "Qa/SU3 packet proof repo", "theta gauge-coupling corpus"],
            "Need a single selected SM-sector embedding theorem, not scattered sector evidence.",
            "P0",
        ),
        ledger_row(
            "fermion representations and generations",
            "SM specifies fermion representation content and three generations.",
            "PARTIAL_TOPOLOGY_EVIDENCE_OPEN",
            True,
            "derive three-family representation packet and anomaly cancellation from selected topology",
            ["q79 three-family/Iwasawa artifacts", "Qa/SU3 monad topology ledgers"],
            "Need selected typed monad/Cech data with actual maps, not just topology.",
            "P0",
        ),
        ledger_row(
            "gauge couplings",
            "SM treats gauge couplings as measured running parameters.",
            "PARITY_ALLOWED_NO_KNOB_OPEN",
            True,
            "derive threshold kernels and absolute normalizations from selected operator data",
            ["nonsm electroweak interfaces", "theta gauge-coupling corpus"],
            "Need selected threshold/local determinant spectra; current no-knob closure is open.",
            "P1",
        ),
        ledger_row(
            "Yukawa matrices and masses",
            "SM takes Yukawa matrices as measured inputs.",
            "PARITY_ALLOWED_NO_KNOB_OPEN",
            True,
            "derive Yukawa magnitudes, CKM/PMNS, and masses from selected overlap/operator kernels",
            ["q79 CKM/Yukawa validator stack", "selected full SM data theorem attempt"],
            "Need selected heavy-link/source matrices, not benchmark entries.",
            "P1",
        ),
        ledger_row(
            "CP phases",
            "SM takes CKM phase and theta-like parameters as measured/fit parameters.",
            "FINITE_PHASE_STRUCTURE_PROMISING_SELECTION_OPEN",
            True,
            "derive CP characters from selected finite quotient, e.g. q79/Z64/Z448 carrier",
            ["q79 finite character artifacts", "Z64 exact branch"],
            "Need selected source linking finite character to physical CKM/PMNS data without target phase fitting.",
            "P1",
        ),
        ledger_row(
            "Higgs sector",
            "SM specifies Higgs doublet, potential parameters, vev, and quartic from measurement/renormalization.",
            "STRUCTURE_OPEN",
            True,
            "derive Higgs carrier/projector and quartic threshold from selected MTT source",
            ["q79 Higgs/projector artifacts", "theta/electroweak scaffold"],
            "Need selected Higgs projector/source and RG matching ledger.",
            "P1",
        ),
        ledger_row(
            "gravity/GR sector",
            "GR takes Newton constant, metric dynamics, and stress-energy coupling as measured/axiomatic.",
            "STRUCTURAL_RECOVERY_PROMISING_ABSOLUTE_ANCHOR_OPEN",
            True,
            "derive physical Newton scale from modal gap or selected dimensional anchor",
            ["protospinor GR dependency matrix", "GR corpus", "QG corpus"],
            "Internal normalization exists, but physical dimensionful anchor remains open.",
            "P0",
        ),
        ledger_row(
            "cosmology and initial/boundary conditions",
            "SM+GR cosmology takes initial conditions and cosmological parameters from observation/model fitting.",
            "OPEN_PARITY_INTERFACE_NEEDED",
            True,
            "type cosmological parameters as measured sector/boundary data, then seek no-knob fixed-point selector",
            ["GR/QG corpus"],
            "Need cosmology parameter interface and admissible boundary-condition rule.",
            "P2",
        ),
        ledger_row(
            "dimensionful constants and units",
            "SM/GR use measured dimensional anchors and unit conventions.",
            "PARITY_ALLOWED_PHYSICAL_NO_KNOB_OPEN",
            True,
            "derive physical absolute anchor without using measured G_N, M_Pl, H0, rho_DE",
            ["nonsm dimensionful obstruction", "GR absolute normalization bridge"],
            "Can close internal units, but not physical absolute scale yet.",
            "P0",
        ),
    ]
    parity_requirements = [
        "Define MTT core axioms and typed measured-sector input policy.",
        "Prove recovery interfaces for QM, QFT, SM gauge sector, and GR at the same parameter-input standard used by SM/GR.",
        "Build a parameter ledger that distinguishes measured parity inputs from no-knob upgrade targets.",
        "Show no contradictions with known SM/QFT/GR tests at the level of the admitted measured inputs.",
        "Keep no-knob artifacts as upgrade obligations, not as prerequisites for SM-parity closure.",
    ]
    candidate = {
        "candidate": "MTTSMParityClosureLedger",
        "status": "SM_PARITY_LEDGER_BUILT_NO_KNOB_UPGRADE_PATH_OPEN",
        "source_presence": source_presence,
        "source_missing": source_missing,
        "ledger": ledger,
        "parity_requirements": parity_requirements,
        "recommended_start": {
            "artifact": "MTT_Core_Axioms_and_Measured_Parameter_Interface_v1",
            "reason": "SM parity requires a typed policy for measured inputs before comparing sectors. This avoids confusing SM-parity constants with no-knob closure.",
            "second_artifact": "MTT_SM_Sector_Embedding_Interface_v1",
        },
        "gate_results": {
            "repo_initialized": True,
            "sm_parity_distinguished_from_no_knob": True,
            "measured_inputs_allowed_for_parity": True,
            "no_knob_targets_preserved": True,
            "full_sm_parity_closed": False,
            "full_no_knob_closed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": "MTT_Core_Axioms_and_Measured_Parameter_Interface_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "MTTSMParityClosureLedger",
        "status": "MTT_SM_PARITY_LEDGER_BUILT_NO_KNOB_UPGRADE_PATH_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "sm_parity_vs_no_knob_distinction": True,
            "measured_parameter_policy_scaffold": True,
            "sector_ledger_built": True,
            "no_knob_upgrade_targets_retained": True,
        },
        "what_remains_open": {
            "core_axioms": True,
            "measured_parameter_interface_theorem": True,
            "qm_qft_sm_gr_recovery_theorems": True,
            "empirical_equivalence_ledger": True,
            "no_knob_constants": True,
            "sm_parity_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
