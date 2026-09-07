---
id: 03-geometry/lichnerowicz-conjecture
title: "Lichnerowicz Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lichnerowicz Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/lichnerowicz-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $(M,g)$ be a smooth connected pseudo-Riemannian manifold of dimension $n \ge 3$. Its **conformal group** $\mathrm{Conf}(M,[g])$ consists of diffeomorphisms $\varphi$ with $\varphi^*g = e^{2\sigma}g$ for some function $\sigma$. The group is called **inessential** if some metric $\hat g = e^{2f}g$ in the conformal class $[g]$ is preserved (so $\mathrm{Conf}(M,[g]) = \mathrm{Isom}(M,\hat g)$), and **essential** otherwise.

**Riemannian Lichnerowicz Conjecture (Lichnerowicz, c. 1964).** If $(M,g)$ is a compact Riemannian manifold whose conformal group acts essentially, then $(M,[g])$ is conformally diffeomorphic to the round sphere $(S^n,[g_{\mathrm{round}}])$. In the noncompact case, the model is Euclidean space $(\mathbb{R}^n,[\delta])$.

This is a **theorem**: proved by Lelong-Ferrand and independently by Obata (1971), with the sharp $C^0$/quasiconformal version by Ferrand (1996) and Schoen (1995).

**Pseudo-Riemannian Lichnerowicz Conjecture.** If a compact pseudo-Riemannian manifold $(M^{p,q},g)$, $p+q\ge 3$, has essential conformal group, then $(M,[g])$ is conformally flat — i.e. locally conformally equivalent to the model space $\mathrm{Ein}^{p,q}$.

The pseudo-Riemannian version is **false in general signature** (Frances, 2015, counterexamples for $\min(p,q)\ge 2$) and is the object of active work in **Lorentzian signature** $(1,n-1)$, where the conjecture is now settled under real-analyticity. A complete resolution means: prove conformal flatness for all compact smooth Lorentzian $(M,g)$ with essential $\mathrm{Conf}(M,[g])$, or exhibit a smooth compact counterexample.

## 2. Mathematical Foundations

**Conformal structure.** A conformal class on $M^n$, $n\ge 3$, is equivalently a reduction of the frame bundle to $\mathrm{CO}(p,q)=\mathbb{R}^{>0}\times O(p,q)$, and (by Cartan) a canonical **parabolic Cartan geometry** modeled on
$$X = G/P, \qquad G = \mathrm{PO}(p+1,q+1), \quad P = \mathrm{Stab}_G(\text{isotropic line}).$$
The model $X = \mathrm{Ein}^{p,q}$ is the **Einstein universe**: the projectivized null cone of a quadratic form of signature $(p+1,q+1)$ on $\mathbb{R}^{n+2}$. For $q=0$ this is $S^n$ with $G = \mathrm{PO}(1,n+1)$; for $p=1$ it is $(S^1\times S^{n-1})/\pm$ with the conformal class of $-d t^2 + g_{S^{n-1}}$.

**Conformal invariants.** For $n\ge 4$ the **Weyl tensor**
$$W = R - \frac{1}{n-2}\,\mathrm{Ric}_0 \owedge g - \frac{\mathrm{Scal}}{2n(n-1)}\, g\owedge g$$
(with $\owedge$ the Kulkarni–Nomizu product) satisfies $W_{\hat g}=e^{2f}W_g$ for $\hat g = e^{2f}g$; $W\equiv 0 \iff$ conformally flat. For $n=3$ the obstruction is the **Cotton tensor** $C_{ijk} = \nabla_k P_{ij} - \nabla_j P_{ik}$, $P = \frac{1}{n-2}(\mathrm{Ric} - \frac{\mathrm{Scal}}{2(n-1)}g)$.

**Conformal vector fields.** $X\in\mathfrak{X}(M)$ is conformal iff $\mathcal{L}_X g = 2\lambda g$, i.e.
$$\nabla_i X_j + \nabla_j X_i = \frac{2}{n}(\mathrm{div}\,X)\,g_{ij}.$$
The space $\mathfrak{conf}(M,[g])$ is finite-dimensional with $\dim \le \frac{(n+1)(n+2)}{2}$, equality iff conformally flat.

