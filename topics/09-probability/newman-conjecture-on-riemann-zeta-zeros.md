---
id: 09-probability/newman-conjecture-on-riemann-zeta-zeros
title: "Newman Conjecture on Riemann Zeta Zeros"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Newman Conjecture on Riemann Zeta Zeros

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/newman-conjecture-on-riemann-zeta-zeros` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\Phi$ be the classical super-exponentially decaying kernel of the Riemann $\xi$-function and define the one-parameter family of entire functions

$$H_t(z) \;=\; \int_0^\infty \Phi(u)\, e^{tu^2}\cos(zu)\,du , \qquad t\in\mathbb{R}.$$

De Bruijn (1950) and Newman (1976) proved that there is a finite real constant $\Lambda$ — the **de Bruijn–Newman constant** — such that $H_t$ has only real zeros if and only if $t \ge \Lambda$. Since $H_0$ is a rescaling of $\xi$, the Riemann Hypothesis (RH) is equivalent to $\Lambda \le 0$.

**Newman's conjecture (1976):** $\Lambda \ge 0$; equivalently, for every $t<0$ the function $H_t$ has a non-real zero. Newman's gloss: *"the Riemann hypothesis, if true, is only barely so."*

Status of the two halves:

- The **lower bound** $\Lambda \ge 0$ was proved by Rodgers and Tao (Forum of Math. Pi, 2020). Newman's conjecture as literally stated is therefore a theorem.
- The **quantitative problem** — pin down $\Lambda$ — is open. Combining Rodgers–Tao with the RH equivalence gives the exact statement
 $$\text{RH} \iff \Lambda = 0 ,$$
 and the best unconditional upper bound is $\Lambda \le 0.22$ (Polymath15, 2019). The open catalog entry is: **prove $\Lambda = 0$ (i.e. RH), or exhibit $\Lambda > 0$ (i.e. disprove RH).**

A complete resolution means determining the value of $\Lambda$, or proving a strict inequality $\Lambda>0$; a proof of $\Lambda \le 0$ would, with Rodgers–Tao, settle RH.

## 2. Mathematical Foundations

**The $\xi$-function and its kernel.** With $\zeta$ the Riemann zeta function, set

$$\xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma\!\left(\tfrac{s}{2}\right)\zeta(s), \qquad \Xi(z) = \xi\!\left(\tfrac12 + iz\right).$$

$\Xi$ is entire of order $1$, even, real on $\mathbb{R}$, and RH says all zeros of $\Xi$ are real. Riemann's Fourier representation is

$$\Xi(z) = 2\int_0^\infty \Phi(u)\cos(zu)\,du, \qquad \Phi(u)=\sum_{n=1}^\infty\left(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\right)e^{-\pi n^2 e^{4u}} .$$

$\Phi$ is positive, even, and $\Phi(u)=O(e^{-\pi e^{4|u|}})$, so inserting the Gaussian factor $e^{tu^2}$ converges for every real $t$ and $H_t$ is entire of order $1$ (for $t\le 0$) or order $2$, genus $2$ (for $t>0$). Normalisation: $H_0(z)=\tfrac18\,\Xi(z/2)$.

**Backward heat flow.** Differentiating under the integral, $u^2\cos(zu) = -\partial_z^2\cos(zu)$, so

$$\partial_t H_t(z) = -\,\partial_z^2 H_t(z),$$

the *backward* heat equation. This is the probabilistic heart of the problem: $H_t = e^{-t\partial_z^2}H_0$, so increasing $t$ runs Gaussian smoothing in reverse in $z$ (forward in the Fourier variable), which pushes complex zeros onto $\mathbb{R}$ and makes real zeros repel.

**Zero dynamics as an interacting particle system.** If at time $t$ the zeros of $H_t$ are simple and real, $\{x_j(t)\}$, they satisfy the (formally derived, rigorously justified after regularisation) gradient system

$$\dot x_j(t) = 2\sum_{k\ne j}\frac{1}{x_j(t)-x_k(t)} ,$$

a deterministic Calogero–Moser / Dyson-type flow with **repulsive** $1/r$ interaction — the zero-temperature limit of Dyson Brownian motion, whose stationary local statistics are the GUE sine kernel. Run backwards ($t$ decreasing) the interaction is attractive: real zeros collide in finite backward time and leave the axis as conjugate pairs unless the configuration is exceptionally rigid.

**De Bruijn–Newman monotonicity.** If $H_{t_0}$ has only real zeros then so does $H_t$ for all $t\ge t_0$ (Pólya–de Bruijn: the Laguerre–Pólya class $\mathcal{LP}$ is preserved by $e^{-t\partial_z^2}$, $t\ge0$). Hence
$$\Lambda := \inf\{t\in\mathbb{R}: H_t \text{ has only real zeros}\}$$
is well defined, and $\{t : H_t \in \mathcal{LP}\} = [\Lambda,\infty)$.

**Lehmer pairs.** A pair of consecutive zeros $\gamma_k<\gamma_{k+1}$ of $\zeta$ on the critical line is a *Lehmer pair* if their gap is anomalously small relative to the mean spacing $2\pi/\log(\gamma_k/2\pi)$. Each such pair, via the backward attractive dynamics, forces a lower bound $\Lambda > -c$ with $c$ controlled by the normalised gap.

## 3. History & State of the Art (SOTA)

- **1926–1927, Pólya.** Studied $\int \Phi(u)e^{tu^2}\cos(zu)du$-type deformations and the reality of zeros of Fourier transforms; origin of the "Pólya–Jensen" program.
- **1950, de Bruijn.** *The roots of trigonometric integrals* (Duke Math. J.): $H_t$ has only real zeros for $t\ge 1/2$, and reality propagates upward in $t$. Gives $\Lambda\le 1/2$.
- **1976, Newman.** *Fourier transforms with only real zeros* (Proc. AMS): existence and finiteness of $\Lambda$, proof that $\Lambda \ge -1/2$, and the conjecture $\Lambda\ge0$.
- **1988–2011, numerical lower bounds.** A chain of Lehmer-pair computations: $\Lambda>-50$ (Csordas–Norfolk–Varga 1988), $\Lambda>-5$ (te Riele 1991), $\Lambda>-4.379\times10^{-6}$ (Csordas–Smith–Varga 1994), $\Lambda>-5.895\times10^{-9}$ (Csordas–Odlyzko–Smith–Varga 1993), $\Lambda\ge-2.7\times10^{-9}$ (Odlyzko 2000), $\Lambda>-1.15\times10^{-11}$ (Saouter–Gourdon–Demichel 2011).
- **2009, Ki–Kim–Lee.** $\Lambda<1/2$ strictly; also: for $t>0$, $H_t$ has only finitely many non-real zeros.
- **2018/2020, Rodgers–Tao.** $\Lambda\ge0$: Newman's conjecture proved. Method: if $\Lambda<0$, the backward flow from time $\Lambda$ forces the zeros of $\Xi$ at time $0$ to be asymptotically *equally spaced* at the local scale — a rigidity incompatible with known pair-correlation/large-gap facts for zeta zeros.
- **2019, Polymath15 (Tao et al.).** $\Lambda\le0.22$, via a rigorous effective approximation of $H_t$ plus a computer-assisted Newton/barrier argument.

**Current interval:** $0 \le \Lambda \le 0.22$.

## 4. Partial Results / Verified Cases

- **Reality regime.** $H_t$ has only real zeros for all $t\ge 0.22$ (Polymath15, 2019), improving de Bruijn's $t\ge 1/2$ and Ki–Kim–Lee's $t>1/2-\varepsilon$.
- **Non-reality regime.** $H_t$ has non-real zeros for every $t<0$ (Rodgers–Tao, 2020) — this is the full lower-bound half.
- **Finiteness.** For every $t>0$, $H_t$ has at most finitely many non-real zeros, and all zeros of $H_t$ lie in the strip $|\mathrm{Im}\,z|\le \sqrt{\max(0,-t)}\,{+}\,o(1)$-type bounds (de Bruijn; Ki–Kim–Lee).
- **Computational verification of $\Lambda\le0$ consequences.** RH is verified for the first $1.2\times10^{13}$ zeros (Gourdon–Demichel, 2004) and for all $\gamma$ with $|\gamma|\le 3\times10^{12}$ (Platt–Trudgian, 2021, rigorous). These are consistent with, but do not prove, $\Lambda=0$.
- **Analogues where the constant is known.** For Dirichlet $L$-functions and for the $\xi$-function of function fields over $\mathbb{F}_q$ (where RH is a theorem of Weil), the corresponding de Bruijn–Newman constant is $\le 0$; combined with the Rodgers–Tao argument transplanted to those families, one gets $\Lambda=0$ for such analogues — the only cases where the constant is pinned exactly.
- **Jensen-polynomial regime.** Griffin–Ono–Rolen–Zagier (2019) proved hyperbolicity of the degree-$d$ Jensen polynomials $J^{d,n}_\xi$ for every fixed $d$ and all $n\gg_d 1$ — the Pólya–Jensen criterion holds in each fixed degree, with $J^{d,n}$ converging to Hermite polynomials (a GUE-flavoured limit).

## 5. Principal Obstacles

- **RH-completeness.** $\Lambda\le0$ *is* RH. Every technique that would establish it must therefore be strong enough to prove RH; no known analytic method (zero-density estimates, mollified moments, sieve-theoretic zero-detection) reaches that strength.
- **Backward heat flow is ill-posed.** The map $t\mapsto H_t$ is a backward parabolic evolution; $H_0$ determines $H_t$ for $t<0$ only through the analytic continuation of a divergent Gaussian smoothing. Standard PDE stability estimates run the wrong way, so control of $H_t$ for $t<0$ cannot be obtained by perturbing $H_0$.
- **Zero collisions are non-perturbative.** The particle system $\dot x_j = 2\sum_{k\ne j}(x_j-x_k)^{-1}$ has a singular kernel and infinitely many particles with logarithmically growing density $\tfrac{1}{2\pi}\log\frac{|x|}{4\pi}$. Rigorous well-posedness requires truncation plus a priori spacing bounds; these bounds degrade exactly in the regime (near-colliding Lehmer pairs) that carries the arithmetic information.
- **Lower-bound methods saturate at $0$.** Lehmer-pair arguments give $\Lambda > -c$ with $c$ proportional to the square of the smallest observed normalised gap. They can approach $0$ from below but can never certify $\Lambda>0$: they are one-sided by construction. Rodgers–Tao replaced them by a global entropy/rigidity argument, which likewise yields only $\ge 0$.
- **No mechanism to detect a positive $\Lambda$.** Proving $\Lambda>0$ means producing a non-real zero of $\Xi$, i.e. disproving RH. There is no known finite computation or structural criterion whose truth would certify $\Lambda>0$ short of an explicit counterexample.
- **Upper-bound methods are computation-bound.** Polymath15's $\Lambda\le0.22$ comes from effective error terms in an approximate functional equation for $H_t$ plus verified numerics up to a finite height; pushing $t$ toward $0$ makes the required height grow super-polynomially, and the barrier method degenerates as $t\downarrow0$ because the zero repulsion that keeps the argument stable vanishes.

## 6. The Gap

Proven: $\Lambda\in[0,0.22]$. Wanted: $\Lambda=0$.

The precise missing step is a lower bound on the *backward-time survival* of reality: one must show that the real-zero configuration of $\Xi$ is rigid enough that it does **not** develop a complex pair under any amount of backward flow — equivalently, that the infinite attractive particle system started from the zeta zeros has no collision in backward time $(-\varepsilon,0]$ for any $\varepsilon>0$. Rodgers–Tao show the *opposite* rigidity statement (over-rigidity is impossible), which caps $\Lambda$ from below; nothing in the method bounds how far above $0$ the collision time sits. Bridging $[0,0.22]$ down to $\{0\}$ requires either (i) an unconditional zero-free region for $H_t$ valid for all $t>0$ at all heights, or (ii) an arithmetic input — an exact-order pair-correlation or moment identity — strong enough to exclude collisions, which is RH-equivalent in strength.

## 7. Current Research (as of June 2026)

- **Effective analysis of $H_t$.** Continuation of the Polymath15 toolkit (UCLA, and the Polymath collaborators around Tao) — sharper effective approximate functional equations for $H_t$ and improved barrier certificates aiming at $\Lambda \le 0.1$. Progress is incremental and computation-limited. *(frontier — verify)*
- **Random-matrix / particle-system methods.** Groups working on Dyson Brownian motion rigidity (Bourgade, Erdős, Yau and collaborators) supply the local-law and gap-universality technology that Rodgers–Tao used in caricature; transplanting quantitative rigidity to the deterministic zeta flow is an active line. *(frontier — verify)*
- **Jensen polynomials and hyperbolicity.** Post-Griffin–Ono–Rolen–Zagier work (Ono's group, Emory/UVA) on making the degree-$d$ thresholds effective and uniform in $d$; a uniform threshold would give new information on $\Lambda$.
- **Function-field and $L$-function analogues.** Determining the de Bruijn–Newman constant for families (Dirichlet $L$, automorphic $L$, curves over $\mathbb{F}_q$) to test which features of the proof of $\Lambda\ge0$ are arithmetic and which are dynamical.
- **Lehmer-pair statistics.** Ongoing large-height zero computations (successors to Odlyzko's and Platt's) supply extremal gap data; these now serve as tests of GUE predictions rather than as $\Lambda$-bounds, since $\Lambda\ge0$ is settled.

## 8. Future Work

- Prove a *quantitative* strengthening of Rodgers–Tao: not just "the zeros are not asymptotically equispaced" but an explicit lower bound on the deviation, which would let one iterate the argument and possibly obtain $\Lambda \le \delta$ for small $\delta$ from arithmetic input alone.
- Develop a rigorous well-posedness theory for the infinite attractive $1/r$ particle system with logarithmic density, including a collision-time criterion in terms of pair correlation.
- Make the Griffin–Ono–Rolen–Zagier degree thresholds effective and uniform; a bound of the form "$J^{d,n}$ hyperbolic for $n\ge C d^A$" with explicit $C,A$ would give a new route to upper bounds on $\Lambda$.
- Extend Polymath15's effective machinery to the whole family of $L$-functions in the Selberg class, seeking a constant $\Lambda$ uniform in conductor.
- Search for a *finitary certificate* whose verification would imply $\Lambda>0$ — currently none is known; even a conditional one would reframe the problem.

## 9. Key References

- **[Foundational]** N. G. de Bruijn. *The roots of trigonometric integrals.* Duke Mathematical Journal 17 (1950), 197–226.
- **[Foundational]** C. M. Newman. *Fourier transforms with only real zeros.* Proceedings of the American Mathematical Society 61 (1976), 245–251.
- **[SOTA]** B. Rodgers and T. Tao. *The de Bruijn–Newman constant is non-negative.* Forum of Mathematics, Pi, 8 (2020), e6.
- **[SOTA]** D. H. J. Polymath. *Effective approximation of heat flow evolution of the Riemann $\xi$ function, and a new upper bound for the de Bruijn–Newman constant.* Research in the Mathematical Sciences 6 (2019), article 31.
- **[Structural]** H. Ki, Y.-O. Kim, J. Lee. *On the de Bruijn–Newman constant.* Advances in Mathematics 222 (2009), 281–306.
- **[Computational]** G. Csordas, T. S. Norfolk, R. S. Varga. *A lower bound for the de Bruijn–Newman constant $\Lambda$.* Numerische Mathematik 52 (1988), 483–497.
- **[Computational]** G. Csordas, A. M. Odlyzko, W. Smith, R. S. Varga. *A new Lehmer pair of zeros and a new lower bound for the de Bruijn–Newman constant $\Lambda$.* Electronic Transactions on Numerical Analysis 1 (1993), 104–111.
- **[Computational]** G. Csordas, W. Smith, R. S. Varga. *Lehmer pairs of zeros, the de Bruijn–Newman constant $\Lambda$, and the Riemann Hypothesis.* Constructive Approximation 10 (1994), 107–129.
- **[Computational]** A. M. Odlyzko. *An improved bound for the de Bruijn–Newman constant.* Numerical Algorithms 25 (2000), 293–303.
- **[Computational]** Y. Saouter, X. Gourdon, P. Demichel. *An improved lower bound for the de Bruijn–Newman constant.* Mathematics of Computation 80 (2011), 2281–2287.
- **[Related]** M. Griffin, K. Ono, L. Rolen, D. Zagier. *Jensen polynomials for the Riemann zeta function and other sequences.* PNAS 116 (2019), 11103–11110.
- **[Survey]** R. S. Varga. *Scientific Computation on Mathematical Problems and Conjectures.* CBMS-NSF Regional Conference Series in Applied Mathematics 60, SIAM, 1990.
- **[Background]** H. L. Montgomery. *The pair correlation of zeros of the zeta function.* Proc. Sympos. Pure Math. 24, AMS, 1973, 181–193.

## 10. Worked Example / Concrete Special Case

**Two-particle model, exactly solvable.** Take the finite caricature $P_0(z)=z^2-a^2$ with $a>0$, evolved by the same backward heat equation $\partial_t P = -\partial_z^2 P$. Since $\partial_z^2 P_0 = 2$,

$$P_t(z) = z^2 - a^2 + 2t \quad\Longrightarrow\quad \text{zeros } \pm\sqrt{a^2-2t}.$$

For $t\ge0$ the zeros are real and separate (repulsion). Running backward, at
$$t_\ast = -\tfrac{a^2}{2}$$
the pair collides at the origin and for $t<t_\ast$ becomes the conjugate pair $\pm i\sqrt{|2t|-a^2}$. So for this model $\Lambda_{\text{model}} = -a^2/2$: **the tighter the pair, the closer $\Lambda$ sits to $0$ from below.** This is exactly the mechanism behind every Lehmer-pair lower bound. Check against the ODE: with $x_1=-x_2=a(t)$, $\dot x_1 = 2/(x_1-x_2) = 1/a$, and $a(t)=\sqrt{a^2_0-2t}$ gives $\dot a = -1/a$ under $t\mapsto -t$ — consistent.

**Numerical instance: Lehmer's pair.** The classical near-collision occurs at the zeros
$$\gamma_k = 7005.06286617\ldots,\qquad \gamma_{k+1}=7005.10056321\ldots,$$
so the gap is $\delta = \gamma_{k+1}-\gamma_k \approx 3.77\times10^{-2}$. The mean spacing at that height is
$$\frac{2\pi}{\log(\gamma_k/2\pi)} = \frac{2\pi}{\log(1114.9\ldots)} \approx \frac{6.2832}{7.0166}\approx 0.8955,$$
so the normalised gap is $\delta \approx 0.042$ of average — a $4\%$ spacing, wildly improbable under GUE, whose small-gap density vanishes like $s^2$.

Feeding the half-gap $a=\delta/2\approx1.885\times10^{-2}$ into the two-particle model gives the crude estimate $t_\ast = -a^2/2 \approx -1.8\times10^{-4}$, i.e. $\Lambda \gtrsim -1.8\times10^{-4}$. The rigorous version must account for the pressure of all the other zeros (which resist the collision) and for the $H_0(z)=\tfrac18\Xi(z/2)$ rescaling; Csordas–Smith–Varga's differential inequality for Lehmer pairs turns this same pair into the theorem $\Lambda > -4.379\times10^{-6}$, and a much tighter pair found by Odlyzko near height $10^{18}$ gave $\Lambda>-5.895\times10^{-9}$.

**Reading the example.** Every Lehmer pair pushes $\Lambda$ up toward $0$; none can push past it. Rodgers–Tao's theorem says the process is not accidental: if $\Lambda<0$ then *almost every* consecutive pair would have to be near-equispaced at time $0$, which contradicts the observed (and provable) fluctuation of the gaps. What remains open is the other side — no computation of this type can show that the collision time is exactly $0$ rather than $+0.1$, and that gap is precisely RH.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*