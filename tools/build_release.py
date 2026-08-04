"""Build the frozen A01-A62 baseline plus the current promoted result layer."""
from __future__ import annotations

import json
import re
import shutil
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "inventory"
ARCHIVE = ROOT / "archive" / "blobs"
RELEASE = ROOT / "release"
CURRENT_RESULT_CONFIG = ROOT / "config" / "current_results.json"
PAPER_CORPUS_LOCK = ROOT / "config" / "paper_corpus_lock.json"

DOMAIN_BY_ID = {
    **{f"A{i:02d}": "global_sm_equivalence" for i in range(1, 7)},
    "A07": "cech_hym_geometry",
    "A08": "q79_discrete_branch",
    "A09": "historical_baseline",
    "A10": "corpus_corrections",
    "A11": "q79_discrete_branch",
    "A12": "q79_discrete_branch",
    "A13": "protospinor_gr",
    "A14": "flavor_ckm",
    "A15": "cech_hym_geometry",
    "A16": "neutrino_strong_cp",
    "A17": "branch_selection",
    "A18": "quantization_qft",
    "A19": "cech_hym_geometry",
    **{f"A{i:02d}": "neutral_neutrino" for i in range(20, 44)},
    "A22": "strong_cp_anomaly",
    **{f"A{i:02d}": "generative_sm_finite_geometry" for i in range(44, 54)},
    **{f"A{i:02d}": "gauge_spectral_threshold" for i in range(54, 63)},
    **{f"A{i:02d}": "gauge_spectral_threshold" for i in range(63, 90)},
    "A90": "parameter_accounting",
    **{f"A{i:02d}": "neutral_neutrino" for i in range(91, 95)},
    "A95": "branch_selection",
    **{f"A{i:02d}": "strong_cp_axion" for i in range(96, 100)},
}

