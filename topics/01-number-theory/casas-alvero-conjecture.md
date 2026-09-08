---
id: 01-number-theory/casas-alvero-conjecture
title: "Casas-Alvero Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Casas-Alvero Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/casas-alvero-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $f \in \mathbb{C}[x]$ be monic of degree $n \ge 1$. Suppose that for every $i = 1, \dots, n-1$ the polynomial $f$ shares a root with its $i$-th derivative $f^{(i)}$ — that is,
$$\gcd\bigl(f, f^{(i)}\bigr) \neq 1 \qquad \text{for } i = 1, \dots, n-1 .$$
**Conjecture (Casas-Alvero, 2001).** Then $f(x) = (x-a)^n$ for some $a \in \mathbb{C}$.

Notes on the hypotheses:

- The roots shared with different derivatives need *not* be the same root. If a single $a$ satisfied $f(a)=f'(a)=\cdots=f^{(n-1)}(a)=0$, then $a$ has multiplicity $n$ and the conclusion is immediate. The content of the conjecture is that the "one root per derivative, chosen freely" version already forces total degeneracy.
- $\mathbb{C}$ may be replaced by any field of characteristic $0$: the statement is equivalent over $\overline{\mathbb{Q}}$ by the Lefschetz principle, since a counterexample's coefficients generate a finitely generated field embeddable in $\mathbb{C}$, and conversely a $\mathbb{C}$-counterexample specializes to $\overline{\mathbb{Q}}$.
- The characteristic-$0$ hypothesis is essential: the analogue is **false** in characteristic $p>0$ (Section 10).

A complete proof must handle every degree $n$; a disproof means exhibiting one monic $f$ of some degree $n$, not a pure $n$-th power, meeting all $n-1$ gcd conditions.

## 2. Mathematical Foundations

Normalize. Composing with a translation $x \mapsto x + c$ and a scaling commutes with differentiation, so the hypothesis and conclusion are invariant under the affine group. Write
$$f(x) = x^n + a_2 x^{n-2} + a_3 x^{n-3} + \cdots + a_n ,$$
where the $x^{n-1}$ coefficient is killed by centering the root centroid at $0$. The conjecture asserts that the only such *Casas-Alvero polynomial* is $f = x^n$, i.e. $a_2 = \cdots = a_n = 0$.

**Resultant formulation.** For $i=1,\dots,n-1$ set
$$R_i(a_2,\dots,a_n) \;=\; \operatorname{Res}_x\bigl(f, f^{(i)}\bigr) \;=\; \Bigl(\tfrac{n!}{(n-i)!}\Bigr)^{n}\!\!\prod_{f(\alpha)=0}\; f^{(i)}(\alpha) ,$$
the product over the $n$ roots with multiplicity. The hypothesis "$f$ and $f^{(i)}$ share a root" is exactly $R_i = 0$. So the Casas-Alvero locus is the affine scheme
$$\mathcal{C}_n \;=\; V(R_1, R_2, \dots, R_{n-1}) \;\subseteq\; \mathbb{A}^{n-1}_{\mathbb{C}} ,$$
with $n-1$ equations in $n-1$ unknowns: the **expected dimension is $0$**. The origin $x^n$ always lies in $\mathcal{C}_n$ (every $f^{(i)}$ vanishes at $0$). The conjecture is the set-theoretic claim
$$\mathcal{C}_n = \{\,0\,\} \quad\text{(as a set)}.$$
$\mathcal{C}_n$ is highly non-reduced at the origin, and $R_i$ is weighted-homogeneous of degree $i\,n$ for weights $\deg a_j = j$, so $\mathcal{C}_n$ is a weighted cone: it is $\{0\}$ iff it contains no nonzero point, i.e. iff the $R_i$ have no common zero at infinity of the weighted projective space.

