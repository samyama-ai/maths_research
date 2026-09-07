---
id: 05-analysis/khavinson-shapiro-conjecture
title: "Khavinson-Shapiro Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Khavinson-Shapiro Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/khavinson-shapiro-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\Omega \subset \mathbb{R}^n$ ($n \ge 2$) be a bounded domain. Say that $\Omega$ has the **polynomial Dirichlet property** (PDP) if for every polynomial $f \in \mathbb{R}[x_1,\dots,x_n]$ the solution $u$ of

$$\Delta u = 0 \ \text{ in } \Omega, \qquad u|_{\partial\Omega} = f|_{\partial\Omega}$$

is itself (the restriction of) a polynomial.

**Conjecture (Khavinson–Shapiro, 1989/1992).** A bounded domain $\Omega \subset \mathbb{R}^n$ has the polynomial Dirichlet property if and only if $\Omega$ is an ellipsoid, i.e.

$$\Omega = \Big\{ x \in \mathbb{R}^n : \sum_{j=1}^n \frac{(x_j - c_j)^2}{a_j^2} < 1 \Big\}$$

after a rigid motion, with $a_j > 0$.

The "if" direction is classical (Section 4). A complete proof requires the "only if": that PDP forces $\partial\Omega$ to be a quadric. A disproof requires a single bounded non-ellipsoidal $\Omega$ with PDP. Boundedness is essential: half-spaces and slabs have PDP (harmonic reflection across a hyperplane maps polynomials to polynomials), so any proof must use global finiteness of $\Omega$, not local boundary geometry.

## 2. Mathematical Foundations

**Setup.** Assume $\partial\Omega$ is algebraic, $\Omega = \{x : P(x) < 0\}$ with $P \in \mathbb{R}[x]$ of degree $m$, $\nabla P \neq 0$ on $\partial\Omega$. Write $P = P_m + P_{m-1} + \cdots$ for the decomposition into homogeneous parts. Boundedness forces $m = 2k$ even and $P_{2k} \ge 0$.

**Reduction to a Fischer operator.** If $u$ is a polynomial solving the Dirichlet problem with data $f$, then $f - u$ vanishes on $\partial\Omega$, hence $f - u = P Q$ for some polynomial $Q$ (real Nullstellensatz applied to an irreducible $P$ with a smooth real point). Applying $\Delta$:

$$\boxed{\ \Delta(PQ) = \Delta f\ }$$

So PDP is exactly the surjectivity, on $\mathbb{R}[x]$, of the **Fischer-type operator**

$$\mathcal{F}_P : \mathbb{R}[x] \to \mathbb{R}[x], \qquad \mathcal{F}_P(Q) = \Delta(PQ),$$

restricted to the range of $\Delta$ (which is all of $\mathbb{R}[x]$). Note $\deg \mathcal{F}_P(Q) \le \deg Q + 2k - 2$, with equality iff $\Delta(P_{2k}Q_{\deg Q}) \neq 0$ for the top homogeneous part $Q_{\deg Q}$.

**Fischer's theorem (1917).** For $P$ homogeneous of degree $d$, the map $Q \mapsto P^*(D)(PQ)$ is bijective on $\mathbb{R}[x]$, where $P^*(D)$ substitutes $\partial_j$ for $x_j$. For $P = |x|^2$ this gives the harmonic (Almansi–Fischer) decomposition

$$f = |x|^2 q + h, \qquad \Delta h = 0,$$

unique, with $\deg q \le \deg f - 2$, $\deg h \le \deg f$.

**Homogeneous harmonic divisors.** The obstruction to degree control is the space
$$\mathcal{K}(P_{2k}) = \{ Q \text{ homogeneous} : \Delta(P_{2k} Q) = 0 \},$$
i.e. homogeneous polynomials $Q$ for which $P_{2k}Q$ is harmonic. For $k = 1$ and $P_2$ positive definite, $\mathcal{K}(P_2) = \{0\}$ (an energy/positivity argument), and $\mathcal{F}_P$ preserves each finite-dimensional space $\mathcal{P}_d$ of polynomials of degree $\le d$ and is injective there, hence bijective. This is precisely why ellipsoids work.

**Fischer inner product.** On $\mathbb{C}[z]$, $\langle f,g\rangle_F = f(D)\,\overline{g}\,|_{0}$; equivalently the Bargmann–Fock inner product $\int f \bar g\, e^{-|z|^2}$ up to normalization. Multiplication by $P$ and the operator $P^*(D)$ are Fischer-adjoint, which converts surjectivity of $\mathcal{F}_P$ into a bounded-below estimate for an operator on a weighted space of entire functions — Render's method.

## 3. History & State of the Art (SOTA)

