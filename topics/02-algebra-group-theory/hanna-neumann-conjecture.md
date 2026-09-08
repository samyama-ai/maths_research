---
id: 02-algebra-group-theory/hanna-neumann-conjecture
title: "Hanna Neumann Conjecture"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hanna Neumann Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/hanna-neumann-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $F$ be a free group and let $U, V \le F$ be finitely generated subgroups. Write $r(H)$ for the rank of a free group $H$ and define the **reduced rank**
$$\bar{r}(H) \;=\; \max\{\,r(H) - 1,\; 0\,\}.$$

**Hanna Neumann Conjecture (HNC), 1957.**
$$\bar{r}(U \cap V) \;\le\; \bar{r}(U)\,\bar{r}(V).$$

**Strengthened Hanna Neumann Conjecture (SHNC), W. Neumann 1990.** Summing over the double cosets of $(U,V)$ in $F$,
$$\sum_{UxV \,\in\, U\backslash F/V} \bar{r}\bigl(U \cap xVx^{-1}\bigr) \;\le\; \bar{r}(U)\,\bar{r}(V).$$

Both statements are now **theorems**: HNC and SHNC were proved independently by Igor Mineyev (Annals of Mathematics, 2012) and Joel Friedman (Memoirs of the AMS, 2015). The problem is retained in the catalog because (i) the proofs are non-elementary and no combinatorial/graph-theoretic proof in the style originally sought is known, and (ii) the natural generalizations — to free products (Kurosh rank), limit groups, right-angled Artin groups, one-relator groups with non-positive immersions, and pro-$p$ analogues — remain open or only partially settled.

A complete resolution of a generalized version requires either a proof of the corresponding inequality for the stated class of groups, or an explicit pair of subgroups violating it.

## 2. Mathematical Foundations

**Free groups and Nielsen–Schreier.** Every subgroup $H \le F$ is free; if $[F:H] = n < \infty$ then $r(H) - 1 = n\,(r(F) - 1)$, i.e. $\bar r(H) = n \cdot \bar r(F)$.

**Howson's theorem (1954).** If $U, V \le F$ are finitely generated, so is $U \cap V$; hence $\bar r(U\cap V)$ is finite and the question is quantitative.

**Graph model (Stallings, 1983).** Fix a wedge of $r$ circles $R_r$ with $\pi_1(R_r) = F$. A finitely generated $U \le F$ corresponds to a finite connected **core graph** $\Gamma_U$ with an immersion $\Gamma_U \to R_r$ (a locally injective, edge-label-preserving map), unique up to isomorphism, with $\pi_1(\Gamma_U) = U$. For a finite connected graph $\Gamma$,
$$\bar r(\Gamma) \;=\; -\chi(\Gamma) \;=\; |E(\Gamma)| - |V(\Gamma)|,$$
where $\chi$ is the Euler characteristic. For a graph with components $\Gamma_i$, set $\bar r(\Gamma) = \sum_i \max\{-\chi(\Gamma_i), 0\}$, discarding trees.

**Fiber product.** The pullback $\Gamma_U \times_{R_r} \Gamma_V$ has vertices $V(\Gamma_U)\times V(\Gamma_V)$ and edges the label-matched pairs. Its non-tree components are in bijection with the double cosets $UxV$ for which $U \cap xVx^{-1} \ne 1$, the component fundamental groups being conjugates of these intersections. So SHNC is exactly
$$\bar r\bigl(\Gamma_U \times_{R_r} \Gamma_V\bigr) \;\le\; \bar r(\Gamma_U)\,\bar r(\Gamma_V),$$
a purely graph-theoretic statement: the naive count gives $-\chi$ of the pullback $= (-\chi_U)(-\chi_V) \cdot$ (a correction), and the difficulty is entirely in discarding tree components efficiently.

**Mineyev's submultiplicativity.** Mineyev's proof constructs, for the free group $\Gamma$, a $\Gamma$-equivariant "deep-fall / atomic decomposition" structure on $\ell^2(\Gamma)$-modules yielding a submultiplicative function
$$\dim_{\Gamma}\!\left(\,\overline{A \cdot B}\,\right) \;\le\; \dim_\Gamma(A)\,\dim_\Gamma(B)$$
for suitable Hilbert $\Gamma$-modules, with von Neumann dimension replacing rank. Applied to the modules attached to $U$ and $V$ this yields SHNC.

