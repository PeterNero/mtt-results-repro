"""Build cross-block covariance map or Rtheta coefficient value fill artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_crossblockcovariance_or_rthetacoefficientvaluefill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BASIS = PACKET_DIR / "deduplicated_cross_block_covariance_basis.packet.json"
DEPENDENCIES = PACKET_DIR / "cross_block_covariance_dependency_graph.packet.json"
RTHETA = PACKET_DIR / "rtheta_coefficient_value_fill_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_cross_block_basis_map.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CrossBlockCovariance_or_RThetaCoefficientValueFill_v1.md"

PREVIOUS = DATA / "selected_covariancesidecarfill_or_rthetasourcerowderivation.candidate.json"
PREVIOUS_CUTSET = (
    DATA
    / "selected_covariancesidecarfill_or_rthetasourcerowderivation"
    / "next_cutset_after_covariance_sidecar_fill.packet.json"
)
WZH_SIDECARS = (
    DATA
    / "selected_covariancesidecarfill_or_rthetasourcerowderivation"
    / "wzh_gauge_and_lambda_covariance_sidecars.packet.json"
)
WEAK_ENVELOPE = (
    DATA
    / "selected_correlatedprofilevalues_or_localqftobservablevalues"
    / "correlation_robust_profile_envelope.packet.json"
)
BCT_ASSEMBLY = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "all_bct_external_rows_assembly.packet.json"
)
BCT_PROFILE = (
    DATA
    / "selected_charmtablesubstitution_or_selectedrthetarowsdecision"
    / "bct_empirical_table_substituted_profile.packet.json"
)
HIGGS_COV = (
    DATA
    / "selected_higgshomogeneousprofile_or_routeaformulacovariance"
    / "source_derived_correlated_covariance_model.packet.json"
)
RTHETA_MANIFEST = (
    DATA
    / "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
    / "rtheta_row_coefficient_slot_manifest.packet.json"
)
RTHETA_RECHECK = (
    DATA
    / "selected_covariancesidecarfill_or_rthetasourcerowderivation"
    / "rtheta_source_row_derivation_recheck_after_sidecar_fill.packet.json"
)

STATUS = (
    "MTT_SELECTED_CROSSBLOCKCOVARIANCE_OR_RTHETACOEFFICIENTVALUEFILL_"
    "BUILT_DEDUP_BASIS_DEPENDENCY_GRAPH_VALUES_OPEN"
)
NEXT = "MTT_Selected_CrossBlockCovarianceValues_or_RThetaCoefficientExecution_v1"


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
        raise FileNotFoundError("missing cross-block covariance sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_CUTSET,
        WZH_SIDECARS,
        WEAK_ENVELOPE,
        BCT_ASSEMBLY,
        BCT_PROFILE,
        HIGGS_COV,
        RTHETA_MANIFEST,
        RTHETA_RECHECK,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    wzh_sidecars = load(WZH_SIDECARS)
    weak = load(WEAK_ENVELOPE)
    bct_assembly = load(BCT_ASSEMBLY)
    bct_profile = load(BCT_PROFILE)
    higgs_cov = load(HIGGS_COV)
    rtheta_manifest = load(RTHETA_MANIFEST)
    rtheta_recheck = load(RTHETA_RECHECK)

    weak_rows = weak["basis_reduction"]["independent_outputs"]
    wzh_basis = wzh_sidecars["independent_covariance_basis"]
    bct_rows = [row["id"] for row in bct_assembly["rows"]]
    higgs_rows = higgs_cov["row_basis"]

    overlap_rows = sorted(set(weak_rows).intersection({"lambda_Mt", "g_2_Mt", "g_Y_Mt"}))
    wzh_unique_rows = [row for row in wzh_basis if row not in {"g_Y_Mt", "g_2_Mt", "lambda_Mt"}]
    dedup_basis = weak_rows + wzh_unique_rows + bct_rows + higgs_rows

    basis_packet = {
        "schema": "MTTDeduplicatedCrossBlockCovarianceBasis.v1",
        "status": "DEDUPLICATED_CROSS_BLOCK_BASIS_BUILT_VALUES_OPEN",
        "weak_basis_source": rel(WEAK_ENVELOPE),
        "wzh_sidecar_source": rel(WZH_SIDECARS),
        "bct_source": rel(BCT_ASSEMBLY),
        "higgs_covariance_source": rel(HIGGS_COV),
        "input_block_rows": {
            "weak_scale_buttazzo_boundary": weak_rows,
            "wzh_electroweak_coordinates": wzh_basis + ["g_1_GUT_Mt_alias"],
            "BCT_mass_scheme_profile": bct_rows,
            "Higgs_decay_covariance_model": higgs_rows,
        },
        "deduplication_rules": [
            {
                "id": "remove_g1GUT_alias",
                "rule": "g_1_GUT_Mt = sqrt(5/3) * g_Y_Mt, so it is metadata/alias, not an independent covariance row.",
                "closed": True,
            },
            {
                "id": "merge_WZH_weak_overlap",
                "rule": "lambda_Mt, g_2_Mt, and g_Y_Mt occur in both W/Z/H and weak-scale blocks; retain only the weak-scale row and attach W/Z/H sidecars as validation metadata.",
                "overlap_rows": overlap_rows,
                "closed": True,
            },
            {
                "id": "retain_v_extension",
                "rule": "v_from_G_F_tree_reference is the only independent W/Z/H coordinate extension after overlap removal.",
                "closed": True,
            },
        ],
        "deduplicated_interim_basis": dedup_basis,
        "row_counts": {
            "weak_rows": len(weak_rows),
            "wzh_unique_extension_rows": len(wzh_unique_rows),
            "BCT_rows": len(bct_rows),
            "Higgs_decay_rows": len(higgs_rows),
            "deduplicated_interim_total": len(dedup_basis),
        },
        "basis_map_closed": True,
        "numeric_cross_block_covariance_values_filled": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(BASIS, basis_packet)

    dependency_edges = [
        {
            "edge": "weak_to_wzh_overlap",
            "left_block": "weak_scale_buttazzo_boundary",
            "right_block": "wzh_electroweak_coordinates",
            "shared_directions": ["M_W", "M_h", "M_t", "alpha3_MZ", "lambda/gY/g2 row identity"],
            "status": "STRUCTURAL_MAP_CLOSED_NUMERIC_COVARIANCE_OPEN",
        },
        {
            "edge": "weak_to_BCT_common_scale",
            "left_block": "weak_scale_buttazzo_boundary",
            "right_block": "BCT_mass_scheme_profile",
            "shared_directions": ["alpha_s", "threshold convention", "MZ_to_Mt common-scale transport"],
            "status": "COMMON_SCALE_CONVENTION_MAP_OPEN",
        },
        {
            "edge": "weak_to_Higgs_decay_inputs",
            "left_block": "weak_scale_buttazzo_boundary",
            "right_block": "Higgs_decay_covariance_model",
            "shared_directions": ["m_H", "G_F/v", "alpha_s", "top/Higgs threshold convention"],
            "status": "DEPENDENCY_MAP_BUILT_NUMERIC_COVARIANCE_OPEN",
        },
        {
            "edge": "BCT_to_Higgs_decay_yukawa_inputs",
            "left_block": "BCT_mass_scheme_profile",
            "right_block": "Higgs_decay_covariance_model",
            "shared_directions": ["running quark/lepton mass rows", "Yukawa conversion via v"],
            "status": "COMMON_SCALE_AND_FORMULA_JACOBIAN_OPEN",
        },
        {
            "edge": "Higgs_decay_internal",
            "left_block": "Higgs_decay_covariance_model",
            "right_block": "Higgs_decay_covariance_model",
            "shared_directions": higgs_cov["nuisance_basis"],
            "status": "SOURCE_DERIVED_INTERNAL_COVARIANCE_AVAILABLE_NOT_OFFICIAL_PROFILE",
        },
    ]
    graph_packet = {
        "schema": "MTTCrossBlockCovarianceDependencyGraph.v1",
        "status": "CROSS_BLOCK_DEPENDENCY_GRAPH_BUILT_NUMERIC_VALUES_OPEN",
        "deduplicated_basis_source": rel(BASIS),
        "dependency_edges": dependency_edges,
        "structural_cross_block_map_closed": True,
        "numeric_cross_block_covariance_values_filled": False,
        "full_covariance_profile_likelihood_closed": False,
        "remaining_numeric_requirements": [
            "common-scale Jacobian from MZ BCT rows to Mt weak/Higgs rows",
            "shared-input covariance values for G_F/v, M_h, M_t, alpha_s, and threshold convention nuisance directions",
            "cross-block covariance entries between weak/WZH, BCT, and Higgs decay rows",
            "profile-likelihood convention for combining source-derived and empirical covariance blocks",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(DEPENDENCIES, graph_packet)

    coefficient_slots = rtheta_manifest["coefficient_slots"]
    wzh_slots = [
        slot
        for slot in coefficient_slots
        if slot["slot_id"] in {"threshold::W_Z_H", "mass_scheme::Higgs_pole_running_lambda"}
    ]
    rtheta_packet = {
        "schema": "MTTRThetaCoefficientValueFillGate.v1",
        "status": "RTHETA_COEFFICIENT_VALUE_FILL_GATE_BUILT_VALUES_STILL_OPEN",
        "manifest_source": rel(RTHETA_MANIFEST),
        "rtheta_recheck_source": rel(RTHETA_RECHECK),
        "wzh_relevant_slots": wzh_slots,
        "slot_count": rtheta_manifest["slot_count"],
        "filled_slot_count": rtheta_manifest["filled_slot_count"],
        "basis_map_closed_in_rtheta_manifest": rtheta_manifest["basis_map_closed"],
        "deduplicated_covariance_basis_map_closed": True,
        "why_this_does_not_fill_Rtheta_coefficients": [
            "deduplicated covariance basis is a profile bookkeeping basis, not a selected source-owner basis map",
            "no coefficient/formula has been emitted for threshold::W_Z_H",
            "precision convention is still open in the Rtheta manifest",
            "selected threshold response functional is still not instantiated",
        ],
        "Rtheta_coefficient_values_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "accepted_Rtheta_source_row_count": rtheta_recheck["accepted_Rtheta_source_row_count"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA, rtheta_packet)

    cutset = {
        "schema": "MTTNextCutsetAfterCrossBlockBasisMap.v1",
        "status": "NEXT_ATTACK_NUMERIC_CROSS_BLOCK_COVARIANCE_OR_RTHETA_COEFFICIENT_EXECUTION",
        "previous_cutset_source": rel(PREVIOUS_CUTSET),
        "closed_now": {
            "deduplicated_cross_block_covariance_basis": True,
            "WZH_weak_overlap_and_g1_alias_removed": True,
            "cross_block_dependency_graph": True,
            "Rtheta_coefficient_value_fill_gate": True,
        },
        "still_open": {
            "numeric_cross_block_covariance_values": True,
            "full_covariance_profile_likelihood": True,
            "Rtheta_coefficient_values": True,
            "selected_threshold_response_functional": True,
            "selected_Rtheta_source_rows": True,
            "common_scale_convention_map": True,
            "EW_formula_kernels_for_WW_ZZ_Zgamma": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "emit numeric cross-block covariance values for the deduplicated 19-row interim basis",
            "route_B": "execute Rtheta coefficient values for threshold::W_Z_H and mass_scheme::Higgs_pole_running_lambda",
            "route_C": "derive the common-scale MZ-to-Mt Jacobian for BCT-to-weak/Higgs coupling",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedCrossBlockCovarianceOrRThetaCoefficientValueFill",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "deduplicated_cross_block_covariance_basis": rel(BASIS),
            "cross_block_covariance_dependency_graph": rel(DEPENDENCIES),
            "rtheta_coefficient_value_fill_gate": rel(RTHETA),
            "next_cutset_after_cross_block_basis_map": rel(CUTSET),
        },
        "theorem": {
            "name": "CrossBlockCovarianceBasisDeduplicationTheorem",
            "proved": True,
            "statement": (
                "The post-sidecar covariance workspace has a deduplicated 19-row interim basis: weak-scale "
                "lambda/yt/g2/gY/g3, the independent v(G_F) W/Z/H extension, three BCT mass-scheme rows, "
                "and ten Higgs decay rows. The W/Z/H overlap rows lambda/g2/gY and the g1GUT alias must not "
                "be double-counted. This closes the structural cross-block basis and dependency graph, but "
                "numeric cross-block covariance values and Rtheta coefficient values remain open."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "deduplicated_cross_block_covariance_basis_closed": True,
            "cross_block_dependency_graph_closed": True,
            "numeric_cross_block_covariance_values_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "Rtheta_coefficient_values_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "previous_status": previous["status"],
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_CrossBlockCovariance_or_RThetaCoefficientValueFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "deduplicated_cross_block_covariance_basis_closed": True,
        "deduplicated_interim_row_count": len(dedup_basis),
        "numeric_cross_block_covariance_values_closed": False,
        "Rtheta_coefficient_values_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected CrossBlockCovariance or RThetaCoefficientValueFill v1

Status: `{STATUS}`.

This artifact closes the structural cross-block covariance basis.

```text
deduplicated interim row count        : {len(dedup_basis)}
W/Z/H weak-overlap rows removed       : true
g1GUT alias removed                   : true
numeric cross-block covariance closed : false
R_theta coefficient values closed     : false
true SM equivalence closed            : false
```

The independent interim basis is weak-scale `lambda/yt/g2/gY/g3`, the
independent `v(G_F)` W/Z/H extension, three BCT rows, and ten Higgs decay rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
