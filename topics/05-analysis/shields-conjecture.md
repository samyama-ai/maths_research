---
id: 05-analysis/shields-conjecture
title: "Shields Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Shields Conjecture (Brown–Shields Conjecture on Cyclic Vectors in the Dirichlet Space)

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/shields-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathcal{D}$ be the classical Dirichlet space of holomorphic functions on the unit disc $\mathbb{D}$ with finite Dirichlet integral. A function $f \in \mathcal{D}$ is **cyclic** if the smallest closed subspace of $\mathcal{D}$ containing $f$ and invariant under multiplication by $z$ is all of $\mathcal{D}$; equivalently,
$$[f] \;:=\; \overline{\{\,pf : p \text{ a polynomial}\,\}}^{\;\mathcal{D}} \;=\; \mathcal{D}.$$

Brown and Shields (1984) proved two necessary conditions: a cyclic $f$ must be an **outer** function, and its boundary zero set
$$Z(f) \;=\; \Big\{ \zeta \in \mathbb{T} : \lim_{r \uparrow 1} f(r\zeta) = 0 \Big\}$$
must have **logarithmic capacity zero**. (Radial limits of Dirichlet functions exist quasi-everywhere, so $Z(f)$ is well defined up to a polar set.)

> **Conjecture (Brown–Shields, 1984).** These conditions are also sufficient: $f \in \mathcal{D}$ is cyclic **if and only if** $f$ is outer and $\operatorname{cap}\big(Z(f)\big) = 0$.

A complete proof requires showing $1 \in [f]$ for every outer $f \in \mathcal{D}$ with $\operatorname{cap}(Z(f))=0$. A disproof requires exhibiting a single outer $f \in \mathcal{D}$ with polar boundary zero set for which $\inf_p \|pf-1\|_{\mathcal{D}} > 0$.

## 2. Mathematical Foundations

**The space.** For $f(z)=\sum_{k\ge 0}\hat f(k) z^k$ holomorphic on $\mathbb{D}$, the Dirichlet integral is
$$D(f) \;=\; \frac{1}{\pi}\int_{\mathbb{D}} |f'(z)|^2\, dA(z) \;=\; \sum_{k\ge 1} k\,|\hat f(k)|^2 ,$$
the area of $f(\mathbb{D})$ counted with multiplicity. Then $\mathcal{D}=\{f : D(f)<\infty\}$, a Hilbert space with
$$\|f\|_{\mathcal{D}}^2 \;=\; \|f\|_{H^2}^2 + D(f) \;=\; \sum_{k\ge 0} (k+1)\,|\hat f(k)|^2 .$$
$\mathcal{D}$ is a reproducing kernel Hilbert space; the equivalent kernel $k_w(z)=\frac{1}{\bar w z}\log\frac{1}{1-\bar w z}$ makes $\mathcal{D}$ a complete Nevanlinna–Pick space (Agler; Shimorin).

**Dirichlet-type scale.** For $\alpha \in \mathbb{R}$, $\mathcal{D}_\alpha = \{f: \sum_k (k+1)^\alpha |\hat f(k)|^2 < \infty\}$, so $\mathcal{D}_0 = H^2$, $\mathcal{D}_{-1}$ is the Bergman space, $\mathcal{D}_1 = \mathcal{D}$.

**Outer functions.** $f \in H^2$ is outer if
$$f(z) \;=\; \lambda \exp\Big( \frac{1}{2\pi}\int_{\mathbb{T}} \frac{e^{i\theta}+z}{e^{i\theta}-z} \log|f(e^{i\theta})|\, d\theta \Big),\qquad |\lambda|=1 .$$
By Beurling's theorem, in $H^2$ cyclicity is *equivalent* to outerness; the Dirichlet problem is exactly the extra obstruction created by boundary zeros.

**Logarithmic capacity.** For compact $E \subset \mathbb{T}$,
$$\operatorname{cap}(E) = e^{-V(E)},\qquad V(E)=\inf_{\mu \in P(E)} \iint \log\frac{1}{|\zeta-\eta|}\, d\mu(\zeta)\,d\mu(\eta),$$
$P(E)$ the probability measures on $E$. $\operatorname{cap}(E)=0$ iff $E$ is polar. Countable compact sets are polar; Hausdorff dimension $0$ does not imply polarity, and polar sets may have positive Hausdorff dimension — capacity, not measure or dimension, is the right gauge. For $\mathcal{D}_\alpha$, $0<\alpha<1$, the correct gauge is the Riesz capacity $\operatorname{cap}_\alpha$ of the kernel $|\zeta-\eta|^{-(1-\alpha)}$.

