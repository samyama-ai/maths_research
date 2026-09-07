---
id: 03-geometry/iitaka-conjecture
title: "Iitaka Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Iitaka Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/iitaka-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $f\colon X \to Y$ be an *algebraic fiber space*: a surjective morphism of smooth complex projective varieties with connected fibers, $\dim X = n$, $\dim Y = m$, $1 \le m < n$. Let $F$ be a general (hence smooth) fiber, $\dim F = n-m$.

**Conjecture $C_{n,m}$ (Iitaka, 1971/72).**
$$\kappa(X) \;\ge\; \kappa(Y) + \kappa(F).$$

Here $\kappa$ is the Kodaira dimension. A complete proof must establish the inequality for all $n > m \ge 1$ over $\mathbb{C}$; a disproof requires one fiber space with $\kappa(X) < \kappa(Y) + \kappa(F)$. Conventions: $\kappa = -\infty$ when all plurigenera vanish, and the inequality is vacuous when $\kappa(Y) = -\infty$ or $\kappa(F) = -\infty$.

Two standard strengthenings:

- **$C^+_{n,m}$ (Viehweg).** $\kappa(X) \ge \kappa(F) + \max\{\kappa(Y),\ \mathrm{Var}(f)\}$, where $\mathrm{Var}(f)$ is the variation, i.e. the number of moduli effectively varying in the family.
- **$C^{\log}_{n,m}$ (Iitaka, logarithmic version).** The same inequality for logarithmic Kodaira dimensions $\bar\kappa$ of open varieties $(X,D) \to (Y,B)$.

## 2. Mathematical Foundations

**Kodaira dimension.** For $X$ smooth projective with canonical divisor $K_X$,
$$\kappa(X) \;=\; \limsup_{k \to \infty} \frac{\log \dim H^0(X, \mathcal{O}_X(kK_X))}{\log k} \;\in\; \{-\infty, 0, 1, \dots, \dim X\},$$
equivalently $\dim \overline{\Phi_{|kK_X|}(X)}$ for $k \gg 0$ divisible, if some plurigenus $P_k = h^0(kK_X)$ is nonzero. $\kappa$ is a birational invariant.

**Iitaka fibration.** For $\kappa(X) = \kappa \ge 1$ there is a birational model and a morphism $\Phi\colon X' \to Z$ with $\dim Z = \kappa$ whose general fiber $G$ satisfies $\kappa(G) = 0$; $C_{n,m}$ is the statement that this structure behaves additively in towers.

**Relative canonical sheaf.** $\omega_{X/Y} = \omega_X \otimes f^*\omega_Y^{-1}$. The basic exact mechanism is
$$H^0(X, k K_X) \;\supseteq\; H^0\!\big(Y,\; f_*\omega_{X/Y}^{\otimes k} \otimes \omega_Y^{\otimes k}\big),$$
so $C_{n,m}$ reduces to producing enough sections of $f_*\omega_{X/Y}^{\otimes k}$, i.e. to *positivity of direct images*.

**Weak positivity (Viehweg).** A torsion-free sheaf $\mathcal{F}$ on $Y$ is weakly positive over an open $U$ if for every ample $H$ and every $\alpha>0$ there is $\beta$ with $\hat{S}^{\alpha\beta}(\mathcal{F}) \otimes \mathcal{O}(\beta H)$ globally generated over $U$.

> **Theorem (Viehweg 1983).** $f_*\omega_{X/Y}^{\otimes k}$ is weakly positive for all $k \ge 1$.

**Canonical bundle formula (Kodaira; Fujino–Mori).** For a fiber space with $\kappa(F) = 0$ and suitable models,
$$K_X \;\sim_{\mathbb{Q}}\; f^*\!\left(K_Y + B_Y + M_Y\right),$$
with $B_Y$ the discriminant (branch/moduli boundary) and $M_Y$ the semi-ample-conjecturally moduli part. For elliptic surfaces this is Kodaira's
$$K_X \;=\; f^*\!\Big(K_Y + L + \textstyle\sum_i (1 - \tfrac{1}{m_i}) P_i\Big), \qquad \deg L = \chi(\mathcal{O}_X).$$

**Reduction of Kawamata.** $C_{n,m}$ for all $n,m$ follows from: (i) $C^+_{n,m}$ with $Y$ of general type, plus (ii) the existence of good minimal models for varieties of Kodaira dimension $\ge 0$ in dimension $n-m$ (equivalently, the abundance conjecture in that dimension).

## 3. History & State of the Art (SOTA)

