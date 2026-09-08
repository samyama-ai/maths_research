---
id: 04-topology/kaplansky-zero-divisor-conjecture
title: "Kaplansky Zero Divisor Conjecture"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kaplansky Zero Divisor Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/kaplansky-zero-divisor-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Conjecture (Kaplansky).** Let $G$ be a torsion-free group and $K$ a field. Then the group algebra $K[G]$ has no zero divisors: if $\alpha,\beta \in K[G]$ and $\alpha\beta = 0$, then $\alpha = 0$ or $\beta = 0$.

Equivalently, $K[G]$ is a domain. The torsion-free hypothesis is necessary: if $g \in G$ has order $n > 1$, then
$$(1-g)(1+g+\cdots+g^{n-1}) = 1 - g^n = 0 ,$$
and neither factor vanishes. The conjecture asserts the converse — torsion is the *only* source of zero divisors.

A complete proof must handle all fields (including $\mathbb{F}_p$, where characteristic-$p$ phenomena defeat analytic methods) and all torsion-free groups, including non-finitely-presented and non-residually-finite ones. A disproof requires an explicit torsion-free $G$, a field $K$, and finite-support elements $\alpha,\beta \neq 0$ with $\alpha\beta = 0$.

The topological content: $G$ torsion-free and finitely presented is (conjecturally, in the aspherical setting) the fundamental group of a closed aspherical manifold, and the conjecture is a purely algebraic shadow of a family of geometric conjectures — Baum–Connes, Farrell–Jones, and the strong Atiyah conjecture — about free actions on contractible spaces.

## 2. Mathematical Foundations

**Group algebra.** For a group $G$ and field $K$, $K[G] = \bigoplus_{g\in G} K g$ with multiplication extending that of $G$. Every $\alpha \in K[G]$ is a finite sum $\alpha = \sum_{g} a_g g$; its **support** is $\operatorname{supp}(\alpha) = \{ g : a_g \neq 0\}$.

**The Kaplansky hierarchy.** For torsion-free $G$, the following implications hold, each strictly (or not known to be) reversible:
$$\text{(ZD) } K[G] \text{ is a domain} \;\Longrightarrow\; \text{(Idem) only idempotents are } 0,1 \;\Longrightarrow\;\text{(Trace) } \operatorname{tr}(e)\in\{0,1\}.$$
Separately, the **unit conjecture** (UC) states that all units of $K[G]$ are trivial, i.e. of the form $a g$ with $a \in K^\times$; UC $\Rightarrow$ ZD.

**Unique product property (UP).** $G$ has UP if for all finite nonempty $A,B \subseteq G$ there is $g \in G$ with a *unique* factorization $g = ab$, $a\in A$, $b \in B$.

> **Lemma.** UP $\Rightarrow$ ZD (and $\Rightarrow$ UC) over every field.

**Proof.** With $A = \operatorname{supp}(\alpha)$, $B = \operatorname{supp}(\beta)$ and $g = a_0b_0$ uniquely represented, the coefficient of $g$ in $\alpha\beta$ is $\alpha_{a_0}\beta_{b_0} \neq 0$. $\square$

**Orderability.** $G$ is left-orderable if it carries a total order with $x<y \Rightarrow gx<gy$; bi-orderable if the order is also right-invariant. Left-orderable $\Rightarrow$ **diffuse** (Bowditch) $\Rightarrow$ UP. $G$ is **locally indicable** if every nontrivial finitely generated subgroup surjects onto $\mathbb{Z}$; locally indicable $\Rightarrow$ left-orderable.

**Analytic route.** Let $\mathcal{N}(G)$ be the group von Neumann algebra, with von Neumann dimension $\dim_{\mathcal{N}(G)}$. The **strong Atiyah conjecture** for torsion-free $G$ says: for every matrix $A \in M_{m\times n}(\mathbb{C}[G])$, the $\mathcal{N}(G)$-dimension of $\ker(A: \ell^2(G)^m \to \ell^2(G)^n)$ is an integer. Taking $m=n=1$ and $A = \alpha \neq 0$: a zero divisor forces $0 < \dim \ker \alpha < 1$, contradicting integrality. Hence
$$\text{strong Atiyah conjecture for } G \;\Longrightarrow\; \mathbb{C}[G] \text{ is a domain}.$$
Likewise Baum–Connes for torsion-free $G$ implies the Kadison–Kaplansky idempotent conjecture for $C^*_r(G)$, hence (Idem) for $\mathbb{C}[G]$ — but *not* (ZD).

## 3. History & State of the Art (SOTA)

