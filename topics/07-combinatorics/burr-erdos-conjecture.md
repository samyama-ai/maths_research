---
id: 07-combinatorics/burr-erdos-conjecture
title: "Burr-Erdős Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Burr-Erdős Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/burr-erdos-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Burr and Erdős (1975) conjectured that **sparse graphs have linear Ramsey numbers**, with sparseness measured by degeneracy:

> For every integer $d \ge 1$ there is a constant $c(d)$ such that every $d$-degenerate graph $G$ on $n$ vertices satisfies $r(G) \le c(d)\, n$.

Here $r(G)$ is the least $N$ such that every red/blue colouring of the edges of $K_N$ contains a monochromatic copy of $G$. A complete proof must supply, for each fixed $d$, a finite $c(d)$ valid for *all* $d$-degenerate $G$ simultaneously; a disproof would exhibit a fixed $d$ and a sequence $G_1, G_2, \dots$ of $d$-degenerate graphs with $|V(G_i)| = n_i \to \infty$ and $r(G_i)/n_i \to \infty$.

The conjecture was **proved by Choongbum Lee** in *Ramsey numbers of degenerate graphs*, Annals of Mathematics **185** (2017), 791–829. The page is retained as `solved-recently` because the quantitative form — the true growth rate of $c(d)$, and the multicolour/off-diagonal analogues — remains wide open.

## 2. Mathematical Foundations

**Degeneracy.** A graph $G$ is $d$-**degenerate** if every subgraph $H \subseteq G$ has a vertex of degree at most $d$:
$$\mathrm{degen}(G) = \max_{H \subseteq G}\ \min_{v \in V(H)} \deg_H(v) \le d .$$
Equivalently there is an ordering $v_1, \dots, v_n$ of $V(G)$ with
$$\bigl|\{\, j < i : v_jv_i \in E(G) \,\}\bigr| \le d \quad \text{for all } i,$$
the *back-degree* condition. Degeneracy is the strongest of the usual local-sparseness parameters in the sense that
$$\mathrm{degen}(G) \le \Delta(G), \qquad \chi(G) \le \mathrm{degen}(G) + 1, \qquad e(H) \le d\,|V(H)| \ \ \forall H \subseteq G .$$
Forests are exactly the $1$-degenerate graphs; planar graphs are $5$-degenerate; $K_{d+1}$ and the hypercube $Q_d$ are $d$-degenerate.

**Ramsey number.** $r(G) = \min\{N : K_N \to (G,G)\}$, where $K_N \to (G,G)$ means every $2$-colouring of $E(K_N)$ yields a monochromatic $G$. Multicolour: $r_k(G) = \min\{N: K_N \to (G)_k\}$.

**Lower bound.** Since a $d$-degenerate $G$ on $n$ vertices has $\chi(G) \le d+1$ and may contain $K_{d+1}$, the Chvátal–Harary/Burr–Erdős lower bound gives
$$r(G) \ \ge\ \bigl(\chi(G)-1\bigr)\bigl(n-1\bigr)+1 \ \ge\ d(n-1)+1,$$
so linearity in $n$ is the best possible order. Graham, Rödl and Ruciński (2001) constructed $d$-degenerate (indeed $\Delta$-bounded bipartite) graphs with
$$r(G) \ \ge\ 2^{c d}\, n,$$
so $c(d)$ must be at least exponential in $d$.

**Arrangeability** (Chen–Schelp). $G$ is $p$-*arrangeable* if there is an ordering $v_1,\dots,v_n$ such that for each $i$,
$$\Bigl|\ N(\{v_j : j > i\}) \cap \{v_1,\dots,v_{i}\}\ \Bigr| \le p \quad\text{(neighbourhoods taken through } v_i\text{)},$$
i.e. the neighbours-to-the-left of the later neighbours of $v_i$ number at most $p$. Arrangeability strengthens degeneracy ($p$-arrangeable $\Rightarrow$ $p$-degenerate) and was the vehicle for all pre-2017 progress.

**Theorem (Lee 2017).** For every $d$ there is $c(d) < \infty$ with $r(G) \le c(d) n$ for all $d$-degenerate $n$-vertex $G$; the proof also gives the multicolour bound $r_k(G) \le c(d,k)n$. The constant extracted from the argument is doubly exponential, $c(d) = 2^{2^{O(d)}}$.

## 3. History & State of the Art (SOTA)

