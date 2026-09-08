---
id: 05-analysis/selberg-eigenvalue-conjecture
title: "Selberg Eigenvalue Conjecture"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Selberg Eigenvalue Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/selberg-eigenvalue-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\Gamma(N) \subset \mathrm{SL}_2(\mathbb{Z})$ be the principal congruence subgroup of level $N$, acting on the upper half-plane $\mathbb{H} = \{z = x+iy : y > 0\}$ with the hyperbolic metric $ds^2 = (dx^2+dy^2)/y^2$. Let $\Delta = -y^2(\partial_x^2 + \partial_y^2)$ be the (positive) Laplace–Beltrami operator on $L^2(\Gamma(N)\backslash\mathbb{H})$, and let

$$\lambda_1(N) = \inf\{\lambda > 0 : \lambda \in \operatorname{spec}\Delta \text{ on } L^2(\Gamma(N)\backslash\mathbb{H})\}$$

be the smallest nonzero eigenvalue of the discrete (cuspidal) spectrum.

**Conjecture (Selberg, 1965).** For every $N \ge 1$,
$$\lambda_1(N) \ \ge \ \tfrac14 .$$

Equivalently: no congruence quotient of $\mathbb{H}$ has an **exceptional eigenvalue**, i.e. a cuspidal eigenvalue strictly between $0$ and the bottom $1/4$ of the continuous spectrum. The same statement is conjectured for $\Gamma_0(N)$ and $\Gamma_1(N)$ with arbitrary nebentypus, and for congruence subgroups of $\mathrm{SL}_2(\mathcal{O}_K)$ over a number field $K$.

A complete proof must handle all levels $N$ uniformly; a disproof requires exhibiting one congruence subgroup and one cuspidal Maass form with $0 < \lambda < 1/4$. The bound $1/4$ is sharp in the sense that it cannot be improved: for each $N$ there are eigenvalues accumulating only above $1/4$, and $1/4$ itself is attained in limit by the continuous spectrum.

## 2. Mathematical Foundations

**Maass forms.** A *Maass cusp form* of level $N$, weight $0$, nebentypus $\chi$ is a smooth $f:\mathbb{H}\to\mathbb{C}$ with $f(\gamma z) = \chi(d) f(z)$ for $\gamma = \begin{psmallmatrix} a&b\\ c&d\end{psmallmatrix}\in\Gamma_0(N)$, satisfying $\Delta f = \lambda f$, square-integrable, and vanishing at every cusp. Write the **spectral parameter** $r$ by
$$\lambda = \tfrac14 + r^2 = s(1-s), \qquad s = \tfrac12 + ir .$$
Then $\lambda \ge 1/4 \iff r \in \mathbb{R}$, and $\lambda < 1/4 \iff r = it$ with $t\in(0,\tfrac12)$, i.e. $s = \tfrac12 + t \in (\tfrac12,1)$ real. So Selberg's conjecture says: **all cuspidal spectral parameters are real.**

**Fourier expansion.** For a Hecke–Maass newform normalized with $a_f(1)=1$,
$$f(z) = \sqrt{y}\sum_{n\neq 0} a_f(n) K_{ir}(2\pi |n| y)\, e(nx),$$
where $K_\nu$ is the modified Bessel function of the second kind. Trivially $K_{ir}$ decays exponentially for $r$ real; for $r = it$ imaginary the form is "non-tempered at $\infty$."

**Representation-theoretic form.** $f$ generates a cuspidal automorphic representation $\pi = \otimes_v \pi_v$ of $\mathrm{GL}_2(\mathbb{A}_\mathbb{Q})$ with trivial central character. The archimedean component $\pi_\infty$ is a principal series $\pi(|\cdot|^{ir},|\cdot|^{-ir})$. Selberg's conjecture $\iff$ $\pi_\infty$ is **tempered** for all $\pi$ of level $N$, i.e. $\pi_\infty$ is never a complementary series. The Generalized Ramanujan Conjecture (GRC) asserts temperedness at **all** places; Selberg's conjecture is exactly its archimedean half, while the Ramanujan–Petersson conjecture $|a_f(p)| \le 2$ is the finite half.

