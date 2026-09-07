---
id: 03-geometry/monodromy-conjecture
title: "Monodromy Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Monodromy Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/monodromy-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $f \in \mathbb{Z}[x_1,\dots,x_n]$ be a nonconstant polynomial and $p$ a prime. Igusa's local zeta function is

$$Z_{f,p}(s) \;=\; \int_{\mathbb{Z}_p^n} |f(x)|_p^{\,s}\, |dx|, \qquad \operatorname{Re}(s)>0,$$

a rational function of $p^{-s}$. **Igusa's monodromy conjecture** asserts: if $s_0 \in \mathbb{C}$ is a pole of $Z_{f,p}(s)$ for infinitely many $p$ (or for $p \gg 0$), then $e^{2\pi i \operatorname{Re}(s_0)}$ is an eigenvalue of the local monodromy of $f$ at some point of $f^{-1}(0) \subset \mathbb{C}^n$.

The **stronger (Bernstein–Sato) form** asserts that $\operatorname{Re}(s_0)$ is a root of the Bernstein–Sato polynomial $b_f(s)$.

The same statements are conjectured for the **topological zeta function** $Z_{\mathrm{top},f}(s)$ of Denef–Loeser and for the **motivic zeta function** $Z_{\mathrm{mot},f}(T)$; the motivic version implies the others. A complete proof must handle arbitrary $n$ and arbitrary singularities, including non-isolated ones. A disproof requires exhibiting one $f$ with a genuine pole whose real part fails the eigenvalue condition — no candidate has survived scrutiny.

## 2. Mathematical Foundations

**Resolution and numerical data.** Let $h: Y \to \mathbb{C}^n$ (resp. over $\mathbb{Q}_p$) be an embedded resolution of $f^{-1}(0)$, with $h^{-1}(f^{-1}(0)) = \bigcup_{i \in S} E_i$ a simple normal crossings divisor. For each $i$ let $N_i$ be the multiplicity of $E_i$ in $\operatorname{div}(f \circ h)$ and $\nu_i - 1$ its multiplicity in the relative canonical divisor $K_{Y/\mathbb{C}^n}$. For $I \subseteq S$ put $E_I = \bigcap_{i \in I} E_i$ and $E_I^\circ = E_I \setminus \bigcup_{j \notin I} E_j$.

**Denef's formula** gives, for almost all $p$,

$$Z_{f,p}(s) \;=\; \sum_{I \subseteq S} (p-1)^{|I|}\, \frac{|\overline{E_I^\circ}(\mathbb{F}_p)|}{p^{n}} \prod_{i \in I} \frac{1}{p^{\nu_i + N_i s} - 1}.$$

**Topological zeta function** (Denef–Loeser 1992), obtained as a limit $p \to 1$:

$$Z_{\mathrm{top},f}(s) \;=\; \sum_{I \subseteq S} \chi\!\left(E_I^\circ\right) \prod_{i \in I} \frac{1}{\nu_i + N_i s},$$

independent of the resolution. The **candidate poles** are $s = -\nu_i/N_i$. The largest is $-\operatorname{lct}(f) = -\min_i \nu_i/N_i$, the negative log canonical threshold.

**Monodromy.** Near $x \in f^{-1}(0)$ the Milnor fibration gives a fibre $F_x$ with quasi-unipotent monodromy $M_x$ acting on $H^\bullet(F_x;\mathbb{C})$. A'Campo's formula computes its zeta function from the same resolution data:

$$\zeta_x(t) \;=\; \prod_{i \in S} \left(1 - t^{N_i}\right)^{-\chi(E_i^\circ \cap h^{-1}(x))}.$$

**Bernstein–Sato polynomial.** $b_f(s)$ is the monic generator of the ideal of $b(s)$ with $P(s) f^{s+1} = b(s) f^s$ for some $P(s) \in \mathcal{D}[s]$. By Kashiwara and Malgrange, $b_f$ has negative rational roots and $\{e^{2\pi i \alpha} : b_f(\alpha)=0\}$ is exactly the set of local monodromy eigenvalues. Hence the chain of implications

