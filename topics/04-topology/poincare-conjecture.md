---
id: 04-topology/poincare-conjecture
title: "Poincare Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Poincaré Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/poincare-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Statement (Poincaré, 1904).** Every closed, simply connected, smooth $3$-manifold is homeomorphic to the $3$-sphere $S^3$.

Unpacked: let $M$ be a compact connected $3$-manifold without boundary. Assume $\pi_1(M) = 1$. Then $M \cong S^3$.

The conjecture is **proved**. Grigori Perelman posted three preprints in 2002–2003 completing Richard Hamilton's Ricci flow program; the proof was verified by several independent teams by 2006. Perelman was awarded the Fields Medal (2006, declined) and the Clay Millennium Prize (2010, declined). It is the only one of the seven Clay Millennium Problems resolved to date.

Perelman actually proved the much stronger **Geometrization Conjecture** of Thurston, from which Poincaré follows as a corollary. What remains genuinely open in the surrounding circle of ideas is the **smooth $4$-dimensional Poincaré conjecture** (SPC4): is every smooth homotopy $4$-sphere diffeomorphic to $S^4$ with its standard smooth structure? This is treated in Sections 5–8 as the live frontier.

A complete resolution of SPC4 requires either (a) a proof that every smooth homotopy $4$-sphere is standard, or (b) an exotic $S^4$: a smooth manifold homeomorphic but not diffeomorphic to $S^4$.

## 2. Mathematical Foundations

**Manifolds.** A closed $n$-manifold $M$ is a compact Hausdorff second-countable space locally homeomorphic to $\mathbb{R}^n$, without boundary. *Simply connected* means path-connected with trivial fundamental group $\pi_1(M,x_0)=1$.

**Homotopy sphere.** A closed $n$-manifold $\Sigma$ with the homotopy type of $S^n$. For $n=3$, simple connectivity plus Poincaré duality forces $H_*(M;\mathbb{Z}) \cong H_*(S^3;\mathbb{Z})$, and by Hurewicz plus Whitehead, $M \simeq S^3$. So "simply connected closed $3$-manifold" and "homotopy $3$-sphere" coincide.

**Ricci flow.** Given a Riemannian metric $g_0$ on $M$, Hamilton's flow is the parabolic PDE
$$\frac{\partial g_{ij}}{\partial t} = -2\,R_{ij},$$
where $R_{ij}$ is the Ricci curvature. Normalized to preserve volume:
$$\frac{\partial g_{ij}}{\partial t} = -2R_{ij} + \frac{2}{n}\, r\, g_{ij}, \qquad r = \frac{\int_M R \, d\mu}{\int_M d\mu}.$$
Scalar curvature satisfies $\partial_t R = \Delta R + 2|\mathrm{Ric}|^2$, so by the maximum principle $R_{\min}(t)$ is nondecreasing and blowup occurs in finite time when $R_{\min}(0)>0$.

**Perelman's monotone functionals.** The $\mathcal{F}$-entropy
$$\mathcal{F}(g,f) = \int_M \left( R + |\nabla f|^2 \right) e^{-f} \, d\mu$$
and the $\mathcal{W}$-entropy
$$\mathcal{W}(g,f,\tau) = \int_M \left[ \tau\left( R + |\nabla f|^2 \right) + f - n \right] (4\pi\tau)^{-n/2} e^{-f} \, d\mu$$
are nondecreasing along the coupled flow. Monotonicity of $\mathcal{W}$ yields the **no local collapsing theorem**: along the flow on a finite time interval there is $\kappa>0$ with $\mathrm{Vol}(B(x,r)) \ge \kappa r^n$ whenever $|\mathrm{Rm}| \le r^{-2}$ on $B(x,r)$. This rules out the cigar soliton as a blowup limit and makes the singularity classification tractable.

**Reduced length / volume.** For a curve $\gamma$ from $(p,0)$,
$$\mathcal{L}(\gamma) = \int_0^{\bar\tau} \sqrt{\tau}\left( R(\gamma(\tau)) + |\dot\gamma(\tau)|^2 \right) d\tau, \qquad \ell(q,\bar\tau) = \frac{1}{2\sqrt{\bar\tau}} \inf_\gamma \mathcal{L}(\gamma),$$
with reduced volume $\tilde V(\tau) = \int_M (4\pi\tau)^{-n/2} e^{-\ell(q,\tau)} d\mu$ monotone nonincreasing.

