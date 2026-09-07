---
id: 05-analysis/quantum-unique-ergodicity
title: "Quantum Unique Ergodicity"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Quantum Unique Ergodicity

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/quantum-unique-ergodicity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(M,g)$ be a compact Riemannian manifold with negative sectional curvature, and let $\{\varphi_j\}_{j\ge 1}$ be an orthonormal basis of $L^2(M)$ of Laplace eigenfunctions,
$$-\Delta_g \varphi_j = \lambda_j \varphi_j, \qquad 0=\lambda_0 < \lambda_1 \le \lambda_2 \le \cdots \to \infty .$$

**Rudnick–Sarnak QUE Conjecture (1994).** The microlocal lifts $\mu_j$ of $|\varphi_j|^2$ to the unit cotangent bundle $S^*M$ converge weak-$*$ to the normalized Liouville measure $\mu_L$:
$$\langle \mathrm{Op}(a)\varphi_j,\varphi_j\rangle \;\longrightarrow\; \int_{S^*M} a \, d\mu_L \qquad \text{for every } a\in C^\infty_c(T^*M),$$
along the **entire** sequence, not merely a density-one subsequence. In particular, on the base,
$$\int_M f\,|\varphi_j|^2\,d\mathrm{vol} \;\longrightarrow\; \frac{1}{\mathrm{vol}(M)}\int_M f\,d\mathrm{vol}, \qquad f\in C(M).$$

A proof must show the set of *quantum limits* (weak-$*$ accumulation points of $\{\mu_j\}$) is the singleton $\{\mu_L\}$. A disproof exhibits a negatively curved $M$ and a subsequence whose limit charges a closed geodesic, a fractal invariant set, or any measure $\ne \mu_L$. The conjecture is stated for negative curvature; the analogous statement for general ergodic geodesic flows is **false** (Section 4).

## 2. Mathematical Foundations

**Semiclassical setup.** Write $\lambda_j = h_j^{-2}$, $h_j\to 0$. For a symbol $a\in S^0(T^*M)$ let $\mathrm{Op}_h(a)$ be a standard quantization. Define the distribution
$$\mu_j(a) := \langle \mathrm{Op}_{h_j}(a)\varphi_j, \varphi_j\rangle_{L^2(M)} .$$
Sharp Gårding and $L^2$-boundedness give $|\mu_j(a)|\le \|a\|_\infty + O(h_j)$, so $\{\mu_j\}$ is precompact in the weak-$*$ topology; every limit is a probability measure on $S^*M$.

**Invariance.** Egorov's theorem states that for the geodesic flow $g^t$ on $S^*M$,
$$U_h(t)^*\,\mathrm{Op}_h(a)\,U_h(t) = \mathrm{Op}_h(a\circ g^t) + O(h), \qquad U_h(t)=e^{it h \Delta_g/2}.$$
Since $\varphi_j$ is an eigenvector of $U_{h_j}(t)$ up to a phase, $\mu_j(a\circ g^t)-\mu_j(a)\to 0$. Hence **every quantum limit is $g^t$-invariant**. QUE asserts that among the (typically uncountably many) invariant measures, only $\mu_L$ arises.

**Quantum ergodicity (the weaker theorem).** If $g^t$ is ergodic for $\mu_L$, then there is $S\subset\mathbb N$ of density one with $\mu_j\to\mu_L$ for $j\in S$ (Shnirelman 1974, Zelditch 1987, Colin de Verdière 1985). Quantitatively,
$$\frac{1}{N(\lambda)}\sum_{\lambda_j\le\lambda}\Big|\mu_j(a)-\int a\,d\mu_L\Big|^2 \longrightarrow 0 .$$
QUE is exactly the removal of the exceptional density-zero set.

**Kolmogorov–Sinai entropy.** For $\mu$ invariant under $g^t$ on a compact negatively curved surface of curvature $-1$, $0\le h_{KS}(\mu)\le 1$, with $h_{KS}(\mu_L)=1$ (Pesin/Ruelle: $h_{KS}(\mu)=\int \lambda^+ d\mu$ for SRB). Delta measures on closed geodesics have $h_{KS}=0$.

