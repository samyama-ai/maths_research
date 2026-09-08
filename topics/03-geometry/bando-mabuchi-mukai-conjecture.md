---
id: 03-geometry/bando-mabuchi-mukai-conjecture
title: "Bando-Mabuchi-Mukai Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bando-Mabuchi-Mukai Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/bando-mabuchi-mukai-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Naming note.** "Bando–Mabuchi–Mukai" is a composite catalog label for the coupled uniqueness-and-existence problem for Kähler–Einstein (KE) metrics on Fano manifolds with continuous automorphisms, whose canonical test object is the Mukai–Umemura threefold. The two halves are due to Bando–Mabuchi (1987) and to Donaldson (2008), building on Mukai–Umemura (1983).

Let $X$ be a Fano manifold of complex dimension $n$: a compact complex manifold with $-K_X$ ample. The conjecture has two parts.

**(A) Uniqueness.** If $\omega_1,\omega_2$ are Kähler–Einstein metrics in $c_1(X)$, then there is $\sigma \in \mathrm{Aut}_0(X)$ (the identity component of the biholomorphism group) with $\sigma^*\omega_1 = \omega_2$. Equivalently, the set of KE metrics in $c_1(X)$ is a single $\mathrm{Aut}_0(X)$-orbit.

**(B) Existence / moduli.** $X$ admits a KE metric if and only if $X$ is K-polystable. Consequently, in a flat family $\mathcal X \to B$ of Fano manifolds with a group $G$ acting fibrewise-equivariantly, the KE locus in $B$ is cut out by a *finite-dimensional GIT* condition. The sharp instance: for the Mukai–Umemura threefold $X_{\mathrm{MU}}$, a small deformation $X_t$ with $t \in H^1(X_{\mathrm{MU}}, T X_{\mathrm{MU}})$ admits a KE metric if and only if $[t]$ is polystable for the induced $\mathrm{PGL}(2,\mathbb C)$-action on $\mathbb P\big(H^1(X_{\mathrm{MU}},TX_{\mathrm{MU}})\big)$.

A complete resolution requires: a proof of (A) with no assumption on $\mathrm{Aut}(X)$; a proof of (B) as an if-and-only-if; and an explicit determination of the GIT-polystable locus in the Mukai–Umemura deformation space. All three are now theorems (Bando–Mabuchi 1987; Chen–Donaldson–Sun 2015), hence the status `solved-recently`. What remains open is the *effective* form: deciding K-polystability for a named Fano variety, and describing the resulting moduli space.

## 2. Mathematical Foundations

**Kähler–Einstein equation.** Fix a Kähler form $\omega_0 \in c_1(X)$ and let $h$ solve $\mathrm{Ric}(\omega_0) - \omega_0 = i\partial\bar\partial h$. A metric $\omega_\varphi = \omega_0 + i\partial\bar\partial\varphi > 0$ is KE with $\mathrm{Ric}(\omega_\varphi) = \omega_\varphi$ iff $\varphi$ solves the complex Monge–Ampère equation
$$(\omega_0 + i\partial\bar\partial\varphi)^n = e^{h-\varphi}\,\omega_0^n .$$

**Obstructions.** Matsushima (1957): if $X$ is KE then $\mathrm{Aut}_0(X)$ is reductive. Futaki (1983): the character
$$\mathrm{Fut}(v) = \int_X v(h)\,\omega_0^n , \qquad v \in \mathfrak{aut}(X),$$
is independent of $\omega_0 \in c_1(X)$ and vanishes identically if $X$ is KE.

**Test configurations and K-stability.** A test configuration for $(X,-K_X)$ is a $\mathbb C^*$-equivariant flat family $\mathcal X \to \mathbb A^1$ with $\mathcal X_1 \cong X$ and a relatively ample $\mathbb C^*$-linearised $\mathcal L$. Its Donaldson–Futaki invariant is read from the expansions
$$\dim H^0(\mathcal X_0, \mathcal L_0^{k}) = a_0k^n + a_1k^{n-1}+O(k^{n-2}), \quad \mathrm{wt}\,H^0(\mathcal X_0,\mathcal L_0^{k}) = b_0k^{n+1}+b_1k^{n}+O(k^{n-1}),$$
$$\mathrm{DF}(\mathcal X,\mathcal L) = \frac{a_1b_0 - a_0b_1}{a_0^2}.$$
$X$ is **K-semistable** if $\mathrm{DF}\ge 0$ always; **K-polystable** if in addition $\mathrm{DF}=0$ only for product configurations.

