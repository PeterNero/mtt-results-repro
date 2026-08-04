"""Build the q79 S3 sheet-monodromy and binary Spin(3) lift reduction."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79signedsheetspinliftreduction"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "q79_signed_sheet_spin_lift_reduction.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79SignedSheetSpinLiftReduction_v1.md"

FB1_CERT = (
    ROOT
    / "certificates"
    / "selected_q79tracesplitclncarrierandworldinworldbridge_certificate.json"
)
FB1_PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79tracesplitclncarrierandworldinworldbridge"
    / "q79_trace_split_cln_carrier_and_bridge_cutset.packet.json"
)
A103_COVER = (
    ROOT
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
    / "q79_genus_two_determinant_zero_spectral_cover.packet.json"
)
A104_TOPOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
    / "spectral_surface_invariants.packet.json"
)
A110_CERT = (
    ROOT
    / "certificates"
    / "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution_certificate.json"
)


@dataclass(frozen=True)
class Qsqrt2:
    """Exact a+b*sqrt(2) arithmetic."""

    rational: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)

    def __add__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational + other.rational, self.radical + other.radical)

    def __sub__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational - other.rational, self.radical - other.radical)

    def __neg__(self) -> Qsqrt2:
        return Qsqrt2(-self.rational, -self.radical)

    def __mul__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(
            self.rational * other.rational + 2 * self.radical * other.radical,
            self.rational * other.radical + self.radical * other.rational,
        )

    def __str__(self) -> str:
        if self.radical == 0:
            return str(self.rational)
        if self.rational == 0:
            return f"{self.radical}*sqrt(2)"
        sign = "+" if self.radical > 0 else "-"
        return f"{self.rational}{sign}{abs(self.radical)}*sqrt(2)"


Quaternion = tuple[Qsqrt2, Qsqrt2, Qsqrt2, Qsqrt2]
Matrix = list[list[Qsqrt2]]

ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))
MINUS_ONE = Qsqrt2(Fraction(-1))
ROOT_HALF = Qsqrt2(Fraction(0), Fraction(1, 2))
Q_ONE: Quaternion = (ONE, ZERO, ZERO, ZERO)
Q_MINUS_ONE: Quaternion = (MINUS_ONE, ZERO, ZERO, ZERO)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def q_add(left: Quaternion, right: Quaternion) -> Quaternion:
    return tuple(left[index] + right[index] for index in range(4))  # type: ignore[return-value]


def q_neg(value: Quaternion) -> Quaternion:
    return tuple(-entry for entry in value)  # type: ignore[return-value]


def q_mul(left: Quaternion, right: Quaternion) -> Quaternion:
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )


def q_pow(value: Quaternion, exponent: int) -> Quaternion:
    output = Q_ONE
    for _ in range(exponent):
        output = q_mul(output, value)
    return output


def rotation_matrix(value: Quaternion) -> Matrix:
    w, x, y, z = value
    two = Qsqrt2(Fraction(2))
    return [
        [
            ONE - two * (y * y + z * z),
            two * (x * y - w * z),
            two * (x * z + w * y),
        ],
        [
            two * (x * y + w * z),
            ONE - two * (x * x + z * z),
            two * (y * z - w * x),
        ],
        [
            two * (x * z - w * y),
            two * (y * z + w * x),
            ONE - two * (x * x + y * y),
        ],
    ]


def integer_matrix(rows: list[list[int]]) -> Matrix:
    return [[Qsqrt2(Fraction(entry)) for entry in row] for row in rows]


def encode_quaternion(value: Quaternion) -> list[str]:
    return [str(entry) for entry in value]


def encode_matrix(value: Matrix) -> list[list[str]]:
    return [[str(entry) for entry in row] for row in value]


def generated_group(generators: list[Quaternion]) -> set[Quaternion]:
    group = {Q_ONE}
    frontier = [Q_ONE]
    expanded_generators = generators + [q_neg(generator) for generator in generators]
    while frontier:
        current = frontier.pop()
        for generator in expanded_generators:
            candidate = q_mul(current, generator)
            if candidate not in group:
                group.add(candidate)
                frontier.append(candidate)
    return group


def main() -> int:
    fb1_cert = load(FB1_CERT)
    fb1 = load(FB1_PACKET)
    cover = load(A103_COVER)
    topology = load(A104_TOPOLOGY)
    a110 = load(A110_CERT)

    if not fb1_cert["q79_trace_split_rank_1_2_3_carrier_closed"]:
        raise AssertionError("FB1 carrier theorem changed")
    if not fb1["monodromy_and_orientation_theorem"]["rho_plus_lies_in_SO3"]:
        raise AssertionError("FB1 SO3 orientation correction changed")
    if cover["q79_genus_two_map"]["map"] != "phi_H:K3 -> P2, generically a double cover branched over a sextic":
        raise AssertionError("q79 genus-two map changed")
    if topology["Lefschetz_and_Hodge"]["betti"][0] != 1:
        raise AssertionError("q79 spectral surface connectedness changed")
    if not a110["checks"]["elliptic_curve_smooth"]:
        raise AssertionError("A110 elliptic smoothness changed")
    if not a110["checks"]["spectral_surface_smooth"]:
        raise AssertionError("A110 spectral surface smoothness changed")

    # Lifts of the signed transpositions (01) and (12). Each is a pi rotation
    # about the corresponding trace-zero axis.
    q1: Quaternion = (ZERO, ROOT_HALF, -ROOT_HALF, ZERO)
    q2: Quaternion = (ZERO, ZERO, ROOT_HALF, -ROOT_HALF)
    expected_r1 = integer_matrix([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])
    expected_r2 = integer_matrix([[-1, 0, 0], [0, 0, -1], [0, -1, 0]])
    braid_left = q_mul(q_mul(q1, q2), q1)
    braid_right = q_mul(q_mul(q2, q1), q2)
    generated = generated_group([q1, q2])

    exact_checks = {
        "q1_unit": q_mul(q1, q_neg(q1)) == Q_ONE,
        "q2_unit": q_mul(q2, q_neg(q2)) == Q_ONE,
        "q1_square_is_minus_one": q_pow(q1, 2) == Q_MINUS_ONE,
        "q2_square_is_minus_one": q_pow(q2, 2) == Q_MINUS_ONE,
        "braid_relation_exact": braid_left == braid_right,
        "product_cube_is_minus_one": q_pow(q_mul(q1, q2), 3) == Q_MINUS_ONE,
        "q1_projects_to_signed_transposition_01": rotation_matrix(q1) == expected_r1,
        "q2_projects_to_signed_transposition_12": rotation_matrix(q2) == expected_r2,
        "binary_preimage_has_order_12": len(generated) == 12,
        "central_minus_one_generated": Q_MINUS_ONE in generated,
    }
    if not all(exact_checks.values()):
        failed = [name for name, value in exact_checks.items() if not value]
        raise AssertionError(f"binary Spin lift checks failed: {failed}")

    global_spin_contract = {
        "q79_K3_sheet_branch_complement_fundamental_group_presentation": False,
        "all_global_monodromy_relators_lift_with_positive_central_sign": False,
        "w2_of_signed_sheet_carrier_proved_zero": False,
        "Spin_lift_extended_across_ramification_or_replaced_by_smooth_HYM_carrier": False,
        "shared_circle_Z2_cancellation_selected_if_SpinC_route_used": False,
    }

    packet = {
        "schema": "MTTSelectedQ79SignedSheetSpinLiftReduction.v1",
        "status": "Q79_SHEET_MONODROMY_S3_AND_LOCAL_BINARY_SPIN_LIFT_CLOSED_GLOBAL_Z2_RELATOR_AND_BRANCH_EXTENSION_OPEN",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in (FB1_CERT, FB1_PACKET, A103_COVER, A104_TOPOLOGY, A110_CERT, Path(__file__))
        ],
        "q79_sheet_monodromy_theorem": {
            "degree": 3,
            "spectral_surface_connected": True,
            "monodromy_transitive": True,
            "K3_to_linear_system_map_surjective": True,
            "ordinary_nonflex_tangencies_exist": True,
            "local_transposition_present": True,
            "transitive_subgroup_of_S3_with_transposition": "S3",
            "monodromy_group": "S3",
            "proved": True,
            "alignment_independence": "every PGL3 alignment is an isomorphism of the hyperplane-parameter P2 and preserves the existence of ordinary tangencies",
        },
        "binary_spin_theorem": {
            "oriented_sheet_action": "rho_plus(sigma)=sign(sigma)P_sigma in SO3",
            "Spin3_preimage": "binary dihedral group Dic_3 of order 12",
            "group_extension": "1 -> {+1,-1} -> Dic_3 -> S3 -> 1",
            "extension_splits": False,
            "non_split_reason": "every lift of a transposition is a pi-rotation spinor with square -1, so no lift can preserve s^2=1",
            "local_braid_lift_exists": True,
            "braid_generators": {
                "q1": encode_quaternion(q1),
                "q2": encode_quaternion(q2),
                "q1_rotation": encode_matrix(rotation_matrix(q1)),
                "q2_rotation": encode_matrix(rotation_matrix(q2)),
            },
            "relations": {
                "q1_squared": "-1",
                "q2_squared": "-1",
                "q1_q2_q1_equals_q2_q1_q2": True,
                "q1_q2_cubed": "-1",
            },
            "generated_group_order": len(generated),
            "checks": exact_checks,
        },
        "interpretation": {
            "proto_spinor_match": "the correct finite target is the binary lift of path/braid monodromy, not an ordinary representation of S3",
            "global_S3_section_forbidden": True,
            "strict_Spin_route": "compute the central sign of every actual q79 branch-complement relator and prove w2=0",
            "shared_circle_route": "if the central obstruction is nonzero, a selected order-two shared-circle holonomy can define a SpinC-type cancellation, but this is not a strict Spin3 proof",
            "continuous_parameters_added": 0,
        },
        "global_spin_contract": {
            "fields": global_spin_contract,
            "closed_count": sum(global_spin_contract.values()),
            "required_count": len(global_spin_contract),
            "global_Spin_lift_closed": all(global_spin_contract.values()),
        },
        "worldinworld_Q_source_status": {
            "oriented_rank3_target_carrier_closed": True,
            "local_binary_path_lift_closed": True,
            "selected_Q_or_closure_Hessian_emitted": False,
            "worldinworld_to_q79_same_source_intertwiner_closed": False,
        },
        "next_required_artifact": "MTT_Selected_q79SheetMonodromyGlobalRelatorAndSpinOrSpinCDecision_v1",
    }
    dump(PACKET, packet)

    note = """# MTT Selected q79 Signed-Sheet Spin-Lift Reduction v1

