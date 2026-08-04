"""Compute the E6 central-generator QCD anomaly and isolate U6 anomaly matching."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
SLUG = "selected_e6centralgeneratorqcdanomalyaudit"
OUT_DIR = ROOT / "candidate_data" / SLUG
OUT_CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
OUT_PACKET = OUT_DIR / "e6_qpsi_qcd_anomaly.packet.json"
OUT_CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "MTT_Selected_E6CentralGeneratorQCDAnomalyAudit_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    dictionary = load(Q79 / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json")
    slots = load(ROOT / "certificates" / "selected_smslotfunctor_overlapkernel_source_emission_certificate.json")
    prior = load(
        ROOT
        / "candidate_data"
        / "selected_neutrinoandstrongcp_strictupgradeattack"
        / "strong_cp_central_charge_anomaly_cutset.packet.json"
    )

    families = 3
    matter_rows = [
        {"field": "Q_L", "colored_multiplicity": 2, "two_T_fund": 1, "Q_psi": 1},
        {"field": "u^c", "colored_multiplicity": 1, "two_T_fund": 1, "Q_psi": 1},
        {"field": "d^c", "colored_multiplicity": 1, "two_T_fund": 1, "Q_psi": 1},
    ]
    exotic_rows = [
        {"field": "D in 5_H", "colored_multiplicity": 1, "two_T_fund": 1, "Q_psi": -2},
        {"field": "D^c in bar5_H", "colored_multiplicity": 1, "two_T_fund": 1, "Q_psi": -2},
    ]

    def anomaly(rows: list[dict]) -> int:
        return sum(
            row["colored_multiplicity"] * row["two_T_fund"] * row["Q_psi"]
            for row in rows
        )

    matter_per_family = anomaly(matter_rows)
    exotic_per_27 = anomaly(exotic_rows)
    matter_total = families * matter_per_family
    exotic_total = families * exotic_per_27
    complete_27_total = matter_total + exotic_total
    singlet_breaking_charge = 4
    naive_reduced_domain_wall = abs(matter_total) // math.gcd(
        abs(matter_total), singlet_breaking_charge
    )

    packet = {
        "schema": "MTTSelectedE6CentralGeneratorQCDAnomalyAudit.v1",
        "status": "E6_QPSI_ANOMALY_COMPUTED_SELECTED_THRESHOLD_MATCHING_OPEN",
        "inputs": {
            "E6_branching": dictionary["representation_dictionary"]["e6_branching"],
            "selected_all_six_SM_slot_arrows": slots["selected_SMSlotFunctor_all_six_arrows_claimed"],
            "conditional_PQ_theorem": prior["closed"]["conditional_PQ_relaxation_theorem"],
        },
        "primitive_E6_central_generator": {
            "name": "Q_psi",
            "branching_charges": {"16_M": 1, "10_H_or_exotic": -2, "1_S": 4},
            "Yukawa_neutrality": "1+1-2=0",
            "generator_is_selected_as_surviving_global_PQ": False,
        },
        "colored_anomaly_trace": {
            "formula": "A_3=sum_colored multiplicity*2T(R)*Q_psi",
            "matter_rows": matter_rows,
            "matter_anomaly_per_family": matter_per_family,
            "matter_family_count": families,
            "matter_anomaly_total": matter_total,
            "exotic_rows_per_27": exotic_rows,
            "exotic_anomaly_per_27": exotic_per_27,
            "exotic_anomaly_total_for_three_27s": exotic_total,
            "complete_three_27_anomaly": complete_27_total,
        },
        "domain_wall_diagnostic": {
            "singlet_breaking_charge": singlet_breaking_charge,
            "matter_only_anomaly": matter_total,
            "naive_N_DW_after_singlet_identification": naive_reduced_domain_wall,
            "N_DW_1_obtained": naive_reduced_domain_wall == 1,
            "is_selected_prediction": False,
            "reason": "The result applies only if flux/threshold data remove the exotic cancellation from the low-energy axion current while retaining the Q_psi phase with singlet charge 4.",
        },
        "theorem": {
            "name": "E6CentralGeneratorAnomalyCancellationAndThresholdDependenceTheorem",
            "proved": True,
            "statement": "The primitive E6 Q_psi generator has colored anomaly 12 on three light 16_1 matter families and -12 on the colored partners of three 10_-2 multiplets, so complete 27 matter is QCD-anomaly free. A nonzero low-energy PQ anomaly is therefore not fixed by representation branching alone; it requires a selected flux/threshold anomaly-matching map. Under the matter-only plus 1_4-breaking diagnostic, the reduced domain-wall number is 3, not 1.",
        },
        "U6_previous_open_items": list(prior["open"].keys()),
        "U6_reduced_missing_object": "SelectedFluxThresholdAxionCurrentAnomalyMatchingMap",
        "U6_selected_QCD_anomaly_closed": False,
        "U6_strong_CP_closed": False,
        "observed_data_used_as_selector": False,
        "next_required_artifact": "MTT_Selected_FluxThresholdAxionCurrentAnomalyMatchingMap_v1",
    }

    cert = {
        "certificate": "MTT_Selected_E6CentralGeneratorQCDAnomalyAudit_v1",
        "status": packet["status"],
        "matter_anomaly_per_family": matter_per_family,
        "matter_anomaly_three_families": matter_total,
        "exotic_anomaly_three_27s": exotic_total,
        "complete_three_27_anomaly": complete_27_total,
        "naive_matter_only_singlet_reduced_N_DW": naive_reduced_domain_wall,
        "N_DW_1_obtained": naive_reduced_domain_wall == 1,
        "representation_only_nonzero_PQ_anomaly_proved": False,
        "U6_reduced_missing_object_count": 1,
        "U6_strong_CP_closed": False,
        "next_required_artifact": packet["next_required_artifact"],
    }

    note = f"""# MTT Selected E6 Central-Generator QCD Anomaly Audit v1

## Exact finite trace

The selected matter-slot chain is compatible with the primitive E6 branching

```text
27 -> 16_1 + 10_-2 + 1_4.
```

For `Q_psi`, the colored anomaly per `16_1` family is

```text
Q_L: 2
u^c: 1
d^c: 1
total per family: {matter_per_family}
three families: {matter_total}
```

The colored `5+bar5` partners in each `10_-2` contribute
`{exotic_per_27}`, hence three complete `27`s give
`{matter_total}+({exotic_total})={complete_27_total}`.

## Consequence

E6 branching alone does not provide an anomalous PQ current. A selected
flux/threshold map must show which colored modes decouple from the axion
current and how anomaly matching is retained. If one provisionally keeps only
the three matter `16_1`s and breaks with `1_4`, the reduced diagnostic is

```text
N_DW = 12/gcd(12,4) = {naive_reduced_domain_wall},
```

not one. This is not promoted as a prediction.

The five former U6 questions therefore contract to one source object:
`MTT_Selected_FluxThresholdAxionCurrentAnomalyMatchingMap_v1`.
"""

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PACKET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    OUT_CANDIDATE.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
