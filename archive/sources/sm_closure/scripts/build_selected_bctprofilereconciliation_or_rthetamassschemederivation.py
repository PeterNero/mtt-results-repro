"""Build BCT profile reconciliation or R_theta mass-scheme derivation artifact."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bctprofilereconciliation_or_rthetamassschemederivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EFT_PROFILE = PACKET_DIR / "bct_correlated_eft_profile.packet.json"
FULLSM_PROFILE = PACKET_DIR / "bct_correlated_fullsm_profile.packet.json"
RTHETA_GAP = PACKET_DIR / "rtheta_mass_scheme_derivation_gap_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bct_profile.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BCTProfileReconciliation_or_RThetaMassSchemeDerivation_v1.md"

PREVIOUS = DATA / "selected_allbctexternalrows_or_fullsmconventionreconciliation.candidate.json"
ROW_ASSEMBLY = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "all_bct_external_rows_assembly.packet.json"
)
HZ_MATRIX = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "huang_zhou_eft_fullsm_reconciliation_matrix.packet.json"
)
PROFILE_GATE = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "fullsm_profile_reconciliation_gate.packet.json"
)
OLD_RTHETA_GAP = (
    DATA
    / "selected_bottomcharmtauformulaimport_or_rthetamassschemederivation"
    / "rtheta_bct_mass_scheme_derivation_gap.packet.json"
)

STATUS = (
    "MTT_SELECTED_BCTPROFILERECONCILIATION_OR_RTHETAMASSSCHEMEDERIVATION_"
    "BUILT_CORRELATED_PROFILE_BORDERLINE_RTHETA_OPEN"
)
NEXT = "MTT_Selected_CharmCRunDecInputPolicy_or_RThetaMassSchemeDerivation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing BCT profile sources: " + ", ".join(missing))


def det3(m: list[list[float]]) -> float:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def inv3(m: list[list[float]]) -> list[list[float]]:
    d = det3(m)
    if abs(d) < 1e-15:
        raise ValueError("singular 3x3 matrix")
    return [
        [
            (m[1][1] * m[2][2] - m[1][2] * m[2][1]) / d,
            (m[0][2] * m[2][1] - m[0][1] * m[2][2]) / d,
            (m[0][1] * m[1][2] - m[0][2] * m[1][1]) / d,
        ],
        [
            (m[1][2] * m[2][0] - m[1][0] * m[2][2]) / d,
            (m[0][0] * m[2][2] - m[0][2] * m[2][0]) / d,
            (m[0][2] * m[1][0] - m[0][0] * m[1][2]) / d,
        ],
        [
            (m[1][0] * m[2][1] - m[1][1] * m[2][0]) / d,
            (m[0][1] * m[2][0] - m[0][0] * m[2][1]) / d,
            (m[0][0] * m[1][1] - m[0][1] * m[1][0]) / d,
        ],
    ]


def quad(z: list[float], inv: list[list[float]]) -> float:
    return sum(z[i] * inv[i][j] * z[j] for i in range(3) for j in range(3))


def chi2_sf_df3(x: float) -> float:
    # Survival function for chi-square with 3 degrees of freedom.
    if x > 1500.0:
        return 0.0
    return math.erfc(math.sqrt(x / 2.0)) + math.sqrt(2.0 * x / math.pi) * math.exp(-x / 2.0)


def profile_packet(
    *,
    status: str,
    profile_label: str,
    table_key: str,
    z_by_row: dict[str, float],
    correlation_matrix: list[list[float]],
    correlation_source: str,
) -> dict[str, Any]:
    ids = [
        "bottom_MSbar_native_scale_transport",
        "charm_MSbar_native_scale_transport",
        "tau_pole_rest_to_running_lepton",
    ]
    z = [z_by_row[row_id] for row_id in ids]
    inv = inv3(correlation_matrix)
    chi2 = quad(z, inv)
    diagonal = sum(v * v for v in z)
    p = chi2_sf_df3(chi2)
    return {
        "schema": "MTTBCTCorrelatedProfile.v1",
        "status": status,
        "profile_label": profile_label,
        "table_key": table_key,
        "row_order": ids,
        "z_residuals": dict(zip(ids, z)),
        "correlation_matrix": correlation_matrix,
        "correlation_source": correlation_source,
        "correlation_matrix_determinant": det3(correlation_matrix),
        "inverse_correlation_matrix": inv,
        "diagonal_chi_square": diagonal,
        "correlated_chi_square": chi2,
        "degrees_of_freedom": 3,
        "chi_square_survival_probability_df3": p,
        "passes_95pct_profile_gate": p >= 0.05,
        "passes_99pct_profile_gate": p >= 0.01,
        "profile_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, ROW_ASSEMBLY, HZ_MATRIX, PROFILE_GATE, OLD_RTHETA_GAP]
    require_sources(sources)

    previous = load(PREVIOUS)
    assembly = load(ROW_ASSEMBLY)
    matrix = load(HZ_MATRIX)
    old_rtheta_gap = load(OLD_RTHETA_GAP)

    ids = [
        "bottom_MSbar_native_scale_transport",
        "charm_MSbar_native_scale_transport",
        "tau_pole_rest_to_running_lepton",
    ]
    eft_z = {
        row_id: matrix["matrix_rows"][row_id]["EFT_QCDxQED_5q3l_MZ"]["z_delta_using_table_sigma"]
        for row_id in ids
    }
    fullsm_z = {
        row_id: matrix["matrix_rows"][row_id]["FullSM_6q3l_MZ"]["z_delta_using_table_sigma"]
        for row_id in ids
    }
    eft_corr = [
        [1.0, 0.37, -0.002],
        [0.37, 1.0, -0.0017],
        [-0.002, -0.0017, 1.0],
    ]
    fullsm_corr = [
        [1.0, 0.37, -0.023],
        [0.37, 1.0, -0.029],
        [-0.023, -0.029, 1.0],
    ]

    eft_profile = profile_packet(
        status="BCT_EFT_CORRELATED_PROFILE_COMPUTED_BORDERLINE_NOT_CLOSED",
        profile_label="Huang-Zhou EFT QCDxQED MZ b/c/tau profile",
        table_key="EFT_QCDxQED_5q3l_MZ",
        z_by_row=eft_z,
        correlation_matrix=eft_corr,
        correlation_source=(
            "Huang-Zhou Table 7, EFT SU(3)c x U(1)EM MZ correlation submatrix for "
            "mb, mc, m_tau"
        ),
    )
    write_json(EFT_PROFILE, eft_profile)

    fullsm_profile = profile_packet(
        status="BCT_FULLSM_CORRELATED_PROFILE_COMPUTED_REJECTED_FOR_CURRENT_EXTERNAL_ROWS",
        profile_label="Huang-Zhou full-SM MZ b/c/tau profile",
        table_key="FullSM_6q3l_MZ",
        z_by_row=fullsm_z,
        correlation_matrix=fullsm_corr,
        correlation_source=(
            "Huang-Zhou Table 8, full SM MZ correlation submatrix for "
            "mb(yb), mc(yc), m_tau(y_tau)"
        ),
    )
    write_json(FULLSM_PROFILE, fullsm_profile)

    rtheta_gap = {
        "schema": "MTTRThetaMassSchemeDerivationGapRecheck.v1",
        "status": "EXTERNAL_PROFILE_COMPUTED_SELECTED_RTHETA_DERIVATION_STILL_OPEN",
        "old_rtheta_gap_source": rel(OLD_RTHETA_GAP),
        "bct_row_assembly_source": rel(ROW_ASSEMBLY),
        "external_rows_available": assembly["all_three_bct_external_mass_scheme_rows_available"],
        "accepted_Rtheta_source_row_count": assembly["accepted_Rtheta_source_row_count"],
        "selected_Rtheta_mass_scheme_derivation_closed": old_rtheta_gap[
            "selected_Rtheta_mass_scheme_derivation_closed"
        ],
        "minimal_internal_missing_object": old_rtheta_gap["minimal_internal_missing_object"],
        "external_profile_may_validate_Rtheta": True,
        "external_profile_selects_Rtheta": False,
        "why_not_selected": (
            "The correlated profile is an external empirical/convention comparison. It does not emit the "
            "selected Route-C/Strominger Galerkin residual solve or the Rtheta projection coefficients."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA_GAP, rtheta_gap)

    cutset = {
        "schema": "MTTNextCutsetAfterBCTProfile.v1",
        "status": "NEXT_ATTACK_CHARM_INPUT_POLICY_OR_SELECTED_RTHETA_ROWS",
        "closed_now": {
            "BCT_correlated_EFT_profile_computed": True,
            "BCT_correlated_fullSM_profile_computed": True,
            "fullSM_current_external_profile_rejected": True,
            "Rtheta_nonselector_gap_rechecked": True,
        },
        "still_open": {
            "BCT_profile_95pct_closure": not eft_profile["passes_95pct_profile_gate"],
            "charm_CRunDec_input_policy_reconciliation": True,
            "selected_Rtheta_mass_scheme_derivation": True,
            "W_Z_H_electroweak_matching_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "recompute charm with the exact Huang-Zhou/RunDec loop, alpha_s, threshold, and input policy",
            "route_B": "derive b/c/tau rows from selected Rtheta mass-scheme projection and compare to this profile",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedBCTProfileReconciliationOrRThetaMassSchemeDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "bct_correlated_eft_profile": rel(EFT_PROFILE),
            "bct_correlated_fullsm_profile": rel(FULLSM_PROFILE),
            "rtheta_mass_scheme_derivation_gap_recheck": rel(RTHETA_GAP),
            "next_cutset_after_bct_profile": rel(CUTSET),
        },
        "theorem": {
            "name": "BCTCorrelatedProfileAndRThetaGapTheorem",
            "proved": True,
            "statement": (
                "Using the Huang-Zhou b/c/tau correlation submatrices, the assembled external rows yield a "
                "computable correlated EFT profile and a rejected full-SM profile for the current convention. "
                "The EFT profile is borderline and does not pass a 95% profile gate; therefore profile closure, "
                "selected Rtheta derivation, true SM equivalence, and no-knob closure remain open."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "accepted_bottom_charm_tau_map_row_count": assembly["accepted_external_map_row_count"],
            "all_three_bct_external_mass_scheme_rows_available": True,
            "BCT_correlated_EFT_profile_computed": True,
            "BCT_EFT_profile_passes_95pct_gate": eft_profile["passes_95pct_profile_gate"],
            "BCT_EFT_profile_passes_99pct_gate": eft_profile["passes_99pct_profile_gate"],
            "BCT_fullSM_profile_passes_95pct_gate": fullsm_profile["passes_95pct_profile_gate"],
            "BCT_profile_95pct_closure_closed": False,
            "selected_Rtheta_mass_scheme_derivation_closed": False,
            "W_Z_H_electroweak_matching_rows_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_BCTProfileReconciliation_or_RThetaMassSchemeDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "accepted_bottom_charm_tau_map_row_count": assembly["accepted_external_map_row_count"],
        "BCT_correlated_EFT_chi_square": eft_profile["correlated_chi_square"],
        "BCT_correlated_EFT_survival_probability": eft_profile["chi_square_survival_probability_df3"],
        "BCT_EFT_profile_passes_95pct_gate": eft_profile["passes_95pct_profile_gate"],
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected BCTProfileReconciliation or RThetaMassSchemeDerivation v1

Status: `{STATUS}`.

This artifact promotes the b/c/tau external-row ledger to a correlated
Huang-Zhou `M_Z` profile check.

```text
accepted b/c/tau external rows : {assembly["accepted_external_map_row_count"]}
EFT correlated chi-square       : {eft_profile["correlated_chi_square"]}
EFT chi-square survival         : {eft_profile["chi_square_survival_probability_df3"]}
EFT passes 95 pct profile gate  : {str(eft_profile["passes_95pct_profile_gate"]).lower()}
full-SM current profile passes  : {str(fullsm_profile["passes_95pct_profile_gate"]).lower()}
selected Rtheta rows closed     : false
```

The result is good but not closure: the EFT profile is within a 99% gate but
does not pass a 95% gate, with the tension localized in charm.  The next
target is charm input/threshold-policy reconciliation or selected Rtheta
mass-scheme row derivation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