**Approximation route (Jaikin-Zapirain).** Reduced rank is recovered as a first $\ell^2$-Betti number: for $H \le F$ finitely generated,
$$\bar r(H) \;=\; b_1^{(2)}(H) \;=\; \lim_{n} \frac{b_1(H_n)}{[H:H_n]}$$
along a chain of finite-index subgroups (Lück approximation), which converts SHNC into a statement about ranks in finite-index approximations.

## 3. History & State of the Art (SOTA)

- **1954.** A. G. Howson proves finite generation of $U\cap V$, with the bound $r(U\cap V) \le 2 r(U) r(V) - r(U) - r(V) + 1$.
- **1957.** Hanna Neumann proves $\bar r(U\cap V) \le 2\,\bar r(U)\bar r(V)$ and conjectures the factor $2$ can be removed; her Addendum (1958) notes she cannot even exclude $\bar r(U\cap V) = 0$ forcing structure.
- **1971.** R. G. Burns improves to $\bar r(U\cap V) \le 2\bar r(U)\bar r(V) - \min\{\bar r(U),\bar r(V)\}$.
- **1983.** Stallings' folding calculus turns the problem into finite graph combinatorics; Gersten (1983) gives a topological proof of Burns' bound.
- **1990.** W. D. Neumann formulates SHNC and shows it is implied by, and refines, HNC; he also observes the bound is attained (equality cases exist for every $\bar r(U),\bar r(V)$).
- **1992–1994.** Tardos proves SHNC when $\bar r(U) = 2$; Dicks reduces SHNC to the purely combinatorial **Amalgamated Graph Conjecture**.
- **2001–2002.** Dicks–Formanek settle $\min\{\bar r(U),\bar r(V)\} \le 3$; Khan and, independently, Meakin–Weil prove HNC when one subgroup is positively generated.
- **2011–2012.** Mineyev proves SHNC (hence HNC) via $\ell^2$/submultiplicativity; Friedman proves it via sheaves on graphs and his "maximum excess" invariant. Dicks extracts a short combinatorial reformulation ("Simplified Mineyev").
- **2017–2022.** Jaikin-Zapirain gives an approximation-theoretic proof and framework; Antolín–Jaikin-Zapirain prove the analogue for surface groups.

## 4. Partial Results / Verified Cases

Cases proved before the general theorem, still the sharpest elementary statements:

| Case | Result | Source |
|---|---|---|
| General $U,V$ | $\bar r(U\cap V) \le 2\bar r(U)\bar r(V)$ | H. Neumann 1957 |
| General $U,V$ | $\le 2\bar r(U)\bar r(V) - \min\{\bar r(U),\bar r(V)\}$ | Burns 1971 |
| $\bar r(U) = 1$ (i.e. $r(U)=2$) | HNC and SHNC hold | Neumann/Imrich, 1970s |
| $\bar r(U) = 2$ | SHNC holds | Tardos 1992 |
| $\bar r(U) = 3$ | SHNC holds | Dicks–Formanek 2001 |
| $U$ positively generated | HNC holds | Khan 2002; Meakin–Weil 2002 |
| $U, V$ of finite index | Equality $\bar r(U\cap V) = \bar r(U)\bar r(V)$ when $UV = F$ | Nielsen–Schreier count |
| $F$ replaced by a surface group | SHNC analogue holds | Antolín–Jaikin-Zapirain 2022 |
| Free products, Kurosh rank | SHNC-type bounds in many cases | Ivanov 2008 onwards |

Equality is attained for arbitrarily large parameters, so no constant $c<1$ improvement $\bar r(U\cap V)\le c\,\bar r(U)\bar r(V)$ is possible.

## 5. Principal Obstacles

- **Tree components dominate.** In the fiber product $\Gamma_U\times_{R_r}\Gamma_V$ the crude count $|E| - |V| = \bar r(U)\bar r(V) + (\text{slack})$ is correct only if one can prove that enough components are trees. There is no local rule that identifies these; the trees are determined by global cancellation patterns in $F$, so induction on edges or folds does not close.
- **Failure of naive combinatorics.** Burns-type arguments delete one edge at a time and lose a factor of $2$; Dicks showed the residual combinatorial content (the Amalgamated Graph Conjecture) is as hard as SHNC itself, and it resisted for two decades.
- **Non-constructive analytic input.** Mineyev's proof relies on an equivariant ordering / "deep-fall" structure on $\ell^2(F)$ that is specific to free groups and does not transport to other groups without a substitute for the tree.
- **No linear-programming certificate.** Attempts to certify the inequality via LP duality or flows on the pullback graph produce fractional relaxations whose optimum is $2\bar r\bar r$, exactly the Burns barrier.
- **Generalizations lack the tree.** For limit groups, RAAGs and one-relator groups, the Stallings graph is replaced by a complex where immersions need not be $\pi_1$-injective and Euler characteristic is not additive over the pullback, so the whole bookkeeping collapses.