$$\text{pole of } Z_f \;\Longrightarrow\; \text{root of } b_f \;\Longrightarrow\; \text{monodromy eigenvalue}.$$

The essential difficulty is that the poles form a small, unpredictable subset of the candidate poles $\{-\nu_i/N_i\}$: massive cancellation occurs, and only the survivors must be explained.

## 3. History & State of the Art (SOTA)

- **1974–75.** Igusa proves rationality of $Z_{f,p}$ in $p^{-s}$ via Hironaka resolution ("Complex powers and asymptotic expansions"), and observes numerically that poles match monodromy eigenvalues.
- **1980s.** Igusa formulates the conjecture; it enters wide circulation through Denef's Séminaire Bourbaki report (1991).
- **1988.** Loeser proves the strong (Bernstein–Sato) form for plane curves, $n=2$, using Newton pairs and Puiseux data.
- **1990.** Loeser proves it for Newton-nondegenerate $f$ in any $n$ under extra numerical conditions on the Newton polyhedron.
- **1992.** Denef–Loeser introduce $Z_{\mathrm{top},f}$; **1998** the motivic zeta function, giving the conjecture its modern "motivic monodromy property" formulation.
- **1995–97.** Veys determines exactly which candidate poles are poles for curves, clarifying cancellation.
- **2002–05.** Artal Bartolo–Cassou-Noguès–Luengo–Melle-Hernández settle superisolated surface singularities and quasi-ordinary hypersurfaces.
- **2011.** Budur–Mustaţă–Teitler reduce hyperplane arrangements to the "$n/d$ conjecture"; Lemahieu–Van Proeyen settle nondegenerate surface singularities.
- **2016–17.** Nicaise–Xu prove the maximal-order-pole case in full generality; Walther (with an appendix by M. Saito) proves the $n/d$ conjecture, completing reduced hyperplane arrangements.
- **2020s.** Log-smooth and tropical methods (Bultot–Nicaise; Nicaise–Payne) extend motivic computations to degenerations and non-hypersurface settings.

The conjecture remains open for $n \geq 3$ in general and even for arbitrary surfaces in $\mathbb{C}^3$.

## 4. Partial Results / Verified Cases

| Class | Result | Reference |
|---|---|---|
| $n = 2$ (plane curves), all singularities | Strong form (Bernstein–Sato) proved | Loeser 1988; Veys 1995/97 |
| Newton-nondegenerate, any $n$, extra conditions | Proved | Loeser 1990 |
| Newton-nondegenerate surfaces ($n=3$) | Proved, topological and $p$-adic | Lemahieu–Van Proeyen 2011; Bories–Veys 2016 |
| Superisolated surface singularities | Proved (modulo a case tied to a rational cuspidal curve question) | Artal Bartolo et al. 2002 |
| Quasi-ordinary hypersurfaces, any $n$ | Proved | Artal Bartolo et al. 2005 |
| Reduced hyperplane arrangements, any $n$ | Proved (topological zeta function) | Budur–Mustaţă–Teitler 2011 + Walther 2017 |
| Largest pole $-\operatorname{lct}(f)$, when of maximal order $n$ | Proved in general | Nicaise–Xu 2016 |
| Abelian varieties / degenerations | Motivic monodromy property proved | Halle–Nicaise 2011 |
| Homogeneous polynomials in $3$ variables | Proved | Veys (via curve case on $\mathbb{P}^2$) |

Computationally, the conjecture has been checked on large families (e.g. all Newton-nondegenerate polynomials with small Newton polyhedra in $n \le 4$) using resolution and toric algorithms; no counterexample is known.

## 5. Principal Obstacles

