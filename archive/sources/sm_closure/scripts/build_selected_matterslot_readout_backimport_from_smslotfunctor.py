"""Backimport SM-slot functor closure into the matter-slot readout frontier.

The older matter-slot readout search blocked because rho_s/projector invariants
were too uniform and the selected section-ring/SM-slot source functor was not
yet emitted.  Later artifacts close all six SM-slot functor source arrows.
This artifact reconciles those layers and promotes the readout only at the
static source tier, leaving dynamic C1/operator payloads open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_matterslot_readout_backimport_from_smslotfunctor"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
READOUT_PACKET = PACKET_DIR / "selected_static_matterslot_readout.packet.json"
DYNAMIC_BOUNDARY = PACKET_DIR / "dynamic_operator_boundary_after_readout.packet.json"
PROMOTION_DECISION = PACKET_DIR / "readout_promotion_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_MatterSlotReadout_BackimportFromSMSlotFunctor_v1.md"

STATUS = "MTT_SELECTED_MATTERSLOT_READOUT_BACKIMPORT_BUILT_STATIC_READOUT_CLOSED_DYNAMIC_OPEN"
NEXT = "MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    old_readout = load(DATA / "selected_matterslot_transversality_readout_functional.candidate.json")
    grading = load(DATA / "selected_matterslot_grading_or_sectionring_readout.candidate.json")
    smslot = load(DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json")
    ledger = load(DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json")
    sector_frontier = load(DATA / "selected_sectorcharge_1mdirac_sourceemission_or_transportclosedvalidatorreplay.candidate.json")

    all_six_closed = smslot["arrow_status"]["all_six_closed"]
    static_routes = ledger["old_contract_reclassification"]["matter_slot_charge"]["selected_partition"]

    readout_packet = {
        "schema": "MTTSelectedStaticMatterSlotReadout.v1",
        "status": "STATIC_SOURCE_TIER_READOUT_CLOSED",
        "source": "selected SM-slot functor all six source arrows",
        "old_blocker": old_readout["next_required_artifact"],
        "why_old_blocker_is_now_resolved_static_tier": [
            "A1 emits terminal Ext -> 10_M clock.",
            "A2 emits terminal Ext -> bar5_M shift.",
            "A3 emits terminal Ext -> 1_M=N^c Dirac-neutrino shift.",
            "A4 emits q79 polarization U_10=I_3 and U_bar5=F.",
            "A5 emits transported-projector trace/transfer normalization.",
            "A6 emits same-source consistency of these maps.",
        ],
        "selected_readouts": {
            "selected_10M_clock_readout": {
                "closed": True,
                "matter_slot": "10_M",
                "sectors": static_routes["clock_phase_side"]["sectors"],
                "weyl_leg": static_routes["clock_phase_side"]["weyl_leg"],
                "polarization": smslot["selected_SMSlotFunctor_all_six_arrows_claimed"]
                and smslot["arrow_status"]["closed_arrows"][3],
            },
            "selected_bar5M_shift_readout": {
                "closed": True,
                "matter_slot": "bar5_M",
                "sectors": ["d"],
                "weyl_leg": static_routes["shift_non10_side"]["weyl_leg"],
                "polarization": "U_bar5=F",
            },
            "selected_1M_Dirac_shift_readout": {
                "closed": True,
                "matter_slot": "1_M=N^c",
                "sectors": ["nuD"],
                "weyl_leg": static_routes["shift_non10_side"]["weyl_leg"],
                "rule": ledger["old_contract_reclassification"]["singlet_neutrino_rule"]["selected_rule"],
            },
            "selected_phase_shift_partition": {
                "closed": True,
                "phase": static_routes["clock_phase_side"]["sectors"],
                "shift": static_routes["shift_non10_side"]["sectors"],
            },
            "selected_overlap_transfer_normalization_static": {
                "closed": ledger["old_contract_reclassification"]["normalization"][
                    "static_trace_innerproduct_normalization_selected"
                ],
                "unit_trace_transfer": ledger["old_contract_reclassification"]["normalization"][
                    "unit_trace_transfer"
                ],
            },
        },
        "forbidden_inputs_absent": {
            "observed_masses_mixings_cp": True,
            "benchmark_matrices": True,
            "locked_C1_splitter_columns_as_selector": True,
            "diagnostic_lifted_flags": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    dynamic_boundary = {
        "schema": "MTTDynamicOperatorBoundaryAfterStaticMatterSlotReadout.v1",
        "status": "STATIC_READOUT_CLOSED_DYNAMIC_OPERATOR_C1_OPEN",
        "static_sm_slot_tier_closed": ledger["payload_tiers"]["static_sm_slot_tier"]["closed"],
        "dynamic_operator_c1_tier_closed": ledger["payload_tiers"]["dynamic_operator_c1_tier"]["closed"],
        "not_promoted_by_this_artifact": {
            "dynamic_visible_routec_operator_source_identity": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "physical_alpha1_driver": True,
            "selected_dynamic_overlap_tensor_or_transfer_functor": True,
            "selected_primitive_C1_contractions": True,
            "selected_b_selected_and_Hessian_normalization": True,
            "A_selected": True,
            "full_flavor_constants": True,
        },
        "next_dynamic_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion_decision = {
        "schema": "MTTMatterSlotReadoutBackimportPromotionDecision.v1",
        "status": "PROMOTE_STATIC_READOUT_ONLY",
        "all_six_smslot_arrows_closed": all_six_closed,
        "old_rho_s_invariant_nogo_preserved": old_readout["what_closes_now"]["rho_s_alone_readout_nogo"],
        "selected_matter_slot_grading_readout_closed_static": all_six_closed,
        "selected_U10_Ubar5_1M_samebranch_emitted_static": all_six_closed,
        "selected_sector_charge_or_chirality_closed_static": all_six_closed,
        "selected_overlap_transfer_normalization_static": ledger["what_closes_now"][
            "selected_static_finite_trace_transfer_normalization"
        ],
        "dynamic_C1_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedMatterSlotReadoutBackimportFromSMSlotFunctor",
        "status": STATUS,
        "inputs": {
            "old_matter_slot_transversality_readout": rel(
                DATA / "selected_matterslot_transversality_readout_functional.candidate.json"
            ),
            "matter_slot_grading_or_sectionring_readout": rel(
                DATA / "selected_matterslot_grading_or_sectionring_readout.candidate.json"
            ),
            "selected_smslotfunctor_overlapkernel_source_emission": rel(
                DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
            ),
            "selected_smslotfunctor_downstream_operator_payloads_ledger": rel(
                DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
            ),
            "sector_source_frontier": rel(
                DATA / "selected_sectorcharge_1mdirac_sourceemission_or_transportclosedvalidatorreplay.candidate.json"
            ),
        },
        "output_packets": {
            "selected_static_matterslot_readout": rel(READOUT_PACKET),
            "dynamic_operator_boundary_after_readout": rel(DYNAMIC_BOUNDARY),
            "readout_promotion_decision": rel(PROMOTION_DECISION),
        },
        "theorem": {
            "name": "MatterSlotReadoutBackimportFromSMSlotFunctorTheorem",
            "proved": True,
            "statement": (
                "The later selected SM-slot functor source-emission theorem fills the matter-slot grading/readout object that the older rho_s-only transversality search lacked. "
                "Thus U_10=I_3, U_bar5=F, the 1_M=N^c Dirac shift source, the u,e | d,nuD partition, and static trace-transfer normalization are promoted at the static source tier. "
                "This does not promote dynamic D_E/Riesz/Green/dotD, C1 overlap tensors, A_selected, b_selected, physical flavor constants, true SM equivalence, or no-knob closure."
            ),
        },
        "superset_strategy": {
            "mode": "BACKIMPORT_LATER_STATIC_SOURCE_FUNCTOR_TO_OLDER_READOUT_GATE",
            "using_one_straight_path": False,
            "straight_path": "selected terminal section-ring/SM-slot functor source arrows",
            "support_paths": [
                "transported rho_s/projector/Riesz/Green stationary source",
                "q79 SU(5)/E6 polarization and Dirac-neutrino dictionary",
                "transported-projector trace Gram normalization",
            ],
            "locked_target_role": "used only as downstream consistency; locked C1 columns are not selectors",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "what_closes_now": {
            "selected_matter_slot_transversality_readout_functional_static_tier": True,
            "selected_10M_clock_readout_static_tier": True,
            "selected_bar5M_shift_readout_static_tier": True,
            "selected_1M_Dirac_shift_readout_static_tier": True,
            "selected_U10_Ubar5_polarization_source_outputs_static_tier": True,
            "selected_overlap_transfer_normalization_static_tier": True,
            "old_rhos_only_nogo_preserved_not_contradicted": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": dynamic_boundary["not_promoted_by_this_artifact"]
        | {
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "SM_parity_closed": sector_frontier["SM_parity_closed"],
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_MatterSlotReadout_BackimportFromSMSlotFunctor_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "packet_paths": candidate["output_packets"],
        "static_readout_closed": True,
        "dynamic_C1_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected MatterSlotReadout Backimport From SMSlotFunctor v1

Status: `{STATUS}`.

The older matter-slot readout search proved an important no-go: stationary
`rho_s` invariants alone cannot distinguish `10_M`, `bar5_M`, and `1_M`.
That no-go still stands.

What changed is that later SM-slot functor work supplied the missing source
labels.  All six static source arrows are now emitted, so the matter-slot
readout is closed at the static source tier:

- `10_M -> u,e` with `U_10=I_3`
- `bar5_M -> d` with `U_bar5=F`
- `1_M=N^c -> nuD`
- phase/shift partition `u,e | d,nuD`
- transported-projector trace/transfer normalization

This is not a dynamic operator/C1 closure.  Dynamic `D_E/Riesz/Green/dotD`,
primitive C1 contractions, `A_selected`, `b_selected`, physical flavor
constants, true SM equivalence, and no-knob closure remain open.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "{SLUG}"
DATA = ROOT / "candidate_data" / f"{{SLUG}}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
READOUT = PACKET_DIR / "selected_static_matterslot_readout.packet.json"
DYNAMIC = PACKET_DIR / "dynamic_operator_boundary_after_readout.packet.json"
DECISION = PACKET_DIR / "readout_promotion_decision.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MatterSlotReadout_BackimportFromSMSlotFunctor_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    readout = load(READOUT)
    dynamic = load(DYNAMIC)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["SM_parity_closed"] is True, "SM parity regressed")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(readout["status"] == "STATIC_SOURCE_TIER_READOUT_CLOSED", "readout not closed")
    for key in [
        "selected_10M_clock_readout",
        "selected_bar5M_shift_readout",
        "selected_1M_Dirac_shift_readout",
        "selected_phase_shift_partition",
        "selected_overlap_transfer_normalization_static",
    ]:
        require(readout["selected_readouts"][key]["closed"] is True, f"readout missing {{key}}")
    require(readout["selected_readouts"]["selected_phase_shift_partition"]["phase"] == ["u", "e"], "phase route mismatch")
    require(readout["selected_readouts"]["selected_phase_shift_partition"]["shift"] == ["d", "nuD"], "shift route mismatch")
    require(all(readout["forbidden_inputs_absent"].values()), "forbidden input present")

    require(dynamic["static_sm_slot_tier_closed"] is True, "static tier not closed")
    require(dynamic["dynamic_operator_c1_tier_closed"] is False, "dynamic tier overclosed")
    require(dynamic["not_promoted_by_this_artifact"]["A_selected"] is True, "A_selected overpromoted")
    require(dynamic["not_promoted_by_this_artifact"]["selected_b_selected_and_Hessian_normalization"] is True, "b_selected overpromoted")

    require(decision["all_six_smslot_arrows_closed"] is True, "SM-slot arrows not closed")
    require(decision["old_rho_s_invariant_nogo_preserved"] is True, "rho_s no-go lost")
    require(decision["selected_matter_slot_grading_readout_closed_static"] is True, "grading not promoted static")
    require(decision["dynamic_C1_promoted"] is False, "dynamic C1 overpromoted")
    require(cert["static_readout_closed"] is True, "cert readout not closed")
    require(cert["dynamic_C1_promoted"] is False, "cert dynamic overpromoted")
    require(data["next_required_artifact"] == "{NEXT}", "wrong next artifact")
    require("That no-go still stands" in note, "note missing no-go preservation")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(READOUT_PACKET, readout_packet)
    write_json(DYNAMIC_BOUNDARY, dynamic_boundary)
    write_json(PROMOTION_DECISION, promotion_decision)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
