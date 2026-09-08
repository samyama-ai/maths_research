---
id: 03-geometry/p-w-conjecture
title: "P=W Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# P=W Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/p-w-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $C$ be a smooth complex projective curve of genus $g \geq 2$, and fix $n \geq 1$, $d \in \mathbb{Z}$ with $\gcd(n,d) = 1$. Non-abelian Hodge theory gives a real-analytic diffeomorphism

$$\Psi \colon \mathcal{M}_{\mathrm{Dol}}(n,d) \xrightarrow{\ \sim\ } \mathcal{M}_{B}(n,d)$$

between the moduli space of stable Higgs bundles (Dolbeault side) and the twisted character variety (Betti side). The two sides carry different extra structure: $\mathcal{M}_{\mathrm{Dol}}$ carries the **perverse filtration** $P_\bullet$ induced by the Hitchin map, and $\mathcal{M}_B$ carries Deligne's **weight filtration** $W_\bullet$ on its mixed Hodge structure. $\Psi$ is not algebraic, so no formal reason links them.

**Conjecture (de Cataldo–Hausel–Migliorini, 2012).** For all $m \geq 0$ and all $k \geq 0$,

$$P_k H^m(\mathcal{M}_{\mathrm{Dol}}(n,d),\mathbb{Q}) \;=\; W_{2k} H^m(\mathcal{M}_B(n,d),\mathbb{Q}) \;=\; W_{2k+1} H^m(\mathcal{M}_B(n,d),\mathbb{Q}),$$

under $\Psi^*$. A complete proof must produce the equality of filtrations for every $n$, $d$ coprime and every $g \geq 2$; a disproof needs one class whose perverse degree differs from half its weight.

**Status.** Proved for $\mathrm{GL}_n$ in 2022 by two independent groups (Maulik–Shen; Hausel–Mellit–Minets–Schiffmann). The page is retained because the natural generalisations — singular (non-coprime) character varieties, other reductive groups, wild/parabolic settings — remain open in general.

## 2. Mathematical Foundations

**Dolbeault side.** A Higgs bundle is a pair $(E,\theta)$ with $E$ a rank-$n$ degree-$d$ vector bundle on $C$ and $\theta \in H^0(C, \mathrm{End}(E)\otimes K_C)$. For $\gcd(n,d)=1$, stability equals semistability and $\mathcal{M}_{\mathrm{Dol}}$ is a smooth quasi-projective variety, holomorphic symplectic, of dimension

$$\dim_{\mathbb{C}} \mathcal{M}_{\mathrm{Dol}} = 2n^2(g-1) + 2.$$

The **Hitchin map** sends $(E,\theta)$ to the characteristic polynomial of $\theta$:

$$h \colon \mathcal{M}_{\mathrm{Dol}} \longrightarrow \mathcal{A} = \bigoplus_{i=1}^{n} H^0(C, K_C^{\otimes i}), \qquad r := \dim \mathcal{A} = n^2(g-1)+1 = \tfrac12 \dim \mathcal{M}_{\mathrm{Dol}}.$$

$h$ is proper and Lagrangian: an algebraically completely integrable system (Hitchin 1987), with generic fibre an abelian variety (the compactified Jacobian of the spectral curve).

**Perverse filtration.** By the decomposition theorem, $Rh_*\mathbb{Q}[r]$ splits into shifted perverse sheaves on $\mathcal{A}$. Define

$$P_k H^m(\mathcal{M}_{\mathrm{Dol}}) = \operatorname{Im}\Big( \mathbb{H}^{m-r}\big(\mathcal{A}, {}^{p}\tau_{\leq k}\,(Rh_*\mathbb{Q}[r])\big) \to H^m(\mathcal{M}_{\mathrm{Dol}}) \Big),$$

