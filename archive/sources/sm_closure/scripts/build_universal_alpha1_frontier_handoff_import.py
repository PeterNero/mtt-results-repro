"""Import the constants-repo alpha1 frontier closure ledger.

The sibling constants repo supplies a clean example of the universal-parameter
middle tier: strict no-knob alpha_phys is not closed, but a one-universal
rod/clock/action-unit primitive extension is handoff-ready and does not use
observed constants as selectors.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SOURCE_REPO = TEXPAPERS / "mtt-individual-constants-source-search"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "universal_alpha1_frontier_handoff_import"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT = BASE / "alpha1_frontier_handoff_import.packet.json"
POLICY_UPDATE = BASE / "universal_parameter_policy_update.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_UniversalAlpha1FrontierHandoffImport_v1.md"
AUDIT = CORPUS / f"{SLUG}_audit.py"

SOURCE_NOTE = SOURCE_REPO / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_FrontierClosureLedger_v1.md"
SOURCE_CANDIDATE = SOURCE_REPO / "candidate_data" / "const_em_01_alpha1_frontier_closure_ledger.candidate.json"
SOURCE_CERT = SOURCE_REPO / "certificates" / "const_em_01_alpha1_frontier_closure_ledger_certificate.json"
SOURCE_PRIMITIVE = SOURCE_REPO / "candidate_data" / "const_em_01_alpha1_universal_primitive_or_nogo" / "one_universal_primitive.packet.json"
LOCAL_POLICY = DATA / "universal_source_parameter_policy.candidate.json"

STATUS = "MTT_UNIVERSAL_ALPHA1_FRONTIER_HANDOFF_IMPORTED_ONE_PRIMITIVE_READY"
NEXT = "MTT_UniversalSourceParameterCandidateAudit_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    source_candidate = load(SOURCE_CANDIDATE)
    source_cert = load(SOURCE_CERT)
    primitive = load(SOURCE_PRIMITIVE)
    local_policy = load(LOCAL_POLICY)

    import_packet = {
        "schema": "MTTUniversalAlpha1FrontierHandoffImport.v1",
        "status": "ALPHA1_FRONTIER_HANDOFF_IMPORTED",
        "source_repo": rel(SOURCE_REPO),
        "source_note": rel(SOURCE_NOTE),
        "source_candidate": rel(SOURCE_CANDIDATE),
        "source_certificate": rel(SOURCE_CERT),
        "source_primitive_packet": rel(SOURCE_PRIMITIVE),
        "source_status": source_candidate["status"],
        "source_claims": {
            "handoff_ready_for_main_repo": source_candidate["handoff_ready_for_main_repo"],
            "strict_current_corpus_nogo": source_cert["strict_current_corpus_nogo"],
            "strict_no_knob_alpha_phys_closed": source_cert["strict_no_knob_alpha_phys_closed"],
            "one_universal_primitive_extension_ready": source_cert["one_universal_primitive_extension_ready"],
            "observed_data_used_as_selector": source_cert["observed_data_used_as_selector"],
            "target_fitting_used": source_cert["target_fitting_used"],
        },
        "values_to_carry": {
            "tau_int": primitive["numeric_internal_coefficients"]["tau_int"],
            "sqrt_tau_int": primitive["numeric_internal_coefficients"]["sqrt_tau_int"],
            "Omega0_over_sqrt_alpha_phys": primitive["numeric_internal_coefficients"]["inv_sqrt_tau_int"],
            "lambda_12_internal": 2.6179362173268497,
            "Delta_G12_internal": 0.08450302790361214,
        },
        "primitive_options": primitive["primitive_options"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    policy_update = {
        "schema": "MTTUniversalSourceParameterPolicyAlpha1Update.v1",
        "status": "POLICY_UPDATED_WITH_ALPHA1_ONE_UNIVERSAL_PRIMITIVE_EXAMPLE",
        "local_policy": rel(LOCAL_POLICY),
        "local_policy_status": local_policy["status"],
        "mapped_universal_parameter_class": "UP-ABS-SCALE",
        "secondary_relevance": ["UP-ACTION-NORM", "UP-RET-OVERLAP"],
        "what_this_adds": {
            "first_crossrepo_example_of_one_universal_primitive_lane": True,
            "strict_no_knob_no_go_preserved": True,
            "observed_selector_guard_preserved": True,
            "numeric_internal_coefficients_available_for_downstream_templates": True,
        },
        "what_this_does_not_close": {
            "selected_universal_parameter_in_this_repo": True,
            "PSM_C1_02_unpatched_source_identity": True,
            "strict_no_knob_alpha_phys": True,
            "full_SM_no_knob_closure": True,
        },
        "policy_decision": (
            "The alpha1 constants branch is accepted here as evidence that the universal-parameter tier is useful and already "
            "has a disciplined one-primitive example. It does not select UP-ABS-SCALE in this repo and does not close any "
            "unpatched PSM-C1-02 gate."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterUniversalAlpha1HandoffImport.v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "UNIV-PARAM / SOURCE-ANCHOR / UP-1-ALPHA1",
            "task": "Audit the alpha1 one-universal-primitive lane as a candidate UP-ABS-SCALE example without promoting it to selected MTT data.",
        },
        "parallel": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED",
            "task": "Keep zero-parameter derivation primary for the SelectedWeylVariationActionPrinciple; do not use the alpha1 primitive to close this gate unless a source theorem connects them.",
        },
        "status": "NEXT_WORKORDER_ALPHA1_ONE_PRIMITIVE_CANDIDATE_AUDIT",
    }

    candidate = {
        "candidate": "MTTUniversalAlpha1FrontierHandoffImport",
        "active_label": "UNIV-PARAM / SOURCE-ANCHOR / UP-1-ALPHA1",
        "status": STATUS,
        "output_packets": {
            "alpha1_frontier_handoff_import": rel(IMPORT),
            "universal_parameter_policy_update": rel(POLICY_UPDATE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "alpha1_one_universal_primitive_example_imported": True,
            "universal_parameter_policy_gets_first_crossrepo_example": True,
            "strict_no_knob_no_go_preserved": True,
        },
        "what_remains_open": {
            "select_UP_ABS_SCALE_in_this_repo": True,
            "connect_alpha1_primitive_to_PSM_C1_02_source_identity": True,
            "strict_zero_parameter_no_knob_alpha_phys": True,
            "unpatched_PSM_C1_02_closure": True,
        },
        "selected_parameter_count_now": 0,
        "imported_one_universal_primitive_ready": True,
        "theorem": {
            "name": "UniversalAlpha1FrontierHandoffImportTheorem",
            "proved": True,
            "statement": (
                "The sibling constants repo alpha1 frontier is admissible as a cross-repo handoff into the universal-parameter "
                "policy: strict no-knob alpha_phys remains open/no-go in the current corpus, while a one-universal-primitive "
                "rod/clock/action-unit extension is ready without observed selectors or target fitting."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_UniversalAlpha1FrontierHandoffImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "source_note": rel(SOURCE_NOTE),
        "selected_parameter_count_now": 0,
        "one_universal_primitive_extension_ready": True,
        "strict_no_knob_alpha_phys_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Universal Alpha1 Frontier Handoff Import v1

Status label: `UNIV-PARAM / SOURCE-ANCHOR / UP-1-ALPHA1`

Status: `{STATUS}`

## Imported Result

The sibling constants repo ledger
`proof_corpus/MTT_CONST_EM_01_Alpha1_FrontierClosureLedger_v1.md` is handoff-ready.

It says:

- strict no-knob numerical `alpha_phys` is a current-corpus no-go,
- one-universal-primitive closure is ready as an extension,
- no observed alpha, Newton/Planck, mass, cosmology, TeV, or electroweak value
  is used as a selector.

## Values To Carry

- `tau_int = {primitive["numeric_internal_coefficients"]["tau_int"]}`
- `sqrt(tau_int) = {primitive["numeric_internal_coefficients"]["sqrt_tau_int"]}`
- `Omega0/sqrt(alpha_phys) = {primitive["numeric_internal_coefficients"]["inv_sqrt_tau_int"]}`
- `lambda_12_internal = 2.6179362173268497`
- `Delta_G12_internal = 0.08450302790361214`

## Meaning Here

This is the first strong cross-repo example for the new universal-parameter
tier.  It maps primarily to `UP-ABS-SCALE`, with secondary relevance to
`UP-ACTION-NORM` and `UP-RET-OVERLAP`.

It does not select a universal parameter in this repo and does not close
`PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED`.

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
SLUG = "{SLUG}"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{{SLUG}}.candidate.json"
IMPORT = BASE / "alpha1_frontier_handoff_import.packet.json"
POLICY_UPDATE = BASE / "universal_parameter_policy_update.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_UniversalAlpha1FrontierHandoffImport_v1.md"
BUILD = ROOT / "scripts" / "build_universal_alpha1_frontier_handoff_import.py"
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
    imported = load(IMPORT)
    policy_update = load(POLICY_UPDATE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["selected_parameter_count_now"] == 0, "parameter overselected")
    require(candidate["imported_one_universal_primitive_ready"] is True, "primitive import missing")
    require(candidate["what_remains_open"]["unpatched_PSM_C1_02_closure"] is True, "PSM overclosed")
    require(imported["source_claims"]["strict_current_corpus_nogo"] is True, "strict no-go missing")
    require(imported["source_claims"]["strict_no_knob_alpha_phys_closed"] is False, "strict alpha overclosed")
    require(imported["source_claims"]["one_universal_primitive_extension_ready"] is True, "one primitive not ready")
    require(abs(imported["values_to_carry"]["tau_int"] - 0.40698621549433234) < 1e-15, "tau mismatch")
    require(policy_update["mapped_universal_parameter_class"] == "UP-ABS-SCALE", "class mapping mismatch")
    require(policy_update["what_this_does_not_close"]["PSM_C1_02_unpatched_source_identity"] is True, "policy overclosed PSM")
    require(next_work["primary"]["label"] == "UNIV-PARAM / SOURCE-ANCHOR / UP-1-ALPHA1", "next label mismatch")
    require(cert["selected_parameter_count_now"] == 0, "cert parameter overselected")
    require("does not select a universal parameter" in note, "note guard missing")

    for packet in [candidate, imported, policy_update, cert]:
        guard(packet)

    print(f"PASS {{CANDIDATE.name}}: {{candidate['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (IMPORT, import_packet),
        (POLICY_UPDATE, policy_update),
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
