"""Build CONST-EM-01 alpha1 import evaluation.

The goal is to import help from corpus/repos/external sources without letting
any of them over-close the individual-constant problem.  Every import receives a
critical verdict: usable as source proof, usable as conditional/candidate
support, too loose, too constrained, or external convention only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
PROTO = TEXPAPERS / "mtt-protospinor-gr-response-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_import_evaluation"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
REPO_IMPORTS = BASE / "repo_imports_critical_evaluation.packet.json"
EXTERNAL = BASE / "external_sources_critical_evaluation.packet.json"
CONVENTIONS = BASE / "alpha1_convention_guardrail.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_ImportEvaluation_v1.md"
AUDIT = CORPUS / f"{SLUG}_audit.py"

STATUS = "MTT_CONST_EM_01_ALPHA1_IMPORT_EVALUATION_BUILT_VALUE_OPEN"
NEXT = "MTT_CONST_EM_01_Alpha1SourceStrengthCandidatePacket_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def exists(path: Path) -> bool:
    return path.exists()


def load(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    sm_strength = SM_PARITY / "candidate_data" / "selected_alpha1_source_strength_normalization_theorem.candidate.json"
    sm_retarded = SM_PARITY / "candidate_data" / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt.candidate.json"
    sm_policy = SM_PARITY / "candidate_data" / "universal_source_parameter_policy.candidate.json"
    nonsm_kernel = NONSM / "candidate_data" / "alpha1_tangent_kernel_crossrepo_refinement.candidate.json"
    nonsm_closed = NONSM / "candidate_data" / "alpha1_driver_closure_and_postalpha_gate_import.candidate.json"
    qa_closed = QA_SU3 / "candidate_data" / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json"
    q79_dotd = Q79 / "certificates" / "q79_selected_dotd_alpha1_c1_response_emission_certificate.json"
    proto_kernel = PROTO / "candidate_data" / "selected_alpha1_tangent_or_retarded_overlap_kernel_construct.packet.json"

    sm_strength_data = load(sm_strength)
    sm_retarded_data = load(sm_retarded)
    sm_policy_data = load(sm_policy)
    nonsm_kernel_data = load(nonsm_kernel)
    nonsm_closed_data = load(nonsm_closed)
    qa_closed_data = load(qa_closed)

    repo_imports = {
        "schema": "MTTConstEM01RepoImportsCriticalEvaluation.v1",
        "status": "REPO_IMPORTS_EVALUATED_ALPHA1_VALUE_OPEN",
        "imports": [
            {
                "id": "SM-PARITY-ALPHA1-STRENGTH-CRITERION",
                "path": rel(sm_strength),
                "present": exists(sm_strength),
                "critical_verdict": "USABLE_AS_ACCEPTANCE_CRITERION_NOT_VALUE",
                "why_useful": "Gives necessary and sufficient current-branch conditions for alpha1_driver_verified.",
                "too_loose_risk": "If treated as value proof it only says what must be emitted, not that alpha1 is emitted.",
                "too_constrained_risk": "It is branch-specific to selected End0/HYM/B_N and may miss an equivalent alternate source route.",
                "import_as_source_proof_now": False,
            },
            {
                "id": "SM-PARITY-ALPHA1-SOURCEIDENTITY-RETARDED",
                "path": rel(sm_retarded),
                "present": exists(sm_retarded),
                "critical_verdict": "USABLE_AS_TWO_LANE_CUTSET",
                "why_useful": "Separates same-source identity from typed retarded derivative and identifies the common missing object.",
                "too_loose_risk": "Retarded-pattern analogy alone is not an alpha1 derivative proof.",
                "too_constrained_risk": "Its open flags are older than later QA imports, so it may be stale for closure status.",
                "import_as_source_proof_now": False,
            },
            {
                "id": "SM-PARITY-UNIVERSAL-PARAMETER-POLICY",
                "path": rel(sm_policy),
                "present": exists(sm_policy),
                "critical_verdict": "USABLE_AS_POLICY_GUARDRAIL",
                "why_useful": "Forbids using measured alpha or residuals as source selectors and keeps universal parameter count zero until selected.",
                "too_loose_risk": "Policy alone does not select a parameter or constant.",
                "too_constrained_risk": "Maximum of three universal parameters is a governance choice, not a physics derivation.",
                "selected_parameter_count": sm_policy_data.get("selected_parameter_count_now") if sm_policy_data else None,
                "import_as_source_proof_now": False,
            },
            {
                "id": "NONSM-ALPHA1-TANGENT-KERNEL",
                "path": rel(nonsm_kernel),
                "present": exists(nonsm_kernel),
                "critical_verdict": "USABLE_AS_CANDIDATE_KERNEL_AND_ACCEPTANCE_REFINEMENT",
                "why_useful": "Pins the unit dual candidate N_alpha1(h_ext)=1 and an exact finite promotion criterion.",
                "too_loose_risk": "Canonical L2 dual can look like a selected normalization while still being only a candidate.",
                "too_constrained_risk": "It may over-focus on one tangent kernel if a different selected source coordinate exists.",
                "import_as_source_proof_now": False,
            },
            {
                "id": "NONSM-ALPHA1-DRIVER-CLOSURE-IMPORT",
                "path": rel(nonsm_closed),
                "present": exists(nonsm_closed),
                "critical_verdict": "POTENTIAL_SOURCE_PROOF_IMPORT_REQUIRES_QA_DEPENDENCY_REPLAY",
                "why_useful": "Claims alpha1 driver, N_alpha1(h_ext)=1, du/dalpha1=h_ext, and honest dotD replay closed by QA oriented-overlap theorem.",
                "too_loose_risk": "If imported without replaying the QA dependency, this would be authority import rather than proof.",
                "too_constrained_risk": "It solves alpha1 driver, not necessarily low-energy alpha(0), alpha(M_Z), or GUT-normalized alpha1 as a measured convention.",
                "claim_status_in_source_repo": nonsm_closed_data.get("status") if nonsm_closed_data else None,
                "selected_value_if_replayed": nonsm_closed_data.get("closed_alpha1_driver", {}).get("promoted_value") if nonsm_closed_data else None,
                "import_as_source_proof_now": False,
            },
            {
                "id": "QA-SU3-U1Y-ORIENTED-OVERLAP",
                "path": rel(qa_closed),
                "present": exists(qa_closed),
                "critical_verdict": "PRIMARY_DEPENDENCY_TO_REPLAY_NEXT",
                "why_useful": "This is the cited theorem source behind the non-SM alpha1 driver closure import.",
                "too_loose_risk": "If its theorem uses local premises or hidden convention choices, it cannot close individual constants directly.",
                "too_constrained_risk": "It may prove source-strength normalization but not map to physical alpha convention by itself.",
                "status_if_present": qa_closed_data.get("status") if qa_closed_data else None,
                "import_as_source_proof_now": False,
            },
            {
                "id": "Q79-DOTD-ALPHA1-C1-RESPONSE",
                "path": rel(q79_dotd),
                "present": exists(q79_dotd),
                "critical_verdict": "USABLE_AS_DOTD_REPLAY_SUPPORT",
                "why_useful": "Provides finite dotD/C1 response emission support in the q79 branch.",
                "too_loose_risk": "Response emission is not the same as physical electromagnetic coupling value.",
                "too_constrained_risk": "q79 response may need transfer to U1Y/SM conventions before comparison.",
                "import_as_source_proof_now": False,
            },
            {
                "id": "PROTOSPINOR-ALPHA1-TANGENT-KERNEL",
                "path": rel(proto_kernel),
                "present": exists(proto_kernel),
                "critical_verdict": "USABLE_AS_GEOMETRIC_KERNEL_SUPPORT",
                "why_useful": "Independent geometric/protospinor support for the alpha1 tangent kernel lane.",
                "too_loose_risk": "Geometric analogy cannot replace same-source U1Y normalization.",
                "too_constrained_risk": "Protospinor normalization may not be the selected U1Y convention.",
                "import_as_source_proof_now": False,
            },
        ],
        "repo_level_conclusion": {
            "strongest_current_help": "QA-SU3-U1Y-ORIENTED-OVERLAP via NONSM-ALPHA1-DRIVER-CLOSURE-IMPORT",
            "safe_current_import": "acceptance criteria, candidate kernel, and dependency replay workorder",
            "unsafe_current_import": "claiming physical alpha value or alpha convention closure without QA replay and convention map",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    external = {
        "schema": "MTTConstEM01ExternalSourcesCriticalEvaluation.v1",
        "status": "EXTERNAL_SOURCES_EVALUATED_AS_CONVENTION_AND_COMPARISON_GUARDRAILS",
        "sources": [
            {
                "id": "PDG-2025-ELECTROWEAK",
                "url": "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf",
                "use": "Defines electroweak context, SU(2)xU(1) couplings, weak mixing, and input-scheme/radiative-correction discipline.",
                "critical_verdict": "NECESSARY_CONVENTION_GUARDRAIL_NOT_SOURCE_PROOF",
                "too_loose_risk": "Using PDG numerical inputs would just reproduce measured SM parameters.",
                "too_constrained_risk": "A source theory may emit a more primitive normalization that must be mapped to PDG schemes.",
            },
            {
                "id": "HVP-RUNNING-ALPHA-1910.09525",
                "url": "https://arxiv.org/abs/1910.09525",
                "use": "Confirms alpha and weak mixing angle running depend on hadronic vacuum polarization/current correlator data.",
                "critical_verdict": "RUNNING_AND_SCALE_GUARDRAIL",
                "too_loose_risk": "Hadronic running data cannot be used to select MTT source strength.",
                "too_constrained_risk": "A high-scale/source alpha result should not be rejected merely because low-energy running is not yet computed.",
            },
            {
                "id": "HVP-ALPHA-MZ-1706.09436",
                "url": "https://arxiv.org/abs/1706.09436",
                "use": "Shows alpha(M_Z) predictions include hadronic vacuum-polarization and cross-section data.",
                "critical_verdict": "COMPARISON_REQUIRES_THRESHOLD_RUNNING",
                "too_loose_risk": "Measured cross sections are comparison inputs, not no-knob derivation.",
                "too_constrained_risk": "It targets precision SM prediction, while this repo first needs source normalization.",
            },
            {
                "id": "GUT-U1-NORMALIZATION",
                "url": "https://www.sciencedirect.com/science/article/pii/S055032130800641X",
                "use": "Illustrates that U(1)/hypercharge normalization is model-dependent and often GUT-normalized.",
                "critical_verdict": "NORMALIZATION_CONVENTION_WARNING",
                "too_loose_risk": "A 5/3 factor or string-inspired normalization cannot be imported without selected operator data.",
                "too_constrained_risk": "Demanding one convention too early may hide the primitive MTT source coordinate.",
            },
        ],
        "external_level_conclusion": "External sources help define what alpha means at a scale/scheme, but none can select the MTT source value.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    conventions = {
        "schema": "MTTConstEM01Alpha1ConventionGuardrail.v1",
        "status": "ALPHA_CONVENTION_GUARDRAIL_BUILT",
        "do_not_identify_without_map": [
            "alpha(0) Thomson-limit fine-structure constant",
            "alpha(M_Z) running electromagnetic coupling",
            "alpha_1^GUT = (5/3) alpha_Y or g1=sqrt(5/3) gprime convention",
            "MTT source-strength coordinate alpha1",
            "lambda_alpha1 unit source-strength candidate",
            "N_alpha1(h_ext)=1 normalization functional value",
        ],
        "required_maps_before_comparison": [
            "selected MTT alpha1 source coordinate -> U(1)_Y/hypercharge normalization",
            "U(1)_Y and SU(2) mixing -> electromagnetic alpha convention",
            "source scale -> comparison scale such as 0 or M_Z",
            "threshold/hadronic vacuum-polarization running policy",
            "uncertainty/profile policy for any measured comparison",
        ],
        "current_working_target": "source-side alpha1 normalization/driver, not a final measured alpha(0) or alpha(M_Z) value",
        "universal_parameter_status": {
            "selected_now": 0,
            "candidate_classes": ["UP-RET-OVERLAP", "UP-ACTION-NORM"],
            "may_use_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterConstEM01ImportEvaluation.v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1-REPLAY-QA",
            "task": "Replay the QA-SU3 oriented-overlap alpha1 driver theorem and its certificate inside this repo, checking whether it is source-proof, local-premise, or too context-specific.",
        },
        "secondary": {
            "label": "CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP",
            "task": "Build the map from MTT alpha1 source-strength to alpha(0), alpha(M_Z), and GUT-normalized alpha1 conventions; do not compare values until this map exists.",
        },
        "status": "NEXT_WORKORDER_REPLAY_QA_ALPHA1_AND_BUILD_CONVENTION_MAP",
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1ImportEvaluation",
        "active_label": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH",
        "status": STATUS,
        "output_packets": {
            "repo_imports_critical_evaluation": rel(REPO_IMPORTS),
            "external_sources_critical_evaluation": rel(EXTERNAL),
            "alpha1_convention_guardrail": rel(CONVENTIONS),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "corpus_repo_external_imports_evaluated": True,
            "alpha1_convention_guardrail_built": True,
            "qa_su3_oriented_overlap_identified_as_primary_dependency": True,
            "measured_alpha_forbidden_as_selector": True,
        },
        "what_remains_open": {
            "replay_qa_su3_alpha1_driver_theorem": True,
            "decide_if_qa_import_is_valid_source_proof_here": True,
            "map_mtt_alpha1_to_physical_alpha_conventions": True,
            "derive_or_compare_any_alpha_value": True,
            "select_any_universal_parameter": True,
        },
        "recommendation": "Replay the QA-SU3 oriented-overlap alpha1 driver theorem first, then build the alpha convention map.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_ImportEvaluation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "value_claimed_now": False,
        "primary_next": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1-REPLAY-QA",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Import Evaluation v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-SOURCE-STRENGTH`

## Result

Corpus, repo, and external sources have been imported critically, not accepted
wholesale.

The strongest repo help is the non-SM constants import claiming alpha1 driver
closure from the QA-SU3 oriented-overlap theorem.  That is promising, but this
repo must replay the QA dependency before treating it as source proof.

The safest current imports are:

- SM-parity alpha1 acceptance criterion,
- SM-parity two-lane source-identity/retarded-kernel cutset,
- non-SM alpha1 tangent kernel and unit dual candidate,
- universal-parameter policy with zero selected parameters,
- external electroweak convention and running guardrails.

## Critical Guardrail

Do not identify the following without a map:

- `alpha(0)`,
- `alpha(M_Z)`,
- GUT-normalized `alpha_1`,
- MTT source-strength `alpha1`,
- `lambda_alpha1 = 1`,
- `N_alpha1(h_ext)=1`.

The current target is source-side alpha1 normalization/driver, not yet a
measured fine-structure value.

## Next

Next artifact: `{NEXT}`
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "{SLUG}"
CANDIDATE = DATA / "{SLUG}.candidate.json"
REPO_IMPORTS = BASE / "repo_imports_critical_evaluation.packet.json"
EXTERNAL = BASE / "external_sources_critical_evaluation.packet.json"
CONVENTIONS = BASE / "alpha1_convention_guardrail.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_ImportEvaluation_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_import_evaluation.py"
STATUS = "{STATUS}"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    repo_imports = load(REPO_IMPORTS)
    external = load(EXTERNAL)
    conventions = load(CONVENTIONS)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["qa_su3_oriented_overlap_identified_as_primary_dependency"] is True, "QA dependency not identified")
    require(candidate["what_remains_open"]["replay_qa_su3_alpha1_driver_theorem"] is True, "QA replay should remain open")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")

    imports = {{item["id"]: item for item in repo_imports["imports"]}}
    require(imports["SM-PARITY-ALPHA1-STRENGTH-CRITERION"]["critical_verdict"] == "USABLE_AS_ACCEPTANCE_CRITERION_NOT_VALUE", "SM criterion verdict mismatch")
    require(imports["NONSM-ALPHA1-DRIVER-CLOSURE-IMPORT"]["critical_verdict"] == "POTENTIAL_SOURCE_PROOF_IMPORT_REQUIRES_QA_DEPENDENCY_REPLAY", "nonSM closure verdict mismatch")
    require(imports["QA-SU3-U1Y-ORIENTED-OVERLAP"]["critical_verdict"] == "PRIMARY_DEPENDENCY_TO_REPLAY_NEXT", "QA verdict mismatch")
    require(all(item["import_as_source_proof_now"] is False for item in repo_imports["imports"]), "source proof imported too early")

    require(len(external["sources"]) == 4, "external source count mismatch")
    require(external["sources"][0]["critical_verdict"] == "NECESSARY_CONVENTION_GUARDRAIL_NOT_SOURCE_PROOF", "PDG verdict mismatch")
    require(external["external_level_conclusion"].endswith("none can select the MTT source value."), "external conclusion mismatch")

    required = set(conventions["do_not_identify_without_map"])
    require("alpha(0) Thomson-limit fine-structure constant" in required, "alpha0 guard missing")
    require("alpha(M_Z) running electromagnetic coupling" in required, "alphaMZ guard missing")
    require("MTT source-strength coordinate alpha1" in required, "MTT alpha1 guard missing")
    require(conventions["universal_parameter_status"]["may_use_now"] is False, "universal parameter allowed too early")

    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1-REPLAY-QA", "next primary mismatch")
    require(cert["value_claimed_now"] is False, "cert value overclaim")
    require("Do not identify" in note, "note convention guard missing")
    require("must replay the QA dependency" in note, "note QA replay guard missing")

    for packet in [candidate, repo_imports, external, conventions, cert]:
        guard(packet)

    print(f"PASS {{CANDIDATE.name}}: {{candidate['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (REPO_IMPORTS, repo_imports),
        (EXTERNAL, external),
        (CONVENTIONS, conventions),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
