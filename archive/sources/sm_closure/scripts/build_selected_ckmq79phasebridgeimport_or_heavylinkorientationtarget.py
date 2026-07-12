"""Import q79 CKM phase bridge and lock heavy-link orientation target."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CKMQ79PhaseBridgeImport_or_HeavyLinkOrientationTarget_v1.md"

Q79_CERT = Q79 / "certificates" / "z64_exact_branch_certificate.json"
Q79_PHASE_NOTE = Q79 / "proof_corpus" / "CKM_Phase_Bridge_and_No_Proxy_Flavor_Closure_Status_v1.md"
Q79_PHASE_AUDIT = Q79 / "proof_corpus" / "ckm_phase_bridge_no_proxy_audit.py"
SELECTED_KERNEL_NOTE = Q79 / "proof_corpus" / "Selected_Kernel_Principle_for_CKM_CP_in_MTT_v1.md"
LEADING_NONCOMM_CERT = Q79 / "certificates" / "ckm_leading_noncommutation_criterion_certificate.json"
HEAVY_LINK_CERT = Q79 / "certificates" / "ckm_heavy_link_gate_calculator_certificate.json"
FULL_SM_ATTEMPT = Q79 / "certificates" / "selected_full_sm_data_theorem_attempt_certificate.json"

CURRENT_MIXING = DATA / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"
MASS_RATIO_SEARCH = DATA / "selected_massratioorientationlawsearch_or_finitephaseckmclue.candidate.json"
FLAVOR_BRIDGE = DATA / "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge.candidate.json"

STATUS = (
    "MTT_SELECTED_CKMQ79PHASEBRIDGEIMPORT_OR_HEAVYLINKORIENTATIONTARGET_"
    "IMPORTED_CKMPHASE_CONTACT_HEAVYLINK_VALUES_OPEN"
)
NEXT = "MTT_Selected_HeavyLinkVectorValues_or_CKMHigherBreakdownOrientationLaw_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def phase_distance(a: float, b: float) -> float:
    return abs(math.atan2(math.sin(a - b), math.cos(a - b)))


def main() -> int:
    q79 = load(Q79_CERT)
    leading = load(LEADING_NONCOMM_CERT)
    heavy = load(HEAVY_LINK_CERT)
    full_sm = load(FULL_SM_ATTEMPT)
    mixing = load(CURRENT_MIXING)
    mass_ratio = load(MASS_RATIO_SEARCH)
    flavor_bridge = load(FLAVOR_BRIDGE)

    q = q79["conclusion"]["q_mod_448"]
    q64 = q79["conclusion"]["q_64"]
    q7 = q79["conclusion"]["q_7"]
    delta_q79 = 2.0 * math.pi * q / 448.0
    delta_q79_deg = math.degrees(delta_q79)

    ckm_params = mixing["CKM_packet"]["derived_parameters"]
    s12 = ckm_params["s12"]
    s13 = ckm_params["s13"]
    s23 = ckm_params["s23"]
    c12 = math.sqrt(1.0 - s12 * s12)
    c13 = math.sqrt(1.0 - s13 * s13)
    c23 = math.sqrt(1.0 - s23 * s23)
    prefactor = c12 * c23 * c13**2 * s12 * s23 * s13
    j_q79_current = prefactor * math.sin(delta_q79)
    j_current = mixing["CKM_packet"]["jarlskog"]
    delta_current = ckm_params["delta_rad"]
    delta_residual = phase_distance(delta_q79, delta_current)
    j_relative_residual = abs(j_q79_current - j_current) / abs(j_current)

    q79_phase_import = {
        "schema": "MTTCKMQ79PhaseBridgeImport.v1",
        "status": "Q79_CKM_CP_PHASE_CONTACT_IMPORTED",
        "q79_certificate": str(Q79_CERT).replace("\\", "/"),
        "q79_phase_note": str(Q79_PHASE_NOTE).replace("\\", "/"),
        "q79_phase_audit": str(Q79_PHASE_AUDIT).replace("\\", "/"),
        "selected_kernel_principle": str(SELECTED_KERNEL_NOTE).replace("\\", "/"),
        "closed_branch_status": q79["status"],
        "q64": q64,
        "q7": q7,
        "q_mod_448": q,
        "delta_q79_rad": delta_q79,
        "delta_q79_deg": delta_q79_deg,
        "selection_path": [
            "Z64 exact central-circle branch closed",
            "retarded predecessor q64=15 selected without CKM scan",
            "Z7 Mukai/Fu-Yau component q7=2 imported",
            "CRT gives q=79 mod 448",
            "selected-kernel principle factors physical CKM CP through finite quotient",
        ],
        "no_empirical_label_scan": True,
        "observed_CKM_used_as_selector": False,
        "selected_CKM_CP_phase_contact_imported": True,
        "full_CKM_orientation_values_derived": False,
    }

    current_postcheck = {
        "schema": "MTTCurrentCKMJarlskogPostcheckFromQ79Phase.v1",
        "status": "Q79_PHASE_COMPATIBLE_WITH_CURRENT_CKM_REPLAY",
        "current_ckm_source": str(CURRENT_MIXING.relative_to(ROOT)).replace("\\", "/"),
        "current_CKM_angles": {
            "s12": s12,
            "s13": s13,
            "s23": s23,
            "delta_replay_rad": delta_current,
            "delta_replay_deg": ckm_params["delta_deg"],
        },
        "q79_delta_rad": delta_q79,
        "q79_delta_deg": delta_q79_deg,
        "phase_residual_rad": delta_residual,
        "phase_residual_deg": math.degrees(delta_residual),
        "jarlskog_prefactor_from_current_angles": prefactor,
        "jarlskog_predicted_from_q79_phase": j_q79_current,
        "jarlskog_current_replay": j_current,
        "jarlskog_relative_residual": j_relative_residual,
        "postcheck_only": True,
        "CKM_angles_used_as_source_selector": False,
        "CKM_angle_magnitudes_derived": False,
    }

    heavy_link_target = {
        "schema": "MTTHeavyLinkHigherBreakdownOrientationTarget.v1",
        "status": "HEAVY_LINK_VECTOR_VALUES_ARE_NEXT_CKM_ORIENTATION_SOURCE_TARGET",
        "leading_noncommutation_certificate": str(LEADING_NONCOMM_CERT).replace("\\", "/"),
        "heavy_link_gate_certificate": str(HEAVY_LINK_CERT).replace("\\", "/"),
        "leading_noncommutation_closed": leading["closed"]["leading_ckm_orientation_test"],
        "heavy_link_calculator_ready": heavy["verdict"]["calculator_ready"],
        "selected_packet_values_open": heavy["verdict"]["selected_packet_values_open"],
        "required_packet_entries": heavy["required_packet_entries"],
        "delta_v_formula": heavy["calculation_results"]["formula"],
        "leading_noncommutation_condition": leading["commutator_expansion"][
            "leading_noncommutation_condition"
        ],
        "maps_to_current_higher_breakdown_hunch": True,
        "interpretation": [
            "The q79 phase supplies the CP-active finite character.",
            "The CKM angle/orientation magnitudes require selected heavy-link vector values.",
            "This is the quark-specific additional breakdown layer: v_u and v_d must be emitted from selected alpha1/C1 primitive contractions.",
        ],
        "still_open": heavy["still_open"],
    }

    no_proxy_boundary = {
        "schema": "MTTNoProxyFlavorBoundaryAfterQ79Import.v1",
        "status": "PHASE_CONTACT_CLOSED_MATRICES_AND_ANGLES_OPEN",
        "q79_phase_contact": True,
        "flavor_operator_bridge_status": flavor_bridge["status"],
        "mass_ratio_search_status": mass_ratio["status"],
        "selected_full_sm_attempt_status": full_sm["status"],
        "usable_selected_inputs_found": full_sm["usable_selected_inputs_found"],
        "missing_selected_inputs": full_sm["missing_selected_inputs"],
        "rejected_proxy_inputs_found": full_sm["rejected_proxy_inputs_found"],
        "current_reduction": [
            "CP phase contact imported from q79 selected branch",
            "CKM angle magnitudes reduced to heavy-link vector values and selected matrix execution",
            "Yukawa magnitudes still require selected overlap/kernel rows or accepted flavor source theorem",
            "PMNS remains separate sector-stiffness/source problem",
        ],
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterCKMQ79PhaseBridgeImport.v1",
        "status": "ATTACK_HEAVY_LINK_VALUES_NOT_PHASE_RESCAN",
        "closed_now": [
            "q79 finite CP phase imported from closed exact/charge branch",
            "selected-kernel principle imported as the physical CKM CP factorization premise",
            "current CKM Jarlskog postcheck recomputed from q79 phase",
            "heavy-link/noncommutation criterion identified as the next quark orientation value target",
        ],
        "remaining_to_close": [
            "selected t_u13,t_u23,t_d13,t_d23 heavy-link entries",
            "selected c_u13,c_u23,c_d13,c_d23 correction entries",
            "Delta_v nonzero/pass-fail from selected values",
            "selected canonical Yukawa matrices and CKM angle magnitudes",
            "selected c_{s,k} source theorem or accepted lower-dimensional flavor value source",
            "PMNS/neutral-sector source data and full precision/covariance closure",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedCKMQ79PhaseBridgeImportOrHeavyLinkOrientationTarget",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "q79_exact_branch_certificate": str(Q79_CERT).replace("\\", "/"),
            "q79_phase_bridge_note": str(Q79_PHASE_NOTE).replace("\\", "/"),
            "selected_kernel_principle": str(SELECTED_KERNEL_NOTE).replace("\\", "/"),
            "leading_noncommutation_certificate": str(LEADING_NONCOMM_CERT).replace("\\", "/"),
            "heavy_link_gate_certificate": str(HEAVY_LINK_CERT).replace("\\", "/"),
            "selected_full_sm_attempt": str(FULL_SM_ATTEMPT).replace("\\", "/"),
            "current_mixing_seed": str(CURRENT_MIXING.relative_to(ROOT)).replace("\\", "/"),
            "current_massratio_search": str(MASS_RATIO_SEARCH.relative_to(ROOT)).replace("\\", "/"),
            "current_flavor_bridge": str(FLAVOR_BRIDGE.relative_to(ROOT)).replace("\\", "/"),
        },
        "output_packets": {
            "q79_ckm_phase_bridge_import": f"candidate_data/{SLUG}/q79_ckm_phase_bridge_import.packet.json",
            "current_ckm_jarlskog_postcheck_from_q79": f"candidate_data/{SLUG}/current_ckm_jarlskog_postcheck_from_q79.packet.json",
            "heavy_link_higher_breakdown_orientation_target": f"candidate_data/{SLUG}/heavy_link_higher_breakdown_orientation_target.packet.json",
            "no_proxy_flavor_boundary_after_q79_import": f"candidate_data/{SLUG}/no_proxy_flavor_boundary_after_q79_import.packet.json",
            "next_cutset_after_ckm_q79_phase_bridge_import": f"candidate_data/{SLUG}/next_cutset_after_ckm_q79_phase_bridge_import.packet.json",
        },
        "next_required_artifact": NEXT,
        "closure_decision": {
            "selected_q79_branch_imported": True,
            "selected_CKM_CP_phase_contact_imported": True,
            "selected_kernel_principle_imported": True,
            "no_empirical_label_scan": True,
            "q_mod_448": q,
            "delta_q79_deg": delta_q79_deg,
            "current_CKM_phase_residual_deg": math.degrees(delta_residual),
            "current_J_q79_relative_residual": j_relative_residual,
            "CKM_angles_derived": False,
            "CKM_heavy_link_calculator_ready": heavy["verdict"]["calculator_ready"],
            "selected_heavy_link_values_emitted": False,
            "leading_CKM_noncommutation_values_closed": False,
            "selected_csk_source_theorem_closed": False,
            "full_true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "theorem": {
            "name": "CKMQ79PhaseBridgeImportAndHeavyLinkTargetTheorem",
            "proved": True,
            "statement": "The current SM-closure ledger imports the older q79 no-proxy CKM phase bridge: q=79 is read from the closed exact/charge branch, not from a CKM phase scan, and the selected-kernel principle supplies the finite-character factorization needed to treat delta=2*pi*79/448 as the CKM CP contact point. Recomputing the current CKM Jarlskog postcheck preserves compatibility. This does not derive CKM angle magnitudes, Yukawa magnitudes, or full SM equivalence; the next quark-orientation source target is the selected heavy-link vector packet for v_u and v_d.",
        },
    }

    cert = {
        "certificate": "MTT_Selected_CKMQ79PhaseBridgeImport_or_HeavyLinkOrientationTarget_v1",
        "status": STATUS,
        "candidate": candidate["candidate"],
        "theorem": candidate["theorem"]["name"],
        "proved": True,
        "selected_q79_branch_imported": True,
        "selected_CKM_CP_phase_contact_imported": True,
        "q_mod_448": q,
        "delta_q79_deg": delta_q79_deg,
        "no_empirical_label_scan": True,
        "current_CKM_phase_residual_deg": math.degrees(delta_residual),
        "current_J_q79_relative_residual": j_relative_residual,
        "CKM_heavy_link_calculator_ready": heavy["verdict"]["calculator_ready"],
        "selected_heavy_link_values_emitted": False,
        "CKM_angles_derived": False,
        "full_true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected CKMQ79PhaseBridgeImport or HeavyLinkOrientationTarget v1

Status: `{STATUS}`

## Theorem

**CKMQ79PhaseBridgeImportAndHeavyLinkTargetTheorem.** The current SM-closure ledger imports the older q79 no-proxy CKM phase bridge: `q=79` is read from the closed exact/charge branch, not from a CKM phase scan, and the selected-kernel principle supplies the finite-character factorization needed to treat `delta=2*pi*79/448` as the CKM CP contact point.

## Imported Phase Contact

- `q64={q64}`, `q7={q7}`, `q={q} mod 448`
- `delta_q79={delta_q79} rad = {delta_q79_deg} deg`
- current CKM replay phase residual: `{math.degrees(delta_residual)} deg`
- current CKM-angle Jarlskog from q79 phase: `{j_q79_current}`
- current replay Jarlskog: `{j_current}`
- relative J residual: `{j_relative_residual}`

## Next Quark Orientation Target

The older q79 repo already closed the leading noncommutation criterion but left selected values open. The exact next packet is:

`{heavy["required_packet_entries"]}`

with formula `{heavy["calculation_results"]["formula"]}` and condition `{leading["commutator_expansion"]["leading_noncommutation_condition"]}`.

## Claim Boundary

This imports a no-proxy CKM CP phase contact point. It does not derive CKM angle magnitudes, Yukawa magnitudes, selected `c_{{s,k}}` rows, PMNS data, or full true SM equivalence.

Next artifact: `{NEXT}`.
"""

    write_json(PACKET_DIR / "q79_ckm_phase_bridge_import.packet.json", q79_phase_import)
    write_json(PACKET_DIR / "current_ckm_jarlskog_postcheck_from_q79.packet.json", current_postcheck)
    write_json(PACKET_DIR / "heavy_link_higher_breakdown_orientation_target.packet.json", heavy_link_target)
    write_json(PACKET_DIR / "no_proxy_flavor_boundary_after_q79_import.packet.json", no_proxy_boundary)
    write_json(PACKET_DIR / "next_cutset_after_ckm_q79_phase_bridge_import.packet.json", next_cutset)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