**Obata's rigidity input.** If $\hat g\in[g]$ is Einstein and admits a nonisometric conformal field, then $\nabla^2 f = \frac{\Delta f}{n} \hat g$ has a nonconstant solution, forcing $(M,\hat g)$ to be the round sphere (Obata, 1962). The **Lichnerowicz–Obata eigenvalue theorem** ($\mathrm{Ric}\ge (n-1)g \Rightarrow \lambda_1 \ge n$, equality iff round sphere) is the analytic core of this rigidity.

**Dynamical reformulation.** Essentiality is equivalent to non-properness of the $\mathrm{Conf}$-action on $M$ (Ferrand; Alekseevskii): there exist $\varphi_k\in\mathrm{Conf}$ and $x_k\to x$ with $\varphi_k(x_k)\to y$ but $\varphi_k$ leaving every compact set of $\mathrm{Conf}$. Equivalently the conformal factors $e^{\sigma_k}$ blow up. In Cartan-geometric language this produces a **holonomy sequence** in $P$ whose $\mathrm{Ad}$-action degenerates, and the model is recovered by proving the Cartan curvature vanishes in the limit.

## 3. History & State of the Art (SOTA)

- **c. 1964, Lichnerowicz.** Posed the problem: the round sphere should be the only compact Riemannian manifold with essential conformal group.
- **1971, Lelong-Ferrand & Obata.** Independent proofs in the compact Riemannian case. Obata used Einstein-metric rigidity; Lelong-Ferrand used quasiconformal/capacity methods.
- **1972, Alekseevskii.** Noncompact Riemannian case: essential $\Rightarrow$ conformally $\mathbb{R}^n$ or $S^n$; introduced the properness viewpoint.
- **1995–1996, Schoen; Ferrand.** Optimal statements: the result holds for $C^0$-conformal (quasiconformal) actions; Schoen proved the parallel CR statement (Heisenberg group / sphere).
- **2007, Frances.** Extended the theorem to all rank-one parabolic geometries, replacing PDE arguments by Cartan-geometry dynamics.
- **2010–2013, Frances–Melnick.** Lorentzian structure theory: nilpotent conformal groups have degree $\le 2$ nilpotence, and essential conformal *flows* admit normal forms; conformally flat model forced in many cases.
- **2015, Frances.** *Counterexamples* in signature $(p,q)$ with $p,q\ge 2$: compact, essential, not conformally flat. This kills the naive pseudo-Riemannian conjecture and isolates the Lorentzian case as the sharp open problem.
- **2018–2022, Frances–Melnick; Melnick–Pecastaing; Pecastaing.** Lorentzian conjecture proved for large classes: $\mathrm{SL}(2,\mathbb{R})$-actions, compact simply connected manifolds, higher-rank lattice and semisimple actions.
- **2021–2024, Frances–Melnick.** The **real-analytic compact Lorentzian case** is resolved: essential $\Rightarrow$ conformally flat. This is the "solved-recently" component; the smooth case remains.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| Compact Riemannian, $n\ge 3$ | **Proved** (Lelong-Ferrand, Obata 1971) |
| Noncompact Riemannian | **Proved**: model $\mathbb{R}^n$ (Alekseevskii 1972; Ferrand 1996) |
| $C^0$/quasiconformal Riemannian actions | **Proved** (Ferrand 1996; Schoen 1995) |
| CR / rank-one parabolic geometries | **Proved** (Schoen 1995; Frances 2007) |
| Signature $(p,q)$, $p,q\ge 2$, compact | **False** — counterexamples (Frances 2015) |
| Compact Lorentzian, real-analytic | **Proved** (Frances–Melnick) |
| Compact simply connected Lorentzian | **Proved** (Melnick–Pecastaing, JAMS 2022) |
| Compact Lorentzian, essential $\mathrm{SL}(2,\mathbb{R})$-action | **Proved** (Frances–Melnick, CMH 2018) |
| Compact Lorentzian, higher-rank simple Lie group or lattice acting | **Proved** (Pecastaing) |
| Compact Lorentzian, nilpotent essential group | **Proved**, nilpotence degree $\le 2$ (Frances–Melnick, GAFA 2010) |
| Compact smooth Lorentzian, general | **Open** |

## 5. Principal Obstacles

