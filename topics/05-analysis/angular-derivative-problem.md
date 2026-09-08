---
id: 05-analysis/angular-derivative-problem
title: "The Angular Derivative Problem for Inner Functions"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Angular Derivative Problem for Inner Functions

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/angular-derivative-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mathbb{D}=\{z:|z|<1\}$ and let $\varphi:\mathbb{D}\to\mathbb{D}$ be holomorphic. For $\zeta\in\partial\mathbb{D}$, $\varphi$ is said to **have a finite angular derivative at $\zeta$** if

$$\alpha(\zeta)\;:=\;\liminf_{z\to\zeta}\frac{1-|\varphi(z)|}{1-|z|}\;<\;\infty .$$

**The angular derivative problem (ADP).** Give a criterion — computable from the data that presents the map — deciding whether $\alpha(\zeta)<\infty$.

Two presentations matter, and they are not equivalent in difficulty.

- **Analytic form (inner functions).** $\varphi$ inner means $|\varphi^*(e^{i\theta})|=1$ a.e. Given the canonical factorization $\varphi = \lambda\prod_n b_{a_n}\cdot S_\mu$, decide $\alpha(\zeta)<\infty$ from $\{a_n\}$ and $\mu$. **Solved** (Section 4).
- **Geometric form (Rodin–Warschawski).** Let $\Omega$ be a simply connected domain contained in the strip $S=\{w:|\operatorname{Im}w|<\pi/2\}$ with $+\infty$ accessible. Let $f:S\to\Omega$ be conformal with $f(w)\to\infty$ as $\operatorname{Re}w\to+\infty$. Decide, **from the shape of $\Omega$ alone**, whether $f$ has a finite angular derivative at $+\infty$, i.e. whether $f(w)-w$ tends to a finite limit in every half-strip $\{\operatorname{Re}w>x_0,\ |\operatorname{Im}w|<\pi/2-\varepsilon\}$. **Open in general.**

A complete solution of the geometric form means: a condition on $\Omega$, stated in terms of Euclidean/metric data (widths, extremal lengths, harmonic measure) and verifiable without solving the mapping problem, that is both necessary and sufficient. The two forms are linked because every inner function with a boundary fixed point admits a linearization model in which the fixed-point multiplier *is* the angular derivative of a Riemann map.

## 2. Mathematical Foundations

**Julia–Carathéodory theorem.** For holomorphic $\varphi:\mathbb{D}\to\mathbb{D}$ and $\zeta\in\partial\mathbb{D}$, the following are equivalent: (i) $\alpha(\zeta)<\infty$; (ii) $\varphi$ has a nontangential limit $\omega\in\partial\mathbb{D}$ at $\zeta$ and $\varphi'$ has a nontangential limit at $\zeta$. In that case

$$\angle\lim_{z\to\zeta}\varphi'(z)=\alpha(\zeta)\,\overline{\zeta}\,\omega,\qquad \alpha(\zeta)>0,$$

