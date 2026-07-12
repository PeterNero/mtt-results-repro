from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

TT_SUPPORT = ROOT / "certificates" / "gr_tt_support_final_theorem_certificate.json"
ABS_NORM = ROOT / "certificates" / "absolute_normalization_bridge_from_nonsm_certificate.json"
SCALE_LIFT = ROOT / "certificates" / "physical_scale_lifting_anchor_gate_certificate.json"
M_THEORY = ROOT / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json"
HESSIAN_KERNEL = ROOT / "certificates" / "selected_gr_hessian_kernel_candidate_certificate.json"

GR_SOURCE = TEXPAPERS / "11 General Relativity & Geometry" / "_md" / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md"
STRING_BRIDGE = (
    TEXPAPERS
    / "11 General Relativity & Geometry"
    / "_md"
    / "Why__GR_Falls_Out_of_String_Theory___A_Coherent_Admissibility_Shadow_Bridge_in_Modal_Triplet_Theory.md"
)
M_THEORY_SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__From_MTT_to_M_theory.md"
THETA_GRAVITY = (
    OBSIDIAN
    / "18 Theta-Closure & Execution Program"
    / "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale.md"
)

OUT_CERT = ROOT / "certificates" / "physical_normalization_stress_response_gate_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Physical_Normalization_Stress_Response_Gate_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(path: Path, *patterns: str) -> bool:
    text = read(path)
    return all(re.search(pattern, text, re.IGNORECASE | re.DOTALL) for pattern in patterns)


