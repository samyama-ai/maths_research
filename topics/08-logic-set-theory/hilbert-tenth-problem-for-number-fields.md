---
id: 08-logic-set-theory/hilbert-tenth-problem-for-number-fields
title: "Hilbert Tenth Problem for Number Fields"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hilbert's Tenth Problem for Number Fields

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/hilbert-tenth-problem-for-number-fields` · **Status:** open

## 1. Problem Statement / Conjecture

Hilbert's tenth problem (H10) over a commutative ring $R$ asks: is there an algorithm that, given a polynomial $f \in R[x_1,\dots,x_n]$ (for rings with a fixed finite presentation of elements), decides whether $f(x_1,\dots,x_n) = 0$ has a solution in $R^n$?

Matiyasevich (1970), completing Davis–Putnam–Robinson, proved the answer is **no** for $R = \mathbb{Z}$.

Two number-theoretic generalizations:

- **(A) Rings of integers.** For a number field $K$ with ring of integers $\mathcal{O}_K$, is H10 over $\mathcal{O}_K$ undecidable? **Resolved affirmatively in 2024–2025** by two independent proofs (Koymans–Pagano; Alpöge–Bhargava–Ho–Shnidman).
- **(B) Number fields themselves.** Is H10 over $K$ undecidable — in particular over $K = \mathbb{Q}$? **Open.** This is the headline open case and the reason this entry is marked `open`.

A resolution of (B) in the negative direction requires an actual decision procedure; a resolution in the positive direction requires exhibiting, for each number field $K$, a Diophantine model of $\mathbb{Z}$ over $K$ — or any other reduction of a known undecidable problem to solvability of polynomial equations over $K$. The near-universal expectation is undecidability.

## 2. Mathematical Foundations

Let $K$ be a number field of degree $d = [K:\mathbb{Q}]$, $\mathcal{O}_K$ its ring of integers, $M_K$ its set of places.

**Diophantine sets.** $A \subseteq R^m$ is *Diophantine over $R$* if there is $f \in R[t_1,\dots,t_m,x_1,\dots,x_n]$ with
$$A = \{\,\bar t \in R^m : \exists \bar x \in R^n,\ f(\bar t,\bar x) = 0\,\}.$$
Diophantine sets are closed under finite unions ($fg=0$) and intersections (over integral domains of characteristic $0$: $f^2+g^2=0$), but *not* known to be closed under complement.

**DPRM theorem.** Over $\mathbb{Z}$, a set is Diophantine iff it is recursively enumerable. Hence a Diophantine set with undecidable membership exists, and H10$/\mathbb{Z}$ is undecidable.

**Diophantine model / interpretation.** A *Diophantine model* of $\mathbb{Z}$ over $R$ is a Diophantine set $S \subseteq R^k$ and a bijection $\phi: \mathbb{Z} \to S$ whose graphs of addition and multiplication,
$$\{(\phi(a),\phi(b),\phi(a+b))\}, \quad \{(\phi(a),\phi(b),\phi(ab))\} \subseteq R^{3k},$$
are Diophantine over $R$. Such a model forces H10$/R$ undecidable, by DPRM.

**Key sufficient condition (integrality).** If $\mathbb{Z}$ is a Diophantine subset of $\mathcal{O}_K$, then H10$/\mathcal{O}_K$ is undecidable. For fields, the analogous target is: **$\mathcal{O}_K$ (or $\mathbb{Z}$) is Diophantine over $K$.**

**Norm and Pell equations.** For $K = \mathbb{Q}(\sqrt{d})$, $d>1$ squarefree, the unit group $\mathcal{O}_K^\times$ has rank $1$ (Dirichlet), and solutions of
$$x^2 - dy^2 = 1$$
form $\{\pm(x_1+y_1\sqrt d)^n\}$. Writing $x_n + y_n\sqrt d = (x_1+y_1\sqrt d)^n$ gives the divisibility and congruence relations
$$y_m \mid y_n \iff m \mid n, \qquad y_n \equiv n\,y_1 \pmod{x_1 - 1},$$
which is the engine converting an exponential recursion into polynomial conditions.

**Elliptic-curve method.** Let $E/K$ be an elliptic curve with $\operatorname{rank} E(K) = 1$ and generator $P$. The set $\{nP : n\in\mathbb{Z}\}$, together with the group law (a rational map, hence Diophantine) and a Diophantine encoding of $n \mapsto x(nP)$, yields a Diophantine model of $(\mathbb{Z},+,\times)$; the multiplication graph comes from divisibility relations among division polynomials, using
$$m \mid n \iff \text{(denominator ideal of } x(mP)) \mid \text{(denominator ideal of } x(nP)).$$
This is Poonen's construction (2002) and its rank-stability refinements.

**Mazur's conjecture (obstruction for fields).** Mazur conjectured that for a variety $X/\mathbb{Q}$, the topological closure $\overline{X(\mathbb{Q})}$ in $X(\mathbb{R})$ has at most finitely many connected components. If true, $\mathbb{Z}$ is **not** Diophantine over $\mathbb{Q}$ (since $\mathbb{Z} \subset \mathbb{R}$ is closed and infinitely disconnected), so the direct route to (B) fails.

## 3. History & State of the Art (SOTA)

- **1900.** Hilbert poses the tenth problem in his Paris list, over $\mathbb{Z}$.
- **1949–1961.** Davis's normal form; Davis–Putnam–Robinson reduce to exponential Diophantine equations (*Ann. of Math.* 74, 1961).
- **1970.** Matiyasevich supplies the missing Fibonacci-growth relation; H10$/\mathbb{Z}$ undecidable.
- **1975–1980.** Denef settles rings of integers of real quadratic fields, then all totally real fields and their quadratic extensions, using Pell equations.
- **1978.** Denef–Lipshitz handle abelian extensions of $\mathbb{Q}$ and further families.
- **1988–1989.** Pheidas and Shlapentokh independently extend to fields with exactly one pair of complex conjugate embeddings, subject to a rank/root-of-unity condition.
- **2002–2008.** Poonen introduces the rank-one elliptic curve method; Cornelissen–Pheidas–Zahidi ("division-ample sets") and Shlapentokh give clean criteria: if there is $E/\mathbb{Q}$ with $\operatorname{rank} E(\mathbb{Q}) = \operatorname{rank} E(K) = 1$, then H10$/\mathcal{O}_K$ is undecidable.
- **2010.** Mazur–Rubin prove (A) for all $K$ **conditionally** on finiteness of $Ш(E/K)[2^\infty]$, via rank-preserving quadratic twists.
- **2018.** Murty–Pasten derive (A) from the full BSD conjecture for elliptic curves over $\mathbb{Q}$.
- **2024–2025.** (A) is proved unconditionally, twice. Koymans–Pagano (arXiv:2412.01768) use additive combinatorics with $2$-Selmer/Rédei-symbol control to build, for any $K/\mathbb{Q}$, an elliptic curve of rank $1$ over $\mathbb{Q}$ keeping rank $1$ over $K$. Alpöge–Bhargava–Ho–Shnidman (arXiv:2501.18774) use geometry-of-numbers averages over $2$-Selmer groups of quadratic twists to obtain rank stability in quadratic extensions, then induct on the tower.
- **Field case (B).** Still open for every number field, $\mathbb{Q}$ included.

## 4. Partial Results / Verified Cases

Undecidability of H10 is **proved** for:

- $\mathcal{O}_K$, **all** number fields $K$ (2024–2025, unconditional; both proofs are elliptic-curve-rank arguments).
- Historically explicit families, by elementary methods: $K$ totally real of any degree; degree-$2$ extensions of totally real fields (Denef 1980); abelian $K/\mathbb{Q}$ (Denef–Lipshitz 1978); $K$ with exactly one conjugate pair of non-real embeddings, e.g. all cubic fields with negative discriminant such as $\mathbb{Q}(\sqrt[3]{2})$ (Pheidas 1988, Shlapentokh 1989); any $K$ admitting $E/\mathbb{Q}$ with $\operatorname{rank}E(\mathbb{Q})=\operatorname{rank}E(K)=1$ — e.g. $K=\mathbb{Q}(i)$ with $E: y^2 = x^3 - 2$ (rank $1$ over both).
- Large subrings of $\mathbb{Q}$: Poonen (2003) constructs subrings $R\subseteq\mathbb{Q}$ obtained by inverting a set of primes of natural density $1$ (complement of density $0$) with H10$/R$ undecidable; Poonen–Shlapentokh extend this to number fields.
- Rings of $S$-integers $\mathcal{O}_{K,S}$ for finite $S$ (follows from the $\mathcal{O}_K$ case plus standard reductions).
- Function fields: $\mathbb{F}_q(t)$ and finite extensions (Pheidas, Videla, Shlapentokh, Eisenträger), and $\mathbb{C}(t_1,t_2)$, $\mathbb{R}(t)$ — undecidable.

**Definability results relevant to (B).** $\mathcal{O}_K$ is first-order definable in $K$ (Rumely, Robinson). Poonen (2009) gives a $\forall\exists$ formula with $2$ universal and $7$ existential quantifiers defining $\mathbb{Z}$ in $\mathbb{Q}$; Koenigsmann (2016) gives a **universal** ($\forall$-only) definition of $\mathbb{Z}$ in $\mathbb{Q}$ with $418$ variables, so $\mathbb{Q}\setminus\mathbb{Z}$ is Diophantine; Park (2013) extends this to all number fields. Consequence: $\mathbb{Q}$ is **not** Diophantine over $\mathbb{Z}$ unless surprising collapses occur, and the complement direction is settled — but the direction needed for (B) is not.

## 5. Principal Obstacles

- **Mazur's conjecture blocks the natural route.** Every known undecidability proof produces a Diophantine model of $\mathbb{Z}$. Over $\mathbb{Q}$ this is expected to be impossible: Mazur's topological conjecture, and its refinements by Cornelissen–Zahidi, imply no Diophantine set of $\mathbb{Q}^n$ can be a model of $\mathbb{Z}$ in the "closed and discrete" sense used so far. Any proof of (B) must be a genuinely different construction.
- **Archimedean topology has no arithmetic counterweight.** Over $\mathcal{O}_K$, integrality at all archimedean places gives a Pell/units handle; over $K$ the group $K^\times$ is far too large and the real topology of $X(\mathbb{Q})$ is uncontrolled.
- **No local-global input is available.** Existence of rational points on a variety is itself not known to be decidable — even for smooth cubic surfaces or genus-$1$ curves. Deciding H10$/\mathbb{Q}$ for degree-$3$, $n=4$ instances would already require effective knowledge of Brauer–Manin obstructions and finiteness of $Ш$.
- **Elliptic-curve methods saturate at rank $1$.** The 2024–25 rank-stability arguments give a rank-$1$ curve over $K$, exactly what the $\mathcal{O}_K$ model needs. Over $K$ (a field) the $n$-torsion/denominator trick disappears because there is no divisibility of ideals to read $m\mid n$ from — every element is a unit up to scaling.
- **Complement-closure failure.** Diophantine sets are not closed under negation, so one cannot bootstrap from Koenigsmann's universal definition of $\mathbb{Z}$ in $\mathbb{Q}$ to an existential one.

## 6. The Gap

Proved: for all $K$, H10$/\mathcal{O}_K$ is undecidable, via a Diophantine model of $\mathbb{Z}$ inside $\mathcal{O}_K$ built from a rank-$1$ elliptic curve.

Wanted: undecidability of H10$/K$. The single missing step is:

> Produce a Diophantine (existential-only, positive) definition over $K$ of a set on which a copy of $(\mathbb{Z},+,\times)$ can be interpreted — for instance show $\mathcal{O}_K$, or the set of elements integral at one fixed prime, is Diophantine over $K$.

Equivalently: convert the known **universal** definition of $\mathbb{Z}$ in $\mathbb{Q}$ into an **existential** one, or bypass models entirely. Mazur's conjecture predicts that the direct conversion is impossible, so the gap is not quantitative but structural: the field of interpretation must change (e.g. to an anabelian, model-theoretic, or non-archimedean encoding).

## 7. Current Research (as of June 2026)

- **Consolidation of the 2024–25 proofs.** Koymans (Utrecht/Bonn) and Pagano (Leiden) continue with Rédei-symbol and additive-combinatorial control of $2$-Selmer groups in towers; Alpöge, Bhargava, Ho, Shnidman (Princeton/IAS, Hebrew University) develop rank-stability statements for higher-degree extensions. Both preprint lines are in refereeing/journal pipelines *(frontier — verify current publication status)*.
- **Mazur's conjecture as a hard target.** Work relating $\overline{X(\mathbb{Q})}$ to Brauer–Manin and to the section conjecture (Stoll, Poonen, Cornelissen–Zahidi). Any counterexample to Mazur's conjecture would immediately reopen the direct route to H10$/\mathbb{Q}$.
- **Quantifier economy over $\mathbb{Q}$.** Following Koenigsmann and Park, reduction of variable counts and quantifier alternations in definitions of $\mathbb{Z}$ in $K$; Daans (2021, 2023) improved universal definitions using quaternion-algebra and valuation-theoretic techniques.
- **Decidability side.** No serious programme claims decidability of H10$/\mathbb{Q}$, but there is work on decidable fragments: bounded degree/variables, and the still-open decidability of H10 over $\mathbb{Q}$ restricted to $n\le 2$ variables or degree $\le 2$ (the quadratic case is decidable by Hasse–Minkowski).
- **Adjacent open rings.** H10 over $\mathbb{C}(t_1)$ (open), $\mathbb{R}$-analogues, and $\mathbb{Z}$-analogues in $p$-adic settings; Eisenträger, Shlapentokh, Pasten and Miller (CUNY) work on Turing-degree and computability-theoretic refinements (e.g. HTP$(\mathbb{Q})$'s degree relative to HTP$(\mathbb{Z})$).

## 8. Future Work

- **Non-model routes.** Find a reduction from a known undecidable problem to H10$/K$ that does not pass through a Diophantine copy of $\mathbb{Z}$ — for example encoding halting into the existence of rational points on a family of surfaces, using functorial or anabelian data rather than a discrete model.
- **Prove Mazur's conjecture**, at least for curves and abelian varieties, to make the obstruction precise and formally rule out the standard approach; conversely, test it computationally on families of surfaces with dense but topologically wild rational point sets.
- **Existentialize valuations.** Show that "$v_\mathfrak{p}(x)\ge 0$" is Diophantine over $K$ for some prime $\mathfrak{p}$ — this alone yields (B). Current quaternion-algebra methods give universal, not existential, definitions.
- **Density subrings as a bridge.** Poonen's density-$1$ subrings of $\mathbb{Q}$ come arbitrarily close to $\mathbb{Q}$; push to density-$1$ sets with prescribed structure, or to inverse limits, to see whether undecidability survives the limit.
- **Computability-theoretic separation.** Determine whether HTP$(\mathbb{Q})$ is Turing-equivalent to the halting problem, or strictly below it — the latter would be the first genuine evidence toward decidability.

## 9. Key References

- **[Foundational]** M. Davis, H. Putnam, J. Robinson. *The decision problem for exponential diophantine equations.* Annals of Mathematics 74 (1961), 425–436.
- **[Foundational]** Yu. Matiyasevich. *Enumerable sets are Diophantine.* Doklady Akademii Nauk SSSR 191 (1970), 279–282.
- **[Foundational]** J. Denef. *Hilbert's tenth problem for quadratic rings.* Proceedings of the AMS 48 (1975), 214–220.
- **[Foundational]** J. Denef. *Diophantine sets over algebraic integer rings II.* Transactions of the AMS 257 (1980), 227–236.
- **[Foundational]** J. Denef, L. Lipshitz. *Diophantine sets over some rings of algebraic integers.* Journal of the London Mathematical Society 18 (1978), 385–391.
- T. Pheidas. *Hilbert's tenth problem for a class of rings of algebraic integers.* Proceedings of the AMS 104 (1988), 611–620.
- A. Shlapentokh. *Extension of Hilbert's tenth problem to some algebraic number fields.* Communications on Pure and Applied Mathematics 42 (1989), 939–962.
- B. Poonen. *Using elliptic curves of rank one towards the undecidability of Hilbert's tenth problem over rings of algebraic integers.* Algorithmic Number Theory (ANTS-V), LNCS 2369, Springer, 2002, 33–42.
- B. Poonen. *Hilbert's tenth problem and Mazur's conjecture for large subrings of $\mathbb{Q}$.* Journal of the AMS 16 (2003), 981–990.
- G. Cornelissen, T. Pheidas, K. Zahidi. *Division-ample sets and the Diophantine problem for rings of integers.* Journal de Théorie des Nombres de Bordeaux 17 (2005), 727–735.
- **[SOTA]** B. Mazur, K. Rubin. *Ranks of twists of elliptic curves and Hilbert's tenth problem.* Compositio Mathematica 146 (2010), 1–33.
- M. R. Murty, H. Pasten. *Elliptic curves, L-functions, and Hilbert's tenth problem.* Journal of Number Theory 182 (2018), 1–18.
- B. Poonen. *Characterizing integers among rational numbers with a universal-existential formula.* American Journal of Mathematics 131 (2009), 675–682.
- J. Koenigsmann. *Defining $\mathbb{Z}$ in $\mathbb{Q}$.* Annals of Mathematics 183 (2016), 73–93.
- J. Park. *A universal first-order formula defining the ring of integers in a number field.* Mathematical Research Letters 20 (2013), 961–980.
- **[SOTA / Recent]** P. Koymans, C. Pagano. *Hilbert's tenth problem via additive combinatorics.* arXiv:2412.01768, 2024.
- **[SOTA / Recent]** L. Alpöge, M. Bhargava, W. Ho, A. Shnidman. *Rank stability in quadratic extensions and Hilbert's tenth problem for the ring of integers of a number field.* arXiv:2501.18774, 2025.
- **[Survey]** A. Shlapentokh. *Hilbert's Tenth Problem: Diophantine Classes and Extensions to Global Fields.* Cambridge University Press, 2007.
- **[Survey]** B. Poonen. *Undecidability in number theory.* Notices of the AMS 55 (2008), 344–350.
- **[Survey]** B. Mazur. *The topology of rational points.* Experimental Mathematics 1 (1992), 35–45.
- **[Survey]** Yu. Matiyasevich. *Hilbert's Tenth Problem.* MIT Press, 1993.

## 10. Worked Example / Concrete Special Case

**Goal:** show $\mathbb{Z}$ is Diophantine in $\mathcal{O}_K$ for $K=\mathbb{Q}(\sqrt{2})$, so H10$/\mathbb{Z}[\sqrt 2]$ is undecidable (Denef 1975, real quadratic case).

Here $\mathcal{O}_K = \mathbb{Z}[\sqrt 2]$ and the fundamental unit is $\varepsilon = 1+\sqrt 2$, with $N(\varepsilon)=-1$; so $\varepsilon^2 = 3+2\sqrt 2$ generates the solutions of the Pell equation
$$x^2 - 2y^2 = 1, \qquad x_n + y_n\sqrt 2 = (3+2\sqrt2)^n .$$
First values:

| $n$ | $x_n$ | $y_n$ |
|---|---|---|
| 1 | 3 | 2 |
| 2 | 17 | 12 |
| 3 | 99 | 70 |
| 4 | 577 | 408 |

**Step 1 — the solution set is Diophantine.** $P=\{(x,y)\in\mathcal{O}_K^2 : x^2-2y^2=1\}$ is defined by one equation. Restricting to $\mathbb{Z}$-solutions is the point of Step 3.

**Step 2 — divisibility mirrors the index.** From $x_{m+n}=x_mx_n+2y_my_n$ and $y_{m+n}=x_my_n+y_mx_n$ one gets $y_n \equiv n y_1 x_1^{\,n-1} \pmod{y_1^{2}}$ and
$$y_m \mid y_n \iff m \mid n .$$
Check: $y_2=12$, $y_4=408=34\cdot 12$ ✓; $y_2 \nmid y_3=70$ ✓.

**Step 3 — congruence extracts the index linearly.** Reducing $(x_1+y_1\sqrt2)^n$ modulo $x_1-1$ gives
$$y_n \equiv n\,y_1 \pmod{x_1-1}.$$
For the branch generated by $x_1=3,y_1=2$: $x_1-1=2$, and indeed $y_n \equiv 2n \equiv 0 \pmod 2$. Taking instead a higher power as base, say $x_1' = x_N$, $y_1'=y_N$ with $N$ large, makes $x_1'-1$ exceed any prescribed bound, so $n$ is recovered *exactly* (not just mod something) from the pair $(y_n \bmod (x_1'-1),\ n < x_1'-1)$.

**Step 4 — assemble.** Steps 2–3 make the graph of exponentiation $\{(a,b,c) : c = a^b\}$ Diophantine over $\mathcal{O}_K$: the relation "$c$ is the $b$-th term of the Pell sequence based at $a$" is cut out by finitely many polynomial equations in $\mathcal{O}_K$, plus auxiliary Pell equations forcing the index. By Davis–Putnam–Robinson, every recursively enumerable set is exponential-Diophantine, hence Diophantine over $\mathcal{O}_K$.

**Step 5 — conclude.** Take a r.e. non-recursive $A\subseteq\mathbb{Z}$ and its defining polynomial $f_A$. Then $a\in A \iff \exists \bar x\in\mathcal{O}_K^n,\ f_A(a,\bar x)=0$, so an algorithm for H10$/\mathbb{Z}[\sqrt 2]$ would decide $A$. Contradiction. $\square$

**Why this does not transfer to the field $\mathbb{Q}(\sqrt2)$.** Steps 2–3 rely on $y_m \mid y_n$ — a divisibility relation among *integers*. In the field, every nonzero element is invertible, so $y_m \mid y_n$ holds always and carries no information. Recovering divisibility over $K$ requires singling out elements integral at a prime $\mathfrak{p}$, i.e. exactly the existential definition of a valuation ring that Section 6 identifies as the missing step.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*