**Uniform bound formulation.** Define $\theta = \theta(\mathrm{GL}_2/\mathbb{Q})$ as the least constant such that for every place $v$ and every cuspidal $\pi$ the local Satake/spectral parameters satisfy
$$|\mathrm{Re}\,\mu_v(\pi)| \le \theta,\qquad\text{equivalently}\qquad |a_f(n)| \ll_\varepsilon n^{\theta+\varepsilon}.$$
Then
$$\lambda_1 \ \ge \ \tfrac14 - \theta^2,$$
and GRC is $\theta = 0$, which implies Selberg. The trivial bound is $\theta \le 1/2$ (unitarity), giving only $\lambda_1 > 0$.

**Selberg trace formula.** For $h$ even, holomorphic and rapidly decaying,
$$\sum_j h(r_j) + (\text{Eisenstein}) = \frac{\mathrm{vol}(\Gamma\backslash\mathbb{H})}{4\pi}\int_{\mathbb{R}} h(r)\, r\tanh(\pi r)\,dr + \sum_{\{\gamma\}\ \mathrm{hyp}} \frac{\ell(\gamma_0)}{2\sinh(\ell(\gamma)/2)}\hat h(\ell(\gamma)) + \cdots$$
This is the engine for both numerical verification and the analytic approach: an exceptional $r_j = it_j$ contributes $h(it_j)$, which is exponentially large for suitable test functions.

**Kuznetsov formula.** Relates spectral sums $\sum_j \frac{a_j(m)\overline{a_j(n)}}{\cosh(\pi r_j)}h(r_j)$ to sums of Kloosterman sums $S(m,n;c) = \sum_{d\bar d\equiv 1 (c)} e((md+n\bar d)/c)$ over moduli $c \equiv 0 \pmod N$. Selberg's $3/16$ comes from Weil's bound $|S(m,n;c)| \le d(c)\gcd(m,n,c)^{1/2}c^{1/2}$ applied here.

## 3. History & State of the Art (SOTA)

- **1956 — Selberg.** Trace formula introduced; the spectrum of $\Gamma\backslash\mathbb{H}$ becomes an object of arithmetic.
- **1965 — Selberg**, *On the estimation of Fourier coefficients of modular forms*, Proc. Sympos. Pure Math. VIII. States the conjecture and proves $\lambda_1 \ge 3/16$ for all congruence subgroups, via Weil's Kloosterman bound. Equivalently $\theta \le 1/4$.
- **1974 — Randol.** Any value in $(0,1/4)$ occurs as $\lambda_1$ for some finite-index (necessarily non-congruence) subgroup of a cocompact group. The congruence hypothesis is essential, not cosmetic.
- **1978 — Gelbart–Jacquet.** Symmetric-square lift $\mathrm{sym}^2:\mathrm{GL}_2\to\mathrm{GL}_3$; combined with Rankin–Selberg non-vanishing yields $\theta \le 1/5$.
- **1995 — Luo–Rudnick–Sarnak**, *On Selberg's eigenvalue conjecture*, GAFA 5. $\theta \le 5/28$, hence $\lambda_1 \ge 21/100 = 0.21$. First breach of $3/16 = 0.1875$ by a genuinely automorphic (not Kloosterman) method.
- **2002 — Kim–Shahidi.** Functoriality of $\mathrm{sym}^3$ and $\mathrm{sym}^4$ gives $\theta \le 1/9$, $\lambda_1 \ge 66/289 \approx 0.2284$.
- **2003 — Kim (Appendix 2 with Sarnak)**, *Functoriality for the exterior square of $\mathrm{GL}_4$ and the symmetric fourth of $\mathrm{GL}_2$*, J. Amer. Math. Soc. 16. **Current record:** $\theta \le 7/64$, hence
$$\lambda_1 \ \ge \ \tfrac14 - \left(\tfrac{7}{64}\right)^2 = \tfrac{975}{4096} = 0.23803\ldots$$
- **2011 — Blomer–Brumley**, Annals of Math. 174. Extends $\theta \le 7/64$ to $\mathrm{GL}_2$ over any number field.
- **2007 — Booker–Strömbergsson.** Rigorous computer verification of $\lambda_1 > 1/4$ for $\Gamma_0(N)$, all squarefree $N \le 857$.

