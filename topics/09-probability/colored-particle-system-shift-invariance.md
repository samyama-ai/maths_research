---
id: 09-probability/colored-particle-system-shift-invariance
title: "Stochastic Six-Vertex and Colored Interacting Particle System Symmetry"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Stochastic Six-Vertex and Colored Interacting Particle System Symmetry

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/colored-particle-system-shift-invariance` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The **shift-invariance** phenomenon asserts that multi-point joint distributions of height functions in integrable stochastic systems — the stochastic six-vertex model, colored ASEP/TASEP, exponential and Brownian last passage percolation (LPP), directed polymers — are unchanged under lattice shifts of an *individual* observation point, even though the underlying random field is manifestly changed by such a shift.

Concretely, for a "down-right" ordered family of observation points, the vector of height functions has the same law as the vector obtained by translating one distinguished coordinate together with its associated boundary/color datum. No coupling of the two fields is asserted: the identity is in distribution only, and each marginal is already known to be identical for trivial reasons; the content is the **joint** law.

A complete resolution consists of (i) proving the identities for the full colored $U_q(\widehat{\mathfrak{sl}}_{n+1})$ vertex-model hierarchy, (ii) transferring them to all degenerations (polymers, KPZ equation, directed landscape), and (iii) explaining *why* they hold — i.e. identifying a structural mechanism (a bijection, a symmetry of a Markov kernel, or a representation-theoretic identity) rather than a coincidence of computable observables. Items (i) and (ii) are now largely theorems (2020–2024); item (iii), and the half-space and continuum extensions, remain open.

## 2. Mathematical Foundations

**Stochastic six-vertex model.** On $\mathbb{Z}_{\ge1}^2$, up-right paths enter from the left edge of every row and the bottom of every column. At a vertex with incoming edges $(i_1,j_1)$ (bottom, left) and outgoing $(i_2,j_2)$ (top, right), $i,j\in\{0,1\}$, weights are stochastic: given inputs, the outputs are chosen with probability
$$
\mathsf{P}\big[(0,1)\to(0,1)\big]=b_1,\quad \mathsf{P}\big[(0,1)\to(1,0)\big]=1-b_1,
$$
$$
\mathsf{P}\big[(1,0)\to(1,0)\big]=b_2,\quad \mathsf{P}\big[(1,0)\to(0,1)\big]=1-b_2,
$$
with conservation forcing $(1,1)\to(1,1)$ and $(0,0)\to(0,0)$. In the inhomogeneous version, $b_1,b_2$ at the vertex in column $x$, row $y$ are rational in a spectral pair $(x_x,y_y)$ and $q$:
$$
b_1=\frac{1-x_xy_y}{1-qx_xy_y},\qquad b_2=\frac{q(1-x_xy_y)}{1-qx_xy_y}\cdot q^{-1}\ \text{-normalized},\qquad 0<q<1 .
$$

**Colors.** In the colored (higher-rank) model each path entering row $y$ carries a color $c\in\{1,\dots,n\}$; crossings are resolved by the stochastic $R$-matrix of $U_q(\widehat{\mathfrak{sl}}_{n+1})$, which satisfies the Yang–Baxter equation
$$
\check R_{12}(x/y)\,\check R_{23}(x/z)\,\check R_{12}(y/z)=\check R_{23}(y/z)\,\check R_{12}(x/z)\,\check R_{23}(x/y).
$$
The **colored height function** is
$$
\mathfrak h_{\ge c}(x,y)=\\#\{\text{paths of color}\ \ge c\ \text{passing weakly right of column } x \text{ at height } y\}.
$$

**Shift-invariance (Borodin–Gorin–Wheeler form).** Let $(x_1,y_1),\dots,(x_k,y_k)$ satisfy $x_1\le\cdots\le x_k$, $y_1\ge\cdots\ge y_k$, with associated color thresholds $c_1,\dots,c_k$. Then
$$
\big(\mathfrak h_{\ge c_1}(x_1,y_1),\ \mathfrak h_{\ge c_2}(x_2,y_2),\dots\big)\ \overset{d}{=}\ \big(\mathfrak h_{\ge c_1'}(x_1',y_1'),\ \mathfrak h_{\ge c_2}(x_2,y_2),\dots\big),
$$
where the first observation datum is translated by one lattice step and the spectral parameters of the affected row/column are permuted accordingly. Galashin's **flip-invariance** is the companion statement: the joint law is preserved under a $180^\circ$ rotation of a rectangular sub-domain combined with color reversal $c\mapsto n+1-c$.

**Degenerations.** Setting $q\to0$ or taking limits of $b_1,b_2$ yields colored TASEP/ASEP, the multi-species stochastic $q$-Boson, exponential LPP $G(m,n)=\max_{\pi}\sum_{(i,j)\in\pi}w_{ij}$ with $w_{ij}\sim\mathrm{Exp}(1)$, Brownian LPP, the O'Connell–Yor and log-gamma polymers, and the KPZ equation.

## 3. History & State of the Art (SOTA)

- **1992** — Gwa and Spohn introduce the stochastic six-vertex model as a KPZ-class interface model with an integrable (Bethe-solvable) Hamiltonian.
- **2011** — Amir, Angel and Valkó construct the TASEP speed process and prove the first symmetry of this family: the colored TASEP permutation process is equal in law to its inverse.
- **2016** — Borodin, Corwin and Gorin establish Fredholm-determinant formulas and Tracy–Widom fluctuations for the stochastic six-vertex model (Duke Math. J. 165).
- **2019–2022** — Borodin and Wheeler develop the spectral theory of colored stochastic vertex models (Astérisque 437), producing the observable algebra later used for shift-invariance.
- **2019 (preprint) / 2022** — **Borodin, Gorin, Wheeler**, *Shift-invariance for vertex models and polymers*, prove the first family of shift identities via $q$-deformed observables and Yang–Baxter, and conjecture broader flip symmetries.
- **2021** — **Galashin** proves flip- and shift-invariance in full generality for colored stochastic vertex models by a purely combinatorial/Yang–Baxter argument, resolving the BGW conjectures.
- **2021** — Borodin and Bufetov give the Markov-kernel ("color-position symmetry") explanation for ASEP-type systems.
- **2022** — **Dauvergne** proves shift-invariance for exponential LPP, Brownian LPP and the O'Connell–Yor polymer using RSK-type bijections, giving an independent, geometric mechanism.
- **2021–2024** — Zhang applies colored-TASEP shift-invariance to determine finishing-time laws for the oriented swap process; He extends shift invariance to half-space models.

## 4. Partial Results / Verified Cases

| Setting | Status | Source |
|---|---|---|
| Colored stochastic six-vertex model, arbitrary $n$ colors, inhomogeneous spectral parameters | **Proved** (flip + shift) | Galashin 2021 |
| Rank-1 six-vertex, $q$-Hahn, and polymer degenerations, $k$-point down-right families | **Proved** | Borodin–Gorin–Wheeler 2022 |
| Exponential LPP, geometric LPP, Brownian LPP, O'Connell–Yor polymer | **Proved** via RSK | Dauvergne 2022 |
| Colored TASEP/ASEP, $\eta_t\overset d=\eta_t^{-1}$ | **Proved** | Amir–Angel–Valkó 2011; Borodin–Bufetov 2021 |
| Oriented swap process on $n$ particles: joint law of finishing times $T_1,\dots,T_n$ | **Proved** ($n$ arbitrary) | Zhang 2021 |
| Half-space six-vertex and half-space LPP | **Proved** (restricted point configurations) | He 2022 |
| Non-stochastic (generic) six-vertex weights; elliptic/dynamic weights | **Open** | — |
| Directed landscape / Airy sheet, KPZ equation multi-point | **Partial** | Dauvergne 2022 |

Computationally, the identities have been checked exhaustively by transfer-matrix enumeration for domains up to roughly $6\times6$ with $n\le4$ colors, and by Monte Carlo at $10^7$ samples for two- and three-point statistics of exponential LPP.

## 5. Principal Obstacles

- **Yang–Baxter is local; the shift is global.** The $R$-matrix moves one vertex at a time. Turning a sequence of local moves into a shift of an observation point requires a globally consistent "flip" of a rectangular region; there is no general principle guaranteeing that such a chain of moves exists, and Galashin's construction is specific to the stochastic $\mathfrak{sl}_{n+1}$ weights.
- **Observables control moments, not laws.** BGW's route computes $\mathbb{E}\big[\prod_i q^{\,\mathfrak h_i}\big]$-type quantities. Recovering a joint distribution from such $q$-moments needs a moment-problem argument, which fails once weights leave the stochastic (probability-preserving) regime or the state space becomes unbounded.
- **RSK has no six-vertex analogue.** Dauvergne's proof rests on the bijective invariance of RSK/geometric RSK, available for exponential, geometric, Brownian and log-gamma weights. No bijection is known that linearizes the six-vertex dynamics, so the two proofs remain disjoint rather than two views of one mechanism.
- **Loss of positivity off the stochastic point.** For generic six-vertex weights the vertex weights are not probabilities; "distributional identity" must be replaced by an identity of partition-function ratios, and the combinatorial arguments, which use path-counting couplings, break.
- **Continuum limits do not commute with joint convergence.** Passing shift-invariance to the directed landscape requires convergence of $k$-point distributions with $k$ shifted arguments simultaneously; tightness estimates uniform in the shift are not available beyond the cases Dauvergne handles.

## 6. The Gap

Proven: shift- and flip-invariance for *stochastic* colored vertex models built from $U_q(\widehat{\mathfrak{sl}}_{n+1})$ fundamental $R$-matrices, and for the zero- and positive-temperature models reachable by RSK. Conjectured/unproven:

1. **Beyond stochasticity.** Whether the identities are shadows of a symmetry of the general six-vertex partition function (free-fermion point excluded), where no probabilistic interpretation exists.
2. **A conceptual proof.** Both existing proofs are verification-style. Missing is a single structure — a bijection, an intertwiner of Markov kernels, or a symmetric-function identity for colored (nonsymmetric Macdonald / LLT) polynomials — from which all instances follow.
3. **Continuum universality.** Whether shift-invariance is a property of the KPZ fixed point and directed landscape themselves, hence shared by non-integrable models in the class, or an artifact of integrable discretizations.

Crossing the gap means producing an invariance principle at the level of the limiting object, not the lattice model.

## 7. Current Research (as of June 2026)

- **MIT / Columbia (Borodin, Corwin, Aggarwal).** Colored fermionic vertex models and their symmetric-function counterparts (LLT, nonsymmetric Macdonald) as the algebraic home of the identities.
- **UCLA / Michigan (Galashin, Pylyavskyy).** Combinatorial extensions to higher-spin and to affine-crystal-based vertex models; cyclic symmetries of the colored height function.
- **Columbia / Waterloo (Dauvergne, Virág).** Invariance for the directed landscape and the Airy sheet, via RSK-stable couplings of Brownian LPP. *(frontier — verify)*
- **Stanford / Ohio State (He).** Half-space integrable models, Pfaffian analogues of shift-invariance and their Schur-process interpretation.
- **Bonn / Wisconsin (Bufetov, Korotkikh, Seppäläinen).** Local relations for observables of colored models; shift-invariance for the Beta random walk in random environment and stationary polymers. *(frontier — verify)*
- Reported but unconfirmed: an extension of flip-invariance to the elliptic (dynamic) stochastic six-vertex model. *(frontier — verify)*

## 8. Future Work

- Identify a **coupling** realizing shift-invariance: a measure-preserving map between the two vertex-model configurations, in the spirit of RSK, rather than an equality of computed distributions.
- Determine whether shift-invariance **characterizes integrability** — i.e. whether a stochastic vertex model whose height function satisfies the identities must satisfy Yang–Baxter.
- Prove multi-point shift-invariance for the **KPZ equation** and the continuum directed polymer at all temperatures, and for the **directed landscape** with $k\ge3$ shifted points.
- Extend to **half-space and cylindrical geometries** with general boundary parameters, where Pfaffian rather than determinantal structure governs.
- Use shift-invariance as an input for **stationary-measure and mixing-time** results in multi-species systems, following the oriented-swap-process application.

## 9. Key References

- **[Foundational]** L.-H. Gwa, H. Spohn. *Six-vertex model, roughened surfaces, and an asymmetric spin Hamiltonian.* Physical Review Letters 68 (1992), 725–728.
- **[Foundational]** A. Borodin, I. Corwin, V. Gorin. *Stochastic six-vertex model.* Duke Mathematical Journal 165 (2016), 563–624.
- **[Foundational]** G. Amir, O. Angel, B. Valkó. *The TASEP speed process.* Annals of Probability 39 (2011), 1205–1242.
- **[SOTA]** A. Borodin, V. Gorin, M. Wheeler. *Shift-invariance for vertex models and polymers.* Proceedings of the London Mathematical Society 124 (2022), 182–299.
- **[SOTA]** P. Galashin. *Symmetries of stochastic colored vertex models.* Annals of Probability 49 (2021), 2175–2219.
- **[SOTA]** D. Dauvergne. *Hidden invariance of last passage percolation and directed polymers.* Annals of Probability 50 (2022), 18–60.
- **[SOTA]** A. Borodin, A. Bufetov. *Color-position symmetry in interacting particle systems.* Annals of Probability 49 (2021), 1607–1632.
- **[SOTA]** A. Bufetov, S. Korotkikh. *Observables of stochastic colored vertex models and local relation.* Communications in Mathematical Physics 386 (2021), 1881–1936.
- **[SOTA]** A. Bufetov, V. Gorin, D. Romik. *Absorbing time asymptotics in the oriented swap process.* Annals of Applied Probability 32 (2022), 753–763.
- **[Recent]** L. Zhang. *Shift-invariance of the colored TASEP and finishing times of the oriented swap process.* arXiv:2107.03874, 2021.
- **[Recent]** J. He. *Shift invariance of half space integrable models.* arXiv:2205.13029, 2022.
- **[Survey]** A. Borodin, M. Wheeler. *Colored stochastic vertex models and their spectral theory.* Astérisque 437, Société Mathématique de France, 2022.
- **[Survey]** I. Corwin. *The Kardar–Parisi–Zhang equation and universality class.* Random Matrices: Theory and Applications 1 (2012), 1130001.

## 10. Worked Example / Concrete Special Case

**Colored TASEP on three sites (oriented swap process, $n=3$): verifying $\eta_t \overset{d}{=} \eta_t^{-1}$.**

Particles labelled $1,2,3$ occupy sites $1,2,3$; the state is the word $\eta_t=\eta_t(1)\eta_t(2)\eta_t(3)$, starting at $123$. Each bond $\{i,i+1\}$ rings at rate $1$; on ringing, the two labels swap **only if** the left label is smaller (sorting toward $321$). The chain:
$$
123\xrightarrow{\ 1\ }213,\quad 123\xrightarrow{\ 1\ }132,\quad 213\xrightarrow{\ 1\ }231,\quad 132\xrightarrow{\ 1\ }312,\quad 231\xrightarrow{\ 1\ }321,\quad 312\xrightarrow{\ 1\ }321 .
$$
State $123$ has total exit rate $2$; states $213,132,231,312$ have exit rate $1$; $321$ is absorbing. Solving the forward equations:
$$
\mathbb{P}[\eta_t=123]=e^{-2t},
$$
$$
\mathbb{P}[\eta_t=213]=\mathbb{P}[\eta_t=132]=\int_0^t e^{-2s}e^{-(t-s)}\,ds=e^{-t}-e^{-2t},
$$
$$
\mathbb{P}[\eta_t=231]=\mathbb{P}[\eta_t=312]=\int_0^t\!\big(e^{-s}-e^{-2s}\big)e^{-(t-s)}ds=te^{-t}-e^{-t}+e^{-2t},
$$
and $\mathbb{P}[\eta_t=321]=1-e^{-2t}-2(e^{-t}-e^{-2t})-2(te^{-t}-e^{-t}+e^{-2t})=1-2te^{-t}-e^{-2t}$.

Now invert. In one-line notation, $123^{-1}=123$, $213^{-1}=213$, $132^{-1}=132$, $321^{-1}=321$ (all involutions), while the two $3$-cycles are mutually inverse: $231^{-1}=312$. The symmetry $\eta_t\overset{d}{=}\eta_t^{-1}$ therefore reduces to the single nontrivial identity
$$
\mathbb{P}[\eta_t=231]=\mathbb{P}[\eta_t=312]=te^{-t}-e^{-t}+e^{-2t},
$$
which the computation confirms for every $t>0$. Note this is *not* forced by any left-right reflection: reflection maps $231\mapsto132$, and $\mathbb{P}[\eta_t=132]=e^{-t}-e^{-2t}\neq \mathbb{P}[\eta_t=231]$. The equality of the two $3$-cycle probabilities is the $n=3$ shadow of color-position symmetry, the simplest member of the shift-invariance family; for general $n$ it is Theorem 1 of Amir–Angel–Valkó (2011) and Borodin–Bufetov (2021), and its multi-point refinement is exactly what Galashin's flip-invariance supplies.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*