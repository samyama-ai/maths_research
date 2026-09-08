---
id: 03-geometry/bott-conjecture
title: "Bott Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bott Conjecture (Rational Ellipticity of Nonnegatively Curved Manifolds)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/bott-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Bott; formulated in print by Grove–Halperin, 1982).** Let $M$ be a closed, simply connected smooth manifold admitting a Riemannian metric of nonnegative sectional curvature, $\sec \ge 0$. Then $M$ is **rationally elliptic**, i.e.
$$\dim_{\mathbb{Q}} \pi_*(M)\otimes\mathbb{Q} \;=\; \sum_{i\ge 2}\dim_{\mathbb{Q}}\big(\pi_i(M)\otimes\mathbb{Q}\big) \;<\; \infty .$$

Equivalently (Félix–Halperin dichotomy): $M$ is **not** rationally hyperbolic, so the sequence $\dim(\pi_i(M)\otimes\mathbb{Q})$ does not grow exponentially.

A proof must show the implication for *all* such $M$ in all dimensions; a disproof requires one closed simply connected rationally hyperbolic manifold carrying a $\sec\ge0$ metric — e.g. a metric of $\sec\ge0$ on $\mathbb{CP}^2\\#\mathbb{CP}^2\\#\mathbb{CP}^2$ or on $\left(S^2\times S^2\right)\\#\left(S^2\times S^2\right)$. Simple connectivity is essential: $T^n$ is flat and rationally elliptic, but the hypothesis is imposed so that the statement is about the universal-cover-free homotopy type; the non-simply-connected version is handled by the Cheeger–Gromoll structure theory.

*Disambiguation:* "Bott conjecture" also names the **Bott vanishing conjecture** for foliations and its algebro-geometric analogue. This page concerns only the curvature/rational-homotopy statement, sometimes called the **Bott–Grove–Halperin conjecture**.

## 2. Mathematical Foundations

**Sectional curvature.** For a Riemannian manifold $(M,g)$ and a $2$-plane $\sigma=\mathrm{span}(X,Y)\subset T_pM$,
$$\sec(\sigma)=\frac{\langle R(X,Y)Y,X\rangle}{|X|^2|Y|^2-\langle X,Y\rangle^2},$$
with $R$ the curvature tensor. $\sec\ge0$ means $\sec(\sigma)\ge0$ for all $p,\sigma$.

**Minimal Sullivan models.** For a simply connected space $M$ with finite-dimensional rational cohomology there is a commutative differential graded algebra $(\Lambda V,d)$, unique up to isomorphism, with $V=\bigoplus_{i\ge2}V^i$, $d(V)\subset \Lambda^{\ge2}V$, and a quasi-isomorphism $(\Lambda V,d)\xrightarrow{\simeq} A_{PL}(M)$. Then
$$V^i \cong \operatorname{Hom}\big(\pi_i(M)\otimes\mathbb{Q},\mathbb{Q}\big).$$
$M$ is **elliptic** if both $\dim V<\infty$ and $\dim H^*(M;\mathbb{Q})<\infty$; otherwise **hyperbolic**.

**Numerical consequences of ellipticity** (Friedlander–Halperin; Halperin). Write $x_1,\dots,x_q$ for the even-degree generators and $y_1,\dots,y_r$ for the odd ones, $n=\dim M$. Then
$$n=\sum_{j=1}^{r}\deg y_j-\sum_{i=1}^{q}\big(\deg x_i-1\big),\qquad q\le \tfrac{n}{2},\qquad r\le n,\qquad q\le r,$$
$$\chi_\pi(M):=\dim\pi_{\mathrm{even}}\otimes\mathbb{Q}-\dim\pi_{\mathrm{odd}}\otimes\mathbb{Q}\le 0,\qquad \chi(M)\ge0,$$
with $\chi(M)>0\iff\chi_\pi(M)=0$, and the total Betti number bound
$$\sum_i \dim H^i(M;\mathbb{Q})\le 2^{\,n}.$$