- **1971–72.** Shigeru Iitaka introduces $D$-dimensions and the classification program; states $C_{n,m}$ (Iitaka, *On $D$-dimensions of algebraic varieties*, J. Math. Soc. Japan 23, 1971).
- **1975.** Ueno's LNM 439 codifies the conjecture and the Iitaka program; $C_{2,1}$ is classical from the Enriques–Kodaira classification of surfaces.
- **1977.** Viehweg proves $C_{n,n-1}$ — relative dimension one — via a covering trick plus Hodge-theoretic positivity of $f_*\omega_{X/Y}$ (Fujita, Kawamata).
- **1981–82.** Kawamata proves $C_{n,1}$ (base a curve), using the semipositivity of Hodge bundles and Kawamata's covering construction.
- **1983–85.** Viehweg proves $C^+_{n,m}$ when $Y$ is of general type; Kawamata reduces the general case to the minimal model / abundance conjecture.
- **1987.** Kollár proves $C_{n,m}$ when the general fiber $F$ is of general type.
- **2009.** Birkar establishes $C_{n,m}$ for $n \le 6$ using progress in the MMP.
- **2017–18.** Cao–Păun prove $C_{n,m}$ when $Y$ is an abelian variety, by $L^2$/Ohsawa–Takegoshi methods and singular Hermitian metrics on $f_*\omega_{X/Y}^{\otimes k}$; Hacon–Popa–Schnell extend to $Y$ of maximal Albanese dimension. Cao proves the case $\dim Y = 2$ under mild hypotheses.

**Status:** open in general; proven in a wide, structured list of cases (Section 4). Conditional on abundance in dimension $n-m$, it is a theorem.

## 4. Partial Results / Verified Cases

| Case | Author, year |
|---|---|
| $n \le 2$ (i.e. $C_{2,1}$) | Enriques–Kodaira classification |
| $C_{n,1}$: base a curve, all $n$ | Kawamata 1982 |
| $C_{n,n-1}$: relative dimension $1$, all $n$ | Viehweg 1977 |
| $Y$ of general type ($\kappa(Y)=\dim Y$), incl. $C^+$ | Viehweg 1983 |
| $F$ of general type | Kollár 1987 |
| $F$ admits a good minimal model | Kawamata 1985 (reduction) |
| $n \le 6$, all $m$ | Birkar 2009 |
| $Y$ abelian variety | Cao–Păun 2017 |
| $Y$ of maximal Albanese dimension | Hacon–Popa–Schnell 2018 |
| $\dim Y = 2$ (surface base), $\kappa(Y)\ge 0$ | Cao 2018 |
| $\kappa(Y) = \dim Y$ or $\kappa(F) \in \{-\infty\}$ | trivial/covered above |
| Logarithmic $C^{\log}_{n,n-1}$ and $C^{\log}_{n,1}$ | Fujino 2014, Kawamata 1981 |
| Char. $p>0$, relative dimension $1$, $n=3$ | Chen–Zhang 2015; Ejiri, Zhang (subsequent) |

Together these cover every fiber space with $n\le 6$, every base of dimension $\le 2$ with $\kappa \ge 0$, every base with maximal Albanese dimension, and every fiber of general type or with a good minimal model. The first genuinely open configurations are $n = 7$ with $3 \le m \le 4$ and fibers of intermediate Kodaira dimension.

## 5. Principal Obstacles

- **Abundance.** The reduction is complete *modulo* the existence of good minimal models for the fibers: one needs $\kappa(F) \ge 0 \Rightarrow$ $F$ has a minimal model with $K$ semi-ample. Abundance is known only up to dimension $3$ (Miyaoka, Kawamata) plus special cases; it is the hard core.
- **The moduli part $M_Y$ is only conjecturally semi-ample.** In the canonical bundle formula, $M_Y$ is nef (Fujino–Mori, via variations of Hodge structure) but semi-ampleness — needed to convert nefness into sections — is open beyond low-dimensional bases. Nef $\ne$ effective on non-general-type bases.
- **Positivity is too weak when $\kappa(Y)=0$.** Weak positivity of $f_*\omega_{X/Y}^{\otimes k}$ gives sections after twisting by an ample; if $K_Y$ is only torsion (abelian, Calabi–Yau bases) the twist cannot be absorbed. Cao–Păun broke this exactly for abelian $Y$ using flat unitary decompositions of the metric; the argument uses the group structure (translation-invariance, generic vanishing) and does not port to a general Calabi–Yau base.
- **Hodge theory sees only variation, not fiber geometry.** Semipositivity of $R^{n-m}f_*\omega_{X/Y}$ controls $\mathrm{Var}(f)$; when the family is isotrivial ($\mathrm{Var}=0$) with $\kappa(F)$ intermediate, Hodge-theoretic input degenerates and one must instead descend pluricanonical sections along the fiber's own Iitaka fibration — a step that requires abundance.
- **Iterating fibrations loses smoothness.** Composing $X\to Y \to Z$ forces base change and resolution; the resulting singular/log pairs demand the log version $C^{\log}$, which is itself weaker-known.

