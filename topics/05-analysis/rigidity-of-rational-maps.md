---
id: 05-analysis/rigidity-of-rational-maps
title: "Rigidity of Rational Maps"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rigidity of Rational Maps

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/rigidity-of-rational-maps` · **Status:** open

## 1. Problem Statement / Conjecture

Let $f:\hat{\mathbb{C}}\to\hat{\mathbb{C}}$ be a rational map of degree $d\ge 2$. The **rigidity conjecture** (also called the *no invariant line fields* conjecture) asserts:

> **Conjecture (Rigidity).** A rational map $f$ of degree $d \ge 2$ carries no invariant line field on its Julia set $J(f)$, unless $f$ is a Lattès map (a map semiconjugate to an endomorphism of a complex torus by the Weierstrass quotient).

Equivalent formulations:

- **(R1) Quasiconformal rigidity.** If two rational maps of degree $d$ are topologically conjugate on $\hat{\mathbb C}$, and neither is Lattès, then the conjugacy can be upgraded to a quasiconformal one; if in addition the conjugacy is conformal on the Fatou set and the map has no nontrivial deformation, $f$ is determined by its combinatorics.
- **(R2) Fatou's conjecture.** Hyperbolic maps are dense in $\mathrm{Rat}_d = \{$rational maps of degree $d\}$. McMullen proved (R-conjecture) $\Rightarrow$ (R2).
- **(R3) Combinatorial rigidity for polynomials.** Two combinatorially equivalent, non-renormalizable-or-suitably-controlled polynomials with all cycles repelling are conformally conjugate. For $z^2+c$ this is equivalent to **MLC**: local connectivity of the Mandelbrot set.

A complete solution means either a proof for all $d\ge 2$ and all $f\in\mathrm{Rat}_d$, or an explicit non-Lattès $f$ with a measurable invariant line field on a positive-measure subset of $J(f)$.

## 2. Mathematical Foundations

**Julia and Fatou sets.** $F(f)$ is the maximal open set where $\{f^n\}$ is normal; $J(f)=\hat{\mathbb C}\setminus F(f)$. $J(f)$ is compact, perfect, totally invariant, and equal to the closure of the repelling periodic points.

**Beltrami differentials and line fields.** A measurable Beltrami differential is $\mu = \mu(z)\,\overline{dz}/dz$ with $\|\mu\|_\infty<\infty$. A **line field** on a measurable set $E\subset J(f)$ of positive area is such a $\mu$ with $|\mu| = 1$ a.e. on $E$ and $\mu = 0$ off $E$; it assigns an unoriented tangent direction $\tfrac12\arg\mu(z)$ at a.e. $z\in E$. It is **invariant** iff
$$f^*\mu = \mu \quad \text{a.e.}, \qquad (f^*\mu)(z) = \mu(f(z))\,\frac{\overline{f'(z)}}{f'(z)}.$$

**Measurable Riemann mapping theorem** (Ahlfors–Bers). For $\|\mu\|_\infty<1$ there is a quasiconformal $\phi^\mu:\hat{\mathbb C}\to\hat{\mathbb C}$ with $\bar\partial\phi = \mu\,\partial\phi$, unique up to Möbius post-composition. If $\mu$ is $f$-invariant, then $\phi^\mu\circ f\circ(\phi^\mu)^{-1}$ is again rational of degree $d$. Hence an invariant line field on $J(f)$ produces a nontrivial analytic family $t\mapsto f_t = \phi^{t\mu}f(\phi^{t\mu})^{-1}$, $|t|<1$: a **deformation supported on the Julia set**.

**Teichmüller space of a dynamical system.** McMullen–Sullivan attach to $f$ a finite-dimensional complex manifold $\mathrm{Teich}(\hat{\mathbb C},f)$; its dimension decomposes as
$$\dim \mathrm{Teich}(\hat{\mathbb C},f) = (\text{Fatou contributions}) + (\text{invariant line-field contributions on } J(f)),$$
and the quotient $\mathrm{Teich}(\hat{\mathbb C},f)/\mathrm{Mod}(f)$ is the quasiconformal conjugacy class of $f$ in $\mathrm{Rat}_d$. Rigidity is exactly the vanishing of the Julia-set term for non-Lattès $f$.

**Lattès maps.** Let $\Lambda\subset\mathbb C$ be a lattice, $\wp$ the Weierstrass function for $\Lambda$, and $L(z)=\alpha z+\beta$ with $\alpha\Lambda\subset\Lambda$, $|\alpha|>1$. Then there is a rational $f$ with $f\circ\wp = \wp\circ L$; $J(f)=\hat{\mathbb C}$, $\deg f = |\alpha|^2$. The flat line field $\overline{dz}/dz$ on $\mathbb C/\Lambda$ pushes forward to an $f$-invariant line field on all of $\hat{\mathbb C}$. These are the only known examples.

**Structural stability.** Mañé–Sad–Sullivan and Lyubich: the set of $J$-stable maps is open and dense in $\mathrm{Rat}_d$. So density of hyperbolicity reduces to showing no stable component consists of non-hyperbolic maps — and such a "queer" component would carry an invariant line field.

## 3. History & State of the Art (SOTA)

- **1918–1920.** Fatou and Julia found the global theory; Fatou raised the question of whether maps with everywhere-attracting behaviour (hyperbolic maps) are dense.
- **1985.** Sullivan proves the **no wandering domains** theorem by quasiconformal deformation, importing Ahlfors–Bers into dynamics and creating the Sullivan dictionary with Kleinian groups (where Mostow rigidity is the analogue).
- **1983.** Mañé–Sad–Sullivan and Lyubich independently prove density of $J$-stability, isolating the invariant line field as the sole obstruction.
- **1987–1994.** Thurston's topological characterization of postcritically finite maps (published by Douady–Hubbard 1993) gives the first genuine rigidity theorem: a postcritically finite branched cover with no Thurston obstruction is realized by a **unique** rational map up to Möbius conjugacy, except for flexible Lattès examples.
- **1990.** Zdunik: the measure of maximal entropy of $f$ is absolutely continuous with respect to Lebesgue measure iff $f$ is Lattès (or a Chebyshev/power map on its Julia set) — a rigidity result in the measure-theoretic direction.
- **1990–1994.** Yoccoz proves MLC at all finitely renormalizable parameters of the quadratic family via puzzles and para-puzzles.
- **1994–1997.** McMullen (*Complex Dynamics and Renormalization*, *Renormalization and 3-Manifolds*) proves rigidity for infinitely renormalizable quadratics with **bounded combinatorics and definite moduli**; Lyubich proves it for a large class with unbounded combinatorics ("Dynamics of quadratic polynomials I–II", Acta 1997).
- **1997–2007.** Density of hyperbolicity settled on the **real line**: Graczyk–Świątek and Lyubich for real quadratics; Kozlovski–Shen–van Strien (Annals 2007) for all real one-dimensional maps.
- **2009.** Avila–Kahn–Lyubich–Shen and Kahn–Lyubich extend rigidity and MLC to **unicritical** polynomials $z^d+c$ at finitely renormalizable parameters.
- **2012.** Buff–Chéritat: quadratic Julia sets of positive area exist. This kills the simplest route (proving $\mathrm{area}(J)=0$ always) and makes the line-field statement essential.

## 4. Partial Results / Verified Cases

Rigidity / no invariant line fields is **proved** in these classes:

1. **Hyperbolic and subhyperbolic maps.** $J(f)$ has zero area, so no line field exists (Fatou set is full measure).
2. **Postcritically finite maps.** Thurston rigidity: unique up to conjugacy except flexible Lattès. Includes all $z^d+c$ with $c$ a Misiurewicz or superattracting parameter.
3. **Semi-hyperbolic / Collet–Eckmann maps.** $\mathrm{area}(J)=0$ whenever $J\neq\hat{\mathbb C}$ (Carleson–Jones–Yoccoz for semi-hyperbolic polynomials; Przytycki–Rohde).
4. **Quadratic polynomials $z^2+c$, at most finitely renormalizable, all periodic orbits repelling** (Yoccoz): $J$ locally connected, $c$ is a point of local connectivity of $\partial M$, rigidity holds.
5. **Unicritical $z^d+c$, $d\ge2$, finitely renormalizable** (Kahn–Lyubich; Avila–Kahn–Lyubich–Shen, Annals 2009).
6. **Infinitely renormalizable quadratics of bounded type with a priori bounds** (McMullen 1996; Lyubich 1997 for many unbounded classes; Kahn–Lyubich for "molecule"/decorations classes).
7. **Real maps in dimension one.** Kozlovski–Shen–van Strien: hyperbolicity is dense among real polynomials of any degree with real critical points; Avila–Lyubich–de Melo for real analytic unimodal families.
8. **Measure-theoretic Lattès characterization** (Zdunik 1990; Berteloot–Loeb for the higher-dimensional analogue on $\mathbb P^k$).
9. **Arithmetic rigidity.** Maps defined over $\bar{\mathbb Q}$ sharing infinitely many preperiodic points are rigidly related (Baker–DeMarco, Duke 2011; Yuan–Zhang equidistribution).

## 5. Principal Obstacles

- **Positive-area Julia sets exist.** Buff–Chéritat (Annals 2012) constructed quadratic $c$ with $\mathrm{area}(J(z^2+c))>0$, and Avila–Lyubich (Annals 2022) produced Feigenbaum Julia sets of positive area. The "measure-zero" shortcut is unavailable exactly where the problem is hardest.
- **Loss of a priori bounds.** All successful rigidity proofs run on **complex bounds**: uniform lower bounds $\mathrm{mod}(A_n)\ge\varepsilon>0$ on annuli in a renormalization tower. For infinitely renormalizable maps with wildly unbounded or *neutral/parabolic-like* combinatorics, no proof of such bounds is known, and the Teichmüller-distance contraction argument collapses.
- **Multiple critical points.** Yoccoz puzzles depend on a single critical point controlling the geometry. With $k\ge2$ free critical points the puzzle pieces of different critical orbits interlock; the combinatorial classification (Kiwi's laminations, Kozlovski–van Strien's decompositions) is far more complex, and no general non-renormalizable rigidity theorem exists for $\mathrm{Rat}_d$, $d\ge3$, with all critical points free.
- **Non-polynomial maps.** For general rational maps the Böttcher/external-ray coordinate at infinity is absent, so there is no global combinatorial model; puzzles must be built by hand (Roesch, Aspenberg–Yampolsky in specific families).
- **Quasiconformal methods are soft.** The measurable Riemann mapping theorem transports a line field but says nothing about its **regularity**. Line fields are only measurable; there is no analytic PDE regularity or Fourier-analytic tool that forces a measurable direction field invariant under a nonlinear expanding-with-critical-points map to be either trivial or flat.
- **Irrationally indifferent cycles.** Small-divisor/Siegel and Cremer behaviour produces geometry with no self-similar scaling, obstructing renormalization control precisely at parameters where positive-area Julia sets appear.

## 6. The Gap

Everything proved so far controls the **geometry at all scales along the critical orbit**: either the critical orbit escapes/is recurrent-with-bounds (Yoccoz, Kahn–Lyubich), or renormalization returns with definite moduli (McMullen, Lyubich). The gap is the complementary regime:

> **Open step.** For an infinitely renormalizable rational map with **unbounded, uncontrolled combinatorics** — or a rational map with $\ge 2$ free recurrent critical points — show that a measurable $f$-invariant field of directions on $J(f)$ of positive measure forces a flat (torus) structure.

Concretely, one needs a Lebesgue density argument: at a density point $z_0$ of the line field, blowing up by $Df^n$ along the orbit should produce nearly-conformal univalent maps carrying an almost-constant line field, and a compactness argument should then linearize $f$ near a torus quotient. The missing ingredient is **uniform bounded distortion of deep renormalization/blow-up limits without a priori moduli bounds**.

## 7. Current Research (as of June 2026)

- **Renormalization with neutral combinatorics.** Dudko and Lyubich have developed uniform a priori bounds for *neutral/satellite* renormalization, aiming at MLC and rigidity for large families of infinitely renormalizable quadratics. Their announced progress covers Feigenbaum-type and molecule parameters. *(frontier — verify)*
- **Pacman renormalization.** Dudko–Lyubich–Selinger's "pacman" renormalization operator handles Siegel and satellite parameters uniformly and is currently the most active technical engine for the remaining quadratic cases.
- **Higher-degree and multi-critical rigidity.** Work of Kozlovski–van Strien and of Roesch, Wang, Yin on non-renormalizable rational maps with several critical points; cubic polynomial rigidity is a testing ground (Branner–Hubbard, Kiwi, Qiu–Yin).
- **Higher-dimensional analogues.** Bianchi, Berteloot, Dujardin and Astorg study stability and bifurcation in $\mathrm{Hol}_d(\mathbb P^k)$; rigidity of Lattès maps on $\mathbb P^k$ is proven, but the line-field statement for $k\ge2$ is wide open.
- **Arithmetic dynamics.** DeMarco, Ghioca, Krieger, Tucker and Ye pursue unlikely-intersection and dynamical André–Oort statements, giving rigidity over number fields independent of the analytic conjecture.
- **Groups.** Stony Brook (Lyubich's IMS), Toronto (Yampolsky), IMPA/Paris (Avila), Warwick/Amsterdam (van Strien), Toulouse/Lille (Buff, Chéritat, Dujardin, Berteloot), CAS Beijing (Yin, Qiu).

## 8. Future Work

- Prove **a priori bounds** for all infinitely renormalizable quadratics; by Lyubich's and McMullen's machinery this would give MLC and rigidity for the whole quadratic family, hence Fatou's conjecture for $\mathrm{Rat}_2$.
- Develop a **puzzle theory for rational maps without escaping critical points**, replacing external rays with dynamically defined graphs (Roesch's program).
- Understand positive-area Julia sets quantitatively: does the Buff–Chéritat set support any measurable invariant structure at all? A rigidity proof restricted to positive-area $J$ would be decisive.
- Import the **Mostow/Sullivan dictionary** more aggressively: find a dynamical replacement for the ergodicity of the geodesic flow on the sphere at infinity, which is what kills line fields for Kleinian groups.
- Sharpen the transfer operator / thermodynamic formalism approach: characterize Lattès maps by the local geometry of conformal measures at density points.

## 9. Key References

- **[Foundational]** D. Sullivan. *Quasiconformal homeomorphisms and dynamics I: Solution of the Fatou–Julia problem on wandering domains.* Annals of Mathematics 122 (1985), 401–418.
- **[Foundational]** R. Mañé, P. Sad, D. Sullivan. *On the dynamics of rational maps.* Annales scientifiques de l'ÉNS 16 (1983), 193–217.
- **[Foundational]** A. Douady, J. H. Hubbard. *A proof of Thurston's topological characterization of rational functions.* Acta Mathematica 171 (1993), 263–297.
- **[Foundational]** C. T. McMullen. *Complex Dynamics and Renormalization.* Annals of Mathematics Studies 135, Princeton University Press, 1994.
- **[Foundational]** C. T. McMullen. *Renormalization and 3-Manifolds which Fiber over the Circle.* Annals of Mathematics Studies 142, Princeton University Press, 1996.
- **[Foundational]** C. T. McMullen, D. Sullivan. *Quasiconformal homeomorphisms and dynamics III: The Teichmüller space of a holomorphic dynamical system.* Advances in Mathematics 135 (1998), 351–395.
- **[SOTA]** M. Lyubich. *Dynamics of quadratic polynomials I–II.* Acta Mathematica 178 (1997), 185–297.
- **[SOTA]** J. Graczyk, G. Świątek. *Generic hyperbolicity in the logistic family.* Annals of Mathematics 146 (1997), 1–52.
- **[SOTA]** O. Kozlovski, W. Shen, S. van Strien. *Density of hyperbolicity in dimension one.* Annals of Mathematics 166 (2007), 145–182.
- **[SOTA]** A. Avila, J. Kahn, M. Lyubich, W. Shen. *Combinatorial rigidity for unicritical polynomials.* Annals of Mathematics 170 (2009), 783–797.
- **[SOTA]** J. Kahn, M. Lyubich. *Local connectivity of Julia sets for unicritical polynomials.* Annals of Mathematics 170 (2009), 413–426.
- **[SOTA]** X. Buff, A. Chéritat. *Quadratic Julia sets with positive area.* Annals of Mathematics 176 (2012), 673–746.
- **[SOTA]** A. Avila, M. Lyubich. *Lebesgue measure of Feigenbaum Julia sets.* Annals of Mathematics 195 (2022), 1–88.
- **[Related]** A. Zdunik. *Parabolic orbifolds and the dimension of the maximal measure for rational maps.* Inventiones Mathematicae 99 (1990), 627–649.
- **[Related]** M. Baker, L. DeMarco. *Preperiodic points and unlikely intersections.* Duke Mathematical Journal 159 (2011), 1–29.
- **[Survey]** J. Milnor. *Dynamics in One Complex Variable*, 3rd ed. Annals of Mathematics Studies 160, Princeton University Press, 2006.
- **[Survey]** C. T. McMullen. *Frontiers in complex dynamics.* Bulletin of the AMS 31 (1994), 155–172.
- **[Survey]** J. Milnor. *On Lattès maps.* In *Dynamics on the Riemann Sphere*, European Mathematical Society, 2006, 9–43.

## 10. Worked Example / Concrete Special Case

**The exceptional case made explicit: a degree-4 Lattès map.**

Take the lattice $\Lambda=\mathbb Z[i]$ and the elliptic curve $E:\;y^2=x^3-x$, uniformized by $x=\wp(z)$, $y=\tfrac12\wp'(z)$ for $\wp=\wp_\Lambda$. The duplication formula on $E$ gives, for $a=-1$, $b=0$ in $x(2P)=\frac{(x^2-a)^2-8bx}{4(x^3+ax+b)}$:
$$f(x)=\frac{(x^2+1)^2}{4x(x^2-1)},\qquad \deg f = 4.$$
Then $f(\wp(z))=\wp(2z)$, i.e. $f$ is semiconjugate by $\wp:\mathbb C/\Lambda\to\hat{\mathbb C}$ (a degree-2 branched cover) to $L(z)=2z$.

*Julia set.* $L$ is uniformly expanding on the torus, and $\wp$ is a surjection, so $J(f)=\hat{\mathbb C}$. The four critical points of $f$ are the images of the $2$-torsion, $x\in\{0,\pm 1,\infty\}$; they map $0\mapsto\infty$, $\pm1\mapsto\infty$, $\infty\mapsto\infty$, so $f$ is postcritically finite with postcritical set $\{\infty\}$ — an orbifold of parabolic type $(2,2,2,2)$.

*The invariant line field.* On $\mathbb C/\Lambda$ put $\mu_0=\overline{dz}/dz$, the horizontal direction field. Since $L^*(\overline{dz}/dz)=\overline{2\,dz}/(2\,dz)=\overline{dz}/dz$, it is $L$-invariant, with $|\mu_0|\equiv1$. Push it forward by $w=\wp(z)$: writing $dz=dw/\wp'(z)$,
$$\mu(w)=\frac{\overline{dz}}{dz}=\frac{\wp'(z)}{\overline{\wp'(z)}}\cdot\frac{\overline{dw}}{dw}.$$
Because $\wp'$ is odd, the coefficient $\wp'(z)/\overline{\wp'(z)}$ is unchanged under $z\mapsto -z$, so $\mu$ is a well-defined measurable Beltrami differential on $\hat{\mathbb C}$ with $|\mu|=1$ a.e. From $f\circ\wp=\wp\circ L$ one gets $f^*\mu=\mu$ a.e. So $f$ **does** carry an invariant line field on $J(f)=\hat{\mathbb C}$.

*The deformation it generates.* For $|t|<1$ solve $\bar\partial\phi_t=t\mu\,\partial\phi_t$; then $f_t=\phi_t\circ f\circ\phi_t^{-1}$ is again a degree-4 rational map, and downstairs it corresponds to replacing $\Lambda$ by $A_t(\Lambda)$ for the real-linear map $A_t$ with dilatation $t$. Since $\mathbb Z[i]$ and $A_t(\mathbb Z[i])$ are generally non-homothetic lattices, $f_t$ is **not** Möbius-conjugate to $f$: a genuine one-complex-parameter family of topologically conjugate, conformally inequivalent maps. This is the *flexible Lattès* phenomenon.

*What the conjecture asserts.* This example is claimed to be the only mechanism. For instance, take $f_c(z)=z^2+c$ with $c$ in the Buff–Chéritat set, so $\mathrm{area}(J(f_c))>0$ and a line field is not excluded by measure alone. Since $f_c$ has one critical point with a Cremer/Siegel-type neutral fixed point, it admits no torus semiconjugacy (its orbifold is hyperbolic, not parabolic). Rigidity predicts $\mathrm{Teich}(\hat{\mathbb C},f_c)$ is a single point, hence no invariant $\mu$ with $|\mu|=1$ on a positive-measure part of $J(f_c)$ exists. No proof is known for this $c$ — that single unresolved instance is the whole conjecture in miniature.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*