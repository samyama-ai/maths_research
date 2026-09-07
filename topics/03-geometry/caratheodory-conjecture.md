---
id: 03-geometry/caratheodory-conjecture
title: "Caratheodory Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Carathéodory Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/caratheodory-conjecture` · **Status:** partially-solved (open in the smooth category)

## 1. Problem Statement / Conjecture

**Conjecture (Carathéodory).** Every closed, convex surface in $\mathbb{R}^3$ of class $C^\infty$ (equivalently, the boundary of a smooth compact convex body with positive Gauss curvature) carries at least two **umbilic points** — points where the two principal curvatures coincide.

The conjecture is standardly attacked through a strictly local statement that implies it:

**Conjecture (local index bound; "Loewner–Carathéodory index conjecture").** Let $S \subset \mathbb{R}^3$ be a $C^\infty$ surface and let $p \in S$ be an *isolated* umbilic point. Then the index of either principal line field at $p$ satisfies
$$\operatorname{ind}_p \le 1 .$$

A complete proof must establish the index bound (or the global existence statement directly) for all smooth surfaces; a disproof must exhibit a smooth convex surface with exactly one umbilic, necessarily of index $2$. The real-analytic case is settled (Section 4); the $C^\infty$ case is open, with a long-standing claimed proof in the $C^{3,\alpha}$ category not yet accepted as verified (Section 7).

## 2. Mathematical Foundations

Let $S$ be an oriented surface with immersion $X: S \to \mathbb{R}^3$, unit normal $\nu$, first fundamental form $\mathrm{I}$ and second fundamental form $\mathrm{II}$. The shape operator $A = -d\nu$ has eigenvalues $\kappa_1 \ge \kappa_2$ (principal curvatures), with
$$H = \tfrac{1}{2}(\kappa_1+\kappa_2), \qquad K = \kappa_1\kappa_2 .$$
A point is **umbilic** iff $\kappa_1 = \kappa_2$, i.e. $A = H\,\mathrm{Id}$, i.e. $H^2 - K = 0$.

**Isothermal coordinates and the Hopf differential.** Choose a local conformal coordinate $z = x+iy$, so $\mathrm{I} = e^{2u}|dz|^2$. Writing $\mathrm{II} = L\,dx^2 + 2M\,dx\,dy + N\,dy^2$, set
$$Q \;=\; \tfrac{1}{2}\big(L-N\big) - i M, \qquad \mathcal{Q} = Q\,dz^2 ,$$
the **Hopf differential**. Then
$$\kappa_1 - \kappa_2 \;=\; 2 e^{-2u}\,|Q| ,$$
so umbilics are exactly the zeros of $Q$, and $\mathcal{Q}$ is a well-defined quadratic differential independent of the conformal chart.

**Principal foliations.** Away from umbilics the principal directions are the two line fields defined by
$$\operatorname{Im}\big(Q\,dz^2\big) = 0 .$$
At an isolated zero $p$ of $Q$ the index of this line field is
$$\operatorname{ind}_p \;=\; -\tfrac{1}{2}\,\deg\!\Big(\frac{Q}{|Q|}\Big|_{\partial B_\varepsilon(p)}\Big) \;\in\; \tfrac{1}{2}\mathbb{Z},$$
where $\deg$ is the winding number on a small positively oriented circle. The index bound $\operatorname{ind}_p\le 1$ is therefore the statement $\deg(Q/|Q|) \ge -2$.

**Codazzi equation.** In the conformal coordinate the Mainardi–Codazzi equations reduce to
$$\frac{\partial Q}{\partial \bar z} \;=\; e^{2u}\,\frac{\partial H}{\partial z} .$$
Thus $Q$ is *quasi-holomorphic*: it satisfies a $\bar\partial$-equation whose right-hand side is unconstrained in general. If $H$ is constant, $Q$ is holomorphic (Hopf), and a holomorphic zero of order $n\ge1$ has $\deg = n$, hence $\operatorname{ind}_p = -n/2 < 0$.

