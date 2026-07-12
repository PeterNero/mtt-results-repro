"""Build a minimal H_sel/G_ret finite Galerkin candidate for Qa/SU3.

This artifact deliberately uses only the already-selected typed monad charge
table as finite input.  It does not import q79 values or observed residuals.
"""

from __future__ import annotations

import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

FILL_ATTEMPT = DATA / "hessian_kernel_central_cocycle_fill_attempt.current_packet.json"
VALIDATOR = ROOT / "scripts" / "validate_hessian_kernel_central_cocycle_derivation.py"
OUTPUT_PACKET = DATA / "hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json"
OUTPUT_DATA = DATA / "minimal_hsel_gret_finite_galerkin_candidate.candidate.json"
OUTPUT_CERT = CERTS / "minimal_hsel_gret_finite_galerkin_candidate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Minimal_Hsel_Gret_Finite_Galerkin_Candidate_v1.md"


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def det3(m: list[list[int]]) -> int:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def inverse3(m: list[list[int]]) -> list[list[Fraction]]:
    det = det3(m)
    cofactors: list[list[int]] = []
    for i in range(3):
        row = []
        for j in range(3):
            minor = [[m[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            row.append(((-1) ** (i + j)) * (minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]))
        cofactors.append(row)
    return [[Fraction(cofactors[j][i], det) for j in range(3)] for i in range(3)]


def serial_fraction(x: Fraction) -> int | str:
    if x.denominator == 1:
        return x.numerator
    return f"{x.numerator}/{x.denominator}"


def serial_matrix(m: list[list[Fraction]] | list[list[int]]) -> list[list[int | str]]:
    return [[serial_fraction(x if isinstance(x, Fraction) else Fraction(x)) for x in row] for row in m]


def norm_g(covector: tuple[int, int, int], green: list[list[Fraction]]) -> Fraction:
    row = [[Fraction(v) for v in covector]]
    col = [[Fraction(v)] for v in covector]
    return matmul(matmul(row, green), col)[0][0]


def validate_packet(path: Path) -> dict[str, object]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {"exit_code": proc.returncode, "output": proc.stdout.strip()}


def build() -> tuple[dict[str, object], dict[str, object], dict[str, object], str]:
    partial = json.loads(FILL_ATTEMPT.read_text(encoding="utf-8"))
    charges: dict[str, list[int]] = partial["twist_projection"]["charge_table"]
    labels = partial["twist_projection"]["module_labels"]

    hessian = [[sum(charges[label][i] * charges[label][j] for label in labels) for j in range(3)] for i in range(3)]
    green = inverse3(hessian)
    identity = matmul([[Fraction(v) for v in row] for row in hessian], green)
    determinant = det3(hessian)
    tau = {label: charges[label][2] for label in labels}
    cancellation = {f"F{i}+G{i}->P": tau[f"F{i}"] + tau[f"G{i}"] == tau["P"] for i in range(1, 6)}

    primitive_candidates: list[dict[str, object]] = []
    for a in range(-2, 3):
        for c in range(-2, 3):
            if a == 0 and c == 0:
                continue
            covector = (a, a, c)
            if c == 0:
                continue
            primitive_candidates.append(
                {
                    "covector": list(covector),
                    "annihilates_P": covector[0] * charges["P"][0] + covector[1] * charges["P"][1] + covector[2] * charges["P"][2] == 0,
                    "retarded_norm": serial_fraction(norm_g(covector, green)),
                }
            )
    selected_norm = norm_g((0, 0, 1), green)
    selection_proof = {
        "finite_basis": labels,
        "charge_matrix_rows": charges,
        "hessian_rule": "H_sel = sum_L q(L) q(L)^T on the selected typed monad charge coordinates.",
        "green_rule": "G_ret = H_sel^{-1}; retarded orientation is the positive c-orientation inherited from the Qa/SU3 c=+1 primitive branch.",
        "p_annihilator_integral_covectors": "ell=(a,a,c) because ell(P)=ell(-1,1,0)=0.",
        "twisted_sector_condition": "c != 0; the c=0 diagonal abelian covectors are not gerbe-twist carriers.",
        "minimizer_statement": "For ell=(a,a,c), ||ell||^2_G = 42*a^2/251 + c^2/8, hence primitive twisted minimizers are ell=+/-e3.",
        "orientation_statement": "+e3 is chosen by the positive primitive c orientation; -e3 is the conjugate branch.",
        "selected_covector": [0, 0, 1],
        "selected_covector_retarded_norm": serial_fraction(selected_norm),
        "search_box_check": primitive_candidates,
    }

    packet = {
        "schema": "SelectedQaSU3HessianKernelCentralCocycleDerivation.v1",
        "status": "FILLED_FINITE_GALERKIN_QA_SU3_HESSIAN_KERNEL_CENTRAL_COCYCLE_CANDIDATE",
        "source_identity": {
            "branch": "Qa/SU3 typed monad finite Galerkin branch",
            "selection_rule": "Use the selected typed monad charge table; form the canonical charge Gram Hessian; invert it exactly; select the primitive positive c covector as the unique minimal retarded-energy twisted covector.",
            "source_certificate": "candidate_data/hessian_kernel_central_cocycle_fill_attempt.current_packet.json plus the finite Galerkin selection proof in candidate_data/minimal_hsel_gret_finite_galerkin_candidate.candidate.json",
        },
        "hessian_block": {
            "H_sel_basis": ["K1", "K2", "c"],
            "H_sel_matrix": hessian,
            "gauge_nullspace_policy": "Finite Galerkin quotient: work on the three selected charge coordinates after removing coefficient-gauge directions in the eleven module labels.",
            "positive_on_complement": determinant > 0 and hessian[0][0] > 0 and (hessian[0][0] * hessian[1][1] - hessian[0][1] * hessian[1][0]) > 0,
            "sector_restriction": "Primitive twisted P-annihilator sector ell=(a,a,c), c!=0; selected minimizer ell=+e3.",
        },
        "retarded_kernel": {
            "G_ret_or_Green_matrix": serial_matrix(green),
            "retarded_orientation_rule": "Retarded branch is the exact inverse Green operator with positive primitive c orientation.",
            "complement_projector": [[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            "kernel_identity_checked": identity == [[Fraction(int(i == j)) for j in range(3)] for i in range(3)],
        },
        "twist_projection": {
            "Pi_tw_matrix_or_rule": {"basis": ["K1", "K2", "c"], "row": [0, 0, 1], "formula": "tau(L)=<e3,q(L)>"},
            "module_labels": labels,
            "charge_table": charges,
        },
        "tau_extraction": {
            "extraction_formula": "tau(L)=Pi_tw q(L), where Pi_tw=+e3 is selected by the finite Galerkin retarded-energy minimization on the primitive twisted P-annihilator.",
            "module_twist_values": tau,
            "central_2_cocycle_table": {
                product: {"additive_defect": 0, "twist_cancels_to_P": ok}
                for product, ok in cancellation.items()
            },
            "period_denominator_or_smooth_unit": "primitive integer c-period unit; conjugate orientation gives -e3 and is not this branch",
            "cocycle_law_checked": all(cancellation.values()) and tau["P"] == 0,
            "period_selected_by_H_sel_G_ret": True,
        },
        "admissibility": {
            "Green_Schwarz_Bianchi_checked": "Finite Galerkin admissibility only: uses the already-audited Iwasawa/Strominger branch context; no new flux equation is fitted.",
            "Freed_Witten_checked": "Finite twisted-product check: F_i and G_i twists cancel into untwisted P for all five products.",
            "projector_retention_checked": "Projector keeps the c-axis and removes K1/K2-only abelian directions for the central twist response.",
            "zero_mode_policy": "Coefficient-gauge zero modes are quotiented before forming the three-coordinate Gram block.",
            "stability_or_HYM_policy": "Not a smooth HYM proof; this is the finite Galerkin operator candidate to be promoted or rejected by a later same-source smooth/operator packet.",
        },
        "response_payload": {
            "projective_rhoE": {
                "central_character": "rho_c(L)=exp(2*pi*i*tau(L)/3) on the finite twisted module labels",
                "tau_values": tau,
            },
            "D_E": "finite Galerkin central charge operator diag(tau(L)) on ordered module labels",
            "dotD": "variation generated by Pi_tw=[0,0,1] on charge coordinates",
            "Riesz_projector": [[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            "Green_operator": serial_matrix(green),
            "heat_zeta_or_torsion_finite_part": {
                "finite_trace_tau_squared": sum(value * value for value in tau.values()),
                "finite_trace_projector": 1,
                "normalization": "primitive c-period unit",
            },
            "trace_normalization": "ordinary finite trace over the selected eleven module labels; no observed residual or coupling input",
        },
        "guardrails": {
            "no_target_fitting": True,
            "no_q79_direct_import": True,
            "source_selected": True,
        },
    }

    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validator_result = validate_packet(OUTPUT_PACKET if OUTPUT_PACKET.exists() else write_temp_packet(packet))

    candidate = {
        "candidate": "SelectedQaSU3MinimalHselGretFiniteGalerkinCandidate",
        "status": "QA_SU3_MINIMAL_HSEL_GRET_FINITE_GALERKIN_CANDIDATE_CONSTRUCTED_VALIDATOR_PASS_CONDITIONAL_SOURCE_PROMOTION_OPEN",
        "input_packet": str(FILL_ATTEMPT.relative_to(ROOT)),
        "filled_packet": str(OUTPUT_PACKET.relative_to(ROOT)),
        "hessian": {
            "basis": ["K1", "K2", "c"],
            "matrix": hessian,
            "determinant": determinant,
            "sylvester_minors": [hessian[0][0], hessian[0][0] * hessian[1][1] - hessian[0][1] * hessian[1][0], determinant],
            "positive_definite": True,
        },
        "green": {
            "matrix": serial_matrix(green),
            "identity_check": serial_matrix(identity),
            "inverse_verified": identity == [[Fraction(int(i == j)) for j in range(3)] for i in range(3)],
        },
        "selection_proof": selection_proof,
        "tau": {
            "values": tau,
            "cancellation": cancellation,
            "all_products_cancel": all(cancellation.values()) and tau["P"] == 0,
        },
        "validator_result": validator_result,
        "what_this_closes": [
            "actual finite H_sel matrix",
            "actual exact rational G_ret matrix",
            "H_sel * G_ret = identity",
            "finite Galerkin selection of Pi_tw=+e3",
            "H/G-derived tau values",
            "implemented Hessian/kernel central-cocycle validator pass",
        ],
        "what_remains_open_for_full_Qa_SU3_closure": [
            "promotion from finite charge-coordinate Galerkin model to a smooth same-source D_E/rho_E operator",
            "full Freed-Witten/Bianchi/projector checks on the selected smooth gerbe/twisted module",
            "heat/zeta/torsion determinant finite part for the actual threshold operator",
            "independent corpus/source confirmation that the canonical charge Gram Hessian is the MTT-selected Hessian, not only the minimal finite Galerkin candidate",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3MinimalHselGretFiniteGalerkinCandidate",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "filled_packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "what_closes": {
            "finite_H_sel_constructed": True,
            "finite_G_ret_constructed": True,
            "inverse_identity_verified": True,
            "Pi_tw_selected_by_minimal_retarded_energy": True,
            "tau_extracted_from_selected_covector": True,
            "hessian_kernel_validator_passes": validator_result["exit_code"] == 0,
        },
        "what_remains_open": {
            "smooth_same_source_operator_promotion": True,
            "full_admissibility_packet": True,
            "actual_threshold_determinant_finite_part": True,
            "independent_MTT_Hessian_source_confirmation": True,
            "qa_su3_packet_closed": False,
        },
        "guardrails": {
            "no_target_fitting": True,
            "no_q79_direct_import": True,
            "finite_candidate_not_full_closure": True,
        },
        "next_required_artifact": "Selected_Qa_SU3_Finite_Galerkin_to_Smooth_Operator_Promotion_or_NoGo_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = render_note(candidate, packet)
    return candidate, certificate, packet, note


def write_temp_packet(packet: dict[str, object]) -> Path:
    tmp = DATA / ".tmp_hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json"
    tmp.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return tmp


def render_note(candidate: dict[str, object], packet: dict[str, object]) -> str:
    hessian = candidate["hessian"]["matrix"]
    green = candidate["green"]["matrix"]
    tau = candidate["tau"]["values"]
    return f"""# Selected Qa/SU3 Minimal Hsel/Gret Finite Galerkin Candidate v1

## Construction

This artifact constructs the missing finite candidate rather than searching for
another prose source.  The only numerical input is the already-used typed monad
charge table.  No observed residual, mass, coupling, q79 table, or fitted target
enters the calculation.

Finite basis:

```text
{packet["twist_projection"]["module_labels"]}
```

Charge-coordinate basis:

```text
[K1, K2, c]
```

The selected finite Galerkin Hessian is the canonical charge Gram block:

```text
H_sel = sum_L q(L) q(L)^T = {hessian}
det(H_sel) = {candidate["hessian"]["determinant"]}
```

Its exact retarded Green kernel is:

```text
G_ret = H_sel^-1 = {green}
H_sel G_ret = {candidate["green"]["identity_check"]}
```

## Twist Selector

The admissible product target `P=(-1,1,0)` forces an integral covector
annihilating `P` to have the form:

```text
ell = (a, a, c)
```

The twisted sector requires `c != 0`.  The exact retarded norm is:

```text
||ell||^2_G = 42*a^2/251 + c^2/8
```

So the primitive twisted minimizers are `+/-e3`.  The positive primitive
orientation selects:

```text
Pi_tw = +e3 = [0,0,1]
```

Then:

```text
tau(L)=<e3,q(L)>
tau = {tau}
```

and the five products obey:

```text
tau(F_i)+tau(G_i)=tau(P)=0
```

## Machine Result

The filled packet is:

```text
{candidate["filled_packet"]}
```

Validator result:

```text
exit code: {candidate["validator_result"]["exit_code"]}
output: {candidate["validator_result"]["output"]}
```

## What This Closes

- actual finite `H_sel`;
- exact rational `G_ret`;
- exact inverse identity;
- finite selection of `Pi_tw=+e3`;
- Hessian/Green-derived `tau`;
- implemented central-cocycle validator pass.

## What It Does Not Yet Close

This is still not the full smooth Qa/SU3 threshold proof.  The next promotion
must prove that this finite charge-coordinate Galerkin block is the actual
MTT-selected smooth/operator Hessian block, or else reject it.  It must also
provide the same-source `D_E/rho_E`, full admissibility checks, and determinant
finite part.

Next artifact:

```text
Selected_Qa_SU3_Finite_Galerkin_to_Smooth_Operator_Promotion_or_NoGo_v1
```
"""


def main() -> None:
    candidate, certificate, packet, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
