---
id: 04-topology/gromov-bounded-cohomology-conjecture
title: "Gromov Bounded Cohomology Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gromov Bounded Cohomology Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/gromov-bounded-cohomology-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Bounded cohomology, introduced by Gromov in *Volume and bounded cohomology* (1982), is the cohomology of the complex of **bounded** real cochains. It is invisible to most of the machinery of algebraic topology: it is not finitely generated, has no Mayer–Vietoris in the usual form, and vanishes for every amenable group. Gromov's guiding structural principle — repeated as an explicit question in his 1993 *Asymptotic invariants* and promoted to a headline problem by Monod (ICM 2006) — is that bounded cohomology admits **no intermediate behaviour**.

**Conjecture (Gromov dichotomy).** Let $\Gamma$ be a finitely presented group and $n \ge 2$. Then
$$H^n_b(\Gamma;\mathbb{R}) \;=\; 0 \qquad\text{or}\qquad \dim_{\mathbb{R}} H^n_b(\Gamma;\mathbb{R}) \;=\; \infty .$$
In the strong form, the non-vanishing alternative asserts that $H^n_b(\Gamma;\mathbb{R})$ is **non-separable** in the quotient seminorm topology, i.e. has cardinality of the continuum as a Banach-space-like object.

Two companion statements travel under the same name and are treated here as variants:

* **(V1) Comparison-map surjectivity.** For $\Gamma$ word-hyperbolic (Gromov 1993) the comparison map $c^n\colon H^n_b(\Gamma;V)\to H^n(\Gamma;V)$ is surjective for all $n\ge 2$ and all bounded $\Gamma$-modules $V$.
* **(V2) Aspherical simplicial volume.** Every closed aspherical manifold $M$ with $\pi_1(M)$ non-amenable has a non-trivial bounded-cohomological obstruction; the sharpest form is $\|M\|>0$ for aspherical $M$.

A complete solution of the main conjecture requires either a uniform mechanism producing infinitely many linearly independent classes from one non-zero class, or a finitely presented $\Gamma$ and degree $n$ with $0 < \dim H^n_b(\Gamma;\mathbb{R}) < \infty$.

## 2. Mathematical Foundations

For a discrete group $\Gamma$ and a normed $\mathbb{R}[\Gamma]$-module $V$, set
$$C^n_b(\Gamma;V) \;=\; \{\, f\colon \Gamma^{n+1}\to V \;:\; \sup_{\bar g}\|f(\bar g)\|<\infty \,\}^{\Gamma},$$
with the homogeneous differential
$$(\delta f)(g_0,\dots,g_{n+1}) \;=\; \sum_{i=0}^{n+1} (-1)^i f(g_0,\dots,\widehat{g_i},\dots,g_{n+1}).$$
Then $H^n_b(\Gamma;V) = \ker\delta^n/\operatorname{im}\delta^{n-1}$, equipped with the quotient seminorm
$$\|\alpha\|_\infty \;=\; \inf\{\, \|f\|_\infty \;:\; [f]=\alpha \,\},$$
which may be degenerate — the *zero-norm subspace* is exactly the obstruction studied by Soma. The inclusion $C^*_b\hookrightarrow C^*$ induces the **comparison map** $c^*\colon H^*_b\to H^*$.

Three structural theorems frame everything:

1. **Vanishing (Gromov; Ivanov; Johnson).** If $\Gamma$ is amenable then $H^n_b(\Gamma;\mathbb{R})=0$ for all $n\ge 1$.
2. **Mapping theorem (Gromov 1982; Ivanov 1987).** For a countable CW-complex $X$, the classifying map induces an isometric isomorphism $H^*_b(X;\mathbb{R})\cong H^*_b(\pi_1(X);\mathbb{R})$; more generally $\pi_1$-surjective maps with amenable kernel are isometric isomorphisms on $H^*_b$.
3. **Degree 2 and quasimorphisms.** A map $\phi\colon\Gamma\to\mathbb{R}$ is a *quasimorphism* if its defect $D(\phi)=\sup_{g,h}|\phi(g)+\phi(h)-\phi(gh)|$ is finite; $Q(\Gamma)$ denotes the homogeneous ones ($\phi(g^k)=k\phi(g)$). There is an exact sequence
$$0 \to H^1(\Gamma;\mathbb{R}) \to Q(\Gamma) \xrightarrow{\;\delta\;} H^2_b(\Gamma;\mathbb{R}) \xrightarrow{\;c^2\;} H^2(\Gamma;\mathbb{R}),$$
so $\ker c^2 \cong Q(\Gamma)/H^1(\Gamma;\mathbb{R})$.