**Local Dirichlet integral (Richter–Sundberg).** For $\zeta \in \mathbb{T}$,
$$D_\zeta(f) \;=\; \frac{1}{2\pi}\int_{\mathbb{T}} \frac{|f(e^{i\theta})-f(\zeta)|^2}{|e^{i\theta}-\zeta|^2}\, d\theta, \qquad D(f) = \frac{1}{2\pi}\int_{\mathbb{T}} D_\zeta(f)\, |d\zeta| ,$$
the main quantitative tool for localizing cyclicity arguments at a boundary zero.

**Capacitary strong-type inequality (Beurling).** If $f\in\mathcal{D}$ then $f$ has radial limits q.e., and
$$\operatorname{cap}\big\{\zeta \in \mathbb{T} : |f^*(\zeta)| \ge \lambda \big\} \;\le\; \exp\!\big(-c\lambda^2/\|f\|_{\mathcal{D}}^2\big),$$
which forces $\operatorname{cap}(Z(f))=0$ whenever $p_n f \to 1$ in $\mathcal{D}$ — this is the proof of necessity.

## 3. History & State of the Art (SOTA)

- **1940 / 1952.** Beurling's *Ensembles exceptionnels* introduces capacitary exceptional sets for Dirichlet functions; Carleson characterizes boundary zero sets of $\mathcal{D}$-functions.
- **1949.** Beurling settles the $H^2$ analogue: cyclic $\iff$ outer.
- **1984.** Leon Brown and Allen Shields, *Cyclic vectors in the Dirichlet space*, Trans. AMS 285. They prove necessity of (outer + polar zero set), prove sufficiency in several classes, and state the conjecture. This is the paper the "Shields conjecture" names.
- **1985.** Brown and Cohn show that for *every* compact polar $E\subset\mathbb{T}$ there exists a cyclic $f\in\mathcal{D}$ with $Z(f)=E$ — so no capacity-zero set is itself an obstruction. The conjecture cannot fail for "geometric" reasons alone; failure would have to come from the fine behaviour of $|f|$.
- **1991–92.** Richter's model theorem for cyclic analytic $2$-isometries and Richter–Sundberg's local Dirichlet integral formula give the structure theory of $z$-invariant subspaces of $\mathcal{D}$ (every such subspace is generated by its extremal function; index $1$).
- **2006–2009.** El-Fallah, Kellay and Ransford prove the sharpest general sufficient conditions, including a paper titled *On the Brown–Shields conjecture for cyclicity in the Dirichlet space* (Adv. Math., 2009), which verifies the conjecture under an extra regularity hypothesis on the modulus $|f|$ near $Z(f)$.
- **2014.** The monograph *A Primer on the Dirichlet Space* (El-Fallah–Kellay–Mashreghi–Ransford) devotes a chapter to the conjecture; it remains open.
- **2015–present.** Bénéteau–Khavinson–Liaw–Seco–Sola develop **optimal polynomial approximants**, turning cyclicity into a computable extremal problem and producing sharp decay rates in $\mathcal{D}_\alpha$.

## 4. Partial Results / Verified Cases

The conjecture is a theorem in each of the following cases.

