---
id: 07-combinatorics/danzers-problem
title: "Danzer's Problem on Dense Forests and Bounded Density Sets"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Danzer's Problem on Dense Forests and Bounded Density Sets

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/danzers-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Let $d \geq 2$. A set $Y \subset \mathbb{R}^d$ is a **Danzer set** if $Y \cap C \neq \emptyset$ for every convex body $C \subset \mathbb{R}^d$ (compact, convex, nonempty interior) with Lebesgue measure $\mathrm{vol}(C) = 1$.

**Danzer's problem (1965).** Does there exist a Danzer set $Y \subset \mathbb{R}^d$ of **bounded density**, i.e. with

$$N_Y(R) \;:=\; \\#\big(Y \cap [-R,R]^d\big) \;=\; O(R^d) \quad (R \to \infty)?$$

Two standard variants are used interchangeably in the literature; both are open.

- **(D1) Bounded density.** $N_Y(R) = O(R^d)$, no separation required.
- **(D2) Uniformly discrete.** $\inf\{\,\|y-y'\| : y \neq y' \in Y\,\} > 0$. This is Conway's "Dead Fly Problem", for which he offered \$1000: place flies at pairwise distance $\geq 1$ so that every convex region of area $1$ contains a fly.

(D2) $\Rightarrow$ (D1) up to constants, since a uniformly discrete set automatically satisfies $N_Y(R)=O(R^d)$; conversely a Danzer set of bounded density need not be separated. A complete solution is either an explicit construction (or existence proof) of such a $Y$ in some dimension $d \geq 2$, or a proof that every Danzer set satisfies $N_Y(R)/R^d \to \infty$.

Note the two trivial poles. Every $Y$ that is $\varepsilon$-dense for small $\varepsilon$ is Danzer but has density $\asymp \varepsilon^{-d}$ — finite but with no scaling gain; and every Danzer set has $N_Y(R) \geq c\,R^d$, since $[-R,R]^d$ contains $\asymp R^d$ disjoint unit-volume cubes. The whole content is the multiplicative gap between $R^d$ and the best known $R^d\log R$.

## 2. Mathematical Foundations

**Growth and density.** For $Y\subset\mathbb{R}^d$ define the upper density $\overline{d}(Y) = \limsup_{R\to\infty} N_Y(R)/(2R)^d$. Bounded density means $\overline{d}(Y)<\infty$. $Y$ is *relatively dense* if $\exists r$ with $Y + B(0,r) = \mathbb{R}^d$, and a *Delone set* if uniformly discrete and relatively dense.

**Reduction to the space of lattices.** Normalise: every convex body of volume $1$ is $gC_0 + v$ for some $g \in SL_d(\mathbb{R})$, $v\in\mathbb{R}^d$, and $C_0$ in the (compact, in Hausdorff metric modulo $SL_d(\mathbb{R})$) space of "shapes". Hence $Y$ is Danzer iff for every $g \in SL_d(\mathbb{R})$ the set $g^{-1}Y$ meets every translate of $C_0$, uniformly over shapes. The difficulty is that $SL_d(\mathbb{R})$ is noncompact: applying the diagonal flow $g_t = \mathrm{diag}(e^{t}, e^{-t/(d-1)},\dots)$ produces arbitrarily long, thin bodies of volume $1$, and $Y$ must hit all of them simultaneously.

**Why no lattice works.** If $\Lambda \subset \mathbb{R}^2$ is a lattice of covolume $1$, pick a primitive direction and a translate: the rectangle $Q_n = (0,n) \times (\delta, \delta + 1/n)$ has area $1$ and, for suitable $\delta$ and large $n$, contains no point of $\Lambda$. More generally, for any finite union of lattices the diagonal flow escapes to the cusp of $SL_d(\mathbb{Z})\backslash SL_d(\mathbb{R})$ and empty bodies appear.

