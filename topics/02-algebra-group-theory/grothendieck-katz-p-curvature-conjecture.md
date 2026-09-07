---
id: 02-algebra-group-theory/grothendieck-katz-p-curvature-conjecture
title: "Grothendieck-Katz p-curvature Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Grothendieck-Katz p-curvature Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/grothendieck-katz-p-curvature-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $K$ be a number field, $X/K$ a smooth geometrically connected variety, and $(E,\nabla)$ a vector bundle of rank $n$ on $X$ with an integrable connection. Spread out to a model $(\mathcal{X},\mathcal{E},\nabla)$ over a ring of $S$-integers $\mathcal{O}_{K,S}$. For each closed point of $\operatorname{Spec}\mathcal{O}_{K,S}$ of residue characteristic $p$, reduction gives a connection in characteristic $p$, which carries an invariant $\psi_p$, the **$p$-curvature**.

**Conjecture (Grothendieck, 1960s; formalized by Katz).** If $\psi_p = 0$ for almost all primes $p$ (all but finitely many), then $(E,\nabla)$ becomes trivial on a finite étale cover of $X_{\bar K}$ — equivalently, the differential equation $\nabla s = 0$ has a full set of $n$ algebraic solutions, equivalently the differential Galois group of $(E,\nabla)$ is finite.

The converse is elementary: a connection trivialized by a finite étale cover has vanishing $p$-curvature away from the primes dividing the degree and the ramification. So the conjecture asserts that an *arithmetic* condition, checkable prime by prime, detects the *transcendence-theoretic* property of having only algebraic solutions. A complete proof must derive global algebraicity from the family of mod-$p$ vanishing statements; a disproof requires one connection with vanishing $p$-curvature almost everywhere and infinite monodromy.

## 2. Mathematical Foundations

**$p$-curvature.** Let $k$ be a field of characteristic $p>0$, $Y/k$ smooth, $(\mathcal{E},\nabla)$ a connection. For a derivation $D \in \operatorname{Der}_k(\mathcal{O}_Y)$, the $p$-th power $D^p$ is again a derivation, written $D^{[p]}$. Define
$$\psi_p(D) \;=\; \nabla(D)^p - \nabla\!\left(D^{[p]}\right) \;\in\; \operatorname{End}_{\mathcal{O}_Y}(\mathcal{E}).$$
Although $\nabla(D)$ is only $k$-linear, $\psi_p(D)$ is $\mathcal{O}_Y$-linear, and $D \mapsto \psi_p(D)$ is $p$-linear ($\psi_p(fD) = f^p\psi_p(D)$). Thus $\psi_p \in H^0\big(Y, F^*\Omega^1_Y \otimes \operatorname{End}(\mathcal{E})\big)$ where $F$ is the absolute Frobenius. Integrability of $\nabla$ forces $\psi_p$ to commute with $\nabla$, so its characteristic polynomial has coefficients that are horizontal.

**Cartier descent.** $\psi_p = 0$ if and only if $\mathcal{E}$ is spanned locally by horizontal sections, i.e. $\mathcal{E} \cong F^*\mathcal{E}^{\nabla}$ with its canonical connection. Hence vanishing $p$-curvature is exactly "solvable in the Frobenius-twisted sense mod $p$".

**Local form.** On a curve with coordinate $x$, write the system as $\partial Y = A Y$, $A \in M_n(k(x))$, $\partial = d/dx$. Then $\psi_p(\partial) = A_p$ where $A_1 = A$ and $A_{i+1} = \partial A_i + A_i A$; so $A_p$ is the matrix of the $p$-th iterate. Equivalently, for a scalar operator $L = \partial^n + a_{n-1}\partial^{n-1}+\dots+a_0$ over $\mathbb{F}_p(x)$, $\psi_p = 0$ iff $L$ divides $\partial^p$ on the right in the Weyl algebra, iff $L$ has $n$ independent solutions in $\mathbb{F}_p(x)$ after Frobenius twist.

**Differential Galois theory.** Over $\mathbb{C}(X)$, the Picard–Vessiot theory attaches to $(E,\nabla)$ a linear algebraic group $G \subseteq GL_n$, whose identity component measures transcendence. Finiteness of $G$ $\iff$ all solutions algebraic $\iff$ $\pi_1(X_{\bar K})$ acts through a finite quotient. Write $\mathfrak{g} = \operatorname{Lie}(G)$.

**Katz's reformulation (1982).** The conjecture is equivalent to: $\mathfrak{g}$ is the smallest algebraic Lie subalgebra of $\mathfrak{gl}_n$ whose reduction mod $p$ contains the $p$-curvatures $\psi_p$ for almost all $p$. Thus "$\psi_p = 0$ for almost all $p$" should force $\mathfrak{g}=0$.