## 6. The Gap

Proved: $C_{n,m}$ whenever the fiber's canonical ring is understood ($F$ of general type, $\dim F \le 3$, or $F$ with a good minimal model) **or** the base is positive enough ($\kappa(Y)=\dim Y$, or $Y$ abelian / maximal Albanese dimension, or $\dim Y \le 2$).

Missing: the middle regime — $\kappa(F)$ strictly between $0$ and $\dim F$ with $\dim F \ge 4$, over a base with $0 \le \kappa(Y) < \dim Y$ that is *not* of maximal Albanese dimension (e.g. a simply connected Calabi–Yau threefold base). Concretely, the single step to cross is:

> Show that $M_Y$ in the canonical bundle formula is $\mathbb{Q}$-effective (semi-ample suffices), without assuming $K_Y$ big;

equivalently, prove abundance in dimension $n-m$. Everything else in the reduction is unconditional.

## 7. Current Research (as of June 2026)

- **Analytic positivity school (Păun, Cao, Takayama, Deng, Hacon–Popa–Schnell).** Singular Hermitian metrics on $f_*\omega_{X/Y}^{\otimes k}$ with Ohsawa–Takegoshi extension; the live target is replacing "abelian base" by "$K_Y \equiv 0$" or "$Y$ Calabi–Yau", using flat-bundle decompositions and Numerical Nonvanishing. *(frontier — verify)*
- **Generic vanishing / Fourier–Mukai (Popa, Schnell, Meng).** Hodge-module-theoretic generic vanishing for $f_*\omega_{X/Y}^{\otimes k}$ over irregular bases; extensions to bases with non-abelian Albanese image.
- **MMP route (Birkar, Hacon, Xu, Fujino).** Abundance for klt pairs in dimension $4$–$5$ and semi-ampleness of moduli b-divisors in higher-dimensional base; each increment mechanically raises the unconditional bound on $n$.
- **Positive characteristic (Ejiri, Zhang, Patakfalvi).** $C_{n,m}$ fails in char $p$ in general (Moret-Bailly-type counterexamples via non-smooth generic fibers); current work isolates hypotheses (separable, geometrically canonical fibers, $F$-splitting) restoring subadditivity.
- **Kähler / non-algebraic setting (Fujino, Cao, Horing).** Subadditivity for fiber spaces of compact Kähler manifolds, following the Kähler MMP.

## 8. Future Work

- Prove semi-ampleness of the moduli part $M_Y$ for fibrations with fiber Kodaira dimension $0$ over bases of dimension $\ge 3$ — the cleanest self-contained sub-goal.
- Extend Cao–Păun to bases with $K_Y \equiv 0$ (Beauville–Bogomolov decomposition splits such $Y$ into abelian, Calabi–Yau, and hyperkähler factors; the abelian factor is done, the other two are not).
- Push abundance one dimension at a time; $n\le 6$ becomes $n \le 7,8$ automatically.
- Settle $C^{\log}_{n,m}$ in relative dimension $2$, which would close the open-variety analogue for surface fibers.
- Formulate and test an orbifold/Campana version $\kappa(X) \ge \kappa(Y, \Delta_f) + \kappa(F)$, where $\Delta_f$ is the multiple-fiber orbifold divisor; Campana argues this is the "right" statement and it implies $C_{n,m}$.

## 9. Key References