- **Cancellation is not understood.** For $n \geq 3$, most candidate poles $-\nu_i/N_i$ are not poles. There is no intrinsic criterion — independent of a chosen resolution — deciding which survive. Curves work because Veys's criterion (poles come from divisors that are "log canonical model" divisors) is available; the analogous criterion in higher dimension is unknown.
- **Resolution data is coordinate-dependent and unbounded.** Hironaka resolutions in $n \ge 3$ are not canonical enough to give uniform numerical control; different resolutions produce wildly different $(\nu_i, N_i)$ lists with the same zeta function.
- **Monodromy eigenvalues are not local-to-global compatible.** Eigenvalues at nearby points of $f^{-1}(0)$ may differ; the conjecture allows *any* point of the zero locus, so one must match a global analytic invariant (the pole) with a pointwise topological one, with no map between them.
- **The Bernstein–Sato polynomial is not computable in practice.** $b_f(s)$ is a $\mathcal{D}$-module invariant with no resolution formula; even for explicit surfaces its roots are hard. So the "strong form" bridge is often unusable.
- **Non-isolated singularities.** For non-isolated singular loci the Milnor fibre is not a bouquet of spheres, the mixed Hodge structure is complicated, and A'Campo's formula only gives the *alternating product* of characteristic polynomials — eigenvalues can cancel in $\zeta_x(t)$ while genuinely existing.
- **$p$-adic vs. topological gap.** The $p$-adic case carries point-count data $|\overline{E_I^\circ}(\mathbb{F}_p)|$ (not just Euler characteristics), so proofs of the topological version do not automatically transfer; each has been settled separately in the known classes.

## 6. The Gap

Proven cases share one feature: an explicit combinatorial model of the resolution (Newton polyhedra, toric data, Puiseux pairs, arrangement lattices) that makes the cancellation transparent. The gap is precisely the absence of such a model for a general singularity in $n \ge 3$.

Concretely, the missing step is a **resolution-independent characterisation of the actual poles of $Z_{\mathrm{top},f}$** — a statement of the form "$s_0$ is a pole iff $s_0 = -\nu_E/N_E$ for a divisor $E$ occurring on the log canonical model of $(\mathbb{C}^n, f^{-1}(0))$ with prescribed contact conditions" — together with a geometric mechanism attaching a monodromy eigenvector to each such $E$. Nicaise–Xu supply this for the single largest pole of maximal order; nothing is known for smaller poles or lower order.

## 7. Current Research (as of June 2026)

