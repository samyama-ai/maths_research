---
id: 08-logic-set-theory/decidability-existential-theory-rationals
title: "Decidability of the Existential Theory of the Rationals"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Decidability of the Existential Theory of the Rationals

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/decidability-existential-theory-rationals` · **Status:** open

## 1. Problem Statement / Conjecture

Is there an algorithm that, given a polynomial $f \in \mathbb{Z}[x_1,\dots,x_n]$, decides whether $f$ has a zero in $\mathbb{Q}^n$?

Equivalently: is the existential first-order theory of the field $\mathbb{Q}$ in the language of rings $L_{\mathrm{ring}} = \{+,\cdot,-,0,1\}$ decidable? This is **Hilbert's Tenth Problem over $\mathbb{Q}$** (H10/$\mathbb{Q}$), open since Matiyasevich settled the case of $\mathbb{Z}$ in 1970.

A resolution requires either:

- **(Negative)** an effective reduction of the halting problem to rational solvability — in practice, a *Diophantine definition* of $\mathbb{Z}$ in $\mathbb{Q}$, or a Diophantine model of $(\mathbb{Z};+,\cdot)$ over $\mathbb{Q}$; or
- **(Positive)** a terminating decision procedure, which would need to decide $X(\mathbb{Q}) \neq \emptyset$ for *every* variety $X/\mathbb{Q}$ — already open for genus-1 curves.

Note the asymmetry: the set of true existential sentences over $\mathbb{Q}$ is recursively enumerable (enumerate $\mathbb{Q}^n$ and test). So the problem is exactly whether it is also co-r.e.

## 2. Mathematical Foundations

**Diophantine sets.** For a commutative ring $R$, a set $S \subseteq R^m$ is *Diophantine over $R$* if there is $f \in R[x_1,\dots,x_m,y_1,\dots,y_n]$ with
$$S = \{\,\mathbf{x} \in R^m : \exists \mathbf{y} \in R^n,\ f(\mathbf{x},\mathbf{y}) = 0\,\}.$$
Over a field, finite systems collapse to one equation ($f_1 = \dots = f_k = 0 \iff \sum f_i^2 = 0$ over $\mathbb{Q}$, since $\mathbb{Q}$ is formally real), and inequations are Diophantine ($x \neq 0 \iff \exists y\ xy = 1$). Hence the existential theory of $\mathbb{Q}$ is decidable iff there is an algorithm deciding membership in Diophantine sets defined by a single equation.

**DPRM.** Davis–Putnam–Robinson (1961) and Matiyasevich (1970): a set $S \subseteq \mathbb{Z}^m$ is Diophantine over $\mathbb{Z}$ iff it is recursively enumerable. Hence H10/$\mathbb{Z}$ is undecidable.

**Transfer principle.** If $\mathbb{Z}$ is Diophantine over $\mathbb{Q}$, i.e. there is $g \in \mathbb{Z}[t,y_1,\dots,y_n]$ with
$$t \in \mathbb{Z} \iff \exists \mathbf{y} \in \mathbb{Q}^n,\ g(t,\mathbf{y}) = 0 \qquad (t \in \mathbb{Q}),$$
then for $f \in \mathbb{Z}[\mathbf{x}]$ the sentence $\exists \mathbf{x}\in\mathbb{Z}^n\, f = 0$ translates into an existential $\mathbb{Q}$-sentence, and H10/$\mathbb{Q}$ is undecidable. More generally a *Diophantine model* — a Diophantine set $A \subseteq \mathbb{Q}^k$ with a bijection $\varphi:\mathbb{Z} \to A$ whose graphs of $+$ and $\cdot$ are Diophantine — suffices.

**Local obstructions.** For a variety $X/\mathbb{Q}$, $X(\mathbb{Q}) \neq \emptyset \Rightarrow X(\mathbb{Q}_v) \neq \emptyset$ for all places $v \in \{\infty, 2, 3, 5, \dots\}$. The converse (Hasse principle) holds for quadrics (Hasse–Minkowski) but fails in general. Each local condition is decidable: $\mathrm{Th}_\exists(\mathbb{R})$ is decidable (Tarski 1951), and $\mathrm{Th}(\mathbb{Q}_p)$ is decidable (Ax–Kochen–Ershov; Macintyre; Denef's cell decomposition gives elimination), so local solvability is checkable.

**Mazur's conjecture (topological form).** For a variety $X/\mathbb{Q}$, the closure of $X(\mathbb{Q})$ in $X(\mathbb{R})$ (real topology) has finitely many connected components. This forbids a set like $\mathbb{Z} \subseteq \mathbb{R}$, which is infinitely disconnected, from being Diophantine.

## 3. History & State of the Art (SOTA)

- **1900.** Hilbert asks for an algorithm for integer solvability; the rational case is the immediate variant.
- **1949.** Julia Robinson defines $\mathbb{Z}$ in $\mathbb{Q}$ by a first-order formula (of shape $\forall\exists\forall$), using quadratic forms and the Hasse–Minkowski theorem. Consequence: $\mathrm{Th}(\mathbb{Q})$ is undecidable. This does **not** settle the existential fragment.
- **1961–1970.** DPRM theorem; H10/$\mathbb{Z}$ negative.
- **1992.** Mazur, *The topology of rational points*, formulates the conjectures that make a negative answer look hard.
- **2000.** Cornelissen–Zahidi: Mazur's conjecture implies $\mathbb{Z}$ is **not** Diophantine over $\mathbb{Q}$, and rules out Diophantine models built from varieties.
- **2003.** Poonen: H10 is undecidable for large subrings $\mathbb{Z}[S^{-1}] \subseteq \mathbb{Q}$ where the inverted primes have natural density $1$ (complement density $0$), the closest approach to $\mathbb{Q}$ from below.
- **2009.** Poonen: $\mathbb{Z}$ is $\forall\exists$-definable in $\mathbb{Q}$ with $2$ universal and $7$ existential quantifiers.
- **2013.** J. Park: universal ($\forall$-only) definition of $\mathcal{O}_K$ in any number field $K$.
- **2016.** Koenigsmann, *Defining $\mathbb{Z}$ in $\mathbb{Q}$* (Annals): $\mathbb{Q}\setminus\mathbb{Z}$ is Diophantine over $\mathbb{Q}$; equivalently $\mathbb{Z}$ has a universal definition (418 quantifiers). Tools: quaternion algebras, Hasse local–global for the Hilbert symbol, transcendental description of the Jacobson radical of rings of $p$-adic integers.
- **2021.** Daans: uniform universal definitions of finitely generated subrings of global fields, with a sharply reduced quantifier count.
- **2024–2025.** Two independent unconditional proofs (Koymans–Pagano; Alpöge–Bhargava–Ho–Shnidman) that H10 is undecidable for $\mathcal{O}_K$ for **every** number field $K$, removing the Shafarevich–Tate hypothesis of Mazur–Rubin (2010). $\mathbb{Q}$ itself remains untouched.

## 4. Partial Results / Verified Cases

Decidable fragments and neighbouring rings where the answer is known:

- **Degree $\le 2$.** Solvability of any quadratic form equation $Q(x_1,\dots,x_n)=0$ over $\mathbb{Q}$ is decidable by Hasse–Minkowski: check $\mathbb{R}$ and the finitely many $p \mid 2\,\mathrm{disc}(Q)$. Same for conics and all Severi–Brauer varieties.
- **One variable.** $f(x)=0$, $f \in \mathbb{Q}[x]$: rational root theorem; decidable in polynomial time.
- **Genus 0 curves; abelian varieties of rank 0.** Decidable given a Mordell–Weil basis.
- **Rings of integers.** H10 undecidable over $\mathcal{O}_K$ for: totally real $K$ (Denef 1980), $K$ with exactly one conjugate pair of complex embeddings (Pheidas; Shlapentokh), $K$ with an elliptic curve of rank $1$ over $\mathbb{Q}$ with rank $1$ over $K$ (Poonen; Cornelissen–Pheidas–Zahidi), and — unconditionally since 2024 — all number fields.
- **Large subrings of $\mathbb{Q}$.** Undecidable for $\mathbb{Z}[S^{-1}]$ with $S$ a computable set of primes of density $1$ (Poonen 2003), and for complementary pairs of such subrings (Eisenträger–Everest; Perlega).
- **Function fields.** Undecidable for $\mathbb{F}_q(t)$ (Pheidas 1991; Videla; Eisenträger–Shlapentokh), $\mathbb{R}(t)$ and $\mathbb{Q}(t)$ (Denef 1978), $\mathbb{C}(t_1,t_2)$ (Kim–Roush 1992).
- **Definability strength.** $\mathbb{Z}$ is $\Pi_1$-definable in $\mathbb{Q}$ (Koenigsmann 2016), hence the $\forall\exists$-theory of $\mathbb{Q}$ is undecidable. Only the purely existential fragment resists.

## 5. Principal Obstacles

- **Mazur's conjecture blocks the standard attack.** Every known undecidability proof over a ring $R$ builds a Diophantine model of $\mathbb{Z}$. Over $\mathbb{Q}$ the real topology obstructs: a Diophantine set is a projection of a real algebraic set, so — if Mazur is right — its real closure has finitely many components and cannot be $\mathbb{Z}$. Cornelissen–Zahidi made this precise. So the negative answer would require *disproving* a plausible arithmetic-geometric conjecture, not merely a clever encoding.
- **No archimedean-blind encoding is known.** Poonen's density-1 subring results work because inverting almost all primes still leaves finitely many $p$-adic valuations available as a "discreteness" device. Over $\mathbb{Q}$ itself no single place can be isolated existentially: Koenigsmann's construction of $\mathbb{Q}\setminus\mathbb{Z}$ is intrinsically existential, and its complement's universal shape is exactly what cannot be flipped.
- **The positive direction needs effective Mordell–Weil / effective Sha.** To decide $X(\mathbb{Q}) \neq \emptyset$ for a genus-1 curve $C$, one runs descent (bounding the Selmer group) in parallel with a naive point search. The pair terminates iff $Ш(E/\mathbb{Q})$ is finite. Finiteness of $Ш$ is itself open, and even granted it, no *effective* bound on the height of a rational point is known.
- **Quadratic-form methods saturate at degree 2.** Robinson's and Koenigsmann's machinery is built on the Hilbert symbol, which is a degree-2 invariant; it produces universal definitions naturally (a point is an integer iff *all* local conditions hold) and existential ones only by accident.
- **Brauer–Manin and beyond are not known to be exhaustive** or effective for arbitrary varieties, so no uniform algorithm for local-to-global failure exists.

## 6. The Gap

Proven (Section 4): $\mathbb{Z}$ is definable in $\mathbb{Q}$ by a $\Pi_1$ (universal) formula; H10 is undecidable over $\mathbb{Z}$, over $\mathcal{O}_K$ for all number fields, and over density-1 subrings of $\mathbb{Q}$; solvability is decidable for quadratic $f$.

Wanted (Section 1): decide $\exists$ over all of $\mathbb{Q}$.

The gap is one quantifier. Concretely, the boundary is:

$$\text{Is } \mathbb{Z} \text{ (or any Diophantine model of } \mathbb{Z}) \text{ } \Sigma_1\text{-definable over } \mathbb{Q}\,?$$

Koenigsmann gives $\mathbb{Q}\setminus\mathbb{Z} \in \Sigma_1$; complementing a $\Sigma_1$ set is precisely the illegal move. On the positive side, the gap is the step from "decidable for quadrics and rank-0 abelian varieties" to "decidable for one genus-1 curve", which is the effective finiteness of $Ш$.

## 7. Current Research (as of June 2026)

- **Quantifier economy.** Daans, Dittmann and Fehm study *existential rank* and essential dimension of Diophantine sets over global fields, driving Koenigsmann's 418 universal quantifiers down by an order of magnitude and asking how few are possible. A definition with zero universal quantifiers is the target. *(frontier — verify)*
- **Post-2024 number-field program.** The Koymans–Pagano and Alpöge–Bhargava–Ho–Shnidman techniques (rank stability in quadratic twists / $2$-Selmer control) are being pushed toward $S$-integer rings with $S$ growing; extending to $S$ = all primes would give $\mathbb{Q}$. Groups at Utrecht/Leiden, Princeton, MIT and Michigan. *(frontier — verify)*
- **Anti-side.** Work on Mazur's conjecture and its variants for specific families (Colliot-Thélène–Skorobogatov–Swinnerton-Dyer's counterexamples to *strengthened* forms show the topological statement is delicate but the base conjecture survives).
- **Model theory of $\mathbb{Q}$ and adelic structures.** Existential closedness questions, and decidability of $\mathbb{Q}$ with added valuation-like predicates, at Oxford (Koenigsmann's school), Konstanz, and Antwerp.

## 8. Future Work

1. Decide whether $\mathbb{Z}$ admits a Diophantine model over $\mathbb{Q}$ *conditionally* on failure of Mazur's conjecture — i.e. build the encoding from a hypothetical variety with infinitely disconnected rational closure.
2. Prove or refute Mazur's conjecture for a single nontrivial family (e.g. rational points on a fixed K3 surface).
3. Establish effective finiteness of $Ш(E/\mathbb{Q})[n]$ for elliptic curves, yielding a decision procedure for genus-1 curves — a necessary sub-step for any positive answer.
4. Reduce the universal quantifier count for $\mathbb{Z}$ in $\mathbb{Q}$ to a small number and study whether an $\exists$-definition is provably impossible.
5. Interpolate between $\mathbb{Z}[S^{-1}]$ (undecidable, density 1) and $\mathbb{Q}$: identify the exact obstruction to letting $S$ be all primes.

## 9. Key References

- **[Foundational]** J. Robinson. *Definability and decision problems in arithmetic.* Journal of Symbolic Logic 14 (1949), 98–114.
- **[Foundational]** M. Davis, H. Putnam, J. Robinson. *The decision problem for exponential Diophantine equations.* Annals of Mathematics 74 (1961), 425–436.
- **[Foundational]** Yu. Matiyasevich. *Enumerable sets are Diophantine.* Doklady Akademii Nauk SSSR 191 (1970), 279–282.
- **[Foundational]** B. Mazur. *The topology of rational points.* Experimental Mathematics 1 (1992), 35–45.
- **[SOTA]** J. Koenigsmann. *Defining $\mathbb{Z}$ in $\mathbb{Q}$.* Annals of Mathematics 183 (2016), 73–93.
- **[SOTA]** B. Poonen. *Characterizing integers among rational numbers with a universal-existential formula.* American Journal of Mathematics 131 (2009), 675–682.
- **[SOTA]** B. Poonen. *Hilbert's Tenth Problem and Mazur's conjecture for large subrings of $\mathbb{Q}$.* Journal of the AMS 16 (2003), 981–990.
- **[SOTA]** J. Park. *A universal first-order formula defining the ring of integers in a number field.* Algebra & Number Theory 7 (2013), 2077–2095.
- **[SOTA]** N. Daans. *Universally defining finitely generated subrings of global fields.* Documenta Mathematica 26 (2021), 1851–1869.
- **[SOTA]** B. Mazur, K. Rubin. *Ranks of twists of elliptic curves and Hilbert's tenth problem.* Inventiones Mathematicae 181 (2010), 541–575.
- **[Structural]** G. Cornelissen, K. Zahidi. *Topology of Diophantine sets: remarks on Mazur's conjectures.* In *Hilbert's Tenth Problem: Relations with Arithmetic and Algebraic Geometry*, Contemporary Mathematics 270, AMS (2000), 253–260.
- **[Structural]** J.-L. Colliot-Thélène, A. Skorobogatov, P. Swinnerton-Dyer. *Double fibres and double covers: paucity of rational points.* Acta Arithmetica 79 (1997), 113–135.
- **[Structural]** E. Selmer. *The Diophantine equation $ax^3+by^3+cz^3=0$.* Acta Mathematica 85 (1951), 203–362.
- **[Survey]** B. Poonen. *Undecidability in number theory.* Notices of the AMS 55 (2008), 344–350.
- **[Survey]** A. Shlapentokh. *Hilbert's Tenth Problem: Diophantine Classes and Extensions to Global Fields.* Cambridge University Press, 2007.
- **[Survey]** T. Pheidas, K. Zahidi. *Undecidability of existential theories of rings and fields: a survey.* Contemporary Mathematics 270, AMS (2000), 49–105.

## 10. Worked Example / Concrete Special Case

**(a) A decidable instance.** Decide $\exists x,y \in \mathbb{Q}:\ x^2 + y^2 = 3$.

Homogenise: write $x = a/c$, $y = b/c$ with $a,b,c \in \mathbb{Z}$, $c \neq 0$, $\gcd(a,b,c)=1$. Then
$$a^2 + b^2 = 3c^2.$$
Reduce mod $3$. The squares mod $3$ are $\{0,1\}$, so $a^2+b^2 \equiv 0 \pmod 3$ forces $a^2 \equiv b^2 \equiv 0$, i.e. $3 \mid a$ and $3 \mid b$. Write $a = 3a'$, $b=3b'$: then $9(a'^2+b'^2) = 3c^2$, so $3 \mid c^2$, so $3\mid c$ — contradicting $\gcd(a,b,c)=1$. Hence **no rational solution**.

This is exactly the Hasse–Minkowski algorithm at work: the form $X^2+Y^2-3Z^2$ is isotropic over $\mathbb{R}$ and over $\mathbb{Q}_p$ for $p \neq 3$, but anisotropic over $\mathbb{Q}_3$ (Hilbert symbol $(-1,3)_3 = -1$). Finitely many local checks, all effective. Every degree-2 instance of H10/$\mathbb{Q}$ falls this way.

**(b) Where the method dies.** Consider Selmer's curve
$$C:\ 3x^3 + 4y^3 + 5z^3 = 0 .$$
$C$ has points over $\mathbb{R}$ (cube roots exist for all reals) and over every $\mathbb{Q}_p$ — direct Hensel-lifting checks succeed at $p = 2,3,5$ and $p \nmid 60$ is handled by Weil's bound plus Hensel. Yet $C(\mathbb{Q}) = \emptyset$ (Selmer 1951). The obstruction lives in $Ш(E/\mathbb{Q})$ for the Jacobian $E: u^3+v^3 = 60\,w^3$; it is invisible to any finite collection of congruence conditions.

**Consequence for the decision problem.** Part (a) shows the algorithm exists in degree 2. Part (b) shows that from degree 3 onward, "no rational point" is not certified by local data, and the only known certificate — descent — terminates only if $Ш$ is finite. A decision procedure for $\mathrm{Th}_\exists(\mathbb{Q})$ must handle every such curve uniformly and effectively; conversely, a negative answer must construct from equations of this kind a Diophantine copy of $\mathbb{Z}$, which Mazur's conjecture says is impossible. Both routes are blocked at exactly this example.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*