**Geometrization.** Every closed orientable $3$-manifold decomposes by connected sum into primes, and each prime piece cuts along incompressible tori (JSJ) into pieces admitting one of Thurston's eight geometries: $S^3$, $\mathbb{E}^3$, $\mathbb{H}^3$, $S^2\times\mathbb{R}$, $\mathbb{H}^2\times\mathbb{R}$, $\widetilde{\mathrm{SL}_2\mathbb{R}}$, Nil, Sol. Simple connectivity kills all but $S^3$; hence Poincaré.

**Smooth structures.** $\Theta_n$, the group of homotopy $n$-spheres under connected sum, is finite for $n \ne 4$ (Kervaire–Milnor). $|\Theta_7| = 28$, $|\Theta_{11}| = 992$, $\Theta_5 = \Theta_6 = 1$. $\Theta_4$ is trivial iff SPC4 holds.

## 3. History & State of the Art (SOTA)

- **1895–1904.** Poincaré's *Analysis Situs* and its complements. In 1900 he claimed homology alone characterizes $S^3$; in 1904 he refuted himself with the **Poincaré homology sphere** $\Sigma(2,3,5) = S^3/I^*$ ($I^*$ the binary icosahedral group of order 120), which has $H_*(\Sigma) \cong H_*(S^3)$ but $\pi_1$ of order $120$. He then posed the question with $\pi_1 = 1$.
- **1960–61.** Smale proves the generalized conjecture (PL/smooth) for $n \ge 5$ by the h-cobordism theorem and handle cancellation; Stallings and Zeeman give independent arguments for $n \ge 5$ in the PL/topological categories.
- **1982.** Freedman classifies simply connected closed topological $4$-manifolds by intersection form plus Kirby–Siebenmann invariant, proving TOP Poincaré in dimension $4$. Fields Medal 1986.
- **1982.** Hamilton introduces Ricci flow and proves: a closed $3$-manifold with $\mathrm{Ric}>0$ admits a metric of constant positive curvature, hence is a spherical space form.
- **1982–86.** Thurston's Geometrization Conjecture and the hyperbolization theorem for Haken manifolds.
- **2002–2003.** Perelman, three arXiv preprints: *The entropy formula for the Ricci flow and its geometric applications* (math.DG/0211159), *Ricci flow with surgery on three-manifolds* (math.DG/0303109), *Finite extinction time...* (math.DG/0307245).
- **2006–2008.** Verification: Kleiner–Lott notes (*Geometry & Topology* 12, 2008), Morgan–Tian book (*Clay Mathematics Monographs* 3, 2007), Cao–Zhu (*Asian J. Math.* 10, 2006). Perelman declines Fields Medal (2006) and Clay Prize (2010).
- **Now.** Attention has shifted to dimension $4$ (SPC4) and to effectivizing Ricci flow with surgery.

## 4. Partial Results / Verified Cases

| Dimension | TOP | PL | DIFF |
|---|---|---|---|
| $1,2$ | true | true | true (classification of surfaces) |
| $3$ | true (Perelman 2003) | true | true (PL $=$ DIFF in dim $\le 3$, Moise) |
| $4$ | true (Freedman 1982) | **open** ($=$ DIFF in dim 4) | **open** |
| $5,6$ | true | true | true ($\Theta_5=\Theta_6=1$) |
| $7$ | true | true | **false** — $|\Theta_7|=28$ exotic spheres (Milnor 1956) |
| $\ge 5$, general | true | true | true up to diffeo-of-homotopy-spheres; $\Theta_n$ finite, often nontrivial |

Additional verified classes bearing on SPC4:

