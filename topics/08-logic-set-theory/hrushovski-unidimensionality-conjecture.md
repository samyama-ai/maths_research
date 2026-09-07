---
id: 08-logic-set-theory/hrushovski-unidimensionality-conjecture
title: "Hrushovski's Unidimensionality Conjecture"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hrushovski's Unidimensionality Conjecture

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/hrushovski-unidimensionality-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Conjecture (unidimensionality conjecture; Shelah, 1970s).** Every unidimensional complete first-order theory is superstable.

Here a stable theory $T$ is *unidimensional* if any two non-algebraic stationary types (over any parameter sets, in the monster model) are non-orthogonal — informally, models of $T$ carry only one independent dimension. Combined with Shelah's characterisation

$$T \text{ countable is } \aleph_1\text{-categorical} \iff T \text{ is superstable and unidimensional},$$

the conjecture asserts that a single-dimension countable theory is automatically $\aleph_1$-categorical, hence $\omega$-stable of finite Morley rank. A complete proof must rule out *strictly stable* unidimensional theories: a stable $T$ with $\kappa(T) > \aleph_0$, i.e. admitting an infinite forking chain, and yet with all non-algebraic types pairwise non-orthogonal. A disproof would exhibit one such theory.

The name in this catalog follows common usage: the statement is Shelah's problem, but it is invariably cited through **Hrushovski's 1990 solution**, "Unidimensional theories are superstable". The page is filed as `solved-recently` because the first-order core is a theorem while its analogues — simple/hypersimple theories, continuous logic, abstract elementary classes — are still moving.

## 2. Mathematical Foundations

Work in $T^{\mathrm{eq}}$ inside a monster model $\mathfrak{C} \models T$; $\downarrow$ denotes non-forking independence.

**Stability.** $T$ is *stable* if for some infinite $\lambda$, $|S_1(A)| \le \lambda$ whenever $|A| \le \lambda$. Let
$$\kappa(T) = \min\{\kappa : \text{no type forks over all subsets of its domain along a chain of length } \kappa\}.$$
$T$ is *superstable* iff $\kappa(T) = \aleph_0$: every type $p \in S(A)$ does not fork over some finite $A_0 \subseteq A$. *Strictly stable* means stable and not superstable; then there are $A_0 \subset A_1 \subset \cdots$ and $p_n \in S(A_n)$ with $p_{n+1}$ forking over $A_n$ for all $n < \omega$.

**Orthogonality.** For stationary $p \in S(A)$, $q \in S(B)$, write $p \perp q$ if for every $C \supseteq A \cup B$ and all $a \models p|C$, $b \models q|C$ (non-forking extensions), $a \downarrow_C b$. Non-orthogonality $p \not\perp q$ is the assertion that some non-forking extensions are dependent.

**Unidimensionality.** $T$ is unidimensional iff $p \not\perp q$ for all non-algebraic stationary $p,q$. Equivalent formulations for stable $T$: (i) $T$ has no *Vaughtian-pair-like* splitting of dimension; (ii) for every $\lambda > |T|$, any two $\lambda$-saturated models of cardinality $\lambda$ are isomorphic.

**Regular types.** $p$ is *regular* if it is stationary and, for every $B \supseteq \operatorname{dom}(p)$, forking extensions of $p$ over $B$ are orthogonal to $p$. Regular types carry a pregeometry via $\operatorname{cl}(X) = \{a : a \not\downarrow_{\operatorname{dom}(p)} X\}$, and the associated dimension $\dim(p, M)$ is well defined. In a superstable theory every non-algebraic type is non-orthogonal to a regular type, and models are determined up to isomorphism by the dimension function on regular types; unidimensionality collapses that function to a single cardinal, giving categoricity.

**Baldwin–Lachlan.** For countable $T$: $T$ is $\aleph_1$-categorical $\iff$ $T$ is $\omega$-stable with no Vaughtian pair $\iff$ $T$ is superstable and unidimensional. An $\aleph_1$-categorical theory satisfies $\operatorname{RM}(x = x) < \omega$.

