---
id: 10-theoretical-cs/oblivious-ram-lower-bound
title: "Oblivious RAM Lower Bound"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Oblivious RAM Lower Bound

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/oblivious-ram-lower-bound` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

An Oblivious RAM (ORAM) is a compiler that turns a program's logical memory accesses into physical accesses whose *pattern* leaks nothing about the logical sequence. The cost measure is **overhead**: physical probes (or bits transferred) per logical operation.

The classical claim, due to Goldreich and Ostrovsky (1987–1996), is that overhead $\Omega(\log n)$ is unavoidable for an array of $n$ entries. Their proof holds only in a restricted "balls-in-bins" model where memory cells store data blocks opaquely and are never encoded together. The open problem has two halves:

1. **(Settled, 2018–2021.)** Prove an $\Omega(\log n)$ lower bound with no structural restriction, in the cell-probe model, for *online* ORAM with computational security. Done by Larsen–Nielsen (CRYPTO 2018) and extended to all parameter regimes by Komargodski–Lin (CRYPTO 2021). Matched by OptORAMa's $O(\log n)$ upper bound.
2. **(Open.)** Determine the true complexity outside the online, single-server, uniform-cost regime. Concretely: is there any $\omega(\log n)$ lower bound for **offline** ORAM (the whole access sequence known in advance)? Is $\Omega(\log n)$ tight in **bandwidth** (bits, not probes) for large blocks? Do lower bounds survive **server computation**, **multiple non-colluding servers**, or **relaxed (differential) obliviousness**?

A complete resolution of (2) means either an unconditional $\omega(\log n)$ lower bound in one of these models, or an ORAM construction with $o(\log n)$ overhead there, or a formal barrier proving neither is achievable with current techniques.

## 2. Mathematical Foundations

**RAM.** Memory is an array of $n$ cells of $w$ bits each; the client holds $m$ cells ($m \ll n$). A logical operation is $\mathsf{op}_i \in \{(\mathrm{read}, a), (\mathrm{write}, a, v)\}$ with address $a \in [n]$, value $v \in \{0,1\}^{w}$.

**ORAM.** A (probabilistic) compiler $\mathcal{C}$ maps a logical sequence $y = (\mathsf{op}_1,\dots,\mathsf{op}_M)$ to a physical probe sequence. Write $A(y)$ for the random variable recording the *addresses* probed (not contents). Correctness: with probability $\ge 1 - \mathrm{negl}(n)$ every read returns the last value written.

**Security.** For all $y, y'$ with $|y| = |y'|$,
$$A(y) \;\approx_c\; A(y') ,$$
computational indistinguishability against $\mathrm{poly}(n)$-time adversaries. Statistical security replaces $\approx_c$ by $\|A(y) - A(y')\|_{TV} \le \mathrm{negl}(n)$.

**Overhead.** For $M$ operations,
$$\mathrm{ovh} \;=\; \frac{\mathbb{E}[\\#\text{physical probes}]}{M}, \qquad \mathrm{bandwidth} \;=\; \frac{\mathbb{E}[\text{bits transferred}]}{M \cdot w}.$$

**Online vs. offline.** Online: $\mathsf{op}_{i+1}$ is revealed only after $\mathsf{op}_i$ completes. Offline: all of $y$ is available at the start (the Goldreich–Ostrovsky setting; also the setting of oblivious sorting).

**Lower-bound machinery.** Larsen–Nielsen work in the **cell-probe model** and use the *information transfer* method of Pătraşcu–Demaine. Fix $M = n$ operations, build a balanced binary tree $T$ over the time axis $[1,M]$. For an internal node $v$ with left interval $L_v$ and right interval $R_v$, let
$$\mathrm{IT}(v) \;=\; \\#\{\text{cells written during } L_v \text{ and read during } R_v \text{ with no intervening write}\}.$$
Every probe is counted at most once across the tree, so
$$\mathbb{E}\Big[\sum_{v \in T} \mathrm{IT}(v)\Big] \;\le\; \mathbb{E}[\text{total probes}] .$$
The theorem proved is: for any online ORAM with $m = n^{o(1)}$ client cells and cell size $w = \Omega(\log n)$,
$$\mathrm{ovh} \;=\; \Omega\!\left(\log \frac{n w}{m}\right) \;=\; \Omega(\log n).$$
The security definition is what makes the argument possible: obliviousness forces the probe distribution to be *the same* for a hard "many distinct addresses" distribution and for an easy "one address repeated" distribution, so the encoding/decoding compression argument at each of the $\log n$ levels transfers $\Omega(w)$ bits in expectation.

**Barrier (Boyle–Naor).** Let $\mathrm{Sort}(n)$ be the size of the smallest circuit sorting $n$ elements of $w$-bit keys in a comparison-agnostic model. Boyle–Naor show: an $\omega(\log n)$ lower bound for *offline* ORAM (even in restricted "balls-in-bins" form) implies $\mathrm{Sort}(n) = \omega(n \log n)$ for such circuits — a superlinear circuit lower bound of a kind unknown for any explicit problem.

## 3. History & State of the Art (SOTA)

- **1987/1990.** Goldreich (STOC 1987) and Ostrovsky (STOC 1990) introduce ORAM for software protection; the square-root and hierarchical constructions give $O(\sqrt{n})$ and $O(\log^3 n)$ amortized overhead.
- **1996.** Goldreich–Ostrovsky (JACM 43(3)) state the $\Omega(\log n)$ lower bound. Its restriction to the balls-in-bins model was widely elided for two decades.
- **2013.** Path ORAM (Stefanov et al., CCS 2013; JACM 2018): $O(\log^2 n)$ bandwidth, $O(\log n)$ blocks of client memory, simple enough to be implemented in hardware (Intel SGX-adjacent designs, Ascend/Phantom processors).
- **2016.** Boyle–Naor (ITCS 2016), *"Is there an oblivious RAM lower bound?"*, exposes the model restriction and proves the sorting-circuit barrier for offline ORAM.
- **2018.** Larsen–Nielsen (CRYPTO 2018), *"Yes, there is an oblivious RAM lower bound!"*: unconditional $\Omega(\log n)$ for online ORAM in the cell-probe model, with computational security.
- **2020.** OptORAMa (Asharov, Komargodski, Lin, Nayak, Peserico, Shi; EUROCRYPT 2020, JACM 2023): $O(\log n)$ amortized overhead, closing the online single-server gap up to constants.
- **2021.** Komargodski–Lin (CRYPTO 2021) extend the $\Omega(\log n)$ bound to all block-size/client-memory regimes; Asharov–Komargodski–Lin–Shi (CRYPTO 2021) achieve $O(\log n)$ *worst-case* overhead.

## 4. Partial Results / Verified Cases

| Setting | Bound | Source |
|---|---|---|
| Balls-in-bins, offline, statistical | $\Omega(\log n)$ | Goldreich–Ostrovsky 1996 |
| Online, cell probe, $w = \Omega(\log n)$, $m = n^{o(1)}$ | $\Omega(\log(nw/m))$ | Larsen–Nielsen 2018 |
| Online, all $w$ and $m$ (including $w = O(1)$) | $\Omega(\log n)$ | Komargodski–Lin 2021 |
| Online, statistically secure, small failure probability | $\Omega(\log n)$, robust version | Hubáček–Koucký–Král–Slívová, TCC 2019 |
| Oblivious stacks, queues, priority queues, search trees | $\Omega(\log n)$ per operation | Jacob–Larsen–Nielsen, SODA 2019 |
| Oblivious near-neighbor search, $d$ dimensions | $\Omega(\log n)$ query overhead | Larsen–Malkin–Weinstein–Yeo, SODA 2020 |
| Differentially private RAM ($\varepsilon$-DP access) | $\Omega(\log n)$ | Persiano–Yeo, EUROCRYPT 2019 |
| Multi-server, $\ell$ non-colluding servers, restricted | $\Omega(\log n)$ | Larsen–Simkin–Yeo, TCC 2020 |
| One-round ORAM | $\Omega(\log n)$-type bound | Cash–Drucker–Hoover, TCC 2020 |
| **Upper bound** $O(\log n)$ amortized / worst case | matching | OptORAMa 2020; AKLS 2021 |

Circumventions with real constructions: **Onion ORAM** (Devadas, van Dijk, Fletcher, Ren, Shi, Wichs; TCC 2016) achieves $O(1)$ *bandwidth blowup* for block size $\Omega(\log^{6} n)$ using homomorphic server computation — the probe count still obeys $\Omega(\log n)$, so no contradiction; it shows the bound is a statement about probes in a passive-server model.

## 5. Principal Obstacles

- **Offline is out of reach by design.** Boyle–Naor reduce it to superlinear circuit lower bounds for sorting. Circuit lower bounds better than $3n$ for explicit functions in general models remain unknown, so no current technique can push through.
- **Online read-only is also blocked.** Weiss–Wichs (TCC 2018) show that even an $\omega(\log n)$ lower bound for *online read-only* ORAM implies either sorting-circuit lower bounds or a breakthrough in constructing certain cryptographic objects — a two-sided barrier.
- **Information transfer saturates at $\log n$.** The counting tree has depth $\log M$; each level contributes at most $\Theta(1)$ amortized probes. To get $\omega(\log n)$ one needs a counting structure with $\omega(\log n)$ "independent" levels, and no such structure is known in cell-probe dynamic lower bounds — this is the same $\Omega(\log n)$ ceiling that blocks dynamic data-structure lower bounds generally (the notorious cell-probe barrier).
- **Encryption defeats combinatorics.** Any bound must hold against a compiler that stores arbitrary encoded functions of blocks (error-correcting codes, homomorphic ciphertexts), so no argument may assume "one block per cell". This is exactly what breaks the Goldreich–Ostrovsky counting proof.
- **Constants and bandwidth are invisible to probe counting.** A probe lower bound of $c \log n$ says nothing about whether the leading constant is $1$ or $100$, nor about bit-bandwidth when blocks are large.

## 6. The Gap

Proven: $\mathrm{ovh} = \Theta(\log n)$ for online, single-server, passive-server, cell-probe ORAM. Not proven, and the exact boundary:

- **Offline ORAM.** Best known lower bound remains the restricted-model $\Omega(\log n)$; no unconditional bound of any strength is known. Crossing this step requires either defeating the Boyle–Naor reduction (e.g., a lower bound that does not yield a sorting circuit) or proving $\mathrm{Sort}(n) = \omega(n\log n)$.
- **Constant factors.** Larsen–Nielsen give $\Omega(\log n)$ with an unspecified small constant; OptORAMa's constant is large (the original write-up is not competitive with Path ORAM below $n \approx 2^{30}$). Determining $\lim \mathrm{ovh}/\log n$ is entirely open.
- **Server computation / multi-server.** No unconditional $\Omega(\log n)$ bound is known when the server computes, and Onion ORAM shows $O(1)$ bandwidth blowup is achievable there. The boundary between "probe model, bound holds" and "computation model, bound fails" is unmapped.

## 7. Current Research (as of June 2026)

- **Aarhus (Larsen, Yeo, Simkin) and Cornell/NTT (Komargodski, Lin, Asharov, Shi)** remain the two poles: cell-probe lower bounds and hierarchical-ORAM upper bounds respectively.
- **Practical constant-factor optimality.** Work on making $O(\log n)$ ORAM concretely beat Path ORAM at realistic $n$ — oblivious hashing with tight compaction, and derandomized shuffles. *(frontier — verify)*
- **Differential obliviousness.** Chan–Chung–Maggs–Shi (SODA 2019) show $o(\log n)$ is possible for some tasks under relaxed leakage; mapping which tasks admit $O(\log\log n)$ or $O(1)$ overhead is active. *(frontier — verify)*
- **Doubly-efficient PIR and ORAM.** Lower bounds for ORAM-like primitives with preprocessing, connecting to LDC and PIR barriers. *(frontier — verify)*
- **Locality-aware ORAM.** Trade-offs between overhead and number of discontiguous memory regions touched (Asharov, Chan, Nayak, Pass, Ren, Shi) — lower bounds here are far from tight. *(frontier — verify)*

## 8. Future Work

- Prove an $\omega(\log n)$ lower bound for offline ORAM under a plausible complexity assumption, or extend the Boyle–Naor barrier to rule out all "natural" proofs.
- Develop a counting method with more than $\log n$ effective levels — likely the single highest-value technical goal, since it would also break the dynamic cell-probe barrier.
- Prove bit-bandwidth (not probe) lower bounds for block size $w = n^{\Omega(1)}$, where Onion ORAM sits.
- Settle multi-server ORAM: is $O(\log n / \log\log n)$ achievable with two non-colluding servers and no server computation?
- Nail the constant: exhibit an ORAM with overhead $(1+o(1)) \cdot c \log n$ matching a lower bound with the same $c$.

## 9. Key References

- **[Foundational]** Oded Goldreich, Rafail Ostrovsky. *Software Protection and Simulation on Oblivious RAMs.* Journal of the ACM 43(3):431–473, 1996.
- **[Foundational]** Oded Goldreich. *Towards a Theory of Software Protection and Simulation by Oblivious RAMs.* STOC 1987.
- **[Barrier]** Elette Boyle, Moni Naor. *Is There an Oblivious RAM Lower Bound?* ITCS 2016.
- **[SOTA / Lower bound]** Kasper Green Larsen, Jesper Buus Nielsen. *Yes, There is an Oblivious RAM Lower Bound!* CRYPTO 2018.
- **[SOTA / Lower bound]** Ilan Komargodski, Wei-Kai Lin. *A Logarithmic Lower Bound for Oblivious RAM (for All Parameters).* CRYPTO 2021.
- **[SOTA / Upper bound]** Gilad Asharov, Ilan Komargodski, Wei-Kai Lin, Kartik Nayak, Enoch Peserico, Elaine Shi. *OptORAMa: Optimal Oblivious RAM.* EUROCRYPT 2020; Journal of the ACM, 2023.
- **[Upper bound]** Emil Stefanov, Marten van Dijk, Elaine Shi, Christopher Fletcher, Ling Ren, Xiangyao Yu, Srinivas Devadas. *Path ORAM: An Extremely Simple Oblivious RAM Protocol.* CCS 2013; JACM 65(4), 2018.
- **[Barrier]** Mor Weiss, Daniel Wichs. *Is There an Oblivious RAM Lower Bound for Online Reads?* TCC 2018; Journal of Cryptology, 2021.
- **[Extension]** Riko Jacob, Kasper Green Larsen, Jesper Buus Nielsen. *Lower Bounds for Oblivious Data Structures.* SODA 2019.
- **[Extension]** Pavel Hubáček, Michal Koucký, Karel Král, Veronika Slívová. *Stronger Lower Bounds for Online ORAM.* TCC 2019.
- **[Extension]** Giuseppe Persiano, Kevin Yeo. *Lower Bounds for Differentially Private RAMs.* EUROCRYPT 2019.
- **[Model separation]** Srinivas Devadas, Marten van Dijk, Christopher Fletcher, Ling Ren, Elaine Shi, Daniel Wichs. *Onion ORAM: A Constant Bandwidth Blowup Oblivious RAM.* TCC 2016-A.
- **[Technique]** Mihai Pătraşcu, Erik D. Demaine. *Logarithmic Lower Bounds in the Cell-Probe Model.* SIAM Journal on Computing 35(4):932–963, 2006.
- **[Survey]** Kevin Yeo. *Lower Bounds for Oblivious Data Structures and Cryptographic Primitives* (thesis / survey material), Columbia University, 2020.

## 10. Worked Example / Concrete Special Case

**Setup.** $n = 8$ logical blocks, cell size $w = 8$ bits, client memory $m = 1$ cell. Run $M = 8$ operations.

**Step 1 — obliviousness equalizes two sequences.** Take
$$y_{\text{hard}} = \big(\mathrm{write}(1,v_1),\dots,\mathrm{write}(4,v_4),\ \mathrm{read}(1),\dots,\mathrm{read}(4)\big),$$
$$y_{\text{easy}} = \big(\mathrm{write}(1,0)\times 4,\ \mathrm{read}(1)\times 4\big).$$
Security forces $A(y_{\text{hard}}) \approx A(y_{\text{easy}})$: the *distribution of probed addresses* is identical, so the number of probes is (up to negligible slack) the same.

**Step 2 — information transfer at the root.** Let $v$ be the root of the time tree, $L_v = \{1,2,3,4\}$ (the writes), $R_v = \{5,6,7,8\}$ (the reads). Choose $v_1,\dots,v_4$ uniformly at random: $4w = 32$ bits of entropy. The client holds $m w = 8$ bits. The reads must output all 32 bits. Everything not in client memory must arrive through cells written in $L_v$ and read in $R_v$:
$$\mathrm{IT}(v)\cdot w \;+\; m w \;\ge\; 4w \quad\Longrightarrow\quad \mathrm{IT}(v) \;\ge\; 3 .$$

**Step 3 — recurse.** The same argument applied to each of the two children (2 writes / 2 reads, $2w = 16$ random bits, $8$ bits of client memory) gives $\mathrm{IT}(v) \ge 1$ at each. At depth $d$ with $2^{\log n - d}$ nodes, each node contributes $\Omega(1)$, so summing over $\log n$ levels:
$$\mathbb{E}[\text{total probes}] \;\ge\; \sum_{d=0}^{\log n - 1} \Omega\!\left(2^{d}\right) \cdot \Omega(1) \;=\; \Omega(n \log n) \;\Longrightarrow\; \mathrm{ovh} = \Omega(\log n).$$

**Step 4 — the numbers at scale.** For $n = 2^{20}$: the bound says $\ge c \cdot 20$ probes per access. Path ORAM uses $\approx 2\log^2 n \approx 800$ block transfers; OptORAMa uses $O(\log n)$, i.e. $C \cdot 20$ with $C$ in the hundreds in the original analysis. So the *asymptotic* gap is closed and the *concrete* gap between $c$ and $C$ is roughly three orders of magnitude — that residual factor, plus the entire offline question, is what remains open.

**Why this does not extend to offline.** In $y_{\text{hard}}$ the compiler learns the read addresses only at time $5$. Offline it knows them at time $1$, so it can place $v_1,\dots,v_4$ where they will be needed — exactly an oblivious sorting/routing problem, and by Boyle–Naor any $\omega(\log n)$ bound here would yield a superlinear sorting-circuit lower bound.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*