No improvement on $7/64$ for $\mathrm{GL}_2/\mathbb{Q}$ has been accepted in the 20+ years since.

## 4. Partial Results / Verified Cases

- **Unconditional bound, all $N$:** $\lambda_1(N) \ge 975/4096 \approx 0.238$ (Kim–Sarnak). Over any number field: same constant (Blomer–Brumley).
- **Numerical verification:** $\lambda_1(\Gamma_0(N)) > 1/4$ proved rigorously for all squarefree $N \le 857$ (Booker–Strömbergsson, *Numerical computations with the trace formula and the Selberg eigenvalue conjecture*, J. reine angew. Math. 607, 2007), using the Selberg trace formula with explicit error control. Earlier: Huxley (1985) established the conjecture for $\Gamma_0(N)$ and $\Gamma_1(N)$ for small levels ($N \le 18$ and related lists) by explicit Kloosterman-sum estimates.
- **Dihedral / CM forms:** all Maass forms induced from Hecke Grössencharacters of real quadratic fields have $\lambda = 1/4 + r^2$ with $r = \pi k/\log\varepsilon_0$ real; Selberg holds for this entire class unconditionally.
- **Holomorphic analogue:** the weight-$k \ge 2$ Ramanujan–Petersson conjecture $|a_f(p)| \le 2p^{(k-1)/2}$ is a **theorem** (Deligne 1974, via Weil I), so the "$\theta = 0$" statement is proved in the holomorphic world; the Maass world resists.
- **Function-field analogue:** GRC for $\mathrm{GL}_n$ over function fields is a theorem (Drinfeld $n=2$; L. Lafforgue, Invent. Math. 147, 2002, general $n$), for cuspidal representations with suitable local conditions.
- **Weight $1/2$ / theta obstruction:** for the metaplectic cover, exceptional eigenvalue $3/16$ genuinely occurs (theta series), showing $3/16$ is not an artifact — it is sharp in a neighbouring problem, which is why Selberg's original bound sits exactly there.
- **Higher rank:** the analogue $\lambda_1 \ge (n^2-1)/4$ for $\mathrm{SL}_n(\mathbb{Z})$ congruence quotients is likewise open, with bounds inherited from $\theta$.

## 5. Principal Obstacles

- **Weil's bound is the natural barrier for Kloosterman methods.** Selberg's $3/16$ is exactly what square-root cancellation in individual $S(m,n;c)$ gives. Beating it requires cancellation in *sums over the modulus $c$*, and the known Kloosterman-sum-over-$c$ estimates (Deshouillers–Iwaniec) themselves *use* spectral input, so the argument is circular unless supplemented.
- **Deligne's method does not apply.** For holomorphic forms, $a_f(p)$ is an eigenvalue of Frobenius on the étale cohomology of a Kuga–Sato variety, and $|a_f(p)|\le 2p^{(k-1)/2}$ follows from purity. Maass forms of eigenvalue $1/4+r^2$ with $r$ transcendental have **no known motivic realization**: there is no algebraic variety whose cohomology carries them, so no Weil-conjecture leverage exists. This is the single deepest obstruction.
- **Functoriality bounds saturate.** The $L$-function route bounds $\theta$ by $\frac12 - \frac{1}{n^2+1}$ once $\mathrm{sym}^{n-1}$ is known to be automorphic. With $\mathrm{sym}^4$ ($n=5$) one gets $7/64$. Pushing further needs $\mathrm{sym}^5,\mathrm{sym}^6,\dots$ automorphy for **Maass** forms, which is unknown — the recent breakthroughs (Newton–Thorne) prove $\mathrm{sym}^n$ automorphy for *holomorphic* forms via $p$-adic/Galois deformation methods that require a residual Galois representation the Maass case lacks. Even granting all $\mathrm{sym}^n$, the method gives only $\theta \to 0$ in the limit, never $\theta = 0$ for a fixed form without full functoriality plus a limiting argument.
- **Trace-formula positivity is too weak.** A single test function detects an exceptional eigenvalue only if geometric side estimates are uniform in level; the hyperbolic terms grow with the index $[\mathrm{SL}_2(\mathbb{Z}):\Gamma(N)] \sim N^3$, and no known test function isolates the interval $(0,1/4)$ with an error term uniformly $o(\text{index})$.
- **Congruence input must be used somewhere.** Randol's theorem forbids any purely geometric/analytic proof: any valid argument must invoke Hecke operators or the arithmetic of $\Gamma(N)$ at a decisive point.

