---
id: 05-analysis/polya-carlson-theorem-extensions
title: "Polya-Carlson Theorem Extensions"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Pólya–Carlson Theorem Extensions

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/polya-carlson-theorem-extensions` · **Status:** open

## 1. Problem Statement / Conjecture

The Pólya–Carlson theorem says that a power series with integer coefficients and radius of convergence exactly $1$ is either a rational function or has the unit circle as a natural boundary. The open problem is to determine how far this **rigidity dichotomy** — "rational, or nowhere continuable" — extends beyond its classical hypotheses.

Three concrete forms of the question, each open:

1. **Dynamical Pólya–Carlson dichotomy (Bell–Miles–Ward).** Let $T$ be an algebraic dynamical system (a continuous endomorphism of a compact abelian group, or more generally a system with $F_n(T) = |\mathrm{Fix}(T^n)| < \infty$ arising from algebraic data). Is the dynamical zeta function
$$\zeta_T(z) = \exp\Big(\sum_{n \ge 1} \frac{F_n(T)}{n} z^n\Big)$$
always either a rational function or a function admitting its circle of convergence as a natural boundary? No intermediate behaviour (algebraic-irrational, or meromorphic across part of the circle) is expected to occur.
2. **Capacity-one boundary case.** Pólya's capacity criterion resolves the case $\mathrm{cap}(\mathbb{C}\setminus D) < 1$. Classify the arithmetic power series that are meromorphic on domains whose complement has capacity exactly $1$ but which are not the unit disc — i.e. give a sharp Pólya–Carlson statement at the critical capacity.
3. **Several variables.** For $F \in \mathbb{Z}[[z_1,\dots,z_d]]$ with a suitable domain-of-convergence normalisation, is there a dichotomy between rationality (or $D$-finiteness) and a natural boundary on the distinguished boundary of the polydisc?

A complete solution to (1) means: a proof that no algebraic dynamical system has a zeta function that is transcendental yet continuable past its circle of convergence, or an explicit counterexample system with a proof of continuation.

## 2. Mathematical Foundations

Let $f(z) = \sum_{n\ge0} a_n z^n$ be holomorphic on the open disc $\mathbb{D}_R = \{|z| < R\}$, $R = (\limsup |a_n|^{1/n})^{-1}$.

**Natural boundary.** The circle $|z| = R$ is a *natural boundary* for $f$ if for no $\zeta$ with $|\zeta| = R$ does there exist a neighbourhood $U \ni \zeta$ and $g$ holomorphic on $U$ with $g = f$ on $U \cap \mathbb{D}_R$. Equivalently, every boundary point is singular.

**Theorem (Pólya 1916; Carlson 1921).** If $a_n \in \mathbb{Z}$ for all $n$ and $R = 1$, then either $f \in \mathbb{Q}(z)$ (and then $f = P/Q$ with $P,Q\in\mathbb{Z}[z]$, $Q(0)=\pm 1$ and all roots of $Q$ roots of unity), or $|z|=1$ is a natural boundary.

**Theorem (Szegő 1922).** If $\{a_n : n \ge 0\}$ is a *finite* set of complex numbers, the same dichotomy holds; in the rational case $(a_n)$ is eventually periodic.

**Transfinite diameter / logarithmic capacity.** For compact $E \subset \mathbb{C}$,
$$\mathrm{cap}(E) = \lim_{n\to\infty}\ \max_{z_1,\dots,z_n \in E}\ \prod_{i<j}|z_i - z_j|^{2/(n(n-1))}.$$
$\mathrm{cap}(\overline{\mathbb{D}}) = 1$; $\mathrm{cap}([a,b]) = (b-a)/4$.

**Theorem (Pólya 1928, capacity criterion).** Let $D \subset \mathbb{C}$ be a simply connected domain with $0 \in D$ and $\mathrm{cap}(\mathbb{C}\setminus D) < 1$. If $f \in \mathbb{Z}[[z]]$ extends meromorphically to $D$, then $f$ is rational. Carlson's theorem is the critical case $\mathrm{cap} = 1$, where rationality can fail only by total non-continuability.

The proofs run through **Hankel determinants**: with $H_n^{(m)} = \det(a_{m+i+j})_{0\le i,j\le n-1}$, Kronecker's criterion states $f \in \mathbb{Q}(z)$ iff $H_n^{(m)} = 0$ for all $n \ge N$ and all $m$. Integrality forces $|H_n^{(m)}| \ge 1$ whenever nonzero, while continuation across an arc plus a capacity estimate forces $H_n^{(m)} \to 0$ — a contradiction. This *arithmetic size vs. analytic smallness* mechanism is the engine of every extension.

**Adelic form (Bertrandias 1963).** For $f \in \mathcal{O}_K[[z]]$, $K$ a number field, meromorphy on domains $D_v$ at each place $v$ with $\prod_v \mathrm{cap}(D_v)$ exceeding an explicit threshold forces rationality; the Borel–Dwork rationality criterion is the special case combining one archimedean and finitely many $p$-adic radii.

**Dynamical setting.** For a compact abelian group $X$ with continuous surjective endomorphism $T$, $F_n(T) = |\ker(T^n - \mathrm{id})|$ when finite. For $T$ dual to multiplication by an algebraic number, $F_n$ is a product of local terms $\prod_v |\xi^n - 1|_v$, and $\zeta_T$ has integer Taylor coefficients. Rationality of $\zeta_T$ corresponds to $F_n$ satisfying a linear recurrence with the right positivity.

## 3. History & State of the Art (SOTA)

- **1916.** Pólya proves the dichotomy under an extra growth hypothesis and introduces the determinant method.
- **1921.** Carlson removes the hypothesis: the theorem in its final form (*Math. Z.* 9).
- **1922.** Szegő extends to coefficients drawn from a finite set — the version that governs automatic sequences.
- **1928.** Pólya's capacity criterion; the transfinite-diameter threshold $1$ is identified as sharp.
- **1928.** Estermann proves an $L$-function analogue: $\prod_p h(p^{-s})$ for $h \in \mathbb{Z}[X]$, $h(0)=1$, continues to $\mathbb{C}$ iff $h$ is a product of cyclotomic polynomials; otherwise $\Re s = 0$ is a natural boundary.
- **1963–69.** Bertrandias' adelic capacity theory; Cantor's arithmetic criteria for coefficients of rational functions.
- **1979.** Dwork–Robba develop the $p$-adic side (natural radii of convergence), giving transfer theorems used in $G$-function theory.
- **1986.** Kurokawa gives a general meromorphy/natural-boundary criterion for Euler products, the definitive Dirichlet-series analogue.
- **2007.** Everest–Miles–Stevens–Ward exhibit dynamical zeta functions with natural boundaries in non-hyperbolic $S$-integer systems.
- **2014.** Bell–Miles–Ward formulate the **Pólya–Carlson dichotomy for algebraic dynamics** and prove it in significant families.
- **2018.** Byszewski–Cornelissen (appendix by Royals–Ward) analyse zeta functions of endomorphisms of abelian varieties in characteristic $p$, producing algebraic-but-irrational and natural-boundary phenomena.

## 4. Partial Results / Verified Cases

- **Classical hypotheses:** fully proved — $a_n \in \mathbb{Z}$, $R=1$ (Carlson); finitely many coefficient values (Szegő); $\mathrm{cap}(\mathbb{C}\setminus D) < 1$ (Pólya).
- **Automatic sequences:** any $k$-automatic sequence over $\mathbb{Z}$ takes finitely many values, so by Szegő its generating function is rational (eventually periodic sequence) or has $|z|=1$ as natural boundary. Complete classification.
- **Mahler functions:** Bell–Coons–Rowland (2013) prove a rational-versus-transcendental dichotomy for solutions of $\sum_{i=0}^{n} p_i(z) f(z^{k^i}) = 0$, with effective transcendence tests.
- **Dirichlet series:** Estermann's theorem is complete for $\prod_p h(p^{-s})$, $h\in\mathbb{Z}[X]$; Kurokawa handles broad classes of Euler products with a natural boundary at the edge of the critical strip.
- **Algebraic dynamics:** Bell–Miles–Ward verify the dichotomy for $S$-integer dynamical systems with $|S| \le 1$ (rational) and for large classes of $S$ with $|S| \ge 2$ where $\zeta_T$ has $|z| = 1/e^{h}$ as natural boundary ($h$ = topological entropy); also for compact group automorphisms with finite entropy and quasihyperbolic behaviour in specific low-rank cases.
- **Full shifts and hyperbolic systems:** rationality holds (Artin–Mazur, Manning), consistent with the dichotomy.
- **Characteristic $p$:** for endomorphisms of abelian varieties over $\overline{\mathbb{F}_p}$, Byszewski–Cornelissen show $\zeta_T$ is rational or has a natural boundary in an explicitly described family, plus examples where $\zeta_T$ is a $p$-adically interesting non-rational algebraic-type object.

## 5. Principal Obstacles

- **Loss of the Hankel mechanism.** Carlson's argument needs integrality *and* radius $1$ simultaneously. When the circle of convergence is $R = e^{-h} \ne 1$ (the dynamical case), rescaling $z \mapsto Rz$ destroys integrality of the coefficients; the determinant lower bound $|H_n| \ge 1$ evaporates. No substitute lower bound is known for $\exp$-transformed coefficient sequences.
- **The exponential is not coefficient-friendly.** $\zeta_T$ has integer coefficients, but they are polynomial-with-rational-coefficients expressions in $F_1,\dots,F_n$; controlling their Hankel determinants requires arithmetic information about the *joint* distribution of $|\xi^n-1|_v$ across places, which is exactly the hard part of $S$-unit / linear-forms-in-logarithms theory.
- **Critical capacity.** At $\mathrm{cap} = 1$ the potential-theoretic estimate is an equality, so any conformal-mapping proof has zero slack. Constructing extremal non-disc domains of capacity $1$ with arithmetic series meromorphic on them requires a fine equidistribution input (Fekete–Szegő-type) that is not available uniformly.
- **Diophantine bottleneck.** Proving that singularities accumulate densely on $|z| = e^{-h}$ typically reduces to showing $\sum_n \log|\xi^n - 1|_p$ has no continuation, which needs lower bounds for $|\xi^n - 1|_p$ of Baker–Yu strength; current bounds are effective but not strong enough for the full range of $S$.
- **Several variables.** Capacity theory in $\mathbb{C}^d$ (pluripotential capacity) does not enjoy the sharp threshold $1$; Hankel determinants have no canonical multivariate analogue, and $D$-finite series in $\ge 2$ variables can be continuable without being rational, so the correct dichotomy statement is itself unclear.

## 6. The Gap

Proven: rigidity when the coefficient sequence is *itself* integral and the convergence radius is *exactly* the critical value $1$ (or the domain has subcritical capacity). Conjectured: rigidity when integrality is present only *before* an exponential transform, and the critical radius is $e^{-h}$ for an entropy $h$ that need not be the logarithm of an algebraic number of the right shape.

The exact step: produce a **scale-invariant arithmetic lower bound** playing the role of $|H_n| \ge 1$ — for instance a height or Mahler-measure lower bound on the Kronecker determinants of $(F_n)$ valid at radius $e^{-h}$ — or, failing that, an entropy-adapted potential theory in which $e^{-h}$-circles are critical. Every known proof of a dynamical natural boundary instead builds singularities by hand from the local factors $\prod_v(1 - \xi^n)$; this is case-by-case and stalls when $|S|$ is large or when the underlying group is non-abelian.

## 7. Current Research (as of June 2026)

- **Algebraic dynamics (Ward's school; Leeds/Durham, Waterloo, Utrecht).** Extension of the Bell–Miles–Ward programme to non-abelian and nilpotent group shifts, and to orbit-counting asymptotics where the boundary structure of $\zeta_T$ controls error terms. *(frontier — verify)* Recent preprints claim the dichotomy for $S$-integer systems over function fields with arbitrary finite $S$.
- **Arithmetic holonomy and $G$-functions.** Techniques from the André–Bombieri–Chudnovsky circle, revitalised by recent "arithmetic holonomy bound" methods, are being applied to capacity-one continuation problems. *(frontier — verify)*
- **Mahler functions and automatic sequences** (Coons, Bell, Adamczewski): quantitative natural-boundary statements, including the density of singular points and radial growth rates.
- **Statistical mechanics.** Nickel's conjecture that the 2D Ising susceptibility series has $|z|=1$ as a natural boundary (Nickel 1999; Boukraa–Hassani–Maillard et al.) is a physically motivated instance where the coefficients are integers after normalisation; still open.
- **Multivariate rigidity.** Bell–Nguyen–Zannier-style height methods for $D$-finite and multivariate series are the main tool being pushed toward a $d$-variable Pólya–Carlson statement.

## 8. Future Work

- Prove the dichotomy for all $S$-integer dynamical systems, then for all compact group automorphisms with finite entropy — Ward's stated staging of the problem.
- Develop a *weighted* Hankel/Kronecker criterion adapted to radius $e^{-h}$, possibly via Arakelov-theoretic heights of the associated Hankel matrices.
- Classify capacity-one domains $D$ admitting a non-rational $f \in \mathbb{Z}[[z]]$ meromorphic on $D$; conjecturally $D$ must be a disc of radius $1$ up to a normalised conformal equivalence.
- Formulate and test a polydisc version: for $F \in \mathbb{Z}[[z_1,z_2]]$ convergent on $\mathbb{D}^2$, is $F$ rational or singular along a dense subset of the distinguished boundary $|z_1|=|z_2|=1$?
- Settle Nickel's conjecture, which would give the first natural-boundary theorem for a series defined by a lattice model rather than by algebraic dynamics.

## 9. Key References

- **[Foundational]** G. Pólya. *Über Potenzreihen mit ganzzahligen Koeffizienten.* Mathematische Annalen 77 (1916), 497–513. [DOI](https://doi.org/10.1007/bf01456965)
- **[Foundational]** F. Carlson. *Über Potenzreihen mit ganzzahligen Koeffizienten.* Mathematische Zeitschrift 9 (1921), 1–13.
- **[Foundational]** G. Szegő. *Über Potenzreihen mit endlich vielen verschiedenen Koeffizienten.* Sitzungsberichte der Preussischen Akademie der Wissenschaften (1922), 88–91.
- **[Foundational]** G. Pólya. *Über gewisse notwendige Determinantenkriterien für die Fortsetzbarkeit einer Potenzreihe.* Mathematische Annalen 99 (1928), 687–706. [DOI](https://doi.org/10.1007/bf01459120)
- **[Foundational]** F. Bertrandias. *Ensembles remarquables d'adèles algébriques.* Bulletin de la Société Mathématique de France, Mémoire 4 (1965). [DOI](https://doi.org/10.24033/msmf.4)
- **[Foundational]** T. Estermann. *On certain functions represented by Dirichlet series.* Proceedings of the London Mathematical Society (2) 27 (1928), 435–448. [DOI](https://doi.org/10.1112/plms/s2-27.1.435)
- **[SOTA / Recent]** J. P. Bell, R. Miles, T. Ward. *Towards a Pólya–Carlson dichotomy for algebraic dynamics.* Indagationes Mathematicae 25 (2014), 652–668. [DOI](https://doi.org/10.1016/j.indag.2014.04.005)
- **[SOTA / Recent]** J. Byszewski, G. Cornelissen. *Dynamics on abelian varieties in positive characteristic* (with an appendix by R. Royals and T. Ward). Algebra & Number Theory 12 (2018), 2185–2235. [DOI](https://doi.org/10.2140/ant.2018.12.2185)
- **[SOTA / Recent]** G. Everest, R. Miles, S. Stevens, T. Ward. *Orbit-counting in non-hyperbolic dynamical systems.* Journal für die reine und angewandte Mathematik 608 (2007), 155–182. [DOI](https://doi.org/10.1515/crelle.2007.056)
- **[SOTA / Recent]** J. P. Bell, M. Coons, E. Rowland. *The rational-transcendental dichotomy of Mahler functions.* Journal of Integer Sequences 16 (2013), Article 13.2.10.
- **[SOTA / Recent]** N. Kurokawa. *On the meromorphy of Euler products, I & II.* Proceedings of the London Mathematical Society (3) 53 (1986), 1–47 and 209–236. [DOI](https://doi.org/10.1112/plms/s3-53.2.209)
- **[SOTA / Recent]** B. Dwork, P. Robba. *On natural radii of $p$-adic convergence.* Transactions of the American Mathematical Society 256 (1979), 199–213. [DOI](https://doi.org/10.2307/1998108)
- **[SOTA / Recent]** J. P. Bell, K. Nguyen, U. Zannier. *D-finiteness, rationality, and height.* Transactions of the American Mathematical Society 373 (2020), 4889–4906. [DOI](https://doi.org/10.1090/tran/8046)
- **[Survey]** S. L. Segal. *Nine Introductions in Complex Analysis*, revised edition. North-Holland/Elsevier, 2008 (chapter on natural boundaries and the Pólya–Carlson theorem). [DOI](https://doi.org/10.1016/s0304-0208(08)x8001-6)
- **[Survey]** J.-P. Allouche, J. Shallit. *Automatic Sequences: Theory, Applications, Generalizations.* Cambridge University Press, 2003.
- **[Related]** B. Nickel. *On the singularity structure of the 2D Ising model susceptibility.* Journal of Physics A 32 (1999), 3889–3906. [DOI](https://doi.org/10.1088/0305-4470/32/21/303)

## 10. Worked Example / Concrete Special Case

**Thue–Morse generating function.** Let $t_n \in \{0,1\}$ be the parity of the number of $1$s in the binary expansion of $n$: $t_{2n} = t_n$, $t_{2n+1} = 1 - t_n$. Put $T(z) = \sum_{n \ge 0} t_n z^n$, convergent on $|z|<1$.

*Functional equation.* Splitting by parity,
$$T(z) = \sum_n t_{2n} z^{2n} + \sum_n t_{2n+1} z^{2n+1} = T(z^2) + z\Big(\frac{1}{1-z^2} - T(z^2)\Big) = (1-z)T(z^2) + \frac{z}{1-z^2}.$$

*Closed form.* Setting $\varepsilon_n = 1 - 2t_n = (-1)^{t_n}$, the same recursion gives $E(z) = \sum \varepsilon_n z^n = (1-z)E(z^2)$, hence
$$E(z) = \prod_{k \ge 0}\big(1 - z^{2^k}\big), \qquad T(z) = \frac{1}{2}\Big(\frac{1}{1-z} - \prod_{k\ge0}\big(1-z^{2^k}\big)\Big).$$

*Dichotomy in action.* The coefficients lie in the finite set $\{0,1\}$, so Szegő's theorem applies. If $T$ were rational, $(t_n)$ would be eventually periodic; but the Thue–Morse word is overlap-free, hence not eventually periodic. Therefore $|z| = 1$ is a natural boundary — and here one can *see* it: the factor $1 - z^{2^k}$ vanishes at every $2^k$-th root of unity, so the zeros of the partial products $\prod_{k\le K}(1-z^{2^k})$ are the $2^{K+1}$-th roots of unity minus $1$, which equidistribute on $|z|=1$ as $K \to \infty$. Singularities are dense on the circle; no arc admits continuation.

*Where the open problem starts.* Now replace $T$ by a dynamical zeta function. Take $X = \widehat{\mathbb{Z}[1/2]}$ with $T$ dual to multiplication by $2$: $F_n = |2^n - 1|$, and
$$\zeta_T(z) = \exp\Big(\sum_{n\ge1}\frac{2^n-1}{n}z^n\Big) = \frac{1-z}{1-2z},$$
rational, radius $1/2 = e^{-h}$ with $h = \log 2$. Take instead $X = \widehat{\mathbb{Z}[1/6]}$, $T$ dual to $\times 2$: now $F_n = \prod_{v \in \{\infty,2,3\}} |2^n-1|_v$, which is $|2^n-1|$ divided by the $3$-part, and the $3$-adic factor oscillates according to $3\mid 2^n-1$ ($n$ even) with $v_3(2^n-1)$ jumping on multiples of $6$. The resulting $\zeta_T$ is *not* rational, and the conjecture — proved for this system by the $S$-integer analysis of Everest–Miles–Stevens–Ward, open in general — asserts $|z| = 1/2$ is a natural boundary. The contrast with the Thue–Morse case is exactly the gap of Section 6: there, integrality lives at radius $1$ and Szegő closes the argument in one line; here the integrality of the coefficients of $\zeta_T$ sits at radius $1/2$, and no Hankel-determinant lower bound is known to survive the rescaling.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*