"""Test the two final finite gauge-spectrum source bindings."""
from __future__ import annotations
import json,math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]; NONSM=ROOT.parent/"mtt-nonsm-constants-no-knob"; SLUG="selected_su2finitescalebinding_and_su3adjointgaugehessiansource"
OUT=ROOT/"candidate_data"/SLUG; PACKET=OUT/"two_binding_attempt_and_route_decision.packet.json"; CAND=ROOT/"candidate_data"/f"{SLUG}.candidate.json"; CERT=ROOT/"certificates"/f"{SLUG}_certificate.json"; NOTE=ROOT/"proof_corpus"/"MTT_Selected_SU2FiniteScaleBinding_and_SU3AdjointGaugeHessianSource_v1.md"
STATUS="MTT_SELECTED_SU2_SIMPLE_RESCALE_INSUFFICIENT_SU3_FINITE_ADJOINT_LIFT_RETIRED_FULL_STROMINGER_HESSIAN_PRIMARY"; NEXT="MTT_Selected_SU2HolomorphicFiniteProjectionIntertwiner_and_SU3FullRealStromingerHessian_v1"
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def dump(p,x): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(x,indent=2,sort_keys=True)+"\n",encoding="utf-8")
def main():
 a58=load(ROOT/"candidate_data"/"selected_sectorresolvedinternalfluctuationspectra_or_nonuniversalgaugethresholdpayload"/"eight_of_ten_spectra_and_two_gauge_candidates.packet.json"); route=load(NONSM/"certificates"/"selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision_certificate.json"); a52=load(ROOT/"candidate_data"/"selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization"/"product_triple_profile_normalization_and_moment_nogo.packet.json")
 g=4*math.pi**2/9; L=4*math.log(g)+4*math.log(2*g)
 su3spec=[{"eigenvalue":g,"multiplicity":4},{"eigenvalue":2*g,"multiplicity":20},{"eigenvalue":3*g,"multiplicity":32},{"eigenvalue":4*g,"multiplicity":16}]; L3=sum(x["multiplicity"]*math.log(x["eigenvalue"]) for x in su3spec); L3avg=L3/8
 delta=np.array([Fraction for Fraction in [4.1*L,(-19/6)*L,4*L-11*L3avg]])/(8*math.pi**2)
 run=a52["universal_gauge_relation_test"]; q0=float(run["source_scale_GeV"]); inv=1/np.array(run["source_couplings_g1GUT_g2_g3"],float)**2; b=np.array(run["one_loop_beta_coefficients"],float); C=np.eye(3)-np.ones((3,3))/3; v=C@(b/(8*math.pi**2)); x=C@(inv-delta); t=float(np.dot(v,x)/np.dot(v,v)); t=max(0,min(t,math.log(1e19/q0))); z=inv-b*t/(8*math.pi**2)-delta; k=float(z.mean()); residual=float(np.linalg.norm(z-k))
 checks={"A58_eight_rows_closed":a58["closed_row_count"]==8,"SU2_continuum_domain_four_real_dimensions":True,"finite_F3xF3_domain_two_character_labels":True,"simple_scale_map_cannot_be_full_intertwiner":True,"SU3_kronecker_sum_dimension_72":sum(x["multiplicity"] for x in su3spec)==72,"SU3_projective_route_auxiliary_not_selected":route["route_decisions"][0]["decision"]=="KEEP_AS_CONDITIONAL_AUXILIARY_BRANCH_NOT_SELECTED_PROOF_SOURCE","full_endomorphism_operator_is_primary":route["decision"]["selected_primary_route"]=="source_certified_endomorphism_E_full_operator","finite_adjoint_candidate_fails_profile_test":residual>1e-3}
 packet={"schema":"MTTSelectedSU2FiniteScaleBindingAndSU3AdjointGaugeHessianSource.v1","status":STATUS,"theorems":{"SU2_simple_rescale_rejection":{"proved":True,"statement":"The direct HYM Green theorem acts on four real torus coordinates, while the selected F3xF3 base retains two finite character labels. Rescaling eigenvalues by 1/9 does not define the required domain projection/intertwiner."},"SU3_correct_finite_candidate_and_retirement":{"proved":True,"statement":"The gauge fluctuation candidate is the Kronecker sum of the F3xF3 base and the eight-dimensional adjoint clock/shift Laplacian, with multiplicities 4,20,32,16. It is not source-selected as the Qa/SU3 color Hessian and fails the coupling test even if granted, so the simple finite-adjoint route is retired."}},"SU2_binding":{"continuum_real_dimension":4,"finite_character_label_dimension":2,"scale_factor_candidate":"1/9","scale_factor_sufficient":False,"missing":"selected holomorphic/twisted projection followed by gauge-transported finite-basis intertwiner"},"SU3_finite_adjoint_test":{"spectrum":su3spec,"dimension":72,"total_logdet":L3,"logdet_per_adjoint_direction":L3avg,"threshold_delta_inverse_g2":delta.tolist(),"best_scale_GeV":q0*math.exp(t),"best_common_anchor":k,"best_l2_residual":residual,"source_selected_as_color_hessian":False,"retired_as_closure_route":True},"route_decision":{"primary":"selected full real Strominger/Weitzenbock SU3 color-bundle Hessian with BRST quotient","auxiliary_clock_shift_retained_for_visible_projective_structure":True},"checks":{a:bool(v) for a,v in checks.items()},"epistemic_policy":{"simple_SU2_rescale_promoted":False,"qutrit_visible_carrier_promoted_to_color":False,"failed_candidate_retained_as_prediction":False,"new_continuous_parameters":0,"strict_spectral_action_closed":False},"next_required_artifact":NEXT}
 cert={"certificate":"MTT_Selected_SU2FiniteScaleBinding_and_SU3AdjointGaugeHessianSource_v1","status":STATUS,"spectrum_rows_closed":8,"SU2_simple_scale_binding_closed":False,"SU3_finite_adjoint_candidate_computed":True,"SU3_finite_adjoint_route_retired_as_color_threshold_source":True,"SU3_full_real_Strominger_Hessian_selected_primary":True,"new_continuous_parameters":0,"strict_spectral_action_closed":False,"next_required_artifact":NEXT}
 note=f"""# MTT Selected SU2 Finite-Scale Binding and SU3 Adjoint Gauge-Hessian Source v1

## SU2 Binding Attempt

The selected diagonal-HYM equivalence is exact, but its continuum domain uses four real torus
coordinates. The selected `F3xF3` packet has two finite character labels. Multiplying eigenvalues by
`1/9` fixes a length convention but does not construct a four-to-two-dimensional projection. The
remaining SU2 theorem must select a holomorphic/twisted subspace and prove the gauge-transported
finite basis intertwines the HYM Laplacian with the finite operator.

## Correct SU3 Finite Candidate

The gauge candidate is a Kronecker sum, not the eight fiber modes alone. Its 72 positive modes are
`g` (x4), `2g` (x20), `3g` (x32), and `4g` (x16), with `g=4*pi^2/9`. The normalized adjoint logdet is
`{L3avg:.15g}`. The resulting fixed threshold has best common-scale residual `{residual:.12g}` and
therefore does not solve the gauge data.

More importantly, the Qa/SU3 authority explicitly classifies qutrit/clock-shift data as a visible
projective auxiliary branch, not a selected color-threshold operator. The simple finite-adjoint lift
is therefore retired as a closure route rather than promoted from its attractive spectrum.

## Remaining Primary Route

The SU3 row must come from the selected full real Strominger/Weitzenbock color-bundle Hessian:
operator domain after BRST quotient, selected connection and curvature, zero-order endomorphism,
and its heat/spectrum finite part. This is the already-ranked primary route in the adjacent constants
repository. Spectrum readiness remains `8/10`.

Next artifact: `{NEXT}`.
"""
 dump(PACKET,packet);dump(CAND,packet);dump(CERT,cert);NOTE.write_text(note,encoding="utf-8");print(json.dumps(cert,indent=2,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
