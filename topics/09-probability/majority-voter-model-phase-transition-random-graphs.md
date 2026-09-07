---
id: 09-probability/majority-voter-model-phase-transition-random-graphs
title: "Phase Transition in the Majority Voter Model on Random Graphs"
topic: 09-probability
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Phase Transition in the Majority Voter Model on Random Graphs

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/majority-voter-model-phase-transition-random-graphs` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

The majority-vote model (MVM) is a non-equilibrium interacting particle system: each vertex of a graph holds a spin $\sigma_i \in \{-1,+1\}$ and flips at a rate that agrees with its local majority with probability $1-q$ and disagrees with probability $q$ (the *noise*). On $\mathbb{Z}^2$ it is known numerically to have an Ising-like order–disorder transition at $q_c \approx 0.075$ (de Oliveira 1992). On sparse random graphs the transition is seen in every simulation and predicted by mean-field/heterogeneous-pair approximations, but is **not proved**.

**Conjecture A (sharp noise threshold).** Fix $d \ge 3$ and let $G_n$ be a random $d$-regular graph on $n$ vertices (or the configuration model with degree distribution of mean $d$ and finite second moment). There is $q_c(d) \in (0,\tfrac12)$ such that the stationary magnetization $m_n(q) = \lim_{t\to\infty}\mathbb{E}\big|n^{-1}\sum_i \sigma_i(t)\big|$ satisfies
$$\lim_{n\to\infty} m_n(q) > 0 \ \text{ for } q<q_c(d), \qquad \lim_{n\to\infty} m_n(q)=0 \ \text{ for } q>q_c(d),$$
and $q_c(d)$ is the value predicted by the tree recursion of §2. A complete solution proves existence of the limit, proves sharpness, and identifies $q_c(d)$.

**Conjecture B (mean-field universality).** At $q \uparrow q_c(d)$, $m(q) \asymp (q_c-q)^{1/2}$, the susceptibility diverges with exponent $\gamma=1$, and the finite-size scaling window has width $n^{-1/2}$ — the Curie–Weiss exponents — for every fixed $d\ge3$ with finite-variance degrees.

**Conjecture C (large-degree asymptotics).** $q_c(d) = \tfrac12 - \sqrt{\pi/(8d)} + o(d^{-1/2})$ as $d\to\infty$.

**Conjecture D (zero-noise consensus threshold).** For $q=0$ deterministic synchronous majority dynamics on $G(n,p)$ from i.i.d. uniform initial opinions, unanimity holds with high probability iff $p \gg n^{-1/2}$; below that scale the number of distinct absorbing configurations grows polynomially.

## 2. Mathematical Foundations

**Dynamics.** Let $G=(V,E)$, $\sigma \in \{-1,+1\}^V$, and $S_i(\sigma) = \sum_{j\sim i}\sigma_j$. The MVM is the continuous-time Markov chain with generator
$$(\mathcal{L}f)(\sigma) = \sum_{i\in V} w_i(\sigma)\,\big[f(\sigma^i)-f(\sigma)\big], \qquad w_i(\sigma) = \frac12\Big[1-(1-2q)\,\sigma_i\,\mathrm{sgn}\big(S_i(\sigma)\big)\Big],$$
where $\sigma^i$ flips coordinate $i$ and $\mathrm{sgn}(0)=0$ (ties are resolved by an unbiased coin). For $q=0$ this is deterministic-in-the-limit *majority dynamics*; for $q=\tfrac12$ it is the trivial i.i.d. flip process. Unlike Glauber dynamics for the Ising model, $w_i$ is **not** of the form $\big(1+e^{2\beta\sigma_iS_i}\big)^{-1}$: it depends on $S_i$ only through its sign, so the chain violates detailed balance and has **no reversible Gibbs measure** for $0<q<\tfrac12$.

**Order parameter.** $M_n = n^{-1}\sum_i \sigma_i$, $m = \lim_n \mathbb{E}|M_n|$ in the stationary law $\mu_n$ (which is unique for $q>0$ on a finite graph, so $m$ is well defined for each $n$).

**Tree recursion.** The configuration model converges locally to a Galton–Watson tree with root degree $D$ and offspring the size-biased law $\hat D$. Assuming (unproved) asymptotic independence of the neighbour spins in the stationary state, a root with $k$ neighbours each $+1$ with probability $p=(1+m)/2$ satisfies the self-consistency equation
$$m = (1-2q)\,\mathbb{E}\big[\,\mathrm{sgn}(S_D)\,\big] =: (1-2q)\,F_D(m),$$
$$F_k(m) = \sum_{j>k/2}\binom{k}{j}\big(p^j(1-p)^{k-j}-p^{k-j}(1-p)^{j}\big) + \mathbf{1}_{\{k \text{ even}\}}\cdot 0 .$$
$F_k$ is odd, increasing, concave on $[0,1]$ for $k\ge3$, so $m=0$ loses stability exactly when $(1-2q)F_k'(0)=1$:
$$\boxed{\;q_c(k) = \frac12\Big(1-\frac{1}{F_k'(0)}\Big),\qquad F_k'(0)=k\binom{k-1}{\lfloor (k-1)/2\rfloor}2^{-(k-1)}.\;}$$
For $k=3$: $F_3'(0)=3/2$, $q_c=1/6$. For $k=5$: $F_5'(0)=15/8$, $q_c=7/30\approx0.2333$. Stirling gives $F_k'(0)\sim\sqrt{2k/\pi}$, hence Conjecture C.

**Zero-noise structure.** Synchronous majority dynamics $\sigma_i(t+1)=\mathrm{sgn}(S_i(\sigma(t)))$ is a threshold automaton; by Goles–Olivos (1980) every orbit is eventually periodic with period $1$ or $2$. The energy $\Phi(\sigma,\tau)=-\sum_{ij\in E}\sigma_i\tau_j$ is a Lyapunov function for the two-step map, which is the only general convergence tool available.

## 3. History & State of the Art (SOTA)

- **1973–75.** The linear voter model is introduced by Clifford–Sudbury (spatial conflict) and analysed by Holley–Liggett via duality with coalescing random walks: clustering in $d\le2$, coexistence in $d\ge3$. The *majority* rule destroys the duality and the linearity of the generator.
- **1992.** M. J. de Oliveira defines the isotropic MVM on $\mathbb{Z}^2$, measures $q_c=0.075(1)$ and exponents $\beta/\nu=0.125$, $\gamma/\nu=1.75$, concluding Ising universality despite the absence of detailed balance.
- **2003–08.** Small-world and network versions: Campos–de Oliveira–Moreira (Watts–Strogatz), Pereira–Moreira (Erdős–Rényi, $q_c$ increasing in mean degree, mean-field exponents), Lima (directed Barabási–Albert). All numerical.
- **2010–13.** Dembo–Montanari and Dembo–Montanari–Sun prove local weak convergence of the *Ising* measure on locally tree-like graphs and identify $\beta_c=\mathrm{atanh}\,1/(d-1)$. Their method is Gibbsian and does not transfer to MVM.
- **2016–2023.** Rigorous progress at $q=0$. Benjamini–Chan–O'Donnell–Tamuz–Tan prove convergence to period $\le2$ on unimodular graphs and conjecture unanimity on $G(n,1/2)$; Fountoulakis–Kang–Makai prove it, with stabilization in $4$ rounds; Berkowitz–Devlin prove a CLT for the round-one bias ("bribing three voters suffices"); Tran–Vu and Chakraborti–Kim–Lee–Tran push unanimity down to $p\ge \lambda n^{-1/2}$.

**SOTA summary:** the $q=0$ dense/moderately sparse regime is a theorem; the $q>0$ transition on random graphs is empirically supported only.

## 4. Partial Results / Verified Cases

- **Complete graph / Curie–Weiss ($d=n-1$).** Rigorous: $M_n$ is a birth–death chain, $m$ solves $m=(1-2q)\mathrm{erf}$-type equation, transition at $q_c\to\tfrac12$ with $\beta=1/2$. All of Conjectures A–C hold in the mean-field limit.
- **$q=0$, dense graphs.** $G(n,p)$ with $p$ constant: unanimity w.h.p., reached in at most $4$ rounds (Fountoulakis–Kang–Makai 2020).
- **$q=0$, sparse-ish graphs.** $p \ge \lambda n^{-1/2}$ for large constant $\lambda$: unanimity w.h.p. (Chakraborti–Kim–Lee–Tran 2023). With an initial bias of $\Theta(\sqrt{n})$ voters the winning side is determined w.h.p. (Tran–Vu 2020; Berkowitz–Devlin 2022).
- **Expanders.** On graphs with spectral gap bounded away from $0$ and minimum degree $\Omega(\log n)$, an initial bias $cn$ spreads to unanimity in $O(\log\log n)$ rounds (Zehmakan 2020).
- **Structure of orbits.** Period $\le 2$ for synchronous dynamics on any finite graph (Goles–Olivos 1980); a.s. convergence on unimodular random graphs (Benjamini et al. 2016).
- **Lattices, numerically.** $\mathbb{Z}^2$: $q_c=0.075$; $\mathbb{Z}^3$: $q_c\approx0.177$; random graphs: $q_c(\langle k\rangle=4)\approx0.20$, $q_c(\langle k\rangle=10)\approx0.32$ (Pereira–Moreira 2005), all consistent with the recursion of §2 to within a few percent.

## 5. Principal Obstacles

- **No Gibbs measure.** The stationary law of MVM is not the Boltzmann measure of any local Hamiltonian. Every rigorous tool for the sparse Ising transition — Bethe recursions, interpolation/Guerra bounds, the Dembo–Montanari–Sun factor-model machinery, correlation inequalities (GKS, FKG, GHS) — assumes reversibility or monotone Gibbs structure and is unavailable.
- **No duality, no linearity.** The linear voter model is solvable through coalescing-random-walk duality; $\mathrm{sgn}(\cdot)$ is nonlinear, and no dual process is known.
- **Loss of attractiveness at ties.** The MVM *is* monotone (attractive) in $\sigma$, so coupling gives existence of extremal stationary measures on infinite graphs; but on a random graph the extremal measures need not be distinguishable by $m$, and monotonicity alone gives no sharpness of the threshold in $q$.
- **Local weak convergence does not imply stationary-measure convergence.** Benjamini–Schramm convergence of $G_n$ to a Galton–Watson tree controls local statistics of *fixed-time* dynamics, but the $t\to\infty$ and $n\to\infty$ limits do not commute: on a finite graph the chain is ergodic and $\mathbb{E}M_n=0$ by symmetry, so the order parameter must be extracted from a metastability/timescale separation argument (relaxation time $e^{cn}$ vs. $\mathrm{poly}(n)$) that is unproven for $d<\infty$.
- **Independence assumption is false.** The recursion in §2 assumes stationary neighbour spins are independent. On a tree of degree $3$ they are provably correlated; the true $q_c(3)$ is expected to differ from $1/6$ by a few percent, and no controlled expansion around the tree approximation exists.
- **Cycles.** Sparse random graphs have $\Theta(1)$ short cycles; recursive tree arguments must absorb them, which is exactly where Ising proofs use the Gibbs property.

## 6. The Gap

Proven: (i) the $q=0$ deterministic problem down to $p \sim n^{-1/2}$; (ii) the $d=\infty$ (Curie–Weiss) transition; (iii) qualitative convergence theorems. Conjectured: everything at $0<q<\tfrac12$ with $d$ fixed.

The precise missing step is a **timescale-separation theorem**: show that for $q<q_c(d)$ the MVM on a random $d$-regular graph started from all-$+$ has $\mathbb{P}\big(M_n(t)>\varepsilon\big)\to1$ for all $t \le e^{cn}$, i.e. an exponential-in-$n$ lower bound on the tunnelling time between the two ordered phases, together with a matching disordered-phase mixing bound $t_{\mathrm{mix}}=O(n\log n)$ for $q>q_c(d)$. For reversible dynamics this is done by bounding the Cheeger constant of the stationary measure; without reversibility one needs either (a) an isoperimetric bound on a non-Gibbsian stationary measure, or (b) a genuinely dynamic contour/percolation argument on the random graph. Neither exists.

## 7. Current Research (as of June 2026)

- **Sparse-regime majority dynamics.** Follow-ups to Chakraborti–Kim–Lee–Tran on lowering the unanimity threshold from $\lambda n^{-1/2}$ toward $n^{-1/2}$ and on the structure of absorbing states for $p = c/n$ (Korea/IBS discrete mathematics group; Vu's group at Yale). *(frontier — verify)*
- **Non-reversible metastability.** Adaptation of potential-theoretic metastability (Bovier–den Hollander) and of Landim's martingale approach to non-reversible mean-field-like chains, applied to majority-type flip rates on the configuration model. *(frontier — verify)*
- **Hydrodynamic/kinetic limits on graphons.** Dense-graph limits where the MVM's mean-field ODE $\dot m = -m + (1-2q)F(m)$ is derived rigorously; sparse extensions remain open.
- **Statistical-physics refinements.** Heterogeneous pair approximation and cluster-variational methods giving $q_c$ estimates on scale-free and modular graphs; degree-heterogeneous MVM where $q_c\to 1/2$ when $\mathbb{E}[D^2]=\infty$.
- **Algorithmic/social-choice side.** Sample complexity of "power of few" bribing results and their extension to noisy dynamics; connections to community detection where majority dynamics is used as a cheap label-propagation primitive.

## 8. Future Work

1. Prove existence of the $n\to\infty$ limit of $m_n(q)$ for random $d$-regular graphs via local weak convergence of the *stationary* measure — the key missing lemma.
2. Establish a non-reversible Cheeger/mixing dichotomy: $t_{\mathrm{mix}} = e^{\Theta(n)}$ below $q_c$ and $O(n\log n)$ above.
3. Prove that the ordered phase is nonempty for small $q$ on the $d$-regular tree, and that stationary boundary conditions propagate (a non-Gibbsian analogue of Kesten–Stigum / reconstruction).
4. Determine the exact $q_c(3)$ beyond the tree approximation, or prove that $q_c(d)>0$ for all $d\ge3$ — even the qualitative statement is open.
5. Settle Conjecture C rigorously at least for the configuration model with $d\to\infty$ slowly (e.g. $d=\log n$), where concentration is strong enough to mimic Curie–Weiss.
6. Close the $q=0$ gap between $p\gg n^{-1/2}$ (unanimity) and $p = \Theta(1/n)$ (fragmentation).

## 9. Key References

- **[Foundational]** P. Clifford and A. Sudbury. *A model for spatial conflict.* Biometrika 60(3):581–588, 1973.
- **[Foundational]** R. Holley and T. M. Liggett. *Ergodic theorems for weakly interacting infinite systems and the voter model.* Annals of Probability 3(4):643–663, 1975.
- **[Foundational]** T. M. Liggett. *Interacting Particle Systems.* Springer, 1985.
- **[Foundational]** E. Goles and J. Olivos. *Periodic behaviour of generalized threshold functions.* Discrete Mathematics 30(2):187–189, 1980.
- **[Foundational]** M. J. de Oliveira. *Isotropic majority-vote model on a square lattice.* Journal of Statistical Physics 66(1–2):273–281, 1992.
- **[Numerical]** P. R. A. Campos, V. M. de Oliveira, F. G. B. Moreira. *Small-world effects in the majority-vote model.* Physical Review E 67:026104, 2003.
- **[Numerical]** L. F. C. Pereira and F. G. B. Moreira. *Majority-vote model on random graphs.* Physical Review E 71:016123, 2005.
- **[Numerical]** F. W. S. Lima. *Majority-vote on directed Barabási–Albert networks.* International Journal of Modern Physics C 17(9):1257–1265, 2006.
- **[SOTA / Recent]** I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan. *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs.* Stochastic Processes and their Applications 126(9):2719–2733, 2016.
- **[SOTA / Recent]** N. Fountoulakis, M. Kang, T. Makai. *Resolution of a conjecture on majority dynamics: rapid stabilization in dense random graphs.* Random Structures & Algorithms 57(4):1134–1156, 2020.
- **[SOTA / Recent]** L. Tran and V. Vu. *Reaching a consensus on random networks: the power of few.* APPROX/RANDOM 2020, LIPIcs vol. 176, art. 20.
- **[SOTA / Recent]** R. Berkowitz and P. Devlin. *Central limit theorem for majority dynamics: bribing three voters suffices.* Stochastic Processes and their Applications 146:187–206, 2022.
- **[SOTA / Recent]** D. Chakraborti, J. H. Kim, J. Lee, T. Tran. *Majority dynamics on sparse random graphs.* Random Structures & Algorithms 63(1):171–191, 2023.
- **[SOTA / Recent]** A. N. Zehmakan. *Opinion forming in Erdős–Rényi random graph and expanders.* Discrete Applied Mathematics 277:280–290, 2020.
- **[Comparison]** A. Dembo and A. Montanari. *Ising models on locally tree-like graphs.* Annals of Applied Probability 20(2):565–592, 2010.
- **[Comparison]** A. Dembo, A. Montanari, N. Sun. *Factor models on locally tree-like graphs.* Annals of Probability 41(6):4162–4213, 2013.
- **[Survey]** C. Castellano, S. Fortunato, V. Loreto. *Statistical physics of social dynamics.* Reviews of Modern Physics 81(2):591–646, 2009.
- **[Survey]** E. Mossel, J. Neeman, O. Tamuz. *Majority dynamics and aggregation of information in social networks.* Autonomous Agents and Multi-Agent Systems 28(3):408–429, 2014.

## 10. Worked Example / Concrete Special Case

**Random $3$-regular graph, mean-field computation of $q_c(3)$ and $\beta$.**

Take $D\equiv3$ and assume stationary neighbour spins i.i.d. with $\mathbb{P}(+1)=p=(1+m)/2$. The local majority of three spins is $+1$ with probability $p^3+3p^2(1-p)=3p^2-2p^3$, so
$$F_3(m)=2(3p^2-2p^3)-1 = 6p^2-4p^3-1.$$
Substituting $p=(1+m)/2$: $6p^2 = \tfrac32 + 3m + \tfrac32 m^2$ and $4p^3 = \tfrac12 + \tfrac32 m + \tfrac32 m^2 + \tfrac12 m^3$, hence
$$F_3(m) = \tfrac32 m - \tfrac12 m^3 .$$
The self-consistency equation $m=(1-2q)F_3(m)$ becomes
$$m = (1-2q)\Big(\tfrac32 m - \tfrac12 m^3\Big).$$
The trivial root $m=0$ always exists. Its stability changes when $(1-2q)\cdot\tfrac32 = 1$, i.e.
$$1-2q_c = \tfrac23 \quad\Longrightarrow\quad q_c(3) = \tfrac16 \approx 0.1667 .$$
For $q<1/6$, dividing by $m$ gives the ordered root
$$m^2 = 3 - \frac{2}{1-2q}.$$
Write $q = \tfrac16-\varepsilon$, so $1-2q = \tfrac23+2\varepsilon$ and $\dfrac{2}{1-2q} = \dfrac{3}{1+3\varepsilon} = 3-9\varepsilon+O(\varepsilon^2)$. Therefore
$$m^2 = 9\varepsilon + O(\varepsilon^2), \qquad m \simeq 3\,(q_c-q)^{1/2},$$
exhibiting the mean-field exponent $\beta=1/2$ of Conjecture B with an explicit amplitude. Sanity checks: at $q=0$, $m^2 = 3-2 = 1$, so $m=1$ (perfect order, consistent with unanimity being absorbing); at $q=1/8$, $m^2=3-2/0.75=1/3$, $m\approx0.577$.

The same computation for $k=5$ gives $F_5'(0)=15/8$ and $q_c(5)=7/30\approx0.2333$; for $k=9$, $F_9'(0)=9\binom{8}{4}/2^8=630/256\approx2.461$, $q_c\approx0.2968$; the large-$k$ asymptotic $q_c\approx\tfrac12-\sqrt{\pi/(8k)}$ evaluated at $k=9$ gives $0.5-0.209=0.291$, within $2\%$.

**What is unproved here.** Every step above uses the independence of the three neighbour spins in the stationary state. On a random $3$-regular graph that is false at any finite $n$, and no error bound on the resulting $q_c$ is known — this single assumption is the whole gap between the numerics and a theorem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*