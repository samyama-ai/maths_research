---
id: 08-logic-set-theory/kaplansky-group-ring-conjecture
title: "Kaplansky Group Ring Conjecture"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kaplansky Group Ring Conjecture

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/kaplansky-group-ring-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $G$ be a **torsion-free** group and $K$ a field. Kaplansky's group ring conjectures assert three properties of the group algebra $K[G]$:

- **(U) Unit conjecture.** Every unit of $K[G]$ is *trivial*: of the form $\lambda g$ with $\lambda \in K^\times$, $g \in G$.
- **(Z) Zero-divisor conjecture.** $K[G]$ is a domain: $\alpha\beta = 0$ with $\alpha,\beta \in K[G]$ forces $\alpha = 0$ or $\beta = 0$.
- **(I) Idempotent conjecture.** The only idempotents of $K[G]$ are $0$ and $1$.

For torsion-free $G$ one has the implications $\mathrm{(U)} \Rightarrow \mathrm{(Z)} \Rightarrow \mathrm{(I)}$; none of the reverse implications is known.

Torsion-freeness is necessary: if $g \in G$ has order $n > 1$, then $(1-g)(1+g+\cdots+g^{n-1}) = 0$, and when $\mathrm{char}\,K \nmid n$ the element $\tfrac1n\sum_{i<n} g^i$ is a nontrivial idempotent.

**Status.** (U) is **false**: Gardam (2021) exhibited a nontrivial unit in $\mathbb{F}_2[P]$ for the torsion-free Promislow group $P$. (Z) and (I) remain open in general. A complete resolution of (Z) means either a proof for all torsion-free $G$ and all fields $K$, or one explicit pair $\alpha\beta = 0$ with $\alpha,\beta \neq 0$.

## 2. Mathematical Foundations

**Group ring.** For a ring $R$ and group $G$, $R[G]$ is the free $R$-module on $G$ with multiplication extending that of $G$:
$$\alpha = \sum_{g\in G}\alpha_g\, g,\qquad \alpha\beta = \sum_{h \in G}\Big(\sum_{g\in G}\alpha_g \beta_{g^{-1}h}\Big) h ,$$
all sums finite. The **support** is $\operatorname{supp}(\alpha) = \{g : \alpha_g \neq 0\}$, and $|\operatorname{supp}(\alpha)|$ is the *length*.

**Trivial units.** $U(K[G]) \supseteq K^\times \times G$; (U) says equality holds.

**Unique product property.** $G$ has the *unique product property* (u.p.) if for all finite nonempty $A,B \subseteq G$ there is $c \in AB$ with a unique factorization $c = ab$, $a\in A$, $b\in B$. If $G$ is u.p. then for $\alpha,\beta \neq 0$ the coefficient of that $c$ in $\alpha\beta$ is $\alpha_a\beta_b \neq 0$, so
$$G \text{ u.p.} \;\Longrightarrow\; K[G] \text{ is a domain with only trivial units.}$$
*Two-unique-products* (t.u.p., two such $c$ when $|A|+|B| \ge 3$) is equivalent to u.p. (Strojnowski).

**Orderability.** $G$ bi-orderable or left-orderable $\Rightarrow$ u.p.; locally indicable $\Rightarrow$ left-orderable. Higman (1940) proved (U) for locally indicable $G$ over any integral domain with only trivial units.

**Analytic route to (I).** For $G$ torsion-free discrete, the Baum–Connes assembly map
$$\mu: K_*^{G}(\underline{E}G) \longrightarrow K_*(C^*_r G)$$
being *rationally surjective* implies the Kadison–Kaplansky conjecture: $C^*_r G$, hence $\mathbb{C}[G]$, has no idempotent $\neq 0,1$. The mechanism is the canonical trace $\tau(\sum \alpha_g g) = \alpha_1$, which is faithful and positive on $C_r^*G$; surjectivity forces $\tau(e) \in \mathbb{Z}$ for idempotents $e$, and $0 \le \tau(e) \le 1$ with $\tau(e) \in \{0,1\}$ gives $e \in \{0,1\}$.

**Promislow group.** $P = \langle a,b \mid a^{-1}b^2a = b^{-2},\; b^{-1}a^2b = a^{-2}\rangle$, the fundamental group of the Hantzsche–Wendt flat $3$-manifold. It is torsion-free crystallographic, contains the central subgroup $\mathbb{Z}^3 = \langle x,y,z\rangle$ with $x=a^2,\, y=b^2,\, z=(ab)^2$ of index $4$, and $P/\mathbb{Z}^3 \cong (\mathbb{Z}/2)^2$ with coset representatives $1, a, b, ab$. Promislow (1988) showed $P$ is not u.p.

