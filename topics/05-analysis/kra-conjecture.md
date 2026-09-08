---
id: 05-analysis/kra-conjecture
title: "Kra Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kra Conjecture (Kra's Theta Conjecture on the Poincaré Series Operator)

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/kra-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\Gamma$ be a Fuchsian group acting on the upper half-plane $H$ (equivalently the unit disc $\Delta$). The **Poincaré theta series operator** sends an integrable holomorphic quadratic differential on $H$ to a $\Gamma$-automorphic one:

$$(\Theta_\Gamma \varphi)(z) \;=\; \sum_{\gamma \in \Gamma} \varphi(\gamma z)\,\gamma'(z)^2 .$$

It is a surjection $A_1(H) \to A_1(H,\Gamma)$ of norm $\|\Theta_\Gamma\| \le 1$.

**Kra's theta conjecture.** $\|\Theta_\Gamma\| < 1$ **if and only if** $\Gamma$ is finitely generated and of the first kind (i.e. $H/\Gamma$ has finite hyperbolic area). Equivalently, in the form that carries the open content:

$$\Gamma \text{ infinitely generated} \;\Longrightarrow\; \|\Theta_\Gamma\| = 1 .$$

A complete proof must produce, for every infinitely generated Fuchsian group $\Gamma$ and every $\varepsilon>0$, some $\varphi \in A_1(H)$ with $\|\Theta_\Gamma\varphi\| > (1-\varepsilon)\|\varphi\|$. A disproof must exhibit one infinitely generated $\Gamma$ with $\|\Theta_\Gamma\| \le c < 1$. The "only if" half is settled (Sections 3–4); the implication above is not.

## 2. Mathematical Foundations

**Spaces.** For a domain $D \subseteq \widehat{\mathbb{C}}$, $A_1(D)$ is the Bergman space of holomorphic quadratic differentials $\varphi(z)\,dz^2$ with

$$\|\varphi\|_{A_1(D)} \;=\; \iint_D |\varphi(z)|\,dx\,dy \;<\; \infty ,$$

and $B_\infty(D)$ the Banach space with the hyperbolic sup-norm $\|\psi\|_\infty = \sup_D \rho_D(z)^{-2}|\psi(z)|$, where $\rho_D$ is the hyperbolic density ($\rho_H(z) = 1/\operatorname{Im} z$). A **weight $-4$ automorphic form** for $\Gamma$ satisfies $\varphi(\gamma z)\gamma'(z)^2 = \varphi(z)$ for all $\gamma \in \Gamma$; $A_1(H,\Gamma)$ and $B_\infty(H,\Gamma)$ denote the corresponding invariant subspaces, with $\|\varphi\|_{A_1(H,\Gamma)} = \iint_F |\varphi|$ over any fundamental domain $F$.

**Convergence and the bound $\|\Theta\|\le 1$.** For any Fuchsian group the exponent of convergence satisfies $\delta(\Gamma) \le 1 < 2$, so $\sum_{\gamma}|\gamma'(z)|^2$ converges locally uniformly on $H$. Unfolding gives

$$\|\Theta_\Gamma\varphi\|_{A_1(H,\Gamma)} = \iint_F \Big|\sum_\gamma \varphi(\gamma z)\gamma'(z)^2\Big| \;\le\; \sum_\gamma \iint_{\gamma F} |\varphi| \;=\; \|\varphi\|_{A_1(H)} . \tag{2.1}$$

Equality in (2.1) forces the orbit terms to share a common argument a.e.; the conjecture is exactly the question of how much phase cancellation the group geometry forces.

**Duality.** $A_1(H)^\ast \cong B_\infty(H)$ under $\langle\varphi,\psi\rangle = \iint_H \varphi\,\overline{\psi}\,\rho_H^{-2}$, and $\Theta_\Gamma^\ast$ is the inclusion $B_\infty(H,\Gamma)\hookrightarrow B_\infty(H)$. Thus $\|\Theta_\Gamma\|<1$ is a statement that the $A_1(\Gamma)$-dual norm on invariant forms is *strictly* dominated by the ambient dual norm — a Bers-type strict inequality.

**Extreme points.** In $\Delta$, with $T_w(z)=(z-w)/(1-\bar w z)$,

