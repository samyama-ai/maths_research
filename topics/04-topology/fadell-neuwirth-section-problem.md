---
id: 04-topology/fadell-neuwirth-section-problem
title: "Section Conjecture for Configuration Spaces and Fadell–Neuwirth Fibrations"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Section Conjecture for Configuration Spaces and Fadell–Neuwirth Fibrations

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/fadell-neuwirth-section-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $M$ be a connected manifold without boundary, $\dim M \ge 2$, and let
$$F_n(M)=\{(x_1,\dots,x_n)\in M^n \;:\; x_i\neq x_j \text{ for } i\neq j\}$$
be the ordered configuration space. For $n>m\ge 1$ the forgetful map
$$p_{n,m}: F_n(M)\longrightarrow F_m(M),\qquad (x_1,\dots,x_n)\mapsto (x_1,\dots,x_m)$$
is a locally trivial fibration (Fadell–Neuwirth, 1962).

**The section problem.** For which triples $(M,n,m)$ does $p_{n,m}$ admit a continuous cross-section $s$ with $p_{n,m}\circ s=\mathrm{id}$, and can all sections be classified up to homotopy?

Concretely: given $m$ distinct points of $M$, can one choose $n-m$ further distinct points *continuously and canonically* in the positions of the first $m$?

A complete solution requires (i) a decision procedure over all $(M,n,m)$, at minimum for all closed surfaces and all spheres $S^k$; (ii) for each solvable case, a classification of sections up to homotopy; (iii) resolution of the **algebraic-vs-topological** question: whether a splitting of the induced short exact sequence of pure braid groups always comes from a genuine section. A disproof in a given case means an obstruction argument (degree, characteristic class, Nielsen theory, or a group-theoretic non-splitting proof).

## 2. Mathematical Foundations

**Fadell–Neuwirth fibration.** For $M$ a manifold without boundary and $Q_m=\{q_1,\dots,q_m\}\subset M$, the map $p_{n,m}$ is a fibration with fibre
$$p_{n,m}^{-1}(q_1,\dots,q_m)\;=\;F_{n-m}\bigl(M\setminus Q_m\bigr).$$

**Long exact sequence.** For $k\ge 1$,
$$\cdots\to \pi_k F_{n-m}(M\setminus Q_m)\to \pi_k F_n(M)\xrightarrow{(p_{n,m})_*} \pi_k F_m(M)\to \pi_{k-1}F_{n-m}(M\setminus Q_m)\to\cdots$$

**Braid groups.** $P_n(M)=\pi_1 F_n(M)$ is the *pure braid group* of $M$ on $n$ strings; $B_n(M)=\pi_1\bigl(F_n(M)/\Sigma_n\bigr)$. If $M$ is a surface other than $S^2$ and $\mathbb{RP}^2$, then $F_n(M)$ is aspherical, i.e. a $K(P_n(M),1)$, and one gets the **Fadell–Neuwirth short exact sequence**
$$1\longrightarrow P_{n-m}(M\setminus Q_m)\longrightarrow P_n(M)\xrightarrow{\;(p_{n,m})_*\;} P_m(M)\longrightarrow 1. \tag{FN}$$

**Reduction principle (asphericity).** If $F_n(M)$ and $F_m(M)$ are aspherical, then homotopy classes of maps $F_m(M)\to F_n(M)$ correspond to conjugacy classes of homomorphisms $P_m(M)\to P_n(M)$. Hence
$$p_{n,m} \text{ admits a section} \iff (\mathrm{FN}) \text{ splits.}$$
For $M=S^2,\mathbb{RP}^2$ the equivalence fails and genuine homotopy-theoretic obstructions appear.

**Vector-field criterion.** If $M$ is closed with $\chi(M)=0$, a nowhere-zero vector field $X$ exists; flowing $x_i$ for times $t,2t,\dots$ with $t=t(x)$ smaller than half the minimal separation produces a section of $p_{n,m}$ for all $n>m\ge1$. For open $M$ the same holds. So all obstructions live in $\chi(M)\neq 0$.

**Degree obstruction.** A section of $p_{2,1}$ is a fixed-point-free self-map $f:M\to M$. On $S^k$, $L(f)=1+(-1)^k\deg f$, so a fixed-point-free $f$ has $\deg f=(-1)^{k+1}$.

