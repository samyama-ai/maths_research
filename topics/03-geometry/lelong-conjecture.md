---
id: 03-geometry/lelong-conjecture
title: "Lelong's Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lelong's Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/lelong-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be an $n$-dimensional complex manifold and let $T$ be a **positive current of bidimension $(p,p)$** on $X$ whose coefficients are measures (order zero). For $x \in X$ write $\nu(T,x)$ for the **Lelong number** (density) of $T$ at $x$, and for $c>0$ set

$$E_c(T) \;=\; \{\, x \in X \;:\; \nu(T,x) \ge c \,\}.$$

> **Lelong's Conjecture (analyticity of density sublevel sets beyond the closed case).** If $T$ is positive and **plurisubharmonic**, i.e. $dd^c T \ge 0$ as a current of bidimension $(p-1,p-1)$, then for every $c>0$ the set $E_c(T)$ is a closed analytic subset of $X$ of dimension at most $p$.

A complete solution is either (i) a proof valid for all $X$, all $p$ with $1 \le p \le n-1$, and all $c > 0$; or (ii) an explicit positive plurisubharmonic current $T$ and a level $c>0$ for which $E_c(T)$ is not contained in any analytic set of dimension $\le p$ (e.g. $E_c(T)$ totally real, or of positive $(2p+1)$-dimensional Hausdorff measure).

**Naming note.** "Lelong's conjecture" is used in the literature for a family of density/analyticity questions originating in Lelong's work on integration currents. The **closed** case $dd^cT = 0$ is a theorem of Siu (1974) and is no longer open; the plurisubharmonic case above is the surviving open form, and is the statement catalogued here. Related open items in the same circle (analyticity for $\partial\bar\partial$-closed currents; the density-current refinement of Dinh–Sibony) are recorded in §4 and §7.

## 2. Mathematical Foundations

**Positive currents.** $\mathcal{D}'^{p,p}(X)$ denotes currents of bidimension $(p,p)$. Fix the normalizations
$$d^c = \frac{i}{2\pi}\left(\bar\partial - \partial\right), \qquad dd^c = \frac{i}{\pi}\,\partial\bar\partial, \qquad \beta = dd^c \tfrac{|z|^2}{2},$$
so that $\beta^n/n!$ is Lebesgue measure on $\mathbb{C}^n$. $T$ is **positive** if $T \wedge i\alpha_1\wedge\bar\alpha_1 \wedge \cdots \wedge i\alpha_p \wedge \bar\alpha_p \ge 0$ for all $(1,0)$-forms $\alpha_j$. Positivity forces order zero, so the **trace measure** $\sigma_T = T \wedge \beta^p / p!$ is a positive Radon measure.

**Lelong number.** In a coordinate ball $B(x,r) \subset \mathbb{C}^n$ put
$$\nu(T,x,r) \;=\; \frac{\sigma_T\big(B(x,r)\big)}{\pi^p r^{2p}/p!}\,, \qquad \nu(T,x) \;=\; \lim_{r \to 0^+} \nu(T,x,r).$$
If $dd^c T \ge 0$ the function $r \mapsto \nu(T,x,r)$ is (up to a controlled correction) increasing, so the limit exists; this **monotonicity** is Lelong's theorem for closed currents and its plurisubharmonic extension. The value $\nu(T,x)$ is independent of coordinates (Siu).

**Two anchors.**
- *Integration currents.* For an analytic set $V \subset X$ of pure dimension $p$, Lelong (1957) showed $[V]$ is a closed positive current of bidimension $(p,p)$, and Thie (1967) proved $\nu([V],x) = \operatorname{mult}_x V$, the algebraic multiplicity.
- *Plurisubharmonic functions.* For $u$ psh near $x$, $T = dd^c u$ is closed positive of bidimension $(n-1,n-1)$ and
$$\nu(u,x) \;=\; \nu(dd^cu, x) \;=\; \lim_{r\to 0^+}\frac{\sup_{|z-x|=r} u(z)}{\log r} \;=\; \sup\{\gamma \ge 0 : u(z) \le \gamma \log|z-x| + O(1)\}.$$

**Siu decomposition.** If $T \ge 0$ is closed of bidimension $(p,p)$, then
$$T \;=\; \sum_{j\ge 1} \lambda_j\,[Z_j] \;+\; R, \qquad \lambda_j > 0,$$
with $Z_j$ irreducible $p$-dimensional analytic sets and $R \ge 0$ closed satisfying $\dim E_c(R) < p$ for all $c>0$.