- **[Foundational]** S. Iitaka. *On $D$-dimensions of algebraic varieties.* Journal of the Mathematical Society of Japan **23** (1971), 356–373.
- **[Foundational]** K. Ueno. *Classification Theory of Algebraic Varieties and Compact Complex Spaces.* Lecture Notes in Mathematics 439, Springer, 1975.
- **[Foundational]** E. Viehweg. *Canonical divisors and the additivity of the Kodaira dimension for morphisms of relative dimension one.* Compositio Mathematica **35** (1977), 197–223.
- **[Foundational]** Y. Kawamata. *Kodaira dimension of algebraic fiber spaces over curves.* Inventiones Mathematicae **66** (1982), 57–71.
- **[Foundational]** E. Viehweg. *Weak positivity and the additivity of the Kodaira dimension II: The local Torelli map.* In *Classification of Algebraic and Analytic Manifolds*, Progress in Mathematics 39, Birkhäuser, 1983, 567–589.
- **[Foundational]** Y. Kawamata. *Minimal models and the Kodaira dimension of algebraic fiber spaces.* Journal für die reine und angewandte Mathematik **363** (1985), 1–46.
- **[Foundational]** J. Kollár. *Subadditivity of the Kodaira dimension: fibers of general type.* Advanced Studies in Pure Mathematics **10** (1987), 361–398.
- **[SOTA / Recent]** C. Birkar. *The Iitaka conjecture $C_{n,m}$ in dimension six.* Compositio Mathematica **145** (2009), 1442–1446.
- **[SOTA / Recent]** J. Cao, M. Păun. *Kodaira dimension of algebraic fiber spaces over abelian varieties.* Inventiones Mathematicae **207** (2017), 345–387.
- **[SOTA / Recent]** C. Hacon, M. Popa, C. Schnell. *Algebraic fiber spaces over abelian varieties: around a recent theorem by Cao and Păun.* Contemporary Mathematics **712**, AMS, 2018, 143–195.
- **[SOTA / Recent]** J. Cao. *Kodaira dimension of algebraic fiber spaces over surfaces.* Algebraic Geometry **5** (2018), 728–741.
- **[SOTA / Recent]** Y. Chen, L. Zhang. *The subadditivity of the Kodaira dimension for fibrations of relative dimension one in positive characteristics.* Mathematical Research Letters **22** (2015), 675–696.
- **[Survey]** O. Fujino. *Iitaka conjecture — An introduction.* SpringerBriefs in Mathematics, Springer, 2020.
- **[Survey]** M. Popa. *D-modules in birational geometry.* Proceedings of the ICM 2018, Vol. II, 781–806.
- **[Survey]** J. Kollár, S. Mori. *Birational Geometry of Algebraic Varieties.* Cambridge Tracts in Mathematics 134, CUP, 1998.

## 10. Worked Example / Concrete Special Case

**Setting.** $C_{2,1}$ for an elliptic surface over an elliptic curve. Let $f\colon X \to Y$ be a relatively minimal elliptic fibration, $Y$ an elliptic curve, general fiber $F$ a smooth elliptic curve. Then $\kappa(Y)=0$, $\kappa(F)=0$, so $C_{2,1}$ predicts $\kappa(X) \ge 0$.

**Kodaira's canonical bundle formula.**
$$K_X \;=\; f^*\!\Big(K_Y + L + \sum_{i=1}^{s}\big(1 - \tfrac{1}{m_i}\big)P_i\Big),$$
where $\deg L = \chi(\mathcal{O}_X) \ge 0$ and $m_1,\dots,m_s \ge 2$ are the multiplicities of the multiple fibers over points $P_i \in Y$.

**Computation.** $K_Y = 0$ since $Y$ is elliptic. Set
$$d \;=\; \deg\Big(K_Y + L + \sum_i (1-\tfrac1{m_i})P_i\Big) \;=\; \chi(\mathcal{O}_X) + \sum_{i=1}^{s}\Big(1-\frac{1}{m_i}\Big).$$
Each term is $\ge 0$ and $1 - 1/m_i \ge 1/2$, so $d \ge 0$ always. Hence:

- If $d > 0$: the $\mathbb{Q}$-divisor is ample on the curve $Y$, so $|kK_X| = f^*|k(\cdots)|$ grows linearly and $\kappa(X) = 1$.
- If $d = 0$: forced $\chi(\mathcal{O}_X)=0$ and $s=0$, so $K_X = f^*(\text{degree-}0\text{ divisor})$, which is torsion in $\mathrm{Pic}^0(Y)$ on the relevant models; then $P_k(X)=1$ for suitable $k$ and $\kappa(X)=0$. (This is the bielliptic/quasi-bundle case, e.g. $X = (E_1 \times E_2)/G$ with $G$ acting by translations and automorphisms.)

Either way $\kappa(X) \ge 0 = \kappa(Y)+\kappa(F)$: the conjecture holds, and both equality ($d=0$) and strict inequality ($d>0$) occur.

**Where the general case breaks.** The proof used exactly two facts unavailable in high dimension: the moduli part $L$ is a genuine line bundle of computable degree $\chi(\mathcal{O}_X)$, and "nef $=$ effective" on a curve. Replace $Y$ by a Calabi–Yau threefold: $M_Y$ is nef by Fujino–Mori but need not be visibly $\mathbb{Q}$-effective, and $K_Y \equiv 0$ gives no ample to absorb into weak positivity — precisely the gap in Section 6.

**$C^+$ in action.** Take instead a non-isotrivial genus-$2$ fibration $g\colon S \to E$ over an elliptic curve (necessarily with singular fibers, by Arakelov). Here $\kappa(F)=1$, $\kappa(E)=0$, $\mathrm{Var}(g)=1$, so $C_{2,1}$ gives only $\kappa(S)\ge 1$, while Viehweg's $C^+$ gives $\kappa(S) \ge \kappa(F)+\mathrm{Var}(g) = 2$: $S$ is of general type. This shows the variation term carries strictly more information than $\kappa(Y)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*