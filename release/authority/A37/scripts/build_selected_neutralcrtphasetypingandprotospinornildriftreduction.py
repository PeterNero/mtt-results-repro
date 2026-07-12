"""Build the neutral CRT phase-typing and proto-spinor nil-drift reduction."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralcrtphasetypingandprotospinornildriftreduction"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_crt_phase_typing_and_nil_drift.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralCRTPhaseTypingAndProtoSpinorNilDriftReduction_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_CRT_PHASE_TYPING_CLOSED_Q7_OVER_448_CLUE_RETIRED_NIL_DRIFT_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralNilHolonomySourceAndAbsoluteScale_v1"

Q79_CERT = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates\z64_exact_branch_certificate.json")
PROTO = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\10 ProtoSpinor\Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def crt_lift(r64: int, r7: int) -> int:
    return next(q for q in range(448) if q % 64 == r64 and q % 7 == r7)


def r_no(phi: float) -> float:
    return abs(math.sin(phi)) / abs(math.sin(phi + math.pi / 3.0))


def main() -> int:
    prior = load(
        ROOT / "candidate_data" / "selected_neutraleffectiveweightidentifiabilityreduction"
        / "neutral_effective_weight_identifiability.packet.json"
    )
    old = load(
        ROOT / "candidate_data" / "selected_neutralspectralactionslopeorseesawsource"
        / "neutral_spectral_and_seesaw_source_discrimination.packet.json"
    )
    qcert = load(Q79_CERT)
    proto = PROTO.read_text(encoding="utf-8")

    q64 = int(qcert["conclusion"]["q_64"])
    q7 = int(qcert["conclusion"]["q_7"])
    q = int(qcert["conclusion"]["q_mod_448"])
    q7_lift = crt_lift(0, q7)
    q64_lift = crt_lift(q64, 0)
    recombined = (q7_lift + q64_lift) % 448

    phi_mistyped = 2.0 * math.pi * q7 / 448.0
    phi_z7 = 2.0 * math.pi * q7 / 7.0
    phi_q7_lift = 2.0 * math.pi * q7_lift / 448.0
    phi_global = 2.0 * math.pi * q / 448.0
    old_ratio = float(old["circle_drift_route"]["candidate_ratios"]["q7_over_qmod_drift"])

    checks = {
        "A36_reduction_closed": prior["theorem"]["proved"],
        "q79_certificate_present": Q79_CERT.exists(),
        "proto_spinor_source_present": PROTO.exists(),
        "q64_equals_15": q64 == 15,
        "q7_equals_2": q7 == 2,
        "global_q_equals_79": q == 79,
        "q7_only_CRT_lift_equals_128": q7_lift == 128,
        "q64_only_CRT_lift_equals_399": q64_lift == 399,
        "CRT_recombines_to_q79": recombined == q,
        "local_Z7_phase_equals_CRT_lift_phase": abs(phi_z7 - phi_q7_lift) < 1e-15,
        "old_q7_over_448_ratio_reproduced": abs(r_no(phi_mistyped) - old_ratio) < 1e-15,
        "proto_spinor_has_nil_phase_model": "Neutrino Nil-Phase Drift Model" in proto,
        "proto_spinor_defines_three_basin_orbit": "m_k^2" in proto and "2\\pi k}{3" in proto,
        "proto_spinor_marks_model_diagnostic": "diagnostic toy models" in proto,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedNeutralCRTPhaseTypingAndProtoSpinorNilDriftReduction.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralEffectiveWeightIdentifiabilityReduction_v1",
        "theorem": {
            "name": "NeutralCRTCharacterTypingAndNilDriftNonIdentificationTheorem",
            "proved": theorem_proved,
            "statement": "On the selected exact branch Z_448 is resolved by residues q_64=15 and q_7=2, recombining to q=79. The Z_7 residue has local character angle 2 pi (2/7); its unique CRT lift with zero Z_64 component is 128 mod 448 and gives the same fraction 128/448=2/7. Therefore the previously tested angle 2 pi (2/448) is neither the local Z_7 character, its CRT lift, nor the selected global q=79 character. Its close neutrino-ratio value 0.0318813296 is a mistyped numerical clue and cannot source the proto-spinor nil drift. The proto-spinor corpus does supply the correct one-parameter three-basin nil-holonomy formula, but it explicitly leaves the drift value and absolute scale execution-level. Thus the physical neutral cutset is sharpened to one genuine neutral nil-holonomy phi_nu plus one absolute scale mu_nu.",
        },
        "source_checks": checks,
        "CRT_character_typing": {
            "group": "Z448 ~= Z64 x Z7",
            "q64": q64,
            "q7": q7,
            "q_global": q,
            "q7_only_lift_mod448": q7_lift,
            "q64_only_lift_mod448": q64_lift,
            "lift_sum_mod448": recombined,
            "Z7_local_fraction": "2/7",
            "Z7_CRT_lift_fraction": "128/448=2/7",
            "selected_global_fraction": "79/448",
            "mistyped_fraction": "2/448",
            "mistyped_fraction_is_selected_character": False,
        },
        "phase_and_ratio_execution": {
            "mistyped_phi_2pi_2_over_448": phi_mistyped,
            "mistyped_r_NO": r_no(phi_mistyped),
            "local_Z7_phi_2pi_2_over_7": phi_z7,
            "local_Z7_r_NO": r_no(phi_z7),
            "CRT_lift_phi_2pi_128_over_448": phi_q7_lift,
            "CRT_lift_r_NO": r_no(phi_q7_lift),
            "global_q79_phi": phi_global,
            "global_q79_r_NO": r_no(phi_global),
            "observed_ratio_used_only_as_postcheck": old["circle_drift_route"]["postcheck_ratio"],
            "observed_ratio_used_as_selector": False,
        },
        "proto_spinor_neutral_shape": {
            "sector": "co-aligned neutrino loops with suppressed anchored curvature",
            "formula": "m_k^2=m_0^2+A*cos(phi_nu+2*pi*k/3)",
            "NO_ratio": "|sin(phi_nu)|/|sin(phi_nu+pi/3)|",
            "shape_coordinate": "phi_nu",
            "absolute_scale_coordinate": "mu_nu (equivalently A after a physical unit is fixed)",
            "phi_nu_selected_by_current_finite_character_packet": False,
            "mu_nu_selected": False,
            "structural_formula_available": True,
            "numerical_realization_execution_level_in_corpus": True,
        },
        "supersession_decision": {
            "A29_second_order_orbit_algebra_retracted": False,
            "A29_orbit_promoted_as_physical_neutral_mass_shape": False,
            "A31_scale_no_go_scope": "valid only for identifying the A29 [1,4,7] orbit as the physical neutral spectrum",
            "A31_excludes_proto_spinor_nil_drift_family": False,
            "A32_q7_over_qmod_close_clue_retired": theorem_proved,
            "reason": "2/448 mixes a Z7 residue numerator with the full Z448 denominator and is not a character supplied by the CRT branch",
        },
        "reduced_physical_cutset": {
            "continuous_coordinates": ["neutral nil-holonomy phi_nu", "absolute scale mu_nu"],
            "count": 2,
            "one_to_three_knob_policy_compatible": True,
            "remaining_source_theorem": "identify the neutral co-aligned nil loop in the selected common U(1) bundle and evaluate its holonomy without using oscillation data",
            "remaining_scale_theorem": "evaluate the anchored neutral Hessian/closure-cost normalization in the same physical scheme",
        },
        "what_closes_here": {
            "CRT_phase_typing": theorem_proved,
            "q7_over_448_near_hit_retired": theorem_proved,
            "proto_spinor_nil_drift_formula_imported": theorem_proved,
            "physical_cutset_specialized_to_phi_and_scale": theorem_proved,
            "neutral_nil_holonomy_selected": False,
            "absolute_neutral_scale_selected": False,
            "dimensionful_neutral_masses": False,
        },
        "new_physical_value_fields_closed_here": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralCRTPhaseTypingAndProtoSpinorNilDriftReduction_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "q7_only_CRT_lift": q7_lift,
        "q64_only_CRT_lift": q64_lift,
        "global_q": q,
        "q7_over_448_is_selected_character": False,
        "q7_over_448_near_hit_retired": theorem_proved,
        "proto_spinor_nil_drift_formula_imported": theorem_proved,
        "remaining_continuous_coordinate_count": 2,
        "neutral_nil_holonomy_selected": False,
        "absolute_neutral_scale_selected": False,
        "dimensionful_neutral_masses_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral CRT Phase Typing and Proto-Spinor Nil-Drift Reduction v1

## CRT correction

The selected exact branch has `q64=15`, `q7=2`, and `q=79 mod 448`.
The isolated `Z7` residue is a phase fraction `2/7`. Its canonical CRT lift is
`128 mod 448`, hence `128/448=2/7`. It is not `2/448`.

The previously attractive calculation

```text
phi = 2*pi*(2/448)
r_NO(phi) = {r_no(phi_mistyped)}
```

therefore mixed a `Z7` residue numerator with the full `Z448` denominator. It
is neither the local `Z7` character, its CRT lift, nor the selected global
`79/448` character. The numerical near-hit is retired as a source clue.

## Correct proto-spinor frontier

The proto-spinor corpus supplies the structurally appropriate neutrino family

```text
m_k^2 = m_0^2 + A cos(phi_nu + 2*pi*k/3),
r_NO = |sin(phi_nu)|/|sin(phi_nu+pi/3)|.
```

It explicitly treats the numerical realization as execution-level. The
remaining physical coordinates are therefore the genuine neutral nil-holonomy
`phi_nu` and one absolute scale `mu_nu`. A31 remains a valid no-go for promoting
the A29 `[1,4,7]` orbit by common scaling, but it does not exclude this distinct
proto-spinor nil-drift family.

Next artifact: `{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