## 3. History & State of the Art (SOTA)

- **1962.** Fadell and Neuwirth introduce configuration spaces, prove the fibration theorem, and pose the section problem (Math. Scand. 10). Fadell's companion paper links $\pi_1F_n(S^3)$ to Dirac's string problem.
- **1969.** Birman studies surface braid groups and (FN), identifying its role in presenting $P_n(M)$.
- **1973.** Goldberg gives splitting criteria for (FN); sections always exist for surfaces with non-empty boundary.
- **2001.** Fadell–Husseini's monograph consolidates the homotopy theory of $F_n(M)$ and the section problem.
- **2003–2013.** Gonçalves and Guaschi carry out the systematic program: closed orientable surfaces, $S^2$, $\mathbb{RP}^2$, and non-orientable surfaces, settling most low-$m$ cases and producing the sharpest non-splitting results.
- **2016.** Salter–Tshishiku prove non-realizability results for braid groups by diffeomorphisms — the smooth analogue of the section question.
- **2020.** Lei Chen classifies sections of $p_{n,m}$ for the Riemann sphere: for $m\ge3$ all sections are, up to homotopy, the "Möbius-canonical" ones.

## 4. Partial Results / Verified Cases

| Case | Answer |
|---|---|
| $M$ open, or $M$ closed with $\chi(M)=0$ (torus, Klein bottle, odd spheres $S^{2k+1}$) | Section exists for **all** $n>m\ge1$ |
| $M$ surface with $\partial M\neq\emptyset$ | Section exists for all $n>m\ge1$ (Goldberg) |
| $M=\mathbb{R}^k$, $k\ge2$ | Section exists; place extra points at radius $1+\max_i\|x_i\|$ |
| $M=S^2$, $m\ge3$ | **Section exists**: $F_n(S^2)\cong \mathrm{PSL}(2,\mathbb{C})\times F_{n-3}(S^2\setminus\{0,1,\infty\})$ |
| $M=S^2$, $m\in\{1,2\}$, $n\ge3$ | **No section**: $\pi_2F_m(S^2)=\mathbb{Z}$ but $\pi_2F_n(S^2)=0$ for $n\ge3$ |
| $M=S^{2k}$, $m=1$, $n\ge3$ | **No section** (degree obstruction, §2) |
| $M=\mathbb{RP}^2$ | Section exists **iff** $(n,m)=(3,2)$ (Gonçalves–Guaschi) |
| $M$ closed orientable, genus $g\ge1$, $m=1$ | Section exists for all $n$ |
| $M$ closed non-orientable, genus $\ge3$, $m=1$ | (FN) splits (Gonçalves–Guaschi, 2010) |

Note the non-monotonicity for $S^2$: sections exist for $m=3$ but not for $m=1,2$, even though $p_{n,1}=p_{3,1}\circ p_{n,3}$. This is exactly the failure of the group-theoretic criterion for non-aspherical bases: $P_1(S^2)=P_2(S^2)=1$, so (FN) splits trivially for $m\le2$ while the fibration has no section.

## 5. Principal Obstacles

- **No universal invariant.** The known negative answers use three unrelated mechanisms: $\pi_2$-obstructions ($S^2$), degree/Lefschetz obstructions (even spheres), and delicate group-theoretic arguments in $P_n(\mathbb{RP}^2)$ using torsion and the structure of $B_n(\mathbb{RP}^2)$. None generalizes.
- **Aspherical case is purely algebraic and hard.** For genus $g\ge2$ the question "does $P_n(\Sigma_g)\to P_m(\Sigma_g)$ split?" concerns extensions of large torsion-free hyperbolic-like groups. Obstruction theory has no finite-dimensional target: $\mathrm{cd}\,P_n(\Sigma_g)=n+1$ grows with $n$, so primary obstructions in $H^k$ do not vanish for dimension reasons.
- **Cohomological obstructions vanish or are inaccessible.** $H^*(F_n(M))$ is well understood (Cohen–Taylor, Kriz, Totaro) but the Leray–Hirsch splitting of $p_{n,m}^*$ typically holds *in cohomology* while no section exists — cohomology is too coarse.
- **Torsion and centre.** $P_n(S^2)$ and $P_n(\mathbb{RP}^2)$ have torsion (elements of order $2,\ 2n-2,\ 4$), forcing case-by-case analysis of finite subgroups; there is no uniform Euler-class-type invariant covering all closed surfaces.
- **Smooth vs. topological.** Sections realized by diffeomorphism-group data can be obstructed by Nielsen realization phenomena even when a continuous section exists; the two categories have not been separated in general.