**Theorem (Hrushovski 1990).** If $T$ is countable and unidimensional then $T$ is superstable — hence $\omega$-stable, $\aleph_1$-categorical, of finite Morley rank.

## 3. History & State of the Art (SOTA)

- **1965.** Morley proves categoricity in one uncountable power implies categoricity in all; the notion of rank and totally transcendental theories enters.
- **1971.** Baldwin–Lachlan replace Morley's transfinite argument with strongly minimal sets and Vaughtian pairs, exposing "dimension" as the invariant.
- **1970s–1978.** Shelah's classification theory isolates regular types, orthogonality, weight, and $\kappa(T)$, and proves the superstable half: superstable + unidimensional $\Rightarrow$ $\aleph_1$-categorical. The converse direction leaves the *unidimensionality problem*: can a strictly stable theory have one dimension? Shelah conjectured no.
- **1980s.** Hrushovski's work on regular and locally modular types (LNM 1292, 1987) builds the group-configuration machinery later reused. Attempts to settle the problem by direct rank-counting fail because strictly stable theories have no ordinal-valued rank on all types.
- **1990.** Hrushovski, *Unidimensional theories are superstable* (APAL 50, 117–138): a strictly stable unidimensional theory is impossible. The proof shows that a non-superstable stable theory always produces two orthogonal non-algebraic types, contradicting unidimensionality.
- **1993.** Hrushovski's new strongly minimal set shows the *internal* structure of unidimensional theories is not classifiable by Zilber's trichotomy — the theorem controls dimension count, not geometry.
- **2000s–2020s.** Transfer of the statement to simple and hypersimple theories (Shami), to metric structures, and to non-elementary classes (Grossberg–VanDieren, Vasey), where the analogues remain partly open.

## 4. Partial Results / Verified Cases

- **Superstable theories, any language.** Unidimensional $\Rightarrow$ categorical in every $\lambda > |T|$ (Shelah). Pure classification-theoretic; no rank hypothesis beyond $\kappa(T) = \aleph_0$.
- **$\omega$-stable countable theories.** Unidimensional $\iff$ no Vaughtian pair $\iff$ $\aleph_1$-categorical (Baldwin–Lachlan, 1971); Morley rank of $x=x$ is finite, typically small: $\operatorname{RM} = 1$ for strongly minimal theories (ACF$_p$, vector spaces over a fixed field, $(\mathbb{Z}, s)$), $\operatorname{RM} = n$ for $\mathrm{Th}$ of an $n$-dimensional bundle over a strongly minimal set.
- **Countable languages, full generality.** Hrushovski (1990): every unidimensional countable $T$ is $\omega$-stable of finite Morley rank. This is the main verified case.
- **Uncountable languages.** The conclusion "superstable" for $|T| > \aleph_0$ is treated in the same paper, but the textbook expositions (Buechler, *Essential Stability Theory*, Ch. 6; Pillay, *Geometric Stability Theory*) present the countable case; the uncountable statement should be checked against the original argument *(frontier — verify)*.
- **Modules.** For $T$ the complete theory of a module, unidimensional theories are exactly those that are $\aleph_1$-categorical, decided by the lattice of pp-definable subgroups — a fully computable class.
- **Groups and fields.** Any unidimensional theory interpreting an infinite field yields an algebraically closed field of finite Morley rank; for $\operatorname{RM} = 1$ the field is strongly minimal, hence ACF.
- **Simple theories.** Countable hypersimple unidimensional theories are supersimple of $\mathrm{SU}$-rank $1$ (Shami) *(frontier — verify scope of hypotheses)*.

## 5. Principal Obstacles

The difficulty was, and in the analogues remains, that **strictly stable theories admit no global ordinal rank**. Standard techniques fail as follows.