and $\varphi$ maps every Stolz angle at $\zeta$ into a Stolz angle at $\omega$ (Julia's lemma: the horodisc $\{|\zeta-z|^2<c(1-|z|^2)\}$ maps into $\{|\omega-w|^2<\alpha c\,(1-|w|^2)\}$).

**Canonical factorization.** Every inner $\varphi$ is $\varphi(z)=\lambda\prod_n \frac{|a_n|}{a_n}\frac{a_n-z}{1-\overline{a_n}z}\cdot\exp\!\Big(-\int_{\partial\mathbb{D}}\frac{e^{i\theta}+z}{e^{i\theta}-z}\,d\mu(e^{i\theta})\Big)$, with $\sum_n(1-|a_n|)<\infty$ and $\mu\ge 0$ singular.

**Ahern–Clark / Frostman criterion.** For such $\varphi$ and $\zeta\in\partial\mathbb{D}$,

$$\alpha(\zeta)\;=\;\sum_{n}\frac{1-|a_n|^{2}}{|\zeta-a_n|^{2}}\;+\;2\int_{\partial\mathbb{D}}\frac{d\mu(e^{i\theta})}{|\zeta-e^{i\theta}|^{2}},$$

finite or infinite; $\alpha(\zeta)<\infty$ exactly when the right side converges.

**Denjoy–Wolff point.** If $\varphi$ is not an elliptic automorphism there is a unique $\tau\in\overline{\mathbb{D}}$ with $\varphi^{\circ n}\to\tau$. If $\tau\in\partial\mathbb{D}$ then $\alpha(\tau)\le 1$, and $\varphi$ is *hyperbolic* if $\alpha(\tau)<1$, *parabolic* if $\alpha(\tau)=1$.

**Strip model and Ahlfors distortion.** Put $\Omega\subseteq S$ and let $\theta(t)=|\{y:t+iy\in\Omega\}|$ (length of the vertical section, $\theta(t)\le\pi$ for the normalization $S=\{|\operatorname{Im}w|<\pi/2\}$ rescaled to width $\pi$). Ahlfors' distortion theorem gives, for the conformal $f:S\to\Omega$,

$$\operatorname{Re}f^{-1}(x+iy)\;=\;\pi\!\int_{x_0}^{x}\frac{dt}{\theta(t)}\;+\;O(1)$$

under mild regularity. Since a finite nonzero angular derivative forces $f(w)=w+c+o(1)$, the convergence of

$$\mathcal{I}(\Omega)\;=\;\int^{\infty}\Big(\frac{1}{\theta(t)}-\frac{1}{\pi}\Big)dt \tag{$\ast$}$$

is a **necessary** condition when $\Omega\subseteq S$. It is *not* sufficient.

**Extremal length.** With $\Gamma_{a,b}$ the family of crosscuts of $\Omega$ separating $\{ \operatorname{Re}w=a\}$ from $\{\operatorname{Re}w=b\}$, the module $\lambda(\Gamma_{a,b})$ is conformally invariant; $\mathcal{I}(\Omega)$ is the naive Euclidean surrogate for $\lim (\lambda_\Omega-\lambda_S)$, and the ADP is the question of when the surrogate can be corrected into an exact criterion.

## 3. History & State of the Art (SOTA)

- **1920–1929.** Julia, Wolff and Carathéodory establish the boundary Schwarz lemma; the angular derivative enters as the sharp constant in Julia's lemma.
- **1930.** Ahlfors' thesis-era distortion theorem for strip domains supplies the first geometric handle: $\pi\int dt/\theta(t)$ controls the map up to $O(1)$.
- **1942.** Frostman computes $|\varphi'|$ on $\partial\mathbb{D}$ for Blaschke products, yielding the series form of $\alpha(\zeta)$.
- **1942–1967.** Warschawski gives successive sufficient conditions for existence of the angular derivative for strip domains ($\theta$ of bounded variation, $\theta$ Lipschitz, smallness of $\theta-\pi$ in integral norms).
- **1970–1974.** Ahern and Clark characterize existence of nontangential limits of $\varphi$ and its higher derivatives for inner functions and for functions in model spaces $K_\varphi$ — the analytic form of the ADP is settled.
- **1971, 1977.** Jenkins and Oikawa sharpen Ahlfors–Warschawski and separate *conformality* from *semiconformality* at a boundary point.
- **1976–1977.** Rodin and Warschawski publish the extremal-length formulation and pose the ADP as an explicit open problem: find a geometric necessary-and-sufficient condition. They also construct domains where $(\ast)$ converges but no angular derivative exists.
- **1986.** Burdzy solves the ADP probabilistically: existence of the angular derivative is equivalent to a statement about Brownian excursions / minimal thinness of $\Omega^c$ at the boundary point. This is a genuine characterization, but the condition is expressed in terms of Brownian paths, not Euclidean geometry.
- **1988.** Carroll gives a classical potential-theoretic proof of Burdzy's theorem, removing probability but not the non-effectivity.
- **1995–2010.** Sastry, Poggi-Corradini, Contreras–Díaz-Madrigal–Pommerenke extend the theory to non-Denjoy–Wolff fixed points, second angular derivatives, and parabolic iteration.
- **Present.** Analytic form: closed. Geometric form: characterized but not *decidable by inspection*; explicit criteria exist only on structured classes.

## 4. Partial Results / Verified Cases

- **Finite Blaschke products.** $\alpha(\zeta)=\sum_{n=1}^{N}\frac{1-|a_n|^2}{|\zeta-a_n|^2}<\infty$ at every $\zeta\in\partial\mathbb{D}$; the angular derivative is finite everywhere and $\varphi$ extends analytically across $\partial\mathbb{D}$.
- **All inner functions, all $\zeta$ (analytic data).** The Ahern–Clark series/integral criterion of Section 2 is a complete answer given $\{a_n\}$ and $\mu$.
- **Singular inner functions.** For $\varphi=S_{\delta_1}$, $\alpha(1)=\infty$; for $\zeta\ne 1$, $\alpha(\zeta)=2/|\zeta-1|^2<\infty$. So the exceptional set can be a single point.
- **Denjoy–Wolff point.** $\alpha(\tau)\le 1$ always; for inner $\varphi$ fixing $0$, $\alpha(\zeta)\ge 1$ at every boundary fixed point (Löwner-type inequality).
- **Arbitrary simply connected $\Omega\subseteq S$.** Burdzy (1986) and Carroll (1988) give a necessary and sufficient condition in terms of minimal thinness of $S\setminus\Omega$ at $+\infty$ in the Martin topology / a Brownian excursion criterion.
- **Comb and slit domains.** For $\Omega=S\setminus\bigcup_k \sigma_k$ with vertical slits $\sigma_k$ at $x=x_k$ of height $h_k$, the criterion reduces to explicit series in $(x_k,h_k)$; Burdzy's condition is checkable. For evenly spaced slits with $x_k=k$, finiteness is governed by $\sum_k h_k^2<\infty$-type conditions *(class-dependent — verify the normalization for each family)*.
- **Regular width functions.** If $\theta(t)\le\pi$, $\theta(t)\to\pi$, and $\theta$ is monotone, or of bounded variation, or Lipschitz, then $(\ast)$ convergent $\Rightarrow$ finite angular derivative (Warschawski; Rodin–Warschawski; Sastry 1995 for a wider class of strip domains).
- **Non-Denjoy–Wolff boundary fixed points.** Poggi-Corradini (1998) shows every boundary fixed point of a self-map with interior Denjoy–Wolff point at which a finite angular derivative exists admits a linearizing model; the set of such points is countable when $\alpha$ is bounded on it.

## 5. Principal Obstacles

- **$(\ast)$ is blind to oscillation.** The Ahlfors integral averages the width. Rodin–Warschawski's counterexamples keep $\int(1/\theta-1/\pi)\,dt$ finite while making $\theta$ oscillate on a sparse sequence of scales; the accumulated *phase* distortion, invisible to the average, destroys convergence of $f(w)-w$. Any purely integral condition on $\theta$ therefore fails.
- **Non-locality of harmonic measure.** Whether $f(w)-w$ converges depends on the interaction between constrictions at widely separated scales. Extremal length is subadditive but not additive, and the defect $\lambda_\Omega-\lambda_S$ is not a sum of local contributions.
- **The known characterization is non-effective.** Minimal thinness at a Martin boundary point is itself a Wiener-type series whose evaluation requires capacities of the complement at every scale — precisely the data one wanted to avoid computing. It converts the ADP into an equally hard potential-theory problem.
- **Failure of perturbation.** $\alpha$ is not continuous under uniform convergence of maps or Hausdorff convergence of domains: an $\varepsilon$-thin slit family can flip $\alpha$ from finite to infinite. So approximation by nice domains cannot transfer the criterion.
- **Fourier methods do not see the tangential regime.** For Blaschke products the borderline occurs when zeros approach $\zeta$ tangentially at a precisely tuned rate; the relevant sums $\sum(1-|a_n|^2)/|\zeta-a_n|^2$ sit exactly at the threshold where Carleson-measure and $L^p$-boundedness techniques give no gain.
- **No conformally invariant Euclidean quantity is known** that both dominates the defect and is computable from $\partial\Omega$ by a Whitney-type decomposition.

## 6. The Gap

Proved (Section 4): the answer is known as a *series in the canonical factorization* (analytic side), and as a *potential-theoretic equivalence* (geometric side, Burdzy–Carroll). Also proved: $(\ast)$ is necessary, and sufficient under one-sided regularity of $\theta$.

Wanted (Section 1): a condition $C(\Omega)$ built from Euclidean boundary data — widths, slit heights, Whitney-cube capacities in a *finite* combination — such that

$$\text{$f$ has a finite angular derivative at $+\infty$} \iff C(\Omega).$$

The exact missing step is a **quantitative comparison between the extremal-length defect and a scale-by-scale Euclidean functional**, valid without any regularity assumption on $\theta$. Equivalently: replace "minimal thinness of $S\setminus\Omega$ at $+\infty$" by a Wiener-type criterion whose terms are explicit geometric quantities and whose convergence can be tested for an arbitrary closed set. On the inner-function side, the parallel gap is: characterize which subsets $E\subseteq\partial\mathbb{D}$ arise as $\{\zeta:\alpha(\zeta)<\infty\}$ for an inner function, with prescribed growth of $\alpha$ on $E$.

## 7. Current Research (as of June 2026)

- **Semigroups and continuous iteration.** Groups around Contreras, Díaz-Madrigal (Sevilla) and Betsakos (Thessaloniki) study rates of convergence to the Denjoy–Wolff point, where the angular derivative is the exponential rate; the Koenigs domain of a semigroup is exactly a strip-type domain, so ADP criteria transfer directly. *(frontier — verify)* recent preprints claim sharp two-sided estimates for the orbit rate in terms of the harmonic measure of the Koenigs domain.
- **Model spaces and one-component inner functions.** Work on $K_\varphi$, embedding measures, and Clark measures uses the Ahern–Clark condition as an input; the open questions concern uniform control of $\alpha$ over families rather than pointwise existence.
- **Composition operators.** Compactness and essential norms of $C_\varphi$ on $H^2$ and on Dirichlet-type spaces are governed by $\inf_\zeta\alpha(\zeta)$; the geometric ADP resurfaces when $\varphi$ is given by its image domain.
- **Potential-theoretic effectivization.** Attempts to convert minimal thinness into Whitney-decomposition Wiener series (in the spirit of Aikawa's work on quasiadditivity of capacity) are the most direct current line on the true gap. *(frontier — verify)*
- **Numerical conformal mapping.** Zipper/Schwarz–Christoffel computations on comb domains are used to probe borderline families and to search for new counterexamples to candidate integral criteria.

## 8. Future Work

- Build a Whitney/Wiener criterion: decompose $S\setminus\Omega$ into dyadic boxes $Q_k$ along the axis, and seek an equivalence between finiteness of $\alpha$ and convergence of $\sum_k \operatorname{cap}(Q_k\cap\Omega^c)\,\ell(Q_k)^{-1}$-type series, using quasiadditivity of capacity to replace minimal thinness.
- Isolate the exact regularity threshold on $\theta$ at which $(\ast)$ becomes sufficient — currently bounded variation suffices and mere continuity does not; the sharp modulus-of-continuity condition is unknown.
- Classify the possible sets $\{\zeta:\alpha(\zeta)<\infty\}$ for inner functions, together with attainable profiles of $\alpha$ on them.
- Develop stability: quantify how much $\alpha$ can change under a perturbation of $\partial\Omega$ of prescribed capacity, to obtain approximation-based proofs.
- Extend to several variables: the Julia–Carathéodory theorem holds on the ball, but no geometric ADP is formulated for pseudoconvex domains.

## 9. Key References

- **[Foundational]** G. Julia. *Extension nouvelle d'un lemme de Schwarz.* Acta Mathematica **42**, 349–355, 1920.
- **[Foundational]** C. Carathéodory. *Conformal Representation.* Cambridge University Press, 1932.
- **[Foundational]** O. Frostman. *Sur les produits de Blaschke.* Kungl. Fysiografiska Sällskapets i Lund Förhandlingar **12**, 169–182, 1942.
- **[Foundational]** P. R. Ahern and D. N. Clark. *Radial limits and invariant subspaces.* American Journal of Mathematics **92**, 332–342, 1970.
- **[Foundational]** P. R. Ahern and D. N. Clark. *On inner functions with $H^p$ derivative.* Michigan Mathematical Journal **21**, 115–127, 1974.
- **[Foundational]** B. Rodin and S. E. Warschawski. *Extremal length and the boundary behavior of conformal mappings.* Annales Academiae Scientiarum Fennicae, Series A I Mathematica **2**, 467–500, 1976.
- **[Foundational]** B. Rodin and S. E. Warschawski. *Extremal length and univalent functions I: The angular derivative.* Mathematische Zeitschrift **153**, 1–17, 1977.
- **[SOTA]** K. Burdzy. *Brownian excursions and minimal thinness III: Applications to the angular derivative problem.* Mathematische Zeitschrift **192**, 89–107, 1986.
- **[SOTA]** T. Carroll. *A classical proof of Burdzy's theorem on the angular derivative.* Journal of the London Mathematical Society (2) **38**, 423–441, 1988.
- **[SOTA]** S. Sastry. *Existence of an angular derivative for a class of strip domains.* Proceedings of the American Mathematical Society **123**, 1075–1082, 1995.
- **[SOTA]** P. Poggi-Corradini. *Angular derivatives at boundary fixed points for self-maps of the disk.* Proceedings of the American Mathematical Society **126**, 1697–1708, 1998.
- **[SOTA]** M. D. Contreras, S. Díaz-Madrigal and Ch. Pommerenke. *Second angular derivatives and parabolic iteration in the unit disk.* Transactions of the American Mathematical Society **362**, 357–388, 2010.
- **[Survey]** Ch. Pommerenke. *Boundary Behaviour of Conformal Maps.* Springer-Verlag, Grundlehren 299, 1992 (Chapters 4 and 11).
- **[Survey]** J. H. Shapiro. *Composition Operators and Classical Function Theory.* Springer-Verlag, 1993 (Chapter 4).
- **[Survey]** J. Mashreghi. *Derivatives of Inner Functions.* Fields Institute Monographs 31, Springer, 2013.
- **[Survey]** J. Jenkins and K. Oikawa. *On results of Ahlfors and Hayman.* Illinois Journal of Mathematics **15**, 664–671, 1971.
- **[Related]** G. T. Cargo. *Angular and tangential limits of Blaschke products and their successive derivatives.* Canadian Journal of Mathematics **14**, 334–348, 1962.

## 10. Worked Example / Concrete Special Case

**A tangential Blaschke product where the answer flips.** Fix $\zeta=1$ and take zeros $a_n = r_n e^{i\theta_n}$ with $r_n = 1-2^{-n}$, so $\sum(1-|a_n|)=\sum 2^{-n}=1<\infty$ and the Blaschke product $B$ converges. Then

$$|1-a_n|^2 = (1-r_n)^2 + 2r_n(1-\cos\theta_n) \asymp 4^{-n} + \theta_n^2 ,\qquad 1-|a_n|^2 \asymp 2\cdot 2^{-n}.$$

*Radial zeros, $\theta_n=0$.* Then $|1-a_n|^2 = 4^{-n}$ and

$$\alpha(1)=\sum_n \frac{1-r_n^2}{(1-r_n)^2}\asymp \sum_n 2\cdot 2^{n} = \infty .$$

No angular derivative at $1$; $B$ has no nontangential limit of modulus controlled near $1$.

*Strongly tangential zeros, $\theta_n = 2^{-n/4}$.* Now $\theta_n^2 = 2^{-n/2}\gg 4^{-n}$, so $|1-a_n|^2\asymp 2^{-n/2}$ and

$$\alpha(1)\;\asymp\;\sum_{n\ge1}\frac{2\cdot 2^{-n}}{2^{-n/2}}\;=\;2\sum_{n\ge1}2^{-n/2}\;=\;\frac{2}{2^{1/2}-1}\approx 4.83\;<\;\infty .$$

So $B$ **has** a finite angular derivative at $1$, with $\angle\lim_{z\to1}B'(z)$ existing and $|B'(1)|=\alpha(1)$; every Stolz angle at $1$ is mapped into a Stolz angle at $\omega=\angle\lim B(z)$.

*The threshold.* Take $\theta_n=2^{-n/2}$. Then $|1-a_n|^2\asymp 2^{-n}$ and each term is $\asymp 2$: the series diverges. Slowing the tangential approach by any factor $2^{-\varepsilon n}$ in the exponent restores convergence. The finite/infinite dichotomy therefore sits at an exponentially sharp rate — this is the analytic shadow of why no coarse averaged quantity can decide the geometric ADP.

*Geometric side of the same phenomenon.* Consider $\Omega = S\setminus\bigcup_{k\ge1}\sigma_k$, $S$ the strip of width $\pi$, with vertical slits $\sigma_k$ at $x=k$ of height $h_k$ rising from the lower edge. Then $\theta(t)=\pi$ off the slit abscissae, so $\mathcal{I}(\Omega)=\int(1/\theta-1/\pi)\,dt = 0$: the Ahlfors integral $(\ast)$ converges trivially for *every* choice of $h_k$. Yet if $h_k\to h>0$ the domain is asymptotically a strip of width $\pi-h$ in the extremal-length sense and the angular derivative fails to exist. The width average sees nothing; the capacity of the slits sees everything. This is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*