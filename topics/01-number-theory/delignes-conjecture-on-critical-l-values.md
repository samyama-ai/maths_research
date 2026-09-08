---
id: 01-number-theory/delignes-conjecture-on-critical-l-values
title: "Deligne's Conjecture on Critical L-Values"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Deligne's Conjecture on Critical L-Values

> **Topic:** Number Theory · **ID:** `01-number-theory/delignes-conjecture-on-critical-l-values` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $M$ be a pure motive over $\mathbb{Q}$ with coefficients in a number field $E$, and let $L(M,s)$ be its Hasse–Weil $L$-function. An integer $n$ is **critical** for $M$ when neither the archimedean factor $L_\infty(M,s)$ nor $L_\infty(M^\vee,1-s)$ has a pole at $s=n$. Deligne (1979) attached to $M$ two transcendental invariants $c^+(M), c^-(M) \in (E\otimes\mathbb{C})^\times$, determinants of the Betti–de Rham comparison isomorphism restricted to $\pm$-eigenspaces of complex conjugation.

**Conjecture (Deligne).** For every critical integer $n$, with $\varepsilon = (-1)^n$ and $d^{\varepsilon} = \dim_E H_B^{\varepsilon}(M)$,
$$L(M,n) \;\sim_{E^\times}\; (2\pi i)^{\,n\,d^{\varepsilon}}\, c^{\varepsilon}(M),$$
i.e. the ratio lies in $E$ (as an element of $E\otimes\mathbb{C}$, componentwise, equivariantly for $\mathrm{Aut}(\mathbb{C})$). If $c^\varepsilon(M)=0$ the assertion is that $L(M,n)=0$.

A complete proof must (i) supply the motive, (ii) compute $c^\varepsilon$, and (iii) prove the algebraicity **with the Galois-equivariance**: $\sigma\big(L(M,n)/(2\pi i)^{nd^\varepsilon}c^\varepsilon(M)\big) = L({}^\sigma\! M,n)/(2\pi i)^{nd^\varepsilon}c^\varepsilon({}^\sigma\! M)$ for all $\sigma \in \mathrm{Aut}(\mathbb{C})$. A disproof would exhibit a critical $n$ and a motive with irrational ratio.

## 2. Mathematical Foundations

**Realizations.** A pure motive $M$ of weight $w$ over $\mathbb{Q}$ with coefficients in $E$ carries:
- Betti realization $H_B(M)$, a free $E$-module of rank $d$, with an involution $F_\infty$ (infinite Frobenius) and a Hodge decomposition $H_B(M)\otimes\mathbb{C} = \bigoplus_{p+q=w} H^{p,q}$, $\overline{H^{p,q}} = H^{q,p}$;
- de Rham realization $H_{dR}(M)$, free of rank $d$ over $E$, with a descending filtration $F^\bullet$;
- $\ell$-adic realizations $H_\ell(M)$ with $G_\mathbb{Q}$-action, giving
$$L(M,s) = \prod_p \det\!\big(1 - \mathrm{Frob}_p\, p^{-s} \,\big|\, H_\ell(M)^{I_p}\big)^{-1}.$$

**Comparison.** $I: H_B(M)\otimes_\mathbb{Q}\mathbb{C} \xrightarrow{\ \sim\ } H_{dR}(M)\otimes_\mathbb{Q}\mathbb{C}$.

**Periods.** Write $H_B^{\pm}$ for the $\pm1$-eigenspaces of $F_\infty$, and $F^{\pm} \subset H_{dR}(M)\otimes\mathbb{C}$ for the span of the $H^{p,q}$ with $p > q$ together with the $\pm$-part of $H^{w/2,w/2}$ when $w$ is even. Set $H_{dR}^{\pm} = (H_{dR}(M)\otimes\mathbb{C})/F^{\mp}$. Then $c^{\pm}(M) := \det\big(H_B^{\pm}\otimes\mathbb{C} \to H_{dR}^{\pm}\big)$, computed in $E$-rational bases; it is well-defined in $(E\otimes\mathbb{C})^\times/E^\times$.