1. **Bounded below.** If $\inf_{\mathbb{D}}|f| > 0$ (so $1/f\in H^\infty$ and $f$ has no boundary zeros), $f$ is cyclic (Brown–Shields).
2. **Polynomials and rational functions.** Every polynomial with no zeros in the open disc is cyclic, including $f(z)=(1-z)^n$; see §10.
3. **Continuous functions with countable zero set.** If $f \in \mathcal{D}\cap A(\mathbb{D})$ is outer and $Z(f)$ is countable (hence polar), $f$ is cyclic (Brown–Shields; Hedenmalm–Shields, 1990).
4. **$\alpha > 1$.** For $\mathcal{D}_\alpha$ with $\alpha>1$, $\mathcal{D}_\alpha$ is a Banach algebra contained in $A(\mathbb{D})$, $\operatorname{cap}_\alpha$-null sets are empty, and $f$ is cyclic iff $f$ has no zeros in $\overline{\mathbb{D}}$ — the analogue is trivially true.
5. **$\alpha \le 0$.** For $\mathcal{D}_\alpha$, $\alpha\le 0$ (Hardy and Bergman-type), cyclic $\iff$ outer (Beurling for $\alpha=0$; the capacity condition is vacuous).
6. **Prescribed zero sets.** For each compact polar $E\subset\mathbb{T}$ there is a cyclic $f\in\mathcal{D}$ with $Z(f)=E$ (Brown–Cohn, 1985).
7. **Regular moduli.** If $f\in\mathcal{D}$ is outer, $\operatorname{cap}(Z(f))=0$, and $|f|$ satisfies a quantitative decay/smoothness condition at $Z(f)$ (e.g. $\log(1/|f|)$ lies in a suitable Dirichlet-type class, or $Z(f)$ is a Carleson set with controlled distance function), then $f$ is cyclic (El-Fallah–Kellay–Ransford, 2006, 2009).
8. **Multiplier-invariant statements.** If $f$ is cyclic in $\mathcal{D}$ it is cyclic in every $\mathcal{D}_\alpha$, $\alpha<1$, by density of the embedding; the conjecture is therefore genuinely a statement about the top of the scale.

## 5. Principal Obstacles

- **No factorization theory.** $\mathcal{D}$ has no Beurling-type inner–outer factorization compatible with the norm: $f$ outer with $f\in\mathcal{D}$ does not imply the outer factors of $|f|^t$ lie in $\mathcal{D}$, and $g\in\mathcal{D}$, $|f|\le|g|$ does **not** imply $f\in\mathcal{D}$. Every $H^2$ proof of Beurling's theorem uses factorization at exactly the step that fails here.
- **The multiplier algebra is small.** $\mathcal{M}(\mathcal{D})=\{\varphi : \varphi\mathcal{D}\subseteq\mathcal{D}\} \subsetneq H^\infty\cap\mathcal{D}$, characterized by a Carleson-measure condition. So one cannot approximate $1/f$ by multipliers with norm control; the natural "divide by $f$" strategy has no bounded implementation.
- **Capacity is not subadditive-friendly.** Logarithmic capacity is non-additive and non-monotone under the natural operations (products, powers), so smallness of $Z(f)$ resists being propagated through the approximation $p_n f\to 1$.
- **Rate mismatch.** Necessity gives an exponential capacitary bound; sufficiency needs a quantitative construction of $p_n$ with $\|p_nf-1\|_{\mathcal{D}}\to0$. Known constructions lose a logarithmic factor exactly at the scale where $\operatorname{cap}=0$ but the "capacity profile" $\operatorname{cap}(Z(f)\cap I)$ decays arbitrarily slowly as $|I|\to0$. There is no uniform modulus.
- **The gauge does not see $|f|$.** Brown–Cohn shows the zero *set* is never the obstruction; any counterexample must come from the interaction between the outer function's rate of vanishing and the capacity of $Z(f)$, a two-parameter phenomenon that current one-parameter capacitary tools cannot separate.

## 6. The Gap

Proven: cyclicity for $f$ whose modulus vanishes at $Z(f)$ at a *controlled* rate (§4.7), plus all cases where the zero set is countable or empty. Conjectured: cyclicity with **no** hypothesis beyond $\operatorname{cap}(Z(f))=0$.

The precise missing step: given an outer $f\in\mathcal{D}$ with $\operatorname{cap}(Z(f))=0$, construct polynomials $p_n$ with
$$\|p_n f - 1\|_{\mathcal{D}}^2 \;=\; \|p_nf-1\|_{H^2}^2 + \frac{1}{2\pi}\int_{\mathbb{T}} D_\zeta(p_nf-1)\,|d\zeta| \;\longrightarrow\; 0 ,$$
uniformly over the family of admissible moduli. Equivalently: show the extremal quantity $\inf_{\deg p \le n}\|pf-1\|_{\mathcal{D}}$ tends to $0$ whenever the equilibrium potential of $Z(f)$ is identically $+\infty$. All known proofs require an a priori link between $\log(1/|f|)$ and the capacitary potential of $Z(f)$; the conjecture asserts none is needed.

