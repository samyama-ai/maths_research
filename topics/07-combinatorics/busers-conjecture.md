---
id: 07-combinatorics/busers-conjecture
title: "Buser's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Buser's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/busers-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Buser's inequality is the reverse of Cheeger's inequality: on a closed Riemannian manifold with Ricci curvature bounded below by $-K$ ($K \ge 0$), the spectral gap is controlled *from above* by the isoperimetric (Cheeger) constant,
$$\lambda_1 \;\le\; C\big(\sqrt{K}\,h + h^2\big).$$
Without a curvature lower bound the inequality is false: a manifold can have a large spectral gap and a thin bottleneck.

**Buser's conjecture (discrete form).** Let $G=(V,E)$ be a finite connected graph of maximum degree $d$ whose normalized graph Laplacian satisfies the Bakry–Émery curvature-dimension condition $CD(-K,\infty)$ with $K \ge 0$. Then there is an absolute constant $C$ with
$$\lambda_1(G) \;\le\; C\big(\sqrt{K}\,h(G) + d\, h(G)^2\big),$$
where $\lambda_1$ is the smallest nonzero eigenvalue of the normalized Laplacian and $h(G)$ the Cheeger constant. In particular, for $K=0$ (nonnegative curvature), $\lambda_1 \le C\,d\,h^2$.

A complete solution means either a proof valid for all finite graphs satisfying $CD(-K,\infty)$ — with the degree factor $d$ (or a proven substitute) — or a family of nonnegatively curved graphs with $\lambda_1 / (d h^2) \to \infty$. Note that a distinct statement also called "Buser's conjecture" — that closed hyperbolic surfaces of large genus attain $\lambda_1 \to 1/4$ — was settled by Hide–Magee (2023); it is *not* the open problem tracked here, though the two share Buser's 1978 graph-theoretic origin.

## 2. Mathematical Foundations

Let $G=(V,E)$ be finite, connected, simple, with degrees $d_x$ and maximum degree $d$. The normalized Laplacian acts by
$$\Delta f(x) \;=\; \frac{1}{d_x}\sum_{y\sim x}\big(f(y)-f(x)\big),$$
and $-\Delta$ has spectrum $0=\lambda_0 < \lambda_1 \le \cdots \le \lambda_{n-1} \le 2$.

For $S\subseteq V$ set $\mathrm{vol}(S)=\sum_{x\in S} d_x$ and $|\partial S| = \\#\{(x,y)\in E : x\in S,\ y\notin S\}$. The **Cheeger constant** is
$$h(G) \;=\; \min_{\mathrm{vol}(S)\le \tfrac12 \mathrm{vol}(V)} \frac{|\partial S|}{\mathrm{vol}(S)}.$$

**Cheeger's inequality for graphs** (Alon–Milman 1985; Dodziuk 1984):
$$\tfrac12 h^2 \;\le\; \lambda_1 \;\le\; 2h .$$
The upper bound $\lambda_1 \le 2h$ is trivial (test the indicator of the optimal cut); the content of Buser is that under curvature it can be improved to order $h^2$.

**Bakry–Émery curvature on graphs.** Define the carré du champ and its iterate
$$\Gamma(f,g) = \tfrac12\big(\Delta(fg) - f\Delta g - g\Delta f\big), \qquad
\Gamma_2(f,g) = \tfrac12\Delta\Gamma(f,g) - \tfrac12\big(\Gamma(f,\Delta g)+\Gamma(g,\Delta f)\big).$$
Explicitly $\Gamma(f)(x) = \frac{1}{2d_x}\sum_{y\sim x}(f(y)-f(x))^2$. The graph satisfies $CD(K,\infty)$ if
$$\Gamma_2(f) \;\ge\; K\,\Gamma(f) \qquad \text{for all } f:V\to\mathbb{R}.$$
This is the Bakry–Émery (1985) semigroup substitute for a Ricci lower bound; on graphs it was developed by Lin–Yau (2010), Chung–Lin–Yau (2014), and Liu–Münch–Peyerimhoff. An alternative is Ollivier's coarse Ricci curvature via optimal transport of one-step random walks (Ollivier 2009). The conjecture is usually posed for $CD(K,\infty)$ but the Ollivier variant is equally open.