so $0 = P_{-1} \subset P_0 \subset \cdots \subset P_{2r} = H^m$. Equivalently (de Cataldo–Migliorini 2010), for a general flag of affine-linear subspaces $\Lambda_0 \subset \Lambda_1 \subset \cdots \subset \Lambda_r = \mathcal{A}$ with $\dim \Lambda_s = s$,

$$P_k H^m(\mathcal{M}_{\mathrm{Dol}}) = \ker\Big( H^m(\mathcal{M}_{\mathrm{Dol}}) \to H^m\big(h^{-1}(\Lambda_{m-k-1})\big) \Big).$$

This description makes multiplicativity plausible; multiplicativity $P_i \cdot P_j \subset P_{i+j}$ is a theorem here (Shen–Zhang, Maulik–Shen).

**Betti side.** For $\zeta_n = e^{2\pi i d/n}$,

$$\mathcal{M}_B(n,d) = \Big\{ (A_1,B_1,\dots,A_g,B_g) \in \mathrm{GL}_n(\mathbb{C})^{2g} \;:\; \prod_{i=1}^{g} [A_i,B_i] = \zeta_n \cdot \mathrm{Id} \Big\} /\!\!/ \mathrm{PGL}_n .$$

Coprimality makes the $\mathrm{PGL}_n$-action free, so $\mathcal{M}_B$ is smooth affine. Its cohomology carries a mixed Hodge structure with increasing weight filtration $W_\bullet$; it is of Hodge–Tate type with only even weights, whence the $W_{2k} = W_{2k+1}$ clause. The mixed Hodge polynomial

$$H(\mathcal{M}_B; q,t) = \sum_{k,m} \dim \big(\mathrm{Gr}^W_{2k} H^m\big)\, q^k t^m$$

was conjecturally computed by Hausel–Rodriguez-Villegas (2008) from arithmetic point counts over $\mathbb{F}_q$.

**Tautological generators.** Fix a universal bundle $\mathbb{E}$ on $C \times \mathcal{M}$. For $\gamma \in H^j(C,\mathbb{Q})$ set $c_k(\gamma) = \int_C \mathrm{ch}_k(\mathbb{E}) \cup \gamma$. These classes generate $H^*(\mathcal{M}_{\mathrm{Dol}})$ as a ring (Markman; Shende). On the Betti side they have weight exactly $2k$, so P=W predicts the sharp perverse bound

$$c_k(\gamma) \in P_k H^{2k-j}(\mathcal{M}_{\mathrm{Dol}}), \qquad c_k(\gamma) \notin P_{k-1}.$$

By multiplicativity, "P $\subseteq$ W" for generators plus a dimension count implies the full statement.

## 3. History & State of the Art (SOTA)