**Dense forests (quantitative weakening).** A uniformly discrete $Y \subset \mathbb{R}^d$ is a **dense forest** with **visibility function** $\varepsilon(L)$ if every line segment $S$ of length $L$ satisfies

$$\mathrm{dist}(S, Y) \leq \varepsilon(L),\qquad \text{i.e.}\quad Y \cap S^{(\varepsilon(L))} \neq \emptyset,$$

where $S^{(\varepsilon)}$ is the $\varepsilon$-neighbourhood (a tube of volume $\asymp \varepsilon^{d-1}L$). A Danzer set of bounded density would give a dense forest with the optimal visibility $\varepsilon(L) \asymp L^{-1/(d-1)}$ (tube volume $\asymp 1$); conversely, volume-counting shows $\varepsilon(L) \geq c\,L^{-1/(d-1)}$ for every uniformly discrete set. So the forest problem is Danzer's problem restricted from all convex bodies to tubes around segments, and it is quantitatively calibrated by the same exponent.

**Bounded complexity.** For a Delone set $Y$, the *patch-counting function* $p_Y(r)$ counts translation-equivalence classes of $Y \cap B(x,r)$, $x\in\mathbb{R}^d$. $Y$ has *finite local complexity* if $p_Y(r)<\infty$ for all $r$, and *bounded complexity* if $p_Y(r)$ grows polynomially. Cut-and-project sets (model sets/quasicrystals), obtained by projecting the points of a lattice $\Lambda \subset \mathbb{R}^{d+m}$ lying in a strip $\mathbb{R}^d \times W$, are the canonical bounded-complexity examples.

## 3. History & State of the Art (SOTA)

- **1965.** Ludwig Danzer poses the question, in the context of Hlawka-style covering and Minkowski-type problems.
- **1971.** R. P. Bambah and A. C. Woods, *On a problem of Danzer* (Pacific J. Math.), give the first nontrivial construction: a Danzer set with growth $N_Y(R) = O(R^d \log R)$. This bound has not been improved in 55 years.
- **1991.** The problem is popularised in Croft–Falconer–Guy, *Unsolved Problems in Geometry*.
- **2000.** W. T. Gowers, *Rough structure and classification* (GAFA 2000 Special Volume), lists it among the problems illustrating the lack of structural tools for "geometric Ramsey" phenomena.
- **2011–2016.** The dense-forest relaxation is introduced (C. J. Bishop, IMRN 2011, on visibility in forests) and made quantitative by F. Adiceam, *How far can you see in a forest?* (IMRN 2016), using Diophantine approximation to build explicit forests.
- **2016.** Y. Solomon and B. Weiss, *Dense forests and Danzer sets* (Ann. Sci. ÉNS): construction of dense forests from homogeneous dynamics, plus the main structural obstruction — **no Danzer set has bounded complexity**, and in particular no cut-and-project set is Danzer.
- **2018.** N. Alon, *Uniformly discrete forests with poor visibility* (Combin. Probab. Comput.): a probabilistic construction of a dense forest in the plane with visibility $\varepsilon(L) = L^{-1+o(1)}$, essentially optimal.
- **2022.** Adiceam–Solomon–Weiss, *Cut-and-project quasicrystals, lattices, and dense forests* (J. London Math. Soc.): explicit polynomial visibility rates from quasicrystals.

**SOTA summary.** Upper bound on achievable growth: $O(R^d \log R)$. Lower bound: $\Omega(R^d)$. Both endpoints unmoved since 1971.

## 4. Partial Results / Verified Cases

