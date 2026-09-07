---
id: 10-theoretical-cs/planted-clique-conjecture
title: "Planted Clique Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Planted Clique Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/planted-clique-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Draw an Erdős–Rényi random graph $G(n,1/2)$, choose a uniformly random vertex subset $S$ with $|S| = k$, and add all missing edges inside $S$ so that $S$ becomes a clique. Call the result $G(n,1/2,k)$. Given only the graph, find $S$ (search) or distinguish the planted distribution from $G(n,1/2)$ (detection).

**Planted Clique Conjecture.** For every fixed $\varepsilon > 0$ and $k = k(n)$ with
$$(2+\varepsilon)\log_2 n \;\le\; k \;\le\; n^{1/2-\varepsilon},$$
no randomized algorithm running in time $n^{O(1)}$ recovers $S$ — or even distinguishes $G(n,1/2,k)$ from $G(n,1/2)$ with advantage $\Omega(1)$ — with probability $1-o(1)$ over the input and its own coins.

The lower endpoint is where the planted clique becomes statistically detectable at all: the maximum clique of $G(n,1/2)$ has size $(2+o(1))\log_2 n$ whp. The upper endpoint is where polynomial-time algorithms exist (Section 4). A disproof is an algorithm at some $k = n^{1/2-\varepsilon}$; a proof would have to be conditional (the problem is in $\mathsf{NP}$-search and average-case, so unconditional hardness would imply $\mathsf{P} \neq \mathsf{NP}$ and more), so "resolution" in practice means either an algorithm, or a reduction from a standard worst-case assumption, or an unconditional lower bound in a restricted model.

## 2. Mathematical Foundations

**Distributions.** Let $\mathcal{G}_n = \{0,1\}^{\binom{n}{2}}$. Define
$$\mathbb{P}_0 = G(n,1/2), \qquad \mathbb{P}_k = G(n,1/2,k),$$
where under $\mathbb{P}_k$, $S \sim \mathrm{Unif}\binom{[n]}{k}$ and $A_{ij} = 1$ for $i \ne j \in S$, $A_{ij} \sim \mathrm{Bern}(1/2)$ otherwise.

**Detection.** Strong detection asks for a test $T:\mathcal{G}_n \to \{0,1\}$ with $\mathbb{P}_0[T=1] + \mathbb{P}_k[T=0] = o(1)$. The second moment of the likelihood ratio $L = d\mathbb{P}_k/d\mathbb{P}_0$ satisfies
$$\mathbb{E}_{\mathbb{P}_0}[L^2] = \mathbb{E}_{S,S'}\big[2^{\binom{|S \cap S'|}{2}}\big],$$
which is $1+o(1)$ when $k \le (2-\varepsilon)\log_2 n$ and unbounded above it — the information-theoretic threshold.

**Spectral structure.** Write $A$ for the adjacency matrix and $M = 2A - J + I$ for the $\pm1$ centering. Under $\mathbb{P}_0$, $\|M\|_2 = (2+o(1))\sqrt{n}$ (Füredi–Komlós). The planted clique contributes a rank-one term $\approx \mathbf{1}_S \mathbf{1}_S^\top$ of spectral norm $k$. Hence the signal escapes the bulk exactly when
$$k \;\gtrsim\; 2\sqrt{n},$$
which is the origin of the $\sqrt{n}$ barrier.

**Degrees.** For $v \in S$, $\deg(v) \approx \frac{n}{2} + \frac{k}{2}$; for $v \notin S$, $\deg(v) \approx \frac n2$ with fluctuation $\frac{\sqrt n}{2}$. Uniform control over $n$ vertices costs $\sqrt{2\log n}$ standard deviations, so degree counting succeeds iff $k = \Omega(\sqrt{n \log n})$.

**Low-degree heuristic.** For a degree-$D$ polynomial $f$, the advantage is measured by
$$\mathrm{Adv}_{\le D} = \max_{\deg f \le D} \frac{\mathbb{E}_{\mathbb{P}_k}[f]}{\sqrt{\mathbb{E}_{\mathbb{P}_0}[f^2]}}.$$
For planted clique, $\mathrm{Adv}_{\le D} = O(1)$ when $k \ll \sqrt n$ and $D = O(\log n)$; the low-degree conjecture (Hopkins 2018) upgrades this to evidence for $n^{\tilde\Omega(1)}$-time hardness.

**Sum-of-squares.** The degree-$d$ SoS relaxation of $\max |S|$ over pseudo-distributions satisfying $x_i^2 = x_i$ and $x_ix_j = 0$ for $(i,j)\notin E$ gives a value $\mathrm{SoS}_d(G)$; the conjecture predicts $\mathrm{SoS}_d(G(n,1/2)) \gg k$ for $k \ll \sqrt n$ and small $d$.

## 3. History & State of the Art (SOTA)

