"""Check the primitive C1 to right-label adapter payload contract."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(name: str) -> str:
    path = ROOT / name
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    contract = read("Primitive_C1_to_Right_Label_Adapter_Payload_Contract_v1.md")
    adapter_note = read("Cross_Repo_Primitive_Row_Adapter_for_Right_Channel_Labels_v1.md")
    row_contract = read("Right_Channel_Label_Row_Emission_Contract_v1.md")
    theorem_attempt = read("Primitive_C1_Right_Label_Source_Promotion_Theorem_Attempt_v1.md")

    gates = [
        Gate("contract saved", "PASS" if "MTTPrimitiveC1ToRightLabelAdapter.v1" in contract else "FAIL", "adapter schema named"),
        Gate("trace table present", "PASS" if "Tr(P_u1 S_u^spin) = -1" in contract and "Tr(P_d2 S_d^nil)  = +1" in contract else "FAIL", "right-label trace targets included"),
        Gate("adapter numerics present", "PASS" if "scale=+3.31494423885" in contract and "scale=-7.38590275834" in contract else "FAIL", "finite affine normalizations recorded"),
        Gate("support-only guard", "PASS" if "residual_replay_dependency=true" in contract and "not proof" in contract else "FAIL", "no promotion overclaim"),
        Gate("row contract compatibility", "PASS" if "MTTFlavorRightChannelLabelRowEmission.v1" in row_contract else "FAIL", "compatible with right-channel row-emission contract"),
        Gate("adapter note compatibility", "PASS" if "strong construction clue" in adapter_note else "FAIL", "cross-repo adapter status imported"),
        Gate("conditional promotion", "PASS" if "CONDITIONAL_PROMOTION_PROVED" in theorem_attempt else "FAIL", "conditional source-promotion implication proved"),
        Gate("unconditional source", "OPEN", "emit source-owner primitive rows with residual_replay_dependency=false"),
    ]

    print("Primitive C1 to right-label adapter contract check")
    print("==================================================")
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