## 7. Current Research (as of June 2026)

- **Optimal polynomial approximants.** The Bénéteau–Khavinson–Liaw–Seco–Sola programme computes $p_n^* = \arg\min_{\deg p\le n}\|pf-1\|_{\mathcal{D}_\alpha}$ via finite Gram systems, giving numerically exact decay rates and zero-location results for $p_n^*$ (zeros stay outside $\overline{\mathbb{D}}$ and accumulate on $Z(f)$). Extended to several variables (Dirichlet-type spaces on the bidisc), where even the necessary conditions are unsettled. *(frontier — verify)*
- **Capacitary/potential-theoretic school (Rabat–Bordeaux–Québec).** El-Fallah, Kellay, Ransford and collaborators continue to weaken the regularity hypothesis in §4.7, aiming at a modulus-free criterion.
- **Operator-model school.** Richter–Sundberg-style $2$-isometry models and complete Nevanlinna–Pick methods (Agler–McCarthy, Aleman, Shimorin, Hartz) are used to transfer cyclicity questions to column-extreme/Corona-type statements in $\mathcal{M}(\mathcal{D})$.
- **Weak-product and Corona techniques.** Arcozzi–Rochberg–Sawyer–Wick's Carleson-measure and weak-product theory for $\mathcal{D}$ provides duality tools not available in 1984; whether they can certify $1\in[f]$ is open. *(frontier — verify)*

## 8. Future Work

- Prove or refute an intermediate statement: is $[f]=[f^2]$ whenever $f, f^2 \in \mathcal{D}$? A positive answer would allow bootstrapping powers and reduce the conjecture to a "half-vanishing" case.
- Establish a **uniform capacitary approximation lemma**: for compact polar $E$, produce polynomials $q_n$ with $q_n \to 1$ off $E$, $q_n\to 0$ near $E$, and $\|q_n\|_{\mathcal{D}}\to0$ at a rate depending only on the equilibrium potential.
- Settle the multiplier case: is every outer $\varphi \in \mathcal{M}(\mathcal{D})$ with $\operatorname{cap}(Z(\varphi))=0$ cyclic? This is the conjecture's most tractable restriction.
- Search for a counterexample by adversarial construction: choose $E$ polar with slowly decaying capacity profile and an outer $f$ vanishing on $E$ as fast as membership in $\mathcal{D}$ allows, then bound $\inf_n\|p_n^*f-1\|$ below numerically via the Gram determinant.
- Resolve the $\mathcal{D}_\alpha$ analogue uniformly in $0<\alpha<1$; a proof whose constants degenerate as $\alpha\uparrow1$ would locate the true obstruction.

## 9. Key References

- **[Foundational]** L. Brown, A. L. Shields. *Cyclic vectors in the Dirichlet space.* Transactions of the American Mathematical Society **285** (1984), 269–304.
- **[Foundational]** A. Beurling. *Ensembles exceptionnels.* Acta Mathematica **72** (1940), 1–13.
- **[Foundational]** L. Carleson. *On the zeros of functions with bounded Dirichlet integrals.* Mathematische Zeitschrift **56** (1952), 289–295.
- **[Partial results]** L. Brown, W. Cohn. *Some examples of cyclic vectors in the Dirichlet space.* Proceedings of the American Mathematical Society **95** (1985), 42–46.
- **[Structure]** S. Richter, C. Sundberg. *A formula for the local Dirichlet integral.* Michigan Mathematical Journal **38** (1991), 355–379.
- **[Structure]** S. Richter, C. Sundberg. *Multipliers and invariant subspaces in the Dirichlet space.* Journal of Operator Theory **28** (1992), 167–186.
- **[Structure]** H. Hedenmalm, A. Shields. *Invariant subspaces in Banach spaces of analytic functions.* Michigan Mathematical Journal **37** (1990), 91–104.
- **[SOTA]** O. El-Fallah, K. Kellay, T. Ransford. *Cyclicity in the Dirichlet space.* Arkiv för Matematik **44** (2006), 61–86.
- **[SOTA]** O. El-Fallah, K. Kellay, T. Ransford. *On the Brown–Shields conjecture for cyclicity in the Dirichlet space.* Advances in Mathematics **222** (2009), 2196–2214.
- **[SOTA]** C. Bénéteau, A. Condori, C. Liaw, D. Seco, A. Sola. *Cyclicity in Dirichlet-type spaces and extremal polynomials.* Journal d'Analyse Mathématique **126** (2015), 259–286.
- **[Survey / Book]** O. El-Fallah, K. Kellay, J. Mashreghi, T. Ransford. *A Primer on the Dirichlet Space.* Cambridge Tracts in Mathematics 203, Cambridge University Press, 2014.
- **[Background]** J. Agler, J. E. McCarthy. *Pick Interpolation and Hilbert Function Spaces.* Graduate Studies in Mathematics 44, American Mathematical Society, 2002.

