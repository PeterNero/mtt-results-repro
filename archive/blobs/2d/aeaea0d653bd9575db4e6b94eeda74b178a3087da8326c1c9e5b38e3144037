"""Audit the primitive C1 right-label source-promotion theorem attempt."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
SMP = TEXPAPERS / "mtt-sm-parity-closure"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def local(name: str) -> str:
    return read(ROOT / name)


def main() -> None:
    theorem = local("Primitive_C1_Right_Label_Source_Promotion_Theorem_Attempt_v1.md")
    adapter_contract = local("Primitive_C1_to_Right_Label_Adapter_Payload_Contract_v1.md")
    adapter_note = local("Cross_Repo_Primitive_Row_Adapter_for_Right_Channel_Labels_v1.md")
    row_contract = local("Right_Channel_Label_Row_Emission_Contract_v1.md")
    rowsource_validator = read(
        SMP
        / "candidate_data"
        / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
        / "row_source_validator_result.packet.json"
    )
    routec_overlap = read(
        SMP
        / "candidate_data"
        / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet.candidate.json"
    )
    routec_operator = read(
        SMP
        / "candidate_data"
        / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"
    )

    gates = [
        Gate("theorem attempt saved", "PASS" if "PrimitiveC1RightLabelSourcePromotionTheorem" in theorem else "FAIL", "target theorem named"),
        Gate("conditional theorem proved", "PASS" if "CONDITIONAL_PROMOTION_PROVED" in theorem and "ConditionalPrimitiveC1RightLabelPromotionTheorem" in theorem else "FAIL", "conditional implication recorded"),
        Gate("unconditional guarded", "PASS" if "UNCONDITIONAL_PROMOTION_OPEN" in theorem and "source_owner_verified=false" in theorem else "FAIL", "no overpromotion"),
        Gate("adapter contract linked", "PASS" if "MTTPrimitiveC1ToRightLabelAdapter.v1" in adapter_contract else "FAIL", "payload contract exists"),
        Gate("row contract linked", "PASS" if "MTTFlavorRightChannelLabelRowEmission.v1" in row_contract else "FAIL", "right-label row contract exists"),
        Gate("adapter clue linked", "PASS" if "strong construction clue" in adapter_note else "FAIL", "diagnostic adapter status imported"),
        Gate("row-source rejection imported", "PASS" if "source_independent_of_residual_projector_replay is not true" in rowsource_validator else "FAIL", "sibling validator rejects current source"),
        Gate("route C exits imported", "PASS" if "prove_same_source_matter_slot_charge_theorem" in routec_overlap and "selected_transfer_normalization" in routec_operator else "FAIL", "Route C source exits identified"),
        Gate("source cutset", "OPEN", "prove SelectedPrimitiveKernelSourceTheorem or Route C overlap/normalization theorem"),
    ]

    print("Primitive C1 right-label source-promotion theorem attempt check")
    print("================================================================")
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
