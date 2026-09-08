---
id: 05-analysis/analytic-capacity-comparability
title: "Analytic Capacity and the Cauchy Transform Semiadditivity Constants"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Analytic Capacity and the Cauchy Transform Semiadditivity Constants

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/analytic-capacity-comparability` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Analytic capacity $\gamma$ measures the obstruction a compact set $E \subset \mathbb{C}$ poses to bounded analytic continuation. Tolsa (2003) proved that $\gamma$ is **countably semiadditive**: there is an absolute constant $C$ with

$$\gamma\Big(\bigcup_{i=1}^{\infty} E_i\Big) \le C \sum_{i=1}^{\infty} \gamma(E_i),$$

and that $\gamma$ is comparable to the positive-measure capacity $\gamma_+$: $\gamma_+(E) \le \gamma(E) \le C\,\gamma_+(E)$.

What remains open is **quantitative**:

1. **(Sharp semiadditivity)** What is the least constant $C_{\mathrm{sa}}$ in the inequality above? Is $C_{\mathrm{sa}} = 1$, i.e. is $\gamma$ genuinely countably subadditive?
2. **(Comparability constant)** What is the least $C_+$ with $\gamma(E) \le C_+\,\gamma_+(E)$ for all compact $E$? Is $\gamma = \gamma_+$?
3. **(Cauchy transform constants)** The proofs route through $L^2$ bounds for the Cauchy transform and Menger curvature. What are the sharp constants in the curvature–capacity inequalities that transfer between the two?

A complete solution means either an explicit value (with matching examples) or a proof that no constant smaller than the trivial one works. Even the *existence* of an explicit numerical bound for $C_{\mathrm{sa}}$ or $C_+$ — extractable from a proof rather than from a compactness/non-quantitative $T(b)$ argument — is unresolved.

## 2. Mathematical Foundations

For compact $E \subset \mathbb{C}$, let $\Omega = \hat{\mathbb{C}} \setminus E$ and

$$\gamma(E) = \sup\big\{ |f'(\infty)| : f \in H^\infty(\Omega),\ \|f\|_\infty \le 1,\ f(\infty) = 0 \big\}, \qquad f'(\infty) := \lim_{z\to\infty} z f(z).$$

Every such $f$ has a distributional representation $f = \frac{1}{\pi} \mathcal{C}T$ for a distribution $T$ supported on $E$; restricting $T$ to be a **positive** Radon measure gives

$$\gamma_+(E) = \sup\big\{ \mu(E) : \operatorname{supp}\mu \subset E,\ \|\mathcal{C}\mu\|_{L^\infty(\mathbb{C}\setminus E)} \le 1 \big\}, \qquad \mathcal{C}\mu(z) = \int \frac{d\mu(\xi)}{\xi - z}.$$

Trivially $\gamma_+ \le \gamma$. Basic normalizations: $\gamma(\overline{D(z_0,r)}) = r$, and $\gamma(E) \le \operatorname{diam}(E)$ up to a constant; $\gamma$ is not a Choquet capacity in the classical sense and is not known to be additive on disjoint sets.

**Menger curvature.** For $x,y,z \in \mathbb{C}$ distinct, $c(x,y,z) = 1/R(x,y,z)$ where $R$ is the circumradius. For a Radon measure $\mu$,

$$c^2(\mu) = \iiint c(x,y,z)^2 \, d\mu(x)\,d\mu(y)\,d\mu(z).$$

Melnikov's identity links this to the Cauchy kernel: for $\mu$ with linear growth,

$$\|\mathcal{C}_\varepsilon \mu\|_{L^2(\mu)}^2 = \tfrac{1}{6}\,c_\varepsilon^2(\mu) + O(\mu(\mathbb{C})),$$

which is the algebraic engine of the whole theory. Melnikov's lower bound then gives, for $\mu$ with $\mu(D(x,r)) \le r$,

$$\gamma_+(\operatorname{supp}\mu) \;\gtrsim\; \frac{\mu(\mathbb{C})^{3/2}}{\big(\mu(\mathbb{C}) + c^2(\mu)\big)^{1/2}}.$$

**Linear growth / non-doubling CZ theory.** $\mathcal{C}$ is bounded on $L^2(\mu)$ for $\mu$ with $\mu(D(x,r)) \le Cr$ iff $\mu$ has finite local curvature on suitable pieces ($T(b)$ theorem for non-doubling measures, Nazarov–Treil–Volberg). Tolsa's comparability theorem states

$$\gamma(E) \asymp \gamma_+(E) \asymp \sup\{\mu(E) : \mu(D(x,r)) \le r,\ c^2(\mu) \le \mu(E)\},$$

a purely metric/geometric quantity — hence semiadditivity, since the right-hand side is manifestly semiadditive.

## 3. History & State of the Art (SOTA)

- **1888–1909.** Painlevé asks which compact sets are removable for bounded analytic functions; Ahlfors (1947) reformulates removability as $\gamma(E)=0$.
- **1967.** Vitushkin's survey poses semiadditivity of $\gamma$ as the central structural problem, driven by rational approximation theory (his localization operator needs it).
- **1977.** Garnett's *Analytic Capacity and Measure* codifies the classical theory; Davie and Øksendal (1982) develop the dual/positive-measure side, giving the first serious control of $\gamma$ by capacities defined through positive measures.
- **1995.** Melnikov discovers the curvature identity; Melnikov–Verdera give a curvature proof of $L^2$-boundedness of $\mathcal{C}$ on Lipschitz graphs.
- **1996.** Mattila–Melnikov–Verdera prove Vitushkin's conjecture for sets of finite length that are *Ahlfors–David regular*.
- **1998.** G. David removes regularity: unrectifiable 1-sets of finite length have zero analytic capacity (Vitushkin's conjecture in the $\mathcal{H}^1$-finite case).
- **2003.** Tolsa, *Acta Mathematica*: $\gamma \asymp \gamma_+$, countable semiadditivity, and the curvature characterization of Painlevé's problem.
- **2005.** Tolsa, *Annals*: $\gamma$ and $\gamma_+$ are invariant (up to constants) under bilipschitz maps.
- **2003–present.** Quantitative refinements: Mateu–Tolsa–Verdera compute $\gamma$ for Cantor sets; Jaye–Nazarov–Tolsa–Volberg extend to Riesz transforms of codimension $<1$; Dąbrowski and collaborators study capacities with big projections.

Every known proof of $\gamma \le C\gamma_+$ passes through a non-homogeneous $T(b)$ theorem plus a corona/stopping-time induction. The constants are absolute but never tracked; no published value exists.

## 4. Partial Results / Verified Cases

- **Continua.** For $E_1,E_2$ continua, subadditivity holds with constant $1$: $\gamma(E_1\cup E_2) \le \gamma(E_1)+\gamma(E_2)$ (Suita). For a connected compact $E$, $\gamma(E) = \gamma_+(E)$ (both equal the capacity of the outer boundary; $\gamma(E) \ge \tfrac14\operatorname{diam}E$).
- **Sets on a line or a Lipschitz graph.** If $E \subset \Gamma$ with $\Gamma$ a Lipschitz graph of constant $L$, then $\gamma(E) \asymp_L \mathcal{H}^1(E)$ and $\gamma = \gamma_+$ up to constants depending only on $L$; semiadditivity is elementary from measure additivity.
- **Finite $\mathcal{H}^1$ measure.** For $\mathcal{H}^1(E) < \infty$, $\gamma(E)>0$ iff $E$ is non-purely-unrectifiable (David 1998), and $\gamma(E) \asymp \gamma_+(E)$ follows; semiadditivity is inherited from $\mathcal{H}^1$-additivity on the rectifiable part.
- **Self-similar Cantor sets.** For the $1/4$-corner Cantor set truncated at generation $n$, $\gamma(E_n) \asymp n^{-1/2}$ (Mateu–Tolsa–Verdera 2003), matching $\gamma_+(E_n)$ with explicit two-sided constants — a case where the comparability constant is effectively computable.
- **Dimension $>1$.** If $\dim_H E > 1$ then $\gamma(E) > 0$ (classical, via Frostman + curvature or Sobolev methods).
- **General compact sets.** $\gamma \asymp \gamma_+$ and countable semiadditivity hold (Tolsa 2003) — but with unspecified absolute constants.

## 5. Principal Obstacles

- **Non-linearity of $\gamma$.** The extremal Ahlfors function of $E_1 \cup E_2$ is not built from those of $E_1$ and $E_2$; there is no superposition principle, so subadditivity cannot be tested directly.
- **Sign-changing distributions.** $\gamma$ admits complex distributions $T$ with no positivity; $\gamma_+$ does not. Converting one to the other requires solving a $\bar\partial$-problem with $L^\infty$ control, and the only known route is the Tolsa induction on scales — which loses a constant at every stopping-time layer.
- **Non-doubling Calderón–Zygmund theory.** The $T(b)$ theorems used (Nazarov–Treil–Volberg) yield constants through good-$\lambda$ inequalities, random dyadic lattices, and Cotlar-type arguments, each multiplicative and none sharp. A tracked constant would be astronomically far from $1$.
- **Curvature is only an $L^2$ proxy.** The identity $\|\mathcal{C}_\varepsilon\mu\|^2_{L^2(\mu)} = \tfrac16 c^2_\varepsilon(\mu) + O(\mu)$ is exact in $L^2(\mu)$ but $\gamma$ is an $L^\infty$ quantity off $E$; the passage $L^2 \to L^\infty$ costs a further uncontrolled factor.
- **No sharp examples.** There is no known family of pairs $E_1,E_2$ forcing $\gamma(E_1\cup E_2) > \gamma(E_1)+\gamma(E_2)$, so even the *sign* of the answer to "is $C_{\mathrm{sa}}=1$?" is unsettled. Classical failures of additivity (Murai-type constructions) show $\gamma$ is far from additive but do not violate subadditivity.
- **Higher-dimensional analogue is worse.** For Riesz transforms of codimension $\neq 1$ the curvature identity fails outright (no positive symmetrization), removing the only quantitative tool.

## 6. The Gap

Proved: $\gamma_+ \le \gamma \le C\gamma_+$ and $\gamma(\bigcup E_i) \le C\sum \gamma(E_i)$, with $C$ absolute, finite, and unquantified. Sought: the sharp $C_+$ and $C_{\mathrm{sa}}$, or a proof that both equal $1$.

The precise barrier is the **direction $\gamma \le C\gamma_+$**. Given an Ahlfors function $f$ for $E$ with $|f|\le 1$, one must produce a *positive* measure $\mu$ on $E$ with $\|\mathcal{C}\mu\|_\infty \lesssim 1$ and $\mu(E) \gtrsim |f'(\infty)|$. Tolsa's construction does this by decomposing $E$ into pieces where $\mathcal{C}$ is bounded, then summing — a lossy procedure. Closing the gap requires either (i) a *variational* argument constructing $\mu$ directly from $f$ (e.g. from $|f'|$ or the Garabedian dual function) with no stopping time, or (ii) a counterexample: a compact set with $\gamma(E)/\gamma_+(E) > 1$, or a pair with $\gamma(E_1\cup E_2)/(\gamma(E_1)+\gamma(E_2)) > 1$.

## 7. Current Research (as of June 2026)

- **Barcelona (UAB/CRM): Tolsa, Dąbrowski, and collaborators.** Quantitative rectifiability, capacities defined by big projections, and Wolff-type energies as substitutes for curvature. Recent work characterizes when capacities associated with the Riesz kernel are semiadditive.
- **Michigan State / Kent State: Volberg, Jaye, Nazarov.** Riesz transforms of codimension $<1$ and Wolff energy (Memoirs AMS, 2020); the goal is a curvature-free proof of comparability, which would in principle be quantifiable. *(frontier — verify)*
- **Constant-tracking programs.** Attempts to run explicit constants through the non-homogeneous $T(b)$ machinery (random lattices, corona decompositions) to produce a first numerical bound for $C_+$. No published value as of mid-2026. *(frontier — verify)*
- **Cantor-set asymptotics.** Refinements of the $n^{-1/2}$ law to non-self-similar and random Cantor sets, aiming to produce candidate extremizers for $C_{\mathrm{sa}}$. *(frontier — verify)*
- **Free-boundary / David–Semmes.** Connections to the David–Semmes problem for Riesz transforms; a positive resolution there would give new quantitative handles on capacities.

## 8. Future Work

1. **Extract any explicit constant.** Even $C_+ \le 10^{10^6}$ would be a milestone: it would convert a soft theorem into an effective one and permit numerical testing on Cantor-type sets.
2. **Variational construction of $\mu$.** Study $\mu = \frac{1}{2\pi}\Delta u$ for suitable subharmonic $u$ built from the Ahlfors function, aiming at $\|\mathcal{C}\mu\|_\infty \le C$ with $C$ computable.
3. **Curvature-free comparability.** Replace $c^2(\mu)$ by Wolff energies or by symmetrization inequalities that survive in codimension $\neq 1$; the same argument would give constants in $\mathbb{R}^d$.
4. **Search for a subadditivity counterexample.** Numerical optimization of $\gamma$ over unions of small Cantor pieces, using the known $n^{-1/2}$ law to design near-extremal configurations.
5. **Sharp constants in restricted classes.** Establish $C_{\mathrm{sa}}=1$ for finite unions of disks, for sets on a line, or for sets of finite $\mathcal{H}^1$ measure with explicit constants.

## 9. Key References

- **[Foundational]** L. V. Ahlfors. *Bounded analytic functions.* Duke Mathematical Journal 14 (1947), 1–11.
- **[Foundational]** J. Garnett. *Analytic Capacity and Measure.* Lecture Notes in Mathematics 297, Springer, 1972.
- **[Foundational]** A. M. Davie, B. Øksendal. *Analytic capacity and differentiability properties of finely harmonic functions.* Acta Mathematica 149 (1982), 127–152.
- **[Foundational]** M. S. Melnikov. *Analytic capacity: a discrete approach and the curvature of measure.* Sbornik: Mathematics 186 (1995), 827–846.
- **[Foundational]** M. S. Melnikov, J. Verdera. *A geometric proof of the $L^2$ boundedness of the Cauchy integral on Lipschitz graphs.* International Mathematics Research Notices 1995, no. 7, 325–331.
- **[Foundational]** P. Mattila, M. S. Melnikov, J. Verdera. *The Cauchy integral, analytic capacity, and uniform rectifiability.* Annals of Mathematics 144 (1996), 127–136.
- **[Foundational]** G. David. *Unrectifiable 1-sets have vanishing analytic capacity.* Revista Matemática Iberoamericana 14 (1998), 369–479.
- **[SOTA]** X. Tolsa. *Painlevé's problem and the semiadditivity of analytic capacity.* Acta Mathematica 190 (2003), 105–149.
- **[SOTA]** X. Tolsa. *Bilipschitz maps, analytic capacity, and the Cauchy integral.* Annals of Mathematics 162 (2005), 1243–1304.
- **[SOTA]** J. Mateu, X. Tolsa, J. Verdera. *The planar Cantor sets of zero analytic capacity and the local $T(b)$-theorem.* Journal of the American Mathematical Society 16 (2003), 19–28.
- **[SOTA]** F. Nazarov, S. Treil, A. Volberg. *The $Tb$-theorem on non-homogeneous spaces.* Acta Mathematica 190 (2003), 151–239.
- **[SOTA]** B. Jaye, F. Nazarov, M. C. Reguera, X. Tolsa. *The Riesz transform of codimension smaller than one and the Wolff energy.* Memoirs of the American Mathematical Society 266 (2020), no. 1293.
- **[Survey]** X. Tolsa. *Analytic capacity, the Cauchy transform, and non-homogeneous Calderón–Zygmund theory.* Progress in Mathematics 307, Birkhäuser, 2014.
- **[Survey]** A. G. Vitushkin. *The analytic capacity of sets in problems of approximation theory.* Russian Mathematical Surveys 22 (1967), 139–200.
- **[Survey]** J. Verdera. *Removability, capacity and approximation.* In *Complex Potential Theory*, NATO ASI Series 439, Kluwer, 1994, 419–473.

## 10. Worked Example / Concrete Special Case

**The $1/4$-corner Cantor set.** Let $Q_0 = [0,1]^2$. At each step replace every square of side $\ell$ by the four corner squares of side $\ell/4$. After $n$ steps, $E_n$ is a union of $4^n$ squares $\{Q_j^n\}$ of side $4^{-n}$. Let $\mu_n$ be the probability measure giving each $Q_j^n$ mass $4^{-n}$.

*Linear growth.* For $4^{-(k+1)} \le r < 4^{-k}$, a disk $D(x,r)$ meets $O(1)$ squares of generation $k$, so $\mu_n(D(x,r)) \lesssim 4^{-k} \asymp r$. So $\mu_n$ has linear growth with an absolute constant.

*Curvature.* Fix $x$ and a scale $4^{-k}$. Triples $(x,y,z)$ with $y,z$ in distinct generation-$k$ children have circumradius $R \gtrsim 4^{-k}$, so $c(x,y,z)^2 \lesssim 16^{k}$; the mass of such pairs is $\asymp 16^{-k}$. Each scale therefore contributes $O(1)$ to the triple integral, and the $n$ scales sum to
$$c^2(\mu_n) \asymp n .$$
(The matching lower bound is the content of Mateu–Tolsa–Verdera: the corner geometry keeps a fixed proportion of triples genuinely non-collinear at every scale.)

*Capacity.* Melnikov's bound with $\mu_n(\mathbb{C}) = 1$ gives
$$\gamma_+(E_n) \;\gtrsim\; \frac{1}{(1 + Cn)^{1/2}} \;\asymp\; n^{-1/2},$$
and the reverse inequality $\gamma(E_n) \lesssim n^{-1/2}$ follows from the local $T(b)$ argument. Hence
$$\gamma(E_n) \asymp \gamma_+(E_n) \asymp n^{-1/2}, \qquad \gamma\Big(\bigcap_n E_n\Big) = 0,$$
recovering Garnett–Ivanov's theorem that the corner Cantor set is removable, with a rate.

*Where the open problem bites.* Write $E_n = \bigcup_{j=1}^{4} E_n^{(j)}$, the four generation-one pieces, each a scaled copy of $E_{n-1}$ with ratio $1/4$. Scaling gives $\gamma(E_n^{(j)}) = \tfrac14 \gamma(E_{n-1}) \asymp \tfrac14 (n-1)^{-1/2}$, so
$$\frac{\gamma(E_n)}{\sum_{j=1}^4 \gamma(E_n^{(j)})} \;\asymp\; \frac{n^{-1/2}}{(n-1)^{-1/2}} \;\to\; 1 .$$
The ratio tends to a constant of order $1$ but the two-sided constants hidden in $\asymp$ are not known well enough to decide whether the ratio ever exceeds $1$. This is exactly the quantitative gap: the asymptotics are sharp in order, and completely uninformative about the sharp constant.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*