---
id: 05-analysis/baker-conjecture
title: "Baker Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Baker Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/baker-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $f:\mathbb{C}\to\mathbb{C}$ be a transcendental entire function and let $F(f)$ denote its Fatou set (the set where the iterates $f^n$ form a normal family) and $J(f)=\mathbb{C}\setminus F(f)$ its Julia set. Write

$$M(r,f)=\max_{|z|=r}|f(z)|,\qquad \rho(f)=\limsup_{r\to\infty}\frac{\log\log M(r,f)}{\log r}.$$

**Baker's conjecture.** *If $\rho(f)<\tfrac12$, then every component of $F(f)$ is bounded.*

Equivalently: $J(f)$ contains unbounded continua separating every Fatou component from $\infty$. A complete proof must handle **all** entire functions of order below $1/2$, with no auxiliary regularity assumption on $\log M(r,f)$; a disproof requires exhibiting a single transcendental entire $f$ with $\rho(f)<1/2$ possessing an unbounded Fatou component (necessarily simply connected and either a wandering domain or a Baker domain, by §4).

The value $1/2$ is not arbitrary. It is the threshold in Wiman's $\cos\pi\rho$ theorem, and it is sharp for the dynamical conclusion: Fatou's function $f(z)=z+1+e^{-z}$ (order $1$) has an unbounded invariant Baker domain containing a right half-plane, and unbounded Fatou components occur already at order $1/2$.

## 2. Mathematical Foundations

**Growth.** For $\rho\ge 0$ the *type* is $\tau=\limsup_{r\to\infty}\log M(r,f)/r^{\rho}$; $f$ has **minimal type** if $\tau=0$, i.e. for every $\varepsilon>0$, $\log M(r,f)\le \varepsilon r^{\rho}$ for large $r$. Baker's *regular growth* condition is: there exist $C>1$, $r_0$ with

$$\log M(2r,f)\le C\log M(r,f),\qquad r\ge r_0 .$$

**Minimum modulus.** Put $m(r,f)=\min_{|z|=r}|f(z)|$. The central analytic input is the **$\cos\pi\rho$ theorem** (Wiman; refined by Hayman and Barry): if $\rho(f)=\rho<1/2$ and $\cos\pi\rho<\alpha<1$, then

