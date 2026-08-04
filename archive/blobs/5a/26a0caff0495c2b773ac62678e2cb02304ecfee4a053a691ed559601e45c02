"""Build the measured-parameter replay manifest for SM-equivalence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

ADMISSION = DATA / "sm_equivalence_measured_replay_admission.candidate.json"
CORE = DATA / "core_axioms_measured_parameter_interface.candidate.json"
SECTOR = DATA / "sm_sector_embedding_interface.candidate.json"
EMPIRICAL = DATA / "empirical_equivalence_ledger.candidate.json"
SMSLOT = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"

OUTPUT = DATA / "sm_equivalence_measured_parameter_replay_manifest.candidate.json"
CERT = CERTS / "sm_equivalence_measured_parameter_replay_manifest_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_Measured_Parameter_Replay_Manifest_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_MEASURED_PARAMETER_REPLAY_MANIFEST_BUILT_VALUES_OPEN"
NEXT = "MTT_SM_Equivalence_Reference_Data_Packet_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def manifest_slot(
    *,
    slot_id: str,
    sector: str,
    parameter_class: str,
    value_shape: str,
    conventions: list[str],
    replay_targets: list[str],
    no_knob_upgrade_target: str,
    parity_scope: str = "SM_EQUIVALENCE",
) -> dict[str, Any]:
    return {
        "slot_id": slot_id,
        "sector": sector,
        "parameter_class": parameter_class,
        "parity_scope": parity_scope,
        "value_status": "MEASURED_VALUE_NOT_FILLED_IN_THIS_MANIFEST",
        "value_shape": value_shape,
        "required_reference_fields": [
            "source_name",
            "source_version_or_date",
            "observable_definition",
            "central_value",
            "uncertainty",
            "units",
            "scheme",
            "scale",
            "correlation_policy",
        ],
        "required_conventions": conventions,
        "allowed_replay_targets": replay_targets,
        "forbidden_uses": [
            "source selection",
            "branch or topology selection",
            "operator-packet selection",
            "post-hoc residual fitting",
            "promotion to no-knob derivation",
        ],
        "no_knob_upgrade_target": no_knob_upgrade_target,
    }


def main() -> int:
    admission = load(ADMISSION)
    core = load(CORE)
    sector = load(SECTOR)
    empirical = load(EMPIRICAL)
    smslot = load(SMSLOT)

    measured_admission_closed = admission["what_closes_now"][
        "SM_equivalence_measured_replay_admission_policy"
    ]
    static_boundary_closed = all(admission["static_source_boundary"].values())

    slots = [
        manifest_slot(
            slot_id="gauge.alpha_1_alpha_2_alpha_3",
            sector="SM gauge/QFT",
            parameter_class="MEASURED_PARITY_INPUT",
            value_shape="three running gauge couplings or equivalent inverse couplings",
            conventions=["renormalization scheme", "reference scale", "normalization of U(1)_Y"],
            replay_targets=[
                "gauge-running replay",
                "electroweak mixing convention check",
                "QCD/electroweak comparison after source boundary",
            ],
            no_knob_upgrade_target="selected threshold/local determinant spectra",
        ),
        manifest_slot(
            slot_id="yukawa.Y_u_Y_d_Y_e",
            sector="SM flavor",
            parameter_class="MEASURED_PARITY_INPUT",
            value_shape="three complex 3x3 matrices modulo declared basis and phase convention",
            conventions=["flavor basis", "left/right field convention", "RG scale", "phase convention"],
            replay_targets=[
                "charged fermion mass spectrum",
                "CKM reconstruction from diagonalization",
                "basis-consistency checks against selected SM-slot routing",
            ],
            no_knob_upgrade_target="selected dynamic overlap tensor and primitive C1 contractions",
        ),
        manifest_slot(
            slot_id="mixing.CKM",
            sector="SM quark mixing",
            parameter_class="MEASURED_PARITY_INPUT",
            value_shape="unitary 3x3 matrix or equivalent angles plus CP phase",
            conventions=["PDG-like parameterization or explicit matrix convention", "phase convention"],
            replay_targets=["unitarity checks", "Jarlskog invariant replay", "quark charged-current replay"],
            no_knob_upgrade_target="selected CP-odd complex overlap/operator invariant",
        ),
        manifest_slot(
            slot_id="mixing.PMNS",
            sector="SM plus Dirac-neutrino parity extension",
            parameter_class="MEASURED_PARITY_INPUT",
            value_shape="unitary 3x3 matrix or equivalent angles plus phases",
            conventions=[
                "neutrino mass ordering",
                "Dirac versus Majorana phase policy",
                "phase convention",
            ],
            replay_targets=[
                "lepton mixing replay",
                "Dirac-neutrino route consistency with 1_M=N^c",
            ],
            no_knob_upgrade_target="selected 1_M Dirac-neutrino overlap and CP kernel",
        ),
        manifest_slot(
            slot_id="higgs.v_mh_lambda_or_potential",
            sector="SM Higgs",
            parameter_class="MEASURED_PARITY_INPUT",
            value_shape="vev, Higgs mass, quartic and potential convention, or equivalent parameter set",
            conventions=["unit convention", "potential sign convention", "scheme", "scale"],
            replay_targets=["Higgs-sector replay", "Yukawa-to-mass conversion", "electroweak scale convention check"],
            no_knob_upgrade_target="selected Higgs projector/source and threshold/RG matching",
        ),
        manifest_slot(
            slot_id="neutrino.yukawa_or_mass_splittings",
            sector="SM plus Dirac-neutrino parity extension",
            parameter_class="MEASURED_PARITY_INPUT",
            value_shape="Dirac neutrino Yukawa matrix or masses/splittings with explicit reconstruction policy",
            conventions=["absolute-mass policy", "ordering", "RG scale", "Dirac-neutrino normalization"],
            replay_targets=[
                "nuD mass/mixing replay",
                "1_M=N^c shift-side routing check",
            ],
            no_knob_upgrade_target="selected 1_M sector overlap response",
        ),
    ]

    replay_pipeline = [
        {
            "step": "freeze_selected_source_boundary",
            "status": "READY",
            "inputs": [rel(SMSLOT), rel(SECTOR)],
            "rule": "No measured value may modify the source packet after this step.",
        },
        {
            "step": "load_reference_data_packet",
            "status": "OPEN_NEXT",
            "inputs": [NEXT],
            "rule": "Reference values must be versioned and convention-typed before computation.",
        },
        {
            "step": "run_tree_level_replay",
            "status": "OPEN",
            "inputs": ["Yukawa/Higgs/mixing/gauge slots"],
            "rule": "Replay may compute masses, mixings, invariants, and consistency checks only.",
        },
        {
            "step": "run_rg_and_scheme_replay",
            "status": "OPEN",
            "inputs": ["scheme/scale/correlation metadata"],
            "rule": "RG transport must be declared separately from source selection.",
        },
        {
            "step": "empirical_equivalence_audit",
            "status": "OPEN",
            "inputs": ["computed replay outputs", rel(EMPIRICAL)],
            "rule": "Pass/fail compares observables; it cannot promote a no-knob selector.",
        },
    ]

    candidate = {
        "candidate": "MTTSMEquivalenceMeasuredParameterReplayManifest",
        "status": STATUS,
        "inputs": {
            "measured_replay_admission": rel(ADMISSION),
            "core_axioms_measured_parameter_interface": rel(CORE),
            "sm_sector_embedding_interface": rel(SECTOR),
            "empirical_equivalence_ledger": rel(EMPIRICAL),
            "selected_smslotfunctor_downstream_payload_ledger": rel(SMSLOT),
        },
        "superset_strategy_use": {
            "mode": "SUPERSET_TO_LOCKED_SOURCE_THEN_STRAIGHT_MEASURED_REPLAY",
            "explanation": (
                "Topology, terminal-monad, q79/theta, Qa/SU3, HYM, and dynamic-overlap paths "
                "are combined only to lock the selected source/operator boundary. The measured "
                "parameter replay then proceeds as a straight SM-standard downstream computation."
            ),
            "locked_target": "static SM source/interface boundary plus measured-slot policy",
            "measured_targets_used_to_lock_source": False,
        },
        "preconditions": {
            "measured_admission_closed": measured_admission_closed,
            "static_source_boundary_closed": static_boundary_closed,
            "measured_inputs_do_not_select_sources": core["gate_results"][
                "measured_inputs_do_not_select_sources"
            ],
            "empirical_interfaces_ready": empirical["acceptance_summary"][
                "interfaces_ready_for_empirical_audit"
            ],
            "all_six_static_sm_slot_arrows_closed": smslot["selected_static_payloads_claimed"],
        },
        "slot_manifest": slots,
        "replay_pipeline": replay_pipeline,
        "reference_data_policy": {
            "values_filled_here": False,
            "next_packet_must_freeze_values_before_replay": True,
            "preferred_sources": [
                "current PDG or equivalent particle-data reference",
                "current CODATA or equivalent constants reference where dimensionful anchors enter",
                "explicit experiment/global-fit source for neutrino parameters",
            ],
            "must_record": [
                "edition or retrieval date",
                "scheme and scale",
                "basis and phase convention",
                "uncertainties and correlations where available",
                "conversion formulas used by replay",
            ],
        },
        "acceptance_tests_for_next_packet": [
            "every slot has a versioned reference or is explicitly marked out of scope",
            "all dimensionful slots carry units and conversion policy",
            "all running quantities carry scheme and scale",
            "all matrices carry basis and phase conventions",
            "no reference value is used to alter the selected source boundary",
        ],
        "forbidden_promotions": [
            "measured Yukawa matrix -> selected dynamic overlap tensor",
            "measured CKM/PMNS phase -> selected CP source",
            "measured gauge couplings -> selected threshold kernel",
            "measured masses -> family or representation selector",
            "good replay residual -> no-knob proof",
        ],
        "what_closes_now": {
            "measured_slot_manifest_built": True,
            "SM_equivalence_replay_pipeline_declared": True,
            "reference_data_packet_schema_declared": True,
            "superset_use_limited_to_source_boundary": True,
            "source_selection_guardrails_preserved": True,
        },
        "what_remains_open": {
            "reference_data_packet_values": True,
            "actual_numeric_tree_level_replay": True,
            "RG_scheme_transport_replay": True,
            "empirical_equivalence_audit_run": True,
            "full_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SMEquivalenceMeasuredParameterReplayManifestTheorem",
            "proved": True,
            "statement": (
                "Given the closed measured-replay admission policy and the static SM source boundary, "
                "the listed measured gauge, Yukawa, CKM/PMNS, Higgs, and Dirac-neutrino parity-extension "
                "slots form a typed downstream replay manifest. Filling those slots from versioned external "
                "references can support SM-equivalence calculations, but cannot select source data or count "
                "as no-knob closure."
            ),
        },
    }

    cert = {
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SM-Equivalence Measured Parameter Replay Manifest v1

Status: `{STATUS}`.

## Theorem

`SMEquivalenceMeasuredParameterReplayManifestTheorem` is proved in the local
audit sense: after the selected source/interface boundary is frozen, measured
SM parameters may enter as downstream replay slots.  They cannot select the
source, topology, operator packet, dynamic overlap tensor, or no-knob kernels.

## Superset Use

This is a superset-to-boundary step, followed by a straight replay step.
Topology, terminal-monad, q79/theta, Qa/SU3, HYM, and dynamic-overlap paths are
used only to lock the selected source/operator boundary.  The measured replay
then follows the SM standard.

## Slots

- `gauge.alpha_1_alpha_2_alpha_3`
- `yukawa.Y_u_Y_d_Y_e`
- `mixing.CKM`
- `mixing.PMNS`
- `higgs.v_mh_lambda_or_potential`
- `neutrino.yukawa_or_mass_splittings`

No numeric values are inserted here.  The next artifact, `{NEXT}`, must freeze
versioned reference values, conventions, units, scales, uncertainties, and
correlation policy before any numeric replay is allowed.

## Guardrail

A successful replay is evidence for SM-equivalence only.  It is not a no-knob
derivation unless the selected internal dynamic overlap/threshold/source kernels
are emitted separately.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