## 6. The Gap

For free groups there is no gap: SHNC $\Rightarrow$ HNC is a theorem. The remaining gaps are:

1. **Combinatorial proof.** No proof of the Amalgamated Graph Conjecture (Dicks 1994) is known by graph-combinatorial means alone; every extant proof passes through $\ell^2$-dimensions, sheaf cohomology, or approximation. The precise missing step is a *local* certificate that the sum of $-\chi$ over non-tree components of the pullback never exceeds the product.
2. **Beyond free groups.** For a group $G$ with a "rank-like" invariant $\bar r$, the general statement $\sum_{UxV} \bar r(U\cap xVx^{-1}) \le \bar r(U)\bar r(V)$ is proved for free groups and surface groups; it is open for limit groups in general, for RAAGs, and for one-relator groups with non-positive immersions. The barrier is the absence of a submultiplicative Hilbert-module structure analogous to Mineyev's.

## 7. Current Research (as of June 2026)

- **Approximation and $\ell^2$-invariants.** Jaikin-Zapirain's Duke (2017) framework reduces HNC-type statements to Lück approximation plus a "strong Atiyah"-style property; groups in the class $\mathcal{C}$ of "$\ell^2$-approximable" groups inherit the inequality. Madrid (ICMAT/UAM) is the main centre.
- **Surface and limit groups.** Antolín–Jaikin-Zapirain (Compositio 2022) settled surface groups; extending to limit groups and to hyperbolic groups with a suitable Euler-characteristic invariant is active *(frontier — verify)*.
- **Non-positive immersions.** Wise's programme, with results of Helfer–Wise and Louder–Wilton on one-relator groups, produces Euler-characteristic inequalities of Hanna Neumann flavour for one-relator complexes; the exact HNC analogue there is open *(frontier — verify)*.
- **Pro-$p$ and profinite analogues.** Work on Hanna Neumann-type formulas for free pro-$p$ groups continues, with partial statements under $p$-adic analytic hypotheses *(frontier — verify)*.
- **Kurosh rank in free products.** Ivanov's programme gives SHNC-type inequalities for intersections in free products; sharp constants for general factor sets remain open.

## 8. Future Work

- Find a genuinely combinatorial (or linear-programming) proof of the Amalgamated Graph Conjecture, giving an elementary route to SHNC.
- Classify all equality cases: characterize pairs $(U,V)$ with $\sum \bar r(U\cap xVx^{-1}) = \bar r(U)\bar r(V)$; only sporadic families are described.
- Develop an axiomatic "Hanna Neumann property" for groups with a well-behaved $\ell^2$-Euler characteristic, and test it against RAAGs and limit groups.
- Effective/algorithmic side: sharp complexity bounds for computing $\bar r(U\cap V)$ from Stallings graphs, and average-case behaviour for random $U,V$.
- Explore whether Friedman's sheaf-theoretic maximum excess yields new invariants for graph immersions beyond the free-group case.

## 9. Key References

