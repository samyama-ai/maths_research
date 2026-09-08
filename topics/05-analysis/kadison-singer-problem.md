---
id: 05-analysis/kadison-singer-problem
title: "Kadison-Singer Problem"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kadison–Singer Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/kadison-singer-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $\mathcal{H}=\ell^2(\mathbb{N})$, let $B(\mathcal{H})$ be the bounded operators on it, and let
$$\mathcal{D}=\{T\in B(\mathcal{H}) : T e_n = \lambda_n e_n \text{ for some bounded } (\lambda_n)\}\cong \ell^\infty(\mathbb{N})$$
be the atomic maximal abelian self-adjoint subalgebra (MASA) of diagonal operators in the standard basis.

**Kadison–Singer question (1959).** Does every pure state $s:\mathcal{D}\to\mathbb{C}$ extend to a *unique* state on $B(\mathcal{H})$?

Existence of an extension is Hahn–Banach plus positivity; the content is uniqueness. A complete solution is either (a) a proof that for every pure state $s$ on $\mathcal{D}$ the set of state extensions to $B(\mathcal{H})$ is a singleton, or (b) an explicit pure state with two distinct extensions.

**Answer: yes.** Marcus, Spielman and Srivastava (2013 preprint; *Annals of Mathematics* 2015) proved Weaver's discrepancy conjecture $\mathrm{KS}_2$, which by the chain Weaver $\Rightarrow$ Anderson paving $\Rightarrow$ Kadison–Singer settles the problem affirmatively. The status here is *solved-recently*: the original question is closed, while the quantitative form (optimal paving constants, algorithms) remains open.

## 2. Mathematical Foundations

**States.** A state on a unital C\*-algebra $\mathcal{A}$ is a linear $s:\mathcal{A}\to\mathbb{C}$ with $s(1)=1$ and $s(a^*a)\ge0$. States form a weak\*-compact convex set; *pure* states are its extreme points. For $\mathcal{D}\cong\ell^\infty(\mathbb{N})=C(\beta\mathbb{N})$, states are finitely additive probability measures on $\mathbb{N}$ and pure states are $\{0,1\}$-valued ones, i.e. ultrafilters $\mathcal{U}\in\beta\mathbb{N}$, with
$$s_{\mathcal{U}}(T)=\lim_{n\to\mathcal{U}} T_{nn}.$$

**Paving.** For $A\subseteq\mathbb{N}$ let $P_A$ be the coordinate projection. $T$ is *$(r,\varepsilon)$-pavable* if there is a partition $\mathbb{N}=A_1\sqcup\cdots\sqcup A_r$ with
$$\bigl\|P_{A_j}\,(T-\mathrm{diag}\,T)\,P_{A_j}\bigr\|\le \varepsilon\|T\|,\qquad j=1,\dots,r.$$

**Anderson's paving conjecture (1979).** For every $\varepsilon>0$ there is $r=r(\varepsilon)\in\mathbb{N}$ such that every $T\in B(\ell^2)$ with zero diagonal is $(r,\varepsilon)$-pavable. Anderson proved this is *equivalent* to Kadison–Singer.

**Weaver's $\mathrm{KS}_r$ (2004).** There exist $\eta\ge 2$ and $\theta>0$ such that: for all $d$ and all $v_1,\dots,v_m\in\mathbb{C}^d$ with $\|v_i\|^2\le 1$ and
$$\sum_{i=1}^m |\langle u,v_i\rangle|^2=\eta \quad \text{for every unit } u\in\mathbb{C}^d,$$
there is a partition $[m]=S_1\sqcup\cdots\sqcup S_r$ with $\sum_{i\in S_j}|\langle u,v_i\rangle|^2\le \eta-\theta$ for all unit $u$ and all $j$. Weaver proved $\mathrm{KS}_r\Rightarrow$ Kadison–Singer.