## 6. The Gap

Proven: $\theta \le 7/64$, hence $\lambda_1 \ge 975/4096$. Conjectured: $\lambda_1 \ge 1/4$, i.e. $\theta = 0$ at the archimedean place. The gap is the numerical interval
$$\left[\tfrac{975}{4096},\ \tfrac14\right), \qquad \text{width } \tfrac{49}{4096} \approx 0.01196,$$
which is not a small quantitative shortfall but a **qualitative** one: any $\theta > 0$ permits a complementary-series component, and every known technique produces a strictly positive $\theta$. Closing it requires one of:

1. Automorphy of $\mathrm{sym}^n \pi$ for all $n$ for Maass forms (then $\theta \le \frac12-\frac1{n^2+1}\to 0$, plus a uniformity argument to reach $\theta=0$ for each fixed $\pi$);
2. A motivic/geometric realization of Maass forms allowing a purity argument;
3. A new positivity identity on the geometric side of Kuznetsov/Selberg that excludes $r = it$ outright.

## 7. Current Research (as of June 2026)

- **Symmetric-power functoriality.** Newton–Thorne (*Symmetric power functoriality for holomorphic modular forms*, Publ. IHÉS 134, 2021) settled all $\mathrm{sym}^n$ for holomorphic newforms. Extending automorphy lifting to the non-motivic Maass case is the flagship problem; groups at Cambridge, IHÉS, Chicago, and Bonn continue to probe whether $p$-adic families or the Calegari–Geraghty framework can reach non-self-dual, non-motivic $\pi_\infty$. *(frontier — verify)*
- **Density theorems as a substitute.** Sarnak's dictum "density is often as good as Ramanujan": Iwaniec, Sarnak, Blomer, Humphries and others prove that exceptional eigenvalues are rare enough (in level aspect) that applications — sieve, equidistribution, subconvexity, spectral gap for expanders — go through unconditionally. This is the dominant practical direction.
- **Trace-formula computation at larger level.** Extending Booker–Strömbergsson beyond squarefree $N \le 857$ with rigorous interval arithmetic, and to $\mathrm{SL}_2(\mathcal{O}_K)$ for imaginary quadratic $K$; LMFDB Maass-form data underpins this. *(frontier — verify)*
- **Relative trace formula / period methods.** Attempts to bound $\theta$ via Ichino–Ikeda type period identities and positivity of triple-product $L$-values.
- **Non-congruence and expander analogues.** Bourgain–Gamburd–Sarnak affine sieve and superstrong approximation, where a $3/16$-type spectral gap for thin groups (Gamburd, Bourgain–Gamburd) plays Selberg's role.

## 8. Future Work

- Prove $\theta \le \frac12 - \frac{1}{n^2+1}$ for a single $n \ge 6$ in the Maass setting; even $\theta < 7/64$ by any route would be the first move in two decades.
- Develop an "archimedean-only" argument: Selberg's conjecture concerns just $\pi_\infty$, so a proof that congruence-arithmeticity forces $\pi_\infty$ tempered — without controlling finite places — might be strictly easier than full GRC.
- Sarnak's suggestion: prove sharp **density hypotheses** $\sum_{\lambda_j < 1/4} X^{2t_j} \ll N^\varepsilon$ strong enough that all standard applications become unconditional, rendering the conjecture's applied content moot even if the statement stays open.
- Push rigorous numerics to non-squarefree and higher levels; a counterexample, if it existed, would most plausibly appear at highly composite level, so systematic search has genuine evidential value.
- Investigate whether Langlands' *Beyond Endoscopy* program, whose whole point is to access functoriality via the trace formula rather than lifting theorems, can deliver $\mathrm{sym}^n$ for Maass forms.