- **Motivic/non-archimedean school** (Nicaise, Xu, Bultot, Payne; KU Leuven, Imperial, Yale/Texas). Log-smooth models and the tropical motivic Fubini theorem compute $Z_{\mathrm{mot},f}$ on degenerations, targeting the "motivic monodromy property" for classes of degenerations rather than hypersurface germs.
- **$\mathcal{D}$-module school** (Budur, Bath, Walther, Saito; Leuven, Purdue, Osaka/RIMS). Bernstein–Sato *varieties* and multivariate $b$-functions extend the strong form to non-reduced and multi-hypersurface settings; the reduced-arrangement case is now a template. *(frontier — verify)* Extensions to free and non-reduced arrangements are in preprint form.
- **Toric and Newton-polyhedron methods** (Veys, Lemahieu, Nguyen, Esterov; Leuven, Lille, HSE). Push nondegenerate results beyond $n=3$; the $n=4$ nondegenerate case is the immediate target. *(frontier — verify)*
- **Positive characteristic and $F$-thresholds** (Mustaţă, Blickle, Zhu). Test-ideal analogues of $b_f$ give reduction-mod-$p$ constraints on candidate poles.
- **Hodge-theoretic input** (Mustaţă–Popa Hodge ideals; Saito's microlocal $V$-filtration) increasingly supplies the eigenvalue side by bounding roots of $b_f$ from Hodge filtration jumps.

## 8. Future Work

- Prove a **pole-selection theorem**: identify the poles of $Z_{\mathrm{top},f}$ with divisorial valuations that are log canonical places or jumping-number places of the pair $(\mathbb{C}^n, c \cdot f^{-1}(0))$.
- Settle **Newton-nondegenerate $f$ in all dimensions** without Loeser's auxiliary conditions — widely viewed as the next reachable milestone.
- Prove the conjecture for **all surfaces in $\mathbb{C}^3$**, using the classification of normal surface singularities and their resolution graphs.
- Establish the **motivic monodromy property** in general; it implies all other versions and is the formulation with the best functorial behaviour.
- Extend the **strong form to ideals/tuples** via Bernstein–Sato varieties, where the conjecture becomes a statement about the arrangement of hyperplanes in the Bernstein–Sato variety.
- Develop **effective algorithms** for $b_f(s)$ on non-isolated singularities to widen computational testing beyond curves and arrangements.

## 9. Key References

- **[Foundational]** J.-I. Igusa. *Complex powers and asymptotic expansions I, II.* J. Reine Angew. Math. **268/269** (1974), 110–130; **278/279** (1975), 307–321.
- **[Foundational]** J.-I. Igusa. *An Introduction to the Theory of Local Zeta Functions.* AMS/IP Studies in Advanced Mathematics **14**, American Mathematical Society, 2000.
- **[Foundational]** N. A'Campo. *La fonction zêta d'une monodromie.* Comment. Math. Helv. **50** (1975), 233–248.
- **[Foundational]** M. Kashiwara. *B-functions and holonomic systems.* Invent. Math. **38** (1976), 33–53.
- **[Foundational]** B. Malgrange. *Polynômes de Bernstein–Sato et cohomologie évanescente.* Astérisque **101–102** (1983), 243–267.
- **[Foundational]** J. Denef, F. Loeser. *Caractéristiques d'Euler-Poincaré, fonctions zêta locales et modifications analytiques.* J. Amer. Math. Soc. **5** (1992), 705–720.
- **[Foundational]** J. Denef, F. Loeser. *Motivic Igusa zeta functions.* J. Algebraic Geom. **7** (1998), 505–537.
- **[Partial results]** F. Loeser. *Fonctions d'Igusa $p$-adiques et polynômes de Bernstein.* Amer. J. Math. **110** (1988), 1–21.
- **[Partial results]** F. Loeser. *Fonctions d'Igusa $p$-adiques, polynômes de Bernstein, et polyèdres de Newton.* J. Reine Angew. Math. **412** (1990), 75–96.
- **[Partial results]** W. Veys. *Zeta functions for curves and log canonical models.* Proc. London Math. Soc. **74** (1997), 360–378.
- **[Partial results]** E. Artal Bartolo, P. Cassou-Noguès, I. Luengo, A. Melle-Hernández. *Monodromy conjecture for some surface singularities.* Ann. Sci. École Norm. Sup. (4) **35** (2002), 605–640.
- **[Partial results]** E. Artal Bartolo, P. Cassou-Noguès, I. Luengo, A. Melle-Hernández. *Quasi-ordinary power series and their zeta functions.* Mem. Amer. Math. Soc. **178** (2005), no. 841.
- **[Partial results]** N. Budur, M. Mustaţă, Z. Teitler. *The monodromy conjecture for hyperplane arrangements.* Geom. Dedicata **153** (2011), 131–137.
- **[Partial results]** A. Lemahieu, L. Van Proeyen. *Monodromy conjecture for nondegenerate surface singularities.* Trans. Amer. Math. Soc. **363** (2011), 4801–4829.
- **[Partial results]** L. H. Halle, J. Nicaise. *Motivic zeta functions of abelian varieties, and the monodromy conjecture.* Adv. Math. **227** (2011), 610–653.
- **[SOTA / Recent]** J. Nicaise, C. Xu. *Poles of maximal order of motivic zeta functions.* Duke Math. J. **165** (2016), 217–243.
- **[SOTA / Recent]** B. Bories, W. Veys. *Igusa's $p$-adic local zeta function and the monodromy conjecture for non-degenerate surface singularities.* Mem. Amer. Math. Soc. **242** (2016), no. 1145.
- **[SOTA / Recent]** U. Walther. *The Jacobian module, the Milnor fiber, and the $\mathcal{D}$-module generated by $f^s$.* Invent. Math. **207** (2017), 1239–1287 (with an appendix by M. Saito).
- **[SOTA / Recent]** E. Bultot, J. Nicaise. *Computing motivic zeta functions on log smooth models.* Math. Z. **295** (2020), 427–462.
- **[Survey]** J. Denef. *Report on Igusa's local zeta function.* Séminaire Bourbaki, exp. 741, Astérisque **201–203** (1991), 359–386.
- **[Survey]** J. Nicaise. *An introduction to $p$-adic and motivic zeta functions and the monodromy conjecture.* In *Algebraic and Analytic Aspects of Zeta Functions and $L$-functions*, MSJ Memoirs **21** (2010), 141–166.
- **[Survey]** N. Budur. *Bernstein–Sato polynomials.* Lecture notes, KU Leuven, 2015.

## 10. Worked Example / Concrete Special Case

Take the cusp $f(x,y) = x^2 + y^3$ at the origin in $\mathbb{C}^2$.

**Resolution.** Three point blow-ups resolve $f^{-1}(0)$. The exceptional divisors and strict transform $E_0$ carry

$$(N_0,\nu_0)=(1,1),\quad (N_1,\nu_1)=(2,2),\quad (N_2,\nu_2)=(3,3),\quad (N_3,\nu_3)=(6,5).$$

The dual graph is a star: $E_3$ meets $E_1$, $E_2$ and $E_0$; no other pair meets. Hence $E_1^\circ \cong \mathbb{P}^1 \setminus \{1 \text{ pt}\}$ ($\chi=1$), $E_2^\circ \cong \mathbb{P}^1\setminus\{1\}$ ($\chi=1$), $E_3^\circ \cong \mathbb{P}^1 \setminus \{3 \text{ pts}\}$ ($\chi=-1$), and $E_0^\circ \cap h^{-1}(0) = \varnothing$.

**Local topological zeta function.**

$$Z_{\mathrm{top},f,0}(s)=\frac{1}{2+2s}+\frac{1}{3+3s}-\frac{1}{5+6s}+\frac{1}{(2+2s)(5+6s)}+\frac{1}{(3+3s)(5+6s)}+\frac{1}{(1+s)(5+6s)}.$$

Putting everything over $6(s+1)(6s+5)$:

$$Z_{\mathrm{top},f,0}(s) \;=\; \frac{5}{6(s+1)} + \frac{5-6s}{6(s+1)(6s+5)} \;=\; \frac{4s+5}{(s+1)(6s+5)}.$$

Check: $Z_{\mathrm{top},f,0}(0) = 5/5 = 1$, as required.

**Candidate poles vs. actual poles.** The candidate set is $\{-1, -1, -1, -5/6\}$ (from $\nu_i/N_i = 1/1, 2/2, 3/3, 5/6$). Both $-1$ and $-5/6$ survive here; in higher dimension the analogous list typically collapses.

**Monodromy side.** The Milnor fibre of the cusp has $\mu = (2-1)(3-1) = 2$, and the characteristic polynomial of the monodromy on $H^1$ is $t^2 - t + 1$, whose roots are the primitive $6$th roots of unity $e^{\pm 2\pi i/6}$. On $H^0$ the eigenvalue is $1$.

- Pole $s_0 = -1$: $e^{2\pi i(-1)} = 1$, an eigenvalue on $H^0(F)$. ✓
- Pole $s_0 = -5/6$: $e^{-2\pi i \cdot 5/6} = e^{2\pi i/6}$, a primitive $6$th root of unity, an eigenvalue on $H^1(F)$. ✓

**Strong form.** Here $b_f(s) = (s+1)\left(s+\tfrac{5}{6}\right)\left(s+\tfrac{7}{6}\right)$. Both poles appear among its roots, while $-7/6$ is a root that is *not* a pole — an explicit instance of the strict inclusion $\{\text{poles}\} \subsetneq \{\text{roots of } b_f\} $ that makes the conjecture delicate.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*