---
id: 04-topology/singer-conjecture
title: "Singer Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Singer Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/singer-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $M$ be a closed aspherical manifold of dimension $n$ (closed: compact, no boundary; aspherical: the universal cover $\widetilde M$ is contractible, equivalently $\pi_i(M)=0$ for $i\ge 2$). Let $b_i^{(2)}(\widetilde M)$ denote the $i$-th $L^2$-Betti number, the von Neumann dimension over the group von Neumann algebra $\mathcal N(\pi_1 M)$ of the reduced $L^2$-homology of $\widetilde M$.

**Conjecture (Singer).**
$$b_i^{(2)}(\widetilde M)=0 \quad \text{for all } i\neq \tfrac n2 .$$

In particular, if $n=2m+1$ is odd, all $L^2$-Betti numbers vanish; if $n=2m$ is even, only $b_m^{(2)}$ may be nonzero, and then Atiyah's $L^2$-index theorem gives
$$\chi(M)=\sum_{i\ge 0}(-1)^i b_i^{(2)}(\widetilde M)=(-1)^m b_m^{(2)}(\widetilde M)\ \ \Longrightarrow\ \ (-1)^m\chi(M)\ge 0 ,$$
so the conjecture implies the **Hopf–Chern conjecture** on the sign of the Euler characteristic of closed aspherical (in particular nonpositively curved) manifolds.

A stronger form, also attributed to Singer, replaces asphericity by nonpositive sectional curvature and additionally asserts $b_m^{(2)}>0$ when the curvature is strictly negative.

A complete resolution means: a proof valid for every closed aspherical $M$ in every dimension, or a single closed aspherical $M^n$ together with a verified computation of some $b_i^{(2)}(\widetilde M)\neq 0$ with $i\neq n/2$.

## 2. Mathematical Foundations

Let $\Gamma=\pi_1(M)$ act freely, cocompactly and cellularly on $\widetilde M$. Write $\mathcal N(\Gamma)=\mathcal B(\ell^2\Gamma)^{\Gamma}$ for the group von Neumann algebra, with faithful normal trace
$$\mathrm{tr}_{\mathcal N(\Gamma)}(f)=\langle f(e),e\rangle_{\ell^2\Gamma},\qquad e\in\Gamma\subset \ell^2\Gamma .$$
For a finitely generated Hilbert $\mathcal N(\Gamma)$-module $V\subset (\ell^2\Gamma)^k$ with orthogonal projection $p_V$,
$$\dim_{\mathcal N(\Gamma)}(V)=\sum_{j=1}^{k}\mathrm{tr}_{\mathcal N(\Gamma)}\big((p_V)_{jj}\big)\in[0,\infty).$$

The cellular $L^2$-chain complex is $C_*^{(2)}(\widetilde M)=\ell^2\Gamma\otimes_{\mathbb Z\Gamma}C_*(\widetilde M)$, and
$$H_i^{(2)}(\widetilde M)=\ker \partial_i/\overline{\operatorname{im}\partial_{i+1}},\qquad b_i^{(2)}(\widetilde M)=\dim_{\mathcal N(\Gamma)}H_i^{(2)}(\widetilde M).$$

