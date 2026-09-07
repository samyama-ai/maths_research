---
id: 07-combinatorics/frankls-conjecture
title: "Frankl's Union-Closed Sets Conjecture"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Frankl's Union-Closed Sets Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/frankls-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mathcal{F}$ be a finite family of finite sets that is **union-closed**: $A, B \in \mathcal{F} \implies A \cup B \in \mathcal{F}$. Assume $\mathcal{F} \neq \{\emptyset\}$ and $\mathcal{F} \neq \emptyset$.

**Conjecture (Frankl, 1979).** There exists an element $x$ belonging to at least half of the members of $\mathcal{F}$:
$$\exists\, x \in \bigcup_{A \in \mathcal{F}} A \quad \text{such that} \quad \bigl|\{A \in \mathcal{F} : x \in A\}\bigr| \geq \tfrac{1}{2}|\mathcal{F}|.$$

A complete proof must establish this for **all** union-closed families, with no bound on the ground set size $m = |\bigcup_{A\in\mathcal{F}} A|$ or the family size $n = |\mathcal{F}|$. A disproof requires exhibiting one union-closed family in which every element has frequency strictly below $n/2$.

The bound $1/2$ is sharp: for $\mathcal{F} = 2^{[m]}$ every element sits in exactly $2^{m-1} = n/2$ sets. Infinitely many other extremal families exist, so no strengthening beyond $\lceil n/2 \rceil$ is possible.

## 2. Mathematical Foundations

**Frequencies.** For a family $\mathcal{F}$ on ground set $U$, write $n = |\mathcal{F}|$ and, for $x \in U$,
$$d_{\mathcal{F}}(x) = |\{A \in \mathcal{F} : x \in A\}|, \qquad \alpha(\mathcal{F}) = \max_{x \in U} \frac{d_{\mathcal{F}}(x)}{n}.$$
The conjecture asserts $\alpha(\mathcal{F}) \geq 1/2$ for every union-closed $\mathcal{F} \neq \{\emptyset\}$. Define the universal constant
$$c^{\star} = \inf \{\alpha(\mathcal{F}) : \mathcal{F} \text{ union-closed}, \ \mathcal{F} \neq \{\emptyset\}\}.$$
The conjecture is exactly $c^\star = 1/2$.

**Normalizations.** One may assume without loss of generality that $\emptyset \in \mathcal{F}$, that $U \in \mathcal{F}$, and that $\mathcal{F}$ **separates** points ($x \neq y \implies \exists A \in \mathcal{F}$ containing exactly one of them). Under separation, $m \le n - 1$ and in fact $n \ge 2^{?}$-type relations constrain the pair $(n,m)$.

**Lattice form.** A union-closed separating family, ordered by inclusion, is a finite lattice $L$ with join $\cup$; conversely every finite lattice arises this way. An element $j \in L$ is **join-irreducible** if $j = a \vee b$ forces $j \in \{a,b\}$. Frankl's conjecture is equivalent (Poonen 1992; Abe–Nakano; Reinhold 2000) to:

> Every finite lattice $L$ with $|L| \ge 2$ contains a join-irreducible $j$ such that $|\{x \in L : x \ge j\}| \le \tfrac{1}{2}|L|$.

**Dual (intersection-closed) form.** By complementation within $U$, $\mathcal{F}$ union-closed with $n$ sets is equivalent to an intersection-closed family in which some element lies in at most half the sets.

**Graph form** (Bruhn–Charbit–Schaudt–Telle 2015). For a graph $G$, let $\mathcal{F}_G$ be the union-closure of the maximal independent sets of $G$; call a vertex $v$ *rare* if $d_{\mathcal{F}_G}(v) < |\mathcal{F}_G|/2$. Frankl's conjecture is equivalent to: **every finite graph with at least one edge has two adjacent vertices that are both non-rare.**

**Entropy machinery** (Gilmer 2022). Let $X, Y$ be i.i.d. uniform on $\mathcal{F}$. Since $X \cup Y \in \mathcal{F}$,
$$H(X \cup Y) \leq \log_2 n = H(X).$$
If every element has frequency $< cn$, one shows $H(X\cup Y) > H(X)$ for suitable $c$ — a contradiction. The engine is the scalar inequality, for $p \in [0,1/2]$ and $h(p) = -p\log_2 p - (1-p)\log_2(1-p)$,
$$h(2p - p^2) \geq \varphi \cdot h(p), \qquad \varphi = \frac{1+\sqrt5}{2},$$
whose failure point governs the achievable constant.

## 3. History & State of the Art (SOTA)