**Criticality via Hodge numbers.** For $M$ with no $(p,p)$ classes, $n$ is critical iff $n$ lies strictly between the two "middle" Hodge jumps; equivalently $\dim F^{\varepsilon} = d^{-\varepsilon}$ so that $c^\varepsilon$ is a determinant of a square matrix. Tate twist: $M(n)$ has $c^{\pm}(M(n)) = (2\pi i)^{n d^{\pm(-1)^n}} c^{\pm(-1)^n}(M)$ and $L(M(n),s)=L(M,s+n)$, so the conjecture reduces to the single value $L(M,0)$.

**Deligne's period relation.** For $M$ with no $(p,p)$-part,
$$c^+(M)\,c^-(M) \;\sim_{E^\times}\; (2\pi i)^{\,d^-}\,\delta(M), \qquad \delta(M) := \det(I),$$
which is why full period matrices ($\delta$, essentially a discriminant/Petersson-norm quantity) and the individual $c^\pm$ carry different information.

## 3. History & State of the Art (SOTA)

- **1735–1849.** Euler's $\zeta(2k)\in \pi^{2k}\mathbb{Q}$ and Dirichlet's class-number formulas are the first critical-value statements. Kummer's congruences make $L(\chi,1-m) = -B_{m,\chi}/m$ the arithmetic anchor.
- **1959–1976.** Klingen and Siegel prove rationality of $\zeta_F(1-m)$ for totally real $F$. Shimura (1976, 1977) proves algebraicity of $L(f,m)$ for critical $m$ and a holomorphic cusp form $f$, in terms of two periods $u^\pm(f)$, and constructs the period lattice from modular symbols (Manin, 1972).
- **1977–1979.** Deligne's Corvallis lecture *Valeurs de fonctions $L$ et périodes d'intégrales* unifies these into the motivic statement above, and checks it against Artin motives, CM Hecke characters, and modular forms.
- **1984–1990.** Beilinson extends the framework to non-critical points via regulators; Bloch–Kato refine the rational number itself into Tamagawa-number form, making Deligne's conjecture the "$\Gamma$-factor-free" shadow of a much finer statement.
- **1986–present.** Blasius proves the CM Hecke-character case. From the 1990s onward, Harris, Raghuram, Harder, Grobner, and Lin transfer the problem to automorphic periods on Shimura varieties and Whittaker models.

**SOTA summary.** Unconditional in rank $\le 2$ and in essentially all CM/holomorphic situations; for $\mathrm{GL}_n$, $n\ge 3$, the strongest results are about **ratios of consecutive critical values**, not individual values against $c^\pm$.

## 4. Partial Results / Verified Cases

- **Artin motives of Dirichlet characters (rank 1, weight 0).** Fully proven; classical, see §10.
- **Hecke characters of CM fields.** Blasius, *Ann. of Math.* 124 (1986): Deligne's conjecture holds for critical values of $L(\chi,s)$, $\chi$ an algebraic Hecke character of a CM field, using Shimura's abelian-variety periods and period relations of the Taniyama group (Anderson, Compositio 57, 1986). Damerell's theorem (1970–71) is the imaginary-quadratic case.
- **Modular forms.** $M_f$ of rank 2, weight $k-1$, Hodge types $(k-1,0),(0,k-1)$; critical integers $n=1,\dots,k-1$. Shimura's theorem gives $L(f,n)/\big((2\pi i)^n u^{\varepsilon}\big) \in K_f$ with $\varepsilon=(-1)^n$, and $u^\pm \sim c^\pm(M_f)$; verified for all levels, nebentypus, and all $k\ge 2$.
- **Hilbert modular forms.** Shimura, *Duke Math. J.* 45 (1978): critical values for totally real fields, matching Deligne after Yoshida's period computations.
- **Rankin–Selberg $\mathrm{GL}_2\times\mathrm{GL}_2$ and symmetric squares.** Shimura (1976, 1977) and Sturm, *Amer. J. Math.* 102 (1980) for $\mathrm{Sym}^2$; the Deligne periods factor as $c^+(M_f)c^-(M_f)$ times explicit $2\pi i$ powers.
- **$\mathrm{GL}_n\times\mathrm{GL}_{n-1}$, cohomological cuspidal, all $n$.** Harder–Raghuram (Annals of Math. Studies 203, 2020) prove rationality of **ratios** $L(\tfrac12+n,\pi\times\sigma)/L(\tfrac12+n+1,\pi\times\sigma)$ over totally real fields; Grobner–Harris (J. Inst. Math. Jussieu 15, 2016) prove individual algebraicity in terms of Whittaker periods for $\mathrm{GL}_n\times\mathrm{GL}_{n-1}$ over CM fields under a conjugate-self-duality hypothesis.
- **Polarized regular motives / unitary groups.** Harris (*Crelle* 483, 1997) proves the conjecture up to explicit "arithmetic automorphic periods" for motives arising from cohomology of unitary Shimura varieties, conditional on standard expected period relations.

