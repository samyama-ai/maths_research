---
id: 05-analysis/smales-mean-value-conjecture
title: "Smale's Mean Value Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Smale's Mean Value Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/smales-mean-value-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $p$ be a complex polynomial of degree $d \ge 2$ and let $z_0 \in \mathbb{C}$ be a point with $p'(z_0) \neq 0$. Let $\theta_1,\dots,\theta_{d-1}$ be the critical points of $p$ (the zeros of $p'$, listed with multiplicity). Smale's mean value conjecture asserts

$$\min_{1 \le j \le d-1} \left| \frac{p(\theta_j) - p(z_0)}{(\theta_j - z_0)\, p'(z_0)} \right| \;\le\; \frac{d-1}{d}.$$

By the affine invariance of the quantity (Section 2) one may normalize $z_0 = 0$, $p(0) = 0$, $p'(0) = 1$, in which case the claim is

$$S(p) := \min_{j} \left| \frac{p(\theta_j)}{\theta_j} \right| \;\le\; \frac{d-1}{d}.$$

A complete proof must establish the inequality for **every** degree $d \ge 2$ and every normalized $p$. A disproof requires one explicit polynomial with $S(p) > (d-1)/d$. The constant is sharp: $p(z) = z^d - dz$ (normalized: $z - z^d/d$) attains equality, so no smaller constant works. The conjecture is open for every $d \ge 5$ in full generality, and the best universal constants remain bounded away from $(d-1)/d$ as $d \to \infty$.

## 2. Mathematical Foundations

**Setup.** Write $\mathcal{P}_d$ for polynomials of degree exactly $d$ over $\mathbb{C}$, and for $p \in \mathcal{P}_d$ with $p'(0) \neq 0$, $p(0)=0$ define the *Smale factor*

$$S(p) = \min\left\{ \left| \frac{p(\theta)}{\theta\, p'(0)} \right| : p'(\theta) = 0 \right\}, \qquad S(d) = \sup\{ S(p) : p \in \mathcal{P}_d,\ p(0)=0,\ p'(0)\neq 0 \}.$$

The conjecture is $S(d) = \frac{d-1}{d}$.

**Invariance.** For $a,b \in \mathbb{C}^{*}$ the map $p(z) \mapsto a\,p(bz)$ sends critical points $\theta \mapsto \theta/b$, sends $p(\theta)/(\theta p'(0))$ to itself, and hence fixes $S(p)$. This two-parameter scaling group lets one normalize $p(z) = z + c_2 z^2 + \cdots + c_d z^d$, leaving a $(d-2)$-dimensional moduli space $\{(c_2,\dots,c_d) : c_d \neq 0\}$ modulo the residual $\mathbb{Z}$-action.

**Motivation (Newton's method).** Smale's estimate arose from complexity analysis of the fundamental theorem of algebra. If $S(p)$ is bounded below for all $p$, then a rescaled Newton step
$$z_{n+1} = z_n - h\,\frac{p(z_n)}{p'(z_n)}$$
cannot be blocked by critical points too close to $z_0$ relative to their critical values; the quantity $|p(\theta)/(\theta p'(0))|$ measures exactly the "flatness" of $p$ between $z_0$ and a critical point.

**Geometric function theory reformulation.** Put $q = p / p'(0)$, so $q(0)=0,\ q'(0)=1$. Let $\Omega = \mathbb{C} \setminus q(\mathrm{Crit}(q))$ be the complement of the critical values, and let $\Omega_0$ be the component of $q^{-1}(\Omega)$ containing $0$. Then $q : \Omega_0 \to \Omega$ is an unbranched covering, and the branch $f = q^{-1}$ fixing $0$ is a locally univalent map from a disc onto $\Omega_0$. Bounding $S(p)$ from above becomes a distortion problem: how far can the nearest singularity of $f$ be from the origin? Applying the Koebe $1/4$-theorem to the univalent branch of $q^{-1}$ on the largest disc $|w| < r$ avoiding critical values gives Smale's original
$$S(p) \le 4,$$
since $\tfrac14 \le S(p)/1$ forces $r \le 4\,|p(\theta)/\theta|$-type control. Sharper versions replace Koebe by hyperbolic-metric comparison on $\Omega$ (Beardon–Minda–Ng) or by coefficient estimates for univalent functions (Conte–Fujikawa–Lakic).

**Dual problem.** The *dual mean value conjecture* (Dubinin–Sugawa) replaces $\min$ by $\max$ and reverses the inequality:
$$\max_j \left| \frac{p(\theta_j)}{\theta_j\, p'(0)} \right| \;\ge\; \frac{1}{d},$$
extremal again for $z^d - dz$ up to the normalization. The two problems bracket the multiset $\{|p(\theta_j)/\theta_j|\}$ from both sides.

## 3. History & State of the Art (SOTA)

- **1981.** Stephen Smale, *The fundamental theorem of algebra and complexity theory* (Bull. AMS 4, 1–36), proves $S(p) \le 4$ and asks whether $4$ can be replaced by $1$ or $(d-1)/d$. The formulation with $(d-1)/d$ became the standard conjecture.
- **1989.** David Tischler analyzes the structure of extremal polynomials and settles low degrees, showing $z^d - dz$ is the unique extremal in its class.
- **2002.** Beardon, Minda and Ng use the hyperbolic metric of the complement of the critical values to give the first universal constant strictly below $4$ for each fixed $d$, of the form $4^{(d-2)/(d-1)}$.
- **2007.** Conte, Fujikawa and Lakic obtain $S(p) \le 4\,\frac{d-1}{d+1}$ via de Branges-type coefficient bounds for univalent functions — again $\to 4$ as $d \to \infty$.
- **2007.** Edward Crane produces the first bound with an *absolute* gain for large degree: $S(p) < 4 - \frac{c}{\sqrt{d}}$ with an explicit constant $c \approx 2.263$ for $d$ large.
- **2007.** Marinov and Sendov verify the conjecture computationally for degrees $d \le 10$.
- **2009 onward.** Dubinin–Sugawa formulate and partially resolve the dual problem; Ng and coauthors transport the question to finite Blaschke products, where an analogous sharp inequality can be proved in cases the polynomial problem resists.

Status summary: the conjectured constant $(d-1)/d < 1$ is known only in special classes; every unconditional universal bound proved to date is $\ge 1$, and in fact $\to 4$ or $4-o(1)$.

## 4. Partial Results / Verified Cases

- **Degrees $d = 2,3,4$:** proved unconditionally. $d=2$ is a one-line computation; $d=3,4$ follow from explicit elimination in the normalized moduli space (Tischler).
- **Degrees $5 \le d \le 10$:** verified by computer-assisted global optimization over the normalized coefficient space (Marinov–Sendov, 2007). These are numerical certifications, not symbolic proofs.
- **Odd polynomials:** if $p(-z) = -p(z)$, the conjecture holds for all $d$ (Ng, 2003).
- **Polynomials with a single critical value**, i.e. $p(\theta_j)$ independent of $j$: extremals are exactly $a\big((bz)^d - d(bz)\big)$, and the bound holds with equality only there (Tischler).
- **Real polynomials with all critical points real** and other "collinear critical point" families: the covering-space argument closes because $\Omega$ is a slit plane with computable hyperbolic metric.
- **Universal bounds valid for all $d$:** $S(p) \le 4$ (Smale); $S(p) \le 4^{(d-2)/(d-1)}$ (Beardon–Minda–Ng); $S(p) \le 4\frac{d-1}{d+1}$ (Conte–Fujikawa–Lakic); $S(p) < 4 - 2.263\,d^{-1/2}$ for large $d$ (Crane).
- **Dual conjecture:** holds for $d \le 4$ and for the same symmetric families; general lower bounds of order $c/d$ with $c<1$ are known.

## 5. Principal Obstacles

- **Koebe-type distortion is intrinsically a factor-of-4 tool.** Every proof route through univalent-function theory ($1/4$-theorem, Grunsky/de Branges coefficient bounds, hyperbolic-metric comparison) is sharp for the Koebe function $z/(1-z)^2$, which is *not* a polynomial. The extremal for the conjecture, $z - z^d/d$, is far from Koebe-extremal, so these methods lose a constant factor of about $4d/(d-1)$ that no refinement of the same argument recovers.
- **Loss of the degree constraint.** Passing from $p$ to the inverse branch $q^{-1}$ discards the information that $q$ is a *polynomial of degree exactly $d$* with exactly $d-1$ critical points counted with multiplicity. The function-theoretic problem with that constraint dropped genuinely has answer $\approx 4$.
- **The optimization is non-convex with many critical configurations.** In normalized coordinates $S$ is a min of $d-1$ moduli of algebraic functions of $(c_2,\dots,c_d)$; the objective is non-smooth exactly where two of these moduli coincide, and the conjectured maximizer sits at a highly degenerate point where all $d-1$ values are equal. Standard Lagrange/variational arguments produce systems of resultants whose degree grows rapidly, which is why symbolic verification stops near $d = 4$ and numerical verification near $d = 10$.
- **No compactness.** The normalized family is unbounded ($c_d \to 0$ degenerates the degree), so a maximizer must first be shown to exist in the interior; the boundary behaviour is delicate.
- **The inequality is tight.** Because equality is attained, any proof must be exactly sharp — no $\varepsilon$-room, so soft or averaging arguments are excluded from the outset.

## 6. The Gap

Proved: $S(d) \le 4 - O(d^{-1/2})$ for all $d$, and $S(d) = (d-1)/d$ for $d \le 4$ (plus numerics to $d=10$ and structured subclasses). Conjectured: $S(d) = (d-1)/d < 1$.

The gap is therefore a **multiplicative factor of roughly $4$, uniform in $d$** — the whole difference between "an absolute constant coming from the Koebe theorem" and "the sharp polynomial constant". Even the qualitative statement $S(d) \le 1$ (equivalently: some critical point $\theta$ satisfies $|p(\theta)| \le |\theta\,p'(0)|$) is open for every $d \ge 5$. Crossing it requires an argument that uses the finiteness of the critical set — the number $d-1$ — quantitatively, rather than only through the topology of the covering $q : \Omega_0 \to \Omega$.

## 7. Current Research (as of June 2026)

- **Blaschke-product transfer.** Finite Blaschke products of degree $d$ are the hyperbolic analogue of polynomials; sharp mean-value inequalities have been established there, and current work asks whether a degeneration of the disc model to the plane recovers the polynomial statement. Groups at the University of Hong Kong (Ng and collaborators) lead this line. *(frontier — verify)*
- **Refined hyperbolic-metric estimates** on the critical-value complement, using the fact that $\Omega$ omits at most $d-1$ points, to beat Crane's $4 - c d^{-1/2}$ by a constant factor. *(frontier — verify)*
- **Certified global optimization** (interval arithmetic, sums-of-squares relaxations of the polynomial system) aiming to push exact verification past $d = 10$; the bottleneck is resultant size.
- **Dual and two-sided problems**, where Dubinin–Sugawa-style symmetrization arguments are more tractable, in the hope that a combined bracket $\frac{1}{d} \le \max$, $\min \le \frac{d-1}{d}$ admits a single unified proof.
- **Connections to Sendov-type geometry of polynomials** and to $\alpha$-theory bounds for Newton's method, which supply the original complexity-theoretic motivation.

## 8. Future Work

- Prove the *weak* form $S(d) \le 1$ for all $d$; leading commentators (Sheil-Small, Crane) treat this as the decisive qualitative step, since it would show that some critical point is always "non-flat".
- Establish existence and uniqueness of an extremal polynomial for each $d$ and derive its Euler–Lagrange equations; a proof that any extremal has a single critical value would finish the conjecture by Tischler's classification.
- Develop a distortion theory for *locally univalent maps of bounded valence* in which the sharp constant is $4(d-1)/(d+1)$-free — i.e. replace Koebe by a $d$-aware extremal function.
- Settle the conjecture for polynomials whose critical points lie on a circle or a line, generalizing the odd-polynomial case.
- Extend certified numerics to $d \le 20$ to test whether $S(d) = (d-1)/d$ persists or whether near-extremal families with several distinct critical values appear.

## 9. Key References

- **[Foundational]** S. Smale. *The fundamental theorem of algebra and complexity theory.* Bulletin of the American Mathematical Society (N.S.) 4 (1981), 1–36.
- **[Foundational]** D. Tischler. *Critical points and values of complex polynomials.* Journal of Complexity 5 (1989), 438–456. [DOI](https://doi.org/10.1016/0885-064x(89)90019-8)
- **[SOTA]** A. F. Beardon, D. Minda, T. W. Ng. *Smale's mean value conjecture and the hyperbolic metric.* Mathematische Annalen 322 (2002), 623–632. [DOI](https://doi.org/10.1007/s002080000184)
- **[SOTA]** E. Crane. *A bound for Smale's mean value conjecture for complex polynomials.* Bulletin of the London Mathematical Society 39 (2007), 781–791. [DOI](https://doi.org/10.1112/blms/bdm063)
- **[SOTA]** A. Conte, E. Fujikawa, N. Lakic. *Smale's mean value conjecture and the coefficients of univalent functions.* Proceedings of the American Mathematical Society 135 (2007), 3295–3300. [DOI](https://doi.org/10.1090/s0002-9939-07-08861-2)
- **[Partial result]** T. W. Ng. *Smale's mean value conjecture for odd polynomials.* Journal of the Australian Mathematical Society 75 (2003), 409–411. [DOI](https://doi.org/10.1017/s1446788700008181)
- **[Computational]** M. Marinov, B. Sendov. *Verification of Smale's mean value conjecture for $n \le 10$.* Comptes Rendus de l'Académie Bulgare des Sciences 60 (2007), 1151–1156.
- **[Dual problem]** V. N. Dubinin, T. Sugawa. *Dual mean value problem for complex polynomials.* Proceedings of the Japan Academy, Series A 85 (2009), 135–137. [DOI](https://doi.org/10.3792/pjaa.85.135)
- **[Survey / Book]** T. Sheil-Small. *Complex Polynomials.* Cambridge Studies in Advanced Mathematics 75, Cambridge University Press, 2002 (Chapter on Smale's conjecture).
- **[Book]** Q. I. Rahman, G. Schmeisser. *Analytic Theory of Polynomials.* London Mathematical Society Monographs, Oxford University Press, 2002.

## 10. Worked Example / Concrete Special Case

**Degree $d = 3$.** Normalize $p(z) = z + c z^2 + e z^3$ with $e \neq 0$, so $p(0)=0$, $p'(0)=1$, and the target is $S(p) \le \tfrac23$.

Critical points $\theta_1,\theta_2$ are the roots of $p'(z) = 1 + 2cz + 3ez^2$, so
$$\theta_1\theta_2 = \frac{1}{3e}, \qquad \theta_1 + \theta_2 = -\frac{2c}{3e}.$$

At a critical point, $3e\theta^2 = -(1+2c\theta)$, hence
$$\frac{p(\theta)}{\theta} = 1 + c\theta + e\theta^2 = 1 + c\theta - \frac{1+2c\theta}{3} = \frac{2 + c\theta}{3}.$$

Multiplying the two values and substituting the symmetric functions:
$$\frac{p(\theta_1)}{\theta_1}\cdot\frac{p(\theta_2)}{\theta_2} = \frac{(2+c\theta_1)(2+c\theta_2)}{9} = \frac{4 + 2c(\theta_1+\theta_2) + c^2\theta_1\theta_2}{9} = \frac{4 - \frac{4c^2}{3e} + \frac{c^2}{3e}}{9} = \frac{4 - c^2/e}{9}.$$

**Check the extremal.** For $p(z) = z - z^3/3$ (i.e. $c=0$, $e=-1/3$, an affine rescaling of $z^3 - 3z$) the product is $4/9$, and by symmetry each factor has modulus $2/3$. So $S(p) = \tfrac23 = \tfrac{d-1}{d}$: the bound is attained.

**Why it is not automatic.** If $|4 - c^2/e| \le 4$ the product of the two moduli is $\le 4/9$, so the smaller factor is $\le 2/3$ and we are done. But $t := c^2/e$ is an unconstrained complex parameter, so the product alone does not suffice. Set $v_j = 2 + c\theta_j$, so $S(p) = \tfrac13\min_j |v_j|$ and we must show $\min_j |v_j| \le 2$. From the relations above, $v_1v_2 = 4 - t$ and $v_1 + v_2 = 4 - \tfrac{2t}{3}$, and eliminating $t$ gives the single constraint
$$3(v_1+v_2) = 4 + 2v_1v_2.$$
Assume for contradiction $|v_1|, |v_2| > 2$ and write $a=|v_1|, b=|v_2|$. Then $2ab - 4 \le |2v_1v_2 + 4| = 3|v_1+v_2| \le 3(a+b)$. Substituting $a = 2+x$, $b = 2+y$ with $x,y>0$ reduces this to $x + y + 2xy \le 8$ — not immediately contradictory, so the putative counterexamples are confined to the **compact** region $x,y \in (0,4]$, where the constraint $3(v_1+v_2) = 4 + 2v_1v_2$ is a plane conic in $(v_1,v_2)$ and can be checked directly to force $\min(|v_1|,|v_2|) \le 2$, with equality only at $v_1=v_2=-2$, i.e. exactly the polynomial $z - z^3/3$.

This is the whole difficulty in miniature: a soft product estimate gets to within a bounded factor, and the sharp statement survives only after a finite but delicate analysis of a compact degenerate locus. For $d \ge 5$ that locus is a positive-dimensional algebraic variety, and no analogue of the last step is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*