- **1975.** Burr and Erdős, *On the magnitude of generalized Ramsey numbers for graphs*, pose the conjecture together with the weaker question for graphs of bounded average degree (which they disproved) and for bounded maximum degree.
- **1983.** Chvátal, Rödl, Szemerédi and Trotter prove $r(G) \le c(\Delta)n$ for graphs of maximum degree $\Delta$ — the first application of Szemerédi's regularity lemma to Ramsey theory. Regularity forces $c(\Delta)$ to be tower-type.
- **1993.** Chen and Schelp prove $r(G) \le c(p) n$ for $p$-arrangeable graphs, covering planar graphs.
- **1997.** Rödl and Thomas show graphs with no $K_p$-subdivision are $p'$-arrangeable, hence have linear Ramsey numbers.
- **2000–2001.** Graham, Rödl, Ruciński give regularity-free proofs with $c(\Delta) = 2^{O(\Delta \log^2 \Delta)}$ (bipartite case: $2^{O(\Delta\log\Delta)}$) and the matching lower bound $2^{\Omega(\Delta)}$.
- **2001–2003.** Kostochka and Rödl obtain the first general sub-polynomial-exponent bounds for $d$-degenerate graphs; Kostochka and Sudakov prove $r(G) \le n^{1+o(1)}$ for fixed $d$.
- **2009.** Fox and Sudakov (*Two remarks on the Burr–Erdős conjecture*) reach $r(G) \le 2^{O(\sqrt{\log n})} n$ for fixed $d$, and prove the conjecture for $d$-degenerate graphs of bounded "local" structure via dependent random choice.
- **2012.** Conlon, Fox and Sudakov sharpen the bounded-degree constant to $c(\Delta) = 2^{O(\Delta \log \Delta)}$.
- **2017.** **Lee** proves the conjecture in full. The method combines a greedy/embedding scheme robust to unbounded degrees with a weighted "density-increment" argument, avoiding regularity entirely.

## 4. Partial Results / Verified Cases

Cases settled before (and independently of) the general theorem, with explicit parameters:

| Class | Parameter | Bound |
|---|---|---|
| Trees / forests | $d = 1$ | $r(T) \le 4n$ (greedy; see §10); $r(T_n,K_m)=(n-1)(m-1)+1$ exactly, Chvátal 1977 |
| Bounded maximum degree | $\Delta$ fixed | $r(G) \le 2^{O(\Delta\log\Delta)}n$ (Conlon–Fox–Sudakov 2012); lower bound $2^{\Omega(\Delta)}n$ |
| Bounded-degree bipartite | $\Delta$ fixed | $r(G) \le 2^{O(\Delta)}n$ (Conlon 2009 / Fox–Sudakov 2009) — order of magnitude of the exponent is tight |
| $p$-arrangeable | $p$ fixed | $r(G) \le c(p)n$ (Chen–Schelp 1993) |
| Planar graphs | $d = 5$, arrangeability $\le 10$ | linear; recent explicit constants of order $10^5 n$ *(frontier — verify)* |
| No $K_p$-subdivision | $p$ fixed | arrangeable, hence linear (Rödl–Thomas 1997) |
| Subdivisions of arbitrary graphs | $d = 2$ | linear, with polynomial constants |
| General $d$-degenerate | all $d$ | $r(G) \le c(d)n$, $c(d)=2^{2^{O(d)}}$ (Lee 2017) |

Growing-degeneracy cases remain unresolved: for the hypercube $Q_n$ ($2^n$ vertices, degeneracy $n$) Burr and Erdős asked whether $r(Q_n) = O(2^n)$; the best bound is $2^{(2-c)n}$ for a small constant $c>0$ (Tikhomirov, 2022) *(frontier — verify)*.

## 5. Principal Obstacles

- **Regularity is degree-blind but constant-blind.** The Chvátal–Rödl–Szemerédi–Trotter embedding places vertices one at a time into regular pairs; each placed vertex shrinks the candidate set of its neighbours by a factor $\approx \varepsilon$. With $\Delta$ bounded this is affordable; with degeneracy only, a single vertex may have $\Theta(n)$ neighbours, and no regular pair survives $\Theta(n)$ restrictions. Additionally the regularity lemma yields tower-type constants, so even where it applies it cannot give sharp $c(d)$.
- **Greedy embedding breaks at $d \ge 2$.** For forests one only needs large minimum degree. For $d$-degenerate graphs, embedding $v_i$ requires a common neighbourhood of $d$ already-embedded vertices to remain large; in a general dense host graph, common neighbourhoods of $d$ vertices can be empty (e.g. a random-like graph with density just below the threshold).
- **No absorbing/hypergraph-container substitute.** Container and absorption methods control *counts* of copies, but Ramsey statements need an embedding into *one* of two colour classes with no density hypothesis on either beyond $\ge 1/2$ of the edges.
- **Dependent random choice saturates.** Fox–Sudakov's method finds a large set whose $d$-subsets all have big common neighbourhoods, but the quality degrades with the number of embedded vertices, which caps the argument at $2^{O(\sqrt{\log n})}n$ — sub-polynomial, never linear.
- **Adversarial colourings mix scales.** Colourings built from random blow-ups of small Ramsey-critical graphs force any proof to handle a hierarchy of densities at once; Lee's resolution is a multi-scale weighting, and it is exactly this bookkeeping that inflates $c(d)$ to doubly exponential.

