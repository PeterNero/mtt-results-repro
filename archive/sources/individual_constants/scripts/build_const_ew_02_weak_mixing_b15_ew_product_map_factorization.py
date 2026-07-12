"""Build CONST-EW-02 B15 electroweak product-map factorization.

B15 turns the open B14 bridge into an exact source contract.  The selected H2
scale and q64=15 covariance are necessary source data, but the weak-mixing
profile product must factor through a same-branch electroweak threshold
operator or local-system torsion payload.  This builder records the factor map,
legal exits, rejected shortcuts, and the next executable source packet.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"
THETA_WEAK = (
    TEXPAPERS
    / "18 Theta-Closure & Execution Program"
    / "_work"
    / "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle"
    / "main.tex"
)

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b15_ew_product_map_factorization"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PAPER_AUDIT = BASE / "theta_weak_mixing_paper_input_audit.packet.json"
SOURCE_FACTOR = BASE / "source_product_map_factorization.packet.json"
EXITS = BASE / "operator_or_torsion_exit_matrix.packet.json"
REJECTIONS = BASE / "shortcut_rejection.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B15_EWProductMapFactorization_v1.md"

STATUS = "MTT_CONST_EW_02_B15_EW_PRODUCT_MAP_FACTORIZED_THRESHOLD_PAYLOAD_REQUIRED"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b14_path = DATA / "const_ew_02_weak_mixing_b14_scalelaw_projection_or_phi_ew_import.candidate.json"
    b14_h2_path = DATA / "const_ew_02_weak_mixing_b14_scalelaw_projection_or_phi_ew_import" / "selected_h2_scalelaw_import.packet.json"
    b14_cov_path = DATA / "const_ew_02_weak_mixing_b14_scalelaw_projection_or_phi_ew_import" / "selected_covariance_phi_ew_import.packet.json"
    b12_routes_path = DATA / "const_ew_02_weak_mixing_b12_profile_product_source_contract" / "profile_product_route_matrix.packet.json"
    heterotic_kernel_note = QA / "proof_corpus" / "Selected_Heterotic_Strominger_Electroweak_Threshold_Kernel_v1.md"
    torsion_payload_note = QA / "proof_corpus" / "Selected_Heterotic_Strominger_AnalyticTorsion_or_ThresholdOperator_Payload_v1.md"
    u1_carrier_note = QA / "proof_corpus" / "Selected_U1_Threshold_Carrier_Projector_or_SU2_Operator_Spectrum_v1.md"
    u1_spectrum_note = QA / "proof_corpus" / "Selected_U1_Hypercharge_Operator_Spectrum_Source_Packet_v1.md"
    chi_qa_note = QA / "proof_corpus" / "Selected_Qa_SU3_Response_Functional_Chi_Qa_v1.md"

    b14 = load(b14_path)
    b14_h2 = load(b14_h2_path)
    b14_cov = load(b14_cov_path)
    b12_routes = load(b12_routes_path)

    xL_required = float(b12_routes["target_product"]["required_value"])
    sin2_if_emitted = float(b12_routes["target_product"]["sin2_if_emitted"])

    paper_audit = {
        "schema": "MTTConstEW02B15ThetaWeakMixingPaperInputAudit.v1",
        "status": "PAPER_FORMULA_USEFUL_NONCIRCULAR_CLAIM_NOT_STRICT_SOURCE_CLOSURE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B15-PAPER-INPUT-AUDIT",
        "input_paper": rel(THETA_WEAK),
        "paper_level_formulae": {
            "one_loop_running": "1/g_a^2(mu)=1/g_a^2(mu0)-b_a log(mu/mu0)/(8*pi^2)",
            "beta_coefficients": {"b1": "41/10", "b2": "-19/6"},
            "weak_angle": "sin^2(theta_W)=(3/5 g1^2)/((3/5 g1^2)+g2^2)",
        },
        "paper_level_inputs_that_are_not_strict_source_outputs": [
            "mu_Theta=5 TeV matching scale",
            "g2 extracted from G_F and m_W, with Delta r_eff as threshold policy",
            "Theta-fixed ratio I2/I1 approximately 0.56027 from gauge-sector closure context",
            "one-loop MS-bar scheme and threshold convention",
        ],
        "usable_now": [
            "algebraic RG/projection shape",
            "SM-parity or one-primitive replay lane",
            "guardrail showing why a strict source theorem must emit g2/scale/threshold data independently",
        ],
        "strict_no_knob_closure_from_paper": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_factor = {
        "schema": "MTTConstEW02B15SourceProductMapFactorization.v1",
        "status": "PRODUCT_MAP_FACTORED_BUT_PAYLOAD_VALUE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B15-SOURCE-PRODUCT-MAP",
        "inputs": {
            "B14_candidate": rel(b14_path),
            "B14_H2_import": rel(b14_h2_path),
            "B14_covariance_import": rel(b14_cov_path),
            "B12_product_contract": rel(b12_routes_path),
            "heterotic_threshold_kernel_note": rel(heterotic_kernel_note),
            "torsion_or_operator_payload_note": rel(torsion_payload_note),
            "u1_carrier_projector_note": rel(u1_carrier_note),
            "u1_hypercharge_spectrum_note": rel(u1_spectrum_note),
            "chi_Qa_note": rel(chi_qa_note),
        },
        "source_verified_inputs": {
            "selected_H2_scale_law": b14_h2["imported_selection"]["scale_law"] == "H2",
            "selected_R_star": b14_h2["imported_selection"]["R_star"],
            "selected_rho_UV": b14_cov["imported_covariance"]["rho_UV"],
            "selected_G_11": b14_cov["imported_covariance"]["G_11"],
            "selected_d_Q": b14_cov["imported_covariance"]["D_raw_norm_squared_d_Q"],
            "selected_q64_15_character_channel": b14_cov["imported_covariance"]["selected_character"],
            "selected_Qa_finite_response_chi_Qa": 1,
        },
        "required_factorization": {
            "xL": "x * L_eff",
            "x": "same-branch electroweak gauge-action/threshold coefficient emitted by K_EW or Phi_EW",
            "L_eff": "same-branch matching/profile log emitted by the selected H2/threshold operator projection",
            "strict_target": xL_required,
            "if_emitted_then_sin2": sin2_if_emitted,
        },
        "allowed_strict_forms": [
            "H2Projection: Pi_EW(H2, threshold payload) -> (x, L_eff)",
            "PhiEWResponse: Phi_EW(rho_UV, q64=15 covariance, threshold payload) -> xL",
            "OperatorThreshold: zeta/heat/torsion finite part emits u1,u2 directly in the B9 profile formula",
        ],
        "not_enough_by_itself": [
            "H2 scale law",
            "G_11=d_Q=1 covariance",
            "chi_Qa=1 internal response",
            "U1 rank-3 carrier shape without selected projector/operator",
            "paper-level 5 TeV RG replay",
        ],
        "emits_xL": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    exits = {
        "schema": "MTTConstEW02B15OperatorOrTorsionExitMatrix.v1",
        "status": "TWO_STRICT_EXITS_LIVE_OPERATOR_LANE_PRIMARY",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B15-EXIT-MATRIX",
        "primary_exit": {
            "name": "C_hym_monad_threshold_operator",
            "source_status": "LIVE_EXIT_DELTA_A_SPECTRUM_AND_MU_OPEN",
            "why_primary": "Sibling Qa/SU3 work has explicit Iwasawa HYM/monad data and a selected operator domain, but still lacks mu/moduli, spectrum, heat/zeta finite part, and trace weights.",
            "must_emit": [
                "selected U1/Y or Qa/Qc/SU2 Laplace-type threshold operator",
                "selected mu/moduli from same branch",
                "positive spectrum or heat/zeta/torsion finite part",
                "P_perp shared-circle quotient projector for U1 carrier",
                "same-scheme trace weights for Qa, Qc, SU2, and hypercharge",
            ],
        },
        "parallel_exit": {
            "name": "B_ray_singer_or_reidemeister_local_system",
            "source_status": "LIVE_EXIT_SOURCE_CHARACTER_OPEN",
            "why_parallel": "A selected compact Nil/Iwasawa local system could emit analytic torsion, but no selected Qa/SU3 lattice character or torsion finite part is certified.",
            "must_emit": [
                "selected Nil/Iwasawa lattice character before electroweak comparison",
                "acyclicity or explicit zero-mode policy",
                "Ray-Singer/Reidemeister finite part",
                "same-stack trace weights and threshold convention",
            ],
        },
        "one_primitive_lane": {
            "name": "SM-standard one input replay",
            "status": "AVAILABLE_BUT_NOT_STRICT_NO_KNOB",
            "meaning": "Use one universal physical gauge-action normalization or g2 input, then replay the paper's RG projection. This is useful for parity but not a strict source derivation.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    rejections = {
        "schema": "MTTConstEW02B15ShortcutRejection.v1",
        "status": "SHORTCUTS_REJECTED_EXACT_PAYLOAD_REQUIRED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B15-SHORTCUT-REJECTION",
        "rejected_shortcuts": [
            {
                "shortcut": "xL = f(R_star) chosen by closeness",
                "reason": "Uses the weak-angle target to choose a projection rather than a source theorem.",
            },
            {
                "shortcut": "xL = f(rho_UV) without threshold payload",
                "reason": "Selected covariance closes the response denominator, not the electroweak observable map.",
            },
            {
                "shortcut": "reuse Qa log(2008) as U1/Y threshold spectrum",
                "reason": "Sibling audit rejects it as wrong scheme and double promotion.",
            },
            {
                "shortcut": "promote rank-3 U1 carrier shape to selected 2/3 threshold index",
                "reason": "Carrier shape is found, but selected projector/operator packet is still missing.",
            },
            {
                "shortcut": "use Theta V 5 TeV result as no-knob closure",
                "reason": "It is a useful RG/parity replay but imports one physical normalization and matching-scale policy.",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B15NextWork.v1",
        "status": "NEXT_WORKORDER_SOURCE_OPERATOR_OR_TORSION_PAYLOAD",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B16-SOURCE-OPERATOR-OR-TORSION-PAYLOAD",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B16-HYM-MONAD-THRESHOLD-OPERATOR",
            "task": "Construct the same-branch HYM/monad Delta_A or equivalent Laplace-type threshold operator, including mu/moduli, P_perp quotient, spectrum/heat/zeta finite part, and trace weights.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B16-LOCAL-SYSTEM-TORSION",
            "task": "Search for a selected compact Nil/Iwasawa local-system character and compute the corresponding analytic torsion finite part.",
        },
        "handoff_to_qa_su3_repo": "Same_Source_Selected_U1_Carrier_Projector_Theorem_v1 plus Selected_Heterotic_Strominger_SourceOperator_or_LocalSystem_Torsion_Computation_v1",
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB15EWProductMapFactorization",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B15-H2-EW-PROJECTION-OR-PHI-EW-PRODUCT",
        "output_packets": {
            "theta_weak_mixing_paper_input_audit": rel(PAPER_AUDIT),
            "source_product_map_factorization": rel(SOURCE_FACTOR),
            "operator_or_torsion_exit_matrix": rel(EXITS),
            "shortcut_rejection": rel(REJECTIONS),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B15EWProductMapFactorizationTheorem",
            "proved": True,
            "statement": (
                "After B14, a strict weak-mixing derivation must factor the profile "
                "product through a same-branch electroweak threshold operator or "
                "local-system torsion payload. H2, rho_UV covariance, and chi_Qa "
                "are source-verified internal ingredients, but none independently "
                "emits xL. The exact next executable object is the selected "
                "HYM/monad threshold operator or local-system torsion packet."
            ),
        },
        "strict_xL_emitted_now": False,
        "paper_replay_lane_available": True,
        "one_universal_primitive_lane_available": True,
        "strict_no_knob_payload_required": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B15_EWProductMapFactorization_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "input_candidate": rel(b14_path),
        "strict_xL_emitted_now": False,
        "product_map_factorized": True,
        "threshold_payload_required": True,
        "primary_exit": exits["primary_exit"]["name"],
        "parallel_exit": exits["parallel_exit"]["name"],
        "paper_replay_lane_available": True,
        "one_universal_primitive_lane_available": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B15 EW Product Map Factorization v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B15-H2-EW-PROJECTION-OR-PHI-EW-PRODUCT`

## Result

B15 factors the open B14 bridge.  The current strict route is:

```text
selected H2 scale law
+ selected q64=15 rho_UV covariance
+ selected Qa finite response chi_Qa=1
+ same-branch electroweak threshold operator or torsion payload
-> xL
```

The first three source ingredients are now available.  The fourth is not.

## Why This Matters

This rules out ad hoc maps such as `xL=f(R_star)` or `xL=f(rho_UV)`.  The
missing map has to pass through an electroweak object with stack trace weights,
zero-mode policy, spectrum/torsion finite part, and threshold convention.

## Legal Exits

Primary:

```text
HYM/monad threshold operator
```

Parallel:

```text
Ray-Singer/Reidemeister local-system torsion
```

One-primitive parity lane:

```text
one physical gauge normalization + Theta V RG replay
```

This lane is useful, but not strict no-knob closure.

## Next

`CONST-EW-02 / WEAK-MIXING / B16-SOURCE-OPERATOR-OR-TORSION-PAYLOAD`
"""

    for path, payload in [
        (PAPER_AUDIT, paper_audit),
        (SOURCE_FACTOR, source_factor),
        (EXITS, exits),
        (REJECTIONS, rejections),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
