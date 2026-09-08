---
id: 03-geometry/geometric-langlands-conjecture
title: "Geometric Langlands Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Geometric Langlands Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/geometric-langlands-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth projective connected curve over an algebraically closed field $k$ of characteristic $0$, let $G$ be a connected reductive group over $k$, and let $\check G$ be its Langlands dual group. The **categorical geometric Langlands conjecture** (de Rham form, Arinkin–Gaitsgory formulation) asserts an equivalence of $k$-linear cocomplete DG categories

$$
\mathbb{L}_G:\ D\text{-mod}(\mathrm{Bun}_G(X)) \ \xrightarrow{\ \sim\ }\ \mathrm{IndCoh}_{\mathcal N}\big(\mathrm{LocSys}_{\check G}(X)\big),
$$

normalized so that it intertwines Hecke functors on the left with tensoring by tautological vector bundles on the right, and sends the Whittaker (Poincaré) object to the structure sheaf. Here $\mathrm{Bun}_G(X)$ is the moduli stack of $G$-bundles, $\mathrm{LocSys}_{\check G}(X)$ the derived stack of $\check G$-local systems (de Rham), and $\mathcal N$ the global nilpotent cone cutting out the allowed singular support.

A complete proof must construct such a functor, prove it is fully faithful and essentially surjective, and verify the Hecke/Whittaker compatibilities. A disproof would exhibit an object of one side with no counterpart, e.g. a Hecke eigensheaf attached to an irreducible local system that fails to exist or fails uniqueness.

**Status.** The de Rham case over $\mathbb{C}$ was announced as proved in 2024 by Gaitsgory, Raskin and collaborators in a five-paper series. The page is kept **open** because the conjecture as a *program* — quantum, Betti, local, wildly ramified, positive-characteristic and arithmetic ($\ell$-adic over $\mathbb F_q$) versions — remains unresolved, and the 2024 series is still under referee review.

## 2. Mathematical Foundations

**Moduli stacks.** $\mathrm{Bun}_G(X)$ is a smooth algebraic stack, locally of finite type, of dimension $(g-1)\dim G$, where $g$ is the genus. $\mathrm{LocSys}_{\check G}(X)$ classifies pairs $(\mathcal P,\nabla)$ with $\mathcal P$ a $\check G$-bundle and $\nabla$ a flat connection; it is a quasi-smooth derived stack with tangent complex at $\sigma$

$$
T_\sigma \mathrm{LocSys}_{\check G} \;=\; C^\bullet_{\mathrm{dR}}\big(X,\ \mathfrak{\check g}_\sigma\big)[1],
$$

so $\dim \mathrm{LocSys}_{\check G} = (2g-2)\dim \check G$ virtually.

**Geometric Satake.** For the affine Grassmannian $\mathrm{Gr}_G = G(\!(t)\!)/G[[t]]$, the category of $G[[t]]$-equivariant perverse sheaves with convolution is a symmetric monoidal abelian category and

$$
\mathrm{Sph}_G \;\simeq\; \mathrm{Rep}(\check G)
$$

(Lusztig; Ginzburg; Mirković–Vilonen 2007). This is what *defines* $\check G$ geometrically.

**Hecke functors.** The Hecke stack $\mathcal{H}ecke$ parametrizes $(\mathcal P_1,\mathcal P_2,x,\alpha)$ with $\alpha:\mathcal P_1|_{X\setminus x}\cong \mathcal P_2|_{X\setminus x}$. For $V\in\mathrm{Rep}(\check G)$ one obtains
$$
H_V:\ D\text{-mod}(\mathrm{Bun}_G)\longrightarrow D\text{-mod}(X\times\mathrm{Bun}_G).
$$
A **Hecke eigensheaf** for $\sigma\in\mathrm{LocSys}_{\check G}$ is $\mathcal F\neq 0$ with functorial isomorphisms
$$
H_V(\mathcal F)\;\simeq\; V_\sigma\boxtimes \mathcal F ,\qquad V\in\mathrm{Rep}(\check G),
$$
compatible with tensor products, where $V_\sigma$ is the associated flat bundle on $X$.