## Exact q79 sheet monodromy

The degree-three q79 cover has connected total space, so its generic sheet
monodromy is transitive. The genus-two polarization map is a double cover of
`P2`, hence surjective, and every `PGL(3)` alignment is an isomorphism of that
`P2` with the hyperplane linear system `|3*0|` of the smooth elliptic cubic.
Ordinary tangent lines to a smooth cubic give one double and one simple
intersection point, so the cover has local transposition monodromy. A
transitive subgroup of `S3` containing a transposition is all of `S3`.

Thus the q79 three-sheet monodromy group is structurally

```text
Mon(C/K3)=S3.
```

This result is independent of the numerical `PGL(3)` alignment.

## Binary Spin lift

FB1 replaced the orientation-reversing permutation action by

```text
rho_plus(sigma)=sign(sigma) P_sigma in SO(3).
```

The inverse image of this rotational `S3` in `Spin(3)=SU(2)` is the binary
dihedral group `Dic_3` of order 12:

```text
1 -> {+1,-1} -> Dic_3 -> S3 -> 1.
```

Choose exact quaternion lifts of the adjacent transpositions,

```text
q1=(i-j)/sqrt(2),
q2=(j-k)/sqrt(2).
```

The audit proves exactly

```text
q1^2=q2^2=-1,
q1 q2 q1=q2 q1 q2,
(q1 q2)^3=-1,
|<q1,q2>|=12.
```