- **1979.** Péter Frankl poses the conjecture (circulated at a Banff conference; first in print via Duffus in *Graphs and Order*, 1985).
- **1980s–90s.** Reformulations proliferate: lattice-theoretic (Poonen 1992; Abe–Nakano), weighted versions, "FC-families" (families forcing the conjecture for every union-closed family containing them).
- **1994.** Knill: some element has frequency at least $(n-1)/\log_2 n$ — a $\Theta(n/\log n)$ bound, still $o(n)$.
- **1999.** Wójcik improves the constant in the $n/\log n$ regime.
- **2003.** Reimer: the average set size of a union-closed family with $n$ sets is at least $\tfrac12 \log_2 n$.
- **2013.** Balla, Bollobás, Eccles prove the conjecture for all families with $n \geq \tfrac{2}{3}2^m$ sets.
- **November 2022 — the breakthrough.** Gilmer gives the first **constant** lower bound $c^\star \geq 0.01$ using entropy. Within weeks, four independent groups (Sawin; Chase–Lovett; Alweiss–Huang–Sellke; Pebody) push this to
$$c^\star \geq \frac{3-\sqrt5}{2} \approx 0.38197,$$
the reciprocal-golden-ratio barrier of the method. Sawin then shows the constant is **strictly** larger; Cambie and (independently) Yu quantify it numerically at $\approx 0.38234$.
- **2023–2026.** The bound has not moved materially. Effort has shifted to structural and lattice-side approaches and to explaining the $0.38$ barrier.

**Status:** partially-solved — proven for many structured classes and for a constant fraction bound, open in general.

## 4. Partial Results / Verified Cases

**Small parameters (computational).**
- $m \le 11$: Bošnjak–Marković (2008), *The 11-element case of Frankl's conjecture*.
- $m \le 12$: Vučković–Živković (2017).
- $n \le 46$ sets: Roberts–Simpson (2010); extended to $n \le 50$ by Vučković–Živković.

**Density regimes.**
- $n \geq \tfrac{2}{3}2^m$ (Balla–Bollobás–Eccles 2013).
- $n \geq 2^{m-1}$ (Karpas 2017), by Fourier/analytic methods.
- Very small $n$ relative to $m$: if $n \le 2m$ the conjecture holds (Falgas-Ravry and earlier work of Nishimura–Takahashi).

**Structural classes.**
- $\mathcal{F}$ contains a singleton $\{a\}$ or a pair $\{a,b\}$ — an easy but instructive case (Section 10).
- $\mathcal{F}$ contains a 3-element set: Sarvate–Renaud-type arguments handle most configurations.
- Lattices: lower semimodular lattices (Reinhold 2000), modular and geometric lattices, relatively complemented lattices, planar lattices (Zaguia), lattices of dimension $\le 2$.
- Graph form: chordal graphs, bipartite graphs, subcubic graphs, chordal bipartite graphs, series-parallel graphs (Bruhn–Charbit–Schaudt–Telle 2015 and follow-ups).

**Universal bound.** For every union-closed $\mathcal{F}$, some element has frequency at least $0.38197\,n$ — and, by Sawin's refinement, at least $\approx 0.38234\,n$. The gap to the conjectured $0.5$ is roughly $0.118\,n$.

## 5. Principal Obstacles

- **No usable global structure.** Union-closed families are closed under an operation with no inverse and no group action. There is no ambient algebraic symmetry to exploit, so Fourier-analytic tools (which need a product measure or a group) apply only when $\mathcal{F}$ is dense inside $2^{[m]}$ — exactly the regime already solved.
- **The extremal set is enormous and unstructured.** Tight examples ($\alpha = 1/2$) include $2^{[m]}$ but also many sparse and irregular families; no classification exists, so stability/compactness arguments have nothing to converge to.
- **Averaging fails.** The natural averaging statement — that the *average* frequency is $\ge n/2$ — is false. Some families have average frequency $\Theta(n \log m / m)$, so the maximum must be extracted, not averaged.
- **The $(3-\sqrt5)/2$ barrier is intrinsic to the entropy method.** Gilmer, and Chase–Lovett, exhibit distributions (not union-closed families, but valid for the relaxation the proof uses) achieving $\alpha = (3-\sqrt5)/2$. Any argument that only uses "$X\cup Y$ is supported on $\mathcal{F}$" plus subadditivity of entropy cannot exceed this. Sawin's improvement uses the correlation between $X$ and $X\cup Y$ and gains only $\sim 4\times10^{-4}$.
- **Induction breaks.** Deleting or contracting an element does not preserve union-closedness in a controlled way; the natural reductions ($\mathcal{F}_x = \{A : x \in A\}$, $\mathcal{F}_{\bar x}$) are union-closed but their sizes are exactly the unknowns being bounded.
- **Lattice side is equally hard.** Reinhold's semimodularity proof uses a rank function; general finite lattices have none, and known counterexamples to natural strengthenings rule out rank-free substitutes.

## 6. The Gap