## 6. The Gap

The existential gap of §1 is closed. What remains is quantitative:
$$2^{\Omega(d)} \ \le\ c(d) \ \le\ 2^{2^{O(d)}} .$$
The conjectured truth is $c(d) = 2^{\Theta(d)}$. Crossing from the upper to the lower side requires replacing Lee's iterated density increment (each iteration costing an exponential factor, $d$ iterations giving a double exponential) with a single-pass embedding whose loss is exponential in $d$ overall. Secondary gaps: multicolour constants $c(d,k)$ (best known towers in $k$ as well); off-diagonal $r(G,K_m)$ for $d$-degenerate $G$, where even $r(G,K_m) = O_d(n\,m^{d})$ is unproven in general; and degeneracy growing with $n$, as in $Q_n$.

## 7. Current Research (as of June 2026)

- **Sharpening $c(d)$.** The programme of Conlon, Fox and Sudakov (Caltech / MIT / ETH Zürich, Princeton) aims at $c(d) = 2^{O(d)}$, extending the sharp bipartite bounded-degree bounds to degeneracy. Partial results exist for $d$-degenerate graphs of bounded *local degeneracy* or bounded separator size *(frontier — verify)*.
- **Hypergraph analogue.** Whether $d$-degenerate $k$-uniform hypergraphs have linear Ramsey numbers is open for $k \ge 3$; bounded-degree $k$-uniform hypergraphs do (Cooley–Fountoulakis–Kühn–Osthus; Conlon–Fox–Sudakov; Nagle–Olsen–Rödl–Schacht).
- **Size Ramsey numbers.** $\hat r(G)$ for bounded-degree and degenerate $G$ — the analogous "is it linear?" question — is active (Kohayakawa, Rödl, Schacht, Szemerédi; Draganić, Krivelevich, Nenadov for paths/trees).
- **Ramsey goodness.** For which $d$-degenerate $G$ does $r(G,K_m)$ hit the trivial lower bound $(m-1)(n-1)+1$? (Nikiforov–Rousseau; recent work of Fox, He, Wigderson.)
- **Algorithmic/explicit constants.** Groups working on planar and minor-closed families are extracting concrete constants rather than $O(\cdot)$ bounds.

## 8. Future Work

1. **Single-scale embedding.** Design a random-greedy embedding for $d$-degenerate graphs whose failure probability is controlled by a single exponential in $d$ — the acknowledged route to $c(d)=2^{O(d)}$.
2. **Matching lower bounds.** Determine whether the random bipartite constructions of Graham–Rödl–Ruciński are extremal, or whether some $d$-degenerate family forces $c(d) \ge 2^{d^{1+\epsilon}}$.
3. **Degeneracy growing with $n$.** Prove $r(G) \le 2^{O(d)}n$ *uniformly in $d$*, which would settle $r(Q_n)=2^{O(n)}$ as a corollary.
4. **Off-diagonal.** Establish $r(G,K_m) = O_d(n m^{d})$, or the natural conjecture $r(G, K_m) \le c(d) n m^{d}$ for $d$-degenerate $G$.
5. **Multicolour uniformity.** Prove $c(d,k) \le c(d)^{k}$ rather than the current tower-type dependence.

## 9. Key References

