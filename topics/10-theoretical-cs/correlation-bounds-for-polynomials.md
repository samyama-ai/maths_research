---
id: 10-theoretical-cs/correlation-bounds-for-polynomials
title: "Correlation Bounds for Polynomials"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Correlation Bounds for Polynomials

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/correlation-bounds-for-polynomials` · **Status:** open

## 1. Problem Statement / Conjecture

Fix the field $\mathbb{F}_2$. For a Boolean function $f:\{0,1\}^n\to\{0,1\}$ and an integer $d\ge 1$, define the **correlation of $f$ with degree-$d$ polynomials**
$$\mathrm{Corr}(f,d)\;=\;\max_{\substack{p\in\mathbb{F}_2[x_1,\dots,x_n]\\ \deg p\le d}}\ \bigl|\ \mathbb{E}_{x\sim\{0,1\}^n}\bigl[(-1)^{f(x)+p(x)}\bigr]\ \bigr| .$$
Equivalently, $\mathrm{Corr}(f,d)=\max_p |2\Pr_x[f(x)=p(x)]-1|$.

**The open problem.** Exhibit an *explicit* function $f$ — computable in deterministic polynomial time, or at minimum in $\mathsf{NP}$ or $\mathsf{E}^{\mathsf{NP}}$ — with
$$\mathrm{Corr}(f,\ \log_2 n)\ \le\ n^{-\omega(1)},$$
and more ambitiously $\mathrm{Corr}(f,d)\le 2^{-n^{\Omega(1)}}$ for $d=\log^2 n$ or $d=n^{0.1}$.

A complete solution is a proof, for a named uniform family $\{f_n\}$, of an upper bound on $\mathrm{Corr}(f_n,d)$ in the stated degree regime. A counting argument shows a *random* $f$ satisfies $\mathrm{Corr}(f,d)\le O\!\bigl(\sqrt{\binom{n}{\le d}/2^{n}}\bigr)=2^{-\Omega(n)}$ for $d\le n/100$; the difficulty is entirely in explicitness. No non-explicit or diagonalization-based construction counts.

## 2. Mathematical Foundations

**Polynomials.** Every $f:\mathbb{F}_2^n\to\mathbb{F}_2$ has a unique multilinear representation $f(x)=\sum_{S\subseteq[n]}c_S\prod_{i\in S}x_i$ with $c_S\in\mathbb{F}_2$; $\deg f=\max\{|S|:c_S\neq 0\}$. Degree-$d$ polynomials are exactly the codewords of the Reed–Muller code $\mathrm{RM}(d,n)$, of dimension $\binom{n}{\le d}=\sum_{i\le d}\binom{n}{i}$. So $\mathrm{Corr}(f,d)$ is a normalized measure of the distance from $f$ to $\mathrm{RM}(d,n)$: $\mathrm{Corr}(f,d)=1-2\delta$ where $\delta$ is the relative distance to the nearest codeword.

**Bias and Gowers norms.** Write $F=(-1)^f$. The $U^k$ Gowers uniformity norm is
$$\|F\|_{U^k}^{2^k}\;=\;\mathbb{E}_{x,y_1,\dots,y_k}\ \prod_{S\subseteq[k]}F\Bigl(x+\sum_{i\in S}y_i\Bigr).$$
Since a derivative $\Delta_y p(x)=p(x+y)-p(x)$ lowers degree by one, $\deg p\le d$ implies $\|(-1)^p\|_{U^{d+1}}=1$, and repeated Cauchy–Schwarz gives the fundamental inequality
$$\mathrm{Corr}(f,d)\ \le\ \|F\|_{U^{d+1}} .$$
The converse — the **inverse conjecture for the Gowers norms** — is a theorem (Bergelson–Tao–Ziegler in high characteristic; Tao–Ziegler in low characteristic, where the correlating object may be a *non-classical* polynomial taking values in $\mathbb{T}=\mathbb{R}/\mathbb{Z}$), but only qualitatively: $\|F\|_{U^{d+1}}\ge\varepsilon$ yields correlation $\ge c(\varepsilon,d)$ with $c$ of tower/ineffective type.

**Why the problem matters.** Razborov–Smolensky: a depth-$h$, size-$s$ $\mathsf{AC}^0[\oplus]$ circuit is computed, with error $\epsilon$, by a random $\mathbb{F}_2$-polynomial of degree $O(\log(s/\epsilon))^{h-1}$. Hence any explicit $f$ with $\mathrm{Corr}(f,d)$ small for $d=\log^{h-1}s$ gives average-case lower bounds against $\mathsf{AC}^0[\oplus]$ of depth $h$. Small correlation is also the hypothesis of the Nisan–Wigderson generator, so bounds at degree $\log n$ with error $n^{-\omega(1)}$ feed directly into pseudorandom generators and $\\#\mathsf{SAT}$ algorithms.

## 3. History & State of the Art (SOTA)

- **1987.** Razborov (*Mat. Zametki*) and Smolensky (STOC) introduce the polynomial method; $\mathrm{MOD}_3$ and $\mathrm{MAJ}$ are shown hard for low-degree $\mathbb{F}_2$ polynomials, yielding the first $\mathsf{AC}^0[\oplus]$ lower bounds.
- **1993.** Smolensky (FOCS, *On representations by low-degree polynomials*) proves any degree-$d$ polynomial agrees with $\mathrm{MAJ}_n$ on at most $\tfrac12+O(d/\sqrt n)$ of inputs — nontrivial all the way to $d=o(\sqrt n)$, but only inverse-polynomially small.
- **2005.** Bourgain (*C. R. Acad. Sci. Paris*) proves exponentially small correlation $\exp(-n/c^d)$ between $\mathrm{MOD}_3$ and degree-$d$ $\mathbb{F}_2$ polynomials; Green–Roy–Straubing repair a gap and simplify.
- **2008.** Viola–Wigderson (*Theory of Computing*) give a clean directional-derivative/Gowers-norm proof of $\mathrm{Corr}(\mathrm{MOD}_3,d)\le\exp(-\Omega(n/4^{d}))$, plus XOR lemmas for the $U^k$ norms.
- **2009.** Viola's SIGACT News survey crystallizes the frontier as the "**$\log n$ degree barrier**".
- **2015.** Bhowmick–Lovett (CCC) show non-classical polynomials obstruct the higher-order-Fourier route.
- **2019–2021.** Chattopadhyay–Hatami–Hosseini–Lovett and Chattopadhyay–Hatami–Lovett–Tal build PRGs from Fourier-level bounds; Viola (ICALP 2021) reduces stronger correlation bounds for $\mathrm{MAJ}$ to Fourier-tail conjectures.

**SOTA in one line.** For $d\le \varepsilon\log_2 n$ we have explicit $2^{-\Omega(n/4^d)}$ bounds; for $\log_2 n\le d=o(\sqrt n)$ the best explicit bound for *any* function is $\tilde O(1/\sqrt n)$. Nothing $n^{-\omega(1)}$ is known at $d=\log_2 n$.

## 4. Partial Results / Verified Cases

| Regime | Function | Best bound | Source |
|---|---|---|---|
| $d=1$ | $\mathrm{IP}_n(x,y)=\sum x_iy_i$ | $2^{-n/2}$, exactly tight (bent) | Rothaus/folklore |
| $d=2$ | $\mathrm{MOD}_3$ | $2^{-\Omega(n)}$ (via Dickson's classification of quadratic forms) | Razborov 1987 |
| $d$ constant | $\mathrm{MOD}_3$, $\mathrm{MOD}_m$ ($m$ odd) | $\exp(-\Omega(n/4^{d}))$ | Bourgain 2005; Green–Roy–Straubing 2005; Viola–Wigderson 2008 |
| $d\le\varepsilon\log_2 n$ | $\mathrm{MOD}_3$ | $2^{-n^{1-o(1)}}$ | as above |
| $d=o(\sqrt n)$ | $\mathrm{MAJ}_n$ and most symmetric $f$ | $O(d/\sqrt n)$ | Smolensky 1993 |
| $d\le n/100$, random $f$ | non-explicit | $2^{-\Omega(n)}$ | counting |
| $d\le n$, worst case | explicit $f$ of degree $>d$ | $<1$ trivially; distance bounds from Reed–Muller weight distribution | Kaufman–Lovett 2012 |
| multilinear/tensor forms | explicit $d$-linear forms | correlation $2^{-\Omega(n)}$ against degree $d-1$ for $d\le\log n$ | Bhrushundi–Harsha–Hatami–Kopparty–Kumar 2020 |

Computationally, $\mathrm{Corr}(f,d)$ has been evaluated exactly by exhaustive search over $\mathrm{RM}(d,n)$ only for tiny $n$ ($n\le 8$ for $d=2,3$), since $|\mathrm{RM}(d,n)|=2^{\binom{n}{\le d}}$.

## 5. Principal Obstacles

- **Derivative loss.** The only general technique — bounding $\|F\|_{U^{d+1}}$ by Cauchy–Schwarz over $d$ directional derivatives — costs a $2^{-d}$ power at each step: a bound $\epsilon$ on the final $d$-fold derivative correlation yields only $\epsilon^{1/2^{d}}$ on $\mathrm{Corr}(f,d)$. This is exactly why $\exp(-n/4^d)$ becomes vacuous at $d\approx\tfrac12\log_2 n$.
- **Lossy inverse theorems.** The inverse conjecture for $U^{d+1}$ converts small correlation into small Gowers norm only with tower-type or unspecified constants (Bergelson–Tao–Ziegler; Tao–Ziegler), so it cannot certify $n^{-\omega(1)}$ correlation.
- **Non-classical polynomials.** Bhowmick–Lovett show that in low characteristic the natural higher-order Fourier objects include $\mathbb{T}$-valued non-classical polynomials, which correlate with structured functions and so block attempts to transfer regularity-based structure theorems into classical correlation bounds.
- **Symmetric functions cap out.** Every symmetric $f$ is determined by $|x|$, and low-degree polynomials already approximate the $O(\sqrt n)$-width window around $n/2$; correlation for symmetric $f$ cannot beat $\Omega(1/\sqrt n)$ for $d=\Omega(\log n)$. Progress requires genuinely non-symmetric candidates, for which no analytic handle exists.
- **Natural-proofs pressure.** Correlation is a large, constructive property of truth tables; a technique proving $2^{-n^{\Omega(1)}}$ bounds for degree $n^{\Omega(1)}$ would be close to a natural property against strong circuit classes.

## 6. The Gap

Proven: exponential bounds for $d<\tfrac12\log_2 n$; polynomial bounds ($\Theta(1/\sqrt n)$) for $d$ up to $\sqrt n$. Wanted: any explicit $f$ with $\mathrm{Corr}(f,\log_2 n)\le n^{-\omega(1)}$.

The gap is a single quantitative step: replace the $2^{-d}$-th-power loss of iterated Cauchy–Schwarz by a derivative argument whose loss is $\mathrm{poly}(d)$ rather than exponential in $d$, or find a non-Gowers certificate of distance from $\mathrm{RM}(\log n, n)$. Concretely: prove $\mathrm{Corr}(f,d)\le \exp(-n/d^{O(1)})$ for a single explicit $f$. Even $\mathrm{Corr}(f,\log_2 n)\le 1/n$ — a factor $\sqrt n$ past Smolensky's $\mathrm{MAJ}$ bound — is open.

## 7. Current Research (as of June 2026)

- **Fourier-tail routes.** Viola (ICALP 2021) shows that conjectured bounds on the Fourier mass of $\mathrm{MAJ}$ at level $k$ would imply improved correlation bounds; Chattopadhyay–Hatami–Lovett–Tal (ITCS 2019) turn second-level Fourier bounds into PRGs for $\mathsf{AC}^0[\oplus]$. Groups at Northeastern (Viola), UC San Diego (Lovett), TIFR/IIT Bombay (Harsha, Chattopadhyay), and Tel Aviv (Tal) drive this line.
- **Tensor rank and multilinear forms.** Bhrushundi–Harsha–Hatami–Kopparty–Kumar link bias of $d$-linear forms to tensor rank; explicit high-rank tensors would give correlation bounds at degree $d-1$. *(frontier — verify)* recent claims of super-linear rank lower bounds for explicit order-$3$ tensors do not yet reach the degree-$\log n$ regime.
- **Non-classical structure theory.** Continuing work on quantitative inverse theorems for $U^4$ over $\mathbb{F}_2$ aims at polynomial-in-$\varepsilon$ bounds; success at $U^4$ would give the first improvement at degree $3$ for functions other than $\mathrm{MOD}_3$.
- **Algorithmic method.** Following Williams' $\mathsf{ACC}^0$ lower bounds, several groups seek *algorithmic* substitutes for correlation bounds (fast $\\#\mathsf{SAT}$ for degree-$\log n$ polynomials), which would yield lower bounds without an analytic correlation estimate.

## 8. Future Work

1. **Break the $4^{-d}$ loss.** Find a derivative scheme (random restrictions composed with derivatives; sub-additive pseudo-norms) whose degradation is $\mathrm{poly}(d)$.
2. **New candidate hard functions.** Non-symmetric, algebraically structured candidates: $\mathrm{MOD}_3$ of a designed encoding, Paley-graph-type quadratic-residue functions, or determinant/permanent restricted to $\mathbb{F}_2$.
3. **Quantitative $U^4$ inverse theorem over $\mathbb{F}_2$** with $\varepsilon^{O(1)}$ dependence, avoiding regularity lemmas.
4. **Reduce to XOR lemmas.** Viola–Wigderson give XOR lemmas for Gowers norms; a *correlation* XOR lemma amplifying $1-1/n$ to $2^{-n^{\Omega(1)}}$ at fixed degree would immediately transfer $\mathrm{MAJ}$-type bounds upward.
5. **Explicit high-rank tensors** of order $\log n$, which would settle the multilinear special case.

## 9. Key References

- **[Foundational]** A. A. Razborov. *Lower bounds on the size of bounded depth circuits over a complete basis with logical addition.* Matematicheskie Zametki 41(4), 598–607, 1987.
- **[Foundational]** R. Smolensky. *Algebraic methods in the theory of lower bounds for Boolean circuit complexity.* STOC 1987, 77–82.
- **[Foundational]** R. Smolensky. *On representations by low-degree polynomials.* FOCS 1993, 130–138.
- **[SOTA]** J. Bourgain. *Estimation of certain exponential sums arising in complexity theory.* C. R. Acad. Sci. Paris, Ser. I 340(9), 627–631, 2005.
- **[SOTA]** F. Green, A. Roy, H. Straubing. *Bounds on an exponential sum arising in Boolean circuit complexity.* C. R. Acad. Sci. Paris, Ser. I 341(5), 279–282, 2005.
- **[SOTA]** E. Viola, A. Wigderson. *Norms, XOR lemmas, and lower bounds for polynomials and protocols.* Theory of Computing 4, 137–168, 2008.
- **[Survey]** E. Viola. *Guest column: correlation bounds for polynomials over $\{0,1\}$.* ACM SIGACT News 40(1), 27–44, 2009.
- **[Structure]** V. Bergelson, T. Tao, T. Ziegler. *An inverse theorem for the uniformity seminorms associated with the action of $\mathbb{F}_p^\infty$.* Geometric and Functional Analysis 19(6), 1539–1596, 2010.
- **[Structure]** T. Tao, T. Ziegler. *The inverse conjecture for the Gowers norm over finite fields in low characteristic.* Annals of Combinatorics 16(1), 121–188, 2012.
- **[Barrier]** A. Bhowmick, S. Lovett. *Nonclassical polynomials as a barrier to polynomial lower bounds.* CCC 2015, 72–87.
- **[Recent]** A. Chattopadhyay, P. Hatami, K. Hosseini, S. Lovett. *Pseudorandom generators from polarizing random walks.* Theory of Computing 15, 1–26, 2019.
- **[Recent]** A. Chattopadhyay, P. Hatami, S. Lovett, A. Tal. *Pseudorandom generators from the second Fourier level and applications to AC0 with parity gates.* ITCS 2019.
- **[Recent]** E. Viola. *Fourier conjectures, correlation bounds, and majority.* ICALP 2021.
- **[Recent]** A. Bhrushundi, P. Harsha, P. Hatami, S. Kopparty, M. Kumar. *On multilinear forms: bias, correlation, and tensor rank.* RANDOM 2020.
- **[Context]** B. Green, T. Tao. *The distribution of polynomials over finite fields, with applications to the Gowers norms.* Contributions to Discrete Mathematics 4(2), 1–36, 2009.

## 10. Worked Example / Concrete Special Case

**Degree $1$, inner product.** Let $n=2m$ and $\mathrm{IP}(x,y)=\sum_{i=1}^m x_iy_i \bmod 2$. Take any linear $p(x,y)=a\cdot x+b\cdot y$ (a constant term only flips a sign). The expectation factorizes over coordinates:
$$\mathbb{E}\bigl[(-1)^{\mathrm{IP}+p}\bigr]=\prod_{i=1}^m \frac14\sum_{x_i,y_i\in\{0,1\}}(-1)^{x_iy_i+a_ix_i+b_iy_i}.$$
Each inner sum has four terms $1,\ (-1)^{b_i},\ (-1)^{a_i},\ (-1)^{1+a_i+b_i}$. Enumerating: $(a_i,b_i)=(0,0)\Rightarrow 1+1+1-1=2$; $(1,0)\Rightarrow 1+1-1+1=2$; $(0,1)\Rightarrow 1-1+1+1=2$; $(1,1)\Rightarrow 1-1-1-1=-2$. So each factor is $\pm\tfrac12$ and
$$\mathrm{Corr}(\mathrm{IP},1)=2^{-m}=2^{-n/2},$$
exactly — $\mathrm{IP}$ is bent, and $2^{-n/2}$ is the minimum possible for any Boolean function (Parseval: $\sum_S \hat F(S)^2=1$ over $2^n$ characters forces $\max_S|\hat F(S)|\ge 2^{-n/2}$).

**Where it breaks.** $\mathrm{IP}$ has degree $2$, so $\mathrm{Corr}(\mathrm{IP},2)=1$: the example dies one degree up. Check the Gowers bound: $\|F\|_{U^2}=\bigl(\sum_S\hat F(S)^4\bigr)^{1/4}=(2^{n}\cdot 2^{-2n})^{1/4}=2^{-n/4}$, and indeed $2^{-n/2}\le 2^{-n/4}$ — but the $U^2$ estimate is already off by a square root. Iterating to $U^{d+1}$ compounds this: a derivative bound $\epsilon$ yields only $\epsilon^{1/2^d}$. For $\mathrm{MOD}_3$ this produces $\exp(-\Omega(n/4^d))$, which at $d=\log_2 n$ reads $\exp(-\Omega(n/n^2))=1-\Theta(1/n)$ — no information. That single line is the $\log n$ barrier in miniature.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*