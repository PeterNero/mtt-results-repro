from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A123 = (
    ROOT
    / "candidate_data"
    / "selected_q79projectivelinechartcovarianceandellzerocontinuation"
    / "projective_line_chart_covariance_theorem.packet.json"
)
A400 = VALIDATED / "n3.relative_chain_identity.a400.json"
A403 = VALIDATED / "n3.common_junction_edge_ledger.a403.json"
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
FLOATING_ENGINE_SOURCE = ROOT / "scripts" / "q79genus2_period_transport.py"
AUGMENTED_ENGINE_SOURCE = ROOT / "scripts" / "run_q79_augmented_beta_transport.py"
OUTPUT = VALIDATED / "n3.junction_reverse_composition.a409t.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourJunctionReverseComposition_A409T_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def main() -> int:
    chart = load(A123)
    identity = load(A400)
    junction = load(A403)
    sweep = load(A404)
    if not chart["theorem"]["proved"]:
        raise AssertionError("A409T requires A123 chart covariance")
    if not identity["theorem"]["proved"]:
        raise AssertionError("A409T requires A400 relative-chain identity")
    if not junction["theorem"]["proved"] or not junction["strict_scope"]["aggregate_common_trunk_cancellation_proved"]:
        raise AssertionError("A409T requires A403 zero-trunk theorem")
    if not sweep["theorem"]["proved"] or not sweep["strict_scope"]["finite_operator_sweep_geometry_selected"]:
        raise AssertionError("A409T requires A404 finite operator geometry")

    payload = {
        "schema": "MTTQ79HeightFourJunctionReverseCompositionTheorem.v1",
        "status": "EXACT_AFFINE_REVERSE_OPERATOR_AND_ZERO_TRUNK_COMPOSITION_PROVED",
        "artifact": "A409T",
        "theorem": {
            "name": "SelectedJunctionReverseCompositionAndZeroTrunkTheorem",
            "proved": True,
            "augmented_coordinate": "q",
            "augmented_forward_block_operator": "T_e^(q)=[[U_e,0],[V_e,I_8]]",
            "augmented_reverse_block_operator": "(T_e^(q))^{-1}=[[U_e^{-1},0],[-V_e U_e^{-1},I_8]]",
            "selected_physical_residue_sign_bridge": "r_phys=-q",
            "forward_block_operator": "T_e^(r)=[[U_e,0],[-V_e,I_8]]",
            "reverse_block_operator": "(T_e^(r))^{-1}=[[U_e^{-1},0],[+V_e U_e^{-1},I_8]]",
            "outer_leg_to_hub_rule": (
                "(p_e,r_e) maps to "
                "(U_e^{-1}p_e,r_e+V_e U_e^{-1}p_e)"
            ),
            "integer_sum_rule": (
                "p_hub=sum_i m_i U_i^{-1}p_i plus the selected handle term; "
                "r_hub=sum_i m_i(r_i+V_i U_i^{-1}p_i) plus the handle residue"
            ),
            "zero_trunk_rule": (
                "if the exact A403 boundary relation gives p_hub=0, every shared "
                "onward physical-residue trunk contributes -V_trunk p_hub=0 exactly"
            ),
            "proof": [
                "The augmented homogeneous ODE has block generator [[C,0],[K,0]].",
                "Its q-coordinate fundamental transport therefore has triangular form [[U,0],[V,I_8]].",
                "The selected floating engine defines the main physical thimble residue as minus the terminal augmented state, hence r_phys=-q.",
                "Conjugating by diag(I_5,-I_8) gives [[U,0],[-V,I_8]] in physical-residue coordinates.",
                "Direct block multiplication gives the displayed physical inverse whenever U is invertible.",
                "Linearity commutes with the fixed integral chain coefficients.",
                "A403 transports the exact A130 boundary relation to the common hub, so the summed period vector is exactly zero.",
                "Multiplying the zero summed period by the signed physical trunk residue operator gives zero before interval addition.",
            ],
        },
        "execution_contract": {
            "A405_requirement": "each interval U_e must be certified invertible",
            "outer_leg_requirement": "each outer state must terminate at its exact A404 entry",
            "chart_requirement": (
                "native-z outer states must be transformed by the exact A123 five-period "
                "transition into the common y frame before applying U_e^{-1}"
            ),
            "frame_requirement": (
                "apply the reverse block map to each retained affine error frame; do not "
                "subtract independently rounded endpoint boxes and call that correlated"
            ),
            "residue_coordinate_requirement": (
                "A405 stores the augmented q-coordinate operator V, while selected "
                "thimble residues use r_phys=-q; apply the conjugated physical blocks"
            ),
            "handle_requirement": "include the selected A-handle entry in the same hub sum",
        },
        "inventory": {
            "selected_thimble_entries": int(sweep["summary"]["selected_thimble_entry_count"]),
            "selected_handle_entries": int(sweep["summary"]["selected_handle_entry_count"]),
            "common_period_dimension": 5,
            "integrated_residue_dimension": 8,
            "native_y_target_count": 36,
            "native_z_target_count": 40,
        },
        "authority": {
            "A123_projective_chart_covariance": authority(A123),
            "A400_relative_chain_identity": authority(A400),
            "A403_zero_trunk_theorem": authority(A403),
            "A404_finite_operator_geometry": authority(A404),
            "floating_transport_sign_definition": authority(FLOATING_ENGINE_SOURCE),
            "augmented_transport_equations": authority(AUGMENTED_ENGINE_SOURCE),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "reverse_affine_operator_formula_proved": True,
            "selected_physical_residue_sign_bridge_proved": True,
            "integer_sum_commutes_with_reverse_transport_proved": True,
            "zero_common_trunk_elimination_rule_proved": True,
            "A123_chart_transition_required_for_native_z_targets": True,
            "A405_numeric_operator_sweeps_consumed": False,
            "outer_thimble_states_consumed": False,
            "common_hub_sum_executed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "audit A405 U_e invertibility, execute the 76 outer states, apply the "
            "A409T reverse maps to retained frames, and evaluate the common hub sum"
        ),
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(
        "# MTT q79 Height-Four Junction Reverse Composition (A409T) v1\n\n"
        "For the augmented homogeneous system, an entry transport has triangular "
        "form `T_e^(q)=[[U_e,0],[V_e,I_8]]`. The selected floating engine defines "
        "the physical residue by `r_phys=-q`. Conjugation therefore gives "
        "`T_e^(r)=[[U_e,0],[-V_e,I_8]]`, whose exact reverse sends an outer entry "
        "state `(p_e,r_e)` to `(U_e^{-1}p_e,r_e+V_eU_e^{-1}p_e)`.\n\n"
        "After applying this rule in one common chart and affine frame, the fixed "
        "integer coefficients commute with transport. A403 then removes the shared "
        "trunk exactly because its input period sum is the zero vector. Numerical "
        "operator invertibility, outer-leg execution, and the hub sum remain execution gates.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
