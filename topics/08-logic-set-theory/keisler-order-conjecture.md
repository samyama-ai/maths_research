---
id: 08-logic-set-theory/keisler-order-conjecture
title: "Keisler Order Conjecture"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Keisler Order Conjecture

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/keisler-order-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Keisler's order $\trianglelefteq$ is a pre-order on complete countable first-order theories measuring how hard a theory is to saturate in regular ultrapowers. The **Keisler Order Conjecture** is the program, implicit in Keisler (1967) and explicit in Shelah's classification theory, of computing $\trianglelefteq$ completely:

1. **Classification.** Every $\trianglelefteq$-class is characterized by a syntactic dividing line (a property of formulas of $T$, checkable without set theory).
2. **Linearity.** $\trianglelefteq$ is a linear order on its classes.
3. **Maximum class.** $T$ is $\trianglelefteq$-maximum if and only if $T$ has $\mathrm{SOP}_2$ (equivalently $\mathrm{TP}_1$).
4. **Simplicity dividing line.** Every simple theory is strictly $\trianglelefteq$-below every non-simple theory.

A complete resolution means: an explicit list of the classes, a syntactic invariant for each, and a proof that no other class exists. Statement (2) is **false** modulo a supercompact cardinal (Ulrich 2018); statements (1), (3), (4) remain open. The number of classes is known to be infinite (Malliaris–Shelah 2018), refuting the earlier expectation of finitely many.

## 2. Mathematical Foundations

Let $\lambda \ge \aleph_0$ and let $D$ be an ultrafilter on $\lambda$.

**Regularity.** $D$ is *regular* if there is $E \subseteq D$ with $|E| = \lambda$ such that every infinite $E' \subseteq E$ has $\bigcap E' = \emptyset$. Equivalently, there is $\{X_i : i < \lambda\} \subseteq D$ with each $t < \lambda$ lying in only finitely many $X_i$.

