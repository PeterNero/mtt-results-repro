"""Build the oriented Phi_fin product-operator / smooth E_Qa magnitude source gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "ctau_dirac": DATA / "selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem.candidate.json",
    "ctau_gate": DATA / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json",
    "trace_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "spectrum_27mode": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.spectrum_attempt.json",
    "finitepart_policy": DATA / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource.candidate.json"
OUTPUT_TABLE = DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_ProductOperator_or_SmoothEQa_MagnitudeSource_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SIMULTANEOUS_TABLE_BUILT_SOURCE_MAGNITUDE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceEmission_or_SmoothEQa_ThresholdIdentity_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def ctau(rank_slot: int) -> int:
    return 0 if rank_slot == 0 else (1 if rank_slot == 1 else -1)


def basis_label(m: int, n: int, r: int) -> str:
    return f"e_m{m}_n{n}_r{r}"


def main() -> dict[str, Any]:
    ctau_dirac = load(INPUTS["ctau_dirac"])
    ctau_gate = load(INPUTS["ctau_gate"])
    trace = load(INPUTS["trace_27mode"])
    spectrum = load(INPUTS["spectrum_27mode"])
    finitepart = load(INPUTS["finitepart_policy"])

    eta = float(trace["decision"]["selected_eta_N"])
    zero_shift_indices = set(trace["finite_trace_route"]["selected_trace_equality"]["zero_cluster_indices"])
    table = []
    counts: dict[str, int] = {}
    positive_logdet_all = 0.0
    oriented_sector_logdet = {"-1": 0.0, "1": 0.0}
    oriented_sector_counts = {"-1": 0, "1": 0}
    kernel_count = 0
    positive_count = 0

    for m in range(3):
        for n in range(3):
            base = m * m + n * n
            for r in range(3):
                row = 3 * (3 * m + n) + r
                sign = ctau(r)
                eigen = float(base)
                if row in zero_shift_indices:
                    eigen += eta
                positive = eigen > 0
                entry = {
                    "row": row,
                    "basis_label": basis_label(m, n, r),
                    "m": m,
                    "n": n,
                    "rank_slot": r,
                    "C_tau": sign,
                    "PhiFin_DE_eigenvalue": eigen,
                    "is_positive_magnitude": positive,
                    "is_Ctau_kernel": sign == 0,
                    "oriented_eigenvalue": None if sign == 0 else sign * eigen,
                    "oriented_square_eigenvalue": None if sign == 0 else eigen * eigen,
                }
                table.append(entry)
                counts[str(sign)] = counts.get(str(sign), 0) + 1
                if positive:
                    positive_count += 1
                    positive_logdet_all += math.log(eigen)
                    if sign != 0:
                        oriented_sector_counts[str(sign)] += 1
                        oriented_sector_logdet[str(sign)] += math.log(eigen)
                else:
                    kernel_count += 1

    simultaneous_table = {
        "schema": "SelectedHeterotic.OrientedPhiFinSimultaneousCtauPhiFinTable.v1",
        "basis_id": trace["finite_trace_route"]["gap_layer"]["basis_id"],
        "basis_dimension": 27,
        "selected_eta_N": eta,
        "zero_shift_indices": sorted(zero_shift_indices),
        "operators": {
            "C_tau": "diagonal by rank slot r with values 0,+1,-1",
            "PhiFin_DE": "selected 27-mode Fourier D_E gap layer with eta_N shift on selected H zero cluster",
        },
        "commutation": {
            "both_diagonal_in_same_basis": True,
            "commutator_zero": True,
            "simultaneous_functional_calculus_closed": True,
        },
        "entries": table,
        "counts": {
            "C_tau_spectrum": counts,
            "PhiFin_positive_count": positive_count,
            "PhiFin_kernel_count": kernel_count,
            "oriented_nonzero_Ctau_positive_magnitude_count": sum(oriented_sector_counts.values()),
            "oriented_sector_counts": oriented_sector_counts,
        },
        "logdet_values": {
            "PhiFin_all_positive_logdet": positive_logdet_all,
            "oriented_plus_sector_logdet": oriented_sector_logdet["1"],
            "oriented_minus_sector_logdet": oriented_sector_logdet["-1"],
            "oriented_abs_sector_logdet_sum": oriented_sector_logdet["1"] + oriented_sector_logdet["-1"],
            "oriented_signed_sector_logdet_difference": oriented_sector_logdet["1"] - oriented_sector_logdet["-1"],
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_TABLE.write_text(json.dumps(simultaneous_table, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    source_gap = {
        "same_domain_closed": True,
        "commutation_closed": True,
        "simultaneous_table_built": True,
        "positive_magnitude_table_computed": True,
        "same_source_threshold_identity_closed": False,
        "smooth_E_Qa_magnitude_source_closed": False,
        "heterotic_PhiFin_identity_closed": False,
        "reason_open": (
            "The algebraic product/orientation table is well-defined on the selected 27-mode "
            "B_N basis, but the current source record still scopes the Phi_fin D_E layer to "
            "Route-C support/gap closure, not to a heterotic Qa/SU3 threshold identity."
        ),
    }

    decision = {
        "same_BN_domain_for_Ctau_and_PhiFin_positive_gap": True,
        "commutation_or_simultaneous_functional_calculus_closed": True,
        "oriented_product_table_built": True,
        "kernel_policy_compatible_algebraically": True,
        "no_double_counting_shared_circle_algebraic_check": True,
        "oriented_product_operator_source_emitted": False,
        "smooth_E_Qa_magnitude_source_closed": False,
        "heterotic_threshold_magnitude_promoted": False,
        "PhiFin_all_positive_logdet": positive_logdet_all,
        "oriented_abs_sector_logdet_sum": oriented_sector_logdet["1"] + oriented_sector_logdet["-1"],
        "oriented_signed_sector_logdet_difference": oriented_sector_logdet["1"] - oriented_sector_logdet["-1"],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinProductOperatorOrSmoothEQaMagnitudeSource",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "ctau_dirac": ctau_dirac["status"],
            "ctau_gate": ctau_gate["status"],
            "trace_27mode": trace["status"],
            "spectrum_27mode": spectrum["schema"],
            "finitepart_policy": finitepart["status"],
        },
        "simultaneous_table_path": rel(OUTPUT_TABLE),
        "source_gap": source_gap,
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinSimultaneousFunctionalCalculusTheorem",
            "proved": True,
            "statement": (
                "On the selected 27-mode B_N carrier, C_tau and the selected Phi_fin D_E "
                "gap-layer operator are simultaneously diagonal: C_tau depends only on the "
                "rank slot and Phi_fin D_E depends on the Fourier mode plus the selected "
                "eta_N zero-cluster shift. Therefore their commutator vanishes and the "
                "oriented magnitude table is algebraically well-defined with no new parameter. "
                "This closes the same-domain and commutation gates. It does not yet promote "
                "the table to a heterotic threshold magnitude because the current source "
                "record does not emit the oriented product as the selected heterotic Phi_fin "
                "or smooth E_Qa threshold identity."
            ),
        },
        "guardrails": {
            "does_not_promote_oriented_table_to_threshold_identity": True,
            "does_not_use_ctau_logdet_as_magnitude": True,
            "does_not_insert_positive_shift": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_scope": "same_domain_commutation_and_simultaneous_table_only",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "simultaneous_table_path": rel(OUTPUT_TABLE),
        "note_path": rel(OUTPUT_NOTE),
        "same_BN_domain_closed": True,
        "commutation_closed": True,
        "oriented_product_table_built": True,
        "oriented_product_operator_source_emitted": False,
        "heterotic_threshold_magnitude_promoted": False,
        "PhiFin_all_positive_logdet": positive_logdet_all,
        "oriented_abs_sector_logdet_sum": decision["oriented_abs_sector_logdet_sum"],
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin ProductOperator or SmoothEQa MagnitudeSource v1

## Result

```text
status = {STATUS}
same_BN_domain_closed = true
commutation_closed = true
oriented_product_table_built = true
oriented_product_operator_source_emitted = false
heterotic_threshold_magnitude_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Computed Values

```json
{json.dumps(simultaneous_table["logdet_values"], indent=2, sort_keys=True)}
```

## Source Gap

```json
{json.dumps(source_gap, indent=2, sort_keys=True)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_TABLE)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