- **1877 / 1917.** Ferrers gives explicit harmonic polynomial solutions on ellipsoids; E. Fischer proves the general decomposition theorem that underlies all later work.
- **1989/1992.** D. Khavinson and H. S. Shapiro, studying when *entire* data produce entire solutions, formulate the conjecture (KTH Stockholm research report TRITA-MAT-1989-36; published as *Dirichlet's problem when the data is an entire function*, Bull. LMS 24 (1992) 456–468). They prove that on an ellipsoid entire data yield entire solutions and observe the ellipsoid–Fischer link.
- **1992–2006.** Shapiro's monograph on the Schwarz function embeds the problem in the theory of quadrature domains and harmonic continuation. Ebenfelt, Khavinson and Shapiro analyse singularity propagation for the harmonic continuation of Dirichlet solutions; Bell–Ebenfelt–Khavinson–Shapiro (2006) settle the analogous rationality question in the plane.
- **2001.** Chamberland–Siegel classify domains admitting polynomial solutions for restricted data classes and record explicit non-ellipsoidal failures.
- **2008 (main breakthrough).** H. Render, *Real Bargmann spaces, Fischer decompositions and sets of uniqueness for polyharmonic functions*, Duke Math. J. 142, 313–352: the conjecture is **true** for every bounded $\Omega = \{P<0\}$ whose leading part $P_{2k}$ is *elliptic*, i.e. $P_{2k}(x) > 0$ for all $x \neq 0$. This is the first result covering all dimensions and all degrees at once.
- **2011–2018.** Lundberg–Render reduce the general algebraic case to statements about polynomial decompositions and harmonic divisors; Render (2016) gives a clean equivalence between the conjecture and invertibility properties of Fischer operators; Khavinson–Lundberg's AMS monograph (2018) is the standard reference.

**SOTA summary.** Proven for elliptic leading part in all dimensions; open in general, the obstruction being degenerate leading parts $P_{2k}$ with real zeros off the origin.

## 4. Partial Results / Verified Cases

- **Ellipsoids, all $n \ge 2$, all degrees (proved).** For $P = \sum x_j^2/a_j^2 - 1$, $\mathcal{F}_P$ is a bijection of $\mathcal{P}_d$ for every $d$; data of degree $d$ gives a solution of degree $\le d$ (Ferrers 1877; Fischer 1917).
- **Elliptic leading part (Render 2008).** If $\Omega$ is bounded, $\partial\Omega \subseteq \{P = 0\}$, $\deg P = 2k$ and $P_{2k}$ has no nontrivial real zero, then PDP $\Rightarrow k = 1 \Rightarrow$ ellipsoid. In particular the conjecture is settled for all bounded domains bounded by, e.g., $\{x_1^4 + \cdots + x_n^4 + \text{lower} = 0\}$ and for all strictly convex algebraic boundaries whose top form is definite.
- **Degree-restricted operators.** If PDP holds with the extra requirement $\deg u \le \deg f$ for all $f$ (no degree inflation), the conjecture holds by a direct dimension count on $\mathcal{F}_P$ (Section 10).
- **Entire data on ellipsoids.** Khavinson–Shapiro (1992) and Armitage (2004): if $f$ is entire, the solution on an ellipsoid extends to an entire harmonic function, with explicit growth estimates in terms of the order and type of $f$.
- **Planar rational analogue.** Bell–Ebenfelt–Khavinson–Shapiro (2006): for bounded simply connected planar domains with rational data, rationality of the solution forces the boundary into the ellipse/disk family; Neumann ovals and other non-elliptical quadrature domains fail explicitly.
- **Necessity of boundedness.** Half-spaces, slabs, and certain paraboloid-type unbounded domains have PDP without being ellipsoids — so no purely local argument can work.

## 5. Principal Obstacles

- **Degree inflation.** For $\deg P = 2k \ge 4$, $\mathcal{F}_P$ raises degree by $2k-2$. Solvability for data of degree $d$ needs $\deg Q$ pinned down; a priori $Q$ may have arbitrarily large degree, provided the leading terms cancel, i.e. $\Delta(P_{2k}Q_{top}) = 0$. Every dimension-counting proof collapses unless one rules out these **homogeneous harmonic divisors**.
- **Degenerate top forms.** Render's positivity argument needs $P_{2k} > 0$ off the origin to make $P_{2k}$ act as a bounded-below multiplier in a real Bargmann space. When $P_{2k}$ vanishes on a nontrivial real cone (e.g. $P_{2k} = (x_1^2 + x_2^2)^2 x_3^0$-type degeneracies, or products of quadrics sharing a real zero), the weight degenerates, the multiplication operator loses its lower bound, and the Fischer decomposition can fail to be direct.
- **No usable boundary regularity input.** PDP is a global algebraic condition; potential-theoretic tools (harmonic measure, capacity, boundary Harnack) are insensitive to it and give no leverage.
- **Reflection methods stall above $n=2$.** In the plane one has the Schwarz function and the Riemann map; in $\mathbb{R}^n$, $n \ge 3$, point-to-point harmonic reflection exists essentially only for spheres and hyperplanes (Ebenfelt–Khavinson), so the planar machinery has no higher-dimensional counterpart.
- **Non-compactness of the search space.** One quantifies over all polynomial data of all degrees; failure of PDP must be exhibited at *some* degree, and no effective bound on that degree is known for a given $P$.

## 6. The Gap

Proven: PDP $\Rightarrow$ ellipsoid whenever $P_{2k}$ is elliptic. Conjectured: the same for arbitrary bounded $\Omega$.

The precise missing step: **show that for a bounded domain with $\deg P = 2k \ge 4$, the Fischer operator $\mathcal{F}_P(Q) = \Delta(PQ)$ is never surjective on $\mathbb{R}[x]$.** Equivalently (Render 2016), show that one cannot have simultaneously

1. $\Delta(P_{2k}Q) = 0$ for a nonzero homogeneous $Q$ of high degree (a harmonic divisor supporting degree inflation), **and**
2. surjectivity of the induced map on the associated graded pieces.

Concretely, the open sub-problem is: *classify all homogeneous $R$ of degree $2k \ge 4$, nonnegative on $\mathbb{R}^n$, for which $R \cdot Q$ is harmonic for some $Q \neq 0$.* If the only such $R$ with $R \ge 0$ are the degenerate ones excluded by boundedness, the conjecture follows.

## 7. Current Research (as of June 2026)

- **Fischer-operator school (Render, Dublin; Lundberg, Florida Atlantic).** Extending the real Bargmann-space estimates to weights $e^{-|x|^2}$ twisted by degenerate $P_{2k}$; work on Fischer decompositions for entire functions and for the Helmholtz and polyharmonic operators, aiming at the non-elliptic case. *(frontier — verify)* Recent preprints report the conjecture for $P_{2k}$ a product of positive semidefinite quadratic forms with pairwise transverse zero sets.
- **Quadrature-domain / free-boundary approach (Khavinson, South Florida; Gustafsson, KTH).** Reading PDP as an algebraic property of the Schwarz potential and its singularity set.
- **Real algebraic geometry input.** Treating "$RQ$ harmonic" as a system of linear conditions on the coefficients of $Q$ and studying the resulting determinantal varieties; connects to the classification of harmonic divisors and to positivity certificates (sums of squares) for $P_{2k}$.
- **Computational verification.** Symbolic linear algebra on $\mathcal{F}_P$ over $\mathcal{P}_d$ for explicit quartic and sextic boundaries in $\mathbb{R}^2, \mathbb{R}^3$, confirming non-surjectivity degree by degree; no counterexample has surfaced.

## 8. Future Work

- Prove the harmonic-divisor classification for nonnegative forms of degree 4 in $\mathbb{R}^3$; this would close the first genuinely open case beyond Render's theorem.
- Replace the ellipticity hypothesis by a weaker Łojasiewicz-type lower bound $P_{2k}(x) \gtrsim \operatorname{dist}(x, Z)^{\alpha}|x|^{2k-\alpha}$ near the real zero cone $Z$, and check whether the Bargmann-space estimates survive.
- Develop an effective degree bound: for given $\deg P = 2k$ and $n$, produce $D(n,k)$ such that PDP failure is already visible for data of degree $\le D(n,k)$. This would make the conjecture decidable domain by domain.
- Study the analogue for other constant-coefficient elliptic operators (Helmholtz, polyharmonic $\Delta^m$), where the ellipsoid answer sometimes changes — a source of structural insight into what is special about $\Delta$.
- Settle the entire-data version: characterize bounded domains for which entire data always give entire solutions; this is formally weaker and may fall first.

## 9. Key References

- **[Foundational]** E. Fischer. *Über die Differentiationsprozesse der Algebra.* Journal für die reine und angewandte Mathematik **148** (1917), 1–78.
- **[Foundational]** N. M. Ferrers. *An Elementary Treatise on Spherical Harmonics and Subjects Connected with Them.* Macmillan, London, 1877.
- **[Foundational]** D. Khavinson, H. S. Shapiro. *Dirichlet's problem when the data is an entire function.* Bulletin of the London Mathematical Society **24** (1992), 456–468.
- **[Foundational]** H. S. Shapiro. *The Schwarz Function and Its Generalization to Higher Dimensions.* Wiley-Interscience, 1992.
- **[SOTA]** H. Render. *Real Bargmann spaces, Fischer decompositions and sets of uniqueness for polyharmonic functions.* Duke Mathematical Journal **142** (2008), 313–352.
- **[SOTA]** E. Lundberg, H. Render. *The Khavinson–Shapiro conjecture and polynomial decompositions.* Journal of Mathematical Analysis and Applications **376** (2011), 506–513.
- **[SOTA]** H. Render. *A characterization of the Khavinson–Shapiro conjecture via Fischer operators.* Potential Analysis **45** (2016), 539–543.
- **[Related]** S. Bell, P. Ebenfelt, D. Khavinson, H. S. Shapiro. *On the classical Dirichlet problem in the plane with rational data.* Journal d'Analyse Mathématique **100** (2006), 157–190.
- **[Related]** D. H. Armitage. *The Dirichlet problem when the boundary function is entire.* Journal of Mathematical Analysis and Applications **291** (2004), 565–577.
- **[Related]** M. Chamberland, D. Siegel. *Polynomial solutions to Dirichlet problems.* Proceedings of the American Mathematical Society **129** (2001), 211–217.
- **[Survey]** D. Khavinson, E. Lundberg. *Linear Holomorphic Partial Differential Equations and Classical Potential Theory.* Mathematical Surveys and Monographs **232**, American Mathematical Society, 2018.
- **[Survey]** D. Khavinson, E. Lundberg. *A tale of ellipsoids in potential theory.* Notices of the American Mathematical Society **61**(2) (2014), 148–156.
- **[Survey]** P. Ebenfelt, D. Khavinson, H. S. Shapiro. *Algebraic aspects of the Dirichlet problem.* In *Quadrature Domains and Their Applications*, Operator Theory: Advances and Applications **156**, Birkhäuser, 2005, 151–172.

## 10. Worked Example / Concrete Special Case

**(a) The ellipse works.** Take $\Omega = \{P < 0\}$ in $\mathbb{R}^2$ with $P(x,y) = \frac{x^2}{a^2} + \frac{y^2}{b^2} - 1$ and data $f(x,y) = x^2$. Seek $u = f - cP$ with $c$ constant:

$$\Delta u = \Delta(x^2) - c\,\Delta P = 2 - c\Big(\frac{2}{a^2} + \frac{2}{b^2}\Big) = 0 \implies c = \frac{a^2b^2}{a^2+b^2}.$$

Hence

$$u(x,y) = x^2 - \frac{a^2b^2}{a^2+b^2}\Big(\frac{x^2}{a^2}+\frac{y^2}{b^2}-1\Big) = \frac{a^2}{a^2+b^2}\,(x^2-y^2) + \frac{a^2b^2}{a^2+b^2}.$$

Check: $\Delta u = 0$, and on $\partial\Omega$ we have $P=0$ so $u = x^2 = f$. The solution is a polynomial of the same degree as the data. The same computation with general $f$ amounts to inverting $\mathcal{F}_P$ on $\mathcal{P}_d$, which is possible because $\mathcal{F}_P$ maps $\mathcal{P}_d$ into $\mathcal{P}_d$ and is injective there.

**(b) A quartic boundary fails — the counting argument.** Let $n=2$ and $P = P_4 + P_3 + \cdots$ with $\deg P = 4$, $\Omega=\{P<0\}$ bounded. Suppose, as Render's ellipticity hypothesis guarantees, that
$$\Delta(P_4 Q) \neq 0 \quad \text{for every nonzero homogeneous } Q. \tag{$\ast$}$$
Then for any $Q$ of degree $m$, $\deg \Delta(PQ) = m + 2$ exactly. Solving $\Delta(PQ) = \Delta f$ with $\deg f = d$ forces $m + 2 = d - 2$, i.e. $\deg Q = d-4$. So PDP requires the linear map

$$\mathcal{F}_P : \mathcal{P}_{d-4} \longrightarrow \mathcal{P}_{d-2}$$

to be surjective. But in $\mathbb{R}^2$, $\dim \mathcal{P}_j = \binom{j+2}{2}$, so

$$\dim \mathcal{P}_{d-4} = \frac{(d-2)(d-3)}{2}, \qquad \dim \mathcal{P}_{d-2} = \frac{d(d-1)}{2},$$

a deficit of $\frac{d(d-1) - (d-2)(d-3)}{2} = 2d - 3 > 0$ for every $d \ge 2$. Surjectivity is impossible, so PDP fails: some polynomial datum of degree $d$ has a non-polynomial harmonic extension. The identical count in $\mathbb{R}^n$ gives a deficit growing like $d^{n-2}$.

**(c) Where the general case breaks.** Step (b) used $(\ast)$. If some nonzero homogeneous $Q_0$ satisfies $\Delta(P_4 Q_0)=0$, the degree of $Q$ is no longer pinned to $d-4$: one may add multiples of $Q_0$ and higher-degree corrections, and the source space becomes infinite-dimensional relative to the target. The whole conjecture is the assertion that this escape route never actually produces solutions for a bounded domain — that is exactly the gap identified in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*