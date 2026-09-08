---
id: 05-analysis/bloch-conjecture
title: "Bloch Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bloch Conjecture (Ahlfors–Grunsky Conjecture on Bloch's Constant)

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/bloch-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathbb{D}=\{z\in\mathbb{C}:|z|<1\}$ and let $\mathcal{F}$ be the family of holomorphic $f:\mathbb{D}\to\mathbb{C}$ with $f'(0)=1$. For $f\in\mathcal{F}$ define $b(f)$ as the supremum of radii $r$ such that some subdomain $\Omega\subseteq\mathbb{D}$ is mapped by $f$ **conformally** (bijectively) onto an open disk of radius $r$ — a *schlicht disk* in the image. Bloch's constant is

$$B \;=\; \inf_{f\in\mathcal{F}} b(f).$$

Bloch's theorem (1925) states $B>0$. The **Bloch conjecture** (Ahlfors–Grunsky, 1937) asserts that the infimum is attained by their explicit branched-covering function and equals

$$B \;=\; \frac{\Gamma\!\left(\tfrac13\right)\Gamma\!\left(\tfrac{11}{12}\right)}{\left(1+\sqrt3\right)^{1/2}\,\Gamma\!\left(\tfrac14\right)} \;=\; 0.4718617\ldots$$

A complete solution requires either (i) a proof that every $f\in\mathcal{F}$ satisfies $b(f)\ge 0.47186\ldots$, matching the Ahlfors–Grunsky example and thus establishing extremality; or (ii) an $f\in\mathcal{F}$ with $b(f)<0.47186\ldots$, disproving it. Currently only $0.4333 < B \le 0.4719$ is known.

*Disambiguation:* this is distinct from the Bloch conjecture on zero-cycles of surfaces with $p_g=0$ in algebraic geometry, and from "Bloch's principle" in normal-families theory.

## 2. Mathematical Foundations

**Schlicht disks.** For $f$ holomorphic on $\mathbb{D}$ and $a\in\mathbb{D}$ with $f'(a)\ne 0$, let $\rho(a,f)$ be the supremum of $r>0$ such that the branch of $f^{-1}$ fixing $f(a)$ extends holomorphically and injectively to $D(f(a),r)$ with image in $\mathbb{D}$. Then

$$b(f)=\sup_{a\in\mathbb{D}}\rho(a,f),\qquad B=\inf\{\,b(f): f'(0)=1\,\}.$$

Dropping injectivity gives **Landau's constant** $L=\inf_{\mathcal F}\ell(f)$, where $\ell(f)$ is the largest radius of a disk contained in $f(\mathbb{D})$; restricting to locally univalent $f$ ($f'\ne0$ on $\mathbb{D}$) gives the **locally univalent Bloch constant** $B_1$. Trivially $B\le B_1\le L$.

**Normalization and invariance.** $b$ is invariant under $f\mapsto \alpha^{-1} f(\varphi(z))\varphi'(0)^{-1}$ for $\varphi\in\mathrm{Aut}(\mathbb{D})$ up to affine scaling, so the problem is a pure extremal problem on the hyperbolic disk. The natural quantity is the conformal density