- **Morley/$U$-rank counting is unavailable.** In a non-superstable theory, $U(p) = \infty$ for the interesting types, so induction on rank — the engine of Baldwin–Lachlan — has no base.
- **Regular types need not be dense.** In superstable theories every type is non-orthogonal to a regular type, which converts unidimensionality into a single dimension immediately. In strictly stable theories regular types can be scarce or absent over small sets, so the "coordinatise the model by dimensions" strategy stalls.
- **Weight is not finite.** Superstability gives finite weight, hence a workable notion of independent dimensions. Without it, one cannot bound how many pairwise-independent realisations a type contributes, and non-orthogonality no longer forces a single cardinal invariant.
- **Compactness gives no contradiction.** An infinite forking chain $p_0 \subset p_1 \subset \cdots$ is consistent by itself; producing from it a type *orthogonal* to $p_0$ requires constructing a definable family of "small" sets, which the chain does not hand over directly.
- **Geometry is uncontrolled.** Hrushovski's own new strongly minimal set shows that even in the resolved case the pregeometry can be non-locally-modular and non-field-like, so no structural classification of unidimensional theories can be used as a proof route.

Hrushovski's solution circumvents these by an intricate combinatorial construction: from a strictly stable unidimensional $T$ he extracts an infinite tree of forking extensions, and shows the two "levels" of that tree give non-algebraic types with independent realisations in every extension — orthogonality, contradiction.

## 6. The Gap

For countable first-order $T$ there is no gap: Section 4's main entry is Section 1's statement. The live boundary sits one level out:

1. **Beyond stability.** For simple theories the correct analogue is "unidimensional $\Rightarrow$ supersimple of $\mathrm{SU}$-rank $1$". Proven under hypersimplicity and countability; the general simple case is open, because forking in simple theories lacks stationarity, so the canonical-base and regular-type tools used in 1990 do not transfer verbatim. The same gap widens for NSOP$_1$ theories, where Kim-independence replaces forking only over models.
2. **Beyond first order.** In abstract elementary classes and in continuous logic, "orthogonality" and "$\kappa(T)$" must be re-derived from amalgamation and tameness hypotheses. The missing step is a rank-free replacement for the tree-of-forking-extensions construction that survives without compactness.

## 7. Current Research (as of June 2026)

- **AEC categoricity.** Vasey's programme on Shelah's eventual categoricity conjecture (proved for universal classes) supplies dimension theory — independence relations, superstability from tameness — that plays the role of the 1990 theorem in the non-elementary setting. Groups at Harvard/Carnegie Mellon and the Jerusalem school remain the centre.
- **Simple and NSOP$_1$ analogues.** Continuing work by Shami and collaborators on unidimensional simple theories; the target is removing hypersimplicity *(frontier — verify)*.
- **Metric structures.** $\aleph_1$-categoricity for continuous first-order theories, following Ben Yaacov's work on categoricity in cats; a metric unidimensionality theorem is asserted in preprint form *(frontier — verify)*.
- **Applications inside stability.** The theorem is used as a black box in differential and difference algebra: a finite-rank definable set with a single dimension is forced into the $\omega$-stable world, which underpins orthogonality analyses of algebraic ODEs (Freitag–Moosa and collaborators, Illinois/Waterloo).

## 8. Future Work

- Isolate the combinatorial core of Hrushovski's construction as an axiomatic lemma about independence relations, then instantiate it for Kim-independence and for AEC frames.
- Settle unidimensional simple theories without the hypersimplicity assumption; the expected conclusion, $\mathrm{SU}$-rank $1$, would be the exact analogue of finite Morley rank.
- Determine whether unidimensionality plus NIP forces $o$-minimal-like or strongly minimal behaviour, sharpening the finite-Morley-rank conclusion in tame settings.
- Effective versions: given a finite axiomatisation of a unidimensional theory, bound $\operatorname{RM}(x=x)$ in terms of the syntax. No such bound is known.

## 9. Key References