**Arithmetic setting.** For $X=\Gamma\backslash\mathbb H$ with $\Gamma$ a congruence lattice (e.g. $\mathrm{SL}_2(\mathbb Z)$ or a unit group of a quaternion division algebra), the eigenfunctions may be taken to be **Hecke–Maass forms**: joint eigenfunctions of $\Delta$ and all Hecke operators $T_p$,
$$(T_n f)(z) = \frac{1}{\sqrt n}\sum_{ad=n}\sum_{b \bmod d} f\!\left(\frac{az+b}{d}\right), \qquad T_n f = \lambda_f(n) f .$$
This extra symmetry is what makes the problem tractable. Watson's triple-product formula converts the QUE integral into a central $L$-value: for $\phi$ a fixed even Hecke–Maass cusp form on $\mathrm{SL}_2(\mathbb Z)\backslash\mathbb H$,
$$\Big|\int_X \phi\,|\varphi_j|^2 d\mu\Big|^2 \;=\; \frac{\Lambda(\tfrac12,\phi\times\varphi_j\times\varphi_j)}{8\,\Lambda(1,\mathrm{sym}^2\phi)\,\Lambda(1,\mathrm{sym}^2\varphi_j)^2},$$
with $\Lambda(s,\phi\times\varphi_j\times\varphi_j)=\Lambda(s,\phi)\Lambda(s,\mathrm{sym}^2\varphi_j\times\phi)$ (degree $1+6$).

## 3. History & State of the Art (SOTA)

- **1974–1985.** Shnirelman, Zelditch, Colin de Verdière establish quantum ergodicity: equidistribution along a density-one subsequence.
- **1994.** Rudnick and Sarnak (*Comm. Math. Phys.* 161) formulate QUE, prove no quantum limit on a congruence surface can be supported on finitely many closed geodesics, and disprove the naive analogue for quantized cat maps' arithmetic-free setting.
- **1995.** Luo and Sarnak prove QUE for **Eisenstein series** $E(z,\tfrac12+it)$ on $\mathrm{SL}_2(\mathbb Z)\backslash\mathbb H$ (continuous spectrum), using subconvexity for $\zeta$ and Rankin–Selberg $L$-functions.
- **2001.** Kurlberg–Rudnick prove QUE for the quantized cat map along Hecke eigenbases.
- **2003.** Faure–Nonnenmacher–De Bièvre construct non-Hecke cat-map eigenbases whose limits are $\tfrac12\mu_L + \tfrac12\delta_{\text{periodic orbits}}$: **strong QUE is false for quantized cat maps**.
- **2006.** Lindenstrauss (*Annals* 163) proves **arithmetic QUE**: on compact congruence quotients, the only quantum limit for Hecke–Maass forms is $\mu_L$. Fields Medal 2010.
- **2008.** Anantharaman (*Annals* 168) proves quantum limits on negatively curved manifolds have positive KS entropy — no purely singular concentration.
- **2010.** Holowinsky–Soundararajan (*Annals* 172) prove QUE for **holomorphic** Hecke eigenforms of increasing weight on $\mathrm{SL}_2(\mathbb Z)\backslash\mathbb H$; Soundararajan (same volume) rules out escape of mass, completing Lindenstrauss's argument for the non-compact modular surface.
- **2010.** Hassell (*Annals* 171) proves the Bunimovich stadium billiard is ergodic but **not** QUE for almost every aspect ratio.
- **2018–2022.** Dyatlov–Jin and Dyatlov–Jin–Nonnenmacher: via fractal uncertainty, every semiclassical measure on a negatively curved surface has **full support**.

## 4. Partial Results / Verified Cases

