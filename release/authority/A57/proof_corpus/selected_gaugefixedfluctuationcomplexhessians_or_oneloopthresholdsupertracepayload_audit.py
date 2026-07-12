from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SLUG="selected_gaugefixedfluctuationcomplexhessians_or_oneloopthresholdsupertracepayload"
STATUS="MTT_SELECTED_GAUGE_FIXED_FLUCTUATION_COMPLEX_AND_BETA_SUPERTRACE_CLOSED_COMMON_INTERNAL_SPECTRUM_IS_SCALE_SHIFT_SECTOR_SPECTRA_OPEN"
NEXT="MTT_Selected_SectorResolvedInternalFluctuationSpectra_or_NonUniversalGaugeThresholdPayload_v1"
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def req(x,m):
    if not x: raise AssertionError(m)
def main():
    subprocess.run([sys.executable,str(ROOT/"scripts"/f"build_{SLUG}.py")],cwd=ROOT,check=True)
    p=load(ROOT/"candidate_data"/SLUG/"gauge_fixed_complex_and_signed_heat_rows.packet.json"); c=load(ROOT/"certificates"/f"{SLUG}_certificate.json"); t=load(ROOT/"candidate_data"/SLUG/"sector_resolved_internal_fluctuation_spectra.template.json")
    n=(ROOT/"proof_corpus"/"MTT_Selected_GaugeFixedFluctuationComplexHessians_or_OneLoopThresholdSupertracePayload_v1.md").read_text(encoding="utf-8")
    req(p["status"]==c["status"]==STATUS,"status"); req(p["next_required_artifact"]==c["next_required_artifact"]==NEXT,"next"); req(all(p["checks"].values()),"checks")
    req(c["derived_beta_vector"]==["41/10","-19/6","-7"],"beta"); req(c["common_internal_spectrum_is_only_scale_shift"],"scale shift"); req(not c["sector_resolved_internal_spectra_closed"],"overclaim")
    req(all(not x["accepted"] for x in t["blocks"].values()),"empty spectrum accepted")
    for s in ["41/10", "FP ghosts", "scale translation", "ten exact spectrum blocks", NEXT]: req(s.lower() in n.lower(),s)
    print(json.dumps(c,indent=2,sort_keys=True)); print("gauge-fixed fluctuation complex audit passed"); return 0
if __name__=="__main__": raise SystemExit(main())
