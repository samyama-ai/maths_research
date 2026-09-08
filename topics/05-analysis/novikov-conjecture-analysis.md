---
id: 05-analysis/novikov-conjecture-analysis
title: "Novikov Conjecture Analysis"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Novikov Conjecture Analysis

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/novikov-conjecture-analysis` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\Gamma$ be a discrete group, $B\Gamma$ its classifying space, $M$ a closed oriented smooth manifold, and $f\colon M \to B\Gamma$ a continuous map. For a class $x \in H^*(B\Gamma;\mathbb{Q})$ define the **higher signature**
$$\operatorname{sign}_x(M,f) \;=\; \big\langle\, L(M)\cup f^*x,\ [M] \,\big\rangle \in \mathbb{Q},$$
where $L(M)$ is the Hirzebruch $L$-class and $[M]$ the fundamental class.

**Novikov Conjecture.** Every higher signature is an oriented homotopy invariant: if $h\colon M' \to M$ is an orientation-preserving homotopy equivalence of closed oriented manifolds, then
$$\operatorname{sign}_x(M', f\circ h) \;=\; \operatorname{sign}_x(M,f)\qquad \text{for all } x \in H^*(B\Gamma;\mathbb{Q}).$$

The conjecture is asserted for **all** discrete groups $\Gamma$. A proof must handle arbitrary (in particular non-finitely-presented, non-exact, and Kazhdan-property-(T)) groups; a disproof requires a single $\Gamma$, a class $x$, and a homotopy equivalence violating the identity. The case $x = 1 \in H^0$ is the Hirzebruch signature theorem and is classical; the content lies in $\deg x > 0$.

The analytic reformulation, which is how the problem is attacked, is **rational injectivity of the Baum–Connes assembly map**
$$\mu\colon K_*^{\Gamma}(\underline{E}\Gamma) \otimes \mathbb{Q} \;\longrightarrow\; K_*(C^*_r\Gamma)\otimes\mathbb{Q},$$
equivalently rational injectivity of the $L$-theoretic assembly $H_*(B\Gamma;\mathbb{L}(\mathbb{Z}))\otimes\mathbb{Q}\to L_*(\mathbb{Z}\Gamma)\otimes\mathbb{Q}$. Either injectivity statement implies the Novikov conjecture for $\Gamma$; surjectivity is *not* needed.

## 2. Mathematical Foundations

**Signature operator.** On a closed oriented Riemannian $4k$-manifold, $D_{\mathrm{sign}} = d + d^*$ acting between the $\pm 1$ eigenbundles of the Hodge involution $\tau$ satisfies $\operatorname{ind} D_{\mathrm{sign}} = \operatorname{sign}(M) = \langle L(M),[M]\rangle$.

**Mishchenko–Fomenko index.** Let $\mathcal{L} = \widetilde{M}\times_\Gamma C^*_r\Gamma$ be the flat bundle of rank-one free $C^*_r\Gamma$-modules associated to $f$. Twisting gives an operator elliptic over the $C^*$-algebra $A = C^*_r\Gamma$ with index
$$\operatorname{Ind}_{\Gamma}(D_{\mathrm{sign}}\otimes\mathcal{L}) \in K_*(C^*_r\Gamma),$$
the **higher signature class** $\sigma(M,f)$. It is an oriented homotopy invariant by Mishchenko's algebraic surgery argument (1974). The Novikov conjecture follows if one can *detect* $\sigma(M,f)$ cohomologically: the Chern-character-type identity
$$\langle \tau_c,\ \sigma(M,f)\rangle \;=\; c\cdot \operatorname{sign}_x(M,f)$$
for a trace/cyclic cocycle $\tau_c$ on a dense subalgebra $\mathcal{A}\subset C^*_r\Gamma$ pairing with $x$, with $c\neq 0$, converts homotopy invariance of the $K$-theory class into homotopy invariance of the number.

**Cyclic cohomology.** Connes–Moscovici use the pairing $HC^{2n}(\mathcal{A}) \times K_0(\mathcal{A}) \to \mathbb{C}$ and a map $H^*(\Gamma;\mathbb{C}) \to HC^*(\mathbb{C}\Gamma)$, $x\mapsto \tau_x$. The obstruction is extending $\tau_x$ continuously to a Banach or smooth subalgebra $\mathcal{A}$ closed under holomorphic functional calculus, so that $K_*(\mathcal{A})\cong K_*(C^*_r\Gamma)$.

**Assembly and descent.** Kasparov's equivariant $KK$-theory supplies a descent map $j^\Gamma\colon KK^\Gamma(A,B)\to KK(A\rtimes_r\Gamma, B\rtimes_r\Gamma)$. A **$\gamma$-element** $\gamma \in KK^\Gamma(\mathbb{C},\mathbb{C})$ with a Dirac–dual-Dirac factorization
$$\gamma = \alpha \otimes_{\mathcal{A}} \beta, \qquad \alpha\in KK^\Gamma(\mathcal{A},\mathbb{C}),\ \beta\in KK^\Gamma(\mathbb{C},\mathcal{A}),$$
$\mathcal{A}$ proper, yields a left inverse to $\mu$ after descent and hence injectivity.

**Coarse geometry.** A metric space $X$ **coarsely embeds** into a Hilbert space $H$ if there is $\phi\colon X\to H$ and nondecreasing $\rho_\pm\colon[0,\infty)\to[0,\infty)$ with $\rho_\pm(t)\to\infty$ and
$$\rho_-(d(x,y)) \le \|\phi(x)-\phi(y)\| \le \rho_+(d(x,y)).$$
**Asymptotic dimension** $\operatorname{asdim} X \le n$ if every uniformly bounded cover refines to one with multiplicity $\le n+1$ and arbitrarily large Lebesgue number. For finitely generated $\Gamma$ with word metric both are quasi-isometry invariants, and finite $\operatorname{asdim}$ implies coarse embeddability.

## 3. History & State of the Art (SOTA)

- **1965.** Novikov proves topological invariance of rational Pontryagin classes (Doklady), using a transversality/signature argument that already contains the $\Gamma=\mathbb{Z}^k$ case.
- **1970.** Novikov formulates the higher-signature conjecture in his Hermitian $K$-theory papers.
- **1972.** Lusztig proves the $\Gamma = \mathbb{Z}^n$ case analytically, via a family of signature operators twisted by flat line bundles parametrized by the dual torus $\widehat{\mathbb{T}}^n$ — the first genuinely analytic proof.
- **1974.** Mishchenko introduces infinite-dimensional Fredholm representations and $C^*$-algebraic surgery; proves the conjecture for fundamental groups of closed nonpositively curved manifolds.
- **1981.** Farrell–Hsiang: topological/surgery proof for nonpositively curved manifolds.
- **1988.** Kasparov's $KK$-theoretic proof for closed subgroups of connected Lie groups and discrete subgroups thereof — the Dirac/dual-Dirac method becomes the standard machine.
- **1990–1993.** Connes–Moscovici (hyperbolic groups, via cyclic cohomology and Haagerup-type estimates); Connes–Gromov–Moscovici (groups with Lipschitz-controlled cohomology classes).
- **1998–2001.** Yu's two theorems (finite asymptotic dimension; coarse embeddability) plus Higson–Kasparov (a-T-menable groups) massively enlarge the class.
- **2002.** Higson–Lafforgue–Skandalis produce counterexamples to Baum–Connes *with coefficients* and to the coarse Baum–Connes conjecture, from Gromov's monster groups containing expanders. The Novikov conjecture itself survives.
- **Present.** No group is known to violate Novikov. The conjecture is regarded as plausibly true but with no unified proof technique.

## 4. Partial Results / Verified Cases

Novikov's conjecture is a **theorem** for:

| Class of $\Gamma$ | Author(s), year |
|---|---|
| $\mathbb{Z}^n$, all $n$; finitely generated abelian | Lusztig 1972; Novikov 1965 |
| $\pi_1$ of closed nonpositively curved manifolds | Mishchenko 1974; Farrell–Hsiang 1981 |
| Discrete subgroups of connected Lie groups; $\pi_1$ of complete nonpositively curved manifolds | Kasparov 1988 |
| Word-hyperbolic groups (Gromov) | Connes–Moscovici 1990 |
| Groups with finite asymptotic dimension ($\operatorname{asdim}\Gamma<\infty$) | Yu 1998 |
| Groups coarsely embeddable into Hilbert space (includes all exact / amenable-at-infinity groups) | Yu 2000 |
| a-T-menable (Haagerup) groups: amenable, free, $\mathrm{SO}(n,1)$, $\mathrm{SU}(n,1)$ lattices, Coxeter groups — full Baum–Connes | Higson–Kasparov 2001 |
| Groups acting properly on bolic spaces, affine buildings, cocompact CAT(0) cube complexes | Kasparov–Skandalis 2003 |
| Linear groups over any field (any subgroup of $\mathrm{GL}_n(K)$) | Guentner–Higson–Weinberger 2005 |
| Groups with property (RD) plus Banach-$KK$ input; many higher-rank lattices | Lafforgue 2002 |
| Mapping class groups $\mathrm{Mod}(S)$ (boundary amenable, and $\operatorname{asdim}<\infty$) | Kida 2008; Hamenstädt 2009; Bestvina–Bromberg–Fujiwara 2015 |
| $\mathrm{Out}(F_n)$ (boundary amenability $\Rightarrow$ exactness $\Rightarrow$ coarse embeddability) | Bestvina–Guirardel–Horbez 2017 |
| Hyperbolic and CAT(0) groups: full Farrell–Jones, hence Borel in dim $\ge 5$ | Bartels–Lück 2012 |

Quantitatively: for $\operatorname{asdim}\Gamma = n < \infty$ Yu's proof is uniform in $n$ but the controlled-$K$-theory constants degrade with $n$; no dimension restriction on $M$ is needed in any of the above, though surgery-theoretic corollaries (Borel) require $\dim M \ge 5$.

## 5. Principal Obstacles

- **Property (T) kills homotopies.** For $\Gamma$ with Kazhdan's property (T) the trivial representation is isolated, producing an idempotent $p\in C^*\Gamma$ whose class obstructs the standard homotopy $\gamma = 1$ in $KK^\Gamma(\mathbb{C},\mathbb{C})$. Higson–Kasparov's Hilbert-space method requires *proper* affine actions, which (T) forbids outright.
- **Expanders defeat coarse geometry.** A sequence of expander graphs cannot be coarsely embedded into Hilbert space (Gromov). Gromov's monster groups contain expanders in their Cayley graphs, so Yu's 2000 hypothesis fails; Higson–Lafforgue–Skandalis show this failure is not merely technical — the coarse assembly map is genuinely non-injective in the associated coefficient setting.
- **Cyclic-cocycle extension.** Connes–Moscovici need $\tau_x$ to extend to a smooth subalgebra $\mathcal{A}\subset C^*_r\Gamma$ stable under holomorphic functional calculus. This requires polynomial cohomology / rapid-decay estimates that are unavailable for general $\Gamma$; higher-rank lattices such as $\mathrm{SL}_3(\mathbb{Z})$ resisted precisely here until Lafforgue's Banach $KK$-theory.
- **No Banach substitute in general.** Lafforgue's approach replaces Hilbert modules with Banach ones to evade (T), but is blocked by his own **strong property (T)** (Duke, 2008), enjoyed by $\mathrm{Sp}(n,1)$ and higher-rank $p$-adic groups, which obstructs Banach-space Dirac–dual-Dirac.
- **Non-finitely-presented groups.** Every geometric technique presumes a Cayley graph or a $\Gamma$-CW model for $\underline{E}\Gamma$ of finite type. Arbitrary countable groups have neither, and no purely algebraic route to rational injectivity of assembly is known.

## 6. The Gap

Proven: rational injectivity of $\mu$ for groups admitting some **large-scale geometric hypothesis** — coarse embeddability, finite asymptotic dimension, properness of an action on a bolic/CAT(0)/Hilbert target, or a controlled cohomology theory. Every known proof factors through a *geometric compression* of $\Gamma$ into a space where an index-theoretic Bott element exists.

The general statement quantifies over **all** countable groups. The exact barrier: produce, for an arbitrary $\Gamma$, either

1. a $\gamma$-element with Dirac/dual-Dirac factorization through a proper $\Gamma$-algebra (blocked by (T) and strong (T)), or
2. a functorial retraction of $\mu\otimes\mathbb{Q}$ not requiring any embedding hypothesis, or
3. a homotopy-invariant characteristic-class argument bypassing $C^*$-algebras entirely.

Concretely: no technique currently applies to a Gromov monster group $\Gamma_{\mathrm{mon}}$ containing an expander *and* having property (T). Whether the Novikov conjecture holds for such $\Gamma$ is the sharpest open instance.

## 7. Current Research (as of June 2026)

- **Controlled/quantitative $K$-theory.** Oyono-Oyono–Yu's quantitative $K$-theory localizes assembly at finite scales, aiming to prove rational injectivity from *sequences* of partial embeddings rather than a global one. Extensions to groups of "finite decomposition complexity" (Guentner–Tessera–Yu) continue.
- **Warped cones and expanders.** Ongoing work relates coarse non-embeddability of warped cones over (T) actions to failures of coarse Baum–Connes, sharpening exactly which parts of the machinery break *(frontier — verify)*.
- **Farrell–Jones program.** Bartels–Lück–Reich-style flow-space methods now cover mapping class groups, $\mathrm{GL}_n(\mathbb{Z})$, and normally poly-free groups; each new case yields Novikov as a corollary. Groups: Münster (Bartels, Lück), Bonn, Vanderbilt (Yu), Texas A&M, IMJ-PRG (Skandalis, Lafforgue).
- **Higher index theory for non-cocompact and singular settings** — Roe algebras on manifolds with boundary, index theory on stratified spaces (Albin, Piazza, Zenobi) — extending higher signatures beyond closed manifolds.
- **Coarse median / hierarchically hyperbolic groups.** Finite asymptotic dimension for HHGs (Behrstock–Hagen–Sisto) puts new classes into Yu's 1998 theorem *(frontier — verify for the full HHG class)*.

## 8. Future Work

- Decide Novikov for Gromov monster groups; Gromov's construction is probabilistic and existing groups are only known to *exist*, so making one explicit enough to compute with is a stated goal.
- Develop a $KK$-theory over Banach spaces or over $L^p$-spaces evading strong property (T) — Lafforgue's own suggested route.
- Prove the "$\mathbb{Q}$-only" version directly: find a rational splitting of assembly using homological algebra of $\mathbb{Z}\Gamma$ rather than analysis.
- Extend controlled $K$-theory to give injectivity from a hypothesis strictly weaker than coarse embeddability, e.g. embeddability into $\ell^p$ or into a Banach space with nontrivial type.
- Push higher-signature index theory to non-compact, foliated, and stratified settings where the homotopy-invariance mechanism may be more flexible.

## 9. Key References

- **[Foundational]** S. P. Novikov. *Topological invariance of rational Pontrjagin classes.* Doklady Akad. Nauk SSSR 163 (1965), 298–300.
- **[Foundational]** A. S. Mishchenko. *Infinite-dimensional representations of discrete groups and higher signatures.* Izv. Akad. Nauk SSSR Ser. Mat. 38 (1974), 81–106. [DOI](https://doi.org/10.1070/im1974v008n01abeh002097)
- **[Foundational]** G. Lusztig. *Novikov's higher signature and families of elliptic operators.* J. Differential Geometry 7 (1972), 229–256. [DOI](https://doi.org/10.4310/jdg/1214430829)
- **[Foundational]** G. G. Kasparov. *Equivariant KK-theory and the Novikov conjecture.* Inventiones Mathematicae 91 (1988), 147–201.
- **[Foundational]** A. Connes, H. Moscovici. *Cyclic cohomology, the Novikov conjecture and hyperbolic groups.* Topology 29 (1990), 345–388. [DOI](https://doi.org/10.1016/0040-9383(90)90003-3)
- **[Foundational]** F. T. Farrell, W. C. Hsiang. *On Novikov's conjecture for nonpositively curved manifolds, I.* Annals of Mathematics 113 (1981), 199–209.
- **[SOTA]** G. Yu. *The Novikov conjecture for groups with finite asymptotic dimension.* Annals of Mathematics 147 (1998), 325–355. [DOI](https://doi.org/10.2307/121011)
- **[SOTA]** G. Yu. *The coarse Baum–Connes conjecture for spaces which admit a uniform embedding into Hilbert space.* Inventiones Mathematicae 139 (2000), 201–240. [DOI](https://doi.org/10.1007/s002229900032)
- **[SOTA]** N. Higson, G. Kasparov. *E-theory and KK-theory for groups which act properly and isometrically on Hilbert space.* Inventiones Mathematicae 144 (2001), 23–74. [DOI](https://doi.org/10.1007/s002220000118)
- **[SOTA]** G. Kasparov, G. Skandalis. *Groups acting properly on "bolic" spaces and the Novikov conjecture.* Annals of Mathematics 158 (2003), 165–206. [DOI](https://doi.org/10.4007/annals.2003.158.165)
- **[SOTA]** V. Lafforgue. *K-théorie bivariante pour les algèbres de Banach et conjecture de Baum–Connes.* Inventiones Mathematicae 149 (2002), 1–95. [DOI](https://doi.org/10.1007/s002220200213)
- **[SOTA]** E. Guentner, N. Higson, S. Weinberger. *The Novikov conjecture for linear groups.* Publications Mathématiques de l'IHÉS 101 (2005), 243–268. [DOI](https://doi.org/10.1007/s10240-005-0030-5)
- **[SOTA]** A. Bartels, W. Lück. *The Borel conjecture for hyperbolic and CAT(0)-groups.* Annals of Mathematics 175 (2012), 631–689. [DOI](https://doi.org/10.4007/annals.2012.175.2.5)
- **[Counterexamples]** N. Higson, V. Lafforgue, G. Skandalis. *Counterexamples to the Baum–Connes conjecture.* Geometric and Functional Analysis 12 (2002), 330–354. [DOI](https://doi.org/10.1007/s00039-002-8249-5)
- **[Counterexamples]** M. Gromov. *Random walk in random groups.* Geometric and Functional Analysis 13 (2003), 73–146.
- **[Survey]** S. Ferry, A. Ranicki, J. Rosenberg (eds.). *Novikov Conjectures, Index Theorems and Rigidity*, Vols. 1–2. LMS Lecture Note Series 226–227, Cambridge University Press, 1995.
- **[Survey]** W. Lück, H. Reich. *The Baum–Connes and the Farrell–Jones conjectures in K- and L-theory.* In *Handbook of K-theory*, Springer, 2005, 703–842. [DOI](https://doi.org/10.1007/978-3-540-27855-9_15)
- **[Survey]** N. Higson, J. Roe. *Analytic K-Homology.* Oxford University Press, 2000.

## 10. Worked Example / Concrete Special Case

**Take $\Gamma = \mathbb{Z}$, so $B\Gamma = S^1$ and $H^1(S^1;\mathbb{Q}) = \mathbb{Q}\langle x\rangle$.** Let $M^5$ be a closed oriented $5$-manifold with $f\colon M\to S^1$. The only nonzero higher signature in positive degree is
$$\operatorname{sign}_x(M,f) = \langle L_1(M)\cup f^*x,\ [M]\rangle, \qquad L_1 = \tfrac{1}{3}p_1 .$$

*Step 1 — transversality.* Homotope $f$ to be smooth and transverse to a point $p\in S^1$. Then $N := f^{-1}(p)$ is a closed oriented $4$-manifold with trivial normal bundle $\nu \cong N\times\mathbb{R}$, and $[N]$ is Poincaré dual to $f^*x$.

*Step 2 — evaluate.* By the definition of Poincaré duality, $\langle \alpha\cup f^*x,[M]\rangle = \langle \alpha|_N,[N]\rangle$. With $\alpha = L_1(M)$:
$$\operatorname{sign}_x(M,f) = \langle L_1(M)|_N,\ [N]\rangle .$$
Since $TM|_N = TN\oplus\nu$ with $\nu$ trivial, $p_1(M)|_N = p_1(N)$, hence $L_1(M)|_N = L_1(N)$.

*Step 3 — Hirzebruch.* $\langle L_1(N),[N]\rangle = \operatorname{sign}(N)$, the signature of the intersection form on $H^2(N;\mathbb{R})$. So
$$\boxed{\ \operatorname{sign}_x(M,f) = \operatorname{sign}\big(f^{-1}(p)\big).\ }$$

*Step 4 — homotopy invariance.* If $h\colon M'\to M$ is an orientation-preserving homotopy equivalence, make $f\circ h$ transverse to $p$ with preimage $N'$. The restriction $h\colon N'\to N$ is a degree-one normal map, and Novikov's argument (surgery below the middle dimension, using that $\pi_1(S^1)=\mathbb{Z}$ contributes only an infinite cyclic cover) shows $\operatorname{sign}(N')=\operatorname{sign}(N)$. Hence $\operatorname{sign}_x(M',f\circ h)=\operatorname{sign}_x(M,f)$.

*Concrete instance.* Take $M = \mathbb{CP}^2 \times S^1$, $f$ the projection. Then $N = \mathbb{CP}^2$, $\operatorname{sign}(N)=1$, so $\operatorname{sign}_x(M,f)=1$. Any $M'$ homotopy equivalent to $\mathbb{CP}^2\times S^1$ must also return $1$ — a nontrivial constraint, since $p_1$ alone is not a homotopy invariant.

*Analytic mirror.* $C^*_r(\mathbb{Z}) \cong C(S^1)$ by Fourier transform, so $K_0(C^*_r\mathbb{Z}) \cong \mathbb{Z}^2$ and the Mishchenko–Fomenko index is a family of ordinary signature operators twisted by flat line bundles $L_\theta$, $\theta\in S^1$. Lusztig's theorem computes its Chern character and recovers exactly the boxed identity — the $\mathbb{Z}$ case where the geometric and analytic proofs visibly coincide. For general $\Gamma$ no such explicit Fourier picture exists, which is the whole difficulty.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*