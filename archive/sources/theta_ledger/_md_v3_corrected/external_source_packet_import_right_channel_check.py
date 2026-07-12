"""Check external source-packet imports for right-channel label assignment."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
CONST = TEXPAPERS / "mtt-individual-constants-source-search"
SMP = TEXPAPERS / "mtt-sm-parity-closure"
QASU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    note = read(ROOT / "External_Source_Packet_Import_for_Right_Channel_Label_Assignment_v1.md")
    contract = read(ROOT / "Right_Channel_Label_Row_Emission_Contract_v1.md")
    h7b1w = read(CONST / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1W_FiniteTraceHYMBindingOrDirectHuvPayload_v1.md")
    h7b1o = read(CONST / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1O_DiagonalHYMPayloadToHuvTransferGate_v1.md")
    h7b1u = read(CONST / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1U_SourceBoundMetricAndFiniteReduction_v1.md")
    primitive_rows = read(SMP / "candidate_data" / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "primitive_rows_execution_ready.packet.json")
    basis_fill = read(SMP / "candidate_data" / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_b_selected_basis_value_fill.packet.json")
    qasu3_twist = read(QASU3 / "certificates" / "twisted_source_promotion_packet_fill_attempt_certificate.json")

    gates = [
        Gate("import note saved", "PASS" if "External Source-Packet Import" in note else "FAIL", "external import note present"),
        Gate("row contract saved", "PASS" if "MTTFlavorRightChannelLabelRowEmission.v1" in contract else "FAIL", "row-emission contract present"),
        Gate("H7B1W imported", "PASS" if "finite trace/HYM binding closed             False" in h7b1w else "FAIL", "Higgs finite-trace contract remains open"),
        Gate("H7B1O imported", "PASS" if "selected diagonal HYM first solve closed       True" in h7b1o else "FAIL", "diagonal HYM support imported"),
        Gate("H7B1U imported", "PASS" if "conditional finite reduction executable         True" in h7b1u else "FAIL", "finite reduction executable but unpromoted"),
        Gate("primitive rows readiness", "PASS" if '"can_execute_rows_now": false' in primitive_rows and '"primitive_row_count": 72' in primitive_rows else "FAIL", "SM-parity primitive rows ready-not-executed"),
        Gate("basis rows selected", "PASS" if '"all_basis_rows_selected": true' in basis_fill and '"observed_data_used": false' in basis_fill else "FAIL", "selected basis support imported"),
        Gate("Qa/SU3 source context", "PASS" if '"source_family_selected": true' in qasu3_twist and '"selected_D_E_dotD_response_supplied": false' in qasu3_twist else "FAIL", "Qa/SU3 source context partial but response open"),
        Gate("flavor row payload", "OPEN", "emit A_u^spin,A_d^dyad,A_d^nil from same source"),
    ]

    print("External source-packet import right-channel check")
    print("=================================================")
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
