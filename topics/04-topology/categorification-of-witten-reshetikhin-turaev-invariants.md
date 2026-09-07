---
id: 04-topology/categorification-of-witten-reshetikhin-turaev-invariants
title: "Categorification of Witten-Reshetikhin-Turaev Invariants"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Categorification of Witten-Reshetikhin-Turaev Invariants

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/categorification-of-witten-reshetikhin-turaev-invariants` · **Status:** open

## 1. Problem Statement / Conjecture

The Witten–Reshetikhin–Turaev (WRT) invariant assigns to a closed oriented $3$-manifold $M$ and a root of unity $\zeta_r$ a complex number $\tau_r(M) \in \mathbb{Z}[\zeta_r]$. The Jones polynomial of a link admits a categorification — Khovanov homology, a bigraded abelian group whose graded Euler characteristic recovers the polynomial. The open problem is the $3$-manifold analogue:

**Problem.** Construct a functorial assignment $M \mapsto \mathcal{H}^{*,*}(M)$ of bigraded (or multigraded) abelian groups, defined for all closed oriented $3$-manifolds, such that

$$\chi_q\big(\mathcal{H}^{*,*}(M)\big) \;=\; \sum_{i,j} (-1)^i q^{j} \operatorname{rk} \mathcal{H}^{i,j}(M) \;=\; \tau(M)$$

where $\tau$ is a $q$-refinement of the WRT invariants (evaluating to $\tau_r(M)$ at $q \to \zeta_r$, or agreeing with Habiro's unified invariant), and such that $\mathcal{H}$ extends to a $(3{+}1)$-dimensional TQFT: cobordisms $W: M_0 \to M_1$ induce maps $\mathcal{H}(M_0) \to \mathcal{H}(M_1)$, giving invariants of smooth $4$-manifolds.

A complete solution requires: (i) a construction independent of surgery presentation, with a proof of invariance under Kirby moves at the categorified level; (ii) finite-rank (or at least finitely generated in each bidegree) homology groups; (iii) the Euler characteristic identity above; (iv) functoriality under $4$-dimensional cobordism. A disproof would exhibit an obstruction — e.g. a proof that no theory with these properties can exist, such as an incompatibility between finiteness and the algebraic-number values of $\tau_r$.

## 2. Mathematical Foundations

**WRT invariants.** Fix $r \ge 3$, $q = \zeta_r = e^{2\pi i/r}$, and set $[n] = \dfrac{q^{n/2} - q^{-n/2}}{q^{1/2}-q^{-1/2}} = \dfrac{\sin(n\pi/r)}{\sin(\pi/r)}$. Let $M$ be obtained by surgery on a framed link $L \subset S^3$ with $\ell$ components and linking matrix of signature $(b_+, b_-)$. Write $\langle L; n_1,\dots,n_\ell\rangle$ for the Kauffman-bracket evaluation of $L$ with components colored by the Jones–Wenzl idempotents $e_{n_i}$. With the Kirby color

$$\omega \;=\; \sum_{n=0}^{r-2} [n+1]\, e_n ,$$

the invariant is

$$\tau_r(M) \;=\; \frac{\langle \omega(L)\rangle}{\langle \omega(U_+)\rangle^{\,b_+}\,\langle \omega(U_-)\rangle^{\,b_-}}, \qquad \langle \omega(U_\pm)\rangle = \sum_{n=0}^{r-2}[n+1]^2 (-1)^n q^{\pm(n^2+2n)/4}.$$

Invariance under the Kirby moves (handle slide, blow-up/down) follows from $\omega$ being killed by encircling and from the Gauss-sum normalization (Reshetikhin–Turaev 1991; Kirby–Melvin 1991; Blanchet–Habegger–Masbaum–Vogel 1995).

**Categorification of the link level.** Khovanov homology $\mathrm{Kh}^{i,j}(L)$ satisfies $\sum_{i,j}(-1)^i q^j \operatorname{rk}\mathrm{Kh}^{i,j}(L) = \hat J(L)(q)$, the unnormalized Jones polynomial. Colored versions $\mathrm{Kh}_n$ categorify the colored Jones polynomials $J_n$; the color-$n$ strand corresponds to a categorified Jones–Wenzl projector $P_n$, an infinite complex of Bott–Samelson bimodules (Cooper–Krushkal; Rozansky; Frenkel–Stroppel–Sussan).

**The Habiro ring.** For an integral homology sphere $M$, Habiro (2008) constructed a unified invariant
$$J_M(q) \;\in\; \widehat{\mathbb{Z}[q]} = \varprojlim_n \mathbb{Z}[q]\big/\big((q;q)_n\big), \qquad (q;q)_n = \prod_{k=1}^{n}(1-q^k),$$
whose evaluation at $q=\zeta_r$ equals $\tau_r(M)$ for all $r$, and whose Taylor expansion at $q=1$ is the Ohtsuki series. $\widehat{\mathbb{Z}[q]}$ is the natural target for an Euler characteristic: it consists of $q$-series with integer coefficients, unlike $\mathbb{Z}[\zeta_r]$.

**$\hat{Z}$-invariants.** Gukov–Pei–Putrov–Vafa proposed, for $M$ a rational homology sphere with $\mathrm{spin}^c$-type label $b \in \mathrm{Spin}^c(M)/\mathbb{Z}_2$, a $q$-series
$$\hat{Z}_b(M;q) \in 2^{-c}q^{\Delta_b}\mathbb{Z}[[q]], \qquad \tau_r(M) \;\dot=\; \sum_b \text{(resurgent/limit combination of } \hat{Z}_b),$$
conjecturally the graded dimension of a homology $\mathcal{H}^{*,*}_b(M)$ coming from BPS states of the $6$d $(2,0)$ theory on $M \times D^2$ — the physics prediction of the sought categorification.

## 3. History & State of the Art (SOTA)

- **1989.** Witten defines $3$-manifold invariants via Chern–Simons path integrals; Reshetikhin–Turaev (Invent. Math. 1991) make them rigorous using $U_q(\mathfrak{sl}_2)$ at roots of unity. Kirby–Melvin (1991) and BHMV (1995) give skein-theoretic constructions.
- **1994.** Crane and Frenkel propose *categorification*: Hopf categories and canonical bases should upgrade the $(2{+}1)$-TQFT to a $(3{+}1)$-dimensional one, giving smooth $4$-manifold invariants. This is the origin of the problem.
- **2000.** Khovanov categorifies the Jones polynomial (Duke Math. J. 101). Khovanov–Rozansky (2008) extend to $\mathfrak{sl}_N$ via matrix factorizations.
- **2008–2012.** Habiro's unified invariant supplies an integral $q$-series target. Cooper–Krushkal and Rozansky categorify Jones–Wenzl projectors, making colored strands categorifiable.
- **2010.** Rozansky categorifies the *stable* SU(2) WRT invariant of links in $S^2 \times S^1$.
- **2016–2020.** Khovanov–Lauda / Rouquier categorified quantum groups and Webster's categorified Reshetikhin–Turaev tangle invariants supply the $2$-representation-theoretic scaffolding. GPPV introduce $\hat{Z}$.
- **2022–2024.** Morrison–Walker–Wedrich define *skein lasagna modules* $\mathcal{S}_0(W;L)$ from Khovanov–Rozansky homology — a genuine $4$-manifold invariant, currently the strongest realization of the Crane–Frenkel program. Ren–Willis (2024) use them to detect an exotic pair of $4$-manifolds, a result unreachable by Seiberg–Witten or Donaldson theory in that setting.

**SOTA summary:** no construction satisfies all of (i)–(iv). Skein lasagna modules satisfy (i) and (iv) but not a WRT Euler-characteristic statement; $\hat{Z}$ satisfies (iii) conjecturally for restricted $M$ but has no homology behind it in general.

## 4. Partial Results / Verified Cases

- **Links, all colors, all $N$.** Khovanov ($\mathfrak{sl}_2$), Khovanov–Rozansky ($\mathfrak{sl}_N$, HOMFLY-PT), Webster (arbitrary $\mathfrak{g}$ and highest weights) categorify the *link-level* Reshetikhin–Turaev invariants, i.e. the invariant before surgery.
- **Jones–Wenzl projectors.** $P_n$ is categorified for all $n \ge 0$ (Cooper–Krushkal 2012; Rozansky 2014 via infinite twists; Frenkel–Stroppel–Sussan 2012 for $3j$-symbols). This handles the *color* summand of $\omega$ but not the infinite alternating sum.
- **$M = S^2 \times S^1$ and stable limits.** Rozansky (2010) constructs a categorification of the stable SU(2) WRT invariant for links in $S^2 \times S^1$; Beliakova–Putyra–Wehrli (Invent. Math. 2019) build link homology in $S^1 \times S^2$ via a trace (Hochschild homology) functor, with the correct Euler characteristic.
- **Negative-definite plumbed $3$-manifolds.** $\hat{Z}_b$ is defined rigorously and shown to recover $\tau_r$ (GPPV 2020) for plumbed manifolds with negative-definite intersection form — including all Brieskorn spheres $\Sigma(p,q,r)$.
- **$4$-manifolds.** Skein lasagna modules are computed for $2$-handlebodies (Manolescu–Neithalath 2020: cabled Khovanov–Rozansky formula) and shown to vanish for $\mathcal{S}_0(-\mathbb{CP}^2)$ and related negative-definite pieces (Manolescu–Walker–Wedrich 2023; Ren–Willis 2024).
- **Homology spheres, $q$-series level.** Habiro's $J_M(q) \in \widehat{\mathbb{Z}[q]}$ exists for *all* integral homology spheres, giving an integrality statement necessary for any categorification.

## 5. Principal Obstacles

1. **Wrong coefficient ring.** $\tau_r(M) \in \mathbb{Z}[\zeta_r]$ is an algebraic number, not a Laurent polynomial in $q$ with integer coefficients. A graded Euler characteristic *is* such a polynomial (or power series). Any categorification must first replace $\tau_r$ by a $q$-series (Habiro, $\hat{Z}$), and the required interpolation exists unconditionally only for homology spheres.
2. **Infinite sums with signs.** The Kirby color $\omega = \sum_n [n+1]e_n$ is a *finite* sum whose coefficients $[n+1]$ are $r$-dependent, and $\langle\omega(U_\pm)\rangle$ is a Gauss sum. Categorifying it needs an infinite complex of categorified projectors with a convergence/completion structure; existing homotopy-limit techniques (Rozansky's infinite twist, Hogancamp's stable homology) converge only under positivity/adequacy hypotheses.
3. **Kirby move invariance is a homotopy statement.** Handle slides must be lifted from equalities to chain homotopy equivalences, and the blow-up relation to a shift. This requires coherence data (a chain-level $E_\infty$-type structure) that no current framework supplies at the level of the full $\omega$-colored complex.
4. **Functoriality failures.** Khovanov homology is functorial only up to sign for classical cobordisms, and $\mathfrak{sl}_N$ foam functoriality was hard-won; $4$-dimensional gluing requires strict functoriality plus a locality (factorization) structure.
5. **Finiteness.** Skein lasagna modules are frequently infinite-rank or unknown even for simple closed $4$-manifolds ($S^4$, $S^2\times S^2$), so the Euler characteristic may not be defined without a genuinely new finiteness theorem.
6. **No non-semisimple/derived analogue of modularity.** The Verlinde formula and $S$-matrix arguments that make WRT well-defined are semisimple statements; their derived analogues (for the non-semisimple categories that appear) are missing.

## 6. The Gap

Proven: categorification of the *link* invariant for all colors and all $\mathfrak{sl}_N$; categorification of the projectors; a $4$-manifold-valued theory (skein lasagna) without a WRT Euler characteristic; a $q$-series refinement $\hat{Z}$ for negative-definite plumbings.

Required: a single construction that (a) accepts the Kirby color as a categorified object — an object $\Omega$ in a suitable derived/completed skein category with $[\Omega] = \omega$; (b) proves handle-slide invariance as an explicit chain homotopy equivalence $\Omega \otimes (-) \simeq (-)$; (c) yields finitely generated homology; (d) recovers $J_M(q)$ or $\hat{Z}_b(M;q)$ on Euler characteristics. The exact barrier is step (b) together with the completion needed for (a): the categorified $\omega$ is an infinite complex, and current homotopy-limit machinery gives invariance only after imposing hypotheses (adequacy, negative-definiteness) that exclude general $M$.

## 7. Current Research (as of June 2026)

- **Skein lasagna school** (Manolescu, Walker, Wedrich, Morrison; Ren–Willis; Stanford/Sydney/MPIM Bonn). Computations of $\mathcal{S}_0(W;L)$ for closed $4$-manifolds and handlebodies; vanishing and non-vanishing criteria; exotic detection. *(frontier — verify)* Reported extensions of the Ren–Willis exotic-detection argument to further $2$-handlebody pairs.
- **$\hat{Z}$ and quantum modularity** (Gukov, Putrov, Park, Cheng, Chun; Caltech/IPMU/IHES). Extending $\hat{Z}_b$ beyond negative-definite plumbings, to positive-definite and non-plumbed manifolds, and to $\mathfrak{sl}_N$ / higher rank; relations to false theta functions and resurgence.
- **Categorified quantum groups and Hochschild-type traces** (Beliakova, Putyra, Wehrli, Lauda, Webster). Trace decategorification and horizontal trace as the mechanism for closing up $3$-manifolds from tangle categories.
- **Non-semisimple TQFT** (Blanchet, Costantino, Geer, Patureau-Mirand). Modified traces and unrolled quantum groups give $3$-manifold invariants with richer $\mathbb{Z}[q]$-integrality; their categorification is an active target.
- **Foam and annular technology** (Queffelec, Rose, Hogancamp, Elias). $\mathfrak{sl}_N$ foam evaluation and stable homology of infinite twists, feeding the categorified Kirby-color problem.

## 8. Future Work

- Construct a categorified Kirby color as a homotopy colimit of categorified projectors in a completed derived skein category, and prove handle-slide invariance directly.
- Prove that $\hat{Z}_b(M;q)$ has non-negative-coefficient decompositions after suitable normalization for a broad class of $M$, evidence that a homology theory exists with $\hat{Z}$ as its Poincaré series.
- Establish finiteness theorems for skein lasagna modules of closed $4$-manifolds; compute $\mathcal{S}_0(S^4)$, $\mathcal{S}_0(S^2\times S^2)$ definitively.
- Relate $\mathcal{H}^{*,*}(M)$ to instanton and Heegaard Floer homology, which categorify the Casson invariant / Turaev torsion — asking whether WRT categorification and Floer theory are two faces of one $(3{+}1)$-TQFT.
- Extend Habiro's unified invariant to rational homology spheres and higher-rank $\mathfrak{g}$, fixing the target ring before the homology is built.

## 9. Key References

- **[Foundational]** E. Witten. *Quantum field theory and the Jones polynomial.* Communications in Mathematical Physics 121 (1989), 351–399.
- **[Foundational]** N. Reshetikhin, V. G. Turaev. *Invariants of 3-manifolds via link polynomials and quantum groups.* Inventiones Mathematicae 103 (1991), 547–597.
- **[Foundational]** R. Kirby, P. Melvin. *The 3-manifold invariants of Witten and Reshetikhin–Turaev for $sl(2,\mathbb{C})$.* Inventiones Mathematicae 105 (1991), 473–545.
- **[Foundational]** C. Blanchet, N. Habegger, G. Masbaum, P. Vogel. *Topological quantum field theories derived from the Kauffman bracket.* Topology 34 (1995), 883–927.
- **[Foundational]** L. Crane, I. B. Frenkel. *Four-dimensional topological quantum field theory, Hopf categories, and the canonical bases.* Journal of Mathematical Physics 35 (1994), 5136–5154.
- **[Foundational]** M. Khovanov. *A categorification of the Jones polynomial.* Duke Mathematical Journal 101 (2000), 359–426.
- **[Foundational]** M. Khovanov, L. Rozansky. *Matrix factorizations and link homology.* Fundamenta Mathematicae 199 (2008), 1–91.
- **[Foundational]** K. Habiro. *A unified Witten–Reshetikhin–Turaev invariant for integral homology spheres.* Inventiones Mathematicae 171 (2008), 1–81.
- **[SOTA / Recent]** B. Cooper, V. Krushkal. *Categorification of the Jones–Wenzl projectors.* Quantum Topology 3 (2012), 139–180.
- **[SOTA / Recent]** L. Rozansky. *An infinite torus braid yields a categorified Jones–Wenzl projector.* Fundamenta Mathematicae 225 (2014), 305–326.
- **[SOTA / Recent]** L. Rozansky. *A categorification of the stable SU(2) Witten–Reshetikhin–Turaev invariant of links in $S^2 \times S^1$.* arXiv:1011.1958 (2010).
- **[SOTA / Recent]** B. Webster. *Knot invariants and higher representation theory.* Memoirs of the American Mathematical Society 250 (2017), no. 1191.
- **[SOTA / Recent]** A. Beliakova, K. Putyra, S. Wehrli. *Quantum link homology via trace functor I.* Inventiones Mathematicae 215 (2019), 383–492.
- **[SOTA / Recent]** S. Gukov, P. Putrov, C. Vafa. *Fivebranes and 3-manifold homology.* Journal of High Energy Physics 2017, no. 7, 071.
- **[SOTA / Recent]** S. Gukov, D. Pei, P. Putrov, C. Vafa. *BPS spectra and 3-manifold invariants.* Journal of Knot Theory and Its Ramifications 29 (2020), 2040003.
- **[SOTA / Recent]** S. Gukov, C. Manolescu. *A two-variable series for knot complements.* Quantum Topology 12 (2021), 1–109.
- **[SOTA / Recent]** S. Morrison, K. Walker, P. Wedrich. *Invariants of 4-manifolds from Khovanov–Rozansky link homology.* Geometry & Topology 26 (2022), 3367–3420.
- **[SOTA / Recent]** C. Manolescu, I. Neithalath. *Skein lasagna modules for 2-handlebodies.* Journal für die reine und angewandte Mathematik (Crelle) 779 (2021), 265–284.
- **[SOTA / Recent]** Q. Ren, M. Willis. *Khovanov skein lasagna detects exotic 4-manifolds.* arXiv:2402.10452 (2024).
- **[Survey]** M. Khovanov. *Categorifications from planar diagrammatics.* Japanese Journal of Mathematics 5 (2010), 153–181.
- **[Survey]** V. G. Turaev. *Quantum Invariants of Knots and 3-Manifolds.* De Gruyter Studies in Mathematics 18, 3rd edition, 2016.

## 10. Worked Example / Concrete Special Case

**Step 1 — the link level works.** For the unknot $U$, reduced-to-unreduced Khovanov homology is $\mathrm{Kh}^{0,-1}(U) = \mathrm{Kh}^{0,1}(U) = \mathbb{Z}$, all else zero, so
$$\chi_q(\mathrm{Kh}(U)) = q^{-1} + q = [2].$$
This matches $\hat J(U) = [2]$. So a single unknotted, color-$1$ strand is categorified.

**Step 2 — the surgery level fails naively.** Take $M = S^1 \times S^2$, obtained by $0$-surgery on $U$. Then $b_+ = b_- = 0$ and the unnormalized WRT bracket is the Kirby-colored unknot:
$$\langle \omega(U)\rangle \;=\; \sum_{n=0}^{r-2}[n+1]^2 \;=\; \sum_{k=1}^{r-1}\frac{\sin^2(k\pi/r)}{\sin^2(\pi/r)} \;=\; \frac{r}{2\sin^2(\pi/r)} .$$
At $r=5$: $\sin^2(\pi/5) = (10-2\sqrt5)/16 = 0.34549\ldots$, so
$$\langle\omega(U)\rangle = \frac{5}{2(0.34549)} = 7.2360\ldots = 5+\sqrt5 .$$

**Step 3 — reading the obstruction.** $5+\sqrt5 \in \mathbb{Z}[\zeta_5]$ is an algebraic irrationality. A graded Euler characteristic $\sum_{i,j}(-1)^i q^j \operatorname{rk}\mathcal{H}^{i,j}$ evaluated at $q = \zeta_5$ could produce this number, but only if the underlying $q$-series exists *before* specialization. Here the summands $[n+1]^2$ individually categorify (each is $\chi_q$ of a colored Khovanov homology of $U$ with a projector inserted), but the total depends on $r$ through the truncation $n \le r-2$: the family of complexes does not stabilize as $r \to \infty$, since $\sum_{n\ge0}[n+1]^2$ diverges in $\mathbb{Z}[[q]]$.

**Step 4 — how the known fixes act.** Two repairs are known for this example:

- *Trace/stable route.* Beliakova–Putyra–Wehrli replace "close up the unknot into $S^1\times S^2$" by the horizontal trace (Hochschild homology) of the Khovanov bimodule category, producing a genuine homology for links in $S^1\times S^2$ with the correct stable Euler characteristic — Rozansky's stable SU(2) invariant. This categorifies the $r\to\infty$ limit, not $\tau_5$.
- *$q$-series route.* Replace $\tau_r$ by $\hat Z_b(M;q) \in q^{\Delta_b}\mathbb{Z}[[q]]$. For $M = \Sigma(2,3,5)$ (negative-definite plumbing) $\hat Z$ is a single well-defined $q$-series with integer coefficients whose radial limit at $q \to \zeta_r$ reproduces $\tau_r(M)$ up to normalization; the conjecture is that these integers are ranks $\sum_i (-1)^i \operatorname{rk}\mathcal{H}^{i,j}_b(M)$.

Neither repair works for a general $M$ with $b_+ > 0$, and neither yet produces the $4$-dimensional functoriality of clause (iv). That triple demand — $r$-independence, integrality, functoriality — is exactly what remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*