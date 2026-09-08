---
id: 02-algebra-group-theory/kaplanskys-idempotent-conjecture
title: "Kaplansky's Idempotent Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kaplansky's Idempotent Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kaplanskys-idempotent-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Kaplansky).** Let $K$ be a field and let $G$ be a torsion-free group. Then the group ring $K[G]$ contains no idempotents other than $0$ and $1$.

An element $e \in K[G]$ is idempotent if $e^2 = e$. The torsion-free hypothesis is necessary: if $g \in G$ has finite order $n$ and $\operatorname{char} K \nmid n$, then
$$e = \frac{1}{n}\sum_{i=0}^{n-1} g^i$$
satisfies $e^2 = e$ and $e \notin \{0,1\}$.

A complete proof must handle all fields (all characteristics) and all torsion-free groups. A disproof requires exhibiting one torsion-free $G$, one field $K$, and one explicit $e \in K[G]$ with $e^2 = e$, $e \neq 0, 1$. The conjecture is open even for $K = \mathbb{Q}$ and even for $K = \mathbb{C}$.

## 2. Mathematical Foundations

**Group ring.** For a field $K$ and group $G$, $K[G]$ is the $K$-vector space with basis $G$ and multiplication extending that of $G$:
$$\Big(\sum_{g} a_g g\Big)\Big(\sum_h b_h h\Big) = \sum_{u} \Big(\sum_{gh=u} a_g b_h\Big) u ,$$
all sums having finite support $\operatorname{supp}(x) = \{g : a_g \neq 0\}$.

**Kaplansky trace.** Define the $K$-linear functional $\operatorname{tr}: K[G] \to K$, $\operatorname{tr}\big(\sum a_g g\big) = a_1$. It is a trace: $\operatorname{tr}(xy) = \operatorname{tr}(yx)$.

**The conjecture hierarchy.** For torsion-free $G$ and a field $K$:
$$\textbf{(U) units conjecture} \implies \textbf{(Z) zero-divisor conjecture} \implies \textbf{(I) idempotent conjecture}.$$
(U): every unit of $K[G]$ is *trivial*, i.e. of the form $\lambda g$. (Z): $K[G]$ has no zero divisors. (Z) $\Rightarrow$ (I) because $e(1-e) = 0$ forces $e \in \{0,1\}$ in a domain.

**Analytic setting.** For $K \subseteq \mathbb{C}$, embed $\mathbb{C}[G] \hookrightarrow C^*_r(G) \subseteq \mathcal{N}(G) \subseteq B(\ell^2 G)$, where $C^*_r(G)$ is the reduced group $C^*$-algebra and $\mathcal{N}(G)$ the group von Neumann algebra. The trace extends to the faithful, positive, normal trace $\tau(x) = \langle x\delta_1, \delta_1\rangle$, so $\tau(x^*x) = \sum_g |a_g|^2 \geq 0$ with equality only for $x = 0$.

**Theorem (Kaplansky, 1969).** If $e \in \mathbb{C}[G]$ is idempotent then $\tau(e) \in \mathbb{R}$ and $0 \le \tau(e) \le 1$, with $\tau(e) = 0 \iff e = 0$ and $\tau(e)=1 \iff e = 1$.

Hence, in characteristic $0$, (I) is *equivalent* to the **Kaplansky trace conjecture**: $\operatorname{tr}(e) \in \{0,1\}$ for every idempotent.

**Theorem (Zalesskii, 1972).** For any field $K$ and any idempotent $e \in K[G]$, $\operatorname{tr}(e)$ lies in the prime field: $\operatorname{tr}(e) \in \mathbb{Q}$ if $\operatorname{char} K = 0$, and $\operatorname{tr}(e) \in \mathbb{F}_p$ if $\operatorname{char} K = p$.

**Unique products.** $G$ has the *unique product property* if for all finite nonempty $A, B \subseteq G$ there is $u \in AB$ with a unique factorization $u = ab$, $a\in A$, $b \in B$. Unique product $\Rightarrow$ (U), hence (Z) and (I), for every $K$. Left-orderable groups have unique products.

