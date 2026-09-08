---
id: 02-algebra-group-theory/jantzen-sum-formula
title: "Jantzen Sum Formula"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Jantzen Sum Formula

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/jantzen-sum-formula` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Jantzen sum formula is a **theorem**: every Weyl module $V(\lambda)$ for a reductive group $G$ over a field of characteristic $p>0$ (and every Verma module in characteristic $0$) carries a canonical descending filtration whose *alternating* character sum is computable in closed form from root data and $p$-adic valuations.

What is open is everything the formula does not say. The catalog entry tracks three linked questions.

- **(Q1) Layer determination.** The formula gives $\sum_{i>0}\operatorname{ch}V^i(\lambda)$ as a single character. Recovering the individual layers $V^i(\lambda)/V^{i+1}(\lambda)$ — equivalently the decomposition numbers $[V(\lambda):L(\mu)]$ — from it is not possible in general: distinct multiplicity patterns give the same total sum. Determine when the sum formula, plus the multiplicity-one bookkeeping of the linkage principle, suffices.
- **(Q2) Semisimplicity of layers.** Are the layers $V^i(\lambda)/V^{i+1}(\lambda)$ semisimple, and does the Jantzen filtration coincide with the radical (Loewy) filtration of $V(\lambda)$? True in characteristic $0$ for integral regular Verma modules (Beilinson–Bernstein); open for Weyl modules in characteristic $p$ outside restricted small-rank cases.
- **(Q3) Range of the Jantzen conjecture.** The Jantzen conjecture — the filtration is the weight filtration of a mixed Hodge/perverse structure, so layers are semisimple and $\mathrm{ch}\,M^i$ is given by degree-$i$ coefficients of Kazhdan–Lusztig polynomials — is proved for regular integral blocks of category $\mathcal{O}$. Its validity for singular, non-integral, parabolic, affine-critical and modular blocks is not settled.

A complete resolution of (Q2)–(Q3) means: a proof that layers are semisimple with characters given by a specified basis (an honest positivity statement), or an explicit counterexample module.

## 2. Mathematical Foundations

Let $G$ be a connected reductive group over an algebraically closed field $k$ of characteristic $p$, with maximal torus $T$, character lattice $X(T)$, root system $R$, positive roots $R^+$, Weyl group $W$, and $\rho=\frac12\sum_{\alpha\in R^+}\alpha$. For a dominant weight $\lambda\in X(T)^+$ let $V(\lambda)=H^0(\lambda)^*$ be the Weyl module, $L(\lambda)$ its simple head, and $\chi(\mu)$ the Weyl character (Euler characteristic $\sum_i(-1)^i\operatorname{ch}H^i(G/B,\mu)$), defined for all $\mu\in X(T)$ and satisfying the dot-action antisymmetry $\chi(w\cdot\mu)=(-1)^{\ell(w)}\chi(\mu)$, $w\cdot\mu = w(\mu+\rho)-\rho$.

Work over a discrete valuation ring $A$ with residue field $k$, fraction field $K$ of characteristic $0$, uniformizer $\pi$, valuation $\nu$. The Weyl module $V_A(\lambda)$ carries a contravariant $A$-bilinear form $\langle-,-\rangle$, nondegenerate after $\otimes K$. Set
$$V^i(\lambda)=\{\,v\in V_A(\lambda)\ :\ \langle v, V_A(\lambda)\rangle\subseteq \pi^i A\,\}\otimes_A k .$$
This is the **Jantzen filtration** $V(\lambda)=V^0\supseteq V^1\supseteq V^2\supseteq\cdots$, with $V^0/V^1\cong L(\lambda)$ and $V^i=0$ for $i\gg0$.

**Theorem (Jantzen sum formula, 1977; Jantzen's book II.8.19).** For $\lambda\in X(T)^+$,
$$\sum_{i>0}\operatorname{ch}V^i(\lambda)\;=\;\sum_{\alpha\in R^+}\ \sum_{0<mp<\langle\lambda+\rho,\alpha^\vee\rangle}\nu_p(mp)\,\chi\!\left(s_{\alpha,mp}\cdot\lambda\right),$$
where $\nu_p$ is the $p$-adic valuation, and the affine reflection acts by
$$s_{\alpha,mp}\cdot\lambda=\lambda-\big(\langle\lambda+\rho,\alpha^\vee\rangle-mp\big)\alpha .$$

The characteristic-$0$ ancestor is the Verma-module version. For a complex semisimple Lie algebra $\mathfrak g$ and $\lambda\in\mathfrak h^*$, the Verma module $M(\lambda)$ has Jantzen filtration $M(\lambda)=M^0\supseteq M^1\supseteq\cdots$ with $M^1=\operatorname{rad}M(\lambda)$ and
$$\sum_{i>0}\operatorname{ch}M^i(\lambda)=\sum_{\substack{\alpha\in R^+\\ \langle\lambda+\rho,\alpha^\vee\rangle\in\mathbb Z_{>0}}}\operatorname{ch}M(s_\alpha\cdot\lambda).$$
Both statements are shadows of the **Shapovalov determinant** formula: $\det\langle-,-\rangle$ on the weight space $M(\lambda)_{\lambda-\eta}$ equals, up to a nonzero scalar,
$$\prod_{\alpha\in R^+}\prod_{m\ge1}\big(\langle\lambda+\rho,\alpha^\vee\rangle-m\big)^{\,P(\eta-m\alpha)},$$
$P$ the Kostant partition function. Taking $\nu$ of this determinant and grouping terms produces the sum formulas; $\sum_i \dim V^i(\lambda)_\mu = \nu(\det)$ on each weight space.

## 3. History & State of the Art (SOTA)

- **1972.** Shapovalov computes the determinant of the contravariant form on Verma modules, giving the arithmetic input.
- **1974–1977.** Jens Carsten Jantzen introduces the filtration and proves the sum formula, first in the Lie-algebra/Verma setting (*Math. Z.* 140, 1974) and then for Weyl modules of semisimple algebraic groups and their Lie algebras (*J. Algebra* 49, 1977). The 1979 Lecture Notes *Moduln mit einem höchsten Gewicht* is the systematic account.
- **1981.** Klaus Dieter Schaper transports the method to symmetric groups: the **Jantzen–Schaper formula** bounds and often determines decomposition numbers of Specht modules $S^\lambda$ in characteristic $p$.
- **1993.** Beilinson and Bernstein prove the **Jantzen conjectures** for regular integral blocks of category $\mathcal{O}$ via weight filtrations on mixed Hodge modules: the layers are semisimple, and $\operatorname{ch}M^i(\lambda)$ is read off from Kazhdan–Lusztig polynomial coefficients. In particular the Jantzen filtration equals the radical filtration there.
- **1997.** James and Mathas prove a $q$-analogue for Hecke algebras of type $A$; Andersen relates Jantzen-type filtrations to tilting modules and Ext-groups.
- **2000s–2010s.** Quantum-group and affine versions: Kashiwara–Tanisaki's character results at non-critical level; Shan's identification of the Jantzen filtration of standard modules over $v$-Schur algebras with the grading given by canonical bases.
- **2017.** Williamson's *torsion explosion* destroys the naive hope that the modular picture matches the characteristic-$0$ one: Lusztig's character conjecture fails for $p$ far larger than the Coxeter number, so no uniform KL-style formula can control the layers.
- **2018–2019.** Riche–Williamson and Achar–Makisumi–Riche–Williamson give tilting-character formulas in terms of the $p$-canonical basis, the current SOTA framework in which the modular sum formula is now read.

## 4. Partial Results / Verified Cases

- **Verma modules, regular integral blocks of $\mathcal{O}$ for any complex semisimple $\mathfrak g$:** fully solved (Beilinson–Bernstein 1993). Layers semisimple, $= $ radical filtration, characters given by KL polynomials.
- **$G=SL_2$, all $p$, all $\lambda$:** the sum formula determines the whole submodule structure; Weyl modules are multiplicity-free and layers are semisimple.
- **Rank 2 ($SL_3$, $Sp_4$, $G_2$):** Jantzen's and later computations settle the decomposition numbers for all $p$ and all dominant $\lambda$; layers verified semisimple in the restricted region.
- **$p\ge 2h-2$ with $\lambda$ in the Jantzen region** ($\langle\lambda+\rho,\alpha_0^\vee\rangle\le p(p-h+2)$): Lusztig's conjecture holds for $p$ sufficiently large (Andersen–Jantzen–Soergel, Fiebig's explicit bound, Kashiwara–Tanisaki), so the layers are determined by periodic KL polynomials.
- **Symmetric groups $\Sigma_n$:** Jantzen–Schaper determines all decomposition numbers of $S^\lambda$ for $p\ge5$ and $n<4p$ in classical computations, and settles all two-row and hook partitions in every characteristic.
- **$v$-Schur algebras / cyclotomic Hecke algebras at generic parameters:** Shan (2012) identifies the Jantzen filtration with the grading filtration, so layers are semisimple with graded decomposition numbers from canonical bases.
- **Tilting modules:** Andersen (1997) shows the analogous "Andersen filtration" of $\operatorname{Hom}$ spaces has semisimple layers in the quantum case at a root of unity.

## 5. Principal Obstacles

- **Alternating-sum loss.** The formula computes $\sum_{i>0}\operatorname{ch}V^i$, a single virtual character. Two different filtrations, with different layer multiplicities, produce identical totals; the map "layers $\mapsto$ sum" is far from injective once $\sum_i i\cdot[\,\cdot\,]$ has more than one preimage in the linkage class. Beyond rank $2$, and beyond the first alcove, cancellation between $\chi(s_{\alpha,mp}\cdot\lambda)$ terms of opposite sign (via $\chi(w\cdot\mu)=(-1)^{\ell(w)}\chi(\mu)$) hides genuine composition factors.
- **No geometric model in characteristic $p$.** Beilinson–Bernstein's proof runs through mixed Hodge modules and the weight filtration on intersection cohomology, where purity is available. Over $\mathbb F_p$ or in the modular setting there is no weight structure on parity sheaves with the required rigidity: parity sheaves exist (Juteau–Mautner–Williamson) but carry no canonical weight filtration, so the semisimplicity of layers has no source.
- **Torsion explosion.** Williamson's counterexamples show $p$-Kazhdan–Lusztig combinatorics is governed by torsion in the integral cohomology of Schubert varieties, whose growth is at least exponential in the rank. Any formula for layers must encode this torsion; no closed combinatorial expression is expected.
- **Non-integrality and singularity.** For singular $\lambda$ or non-integral blocks, translation functors do not preserve the Jantzen filtration on the nose (they shift indices only up to comparison inequalities), so the standard reduction to the regular integral case breaks.
- **Ext-degeneration.** The relation $\operatorname{Ext}^1(V(\lambda),L(\mu))\cong \operatorname{Hom}(V^1/V^2, L(\mu))$-type statements hold only under semisimplicity hypotheses one is trying to prove; the argument is circular without an independent input.

## 6. The Gap

Proved: the identity of Section 2, for every reductive $G$, every $p$, every dominant $\lambda$ — plus full layer information in the cases of Section 4.

Unproved, general: an assignment $\lambda\mapsto\{\operatorname{ch}(V^i/V^{i+1})\}_{i\ge0}$ consistent with the sum formula. Concretely, the missing step is a **positivity/semisimplicity input in characteristic $p$**: a functor or grading on $\operatorname{Rep}(G)$ whose induced filtration on $V(\lambda)$ provably coincides with the Jantzen filtration and whose layers are semisimple by construction. In characteristic $0$ that input is Hodge-theoretic weights. In characteristic $p$ the candidate is the grading from a Koszul-dual / $p$-canonical-basis description of the principal block; making the two filtrations agree — not merely have the same total character — is the boundary.

## 7. Current Research (as of June 2026)

- **Modular geometric representation theory** (Williamson, Riche, Achar, Makisumi; Sydney, Clermont-Ferrand, LSU). Tilting characters via the $p$-canonical basis are established; the active question is whether the Jantzen filtration is the perverse/grading filtration transported through the Koszul-type equivalence. *(frontier — verify)*
- **Diagrammatic Soergel-bimodule computation** of $p$-KL polynomials in ranks $\le 8$, used to test predicted layer multiplicities against the sum formula as a consistency check.
- **Jantzen filtrations in category $\mathcal{O}$ for Kac–Moody and rational Cherednik algebras** (Shan, Varagnolo, Vasserot and successors): identification of Jantzen with grading filtrations in the cyclotomic case, with extensions to affine level and to $\mathcal O$ for $\mathfrak{gl}_{m|n}$ under study. *(frontier — verify)*
- **Symmetric-group side:** refinements of Jantzen–Schaper via graded Khovanov–Lauda–Rouquier theory, where the Jantzen filtration of a Specht module is compared with its grading filtration; equality is known in special families and conjectural in general. *(frontier — verify)*
- **Computer algebra:** systematic verification of decomposition numbers for exceptional types at small $p$ (Lübeck's tables), which pin the sum formula's predictions in ranges beyond hand computation.

## 8. Future Work

- Construct a modular analogue of the weight filtration on parity sheaves strong enough to force semisimple Jantzen layers, or produce a Weyl module with a non-semisimple layer — the latter would be as informative as a proof.
- Settle the Jantzen conjecture for singular and parabolic blocks of $\mathcal{O}$, where translation-functor arguments currently give only inequalities between filtration indices.
- Determine whether $\mathrm{ch}\,V^i(\lambda)$ for $i\ge2$ admits a $p$-canonical-basis expression with nonnegative coefficients.
- Extend Jantzen–Schaper machinery to all cyclotomic KLR algebras with a proof that the graded and Jantzen filtrations agree.

## 9. Key References

- **[Foundational]** N. N. Shapovalov. *On a bilinear form on the universal enveloping algebra of a complex semisimple Lie algebra.* Functional Analysis and Its Applications 6 (1972), 307–312. [DOI](https://doi.org/10.1007/bf01077650)
- **[Foundational]** J. C. Jantzen. *Zur Charakterformel gewisser Darstellungen halbeinfacher Gruppen und Lie-Algebren.* Mathematische Zeitschrift 140 (1974), 127–149. [DOI](https://doi.org/10.1007/bf01213951)
- **[Foundational]** J. C. Jantzen. *Über das Dekompositionsverhalten gewisser modularer Darstellungen halbeinfacher Gruppen und ihrer Lie-Algebren.* Journal of Algebra 49 (1977), 441–469. [DOI](https://doi.org/10.1016/0021-8693(77)90252-6)
- **[Foundational]** J. C. Jantzen. *Moduln mit einem höchsten Gewicht.* Lecture Notes in Mathematics 750, Springer, 1979. [DOI](https://doi.org/10.1007/bfb0069523)
- **[Reference]** J. C. Jantzen. *Representations of Algebraic Groups*, 2nd edition. Mathematical Surveys and Monographs 107, American Mathematical Society, 2003. (Sum formula: II.8.19.)
- **[Foundational]** A. Beilinson, J. Bernstein. *A proof of Jantzen conjectures.* I. M. Gelfand Seminar, Advances in Soviet Mathematics 16, Part 1, AMS, 1993, 1–50. [DOI](https://doi.org/10.1090/advsov/016.1/01)
- **[Related]** G. James, A. Mathas. *A $q$-analogue of the Jantzen–Schaper theorem.* Proceedings of the London Mathematical Society 74 (1997), 241–274. [DOI](https://doi.org/10.1112/s0024611597000099)
- **[Related]** H. H. Andersen. *Filtrations and tilting modules.* Annales Scientifiques de l'École Normale Supérieure 30 (1997), 353–366. [DOI](https://doi.org/10.1016/s0012-9593(97)89924-7)
- **[SOTA]** P. Shan. *Graded decomposition matrices of $v$-Schur algebras via Jantzen filtration.* Representation Theory 16 (2012), 212–269. [DOI](https://doi.org/10.1090/s1088-4165-2012-00416-2)
- **[SOTA]** G. Williamson. *Schubert calculus and torsion explosion* (with an appendix by A. Kontorovich, P. J. McNamara, G. Williamson). Journal of the American Mathematical Society 30 (2017), 1023–1046. [DOI](https://doi.org/10.1090/jams/868)
- **[SOTA]** S. Riche, G. Williamson. *Tilting modules and the $p$-canonical basis.* Astérisque 397, Société Mathématique de France, 2018. [DOI](https://doi.org/10.24033/ast.1043)
- **[Survey]** A. Mathas. *Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group.* University Lecture Series 15, AMS, 1999. [DOI](https://doi.org/10.1090/ulect/015)

## 10. Worked Example / Concrete Special Case

Take $G=SL_2$, $p=3$, weights identified with $\mathbb Z$ so that $\alpha=2$, $\rho=1$, $\langle\lambda+\rho,\alpha^\vee\rangle=\lambda+1$. Let $\lambda=4$, so $\dim V(4)=5$.

**Right-hand side.** Only $\alpha$ positive root. Need $0<3m<5$: only $m=1$, $mp=3$, $\nu_3(3)=1$. Then
$$s_{\alpha,3}\cdot 4 = 4-(5-3)\cdot\alpha = 4-2\cdot 2=0 .$$
So
$$\sum_{i>0}\operatorname{ch}V^i(4)=1\cdot\chi(0)=\operatorname{ch}L(0).$$

**Reading the layers.** The total is a single simple character, so $V^1(4)\cong L(0)$ and $V^i(4)=0$ for $i\ge2$. Hence $V(4)$ has exactly two composition factors, $L(4)$ and $L(0)$, and $\operatorname{rad}V(4)=L(0)$.

**Independent check.** By Steinberg's tensor product theorem, $L(4)=L(1)\otimes L(1)^{[3]}$, of dimension $2\cdot2=4$. Since $\dim V(4)=5$, the remaining factor has dimension $1$, i.e. $L(0)$. ✓

**Where the method starts to fail.** Take $\lambda=10$, $p=3$: $\langle\lambda+\rho,\alpha^\vee\rangle=11$, and $mp\in\{3,6,9\}$ contribute $\nu_3=1,1,2$ at $s_{\alpha,mp}\cdot 10=10-8\cdot2=-6$, $10-5\cdot2=0$, $10-2\cdot2=6$. Using $\chi(-6)=-\chi(\,s\cdot(-6)\,)$ with $s\cdot(-6)=-6-2\cdot(-5)=4$ gives $\chi(-6)=-\chi(4)$, so
$$\sum_{i>0}\operatorname{ch}V^i(10)=-\chi(4)+\chi(0)+2\chi(6).$$
A negative coefficient appears in the raw expression: the answer is only obtained after rewriting every $\chi(\mu)$ in the basis $\{\operatorname{ch}L(\nu)\}$. For $SL_2$ this rewriting is explicit, so the layers are pinned down. In rank $\ge3$ with $\lambda$ outside the lowest $p^2$-alcove, the number of cancelling terms grows and the same total is compatible with several multiplicity patterns — precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*