- **1976.** Karp asks for a polynomial algorithm finding a clique of size $(1+\varepsilon)\log_2 n$ in $G(n,1/2)$ — the "clique problem" that motivates the planted version. Greedy reaches $(1+o(1))\log_2 n$, and nothing beats it.
- **1992.** Jerrum formalizes the planted model and proves the Metropolis process fails for $k = n^{1/2-\varepsilon}$ (*Large cliques elude the Metropolis process*).
- **1995.** Kučera observes the degree-based algorithm works at $k = \Omega(\sqrt{n\log n})$.
- **1998.** Alon, Krivelevich and Sudakov give the spectral algorithm at $k = c\sqrt n$, the still-unimproved threshold up to constants.
- **2000–2003.** Feige–Krauthgamer extend to semirandom graphs and show the Lovász–Schrijver hierarchy at $r$ rounds needs $k = \tilde\Omega(\sqrt{n/2^r})$.
- **2008–2015.** Frieze–Kannan (tensor), Ames–Vavasis (nuclear-norm), Dekel–Gurel-Gurevich–Peres (linear time), Deshpande–Montanari (message passing, $k \ge \sqrt{n/e}$, near-linear time) all match $\Theta(\sqrt n)$ with better constants or running times.
- **2013–2017.** Feldman, Grigorescu, Reyzin, Vempala and Xiao prove statistical-query lower bounds; Meka–Potechin–Wigderson and then Barak, Hopkins, Kelner, Kothari, Moitra and Potechin prove the near-tight degree-$d$ SoS lower bound.
- **2011–2020.** The conjecture becomes a hardness hub: cryptographic applications (Applebaum–Barak–Wigderson), approximate Nash equilibria (Hazan–Krauthgamer), densest $k$-subgraph, sparse PCA (Berthet–Rigollet), and the reduction framework of Brennan–Bresler.

**SOTA summary:** algorithms at $k = \Theta(\sqrt n)$; unconditional hardness only in restricted models (SQ, SoS, low-degree, monotone circuits, local/MCMC dynamics); no reduction from a worst-case assumption is known in either direction.

## 4. Partial Results / Verified Cases

- **$k \ge (2+\varepsilon)\log_2 n$:** exhaustive search over $\binom{n}{k}$ finds $S$ whp — solved information-theoretically, in time $n^{O(\log n)}$.
- **$k = \Omega(\sqrt{n\log n})$:** Kučera's degree ranking, $O(n^2)$ time.
- **$k \ge c\sqrt n$, any fixed $c>0$:** Alon–Krivelevich–Sudakov, spectral plus $n^{O(\log(1/c))}$ enumeration.
- **$k \ge \sqrt{n/e}\,(1+o(1))$:** Deshpande–Montanari, belief propagation, $O(n^2\log n)$ time.
- **$k = \Omega(\sqrt n)$ in the semirandom model** (adversary may delete edges outside $S$): Feige–Krauthgamer, via the Lovász theta function, with a certificate.
- **Restricted-model hardness, all for $k = n^{1/2-\varepsilon}$:**
  - Degree-$d$ SoS requires $k \ge n^{1/2 - O(d/\log n)}$ (Barak et al., FOCS 2016) — so $n^{\Omega(1)}$-degree SoS is needed below $\sqrt n$.
  - Statistical algorithms with tolerance $\tilde O(\sqrt{k^2/n})$ need $n^{\Omega(\log n)}$ queries (Feldman et al., JACM 2017).
  - Monotone circuits: $k$-clique on $G(n,p)$ at the threshold needs size $n^{\Omega(k)}$ for $k \le n^{1/3}$ (Rossman, SICOMP 2014).
  - Local Markov dynamics: Jerrum (1992); overlap-gap obstruction for dense subgraphs (Gamarnik–Zadik).
- **$k \le (2-\varepsilon)\log_2 n$:** impossible for *any* algorithm — the second-moment computation of Section 2.

## 5. Principal Obstacles

- **No worst-case anchor.** Planted clique is an average-case problem over a fixed, highly symmetric distribution. Bogdanov–Trevisan-style barriers rule out non-adaptive worst-case-to-average-case reductions for $\mathsf{NP}$ problems under standard assumptions, so a proof from $\mathsf{P}\neq\mathsf{NP}$ is not available with current tools.
- **Symmetry kills counting/diagonalization.** The distribution is invariant under $S_n$; every vertex and edge is exchangeable. Techniques that isolate a hard instance have nothing to isolate.
- **Spectral saturation.** Every known efficient method — degrees, eigenvectors, AMP, nuclear norm, theta function, low-degree polynomials — is at bottom a spectral statistic of a matrix built from $A$. All such statistics see signal $k$ against a semicircle bulk of width $2\sqrt n$; below $\sqrt n$ the leading eigenvector is pure noise. Tensor and higher-order lifts raise the signal but raise the noise by the same order (Frieze–Kannan), because the relevant tensors have no efficiently computable spectral norm.
- **Lower bounds are model-bound.** SoS, SQ and low-degree bounds are proofs about *restricted* algorithm classes. Extending them requires either a general model of computation (i.e. circuit lower bounds, wide open) or a completeness theory for average-case problems, which does not exist at the needed granularity.
- **Pseudo-calibration is one-directional.** The moment-matrix machinery of Barak et al. certifies that natural relaxations fail, but gives no route to a reduction; conversely, the constructions leave open whether some non-spectral algebraic invariant separates the two distributions.