The topological payoff is the **simplicial volume** $\|M\| = \inf\{\sum|a_i| : \sum a_i\sigma_i \text{ a fundamental cycle}\}$, which by duality satisfies $\|M\| = \sup\{\,1/\|\alpha\|_\infty\,\}^{-1}$-type relations with $H^n_b$; in particular $\|M\|>0$ iff the fundamental class pairs non-trivially with a bounded class.

## 3. History & State of the Art (SOTA)

* **1972–1981.** Johnson's amenability criterion in Banach-algebra cohomology; Trauber's unpublished vanishing result; Brooks (1981) constructs infinitely many independent quasimorphisms on free groups.
* **1982.** Gromov, *Volume and bounded cohomology* (Publ. IHÉS 56): defines $\|M\|$, proves the mapping theorem and proportionality principle, computes $\|M\|$ for hyperbolic $M$ via straightening.
* **1984–1987.** Mitsumatsu computes $H^2_b$ of surfaces; Ivanov gives the homological-algebra foundation (relatively injective resolutions), which makes bounded cohomology a functorial theory rather than a collection of tricks.
* **1993.** Gromov's *Asymptotic invariants* poses the dichotomy and the hyperbolic surjectivity question.
* **1997–2002.** Epstein–Fujiwara: $\dim H^2_b(\Gamma;\mathbb{R})=\infty$ for every non-elementary word-hyperbolic $\Gamma$. Soma: non-separability of $H^3_b$ for hyperbolic 3-manifold groups. Burger–Monod: $H^2_b$ vanishing for higher-rank lattices. Mineyev: **(V1) is a theorem for word-hyperbolic groups** — surjectivity of $c^n$, $n\ge2$, all bounded coefficients — and conversely bounded surjectivity characterises hyperbolicity.
* **2001–2017.** Monod's continuous theory (LNM 1758) and Frigerio's monograph (AMS Surveys 227, 2017) consolidate the field.
* **2021–2024.** A wave of *bounded acyclicity* results: Monod proves Thompson's group $F$ is boundedly acyclic; Fournier-Facio–Löh–Moraschini produce finitely presented boundedly acyclic groups; Monod–Nariman compute $H^*_b$ of homeomorphism and diffeomorphism groups. These all land on the *vanishing* side of the dichotomy — no finite non-zero dimension has ever surfaced.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Amenable groups (all $n\ge1$) | $H^n_b=0$ — vanishing side | Johnson 1972; Gromov 1982 |
| Non-elementary word-hyperbolic $\Gamma$, $n=2$ | $\dim H^2_b(\Gamma;\mathbb{R})=\infty$, non-separable | Epstein–Fujiwara 1997 |
| Free groups $F_k$, $k\ge2$, $n=2,3$ | non-separable; $H^3_b(F_2;\mathbb{R})\neq0$ | Brooks 1981; Soma 1997 |
| Word-hyperbolic $\Gamma$, all $n\ge2$ | $c^n$ surjective (variant V1 **proved**) | Mineyev 2001, 2002 |
| Subgroups of mapping class groups, non-virtually-abelian | $\dim H^2_b=\infty$ | Bestvina–Fujiwara 2002 |
| Irreducible lattices in higher-rank Lie groups | $H^2_b(\Gamma;\mathbb{R})=0$ — vanishing side | Burger–Monod 1999 |
| $\mathrm{Homeo}_c(\mathbb{R}^n)$, binate/mitotic groups | boundedly acyclic, all $n\ge1$ | Matsumoto–Morita 1985; Fournier-Facio–Löh–Moraschini 2023 |
| Thompson's group $F$ | boundedly acyclic | Monod 2022 |
| Closed hyperbolic $M^n$, $n\ge2$ | $\|M\|>0$; V2 holds | Gromov 1982; Thurston |
| Groups with $\dim H^2_b < \infty$, non-zero | **none known in any degree** | — |

Degree $n=2$ is the only degree where the dichotomy is verified across a large class: for every countable group either $Q(\Gamma)$ reduces to homomorphisms (then $\ker c^2=0$) or it is infinite-dimensional, since a single unbounded homogeneous quasimorphism on a group with a non-abelian free-ish subgroup already generates infinitely many by the Bestvina–Fujiwara/Brooks machinery. No comparable statement is available in degree $3$ or higher.

## 5. Principal Obstacles

