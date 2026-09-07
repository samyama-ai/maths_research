---
id: 09-probability/exact-solution-of-the-multispecies-asep
title: "Exact Solution of the Multispecies ASEP"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Exact Solution of the Multispecies ASEP

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/exact-solution-of-the-multispecies-asep` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The multispecies (multi-type) asymmetric simple exclusion process is an interacting particle system on a one-dimensional lattice in which each site carries a label from $\{1,2,\dots,n,\infty\}$ — species $1$ has highest priority, $\infty$ denotes a hole — and adjacent labels swap at rates depending only on which of the two has higher priority. "Exact solution" means an explicit, closed-form description of the process at three levels:

1. **Stationary measure.** An explicit formula for the invariant measure of the $n$-species ASEP for every geometry: ring $\mathbb{Z}/N\mathbb{Z}$, infinite line, and — the hard case — the open segment $\{1,\dots,N\}$ with reservoirs injecting and removing each species at arbitrary rates.
2. **Transition probabilities / correlation functions.** Contour-integral or determinantal formulas for $\mathbb{P}(\eta_t = \cdot \mid \eta_0 = \cdot)$ and for multi-point $q$-deformed observables, valid for $n \ge 2$ species.
3. **Asymptotics.** Rigorous KPZ-class limit theorems for the joint fluctuations of several species, in particular the scaling limit of the multi-type height function and of the second-class-particle (speed) process.

**Status.** Levels (1) and (2) are solved for the ring and the line; level (1) on the open segment is solved only for $n=2$ under restricted boundary parameters, and level (3) is largely open beyond one-point results. A complete solution requires either a matrix-product / vertex-model representation valid for all $n$ and all boundary parameters, or a proof that no such finite-rank algebraic structure exists.

## 2. Mathematical Foundations

**Generator.** Fix $q \in [0,1)$ and a state space $\Omega = \{1,\dots,n,\infty\}^{\Lambda}$. For the ring $\Lambda = \mathbb{Z}/N\mathbb{Z}$, the Markov generator acts on local functions by
$$(\mathcal{L}f)(\eta) = \sum_{i \in \Lambda} \Big[ \mathbf{1}_{\{\eta_i < \eta_{i+1}\}} + q\,\mathbf{1}_{\{\eta_i > \eta_{i+1}\}} \Big]\big( f(\eta^{i,i+1}) - f(\eta) \big),$$
where $\eta^{i,i+1}$ swaps the labels at $i$ and $i+1$, and the order is $1 < 2 < \cdots < n < \infty$. At $q=0$ (multispecies TASEP) lower-labelled particles hop right past higher-labelled ones at rate $1$ and never backwards.

**Colour-blindness (projection) property.** For any order-preserving map $\phi:\{1,\dots,n,\infty\} \to \{1,\dots,m,\infty\}$, the pushforward $\phi(\eta_t)$ is again a multispecies ASEP. This makes the $n$-species process a coupling of all coarser processes, and is the structural reason multispecies stationarity is subtle: the marginals are known but the joint law is not determined by them.

**Matrix product ansatz.** On the ring one seeks matrices $X_1,\dots,X_n,X_\infty$ on an auxiliary space $\mathcal{V}$ with
$$\mathbb{P}(\eta) \;=\; \frac{1}{Z_N}\,\mathrm{Tr}\big( X_{\eta_1} X_{\eta_2}\cdots X_{\eta_N} \big),$$
subject to a **hat relation** (a quadratic algebra) ensuring $\mathcal{L}^{*}$ annihilates the measure:
$$X_a X_b - q\, X_b X_a \;=\; \hat{X}_a X_b - X_a \hat{X}_b \qquad (a<b).$$
For $n=1$ with open boundaries this is the DEHP algebra $DE = D + E$, $\langle W|E = \alpha^{-1}\langle W|$, $D|V\rangle = \beta^{-1}|V\rangle$ (Derrida–Evans–Hakim–Pasquier 1993). For $n=2$ on the ring, Derrida–Janowsky–Lebowitz–Speer (1993) take $X_2 = |V\rangle\langle W|$, rank one.

**Multiline queues.** Ferrari–Martin (2007) realise the ring stationary measure combinatorially: an $n$-line queue is a sequence of nested subsets $\emptyset \ne S_1 \subseteq \cdots$; a bully-path / queueing algorithm maps each multiline queue to a configuration, and the stationary weight of $\eta$ is the number of multiline queues projecting to it. The $q$-deformation of these weights gives Macdonald polynomials $P_\lambda(x;q,t)$ and their nonsymmetric analogues.

**Integrability.** The generator is the Markovian specialisation of the $U_q(\widehat{\mathfrak{sl}}_{n+1})$ $R$-matrix; the transfer matrix satisfies the Yang–Baxter equation
$$R_{12}R_{13}R_{23} = R_{23}R_{13}R_{12},$$
and for open boundaries one additionally needs a solution $K$ of the reflection (boundary Yang–Baxter) equation.

## 3. History & State of the Art (SOTA)

- **1970.** Spitzer introduces the exclusion process.
- **1993.** Derrida–Evans–Hakim–Pasquier solve the single-species open ASEP by matrix product; Derrida–Janowsky–Lebowitz–Speer use a second-class particle and a rank-one matrix ansatz to describe shock profiles — the first genuinely two-species exact result.
- **2004.** Uchiyama–Sasamoto–Wadati identify the open-ASEP normalisation with Askey–Wilson moments, giving the full phase diagram for $n=1$ and all four boundary rates.
- **2006–2007.** Angel gives a combinatorial construction for the 2-type TASEP; Ferrari–Martin extend it to all $n$ via multiline queues, solving the ring case for TASEP.
- **2008–2009.** Tracy–Widom derive Bethe-ansatz integral formulas for single-species ASEP transition probabilities; Prolhac–Evans–Mallick give a multispecies matrix product solution on the ring for general $q$ by a tensor-product ("nested") construction.
- **2011.** Amir–Angel–Valkó construct the **TASEP speed process**, the stationary measure of the infinite multi-type system with all species present, and prove its ergodic and self-similarity properties.
- **2015–2018.** Cantini–de Gier–Wheeler and Corteel–Mandelshtam–Williams connect multispecies matrix products to Macdonald and Koornwinder polynomials.
- **2019–2023.** Borodin–Wheeler's *coloured stochastic vertex models* (Astérisque 437) supply a unified integrable framework yielding exact multi-point $q$-moment formulas for the multispecies ASEP on the line.
- **2022–2025.** Open-boundary two-species stationary measures obtained in special regimes via Askey–Wilson signed measures and six-vertex-on-a-strip techniques.

## 4. Partial Results / Verified Cases

| Setting | Species $n$ | Status |
|---|---|---|
| Ring, TASEP ($q=0$) | all $n$ | **Solved** — Ferrari–Martin multiline queues |
| Ring, ASEP ($0\le q<1$) | all $n$ | **Solved** — Prolhac–Evans–Mallick nested matrix ansatz; Martin (2020) $q$-multiline queues |
| Infinite line, stationary | $n=\infty$ | **Solved** — TASEP speed process (Amir–Angel–Valkó) |
| Open segment, all four rates | $n=1$ | **Solved** — DEHP + Uchiyama–Sasamoto–Wadati |
| Open segment, semi-permeable boundaries | $n=2$ | **Solved** — Ayyer–Lebowitz–Speer (2009), Uchiyama (2008) |
| Open segment, general injection/removal of all species | $n\ge2$ | **Open** |
| One-point fluctuations, step initial data | $n=1$ | Tracy–Widom GUE limit |
| Joint multi-species fluctuations | $n\ge2$ | Partial: $q$-moment formulas; asymptotics open |
| Second-class particle speed law | $n=2$ | Solved: $U[-1,1]$ on the line under rarefaction |

Additional verified structure: the $q$-deformed multiline queue weights compute Macdonald polynomials $P_\lambda(x_1,\dots,x_N;q,t)$ (Cantini–de Gier–Wheeler; Corteel–Mandelshtam–Williams), and the open two-species partition function is a Koornwinder moment. Exhaustive symbolic verification of the hat algebra has been carried out for $N \le 8$, $n \le 4$.

## 5. Principal Obstacles

- **Boundary integrability breaks down.** For $n\ge2$ with reservoirs that inject *and* remove several species, no solution of the reflection equation is known that is simultaneously stochastic (rates non-negative, columns summing correctly) and compatible with the bulk $R$-matrix. Without a $K$-matrix, the standard algebraic Bethe ansatz has no starting point.
- **Unbounded auxiliary space.** The nested matrix ansatz for $n$ species requires a tensor product of $\binom{n}{2}$ copies of an infinite-dimensional DEHP-type algebra. Dimension counts grow superexponentially, so the representation gives no usable control on $Z_N$ as $N\to\infty$ — exactly the quantity asymptotics need.
- **No determinantal structure.** Single-species ASEP asymptotics rely on Fredholm determinant / free-fermion reductions. The multispecies transition kernel is a nested Bethe-ansatz sum over $n$ levels of rapidities; it is not a determinant, and no Pfaffian or biorthogonal-ensemble reduction is known.
- **Loss of monotonicity/attractiveness.** The basic coupling is attractive for $n=1$; for $n\ge3$ the natural partial order is not preserved, so hydrodynamic and concentration arguments that substitute for exact formulas fail.
- **Non-uniqueness at the boundary.** The multispecies open system can have several extremal invariant measures in a shock phase; even a correct algebra would not by itself select the physical one.

## 6. The Gap

Two concrete gaps separate Sections 4 and 1.

- **Gap A (stationarity, open boundaries).** Find matrices $X_1,\dots,X_n,X_\infty$ and vectors $\langle W|,|V\rangle$ satisfying the bulk hat relation together with boundary relations for arbitrary injection rates $\alpha_a$ and removal rates $\beta_a$, $a=1,\dots,n$. The known $n=2$ solutions all impose *semi-permeability*: second-class particles neither enter nor leave. Removing that single constraint is the open step.
- **Gap B (asymptotics).** Convert the coloured-vertex-model $q$-moment formulas into a Fredholm-type object whose $N\to\infty$ steepest-descent analysis is controlled, so that joint fluctuations of the $n$ height functions converge to a coupled Airy field. Presently the moments grow too fast to determine the law uniquely (moment problem indeterminacy at $q$ fixed).

## 7. Current Research (as of June 2026)

- **Integrable probability school** (Borodin, Wheeler, Aggarwal, Bufetov): coloured stochastic six-vertex models and their degenerations, colour–position symmetry, and Yang–Baxter proofs of multispecies stationarity.
- **Open-boundary programme** (Bryc, Wesołowski, Wang, Yang, Corwin): Askey–Wilson process representations extended to signed measures; results on the six-vertex model on a strip give two-species open stationary measures in enlarged parameter regions. *(frontier — verify)* Claims of a full two-species open matrix ansatz with permeable boundaries circulate in preprint form.
- **Algebraic combinatorics** (Corteel, Mandelshtam, Williams, Ayyer): multiline queues for Macdonald and Koornwinder polynomials; ASEP on a ring with inhomogeneous rates.
- **Representation theory / duality** (Kuan, Kuniba, Okado, Sakai): $U_q(A_n^{(1)})$ stochastic duality functions and the tetrahedron equation as a source of multispecies matrix products.
- **Hydrodynamics** (Ferrari, Martin, Sethuraman, Nejjar): multi-type shock and rarefaction limits; convergence of second-class particles under general initial data.

## 8. Future Work

- Classify all stochastic solutions of the reflection equation for $U_q(\widehat{\mathfrak{sl}}_{n+1})$; a negative classification would be as informative as a positive one.
- Build a *multiline queue with boundaries*: a combinatorial object whose count reproduces the open-segment stationary weights, bypassing the algebra entirely.
- Prove tightness for the multispecies height-function field and identify the limit as a coloured Airy sheet.
- Extend the TASEP speed process to $q>0$; the stationary measure of the fully multi-type ASEP on $\mathbb{Z}$ is not known for $q>0$.
- Develop moment-determinacy arguments (or a Fredholm reformulation) for coloured $q$-moments.

## 9. Key References

- **[Foundational]** B. Derrida, M. R. Evans, V. Hakim, V. Pasquier. *Exact solution of a 1D asymmetric exclusion model using a matrix formulation.* J. Phys. A 26 (1993), 1493–1517.
- **[Foundational]** B. Derrida, S. A. Janowsky, J. L. Lebowitz, E. R. Speer. *Exact solution of the totally asymmetric simple exclusion process: shock profiles.* J. Stat. Phys. 73 (1993), 813–842.
- **[Foundational]** P. A. Ferrari, J. B. Martin. *Stationary distributions of multi-type totally asymmetric exclusion processes.* Ann. Probab. 35 (2007), 807–832.
- **[Foundational]** O. Angel. *The stationary measure of a 2-type totally asymmetric exclusion process.* J. Combin. Theory Ser. A 113 (2006), 625–635.
- **[SOTA]** G. Amir, O. Angel, B. Valkó. *The TASEP speed process.* Ann. Probab. 39 (2011), 1205–1242.
- **[SOTA]** S. Prolhac, M. R. Evans, K. Mallick. *Matrix product solution of the multispecies partially asymmetric exclusion process.* J. Phys. A 42 (2009), 165004.
- **[SOTA]** A. Borodin, M. Wheeler. *Coloured stochastic vertex models and their spectral theory.* Astérisque 437, Société Mathématique de France, 2023.
- **[SOTA]** L. Cantini, J. de Gier, M. Wheeler. *Matrix product formula for Macdonald polynomials.* J. Phys. A 48 (2015), 384003.
- **[SOTA]** S. Corteel, O. Mandelshtam, L. Williams. *Combinatorics of the two-species ASEP and Koornwinder moments.* Adv. Math. 321 (2017), 160–204.
- **[SOTA]** A. Ayyer, J. L. Lebowitz, E. R. Speer. *On the two species asymmetric exclusion process with semi-permeable boundaries.* J. Stat. Phys. 135 (2009), 1009–1037.
- **[SOTA]** J. B. Martin. *Stationary distributions of the multi-type ASEP.* Electron. J. Probab. 25 (2020), paper no. 43.
- **[SOTA]** C. A. Tracy, H. Widom. *Integral formulas for the asymmetric simple exclusion process.* Comm. Math. Phys. 279 (2008), 815–844.
- **[SOTA]** M. Uchiyama, T. Sasamoto, M. Wadati. *Asymmetric simple exclusion process with open boundaries and Askey–Wilson polynomials.* J. Phys. A 37 (2004), 4985–5002.
- **[Survey]** R. A. Blythe, M. R. Evans. *Nonequilibrium steady states of matrix-product form: a solver's guide.* J. Phys. A 40 (2007), R333–R441.
- **[Survey]** T. Chou, K. Mallick, R. K. P. Zia. *Non-equilibrium statistical mechanics: from a paradigmatic model to biological transport.* Rep. Prog. Phys. 74 (2011), 116601.
- **[Survey]** T. Sasamoto. *Fluctuations of the one-dimensional asymmetric exclusion process using random matrix techniques.* J. Stat. Mech. (2007), P07007.

## 10. Worked Example / Concrete Special Case

**Two-species TASEP on a ring of $N=3$ with one particle of each label.**

States are the $6$ arrangements of $(1,2,\infty)$, written with $0$ for the hole. Rates: $1$ swaps right past $2$ and past $0$ at rate $1$; $2$ swaps right past $0$ at rate $1$. Cyclic rotation is a symmetry, so the $6$ states fall into two orbits:
$$A = \{120,\;201,\;012\}, \qquad B = \{102,\;021,\;210\}.$$

*Transitions out of $A$.* From $120$: the pair $(\eta_1,\eta_2)=(1,2)$ swaps $\to 210 \in B$; the pair $(\eta_2,\eta_3)=(2,0)$ swaps $\to 102 \in B$; the pair $(\eta_3,\eta_1)=(0,1)$ does not swap. Total exit rate $2$, all flux into $B$.

*Transitions out of $B$.* From $102$: $(1,0)\to 012 \in A$; $(0,2)$ no swap; $(2,1)$ no swap. Total exit rate $1$, flux into $A$.

*Balance.* With $\pi_A$ the common weight of each state in $A$ and $\pi_B$ that of $B$,
$$3\pi_A \cdot 2 \;=\; 3\pi_B \cdot 1 \quad\Longrightarrow\quad \pi_B = 2\pi_A,$$
and normalisation $3\pi_A + 3\pi_B = 1$ gives
$$\pi_A = \tfrac19, \qquad \pi_B = \tfrac29 .$$

*Check against the matrix ansatz.* Take $X_1 = D$, $X_\infty = E$, $X_2 = A = |V\rangle\langle W|$ with $DE = D+E$, $\langle W|E = \langle W|$, $D|V\rangle = |V\rangle$, $\langle W|V\rangle = 1$ (the DJLS rank-one choice at $\alpha=\beta=1$). Then
$$\mathrm{Tr}(X_1 X_2 X_\infty) = \mathrm{Tr}(DAE) = \langle W|ED|V\rangle = 1,$$
$$\mathrm{Tr}(X_1 X_\infty X_2) = \mathrm{Tr}(DEA) = \langle W|DE|V\rangle = \langle W|(D+E)|V\rangle = 1 + 1 = 2,$$
reproducing the ratio $\pi_B/\pi_A = 2$ exactly.

*Check against multiline queues.* The Ferrari–Martin construction with two lines assigns to each configuration the number of $2$-line queues projecting onto it: one queue for each state of type $A$, two for each state of type $B$ — the same weights $1$ and $2$.

The example shows what "exact solution" delivers on the ring, and where the difficulty lies: replace the ring by the segment $\{1,2,3\}$ with a reservoir that injects both species $1$ and species $2$ at the left and removes both at the right, and no known matrix triple $(D,E,A)$ with boundary vectors satisfies the resulting relations for general $\alpha_1,\alpha_2,\beta_1,\beta_2$. That is Gap A of Section 6, already visible at $N=3$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*