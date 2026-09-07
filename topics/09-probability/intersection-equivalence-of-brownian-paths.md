---
id: 09-probability/intersection-equivalence-of-brownian-paths
title: "Intersection Equivalence of Brownian Paths"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Intersection Equivalence of Brownian Paths

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/intersection-equivalence-of-brownian-paths` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $B$ be standard Brownian motion in $\mathbb{R}^d$ started at a point of the open unit cube, and let $\mathcal{B} = B[0,\tau]$ be its trace up to exit from the cube. Let $\Gamma_d$ be the limit set of fractal (Mandelbrot) percolation on the dyadic subdivision of $[0,1]^d$ with retention parameter $p = 2^{2-d}$.

Two random closed sets $\Xi_1,\Xi_2 \subseteq U$ are **intersection-equivalent in $U$** if there are constants $0 < c \le C < \infty$, depending only on $U$ and the laws, with
$$c\,\mathbf{P}\{\Xi_2 \cap A \neq \emptyset\} \;\le\; \mathbf{P}\{\Xi_1 \cap A \neq \emptyset\} \;\le\; C\,\mathbf{P}\{\Xi_2 \cap A \neq \emptyset\}$$
for **every** closed $A \subseteq U$.

**Theorem (Peres, 1996).** For $d \ge 4$, $\mathcal{B}$ and $\Gamma_d$ are intersection-equivalent in $[0,1]^d$.

**The open problem.** (i) Is the same statement true for $d = 3$ (i.e. $p = 1/2$), where only the weaker *capacity-equivalence* is known? (ii) Is there an intersection-equivalent branching model for the space–time graph $\{(t,B_t)\}$, for $\alpha$-stable processes with $\alpha < 2$, and for multiparameter processes (the Brownian sheet, additive Brownian motion)? (iii) Can the constants be made explicit, or the ratio $C/c$ driven to $1$ under a scaling normalisation?

A complete resolution of (i) means either a coupling/comparison proof valid at $d=3$, or a closed set $A \subseteq [0,1]^3$ along a family for which the two hitting probabilities separate by an unbounded factor.

## 2. Mathematical Foundations

**Riesz kernels and capacity.** For $\alpha > 0$ and a closed $A \subseteq \mathbb{R}^d$,
$$\mathcal{E}_\alpha(\mu) = \iint |x-y|^{-\alpha}\,d\mu(x)\,d\mu(y), \qquad \operatorname{Cap}_\alpha(A) = \Big[\inf_{\mu \in \mathcal{P}(A)} \mathcal{E}_\alpha(\mu)\Big]^{-1}.$$
More generally, for a gauge $\phi$ (kernel $K_\phi(x,y)=\phi(|x-y|)$) write $\operatorname{Cap}_\phi$.

**Kakutani's criterion.** For $d \ge 3$ and $A$ compact,
$$\mathbf{P}\{B[0,\infty) \cap A \neq \emptyset\} > 0 \iff \operatorname{Cap}_{d-2}(A) > 0,$$
and quantitatively, with the Martin kernel $K(x,y)=G(x,y)/G(x_0,y)$ where $G(x,y)=c_d|x-y|^{2-d}$,
$$\tfrac{1}{2}\operatorname{Cap}_K(A) \le \mathbf{P}_{x_0}\{B \text{ hits } A\} \le \operatorname{Cap}_K(A)$$
(Benjamini–Pemantle–Peres, Martin capacity). Since $K(x_0,\cdot)$ is bounded above and below on $[0,1]^d$, hitting probability $\asymp \operatorname{Cap}_{d-2}$.

**Fractal percolation.** Subdivide $[0,1]^d$ dyadically; each level-$n$ cube is retained independently with probability $p$ given its parent is retained. Let $\Gamma = \bigcap_n \bigcup \{\text{retained level-}n\text{ cubes}\}$. Then $\mathbf{E}[\\#\text{level-}n\text{ survivors}] = (2^dp)^n$ and, conditioned on $\Gamma \ne \emptyset$, $\dim_H \Gamma = \log_2(2^dp)$ a.s. Choosing $p = 2^{2-d}$ gives $\dim_H \Gamma_d = d-(d-2) = 2$, matching $\dim_H \mathcal{B} = 2$.

**Lyons' tree criterion.** Identify $A \subseteq [0,1]^d$ with a subtree of the $2^d$-ary dyadic tree $T$. Percolation with parameter $p$ satisfies
$$\mathbf{P}\{\Gamma \cap A \neq \emptyset\} \asymp \operatorname{Cap}_{K_p}(A), \qquad K_p(\xi,\eta) = p^{-|\xi \wedge \eta|},$$
where $|\xi\wedge\eta|$ is the level of the last common ancestor. If $|x-y| \asymp 2^{-n}$ then $|\xi \wedge \eta| = n + O(1)$, so
$$K_p(\xi,\eta) \asymp 2^{n\log_2(1/p)} \asymp |x-y|^{-\log_2(1/p)}.$$
With $p = 2^{2-d}$ this is exactly the Riesz kernel of order $d-2$ — the same kernel Kakutani's theorem attaches to Brownian motion. Intersection equivalence is the assertion that this *kernel-level* coincidence is a genuine coincidence of hitting probabilities, uniformly over all closed $A$.

**Capacity-equivalence** (weaker): $\Xi_1 \equiv_{\mathrm{cap}} \Xi_2$ if for every gauge $\phi$, $\operatorname{Cap}_\phi(\Xi_1) > 0$ a.s. iff $\operatorname{Cap}_\phi(\Xi_2) > 0$ a.s. Intersection equivalence implies capacity equivalence; the converse fails.

## 3. History & State of the Art (SOTA)

- **1944–1957.** Kakutani links hitting to Newtonian capacity. Dvoretzky, Erdős and Kakutani prove double points exist in $\mathbb{R}^2,\mathbb{R}^3$ but not $\mathbb{R}^d$, $d\ge4$; with Taylor (1957) they show no triple points in $\mathbb{R}^3$ and points of all multiplicities in $\mathbb{R}^2$. The arithmetic $k(d-2)<d$ governing $k$-multiple points is the first hint of a branching mechanism.
- **1974–1988.** Mandelbrot introduces fractal percolation; Chayes–Chayes–Durrett establish its connectivity phase transition, making $\Gamma_d$ a tractable comparison object.
- **1990–1992.** Lyons' theory of percolation and capacity on trees supplies the exact tool: hitting probabilities of tree boundaries are capacities in an explicit kernel.
- **1996.** Peres proves intersection-equivalence of $\mathcal{B}$ and $\Gamma_d$ for $d \ge 4$ (*Comm. Math. Phys.* 177), and in a companion paper separates intersection-equivalence from capacity-equivalence.
- **1996.** Pemantle, Peres and Shapiro prove the trace of Brownian motion in $\mathbb{R}^3$ is *capacity-equivalent* to $[0,1]^2$ — the sharpest published $d=3$ statement, strictly weaker than intersection equivalence.
- **1999–2016.** The method is codified in Peres' St-Flour notes and in Lyons–Peres, *Probability on Trees and Networks*; Mörters–Peres, *Brownian Motion* (2010) gives a textbook treatment of the $d\ge4$ case.

## 4. Partial Results / Verified Cases

- **$d \ge 4$: fully solved.** Peres (1996): $\mathcal{B}$ and $\Gamma_d$ with $p = 2^{2-d}$ are intersection-equivalent in $[0,1]^d$. Constants depend on $d$ only.
- **$d = 3$: capacity-equivalence only.** $B[0,1]$ in $\mathbb{R}^3$ is capacity-equivalent to $[0,1]^2$ (Pemantle–Peres–Shapiro 1996). Hence $\operatorname{Cap}_{1}$ and $\mathbf{P}\{B \text{ hits } A\}$ still agree up to constants for *deterministic* $A$ by Kakutani/Martin capacity; what is missing is the pathwise branching representation.
- **$d \le 2$: false.** For $d=2$, $p = 2^{2-2} = 1$ makes $\Gamma_2 = [0,1]^2$, which hits every non-empty closed set, while planar Brownian motion misses singletons a.s.
- **Consequences established via the equivalence ($d \ge 4$).** Multiplicity criterion: $k$ independent traces intersect in $[0,1]^d$ with positive probability iff $k(d-2) < d$; Hausdorff dimension of $k$-fold intersections is $d - k(d-2)$ when positive; hitting criterion $\mathbf{P}\{\mathcal{B}\cap A \ne \emptyset\}>0 \iff \dim_H A > d-2$ for self-similar $A$.
- **Related families.** Symmetric $\alpha$-stable processes with $\alpha<d$ have hitting probability $\asymp \operatorname{Cap}_{d-\alpha}$, so the kernel matching goes through with $p = 2^{\alpha - d}$; a full intersection-equivalence theorem in that generality is stated for the transient regime but is not uniformly documented for $d - \alpha < 1$.
- **Multiparameter.** Fitzsimmons–Salisbury and Khoshnevisan–Xiao establish capacity/energy hitting criteria for $N$-parameter processes (kernel order $d - 2N$), the natural setting for an analogue, without a branching representation.

## 5. Principal Obstacles

- **Self-intersections destroy branching independence.** Peres' proof decomposes the path by dyadic cubes and treats the number of *distinct* level-$n$ cubes visited as a branching process; this requires that once the path leaves a cube it returns only with probability bounded away from $1$, uniformly. In $d \ge 4$ the path has no double points and excursions decouple. In $d = 3$ double points have dimension $1$ and the path re-enters cubes it has already visited on a non-negligible set of scales, so the offspring variables are neither independent nor stationary.
- **Capacity comparison is not enough.** Both objects have hitting probability comparable to $\operatorname{Cap}_{d-2}$, but the comparison constants from Lyons' theorem and from Martin capacity are two-sided only within a factor depending on the kernel's quasi-Bernoulli constants. Chaining two $\asymp$ statements gives intersection equivalence *for a fixed kernel*; the difficulty at $d=3$ is that the standard second-moment lower bound degrades because the second moment of the occupation measure of a small ball picks up the logarithmically divergent self-intersection contribution.
- **No conformal or Fourier handle.** The statement quantifies over *all* closed sets, so Fourier/Frostman methods that require regularity (Ahlfors–David, or fixed dimension) do not apply; the extremal $A$ can be a Cantor set of vanishing gauge.
- **Sharp constants are structurally out of reach.** The tree comparison loses a factor $2$ at every application of the Paley–Zygmund inequality, and the dyadic discretisation loses a factor depending on cube geometry; no known argument tracks these.

## 6. The Gap

Proven: an explicit branching model reproducing Brownian hitting probabilities up to constants, valid exactly when the path is *non-self-intersecting*, i.e. $d \ge 4$. Claimed: the same for $d = 3$.

The precise missing step is a **quasi-independent decomposition of the $\mathbb{R}^3$ path across dyadic scales in the presence of a dimension-one set of double points**. Concretely: one needs constants $c,C$ such that for all $n$ and all collections $\mathcal{Q}$ of level-$n$ cubes,
$$c\,\mathbf{P}\{\Gamma_3 \text{ meets } \mathcal{Q}\} \le \mathbf{P}\{B[0,\tau] \text{ meets } \mathcal{Q}\} \le C\,\mathbf{P}\{\Gamma_3 \text{ meets } \mathcal{Q}\}$$
uniformly in $n$. The upper bound follows from a first-moment/capacity argument; the **lower bound fails with current second-moment estimates**, because $\mathbf{E}[(\\#\text{visited cubes in } \mathcal{Q})^2]$ exceeds $(\mathbf{E}[\cdot])^2$ by a factor that current bounds do not close, exactly the self-intersection term. Either a new decoupling (perhaps via Brownian loop-soup or excursion decompositions) or a genuine counterexample at $d=3$ closes the gap.

## 7. Current Research (as of June 2026)

- **Israeli/US probability groups** (Peres and collaborators; Berkeley, Weizmann, Microsoft Research lineage) continue to use intersection equivalence as a black box for hitting problems: Brownian motion with drift, thick points, and Brownian survival among obstacles.
- **Loop soups and interlacements.** Sznitman's Brownian interlacements and the Brownian loop soup give alternative decompositions of the occupation field; adapting them to obtain a branching representation valid at $d=3$ is an active line *(frontier — verify)*.
- **Multiparameter and additive Lévy processes.** Khoshnevisan–Xiao's capacity framework for $N$-parameter processes has stimulated attempts at a "branching in $N$ directions" model; no intersection-equivalence theorem is published in that setting *(frontier — verify)*.
- **Random-environment analogues.** Intersection equivalence for random walks on supercritical percolation clusters and for Liouville Brownian motion has been raised as a test of robustness; the quenched hitting kernels are not known to be quasi-Bernoulli *(frontier — verify)*.

## 8. Future Work

- Prove or disprove the $d=3$ statement by controlling the double-point contribution to the second moment, e.g. via Le Gall's exact multiple-point measures.
- Replace $\Gamma_3$ by a *dependent* branching model (e.g. a branching random walk with attraction, or percolation with level-dependent $p_n$ tuned to self-intersection counts) for which equivalence at $d=3$ may hold; identify the minimal dependence needed.
- Establish intersection-equivalence for symmetric $\alpha$-stable traces uniformly in $\alpha \in (0,2]$, and quantify the constants' behaviour as $\alpha \uparrow d$.
- Develop a **quantitative** intersection equivalence: hitting probabilities agreeing to $1+o(1)$ for sets of small capacity, which would yield sharp asymptotics for Wiener-sausage type functionals.
- Extend to space–time: find the branching model intersection-equivalent to the graph $\{(t,B_t): t\in[0,1]\}$, whose Hausdorff dimension is $3/2$ in the parabolic metric.

## 9. Key References

- **[Foundational]** S. Kakutani. *Two-dimensional Brownian motion and harmonic functions.* Proc. Imp. Acad. Tokyo 20, 1944.
- **[Foundational]** A. Dvoretzky, P. Erdős, S. Kakutani. *Double points of paths of Brownian motion in $n$-space.* Acta Sci. Math. (Szeged) 12, 75–81, 1950.
- **[Foundational]** A. Dvoretzky, P. Erdős, S. Kakutani, S. J. Taylor. *Triple points of Brownian paths in 3-space.* Proc. Cambridge Philos. Soc. 53, 856–862, 1957.
- **[Foundational]** R. Lyons. *Random walks and percolation on trees.* Annals of Probability 18, 931–958, 1990.
- **[Foundational]** R. Lyons. *Random walks, capacity and percolation on trees.* Annals of Probability 20, 2043–2088, 1992.
- **[SOTA]** Y. Peres. *Intersection-equivalence of Brownian paths and certain branching processes.* Communications in Mathematical Physics 177, 417–434, 1996.
- **[SOTA]** Y. Peres. *Remarks on intersection-equivalence and capacity-equivalence.* Annales de l'Institut Henri Poincaré, Physique Théorique 64, 339–347, 1996.
- **[SOTA]** R. Pemantle, Y. Peres, J. W. Shapiro. *The trace of spatial Brownian motion is capacity-equivalent to the unit square.* Probability Theory and Related Fields 106, 379–399, 1996.
- **[SOTA]** I. Benjamini, R. Pemantle, Y. Peres. *Martin capacity for Markov chains.* Annals of Probability 23, 1332–1346, 1995.
- **[Foundational]** J. T. Chayes, L. Chayes, R. Durrett. *Connectivity properties of Mandelbrot's percolation process.* Probability Theory and Related Fields 77, 307–324, 1988.
- **[Foundational]** P. J. Fitzsimmons, T. S. Salisbury. *Capacity and energy for multiparameter Markov processes.* Annales de l'IHP Probabilités et Statistiques 25, 325–350, 1989.
- **[Survey]** Y. Peres. *Probability on trees: an introductory climb.* In: Lectures on Probability Theory and Statistics (École d'Été de St-Flour XXVII), Lecture Notes in Mathematics 1717, Springer, 1999.
- **[Survey]** R. Lyons, Y. Peres. *Probability on Trees and Networks.* Cambridge University Press, 2016.
- **[Survey]** P. Mörters, Y. Peres. *Brownian Motion.* Cambridge University Press, 2010.
- **[Survey]** D. Khoshnevisan. *Multiparameter Processes: An Introduction to Random Fields.* Springer, 2002.
- **[Survey]** G. F. Lawler. *Intersections of Random Walks.* Birkhäuser, 1991.

## 10. Worked Example / Concrete Special Case

**Recovering the multiple-point criterion in $d = 4$.**

Take $d = 4$, so $p = 2^{2-4} = 1/4$ and the dyadic tree is $2^4 = 16$-ary. Mean offspring: $16 \cdot \tfrac14 = 4 = 2^2$, so $\dim_H \Gamma_4 = \log_2 4 = 2 = \dim_H \mathcal{B}$. ✓

*Check on a single small cube.* Let $Q$ be a fixed dyadic cube of side $2^{-n}$ inside $[0,1]^4$. Then
$$\mathbf{P}\{\Gamma_4 \cap Q \neq \emptyset\} = p^{\,n} = 4^{-n},$$
since $Q$ survives iff each of its $n$ ancestors is retained. For Brownian motion started at distance $\asymp 1$, Kakutani gives
$$\mathbf{P}\{\mathcal{B} \cap Q \neq \emptyset\} \asymp \operatorname{Cap}_{d-2}(Q) = \operatorname{Cap}_2(Q) \asymp (2^{-n})^{d-2} = 4^{-n}.$$
The two agree up to a constant, as intersection equivalence demands.

*$k$ independent copies.* Let $\Gamma^{(1)},\dots,\Gamma^{(k)}$ be independent copies of $\Gamma_d$ on the same dyadic tree. A level-$n$ cube survives in all $k$ iff it survives each independently: the intersection is again fractal percolation with parameter $p^k = 2^{k(2-d)}$. Its mean offspring number is
$$2^d p^k = 2^{\,d - k(d-2)},$$
so $\Gamma^{(1)} \cap \cdots \cap \Gamma^{(k)} \neq \emptyset$ with positive probability iff $2^d p^k > 1$, i.e.
$$\boxed{\,k(d-2) < d\,}$$
and then the intersection has dimension $d - k(d-2)$.

*Numbers.* $d=4$, $k=2$: $k(d-2) = 4 = d$ — critical, so two independent Brownian paths in $\mathbb{R}^4$ do not intersect (matching Dvoretzky–Erdős–Kakutani). $d=3$, $k=2$: $2 < 3$ — they intersect, in a set of dimension $1$. $d=3$, $k=3$: $3 = 3$ — critical, no triple points in $\mathbb{R}^3$ (Dvoretzky–Erdős–Kakutani–Taylor). $d=5$, $k=2$: $6 > 5$ — no intersection.

By intersection equivalence (valid for $d \ge 4$), the branching computation transfers verbatim to Brownian traces: a one-line offspring count replaces the delicate 1950s multiple-point analysis. At $d = 3$ the same arithmetic gives the right answers, but the transfer theorem justifying it is precisely what is not proven.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*