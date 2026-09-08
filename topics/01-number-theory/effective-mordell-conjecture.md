---
id: 01-number-theory/effective-mordell-conjecture
title: "Chabauty-Kim Program for Rational Points"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chabauty–Kim Program for Rational Points

> **Topic:** Number Theory · **ID:** `01-number-theory/effective-mordell-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Faltings (1983) proved Mordell's conjecture: a smooth projective geometrically irreducible curve $X/K$ of genus $g \ge 2$ over a number field $K$ has $\\#X(K) < \infty$. The proof, and Vojta's and Bombieri's later proofs, are **ineffective**: they bound the number of points but give no algorithm to find them.

**Effective Mordell.** There is a computable function $B$ such that for every $X/K$ of genus $g\ge 2$ given by equations of height $H$,
$$h_{\mathcal{L}}(P) \le B(g, K, H) \qquad \text{for all } P \in X(K),$$
where $h_{\mathcal{L}}$ is a Weil height attached to an ample $\mathcal{L}$. Equivalently: an algorithm that, on input $X$, outputs the finite set $X(K)$ and a proof of completeness.

**Chabauty–Kim as a route.** Kim's program replaces the Jacobian by the unipotent fundamental group. For each $n\ge 1$ it produces a nested chain of $p$-adic loci
$$X(K) \subseteq \cdots \subseteq X(K_v)_n \subseteq \cdots \subseteq X(K_v)_2 \subseteq X(K_v)_1 \subseteq X(K_v).$$
Two conjectural statements drive the field:

- **(Finiteness / effectivity)** For $n \gg 0$, $X(K_v)_n$ is finite and computable, giving effective Mordell.
- **(Kim's conjecture)** $\bigcap_{n\ge1} X(K_v)_n = X(K)$ — the tower cuts out exactly the rational points, so the method terminates with a *complete* answer, not merely a superset.

A proof requires either establishing the Selmer-dimension inequality $\dim \mathrm{Sel}_n < \dim \pi_1^{\mathrm{un}}(X_{K_v})_n$ for large $n$ in general (currently conditional on Bloch–Kato-type conjectures), or an independent effective height bound.

## 2. Mathematical Foundations

Fix $X/\mathbb{Q}$ smooth projective of genus $g\ge2$ with a rational base point $b$, Jacobian $J$, Mordell–Weil rank $r = \operatorname{rank} J(\mathbb{Q})$, and $p$ a prime of good reduction.

**Classical Chabauty–Coleman.** Let $\overline{J(\mathbb{Q})}$ be the $p$-adic closure of $J(\mathbb{Q})$ in $J(\mathbb{Q}_p)$. Chabauty (1941): if $r < g$ then $\dim \overline{J(\mathbb{Q})} \le r < g$, so there is a nonzero $\omega \in H^0(X_{\mathbb{Q}_p}, \Omega^1)$ with $\int_{J} \omega = 0$ on $\overline{J(\mathbb{Q})}$. Coleman integration gives a locally analytic $f(z)=\int_b^z\omega$ vanishing on $X(\mathbb{Q})$, and Newton-polygon bounds on its zeros yield (Coleman 1985), for $p>2g$,
$$\\#X(\mathbb{Q}) \le \\#X(\mathbb{F}_p) + 2g - 2 .$$

**Unipotent Albanese and Selmer schemes.** Let $U = \pi_1^{\mathrm{un},\mathbb{Q}_p}(X_{\overline{\mathbb{Q}}}, b)$ be the $\mathbb{Q}_p$-pro-unipotent étale fundamental group, with descending central series quotients $U_n = U/[U]^{n+1}$; $U_1 = V_p J = H_1^{\text{ét}}\otimes\mathbb{Q}_p$. Galois acts, giving a class map to a continuous cohomology set, and one defines the **Selmer scheme**
$$\mathrm{Sel}_n \;=\; H^1_f(G_{\mathbb{Q},S}, U_n) \subseteq H^1(G_{\mathbb{Q},S}, U_n),$$
cut out by local conditions (crystalline at $p$, unramified outside $S$). The unipotent Kummer map $j_n : X(\mathbb{Q}) \to \mathrm{Sel}_n$ and its local counterpart $j_n^{\mathrm{loc}} : X(\mathbb{Q}_p) \to H^1_f(G_{\mathbb{Q}_p}, U_n) \cong U_n^{\mathrm{dR}}/F^0$ fit in a commutative square, and
$$X(\mathbb{Q}_p)_n \;:=\; (j_n^{\mathrm{loc}})^{-1}\big(\mathrm{loc}_p(\mathrm{Sel}_n)\big) \;\supseteq\; X(\mathbb{Q}).$$

**Kim's criterion.** If
$$\dim \mathrm{Sel}_n \;<\; \dim \big(U_n^{\mathrm{dR}}/F^0\big),$$
then $\mathrm{loc}_p$ is not dominant, its image lies in a proper Zariski-closed subset, and pulling back nonzero algebraic functions gives nonzero Coleman–Kim functions vanishing on $X(\mathbb{Q})$; hence $X(\mathbb{Q}_p)_n$ is finite. For $n=1$ this is exactly $r<g$.

**Quadratic Chabauty ($n=2$).** Let $\rho = \operatorname{rank}\mathrm{NS}(J)$ be the Picard number. Balakrishnan–Dogra: if
$$r < g + \rho - 1,$$
then $X(\mathbb{Q}_p)_2$ is finite, and is cut out by the equation
$$h_p(z) \;=\; \sum_{v \neq p} h_v(z) \;+\; \text{(bilinear form in } \log \text{ of MW generators)},$$
where $h_p$ is a $p$-adic (Nekovář/Coleman–Gross) height on a Selmer variety of a $\mathbb{G}_m$-torsor over $X$, and each $h_v$ takes finitely many explicitly computable values depending only on the reduction type at $v$.

**Effectivity link.** Elkies (1991) showed effective ABC $\Rightarrow$ effective Mordell, via Belyi maps; conversely no unconditional effective height bound is known for a single curve of genus $\ge 2$ whose Jacobian has no special structure.

## 3. History & State of the Art

- **1922** Mordell states the conjecture.
- **1941** Chabauty proves finiteness when $r<g$, using $p$-adic analytic groups.
- **1968–69** Baker's linear forms in logarithms give effective bounds for integral points on genus-1 and hyperelliptic/superelliptic curves.
- **1983** Faltings proves Mordell (ineffective). **1991** Vojta gives a Diophantine-approximation proof; Bombieri (1990) simplifies it.
- **1985** Coleman reinterprets Chabauty via $p$-adic integration, yielding the bound $\\#X(\mathbb{F}_p)+2g-2$.
- **2005, 2009** Kim constructs the Selmer variety tower; recovers Siegel's theorem for $\mathbb{P}^1\setminus\{0,1,\infty\}$ effectively in low depth and reproves Faltings' theorem conditionally on Bloch–Kato.
- **2018** Balakrishnan–Dogra, *Quadratic Chabauty and rational points I*, Duke Math. J. 167 — the first practical non-abelian instance.
- **2019** Balakrishnan–Dogra–Müller–Tuitman–Vonk determine $X_s(13)(\mathbb{Q})$ (the "cursed curve"), Annals of Math. 189.
- **2020** Lawrence–Venkatesh give a new proof of Mordell via $p$-adic period maps (Invent. Math. 221) — still ineffective on heights.
- **2021** Dimitrov–Gao–Habegger prove uniform bounds $\\#X(K) \le c(g,d)^{1+r}$; Kühne's equidistribution result removes remaining hypotheses.
- **2023** Balakrishnan–Dogra–Müller–Tuitman–Vonk, *Quadratic Chabauty for modular curves*, Compositio Math. 159 — algorithmic package applied to many $X_0(N)^+$.

**SOTA summary.** Counting is effective and uniform; *heights* are not. Chabauty–Kim is the only method that has produced provably complete rational-point sets for curves with $r \ge g$.

## 4. Partial Results / Verified Cases

- **$r < g$:** Chabauty–Coleman; $\\#X(\mathbb{Q}) \le \\#X(\mathbb{F}_p)+2g-2$ for $p>2g$ of good reduction (Coleman 1985); Stoll's refinement removes the good-reduction/prime-size hypotheses in many cases.
- **$r \le g-3$:** Katz–Rabinoff–Zureick-Brown (2016) prove the uniform bound $\\#X(\mathbb{Q}) \le 76g^2 - 82g + 22$ for any such curve over $\mathbb{Q}$, with no good-reduction hypothesis.
- **$r < g + \rho - 1$:** quadratic Chabauty gives finite, computable $X(\mathbb{Q}_p)_2$. Applies whenever $J$ has real multiplication or a nontrivial isogeny decomposition — in particular to modular curves.
- **$X_s(13)$:** $g=3$, $r=3$, $\rho=3$; exactly **7** rational points, all cusps or CM points (BDMTV, Annals 2019). Same for $X_{ns}^+(N)$ in further small levels.
- **$X_0(N)^+$:** rational points determined for all hyperelliptic and many further levels by quadratic Chabauty (BDMTV, Compositio 2023).
- **CM Jacobians:** Coates–Kim (2010) prove finiteness of $X(\mathbb{Q}_p)_n$ for curves whose Jacobian has CM by a field containing... (all endomorphisms defined over $K$), unconditionally.
- **Effective height bounds** are known for: genus-1 curves and hyperelliptic/superelliptic integral points (Baker), Thue and unit equations, curves admitting a map to such a curve (Bilu 1995, via Chevalley–Weil), and modular curves accessible to Runge's method (Bilu–Parent, Annals 2011).
- **Kim's conjecture** is verified in depth $2$ for $\mathbb{P}^1\setminus\{0,1,\infty\}$ over $\mathbb{Q}$ at many primes (Balakrishnan–Dan-Cohen–Kim–Wewers, Math. Ann. 372, 2018), numerically.

## 5. Principal Obstacles

- **No lower bound on Selmer dimension growth.** Kim's criterion needs $\dim\mathrm{Sel}_n$ to grow slower than $\dim U_n^{\mathrm{dR}}/F^0$. Controlling $\dim\mathrm{Sel}_n$ requires vanishing of $H^1_f$ of Tate twists — precisely the Bloch–Kato conjecture. Nothing unconditional bounds $\mathrm{Sel}_n$ for $n\ge3$ in general.
- **Kim's conjecture gives no error term.** Even when $X(\mathbb{Q}_p)_n$ is finite, one only knows $X(\mathbb{Q}) \subseteq X(\mathbb{Q}_p)_n$. Excess points ("$p$-adic ghosts") must be eliminated by hand, typically by the Mordell–Weil sieve, which has no proof of termination.
- **Heights vs. counts.** Vojta's inequality and the DGH/Kühne machinery bound *how many* points there are via geometry of numbers on $J(K)\otimes\mathbb{R}$; they say nothing about how large a point can be, because the ineffectivity sits in an unknown "first exceptional point" of comparison of heights.
- **Mordell–Weil generators.** Every version of Chabauty requires explicit generators of $J(\mathbb{Q})$; computing them needs $\Sha(J/\mathbb{Q})[p^\infty]$ finiteness, itself open.
- **Computation.** Coleman integration on non-hyperelliptic curves, and iterated Coleman integrals in depth $\ge3$, are expensive; local height contributions $h_v$ at bad primes require explicit regular models.
- **Lawrence–Venkatesh** replaces Selmer varieties by variation of Hodge structure in $p$-adic families, but its ineffectivity is inherited from a non-constructive Zariski-density argument.

## 6. The Gap

Proven: finiteness and computability of $X(\mathbb{Q}_p)_n$ under the *numerical* hypotheses $r<g$ ($n=1$) and $r<g+\rho-1$ ($n=2$), plus a conditional general statement assuming Bloch–Kato. Wanted: for arbitrary $X$ of genus $\ge2$, an $n = n(X)$, computable from $g$, $K$ and the bad primes, with

1. $\dim \mathrm{Sel}_n < \dim U_n^{\mathrm{dR}}/F^0$ — **unconditional**, and
2. $X(\mathbb{Q}_p)_n = X(\mathbb{Q})$ (Kim's conjecture), or a computable bound on $\\#\big(X(\mathbb{Q}_p)_n \setminus X(\mathbb{Q})\big)$ that a sieve can clear.

The single missing step in (1) is a bound of the shape $\dim H^1_f(G_{\mathbb{Q},S}, \mathrm{gr}^n U) = 0$ for the "irrelevant" Galois representations appearing in the graded pieces — equivalent to non-vanishing of certain $L$-values, i.e. Bloch–Kato in the specific weights arising from $\pi_1$.

## 7. Current Research (as of June 2026)

- **Boston University / Groningen / Warwick / Oxford axis** (Balakrishnan, Müller, Dogra, Vonk, Tuitman): algorithmic quadratic Chabauty in `Magma`/`SageMath`, extension to non-hyperelliptic and higher-genus modular curves; "geometric quadratic Chabauty" of Edixhoven–Lido replaces Selmer varieties with explicit torsors under $\mathbb{G}_m^{\rho-1}$-bundles, making the method scheme-theoretic and easier to certify.
- **Refined Selmer schemes** (Betts, Dogra): imposing local conditions at bad primes shrinks $X(\mathbb{Q}_p)_n$ and gives effective bounds on $\\#X(\mathbb{Q}_p)_n$ in terms of reduction data. Betts' work on "the motivic anabelian geometry of local heights" gives uniform bounds on the number of points in $X(\mathbb{Q}_p)_2$. *(frontier — verify)*
- **Depth $\ge 3$ / polylogarithmic quotients** (Corwin, Dan-Cohen): explicit equations for $X(\mathbb{Q}_p)_n$ for $\mathbb{P}^1\setminus\{0,1,\infty\}$ using motivic multiple zeta values; the bottleneck is deciding when the Goncharov-type coordinates suffice.
- **Lawrence–Venkatesh descendants**: applications to $S$-unit and Shafarevich-type problems, and to uniform Mordell–Lang; effectivity remains out of reach.
- **Sieve-free termination**: work relating Kim's conjecture to Grothendieck's section conjecture (Betts–Kumpitsch–Lüdtke) shows locally geometric sections are controlled by the same Selmer tower. *(frontier — verify)*

## 8. Future Work

- Prove Kim's conjecture in depth $2$ for a single infinite family of curves, unconditionally.
- Establish $\dim \mathrm{Sel}_n = O(n^{\epsilon}\cdot\text{something sublinear in }\dim U_n)$ using known cases of Bloch–Kato (Soulé's theorem, Beilinson–Kato Euler systems).
- Extend quadratic Chabauty to number fields $K \neq \mathbb{Q}$ with $r$ large, where local conditions at real and complex places obstruct the current setup (Dogra's "unlikely intersections" framework).
- Combine Chabauty–Kim with explicit height bounds from Arakelov theory (Rémond, von Känel) to convert a *finite computable superset* into a *certified complete list*.
- Pursue effective ABC in restricted regimes (Elkies' reduction), which would give effective Mordell outright.

## 9. Key References

- **[Foundational]** G. Faltings. *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern.* Invent. Math. 73 (1983), 349–366.
- **[Foundational]** C. Chabauty. *Sur les points rationnels des courbes algébriques de genre supérieur à l'unité.* C. R. Acad. Sci. Paris 212 (1941), 882–885.
- **[Foundational]** R. Coleman. *Effective Chabauty.* Duke Math. J. 52 (1985), 765–770.
- **[Foundational]** M. Kim. *The motivic fundamental group of $\mathbb{P}^1\setminus\{0,1,\infty\}$ and the theorem of Siegel.* Invent. Math. 161 (2005), 629–656.
- **[Foundational]** M. Kim. *The unipotent Albanese map and Selmer varieties for curves.* Publ. RIMS 45 (2009), 89–133.
- **[SOTA]** J. Balakrishnan, N. Dogra. *Quadratic Chabauty and rational points I: p-adic heights.* Duke Math. J. 167 (2018), 1981–2038.
- **[SOTA]** J. Balakrishnan, N. Dogra, J. S. Müller, J. Tuitman, J. Vonk. *Explicit Chabauty–Kim for the split Cartan modular curve of level 13.* Ann. of Math. 189 (2019), 885–944.
- **[SOTA]** J. Balakrishnan, N. Dogra, J. S. Müller, J. Tuitman, J. Vonk. *Quadratic Chabauty for modular curves: algorithms and examples.* Compositio Math. 159 (2023), 1111–1152.
- **[SOTA]** B. Lawrence, A. Venkatesh. *Diophantine problems and p-adic period mappings.* Invent. Math. 221 (2020), 893–999.
- **[SOTA]** V. Dimitrov, Z. Gao, P. Habegger. *Uniformity in Mordell–Lang for curves.* Ann. of Math. 194 (2021), 237–298.
- **[SOTA]** E. Katz, J. Rabinoff, D. Zureick-Brown. *Uniform bounds for the number of rational points on curves of small Mordell–Weil rank.* Duke Math. J. 165 (2016), 3189–3240.
- **[SOTA]** B. Edixhoven, G. Lido. *Geometric quadratic Chabauty.* J. Inst. Math. Jussieu 22 (2023), 279–333.
- **[Related]** J. Coates, M. Kim. *Selmer varieties for curves with CM Jacobians.* Kyoto J. Math. 50 (2010), 827–852.
- **[Related]** Yu. Bilu, P. Parent. *Serre's uniformity problem in the split Cartan case.* Ann. of Math. 173 (2011), 569–584.
- **[Survey]** W. McCallum, B. Poonen. *The method of Chabauty and Coleman.* In *Explicit Methods in Number Theory*, Panor. Synthèses 36, SMF, 2012, 99–117.
- **[Survey]** J. Balakrishnan, A. Best, F. Bianchi, B. Lawrence, J. S. Müller, N. Triantafillou, J. Vonk. *Two recent p-adic approaches towards the (effective) Mordell conjecture.* In *Arithmetic L-Functions and Differential Geometric Methods*, Progr. Math. 338, Birkhäuser, 2021.
- **[Survey]** N. D. Elkies. *ABC implies Mordell.* Int. Math. Res. Not. 1991, no. 7, 99–109.

## 10. Worked Example / Concrete Special Case

**The cursed curve $X_s(13)$.** Take $X = X_s(13)$, the modular curve of level $13$ with split Cartan level structure. Its invariants:

- Genus $g = 3$; the curve is non-hyperelliptic, a plane quartic.
- Jacobian $J$ is isogenous to the new part $J_0(169)^{\text{new},+}$; Mordell–Weil rank $r = 3$.
- Picard number $\rho(J) = 3$, because $J$ has extra endomorphisms coming from Hecke operators (real multiplication by a cubic field).

**Step 1 — classical Chabauty fails.** The Chabauty condition is $r < g$, i.e. $3 < 3$: false. The space of annihilating differentials has dimension $g - \dim\overline{J(\mathbb{Q})} \ge g-r = 0$; generically zero, so there is no Coleman function to work with. Since $X_s(13)$ also covers no curve to which Baker's method applies and Runge's method does not apply at this level, all pre-2018 techniques stall.

**Step 2 — the quadratic Chabauty inequality.** Check Balakrishnan–Dogra's criterion:
$$r \;<\; g + \rho - 1 \quad \Longleftrightarrow \quad 3 \;<\; 3 + 3 - 1 = 5 \quad \checkmark$$
So $X(\mathbb{Q}_p)_2$ is finite. Concretely, the Selmer scheme in depth $2$ has dimension $r + (\rho - 1) = 3 + 2 = 5$ while the local target $U_2^{\mathrm{dR}}/F^0$ has dimension $g + (\rho - 1) + 1 = 3+2+1 = 6$; the codimension-$1$ gap yields one nontrivial equation on $X(\mathbb{Q}_p)$.

**Step 3 — the height equation.** For a correspondence $Z \in \mathrm{NS}(J)$ not a multiple of the theta divisor, one obtains a locally analytic function
$$\rho_Z(z) \;=\; h_p(z) - \sum_{v\mid 13} h_v(z),$$
where $h_p$ is a double Coleman integral and the finitely many possible values of $h_v$ at $v=13$ are read off the special fibre of a regular model. Rationality forces $\rho_Z(z)$ to lie in the *finite* set $\{\text{values of } \sum_v h_v\}$ for every $z \in X(\mathbb{Q})$, cutting the $p$-adic points down to a finite list.

**Step 4 — output.** Running this at a good prime of small residue degree and intersecting the loci from two independent classes $Z_1, Z_2$ produces exactly seven $p$-adic solutions, each of which is recognised as a rational point:
$$\\#X_s(13)(\mathbb{Q}) = 7,$$
all of them cusps or CM points. Combined with the analogous results at levels $\le 13$, this closes the split Cartan case of Serre's uniformity problem.

**What this does *not* give.** The computation certifies completeness for *this* curve, but the input $r=3$, $\rho=3$ and the explicit Mordell–Weil generators were found by descent, and the bound produced is on the $p$-adic locus, not on the height of a hypothetical missed point. That is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*