* **No finite-dimensional models.** $C^*_b(\Gamma)$ is a huge Banach space; no CW-structure, no cellular chain complex, no finiteness theorem applies. Standard algebraic topology computes cohomology by reducing to finitely generated complexes — precisely the step that is illegal here.
* **Broken exact sequences.** Mayer–Vietoris and the Lyndon–Hochschild–Serre spectral sequence exist only in weakened, seminorm-lossy forms. Amenable subgroups are *invisible*, so decomposing $\Gamma$ along them collapses information instead of organising it.
* **Degree 3 barrier.** The quasimorphism dictionary is a degree-2 phenomenon. There is no known cocycle-level object in degree $\ge 3$ playing the role of $Q(\Gamma)$, so the only successful non-vanishing arguments above degree 2 (Soma) are analytic and manifold-specific.
* **Non-separability is a Banach obstruction, not an algebraic one.** Proving $\dim = \infty$ typically means constructing a continuum of classes with uniformly separated seminorms; a purely algebraic non-vanishing certificate gives no such family.
* **Coefficients.** The dichotomy is *false-in-spirit* for general coefficient modules: examples with prescribed finite-dimensional $H^*_b$ exist for exotic Banach coefficients, so any proof must use $\mathbb{R}$-specific rigidity — which no current technique isolates.

## 6. The Gap

Proved: a dichotomy in degree $2$ for large classes (hyperbolic, acylindrically hyperbolic, mapping class groups) and a growing list of *vanishing* results in all degrees. Conjectured: the same dichotomy in **every** degree $n\ge3$ for **every** finitely presented group.

The precise missing step is an **amplification lemma**: given $0\neq\alpha\in H^n_b(\Gamma;\mathbb{R})$, produce a family $\{\alpha_t\}_{t\in\mathbb{R}}$ of classes with $\|\alpha_t-\alpha_s\|_\infty \ge \varepsilon>0$. In degree 2 this is achieved by perturbing a quasimorphism along independent hyperbolic elements (Brooks/Bestvina–Fujiwara); in degree $\ge3$ nobody knows what to perturb. Equivalently: no cup-product or transfer argument is known that turns one bounded class into infinitely many, because the cup product on $H^*_b$ is norm-non-increasing and frequently kills classes.

## 7. Current Research (as of June 2026)

* **Bounded acyclicity as a computational engine.** Monod's lamplighter/commuting-conjugates criterion and its extensions (Fournier-Facio, Löh, Moraschini) now certify vanishing for large families — transformation groups, binate groups, many groups of homeomorphisms. Groups (Regensburg, EPFL, ETH/Zurich, Oxford) are pushing these to *relative* and *coefficient* versions. *(frontier — verify)*
* **Degree-3 non-vanishing.** Attempts to extend Soma's non-separability from 3-manifold groups to all acylindrically hyperbolic groups, using higher quasi-cocycles (Frigerio–Pozzetti–Sisto). Still open in general. *(frontier — verify)*
* **Simplicial volume of aspherical manifolds (V2).** Ongoing work relating $\|M\|>0$ to macroscopic scalar curvature and to $\ell^2$-invariants; still open even for aspherical $M$ with hyperbolic-like fundamental groups that are not relatively hyperbolic.
* **Homeomorphism groups.** Monod–Nariman (Invent. Math. 2023) computed $H^*_b$ for $\mathrm{Homeo}_0(S^1)$ and $\mathrm{Homeo}_0(D^n\,\mathrm{rel}\,\partial)$; the surprising output — genuine non-trivial classes in a transformation group — is being mined for a degree-$\ge3$ amplification mechanism. *(frontier — verify)*

## 8. Future Work

1. **Find a counterexample deliberately.** Monod suggests looking among groups engineered to have exactly one obstruction — e.g. central extensions of boundedly acyclic groups — where $H^n_b$ might be forced to be $1$-dimensional.
2. **Develop a bounded-coefficient spectral sequence** that does not lose seminorm control, so that vanishing on an amenable normal subgroup can be leveraged rather than discarded.
3. **Higher quasimorphisms.** Define an $n$-dimensional analogue of $Q(\Gamma)$ — candidates: bounded $n$-cocycles on a boundary $\partial\Gamma$ modulo coboundaries, in the spirit of Burger–Monod boundary theory.
4. **Coarse geometry.** Interpret bounded classes as obstructions to coarse-fillings; a quantitative isoperimetric proof of infinite-dimensionality would be degree-agnostic.

## 9. Key References