**MSS Theorem (2015).** If $v_1,\dots,v_m\in\mathbb{C}^d$ satisfy $\sum_i v_iv_i^*=I$ and $\|v_i\|^2\le\epsilon$, then there is a partition $[m]=S_1\sqcup S_2$ with
$$\Bigl\|\sum_{i\in S_j} v_iv_i^*\Bigr\|\le \frac{(1+\sqrt{2\epsilon})^2}{2},\qquad j=1,2 .$$

The proof machinery is the *mixed characteristic polynomial* of PSD matrices $A_1,\dots,A_m$:
$$\mu[A_1,\dots,A_m](x)=\Bigl(\prod_{i=1}^m\bigl(1-\partial_{z_i}\bigr)\Bigr)\det\Bigl(xI+\sum_{i=1}^m z_iA_i\Bigr)\Big|_{z_1=\cdots=z_m=0},$$
which equals $\mathbb{E}\det\bigl(xI-\sum_i w_iw_i^*\bigr)$ for independent random vectors with $\mathbb{E}\,w_iw_i^*=A_i$. Two ingredients: (i) these polynomials form an *interlacing family*, so some realization has largest root at most that of the expected polynomial; (ii) a multivariate barrier argument on real-stable polynomials (Borcea–Brändén theory, extending Batson–Spielman–Srivastava sparsification) bounds the largest root of $\mu$ by $(\sqrt{\epsilon_1}+\sqrt{\epsilon_2})^2$ when $\sum A_i=I$ and $\mathrm{tr}\,A_i\le\epsilon$.

## 3. History & State of the Art (SOTA)

- **1959.** Kadison and Singer, *Extensions of pure states* (Amer. J. Math. 81), pose the question, motivated by Dirac's claim that a complete commuting set of observables determines a state. They *prove* the continuous (Lebesgue) MASA fails uniqueness, and conjecture — with stated doubt — failure in the discrete case too.
- **1979.** Anderson reformulates via paving; the operator-theoretic combinatorics era begins.
- **1988.** Berman–Halpern–Kaftal–Weiss: paving for matrices with non-negative entries; Halpern–Kaftal–Weiss handle Toeplitz operators with continuous symbol.
- **1991.** Bourgain–Tzafriri, *On a problem of Kadison and Singer* (Crelle 420): paving for $n\times n$ matrices with entries $O(n^{-\delta})$, and restricted-invertibility techniques.
- **2004.** Weaver recasts the problem as a purely finite-dimensional discrepancy statement $\mathrm{KS}_r$.
- **2006.** Casazza–Fickus–Tremain–Weber and Casazza–Tremain document $\sim$ 20 equivalent formulations: Feichtinger conjecture (every bounded frame splits into finitely many Riesz sequences), Bourgain–Tzafriri conjecture, Akemann–Anderson projection paving, the $R_\epsilon$-conjecture.
- **2013/2015.** Marcus–Spielman–Srivastava, *Interlacing families II* (Ann. of Math. 182), prove $\mathrm{KS}_2$ and hence Kadison–Singer. Companion paper *Interlacing families I* gives bipartite Ramanujan graphs of every degree.
- **2019–2021 (quantitative SOTA).** Bownik–Casazza–Marcus–Speegle (Crelle 749) sharpen the MSS constants and give $r=O(\varepsilon^{-4})$-type paving; Ravichandran–Srivastava (*Asymptotically optimal multi-paving*, IMRN 2021) obtain paving with $r=O(\varepsilon^{-2})$ parts, matching the known $\Omega(\varepsilon^{-2})$ lower bound up to constants.

## 4. Partial Results / Verified Cases