STATUS_TAGS = {
    "A01": ["PROFILE_REPLAY", "CURRENT_LOCK"],
    "A02": ["PROFILE_REPLAY", "NUMERIC_CERTIFIED"],
    "A03": ["CONDITIONAL", "IMPORTED_STANDARD_QFT"],
    "A04": ["PROFILE_REPLAY", "CLOSED_DECLARED_SCOPE"],
    "A05": ["OPEN", "STRICT_UPGRADE_LEDGER"],
    "A06": ["PROFILE_REPLAY", "DECLARED_FINAL_PROFILE"],
    "A07": ["DERIVED_EXACT", "SUPERSEDED_PARTIAL"],
    "A08": ["DERIVED_EXACT", "PROOF_HISTORY"],
    "A09": ["RETIRED", "HISTORICAL_GUARDRAIL"],
    "A10": ["AUDIT", "CORRECTION_AUTHORITY"],
    "A11": ["DERIVED_EXACT"],
    "A12": ["AUDIT", "CORRECTION_AUTHORITY"],
    "A13": ["DERIVED_EXACT", "OPEN_PHYSICAL_NORMALIZATION"],
    "A14": ["NUMERIC_CERTIFIED", "PROFILE_PREDICTION"],
    "A15": ["NUMERIC_CERTIFIED", "SUPERSEDED_PARTIAL"],
    "A16": ["CONDITIONAL", "OPEN"],
    "A17": ["DERIVED_EXACT", "OPEN_GLOBAL_UNIQUENESS"],
    "A18": ["CONDITIONAL", "OPEN"],
    "A19": ["DERIVED_EXACT", "NUMERIC_CERTIFIED"],
    "A20": ["CONDITIONAL", "OPEN_SOURCE_PROMOTION"],
    "A21": ["OPEN", "INTERMEDIATE"],
    "A22": ["DERIVED_EXACT", "OPEN_STRONG_CP_MAP"],
    "A23": ["OPEN", "INTERMEDIATE"],
    "A24": ["OPEN", "INTERMEDIATE"],
    "A25": ["OPEN", "INTERMEDIATE"],
    "A26": ["OPEN", "INTERMEDIATE"],
    "A27": ["OPEN", "INTERMEDIATE"],
    "A28": ["DERIVED_EXACT", "OPEN"],
    "A29": ["DERIVED_EXACT", "OPEN"],
    "A30": ["DERIVED_EXACT", "OPEN_PHYSICAL_NORMALIZATION"],
    "A31": ["NO_GO", "OPEN"],
    "A32": ["NO_GO", "OPEN"],
    "A33": ["DERIVED_EXACT", "OPEN"],
    "A34": ["DERIVED_EXACT", "PROFILE_REPLAY", "OPEN"],
    "A35": ["DERIVED_EXACT", "OPEN"],
    "A36": ["DERIVED_EXACT", "OPEN"],
    "A37": ["DERIVED_EXACT", "RETIRED_ROUTE", "OPEN"],
    "A38": ["DERIVED_EXACT", "OPEN"],
    "A39": ["NO_GO", "OPEN"],
    "A40": ["PROFILE_REPLAY", "NUMERIC_CERTIFIED"],
    "A41": ["CONDITIONAL", "PROFILE_POSTCHECK", "OPEN"],
    "A42": ["CONDITIONAL", "PROFILE_POSTCHECK", "OPEN"],
    "A43": ["CONDITIONAL", "NO_GO_NATIVE_10D", "OPEN"],
    "A44": ["CONDITIONAL", "OPEN"],
    "A45": ["DERIVED_EXACT", "OPEN_GENERATIVE_VALUES"],
    "A46": ["DERIVED_EXACT", "OPEN_VACUUM_SELECTOR"],
    "A47": ["DERIVED_EXACT"],
    "A48": ["DERIVED_EXACT", "SUPERSEDED_PARTIAL"],
    "A49": ["PROFILE_REPLAY", "DERIVED_EXACT", "NO_GO_NATIVE_TRIPLE"],
    "A50": ["DERIVED_EXACT", "PROFILE_TIER"],
    "A51": ["DERIVED_EXACT", "PROFILE_REPLAY", "OPEN_ABSOLUTE_NORMALIZATION"],
    "A52": ["PROFILE_REPLAY", "NO_GO", "OPEN_STRICT_SOURCE"],
    "A53": ["CONDITIONAL", "NO_GO", "OPEN"],
    "A54": ["NUMERIC_CERTIFIED", "NO_GO", "OPEN"],
    "A55": ["DERIVED_EXACT", "NO_GO", "OPEN"],
    "A56": ["NO_GO", "OPEN"],
    "A57": ["DERIVED_EXACT", "NO_GO", "OPEN"],
    "A58": ["DERIVED_EXACT", "INTERMEDIATE"],
    "A59": ["NO_GO", "RETIRED_ROUTE", "OPEN"],
    "A60": ["DERIVED_EXACT", "INTERMEDIATE"],
    "A61": ["DERIVED_EXACT", "INTERMEDIATE", "RETIRED_ROUTE"],
    "A62": ["DERIVED_EXACT", "NO_GO", "OPEN_STRICT_GAUGE_PREDICTION"],
    "A63": ["DERIVED_EXACT", "NO_GO_FAMILY_SPLITTING", "OPEN_GAUGE_HESSIAN_VALUES"],
    "A64": ["NO_GO", "OPEN_NATIVE_GAUGE_FUNCTIONAL"],
    "A65": ["DERIVED_EXACT", "OPEN_W_KIN_SOURCE"],
    "A66": ["NUMERIC_DIAGNOSTIC", "OPEN_SOURCE"],
    "A67": ["CONDITIONAL", "NO_GO_POSITIVE_DENSITY_CLASS", "OPEN_STRICT_VALUES"],
    "A68": ["DERIVED_EXACT_INVERSE", "PROFILE_DIAGNOSTIC", "OPEN_SOURCE"],
    "A69": ["DERIVED_EXACT_CANDIDATE", "CONDITIONAL", "PROFILE_INFERRED", "OPEN"],
    "A70": ["NUMERIC_DIAGNOSTIC", "TARGET_AWARE", "NOT_PROMOTED"],
    "A71": ["DERIVED_EXACT", "NO_GO_A70_PROMOTION", "OPEN_PHYSICAL_EMBEDDING"],
    "A72": ["DERIVED_EXACT_CANDIDATE", "TARGET_RANKED", "NOT_PREDICTION"],
    "A73": ["DERIVED_EXACT_SAME_ACTION_EXISTENCE", "OPEN_PHYSICAL_SELECTION"],
    "A74": ["DERIVED_EXACT_NORMALIZATION", "PROFILE_COMPATIBILITY", "OPEN_PHYSICAL_GATE"],
    "A75": ["DERIVED_EXACT_CONDITIONAL_HESSIAN", "NO_GO_RELABELLING", "OPEN"],
    "A76": ["DERIVED_EXACT_DOMAIN", "NO_GO_SHORTCUT", "OPEN_FLUCTUATION_COMPLEX"],
    "A77": ["DERIVED_EXACT_STRUCTURAL", "OPEN_PHYSICAL_PLACEMENT"],
    "A78": ["CONDITIONAL", "BINARY_SIGN_OPEN"],
    "A79": ["DERIVED_EXACT_NO_GO", "OPEN_INSERTION_LAW"],
    "A80": ["DERIVED_EXACT_POSITIVE_REPRESENTATIVE", "OPEN_ACTION_MAP"],
    "A81": ["DERIVED_EXACT_BRIDGE", "OPEN_COMPLETENESS"],
    "A82": ["DERIVED_EXACT_LATER_AUTHORITY_CONSTRUCTION", "OPEN_CLOSURE_HESSIAN"],
    "A83": ["DERIVED_EXACT_EXECUTION", "CONDITIONAL_AXIOM", "OPEN_DERIVATION"],
    "A84": ["DERIVED_EXACT_ACTION_TIER", "OPEN_FINITE_MATCHING"],
    "A85": ["DERIVED_EXACT_CORPUS_ACTION_TIER", "PROFILE_SCHEME", "OPEN_PRIMITIVE_CORE"],
    "A86": ["DERIVED_EXACT_CORPUS_ACTION_SOURCE", "OPEN_PRIMITIVE_CORE"],
    "A87": ["DERIVED_EXACT_CONVENTION_MAP", "PROFILE_COMPATIBILITY", "PROSPECTIVE_FROZEN"],
    "A88": ["DERIVED_EXACT_SCALE_NO_GO", "OPEN_COMMON_NORMALIZATION"],
    "A89": ["DERIVED_EXACT_FACTORIZATION", "NO_GO_CANDIDATE", "CLOSED_ADOPTED_TIER"],
    "A90": ["AUDIT", "PARAMETER_LEDGER", "OPEN_STRICT_UPGRADES"],
    "A91": ["DERIVED_EXACT_AMBIGUITY", "NO_GO_UNIQUE_PHASE", "OPEN_NEUTRAL_SOURCE"],
    "A92": ["DERIVED_EXACT_DOMAIN", "OPEN_PHYSICAL_SELECTION"],
    "A93": ["DERIVED_EXACT_NECESSITY_SUFFICIENCY", "NO_GO_EXISTING_SELECTION", "OPEN"],
    "A94": ["PROFILE_CLOSURE_ADOPTED_TIER", "CONDITIONAL", "OPEN_STRICT"],
    "A95": ["DERIVED_EXACT_CONDITIONAL_MEASURE", "CLOSED_ADOPTED_TIER", "OPEN_GLOBAL_UNIQUENESS"],
    "A96": ["DERIVED_EXACT_ANOMALY_MATCHING", "NO_GO_THRESHOLD_SHORTCUT", "OPEN_U6"],
    "A97": ["DERIVED_EXACT_REDUCTION", "OPEN_ABSOLUTE_SCALE", "OPEN_QUALITY"],
    "A98": ["DERIVED_EXACT_BOUND", "OPEN_SOURCE_PAYLOAD"],
    "A99": ["DERIVED_EXACT_CONDITIONAL_COUPLING", "OPEN_SAME_SOURCE_LATTICE", "U6_9_OF_10"],
}

