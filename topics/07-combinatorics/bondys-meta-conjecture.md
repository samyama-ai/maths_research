---
id: 07-combinatorics/bondys-meta-conjecture
title: "Bondy's Meta-Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bondy's Meta-Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/bondys-meta-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

In 1971 J. A. Bondy wrote, at the end of *Pancyclic graphs I*:

> "almost any nontrivial condition on a graph which implies that the graph is Hamiltonian also implies that the graph is pancyclic (except for maybe a simple family of exceptional graphs)."

This is a **meta-conjecture**: a claim about the class of theorems, not a single first-order statement. It cannot be proved or disproved as written, because "nontrivial condition" and "simple family of exceptions" are not formalized. Its research content is a *program*:

- **(P1)** For each known sufficient condition $\mathcal{C}$ for Hamiltonicity, decide whether $\mathcal{C}$ implies pancyclicity, and if not, determine the complete exceptional family $\mathcal{E}(\mathcal{C})$.
- **(P2)** Decide whether $\mathcal{E}(\mathcal{C})$ is "simple" — typically finite up to isomorphism, or a single parametrized family such as $\{K_{n/2,n/2}\}$.
- **(P3)** Identify conditions that genuinely violate the principle, and explain the structural feature (usually forced bipartiteness or forced sparseness) that causes the violation.

A **complete resolution** of any instance means: a theorem of the form "$G$ satisfies $\mathcal{C}$ $\Rightarrow$ $G$ is pancyclic or $G \in \mathcal{E}(\mathcal{C})$", together with a proof that every member of $\mathcal{E}(\mathcal{C})$ really fails pancyclicity. The headline open instance is the **Chvátal–Erdős pancyclicity conjecture** (Section 4).

## 2. Mathematical Foundations

Let $G=(V,E)$ be a finite simple graph, $n=|V|$, $e(G)=|E|$, $\delta(G)$ the minimum degree, $\kappa(G)$ the vertex connectivity, $\alpha(G)$ the independence number, $\tau(G)$ the toughness. Let $C_\ell$ denote a cycle of length $\ell$ and $g(G)$ the girth.

**Definitions.**
- $G$ is **Hamiltonian** if it contains a cycle of length $n$.
- $G$ is **pancyclic** if it contains $C_\ell$ for every $\ell$ with $3 \le \ell \le n$.
- $G$ is **vertex-pancyclic** if every $v \in V$ lies on a $C_\ell$ for every $3 \le \ell \le n$.
- A bipartite $G$ with parts of size $n/2$ is **bipancyclic** if it contains $C_{2k}$ for every $2 \le k \le n/2$.

**Baseline Hamiltonicity conditions** (each an instance of the program):

$$\text{(Dirac, 1952)}\quad \delta(G) \ge n/2,\ n\ge 3 \ \Longrightarrow\ G \text{ Hamiltonian.}$$
$$\text{(Ore, 1960)}\quad \forall\, uv \notin E:\ d(u)+d(v) \ge n \ \Longrightarrow\ G \text{ Hamiltonian.}$$
$$\text{(Chvátal, 1972)}\quad d_1 \le \cdots \le d_n,\ \ \forall i < n/2:\ d_i \le i \Rightarrow d_{n-i} \ge n-i \ \Longrightarrow\ G \text{ Hamiltonian.}$$
$$\text{(Chvátal–Erdős, 1972)}\quad \kappa(G) \ge \alpha(G),\ n \ge 3 \ \Longrightarrow\ G \text{ Hamiltonian.}$$
$$\text{(Häggkvist–Nicoghossian, 1981)}\quad G\ 2\text{-connected},\ \delta(G) \ge \tfrac{n+\kappa(G)}{3} \ \Longrightarrow\ G \text{ Hamiltonian.}$$
$$\text{(Fan, 1984)}\quad G\ 2\text{-connected},\ \forall u,v:\ d(u,v)=2 \Rightarrow \max\{d(u),d(v)\}\ge n/2 \ \Longrightarrow\ G \text{ Hamiltonian.}$$