- **Atomic pure states:** if $s$ comes from a principal ultrafilter, $s(T)=T_{nn}$, uniqueness is elementary (proved in Kadison–Singer 1959). Only free ultrafilters were ever at issue.
- **Continuous MASA:** uniqueness *fails* (Kadison–Singer 1959) — a genuine negative case, showing the answer depends on atomicity.
- **Structured matrix classes solved pre-2013:** non-negative entries (BHKW 1988); Toeplitz with continuous symbol; matrices with $\ell^2$-normalized entries of size $O(n^{-\delta})$, $\delta>0$ (Bourgain–Tzafriri 1991); Laurent operators with certain symbol regularity.
- **Full theorem:** all $T\in B(\ell^2)$ with zero diagonal, all $\varepsilon>0$, some finite $r(\varepsilon)$ (MSS 2015 via Weaver).
- **Explicit constants:** $\epsilon\le 1/2$ splits a tight frame into two parts of norm $\le (1+\sqrt{2\epsilon})^2/2$; iterating $k$ times yields $2^k$-set pavings. Current best paving: $r=O(\varepsilon^{-2})$ (Ravichandran–Srivastava). For projections with diagonal entries $\le\delta$, two-set paving with $\|P_{A_j}QP_{A_j}\|\le \tfrac12+O(\sqrt\delta)$.
- **Strongly Rayleigh generalization:** Anari–Oveis Gharan prove a Kadison–Singer-type partitioning theorem for strongly Rayleigh measures, applied to asymmetric TSP.

## 5. Principal Obstacles

Why the problem stood for 54 years, and why the quantitative version is still hard:

- **Union bound / random partition failure.** A uniformly random $r$-partition of a tight frame gives $\|\sum_{i\in S_j}v_iv_i^*\|\approx 1/r + O(\sqrt{\log d/r})$ only after a matrix-Chernoff bound; the $\log d$ factor is fatal because $d$ (equivalently the truncation size of $T$) is unbounded. Every concentration-based argument leaks a dimension factor, and the paving constant $r$ must be dimension-free.
- **Non-constructive extreme cases.** The extremal frames (Fourier submatrices, discrete Hilbert transforms) sit exactly where Chernoff bounds are tight; no perturbative or compactness argument reduces the general operator to a structured one.
- **Operator-algebraic barriers.** Pure states on $B(\mathcal{H})$ are wildly non-normal; there is no explicit description, so direct verification of uniqueness is impossible. Anderson's translation to paving was needed to make the problem finite-dimensional at all.
- **Determinantal rigidity.** The MSS proof works because $\det(xI+\sum z_iA_i)$ is real stable and $(1-\partial_{z_i})$ preserves stability. This is a *characteristic-polynomial* argument: it controls the largest root of one realization but yields no witness. All known proofs are therefore existential; the same rigidity blocks quantitative refinements, since the barrier bound $(\sqrt{\epsilon_1}+\sqrt{\epsilon_2})^2$ is tight for the expected polynomial but not necessarily for the best partition.

## 6. The Gap

The original gap — between structured classes (Section 4) and arbitrary zero-diagonal operators — was closed in 2015. The residual gaps are:

1. **Optimal paving.** Known: $r=O(\varepsilon^{-2})$ suffices and $r=\Omega(\varepsilon^{-2})$ is necessary. The constant in front is unresolved; the natural conjecture that $r=\lceil \varepsilon^{-2}\rceil+O(1)$ suffices is open.
2. **Algorithmics.** Interlacing families prove existence by showing $\min_{\text{leaf}}\le$ root value. Finding a good partition in time polynomial in $m,d$ is open; the best known constructions are quasi-polynomial or restricted to special measures. *(frontier — verify)*
3. **Beyond MASAs.** Uniqueness of pure-state extension for general C\*-inclusions ("Kadison–Singer property" for arbitrary abelian subalgebras, group C\*-algebras, von Neumann algebras of type II$_1$) is only partially charted.

## 7. Current Research (as of June 2026)