## 5. Principal Obstacles

- **No unconditional category of motives.** Without the standard conjectures, "the motive $M$" attached to an automorphic representation may not exist as an object with compatible Betti/de Rham/$\ell$-adic realizations; $c^\pm(M)$ is then undefined. All $\mathrm{GL}_n$ results ($n\ge 3$) are therefore stated with automorphic surrogates.
- **Periods are not computable term by term.** $c^\pm$ is a determinant over a *proper subspace*. Cohomological methods (Eisenstein cohomology, Rankin–Selberg integrals, doubling) naturally produce the **full** period $\delta(M)$ or Petersson/Whittaker norms — products of $c^+$ and $c^-$ — and cannot separate the factors. Splitting requires extra input (CM period relations, quadratic period invariants), available only when a Shimura variety with enough Hecke correspondences is present.
- **Non-cohomological and non-tempered cases.** Maass forms and non-regular weights carry no motive at all; their critical values are not expected to be periods in Deligne's sense, so any general argument must first excise them, and no intrinsic criterion does so.
- **Galois equivariance is stronger than rationality.** Analytic methods (Rankin–Selberg unfolding, holomorphic projection) give rationality over a field of definition, but the $\sigma$-equivariance requires rational structures on automorphic cohomology compatible with $\mathrm{Aut}(\mathbb{C})$ — known only where the Shimura variety has a canonical model over a number field.
- **Vanishing periods.** When $c^\varepsilon(M)=0$ the conjecture predicts $L(M,n)=0$; no method produces vanishing from period degeneracy, so those cases stand outside every current technique.

## 6. The Gap

The proven statements have the shape
$$L(M,n) \sim_{E^\times} (2\pi i)^{a}\, P_{\mathrm{aut}}(\pi),$$
with $P_{\mathrm{aut}}$ an automorphic period (Whittaker, Petersson, or arithmetic-automorphic). The conjecture asserts the same with $c^\varepsilon(M)$. The gap is exactly two implications:

1. **Motivic existence + realization:** a motive $M(\pi)$ over the reflex field with $L(M(\pi),s)=L(\pi,s-\tfrac{w}{2})$ and known Hodge numbers.
2. **Period comparison:** $P_{\mathrm{aut}}(\pi) \sim c^{\varepsilon}(M(\pi))$ up to $E^\times$ and $2\pi i$ powers — a *factorization* of an automorphic period into motivic ones, conjectured by Harris and by Lin but proven only for $n\le 2$, CM cases, and under self-duality hypotheses.

Crossing step (2) means proving that the ratio of two transcendental quantities defined by entirely different constructions (an $L^2$-norm vs. a Betti–de Rham determinant) is algebraic — currently only accessible by exhibiting both inside the same cohomology of the same variety.

## 7. Current Research (as of June 2026)

