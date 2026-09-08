---
id: 10-theoretical-cs/explicit-ramsey-graph-construction
title: "Ramsey Graph Construction Explicitness"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ramsey Graph Construction Explicitness

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/explicit-ramsey-graph-construction` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Erdős (1947) proved by a counting argument that for every $N$ there exists a graph on $N$ vertices with no clique and no independent set of size $2\log_2 N$. No known deterministic algorithm produces such a graph. The open problem:

> **Explicit Ramsey graph construction.** Give a deterministic polynomial-time algorithm that, on input $1^N$, outputs the adjacency matrix of a graph $G_N$ on $N$ vertices with
> $$\max\big(\omega(G_N),\ \alpha(G_N)\big) \le C\log N$$
> for an absolute constant $C$, matching the probabilistic bound up to a constant factor.

A complete solution is an algorithm plus a proof of the clique/independence bound. Weaker milestones — replacing $C\log N$ by $(\log N)^{C}$, by $2^{(\log\log N)^{C}}$, or by $N^{o(1)}$ — are partial results, and the first two have now been achieved, which is why this entry is marked **partially-solved**. The *strong* form asks for a **strongly explicit** graph: adjacency of vertices $u,v$ decidable in time $\mathrm{poly}(\log N)$. The bipartite form asks for a bipartite graph on $N+N$ vertices with no $K\times K$ complete or empty bipartite subgraph; it is equivalent to constructing two-source extractors/dispersers and is strictly harder in general.

## 2. Mathematical Foundations

**Ramsey graphs.** $G$ on $N$ vertices is *$K$-Ramsey* if $\omega(G)<K$ and $\alpha(G)<K$. Equivalently, no $K$-subset of $V(G)$ is homogeneous. The Ramsey number $R(k,k)$ is the least $N$ such that no $k$-Ramsey graph on $N$ vertices exists; Erdős's bound is
$$R(k,k) > 2^{k/2},\qquad\text{improved to } R(k,k) \ge (1+o(1))\frac{k}{e\sqrt2}\,2^{k/2}\ \ \text{(Spencer 1975).}$$

**Explicitness.** $\{G_N\}$ is *explicit* if the $N\times N$ adjacency matrix is computable in time $\mathrm{poly}(N)$, and *strongly explicit* if the predicate $(u,v)\mapsto[uv\in E]$ is computable in time $\mathrm{poly}(\log N)$ for $u,v\in\{0,1\}^{n}$, $N=2^{n}$.

**Extractor formulation.** For a random variable $X$ on $\{0,1\}^n$, the min-entropy is
$$H_\infty(X) = \min_{x}\log_2\frac{1}{\Pr[X=x]}.$$
A function $\mathsf{Ext}\colon\{0,1\}^n\times\{0,1\}^n\to\{0,1\}$ is a *two-source extractor for entropy $k$ with error $\varepsilon$* if for all independent $X,Y$ with $H_\infty(X),H_\infty(Y)\ge k$,
$$\big|\Pr[\mathsf{Ext}(X,Y)=1]-\tfrac12\big|\le\varepsilon .$$
A *two-source disperser* only requires $\mathsf{Ext}(X,Y)$ to be non-constant on the support. The dictionary is exact:

$$\mathsf{Ext}\ \text{a two-source disperser for entropy }k \iff \text{the bipartite graph } E=\{(x,y):\mathsf{Ext}(x,y)=1\} \text{ is } (2^k)\text{-Ramsey bipartite}.$$

Setting $K=2^k$ and $N=2^n$: entropy $k=O(\log n)$ corresponds to $K=\mathrm{poly}(\log N)$; $k=O(1)+\log n$ would give $K=O(\log N)$, the target of Section 1.

**Frankl–Wilson algebra.** For a prime $p$ and $m$, let $V$ be the family of $(p^2-1)$-subsets of $[m]$, with $A\sim B$ iff $|A\cap B|\equiv -1 \pmod p$. The modular Ray-Chaudhuri–Wilson inequality bounds any homogeneous family by $\binom{m}{p-1}$.

## 3. History & State of the Art (SOTA)

- **1947.** Erdős's probabilistic proof of $R(k,k)>2^{k/2}$; he repeatedly offered money for a constructive counterpart, and the problem became the canonical example of the gap between existence and construction.
- **1981.** Frankl and Wilson give the first construction beating all algebraic predecessors (Paley graphs, Kneser-type graphs): $K = \exp\!\big(\Theta(\sqrt{\log N\log\log N})\big)$. Alon (1998) and Grolmusz (2000) give alternative constructions with the same or comparable bound via low-rank matrices over $\mathbb{Z}_m$.
- **2005–2010.** Barak, Kindler, Shaltiel, Sudakov and Wigderson build two-source dispersers for entropy rate $o(1)$, giving the first $N^{o(1)}$-Ramsey graphs — the first asymptotic improvement over Frankl–Wilson in 25 years. Bourgain's 2005 two-source extractor for entropy rate $0.4999n$ was the key analytic input (sum-product estimates in $\mathbb{F}_p$).
- **2012.** Barak, Rao, Shaltiel, Wigderson, *Annals of Mathematics*: dispersers for $n^{o(1)}$ entropy, $K=N^{o(1)}$.
- **2016.** Chattopadhyay and Zuckerman (STOC 2016; *Annals of Mathematics* 2019) construct two-source extractors for polylogarithmic min-entropy using resilient functions and non-malleable extractors, yielding
$$K = 2^{(\log\log N)^{O(1)}},$$
a super-polynomial improvement. Cohen (2016) obtained comparable disperser bounds independently by different means; Li, and Ben-Aroya–Doron–Ta-Shma, then reduced the entropy to $O(\log n\log\log n)$.
- **2023.** Xin Li (FOCS 2023) constructs two-source extractors for min-entropy $O(\log n)$, i.e. explicit Ramsey graphs with
$$K = (\log N)^{O(1)},$$
within a *polynomial* of the optimal $2\log N$. This is the current SOTA and the strongest form of "explicit" known (strongly explicit, since the extractor is a $\mathrm{poly}(n)$-time predicate).

Separately, on the *numerical* Ramsey front: Campos, Griffiths, Morris and Sahasrabudhe (2023) proved $R(k,k)\le(4-\varepsilon)^k$ with $\varepsilon=2^{-7}$, later improved to about $3.8^k$ by Gupta, Ndiaye, Norin and Wei (2024). These are existence bounds and do not bear on explicitness.

## 4. Partial Results / Verified Cases

| Construction | Year | $K$ (clique/independence bound) | Type |
|---|---|---|---|
| Paley graph $\mathbb{F}_q$ | classical | $\Theta(\sqrt N)$ | strongly explicit |
| Frankl–Wilson | 1981 | $\exp(\Theta(\sqrt{\log N\log\log N}))$ | strongly explicit |
| Grolmusz (mod-6 rank) | 2000 | $\exp(\Theta(\sqrt{\log N\log\log N}))$ | explicit |
| Barak–Kindler–Shaltiel–Sudakov–Wigderson | 2010 | $N^{o(1)}$ | explicit (bipartite) |
| Barak–Rao–Shaltiel–Wigderson | 2012 | $N^{o(1)}$ | explicit (bipartite) |
| Chattopadhyay–Zuckerman | 2016/2019 | $2^{(\log\log N)^{O(1)}}$ | strongly explicit (bipartite) |
| Li | 2023 | $(\log N)^{O(1)}$ | strongly explicit (bipartite) |

Additional solved regimes:
- **Unbalanced/high-entropy sources.** Chor–Goldreich (1988): the inner product $\langle x,y\rangle \bmod 2$ is a two-source extractor whenever $k_1+k_2 > n + 2\log(1/\varepsilon)$, i.e. entropy rate $>1/2$. Bourgain (2005) broke rate $1/2$, reaching $0.4999n$; Raz (2005) handles one source of entropy rate $>1/2$ and the other of entropy $O(\log n)$.
- **Small finite cases.** $R(3,3)=6$, $R(4,4)=18$, $R(4,5)=25$ (McKay–Radziszowski 1995); $R(5,5)\in[43,46]$ after the 2024 upper-bound improvement by Angeltveit and McKay. Extremal Ramsey graphs for $k\le 4$ are known explicitly and are unique up to isomorphism at $N=R(k,k)-1$ for $k=3,4$.
- **Multicolour and bipartite variants** admit the same extractor-based bounds, with bipartite results implying the ordinary (non-bipartite) ones.

## 5. Principal Obstacles

- **Algebraic ceiling.** Polynomial/rank methods (Frankl–Wilson, Grolmusz, Paley) bound homogeneous sets through the rank of an intersection matrix of dimension $\binom{m}{p-1}$. Since the rank of any low-degree polynomial scheme is at least quasi-polynomial in the parameter, these methods cannot go below $\exp(\sqrt{\log N})$ — the barrier is structural, not a matter of tuning parameters.
- **Character sums saturate at rate $1/2$.** Analytic proofs (inner product, Paley) bound $|\sum_{x,y}(-1)^{\langle x,y\rangle}f(x)g(y)|$ by a singular-value/Weil-type estimate, which cannot beat entropy $n/2$: this is the well-documented "$1/2$ barrier" for two-source extractors, evaded only by sum-product and later by combinatorial (resilient-function) machinery.
- **Error versus entropy.** The Chattopadhyay–Zuckerman route uses non-malleable extractors plus resilient functions (Ajtai–Linial-type). Resilient functions are only *weakly* unbiased: they give constant, not exponentially small, error. Pushing $K$ to $O(\log N)$ apparently requires error $o(1)$ at entropy $k=\log n+O(1)$, where every known non-malleable extractor breaks down.
- **Loss in the entropy accounting.** Each composition step (condensing, non-malleable extraction, correlation breaking) loses an additive $\Omega(\log n)$ or multiplicative constant of entropy. Reaching $k=\log n+O(1)$ leaves no slack for a single such step, so the current modular architecture cannot be optimised into the target.
- **No derandomisation route.** The probabilistic proof is a union bound over $\binom{N}{K}$ sets; derandomising it by conditional expectations requires evaluating a quantity that is itself $\mathrm{\\#P}$-hard-looking. Even deciding $\omega(G)<K$ for a *given* explicit $G$ is coNP-hard in general, so verification of a candidate construction must come from the construction's own algebraic structure.

## 6. The Gap

Proven: strongly explicit graphs with $K=(\log N)^{c}$ for some unspecified constant $c$ (Li 2023). Target: $K=O(\log N)$, i.e. $c=1$ with a constant factor. The precise missing step is a **two-source extractor (or even disperser) for min-entropy $k=\log n + O(1)$** on $n$-bit sources, with error bounded away from $1/2$ — equivalently, removing the polynomial slack $2^{O(\log n)}$ down to $2^{\log n+O(1)}$. A non-explicit extractor exists at $k=\log n+O(1)$ by the probabilistic method, so the gap is purely constructive. A secondary gap: even the *value* of the exponent $c$ in Li's construction is not optimised in the literature *(frontier — verify)*.

## 7. Current Research (as of June 2026)

- **Johns Hopkins (Li) and UT Austin (Zuckerman, Chattopadhyay's collaborators).** Continued refinement of correlation breakers, non-malleable extractors and low-error two-source extractors; the stated goal is error $2^{-\Omega(k)}$ at entropy $O(\log n)$, which would additionally yield strong bipartite Ramsey graphs and improved privacy amplification protocols *(frontier — verify)*.
- **Weizmann / IAS lineage (Wigderson, Shaltiel, Ta-Shma, Ben-Aroya, Doron).** Seeded-extractor-based and Ramanujan-graph-based approaches; the "few-bit-output at low entropy" question.
- **Additive combinatorics.** Sum-product and incidence bounds in $\mathbb{F}_p$ and in $\mathbb{Z}_m$ as inputs to extractors; connections to the polynomial Freiman–Ruzsa theorem, proved in 2023 by Gowers, Green, Manners and Tao, which has been suggested as an ingredient for improved affine and two-source extractors *(frontier — verify)*.
- **Structural Ramsey-graph theory.** Work of Bukh, Sudakov, Kwan, Sah, Sawhney and Simkin on the induced-subgraph richness of $K$-Ramsey graphs (Erdős–Hajnal-type statements), which constrains what any explicit construction must look like.
- **Numerical Ramsey bounds.** The $(4-\varepsilon)^k$ programme (Cambridge/Oxford) and its book-algorithm refinements continue but are orthogonal to explicitness.

## 8. Future Work

1. **Low-error two-source extractors at logarithmic entropy.** Replace the resilient-function bottleneck with an object achieving error $n^{-\omega(1)}$ at $k=O(\log n)$.
2. **Direct algebraic constructions.** Find a Frankl–Wilson-style graph whose homogeneous-set bound is proved by a rank argument over a *large* field or over $\mathbb{Z}_m$ for composite $m$ with many factors, aiming to break the $\exp(\sqrt{\log N})$ ceiling within algebra rather than pseudorandomness.
3. **Hardness-to-randomness.** Ask whether $\mathrm{E}\not\subseteq \mathrm{SIZE}(2^{o(n)})$ (or a similar assumption) implies optimal explicit Ramsey graphs; unlike standard derandomisation, two-source extraction is not known to follow from circuit lower bounds, and settling this either way would be informative.
4. **Non-bipartite shortcuts.** Since the non-bipartite problem is formally easier, look for constructions exploiting self-complementary or Cayley structure with no bipartite analogue.
5. **Lower bounds on explicit techniques.** Formalise a barrier showing that rank-based or degree-$d$ polynomial constructions cannot beat a specified $K$.

## 9. Key References

- **[Foundational]** P. Erdős. *Some remarks on the theory of graphs.* Bulletin of the AMS 53 (1947), 292–294.
- **[Foundational]** P. Frankl, R. M. Wilson. *Intersection theorems with geometric consequences.* Combinatorica 1 (1981), 357–368.
- **[Foundational]** B. Chor, O. Goldreich. *Unbiased bits from sources of weak randomness and probabilistic communication complexity.* SIAM Journal on Computing 17(2) (1988), 230–261.
- **[Foundational]** J. Spencer. *Ramsey's theorem — a new lower bound.* Journal of Combinatorial Theory, Series A 18 (1975), 108–115.
- **[SOTA / Recent]** X. Li. *Two-source extractors for asymptotically optimal entropy, and (many) more.* Proc. 64th IEEE Symposium on Foundations of Computer Science (FOCS), 2023.
- **[SOTA / Recent]** E. Chattopadhyay, D. Zuckerman. *Explicit two-source extractors and resilient functions.* Annals of Mathematics 189(3) (2019), 653–705. (Conference version: STOC 2016.)
- **[SOTA / Recent]** B. Barak, A. Rao, R. Shaltiel, A. Wigderson. *2-source dispersers for $n^{o(1)}$ entropy, and Ramsey graphs beating the Frankl–Wilson construction.* Annals of Mathematics 176(3) (2012), 1483–1543.
- **[SOTA / Recent]** M. Campos, S. Griffiths, R. Morris, J. Sahasrabudhe. *An exponential improvement for diagonal Ramsey.* arXiv:2303.09521, 2023.
- **[Related]** N. Alon. *The Shannon capacity of a union.* Combinatorica 18(3) (1998), 301–310.
- **[Related]** V. Grolmusz. *Low rank co-diagonal matrices and Ramsey graphs.* Electronic Journal of Combinatorics 7 (2000), R15.
- **[Related]** J. Bourgain. *More on the sum-product phenomenon in prime fields and its applications.* International Journal of Number Theory 1 (2005), 1–32.
- **[Survey]** S. Radziszowski. *Small Ramsey Numbers.* Electronic Journal of Combinatorics, Dynamic Survey DS1 (revised periodically).
- **[Survey]** S. Vadhan. *Pseudorandomness.* Foundations and Trends in Theoretical Computer Science 7(1–3) (2012), 1–336.

## 10. Worked Example / Concrete Special Case

**The Paley graph $P_{17}$ as an extremal $4$-Ramsey graph.** Take $V=\mathbb{F}_{17}$ and join $u\sim v$ iff $u-v$ is a nonzero quadratic residue. The residues mod $17$ are
$$QR = \{1,2,4,8,9,13,15,16\},$$
a set closed under negation ($-1=16\in QR$ since $17\equiv1\pmod 4$), so the graph is well defined and $8$-regular.

*Clique number.* Suppose $\{a,b,c,d\}$ is a clique. Translating and scaling by an element of $QR$ (both are graph automorphisms) we may assume $a=0$ and $b=1$. The common neighbours of $0$ and $1$ are $x\in QR$ with $x-1\in QR$: checking $x=2\ (1\in QR)$, $x=9\ (8\in QR)$, $x=16\ (15\in QR)$ gives $\{2,9,16\}$; the others fail ($4-1=3\notin QR$, $8-1=7\notin QR$, $13-1=12\notin QR$, $15-1=14\notin QR$). Now $9-2=7\notin QR$, $16-2=14\notin QR$, $16-9=7\notin QR$, so no two of $\{2,9,16\}$ are adjacent. Hence $\omega(P_{17})=3$. Because $x\mapsto gx$ for a non-residue $g$ is an isomorphism $P_{17}\to\overline{P_{17}}$, also $\alpha(P_{17})=3$.

So $P_{17}$ is $4$-Ramsey on $17$ vertices, certifying $R(4,4)\ge18$; McKay–Radziszowski's search shows it is the unique such graph and $R(4,4)=18$.

*Why this does not scale.* For general prime $q\equiv1\pmod4$, Weil's bound gives $\omega(P_q)=\alpha(P_q)\le\sqrt q$, and no better bound is known — $K=\Theta(\sqrt N)$. The optimal target at $N=17$ is $2\log_2 17\approx 8.2$, so at this tiny size Paley is *better* than the generic bound; but at $N=2^{100}$ Paley gives $K\approx2^{50}$ where the probabilistic bound gives $K=200$, and Li's construction gives $K=\mathrm{poly}(100)$. The chain
$$\Theta(\sqrt N)\ \longrightarrow\ e^{\Theta(\sqrt{\log N\log\log N})}\ \longrightarrow\ N^{o(1)}\ \longrightarrow\ 2^{(\log\log N)^{O(1)}}\ \longrightarrow\ (\log N)^{O(1)}\ \longrightarrow\ ?\ O(\log N)$$
is exactly the history of the problem, with the last arrow open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*