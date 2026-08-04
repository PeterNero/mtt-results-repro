"""Audit the hard-leap attempt to build a rank-one lift operator."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "rank_one_lift_operator_attempt_certificate.json"
SEED_CERT = ROOT.parent / "certificates" / "iwasawa_rank_one_yukawa_seed_certificate.json"
LEDGER_CERT = ROOT.parent / "certificates" / "rank_one_lift_correction_channel_ledger_certificate.json"
THETA_CERT = ROOT.parent / "certificates" / "theta_flavor_kernel_skeleton_certificate.json"
DICT_CERT = ROOT.parent / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"
HIGGS_CERT = ROOT.parent / "certificates" / "single_higgs_channel_projection_certificate.json"
CHANNEL_CERT = ROOT.parent / "certificates" / "finite_channel_sets_certificate.json"
Q79_RESTRICTION_CERT = ROOT.parent / "certificates" / "q79_channel_restriction_certificate.json"
WEIGHT_PROTOCOL_CERT = ROOT.parent / "certificates" / "selected_channel_weight_extraction_protocol_certificate.json"
FORCED_WEIGHT_BLOCKS_CERT = ROOT.parent / "certificates" / "forced_channel_weight_blocks_certificate.json"
C3_LENS_NIL_CERT = ROOT.parent / "certificates" / "c3_lens_nil_weight_source_audit_certificate.json"
C1_CURVATURE_CERT = ROOT.parent / "certificates" / "c1_curvature_weight_source_audit_certificate.json"
C1_INSERTION_CERT = ROOT.parent / "certificates" / "c1_curvature_insertion_formula_certificate.json"
C1_IWASAWA_RPLUS_CERT = ROOT.parent / "certificates" / "c1_iwasawa_rplus_support_certificate.json"
C1_ALPHA1_RANK_CERT = ROOT.parent / "certificates" / "c1_alpha1_rank_lift_criterion_certificate.json"
CKM_NONCOMM_CERT = ROOT.parent / "certificates" / "ckm_leading_noncommutation_criterion_certificate.json"
JARLSKOG_CERT = ROOT.parent / "certificates" / "jarlskog_closure_criterion_certificate.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def determinant_diagonal(entries: list[Fraction]) -> Fraction:
    det = Fraction(1, 1)
    for entry in entries:
        det *= entry
    return det


def main() -> None:
    seed_cert = load_json(SEED_CERT)
    ledger_cert = load_json(LEDGER_CERT)
    theta_cert = load_json(THETA_CERT)
    dict_cert = load_json(DICT_CERT)
    higgs_cert = load_json(HIGGS_CERT)
    channel_cert = load_json(CHANNEL_CERT)
    q79_restriction_cert = load_json(Q79_RESTRICTION_CERT)
    weight_protocol_cert = load_json(WEIGHT_PROTOCOL_CERT)
    forced_weight_blocks_cert = load_json(FORCED_WEIGHT_BLOCKS_CERT)
    c3_lens_nil_cert = load_json(C3_LENS_NIL_CERT)
    c1_curvature_cert = load_json(C1_CURVATURE_CERT)
    c1_insertion_cert = load_json(C1_INSERTION_CERT)
    c1_iwasawa_rplus_cert = load_json(C1_IWASAWA_RPLUS_CERT)
    c1_alpha1_rank_cert = load_json(C1_ALPHA1_RANK_CERT)
    ckm_noncomm_cert = load_json(CKM_NONCOMM_CERT)
    jarlskog_cert = load_json(JARLSKOG_CERT)
    cert = load_json(CERT)
    paper = read(ROOT / "Rank_One_Lift_Operator_Hard_Leap_Attempt_v1.md")
    holonomy = read(ROOT / "Holonomy_Quotient_and_Majorana_Admissibility_for_No_Proxy_Flavor_Closure_in_MTT_v1.md")

    q = theta_cert.get("cp_character", {}).get("q_mod_448")
    delta = 2.0 * math.pi * q / 448 if q is not None else float("nan")
    sin_delta = math.sin(delta)

    # Algebraic rank-opening toy gate, not a derived spectrum.
    e1 = Fraction(1, 64)
    e2 = Fraction(1, 8)
    det_min = determinant_diagonal([e1, e2, Fraction(1, 1)])

    required_fields = cert.get("required_selected_data", {})
    missing_required = [key for key, value in required_fields.items() if value is None]
    selected_embedding = required_fields.get("selected_E6_to_SM_embedding")
    higgs_embedding = required_fields.get("higgs_doublet_embedding")
    finite_channel_sets = required_fields.get("finite_channel_sets")
    q79_channel_restriction = required_fields.get("q79_channel_restriction")
    weight_protocol = required_fields.get("selected_channel_weight_extraction_protocol")
    forced_weight_blocks = required_fields.get("forced_c0_c6_weight_blocks")
    c3_lens_nil_audit = required_fields.get("c3_lens_nil_weight_source_audit")
    c1_curvature_audit = required_fields.get("c1_curvature_weight_source_audit")
    c1_curvature_insertion = required_fields.get("c1_curvature_insertion_formula")
    c1_iwasawa_rplus_support = required_fields.get("c1_iwasawa_rplus_support")
    c1_alpha1_rank_lift_criterion = required_fields.get("c1_alpha1_rank_lift_criterion")
    ckm_leading_noncommutation_criterion = required_fields.get("ckm_leading_noncommutation_criterion")
    jarlskog_closure_criterion = required_fields.get("jarlskog_closure_criterion")

    gates = [
        Gate(
            "rank-one seed",
            "CLOSED" if seed_cert.get("tree_level_seed", {}).get("rank") == 1 else "FAIL",
            "Iwasawa certificate gives rank(Y0)=1",
        ),
        Gate(
            "correction ledger",
            "FORMULATED" if ledger_cert.get("status") == "CHANNEL_LEDGER_FORMULATED_COEFFICIENTS_OPEN" else "FAIL",
            "finite correction-channel classes are audited",
        ),
        Gate(
            "q79 CP character",
            "CLOSED" if q == 79 and abs(sin_delta) > 1e-12 else "FAIL",
            f"sin(2*pi*79/448)={sin_delta:.12f}",
        ),
        Gate(
            "generic kernel form",
            "DEFINED" if all(token in holonomy for token in ["A_gamma", "S_gamma", "chi_gamma"]) else "FAIL",
            "selected channel formula exists",
        ),
        Gate(
            "rank-opening algebra",
            "PASS" if det_min != 0 else "FAIL",
            f"det diag(1/64,1/8,1)={det_min}",
        ),
        Gate(
            "no algebraic rank obstruction",
            "PASS" if "det(Y_min) = e1 e2" in paper else "FAIL",
            "two selected nonzero light-family eigenchannels would give rank 3",
        ),
        Gate(
            "operator certificate status",
            "BLOCKED" if cert.get("status") == "BLOCKED_MISSING_SELECTED_COEFFICIENTS" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "E6-to-SM operator dictionary",
            "FORMULATED"
            if selected_embedding is not None
            and dict_cert.get("status") == "REPRESENTATION_DICTIONARY_CLOSED_HIGGS_SELECTION_OPEN"
            else "FAIL",
            "representation map formulated; low-energy Higgs projection supplied separately",
        ),
        Gate(
            "physical Higgs embedding",
            "FORMULATED"
            if higgs_embedding is not None
            and higgs_cert.get("status") == "SINGLE_HIGGS_CHANNEL_PROJECTION_FORMULATED_TRIPLET_DECOUPLING_OPEN"
            else "FAIL",
            "low-energy single-Higgs projection formulated; triplet decoupling remains open",
        ),
        Gate(
            "finite channel sets",
            "FORMULATED"
            if finite_channel_sets is not None
            and channel_cert.get("status") == "FINITE_CHANNEL_SETS_FORMULATED_WEIGHTS_OPEN"
            else "FAIL",
            "Gamma_u,d,e,nuD finite channel support is formulated; weights remain open",
        ),
        Gate(
            "channel weights",
            "OPEN" if required_fields.get("channel_weights") is None else "FAIL",
            "A_gamma and S_gamma are not computed",
        ),
        Gate(
            "q79 channel restriction",
            "FORMULATED"
            if q79_channel_restriction is not None
            and q79_restriction_cert.get("status") == "Q79_CHANNEL_RESTRICTION_FORMULATED_WEIGHTS_OPEN"
            else "FAIL",
            "C6 channels restricted to q79/conjugate; non-C6 channels trivial",
        ),
        Gate(
            "weight extraction protocol",
            "FORMULATED"
            if weight_protocol is not None
            and weight_protocol_cert.get("status") == "WEIGHT_EXTRACTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            else "FAIL",
            "finite A_gamma exp(-S_gamma) chi_gamma extraction rule formulated; values remain open",
        ),
        Gate(
            "forced C0/C6 weight blocks",
            "PARTIAL-CLOSED"
            if forced_weight_blocks is not None
            and forced_weight_blocks_cert.get("status") == "FORCED_C0_C6_WEIGHT_BLOCKS_PARTIALLY_CLOSED"
            else "FAIL",
            "C0 has A=1,S=0,chi=1; pure C6 has S=0 and q79/conjugate unit phase",
        ),
        Gate(
            "C3 Lens-Nil weight source",
            "RETIRED-BLOCKED"
            if c3_lens_nil_audit is not None
            and c3_lens_nil_cert.get("status") == "C3_LENS_NIL_WEIGHT_SOURCE_RETIRED_UNTIL_REPAIRED"
            else "FAIL",
            "finite C3 support retained, but old Lens-Nil coefficient source cannot supply weights",
        ),
        Gate(
            "C1 curvature weight source",
            "ADMISSIBLE-OPEN"
            if c1_curvature_audit is not None
            and c1_curvature_cert.get("status") == "C1_CURVATURE_WEIGHT_SOURCE_ADMISSIBLE_VALUES_OPEN"
            else "FAIL",
            "finite C1 support retained; curvature source admissible, values require O_C1 and corrected overlaps",
        ),
        Gate(
            "C1 insertion formula",
            "FORMULATED-OPEN"
            if c1_curvature_insertion is not None
            and c1_insertion_cert.get("status") == "C1_CURVATURE_INSERTION_FORMULATED_VALUES_OPEN"
            else "FAIL",
            "O_C1 is the linear response of the selected raw overlap; values remain open",
        ),
        Gate(
            "C1 Iwasawa Rplus support",
            "SUPPORT-CLOSED"
            if c1_iwasawa_rplus_support is not None
            and c1_iwasawa_rplus_cert.get("status") == "C1_IWASAWA_RPLUS_INVARIANT_SUPPORT_CLOSED_OVERLAPS_OPEN"
            else "FAIL",
            "selected invariant R_+ curvature driver is the alpha_1 row only; overlaps remain open",
        ),
        Gate(
            "C1 alpha1 rank criterion",
            "CRITERION-CLOSED"
            if c1_alpha1_rank_lift_criterion is not None
            and c1_alpha1_rank_cert.get("status") == "C1_ALPHA1_RANK_LIFT_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            "rank lift reduces to the light-family minor C33(M_C1^(alpha1)); entries remain open",
        ),
        Gate(
            "CKM leading noncommutation",
            "CRITERION-CLOSED"
            if ckm_leading_noncommutation_criterion is not None
            and ckm_noncomm_cert.get("status") == "CKM_LEADING_NONCOMMUTATION_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            "leading up/down noncommutation reduces to heavy-link mismatch Delta_v; values remain open",
        ),
        Gate(
            "Jarlskog closure criterion",
            "CRITERION-CLOSED"
            if jarlskog_closure_criterion is not None
            and jarlskog_cert.get("status") == "JARLSKOG_CLOSURE_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            "full CKM CP gate is Im det([Hu,Hd]) with nondegenerate spectra; values remain open",
        ),
        Gate(
            "family kinetic metrics",
            "OPEN" if required_fields.get("family_kinetic_metrics") is None else "FAIL",
            "post-breaking kinetic matrices are not computed",
        ),
        Gate(
            "RG matching",
            "OPEN" if required_fields.get("rg_threshold_matching") is None else "FAIL",
            "matching from mu_Theta is not computed",
        ),
        Gate(
            "missing required fields",
            "EXPECTED" if len(missing_required) >= 5 else "FAIL",
            ", ".join(missing_required),
        ),
    ]

    print("Rank-one lift operator hard-leap audit")
    print("======================================")
    print()
    print(f"q={q}")
    print(f"delta={delta:.15f}")
    print(f"det_minimal_rank_lift={det_min}")
    print(f"missing_required_count={len(missing_required)}")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
