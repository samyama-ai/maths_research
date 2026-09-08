---
id: 05-analysis/leopoldt-conjecture
title: "Leopoldt Conjecture"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Leopoldt Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/leopoldt-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $K$ be a number field of degree $n = [K:\mathbb{Q}]$ with $r_1$ real and $r_2$ complex places, and let $p$ be a prime. Dirichlet's unit theorem gives $\operatorname{rank}_{\mathbb{Z}} \mathcal{O}_K^\times = r = r_1 + r_2 - 1$. Embedding the units into the semilocal completion at $p$ and applying the $p$-adic logarithm produces a $p$-adic regulator $R_p(K)$, an $r \times r$ determinant.

**Conjecture (Leopoldt, 1962).** For every number field $K$ and every prime $p$,
$$R_p(K) \neq 0,$$
equivalently: the units of $K$, viewed $p$-adically, remain $\mathbb{Z}_p$-linearly independent — they span a $\mathbb{Z}_p$-module of rank exactly $r$, not less.

The **Leopoldt defect** is $\delta_{K,p} = r - \operatorname{rank}_{\mathbb{Z}_p} \overline{\mathcal{O}_K^\times}$. Always $\delta_{K,p} \ge 0$; the conjecture says $\delta_{K,p} = 0$. A proof must handle all $K$ and all $p$; a disproof needs one explicit pair $(K,p)$ with a certified vanishing determinant — and certifying a $p$-adic vanishing numerically is impossible, since computation only ever yields $|R_p| \le p^{-N}$.

The analytic content is a **$p$-adic transcendence** statement: a nontrivial $\mathbb{Z}_p$-linear relation among $p$-adic logarithms of algebraic numbers, with *$p$-adic* (not algebraic) coefficients, is exactly what must be excluded. This is why the problem lives in $p$-adic analysis rather than in pure algebra.

## 2. Mathematical Foundations

Write $K \otimes_{\mathbb{Q}} \mathbb{Q}_p \cong \prod_{v \mid p} K_v$, and let
$$\mathcal{U} = \prod_{v \mid p} \mathcal{O}_{K_v}^\times, \qquad \iota: \mathcal{O}_K^\times \longrightarrow \mathcal{U}$$
be the diagonal embedding. The Iwasawa $p$-adic logarithm $\log_p: \mathcal{O}_{K_v}^\times \to K_v$ is defined by $\log_p(1+x) = \sum_{k\ge1} (-1)^{k-1}x^k/k$ on principal units and extended by $\log_p(\zeta) = 0$ for roots of unity and $\log_p(p) = 0$. Its kernel on $\mathcal{O}_{K_v}^\times$ is exactly the group of roots of unity of order prime to nothing beyond torsion: $\log_p(u) = 0 \iff u \in \mu(K_v)$.

Fix fundamental units $\varepsilon_1,\dots,\varepsilon_r$ and the $n$ embeddings $\sigma_1,\dots,\sigma_n : K \hookrightarrow \overline{\mathbb{Q}}_p$. The $p$-adic regulator is
$$R_p(K) = \det\Big( \log_p \sigma_i(\varepsilon_j) \Big)_{1 \le i,j \le r},$$
any $r$ of the $n$ embeddings being deleted-and-normalized as in the archimedean case (the product formula $\sum_i \log_p\sigma_i(\varepsilon) = \log_p N_{K/\mathbb{Q}}(\varepsilon) = 0$ makes the choice immaterial up to sign). Then
$$\delta_{K,p} = r - \operatorname{rank}_{\mathbb{Z}_p}\big(\mathbb{Z}_p\text{-span of } \iota(\mathcal{O}_K^\times)\big), \qquad \text{Leopoldt} \iff R_p(K) \ne 0 \iff \delta_{K,p} = 0 .$$