**Singular support.** For a quasi-smooth stack $\mathcal Y$, coherent complexes have singular support in $\mathrm{Sing}(\mathcal Y)\subset H^{-1}(T^*\mathcal Y)$ (Arinkin–Gaitsgory 2015). Here $\mathrm{Sing}(\mathrm{LocSys}_{\check G})$ is the space of pairs $(\sigma,A)$ with $A\in H^0_{\mathrm{dR}}(X,\mathfrak{\check g}^*_\sigma)$, and $\mathcal N$ imposes that $A$ be nilpotent. Without this restriction the equivalence is false already for $G=\mathrm{GL}_1$, $g=1$.

**Local counterpart.** The Beilinson–Drinfeld construction realizes eigensheaves via critical-level localization: for $\sigma$ an **oper**, $\hat{\mathfrak g}_{\mathrm{crit}}$-modules localize to $D$-modules on $\mathrm{Bun}_G$ and the Feigin–Frenkel isomorphism
$$
\mathfrak z(\hat{\mathfrak g}) \;\simeq\; \mathrm{Fun}\,\mathrm{Op}_{\check{\mathfrak g}}(D^\times)
$$
identifies the center at critical level with functions on the space of $\check{\mathfrak g}$-opers on the punctured disc.

## 3. History & State of the Art (SOTA)

- **1967–70.** Langlands' letter to Weil and the arithmetic reciprocity conjectures; Weil's "Rosetta stone" analogy number fields $\leftrightarrow$ function fields $\leftrightarrow$ Riemann surfaces.
- **1980–87.** Drinfeld proves Langlands for $\mathrm{GL}_2$ over function fields and gives the first geometric reformulation; Laumon (Duke, 1987) states the $\mathrm{GL}_n$ geometric conjecture via automorphic sheaves.
- **1990s.** Beilinson–Drinfeld construct Hecke eigensheaves for **oper** local systems by quantizing the Hitchin system; introduce the "Hitchin's integrable system" framework.
- **2002–04.** Frenkel–Gaitsgory–Vilonen (JAMS 2002) and Gaitsgory (Annals 2004) prove the $\mathrm{GL}_n$ vanishing conjecture, establishing existence of Hecke eigensheaves for irreducible rank-$n$ local systems.
- **2007.** Kapustin–Witten interpret the correspondence as S-duality of $4$d $\mathcal N=4$ super Yang–Mills reduced on $X$, with the Hitchin fibration as a hyperkähler mirror symmetry (SYZ) statement.
- **2015.** Arinkin–Gaitsgory identify nilpotent singular support as the correct spectral condition, yielding the first formulation believed to be literally true.
- **2018–19.** Ben-Zvi–Nadler formulate the **Betti** version (topological local systems, no de Rham structure); Gaitsgory–Lurie prove Weil's conjecture on Tamagawa numbers for function fields, a nonabelian trace-formula input.
- **2024.** Gaitsgory, Raskin, with Arinkin, Beraldo, Campbell, Chen, Færgeman, Lin, Rozenblyum, post *Proof of the geometric Langlands conjecture* I–V (~1000 pages), establishing $\mathbb L_G$ for all reductive $G$ in the unramified de Rham setting over characteristic $0$.

## 4. Partial Results / Verified Cases

- **$G=\mathrm{GL}_1$, any genus $g$:** fully proved — geometric class field theory (Deligne, Laumon). The equivalence reduces to Fourier–Mukai on $\mathrm{Pic}(X)$.
- **$G=\mathrm{GL}_n$, irreducible $\sigma$:** existence of Hecke eigensheaves proved by FGV (2002) + Gaitsgory (2004) via Whittaker sheaves and the vanishing theorem.
- **Oper local systems, any reductive $G$:** eigensheaves constructed by Beilinson–Drinfeld; the locus $\mathrm{Op}_{\check{\mathfrak g}}(X)\subset\mathrm{LocSys}_{\check G}$ has dimension $(g-1)\dim\check G$, exactly half.
- **Abelian/torus case $G=T$:** the equivalence is Fourier–Mukai for the dual torus, with $\mathcal N=0$-section subtleties at $g=1$.
- **Genus $0$:** $\mathrm{LocSys}_{\check G}(\mathbb P^1)$ has only the trivial local system (with automorphisms), and both sides reduce to modules over $H^\bullet(B\check G)$-type algebras; verified directly.
- **Positive characteristic $p$:** Bezrukavnikov–Braverman (2007) prove a $p$-curvature ("Azumaya") form of geometric Langlands for $\mathrm{GL}_n$ over $\overline{\mathbb F}_p$, using the Azumaya property of crystalline differential operators over the Hitchin base.
- **Betti version:** established for $G=\mathrm{GL}_1$; spectral action and Hecke-eigensheaf structure by Nadler–Yun (2019) for rigid local systems.
- **de Rham categorical conjecture, all reductive $G$, char $0$:** claimed proved 2024 *(frontier — verify)*.

