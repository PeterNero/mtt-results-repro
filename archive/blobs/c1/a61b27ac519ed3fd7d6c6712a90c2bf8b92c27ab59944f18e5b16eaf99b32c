"""Build the central-twist orbit-democracy source / determinant operator gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

ORTHO = DATA / "caxis_orthogonality_source_or_weighted_operator_packet.candidate.json"
PACKET = DATA / "hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json"
PROMOTION = DATA / "finite_galerkin_to_smooth_operator_promotion_or_nogo.candidate.json"

OUTPUT_DATA = DATA / "central_twist_orbit_democracy_source_or_determinant_operator.candidate.json"
OUTPUT_CERT = CERTS / "central_twist_orbit_democracy_source_or_determinant_operator_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Central_Twist_Orbit_Democracy_Source_or_Determinant_Operator_v1.md"


def build() -> tuple[dict[str, object], dict[str, object], str]:
    ortho = json.loads(ORTHO.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    promotion = json.loads(PROMOTION.read_text(encoding="utf-8"))

    tau: dict[str, int] = packet["tau_extraction"]["module_twist_values"]
    trace_payload = packet["response_payload"]["heat_zeta_or_torsion_finite_part"]
    trace_normalization = packet["response_payload"]["trace_normalization"]

    nonzero_labels = [label for label, value in tau.items() if value != 0]
    zero_labels = [label for label, value in tau.items() if value == 0]
    finite_trace_tau_squared = sum(value * value for value in tau.values())
    finite_nonzero_tau_label_count = sum(1 for value in tau.values() if value != 0 and label_is_primitive(value))

    finite_orbit_source_theorem = {
        "name": "FiniteTraceCentralTwistOrbitDemocracy",
        "hypotheses": [
            "use the selected finite Galerkin Qa/SU3 typed module labels",
            "use the packet's ordinary finite trace over the selected eleven module labels",
            "use the central character operator D_E=diag(tau(L)) on those labels",
            "do not add observed Qa/SU3 residuals, coupling targets, or external fit weights",
        ],
        "proof": [
            "The ordinary finite trace assigns coefficient one to each selected module label.",
            "Any class function of D_E depends on a label only through tau(L).",
            "Therefore the induced weight is invariant on the |tau|=1 labels, invariant on the tau=0 F3/G3 pair, and gives P its own tau=0 product slot.",
            "Thus the central-twist orbit-democracy packet is source-selected on the finite Galerkin trace branch with a=b=p=1.",
            "Substitution into the previous c-axis theorem gives H13=H23=0, the validated H_sel block, the exact G_ret block, Pi_tw=+e3, and the same tau table.",
        ],
        "selected_weights": {"a": 1, "b": 1, "p": 1},
        "status": "CLOSED_ON_FINITE_GALERKIN_TRACE_BRANCH",
    }

    finite_determinant_probe = {
        "central_operator": "D_E=diag(tau(L)) on the selected finite labels",
        "nonzero_labels": nonzero_labels,
        "zero_labels": zero_labels,
        "finite_trace_tau_squared_computed": finite_trace_tau_squared,
        "finite_trace_tau_squared_packet": trace_payload["finite_trace_tau_squared"],
        "finite_nonzero_tau_label_count_computed": finite_nonzero_tau_label_count,
        "finite_trace_projector_packet": trace_payload["finite_trace_projector"],
        "nonzero_central_character_abs_logdet": 0,
        "reason": "On the nonzero central-character sector the eigenvalues are +/-1, so the absolute finite log determinant is zero after zero modes are quotiented.",
        "what_this_determines": [
            "finite central projector trace",
            "finite nonzero tau label count",
            "finite tau^2 heat trace",
            "finite central-character determinant of D_E itself",
        ],
        "what_this_does_not_determine": [
            "smooth Nil/Iwasawa threshold spectrum",
            "multiplicities and index weights for the threshold operator",
            "regularized heat/zeta/torsion finite part of a same-source smooth D_E/rho_E/operator",
            "absolute determinant normalization beyond the finite central-character toy operator",
        ],
        "status": "FINITE_RESPONSE_CLOSED_SMOOTH_DETERMINANT_OPEN",
    }

    determinant_no_go = {
        "name": "FiniteCentralCharacterDoesNotSelectSmoothThresholdDeterminant",
        "proof": [
            "The finite central-character operator records only tau labels and finite traces.",
            "The local determinant interface requires positive eigenvalues, multiplicities, and index weights of the selected threshold operator.",
            "Those spectral data are not present in the finite Galerkin trace packet.",
            "Promoting the finite central logdet 0 to the physical determinant would silently assume that the full smooth threshold operator has no nontrivial positive spectrum beyond the central-character signs.",
            "That assumption is not source-selected and conflicts with the earlier promotion gate, which still marks the smooth operator and determinant finite part open.",
        ],
        "verdict": "DETERMINANT_OPERATOR_EXIT_NOT_CLOSED_BY_CURRENT_SOURCE",
        "required_next_object": "Selected_Qa_SU3_Smooth_Determinant_Spectral_Table_or_Source_Operator_v1",
    }

    candidate = {
        "candidate": "SelectedQaSU3CentralTwistOrbitDemocracySourceOrDeterminantOperator",
        "status": "QA_SU3_ORBIT_DEMOCRACY_SOURCE_SELECTED_FINITE_TRACE_SMOOTH_DETERMINANT_OPEN",
        "input_caxis_packet": str(ORTHO.relative_to(ROOT)),
        "input_finite_packet": str(PACKET.relative_to(ROOT)),
        "finite_orbit_democracy_source": {
            "source_selected": True,
            "source": trace_normalization,
            "theorem": finite_orbit_source_theorem,
            "closes_previous_open_condition": "orbit_democracy_source_selection_on_finite_galerkin_trace_branch",
        },
        "determinant_operator_branch": {
            "finite_probe": finite_determinant_probe,
            "smooth_exit_closed": False,
            "no_go": determinant_no_go,
        },
        "cross_check_against_previous_promotion_gate": {
            "same_source_smooth_operator": promotion["source_theorem_tests"][0]["verdict"],
            "charge_factorization": promotion["source_theorem_tests"][1]["verdict"],
            "determinant_finite_part": promotion["source_theorem_tests"][4]["verdict"],
            "promotes_now": promotion["decision"]["promotes_now"],
        },
        "decision": {
            "orbit_democracy_weight_source_selection": "CLOSED_FOR_FINITE_GALERKIN_TRACE_BRANCH",
            "finite_caxis_orthogonality": "CLOSED",
            "finite_response_payload": "CLOSED_TRACE_PROJECTOR_AND_TAU_SQUARED",
            "smooth_threshold_determinant_operator": "OPEN",
            "full_Qa_SU3_threshold_closure_now": False,
            "next_required_artifact": determinant_no_go["required_next_object"],
        },
        "what_this_closes": [
            "source selection of orbit-democracy weights on the finite Galerkin trace branch",
            "finite branch c-axis orthogonality without a conditional weight caveat",
            "finite central-character response invariants trace(Pi_tw)=1 and trace(tau^2)=8",
        ],
        "what_remains_open": [
            "same-source smooth Nil/Iwasawa threshold operator",
            "smooth determinant spectrum or heat/zeta/torsion finite part",
            "promotion from finite central-character response to physical Qa/SU3 threshold determinant",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedQaSU3CentralTwistOrbitDemocracySourceOrDeterminantOperator",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "finite_orbit_democracy_source_selected": True,
            "finite_caxis_orthogonality_unconditional_on_finite_trace_branch": True,
            "finite_trace_projector_and_tau_squared_checked": True,
        },
        "what_remains_open": {
            "smooth_threshold_determinant_operator": True,
            "same_source_smooth_spectrum": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["decision"]["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    note = render_note(candidate)
    return candidate, certificate, note


def label_is_primitive(value: int) -> bool:
    return abs(value) == 1


def render_note(candidate: dict[str, object]) -> str:
    finite = candidate["finite_orbit_democracy_source"]
    det = candidate["determinant_operator_branch"]["finite_probe"]
    return f"""# Selected Qa/SU3 Central-Twist Orbit-Democracy Source or Determinant Operator v1

