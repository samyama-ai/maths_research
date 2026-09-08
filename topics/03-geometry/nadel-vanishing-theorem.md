---
id: 03-geometry/nadel-vanishing-theorem
title: "Nadel Vanishing Theorem"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nadel Vanishing Theorem

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/nadel-vanishing-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Theorem (Nadel, 1989/1990).** Let $X$ be a complex projective algebraic manifold (more generally, a weakly pseudoconvex Kähler manifold) of dimension $n$, and let $(L,h)$ be a holomorphic line bundle equipped with a *singular* Hermitian metric $h = e^{-2\varphi}h_0$ whose curvature current satisfies
$$i\Theta_h(L) \;=\; i\Theta_{h_0}(L) + 2i\partial\bar\partial\varphi \;\ge\; \varepsilon\,\omega \qquad \text{for some } \varepsilon > 0$$
in the sense of currents, where $\omega$ is a Kähler form. Then
$$H^q\!\left(X,\; \mathcal{O}_X(K_X \otimes L) \otimes \mathcal{I}(h)\right) \;=\; 0 \qquad \text{for all } q \ge 1,$$
where $\mathcal{I}(h)$ is the multiplier ideal sheaf of $h$.

The theorem itself is settled. What remains open is the **positivity threshold**: the strict-positivity hypothesis $i\Theta_h(L) \ge \varepsilon\omega$ cannot simply be relaxed to $i\Theta_h(L)\ge 0$, and the correct statement in the semipositive / pseudoeffective / transcendental regime is only partially known. The live problem is:

> **(Nadel-type vanishing in the degenerate range.)** For $L$ pseudoeffective on a compact Kähler $X^n$ with singular metric $h$, $i\Theta_h(L)\ge 0$, does
> $$H^q\!\left(X, K_X\otimes L\otimes \mathcal{I}(h)\right)=0 \quad\text{for } q > n - \operatorname{nd}(L,h)\,?$$

A resolution means either a proof for arbitrary singular $h$ on arbitrary compact Kähler $X$, or a counterexample manifold/bundle pair.

## 2. Mathematical Foundations

**Singular Hermitian metric.** On $L\to X$, a singular metric is locally $h = e^{-2\varphi}$ with $\varphi \in L^1_{\mathrm{loc}}$. Its curvature $i\Theta_h(L)$ is a closed real $(1,1)$-current; $h$ is *positively curved* if $\varphi$ is plurisubharmonic modulo the smooth local weight.

**Multiplier ideal sheaf.** For $\varphi$ psh,
$$\mathcal{I}(\varphi)_x \;=\; \Big\{\, f \in \mathcal{O}_{X,x} \;:\; |f|^2 e^{-2\varphi} \in L^1_{\mathrm{loc}} \text{ near } x \,\Big\}.$$
Nadel proved $\mathcal{I}(\varphi)$ is **coherent**, via the Hörmander–Bombieri–Skoda $L^2$ extension of local sections. Coherence is what turns an analytic integrability condition into an algebraic-geometric object.

