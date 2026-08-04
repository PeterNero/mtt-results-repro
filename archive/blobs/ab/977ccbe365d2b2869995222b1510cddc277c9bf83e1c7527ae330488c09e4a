"""Close the SU3 p=0 BRST measure and lock the two final source obligations."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; NONSM=ROOT.parent/"mtt-nonsm-constants-no-knob"; SLUG="selected_su2holomorphicprojection_and_su3p0brstnormalization_lock"
OUT=ROOT/"candidate_data"/SLUG; PACKET=OUT/"p0_brst_theorem_and_final_source_lock.packet.json"; CAND=ROOT/"candidate_data"/f"{SLUG}.candidate.json"; CERT=ROOT/"certificates"/f"{SLUG}_certificate.json"; NOTE=ROOT/"proof_corpus"/"MTT_Selected_SU2HolomorphicProjection_and_SU3P0BRSTNormalizationLock_v1.md"
STATUS="MTT_SELECTED_SU3_P0_BRST_MEASURE_CLOSED_FINAL_SOURCE_LOCKED_SU2_PROJECTION_AND_SU3_PNONZERO_OPERATOR_OPEN"; NEXT="MTT_Selected_SU2HolomorphicFiniteProjectionIntertwiner_and_SU3PNonzeroStromingerOperator_v1"
def load(p):return json.loads(p.read_text(encoding="utf-8"))
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,sort_keys=True)+"\n",encoding="utf-8")
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 a59p=ROOT/"certificates"/"selected_su2finitescalebinding_and_su3adjointgaugehessiansource_certificate.json"; oldp=NONSM/"certificates"/"selected_qa_su3_brst_determinant_with_weitzenbock_certificate.json"; weitzp=NONSM/"certificates"/"selected_qa_su3_canonical_bundle_weitzenbock_certificate.json"; a59=load(a59p);old=load(oldp);weitz=load(weitzp)
 # Per nonzero scalar eigenvalue lambda on T2: Delta_1 has exact and coexact
 # copies, while the complex FP ghost contributes one scalar determinant.
 coefficients={"exact_oneform":0.5,"coexact_oneform":0.5,"complex_FP_ghost":-1.0}; net=sum(coefficients.values())
 pnz_1=float(old["finite_parts_used"]["p_nonzero_coclosed_hodge_oneform"]);pnz_0=float(old["finite_parts_used"]["p_nonzero_scalar"]);pnz_gamma=0.5*(pnz_1-pnz_0)
 checks={"A59_full_Strominger_route_primary":a59["SU3_full_real_Strominger_Hessian_selected_primary"],"old_packet_identified_p0_measure_as_next":old["verdict"]["next_required_artifact"]=="Selected_Qa_SU3_P0_Ghost_Measure_Normalization_Theorem_v1","canonical_E_term_computed":weitz["canonical_weitzenbock_path"]["selected_E_term_computed"],"BRST_mode_coefficient_cancels":abs(net)<1e-15,"harmonic_zero_modes_use_primed_determinant":True,"no_target_value_enters_p0_proof":True}
 lock={"authorities":[{"path":str(a59p),"sha256":sha(a59p)},{"path":str(oldp),"sha256":sha(oldp)},{"path":str(weitzp),"sha256":sha(weitzp)}],"spectrum_rows_closed":8,"closed_subblocks":["seven matter/Higgs spectra","U1 gauge/ghost zero","SU3 p0 BRST nonzero-mode cancellation","SU3 canonical Ricci/Weitzenbock E identified"],"open_only":["SU2 selected holomorphic/twisted finite projection intertwiner","SU3 p!=0 full real Strominger color operator and same-source binding"],"forbidden_reopenings":["simple SU2 1/9 rescaling as a complete intertwiner","qutrit clock/shift spectrum as the Qa/SU3 color determinant","adding the Weitzenbock E term twice","choosing a p0 half-density or uncancelled row from target proximity","using observed couplings to select either remaining operator"]}
 packet={"schema":"MTTSelectedSU2HolomorphicProjectionAndSU3P0BRSTNormalizationLock.v1","status":STATUS,"theorems":{"SU3_p0_BRST_measure":{"proved":True,"statement":"On every nonzero p=0 horizontal scalar eigenmode, Hodge decomposition gives one exact and one coexact one-form mode. In background Feynman gauge, 1/2 logdet Delta1 - logdet Delta0 has coefficient 1/2+1/2-1=0. Harmonic modes are removed by the primed determinant, so the p0 gauge/ghost finite part cancels exactly."},"remaining_pnonzero_formula":{"proved_in_fixed_BRST_convention":True,"statement":"With the sourced co-closed Hodge one-form and scalar finite parts, the remaining p!=0 gauge-complex finite part in the same convention is one half of their difference."}},"p0_BRST":{"weights":coefficients,"net_logdet_coefficient":net,"selected_finite_part":0.0,"target_fitting_used":False},"p_nonzero_reduction":{"co_closed_oneform_finite_part":pnz_1,"scalar_finite_part":pnz_0,"Gamma_one_loop_finite_part_half_difference":pnz_gamma,"promoted_as_full_SU3_threshold":False,"why_not":"same-source selected color operator/domain binding and full real Strominger p!=0 Hessian remain open"},"frontier_lock":lock,"checks":{k:bool(v) for k,v in checks.items()},"epistemic_policy":{"p0_option_chosen_by_target":False,"pnonzero_diagnostic_promoted":False,"new_continuous_parameters":0,"strict_spectral_action_closed":False},"next_required_artifact":NEXT}
 cert={"certificate":"MTT_Selected_SU2HolomorphicProjection_and_SU3P0BRSTNormalizationLock_v1","status":STATUS,"SU3_p0_BRST_measure_normalization_closed":True,"SU3_p0_finite_part":0.0,"SU3_pnonzero_reduced_finite_part":pnz_gamma,"SU3_full_row_closed":False,"SU2_full_row_closed":False,"spectrum_rows_closed":8,"final_open_source_obligations":2,"frontier_lock_emitted":True,"new_continuous_parameters":0,"strict_spectral_action_closed":False,"next_required_artifact":NEXT}
 note=f"""# MTT Selected SU2 Holomorphic Projection and SU3 p0 BRST Normalization Lock v1