**Dichotomy Theorem (Félix–Halperin).** A simply connected finite complex is either elliptic, or $\sum_{i\le k}\dim(\pi_i\otimes\mathbb{Q})$ grows exponentially in $k$.

**Geometric inputs.** Gromov's Betti number theorem: for closed $M^n$ with $\sec\ge0$, $\sum_i b_i(M;F)\le C(n)$ for every field $F$, with $C(n)$ exponential in $n$. Cheeger–Gromoll soul theorem (complete open case) and the Cheeger–Gromoll splitting theorem structure the non-simply-connected setting.

## 3. History & State of the Art (SOTA)

- **1960s–70s.** Raoul Bott raised the question in oral form while studying the topology of loop spaces and homogeneous spaces; every then-known example of $\sec\ge0$ was a homogeneous space or a biquotient, and all of these are elliptic.
- **1979.** Friedlander–Halperin establish the arithmetic constraints on rational homotopy of elliptic spaces, making the conjecture quantitative.
- **1981.** Gromov proves the universal Betti-number bound $C(n)$ under $\sec\ge0$ — the only unconditional topological restriction of this strength known to date. Bott's conjecture predicts the sharp constant $2^n$.
- **1982.** Grove and Halperin publish the conjecture ("Contributions of rational homotopy theory to global problems in geometry", Publ. IHÉS 56), together with the observation that ellipticity would force $\chi(M)\ge0$, recovering a case of the Hopf conjecture, and would bound the growth of $\pi_*$.
- **1987.** Grove–Halperin prove rational ellipticity for manifolds built as double mapping cylinders, hence for all **cohomogeneity-one** manifolds — a class containing many of the known $\sec\ge0$ examples.
- **1994–2003.** Symmetry-based attacks: Searle–Yang (dimension 4 with $S^1$-symmetry), Wilking's torus-action machinery, Paternain–Petean's collapsing/minimal-entropy results in low dimensions.
- **2015–2018.** Amann–Kennard connect positive curvature with large torus symmetry to ellipticity; Galaz-García–Kerin–Radeschi–Wiemeler prove ellipticity for slice-maximal torus actions.
- **State of the art.** No counterexample and no proof in any dimension $\ge 4$ without extra symmetry hypotheses. The conjecture is open even for closed simply connected $4$-manifolds.

## 4. Partial Results / Verified Cases

- **Dimension $\le 3$.** Trivially true: closed simply connected $3$-manifolds are $S^3$ (Poincaré/Perelman), which is elliptic.
- **Dimension 4 with symmetry.** Searle–Yang (1994): a closed simply connected $4$-manifold with $\sec\ge0$ and an isometric $S^1$-action has $\chi(M)\le 4$, hence $b_2\le2$, hence is rationally elliptic. Without symmetry, dimension 4 is open — it is unknown whether $\\#_3\mathbb{CP}^2$ admits $\sec\ge0$.
- **All known examples.** Compact homogeneous spaces $G/H$ have pure elliptic models and are elliptic; the same holds for biquotients $G/\!\!/H$. Since essentially every known closed simply connected manifold with $\sec\ge0$ is a biquotient, a cohomogeneity-one manifold, or built from these by Cheeger deformation / Grove–Ziller gluing, the conjecture holds for the entire known catalogue of examples.
- **Cohomogeneity one.** Grove–Halperin (1987): any closed simply connected manifold with a cohomogeneity-one group action is rationally elliptic — no curvature hypothesis needed.
- **Torus symmetry.** Galaz-García–Kerin–Radeschi–Wiemeler (2018): closed simply connected $M^n$ with $\sec\ge0$ and an isometric *slice-maximal* torus action is rationally elliptic; this covers maximal symmetry rank $\lfloor 2n/3\rfloor$-type hypotheses. Amann–Kennard (2015): positively curved $M^n$ with torus symmetry of rank $\gtrsim \log_2 n$ satisfies strong ellipticity-type conclusions.
- **Weakened conclusions, no symmetry.** Gromov's theorem gives the Betti-number half of the elliptic package (with a non-sharp constant); Kapovitch–Petrunin–Tuschmann (Annals 171, 2010) give the almost-nonnegative-curvature analogue of the $\pi_1$ structure results.
- **Dimensions 5–6 under collapsing.** Paternain–Petean's minimal-entropy techniques give ellipticity for low-dimensional simply connected manifolds admitting $T$-structures / collapsing with curvature bounded below.