**Poincaré–Hopf.** On a closed convex surface $S \cong S^2$, if all umbilics are isolated,
$$\sum_{p \,\text{umbilic}} \operatorname{ind}_p = \chi(S^2) = 2 .$$
Hence a single umbilic would force index $2$, and the local bound $\operatorname{ind}_p\le1$ immediately yields $\ge 2$ umbilics. (A non-isolated umbilic set on a convex surface also forces the conclusion by a separate compactness argument.)

**Loewner's reduction.** For a graph $z = h(x,y)$ at a critical point, $Q$ agrees to leading order with $2\,\partial_z^2 h$, since $\partial_z^2 h = \tfrac14(h_{xx}-h_{yy}-2ih_{xy})$. Loewner conjectured more generally that for real $C^\infty$ $h$, an isolated zero of $\partial_z^{\,n} h$ has index at most $n$; the case $n=2$ implies Carathéodory.

## 3. History & State of the Art (SOTA)

- **1920s.** Carathéodory stated the conjecture in conversation and lectures in Berlin/Munich; it was disseminated in print by Blaschke (*Vorlesungen über Differentialgeometrie III*, Springer, 1929) and by Cohn-Vossen. Carathéodory never published it himself.
- **1940–41.** Hans Hamburger published a three-part proof of the index bound for **real-analytic** surfaces (*Annals of Mathematics* 1940; *Acta Mathematica* 1941), running to several hundred pages and based on a delicate resolution of the singularity of the principal foliation.
- **1943–44.** Gerrit Bol gave a shorter analytic argument (*Math. Z.*); **1959.** Tilla Klotz (Milnor) revised and corrected it (*Comm. Pure Appl. Math.*), but Titus later found a gap in the Bol–Klotz line.
- **1973.** Charles Titus (*Acta Math.*) gave a topological proof of the analytic case (reducing to a combinatorial statement about curves), also viewed as incomplete by some referees.
- **1993 / 2002.** Independent, self-contained proofs of the analytic case: H. Scherbel's ETH Zürich dissertation (a modern rewrite of Hamburger) and V. V. Ivanov's long paper in *Siberian Mathematical Journal*, which reconstructs and repairs Hamburger's argument in full.
- **1992–98.** Smyth and Xavier introduced PDE and index-theoretic methods, proving the bound under explicit curvature hypotheses and reducing the general case to a solvability question for $\partial_z^2\omega = \rho g$.
- **2008–present.** Guilfoyle and Klingenberg announced a proof for $C^{3,\alpha}$ surfaces using holomorphic discs with boundary in the space of oriented lines $\mathbb{L}(\mathbb{R}^3) \cong TS^2$, equipped with a neutral Kähler structure. The related **Toponogov conjecture** (a complete convex surface with bounded Gauss curvature contains an umbilic or umbilic-like point at infinity) was addressed by the same machinery.

**SOTA summary:** proved for real-analytic surfaces; open for $C^\infty$; a claimed but not community-verified proof exists in $C^{3,\alpha}$.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| Real-analytic surfaces | Index bound $\operatorname{ind}_p \le 1$ proved (Hamburger 1940–41; Scherbel 1993; Ivanov 2002). Hence $\ge 2$ umbilics on analytic ovaloids. |
| Constant mean curvature | $Q$ holomorphic $\Rightarrow$ $\operatorname{ind}_p = -n/2 \le -1/2$; Hopf's theorem gives that a CMC sphere is round (all points umbilic). |
| Finite-type umbilics | If $Q$ vanishes to finite order with nondegenerate leading homogeneous part, the winding is computable and $\operatorname{ind}_p \le 1$. |
| Generic surfaces | For an open dense set of $C^r$ immersions ($r\ge4$), all umbilics are *Darbouxian* ($D_1, D_2, D_3$) with index $\pm\tfrac12$; the conjecture then holds with $\ge 4$ umbilics (Gutierrez–Sotomayor). |
| Explicit ovaloids | Triaxial ellipsoids: exactly $4$ umbilics of index $\tfrac12$ each. Surfaces of revolution: the two poles are umbilic. |
| Curvature-condition classes | Smyth–Xavier (1992) proved the sharp bound $\operatorname{ind}_p \le 1$ for smooth surfaces satisfying an explicit third-order/curvature-sign condition at the umbilic. |
| Open convex surfaces | Fontenele–Xavier (2014) established existence of umbilics on classes of complete open convex surfaces. |
| $C^{3,\alpha}$ convex surfaces | Claimed by Guilfoyle–Klingenberg via holomorphic disc theory *(frontier — verify)*. |