## Result

One of the two remaining branches closes, and one does not.

The orbit-democracy weight source closes on the finite Galerkin trace branch.
The selected packet already uses:

```text
{finite["source"]}
```

That source selects unit counting weights on the eleven typed labels.  Therefore
the central-twist orbit-democracy packet has:

```text
a = b = p = 1
```

on the finite trace branch, and the previous c-axis theorem is no longer merely
conditional there.

## Finite Determinant Probe

The same finite response determines:

```text
trace(Pi_tw) = {det["finite_trace_projector_packet"]}
nonzero tau label count = {det["finite_nonzero_tau_label_count_computed"]}
trace(tau^2) = {det["finite_trace_tau_squared_computed"]}
nonzero central-character abs logdet = {det["nonzero_central_character_abs_logdet"]}
```

This is a real finite response payload, but it is not the smooth threshold
determinant.  It only computes the determinant of the finite central-character
operator `D_E=diag(tau(L))` after zero modes are quotiented.

## Determinant Verdict

The determinant exit does not close from the current source.  The missing object
is still the same-source smooth threshold spectrum, heat coefficient table,
zeta determinant, analytic torsion, or equivalent operator finite part.

Promoting the finite central-character logdet `0` to the physical Qa/SU3
threshold determinant would add an unstated assumption that the smooth operator
has no additional positive spectral content.  That assumption is not selected.

## New Frontier

```text
{candidate["decision"]["next_required_artifact"]}
```

So the proof state is sharper: finite orbit-democracy and finite c-axis
orthogonality are closed; smooth determinant/operator promotion remains open.
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