## 6. The Gap

Proven: polynomial algorithms for $k \ge (1/\sqrt e)\sqrt n$; impossibility for $k \le (2-\varepsilon)\log_2 n$; restricted-model hardness for $k \le n^{1/2-\varepsilon}$. Conjectured: hardness for all $\log n \ll k \ll \sqrt n$.

The gap is the entire window
$$\Theta(\log n) \;\ll\; k \;\ll\; \sqrt n,$$
a polynomial-sized statistical–computational gap. Two distinct crossings are needed. **(a)** *Algorithmic side:* an efficient statistic whose signal-to-noise at $k = n^{0.49}$ exceeds a constant — necessarily not a bounded-degree polynomial in $A$, by the low-degree bounds. **(b)** *Hardness side:* a reduction transporting hardness from a standard assumption (worst-case lattice problems, refuting random CSPs, or $\mathsf{NP}$-hardness with a non-black-box argument) into a distribution as symmetric as $G(n,1/2,k)$. No candidate for either currently exists past the $\sqrt n$ / restricted-model line.

## 7. Current Research (as of June 2026)

- **Low-degree program.** The dominant framework (Hopkins, Kothari, Potechin, Raghavendra, Schramm, Steurer; Wein, Bandeira) treats $\mathrm{Adv}_{\le D}$ as the canonical hardness predictor and now covers most planted problems. Active work: making the low-degree conjecture itself provable in a defined model, and finding counterexamples where it mispredicts *(frontier — verify)*.
- **Reduction webs.** Brennan–Bresler-style secret-leakage reductions continue to be extended, deriving sharp constants for sparse PCA, biclustering, robust mean estimation, tensor PCA and community detection from planted clique. Groups at MIT, Berkeley, Stanford, EPFL, ETH.
- **Landscape/geometry.** Overlap-gap arguments (Gamarnik, Zadik, Wein) rule out stable and local algorithms below $\sqrt n$ and are being pushed toward broader classes.
- **Quantum and continuous-time methods.** Occasional claims of quantum speedups below $\sqrt n$; none survives scrutiny to date *(frontier — verify)*.
- **Certification vs. search.** Certifying $\omega(G(n,1/2)) \le k$ for $k = n^{0.49}$ remains open even with quasipolynomial time; recent work connects this to refutation of random CSPs *(frontier — verify)*.

## 8. Future Work

1. **Break the spectral barrier or explain it.** Either produce an algorithm at $k = n^{0.49}$ or prove a lower bound against all algorithms expressible as spectral statistics of arbitrary polynomially-computable matrix ensembles.
2. **A completeness theory.** Identify a distributional problem to which planted clique reduces *and* which reduces back — currently the reduction web has planted clique only as a source.
3. **Sharpen the constant.** Close the gap between $\sqrt{n/e}$ (Deshpande–Montanari) and the conjectured optimum near $\sqrt{n/e}$ or below; determine whether $c^*$ is a genuine algorithmic phase transition.
4. **Prove the low-degree conjecture** in a robust setting, or exhibit a natural problem where degree-$O(\log n)$ polynomials fail but a polynomial-time algorithm exists.
5. **Cryptography from planted clique.** Extend Applebaum–Barak–Wigderson to obtain public-key primitives from the conjecture at $k = n^{1/2-\varepsilon}$.

## 9. Key References

