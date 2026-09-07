---
id: 08-logic-set-theory/homotopy-type-theory-coherence-problem
title: "Homotopy Type Theory Coherence Problem"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Homotopy Type Theory Coherence Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/homotopy-type-theory-coherence-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Homotopy type theory (HoTT) is a dependent type theory whose types are read as homotopy types (∞-groupoids). The **coherence problem** is the mismatch between the *strict* equations demanded by type-theoretic syntax and the *weak* (up-to-homotopy) structure supplied by homotopical semantics. It has two faces, both open in general:

- **Semantic coherence (strictification).** Given a homotopy-theoretic structure $\mathcal{M}$ (a model category, an $(\infty,1)$-category, an $\infty$-topos), produce a model of Martin-Löf type theory with $\Sigma$, $\Pi$, identity types and univalent universes in which substitution acts *strictly functorially*, i.e. $A[\sigma][\tau] = A[\sigma\tau]$ on the nose and $\Pi(A,B)[\sigma] = \Pi(A[\sigma], B[\sigma^+])$ on the nose — not merely up to canonical isomorphism. Conjecturally every elementary $\infty$-topos, and every locally cartesian closed $(\infty,1)$-category with enough universes, admits such a strictification, and the interpretation is *invariant*: the resulting model is determined up to equivalence by $\mathcal{M}$.
- **Syntactic coherence (internal infinite structures).** Inside book HoTT, define by a single internal construction the infinite towers of coherence data that homotopy theory needs: semi-simplicial types $X:\mathbb{N}\to\mathcal{U}$ with all face maps and all compatibility conditions, $(\infty,1)$-categories, $\infty$-groupoid objects, the type of $\mathcal{U}$-small $\infty$-structures. No such definition is known, and it is open whether one exists in HoTT without extra axioms.

A complete resolution means either (a) a uniform strictification theorem plus an internal definition of semi-simplicial types, or (b) a proof that the internal definition is impossible (e.g. a model of HoTT in which the type of semi-simplicial types provably does not exist).

## 2. Mathematical Foundations

**Contextual categories.** A model of dependent type theory is a *contextual category* (Cartmell) / *category with families* (Dybjer): a category $\mathcal{C}$ of contexts with a terminal object, a presheaf
$$\mathrm{Ty}:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set},\qquad \mathrm{Tm}:\left(\textstyle\int\mathrm{Ty}\right)^{\mathrm{op}}\to\mathbf{Set},$$
together with context extension $\Gamma.A$ and projections $p_A:\Gamma.A\to\Gamma$ satisfying, for $\sigma:\Delta\to\Gamma$,
$$A[\mathrm{id}]=A,\qquad A[\sigma][\tau]=A[\sigma\tau],\qquad a[\mathrm{id}]=a,\qquad a[\sigma][\tau]=a[\sigma\tau].$$
Functoriality here is **equality of sets**, not isomorphism. Semantics natively gives instead a **Grothendieck fibration** (pullback of a fibration along a map is defined only up to canonical iso via a universal property), so the strict equations fail.

**The coherence gap.** In a locally cartesian closed category $\mathcal{C}$, pullback $\sigma^*:\mathcal{C}/\Gamma\to\mathcal{C}/\Delta$ is a pseudofunctor: there are invertible comparisons
$$c_{\sigma,\tau}: \tau^*\sigma^* \xrightarrow{\ \cong\ } (\sigma\tau)^*,$$
satisfying Bénabou cocycle conditions but not identities. Strictification means replacing this pseudofunctor $\mathcal{C}^{\mathrm{op}}\to\mathbf{Cat}$ by an equivalent strict functor; the classical tool is the Bénabou/Giraud strictification, which for *fibrations of sets* is Bénabou's "right adjoint splitting" (Hofmann 1995) and for models with universes is Lumsdaine–Warren's **local universes**: one replaces types over $\Gamma$ by triples $(V,E\twoheadrightarrow V,\ \chi:\Gamma\to V)$, where substitution acts by composing $\chi$ — strictly associative because composition in $\mathcal{C}$ is.

**Identity types and weak factorization.** In Awodey–Warren semantics, $\mathrm{Id}_A$ is interpreted by a path object: a factorization
$$A \xrightarrow{\ r\ } PA \xrightarrow{\ (s,t)\ } A\times A$$
with $r$ an acyclic cofibration and $(s,t)$ a fibration. The induced structure on each type is a *weak* $\omega$-groupoid: associativity $p\cdot(q\cdot r)=(p\cdot q)\cdot r$ holds only as an inhabitant of an identity type, and its coherences form an infinite tower (Lumsdaine; van den Berg–Garner).