## 3. History & State of the Art (SOTA)

Irving Kaplansky circulated the zero-divisor and idempotent questions from the late 1940s; they appear in his 1956 Chicago problem list and in the widely cited *"Problems in the theory of rings" revisited* (Amer. Math. Monthly, 1970). Higman's 1940 thesis had already settled the unit conjecture for locally indicable groups, which contains the orderable case.

Milestones:

- **1940** — Higman: (U), (Z), (I) hold for locally indicable groups over any field with no nontrivial units in $K$.
- **1969** — Kaplansky: trace of an idempotent in $\mathbb{C}[G]$ lies in $[0,1]$, reducing (I) in characteristic 0 to the trace conjecture.
- **1972** — Zalesskii: rationality/prime-field membership of the trace.
- **1976** — Farkas–Snider: (Z) for torsion-free polycyclic-by-finite $G$, $\operatorname{char} K = 0$; K. A. Brown gave a shorter proof of the abelian-by-finite case.
- **1988** — Kropholler–Linnell–Moody: (Z) for torsion-free elementary amenable $G$ in characteristic 0.
- **1988** — Promislow: the first explicit torsion-free group without unique products (a 3-dimensional crystallographic group, the "Hantzsche–Wendt" or Promislow group $P$), removing the most flexible combinatorial route.
- **2001** — Higson–Kasparov: Baum–Connes with coefficients for a-T-menable (Haagerup) groups; via the Kadison–Kaplansky conjecture this gives (I) over $\mathbb{C}$ for torsion-free amenable groups, free groups, and groups acting properly on trees or on $\mathrm{CAT}(0)$ cube complexes.
- **2012** — Bartels–Lück: Farrell–Jones conjecture for hyperbolic and $\mathrm{CAT}(0)$ groups, giving (I) in characteristic 0 for those torsion-free classes.
- **2021** — Gardam: **the unit conjecture (U) is false**, with an explicit nontrivial unit in $\mathbb{F}_2[P]$ for the Promislow group. (Z) and (I) survive untouched, since (U) $\Rightarrow$ (Z) is one-directional.

## 4. Partial Results / Verified Cases

The conjecture is a **theorem** in the following cases.

| Class of torsion-free $G$ | Field | Source |
|---|---|---|
| Left-orderable, locally indicable, unique-product groups (incl. free, free abelian, one-relator torsion-free, braid groups, RAAGs) | any $K$ | Higman 1940 |
| Torsion-free polycyclic-by-finite | $\operatorname{char} K = 0$ | Farkas–Snider 1976 |
| Torsion-free abelian-by-finite | $\operatorname{char} K = 0$ | Brown 1976 |
| Torsion-free elementary amenable | $\operatorname{char} K = 0$ | Kropholler–Linnell–Moody 1988 |
| Torsion-free a-T-menable (amenable, free, Coxeter, cubulated groups) | $K \subseteq \mathbb{C}$ | Higson–Kasparov 2001 (via Baum–Connes) |
| Torsion-free hyperbolic; torsion-free $\mathrm{CAT}(0)$; mapping class groups | $\operatorname{char} K = 0$ | Bartels–Lück 2012; Bartels–Bestvina 2019 |
| Linnell's class $\mathcal{C}$ with bounded torsion (analytic Atiyah-type results) | $K \subseteq \mathbb{C}$ | Linnell 1993 |
| $|\operatorname{supp}(e)| \le 3$ arguments, and $G$ with all subgroups generated by $\le 2$ elements free | any $K$ | elementary / Passman 1977 |

Related: Elek–Szabó (2004) proved Kaplansky's *direct finiteness* conjecture ($xy=1 \Rightarrow yx=1$ in $K[G]$) for all sofic groups and all fields — the strongest characteristic-free result in the Kaplansky family.

