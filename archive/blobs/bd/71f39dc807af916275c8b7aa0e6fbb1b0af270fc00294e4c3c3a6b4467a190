"""Audit the Iwasawa typed monad-map data gate."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_monad_map_data_gate_certificate.json"
PREVIOUS = CERT_DIR / "iwasawa_dolbeault_complex_extraction_certificate.json"
PAPER = ROOT / "Iwasawa_Monad_Map_Data_Gate_for_Three_Family_Slots_v1.md"
FLUX = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)


LINE_CLASSES: dict[str, tuple[int, int, int]] = {
    "L1": (-2, 0, 1),
    "L2": (-1, 1, -1),
    "L3": (1, -1, 0),
    "L4": (1, 0, -1),
    "L5": (2, 1, 1),
    "K1": (1, 0, 0),
    "K2": (0, 1, 0),
}


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def vector_add(*vectors: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(vector[index] for vector in vectors) for index in range(3))  # type: ignore[return-value]


def vector_sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def pair_vector(vector: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = vector
    return (x * y, x * z, y * z)


def triple_number(vector: tuple[int, int, int]) -> int:
    x, y, z = vector
    return x * y * z


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    cert = load_json(CERT)
    previous = load_json(PREVIOUS)
    paper = read(PAPER)
    flux = read(FLUX)

    l_keys = ["L1", "L2", "L3", "L4", "L5"]
    sum_l = vector_add(*(LINE_CLASSES[key] for key in l_keys))
    sum_k = vector_add(LINE_CLASSES["K1"], LINE_CLASSES["K2"])
    ch2_l = vector_add(*(pair_vector(LINE_CLASSES[key]) for key in l_keys))
    ch2_k = vector_add(pair_vector(LINE_CLASSES["K1"]), pair_vector(LINE_CLASSES["K2"]))
    ch3_integral = 2 * (
        sum(triple_number(LINE_CLASSES[key]) for key in l_keys)
        - triple_number(LINE_CLASSES["K1"])
        - triple_number(LINE_CLASSES["K2"])
    )

    f_types = {
        f"f{index}_{key}_tensor_K1_inverse": vector_sub(LINE_CLASSES[key], LINE_CLASSES["K1"])
        for index, key in enumerate(l_keys, start=1)
    }
    g_types = {
        f"g{index}_K2_tensor_{key}_inverse": vector_sub(LINE_CLASSES["K2"], LINE_CLASSES[key])
        for index, key in enumerate(l_keys, start=1)
    }
    scalar_f_entries = [name for name, vector in f_types.items() if vector == (0, 0, 0)]
    scalar_g_entries = [name for name, vector in g_types.items() if vector == (0, 0, 0)]

    cert_source = cert.get("source_monad", {})
    cert_topology = cert.get("topological_cern_check", {})
    cert_typed = cert.get("typed_map_check", {})
    cert_consequence = cert.get("consequence_for_sm_closure", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status")
            == "IWASAWA_MONAD_MAP_DATA_GATE_BLOCKED_TYPED_MAP_SECTIONS_MISSING"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "previous A01 obstruction",
            "PASS"
            if previous.get("literal_integrability_result", {}).get("integrable") is False
            and previous.get("minimal_repair_candidate", {}).get("cohomology_dimensions", {}).get("h1") == 2
            else "FAIL",
            str(previous.get("status")),
        ),
        Gate(
            "source monad present",
            "PASS"
            if contains_all(flux, ["0\\longrightarrow K_1", "E:=\\ker g / \\mathrm{im}\\,f"])
            else "FAIL",
            str(FLUX),
        ),
        Gate(
            "source generic constant phrase",
            "PASS"
            if "generic holomorphic maps $f,g$" in flux and "constant matrices in the left-invariant frame" in flux
            else "FAIL",
            "source phrase checked",
        ),
        Gate(
            "source lacks explicit map entries",
            "PASS"
            if cert_source.get("source_gives_explicit_f_entries") is False
            and cert_source.get("source_gives_explicit_g_entries") is False
            else "FAIL",
            str(cert_source),
        ),
        Gate(
            "c1 zero",
            "PASS" if sum_l == sum_k and cert_topology.get("c1_zero") is True else "FAIL",
            f"sum_L={sum_l}, sum_K={sum_k}",
        ),
        Gate(
            "ch2 zero",
            "PASS" if ch2_l == ch2_k and cert_topology.get("ch2_zero") is True else "FAIL",
            f"sum_pair_L={ch2_l}, sum_pair_K={ch2_k}",
        ),
        Gate(
            "integral c3 six",
            "PASS" if ch3_integral == 6 == cert_topology.get("integral_c3") else "FAIL",
            str(ch3_integral),
        ),
        Gate(
            "f scalar constants blocked by type",
            "PASS"
            if not scalar_f_entries
            and cert_typed.get("nonzero_scalar_constant_f_entries_type_valid") is False
            else "FAIL",
            str(f_types),
        ),
        Gate(
            "g scalar constants blocked by type",
            "PASS"
            if not scalar_g_entries
            and cert_typed.get("nonzero_scalar_constant_g_entries_type_valid") is False
            else "FAIL",
            str(g_types),
        ),
        Gate(
            "typed sections required",
            "PASS"
            if cert_typed.get("requires_global_holomorphic_sections_or_transition_data") is True
            and cert_typed.get("can_verify_g_after_f_zero") is False
            and cert_typed.get("can_verify_monad_exactness") is False
            else "FAIL",
            str(cert_typed),
        ),
        Gate(
            "SM matrices blocked",
            "PASS"
            if cert_consequence.get("can_compute_H1_X_E_from_current_monad_data") is False
            and cert_consequence.get("can_compute_primitive_C1_response_blocks") is False
            and cert_consequence.get("can_claim_no_proxy_yukawa_matrices") is False
            else "FAIL",
            str(cert_consequence),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("uses_scalar_constant_maps_without_type_check") is False
            and guardrails.get("uses_c3_index_as_explicit_zero_mode_basis") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("topological_three_net_family_data_supported") is True
            and verdict.get("typed_monad_route_open_but_data_missing") is True
            and "typed monad sections" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records data gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "The remaining source route is the monad route",
                    "None of these classes is zero",
                    "topological three-net-family data: supported",
                    "monad route: blocked until typed maps f,g are supplied",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa monad map data gate audit")
    print("=================================")
    print()
    print(f"sum_L={sum_l}")
    print(f"sum_K={sum_k}")
    print(f"ch2_pair_sum_L={ch2_l}")
    print(f"ch2_pair_sum_K={ch2_k}")
    print(f"integral_c3={ch3_integral}")
    print(f"scalar_f_entries={scalar_f_entries}")
    print(f"scalar_g_entries={scalar_g_entries}")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
