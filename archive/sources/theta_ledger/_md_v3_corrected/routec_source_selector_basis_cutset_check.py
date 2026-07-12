"""Verify the imported Route-C source-selector/basis cutset status."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
IMPORT_PACKET = ROOT / "selected_routec_source_selector_basis_cutset.import.json"
SOURCE_CANDIDATE = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure"
    r"\candidate_data\selected_routec_source_selector_and_basis_theorem.candidate.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    packet = load(IMPORT_PACKET)
    source = load(SOURCE_CANDIDATE)
    errors: list[str] = []

    calc = source["calculation"]
    diff = calc["root_vs_formal_payload_diff"]
    basis_open = calc["basis_protocol_values_open"]

    require(packet["closure_claimed"] is False, "import must not claim closure", errors)
    require(packet["target_fitting_used"] is False, "target fitting must be false", errors)
    require(source["target_fitting_used"] is False, "source target fitting must be false", errors)
    require(source["closure_claimed"] is False, "source must not claim closure", errors)
    require(source["theorem"]["proved"] is True, "cutset theorem must be proved", errors)
    require(diff["total_difference_count"] == 36, "expected 36 root/formal differences", errors)
    require(
        diff["changed_terminal_keys"]
        == ["alpha1_driver_verified", "selected_dotD_source_verified", "selected_source_verified"],
        "changed terminal keys must be exactly selected-source flags",
        errors,
    )
    require(
        diff["all_differences_are_allowed_flags"] is True,
        "root/formal differences must be allowed flags only",
        errors,
    )
    require(
        calc["formal_lift_lower_validators_all_pass"] is True,
        "formal lift lower validators must pass",
        errors,
    )
    require(
        calc["formal_lift_de_response_promotion_passes"] is True,
        "formal lift de_response promotion must pass",
        errors,
    )
    require(
        all(item["exit_code"] == 1 for item in calc["honest_root_failures"].values()),
        "honest-root failures should remain selector/provenance failures",
        errors,
    )
    require(all(value is True for value in basis_open.values()), "all basis protocol values should remain open", errors)
    require(
        source["what_remains_open"]["selected_source_provenance_theorem"] is True,
        "selected source provenance theorem must remain open",
        errors,
    )
    require(
        source["what_remains_open"]["quotient_valid_BN_basis_certificate"] is True,
        "quotient-valid B_N basis certificate must remain open",
        errors,
    )

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1

    print("Route-C source selector/basis cutset import PASS")
    print(f"status {packet['status']}")
    print(f"differences {diff['total_difference_count']}")
    print(f"next {packet['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