EXTRA_AUTHORITY_PATHS = {
    "A01": [
        "candidate_data/current_true_sm_closure_consolidated_ledger.candidate.json",
        "candidate_data/global_locked_breakthroughs_do_not_reopen.candidate.json",
    ],
}

KEY_RESULTS = [
    {"id": "current_global_lock", "authority": "A01", "repo_id": "sm_closure", "path": "candidate_data/current_true_sm_closure_consolidated_ledger.candidate.json", "tier": "PROFILE_REPLAY", "description": "Current non-looping global status and source-certificate map."},
    {"id": "final_12_of_12_audit", "authority": "A04", "repo_id": "sm_closure", "path": "candidate_data/selected_finalglobaltruesmclosureaudit_aftermultiloopprecision/final_global_true_sm_closure_audit.packet.json", "tier": "PROFILE_REPLAY", "description": "Twelve-obligation embedded renormalized-SM equivalence audit."},
    {"id": "q79_exact_theorem", "authority": "A11", "repo_id": "q79", "path": "proof_corpus/Consolidated_Exact_Z64_to_q79_Closure_Theorem_v1.md", "tier": "DERIVED_EXACT", "description": "CRT q=79 theorem on the selected exact branch."},
    {"id": "q79_exact_audit", "authority": "A11", "repo_id": "q79", "path": "proof_corpus/consolidated_exact_z64_to_q79_closure_audit.py", "tier": "DERIVED_EXACT", "description": "Executable q=79 exact-branch audit."},
    {"id": "qutrit_weyl_27_matrix", "authority": "A01", "repo_id": "sm_closure", "path": "candidate_data/selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging/qutrit_weyl_27x27_matrix_realization.packet.json", "tier": "DERIVED_EXACT", "description": "Sparse 27x27 qutrit-Weyl left-action realization."},
    {"id": "charged_yukawa_higgs_profile", "authority": "A01", "repo_id": "sm_closure", "path": "candidate_data/selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution/versioned_common_scale_yukawa_higgs_values.packet.json", "tier": "PROFILE_REPLAY", "description": "Versioned Yu, Yd, Ye and lambda_H profile packet."},
    {"id": "precision_8x8_workspace", "authority": "A02", "repo_id": "sm_closure", "path": "candidate_data/selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood/selected_smdr_multiloop_precision_workspace.packet.json", "tier": "PROFILE_REPLAY", "description": "Eight-coordinate SMDR output with positive-definite 8x8 covariance."},
    {"id": "precision_15_source_transport", "authority": "A02", "repo_id": "sm_closure", "path": "candidate_data/selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood/smdr_multiloop_common_source_transport.raw.json", "tier": "PROFILE_REPLAY", "description": "Fifteen measured source coordinates, Jacobian and covariance transport."},
    {"id": "ckm_prediction_profile", "authority": "A14", "repo_id": "sm_closure", "path": "candidate_data/selected_ckmcentralestimatorretirement_or_predictionprofileclosure/ckm_prediction_profile_closure.packet.json", "tier": "NUMERIC_CERTIFIED", "description": "Three selected CKM profile rows and uncertainty comparison."},
    {"id": "strict_pew_row", "authority": "A01", "repo_id": "sm_closure", "path": "candidate_data/selected_strictpewdenominatorselectiontheorem_or_directkpromotion/promoted_strict_pew_source_row.packet.json", "tier": "DERIVED_EXACT", "description": "Promoted P_EW source row at the declared one-shared-primitive standard."},
    {"id": "direct_k_higgs_row", "authority": "A01", "repo_id": "sm_closure", "path": "candidate_data/selected_strictpewdenominatorselectiontheorem_or_directkpromotion/promoted_direct_kthreshold_omega_h_lambda_row.packet.json", "tier": "DERIVED_EXACT", "description": "Promoted direct K_threshold.Omega_H.lambda row."},
    {"id": "literal_cech_witness", "authority": "A07", "repo_id": "sm_closure", "path": "candidate_data/selected_literalcechwitness_or_globalhymconnectioncoefficients/literal_selected_s3_deligne_cech_witness.packet.json", "tier": "DERIVED_EXACT", "description": "Literal 81-entry, 729-cocycle finite Cech witness."},
    {"id": "hym_wiener_contraction", "authority": "A19", "repo_id": "sm_closure", "path": "candidate_data/selected_hymvalidatedfourierresidualtailbound/wiener_contraction.packet.json", "tier": "NUMERIC_CERTIFIED", "description": "Weighted-theta Fourier-tail and Wiener contraction certificate."},
    {"id": "neutral_two_primitive_profile", "authority": "A40", "repo_id": "sm_closure", "path": "candidate_data/selected_neutraltwoprimitiveprofilevalueclosure/neutral_two_primitive_profile_values.packet.json", "tier": "PROFILE_REPLAY", "description": "Measured two-splitting neutrino profile, masses and Dirac Yukawa rows."},
    {"id": "typed_family_representation", "authority": "A46", "repo_id": "sm_closure", "path": "candidate_data/selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem/typed_family_gauge_carrier_and_anomaly_table.packet.json", "tier": "DERIVED_EXACT", "description": "48-state family-diagonal chiral representation and anomaly table."},
    {"id": "native_gauge_group", "authority": "A47", "repo_id": "sm_closure", "path": "candidate_data/selected_nativebundleautomorphismgaugegroup_or_parameterassumptionaudit/native_bundle_gauge_group_and_parameter_audit.packet.json", "tier": "DERIVED_EXACT", "description": "Native U1, SU2, SU3 bundle automorphisms and Z6 quotient."},
    {"id": "physical_df_96", "authority": "A49", "repo_id": "sm_closure", "path": "candidate_data/selected_physicalfinitediracoperatorandintersectionform_or_fullfinitetripleclosure/physical_DF_and_finite_triple.packet.json", "tier": "PROFILE_REPLAY", "description": "Explicit profile-tier 96x96 finite Dirac operator invariants and finite-triple checks."},
    {"id": "neutral_summand_hypercharge", "authority": "A50", "repo_id": "sm_closure", "path": "candidate_data/selected_neutralalgebrasummandorequivalentaxiomrevision/neutral_summand_and_hypercharge_reduction.packet.json", "tier": "DERIVED_EXACT", "description": "C_N completion and unique anomaly-free shared hypercharge circle."},
    {"id": "finite_inner_fluctuation", "authority": "A51", "repo_id": "sm_closure", "path": "candidate_data/selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure/finite_inner_fluctuation_and_spectral_traces.packet.json", "tier": "PROFILE_REPLAY", "description": "676-pair inner-fluctuation execution, one-Higgs projector and trace invariants."},
    {"id": "su2_finite_gauge_spectrum", "authority": "A61", "repo_id": "sm_closure", "path": "candidate_data/selected_su2transportclosedfinitegaugerow_and_su3nativecolorsourcereduction.candidate.json", "tier": "DERIVED_EXACT", "description": "Exact SU2 finite gauge/ghost spectrum row."},
    {"id": "su3_finite_gauge_spectrum", "authority": "A62", "repo_id": "sm_closure", "path": "candidate_data/selected_su3adjointcentraltrivialfinitegaugerow_and_tenspectrumclosure.candidate.json", "tier": "DERIVED_EXACT", "description": "Exact SU3 adjoint-central-trivial row and ten-spectrum closure/no-go."},
    {"id": "e6_qpsi_qcd_anomaly", "authority": "A22", "repo_id": "sm_closure", "path": "candidate_data/selected_e6centralgeneratorqcdanomalyaudit/e6_qpsi_qcd_anomaly.packet.json", "tier": "DERIVED_EXACT", "description": "E6 Qpsi matter/exotic QCD anomaly cancellation audit."},
    {"id": "gr_tt_support", "authority": "A13", "repo_id": "protospinor_gr", "path": "certificates/gr_tt_support_final_theorem_certificate.json", "tier": "DERIVED_EXACT", "description": "Exact-branch internal TT support certificate; physical normalization remains open."},
    {"id": "strict_upgrade_ledger", "authority": "A05", "repo_id": "sm_closure", "path": "candidate_data/selected_strictnoknobupgradeledger_aftertruesmequivalence.candidate.json", "tier": "OPEN", "description": "Current 2/9 strict no-knob upgrade ledger."},
    {"id": "qa_su3_support_program", "authority": None, "repo_id": "qa_su3", "path": "README.md", "tier": "SUPPORT_ONLY", "description": "Complete adjacent Qa/SU3 research chronology; final claims require promotion through A01-A62."},
    {"id": "nonsm_constants_program", "authority": None, "repo_id": "constants", "path": "README.md", "tier": "STRICT_UPGRADE_EVIDENCE", "description": "Non-SM constants and no-knob source-search chronology."},
    {"id": "individual_constants_program", "authority": None, "repo_id": "individual_constants", "path": "README.md", "tier": "STRICT_UPGRADE_EVIDENCE", "description": "Individual-constant source-search policy and evidence."},
    {"id": "protospinor_simulation_kernel", "authority": None, "repo_id": "protospinor_sim", "path": "components/proto-spinor/ProtoSpinorKernel.vue", "tier": "EXPLORATORY_SIMULATION", "description": "Proto-spinor particle-state simulation kernel."},
]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def archive_blob_path(artifact: dict[str, Any]) -> Path:
    digest = artifact["sha256"]
    return ARCHIVE / digest[:2] / digest[2:]


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(value, indent=2, sort_keys=True) + "\n")


