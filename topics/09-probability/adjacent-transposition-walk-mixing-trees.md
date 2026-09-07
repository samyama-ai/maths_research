---
id: 09-probability/adjacent-transposition-walk-mixing-trees
title: "Mixing Time of Adjacent Transposition Walks on Trees"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mixing Time of Adjacent Transposition Walks on Trees

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/adjacent-transposition-walk-mixing-trees` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $T=(V,E)$ be a finite tree with $|V|=n$. Place the labels $1,\dots,n$ on the vertices, one per vertex, and run the **interchange process** (adjacent transposition walk): each edge $e=\{u,v\}$ carries an independent rate-$1$ Poisson clock, and when $e$ rings the labels at $u$ and $v$ are swapped. The state space is the symmetric group $S_n$; the stationary law is uniform.

Write $t_{\rm mix}(T)$ for the total-variation mixing time of this process and $t_{\rm rel}(T)=\mathrm{gap}(T)^{-1}$ for the relaxation time of a **single** continuous-time random walk on $T$ with rate $1$ across each edge.

**Conjecture (Wilson-type product law for trees).** There are absolute constants $0<c<C<\infty$ such that for every tree $T$ on $n\ge 2$ vertices,
$$c\,t_{\rm rel}(T)\,\log n \;\le\; t_{\rm mix}(T)\;\le\; C\,t_{\rm rel}(T)\,\log n .$$

A complete solution requires either (i) a proof of both inequalities valid uniformly over all trees, or (ii) a sequence of trees $T_n$ for which $t_{\rm mix}(T_n)/(t_{\rm rel}(T_n)\log n)\to 0$ or $\to\infty$. A stronger form asks for the sharp constant and cutoff: does $t_{\rm mix}(T_n)\sim \tfrac12 t_{\rm rel}(T_n)\log n$ with a cutoff, as holds for the path?

## 2. Mathematical Foundations

**Generator.** For $f:S_n\to\mathbb R$,
$$(\mathcal L f)(\sigma)=\sum_{\{u,v\}\in E}\bigl[f(\sigma\circ\tau_{uv})-f(\sigma)\bigr],$$
where $\tau_{uv}$ is the transposition of $u$ and $v$. $\mathcal L$ is self-adjoint on $L^2(S_n,\mathrm{Unif})$, so the chain is reversible; its spectrum lies in $[-2|E|,0]$.

**Mixing and relaxation.** With $\mu_t^\sigma$ the law at time $t$ started from $\sigma$,
$$d(t)=\max_{\sigma\in S_n}\bigl\|\mu_t^\sigma-\mathrm{Unif}\bigr\|_{\rm TV},\qquad t_{\rm mix}=\inf\{t: d(t)\le 1/4\}.$$
Writing $0=\lambda_0<\lambda_1\le\cdots$ for the eigenvalues of $-\mathcal L$, $t_{\rm rel}^{\rm IP}=\lambda_1^{-1}$ and the standard bounds give
$$(t_{\rm rel}^{\rm IP}-1)\log\tfrac{1}{2\varepsilon}\;\le\; t_{\rm mix}(\varepsilon)\;\le\; t_{\rm rel}^{\rm IP}\log\frac{1}{\varepsilon\,\sqrt{\pi_{\min}}},\qquad \pi_{\min}=1/n! .$$
The upper bound costs $\log(n!)\asymp n\log n$, a factor $n$ more than the conjectured truth: this discrepancy is the analytic heart of the problem.

**Aldous' spectral gap identity.** The interchange process and the single walk have the *same* spectral gap:
$$\lambda_1 = \mathrm{gap}(T)=\min\Bigl\{\tfrac{\sum_{\{u,v\}\in E}(g(u)-g(v))^2}{\sum_{x\in V}g(x)^2}\;:\;\textstyle\sum_x g(x)=0,\ g\not\equiv0\Bigr\}.$$
Hence $t_{\rm rel}^{\rm IP}=t_{\rm rel}$ and the conjecture is exactly the statement $t_{\rm mix}\asymp t_{\rm rel}\log n$. For trees this identity is a theorem of Handjani and Jungreis (1996); for all weighted graphs it is the Caputo–Liggett–Richthammer theorem (2010), proved via the *octopus inequality*
$$\sum_{v\sim u} c_{uv}\,\bigl(\mathcal E_{uv}\text{-terms}\bigr)\ \succeq\ \tfrac12\sum_{v,w\sim u} c_{uv}c_{uw}\,(\cdots),$$
an operator inequality on $\mathbb R[S_n]$ that localises the Dirichlet form at a vertex $u$ and its neighbours.

**Projections.** Colouring $k$ labels black and $n-k$ white projects the interchange process onto the **symmetric exclusion process** $\mathrm{EX}(T,k)$; $k=1$ recovers the single random walk. Thus $t_{\rm mix}(T)\ge \max_k t_{\rm mix}(\mathrm{EX}(T,k))$, and lower bounds are naturally sought at $k=\lfloor n/2\rfloor$.

**Discrete-time normalisation.** If instead one edge of the $n-1$ is chosen uniformly per step, times are multiplied by $n-1$.

## 3. History & State of the Art (SOTA)

- **1981–1988.** Diaconis and Shahshahani established cutoff at $\tfrac12 n\log n$ steps for random transpositions (the complete graph); the star $K_{1,n-1}$ ("star transpositions") was treated by representation-theoretic methods with mixing at $n\log n$ steps, i.e. $\asymp\log n$ in continuous time — the first tree case.
- **1992.** Aldous conjectured the spectral gap identity, recorded in the Aldous–Fill open-problem list.
- **1996.** Handjani and Jungreis proved Aldous' conjecture for weighted trees.
- **2004.** Wilson introduced his eigenfunction lower-bound technique and proved that the adjacent transposition shuffle on the path $P_n$ needs $\Theta(n^3\log n)$ steps, with the sharp constant conjectured to be $1/(2\pi^2)$. He also conjectured that exclusion mixing should be governed by the single-particle statistics times $\log n$.
- **2010.** Caputo, Liggett and Richthammer proved the general spectral gap identity, making $t_{\rm rel}^{\rm IP}=t_{\rm rel}$ available for arbitrary trees.
- **2013.** Oliveira proved that the exclusion process on any graph mixes within an $O(\log n)$ factor of the single particle, the first general product-type upper bound.
- **2016.** Lacoin proved cutoff for the adjacent transposition shuffle on $P_n$ at $\frac{n^3\log n}{2\pi^2}$ steps, and cutoff for the exclusion process on the segment — closing the path case.
- **2020.** Hermon and Pymar sharpened the comparison with independent particles, removing logarithmic losses in broad settings.

**SOTA for trees.** Combining the gap identity with Oliveira-type comparison gives
$$c\,\max\{t_{\rm rel},\,\log n\}\ \le\ t_{\rm mix}(T)\ \le\ C\,t_{\rm rel}\,\log^{2} n$$
for all trees (the upper bound using $t_{\rm mix}^{(1)}=O(t_{\rm rel}\log n)$ for a single walk on a tree). The conjectured product law sits strictly between these.

## 4. Partial Results / Verified Cases

| Tree family | Result | Source |
|---|---|---|
| Path $P_n$ | $t_{\rm mix}=\frac{n^2\log n}{2\pi^2}(1+o(1))$ (continuous), cutoff; $t_{\rm rel}=\bigl(2(1-\cos\frac{\pi}{n})\bigr)^{-1}\sim n^2/\pi^2$ | Wilson 2004 (bounds), Lacoin 2016 (cutoff) |
| Star $K_{1,n-1}$ | $t_{\rm rel}=1$, $t_{\rm mix}\sim\log n$ with cutoff | Diaconis 1988; Flatto–Odlyzko–Wales 1985 |
| All trees, any $n$ | $\mathrm{gap}^{\rm IP}=\mathrm{gap}^{(1)}$ exactly | Handjani–Jungreis 1996 |
| Exclusion $\mathrm{EX}(P_n,k)$, all $1\le k\le n-1$ | mixing time and cutoff known, $\asymp n^2\log k$ | Lacoin 2016 |
| Bounded-degree trees of diameter $D$ with $t_{\rm rel}\asymp D^2$ | product law verified up to constants in worked families (caterpillars with $O(1)$ legs per spine vertex, via comparison with $P_n$) | Diaconis–Saloff-Coste comparison 1993 |
| Any tree | $t_{\rm mix}=O(t_{\rm rel}\log^2 n)$ and $t_{\rm mix}=\Omega(\max\{t_{\rm rel},\log n\})$ | Oliveira 2013 |

Unresolved representative cases: the complete binary tree $B_h$ ($n=2^{h+1}-1$, $t_{\rm rel}\asymp n$), where the conjecture predicts $t_{\rm mix}\asymp n\log n$ but only $O(n\log^2 n)$ is proved; and spider/broom graphs with unbalanced branch lengths.

## 5. Principal Obstacles

- **The entropy defect.** Every $L^2$ or log-Sobolev argument pays $\log|S_n|\asymp n\log n$, while the target is $\log n$. Only arguments exploiting the *product structure* of the $n$ single-particle marginals can avoid the factor $n$, and no general mechanism does this on inhomogeneous graphs.
- **No exact solvability off the path.** The path case succeeds because adjacent-transposition exclusion is exactly the symmetric simple exclusion process, integrable via the Bethe ansatz / Schütz determinantal formulas, hydrodynamic limits and monotone (censoring) couplings. Trees with branching destroy the total order needed for monotone couplings and for the height-function representation used by Wilson and Lacoin.
- **Negative dependence is not enough.** Comparison with $n$ independent walkers (Oliveira; Hermon–Pymar) yields chi-square control at the cost of a $\log n$ slack, and it degrades on graphs with a strong bottleneck — exactly the trees (binary tree, brooms) that remain open.
- **The gap identity gives no eigenfunctions.** Caputo–Liggett–Richthammer pins $\lambda_1$ but says nothing about the multiplicity structure or higher spectrum, which is what a Wilson-type lower bound needs.
- **Lower bounds are the harder half.** Wilson's method requires an eigenfunction whose statistic concentrates; on a branching tree the natural test function $\sum_x g(x)\,\mathbf 1\{\sigma(x)\in A\}$ has fluctuations of the same order as its mean unless the tree is nearly one-dimensional.

## 6. The Gap

Proven: $t_{\rm mix}\le C\,t_{\rm rel}\log^2 n$ and $t_{\rm mix}\ge c\max\{t_{\rm rel},\log n\}$ for all trees; the product law with sharp constant only for $P_n$ and $K_{1,n-1}$.

Missing: (a) removal of one $\log n$ from the upper bound, i.e. a comparison theorem that converts single-particle *relaxation* (not mixing) into interchange mixing with a single logarithmic factor; and (b) a lower bound of order $t_{\rm rel}\log n$ that does not assume a linear geometry. Note that (b) is not formal: $t_{\rm mix}\ge \max\{t_{\rm rel},\log n\}$ is elementary, but the *product* $t_{\rm rel}\log n$ requires $\log n$ independent decorrelation scales at the slow spatial mode — precisely the "coupon-collector on top of diffusion" mechanism that Lacoin verified only on the segment.

## 7. Current Research (as of June 2026)

- **Comparison and negative-dependence school** (Oliveira, Hermon, Pymar, Salez): pushing chi-square comparison with independent particles toward a clean $O(t_{\rm rel}\log n)$ bound on trees; the remaining loss is $\log\log n$-type in the best current arguments. *(frontier — verify)*
- **Cutoff programme for non-integrable geometries** (Lacoin and collaborators): transferring the segment cutoff proof to caterpillars and spiders by censoring plus a hydrodynamic profile per branch. *(frontier — verify)*
- **Octopus-inequality refinements**: attempts to extend Caputo–Liggett–Richthammer from the gap to a bound on the full spectral measure of $-\mathcal L$ restricted to low-degree representations of $S_n$.
- **Numerics**: Monte-Carlo estimates of $t_{\rm mix}/(t_{\rm rel}\log n)$ on binary trees to depth $h\le 12$ ($n\le 8191$) are consistent with a bounded ratio, but the accessible range of $\log n$ is only about $9$, too short to separate $\log n$ from $\log n\log\log n$.

## 8. Future Work

1. Prove $t_{\rm mix}=O(t_{\rm rel}\log n)$ for bounded-degree trees, where $t_{\rm rel}\asymp$ (a bottleneck quantity) is explicitly computable.
2. Establish cutoff for the complete binary tree; a positive answer would be the first cutoff result for interchange on a graph with exponential volume growth.
3. Develop a Wilson-type lower bound using the *second* eigenfunction of the tree walk (which localises on the two heaviest branches) rather than a global linear statistic.
4. Test the product law on the boundary of the tree class: what happens on trees whose gap is attained by a bottleneck ($\mathrm{gap}\asymp \Phi^2$) versus by diameter ($\mathrm{gap}\asymp D^{-2}$)? A counterexample, if one exists, is likelier in the bottleneck regime.
5. Extend to non-uniform edge rates $c_e$, where the gap identity still holds but the coupon-collector time becomes $\log n$ only under rate regularity.

## 9. Key References

- **[Foundational]** Diaconis, P. and Shahshahani, M. *Generating a random permutation with random transpositions.* Z. Wahrscheinlichkeitstheorie verw. Gebiete **57** (1981), 159–179.
- **[Foundational]** Flatto, L., Odlyzko, A. M. and Wales, D. B. *Random shuffles and group representations.* Annals of Probability **13** (1985), 154–178.
- **[Foundational]** Diaconis, P. *Group Representations in Probability and Statistics.* IMS Lecture Notes–Monograph Series 11, 1988.
- **[Foundational]** Handjani, S. and Jungreis, D. *Rate of convergence for shuffling cards by transpositions.* Journal of Theoretical Probability **9** (1996), 983–993.
- **[Foundational]** Diaconis, P. and Saloff-Coste, L. *Comparison theorems for reversible Markov chains.* Annals of Applied Probability **3** (1993), 696–730.
- **[SOTA]** Wilson, D. B. *Mixing times of lozenge tiling and card shuffling Markov chains.* Annals of Applied Probability **14** (2004), 274–325.
- **[SOTA]** Caputo, P., Liggett, T. M. and Richthammer, T. *Proof of Aldous' spectral gap conjecture.* Journal of the American Mathematical Society **23** (2010), 831–851.
- **[SOTA]** Oliveira, R. I. *Mixing of the symmetric exclusion process in terms of the corresponding single-particle random walk.* Annals of Probability **41** (2013), 871–913.
- **[SOTA]** Lacoin, H. *Mixing time and cutoff for the adjacent transposition shuffle and the simple exclusion process.* Annals of Probability **44** (2016), 1426–1487.
- **[SOTA]** Hermon, J. and Pymar, R. *The exclusion process mixes (almost) faster than independent particles.* Annals of Probability **48** (2020), 3077–3123.
- **[Related]** Alon, G. and Kozma, G. *The probability of long cycles in interchange processes.* Duke Mathematical Journal **162** (2013), 1567–1585.
- **[Survey]** Levin, D. A. and Peres, Y. *Markov Chains and Mixing Times*, 2nd edition. American Mathematical Society, 2017.
- **[Survey]** Morris, B. *The mixing time for simple exclusion.* Annals of Applied Probability **16** (2006), 615–635.

## 10. Worked Example / Concrete Special Case

Take the path $T=P_3$ with vertices $1-2-3$, so $n=3$ and the interchange process is the continuous-time walk on $S_3$ generated by $s_1=(1\,2)$ and $s_2=(2\,3)$, each at rate $1$.

**Single particle.** The generator matrix is
$$L^{(1)}=\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix},\qquad \mathrm{spec}(-L^{(1)})=\{0,\,1,\,3\},$$
so $\mathrm{gap}=1$ and $t_{\rm rel}=1$.

**Interchange process.** Decompose $L^2(S_3)$ into irreducibles. On the trivial representation $-\mathcal L$ acts as $0$. On the sign representation each $s_i$ acts as $-1$, so $-\mathcal L$ acts as $2-(-1)-(-1)=4$. On the $2$-dimensional standard representation $\rho$, put $M=\rho(s_1)+\rho(s_2)$. Then $\mathrm{tr}\,M=\chi(s_1)+\chi(s_2)=0$ and
$$M^2=2I+\rho(s_1s_2)+\rho(s_2s_1)=2I+\rho(c)+\rho(c^2)=2I-I=I,$$
since $\rho(c),\rho(c^2)$ are rotations by $\pm 120^\circ$ and sum to $2\cos(120^\circ)I=-I$. Hence $M$ has eigenvalues $\pm1$ and $-\mathcal L=2I-M$ has eigenvalues $1$ and $3$, each with multiplicity $2$ (dimension times multiplicity). Altogether
$$\mathrm{spec}(-\mathcal L)=\{0,\;1,\;1,\;3,\;3,\;4\}.$$

Two things are visible. First, $\lambda_1=1=\mathrm{gap}(P_3)$: the Handjani–Jungreis / Aldous identity, verified by hand. Second, the interchange spectrum is exactly the set of sums of distinct single-particle eigenvalues, $\{0,1,3,1+3\}$ — the "independent particles" heuristic is *exact* here, which is the structure that Oliveira's and Hermon–Pymar's comparison theorems try to recover approximately on large graphs.

**Mixing.** Since $d(t)^2\le\frac14\sum_{i\ge1}e^{-2\lambda_i t}=\frac14(2e^{-2t}+2e^{-6t}+e^{-8t})$, one gets $d(t)\le 1/4$ for $t\ge 1.1$, while $d(t)\ge \tfrac12 e^{-t}\cdot$const forces $t_{\rm mix}\ge 0.6$. So $t_{\rm mix}(P_3)\asymp 1 \asymp t_{\rm rel}\log 3$.

**Scaling up.** For $P_n$, $t_{\rm rel}=\bigl(2(1-\cos\frac{\pi}{n})\bigr)^{-1}\sim n^2/\pi^2$ and Lacoin's theorem gives $t_{\rm mix}\sim \frac{n^2\log n}{2\pi^2}=\tfrac12 t_{\rm rel}\log n$ — the conjectured law with constant $1/2$. For the complete binary tree $B_h$ with $n=2^{h+1}-1$ vertices, the bisection edge at the root gives $\mathrm{gap}\asymp 1/n$, so the conjecture predicts $t_{\rm mix}\asymp n\log n$, whereas the best proved upper bound is $O(n\log^2 n)$. Closing that single logarithm on $B_h$ is the smallest concrete instance of the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*