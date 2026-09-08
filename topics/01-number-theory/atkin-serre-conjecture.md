---
id: 01-number-theory/atkin-serre-conjecture
title: "Atkin-Serre Conjecture on Coefficient Growth"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Atkin-Serre Conjecture on Coefficient Growth

> **Topic:** Number Theory · **ID:** `01-number-theory/atkin-serre-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $f=\sum_{n\ge 1}a_f(n)q^n$ be a normalized Hecke eigenform of integral weight $k\ge 4$ and level $N$, cuspidal and **without complex multiplication**. The Atkin–Serre conjecture asserts a lower bound on the size of the prime-indexed coefficients:

$$\text{for every }\varepsilon>0,\qquad |a_f(p)|\;\gg_{f,\varepsilon}\;p^{\frac{k-3}{2}-\varepsilon}\qquad (p\nmid N).$$

The implied constant may depend on $f$ and $\varepsilon$; the bound is asserted for **all** sufficiently large primes, not merely almost all. A proof must handle every prime, with no exceptional set. A disproof requires exhibiting a non-CM eigenform of weight $\ge 4$ and an infinite sequence of primes with $|a_f(p)| \le p^{(k-3)/2-\varepsilon}$ for some fixed $\varepsilon>0$ — in particular, infinitely many $p$ with $a_f(p)=0$ would suffice.

Two constraints are essential. **CM forms are excluded**: if $f$ has CM by an imaginary quadratic field $K$, then $a_f(p)=0$ for every $p$ inert in $K$, a set of density $1/2$. **Weight $k\ge 4$ is required**: for $k=2$ the exponent $(k-3)/2$ is negative and the statement would assert $a_f(p)\neq 0$ for large $p$, which is false — Elkies proved every elliptic curve over $\mathbb{Q}$ has infinitely many supersingular primes, i.e. infinitely many $p$ with $a_f(p)=0$.

The special case $k=12$, $N=1$, $f=\Delta$, reduced to the assertion $\tau(p)\neq 0$, is **Lehmer's conjecture** on the non-vanishing of the Ramanujan tau function.

## 2. Mathematical Foundations

Let $S_k(\Gamma_0(N),\chi)$ be the space of cusp forms of weight $k$, level $N$, nebentypus $\chi$. A newform $f$ is an eigenvector of all Hecke operators $T_n$, normalized so $a_f(1)=1$; then $T_nf=a_f(n)f$ and the coefficients are multiplicative with

$$a_f(p^{m+1})=a_f(p)a_f(p^m)-\chi(p)p^{k-1}a_f(p^{m-1}),\qquad p\nmid N .$$

The coefficients generate a totally real (or CM) number field $K_f=\mathbb{Q}(a_f(n):n\ge1)$ of finite degree $d$, and each $a_f(n)$ is an algebraic integer.

**Deligne's bound.** From the Weil conjectures (Deligne 1974), for $p \nmid N$,

$$|a_f(p)|\le 2p^{\frac{k-1}{2}},\qquad\text{so we may write } a_f(p)=2p^{\frac{k-1}{2}}\cos\theta_p,\quad \theta_p\in[0,\pi].$$

The Atkin–Serre bound is therefore equivalent to $|\cos\theta_p|\gg_\varepsilon p^{-1-\varepsilon}$: the Satake angle $\theta_p$ must not approach $\pi/2$ faster than $p^{-1}$.

**Galois representations.** For each prime $\ell$ there is a continuous representation
$$\rho_{f,\ell}:\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to \mathrm{GL}_2(K_{f,\lambda}),\qquad \mathrm{tr}\,\rho_{f,\ell}(\mathrm{Frob}_p)=a_f(p),\quad \det\rho_{f,\ell}(\mathrm{Frob}_p)=\chi(p)p^{k-1},$$
unramified outside $N\ell$. Vanishing $a_f(p)=0$ is the condition that $\mathrm{Frob}_p$ lands in the trace-zero locus, a proper closed subvariety of the image group. Ribet proved that for non-CM $f$ the image of $\rho_{f,\ell}$ is open in the subgroup of $\mathrm{GL}_2(\mathcal{O}_\lambda)$ with determinant in the expected line, for all but finitely many $\ell$.

**Sato–Tate.** For non-CM $f$, the angles $\theta_p$ equidistribute with respect to
$$\mu_{ST}=\frac{2}{\pi}\sin^2\theta\,d\theta$$
(Barnet-Lamb–Geraghty–Harris–Taylor 2011, building on Taylor's potential automorphy). Since $\mu_{ST}\{|\cos\theta|<\delta\}\asymp \delta^{3}$ as $\delta\to0$, a Borel–Cantelli heuristic predicts $\sum_p p^{-3(1+\varepsilon)}<\infty$ exceptions — this is exactly the probabilistic evidence for the exponent $(k-3)/2$, and it suggests the truth is stronger: $|a_f(p)|\gg p^{(k-1)/2-\varepsilon}$ for all but finitely many $p$.

**Algebraic lower bound.** If $a_f(p)\neq 0$, taking the norm $|N_{K_f/\mathbb{Q}}(a_f(p))|\ge 1$ and bounding the $d-1$ conjugates by Deligne gives
$$|a_f(p)|\ \ge\ \left(2p^{\frac{k-1}{2}}\right)^{-(d-1)} .$$
For $d\ge 3$ this is weaker than nothing useful; for $d=1$ (rational coefficients, e.g. the level-one forms of weight $12,16,18,20,22,26$) it gives only $|a_f(p)|\ge 1$.

## 3. History & State of the Art (SOTA)

- **1916.** Ramanujan introduces $\tau(n)$ via $\Delta=q\prod_{n\ge1}(1-q^n)^{24}=\sum\tau(n)q^n$ and conjectures $|\tau(p)|\le 2p^{11/2}$.
- **1947.** Lehmer, *The vanishing of Ramanujan's function $\tau(n)$*, verifies $\tau(n)\neq0$ for $n<3\,316\,799$ and raises the non-vanishing question.
- **1968–1973.** Serre and Swinnerton-Dyer develop the $\ell$-adic theory; Swinnerton-Dyer classifies the exceptional primes for $\Delta$ as $\ell\in\{2,3,5,7,23,691\}$, converting congruences for $\tau$ into congruence obstructions to $\tau(p)=0$.
- **1974.** Deligne proves the Ramanujan–Petersson bound, fixing the *upper* side once and for all. The lower side becomes the open problem.
- **1981.** Serre, *Quelques applications du théorème de densité de Chebotarev* (Publ. IHÉS 54), records the question in the form now attributed to Atkin and Serre, and proves the first density results: for non-CM $f$,
 $$\\#\{p\le x: a_f(p)=0\}\ \ll_f\ \frac{x(\log\log x)}{(\log x)^{3/2}},$$
 and $\ll_f x^{3/4}$ under GRH for the relevant Artin/symmetric-power $L$-functions.
- **2011.** Sato–Tate for non-CM holomorphic newforms is proved, giving the density-one statement $|a_f(p)|\ge p^{(k-1)/2-\varepsilon}$ outside a set of density $0$ — far stronger than Atkin–Serre, but only in density.
- **2017–2021.** Rouse–Thorner and Thorner make Sato–Tate effective: explicit bounds under GRH for the exceptional counts and for the least prime in a Satake interval.
- **2021–2023.** Balakrishnan, Craig, Ono, and Tsai prove that $\tau(n)$ and newform coefficients omit explicit small odd values, using integral points on Thue–Mahler equations and hyperelliptic curves.

## 4. Partial Results / Verified Cases

- **Density one.** For every non-CM eigenform of weight $k\ge2$, the set of $p$ with $|a_f(p)|<p^{(k-1)/2-\varepsilon}$ has natural density $0$ (Sato–Tate). The conjecture is thus true "for almost all $p$" with a better exponent.
- **Exceptional-set bounds.** $\\#\{p\le x: a_f(p)=0\}\ll x(\log\log x)(\log x)^{-3/2}$ unconditionally; $\ll x^{3/4}$ under GRH (Serre 1981); refinements and explicit constants in Rouse–Thorner (2017).
- **Congruence exclusions.** For $\Delta$, the exceptional primes $2,3,5,7,23,691$ force any $p$ with $\tau(p)=0$ into a very sparse union of congruence classes (see §10): such $p$ satisfy $p\equiv 2 \pmod 3$, $p\equiv 4\pmod 5$, $p^{3}\equiv -1\pmod 7$, $p^{11}\equiv -1\pmod{691}$, and further $2$-adic and $23$-adic conditions. The resulting set has density below $10^{-3}$.
- **Computational verification.** $\tau(n)\neq0$ for all $n<816\,212\,624\,008\,487\,344\,127\,999\approx8.2\times10^{23}$ (Derickx, van Hoeij, Zeng, 2013), via computation of the mod-$\ell$ representations attached to $\Delta$ following Edixhoven–Couveignes. Analogous ranges are verified for other small-level newforms.
- **Odd-argument transcendence bound.** Murty, Murty and Shorey (1987) proved, by Baker's theory of linear forms in logarithms, that $|\tau(n)|>(\log n)^{\delta}$ for some effective $\delta>0$ for all **odd** $n$. This is the only known effective growth statement, and it does not apply to odd primes, since $\tau(p)\equiv\sigma_{11}(p)=1+p^{11}\equiv 0\pmod 2$ for $p$ odd.
- **Omitted values.** $\tau(n)\notin\{\pm1,\pm3,\pm5,\pm7,\pm13,\pm17,\pm19,\ldots,\pm691\}$ for $n>1$, and similar lists for other newforms (Balakrishnan–Craig–Ono, Balakrishnan–Craig–Ono–Tsai).

## 5. Principal Obstacles

- **Chebotarev is a counting theorem, not a pointwise theorem.** All Galois-theoretic input controls the *frequency* of $\mathrm{Frob}_p$ in a conjugacy-stable set. No known effective Chebotarev statement — even under GRH — excludes a single prescribed prime from a positive-measure-zero locus. The trace-zero locus is measure zero in the image group, so it is invisible to density arguments.
- **No archimedean handle on a single $a_f(p)$.** Analytic methods (moments of symmetric-power $L$-functions, large sieve, Rankin–Selberg) bound averages $\sum_{p\le x}|a_f(p)|^{2m}$ from below, which cannot preclude one tiny term.
- **Transcendence methods stall at parity.** Baker's method converts $|a_f(p)|$ small into an $S$-unit equation only when the relevant factorization is controlled — available for odd $n$ via $\tau(n)$ odd $\Leftrightarrow n$ odd square, and unavailable at primes.
- **Degree-one coefficient fields kill the norm trick.** For $\Delta$ the norm bound gives $|\tau(p)|\ge1$, i.e. exactly the non-vanishing question restated. For $d\ge2$ the bound degrades like $p^{-(d-1)(k-1)/2}$, worse than trivial.
- **Mod-$\ell$ methods are finite in nature.** Congruences at exceptional primes remove congruence classes, but the non-exceptional $\ell$ have large image, so $a_f(p)\equiv0 \pmod \lambda$ is possible for a positive density of $p$ for each $\ell$; intersecting over infinitely many $\ell$ is not a legitimate operation without an effective bound on $p$ in terms of $\ell$.
- **Even a proof of $a_f(p)\neq0$ is not enough.** Atkin–Serre demands a *quantitative* lower bound; non-vanishing alone gives at best $|a_f(p)|\ge (2p^{(k-1)/2})^{-(d-1)}$.

## 6. The Gap

Proven: the bound holds for a density-one set of primes with the stronger exponent $(k-1)/2-\varepsilon$; the exceptional set has size $O(x^{3/4})$ under GRH. Conjectured: the bound holds for **every** large prime with exponent $(k-3)/2-\varepsilon$.

The gap is therefore entirely the passage from *statistical* to *pointwise*. Concretely, one needs an effective, prime-specific mechanism: an inequality of the form "if $|a_f(p)|<p^{(k-3)/2-\varepsilon}$ then $p<C(f,\varepsilon)$." Every known tool produces bounds on counts $\pi_f(x)$ of bad primes up to $x$; none produces an upper bound on an individual bad prime. Even the sharpest conditional effective Sato–Tate results give the *least* prime with $\theta_p$ in a fixed interval, not the *largest* prime with $\theta_p$ in a shrinking one. Closing the gap for the single form $\Delta$ and the single weakened conclusion $\tau(p)\ne0$ (Lehmer) is already open.

## 7. Current Research (as of June 2026)

- **Effective Sato–Tate.** Thorner's framework (Res. Math. Sci., 2021) and refinements by Chiriac–Jorza give GRH-conditional bounds for $\theta_p$ in shrinking intervals of width $p^{-\delta}$; pushing $\delta$ past $1$ would give Atkin–Serre under GRH. Current admissible $\delta$ remains far below $1$. *(frontier — verify)*
- **Diophantine methods for coefficient values.** The Ono school (Ono, Tsai, Craig, Balakrishnan, and collaborators at Virginia, Boston University, Emory) continues to convert $a_f(p)=\alpha$ into Thue–Mahler and hyperelliptic equations for explicit small $\alpha$; the method is finite for each target value and cannot yet reach the value $0$ for prime index.
- **Computation of mod-$\ell$ Galois representations.** The Edixhoven–Couveignes algorithm, as implemented by Derickx, van Hoeij, Zeng and successors in Pari/GP and Magma, extends the verified range for $\tau(n)\neq0$; work on higher-weight and higher-level newforms (Mascot, Zeng) broadens the tested families. *(frontier — verify)*
- **Sparsity and lacunarity.** Descendants of Serre's *Sur la lacunarité des puissances de $\eta$* study the exact density of $\{p:a_f(p)\equiv0\ (\mathrm{mod}\ \ell)\}$ and its interaction with the $\ell$-adic image, aiming at unconditional improvements to the $x(\log x)^{-3/2}$ exceptional bound.
- **Large-scale data.** LMFDB coefficient tables permit systematic scanning for near-minimal $|\cos\theta_p|$ across thousands of newforms; no violation of $|a_f(p)|>p^{(k-3)/2}$ has been observed.

## 8. Future Work

- Prove Lehmer's conjecture $\tau(p)\neq0$ as the minimal test case; any method that succeeds will likely generalize to all $k\ge4$.
- Establish an effective version of Chebotarev / Sato–Tate with a power-saving dependence on the modulus of the shrinking target set, giving an explicit $C(f,\varepsilon)$.
- Develop a $p$-adic or Diophantine criterion turning $a_f(p)=0$ into an integral-point problem on a curve of genus $\ge2$, so Faltings/Chabauty methods apply; the parity obstruction at $p$ must be circumvented.
- Prove the strong form $|a_f(p)|\gg p^{(k-1)/2-\varepsilon}$ outside a finite set, consistent with the $\mu_{ST}$ Borel–Cantelli heuristic, and test it numerically for large families.
- Extend the verified ranges for $\tau(n)\ne0$ by an order of magnitude using faster modular-representation computations.

## 9. Key References

- **[Foundational]** D. H. Lehmer. *The vanishing of Ramanujan's function $\tau(n)$.* Duke Mathematical Journal **14** (1947), 429–433.
- **[Foundational]** P. Deligne. *La conjecture de Weil. I.* Publications Mathématiques de l'IHÉS **43** (1974), 273–307.
- **[Foundational]** H. P. F. Swinnerton-Dyer. *On $\ell$-adic representations and congruences for coefficients of modular forms.* In: Modular Functions of One Variable III, Lecture Notes in Mathematics 350, Springer, 1973, 1–55.
- **[Foundational]** J.-P. Serre. *Quelques applications du théorème de densité de Chebotarev.* Publications Mathématiques de l'IHÉS **54** (1981), 123–201.
- **[Foundational]** J.-P. Serre. *Sur la lacunarité des puissances de $\eta$.* Glasgow Mathematical Journal **27** (1985), 203–221.
- **[Partial result]** M. R. Murty, V. K. Murty, T. N. Shorey. *Odd values of the Ramanujan $\tau$-function.* Bulletin de la Société Mathématique de France **115** (1987).
- **[SOTA]** T. Barnet-Lamb, D. Geraghty, M. Harris, R. Taylor. *A family of Calabi–Yau varieties and potential automorphy II.* Publications of RIMS **47** (2011), 29–98.
- **[SOTA]** J. Rouse, J. Thorner. *The explicit Sato–Tate conjecture and densities pertaining to Lehmer-type questions.* Transactions of the American Mathematical Society **369** (2017).
- **[SOTA]** J. Thorner. *Effective forms of the Sato–Tate conjecture.* Research in the Mathematical Sciences **8** (2021).
- **[SOTA / Recent]** J. S. Balakrishnan, W. Craig, K. Ono. *Variations of Lehmer's conjecture for Ramanujan's tau-function.* Journal of Number Theory, 2021.
- **[SOTA / Recent]** J. S. Balakrishnan, W. Craig, K. Ono, W.-L. Tsai. *Variants of Lehmer's speculation for newforms.* Advances in Mathematics, 2023.
- **[Computational]** M. Derickx, M. van Hoeij, J. Zeng. *Computing Galois representations and equations for modular curves $X_H(\ell)$.* Preprint, arXiv:1312.6819, 2013.
- **[Computational]** N. Lygeros, O. Rozier. *A new solution to the equation $\tau(p)\equiv 0\pmod p$.* Journal of Integer Sequences **13** (2010).
- **[Survey]** M. Ram Murty. *The Ramanujan $\tau$ function.* In: Ramanujan Revisited, Academic Press, 1988, 269–288.

## 10. Worked Example / Concrete Special Case

Take $f=\Delta$, $k=12$, $N=1$, $d=1$ (rational coefficients), non-CM. Here $(k-1)/2=5.5$ and $(k-3)/2=4.5$.

**Numerical check at $p=13$.** $\tau(13)=-577738$.
- Deligne: $2\cdot13^{5.5}=2\cdot13^5\sqrt{13}=2\cdot371293\cdot3.60555\approx 2\,677\,500$. Indeed $577738<2\,677\,500$. ✓
- Atkin–Serre target: $13^{4.5}=13^4\sqrt{13}=28561\cdot3.60555\approx 102\,980$. Indeed $577738 > 102\,980$. ✓
- Satake angle: $\cos\theta_{13}=-577738/2\,677\,500\approx-0.2158$, comfortably away from $0$.

**Why a violation is hard to arrange.** A violation at $p$ needs $|\cos\theta_p|<p^{-1-\varepsilon}$; at $p=13$ that means $|\cos\theta_{13}|<0.077$, i.e. $|\tau(13)|<205\,000$. Since $\tau(p)$ is an integer of size $\sim p^{5.5}$ that behaves "randomly" in $[-2p^{5.5},2p^{5.5}]$, landing in a window of relative width $p^{-1}$ has heuristic probability $\asymp p^{-3}$, and $\sum_p p^{-3}$ converges rapidly.

**The congruence obstruction to $\tau(p)=0$.** Use the classical congruences, valid for $\gcd(n,\ell)=1$:

$$\tau(n)\equiv n^{2}\sigma_1(n)\ (\mathrm{mod}\ 3),\quad \tau(n)\equiv n\,\sigma_1(n)\ (\mathrm{mod}\ 5),\quad \tau(n)\equiv n\,\sigma_3(n)\ (\mathrm{mod}\ 7),\quad \tau(n)\equiv\sigma_{11}(n)\ (\mathrm{mod}\ 691).$$

Set $n=p$ prime, so $\sigma_s(p)=1+p^{s}$, and suppose $\tau(p)=0$:

- mod $3$: $p^{2}(1+p)\equiv0$, and $p\not\equiv0$, so $p\equiv 2\pmod 3$.
- mod $5$: $p(1+p)\equiv0$, so $p\equiv 4\pmod 5$.
- mod $7$: $p(1+p^{3})\equiv0$, so $p^{3}\equiv-1\pmod 7$, i.e. $p\equiv 3,5,6\pmod 7$.
- mod $691$: $1+p^{11}\equiv0\pmod{691}$. Since $691$ is prime and $\gcd(11,690)=1$, the map $x\mapsto x^{11}$ is a bijection on $(\mathbb{Z}/691)^\times$, so exactly one residue class mod $691$ survives.

Multiplying densities: $\frac{1}{2}\cdot\frac{1}{4}\cdot\frac{3}{6}\cdot\frac{1}{690}\approx 9.1\times10^{-5}$ of all primes remain admissible (further $2$-adic and $23$-adic conditions from Swinnerton-Dyer shrink this more). So candidate counterexamples are extremely sparse — yet this argument, being purely a congruence restriction, removes only positive-density classes and can never reduce the candidate set to a finite one. That is precisely the gap of §6, in miniature.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*