## 3. History & State of the Art (SOTA)

- **1940.** Higman's thesis and *The units of group-rings* prove (U) for locally indicable groups; the origin of the trivial-units question.
- **1950s–60s.** Kaplansky circulates the conjectures; they are recorded in his 1970 *Problems in the theory of rings revisited* (Amer. Math. Monthly).
- **1976–1980.** Farkas–Snider prove (Z) for torsion-free polycyclic-by-finite groups in characteristic $0$; Cliff extends to characteristic $p$.
- **1987–88.** Rips–Segev construct the first torsion-free non-u.p. group; Promislow gives the small crystallographic example $P$. This severs the u.p. method from the general conjecture.
- **1988.** Kropholler–Linnell–Moody: (Z) for torsion-free elementary amenable groups over fields of characteristic $0$.
- **1993–2002.** Linnell's division-ring theorem links the strong Atiyah conjecture to (Z); Higson–Kasparov (a-T-menable groups) and Lafforgue (hyperbolic groups, $\mathrm{SL}_3$ lattices) give large Baum–Connes classes, hence (I) over $\mathbb{C}$.
- **2021.** **Gardam disproves (U)**: a unit $\alpha\beta = 1$ in $\mathbb{F}_2[P]$ with $|\operatorname{supp}\alpha| = |\operatorname{supp}\beta| = 21$, found by SAT/computer search over the $4$ cosets of $\mathbb{Z}^3$ (Annals of Math. 194).
- **2021–.** Murray produces counterexamples over $\mathbb{F}_p$ for further primes; Gardam and others report units in characteristic $0$ *(frontier — verify)*. (Z) and (I) survive intact — no known counterexample multiplies to $0$.

## 4. Partial Results / Verified Cases

**(Z) and (U) proved for:**

| Class | Field/coefficients | Source |
|---|---|---|
| Locally indicable (incl. free, free-by-free, one-relator torsion-free) | any domain with trivial units | Higman 1940 |
| Left-orderable, bi-orderable, u.p. groups | any field | u.p. argument |
| Torsion-free polycyclic-by-finite | $\mathrm{char}\,K = 0$ | Farkas–Snider 1976 |
| Torsion-free polycyclic-by-finite | $\mathrm{char}\,K = p$ | Cliff 1980 |
| Torsion-free elementary amenable | $\mathrm{char}\,K = 0$ | Kropholler–Linnell–Moody 1988 |
| Groups in Linnell's class $\mathcal{C}$ with bounded finite-subgroup order (extensions of free by elementary amenable) | $\mathbb{C}$ | Linnell 1993 |
| Torsion-free groups satisfying the strong Atiyah conjecture | $\mathbb{C}$ | Linnell's criterion |

**(I) only, via $K$-theory over $\mathbb{C}$:** torsion-free a-T-menable (Haagerup property) groups — Higson–Kasparov 2001; torsion-free hyperbolic groups and cocompact lattices in $\mathrm{Sp}(n,1)$, $\mathrm{SL}_3(\mathbb{Q}_p)$ — Lafforgue 2002.

**(U) verified computationally** for supersoluble group algebras over $\mathbb{F}_2$ up to prescribed support sizes (Craven–Pappas 2013): no nontrivial unit of length $\le 3$ in any $K[G]$, and support-size searches in $\mathbb{F}_2[P]$ up to length $20$ found nothing — Gardam's counterexample sits at exactly length $21$.

**Related settled case.** Kaplansky's *direct finiteness* conjecture ($\alpha\beta = 1 \Rightarrow \beta\alpha = 1$) holds for all sofic groups over any field (Elek–Szabó 2004).

## 5. Principal Obstacles

- **Loss of the ordering method.** Every general proof of (Z)/(U) proceeds through u.p. or an ordering. Rips–Segev and Promislow show torsion-free $\not\Rightarrow$ u.p., and $P$ — the smallest such example — is exactly where (U) fails. The combinatorial technique has no successor.
- **No invariant separates the cases.** For $K$ a field of positive characteristic there is no trace with values in $\mathbb{R}$ and no $K$-theoretic assembly map; the analytic proof of (I) over $\mathbb{C}$ (positivity of $\tau$) has no algebraic analogue over $\mathbb{F}_p$.
- **Baum–Connes is not universal and does not give (Z).** Even where $\mu$ is an isomorphism it yields idempotent-freeness, not the absence of zero divisors, because $C^*_r G$ is never a domain in the relevant sense — passing back to $\mathbb{C}[G]$ loses information.
- **Amenability/growth barriers.** The strong Atiyah conjecture is open for groups with unbounded finite subgroups and fails for Lamplighter-type groups (Grigorchuk–Żuk, Austin), so Linnell's route cannot be pushed to all torsion-free groups.
- **Search space.** A putative zero divisor is a solution of a bilinear system over $K$ with unknown support in an infinite group. Gardam's SAT search was feasible only because $P$ has a rank-$3$ abelian subgroup of index $4$; no comparable finite reduction exists for e.g. Burnside-type or Tarski-monster-like torsion-free groups.