**Univalence.** For a universe $\mathcal{U}$ with $\mathrm{El}$, univalence asserts that
$$\mathrm{idtoeqv}:(A=_{\mathcal U}B)\longrightarrow (A\simeq B)$$
is an equivalence. Semantically the universe must be a fibration $\widetilde{\mathcal U}\to\mathcal U$ classifying (a class of) fibrations *strictly* — and strictness of the classification is exactly where coherence bites.

**Initiality.** The syntax should form the initial such structure: for the term model $\mathcal{T}$ and any model $\mathcal{M}$, there is a unique structure-preserving morphism $\mathcal{T}\to\mathcal{M}$. Without initiality, "the interpretation" of syntax in a model is not well defined.

## 3. History & State of the Art (SOTA)

- **1993–1995.** Curien ("Substitution up to isomorphism") and Hofmann ("On the interpretation of type theory in locally cartesian closed categories") isolate the strictness mismatch and give the first splitting for LCCCs; Hofmann's argument uses a right-adjoint splitting and requires care with $\Pi$-types.
- **1998.** Hofmann–Streicher's groupoid model refutes uniqueness of identity proofs (UIP) and gives the first genuinely homotopical model, with a universe of small groupoids.
- **2006–2009.** Awodey–Warren interpret identity types in weak factorization systems; Voevodsky formulates univalence and builds the simplicial set model.
- **2012–2015.** Lumsdaine–Warren's *local universes* method makes strictification systematic; Voevodsky introduces C-systems and states the **initiality conjecture** as a genuine open problem.
- **2018–2021.** Cubical type theory (Cohen–Coquand–Huber–Mörtberg) sidesteps part of the problem by giving *computational* univalence with strict substitution in a presheaf topos on the cube category. Kapulkin–Lumsdaine publish the simplicial model in JEMS (2021). Shulman proves every $\infty$-topos has strict univalent universes (2019).
- **2020–2023.** de Boer, Brunerie, Lumsdaine, Mörtberg formalize initiality for a substantial MLTT; Bocquet, Kaposi and Sattler develop general "coherence for strict equalities" and second-order/internal-language techniques.

## 4. Partial Results / Verified Cases

- **Groupoid model (homotopy 1-types).** Hofmann–Streicher (1998): full strict model of MLTT with a univalent universe of 1-truncated types. Coherence is finite here — only associativity and unit at level 1.
- **Truncated levels $n \le 2$.** Semi-simplicial types are definable in HoTT for each *fixed external* $n$: $X_0:\mathcal U$, $X_1:X_0\to X_0\to\mathcal U$, etc. The obstruction is uniformity in $n$, not any particular $n$.
- **Simplicial sets.** Kapulkin–Lumsdaine (2021): $\mathbf{sSet}$ with Kan fibrations models MLTT with $\Sigma,\Pi,\mathrm{Id}$ and univalent universes $\mathcal U_\kappa$ for inaccessible $\kappa$ — classically, using the axiom of choice.
- **All $\infty$-toposes.** Shulman (2019): every Grothendieck $\infty$-topos admits a type-theoretic model category presentation with strict univalent universes closed under $\Sigma,\Pi,\mathrm{Id}$, and higher inductive types; this settles the *existence* half of semantic coherence for Grothendieck (not elementary) $\infty$-toposes.
- **Inverse diagrams.** Shulman (2015): univalence and homotopy canonicity for inverse-diagram models over inverse categories of finite height — a controlled, finite-coherence case.
- **Cubical.** Cartesian and De Morgan cubical type theories have canonicity (Huber 2019) and homotopy canonicity results (Coquand–Huber–Sattler 2019), with strict substitution by construction.
- **Initiality.** Proved and machine-checked for MLTT with $\Pi$, $\Sigma$, $\mathrm{Id}$, universes by de Boer (2020) and the Initiality Project.
- **Two-level type theory.** Annenkov–Capriotti–Kraus–Sattler (2023): adding a strict equality layer makes semi-simplicial types definable — a solution *outside* plain HoTT.

## 5. Principal Obstacles