$$k_w(z) \;=\; \big(T_w'(z)\big)^2 \;=\; \frac{(1-|w|^2)^2}{(1-\bar w z)^4}, \qquad \|k_w\|_{A_1(\Delta)} = \pi \ \ \text{for every } w\in\Delta ,$$

using $\iint_\Delta |1-\bar wz|^{-4}dA = \pi(1-|w|^2)^{-2}$. These Möbius-normalized kernels are the standard test functions: their mass concentrates at $\zeta \in \partial\Delta$ as $w \to \zeta$, and **no** $A_1$ function can concentrate at an interior point (interior sup-norm bounds are controlled by the $L^1$ norm).

**Monotonicity.** If $\Gamma' \le \Gamma$, then $\Theta_\Gamma = \Theta_{\Gamma'\backslash\Gamma}\circ\Theta_{\Gamma'}$ with both factors of norm $\le 1$, so

$$\|\Theta_\Gamma\| \;\le\; \|\Theta_{\Gamma'}\| . \tag{2.2}$$

The conjecture is therefore consistent only if infinite-index (hence infinitely generated) subgroups of finite-area groups have norm exactly $1$.

## 3. History & State of the Art (SOTA)

The theta operator goes back to Poincaré; its Banach-space theory was built by Ahlfors and Bers in the 1960s (surjectivity of $\Theta$ onto $A_1(\Gamma)$, the Bers area inequalities). Bers' 1965 paper treated Poincaré series for *infinitely* generated Fuchsian groups, where the pathologies first appeared: series that vanish identically, non-closed images under related maps, failure of finite-dimensionality.

Irwin Kra systematized the subject in *Automorphic Forms and Kleinian Groups* (1972) and, in a long line of papers culminating in the Acta Mathematica memoir of 1984, studied vanishing and spanning phenomena for Poincaré series. The norm question $\|\Theta_\Gamma\| \overset{?}{<} 1$ — the **theta conjecture** — crystallized from that program: the norm should detect the dichotomy "finite-area quotient vs. everything else."

Milestones:

- **1964–67 (Ahlfors, Bers):** $\Theta$ bounded, surjective, $\|\Theta\|\le 1$; area/dimension inequalities for finitely generated groups.
- **1969 (Earle):** structural remarks on Poincaré series, kernel description, behavior under subgroup inclusion.
- **1977 (Niebur–Sheingorn):** characterization of Fuchsian groups for which $A_1(\Gamma)\subseteq B_\infty(\Gamma)$ — the first result showing that fine boundary geometry (not just generation) governs integrable forms.
- **1982 (Ohtake):** $\|\Theta_\Gamma\|<1$ for finitely generated Fuchsian groups of the first kind. *(This is the affirmative half.)*
- **Elementary (folklore):** $\|\Theta_\Gamma\|=1$ for every group of the second kind, by concentration on an arc of discontinuity (Section 10).
- **1984 (Kra, Acta):** identically vanishing Poincaré series for infinitely generated and for infinite-index normal subgroups — evidence that $\Theta$ behaves qualitatively differently there.

No exact value of $\|\Theta_\Gamma\|$ is known for a single group with $\|\Theta_\Gamma\|<1$; even for $\mathrm{PSL}(2,\mathbb{Z})$ only $\|\Theta\|<1$ is known, with no explicit numerical constant in the literature.

## 4. Partial Results / Verified Cases

1. **All groups of the second kind** (limit set $\ne \partial H$), finitely or infinitely generated, elementary or not: $\|\Theta_\Gamma\|=1$. Proved by concentrating $k_w$ at a point of the discontinuity arc inside a fundamental domain (Section 10 gives the full estimate).
2. **Finitely generated, first kind** — signatures $(g;n_1,\dots,n_k;m)$ with $2g-2+\sum(1-1/n_i)+m>0$ and finite area, including all cocompact groups and all finite-index subgroups of $\mathrm{PSL}(2,\mathbb{Z})$: $\|\Theta_\Gamma\|<1$ (Ohtake, 1982). Hence the "only if" direction of the conjecture is complete.
3. **Trivial and elementary cases:** $\Gamma=\{1\}$ gives $\|\Theta\|=1$; cyclic parabolic and cyclic hyperbolic groups (quotient a punctured disc or annulus) are of the second kind, so $\|\Theta\|=1$ — consistent with the conjecture.
4. **Monotonicity consequences:** by (2.2), if $\Gamma'\le\Gamma$ and $\|\Theta_{\Gamma'}\|=1$ is unknown while $\|\Theta_\Gamma\|=1$ is known, nothing follows; but any single infinitely generated counterexample $\Gamma'$ with $\|\Theta_{\Gamma'}\|<1$ would force $\|\Theta_\Gamma\|<1$ for every overgroup — a strong rigidity constraint.
5. **Open in general:** infinitely generated groups of the **first** kind — e.g. infinite-index normal subgroups $\Gamma' \triangleleft \mathrm{PSL}(2,\mathbb{Z})$ with $\Gamma/\Gamma'\cong\mathbb{Z}$, and Riemann surfaces of infinite genus with limit set the whole circle. Verified sub-classes have been announced for divergence-type groups and for groups admitting a "thick" invariant sequence of collars *(frontier — verify)*.

