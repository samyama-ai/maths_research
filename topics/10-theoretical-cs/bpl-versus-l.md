---
id: 10-theoretical-cs/bpl-versus-l
title: "BPL versus L"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# BPL versus L

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/bpl-versus-l` · **Status:** open

## 1. Problem Statement / Conjecture

Does randomness help space-bounded computation? Formally: is
$$\mathbf{BPL} = \mathbf{L}\,?$$

$\mathbf{L}$ is the class of languages decided by deterministic Turing machines using $O(\log n)$ workspace. $\mathbf{BPL}$ is the class decided by randomized logspace machines with two-sided error $\le 1/3$, where the machine reads its random bits from a one-way read-once tape and halts in polynomial time. The conjecture, near-universally believed, is that the two classes coincide — that every randomized logspace algorithm can be simulated deterministically with only a constant-factor blow-up in space.

A complete resolution requires either (a) a deterministic $O(\log n)$-space algorithm for a $\mathbf{BPL}$-complete problem, or (b) a proof that some language in $\mathbf{BPL}$ requires $\omega(\log n)$ deterministic space. Direction (b) would be an unconditional space lower bound of a kind currently far beyond reach; essentially all work targets (a). Note that unlike $\mathbf{P}$ vs $\mathbf{BPP}$, no complexity-theoretic barrier such as a relativization obstacle or a hardness assumption is needed: the derandomization is believed to be provable outright, and partial unconditional progress exists.

The canonical complete problem is **approximate matrix powering**: given a substochastic matrix and a step count, estimate a walk probability. Its promise version is $\mathbf{BPL}$-complete under logspace reductions.

## 2. Mathematical Foundations

**Ordered branching programs (ROBPs).** A randomized logspace machine on a fixed input $x$ induces a layered graph. An ROBP of length $n$ and width $w$ is a DAG with layers $V_0,\dots,V_n$, $|V_i| \le w$, a start state $v_0 \in V_0$, an accept set $A \subseteq V_n$, and transition functions
$$\delta_i : V_{i-1} \times \{0,1\} \to V_i .$$
For $r \in \{0,1\}^n$ let $B(r) = 1$ iff the walk from $v_0$ following $r$ lands in $A$. A $\mathbf{BPL}$ machine on inputs of length $m$ with space $s = O(\log m)$ yields $w = 2^{O(s)} = \mathrm{poly}(m)$ and $n = \mathrm{poly}(m)$, and acceptance probability $\Pr_{r}[B(r)=1]$.

**Matrix form.** Let $M_i \in \mathbb{R}^{w\times w}$ be the stochastic matrix $\left(M_i\right)_{u,v} = \tfrac{1}{2}\,|\{b : \delta_i(u,b)=v\}|$. Then
$$\Pr_r[B(r)=1] \;=\; e_{v_0}^{\top}\Big(\prod_{i=1}^{n} M_i\Big)\mathbf{1}_A .$$
Derandomizing $\mathbf{BPL}$ is exactly the problem of computing this iterated product to additive error $1/10$ in space $O(\log(nw))$.

**Pseudorandom generator (PRG).** $G:\{0,1\}^{s}\to\{0,1\}^n$ $\varepsilon$-fools width-$w$ length-$n$ ROBPs if for all such $B$,
$$\Big|\Pr_{z\sim U_s}[B(G(z))=1] - \Pr_{r\sim U_n}[B(r)=1]\Big| \le \varepsilon .$$
An explicit (logspace-computable) $G$ with $s = O(\log n)$ for $w=\mathrm{poly}(n)$, $\varepsilon = 1/10$ gives $\mathbf{BPL}=\mathbf{L}$ by enumerating all $2^s = \mathrm{poly}(n)$ seeds. Non-constructively such $G$ exists with $s = O(\log(nw/\varepsilon))$.

**Weighted PRG (pseudorandom pseudodistribution).** A pair $(G,\rho)$ with $G:\{0,1\}^s\to\{0,1\}^n$, $\rho:\{0,1\}^s\to\mathbb{R}$, such that
$$\Big|\mathbb{E}_{z}\big[\rho(z)\,B(G(z))\big] - \Pr_r[B(r)=1]\Big|\le \varepsilon .$$
Weights may be negative, so $(G,\rho)$ need not fool anything as a distribution; this relaxation is strictly more powerful.

**Hitting set generator (HSG).** $H$ hits with threshold $\varepsilon$ if $\Pr_r[B(r)=1] > \varepsilon$ implies $B(H(z))=1$ for some $z$. HSGs suffice for $\mathbf{RL}=\mathbf{L}$ by definition, and — by Cheng–Hoza — also for $\mathbf{BPL}=\mathbf{L}$.

**Known containments.**
$$\mathbf{L}\subseteq\mathbf{RL}\subseteq\mathbf{BPL}\subseteq\mathbf{SC}\cap\mathbf{DSPACE}\big(\log^{3/2} n\big)\subseteq \mathbf{P}.$$

## 3. History & State of the Art (SOTA)

- **1979–1982.** Aleliunas, Karp, Lipton, Lovász and Rackoff show undirected $s$-$t$ connectivity (USTCON) is in $\mathbf{RL}$ via the $O(n^3\log n)$ cover-time bound for random walks, making $\mathbf{RL}$ a class with a natural, central complete-looking problem.
- **1990–1992.** Babai–Nisan–Szegedy and then Nisan construct the first unconditional PRG for logspace: seed length $O(\log^2 n)$ for $\varepsilon = 1/\mathrm{poly}(n)$, width $\mathrm{poly}(n)$. This gives $\mathbf{BPL}\subseteq\mathbf{DSPACE}(\log^2 n)$ — no better than the trivial deterministic simulation, but with a reusable object.
- **1992–1994.** Nisan proves $\mathbf{RL}\subseteq\mathbf{SC}$ (simultaneous $\mathrm{poly}$ time and $\log^2 n$ space). Impagliazzo–Nisan–Wigderson give the INW generator: the same $O(\log^2 n)$ seed from a recursive expander-composition, far more flexible than Nisan's.
- **1995–1999.** Nisan–Zuckerman: randomized space $S$ with only $\mathrm{poly}(S)$ random bits is derandomizable, so $\mathbf{BPSPACE}(S) = \mathbf{DSPACE}(S)$ when randomness is $S^{O(1)}$. Saks–Zhou combine Nisan's generator with random rounding of matrix entries to prove
$$\mathbf{BPSPACE}(S)\subseteq\mathbf{DSPACE}(S^{3/2}),\qquad\text{so }\ \mathbf{BPL}\subseteq\mathbf{DSPACE}(\log^{3/2}n).$$
This exponent $3/2$ stood for over two decades and is still the state of the art up to a $\sqrt{\log\log n}$ factor.
- **2005.** Reingold's $\mathbf{SL}=\mathbf{L}$: USTCON in deterministic logspace via the zig-zag product. This removed the flagship $\mathbf{RL}$ problem from the open list and reframed the target as *directed*, non-reversible walks.
- **2006.** Reingold–Trevisan–Vadhan reduce $\mathbf{RL}$ vs $\mathbf{L}$ to $s$-$t$ connectivity on *regular* digraphs, and to constructing pseudorandom walk generators for them.
- **2010–2018.** Braverman–Rao–Raz–Yehudayoff and Brody–Verbin fool constant-width and regular ROBPs with near-optimal seeds. Braverman–Cohen–Garg introduce weighted PRGs with near-optimal error dependence, breaking the "$\log(1/\varepsilon)$ costs a multiplicative $\log n$" barrier of Nisan/INW.
- **2018–2021.** Hoza–Zuckerman give near-optimal hitting sets in the small-success regime; Cheng–Hoza show hitting sets imply two-sided derandomization; Hoza improves Saks–Zhou to space $O(\log^{3/2}n/\sqrt{\log\log n})$ — the first asymptotic improvement since 1999.
- **2020–2023.** Ahmadinejad–Kelner–Murtagh–Peebles–Sidford–Vadhan give near-logarithmic-space high-precision estimation of random-walk probabilities for Eulerian digraphs, importing spectral-sparsification and Laplacian-solver machinery into space complexity. Pyne–Raz–Zhan and Doron–Pyne–Tell develop hardness-vs-randomness frameworks tailored to space.

## 4. Partial Results / Verified Cases

Solved or near-solved sub-cases, with parameters:

- **Undirected connectivity / symmetric logspace.** $\mathbf{SL}=\mathbf{L}$ (Reingold 2005), deterministic space $O(\log n)$.
- **Eulerian and reversible digraphs.** Random-walk probabilities on Eulerian digraphs estimated to *high* precision $\varepsilon = 1/\mathrm{poly}(n)$ in space $\tilde O(\log n)$ (AKMPSV, FOCS 2020). Covers all reversible chains.
- **Constant width.** Width $w = O(1)$ ROBPs: explicit PRGs with seed $\tilde O(\log n)$ for constant error; width $3$ and width $2$ have seed length $O(\log n \cdot \log(1/\varepsilon))$ or better.
- **Regular ROBPs** (every state has in-degree 2): seed length $O(\log n(\log\log n + \log(1/\varepsilon)))$ for constant width (BRRY 2010), i.e. $O(\log n\log\log n)$ for constant $\varepsilon$.
- **Permutation branching programs**, read-once $\mathrm{AC}^0$, combinatorial rectangles, and small-space *oblivious* models all have $\tilde O(\log n)$-seed PRGs.
- **Few random bits.** If the machine uses $O(\log n)$ (indeed $\log^{O(1)} n$ with space $\log n$… more precisely $S^{O(1)}$ bits at space $S$) random coins: full derandomization (Nisan–Zuckerman 1996).
- **Error regime.** Weighted PRGs achieve seed $\tilde O(\log^2 n) + O(\log(1/\varepsilon))$ for $\mathrm{poly}(n)$ width (Braverman–Cohen–Garg 2018), optimal in the $\varepsilon$-dependence; hitting sets reach seed $O(\log n + \log(1/\varepsilon))$-type bounds for small success (Hoza–Zuckerman 2018).
- **Space upper bound.** $\mathbf{BPL}\subseteq\mathbf{DSPACE}\big(\log^{3/2}n/\sqrt{\log\log n}\big)$ (Hoza 2021), and $\mathbf{BPL}\subseteq\mathbf{SC}$ (Nisan 1994).
- **Catalytic setting.** With a full-but-restorable auxiliary tape, $\mathbf{BPL}$ derandomizes in $O(\log n)$ free space (Pyne, CCC 2024) *(frontier — verify)*.

## 5. Principal Obstacles

- **The recursion tax.** Both Nisan and INW build a length-$n$ generator by $\log n$ levels of recursive doubling, each level paying $\Theta(\log(1/\varepsilon'))$ fresh seed bits for an expander or hash function. Errors compound additively over $n$ steps, forcing $\varepsilon' \approx \varepsilon/n$ at every level, hence $\log n$ levels $\times$ $\log n$ bits $=\log^2 n$. No known analysis lets error *cancel* across levels rather than accumulate. This "$\log^2$ wall" is the single most persistent obstruction.
- **Non-reversibility.** Reingold's and AKMPSV's successes rest on spectral tools — Cheeger inequalities, expander mixing, Laplacian solvers — that require a symmetric or Eulerian structure with real spectrum. General $\mathbf{BPL}$ matrices are arbitrary substochastic, possibly nilpotent, with complex spectra and no useful singular-value/eigenvalue correspondence. Spectral approximation notions ($\tilde L \approx_\epsilon L$) degrade badly or become vacuous.
- **Precision under composition.** Repeated squaring $M \mapsto M^2$ needs $\Theta(\log n)$ bits of precision per level to survive $\log n$ levels; storing intermediate matrices is what costs space. Saks–Zhou's random-shift rounding buys only a $\sqrt{\cdot}$ saving because the rounding must be independent across $\sqrt{\log n}$ blocks and each block still incurs a full Nisan seed.
- **Lower-bound side is empty.** No superlinear space lower bound is known for any explicit problem in $\mathbf{P}$; proving $\mathbf{BPL}\ne\mathbf{L}$ is strictly harder than open problems like $\mathbf{L}\ne\mathbf{P}$-type separations.
- **Hardness-vs-randomness does not transfer.** The Nisan–Wigderson/IW paradigm needs a hard function *computable in the class itself*; a logspace machine cannot afford to evaluate a hard truth table, and standard reconstruction arguments need more space than the simulation saves. Recent "certified" and "distinguisher-opening" frameworks are attempts to patch exactly this.

## 6. The Gap

Everything proven leaves one quantitative gap: **seed length $\log^2 n$ versus $\log n$** for explicit PRGs fooling $\mathrm{poly}(n)$-width, $\mathrm{poly}(n)$-length ROBPs to constant error — equivalently, deterministic space $\log^{3/2}n$ versus $\log n$.

Precisely: for the general case no construction improves on $O(\log^2 n)$ seed for *any* width $w = n^{\Omega(1)}$ with error $\varepsilon = 1/10$, and no black-box improvement is known even for width $n^{0.001}$. The proven cases (undirected, Eulerian, regular, constant-width, permutation) all supply *extra algebraic structure* — symmetry, doubly-stochasticity, or bounded state count — which the generic simulation lacks. The crossing step is: **fool arbitrary substochastic matrix products with error that does not accumulate linearly in the number of layers**, or equivalently produce a $\tilde O(\log n)$-seed hitting set for general width-$n$ ROBPs (which by Cheng–Hoza would immediately give $\mathbf{BPL}=\mathbf{L}$).

## 7. Current Research (as of June 2026)

- **Spectral / Laplacian-solver school** (Vadhan, Sidford, Murtagh, Kelner, Peebles, Ahmadinejad; Harvard/Stanford/Simons). Pushing singular-value approximation and sparsification from Eulerian to general directed chains; "singular value approximation" notions are the current best route *(frontier — verify)*.
- **Weighted PRG / error-reduction school** (Braverman, Cohen, Garg, Hoza, Pyne, Chen, Tal). Iterated Richardson-extrapolation of INW; the current target is a WPRG with seed $o(\log^2 n)$ for constant error, which would break the wall for the first time.
- **Hardness-vs-randomness for space** (Pyne–Raz–Zhan, *Certified hardness vs. randomness for log-space*, FOCS 2023; Doron–Pyne–Tell, STOC 2024). Conditional $\mathbf{BPL}=\mathbf{L}$ under space-bounded hardness assumptions, with reconstruction procedures that themselves run in small space.
- **Catalytic and shared-memory models** (Cook, Mertz, Pyne). The Cook–Mertz tree-evaluation breakthrough ($O(\log n\log\log n)$ space) has revived compress-or-random techniques and suggests catalytic space as a route to $\mathbf{BPL}$ derandomization.
- **Structured-class extension** (Meka, Reingold, Tal, Lee): fooling read-once $\mathrm{AC}^0$, $\mathbb{F}_2$-polynomials over ROBPs, and unordered/unbounded-width models.

## 8. Future Work

1. **Break $\log^{3/2}$ decisively.** Any deterministic simulation in $O(\log^{1.49} n)$ space would be the first genuinely new mechanism since Saks–Zhou.
2. **Eulerian $\to$ general digraphs.** Extend high-precision small-space walk estimation past the Eulerian barrier, e.g. by a space-efficient analogue of directed spectral sparsification with Eulerian-scaling preprocessing.
3. **Hitting sets over PRGs.** Given Cheng–Hoza, focus effort on one-sided objects; hitting sets have looser requirements and already exhibit better parameters in some regimes.
4. **Non-black-box derandomization.** Exploit that the ROBP comes from an actual machine (uniformity), as in Doron–Pyne–Tell, rather than fooling all ROBPs.
5. **Lower bounds on PRGs.** Prove that INW-style recursive constructions provably need $\Omega(\log^2 n)$ seed, to force the community off the paradigm.

## 9. Key References

- **[Foundational]** Noam Nisan. *Pseudorandom generators for space-bounded computation.* Combinatorica 12(4):449–461, 1992.
- **[Foundational]** Russell Impagliazzo, Noam Nisan, Avi Wigderson. *Pseudorandomness for network algorithms.* STOC 1994.
- **[Foundational]** Noam Nisan. *RL ⊆ SC.* Computational Complexity 4:1–11, 1994.
- **[Foundational]** Noam Nisan, David Zuckerman. *Randomness is linear in space.* Journal of Computer and System Sciences 52(1):43–52, 1996.
- **[Foundational]** Michael Saks, Shiyu Zhou. *$\mathrm{BP}_H\mathrm{SPACE}(S)\subseteq \mathrm{DSPACE}(S^{3/2})$.* JCSS 58(2):376–403, 1999.
- **[Foundational]** Omer Reingold. *Undirected connectivity in log-space.* Journal of the ACM 55(4), 2008 (STOC 2005).
- **[Foundational]** Omer Reingold, Luca Trevisan, Salil Vadhan. *Pseudorandom walks on regular digraphs and the RL vs. L problem.* STOC 2006.
- **[SOTA]** Mark Braverman, Anup Rao, Ran Raz, Amir Yehudayoff. *Pseudorandom generators for regular branching programs.* SIAM Journal on Computing 43(3):973–986, 2014 (FOCS 2010).
- **[SOTA]** Mark Braverman, Gil Cohen, Sumegha Garg. *Pseudorandom pseudo-distributions with near-optimal error for read-once branching programs.* SIAM Journal on Computing 49(5), 2020 (STOC 2018).
- **[SOTA]** William Hoza, David Zuckerman. *Simple optimal hitting sets for small-success RL.* SIAM Journal on Computing 49(4), 2020 (FOCS 2018).
- **[SOTA]** Kuan Cheng, William Hoza. *Hitting sets give two-sided derandomization of small space.* CCC 2020.
- **[SOTA]** AmirMahdi Ahmadinejad, Jonathan Kelner, Jack Murtagh, John Peebles, Aaron Sidford, Salil Vadhan. *High-precision estimation of random walks in small space.* FOCS 2020.
- **[SOTA]** Edward Pyne, Salil Vadhan. *Pseudodistributions that beat all pseudorandom generators.* CCC 2021.
- **[SOTA]** William Hoza. *Better pseudodistributions and derandomization for space-bounded computation.* RANDOM 2021.
- **[SOTA]** Edward Pyne, Ran Raz, Wei Zhan. *Certified hardness vs. randomness for log-space.* FOCS 2023.
- **[Survey]** William Hoza. *Recent progress on derandomizing space-bounded computation.* Bulletin of the EATCS, 2022.
- **[Survey]** Michael Saks. *Randomization and derandomization in space-bounded computation.* Proceedings of Computational Complexity (CCC), 1996.

## 10. Worked Example / Concrete Special Case

**A width-3 chain and the cost of repeated squaring.** Take the $\mathbf{BPL}$-complete task of estimating an entry of $M^n$ for a stochastic $M$. Let states be $\{1,2,3\}$ with state $3$ absorbing:
$$M=\begin{pmatrix}1/2 & 1/2 & 0\\ 1/2 & 0 & 1/2\\ 0&0&1\end{pmatrix}.$$
Squaring once:
$$M^{2}=\begin{pmatrix}1/2 & 1/4 & 1/4\\ 1/4 & 1/4 & 1/2\\ 0&0&1\end{pmatrix},$$
since row 1 of $M^2$ is $\tfrac12(\tfrac12,\tfrac12,0)+\tfrac12(\tfrac12,0,\tfrac12)=(\tfrac12,\tfrac14,\tfrac14)$, and row 2 is $\tfrac12(\tfrac12,\tfrac12,0)+\tfrac12(0,0,1)=(\tfrac14,\tfrac14,\tfrac12)$. Squaring again:
$$\big(M^{2}\big)^{2}\text{, row }1=\tfrac12(\tfrac12,\tfrac14,\tfrac14)+\tfrac14(\tfrac14,\tfrac14,\tfrac12)+\tfrac14(0,0,1)=\Big(\tfrac{5}{16},\tfrac{3}{16},\tfrac12\Big),$$
so $\Pr[\text{absorbed within }4\text{ steps}\mid \text{start }1]=1/2$ exactly.

**Why this is the whole difficulty in miniature.** For $n=2^k$ steps, the deterministic algorithm does $k=\log n$ squarings. Computing one entry of $M^{2^k}$ recursively costs $O(\log w)$ space per recursion level to hold indices, and the recursion has depth $k$ — total $O(\log n\log w)=O(\log^2 n)$, the trivial bound. Nisan's generator reproduces exactly this $\log^2$ via $\log n$ levels of $O(\log n)$-bit hashes.

Now truncate every entry to $b$ bits after each squaring, as Saks–Zhou do. A single rounding perturbs each entry by $\le 2^{-b}$; after $k$ squarings the perturbation can grow by a factor $w$ per level, so naively $b > k\log w$ bits are required — no saving. Saks–Zhou's fix is to round with a *shared random shift* $\delta$ so that, with high probability over $\delta$, the rounded matrix is a deterministic function of the true matrix, letting the same Nisan seed be **reused** across a block of $\sqrt{\log n}$ levels. Reusing one $O(\log n)$-bit seed across $\sqrt{\log n}$ levels and paying separately for $\sqrt{\log n}$ blocks yields
$$O\big(\sqrt{\log n}\cdot \log n\big)=O\big(\log^{3/2}n\big)$$
space. Proving $\mathbf{BPL}=\mathbf{L}$ means reusing randomness across **all** $\log n$ levels — with the $3\times 3$ example above, the analogue of doing all squarings with a single $O(\log n)$-bit random string whose error does not accumulate.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*