Proven: $c^\star \ge 0.38234$; conjectured $c^\star = 1/2$. The gap is a **constant-factor** gap of about $0.118$, not an asymptotic one, and it is not closable by tuning the current proof: the entropy relaxation provably saturates at $(3-\sqrt5)/2$, so the remaining $0.118$ requires an argument that uses a property of union-closed families beyond "the union of two members is a member." Concretely, the missing step is either

1. a new invariant (a weighting, a rank, or a submodular potential) that distinguishes genuine union-closed families from the entropy method's fictitious near-extremal distributions; or
2. a structural classification of families with $\alpha(\mathcal{F}) < 1/2 + \epsilon$, sharp enough to force a contradiction.

Verified cases ($m \le 12$, $n \le 50$, dense families, semimodular lattices) cover no infinite "generic" regime: sparse families on large ground sets with all frequencies near $0.4n$ remain entirely untouched.

## 7. Current Research (as of June 2026)

- **Refining the entropy constant.** Post-2023 work (Cambie; Yu; Liu) squeezes the Gilmer–Sawin framework with better scalar inequalities and dimension-free formulations. Gains are in the fourth decimal place; consensus is that the method is exhausted near $0.3824$. *(frontier — verify)*
- **Approximate and asymmetric versions.** Chase–Lovett's "approximate union-closed" statement — for any $\epsilon$, a family with all frequencies $< (1/2-\epsilon)n$ must be far from union-closed in a measurable sense — is being sharpened into a stability theorem.
- **Lattice-theoretic programs.** Groups in universal algebra (Novi Sad, following Bošnjak–Marković; Czech and Slovenian lattice-theory groups) extend the join-irreducible formulation to new lattice varieties.
- **Graph formulation.** Bruhn–Schaudt-style work (Hamburg, Bergen) keeps adding graph classes; the current frontier is graphs of bounded treewidth and $H$-free classes. *(frontier — verify)*
- **Computer search and SAT/ILP.** Verification beyond $m = 12$ is bounded by the double-exponential count of union-closed families; targeted searches now look for families with $\alpha < 0.45$ rather than exhaustive enumeration.
- **Formalization.** Portions of the Gilmer–Sawin argument have been checked in Lean/mathlib-adjacent projects. *(frontier — verify)*

## 8. Future Work

- **Break the golden-ratio barrier.** Find a second constraint on $(X, Y, X\cup Y)$ — e.g. using three-fold unions $X \cup Y \cup Z$, or the lattice's join-irreducible count — that the fictitious extremizers violate.
- **Classify near-extremal families.** Prove that $\alpha(\mathcal{F}) \le 1/2 + o(1)$ forces $\mathcal{F}$ to be close to a power set or a "cube-like" family.
- **FC-family program.** Enumerate more forcing families: if a modest finite family $\mathcal{G}$ can be shown to force the conjecture whenever $\mathcal{G} \subseteq \mathcal{F}$, the residual case shrinks. Existing FC-families cover small ground sets only.
- **Weighted / fractional relaxations.** Poonen's weighted characterization suggests attacking an LP-dual: find nonnegative weights certifying frequency $\ge n/2$ for all families simultaneously; determine whether such a certificate can exist.
- **Resolve the graph version for all graphs of maximum degree $\le 4$**, the first open degree case, as a testbed.

## 9. Key References

- **[Foundational]** Bjorn Poonen. *Union-closed families.* Journal of Combinatorial Theory, Series A, 59(2):253–268, 1992.
- **[Foundational]** Edward Knill. *Graph generated union-closed families of sets.* arXiv:math/9409215, 1994.
- **[Foundational]** Jürgen Reinhold. *Frankl's conjecture is true for lower semimodular lattices.* Algebra Universalis, 43:267–271, 2000.
- **[Partial]** Piotr Wójcik. *Union-closed families of sets.* Discrete Mathematics, 199:173–182, 1999.
- **[Partial]** David Reimer. *An average set size theorem.* Combinatorics, Probability and Computing, 12:89–93, 2003.
- **[Partial]** Ivica Bošnjak, Petar Marković. *The 11-element case of Frankl's conjecture.* Electronic Journal of Combinatorics, 15:R88, 2008.
- **[Partial]** Ian Roberts, Jamie Simpson. *A note on the union-closed sets conjecture.* Australasian Journal of Combinatorics, 47:265–267, 2010.
- **[Partial]** Igor Balla, Béla Bollobás, Tom Eccles. *Union-closed families of sets.* Journal of Combinatorial Theory, Series A, 120:531–544, 2013.
- **[Partial]** Henning Bruhn, Pierre Charbit, Oliver Schaudt, Jan Arne Telle. *The graph formulation of the union-closed sets conjecture.* European Journal of Combinatorics, 43:210–219, 2015.
- **[Partial]** Ilan Karpas. *Two results on union-closed families.* arXiv:1708.01434, 2017.
- **[Partial]** Bojan Vučković, Miodrag Živković. *The 12-element case of Frankl's conjecture.* IPSI BgD Transactions on Internet Research, 13(1):65–71, 2017.
- **[SOTA]** Justin Gilmer. *A constant lower bound for the union-closed sets conjecture.* arXiv:2211.09055, 2022.
- **[SOTA]** Will Sawin. *An improved lower bound for the union-closed set conjecture.* arXiv:2211.11504, 2022.
- **[SOTA]** Zachary Chase, Shachar Lovett. *Approximate union closed conjecture.* arXiv:2211.11689, 2022.
- **[SOTA]** Ryan Alweiss, Brice Huang, Mark Sellke. *Improved lower bound for Frankl's union-closed sets conjecture.* Electronic Journal of Combinatorics, 31(1):P1.11, 2024.
- **[SOTA]** Luke Pebody. *Extension of a method of Gilmer.* arXiv:2211.13139, 2022.
- **[Survey]** Henning Bruhn, Oliver Schaudt. *The journey of the union-closed sets conjecture.* Graphs and Combinatorics, 31:2043–2074, 2015.