- **Homotopy $4$-spheres with handle decompositions of small complexity.** Every homotopy $4$-sphere admitting a handle decomposition with no $1$- or $3$-handles is standard; more generally, Gluck twists on many families of $2$-knots yield standard $S^4$ (Gluck 1962; Akbulut).
- **Cappell–Shaneson spheres.** Constructed 1976 from mapping tori of $\mathbb{Z}^3$ automorphisms; many were suspected exotic. Akbulut (2010, *Ann. of Math.*) showed the Cappell–Shaneson sphere family with $\det = -1$ is standard; Gompf (2010) showed infinitely many are standard.
- **Gluck twists.** Gluck (1962): twisting along an embedded $S^2 \subset S^4$ gives a homotopy $4$-sphere; standardness proved for ribbon $2$-knots, unknotted $2$-knots, and large computationally checked families.
- **Small Property R / trisections.** All genus-$\le 2$ trisected homotopy $4$-spheres are standard (Meier–Zupan, 2017); genus-$3$ cases partially handled.
- **Elliptic curvature classes in dim 3.** Hamilton's theorem covers $\mathrm{Ric}>0$; Böhm–Wilking extended to $2$-positive curvature operator in all dimensions.

## 5. Principal Obstacles

For dimension $3$: none remain — the theorem is proved. The obstacles that *were* crossed, and the reasons dimension $4$ resists, are the substance here.

- **Whitney trick fails in dimension $4$.** In dimension $n\ge 5$, intersections of submanifolds of complementary dimension can be cancelled by pushing across an embedded Whitney disk. In a $4$-manifold, a Whitney disk has dimension $2$ and its generic self-intersection in a $4$-manifold is $0$-dimensional, so it cannot be made embedded. This kills h-cobordism-style handle cancellation in the smooth category. Freedman recovers it topologically via infinite Casson-handle towers, which produce topological but not smooth structure.
- **Gauge theory has the wrong sign for $S^4$.** Donaldson and Seiberg–Witten invariants detect exotic smooth structures on $4$-manifolds with $b_2^+ > 1$. For a homotopy $4$-sphere, $b_2 = 0$, so all these invariants vanish identically. There is currently **no known invariant that could distinguish an exotic $S^4$ from $S^4$.** This is the central bottleneck: even if an exotic $S^4$ existed, we lack the tool to certify it.
- **Rasmussen $s$-invariant route stalled.** Freedman–Gompf–Morrison–Walker (2010) proposed using Khovanov homology's $s$-invariant to obstruct sliceness of knots in candidate exotic spheres. Their computations found no counterexample among Cappell–Shaneson candidates; later work showed the approach cannot succeed for whole families.
- **Combinatorial explosion in handle calculus.** Certifying a homotopy $4$-sphere is standard means finding a sequence of handle slides and cancellations; the search space is a group-theoretic word problem with no effective bound. Andrews–Curtis Conjecture (balanced presentations of the trivial group reduce to trivial by elementary moves) is a group-theoretic shadow of SPC4 and is itself open, with resistant candidates like $\langle x,y \mid x^{-1}y^{-1}xy = y^{n}, \ldots \rangle$ at low complexity.

## 6. The Gap

Precisely: dimension $3$ has no gap. In dimension $4$ the gap is between Freedman's **topological** classification (every homotopy $4$-sphere is homeomorphic to $S^4$) and the **smooth** statement (is it diffeomorphic?). The missing step is one of:

1. A smooth invariant, vanishing on $S^4$ and nonvanishing on some candidate, that is defined without $b_2^+ > 1$ — nothing in Donaldson/Seiberg–Witten/Heegaard–Floer currently qualifies; or
2. A general handle-cancellation theorem showing every balanced-presentation obstruction can be resolved by stabilization, which would also settle a stable Andrews–Curtis statement.

Note the *stable* result is known: Wall (1964) showed any two homotopy $4$-spheres become diffeomorphic after connected-summing with enough copies of $S^2 \times S^2$. The gap is entirely about unstabilized behaviour.

## 7. Current Research (as of June 2026)