**Global nilpotence (Katz 1970).** Any Gauss–Manin connection $R^i f_* \Omega^\bullet_{Y/X}$ has *nilpotent* $p$-curvature for almost all $p$; this is the geometric-origin input behind the strongest known cases.

## 3. History & State of the Art (SOTA)

- **1960s.** Grothendieck states the conjecture in correspondence and seminars; it is never published by him. It is motivated by the analogy with the Tate and Hodge conjectures — an arithmetic criterion for a transcendental property — and by Cartier descent.
- **1970.** Katz, *Nilpotent connections and the monodromy theorem*, proves global nilpotence of $p$-curvature for connections of geometric origin (Publ. IHÉS 39).
- **1972.** Katz, *Algebraic solutions of differential equations*, proves the conjecture for Gauss–Manin connections and their subquotients, using the Hodge filtration and Griffiths transversality (Invent. Math. 18).
- **1982.** Katz, *A conjecture in the arithmetic theory of differential equations* (Bull. SMF 110): the Lie-algebra reformulation, reduction steps, and the descent to the case of a connection on an open subset of $\mathbb{A}^1$.
- **1985.** D. V. and G. V. Chudnovsky settle the rank-1 case by Padé-approximation/$G$-function methods.
- **2001–2004.** Bost's algebraicity criteria for formal leaves of algebraic foliations (Publ. IHÉS 93) and André's Arakelov-theoretic arguments give the case of **solvable** differential Galois group.
- **2009.** Farb–Kisin use Margulis superrigidity to prove the conjecture for connections on certain locally symmetric varieties.
- **2018.** Shankar proves it for rank-2 connections on curves under a local monodromy hypothesis around a simple closed loop.
- **2020.** Esnault–Groechenig prove it for cohomologically rigid flat connections on smooth projective varieties, via $F$-isocrystals.

No counterexample is known, and no unconditional proof exists even for rank $2$ on $\mathbb{P}^1 \setminus \{0,1,\infty\}$ in general.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| Rank $n=1$, any base | Proved | Chudnovsky–Chudnovsky (1985); also via Katz's Kummer analysis |
| Gauss–Manin connections and subquotients (all ranks, all dimensions) | Proved | Katz (1972) |
| Solvable differential Galois group $G$ (in particular $G$ abelian, or triangularizable) | Proved | André (2004), Bost (2001) |
| Rank $2$ on a punctured curve with non-virtually-unipotent monodromy about a simple closed loop | Proved | Shankar (2018) |
| Cohomologically rigid flat connections, $X$ smooth projective | Proved | Esnault–Groechenig (2020) |
| Connections on locally symmetric $X$ of rank-$\ge 2$ arithmetic type, $\dim_{\mathbb C} X \ge 2$ | Proved | Farb–Kisin (2009) |
| Hypergeometric ${}_nF_{n-1}$ with rational parameters | Verified by classification: Schwarz's list ($n=2$) and Beukers–Heckman ($n\ge 2$) determine exactly when monodromy is finite; the $p$-curvature criterion matches | Beukers–Heckman (1989) |
| Positive-equicharacteristic analogue | Proved in a variant form | Esnault–Langer (2013) |

Computationally, the vanishing of $\psi_p$ is decidable for a given $L$ and $p$ (compute $A_p$ by $p-1$ differentiations mod $p$, or use the Katz/van Hoeij algorithms); packages in Maple/Magma have checked ranges such as $p < 10^4$ for classical operators (Heun, Lamé, hypergeometric) without discrepancy.

## 5. Principal Obstacles