def canonical_artifact_name(value: str) -> str:
    name = Path(value).name.lower()
    for suffix in (".candidate.json", "_certificate.json", "_audit.py", ".packet.json", ".json", ".py", ".md"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    name = re.sub(r"^(mtt_|build_|compute_|verify_)", "", name)
    name = re.sub(r"_v\d+$", "", name)
    canonical = re.sub(r"[^a-z0-9]", "", name)
    return re.sub(r"(theorem)$", "", canonical)


def string_leaves(value: Any):
    if isinstance(value, dict):
        for child in value.values():
            yield from string_leaves(child)
    elif isinstance(value, list):
        for child in value:
            yield from string_leaves(child)
    elif isinstance(value, str):
        yield value


def companion_paths(authority: dict[str, Any], artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    relative = authority["relative_path"].lower()
    stem = Path(relative).stem.removeprefix("mtt_")
    stem = re.sub(r"_v\d+$", "", stem)
    canonical_stem = canonical_artifact_name(stem)
    exact = {
        relative,
        f"candidate_data/{stem}.candidate.json",
        f"certificates/{stem}_certificate.json",
        f"proof_corpus/{stem}.py",
        f"scripts/build_{stem}.py",
    }
    packet_prefix = f"candidate_data/{stem}/"
    rows = []
    repo_artifacts = [row for row in artifacts if row["repo_id"] == authority["repo_id"]]
    repo_index = {row["path"].lower(): row for row in repo_artifacts}
    for artifact in artifacts:
        if artifact["repo_id"] != authority["repo_id"]:
            continue
        path = artifact["path"].lower()
        parts = Path(path).parts
        candidate_directory_match = (
            len(parts) >= 3
            and parts[0] == "candidate_data"
            and canonical_artifact_name(parts[1]) == canonical_stem
        )
        artifact_name_match = (
            parts
            and parts[0] in {"candidate_data", "certificates", "proof_corpus", "scripts"}
            and canonical_artifact_name(parts[-1]) == canonical_stem
        )
        if path in exact or path.startswith(packet_prefix) or candidate_directory_match or artifact_name_match:
            rows.append(artifact)
    for path in EXTRA_AUTHORITY_PATHS.get(authority["authority_id"], []):
        matched = repo_index.get(path.lower())
        if matched is None:
            raise RuntimeError(f"missing configured authority dependency: {authority['authority_id']} {path}")
        rows.append(matched)

    selected = {row["path"].lower(): row for row in rows}
    frontier = list(selected.values())
    for _ in range(2):
        next_frontier = []
        for artifact in frontier:
            if artifact["suffix"] != ".json":
                continue
            source = archive_blob_path(artifact)
            try:
                payload = json.loads(source.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError, OSError):
                continue
            for raw_reference in string_leaves(payload):
                reference = raw_reference.replace("\\", "/").lower()
                matched = repo_index.get(reference)
                if matched is None and ":/" in reference:
                    for candidate_path, candidate in repo_index.items():
                        if reference.endswith("/" + candidate_path):
                            matched = candidate
                            break
                if matched is None or matched["path"].lower() in selected:
                    continue
                selected[matched["path"].lower()] = matched
                next_frontier.append(matched)
        frontier = next_frontier
    return sorted(selected.values(), key=lambda row: row["path"])


def main() -> int:
    authority_payload = json.loads((INVENTORY / "authority_entries.json").read_text(encoding="utf-8"))
    artifacts = load_jsonl(INVENTORY / "artifacts.jsonl")
    entries = []
    tag_counts: Counter[str] = Counter()
    domain_counts: Counter[str] = Counter()

    authority_root = (RELEASE / "authority").resolve()
    if ROOT.resolve() not in authority_root.parents:
        raise RuntimeError(f"unsafe generated release path: {authority_root}")
    if authority_root.exists():
        shutil.rmtree(authority_root)

    for authority in authority_payload["entries"]:
        authority_id = authority["authority_id"]
        domain = DOMAIN_BY_ID[authority_id]
        tags = STATUS_TAGS[authority_id]
        companions = companion_paths(authority, artifacts)
        bundle_rows = []
        for artifact in companions:
            source = archive_blob_path(artifact)
            destination = RELEASE / "authority" / authority_id / f"{artifact['sha256']}{artifact['suffix']}"
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            bundle_rows.append(
                {
                    "release_path": destination.relative_to(ROOT).as_posix(),
                    "source_repo_id": artifact["repo_id"],
                    "source_path": artifact["path"],
                    "sha256": artifact["sha256"],
                    "kind": artifact["kind"],
                }
            )
        if not any(row["source_path"].lower() == authority["relative_path"].lower() for row in bundle_rows):
            raise RuntimeError(f"authority note was not bundled: {authority_id}")
        entries.append(
            {
                **authority,
                "domain": domain,
                "status_tags": tags,
                "bundle_artifacts": bundle_rows,
            }
        )
        domain_counts[domain] += 1
        tag_counts.update(tags)

    manifest = {
        "schema": "MTTCurrentAuthorityRelease.v2",
        "authority_entry_count": len(entries),
        "baseline_authority_entry_count": 62,
        "current_authority_extension_count": len(entries) - 62,
        "bundle_artifact_count": sum(len(row["bundle_artifacts"]) for row in entries),
        "domain_counts": dict(sorted(domain_counts.items())),
        "status_tag_counts": dict(sorted(tag_counts.items())),
        "entries": entries,
        "policy": {
            "authority_order": "MTT_CORPUS_REVISION_UPDATE_LEDGER A01-A99",
            "frozen_baseline": "A01-A62 at 2026-07-12",
            "current_extension": "A63-A99 indexed and bundled at 2026-08-05",
            "historical_packet_status_is_authority": False,
            "profile_replay_promoted_to_no_knob_prediction": False,
            "open_and_no_go_results_retained": True,
        },
    }
    dump(RELEASE / "authority_manifest.json", manifest)

    machine_rows = []
    hash_only_rows = load_jsonl(ROOT / "archive" / "hash_only_artifacts.jsonl")
    hash_only_keys = {(row["repo_id"], row["path"]) for row in hash_only_rows}
    for artifact in artifacts:
        if artifact["kind"] not in {"certificate", "result_packet", "calculation", "audit", "report", "data"}:
            continue
        archive_available = (artifact["repo_id"], artifact["path"]) not in hash_only_keys
        machine_rows.append(
            {
                "repo_id": artifact["repo_id"],
                "source_path": artifact["path"],
                "archive_available": archive_available,
                "archive_path": archive_blob_path(artifact).relative_to(ROOT).as_posix() if archive_available else None,
                "kind": artifact["kind"],
                "sha256": artifact["sha256"],
                "schema": artifact.get("schema"),
                "historical_status": artifact.get("status"),
                "heuristic_tier_non_authoritative": artifact.get("heuristic_tier"),
            }
        )
    with (RELEASE / "machine_evidence_catalog.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for row in machine_rows:
            handle.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")

    artifact_index = {(row["repo_id"], row["path"].lower()): row for row in artifacts}
    results_root = (RELEASE / "results").resolve()
    if ROOT.resolve() not in results_root.parents:
        raise RuntimeError(f"unsafe generated results path: {results_root}")
    if results_root.exists():
        shutil.rmtree(results_root)
    current_selection = json.loads(CURRENT_RESULT_CONFIG.read_text(encoding="utf-8"))
    current_results = current_selection["results"]
    all_results = KEY_RESULTS + current_results
    if len({row["id"] for row in all_results}) != len(all_results):
        raise RuntimeError("duplicate result id in baseline/current selection")
    result_entries = []
    for key_result in all_results:
        artifact = artifact_index.get((key_result["repo_id"], key_result["path"].lower()))
        if artifact is None:
            raise RuntimeError(f"missing key result: {key_result['repo_id']} {key_result['path']}")
        if (artifact["repo_id"], artifact["path"]) in hash_only_keys:
            raise RuntimeError(f"selected result cannot be hash-only: {key_result['id']}")
        source = archive_blob_path(artifact)
        destination = RELEASE / "results" / key_result["id"] / f"artifact{artifact['suffix']}"
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        result_entries.append(
            {
                **key_result,
                "release_path": destination.relative_to(ROOT).as_posix(),
                "archive_path": archive_blob_path(artifact).relative_to(ROOT).as_posix(),
                "sha256": artifact["sha256"],
                "historical_status": artifact.get("status"),
            }
        )
    dump(RELEASE / "result_manifest.json", {
        "schema": "MTTKeyResultManifest.v2",
        "result_count": len(result_entries),
        "baseline_result_count": len(KEY_RESULTS),
        "current_promoted_result_count": len(current_results),
        "results": result_entries,
        "selection_policy": "The July-12 A01-A62 baseline is retained, A63-A99 form the later authority extension, and hash-addressed current results retain their declared tiers.",
    })

    paper_lock = json.loads(PAPER_CORPUS_LOCK.read_text(encoding="utf-8"))
    dump(RELEASE / "paper_corpus_lock.json", paper_lock)
    source_snapshot = json.loads(
        (INVENTORY / "source_repositories.json").read_text(encoding="utf-8")
    )
    def archived_json(repo_id: str, path: str) -> dict[str, Any]:
        artifact = artifact_index[(repo_id, path.lower())]
        return json.loads(archive_blob_path(artifact).read_text(encoding="utf-8"))

    unified_frontier = archived_json("unified_source", "state/frontier.json")
    dump(
        RELEASE / "current_snapshot.json",
        {
            "schema": "MTTCurrentCuratedSnapshot.v2",
            "snapshot_date": current_selection["snapshot_date"],
            "baseline": {
                "snapshot_date": "2026-07-12",
                "authority_chain": "A01-A62",
                "authority_entries": 62,
                "preserved_as_immutable_history": True,
            },
            "current_layer": {
                "authority_extension": "A63-A99",
                "authority_extension_count": len(entries) - 62,
                "promoted_result_count": len(current_results),
                "result_ids": [row["id"] for row in current_results],
                "unified_source_hypothesis": unified_frontier["hypothesis"],
                "unified_source_next_action": unified_frontier["next_action"],
            },
            "paper_corpus": paper_lock,
            "source_repositories": source_snapshot["repositories"],
            "claim_guard": "Archive inclusion preserves evidence and declared tier; it does not prove physical source selection.",
        },
    )

    precision_source = archived_json(
        "sm_closure",
        "candidate_data/selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood/smdr_multiloop_common_source_transport.raw.json",
    )
    pew_row = archived_json(
        "sm_closure",
        "candidate_data/selected_strictpewdenominatorselectiontheorem_or_directkpromotion/promoted_strict_pew_source_row.packet.json",
    )
    neutral_profile = archived_json(
        "sm_closure",
        "candidate_data/selected_neutraltwoprimitiveprofilevalueclosure/neutral_two_primitive_profile_values.packet.json",
    )
    neutral_values = neutral_profile["calibrated_shape_and_scale"]
    dump(RELEASE / "parameter_ledger.json", {
        "schema": "MTTCurrentParameterLedger.v2",
        "declared_closure_scope": "embedded renormalized-SM equivalence at the one-shared-physical-primitive/profile standard",
        "construction_side_continuous_primitives": {
            "count": 1,
            "rows": [
                {
                    "id": "P_EW",
                    "value": pew_row["P_EW_value"],
                    "role": "shared electroweak/action primitive used once across the locked matrix and threshold construction",
                    "H_specific": False,
                    "authority": "A01",
                }
            ],
            "H_specific_parameter_count": 0,
        },
        "measured_sm_profile_coordinates": {
            "count": len(precision_source["source_inputs"]),
            "covariance_policy": precision_source["source_covariance_policy"],
            "rows": precision_source["source_inputs"],
            "authority": "A02/A06",
            "official_joint_correlations_imported": False,
        },
        "neutral_extension_profile_coordinates": {
            "count": 2,
            "rows": [
                {"id": "Delta_m21_sq_eV2", "value": neutral_values["Delta_m21_sq_eV2"]},
                {"id": "Delta_m31_sq_eV2", "value": neutral_values["Delta_m31_sq_eV2"]},
            ],
            "authority": "A40",
            "strict_mtt_source_selected": False,
        },
        "current_effective_model_coordinate_accounting": {
            "authority": "A90",
            "non_neutrino_count_excluding_qcd_theta": 13,
            "rows": {
                "common_gauge_kinetic_anchor": 1,
                "charged_yukawa_magnitudes": 9,
                "ckm_phase": 1,
                "electroweak_scale": 1,
                "separately_typed_shared_P_EW": 1
            },
            "minimal_pmns_policy_count": 6,
            "count_with_minimal_pmns_policy": 19,
            "guards": {
                "is_transport_input_count": False,
                "is_strict_zero_knob_count": False,
                "is_independent_prospective_evidence_count": False,
                "qcd_theta_included": False
            }
        },
        "transported_or_reconstructed_outputs_not_counted_as_new_independent_inputs": {
            "SMDR_output_rows": 8,
            "charged_yukawa_magnitude_rows": 9,
            "finite_DF_dimension": 96,
            "precision_covariance_shape": [8, 8],
        },
        "interpretation_guards": {
            "one_shared_primitive_means_one_total_empirical_parameter": False,
            "measured_profile_inputs_are_derived_no_knob_predictions": False,
            "strict_zero_primitive_global_closure": False,
            "parameter_reduction_relative_to_the_SM_claimed_at_strict_prediction_tier": False,
            "same_profile_outputs_can_be_double_counted_as_independent_inputs": False,
            "transport_input_count_equals_effective_model_coordinate_count": False,
        },
    })

    print(json.dumps({
        "authority_entries": len(entries),
        "authority_bundle_artifacts": manifest["bundle_artifact_count"],
        "machine_evidence_rows": len(machine_rows),
        "key_results": len(result_entries),
        "baseline_results": len(KEY_RESULTS),
        "current_promoted_results": len(current_results),
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