- **[Foundational]** M. Morley. *Categoricity in power.* Transactions of the American Mathematical Society 114 (1965), 514–538.
- **[Foundational]** J. T. Baldwin, A. H. Lachlan. *On strongly minimal sets.* Journal of Symbolic Logic 36 (1971), 79–96.
- **[Foundational]** S. Shelah. *Classification Theory and the Number of Non-Isomorphic Models.* 2nd ed., North-Holland, 1990.
- **[Solution]** E. Hrushovski. *Unidimensional theories are superstable.* Annals of Pure and Applied Logic 50 (1990), 117–138.
- **[Foundational]** E. Hrushovski. *Locally modular regular types.* In: Classification Theory (Chicago, 1985), Lecture Notes in Mathematics 1292, Springer, 1987, 132–164.
- **[Related]** E. Hrushovski. *A new strongly minimal set.* Annals of Pure and Applied Logic 62 (1993), 147–166.
- **[Survey]** S. Buechler. *Essential Stability Theory.* Springer (Perspectives in Mathematical Logic), 1996.
- **[Survey]** A. Pillay. *Geometric Stability Theory.* Oxford University Press, 1996.
- **[Survey]** B. Zilber. *Uncountably Categorical Theories.* Translations of Mathematical Monographs 117, American Mathematical Society, 1993.
- **[Survey]** K. Tent, M. Ziegler. *A Course in Model Theory.* Cambridge University Press, 2012.
- **[SOTA / Recent]** F. O. Wagner. *Simple Theories.* Kluwer Academic Publishers, 2000.
- **[SOTA / Recent]** Z. Shami. *Countable hypersimple unidimensional theories.* Journal of the London Mathematical Society, 2011.
- **[SOTA / Recent]** S. Vasey. *Shelah's eventual categoricity conjecture in universal classes: Part I.* Annals of Pure and Applied Logic 168 (2017), 1609–1642.

## 10. Worked Example / Concrete Special Case

**A theory with two dimensions.** Let $L = \{P\}$ with $P$ unary, and let $T$ say: $P$ is infinite and $\neg P$ is infinite. $T$ is complete and $\omega$-stable. Compute ranks: $P(x)$ and $\neg P(x)$ are strongly minimal (each is an infinite set with no structure), so
$$\operatorname{RM}(x=x) = 1, \qquad \operatorname{deg}(x=x) = 2.$$
Let $p$ = the generic type of $P$ over a model $M$ ("$P(x)$ and $x \ne m$ for all $m \in M$") and $q$ = the generic type of $\neg P$. For any $C \supseteq M$ and any $a \models p|C$, $b \models q|C$ we have $a \downarrow_C b$: $\operatorname{tp}(a/Cb)$ does not fork over $C$, since the only information $b$ carries about $a$ is $a \ne b$, which is already implied. Hence $p \perp q$: **$T$ is not unidimensional.**

The consequence is visible in model counts. A model is determined by $(|P|, |\neg P|)$, so at cardinality $\aleph_1$ there are exactly three models:
$$(\aleph_0, \aleph_1), \quad (\aleph_1, \aleph_0), \quad (\aleph_1, \aleph_1).$$
$T$ is not $\aleph_1$-categorical, matching Baldwin–Lachlan: $(M, N)$ with $P^M = P^N$ infinite and $M \prec N$ proper is a Vaughtian pair.

**A theory with one dimension.** $T = \mathrm{ACF}_0$. Every non-algebraic type over a set $A$ is the generic type of the field, all such types are non-orthogonal (two transcendental elements over a common base can be made dependent by adjoining their sum), $\operatorname{RM}(x=x) = 1$, and $\dim(M) = \operatorname{trdeg}_{\mathbb{Q}}(M)$. A model of size $\aleph_1$ has transcendence degree $\aleph_1$ and is unique — $\aleph_1$-categorical, as required.

**What the theorem adds.** Suppose one tried to build a strictly stable $T$ with a single dimension: take an infinite forking chain $p_0 \subset p_1 \subset \cdots$, $p_n \in S(A_n)$. Hrushovski's theorem says the chain always leaks a second dimension — the levels of the induced tree of forking extensions yield non-algebraic $r, s$ with $r \perp s$, exactly as $p \perp q$ in the first example. So the only way to have one dimension is to have no infinite forking chain at all, i.e. $\kappa(T) = \aleph_0$: superstability, hence $\omega$-stability and finite Morley rank.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*