- **Trisections.** Gay–Kirby's trisection theory gives every closed $4$-manifold a decomposition into three handlebodies; Meier, Zupan, and collaborators use bridge trisections to attack SPC4 by genus. Genus-$3$ classification is the current front line *(frontier — verify)*.
- **Khovanov skein lasagna modules.** Morrison–Walker–Wedrich's $S_0$ invariant of $4$-manifolds (2022) is the first candidate to detect exotic smooth structures where Seiberg–Witten fails; Ren–Willis (2024) computed it and distinguished exotic $\mathbb{R}^4$-like pairs. Whether it can be nonvanishing on a homotopy $4$-sphere is an active question *(frontier — verify)*.
- **Computational Andrews–Curtis.** Reinforcement-learning searches (Shehper et al., 2024) trivialized several long-standing Akbulut–Kirby presentations, removing them as SPC4 counterexample candidates.
- **Ricci flow beyond dimension 3.** Bamler's compactness and partial regularity theory for Ricci flows in higher dimensions (Bamler, *Ann. of Math.* / *Acta*, 2020–23), plus Bamler–Kleiner's proof of the Generalized Smale Conjecture and contractibility of $\mathrm{Diff}(M^3)$ components.
- **Groups.** IAS/Princeton (Bamler, Kleiner at NYU), UC Berkeley, Stanford (Zupan network at Nebraska), Michigan State (Akbulut lineage), MPIM Bonn.

## 8. Future Work

- Compute skein lasagna modules for Gluck twists on non-ribbon $2$-knots; a nonzero obstruction would give an exotic $S^4$.
- Settle genus-$3$ and genus-$4$ trisections of homotopy $4$-spheres; Meier–Zupan's genus-$\le 2$ result suggests a possible inductive scheme.
- Resolve the Andrews–Curtis Conjecture for balanced presentations of length $\le 12$; a counterexample would not immediately give an exotic $S^4$ but would sharpen the algebraic barrier.
- Effectivize Ricci flow with surgery: bound surgery count and extinction time in terms of geometric data, giving an algorithmic recognition procedure for $S^3$ (currently Rubinstein–Thompson normal-surface recognition is the effective route, in NP $\cap$ co-NP).
- Extend Bamler's Ricci flow regularity theory to a singularity classification in dimension $4$, which would be the closest analogue of Perelman's dimension-3 argument.

## 9. Key References

- **[Foundational]** H. Poincaré. *Cinquième complément à l'Analysis Situs.* Rendiconti del Circolo Matematico di Palermo, 18:45–110, 1904.
- **[Foundational]** J. Milnor. *On manifolds homeomorphic to the 7-sphere.* Annals of Mathematics, 64(2):399–405, 1956.
- **[Foundational]** S. Smale. *Generalized Poincaré's conjecture in dimensions greater than four.* Annals of Mathematics, 74(2):391–406, 1961.
- **[Foundational]** M. Kervaire, J. Milnor. *Groups of homotopy spheres: I.* Annals of Mathematics, 77(3):504–537, 1963.
- **[Foundational]** R. S. Hamilton. *Three-manifolds with positive Ricci curvature.* Journal of Differential Geometry, 17(2):255–306, 1982.
- **[Foundational]** M. H. Freedman. *The topology of four-dimensional manifolds.* Journal of Differential Geometry, 17(3):357–453, 1982.
- **[Foundational]** W. P. Thurston. *Three-dimensional manifolds, Kleinian groups and hyperbolic geometry.* Bulletin of the AMS, 6(3):357–381, 1982.
- **[SOTA]** G. Perelman. *The entropy formula for the Ricci flow and its geometric applications.* arXiv:math/0211159, 2002.
- **[SOTA]** G. Perelman. *Ricci flow with surgery on three-manifolds.* arXiv:math/0303109, 2003.
- **[SOTA]** G. Perelman. *Finite extinction time for the solutions to the Ricci flow on certain three-manifolds.* arXiv:math/0307245, 2003.
- **[Verification]** J. Morgan, G. Tian. *Ricci Flow and the Poincaré Conjecture.* Clay Mathematics Monographs, vol. 3, AMS, 2007.
- **[Verification]** B. Kleiner, J. Lott. *Notes on Perelman's papers.* Geometry & Topology, 12(5):2587–2855, 2008.
- **[Verification]** H.-D. Cao, X.-P. Zhu. *A complete proof of the Poincaré and geometrization conjectures.* Asian Journal of Mathematics, 10(2):165–492, 2006.
- **[SPC4]** S. Akbulut. *Cappell–Shaneson homotopy spheres are standard.* Annals of Mathematics, 171(3):2171–2175, 2010.
- **[SPC4]** R. E. Gompf. *More Cappell–Shaneson spheres are standard.* Algebraic & Geometric Topology, 10(3):1665–1681, 2010.
- **[SPC4]** M. Freedman, R. Gompf, S. Morrison, K. Walker. *Man and machine thinking about the smooth 4-dimensional Poincaré conjecture.* Quantum Topology, 1(2):171–208, 2010.
- **[SPC4]** J. Meier, A. Zupan. *Characterizing Dehn surgeries on links via trisections.* PNAS, 115(43):10887–10893, 2018.
- **[Recent]** R. Bamler. *Compactness theory of the space of super Ricci flows.* Inventiones Mathematicae, 233:1121–1277, 2023.
- **[Survey]** J. Milnor. *Towards the Poincaré Conjecture and the classification of 3-manifolds.* Notices of the AMS, 50(10):1226–1233, 2003.
- **[Survey]** R. Kirby (ed.). *Problems in Low-Dimensional Topology.* AMS/IP Studies in Advanced Mathematics, 1997.