- **Period relations for $\mathrm{GL}_n$ over CM fields.** Continuation of the Grobner–Harris–Lin program: factorizing Whittaker periods into products of "motivic-type" periods $p^{(s)}(\pi)$ via the refined Gan–Gross–Prasad conjecture (Grobner–Lin, *Amer. J. Math.* 143 (2021)). Recent work extends this to non-conjugate-self-dual $\pi$ *(frontier — verify)*.
- **Eisenstein cohomology.** The Harder–Raghuram machine (Bonn, IISER Pune) is being pushed from ratios to individual values and to $\mathrm{GL}_n \times \mathrm{GL}_m$ with $m < n-1$.
- **Unitary-group branching and theta correspondence.** Harris, Ichino, Beuzart-Plessis and collaborators use branching-law period identities to compute critical values of standard $L$-functions on unitary groups.
- **$p$-adic and Iwasawa side.** Constructions of $p$-adic $L$-functions (Panchishkin-type interpolation) supply strong indirect evidence: every interpolated value must be algebraic after dividing by the conjectured period.
- **Bloch–Kato refinement.** Groups at Regensburg, Münster and Cambridge work on Tamagawa-number formulas that imply Deligne's statement as a corollary in Rankin–Selberg and Hilbert-modular settings.

## 8. Future Work

- Prove the expected factorization of Whittaker periods into Deligne periods for all cohomological cuspidal $\pi$ on $\mathrm{GL}_n/F$, $F$ CM — the single step that would make Deligne's conjecture a theorem in the entire cohomological range.
- Construct motives for regular algebraic $\pi$ unconditionally (currently only the $\ell$-adic realizations are known, via Scholze and Harris–Lan–Taylor–Thorne); a de Rham realization with the right Hodge filtration would close step (1) of §6.
- Attack the vanishing case: prove $c^\varepsilon(M)=0 \Rightarrow L(M,n)=0$ for at least one nontrivial family.
- Extend to motives with $(p,p)$-classes (Tate classes), where criticality and $c^\pm$ interact with the Hodge conjecture.
- Establish compatibility with Beilinson–Bloch–Kato in enough examples to make the constant in $E^\times$ itself predictable.

## 9. Key References

- **[Foundational]** P. Deligne. *Valeurs de fonctions $L$ et périodes d'intégrales.* In *Automorphic Forms, Representations and L-functions*, Proc. Sympos. Pure Math. 33, Part 2, AMS, 1979, pp. 313–346.
- **[Foundational]** G. Shimura. *The special values of the zeta functions associated with cusp forms.* Comm. Pure Appl. Math. 29 (1976), 783–804.
- **[Foundational]** G. Shimura. *On the periods of modular forms.* Math. Ann. 229 (1977), 211–221.
- **[Major case]** D. Blasius. *On the critical values of Hecke L-series.* Annals of Mathematics (2) 124 (1986), 23–63.
- **[Related]** G. Anderson. *Cyclotomy and an extension of the Taniyama group.* Compositio Mathematica 57 (1986), 153–217.
- **[SOTA]** G. Harder, A. Raghuram. *Eisenstein Cohomology for $\mathrm{GL}_N$ and the Special Values of Rankin–Selberg L-Functions.* Annals of Mathematics Studies 203, Princeton University Press, 2020.
- **[SOTA]** H. Grobner, M. Harris. *Whittaker periods, motivic periods, and special values of tensor product L-functions.* Journal of the Institute of Mathematics of Jussieu 15 (2016), 711–769.
- **[SOTA]** H. Grobner, J. Lin. *Special values of L-functions and the refined Gan–Gross–Prasad conjecture.* American Journal of Mathematics 143 (2021), 859–937.
- **[Structural]** M. Harris. *L-functions and periods of polarized regular motives.* J. reine angew. Math. (Crelle) 483 (1997), 75–161.
- **[Refinement]** S. Bloch, K. Kato. *L-functions and Tamagawa numbers of motives.* In *The Grothendieck Festschrift I*, Birkhäuser, 1990, pp. 333–400.
- **[Refinement]** A. Beilinson. *Higher regulators and values of L-functions.* J. Soviet Math. 30 (1985), 2036–2070.
- **[Survey]** M. Rapoport, N. Schappacher, P. Schneider (eds.). *Beilinson's Conjectures on Special Values of L-Functions.* Perspectives in Mathematics 4, Academic Press, 1988.
- **[Survey/Periods]** H. Yoshida. *Absolute CM-Periods.* Mathematical Surveys and Monographs 106, AMS, 2003.
- **[Case]** J. Sturm. *Special values of zeta functions, and Eisenstein series of half integral weight.* Amer. J. Math. 102 (1980), 219–240.
- **[Background]** L. Washington. *Introduction to Cyclotomic Fields.* 2nd ed., Graduate Texts in Mathematics 83, Springer, 1997.