## 6. The Gap

The proven cases are exactly: (a) $\chi(M)=0$ or $M$ open, (b) $M=S^k$ and $M=\mathbb{RP}^2$ completely, (c) closed surfaces of genus $\ge1$ with $m=1$. The gap is:

$$\boxed{\;M=\Sigma_g \text{ closed, } g\ge2 \text{ (or non-orientable genus} \ge 2), \quad 2\le m<n\;}$$

Here the topological problem is *equivalent* to the algebraic one — does (FN) split? — and neither a splitting homomorphism nor a non-splitting proof is known in general. The missing step is a computable invariant of the extension class in $H^2(P_m(\Sigma_g); Z(P_{n-m}(\Sigma_g\setminus Q_m)))$-type terms, or a rigidity theorem forcing every homomorphism $P_m(\Sigma_g)\to P_n(\Sigma_g)$ lifting the identity to be geometric. A second gap: closed manifolds of dimension $\ge3$ with $\chi\neq0$ beyond even spheres are essentially untouched.

## 7. Current Research (as of June 2026)

- **Rigidity of homomorphisms between braid/mapping class groups.** Chen's method for $S^2$ — show any section induces a homomorphism forced to be "canonical" by Thurston-type rigidity — is being pushed to $\Sigma_g$, $g\ge2$. *(frontier — verify)*
- **The Gonçalves–Guaschi program** (São Paulo / Caen) continues on non-orientable surfaces and on the generalized sequence for mixed braid groups $B_{n,m}$.
- **Smooth and holomorphic variants.** Salter–Tshishiku-style non-realizability arguments are applied to ask whether sections of $p_{n,m}$ can be taken smooth in the fibre-preserving sense, and whether the algebraic/holomorphic section problem over $\mathcal{M}_{0,n}$ has extra obstructions.
- **Arithmetic analogue.** $F_n(\mathbb{C})/\Sigma_n$ is $\mathcal{M}_{0,n+3}$-adjacent, so the topological question sits beside Grothendieck's anabelian section conjecture; techniques traffic in both directions. *(frontier — verify)*

## 8. Future Work

1. Settle $p_{n,2}$ for $\Sigma_2$ — the smallest genuinely open case — by direct analysis of $P_2(\Sigma_2)$-actions.
2. Build an Euler-class-like invariant $e(p_{n,m})\in H^2$ that recovers all three known obstruction mechanisms as specializations.
3. Classify sections up to homotopy in the solved cases beyond $S^2$ (only $\mathbb{RP}^2$ and $S^2$ are fully understood).
4. Extend to closed $n$-manifolds with $\chi\neq0$ in dimension $\ge4$, where the degree argument for even spheres has no analogue.
5. Determine whether a splitting of (FN) can exist without a *geometric* section in the smooth category.

## 9. Key References

