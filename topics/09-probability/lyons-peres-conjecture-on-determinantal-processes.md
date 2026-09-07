---
id: 09-probability/lyons-peres-conjecture-on-determinantal-processes
title: "Lyons-Peres Conjecture for Determinantal Point Processes"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lyons-Peres Conjecture for Determinantal Point Processes

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/lyons-peres-conjecture-on-determinantal-processes` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $H$ be a closed subspace of $L^2(E,\mu)$ whose orthogonal projection operator $K$ is locally trace class with a reproducing kernel $K(x,y)$, and let $\mathcal{X}$ be a random configuration sampled from the determinantal point process (DPP) $\mathbb{P}_K$ governed by $K$. Write $K_x := K(\cdot,x) \in H$.

**Conjecture (Lyons–Peres, completeness).** For every such $H$,
$$\mathbb{P}_K\Big[\ \overline{\operatorname{span}}\,\{K_x : x \in \mathcal{X}\} = H \ \Big] = 1 .$$

Equivalently, since $f(x) = \langle f, K_x\rangle$ for $f \in H$: almost every sampled configuration is a **uniqueness set** for $H$ — the only $f \in H$ vanishing on all of $\mathcal{X}$ is $f \equiv 0$.

The same statement is conjectured in the discrete setting: $E$ countable, $H \subseteq \ell^2(E)$, $P = P_H$, $\mathfrak{S} \sim \mathbb{P}_H$, and the claim is that $\{P\delta_x\}_{x \in \mathfrak{S}}$ spans a dense subspace of $H$ almost surely.

A complete resolution requires either (a) a proof valid for **all** locally trace class Hermitian projections $K$, in both the discrete and continuous settings, or (b) an explicit $H$ together with a positive-probability event on which some nonzero $f \in H$ vanishes on the whole sample. Note the projection hypothesis is essential; for general contractions $0 \le K \le I$ the statement is false (e.g. $K = \tfrac12 I$ on a finite set).

## 2. Mathematical Foundations

**Configuration space.** $E$ a locally compact Polish space, $\mu$ a Radon measure, $\operatorname{Conf}(E)$ the space of locally finite subsets with the vague topology.

**Determinantal point process.** $\mathcal{X}$ is determinantal with kernel $K$ if its $n$-point correlation functions with respect to $\mu$ are
$$\rho_n(x_1,\dots,x_n) \;=\; \det\big[K(x_i,x_j)\big]_{i,j=1}^n .$$
**Macchi–Soshnikov theorem.** If $K$ is a self-adjoint, locally trace class operator on $L^2(E,\mu)$ with $0 \preceq K \preceq I$, then $\mathbb{P}_K$ exists and is unique.

**Projection case.** If $K = K^2 = K^*$ with range $H$, then for $f \in H$, $f(x)=\int_E K(x,y)f(y)\,d\mu(y)$, so $H$ is a reproducing kernel Hilbert space with kernel $K(x,y) = \langle K_y, K_x\rangle$. The expected number of points in $B$ is $\int_B K(x,x)\,d\mu(x) = \operatorname{tr}(\mathbb{1}_B K \mathbb{1}_B)$; if $\dim H = n < \infty$ then $|\mathcal{X}| = n$ almost surely, since the generating functional gives $\mathbb{E}[z^{|\mathcal X|}]=\det(I+(z-1)K)=z^n$.

**Discrete case and matroids.** For $H \subseteq \ell^2(E)$ with $\dim H = r < \infty$,
$$\mathbb{P}_H[\mathfrak{S}=S] \;=\; \det\big[P(x,y)\big]_{x,y \in S}, \qquad |S| = r,$$
which is nonzero exactly when $\{P\delta_x\}_{x\in S}$ is a basis of $H$ — i.e. $\mathfrak{S}$ is a uniformly-weighted random base of the represented matroid. Uniform spanning trees and forests are the canonical instance ($H = $ the cycle space's orthogonal complement, the star space).

**Related structural facts the conjecture leans on.**
- *Tail triviality*: $\mathbb{P}_K$ has trivial tail $\sigma$-field for Hermitian $K$ (Lyons 2003 discrete; Lyons 2018, Osada–Osada, Bufetov–Qiu–Shamov in general). Hence completeness is a $0$–$1$ event only after checking measurability and tail-invariance — the completeness event is *not* tail-measurable in general, which is precisely the difficulty.
- *Number rigidity* (Ghosh, Ghosh–Peres): for the sine and Ginibre processes, the point count in a bounded set is measurable with respect to the configuration outside it.
- *Conditional measures*: the conditional law of $\mathcal{X}\cap B$ given $\mathcal{X}\setminus B$ is again determinantal, with kernel the projection onto
$$H(\mathcal{X}\setminus B) \;=\; \{f \in H : f|_{\mathcal{X}\setminus B} = 0\}.$$
The conjecture is exactly the statement that $H(\mathcal{X}) = \{0\}$.

## 3. History & State of the Art (SOTA)

- **1975.** Macchi introduces fermion processes; Soshnikov's 2000 survey and Shirai–Takahashi's work establish the general existence and structure theory.
- **2003.** Lyons, *Determinantal probability measures* (Publ. IHES 98), builds the exterior-algebra/matroid framework, proves negative association, stochastic domination and tail triviality in the discrete case. The completeness question is implicit here in the guise of "is the sample a spanning set?".
- **2006–2009.** Hough–Krishnapur–Peres–Virág give the algorithmic sampling proof (a DPP with projection kernel is a sum of independent Bernoulli-type conditional draws), which is the main constructive tool for completeness proofs.
- **2014.** Lyons, *Determinantal probability: basic properties and conjectures* (ICM Seoul), states the conjecture explicitly with Peres, in both discrete and continuous form. It is restated in Lyons–Peres, *Probability on Trees and Networks* (2016).
- **2015.** Ghosh proves the sine-kernel case: random exponentials at the points of the $\operatorname{sinc}$ process are complete in $L^2[-\pi,\pi]$, and the completeness is critical.
- **2016–2017.** Bufetov proves rigidity for Airy, Bessel and Gamma kernels; Bufetov–Qiu handle DPPs from Hilbert spaces of holomorphic functions.
- **2021.** Bufetov–Qiu–Shamov, *Kernels of conditional determinantal measures and the Lyons–Peres completeness conjecture* (JEMS 23), identify the conditional kernel as the projection onto $H(\mathcal{X}\setminus B)$ and deduce the conjecture for a large class of kernels, including all the classical integrable ones. This is the current SOTA and the reason the status here is *partially-solved*.

## 4. Partial Results / Verified Cases

| Class | Status | Source |
|---|---|---|
| $\dim H = n < \infty$ (discrete or continuous) | **Proved**, elementary: $\vert\mathcal X\vert = n$ a.s. and every atom of the law is a basis | Lyons 2003 |
| Uniform spanning trees of finite graphs | **Proved** (special case of above) | Lyons–Peres 2016 |
| Sine kernel $\frac{\sin\pi(x-y)}{\pi(x-y)}$ on $\mathbb{R}$, i.e. $H=PW_\pi$ | **Proved**; completeness is critical (deleting one point destroys it) | Ghosh, PTRF 2015 |
| Ginibre ensemble on $\mathbb{C}$, $H = $ Fock–Bargmann space | **Proved** | Ghosh–Peres 2017; Bufetov–Qiu 2017 |
| Airy, Bessel, Gamma kernels | **Proved** | Bufetov 2016; Bufetov–Qiu–Shamov 2021 |
| DPPs from Hilbert spaces of holomorphic functions on $\mathbb{C}$ or the disc (weighted Bergman, generalized Ginibre) | **Proved** | Bufetov–Qiu, CMP 2017 |
| Translation-invariant kernels on $\mathbb{R}$ / $\mathbb{Z}$ with spectral density $\mathbb{1}_S$ | **Proved** for the classical cases; general $S$ *(frontier — verify)* | Bufetov–Qiu–Shamov 2021 |
| General Hermitian projection, $\dim H = \infty$ | **Open** | — |

## 5. Principal Obstacles

- **Completeness is not a tail event.** Tail triviality — the strongest general structural theorem available — does not apply, because a witness $f \in H(\mathcal{X})$ can be destroyed by adding or removing finitely many points. So the $0$–$1$ law that trivialises most global DPP questions gives nothing here.
- **No general quantitative uniqueness theory.** Proofs in the verified cases all import external analytic input: Beurling–Malliavin / Levinson–Kadec theory of uniqueness sets for Paley–Wiener spaces (sine kernel), or Jensen-type estimates on zero counting for entire functions of finite order (Ginibre, Bergman). For an abstract RKHS $H$ there is no notion of "density of a uniqueness set", and no substitute for a growth/order hypothesis.
- **Rigidity is not available in general.** The Bufetov–Qiu–Shamov conditional-kernel machinery converts completeness into a statement about $H(\mathcal{X}\setminus B)$, but to run it one needs enough control (rigidity, or explicit integrable structure) to show the conditional kernel is a *projection of the right rank*. Rigidity itself is known only for restricted classes and fails for e.g. many Bergman-type processes.
- **Sampling algorithms lose the linear structure.** The HKPV algorithm removes one dimension of $H$ per sampled point, but the residual subspace depends on the already-drawn points in a way that is not stationary; controlling the limit of the nested subspaces $H \supset H_1 \supset \cdots$ requires exactly the completeness one is trying to prove.
- **Criticality.** In the sine-kernel case the system is complete but has zero "excess": there is no slack to absorb error terms, so perturbative or comparison arguments (stochastic domination between DPPs, Lyons 2003) cannot transfer completeness from one kernel to another.

## 6. The Gap

Section 4 covers kernels with *integrable structure*: $K(x,y) = \frac{\sum_i f_i(x)g_i(y)}{x-y}$ or reproducing kernels of spaces of entire/holomorphic functions, where zero sets are governed by classical function theory. Section 1 asks about an arbitrary locally trace class Hermitian projection on an arbitrary Polish $E$.

The precise missing step: given only $K = K^2 = K^*$, show that
$$\mathbb{P}_K\big[\,H(\mathcal{X}) \neq \{0\}\,\big] = 0,$$
without assuming (i) number rigidity, (ii) an integrable or holomorphic representation of $K$, or (iii) a transitive symmetry group acting on $E$. Even a *soft* dichotomy — that $\dim H(\mathcal{X})$ is a.s. constant and equal to $0$ or $\infty$ — is not known in general. The discrete infinite-rank case (e.g. $H$ the star space of an infinite graph, where the conjecture asserts the wired uniform spanning forest's edge set spans the star space) is a fully combinatorial special case that remains open and would be the natural first target.

## 7. Current Research (as of June 2026)

- **Aix-Marseille / Steklov (Bufetov and collaborators):** extensions of the conditional-kernel description to non-projection kernels and to quasi-invariance/Palm-equivalence questions; the "kernel of the conditional measure" identity is the main engine.
- **Fudan / Chinese groups (Qiu and coauthors):** completeness and rigidity for DPPs on Hilbert spaces of holomorphic functions with general weights; the borderline between rigidity and non-rigidity as a function of the weight's growth *(frontier — verify)*.
- **Indian Statistical Institute / NUS (Ghosh and coauthors):** rigidity hierarchies, "critical completeness" and quantitative uniqueness-set thresholds for perturbed sine processes.
- **Lyons' school (Indiana):** the discrete/matroidal side — uniform spanning forests, tree-entropy, and whether the WUSF sample spans the star space of an infinite transitive graph.
- **Techniques gaining traction:** Shamov's Gaussian/quasi-free-state representation of DPPs, which recasts completeness as a statement about the zero set of a random field; and transference of Beurling–Malliavin density arguments to de Branges spaces.

## 8. Future Work

- Prove the **discrete infinite-rank case** first; a matroid-theoretic or spanning-forest argument might avoid function theory entirely.
- Establish a general **$0$–$\infty$ dichotomy** for $\dim H(\mathcal{X})$ via an ergodicity argument for group-invariant $K$; combine with a single-point tolerance estimate to exclude the $\infty$ branch.
- Develop an abstract notion of **stochastic uniqueness density** for RKHS, generalising Beurling–Malliavin, and test it against non-integrable kernels.
- Decide whether **rigidity implies completeness** in general, or produce a rigid-but-incomplete example.
- Search computationally for a counterexample among finitely-supported-spectrum kernels on $\mathbb{Z}$ where $H(\mathcal{X}) \neq \{0\}$ could be detected numerically.

## 9. Key References

- **[Foundational]** Russell Lyons. *Determinantal probability measures.* Publications Mathématiques de l'IHÉS, 98:167–212, 2003.
- **[Foundational]** Odile Macchi. *The coincidence approach to stochastic point processes.* Advances in Applied Probability, 7:83–122, 1975.
- **[Foundational]** Alexander Soshnikov. *Determinantal random point fields.* Russian Mathematical Surveys, 55(5):923–975, 2000.
- **[Conjecture source]** Russell Lyons. *Determinantal probability: basic properties and conjectures.* Proceedings of the International Congress of Mathematicians, Seoul, Vol. IV, 137–161, 2014.
- **[Book]** Russell Lyons with Yuval Peres. *Probability on Trees and Networks.* Cambridge University Press, 2016.
- **[Book]** J. Ben Hough, Manjunath Krishnapur, Yuval Peres, Bálint Virág. *Zeros of Gaussian Analytic Functions and Determinantal Point Processes.* American Mathematical Society, University Lecture Series 51, 2009.
- **[Survey]** J. Ben Hough, Manjunath Krishnapur, Yuval Peres, Bálint Virág. *Determinantal processes and independence.* Probability Surveys, 3:206–229, 2006.
- **[SOTA]** Alexander I. Bufetov, Yanqi Qiu, Alexander Shamov. *Kernels of conditional determinantal measures and the Lyons–Peres completeness conjecture.* Journal of the European Mathematical Society, 23(5):1477–1519, 2021.
- **[SOTA]** Subhroshekhar Ghosh. *Determinantal processes and completeness of random exponentials: the critical case.* Probability Theory and Related Fields, 163:643–665, 2015.
- **[SOTA]** Subhroshekhar Ghosh, Yuval Peres. *Rigidity and tolerance in point processes: Gaussian zeros and Ginibre eigenvalues.* Duke Mathematical Journal, 166(10):1789–1858, 2017.
- **[Related]** Alexander I. Bufetov. *Rigidity of determinantal point processes with the Airy, the Bessel and the Gamma kernel.* Bulletin of Mathematical Sciences, 6:163–172, 2016.
- **[Related]** Alexander I. Bufetov, Yanqi Qiu. *Determinantal point processes associated with Hilbert spaces of holomorphic functions.* Communications in Mathematical Physics, 351:1–44, 2017.
- **[Related]** Russell Lyons. *A note on tail triviality for determinantal point processes.* Electronic Communications in Probability, 23, paper 72, 2018.

## 10. Worked Example / Concrete Special Case

**Finite case: the uniform spanning tree of a triangle.** Let $E = \{1,2,3\}$ index the edges of $K_3$ and let
$$H = \{v \in \mathbb{R}^3 : v_1+v_2+v_3 = 0\}, \qquad \dim H = 2,$$
which is the orthogonal complement of the (one-dimensional) cycle space of the triangle. Its projection is
$$K \;=\; I - \tfrac13 J \;=\; \frac{1}{3}\begin{pmatrix} 2 & -1 & -1\\ -1 & 2 & -1\\ -1 & -1 & 2\end{pmatrix}.$$
Then $\mathbb{E}|\mathcal{X}| = \operatorname{tr} K = 2$, and for each pair,
$$\mathbb{P}[\mathcal{X} = \{1,2\}] = \det\begin{pmatrix} 2/3 & -1/3 \\ -1/3 & 2/3\end{pmatrix} = \tfrac49 - \tfrac19 = \tfrac13,$$
identically for $\{1,3\}$ and $\{2,3\}$, summing to $1$: the DPP is the uniform spanning tree (pick 2 of the 3 edges uniformly). On the event $\mathcal{X}=\{1,2\}$ the sampled reproducing kernels are the columns
$$K_1 = \tfrac13(2,-1,-1)^{\!\top}, \qquad K_2 = \tfrac13(-1,2,-1)^{\!\top},$$
which are linearly independent and lie in $H$, hence span $H$. The same holds for each of the three outcomes, so completeness holds with probability $1$ — as it must, since $|\mathcal{X}| = \dim H$ a.s. and non-bases carry zero determinant.

**Infinite case: the sine kernel.** Take $E=\mathbb{R}$, $\mu = $ Lebesgue, $H = PW_\pi$ (Fourier transforms of $L^2[-\pi,\pi]$), $K(x,y) = \frac{\sin\pi(x-y)}{\pi(x-y)}$. Here $K_x(\cdot) = \widehat{\mathbb{1}_{[-\pi,\pi]}e^{-ix\,\cdot}}$, so completeness of $\{K_x\}_{x\in\mathcal{X}}$ is exactly completeness of the random exponential system $\{e^{ixt}\}_{x \in \mathcal{X}}$ in $L^2[-\pi,\pi]$. The deterministic comparison is instructive: $\{e^{int}\}_{n\in\mathbb{Z}}$ is an orthogonal basis with zero excess, and deleting a single frequency makes it incomplete. The sine process has mean density $K(x,x) = 1$, i.e. the same density as $\mathbb{Z}$, so it sits exactly at the classical Levinson–Kadec threshold and no density argument decides the question. Ghosh (2015) proved completeness holds almost surely nonetheless, and that it is critical: removing one point of $\mathcal{X}$ destroys it — a direct reflection of the number rigidity of the sine process, where the count in an interval is determined by the outside configuration.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*