**Plurisubharmonic currents.** $T \ge 0$ with $dd^cT \ge 0$. This class is strictly larger than the closed one and is the natural home for non-Kähler geometry: it is stable under pushforward by proper holomorphic maps and under multiplication by psh weights, and it contains $u\,[V]$ for $u$ psh $\ge 0$.

**Skoda's integrability theorem.** For $u$ psh near $0 \in \mathbb{C}^n$: $\nu(u,0) < 1 \Rightarrow e^{-2u} \in L^1_{\mathrm{loc}}(0)$; $\nu(u,0) \ge n \Rightarrow e^{-2u} \notin L^1_{\mathrm{loc}}(0)$. This links Lelong numbers to multiplier ideals $\mathcal{I}(u)$ and hence to vanishing theorems.

## 3. History & State of the Art (SOTA)

- **1957.** Pierre Lelong, *Intégration sur un ensemble analytique complexe*: analytic sets define closed positive currents; monotonicity of $r \mapsto \nu(T,x,r)$; the density $\nu(T,x)$ is introduced.
- **1967–68.** Thie identifies $\nu([V],x)$ with multiplicity; Lelong's book *Fonctions plurisousharmoniques et formes différentielles positives* codifies the theory and raises the structural question: **are the density sublevel sets analytic?**
- **1972.** Skoda studies analytic sets of finite order in $\mathbb{C}^n$ and proves the integrability threshold above; he also establishes analyticity of $E_c(dd^cu)$ in special growth classes.
- **1974.** Siu (Invent. Math. 27) proves the conjecture for **closed** positive currents: $E_c(T)$ is analytic for every $c > 0$. The proof runs through Hörmander $L^2$ estimates and the strong noetherian property of coherent sheaves.
- **1979.** Kiselman's "densité des fonctions plurisousharmoniques" gives directional/refined Lelong numbers and a much shorter route to semicontinuity.
- **1987.** Demailly (Acta Math. 159) introduces **generalized Lelong numbers** $\nu(T,\varphi)$ with respect to psh weights $\varphi$, proves integrality and analyticity theorems, and gives the comparison inequalities that dominate all later work.
- **2013–2015.** Berndtsson, then Guan–Zhou, prove the openness and strong openness conjectures of Demailly–Kollár, settling the multiplier-ideal side of the singularity dictionary.
- **2018.** Dinh–Sibony's theory of **density currents** replaces $\nu(T,x)$ by a whole cone of tangent currents, giving a non-generic intersection theory and a finer invariant whose sublevel structure is only partly understood.

The plurisubharmonic (non-closed) case remains open in all dimensions $n \ge 3$ for $1 \le p \le n-1$.

## 4. Partial Results / Verified Cases