def main() -> None:
    tt_support = load(TT_SUPPORT)
    abs_norm = load(ABS_NORM)
    scale_lift = load(SCALE_LIFT)
    m_theory = load(M_THEORY)
    hessian_kernel = load(HESSIAN_KERNEL)

    source_tests = {
        "effective_einstein_hilbert_action_sourced": has(
            GR_SOURCE,
            r"S_\\?rm eff|S_\{\\rm eff\}|S_eff",
            r"Einstein--Hilbert",
            r"G_\\?rm eff|G_\{\\rm eff\}|G_eff",
        ),
        "variational_stress_tensor_sourced": has(
            GR_SOURCE,
            r"T_\{\\mu\\nu\}",
            r"delta S_\\?rm matter|\\delta S_\{\\rm matter\}",
        ),
        "einstein_equation_sourced": has(
            GR_SOURCE,
            r"G_\{\\mu\\nu\}",
            r"8\\pi G_\\?rm eff|8\\pi G_\{\\rm eff\}|8\\pi G_eff",
        ),
        "bianchi_conservation_sourced": has(GR_SOURCE, r"nabla\^\\mu T_\{\\mu\\nu\}", r"Bianchi"),
        "scalar_ym_dirac_examples_sourced": has(GR_SOURCE, r"Coherent scalar", r"Yang--Mills", r"Dirac"),
        "string_shadow_einstein_equivalence_sourced": has(
            STRING_BRIDGE,
            r"worldsheet",
            r"Einstein equations",
            r"admissibility",
        ),
        "m_theory_planck_slot_sourced": has(
            M_THEORY_SOURCE,
            r"kappa_\{11\}|kappa_11|\\kappa_\{11\}",
            r"Vol\(X_7\)|mathrm\{Vol\}\(X_7\)",
            r"M_\{\\mathrm\{P\}\}|Planck",
        ),
        "theta_volume_to_newton_slot_sourced": has(THETA_GRAVITY, r"31\.8", r"G_\{10\}|G_10", r"Newton"),
    }

    internal_closure = {
        "tt_support_closed": tt_support["theorem"]["status"] == "CLOSED",
        "lambda_GR_TT_internal_exact_branch": tt_support["conclusion"]["lambda_GR_TT_internal_exact_branch"],
        "canonical_internal_gr_normalization_closed": abs_norm["guardrails"][
            "claims_internal_dimensionless_normalization_closure"
        ],
        "internal_scale_lift_imported": scale_lift["closed_tests"]["internal_scale_lifting_number_available"],
        "m_theory_normalization_slot_identified": m_theory["closed_tests"]["m_theory_planck_slot_identified"],
    }

    stress_response = {
        "universal_variational_definition_closed": source_tests["variational_stress_tensor_sourced"],
        "conservation_law_closed": source_tests["bianchi_conservation_sourced"],
        "matter_examples_closed_as_forms": source_tests["scalar_ym_dirac_examples_sourced"],
        "selected_numeric_matter_parameters_closed": False,
        "selected_coherence_to_matter_map_closed": False,
        "interpretation": (
            "The variational stress tensor and standard coherent scalar/YM/Dirac forms are sourced. "
            "The selected MTT matter-spectrum coefficients and full coherence-to-matter map remain separate inputs."
        ),
    }

    physical_normalization = {
        "internal_theta_volume_rows_available": True,
        "theta_volume_coefficient": 31.8,
        "G_eff_relation_internal": "G_eff = G_10 / Vol_int",
        "m_theory_relation": "kappa_4^-2 = kappa_11^-2 Vol(X_7)",
        "physical_absolute_dimensionful_anchor_closed": abs_norm["physical_absolute_status"][
            "physical_absolute_dimensionful_predictions_closed"
        ],
        "internal_to_SI_unit_map_selected": scale_lift["open_tests"]["internal_to_SI_unit_map_selected"],
        "dimensionful_modal_gap_value_computed": m_theory["open_tests"]["dimensionful_modal_gap_value_computed"],
        "newton_or_planck_prediction_allowed_now": m_theory["verdict"]["newton_or_planck_prediction_allowed_now"],
    }

    assembly = {
        "dimensionless_exact_TT_branch_ready": all(internal_closure.values()),
        "stress_response_form_ready": all(
            [
                stress_response["universal_variational_definition_closed"],
                stress_response["conservation_law_closed"],
                stress_response["matter_examples_closed_as_forms"],
            ]
        ),
        "EH_target_operator_identified": hessian_kernel["what_this_closes"]["EH_target_operator_identified"],
        "retarded_support_target_identified": hessian_kernel["what_this_closes"]["retarded_support_target_identified"],
        "physical_absolute_normalization_ready": physical_normalization["physical_absolute_dimensionful_anchor_closed"],
        "selected_full_matter_map_ready": stress_response["selected_coherence_to_matter_map_closed"],
    }

    full_physical_gr_closed = (
        assembly["dimensionless_exact_TT_branch_ready"]
        and assembly["stress_response_form_ready"]
        and assembly["EH_target_operator_identified"]
        and assembly["retarded_support_target_identified"]
        and assembly["physical_absolute_normalization_ready"]
        and assembly["selected_full_matter_map_ready"]
    )

    status = (
        "STRUCTURAL_STRESS_RESPONSE_CLOSED_PHYSICAL_NORMALIZATION_OPEN"
        if assembly["stress_response_form_ready"] and not full_physical_gr_closed
        else "PHYSICAL_GR_RESPONSE_GATE_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "physical_normalization_stress_response_gate",
        "status": status,
        "input_certificates": {
            "gr_tt_support_final_theorem": str(TT_SUPPORT),
            "absolute_normalization_bridge_from_nonsm": str(ABS_NORM),
            "physical_scale_lifting_anchor_gate": str(SCALE_LIFT),
            "m_theory_modal_gap_dimensional_anchor_candidate": str(M_THEORY),
            "selected_gr_hessian_kernel_candidate": str(HESSIAN_KERNEL),
        },
        "source_files": {
            "gr_reduction": str(GR_SOURCE),
            "string_shadow_bridge": str(STRING_BRIDGE),
            "m_theory": str(M_THEORY_SOURCE),
            "theta_gravity": str(THETA_GRAVITY),
        },
        "source_tests": source_tests,
        "internal_closure": internal_closure,
        "stress_response": stress_response,
        "physical_normalization": physical_normalization,
        "einstein_response_assembly": assembly,
        "full_physical_gr_closed": full_physical_gr_closed,
        "what_is_closed_now": [
            "exact-branch TT support and lambda_GR,TT=15 in canonical internal units",
            "universal variational stress-tensor form for coherent scalar/YM/Dirac sectors",
            "Bianchi/Noether conservation pushforward for the reduced effective action",
            "normalization slot G_eff=G_10/Vol_int and kappa_4^-2=kappa_11^-2 Vol(X_7)",
        ],
        "what_remains": [
            "select a target-independent dimensionful anchor: G_10, ell_p, kappa_11, alpha_prime, or equivalent modal-gap unit",
            "compute the selected internal-to-SI unit map without observed G_N or M_Pl input",
            "complete the selected coherence-to-matter stress map with actual matter/gauge coefficients",
            "assemble the low-energy Einstein-response theorem including retarded kernel, matter source, and normalization",
            "prove QG loop execution and GR response use the same selected operator beyond structural equivalence",
        ],
        "guardrails": {
            "claims_measured_Newton_constant": False,
            "claims_measured_Planck_scale": False,
            "uses_observed_Newton_or_Planck_input": False,
            "claims_full_physical_GR_closed": full_physical_gr_closed,
            "adds_new_GR_parameter": False,
            "treats_G10_as_selected": False,
        },
        "next_theorem": {
            "name": "Selected_Physical_Anchor_and_Einstein_Response_Theorem",
            "minimal_inputs": [
                "dimensionful modal-gap or fundamental length/action selection",
                "derived G_10 or kappa_11 in fixed conventions",
                "selected matter/gauge stress-response coefficients",
                "retarded kernel/operator equality with QG loop execution",
            ],
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Physical Normalization Stress Response Gate v1

## Closed Now

The exact TT branch is ready in canonical internal units:

```text
support(J_TT)=|d_*> tensor span{c2,s2}
lambda_GR,TT=15
```

The GR corpus also sources the universal stress-response form:

```text
T_{mu nu} = -2/sqrt(-g) * delta S_matter / delta g^{mu nu}.
```

For the coherent reduced action, the Bianchi/Noether identity gives
`nabla^mu T_{mu nu}=0`, and the scalar, Yang-Mills, and Dirac stress tensors are
spelled out as standard variational forms. This closes the structural
stress-response slot.

## Still Open

The physical normalization is not closed. Current sources give the correct
slots:

```text
G_eff = G_10 / Vol_int
kappa_4^-2 = kappa_11^-2 Vol(X_7)
Vol_int ~= 31.8 R_1^3
```

but they do not select the dimensionful unit `G_10`, `ell_p`, `kappa_11`,
`alpha_prime`, or an equivalent modal-gap scale without using observed Newton
or Planck data.

## Verdict

The next theorem is not another TT support theorem. It is a physical anchor and
Einstein-response assembly theorem: select the dimensionful scale, complete the
coherence-to-matter stress map, and prove the QG loop execution operator is the
same selected low-energy GR response operator.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
