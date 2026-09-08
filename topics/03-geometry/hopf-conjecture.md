---
id: 03-geometry/hopf-conjecture
title: "Hopf Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hopf Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/hopf-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Heinz Hopf posed two linked questions about how positive sectional curvature constrains topology. Both are open.

**Conjecture A (Euler characteristic).** Let $(M^{2n}, g)$ be a closed, connected, orientable Riemannian manifold of even dimension $2n$ with positive sectional curvature, $\sec > 0$. Then
$$\chi(M^{2n}) > 0 .$$
The companion statement for nonpositive curvature (usually attributed to Chern, and also on Hopf's list): if $\sec \le 0$ then $(-1)^n \chi(M^{2n}) \ge 0$.

**Conjecture B (product of spheres).** The manifold $S^2 \times S^2$ admits no Riemannian metric with $\sec > 0$.

Conjecture B is the smallest unresolved instance of a broader principle: no product of closed manifolds of positive dimension carries positive sectional curvature. Note that B is *not* a consequence of A — $\chi(S^2\times S^2)=4>0$ — so B needs an obstruction beyond Euler characteristic.

A resolution of A means either a proof valid in all even dimensions, or a closed even-dimensional manifold with $\sec>0$ and $\chi \le 0$. A resolution of B means either a metric on $S^2\times S^2$ with $\sec>0$ exhibited explicitly, or a proof that none exists.

## 2. Mathematical Foundations

Let $(M,g)$ be Riemannian with Levi-Civita connection $\nabla$ and curvature tensor
$$R(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z .$$
For a $2$-plane $\sigma = \mathrm{span}\{X,Y\} \subset T_pM$, the **sectional curvature** is
$$\sec(\sigma) = \frac{\langle R(X,Y)Y, X\rangle}{\|X\|^2\|Y\|^2 - \langle X,Y\rangle^2}.$$
$\sec>0$ means this is positive for every plane at every point.

**Gauss–Bonnet–Chern** (Chern, 1944/1955): for closed oriented $M^{2n}$,
$$\chi(M) = \int_M \mathrm{Pf}(\Omega), \qquad \mathrm{Pf}(\Omega) = \frac{1}{(2\pi)^n\, 2^n n!}\sum_{\sigma,\tau \in S_{2n}} \mathrm{sgn}(\sigma)\,\mathrm{sgn}(\tau)\, R_{\sigma(1)\sigma(2)\tau(1)\tau(2)}\cdots R_{\sigma(2n-1)\sigma(2n)\tau(2n-1)\tau(2n)} .$$
Hopf's Conjecture A would follow at once from the **algebraic Hopf conjecture**: that $\sec>0$ at a point forces $\mathrm{Pf}(\Omega)>0$ at that point. In dimension $4$ the Gauss–Bonnet integrand can be written
$$\chi(M^4) = \frac{1}{8\pi^2}\int_M \Big( |W|^2 + \frac{\mathrm{scal}^2}{24} - \frac{|\mathrm{Ric}_0|^2}{2}\Big)\, dV,$$
with $W$ the Weyl tensor and $\mathrm{Ric}_0$ the trace-free Ricci tensor.

**Reference results used throughout.** Bonnet–Myers: $\mathrm{Ric}\ge (n-1)k>0$ implies $\mathrm{diam}\le \pi/\sqrt{k}$ and $\pi_1$ finite. Synge: closed orientable even-dimensional $M$ with $\sec>0$ is simply connected. Frankel (1961): in $M^n$ with $\sec>0$, two closed totally geodesic submanifolds of dimensions $p,q$ with $p+q\ge n$ must intersect. Weinstein (1967): an isometry of an oriented $M^n$ with $\sec>0$ preserving (resp. reversing) orientation has a fixed point if $n$ is even (resp. odd). Berger (1961): for closed even-dimensional $M$ with $\sec>0$, every isometry of finite order... more usefully, every Killing field vanishes somewhere. The **symmetry rank** of $M$ is $\mathrm{symrank}(M)=\mathrm{rank}\,\mathrm{Isom}(M,g)$, i.e. the dimension of a maximal torus acting effectively by isometries.

Known closed simply connected manifolds with $\sec>0$: rank-one symmetric spaces $S^n, \mathbb{CP}^n, \mathbb{HP}^n, \mathbb{OP}^2$; the Berger spaces $B^7, B^{13}$; the Wallach flag manifolds $W^6, W^{12}, W^{24}$; the Aloff–Wallach $W^7_{k,l}$; the Eschenburg and Bazaikin families. All have $\chi>0$ in even dimensions, and none is a product.

## 3. History & State of the Art (SOTA)

- **1926–1932.** Hopf's work on the *Curvatura integra* and on space forms puts the relation "curvature sign $\to$ Euler characteristic sign" on the table; the conjecture circulates in his lectures and problem lists.
- **1940s–50s.** Chern's intrinsic proof of Gauss–Bonnet gives the Pfaffian formulation. Milnor proves the algebraic version in dimension $4$: $\sec>0$ (indeed $\sec$ of one sign) implies positive integrand, so $\chi(M^4)>0$. Chern (1955) records the problem and settles the case $2n=4$ this way.
- **1960s.** Berger, Klingenberg, Rauch develop pinching; Berger proves the vanishing of Killing fields; Weinstein's fixed-point theorem appears (1967). Bott, Milnor, and others fail to extend the algebraic route.
- **1976.** Geroch shows the algebraic Hopf conjecture is **false** for $2n\ge 6$: there exist algebraic curvature tensors with all sectional curvatures positive and negative Pfaffian. Klembeck sharpens this, showing the counterexamples are not isolated.
- **1981.** Gromov's Betti number theorem: for $\sec \ge 0$, $\sum_i b_i(M^n;F) \le C(n)$. This bounds $|\chi|$ but does not sign it.
- **1989–2013.** The **Grove symmetry program** — study $\sec>0$ under isometric group actions — becomes the dominant approach. Hsiang–Kleiner (1989), Grove–Searle (1994), Püttmann–Searle (2002), Rong–Su (2005), Kennard (2013) prove Conjecture A under successively weaker torus-symmetry hypotheses.
- **2014.** Bettiol constructs metrics on $S^2\times S^2$ with positive *biorthogonal* curvature (the average $\sec(\sigma)+\sec(\sigma^\perp)>0$), showing how close one can get to $\sec>0$ on the very manifold in Conjecture B.

## 4. Partial Results / Verified Cases

- **Dimension 4:** proven unconditionally. $\sec>0$ (or $\sec<0$, via $(-1)^n$) makes the Gauss–Bonnet integrand pointwise positive (Milnor; Chern 1955). Also $\chi(M^4)\ge 2$ by Synge + Poincaré duality.
- **Dimension 2:** trivial — $\sec>0$ forces $M=S^2$, $\chi=2$.
- **Homogeneous and cohomogeneity $\le 1$:** true. If $\sec>0$ and $G$ acts transitively, then $\mathrm{rank}\,G = \mathrm{rank}\,H$ for the isotropy group $H$ (Hopf–Samelson / Bott–Samelson), giving $\chi>0$. Püttmann–Searle (2002) extend to cohomogeneity $\le 4$ in low dimensions and to $\mathrm{symrank} \ge \lfloor 2n/4\rfloor$... precisely: $\chi>0$ for $M^{2n}$ with $\sec>0$ and $\mathrm{symrank} \ge 2n/4 - 1$ (for $2n\ge 10$).
- **Torus symmetry:** Rong–Su (2005) prove $\chi>0$ when $\mathrm{symrank}\ge 2n/6$ for $2n \equiv 0 \bmod 4$. Kennard (2013) proves $\chi>0$ for $M^{2n}$ with $\sec>0$ admitting an effective isometric $T^r$-action with $r \ge 2\log_2 (2n)$ — a logarithmic, hence asymptotically optimal-order, symmetry bound.
- **Hsiang–Kleiner (1989):** a closed simply connected $M^4$ with $\sec>0$ and an isometric $S^1$-action is homeomorphic to $S^4$ or $\mathbb{CP}^2$. This is a strong dimension-$4$ instance of the philosophy behind Conjecture B (in particular $S^2\times S^2$ admits no $\sec>0$ metric *with* $S^1$-symmetry).
- **Rational ellipticity:** Amann–Kennard (2015) show that if the Bott conjecture holds ($\sec\ge0$ $\Rightarrow$ rationally elliptic), then $\chi(M^{2n})>0$ follows for $\sec>0$; they also prove $\chi>0$ for rationally elliptic $M$ with $\sec>0$ and mild symmetry.
- **Nonpositive curvature side:** the Chern conjecture $(-1)^n\chi\ge0$ is known for $2n=4$, for Kähler manifolds, for locally symmetric spaces (Hirzebruch proportionality), and for manifolds admitting a flat affine or projective structure only in restricted settings; the general affine-flat case (Chern's other conjecture, $\chi=0$) was resolved by Klingler (2017).

## 5. Principal Obstacles

- **The pointwise route is dead.** Geroch's counterexamples (1976) mean no purely algebraic implication "$\sec>0$ at $p$ $\Rightarrow$ $\mathrm{Pf}(\Omega)_p>0$" exists for $2n\ge6$. Any proof must be global: the negative Pfaffian must be shown to be impossible to spread over a closed manifold, i.e. one needs to exploit the second Bianchi identity and integrability, which the algebraic counterexamples ignore.
- **Bochner/Weitzenböck techniques control Ricci, not $\sec$.** Vanishing theorems bound Betti numbers under curvature *operator* or Ricci hypotheses; positive sectional curvature is a condition on $2$-planes only and does not yield a sign for the relevant curvature terms in $\Delta = \nabla^*\nabla + \mathcal{R}$.
- **Sec>0 vs sec≥0 is invisible to every known invariant.** No closed simply connected manifold is currently known to admit $\sec\ge0$ but not $\sec>0$. Every topological obstruction proved for $\sec>0$ (Gromov Betti bounds, Synge, Cheeger–Gromoll splitting) already holds for $\sec\ge0$ — and $S^2\times S^2$ has $\sec\ge0$. So Conjecture B cannot be attacked by any invariant insensitive to the strict inequality.
- **Comparison geometry saturates.** Toponogov and critical-point theory give diameter/injectivity control and hence sphere theorems under pinching $\delta > 1/4$, but positive curvature without pinching gives essentially no quantitative handle.
- **Symmetry is a hypothesis, not a theorem.** All the strong results in §4 assume a torus action. Generic metrics have trivial isometry group, and there is no mechanism to produce symmetry from curvature.

## 6. The Gap

For Conjecture A the gap is quantitative and precise: results are known for $M^{2n}$ with $\sec>0$ *and* symmetry rank $r \gtrsim 2\log_2(2n)$ (Kennard). The general conjecture is the case $r=0$. Closing it requires either (i) a global replacement for the failed algebraic Hopf conjecture — a proof that $\int_M \mathrm{Pf}(\Omega)>0$ using the Bianchi identities and closedness, not pointwise positivity; or (ii) a proof of the Bott conjecture ($\sec\ge0 \Rightarrow$ rational ellipticity), which by Amann–Kennard implies A.

For Conjecture B the gap is starker: **zero** unconditional obstruction is known. Every candidate invariant of $S^2\times S^2$ is compatible with $\sec>0$. The barrier is to find any invariant at all that separates $\sec>0$ from $\sec\ge0$ on a fixed simply connected $4$-manifold. Bettiol's positive-biorthogonal metrics show the natural weakenings of the hypothesis do not obstruct.

## 7. Current Research (as of June 2026)

- **Grove symmetry program.** Groups around Karsten Grove (Notre Dame), Burkhard Wilking (Münster), Lee Kennard (Syracuse), Catherine Searle (Wichita State), Michael Wiemeler (Münster). Kennard–Wiemeler–Wilking's representation-theoretic splitting techniques for torus actions push the required symmetry rank down and yield classification of positively curved manifolds with large torus symmetry *(frontier — verify)*.
- **Rational homotopy / Bott conjecture.** Amann, Kennard, and collaborators continue to link elliptic rational homotopy type to $\chi>0$; progress is on manifolds with additional symmetry or small dimension.
- **Curvature-operator conditions.** Böhm–Wilking-style Ricci flow arguments have settled classification under positive curvature *operator* and, more recently, under weaker "$k$-positive curvature operator" conditions; extending Ricci flow to preserve $\sec>0$ is known to be impossible in general (Böhm–Wilking gave examples where $\sec>0$ is not preserved), which limits this route.
- **Intermediate curvature notions.** Positive biorthogonal curvature, positive $m$-intermediate Ricci ($\mathrm{Ric}_m>0$), and $k$-positivity are being used to isolate exactly which weakening of $\sec>0$ admits products — Bettiol's $S^2\times S^2$ example is the reference point.
- **Computer-assisted / algebraic searches** for curvature tensors with $\sec>0$ and controlled Pfaffian, aimed at understanding how far Geroch-type examples can satisfy the second Bianchi identity *(frontier — verify)*.

## 8. Future Work

- Determine whether Geroch-type algebraic counterexamples can be realized by *integrable* curvature tensors, i.e. as $R_p$ of an actual metric on a neighbourhood with $\sec>0$ everywhere. A negative answer in some dimension would revive a local route.
- Prove the Bott conjecture in dimension $6$ or $8$; by Amann–Kennard this yields new cases of Conjecture A.
- Reduce Kennard's $r\ge 2\log_2(2n)$ symmetry bound to a constant, or to $r\ge 2$, which would be a decisive structural advance.
- Find an obstruction to $\sec>0$ that vanishes for $\sec\ge0$ — Wilking has repeatedly identified this as the central missing idea for Conjecture B.
- Study the moduli space of nonnegatively curved metrics on $S^2\times S^2$ and whether the positively curved locus can be shown to be empty by a degeneration/compactness argument.

## 9. Key References

- **[Foundational]** H. Hopf. *Über die Curvatura integra geschlossener Hyperflächen.* Mathematische Annalen **95** (1926), 340–367. [DOI](https://doi.org/10.1007/bf01206615)
- **[Foundational]** S.-S. Chern. *On curvature and characteristic classes of a Riemannian manifold.* Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **20** (1955), 117–126.
- **[Foundational]** T. Frankel. *Manifolds with positive curvature.* Pacific Journal of Mathematics **11** (1961), 165–174.
- **[Foundational]** A. Weinstein. *On the homotopy type of positively-pinched manifolds.* Archiv der Mathematik **18** (1967), 523–524. [DOI](https://doi.org/10.1007/bf01899493)
- **[Counterexample]** R. Geroch. *Positive sectional curvatures does not imply positive Gauss–Bonnet integrand.* Proceedings of the American Mathematical Society **54** (1976), 267–270. [DOI](https://doi.org/10.1090/s0002-9939-1976-0390961-8)
- **[Counterexample]** P. F. Klembeck. *On Geroch's counterexample to the algebraic Hopf conjecture.* Proceedings of the American Mathematical Society **59** (1976), 334–336. [DOI](https://doi.org/10.2307/2041496)
- **[Foundational]** M. Gromov. *Curvature, diameter and Betti numbers.* Commentarii Mathematici Helvetici **56** (1981), 179–195. [DOI](https://doi.org/10.1007/bf02566208)
- **[Partial]** W.-Y. Hsiang, B. Kleiner. *On the topology of positively curved 4-manifolds with symmetry.* Journal of Differential Geometry **29** (1989), 615–621. [DOI](https://doi.org/10.4310/jdg/1214443064)
- **[Partial]** K. Grove, C. Searle. *Positively curved manifolds with maximal symmetry-rank.* Journal of Pure and Applied Algebra **91** (1994), 137–142. [DOI](https://doi.org/10.1016/0022-4049(94)90138-4)
- **[Partial]** T. Püttmann, C. Searle. *The Hopf conjecture for manifolds with low cohomogeneity or high symmetry rank.* Proceedings of the American Mathematical Society **130** (2002), 163–166. [DOI](https://doi.org/10.1090/s0002-9939-01-06039-7)
- **[Partial]** X. Rong, X. Su. *The Hopf conjecture for manifolds with abelian group actions.* Communications in Contemporary Mathematics **7** (2005), 121–136. [DOI](https://doi.org/10.1142/s0219199705001660)
- **[SOTA]** L. Kennard. *On the Hopf conjecture with symmetry.* Geometry & Topology **17** (2013), 563–593. [DOI](https://doi.org/10.2140/gt.2013.17.563)
- **[SOTA]** M. Amann, L. Kennard. *Positive curvature and rational ellipticity.* Algebraic & Geometric Topology **15** (2015), 2269–2301. [DOI](https://doi.org/10.2140/agt.2015.15.2269)
- **[SOTA]** R. G. Bettiol. *Positive biorthogonal curvature on $S^2\times S^2$.* Proceedings of the American Mathematical Society **142** (2014), 4341–4353. [DOI](https://doi.org/10.1090/s0002-9939-2014-12173-3)
- **[Survey]** B. Wilking. *Nonnegatively and positively curved manifolds.* In *Surveys in Differential Geometry, Vol. XI: Metric and Comparison Geometry*, International Press, 2007, 25–62. [DOI](https://doi.org/10.4310/sdg.2006.v11.n1.a3)
- **[Survey]** W. Ziller. *Riemannian manifolds with positive sectional curvature.* In *Geometry of Manifolds with Non-negative Sectional Curvature*, Lecture Notes in Mathematics **2110**, Springer, 2014, 1–19. [DOI](https://doi.org/10.1007/978-3-319-06373-7_1)

## 10. Worked Example / Concrete Special Case

**Dimension 4: why the conjecture is a theorem, and exactly where the argument stops.**

Let $(M^4,g)$ be closed, oriented, $\sec>0$. Fix $p\in M$ and an oriented orthonormal frame $e_1,\dots,e_4$ of $T_pM$. The Gauss–Bonnet–Chern integrand in dimension $4$ reduces to
$$8\pi^2\,\mathrm{Pf}(\Omega) = R_{1212}R_{3434} + R_{1313}R_{2424} + R_{1414}R_{2323} - R_{1234}^2 - R_{1342}^2 - R_{1423}^2 + (\text{mixed terms}),$$
and one may choose the frame so that the curvature operator $\mathcal{R}: \Lambda^2 T_pM \to \Lambda^2 T_pM$ is diagonalized in the basis $e_1\wedge e_2 \pm e_3\wedge e_4$, etc. Writing $A = R_{1212}, B = R_{1313}, C=R_{1414}$ and $A'=R_{3434}, B'=R_{2424}, C'=R_{2323}$, the first Bianchi identity $R_{1234}+R_{1342}+R_{1423}=0$ together with the diagonalizing choice makes the off-diagonal terms vanish, leaving
$$8\pi^2\,\mathrm{Pf}(\Omega) = AA' + BB' + CC' .$$
Each of $A,B,C,A',B',C'$ is a sectional curvature of a $2$-plane, hence $>0$. So $\mathrm{Pf}(\Omega)>0$ pointwise, and integrating,
$$\chi(M^4) = \int_M \mathrm{Pf}(\Omega) \, dV > 0 .$$
This is Milnor's argument. It uses only the **algebraic** structure of $R$ in dimension $4$: the Pfaffian is a sum of *products of pairs of sectional curvatures of complementary planes*.

**Where it fails.** In dimension $6$ the Pfaffian is a degree-$3$ polynomial in the $R_{ijkl}$ and expands into terms of mixed sign that cannot be reorganized into a sum of products of sectional curvatures. Geroch (1976) exhibits an algebraic curvature tensor on $\mathbb{R}^6$ with $\sec(\sigma)>0$ for all $\sigma$ and $\mathrm{Pf}(\Omega)<0$. Concretely, one takes a tensor close to that of a product-like model where three "complementary-pair" products are small and positive while a mixed term $\sim -R_{1234}R_{1256}R_{3456}$ dominates; positivity of all sectional curvatures constrains only the diagonal entries $\langle \mathcal{R}(e_i\wedge e_j), e_i\wedge e_j\rangle$, leaving the off-diagonal entries free enough to flip the sign of the Pfaffian.

**And Conjecture B, concretely.** On $S^2(1)\times S^2(1)$ with the product metric, take $e_1,e_2$ tangent to the first factor and $f_1,f_2$ to the second. Then $\sec(e_1,e_2)=\sec(f_1,f_2)=1$, but for the mixed plane
$$\sec(e_1,f_1) = \frac{\langle R(e_1,f_1)f_1, e_1\rangle}{1} = 0,$$
since $R = R_1 \oplus R_2$ has no mixed components. So $\sec\ge0$ with a $2$-dimensional family of flat planes at every point. Gauss–Bonnet gives $\chi = 2\cdot 2 = 4 > 0$, consistent with Conjecture A. The question of Conjecture B is whether these flat planes can be perturbed away — and Bettiol's metrics show that one *can* make $\sec(\sigma)+\sec(\sigma^\perp)>0$ everywhere on $S^2\times S^2$, i.e. no mixed plane and its orthogonal complement are simultaneously flat. Whether both can be made strictly positive individually is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*