- **[Foundational]** A. G. Howson. *On the intersection of finitely generated free groups.* Journal of the London Mathematical Society 29 (1954), 428–434.
- **[Foundational]** H. Neumann. *On the intersection of finitely generated free groups.* Publicationes Mathematicae Debrecen 4 (1957), 186–189; Addendum, ibid. 5 (1958), 128.
- **[Foundational]** R. G. Burns. *On the intersection of finitely generated subgroups of a free group.* Mathematische Zeitschrift 119 (1971), 121–130. [DOI](https://doi.org/10.1007/bf01109964)
- **[Foundational]** J. R. Stallings. *Topology of finite graphs.* Inventiones Mathematicae 71 (1983), 551–565.
- **[Foundational]** W. D. Neumann. *On intersections of finitely generated subgroups of free groups.* In: Groups—Canberra 1989, Lecture Notes in Mathematics 1456, Springer, 1990, 161–170. [DOI](https://doi.org/10.1007/bfb0100737)
- **[Partial]** G. Tardos. *On the intersection of subgroups of a free group.* Inventiones Mathematicae 108 (1992), 29–36. [DOI](https://doi.org/10.1007/bf02100597)
- **[Partial]** W. Dicks. *Equivalence of the strengthened Hanna Neumann conjecture and the amalgamated graph conjecture.* Inventiones Mathematicae 117 (1994), 373–389. [DOI](https://doi.org/10.1007/bf01232249)
- **[Partial]** W. Dicks, E. Formanek. *The rank three case of the Hanna Neumann conjecture.* Journal of Group Theory 4 (2001), 113–151. [DOI](https://doi.org/10.1515/jgth.2001.012)
- **[Partial]** J. Meakin, P. Weil. *Subgroups of free groups: a contribution to the Hanna Neumann conjecture.* Geometriae Dedicata 94 (2002), 33–43. [DOI](https://doi.org/10.1023/a:1020900823482)
- **[SOTA]** I. Mineyev. *Submultiplicativity and the Hanna Neumann conjecture.* Annals of Mathematics 175 (2012), 393–414. [DOI](https://doi.org/10.4007/annals.2012.175.1.11)
- **[SOTA]** J. Friedman. *Sheaves on Graphs, Their Homological Invariants, and a Proof of the Hanna Neumann Conjecture.* Memoirs of the American Mathematical Society 233, no. 1100, 2015.
- **[SOTA]** A. Jaikin-Zapirain. *Approximation by subgroups of finite index and the Hanna Neumann conjecture.* Duke Mathematical Journal 166 (2017), 1955–1987. [DOI](https://doi.org/10.1215/00127094-0000015x)
- **[SOTA]** Y. Antolín, A. Jaikin-Zapirain. *The Hanna Neumann conjecture for surface groups.* Compositio Mathematica 158 (2022). [DOI](https://doi.org/10.1112/s0010437x22007709)
- **[Survey]** R. P. Kent IV. *Intersections and joins of free groups.* Algebraic & Geometric Topology 9 (2009), 305–325. [DOI](https://doi.org/10.2140/agt.2009.9.305)
- **[Survey]** W. Dicks. *Simplified Mineyev.* Preprint, 2011 (author's webpage, Universitat Autònoma de Barcelona).

## 10. Worked Example / Concrete Special Case

Take $F = F(a,b)$, so $r(F)=2$, $\bar r(F) = 1$. Define two homomorphisms onto $\mathbb{Z}/2$:
$$\varphi(a)=1,\ \varphi(b)=0; \qquad \psi(a)=0,\ \psi(b)=1,$$
and set $U = \ker\varphi$, $V = \ker\psi$.

**Ranks.** Both have index $2$, so by Nielsen–Schreier $r(U) - 1 = 2\cdot(2-1) = 2$, giving $r(U)=3$ and $\bar r(U) = 2$; likewise $\bar r(V)=2$. Explicitly $U = \langle a^2,\ b,\ aba^{-1}\rangle$.

**Stallings graphs.** $\Gamma_U$ has vertices $\{0,1\} = \mathbb{Z}/2$, $a$-edges $0\to 1$ and $1\to 0$, and $b$-loops at $0$ and at $1$: $|V|=2$, $|E|=4$, so $\bar r = 4-2 = 2$. ✓ Similarly for $\Gamma_V$ with the roles of $a,b$ swapped.

**Fiber product.** $\Gamma_U\times_{R_2}\Gamma_V$ has vertex set $\mathbb{Z}/2\times\mathbb{Z}/2$ (4 vertices). Label-matching gives exactly $4$ $a$-edges and $4$ $b$-edges, so $|E| = 8$. The graph is connected, hence
$$\bar r\bigl(U\cap V\bigr) = |E| - |V| = 8 - 4 = 4 .$$

**Checking the conjecture.** $\bar r(U)\bar r(V) = 2\cdot 2 = 4$, so $\bar r(U\cap V) = 4 \le 4$: the bound is **attained with equality**. Directly, $U\cap V = \ker(\varphi\times\psi: F \to \mathbb{Z}/2\times\mathbb{Z}/2)$ has index $4$, so $r(U\cap V) - 1 = 4\cdot 1 = 4$, i.e. $r(U\cap V) = 5$. ✓

**SHNC check.** $U$ and $V$ are normal, so $U\cap xVx^{-1} = U\cap V$ for every $x$, and $UV = F$ means there is a single double coset. The SHNC sum is therefore $4 = \bar r(U)\bar r(V)$ — again equality.

Contrast with Burns' bound, which only yields $\bar r(U\cap V) \le 2\cdot2\cdot2 - 2 = 6$: the example shows the true value is $4$, and the family $U = \ker(F\to\mathbb{Z}/m)$, $V=\ker(F\to\mathbb{Z}/n)$ gives equality $\bar r(U\cap V) = mn = \bar r(U)\bar r(V)$ for all $m,n$, proving the Hanna Neumann bound is sharp.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*