## 5. Principal Obstacles

- **Non-quasi-compactness.** $\mathrm{Bun}_G$ is not quasi-compact and has infinitely many unstable strata; naive $D$-module categories lack a compact generator and $!$- and $*$-pushforwards disagree. Controlling behaviour "at infinity" (the Drinfeld–Gaitsgory *ambidexterity* / miraculous duality statements) was the single hardest analytic input.
- **Derived and singular structure.** $\mathrm{LocSys}_{\check G}$ is derived and quasi-smooth, not smooth; ordinary $\mathrm{QCoh}$ fails and $\mathrm{IndCoh}$ with a *nonzero* singular-support condition is required. No classical Fourier transform machinery handles this.
- **Failure of abelian Fourier–Mukai.** For nonabelian $G$ the Hitchin fibration is only generically a torsor under a dual abelian scheme; over the discriminant the fibres are singular, so Fourier–Mukai duality of Hitchin systems (Donagi–Pantev) degenerates precisely where the interesting sheaves live.
- **Perverse $t$-structures do not match.** The equivalence is not $t$-exact; abelian-categorical intuition (perverse sheaves ↔ coherent sheaves) breaks, forcing fully $\infty$-categorical arguments.
- **Trace-formula obstruction.** Deducing statements over $\mathbb F_q$ from geometry requires categorical trace/Frobenius formalism that is only partly developed; the local terms are not known to be computable in general.

## 6. The Gap

Concretely, three gaps remain between Section 4 and Section 1's program:

1. **Ramified/wild case.** The 2024 theorem is unramified. Local systems with irregular singularities require a categorical Stokes-data theory; even the correct statement is conjectural.
2. **Betti and $\ell$-adic transfer.** The Betti conjecture is not formally implied by the de Rham theorem: Riemann–Hilbert does not preserve the relevant singular-support/nilpotence conditions on the automorphic side. The arithmetic $\ell$-adic statement over $\mathbb F_q$, which would feed classical Langlands, requires categorical trace machinery not yet complete.
3. **Quantum deformation.** For $\kappa\neq\mathrm{crit}$ the conjectured equivalence $D_\kappa\text{-mod}(\mathrm{Bun}_G)\simeq D_{\check\kappa}\text{-mod}(\mathrm{Bun}_{\check G})$ (Gaitsgory, Aganagic–Frenkel–Okounkov) is open except for tori and $\mathrm{SL}_2$-type checks.

## 7. Current Research (as of June 2026)

- **Verification of the 2024 proof.** Refereeing and seminar-level verification continues at IHES, Harvard, Yale, Chicago and Bonn; the "vanishing/ambidexterity" chapter (Part IV) is the most scrutinized *(frontier — verify)*.
- **Arithmetic transfer.** Gaitsgory, Raskin, Xinwen Zhu and collaborators work on categorical trace of Frobenius on $\mathrm{Shv}(\mathrm{Bun}_G)$ to extract classical automorphic consequences; Zhu's "coherent sheaves on the stack of Langlands parameters" is the spectral-side model.
- **Local Langlands geometrization.** Fargues–Scholze's geometrization over the Fargues–Fontaine curve gives a $p$-adic analogue; interaction with the function-field proof is an active frontier.
- **Quantum/physics side.** Aganagic–Frenkel–Okounkov's analytic and $q$-deformed program; Kapustin–Witten-style approaches via boundary conditions and $\mathcal N=4$ SYM, pursued by Gaiotto, Witten, Elliott–Yoo.
- **Betti program.** Ben-Zvi, Nadler, Yun: spectral action, character varieties, and links to skein modules and cluster structures.