## 10. Worked Example / Concrete Special Case

Take $\chi = \chi_{-4}$, the odd primitive Dirichlet character mod $4$, and $M = M(\chi)$, the rank-1 Artin motive with $E = \mathbb{Q}$, weight $0$, Hodge type $(0,0)$, and $F_\infty$ acting by $\chi(-1) = -1$.

**Periods.** $H_B^- = \mathbb{Q}$, $H_B^+ = 0$, so $d^-=1$, $d^+=0$. The comparison isomorphism is realized inside $\mathbb{Q}(i)$, and the determinant of $I$ on the $\chi$-eigenspace is the Gauss sum:
$$c^-(M(\chi)) = \tau(\chi) = \sum_{a=1}^{4}\chi(a)e^{2\pi i a/4} = i - (-i)\cdot 1 \cdot(-1)^{?}\;=\; 2i, \qquad c^+(M(\chi)) = 1 \ (\text{empty determinant}).$$
(Directly: $\tau(\chi_{-4}) = e^{2\pi i/4} - e^{6\pi i/4} = i - (-i) = 2i$.)

**Criticality.** $L_\infty(M,s) = \Gamma_\mathbb{R}(s+1)$ since $\chi$ is odd. Every integer $n$ with $(-1)^n = -1$, i.e. every odd $n$, and every even $n \le 0$, is critical.

**Case $n$ odd, $\varepsilon = -$, $d^-=1$.** The conjecture predicts $L(\chi,n)/\big((2\pi i)^n\cdot 2i\big)\in\mathbb{Q}$.
- $n=1$: $L(\chi,1) = 1 - \tfrac13 + \tfrac15 - \cdots = \pi/4$. Then
$$\frac{\pi/4}{(2\pi i)\cdot 2i} = \frac{\pi/4}{4\pi i^2} = \frac{\pi/4}{-4\pi} = -\frac{1}{16}\in\mathbb{Q}. \checkmark$$
- $n=3$: $L(\chi,3) = \pi^3/32$. Here $(2\pi i)^3 = -8i\pi^3$, so $(2\pi i)^3\cdot 2i = -16i^2\pi^3 = 16\pi^3$ and
$$\frac{\pi^3/32}{16\pi^3} = \frac{1}{512}\in\mathbb{Q}. \checkmark$$

**Case $n$ even, $n\le 0$, $\varepsilon=+$, $d^+=0$.** The prediction degenerates to $L(\chi,n)\in\mathbb{Q}$ outright, with no transcendental factor. Indeed $L(\chi,1-m) = -B_{m,\chi}/m$ with $B_{1,\chi} = \tfrac14\big(1\cdot 1 + 3\cdot(-1)\big) = -\tfrac12$, giving
$$L(\chi,0) = -B_{1,\chi} = \tfrac12 \in\mathbb{Q}. \checkmark$$

**What this illustrates.** The whole content of the conjecture is that the *single* invariant $c^\varepsilon$ — here the Gauss sum $2i$ — governs an infinite family of values, and that the parity of $n$ selects which of $c^+, c^-$ appears. For $M_f$ attached to a weight-$k$ cusp form the same bookkeeping gives $L(f,n)\sim(2\pi i)^n u^{(-1)^n}$ for $1\le n\le k-1$, with $u^+u^-$ tied to $\langle f,f\rangle$ up to $K_f^\times$ and an explicit power of $2\pi i$ — the product is accessible by Rankin–Selberg, the individual factors are not, which is precisely the obstruction of §5 in miniature.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*