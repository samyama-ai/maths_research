---
id: 03-geometry/shafarevich-conjecture-holomorphic-convexity
title: "Shafarevich Conjecture on Holomorphic Convexity"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Shafarevich Conjecture on Holomorphic Convexity

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/shafarevich-conjecture-holomorphic-convexity` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Shafarevich, 1972).** Let $X$ be a smooth connected complex projective variety and let $\widetilde{X} \to X$ be its universal covering. Then $\widetilde{X}$ is holomorphically convex.

Equivalently, by the Cartan–Remmert theorem, there exists a proper surjective holomorphic map with connected fibres
$$\mathrm{sh}_X : \widetilde{X} \longrightarrow \mathrm{Sh}(X)$$
onto a normal Stein space $\mathrm{Sh}(X)$ (the *Shafarevich variety*), contracting exactly the connected compact analytic subsets of $\widetilde{X}$.

A complete proof must produce, for every such $X$, a smooth exhaustion whose sublevel sets have compact-analytic-set closure hulls; a disproof must exhibit a single smooth projective $X$ whose universal cover carries a divergent sequence of compact analytic subsets no proper map can separate — concretely, a compact analytic subset $Z \subset X$ whose lifts to $\widetilde{X}$ accumulate.

Variants: the **Kähler Shafarevich conjecture** (replace projective by compact Kähler); the **$\Gamma$-Shafarevich problem** (for a normal subgroup $H \trianglelefteq \pi_1(X)$, ask whether the intermediate cover $\widetilde{X}/H$ is holomorphically convex); and the **linear/reductive Shafarevich conjecture**, where $H$ is the intersection of kernels of a family of linear representations.

## 2. Mathematical Foundations

Let $Y$ be a complex space. $Y$ is **holomorphically convex** if for every compact $K \subset Y$ the holomorphic hull
$$\widehat{K} \;=\; \{\, y \in Y \;:\; |f(y)| \le \sup_K |f| \ \ \forall f \in \mathcal{O}(Y) \,\}$$
is compact. $Y$ is **Stein** if in addition $\mathcal{O}(Y)$ separates points and gives local coordinates. **Cartan–Remmert:** a holomorphically convex complex space admits a proper Remmert reduction $r: Y \to Y'$ with $r_*\mathcal{O}_Y = \mathcal{O}_{Y'}$ and $Y'$ Stein; $Y$ is Stein iff it has no positive-dimensional compact analytic subset.

A key equivalent criterion: $Y$ is holomorphically convex iff it admits a smooth plurisubharmonic exhaustion $\varphi: Y \to \mathbb{R}$ that is *strictly* plurisubharmonic outside a compact-fibred locus, i.e. $i\partial\bar\partial \varphi \ge 0$ with $\varphi$ proper.

**Shafarevich map (Kollár, Campana).** For $X$ smooth projective there is a dominant rational map $\mathrm{sh}_X : X \dashrightarrow \mathrm{Sh}_{\dim}(X)$, unique up to birational equivalence, characterised by: for a very general point $x$ and a closed irreducible subvariety $Z \ni x$,
$$\mathrm{sh}_X(Z) = \text{point} \iff \mathrm{im}\big(\pi_1(\widetilde{Z}^{\mathrm{norm}}) \to \pi_1(X)\big) \text{ is finite},$$
where $\widetilde{Z}^{\mathrm{norm}}$ is a resolution of $Z$. The conjecture asserts this rational map is realised by a genuine proper *holomorphic* map upstairs on $\widetilde{X}$.

**Obstruction language.** Set $\gamma = \pi_1(X)$ and $\rho: \gamma \to GL_n(K)$ a representation over a field $K$. Reductive $\rho$ over $\mathbb{C}$ correspond, by Corlette–Simpson nonabelian Hodge theory, to harmonic bundles / Higgs bundles $(E,\theta)$ with $\theta\wedge\theta=0$, and the harmonic map $u:\widetilde{X}\to \mathcal{N}$ to the symmetric space $GL_n(\mathbb{C})/U(n)$ yields plurisubharmonic functions $\varphi = \mathrm{dist}(u(\cdot), u(x_0))^2$. For $K$ non-archimedean, $\rho$ gives an equivariant harmonic map to a Bruhat–Tits building, producing pluriharmonic $\pi$-forms. The Shafarevich programme builds the exhaustion of $\widetilde{X}$ from these.

**$L^2$ criterion (Napier).** If $\widetilde{X}$ admits a positive-degree $L^2$ holomorphic function theory — e.g. $H^0_{(2)}(\widetilde{X},\mathcal{O})$ separates the ends — then convexity properties follow from Andreotti–Vesentini and Gromov's $L^2$ vanishing.

**Necessity of projectivity.** The Hopf surface $X = (\mathbb{C}^2\setminus\{0\})/\langle z \mapsto 2z\rangle$ has $\widetilde{X}=\mathbb{C}^2\setminus\{0\}$, which is *not* holomorphically convex by Hartogs extension. $X$ is compact complex but not Kähler; this shows the Kähler hypothesis is essential.

## 3. History & State of the Art (SOTA)

- **1972.** I. R. Shafarevich raises the question in *Basic Algebraic Geometry* (Ch. IX, "Uniformisation") as a conjectural higher-dimensional analogue of the uniformisation theorem for curves.
- **1990.** T. Napier proves convexity statements for coverings of projective varieties under $L^2$ and end-structure hypotheses (*Math. Ann.* 286).
- **1993.** J. Kollár introduces Shafarevich maps and proves their existence as rational maps (*Invent. Math.* 113); D. Toledo constructs projective surfaces with non-residually-finite $\pi_1$ (*Publ. IHÉS* 77), removing the hope of reducing to finite covers.
- **1994–95.** F. Campana gives an independent construction of the $\gamma$-reduction; Kollár's book *Shafarevich Maps and Automorphic Forms* (Princeton, 1995) systematises the theory. Napier–Ramachandran prove structure theorems for complete Kähler manifolds with applications to Lefschetz-type results (*GAFA* 5, 1995).
- **1998.** Katzarkov–Ramachandran settle the surface case for large classes of representations (*Ann. Sci. ÉNS* 31). Bogomolov–Katzarkov study symplectic/projective surfaces and propose potential counterexample mechanisms.
- **2004.** P. Eyssidieux proves the conjecture for reductive *linear* covers of projective varieties (*Invent. Math.* 156), using harmonic maps to symmetric spaces and buildings simultaneously.
- **2012.** Eyssidieux–Katzarkov–Pantev–Ramachandran, *Linear Shafarevich conjecture* (*Ann. of Math.* 176): for any linear representation $\rho:\pi_1(X)\to GL_n(\mathbb{C})$, the covering $\widetilde{X}^\rho$ associated with $\ker\rho$ is holomorphically convex. This is the landmark positive result.
- **2023–present.** Deng–Yamanoi extend to reductive representations over arbitrary fields and to non-linear settings via Nevanlinna-theoretic and Katzarkov–Zuo methods.

The general conjecture — for $\pi_1(X)$ with no faithful linear structure — remains open, and no counterexample is known.

## 4. Partial Results / Verified Cases

- **$\dim X = 1$.** Trivially true: $\widetilde{X}\in\{\mathbb{P}^1,\mathbb{C},\mathbb{D}\}$, each holomorphically convex ($\mathbb{P}^1$ compact; $\mathbb{C},\mathbb{D}$ Stein).
- **$\pi_1(X)$ finite.** $\widetilde{X}$ is compact projective, hence holomorphically convex.
- **$X$ with $\pi_1(X)$ abelian, nilpotent, or virtually solvable.** Follows from the linear case plus Campana–Claudon–Eyssidieux type arguments; e.g. for abelian varieties $\widetilde{X}=\mathbb{C}^g$ is Stein.
- **Linear fundamental group (EKPR 2012).** If $\pi_1(X)$ admits a faithful representation into $GL_n(\mathbb{C})$, then $\widetilde{X}$ is holomorphically convex. This covers all $X$ with residually finite *linear* $\pi_1$, all locally symmetric quotients, all $X$ with large linear representations.
- **Non-archimedean/reductive extensions.** Eyssidieux (2004) for reductive $\rho$ into $GL_n(K)$, $K$ any field; Deng–Yamanoi (2023) for reductive $\rho$ over arbitrary fields with the full Shafarevich reduction. *(frontier — verify)*
- **Surfaces ($\dim X = 2$).** Resolved by Katzarkov–Ramachandran (1998) when $\pi_1(X)$ has a nontrivial linear representation with infinite image; open in general for surfaces with only "exotic" (non-linear) infinite $\pi_1$.
- **$\pi_1(X)$ hyperbolic-by-linear / Kähler groups from lattices.** True for $X$ uniformised by bounded symmetric domains: $\widetilde{X}$ is Stein.
- **Nefness hypotheses.** If the cotangent bundle $\Omega^1_X$ is nef and $\pi_1$ infinite, symmetric differentials (Brunebarbe) give the required plurisubharmonic exhaustion.

## 5. Principal Obstacles

1. **Non-linear Kähler groups.** No structure theory covers $\pi_1(X)$ that admit no faithful finite-dimensional representation. Every proven case ultimately manufactures the exhaustion from a representation; without one, there is no known source of plurisubharmonic functions on $\widetilde{X}$.
2. **Failure of residual finiteness.** Toledo's 1993 examples kill the naive strategy "approximate $\widetilde{X}$ by finite covers, then take a limit of pullbacks of ample line bundles". The intersection of finite-index subgroups can be infinite and invisible.
3. **Accumulation of compact subvarieties.** Holomorphic convexity fails exactly when a family of compact curves in $\widetilde{X}$ accumulates on a non-compact set. Controlling this requires uniform bounds on volumes of lifted subvarieties; no general such bound exists, since $\pi_1$ can act with wild orbit geometry.
4. **$L^2$ methods degenerate.** Gromov's $\bar\partial$-technique produces many $L^2$ holomorphic sections only when $\widetilde{X}$ carries a Kähler *hyperbolic* metric; for general $X$ the $L^2$-index can vanish, giving no functions to build a hull with.
5. **Harmonic map targets.** Corlette–Simpson theory needs a target of nonpositive curvature — a symmetric space or a building. Non-linear groups supply no canonical such target, and CAT(0) cube complexes / $\mathbb{R}$-trees only capture codimension-one data.
6. **The Kähler case is strictly harder.** Even granting the projective conjecture, transferring to compact Kähler $X$ fails because Simpson's correspondence and the algebraicity of Shafarevich reductions use projectivity.

## 6. The Gap

Proven: for every *linear* datum $\rho:\pi_1(X)\to GL_n(\mathbb{C})$, the cover $\widetilde{X}^\rho = \widetilde{X}/\ker\rho$ is holomorphically convex (EKPR). Conjectured: $\widetilde{X}$ itself is holomorphically convex.

The gap is the passage from a tower of quotients to the full universal cover. Write $\Gamma_{\mathrm{lin}} = \bigcap_\rho \ker\rho$, the *linear residue* of $\pi_1(X)$. EKPR gives convexity of $\widetilde{X}/\Gamma_{\mathrm{lin}}$; the missing step is:

> Show that the further covering $\widetilde{X} \to \widetilde{X}/\Gamma_{\mathrm{lin}}$, with deck group $\Gamma_{\mathrm{lin}}$ carrying no linear representations at all, preserves holomorphic convexity.

Two sub-obstructions: (i) an inverse-limit problem — holomorphic convexity is not stable under infinite towers of covers, because hulls can grow without bound; (ii) a group-theoretic one — no classification, or even a single structural theorem, exists for infinite Kähler groups with $\Gamma_{\mathrm{lin}} \ne 1$. Producing one non-trivial plurisubharmonic exhaustion out of purely non-linear $\pi_1$ data is the precise barrier.

## 7. Current Research (as of June 2026)

- **Deng–Yamanoi programme** (CNRS/Nancy and Osaka): reductive Shafarevich conjecture over arbitrary fields, plus hyperbolicity consequences (Green–Griffiths–Lang for varieties with big fundamental group). Uses Nevanlinna theory paired with Katzarkov–Zuo spectral covers. *(frontier — verify)*
- **Eyssidieux school** (Grenoble): non-reductive and mixed Hodge-theoretic extensions; Shafarevich conjecture for covers defined by representations into $\mathbb{Z}_p$-analytic groups.
- **Brunebarbe** (Bordeaux): symmetric differentials, existence of $\Omega^1_X$-based exhaustions, and the link to varieties with big period maps.
- **Bogomolov–Katzarkov–Pantev** (Miami/Penn): search for counterexample candidates among surfaces with irregular non-linear $\pi_1$, and connections to symplectic Lefschetz pencils.
- **Claudon–Höring–Campana** (Nancy/Nice): Shafarevich reductions in the singular and orbifold categories, the Kähler case, and stability under $\mathrm{MRC}$-fibrations.
- **Kähler groups and cube complexes** (Delzant, Py): actions of Kähler groups on CAT(0) cube complexes and hyperbolic spaces — a route to plurisubharmonicity that does not pass through $GL_n$.

## 8. Future Work

- Prove convexity of $\widetilde{X}$ under the sole hypothesis that $\pi_1(X)$ is residually finite (open even so; residual finiteness alone is not known to suffice).
- Establish stability of holomorphic convexity in towers: find conditions on a tower $\widetilde{X}\to \cdots \to X_2 \to X_1 \to X$ ensuring the limit is convex.
- Settle the compact Kähler analogue, using Demailly-type regularisation of closed positive currents to replace ampleness.
- Attack the surface case unconditionally: classify possible $\Gamma_{\mathrm{lin}}$ for projective surfaces, exploiting the Bogomolov–Miyaoka–Yau inequality and Albanese/Iitaka fibrations.
- Build the exhaustion from harmonic maps to general CAT(0) or Gromov-hyperbolic targets rather than symmetric spaces (Delzant–Gromov, Py).
- Develop a positive-characteristic / $p$-adic analogue with Berkovich analytifications, where hulls are combinatorial and possibly computable.

## 9. Key References

- **[Foundational]** I. R. Shafarevich. *Basic Algebraic Geometry.* Springer, 1974 (Russian original: Nauka, 1972). — the original question.
- **[Foundational]** J. Kollár. *Shafarevich maps and plurigenera of algebraic varieties.* Inventiones Mathematicae 113 (1993), 177–215. [DOI](https://doi.org/10.1007/bf01244307)
- **[Foundational]** J. Kollár. *Shafarevich Maps and Automorphic Forms.* Princeton University Press, 1995.
- **[Foundational]** F. Campana. *Remarques sur le revêtement universel des variétés kählériennes compactes.* Bulletin de la Société Mathématique de France 122 (1994), 255–284. [DOI](https://doi.org/10.24033/bsmf.2232)
- **[Foundational]** T. Napier. *Convexity properties of coverings of smooth projective varieties.* Mathematische Annalen 286 (1990), 433–479. [DOI](https://doi.org/10.1007/bf01453583)
- **[SOTA]** P. Eyssidieux, L. Katzarkov, T. Pantev, M. Ramachandran. *Linear Shafarevich conjecture.* Annals of Mathematics 176 (2012), 1545–1581. [DOI](https://doi.org/10.4007/annals.2012.176.3.4)
- **[SOTA]** P. Eyssidieux. *Sur la convexité holomorphe des revêtements linéaires réductifs d'une variété projective algébrique complexe.* Inventiones Mathematicae 156 (2004), 503–564. [DOI](https://doi.org/10.1007/s00222-003-0345-0)
- **[SOTA]** L. Katzarkov, M. Ramachandran. *On the universal coverings of algebraic surfaces.* Annales Scientifiques de l'École Normale Supérieure 31 (1998), 525–535. [DOI](https://doi.org/10.1016/s0012-9593(98)80105-5)
- **[SOTA / Recent]** Y. Deng, K. Yamanoi. *Reductive Shafarevich conjecture.* arXiv:2306.03070, 2023.
- **[Context]** D. Toledo. *Projective varieties with non-residually finite fundamental group.* Publications Mathématiques de l'IHÉS 77 (1993), 103–119. [DOI](https://doi.org/10.1007/bf02699189)
- **[Context]** T. Napier, M. Ramachandran. *Structure theorems for complete Kähler manifolds and applications to Lefschetz type theorems.* Geometric and Functional Analysis 5 (1995), 809–851. [DOI](https://doi.org/10.1007/bf01897052)
- **[Survey]** J. Amorós, M. Burger, K. Corlette, D. Kotschick, D. Toledo. *Fundamental Groups of Compact Kähler Manifolds.* AMS Mathematical Surveys and Monographs 44, 1996.
- **[Survey]** C. Simpson. *Higgs bundles and local systems.* Publications Mathématiques de l'IHÉS 75 (1992), 5–95. [DOI](https://doi.org/10.1007/bf02699491)

## 10. Worked Example / Concrete Special Case

**Setting.** Let $C$ be a smooth projective curve of genus $g \ge 2$, $E$ a rank-2 vector bundle on $C$, and $X = \mathbb{P}(E) \to C$ the associated ruled surface. Then $\dim_{\mathbb{C}} X = 2$ and $X$ has a $\mathbb{P}^1$-fibration $p:X\to C$.

**Step 1: fundamental group.** The homotopy exact sequence of the fibration gives
$$\pi_1(\mathbb{P}^1)=1 \to \pi_1(X) \xrightarrow{\;p_*\;} \pi_1(C) \to \pi_0(\mathbb{P}^1)=1,$$
so $p_*$ is an isomorphism: $\pi_1(X)\cong \pi_1(C) = \Gamma_g$, the surface group with presentation $\langle a_1,b_1,\dots,a_g,b_g \mid \prod [a_i,b_i]=1\rangle$.

**Step 2: the universal cover.** Since $\pi_1$ of the fibre is trivial, $\widetilde{X} = X\times_C \widetilde{C}$. By uniformisation $\widetilde{C}=\mathbb{D}$, the unit disc, so
$$\widetilde{X} \;\cong\; \mathbb{P}(\tilde p^*E) \longrightarrow \mathbb{D},$$
a $\mathbb{P}^1$-bundle over $\mathbb{D}$. As $\mathbb{D}$ is Stein and contractible, every holomorphic vector bundle on it is trivial (Grauert), hence $\widetilde{X}\cong \mathbb{P}^1\times\mathbb{D}$.

**Step 3: verify holomorphic convexity by hand.** Let $\pi:\mathbb{P}^1\times\mathbb{D}\to\mathbb{D}$ be the projection and put
$$\varphi(z,w) \;=\; -\log\big(1-|w|^2\big), \qquad (z,w)\in \mathbb{P}^1\times\mathbb{D}.$$
Then $\varphi = \pi^*\varphi_0$ with $\varphi_0$ a strictly plurisubharmonic exhaustion of $\mathbb{D}$; indeed
$$i\partial\bar\partial \varphi_0 \;=\; \frac{i\,dw\wedge d\bar w}{(1-|w|^2)^2} \;>\; 0 ,$$
the Poincaré metric. So $\varphi$ is plurisubharmonic, and its sublevel sets $\{\varphi < c\} = \mathbb{P}^1\times \{|w|^2 < 1-e^{-c}\}$ are relatively compact — $\varphi$ is a proper plurisubharmonic exhaustion. Hence $\widetilde{X}$ is holomorphically convex. ∎

**Step 4: read off the Shafarevich variety.** Every holomorphic $f\in\mathcal{O}(\mathbb{P}^1\times\mathbb{D})$ is constant on the compact fibres $\mathbb{P}^1\times\{w\}$ (maximum principle on $\mathbb{P}^1$), so $\mathcal{O}(\widetilde{X}) = \pi^*\mathcal{O}(\mathbb{D})$. The Remmert reduction is exactly $\pi$, and
$$\mathrm{Sh}(X) \;=\; \mathbb{D}, \qquad \mathrm{sh}_X = \pi .$$
This matches Kollár's characterisation: the compact curves contracted are the fibres $\mathbb{P}^1$, whose image $\pi_1(\mathbb{P}^1)\to\pi_1(X)$ is trivial (finite), while a multisection maps onto a finite-index subgroup of $\Gamma_g$, hence is not contracted. Note $\widetilde{X}$ is *not* Stein — it contains compact curves — which is why the conjecture asks for convexity, not Steinness.

**Step 5: what breaks in general.** Here the exhaustion came for free from the map $\pi_1(X)\to \Gamma_g \subset PSL_2(\mathbb{R})$, a faithful *linear* representation; this is the EKPR mechanism in miniature. Replace $\pi_1(X)$ by a hypothetical Kähler group with $\Gamma_{\mathrm{lin}}\ne 1$ and there is no map to a nonpositively curved target to pull $\varphi_0$ back from — Step 3 has no substitute. That absence is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*