## 6. The Gap

Proven: (Z) for torsion-free groups admitting either (i) an ordering / u.p. structure, or (ii) an elementary-amenable or Atiyah-conjecture-controlled decomposition. Conjectured: (Z) for *all* torsion-free $G$.

The exact barrier is the class of torsion-free non-u.p. groups with no orderable or amenable structure — the Rips–Segev/Promislow zone. Gardam's unit proves this zone is genuinely different, not merely technically hard: the multiplicative structure of $K[P]$ admits nontrivial invertibles. The open step is to decide whether the phenomenon that produces a unit ($\alpha\beta = 1$) can be tuned to produce $\alpha\beta = 0$ with both factors nonzero, or whether some conserved quantity (a $K$-theoretic class, an $L^2$-Betti number, a Følner-type dimension) forbids it. No candidate invariant is currently known that is defined over all fields and all torsion-free groups.

## 7. Current Research (as of June 2026)

- **Extending Gardam's counterexample.** Murray (arXiv 2021) produced units in $\mathbb{F}_p[P]$ for further primes; Gardam has reported nontrivial units in group rings over fields of characteristic $0$, including complex coefficients *(frontier — verify)*. If confirmed, this rules out any characteristic-$0$-specific proof of (U).
- **SAT/SMT and computer algebra searches.** Groups at Münster (Gardam), Bonn, and Newcastle run constraint solvers over torsion-free crystallographic and Bieberbach groups, searching for zero divisors and idempotents rather than units; nothing found to date.
- **$L^2$-invariants and Atiyah conjecture.** Jaikin-Zapirain's approximation and base-change results (GAFA 2019) push the strong Atiyah conjecture through free-by-\{elementary amenable\} and locally indicable classes, widening the (Z)-verified list.
- **Hyperbolic and CAT(0) groups.** Positive results on (I) via Lafforgue's Banach $KK$-theory; (Z) for torsion-free hyperbolic groups remains open and is regarded as the most tractable major target.
- **Model-theoretic and logical angles.** Whether (Z) is decidable for finitely presented torsion-free groups, and whether a counterexample could be independent of ZFC, are occasionally raised but there is no formal independence result.

## 8. Future Work

1. **Decide (Z) for the Promislow group.** $\mathbb{F}_2[P]$ is now known to be non-domain-like in the unit sense; exhaustive support-bounded search for zero divisors in $\mathbb{F}_2[P]$ is the sharpest available experiment.
2. **Find a field-independent obstruction.** Seek a trace-like or $K$-theoretic invariant defined over $\mathbb{F}_p$ that reproduces the $\tau(e)\in\{0,1\}$ argument.
3. **Torsion-free hyperbolic groups.** Combine Lafforgue's (I) with a domain criterion; a proof of (Z) here would be the first large non-amenable, non-orderable class.
4. **Structure of Gardam's unit.** Understand the $\mathbb{Z}^3\rtimes(\mathbb{Z}/2)^2$ coset algebra conceptually rather than by search, aiming for a family of counterexamples parameterized by crystallographic data.
5. **Direct finiteness beyond sofic groups.** Since sofic-ness is unresolved for all groups, deciding Kaplansky direct finiteness for a non-sofic candidate would sharpen the whole picture.

## 9. Key References

