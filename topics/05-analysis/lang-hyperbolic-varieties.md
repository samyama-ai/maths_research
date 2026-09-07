---
id: 05-analysis/lang-hyperbolic-varieties
title: "Lang Hyperbolic Varieties"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lang's Conjecture on Hyperbolic Varieties

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/lang-hyperbolic-varieties` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth complex projective variety.

**Lang's conjecture (geometric form).** $X$ is Kobayashi hyperbolic if and only if every irreducible subvariety $Y \subseteq X$ (including $X$ itself) is of general type.

**Lang's conjecture (arithmetic form).** If $X$ is defined over a number field $K$ and is Kobayashi hyperbolic, then $X(L)$ is finite for every finite extension $L/K$. More generally (Bombieri–Lang): if $X$ is of general type over $K$, then $X(K)$ is not Zariski dense.

The "only if" direction of the geometric form is a theorem: hyperbolicity passes to subvarieties, and hyperbolic implies general type is what is missing. The **hard content** is:

- (a) every subvariety of general type $\Rightarrow$ $X$ hyperbolic (the analytic direction), and
- (b) $X$ hyperbolic $\Rightarrow$ $X$ and all its subvarieties are of general type (the algebraic direction; already open for $X$ itself in dimension $\ge 3$).

A complete resolution means proving both implications for all $n = \dim X$, or exhibiting a projective $X$ with all subvarieties of general type that carries a non-constant entire curve $f : \mathbb{C} \to X$ (disproof of (a)), or a hyperbolic $X$ with $\kappa(X) < \dim X$ (disproof of (b)).

## 2. Mathematical Foundations

**Kobayashi pseudodistance.** For $p,q \in X$, let $d_X(p,q)$ be the infimum of $\sum_i \rho_{\mathbb{D}}(a_i,b_i)$ over chains of holomorphic discs $f_i : \mathbb{D} \to X$ with $f_i(a_i)=p_i$, $f_i(b_i)=p_{i+1}$, $\rho_{\mathbb{D}}$ the Poincaré distance. Infinitesimally,
$$
\kappa_X(x,\xi)=\inf\{\, \lambda>0 : \exists f:\mathbb{D}\to X,\ f(0)=x,\ \lambda f'(0)=\xi \,\}.
$$
$X$ is **Kobayashi hyperbolic** iff $d_X$ is a genuine distance, equivalently (for $X$ compact) iff $\kappa_X(x,\xi)>0$ for all $\xi \neq 0$.

**Brody's theorem** (1978). A compact complex space $X$ is Kobayashi hyperbolic iff there is no non-constant holomorphic map $f:\mathbb{C}\to X$. This converts an infinitesimal-metric condition into a statement about entire curves and is the bridge to value-distribution theory.

**General type.** $X$ smooth projective of dimension $n$ is of general type iff the Kodaira dimension
$$
\kappa(X)=\limsup_{m\to\infty}\frac{\log h^0(X,mK_X)}{\log m}
$$
equals $n$, i.e. $h^0(X, mK_X) \sim c\, m^n$ with $c>0$. For singular $Y$, "general type" means general type on a resolution.

**Jet differentials.** Let $J_kX \to X$ be the bundle of $k$-jets of germs $(\mathbb{C},0)\to X$. A section of $E_{k,m}^{GG}T^*_X$ (Green–Griffiths sheaf) is a polynomial $P(f',f'',\dots,f^{(k)})$ of weighted degree $m$; Demailly's subsheaf $E_{k,m}T^*_X \subset E^{GG}_{k,m}T^*_X$ consists of those invariant under reparametrization $t \mapsto \varphi(t)$.

**Fundamental vanishing theorem** (Green–Griffiths; Siu–Yeung; Demailly). If $P \in H^0(X, E_{k,m}T^*_X \otimes A^{-1})$ with $A$ ample, then every entire curve $f:\mathbb{C}\to X$ satisfies
$$
P(f',f'',\dots,f^{(k)}) \equiv 0 .
$$
Hence entire curves are confined to the base locus $\mathrm{Bs}\big(\bigcap_{k,m}\big)$ of such jet differentials — this is the engine behind every known case.

**Green–Griffiths–Lang conjecture.** If $X$ is of general type there is a proper closed $Z \subsetneq X$ containing the image of every non-constant $f:\mathbb{C}\to X$ (Lang: $Z$ = union of the non-general-type subvarieties, the *special locus*).

**Kobayashi conjecture.** A general hypersurface $X_d \subset \mathbb{P}^n$ of degree $d \ge 2n-1$ is hyperbolic. Its complement $\mathbb{P}^n \setminus X_d$ is hyperbolic for $d \ge 2n+1$.

## 3. History & State of the Art (SOTA)

- **1970** — Kobayashi introduces the pseudodistance and the hyperbolicity program (*Hyperbolic Manifolds and Holomorphic Mappings*).
- **1926 / 1977** — Bloch's theorem on entire curves in abelian varieties, made rigorous by Ochiai and Green.
- **1979–80** — Green and Griffiths propose the algebraic-degeneracy conjecture for varieties of general type.
- **1986** — Lang's *Bull. AMS* survey "Hyperbolic and Diophantine analysis" states the equivalence above and the analytic/arithmetic dictionary in its modern form.
- **1980** — Kawamata's structure theorem for the "Kawamata locus" of a subvariety of an abelian variety; combined with Bloch–Ochiai this settles the abelian case.
- **1991** — Faltings proves the arithmetic Lang conjecture for subvarieties of abelian varieties.
- **1998–2000** — McQuillan proves Green–Griffiths for surfaces of general type with $c_1^2 > c_2$ and positive index-type hypotheses, via Diophantine approximation on foliations; Demailly–El Goul get hyperbolicity of very general surfaces in $\mathbb{P}^3$ of degree $d \ge 21$.
- **2010** — Diverio–Merker–Rousseau: algebraic degeneracy for generic hypersurfaces $X_d \subset \mathbb{P}^n$ with $d \ge 2^{n^5}$.
- **2015–2017** — Siu proves hyperbolicity of generic hypersurfaces of sufficiently high (non-explicit) degree; Brotbek gives a clean proof via Wronskian/ Cartan-type jet constructions.
- **2019–2022** — effective degree bounds pushed to $d \ge (\sqrt{n}\log n)^n$ (Merker–Ta) and reduced further by the Riedl–Yang Grassmannian technique, which converts hyperbolicity in $\mathbb{P}^{n}$ into hyperbolicity statements about lower-dimensional families.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| Curves ($n=1$) | Complete: $C$ hyperbolic $\iff$ $g(C)\ge 2$ $\iff$ general type. |
| Subvarieties of abelian varieties | **Fully proved.** Bloch–Ochiai + Kawamata: $Y \subseteq A$ is hyperbolic iff $Y$ contains no translated abelian subvariety of positive dimension, which is equivalent to all subvarieties being of general type. Yamanoi added the pseudo-metric refinement. |
| Surfaces of general type with $c_1^2 > c_2$ | McQuillan (1998): entire curves are algebraically degenerate. |
| Very general surfaces $X_d \subset \mathbb{P}^3$ | Hyperbolic for $d\ge 21$ (Demailly–El Goul); improved to $d \ge 18$ by Păun's refinement of the same jet method. |
| General hypersurfaces $X_d \subset \mathbb{P}^n$ | Hyperbolic for $d \ge (\sqrt{n}\log n)^n$ (Merker–Ta, 2019), following Brotbek (2017) and Siu (2015). Conjectured optimal: $d \ge 2n-1$. |
| Complements $\mathbb{P}^n \setminus X_d$ | Hyperbolic for general $X_d$ with $d$ large and explicit (Brotbek–Deng, GAFA 2019). |
| Quotients of bounded symmetric domains | Compact quotients $\Gamma \backslash \Omega$ are hyperbolic and of general type; conjecture holds trivially. |
| Arithmetic side, $n=1$ | Faltings' theorem (Mordell): $g\ge2 \Rightarrow$ $C(K)$ finite. |
| Arithmetic side, $Y \subset A$ | Faltings (1991): $Y(K)$ contained in finitely many translated subgroups. |

Dimension $n \ge 3$ for general projective $X$: **open in both directions**.

## 5. Principal Obstacles

- **Jet differentials are scarce in low degree.** Riemann–Roch for $E_{k,m}T^*_X$ has an Euler characteristic dominated by $h^0 - h^2$; the intermediate cohomology $h^1$ is uncontrolled for $n \ge 3$, so existence of a single jet differential vanishing on an ample divisor requires either huge $k$ (order of jets $\ge n$, often $k \sim n$ or larger) or huge degree $d$. This is exactly why the bounds are exponential in $n$ rather than linear.
- **From degeneracy to hyperbolicity.** The vanishing theorem confines entire curves to a base locus $Z$; one must then run the whole argument again on $Z$, whose singularities and positivity are not controlled. There is no known induction that terminates uniformly.
- **The algebraic direction has no analytic input.** To prove "hyperbolic $\Rightarrow$ general type" one must produce pluricanonical sections from the *absence* of entire curves. No positivity of $K_X$ is known to follow from $\kappa_X > 0$; the only general tool is Mori theory, which gives rational curves when $K_X$ is not nef — but $K_X$ nef with $\kappa(X)<n$ (e.g. abundance-type situations) is not excluded by any current argument.
- **Failure of standard analysis.** Nevanlinna theory yields a Second Main Theorem with truncated counting only in dimension 1 or under strong positivity; the higher-dimensional SMT with a defect relation strong enough to force degeneracy is itself equivalent to the conjecture. Foliation theory (McQuillan, Brunella) works on surfaces because a foliation by curves on a surface has a nef canonical class dichotomy — an analogue in dimension $\ge 3$ is missing.
- **Genericity is essential to all known high-degree results.** The proofs of Siu/Brotbek use a general member of a family and a Wronskian/deformation argument; they say nothing about a *given* hypersurface such as a Fermat one.

## 6. The Gap

Proven: hyperbolicity of *very general* members of explicit families in $\mathbb{P}^n$ with degree $d \gtrsim n^{n/2}$, and the complete abelian/curve cases. Conjectured: an intrinsic equivalence for *every* projective $X$.

Two precise barriers:

1. **Effectivity gap in the Kobayashi conjecture**: between the proven $d \ge (\sqrt n \log n)^n$ and the expected $d \ge 2n-1$ lies a super-exponential factor. Closing it requires jet differentials of order $k = O(1)$ rather than $k \sim n$, i.e. a positivity theorem for $E_{k,m}T^*_X$ with $k$ bounded.
2. **The converse implication**: a proof that $\kappa_X > 0$ forces $h^0(mK_X)$ to grow like $m^n$. Even the weaker statement "$X$ hyperbolic $\Rightarrow K_X$ big" is open for $n=3$; the case "$X$ hyperbolic $\Rightarrow K_X$ ample" is a known consequence of the (open) abundance conjecture plus non-existence of hyperbolic varieties with $\kappa = 0$.

## 7. Current Research (as of June 2026)

- **Effective jet methods** — the school around Demailly (Grenoble), Păun (Stony Brook), Deng Ya (Paris-Saclay), Brotbek (Strasbourg), Merker (Orsay). The focus is on Wronskian ideal sheaves and "Fermat-type" degeneracy loci to reduce the Kobayashi degree bound toward polynomial in $n$. *(frontier — verify)* Claims of bounds polynomial in $n$ for hyperbolicity of general $X_d \subset \mathbb{P}^n$ circulate as preprints and should be checked against Demailly's 2020 survey baseline.
- **Grassmannian/moving-coefficient techniques** — Riedl and Yang show that hyperbolicity of general hypersurfaces of dimension $n$ in $\mathbb{P}^{n+1}$ follows from degeneracy statements in higher ambient dimensions, converting one conjecture's bound into another's.
- **Foliations and orbifolds** — Campana's special/orbifold framework recasts Lang's dichotomy as: $X$ is hyperbolic iff its core map is trivial. Work of Campana, Claudon, Rousseau seeks the orbifold analogue of Bloch–Ochiai.
- **Arithmetic transfer** — Lawrence–Venkatesh's $p$-adic period-map method gives non-density of rational points for families with large monodromy, an arithmetic route toward Bombieri–Lang cases independent of analysis.
- **Big Picard / hyperbolic extension** — Deng, Brotbek, Cadorel prove Picard-type extension theorems for maps into varieties admitting Finsler metrics with negative curvature, from period domains and base spaces of maximal-variation families.

## 8. Future Work

- Prove "hyperbolic $\Rightarrow$ $K_X$ big" for threefolds, using the minimal model program: rule out hyperbolic varieties with a nef $K_X$ and $\kappa < n$ by showing the Iitaka fibration produces non-hyperbolic fibres.
- Establish the Green–Griffiths–Lang conjecture for hypersurfaces of general type in $\mathbb{P}^n$ with $d \ge n+2$ (the minimal general-type degree) — currently far out of reach; even $d = n+2$ in $\mathbb{P}^4$ is open.
- Develop a Second Main Theorem with truncation level 1 for entire curves into varieties of general type; Yamanoi's results for abelian varieties are the model.
- Find a *non-generic* method: a hyperbolicity criterion checkable on a specific equation, e.g. deciding whether the Fermat hypersurface's small deformations are hyperbolic.
- Clarify the conjectural degree $2n-1$: are there hyperbolic hypersurfaces of degree exactly $2n-1$ in $\mathbb{P}^n$ for $n \ge 4$? Examples exist only for small $n$ (Duval, Shiffman–Zaidenberg for surfaces in $\mathbb{P}^3$).

## 9. Key References

- **[Foundational]** S. Lang. *Hyperbolic and Diophantine analysis.* Bulletin of the American Mathematical Society **14** (1986), 159–205.
- **[Foundational]** S. Kobayashi. *Hyperbolic Complex Spaces.* Grundlehren der mathematischen Wissenschaften 318, Springer, 1998.
- **[Foundational]** R. Brody. *Compact manifolds and hyperbolicity.* Transactions of the AMS **235** (1978), 213–219.
- **[Foundational]** M. Green, P. Griffiths. *Two applications of algebraic geometry to entire holomorphic mappings.* In: The Chern Symposium 1979, Springer, 1980, 41–74.
- **[Foundational]** Y. Kawamata. *On Bloch's conjecture.* Inventiones Mathematicae **57** (1980), 97–100.
- **[Foundational]** T. Ochiai. *On holomorphic curves in algebraic varieties with ample irregularity.* Inventiones Mathematicae **43** (1977), 83–96.
- **[Foundational]** P. Vojta. *Diophantine Approximations and Value Distribution Theory.* Lecture Notes in Mathematics 1239, Springer, 1987.
- **[SOTA]** M. McQuillan. *Diophantine approximations and foliations.* Publications Mathématiques de l'IHÉS **87** (1998), 121–174.
- **[SOTA]** J.-P. Demailly, J. El Goul. *Hyperbolicity of generic surfaces of high degree in projective 3-space.* American Journal of Mathematics **122** (2000), 515–546.
- **[SOTA]** S. Diverio, J. Merker, E. Rousseau. *Effective algebraic degeneracy.* Inventiones Mathematicae **180** (2010), 161–223.
- **[SOTA]** Y.-T. Siu. *Hyperbolicity of generic high-degree hypersurfaces in complex projective space.* Inventiones Mathematicae **202** (2015), 1069–1166.
- **[SOTA]** D. Brotbek. *On the hyperbolicity of general hypersurfaces.* Publications Mathématiques de l'IHÉS **126** (2017), 1–34.
- **[SOTA]** D. Brotbek, Y. Deng. *Hyperbolicity of the complements of general hypersurfaces of high degree.* Geometric and Functional Analysis **29** (2019), 690–750.
- **[SOTA]** J. Merker, T.-A. Ta. *Degrees $d \ge (\sqrt{n}\log n)^n$ and $d \ge (n\log n)^n$ in the conjectures of Green–Griffiths and of Kobayashi.* Acta Mathematica Vietnamica **44** (2019), 63–99.
- **[SOTA]** G. Faltings. *Diophantine approximation on abelian varieties.* Annals of Mathematics **133** (1991), 549–576.
- **[SOTA]** K. Yamanoi. *Pseudo Kobayashi hyperbolicity of subvarieties of general type on abelian varieties.* Journal of the Mathematical Society of Japan **71** (2019), 259–298.
- **[Survey]** J.-P. Demailly. *Recent results on the Kobayashi and Green–Griffiths–Lang conjectures.* Japanese Journal of Mathematics **15** (2020), 1–120.
- **[Survey]** F. Campana. *Orbifolds, special varieties and classification theory.* Annales de l'Institut Fourier **54** (2004), 499–630.

## 10. Worked Example / Concrete Special Case

**Setting.** Let $A = \mathbb{C}^2/\Lambda$ be a simple abelian surface (no abelian subvariety of dimension 1), and let $C \subset A$ be a smooth ample curve, e.g. a curve in the linear system $|D|$ with $D^2 = 2$ (a principal polarization). Check both sides of Lang's equivalence for $X = C$ and for $X = A$.

**Step 1 — Kodaira dimension of $C$.** Adjunction on the abelian surface: $K_A = \mathcal{O}_A$, so
$$
2g(C)-2 = (K_A + C)\cdot C = C^2 = D^2 = 2 \implies g(C) = 2 .
$$
Thus $\deg K_C = 2g-2 = 2 > 0$ and $\kappa(C) = 1 = \dim C$: $C$ is of general type. Its only subvarieties are points, trivially of general type.

**Step 2 — Hyperbolicity of $C$.** Since $g(C) = 2 \ge 2$, the universal cover of $C$ is the unit disc $\mathbb{D}$, the Kobayashi metric equals the Poincaré metric of curvature $-1$, and it is a genuine distance. So $C$ is hyperbolic. Equivalently by Brody: any $f:\mathbb{C}\to C$ lifts to $\tilde f : \mathbb{C}\to\mathbb{D}$, which is constant by Liouville. **Both sides agree.**

**Step 3 — The ambient surface $A$.** Here $K_A = \mathcal{O}_A$ gives $\kappa(A) = 0 \neq 2$: $A$ is not of general type. And indeed $A$ is not hyperbolic — the projection $\mathbb{C}^2 \to A$ restricted to any complex line $L \subset \mathbb{C}^2$ gives a non-constant entire curve $f(t) = \pi(t v)$ for $v \neq 0$. Its image is dense if $L$ has irrational slope with respect to $\Lambda$. **Both sides agree again.**

**Step 4 — Where the conjecture becomes a theorem.** For a general $Y \subseteq A$, Bloch–Ochiai says: the Zariski closure of any entire curve $f:\mathbb{C}\to A$ is a translate $a + B$ of an abelian subvariety $B \subseteq A$. Hence
$$
Y \text{ not hyperbolic} \iff Y \supseteq a + B \text{ for some } \dim B \ge 1 .
$$
By Kawamata's structure theorem, $Y$ is of general type iff $Y$ contains no such translate. Chaining the two equivalences gives Lang's conjecture *exactly* for subvarieties of abelian varieties.

**Step 5 — Why this does not generalise.** In Step 4 the group law supplies a translation-invariant frame, so the jet bundle splits: $J_kY \subset Y \times (\mathbb{C}^{n})^k$ is trivialized, and jet differentials are just polynomials in the derivatives with constant coefficients — abundant by a naive dimension count. On a hypersurface $X_d \subset \mathbb{P}^n$, $T_X$ has no such trivialization; the count of sections of $E_{k,m}T^*_X \otimes \mathcal{O}(-1)$ becomes an Euler characteristic estimate that only turns positive once $d$ exceeds roughly $(\sqrt n \log n)^n$. That single missing structure — a global frame — is the concrete content of the gap in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*