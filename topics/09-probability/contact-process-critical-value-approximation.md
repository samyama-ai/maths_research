---
id: 09-probability/contact-process-critical-value-approximation
title: "Contact Process Critical Value Approximation"
topic: 09-probability
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Contact Process Critical Value Approximation

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/contact-process-critical-value-approximation` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

The basic contact process on $\mathbb{Z}$ has a single parameter $\lambda > 0$ (the infection rate) and a phase transition at a critical value $\lambda_c$. Numerical work places it at
$$\lambda_c(\mathbb{Z}) = 1.6488 \pm 0.0001 ,$$
while the best rigorous bracket is
$$1.539 \;\le\; \lambda_c(\mathbb{Z}) \;\le\; 1.942 .$$

**The problem, in three graded forms.**

1. **Closed form.** Determine $\lambda_c(\mathbb{Z})$ exactly, or prove that it is not algebraic / not expressible in closed form. No exact value is known or conjectured.
2. **Rigorous approximation.** Produce a convergent scheme with certified error bars: sequences $\ell_n \uparrow \lambda_c$ and $u_n \downarrow \lambda_c$, each computable in finite time, with $u_n - \ell_n \to 0$. The bracket has been narrower than a factor $1.3$ since 1995 and has not closed.
3. **Validation of the numerics.** Prove that the series-expansion estimate $1.6488$ is correct to the claimed precision. Currently the numeric estimate is not even known to lie inside a rigorously certified interval of width $10^{-3}$.

A complete resolution of (2) would be a proof that some explicit algorithm outputs $\lambda_c$ to any requested accuracy, i.e. that $\lambda_c$ is a *computable real* with an effective modulus. Even this weak-looking statement is open.

## 2. Mathematical Foundations

**The process.** The contact process is the Feller Markov process $(\eta_t)_{t\ge 0}$ on $\{0,1\}^{\mathbb{Z}^d}$, or equivalently on subsets $A_t = \{x : \eta_t(x) = 1\}$, with generator acting on cylinder functions $f$ by
$$(\Omega f)(\eta) \;=\; \sum_{x \in \mathbb{Z}^d} c(x,\eta)\,\bigl[f(\eta^x) - f(\eta)\bigr], \qquad
c(x,\eta) = \begin{cases} 1, & \eta(x) = 1,\\[2pt] \lambda \displaystyle\sum_{y \sim x} \eta(y), & \eta(x) = 0,\end{cases}$$
where $\eta^x$ flips the coordinate at $x$ and $y \sim x$ means $\|y - x\|_1 = 1$. Infected sites recover at rate $1$; each infected site infects each healthy neighbour at rate $\lambda$. (Physics convention: infection at rate $\tilde\lambda\, n/(2d)$, so $\tilde\lambda = 2d\,\lambda$; on $\mathbb{Z}$, $\tilde\lambda_c \approx 3.2976$.)

**Harris graphical representation.** Place independent Poisson processes on $\mathbb{Z}^d\times[0,\infty)$: rate-$1$ "recovery" marks $\times$ at each site, and rate-$\lambda$ arrows $x \to y$ for each ordered neighbour pair. Then $y \in A_t^A$ iff there is an active path from $A\times\{0\}$ to $(y,t)$ moving up in time, never crossing a $\times$, and jumping along arrows. This makes the contact process an oriented percolation model in continuous time.

**Self-duality.** For finite $A$ and any $B$,
$$\mathbb{P}\bigl(A_t^A \cap B \neq \emptyset\bigr) = \mathbb{P}\bigl(A_t^B \cap A \neq \emptyset\bigr).$$
Consequently the upper invariant measure $\bar\nu_\lambda = \lim_{t\to\infty}\delta_{\mathbb{Z}^d} S(t)$ satisfies $\bar\nu_\lambda\{\eta : \eta \equiv 0 \text{ on } A\} = \lim_t \mathbb{P}(A^A_t = \emptyset)$.

**Critical value.** With $\theta(\lambda) = \mathbb{P}\bigl(A_t^{\{0\}} \neq \emptyset \ \forall t\bigr)$,
$$\lambda_c(\mathbb{Z}^d) \;=\; \inf\{\lambda > 0 : \theta(\lambda) > 0\} .$$
Monotonicity in $\lambda$ (basic coupling) makes $\theta$ nondecreasing, so this is a genuine threshold. Equivalently, by Durrett's edge-speed theorem in $d=1$, $\lambda_c = \inf\{\lambda : \alpha(\lambda) > 0\}$ where $\alpha(\lambda) = \lim_t r_t/t$ is the a.s. speed of the right edge $r_t = \sup A_t^{(-\infty,0]}$, whose existence follows from Kingman subadditivity.

**Foundational theorems relied on.**
- *Harris (1974):* $0 < \lambda_c(\mathbb{Z}^d) < \infty$, with the branching-random-walk comparison giving $\lambda_c(\mathbb{Z}^d) \ge 1/(2d)$.
- *Bezuidenhout–Grimmett (1990):* $\theta(\lambda_c) = 0$ in every dimension — the critical process dies out.
- *Bezuidenhout–Grimmett (1991):* for $\lambda < \lambda_c$, $\mathbb{P}(A_t^{\{0\}} \neq \emptyset) \le C e^{-ct}$ (sharpness).

## 3. History & State of the Art (SOTA)

- **1974.** Harris introduces the process and proves $1 \le \lambda_c(\mathbb{Z}) \le 2\cdot$const via a subcritical branching comparison and a crude contour argument.
- **1978.** Holley and Liggett prove $\lambda_c(\mathbb{Z}) \le 2$ by exhibiting a product-like renewal measure that is a supersolution of the dual dynamics — the first genuinely sharp upper-bound technique, still the parent of all later ones.
- **1980–81.** Durrett establishes the edge speed and shape results; Griffeath's survey systematizes "the basic contact processes".
- **1988.** Ziezold and Grillenberger obtain the rigorous lower bound $\lambda_c(\mathbb{Z}) \ge 1.539$ via a computer-assisted finite-state truncation of the dual semigroup.
- **1990–91.** Bezuidenhout and Grimmett settle death at criticality and exponential subcritical decay, removing the possibility of an intermediate phase but giving no numerical information.
- **1995.** Liggett improves the upper bound to $\lambda_c(\mathbb{Z}) \le 1.942$ using higher-order renewal measures with several free parameters, verified by rigorous interval computation.
- **1991–1999.** Series expansions (Dickman–Jensen time-dependent perturbation theory; Jensen's low-density algorithms for directed percolation) push the numeric estimate to $\tilde\lambda_c = 3.29785(2)$, i.e. $\lambda_c = 1.648925(10)$, with $\sim 20$–$30$ series terms and Padé/differential-approximant analysis.
- **2000s–2020s.** Large-scale Monte Carlo and dynamic scaling reproduce the same value; the $1+1$-dimensional directed percolation exponents $\beta = 0.276486(8)$, $\nu_\perp = 1.096854(4)$, $\nu_\parallel = 1.733847(6)$ are known to more digits than $\lambda_c$ is known rigorously.

The 1995 bound has not been improved in the literature in thirty years.

## 4. Partial Results / Verified Cases

- **Rigorous bracket on $\mathbb{Z}$:** $1.539 \le \lambda_c \le 1.942$ (Ziezold–Grillenberger 1988; Liggett 1995). Width $0.403$, relative width $\approx 24\%$.
- **Elementary bounds in all $d$:** $\lambda_c(\mathbb{Z}^d) \ge 1/(2d)$ (branching comparison), and $2d\,\lambda_c(\mathbb{Z}^d) \to 1$ as $d \to \infty$ — the mean-field value is asymptotically exact in high dimension.
- **Qualitative structure fully resolved:** $\theta(\lambda_c) = 0$ (all $d$); exponential decay for $\lambda<\lambda_c$; the complete convergence theorem for $\lambda>\lambda_c$; $\theta$ continuous on $(0,\infty)$.
- **Exactly solvable relatives:** on the homogeneous tree $\mathbb{T}_d$ there are two distinct critical values $\lambda_1 < \lambda_2$ (Pemantle 1992), with explicit bounds; on the complete graph and in the mean-field limit $\lambda_c$ is exact and elementary.
- **One-sided variants:** the "one-sided" contact process and certain long-range models admit exact renewal-measure solutions where the Holley–Liggett bound is *tight*, giving exact critical values — the only known family with closed-form answers.
- **Computational verification:** $\lambda_c$ estimated to $\sim 6$ significant figures by three independent nonrigorous methods (series, Monte Carlo, transfer-matrix / density-matrix truncation) with mutual agreement at $10^{-5}$.

## 5. Principal Obstacles

- **No exact solvability.** The contact process is not integrable: the generator has no free-fermion, Yang–Baxter or determinantal structure (unlike ASEP or the voter model). Duality maps the process to itself, not to a simpler object, so it removes no degrees of freedom.
- **Hierarchy non-closure.** Correlation equations for $\mathbb{P}(\eta \equiv 1 \text{ on } A)$ couple each $|A|=n$ observable to $|A|=n+1$ observables. Every truncation (mean-field, pair, $(n,m)$-cluster) is *uncontrolled*: it produces a number but no error bound, and the numbers converge slowly and non-monotonically.
- **Bounds are one-sided by construction.** Upper bounds come from finding a measure that survives under the dual dynamics; lower bounds from finite truncations that must dominate death. Neither family is known to converge to $\lambda_c$, and there is no duality between the two schemes that would force the gap to close.
- **Loss in the renormalization.** Bezuidenhout–Grimmett block arguments prove sharpness but only after passing to blocks of unspecified, astronomically large size; the constants are non-explicit, so the machinery that resolves the qualitative theory contributes nothing numerically.
- **Non-monotone in the wrong variable.** The Holley–Liggett renewal ansatz optimizes over a finite-dimensional family; enlarging the family improves the bound but with rapidly growing algebra (Liggett's 1995 computation is already at the edge of hand verification) and no proof that the infimum over all such families equals $\lambda_c$.

## 6. The Gap

Proven: $\lambda_c \in [1.539, 1.942]$, plus the full qualitative phase picture. Wanted: the number itself, or brackets of arbitrary tightness.

The precise missing step is a **convergent variational characterization**. Upper bounds need a family $\mathcal{M}_n$ of trial measures with $\inf\{\lambda : \exists \mu \in \mathcal{M}_n \text{ supersolution}\} \downarrow \lambda_c$; lower bounds need finite truncations whose failure thresholds increase to $\lambda_c$. Each side has candidates; neither has a convergence proof. Concretely, no one has shown that the Ziezold–Grillenberger truncation at level $n$ gives $\ell_n \to \lambda_c$ rather than stalling below it, and no one has shown that renewal measures of unbounded order exhaust the survival region. Closing the gap therefore does not require a new phase-transition theorem — it requires converting the qualitative renormalization into a scheme with computable, shrinking constants.

## 7. Current Research (as of June 2026)

- **Rigorous computational probability.** Interval-arithmetic and SDP-relaxation approaches to particle-system generators: pose "does a supersolution exist in this $n$-parameter family?" as a certified feasibility problem. Groups working on computer-assisted proofs for lattice models are the natural home; no published improvement on $1.942$ yet. *(frontier — verify)*
- **Sum-of-squares / moment hierarchies for interacting particle systems.** Adapting Lasserre-type hierarchies to the correlation equations, which would give lower bounds with certified convergence in principle. Applied successfully to some spin systems; contact-process instances are reported but not yet competitive with $1.539$. *(frontier — verify)*
- **High-precision numerics.** Tensor-network and density-matrix renormalization treatments of the $1+1$-D directed-percolation transfer matrix continue to refine $\tilde\lambda_c$; current consensus values agree to $\sim 10^{-6}$.
- **Structural probability.** Continued work on contact processes in random environments, on trees, on scale-free and evolving graphs, where the phenomenon $\lambda_c = 0$ (heavy-tailed degrees) is the focus; this is where most current effort sits, rather than on the $\mathbb{Z}$ constant.
- **Conjectural non-closed-form.** Informal consensus, echoing the situation for the 2-D self-avoiding walk connective constant, is that $\lambda_c(\mathbb{Z})$ has no closed form; no proof technique for such a statement exists.

## 8. Future Work

- Prove that the Holley–Liggett renewal hierarchy is **complete**: that for every $\lambda > \lambda_c$ some finite-order renewal measure certifies survival. This alone yields $u_n \downarrow \lambda_c$.
- Give an **explicit-constant** Bezuidenhout–Grimmett block construction: a block size $L(\lambda)$ and coupling estimate that are computable. This would convert sharpness into an effective algorithm.
- Prove **computability with modulus**: exhibit any pair of algorithms producing $\ell_n \uparrow \lambda_c$, $u_n \downarrow \lambda_c$. Suggested as the minimal honest target by several authors, and strictly weaker than a closed form.
- Import **rigorous series-analysis** technology: bound the truncation error of the low-density expansion, as has been partially done for percolation thresholds, to certify at least the first two decimals of $1.6488$.
- Settle whether the **$(n,m)$-cluster approximations converge** to $\lambda_c$ as $n \to \infty$; empirically they do, at an apparently power-law rate, with no proof.

## 9. Key References

- **[Foundational]** Harris, T. E. *Contact interactions on a lattice.* Annals of Probability 2 (1974), 969–988.
- **[Foundational]** Holley, R. and Liggett, T. M. *The survival of contact processes.* Annals of Probability 6 (1978), 198–206.
- **[Foundational]** Durrett, R. *On the growth of one dimensional contact processes.* Annals of Probability 8 (1980), 890–907.
- **[Foundational]** Griffeath, D. *The basic contact processes.* Stochastic Processes and their Applications 11 (1981), 151–185.
- **[Structural]** Bezuidenhout, C. and Grimmett, G. *The critical contact process dies out.* Annals of Probability 18 (1990), 1462–1482.
- **[Structural]** Bezuidenhout, C. and Grimmett, G. *Exponential decay for subcritical contact and percolation processes.* Annals of Probability 19 (1991), 984–1009.
- **[Bounds — lower]** Ziezold, H. and Grillenberger, C. *On the critical infection rate of the one-dimensional basic contact process: numerical results.* Journal of Applied Probability 25 (1988), 1–8.
- **[Bounds — upper / SOTA]** Liggett, T. M. *Improved upper bounds for the contact process critical value.* Annals of Probability 23 (1995), 697–723.
- **[Bounds]** Katori, M. and Konno, N. *Upper bounds for survival probability of the contact process.* Journal of Statistical Physics 63 (1991), 115–130.
- **[Trees]** Pemantle, R. *The contact process on trees.* Annals of Probability 20 (1992), 2089–2116.
- **[Numerics]** Dickman, R. and Jensen, I. *Time-dependent perturbation theory for nonequilibrium lattice models.* Physical Review Letters 67 (1991), 2391–2394.
- **[Numerics]** Jensen, I. *Low-density series expansions for directed percolation: I. A new efficient algorithm with applications to the square lattice.* Journal of Physics A 32 (1999), 5233–5249.
- **[Approximations]** ben-Avraham, D. and Köhler, J. *Mean-field (n,m)-cluster approximation for lattice models.* Physical Review A 45 (1992), 8358–8370.
- **[Book / Survey]** Liggett, T. M. *Stochastic Interacting Systems: Contact, Voter and Exclusion Processes.* Springer, Grundlehren 324, 1999.
- **[Book]** Liggett, T. M. *Interacting Particle Systems.* Springer, 1985.
- **[Survey]** Hinrichsen, H. *Non-equilibrium critical phenomena and phase transitions into absorbing states.* Advances in Physics 49 (2000), 815–958.
- **[Book]** Marro, J. and Dickman, R. *Nonequilibrium Phase Transitions in Lattice Models.* Cambridge University Press, 1999.
- **[Book]** Henkel, M., Hinrichsen, H. and Lübeck, S. *Non-Equilibrium Phase Transitions, Vol. 1: Absorbing Phase Transitions.* Springer, 2008.

## 10. Worked Example / Concrete Special Case

**Cluster approximations on $\mathbb{Z}$, computed and compared to truth.**

*Level 1 (mean field).* Let $\rho(t) = \mathbb{P}(\eta_t(0)=1)$ and assume sites independent. A site recovers at rate $1$; a healthy site is infected at rate $\lambda$ per infected neighbour, and has $2$ neighbours:
$$\frac{d\rho}{dt} = -\rho + 2\lambda\,\rho(1-\rho).$$
The nonzero fixed point $\rho^* = 1 - 1/(2\lambda)$ is positive iff $\lambda > 1/2$, so
$$\lambda_c^{\mathrm{MF}} = 0.5 .$$
This underestimates by a factor $3.3$: independence ignores that infected sites cluster, wasting infection attempts on already-infected neighbours.

*Level 2 (pair approximation).* Track $\rho = \mathbb{P}(\eta(0)=1)$ and $z = \mathbb{P}(\eta(0)=\eta(1)=1)$. Writing $\mathbb{P}(\bullet\circ) = \rho - z$ for an adjacent infected–healthy pair:
$$\frac{d\rho}{dt} = -\rho + 2\lambda(\rho - z), \qquad
\frac{dz}{dt} = -2z + 2\lambda(\rho-z) + 2\lambda\,\mathbb{P}(\bullet\circ\bullet),$$
the last term being creation of a pair when the middle site of $\bullet\circ\bullet$ is infected from the far side. Close the hierarchy with the Bayesian closure
$$\mathbb{P}(\bullet\circ\bullet) \approx \frac{\mathbb{P}(\bullet\circ)\,\mathbb{P}(\circ\bullet)}{\mathbb{P}(\circ)} = \frac{(\rho-z)^2}{1-\rho}.$$
Set $u = z/\rho$ (conditional probability that a neighbour of an infected site is infected). At a stationary point with $\rho > 0$, the first equation gives $2\lambda(1-u) = 1$. Dividing the second by $\rho$ and letting $\rho \downarrow 0$ at the threshold kills the closure term ($\propto \rho$), leaving $2u = 2\lambda(1-u) = 1$, so $u = 1/2$ and
$$\lambda_c^{\mathrm{pair}} = 1 .$$

*Comparison.*

| method | $\lambda_c$ (Harris) | $\tilde\lambda_c = 2\lambda_c$ | error vs. $1.6488$ |
|---|---|---|---|
| mean field | $0.5$ | $1$ | $-70\%$ |
| pair | $1$ | $2$ | $-39\%$ |
| Harris branching bound (rigorous) | $\ge 1$ | $\ge 2$ | — |
| Ziezold–Grillenberger (rigorous) | $\ge 1.539$ | $\ge 3.078$ | $-6.7\%$ |
| Liggett 1995 (rigorous) | $\le 1.942$ | $\le 3.884$ | $+17.8\%$ |
| series / Monte Carlo | $1.6488$ | $3.2976$ | reference |

Two features of the table are the whole problem. First, the pair approximation coincidentally reproduces exactly the elementary rigorous lower bound $\lambda_c \ge 1$, and both are far off. Second, going from level $1$ to level $2$ recovers less than half the deficit; empirically the $(n,1)$-cluster sequence approaches $1.6488$ like a power of $1/n$, so reaching four correct digits by this route needs cluster sizes far beyond what can be handled — and, crucially, with no bound on the remaining error at any $n$. That is exactly the "uncontrolled truncation" obstacle of Section 5, made arithmetic.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*