## 10. Worked Example / Concrete Special Case

**The Poincaré homology sphere: why homology alone is not enough.**

Let $I^* \subset SU(2) \cong S^3$ be the binary icosahedral group, the preimage of the icosahedral rotation group $A_5$ (order $60$) under the double cover $SU(2) \to SO(3)$. So $|I^*| = 120$. Set
$$\Sigma = S^3 / I^*.$$
Since $I^*$ acts freely (it is a finite subgroup of the group $S^3$ acting by left translation, and left translation by $g \ne e$ has no fixed points), $\Sigma$ is a closed orientable $3$-manifold with $\pi_1(\Sigma) \cong I^*$.

**Homology computation.** $H_1(\Sigma;\mathbb{Z}) = I^*/[I^*,I^*]$. Since $I^*$ is perfect ($[I^*,I^*] = I^*$, because $A_5$ is simple non-abelian and the central extension is perfect), we get
$$H_1(\Sigma;\mathbb{Z}) = 0.$$
By Poincaré duality for a closed orientable $3$-manifold, $H_2(\Sigma) \cong H^1(\Sigma)$, and by universal coefficients $H^1(\Sigma) \cong \mathrm{Hom}(H_1,\mathbb{Z}) \oplus \mathrm{Ext}(H_0,\mathbb{Z}) = 0$. And $H_3(\Sigma) = \mathbb{Z}$, $H_0(\Sigma) = \mathbb{Z}$. So
$$H_*(\Sigma;\mathbb{Z}) \cong H_*(S^3;\mathbb{Z}) = (\mathbb{Z}, 0, 0, \mathbb{Z}).$$

**Conclusion.** $\Sigma$ has the homology of $S^3$ but $\pi_1(\Sigma)$ has order $120 \ne 1$, so $\Sigma \not\cong S^3$. This is exactly Poincaré's 1904 self-correction: it shows the hypothesis in Section 1 must be $\pi_1 = 1$, not $H_1 = 0$.

**Alternate descriptions, all giving $\Sigma$.**
- Brieskorn sphere: $\Sigma(2,3,5) = \{ z_1^2 + z_2^3 + z_3^5 = 0 \} \cap S^5 \subset \mathbb{C}^3$.
- $-1$ surgery on the left-handed trefoil in $S^3$.
- Boundary of the $E_8$-plumbing $4$-manifold; its intersection form is the $E_8$ lattice, even, definite, of rank $8$ and signature $8$.
- Quotient of the dodecahedron with opposite faces glued after a $\pi/5$ twist.

**Ricci flow on $\Sigma$.** The round metric on $S^3$ of radius $1$ descends to $\Sigma$ with $R_{ij} = 2g_{ij}$, so unnormalized Ricci flow gives $g(t) = (1-4t)g_0$: the manifold shrinks homothetically and becomes extinct at $t = 1/4$. This is the model round shrinking case. In Perelman's argument, any simply connected $M$ has finite extinction time (third preprint), and the surgery process shows $M$ is a connected sum of spherical space forms and $S^2\times S^1$'s; simple connectivity forces exactly one $S^3$ summand. If $M$ were $\Sigma$, the flow would still go extinct — but $\pi_1 \ne 1$, so $\Sigma$ is never a counterexample, only a warning that homology is the wrong invariant.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*