- **Infinite towers are not internally indexable.** Defining $X:\mathbb{N}\to\mathcal{U}$ by recursion requires, at step $n+1$, a type whose formulation mentions all coherences at stages $\le n$; the recursion is not structurally decreasing in any known HoTT-definable well-founded order, and its "type" changes at every step. Higher inductive types do not help because they add points and paths, not indexed coherence schemas.
- **No internal strict equality.** Every candidate construction needs to say "these two composites are *the same* type", but in HoTT sameness is $\mathrm{Id}$, which itself carries structure — the fix reproduces the problem one level up. This is the core reason two-level type theory works and plain HoTT does not.
- **Strictification vs. invariance.** Local universes and Shulman's construction pick *choices* (representing fibrations, cofibrant replacements, well-ordering data). Nothing currently proves the resulting contextual category is independent of these choices up to the right notion of equivalence of models; Kapulkin–Lumsdaine's homotopy theory of type theories gives a framework but not the general invariance theorem.
- **Elementary $\infty$-toposes.** Shulman's proof uses presentability: a combinatorial model category and Grothendieck-universe-sized inaccessibles. Elementary $\infty$-toposes need not be presentable, so there is no model category to strictify.
- **Choice and constructivity.** The simplicial model is not constructive; cubical models are constructive but it is open whether they are *equivalent* to spaces as a model of HoTT in a constructive metatheory.

## 6. The Gap

Precisely: we can strictify (i) presentable homotopy theories, using classical set theory, and (ii) each finite level of coherence, one at a time. What is missing is

1. a **uniform internal** construction — a single HoTT term of type $\sum_{X:\mathbb{N}\to\mathcal U}\ \mathrm{FaceData}(X)$ that produces semi-simplicial types for all $n$ simultaneously (or a model-theoretic proof that no such term exists);
2. a strictification for **non-presentable** settings, chiefly elementary $\infty$-toposes, where no model category is available;
3. an **invariance theorem**: the assignment $\mathcal{M}\mapsto$ (strict model) is functorial and equivalence-invariant, so that "HoTT is the internal language of $\infty$-toposes" becomes a theorem rather than a program.

## 7. Current Research (as of June 2026)

- **Internal-language conjectures.** Work extending Kapulkin–Lumsdaine's homotopy theory of type theories toward a full equivalence between a homotopy theory of type theories and one of locally cartesian closed $(\infty,1)$-categories. Groups: Western Ontario (Kapulkin), Stockholm/Nottingham (Lumsdaine, Kraus), Aarhus (Gratzer, Birkedal). *(frontier — verify)*
- **Synthetic Tait computability and internal-language methods** (Sterling, Angiuli, Gratzer): normalization and canonicity proofs presented as constructions in a glued topos, reducing coherence bookkeeping to sheaf-theoretic arguments.
- **Higher observational type theory** (Altenkirch, Kaposi, Shulman and collaborators): identity types defined by recursion on type structure, aiming at strict computation rules that dissolve some coherence obligations. *(frontier — verify)*
- **Bocquet–Kaposi–Sattler**-style coherence theorems: replacing strict equalities in a type theory by equivalences, giving general "internal sameness is enough" statements.
- **Elementary $\infty$-topos program** (Rasekh, Shulman): axiomatics of elementary $\infty$-toposes and the search for object classifiers that strictify.

## 8. Future Work

- Prove or refute definability of semi-simplicial types in book HoTT — a negative result would need a model of HoTT with a definable failure, likely via a parametricity or realizability model.
- Extend Shulman's strictification to elementary $\infty$-toposes, possibly by replacing model categories with fibration categories or with internal-language arguments in a Grothendieck construction.
- Establish invariance of the local-universe strictification under Dwyer–Kan equivalence of the underlying homotopy theory.
- Settle whether cubical type theories are conservative over book HoTT, and whether their strictness can be transported back.
- Develop displayed/two-level fragments where the strict layer is provably conservative, giving HoTT-safe access to infinite coherence.

## 9. Key References