- **No Einstein representative.** Obata's proof runs by finding $\hat g\in[g]$ with $\mathrm{Ric}$ controlled, using the Yamabe problem and the maximum principle. In Lorentzian signature the conformal Laplacian $L = \Delta_g + \frac{n-2}{4(n-1)}\mathrm{Scal}$ is **hyperbolic**, not elliptic: no maximum principle, no Yamabe solution, no eigenvalue rigidity.
- **Loss of properness/compactness dichotomy.** In Riemannian signature, $\mathrm{Isom}(M,\hat g)$ compact for $M$ compact makes "essential $\Leftrightarrow$ noncompact conformal group" usable. Lorentzian isometry groups of compact manifolds are noncompact routinely (e.g. flat tori with a lightlike Killing field), so noncompactness carries no information.
- **Degenerate dynamics at null directions.** The blow-up of holonomy sequences in $P\subset \mathrm{PO}(2,n)$ can be *lightlike* rather than hyperbolic. Frances' local-degeneracy theory shows the curvature need only vanish along a null sub-locus, not on an open set — the exact failure exploited by his $(2,2)$-counterexamples.
- **Analyticity as a crutch.** Real-analytic proofs propagate vanishing curvature from a single point by the Nomizu/Gromov open-dense integrability theorem for Killing generators. Smooth structures admit local Killing algebras defined only on open subsets, and flat-plus-bump constructions cannot be excluded by any known invariant.

## 6. The Gap

Everything proved in the Lorentzian case either (i) assumes real-analyticity, so that a local conformal flatness statement propagates globally, or (ii) assumes a large acting group (semisimple, lattice, nilpotent, or simply connected ambient topology) whose algebraic structure forces a homogeneous model.

The gap is: **a compact smooth Lorentzian manifold whose essential conformal group is a single one-parameter flow, or a discrete group, with no algebraic structure to exploit.** Concretely, the missing step is to show that the set
$$\Omega = \{x \in M : W_g \text{ vanishes to infinite order at } x\}$$
produced by the blow-up dynamics of a non-proper conformal flow is open — equivalently, to upgrade Frances' "curvature degenerates along the stable null direction" into "curvature vanishes on a neighborhood" without analytic continuation.

## 7. Current Research (as of June 2026)

- **Frances (Strasbourg) and Melnick (Bradley/Maryland):** completion of the real-analytic Lorentzian program and attempts to remove analyticity via normal forms for conformal flows near a fixed point. *(frontier — verify the smooth-case status of the most recent preprints.)*
- **Pecastaing (Nice/Luxembourg):** conformal and projective actions of Lie groups and lattices on compact pseudo-Riemannian manifolds; Zimmer-program methods giving the conjecture whenever the acting group has real rank $\ge 2$.
- **Čap, Melnick, Zimmer school:** general parabolic-geometry essentiality — the conjectured statement that an essential automorphism group of a parabolic geometry forces the flat model in "most" types, with known exceptions in projective and higher-signature conformal geometry.
- **Related but distinct:** the *Lichnerowicz conjecture on harmonic manifolds* (harmonic $\Rightarrow$ flat or rank-one symmetric) — true for compact with finite $\pi_1$ (Szabó 1990), false in the noncompact case (Damek–Ricci 1992), true up to dimension 5 (Nikolayevsky). Do not conflate the two problems.

## 8. Future Work

