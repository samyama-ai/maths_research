---
id: 10-theoretical-cs/rl-versus-l
title: "RL versus L"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# RL versus L

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/rl-versus-l` · **Status:** open

## 1. Problem Statement / Conjecture

Does randomness help space-bounded computation? Formally:

$$\textbf{Question: } \quad \mathrm{RL} \stackrel{?}{=} \mathrm{L}.$$

$\mathrm{L}$ is the class of languages decided by a deterministic Turing machine using $O(\log n)$ work-tape cells on inputs of length $n$ (read-only input tape, not counted). $\mathrm{RL}$ is the class decided by a *randomized* logspace machine with a one-way read-only random tape, running in polynomial time, with one-sided error: $x \in L \Rightarrow \Pr[\text{accept}] \ge 1/2$, and $x \notin L \Rightarrow \Pr[\text{accept}] = 0$. $\mathrm{BPL}$ is the two-sided-error analogue with error $\le 1/3$.

The conjecture held by most researchers is $\mathrm{RL} = \mathrm{BPL} = \mathrm{L}$: randomness buys nothing in logarithmic space, unconditionally (unlike $\mathrm{P}$ vs $\mathrm{BPP}$, where derandomization is only known under circuit lower bounds). A complete resolution means either (i) an explicit deterministic $O(\log n)$-space algorithm for an $\mathrm{RL}$-complete problem — canonically, $s\text{-}t$ connectivity in directed graphs restricted so that a random walk finds $t$ — or (ii) a proof that some language in $\mathrm{RL}$ requires $\omega(\log n)$ deterministic space, which would in particular separate $\mathrm{L}$ from $\mathrm{NL}$ or from $\mathrm{P}$.

Two caveats fix the statement. The polynomial time bound matters: randomized logspace *without* a time bound and with one-sided error equals $\mathrm{NL}$, so $\mathrm{RL}$ as defined above is the time-bounded class. And the error must be bounded away from $0$ and $1$ by a constant; the "small-success" regime behaves differently (Section 4).

## 2. Mathematical Foundations

**Space classes.** For $s: \mathbb{N} \to \mathbb{N}$, $\mathrm{DSPACE}(s)$, $\mathrm{NSPACE}(s)$, $\mathrm{BPSPACE}(s)$ denote deterministic, nondeterministic and bounded-error randomized space-$s$ classes; $\mathrm{L} = \mathrm{DSPACE}(\log n)$, $\mathrm{NL} = \mathrm{NSPACE}(\log n)$. Known inclusions:

$$\mathrm{L} \subseteq \mathrm{RL} \subseteq \mathrm{BPL} \subseteq \mathrm{NL} \subseteq \mathrm{DSPACE}(\log^2 n) \cap \mathrm{P},$$

the penultimate inclusion by **Savitch's theorem** $\mathrm{NSPACE}(s) \subseteq \mathrm{DSPACE}(s^2)$ for $s \ge \log n$.

**Branching-program model.** A space-$s$, time-$n$ randomized machine on a fixed input is exactly a *read-once branching program* (ROBP) of width $w = 2^{O(s)}$ and length $n$: a layered graph $V_0, \dots, V_n$ with $|V_i| \le w$ and transition maps $\delta_i : V_i \times \{0,1\} \to V_{i+1}$, reading one fresh random bit per layer. Equivalently, layer $i$ acts by a stochastic matrix and the acceptance probability is

$$f(B) \;=\; \mathbb{E}_{x \sim U_n}\big[B(x)\big] \;=\; \Big(\textstyle\prod_{i=1}^{n} M_i\Big)[v_{\mathrm{start}}, v_{\mathrm{acc}}], \qquad M_i = \tfrac{1}{2}\big(A_i^{(0)} + A_i^{(1)}\big).$$

Deciding $f(B) \ge 2/3$ vs $f(B) \le 1/3$ for $w = \mathrm{poly}(n)$ is the $\mathrm{BPL}$-complete problem; $f(B) > 0$ vs $f(B) = 0$ is the $\mathrm{NL}$-complete reachability problem.

**Pseudorandom generators.** $G : \{0,1\}^{d} \to \{0,1\}^{n}$ *$\varepsilon$-fools* width-$w$ length-$n$ ROBPs if for all such $B$,
$$\big|\mathbb{E}_{y \sim U_d}[B(G(y))] - \mathbb{E}_{x \sim U_n}[B(x)]\big| \le \varepsilon .$$
An explicit $G$ computable in space $O(d)$ with $d = O(\log n)$ and $w = \mathrm{poly}(n)$, $\varepsilon = 1/10$, gives $\mathrm{BPL} = \mathrm{L}$ by enumerating all $2^d = \mathrm{poly}(n)$ seeds. A *hitting set generator* (HSG) only guarantees $f(B) > \varepsilon \Rightarrow \exists y,\ B(G(y)) = 1$; an $O(\log n)$-seed HSG suffices for $\mathrm{RL} = \mathrm{L}$. A *weighted PRG* (pseudorandom pseudodistribution) attaches real weights $\rho_y$ with $|\sum_y \rho_y B(G(y)) - f(B)| \le \varepsilon$.

**Random walks.** For a $d$-regular digraph $G$ on $n$ vertices with transition matrix $M = A/d$, the spectral gap is $1 - \lambda(M)$ with $\lambda(M) = \max_{v \perp \mathbf{1}} \|Mv\|/\|v\|$. Mixing time $\tau \approx O(\log n / (1-\lambda))$. For connected *undirected* graphs, the cover time of the lazy walk is $O(n^3)$ (Aleliunas–Karp–Lipton–Lovász–Rackoff, 1979), which is what puts $\mathrm{USTCON} \in \mathrm{RL}$ with $O(\log n)$ space and $O(\log n)$ bits of state.

## 3. History & State of the Art (SOTA)

- **1970.** Savitch proves $\mathrm{NSPACE}(s) \subseteq \mathrm{DSPACE}(s^2)$, giving the trivial upper bound $\mathrm{RL} \subseteq \mathrm{DSPACE}(\log^2 n)$.
- **1979.** Aleliunas, Karp, Lipton, Lovász, Rackoff: undirected $s$-$t$ connectivity is in $\mathrm{RL}$ via random walks; universal traversal sequences exist but are not known to be explicit. This is the origin of $\mathrm{RL}$ as a class of interest.
- **1990–92.** Nisan's generator: seed length $O(\log n \log(nw/\varepsilon))$ to $\varepsilon$-fool width-$w$ length-$n$ ROBPs, i.e. $O(\log^2 n)$ for $w = \mathrm{poly}(n)$, $\varepsilon = 1/\mathrm{poly}$. Still the benchmark after 35 years.
- **1994.** Nisan: $\mathrm{RL} \subseteq \mathrm{SC}^2$ (simultaneously $O(\log^2 n)$ space and polynomial time) — a genuine improvement over Savitch, which is not simultaneously poly-time.
- **1996.** Nisan–Zuckerman: randomized space $s$ using only $s^{O(1)}$ random bits is derandomizable in space $O(s)$; so $\mathrm{BPSPACE}(s)$ with $\mathrm{poly}(s)$ randomness collapses.
- **1999.** Saks–Zhou: $\mathrm{BPSPACE}(s) \subseteq \mathrm{DSPACE}(s^{3/2})$, hence $\mathrm{BPL} \subseteq \mathrm{DSPACE}(\log^{1.5} n)$. The current headline unconditional bound.
- **2005/2008.** Reingold: $\mathrm{USTCON} \in \mathrm{L}$, so $\mathrm{SL} = \mathrm{L}$, using zig-zag expander products. This removed the canonical $\mathrm{RL}$ candidate problem from the open list.
- **2018–2021.** Braverman–Cohen–Garg introduce weighted PRGs achieving near-optimal error dependence; Hoza (2021) improves Saks–Zhou to $O(\log^{3/2} n / \sqrt{\log\log n})$ space — the first asymptotic improvement in over 20 years, and only by a $\sqrt{\log\log n}$ factor.

## 4. Partial Results / Verified Cases

- **Undirected graphs (all $n$):** $\mathrm{SL} = \mathrm{L}$ (Reingold 2008). Every problem logspace-reducible to undirected connectivity — bipartiteness, planarity of undirected graphs, undirected forest accessibility — is derandomized.
- **Regular digraphs with polynomial mixing:** Reingold–Trevisan–Vadhan (2006) derandomize walks on consistently labelled regular digraphs; Chung–Reingold–Vadhan (CCC 2007) give logspace $s$-$t$ connectivity for digraphs of polynomial mixing time when the stationary distribution is supplied.
- **Bounded randomness:** $\mathrm{poly}(s)$ random bits, $s = \log n$ (Nisan–Zuckerman 1996).
- **Constant width:** width-$3$ ROBPs are fooled with seed $O(\log n)$ ($\varepsilon$ constant); permutation/regular ROBPs of constant width admit $\tilde O(\log n)$ seeds (Braverman–Rao–Raz–Yehudayoff; Koucký–Nimbhorkar–Pudlák). Width $w \ge 4$ with $\varepsilon = 1/\mathrm{poly}$ is open.
- **Small success probability:** Hoza–Zuckerman (FOCS 2018) give hitting sets with essentially optimal seed length in the regime where the acceptance threshold $\varepsilon$ is polynomially or exponentially small, derandomizing "small-success $\mathrm{RL}$".
- **Space bound:** $\mathrm{BPL} \subseteq \mathrm{DSPACE}\!\big(\log^{3/2} n / \sqrt{\log\log n}\big)$ (Hoza 2021), and $\mathrm{RL} \subseteq \mathrm{SC}^2$ (Nisan 1994).
- **Reductions:** Cheng–Hoza (CCC 2020) prove hitting sets suffice for two-sided derandomization, so $\mathrm{RL} = \mathrm{L}$ and $\mathrm{BPL} = \mathrm{L}$ stand or fall together.

## 5. Principal Obstacles

- **Nisan's $\log^2$ barrier is structural.** Nisan-type generators recurse by halving the length and re-using a hash to "recycle" randomness; each of the $\log n$ levels of recursion pays $\Theta(\log n)$ fresh seed bits. Every variant (Impagliazzo–Nisan–Wigderson, Nisan–Zuckerman) pays the same product. No known construction beats $\log n \cdot \log(1/\varepsilon)$ for general $\mathrm{poly}$-width ROBPs, and there are matching lower bounds against the specific *recycling* framework.
- **No hardness-vs-randomness shortcut.** In the time-bounded world, $\mathrm{BPP} = \mathrm{P}$ follows from circuit lower bounds. For space, Klivans–van Melkebeek's translation needs a function in $\mathrm{DSPACE}(n)$ with $2^{\Omega(n)}$ *branching-program* size — a lower bound not known and not obviously easier than the derandomization itself. Meanwhile $\mathrm{L} \ne \mathrm{NL}$ and even $\mathrm{L} \ne \mathrm{P}$ are open, so no useful hardness is available.
- **Reingold's method does not survive orientation.** The zig-zag argument turns an undirected graph into an expander while preserving connectivity, using that undirected walks are reversible and the stationary distribution is known (degree-proportional). Directed walks have unknown, possibly exponentially skewed stationary distributions; powering a directed graph in logspace loses the connectivity information.
- **Error accumulation.** Saks–Zhou combines Nisan's generator with matrix powering and *randomized rounding of the space parameter* to shave $\log^{1/2}$; the argument is tight because each recursion level must round away $\Theta(\log n)$ bits of precision. Improving it needs a generator with error $\varepsilon = n^{-\omega(1)}$ at seed $o(\log n \log(1/\varepsilon))$.
- **Lower-bound side is empty.** No superlogarithmic space lower bound is known for any explicit problem in $\mathrm{P}$, let alone in $\mathrm{RL}$. A separation $\mathrm{RL} \ne \mathrm{L}$ would imply $\mathrm{L} \ne \mathrm{P}$.

## 6. The Gap

Proven: seed length $O(\log^2 n)$ for $\mathrm{poly}$-width ROBPs; deterministic space $\log^{1.5}n/\sqrt{\log\log n}$; full derandomization for undirected/reversible and constant-width cases.

Needed: an explicit $G : \{0,1\}^{O(\log n)} \to \{0,1\}^n$ that $\tfrac{1}{10}$-hits (hitting is enough) every width-$n$, length-$n$ ROBP. The gap is a factor $\Theta(\log n)$ in seed length, or equivalently the step from **reversible/known-stationary** walks to **arbitrary directed** walks with polynomial mixing. Intermediate milestones that remain open and would be major: seed $O(\log^{2-\delta} n)$ for any $\delta > 0$; $\mathrm{BPL} \subseteq \mathrm{DSPACE}(\log^{1.4} n)$; fooling width-$4$ ROBPs with $O(\log n)$ seed at inverse-polynomial error.

## 7. Current Research (as of June 2026)

- **Weighted PRGs / pseudodistributions.** Post-Braverman–Cohen–Garg line (Chattopadhyay–Liao, Cohen–Doron–Renard–Sberlo–Ta-Shma, Pyne–Vadhan): seed $\tilde O(\log^2 n) + O(\log(1/\varepsilon))$, decoupling error from length. Groups at Weizmann, Tel Aviv, UT Austin, Harvard, Simons Institute.
- **Catalytic and tree-evaluation techniques.** Cook–Mertz's $O(\log n \log\log n)$-space Tree Evaluation algorithm (STOC 2024) and Williams' $\mathrm{TIME}(t) \subseteq \mathrm{SPACE}(\sqrt{t \log t})$ (STOC 2025) reopened space-complexity techniques thought exhausted; several groups are testing whether the same "compute in a full memory, restore it" idea derandomizes $\mathrm{BPL}$. *(frontier — verify)*
- **Certified derandomization.** Pyne–Raz–Zhan (FOCS 2023) give hardness-vs-randomness for logspace with a *certified* (verifiable) generator; Doron–Pyne–Tell pursue "opening up the distinguisher" to lower the hardness requirement. *(frontier — verify)*
- **Spectral / Laplacian solvers.** Ahmadinejad–Kelner–Peebles–Pyne–Sidford–Vadhan: nearly-logspace algorithms for approximating random-walk quantities on Eulerian digraphs, extending Reingold's reach beyond the undirected case. *(frontier — verify)*

## 8. Future Work

- Push the Eulerian/known-stationary machinery to arbitrary regular digraphs; this is the explicitly stated next step in the Reingold–Trevisan–Vadhan program.
- Exploit the Cheng–Hoza equivalence: focus construction effort entirely on hitting sets, which are a weaker and combinatorially simpler object than PRGs.
- Beat Nisan's seed for width $n^{o(1)}$ at constant error — Hoza's survey identifies this as the cleanest unclaimed target.
- Develop unconditional space lower bounds for restricted models (regular ROBPs, oblivious catalytic machines) to test whether $\mathrm{RL} \ne \mathrm{L}$ is even consistent with known techniques.
- Import catalytic-space register manipulation into matrix powering, replacing Saks–Zhou's lossy rounding.

## 9. Key References

- **[Foundational]** W. J. Savitch. *Relationships between nondeterministic and deterministic tape complexities.* Journal of Computer and System Sciences 4(2), 1970.
- **[Foundational]** R. Aleliunas, R. M. Karp, R. J. Lipton, L. Lovász, C. Rackoff. *Random walks, universal traversal sequences, and the complexity of maze problems.* FOCS 1979.
- **[Foundational]** N. Nisan. *Pseudorandom generators for space-bounded computation.* Combinatorica 12(4), 1992.
- **[Foundational]** N. Nisan. *RL ⊆ SC.* Computational Complexity 4(1), 1994.
- **[Foundational]** N. Nisan, D. Zuckerman. *Randomness is linear in space.* Journal of Computer and System Sciences 52(1), 1996.
- **[SOTA]** M. Saks, S. Zhou. *$BP_HSPACE(S) \subseteq DSPACE(S^{3/2})$.* Journal of Computer and System Sciences 58(2), 1999.
- **[SOTA]** O. Reingold. *Undirected connectivity in log-space.* Journal of the ACM 55(4), 2008 (STOC 2005).
- **[SOTA]** O. Reingold, L. Trevisan, S. Vadhan. *Pseudorandom walks on regular digraphs and the RL vs. L problem.* STOC 2006.
- **[SOTA]** M. Braverman, G. Cohen, S. Garg. *Pseudorandom pseudo-distributions with near-optimal error for read-once branching programs.* SIAM Journal on Computing 49(5), 2020 (STOC 2018).
- **[SOTA]** W. M. Hoza, D. Zuckerman. *Simple optimal hitting sets for small-success RL.* SIAM Journal on Computing 49(4), 2020 (FOCS 2018).
- **[SOTA]** K. Cheng, W. M. Hoza. *Hitting sets give two-sided derandomization of small space.* CCC 2020.
- **[SOTA]** W. M. Hoza. *Better pseudodistributions and derandomization for space-bounded computation.* RANDOM 2021.
- **[Recent]** J. Cook, I. Mertz. *Tree evaluation is in space $O(\log n \cdot \log\log n)$.* STOC 2024.
- **[Survey]** M. Saks. *Randomization and derandomization in space-bounded computation.* CCC 1996.
- **[Survey]** S. Vadhan. *Pseudorandomness.* Foundations and Trends in Theoretical Computer Science 7(1–3), 2012.
- **[Survey]** W. M. Hoza. *Recent progress on derandomizing space-bounded computation.* Bulletin of the EATCS 138, 2022 (ECCC TR22-121).

## 10. Worked Example / Concrete Special Case

**The randomized algorithm.** Let $G$ be an undirected graph on $n = 1024$ vertices, $s, t \in V$. The $\mathrm{RL}$ algorithm stores only the current vertex ($\log_2 1024 = 10$ bits) and a step counter ($\le 30$ bits): take $T = 4n^3 \approx 4.3 \times 10^9$ uniform random steps from $s$, accept if $t$ is visited. By AKLLR the cover time of a connected undirected graph is $\le 2|E|(n-1) < n^3$, so $\Pr[\text{accept}] \ge 1/2$ when $s \leadsto t$, and $0$ otherwise. Total workspace: $40$ bits $= O(\log n)$. Random bits consumed: $T \log_2 d \approx 4 \times 10^{10}$ — far more than $\mathrm{poly}(\log n)$, so Nisan–Zuckerman does not apply.

**The ROBP view.** Fix $G$. The computation is a width-$w$ ROBP with $w = n = 1024$ (one state per vertex) and length $\ell = T$. Layer $i$ applies the same stochastic matrix $M = D^{-1}A$; acceptance probability is $\big(\prod_{i\le T} M\big)[s,t]$ with $t$ absorbing.

**Cost of naive derandomization.** Nisan's generator with $w = n$, $\ell = T$, $\varepsilon = 1/4$ needs seed
$$d = O\!\big(\log \ell \cdot \log(w\ell/\varepsilon)\big) \approx c \cdot 32 \cdot 42 \approx 1.3\times 10^3 \text{ bits}.$$
Enumerating $2^{d}$ seeds costs $n^{\Theta(\log n)}$ time — quasipolynomial, and space $O(d) = O(\log^2 n)$: exactly the Savitch/Nisan bound, no better. What $\mathrm{RL} = \mathrm{L}$ demands is $d = O(\log n) \approx 10$–$40$ bits, so that $2^d = \mathrm{poly}(n)$ seeds can be tried in $O(\log n)$ space. The **gap is the factor $\log \ell \approx 32$** between $d \approx 1300$ and $d \approx 40$.

**Why Reingold closes it here but not in general.** Instead of derandomizing the walk, Reingold rewrites the graph: $O(\log n)$ rounds of squaring interleaved with zig-zag products with a fixed constant-size expander $H$ produce $G'$ with the same connected components and spectral gap $\ge 1/2$, so diameter $O(\log n)$; then exhaustively search paths of length $O(\log n)$, storing $O(\log n)$ bits. Each round's vertex relabelling is recomputable on the fly in $O(\log n)$ space *because the walk is reversible with known stationary distribution $\pi(v) \propto \deg(v)$*. Orient the edges of this same $G$ arbitrarily and $\pi$ becomes unknown and possibly exponentially non-uniform; the squaring step no longer preserves the gap computably, and the argument collapses. That single failure point is the whole of the $\mathrm{RL}$ vs $\mathrm{L}$ problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*