- **Arithmetic hyperbolic surfaces, Hecke basis.** Lindenstrauss (2006): for $\Gamma$ a congruence lattice in $\mathrm{SL}_2(\mathbb R)$ coming from a quaternion division algebra (compact $X$), $\mu_j\to\mu_L$ along all Hecke–Maass forms. With Soundararajan (2010), also for $\Gamma=\mathrm{SL}_2(\mathbb Z)$.
- **Holomorphic forms, weight aspect.** Holowinsky–Soundararajan (2010): $k^{-1}\,y^k|f(z)|^2\,\frac{dxdy}{y^2}\to \mu_L$ as $k\to\infty$ for Hecke cusp forms of level 1. Extended to level aspect by Nelson (Duke 2011) and to powerful levels by Nelson–Pitale–Saha (*JAMS* 2014).
- **Eisenstein series.** Luo–Sarnak (1995), Jakobson (1994): full QUE with a rate $O(t^{-1/6+\epsilon})$ type saving for the continuous spectrum on the modular surface.
- **Higher rank.** Silberman–Venkatesh (2007, GAFA) prove arithmetic QUE for Hecke eigenfunctions on compact quotients of $\mathrm{SL}_n(\mathbb R)/\mathrm{SO}(n)$, $n$ prime.
- **Entropy bounds.** Anantharaman–Nonnenmacher (2007): on a surface of curvature $-1$, every semiclassical measure has $h_{KS}\ge \tfrac12$; on $\mathbb H$-quotients Brooks–Lindenstrauss (2014) show any measure with $h_{KS}>0$ plus Hecke-recurrence is $\mu_L$.
- **Support.** Dyatlov–Jin–Nonnenmacher (2022, *JAMS*): every semiclassical measure on a negatively curved surface has full support in $S^*M$.
- **Negative results delimiting scope.** Stadium billiards (Hassell 2010) and cat maps (FNDB 2003) show that ergodicity alone, or Anosov-ness without arithmetic symmetry and without multiplicity control, does not force QUE.

## 5. Principal Obstacles

- **Spectral degeneracy.** Nothing is known about multiplicities of $\lambda_j$; conjecturally $O(\lambda^\epsilon)$ on congruence surfaces, but only $O(\sqrt\lambda/\log\lambda)$ is proved. Any large eigenspace lets one form bad linear combinations — exactly the FNDB cat-map mechanism. Without a canonical basis, QUE is basis-dependent.
- **Ehrenfest barrier.** Egorov's theorem holds only for $|t|\lesssim \frac{1}{2\lambda_{\max}}\log(1/h)$. Beyond the Ehrenfest time, classical/quantum correspondence collapses; but equidistribution of a single orbit needs times of order $h^{-\epsilon}$, exponentially longer. All propagation-based arguments stall here.
- **The entropy gap.** Anantharaman–Nonnenmacher give $h_{KS}\ge \frac12$ (constant curvature $-1$, surface). QUE needs the maximum $h_{KS}=1$, and even that only *characterizes* $\mu_L$ by the variational principle. Closing $[\tfrac12,1)$ requires beating the hyperbolic-dispersive estimate with no known replacement; the $\frac12$ is a hard limit of the entropic uncertainty principle used.
- **Subconvexity wall.** Watson's formula reduces QUE on $\mathrm{SL}_2(\mathbb Z)\backslash\mathbb H$ to subconvexity for $L(\tfrac12,\mathrm{sym}^2\varphi_j\times\phi)$, a degree-6 $L$-function with conductor $\asymp t_j^4$ in the spectral aspect. No subconvex bound for degree-6 $L$-functions in this aspect is known; the convexity bound falls short by exactly the amount needed.
- **No arithmetic in general.** Lindenstrauss's measure classification uses Hecke correspondences to produce a second, transverse invariance. A generic negatively curved $M$ has trivial commensurator (Margulis), so this input has no analogue.

## 6. The Gap

Proved: (i) equidistribution for the arithmetic Hecke basis on congruence quotients; (ii) $h_{KS}\ge\frac12$ and full support for *all* eigenfunctions in negative curvature. The general conjecture asserts uniqueness of the quantum limit for *any* orthonormal basis on *any* negatively curved $M$.

The gap has two disjoint components:

1. **Non-arithmetic case.** Upgrade $h_{KS}\ge\frac12$ (or full support) to $h_{KS}=1$, equivalently $\mu=\mu_L$ by the variational principle for the Anosov geodesic flow. Nothing currently interpolates between "positive entropy" and "maximal entropy".
2. **Arithmetic case, non-Hecke bases.** Even on $\mathrm{SL}_2(\mathbb Z)\backslash\mathbb H$, QUE for an arbitrary orthonormal eigenbasis is open, and would follow from simplicity (or $\lambda^{o(1)}$ multiplicity) of the Laplace spectrum — itself open.