$$\underline{\mathrm{logdens}}\;\{r>0:\ m(r,f)>M(r,f)^{\alpha}\}\ \ge\ 1-\frac{\log(1/ \alpha')}{\ldots}>0,$$

and in the weakest usable form: there is an unbounded set of $r$ with $m(r,f)>M(r,f)^{\cos\pi\rho-\varepsilon}\to\infty$. For $\rho=0$ one gets $m(r,f)>M(r,f)^{1-\varepsilon}$ on a set of logarithmic density $1$.

**Escaping and fast-escaping sets.**

$$I(f)=\{z:\ f^n(z)\to\infty\},\qquad A_R(f)=\{z:\ \exists\,\ell\in\mathbb{N},\ |f^{n+\ell}(z)|\ge M^n(R,f)\ \ \forall n\ge 0\},$$

where $M^n$ is the $n$-th iterate of $r\mapsto M(r,f)$ and $R$ exceeds the smallest fixed point of $M(\cdot,f)$. The set $A(f)=\bigcup_{\ell\ge0}f^{-\ell}(A_R(f))$ is the fast escaping set (Bergweiler–Hinkkanen); it is independent of $R$, non-empty, and $J(f)=\partial A(f)$.

**Spider's web.** A set $E\subset\mathbb{C}$ is a **spider's web** if it is connected and there exist bounded simply connected domains $G_n$ with

$$\partial G_n\subset E,\qquad G_n\subset G_{n+1},\qquad \bigcup_{n\ge0}G_n=\mathbb{C}.$$

Since $A_R(f)\subset J(f)$ when $A_R(f)$ is a spider's web (its loops lie in $J(f)$), every Fatou component is then trapped inside some $G_n$ and is bounded. This implication is the engine of all modern progress:

$$A_R(f)\ \text{is a spider's web}\ \Longrightarrow\ \text{every component of }F(f)\ \text{is bounded}.$$

The converse is false, so the "strong Baker conjecture" ($A_R(f)$ a spider's web whenever $\rho(f)<1/2$) is formally stronger.

## 3. History & State of the Art (SOTA)

- **1963.** I. N. Baker, *Multiply connected domains of normality in iteration theory* (Math. Z. 81): multiply connected Fatou components are bounded and wandering — the first structural boundedness theorem.
- **1981.** Baker, *The iteration of polynomials and transcendental entire functions* (J. Austral. Math. Soc.): proves that $F(f)$ has no unbounded components if $\rho(f)<1/2$ **and** $f$ has regular growth, and asks whether the regularity hypothesis can be dropped. This is the origin of the conjecture.
- **1993.** G. M. Stallard weakens the regularity to a condition on $\log\log M(r)$, covering all functions of order $0$ with sufficiently smooth growth.
- **1998.** J. M. Anderson and A. Hinkkanen (Proc. AMS 126) prove boundedness under a growth condition of the form $\log M(r)\le c(\log r)^{p}$ type regularity, and give geometric restrictions on hypothetical unbounded components.
- **2005–2012.** Rippon and Stallard build the theory of $A_R(f)$ and spiders' webs; they show $I(f)$ always has at least one unbounded component and that spider's-web structure of $A_R(f)$ forces bounded Fatou components, connected $I(f)$, and no unbounded wandering domains.
- **2009.** Rippon and Stallard, *Functions of small growth with no unbounded Fatou components* (J. Anal. Math. 108): the conjecture holds for **order $<1/2$, minimal type**, and for various regular-growth classes, by proving $A_R(f)$ is a spider's web. This remains the headline general result.
- **2018.** D. A. Nicks, Rippon and Stallard (Proc. LMS 117) prove the conjecture for **all** $f$ of order $<1/2$ whose zeros lie on the negative real axis — the first large class with no regularity hypothesis whatsoever.

## 4. Partial Results / Verified Cases

The conjecture is a theorem in each of the following classes.

| Class | Result |
|---|---|
| $\rho(f)<1/2$, regular growth ($\log M(2r)\le C\log M(r)$) | Baker 1981 |
| $\rho(f)<1/2$, minimal type (in particular all $0<\rho<1/2$ with $\tau=0$, and order $0$ with $\log M(r)=O((\log r)^p)$) | Rippon–Stallard 2009; $A_R(f)$ is a spider's web |
| $\rho(f)<1/2$, all zeros real and negative (canonical products $\prod(1+z/a_n)$, $a_n>0$) | Nicks–Rippon–Stallard 2018 |
| Fabry gaps: $f(z)=\sum a_{n_k}z^{n_k}$ with $n_k/k\to\infty$, finite order | Sixsmith 2011; $A_R(f)$ is a spider's web |
| Any transcendental entire $f$, **multiply connected** components | Baker 1963/1984: always bounded |
| $\rho(f)<1/2$, components containing a periodic point or lying in an attracting/parabolic/Siegel cycle | Bounded: unbounded periodic components of small-growth functions are excluded by the $\cos\pi\rho$ theorem |

Consequently a counterexample would have to be a **simply connected, unbounded, wandering or Baker domain** of a function of order $<1/2$ with irregular growth, positive type, and zeros not confined to a ray.

## 5. Principal Obstacles

- **Irregular growth defeats annulus arguments.** The proofs above compare $M(r)$ at scales $r$ and $2r$ (or $r^2$) to build nested loops on which $|f|$ is large. If $\log M(r)$ jumps — e.g. $\log M(r)$ alternately constant over long ranges and then exploding — the loop at level $n$ need not map beyond the loop at level $n+1$, and the inductive spider's-web construction breaks.
- **The $\cos\pi\rho$ theorem is only a density statement.** It supplies a *set* of radii $r$ with $m(r)$ large, of positive logarithmic density, but gives no control over *which* radii. Dynamics needs a sequence $r_n$ with $m(r_n)\ge$ (something like) $M(r_{n}) \gg r_{n+1}$, i.e. a matching between the good radii and the orbit's scale growth. No minimum-modulus theorem currently delivers that matching for arbitrary irregular $f$.
- **Failure of the strong form.** $A_R(f)$ need not be a spider's web for every function of order $<1/2$; the 2018 real-zeros work had to prove boundedness of Fatou components by direct covering arguments rather than the spider's-web route *(frontier — verify the exact scope of the counterexamples)*. So the only general mechanism known is not universally available.
- **No local obstruction.** Unbounded wandering domains are not forbidden by any local normality, harmonic-measure or hyperbolic-metric estimate at finite scale; the obstruction must be genuinely global, which is why quasiconformal surgery constructions (Bishop's folding) cannot be ruled out a priori.
- **Surgery constructions are order-limited.** Bishop-type folding produces functions in the Eremenko–Lyubich class with order at least $1$ in practice; there is no known technique for building entire functions of order $<1/2$ with prescribed exotic dynamics, so neither side of the conjecture has a constructive toolkit.

## 6. The Gap

Proven: for $\rho(f)<1/2$ **plus** any of (i) minimal type, (ii) regular growth, (iii) real negative zeros, (iv) Fabry gaps, all Fatou components are bounded. Open: $\rho(f)<1/2$ of **positive, non-minimal type with irregular growth and arbitrarily distributed zeros**, e.g. $\rho(f)=1/4$, $\tau>0$, with $\log M(r)$ oscillating between $r^{1/8}$ and $r^{1/4}$ along sparse scales.

The precise missing step: produce, for every such $f$, a sequence $r_n\to\infty$ with

$$m(r_n,f)\ \ge\ r_{n+1}\quad\text{and}\quad r_{n+1}\ \ge\ 2r_n ,$$

so that the circles $|z|=r_n$ map to curves surrounding $|z|=r_{n+1}$, generating nested loops in $J(f)$. Wiman–Barry gives $m(r)$ large on a density-positive radius set; what is missing is the *self-consistency* of that set under the map $r\mapsto m(r)$.

## 7. Current Research (as of June 2026)

- **Open University school (Rippon, Stallard) and Nottingham (Nicks).** Extending the real-zeros method to zeros in a sector $|\arg z-\pi|\le\theta$, and to functions with zeros of finite "angular density"; the minimum-modulus machinery in Nicks–Rippon–Stallard is the template *(frontier — verify)*.
- **Liverpool/Manchester (Rempe, Sixsmith, Waterman, Martí-Pete).** After the disproof of the strong Eremenko conjecture by Martí-Pete, Rempe and Waterman (wandering Lakes of Wada, maverick points), attention has turned to whether analogous approximation-theoretic constructions can be pushed below order $1/2$. Current consensus is that they cannot, which is taken as evidence *for* Baker's conjecture *(frontier — verify)*.
- **Potential-theoretic approaches.** Recasting the problem for $\delta$-subharmonic $\log|f|$ and using Baernstein star-function / Beurling–Kjellberg estimates to obtain radii sequences adapted to the orbit scales.
- **Spider's-web classification.** Ongoing work catalogues which growth classes force $A_R(f)$, $I(f)$ or $J(f)$ to be spiders' webs (Osborne, Sixsmith), sharpening exactly where the mechanism of §2 stops.

## 8. Future Work

1. **Uniform minimum-modulus theorem.** Prove: for $\rho(f)<1/2$ and any $K>1$ there are arbitrarily large $r$ with $m(r,f)\ge M(r/K,f)^{c}$, $c=c(\rho)>0$, *and* $m$ large on all of a fixed multiplicative window $[r,Kr]$. This would close the gap directly.
2. **Reduce to wandering domains.** Show that a hypothetical unbounded component must be wandering (Baker domains for order $<1/2$ are already heavily constrained), then apply the theory of orbits of wandering domains (Benini–Evdoridou–Fagella–Rippon–Stallard, 2022 classification of simply connected wandering domains).
3. **Zero-distribution program.** Interpolate between "zeros on a ray" (solved) and general zero sets by controlling $\log|f|$ via the Riesz measure.
4. **Search for a counterexample** using approximation theory (Arakelian/Runge) rather than quasiconformal surgery, since surgery cannot presently reach small order.

## 9. Key References

- **[Foundational]** I. N. Baker. *Multiply connected domains of normality in iteration theory.* Mathematische Zeitschrift 81 (1963), 206–214.
- **[Foundational]** I. N. Baker. *The iteration of polynomials and transcendental entire functions.* Journal of the Australian Mathematical Society, Series A, 30 (1981), 483–495.
- **[Foundational]** I. N. Baker. *Wandering domains in the iteration of entire functions.* Proceedings of the London Mathematical Society (3) 49 (1984), 563–576.
- **[Analytic input]** W. K. Hayman. *The minimum modulus of large integral functions.* Proceedings of the London Mathematical Society (3) 2 (1952), 469–512.
- **[Analytic input]** P. D. Barry. *The minimum modulus of small integral and subharmonic functions.* Proceedings of the London Mathematical Society (3) 12 (1962), 445–495.
- **[Partial result]** G. M. Stallard. *The iteration of entire functions of small growth.* Mathematical Proceedings of the Cambridge Philosophical Society 114 (1993), 43–55.
- **[Partial result]** J. M. Anderson and A. Hinkkanen. *Unbounded domains of normality.* Proceedings of the American Mathematical Society 126 (1998), 3243–3252.
- **[SOTA]** P. J. Rippon and G. M. Stallard. *Functions of small growth with no unbounded Fatou components.* Journal d'Analyse Mathématique 108 (2009), 61–86.
- **[SOTA]** P. J. Rippon and G. M. Stallard. *Fast escaping points of entire functions.* Proceedings of the London Mathematical Society (3) 105 (2012), 787–820.
- **[SOTA]** D. A. Nicks, P. J. Rippon and G. M. Stallard. *Baker's conjecture for functions with real zeros.* Proceedings of the London Mathematical Society (3) 117 (2018), 100–124.
- **[Related]** D. J. Sixsmith. *Entire functions for which the escaping set is a spider's web.* Mathematical Proceedings of the Cambridge Philosophical Society 151 (2011), 551–571.
- **[Survey]** W. Bergweiler. *Iteration of meromorphic functions.* Bulletin of the American Mathematical Society 29 (1993), 151–188.
- **[Survey]** A. Hinkkanen. *Entire functions with no unbounded Fatou components.* In: *Complex Analysis and Dynamical Systems II*, Contemporary Mathematics 382, AMS, 2005, 217–226.

## 10. Worked Example / Concrete Special Case

Take the canonical product with zeros at $-a_k$, $a_k=2^{k^2}$:

$$f(z)=c\prod_{k=1}^{\infty}\Big(1+\frac{z}{2^{k^2}}\Big),\qquad c>1 .$$

The zero counting function is $n(r)\approx\sqrt{\log_2 r}$, so $\log M(r,f)=O\big((\log r)^{3/2}\big)$ and $\rho(f)=0$: this lies in the solved minimal-type class, and we can see the mechanism explicitly.

**Step 1 — minimum modulus on geometric-mean circles.** For $|z|=r$, $\min_{|z|=r}|1+z/a_k|=|1-r/a_k|$. Choose $r_n=\sqrt{a_na_{n+1}}=2^{\,n^2+n+1/2}$. Then:

- For $k\le n$: $r_n/a_k=2^{\,n^2+n+1/2-k^2}\ge 2^{\,n+1/2}$, so $|1-r_n/a_k|\ge \tfrac12\, r_n/a_k$.
- For $k=n+1+j$, $j\ge0$: $r_n/a_k\le 2^{-(n+1/2)}2^{-j}$, hence

$$\prod_{k>n}\Big(1-\frac{r_n}{a_k}\Big)\ \ge\ 1-\sum_{j\ge0}2^{-(n+1/2)-j}\ =\ 1-2^{\,1/2-n}\ \ge\ \tfrac12\quad (n\ge3).$$

Therefore

$$m(r_n,f)\ \ge\ \frac{c}{2}\prod_{k\le n}\frac{r_n}{2a_k}\ =\ \frac{c}{2}\,\frac{r_n^{\,n}}{2^{\,n}\,2^{\,n(n+1)(2n+1)/6}} .$$

With $r_n^{\,n}=2^{\,n^3+n^2+n/2}$ and $\sum_{k\le n}k^2=\tfrac{n^3}{3}+O(n^2)$, the exponent is $\tfrac23 n^3+O(n^2)$, so

$$m(r_n,f)\ \ge\ 2^{\,\frac23 n^3 + O(n^2)} .$$

Meanwhile $M(r_n,f)\le c\prod_k(1+r_n/a_k)\le 2^{\,\frac23n^3+O(n^2)}$ by the same computation with $+$ signs. Hence $m(r_n,f)\ge M(r_n,f)^{1-o(1)}$ — the $\rho=0$ case of the $\cos\pi\rho$ theorem, made explicit.

**Step 2 — nested loops.** Since $m(r_n,f)=2^{\frac23n^3+O(n^2)}$ while $r_{n+1}=2^{\,n^2+3n+3/2}$, we have $m(r_n,f)>r_{n+1}$ for all large $n$ (cubic beats quadratic in the exponent). So $f$ maps the circle $C_n=\{|z|=r_n\}$ to a curve lying entirely outside $C_{n+1}$, and by induction

$$|f^{j}(z)|\ >\ r_{n+j}\quad\text{for all }z\in C_n,\ j\ge1 .$$

Iterating, every point of $C_n$ has orbit escaping at least as fast as $M^j(R,f)$ for suitable $R$, i.e. $C_n\subset A_R(f)\subset J(f)$ up to the standard maximum-principle upgrade (Rippon–Stallard: if $|f^j|\ge M^j(R)$ on a loop, the loop is in $A_R(f)$).

**Step 3 — conclusion.** The disks $G_n=\{|z|<r_n\}$ are bounded, simply connected, increasing, exhaust $\mathbb{C}$, and $\partial G_n=C_n\subset J(f)$. Thus $A_R(f)$ is a spider's web. Any Fatou component $U$ is connected and disjoint from $J(f)$, so $U$ cannot cross any $C_n$; picking $n$ with $U\cap G_n\ne\emptyset$ gives $U\subset G_n$, so $U$ is **bounded**.

What breaks in general: Step 2 used $m(r_n)>r_{n+1}$, which held because the gaps $a_{n+1}/a_n=2^{2n+1}$ are regular. For a function of order $1/4$ with wildly irregular zero clusters, the good radii supplied by Barry's theorem may all fall in windows where $M$ has just jumped, so no sequence with $m(r_n)>r_{n+1}$ is known to exist. That single inequality is the content of the open conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*