- **[Foundational]** G. Higman. *The units of group-rings.* Proc. London Math. Soc. (2) **46** (1940), 231–248.
- **[Foundational]** I. Kaplansky. *Problems in the theory of rings revisited.* American Mathematical Monthly **77** (1970), 445–454.
- **[Foundational]** D. S. Passman. *The Algebraic Structure of Group Rings.* Wiley-Interscience, 1977.
- **[SOTA / Recent]** G. Gardam. *A counterexample to the unit conjecture for group rings.* Annals of Mathematics **194** (2021), no. 3, 967–979.
- **[SOTA / Recent]** A. G. Murray. *More counterexamples to the unit conjecture for group rings.* arXiv preprint, 2021.
- **[Structural]** S. D. Promislow. *A simple example of a torsion-free, non-unique product group.* Bulletin of the London Mathematical Society **20** (1988), 302–304.
- **[Structural]** E. Rips, Y. Segev. *Torsion-free group without unique product property.* Journal of Algebra **108** (1987), 116–126.
- **[Partial results]** D. R. Farkas, R. L. Snider. *$K_0$ and Noetherian group rings.* Journal of Algebra **42** (1976), 192–198.
- **[Partial results]** G. H. Cliff. *Zero divisors and idempotents in group rings.* Canadian Journal of Mathematics **32** (1980), 596–602.
- **[Partial results]** P. H. Kropholler, P. A. Linnell, J. A. Moody. *Applications of a new K-theoretic theorem to soluble group rings.* Proc. Amer. Math. Soc. **104** (1988), 675–684.
- **[Partial results]** P. A. Linnell. *Division rings and group von Neumann algebras.* Forum Mathematicum **5** (1993), 561–576.
- **[Analytic]** N. Higson, G. Kasparov. *E-theory and KK-theory for groups which act properly and isometrically on Hilbert space.* Inventiones Mathematicae **144** (2001), 23–74.
- **[Analytic]** V. Lafforgue. *K-théorie bivariante pour les algèbres de Banach et conjecture de Baum–Connes.* Inventiones Mathematicae **149** (2002), 1–95.
- **[Computational]** D. A. Craven, P. Pappas. *On the unit conjecture for supersoluble group algebras.* Journal of Algebra **394** (2013), 310–356.
- **[Related]** G. Elek, E. Szabó. *Sofic groups and direct finiteness.* Journal of Algebra **280** (2004), 426–434.
- **[Survey]** G. Gardam. *Kaplansky's conjectures.* Survey article, European Congress of Mathematics proceedings, 2023.

## 10. Worked Example / Concrete Special Case

**(a) The conjecture holds for $G=\mathbb{Z}$.** Here $K[\mathbb{Z}] = K[t,t^{-1}]$. Write $\alpha = \sum_{i=m}^{M}\alpha_i t^i$ with $\alpha_m,\alpha_M \neq 0$, and similarly $\beta$ with degrees $n \le N$. Then
$$\alpha\beta = \alpha_m\beta_n\,t^{m+n} + \cdots + \alpha_M\beta_N\,t^{M+N},$$
and since $K$ is a field the extreme coefficients are nonzero. Hence $\alpha\beta \neq 0$ (proving (Z)), and $\alpha\beta = 1$ forces $m+n = M+N = 0$, so $m=M$, $n=N$: both factors are monomials $\lambda t^m$ (proving (U)). This *ordering* argument is exactly what fails once $G$ is not u.p.

**(b) $P$ is not a unique product group.** In $P$ take the $14$-element set
$$S = \{1,\,a,\,b,\,ab,\,a^{-1},\,b^{-1},\,\dots\}$$
Promislow's explicit $14$-element set $S \subset P$ satisfies: every $c \in S\cdot S$ has at least two factorizations $c = s_1 s_2$, $s_i \in S$. The obstruction comes from the relations $a^{-1}b^2a = b^{-2}$ and $b^{-1}a^2b=a^{-2}$, which make the action of $P/\mathbb{Z}^3 \cong (\mathbb{Z}/2)^2$ on $\mathbb{Z}^3=\langle x,y,z\rangle$ by the diagonal sign matrices
$$a: (x,y,z)\mapsto (x,y^{-1},z^{-1}),\qquad b: (x,y,z)\mapsto(x^{-1},y,z^{-1}),$$
so products in different cosets fold onto each other and no "extremal" term survives.

**(c) Gardam's unit.** Decompose $\alpha \in \mathbb{F}_2[P]$ along the four cosets, $\alpha = p + qa + rb + s\,ab$ with $p,q,r,s \in \mathbb{F}_2[\mathbb{Z}^3]$:
$$p = (1+x)(1+y)(1+z^{-1}),\qquad q = x^{-1}y^{-1} + x + y^{-1}z + z,$$
$$r = 1 + x + y^{-1}z + xyz,\qquad s = 1 + (x + x^{-1} + y + y^{-1})z^{-1}.$$
Support sizes are $8 + 4 + 4 + 5 = 21$. Setting $\beta = x^{-1}p^{*} + \cdots$ (the mirrored element given in Gardam 2021, also of length $21$), one verifies $\alpha\beta = 1$ by expanding the four coset components and using the twisted commutation $g\cdot u = u^{\sigma(g)}\cdot g$ for $u\in\mathbb{Z}^3$; every non-identity monomial cancels in pairs over $\mathbb{F}_2$. This is a *nontrivial* unit since $|\operatorname{supp}\alpha| = 21 > 1$, refuting (U).

**What it does not do.** $\alpha$ is invertible, hence not a zero divisor, and $\alpha \neq \alpha^2$, so neither (Z) nor (I) is touched. That is the exact shape of the current gap.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*