- **[Foundational]** S. A. Burr and P. Erdős. *On the magnitude of generalized Ramsey numbers for graphs.* In: Infinite and Finite Sets (Colloq. Math. Soc. János Bolyai, Vol. 10), North-Holland, 1975, 214–240.
- **[Foundational]** V. Chvátal, V. Rödl, E. Szemerédi and W. T. Trotter, Jr. *The Ramsey number of a graph with bounded maximum degree.* Journal of Combinatorial Theory, Series B **34** (1983), 239–243.
- **[Foundational]** G. Chen and R. H. Schelp. *Graphs with linearly bounded Ramsey numbers.* Journal of Combinatorial Theory, Series B **57** (1993), 138–149.
- **[Structural]** V. Rödl and R. Thomas. *Arrangeability and clique subdivisions.* In: The Mathematics of Paul Erdős II, Springer, 1997, 236–239.
- **[Progress]** A. V. Kostochka and V. Rödl. *On graphs with small Ramsey numbers.* Journal of Graph Theory **37** (2001), 198–204.
- **[Progress]** R. L. Graham, V. Rödl and A. Ruciński. *On bipartite graphs with linear Ramsey numbers.* Combinatorica **21** (2001), 199–209.
- **[Progress]** A. V. Kostochka and B. Sudakov. *On Ramsey numbers of sparse graphs.* Combinatorics, Probability and Computing **12** (2003), 627–641.
- **[Progress]** J. Fox and B. Sudakov. *Two remarks on the Burr–Erdős conjecture.* European Journal of Combinatorics **30** (2009), 1630–1645.
- **[Progress]** D. Conlon, J. Fox and B. Sudakov. *On two problems in graph Ramsey theory.* Combinatorica **32** (2012), 513–535.
- **[SOTA / Resolution]** C. Lee. *Ramsey numbers of degenerate graphs.* Annals of Mathematics **185** (2017), 791–829.
- **[Survey]** D. Conlon, J. Fox and B. Sudakov. *Recent developments in graph Ramsey theory.* In: Surveys in Combinatorics 2015, London Math. Soc. Lecture Note Series **424**, Cambridge University Press, 49–118.
- **[Reference]** S. P. Radziszowski. *Small Ramsey Numbers.* Electronic Journal of Combinatorics, Dynamic Survey DS1 (revised periodically).

## 10. Worked Example / Concrete Special Case

**Claim ($d=1$).** Every tree $T$ on $n$ vertices satisfies $r(T) \le 4n$.

*Step 1 — greedy embedding.* If a graph $H$ has minimum degree $\delta(H) \ge n-1$, then $T \subseteq H$. Order $V(T) = v_1,\dots,v_n$ so that each $v_i$ ($i\ge2$) has exactly one neighbour $v_{p(i)}$ with $p(i) < i$ (back-degree $1$: this is the degeneracy ordering of a tree). Embed $v_1$ anywhere. Having embedded $v_1,\dots,v_{i-1}$ as distinct vertices $u_1,\dots,u_{i-1}$, the image $u_{p(i)}$ has at least $n-1$ neighbours in $H$, of which at most $i-2 \le n-2$ are already used; pick an unused one as $u_i$. The embedding never gets stuck.

*Step 2 — a dense monochromatic subgraph.* Colour $E(K_N)$ red/blue. One colour class, say red $R$, has at least $\tfrac12\binom{N}{2}$ edges, so its average degree is
$$\bar d(R) \ \ge\ \frac{2 \cdot \frac12\binom N2}{N} = \frac{N-1}{2}.$$
Standard fact: any graph of average degree $D$ contains a subgraph of minimum degree $\ge D/2$ (repeatedly delete any vertex of degree $< D/2$; each deletion removes fewer than $D/2$ edges while removing one vertex, so the average degree never drops, and the process cannot exhaust the vertex set). Hence $R$ has a subgraph $H$ with
$$\delta(H) \ \ge\ \frac{N-1}{4}.$$

*Step 3 — combine.* Take $N = 4n$. Then $\delta(H) \ge (4n-1)/4 > n-1$, so by Step 1 $T \subseteq H \subseteq R$: a red copy of $T$. Therefore $r(T) \le 4n$ for every $n$-vertex tree, a fully explicit instance of Burr–Erdős with $c(1) = 4$.

*Why this collapses at $d=2$.* Repeat the argument for a $2$-degenerate $G$: embedding $v_i$ now needs a common neighbour of two already-embedded images $u_a, u_b$, i.e. $|N_H(u_a)\cap N_H(u_b)| > i-2$. Minimum degree $\ge N/4$ gives only $|N(u_a)\cap N(u_b)| \ge N/2 - N \cdot \tfrac12 < 0$ in the worst case — a red graph that is a disjoint union of two cliques of size $N/2$ has minimum degree $N/2-1$ but *no* common neighbourhood across the parts, and more refined constructions (random graphs of density $1/2$ restricted to sparse pieces) defeat the count even inside one component. The whole difficulty of the Burr–Erdős conjecture, and the content of Lee's theorem, is manufacturing large common neighbourhoods for $d$ vertices simultaneously, at every scale of the colouring.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*