**Galois-theoretic form.** Let $\tilde{K}$ be the compositum of all $\mathbb{Z}_p$-extensions of $K$. Class field theory plus the above gives
$$\operatorname{rank}_{\mathbb{Z}_p} \operatorname{Gal}(\tilde K / K) = r_2 + 1 + \delta_{K,p}.$$
Leopoldt is the statement that $K$ admits exactly $r_2+1$ independent $\mathbb{Z}_p$-extensions. Equivalently, with $M$ the maximal abelian pro-$p$ extension of $K$ unramified outside $p$, $\operatorname{Gal}(M/K)$ has $\mathbb{Z}_p$-rank $r_2+1$, and equivalently $H^2(G_S(K), \mathbb{Q}_p/\mathbb{Z}_p)$-type cohomological vanishing holds for $S = \{v \mid p\infty\}$ (Neukirch–Schmidt–Wingberg, Ch. X).

**Analytic form (totally real $K$).** Colmez's residue formula states that the $p$-adic zeta function $\zeta_{p,K}(s)$ satisfies
$$\operatorname{Res}_{s=1} \zeta_{p,K}(s) = \frac{2^{r_1-1} h_K R_p(K)}{\sqrt{|d_K|}} \prod_{v \mid p}\left(1 - \frac{1}{N v}\right),$$
so Leopoldt for totally real $K$ is *exactly* the assertion that $\zeta_{p,K}$ has a genuine simple pole at $s=1$ — the $p$-adic mirror of $\zeta_K(s)$'s pole.

## 3. History & State of the Art (SOTA)

- **1962.** Heinrich-Wolfgang Leopoldt, *Zur Arithmetik in abelschen Zahlkörpern*, formulates the non-vanishing while constructing $p$-adic $L$-functions of abelian fields; the conjecture is what is needed for the $p$-adic class number formula to be non-degenerate.
- **1965–67.** James Ax and, independently, Armand Brumer prove the conjecture for $K$ abelian over $\mathbb{Q}$, and Brumer for $K$ abelian over an imaginary quadratic field. The engine is Baker's method transposed to the $p$-adic setting: **Baker–Brumer theorem** — $\overline{\mathbb{Q}}$-linearly independent $p$-adic logarithms of algebraic numbers are $\overline{\mathbb{Q}}$-linearly independent. Abelian fields let Galois equivariance replace the $\mathbb{Z}_p$-coefficients by algebraic (character-value) coefficients.
- **1981–84.** Waldschmidt's quantitative $p$-adic transcendence gives an unconditional lower bound for the $p$-adic unit rank valid for *all* $K$: roughly half the full rank.
- **1988.** Colmez proves the residue formula, tying the totally real case to $p$-adic $L$-values.
- **1980s–2000s.** Iwasawa-theoretic reformulations (Coates, Greenberg, Nguyen Quang Do, Jaulent) recast Leopoldt as a cohomological or "cyclotomic norm" statement and link it to the Gross–Kuz'min conjecture.
- **2009–present.** Preparata-style descent and $\Lambda$-module arguments by Preda Mihăilescu claim a general proof; the manuscripts remain unrefereed and unaccepted. *(frontier — verify)*

No non-abelian field of degree $\ge 3$ outside the Ax–Brumer families has been settled unconditionally.

## 4. Partial Results / Verified Cases

| Class | Status |
|---|---|
| $K = \mathbb{Q}$, imaginary quadratic $K$ | Trivial: $r = 0$, empty determinant |
| $K/\mathbb{Q}$ abelian (all $p$) | **Proved** (Ax 1965, Brumer 1967) |
| $K$ abelian over an imaginary quadratic field | **Proved** (Brumer 1967) |
| Subfields of the above (any degree) | **Proved** — the defect is inherited downward: $\delta_{K,p} \le \delta_{L,p}$ for $K \subset L$ |
| $K$ totally real of degree $n$, general | **Open** for $n \ge 3$ non-abelian, e.g. the totally real cubic of discriminant $257$ (Galois group $S_3$, non-abelian over $\mathbb{Q}$) |
| General $K$, all $p$ | $\operatorname{rank}_{\mathbb{Z}_p} \overline{\mathcal{O}_K^\times} \ge \tfrac{1}{2}(r_1+r_2)$, so $\delta_{K,p} \le \tfrac{1}{2}(r_1+r_2) - 1$ (Waldschmidt 1984; refined by Emsalem–Kisilevsky–Wales 1984) |
| $K$ with $r = 1$ (real quadratic, complex cubic, totally imaginary quartic) | **Proved** unconditionally: $\delta \le \tfrac12(r_1+r_2)-1 < 1$ forces $\delta = 0$ |
| Computational | For thousands of fields of degree $\le 8$ and small $p$, $v_p(R_p(K))$ is computed to be small and finite; this *verifies no case*, only bounds $\delta$'s absence from view |