**Not known** in *any* positive characteristic beyond the orderable/unique-product classes: e.g. (I) for $\mathbb{F}_2[P]$, $P$ the Promislow group, is open even though $P$ is virtually $\mathbb{Z}^3$ and (I) over $\mathbb{Q}$ holds for it by Brown's theorem.

## 5. Principal Obstacles

- **Combinatorics of supports collapses.** The classical method — order $G$, take extremal elements of $\operatorname{supp}(x)\operatorname{supp}(y)$, show they cannot cancel — needs a unique product. Promislow's group shows the property genuinely fails for torsion-free groups, and Gardam's counterexample shows the failure is not merely technical: cancellation really can produce exotic units.
- **Positivity is only available over $\mathbb{C}$.** The whole Kaplansky trace apparatus ($0 \le \tau(e) \le 1$, faithfulness of $\tau$) rests on the $C^*$-algebra order structure. In characteristic $p$ there is no positive cone, no $\ell^2$-completion, no von Neumann trace; Zalesskii's $\operatorname{tr}(e) \in \mathbb{F}_p$ is far weaker than $\operatorname{tr}(e) \in \{0,1\}$ because $\mathbb{F}_p$ is finite and offers no ordering to exploit.
- **Baum–Connes and Farrell–Jones are not known in general.** Both are open for arbitrary groups; Gromov-style random groups with expanders give counterexamples to Baum–Connes *with coefficients* (Higson–Lafforgue–Skandalis 2002), so the analytic route cannot be pushed uniformly.
- **$K$-theory gives the wrong invariant alone.** Farrell–Jones yields $K_0(K[G]) \cong K_0(K) \cong \mathbb{Z}$ for torsion-free $G$, i.e. every f.g. projective module is stably free. Stably free $\neq$ free, and $[e] = n[1]$ in $K_0$ does not by itself force $e \in \{0,1\}$; one must add the Bass/Hattori–Stallings trace conjecture, available only in characteristic $0$.
- **No structure theory for a hypothetical counterexample.** Unlike the unit conjecture, where Gardam's unit was found by a targeted SAT/computer search in a fixed small group over $\mathbb{F}_2$, an idempotent must satisfy the extra constraint $\operatorname{tr}(e) \in \mathbb{F}_p$ together with $e^2 = e$, which prunes searches but also removes obvious candidates.

## 6. The Gap

Two disjoint gaps.

1. **Characteristic zero.** Everything reduces to the trace conjecture $\operatorname{tr}(e) \in \{0,1\}$, which is implied by the Bass conjecture, which is implied by Farrell–Jones. So the gap is exactly: *prove the (K-theoretic) Farrell–Jones or Baum–Connes conjecture for all torsion-free groups* — or find a trace argument independent of assembly maps. Current proofs of FJC need a geometric input (a hyperbolic/$\mathrm{CAT}(0)$/flow-space action with controlled dynamics) that no one knows how to supply for a general finitely presented group.
2. **Positive characteristic.** No reduction to a trace conjecture exists. The gap here is the absence of *any* invariant playing the role of $\tau$. The frontier case is concrete and small: does $\mathbb{F}_2[P]$ have a nontrivial idempotent, where $P = \langle a, b \mid a^{-1}b^2a = b^{-2},\ b^{-1}a^2b = a^{-2}\rangle$?

## 7. Current Research (as of June 2026)

- **Farrell–Jones expansion.** Bartels, Lück, Reich, Bestvina and collaborators (Münster, Bonn, Utah) continue extending FJC — mapping class groups (Bartels–Bestvina 2019), $\mathrm{GL}_n(\mathbb{Z})$, normally poly-free groups. Each extension mechanically adds a class to Section 4 in characteristic $0$.
- **Computer-assisted search over $\mathbb{F}_p$.** Following Gardam's method, groups of the Promislow type are being searched by SAT and Gröbner-basis methods for idempotents and zero divisors; the search space is much larger than for units because $e$ need not be invertible. *(frontier — verify)*
- **Murray's extension.** Murray (2021) produced nontrivial units in $\mathbb{F}_p[P]$ for odd primes, confirming (U) fails in all characteristics for $P$ and refocusing attention on whether (Z) can be attacked in $P$ by similar means.
- **$L^2$-invariants and the Atiyah conjecture.** Jaikin-Zapirain, Linnell, López-Álvarez and Kielak use Hughes-free division rings, $\ast$-regular closures and fibring to prove (Z) for classes such as locally indicable and residually-(torsion-free nilpotent) groups over general fields — the most promising characteristic-free technology.
- **Sofic/hyperlinear approximations.** Elek–Szabó's direct-finiteness method is periodically revisited for whether soficity can force idempotent triviality; no proof is known, and there is no known non-sofic group.

