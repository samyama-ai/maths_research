---
id: 04-topology/smooth-schoenflies-problem
title: "Smooth Schoenflies Problem"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Smooth Schoenflies Problem

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/smooth-schoenflies-problem` · **Status:** open

## 1. Problem Statement / Conjecture

**Smooth Schoenflies Conjecture (SSC).** Let $\Sigma \subset S^n$ be a smoothly embedded submanifold diffeomorphic to $S^{n-1}$. Then each of the two closures of the complementary components of $\Sigma$ is diffeomorphic to the closed $n$-ball $D^n$; equivalently, the pair $(S^n,\Sigma)$ is diffeomorphic to the standard pair $(S^n, S^{n-1})$ with $S^{n-1}$ the equator.

The statement is a theorem for every $n \neq 4$. **The open case is $n = 4$:** does every smoothly embedded $3$-sphere $\Sigma^3 \subset S^4$ bound a smooth $4$-ball on both sides?

A complete resolution means either (i) a proof that every such $\Sigma^3$ is smoothly ambiently isotopic to the equatorial $S^3$, or (ii) an explicit $\Sigma^3 \subset S^4$ together with a proof that one complementary piece is not diffeomorphic to $D^4$ — necessarily by a diffeomorphism invariant, since the piece is always *homeomorphic* to $D^4$.

## 2. Mathematical Foundations

Let $\Sigma \subset S^n$ be a smooth embedded $(n-1)$-sphere. Alexander duality with $\mathbb{Z}$ coefficients gives
$$\tilde H_i(S^n \setminus \Sigma;\mathbb{Z}) \;\cong\; \tilde H^{\,n-i-1}(\Sigma;\mathbb{Z}) \;=\; \begin{cases}\mathbb{Z}, & i = 0,\\ 0, & i > 0,\end{cases}$$
so the complement has exactly two components $U_1, U_2$, each with the homology of a point. A smooth embedding is locally flat and has a bicollar $\Sigma \times (-1,1)$, so $W_j := \overline{U_j}$ is a compact smooth $n$-manifold with $\partial W_j \cong S^{n-1}$. For $n \geq 3$, van Kampen applied to $S^n = W_1 \cup_\Sigma W_2$ with $\pi_1(\Sigma) = 1$ forces $\pi_1(W_j) = 1$. Hence each $W_j$ is a **smooth homotopy $n$-ball**:
$$H_*(W_j) = H_*(\text{pt}), \qquad \pi_1(W_j) = 1, \qquad \partial W_j \cong S^{n-1}.$$

SSC$_n$ is therefore equivalent to: *every smooth compact contractible $n$-manifold with boundary $S^{n-1}$ is diffeomorphic to $D^n$.*

**Relation to the smooth Poincaré conjecture.** Capping gives a smooth homotopy sphere $\widehat{W_j} := W_j \cup_{S^{n-1}} D^n$. Conversely, by the Palais–Cerf disc theorem (any two smooth embeddings $D^n \hookrightarrow M^n$ into a connected oriented $M$ are ambiently isotopic up to orientation), if $\widehat{W_j} \cong S^n$ then $W_j$ is the complement of a standardly embedded ball, hence $W_j \cong D^n$. So
$$\mathrm{SPC}_n \;\Longrightarrow\; \mathrm{SSC}_n ,$$
where SPC$_n$ is the smooth $n$-dimensional Poincaré conjecture. In dimension $4$ the converse implication is *not* known: an arbitrary homotopy $4$-sphere is not given with a preferred smoothly embedded $S^3$. Thus SSC$_4$ is a formally weaker — and hence a natural first — target than SPC$_4$.

**Morse-theoretic formulation.** For $\Sigma^{n-1} \subset \mathbb{R}^n$ compact, the height $h = x_n|_\Sigma$ is generically Morse with critical points of indices $i$ and counts $c_i$ satisfying
$$\sum_{i=0}^{n-1} (-1)^i c_i = \chi(S^{n-1}) = \begin{cases} 2, & n \text{ odd},\\ 0, & n \text{ even}.\end{cases}$$
For $n=4$: $c_0 - c_1 + c_2 - c_3 = 0$, and the generic level sets $\Sigma_t = \Sigma \cap \{x_4 = t\}$ are closed orientable surfaces in $\mathbb{R}^3$. Complexity of $\Sigma$ is measured by $\sum_i c_i$ and by the maximal genus of the $\Sigma_t$.

**Necessity of smoothness.** The Alexander horned sphere (Alexander, 1924) is a topologically embedded $S^2 \subset S^3$ whose outside has non-trivial $\pi_1$; so the topological statement requires local flatness, which smooth embeddings supply automatically.

## 3. History & State of the Art (SOTA)

- **1908–1924.** Schoenflies proves the planar case ($n=2$): a Jordan curve in $S^2$ bounds discs. Alexander (1924) proves the polyhedral case in $S^3$ and constructs the horned sphere, showing the naive topological version is false.
- **1959–1960.** Mazur's infinite swindle plus Morse's removal of his extra hypothesis, and independently Brown's proof, give the **generalized topological Schoenflies theorem**: a *bicollared* $S^{n-1} \subset S^n$ bounds topological balls, in all $n$. This settles the topological category completely.
- **1961–1965.** Smale's $h$-cobordism theorem yields SSC$_n$ for $n \geq 6$: a contractible $W^n$ with $\partial W = S^{n-1}$, minus an open ball, is an $h$-cobordism from $S^{n-1}$ to $S^{n-1}$ of dimension $\geq 6$, hence a product.
- **1963–1968.** Kervaire–Milnor's $\Theta_5 = 0$ together with the disc theorem settles $n = 5$; Cerf's $\Gamma_4 = 0$ (i.e. $\pi_0\,\mathrm{Diff}^+(S^3) = 0$) supplies the needed uniqueness of smooth discs and the smoothing statements in low dimensions. Dimension $3$ follows from Alexander plus Munkres–Whitehead smoothing.
- **1982.** Freedman's topological classification gives, for $n=4$, that both complementary pieces are *homeomorphic* to $D^4$ — reinforcing that only smooth invariants can decide the question.
- **1985.** Scharlemann proves SSC$_4$ for $3$-spheres in $\mathbb{R}^4$ with four critical points, the first genuinely $4$-dimensional Morse-theoretic case.
- **2010–2020.** Candidate counterexamples to SPC$_4$ (Cappell–Shaneson spheres, Gluck twists, plumbing/link-surgery constructions) are systematically standardized by Akbulut, Gompf, and others; Freedman–Gompf–Morrison–Walker test the Rasmussen $s$-invariant as a detector and find nothing.
- **2018–2026.** Watanabe disproves the $4$-dimensional Smale conjecture ($\pi_*(\mathrm{Diff}(D^4),\mathrm{rel}\,\partial) \otimes \mathbb{Q} \neq 0$), removing the last hope of a direct Cerf-style parametrized argument in dimension $4$.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| $n = 2, 3$ | Proven (PL and smooth) | Schoenflies; Alexander 1924 |
| $n = 5$ | Proven ($\Theta_5 = 0$ + disc theorem) | Kervaire–Milnor 1963; Cerf 1968 |
| $n \geq 6$ | Proven ($h$-cobordism) | Smale 1961; Milnor 1965 |
| All $n$, topological, bicollared | Proven | Mazur 1959, Morse 1960, Brown 1960 |
| All $n$, PL, locally flat, $n \neq 4$ | Proven | Smale/Cerf machinery |
| $n = 4$, $\Sigma$ homeomorphic conclusion | Proven: both sides $\approx D^4$ topologically | Brown 1960; Freedman 1982 |
| $n = 4$, $\le 4$ critical points of a height function | Proven: $\Sigma$ is standard | Scharlemann 1985 |
| $n = 4$, all level sets of genus $\le 1$ after isotopy | Proven (contained in Scharlemann's argument) | Scharlemann 1985 |
| $n = 4$, $\Sigma$ bounding a handlebody-like $W$ with a handle decomposition with no $1$- or $3$-handles | Standard by direct cancellation | folklore; Kirby's problem list |
| $n=4$, $W$ diffeomorphic to a Cappell–Shaneson or Gluck-twist candidate ball | Standardized case by case | Akbulut 2010; Gompf 2010 |

No known invariant distinguishes any complementary $W \subset S^4$ from $D^4$: Seiberg–Witten, Heegaard Floer, and Khovanov-type invariants all vanish or agree on homotopy $4$-balls.

## 5. Principal Obstacles

- **Whitney trick fails in dimension 4 (smoothly).** The $h$-cobordism proof for $n \ge 6$ needs embedded Whitney discs with $2 + 2 < n$ dimension count. In dimension $4$ Whitney discs generically self-intersect; Casson–Freedman theory recovers only *topological* embeddings, which is exactly the category where the problem is already solved.
- **No parametrized replacement.** Arguments in low dimensions (e.g. $n=3$) fibre over families of level sets and need contractibility of diffeomorphism groups. Hatcher's Smale conjecture $\mathrm{Diff}(S^3) \simeq O(4)$ makes this work below dimension $4$; Watanabe's theorem shows the $4$-dimensional analogue is false, so no analogous family argument can be run.
- **Gauge theory is blind here.** Seiberg–Witten and Donaldson invariants require $b_2^+ > 1$ or non-trivial homology; a homotopy $4$-ball has $H_*(W) = 0$. Heegaard Floer and Khovanov homology of the boundary $S^3$ carry no information about the filling.
- **Handle calculus is non-terminating.** Testing whether a given contractible $W$ is $D^4$ reduces to trivializing a handle presentation, i.e. to Andrews–Curtis-type problems on balanced presentations of the trivial group, for which no algorithm and no proven obstruction exists.
- **Counterexample supply keeps collapsing.** Every explicit candidate produced since the 1970s (Cappell–Shaneson, Gluck twists on many knotted $2$-spheres, zero-surgery constructions) has eventually been shown standard, so neither side accumulates evidence.

## 6. The Gap

Proven: for $n \ne 4$, every smooth homotopy $n$-ball with $S^{n-1}$ boundary is $D^n$; and for $n = 4$, every complementary piece $W \subset S^4$ is *homeomorphic* to $D^4$ and smoothly $h$-cobordant rel boundary to $D^4$.

Missing: upgrading "homeomorphic" to "diffeomorphic" in dimension $4$ — equivalently, showing the smooth $h$-cobordism from $W$ to $D^4$ can be trivialized. The precise obstruction is the failure of the smooth Whitney trick for the middle-dimensional intersection pairing in a $5$-dimensional $h$-cobordism between $4$-manifolds. Concretely, the gap is the step: *given a contractible $W^4$ with $\partial W = S^3$ and a handle decomposition with $k$ cancelling $1$-/$2$-handle pairs that cancel algebraically, cancel them geometrically.*

## 7. Current Research (as of June 2026)

- **Trisections and bridge trisections.** Gay–Kirby's trisection theory, and Meier–Zupan's bridge trisections of embedded surfaces and $3$-spheres, give a finite combinatorial encoding of $\Sigma^3 \subset S^4$; the aim is a normal form in which standardness is decidable. *(frontier — verify: no complete decision procedure is claimed.)*
- **Extending Scharlemann's critical-point bound.** Attempts to push "four critical points" to six or eight, or to bound the genus of level surfaces after isotopy, using thin position and sweep-out arguments (Scharlemann–Thompson school).
- **Light-bulb and Dax-invariant techniques.** Gabai's $4$-dimensional light bulb theorem and subsequent work on $\pi_0$ of embedding spaces give new isotopy statements for surfaces with dual spheres; whether an analogue exists for $3$-spheres in $S^4$ is open. *(frontier — verify.)*
- **Candidate hunting.** Manolescu–Piccirillo's programme converting zero-surgery homeomorphisms into candidate exotic definite $4$-manifolds and homotopy spheres continues; the candidates produced so far have been standardized.
- **Diffeomorphism-group input.** Watanabe-style configuration-space integrals and Kontsevich classes are being pushed toward $\pi_0$-level invariants of $\mathrm{Diff}(D^4,\partial)$ that might obstruct standardness of a filling. *(frontier — verify.)*

Active groups: Princeton (Gabai), MIT/Stanford (Piccirillo, Manolescu), UT Austin (Meier, Zupan at Nebraska), Rényi/Kyoto (Watanabe), and the Kirby problem-list community.

## 8. Future Work

- Find a diffeomorphism invariant of compact contractible $4$-manifolds with $S^3$ boundary that is not a homeomorphism invariant — the single most valuable target, since none is known.
- Prove SSC$_4$ for $\Sigma$ with $\le 6$ or $\le 8$ critical points; a uniform bound on the isotopy complexity would give the full result.
- Determine whether SSC$_4 \Rightarrow$ SPC$_4$; a proof would collapse the two problems and let SPC$_4$ techniques be imported.
- Settle whether any Gluck twist $S^4_\gamma$ on a knotted $2$-sphere is exotic; a positive answer would likely produce a Schoenflies counterexample.
- Develop an effective handle calculus for balanced presentations sufficient to decide Andrews–Curtis triviality in the cases arising from contractible $4$-manifolds.

## 9. Key References

- **[Foundational]** J. W. Alexander. *On the subdivision of 3-space by a polyhedron.* Proc. Natl. Acad. Sci. USA 10 (1924), 6–8. [DOI](https://doi.org/10.1073/pnas.10.1.6)
- **[Foundational]** B. Mazur. *On embeddings of spheres.* Bull. Amer. Math. Soc. 65 (1959), 59–65.
- **[Foundational]** M. Morse. *A reduction of the Schoenflies extension problem.* Bull. Amer. Math. Soc. 66 (1960), 113–115. [DOI](https://doi.org/10.1090/s0002-9904-1960-10420-x)
- **[Foundational]** M. Brown. *A proof of the generalized Schoenflies theorem.* Bull. Amer. Math. Soc. 66 (1960), 74–76. [DOI](https://doi.org/10.1090/s0002-9904-1960-10400-4)
- **[Foundational]** S. Smale. *Generalized Poincaré's conjecture in dimensions greater than four.* Ann. of Math. 74 (1961), 391–406.
- **[Foundational]** M. Kervaire and J. Milnor. *Groups of homotopy spheres: I.* Ann. of Math. 77 (1963), 504–537.
- **[Foundational]** J. Milnor. *Lectures on the h-Cobordism Theorem.* Princeton University Press, 1965.
- **[Foundational]** J. Cerf. *Sur les difféomorphismes de la sphère de dimension trois ($\Gamma_4 = 0$).* Lecture Notes in Mathematics 53, Springer, 1968.
- **[Key partial result]** M. Scharlemann. *Smooth spheres in $\mathbb{R}^4$ with four critical points are standard.* Invent. Math. 79 (1985), 125–141. [DOI](https://doi.org/10.1007/bf01388659)
- **[Foundational]** A. Hatcher. *A proof of the Smale conjecture, $\mathrm{Diff}(S^3) \simeq O(4)$.* Ann. of Math. 117 (1983), 553–607. [DOI](https://doi.org/10.2307/2007035)
- **[Foundational]** M. Freedman. *The topology of four-dimensional manifolds.* J. Differential Geom. 17 (1982), 357–453.
- **[SOTA / Recent]** S. Akbulut. *Cappell–Shaneson homotopy spheres are standard.* Ann. of Math. 171 (2010), 2171–2175. [DOI](https://doi.org/10.4007/annals.2010.171.2171)
- **[SOTA / Recent]** R. Gompf. *More Cappell–Shaneson spheres are standard.* Algebr. Geom. Topol. 10 (2010), 1665–1681. [DOI](https://doi.org/10.2140/agt.2010.10.1665)
- **[SOTA / Recent]** M. Freedman, R. Gompf, S. Morrison, K. Walker. *Man and machine thinking about the smooth 4-dimensional Poincaré conjecture.* Quantum Topology 1 (2010), 171–208. [DOI](https://doi.org/10.4171/qt/5)
- **[SOTA / Recent]** D. Gabai. *The 4-dimensional light bulb theorem.* J. Amer. Math. Soc. 33 (2020), 609–652. [DOI](https://doi.org/10.1090/jams/920)
- **[SOTA / Recent]** T. Watanabe. *Some exotic nontrivial elements of the rational homotopy groups of $\mathrm{Diff}(S^4)$.* arXiv:1812.02448, 2018.
- **[SOTA / Recent]** C. Manolescu, L. Piccirillo. *From zero surgeries to candidates for exotic definite four-manifolds.* arXiv:2102.04391, 2021.
- **[Survey]** R. Kirby. *Problems in low-dimensional topology.* In: Geometric Topology (AMS/IP Stud. Adv. Math. 2.2), AMS, 1997. [DOI](https://doi.org/10.1090/amsip/002.2/02)
- **[Survey]** A. Scorpan. *The Wild World of 4-Manifolds.* American Mathematical Society, 2005.
- **[Survey]** T. B. Rushing. *Topological Embeddings.* Academic Press, 1973.

## 10. Worked Example / Concrete Special Case

**Claim.** If $\Sigma^3 \subset \mathbb{R}^4$ is a smoothly embedded $3$-sphere such that $h = x_4|_\Sigma$ is Morse with exactly **two** critical points, then $\Sigma$ is standard.

**Step 1 — index count.** With $c_0 - c_1 + c_2 - c_3 = \chi(S^3) = 0$ and $c_0 + c_1 + c_2 + c_3 = 2$, and $c_0, c_3 \geq 1$ for a compact $\Sigma$, we get $c_0 = c_3 = 1$, $c_1 = c_2 = 0$. Say the critical values are $a < b$.

**Step 2 — level sets.** For $t \in (a,b)$, $\Sigma_t = \Sigma \cap \{x_4 = t\}$ is a closed orientable surface in the hyperplane $\mathbb{R}^3_t \cong \mathbb{R}^3$. Since no index-$1$ or index-$2$ critical point occurs, the diffeomorphism type of $\Sigma_t$ is constant on $(a,b)$, and just above $a$ it is a small sphere born at the index-$0$ point. So every $\Sigma_t$ is an embedded $2$-sphere in $\mathbb{R}^3$.

**Step 3 — Alexander in each slice.** By the Alexander–Schoenflies theorem in $\mathbb{R}^3$, each $\Sigma_t$ bounds a closed $3$-ball $B_t \subset \mathbb{R}^3_t$, and $\Sigma_t$ is ambiently isotopic to a round sphere.

**Step 4 — smoothing the family.** The choices in Step 3 must be made continuously in $t$. The space of smooth unknotted $2$-spheres in $\mathbb{R}^3$ is homotopy equivalent to the space of round spheres, by Hatcher's theorem $\mathrm{Diff}(S^3) \simeq O(4)$ (equivalently $\mathrm{Diff}(D^3, \partial) \simeq \ast$). Hence the family $\{\Sigma_t\}_{t \in (a,b)}$ can be smoothly straightened to a family of round spheres of radius $r(t) > 0$ centred at $c(t) \in \mathbb{R}^3$, with $r(t) \to 0$ as $t \to a^+$ and as $t \to b^-$.

**Step 5 — conclusion.** After the ambient isotopy of Step 4, $\Sigma = \{(c(t) + r(t)u,\, t) : u \in S^2,\ t \in [a,b]\}$, which is the boundary of the smooth $4$-ball $\{(x,t) : |x - c(t)| \leq r(t)\}$. So $\Sigma$ is standard, and the outside is $D^4$ as well by the disc theorem applied in $S^4 = \mathbb{R}^4 \cup \{\infty\}$. $\qquad\blacksquare$

**Where it stops.** With four critical points ($c_0 = c_3 = 1$, $c_1 = c_2 = 1$), the middle levels are tori, and Step 3 fails: an embedded torus in $\mathbb{R}^3$ can be knotted. Scharlemann (1985) handles exactly this case by a delicate thin-position analysis of the knotted middle torus. At six critical points the middle levels can be genus-$2$ surfaces, the possible configurations grow without a known bound, and no argument is available — this is precisely where the problem is open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*