- **1987.** Hitchin's self-duality equations; Hitchin and Donaldson, plus Corlette (1988) and Simpson (1992–94), assemble non-abelian Hodge theory: $\mathcal{M}_{\mathrm{Dol}} \cong \mathcal{M}_{\mathrm{dR}} \cong \mathcal{M}_B$ as real-analytic spaces.
- **2008.** Hausel–Rodriguez-Villegas compute the $E$-polynomial and conjecture the mixed Hodge polynomial of $\mathcal{M}_B$; they also formulate **Curious Hard Lefschetz** — an $\mathfrak{sl}_2$-symmetry of $\mathrm{Gr}^W$ that has no Betti-side explanation but is the obvious relative hard Lefschetz on the Dolbeault side.
- **2012.** de Cataldo, Hausel and Migliorini state P=W and prove it for $n=2$ (type $A_1$), all $g$, in *Annals of Mathematics* 175.
- **2019–2020.** Mellit proves the Hausel–Rodriguez-Villegas formula and Curious Hard Lefschetz using cell decompositions and affine Springer fibres.
- **2021–2022.** Shen–Zhang prove parabolic cases in genus $\le 1$ via Hilbert schemes of points; Felisetti–Mauri prove the intersection-cohomology version PI=WI for symplectic-resolution cases; de Cataldo–Maulik–Neguț prove P=W for $g=2$ and all $n$ (*JAMS* 35), by degenerating to abelian surfaces and propagating along the moduli of curves.
- **September 2022.** Two independent proofs for $\mathrm{GL}_n$, all $n$, all $g\geq 2$: Maulik–Shen (*Annals* 200, 2024), via $\chi$-independence, Ngô's support theorem and vanishing-cycle comparison with moduli of 1-dimensional sheaves on a surface; and Hausel–Mellit–Minets–Schiffmann, via a global $\mathfrak{sl}_2$-type Lie algebra $\mathcal{H}_2$ of Hecke-modification operators acting on $H^*(\mathcal{M}_{\mathrm{Dol}})$.
- **2023–2026.** Maulik–Shen–Yin recast both proofs through a Fourier transform on the Hitchin base, extending P=W-type statements to singular moduli.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $n=1$, all $g$ | Trivial; direct computation on $T^*\mathrm{Jac}$ vs $(\mathbb{C}^*)^{2g}$ | folklore |
| $n=2$, all $g\ge2$, $d$ odd | Full P=W | de Cataldo–Hausel–Migliorini 2012 |
| $g=2$, all $n$ coprime $d$ | Full P=W | de Cataldo–Maulik–Neguț 2022 |
| $\mathrm{GL}_n$, all $n$, $g\ge 2$, $\gcd(n,d)=1$ | **Theorem** | Maulik–Shen 2024; Hausel–Mellit–Minets–Schiffmann 2022 |
| $\mathrm{SL}_n$ / $\mathrm{PGL}_n$ | Follows for $\mathrm{SL}_n$ from the $\mathrm{GL}_n$ theorem via the $\Gamma = (\mathbb{Z}/n)^{2g}$-isotypic decomposition; the variant twisted by a gerbe (topological mirror symmetry) is a separate theorem of Groechenig–Wyss–Ziegler (2020) | de Cataldo–Maulik–Neguț, Selecta 2022 |
| Parabolic, $g=0,1$ with punctures | P=W via Hilbert schemes of points on elliptic surfaces | Shen–Zhang 2021 |
| Singular case, PI=WI | Proven when $\mathcal{M}_B$ admits a symplectic resolution: $(n,d)$ with $g=1$ arbitrary $n$; $g=2$, $n=2$ | Felisetti–Mauri 2022 |
| Curious Hard Lefschetz | Proven for all $n,g$ | Mellit 2020 |

## 5. Principal Obstacles

- **No algebraic map to transport filtrations.** $\Psi$ is a diffeomorphism built from harmonic-metric PDE; it does not respect any algebraic structure, so functoriality of weights is unavailable. Every proof must compare the two filtrations on *explicitly named* cohomology classes.
- **Weights are not motivic-visible on the Dolbeault side.** $H^*(\mathcal{M}_{\mathrm{Dol}})$ is pure of Hodge–Tate type; all the Betti weight information has to be reconstructed from the geometry of the Hitchin fibration.
- **The hard half is the upper bound $P \subseteq W$.** Producing classes of low perverse degree is easy (restrict to fibres); proving $c_k(\gamma) \notin P_{k-1}$, i.e. sharpness, requires control of *all* summands of $Rh_*\mathbb{Q}$, including those supported on the deep strata of $\mathcal{A}$ where spectral curves are singular or non-reduced.
- **Support theorems degenerate off the elliptic locus.** Ngô's support theorem applies over the anisotropic/elliptic locus; the Hitchin base for $\mathrm{GL}_n$ contains the whole nilpotent and reducible locus where the $\delta$-regularity bounds fail, and naive induction on $n$ loses the coprimality that guarantees smoothness.
- **Standard tools fail.** Mixed Hodge module weights compute the *perverse* filtration on the Dolbeault side but say nothing about the Betti MHS; deformation to nearby curves does not by itself carry the character variety; and the classical Bialynicki-Birula/Morse decomposition of $\mathcal{M}_{\mathrm{Dol}}$ by the $\mathbb{C}^*$-action refines the wrong filtration (the Hodge–Bialynicki-Birula one), not $P$.