**The canonical obstruction.** $K_{n/2,n/2}$ ($n$ even) satisfies Dirac, Ore, Chvátal and Fan, is Hamiltonian, and is bipartite, hence has no odd cycle: it is Hamiltonian but not pancyclic. It is the "simple family of exceptional graphs" Bondy had in mind. The second recurring exception is $C_5$, which satisfies $\kappa = \alpha = 2$ but has no $C_3$ or $C_4$.

**Bondy's edge theorem** (the metric form of the principle):
$$G \text{ Hamiltonian},\ e(G) \ge n^2/4 \ \Longrightarrow\ G \text{ pancyclic or } G \cong K_{n/2,n/2}.$$

## 3. History & State of the Art (SOTA)

- **1971.** Bondy, *Pancyclic graphs I* (JCTB 11): proves that Ore's condition implies pancyclic or $K_{n/2,n/2}$, proves the edge theorem above, and states the meta-conjecture.
- **1974.** Schmeichel and Hakimi (JCTB 17) attack the Bondy–Chvátal conjecture — that Chvátal's degree-sequence condition implies pancyclicity up to $K_{n/2,n/2}$ — settling substantial cases.
- **1975.** Bondy, *Pancyclic graphs: recent results* (Colloq. Math. Soc. J. Bolyai 10), the first survey framed around the meta-conjecture.
- **1976.** Bondy and Chvátal, *A method in graph theory* (Discrete Math. 15): the closure operation, which mechanizes the transfer of degree-type conditions and became the standard tool for the program.
- **1987.** Benhocine and Wojda (JCTB 42) settle the pancyclic version of Fan's condition.
- **1990.** Bauer and Schmeichel, *Hamiltonian degree conditions which imply a graph is pancyclic* (JCTB 48): a uniform treatment showing the conditions of Bondy, Chvátal, Fan and Häggkvist–Nicoghossian all force pancyclicity up to a short explicit exception list. This is the strongest confirmation of the principle for degree-type hypotheses.
- **1991.** Amar, Fournier and Germa, *Pancyclism in Chvátal–Erdős graphs* (Graphs and Combinatorics 7): the first substantial progress on the connectivity/independence instance.
- **2010.** Keevash and Sudakov (JCTB 100) prove that $\kappa(G) \ge 600\,\alpha(G)$ forces pancyclicity — the meta-conjecture for Chvátal–Erdős up to a constant factor.
- **2000.** Bauer, Broersma and Veldman construct 2-tough non-Hamiltonian graphs, showing that the Hamiltonicity side of the toughness instance is itself unsettled.
- **2020s.** Sudakov's school (Draganić, Munhá Correia, Sudakov) revisits pancyclicity with expander and absorption machinery, improving the Keevash–Sudakov constant *(frontier — verify the exact constant in the published version)*.

## 4. Partial Results / Verified Cases

Confirmed instances, with exact exception families:

| Condition | Pancyclicity verdict | Exceptions |
|---|---|---|
| Ore, $d(u)+d(v)\ge n$ | pancyclic (Bondy 1971) | $K_{n/2,n/2}$ |
| Dirac, $\delta \ge n/2$ | pancyclic (corollary) | $K_{n/2,n/2}$ |
| $e(G) \ge n^2/4$ + Hamiltonian | pancyclic (Bondy 1971) | $K_{n/2,n/2}$ |
| Chvátal degree sequence | pancyclic (Schmeichel–Hakimi 1974; Bauer–Schmeichel 1990) | $K_{n/2,n/2}$ and a short explicit list |
| Fan's distance-2 condition | pancyclic (Benhocine–Wojda 1987) | $K_{n/2,n/2}$, $C_n$-type sparse cases |
| Häggkvist–Nicoghossian $\delta \ge (n+\kappa)/3$ | pancyclic (Bauer–Schmeichel 1990) | $K_{n/2,n/2}$, small explicit graphs |
| Strong tournaments (digraphs) | vertex-pancyclic (Moon 1966) | none |
| $G(n,p)$ at the Hamiltonicity threshold | pancyclic (Cooper–Frieze) | none a.a.s. |
| $\kappa \ge \alpha$, triangle-free | cycles of many lengths (Lou 1996) | $C_5$, $K_{n/2,n/2}$ |
| $\kappa(G) \ge 600\,\alpha(G)$ | pancyclic (Keevash–Sudakov 2010) | none |