## 8. Future Work

- Prove the Betti equivalence, ideally by a Riemann–Hilbert-type comparison adapted to nilpotent singular support.
- Extend to ramified and wild ramification, with a categorical Stokes formalism (Boalch's wild character varieties as spectral side).
- Develop the categorical trace formalism to descend from $\overline{\mathbb F}_q$ to $\mathbb F_q$ and obtain new instances of classical function-field Langlands beyond Lafforgue.
- Prove quantum geometric Langlands for $\mathrm{SL}_2$, the first honest nonabelian test.
- Find a shorter, more conceptual proof of the vanishing/ambidexterity theorem; Gaitsgory has flagged this explicitly as desirable.

## 9. Key References

- **[Foundational]** V. Drinfeld. *Langlands' conjecture for $\mathrm{GL}(2)$ over functional fields.* Proc. ICM Helsinki, 1978 (publ. 1980).
- **[Foundational]** G. Laumon. *Correspondance de Langlands géométrique pour les corps de fonctions.* Duke Mathematical Journal 54 (1987), 309–359. [DOI](https://doi.org/10.1215/s0012-7094-87-05418-4)
- **[Foundational]** A. Beilinson, V. Drinfeld. *Quantization of Hitchin's integrable system and Hecke eigensheaves.* Preprint, ca. 1991–2000 (unpublished manuscript).
- **[Foundational]** I. Mirković, K. Vilonen. *Geometric Langlands duality and representations of algebraic groups over commutative rings.* Annals of Mathematics 166 (2007), 95–143. [DOI](https://doi.org/10.4007/annals.2007.166.95)
- **[Key theorem]** E. Frenkel, D. Gaitsgory, K. Vilonen. *On the geometric Langlands conjecture.* Journal of the AMS 15 (2002), 367–417.
- **[Key theorem]** D. Gaitsgory. *On a vanishing conjecture appearing in the geometric Langlands correspondence.* Annals of Mathematics 160 (2004), 617–682. [DOI](https://doi.org/10.4007/annals.2004.160.617)
- **[Formulation]** D. Arinkin, D. Gaitsgory. *Singular support of coherent sheaves and the geometric Langlands conjecture.* Selecta Mathematica 21 (2015), 1–199. [DOI](https://doi.org/10.1007/s00029-014-0167-5)
- **[SOTA / Recent]** D. Arinkin, D. Beraldo, J. Campbell, L. Chen, J. Færgeman, D. Gaitsgory, K. Lin, S. Raskin, N. Rozenblyum. *Proof of the geometric Langlands conjecture, I–V.* Preprint series, 2024.
- **[Physics]** A. Kapustin, E. Witten. *Electric-magnetic duality and the geometric Langlands program.* Communications in Number Theory and Physics 1 (2007), 1–236. [DOI](https://doi.org/10.4310/cntp.2007.v1.n1.a1)
- **[Positive characteristic]** R. Bezrukavnikov, A. Braverman. *Geometric Langlands correspondence for D-modules in prime characteristic: the $\mathrm{GL}(n)$ case.* Pure and Applied Mathematics Quarterly 3 (2007), 153–179. [DOI](https://doi.org/10.4310/pamq.2007.v3.n1.a5)
- **[Betti]** D. Ben-Zvi, D. Nadler. *Betti geometric Langlands.* Proceedings of Symposia in Pure Mathematics 97.2 (2018), 3–41. [DOI](https://doi.org/10.1090/pspum/097.2/01)
- **[Survey]** E. Frenkel. *Lectures on the Langlands program and conformal field theory.* In *Frontiers in Number Theory, Physics and Geometry II*, Springer, 2007, 387–533.
- **[Related]** D. Gaitsgory, J. Lurie. *Weil's Conjecture for Function Fields I.* Annals of Mathematics Studies 199, Princeton University Press, 2019. [DOI](https://doi.org/10.23943/princeton/9780691182148.001.0001)
- **[Local, $p$-adic]** L. Fargues, P. Scholze. *Geometrization of the local Langlands correspondence.* Preprint, arXiv:2102.13459, 2021.

## 10. Worked Example / Concrete Special Case

**Case $G=\mathrm{GL}_1$: geometric class field theory.**

Take $\check G=\mathrm{GL}_1=\mathbb{G}_m$ (self-dual). Then $\mathrm{Bun}_{\mathbb G_m}(X)=\mathrm{Pic}(X)$, and $\mathrm{LocSys}_{\mathbb G_m}(X)$ is the moduli of rank-one flat bundles. A Hecke eigensheaf for $\sigma=(\mathcal L,\nabla)$ is a rank-one local system $\mathcal{A}_\sigma$ on $\mathrm{Pic}(X)$ with
$$
m^*\mathcal A_\sigma \;\simeq\; \sigma \boxtimes \mathcal A_\sigma \quad\text{on } X\times \mathrm{Pic}(X),
$$
where $m(x,\mathcal M)=\mathcal M(x)$ adds a point. This is *multiplicativity* under the Abel–Jacobi maps.

**Construction (Deligne).** Let $X^{(n)}=X^n/S_n$ be the $n$-th symmetric power, $\mathrm{AJ}_n:X^{(n)}\to\mathrm{Pic}^n(X)$ the Abel–Jacobi map, $D\mapsto\mathcal O(D)$. Set $\sigma^{(n)}:=\big(\sigma^{\boxtimes n}\big)^{S_n}$ on $X^{(n)}$. For $n>2g-2$, $\mathrm{AJ}_n$ is a $\mathbb P^{\,n-g}$-bundle, so it has connected simply-connected fibres and $\sigma^{(n)}$ descends: there is a unique $\mathcal A_\sigma^{(n)}$ on $\mathrm{Pic}^n$ with $\mathrm{AJ}_n^*\mathcal A_\sigma^{(n)}\simeq\sigma^{(n)}$. Translating by a fixed degree-one line bundle extends this to all components, giving $\mathcal A_\sigma$ on $\mathrm{Pic}(X)$, and the eigensheaf property follows from $\sigma^{(n+1)}|_{X\times X^{(n)}}=\sigma\boxtimes\sigma^{(n)}$.

**Numerical check, $g=1$.** Let $X=E$ be elliptic, $\mathrm{Pic}^0(E)\cong E$, $\pi_1(E)=\mathbb Z^2$. Rank-one local systems form $\mathrm{Hom}(\mathbb Z^2,\mathbb G_m)=\mathbb G_m^2$, but in the de Rham setting $\mathrm{LocSys}_{\mathbb G_m}(E)$ is a $2$-dimensional stack with generic $\mathbb G_m$-automorphisms; $\dim \mathrm{Bun}_{\mathbb G_m}=(g-1)\cdot 1=0$ plus the $\mathbb G_m$-gerbe, matching $\dim\mathrm{Pic}^0 = 1$ across components. The equivalence is the classical Fourier–Mukai transform
$$
\mathrm{FM}:\ D\text{-mod}(\mathrm{Pic}(E))\ \xrightarrow{\ \sim\ }\ \mathrm{IndCoh}_{\mathcal N}(\mathrm{LocSys}_{\mathbb G_m}(E)),
$$
and here the nilpotence condition is *not* vacuous: $H^0_{\mathrm{dR}}(E,\mathcal O)=k\neq0$, so $\mathrm{Sing}$ is nonzero and dropping the condition $\mathcal N$ would make the functor fail essential surjectivity. This is the smallest instance showing why Arinkin–Gaitsgory's singular-support correction is forced.

**Genus $0$ contrast.** For $X=\mathbb P^1$, $\pi_1=1$, so the only $\check G$-local system is trivial; $\mathrm{Bun}_{\mathbb G_m}(\mathbb P^1)=\mathbb Z\times B\mathbb G_m$ and both sides collapse to $\mathbb Z$-graded modules over $H^\bullet(B\mathbb G_m)=k[u]$, $\deg u=2$ — the conjecture holds by direct computation, with no nilpotence subtlety.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*