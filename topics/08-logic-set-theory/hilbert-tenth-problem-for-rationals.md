---
id: 08-logic-set-theory/hilbert-tenth-problem-for-rationals
title: "Hilbert Tenth Problem for Rationals"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hilbert's Tenth Problem for the Rationals

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/hilbert-tenth-problem-for-rationals` · **Status:** open

## 1. Problem Statement / Conjecture

**Question.** Is there an algorithm that, given a polynomial $f \in \mathbb{Z}[x_1,\dots,x_n]$, decides whether
$$f(x_1,\dots,x_n) = 0$$
has a solution with all $x_i \in \mathbb{Q}$?

Equivalently: is the set
$$\mathrm{HTP}(\mathbb{Q}) \;=\; \{\, \ulcorner f \urcorner \;:\; f \in \mathbb{Z}[x_1,\dots,x_n],\ \exists\, \bar{x}\in\mathbb{Q}^n,\ f(\bar x)=0 \,\}$$
decidable? $\mathrm{HTP}(\mathbb{Q})$ is always computably enumerable (search over $\mathbb{Q}^n$), so the question is whether its complement is also c.e.

A resolution requires either (a) an explicit decision procedure with a correctness proof, or (b) a proof that $\mathrm{HTP}(\mathbb{Q})$ is undecidable — in practice, an existential (Diophantine) interpretation of $(\mathbb{Z},+,\times)$ inside $\mathbb{Q}$, which by the DPRM theorem forces undecidability. Both remain open. Neither direction is known even conditionally on a widely accepted arithmetic conjecture; the standing conjectures (Mazur's, below) point *against* the standard route to (b).

## 2. Mathematical Foundations

**Diophantine sets.** For a commutative ring $R$ with a fixed presentation, $S \subseteq R^m$ is *Diophantine over $R$* if there is $p \in \mathbb{Z}[t_1,\dots,t_m,y_1,\dots,y_k]$ with
$$S = \{\bar t \in R^m : \exists\, \bar y \in R^k,\ p(\bar t,\bar y)=0\}.$$
Over a field, finitely many equations reduce to one ($f_1=\dots=f_r=0 \iff \sum f_i^2=0$ over $\mathbb{Q}$, using formal reality), so "one equation" is no loss.

**DPRM theorem** (Davis–Putnam–Robinson 1961, Matiyasevich 1970): over $\mathbb{Z}$, Diophantine $=$ computably enumerable. Hence $\mathrm{HTP}(\mathbb{Z})$ is undecidable.

**Transfer principle.** If $\mathbb{Z}$ is Diophantine in $\mathbb{Q}$ — i.e. $\mathbb{Z} = \{t \in \mathbb{Q} : \exists \bar y \in \mathbb{Q}^k,\ p(t,\bar y)=0\}$ — then any Diophantine subset of $\mathbb{Z}^n$ is Diophantine over $\mathbb{Q}$ (substitute the definition for each variable), so $\mathrm{HTP}(\mathbb{Q})$ is undecidable. More weakly, a *Diophantine model* of $(\mathbb{Z},+,\times)$ — a Diophantine set $A\subseteq \mathbb{Q}^m$ with a Diophantine bijection $\mathbb{Z}\to A$ carrying $+$ and $\times$ to Diophantine relations — suffices.

**Local–global input.** The workhorse is Hasse–Minkowski: a quadratic form over $\mathbb{Q}$ is isotropic iff it is isotropic over $\mathbb{R}$ and every $\mathbb{Q}_p$. Encoded by the Hilbert symbol $(a,b)_v \in \{\pm 1\}$ with the product formula $\prod_v (a,b)_v = 1$. For $a,b\in\mathbb{Q}^\times$ the quaternion algebra $H_{a,b}$ has reduced-norm set
$$N_{a,b} = \{\,z_1^2 - a z_2^2 - b z_3^2 + ab\, z_4^2 \;:\; z_i \in \mathbb{Q}\,\},$$
manifestly Diophantine; conditions on $N_{a,b}$ translate into congruence and valuation conditions at ramified places. This is the source of every known definition of $\mathbb{Z}$ in $\mathbb{Q}$.

**Mazur's conjecture** (1992): for a variety $X/\mathbb{Q}$, the closure of $X(\mathbb{Q})$ in $X(\mathbb{R})$ (real topology) has finitely many connected components. Consequence: no infinite discrete subset of $\mathbb{R}$, in particular $\mathbb{Z}$, is the projection of the rational points of a variety — so $\mathbb{Z}$ is **not** Diophantine in $\mathbb{Q}$.

## 3. History & State of the Art (SOTA)

- **1900.** Hilbert's tenth problem, stated for integer solutions.
- **1949.** Julia Robinson (*Definability and decision problems in arithmetic*, JSL) proves $\mathbb{Z}$ is **first-order** definable in $\mathbb{Q}$, using ternary quadratic forms and Hasse–Minkowski. Hence the full first-order theory of $\mathbb{Q}$ is undecidable — but her formula alternates quantifiers, so nothing follows for $\mathrm{HTP}(\mathbb{Q})$.
- **1970.** DPRM closes the integer case.
- **1980s–90s.** Denef, Denef–Lipshitz, Pheidas, Videla, Shlapentokh: $\mathrm{HTP}(\mathcal{O}_K)$ undecidable for totally real $K$, imaginary quadratic $K$, and abelian extensions; $\mathbb{Z}$ shown Diophantine in $\mathcal{O}_K$ for those classes.
- **2003.** Poonen: undecidability for "large" subrings of $\mathbb{Q}$ (Section 4).
- **2009.** Poonen (*J. AMS*): $\mathbb{Z}$ is definable in $\mathbb{Q}$ by a $\forall\exists$-formula with **2 universal and 7 existential** quantifiers.
- **2016.** Koenigsmann (*Annals of Math.*): $\mathbb{Q}\setminus\mathbb{Z}$ is **Diophantine** in $\mathbb{Q}$; equivalently $\mathbb{Z}$ is **universally** definable, with a $\forall$-formula in 418 variables.
- **2021.** Daans (*Documenta Math.*) gives a uniform method for universally defining finitely generated subrings of global fields, cutting the quantifier count for $\mathbb{Z}$ in $\mathbb{Q}$ by an order of magnitude.
- **2024–25.** Alpöge–Bhargava–Ho–Shnidman and, independently, Koymans–Pagano prove $\mathrm{HTP}(\mathcal{O}_K)$ undecidable for **every** number field $K$, unconditionally — closing the ring-of-integers case *(frontier — verify final published versions)*. The rational case is untouched by these methods.

## 4. Partial Results / Verified Cases

- **Rings of integers.** $\mathrm{HTP}(\mathcal{O}_K)$ is undecidable for all number fields $K$ (2024–25 preprints above); previously known for totally real fields and their degree-2 extensions (Denef, Denef–Lipshitz), imaginary quadratic fields (Pheidas), fields with an elliptic curve of rank 1 (Poonen, Shlapentokh), and — conditional on finiteness of $Ш$ — all $K$ (Mazur–Rubin 2010; Murty–Pasten 2018 under finiteness of $Ш$ for elliptic curves over $\mathbb{Q}$).
- **Large subrings of $\mathbb{Q}$.** Poonen (2003): for any set $S$ of primes of natural density $1$ (indeed, complement of density $0$), $\mathrm{HTP}(\mathbb{Z}[S^{-1}])$ is undecidable, and Mazur's conjecture fails for such rings. Eisenträger–Everest and Eisenträger–Morrison extend this to large subrings of number fields.
- **Turing-equivalence family.** Eisenträger–Miller–Park–Shlapentokh (*Trans. AMS*, 2017): there are uncountably many subrings $R \subseteq \mathbb{Q}$ (of any prescribed "size") with $\mathrm{HTP}(R) \equiv_T \mathrm{HTP}(\mathbb{Q})$ — so the rational case is not an isolated point.
- **Function-field analogue solved.** $\mathrm{HTP}$ is undecidable for $\mathbb{F}_q(t)$ (Pheidas, char $\neq 2$; Videla, Shlapentokh, Eisenträger in char $2$) and for function fields of curves over various base fields.
- **Decidable neighbours.** $\mathbb{R}$ (Tarski), $\mathbb{C}$, all $\mathbb{Q}_p$ (Ax–Kochen/Ershov, Denef for the existential theory), and $\overline{\mathbb{Q}}$ have decidable existential theories. $\mathbb{Q}$ sits precisely at the local–global junction of these decidable completions.
- **Definability strength over $\mathbb{Q}$ itself.** $\mathbb{Z}$ is $\forall$-definable (Koenigsmann); $\mathbb{Z}_{(p)}$, the set of non-squares, and $\mathbb{Q}\setminus\mathbb{Z}$ are Diophantine.

## 5. Principal Obstacles

- **The quantifier is one-sided.** Every known handle on $\mathbb{Z}$ inside $\mathbb{Q}$ is *universal*: the norm-form machinery naturally expresses "for all $(a,b)$, $x$ is a norm from $H_{a,b}$", i.e. a valuation-parity condition at *all* places at once. Converting $\forall$ to $\exists$ would require witnessing the infinitely many local conditions by finitely many rational parameters, and no mechanism for that is known.
- **Archimedean topology blocks the standard route.** $\mathbb{Z}$ is discrete and infinite in $\mathbb{R}$. Mazur's conjecture says Diophantine sets over $\mathbb{Q}$ cannot look like that. Cornelissen–Zahidi showed Mazur's conjecture also rules out Diophantine *models* of $\mathbb{Z}$ in $\mathbb{Q}$ built from varieties in the natural way. So the community's best-supported conjecture predicts the standard undecidability route fails.
- **Elliptic-curve methods need a rank-1 anchor that $\mathbb{Q}$ lacks.** The Poonen–Shlapentokh–Mazur–Rubin technique defines $\mathbb{Z}$ in $\mathcal{O}_K$ using an elliptic curve whose rank does not grow in a chosen extension; over $\mathbb{Q}$ there is no ambient extension to exploit, and $E(\mathbb{Q})\cong\mathbb{Z}$ is dense in a real component, not discrete, so the divisibility-sequence trick that works in $\mathcal{O}_K$ has no rational analogue.
- **No decision procedure in sight either.** Quantifier elimination fails: the existential theory of $\mathbb{Q}$ is not model-complete in any usable sense, and $\mathbb{Q}$ has no Ax–Kochen-style completeness because it is not henselian. Local solvability is decidable place-by-place, but the Hasse principle fails for general varieties (Selmer's $3x^3+4y^3+5z^3=0$), and the Brauer–Manin obstruction — the only systematic global obstruction — is itself not known to be computable or complete.

## 6. The Gap

Proven: $\mathbb{Z}$ is definable in $\mathbb{Q}$ with quantifier complexity $\forall$ (418 variables, Koenigsmann; fewer after Daans), and $\forall\exists$ with $(2,7)$ variables (Poonen). Needed for undecidability: complexity $\exists$, i.e. a single polynomial $p(t,\bar y)$ with $\mathbb{Z}=\{t:\exists\bar y\, p=0\}$, or a Diophantine model. The gap is exactly **one quantifier alternation**, but it is not a technical gap: it is the boundary at which the real topology enters. A purely existential definition would produce an infinite discrete Diophantine subset of $\mathbb{Q}$, refuting Mazur's conjecture. Conversely, a proof of decidability would need a global effective local–global theorem for arbitrary varieties, far beyond current arithmetic geometry. The problem is therefore genuinely two-sided: no one knows which answer to expect.

## 7. Current Research (as of June 2026)

- **Quantifier economy.** Daans, Dittmann, and collaborators pursue uniform universal definitions of rings of integers in global fields with minimal variable counts, and study which subsets of $\mathbb{Q}$ are Diophantine (e.g. sets defined by prescribed local conditions). *(frontier — verify current record for the number of universal quantifiers.)*
- **Rank statistics.** The 2024–25 unconditional resolution of $\mathrm{HTP}(\mathcal{O}_K)$ — Alpöge–Bhargava–Ho–Shnidman via rank stability in quadratic twists, Koymans–Pagano via additive combinatorics on $2^\infty$-Selmer groups — has revived attempts to import rank-theoretic input into the rational case. Consensus so far: these techniques control ranks in *extensions*, and have no direct rational analogue. *(frontier — verify.)*
- **Computability-theoretic degree of $\mathrm{HTP}(\mathbb{Q})$.** Eisenträger, Miller, Park, Shlapentokh and Miller's school study $\mathrm{HTP}(R)$ for subrings $R\subseteq\mathbb{Q}$ as a function of the set of inverted primes, asking whether $\mathrm{HTP}(\mathbb{Q}) \equiv_T \mathrm{HTP}(\mathbb{Z})$, i.e. whether the rational problem is exactly as hard as the integer one. Miller has shown the map $S\mapsto \mathrm{HTP}(\mathbb{Z}[S^{-1}])$ behaves measure-theoretically well.
- **Anti-undecidability evidence.** Work on the Brauer–Manin obstruction (Poonen, Colliot-Thélène, Skorobogatov) and on Mazur's conjecture for specific families continues; Poonen's counterexamples show the obstruction is not always sufficient, keeping the decidability side open too.

## 8. Future Work

- Find a Diophantine definition of $\mathbb{Z}_{(p)}$-type data strong enough to pin down $\mathbb{Z}$ existentially, or prove a *barrier theorem*: e.g. that no existential formula in the norm-form family can define $\mathbb{Z}$.
- Settle Mazur's conjecture for a single nontrivial class (say, all curves of genus $\ge 1$ with prescribed Mordell–Weil rank); Poonen's counterexample for large subrings shows the conjecture is delicate and any proof must use $\mathbb{Z}$-specific input.
- Determine the Turing degree of $\mathrm{HTP}(\mathbb{Q})$ relative to $\mathrm{HTP}(\mathbb{Z})$ — a strictly weaker but possibly tractable target.
- Develop an effective theory of the Brauer–Manin obstruction for a restricted class (e.g. rational points on conic bundles) as a step toward a partial decision procedure.
- Import the additive-combinatorial rank machinery of Koymans–Pagano to families over $\mathbb{Q}$ itself, e.g. to produce Diophantine sets with controlled archimedean closure.

## 9. Key References

- **[Foundational]** Julia Robinson. *Definability and Decision Problems in Arithmetic.* Journal of Symbolic Logic 14 (1949), 98–114.
- **[Foundational]** Yuri Matiyasevich. *Hilbert's Tenth Problem.* MIT Press, 1993.
- **[Foundational]** Martin Davis. *Hilbert's Tenth Problem is Unsolvable.* American Mathematical Monthly 80 (1973), 233–269.
- **[SOTA]** Jochen Koenigsmann. *Defining $\mathbb{Z}$ in $\mathbb{Q}$.* Annals of Mathematics 183 (2016), 73–93.
- **[SOTA]** Bjorn Poonen. *Characterizing integers among rational numbers with a universal-existential formula.* American Journal of Mathematics 131 (2009), 675–682.
- **[SOTA]** Bjorn Poonen. *Hilbert's Tenth Problem and Mazur's Conjecture for large subrings of $\mathbb{Q}$.* Journal of the AMS 16 (2003), 981–990.
- **[SOTA]** Barry Mazur, Karl Rubin. *Ranks of twists of elliptic curves and Hilbert's tenth problem.* Compositio Mathematica 146 (2010), 487–517.
- **[SOTA]** Barry Mazur, Karl Rubin. *Diophantine stability* (with an appendix by Michael Larsen). American Journal of Mathematics 140 (2018), 571–616.
- **[SOTA]** Nicolas Daans. *Universally defining finitely generated subrings of global fields.* Documenta Mathematica 26 (2021), 1851–1869.
- **[SOTA]** Kirsten Eisenträger, Russell Miller, Jennifer Park, Alexandra Shlapentokh. *As easy as $\mathbb{Q}$: Hilbert's Tenth Problem for subrings of the rationals and number fields.* Transactions of the AMS 369 (2017), 8291–8315.
- **[Survey]** Bjorn Poonen. *Undecidability in number theory.* Notices of the AMS 55 (2008), 344–350.
- **[Survey]** Alexandra Shlapentokh. *Hilbert's Tenth Problem: Diophantine Classes and Extensions to Global Fields.* Cambridge University Press, 2007.
- **[Survey]** Jan Denef, Leonard Lipshitz, Thanases Pheidas, Jan Van Geel (eds.). *Hilbert's Tenth Problem: Relations with Arithmetic and Algebraic Geometry.* Contemporary Mathematics 270, AMS, 2000.
- **[Survey]** Barry Mazur. *The topology of rational points.* Experimental Mathematics 1 (1992), 35–45.
- **[Related]** Gunther Cornelissen, Karim Zahidi. *Topology of Diophantine sets: remarks on Mazur's conjectures.* In Contemporary Mathematics 270 (2000), 253–260.

## 10. Worked Example / Concrete Special Case

**How a Diophantine condition over $\mathbb{Q}$ "sees" a prime.** Take the simplest norm form, from $\mathbb{Q}(i)$:
$$D \;=\; \{\, x\in\mathbb{Q} \;:\; \exists\, y,z \in \mathbb{Q},\ x = y^2+z^2 \,\}.$$
$D$ is Diophantine by definition. By Hasse–Minkowski, $x = y^2+z^2$ is solvable over $\mathbb{Q}$ iff it is solvable over $\mathbb{R}$ and every $\mathbb{Q}_p$; unwinding the local conditions gives, for $x>0$,
$$x \in D \iff v_p(x) \equiv 0 \pmod 2 \ \text{ for every prime } p \equiv 3 \pmod 4,$$
where $v_p$ is the $p$-adic valuation. (For $p\equiv 1 \bmod 4$ and $p=2$, $-1$ is a norm locally and no condition arises.)

Check three values.
- $x=3$: $v_3(3)=1$, odd, $3\equiv 3 \bmod 4$, so $3\notin D$. Directly: $3=y^2+z^2$ with $y=a/c,z=b/c$ gives $3c^2=a^2+b^2$; reducing mod $3$, $a^2+b^2\equiv 0$ forces $3\mid a$ and $3\mid b$ (since $-1$ is not a square mod $3$), then $9 \mid 3c^2$, so $3\mid c$ — infinite descent. No solution.
- $x=9/4$: $v_3=2$, even; and indeed $9/4 = (3/2)^2 + 0^2 \in D$.
- $x=5/13$: $5,13\equiv 1 \bmod 4$, all relevant valuations vacuously even; explicitly $5/13 = (7/13)^2+(4/13)^2 = (49+16)/169 = 65/169 = 5/13$. ✓

**What this shows.** A single existential formula detects the *parity* of $v_3$, $v_7$, $v_{11}$, … simultaneously. This is exactly the raw material Robinson, Poonen and Koenigsmann use: varying the form to $z_1^2-az_2^2-bz_3^2+ab z_4^2$ over parameters $(a,b)$ produces a family of Diophantine sets whose intersection cuts out $\mathbb{Z}_{(p)}$ and then
$$\mathbb{Z} = \bigcap_{p} \mathbb{Z}_{(p)}.$$
The intersection over the parameters $(a,b)$ is a **universal** quantifier — that is Koenigsmann's $\forall$-definition. Parity data alone never isolates $\mathbb{Z}$: $D$ contains $1/4$ and $3^2/7^2$ and misses $3$, so it is neither discrete nor bounded, consistent with Mazur's conjecture. Closing Hilbert's tenth problem for $\mathbb{Q}$ means replacing that infinite intersection with a finite existential witness — or proving no such witness can exist.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*