## 5. Principal Obstacles

- **No local-to-global curvature operator.** $\sec\ge0$ is a pointwise inequality on $2$-planes; unlike $\mathrm{Ric}\ge0$ or scalar curvature it feeds into no Bochner–Weitzenböck vanishing theorem. Harmonic-form methods (which give $b_1=0$ under $\mathrm{Ric}>0$) simply do not see sectional curvature.
- **Rational homotopy is not a curvature quantity.** Ellipticity is a statement about the *whole* minimal model, i.e. about infinitely many homotopy groups. Comparison geometry controls distances, volumes and critical points of distance functions — these bound cohomology (Gromov), but there is no known mechanism converting a Betti-number bound into a bound on $\dim\pi_*\otimes\mathbb{Q}$. Indeed, no bound $\sum b_i \le B$ implies ellipticity: $\\#_3\mathbb{CP}^2$ has total Betti number $5$ and is hyperbolic.
- **Gromov's constant is not sharp.** His proof runs through critical point theory for distance functions and a covering/compactness argument, producing $C(n)$ far above $2^n$; improving it to $2^n$ is itself a long-standing open problem, and even that would not give ellipticity.
- **Poverty of examples cuts both ways.** The construction toolkit for $\sec\ge0$ (homogeneous, biquotient, Grove–Ziller cohomogeneity one, Cheeger deformation, Riemannian submersion) is closed under operations that preserve ellipticity, so it can neither produce a counterexample nor suggest which structure to prove.
- **Connected sums.** The only plausible source of hyperbolic candidates is connected sums, but there is no obstruction theory forbidding $\sec\ge0$ on $\\#_k\mathbb{CP}^2$ for $k\ge3$; conversely, all known gluing techniques (Gromoll–Meyer, Grove–Ziller) fail to build $\sec\ge0$ on such sums because the pieces cannot be matched with totally geodesic boundary of the required type.
- **Symmetry hypotheses are unavoidable in current proofs.** Every verified case exploits a group action to reduce to a quotient orbifold or a double mapping cylinder. A generic $\sec\ge0$ metric need have no isometries at all.

## 6. The Gap

Proven: ellipticity for manifolds with enough symmetry (cohomogeneity one, slice-maximal torus actions, low-dimensional $S^1$-symmetric cases) and bounded total Betti number for all $\sec\ge0$ manifolds. Conjectured: ellipticity for all of them.

The precise missing step is a mechanism transferring a *lower sectional curvature bound* to *finiteness of the minimal Sullivan model*. Concretely, one must rule out the exponential-growth alternative of the Félix–Halperin dichotomy under $\sec\ge0$. Two intermediate targets frame the gap: (i) sharpen Gromov's constant to $2^n$; (ii) prove the "loop-space" formulation — that for $\sec\ge0$ the Betti numbers of $\Omega M$ grow polynomially rather than exponentially, which by Félix–Halperin–Thomas is equivalent to ellipticity. Neither is currently reachable, because no known curvature argument controls $H_*(\Omega M;\mathbb{Q})$ beyond Morse theory on the path space, which requires curvature *upper* bounds or index estimates unavailable under $\sec\ge0$ alone.

## 7. Current Research (as of June 2026)

