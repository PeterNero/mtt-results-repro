"""Build CONST-EM-01 alpha1 convention map.

The QA replay closes the source-side driver.  This artifact constructs the
electroweak convention bridge and exposes every remaining normalization or
running slot before a physical alpha value may be claimed.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_convention_map"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FORMULA_MAP = BASE / "electroweak_formula_map.packet.json"
NORMALIZATION = BASE / "normalization_slots.packet.json"
COMPARISON = BASE / "comparison_protocol.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_ConventionMap_v1.md"

QA_REPLAY = DATA / "const_em_01_alpha1_qa_replay.candidate.json"
STATUS = "MTT_CONST_EM_01_ALPHA1_CONVENTION_MAP_BUILT_NUMERICAL_ALPHA_OPEN"


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
    qa = load(QA_REPLAY)
    source_side_ready = qa["what_closes_now"]["source_side_alpha1_driver_accepted_here"] is True

    formula_map = {
        "schema": "MTTConstEM01ElectroweakFormulaMap.v1",
        "status": "FORMULA_MAP_BUILT_VALUE_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP",
        "source_input": {
            "N_alpha1_h_ext": 1.0,
            "lambda_alpha1": 1.0,
            "du_dalpha1": "h_ext",
            "source_side_ready": source_side_ready,
            "source": rel(QA_REPLAY),
        },
        "convention_equations": {
            "hypercharge_alpha": "alpha_Y(mu) = g_prime(mu)^2/(4*pi)",
            "GUT_normalized_alpha1": "alpha_1^GUT(mu) = (5/3) alpha_Y(mu)",
            "inverse_tree_electromagnetic": "1/alpha_em(mu) = 1/alpha_Y(mu) + 1/alpha_2(mu)",
            "direct_tree_electromagnetic": "alpha_em(mu) = alpha_Y(mu)*alpha_2(mu)/(alpha_Y(mu)+alpha_2(mu))",
            "weak_mixing": "sin^2(theta_W)(mu) = alpha_Y(mu)/(alpha_Y(mu)+alpha_2(mu))",
            "low_energy_comparison": "alpha(0) requires running alpha_em(mu)->alpha_em(0) with leptonic, perturbative, hadronic, and threshold terms",
            "MZ_comparison": "alpha(M_Z) requires a declared electroweak input scheme and vacuum-polarization profile at mu=M_Z",
        },
        "source_to_convention_symbols": {
            "alpha_Y(mu_source)": "C_Y(mu_source) * N_alpha1(h_ext)",
            "alpha_1^GUT(mu_source)": "(5/3) * C_Y(mu_source) * N_alpha1(h_ext)",
            "alpha_em(mu_source)": "C_Y*N_alpha1 * alpha_2 / (C_Y*N_alpha1 + alpha_2)",
            "alpha_em(mu_target)": "Run[alpha_em(mu_source), source_scale -> mu_target, thresholds]",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    normalization = {
        "schema": "MTTConstEM01NormalizationSlots.v1",
        "status": "NORMALIZATION_SLOTS_EXPOSED_VALUE_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP",
        "closed_slots": {
            "source_side_N_alpha1_h_ext": source_side_ready,
            "source_side_lambda_alpha1": source_side_ready,
            "source_side_du_dalpha1_h_ext": source_side_ready,
        },
        "open_slots": {
            "C_Y_source_to_hypercharge_coupling": {
                "needed_for": "turn source-side alpha1 unit into alpha_Y at a declared source scale",
                "may_be_universal_parameter": True,
                "selected_now": False,
                "allowed_to_fit_from_alpha": False,
            },
            "alpha_2_or_SU2_source_driver": {
                "needed_for": "tree electroweak mixing to alpha_em",
                "may_use_SM_parity_measured_input": True,
                "no_knob_source_derivation_open": True,
            },
            "source_scale_mu_source": {
                "needed_for": "running to M_Z or 0",
                "selected_now": False,
            },
            "threshold_running_operator": {
                "needed_for": "transport alpha_em between scales",
                "requires_hadronic_vacuum_polarization_policy": True,
            },
            "comparison_profile": {
                "needed_for": "credible comparison with PDG-style values and uncertainties",
                "selected_now": False,
            },
        },
        "universal_parameter_policy": {
            "selected_universal_parameters_now": 0,
            "candidate_if_unavoidable": "one absolute gauge/action normalization C_Y or a shared gauge-normalization scale",
            "credibility_rule": "Declare it as universal only if it is shared across sectors and selected independently of the measured alpha target.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    comparison = {
        "schema": "MTTConstEM01AlphaComparisonProtocol.v1",
        "status": "COMPARISON_PROTOCOL_BUILT_VALUES_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP",
        "allowed_modes": {
            "SM_parity_replay": {
                "description": "Use measured alpha, alpha_2, masses, and thresholds as downstream replay inputs only.",
                "source_selector_allowed": False,
                "can_check_framework_consistency": True,
            },
            "no_knob_derivation": {
                "description": "Derive C_Y, alpha_2/source driver, source scale, and running operator from selected MTT data before comparing to measured values.",
                "source_selector_allowed": False,
                "can_claim_constant_derivation": True,
            },
            "one_to_three_universal_parameters": {
                "description": "If zero-parameter closure fails, allow only universal constants selected independently and shared across sectors.",
                "source_selector_allowed": False,
                "can_claim_reduced_parameter_theory": True,
            },
        },
        "blocked_modes": {
            "backfit_alpha_to_C_Y": "Would turn measured alpha into a source selector.",
            "identify_N_alpha1_with_alpha_em": "Conflates source coordinate with observable electromagnetic coupling.",
            "ignore_running_and_thresholds": "Would compare values at incompatible scales/schemes.",
        },
        "external_guardrail_sources": [
            "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf",
            "https://arxiv.org/abs/1910.09525",
            "https://arxiv.org/abs/1706.09436",
            "https://www.sciencedirect.com/science/article/pii/S055032130800641X",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterConstEM01ConventionMap.v1",
        "status": "NEXT_WORKORDER_NORMALIZATION_SLOT_SEARCH",
        "primary": {
            "label": "CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY",
            "task": "Search corpus/repos for a selected gauge/action normalization C_Y that maps source-side N_alpha1(h_ext)=1 to hypercharge alpha_Y without using measured alpha as selector.",
        },
        "secondary": {
            "label": "CONST-EM-01 / ALPHA1-SU2-MIXING / A4-SHARED-GAUGE-PACKET",
            "task": "Import or derive the SU2 source driver and shared gauge packet required for alpha_em = alpha_Y alpha_2/(alpha_Y+alpha_2).",
        },
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1ConventionMap",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP",
        "output_packets": {
            "electroweak_formula_map": rel(FORMULA_MAP),
            "normalization_slots": rel(NORMALIZATION),
            "comparison_protocol": rel(COMPARISON),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "source_to_observable_formula_map_built": True,
            "hypercharge_GUT_and_em_alpha_conventions_separated": True,
            "normalization_slots_exposed": True,
            "allowed_vs_blocked_comparison_modes_declared": True,
            "source_side_alpha1_driver_preserved": source_side_ready,
        },
        "what_remains_open": {
            "C_Y_source_to_hypercharge_coupling": True,
            "SU2_alpha2_source_driver_or_replay_input": True,
            "source_scale_mu_source": True,
            "threshold_running_operator": True,
            "alpha_zero_value": True,
            "alpha_MZ_value": True,
            "no_knob_fine_structure_constant_derivation": True,
        },
        "theorem": {
            "name": "CONSTEM01Alpha1ConventionMapSeparationTheorem",
            "proved": True,
            "statement": (
                "Given the source-side QA replay N_alpha1(h_ext)=1, the observable electromagnetic alpha is not the same object. "
                "A comparison requires a selected hypercharge normalization C_Y, an SU2 coupling/source input, a scale, "
                "and a running/threshold operator.  The tree convention layer is alpha_Y=C_Y*N_alpha1, "
                "alpha_1^GUT=(5/3)alpha_Y, and alpha_em=alpha_Y alpha_2/(alpha_Y+alpha_2)."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_ConventionMap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "formula_map_built": True,
        "physical_alpha_value_claimed": False,
        "selected_universal_parameters_now": 0,
        "next_primary": "CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Convention Map v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP`

## Result

The source-side alpha1 result is now separated from the observable
electromagnetic coupling conventions.

Closed source-side input:

- `N_alpha1(h_ext)=1`,
- `lambda_alpha1=1`,
- `du/dalpha1=h_ext`.

Convention bridge:

- `alpha_Y(mu) = g_prime(mu)^2/(4*pi)`,
- `alpha_1^GUT(mu) = (5/3) alpha_Y(mu)`,
- `alpha_em(mu) = alpha_Y(mu) alpha_2(mu)/(alpha_Y(mu)+alpha_2(mu))`.

MTT source-to-convention slot:

- `alpha_Y(mu_source) = C_Y(mu_source) * N_alpha1(h_ext)`.

Thus the next missing object is not another alpha1 source-side proof.  It is
the selected normalization `C_Y`, plus the SU2/mixing and running machinery.

## Superset Use

This step uses a straight electroweak convention map, constrained by the
superset source result already obtained from QA-SU3/Chern-Weil/dotD routes.
The combined source route is locked to the source coordinate; the electroweak
map prevents it from being over-read as a measured fine-structure value.

## Open

- `C_Y` source-to-hypercharge normalization,
- `alpha_2` or selected SU2 source driver,
- source scale,
- threshold/running operator,
- hadronic vacuum-polarization policy,
- `alpha(0)` and `alpha(M_Z)` numerical comparisons.

No observed value is used as a selector and no universal parameter is selected.

## Next

Next label: `CONST-EM-01 / ALPHA1-NORMALIZATION / A3-FIND-CY`
"""

    for path, payload in [
        (FORMULA_MAP, formula_map),
        (NORMALIZATION, normalization),
        (COMPARISON, comparison),
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
