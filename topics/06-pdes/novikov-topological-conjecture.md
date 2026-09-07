---
id: 06-pdes/novikov-topological-conjecture
title: "Novikov Topological Conjecture"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Novikov Topological Conjecture

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/novikov-topological-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $M$ be a closed, oriented, smooth manifold with fundamental group $\Gamma = \pi_1(M)$, and let $f\colon M \to B\Gamma$ classify the universal cover. For a cohomology class $x \in H^*(B\Gamma;\mathbb{Q})$, the **higher signature** is

$$\mathrm{sign}_x(M,f) \;=\; \big\langle\, L(M)\smile f^*x,\ [M] \,\big\rangle \in \mathbb{Q},$$

where $L(M)$ is the Hirzebruch $L$-class and $[M]$ the fundamental class.

**Novikov Conjecture.** For every discrete group $\Gamma$ and every $x \in H^*(B\Gamma;\mathbb{Q})$, the higher signature is an oriented homotopy invariant: if $h\colon M' \to M$ is an orientation-preserving homotopy equivalence of closed oriented manifolds, then

$$\mathrm{sign}_x(M', f\circ h) \;=\; \mathrm{sign}_x(M, f).$$

The case $x = 1$ is the Hirzebruch signature theorem, $\mathrm{sign}_1(M) = \mathrm{sign}(M)$, already a homotopy invariant. The content is that the *non-trivial* $L$-class components, which individually are **not** homotopy invariant (rational Pontryagin classes are only topological invariants, by Novikov's own 1965 theorem), become invariant after pairing with pullbacks from $B\Gamma$.

A complete resolution means: a proof valid for all countable discrete $\Gamma$, or a single $\Gamma$, $x$, and homotopy equivalence $h$ with $\mathrm{sign}_x(M',f h) \neq \mathrm{sign}_x(M,f)$.

## 2. Mathematical Foundations

**The signature operator.** On a closed oriented Riemannian $n$-manifold ($n=4k$), let $\tau = i^{p(p-1)+2k}\ast$ be the Hodge involution on $\Omega^p(M)\otimes\mathbb{C}$ and $D = d + d^*$. The signature operator $D^+\colon \Omega^+ \to \Omega^-$ is elliptic with

$$\mathrm{ind}(D^+) \;=\; \int_M L(M) \;=\; \mathrm{sign}(M) \qquad \text{(Atiyah–Singer / Hirzebruch)},$$

where $L(M) = \prod_j \dfrac{\sqrt{y_j}}{\tanh\sqrt{y_j}}$ in Pontryagin roots, $L_1 = \tfrac{1}{3}p_1$, $L_2 = \tfrac{1}{45}(7p_2 - p_1^2)$.

**Mishchenko–Fomenko index.** Let $C^*_r\Gamma$ be the reduced group $C^*$-algebra and $\mathcal{V} = \widetilde{M}\times_\Gamma C^*_r\Gamma$ the canonical flat bundle of finitely generated projective modules. The signature operator twisted by $\mathcal{V}$ has an index in $K_*(C^*_r\Gamma)$,

$$\mathrm{ind}_\Gamma(D_{\mathcal V}) \in K_{n}(C^*_r\Gamma),$$

and Mishchenko–Fomenko (1979) proved this **higher index** is an oriented homotopy invariant of $(M,f)$.

**Assembly.** The Baum–Connes assembly map is

$$\mu\colon K_*^\Gamma(\underline{E}\Gamma) \longrightarrow K_*(C^*_r\Gamma).$$

**Strong Novikov Conjecture (SNC).** $\mu \otimes \mathbb{Q}$ is injective on $K_*(B\Gamma)\otimes\mathbb{Q}$.

**Reduction.** Rationally, $K_*(B\Gamma)\otimes\mathbb{Q}\cong \bigoplus_j H_{*+2j}(B\Gamma;\mathbb{Q})$ (Chern character), and $\mathrm{ch}\,\mu(f_*[D_M]) $ carries exactly the data $\{\mathrm{sign}_x(M,f)\}_x$. Hence

$$\textbf{SNC for }\Gamma \;\Longrightarrow\; \textbf{Novikov for }\Gamma.$$

Equivalently, in surgery-theoretic terms, rational injectivity of the $L$-theory assembly $H_*(B\Gamma;\mathbb{L}(\mathbb{Z}))\otimes\mathbb{Q}\to L_*(\mathbb{Z}\Gamma)\otimes\mathbb{Q}$ implies the conjecture; this is the rational-injectivity part of the Farrell–Jones conjecture.

**PDE content.** The conjecture is a statement about elliptic operators with operator-algebra coefficients: it asks whether the analytic index of the signature operator, computed in a noncommutative receptacle, detects all of $L(M)\smile f^*H^*(B\Gamma;\mathbb{Q})$. Its positive-scalar-curvature analogue for the Dirac operator (Rosenberg 1983) is the reason SNC also obstructs metrics of positive scalar curvature on aspherical manifolds.

## 3. History & State of the Art (SOTA)

- **1965.** Novikov proves topological invariance of rational Pontryagin classes.
- **1966–1970.** Novikov formulates the higher-signature conjecture, proving it for $\Gamma = \mathbb{Z}^n$ by a splitting/Bass–Heller–Swan argument (Izv. Akad. Nauk SSSR, 1966), and restates it via Hermitian $K$-theory (1970).
- **1972.** Lusztig gives the first *analytic* proof for $\Gamma=\mathbb{Z}^n$: the family of signature operators twisted by flat line bundles over the character torus $\widehat{\mathbb{Z}^n}=T^n$, with the Atiyah–Singer families index theorem.
- **1974.** Mishchenko: nonpositively curved case, via infinite-dimensional Fredholm representations.
- **1979.** Mishchenko–Fomenko: index theory over $C^*$-algebras — the machine that converts SNC into Novikov.
- **1988.** Kasparov: equivariant $KK$-theory (the Dirac–dual-Dirac method); Novikov for discrete subgroups of arbitrary connected Lie groups.
- **1990–93.** Connes–Moscovici (hyperbolic groups, via cyclic cohomology and the Gauss–Bonnet/local index formula); Connes–Gromov–Moscovici (classes with Lipschitz control; proper Lipschitz cohomology).
- **1998–2000.** Yu: finite asymptotic dimension, then coarse embeddability into Hilbert space, both implying coarse Baum–Connes and hence Novikov. This is the single largest advance in coverage.
- **2001.** Higson–Kasparov: a-T-menable (Haagerup) groups satisfy full Baum–Connes with coefficients.
- **2002.** Lafforgue: Banach $KK$-theory, Baum–Connes for many hyperbolic and cocompact-lattice cases including some with property (T).
- **2005.** Guentner–Higson–Weinberger: all countable linear groups over any field.
- **2006.** Kasparov–Yu: embeddability into uniformly convex Banach spaces suffices.

No counterexample is known; the conjecture is widely believed. Baum–Connes *with coefficients* is false (Higson–Lafforgue–Skandalis, 2002), which removed the most natural uniform strategy.

## 4. Partial Results / Verified Cases

Proven for:

| Class of $\Gamma$ | Authority |
|---|---|
| $\mathbb{Z}^n$, all $n$ | Novikov 1966; Lusztig 1972 |
| $\pi_1$ of complete nonpositively curved manifolds | Mishchenko 1974; Kasparov 1988 |
| Discrete subgroups of connected Lie groups | Kasparov 1988 |
| Word-hyperbolic groups (Gromov) | Connes–Moscovici 1990 |
| Groups of finite asymptotic dimension $\mathrm{asdim}\,\Gamma < \infty$ | Yu 1998 |
| Groups coarsely embeddable in Hilbert space | Yu 2000 |
| a-T-menable / Haagerup groups (free groups, Coxeter groups, $\mathbb{Z}^n\rtimes$ amenable) | Higson–Kasparov 2001 |
| Countable subgroups of $GL_n(K)$, any field $K$ | Guentner–Higson–Weinberger 2005 |
| Groups embeddable in uniformly convex Banach spaces | Kasparov–Yu 2006 |
| Mapping class groups $\mathrm{Mod}(S_g)$ | Hamenstädt 2009 (boundary amenability); Bestvina–Bromberg–Fujiwara 2015 ($\mathrm{asdim}<\infty$) |
| $\mathrm{Out}(F_N)$, all $N$ | Bestvina–Guirardel–Horbez 2021 |
| Amenable groups, elementary amenable, all $\mathrm{asdim}$-finite solvable | via Yu 1998/2000 |

Also: unconditional homotopy invariance of higher signatures in codimension-one splitting situations (Cappell 1976, for $\Gamma$ a free product with amalgamation or HNN extension over a square-root-closed subgroup), and for $x \in H^1(B\Gamma;\mathbb{Q})$ and $H^2$ for all $\Gamma$ (Connes–Gromov–Moscovici; the degree-$\le 2$ case is known in full generality).

## 5. Principal Obstacles

- **Property (T) blocks Dirac–dual-Dirac.** Higson–Kasparov requires a proper affine isometric action on Hilbert space. Groups with Kazhdan's property (T) have none; worse, $\gamma$-element arguments in $KK$ break because the Kazhdan projection makes the unit and the $\gamma$-element differ in $K_*(C^*_r\Gamma)$. Lafforgue's Banach $KK$ recovers some, but *strong property (T)* (Lafforgue) obstructs even Banach-space deformation for higher-rank lattices such as $SL_3(\mathbb{Z}_p)$-lattices.
- **Expanders obstruct coarse geometry.** Gromov's random groups (GAFA 2003, rigorously realised by Osajda, Acta Math. 2020) contain coarsely embedded expander sequences and therefore admit **no** coarse embedding into Hilbert space. Yu's theorem does not apply; the coarse Baum–Connes assembly map is not injective for such expanders (Higson–Lafforgue–Skandalis).
- **No local formula.** The higher index lives in $K_*(C^*_r\Gamma)$, a group with no computable local (heat-kernel) expression in general; Connes–Moscovici's cyclic-cohomology route needs the cocycle to extend to a dense smooth subalgebra with a bounded-cohomology-type estimate, which fails for high-degree classes on groups of exponential growth.
- **Degree barrier.** Techniques controlling $x$ of degree $\le 2$ (bounded cohomology, almost-flat bundles) have no known analogue in higher degree, because "almost flat" vector bundles of the needed curvature decay do not exist on general $B\Gamma$.
- **Surgery side.** The $L$-theoretic assembly map is not computable without a geometric model of $\underline{E}\Gamma$ with controlled dimension; groups of infinite asymptotic dimension supply none.

## 6. The Gap

Every proof to date factors through a **geometric largeness hypothesis** on $\Gamma$: coarse embeddability into a Hilbert or uniformly convex Banach space, finite asymptotic dimension, or an action on a bolic/CAT(0)/Hilbertian space producing a $\gamma$-element. The gap is exactly the class of groups admitting none of these — Gromov monster groups and higher-rank lattices with strong property (T).

Precisely: no known argument produces homotopy invariance of $\mathrm{sign}_x$ for $\deg x \ge 3$ without first constructing a Dirac–dual-Dirac pair or a coarse embedding. What must be crossed is either (a) a proof of rational injectivity of $\mu$ that is *insensitive* to expanders, or (b) a genuinely non-$KK$-theoretic mechanism (controlled topology, $\ell^1$- or bounded-cohomology, or Farrell–Jones-style flow-space methods) that reaches groups with no coarse embedding.

## 7. Current Research (as of June 2026)

- **Coarse geometry beyond Hilbert space.** Willett–Yu's programme on higher index theory and the maximal coarse Baum–Connes conjecture; expanders with large girth satisfy the *maximal* version even when the reduced one fails. Extending to Osajda-type monsters remains the target *(frontier — verify)*.
- **Farrell–Jones methods.** Bartels–Lück–Reich-style flow spaces have proved Farrell–Jones (hence Novikov) for hyperbolic and CAT(0)-cocompact groups, $GL_n(\mathbb{Z})$, and lattices in virtually connected Lie groups (Bartels–Lück–Reich–Rüping). Current work pushes to mapping class groups and $\mathrm{Out}(F_N)$ *(frontier — verify)*.
- **Secondary invariants.** Weinberger–Yu and Weinberger–Xie–Yu use the finite part of $K_*(C^*_r\Gamma)$ and $\rho$-invariants to derive lower bounds on structure sets, giving Novikov-adjacent rigidity for groups with torsion.
- **Groups acting on finite-dimensional CAT(0) cube complexes and hierarchically hyperbolic groups**, where finite asymptotic dimension is being established case by case (Behrstock–Hagen–Sisto and successors).
- **Institutions:** Texas A&M (Yu, Guo), Münster (Bartels, Lück's school), Vanderbilt, IHÉS, Fudan, Warsaw (Osajda), Copenhagen.

## 8. Future Work

- Decide Novikov for a fixed Gromov monster group; a positive answer would show expanders are not a genuine obstruction, a negative one would be the first counterexample.
- Develop index theory in $\ell^p$ or general Banach algebras where the Kazhdan projection is absent, as advocated by Lafforgue and pursued in the $\ell^p$ Roe algebra literature.
- Prove rational injectivity of the $L$-theoretic assembly directly by controlled topology, avoiding $C^*$-algebras entirely (Ferry–Weinberger programme).
- Establish the "degree $\le 3$" case of Novikov for all groups, the first genuinely open degree.
- Clarify the relation to the Gromov–Lawson–Rosenberg conjecture, false in general (Schick 1998) but whose stable form for aspherical manifolds remains tied to SNC.

## 9. Key References

- **[Foundational]** S. P. Novikov. *On manifolds with free abelian fundamental group and their application.* Izv. Akad. Nauk SSSR Ser. Mat. **30** (1966), 207–246.
- **[Foundational]** G. Lusztig. *Novikov's higher signature and families of elliptic operators.* J. Differential Geometry **7** (1972), 229–256.
- **[Foundational]** A. S. Mishchenko, A. T. Fomenko. *The index of elliptic operators over $C^*$-algebras.* Izv. Akad. Nauk SSSR Ser. Mat. **43** (1979), 831–859.
- **[Foundational]** G. G. Kasparov. *Equivariant $KK$-theory and the Novikov conjecture.* Invent. Math. **91** (1988), 147–201.
- **[Foundational]** A. Connes, H. Moscovici. *Cyclic cohomology, the Novikov conjecture and hyperbolic groups.* Topology **29** (1990), 345–388.
- **[SOTA]** G. Yu. *The Novikov conjecture for groups with finite asymptotic dimension.* Ann. of Math. **147** (1998), 325–355.
- **[SOTA]** G. Yu. *The coarse Baum–Connes conjecture for spaces which admit a uniform embedding into Hilbert space.* Invent. Math. **139** (2000), 201–240.
- **[SOTA]** N. Higson, G. Kasparov. *E-theory and KK-theory for groups which act properly and isometrically on Hilbert space.* Invent. Math. **144** (2001), 23–74.
- **[SOTA]** E. Guentner, N. Higson, S. Weinberger. *The Novikov conjecture for linear groups.* Publ. Math. IHÉS **101** (2005), 243–268.
- **[SOTA]** G. Kasparov, G. Yu. *The coarse geometric Novikov conjecture and uniform convexity.* Adv. Math. **206** (2006), 1–56.
- **[Obstruction]** N. Higson, V. Lafforgue, G. Skandalis. *Counterexamples to the Baum–Connes conjecture.* Geom. Funct. Anal. **12** (2002), 330–354.
- **[Obstruction]** D. Osajda. *Small cancellation labellings of some infinite graphs and applications.* Acta Math. **225** (2020), 159–191.
- **[Recent]** M. Bestvina, V. Guirardel, C. Horbez. *Boundary amenability of $\mathrm{Out}(F_N)$.* Ann. Sci. Éc. Norm. Supér. **54** (2021).
- **[Survey]** S. Ferry, A. Ranicki, J. Rosenberg (eds.). *Novikov Conjectures, Index Theorems and Rigidity*, Vols. 1–2. LMS Lecture Note Series 226–227, Cambridge University Press, 1995.
- **[Survey]** R. Willett, G. Yu. *Higher Index Theory.* Cambridge Studies in Advanced Mathematics 189, Cambridge University Press, 2020.

## 10. Worked Example / Concrete Special Case

**Case $\Gamma = \mathbb{Z}$, $B\Gamma = S^1$, $x = [d\theta] \in H^1(S^1;\mathbb{Q})$.**

Take $M^5 = \mathbb{CP}^2 \times S^1$ with $f\colon M \to S^1$ the projection.

*Compute the higher signature.* $T\mathbb{CP}^2 \oplus \mathbb{C} \cong 3H$ gives total Pontryagin class $p(\mathbb{CP}^2) = (1+h^2)^3 = 1 + 3h^2$, so $p_1 = 3h^2$ and

$$L_1(\mathbb{CP}^2) = \tfrac{1}{3}p_1 = h^2, \qquad \langle h^2, [\mathbb{CP}^2]\rangle = 1.$$

Since $L(M) = L(\mathbb{CP}^2)\times 1$ and $f^*x$ generates $H^1(M;\mathbb{Q})$,

$$\mathrm{sign}_x(M,f) = \big\langle L_1(\mathbb{CP}^2)\smile f^*x,\ [\mathbb{CP}^2\times S^1]\big\rangle = 1.$$

Note $\mathrm{sign}(\mathbb{CP}^2) = 1$, consistent.

*Why it is homotopy invariant.* Make $f$ transverse to a point $p \in S^1$ and set $N = f^{-1}(p)$, a closed oriented $4$-manifold with trivial normal bundle. Poincaré duality gives $f^*x \frown [M] = [N]$, and triviality of the normal bundle gives $L(M)|_N = L(N)$. Hence

$$\mathrm{sign}_x(M,f) = \langle L(N),[N]\rangle = \mathrm{sign}(N).$$

Here $N = \mathbb{CP}^2$ and $\mathrm{sign}(N)=1$.

*Analytic proof (Lusztig's argument).* For $\theta \in S^1 = \widehat{\mathbb{Z}}$ let $\mathcal{L}_\theta \to M$ be the flat line bundle with holonomy $e^{2\pi i\theta}$ along the $S^1$ factor. The signature operators $D_{\mathcal L_\theta}$ form a family over $\widehat{\mathbb{Z}}$; the Atiyah–Singer families index theorem gives

$$\mathrm{ch}\big(\mathrm{ind}\,D_{\mathcal L}\big) = \int_M L(M)\smile \mathrm{ch}(\mathcal L),$$

whose degree-one component over $\widehat{\mathbb{Z}}$ is precisely $\mathrm{sign}_x(M,f)$. Because the family index lives in $K^0(\widehat{\mathbb{Z}}) \cong K_1(C^*_r\mathbb{Z})$ and equals the Mishchenko–Fomenko higher index, it is unchanged under homotopy equivalence. So any $M'$ homotopy equivalent to $\mathbb{CP}^2\times S^1$ has $\mathrm{sign}_x(M',fh)=1$: every codimension-one submanifold dual to the $H^1$ generator has signature $1$.

Contrast: the individual class $p_1(M)$ is *not* homotopy invariant in general — only the paired quantity is. This is the whole content of the conjecture, and for $\Gamma=\mathbb{Z}$ the character torus $\widehat{\mathbb{Z}}$ is compact and one-dimensional, which is exactly the structure that disappears for nonabelian $\Gamma$ and forces the passage to $K_*(C^*_r\Gamma)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*