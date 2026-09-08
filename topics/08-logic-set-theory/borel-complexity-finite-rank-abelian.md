---
id: 08-logic-set-theory/borel-complexity-finite-rank-abelian
title: "Borel Complexity of the Isomorphism Relation for Torsion-Free Abelian Groups of Finite Rank"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Borel Complexity of the Isomorphism Relation for Torsion-Free Abelian Groups of Finite Rank

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/borel-complexity-finite-rank-abelian` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\cong_n$ denote the isomorphism relation on the standard Borel space $R(n)$ of torsion-free abelian groups of rank exactly $n$. Baer (1937) classified $n=1$ completely; no satisfactory classification is known for any $n \ge 2$. The problem is to locate $\cong_n$ exactly in the Borel reducibility order $\le_B$ on countable Borel equivalence relations.

Established: $\cong_1 \sim_B E_0$, and $\cong_n <_B \cong_{n+1}$ strictly for every $n \ge 1$ (Thomas, 2003). The principal open questions are:

- **(Q1) Non-universality conjecture (Thomas).** For every $n \ge 1$, $\cong_n <_B E_\infty$, where $E_\infty$ is the universal countable Borel equivalence relation. Equivalently: the finite-rank classification problem never attains maximal complexity among countable Borel equivalence relations. A proof would have to produce, for each $n$, a Borel obstruction to reducing $E_\infty$ into $\cong_n$; a disproof would exhibit a Borel reduction $E_\infty \le_B \cong_n$ for some $n$.
- **(Q2) Structural invariants.** Identify a computable/definable invariant that witnesses the strict increase $\cong_n <_B \cong_{n+1}$ intrinsically, rather than through the ergodic-theoretic superrigidity argument.
- **(Q3) Treeability and essential freeness.** Is $\cong_2$ treeable? Is $\cong_n$ essentially free for any $n \ge 2$?

A complete solution means determining the $\le_B$-position of each $\cong_n$ relative to the known landmarks $E_0 <_B E_\infty^{\mathrm{tree}} \le_B E_\infty$, with proof.

## 2. Mathematical Foundations

**The space of finite-rank groups.** A torsion-free abelian group $A$ has rank $n$ iff $\dim_{\mathbb{Q}}(A \otimes \mathbb{Q}) = n$; every such $A$ embeds in $\mathbb{Q}^n$. Set
$$R(n) \;=\; \{\, A \le \mathbb{Q}^n \;:\; A \text{ contains a basis of } \mathbb{Q}^n \,\},$$
a Borel subset of the Polish space $2^{\mathbb{Q}^n}$ with the product topology. Every rank-$n$ group is isomorphic to some $A \in R(n)$, and for $A, B \in R(n)$,
$$A \cong B \iff \exists\, g \in \mathrm{GL}_n(\mathbb{Q}) \; \text{ with } \; g(A) = B .$$
Thus $\cong_n$ is the orbit equivalence relation $E^{R(n)}_{\mathrm{GL}_n(\mathbb{Q})}$ of a Borel action of a *countable* group, hence a **countable Borel equivalence relation** (every class is countable). By the Feldman–Moore theorem, every countable Borel equivalence relation arises this way.

**Borel reducibility.** For Borel equivalence relations $E$ on $X$ and $F$ on $Y$, $E \le_B F$ iff there is a Borel $f : X \to Y$ with $x \mathbin{E} x' \iff f(x) \mathbin{F} f(x')$. Write $E <_B F$ for $E \le_B F \not\le_B E$, and $E \sim_B F$ for bireducibility. Landmarks:
- $\Delta_{\mathbb{R}}$ (smooth), $E_0 = $ eventual equality on $2^{\mathbb{N}}$; by the Harrington–Kechris–Louveau dichotomy, $E_0 \le_B E$ for every non-smooth Borel $E$.
- $E_\infty$: the universal countable Borel equivalence relation, e.g. the shift action of $F_2$ on $2^{F_2}$.
- $E^{\mathrm{tree}}_\infty$: universal treeable; $E_0 <_B E^{\mathrm{tree}}_\infty <_B E_\infty$.

**Rank one (Baer).** For $A \le \mathbb{Q}$ with $1 \in A$ and prime $p$, the $p$-height is
$$h_p(A) = \sup\{\, k : \exists a \in A,\; p^k a = 1 \,\} \in \mathbb{N} \cup \{\infty\},$$
and the *characteristic* is $\chi(A) = (h_p(A))_{p}$. **Baer's theorem:** $A \cong B$ iff $\chi(A)$ and $\chi(B)$ agree at all but finitely many primes and differ by finite amounts elsewhere (same *type*). Hence
$$\cong_1 \;\sim_B\; E_0 .$$

**Superrigidity input.** Thomas's strictness proof uses Zimmer cocycle superrigidity for lattices $\Gamma \le G$ in higher-rank semisimple Lie groups, applied to $\mathrm{SL}_n(\mathbb{Z})$ acting on profinite completions such as $\prod_{p \in S} \mathrm{SL}_n(\mathbb{Z}_p)$, together with the Adams–Kechris machinery converting superrigidity into non-reducibility of orbit equivalence relations.

## 3. History & State of the Art (SOTA)

- **1937.** Baer classifies rank $1$ by types (Duke Math. J.).
- **1937–1970s.** Kurosh, Malcev, Derry give rank-$n$ "classifications" by $p$-adic matrix data modulo an intractable equivalence; Fuchs (*Infinite Abelian Groups* II, 1973) records the rank-$2$ problem as the standard test case for hopelessness.
- **1989.** Friedman–Stanley introduce Borel reducibility for classes of countable structures; isomorphism of *arbitrary* countable torsion-free abelian groups is later shown Borel complete (Downey–Montalbán, 2008 — it is $\Sigma^1_1$-complete, so finite rank is genuinely the tame end).
- **1996–2000.** Hjorth–Kechris develop the countable-model reducibility framework; Adams–Kechris (JAMS 2000) prove there are continuum-many pairwise $\le_B$-incomparable countable Borel equivalence relations, via algebraic groups and superrigidity.
- **1999–2001.** Hjorth proves $\cong_2$ is not hyperfinite, hence $\cong_1 <_B \cong_2$: the first proof that rank $2$ is strictly harder than rank $1$.
- **2003.** Thomas (*J. Amer. Math. Soc.* 16), the central result: $\cong_n <_B \cong_{n+1}$ for all $n \ge 1$. The finite-rank problems form a strictly increasing $\omega$-chain.
- **2006.** Hjorth–Thomas analyze $p$-local rank-two groups; Thomas surveys the program at the ICM (Madrid, 2006), stating the non-universality conjecture.
- **2012.** Coskey (*Trans. AMS* 364) proves the analogous strict hierarchy for quasi-isomorphism and near-isomorphism of finite-rank groups.
- **2011–.** Ioana's cocycle superrigidity for profinite actions of property (T) groups replaces/strengthens Zimmer input; Marks's work on universality methods sharpens what "universal" arguments can do.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $n = 1$ | Fully solved: $\cong_1 \sim_B E_0$, hyperfinite, non-smooth (Baer 1937; folklore DST) |
| $n = 2$ | Not hyperfinite (Hjorth); $\cong_1 <_B \cong_2$ |
| All $n \ge 1$ | $\cong_n <_B \cong_{n+1}$ (Thomas 2003) |
| All $n$ | $\cong_n \le_B E_\infty$ (it is countable Borel); $\cong_n$ is Borel, so *not* Borel complete |
| Arbitrary (infinite) rank | Isomorphism is Borel complete / $\Sigma^1_1$-complete — strictly beyond every $\cong_n$ |
| Divisible, completely decomposable, finite-rank free | Smooth: classified by rank plus a finite tuple of types |
| Rank-$n$ groups that are direct sums of rank-1 groups | $\cong$ reduces to $(E_0)^n$ modulo $S_n$: essentially hyperfinite |
| Quasi-isomorphism, near-isomorphism, rank $n$ | Strictly increasing hierarchy in $n$ (Coskey 2012) |
| $p$-local rank two | Analyzed by Hjorth–Thomas (2006): the $p$-local relations for distinct primes are non-trivially related and none is shown universal *(frontier — verify exact incomparability statement)* |
| Universality for any fixed $n$ | **Open** — no $n$ is known to satisfy $\cong_n \sim_B E_\infty$, and no $n \ge 2$ is known to satisfy $\cong_n <_B E_\infty$ |

## 5. Principal Obstacles

- **Superrigidity gives separations, not upper bounds.** The Zimmer/Adams–Kechris/Ioana toolkit proves statements of the form "$E \not\le_B F$" by comparing ergodic-theoretic invariants of measure-preserving actions. To prove $\cong_n <_B E_\infty$ one needs $E_\infty \not\le_B \cong_n$, i.e. an obstruction *inside* $\cong_n$. But $E_\infty$ has no invariant probability measure on any of its standard realizations that the machinery can exploit; measure-theoretic rigidity is the wrong instrument for capping complexity from above.
- **Measure-theoretic invariants are blind on null sets.** Every known separation argument runs on an ergodic invariant measure and concludes "no reduction on a conull set". Borel reducibility is a strictly finer, everywhere-defined notion; results proved measure-theoretically can fail to lift, and the gap between "$\mu$-reducibility" and "$\le_B$" is exactly where universality could hide.
- **Baire-category and Ramsey methods do not apply.** $\mathrm{GL}_n(\mathbb{Q})$ acting on $R(n)$ has generically ergodic behaviour that gives $E_0$-type lower bounds but no non-universality; Hjorth's turbulence theory addresses non-countable orbit equivalence relations and is vacuous here, since $\cong_n$ is countable.
- **No algebraic normal form.** Kurosh–Malcev invariants for rank $n \ge 2$ are $n$-tuples of $\mathbb{Z}_p$-lattices modulo a $\mathrm{GL}_n(\mathbb{Q})$-action — precisely the object whose complexity we are trying to measure. There is no independent combinatorial description to attack.
- **Universality proofs are one-directional.** Constructing $E_\infty \le_B \cong_n$ requires encoding an arbitrary $F_2$-shift into rank-$n$ groups; Marks's uniformity analysis shows the standard "Borel-coding" strategies cannot be made to work uniformly here, but does not rule out non-uniform reductions.

## 6. The Gap

Known: $E_0 \sim_B \cong_1 <_B \cong_2 <_B \cong_3 <_B \cdots \le_B E_\infty$. Unknown: whether any of the last inequalities is strict, or whether the chain is eventually constant at $E_\infty$. The exact missing step is a **Borel-definable obstruction to universality** for a countable Borel equivalence relation generated by a linear algebraic group action over $\mathbb{Q}$ — an "upper-bound invariant" that is preserved under $\le_B$, computable for $\cong_n$, and known to fail for $E_\infty$. Candidate invariants (cost, treeability, essential freeness, weak-containment-type data) are either not $\le_B$-monotone or not currently computable for $\cong_n$ when $n \ge 2$. Bridging $\bigvee_n \cong_n$ to $E_\infty$ additionally requires understanding the increasing union of the chain, which is not itself known to be Borel-bireducible with any standard relation.

## 7. Current Research (as of June 2026)

- **Rutgers (Thomas and collaborators)** continue the superrigidity program, extending strict-hierarchy results to $S$-local groups, Dedekind modules, and quasi-isomorphism variants.
- **Descriptive set theory / operator algebras interface**: Ioana-style cocycle superrigidity for profinite actions of property (T) groups is the current engine for separations; the search is for a version applicable to $\mathrm{GL}_2(\mathbb{Q})$, which lacks property (T). *(frontier — verify current status)*
- **Caltech/UCLA school (Marks, Tucker-Drob and collaborators)**: structural theory of countable Borel equivalence relations — treeability, cost, Borel combinatorics — aimed at producing exactly the upper-bound invariants Section 6 demands.
- **Effective/computability-theoretic approaches** (Montalbán, Downey, Melnikov school): analysing finite-rank groups via computable structure theory and Turing-invariant reductions, an approach that yields non-universality obstructions in adjacent settings. *(frontier — verify transfer to $\cong_n$)*
- No preprint claiming resolution of (Q1) for any $n \ge 2$ is known as of this review.

## 8. Future Work

- Prove or refute $\cong_2 \sim_B E_\infty$; rank $2$ is the smallest open case and the one where $\mathrm{SL}_2$ (virtually free, no property (T)) makes both directions plausible.
- Develop a $\le_B$-monotone invariant for countable Borel equivalence relations that separates $E_\infty$ from algebraic-group orbit relations — Thomas's stated priority.
- Decide treeability of $\cong_2$; a positive answer immediately gives $\cong_2 <_B E_\infty$, since $E^{\mathrm{tree}}_\infty <_B E_\infty$.
- Compute the cost of $\cong_n$ with respect to natural invariant measures on $R(n)$.
- Extend Coskey's quasi-isomorphism hierarchy to derive constraints on $\cong_n$ itself.
- Determine the position of $\cong_\infty^{fr} = \bigcup_n \cong_n$ (finite rank, unbounded) in $\le_B$.

## 9. Key References

- **[Foundational]** R. Baer. *Abelian groups without elements of finite order.* Duke Mathematical Journal 3 (1937), 68–122.
- **[Foundational]** L. Fuchs. *Infinite Abelian Groups, Volume II.* Academic Press, 1973.
- **[Foundational]** H. Friedman, L. Stanley. *A Borel reducibility theory for classes of countable structures.* Journal of Symbolic Logic 54 (1989), 894–914.
- **[Foundational]** A. S. Kechris. *Classical Descriptive Set Theory.* Graduate Texts in Mathematics 156, Springer, 1995.
- **[Foundational]** R. J. Zimmer. *Ergodic Theory and Semisimple Groups.* Birkhäuser, 1984.
- **[SOTA]** S. Adams, A. S. Kechris. *Linear algebraic groups and countable Borel equivalence relations.* Journal of the American Mathematical Society 13 (2000), 909–943.
- **[SOTA]** G. Hjorth. *Around nonclassifiability for countable torsion free abelian groups.* In: Abelian Groups and Modules (Dublin, 1998), Birkhäuser, 1999.
- **[SOTA]** S. Thomas. *The classification problem for torsion-free abelian groups of finite rank.* Journal of the American Mathematical Society 16 (2003), 233–258.
- **[SOTA]** G. Hjorth, S. Thomas. *The classification problem for p-local torsion-free abelian groups of rank two.* Journal of Mathematical Logic 6 (2006), 233–251.
- **[SOTA]** S. Coskey. *The classification of torsion-free abelian groups of finite rank up to isomorphism and up to quasi-isomorphism.* Transactions of the American Mathematical Society 364 (2012), 175–194.
- **[SOTA]** A. Ioana. *Cocycle superrigidity for profinite actions of property (T) groups.* Duke Mathematical Journal 157 (2011), 337–367.
- **[Survey]** S. Thomas. *Borel superrigidity and the classification problem for the torsion-free abelian groups of finite rank.* Proceedings of the International Congress of Mathematicians, Madrid 2006, Vol. II, EMS, 2006, 93–116.
- **[Survey]** G. Hjorth, A. S. Kechris. *Borel equivalence relations and classifications of countable models.* Annals of Pure and Applied Logic 82 (1996), 221–272.
- **[Survey]** S. Gao. *Invariant Descriptive Set Theory.* CRC Press, 2009.

## 10. Worked Example / Concrete Special Case

**Rank one computed explicitly, showing $\cong_1 \sim_B E_0$.**

Take $A \le \mathbb{Q}$ with $1 \in A$. Its characteristic $\chi(A) = (h_2, h_3, h_5, \dots)$ records for each prime $p$ the largest $k$ with $p^{-k} \in A$ (or $\infty$).

- $A = \mathbb{Z}$: $\chi = (0,0,0,\dots)$.
- $A = \mathbb{Z}[1/2]$: $\chi = (\infty, 0, 0, \dots)$.
- $A = \mathbb{Z}[1/3]$: $\chi = (0, \infty, 0, \dots)$.
- $A = \tfrac{1}{3}\mathbb{Z}[1/2] = \mathbb{Z}[1/2] \cdot \tfrac13$: as an abstract group this is $\cong \mathbb{Z}[1/2]$ (multiply by $3 \in \mathrm{GL}_1(\mathbb{Q}) = \mathbb{Q}^\times$), and normalising so $1$ lies in the group gives $\chi = (\infty,1,0,0,\dots)$ — differing from $\chi(\mathbb{Z}[1/2])$ in one finite coordinate.

The last bullet is exactly the content of Baer's equivalence: multiplying by $q = \prod p^{e_p} \in \mathbb{Q}^\times$ shifts finitely many coordinates by finite amounts. So
$$A \cong B \iff \chi(A) \mathbin{\sim} \chi(B), \quad (a_p) \sim (b_p) :\iff \sum_p |a_p - b_p| < \infty \text{ with } a_p = \infty \leftrightarrow b_p = \infty .$$

$\mathbb{Z}[1/2] \not\cong \mathbb{Z}[1/3]$: their characteristics differ at *infinitely* many coordinates? No — they differ at exactly two coordinates, but the difference at $p=2$ is $\infty$ vs $0$, which is not a finite shift. This is the invariant "the set $P_\infty(A) = \{p : h_p = \infty\}$ is an isomorphism invariant": $P_\infty(\mathbb{Z}[1/2]) = \{2\} \ne \{3\}$.

The map $A \mapsto \chi(A) \in (\mathbb{N}\cup\{\infty\})^{\mathbb{P}}$ is a Borel reduction of $\cong_1$ to the "finite difference" relation, which is Borel bireducible with $E_0$. Two consequences:
1. $\cong_1$ is **not smooth** (no real-number complete invariant): by HKL, $E_0 \le_B \cong_1$, so a Borel assignment $A \mapsto r_A \in \mathbb{R}$ with $A \cong B \iff r_A = r_B$ would contradict $E_0 \not\le_B \Delta_{\mathbb{R}}$. Concretely, one cannot Borel-choose a canonical representative from each type.
2. $\cong_1$ is hyperfinite — an increasing union of finite Borel equivalence relations $\chi \restriction$ first $k$ coordinates modulo bounded shift.

Now move to rank $2$. Take $A = \langle (1,0), (0,1), \tfrac{1}{p}(1, a_p) : p \in S \rangle \le \mathbb{Q}^2$ for a set $S$ of primes and residues $a_p \in \mathbb{Z}/p$. Isomorphism now asks for $g \in \mathrm{GL}_2(\mathbb{Q})$ carrying one lattice-data family to another: the residues $a_p$ transform by the Möbius action of $g$ modulo $p$. The invariant is thus a point of $\prod_{p \in S} \mathbb{P}^1(\mathbb{F}_p)$ modulo the diagonal $\mathrm{PGL}_2(\mathbb{Q})$-action — a genuine group action with no finite-difference normal form. Hjorth's theorem says this relation is not hyperfinite; Thomas's theorem says the analogous rank-$(n+1)$ relation is strictly harder still. Whether this family of $\mathrm{PGL}_n(\mathbb{Q})$-actions on adelic projective spaces can encode the full $F_2$-shift $E_\infty$ is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*