Analytically (Dodziuk's $L^2$-Hodge–de Rham theorem), for any $\Gamma$-invariant metric,
$$H_i^{(2)}(\widetilde M)\cong \mathcal H^i_{(2)}(\widetilde M)=\{\omega\in \Omega^i_{L^2}(\widetilde M): d\omega=0,\ \delta\omega=0\},$$
and $b_i^{(2)}$ equals the trace of the heat kernel of the Laplacian $\Delta_i$ on a fundamental domain $\mathcal F$:
$$b_i^{(2)}(\widetilde M)=\lim_{t\to\infty}\int_{\mathcal F}\mathrm{tr}_{\mathbb C}\, e^{-t\Delta_i}(x,x)\,d\mathrm{vol}(x).$$

Facts used throughout:

- **Poincaré duality:** $b_i^{(2)}=b_{n-i}^{(2)}$ for closed orientable $M^n$.
- **$b_0^{(2)}(\widetilde M)=|\Gamma|^{-1}$**, hence $0$ whenever $\Gamma$ is infinite (always true for closed aspherical $M$ with $n\ge1$).
- **Atiyah's $L^2$-index theorem** (1976): $\chi(M)=\sum_i(-1)^i b_i^{(2)}(\widetilde M)$.
- **Cheeger–Gromov / Lück vanishing:** if $\Gamma$ contains an infinite amenable normal subgroup, all $b_i^{(2)}$ vanish.
- **Lück approximation:** for residually finite $\Gamma$ with tower $\Gamma\supset\Gamma_1\supset\cdots$, $b_i^{(2)}(\widetilde M)=\lim_k b_i(M_k;\mathbb Q)/[\Gamma:\Gamma_k]$.

The conjecture is invariant of metric and depends only on $\Gamma$, since $b_i^{(2)}(\widetilde M)=b_i^{(2)}(\Gamma)$ for aspherical $M$; so Singer is a statement about *Poincaré duality groups*.

## 3. History & State of the Art (SOTA)

- **1970s.** Isadore M. Singer raised the question in conversation and lectures following Atiyah's introduction of $L^2$-index theory (Atiyah, *Elliptic operators, discrete groups and von Neumann algebras*, Astérisque 32–33, 1976). Dodziuk's $L^2$-Hodge theory (Topology, 1977) made the invariants computable combinatorially.
- **1979.** Dodziuk computes $\mathcal H^i_{(2)}(\mathbb H^n)$: zero unless $i=n/2$, infinite-dimensional there. This settles the conjecture for closed hyperbolic manifolds and fixes the expected shape of the answer.
- **1985–86.** Borel computes $L^2$-cohomology of symmetric spaces; concentration in the middle degree holds exactly when the fundamental rank $\delta(G)=\mathrm{rk}_{\mathbb C}G-\mathrm{rk}_{\mathbb C}K$ vanishes. Cheeger–Gromov (*Topology*, 1986) prove the amenable-cover vanishing theorems.
- **1991.** Gromov, *Kähler hyperbolicity and $L^2$-Hodge theory* (J. Diff. Geom.): the conjecture holds for closed Kähler hyperbolic manifolds, in particular for closed Kähler manifolds with negative sectional curvature; deduces $(-1)^m\chi>0$.
- **1995.** Lott–Lück (*Invent. Math.*) compute $L^2$-invariants of 3-manifolds; combined with Perelman's geometrization this proves Singer in dimension 3.
- **2001.** Davis–Okun (*Geom. Topol.*) prove Singer for right-angled Coxeter groups in dimension $\le 3$ and show that in dimension 4 it is **equivalent** to the Charney–Davis conjecture on flag triangulations of $S^3$.
- **2002.** Lück's monograph codifies the conjecture (Conjecture 11.1) and its web of consequences.
- **2016–2021.** Okun–Schreve extend vanishing results to groups with hierarchies; Avramidi–Okun–Schreve (*Invent. Math.*, 2021) obtain mod-$p$ and torsion-homology-growth analogues in nonpositive curvature.

No dimension $\ge 4$ is known in general.

## 4. Partial Results / Verified Cases

| Class | Status | Source |
|---|---|---|
| $n\le 2$ | Proven ($b_0^{(2)}=b_2^{(2)}=0$ by duality) | elementary |
| $n=3$, closed aspherical | Proven: all $b_i^{(2)}=0$ | Lott–Lück 1995 + geometrization |
| Closed hyperbolic $M^n$ | Proven | Dodziuk 1979 |
| Closed locally symmetric $\Gamma\backslash G/K$ | Proven; nonvanishing in middle degree iff $\delta(G)=0$ | Borel 1985; Olbrich 2002 |
| Kähler hyperbolic; negatively curved Kähler | Proven, with $(-1)^m\chi>0$ | Gromov 1991 |
| Kähler, nonpositive curvature ("Kähler parabolic") | Proven | Cao–Xavier 2001; Jost–Zuo 2000 |
| $\pi_1$ with infinite amenable normal subgroup (e.g. $T^n$, nilmanifolds, $S^1$-actions) | All $b_i^{(2)}=0$ | Cheeger–Gromov 1986; Lück 2002 |
| Right-angled Coxeter groups, $\dim\le 3$; Davis complexes | Proven | Davis–Okun 2001 |
| RACGs, $\dim 4$ | Equivalent to Charney–Davis conjecture for flag $S^3$ | Davis–Okun 2001 |
| Groups with a hierarchy terminating in trivial groups (many cubulated/hyperbolic cases) | Concentration proven | Okun–Schreve 2016 |
| Pinched negative curvature $-1\le K\le -1+\varepsilon(n)$ | Proven | Donnelly–Xavier 1984; Jost–Xin |
| Graph manifolds, $S^1$-fibered, mapping tori of aspherical bases | All vanish | Lück 2002, Ch. 4 |

## 5. Principal Obstacles

- **$L^2$-Betti numbers are not homotopy-local.** They are quasi-isometry invariants of $\Gamma$, not computable from any finite piece of $M$; no Mayer–Vietoris-plus-induction scheme closes because the pieces of an aspherical manifold are not themselves closed aspherical manifolds.
- **No positivity of the Bochner term.** Gromov's proof rests on a *bounded primitive* of the Kähler form, $\tilde\omega=d\beta$ with $\|\beta\|_\infty<\infty$, which forces a spectral gap of $\Delta$ off the middle degree. General nonpositively curved (or merely aspherical) manifolds carry no such closed 2-form; the Bochner–Weitzenböck curvature term in $\Delta=\nabla^*\nabla+\mathcal R_i$ is indefinite on $i$-forms once $2\le i\le n-2$, so vanishing cannot be read off pointwise curvature.
- **No spectral gap in general.** Vanishing of $b_i^{(2)}$ needs $0$ to be either outside the spectrum of $\Delta_i$ or non-atomic in a dimension-measure sense; for a general cocompact $\Gamma$ nothing constrains the Novikov–Shubin invariants, and $0$ may be a spectral point of infinite multiplicity a priori.
- **Aspherical $\ne$ nonpositively curved.** Davis's reflection-group constructions produce closed aspherical manifolds whose universal covers are not simply connected at infinity and which admit no CAT(0) metric, killing all comparison-geometry arguments.
- **Approximation gives the wrong side.** Lück approximation converts $b_i^{(2)}$ into normalized ordinary Betti numbers of finite covers, but no method bounds $b_i(M_k)$ sublinearly for $i\neq n/2$ without already knowing the geometry; torsion-homology growth in the same range is likewise uncontrolled.
- **Combinatorial reduction is itself open.** In the best-understood family (RACGs), dimension 4 is exactly the Charney–Davis conjecture, an open flag-complex inequality about $f$-vectors — the difficulty simply relocates.

## 6. The Gap

Everything proven falls into three buckets: (i) dimension $\le 3$, where duality plus geometrization is decisive; (ii) manifolds carrying extra rigid structure (locally symmetric, Kähler with bounded primitive, pinched curvature, amenable normal subgroup); (iii) combinatorially special groups (Coxeter, cubulated, hierarchies).

The gap is a **single closed aspherical 4-manifold with no extra structure**. Precisely: for $M^4$ aspherical one must show $b_1^{(2)}(\widetilde M)=0$ — by duality this forces $b_3^{(2)}=0$ and $\chi(M)=b_2^{(2)}\ge0$. The needed step is a mechanism producing vanishing of low-degree $L^2$-cohomology from asphericity alone (a Poincaré-duality-group property), rather than from curvature, complex structure, or a group hierarchy. No candidate for such a mechanism is currently known, and even the weaker Hopf conjecture $\chi\ge0$ for aspherical $M^4$ is open (it is known for nonpositively curved $M^4$ by the sign of the Gauss–Bonnet integrand).

## 7. Current Research (as of June 2026)

- **Cubulation and hierarchies.** Okun, Schreve, and collaborators continue pushing hierarchy-based concentration theorems to broader classes of cocompactly cubulated and hyperbolic groups; the target is a class large enough to contain a 4-dimensional aspherical example not covered by curvature hypotheses.
- **Homology growth and $\ell^2$-torsion.** Avramidi–Okun–Schreve's mod-$p$ growth program (Invent. Math. 2021) is being extended to relate torsion growth in degrees $\neq n/2$ to Singer-type vanishing *(frontier — verify)*.
- **Agrarian and RFRS methods.** Kielak's RFRS/Bieri–Neumann–Strebel machinery, and work of Fisher, Hughes and coauthors on agrarian invariants and $\ell^2$-Betti numbers of virtually RFRS groups, give new vanishing criteria in degree 1 for large classes of groups *(frontier — verify)*.
- **Coxeter/flag-complex combinatorics.** Charney–Davis in dimension 3 (flag triangulations of $S^3$) remains the crisp equivalent target; work on $\gamma$-vectors and Gal's conjecture is the combinatorial front.
- **Groups:** Bonn/Münster ($L^2$-invariants school around Lück), Illinois–Chicago and Michigan State (Schreve, Okun), MPIM Bonn (Avramidi), Oxford (Kielak, Hughes, Fisher), Ohio State (Davis).

## 8. Future Work

- Prove the Charney–Davis conjecture for flag triangulations of $S^3$, settling Singer for 4-dimensional right-angled Coxeter orbifolds.
- Find a purely group-theoretic criterion — a Poincaré-duality-group analogue of "bounded primitive" — implying $b_1^{(2)}(\Gamma)=0$ for $n$-dimensional $\mathrm{PD}_n$ groups with $n\ge3$.
- Prove the aspherical Hopf conjecture $(-1)^{n/2}\chi\ge0$ in dimension 4 independently, as a consistency test and possible stepping stone.
- Establish sublinear growth of $b_1$ in residually finite towers of aspherical 4-manifolds, using Lück approximation in reverse.
- Extend Gromov's spectral-gap argument to non-Kähler settings via bounded cohomology classes of degree 2 with bounded primitives on $\widetilde M$.

## 9. Key References

- **[Foundational]** M. F. Atiyah. *Elliptic operators, discrete groups and von Neumann algebras.* Astérisque 32–33 (1976), 43–72.
- **[Foundational]** J. Dodziuk. *de Rham–Hodge theory for $L^2$-cohomology of infinite coverings.* Topology 16 (1977), 157–165.
- **[Foundational]** J. Dodziuk. *$L^2$-harmonic forms on rotationally symmetric Riemannian manifolds.* Proc. Amer. Math. Soc. 77 (1979), 395–400. [DOI](https://doi.org/10.2307/2042193)
- **[Foundational]** J. Cheeger, M. Gromov. *$L_2$-cohomology and group cohomology.* Topology 25 (1986), 189–215.
- **[Foundational]** M. Gromov. *Kähler hyperbolicity and $L_2$-Hodge theory.* J. Differential Geom. 33 (1991), 263–292. [DOI](https://doi.org/10.4310/jdg/1214446039)
- **[Foundational]** J. Lott, W. Lück. *$L^2$-topological invariants of 3-manifolds.* Invent. Math. 120 (1995), 15–60.
- **[SOTA]** M. W. Davis, B. Okun. *Vanishing theorems and conjectures for the $\ell^2$-homology of right-angled Coxeter groups.* Geom. Topol. 5 (2001), 7–74.
- **[SOTA]** J. Cao, F. Xavier. *Kähler parabolicity and the Euler number of compact manifolds of non-positive sectional curvature.* Math. Ann. 319 (2001), 483–491. [DOI](https://doi.org/10.1007/pl00004444)
- **[SOTA]** M. Olbrich. *$L^2$-invariants of locally symmetric spaces.* Doc. Math. 7 (2002), 219–237. [DOI](https://doi.org/10.4171/dm/125)
- **[SOTA]** B. Okun, K. Schreve. *The $L^2$-(co)homology of groups with hierarchies.* Algebr. Geom. Topol. 16 (2016), 2549–2569.
- **[SOTA]** G. Avramidi, B. Okun, K. Schreve. *Mod p and torsion homology growth in nonpositive curvature.* Invent. Math. 226 (2021), 711–723. [DOI](https://doi.org/10.1007/s00222-021-01057-x)
- **[Survey / Book]** W. Lück. *$L^2$-Invariants: Theory and Applications to Geometry and K-Theory.* Ergebnisse der Mathematik 44, Springer, 2002.
- **[Survey / Book]** M. W. Davis. *The Geometry and Topology of Coxeter Groups.* London Math. Soc. Monographs 32, Princeton Univ. Press, 2008.

## 10. Worked Example / Concrete Special Case

**Case A: genus-2 surface, $n=2$.** Let $M=\Sigma_2$, $\Gamma=\pi_1(\Sigma_2)$, $\widetilde M=\mathbb H^2$. Then:

1. $\Gamma$ is infinite, so $b_0^{(2)}=|\Gamma|^{-1}=0$.
2. Poincaré duality: $b_2^{(2)}=b_0^{(2)}=0$.
3. Atiyah: $\chi(\Sigma_2)=2-2\cdot2=-2=b_0^{(2)}-b_1^{(2)}+b_2^{(2)}=-b_1^{(2)}$, so
$$b_1^{(2)}(\mathbb H^2)=2 .$$

Concentration in degree $n/2=1$ holds, with strict positivity as predicted for negative curvature. Cross-check by Lück approximation: the degree-$k$ cover $\Sigma_{k+1}\to\Sigma_2$ has $b_1=2k+2$, so $b_1/k\to 2$. ✔

**Case B: a 3-manifold, $n=3$.** Let $M=S^1\times\Sigma_2$, aspherical with $\Gamma=\mathbb Z\times\pi_1(\Sigma_2)$. The factor $\mathbb Z$ is an infinite amenable normal subgroup, so by Cheeger–Gromov/Lück all $b_i^{(2)}=0$ — consistent with the odd-dimensional prediction. Directly: the Künneth formula for $L^2$-Betti numbers gives
$$b_i^{(2)}(\widetilde M)=\sum_{p+q=i} b_p^{(2)}(\mathbb R)\,b_q^{(2)}(\mathbb H^2),$$
and $b_0^{(2)}(\mathbb R)=b_1^{(2)}(\mathbb R)=0$ for the $\mathbb Z$-cover of $S^1$, so every term vanishes. ✔

**Where it breaks down, $n=4$.** Take $M^4$ aspherical with $\Gamma$ a $\mathrm{PD}_4$ group having no amenable normal subgroup, no CAT(0) or Kähler structure (e.g. a Davis reflection-group manifold built from a flag triangulation $L$ of $S^3$). Duality gives $b_0^{(2)}=b_4^{(2)}=0$ and $b_1^{(2)}=b_3^{(2)}$, hence
$$\chi(M)=b_2^{(2)}-2b_1^{(2)} .$$
Singer asserts $b_1^{(2)}=0$, i.e. $\chi(M)=b_2^{(2)}\ge0$. For the Davis complex of the right-angled Coxeter group $W_L$, Davis–Okun show this reduces to the inequality $(-1)^{2}\kappa(L)\ge0$ where $\kappa(L)=\sum_{\sigma\in L}(-1/2)^{|\sigma|}$ — exactly the Charney–Davis conjecture for flag $S^3$. No proof of that inequality is known, and no computation of $b_1^{(2)}(W_L)$ bypasses it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*