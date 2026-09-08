---
id: 05-analysis/corona-theorem
title: "Corona Theorem"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Corona Theorem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/corona-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $H^\infty(\Omega)$ be the Banach algebra of bounded holomorphic functions on a domain $\Omega$, with the sup norm. Its maximal ideal space $\mathcal{M}(H^\infty(\Omega))$ — the set of nonzero multiplicative linear functionals with the weak-$*$ topology — contains a copy of $\Omega$ via point evaluations $f \mapsto f(\lambda)$. The **corona problem** asks whether $\Omega$ is dense in $\mathcal{M}(H^\infty(\Omega))$, i.e. whether the "corona" $\mathcal{M} \setminus \overline{\Omega}$ is empty.

Equivalently (Gelfand duality), the question is a Bézout statement: given $f_1,\dots,f_n \in H^\infty(\Omega)$ with

$$\delta \;:=\; \inf_{z \in \Omega} \max_{1 \le j \le n} |f_j(z)| \;>\; 0, \qquad \|f_j\|_\infty \le 1,$$

do there exist $g_1,\dots,g_n \in H^\infty(\Omega)$ with

$$\sum_{j=1}^n f_j(z)\, g_j(z) \;=\; 1 \quad \text{for all } z \in \Omega ?$$

**Carleson (1962)** proved this for $\Omega = \mathbb{D}$, the unit disc, with a bound $\|g_j\|_\infty \le C(n,\delta)$. The problem is therefore *solved* in its classical form; the label "solved-recently" here tracks the still-open generalizations that carry the same name:

- **(C1) Polydisc / ball.** Is the corona theorem true for $H^\infty(\mathbb{D}^n)$ or $H^\infty(\mathbb{B}_n)$, $n \ge 2$? **Open.**
- **(C2) Planar domains and Riemann surfaces.** True for arbitrary plane domains? **Open.** False for general Riemann surfaces (Cole).
- **(C3) Sharp constants.** Determine the optimal growth of $C(\delta)$ as $\delta \to 0^+$. **Open.**

A complete resolution of (C1) means either a Bézout identity with a uniform bound, or a construction of $f_j$ satisfying the hypothesis for which $1 \notin (f_1,\dots,f_n)$.

## 2. Mathematical Foundations

**Hardy spaces.** For $0 < p \le \infty$, $H^p(\mathbb{D}) = \{f \text{ holomorphic} : \sup_{r<1}\int_0^{2\pi}|f(re^{i\theta})|^p\,\tfrac{d\theta}{2\pi} < \infty\}$. Every $f \in H^\infty$ has nontangential boundary values a.e. and $\|f\|_{H^\infty} = \|f\|_{L^\infty(\mathbb{T})}$.

**Carleson measures.** A positive measure $\mu$ on $\mathbb{D}$ is Carleson if there is $C$ with $\mu(S(I)) \le C|I|$ for every boundary arc $I$, where $S(I) = \{re^{i\theta}: e^{i\theta}\in I,\ 1-|I| < r < 1\}$. Carleson's embedding theorem: $\mu$ is Carleson $\iff$ $\|f\|_{L^p(\mu)} \lesssim \|f\|_{H^p}$.

**The $\bar\partial$ route (Hörmander, Wolff).** Put $\Phi = \sum_j |f_j|^2 \ge \delta^2$ and $\varphi_j = \bar f_j / \Phi$, so $\sum_j f_j \varphi_j = 1$ but $\varphi_j$ is merely smooth. Seek $b_{jk} \in C^\infty$, $b_{jk} = -b_{kj}$, solving

$$\bar\partial b_{jk} \;=\; \varphi_j \,\bar\partial \varphi_k - \varphi_k\, \bar\partial\varphi_j \;=:\; \omega_{jk}.$$

Then $g_j = \varphi_j + \sum_k b_{jk} f_k$ is holomorphic and $\sum_j f_j g_j = 1$ by antisymmetry. The whole difficulty is an $L^\infty$ estimate for $\bar\partial$: one needs $\|b\|_\infty \lesssim \|\,|\omega|^2 \,dx\,dy\,\|_{\mathrm{Carleson}}^{1/2}$, which holds in one variable because