## 10. Worked Example / Concrete Special Case

**Claim.** $f(z)=1-z$ is cyclic in $\mathcal{D}$, in agreement with the conjecture: $f$ is outer and $Z(f)=\{1\}$, a single point, which is polar ($\operatorname{cap}\{1\}=0$).

**Construction.** For $n \ge 2$ set
$$p_n(z) \;=\; \sum_{k=0}^{n-1} a_k z^k, \qquad a_k \;=\; 1 - \frac{\log(k+1)}{\log n}.$$
Note $a_0 = 1$ and $a_{n-1} = 1-\frac{\log n}{\log n}=0$. Then
$$1 - (1-z)p_n(z) \;=\; (1-a_0) + \sum_{k=1}^{n-1} (a_{k-1}-a_k)\, z^k + a_{n-1} z^n \;=\; \sum_{k=1}^{n-1} c_k z^k,$$
with $c_0 = 0$, $c_n = 0$, and for $1\le k\le n-1$,
$$c_k \;=\; a_{k-1}-a_k \;=\; \frac{\log(k+1)-\log k}{\log n} \;=\; \frac{\log\!\big(1+\tfrac1k\big)}{\log n} \;\le\; \frac{1}{k\log n}.$$

**Norm estimate.** Using $\|g\|_{\mathcal{D}}^2 = \sum_{k\ge0}(k+1)|\hat g(k)|^2$ exactly,
$$\|1-(1-z)p_n\|_{\mathcal{D}}^2 \;=\; \sum_{k=1}^{n-1}(k+1)\,c_k^2 \;\le\; \frac{1}{\log^2 n}\sum_{k=1}^{n-1}\frac{k+1}{k^2} \;\le\; \frac{2}{\log^2 n}\sum_{k=1}^{n-1}\frac{1}{k} \;\le\; \frac{2(1+\log n)}{\log^2 n}.$$
Hence $\|1-(1-z)p_n\|_{\mathcal{D}} = O\big((\log n)^{-1/2}\big) \to 0$, so $1 \in [1-z]$. Since the polynomials are dense in $\mathcal{D}$ and $1$ generates them, $[1-z]=\mathcal{D}$: $f$ is cyclic. $\square$

**Reading the example.** Three points generalize.

- The decay is only $(\log n)^{-1/2}$ — *no* polynomial rate is available even for the simplest boundary zero. This logarithmic scale is exactly the scale of the logarithmic capacity kernel $\log\frac{1}{|\zeta-\eta|}$, which is why $\operatorname{cap}$, and not Lebesgue measure or Hausdorff dimension, is the correct gauge in §1.
- Multiplicativity gives more: since $\mathcal{M}(\mathcal{D})\supseteq$ polynomials and $[fg]\subseteq[f]$, the same argument applied repeatedly yields cyclicity of $(1-z)^m$ and of any polynomial with all zeros in $\mathbb{C}\setminus\mathbb{D}$.
- The construction used the *explicit* profile of $|f|$ near $\zeta=1$. For a general outer $f$ with $Z(f)$ an uncountable polar Cantor-type set, no such explicit profile exists, and manufacturing the analogue of $(a_k)$ from the equilibrium potential of $Z(f)$ alone is precisely the gap of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*