So local braid/path monodromy has an exact `Spin(3)` lift. However the central
extension does not split as a representation of `S3`: every lift of a
transposition squares to `-1`, not `+1`. This is exactly the double-return
behavior required by the proto-spinor narrative.

## What remains

The global question is now finite and sharp. One must obtain a presentation of
the actual q79 `K3` sheet-branch complement, lift its generators by the binary
rules above, and evaluate the central sign of every relator. All signs `+1`
prove a strict Spin lift and `w2=0`. A surviving `-1` is the obstruction.

If that obstruction is nonzero, a selected order-two holonomy on the shared
circle could cancel it in a SpinC-type construction. That would use the shared
circle in a mathematically standard way, but it must not be reported as a
strict `Spin(3)` lift unless the obstruction itself vanishes.

Closed here:

```text
q79 sheet monodromy group S3,
binary preimage Dic_3,
non-splitting over S3,
exact local braid lift.
```

Still open:

```text
global q79 relator signs / w2,
extension across the branch locus or smooth HYM replacement,
any selected shared-circle Z2 cancellation,
the actual world-in-world Q/Hessian source.
```

No observed Standard Model value and no fitted continuous parameter is used.

Next artifact:
`MTT_Selected_q79SheetMonodromyGlobalRelatorAndSpinOrSpinCDecision_v1`.
"""
    NOTE.write_text(note, encoding="utf-8")

    candidate = {
        "schema": "MTTSelectedQ79SignedSheetSpinLiftReduction.v1",
        "artifact": "FoundationalBridge-FB2",
        "status": packet["status"],
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "new_fitted_continuous_parameters": 0,
        "what_closes": {
            "q79_sheet_monodromy_group_S3": True,
            "binary_Dic3_preimage": True,
            "ordinary_S3_spin_section_no_go": True,
            "local_braid_spin_lift": True,
        },
        "what_remains_open": {
            "global_relator_signs_and_w2": True,
            "branch_locus_extension": True,
            "shared_circle_SpinC_decision": True,
            "selected_worldinworld_Q_source": True,
        },
        "next_required_artifact": packet["next_required_artifact"],
    }
    dump(CANDIDATE, candidate)

    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79SignedSheetSpinLiftReduction",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate["status"],
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "new_fitted_continuous_parameters": 0,
        "q79_sheet_monodromy_S3_closed": True,
        "local_binary_spin_lift_closed": True,
        "global_spin_lift_closed": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(CERTIFICATE, certificate)

    print(f"wrote {relative(PACKET)}")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(f"wrote {relative(NOTE)}")
    print("closed: q79 sheet monodromy is S3")
    print("closed: local binary Spin(3) braid lift generates Dic_3 of order 12")
    print("open: global relator signs, w2, and branch-locus continuation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