- **[Foundational]** Martin Hofmann, Thomas Streicher. *The groupoid interpretation of type theory.* In *Twenty-Five Years of Constructive Type Theory*, Oxford University Press, 1998.
- **[Foundational]** Martin Hofmann. *On the interpretation of type theory in locally cartesian closed categories.* CSL 1994, LNCS 933, Springer, 1995.
- **[Foundational]** John Cartmell. *Generalised algebraic theories and contextual categories.* Annals of Pure and Applied Logic 32, 1986.
- **[Foundational]** The Univalent Foundations Program. *Homotopy Type Theory: Univalent Foundations of Mathematics.* Institute for Advanced Study, 2013.
- **[SOTA]** Peter LeFanu Lumsdaine, Michael A. Warren. *The local universes model: an overlooked coherence construction for dependent type theories.* ACM Transactions on Computational Logic 16(3), 2015.
- **[SOTA]** Chris Kapulkin, Peter LeFanu Lumsdaine. *The simplicial model of univalent foundations (after Voevodsky).* Journal of the European Mathematical Society 23(6), 2021.
- **[SOTA]** Michael Shulman. *All $(\infty,1)$-toposes have strict univalent universes.* arXiv:1904.07004, 2019.
- **[SOTA]** Michael Shulman. *Univalence for inverse diagrams and homotopy canonicity.* Mathematical Structures in Computer Science 25(5), 2015.
- **[SOTA]** Cyril Cohen, Thierry Coquand, Simon Huber, Anders Mörtberg. *Cubical Type Theory: a constructive interpretation of the univalence axiom.* TYPES 2015, LIPIcs, 2018.
- **[SOTA]** Danil Annenkov, Paolo Capriotti, Nicolai Kraus, Christian Sattler. *Two-level type theory and applications.* Mathematical Structures in Computer Science 33(8), 2023.
- **[SOTA]** Chris Kapulkin, Peter LeFanu Lumsdaine. *The homotopy theory of type theories.* Advances in Mathematics 337, 2018.
- **[SOTA]** Steve Awodey. *Natural models of homotopy type theory.* Mathematical Structures in Computer Science 28(2), 2018.
- **[Survey]** Pierre-Louis Curien, Richard Garner, Martin Hofmann. *Revisiting the categorical interpretation of dependent type theory.* Theoretical Computer Science 546, 2014.
- **[Survey]** Hugo Herbelin. *A dependently-typed construction of semi-simplicial types.* Mathematical Structures in Computer Science 25(5), 2015.
- **[Survey]** Benno van den Berg, Richard Garner. *Types are weak $\omega$-groupoids.* Proceedings of the London Mathematical Society 102(2), 2011.

## 10. Worked Example / Concrete Special Case

**Semi-simplicial types, levels 0–3.** A semi-simplicial type is a sequence $X_n$ with face maps and no degeneracies. In HoTT one writes it "matched", each level indexed by its boundary:

$$X_0 : \mathcal{U},\qquad X_1 : X_0 \to X_0 \to \mathcal{U},$$
$$X_2 : \prod_{a,b,c:X_0} X_1(a,b)\to X_1(b,c)\to X_1(a,c)\to\mathcal{U},$$
$$X_3 : \prod_{a,b,c,d:X_0}\ \prod_{\substack{f:X_1(a,b),\,g:X_1(b,c),\,h:X_1(c,d)\\ i:X_1(a,c),\,j:X_1(b,d),\,k:X_1(a,d)}} X_2(f,g,i)\to X_2(g,h,j)\to X_2(i,h,k)\to X_2(f,j,k)\to\mathcal{U}.$$

Each level is writable; counts follow the simplex: level $n$ takes as arguments one filler for each of the $\binom{n+1}{m+1}$ $m$-faces, $m<n$. For $n=3$: $4$ vertices, $6$ edges, $4$ triangles — exactly the arguments above.

**Where the uniform definition breaks.** The natural attempt is to define, simultaneously with $X$, a *boundary* operator
$$\mathrm{Sk}_n : \big(\text{first } n \text{ levels}\big)\to \mathcal{U},\qquad X_{n+1}:\mathrm{Sk}_{n+1}(X)\to\mathcal U,$$
by recursion on $n$. The recursion must produce, at step $n+1$, both the type $\mathrm{Sk}_{n+1}$ *and* proofs that the face maps $d_i \circ d_j = d_{j-1}\circ d_i$ ($i<j$) commute. In a strict setting these are definitional equalities and the recursion goes through. In HoTT they are inhabitants of identity types, so the recursion must also produce coherences between those proofs at level $n+2$, then coherences between coherences, ad infinitum. The recursion's *motive* is thus not a fixed type family but one that grows with $n$ — there is no HoTT-definable $\mathbb N$-indexed motive to feed to $\mathbb{N}$-recursion.

**How each partial result cuts the knot.** In the groupoid model everything is 1-truncated: coherences above level 2 are trivially inhabited and the tower terminates, so $X$ exists. In two-level type theory $X_0$ lives in the strict (exo-)layer, $d_i\circ d_j = d_{j-1}\circ d_i$ is a strict equality with no higher structure, and the recursion goes through unchanged. In simplicial or cubical semantics the strictness is imported from the ambient presheaf category — where composition of substitutions is literally composition of functions, hence associative on the nose. What no one has done is perform this cut *inside* plain HoTT.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*