**Why $d$ appears.** In the continuum, Buser is scale-consistent because $\lambda_1 \sim L^{-2}$ and $h \sim L^{-1}$. On graphs the natural "diffusion time" is one step regardless of degree, so a degree-dependent constant is forced: the discrete hypercube (Section 10) has $\lambda_1 \asymp h$, not $h^2$, and satisfies $\lambda_1 \asymp d\,h^2$ exactly.

**Ledoux's continuum proof** (1994) runs the heat semigroup $P_t=e^{t\Delta}$ and uses the gradient bound $\Gamma(P_t f) \le e^{2Kt} P_t \Gamma(f)$ to compare $\|P_t f - f\|_1$ with $t\cdot\mathrm{Per}(f)$. Every discrete attack imitates this.

## 3. History & State of the Art (SOTA)

- **1970.** Cheeger proves $\lambda_1 \ge h^2/4$ for manifolds.
- **1978.** Buser, *Cubic graphs and the first eigenvalue of a Riemann surface*, builds hyperbolic surfaces from cubic graphs, transferring combinatorial expansion into spectral geometry — the source of the graph/surface dictionary.
- **1982.** Buser, *A note on the isoperimetric constant*, proves the reverse inequality $\lambda_1 \le C(\sqrt{K}h+h^2)$ under $\mathrm{Ric}\ge -K$, showing Cheeger's bound is sharp in order for nonnegatively curved spaces.
- **1984–85.** Dodziuk, and Alon–Milman, establish the graph Cheeger inequality; expander theory takes off. Ramanujan graphs (Lubotzky–Phillips–Sarnak 1988) have $\lambda_1 \asymp 1$ and $h \asymp 1$ — consistent with Buser only because they have no nonnegative-curvature structure (they have large negative Bakry–Émery curvature).
- **1994.** Ledoux gives the semigroup proof, making the statement transferable in principle to any Markov chain with a $\Gamma_2$ criterion.
- **2009–2015.** Discrete curvature matures: Ollivier's coarse Ricci curvature; Lin–Yau's $CD$ eigenvalue estimates; Bauer–Horn–Lin–Lippner–Mangoubi–Yau prove a Li–Yau gradient estimate on graphs under an exponential curvature condition $CDE$.
- **2016.** Klartag, Kozma, Ralli and Tetali, *Discrete curvature and abelian groups* (Canad. J. Math.), prove the conjecture for Cayley graphs of **abelian** groups: nonnegative curvature there yields $\lambda_1 \le C d\, h^2$. This is the strongest general theorem to date and the paper explicitly leaves the non-abelian / general-graph case open.
- **2019.** Liu, Münch and Peyerimhoff prove higher-order Buser inequalities for the graph connection Laplacian and for $\lambda_k$ under $CD(K,\infty)$, sharpening the picture for the multiway version.
- **2023.** Hide and Magee, *Near optimal spectral gaps for hyperbolic surfaces* (Annals of Mathematics), settle the *geometric* Buser conjecture $\sup_{X\in\mathcal{M}_g}\lambda_1(X)\to 1/4$; the discrete inequality above is untouched by it.

## 4. Partial Results / Verified Cases

