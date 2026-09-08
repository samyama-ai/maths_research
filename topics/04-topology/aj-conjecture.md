---
id: 04-topology/aj-conjecture
title: "AJ Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# AJ Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/aj-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $K \subset S^3$ be a knot. Two very different objects are attached to $K$:

- $A_K(M,L)$, the **A-polynomial** of Cooper–Culler–Gillet–Long–Shalen (1994), a classical/geometric invariant cutting out the eigenvalue curve of the $SL_2(\mathbb{C})$-character variety of the knot exterior;
- $\alpha_K(M,L,q)$, the **non-commutative (quantum) A-polynomial**: the minimal-order linear $q$-difference operator annihilating the sequence $n \mapsto J_K(n)$ of colored Jones polynomials.

**AJ Conjecture (Garoufalidis, 2004).** For every knot $K$,
$$\alpha_K(M,L,1) \;\doteq\; A_K(M^2,L),$$
where $\doteq$ means equality up to a factor depending on $M$ alone (a unit of $\mathbb{C}(M)[L]$), and $A_K$ is normalized to include the abelian factor $L-1$.

A complete proof must (i) show the recurrence ideal of $J_K$ localizes to a principal ideal with a well-defined generator, (ii) show that generator survives the specialization $q\to 1$ without degeneration, and (iii) identify the resulting plane curve with the full A-polynomial curve. A disproof requires one knot where the $q=1$ specialization has an irreducible factor not dividing $A_K(M^2,L)$, or misses a factor of $A_K$.

## 2. Mathematical Foundations

**Colored Jones.** $J_K(n)\in\mathbb{Z}[q^{\pm1}]$ denotes the Jones polynomial of $K$ colored by the $n$-dimensional irreducible $sl_2$-representation, normalized so $J_{\text{unknot}}(n)=1$ and $J_K(2)$ is the ordinary Jones polynomial.

**Quantum torus.** Let
$$\mathcal{T}=\mathbb{Z}[q^{\pm1}]\langle M^{\pm1},L^{\pm1}\rangle/(LM-qML),$$
acting on sequences $f:\mathbb{N}\to\mathbb{Z}[q^{\pm1}]$ by
$$(Mf)(n)=q^{n}f(n),\qquad (Lf)(n)=f(n+1).$$
The **recurrence ideal** is $\mathcal{A}_K=\{P\in\mathcal{T}: P\,J_K=0\}$.

**$q$-holonomicity.** Garoufalidis–Lê (2005) proved $J_K$ is $q$-holonomic, i.e. $\mathcal{A}_K \neq 0$ for every knot. Hence, after localizing coefficients to $\mathbb{Q}(q,M)$, the ideal $\widetilde{\mathcal{A}}_K \subset \widetilde{\mathcal{T}} = \mathbb{Q}(q,M)\langle L^{\pm1}\rangle$ becomes principal, since $\widetilde{\mathcal{T}}$ is a (left) principal ideal domain. Its generator, cleared of denominators and made content-free in $\mathbb{Z}[q,M]$, is
$$\alpha_K(M,L,q)=\sum_{i=0}^{d} a_i(M,q)\,L^{i}.$$

**A-polynomial.** With $X$ the knot exterior and $\pi_1(\partial X)=\langle \mu,\lambda\rangle$, restrict representations $\rho:\pi_1(X)\to SL_2(\mathbb{C})$ to the boundary torus and diagonalize:
$$\rho(\mu)\sim\begin{pmatrix}M&*\\0&M^{-1}\end{pmatrix},\qquad \rho(\lambda)\sim\begin{pmatrix}L&*\\0&L^{-1}\end{pmatrix}.$$
The closure of the image of this eigenvalue map is a curve in $(\mathbb{C}^*)^2$ whose defining polynomial (with integer coprime coefficients, including the abelian component $L-1$) is $A_K(M,L)$.

**Skein-theoretic bridge.** By Bullock (1997) and Przytycki–Sikora (2000), the Kauffman bracket skein module at $q=-1$ is isomorphic, modulo nilpotents, to the coordinate ring of the $SL_2(\mathbb{C})$-character variety:
$$\mathcal{S}_{-1}(X)/\sqrt{0}\;\cong\;\mathbb{C}[X_{SL_2}(X)].$$
Frohman–Gelca–Lofaro (2002) built the **peripheral ideal** $\mathfrak{p}_K$ — elements of the skein algebra of the boundary torus whose image in $\mathcal{S}(X)$ vanishes — and showed its $q=1$ limit lies inside the A-ideal. The AJ conjecture is exactly the assertion that these two constructions produce the *same* curve.

## 3. History & State of the Art (SOTA)