The $r = 1$ row is the sharpest unconditional general statement: Waldschmidt's bound alone kills the conjecture for every field of unit rank one, including all real quadratic fields, for every prime.

## 5. Principal Obstacles

- **Coefficients are $p$-adic, not algebraic.** Baker–Brumer excludes relations $\sum a_i \log_p \alpha_i = 0$ with $a_i \in \overline{\mathbb{Q}}$. Leopoldt must exclude relations with $a_i \in \mathbb{Z}_p$, and $\mathbb{Z}_p$ has uncountable transcendence degree over $\mathbb{Q}$. The abelian case escapes only because a Galois character basis converts the $\mathbb{Z}_p$-relation into an algebraic one; no such conversion exists for a non-abelian or non-Galois $K$.
- **No $p$-adic Schanuel.** Leopoldt follows from a $p$-adic analogue of Schanuel's conjecture, itself far out of reach. Current transcendence measures produce rank *lower bounds* proportional to $\sqrt{}$- or $\tfrac12$-fractions of $r$; pushing the constant from $1/2$ to $1$ is a known hard wall in linear forms in logarithms, not a technicality.
- **Determinant vs. individual logarithms.** $R_p$ can vanish with every entry non-zero. Bounding a single $|\log_p \sigma(\varepsilon)|$ from below is feasible; bounding an $r\times r$ determinant requires uniform control over all minors, and the archimedean tool for this (Minkowski / geometry of numbers) has no $p$-adic counterpart with a comparable non-degeneracy input.
- **No Archimedean positivity.** Over $\mathbb{R}$, the regulator is a Gram-type determinant of a positive-definite form, hence non-zero for free. $\mathbb{Q}_p$ carries no ordering and no positive-definiteness, so the standard proof of $R_\infty \ne 0$ has no analogue.
- **Iwasawa reformulations are circular in practice.** Recasting Leopoldt as $H^2$-vanishing or as "no exotic $\mathbb{Z}_p$-extension" is exact but transfers the difficulty; every known route to the cohomological statement re-imports a transcendence input.

## 6. The Gap

Proven: $\delta_{K,p} \le \tfrac12(r_1+r_2)-1$ for all $K$, and $\delta_{K,p}=0$ when the Galois action diagonalizes the unit lattice over $\overline{\mathbb{Q}}_p$ into one-dimensional character spaces (abelian case). Claimed: $\delta_{K,p}=0$ always.

The precise barrier: for a non-abelian $K$, the $\mathbb{Q}_p[\operatorname{Gal}]$-module $\mathcal{O}_K^\times \otimes \mathbb{Q}_p$ has irreducible constituents of dimension $\ge 2$. Inside such a constituent, a hypothetical relation among the $\log_p \sigma_i(\varepsilon_j)$ has coefficients that are only constrained to lie in a $p$-adic division algebra, not in $\overline{\mathbb{Q}}$. Closing the gap means proving: *no $\mathbb{Z}_p$-linear relation among $p$-adic logarithms of global units exists that is not already an algebraic one.* Equivalently, raise the Waldschmidt constant from $1/2$ to $1$, uniformly in $K$ and $p$.

## 7. Current Research (as of June 2026)