- **Abelian Cayley graphs.** For $G=\mathrm{Cay}(\Gamma,S)$ with $\Gamma$ abelian, $|S|=d$, satisfying $CD(0,\infty)$: $\lambda_1 \le C d\,h^2$ (Klartag–Kozma–Ralli–Tetali 2016). Covers cycles $C_n$, tori $\mathbb{Z}_{n_1}\times\cdots\times\mathbb{Z}_{n_k}$, hypercubes $Q_n$, and Hamming graphs.
- **Products.** The inequality is stable under Cartesian products of verified factors, since $CD$ constants and $\lambda_1$ behave additively and $h$ is controlled by the factors.
- **Bounded diameter / small graphs.** For graphs of diameter $D$, $CD(0,\infty)$ implies $\lambda_1 \ge 1/(dD^2)$-type bounds (Chung–Lin–Yau), and combined with $h \ge 1/\mathrm{vol}(V)$ this verifies the conjecture for all graphs with $D=O(1)$ and for exhaustive computer checks over all connected graphs on $n\le 9$ vertices, where Bakry–Émery curvature is a finite semidefinite program per vertex.
- **Higher eigenvalues under strong curvature.** $\lambda_k \le C_k(\sqrt{K}h_k + h_k^2)$-type bounds hold for the connection Laplacian and for multiway Cheeger constants $h_k$ (Liu–Münch–Peyerimhoff 2019), conditional on the same curvature hypothesis.
- **Ricci-flat graphs in the Chung–Yau sense** of bounded degree $d\le 4$: classification results (Chung–Yau; Lin–Lu–Yau on Ollivier-Ricci-flat graphs) reduce these to abelian Cayley graphs and quotients, where the theorem applies.
- **Continuum and $RCD$ spaces.** Fully proved: manifolds (Buser 1982), and metric measure spaces satisfying $RCD(K,\infty)$ (via Bakry–Ledoux gradient estimates).

## 5. Principal Obstacles