**Alpha invariant.** $\alpha(X) = \sup\{\alpha : \int_X e^{-\alpha(\varphi - \sup\varphi)}\omega_0^n < C_\alpha \ \forall \varphi \in \mathrm{PSH}(X,\omega_0)\}$. Tian's criterion (1987): $\alpha(X) > \tfrac{n}{n+1}$ implies $X$ is KE.

**Mukai–Umemura threefold.** $X_{\mathrm{MU}}$ is the prime Fano threefold of index $1$, genus $12$, with $-K^3 = 22$ (family №1.10, the $V_{22}$'s), realised as the closure of the $\mathrm{SL}(2,\mathbb C)$-orbit of the icosahedral binary form
$$f_{12}(x,y) = xy\,(x^{10} + 11x^5y^5 - y^{10})$$
inside $\mathbb P(\mathrm{Sym}^{12}\mathbb C^2) = \mathbb P^{12}$. Its automorphism group is $\mathrm{PGL}(2,\mathbb C)$, and $H^1(X_{\mathrm{MU}},TX_{\mathrm{MU}})$ is an irreducible $\mathrm{SL}(2,\mathbb C)$-representation, so the deformation space carries a natural GIT problem.

## 3. History & State of the Art (SOTA)

- **1957–1983.** Matsushima's reductivity obstruction; Futaki's character. Both show KE existence on Fano manifolds is not automatic, in contrast to Yau's solution of Calabi for $c_1 \le 0$.
- **1983.** Mukai–Umemura construct $X_{\mathrm{MU}}$ as a compactification of $\mathrm{SL}(2,\mathbb C)/I$ ($I$ = binary icosahedral group), the first Fano threefold with non-finite automorphism group in its family.
- **1987.** Bando–Mabuchi prove (A) in full: uniqueness modulo $\mathrm{Aut}_0(X)$, via the continuity method along $\mathrm{Ric}(\omega_t)=t\omega_t + (1-t)\omega_0$ plus a connectedness/openness argument.
- **1987.** Tian's $\alpha$-invariant criterion; 1990, Tian settles KE existence for all del Pezzo surfaces.
- **1997–2002.** Tian introduces analytic K-stability; Donaldson gives the algebro-geometric Donaldson–Futaki formulation and states the Yau–Tian–Donaldson (YTD) conjecture for Fano manifolds.
- **2008.** Donaldson computes $\alpha(X_{\mathrm{MU}}) = 5/6 > 3/4$, giving a KE metric on $X_{\mathrm{MU}}$, and formulates the deformation conjecture (B).
- **2010.** Székelyhidi exhibits explicit small deformations of $X_{\mathrm{MU}}$ that are K-unstable, showing the KE locus is a *proper* subset — the conjecture is not vacuous.
- **2015.** Chen–Donaldson–Sun prove YTD for Fano manifolds (three papers, JAMS 28), and deduce Donaldson's Mukai–Umemura deformation statement.
- **2016–2023.** Odaka–Spotti–Sun build explicit KE moduli for del Pezzo surfaces; Berman–Boucksom–Jonsson give a variational proof of YTD; Li–Wang–Xu and Liu–Xu–Zhuang construct projective K-moduli spaces of Fano varieties.
- **2023.** The Calabi problem for Fano threefolds (Araujo et al.) determines K-polystability of general members for $101$ of the $105$ deformation families.

## 4. Partial Results / Verified Cases

- **Uniqueness (A):** proved unconditionally in all dimensions $n$ (Bando–Mabuchi 1987). Extended to twisted and singular settings: Berndtsson (2015) via a Brunn–Minkowski/plurisubharmonic-variation argument; Berman–Boucksom–Guedj–Zeriahi for KE metrics on $\mathbb Q$-Fano varieties with klt singularities.
- **Existence (B), $n=1$:** $\mathbb P^1$, trivially KE.
- **$n=2$:** $X$ del Pezzo is KE iff $X \not\cong \mathrm{Bl}_1\mathbb P^2, \mathrm{Bl}_2\mathbb P^2$ (Tian 1990); these two are exactly the non-reductive cases.
- **$n=3$:** general members of $101$ of the $105$ families are decided (Araujo–Castravet–Cheltsov–Fujita–Kaloghiros–Martinez-Garcia–Shramov–Süß–Viswanathan, 2023). For family №1.10 ($V_{22}$, $-K^3=22$) the general member is K-stable, while $X_{\mathrm{MU}}$ itself is K-polystable with $\mathrm{Aut}_0 = \mathrm{PGL}(2,\mathbb C)$.
- **Mukai–Umemura deformations:** Székelyhidi (2010) shows deformations in the direction of a binary form with a root of multiplicity exceeding half the degree are K-unstable; CDS (2015) show polystable directions are KE.
- **Toric and $T$-varieties:** $X$ toric Fano is KE iff the barycentre of the reflexive polytope $P$ is the origin (Wang–Zhu 2004) — a finite, checkable condition in every dimension.
- **Hypersurfaces:** smooth Fano hypersurfaces $X_d \subset \mathbb P^{n+1}$ of degree $d \ge 3$ are K-stable (Fujita 2019 / Liu–Xu; $\delta$-invariant estimates).

## 5. Principal Obstacles

- **Infinitely many test configurations.** K-polystability quantifies over all degenerations. Reduction to a finite check requires finite generation of the associated graded ring, only established in 2022 (Liu–Xu–Zhuang) and non-constructive in practice.
- **Failure of the implicit function theorem across the automorphism jump.** Near $X_{\mathrm{MU}}$, $\mathrm{Aut}$ drops from $3$-dimensional to finite. The linearised Monge–Ampère operator has a $3$-dimensional cokernel from holomorphic vector fields, so no uniform Schauder estimate holds; the KE metrics on nearby $X_t$ blow up in the Gromov–Hausdorff sense unless $t$ is balanced against the $\mathrm{PGL}(2)$-moment map.
- **No a-priori $C^0$ bound.** The Monge–Ampère equation has no maximum-principle bound on $\varphi$ when $\mathrm{Fut}\ne 0$; the "partial $C^0$ estimate" — uniform lower bounds on Bergman kernels along the continuity path — needed the full Cheeger–Colding–Tian regularity theory of non-collapsed Ricci limit spaces, which is why the proof waited 20 years.
- **Non-effectivity of $\alpha$ and $\delta$.** Tian's criterion is sufficient only; $\alpha(X) \le n/(n+1)$ gives no information, and $\alpha$ is itself an infimum over log canonical thresholds of all effective $\mathbb Q$-divisors, hard to compute outside high-symmetry cases.
- **Singular limits.** Even when each $X_t$ is smooth, the Gromov–Hausdorff limit is a singular $\mathbb Q$-Fano variety; algebraicity of these limits (Donaldson–Sun) was itself a major theorem, not a technical lemma.

## 6. The Gap

The remaining gap is no longer existence-vs-uniqueness but **decidability and explicitness**:

1. YTD (B) converts an analytic question into an algebraic one, but K-polystability is not known to be decidable by a terminating algorithm for a given Fano variety of dimension $\ge 4$. The gap is between "finitely many test configurations suffice" (abstract, via finite generation) and "here is the finite list".
2. For Fano threefolds, $4$ of the $105$ families still lack a determination of the general member.
3. Section 4's GIT description of the KE locus is proved only for small deformations of $X_{\mathrm{MU}}$; a global identification of the K-moduli of $V_{22}$'s with a GIT quotient of binary forms is known in outline but the wall-crossing structure for larger deformations is not fully described.

## 7. Current Research (as of June 2026)

- **K-moduli and wall-crossing.** Ascher–DeVleming–Liu compute K-moduli of low-degree Fano hypersurfaces and log Fano pairs by variation of stability; the programme aims at explicit projective compactifications of $V_{22}$-moduli.
- **Valuative invariants.** The $\delta$-invariant (Fujita–Odaka; Blum–Jonsson) reduces K-stability to $\delta(X) > 1$; current work computes $\delta$ via Abban–Zhuang flag-type induction, which drove the Fano-threefold classification.
- **Higher-dimensional Calabi problem.** Groups at Edinburgh, Nottingham, Princeton, MIT, Peking (BICMR) and Kyoto extend the threefold methods to Fano fourfolds and to $T$-varieties of low complexity. *(frontier — verify)*
- **Non-Archimedean pluripotential theory.** Boucksom–Jonsson's framework recasts DF as an energy on the Berkovich analytification; ongoing work seeks a purely non-Archimedean proof of YTD avoiding Cheeger–Colding. *(frontier — verify)*
- **Kähler–Ricci flow.** The Hamilton–Tian conjecture (Bamler; Chen–Wang) gives flow-based access to the polystable degeneration, with recent work on the algebraicity of the optimal degeneration. *(frontier — verify)*

## 8. Future Work

- Produce an effective algorithm certifying K-polystability from the defining equations of a Fano variety, using finite generation of valuation-graded rings.
- Settle the four undetermined Fano threefold families and begin a systematic fourfold census.
- Give a complete GIT-theoretic description of the K-moduli component containing $X_{\mathrm{MU}}$, including all walls.
- Extend Bando–Mabuchi uniqueness to constant scalar curvature Kähler metrics in general polarisations (the cscK YTD conjecture), where uniqueness is known (Berman–Berndtsson, Chen–Cheng) but existence is not.

## 9. Key References

- **[Foundational]** S. Bando, T. Mabuchi. *Uniqueness of Einstein Kähler metrics modulo connected group actions.* Advanced Studies in Pure Mathematics 10 (Algebraic Geometry, Sendai 1985), 11–40, 1987.
- **[Foundational]** S. Mukai, H. Umemura. *Minimal rational threefolds.* In: Algebraic Geometry (Tokyo/Kyoto 1982), Lecture Notes in Mathematics 1016, Springer, 490–518, 1983. [DOI](https://doi.org/10.1007/bfb0099976)
- **[Foundational]** G. Tian. *On Kähler–Einstein metrics on certain Kähler manifolds with $C_1(M)>0$.* Inventiones Mathematicae 89, 225–246, 1987.
- **[Foundational]** A. Futaki. *An obstruction to the existence of Einstein Kähler metrics.* Inventiones Mathematicae 73, 437–443, 1983.
- **[Foundational]** S. K. Donaldson. *Scalar curvature and stability of toric varieties.* Journal of Differential Geometry 62, 289–349, 2002. [DOI](https://doi.org/10.4310/jdg/1090950195)
- **[SOTA]** S. K. Donaldson. *A note on the $\alpha$-invariant of the Mukai–Umemura 3-fold.* arXiv:0711.4357, 2007.
- **[SOTA]** G. Székelyhidi. *The Kähler–Ricci flow and K-polystability.* American Journal of Mathematics 132, 1077–1090, 2010. [DOI](https://doi.org/10.1353/ajm.0.0128)
- **[SOTA]** X. Chen, S. Donaldson, S. Sun. *Kähler–Einstein metrics on Fano manifolds, I–III.* Journal of the American Mathematical Society 28, 183–197, 199–234, 235–278, 2015.
- **[SOTA]** B. Berndtsson. *A Brunn–Minkowski type inequality for Fano manifolds and some uniqueness theorems in Kähler geometry.* Inventiones Mathematicae 200, 149–200, 2015. [DOI](https://doi.org/10.1007/s00222-014-0532-1)
- **[SOTA]** R. Berman, S. Boucksom, M. Jonsson. *A variational approach to the Yau–Tian–Donaldson conjecture.* Journal of the American Mathematical Society 34, 605–652, 2021. [DOI](https://doi.org/10.1090/jams/964)
- **[SOTA]** Y. Liu, C. Xu, Z. Zhuang. *Finite generation for valuations computing stability thresholds and applications to K-stability.* Annals of Mathematics 196, 507–566, 2022. [DOI](https://doi.org/10.4007/annals.2022.196.2.2)
- **[Survey]** C. Xu. *K-stability of Fano varieties.* Cambridge University Press (New Mathematical Monographs), 2025. [DOI](https://doi.org/10.1017/9781009538763)
- **[Survey]** C. Araujo, A.-M. Castravet, I. Cheltsov, K. Fujita, A.-S. Kaloghiros, J. Martinez-Garcia, C. Shramov, H. Süß, N. Viswanathan. *The Calabi Problem for Fano Threefolds.* London Mathematical Society Lecture Note Series 485, Cambridge University Press, 2023.
- **[Survey]** Y. Odaka, C. Spotti, S. Sun. *Compact moduli spaces of del Pezzo surfaces and Kähler–Einstein metrics.* Journal of Differential Geometry 102, 127–172, 2016. [DOI](https://doi.org/10.4310/jdg/1452002879)

## 10. Worked Example / Concrete Special Case

**(a) Bando–Mabuchi uniqueness on $\mathbb P^1$.** Take $n=1$, $\omega_0 = \omega_{FS}$ with $\int_{\mathbb P^1}\omega_{FS}=2\pi$, normalised so $\mathrm{Ric}(\omega_{FS})=\omega_{FS}$. A competing KE metric is $\omega_\varphi = \omega_{FS} + i\partial\bar\partial\varphi$ solving $e^{-\varphi}\omega_{FS} = \omega_\varphi$. In the coordinate $z$, writing $\omega_{FS} = \frac{i\,dz\wedge d\bar z}{(1+|z|^2)^2}$, every solution has the form
$$\omega_\varphi = \sigma^*\omega_{FS}, \qquad \sigma(z)=\frac{az+b}{cz+d}\in \mathrm{PGL}(2,\mathbb C)=\mathrm{Aut}_0(\mathbb P^1),$$
and nothing else: the moduli of KE metrics is the $3$-complex-dimensional group orbit, not a point. This is exactly why (A) must be stated "modulo $\mathrm{Aut}_0$".

**(b) GIT test for Mukai–Umemura deformations.** Deformation directions are binary forms $g(x,y)=\sum_{i=0}^{d} a_i x^i y^{d-i}$ acted on by $\mathrm{SL}(2,\mathbb C)$. For the one-parameter subgroup $\lambda(t)=\mathrm{diag}(t,t^{-1})$, the monomial $x^iy^{d-i}$ has weight $2i-d$, so the Hilbert–Mumford weight is
$$\mu(g,\lambda) = \max\{\,d-2i \;:\; a_i \ne 0\,\}.$$
Applying the classical criterion, $[g]$ is unstable iff some root of $g$ has multiplicity $> d/2$, and strictly semistable iff some root has multiplicity exactly $d/2$.

Check the base point: $f_{12} = xy(x^{10}+11x^5y^5-y^{10})$ has $12$ **distinct** roots — the $12$ vertices of an icosahedron on $\mathbb P^1$ — so every multiplicity is $1 < 6$, and $[f_{12}]$ is GIT-stable with stabiliser the binary icosahedral group. Correspondingly $X_{\mathrm{MU}}$ is K-polystable and, by Donaldson's computation,
$$\alpha(X_{\mathrm{MU}}) = \frac{5}{6} > \frac{3}{4} = \frac{n}{n+1}\Big|_{n=3},$$
so Tian's criterion already gives the KE metric directly.

Now take a deformation direction $g_0 = x^{k}h(x,y)$ where $x$ divides $g_0$ to order $k > d/2$. Then $\lambda(t)\cdot g_0 \to 0$ as $t\to 0$, so $[g_0]$ is GIT-unstable, and the induced $\mathbb C^*$-degeneration of $X_{t g_0}$ has $\mathrm{DF} < 0$. Székelyhidi's construction is of this type: the deformed threefold $X_{tg_0}$ carries **no** KE metric for any $t \ne 0$, even though it is a smooth Fano threefold in the same family as the KE manifold $X_{\mathrm{MU}}$. The KE locus near $X_{\mathrm{MU}}$ is therefore the image of the polystable cone $\{[g] \text{ polystable}\}$ — a proper, Zariski-open-modulo-orbits subset — exactly as asserted in Section 1(B).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*