The **open flagship**: Erdős asked whether $\kappa(G) \ge \alpha(G)$ with $n \ge n_0(\alpha)$ forces pancyclicity. Amar–Fournier–Germa established cycles of all lengths in a large initial range (up to roughly $n-\alpha$) under $\kappa \ge \alpha$, but the full range $3 \le \ell \le n$ with $\kappa \ge \alpha$ exactly is unresolved. The bipartite analogue (Hamiltonian conditions $\Rightarrow$ bipancyclic) is confirmed in the Ore/Moon–Moser regime by Schmeichel and Mitchem (1982).

## 5. Principal Obstacles

- **The meta-conjecture is not a theorem-shaped object.** No proof technique can quantify over "all nontrivial conditions". Progress is necessarily instance-by-instance, so the program has no terminating criterion.
- **Rotation–extension breaks at short lengths.** The standard Hamiltonicity toolkit (Pósa rotation, the Bondy–Chvátal closure, Woodall's hopping lemma) manipulates *long* paths and cycles. Producing a $C_3$ or $C_4$ requires local density, which global connectivity hypotheses like $\kappa \ge \alpha$ do not supply. This is exactly why the Chvátal–Erdős instance resists: the hypothesis is scale-free while the conclusion at $\ell=3$ is local.
- **Closure is not pancyclicity-preserving in an obvious way.** $G$ and its Bondy–Chvátal closure $\mathrm{cl}(G)$ have the same Hamiltonicity status, but adding an edge $uv$ with $d(u)+d(v)\ge n$ can create short cycles that were absent in $G$. Every degree-type instance therefore needs a bespoke argument that unwinds the closure.
- **Extremal counting is tight only at $n^2/4$.** Bondy's edge theorem is sharp; below $n^2/4$ edges there is no counting proof, and one must argue structurally. Regularity/absorption methods, which dominate modern Dirac-type work, produce cycles of length $\Theta(n)$ and are blind to $\ell = O(1)$.
- **Genuine counterexamples exist.** Any condition forcing bipartiteness (e.g. Moon–Moser-type bipartite degree conditions, Jackson's theorem for 2-connected $k$-regular graphs with $n \le 3k$, where $K_{k,k}$ qualifies) kills all odd cycles. The principle therefore needs a hypothesis excluding bipartiteness, and no one has stated one that covers all known cases.
- **The toughness instance is blocked upstream.** Chvátal's conjecture that $\tau(G) \ge t_0$ implies Hamiltonicity is itself open, with $t_0 \ge 9/4$ forced by Bauer–Broersma–Veldman; the pancyclic analogue cannot be attempted first.

## 6. The Gap

For the Chvátal–Erdős instance the gap is a **multiplicative constant**: proven at $\kappa \ge 600\,\alpha$ (Keevash–Sudakov), conjectured at $\kappa \ge \alpha$. The slack is used to run a stability/expansion argument that needs many disjoint connectivity certificates; at $\kappa = \alpha$ there is exactly one, so no averaging is available.

For the program as a whole the gap is **definitional**: no one has produced a formal predicate $\Phi$ on graph properties such that "$\Phi(\mathcal{C})$ and $\mathcal{C} \Rightarrow$ Hamiltonian" entails "$\mathcal{C} \Rightarrow$ pancyclic modulo a finite union of parametrized families". Candidate formalizations — monotone properties, properties closed under the Bondy–Chvátal closure, properties invariant under edge addition — each admit bipartite counterexamples. Crossing the gap means either (i) finding such a $\Phi$, or (ii) accepting the meta-conjecture permanently as a heuristic and closing its instances one at a time.

## 7. Current Research (as of June 2026)

- **Zurich (Sudakov and coauthors: Draganić, Munhá Correia).** Expander-based pancyclicity: transferring the "sublinear expander" and absorption technology from Hamiltonicity to the full cycle spectrum. Recent work reduces the Keevash–Sudakov constant substantially *(frontier — verify the published constant and whether the bound is $O(\alpha)$ with a small explicit factor)*.
- **Cycle spectrum school.** Rather than all lengths, quantify $|\{\ell : C_\ell \subseteq G\}|$ under Hamiltonicity hypotheses; this weaker target is provable where full pancyclicity is not, and gives lower bounds approaching $n - o(n)$ under Chvátal–Erdős.
- **Digraphs and oriented graphs.** Kühn–Osthus-style semi-degree conditions; the tournament case (Moon) is the cleanest confirmation of the principle and motivates conjectural analogues for $c$-partite tournaments.
- **Hypergraphs.** Dirac-type thresholds for tight/loose Hamilton cycles are known; the corresponding "pancyclicity" question — all cycle lengths at the Hamiltonicity threshold — is largely open and is the most active new instance of the program.
- **Forbidden-subgraph instances.** Claw-free and $\{K_{1,3}, N\}$-free Hamiltonicity theorems (Ryjáček closure) with pancyclic strengthenings; the Ryjáček closure does not preserve short cycles, mirroring the Bondy–Chvátal difficulty.

## 8. Future Work

- Prove $\kappa(G) \ge \alpha(G)$, $n \ge n_0(\alpha)$ $\Rightarrow$ $G$ pancyclic or $G \in \{C_5, K_{n/2,n/2}\}$. Bondy and, later, Keevash and Sudakov both single this out as the decisive test.
- Reduce the Chvátal–Erdős constant to $\kappa \ge (1+\varepsilon)\alpha$; the current barrier is the absence of vertex-disjoint expansion certificates at $\kappa = \alpha$.
- Formalize a bipartiteness-excluding hypothesis $\Phi$ under which a general transfer theorem is provable; even a version restricted to monotone increasing properties would be the first genuine theorem *about* the meta-conjecture.
- Settle the hypergraph analogue: does the tight Hamilton cycle codegree threshold $n/2$ also force all cycle lengths?
- Establish the toughness instance conditionally: assuming Chvátal's toughness conjecture, does $\tau \ge t_0$ imply pancyclicity?
- Catalogue the failures. A systematic list of Hamiltonicity conditions that do *not* imply pancyclicity, with the structural reason in each case, would sharpen what "nontrivial" must mean.

## 9. Key References

- **[Foundational]** J. A. Bondy. *Pancyclic graphs I.* Journal of Combinatorial Theory, Series B, 11 (1971), 80–84.
- **[Foundational]** J. A. Bondy. *Pancyclic graphs: recent results.* In *Infinite and Finite Sets*, Colloq. Math. Soc. János Bolyai 10, North-Holland, 1975, pp. 181–187.
- **[Foundational]** V. Chvátal and P. Erdős. *A note on Hamiltonian circuits.* Discrete Mathematics, 2 (1972), 111–113.
- **[Foundational]** J. A. Bondy and V. Chvátal. *A method in graph theory.* Discrete Mathematics, 15 (1976), 111–135.
- **[Classical]** E. F. Schmeichel and S. L. Hakimi. *Pancyclic graphs and a conjecture of Bondy and Chvátal.* Journal of Combinatorial Theory, Series B, 17 (1974), 22–34.
- **[Classical]** D. Bauer and E. Schmeichel. *Hamiltonian degree conditions which imply a graph is pancyclic.* Journal of Combinatorial Theory, Series B, 48 (1990), 111–116.
- **[Classical]** A. Benhocine and A. P. Wojda. *The Geng-Hua Fan conditions for pancyclic or Hamilton-connected graphs.* Journal of Combinatorial Theory, Series B, 42 (1987), 167–180.
- **[Classical]** J. W. Moon. *On subtournaments of a tournament.* Canadian Mathematical Bulletin, 9 (1966), 297–301.
- **[Classical]** E. Schmeichel and J. Mitchem. *Bipartite graphs with cycles of all even lengths.* Journal of Graph Theory, 6 (1982), 429–439.
- **[SOTA / Recent]** P. Keevash and B. Sudakov. *Pancyclicity of Hamiltonian and highly connected graphs.* Journal of Combinatorial Theory, Series B, 100 (2010), 456–467.
- **[SOTA / Recent]** D. Amar, I. Fournier and A. Germa. *Pancyclism in Chvátal–Erdős graphs.* Graphs and Combinatorics, 7 (1991), 101–112.
- **[SOTA / Recent]** D. Bauer, H. J. Broersma and H. J. Veldman. *Not every 2-tough graph is Hamiltonian.* Discrete Applied Mathematics, 99 (2000), 317–321.
- **[Survey]** R. J. Gould. *Advances on the Hamiltonian problem — a survey.* Graphs and Combinatorics, 19 (2003), 7–52.
- **[Survey]** R. J. Gould. *Recent advances on the Hamiltonian problem: Survey III.* Graphs and Combinatorics, 30 (2014), 1–46.
- **[Textbook]** J. A. Bondy and U. S. R. Murty. *Graph Theory.* Springer GTM 244, 2008.

## 10. Worked Example / Concrete Special Case

Take $n=6$ and the Ore condition $d(u)+d(v)\ge 6$ for all non-adjacent $u,v$. Two graphs meet it; they are the whole story.

**(a) $K_{3,3}$ — the exception.** Parts $A=\{a_1,a_2,a_3\}$, $B=\{b_1,b_2,b_3\}$, $e=9$. Every vertex has degree $3$. Non-adjacent pairs lie inside a part, so $d(u)+d(v)=3+3=6=n$: Ore holds. It is Hamiltonian: $a_1b_1a_2b_2a_3b_3a_1$. But $K_{3,3}$ is bipartite, so its girth is $4$ and it contains no $C_3$ and no $C_5$. Its cycle spectrum is $\{4,6\}$, not $\{3,4,5,6\}$. Note $e(K_{3,3})=9=n^2/4$, so it sits exactly on the boundary of Bondy's edge theorem — the unique extremal graph there.

**(b) $K_{2,2,2}$ (the octahedron) — pancyclic.** Vertices $\{1,1',2,2',3,3'\}$ with $i \not\sim i'$ and all other pairs adjacent; $\delta = 4 \ge 3 = n/2$, $e = 12 > 9$. Ore holds ($4+4=8\ge 6$). Exhibit every length:
- $C_3$: $1\,2\,3\,1$.
- $C_4$: $1\,2\,1'\,2'\,1$.
- $C_5$: $1\,2\,3\,1'\,2'\,1$ — check adjacencies $1\sim2$, $2\sim3$, $3\sim1'$, $1'\sim2'$, $2'\sim1$. All hold.
- $C_6$: $1\,2\,3\,1'\,2'\,3'\,1$.

So $K_{2,2,2}$ is pancyclic, as Bondy's theorem predicts.

**What the example shows.** At $n=6$ the exceptional family is exactly $\{K_{3,3}\}$: any Ore graph on 6 vertices with $e \ge 10$ is pancyclic, and the only Ore graph with $e = 9$ that is not is $K_{3,3}$. The failure mechanism is parity, not sparseness — $K_{3,3}$ has the maximum possible number of edges for a triangle-free graph on 6 vertices. This is precisely why the meta-conjecture's exception clause is needed, and why any formalization must exclude bipartiteness rather than merely impose density.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*