**Ambient facts used.** (i) Gauss–Lucas: the roots of $f'$ lie in the convex hull of the roots of $f$; iterating, roots of $f^{(i)}$ lie in that hull. (ii) Rolle's theorem for real-rooted $f$. (iii) $\deg \gcd(f,f') = n - \\#\{\text{distinct roots}\}$, so the $i=1$ condition alone says only that $f$ has a repeated root.

**Origin of the problem.** Casas-Alvero arrived at the statement through *higher-order polar germs* of plane curve singularities: for a germ $f$, the polars $f^{(i)}$ carry equisingularity data, and the conjecture says that maximal contact with all polars forces the germ to be a single smooth branch to the power $n$.

## 3. History & State of the Art (SOTA)

- **2001.** Eduardo Casas-Alvero states the conjecture in *Higher order polar germs* (J. Algebra 240), in the context of polar invariants of plane curve germs.
- **2006–2007.** Computer-algebra attacks by elimination (subresultants, Gröbner bases) settle small degrees but stall around $n \approx 8$–$10$: the resultants $R_i$ have astronomically many terms.
- **2007.** Graf von Bothmer, Labs, Schicho and van de Woestijne, *The Casas-Alvero conjecture for infinitely many degrees* (J. Algebra 316), prove the conjecture for all degrees $n = p^k$ and $n = 2p^k$, $p$ prime. The method is reduction modulo $p$: a hypothetical counterexample in characteristic $0$ with $p$-integral coefficients reduces to one in characteristic $p$, where the structure of $f^{(i)}$ (many derivatives vanish identically, Frobenius rigidity) is rigid enough to contradict the arithmetic of $n$'s base-$p$ digits.
- **2011.** Draisma and de Jong publish an expository account, *On the Casas-Alvero conjecture* (EMS Newsletter 80), which fixes the modern framing (resultant scheme, degeneration, char-$p$ obstruction) and is the standard entry point.
- **2014.** Castryck, Laterveer and Ounaïes, *Constraints on counterexamples to the Casas-Alvero conjecture and a verification in degree 12* (Math. Comp. 83), extend the arithmetic families to $n = 3p^k$ and $n = 4p^k$, and derive structural constraints (bounds forcing counterexamples to have many distinct roots and to be non-degenerate at several primes simultaneously). Degree $12 = 3\cdot 2^2$ falls out.
- **2014–present.** No degree outside the four arithmetic families has been settled by a new mechanism; work has shifted to constraints, valuation/Newton-polygon methods, and analytic estimates.

## 4. Partial Results / Verified Cases

- **$n \le 4$:** elementary, by hand (see Section 10 for $n=3$).
- **Prime-power families:** the conjecture holds for
 $$n \in \{\,p^k,\; 2p^k,\; 3p^k,\; 4p^k \;:\; p \text{ prime},\ k \ge 1\,\}.$$
 (Graf von Bothmer–Labs–Schicho–van de Woestijne 2007 for $p^k, 2p^k$; Castryck–Laterveer–Ounaïes 2014 for $3p^k, 4p^k$.)
- **Consequently all $n \le 29$ are settled.** Every integer $2 \le n \le 29$ is $m\,p^k$ with $m \le 4$; the first degree not of that shape is
 $$n = 30 = 2\cdot 3\cdot 5,$$
 since $30, 15, 10$ are not prime powers and $4 \nmid 30$. **Degree $30$ is the smallest open case.** The next open degrees are $35, 40, 42, 45, \dots$ — a set of density $1$ in $\mathbb{N}$, so the known families, though infinite, are sparse.
- **Real-rooted case:** if $f \in \mathbb{R}[x]$ has all roots real, the conjecture holds. Rolle plus induction forces the interlacing pattern to collapse.
- **Few distinct roots:** counterexamples are excluded when the number of distinct roots is small relative to $n$; the Castryck–Laterveer–Ounaïes constraints show a minimal counterexample must be arithmetically non-degenerate at every prime dividing quantities attached to $n$, ruling out the "two-root" and other low-complexity shapes.
- **Local rigidity:** $x^n$ is an isolated point of $\mathcal{C}_n$ for all $n$ — the tangent-space computation at the origin is unobstructed. The open problem is purely about *other* components.

## 5. Principal Obstacles

- **Elimination is intractable.** $\operatorname{Res}(f, f^{(i)})$ is a determinant of size $\approx 2n-i$ in $n-1$ variables; the total-degree growth $\sim in$ and coefficient explosion make Gröbner-basis elimination hopeless beyond very small $n$. Degree $12$ required a bespoke mixture of modular arithmetic, weighted homogeneity and case analysis rather than a direct ideal computation.
- **The statement is false in characteristic $p$.** Any proof must be characteristic-$0$-specific. This kills the most powerful modern toolkit: one cannot simply prove the identity over $\mathbb{F}_p$ for all $p$ and lift. Reduction mod $p$ only works when the failure mode in characteristic $p$ (whole derivatives vanishing identically) is itself blocked by the base-$p$ digits of $n$ — which is exactly what pins the known results to $n = m p^k$ with $m \le 4$. Pushing $m$ to $5$ has resisted; the digit combinatorics stops being forced.
- **No structural reason is known.** There is no invariant, no positivity statement, no degeneration argument that *explains* why the pure power should be the only solution. Gauss–Lucas confines the roots of derivatives to the convex hull of the roots of $f$, but the hull constraint is far too weak: it permits abundant configurations satisfying all $n-1$ incidences numerically.
- **Overdetermination is illusory.** $n-1$ equations in $n-1$ unknowns is the *expected* count, so no dimension count forbids extra zero-dimensional components; one must rule them out one prime, or one degree, at a time.
- **Numerics do not certify.** Homotopy-continuation searches over $\mathcal{C}_n$ find only the origin, but a near-solution cannot be distinguished from a genuine one without exact certification, and the origin's high multiplicity destroys conditioning.

## 6. The Gap

Proven: $\mathcal{C}_n=\{0\}$ for $n \in \{p^k,2p^k,3p^k,4p^k\}$, plus the real-rooted and few-distinct-root subcases in general degree. Conjectured: $\mathcal{C}_n=\{0\}$ for all $n$.

The gap is arithmetic, not analytic. Every known proof factors through a prime $p$ with $v_p(n)$ large enough that reducing a would-be counterexample mod $p$ forces $f^{(i)} \equiv 0$ for a controlled set of $i$, producing a contradiction with the binomial coefficients $\binom{n}{i} \bmod p$ (Lucas' theorem on base-$p$ digits). When $n$ has at least three distinct prime factors and no large prime-power part — $n = 30$ being minimal — no single prime dominates, each reduction leaves too many derivatives alive, and the argument produces no contradiction. **Crossing the gap means either (a) a mod-$p$ argument that combines several primes simultaneously rather than choosing one, or (b) a characteristic-$0$ mechanism (transcendental, tropical, or geometric) that has no mod-$p$ shadow at all** — necessarily so, since the statement is false mod $p$.

## 7. Current Research (as of June 2026)

- **Multi-prime reductions.** Attempts to run the Graf von Bothmer et al. degeneration at two primes at once, tracking the Newton polygon of a counterexample in the $p$-adic and $q$-adic valuations simultaneously. This is the most direct route to degree $30$. *(frontier — verify)*
- **Tropical / valuation-theoretic methods.** Encoding the $n-1$ incidence conditions as tropical intersection data on the weighted cone $\mathcal{C}_n$, hoping stable intersection forces the origin. *(frontier — verify)*
- **Analytic estimates on root configurations.** Refinements of the Ounaïes-style approach: quantitative bounds showing that a root of $f^{(i)}$ close to a root of $f$ for all $i$ forces the roots of $f$ into a shrinking cluster. Complete for large $i$, still open for the middle range $i \approx n/2$.
- **Certified computation.** Extending exact verification past degree $12$ using symmetric-function coordinates (power sums instead of coefficients) and modular Gröbner bases; the practical wall is around degree $14$–$16$. *(frontier — verify)*
- **Groups.** Work has been carried out at KU Leuven and Ghent (Castryck), Strasbourg (Ounaïes, Laterveer), RICAM/Linz (Schicho), Eindhoven (Draisma), and Barcelona (Casas-Alvero's school), with the singularity-theory framing kept alive on the geometry side.

## 8. Future Work

- **Settle degree $30$** by any means. It is the single most informative data point: it is the first degree where the digit-combinatorics mechanism provably has nothing to say.
- **Find the "reason".** Several authors have argued that a proof must come with a conceptual statement — a functional inequality, or an interpretation of the incidence conditions as maximal contact for a plane curve germ, so that the conclusion follows from equisingularity theory rather than elimination.
- **Classify the characteristic-$p$ counterexamples completely.** A full description of Casas-Alvero polynomials over $\overline{\mathbb{F}}_p$ would show precisely which char-$0$ arguments cannot exist, and may isolate the one that can.
- **Weakened variants.** Ask only $\gcd(f,f^{(i)})\ne 1$ for $i$ in a subset $S \subseteq \{1,\dots,n-1\}$, and determine the minimal $S$ forcing $f=(x-a)^n$. Results here would locate which of the $n-1$ conditions are doing the work.
- **Scheme structure.** Compute the multiplicity of $\mathcal{C}_n$ at the origin as a function of $n$; if it equals $\deg \mathcal{C}_n = \prod_{i=1}^{n-1}\deg R_i$ (suitably weighted) by Bézout, the conjecture follows for that $n$ immediately.

## 9. Key References

- **[Foundational]** Eduardo Casas-Alvero. *Higher order polar germs.* Journal of Algebra **240** (2001), 326–337.
- **[Foundational / SOTA]** Hans-Christian Graf von Bothmer, Oliver Labs, Josef Schicho, Christiaan van de Woestijne. *The Casas-Alvero conjecture for infinitely many degrees.* Journal of Algebra **316** (2007), 224–230.
- **[SOTA / Recent]** Wouter Castryck, Robert Laterveer, Myriam Ounaïes. *Constraints on counterexamples to the Casas-Alvero conjecture and a verification in degree 12.* Mathematics of Computation **83** (2014), 3017–3037.
- **[Survey]** Jan Draisma, Johan P. de Jong. *On the Casas-Alvero conjecture.* European Mathematical Society Newsletter **80** (2011), 29–33.
- **[Background]** Eduardo Casas-Alvero. *Singularities of Plane Curves.* London Mathematical Society Lecture Note Series 276, Cambridge University Press, 2000.
- **[Background]** Morris Marden. *Geometry of Polynomials.* Mathematical Surveys No. 3, American Mathematical Society, 2nd ed., 1966. (Gauss–Lucas and root-derivative geometry.)

## 10. Worked Example / Concrete Special Case

**(a) The conjecture in degree $3$, proved.** Let $f$ be monic cubic. Translate so the roots sum to $0$:
$$f(x) = x^3 + px + q, \qquad f'(x) = 3x^2 + p, \qquad f''(x) = 6x .$$
The condition for $i=2$: $f''$ has the single root $0$, so $f(0)=0$, i.e. $q = 0$. Hence
$$f(x) = x^3 + px = x\,(x^2+p).$$
The condition for $i=1$: some root $r$ of $f$ satisfies $3r^2 + p = 0$.
- If $r = 0$: then $p = 0$.
- If $r \ne 0$: then $r^2 = -p$ from $f(r)=0$, and substituting into $3r^2+p=0$ gives $-3p + p = -2p = 0$, so $p=0$.

Either way $p = q = 0$ and $f(x) = x^3$, i.e. $(x-a)^3$ before the translation. $\square$

Note where characteristic $0$ entered: the step $-2p = 0 \Rightarrow p = 0$ fails in characteristic $2$, and $f''=6x$ is identically zero in characteristic $2$ and $3$.

**(b) Failure in characteristic $p$.** Let $p$ be an odd prime and work over $\mathbb{F}_p$ with $n = p+1$:
$$f(x) = x^{p+1} + x .$$
Then $f'(x) = (p+1)x^p + 1 = x^p + 1 = (x+1)^p$ in $\mathbb{F}_p[x]$, whose only root is $x = -1$; and
$$f(-1) = (-1)^{p+1} + (-1) = 1 - 1 = 0 ,$$
so $f$ and $f'$ share the root $-1$. For $i \ge 2$, $f^{(i)} \equiv 0$ because $f'' = (p+1)p\,x^{p-1} = 0$ — and the zero polynomial vacuously shares a root with $f$. So all $n-1 = p$ conditions hold. But
$$f(x) = x\,(x^p+1) = x\,(x+1)^p$$
has two distinct roots and is not $(x-a)^{p+1}$.

Concretely at $p=3$, $n=4$: $f = x^4 + x = x(x+1)^3$ over $\mathbb{F}_3$, with $f' = x^3+1$, $f''=f'''=0$.

This is the exact obstruction described in Sections 5–6: the char-$p$ statement is false, so no proof can be uniform in the characteristic, and every known char-$0$ proof must first show that the derivatives *cannot* collapse mod $p$ — which the base-$p$ digits of $n$ guarantee only for $n = p^k, 2p^k, 3p^k, 4p^k$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*