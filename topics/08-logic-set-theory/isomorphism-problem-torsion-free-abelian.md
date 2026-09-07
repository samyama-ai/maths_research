---
id: 08-logic-set-theory/isomorphism-problem-torsion-free-abelian
title: "Isomorphism Problem for Torsion-Free Abelian Groups"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Isomorphism Problem for Torsion-Free Abelian Groups

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/isomorphism-problem-torsion-free-abelian` · **Status:** open

## 1. Problem Statement / Conjecture

Classify the torsion-free abelian groups of finite rank $n$ up to isomorphism, and determine the exact position of each isomorphism relation $\cong_n$ in the Borel-reducibility hierarchy of countable Borel equivalence relations.

Concretely, let $\cong_n$ denote isomorphism on the standard Borel space $S(\mathbb{Q}^n)$ of full-rank subgroups of $\mathbb{Q}^n$. The following are open:

- **(A) Universality.** Is $\cong_n$ a *universal* countable Borel equivalence relation for some (equivalently, all sufficiently large) $n \ge 3$? Thomas conjectures **no** — that $\cong_n <_B E_\infty$ for every $n$, so the $\cong_n$ form a strictly increasing tower that never reaches the top.
- **(B) Explicit invariants.** Is there, for $n = 2$, a complete system of isomorphism invariants of a concretely describable kind (e.g. computable from the Kurosh–Malcev $p$-adic data by a Borel function into a Polish space acted on by a countable group in a manageable way)?
- **(C) The rank hierarchy at the bottom.** $\cong_1$ is hyperfinite and $\cong_2$ is not; is $\cong_2$ *treeable*? Is $\cong_n$ treeable for any $n \ge 2$?

A complete solution to (A) means either a Borel reduction $E_\infty \le_B \cong_n$ for some $n$, or a proof (in ZFC) that no such reduction exists for any $n$. A solution to (B) means a Borel classification by invariants strictly simpler than the groups themselves, or a proof that none exists at the stated level.

Note what is **not** open: the infinite-rank case. Paolini and Shelah proved that isomorphism of countable torsion-free abelian groups is Borel complete — maximally complex among isomorphism relations on countable structures.

## 2. Mathematical Foundations

**Groups.** An abelian group $A$ is *torsion-free* if $na = 0$ with $n \ne 0$ implies $a = 0$. Its *rank* is $\operatorname{rk}(A) = \dim_{\mathbb{Q}}(A \otimes_{\mathbb{Z}} \mathbb{Q})$. A torsion-free group of rank $n$ embeds in $\mathbb{Q}^n$, and we may assume it is a *full* subgroup: $A \le \mathbb{Q}^n$ with $\mathbb{Q}A = \mathbb{Q}^n$.

**The Borel space.** Let
$$S(\mathbb{Q}^n) = \{\, A \in 2^{\mathbb{Q}^n} : A \text{ is a full subgroup of } \mathbb{Q}^n \,\},$$
a Borel subset of the Cantor space $2^{\mathbb{Q}^n}$, hence a standard Borel space. Two full subgroups satisfy $A \cong B$ iff some $g \in \mathrm{GL}_n(\mathbb{Q})$ carries $A$ onto $B$. So
$$\cong_n \;=\; E^{\mathrm{GL}_n(\mathbb{Q})}_{S(\mathbb{Q}^n)},$$
the orbit equivalence relation of a *countable* group acting by Borel automorphisms — a **countable Borel equivalence relation** (CBER): every class is countable.

**Borel reducibility.** For equivalence relations $E$ on $X$ and $F$ on $Y$, $E \le_B F$ iff there is Borel $f : X \to Y$ with $x \mathbin{E} x' \iff f(x) \mathbin{F} f(x')$. Write $E <_B F$ for $E \le_B F \not\le_B E$. Benchmarks:
$$\Delta_{\mathbb{R}} \;<_B\; E_0 \;<_B\; \cdots \;<_B\; E_\infty,$$
where $E_0$ is eventual agreement on $2^{\mathbb{N}}$, and $E_\infty$ is the universal CBER (realized by the shift action of $F_2$ on $2^{F_2}$). $E$ is *smooth* if $E \le_B \Delta_{\mathbb{R}}$; *hyperfinite* if $E = \bigcup_n F_n$ with $F_n$ finite Borel and increasing (equivalently $E \le_B E_0$, by Dougherty–Jackson–Kechris); *treeable* if some Borel treeing exists on its classes.

**Rank 1 (Baer).** For $0 \neq a \in A \le \mathbb{Q}$ the *characteristic* is $\chi(a) = (h_p(a))_{p \text{ prime}} \in (\mathbb{N} \cup \{\infty\})^{\mathcal{P}}$, where $h_p(a) = \sup\{k : a \in p^k A\}$. The *type* $\tau(A)$ is $\chi(a)$ modulo the relation "differ in finitely many coordinates, all differences finite". Then
$$A \cong B \iff \tau(A) = \tau(B),$$
so $\cong_1$ is Borel bireducible with $E_0$ restricted to $(\mathbb{N}\cup\{\infty\})^{\mathcal{P}}$: non-smooth but hyperfinite.

**Rank $n$ (Kurosh–Malcev).** A full $A \le \mathbb{Q}^n$ is determined by its $p$-adic localizations $A_p = \mathbb{Z}_p \otimes A \le \mathbb{Q}_p^n$, each a full $\mathbb{Z}_p$-submodule. This gives the invariant
$$A \;\longmapsto\; (A_p)_{p} \in \prod_p \{\text{full } \mathbb{Z}_p\text{-submodules of } \mathbb{Q}_p^n\},$$
complete only up to the equivalence: $(A_p) \sim (B_p)$ iff there is $g \in \mathrm{GL}_n(\mathbb{Q})$ and $g_p \in \mathrm{GL}_n(\mathbb{Z}_p)$ with $B_p = g_p g A_p$ for all $p$, and $g_p = 1$ for almost all $p$. The invariant is thus not a solution but a restatement — the classifying data carries an unresolved group action.

**Superrigidity input.** Thomas's method exploits: (i) Zimmer cocycle superrigidity for higher-rank lattices, applied to $\mathrm{SL}_n(\mathbb{Z}) \curvearrowright$ (products of) $p$-adic Grassmannians; (ii) Popa cocycle superrigidity for Bernoulli actions of groups with property (T). These force any Borel reduction between such actions to be, off a null set, induced by a group isomorphism — a rigidity statement with no counterpart in classical algebra.

## 3. History & State of the Art (SOTA)

- **1937.** Baer classifies rank-1 groups by type; Kurosh gives $p$-adic invariants for finite rank, refined by Malcev (1938). Both note the invariants do not settle isomorphism.
- **1937–1970s.** Fuchs's *Infinite Abelian Groups* records the finite-rank problem as intractable; Fuchs writes (vol. II, 1973) that a satisfactory classification even for rank 2 seems hopeless. Explicit pathologies: Jónsson's non-unique direct decompositions, Corner's 1961 theorem realizing arbitrary countable reduced torsion-free rings as endomorphism rings.
- **1989–1996.** Friedman–Stanley introduce Borel completeness; Harrington–Kechris–Louveau prove the $E_0$ dichotomy; Dougherty–Jackson–Kechris develop hyperfiniteness — the toolkit that makes "hopeless" a theorem rather than a mood.
- **1998–2001.** Hjorth proves $\cong_2$ is not hyperfinite, so $\cong_1 <_B \cong_2$: rank genuinely matters for descriptive complexity.
- **2003.** Thomas, *The classification problem for torsion-free abelian groups of finite rank* (JAMS): the tower is strictly increasing,
$$\cong_1 \;<_B\; \cong_2 \;<_B\; \cong_3 \;<_B\; \cdots,$$
via Zimmer superrigidity. This is the central structural theorem.
- **2008.** Downey–Montalbán: isomorphism of computable torsion-free abelian groups (infinite rank) is $\Sigma^1_1$-complete — the recursion-theoretic analogue of maximal complexity.
- **2021–2025.** Paolini–Shelah: torsion-free abelian groups are **Borel complete**; isomorphism on countable torsion-free abelian groups is maximally complex among isomorphism relations of countable structures. This closes the infinite-rank problem and sharply isolates the finite-rank questions as the remaining open ground.

## 4. Partial Results / Verified Cases

- **Rank $n = 1$:** completely solved (Baer 1937). $\cong_1 \sim_B E_0$: hyperfinite, non-smooth. Continuum many types; no Borel assignment of real-number invariants exists.
- **Rank $n = 2$:** not hyperfinite (Hjorth). So no classification by countable increasing unions of finite pieces, hence no "$E_0$-style" invariants.
- **All finite $n$:** $\cong_n <_B \cong_{n+1}$ (Thomas 2003). Also $\cong_n \le_B E_\infty$ for all $n$, since each $\cong_n$ is a countable Borel equivalence relation.
- **Infinite / countable rank:** Borel complete (Paolini–Shelah). Equivalently $\cong_{\mathrm{TFA}} \sim_B \cong_{\text{graphs}} \sim_B \cong_{\text{groups}}$.
- **Restricted classes with positive classification.** *Completely decomposable* groups $A = \bigoplus_{i\le n} A_i$ with $\operatorname{rk} A_i = 1$: classified by the multiset of types (Baer) — smooth relative to $E_0^{n}$. *Homogeneous* rank-$n$ groups of a fixed type: reduce to type data. *Quasi-isomorphism* on rank-$n$ groups (i.e. $A, B$ with $mB \le A \le \frac 1m B$) is strictly simpler than $\cong_n$ and Thomas showed the quasi-isomorphism analogues also form a strict hierarchy.
- **$S$-local groups.** For a finite set $S$ of primes, Thomas analysed $\cong_n^S$ (groups with $A_p = \mathbb{Q}_p^n$ off $S$) and showed the complexity grows with $|S|$ as well as with $n$ — giving a two-parameter family of strictly increasing CBERs.
- **Computational.** Full subgroups of $\mathbb{Q}^2$ containing $\mathbb{Z}^2$ with index $\le N$ can be enumerated and isomorphism-tested by $\mathrm{GL}_2(\mathbb{Z})$-orbit computation on $\mathbb{Z}^2/N\mathbb{Z}^2$; this is a finite linear-algebra problem for each $N$ and settles all finite-index instances, but says nothing about the limit behaviour that $\le_B$ measures.

## 5. Principal Obstacles

- **Lower bounds require rigidity, and rigidity has a ceiling.** All strictness results (Hjorth, Thomas) come from Zimmer/Popa superrigidity for higher-rank lattices and property (T) groups. These theorems say a cocycle is *trivial up to a homomorphism*; they yield non-reducibility between specific actions. They do not give tools to *build* a reduction from $E_\infty$, because $F_2$ (the source of $E_\infty$) is treeable and amenable-free-like — precisely the opposite regime from where the superrigidity machinery is productive.
- **No known invariant for "non-universal".** Proving $\cong_n <_B E_\infty$ requires an invariant of CBERs preserved under $\le_B$ that separates $\cong_n$ from $E_\infty$. The known ones — hyperfiniteness, treeability, cost, $\ell^2$-Betti numbers, ergodic-dimension bounds — are either already known to fail to separate, or are not known to be $\le_B$-monotone in the needed direction. Cost, in particular, is not a Borel-reducibility invariant for non-measure-preserving reductions.
- **The Kurosh–Malcev data are not a simplification.** The local invariants $(A_p)_p$ replace a group by a point of a Grassmannian product, but the classifying equivalence is the orbit relation of $\mathrm{GL}_n(\mathbb{Q})$ on $\prod_p \mathrm{GL}_n(\mathbb{Q}_p)/\mathrm{GL}_n(\mathbb{Z}_p)$ — a diagonal action of a lattice-like group on a homogeneous space, exactly as hard as the original.
- **Model-theoretic methods stall.** Torsion-free abelian groups of rank $n$ are not finitely axiomatizable as a class with a well-behaved theory; Ehrenfeucht–Fraïssé and back-and-forth arguments produce the Borel-completeness result in infinite rank but collapse at finite rank, where each group is "small" yet the moduli are wild.
- **Endomorphism-ring pathology.** Corner's realization theorem means the class contains groups with essentially arbitrary countable reduced rings as $\operatorname{End}$; any invariant hoping to be algebraically natural must survive that, which rules out ring-theoretic normal forms.

## 6. The Gap

Proven: $\cong_1 \sim_B E_0$ and $\cong_1 <_B \cong_2 <_B \cong_3 <_B \cdots \le_B E_\infty$, plus Borel completeness at infinite rank.

Wanted: the value of $\sup_n \cong_n$ relative to $E_\infty$, and a positive structure theorem at rank 2.

The precise barrier is a single implication in either direction:

- **Upward:** exhibit a Borel $f : 2^{F_2} \to S(\mathbb{Q}^n)$ reducing the shift $E(F_2, 2^{F_2})$ to $\cong_n$. No construction is known that encodes free-group orbit data into $p$-adic lattice data while remaining $\mathrm{GL}_n(\mathbb{Q})$-equivariant; the obstruction is that $\mathrm{GL}_n(\mathbb{Q})$-orbits on the local data have a *linear* structure with no room for the tree-like branching of $F_2$.
- **Downward:** produce a $\le_B$-monotone invariant $I$ with $I(\cong_n)$ bounded and $I(E_\infty)$ not. Every candidate to date is either not monotone (cost) or already equal on both sides.

This is a single missing invariant, not a chain of steps — which is why the question has stood essentially unchanged since 2003.

## 7. Current Research (as of June 2026)

- **Rigidity-driven lower bounds.** Continued exploitation of Popa-type superrigidity and Ioana's cocycle theorems to separate CBERs (Thomas; Ioana; Adams–Kechris lineage). Applied to $\cong_n$ these keep producing strictness but not non-universality.
- **The Paolini–Shelah program.** After Borel completeness for torsion-free abelian groups, Paolini and Shelah and coauthors have pushed Borel completeness to further algebraic classes (e.g. abelian $p$-groups of bounded Ulm data, torsion-free modules over specific rings). Whether their coding technique can be localized to bounded rank is under active study *(frontier — verify)*.
- **Anti-classification via Baire category and generic ergodicity** rather than measure — an approach that avoids the measure-preserving restrictions that block cost arguments *(frontier — verify)*.
- **Groups/institutions.** Rutgers (Thomas's school and successors), Caltech/UCLA descriptive set theory (Kechris and students, Marks, Tucker-Drob), Jerusalem (Shelah), Torino/Vienna (Paolini, Motto Ros), UIC and Notre Dame (computable structure theory: Montalbán, Downey's collaborators).
- **Computable-structure angle.** Refinement of the Downey–Montalbán $\Sigma^1_1$-completeness to bounded-rank and effective-Borel settings; degree-spectra of rank-$n$ groups.

## 8. Future Work

1. **Find a new $\le_B$-monotone invariant of CBERs.** The most-named target: an invariant sensitive to "how much of $E_\infty$" a relation contains, defined without a preserved measure. Suggested sources — measured-equivalence-relation $\ell^2$-invariants transported to the Borel category, or Marks-style determinacy arguments on the space of colorings.
2. **Settle treeability of $\cong_2$.** A negative answer would already separate $\cong_2$ from the treeable universal relation $E_{\infty T}$; a positive answer would be the first structural upper bound above hyperfinite.
3. **Two-parameter $S$-local analysis.** Map the full lattice $\{\cong_n^S\}$ to see whether the supremum over $n$ and $S$ hits $E_\infty$.
4. **Localize the Paolini–Shelah coding.** Determine the smallest rank (finite or not) at which their construction can be run; any finite-rank version would immediately answer (A) affirmatively.
5. **Algebraic side:** classify rank-2 groups with prescribed $\operatorname{End}$, testing whether Corner-realizable rings can be used to encode $F_2$-orbits.

## 9. Key References

- **[Foundational]** Reinhold Baer. *Abelian groups without elements of finite order.* Duke Mathematical Journal, 3 (1937), 68–122.
- **[Foundational]** A. G. Kurosh. *Primitive torsionsfreie abelsche Gruppen vom endlichen Range.* Annals of Mathematics, 38 (1937), 175–203.
- **[Foundational]** A. I. Malcev. *Torsion-free abelian groups of finite rank* (Russian). Matematicheskii Sbornik, 4 (1938), 45–68.
- **[Foundational]** László Fuchs. *Infinite Abelian Groups*, Vols. I–II. Academic Press, 1970/1973. (See also Fuchs, *Abelian Groups*, Springer Monographs in Mathematics, 2015.)
- **[Foundational]** A. L. S. Corner. *Every countable reduced torsion-free ring is an endomorphism ring.* Proceedings of the London Mathematical Society, 13 (1963), 687–710.
- **[Foundational]** R. Dougherty, S. Jackson, A. S. Kechris. *The structure of hyperfinite Borel equivalence relations.* Transactions of the AMS, 341 (1994), 193–225.
- **[Foundational]** H. Friedman, L. Stanley. *A Borel reducibility theory for classes of countable structures.* Journal of Symbolic Logic, 54 (1989), 894–914.
- **[SOTA]** Simon Thomas. *The classification problem for torsion-free abelian groups of finite rank.* Journal of the American Mathematical Society, 16 (2003), 233–258.
- **[SOTA]** Greg Hjorth. *Around nonclassifiability for countable torsion free abelian groups.* In *Abelian Groups and Modules* (Dublin, 1998), Trends in Mathematics, Birkhäuser, 1999, 269–292.
- **[SOTA]** Simon Thomas. *The classification problem for $S$-local torsion-free abelian groups of finite rank.* Advances in Mathematics, 226 (2011), 3699–3723.
- **[SOTA / Recent]** Gianluca Paolini, Saharon Shelah. *Torsion-free abelian groups are Borel complete.* arXiv:2102.12371; Annals of Mathematics, 2025.
- **[SOTA]** Rodney G. Downey, Antonio Montalbán. *The isomorphism problem for torsion-free abelian groups is analytic complete.* Journal of Algebra, 320 (2008), 2291–2300.
- **[Survey]** Simon Thomas. *Superrigidity and countable Borel equivalence relations.* Annals of Pure and Applied Logic, 120 (2003), 237–262.
- **[Survey]** Su Gao. *Invariant Descriptive Set Theory.* CRC Press, Pure and Applied Mathematics 293, 2009.
- **[Survey]** A. S. Kechris. *The theory of countable Borel equivalence relations.* Cambridge Tracts in Mathematics, Cambridge University Press, 2024.

## 10. Worked Example / Concrete Special Case

**Rank 1, computed.** Take $A = \mathbb{Z}[1/2] \le \mathbb{Q}$ and $B = \mathbb{Z}[1/3]$. Compute characteristics at the generator $1$:
$$\chi_A(1) = (\infty, 0, 0, 0, \ldots) \quad (\text{at } p = 2,3,5,7,\ldots), \qquad \chi_B(1) = (0, \infty, 0, 0, \ldots).$$
These differ in a coordinate where one is $\infty$ and the other finite, so they are not equivalent modulo finite differences: $\tau(A) \ne \tau(B)$, hence $A \not\cong B$. By contrast $C = \frac{1}{5}\mathbb{Z}[1/2]$ has $\chi_C(1/5) = \chi_A(1)$, so $\tau(C) = \tau(A)$ and $C \cong A$ — indeed $x \mapsto x/5$ is an isomorphism.

Now note $A' = \mathbb{Z}[1/2, 1/3, 1/5, \ldots]$-style groups: for any $S \subseteq \mathcal{P}$ set $A_S = \mathbb{Z}[1/p : p \in S]$. Then $A_S \cong A_T$ iff $S \mathbin{\triangle} T$ is finite. The map $S \mapsto A_S$ is a Borel reduction of $E_0$ on $2^{\mathcal{P}}$ into $\cong_1$, so $\cong_1$ is not smooth: **no assignment of real-number invariants classifies even rank-1 groups.** Conversely Baer's theorem gives $\cong_1 \le_B E_0$, so $\cong_1 \sim_B E_0$ — exactly hyperfinite.

**Rank 2, where it breaks.** Fix the prime $p$ and consider full subgroups $A \le \mathbb{Q}^2$ that are $\mathbb{Z}[1/q]$-modules for all $q \ne p$ and have $A_p$ a full $\mathbb{Z}_p$-submodule of $\mathbb{Q}_p^2$. Up to scaling, $A_p$ is determined by a point of the projective line $\mathbb{P}^1(\mathbb{Q}_p)$ together with a "depth", and the Kurosh–Malcev criterion becomes:
$$A \cong B \iff \exists\, g \in \mathrm{GL}_2(\mathbb{Q}) \text{ with } g \cdot [A_p] = [B_p] \text{ in } \mathbb{P}^1(\mathbb{Q}_p).$$
So isomorphism of these rank-2 groups **is** the orbit equivalence relation of $\mathrm{PGL}_2(\mathbb{Q}) \curvearrowright \mathbb{P}^1(\mathbb{Q}_p)$. Concretely: the lines spanned by $(1,\alpha)$ and $(1,\beta)$ for $\alpha,\beta \in \mathbb{Q}_p \setminus \mathbb{Q}$ give isomorphic groups iff
$$\beta = \frac{a\alpha + b}{c\alpha + d} \quad \text{for some } \begin{pmatrix} a & b \\ c & d\end{pmatrix} \in \mathrm{GL}_2(\mathbb{Q}).$$
This is a Möbius-orbit problem on $\mathbb{Q}_p$: each orbit is countable and dense, the action is ergodic with respect to Haar measure on $\mathbb{P}^1(\mathbb{Q}_p)$, and by Hjorth's argument the resulting relation is not hyperfinite. The whole open problem is visible here: one can *state* the invariant ($\alpha$ modulo $\mathrm{GL}_2(\mathbb{Q})$-Möbius action) in one line, and yet no one knows whether this relation is as complex as the free-group shift.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*