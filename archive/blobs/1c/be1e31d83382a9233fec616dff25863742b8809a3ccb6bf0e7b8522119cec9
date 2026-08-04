from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "revision_update_ledger.json"
MARKDOWN = ROOT / "MTT_CORPUS_REVISION_UPDATE_LEDGER_2026-07-11.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    counts = data["counts"]
    papers = data["papers"]
    authority_ids = {item["id"] for item in data["authorities"]}

    require(data["schema"] == "MTTCorpusRevisionUpdateLedger.v1", "unexpected ledger schema")
    require(data["status"] == "CONSOLIDATED_FOR_NEXT_VERSION_EDITING_NOT_YET_APPLIED", "ledger overclaims applied revisions")
    require(counts["target_papers"] == 137, "target-paper count changed")
    require(counts["markdown_papers"] == 135, "Markdown-paper count changed")
    require(counts["zip_only_papers"] == 2, "ZIP-only source count changed")
    require(counts["theta_first_pass_papers"] == 10, "Theta first-pass paper count changed")
    require(counts["theta_first_pass_materially_changed"] == 5, "Theta material-repair count changed")
    require(counts["theta_first_pass_copied_unchanged"] == 5, "Theta unchanged-copy count changed")
    require(counts["external_report_paper_entries"] == 136, "external report entry count changed")
    require(counts["papers_covered_by_external_report"] == 135, "external report coverage changed")
    require(counts["papers_missing_from_external_report"] == 2, "external report omission count changed")
    require(counts["unmatched_report_entries"] == 0, "external report contains unmatched entries")
    require(len(papers) == counts["target_papers"], "paper inventory length mismatch")
    require(len(data["report_clause_decisions"]) >= 16, "report applicability matrix incomplete")
    require(len(data["high_impact_updates"]) >= 13, "high-impact replacement matrix incomplete")
    require(len(data["repository_decisions"]) == 8, "repository disposition table incomplete")
    require(len(data["authorities"]) == 44, "latest strict-upgrade authority set incomplete")

    paths = [item["path"] for item in papers]
    require(len(paths) == len(set(paths)), "duplicate paper source paths")
    for paper in papers:
        require(Path(paper["path"]).exists(), f"missing paper source: {paper['path']}")
        require(paper["source_kind"] in {"markdown", "markdown_corrected_intermediate", "zip_tex"}, f"invalid source kind: {paper['name']}")
        require(paper["line_count"] > 0, f"empty source: {paper['name']}")
        require(paper["revision_anchor_summary"], f"no exact update anchor: {paper['name']}")
        require(set(paper["authority_overlays"]) <= authority_ids, f"unknown authority overlay: {paper['name']}")

    for authority in data["authorities"]:
        require(Path(authority["path"]).exists(), f"missing authority: {authority['id']} {authority['path']}")

    omitted = [paper for paper in papers if not paper["external_report"]["covered"]]
    omitted_names = {paper["name"] for paper in omitted}
    require(
        omitted_names
        == {
            "The_Book_on_Modal_Triplet_Theory_v9.md",
            "Modal_Triplet_Theory__From_MTT_to_Standard_Model_v2.zip",
        },
        "unexpected external-report omission set",
    )

    sm = next(paper for paper in papers if paper["name"] == "Modal_Triplet_Theory__From_MTT_to_Standard_Model_v2.zip")
    require({"A01", "A02", "A04", "A05", "A06", "A08", "A10", "A21", "A22", "A23", "A24", "A25", "A26", "A27", "A28", "A29", "A30", "A31", "A32", "A33", "A34", "A35", "A36", "A37", "A38", "A39", "A40", "A41", "A42", "A43", "A44"} <= set(sm["authority_overlays"]), "SM rewrite lacks authority chain")
    require("MAJOR_REWRITE" in sm["external_report"]["current_applicability"], "SM source not marked major rewrite")

    flux = next(paper for paper in papers if paper["name"] == "Flux_Compactifications_in_Heterotic_String_Theory_v3.md")
    require("A07" in flux["authority_overlays"], "flux revision lacks finite-Cech successor")
    require("A15" in flux["authority_overlays"], "flux revision lacks finite projected HYM successor")
    require("A19" in flux["authority_overlays"], "flux revision lacks continuum HYM successor")
    require("old Iwasawa bundle construction remains withdrawn" in flux["external_report"]["current_applicability"], "Iwasawa guard missing")

    markdown = MARKDOWN.read_text(encoding="utf-8")
    require("137 papers" in markdown, "human ledger count missing")
    require("five contain material repairs not propagated to the vault" in markdown, "Theta first-pass lineage missing")
    require("Clause-by-clause applicability" in markdown, "report applicability matrix missing")
    require("High-impact replacement matrix" in markdown, "replacement matrix missing")
    require("Repository disposition" in markdown, "repository disposition table missing")
    require("one-shared-physical-primitive/profile standard" in markdown, "scoped SM closure wording missing")
    require("not zero-knob derivation" in markdown, "no-knob guard missing")
    require("former 4.2-5 TeV crossing" in markdown, "old crossing withdrawal missing")
    require("Rank-three sector transfer and uniqueness over all HYM branches remain open" in markdown, "post-HYM scope guard missing")
    require("2/9 closed, six partial, and one dependency-blocked" in markdown, "strict-upgrade status is stale")
    require("Y+Zr=0.00932703<r=0.01" in markdown, "validated HYM successor missing")
    require("prediction-with-uncertainty standard" in markdown, "CKM prediction-profile successor missing")
    require("Dirac channel" in markdown, "neutrino channel successor missing")
    require("m_lightest=0" in markdown, "neutral minimal-trace successor missing")
    require("All 36 neutral numerical rows" in markdown, "neutral two-primitive profile completion missing")
    require("exact Lens/Dedekind mixed reciprocity residue 1/240" in markdown, "neutral Lens/Dedekind successor missing")
    require("conditional 11D-lift E0 candidate at 18 ppm" in markdown, "neutral universal-E0 successor missing")
    require("physical neutral-operator lift identification" in markdown, "neutral E0 lift guard missing")
    require("composite 661/4 reduction" in markdown, "neutral composite spectrum successor missing")
    require("common-circle/nil same-operator bridge" in markdown, "neutral recursive branch bridge guard missing")
    require("Native MTT is 10D" in markdown, "native MTT dimension guard missing")
    require("native 10D formula misses A40 by 448^2" in markdown, "native 10D counterfactual missing")
    require("A_Q=M3(C)^3 is not directly the SM finite algebra" in markdown, "same-geometry algebra no-go missing")
    require("rank-one/rank-two/full projectors and quaternionic weak real structure" in markdown, "same-geometry source frontier missing")
    require("target-ranked hypothesis is not yet a prediction" in markdown, "neutral phase epistemic guard missing")
    require("one selected complex-symmetric neutral operator" in markdown, "neutral source contraction missing")
    require("source-provenance inventory is now 4/8" in markdown, "neutral operator inventory guard missing")
    require("remaining exits are Dirac-complete" in markdown, "neutral normal-form successor missing")
    require("neutral OK gates are 3/9" in markdown and "accepted neutral exits remain 0/3" in markdown, "neutral overlap/action gate missing")
    require("5/9 and readiness to 6/12" in markdown, "neutral projector/Gram readiness successor missing")
    require("typed L x N^c x H_u neutral trilinear carrier skeleton" in markdown, "neutral Gamma_nu structural successor missing")
    require("readiness advances to 7/13" in markdown, "neutral Gamma_nu readiness successor missing")
    require("Gamma_nu^chan=I3+X3" in markdown, "neutral finite channel operator successor missing")
    require("six active channels and three exact zeros" in markdown, "neutral finite channel count missing")
    require("6/9" in markdown and "readiness to 8/13" in markdown, "neutral finite channel readiness missing")
    require("absolute action scale/prefactor" in markdown and "dimensionful M_D/M_L/M_R remain open" in markdown, "neutral remaining-field guard missing")
    require("two-representative neutral relative-amplitude orbit" in markdown, "neutral relative-amplitude orbit missing")
    require("3/2 +/- i sqrt(3)/2" in markdown, "neutral relative coefficients missing")
    require("Eighteen relative dimensionless rows" in markdown, "neutral relative row count missing")
    require("absolute action scale/prefactor" in markdown, "neutral absolute-scale guard missing")
    require("a_int=0.34195899479289005" in markdown, "neutral internal amplitude missing")
    require("9/9 rows and 7/7 provenance fields" in markdown, "neutral internal row closure missing")
    require("Nil subtraction gives `[0,3,6]`" in markdown, "neutral nil-shift obstruction missing")
    require("normal-ordering ratio `0.029805`" in markdown, "neutral ratio postcheck missing")
    require("selected non-affine spectral-action slope plus one universal scale" in markdown, "neutral surviving route missing")
    require("q7/qmod" in markdown and "0.031881" in markdown, "neutral circle trial missing")
    require("CP/retarded characters cannot be reused as Majorana self-characters" in markdown, "neutral character typing guard missing")
    require("typed neutral circle/proper-time-to-mass-cost transfer or neutral real-structure functor" in markdown, "neutral transfer frontier missing")
    require("self-adjoint, chirally odd `6x6` operator" in markdown, "proto-spinor Dirac successor missing")
    require("`H1` is indefinite" in markdown, "neutral H1 signature guard missing")
    require("`[0,a,2a]`" in markdown and "ratio `1/4`" in markdown, "neutral alignment trial missing")
    require("radial second-variation/VEV theorem" in markdown, "neutral radial successor missing")
    require("positive spectrum `[2,2,8]`" in markdown, "neutral positive second variation missing")
    require("adds no neutrino-specific parameter" in markdown, "neutral VEV parameter policy missing")
    require("typed neutral Higgs-insertion functor and coordinate normalization" in markdown, "neutral insertion frontier missing")
    require("same-source rank-one `H:h0` insertion" in markdown, "neutral H insertion successor missing")
    require("dY_nu/dh_H=Gamma_nu^chan=I3+X3" in markdown, "neutral H derivative identity missing")
    require("action-weighted neutral response and dimensionful Dirac readout" in markdown, "neutral action-weight frontier missing")
    require("non-identifiable factorization-gauge variables" in markdown, "neutral effective-weight reduction missing")
    require("one selected non-affine shape coordinate plus one absolute scale" in markdown, "neutral reduced physical cutset missing")
    require("q7-only CRT lift `128/448=2/7`" in markdown, "neutral CRT phase correction missing")
    require("`0.031881` clue is retired" in markdown, "neutral mistyped near-hit not retired")
    require("H_nu(phi_nu)=exp(i phi_nu)H_cen" in markdown, "neutral common-circle factorization missing")
    require("phi_nu=(arg det H_nu)/3" in markdown, "neutral determinant phase readout missing")
    require("all 27 finite Heisenberg elements" in markdown, "neutral determinant no-go missing")
    require("smooth determinant-line `U(1)`" in markdown, "neutral smooth lift target missing")
    require("+12 matter and -12 complete-27 exotics cancel" in markdown, "E6 anomaly cancellation missing")
    require("N_DW=3" in markdown, "domain-wall diagnostic missing")
    require("selected flux/threshold axion-current anomaly-matching map" in markdown, "strong-CP source guard missing")
    require("q=79/F/m1" in markdown, "retarded branch representative successor missing")
    require("A125" in markdown, "q79 interval Picard-Lefschetz successor missing")
    require("A126" in markdown, "q79 validated endpoint-beta successor missing")
    require("finite flat of rank two" in markdown, "q79 finite-flat divisor theorem missing")
    require("||beta(1)||_2>2.2500100575" in markdown, "q79 endpoint beta bound missing")
    require("frozen selected-side `ell=0`" in markdown, "q79 selected-branch scope missing")
    require("interval `8x92` period lattice" in markdown, "q79 next period-lattice gate missing")
    require("period transition has determinant `-1`" in markdown, "q79 chart covariance theorem missing")
    require("first apparent node is a chart artifact" in markdown, "q79 false-wall correction missing")
    require("2.729845 -> 2.357980" in markdown, "q79 ell-zero continuation missing")
    require("V_k=2*pi*i*t_*^k/sqrt(f_tt(t_*)/2)" in markdown, "q79 local vanishing state missing")
    require("projective overlap `0.999999999999962`" in markdown, "q79 transported jump execution missing")
    require("minimum strict-inclusion margin `6.385e-11`" in markdown, "q79 Krawczyk enclosure missing")
    require("|V_0|>0.012334923056187106" in markdown, "q79 nonzero interval jump bound missing")
    require("`2995` ACB integrals" in markdown, "q79 interval base lift missing")
    require("Validated high-order selected-side endpoint beta transport" in markdown, "q79 endpoint transport guard missing")

    print(
        json.dumps(
            {
                "target_papers": counts["target_papers"],
                "report_entries_mapped": counts["external_report_paper_entries"],
                "unmatched_report_entries": counts["unmatched_report_entries"],
                "authority_sources": len(data["authorities"]),
                "report_clause_decisions": len(data["report_clause_decisions"]),
                "high_impact_update_families": len(data["high_impact_updates"]),
                "status": "READY_FOR_NEW_VERSION_EDITING_PASS",
            },
            indent=2,
        )
    )
    print("corpus revision update ledger audit passed")


if __name__ == "__main__":
    main()