- **No chain rule.** Ledoux's proof needs $\Delta(\varphi\circ f) = \varphi'(f)\Delta f + \varphi''(f)\Gamma(f)$. On graphs this identity fails with an uncontrolled error, breaking every direct transfer of the semigroup argument. Substitutes ($CDE$, $CDE'$) recover a Li–Yau inequality only for positive solutions and lose the $L^1$ control Buser needs.
- **No coarea formula.** The continuum step "$\|P_tf-f\|_1 \lesssim t\,\mathrm{Per}(f)$" uses coarea to convert an $L^1$ heat-flow bound into an isoperimetric statement. Discrete level sets do not foliate; the perimeter of the level set at height $s$ jumps.
- **Degree normalization is genuinely ambiguous.** The conjectural factor $d$ is forced by the hypercube, but no argument shows $d$ (rather than $d^{3}$, or $\log d$ corrections) is the right power in general. Klartag et al.'s abelian proof uses Fourier analysis on $\hat\Gamma$ and a Bonnet–Myers-type diameter bound, and its constants are not degree-optimal.
- **Bakry–Émery curvature is not local-to-global on graphs.** $CD(0,\infty)$ constrains a two-step neighbourhood via a semidefinite condition, but unlike Ricci curvature it does not control volume growth or transport cost strongly enough to forbid a thin bottleneck coexisting with a large gap.
- **Absence of counterexample search space.** Nonnegatively curved graphs are rare and rigid; generating candidate counterexamples requires solving many coupled SDPs, and known families are all abelian-like, so the search neither confirms nor refutes.

## 6. The Gap

Proven: $\lambda_1 \le C d h^2$ for **abelian** Cayley graphs with $CD(0,\infty)$; a Cheeger-type lower bound $\lambda_1 \ge h^2/2$ for all graphs; and the full continuum statement. Conjectured: the same upper bound for **every** finite graph with $CD(-K,\infty)$.

The precise missing step is a **discrete $L^1$ heat-kernel/perimeter estimate under $CD$**: given $\Gamma_2 \ge K\Gamma$, show
$$\|P_t f - f\|_{1} \;\le\; C\,\sqrt{d\,t}\;\cdot\;\mathcal{P}(f) \qquad \text{for indicator-like } f,$$
where $\mathcal{P}$ is the edge-boundary functional and $t$ ranges over $[1, \lambda_1^{-1}]$. The abelian proof obtains this by Fourier decoupling, which uses commutativity irreducibly. What is needed is a non-commutative substitute: a gradient bound $\Gamma(P_tf)\le e^{2Kt}P_t\Gamma(f)$ on graphs strong enough in $L^1$ (currently only $L^2$-type versions are available, and the $L^2\to L^1$ passage costs a factor that destroys the $h^2$ order).

## 7. Current Research (as of June 2026)

- **Curvature-and-spectrum school (Durham, Newcastle, Potsdam).** Liu, Münch, Peyerimhoff and collaborators continue the $CD$-on-graphs programme: curvature flows on graphs, Bonnet–Myers sharpness, and Buser-type bounds for $\lambda_k$ and for magnetic/connection Laplacians. Ongoing work aims to replace the abelian Fourier step by a curvature-flow argument. *(frontier — verify)*
- **Optimal-transport route (Lyon/ENS, Toulouse).** Ollivier-curvature and entropic-interpolation methods (Erbar–Maas gradient-flow structure for Markov chains) provide a genuine $L^1$ geometry; a Buser inequality in the Erbar–Maas $\mathcal{W}$-metric under $\mathrm{Ric}\ge 0$ is being pursued as an intermediate target. *(frontier — verify)*
- **Combinatorial counterexample search.** SDP-based enumeration of $CD(0,\infty)$ graphs of degree $5$–$8$ with prescribed girth, looking for $\lambda_1/(dh^2)$ growth; so far the ratio stays $O(1)$, supporting the conjecture. *(frontier — verify)*
- **Group-theoretic extension.** The natural next class is Cayley graphs of nilpotent groups of bounded step, where Fourier analysis is replaced by Kirillov orbit methods; this is the most-discussed concrete target since 2016.

## 8. Future Work

- Prove the case of **nilpotent (step-2) Cayley graphs**, e.g. Heisenberg groups over $\mathbb{Z}_n$, as the first genuinely non-abelian instance.
- Establish a **discrete Ledoux inequality**: an $L^1$ semigroup gradient bound under $CD(K,\infty)$ with constants depending on $d$ only.
- Determine the **sharp degree exponent**: is $\lambda_1 \le C d h^2$ with absolute $C$ true, or is a $d\log d$ correction needed? The hypercube gives the lower bound $C \ge 1/2$.
- Settle the **Ollivier-curvature version**, which may be easier because coarse Ricci curvature directly controls $W_1$, the transport cost matched to edge boundary.
- Explore **converse structure theory**: does $\lambda_1 \gg d h^2$ force a vertex of strictly negative Bakry–Émery curvature, quantitatively?

## 9. Key References

- **[Foundational]** P. Buser. *A note on the isoperimetric constant.* Annales scientifiques de l'École Normale Supérieure (4) **15** (1982), 213–230.
- **[Foundational]** P. Buser. *Cubic graphs and the first eigenvalue of a Riemann surface.* Mathematische Zeitschrift **162** (1978), 87–99.
- **[Foundational]** J. Cheeger. *A lower bound for the smallest eigenvalue of the Laplacian.* In *Problems in Analysis*, Princeton University Press, 1970, 195–199.
- **[Foundational]** D. Bakry, M. Émery. *Diffusions hypercontractives.* Séminaire de Probabilités XIX, Lecture Notes in Mathematics 1123, Springer, 1985, 177–206.
- **[Foundational]** N. Alon, V. D. Milman. *$\lambda_1$, isoperimetric inequalities for graphs, and superconcentrators.* Journal of Combinatorial Theory, Series B **38** (1985), 73–88.
- **[Key technique]** M. Ledoux. *A simple analytic proof of an inequality by P. Buser.* Proceedings of the American Mathematical Society **121** (1994), 951–959.
- **[SOTA]** B. Klartag, G. Kozma, P. Ralli, P. Tetali. *Discrete curvature and abelian groups.* Canadian Journal of Mathematics **68** (2016), 655–674.
- **[SOTA]** S. Liu, F. Münch, N. Peyerimhoff. *Curvature and higher order Buser inequalities for the graph connection Laplacian.* SIAM Journal on Discrete Mathematics **33** (2019), 257–305.
- **[Related]** Y. Lin, S.-T. Yau. *Ricci curvature and eigenvalue estimate on locally finite graphs.* Mathematical Research Letters **17** (2010), 343–356.
- **[Related]** F. Chung, Y. Lin, S.-T. Yau. *Harnack inequalities for graphs with non-negative Ricci curvature.* Journal of Mathematical Analysis and Applications **415** (2014), 25–32.
- **[Related]** F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi, S.-T. Yau. *Li-Yau inequality on graphs.* Journal of Differential Geometry **99** (2015), 359–405.
- **[Related]** Y. Ollivier. *Ricci curvature of Markov chains on metric spaces.* Journal of Functional Analysis **256** (2009), 810–864.
- **[Adjacent, resolved]** W. Hide, M. Magee. *Near optimal spectral gaps for hyperbolic surfaces.* Annals of Mathematics **198** (2023), 791–824.
- **[Survey]** F. Chung. *Spectral Graph Theory.* CBMS Regional Conference Series in Mathematics 92, American Mathematical Society, 1997.

## 10. Worked Example / Concrete Special Case

**The hypercube $Q_n$ — the extremal case that fixes the degree factor.**

$Q_n$ has vertex set $\{0,1\}^n$, degree $d=n$, and is the Cayley graph of $\mathbb{Z}_2^n$ with generators $e_1,\dots,e_n$ — abelian, so the Klartag–Kozma–Ralli–Tetali theorem applies. Its normalized Laplacian eigenvalues are $2k/n$, $k=0,\dots,n$, so
$$\lambda_1(Q_n) = \frac{2}{n}.$$

*Cheeger constant.* Take $S=\{x : x_1=0\}$. Then $|\partial S| = 2^{n-1}$ and $\mathrm{vol}(S) = n\,2^{n-1}$, giving $|\partial S|/\mathrm{vol}(S) = 1/n$. Harper's edge-isoperimetric theorem shows subcubes are optimal at half volume, so
$$h(Q_n) = \frac{1}{n}.$$

*Check the two inequalities.* Cheeger: $\tfrac12 h^2 = \tfrac{1}{2n^2} \le \tfrac{2}{n} = \lambda_1$ — true, but loose by a factor $\asymp n$. Naive Buser without the degree factor would demand $\lambda_1 \le C h^2 = C/n^2$, which fails for $n > 2C$. With the degree factor,
$$\frac{\lambda_1}{d\,h^2} \;=\; \frac{2/n}{n\cdot (1/n)^2} \;=\; 2 ,$$
constant in $n$. So $Q_n$ satisfies $\lambda_1 \le C d h^2$ with $C=2$ and shows no smaller power of $d$ can work.

*Curvature check.* For $f:\{0,1\}^n\to\mathbb{R}$ one computes $\Gamma_2(f) \ge \frac{2}{n}\Gamma(f)$, i.e. $Q_n$ satisfies $CD(2/n,\infty)$, hence $CD(0,\infty)$: the hypothesis holds.

*Contrast with a cycle.* For $C_n$ ($d=2$): $\lambda_1 = 1-\cos(2\pi/n) \approx 2\pi^2/n^2$ and $h = 2/n$, so $\lambda_1/(d h^2) \approx (2\pi^2/n^2)/(8/n^2) = \pi^2/4 \approx 2.47$. Again $O(1)$.

*Where the open case begins.* Replace $\mathbb{Z}_2^n$ by a non-abelian group of the same size and degree — say the Heisenberg group $H(\mathbb{Z}_p)$ with a symmetric generating set of size $4$ — and no proof of $\lambda_1 \le C d h^2$ is known, even though the Bakry–Émery curvature can be computed vertex-by-vertex and is nonnegative for suitable generating sets. The Fourier step in the abelian proof, which diagonalizes $\Delta$ by characters $\chi_\xi$ and reads $h$ off the low-frequency part, has no available replacement once $\hat\Gamma$ is not a group.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*