## 9. Key References

- **[Foundational]** A. Selberg. *On the estimation of Fourier coefficients of modular forms.* Proc. Sympos. Pure Math. VIII, Amer. Math. Soc., 1965, pp. 1–15. [DOI](https://doi.org/10.1090/pspum/008/0182610)
- **[Foundational]** A. Selberg. *Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces with applications to Dirichlet series.* J. Indian Math. Soc. 20 (1956), 47–87.
- **[Foundational]** P. Deligne. *La conjecture de Weil. I.* Publ. Math. IHÉS 43 (1974), 273–307. [DOI](https://doi.org/10.1007/bf02684373)
- **[Key partial result]** W. Luo, Z. Rudnick, P. Sarnak. *On Selberg's eigenvalue conjecture.* Geom. Funct. Anal. 5 (1995), 387–401.
- **[SOTA]** H. Kim. *Functoriality for the exterior square of $\mathrm{GL}_4$ and the symmetric fourth of $\mathrm{GL}_2$* (with Appendix 1 by D. Ramakrishnan and Appendix 2 by H. Kim and P. Sarnak). J. Amer. Math. Soc. 16 (2003), 139–183.
- **[SOTA]** H. Kim, F. Shahidi. *Functorial products for $\mathrm{GL}_2\times\mathrm{GL}_3$ and the symmetric cube for $\mathrm{GL}_2$.* Ann. of Math. 155 (2002), 837–893.
- **[SOTA / Recent]** V. Blomer, F. Brumley. *On the Ramanujan conjecture over number fields.* Ann. of Math. 174 (2011), 581–605. [DOI](https://doi.org/10.4007/annals.2011.174.1.18)
- **[Computational]** A. Booker, A. Strömbergsson. *Numerical computations with the trace formula and the Selberg eigenvalue conjecture.* J. reine angew. Math. (Crelle) 607 (2007), 113–161. [DOI](https://doi.org/10.1515/crelle.2007.047)
- **[Related]** L. Lafforgue. *Chtoucas de Drinfeld et correspondance de Langlands.* Invent. Math. 147 (2002), 1–241. [DOI](https://doi.org/10.1007/s002220100174)
- **[Related]** J. Newton, J. Thorne. *Symmetric power functoriality for holomorphic modular forms.* Publ. Math. IHÉS 134 (2021), 1–116. [DOI](https://doi.org/10.1007/s10240-021-00127-3)
- **[Counterpoint]** B. Randol. *Small eigenvalues of the Laplace operator on compact Riemann surfaces.* Bull. Amer. Math. Soc. 80 (1974), 996–1000. [DOI](https://doi.org/10.1090/s0002-9904-1974-13609-8)
- **[Survey]** P. Sarnak. *Selberg's eigenvalue conjecture.* Notices Amer. Math. Soc. 42 (1995), 1272–1277.
- **[Survey]** P. Sarnak. *Notes on the generalized Ramanujan conjectures.* In: Harmonic Analysis, the Trace Formula, and Shimura Varieties, Clay Math. Proc. 4, Amer. Math. Soc., 2005, pp. 659–685.
- **[Textbook]** H. Iwaniec. *Spectral Methods of Automorphic Forms*, 2nd ed. Graduate Studies in Mathematics 53, Amer. Math. Soc., 2002. [DOI](https://doi.org/10.1090/gsm/053)
- **[Textbook]** H. Iwaniec, E. Kowalski. *Analytic Number Theory.* AMS Colloquium Publications 53, 2004 (Chapters 5, 15, 16).

## 10. Worked Example / Concrete Special Case

**Dihedral Maass forms from $\mathbb{Q}(\sqrt{2})$ — a class where Selberg is provable by hand.**

Let $K = \mathbb{Q}(\sqrt2)$, discriminant $D = 8$, ring of integers $\mathcal{O}_K = \mathbb{Z}[\sqrt2]$, fundamental unit $\varepsilon = 1+\sqrt2$, $\log\varepsilon = 0.8813735\ldots$. $K$ has class number $1$ and two real embeddings $\alpha \mapsto (\alpha, \alpha')$.

Define a Hecke Grössencharacter of $K$ on principal ideals by
$$\xi_k\big((\alpha)\big) \;=\; \left|\frac{\alpha}{\alpha'}\right|^{\,i\pi k/\log\varepsilon}, \qquad k \in \mathbb{Z}_{\ge 1}.$$

*Well-definedness.* The formula must not depend on the generator, i.e. must be trivial on units. Since $N(\varepsilon) = (1+\sqrt2)(1-\sqrt2) = -1$, we have $\varepsilon' = -\varepsilon^{-1}$, so $|\varepsilon/\varepsilon'| = \varepsilon^2$ and
$$\xi_k\big((\varepsilon)\big) = \left(\varepsilon^{2}\right)^{i\pi k/\log\varepsilon} = \exp\!\Big(2\log\varepsilon \cdot \tfrac{i\pi k}{\log\varepsilon}\Big) = e^{2\pi i k} = 1. \checkmark$$
It is trivial on $-1$ likewise. So $\xi_k$ is a genuine unramified Grössencharacter.

*The induced form.* Automorphic induction from $\mathrm{GL}_1(\mathbb{A}_K)$ to $\mathrm{GL}_2(\mathbb{A}_\mathbb{Q})$ (Hecke, Maass) attaches to $\xi_k$ a cuspidal Maass newform $f_k$ of level $N = |D| = 8$ with nebentypus the quadratic character $\chi_8$, whose Hecke eigenvalues are
$$a_{f_k}(p) = \begin{cases} \xi_k(\mathfrak{p}) + \xi_k(\bar{\mathfrak{p}}) & p \text{ split in } K,\\ 0 & p \text{ inert},\end{cases}$$
and whose spectral parameter is read off from the infinity type:
$$r_k \;=\; \frac{\pi k}{\log \varepsilon}.$$

*The eigenvalue.* For $k=1$:
$$r_1 = \frac{3.14159265}{0.88137359} = 3.564450\ldots, \qquad \lambda_1(f_1) = \tfrac14 + r_1^2 = 0.25 + 12.7053 = 12.9553\ldots$$
For $k=2$: $r_2 = 7.128900\ldots$, $\lambda = 0.25 + 50.821 = 51.071\ldots$.

*Why this settles Selberg for the class.* Because $\xi_k$ is **unitary** with purely imaginary infinity exponent, $r_k$ is manifestly **real**, so $\lambda = \frac14 + r_k^2 \ge \frac14$ automatically, for every $k$ and every real quadratic $K$. Moreover $|a_{f_k}(p)| = |\xi_k(\mathfrak p)+\xi_k(\bar{\mathfrak p})| \le 2$, so even the full Ramanujan bound $\theta = 0$ holds. Dihedral forms are tempered for free.

*Where the general case breaks.* A generic Maass form on $\Gamma_0(8)$ — say the ones with $r \approx 2.34$, $3.75$, $4.53$ found numerically — is **not** induced from any $\mathrm{GL}_1$ character; there is no unitary character forcing $r$ real, and no variety whose cohomology contains it. All one can assert unconditionally is Kim–Sarnak: if such a form had $\lambda = \frac14 - t^2$ with $t > 0$, then $t \le 7/64 = 0.109375$, hence
$$\lambda \;\ge\; \tfrac14 - \tfrac{49}{4096} \;=\; \tfrac{975}{4096} \;=\; 0.2380371\ldots$$
The conjecture asserts $t = 0$ always. For $N=8$ the Booker–Strömbergsson computation confirms $t=0$; for $N = 858$ or $N = 2^{20}$ it remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*