## 6. The Gap

For $\mathrm{GL}_n$ with $\gcd(n,d)=1$ there is now no gap: the statement of Section 1 is a theorem. The remaining boundary lies one step outward.

1. **Non-coprime / singular case (PI=WI).** When $\gcd(n,d)>1$, $\mathcal{M}_B$ is singular; the conjecture is restated with intersection cohomology, $P_k IH^m(\mathcal{M}_{\mathrm{Dol}}) = W_{2k} IH^m(\mathcal{M}_B)$. Known only when a symplectic resolution exists or in low rank; the obstruction is that the decomposition theorem for $h$ on a singular total space has summands with unclassified supports.
2. **Other groups.** For $G$ reductive beyond type $A$, tautological generation of $H^*(\mathcal{M}_{\mathrm{Dol}}^G)$ is not known, so both existing proof strategies lose their starting point. Endoscopic contributions appear in $Rh_*\mathbb{Q}$ and have no evident Betti counterpart.
3. **Wild / irregular and higher-dimensional analogues.** For wild Higgs bundles and for $\dim C > 1$ (Simpson's programme), even the correct formulation of $\mathcal{A}$ and of $P_\bullet$ is unsettled.

## 7. Current Research (as of June 2026)

- **Fourier-theoretic unification.** Maulik–Shen–Yin's "Perverse filtrations and Fourier transforms" reproves P=W by transporting the perverse filtration through a Fourier–Mukai-type transform on the Hitchin base and identifies the multiplicativity statement as a formal consequence. This framework is being pushed toward PI=WI for arbitrary $(n,d)$ *(frontier — verify)*.
- **Cohomological Hall algebra methods.** The Hausel–Mellit–Minets–Schiffmann $\mathcal{H}_2$-action is being extended to parabolic and multiplicative (Betti–Deligne) settings by groups at IST Austria, CNRS/Jussieu and Edinburgh; the target is a Lie-algebra proof independent of $\chi$-independence.
- **$\chi$-independence and enumerative geometry.** Maulik–Shen's cohomological $\chi$-independence for one-dimensional sheaves connects P=W to Gopakumar–Vafa invariants of local surfaces; Kinjo–Koseki and collaborators develop the DT-theoretic version.
- **Mirror symmetry.** Topological mirror symmetry (Hausel–Thaddeus; proved $p$-adically by Groechenig–Wyss–Ziegler) is being combined with P=W to constrain the $\mathrm{SL}_n/\mathrm{PGL}_n$ pair; the compatibility of $P$, $W$, and the Langlands-dual stringy Hodge numbers is an active question.
- **Institutions.** MIT (Maulik), Yale/Rutgers (Shen, Yin), IST Austria (Hausel), Stony Brook (de Cataldo), Bologna (Migliorini), IMJ-PRG (Schiffmann), Milan (Mauri, Felisetti).

## 8. Future Work

- Prove PI=WI in full generality; the expected route is a support theorem for the Hitchin map on singular moduli, plus an intersection-cohomology analogue of tautological generation.
- Find tautological-type generators of $H^*(\mathcal{M}_{\mathrm{Dol}}^G)$ for $G$ of type $B,C,D,G_2$, or replace generation by a Lie-algebra action that exists for all $G$.
- Upgrade P=W from an equality of filtrations to a statement about mixed Hodge *modules*, giving a canonical isomorphism rather than a numerical coincidence.
- Formulate and test P=W for character varieties of higher-dimensional base and for the de Rham/Betti correspondence with irregular singularities.
- Extract from P=W new closed formulas for $\mathrm{Gr}^W IH^*(\mathcal{M}_B)$ and compare against arithmetic point counts as a consistency check.

## 9. Key References

- **[Foundational]** N. Hitchin. *The self-duality equations on a Riemann surface.* Proc. London Math. Soc. (3) 55 (1987), 59–126. [DOI](https://doi.org/10.1112/plms/s3-55.1.59)
- **[Foundational]** C. Simpson. *Moduli of representations of the fundamental group of a smooth projective variety, I & II.* Publ. Math. IHÉS 79 (1994), 47–129; 80 (1994), 5–79. [DOI](https://doi.org/10.1007/bf02698895)
- **[Foundational]** K. Corlette. *Flat $G$-bundles with canonical metrics.* J. Differential Geom. 28 (1988), 361–382. [DOI](https://doi.org/10.4310/jdg/1214442469)
- **[Foundational]** M. de Cataldo, L. Migliorini. *The perverse filtration and the Lefschetz hyperplane theorem.* Ann. of Math. 171 (2010), 2089–2113. [DOI](https://doi.org/10.4007/annals.2010.171.2089)
- **[Foundational]** T. Hausel, F. Rodriguez-Villegas. *Mixed Hodge polynomials of character varieties.* Invent. Math. 174 (2008), 555–624. [DOI](https://doi.org/10.1007/s00222-008-0142-x)
- **[Foundational]** M. de Cataldo, T. Hausel, L. Migliorini. *Topology of Hitchin systems and Hodge theory of character varieties: the case $A_1$.* Ann. of Math. 175 (2012), 1329–1407. [DOI](https://doi.org/10.4007/annals.2012.175.3.7)
- **[SOTA]** D. Maulik, J. Shen. *The P=W conjecture for $\mathrm{GL}_n$.* Ann. of Math. 200 (2024), 529–556. [DOI](https://doi.org/10.4007/annals.2024.200.2.3)
- **[SOTA]** T. Hausel, A. Mellit, A. Minets, O. Schiffmann. *P=W via $H_2$.* arXiv:2209.05429 (2022).
- **[SOTA]** M. de Cataldo, D. Maulik, A. Neguț. *Hitchin fibrations, abelian surfaces, and the P=W conjecture.* J. Amer. Math. Soc. 35 (2022), 911–953. [DOI](https://doi.org/10.1090/jams/989)
- **[SOTA]** D. Maulik, J. Shen. *Cohomological $\chi$-independence for moduli of one-dimensional sheaves and moduli of Higgs bundles.* Geom. Topol. 27 (2023), 1539–1586. [DOI](https://doi.org/10.2140/gt.2023.27.1539)
- **[SOTA]** A. Mellit. *Poincaré polynomials of character varieties, Macdonald polynomials and affine Springer fibers.* Ann. of Math. 192 (2020), 165–228. [DOI](https://doi.org/10.4007/annals.2020.192.1.3)
- **[SOTA]** C. Felisetti, M. Mauri. *P=W conjectures for character varieties with symplectic resolution.* J. Éc. polytech. Math. 9 (2022), 853–905. [DOI](https://doi.org/10.5802/jep.196)
- **[SOTA]** J. Shen, Z. Zhang. *Perverse filtrations, Hilbert schemes, and the P=W conjecture for parabolic Higgs bundles.* Algebraic Geometry 8 (2021), 465–489. [DOI](https://doi.org/10.14231/ag-2021-014)
- **[SOTA]** M. Groechenig, D. Wyss, P. Ziegler. *Mirror symmetry for moduli spaces of Higgs bundles via p-adic integration.* Invent. Math. 221 (2020), 505–596. [DOI](https://doi.org/10.1007/s00222-020-00957-8)
- **[Survey]** T. Hausel. *Global topology of the Hitchin system.* In *Handbook of Moduli*, Vol. II, Adv. Lect. Math. 25, International Press, 2013, 29–69.
- **[Survey]** B. C. Ngô. *Le lemme fondamental pour les algèbres de Lie.* Publ. Math. IHÉS 111 (2010), 1–169. (Source of the support theorem.). [DOI](https://doi.org/10.1007/s10240-010-0026-7)

## 10. Worked Example / Concrete Special Case

**Rank 1, genus $g$.** Take $n=1$, $d=0$.

*Dolbeault.* A rank-1 Higgs bundle is $(L,\theta)$ with $L \in \mathrm{Jac}(C)$ and $\theta \in H^0(C,K_C) \cong \mathbb{C}^g$. So

$$\mathcal{M}_{\mathrm{Dol}} = T^*\mathrm{Jac}(C) = \mathrm{Jac}(C) \times \mathbb{C}^g, \qquad h = \mathrm{pr}_2 \colon \mathcal{M}_{\mathrm{Dol}} \to \mathcal{A} = \mathbb{C}^g, \ r=g.$$

$h$ is a trivial fibre bundle with fibre the abelian variety $\mathrm{Jac}(C)$, so

$$Rh_*\mathbb{Q}[g] \;\cong\; \bigoplus_{i=0}^{2g} H^i(\mathrm{Jac}(C),\mathbb{Q}) \otimes \mathbb{Q}_{\mathcal{A}}[g-i],$$

and $\mathbb{Q}_{\mathcal{A}}[g]$ is perverse ($\mathcal{A}$ smooth of dimension $g$). Hence the $i$-th summand sits in perverse degree $i$, and

$$P_k H^m(\mathcal{M}_{\mathrm{Dol}}) = \bigoplus_{i \le k} H^i(\mathrm{Jac}) \cap H^m = \begin{cases} H^m(\mathrm{Jac}) = \Lambda^m H^1(C) & m \le k,\\ 0 & m > k.\end{cases}$$

So $P_k H^m$ is everything for $k \geq m$ and zero otherwise; the perverse degree of a class in $H^m$ is exactly $m$.

*Betti.* $\mathcal{M}_B = \mathrm{Hom}(\pi_1(C),\mathbb{C}^*) = (\mathbb{C}^*)^{2g}$, so $H^*(\mathcal{M}_B) = \Lambda^*(V)$ with $V = H^1((\mathbb{C}^*)^{2g}) \cong \mathbb{Q}^{2g}$. Each generator is $\frac{dz_j}{z_j}$, of type $(1,1)$ and weight $2$ (as for $H^1(\mathbb{C}^*)$). Therefore $\Lambda^m V$ is pure of weight $2m$ and

$$W_{2k}H^m(\mathcal{M}_B) = \begin{cases} H^m & m \le k, \\ 0 & m>k.\end{cases}$$

*Comparison.* The two answers agree term by term: $P_k H^m = W_{2k}H^m$, and both jump exactly at $k=m$. Concretely for $g=2$: $\dim \mathcal{M} = 4$, $H^1$ has dimension $4$ with all classes of perverse degree $1$ and weight $2$; $H^2$ has dimension $6$, perverse degree $2$, weight $4$. The mixed Hodge polynomial $H(q,t) = (1+qt)^{2g}$ matches the perverse Poincaré polynomial $\sum_{i} \dim H^i(\mathrm{Jac})\, q^{i}t^{i} = (1+qt)^{2g}$.

*Why it is hard for $n \ge 2$.* Here $h$ was a trivial bundle and $Rh_*\mathbb{Q}$ had a single support, all of $\mathcal{A}$. For $n\geq 2$ the fibres degenerate over the discriminant locus of singular spectral curves, extra summands with small support can a priori appear, and the sharpness statement $c_k(\gamma)\notin P_{k-1}$ becomes the whole content — this is exactly what Ngô-type support theorems (Maulik–Shen) or the $\mathcal{H}_2$-action (Hausel–Mellit–Minets–Schiffmann) are needed to control.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*