**Saturation.** Say $D$ *$\lambda^+$-saturates* $T$ if for some (equivalently, by Keisler's theorem, every) $M \models T$ with $|M| \le \lambda$, the ultrapower $M^\lambda/D$ is $\lambda^+$-saturated.

**Keisler's order.**
$$T_1 \trianglelefteq T_2 \iff \forall \lambda \ge \aleph_0\ \forall D \text{ regular on } \lambda:\ \big(D \text{ saturates } T_2 \Rightarrow D \text{ saturates } T_1\big).$$
Write $T_1 \bowtie T_2$ for $\trianglelefteq$-equivalence and $T_1 \lhd T_2$ for strict.

**Goodness.** $D$ on $\lambda$ is *$\lambda^+$-good* if every monotone $f : [\lambda]^{<\omega} \to D$ has a multiplicative refinement $g$, i.e. $g(u) \subseteq f(u)$ and $g(u \cup v) = g(u) \cap g(v)$. Keisler (1964) and Kunen (1972): $\lambda^+$-good countably incomplete regular ultrafilters exist in ZFC, and such $D$ saturate every countable $T$. Hence $\trianglelefteq$ has a maximum class, witnessed by goodness.

**Dividing lines.** For a formula $\varphi(x;y)$:
- *fcp* (finite cover property): for arbitrarily large $k$ there are $a_1,\dots,a_k$ with $\{\varphi(x;a_i)\}$ $k$-inconsistent but $(k-1)$-consistent.
- $\mathrm{SOP}_2$/$\mathrm{TP}_1$: there is a tree $(a_\eta)_{\eta \in 2^{<\omega}}$ with $\{\varphi(x;a_{\eta\restriction n})\}_n$ consistent along branches and $\{\varphi(x;a_\eta),\varphi(x;a_\nu)\}$ inconsistent for $\eta \perp \nu$.
- $\mathrm{TP}_2$: an array $(a_{i,j})_{i,j<\omega}$ with rows $2$-inconsistent and every choice function consistent. $T$ simple $\iff$ no $\mathrm{TP}_1$ and no $\mathrm{TP}_2$.

**Known bottom of the order.** $\mathcal{K}_1 = \{T : T \text{ has nfcp}\}$ (minimum), $\mathcal{K}_2 = \{T \text{ stable with fcp}\}$, $\mathcal{K}_3 = $ the class of the random graph $T_{\mathrm{rg}}$ (minimum unstable).

## 3. History & State of the Art (SOTA)

- **1967.** Keisler, *Ultraproducts which are not saturated* (JSL 32), defines $\trianglelefteq$, proves the maximum class is non-empty (linear orders are maximum, via goodness) and asks for the full computation.
- **1978.** Shelah, *Classification Theory*, Ch. VI: minimum class $=$ nfcp; second class $=$ stable with fcp; unstable theories sit strictly above; the order has at least these three lowest classes.
- **1996.** Shelah, *Toward classifying unstable theories* (APAL 80): $\mathrm{SOP}_3 \Rightarrow$ maximality; $\mathrm{SOP}_2$-maximality conjectured.
- **2009–2012.** Malliaris develops the characteristic-sequence method and hypergraph-sequence tools, isolating *flexible*, *good for $T$* ultrafilter properties.
- **2016.** Malliaris–Shelah, *Cofinality spectrum theorems* (JAMS 29): $\mathfrak{p} = \mathfrak{t}$, $T_{\mathrm{rg}}$ is minimum among unstable theories, and $\mathrm{SOP}_2 \Rightarrow$ maximality.
- **2016.** Malliaris–Shelah, *Existence of optimal ultrafilters* (Adv. Math. 290): optimal ultrafilters separate simple low theories from $\mathrm{TP}_2$ theories.
- **2018.** Malliaris–Shelah (Israel J. Math 224): **infinitely many classes**, via generic $k$-ary $n$-free hypergraph theories $T_{n,k}$, all simple.
- **2018.** Ulrich (JSL 83): assuming a supercompact cardinal, $\trianglelefteq$ is **not linear**.
- **2021.** Malliaris–Shelah, *Keisler's order is not simple (and simple theories may not be either)* (Adv. Math. 392): large families of incomparable-or-strictly-ordered simple theories, built by Boolean-algebra/ultrafilter constructions.

## 4. Partial Results / Verified Cases

| Region | Result | Source |
|---|---|---|
| Minimum class | $T$ minimum $\iff$ nfcp (e.g. pure equality, $\mathrm{Th}(\mathbb{Z},+)$, algebraically closed fields, any uncountably categorical nfcp theory) | Shelah 1978 |
| Second class | stable $+$ fcp (e.g. infinitely many refining equivalence relations with classes of size $n$) is exactly one class, immediately above | Shelah 1978 |
| Minimum unstable | $T_{\mathrm{rg}} \trianglelefteq T$ for every unstable $T$; $T_{\mathrm{rg}}$ is a single class | Malliaris–Shelah 2016 (JAMS) |
| Maximum | $\mathrm{SOP}_3 \Rightarrow$ max (Shelah 1996); improved to $\mathrm{SOP}_2 \Rightarrow$ max (2016). Covers DLO, $\mathrm{Th}(\mathbb{Q},<)$, Peano arithmetic, ZFC-like theories, any theory with the strict order property | Shelah; Malliaris–Shelah |
| Infinitely many classes | For $2 \le n < k$, the $n$-free $k$-hypergraph theories $T_{n,k}$ realize infinitely many distinct classes, all strictly between $T_{\mathrm{rg}}$ and the maximum | Malliaris–Shelah 2018 |
| Non-linearity | Consistent (supercompact) that there exist $\trianglelefteq$-incomparable countable theories | Ulrich 2018 |
| $\lambda = \aleph_0$ | Degenerate: every ultrafilter on $\omega$ is regular and $\aleph_1$-good, so all countable theories are saturated equally; the order is only informative for $\lambda \ge \aleph_1$ | Keisler 1967 |

## 5. Principal Obstacles

- **Two-sided problem.** Proving $T_1 \lhd T_2$ needs a *construction* of a regular ultrafilter saturating $T_1$ but not $T_2$. Constructing regular ultrafilters with precisely calibrated saturation is the hard half: the only flexible technique is Keisler-style transfer from a Boolean algebra $\mathcal{B}$ with a suitable independent family plus a $\lambda^+$-good ultrafilter on $\mathcal{B}$, and the possible "shapes" of such $\mathcal{B}$ are poorly understood.
- **Set-theoretic entanglement.** Saturation of ultrapowers is sensitive to cardinal arithmetic and cofinality spectra. The Malliaris–Shelah $\mathfrak{p} = \mathfrak{t}$ theorem shows the order encodes genuine set-theoretic content, so purely model-theoretic (syntactic) arguments cannot suffice; conversely, Ulrich's non-linearity uses large cardinals, so ZFC-only answers may be unavailable.
- **Simple unstable theories resist local analysis.** Below $\mathrm{TP}_2$, saturation depends on higher-arity amalgamation data, not on a single formula. Characteristic-sequence methods reduce $\varphi$-types to hypergraph sequences, but the relevant combinatorics (Ramsey-type behaviour of $k$-uniform hypergraphs at uncountable $\lambda$) is itself open.
- **No forcing/absoluteness machinery.** Unlike Borel-reducibility classifications, $\trianglelefteq$ has no known absolute reformulation; a candidate one via Boolean ultrapowers (Ulrich) is not yet proven equivalent for all theories.
- **$\mathrm{SOP}_2$ gap.** No known invariant strictly between simple and $\mathrm{SOP}_2$ gives maximality, but the class $\mathrm{NSOP}_2 \cap$ non-simple ($\mathrm{TP}_2$, $\mathrm{SOP}_1$) is essentially uncharted.

## 6. The Gap

The proven picture is: a determined bottom ($\mathcal{K}_1 \lhd \mathcal{K}_2 \lhd \mathcal{K}_3 = [T_{\mathrm{rg}}]$), an infinite family of simple classes above $\mathcal{K}_3$, a maximum class containing all $\mathrm{SOP}_2$ theories, and a consistent failure of linearity. The gap is everything in between:

- Is $\mathrm{SOP}_2$ **necessary** for maximality? Equivalently: is every $\mathrm{NSOP}_2$ theory strictly below the maximum? The missing step is a construction of a regular $D$ that saturates all $\mathrm{NSOP}_2$ theories yet is not $\lambda^+$-good — no such $D$ is known for any $\lambda$.
- Are all simple theories below all non-simple ones? Known only for restricted subclasses (low simple vs. $\mathrm{TP}_2$, via optimal ultrafilters).
- Is $\trianglelefteq$ well-founded? Is the number of classes exactly $2^{\aleph_0}$, or $2^{2^{\aleph_0}}$?
- Is non-linearity a ZFC theorem, or is linearity consistent?

## 7. Current Research (as of June 2026)

- **Chicago / Jerusalem axis.** Malliaris (U. Chicago) and Shelah (HUJI/Rutgers) continue the ultrafilter-construction program: separating simple theories by explicit hypergraph sequences and by Boolean-algebra-theoretic invariants of the constructing algebra. Recent work reframes $\trianglelefteq$ on simple theories as a question about "which sequences of $k$-uniform hypergraph patterns can be realized" *(frontier — verify)*.
- **Boolean ultrapowers and absoluteness.** Ulrich's reformulation of $\trianglelefteq$ via Boolean ultrapowers aims to remove regular ultrafilters entirely, yielding a version potentially absolute between models of ZFC; proving equivalence with the classical order for all $T$ is an active target *(frontier — verify)*.
- **Interaction with $\mathrm{NSOP}_1$/Kim-independence.** The rapid post-2017 development of $\mathrm{NSOP}_1$ theories (Kaplan–Ramsey and collaborators) supplies new candidate dividing lines just above simplicity that had no name when the order was first studied; whether $\mathrm{NSOP}_1$ is a $\trianglelefteq$-relevant line is open.
- **Cardinal-characteristic side.** Continued exploitation of cofinality spectrum problems, which produced $\mathfrak{p} = \mathfrak{t}$, to bound saturation of $\mathrm{NSOP}_2$ theories.

## 8. Future Work

- Isolate a *lower* bound for maximality: show any theory in the maximum class interprets a tree order pattern, closing $\mathrm{SOP}_2 \Leftrightarrow$ max.
- Build a "generic" ultrafilter construction schema parameterized by an abstract independence notion, so that each dividing line yields an ultrafilter by machine rather than by hand.
- Determine the order type: prove or refute well-foundedness of $\trianglelefteq$ restricted to simple theories.
- Settle whether non-linearity holds in ZFC alone by lowering Ulrich's large-cardinal hypothesis.
- Relate $\trianglelefteq$ to Borel complexity of countable models (Laskowski-style invariants), which would give an independent, absolute handle.

## 9. Key References

- **[Foundational]** H. J. Keisler. *Ultraproducts which are not saturated.* Journal of Symbolic Logic **32** (1967), 23–46.
- **[Foundational]** H. J. Keisler. *Good ideals in fields of sets.* Annals of Mathematics **79** (1964), 338–359.
- **[Foundational]** S. Shelah. *Classification Theory and the Number of Non-Isomorphic Models.* North-Holland, 1978 (rev. ed. 1990), Chapter VI.
- **[Foundational]** K. Kunen. *Ultrafilters and independent sets.* Transactions of the AMS **172** (1972), 299–306.
- **[Key]** S. Shelah. *Toward classifying unstable theories.* Annals of Pure and Applied Logic **80** (1996), 229–255.
- **[Key]** M. Malliaris. *Hypergraph sequences as a tool for saturation of ultrapowers.* Journal of Symbolic Logic **77** (2012), 195–223.
- **[SOTA]** M. Malliaris, S. Shelah. *Cofinality spectrum theorems in model theory, set theory, and general topology.* Journal of the AMS **29** (2016), 237–297.
- **[SOTA]** M. Malliaris, S. Shelah. *Existence of optimal ultrafilters and the fundamental complexity of simple theories.* Advances in Mathematics **290** (2016), 614–681.
- **[SOTA]** M. Malliaris, S. Shelah. *Keisler's order has infinitely many classes.* Israel Journal of Mathematics **224** (2018), 189–230.
- **[SOTA]** D. Ulrich. *Keisler's order is not linear, assuming a supercompact.* Journal of Symbolic Logic **83** (2018), 634–641.
- **[SOTA]** M. Malliaris, S. Shelah. *Keisler's order is not simple (and simple theories may not be either).* Advances in Mathematics **392** (2021), 108036.
- **[Survey]** M. Malliaris. *Model theory and ultraproducts.* Proceedings of the ICM 2018, Vol. 2, World Scientific, 2018.
- **[Textbook]** C. C. Chang, H. J. Keisler. *Model Theory*, 3rd ed. North-Holland, 1990.

## 10. Worked Example / Concrete Special Case

**Claim.** $T_= $, the theory of an infinite set in the empty language, is $\trianglelefteq$-minimum: every regular $D$ on $\lambda$ gives a $\lambda^+$-saturated ultrapower.

Let $M$ be countably infinite, $N = M^\lambda/D$, and let $p(x)$ be a type over $A \subseteq N$ with $|A| = \lambda$. In the empty language every formula is a Boolean combination of $x = a$, so consistency forces
$$p(x) = \{\, x \neq a_i \;:\; i < \lambda \,\},\qquad a_i = f_i/D .$$
Fix a regular family $\{X_i : i<\lambda\} \subseteq D$: each coordinate $t < \lambda$ lies in only finitely many $X_i$. Put $u(t) = \{ i < \lambda : t \in X_i\}$, a **finite** set. Define $f : \lambda \to M$ by choosing
$$f(t) \in M \setminus \{ f_i(t) : i \in u(t) \},$$
possible since $|u(t)| < \omega$ and $M$ is infinite. For each $i$, if $t \in X_i$ then $i \in u(t)$, so $f(t) \neq f_i(t)$. Hence $\{t : f(t) \neq f_i(t)\} \supseteq X_i \in D$, so $f/D \neq a_i$ in $N$. Thus $f/D \models p$. Regularity alone sufficed — this is exactly the content of "nfcp $\Rightarrow$ minimum".

**Contrast (maximum class).** Take $T = \mathrm{Th}(\mathbb{Q},<)$ and the cut type $p(x) = \{c_i < x : i<\lambda\} \cup \{x < d_j : j<\lambda\}$. Realizing all such types for all $\lambda$-sized parameter sets forces $D$ to satisfy: for every monotone $f : [\lambda]^{<\omega} \to D$ there is a multiplicative refinement $g$ — i.e. $D$ must be $\lambda^+$-good. Take $D$ regular but *not* $\lambda^+$-good (such $D$ exist for every $\lambda \ge \aleph_1$: build the ultrafilter from an independent family of functions so that some monotone $f$ has no multiplicative refinement). Then $D$ still saturates $T_=$ by the computation above, but $(\mathbb{Q},<)^\lambda/D$ omits a cut of coinitiality/cofinality $\le \lambda$. So
$$T_= \lhd \mathrm{Th}(\mathbb{Q},<),$$
and the same $D$ separates the bottom from the top. The unsolved part of the conjecture is precisely which theories between these two poles such an ultrafilter can be tuned to separate.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*