- **1940.** Graham Higman's thesis proves ZD and UC for locally indicable groups over fields (and over domains with only trivial units), the first substantial result.
- **1950s–1970.** Irving Kaplansky circulates the zero-divisor, unit, idempotent and direct-finiteness problems in Chicago lectures; they are published in "Problems in the theory of rings revisited" (1970).
- **1976.** K. A. Brown settles torsion-free abelian-by-finite groups in characteristic $0$; Farkas–Snider extend to torsion-free polycyclic-by-finite in characteristic $0$ using $K_0$ and Moody-type induction.
- **1980.** Cliff removes the characteristic hypothesis for polycyclic-by-finite groups.
- **1987–88.** Rips–Segev construct the first torsion-free non-UP group; Promislow gives the small crystallographic example $P$ (the Hantzsche–Wendt group, $\pi_1$ of a closed flat $3$-manifold), showing the UP method has a hard ceiling.
- **1988.** Kropholler–Linnell–Moody prove ZD for all torsion-free **elementary amenable** groups.
- **1993–2000.** Linnell's division-ring theorem establishes the strong Atiyah conjecture for the class $\mathcal{C}$ (extensions of free by elementary amenable, with a bound on torsion orders), giving ZD in characteristic $0$ for a large geometric class; Schick and Lück extend the analytic machinery.
- **2020.** Jaikin-Zapirain and López-Álvarez prove the strong Atiyah conjecture for torsion-free one-relator groups, hence ZD over $\mathbb{C}$ for that class (knot groups included).
- **2021.** Giles Gardam disproves the **unit** conjecture: a nontrivial unit in $\mathbb{F}_2[P]$, $P$ the Promislow group. Murray extends to all fields of positive characteristic. The zero-divisor conjecture is untouched — indeed $K[P]$ *is* a domain by Cliff's theorem.

## 4. Partial Results / Verified Cases

ZD is a theorem for torsion-free $G$ in each of these classes:

| Class | Field | Source |
|---|---|---|
| Locally indicable (incl. free, free-by-$\mathbb{Z}$, bi-orderable) | any | Higman 1940 |
| Unique product / diffuse / left-orderable (incl. $\pi_1$ of most hyperbolic $3$-manifolds) | any | UP lemma |
| Abelian-by-finite | char $0$ | Brown 1976 |
| Polycyclic-by-finite (incl. all torsion-free crystallographic groups: flat $n$-manifold groups, all $n$) | any | Farkas–Snider 1976; Cliff 1980 |
| Elementary amenable | any | Kropholler–Linnell–Moody 1988 |
| Linnell's class $\mathcal{C}$ (free-by-elementary-amenable, e.g. limit groups, many $3$-manifold groups) | char $0$ | Linnell 1993 |
| One-relator groups (incl. all knot groups $\pi_1(S^3\setminus K)$) | char $0$ | Jaikin-Zapirain–López-Álvarez 2020 |
| Hyperbolic groups with large injectivity radius / small-cancellation $C'(1/12)$-type | any | Delzant 1997 |
| Residually torsion-free-nilpotent; RFRS groups | char $0$ | via Atiyah/Linnell machinery |

Weaker statements with far broader reach: the **idempotent** conjecture holds for all torsion-free a-T-menable groups (Higson–Kasparov 2001) and all torsion-free hyperbolic groups (Mineyev–Yu 2002) via Baum–Connes; **direct finiteness** ($\alpha\beta=1 \Rightarrow \beta\alpha=1$) holds for all sofic groups (Elek–Szabó 2004).

## 5. Principal Obstacles

- **UP is exhausted.** The Promislow group $P = \langle a,b \mid ab^2a^{-1}b^2,\, ba^2b^{-1}a^2\rangle$ is torsion-free and fails UP via an explicit $14$-element set; no combinatorial-support argument applies. Since non-UP torsion-free groups are now known to be abundant (small-cancellation constructions), UP cannot be the mechanism in general.
- **Positive characteristic kills analysis.** The Atiyah route uses $\ell^2$-dimension over $\mathcal{N}(G)$ — a real-valued trace on a $C^*$-algebra. Over $\mathbb{F}_p$ there is no $\ell^2$-completion, no positivity, no trace with integrality. Every char-$p$ result (Cliff, Higman) is combinatorial or $K$-theoretic instead.
- **Induction breaks past polycyclic.** Farkas–Snider/Cliff rest on $K_0$ vanishing and Moody's induction theorem, which need Noetherian group rings. Non-elementary-amenable groups have wildly non-Noetherian group rings.
- **No local-to-global principle.** ZD is not known to be preserved by directed unions with control, extensions with non-orderable quotients, or finite index (a torsion-free $G$ with $H \le G$ of index $2$ and $K[H]$ a domain need not visibly inherit it — one only gets that $K[G]$ has no *nilpotents* of a controlled shape).
- **Gardam's counterexample is a warning.** UC failed exactly where the geometry looked safest (a flat $3$-manifold group, virtually $\mathbb{Z}^3$). The heuristic "torsion-free geometry $\Rightarrow$ rigid algebra" is now known to be unsound for the sibling conjecture.