## 7. Current Research (as of June 2026)

- **Fractal uncertainty principle (FUP).** Dyatlov, Jin, Bourgain, Nonnenmacher: FUP gives full support and observability; extending FUP-derived lower bounds on $\mu(a)$ toward a quantitative entropy improvement is the most active analytic route. Higher-dimensional FUP remains partial. *(frontier — verify)*
- **Effective/quantitative arithmetic QUE.** Rates of convergence in Lindenstrauss's theorem, using effective measure rigidity (Lindenstrauss–Einsiedler–Wieser style) — currently far weaker than the $t_j^{-1/2+\epsilon}$ predicted under GRH. *(frontier — verify)*
- **QUE in the level and hybrid aspects.** Nelson, Saha, Hu, and collaborators push mass equidistribution to $\mathrm{GL}_2$ over number fields, Siegel modular forms, and $p$-adic/hybrid aspects via the relative trace formula. *(frontier — verify)*
- **Random-wave and Berry-conjecture side.** Statistical models (Nazarov–Sodin, Ingremeau) test whether QUE is consistent with Gaussian-field heuristics for nodal sets; QUE implies equidistribution of nodal domains (Han, Jung–Zelditch).
- **Groups.** Princeton/IAS (Sarnak school), Hebrew University (Lindenstrauss), MIT/Berkeley (Dyatlov, Jin), Bristol/Göttingen (Marklof, Rudnick's collaborators), Bonn/MPIM (Nelson).

## 8. Future Work

- Prove multiplicity bounds $m(\lambda)=O(\lambda^{\epsilon})$ on congruence surfaces; this would make Hecke-basis QUE basis-independent and close component (2) of the gap.
- Obtain subconvexity for degree-6 $L$-functions in the spectral aspect, giving a second, effective proof of QUE with a power-saving rate.
- Push the entropy lower bound above $\frac12$ on hyperbolic surfaces by combining FUP with the Anantharaman–Nonnenmacher pressure argument.
- Settle QUE for the *joint quasimode* / small-spectral-window version (Brooks–Lindenstrauss), which is the natural strengthening robust to multiplicity.
- Clarify the boundary: classify which ergodic-but-not-Anosov systems (stadiums, polygons, Sinai billiards) admit exceptional subsequences, sharpening what curvature actually buys.

## 9. Key References

- **[Foundational]** Z. Rudnick and P. Sarnak. *The behaviour of eigenstates of arithmetic hyperbolic manifolds.* Communications in Mathematical Physics 161 (1994), 195–213.
- **[Foundational]** Y. Colin de Verdière. *Ergodicité et fonctions propres du laplacien.* Communications in Mathematical Physics 102 (1985), 497–502.
- **[Foundational]** S. Zelditch. *Uniform distribution of eigenfunctions on compact hyperbolic surfaces.* Duke Mathematical Journal 55 (1987), 919–941.
- **[SOTA]** E. Lindenstrauss. *Invariant measures and arithmetic quantum unique ergodicity.* Annals of Mathematics 163 (2006), 165–219.
- **[SOTA]** K. Soundararajan. *Quantum unique ergodicity for $\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$.* Annals of Mathematics 172 (2010), 1529–1538.
- **[SOTA]** R. Holowinsky and K. Soundararajan. *Mass equidistribution for Hecke eigenforms.* Annals of Mathematics 172 (2010), 1517–1528.
- **[SOTA]** N. Anantharaman. *Entropy and the localization of eigenfunctions.* Annals of Mathematics 168 (2008), 435–475.
- **[SOTA]** N. Anantharaman and S. Nonnenmacher. *Half-delocalization of eigenfunctions for the Laplacian on an Anosov manifold.* Annales de l'Institut Fourier 57 (2007), 2465–2523.
- **[SOTA]** S. Dyatlov, L. Jin and S. Nonnenmacher. *Control of eigenfunctions on surfaces of variable curvature.* Journal of the AMS 35 (2022), 361–465.
- **[Counterexample]** A. Hassell. *Ergodic billiards that are not quantum unique ergodic.* Annals of Mathematics 171 (2010), 605–618.
- **[Counterexample]** F. Faure, S. Nonnenmacher and S. De Bièvre. *Scarred eigenstates for quantum cat maps of minimal periods.* Communications in Mathematical Physics 239 (2003), 449–492.
- **[Related]** W. Luo and P. Sarnak. *Quantum ergodicity of eigenfunctions on $\mathrm{PSL}_2(\mathbb{Z})\backslash\mathbb{H}^2$.* Publications Mathématiques de l'IHÉS 81 (1995), 207–237.
- **[Survey]** P. Sarnak. *Recent progress on the quantum unique ergodicity conjecture.* Bulletin of the AMS 48 (2011), 211–228.
- **[Survey]** S. Zelditch. *Recent developments in mathematical quantum chaos.* Current Developments in Mathematics 2009, International Press, 2010, 115–204.
- **[Textbook]** M. Zworski. *Semiclassical Analysis.* Graduate Studies in Mathematics 138, American Mathematical Society, 2012.

## 10. Worked Example / Concrete Special Case

**Why degeneracy kills QUE: the flat torus $\mathbb T^2=\mathbb R^2/\mathbb Z^2$.**

Eigenfunctions are $e_n(x)=e^{2\pi i\,n\cdot x}$ with $-\Delta e_n = 4\pi^2|n|^2 e_n$. Take $\lambda/4\pi^2 = 25$, realized by $n_1=(5,0)$ and $n_2=(4,3)$ (and symmetric images). Set
$$\psi = \tfrac{1}{\sqrt2}\big(e_{n_1}+e_{n_2}\big), \qquad \|\psi\|_{L^2}=1 .$$
Then
$$|\psi(x)|^2 = \tfrac12\big(2 + 2\,\mathrm{Re}\,e^{2\pi i (n_1-n_2)\cdot x}\big) = 1 + \cos\!\big(2\pi (x_1-3x_2)\big).$$
Testing against $f(x)=\cos(2\pi(x_1-3x_2))$ gives
$$\int_{\mathbb T^2} f\,|\psi|^2\,dx = \tfrac12 \ne 0 = \int_{\mathbb T^2} f\,dx .$$
Repeating with $|n|^2 = 25\cdot 4^k$ produces an infinite sequence of eigenfunctions whose mass never equidistributes: the limit measure is $(1+\cos 2\pi(x_1-3x_2))\,dx$. The mechanism is the unbounded multiplicity $r_2(N)$ of the circle problem, which is $N^{o(1)}$ on average but unbounded.

Two lessons. First, this does **not** contradict QUE: the torus is flat, its geodesic flow is not ergodic, and the exceptional basis exploits eigenvalue multiplicity, not dynamics. Second, it isolates precisely the risk in the negatively curved case — if $\lambda_j$ had large multiplicities there, the same recombination could manufacture a non-Liouville limit.

**Contrast, the arithmetic surface.** On $X=\mathrm{SL}_2(\mathbb Z)\backslash\mathbb H$, Hecke operators select a canonical basis. For $\varphi_j$ Hecke–Maass with spectral parameter $t_j$ and a fixed Maass form $\phi$, Watson's formula gives
$$\Big|\int_X \phi\,|\varphi_j|^2 d\mu\Big|^2 \;\asymp\; \frac{L(\tfrac12,\phi)\,L(\tfrac12,\mathrm{sym}^2\varphi_j\times\phi)}{L(1,\mathrm{sym}^2\varphi_j)^2}\cdot \frac{1}{t_j^{\,2}}\quad(\text{archimedean factors absorbed}),$$
so under the Generalized Lindelöf Hypothesis the numerator is $t_j^{\epsilon}$, and $\int_X \phi|\varphi_j|^2 d\mu \ll t_j^{-1/2+\epsilon}\to 0$: QUE with an essentially optimal rate. Unconditionally the convexity bound for the degree-6 factor is too weak, which is why Lindenstrauss's ergodic-theoretic proof — measure rigidity for the diagonal flow with Hecke recurrence, giving qualitative but ineffective convergence — remains the only complete argument.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*