- **Yale / Berkeley / Washington (Spielman, Srivastava, Ravichandran, Marcus):** effective and algorithmic interlacing families; barrier-function analyses that also drive spectral sparsification and restricted invertibility.
- **Missouri / Oregon (Casazza, Speegle, Bownik):** frame-theoretic consequences — Feichtinger decompositions with explicit Riesz bounds, exponential frames for sets of positive measure, sampling theory.
- **Real stability community (Brändén, Anari, Oveis Gharan, Vinzant):** completely log-concave / Lorentzian polynomials as the successor framework, with applications to matroid counting and TSP.
- **Operator algebras (Weaver, Akemann, Tao's expository account):** the Lyapunov-type theorem from Kadison–Singer, and Kadison–Singer properties for non-atomic and non-commutative inclusions.
- Reported near-optimal or polynomial-time partitioning algorithms for special frame families continue to appear as preprints. *(frontier — verify)*

## 8. Future Work

- Determine the exact paving function $r(\varepsilon)$, closing the constant-factor gap to the $\Omega(\varepsilon^{-2})$ lower bound.
- Produce a *constructive* proof of $\mathrm{KS}_2$ — Spielman has repeatedly flagged this as the main open problem left by the 2013 argument.
- Extend the mixed-characteristic-polynomial method to non-PSD and infinite-rank settings, e.g. discrepancy of general matrices (Spencer-type $\pm1$ colorings with spectral norm objectives).
- Classify C\*-inclusions with the Kadison–Singer property; settle the case of MASAs in II$_1$ factors.
- Exploit the Lorentzian/completely log-concave generalization to obtain unified proofs of Kadison–Singer, Ramanujan graphs, and restricted invertibility.

## 9. Key References

- **[Foundational]** R. V. Kadison and I. M. Singer. *Extensions of pure states.* American Journal of Mathematics 81 (1959), 383–400. [DOI](https://doi.org/10.2307/2372748)
- **[Foundational]** J. Anderson. *Extensions, restrictions, and representations of states on C\*-algebras.* Transactions of the AMS 249 (1979), 303–329. [DOI](https://doi.org/10.2307/1998793)
- **[Foundational]** J. Bourgain and L. Tzafriri. *On a problem of Kadison and Singer.* Journal für die reine und angewandte Mathematik 420 (1991), 1–43.
- **[Reformulation]** N. Weaver. *The Kadison–Singer problem in discrepancy theory.* Discrete Mathematics 278 (2004), 227–239. [DOI](https://doi.org/10.1016/s0012-365x(03)00253-x)
- **[Solution]** A. Marcus, D. A. Spielman, N. Srivastava. *Interlacing families II: Mixed characteristic polynomials and the Kadison–Singer problem.* Annals of Mathematics 182 (2015), 327–350. [DOI](https://doi.org/10.4007/annals.2015.182.1.8)
- **[Companion]** A. Marcus, D. A. Spielman, N. Srivastava. *Interlacing families I: Bipartite Ramanujan graphs of all degrees.* Annals of Mathematics 182 (2015), 307–325. [DOI](https://doi.org/10.4007/annals.2015.182.1.7)
- **[SOTA / Recent]** M. Bownik, P. G. Casazza, A. Marcus, D. Speegle. *Improved bounds in Weaver and Feichtinger conjectures.* Journal für die reine und angewandte Mathematik 749 (2019), 267–293.
- **[SOTA / Recent]** M. Ravichandran, N. Srivastava. *Asymptotically optimal multi-paving.* International Mathematics Research Notices 2021.
- **[Related]** N. Anari, S. Oveis Gharan. *The Kadison–Singer problem for strongly Rayleigh measures and applications to asymmetric TSP.* Preprint, 2014.
- **[Survey]** P. G. Casazza, M. Fickus, J. C. Tremain, E. Weber. *The Kadison–Singer problem in mathematics and engineering: a detailed account.* Contemporary Mathematics 414 (2006), 299–355. [DOI](https://doi.org/10.1090/conm/414/07820)
- **[Survey]** P. G. Casazza and J. C. Tremain. *The Kadison–Singer problem in mathematics and engineering.* PNAS 103 (2006), 2032–2039.
- **[Book]** M. Stevens. *The Kadison–Singer Property.* SpringerBriefs in Mathematical Physics, Springer, 2016. [DOI](https://doi.org/10.1007/978-3-319-47702-2)
- **[Related]** C. Akemann and N. Weaver. *A Lyapunov-type theorem from Kadison–Singer.* Bulletin of the London Mathematical Society 46 (2014), 517–524. [DOI](https://doi.org/10.1112/blms/bdu005)

## 10. Worked Example / Concrete Special Case

**A tight frame in $\mathbb{C}^2$ split in two.** Take $d=2$, $m=4$ and
$$v_1=\tfrac{1}{\sqrt2}\binom{1}{0},\quad v_2=\tfrac{1}{\sqrt2}\binom{0}{1},\quad v_3=\tfrac12\binom{1}{1},\quad v_4=\tfrac12\binom{1}{-1}.$$
Then $v_1v_1^*+v_2v_2^*=\tfrac12 I$ and $v_3v_3^*+v_4v_4^*=\tfrac12 I$, so $\sum_{i=1}^4 v_iv_i^*=I$: this is a unit-norm tight frame ("Parseval frame") with $\|v_i\|^2=\epsilon=1/2$.

Partition $S_1=\{1,2\}$, $S_2=\{3,4\}$. Each block satisfies $\bigl\|\sum_{i\in S_j}v_iv_i^*\bigr\|=\tfrac12$ — a perfect split. The MSS bound gives only $\tfrac12(1+\sqrt{2\cdot\tfrac12})^2=2$, which is vacuous at $\epsilon=1/2$; it becomes informative for small $\epsilon$. With $\epsilon=10^{-2}$ the theorem guarantees a two-set split with each part of norm $\le\tfrac12(1+\sqrt{0.02})^2\approx 0.646$, and iterating $k$ times yields $2^k$ parts of norm $\to 0$.

**Why no split can be perfect in general.** Replace $v_3,v_4$ by $\tilde v_3=\tfrac{1}{\sqrt2}\binom{1}{0}$, $\tilde v_4=\tfrac{1}{\sqrt2}\binom{0}{1}$, so all four vectors lie along the two axes with multiplicity two. Any two-set partition either separates the duplicates (giving $\tfrac12 I$, norm $\tfrac12$) or groups both copies of one axis together, giving $\mathrm{diag}(1,0)$ with norm $1$. A greedy or random choice can land on the bad branch; the theorem asserts that *some* branch is good, which is exactly what the interlacing-family argument supplies.

**The mixed characteristic polynomial, degenerate case.** For $d=1$ with scalars $a_i=\|v_i\|^2$, $\sum a_i=1$,
$$\mu(x)=\prod_i(1-\partial_{z_i})\Bigl(x+\sum_i z_ia_i\Bigr)\Big|_{z=0}=x-\sum_i a_i=x-1,$$
whose unique root $1$ is the exact (deterministic) value of the sum. The multivariate barrier argument bounds the largest root of $\mu$ by $(\sqrt{\epsilon_1}+\sqrt{\epsilon_2})^2$ in general; the interlacing property then converts that bound on the *average* polynomial into the existence of a single partition achieving it.

**Back to paving.** Given a zero-diagonal $T$ with $\|T\|=1$, apply the frame statement to the columns of a suitable factorization of $I-\tfrac12(T/\|T\|+\cdots)$; iterating $k=O(\log(1/\varepsilon))$ times produces a partition of $\mathbb{N}$ into $r$ blocks with $\|P_{A_j}TP_{A_j}\|\le\varepsilon$, with $r=O(\varepsilon^{-2})$ in the sharpest current form. Anderson's equivalence then yields uniqueness of pure-state extension: any two extensions of $s_{\mathcal{U}}$ agree on each $T$ because for every $\varepsilon$ some block $A_j\in\mathcal{U}$ forces $|s(T)-s_{\mathcal U}(\mathrm{diag}\,T)|\le\varepsilon\|T\|$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*