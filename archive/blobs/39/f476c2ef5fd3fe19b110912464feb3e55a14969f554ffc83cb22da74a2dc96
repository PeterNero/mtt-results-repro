"""Attempt to select the twisted D7 stack from executed CY volume data.

The finite twisted Chan-Paton rescue reduces the coordinate route to choosing
one twisted D7 stack among S1,S2,S3.  This script tests whether the executed
Kahler/divisor-volume data distinguish one of those choices.

Result: S3 is the unique volume-anisotropic candidate.  It is the only divisor
with tau_a/tau_1 ~= 0.229, while S1 and S2 remain exactly degenerate in the
executed corner.  Therefore any future MTT rule that attaches the qutrit twist
to the unique anisotropic/small-volume divisor would select S3.  That rule is
not yet proved here, so the result is a conditional selector attempt.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXEC_I = ROOT / "proof_corpus" / "Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v2.md"
RESCUE_CERT = ROOT / "certificates" / "visible_twisted_chan_paton_rescue_certificate.json"
OUT_CANDIDATE = ROOT / "candidate_data" / "visible_twisted_d7_volume_selector_attempt.candidate.json"
OUT_CERT = ROOT / "certificates" / "visible_twisted_d7_volume_selector_attempt_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def first_float(pattern: str, text: str) -> float | None:
    match = re.search(pattern, text, flags=re.MULTILINE)
    return float(match.group(1)) if match else None


def source_values(text: str) -> dict[str, Any]:
    # Use the printed source values when present, and independently recompute
    # the same hierarchy from the stated Tier-3 ratios and K/(4*pi).
    zeta31 = first_float(r"\\frac\{\\zeta_3\}\{\\zeta_1\}\s*=\s*([0-9.]+)", text)
    if zeta31 is None:
        zeta31 = first_float(r"\\frac\{\\zeta_3\}\{\\zeta_1\}[\s\S]*?([0-9]+\.[0-9]+)", text)
    volume = 45.0 / (4.0 * math.pi)
    ratio = zeta31 or 0.229
    t = (volume * ratio) ** (1.0 / 3.0)
    t3 = t / ratio
    tau = {
        "S1": t * t3,
        "S2": t * t3,
        "S3": t * t,
    }
    return {
        "source_hits": {
            "zeta2_over_zeta1_equals_one": "\\frac{\\zeta_2}{\\zeta_1}" in text and "= 1" in text,
            "zeta3_over_zeta1_0229": "0.229" in text,
            "t1_equals_t2": "t_1 = t_2" in text,
            "t3_large": "t_3 \\simeq 4.11" in text or "t_3 \\simeq 4.37" in text,
            "tau_values_printed": "\\tau_1 &= t_2 t_3 \\simeq 3.86" in text
            and "\\tau_3 &= t_1 t_2 \\simeq 0.88" in text,
            "moderately_anisotropic": "moderately anisotropic" in text,
        },
        "computed_from_tier3": {
            "volume_K_over_4pi": volume,
            "zeta3_over_zeta1": ratio,
            "t1": t,
            "t2": t,
            "t3": t3,
            "tau": tau,
            "tau3_over_tau1": tau["S3"] / tau["S1"],
        },
    }


def build_certificate() -> dict[str, Any]:
    text = read(EXEC_I)
    values = source_values(text)
    rescue = load_json(RESCUE_CERT)
    tau = values["computed_from_tier3"]["tau"]
    sorted_tau = sorted(tau.items(), key=lambda item: item[1])
    unique_min = sorted_tau[0][0] if sorted_tau[0][1] < sorted_tau[1][1] else None
    degenerate_max = abs(tau["S1"] - tau["S2"]) < 1e-12 and tau["S1"] > tau["S3"]

    rescue_choices = rescue.get("coordinate_rescue_enumeration", {}).get(
        "twisted_D7_stack_choices", []
    )
    candidate_present = unique_min in rescue_choices
    conditional_s3_selector = (
        rescue.get("status")
        == "VISIBLE_TWISTED_CP_MINIMAL_COORDINATE_RESCUE_REDUCED_SELECTION_OPEN"
        and unique_min == "S3"
        and degenerate_max
        and candidate_present
        and all(values["source_hits"].values())
    )

    status = (
        "VISIBLE_TWISTED_D7_VOLUME_SELECTOR_ATTEMPT_S3_CONDITIONAL_SELECTION_OPEN"
        if conditional_s3_selector
        else "VISIBLE_TWISTED_D7_VOLUME_SELECTOR_ATTEMPT_INCONCLUSIVE"
    )
    return {
        "certificate": "VisibleTwistedD7VolumeSelectorAttempt",
        "status": status,
        "generated_by": "scripts/attempt_select_visible_twisted_d7_by_volume.py",
        "depends_on": [
            str(RESCUE_CERT.relative_to(ROOT)),
            str(EXEC_I.relative_to(ROOT)),
        ],
        "executed_volume_data": values,
        "rescue_choices": rescue_choices,
        "volume_ordering": [
            {"stack": stack, "tau": value}
            for stack, value in sorted_tau
        ],
        "conditional_selector": {
            "rule_not_yet_proved": "attach the qutrit projective twist to the unique anisotropic/small-volume divisor carrying the zeta3/zeta1=0.229 hierarchy",
            "selected_if_rule_is_added": unique_min,
            "reason": "S1 and S2 are volume-degenerate; S3 is the only divisor with tau_a/tau_1 ~= 0.229.",
            "equivalent_active_direction_picture": "twisted S3 corresponds to placing e1,e2 on T1,T2 and leaving the unique large T3 direction inactive.",
        },
        "what_this_closes": {
            "S3_is_unique_volume_distinguished_twisted_D7_candidate": conditional_s3_selector,
            "S1_S2_not_separated_by_executed_volume_data": degenerate_max,
            "unconditional_MTT_selection_of_S3": False,
        },
        "still_open": {
            "prove_MTT_volume_or_anisotropy_rule_for_twisted_stack": True,
            "geometric_Deligne_Cech_or_worldvolume_flux_source_for_S3": True,
            "selected_visible_operator_source": True,
            "projector_retention_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions_and_SM_closure": True,
        },
        "guardrails": {
            "claims_S3_selected_unconditionally": False,
            "claims_complete_Freed_Witten_closed": False,
            "claims_visible_operator_source_constructed": False,
            "claims_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": "The executed Kahler data single out S3 as the only volume-anisotropic D7 stack in the twisted-CP rescue family. This makes S3 the strongest current candidate if the qutrit twist is required to attach to the unique small-volume/zeta3 divisor, but that selection rule is still an extra theorem to prove.",
            "next_closing_object": "Prove or reject the MTT rule that the projective qutrit twist attaches to the unique anisotropic S3 divisor; if proved, build the selected S3 Deligne/Cech/worldvolume-flux source packet.",
        },
    }


def main() -> int:
    data = build_certificate()
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0 if data["status"] != "VISIBLE_TWISTED_D7_VOLUME_SELECTOR_ATTEMPT_INCONCLUSIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