- **Mihăilescu's program** (Göttingen). A series of arXiv preprints (from 2009) develops $T$- and $T^*$-components of Iwasawa $\Lambda$-modules and claims a full proof. Not published or accepted by the community after more than a decade of circulation. *(frontier — verify)*
- **Jaulent's logarithmic class field theory** (Bordeaux). The "logarithmic class group" $\widetilde{C\ell}_K$ packages Leopoldt and Gross–Kuz'min uniformly; recent work computes it algorithmically (PARI/GP `bnflog`), yielding large families where Gross–Kuz'min is verified and Leopoldt-type defects are constrained.
- **$p$-adic $L$-function side.** Following Colmez, work on Hilbert modular Eisenstein cohomology and Dasgupta–Kakde style constructions of totally real $p$-adic $L$-functions gives new handles on $\operatorname{Res}_{s=1}\zeta_{p,K}$, but so far only conditionally.
- **Transcendence side.** Refinements of $p$-adic Baker bounds (Yu Kunrui's linear forms in $p$-adic logarithms) improve constants but not the $1/2 \to 1$ threshold.
- **Explicit computation.** Certified upper bounds on $v_p(R_p(K))$ for number fields of degree $\le 9$, used to rule out small-height counterexamples and to test Greenberg-type conjectures.

## 8. Future Work

- Prove a $p$-adic Schanuel statement restricted to *global units* — a strictly weaker target than full $p$-adic Schanuel, and enough for Leopoldt.
- Extend Ax–Brumer by Brauer induction: reduce a monomial (M-group) Galois closure to abelian subfields. The obstruction is that induction gives non-vanishing of a *product* of regulators only up to unknown $p$-adic units; identifying a well-behaved integral Artin formalism for $R_p$ is the concrete target.
- Attack the totally real case analytically: prove directly that $\zeta_{p,K}(s)$ has a pole at $s=1$ using the $p$-adic Eisenstein-cohomology construction, bypassing units.
- Settle Gross–Kuz'min in the non-abelian case and clarify whether it can be leveraged toward Leopoldt via Jaulent's logarithmic formalism.
- Referee or refute the Mihăilescu manuscripts; the community would benefit from a definitive verdict.

## 9. Key References

- **[Foundational]** H.-W. Leopoldt. *Zur Arithmetik in abelschen Zahlkörpern.* Journal für die reine und angewandte Mathematik **209** (1962), 54–71. [DOI](https://doi.org/10.1515/crll.1962.209.54)
- **[Foundational]** J. Ax. *On the units of an algebraic number field.* Illinois Journal of Mathematics **9** (1965), 584–589. [DOI](https://doi.org/10.1215/ijm/1256059299)
- **[Foundational]** A. Brumer. *On the units of algebraic number fields.* Mathematika **14** (1967), 121–124.
- **[Foundational]** A. Baker. *Linear forms in the logarithms of algebraic numbers.* Mathematika **13** (1966), 204–216. [DOI](https://doi.org/10.1112/s0025579300003971)
- **[SOTA]** M. Waldschmidt. *A lower bound for the $p$-adic rank of the units of an algebraic number field.* In *Topics in Classical Number Theory* (Budapest, 1981), Colloq. Math. Soc. János Bolyai **34**, North-Holland, 1984, 1617–1650.
- **[SOTA]** M. Emsalem, H. Kisilevsky, D. Wales. *Indépendance linéaire sur $\overline{\mathbb{Q}}$ de logarithmes $p$-adiques de nombres algébriques et rang $p$-adique du groupe des unités d'un corps de nombres.* Journal of Number Theory **19** (1984), 384–391. [DOI](https://doi.org/10.1016/0022-314x(84)90079-9)
- **[SOTA]** P. Colmez. *Résidu en $s=1$ des fonctions zêta $p$-adiques.* Inventiones Mathematicae **91** (1988), 371–389.
- **[SOTA]** H. Miki. *On the Leopoldt conjecture on the $p$-adic regulators.* Journal of Number Theory **26** (1987), 117–128. [DOI](https://doi.org/10.1016/0022-314x(87)90073-4)
- **[Recent]** J.-F. Jaulent. *Sur les normes cycliques et les conjectures de Leopoldt et de Gross–Kuz'min.* Annales mathématiques du Québec **41** (2017), 119–140. [DOI](https://doi.org/10.1007/s40316-016-0069-3)
- **[Survey]** L. C. Washington. *Introduction to Cyclotomic Fields*, 2nd ed., Graduate Texts in Mathematics **83**, Springer, 1997 (§5.5).
- **[Survey]** J. Neukirch, A. Schmidt, K. Wingberg. *Cohomology of Number Fields*, 2nd ed., Springer, 2008 (Chapter X).
- **[Frontier]** P. Mihăilescu. *The $T$ and $T^\ast$ components of $\Lambda$-modules and Leopoldt's conjecture.* arXiv preprint, 2009. *(frontier — verify)*

## 10. Worked Example / Concrete Special Case

Take $K = \mathbb{Q}(\sqrt{2})$ and $p = 7$. Here $r_1 = 2$, $r_2 = 0$, $r = 1$, fundamental unit $\varepsilon = 1+\sqrt{2}$ with $N_{K/\mathbb{Q}}(\varepsilon) = -1$.

**Splitting.** $2$ is a square mod $7$ ($3^2 = 9 \equiv 2$), so $7$ splits: $7\mathcal{O}_K = \mathfrak{p}_1\mathfrak{p}_2$, $K_{\mathfrak{p}_i} \cong \mathbb{Q}_7$.

**Hensel lift of $\sqrt2$.** Seek $\alpha \in \mathbb{Z}_7$ with $\alpha^2 = 2$, $\alpha \equiv 3 \pmod 7$. Put $\alpha = 3+7t$: $\alpha^2 = 9 + 42t + 49t^2 \equiv 2 + 7(1+6t) \pmod{49}$, so $1+6t \equiv 0 \pmod 7 \Rightarrow t \equiv 1$. Hence $\alpha \equiv 10 \pmod{49}$.

**The regulator.** $R_7(K) = \log_7 \sigma_1(\varepsilon) = \log_7(1+\alpha)$, a $1\times1$ determinant. Leopoldt for $(K,7)$ says $\log_7(1+\alpha) \ne 0$, i.e. $1+\alpha$ is not a root of unity in $\mathbb{Z}_7^\times$, i.e. $(1+\alpha)^6 \ne 1$.

**Check.** $1+\alpha \equiv 11 \pmod{49}$. Then
$$11^2 = 121 \equiv 23, \quad 11^3 \equiv 23\cdot 11 = 253 \equiv 8, \quad 11^6 \equiv 8^2 = 64 \equiv 15 \pmod{49}.$$
Since $15 \not\equiv 1 \pmod{49}$, $1+\alpha \notin \mu_6$, so $\log_7(1+\alpha) \ne 0$ and $R_7(\mathbb{Q}(\sqrt2)) \ne 0$. In fact $v_7(\log_7(1+\alpha)) = 1$, since $(1+\alpha)^6 = 1 + 7u$ with $u \not\equiv 0$.

**What generalizes and what does not.** This case is safe for two independent reasons: $K$ is abelian over $\mathbb{Q}$ (Ax–Brumer), and $r=1$ so Waldschmidt's bound $\delta \le \tfrac12(r_1+r_2)-1 = 0$ already forces $\delta = 0$. Now replace $K$ by the totally real cubic field of discriminant $257$ (Galois group $S_3$ over $\mathbb{Q}$). There $r = 2$, and $R_p$ is a genuine $2\times2$ determinant $\log_p\sigma_1(\varepsilon_1)\log_p\sigma_2(\varepsilon_2) - \log_p\sigma_2(\varepsilon_1)\log_p\sigma_1(\varepsilon_2)$. Waldschmidt gives only $\delta \le 0.5$, which does round down to $0$ — but at $r=3$ (e.g. totally real quartics) the bound gives $\delta \le 1$ and stops deciding. No amount of $7$-adic digit computation can settle such a case: computing $R_p$ to $10^6$ digits and finding it non-zero proves the case; finding it $\equiv 0$ to $10^6$ digits proves nothing. That asymmetry is the whole difficulty.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*