$$b(z) = \frac{1}{2\pi i}\int_{\mathbb{T}} \frac{(1-|\zeta|^2)\,\omega(\zeta)}{ \dots }\,\text{(Wolff's kernel)}$$

can be dualized against $H^1$ via the $H^1$–$BMO$ duality of Fefferman and the Littlewood–Paley identity
$$\|h\|_{H^1} \asymp |h(0)| + \int_{\mathbb{D}} |h'(z)|\,\log\tfrac{1}{|z|}\,dA(z).$$

**Wolff's lemma.** If $|\omega|^2\log\frac{1}{|z|}\,dA$ and $|\bar\partial\omega|\log\frac{1}{|z|}\,dA$ are both Carleson measures, then $\bar\partial b = \omega$ has a solution $b \in L^\infty(\mathbb{T})$ with a bound by the Carleson norms. This is the engine of the modern proof (Garnett, *Bounded Analytic Functions*, Ch. VIII).

**Uniform algebras.** $H^\infty(\Omega) \subset C_b(\Omega)$ is a uniform algebra; $\mathcal{M}$ is compact Hausdorff, and $\Omega$ dense in $\mathcal{M}$ $\iff$ the Bézout problem is solvable, since a corona point is exactly a character killing an ideal $(f_1,\dots,f_n)$ with $\inf \max_j |f_j| > 0$.

## 3. History & State of the Art

- **1941.** Kakutani poses the corona question for $H^\infty(\mathbb{D})$; it circulates as the "corona problem" (named for the possible fringe $\mathcal{M}\setminus\overline{\mathbb{D}}$ around the disc).
- **1962.** **Lennart Carleson**, *Interpolations by bounded analytic functions and the corona problem*, Ann. of Math. **76**, 547–559: the disc case, via Carleson measures and a delicate contour/stopping-time construction.
- **1967.** Hörmander recasts the argument through $\bar\partial$ with weights; Kerzman and others push $L^p$ theory.
- **1979–80.** **T. Wolff** gives the short $\bar\partial$ proof (unpublished, disseminated in Garnett's book) and proves the **ideal theorem**: if $|h| \le \big(\sum_j |f_j|^2\big)^{1/2}$ then $h^3 \in (f_1,\dots,f_n)$; $h^2$ is *not* enough (Rao's counterexample).
- **1970s–80s.** Corona theorems for finitely connected domains (Stout, Alling), Behrens' infinitely connected domains with well-separated boundary components, and **Garnett–Jones (1985)** for Denjoy domains ($\Omega = \mathbb{C}\setminus E$, $E \subset \mathbb{R}$ closed).
- **1970s.** **B. Cole** constructs a Riemann surface for which the corona theorem *fails* (see Gamelin, *Uniform Algebras*), killing any purely potential-theoretic proof strategy.
- **1987–93.** **Sibony**, and **Fornæss–Sibony**, produce smoothly bounded pseudoconvex domains in $\mathbb{C}^2$ where corona and $L^p$ $\bar\partial$-estimates fail — so the several-variable statement cannot be a soft consequence of pseudoconvexity.
- **2002.** **Treil** settles Wolff's question on the ideal problem and sharpens corona constants.
- **2011.** **Costea–Sawyer–Wick** prove a corona theorem for the multiplier algebra of the Drury–Arveson space and Besov–Sobolev spaces $B_2^\sigma(\mathbb{B}_n)$, $0 \le \sigma \le 1/2$ — the strongest positive several-variable result.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $\mathbb{D} \subset \mathbb{C}$, $n$ generators, any $n \le \infty$ | **True** (Carleson 1962; infinitely many generators: Rosenblum, Tolokonnikov, Uchiyama) with $C(\delta)$ independent of $n$ |
| Finitely connected plane domains | **True** (Stout, Alling) |
| Denjoy domains $\mathbb{C}\setminus E$, $E\subset\mathbb{R}$ | **True** (Garnett–Jones, *Acta Math.* 155, 1985) |
| Widom / Behrens-type infinitely connected domains | **True** under separation or Green's-function hypotheses |
| Half-plane, annulus, $H^\infty$ of a strip | **True** (conformal transport) |
| $H^\infty(\mathbb{D}) \otimes M_{n}$, finite matrices | **True** (Fuhrmann, Vasyunin); operator-valued with $\dim = \infty$: **False** (Treil 1989) |
| Multiplier algebra of Dirichlet space, Drury–Arveson space on $\mathbb{B}_n$ | **True** (Tolokonnikov; Trent; Costea–Sawyer–Wick 2011) |
| Smooth pseudoconvex $\Omega \Subset \mathbb{C}^2$ (special constructions) | **False** (Sibony 1987; Fornæss–Sibony 1993) |
| General Riemann surfaces | **False** (Cole) |
| $H^\infty(\mathbb{D}^n)$, $H^\infty(\mathbb{B}_n)$, $n\ge2$ | **Open** |
| General plane domains | **Open** |

Quantitatively, in $\mathbb{D}$ with $n = 2$ and $\|f_j\|\le1$ one may take $\|g\|_\infty \le C\,\delta^{-2}\log(1/\delta)$; the best known lower bound on the optimal constant is of order $\delta^{-2}$, so a single $\log(1/\delta)$ separates upper and lower bound.

## 5. Principal Obstacles

- **No $L^\infty$ $\bar\partial$-theory in $\mathbb{C}^n$.** The one-variable proof rests on solving $\bar\partial b = \omega$ with $\|b\|_\infty$ controlled by a Carleson norm. In $\ge 2$ variables the Cauchy–Green kernel is replaced by Bochner–Martinelli/Henkin kernels whose $L^\infty$ mapping properties fail; Fornæss–Sibony exhibit smooth pseudoconvex domains where $\bar\partial$ has no $L^p$ solution operator at all.
- **Carleson measures are not enough.** On $\mathbb{D}^n$ the natural "Carleson box" condition is not equivalent to the embedding $H^2(\mathbb{D}^n)\hookrightarrow L^2(\mu)$ (Carleson's own bidisc counterexample), so the dualization step collapses.
- **Failure of $H^1$–$BMO$ machinery.** Product $BMO$ (Chang–Fefferman) has a genuinely different structure — rectangle-based versus box-based — and the Littlewood–Paley identity used for the $\|b\|_\infty$ bound has no product analogue with the same constants.
- **Boundary geometry.** In $\mathbb{C}^n$ the Shilov boundary ($\mathbb{T}^n$) is strictly smaller than the topological boundary of $\mathbb{D}^n$; the zero sets $\{f_j = 0\}$ are analytic varieties of positive dimension, so stopping-time decompositions on "small" zero sets have no analogue.
- **Counterexamples nearby.** Cole's Riemann surface and Sibony's $\mathbb{C}^2$ domains show that any proof must use fine properties of $\mathbb{D}^n$ or $\mathbb{B}_n$ specifically, not soft function-algebra or pseudoconvexity arguments.
- **Operator corona is false.** Treil's counterexample for infinite-dimensional operator-valued $H^\infty$ blocks the tempting route of viewing $H^\infty(\mathbb{D}^2)$ as $H^\infty$ of the disc with values in $H^\infty(\mathbb{D})$.

## 6. The Gap

Section 4 gives corona in one complex dimension, in a broad class of plane domains, and for *multiplier algebras of specific Hilbert function spaces* on $\mathbb{B}_n$ — spaces with a complete Nevanlinna–Pick kernel, where the Toeplitz-corona theorem (a Hilbert-space, Schur-complement argument) is available. Section 1(C1) concerns $H^\infty(\mathbb{D}^n)$, whose multiplier structure is *not* complete Nevanlinna–Pick for $n \ge 2$. The precise missing step is:

> Given $f_1,\dots,f_m \in H^\infty(\mathbb{D}^2)$ with $\max_j |f_j| \ge \delta$, produce bounded solutions to $\bar\partial b_{jk} = \varphi_j\bar\partial\varphi_k - \varphi_k\bar\partial\varphi_j$ on the bidisc — i.e. an $L^\infty(\mathbb{T}^2)$ estimate for $\bar\partial$ against a *product* Carleson-type condition.

Equivalently: is the Toeplitz-corona (positivity of the operator matrix $[\,(\sum_j M_{f_j}M_{f_j}^* - \delta^2 I)\,]$) sufficient in the bidisc? In one variable, Toeplitz-corona $\Rightarrow$ corona via Tolokonnikov's lemma; in the bidisc no such implication is known, and the failure of von Neumann's inequality for three commuting contractions is the model obstruction.

## 7. Current Research (as of June 2026)

- **Function-space corona on the ball.** Extensions of Costea–Sawyer–Wick to $B_2^\sigma(\mathbb{B}_n)$ for $\sigma > 1/2$ and to weighted Besov–Sobolev multipliers (Wick and collaborators, Washington University in St. Louis; Sawyer, McMaster). *(frontier — verify)*
- **Product harmonic analysis.** Attempts to substitute Chang–Fefferman product $BMO$, Journé's lemma and multiparameter stopping-time (Bellman-function) methods for the classical Carleson decomposition (Treil, Volberg, Pott, Petermichl). Bellman-function techniques have produced sharp one-parameter constants but stall in two parameters.
- **Sharp constants.** Narrowing the $\delta^{-2}$ vs $\delta^{-2}\log(1/\delta)$ gap in $\mathbb{D}$, including the $n$-independent case and $H^p$ analogues.
- **Operator theory route.** Corona for $H^\infty$ of the symmetrized bidisc, tetrablock, and other inhomogeneous domains where a Nevanlinna–Pick-like realization theory exists.
- **Cole-type constructions.** Search for a corona *counterexample* on $\mathbb{D}^2$ by transplanting Cole's Riemann-surface fibration; no candidate has survived. *(frontier — verify)*
- **Plane domains.** Corona for domains whose complement satisfies capacity-density conditions; Garnett–Jones-style analysis extended beyond Denjoy sets.

## 8. Future Work

- Prove or refute an $L^\infty$ $\bar\partial$-estimate on $\mathbb{D}^2$ with product-Carleson data — the single decisive technical target.
- Determine whether corona for $H^\infty(\mathbb{B}_n)$ is strictly weaker than for $H^\infty(\mathbb{D}^n)$; the ball has a homogeneous boundary and an $\mathcal{M}$-invariant Green's operator, which may make it the easier case.
- Settle the *ideal problem* in the bidisc: is $h^3 \in (f_1,\dots,f_n)$ whenever $|h| \lesssim (\sum|f_j|^2)^{1/2}$?
- Resolve the sharp constant in $\mathbb{D}$: is the true growth $\delta^{-2}$, $\delta^{-2}\log(1/\delta)$, or something between?
- Characterize which plane domains admit corona, in terms of harmonic measure or Green's function separation — a conjectured "Widom-type" criterion.
- Clarify why the Drury–Arveson proof (Hilbert-space, complete NP kernel) cannot be upgraded to $H^\infty$: identify the exact algebraic obstruction.

## 9. Key References

- **[Foundational]** L. Carleson. *Interpolations by bounded analytic functions and the corona problem.* Annals of Mathematics **76** (1962), 547–559. [DOI](https://doi.org/10.2307/1970375)
- **[Foundational]** L. Hörmander. *Generators for some rings of analytic functions.* Bulletin of the AMS **73** (1967), 943–949. [DOI](https://doi.org/10.1090/s0002-9904-1967-11860-3)
- **[Book / Standard reference]** J. B. Garnett. *Bounded Analytic Functions.* Revised 1st ed., Graduate Texts in Mathematics 236, Springer, 2007 (orig. Academic Press, 1981). — Wolff's proof, Chapter VIII. [DOI](https://doi.org/10.1007/0-387-49763-3)
- **[Book]** T. W. Gamelin. *Uniform Algebras.* Prentice-Hall, 1969 (reprinted AMS Chelsea). — Cole's counterexample, maximal ideal space theory.
- **[SOTA / Planar]** J. B. Garnett and P. W. Jones. *The corona theorem for Denjoy domains.* Acta Mathematica **155** (1985), 27–40. [DOI](https://doi.org/10.1007/bf02392536)
- **[Counterexample]** N. Sibony. *Problème de la couronne pour des domaines pseudoconvexes à bord lisse.* Annals of Mathematics **126** (1987), 675–682.
- **[Counterexample]** J. E. Fornæss and N. Sibony. *Smooth pseudoconvex domains in $\mathbb{C}^2$ for which the corona theorem and $L^p$ estimates for $\bar\partial$ fail.* In *Complex Analysis and Geometry*, Plenum Press, 1993.
- **[SOTA / Several variables]** Ş. Costea, E. T. Sawyer and B. D. Wick. *The corona theorem for the Drury–Arveson Hardy space and other holomorphic Besov–Sobolev spaces on the unit ball in $\mathbb{C}^n$.* Analysis & PDE **4** (2011), 499–550. [DOI](https://doi.org/10.2140/apde.2011.4.499)
- **[Constants / Ideals]** S. Treil. *Estimates in the corona theorem and ideals of $H^\infty$: a problem of T. Wolff.* Journal d'Analyse Mathématique **87** (2002), 481–495.
- **[Operator corona]** S. Treil. *Angles between co-invariant subspaces, and the operator corona problem. The Szőkefalvi-Nagy problem.* Soviet Math. Doklady **38** (1989).
- **[Survey]** R. G. Douglas, S. G. Krantz, E. T. Sawyer, S. Treil, B. D. Wick (eds.). *The Corona Problem: Connections Between Operator Theory, Function Theory, and Geometry.* Fields Institute Communications 72, Springer, 2014.

## 10. Worked Example / Concrete Special Case

**Two generators on $\mathbb{D}$ with an explicit Bézout pair.** Take

$$f_1(z) = z^2, \qquad f_2(z) = (1-z)^2 .$$

*Hypothesis check.* On $\overline{\mathbb{D}}$, $|z| + |1-z| \ge |z + (1-z)| = 1$, so $\max(|z|,|1-z|) \ge 1/2$ and therefore

$$\max_j |f_j(z)| \;\ge\; \tfrac14 \quad\Longrightarrow\quad \delta \ge \tfrac14 .$$

(At $z = 1/2$ both equal $1/4$, so $\delta = 1/4$ exactly.) Normalize: $\|f_1\|_\infty = 1$, $\|f_2\|_\infty = 4$, so rescale $\tilde f_2 = f_2/4$ if a unit ball hypothesis is wanted.

*Solving the Bézout equation.* Expand the identity $1 = \big(z + (1-z)\big)^3$:

$$1 = z^3 + 3z^2(1-z) + 3z(1-z)^2 + (1-z)^3 = z^2\big(z + 3(1-z)\big) + (1-z)^2\big(3z + (1-z)\big).$$

Hence
$$g_1(z) = 3 - 2z, \qquad g_2(z) = 1 + 2z, \qquad f_1 g_1 + f_2 g_2 \equiv 1 .$$

*Norm comparison.* $\|g_1\|_\infty = 5$, $\|g_2\|_\infty = 3$. Carleson's bound for $n=2$ predicts a solution of size $\lesssim \delta^{-2}\log(1/\delta) = 16\log 4 \approx 22$, so the explicit polynomial solution sits comfortably inside the theoretical envelope — but only because both generators are polynomials with a common algebraic identity.

*Why this is the easy case.* The Bézout pair here comes from the polynomial ring $\mathbb{C}[z]$, where $\gcd(z^2,(1-z)^2)=1$ makes the identity purely algebraic. Carleson's theorem asserts the same conclusion when $f_1,f_2$ are, say, two Blaschke products with interlacing zeros — there $\{f_1 = 0\}$ and $\{f_2 = 0\}$ accumulate on all of $\mathbb{T}$, no algebraic identity exists, and one must run the $\bar\partial$ construction of §2: set $\Phi = |f_1|^2+|f_2|^2 \ge \delta^2$, $\varphi_j = \bar f_j/\Phi$, solve $\bar\partial b_{12} = \varphi_1\bar\partial\varphi_2 - \varphi_2\bar\partial\varphi_1$ with $\|b_{12}\|_\infty \lesssim \delta^{-2}\log(1/\delta)$ using Wolff's lemma, and put $g_1 = \varphi_1 + b_{12}f_2$, $g_2 = \varphi_2 - b_{12}f_1$.

*The bidisc failure point.* Repeat with $f_1(z,w) = z^2$, $f_2(z,w) = (1-z)^2$ on $\mathbb{D}^2$: the same $g_j$ work, since nothing depends on $w$. But for genuinely two-variable data — e.g. $f_1 = z - w$, $f_2$ a function vanishing on a curve transverse to $\{z=w\}$ — the zero sets are one-dimensional analytic varieties and the corresponding $\bar\partial$ system is over-determined ($\bar\partial b = \omega$ with $\bar\partial \omega = 0$ a compatibility condition in two variables). No $L^\infty$ solution operator is known for that system on $\mathbb{D}^2$. That is exactly the gap of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*