- **Symmetry programme.** Groups around Karsten Grove, Wolfgang Ziller (Penn), Burkhard Wilking (Münster), Fernando Galaz-García (Durham), Martin Kerin (Durham), Lee Kennard (Syracuse) and Manuel Amann (Augsburg) continue reducing the required symmetry rank for ellipticity conclusions. The trend is to replace "maximal symmetry rank" by logarithmic-in-$n$ rank hypotheses.
- **Alexandrov-geometric formulation.** Extending the conjecture to finite-dimensional Alexandrov spaces with $\mathrm{curv}\ge0$, so that quotients $M/G$ stay in the category; work of Harvey–Searle and collaborators on orbit-space topology feeds this. *(frontier — verify)*
- **Torus orbifolds and GKM theory.** Wiemeler and coauthors use combinatorial models of torus orbifolds to compute rational homotopy of the quotient data directly. *(frontier — verify)*
- **Collapsing / almost nonnegative curvature.** The Kapovitch–Petrunin–Tuschmann circle of ideas is being pushed toward the statement "almost nonnegatively curved $\Rightarrow$ rationally elliptic up to finite cover", which would be strictly stronger. *(frontier — verify)*
- **Ricci-flow and moduli approaches.** Attempts to use Ricci flow to deform $\sec\ge0$ metrics fail in dimensions $\ge4$ because $\sec\ge0$ is not preserved (Böhm–Wilking counterexamples), so this line is largely dormant.

## 8. Future Work

- **Sharpen Gromov's bound.** Prove $\sum_i b_i(M^n;F)\le 2^n$ for $\sec\ge0$; a proof would very likely carry structural information about the rational homotopy type.
- **Dimension 4 unconditionally.** Show that a closed simply connected $4$-manifold with $\sec\ge0$ has $b_2\le2$, removing the $S^1$-symmetry hypothesis of Searle–Yang. This is the smallest open instance and is regarded as the natural test case.
- **Connected-sum obstruction.** Find any obstruction to $\sec\ge0$ on $\\#_k\mathbb{CP}^2$, $k\ge3$ — a problem of independent interest, since no closed simply connected manifold is currently known *not* to admit $\sec\ge0$ for reasons other than Gromov's bound or the Hopf/Synge-type arguments.
- **Loop space entropy.** Relate the exponential growth rate of $H_*(\Omega M;\mathbb{Q})$ to geometric invariants (minimal volume entropy) that are controlled under $\sec\ge0$, following Paternain–Petean.
- **Weak forms.** Prove the Bott conjecture's corollaries independently: $\chi(M)\ge0$ (Hopf), and $\chi(M)>0\Rightarrow$ vanishing odd rational homotopy.

## 9. Key References

