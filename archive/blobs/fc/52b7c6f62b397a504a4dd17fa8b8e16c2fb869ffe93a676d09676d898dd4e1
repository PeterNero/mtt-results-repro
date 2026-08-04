"""Audit the attempted recovery of typed Iwasawa monad sections."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_typed_monad_section_recovery_certificate.json"
SPECTRAL_TEMPLATE = CERT_DIR / "iwasawa_spectral_galerkin_data.template.json"
PAPER = ROOT / "Iwasawa_Typed_Monad_Section_Recovery_Attempt_v1.md"
FLUX = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
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


def vector_sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def explicit_map_entries_present(text: str, prefix: str) -> bool:
    for index in range(1, 6):
        patterns = [
            rf"{prefix}_{index}\s*(?:=|:=|\\in)",
            rf"{prefix}_\{{{index}\}}\s*(?:=|:=|\\in)",
            rf"{prefix}{index}\s*(?:=|:=|\\in)",
        ]
        if any(re.search(pattern, text) for pattern in patterns):
            return True
    return False


def main() -> None:
    cert = load_json(CERT)
    template = load_json(SPECTRAL_TEMPLATE)
    paper = read(PAPER)
    flux = read(FLUX)

    l_keys = ["L1", "L2", "L3", "L4", "L5"]
    f_types = {
        f"f{index}": vector_sub(LINE_CLASSES[key], LINE_CLASSES["K1"])
        for index, key in enumerate(l_keys, start=1)
    }
    g_types = {
        f"g{index}": vector_sub(LINE_CLASSES["K2"], LINE_CLASSES[key])
        for index, key in enumerate(l_keys, start=1)
    }
    all_hom_nonzero = all(vector != (0, 0, 0) for vector in [*f_types.values(), *g_types.values()])
    source_has_f_entries = explicit_map_entries_present(flux, "f")
    source_has_g_entries = explicit_map_entries_present(flux, "g")

    recovered = cert.get("recovered_from_corpus", {})
    missing = cert.get("not_recovered_from_corpus", {})
    typing = cert.get("typing_obstruction_confirmed", {})
    route = cert.get("route_decision", {})
    fallback = cert.get("spectral_fallback_contract", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    required_missing = [
        "explicit_f_i_section_representatives",
        "explicit_g_i_section_representatives",
        "transition_functions_for_L_i_K1_K2",
        "Cech_cover_and_cocycles",
        "line_bundle_cohomology_tables_for_Hom_bundles",
        "g_after_f_zero_certificate",
        "monad_exactness_or_sheaf_singularity_control",
        "long_exact_sequence_maps",
        "selected_H1_E_representatives",
        "anti_family_vanishing_certificate",
        "sector_projection_maps_Q_u_d_L_e_N_H",
        "dotD_alpha1_and_Green_operator_data",
    ]
    fallback_must = " ".join(fallback.get("must_supply", []))

    gates = [
        Gate(
            "certificate status",
            "TRIGGERED"
            if cert.get("status") == "TYPED_MONAD_SECTIONS_NOT_RECOVERED_SPECTRAL_FALLBACK_TRIGGERED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "flux source present",
            "PASS" if FLUX.exists() else "FAIL",
            str(FLUX),
        ),
        Gate(
            "source monad recovered",
            "PASS"
            if recovered.get("monad_sequence") is True
            and contains_all(flux, ["0\\longrightarrow K_1", "E:=\\ker g / \\mathrm{im}\\,f"])
            else "FAIL",
            str(recovered),
        ),
        Gate(
            "source generic-map phrase recovered",
            "PASS"
            if recovered.get("generic_constant_maps_phrase") is True
            and "constant matrices in the left-invariant frame" in flux
            else "FAIL",
            "generic holomorphic maps phrase checked",
        ),
        Gate(
            "no explicit f entries in source",
            "PASS" if not source_has_f_entries and missing.get("explicit_f_i_section_representatives") is True else "FAIL",
            str(source_has_f_entries),
        ),
        Gate(
            "no explicit g entries in source",
            "PASS" if not source_has_g_entries and missing.get("explicit_g_i_section_representatives") is True else "FAIL",
            str(source_has_g_entries),
        ),
        Gate(
            "missing data inventory",
            "PASS" if all(missing.get(key) is True for key in required_missing) else "FAIL",
            ", ".join(required_missing),
        ),
        Gate(
            "Hom c1 vectors nonzero",
            "PASS" if all_hom_nonzero and typing.get("all_Hom_c1_vectors_nonzero") is True else "FAIL",
            f"f={f_types}, g={g_types}",
        ),
        Gate(
            "scalar constant maps blocked",
            "PASS"
            if typing.get("nonzero_scalar_constant_entries_globally_typed") is False
            and "local-frame shorthand" in typing.get("interpretation", "")
            else "FAIL",
            str(typing),
        ),
        Gate(
            "fallback route triggered",
            "PASS"
            if route.get("typed_monad_cech_can_close_now") is False
            and route.get("non_invariant_spectral_galerkin_fallback_triggered") is True
            else "FAIL",
            str(route),
        ),
        Gate(
            "fallback contract strict",
            "PASS"
            if contains_all(
                fallback_must,
                [
                    "basis that extends beyond left-invariant forms",
                    "Riesz projector",
                    "anti-family",
                    "dotD_alpha1",
                    "Green operator",
                ],
            )
            else "FAIL",
            str(fallback),
        ),
        Gate(
            "spectral template present",
            "PASS"
            if template.get("certificate") == "IwasawaSpectralGalerkinDataTemplate"
            and template.get("mode") == "non_invariant_spectral_galerkin"
            and template.get("success_gates", {}).get("kernel_dimension_is_three") is False
            else "FAIL",
            str(template.get("certificate")),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_typed_monad_sections_exist") is False
            and guardrails.get("uses_constant_scalar_maps_without_transition_data") is False
            and guardrails.get("uses_index_as_zero_mode_basis") is False
            and guardrails.get("silently_repairs_A01") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("closes_corpus_recovery_attempt") is True
            and verdict.get("closes_selected_H1_E_values") is False
            and verdict.get("next_template") == "iwasawa_spectral_galerkin_data.template.json"
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records fallback trigger",
            "PASS"
            if contains_all(
                paper,
                [
                    "The answer is no",
                    "None is zero",
                    "fallback condition",
                    "non-invariant spectral Galerkin route",
                    "build the Iwasawa non-invariant spectral Galerkin operator certificate",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa typed monad section recovery audit")
    print("==========================================")
    print()
    print(f"source_has_f_entries={source_has_f_entries}")
    print(f"source_has_g_entries={source_has_g_entries}")
    print(f"f_types={f_types}")
    print(f"g_types={g_types}")
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
