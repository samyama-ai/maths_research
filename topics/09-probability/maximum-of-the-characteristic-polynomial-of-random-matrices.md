---
id: 09-probability/maximum-of-the-characteristic-polynomial-of-random-matrices
title: "Maximum of the Characteristic Polynomial of Random Matrices"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Maximum of the Characteristic Polynomial of Random Matrices

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/maximum-of-the-characteristic-polynomial-of-random-matrices` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $U_N$ be Haar-distributed on the unitary group $\mathrm{U}(N)$ and let

$$P_N(\theta) = \det\!\left(I - e^{-i\theta}U_N\right), \qquad \theta\in[0,2\pi).$$

Set $\displaystyle \mathcal{X}_N = \max_{\theta\in[0,2\pi)} \log|P_N(\theta)|$.

**Fyodorov–Hiary–Keating conjecture (CUE case, 2012).**

$$\mathcal{X}_N = \log N - \tfrac{3}{4}\log\log N + \mathcal{M}_N,$$

where $\mathcal{M}_N$ converges in distribution to a randomly shifted Gumbel law: $\mathcal{M}_N \Rightarrow \mathcal{G} + \tfrac{1}{2}\log \mathcal{B}$, with $\mathcal{G}$ standard Gumbel (rate $2$ in the exponential tail, i.e. $\mathbb P(\mathcal G \le x) = e^{-Ce^{-2x}}$) independent of a "derivative-martingale" total mass $\mathcal{B}$ arising from critical Gaussian multiplicative chaos.

A complete resolution requires: (i) the two deterministic terms $\log N$ and $-\frac34\log\log N$; (ii) tightness of $\mathcal M_N$; (iii) identification of the limit law, including the conjectured explicit density. The conjecture is asserted more generally for the circular $\beta$-ensemble (C$\beta$E), where the centering becomes $\sqrt{2/\beta}\,(\log N - \frac{3}{4}\log\log N)$, and for Hermitian ensembles (GUE/G$\beta$E) and non-Hermitian ones (Ginibre), each with its own constants. Items (i) and (ii) are theorems; (iii) is open.

## 2. Mathematical Foundations

**Fourier expansion.** For $|z|<1$, $\log\det(I-zU) = -\sum_{k\ge1}\frac{z^k}{k}\operatorname{Tr}U^k$, so on the unit circle

$$\log|P_N(\theta)| \;=\; -\sum_{k\ge 1}\frac{1}{k}\,\Re\!\left(e^{-ik\theta}\operatorname{Tr}U_N^{k}\right).$$

**Diaconis–Shahshahani.** For fixed $k$, $\operatorname{Tr}U_N^k \Rightarrow \sqrt{k}\,\mathcal N^{\mathbb C}_k$ with $\mathcal N^{\mathbb C}_k$ standard complex Gaussians, independent across $k$, and all moments match exactly for $k\le N$. Hence $\log|P_N|$ is *almost* the Gaussian field with covariance

$$\mathbb E\big[\log|P_N(\theta)|\log|P_N(\theta')|\big] \approx \tfrac12\log\frac{1}{|e^{i\theta}-e^{i\theta'}|}\quad(|\theta-\theta'|\gg 1/N),\qquad \operatorname{Var}\log|P_N(\theta)| = \tfrac12\log N + O(1).$$

This is the defining property of a **log-correlated field**.

**Keating–Snaith moments.** Exactly, via Selberg's integral,

$$\mathbb E\,|P_N(\theta)|^{2s} = \prod_{j=1}^{N-1}\frac{\Gamma(j)\Gamma(j+2s)}{\Gamma(j+s)^2} \;\sim\; \frac{G(1+s)^2}{G(1+2s)}\,N^{s^2},\qquad \Re s > -\tfrac12,$$

with $G$ the Barnes $G$-function. Note $N^{s^2}$ — the signature of a $\frac12\log N$ Gaussian variance.

**Branching heuristic.** Write $n=\log N$ and split the Fourier sum into dyadic blocks $2^{j}\le k<2^{j+1}$. Block $j$ has variance $\approx \frac12\log 2$ and decorrelation scale $2^{-j}$, so the field behaves like a branching random walk (BRW) of $n$ generations, branching number $e$, step variance $\sigma^2=\frac12$. Bramson's formula for BRW/BBM,

$$m_n = \sqrt{2\sigma^2\log b}\;n \;-\; \frac{3}{2}\sqrt{\frac{\sigma^2}{2\log b}}\;\log n,$$

with $b=e$, $\sigma^2=\frac12$ gives $m_n = n - \frac34\log n$, i.e. $\log N - \frac34\log\log N$.

**GMC link.** For $\gamma<\sqrt2$, $|P_N(\theta)|^{\gamma}/\mathbb E|P_N|^{\gamma}\,d\theta$ converges to Gaussian multiplicative chaos of parameter $\gamma$ (Webb, $L^2$-phase $\gamma<1$; Nikula–Saksman–Webb, $L^1$-phase $\gamma<\sqrt2$). The random shift $\mathcal B$ is the critical ($\gamma=\sqrt2$) derivative martingale.

## 3. History & State of the Art (SOTA)

- **2000.** Keating–Snaith compute all moments of $|P_N|$ and use the CLT $\log|P_N|/\sqrt{\tfrac12\log N}\Rightarrow \mathcal N(0,1)$ as the random-matrix model for $\log|\zeta(\tfrac12+it)|$.
- **2012.** Fyodorov, Hiary and Keating (PRL 108, 170601) apply the freezing-transition heuristic from disordered landscapes / Derrida's REM to $\log|P_N|$, predict the three-term expansion, and transfer it to $\max_{|h|\le1}\log|\zeta(\tfrac12+it+ih)| = \log\log T - \frac34\log\log\log T + O(1)$. Fyodorov–Keating (2014) give the extended physics derivation, including the conjectured limiting density.
- **2017.** Arguin–Belius–Bourgade prove the leading order: $\mathcal X_N/\log N \to 1$ in probability.
- **2018.** Paquette–Zeitouni prove the second-order term for CUE: $(\mathcal X_N - \log N + \frac34\log\log N)/\log\log N \to 0$ in probability. Independently, Chhaibi–Madaule–Najnudel prove **tightness** of $\mathcal M_N$ for all C$\beta$E, $\beta>0$ — a stronger statement, achieved via a coupling of the CMN "$\beta$-circular" recursion with an exact hierarchical BRW.
- **2019–2021.** Extension beyond the circle: Lambert–Paquette (GUE/G$\beta$E, law of large numbers in the bulk), Lambert (Ginibre), Claeys–Fahs–Lambert–Webb (rigidity/moderate deviations for Hermitian ensembles).
- **2020–2023.** Arguin–Bourgade–Radziwiłł prove the FHK conjecture for $\zeta$ itself at the level of tightness (Parts I and II), unconditionally, so the number-theoretic analogue now matches the matrix one.
- **2022+.** Paquette–Zeitouni, *The extremal landscape for the C$\beta$E ensemble*, describe the full extremal point process and give convergence in law of the maximum, modulo identification of the limiting object. *(frontier — verify)*

## 4. Partial Results / Verified Cases

| Ensemble / regime | Result | Reference |
|---|---|---|
| CUE, leading order | $\mathcal X_N = (1+o(1))\log N$ in probability | Arguin–Belius–Bourgade 2017 |
| CUE, second order | $\mathcal X_N = \log N - \frac34\log\log N + o(\log\log N)$ | Paquette–Zeitouni 2018 |
| C$\beta$E, all $\beta>0$ | $\mathcal X_N - \sqrt{2/\beta}\big(\log N-\frac34\log\log N\big)$ is **tight** | Chhaibi–Madaule–Najnudel 2018 |
| GUE / G$\beta$E, bulk | $\max_{x\in(-2+\delta,2-\delta)}\log|\det(H_N-x)| = (1+o(1))\sqrt{\tfrac{2}{\beta}}\cdot\tfrac{\log N}{\sqrt2}\cdot\sqrt2$; LLN with the analogous constant | Lambert–Paquette 2019 |
| GUE, conjectural full law | Explicit conjectured law of $\max\log|\det(H_N-x)|$ over $[-1,1]$ | Fyodorov–Simm 2016 |
| Ginibre (non-Hermitian) | $\max_{|z|\le1}\log|\det(G_N-z)| = \sqrt{\tfrac{N}{2}}\,\gamma_N + O(1)$-type two-term expansion with $\log$-correlated correction | Lambert 2020 |
| $\gamma$-moments / GMC | Convergence of $|P_N|^\gamma$ to GMC for $0\le\gamma<\sqrt2$ | Webb 2015; Nikula–Saksman–Webb 2020 |
| Riemann zeta analogue | $\max_{|h|\le1}\log|\zeta(\tfrac12+it+ih)| - \log\log T + \frac34\log\log\log T$ tight | Arguin–Bourgade–Radziwiłł 2020, 2023 |
| $\beta\to\infty$, $N$ small | Exact laws computable; $N=1,2$ done in closed form (§10) | — |

Not proven for any ensemble: convergence in distribution of $\mathcal M_N$ to the randomly-shifted Gumbel with the FHK density.

## 5. Principal Obstacles

- **The field is not Gaussian.** Gaussian comparison (Slepian, Sudakov–Fernique, Kahane) gives leading order but is too lossy at the $\log\log N$ scale, because the sub-Gaussian corrections to $\operatorname{Tr}U^k$ for $k$ comparable to $N$ enter exactly at $O(1)$.
- **The correlation structure is only approximately hierarchical.** BRW technology (Bramson's tail estimates, Aïdékon's derivative-martingale identification, the Bramson–Ding–Zeitouni criterion) requires either exact branching or a precise multiscale decomposition with controlled error. On the circle the "tree" is only approximate; block errors accumulate to $O(\log\log N)$ unless coupled very carefully — Chhaibi–Madaule–Najnudel escape this only by using the exact Killip–Nenciu Verblunsky-coefficient recursion, which has no Hermitian analogue.
- **Small-scale ($|\theta-\theta'|\lesssim 1/N$) behaviour.** Below the eigenvalue spacing the field is smooth, not log-correlated; the crossover contributes an $O(1)$ term that no soft argument controls.
- **Critical GMC.** The shift $\mathcal B$ lives at $\gamma=\sqrt2$, the critical point, where the standard chaos construction degenerates and one needs derivative-martingale convergence — established for exactly scale-invariant fields, not yet for $\log|P_N|$.
- **Freezing is a physics input.** The conjectured density follows from the assumption that the free energy $\frac1\beta\log\int e^{\beta\log|P_N|}$ freezes above $\beta_c=\sqrt2$ and from an analytic continuation of the Fisher–Hartwig / Selberg moment formula to complex $s$ — a step with no rigorous justification.

## 6. The Gap

Proven: two deterministic terms plus tightness of the remainder (C$\beta$E). Conjectured: the remainder has a limit, and that limit is $\mathcal G + \frac12\log\mathcal B$.

The exact missing step is a **derivative-martingale convergence theorem for the non-Gaussian, non-hierarchical field $\log|P_N|$**, together with an $O(1)$-precise decoupling of the near-diagonal ($|\theta-\theta'|\le N^{-1+\varepsilon}$) contribution. Equivalently: prove
$$\lim_{N\to\infty}\mathbb P\big(\mathcal X_N \le \log N-\tfrac34\log\log N + x\big)=\mathbb E\big[e^{-C\mathcal B e^{-2x}}\big]$$
for some constant $C>0$, and identify $C$ and the law of $\mathcal B$.

## 7. Current Research (as of June 2026)

- **NYU / Courant (Bourgade and collaborators).** Dynamical and Dyson-Brownian-motion routes to the extremal process; Bourgade–Falconet connect eigenvalue dynamics to Liouville quantum gravity, which would supply the missing GMC object. *(frontier — verify)*
- **Ohio State / Weizmann (Paquette, Zeitouni).** *The extremal landscape for the C$\beta$E ensemble* aims at the full decorated point process, the strongest program towards item (iii). *(frontier — verify)*
- **KTH / Copenhagen (Lambert, Claeys, Webb, Fahs).** Riemann–Hilbert and Fisher–Hartwig asymptotics with merging singularities, giving uniform moment control needed for the $O(1)$ term; extension to Hermitian and non-Hermitian ensembles.
- **Nottingham / Bristol (Fyodorov, Keating, Simm).** Refined freezing predictions, edge and multifractal spectra, and the GUE/G$\beta$E constants.
- **Number theory side (Arguin, Radziwiłł, Soundararajan, Harper).** Transfer of the ABR method for $\zeta$ back to matrices; Harper's low-moment/better-than-square-root cancellation machinery.
- **Augeri–Butez–Zeitouni** CLT for characteristic polynomials of random Jacobi matrices supplies tridiagonal recursions that may replay the CMN argument in the Hermitian setting. *(frontier — verify)*

## 8. Future Work

1. Prove tightness for GUE/G$\beta$E in the bulk using the Dumitriu–Edelman tridiagonal model as the Hermitian substitute for Verblunsky coefficients.
2. Establish convergence of the critical derivative martingale for $\log|P_N|$; this alone yields the randomly-shifted-Gumbel form.
3. Rigorously justify freezing: show that the analytic continuation of $\mathbb E|P_N|^{2s}$ to $\Re s>\sqrt{2}/2$ controls the free energy, closing the physics gap.
4. Compute the constant $C$ and test the conjectured density against high-precision simulation at $N=2^{20}$ and beyond — current numerics are consistent but the $\log\log N$ convergence rate makes them weak evidence.
5. Extend to the edge (Airy regime) and to non-Hermitian ensembles beyond Ginibre.

## 9. Key References

- **[Foundational]** J. P. Keating, N. C. Snaith. *Random matrix theory and $\zeta(1/2+it)$.* Communications in Mathematical Physics 214 (2000), 57–89.
- **[Foundational]** Y. V. Fyodorov, G. A. Hiary, J. P. Keating. *Freezing Transition, Characteristic Polynomials of Random Matrices, and the Riemann Zeta Function.* Physical Review Letters 108 (2012), 170601.
- **[Foundational]** Y. V. Fyodorov, J. P. Keating. *Freezing transitions and extreme values: random matrix theory, and disordered landscapes.* Philosophical Transactions of the Royal Society A 372 (2014), 20120503.
- **[Foundational]** M. Bramson. *Maximal displacement of branching Brownian motion.* Communications on Pure and Applied Mathematics 31 (1978), 531–581.
- **[SOTA]** L.-P. Arguin, D. Belius, P. Bourgade. *Maximum of the characteristic polynomial of random unitary matrices.* Communications in Mathematical Physics 349 (2017), 703–751.
- **[SOTA]** E. Paquette, O. Zeitouni. *The maximum of the CUE field.* International Mathematics Research Notices 2018 (16), 5028–5119.
- **[SOTA]** R. Chhaibi, T. Madaule, J. Najnudel. *On the maximum of the C$\beta$E field.* Duke Mathematical Journal 167 (2018), 2243–2345.
- **[SOTA]** G. Lambert, E. Paquette. *The law of large numbers for the maximum of almost Gaussian log-correlated fields coming from random matrices.* Probability Theory and Related Fields 173 (2019), 157–209.
- **[SOTA]** G. Lambert. *Maximum of the characteristic polynomial of the Ginibre ensemble.* Communications in Mathematical Physics 378 (2020), 943–985.
- **[SOTA]** T. Claeys, B. Fahs, G. Lambert, C. Webb. *How much can the eigenvalues of a random Hermitian matrix fluctuate?* Duke Mathematical Journal 170 (2021), 2085–2235.
- **[Related]** Y. V. Fyodorov, N. J. Simm. *On the distribution of the maximum value of the characteristic polynomial of the GUE random matrix.* Nonlinearity 29 (2016), 2837–2855.
- **[Related]** C. Webb. *The characteristic polynomial of a random unitary matrix and Gaussian multiplicative chaos — the $L^2$-phase.* Electronic Journal of Probability 20 (2015), no. 104.
- **[Related]** M. Nikula, E. Saksman, C. Webb. *Multiplicative chaos and the characteristic polynomial of the CUE: the $L^1$-phase.* Transactions of the American Mathematical Society 373 (2020), 3905–3965.
- **[Related]** L.-P. Arguin, D. Belius, P. Bourgade, M. Radziwiłł, K. Soundararajan. *Maximum of the Riemann zeta function on a short interval of the critical line.* Communications on Pure and Applied Mathematics 72 (2019), 500–535.
- **[Related]** J. Najnudel. *On the extreme values of the Riemann zeta function on random intervals of the critical line.* Probability Theory and Related Fields 172 (2018), 387–452.
- **[Related]** L.-P. Arguin, P. Bourgade, M. Radziwiłł. *The Fyodorov–Hiary–Keating conjecture. I.* arXiv:2007.00988 (2020); *II*, arXiv:2307.00982 (2023).
- **[Related]** P. Diaconis, M. Shahshahani. *On the eigenvalues of random matrices.* Journal of Applied Probability 31A (1994), 49–62.
- **[Survey]** L.-P. Arguin. *Extrema of log-correlated random variables: principles and examples.* In *Advances in Disordered Systems, Random Processes and Some Applications*, Cambridge University Press, 2017.

## 10. Worked Example / Concrete Special Case

**(a) Exact small $N$.** For $N=1$, $U=e^{i\phi}$ with $\phi$ uniform, $P_1(\theta)=1-e^{i(\phi-\theta)}$, so $|P_1(\theta)|=2|\sin\frac{\phi-\theta}{2}|$ and $\mathcal X_1=\log 2$ deterministically. For $N=2$ with eigenvalues $e^{i\phi_1},e^{i\phi_2}$,
$$|P_2(\theta)| = 4\left|\sin\tfrac{\phi_1-\theta}{2}\right|\left|\sin\tfrac{\phi_2-\theta}{2}\right|,$$
maximised at $\theta$ antipodal-ish to the pair; if $\Delta=\phi_1-\phi_2$ then $\mathcal X_2=\log\big(2+2\cos\frac{\Delta}{2}\big)$ evaluated at the midpoint-opposite angle, with $\Delta$ having CUE density $\frac{1}{2\pi}(1-\cos\Delta)$. So $\mathcal X_2\in[\log 2,\log 4]$. No asymptotic structure is visible yet: the $\log\log N$ correction needs $N$ astronomically large.

**(b) Where the constants come from.** Model $\log|P_N|$ by the exactly hierarchical BRW of §2: $n=\log N$ generations, each particle has $e$ children (formally $\log b=1$), each step Gaussian with variance $\sigma^2=\frac12$ (matching $\operatorname{Var} = \frac12\log N$).

*First moment / union bound.* There are $e^{n}=N$ leaves; each leaf value is $\mathcal N(0,n/2)$, so
$$\mathbb E\,\\#\{\text{leaves} > a n\} = e^{n}\,\mathbb P\big(\mathcal N(0,n/2)>an\big) \approx \exp\!\big(n - a^2 n\big).$$
This vanishes iff $a>1$, giving the upper bound $\mathcal X_N \lesssim \log N$ — the leading term, and it is the correct one (ABB 2017).

*Bramson correction.* The naive first-moment threshold $a=1$ overcounts: paths reaching level $n$ must stay below the line $t\mapsto t$ at all intermediate times $t\le n$. Conditioning on this ballot-type event costs a factor $\asymp n^{-3/2}$, so the true count near $m_n$ is $\exp(n-a^2n)\cdot n^{-3/2}$; solving $an = n - \frac{c}{2}\log n$ with the $n^{-3/2}$ correction gives
$$m_n = n - \frac{3}{2}\sqrt{\frac{\sigma^2}{2\log b}}\,\log n = n - \frac34\log n.$$
Substituting $n=\log N$:
$$\boxed{\;\mathcal X_N \approx \log N - \tfrac34\log\log N\;}$$
which is exactly the Paquette–Zeitouni / Chhaibi–Madaule–Najnudel theorem. The remaining $O(1)$ term is $\mathcal G+\frac12\log\mathcal B$ in the BRW (Aïdékon), and proving the same for the genuine matrix field is the open part of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*