- **Bambah–Woods (1971), all $d\geq 2$:** Danzer sets with $N_Y(R)=O(R^d\log R)$ exist, and can be taken uniformly discrete. The $\log R$ is exactly the number of dyadic scales of the diagonal flow visible inside $[-R,R]^d$.
- **Restricted shape families.** For **axis-parallel boxes only**, bounded-density solutions exist in $\mathbb{R}^2$: any *admissible* lattice $\Lambda$ (one with $\inf_{v\in\Lambda\setminus\{0\}} |v_1 v_2| > 0$, e.g. $\Lambda = \{(m+n\sqrt2,\;m-n\sqrt2)\}$) meets every axis-parallel rectangle of area at least some constant $C$. Density $O(R^2)$. The construction fails the moment rotations are admitted.
- **Dense forests, $d = 2$:** Alon (2018) achieves $\varepsilon(L) = L^{-1+o(1)}$ against the optimal $L^{-1}$; Adiceam (2016) and Adiceam–Solomon–Weiss (2022) give explicit (non-probabilistic) forests with rates such as $\varepsilon(L) = O(L^{-\alpha})$ for explicit $\alpha < 1$ depending on Diophantine data.
- **Negative results (classes ruled out).** No lattice, no finite union of lattices, no cut-and-project/model set, and more generally no Delone set of bounded patch complexity is Danzer (Solomon–Weiss 2016). Every Danzer set must therefore be "aperiodic and complicated" — its patch counting function grows superpolynomially.
- **Convex bodies of volume $\geq V$ for large $V$:** trivially solvable by a sufficiently coarse $\varepsilon$-net; the problem is genuinely about the *uniform* normalisation $\mathrm{vol}=1$ across all shapes and orientations.

## 5. Principal Obstacles

- **Noncompactness of $SL_d(\mathbb{R})$.** The family of unit-volume convex bodies is a noncompact orbit. Any construction tuned to a compact family of shapes fails at the cusp; the $\log R$ loss in Bambah–Woods is precisely the price of covering $\log R$ dyadic scales of eccentricity with independent point families. No known mechanism lets one point set serve two very different eccentricities at once.
- **Structure destroys the property; the property forbids structure.** Solomon–Weiss show bounded complexity is incompatible with being Danzer. But every explicit construction technique — lattices, substitution tilings, cut-and-project, Ostrowski/continued-fraction schemes — produces bounded complexity. The only known route to high complexity is randomness, and random constructions with density $O(R^d)$ leave a positive proportion of thin bodies empty (a second-moment/Poisson computation: a tube of volume $1$ is missed with probability $\approx e^{-\lambda}$, and there are infinitely many essentially independent shapes to miss).
- **Fourier analysis is the wrong tool.** Hitting *every* body is an $L^\infty$/covering statement, not an average one. Spectral methods control $\int |\widehat{\mu}|^2$ and give discrepancy on average over shapes; they cannot exclude a single bad body. Bounded-remainder and equidistribution theory (Skriganov, Rauzy) delivers exactly the average control that is insufficient here.
- **No lower-bound machinery.** There is no known method producing a superlinear-in-$R^d$ lower bound for an arbitrary set. Existing obstructions are all *structural* (they assume complexity bounds), not *metric*, so they say nothing about a hypothetical wild Danzer set.
- **Union bound over a continuum.** Even for the forest relaxation, directions form a continuum; chaining/net arguments over directions cost logarithms, which is exactly the quantity in dispute.

## 6. The Gap

Proven: growth $O(R^d \log R)$ is achievable (Bambah–Woods); growth $\Omega(R^d)$ is necessary; bounded-complexity sets are excluded. Wanted: decide the single logarithm.

