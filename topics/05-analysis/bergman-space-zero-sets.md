---
id: 05-analysis/bergman-space-zero-sets
title: "Bergman Space Zero Set Characterization"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bergman Space Zero Set Characterization

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/bergman-space-zero-sets` · **Status:** open

## 1. Problem Statement / Conjecture

Give an intrinsic, checkable description of the zero sets of the Bergman space $A^p(\mathbb{D})$.

Let $\mathbb{D}=\{z\in\mathbb{C}:|z|<1\}$ and $0<p<\infty$. A sequence $Z=\{z_n\}\subset\mathbb{D}$ (with multiplicities, repetitions allowed) is an **$A^p$ zero set** if there is $f\in A^p$, $f\not\equiv 0$, whose zero divisor is exactly $Z$. Write $\mathcal{Z}(A^p)$ for the family of such sequences.

**Problem.** Characterize $\mathcal{Z}(A^p)$ by a condition on the geometry of $Z$ alone — an explicit density, entropy, or summability criterion, decidable from the points $z_n$ without producing the function $f$.

A complete solution must supply a condition $\mathcal{C}_p(Z)$ such that $Z\in\mathcal{Z}(A^p)\iff \mathcal{C}_p(Z)$ holds, together with proofs of both implications. The analogue for the Hardy space $H^p$ is the Blaschke condition $\sum_n(1-|z_n|)<\infty$, independent of $p$; for $A^p$ no such statement is known, and the class genuinely depends on $p$.

Three structural sub-questions, all open in general:

- **Union problem (per $p$):** for which $p$ is $\mathcal{Z}(A^p)$ closed under finite unions?
- **Contraction problem:** if $\{z_n\}\in\mathcal{Z}(A^p)$ and $w_n=t_n z_n$ with $0\le t_n\le 1$, is $\{w_n\}\in\mathcal{Z}(A^p)$?
- **Modulus problem:** to what extent does membership depend on $\{|z_n|\}$ alone?

## 2. Mathematical Foundations

For $0<p<\infty$ and $\alpha>-1$, the **weighted Bergman space** is
$$A^p_\alpha=\Big\{f\in\mathrm{Hol}(\mathbb{D}):\ \|f\|^p_{A^p_\alpha}=(\alpha+1)\int_{\mathbb{D}}|f(z)|^p(1-|z|^2)^\alpha\,dA(z)<\infty\Big\},$$
with $dA$ normalized area measure and $A^p=A^p_0$. Point evaluation is bounded:
$$|f(z)|^p\le \frac{C_\alpha\,\|f\|^p_{A^p_\alpha}}{(1-|z|^2)^{2+\alpha}},$$
so $A^p_\alpha$ is a space of "almost bounded-growth" functions; consequently $\mathcal{Z}(A^p_\alpha)$ is closed under passing to subsequences.

**Jensen's formula.** For $f$ with $f(0)\ne 0$ and zeros $\{z_n\}$, with counting function $n(t)=\\#\{n:|z_n|\le t\}$ and $N(r)=\int_0^r n(t)\,\frac{dt}{t}$,
$$N(r)=\frac{1}{2\pi}\int_0^{2\pi}\log|f(re^{i\theta})|\,d\theta-\log|f(0)|.$$
Combining with $M_p(r)^p=\frac{1}{2\pi}\int|f(re^{i\theta})|^p d\theta\le \frac{C\|f\|^p_{A^p_\alpha}}{(1-r)^{1+\alpha}}$ and Jensen's inequality gives the basic **growth ceiling**
$$N(r)\le \frac{1+\alpha}{p}\log\frac{1}{1-r}+O(1),\qquad r\to 1^-. \tag{2.1}$$

**Horowitz's necessary condition** (Horowitz 1974). If $Z\in\mathcal{Z}(A^p)$ then for every $\varepsilon>0$
$$\sum_n \frac{1-|z_n|}{\big(\log\frac{1}{1-|z_n|}\big)^{1+\varepsilon}}<\infty, \tag{2.2}$$
and this is sharp: there exist $A^p$ zero sets with $\sum_n (1-|z_n|)\big(\log\frac{1}{1-|z_n|}\big)^{-1}=\infty$. Note (2.2) does not mention $p$.

**Horowitz products.** With $b_n(z)=\frac{|z_n|}{z_n}\frac{z_n-z}{1-\overline{z_n}z}$, set
$$H(z)=\prod_n b_n(z)\big(2-b_n(z)\big)=\prod_n\big(1-(1-b_n(z))^2\big).$$
Since $1-b_n=O\big((1-|z_n|)^{1/2}\big)$ in a suitable sense, $H$ converges for many non-Blaschke sequences and supplies the standard sufficiency machinery.

**Seip densities.** For $\varphi_z(w)=\frac{z-w}{1-\bar z w}$ and $\Gamma$ uniformly discrete in the hyperbolic metric,
$$D^+(\Gamma)=\limsup_{r\to1^-}\ \sup_{z\in\mathbb{D}}\ \frac{\sum_{1/2<|\varphi_z(\gamma)|<r}\log\frac{1}{|\varphi_z(\gamma)|}}{\log\frac{1}{1-r}},$$
with $D^-$ the corresponding $\liminf/\inf$.

**Korenblum entropy.** For a finite union of disjoint arcs $I=\bigcup_k I_k\subset\partial\mathbb{D}$, $\kappa(I)=\sum_k |I_k|\log\frac{e}{|I_k|}$; the Korenblum condition asks $\mu_Z(S(I))\le C\,\kappa(I)$ for the Carleson boxes $S(I)$, where $\mu_Z$ counts points of $Z$ weighted by $1-|z_n|$.

## 3. History & State of the Art (SOTA)

- **1962.** Shapiro and Shields treat zero sets of Dirichlet-type spaces (Math. Z. 80), establishing the template of "no Blaschke-style characterization beyond Hardy".
- **1974.** Charles Horowitz, *Zeros of functions in the Bergman spaces* (Duke Math. J. 41), founds the subject: the products above, the necessary condition (2.2) with its sharpness, the strictness $\mathcal{Z}(A^p)\subsetneq\mathcal{Z}(A^q)$ for $0<q<p$, and the fact that $Z_1,Z_2\in\mathcal{Z}(A^p)\Rightarrow Z_1\cup Z_2\in\mathcal{Z}(A^{p/2})$.
- **1975.** Korenblum, *An extension of the Nevanlinna theory* (Acta Math. 135), fully characterizes zero sets of the growth space $A^{-\infty}=\bigcup_{n}A^{-n}$ by the entropy condition. This is the one genuinely solved neighbour.
- **1991–1993.** Hedenmalm's contractive/canonical divisor for $A^2$ (Crelle 422) and Duren–Khavinson–Shapiro–Sundberg (Pacific J. Math. 157) give a Blaschke-substitute *factorization* for a given zero set, but the construction presupposes the zero set.
- **1993–1995.** Seip characterizes sampling and interpolation sequences for $A^p_\alpha$ by $D^\pm$ (Invent. Math. 113) and settles the $A^{-\alpha}$ zero-set problem in Korenblum's density language (J. Anal. Math. 67).
- **1996.** Luecking, *Zero sequences for Bergman spaces* (Complex Variables 30), proves $\mathcal{Z}(A^p)$ is **not** closed under finite unions, killing the hope that the class is a lattice and hence that a simple additive density could describe it.
- **2000s–present.** Textbook accounts: Hedenmalm–Korenblum–Zhu (2000, Ch. 4), Duren–Schuster (2004, Ch. 4–5). No characterization has appeared; the problem is listed as open in both.

## 4. Partial Results / Verified Cases

- **$A^{-\infty}$ and $A^{-\alpha}$ (growth spaces):** solved. Korenblum (1975) for $A^{-\infty}$ via $\kappa$-entropy; Seip (1995) for fixed $\alpha>0$.
- **Uniformly discrete sequences:** if $D^+(\Gamma)<\frac{1+\alpha}{p}$ then $\Gamma$ is an interpolation sequence for $A^p_\alpha$ and hence a zero set; if $D^-(\Gamma)>\frac{1+\alpha}{p}$ it is not (Seip 1993). The boundary case $D^\pm=\frac{1+\alpha}{p}$ is undecided, and the gap between $D^-$ and $D^+$ is unresolved for non-regular sequences.
- **Blaschke sequences:** $\sum(1-|z_n|)<\infty\Rightarrow Z\in\mathcal{Z}(A^p)$ for all $p$ (via a Blaschke product, which lies in $H^\infty\subset A^p$). Strictly sufficient, far from necessary.
- **Radial/one-ray sequences:** for $Z\subset[0,1)$ the Jensen ceiling (2.1) and Horowitz-product estimates match in order, giving essentially sharp criteria in terms of $N(r)$ versus $\frac1p\log\frac1{1-r}$.
- **Sequences in a Stolz angle** or in finitely many hyperbolic geodesic strips: Luecking-type integral conditions on the counting measure are both necessary and sufficient up to constants.
- **$p=2$:** the extremal (canonical) divisor $G_Z$ exists for every $Z\in\mathcal{Z}(A^2)$ and satisfies the expansive multiplier property $\|f\|_{A^2}\ge\|f/G_Z\|_{A^2}$ — a complete factorization theory on the solved side.
- **Random zero sets:** for the hyperbolic Gaussian analytic function $\sum a_n z^n$ with i.i.d. standard complex Gaussians, the zero set is a determinantal process (Peres–Virág 2005) whose a.s. membership in $\mathcal{Z}(A^p)$ is decidable; Bomash (1992) gave earlier random constructions.

## 5. Principal Obstacles

- **No Nevanlinna factorization.** In $H^p$, $f=B\cdot S\cdot F$ separates zeros from growth, so the zero condition decouples from the norm. $A^p$ has no inner–outer factorization; Hedenmalm's divisors are extremal objects defined *from* $Z$, so they cannot serve as a test.
- **Jensen's formula loses the arguments.** The only robust necessary tool, (2.1)–(2.2), sees $\{|z_n|\}$ only. But $\mathcal{Z}(A^p)$ is not determined by moduli: angular clustering matters. Any modulus-based criterion is therefore provably incomplete, and no analogue of Jensen sensitive to argument is available.
- **Failure of union-closure** (Luecking 1996). A criterion of the form "$\mu_Z(S(I))\le C\kappa(I)$" or any subadditive density condition is automatically union-stable, hence cannot characterize $\mathcal{Z}(A^p)$. This rules out the entire family of Korenblum-type answers that worked for $A^{-\infty}$.
- **Non-uniformly-discrete sequences.** Seip's density theory requires hyperbolic separation. Bergman zero sets may cluster arbitrarily (multiplicities, dense pile-ups on a ray), and $D^\pm$ is then $+\infty$ or undefined.
- **The $p$-dependence is fine-grained.** The known necessary condition (2.2) is $p$-free; the known sufficient conditions are integral estimates whose constants degrade as $p\to0$ or $p\to\infty$. Nothing interpolates.
- **Non-convexity for $p<1$.** For $0<p<1$ the space is only quasi-Banach; duality and Hahn–Banach arguments that could convert an extremal problem into a geometric condition are unavailable.

## 6. The Gap

Proven: two one-sided conditions that never meet.

$$\underbrace{\sum(1-|z_n|)<\infty\ \ \text{or}\ \ D^+(Z)<\tfrac{1+\alpha}{p}}_{\text{sufficient}}\ \subsetneq\ \mathcal{Z}(A^p_\alpha)\ \subsetneq\ \underbrace{\Big\{N(r)\le\tfrac{1+\alpha}{p}\log\tfrac1{1-r}+O(1)\ \text{and}\ (2.2)\Big\}}_{\text{necessary}}.$$

Both inclusions are strict, and the sufficient side is modulus-blind in one direction while the necessary side is modulus-blind in the other. The exact missing step: a quantity $\mathcal{C}_p(Z)$ that (i) depends on the arguments $\arg z_n$, (ii) is *not* subadditive under unions — matching Luecking's counterexample — and (iii) is comparable to the extremal quantity
$$\inf\Big\{\|f\|_{A^p}:\ f\in A^p,\ f|_Z=0\ \text{to order},\ f(0)=1\Big\}<\infty.$$
Every known geometric functional fails (ii). Crossing the gap means either constructing a genuinely non-subadditive density, or proving that no condition expressible in a suitable class (e.g. a Borel condition on the counting measure) can characterize $\mathcal{Z}(A^p)$ — a rigidity/undecidability-flavoured negative answer.

## 7. Current Research (as of June 2026)

- **Extremal/divisor methods.** Norwegian (NTNU, Seip school) and Nordic groups continue to push canonical divisors and their $A^p$, $p\ne2$ analogues, seeking two-sided norm control on $f/G_Z$.
- **Luecking-type integral conditions.** Refinements replacing counting by weighted Carleson-box sums over hyperbolic Whitney partitions, with the aim of an "almost characterization" whose sufficient and necessary versions differ only by an $\varepsilon$ in the exponent. *(frontier — verify)*
- **Random zero sets and determinantal processes.** Gaussian analytic function techniques give sharp a.s. thresholds and yield explicit non-subadditive examples; a program to convert hole probabilities into deterministic zero-set criteria is active. *(frontier — verify)*
- **Transfer to Fock spaces and several variables.** Zero-set/divisor problems in $\mathcal{F}^p(\mathbb{C})$ and in Bergman spaces of the ball and of bounded symmetric domains, where the Seip density theory has clean analogues but the same characterization gap persists.
- **Model-space and operator-theoretic reformulations.** Membership of $Z$ in $\mathcal{Z}(A^p)$ recast as non-triviality of an invariant subspace of the Bergman shift with index one; work relating this to the Aleman–Richter–Sundberg structure theory. *(frontier — verify)*

## 8. Future Work

- Settle the **union problem quantitatively**: determine the least $q=q(p)$ with $Z_1,Z_2\in\mathcal{Z}(A^p)\Rightarrow Z_1\cup Z_2\in\mathcal{Z}(A^q)$; Horowitz gives $q\le p/2$, Luecking gives $q<p$, the truth is unknown.
- Resolve the **contraction problem**; a positive answer would make $\mathcal{Z}(A^p)$ a hereditary class and drastically constrain the form of any characterization.
- Decide the **boundary density case** $D^-(\Gamma)=D^+(\Gamma)=\frac{1+\alpha}{p}$ for uniformly discrete $\Gamma$.
- Sharpen (2.2) to a $p$-dependent necessary condition; even a criterion detecting one bit of angular information would be new.
- Prove a **negative structure theorem**: exhibit a class of geometric conditions provably unable to characterize $\mathcal{Z}(A^p)$, formalizing the union obstruction.

## 9. Key References

- **[Foundational]** C. Horowitz. *Zeros of functions in the Bergman spaces.* Duke Mathematical Journal **41** (1974), 693–710.
- **[Foundational]** C. Horowitz. *Factorization theorems for functions in the Bergman spaces.* Duke Mathematical Journal **44** (1977), 201–213.
- **[Foundational]** B. Korenblum. *An extension of the Nevanlinna theory.* Acta Mathematica **135** (1975), 187–219.
- **[Foundational]** H. S. Shapiro, A. L. Shields. *On the zeros of functions with finite Dirichlet integral and some related function spaces.* Mathematische Zeitschrift **80** (1962), 217–229.
- **[SOTA]** K. Seip. *Beurling type density theorems in the unit disk.* Inventiones Mathematicae **113** (1993), 21–39.
- **[SOTA]** K. Seip. *On Korenblum's density condition for the zero sequences of $A^{-\alpha}$.* Journal d'Analyse Mathématique **67** (1995), 307–322.
- **[SOTA]** D. H. Luecking. *Zero sequences for Bergman spaces.* Complex Variables, Theory and Application **30** (1996), 345–362.
- **[SOTA]** H. Hedenmalm. *A factorization theorem for square area-integrable analytic functions.* Journal für die reine und angewandte Mathematik **422** (1991), 45–68.
- **[SOTA]** P. Duren, D. Khavinson, H. S. Shapiro, C. Sundberg. *Contractive zero-divisors in Bergman spaces.* Pacific Journal of Mathematics **157** (1993), 37–56.
- **[SOTA]** C. Horowitz. *Some conditions on Bergman space zero sets.* Journal d'Analyse Mathématique **62** (1994), 323–348.
- **[SOTA]** Y. Peres, B. Virág. *Zeros of the i.i.d. Gaussian power series: a conformally invariant determinantal process.* Acta Mathematica **194** (2005), 1–35.
- **[SOTA]** G. Bomash. *A Blaschke-type product and random zero sets for Bergman spaces.* Arkiv för Matematik **30** (1992), 45–60.
- **[Survey]** H. Hedenmalm, B. Korenblum, K. Zhu. *Theory of Bergman Spaces.* Graduate Texts in Mathematics 199, Springer, 2000 (Chapter 4).
- **[Survey]** P. Duren, A. Schuster. *Bergman Spaces.* Mathematical Surveys and Monographs 100, American Mathematical Society, 2004 (Chapters 4–5).

## 10. Worked Example / Concrete Special Case

**A radial sequence with a sharp $p$-threshold.** Take
$$z_n=1-\tfrac1n,\qquad n=2,3,4,\dots$$

*Step 1 — not a Hardy zero set.* $\sum_{n\ge2}(1-|z_n|)=\sum 1/n=\infty$, so $Z$ violates Blaschke and is not the zero set of any nonzero $f\in H^p$, $p>0$, nor of any bounded function.

*Step 2 — Horowitz's condition passes.* With $1-|z_n|=1/n$, $\log\frac{1}{1-|z_n|}=\log n$, so for every $\varepsilon>0$
$$\sum_{n\ge2}\frac{1/n}{(\log n)^{1+\varepsilon}}<\infty,$$
so (2.2) gives no obstruction: $Z$ is a candidate.

*Step 3 — the Jensen ceiling decides.* Here $n(t)=\\#\{n:1-\frac1n\le t\}=\big\lfloor\frac{1}{1-t}\big\rfloor$, hence
$$N(r)=\int_0^r\frac{n(t)}{t}\,dt=\log\frac{1}{1-r}+O(1).$$
Condition (2.1) with $\alpha=0$ requires $N(r)\le\frac1p\log\frac1{1-r}+O(1)$, i.e.
$$1\le \frac1p .$$
So for **$p>1$ the sequence $Z$ is not an $A^p$ zero set**: no nonzero $f\in A^p$ vanishes on $\{1-\frac1n\}$. For $p<1$ the ceiling leaves room, and a Horowitz product built on $Z$ is shown to lie in $A^p$ for all sufficiently small $p>0$; the threshold sits at $p=1$, where the two sides of (2.1) agree to $O(1)$ and the borderline is delicate.

*Step 4 — moduli are not enough.* Keep the same multiset of moduli $\{1-\frac1n\}$ but redistribute arguments: place the $m_k=\lfloor\lambda 2^k\rfloor$ points falling in the annulus $1-2^{-k}\le|z|<1-2^{-k-1}$ at equally spaced angles $\theta=2\pi j/m_k$. The new sequence $\Gamma_\lambda$ is uniformly discrete with $D^+(\Gamma_\lambda)\asymp\lambda$, so by Seip's theorem $\Gamma_\lambda\in\mathcal{Z}(A^p)$ whenever $\lambda$ is small — even though $\sum(1-|\gamma|)=\sum_k m_k2^{-k}=\infty$ and the radial data $N(r)$ is unchanged from Step 3. Jensen's formula, seeing only $N(r)$, assigns both configurations the same verdict, yet their memberships differ for $p$ near the threshold.

That mismatch is the problem in miniature: the only sharp necessary tool is blind to exactly the information the sufficient tools use.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*