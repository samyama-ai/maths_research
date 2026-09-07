---
id: 10-theoretical-cs/l-versus-nl
title: "L versus NL"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# L versus NL

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/l-versus-nl` · **Status:** open

## 1. Problem Statement / Conjecture

Is every problem decidable by a nondeterministic Turing machine in $O(\log n)$ workspace also decidable by a deterministic machine in $O(\log n)$ workspace? Formally: does $\mathsf{L} = \mathsf{NL}$?

The consensus conjecture is $\mathsf{L} \neq \mathsf{NL}$. A resolution requires either:

- **Separation.** Exhibit a language $A \in \mathsf{NL}$ and prove no deterministic $O(\log n)$-space machine decides $A$. By completeness it suffices to prove $\mathrm{STCON} \notin \mathsf{L}$, where $\mathrm{STCON}$ is directed $s$-$t$ reachability. This entails $\mathsf{L} \neq \mathsf{PSPACE}$ but is *not* known to entail $\mathsf{P} \neq \mathsf{NP}$.
- **Collapse.** Give a deterministic $O(\log n)$-space algorithm for $\mathrm{STCON}$. This would imply $\mathsf{NL} = \mathsf{L} \subseteq \mathsf{P}$ and, by the space hierarchy theorem, $\mathsf{NSPACE}(s) = \mathsf{DSPACE}(s)$ for all space-constructible $s(n) \geq \log n$ (translation), collapsing the whole nondeterministic space hierarchy to its deterministic counterpart.

The problem is the space analogue of $\mathsf{P}$ vs $\mathsf{NP}$, and is considered strictly easier — yet it is open after more than fifty years.

## 2. Mathematical Foundations

**Machine model.** An offline Turing machine has a read-only input tape (head movement free) and a read-write work tape whose used cells are counted. For space-constructible $s : \mathbb{N} \to \mathbb{N}$,
$$\mathsf{DSPACE}(s) = \{ A : A \text{ decided by a deterministic TM using } O(s(n)) \text{ work cells}\},$$
and $\mathsf{NSPACE}(s)$ likewise with nondeterminism. Set
$$\mathsf{L} = \mathsf{DSPACE}(\log n), \qquad \mathsf{NL} = \mathsf{NSPACE}(\log n), \qquad \mathsf{coNL} = \{\bar A : A \in \mathsf{NL}\}.$$

**Configuration graph.** A machine $M$ with space $s(n)$ on input $x$, $|x|=n$, has configuration count
$$|C_M(x)| \;=\; O\!\big(n \cdot s(n) \cdot |Q| \cdot |\Gamma|^{s(n)}\big) \;=\; n^{O(1)} \text{ when } s = O(\log n).$$
$M$ accepts $x$ iff $C_M(x)$ contains a path from $c_{\text{start}}$ to $c_{\text{accept}}$. Hence:

**Theorem (completeness; Savitch 1970, Jones 1975).** $\mathrm{STCON} = \{\langle G,s,t\rangle : G \text{ digraph},\ t \text{ reachable from } s\}$ is $\mathsf{NL}$-complete under logspace many-one reductions $\leq_{\mathrm{m}}^{\log}$; so $\mathsf{L}=\mathsf{NL} \iff \mathrm{STCON} \in \mathsf{L}$.

**Theorem (Savitch 1970).** $\mathsf{NSPACE}(s) \subseteq \mathsf{DSPACE}(s^2)$ for $s(n) \geq \log n$. In particular $\mathsf{NL} \subseteq \mathsf{DSPACE}(\log^2 n)$, via the recursion
$$\mathrm{REACH}(u,v,2^k) \;=\; \bigvee_{w} \big[\mathrm{REACH}(u,w,2^{k-1}) \wedge \mathrm{REACH}(w,v,2^{k-1})\big],$$
of depth $\log n$ and $O(\log n)$ bits per frame.

**Theorem (Immerman 1988; Szelepcsényi 1987).** $\mathsf{NSPACE}(s) = \mathsf{coNSPACE}(s)$ for $s \geq \log n$; hence $\mathsf{NL} = \mathsf{coNL}$. Proof by inductive counting: with $r_i = |\{v : \mathrm{dist}(s,v) \le i\}|$ computed nondeterministically from $r_{i-1}$ in $O(\log n)$ space, non-reachability is certifiable.

**Known inclusions.**
$$\mathsf{NC}^1 \subseteq \mathsf{L} \subseteq \mathsf{NL} \subseteq \mathsf{LOGCFL} \subseteq \mathsf{AC}^1 \subseteq \mathsf{NC}^2 \subseteq \mathsf{P} \subseteq \mathsf{PSPACE},$$
with $\mathsf{NL} \subseteq \mathsf{DSPACE}(\log^2 n)$ and $\mathsf{L} \subsetneq \mathsf{PSPACE}$ by the space hierarchy theorem. Also $\mathsf{NL} = \mathsf{FO}[\text{DTC} \to \text{TC}]$: by Immerman's descriptive characterization, $\mathsf{NL} = \mathrm{FO}(\mathrm{TC})$ and $\mathsf{L} = \mathrm{FO}(\mathrm{DTC})$ on ordered structures, so the question is whether transitive closure is first-order expressible from *deterministic* transitive closure.

**Branching programs.** $\mathsf{L}/\mathrm{poly}$ = languages with polynomial-size branching programs; $\mathsf{NL}/\mathrm{poly}$ = polynomial-size nondeterministic (switching-and-rectifier) branching programs. A superpolynomial size lower bound for some explicit $\mathsf{NL}$ function against deterministic branching programs would give $\mathsf{L}/\mathrm{poly} \neq \mathsf{NL}/\mathrm{poly}$, hence (non-uniformly) the separation.

## 3. History & State of the Art (SOTA)

- **1970.** Savitch proves $\mathsf{NSPACE}(s) \subseteq \mathsf{DSPACE}(s^2)$ — still the best deterministic simulation, unimproved in 55 years.
- **1975–76.** Jones, and Jones–Lien–Laaser, establish $\mathrm{STCON}$ and $2$-$\mathrm{SAT}$-unsatisfiability as $\mathsf{NL}$-complete under logspace reductions.
- **1979.** Aleliunas–Karp–Lipton–Lovász–Rackoff: undirected $s$-$t$ connectivity ($\mathrm{USTCON}$) is in $\mathsf{RL}$ via random walks with cover time $O(mn)$.
- **1980.** Cook–Rackoff introduce the **jumping automaton for graphs (JAG)**, a restricted pebble model, and prove $\Omega(\log^2 n / \log\log n)$ space lower bounds for $\mathrm{STCON}$ in it.
- **1987–88.** Immerman and Szelepcsényi independently prove $\mathsf{NL} = \mathsf{coNL}$, refuting the then-popular analogy with $\mathsf{NP}$ vs $\mathsf{coNP}$.
- **1992.** Nisan: $\mathsf{RL} \subseteq \mathsf{SC}$; his pseudorandom generator fools $\mathrm{poly}$-width read-once branching programs with seed $O(\log^2 n)$.
- **1999.** Saks–Zhou: $\mathsf{BPSPACE}(s) \subseteq \mathsf{DSPACE}(s^{3/2})$, hence $\mathsf{RL} \subseteq \mathsf{DSPACE}(\log^{3/2} n)$.
- **2005/2008.** **Reingold**: $\mathrm{USTCON} \in \mathsf{L}$, i.e. $\mathsf{SL} = \mathsf{L}$, using the zig-zag product to build expanders in logspace. This is the single largest positive result toward $\mathsf{L}=\mathsf{NL}$.
- **2024.** Cook–Mertz solve Tree Evaluation in $O(\log n \cdot \log\log n)$ space, breaking a conjectured $\mathsf{L}$-separating barrier; Williams (2025) leverages it to prove $\mathsf{TIME}[t] \subseteq \mathsf{SPACE}[\sqrt{t \log t}]$.

**SOTA summary.** Best deterministic space for $\mathrm{STCON}$: $O(\log^2 n)$ (Savitch), or $O(n)$-ish time-space tradeoffs; best simultaneous bound $n^{O(1)}$ time and $n/2^{\Theta(\sqrt{\log n})}$ space (Barnes–Buss–Ruzzo–Schieber 1998). Best unconditional lower bound against general logspace machines: **none**.

## 4. Partial Results / Verified Cases

- **Undirected graphs (Reingold 2008).** $\mathrm{USTCON} \in \mathsf{L}$; the symmetric analogue of the question is settled affirmatively. Earlier: $O(\log^{4/3} n)$ (Armoni–Ta-Shma–Wigderson–Zhou 2000), $O(\log n \log\log n)$ (Trifonov 2008).
- **Planar directed reachability.** In $\mathsf{UL} \cap \mathsf{coUL}$ (Bourke–Tewari–Vinodchandran 2009); planar $\mathrm{STCON}$ is in $\mathsf{DSPACE}(O(\log^2 n / \log\log n))$ and in $\mathsf{polyL} \cap \mathsf{P}$ simultaneously (Imai–Nakagawa–Pavan–Vinodchandran–Watanabe 2013: $O(n^{1/2+\epsilon})$ space in polynomial time).
- **Bounded genus, minor-free, and bounded-treewidth digraphs.** Reachability in $\mathsf{L}$ for graphs of bounded treewidth (Elberfeld–Jakoby–Tantau 2010, via logspace Bodlaender–Courcelle); constant-genus digraph reachability in $\mathsf{UL}$.
- **Nonuniform / promise collapses.** $\mathsf{NL} \subseteq \mathsf{UL}/\mathrm{poly}$ (Reinhardt–Allender 2000) — unambiguity is free non-uniformly. Under the hardness assumption $\mathsf{DSPACE}(n)$ requires $2^{\Omega(n)}$-size circuits, $\mathsf{NL} = \mathsf{UL}$ (Allender–Reinhardt–Zhou 1999).
- **Restricted models.** JAG and NNJAG lower bounds: $\Omega(\log^2 n/\log\log n)$ space (Cook–Rackoff 1980; Poon 1993; Edmonds–Poon–Achlioptas 1999), i.e. Savitch is optimal *within these models*.
- **Monotone models.** Potechin (2010) proved $n^{\Omega(\log n)}$ size for monotone switching networks solving directed $\mathrm{STCON}$, matching Savitch monotonically; extended by Chan–Potechin (2014) to a tight $n^{\Theta(\log n)}$ hierarchy for $\mathrm{REACH}(k)$.
- **Small parameters.** For $\mathrm{REACH}$ restricted to paths of length $\le k$, deterministic space $O(k \log n)$ suffices trivially; the problem is only hard for $k = n^{\Omega(1)}$.

## 5. Principal Obstacles

- **Relativization.** With oracle access, both answers are consistent: there are oracles $A,B$ with $\mathsf{L}^A = \mathsf{NL}^A$ and $\mathsf{L}^B \neq \mathsf{NL}^B$ (Ladner–Lynch 1976, for appropriate space-bounded oracle-access conventions). Any diagonalization-only argument fails.
- **No lower-bound technique reaches $\log n$ space.** The strongest explicit branching-program size bound remains Nečiporuk's $\Omega(n^2/\log^2 n)$ (1966) — polynomial, not superpolynomial. Superpolynomial size is exactly what $\mathsf{L}/\mathrm{poly} \neq \mathsf{NL}/\mathrm{poly}$ demands, and Nečiporuk's method provably cannot exceed $n^2/\log^2 n$.
- **Structural symmetry defeats intuition.** $\mathsf{NL} = \mathsf{coNL}$ removes the closure-property asymmetry that motivates $\mathsf{P} \neq \mathsf{NP}$; and $\mathsf{NL} \subseteq \mathsf{UL}/\mathrm{poly}$ removes the "many witnesses" asymmetry non-uniformly. The class is far more robust than $\mathsf{NP}$, so plausible separating invariants keep evaporating.
- **Barrier results are model-bound.** JAG/NNJAG and monotone-switching-network bounds are strong but are known to be *evaded* by general algorithms: Reingold's algorithm is non-monotone and non-JAG-like, and it beats the JAG bound for the undirected case. Monotonicity is not a property real logspace algorithms respect.
- **Catalytic and Cook–Mertz effects.** The recent tree-evaluation and catalytic-computation results (Buhrman–Cleve–Koucký–Loff–Speelman 2014) show that "obviously space-wasteful" recursion can be compressed by algebraic reuse of memory. Several conjectured barriers to $\mathsf{L}=\mathsf{NL}$ were built on such intuitions and have now been falsified, so the community's confidence in *lower-bound* heuristics has weakened.
- **Natural proofs / pseudorandomness.** A separation would yield explicit hard functions for a nonuniform model; and unconditional derandomization $\mathsf{BPL}=\mathsf{L}$ is itself equivalent to circuit-lower-bound-flavored statements, entangling the problem with the general hardness-vs-randomness program.

## 6. The Gap

Proven: $\mathrm{STCON} \in \mathsf{DSPACE}(\log^2 n)$; $\mathrm{USTCON} \in \mathsf{DSPACE}(\log n)$; monotone and JAG models require $\log^2 n$ space (equivalently $n^{\Theta(\log n)}$ size). Needed: a bound on $\mathsf{DSPACE}(\log n)$ for directed reachability, or an algorithm.

The gap is the quadratic factor between $\log n$ and $\log^2 n$. Concretely:

1. **Algorithmic side.** Reingold's method makes undirected graphs into constant-degree expanders in logspace, so that diameter $O(\log n)$ makes brute-force path search feasible. Directed graphs admit no analogous logspace-computable "derandomized rotation"; directed expansion is not preserved by the zig-zag product, and directed random walks need not be rapidly mixing or even reversible. **Closing the gap algorithmically means finding a directed substitute for reversibility.**
2. **Lower-bound side.** One must remove the monotonicity restriction from Potechin's $n^{\Omega(\log n)}$ switching-network bound, or the "graph-access-only" restriction from NNJAG bounds. No known technique proves a superpolynomial size lower bound for a general (non-monotone) branching program on any explicit function.

Even improving Savitch to $O(\log^{2-\epsilon} n)$ for directed reachability is open and would be a landmark.

## 7. Current Research (as of June 2026)

- **Catalytic space and Cook–Mertz recursion.** Following Cook–Mertz (STOC 2024) and Williams (STOC 2025, $\mathsf{TIME}[t] \subseteq \mathsf{SPACE}[\sqrt{t\log t}]$), groups at Toronto (Cook, Mertz), MIT (Williams), and CWI/QuSoft (Buhrman, Koucký, Loff, Speelman) are testing whether the same low-degree-polynomial memory-reuse trick applies to reachability. To date it has not broken $\log^2 n$ for $\mathrm{STCON}$; a $o(\log^2 n)$ claim should be treated as *(frontier — verify)*.
- **Derandomizing space.** Hoza–Zuckerman, Pyne–Vadhan, Chattopadhyay–Liao and Cohen–Doron–Sberlo pursue $\mathsf{BPL} = \mathsf{L}$ via weighted pseudorandom generators; Hoza's 2022 survey catalogs the state. $\mathsf{RL}=\mathsf{L}$ would not settle $\mathsf{L}$ vs $\mathsf{NL}$, but it removes randomness as a confounder.
- **Monotone and lifting-based lower bounds.** Göös, Pitassi, Watson and collaborators use query-to-communication lifting to transfer $\Omega(\log^2 n)$-type bounds; Potechin's Fourier-analytic framework for switching networks continues to be extended (Chan–Potechin, Robere–Pitassi–Tzameret–Göös on monotone span programs).
- **Unambiguity.** Whether $\mathsf{NL} = \mathsf{UL}$ unconditionally, and whether reachability in min-unique graphs generalizes, remains actively studied (Allender, Tewari, Vinodchandran, Datta).
- **Descriptive complexity.** Ongoing work on whether $\mathrm{TC}$ is definable from $\mathrm{DTC}$ over unordered structures, and on symmetric/choiceless models where separations *are* provable.

## 8. Future Work

- Construct a logspace-computable transformation of arbitrary digraphs into digraphs with $\mathrm{polylog}$ diameter preserving reachability — the directed analogue of Reingold's expander construction. Wigderson has repeatedly named this the natural target.
- Improve Savitch: any deterministic $O(\log^{2-\epsilon} n)$ algorithm for $\mathrm{STCON}$, or a $n^{1-\epsilon}$-space polynomial-time algorithm improving Barnes–Buss–Ruzzo–Schieber.
- Extend Potechin's monotone bound to *non-monotone* switching networks with limited negation, or prove $n^{\omega(1)}$ size for any explicit function in $\mathsf{NL}$ against general branching programs.
- Prove $\mathsf{NL} \neq \mathsf{L}$ conditionally on plausible hardness assumptions, thereby locating the problem in the hardness-vs-randomness landscape.
- Determine whether catalytic space $\mathsf{CL}$ contains $\mathsf{NL}$, and whether $\mathsf{CL} = \mathsf{L}$; this is now the most active adjacent question.

## 9. Key References

- **[Foundational]** Walter J. Savitch. *Relationships between nondeterministic and deterministic tape complexities.* Journal of Computer and System Sciences, 4(2):177–192, 1970.
- **[Foundational]** Neil Immerman. *Nondeterministic space is closed under complementation.* SIAM Journal on Computing, 17(5):935–938, 1988.
- **[Foundational]** Róbert Szelepcsényi. *The method of forced enumeration for nondeterministic automata.* Acta Informatica, 26(3):279–284, 1988.
- **[Foundational]** Neil D. Jones. *Space-bounded reducibility among combinatorial problems.* Journal of Computer and System Sciences, 11(1):68–85, 1975.
- **[SOTA]** Omer Reingold. *Undirected connectivity in log-space.* Journal of the ACM, 55(4):Article 17, 2008.
- **[SOTA]** Aaron Potechin. *Bounds on monotone switching networks for directed connectivity.* Journal of the ACM, 64(1):Article 4, 2017 (FOCS 2010).
- **[SOTA]** James Cook and Ian Mertz. *Tree evaluation is in space $O(\log n \cdot \log\log n)$.* Proceedings of STOC 2024.
- **[SOTA]** R. Ryan Williams. *Simulating time with square-root space.* Proceedings of STOC 2025.
- **[SOTA]** Klaus Reinhardt and Eric Allender. *Making nondeterminism unambiguous.* SIAM Journal on Computing, 29(4):1118–1131, 2000.
- **[SOTA]** Michael Saks and Shiyu Zhou. *$\mathsf{BP}_H\mathsf{SPACE}(S) \subseteq \mathsf{DSPACE}(S^{3/2})$.* Journal of Computer and System Sciences, 58(2):376–403, 1999.
- **[SOTA]** Michael Elberfeld, Andreas Jakoby, Till Tantau. *Logspace versions of the theorems of Bodlaender and Courcelle.* FOCS 2010.
- **[Survey]** Avi Wigderson. *The complexity of graph connectivity.* Mathematical Foundations of Computer Science (MFCS) 1992, LNCS 629, 112–132.
- **[Survey]** William Hoza. *Recent progress on derandomizing space-bounded computation.* Bulletin of the EATCS, No. 138, 2022.
- **[Survey]** Neil Immerman. *Descriptive Complexity.* Springer, 1999.
- **[Textbook]** Sanjeev Arora and Boaz Barak. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009 (Chapter 4).

## 10. Worked Example / Concrete Special Case

**Instance.** Let $G$ be the digraph on $V=\{1,\dots,8\}$ with edges
$$1\to2,\;1\to3,\;2\to4,\;3\to4,\;4\to5,\;5\to6,\;6\to7,\;3\to8,$$
$s=1$, $t=7$.

**Nondeterministic logspace.** The machine stores only the current vertex ($\lceil \log 8\rceil = 3$ bits) and a step counter ($\le 3$ bits). It guesses $1\to2\to4\to5\to6\to7$ and accepts. Total workspace: $6$ bits $= O(\log n)$. Note it never stores the path — that would need $\Theta(n\log n)$ bits.

**Savitch's deterministic simulation.** Compute $\mathrm{REACH}(1,7,8)$ by
$$\mathrm{REACH}(u,v,2^k)=\bigvee_{w=1}^{8}\big[\mathrm{REACH}(u,w,2^{k-1}) \wedge \mathrm{REACH}(w,v,2^{k-1})\big].$$
Depth is $\log_2 8 = 3$; each stack frame stores $(u,v,w,k)$, i.e. $3\cdot 3 + 2 = 11$ bits. Peak space $= 3 \times 11 = 33$ bits $= \Theta(\log^2 n)$. Trace of the successful branch: $\mathrm{REACH}(1,7,8)$ picks $w=4$, giving $\mathrm{REACH}(1,4,4)$ (which picks $w=2$: $1\to2$, $2\to4$) and $\mathrm{REACH}(4,7,4)$ (picks $w=6$: $4\to5\to6$, $6\to7$). Every subcall bottoms out at $\mathrm{REACH}(x,y,1)$, a single edge lookup on the input tape — free.

**Where the extra $\log n$ factor comes from.** The recursion re-derives $\mathrm{REACH}(1,4,4)$ from scratch each time it is needed rather than caching it; caching would need $\Omega(n^2)$ bits. The $\log n$ stack frames of $\log n$ bits each are precisely the quadratic gap of Section 6.

**Contrast with the undirected case.** Replace every arc by an undirected edge. Reingold's algorithm applies: after $O(\log n)$ rounds of zig-zag powering, $G$ becomes a constant-degree expander of diameter $O(\log n)$, and a *deterministic* enumeration of all $d^{O(\log n)} = \mathrm{poly}(n)$ walk-labels from $s$ — each label stored in $O(\log n)$ bits, one at a time — decides connectivity in $O(\log n)$ space. The step that breaks in the directed case is the very first one: the zig-zag product requires the rotation map $\mathrm{Rot}(v,i)=(u,j)$ to be an involution, i.e. edges traversable in both directions. In our $G$, $3\to8$ has no reverse, and no logspace-computable repair is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*