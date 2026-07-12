from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_officialjointlikelihoodtransport_or_declareddiagonalprofilefinality"
OUT = ROOT / "candidate_data" / SLUG


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    raw = load("candidate_data/selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood/smdr_multiloop_common_source_transport.raw.json")
    multiloop = load("certificates/selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood_certificate.json")
    ledger = load("candidate_data/selected_strictnoknobupgradeledger_aftertruesmequivalence/strict_no_knob_upgrade_ledger.packet.json")

    source_ids = [row["id"] for row in raw["source_inputs"]]
    partitions = [
        {
            "id": "collider_and_PDG_pole_masses",
            "coordinates": ["SMDR_Mt_pole", "SMDR_Mh_pole", "SMDR_MZ_PDG", "SMDR_Mtau_pole"],
            "authority": "Particle Data Group and underlying collider combinations",
            "url": "https://pdg.lbl.gov/2025/index.html",
        },
        {
            "id": "QCD_and_hadronic_inputs",
            "coordinates": ["SMDR_alphaS_5_MZ", "SMDR_Delta_alpha_had_5_MZ_in", "SMDR_mbmb", "SMDR_mcmc", "SMDR_ms_2GeV", "SMDR_md_2GeV", "SMDR_mu_2GeV"],
            "authority": "Particle Data Group/lattice-QCD averages and SMDR reference nuisance convention",
            "url": "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-quark-masses.pdf",
        },
        {
            "id": "CODATA_adjusted_constants",
            "coordinates": ["SMDR_alpha", "SMDR_GFermi", "SMDR_Mmuon_pole", "SMDR_Melectron_pole"],
            "authority": "NIST 2022 CODATA adjusted constants",
            "url": "https://physics.nist.gov/cuu/Constants/index.html",
        },
    ]
    covered = sorted(coordinate for block in partitions for coordinate in block["coordinates"])
    if covered != sorted(source_ids):
        raise ValueError("source partition is incomplete")

    packet = {
        "schema": "MTTOfficialJointLikelihoodTransportOrDeclaredDiagonalProfileFinality.v1",
        "status": "SOURCE_BLOCK_AUDIT_CLOSED_UNIFIED_OFFICIAL_15D_LIKELIHOOD_NOT_PUBLICLY_IDENTIFIED",
        "audit_date": "2026-07-11",
        "source_coordinate_count": len(source_ids),
        "source_partitions": partitions,
        "public_source_findings": {
            "NIST_CODATA_pairwise_correlation_service_exists": True,
            "PDG_uses_correlations_inside_specific_averages": True,
            "single_versioned_joint_15_coordinate_likelihood_identified": False,
            "cross_authority_covariances_published_as_one_object": False,
            "source_block_independence_proved_by_authorities": False,
        },
        "transport_state": {
            "SMDR_multiloop_transport_closed": multiloop["multiloop_threshold_mass_scheme_transport_closed"],
            "frozen_Jacobian_shape": [8, 15],
            "output_covariance_shape": [8, 8],
            "output_covariance_positive_definite": multiloop["full_8x8_multiloop_covariance_positive_definite"],
            "symmetric_entries": multiloop["symmetric_unique_entries_determined"],
            "BCT_WZH_cross_entries": multiloop["BCT_WZH_cross_entries_determined"],
        },
        "decision": {
            "declared_diagonal_source_profile_is_reproducible_baseline": True,
            "declared_diagonal_source_profile_is_official_joint_likelihood": False,
            "invent_unpublished_cross_authority_correlations": False,
            "official_joint_likelihood_strict_upgrade_closed": False,
            "U3_executable_local_work_exhausted_without_new_external_dataset": True,
            "next_active_upgrade": "U2_literal_global_Cech_HYM_QaSU3",
        },
        "replacement_rule": "If a versioned joint or block covariance is supplied, validate its coordinate map and positive semidefiniteness, then replace C_source in C_out = J C_source J^T without changing the frozen SMDR map.",
        "ledger_consistency": {
            "strict_upgrade_count": ledger["upgrade_count"],
            "U3_remains_partially_closed": True,
        },
    }
    dump(OUT / "official_joint_source_block_audit.packet.json", packet)

    status = "MTT_SELECTED_OFFICIALJOINTLIKELIHOODTRANSPORT_SOURCEBLOCK_AUDIT_CLOSED_EXTERNAL_DATASET_OPEN"
    candidate = {
        "candidate": "MTT_Selected_OfficialJointLikelihoodTransport_or_DeclaredDiagonalProfileFinality_v1",
        "status": status,
        "date": "2026-07-11",
        "closure_claimed": True,
        "theorem": {
            "name": "HeterogeneousSourceLikelihoodNonPromotionTheorem",
            "proved": True,
            "statement": "The 15-coordinate SMDR source vector is a product of at least three authority domains. No single public versioned 15-dimensional joint likelihood was identified, and cross-authority independence is not itself an official theorem. Therefore the diagonal source profile is the reproducible declared baseline but cannot be relabeled an official joint likelihood. Future covariance data can be propagated through the frozen Jacobian without rebuilding the transport.",
        },
        "official_joint_likelihood_closed": False,
        "declared_diagonal_profile_finality_closed": True,
        "next_required_artifact": "MTT_Selected_LiteralGoodCoverCechHYMGlobalWitness_AfterDeclaredProfileFinality_v1",
    }
    dump(ROOT / "candidate_data" / f"{SLUG}.candidate.json", candidate)

    certificate = {
        "certificate": "MTT_Selected_OfficialJointLikelihoodTransport_or_DeclaredDiagonalProfileFinality_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": status,
        "theorem_proved": True,
        "source_coordinates_partitioned": 15,
        "source_authority_blocks": 3,
        "frozen_transport_Jacobian_ready": True,
        "declared_diagonal_profile_finality_closed": True,
        "official_joint_likelihood_closed": False,
        "unpublished_cross_correlations_invented": False,
        "U3_local_execution_exhausted": True,
        "next_active_upgrade": "U2_literal_global_Cech_HYM_QaSU3",
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(ROOT / "certificates" / f"{SLUG}_certificate.json", certificate)


if __name__ == "__main__":
    main()