## 5. Principal Obstacles

- **$L^1$, not $L^2$.** $A_1$ is non-reflexive, non-uniformly-convex, and has no inner product. Orthogonality, spectral decomposition and the Selberg-style harmonic analysis available for $L^2$ automorphic forms are all unavailable; the norm is an $L^1$ extremal problem over the phases $\arg(\varphi\circ\gamma\cdot(\gamma')^2)$.
- **The norm is a supremum, not a maximum.** For groups with $\|\Theta\|<1$ no extremal $\varphi$ is known to exist, so variational arguments (Euler–Lagrange, uniqueness of extremals) cannot be closed.
- **Concentration lives only at the boundary.** Since $A_1$ functions cannot concentrate in the interior, the entire question is a boundary phenomenon; one must control the orbit $\{\gamma\}$ near limit points where the group geometry is least uniform.
- **Infinitely generated first-kind groups are geometrically wild.** The injectivity radius of $H/\Gamma$ may tend to $0$ along infinitely many ends, the convex core can be infinite-area, and the limit set can have Hausdorff dimension anywhere in $(0,1]$. Neither $\delta(\Gamma)$ nor convergence/divergence type is known to control phase cancellation in (2.1).
- **No compactness.** Finitely generated groups admit compact-core arguments (Ohtake's proof uses finiteness of the quotient area); an infinitely generated group has no compact core, so limits of test functions escape.
- **Degenerate behavior of $\Theta$.** Kra's vanishing theorems show $\ker\Theta$ is huge and $\Theta\varphi \equiv 0$ can occur for nonzero $\varphi$; the operator has no injective restriction whose norm is easier to compute.

## 6. The Gap

Proved: $\Gamma$ second kind $\Rightarrow \|\Theta\|=1$; $\Gamma$ finitely generated first kind $\Rightarrow \|\Theta\|<1$. Conjectured but unproved: $\Gamma$ infinitely generated of the **first** kind $\Rightarrow \|\Theta\|=1$.

The exact step to cross: given such $\Gamma$ and $\varepsilon>0$, construct $\varphi\in A_1(H)$ whose mass concentrates near a limit point $\zeta$ in such a way that **at most $\varepsilon$-fraction of its total mass is carried by non-identity orbit translates over a fundamental domain**. In the second-kind case this is free (concentrate on an interval of discontinuity). For an infinitely generated first-kind group, every boundary neighbourhood meets infinitely many translates of $F$, so one must instead exploit the *unbounded geometry* — an infinite sequence of collars of growing modulus, or an escaping end — to build a quasi-fundamental "almost-free" region. Whether such a region exists for **every** infinitely generated first-kind group is precisely the gap.

## 7. Current Research (as of June 2026)

- **Infinite-type Riemann surface analysis** (Waseda/Japanese Teichmüller school, K. Matsuzaki and collaborators): quantitative links between the theta norm, the Nielsen convex core geometry, and the bounded/uniformly-thick hypotheses on the quotient surface. Announced criteria give $\|\Theta_\Gamma\|=1$ whenever $H/\Gamma$ has arbitrarily short essential curves escaping to infinity *(frontier — verify)*.
- **CUNY / Teichmüller theory of infinite-dimensional spaces** (in the lineage of Gardiner–Lakic): reformulations of $\|\Theta\|<1$ as a strict-contraction property of the projection $B_\infty(H)\to B_\infty(H,\Gamma)$, and its consequences for uniqueness of extremal quasiconformal maps.
- **Ergodic-theoretic angle:** attempts to relate $\|\Theta_\Gamma\|$ to divergence type via the Hopf–Tsuji–Sullivan dichotomy — divergence type (conservative, ergodic boundary action) is expected to force strong cancellation but is *not* equivalent to finite generation, so it cannot alone characterize $\|\Theta\|<1$ *(frontier — verify)*.
- **Numerics:** no rigorous numerical value of $\|\Theta_\Gamma\|$ for a first-kind finitely generated group has been published; obtaining a certified bound (say for the modular group) is an accessible open computational target.

## 8. Future Work

1. **Prove a geometric criterion.** Show that an infinite sequence of disjoint collars with moduli $\to\infty$, or an end of the quotient with injectivity radius $\to 0$, yields test functions with $\|\Theta\varphi\|/\|\varphi\|\to1$; then verify every infinitely generated group has one such feature.
2. **Quantify Ohtake's theorem.** Produce $\|\Theta_\Gamma\| \le 1 - c(\text{area}, \text{injectivity radius})$ for finite-area groups. A bound degenerating exactly as the group degenerates to an infinitely generated one would prove the conjecture by exhaustion.
3. **Normal-subgroup test case.** Settle $\|\Theta_{\Gamma'}\|=1$ for $\Gamma' \triangleleft \mathrm{PSL}(2,\mathbb{Z})$ with $\Gamma/\Gamma'\cong \mathbb{Z}$ (the "$\mathbb{Z}$-cover" of the modular surface) — the cleanest infinitely generated first-kind example, where relative Poincaré series over $\mathbb{Z}$ make the cancellation explicit.
4. **Duality attack.** Use $\Theta^\ast$ = inclusion of $B_\infty(\Gamma)$ to convert the problem into a comparison of the sup-norm and the $A_1(\Gamma)$-dual norm on invariant Bloch-type differentials, where boundary-value techniques for Bloch functions may apply.
5. **Exact values.** Compute $\|\Theta\|$ for a single cocompact group; even a certified interval would test whether the norm is a genuine geometric invariant.

## 9. Key References

- **[Foundational]** L. V. Ahlfors. *Finitely generated Kleinian groups.* American Journal of Mathematics 86 (1964), 413–429. [DOI](https://doi.org/10.2307/2373173)
- **[Foundational]** L. Bers. *Automorphic forms and Poincaré series for infinitely generated Fuchsian groups.* American Journal of Mathematics 87 (1965), 196–214. [DOI](https://doi.org/10.2307/2373231)
- **[Foundational]** L. Bers. *Inequalities for finitely generated Kleinian groups.* Journal d'Analyse Mathématique 18 (1967), 23–41. [DOI](https://doi.org/10.1007/bf02798032)
- **[Foundational]** I. Kra. *Automorphic Forms and Kleinian Groups.* W. A. Benjamin, Reading MA, 1972.
- **[Structural]** C. J. Earle. *Some remarks on Poincaré series.* Compositio Mathematica 21 (1969), 167–176.
- **[SOTA]** H. Ohtake. *On the norm of the Poincaré series operator for a finitely generated Fuchsian group.* Journal of Mathematics of Kyoto University 22 (1982), 725–732.
- **[SOTA]** I. Kra. *On the vanishing of and spanning sets for Poincaré series for cusp forms.* Acta Mathematica 153 (1984), 47–116. [DOI](https://doi.org/10.1007/bf02392375)
- **[Related]** D. Niebur and M. Sheingorn. *Characterization of Fuchsian groups whose integrable forms are bounded.* Annals of Mathematics (2) 106 (1977), 239–258. [DOI](https://doi.org/10.2307/1971094)
- **[Survey / Book]** F. P. Gardiner and N. Lakic. *Quasiconformal Teichmüller Theory.* Mathematical Surveys and Monographs 76, American Mathematical Society, 2000.
- **[Survey / Book]** P. J. Nicholls. *The Ergodic Theory of Discrete Groups.* LMS Lecture Note Series 143, Cambridge University Press, 1989.
- **[Background]** A. F. Beardon. *The Geometry of Discrete Groups.* Graduate Texts in Mathematics 91, Springer, 1983.

## 10. Worked Example / Concrete Special Case

**Claim.** For the cyclic hyperbolic group $\Gamma = \langle \gamma_0 \rangle$, $\gamma_0(z)=4z$, acting on $H$ (quotient: an annulus; limit set $\{0,\infty\}$, so $\Gamma$ is of the second kind), $\|\Theta_\Gamma\|=1$.

**Test functions.** For $\epsilon>0$ set

$$\varphi_\epsilon(z) \;=\; \frac{\epsilon^{2}}{(z-2+i\epsilon)^{4}},$$

holomorphic on $H$ (pole at $2-i\epsilon \notin H$). Using $\iint_H |z+i|^{-4}\,dA = \int_0^\infty\!\!\int_{\mathbb R}\frac{dx\,dy}{(x^2+(y+1)^2)^2} = \int_0^\infty \frac{\pi}{2(1+y)^3}dy = \frac{\pi}{4}$ and the scaling $z\mapsto \epsilon z$,

$$\|\varphi_\epsilon\|_{A_1(H)} \;=\; \epsilon^{2}\cdot \frac{1}{\epsilon^{2}}\cdot\frac{\pi}{4} \;=\; \frac{\pi}{4}\qquad\text{for every }\epsilon>0 .$$

**Mass concentration.** Fix $r=1/2$ and let $U=D(2,r)\cap H$. For $z\notin U$ and $\epsilon<r/2$ we have $|z-2+i\epsilon|\ge |z-2|-\epsilon \ge \tfrac12|z-2|$, so

$$\iint_{H\setminus U}|\varphi_\epsilon| \;\le\; 16\,\epsilon^{2}\iint_{|u|>r}\frac{dA(u)}{|u|^{4}} \;=\; 16\,\epsilon^{2}\cdot 2\pi\!\int_r^\infty \frac{ds}{s^{3}} \;=\; \frac{16\pi\epsilon^{2}}{r^{2}} \;=\; 64\pi\epsilon^{2}.$$

**Fundamental domain.** $F=\{z\in H : 1\le |z| <4\}$ contains $U$ (since $1.5<|z|<2.5$ there).

**Lower bound.** Write $\gamma_n(z)=4^nz$, $\gamma_n'(z)^2=16^n$. By the triangle inequality and unfolding,

$$\|\Theta_\Gamma\varphi_\epsilon\| = \iint_F\Big|\sum_{n\in\mathbb Z}\varphi_\epsilon(4^nz)16^{n}\Big| \;\ge\; \iint_F|\varphi_\epsilon| \;-\; \sum_{n\ne0}\iint_{\gamma_nF}|\varphi_\epsilon| \;=\; 2\iint_F|\varphi_\epsilon| - \|\varphi_\epsilon\| .$$

Since $\iint_F |\varphi_\epsilon| \ge \|\varphi_\epsilon\| - 64\pi\epsilon^2$,

$$\frac{\|\Theta_\Gamma\varphi_\epsilon\|}{\|\varphi_\epsilon\|} \;\ge\; 1 - \frac{128\pi\epsilon^{2}}{\pi/4} \;=\; 1-512\,\epsilon^{2} \;\xrightarrow[\epsilon\to0]{}\; 1 .$$

With $\|\Theta\|\le1$ from (2.1), $\|\Theta_\Gamma\|=1$. Taking $\epsilon=10^{-2}$ already gives $\|\Theta_\Gamma\|\ge 0.948$.

**Why this fails for first-kind groups.** The argument needs a boundary point $\zeta=2$ lying in the *ordinary set*, so that a whole half-disc neighbourhood of $\zeta$ sits inside one fundamental domain. If $\Gamma$ is of the first kind, every boundary neighbourhood meets infinitely many translates of $F$, the "leakage" term $\sum_{n\ne0}\iint_{\gamma_nF}|\varphi|$ no longer vanishes, and the phases $\arg(\varphi\circ\gamma\cdot(\gamma')^2)$ must be tracked. Ohtake's theorem shows the resulting cancellation is uniform when $\operatorname{area}(H/\Gamma)<\infty$. The conjecture asserts that as soon as $\Gamma$ is infinitely generated, the quotient has ends thin or long enough to rebuild an *almost*-free region and push the ratio back to $1$ — this is exactly what remains unproved.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*