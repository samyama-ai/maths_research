---
id: 04-topology/hopf-conjecture-on-curvature
title: "Hopf Conjecture on Curvature"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hopf Conjecture on Curvature

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/hopf-conjecture-on-curvature` · **Status:** open

## 1. Problem Statement / Conjecture

Heinz Hopf posed two linked questions about which closed manifolds carry metrics of positive sectional curvature.

**Hopf Conjecture I (product conjecture).** The manifold $S^2 \times S^2$ admits no Riemannian metric of positive sectional curvature. More generally, no product $M_1 \times M_2$ of closed manifolds of dimension $\ge 2$ admits such a metric.

**Hopf Conjecture II (Euler characteristic conjecture).** If $M^{2n}$ is a closed, even-dimensional Riemannian manifold with positive sectional curvature $\sec > 0$, then its Euler characteristic is positive:
$$\chi(M^{2n}) > 0 .$$
The companion statement for $\sec < 0$ is $(-1)^n \chi(M^{2n}) > 0$ (the Hopf sign conjecture, sometimes attributed to Chern in this form).

Conjecture II implies Conjecture I in the smooth category only partially: $\chi(S^2\times S^2)=4>0$, so II does **not** obstruct $S^2\times S^2$. The two are genuinely independent problems; I is a rigidity question, II a Gauss–Bonnet question. A complete resolution of I requires either an explicit positively curved metric on some product, or a curvature obstruction ruling all of them out. For II, a proof must produce a positive lower bound on $\chi$ from pointwise curvature positivity, or exhibit a positively curved $M^{2n}$ with $\chi \le 0$.

## 2. Mathematical Foundations

Let $(M^n,g)$ be a closed Riemannian manifold with curvature tensor $R$. For a $2$-plane $\sigma = \mathrm{span}(X,Y) \subset T_pM$, the **sectional curvature** is
$$\sec(\sigma) = \frac{\langle R(X,Y)Y, X\rangle}{|X|^2|Y|^2 - \langle X,Y\rangle^2}.$$

**Chern–Gauss–Bonnet.** For $M^{2n}$ closed and oriented, with curvature $2$-form $\Omega$,
$$\chi(M^{2n}) = \frac{1}{(2\pi)^n}\int_M \mathrm{Pf}(\Omega), \qquad
\mathrm{Pf}(\Omega) = \frac{1}{2^n n!}\sum_{\tau \in S_{2n}} \mathrm{sgn}(\tau)\, \Omega_{\tau(1)\tau(2)}\wedge\cdots\wedge\Omega_{\tau(2n-1)\tau(2n)} .$$
In dimension $4$ this reduces to
$$\chi(M^4) = \frac{1}{32\pi^2}\int_M \left(|R|^2 - 4|\mathrm{Ric}|^2 + \mathrm{scal}^2\right) dV .$$

**Algebraic Hopf problem.** Say an algebraic curvature tensor $R$ on $\mathbb{R}^{2n}$ (satisfying the symmetries and the first Bianchi identity) is *positive* if $\sec_R > 0$. The **algebraic Hopf conjecture** asks whether $\sec_R>0$ forces the Pfaffian density $\mathrm{Pf}(R)>0$ pointwise. A positive answer for all $n$ would prove Conjecture II immediately.

**Ambient classical theorems.**
- *Bonnet–Myers:* $\mathrm{Ric}\ge (n-1)k>0 \Rightarrow \mathrm{diam} \le \pi/\sqrt{k}$ and $\pi_1(M)$ finite.
- *Synge:* $M^{2n}$ closed, orientable, $\sec>0 \Rightarrow M$ simply connected.
- *Berger (1965):* on a closed even-dimensional $\sec>0$ manifold every Killing field has a zero; hence for an isometric $S^1$-action the fixed point set is nonempty and $\chi(M)=\chi(M^{S^1})$.
- *Gromov (1981):* $\sec\ge 0 \Rightarrow \sum_i b_i(M;F) \le C(n)$ for any field $F$ — a universal Betti number bound, but with no sign information about $\chi$.
- *Bochner:* $\sec>0$ gives $b_1=0$, but no control on middle Betti numbers.

## 3. History & State of the Art (SOTA)

Hopf raised the questions in the 1930s and returned to them in his 1932 ICM-era work on the topology of positively curved spaces; they were circulated widely by S.-S. Chern, who in *On curvature and characteristic classes of a Riemann manifold* (Abh. Math. Sem. Univ. Hamburg, 1955) attempted the algebraic route. Milestones:

- **1961, Berger.** Classification of simply connected *homogeneous* positively curved manifolds; combined with Wallach (1972) and Bérard-Bergery (1976), the full homogeneous list is known and every even-dimensional entry has $\chi>0$.
- **1965, Berger.** Killing fields on even-dimensional $\sec>0$ manifolds have zeros — the seed of the entire "positive curvature with symmetry" program.
- **1976, Geroch.** *Positive sectional curvature does not imply positive Gauss–Bonnet integrand* (Proc. AMS): the algebraic Hopf conjecture fails in dimension $6$.
- **1976, Klembeck.** Explicit counterexample analysis confirming Geroch's obstruction. Chern's algebraic route is dead for $2n \ge 6$.
- **1989, Hsiang–Kleiner.** A closed, simply connected positively curved $M^4$ with an isometric $S^1$-action is homeomorphic to $S^4$ or $\mathbb{CP}^2$; in particular $b_2\le 1$, so $S^2\times S^2$ admits no positively curved metric with even circle symmetry.
- **1994–2002, Grove–Searle, Püttmann–Searle, Rong–Su.** Symmetry-rank theorems giving $\chi>0$ under large torus actions.
- **2013, Kennard.** $\chi>0$ under a torus action of rank $r \ge 2\log_2 n$ — the first *logarithmic* symmetry requirement.
- **2014, Amann–Kennard.** Rational-ellipticity and Euler-characteristic results for positively curved manifolds with symmetry (GAFA / Adv. Math.).
- **2016, Bettiol.** $S^2\times S^2$ admits metrics with positive *biorthogonal* curvature (the average $\sec(\sigma)+\sec(\sigma^\perp)>0$) — the closest known approach to Conjecture I from the constructive side.

No new closed simply connected positively curved manifold has been found since the Eschenburg (1982) and Bazaikin (1996) spaces; the known list is extremely short, which is itself evidence for both conjectures.

## 4. Partial Results / Verified Cases

- **Dimensions $2$ and $4$ (Conjecture II, unconditional).** $\chi(M^2)>0$ by Gauss–Bonnet. In dimension $4$, Berger showed $\sec>0$ implies the integrand $|R|^2-4|\mathrm{Ric}|^2+\mathrm{scal}^2>0$ pointwise, so $\chi(M^4)>0$. Synge plus Poincaré duality independently give $\chi = 2 + b_2 \ge 2$.
- **Dimension $6$ (Conjecture II, conditional).** Known if $M^6$ admits an isometric $S^1$-action (Berger + fixed-point analysis); the general $6$-dimensional case is open.
- **Symmetry rank bounds.** With $\mathrm{symrank}(M^n)=r$ (rank of a torus acting isometrically): $\chi>0$ if $r \ge n/4$ (Püttmann–Searle 1999, for $n\ge 10$ variants), improved by Rong–Su, and to $r\ge 2\log_2 n$ by Kennard (Geom. Topol. 2013).
- **Nonnegative curvature analogue.** For $\sec \ge 0$, the Cheeger–Gromoll soul theorem and Gromov's Betti bound hold, but $\chi \ge 0$ is *known false* as a strict analogue only in odd dimensions trivially; the even-dimensional nonnegative statement follows from $\sec>0$ results in dim $\le 4$.
- **Conjecture I, verified subclasses.** No positively curved metric on $S^2\times S^2$ exists that is (i) $S^1$-invariant (Hsiang–Kleiner 1989); (ii) Kähler (Berger/Andreotti–Frankel: a positively curved Kähler surface is $\mathbb{CP}^2$); (iii) has positive curvature operator (Böhm–Wilking 2008: such $M$ is a spherical space form); (iv) is $\delta$-pinched with $\delta > 1/4$ (Brendle–Schoen 2009: diffeomorphic to a space form).
- **Positive Ricci/scalar.** $S^2\times S^2$ carries plenty of $\mathrm{Ric}>0$ metrics; the obstruction must be strictly sectional.

## 5. Principal Obstacles

- **The algebraic route is provably blocked.** Geroch's dimension-$6$ counterexample shows $\sec>0 \not\Rightarrow \mathrm{Pf}(R)>0$. Any Gauss–Bonnet proof must be global and integral, not pointwise — but there is no known global mechanism converting integrated curvature positivity into Euler-characteristic sign.
- **Too few examples.** The known simply connected positively curved manifolds are rank-one symmetric spaces plus finitely many families (Wallach, Aloff–Wallach, Eschenburg, Bazaikin). This starves both intuition and any inductive scheme; a counterexample would need a construction technique nobody has.
- **Ricci flow does not preserve $\sec>0$.** In dimensions $\ge 4$, positive sectional curvature is not a Ricci-flow-invariant cone (Böhm–Wilking produced flows leaving $\sec>0$), so the Hamilton–Brendle–Schoen machinery that resolved the $1/4$-pinched sphere theorem does not apply here.
- **Comparison geometry sees only distance.** Toponogov comparison, critical point theory and Alexandrov techniques control the topology at coarse scale; they yield diameter, fundamental group and Betti-number bounds, but the Euler characteristic is a signed alternating sum that these methods never reach.
- **Symmetry is an added hypothesis, not a consequence.** Every strong result assumes a torus action; there is no theorem forcing a positively curved metric to have any symmetry, and generic metrics have trivial isometry group.
- **Deformation obstruction for $S^2\times S^2$.** The product metric has zero-curvature planes on a full $2$-parameter family at every point (mixed planes). Bourguignon–Deschamps–Karcher showed the product metric is a rigid critical configuration: no second-order deformation removes the flat planes.

## 6. The Gap

For Conjecture II the gap is dimension-theoretic and mechanistic: proven unconditionally in $2n \le 4$, and in higher even dimensions only under a torus action of rank $\gtrsim \log_2 n$. The missing step is a *symmetry-free* argument. Concretely, one needs either
1. a global integral inequality $\int_M \mathrm{Pf}(R)\,dV > 0$ valid whenever $\sec>0$, despite the pointwise integrand changing sign (Geroch); or
2. a topological consequence of $\sec>0$ — e.g. rational ellipticity (Bott–Grove–Halperin conjecture) — strong enough to force $\chi>0$ via the known fact that a rationally elliptic even-dimensional space has $\chi \ge 0$, with $\chi>0$ iff its rational homotopy is concentrated in even degrees.

For Conjecture I the gap is the passage from "no $S^1$-invariant positively curved metric on $S^2\times S^2$" to "no metric at all". Every existing 4-dimensional proof consumes the fixed-point structure of an isometric circle action; without symmetry there is no known invariant separating $S^2\times S^2$ ($b_2=2$, $\chi=4$) from $\mathbb{CP}^2$ ($b_2=1$, $\chi=3$) using sectional curvature alone. Bettiol's positive-biorthogonal metrics show the gap is thin: the intermediate curvature condition is achievable, so the obstruction lives precisely at the level of individual mixed $2$-planes.

## 7. Current Research (as of June 2026)

- **Positive curvature with symmetry (Kennard, Wilking, Grove schools).** Ongoing effort to push the torus-rank threshold in Kennard's theorem below $2\log_2 n$, and to replace torus actions by weaker hypotheses such as a single non-trivial Killing field with controlled zero set. Groups at Notre Dame (Kennard), Münster (Wilking, Nienhaus) and Penn (Ziller). *(frontier — verify)*
- **Rational ellipticity route.** Amann–Kennard's programme deducing bounds on rational homotopy from positive curvature plus symmetry, aimed at the Bott–Grove–Halperin conjecture as an intermediate target implying $\chi\ge 0$.
- **Intermediate curvature conditions.** Bettiol-style constructions on $S^2\times S^2$ (positive biorthogonal, positive $k$-th intermediate Ricci $\mathrm{Ric}_k$) mapping out exactly how much positivity a product tolerates. Recent work on $\mathrm{Ric}_2 > 0$ for products is active. *(frontier — verify)*
- **New-example hunting.** Search for positively curved cohomogeneity-one and biquotient metrics; the long-disputed Petersen–Wilhelm claim of positive curvature on the Gromoll–Meyer sphere remains unconfirmed in the literature. *(frontier — verify)*
- **Curvature-operator flows.** Extending Böhm–Wilking cone techniques to invariant conditions strictly weaker than positive curvature operator but stronger than $\sec>0$.

## 8. Future Work

- Determine the algebraic Hopf conjecture's exact failure set: characterize the algebraic curvature tensors with $\sec>0$ and $\mathrm{Pf}\le 0$ in each dimension, and test whether such tensors can be realized as the curvature of an actual metric on a closed manifold at a full-measure set of points.
- Prove the Bott–Grove–Halperin conjecture (nonnegatively curved simply connected closed manifolds are rationally elliptic) in dimension $6$; Grove has repeatedly identified this as the most plausible bridge to Hopf II.
- Remove symmetry: find any topological invariant of $\sec>0$ manifolds, beyond $\pi_1$ and Betti bounds, that is sensitive to the sign of $\chi$.
- For $S^2\times S^2$: classify all metrics of positive biorthogonal curvature and study the boundary of the space of such metrics inside the space of all metrics, testing whether $\sec>0$ is a closed empty face.
- Systematic computer search over invariant metrics on cohomogeneity-two $T^2$-manifolds with $b_2 = 2$.

## 9. Key References

- **[Foundational]** S.-S. Chern. *On curvature and characteristic classes of a Riemann manifold.* Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg, 20:117–126, 1955.
- **[Foundational]** M. Berger. *Les variétés riemanniennes homogènes normales simplement connexes à courbure strictement positive.* Annali della Scuola Normale Superiore di Pisa, 15:179–246, 1961.
- **[Foundational]** M. Berger. *Trois remarques sur les variétés riemanniennes à courbure positive.* C. R. Acad. Sci. Paris, 263:76–78, 1966.
- **[Foundational]** R. Geroch. *Positive sectional curvatures does not imply positive Gauss–Bonnet integrand.* Proceedings of the American Mathematical Society, 54:267–270, 1976.
- **[Foundational]** P. Klembeck. *On Geroch's counterexample to the algebraic Hopf conjecture.* Proceedings of the American Mathematical Society, 59:334–336, 1976.
- **[Foundational]** M. Gromov. *Curvature, diameter and Betti numbers.* Commentarii Mathematici Helvetici, 56:179–195, 1981.
- **[Key result]** W.-Y. Hsiang and B. Kleiner. *On the topology of positively curved 4-manifolds with symmetry.* Journal of Differential Geometry, 29(3):615–621, 1989.
- **[Key result]** T. Püttmann and C. Searle. *The Hopf conjecture for manifolds with low cohomogeneity or high symmetry rank.* Proceedings of the American Mathematical Society, 130:163–166, 2002.
- **[Key result]** X. Rong and X. Su. *The Hopf conjecture for manifolds with abelian group actions.* Communications in Contemporary Mathematics, 7(1):121–136, 2005.
- **[SOTA / Recent]** L. Kennard. *On the Hopf conjecture with symmetry.* Geometry & Topology, 17:563–593, 2013.
- **[SOTA / Recent]** M. Amann and L. Kennard. *Topological properties of positively curved manifolds with symmetry.* Geometric and Functional Analysis, 24:1377–1405, 2014.
- **[SOTA / Recent]** C. Böhm and B. Wilking. *Manifolds with positive curvature operators are space forms.* Annals of Mathematics, 167:1079–1097, 2008.
- **[SOTA / Recent]** R. G. Bettiol. *Positive biorthogonal curvature on $S^2\times S^2$.* Proceedings of the American Mathematical Society, 142:4341–4353, 2014.
- **[Survey]** K. Grove. *Developments around positive sectional curvature.* Surveys in Differential Geometry, Vol. 13, International Press, 2009.
- **[Survey]** B. Wilking. *Nonnegatively and positively curved manifolds.* Surveys in Differential Geometry, Vol. 11, International Press, 2007.
- **[Survey]** W. Ziller. *Examples of Riemannian manifolds with non-negative sectional curvature.* Surveys in Differential Geometry, Vol. 11, International Press, 2007.

## 10. Worked Example / Concrete Special Case

**Chern–Gauss–Bonnet on the product metric of $S^2\times S^2$.**

Take $M = S^2(1)\times S^2(1)$ with the product metric. Choose an orthonormal frame $e_1,e_2$ tangent to the first factor and $e_3,e_4$ to the second at a point $p$.

*Sectional curvatures.* $\sec(e_1,e_2) = \sec(e_3,e_4) = 1$; every mixed plane $\sec(e_i,e_j)=0$ for $i\in\{1,2\}, j\in\{3,4\}$. So $\sec \ge 0$ but a $4$-dimensional family of flat planes exists at every point — this is exactly what Hopf I asks to be unremovable.

*Curvature invariants.* The only nonzero components are $R_{1212}=R_{3434}=1$ together with their symmetry images $R_{1221}=R_{2112}=-1$, $R_{2121}=1$ (and likewise for indices $3,4$). Hence
$$|R|^2 = \sum_{i,j,k,l} R_{ijkl}^2 = 4 + 4 = 8 .$$
Each factor is Einstein with $\mathrm{Ric}=g$, so on the product $\mathrm{Ric}=g$, giving
$$|\mathrm{Ric}|^2 = 4, \qquad \mathrm{scal} = 4 .$$

*Integrand.*
$$|R|^2 - 4|\mathrm{Ric}|^2 + \mathrm{scal}^2 = 8 - 16 + 16 = 8 .$$

*Volume.* $\mathrm{Vol}(S^2(1)) = 4\pi$, so $\mathrm{Vol}(M)=16\pi^2$.

*Euler characteristic.*
$$\chi(M) = \frac{1}{32\pi^2}\int_M 8\, dV = \frac{8 \cdot 16\pi^2}{32\pi^2} = 4 ,$$
matching $\chi(S^2\times S^2) = 2\times 2 = 4$.

**What this shows.** The Gauss–Bonnet integrand is strictly positive ($=8$) even though the metric is *not* positively curved. So integrand positivity is strictly weaker than $\sec>0$ and carries no information about Hopf I. Conversely, Geroch's dimension-$6$ example runs the other way: $\sec>0$ with $\mathrm{Pf}\le 0$. The two failures together explain why the Chern programme cannot decide either conjecture, and why $S^2\times S^2$ — with $\chi=4>0$, so unobstructed by Hopf II — must be attacked by a mechanism that detects the mixed flat planes themselves. Bettiol's theorem sharpens the point: averaging $\sec(\sigma)+\sec(\sigma^\perp)$ over the flat mixed planes *can* be made positive, so the obstruction, if it exists, is not an averaged one.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*