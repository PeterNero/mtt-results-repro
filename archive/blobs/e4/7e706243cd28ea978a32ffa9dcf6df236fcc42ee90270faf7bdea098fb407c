"""Audit the durable q79 u1=2, u2=28 execution result."""

from pathlib import Path

from q79_Ronly_u1_002_u2_021_execution_audit import main as audit_execution


ROOT = Path(__file__).resolve().parents[1]
RESULT = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_u2_028_job"
    / "q79_Ronly_u1_002_u2_028.result.packet.json"
)


if __name__ == "__main__":
    audit_execution(result_path=RESULT, expected_u2=28)