- **1994.** Cooper–Culler–Gillet–Long–Shalen introduce $A_K(M,L)$; its Newton polygon detects boundary slopes.
- **2002.** Frohman–Gelca–Lofaro define the non-commutative A-ideal via skein modules of the torus and the "product-to-sum" formula, giving the first quantum shadow of $A_K$.
- **2004.** Garoufalidis states the AJ conjecture in *On the characteristic and deformation varieties of a knot*, computing $\alpha_K$ for $3_1$ and $4_1$. Hikami independently derives the $q$-difference equation for torus knots.
- **2005.** Garoufalidis–Lê prove $q$-holonomicity, making $\alpha_K$ well defined for all knots — the conjecture becomes a statement, not a hope.
- **2006.** Lê proves AJ for a large class of two-bridge knots, introducing the "reduced universal character ring" condition.
- **2010–2013.** Garoufalidis–Sun compute non-commutative A-polynomials of twist knots; Garoufalidis–Koutschan settle $7_4$ using certified irreducibility of $q$-difference operators (Koutschan's `HolonomicFunctions`).
- **2013–2015.** Tran proves a *stronger* AJ (no extra $M$-factor) for torus knots; Lê–Tran extend AJ to cables and to $(-2,3,6n\pm1)$-pretzel knots.
- **Physics side.** Gukov (2005) interprets $\alpha_K$ as the quantization of the A-polynomial curve in Chern–Simons theory, tying AJ to the volume conjecture's asymptotic framework.

The state of the art: AJ is proved for several infinite families, verified by computer for all knots of small crossing number, and unproved in general.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Torus knots $T(p,q)$ | Stronger AJ (exact equality, no $M$-factor) | Tran (2013); Hikami (2004) |
| Two-bridge knots with irreducible nonabelian character variety and reduced universal character ring | AJ holds | Lê (2006) |
| Double twist knots $J(k,l)$ (incl. all twist knots $K_p$) | AJ holds for the double twist family covered by Lê–Tran | Lê–Tran (2015) |
| $(-2,3,6n\pm1)$-pretzel knots | AJ holds | Lê–Tran (2015) |
| $(r,2)$-cables of knots satisfying AJ (with mild conditions) | AJ holds | Lê–Tran (2015) |
| $7_4$ (first knot where irreducibility of $\alpha_K$ was the obstruction) | AJ verified | Garoufalidis–Koutschan (2013) |
| Twist knots $K_p$, roughly $-8\le p\le 11$ | $\alpha_K$ computed explicitly; AJ checked | Garoufalidis–Sun (2010) |

Beyond these, $\alpha_K$ has been machine-computed for all knots up to 8 crossings and many 9–10 crossing knots; in every computed case the $q=1$ specialization matches $A_K(M^2,L)$ up to an $M$-factor. No counterexample is known.

## 5. Principal Obstacles

- **Nilpotents in skein modules.** Bullock's isomorphism holds only *modulo nilpotents*. To recover $A_K$ from the $q=1$ limit one needs the universal character ring of $\pi_1(X)$ to be reduced. This is known for two-bridge knots and a few other families, and is open in general — it is the single largest structural barrier.
- **Only one inclusion is easy.** Skein-theoretic arguments show $A_K(M^2,L)$ divides $\alpha_K(M,L,1)$ (up to $M$-factors) whenever the recurrence and peripheral ideals can be compared. The reverse — that no *extra* factors appear — requires an $L$-degree bound on the minimal recurrence, which is exactly what is hard.
- **Degree explosion.** The $L$-degree and $M$-degree of $\alpha_K$ grow rapidly (order 3 for $4_1$, order 6 for $7_4$, and larger for twist knots with $|p|$ large). Creative-telescoping certificates become enormous; guessing plus certification works case-by-case but produces no uniform theorem.
- **Minimality is not automatic.** Zeilberger-style algorithms return *some* annihilating operator, not the minimal one. Proving minimality means proving irreducibility of a $q$-difference operator over $\mathbb{Q}(q,M)$ — a hard problem in differential Galois / $q$-difference Galois theory, and the technical heart of Garoufalidis–Koutschan.
- **Specialization degeneration.** Setting $q=1$ can drop the leading coefficient $a_d(M,q)$ (if $a_d(M,1)\equiv 0$) or introduce spurious $M$-factors; controlling this needs uniform coefficient bounds not supplied by holonomic theory.
- **Character variety reducibility.** When the nonabelian character variety has several components, the correspondence between components and factors of $\alpha_K$ is not understood; the quantum side has no visible "component" decomposition.

## 6. The Gap

The proven statements are all of the form: *for knots in family $\mathcal{F}$, the universal character ring is reduced, the nonabelian character variety is irreducible, and an explicit recurrence of matching degree is available.* All three hypotheses are used, and none is known for arbitrary knots.

The precise missing step is a **uniform degree/irreducibility theorem**: a bound on the $L$-degree of the minimal recurrence for $J_K$ in terms of a classical invariant (e.g. the $L$-degree of $A_K$, or the number of ideal points of the character variety), together with reducedness of the universal character ring. Given both, Lê's skein-module argument closes the conjecture. Without them, each new knot family requires a bespoke computation, and the general case is untouched.

## 7. Current Research (as of June 2026)

- **Skein algebras at roots of unity.** The Frohman–Kania-Bartoszynska–Lê program on the Azumaya locus and unicity for Kauffman bracket skein algebras gives new algebraic control over $\mathcal{S}_\zeta$; extending it to knot exteriors to force reducedness is an active line (Georgia Tech, Paris-Saclay, Michigan State).
- **Certified holonomic computation.** Koutschan's `HolonomicFunctions` and successors continue to push computations to higher crossing number, with irreducibility certificates; the bottleneck is memory, not method.
- **Quantization / resurgence.** Gukov–Dimofte-style quantization of the A-polynomial, and more recently resurgent analysis of the asymptotic series of $J_K(n)$, predict $\alpha_K$ from the geometry of the $A$-curve. A resurgence-based derivation of AJ for hyperbolic knots is a stated aim *(frontier — verify)*.
- **AJ for cables and satellites.** Following Lê–Tran, incremental extensions to general $(r,s)$-cables and Whitehead doubles are appearing; several such results are announced but not all refereed *(frontier — verify)*.
- **Adjoint and higher-rank analogues.** AJ-type statements for $SL_N$ character varieties and for the adjoint Reidemeister torsion (the "AJ conjecture with torsion") are being formulated; these are conjecturally strictly stronger.

## 8. Future Work

1. **Prove reducedness of the universal character ring** for all knot groups, or characterize the failures. This is the cleanest single target.
2. **Find an a priori $L$-degree bound** on the minimal recurrence, e.g. via the degree of the Jones slopes or the Newton polygon of $A_K$ (Garoufalidis's slope conjectures give the analogous statement for degrees in $q$).
3. **Structural proof of irreducibility** of $\alpha_K$ replacing case-by-case certification, using $q$-difference Galois theory.
4. **Geometric interpretation of the extra $M$-factor**: identify exactly when the "stronger AJ" (no factor) holds; Tran proved it for torus knots, and a general criterion is missing.
5. **Extend to links and 3-manifolds**, where even the $q$-holonomicity statement for multivariable colored Jones is subtler.

## 9. Key References

- **[Foundational]** D. Cooper, M. Culler, H. Gillet, D. D. Long, P. B. Shalen. *Plane curves associated to character varieties of 3-manifolds.* Inventiones Mathematicae 118 (1994), 47–84. [DOI](https://doi.org/10.1007/bf01231526)
- **[Foundational]** S. Garoufalidis. *On the characteristic and deformation varieties of a knot.* Geometry & Topology Monographs 7 (2004), 291–309. [DOI](https://doi.org/10.2140/gtm.2004.7.291)
- **[Foundational]** S. Garoufalidis, T. T. Q. Lê. *The colored Jones function is q-holonomic.* Geometry & Topology 9 (2005), 1253–1293. [DOI](https://doi.org/10.2140/gt.2005.9.1253)
- **[Foundational]** C. Frohman, R. Gelca, W. Lofaro. *The A-polynomial from the noncommutative viewpoint.* Transactions of the AMS 354 (2002), 735–747. [DOI](https://doi.org/10.1090/s0002-9947-01-02889-6)
- **[Foundational]** D. Bullock. *Rings of $SL_2(\mathbb{C})$-characters and the Kauffman bracket skein module.* Commentarii Mathematici Helvetici 72 (1997), 521–542.
- **[Foundational]** J. Przytycki, A. Sikora. *On skein algebras and $Sl_2(\mathbb{C})$-character varieties.* Topology 39 (2000), 115–148.
- **[SOTA]** T. T. Q. Lê. *The colored Jones polynomial and the A-polynomial of knots.* Advances in Mathematics 207 (2006), 782–804. [DOI](https://doi.org/10.1016/j.aim.2006.01.006)
- **[SOTA]** T. T. Q. Lê, A. T. Tran. *On the AJ conjecture for knots.* Indiana University Mathematics Journal 64 (2015), 1103–1151. (With an appendix by V. Q. Huynh.). [DOI](https://doi.org/10.1512/iumj.2015.64.5602)
- **[SOTA]** A. T. Tran. *Proof of a stronger version of the AJ conjecture for torus knots.* Algebraic & Geometric Topology 13 (2013), 609–624. [DOI](https://doi.org/10.2140/agt.2013.13.609)
- **[SOTA]** S. Garoufalidis, C. Koutschan. *Irreducibility of q-difference operators and the knot $7_4$.* Algebraic & Geometric Topology 13 (2013), 3261–3286. [DOI](https://doi.org/10.2140/agt.2013.13.3261)
- **[SOTA]** S. Garoufalidis, X. Sun. *The non-commutative A-polynomial of twist knots.* Journal of Knot Theory and Its Ramifications 19 (2010), 1571–1595. [DOI](https://doi.org/10.1142/s021821651000856x)
- **[Recent / computational]** K. Hikami. *Difference equation of the colored Jones polynomial for torus knot.* International Journal of Mathematics 15 (2004), 959–965. [DOI](https://doi.org/10.1142/s0129167x04002582)
- **[Physics]** S. Gukov. *Three-dimensional quantum gravity, Chern–Simons theory, and the A-polynomial.* Communications in Mathematical Physics 255 (2005), 577–627. [DOI](https://doi.org/10.1007/s00220-005-1312-y)
- **[Survey]** T. T. Q. Lê. *The colored Jones polynomial and the AJ conjecture*, in *Lectures on Quantum Topology in Dimension Three*, Panoramas et Synthèses 48, Société Mathématique de France, 2016.
- **[Tool]** C. Koutschan. *HolonomicFunctions (User's Guide).* RISC Report Series 10-01, Johannes Kepler University Linz, 2010.

## 10. Worked Example / Concrete Special Case

**The trefoil $3_1$ — classical side computed in full.**

The knot group is $\pi_1(S^3\setminus 3_1)=\langle a,b \mid aba=bab\rangle$ with $a,b$ meridians. Put
$$\rho(a)=\begin{pmatrix} m & 1\\ 0 & m^{-1}\end{pmatrix},\qquad \rho(b)=\begin{pmatrix} m & 0\\ -u & m^{-1}\end{pmatrix},$$
so $\operatorname{tr}\rho(ab)=m^2+m^{-2}-u$. Writing out $\rho(aba)=\rho(bab)$ and discarding the reducible locus $u=0$, the relation reduces to the single equation
$$u = m^2+m^{-2}-1,\qquad\text{i.e.}\qquad \operatorname{tr}\rho(ab)=1 .$$
Hence $\rho(ab)$ has characteristic polynomial $x^2-x+1$: its eigenvalues are primitive sixth roots of unity, so
$$\rho\big((ab)^3\big)=-I .$$
The longitude of the trefoil is $\lambda=(ab)^3 a^{-6}$ (the element $(ab)^3$ generates the center and $a^{-6}$ makes $\lambda$ null-homologous). Therefore
$$\rho(\lambda) = -\rho(a)^{-6},$$
whose eigenvalue paired with $M=m$ is $L=-m^{-6}$. Clearing denominators:
$$L M^6 + 1 = 0 .$$
Adding the abelian component $L-1$ gives
$$A_{3_1}(M,L)=(L-1)\,(M^{6}L+1),\qquad\text{so}\qquad A_{3_1}(M^2,L)=(L-1)(M^{12}L+1).$$

**Quantum side.** Habiro's cyclotomic expansion gives
$$J_{3_1}(n)=\sum_{k\ge 0}(-1)^k q^{-k(k+3)/2}\prod_{j=1}^{k}\big(q^{n}+q^{-n}-q^{j}-q^{-j}\big),$$
a $q$-proper-hypergeometric sum. Creative telescoping (Zeilberger's algorithm in the $q$-setting) produces an *inhomogeneous* first-order recurrence in $n$; homogenizing it — multiplying by the operator that kills the inhomogeneous term — yields an operator of $L$-degree $2$,
$$\alpha_{3_1}(M,L,q)=a_2(M,q)L^2+a_1(M,q)L+a_0(M,q),$$
and Garoufalidis (2004) checks minimality. Specializing $q\to 1$ gives, up to a factor in $\mathbb{Z}[M]$,
$$\alpha_{3_1}(M,L,1)\;\doteq\;(L-1)(M^{12}L+1)\;=\;A_{3_1}(M^2,L).$$

**What the example shows.** The two computations share no common language: the left one is a $2\times 2$ matrix equation over a commutative ring; the right one is a telescoping identity for a $q$-hypergeometric sum. AJ asserts they agree for every knot. Note the two degree-matching facts that had to hold: the $L$-degree $2$ of the minimal recurrence equals the $L$-degree of $A_{3_1}$, and the leading coefficient $a_2(M,q)$ does not vanish at $q=1$. Proving those two facts *in general* — rather than verifying them knot by knot — is the whole content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*