## 5. Principal Obstacles

- **The $\bar\partial$-equation is unconstrained.** Codazzi gives only $\partial_{\bar z} Q = e^{2u}\partial_z H$. Since $H$ is arbitrary for a general smooth surface, $Q$ is merely a solution of $\partial_{\bar z}Q = f$ with $f$ smooth — a class far too large to control winding numbers. Holomorphicity, the one mechanism that forces negative index, is destroyed.
- **Infinite-order degeneracy.** A $C^\infty$ function can vanish to infinite order (e.g. $e^{-1/|z|^2}$-type factors). All finite-jet/resolution methods — Hamburger's blow-up of the foliation singularity, Newton-polygon arguments, formal power series — need a nonzero leading term. Real-analyticity supplies it; smoothness does not. **This is the single decisive gap.**
- **Non-genericity of the counterexample.** The conjecture only fails on a set of infinite codimension in the space of immersions, so transversality/genericity arguments (Gutierrez–Sotomayor) cannot reach it; they prove the conjecture off a nowhere-dense set that is exactly where the difficulty lives.
- **No variational or curvature-flow formulation.** The umbilic set is not the critical set of a natural functional, and $H^2 - K \ge 0$ has no maximum-principle structure that forces multiple zeros.
- **Failure of naive index theory.** Poincaré–Hopf gives the total index $2$ but says nothing about individual indices; there is no known cohomological obstruction to a single index-$2$ zero of a general line field on $S^2$ — indeed such line fields exist; the constraint must come from the surface's integrability (Gauss–Codazzi), not topology alone.
- **Verification burden.** The successful proofs (Hamburger, Ivanov) run to hundreds of pages, making independent checking and generalization extremely costly; the same difficulty attaches to the current $C^{3,\alpha}$ claim.

## 6. The Gap

Proved: for real-analytic $S$, every isolated umbilic has $\operatorname{ind}_p \le 1$. General statement: same bound for $C^\infty$ $S$.

The precise barrier is the passage from *finite-order* to *flat* vanishing of the Hopf differential. All analytic proofs write $Q(z) = c\,z^{k}\bar z^{\,\ell}(1+o(1))$ or similar, resolve the foliation singularity by finitely many blow-ups, and read off the winding number from the leading homogeneous part. For $C^\infty$ surfaces the Taylor expansion of $Q$ at $p$ may vanish identically while $Q\not\equiv0$, so no leading part exists, the blow-up terminates without a normal form, and the winding number is not determined by any jet. Crossing the gap requires either (i) an argument that a flat umbilic with index $>1$ is incompatible with $\partial_{\bar z} Q = e^{2u}\partial_z H$ plus $K>0$, or (ii) a global method that never localizes — the route taken by the holomorphic-disc programme.

## 7. Current Research (as of June 2026)