**Analytic singularities.** $\varphi$ has analytic singularities of coefficient $c>0$ if locally
$$\varphi = \tfrac{c}{2}\log\big(|g_1|^2+\cdots+|g_N|^2\big) + O(1),\qquad g_j \in \mathcal{O}(U).$$
Then $\mathcal{I}(\varphi)$ is computed by a log resolution: if $\mu^*\mathfrak{a} = \mathcal{O}(-F)$ with exceptional data $K_{X'/X}$, then $\mathcal{I}(c\cdot\mathfrak{a}) = \mu_*\mathcal{O}_{X'}(K_{X'/X} - \lfloor cF\rfloor)$ — the algebraic multiplier ideal of Lazarsfeld.

**Numerical dimension.** For $\alpha \in H^{1,1}(X,\mathbb{R})$ nef, $\operatorname{nd}(\alpha)=\max\{k: \alpha^k\neq 0 \text{ in } H^{2k}\}$. For a pseudoeffective class with singular metric $h$, Cao's definition is
$$\operatorname{nd}(L,h) \;=\; \max\Big\{ k : \limsup_{\varepsilon\to 0}\int_{X\setminus Z_\varepsilon}\big(i\Theta_{h_\varepsilon}(L)+\varepsilon\omega\big)^k \wedge \omega^{n-k} > 0 \Big\},$$
taken along a Demailly regularization $h_\varepsilon$.

**Specializations.** Taking $h$ smooth gives $\mathcal{I}(h)=\mathcal{O}_X$ and Nadel $\Rightarrow$ **Kodaira vanishing**. Taking $h$ with analytic singularities along a $\mathbb{Q}$-divisor gives **Kawamata–Viehweg vanishing**: for $L$ nef and big, $H^q(X,K_X\otimes L)=0$, $q\ge1$.

**Proof mechanism.** Hörmander's $L^2$ estimate: for $\Omega$ weakly pseudoconvex, $v$ a $(n,q)$-form with $\bar\partial v = 0$ and $\int \langle A_{q}^{-1}v,v\rangle e^{-2\varphi} < \infty$ where $A_q$ is the curvature operator on $\Lambda^{n,q}T^*_X\otimes L$, there is $u$ with $\bar\partial u = v$ and $\int|u|^2e^{-2\varphi} \le \int\langle A_q^{-1}v,v\rangle e^{-2\varphi}$. Strict positivity $\ge\varepsilon\omega$ makes $A_q \ge q\varepsilon$ for $q\ge1$, so $A_q^{-1}$ is bounded; the resulting sheaf of $L^2$ forms is a fine resolution of $K_X\otimes L\otimes\mathcal{I}(h)$.

## 3. History & State of the Art (SOTA)

- **1965–1966.** Hörmander and Andreotti–Vesentini establish $L^2$ existence theorems for $\bar\partial$ with plurisubharmonic weights — the analytic engine.
- **1975.** Bombieri, and Skoda, use $L^2$ methods with weights $\log|g|$ for algebraic-number-theoretic and division problems; the integrability condition later named "multiplier" appears.
- **1989.** A. Nadel announces the vanishing theorem and coherence of $\mathcal{I}(h)$ in *PNAS* 86, applying it to existence of Kähler–Einstein metrics of positive scalar curvature.
- **1990.** Full paper in *Annals of Mathematics* 132, 549–596.
- **1993.** Demailly's $L^2$ regularization theorem: any closed $(1,1)$-current with $\ge \gamma$ bound can be approximated by currents with analytic singularities, with controlled Lelong numbers. This makes Nadel usable in birational geometry.
- **1994–2004.** Demailly–Ein–Lazarsfeld subadditivity $\mathcal{I}(\varphi+\psi)\subseteq\mathcal{I}(\varphi)\mathcal{I}(\psi)$; Lazarsfeld's *Positivity II* codifies the algebraic side; Siu's invariance of plurigenera and effective Matsusaka use Nadel as the key vanishing input.
- **2012–2015.** Fujino's injectivity/torsion-free package and Matsumura's Nadel-type theorems push into the semipositive regime. Cao (2014) proves the numerical-dimension version on compact Kähler manifolds.
- **2015.** Guan–Zhou prove Demailly's **strong openness conjecture**: $\mathcal{I}(\varphi)=\bigcup_{p>1}\mathcal{I}(p\varphi)$ (*Annals* 182). This removes a long-standing gap in arguments that approximate $\mathcal{I}(h)$ from inside.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $i\Theta_h(L)\ge\varepsilon\omega$, $X$ projective or weakly pseudoconvex Kähler, any $n$ | Full vanishing $q\ge1$ | Nadel 1990 |
| $h$ smooth, $L$ ample | Kodaira vanishing | Kodaira 1953 |
| $L$ nef and big, $\mathcal{I}$ from analytic singularities | Kawamata–Viehweg | Kawamata 1982, Viehweg 1982 |
| $X$ compact Kähler, $h$ with **analytic singularities**, $L$ psef | $H^q(X,K_X\otimes L\otimes\mathcal{I}(h))=0$ for $q>n-\operatorname{nd}(L,h)$ | Cao 2014 |
| $L$ **big**, $h_{\min}$ a metric with minimal singularities | $H^q(X,K_X\otimes L\otimes\mathcal{I}(h_{\min}))=0$ for $q>n-\operatorname{nd}(L)$ | Matsumura 2015 |
| $i\Theta_h(L)\ge0$ and $L$ semipositive-in-the-large; injectivity route | Nadel-type vanishing with $\mathcal{I}$ replaced by $\mathcal{I}(h^{1-\delta})$-type sheaves | Matsumura 2014 |
| $\dim X = 1$ | Trivial: $q\ge1$ forces $q=1$, $\deg(K+L)>2g-2$ | classical |
| $\dim X = 2$, $L$ nef with $L^2>0$ | Complete via Kawamata–Viehweg plus Zariski decomposition | Sakai, Miyaoka |
| char $p>0$ | **Fails**: Raynaud's counterexamples to Kodaira vanishing on surfaces fibered in genus-2 curves | Raynaud 1978 |

## 5. Principal Obstacles

- **Loss of coercivity in the $L^2$ estimate.** When $i\Theta_h(L)\ge0$ only, the curvature operator $A_q$ has kernel; $A_q^{-1}$ is unbounded and Hörmander's inequality gives no solution to $\bar\partial u=v$ with finite norm. Adding $\varepsilon\omega$ restores coercivity but changes the ideal sheaf: $\mathcal{I}(h_\varepsilon)$ need not converge to $\mathcal{I}(h)$ in a controlled way.
- **Regularization changes the ideal.** Demailly regularization $h_\varepsilon\downarrow h$ produces $\mathcal{I}(h_\varepsilon)\supseteq\mathcal{I}(h)$ with Lelong-number loss $O(\varepsilon)$. Passing to the limit in cohomology needs a Mittag-Leffler / stabilization argument that fails for general psh weights whose singularities are not analytic.
- **No algebraic model in the transcendental case.** On a non-projective compact Kähler $X$, a psef class need not contain a current with analytic singularities of prescribed type; log resolutions and Hodge-theoretic (Kollár, Esnault–Viehweg) proofs are unavailable.
- **Numerical dimension is not semicontinuous.** $\operatorname{nd}(L,h)$ can jump under approximation, so the conjectural bound $q>n-\operatorname{nd}(L,h)$ is not stable along the very approximations used to prove it.
- **Characteristic $p$ obstruction.** Raynaud's examples show no purely formal/cohomological derivation exists; any proof must use the archimedean $L^2$ theory or Hodge theory over $\mathbb{C}$.

## 6. The Gap

Proved: strict positivity ($\varepsilon\omega$) in full generality; degenerate positivity **when the singularities are analytic** (Cao) or the metric is a minimal-singularity metric on a **big** bundle (Matsumura). Conjectured: the same numerical-dimension bound for an **arbitrary** positively curved singular metric on an **arbitrary** psef line bundle over a compact Kähler manifold.

The precise missing step: given psef $(L,h)$ with $i\Theta_h(L)\ge0$ and a regularizing family $h_\varepsilon$ with $i\Theta_{h_\varepsilon}(L)\ge-\varepsilon\omega$, show that the natural maps
$$H^q\big(X,K_X\otimes L\otimes\mathcal{I}(h_\varepsilon)\big)\longrightarrow H^q\big(X,K_X\otimes L\otimes\mathcal{I}(h_{\varepsilon'})\big),\qquad \varepsilon'<\varepsilon,$$
stabilize to zero for $q>n-\operatorname{nd}(L,h)$, with an $\varepsilon$-uniform $L^2$ estimate. Strong openness (Guan–Zhou) supplies sheaf-level stabilization $\mathcal{I}(p\varphi)\to\mathcal{I}(\varphi)$ but not the uniform cohomological bound.

## 7. Current Research (as of June 2026)

- **Transcendental Kähler birational geometry.** The Demailly school (Grenoble/IMJ) and the Cao–Höring program on structure of psef canonical bundles continue to demand degenerate Nadel vanishing as an input; progress on the transcendental Morse inequality conjecture is the recognized gateway. *(frontier — verify)*
- **Injectivity-theorem route.** Fujino (Kyoto/Osaka) and Matsumura (Tohoku) develop injectivity, torsion-freeness and vanishing as a single package for $\mathbb{R}$-line bundles with singular metrics; the aim is to replace strict positivity with semipositivity plus a nowhere-degeneracy assumption on a Zariski-open set.
- **Guan–Zhou circle.** Effective and optimal versions of strong openness, $L^2$ extension with optimal constants, and jumping-number theory (Guan, Zhou, Xu, and collaborators) are being fed back into vanishing statements. *(frontier — verify)*
- **Singular ambient spaces.** Nadel vanishing for klt pairs and for $\mathcal{I}$ on normal varieties with $\mathbb{Q}$-Gorenstein singularities, via Grauert–Riemenschneider-type arguments.
- **Positive characteristic surrogates.** Test ideals $\tau(\mathfrak{a}^c)$ and Frobenius-split methods (Schwede, Smith, Takagi) recover fragments of Nadel vanishing for globally $F$-regular varieties.

## 8. Future Work

1. Prove the transcendental holomorphic Morse inequality: $\int_{X(\le1,\alpha)}\alpha^n>0 \Rightarrow \alpha$ big for nef $(1,1)$-classes. This would give a Kähler Kawamata–Viehweg theorem and, plausibly, the degenerate Nadel statement.
2. Establish uniform $L^2$ estimates along Demailly regularizations with control by $\operatorname{nd}(L,h)$ rather than by strict positivity.
3. Remove the analytic-singularity hypothesis in Cao's theorem using strong openness plus a Zariski-type decomposition of currents.
4. Determine whether $\mathcal{I}(h_{\min})$ for a psef (not big) $L$ can be computed by a finite algebraic model; equivalently, whether jumping numbers of $h_{\min}$ are rational.
5. Build a counterexample search: a compact Kähler $X$ with psef $L$ and $H^n(X,K_X\otimes L\otimes\mathcal{I}(h))\ne0$ despite $\operatorname{nd}(L,h)\ge1$.

## 9. Key References

- **[Foundational]** A. M. Nadel. *Multiplier ideal sheaves and Kähler–Einstein metrics of positive scalar curvature.* Annals of Mathematics **132** (1990), 549–596. (Announcement: Proc. Nat. Acad. Sci. USA **86** (1989), 7299–7300.). [DOI](https://doi.org/10.1073/pnas.86.19.7299)
- **[Foundational]** L. Hörmander. *$L^2$ estimates and existence theorems for the $\bar\partial$ operator.* Acta Mathematica **113** (1965), 89–152.
- **[Foundational]** J.-P. Demailly. *Regularization of closed positive currents and intersection theory.* Journal of Algebraic Geometry **1** (1992), 361–409.
- **[Book]** J.-P. Demailly. *Analytic Methods in Algebraic Geometry.* Surveys of Modern Mathematics **1**, Higher Education Press / International Press, 2012.
- **[Book]** R. Lazarsfeld. *Positivity in Algebraic Geometry II: Positivity for Vector Bundles, and Multiplier Ideals.* Ergebnisse der Mathematik **49**, Springer, 2004.
- **[SOTA]** Q. Guan, X. Zhou. *A proof of Demailly's strong openness conjecture.* Annals of Mathematics **182** (2015), 605–616. [DOI](https://doi.org/10.4007/annals.2015.182.2.5)
- **[SOTA]** J. Cao. *Numerical dimension and a Kawamata–Viehweg–Nadel-type vanishing theorem on compact Kähler manifolds.* Compositio Mathematica **150** (2014), 1869–1902. [DOI](https://doi.org/10.1112/s0010437x14007398)
- **[SOTA]** S. Matsumura. *A Nadel vanishing theorem via injectivity theorems.* Mathematische Annalen **359** (2014), 785–802. [DOI](https://doi.org/10.1007/s00208-014-1018-6)
- **[SOTA]** S. Matsumura. *A Nadel vanishing theorem for metrics with minimal singularities on big line bundles.* Advances in Mathematics **280** (2015), 188–207. [DOI](https://doi.org/10.1016/j.aim.2015.03.019)
- **[Context]** J.-P. Demailly, T. Peternell, M. Schneider. *Pseudo-effective line bundles on compact Kähler manifolds.* International Journal of Mathematics **12** (2001), 689–741. [DOI](https://doi.org/10.1142/s0129167x01000861)
- **[Counterexample]** M. Raynaud. *Contre-exemple au "vanishing theorem" en caractéristique $p>0$.* In *C. P. Ramanujam — A Tribute*, Tata Institute Studies in Mathematics **8**, Springer, 1978, 273–278.
- **[Survey]** O. Fujino. *Injectivity theorems.* In *Higher Dimensional Algebraic Geometry*, Advanced Studies in Pure Mathematics **74**, Mathematical Society of Japan, 2017, 131–157.

## 10. Worked Example / Concrete Special Case

**Claim to derive.** On $X=\mathbb{P}^2$, degree-$m$ forms surject onto the $m$-jets at a point: $H^0(\mathbb{P}^2,\mathcal{O}(m))\to\mathcal{O}/\mathfrak{m}_p^{m+1}$ is onto. We get this from Nadel.

Fix $p\in\mathbb{P}^2$ with homogeneous coordinates $[x_0:x_1:x_2]$, $p=[0:0:1]$, and let $\ell_0=x_0$, $\ell_1=x_1$ be the linear forms vanishing at $p$. Set
$$\psi(x)\;=\;\log\frac{|\ell_0(x)|^2+|\ell_1(x)|^2}{\|x\|^2},$$
a global quasi-psh function on $\mathbb{P}^2$ with $i\partial\bar\partial\psi \ge -\,\omega_{FS}$ (the numerator's $\log$ is the pullback of a Fubini–Study potential under the projection $\mathbb{P}^2\dashrightarrow\mathbb{P}^1$, hence psh-positive; the denominator contributes exactly $-\omega_{FS}$).

Take $L=\mathcal{O}(d)$ with $h=h_{FS}^{\otimes d}\,e^{-\gamma\psi}$, $\gamma>0$. Then
$$i\Theta_h(L)\;=\;d\,\omega_{FS}+\gamma\, i\partial\bar\partial\psi\;\ge\;(d-\gamma)\,\omega_{FS},$$
which is $\ge\varepsilon\omega_{FS}$ exactly when $\gamma<d$.

**Compute the multiplier ideal.** Near $p$ in affine coordinates $z=(z_1,z_2)$, $\tfrac{\gamma}{2}\psi = \tfrac{\gamma}{2}\log|z|^2+O(1)$, so the weight is $|z|^{-2\gamma}$. For $f\in\mathcal{O}_{\mathbb{C}^2,0}$ vanishing to order $k$,
$$\int_{|z|<1}\frac{|f|^2}{|z|^{2\gamma}}\,d\lambda \;\asymp\; \int_0^1 r^{2k-2\gamma}\,r^{3}dr <\infty \iff 2k-2\gamma+3>-1 \iff k>\gamma-2 .$$
So $\mathcal{I}(h)=\mathfrak{m}_p^{k}$ with $k=\lceil\gamma\rceil-2$ for $\gamma\notin\mathbb{Z}$, and $\mathcal{I}(h)=\mathcal{O}$ away from $p$.

**Apply Nadel.** Choose $\gamma=k+2-\epsilon$ with $0<\epsilon\ll1$. Positivity needs $\gamma<d$, i.e. $k\le d-2$. With $K_{\mathbb{P}^2}=\mathcal{O}(-3)$,
$$H^q\big(\mathbb{P}^2,\ \mathcal{O}(d-3)\otimes\mathfrak{m}_p^{k}\big)=0,\qquad q\ge1,\quad k\le d-2 .$$

**Read off the conclusion.** Put $m=d-3$ and take the maximal $k=d-2=m+1$. The ideal sequence
$$0\to\mathcal{O}(m)\otimes\mathfrak{m}_p^{m+1}\to\mathcal{O}(m)\to\mathcal{O}/\mathfrak{m}_p^{m+1}\to0$$
has $H^1$ of the left term $=0$, so $H^0(\mathbb{P}^2,\mathcal{O}(m))\twoheadrightarrow\mathcal{O}/\mathfrak{m}_p^{m+1}$. Both sides have dimension $\binom{m+2}{2}$, so the map is an isomorphism — the bound $k\le d-2$ is sharp, and pushing to $k=m+2$ would force a surjection onto a strictly larger space, which is false. This shows the strict-positivity hypothesis in Section 1 is not an artifact: it is saturated by this example at $\gamma\uparrow d$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*