## 8. Future Work

- Prove the Bass trace conjecture directly, without assembly maps, for a large class such as all residually finite groups.
- Find a characteristic-$p$ substitute for the von Neumann trace — for instance a Sylvester rank function or a $\ast$-regular closure with a well-behaved rational-valued rank on $\mathbb{F}_p[G]$.
- Settle (Z) or (I) for the single group $P$ over $\mathbb{F}_2$; a positive resolution there would show Gardam's phenomenon does not propagate down the hierarchy.
- Push Hughes-free division ring embeddings (Jaikin-Zapirain) from locally indicable groups to broader classes; an embedding $K[G] \hookrightarrow D$ into a division ring immediately gives (Z) and hence (I).
- Search systematically for torsion-free groups failing unique products beyond the Promislow family, to test whether idempotent-free-ness is a genuinely different property.

## 9. Key References

- **[Foundational]** G. Higman. *The units of group-rings.* Proc. London Math. Soc. (2) **46** (1940), 231–248.
- **[Foundational]** I. Kaplansky. *Fields and Rings.* University of Chicago Press, 1969.
- **[Foundational]** I. Kaplansky. *"Problems in the theory of rings" revisited.* Amer. Math. Monthly **77** (1970), 445–454. [DOI](https://doi.org/10.2307/2317376)
- **[Foundational]** A. E. Zalesskii. *On a problem of Kaplansky.* Soviet Math. Doklady **13** (1972), 449–452. [DOI](https://doi.org/10.1070/im1973v007n03abeh001952)
- **[Foundational]** D. R. Farkas, R. L. Snider. *$K_0$ and Noetherian group rings.* J. Algebra **42** (1976), 192–198.
- **[Foundational]** K. A. Brown. *On zero divisors in group rings.* Bull. London Math. Soc. **8** (1976), 251–256.
- **[Foundational]** P. H. Kropholler, P. A. Linnell, J. A. Moody. *Applications of a new $K$-theoretic theorem to soluble group rings.* Proc. Amer. Math. Soc. **104** (1988), 675–684. [DOI](https://doi.org/10.2307/2046771)
- **[Foundational]** S. D. Promislow. *A simple example of a torsion-free, non-unique product group.* Bull. London Math. Soc. **20** (1988), 302–304. [DOI](https://doi.org/10.1112/blms/20.4.302)
- **[SOTA]** P. A. Linnell. *Division rings and group von Neumann algebras.* Forum Math. **5** (1993), 561–576. [DOI](https://doi.org/10.1515/form.1993.5.561)
- **[SOTA]** N. Higson, G. Kasparov. *$E$-theory and $KK$-theory for groups which act properly and isometrically on Hilbert space.* Invent. Math. **144** (2001), 23–74. [DOI](https://doi.org/10.1007/s002220000118)
- **[SOTA]** G. Elek, E. Szabó. *Sofic groups and direct finiteness.* J. Algebra **280** (2004), 426–434. [DOI](https://doi.org/10.1016/j.jalgebra.2004.06.023)
- **[SOTA]** A. Bartels, W. Lück. *The Borel conjecture for hyperbolic and $\mathrm{CAT}(0)$-groups.* Ann. of Math. **175** (2012), 631–689. [DOI](https://doi.org/10.4007/annals.2012.175.2.5)
- **[SOTA]** A. Bartels, M. Bestvina. *The Farrell–Jones conjecture for mapping class groups.* Invent. Math. **215** (2019), 651–712. [DOI](https://doi.org/10.1007/s00222-018-0834-9)
- **[SOTA]** G. Gardam. *A counterexample to the unit conjecture for group rings.* Ann. of Math. **194** (2021), 967–979. [DOI](https://doi.org/10.4007/annals.2021.194.3.9)
- **[SOTA]** A. G. Murray. *More counterexamples to the unit conjecture for group rings.* Preprint, 2021.
- **[Survey]** D. S. Passman. *The Algebraic Structure of Group Rings.* Wiley-Interscience, 1977.
- **[Survey]** W. Lück. *$L^2$-Invariants: Theory and Applications to Geometry and $K$-Theory.* Ergebnisse der Mathematik 44, Springer, 2002.
- **[Survey]** G. Gardam. *Kaplansky's conjectures.* Proceedings of the 8th European Congress of Mathematics, EMS Press, 2023.

## 10. Worked Example / Concrete Special Case

**(a) Support of size 2.** Let $G$ be torsion-free and suppose $e = \alpha \cdot 1 + \beta g \in K[G]$ with $g \neq 1$, $\beta \neq 0$, and $e^2 = e$. Expanding,
$$e^2 = \alpha^2 \cdot 1 + 2\alpha\beta\, g + \beta^2 g^2 .$$
Since $G$ is torsion-free, $g^2 \neq 1$ and $g^2 \neq g$, so $g^2$ is a *third* basis element. Matching coefficients of $g^2$ in $e^2 = e$ gives $\beta^2 = 0$, contradicting $\beta \neq 0$. Hence $e = \alpha\cdot 1$ with $\alpha^2 = \alpha$, so $e \in \{0,1\}$. (In char $2$ the coefficient of $g$ gives $0 = \beta$ directly.) The argument used torsion-freeness exactly once — and fails immediately if $g^2 = 1$.

**(b) $G = \mathbb{Z}$.** Here $K[\mathbb{Z}] \cong K[t, t^{-1}]$, an integral domain (the leading coefficients of a product multiply). So $e(1-e)=0$ forces $e \in \{0,1\}$. Equivalently, if $e = \sum_{i=m}^{n} a_i t^i$ with $a_m, a_n \neq 0$ and $n > m$, then $e^2$ has top degree $2n > n$, impossible.

**(c) Why torsion breaks it.** Take $G = \mathbb{Z}/3 = \langle g \rangle$, $K = \mathbb{Q}$, and $e = \tfrac13(1 + g + g^2)$. Then $eg = e$, so $e^2 = \tfrac13(e + eg + eg^2) = \tfrac13(3e) = e$, and $\operatorname{tr}(e) = 1/3 \notin \{0,1\}$. This is precisely the trace value the Kaplansky trace conjecture forbids for torsion-free groups, and it illustrates Zalesskii's theorem: $1/3 \in \mathbb{Q}$.

**(d) The open frontier, concretely.** Let $P = \langle a, b \mid a^{-1}b^2a = b^{-2},\; b^{-1}a^2b = a^{-2}\rangle$, torsion-free with $\langle a^2, b^2, (ab)^2\rangle \cong \mathbb{Z}^3$ of index $4$. Gardam exhibited a unit $u \in \mathbb{F}_2[P]$ with $|\operatorname{supp}(u)| = 21$ that is not of the form $\lambda g$. Since $P$ is abelian-by-finite, Brown's theorem gives (I) over every characteristic-$0$ field. Over $\mathbb{F}_2$ nothing is known: any $e \in \mathbb{F}_2[P]$ with $e^2 = e$, $e \neq 0,1$ must satisfy $\operatorname{tr}(e) \in \{0,1\} \subset \mathbb{F}_2$ (Zalesskii gives no obstruction), and finding or excluding such an $e$ is the smallest fully open instance of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*