## 6. The Gap

Proven cases all satisfy at least one of: (i) an ordering/UP structure supplying a top-degree term; (ii) a Noetherian $K$-theoretic induction (polycyclic-by-finite, elementary amenable); (iii) an $\ell^2$-integrality theorem valid only in characteristic $0$.

The gap is the complement: torsion-free groups that are **non-UP, non-elementary-amenable, and considered over $\mathbb{F}_p$**. The concrete missing step is a characteristic-free replacement for the von Neumann dimension — a $\mathbb{Z}$-valued "rank" on $K[G]$-modules with $\operatorname{rk}(\ker \alpha) \in \mathbb{Z}$ for $\alpha \neq 0$. Candidates (Sylvester rank functions, Hughes-free division rings, positive-characteristic Lück approximation) exist but are only known to be well-behaved on the classes where ZD is already proved. The first fully open testbed: a torsion-free hyperbolic non-UP group over $\mathbb{F}_2$.

## 7. Current Research (as of June 2026)

- **Sylvester rank functions and division closures.** Jaikin-Zapirain's programme (UAM Madrid) constructs Hughes-free epic division $K[G]$-rings; existence of such a ring immediately gives ZD over any $K$. Extensions beyond locally indicable groups are the active frontier *(frontier — verify)*.
- **Positive-characteristic Atiyah/Lück approximation.** Jaikin-Zapirain, López-Álvarez, and collaborators pursue mod-$p$ analogues of $\ell^2$-Betti numbers; a char-$p$ integrality theorem would transfer most char-$0$ results.
- **Computational search.** Following Gardam's SAT-solver methodology, groups (Newcastle, Bonn, Oxford) run exhaustive support-bounded searches for zero divisors in $\mathbb{F}_2[P]$ and in small non-UP groups; all reported searches are negative through moderate support sizes *(frontier — verify)*.
- **Non-UP group constructions.** Steenbock, Gruber and coauthors build torsion-free non-UP groups from graphical small cancellation, widening the class of genuine test cases.
- **Farrell–Jones transfer.** Bartels–Lück-style results for hyperbolic and $\mathrm{CAT}(0)$ groups give $K$- and $L$-theoretic control; converting this into zero-divisor statements remains unachieved.

## 8. Future Work

1. Prove the strong Atiyah conjecture for all torsion-free hyperbolic groups — this would settle ZD over $\mathbb{C}$ for the largest natural geometric class.
2. Define a Sylvester rank function on $\mathbb{F}_p[G]$ that is integral for $G$ torsion-free, and verify it for one non-elementary-amenable, non-UP example.
3. Decide whether Gardam's unit in $\mathbb{F}_2[P]$ has any zero-divisor analogue in nearby crystallographic-like groups where Cliff's theorem does not apply.
4. Extend Higman's locally indicable theorem to *diffuse* groups over arbitrary coefficient rings, closing the gap between the orderability and support methods.
5. Determine whether ZD is inherited by finite-index overgroups of torsion-free groups — a positive answer would automatically upgrade many results.

## 9. Key References

