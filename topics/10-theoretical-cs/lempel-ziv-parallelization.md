---
id: 10-theoretical-cs/lempel-ziv-parallelization
title: "Lempel-Ziv Parallelization"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lempel-Ziv Parallelization

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/lempel-ziv-parallelization` · **Status:** open

## 1. Problem Statement / Conjecture

Lempel–Ziv parsing is defined by a strictly sequential greedy recurrence: the $k$-th phrase begins where the $(k-1)$-st ended, and its content depends on every character read so far. The parallelization problem asks how much of that sequentiality is intrinsic.

Three linked questions, all open:

- **(Q1) Work-optimal deterministic LZ77.** Is there a *deterministic* PRAM algorithm computing the greedy LZ77 factorization of $T \in \Sigma^n$ in $O(n)$ work and $O(\log n)$ depth for integer alphabets $\Sigma = \{1,\dots,n^{O(1)}\}$? Farach and Muthukrishnan (SPAA 1995) achieve these bounds *randomized* on a CRCW PRAM; no deterministic match is known, and the best deterministic linear-work algorithms have depth $\Theta(\log^2 n)$.
- **(Q2) Packed/sublinear parallel parsing.** Ellert (SPIRE 2023) computes LZ77 sequentially in $O(n/\log_\sigma n)$ time on the packed word-RAM. Is there a parallel algorithm with $O(n\log\sigma/\log n)$ *work* and $\mathrm{polylog}(n)$ depth — i.e. work-optimality below the $\Theta(n)$ barrier?
- **(Q3) LZ78/LZW approximation in NC.** Greedy LZ78/LZW parsing is **P-complete** under log-space reductions (De Agostino 1994). Hence it admits no NC algorithm unless $\mathrm{NC} = \mathrm{P}$. Open: is there an NC algorithm producing a parse with at most $c \cdot z_{78}(T)$ phrases for some constant $c$, where $z_{78}$ is the greedy phrase count?

A complete resolution of (Q1) is an algorithm with proven bounds on a stated PRAM variant, or an unconditional/conditional lower bound separating deterministic from randomized parsing. A resolution of (Q3) is a constant-factor NC approximation, or a proof that constant-factor approximation is itself P-hard.

## 2. Mathematical Foundations

Let $T = T[1..n]$ over an ordered alphabet $\Sigma$, $\sigma = |\Sigma|$.

**Longest previous factor.** For $1 \le i \le n$,
$$\mathrm{LPF}[i] = \max\{\,\ell \ge 0 : \exists\, j < i \text{ with } T[j..j+\ell-1] = T[i..i+\ell-1]\,\},$$
where the source may overlap the target ($j + \ell - 1 \ge i$ is allowed — this is the *self-referential* variant used in practice).

**LZ77 factorization.** Define the successor map $S(i) = i + \max(1, \mathrm{LPF}[i])$. The phrase boundaries are the orbit
$$p_1 = 1, \qquad p_{k+1} = S(p_k),$$
terminating at the first $p_{z+1} > n$. The output is the phrase list $(\pi_k, \ell_k)_{k=1}^{z}$ with $\ell_k = \mathrm{LPF}[p_k]$ and $\pi_k$ a witness position $j < p_k$ realizing it (literal $T[p_k]$ when $\ell_k = 0$). Write $z = z(T)$.

**Suffix array route.** With $\mathrm{SA}$ the suffix array, $\mathrm{ISA} = \mathrm{SA}^{-1}$ and $\mathrm{LCP}[r] = \mathrm{lcp}(T[\mathrm{SA}[r-1]..], T[\mathrm{SA}[r]..])$, Crochemore and Ilie (2008) show
$$\mathrm{LPF}[i] = \max\bigl(\mathrm{lcp}(i, \mathrm{prev}(i)),\ \mathrm{lcp}(i, \mathrm{next}(i))\bigr),$$
where $\mathrm{prev}(i)$ / $\mathrm{next}(i)$ are the nearest suffix-array neighbours of $\mathrm{ISA}[i]$ with smaller text position, and $\mathrm{lcp}(a,b)$ is a range minimum over $\mathrm{LCP}$. Computing all $\mathrm{prev}/\mathrm{next}$ is exactly the **all-nearest-smaller-values (ANSV)** problem, solvable in $O(n)$ work and $O(\log\log n)$ depth on a CRCW PRAM (Berkman–Schieber–Vishkin 1993).

**LZ78.** Phrases $f_1 f_2 \cdots f_{z_{78}}$ with each $f_k = f_{j}c$ for some earlier phrase $f_j$ ($j<k$, or the empty phrase) and $c \in \Sigma$, chosen greedily longest. The dictionary evolves as a trie; this evolution is the object of the P-completeness proof.

**Complexity model.** Depth $D$ and work $W$ on the CRCW/EREW PRAM; $\mathrm{NC} = $ problems with $D = \mathrm{polylog}(n)$, $W = \mathrm{poly}(n)$. *Work-optimal* means $W = O(T_{\text{seq}})$ for the best sequential time $T_{\text{seq}}$.

**Size relations.** $z(T) \le \frac{n}{\log_\sigma n}(1+o(1))$; $z \le g^*$ for the smallest grammar $g^*$, and $g^* = O(z \log(n/z))$ (Rytter 2003; Charikar et al. 2005). Also $z = O(r \log^2 n)$ for the BWT run count $r$ (Kempa–Kociumaka, FOCS 2020).

## 3. History & State of the Art (SOTA)

- **1977–78.** Ziv and Lempel introduce LZ77 and LZ78; both are defined by an inherently online greedy rule.
- **1991.** Crochemore and Rytter give the first NC algorithm for the LZ77 ($f$-)factorization: $O(\log n)$ time with $n$ processors on a CRCW PRAM, i.e. $O(n\log n)$ work. Not work-optimal.
- **1994.** De Agostino proves greedy LZ2/LZW dictionary compression is P-complete under log-space reductions; catalogued in Greenlaw–Hoover–Ruzzo's *Limits to Parallel Computation* (1995). This permanently separates the two families: **LZ77 is in NC, LZ78 is not (unless NC = P).**
- **1995–96.** Farach and Muthukrishnan give an optimal randomized CRCW algorithm: $O(\log n)$ time, $O(n)$ work, via optimal randomized suffix-tree construction.
- **2003–2006.** Kärkkäinen–Sanders skew algorithm: linear-work suffix arrays with $O(\log^2 n)$ depth, giving the standard deterministic route to LPF.
- **2008–2013.** Crochemore–Ilie's LPF formulation; Kärkkäinen–Kempa–Puglisi's linear-time small-space sequential parsers (CPM/SEA 2013).
- **2013–2017.** Shun and Zhao give the first practical shared-memory parallel LZ77 (DCC 2013): ANSV on the suffix array plus a merge/pointer-jumping phase, $O(n\log n)$ work, $O(\log^2 n)$ depth, with ~20–30× speedup on 40 cores; consolidated in Shun's ACM Books volume (2017).
- **2019–2023.** String synchronizing sets (Kempa–Kociumaka, STOC 2019) give sublinear-time BWT and LCE machinery; Ellert (SPIRE 2023) attains $O(n/\log_\sigma n)$ sequential LZ77 — sequential time now beats the natural $\Theta(n)$ parallel work of every known parallel parser.

## 4. Partial Results / Verified Cases

- **Constant alphabet, randomized CRCW:** $O(\log n)$ depth, $O(n)$ work, optimal (Farach–Muthukrishnan 1995). Q1 is solved *up to randomization*.
- **Integer alphabet $\sigma = n^{O(1)}$, deterministic EREW:** $O(n)$ work, $O(\log^2 n)$ depth, by skew suffix array + parallel LCP + ANSV + tree-contraction chaining. Polylog depth with optimal work is therefore achieved; $O(\log n)$ depth is not.
- **The chaining step is not the obstacle.** Since $S(i) > i$, the map $S$ induces a forest on $[1..n]$; extracting the orbit of $1$ is a root-path/list-ranking problem, solved deterministically in $O(n)$ work and $O(\log n)$ depth (Cole–Vishkin). The bottleneck is entirely in producing $\mathrm{LPF}$.
- **Bounded window $w = O(1)$:** trivially in $\mathrm{NC}^1$ with $O(n)$ work — each phrase depends on $O(1)$ preceding characters, so factor boundaries are computed by a constant-width prefix scan.
- **LZ78 lower bound side:** greedy LZ2/LZW is P-complete (De Agostino 1994); De Agostino (*Information Sciences*, 2001) gives NC parsers achieving a *sublinear-window* approximation with provable ratio degradation, not a constant factor on unbounded input.
- **Approximate LZ77:** Fischer, Gagie, Gawrychowski and Kociumaka (ESA 2015) produce a parsing of size $O(z\log(n/z))$ in small space; its phase structure is amenable to parallelism, but no matching work-optimal parallel bound is published.
- **Empirical:** parallel LZ77 verified against sequential parsers on standard corpora (Pizza&Chili, Silesia) for $n$ up to $\sim 10^{10}$ bytes in external-memory/distributed settings.

## 5. Principal Obstacles

- **Greedy dependence is a long chain.** The parse is the orbit of $S$; a priori the chain has length $z$, which can be $\Theta(n/\log_\sigma n)$. Any algorithm must decouple "where phrases start" from "how long they are". The standard escape — compute $\mathrm{LPF}[i]$ for *all* $i$, then chain — spends $\Theta(n)$ work regardless of $z$, which is why (Q2) resists.
- **Derandomizing suffix construction.** The $O(\log n)$-depth, $O(n)$-work suffix tree of Farach–Muthukrishnan uses randomized hashing for character-set naming. Deterministic naming schemes (radix sort over a $\mathrm{polylog}$-size alphabet, deterministic coin tossing) cost an extra $\log$ factor in depth or work; no deterministic $O(\log n)$-depth linear-work suffix array is known even in isolation. Q1 is thus at least as hard as an open problem in parallel suffix sorting.
- **Packed inputs break the RAM/PRAM correspondence.** Sublinear sequential algorithms exploit word-packed $\Theta(\log_\sigma n)$-character blocks and precomputed tables. In the PRAM, table lookups are fine but the *irregular* block boundaries induced by string synchronizing sets create load imbalance whose depth cost has not been bounded.
- **P-completeness is a hard wall for LZ78.** The reduction encodes a circuit's gate evaluation into dictionary growth: phrase $k$'s existence depends on the entire dictionary at step $k-1$. Neither speculative parallel execution nor block decomposition helps, because the dictionary is global state with no locality. Techniques that work for LZ77 (suffix structures, ANSV) have no LZ78 analogue: LZ78 phrases are not substrings determined by the text alone but by the parse history.
- **Approximation hardness is unmapped.** For (Q3) there is no known reduction showing constant-factor approximation is P-hard, and no NC algorithm; the standard NC toolkit (parallel prefix, tree contraction, matrix powering) offers no handle on a monotonically growing trie.

## 6. The Gap

Proven (Section 4) is: *randomized* $O(\log n)$ depth with $O(n)$ work, and *deterministic* $O(\log^2 n)$ depth with $O(n)$ work. The general statement (Q1) asks for both at once. The precise missing step is a **deterministic, work-optimal, $O(\log n)$-depth construction of a suffix-order structure sufficient for $\mathrm{LPF}$** — either a suffix array/tree, or a weaker object (nearest-smaller-suffix pointers, or a string synchronizing set with LCE queries) that suffices. For (Q2), the gap is that every known parallel parser reads all $n$ characters individually; nothing shows $\Omega(n)$ work is necessary, and nothing achieves $o(n)$. For (Q3), the gap is between "exact is P-complete" and "constant-factor is unclassified" — no reduction and no algorithm.

## 7. Current Research (as of June 2026)

- **Synchronizing-set parallelism.** Groups around Kempa (Johns Hopkins) and Kociumaka (MPI-INF Saarbrücken) are pushing string synchronizing sets into parallel and compressed-space settings; a parallel LZ77 in $O(z\,\mathrm{polylog}\,n)$ work given a compressed index is the stated target *(frontier — verify)*.
- **Practical shared-memory / GPU.** Continuation of Shun's line (Berkeley/CMU parlaylib ecosystem) and Kärkkäinen–Kempa–Puglisi (Helsinki) on external-memory and distributed parsing; GPU LZ77 work reports throughput gains but no improved depth bound.
- **Recompression and grammar routes.** Jeż's recompression yields a naturally parallel $O(\log(n/g^*))$-approximation grammar; converting a grammar back to an exact LZ77 parse in polylog depth is an active question *(frontier — verify)*.
- **Approximation complexity of LZ78.** Small activity, mainly De Agostino's continued work on bounded-memory dictionary parsers with provable ratios in distributed models.

## 8. Future Work

- Derandomize Farach–Muthukrishnan by replacing hashing with deterministic $\log$-depth naming over difference covers; a positive answer resolves (Q1).
- Prove a conditional depth lower bound for deterministic LZ77 — e.g. reduce from a problem believed to require $\Omega(\log^2 n)$ deterministic EREW depth.
- Design an *output-sensitive* parallel parser with $O(z\,\mathrm{polylog}\,n + n/\log_\sigma n)$ work, which would settle (Q2) for highly repetitive inputs where $z \ll n$.
- Settle (Q3) by either an NC $c$-approximation for LZ78, or a P-hardness result for $c$-approximation via a gap-preserving circuit reduction.
- Extend to LZ-End and LZ77 with bounded window $w = n^{\varepsilon}$, where neither NC membership nor P-hardness is established.

## 9. Key References

- **[Foundational]** J. Ziv, A. Lempel. *A Universal Algorithm for Sequential Data Compression.* IEEE Transactions on Information Theory 23(3):337–343, 1977.
- **[Foundational]** J. Ziv, A. Lempel. *Compression of Individual Sequences via Variable-Rate Coding.* IEEE Transactions on Information Theory 24(5):530–536, 1978.
- **[Foundational]** M. Crochemore, W. Rytter. *Efficient Parallel Algorithms to Test Square-Freeness and Factorize Strings.* Information Processing Letters 38(2):57–60, 1991.
- **[Foundational]** S. De Agostino. *P-complete Problems in Data Compression.* Theoretical Computer Science 127(1):181–186, 1994.
- **[Foundational]** O. Berkman, B. Schieber, U. Vishkin. *Optimal Doubly Logarithmic Parallel Algorithms Based on Finding All Nearest Smaller Values.* Journal of Algorithms 14(3):344–370, 1993.
- **[SOTA / Recent]** M. Farach, S. Muthukrishnan. *Optimal Parallel Dictionary Matching and Compression.* Proc. 7th ACM Symposium on Parallel Algorithms and Architectures (SPAA), 244–253, 1995.
- **[SOTA / Recent]** J. Kärkkäinen, P. Sanders, S. Burkhardt. *Linear Work Suffix Array Construction.* Journal of the ACM 53(6):918–936, 2006.
- **[SOTA / Recent]** M. Crochemore, L. Ilie. *Computing Longest Previous Factor in Linear Time and Applications.* Information Processing Letters 106(2):75–80, 2008.
- **[SOTA / Recent]** J. Shun, F. Zhao. *Practical Parallel Lempel-Ziv Factorization.* Proc. IEEE Data Compression Conference (DCC), 123–132, 2013.
- **[SOTA / Recent]** J. Kärkkäinen, D. Kempa, S. J. Puglisi. *Linear Time Lempel-Ziv Factorization: Simple, Fast, Small.* Proc. CPM 2013, LNCS 7922, 189–200.
- **[SOTA / Recent]** J. Fischer, T. Gagie, P. Gawrychowski, T. Kociumaka. *Approximating LZ77 via Small-Space Multiple-Pattern Matching.* Proc. ESA 2015, LNCS 9294, 533–544.
- **[SOTA / Recent]** D. Kempa, T. Kociumaka. *String Synchronizing Sets: Sublinear-Time BWT Construction and Optimal LCE Data Structure.* Proc. 51st ACM STOC, 756–767, 2019.
- **[SOTA / Recent]** J. Ellert. *Sublinear Time Lempel-Ziv (LZ77) Factorization.* Proc. SPIRE 2023, LNCS 14240, 171–187.
- **[Survey]** R. Greenlaw, H. J. Hoover, W. L. Ruzzo. *Limits to Parallel Computation: P-Completeness Theory.* Oxford University Press, 1995.
- **[Survey]** J. Shun. *Shared-Memory Parallelism Can Be Simple, Fast, and Scalable.* ACM Books \#15, Association for Computing Machinery / Morgan & Claypool, 2017.
- **[Survey]** W. Rytter. *Application of Lempel–Ziv Factorization to the Approximation of Grammar-Based Compression.* Theoretical Computer Science 302(1–3):211–222, 2003.
- **[Survey]** M. Charikar, E. Lehman, D. Liu, R. Panigrahy, M. Prabhakaran, A. Sahai, A. Shelat. *The Smallest Grammar Problem.* IEEE Transactions on Information Theory 51(7):2554–2576, 2005.

## 10. Worked Example / Concrete Special Case

Take $T = \texttt{abbaabbaab}$, $n = 10$, positions $1..10$.

**Step 1 — LPF at each phrase start.**

| $i$ | $T[i..]$ | witness $j<i$ | $\mathrm{LPF}[i]$ |
|---|---|---|---|
| 1 | `abbaabbaab` | — | 0 |
| 2 | `bbaabbaab` | — | 0 |
| 3 | `baabbaab` | $j=2$ (`b`) | 1 |
| 4 | `aabbaab` | $j=1$ (`a`) | 1 |
| 5 | `abbaab` | $j=1$ | 6 |

At $i=3$: `ba` would need $j<3$ with $T[j..j+1]=\texttt{ba}$; only `ab`, `bb` occur, so $\mathrm{LPF}[3]=1$. At $i=4$: `aa` needs an earlier `aa`; none, so $\mathrm{LPF}[4]=1$. At $i=5$: $T[1..6] = \texttt{abbaab} = T[5..10]$, and the source $[1,6]$ **overlaps** the target $[5,10]$ — legal in the self-referential model — giving $\mathrm{LPF}[5]=6$.

**Step 2 — orbit of $S(i) = i + \max(1,\mathrm{LPF}[i])$.**
$$1 \mapsto 2 \mapsto 3 \mapsto 4 \mapsto 5 \mapsto 11 > n.$$
So $z = 5$ and the parse is
$$(0,\texttt{a}),\ (0,\texttt{b}),\ (2,1),\ (1,1),\ (1,6).$$

**Step 3 — where parallelism bites.** The chain $1\to2\to3\to4\to5$ is a path in the forest induced by $S$; pointer jumping resolves it in $\lceil\log_2 5\rceil = 3$ rounds, and tree contraction does it in $O(n)$ total work. That part parallelizes cleanly. The cost sits in Step 1: computing $\mathrm{LPF}[5]=6$ requires knowing that suffix $5$'s nearest suffix-array neighbour with a smaller text position is suffix $1$, and that their LCP is $6$. Deterministically, obtaining $\mathrm{SA}$ and $\mathrm{LCP}$ for this $n=10$ instance in linear work costs $O(\log^2 n)$ depth via skew recursion; randomized hashing collapses it to $O(\log n)$. Scaling this table to $n = 10^{10}$ is exactly where the open gap of Section 6 becomes the practical bottleneck: the $\log n$ factor in depth, and the fact that all $10^{10}$ entries of $\mathrm{LPF}$ are computed even though a repetitive text may have $z < 10^6$ phrases.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*