- **No archimedean information.** Vanishing of $\psi_p$ is a statement at each finite place. Algebraicity of solutions is an assertion about the monodromy representation of $\pi_1(X(\mathbb{C}))$. Nothing in the hypothesis directly bounds the complex-analytic size of solutions, so one must manufacture an archimedean estimate from infinitely many $p$-adic ones. Bost's and the Chudnovskys' proofs do exactly this via Arakelov slope inequalities or Padé approximation, but the bounds degrade with the rank of the connection and only close in the solvable/rank-1 cases.
- **Failure of Hodge input outside geometry.** Katz's 1972 proof needs a Hodge filtration with Griffiths transversality and a lattice of geometric origin. A general connection has no Hodge structure; Simpson-style nonabelian Hodge theory supplies one only for rigid or otherwise special local systems.
- **The Lie-algebra reformulation is circular in practice.** Katz's equivalence converts the conjecture into "$\mathfrak{g}$ is generated by $p$-curvatures", but proving one inclusion needs the very global control the conjecture supplies. Unconditionally one knows only that $\mathfrak{g}$ *contains* the algebra generated by almost all $\psi_p$ after conjugation, not that it equals it.
- **No effective bound on the finite Galois group.** Even granting the conclusion, no known method bounds the degree of the trivializing étale cover in terms of $n$, $\deg$, and the bad primes; without such a bound one cannot run a compactness or Chebotarev argument to finish from finitely many primes.
- **Non-solvable monodromy is invisible to descent.** For $G$ semisimple (e.g. $SL_2$ Zariski-dense monodromy), $p$-curvature can be nilpotent-but-nonzero at every $p$, and the known criteria (Cartier descent, Frobenius structure, Katz's nilpotence) cannot separate "nilpotent" from "zero" uniformly in $p$.

## 6. The Gap

Proved: the conjecture whenever an *extra structure* is available — a Hodge filtration (geometric origin), a solvable Galois group (so the slope inequalities converge), rigidity (so an $F$-isocrystal structure exists), or superrigidity of $\pi_1(X)$. Open: the generic case where $(E,\nabla)$ has Zariski-dense semisimple monodromy, is not rigid, and is not known to come from geometry — already open for rank-2 connections on $\mathbb{P}^1$ minus four points with generic exponents.

The precise missing step: from $\psi_p = 0$ for almost all $p$, produce a *uniform* $p$-adic radius of convergence estimate for the formal horizontal sections at a point, strong enough to feed into an algebraicity criterion (Bost's, or the Borel–Dwork rationality criterion). Currently the estimate obtained is enough only when the Galois group's derived series terminates, or when a Frobenius structure is imported from rigidity.

## 7. Current Research (as of June 2026)

- **Rigidity and companions.** The Esnault–Groechenig programme (Berlin/Toronto) links rigid local systems, integrality, and $F$-isocrystals; extensions to *irregular* and non-cohomologically-rigid connections are being pursued. Reported progress on relaxing projectivity to quasi-projective with tame ramification *(frontier — verify)*.
- **$p$-adic Hodge theory for local systems.** Work in the circle around Petrov, Klevdal–Patrikis, and Litt on de Rham-ness and integrality of $\ell$-adic and $p$-adic local systems supplies new routes to "geometric origin", which would import Katz's 1972 theorem *(frontier — verify)*.
- **Arakelov/Diophantine approximation.** Continuation of Bost–Chambert-Loir style algebraicity criteria; the target is a slope inequality valid for reductive Galois groups.
- **Algorithmic.** Improved algorithms for computing $\psi_p$ and for testing finiteness of differential Galois groups (van Hoeij, Compoint, Singer school; Inria/RISC groups) allow systematic scans of Heun and Lamé families.
- **Positive characteristic analogues.** Esnault–Langer-type equicharacteristic statements as a testing ground for the mechanism.

## 8. Future Work

- Prove the conjecture for rank $2$ on $\mathbb{P}^1 \setminus \{0,1,\infty,\lambda\}$ unconditionally; this is the first genuinely non-solvable, non-rigid case.
- Establish an *effective* Chebotarev-type statement: bound the order of the differential Galois group when it is finite by data of the model, converting the conjecture into a finite computation.
- Extend Bost's slope method beyond solvable groups by finding a filtration replacement for the derived series in the reductive case.
- Settle whether "nilpotent $p$-curvature for almost all $p$" (Dwork's variant) implies geometric origin — a strengthening whose resolution either way would sharpen the picture.
- Develop a motivic formulation: is vanishing $p$-curvature equivalent to the connection being an Artin motive over $X$?

## 9. Key References

- **[Foundational]** N. Katz. *Nilpotent connections and the monodromy theorem: applications of a result of Turrittin.* Publications Mathématiques de l'IHÉS 39 (1970), 175–232.
- **[Foundational]** N. Katz. *Algebraic solutions of differential equations ($p$-curvature and the Hodge filtration).* Inventiones Mathematicae 18 (1972), 1–118.
- **[Foundational]** N. Katz. *A conjecture in the arithmetic theory of differential equations.* Bulletin de la Société Mathématique de France 110 (1982), 203–239 (corrections, 347–348).
- **[Partial results]** D. V. Chudnovsky, G. V. Chudnovsky. *Applications of Padé approximations to the Grothendieck conjecture on linear differential equations.* In: Number Theory (New York 1983–84), Lecture Notes in Mathematics 1135, Springer, 1985, 52–100.
- **[Partial results]** J.-B. Bost. *Algebraic leaves of algebraic foliations over number fields.* Publications Mathématiques de l'IHÉS 93 (2001), 161–221.
- **[Partial results]** Y. André. *Sur la conjecture des $p$-courbures de Grothendieck–Katz et un problème de Dwork.* In: Geometric Aspects of Dwork Theory, Vol. I, Walter de Gruyter, 2004, 55–112.
- **[Partial results]** B. Farb, M. Kisin. *Rigidity, locally symmetric varieties, and the Grothendieck–Katz conjecture.* International Mathematics Research Notices 2009, no. 22, 4159–4167.
- **[SOTA / Recent]** A. Shankar. *The $p$-curvature conjecture and monodromy around simple closed loops.* Duke Mathematical Journal 167 (2018), no. 10, 1951–1980.
- **[SOTA / Recent]** H. Esnault, M. Groechenig. *Rigid connections and $F$-isocrystals.* Acta Mathematica 225 (2020), no. 1, 103–158.
- **[SOTA / Recent]** H. Esnault, A. Langer. *On a positive equicharacteristic variant of the $p$-curvature conjecture.* Documenta Mathematica 18 (2013), 23–50.
- **[Survey]** A. Chambert-Loir. *Théorèmes d'algébricité en géométrie diophantienne (d'après J.-B. Bost, Y. André, D. & G. Chudnovsky).* Séminaire Bourbaki, Exp. 886, Astérisque 282 (2002), 175–209.
- **[Background]** M. van der Put, M. F. Singer. *Galois Theory of Linear Differential Equations.* Grundlehren der mathematischen Wissenschaften 328, Springer, 2003.
- **[Background]** F. Beukers, G. Heckman. *Monodromy for the hypergeometric function ${}_nF_{n-1}$.* Inventiones Mathematicae 95 (1989), 325–354.

## 10. Worked Example / Concrete Special Case

Take $X = \mathbb{G}_m = \operatorname{Spec} K[x,x^{-1}]$, rank $n=1$, and the connection $\nabla = \partial - \tfrac{a}{x}$ with $a \in K$ a number field, $\partial = d/dx$. The horizontal section is $y = x^a$.

**Computing $\psi_p$.** Reduce mod a prime $p$ of good reduction. For a rank-1 operator $\partial + f$ over a field of characteristic $p$, Jacobson's formula gives
$$(\partial + f)^p \;=\; \partial^p + f^p + \partial^{\,p-1}(f).$$
Since $\partial^{[p]} = \partial^p = 0$ on $\mathbb{F}_p(x)$, the $p$-curvature is $\psi_p(\partial) = f^p + \partial^{p-1}(f)$ with $f = -a/x$.

Compute the two terms for odd $p$:
$$f^p = (-a)^p x^{-p} = -a^p x^{-p}, \qquad \partial^{p-1}\!\left(x^{-1}\right) = (-1)^{p-1}(p-1)!\, x^{-p} = (p-1)!\,x^{-p} = -x^{-p},$$
using Wilson's theorem $(p-1)! \equiv -1 \pmod p$. Hence $\partial^{p-1}(-a x^{-1}) = a\,x^{-p}$, and
$$\boxed{\;\psi_p(\partial) \;=\; \left(a - a^{p}\right) x^{-p}\;}$$

**Reading off the conjecture.** $\psi_p = 0 \iff a^p = a$ in the residue field $\iff \bar a \in \mathbb{F}_p$.

- If $a \in \mathbb{Q}$, say $a = r/s$, then $\bar a \in \mathbb{F}_p$ for every $p \nmid s$, so $\psi_p = 0$ for almost all $p$. Correspondingly $y = x^{r/s}$ is algebraic, trivialized by the degree-$s$ étale cover $t \mapsto t^s$ of $\mathbb{G}_m$. Conclusion holds.
- If $a$ is algebraic of degree $d \ge 2$ over $\mathbb{Q}$, say $a = \sqrt 2$, then $\bar a \in \mathbb{F}_p$ exactly when $p$ splits in $\mathbb{Q}(\sqrt2)$, i.e. $p \equiv \pm 1 \pmod 8$. By Chebotarev this is a set of density $1/2$, so $\psi_p \neq 0$ for a positive-density set of primes. Correspondingly $x^{\sqrt2}$ is transcendental and the differential Galois group is $\mathbb{G}_m$, infinite. Hypothesis fails, as it must.
- If $a \notin \bar{\mathbb{Q}}$ the model is not defined over a number field, and the statement does not apply.

This is the entire rank-1 case: the conjecture reduces to the Chebotarev fact that an algebraic number lying in $\mathbb{F}_p$ for almost all $p$ is rational. The difficulty of the general conjecture is that for $n \ge 2$ there is no analogous finite-dimensional "field of definition" argument — vanishing $\psi_p$ becomes a condition on a $p$-linear endomorphism of an $n$-dimensional space whose accumulated content over all $p$ has no direct Galois-theoretic translation.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*