- **[Foundational]** G. Higman. *The units of group-rings.* Proc. London Math. Soc. (2) **46** (1940), 231–248.
- **[Foundational]** I. Kaplansky. *Problems in the theory of rings revisited.* Amer. Math. Monthly **77** (1970), 445–454. [DOI](https://doi.org/10.2307/2317376)
- **[Foundational]** D. S. Passman. *The Algebraic Structure of Group Rings.* Wiley-Interscience, 1977.
- K. A. Brown. *On zero divisors in group rings.* Bull. London Math. Soc. **8** (1976), 251–256.
- D. R. Farkas, R. L. Snider. *$K_0$ and Noetherian group rings.* J. Algebra **42** (1976), 192–198.
- G. H. Cliff. *Zero divisors in group rings.* Comm. Algebra **8** (1980), 1993–1998.
- P. H. Kropholler, P. A. Linnell, J. A. Moody. *Applications of a new $K$-theoretic theorem to soluble group rings.* Proc. Amer. Math. Soc. **104** (1988), 675–684. [DOI](https://doi.org/10.2307/2046771)
- S. D. Promislow. *A simple example of a torsion-free non-unique product group.* Bull. London Math. Soc. **20** (1988), 302–304. [DOI](https://doi.org/10.1112/blms/20.4.302)
- E. Rips, Y. Segev. *Torsion-free group without unique product property.* J. Algebra **108** (1987), 116–126. [DOI](https://doi.org/10.1016/0021-8693(87)90125-6)
- P. A. Linnell. *Division rings and group von Neumann algebras.* Forum Math. **5** (1993), 561–576. [DOI](https://doi.org/10.1515/form.1993.5.561)
- T. Delzant. *Sur l'anneau d'un groupe hyperbolique.* C. R. Acad. Sci. Paris Sér. I **324** (1997), 381–384.
- B. H. Bowditch. *A variation on the unique product property.* J. London Math. Soc. **62** (2000), 813–826. [DOI](https://doi.org/10.1112/s0024610700001307)
- N. Higson, G. Kasparov. *$E$-theory and $KK$-theory for groups which act properly and isometrically on Hilbert space.* Invent. Math. **144** (2001), 23–74. [DOI](https://doi.org/10.1007/s002220000118)
- I. Mineyev, G. Yu. *The Baum–Connes conjecture for hyperbolic groups.* Invent. Math. **149** (2002), 97–122. [DOI](https://doi.org/10.1007/s002220200214)
- G. Elek, E. Szabó. *Sofic groups and direct finiteness.* J. Algebra **280** (2004), 426–434. [DOI](https://doi.org/10.1016/j.jalgebra.2004.06.023)
- **[SOTA]** A. Jaikin-Zapirain, D. López-Álvarez. *The strong Atiyah and Lück approximation conjectures for one-relator groups.* Math. Ann. **376** (2020), 1741–1793. [DOI](https://doi.org/10.1007/s00208-019-01926-0)
- **[SOTA]** G. Gardam. *A counterexample to the unit conjecture for group rings.* Ann. of Math. (2) **194** (2021), 967–979. [DOI](https://doi.org/10.4007/annals.2021.194.3.9)
- **[SOTA]** A. G. Murray. *More counterexamples to the unit conjecture for group rings.* arXiv:2106.02147 (2021).
- **[Survey]** W. Lück. *$L^2$-Invariants: Theory and Applications to Geometry and $K$-Theory.* Springer, 2002.
- **[Survey]** G. Gardam. *Kaplansky's conjectures.* European Congress of Mathematics (8ECM) Proceedings, EMS Press, 2023.

## 10. Worked Example / Concrete Special Case

**Case: the Klein bottle group.** Let $G = \langle a, b \mid bab^{-1} = a^{-1}\rangle$, the fundamental group of the Klein bottle — torsion-free, virtually $\mathbb{Z}^2$, not bi-orderable. We prove $K[G]$ is a domain by direct computation.

$G = \langle a \rangle \rtimes \langle b \rangle \cong \mathbb{Z} \rtimes_{-1} \mathbb{Z}$, so
$$K[G] \;\cong\; R[t^{\pm1}; \sigma], \qquad R = K[x^{\pm 1}],\; x = a,\; t = b,\; \sigma(x) = x^{-1},$$
the skew Laurent ring with relation $t x = \sigma(x) t = x^{-1}t$.

Take nonzero $\alpha = \sum_{i=m}^{M} r_i t^i$ and $\beta = \sum_{j=n}^{N} s_j t^j$ with $r_M, s_N \neq 0$ and $r_m,s_n \neq 0$. Because $\sigma$ is a ring automorphism of the commutative domain $R = K[x^{\pm1}]$,
$$\alpha\beta = \sum_{k} \Big( \sum_{i+j=k} r_i\,\sigma^{i}(s_j) \Big) t^{k},$$
and the top coefficient is $r_M \,\sigma^{M}(s_N)$. Now $\sigma^{M}(s_N) \neq 0$ (automorphisms are injective) and $R$ is a domain, so $r_M\sigma^M(s_N) \neq 0$. Hence $\alpha\beta \neq 0$: $K[G]$ is a domain over **every** field.

*Numerical instance.* With $\alpha = 1 + a$, $\beta = 1 - a b$ in $\mathbb{F}_2[G]$:
$$\alpha\beta = (1+a)(1+ab) = 1 + ab + a + a\!\cdot\! ab = 1 + a + ab + a^2b \neq 0,$$
the four group elements $1, a, ab, a^2b$ being pairwise distinct.

**Why this does not generalize.** The same skew-degree argument works for any polycyclic tower, which is exactly the reach of Farkas–Snider/Cliff. It fails the moment the group has no normal series with cyclic-like quotients. For the Promislow group $P$ — torsion-free, $\pi_1$ of a closed flat $3$-manifold, virtually $\mathbb{Z}^3$ — the polycyclic argument still applies, so $K[P]$ *is* a domain; yet Gardam exhibited a nontrivial unit $\alpha \in \mathbb{F}_2[P]^\times$ with $|\operatorname{supp}(\alpha)| = 21$. The lesson: the leading-term technique that proves ZD here says nothing about units, and outside polycyclic-by-finite groups it says nothing at all.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*