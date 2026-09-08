---
id: 03-geometry/classification-ancient-ricci-flows
title: "Cartan-Hadamard Conjecture for Ricci Flow Singularities: Uniqueness of Ancient Solutions"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cartan-Hadamard Conjecture for Ricci Flow Singularities: Uniqueness of Ancient Solutions

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/classification-ancient-ricci-flows` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Singularity models of the Ricci flow are *ancient solutions*: flows defined on $(-\infty, T)$. The classification problem asks for a complete list of them under the curvature and non-collapsing hypotheses that blow-up limits automatically inherit. The name attached here records the intended analogy with Cartan–Hadamard-type rigidity: a curvature sign condition plus a completeness/non-collapsing condition should force a *unique* model geometry, with no moduli.

**Conjecture (classification of $\kappa$-solutions).** Let $(M^n, g(t))$, $t \in (-\infty,0)$, be a complete non-flat ancient Ricci flow that is $\kappa$-noncollapsed at all scales, has bounded curvature on compact time intervals, and has nonnegative curvature operator (in dimension 3, nonnegative sectional curvature is automatic by Hamilton–Ivey). Then $(M,g(t))$ is isometric, up to scaling, parabolic rescaling and time translation, to one of an explicit finite list of models.

In dimension $3$ the list is conjectured (and now proved) to be:

1. the shrinking round sphere $S^3$ and its metric quotients;
2. the shrinking round cylinder $S^2 \times \mathbb{R}$ and its $\mathbb{Z}_2$-quotient;
3. the Bryant steady soliton;
4. Perelman's noncompact ancient solution on $S^2 \times \mathbb R$'s one-point... i.e. Perelman's $\kappa$-solution on $\mathbb R^3$;
5. the family of compact rotationally symmetric *ancient ovals* on $S^3$.

**Open general statement.** In dimensions $n \ge 4$ no finite list is known, and it is open whether the moduli of $\kappa$-solutions is even finite-dimensional. A complete resolution means: (i) an explicit classification in each dimension under nonnegative curvature operator and $\kappa$-noncollapsing, or (ii) a counterexample exhibiting a continuous family of pairwise non-homothetic $\kappa$-solutions. Weakening any hypothesis (dropping non-collapsing, or replacing nonnegative curvature operator by weak $\mathrm{PIC}$) changes the answer and must be stated explicitly.

## 2. Mathematical Foundations

**Ricci flow.** A family $g(t)$ of Riemannian metrics on $M^n$ with
$$\partial_t g_{ij} = -2 R_{ij}, \qquad \partial_t R = \Delta R + 2|\mathrm{Ric}|^2 .$$

**Ancient solution.** A solution defined for all $t \in (-\infty, T)$.

**Solitons.** $(M,g,f,\lambda)$ is a gradient Ricci soliton if
$$R_{ij} + \nabla_i\nabla_j f = \lambda\, g_{ij},$$
shrinking, steady or expanding for $\lambda > 0$, $=0$, $<0$. Every soliton generates an ancient solution by $g(t) = (1-2\lambda t)\,\varphi_t^* g$.

**$\kappa$-noncollapsing.** $(M,g)$ is $\kappa$-noncollapsed at scale $\rho$ if for every $r < \rho$ and $x$ with $|\mathrm{Rm}| \le r^{-2}$ on $B(x,r)$, one has $\mathrm{vol}\, B(x,r) \ge \kappa r^n$. Perelman's monotone entropy
$$\mathcal{W}(g,f,\tau) = \int_M \big[\tau(R + |\nabla f|^2) + f - n\big](4\pi\tau)^{-n/2}e^{-f}\,dV$$
gives $\kappa$-noncollapsing along any smooth flow with bounded geometry.

**$\kappa$-solution.** Ancient, complete, non-flat, bounded curvature on compact time intervals, nonnegative curvature operator, $\kappa$-noncollapsed at all scales. Perelman's theory shows every finite-time singularity of a 3-dimensional closed Ricci flow has blow-up limits that are $\kappa$-solutions; this is exactly why classification controls surgery.

**Asymptotic soliton.** For a $\kappa$-solution, the rescaled backward limits $\tau^{-1} g(-\tau)$, $\tau \to \infty$, subconverge to a nonflat gradient shrinking soliton (Perelman, §11).

**Key rigidity inputs.** Hamilton's strong maximum principle for $\mathrm{Rm}$; Hamilton–Ivey pinching in dimension 3, $R \ge |\mathrm{Rm}|\,\phi(|\mathrm{Rm}|)$-type estimates forcing nonnegative sectional curvature on ancient 3-flows; Harnack inequality $\partial_t R + 2\langle \nabla R, V\rangle + 2\mathrm{Ric}(V,V) \ge 0$ for nonnegatively curved solutions.

**Explicit models.** Bryant soliton: rotationally symmetric steady gradient soliton on $\mathbb{R}^n$, $g = dr^2 + \varphi(r)^2 g_{S^{n-1}}$ with $\varphi(r) \sim \sqrt{r}$ and $R \sim c/r$. Round shrinking sphere: $g(t) = -2(n-1)t\, g_{S^n}$.

## 3. History & State of the Art (SOTA)

- **1982.** Hamilton introduces Ricci flow; the cigar/Witten soliton on $\mathbb{R}^2$ is the first nontrivial ancient example.
- **1988–95.** Hamilton's Harnack inequality and singularity classification (Type I/II/III) put ancient solutions at the center of the theory.
- **2002–03.** Perelman's entropy and no-local-collapsing theorems define $\kappa$-solutions, prove compactness of the space of 3-dimensional $\kappa$-solutions, and prove the *canonical neighborhood theorem*. He states the classification in dimension 3 and constructs the rotationally symmetric noncompact $\kappa$-solution on $\mathbb{R}^3$ that carries his name.
- **2005.** Bryant's explicit construction/uniqueness of the rotationally symmetric steady soliton in dimension 3.
- **2012.** Daskalopoulos–Hamilton–Sesum classify *all* compact ancient solutions on surfaces: round sphere and the King–Rosenau "sausage".
- **2013.** Brendle proves rotational symmetry of 3-dimensional non-flat $\kappa$-noncollapsed steady gradient solitons: they are the Bryant soliton.
- **2020–2023.** The 3-dimensional conjecture is completed: Brendle (noncompact case, *Acta* 2020), Brendle–Daskalopoulos–Sesum (compact case, *Invent. Math.* 2021), with Bamler–Kleiner giving an independent route to rotational symmetry of 3d $\kappa$-solutions. Angenent–Brendle–Daskalopoulos–Sesum supply the sharp asymptotics of ancient ovals used in the uniqueness argument.
- **2023–present.** Higher dimensions: uniqueness of compact ancient solutions with uniformly $\mathrm{PIC}$ and weakly $\mathrm{PIC2}$, and Bamler's partial-regularity/compactness theory for Ricci flows, which shows singular sets of noncollapsed limits have codimension $\ge 4$.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n=2$, compact | Exactly: round shrinking $S^2$, King–Rosenau solution | Daskalopoulos–Hamilton–Sesum 2012 |
| $n=2$, complete noncollapsed | Round sphere, cylinder, cigar (collapsed) | Hamilton; Chu |
| $n=3$, steady gradient solitons, $\kappa$-noncollapsed | Bryant soliton, unique | Brendle 2013 |
| $n=3$, noncompact $\kappa$-solutions | Cylinder/quotient or Bryant | Brendle 2020 (*Acta* 225) |
| $n=3$, compact $\kappa$-solutions | Round $S^3$/quotients or the ancient ovals | Brendle–Daskalopoulos–Sesum 2021 |
| $n \ge 4$, compact, uniformly $\mathrm{PIC}$ + weakly $\mathrm{PIC2}$, noncollapsed | Round sphere or the $(n)$-dimensional ancient oval | Brendle–Daskalopoulos–Naff–Sesum 2023 |
| $n\ge 4$, noncompact, uniformly $\mathrm{PIC}$, noncollapsed | Rotational symmetry; Bryant or cylinder | Brendle–Naff |
| Type I ancient, closed, any $n$ | Backward limit is a nontrivial shrinking soliton | Ni 2010 |
| 4-dim shrinking solitons | Classified under nonnegative curvature operator; $S^4, S^3\times\mathbb R, S^2\times\mathbb R^2, \mathbb{CP}^2$-type quotients | Munteanu–Wang; Li–Wang |

Additionally, all $3$-dimensional results are effective enough to yield the canonical-neighborhood constants used in Ricci flow with surgery and in Kleiner–Lott/Bamler–Kleiner singular Ricci flows (existence and *uniqueness* of the flow through singularities in dimension 3).

## 5. Principal Obstacles

- **No Hamilton–Ivey pinching for $n \ge 4$.** In dimension 3 nonnegative sectional curvature comes free on ancient flows. In higher dimensions one must *assume* a curvature condition, and each choice ($\mathrm{PIC}$, $\mathrm{PIC1}$, $\mathrm{PIC2}$, nonnegative curvature operator) gives a different, incomparable classification problem.
- **Failure of soliton rigidity.** The Brendle-type arguments work by (a) identifying the backward asymptotic soliton as a cylinder, (b) proving the *neck improvement* theorem showing approximate rotational symmetry propagates, (c) upgrading to exact symmetry via a Lie-derivative/ODE argument on the linearized operator. Step (a) breaks in higher dimensions because the list of shrinking solitons is itself unclassified — e.g. Bamler–Cifarelli–Conlon–Deruelle produced a new complete non-Kähler-trivial shrinking gradient Kähler–Ricci soliton in complex dimension 2, showing the soliton zoo is richer than expected.
- **Non-uniqueness of tangent flows.** Without a Łojasiewicz-type inequality for Perelman's entropy at general shrinkers, different sequences $\tau_i \to \infty$ may a priori give non-isometric backward limits; only in dimension 3 (and in the $\mathrm{PIC}$ setting) is this ruled out.
- **Analytic degeneracy at the tips.** Ancient ovals are Type II: $\sup R \not\to 0$ backwards. The linearized operator on the neck has an infinite-dimensional kernel of "slowly decaying" modes; separating the neutral modes from unstable ones requires the sharp asymptotics of Angenent–Brendle–Daskalopoulos–Sesum, which are proved by delicate matched asymptotics not currently available in $n\ge5$ without $\mathrm{PIC}$.
- **Collapsed ancient solutions.** Dropping $\kappa$-noncollapsing admits the cigar and infinitely many homogeneous ancient solutions on nilmanifolds — no finite classification exists there.

## 6. The Gap

Proven: the full 3-dimensional list, and in $n \ge 4$ the classification *conditional on* uniform $\mathrm{PIC}$ (plus weak $\mathrm{PIC2}$ in the compact case). Conjectured: the same finiteness with $\mathrm{PIC}$ replaced by nonnegative curvature operator, or with no curvature assumption beyond what blow-ups of *general* singularities inherit.

The precise barrier has two links:

1. **Classify $n$-dimensional shrinking gradient solitons with nonnegative curvature operator and bounded curvature.** Without this, the asymptotic soliton in Perelman's backward-limit theorem is an unknown object, and no neck structure can be asserted.
2. **Prove uniqueness of the backward asymptotic soliton** (an entropy Łojasiewicz inequality at every shrinker), so that "the flow is asymptotic to a cylinder" is a well-posed starting hypothesis rather than a subsequential statement.

Crossing link 1 for $n = 4$ under nonnegative curvature operator would already close the 4-dimensional case, since neck improvement and the rotational-symmetry machinery are dimension-independent once the neck model is known.

## 7. Current Research (as of June 2026)

- **Columbia/Rutgers school (Brendle, Daskalopoulos, Sesum, Naff, Angenent).** Continues the $\mathrm{PIC}$ program; the open target is removing "uniformly" from uniformly $\mathrm{PIC}$ and handling $\mathrm{PIC1}$ in $n=4$.
- **Berkeley/NYU (Bamler, Kleiner).** Partial regularity and $\mathbb{F}$-convergence theory for Ricci flows; codimension-4 structure of singular sets in noncollapsed limits, and applications to spaces of metrics. A metric-measure formulation of ancient solutions ("metric flows") is being used to attack compactness without curvature bounds. *(frontier — verify)*
- **Soliton constructions (Conlon, Deruelle, Cifarelli, Sun).** New shrinking and steady Kähler–Ricci solitons; each new example constrains any conjectural classification list in $n\ge4$.
- **4-dimensional ancient flows with symmetry.** Cohomogeneity-one and $\mathrm{U}(2)$-invariant ancient solutions are being classified numerically and by ODE shooting arguments. *(frontier — verify)*
- **Mean curvature flow transfer.** The Angenent–Daskalopoulos–Sesum classification of compact ancient MCF ovals and the Brendle–Choi noncompact result supply the template; the analogies (bowl $\leftrightarrow$ Bryant, oval $\leftrightarrow$ oval) are being transported in both directions.

## 8. Future Work

- Prove an entropy Łojasiewicz–Simon inequality at cylindrical shrinkers in all dimensions; this alone would give uniqueness of tangent flows and remove the subsequence issue in Section 6.
- Classify 4-dimensional shrinking gradient solitons with bounded scalar curvature — a step short of full nonnegative curvature operator, and possibly reachable via Munteanu–Wang's structure theory.
- Extend neck improvement to necks modeled on $S^{k}\times \mathbb{R}^{n-k}$ with $k < n-1$, where the isometry group of the model is larger and the current rotational-symmetry ODE argument degenerates.
- Determine whether the moduli space of $n$-dimensional $\kappa$-solutions is compact modulo scaling for $n = 4$; Perelman proved this for $n=3$.
- Produce a counterexample: a continuous family of $\kappa$-solutions in some dimension would settle the general conjecture negatively and reshape higher-dimensional surgery programs.

## 9. Key References

- **[Foundational]** G. Perelman. *The entropy formula for the Ricci flow and its geometric applications.* arXiv:math/0211159, 2002.
- **[Foundational]** R. S. Hamilton. *The formation of singularities in the Ricci flow.* Surveys in Differential Geometry, Vol. II, International Press, 1995, 7–136.
- **[Foundational]** R. Bryant. *Ricci flow solitons in dimension three with SO(3)-symmetries.* Preprint, Duke University, 2005.
- **[Partial result]** P. Daskalopoulos, R. Hamilton, N. Sesum. *Classification of ancient compact solutions to the Ricci flow on surfaces.* Journal of Differential Geometry 91 (2012), 171–214.
- **[Partial result]** S. Brendle. *Rotational symmetry of self-similar solutions to the Ricci flow.* Inventiones Mathematicae 194 (2013), 731–764.
- **[SOTA]** S. Brendle. *Ancient solutions to the Ricci flow in dimension 3.* Acta Mathematica 225 (2020), 1–102.
- **[SOTA]** S. Brendle, P. Daskalopoulos, N. Sesum. *Uniqueness of compact ancient solutions to three-dimensional Ricci flow.* Inventiones Mathematicae 226 (2021), 579–651.
- **[SOTA]** S. Angenent, S. Brendle, P. Daskalopoulos, N. Sesum. *Unique asymptotics of compact ancient solutions to three-dimensional Ricci flow.* Communications on Pure and Applied Mathematics 75 (2022), 1032–1073.
- **[SOTA]** S. Brendle, P. Daskalopoulos, K. Naff, N. Sesum. *Uniqueness of compact ancient solutions to the higher-dimensional Ricci flow.* Journal für die reine und angewandte Mathematik (Crelle) 795 (2023), 85–138.
- **[SOTA]** R. Bamler, B. Kleiner. *On the rotational symmetry of 3-dimensional $\kappa$-solutions.* Journal für die reine und angewandte Mathematik (Crelle) 764 (2020), 287–304.
- **[SOTA]** R. Bamler, B. Kleiner. *Uniqueness and stability of Ricci flow through singularities.* Acta Mathematica 228 (2022), 1–215.
- **[SOTA]** R. Bamler. *Compactness theory of the space of super Ricci flows.* Inventiones Mathematicae 233 (2023), 1121–1277.
- **[SOTA]** R. Bamler, C. Cifarelli, R. Conlon, A. Deruelle. *A new complete two-dimensional shrinking gradient Kähler–Ricci soliton.* Geometric and Functional Analysis 34 (2024), 377–406.
- **[Related]** B. Kleiner, J. Lott. *Singular Ricci flows I.* Acta Mathematica 219 (2017), 65–134.
- **[Survey]** H.-D. Cao, B.-L. Chen, X.-P. Zhu. *Recent developments on Hamilton's Ricci flow.* Surveys in Differential Geometry, Vol. XII, International Press, 2008, 47–112.
- **[Book]** B. Chow et al. *The Ricci Flow: Techniques and Applications, Parts I–IV.* Mathematical Surveys and Monographs, American Mathematical Society, 2007–2015.

## 10. Worked Example / Concrete Special Case

**The King–Rosenau ancient solution on $S^2$, verified by hand.** This is the smallest nontrivial member of the conjectural list: a compact ancient solution that is *not* a soliton.

Write $S^2 \setminus \{N,S\}$ conformally as the cylinder $\mathbb{R}\times S^1$ with coordinates $(s,\theta)$ and set $g = u(s,t)\,(ds^2 + d\theta^2)$. In dimension 2, $\mathrm{Ric} = \tfrac{1}{2}R\,g$ and $R = -u^{-1}(\log u)_{ss}$, so Ricci flow reduces to the logarithmic fast-diffusion equation
$$u_t = (\log u)_{ss}.$$

Try the ansatz $u = A(t)/(\cosh s + B(t))$. Then
$$(\log u)_{ss} = -\frac{B\cosh s + 1}{(\cosh s + B)^2}, \qquad u_t = \frac{A'\cosh s + (A'B - AB')}{(\cosh s + B)^2}.$$
Matching coefficients of $\cosh s$ and the constant term gives the system
$$A' = -B, \qquad A'B - AB' = -1 \;\Longrightarrow\; AB' = 1 - B^2 .$$
Set $\tau = -t > 0$. Then $A_\tau = B$ and $B_\tau = (B^2-1)/A$. The choice $A = \sinh\tau$, $B = \cosh\tau$ satisfies both: $A_\tau = \cosh\tau = B$ and $(B^2-1)/A = \sinh^2\tau/\sinh\tau = \sinh\tau = B_\tau$. Hence
$$\boxed{\,u(s,t) = \frac{\sinh(-t)}{\cosh s + \cosh(-t)}\,}, \qquad t \in (-\infty,0).$$

**Reading off the geometry.** The scalar curvature is
$$R(s,t) = \frac{\cosh\tau\,\cosh s + 1}{\sinh\tau\,(\cosh s + \cosh\tau)} .$$

- At the *equator* $s=0$: $R = \dfrac{\cosh\tau + 1}{\sinh\tau(1+\cosh\tau)} = \dfrac{1}{\sinh\tau}$, which $\to \infty$ as $\tau \to 0^+$ (extinction at $t=0$) and $\to 0$ as $\tau\to\infty$.
- At the *tips* $s \to \pm\infty$: $R \to \coth\tau \to 1$ as $\tau\to\infty$.

So $\sup_M R$ does **not** decay backwards: the solution is Type II, and its two ends look like cigar solitons while its middle looks like a longer and longer flat cylinder ($u \to 1$ pointwise as $\tau\to\infty$). That is exactly the "ancient oval" picture — a cylinder capped by two soliton tips — that Brendle–Daskalopoulos–Sesum prove is the *only* alternative to the round sphere among compact 3-dimensional $\kappa$-solutions.

Contrast with the round shrinking sphere $g(t) = -2(n-1)t\,g_{S^n}$: since $\mathrm{Ric}(c\,g_{S^n}) = (n-1)g_{S^n}$ is scale-invariant, $\partial_t g = c'(t) g_{S^n} = -2(n-1)g_{S^n}$ holds identically, and $R = n/(-2t) \to 0$ backwards — Type I. The classification conjecture is the assertion that in every dimension, under nonnegative curvature operator and $\kappa$-noncollapsing, these two behaviours (Type I round shrinkers, Type II oval/Bryant models) exhaust the possibilities. It is a theorem for $n \le 3$; for $n \ge 4$ it is known only under $\mathrm{PIC}$-type hypotheses.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*