- **Closed currents, all $n$, all $p$, all $c$.** Siu (1974): $E_c(T)$ is analytic of dimension $\le p$. Demailly (1987) reproves and extends it to generalized Lelong numbers $\nu(T,\varphi)$ for weights with analytic singularities.
- **Bidimension $(n-1,n-1)$ closed, i.e. $T = dd^cu$.** $E_c(dd^cu) = \{x : \nu(u,x) \ge c\}$ is analytic; equivalently the psh-singularity level sets are analytic. This case admits a self-contained Hörmander-estimate proof.
- **Divisorial level $c$ with $\dim = p$.** In the Siu decomposition the top-dimensional components $Z_j$ are exactly the $p$-dimensional components of $E_{\lambda_j}(T)$; the "residual" $R$ has $\dim E_c(R) \le p-1$.
- **$p = 0$.** Trivial: $E_c(T)$ is a discrete set of atoms of the measure $T$.
- **$T = u\,S$ with $S$ closed positive and $u \ge 0$ psh.** Then $T$ is plurisubharmonic and $\nu(T,x) = e^{-?}$-type formulas reduce to $\nu(S,x)$ off $\{u = +\infty\}$; the conjecture holds because $E_c(T)$ is a union of $E_{c'}(S)$-type sets.
- **Currents with $dd^cT \ge -\gamma \wedge T$ for a smooth $(1,1)$-form $\gamma$ on a compact manifold.** Demailly's comparison machinery gives monotonicity of $e^{Cr}\nu(T,x,r)$ and hence upper semicontinuity of $x \mapsto \nu(T,x)$; **semicontinuity is known, analyticity is not.**
- **Extension across analytic sets.** Alessandrini–Bassanelli (Forum Math., 1993) prove extension theorems for plurisubharmonic currents across analytic subsets of small dimension, and obtain analyticity of $E_c(T)$ in bidimension $(n-1,n-1)$ under $\partial\bar\partial$-closedness plus a mass hypothesis.
- **Counterexample boundary.** For merely positive $T$ (no hypothesis on $dd^cT$) the conjecture is false: taking $T = f\,\beta^{n-p}$ with $f \ge 0$ a suitably chosen $L^1_{\mathrm{loc}}$ density, $E_c(T)$ can be a prescribed non-analytic Borel set. So $dd^cT \ge 0$ carries the entire content.

## 5. Principal Obstacles

- **Loss of the $L^2$ machine.** Siu's proof factors through Hörmander/Bombieri $L^2$ estimates applied to the local potential $u$ with $dd^cu = T$. A closed positive $(1,1)$-current has such a potential; a plurisubharmonic current of bidimension $(p,p)$ with $p<n-1$ has none, so there is no weight to feed into $\bar\partial$-estimates and no multiplier ideal to invoke the strong noetherian property.
- **No Siu decomposition.** The extraction $T = \sum \lambda_j[Z_j] + R$ uses $d$-closedness twice: to make $\mathbf{1}_{Z}T$ closed (Skoda–El Mir extension) and to make the residual current positive. Both steps fail under $dd^cT \ge 0$ only; $\mathbf{1}_{Z}T$ need not be plurisubharmonic.
- **Weak monotonicity.** For closed $T$, $r \mapsto \nu(T,x,r)$ is exactly increasing. Under $dd^cT \ge 0$ one gets monotonicity of $\nu$ only after multiplying by a correction factor, and the correction degrades uniformly in $x$ as the mass of $dd^cT$ concentrates — so the limit $\nu(T,x)$ exists pointwise but the convergence is not locally uniform, blocking the standard "semicontinuity + noetherian" argument.
- **Coherence has no analogue.** Analyticity in the closed case ultimately comes from coherence of $\mathcal{I}(cu)$. There is no sheaf of ideals attached to a bidimension-$(p,p)$ plurisubharmonic current, so "the level set is a zero set" has no algebraic mechanism behind it.
- **Non-Kähler pathologies.** On non-Kähler compact manifolds, plurisubharmonic currents exist in abundance with no cohomological control: $\{T\}$ lives in no fixed Bott–Chern class, so mass bounds — the source of all compactness arguments — are unavailable.
- **Tangent cones need not be unique.** Dinh–Sibony show tangent currents at a point can form a nontrivial family; when the tangent cone is non-unique, "density" is not a single number and the very object whose level sets are being tested becomes coarse.

## 6. The Gap

Proven: analyticity of $E_c(T)$ whenever $T$ admits a local psh potential in a suitable sense — concretely, closed positive $(1,1)$-currents, closed positive $(p,p)$-currents by Siu's reduction, and generalized Lelong numbers with analytic-singularity weights. Conjectured: the same for $dd^cT \ge 0$.

The precise missing step is a **potential-theoretic representation for plurisubharmonic currents of bidimension $(p,p)$, $p < n-1$**: an assignment $T \mapsto \mathcal{J}(cT)$ of a coherent ideal (or a closed positive current of the same bidimension with the same Lelong numbers) such that $E_c(T) = V(\mathcal{J}(cT))$ locally. Equivalently: given $T \ge 0$ with $dd^cT \ge 0$ and $c > 0$, produce a *closed* positive current $T'$ of bidimension $(p,p)$ near $x$ with $\nu(T',y) \ge \nu(T,y)$ for all $y$ near $x$ and $\nu(T',x) < \infty$. No construction of such a $T'$ is known, and it is not known whether one must exist.

## 7. Current Research (as of June 2026)

- **Density currents (Dinh–Sibony school; Paris–Orsay, Sorbonne, NUS).** Tangent-current techniques replace scalar densities; the analyticity question becomes a question about the structure of the set where the density current has prescribed mass. *(frontier — verify)* Recent work extends density theory to non-Kähler compact manifolds where plurisubharmonic currents are the natural objects.
- **Duc-Viet Vu (Cologne) and collaborators.** Quantitative bounds for Lelong numbers of currents of full mass intersection and for densities under pullback; these yield analyticity in bidimension $(n-1,n-1)$ under mass-concentration hypotheses. *(frontier — verify)*
- **Non-Kähler geometry (Alessandrini–Bassanelli lineage; Parma, Torino).** Structure and extension theorems for $\partial\bar\partial$-closed positive currents, aiming at the $p = n-1$ case first.
- **Pluripotential/relative-type methods (Rashkovskii, Stavanger; Guedj–Zeriahi, Toulouse).** Relative types $\sigma(u,\varphi)$ and generalized Lelong numbers give semicontinuity in wider classes; the open point is whether the level sets of relative types are analytic when the reference weight is not toric.
- **Algebraic-geometry side (Demailly school, Grenoble; Guan–Zhou, CAS Beijing).** Strong openness and its effective versions supply the closed-case toolkit; efforts to transplant multiplier ideals to non-closed currents are ongoing and so far unsuccessful.

## 8. Future Work

- Settle bidimension $(n-1,n-1)$ with $dd^cT \ge 0$ on $\mathbb{C}^n$ — the case with the best chance, since a scalar potential for the trace is available.
- Build the missing coherent-ideal analogue: define $\mathcal{J}(cT)$ via $L^2$ estimates for the $\bar\partial$-operator twisted by the trace potential of $T$, and prove a noetherian property for the resulting filtration.
- Prove or refute **locally uniform** convergence $\nu(T,x,r) \to \nu(T,x)$ for plurisubharmonic $T$ with $dd^cT$ of locally finite mass; a positive answer would give analyticity by Siu's original scheme.
- Search for counterexamples on non-Kähler compact threefolds (Iwasawa manifold and its deformations), where plurisubharmonic currents are plentiful and cohomological obstructions vanish.
- Reformulate via density currents: prove that $\{x : \text{tangent cone of } T \text{ at } x \text{ has mass} \ge c\}$ is analytic, which implies the conjecture where tangent cones are unique.

## 9. Key References

- **[Foundational]** P. Lelong. *Intégration sur un ensemble analytique complexe.* Bulletin de la Société Mathématique de France, 85 (1957), 239–262. [DOI](https://doi.org/10.24033/bsmf.1488)
- **[Foundational]** P. Lelong. *Fonctions plurisousharmoniques et formes différentielles positives.* Gordon & Breach / Dunod, Paris, 1968.
- **[Foundational]** P. Thie. *The Lelong number of a point of a complex analytic set.* Mathematische Annalen, 172 (1967), 269–312. [DOI](https://doi.org/10.1007/bf01351593)
- **[Foundational]** Y.-T. Siu. *Analyticity of sets associated with Lelong numbers and the extension of closed positive currents.* Inventiones Mathematicae, 27 (1974), 53–156. [DOI](https://doi.org/10.1007/bf01389965)
- **[Foundational]** H. Skoda. *Sous-ensembles analytiques d'ordre fini ou infini dans $\mathbb{C}^n$.* Bulletin de la Société Mathématique de France, 100 (1972), 353–408. [DOI](https://doi.org/10.24033/bsmf.1743)
- **[SOTA]** J.-P. Demailly. *Nombres de Lelong généralisés, théorèmes d'intégralité et d'analyticité.* Acta Mathematica, 159 (1987), 153–169. [DOI](https://doi.org/10.1007/bf02392558)
- **[SOTA]** C. O. Kiselman. *Densité des fonctions plurisousharmoniques.* Bulletin de la Société Mathématique de France, 107 (1979), 295–304. [DOI](https://doi.org/10.24033/bsmf.1898)
- **[SOTA]** L. Alessandrini, G. Bassanelli. *Plurisubharmonic currents and their extension across analytic subsets.* Forum Mathematicum, 5 (1993), 577–602. [DOI](https://doi.org/10.1515/form.1993.5.577)
- **[SOTA / Recent]** T.-C. Dinh, N. Sibony. *Density of positive closed currents, a theory of non-generic intersections.* Journal of Algebraic Geometry, 27 (2018), 497–551. [DOI](https://doi.org/10.1090/jag/711)
- **[SOTA / Recent]** Q. Guan, X. Zhou. *A proof of Demailly's strong openness conjecture.* Annals of Mathematics, 182 (2015), 605–616. [DOI](https://doi.org/10.4007/annals.2015.182.2.5)
- **[SOTA / Recent]** B. Berndtsson. *The openness conjecture for plurisubharmonic functions.* arXiv:1305.5781, 2013.
- **[Survey]** J.-P. Demailly. *Complex Analytic and Differential Geometry.* Open-content book, Université Grenoble Alpes (Chapters II–III on positive currents and Lelong numbers).
- **[Survey]** V. Guedj, A. Zeriahi. *Degenerate Complex Monge–Ampère Equations.* EMS Tracts in Mathematics 26, European Mathematical Society, 2017. [DOI](https://doi.org/10.4171/167)

## 10. Worked Example / Concrete Special Case

**Setting.** $X = \mathbb{C}^2$, $p = 1$. Pick distinct slopes $a_1, a_2, \ldots \in \mathbb{C}$ and lines $\ell_j = \{ z_2 = a_j z_1 \}$, all through the origin. Define
$$T \;=\; \sum_{j \ge 1} 2^{-j}\,[\ell_j].$$

**Step 1 — $T$ is a legitimate closed positive current.** Each $[\ell_j]$ is closed positive of bidimension $(1,1)$ with trace mass $\sigma_{[\ell_j]}(B(0,r)) = \pi r^2$. Hence $\sigma_T(B(0,r)) = \pi r^2 \sum_j 2^{-j} = \pi r^2$, finite, so the sum converges in the weak topology and $dd^cT = 0$.

**Step 2 — Lelong numbers.** With the normalization of §2, $\nu(T,x,r) = \sigma_T(B(x,r))/(\pi r^2)$.
- At $x = 0$: $\nu(T,0) = \sum_{j\ge1} 2^{-j} = 1$.
- At $x \in \ell_k \setminus \{0\}$: only $\ell_k$ passes through $x$, so $\nu(T,x) = 2^{-k}$.
- At $x \notin \bigcup_j \ell_j$: $\nu(T,x) = 0$.

**Step 3 — the sublevel sets.**
$$E_c(T) \;=\; \begin{cases} \{0\} & 2^{-1} < c \le 1,\\[2pt] \{0\} \cup \ell_1 \cup \cdots \cup \ell_k & 2^{-(k+1)} < c \le 2^{-k},\\[2pt] \varnothing & c > 1.\end{cases}$$
For $c = 3/4$: $E_{3/4}(T) = \{0\}$, an analytic set of dimension $0 \le p = 1$. For $c = 1/8$: $E_{1/8}(T) = \ell_1 \cup \ell_2 \cup \ell_3$, analytic of dimension $1$. Every level is a **finite** union of lines even though $T$ has infinitely many components — because only finitely many $\lambda_j = 2^{-j}$ exceed any fixed $c$. This is exactly Siu's decomposition with $\lambda_j = 2^{-j}$, $Z_j = \ell_j$, $R = 0$.

**Step 4 — where the open case begins.** Now let $u \ge 0$ be psh on $\mathbb{C}^2$ and set $T_u = u\,T$. Then $T_u \ge 0$ and $dd^c T_u = (dd^cu)\wedge T \ge 0$, so $T_u$ is plurisubharmonic but **not closed**. Here $\nu(T_u, x)$ can differ from $\nu(T,x)$ only where $u$ is singular, and the conjecture still holds because $E_c(T_u)$ is built from the $\ell_j$ and the analytic sets $E_{c'}(dd^cu)$.

The unresolved question is whether *every* plurisubharmonic $T$ arises with this much structure. Concretely: does there exist $T \ge 0$ of bidimension $(1,1)$ on $\mathbb{C}^3$ with $dd^cT \ge 0$ and $\nu(T,x) \ge 1$ for all $x$ in the totally real $3$-sphere $S = \{ |z_1|^2+|z_2|^2+|z_3|^2 = 1,\ z_j \in \mathbb{R}\}$? Since $S$ contains no positive-dimensional complex analytic subset, such a $T$ would refute the conjecture. No construction is known, and no proof that one cannot exist is known — that is precisely the gap of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*