- **[Foundational]** K. Grove, S. Halperin. *Contributions of rational homotopy theory to global problems in geometry.* Publications Mathématiques de l'IHÉS **56** (1982), 171–177. [DOI](https://doi.org/10.1007/bf02700465)
- **[Foundational]** M. Gromov. *Curvature, diameter and Betti numbers.* Commentarii Mathematici Helvetici **56** (1981), 179–195. [DOI](https://doi.org/10.1007/bf02566208)
- **[Foundational]** J. Friedlander, S. Halperin. *An arithmetic characterization of the rational homotopy groups of certain spaces.* Inventiones Mathematicae **53** (1979), 117–133. [DOI](https://doi.org/10.1007/bf01390029)
- **[Foundational]** K. Grove, S. Halperin. *Dupin hypersurfaces, group actions and the double mapping cylinder.* Journal of Differential Geometry **26** (1987), 429–459. [DOI](https://doi.org/10.4310/jdg/1214441486)
- **[SOTA / Recent]** C. Searle, D. Yang. *On the topology of non-negatively curved simply connected 4-manifolds with continuous symmetry.* Duke Mathematical Journal **74** (1994), 547–556.
- **[SOTA / Recent]** V. Kapovitch, A. Petrunin, W. Tuschmann. *Nilpotency, almost nonnegative curvature, and the gradient push.* Annals of Mathematics **171** (2010), 343–373.
- **[SOTA / Recent]** M. Amann, L. Kennard. *Positive curvature and rational ellipticity.* Algebraic & Geometric Topology **15** (2015), 2269–2301. [DOI](https://doi.org/10.2140/agt.2015.15.2269)
- **[SOTA / Recent]** F. Galaz-García, M. Kerin, M. Radeschi, M. Wiemeler. *Torus orbifolds, slice-maximal torus actions and rational ellipticity.* International Mathematics Research Notices (2018). [DOI](https://doi.org/10.1093/imrn/rnx064)
- **[SOTA / Recent]** G. P. Paternain, J. Petean. *Minimal entropy and collapsing with curvature bounded from below.* Inventiones Mathematicae **151** (2003), 415–450. [DOI](https://doi.org/10.1007/s00222-002-0262-7)
- **[Survey]** B. Wilking. *Nonnegatively and positively curved manifolds.* Surveys in Differential Geometry **XI** (2007), 25–62. [DOI](https://doi.org/10.4310/sdg.2006.v11.n1.a3)
- **[Survey]** W. Ziller. *Examples of Riemannian manifolds with non-negative sectional curvature.* Surveys in Differential Geometry **XI** (2007), 63–102. [DOI](https://doi.org/10.4310/sdg.2006.v11.n1.a4)
- **[Survey / Textbook]** Y. Félix, S. Halperin, J.-C. Thomas. *Rational Homotopy Theory.* Graduate Texts in Mathematics 205, Springer, 2001.

## 10. Worked Example / Concrete Special Case

**Claim.** $M=\mathbb{CP}^2\\#\mathbb{CP}^2\\#\mathbb{CP}^2$ is rationally hyperbolic; hence the Bott conjecture predicts $M$ carries no metric with $\sec\ge0$. Whether it does is open.

**Cohomology.** $H^0=\mathbb{Q}$, $H^2=\mathbb{Q}\langle u_1,u_2,u_3\rangle$, $H^4=\mathbb{Q}\langle\mu\rangle$, with intersection form $\mathrm{diag}(1,1,1)$:
$$u_i\,u_j=\delta_{ij}\,\mu .$$

**Minimal model, stage 1.** Take $V^2=\mathbb{Q}\langle x_1,x_2,x_3\rangle$, $dx_i=0$, mapping $x_i\mapsto u_i$. In degree 4, $\Lambda^2V^2$ has basis $\{x_ix_j\}_{i\le j}$, so $\dim(\Lambda V)^4=6$, while $\dim H^4(M)=1$.

**Stage 2.** The kernel of $(\Lambda V)^4\to H^4(M)$ is $5$-dimensional, spanned by
$$x_1x_2,\quad x_1x_3,\quad x_2x_3,\quad x_1^2-x_2^2,\quad x_2^2-x_3^2 .$$
Each class must be killed, so $V^3$ has dimension exactly $5$: generators $y_1,\dots,y_5$ with
$$dy_1=x_1x_2,\; dy_2=x_1x_3,\; dy_3=x_2x_3,\; dy_4=x_1^2-x_2^2,\; dy_5=x_2^2-x_3^2 .$$
Hence $\dim\big(\pi_3(M)\otimes\mathbb{Q}\big)=5$.

**Contradiction with ellipticity.** For an elliptic space of formal dimension $n$, $\dim\pi_{\mathrm{odd}}\otimes\mathbb{Q}\le n$ (Félix–Halperin–Thomas, Thm. 32.6 package). Here $n=4$ but already $\dim\pi_3\otimes\mathbb{Q}=5>4$. So $M$ is hyperbolic; equivalently, the numerical identity $n=\sum\deg y_j-\sum(\deg x_i-1)$ would force $4=15-3=12$ at this stage, and later generators cannot repair it. Consistently, $\dim(\pi_i(M)\otimes\mathbb{Q})$ grows exponentially.

**Why Gromov's theorem does not settle it.** $\sum_i b_i(M)=1+3+1=5\le 2^4=16$, so even the conjecturally sharp Betti bound is satisfied. The obstruction, if any, lives entirely in the higher rational homotopy — precisely the gap of Section 6.

**Contrast.** For $b_2\le2$ the same computation closes up: for $S^2\times S^2$ the model is $(\Lambda(x_1,x_2,y_1,y_2),\,dy_i=x_i^2)$, with $\dim\pi_*\otimes\mathbb{Q}=4$ and $n=(3+3)-(1+1)=4$ — elliptic, and indeed $S^2\times S^2$ carries the product metric of $\sec\ge0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*