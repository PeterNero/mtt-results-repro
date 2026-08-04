from __future__ import annotations

import cmath
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_literalcechwitness_or_globalhymconnectioncoefficients"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def phase(a: tuple[int, int], b: tuple[int, int]) -> complex:
    numerator = (-b[0] * a[1]) % 3
    return cmath.exp(2j * cmath.pi * numerator / 3)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    cech = load(f"candidate_data/{SLUG}/literal_selected_s3_deligne_cech_witness.packet.json")
    hym = load(f"candidate_data/{SLUG}/remaining_global_hym_connection_cutset.packet.json")
    cert = load(f"certificates/{SLUG}_certificate.json")

    require(len(cech["entries"]) == 81, "Cech table size")
    for row in cech["entries"]:
        a = tuple(row["left"])
        b = tuple(row["right"])
        require(row["numerator_mod_3"] == (-b[0] * a[1]) % 3, "Cech table formula")
    group = [(a, b) for a in range(3) for b in range(3)]
    for x in group:
        for y in group:
            for z in group:
                xy = ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)
                yz = ((y[0] + z[0]) % 3, (y[1] + z[1]) % 3)
                residual = phase(x, y) * phase(xy, z) - phase(y, z) * phase(x, yz)
                require(abs(residual) < 1e-12, "U(1) cocycle law")
    require(all(cech["checks"].values()), "selected Cech checks")
    require(hym["closed"]["abstract_HYM_existence"] is True, "HYM existence")
    require(all(hym["open"].values()), "global HYM cutset changed")
    require(cert["literal_Cech_witness_closed"] is True, "Cech closure")
    require(cert["literal_global_HYM_witness_closed"] is False, "HYM overclaim")

    print(json.dumps({
        "literal_Cech_entries": 81,
        "U1_cocycle_triples_checked": 729,
        "literal_Cech_witness_closed": True,
        "abstract_HYM_existence_closed": True,
        "literal_global_HYM_witness_closed": False,
        "U2_literal_witness_families": "1/2",
    }, indent=2))
    print("selected literal Cech witness audit passed")


if __name__ == "__main__":
    main()