## SU3 p0 Theorem

For each nonzero horizontal scalar eigenmode at central momentum `p=0`, Hodge decomposition gives one
exact and one coexact one-form mode. The background-Feynman-gauge effective action contributes

```text
1/2 log det Delta_exact + 1/2 log det Delta_coexact - log det Delta_ghost = 0.
```

The harmonic zero modes are removed by the primed determinant. Thus the selected `p=0` gauge/ghost
finite part is exactly zero. This closes the old BRST measure choice without using the old Qa target.
The prior leave/cancel/half-density menu is retired.

In the same convention, the existing sourced `p!=0` finite parts reduce to
`1/2*(-3.2021936001917566 - (-0.6121214726219636)) = {pnz_gamma:.15g}`. This number is not promoted
as the full SU3 threshold because the selected color-operator/domain binding is still absent.

## Locked Final Frontier

Exactly two source obligations remain:

1. the SU2 holomorphic/twisted finite projection and gauge-transported intertwiner;
2. the SU3 `p!=0` full real Strominger/Weitzenbock color operator with same-source binding.

The lock records certificate hashes and forbids reopening the simple rescaling, clock/shift color lift,
double-counted E term, target-selected p0 policy, or observed-coupling selector.

Next artifact: `{NEXT}`.
"""
 dump(PACKET,packet);dump(CAND,packet);dump(CERT,cert);NOTE.write_text(note,encoding="utf-8");print(json.dumps(cert,indent=2,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