- **[Foundational]** M. Gromov. *Volume and bounded cohomology.* Publications Mathématiques de l'IHÉS **56** (1982), 5–99.
- **[Foundational]** M. Gromov. *Asymptotic invariants of infinite groups.* In: Geometric Group Theory, Vol. 2, LMS Lecture Note Series 182, Cambridge University Press, 1993.
- **[Foundational]** N. V. Ivanov. *Foundations of the theory of bounded cohomology.* Journal of Soviet Mathematics **37** (1987), 1090–1115.
- **[Foundational]** R. Brooks. *Some remarks on bounded cohomology.* In: Riemann Surfaces and Related Topics, Annals of Mathematics Studies 97, Princeton University Press, 1981, 53–63.
- **[SOTA]** I. Mineyev. *Straightening and bounded cohomology of hyperbolic groups.* Geometric and Functional Analysis **11** (2001), 807–839.
- **[SOTA]** D. B. A. Epstein, K. Fujiwara. *The second bounded cohomology of word-hyperbolic groups.* Topology **36** (1997), 1275–1289.
- **[SOTA]** M. Bestvina, K. Fujiwara. *Bounded cohomology of subgroups of mapping class groups.* Geometry & Topology **6** (2002), 69–89.
- **[SOTA / Recent]** N. Monod. *Lamplighters and the bounded cohomology of Thompson's group F.* Geometric and Functional Analysis **32** (2022), 662–675.
- **[SOTA / Recent]** N. Monod, S. Nariman. *Bounded and unbounded cohomology of homeomorphism and diffeomorphism groups.* Inventiones Mathematicae **232** (2023), 1439–1475.
- **[Recent]** F. Fournier-Facio, C. Löh, M. Moraschini. *Bounded cohomology and binate groups.* Journal of the Australian Mathematical Society, 2023.
- **[Survey]** R. Frigerio. *Bounded Cohomology of Discrete Groups.* Mathematical Surveys and Monographs 227, American Mathematical Society, 2017.
- **[Survey]** N. Monod. *An invitation to bounded cohomology.* Proceedings of the ICM Madrid 2006, Vol. II, EMS, 1183–1211.
- **[Background]** N. Monod. *Continuous Bounded Cohomology of Locally Compact Groups.* Lecture Notes in Mathematics 1758, Springer, 2001.
- **[Background]** T. Soma. *The zero-norm subspace of bounded cohomology.* Commentarii Mathematici Helvetici **72** (1997), 582–592.

## 10. Worked Example / Concrete Special Case

**Claim.** For the free group $F_2=\langle a,b\rangle$, $H^2_b(F_2;\mathbb{R})$ is infinite-dimensional — the dichotomy holds, in its non-vanishing branch.

*Step 1 — the cohomology is trivial.* $F_2$ has a $2$-vertex-free wedge-of-circles classifying space, a $1$-complex, so $H^2(F_2;\mathbb{R})=0$. By the exact sequence of §2 with $H^1(F_2;\mathbb{R})\cong\mathbb{R}^2$:
$$H^2_b(F_2;\mathbb{R}) \;\cong\; Q(F_2)/\mathbb{R}^2 .$$

*Step 2 — Brooks counting quasimorphisms.* For a reduced word $w$, let $|g|_w$ be the number of occurrences of $w$ as a subword of the reduced form of $g$, and set
$$\phi_w(g) \;=\; |g|_w - |g|_{w^{-1}} .$$
Cancellation when concatenating $g$ and $h$ affects only the letters near the seam, so $|\phi_w(gh)-\phi_w(g)-\phi_w(h)| \le 2|w|$; hence $D(\phi_w)\le 4|w|$ and $\phi_w$ is a quasimorphism. Its homogenisation $\overline{\phi_w}(g)=\lim_{k\to\infty}\phi_w(g^k)/k$ exists and lies in $Q(F_2)$.

*Step 3 — infinitely many independent classes.* Take $w_n=a^n b$ for $n\ge1$ and test on $g_m = a^m b$. For $m \ge 1$, $g_m^k = (a^m b)^k$ is already reduced, so $|g_m^k|_{w_n} = k$ if $n=m$ and $0$ otherwise, while $|g_m^k|_{w_n^{-1}} = 0$. Hence
$$\overline{\phi_{w_n}}(g_m) \;=\; \delta_{nm}.$$
The matrix of values is the identity, so $\{\overline{\phi_{w_n}}\}_{n\ge1}$ is linearly independent in $Q(F_2)$; each $\overline{\phi_{w_n}}$ is unbounded, so none is a homomorphism plus a bounded function (homomorphisms $F_2\to\mathbb R$ are determined by their values on $a,b$, and $\overline{\phi_{w_n}}(a)=\overline{\phi_{w_n}}(b)=0$ while $\overline{\phi_{w_n}}(a^nb)=1$).

*Step 4 — conclusion.* $\dim Q(F_2)/\mathbb{R}^2 = \infty$, so $\dim H^2_b(F_2;\mathbb{R})=\infty$. Taking uncountably many $\mathbb{R}$-linear combinations with separated defects upgrades this to non-separability (Brooks; Grigorchuk).

**Contrast.** For $\Gamma=\mathbb{Z}$ (amenable) every homogeneous quasimorphism is a homomorphism, so $H^2_b(\mathbb{Z};\mathbb{R})=0$: the vanishing branch. The conjecture asserts that in degree $3$ and above, and for every finitely presented group, exactly one of these two pictures occurs — and that is what nobody can prove.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*