- **Neutral Kähler / holomorphic disc programme (Guilfoyle, Klingenberg; Univ. of Limerick, Univ. Duisburg-Essen).** The space of oriented lines $\mathbb{L}(\mathbb{R}^3)\cong TS^2$ carries a neutral Kähler metric; a surface's normal congruence is a Lagrangian surface, and an umbilic corresponds to a complex point. A hypothetical index-$2$ umbilic is ruled out by constructing a family of holomorphic discs with boundary on the Lagrangian and applying Fredholm index / Riemann–Hilbert boundary-value theory. Claimed to prove the conjecture for $C^{3,\alpha}$ surfaces *(frontier — verify: the central preprint, arXiv:0808.0851, has circulated since 2008 with supporting papers on Fredholm regularity of holomorphic discs published in refereed venues, but the main claim is not yet regarded as fully verified by the community).*
- **PDE/solvability route (Xavier and collaborators).** Pushing the Smyth–Xavier reduction: understand which right-hand sides $g$ admit real solutions of $\partial_z^2\omega = \rho g$, which converts the index bound into a linear-analysis question.
- **Dynamical-systems school (Brazilian tradition: Sotomayor, Garcia, Mello).** Classification and bifurcation of umbilic points, umbilics on algebraic surfaces and on surfaces in $\mathbb{R}^4$, and quantitative counts for explicit families.
- **Computer-assisted search.** Numerical exploration of candidate single-umbilic convex surfaces; no counterexample has ever been produced, consistent with the infinite-codimension obstruction.
- **Related conjectures.** Toponogov's conjecture for complete convex surfaces; the higher $n$ cases of Loewner's conjecture on $\partial_z^n h$, all open.

## 8. Future Work

1. **Independent verification of the $C^{3,\alpha}$ claim.** A refereed, community-checked account of the holomorphic-disc argument would settle the smooth case, since $C^\infty \subset C^{3,\alpha}$.
2. **A short proof of the analytic case.** Ivanov and Scherbel are long; a conceptual proof would likely expose the mechanism that could be transplanted to $C^\infty$.
3. **Flat-umbilic rigidity.** Prove directly that a smooth surface whose Hopf differential is flat at $p$ but not identically zero cannot have $\deg(Q/|Q|) \le -3$; this is the minimal missing lemma.
4. **Loewner for general $n$.** Even $n=3$ is open and would test whether the analytic techniques are $n$-specific.
5. **Global-to-local transfer.** Formalize when a global convexity hypothesis ($K>0$ on a sphere) forbids a local index excess, bypassing jets entirely.
6. **Extensions.** Umbilics of surfaces in space forms, in $\mathbb{R}^4$, and for Finsler/affine analogues.

## 9. Key References

- **[Foundational]** W. Blaschke. *Vorlesungen über Differentialgeometrie III: Differentialgeometrie der Kreise und Kugeln.* Springer, Berlin, 1929. (First printed record of the conjecture.)
- **[Foundational]** H. Hamburger. *Beweis einer Carathéodoryschen Vermutung, Teil I.* Annals of Mathematics **41** (1940), 63–86; *Teil II, III.* Acta Mathematica **73** (1941), 175–228 and 229–332.
- **[Foundational]** G. Bol. *Über Nabelpunkte auf einer Eifläche.* Mathematische Zeitschrift **49** (1943/44), 389–410.
- **[Historical]** T. Klotz. *On G. Bol's proof of Carathéodory's conjecture.* Communications on Pure and Applied Mathematics **12** (1959), 277–311.
- **[Historical]** C. J. Titus. *A proof of a conjecture of Loewner and of the conjecture of Carathéodory on umbilic points.* Acta Mathematica **131** (1973), 43–77.
- **[SOTA]** V. V. Ivanov. *The analytic Carathéodory conjecture.* Siberian Mathematical Journal **43** (2002), no. 2, 251–322.
- **[SOTA]** H. Scherbel. *A new proof of Hamburger's index theorem on umbilical points.* Dissertation No. 10281, ETH Zürich, 1993.
- **[SOTA]** B. Smyth, F. Xavier. *A sharp geometric estimate for the index of an umbilic on a smooth surface.* Bulletin of the London Mathematical Society **24** (1992), 176–180.
- **[SOTA]** B. Smyth, F. Xavier. *Real solvability of the equation $\partial_{\bar z}^2\omega = \rho g$ and the topology of isolated umbilics.* Journal of Geometric Analysis **8** (1998), 655–671.
- **[Recent]** F. Fontenele, F. Xavier. *Finding umbilics on open convex surfaces.* Revista Matemática Iberoamericana **30** (2014), 553–556.
- **[Frontier]** B. Guilfoyle, W. Klingenberg. *Proof of the Carathéodory conjecture.* Preprint, arXiv:0808.0851 (2008, revised subsequently). *(frontier — verify)*
- **[Survey]** C. Gutierrez, J. Sotomayor. *Lines of curvature and umbilical points on surfaces.* 18º Colóquio Brasileiro de Matemática, IMPA, Rio de Janeiro, 1991 (reprinted 1998).
- **[Survey]** M. Berger. *A Panoramic View of Riemannian Geometry.* Springer, 2003. (§ on umbilics and the Carathéodory conjecture.)

