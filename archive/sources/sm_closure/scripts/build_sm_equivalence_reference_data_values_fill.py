"""Build the first frozen measured-reference values packet for SM-equivalence."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

REGISTRY = DATA / "sm_equivalence_reference_source_registry.candidate.json"
MANIFEST = DATA / "sm_equivalence_measured_parameter_replay_manifest.candidate.json"

OUTPUT = DATA / "sm_equivalence_reference_data_values_fill.candidate.json"
CERT = CERTS / "sm_equivalence_reference_data_values_fill_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_Reference_Data_Values_Fill_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_REFERENCE_DATA_VALUES_FILL_BUILT_PARTIAL_REPLAY_SEED"
NEXT = "MTT_SM_Equivalence_Tree_Level_Replay_Seed_v1"

PDG_SQLITE_SHA256 = "3de494ba22d7229eda9ba3047660b345fd82d3eea0e10747b7119bb4c2947196"
SQRT2 = math.sqrt(2.0)


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def pdg_value(
    *,
    pdgid: str,
    observable: str,
    value: float,
    unit: str,
    err_plus: float,
    err_minus: float | None = None,
    display: str,
    comment: str | None = None,
    scheme: str = "PDG summary value; see observable-specific PDG convention",
    scale: str = "observable-specific",
) -> dict[str, Any]:
    return {
        "source_key": "PDG_2025",
        "source_version_or_date": "PDG 2025 update; pdg-2025-v0.2.2.sqlite",
        "source_hash_sha256": PDG_SQLITE_SHA256,
        "pdgid": pdgid,
        "observable_definition": observable,
        "central_value": value,
        "uncertainty": {
            "plus": err_plus,
            "minus": err_minus if err_minus is not None else err_plus,
            "type": "PDG summary uncertainty",
        },
        "units": unit,
        "display_value_text": display,
        "scheme": scheme,
        "scale": scale,
        "correlation_policy": "correlations not encoded in this first seed packet",
        "comment": comment,
        "used_as_source_selector": False,
    }


def codata_value(
    *,
    observable: str,
    value: float,
    unit: str,
    uncertainty: float,
    display: str,
    scheme: str,
    scale: str,
) -> dict[str, Any]:
    return {
        "source_key": "NIST_CODATA_2022",
        "source_version_or_date": "CODATA 2022 recommended values; NIST Web Version 9.0",
        "observable_definition": observable,
        "central_value": value,
        "uncertainty": {
            "plus": uncertainty,
            "minus": uncertainty,
            "type": "standard uncertainty",
        },
        "units": unit,
        "display_value_text": display,
        "scheme": scheme,
        "scale": scale,
        "correlation_policy": "CODATA correlations not encoded in this first seed packet",
        "used_as_source_selector": False,
    }


def mev_to_gev(value: dict[str, Any]) -> float:
    if value["units"] == "MeV":
        return value["central_value"] / 1000.0
    if value["units"] == "GeV":
        return value["central_value"]
    raise ValueError(f"Unsupported mass unit {value['units']}")


def sym_mass_unc_gev(value: dict[str, Any]) -> float:
    plus = value["uncertainty"]["plus"]
    minus = value["uncertainty"]["minus"]
    scale = 1000.0 if value["units"] == "MeV" else 1.0
    return max(abs(plus), abs(minus)) / scale


def yukawa_from_mass(mass: dict[str, Any], vev: dict[str, Any]) -> dict[str, Any]:
    mass_gev = mev_to_gev(mass)
    vev_value = vev["central_value"]
    y = SQRT2 * mass_gev / vev_value
    dm = sym_mass_unc_gev(mass)
    dv = vev["uncertainty"]["plus"]
    rel = math.sqrt((dm / mass_gev) ** 2 + (dv / vev_value) ** 2) if mass_gev else 0.0
    return {
        "source_key": "DERIVED_FROM_PDG_2025_AND_NIST_CODATA_2022",
        "observable_definition": f"diagonal Yukawa magnitude derived from {mass['observable_definition']}",
        "central_value": y,
        "uncertainty": {
            "plus": abs(y) * rel,
            "minus": abs(y) * rel,
            "type": "uncorrelated first-order propagation; correlations omitted",
        },
        "units": "dimensionless",
        "scheme": "tree-level SM relation y_f = sqrt(2) m_f / v",
        "scale": mass["scale"],
        "conversion_formula": "y_f = sqrt(2) m_f / v; v=(sqrt(2) G_F)^(-1/2)",
        "input_refs": [mass["observable_definition"], vev["observable_definition"]],
        "used_as_source_selector": False,
    }


def main() -> int:
    registry = load(REGISTRY)
    manifest = load(MANIFEST)

    masses = {
        "e": pdg_value(
            pdgid="S003M",
            observable="electron mass",
            value=0.51099895,
            unit="MeV",
            err_plus=1.5e-10,
            display="0.51099895000+-0.00000000015",
            scheme="pole/rest mass",
            scale="on shell",
        ),
        "mu": pdg_value(
            pdgid="S004M",
            observable="muon mass",
            value=105.6583755,
            unit="MeV",
            err_plus=2.3e-06,
            display="105.6583755+-0.0000023",
            scheme="pole/rest mass",
            scale="on shell",
        ),
        "tau": pdg_value(
            pdgid="S035M",
            observable="tau mass",
            value=1776.93246513409,
            unit="MeV",
            err_plus=0.08491495391323055,
            err_minus=0.08758019173411406,
            display="1776.93+-0.09",
            scheme="pole/rest mass",
            scale="on shell",
        ),
        "u": pdg_value(
            pdgid="Q002M",
            observable="u-quark mass",
            value=2.16,
            unit="MeV",
            err_plus=0.07,
            display="2.16+-0.07",
            scheme="MSbar running mass",
            scale="2 GeV",
        ),
        "d": pdg_value(
            pdgid="Q001M",
            observable="d-quark mass",
            value=4.7,
            unit="MeV",
            err_plus=0.07,
            display="4.70+-0.07",
            scheme="MSbar running mass",
            scale="2 GeV",
        ),
        "s": pdg_value(
            pdgid="Q003M",
            observable="s-quark mass",
            value=93.5,
            unit="MeV",
            err_plus=0.8,
            display="93.5+-0.8",
            scheme="MSbar running mass",
            scale="2 GeV",
        ),
        "c": pdg_value(
            pdgid="Q004M",
            observable="c-quark mass",
            value=1.273,
            unit="GeV",
            err_plus=0.0046,
            display="1.2730+-0.0046",
            scheme="MSbar running mass",
            scale="m_c",
        ),
        "b": pdg_value(
            pdgid="Q005M",
            observable="b-quark mass",
            value=4.183,
            unit="GeV",
            err_plus=0.007,
            display="4.183+-0.007",
            comment="of MSbar Mass.",
            scheme="MSbar running mass",
            scale="m_b",
        ),
        "t": pdg_value(
            pdgid="Q007TP",
            observable="t-quark mass direct measurements",
            value=172.5590883453979,
            unit="GeV",
            err_plus=0.3040826988999338,
            err_minus=0.3061998752861254,
            display="172.56+-0.31",
            scheme="direct top-mass combination; not a pure short-distance mass",
            scale="top direct measurement convention",
        ),
        "H": pdg_value(
            pdgid="S126M",
            observable="Higgs boson mass",
            value=125.1995304097179,
            unit="GeV",
            err_plus=0.1148838236816068,
            display="125.20+-0.11",
            scheme="pole mass summary",
            scale="on shell",
        ),
        "W": pdg_value(
            pdgid="S043M",
            observable="W boson mass",
            value=80.377,
            unit="GeV",
            err_plus=0.012,
            display="80.3692+-0.0133",
            comment="PDG row comment: (AMOROSO 2024); numeric column and display text differ in source row",
            scheme="PDG summary electroweak mass",
            scale="on shell",
        ),
        "Z": pdg_value(
            pdgid="S044M",
            observable="Z boson mass",
            value=91.18797809193725,
            unit="GeV",
            err_plus=0.002013761937203607,
            display="91.1880+-0.0020",
            scheme="PDG summary electroweak mass",
            scale="on shell",
        ),
    }

    constants = {
        "G_F": codata_value(
            observable="Fermi coupling constant",
            value=1.1663788e-5,
            unit="GeV^-2",
            uncertainty=6.0e-12,
            display="1.1663788(6)e-5 GeV^-2",
            scheme="CODATA electroweak low-energy constant",
            scale="muon decay normalization",
        ),
        "alpha": codata_value(
            observable="fine-structure constant",
            value=7.2973525643e-3,
            unit="dimensionless",
            uncertainty=1.1e-12,
            display="7.2973525643(11)e-3",
            scheme="CODATA low-energy alpha",
            scale="zero-momentum/atomic-physics convention",
        ),
    }
    v = 1.0 / math.sqrt(SQRT2 * constants["G_F"]["central_value"])
    # dv/v = 0.5 dG/G.
    dv = 0.5 * v * constants["G_F"]["uncertainty"]["plus"] / constants["G_F"]["central_value"]
    constants["v_from_G_F"] = {
        "source_key": "DERIVED_FROM_NIST_CODATA_2022",
        "observable_definition": "Higgs vacuum expectation value from Fermi constant",
        "central_value": v,
        "uncertainty": {"plus": dv, "minus": dv, "type": "first-order propagation from G_F"},
        "units": "GeV",
        "display_value_text": f"{v:.12g} GeV",
        "scheme": "tree-level SM relation v=(sqrt(2) G_F)^(-1/2)",
        "scale": "muon decay normalization",
        "conversion_formula": "v=(sqrt(2) G_F)^(-1/2)",
        "used_as_source_selector": False,
    }

    diagonal_yukawas = {
        name: yukawa_from_mass(masses[name], constants["v_from_G_F"])
        for name in ["u", "c", "t", "d", "s", "b", "e", "mu", "tau"]
    }

    slot_values = {
        "higgs.v_mh_lambda_or_potential": {
            "status": "PARTIAL_FILLED",
            "filled_values": {
                "m_H": masses["H"],
                "v_from_G_F": constants["v_from_G_F"],
            },
            "open_values": ["Higgs quartic lambda after scheme/scale declaration", "Higgs mass RG matching"],
        },
        "yukawa.Y_u_Y_d_Y_e": {
            "status": "PARTIAL_FILLED_DIAGONAL_MAGNITUDE_SEED",
            "basis_convention": "diagonal mass basis; CKM/PMNS off-diagonal data not filled here",
            "filled_values": {
                "masses": {key: masses[key] for key in ["u", "c", "t", "d", "s", "b", "e", "mu", "tau"]},
                "diagonal_yukawa_magnitudes": diagonal_yukawas,
            },
            "open_values": [
                "full complex Yukawa matrices",
                "basis transformation convention",
                "CKM/PMNS-carrying off-diagonal structure",
                "RG transport to common scale",
            ],
        },
        "gauge.alpha_1_alpha_2_alpha_3": {
            "status": "PARTIAL_FILLED_LOW_ENERGY_ANCHORS_ONLY",
            "filled_values": {
                "alpha_low_energy": constants["alpha"],
                "m_W": masses["W"],
                "m_Z": masses["Z"],
            },
            "open_values": [
                "alpha_1(M_Z) in declared GUT or SM normalization",
                "alpha_2(M_Z)",
                "alpha_3(M_Z)",
                "sin^2(theta_W) scheme",
                "RG scheme/correlation packet",
            ],
        },
        "mixing.CKM": {
            "status": "OPEN_NOT_FILLED_IN_FIRST_PACKET",
            "reason": "requires a convention-complete CKM source row or PDG review table extraction with correlations",
        },
        "mixing.PMNS": {
            "status": "OPEN_NOT_FILLED_IN_FIRST_PACKET",
            "reason": "requires NuFIT/PDG convention, ordering, phases, and covariance policy",
        },
        "neutrino.yukawa_or_mass_splittings": {
            "status": "OPEN_NOT_FILLED_IN_FIRST_PACKET",
            "reason": "requires absolute-mass policy before Dirac Yukawa magnitudes can be reconstructed",
        },
    }

    candidate = {
        "candidate": "MTTSMEquivalenceReferenceDataValuesFill",
        "status": STATUS,
        "inputs": {
            "reference_source_registry": rel(REGISTRY),
            "measured_parameter_replay_manifest": rel(MANIFEST),
        },
        "retrieval_date": "2026-05-25",
        "source_boundary_preserved": True,
        "superset_strategy_use": registry["superset_strategy_use"],
        "reference_values": {
            "masses": masses,
            "constants": constants,
            "diagonal_yukawa_magnitudes": diagonal_yukawas,
        },
        "slot_values": slot_values,
        "conversion_formulas": {
            "mass_unit_conversion": "1 GeV = 1000 MeV",
            "vev_from_fermi_constant": "v=(sqrt(2) G_F)^(-1/2)",
            "tree_level_yukawa_magnitude": "y_f=sqrt(2) m_f/v",
            "higgs_quartic_tree_level_pending": "lambda=m_H^2/(2 v^2), intentionally delayed until Higgs potential convention is frozen",
        },
        "quality_flags": {
            "values_filled": True,
            "partial_packet": True,
            "all_values_have_sources": True,
            "all_filled_values_have_units": True,
            "all_filled_values_have_uncertainty": True,
            "all_filled_values_have_scheme_or_scale": True,
            "correlation_matrices_included": False,
            "common_RG_scale_transport_done": False,
            "full_complex_Yukawa_matrices_filled": False,
            "CKM_filled": False,
            "PMNS_filled": False,
            "gauge_running_triplet_filled": False,
        },
        "what_closes_now": {
            "first_reference_values_packet_frozen": True,
            "charged_fermion_and_quark_mass_seed_filled": True,
            "Higgs_W_Z_mass_seed_filled": True,
            "CODATA_alpha_and_G_F_anchor_filled": True,
            "tree_level_diagonal_yukawa_seed_computed": True,
            "source_selection_guardrails_preserved": True,
        },
        "what_remains_open": {
            "full_CKM_reference_packet": True,
            "full_PMNS_and_neutrino_reference_packet": True,
            "gauge_running_triplet_alpha1_alpha2_alpha3": True,
            "common_RG_scale_transport": True,
            "full_complex_Yukawa_matrices": True,
            "numeric_tree_level_replay": True,
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
            "name": "SMEquivalenceReferenceDataValuesFillTheorem",
            "proved": True,
            "statement": (
                "A first versioned measured-reference packet is frozen for SM-equivalence replay. "
                "It supplies PDG 2025 mass seeds, CODATA 2022 alpha/G_F anchors, v from G_F, and "
                "tree-level diagonal Yukawa magnitudes. It is partial: CKM, PMNS, full gauge-running "
                "triplet, common RG transport, and full complex Yukawa matrices remain open. No value "
                "is used to select MTT source data."
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

    note = f"""# MTT SM-Equivalence Reference Data Values Fill v1

Status: `{STATUS}`.

## Result

The first frozen measured-reference packet is built.  It fills PDG 2025 mass
seeds, CODATA 2022 `alpha` and `G_F`, derives `v=(sqrt(2)G_F)^(-1/2)`, and
computes tree-level diagonal Yukawa magnitudes.

This is intentionally partial.  It does not yet fill CKM, PMNS, the full
`alpha_1, alpha_2, alpha_3` running triplet, RG transport to a common scale, or
full complex Yukawa matrices.

## Guardrail

The filled values are downstream SM-equivalence inputs only.  They do not select
source structure, topology, branch, dynamic overlap tensor, `A_selected`,
`b_selected`, or no-knob kernels.

## Next

Build `{NEXT}`: run the first tree-level replay from the frozen seed values and
identify the exact remaining convention packets needed for full SM-equivalence.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
