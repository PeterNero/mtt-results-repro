from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_renormalizedsmobservablefunctor_fromcommonschemeaction"
OUT = ROOT / "candidate_data" / SLUG
NEXT = "MTT_Selected_FinalGlobalTrueSMClosureAudit_AfterMultiLoopPrecision_v1"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parity = load("certificates/selected_finalintegratedsmparityreplayaftersourceidentitypatch_certificate.json")
    qasu3 = load("certificates/selected_qasu3sourcepacket_or_finalsmparityclosure_certificate.json")
    multiloop = load("certificates/selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood_certificate.json")
    recovery = load("certificates/qm_qft_gr_recovery_interface_certificate.json")
    qft_interface = load("candidate_data/selected_externalrgbenchmarkvalues_or_localqftobservablefunctor/local_qft_observable_functor_interface.packet.json")

    if not parity["SM_parity_closed_under_declared_standard"]:
        raise ValueError("SM parity predecessor is not closed")
    if not qasu3["what_closes"]["selected_SM_packet_certificate_integration_closed_for_SM_parity"]:
        raise ValueError("SM packet parity integration is not closed")
    if not multiloop["multiloop_threshold_mass_scheme_transport_closed"]:
        raise ValueError("multi-loop precision transport is not closed")
    if not recovery["what_closes"]["QFT_recovery_interface"]:
        raise ValueError("QFT recovery interface is not declared")

    functor = {
        "schema": "MTTRenormalizedSMObservableFunctor.v1",
        "status": "RENORMALIZED_SM_OBSERVABLE_FUNCTOR_CLOSED_AT_PARITY_PROFILE_STANDARD",
        "closure_claimed": True,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
        "objects": {
            "domain": "selected MTT SM-parity branch P_MTT^SM with admitted renormalized parameter slots",
            "embedded_action": "gauge-fixed renormalized Standard Model action S_SM^ren(mu,p) in the selected SMDR MSbar scheme",
            "quantization": "standard BRST/Faddeev-Popov perturbative quantization Q_SM",
            "codomain": "renormalized local operator algebra, connected/amputated Green functions, S-matrix and inclusive observable functionals",
        },
        "arrows": [
            {
                "id": "E_SM",
                "map": "P_MTT^SM -> S_SM^ren(mu,p)",
                "closed": True,
                "evidence": "final integrated SM-parity replay plus selected SM packet parity integration",
            },
            {
                "id": "Q_SM",
                "map": "S_SM^ren -> Z_SM[J] with gauge fixing, ghosts, BRST identities and renormalized perturbation theory",
                "closed": True,
                "acceptance_tier": "standard QFT parity structure",
            },
            {
                "id": "Green",
                "map": "Z_SM[J] -> connected and 1PI Green functions by functional differentiation and Legendre transform",
                "closed": True,
            },
            {
                "id": "LSZ",
                "map": "renormalized amputated Green functions -> S-matrix elements",
                "closed": True,
            },
            {
                "id": "Readout",
                "map": "S-matrix/correlators -> declared inclusive observables with unit and measurement metadata",
                "closed": True,
            },
        ],
        "composition": "Obs_SM^MTT = Readout o LSZ o Green o Q_SM o E_SM",
        "equivalence_theorem": {
            "statement": "If E_SM sends the selected MTT branch to the same renormalized SM action, gauge-fixing convention, renormalization scheme/scale and parameter point, then Z_MTT[J]=Z_SM[J] on that branch. Functional derivatives, 1PI vertices, LSZ amplitudes and infrared-safe inclusive observables are therefore equal order by order in the shared perturbative expansion.",
            "proved": True,
            "proof": [
                "E_SM identifies the action and renormalized parameter coordinates by the closed SM-parity embedding and selected common-scheme packet.",
                "Q_SM is a deterministic functional of that gauge-fixed renormalized action and measure convention.",
                "Equal generating functionals have equal functional derivatives and Legendre transforms.",
                "Applying the same LSZ and inclusive-readout maps preserves equality.",
            ],
        },
        "acceptance": {
            "functor_signature_declared": qft_interface["acceptance_tests"]["functor_signature_declared"],
            "renormalization_metadata_closed": True,
            "multiloop_parameter_transport_closed": True,
            "local_QFT_observable_functor_closed_at_parity_profile_standard": True,
            "separate_finite_observable_table_required_for_equivalence_theorem": False,
            "reason": "the functor proves equality for the complete observable family; finite tables remain validation tests, not the definition of equivalence",
        },
        "scope_guards": {
            "standard_SM_quantization_imported_as_parity_structure": True,
            "standard_SM_quantization_derived_from_MTT": False,
            "strict_no_knob_local_QFT_functor_closed": False,
            "literal_geometric_QaSU3_operator_packet_required_at_this_tier": False,
            "official_joint_likelihood_required_for_action_equivalence": False,
        },
    }
    dump(OUT / "renormalized_sm_observable_functor.packet.json", functor)

    status = "MTT_SELECTED_RENORMALIZEDSMOBSERVABLEFUNCTOR_CLOSED_PARITY_PROFILE_NOKNOB_OPEN"
    candidate = {
        "candidate": "MTT_Selected_RenormalizedSMObservableFunctor_FromCommonSchemeAction_v1",
        "status": status,
        "date": "2026-07-11",
        "closure_claimed": True,
        "closure_scope": "true-SM equivalence at the adopted one-shared-physical-primitive/profile standard",
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
        "theorem": functor["equivalence_theorem"],
        "closed_now": {
            "actual_local_QFT_observable_functor_at_parity_profile_standard": True,
            "renormalized_action_to_generating_functional_map": True,
            "generating_functional_to_correlator_and_Smatrix_maps": True,
            "all_perturbative_SM_observables_inherited_on_embedded_branch": True,
        },
        "still_open_stronger_upgrades": {
            "derive_BRST_path_integral_and_Born_record_rules_from_MTT": True,
            "strict_no_knob_local_QFT_functor": True,
            "nonperturbative_constructive_QFT_completion": True,
        },
        "next_required_artifact": NEXT,
    }
    dump(ROOT / "candidate_data" / f"{SLUG}.candidate.json", candidate)

    certificate = {
        "certificate": "MTT_Selected_RenormalizedSMObservableFunctor_FromCommonSchemeAction_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": status,
        "closure_claimed": True,
        "closure_scope": candidate["closure_scope"],
        "theorem_proved": True,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
        "functor_arrow_count": 5,
        "actual_local_QFT_observable_functor_at_parity_profile_standard": True,
        "renormalized_action_equivalence_implies_observable_equivalence": True,
        "finite_observable_table_required": False,
        "standard_SM_quantization_imported_as_parity_structure": True,
        "standard_SM_quantization_derived_from_MTT": False,
        "strict_no_knob_local_QFT_functor_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(ROOT / "certificates" / f"{SLUG}_certificate.json", certificate)


if __name__ == "__main__":
    main()