- **[Foundational]** M. Jerrum. *Large cliques elude the Metropolis process.* Random Structures & Algorithms, 3(4):347–359, 1992.
- **[Foundational]** L. Kučera. *Expected complexity of graph partitioning problems.* Discrete Applied Mathematics, 57(2–3):193–212, 1995.
- **[Foundational]** N. Alon, M. Krivelevich, B. Sudakov. *Finding a large hidden clique in a random graph.* Random Structures & Algorithms, 13(3–4):457–466, 1998.
- **[SOTA]** U. Feige, R. Krauthgamer. *Finding and certifying a large hidden clique in a semirandom graph.* Random Structures & Algorithms, 16(2):195–208, 2000.
- **[SOTA]** Y. Deshpande, A. Montanari. *Finding hidden cliques of size $\sqrt{N/e}$ in nearly linear time.* Foundations of Computational Mathematics, 15(4):1069–1128, 2015.
- **[SOTA]** Y. Dekel, O. Gurel-Gurevich, Y. Peres. *Finding hidden cliques in linear time with high probability.* Combinatorics, Probability and Computing, 23(1):29–49, 2014.
- **[SOTA]** B. Barak, S. B. Hopkins, J. Kelner, P. Kothari, A. Moitra, A. Potechin. *A nearly tight sum-of-squares lower bound for the planted clique problem.* SIAM Journal on Computing, 48(2):687–735, 2019 (FOCS 2016).
- **[SOTA]** R. Meka, A. Potechin, A. Wigderson. *Sum-of-squares lower bounds for planted clique.* STOC 2015.
- **[SOTA]** V. Feldman, E. Grigorescu, L. Reyzin, S. Vempala, Y. Xiao. *Statistical algorithms and a lower bound for detecting planted cliques.* Journal of the ACM, 64(2):8, 2017.
- **[SOTA]** B. Rossman. *The monotone complexity of $k$-clique on random graphs.* SIAM Journal on Computing, 43(1):256–279, 2014.
- **[Applications]** E. Hazan, R. Krauthgamer. *How hard is it to approximate the best Nash equilibrium?* SIAM Journal on Computing, 40(1):79–91, 2011.
- **[Applications]** B. Applebaum, B. Barak, A. Wigderson. *Public-key cryptography from different assumptions.* STOC 2010.
- **[Applications]** Q. Berthet, P. Rigollet. *Complexity theoretic lower bounds for sparse principal component detection.* COLT 2013.
- **[Survey]** S. B. Hopkins. *Statistical Inference and the Sum of Squares Method.* PhD thesis, Cornell University, 2018.
- **[Survey]** A. S. Bandeira, A. El Alaoui, S. B. Hopkins, T. Schramm, A. S. Wein, I. Zadik. *The Franz–Parisi criterion and computational trade-offs in high dimensional statistics.* NeurIPS 2022.
- **[Survey]** M. Brennan, G. Bresler. *Reducibility and statistical-computational gaps from secret leakage.* COLT 2020.

## 10. Worked Example / Concrete Special Case

Take $n = 10^6$, so $\sqrt n = 1000$ and $\log_2 n \approx 20$.

**Case A: $k = 4000$ (above the barrier).** Compute $M = 2A - J + I$, a symmetric $\pm1$ matrix with zero diagonal off the clique. Its noise part has $\|\cdot\|_2 \approx 2\sqrt n = 2000$; the clique contributes $\approx k = 4000$. So the top eigenvalue separates, and its eigenvector $v$ has mass concentrated on $S$. Take the $k$ vertices of largest $|v_i|$, call this $W$; standard analysis gives $|W \cap S| \ge 3k/4$. Then keep every vertex of $[n]$ adjacent to at least $3k/4$ members of $W$. A vertex in $S$ passes; a vertex outside $S$ passes with probability $\Pr[\mathrm{Bin}(k,1/2) \ge 3k/4] \le e^{-k/8} = e^{-500}$, so a union bound over $10^6$ vertices recovers $S$ exactly. Total: two matrix operations, $\tilde O(n^2)$.

**Case B: $k = 100$ (inside the gap).** Now $k \ll 2\sqrt n$: the planted eigenvalue $100$ is buried inside the semicircle of radius $2000$, and the top eigenvector is uninformative. Degrees are no better. A clique vertex has expected degree
$$\tfrac{n}{2} + \tfrac{k}{2} = 500{,}050,$$
a non-clique vertex $500{,}000$, both with standard deviation $\sqrt n/2 = 500$. The shift is $0.1$ standard deviations, while the maximum of $10^6$ Gaussians sits $\approx 5.2$ standard deviations above the mean. So the top-degree vertices are noise, not signal.

Statistically the clique is still there: $k = 100 \gg 2\log_2 n \approx 40$, and $\mathbb{E}_{\mathbb{P}_0}[L^2] \approx \binom{n}{k}^{-1}\cdot 2^{\binom{k}{2}} \cdot \ldots$ diverges, so brute force over all $\binom{10^6}{100}$ vertex sets — or, more cheaply, over $\binom{10^6}{40}$ candidate seeds — succeeds with certainty. That is $n^{\Theta(\log n)}$ work.

**Case C: certification.** Even asking for a *proof* that $G \sim G(n,1/2)$ has no clique of size $100$ defeats degree-$4$ SoS: by Barak et al., $\mathrm{SoS}_4$ certifies only $\omega(G) \le \tilde O(n^{1/2})=\tilde O(1000)$, a factor $10$ short.

The conjecture is exactly the claim that Case B has no shortcut: the gap between $k=100$ (statistically easy, computationally believed hard) and $k=4000$ (easy) is real and polynomially wide.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*