## 10. Worked Example / Concrete Special Case

**(a) A small family, computed.** Take
$$\mathcal{F} = \bigl\{\ \emptyset,\ \{1\},\ \{2\},\ \{1,2\},\ \{1,3\},\ \{1,2,3\}\ \bigr\}, \qquad n = 6.$$
Union-closedness: $\{1\}\cup\{2\}=\{1,2\}\in\mathcal F$; $\{2\}\cup\{1,3\}=\{1,2,3\}\in\mathcal F$; $\{1,2\}\cup\{1,3\}=\{1,2,3\}\in\mathcal F$; all other pairs give members already listed. Frequencies:
$$d(1) = 4,\quad d(2) = 3,\quad d(3) = 2, \qquad n/2 = 3.$$
Elements $1$ and $2$ both meet the threshold; element $3$ does not. Note $\alpha(\mathcal F) = 4/6 = 2/3 > 1/2$, so the family is not extremal.

**(b) A complete proof of a genuine special case: $\mathcal{F}$ contains a 2-element set.**

Suppose $\{a,b\} \in \mathcal{F}$. Partition $\mathcal{F}$ by the trace on $\{a,b\}$:
$$\mathcal{F} = \mathcal{N} \sqcup \mathcal{A} \sqcup \mathcal{B} \sqcup \mathcal{C},$$
where $\mathcal{N}$ contains neither $a$ nor $b$, $\mathcal{A}$ contains $a$ only, $\mathcal{B}$ contains $b$ only, $\mathcal{C}$ contains both.

Define $\phi : \mathcal{N} \to \mathcal{C}$ by $\phi(S) = S \cup \{a,b\}$. Since $S \in \mathcal{F}$ and $\{a,b\} \in \mathcal{F}$, union-closedness gives $\phi(S) \in \mathcal{F}$, and clearly $a,b \in \phi(S)$, so $\phi(S) \in \mathcal{C}$. The map is injective: if $S \cup \{a,b\} = T \cup \{a,b\}$ with $S,T$ containing neither $a$ nor $b$, then $S = T$. Hence
$$|\mathcal{N}| \leq |\mathcal{C}|.$$
Now
$$d(a) + d(b) = \bigl(|\mathcal{A}| + |\mathcal{C}|\bigr) + \bigl(|\mathcal{B}| + |\mathcal{C}|\bigr) = |\mathcal{A}| + |\mathcal{B}| + 2|\mathcal{C}| \geq |\mathcal{A}| + |\mathcal{B}| + |\mathcal{C}| + |\mathcal{N}| = n.$$
So $\max\{d(a), d(b)\} \geq n/2$. $\blacksquare$

In example (a), $\{1,2\} \in \mathcal{F}$: here $\mathcal{N} = \{\emptyset\}$, $\mathcal{A} = \{\{1\},\{1,3\}\}$, $\mathcal{B} = \{\{2\}\}$, $\mathcal{C} = \{\{1,2\},\{1,2,3\}\}$, and indeed $|\mathcal N| = 1 \le 2 = |\mathcal C|$ and $d(1)+d(2) = 7 \ge 6$.

**(c) Why this does not generalize.** The argument depends on having a *small* member to union with. If the minimum nonempty member has size $k$, the same injection only yields $\sum_{x \in S_0} d(x) \geq n$ for a $k$-set $S_0$, giving $\max_x d(x) \ge n/k$ — which degrades to nothing as $k$ grows. Knill's $(n-1)/\log_2 n$ bound is essentially the best that this "small generator" philosophy delivers; the constant-factor bound $0.38n$ required the entirely different entropy argument of Section 2.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*