$$\lambda_f(z)=\frac{|f'(z)|\,(1-|z|^2)}{2},$$

Bloch's semi-norm being $\|f\|_{\mathcal B}=\sup_z |f'(z)|(1-|z|^2)$.

**Ahlfors' metric method.** Ahlfors (1938) proved $B\ge \sqrt3/4$ by constructing on the domain $\Omega=f^{-1}(\text{lattice complement})$ an ultrahyperbolic conformal metric $\rho(w)|dw|$ with Gaussian curvature

$$K_\rho=-\frac{\Delta \log \rho}{\rho^2}\le -1$$

in the supporting sense, and applying the **Schwarz–Ahlfors lemma**: if $\rho$ is ultrahyperbolic on $\mathbb{D}$ with $K_\rho\le -1$, then $\rho(z)\le \lambda_{\mathbb D}(z)=\dfrac{2}{1-|z|^2}$.

**The extremal candidate.** Ahlfors and Grunsky constructed $f_0\in\mathcal{F}$ mapping $\mathbb{D}$ conformally onto a Riemann surface spread over $\mathbb{C}$, branched with simple branch points over the vertices of an equilateral triangular lattice, obtained by reflection from a Schwarz triangle map of a hyperbolic triangle with angles $\left(\tfrac{\pi}{3},\tfrac{\pi}{3},0\right)$. Every schlicht disk of $f_0$ has radius at most the distance from a lattice cell centre to the nearest branch point, giving

$$b(f_0)=\frac{\Gamma(1/3)\,\Gamma(11/12)}{(1+\sqrt3)^{1/2}\,\Gamma(1/4)}=0.47186\ldots$$

Hence $B\le 0.47186\ldots$ unconditionally; the conjecture is that this is an equality.

**Companion constants.** Landau proved $L\le \dfrac{\Gamma(1/3)\Gamma(5/6)}{\Gamma(1/6)}=0.5432\ldots$, conjectured sharp (Rademacher), and $L\ge 1/2$.

## 3. History & State of the Art (SOTA)

- **1925.** André Bloch, in *Les théorèmes de M. Valiron…*, proves the existence of an absolute constant; his implicit value is roughly $1/72$.
- **1929.** Landau (*Math. Z.* 30) isolates the constants $B$ and $L$ as "Weltkonstanten", proves $L\ge 1/2$ and $B\ge 1/16$-type bounds, and popularizes the extremal problem.
- **1937.** Ahlfors and Grunsky (*Math. Z.* 42, 671–673) produce the branched extremal candidate, giving the upper bound $0.4719$, and conjecture its extremality.
- **1938.** Ahlfors (*Trans. AMS* 43) proves $B\ge \sqrt3/4=0.43301\ldots$ by the ultrahyperbolic-metric method — still the structural core of every lower bound.
- **1962.** Heins (*Nagoya Math. J.* 21) shows the Ahlfors bound is **not** attained: $B>\sqrt3/4$ strictly, but with no effective increment.
- **1990.** Bonk (*Proc. AMS* 110) makes Heins effective via his distortion theorem for Bloch functions: $B\ge \sqrt3/4+10^{-14}$.
- **1996.** Chen and Gauthier (*J. Anal. Math.* 69) refine Bonk's method: $B\ge \sqrt3/4+2\times10^{-4}=0.43321\ldots$.
- **1998.** Xiong (*Nagoya Math. J.* 150) gives a further small numerical improvement by sharpening the same distortion estimates.
- **1995.** Yanagihara (*J. Anal. Math.* 65) proves the locally univalent Bloch constant satisfies $B_1\ge 1/2+10^{-335}$, showing the corresponding "$1/2$" barrier is not extremal either.
- **1998.** Baernstein and Vinson establish *local* minimality properties of the Ahlfors–Grunsky and Rademacher candidates within restricted deformation classes.

Numerically nothing has moved the leading digits since 1938: the certified interval is $[0.4332,\,0.4719]$, a gap of about $0.039$, i.e. roughly $8\%$ of the conjectured value.

## 4. Partial Results / Verified Cases

- **Two-sided bounds.** $\sqrt3/4+2\times10^{-4}\le B\le 0.4718617\ldots$ (Ahlfors 1938; Chen–Gauthier 1996; Ahlfors–Grunsky 1937).
- **Non-extremality of the metric bound.** Heins (1962): equality $B=\sqrt3/4$ is impossible; the extremal configuration for the Schwarz–Ahlfors comparison cannot be realized by an actual holomorphic map.
- **Locally univalent class.** $1/2+10^{-335}\le B_1\le 0.5433$ (Yanagihara 1995; Landau's upper bound); the same qualitative picture — the naive barrier $1/2$ is beaten, the conjectured value is not reached.
- **Univalent class solved.** For univalent $f\in\mathcal F$ the analogous constant is exactly $\log(1+\sqrt2)\cdot$-type; more simply, the sharp inscribed-disk constant for the full univalent class is $1/4$ by the Koebe one-quarter theorem, and the Bloch-type constant for univalent maps equals $\sqrt{3}/4\cdot$ ... — in all such subfamilies the extremal problem is closed because the Koebe function is an explicit extremal. The obstruction is specific to branched maps.
- **Local extremality.** Baernstein–Vinson (1998): the Ahlfors–Grunsky function is a local minimum of $b(\cdot)$ under certain finite-dimensional perturbations, supporting the conjecture.
- **Generalizations settled.** Bonk–Eremenko (*Ann. of Math.* 152, 2000) determined the sharp constant for the analogous covering problem for meromorphic functions on the plane using spherical geometry — the sharp radius is $\arccos(1/3)$ — showing that curvature-comparison methods *can* be pushed to sharpness in a curved target.
- **Harmonic and several-variable analogues.** Chen–Gauthier–Hengartner (2000) give explicit Bloch constants for planar harmonic mappings; FitzGerald–Gong (1994) prove Bloch-type theorems in $\mathbb{C}^n$ with non-sharp constants.

## 5. Principal Obstacles

- **The metric method is structurally lossy.** Ahlfors' ultrahyperbolic metric is built by patching around branch points; the comparison $\rho\le\lambda_{\mathbb D}$ is sharp only for a metric that no actual holomorphic map realizes (Heins). Every refinement (Bonk, Chen–Gauthier, Xiong) recovers only an $\varepsilon$ of the loss, because the loss is spread over the whole configuration rather than concentrated at a fixable point.
- **No compactness for the extremal problem.** $b(\cdot)$ is not upper semicontinuous in a way that survives normal-family limits: minimizing sequences can push branch points to the boundary of $\mathbb{D}$ and degenerate. Existence of an extremal function is itself not established, so a variational argument has no fixed object to perturb.
- **The functional is non-smooth.** $b(f)=\sup_a \rho(a,f)$ is a supremum of quantities defined by a global injectivity condition. First-variation calculus produces inequalities only at the (typically many) points where the supremum is attained, and the injectivity constraint is not differentiable.
- **Branching is combinatorial.** The conjectured extremal has infinitely many branch points arranged in a lattice. Any proof must simultaneously control a discrete combinatorial pattern and a conformal modulus, and no known technique (quasiconformal deformation, extremal length, Loewner flow) handles both at once.
- **Numerics do not certify.** One can compute $b(f)$ for explicit trial functions, but $B$ is an infimum over an infinite-dimensional family; no finite computation excludes a better competitor, and no rigorous finite-dimensional reduction is known.

## 6. The Gap

Proven: $B\ge \sqrt3/4+2\times10^{-4}$. Conjectured: $B=0.4718617\ldots$. The gap is the interval $(0.4333,\,0.4719)$.

The precise missing step: **upgrade the Schwarz–Ahlfors comparison from a pointwise curvature inequality to a rigidity statement that identifies the extremal branching pattern.** Ahlfors' argument only uses $K\le-1$ near each branch point; it never uses the *global* incompatibility of a dense branch set with a schlicht disk of subcritical radius. One needs an inequality of the form: if $b(f)<r$ then the branch set of $f$ must be at least as dense as the equilateral lattice, and any such density forces $\|f\|_{\mathcal B}$ below the normalization $f'(0)=1$. Equivalently, one needs existence plus uniqueness of an extremal function; either half alone would be a major advance.

## 7. Current Research (as of June 2026)

- **Sharp curvature comparison.** The Bonk–Eremenko programme — replacing pointwise curvature bounds by sharp geometric comparison with a model surface — remains the most promising template. Groups working in geometric function theory at Michigan/Purdue (Bonk, Eremenko school) and in Chinese universities (Chen Huaihui's school, Nanjing) continue to pursue sharp forms.
- **Incremental distortion estimates.** Improvements to Bonk's distortion theorem for Bloch functions continue to appear; reported increments remain in the $10^{-3}$–$10^{-4}$ range and do not change the leading digits. *(frontier — verify)*
- **Computer-assisted variational study.** Interval-arithmetic exploration of finite-branch-point trial surfaces, testing local minimality of the Ahlfors–Grunsky configuration numerically. No certified global bound has emerged. *(frontier — verify)*
- **Harmonic, quasiregular and higher-dimensional analogues.** Sharp Bloch constants for planar harmonic mappings and $K$-quasiregular maps are an active side channel, on the hypothesis that a solvable relative may reveal the right mechanism.

## 8. Future Work

- Prove **existence of an extremal function** for $B$ by controlling degeneration of minimizing sequences; this alone would open the door to variational methods.
- Develop a **rigidity form of the Schwarz–Ahlfors lemma**: characterize when equality is approached, in terms of the geometry of the branch set.
- Import **extremal length / modulus of curve families** arguments to convert schlicht-disk radius into a conformal modulus that can be compared with the lattice model.
- Settle the **Landau constant** $L=\Gamma(1/3)\Gamma(5/6)/\Gamma(1/6)$ first: the unbranched problem is strictly easier and may isolate the correct comparison principle.
- Push the **Bonk–Eremenko spherical method** back to the plane by treating the branched surface as a hyperbolic orbifold and using orbifold uniformization.

## 9. Key References

- **[Foundational]** A. Bloch. *Les théorèmes de M. Valiron sur les fonctions entières et la théorie de l'uniformisation.* Annales de la Faculté des Sciences de Toulouse (3) 17 (1925), 1–22. [DOI](https://doi.org/10.5802/afst.335)
- **[Foundational]** E. Landau. *Über die Blochsche Konstante und zwei verwandte Weltkonstanten.* Mathematische Zeitschrift 30 (1929), 608–634. [DOI](https://doi.org/10.1007/bf01187791)
- **[Foundational]** L. V. Ahlfors, H. Grunsky. *Über die Blochsche Konstante.* Mathematische Zeitschrift 42 (1937), 671–673. [DOI](https://doi.org/10.1007/bf01160101)
- **[Foundational]** L. V. Ahlfors. *An extension of Schwarz's lemma.* Transactions of the American Mathematical Society 43 (1938), 359–364.
- **[Structural]** M. Heins. *On a class of conformal metrics.* Nagoya Mathematical Journal 21 (1962), 1–60. [DOI](https://doi.org/10.1017/s002776300002376x)
- **[SOTA]** M. Bonk. *On Bloch's constant.* Proceedings of the American Mathematical Society 110 (1990), 889–894.
- **[SOTA]** H. Chen, P. M. Gauthier. *On Bloch's constant.* Journal d'Analyse Mathématique 69 (1996), 275–291.
- **[SOTA]** C. Xiong. *Lower bound of Bloch's constant.* Nagoya Mathematical Journal 150 (1998), 21–31.
- **[SOTA]** H. Yanagihara. *On the locally univalent Bloch constant.* Journal d'Analyse Mathématique 65 (1995), 1–17. [DOI](https://doi.org/10.1007/bf02788763)
- **[SOTA]** M. Bonk, A. Eremenko. *Covering properties of meromorphic functions, negative curvature and spherical geometry.* Annals of Mathematics 152 (2000), 551–592. [DOI](https://doi.org/10.2307/2661392)
- **[Related]** A. Baernstein II, J. P. Vinson. *Local minimality results related to the Bloch and Landau constants.* In: Quasiconformal Mappings and Analysis, Springer, 1998, 55–89. [DOI](https://doi.org/10.1007/978-1-4612-0605-7_7)
- **[Related]** H. Chen, P. M. Gauthier, W. Hengartner. *Bloch constants for planar harmonic mappings.* Proceedings of the American Mathematical Society 128 (2000), 3231–3240. [DOI](https://doi.org/10.1090/s0002-9939-00-05590-8)
- **[Related]** C. H. FitzGerald, S. Gong. *The Bloch theorem in several complex variables.* Journal of Geometric Analysis 4 (1994), 35–58. [DOI](https://doi.org/10.1007/bf02921592)
- **[Survey]** C. D. Minda. *Bloch constants.* Journal d'Analyse Mathématique 41 (1982), 54–84. [DOI](https://doi.org/10.1007/bf02803394)
- **[Textbook]** J. B. Conway. *Functions of One Complex Variable II.* Springer GTM 159, 1995 (Chapter on Bloch's theorem). [DOI](https://doi.org/10.1007/978-1-4612-0817-4)
- **[Textbook]** Ch. Pommerenke. *Univalent Functions.* Vandenhoeck & Ruprecht, Göttingen, 1975.

## 10. Worked Example / Concrete Special Case

**Computing $b(f)$ for $f(z)=-\log(1-z)$.**

$f(0)=0$, $f'(z)=(1-z)^{-1}$, so $f'(0)=1$ and $f\in\mathcal F$. Since $f$ is univalent on $\mathbb{D}$, $b(f)$ is simply the supremum of radii of disks contained in $\Omega=f(\mathbb{D})$.

Write $w=1-z$. As $z$ ranges over $\mathbb{D}$, $w$ ranges over $|w-1|<1$, i.e. $w=re^{i\theta}$ with $|\theta|<\pi/2$ and $0<r<2\cos\theta$. Then $f=-\log w=-\log r-i\theta$, so with $U=-\log r$, $V=-\theta$:

$$\Omega=\left\{U+iV:\ |V|<\tfrac{\pi}{2},\ U>-\log(2\cos V)\right\}.$$

This is the half-strip-like region of half-width $\pi/2$, closed off on the left by the curve $U=-\log(2\cos V)$, which tends to $+\infty$ as $|V|\to\pi/2$.

*Largest disk centred at the origin.* Minimize $\sqrt{U^2+V^2}$ on the boundary curve. At $V=0$: $U=-\log 2=-0.6931$, distance $0.6931$. At $V=0.3$: $U=-0.6474$, distance $0.7137$. At $V=0.5$: $U=-0.5625$, distance $0.7521$. The minimum is $\log 2=0.693$.

*Largest disk anywhere.* Taking centres $U_0+i0$ with $U_0\to+\infty$, the region locally looks like the full strip $|V|<\pi/2$, so inscribed radii approach $\pi/2$ and never exceed it. Hence

$$b(f)=\frac{\pi}{2}=1.5708.$$

**Interpretation.** $1.5708 \gg 0.4719$: this univalent competitor is far from extremal, consistent with the conjecture. The same happens for the Koebe function $k(z)=z/(1-z)^2$, whose image $\mathbb{C}\setminus(-\infty,-1/4]$ contains disks of arbitrarily large radius, so $b(k)=\infty$. Univalent functions are therefore useless as competitors: the infimum defining $B$ is driven entirely by **heavily branched** maps, whose images are Riemann surfaces with branch points packed as densely as the normalization $f'(0)=1$ permits. The Ahlfors–Grunsky function is exactly such a map — a branched cover of $\mathbb{C}$ over an equilateral lattice — and every schlicht disk in its image is blocked by a nearby branch point at distance $0.47186\ldots$. The open problem is that no argument rules out a cleverer branch configuration blocking at distance below $0.47186$ while still achieving $f'(0)=1$; all we can currently prove is that no configuration blocks below $0.43321$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*