- Develop a **smooth-category propagation theorem** for local conformal Killing fields: identify a conformally invariant condition weaker than analyticity that forces the local Killing algebra to extend over an open set.
- Classify **compact Lorentzian manifolds with a non-proper conformal flow** by normal form of the flow's linearization at a fixed point (hyperbolic, parabolic-null, mixed), then rule out non-flat curvature case by case.
- Extend Frances' $(2,2)$-counterexample machine to test whether the Lorentzian obstruction is genuinely signature-dependent, or whether the counterexamples are an artifact of two independent timelike directions.
- Transport quasiconformal/capacity methods (Ferrand's route) into a causal setting via optimal-transport or null-geodesic-capacity analogues.

## 9. Key References

- **[Foundational]** M. Obata. *The conjectures on conformal transformations of Riemannian manifolds.* Journal of Differential Geometry 6 (1971), 247–258.
- **[Foundational]** J. Lelong-Ferrand. *Transformations conformes et quasi-conformes des variétés riemanniennes compactes (démonstration de la conjecture de A. Lichnerowicz).* Académie Royale de Belgique, Mémoires Cl. Sci. (2) 39, no. 5 (1971).
- **[Foundational]** D. V. Alekseevskii. *Groups of conformal transformations of Riemannian spaces.* Matematicheskii Sbornik 89 (1972); English transl. Math. USSR Sbornik 18 (1972), 285–301.
- **[Foundational]** J. Ferrand. *The action of conformal transformations on Riemannian manifolds.* Mathematische Annalen 304 (1996), 277–291.
- **[Foundational]** R. Schoen. *On the conformal and CR automorphism groups.* Geometric and Functional Analysis 5 (1995), 464–481.
- **[SOTA]** C. Frances. *Sur le groupe d'automorphismes des géométries paraboliques de rang 1.* Annales Scientifiques de l'École Normale Supérieure 40 (2007), 741–764.
- **[SOTA]** C. Frances, K. Melnick. *Nilpotent groups of conformal transformations of Lorentzian manifolds.* Geometric and Functional Analysis 20 (2010), 1052–1101.
- **[SOTA]** C. Frances, K. Melnick. *Formes normales pour les champs conformes pseudo-riemanniens.* Bulletin de la Société Mathématique de France 141 (2013), 377–421.
- **[SOTA]** C. Frances. *About pseudo-Riemannian Lichnerowicz conjecture.* Transformation Groups 20 (2015), 1103–1128.
- **[SOTA]** C. Frances, K. Melnick. *Lorentzian manifolds with a conformal action of $\mathrm{SL}(2,\mathbb{R})$.* Commentarii Mathematici Helvetici 93 (2018), 61–82.
- **[SOTA]** K. Melnick, F. Pecastaing. *The conformal group of a compact simply connected Lorentzian manifold.* Journal of the American Mathematical Society 35 (2022), 81–122.
- **[Survey]** K. Melnick. *Rigidity of transformation groups in differential geometry.* Notices of the American Mathematical Society 68 (2021), 721–732.
- **[Background]** A. Čap, J. Slovák. *Parabolic Geometries I: Background and General Theory.* Mathematical Surveys and Monographs 154, American Mathematical Society, 2009.
- **[Background]** R. W. Sharpe. *Differential Geometry: Cartan's Generalization of Klein's Erlangen Program.* Springer GTM 166, 1997.

## 10. Worked Example / Concrete Special Case

**Claim: the round sphere $S^n$ is essential — and the computation shows exactly which quantity blows up.**

Use stereographic projection to identify $S^n \setminus \{N\} \cong \mathbb{R}^n$ with $g_{\mathrm{round}} = e^{2u}\delta$, $e^{u(x)} = \frac{2}{1+|x|^2}$. Consider the dilation flow on $\mathbb{R}^n$,
$$\varphi_t(x) = e^{t}x .$$
It is conformal for $\delta$: $\varphi_t^*\delta = e^{2t}\delta$, hence conformal for $[g_{\mathrm{round}}]$, and it extends to $S^n$ fixing $N$ (source) and $S=0$ (sink). The generating field $X = \sum_i x_i\partial_{x_i}$ satisfies $\mathcal{L}_X\delta = 2\delta$.

Suppose some $\hat g = e^{2f}\delta$ on $\mathbb{R}^n$ were invariant. Then
$$\varphi_t^*\hat g = e^{2f\circ\varphi_t}\,e^{2t}\delta = e^{2f}\delta \;\;\Longrightarrow\;\; f(e^t x) = f(x) - t \quad \forall t\in\mathbb{R},\,x\neq 0 .$$
Fix $x_0$ with $|x_0|=1$. Then $f(e^t x_0) = f(x_0)-t \to +\infty$ as $t\to -\infty$, i.e. $f$ is unbounded on every punctured neighborhood of the origin, contradicting continuity of $f$ at $0$. Hence **no metric in the conformal class is $\varphi_t$-invariant: the action is essential.**

The same computation exhibits the non-properness: take $x_k = e^{-k}x_0 \to 0$ and $\varphi_k(x_k) = x_0$, while $\varphi_k \to \infty$ in $\mathrm{Conf}(S^n) = \mathrm{PO}(1,n+1)$. The conformal factor relative to $g_{\mathrm{round}}$ at $x_k$ is
$$e^{\sigma_k(x_k)} = e^{k}\cdot\frac{1+|x_k|^2}{1+|x_0|^2} \;\longrightarrow\; \infty ,$$
the blow-up that Section 2 identifies as the definition of essentiality.

Lichnerowicz's theorem says this is the *only* compact Riemannian example. The Lorentzian question is whether the analogous blow-up on a compact Lorentzian manifold — where the dilation can be replaced by a *null* parabolic flow whose conformal factor grows only along a lightlike direction — still forces $W \equiv 0$. On $\mathrm{Ein}^{1,n-1}$ it does; off the model, in the smooth category, it is unproven.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*