## 10. Worked Example / Concrete Special Case

**(a) The triaxial ellipsoid: index $\tfrac12$, four umbilics.** Let
$$E: \quad \frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1, \qquad a>b>c>0 .$$
The umbilics lie in the plane $y=0$ and are the four points
$$\Big(\pm a\sqrt{\tfrac{a^2-b^2}{a^2-c^2}},\;0,\;\pm c\sqrt{\tfrac{b^2-c^2}{a^2-c^2}}\Big).$$
Each is a *lemon*-type (Darbouxian $D_1$) umbilic of index $+\tfrac12$, and
$$4 \times \tfrac12 = 2 = \chi(S^2),$$
confirming Poincaré–Hopf. Degenerating $b \to a$ merges the four points into the two poles of a spheroid, each of index $+1$: two umbilics, total index $2$. So the conjectural minimum of two umbilics is attained.

**(b) Sharpness of the index bound.** Take the rotationally symmetric graph
$$h(x,y) = \tfrac12 r^4, \qquad r=\sqrt{x^2+y^2}.$$
Its principal curvatures are
$$\kappa_{\text{merid}} = \frac{h''}{(1+h'^2)^{3/2}} = \frac{6r^2}{(1+4r^6)^{3/2}}, \qquad
\kappa_{\text{par}} = \frac{h'}{r(1+h'^2)^{1/2}} = \frac{2r^2}{(1+4r^6)^{1/2}} .$$
They agree only at $r=0$, so the origin is an *isolated* umbilic. Its Hopf differential is, to leading order, $Q \sim 2\,\partial_z^2 h = 2\,\partial_z^2\big(\tfrac12 z^2\bar z^2\big) = 2\bar z^{\,2}$, whose winding on $|z|=\varepsilon$ is $-2$; hence
$$\operatorname{ind}_0 = -\tfrac12(-2) = 1 .$$
The principal foliation is the radial/circular net. This shows the bound $\operatorname{ind}\le1$ is **sharp**.

**(c) A negative-index umbilic.** For $h(x,y) = \operatorname{Re}(z^3) = x^3-3xy^2$ one gets $Q \sim 2\,\partial_z^2 h = 6z$, winding $+1$, so $\operatorname{ind}_0 = -\tfrac12$: the *monkey-saddle* (star, $D_3$) umbilic with three separatrices.

**(d) What a counterexample must look like.** By (b) and Poincaré–Hopf, a convex surface with a *single* umbilic requires $\operatorname{ind}_p = 2$, i.e. $\deg(Q/|Q|) = -4$, so $Q$ would have to behave like $\bar z^{\,4}$ to leading order. But $\bar z^{\,4} = \partial_z^2\big(\tfrac{1}{6}z^2\bar z^{\,4}\big)$ and $z^2\bar z^{\,4}$ is *not real*; no real $h$ has $\partial_z^2 h$ with a nondegenerate $\bar z^4$ leading term. For real-analytic surfaces this obstruction can be pushed through all orders — that is Hamburger's theorem. For $C^\infty$ surfaces the leading term may not exist at all, and the argument stalls: precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*