- **[Foundational]** E. Fadell, L. Neuwirth. *Configuration spaces.* Mathematica Scandinavica 10 (1962), 111–118.
- **[Foundational]** E. Fadell. *Homotopy groups of configuration spaces and the string problem of Dirac.* Duke Mathematical Journal 29 (1962), 231–242.
- **[Foundational]** J. Birman. *On braid groups.* Communications on Pure and Applied Mathematics 22 (1969), 41–72.
- **[Foundational]** C. H. Goldberg. *An exact sequence of braid groups.* Mathematica Scandinavica 33 (1973), 69–82.
- **[Survey]** E. Fadell, S. Husseini. *Geometry and Topology of Configuration Spaces.* Springer Monographs in Mathematics, Springer, 2001.
- **[SOTA]** D. L. Gonçalves, J. Guaschi. *On the structure of surface pure braid groups.* Journal of Pure and Applied Algebra, 2004.
- **[SOTA]** D. L. Gonçalves, J. Guaschi. *The braid groups of the projective plane.* Algebraic & Geometric Topology 4 (2004), 757–780.
- **[SOTA]** D. L. Gonçalves, J. Guaschi. *The braid group $B_{n,m}(S^2)$ and the generalised Fadell–Neuwirth short exact sequence.* Journal of Knot Theory and Its Ramifications, 2005.
- **[SOTA]** D. L. Gonçalves, J. Guaschi. *The Fadell–Neuwirth short exact sequence for non-orientable surfaces.* Journal of Pure and Applied Algebra 214 (2010), 667–677.
- **[SOTA / Recent]** L. Chen. *Section problems for configurations of points on the Riemann sphere.* Algebraic & Geometric Topology 20 (2020), 3047–3082.
- **[Recent]** N. Salter, B. Tshishiku. *On the non-realizability of braid groups by diffeomorphisms.* Geometry & Topology 20 (2016), 3057–3086.
- **[Context]** J. Stix. *Rational Points and Arithmetic of Fundamental Groups.* Lecture Notes in Mathematics 2054, Springer, 2013.

## 10. Worked Example / Concrete Special Case

**Claim A: $p_{3,2}:F_3(\mathbb{RP}^2)\to F_2(\mathbb{RP}^2)$ admits a section.**

Write $\mathbb{RP}^2=S^2/\{\pm1\}$ and denote points by $[u]$, $u\in S^2$. Given $([u],[v])$ with $[u]\neq[v]$, the vectors $u,v$ are linearly independent, so $u\times v\neq0$. Set
$$s([u],[v])=\Bigl([u],[v],\bigl[\tfrac{u\times v}{\|u\times v\|}\bigr]\Bigr).$$
Well-defined: replacing $u\mapsto -u$ or $v\mapsto -v$ changes $u\times v$ by a sign, which is invisible in $\mathbb{RP}^2$. Distinctness: $u\times v\perp u$ and $u\times v\perp v$, so $[u\times v]\notin\{[u],[v]\}$. Continuity is clear. Hence a section exists, and correspondingly the sequence
$$1\to P_1(\mathbb{RP}^2\setminus\{q_1,q_2\})\to P_3(\mathbb{RP}^2)\to P_2(\mathbb{RP}^2)\to 1$$
splits. This is the *unique* splitting case for $\mathbb{RP}^2$.

**Claim B: $p_{2,1}:F_2(\mathbb{RP}^2)\to\mathbb{RP}^2$ admits no section.**

A section is $x\mapsto(x,f(x))$ with $f:\mathbb{RP}^2\to\mathbb{RP}^2$ continuous and $f(x)\neq x$ for all $x$. But $\mathbb{RP}^2$ has the fixed-point property: with $\mathbb{Z}/2$ coefficients $H^*(\mathbb{RP}^2;\mathbb{F}_2)=\mathbb{F}_2[a]/(a^3)$, and $f^*a=\varepsilon a$ with $\varepsilon\in\{0,1\}$, giving mod-2 Lefschetz number $L_2(f)=1+\varepsilon+\varepsilon^2 = 1 \bmod 2$ for either value of $\varepsilon$. So $L(f)\neq0$ and $f$ has a fixed point. Contradiction.

**Contrast with $S^2$.** Here $p_{2,1}$ *does* have the section $x\mapsto(x,-x)$, but $p_{3,1}$ does not: a section would give $s_*:\pi_2(S^2)=\mathbb{Z}\hookrightarrow\pi_2(F_3(S^2))$, while $F_3(S^2)\simeq\mathrm{PSL}(2,\mathbb{C})\simeq SO(3)$ has $\pi_2=0$. Yet $p_{n,3}$ *does* have a section: fix $z_4,\dots,z_n\in S^2\setminus\{0,1,\infty\}$ and send $(x_1,x_2,x_3)\mapsto(x_1,x_2,x_3,\phi(z_4),\dots,\phi(z_n))$ where $\phi$ is the unique Möbius transformation with $\phi(0,1,\infty)=(x_1,x_2,x_3)$. These three computations exhibit all three obstruction mechanisms and the non-monotonicity in $m$ that makes the general problem hard.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*