Precisely, define
$$\gamma_d \;=\; \inf\Big\{\, \gamma : \exists \text{ Danzer } Y \subset \mathbb{R}^d \text{ with } N_Y(R) = O(R^d (\log R)^{\gamma}) \,\Big\}.$$
Known: $0 \leq \gamma_d \leq 1$. Unknown: whether $\gamma_d = 0$ and whether the infimum is attained ($\gamma_d = 0$ attained is exactly Danzer's problem). The step to be crossed is one of the following two:

1. **Construction.** Produce a set of superpolynomial patch complexity — hence not from any known algebraic scheme — that nevertheless hits all $\mathrm{vol}=1$ bodies with only $O(R^d)$ points. This requires a derandomisation-style object combining the "scale-coupling" of lattices with the complexity of randomness.
2. **Obstruction.** Prove a metric (complexity-free) lower bound $N_Y(R) \gg R^d \log R$, or even $\gg R^d\omega(R)$ for any $\omega\to\infty$. Nothing of this kind is known even for the tube/forest sub-problem.

## 7. Current Research (as of June 2026)

- **Homogeneous dynamics school (Weiss, Solomon, Adiceam, and collaborators; Hebrew University, Tel Aviv, Manchester/Bristol).** Encoding Danzer-type properties as non-divergence statements for orbits in $SL_d(\mathbb{Z})\backslash SL_d(\mathbb{R})$, and using Ratner/quantitative-nondivergence tools to bound how fast a construction must "spend" points across scales.
- **Diophantine forests.** Extending Adiceam–Solomon–Weiss to higher dimensions and to explicit forests with $\varepsilon(L)=O(L^{-1/(d-1)+o(1)})$ from badly approximable matrices. Some announced rates in $d\geq 3$ remain unrefereed *(frontier — verify)*.
- **Complexity lower bounds.** Attempts to convert the Solomon–Weiss bounded-complexity obstruction into a quantitative trade-off of the form "$p_Y(r) \leq \exp(r^{\beta})$ implies $N_Y(R) \gg R^d \log^{c} R$" *(frontier — verify)*.
- **Probabilistic/combinatorial constructions.** Post-Alon work on derandomising the poor-visibility forest and on discrepancy-theoretic analogues (Bansal-style partial-colouring applied to families of thin tubes) *(frontier — verify)*.
- **Discrete geometry community.** The problem is regularly listed in Oberwolfach and Discrete & Computational Geometry problem sessions; no claimed resolution has survived scrutiny.

## 8. Future Work

- **Interpolate the two variants.** Decide whether the bounded-density (D1) and uniformly discrete (D2) versions are genuinely equivalent; a separation would indicate where the difficulty lives.
- **Weaken the shape family monotonically.** Determine the largest $SL_d(\mathbb{R})$-invariant family of shapes for which a bounded-density hitting set exists — boxes (solved, axis-parallel), boxes with rotations (open), tubes (forest problem), all convex bodies. Mapping this hierarchy is the most concrete programme available.
- **Quantify the complexity barrier.** Prove a theorem of the form: growth $O(R^d)$ forces patch complexity $\geq \exp(cr^d)$, then look for a contradiction with a covering argument.
- **Attack $\gamma_d$ for large $d$.** As $d$ grows, the shape space is larger but concentration is stronger; it is not known whether the problem is easier or harder in high dimension — a monotonicity result in $d$ would itself be new.
- **Effective versions.** Even a Danzer set with growth $O(R^d \log\log R)$ would be a breakthrough, breaking the 1971 barrier without solving the problem.

## 9. Key References

- **[Foundational]** R. P. Bambah, A. C. Woods. *On a problem of Danzer.* Pacific Journal of Mathematics, 37(2):295–301, 1971.
- **[Foundational]** H. T. Croft, K. J. Falconer, R. K. Guy. *Unsolved Problems in Geometry.* Springer-Verlag, Problem Books in Mathematics, 1991.
- **[SOTA]** Y. Solomon, B. Weiss. *Dense forests and Danzer sets.* Annales Scientifiques de l'École Normale Supérieure, 49(5):1053–1074, 2016.
- **[SOTA]** N. Alon. *Uniformly discrete forests with poor visibility.* Combinatorics, Probability and Computing, 27(4):442–448, 2018.
- **[SOTA]** F. Adiceam. *How far can you see in a forest?* International Mathematics Research Notices, 2016(16):4867–4881, 2016.
- **[SOTA / Recent]** F. Adiceam, Y. Solomon, B. Weiss. *Cut-and-project quasicrystals, lattices, and dense forests.* Journal of the London Mathematical Society, 2022.
- **[Context]** C. J. Bishop. *How far can you see in a forest?* International Mathematics Research Notices, 2011.
- **[Survey]** W. T. Gowers. *Rough structure and classification.* Geometric and Functional Analysis (GAFA), Special Volume, Part I, 79–117, 2000.
- **[Problem list]** J. H. Conway. *Five \$1,000 Problems (Update 2017).* Problem list (the "Dead Fly Problem"), distributed via the OEIS.

## 10. Worked Example / Concrete Special Case

**(a) A single lattice fails.** Take $\Lambda = \mathbb{Z}^2$ and the rectangle
$$Q_n = \left(0,\,n\right) \times \left(\tfrac13,\ \tfrac13 + \tfrac1n\right), \qquad \mathrm{area}(Q_n) = 1 .$$
For $n \le 3$ its $y$-range $(\tfrac13,\tfrac13+\tfrac1n)$ contains no integer, so $Q_n \cap \mathbb{Z}^2 = \emptyset$. So $\mathbb{Z}^2$ is not Danzer, despite density $1$.

**(b) Axis-parallel boxes are easy.** Let $\Lambda = \{(m+n\sqrt2,\ m-n\sqrt2) : m,n \in \mathbb{Z}\}$, a lattice of covolume $2\sqrt2$. For $v = (m+n\sqrt2, m-n\sqrt2) \neq 0$,
$$|v_1 v_2| = |m^2 - 2n^2| \geq 1,$$
since $m^2 = 2n^2$ has no nonzero integer solution. So $\Lambda$ is admissible. The diagonal group $g_t = \mathrm{diag}(e^t, e^{-t})$ contains the unit $\varepsilon = 1+\sqrt2$ acting as $g_{t_0}\Lambda = \Lambda$ with $e^{t_0} = \varepsilon^2$. Any axis-parallel rectangle of area $A$ can be normalised by $g_t$ to one with side ratio in $[1, \varepsilon^2]$; because $\Lambda$ is a fixed lattice, all such rectangles of area $\geq C$ (for a suitable absolute $C$) contain a point. So $\Lambda$ hits every axis-parallel rectangle of area $\ge C$ using only $O(R^2)$ points in $[-R,R]^2$. Rescaling $\Lambda \mapsto C^{-1/2}\Lambda$ handles area exactly $1$.

**(c) Why rotations force a logarithm.** Rotating the rectangle by $\theta$ replaces $\Lambda$ by $r_{-\theta}\Lambda$, which is admissible only for $\theta$ in a measure-zero set; for typical $\theta$, $\inf|v_1v_2| = 0$ over $r_{-\theta}\Lambda$ and arbitrarily thin empty rectangles appear. The Bambah–Woods fix, in outline: put
$$Y \;=\; \bigcup_{k \in \mathbb{Z}} \; g_k \Lambda_k, \qquad g_k = \mathrm{diag}(2^{k}, 2^{-k}),$$
with $\Lambda_k$ a lattice whose fundamental domain is refined enough to catch all orientations at eccentricity $\approx 2^{2k}$. Inside $[-R,R]^2$ only the scales $|k| \lesssim \log_2 R$ contribute, and each contributes $O(R^2)$ points. Total:
$$N_Y(R) \;=\; \sum_{|k| \lesssim \log_2 R} O(R^2) \;=\; O(R^2 \log R).$$

**The open question in one line.** Every known scheme pays one independent point family per dyadic eccentricity scale, giving the factor $\log R$; Danzer's problem asks whether a single family of $O(R^2)$ points can serve all $\log R$ scales at once — and Solomon–Weiss show that if it can, that family cannot be any quasicrystal, lattice union, or other bounded-complexity object.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*