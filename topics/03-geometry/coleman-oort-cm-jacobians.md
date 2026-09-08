---
id: 03-geometry/coleman-oort-cm-jacobians
title: "Coleman's Conjecture on Jacobians with Complex Multiplication"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Coleman's Conjecture on Jacobians with Complex Multiplication

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/coleman-oort-cm-jacobians` · **Status:** open

## 1. Problem Statement / Conjecture

Let $g \ge 4$ and let $\mathcal{M}_g$ be the coarse moduli space of smooth projective curves of genus $g$ over $\mathbb{C}$.

**Coleman's Conjecture (1987).** For every $g \ge 4$, the set
$$\mathcal{CM}_g \;=\; \{\, [C] \in \mathcal{M}_g \;:\; \operatorname{Jac}(C) \text{ has complex multiplication} \,\}$$
is finite.

As literally stated this is **false**: counterexamples exist for $4 \le g \le 7$ (Section 4). The live problem is the weakened form used throughout the literature:

**Coleman–Oort Conjecture.** There exists $g_0$ such that for all $g \ge g_0$, $\mathcal{CM}_g$ is finite. The expected value is $g_0 = 8$.

A complete solution requires either (a) a proof of finiteness for all $g$ beyond an explicit bound, or (b) construction of a positive-dimensional family of curves of arbitrarily large genus with dense CM locus. By the André–Oort theorem for $\mathcal{A}_g$ (Tsimerman 2018), (a) is equivalent to: for $g \ge g_0$ there is no positive-dimensional special (Shimura) subvariety $Z \subset \mathcal{A}_g$ meeting the open Torelli locus $\mathcal{T}_g^{\circ}$ and contained in its closure.

## 2. Mathematical Foundations

**CM abelian varieties.** An abelian variety $A/\mathbb{C}$ of dimension $g$ has *complex multiplication* if $\operatorname{End}^0(A) = \operatorname{End}(A)\otimes\mathbb{Q}$ contains a commutative semisimple $\mathbb{Q}$-algebra $E$ with $[E:\mathbb{Q}] = 2g$. Equivalently, the Mumford–Tate group $\mathrm{MT}(H^1(A,\mathbb{Q}))$ is a torus. CM points are exactly the special points of the Shimura variety
$$\mathcal{A}_g = \mathrm{Sp}_{2g}(\mathbb{Z}) \backslash \mathbb{H}_g, \qquad \dim \mathcal{A}_g = \tfrac{g(g+1)}{2}.$$

**Torelli locus.** The Torelli morphism $j : \mathcal{M}_g \to \mathcal{A}_g$, $[C] \mapsto [\operatorname{Jac}(C),\Theta]$, is injective on coarse spaces. Write $\mathcal{T}_g^{\circ} = j(\mathcal{M}_g)$ (open Torelli locus) and $\mathcal{T}_g = \overline{\mathcal{T}_g^{\circ}}$. Then
$$\dim \mathcal{T}_g = 3g-3, \qquad \operatorname{codim}_{\mathcal{A}_g}\mathcal{T}_g = \tfrac{(g-2)(g-3)}{2},$$
which is $0$ for $g \le 3$ and grows quadratically. Heuristically, a "random" subvariety of that codimension should contain few special points — the geometric intuition behind the conjecture.

**Special subvarieties.** $Z \subseteq \mathcal{A}_g$ is *special* if it is an irreducible component of the image of a Shimura subdatum $(G,X) \hookrightarrow (\mathrm{Sp}_{2g},\mathbb{H}_g)$. Special subvarieties contain a dense set of CM points; conversely (André–Oort, proved for $\mathcal{A}_g$) the Zariski closure of any set of CM points is a finite union of special subvarieties. $Z$ is *generically contained* in $\mathcal{T}_g$ if $Z \subseteq \mathcal{T}_g$ and $Z \cap \mathcal{T}_g^{\circ} \ne \emptyset$.

**Cyclic covers of $\mathbb{P}^1$.** The main source of examples. Fix $N \ge 2$ and $a = (a_1,\dots,a_r)$ with $0 < a_i < N$, $\sum a_i \equiv 0 \bmod N$, $\gcd(N,a_1,\dots,a_r) = 1$. For distinct $t_1,\dots,t_r \in \mathbb{P}^1$ set
$$C:\; y^N = \prod_{i=1}^{r}(x - t_i)^{a_i}.$$
The group $\mu_N$ acts, and for a primitive character the eigenspace dimensions of the $\mu_N$-action on $H^0(C,\Omega^1_C)$ are
$$d_n \;=\; \dim H^0(C,\Omega^1_C)^{(n)} \;=\; -1 + \sum_{i=1}^{r}\Big\langle \tfrac{n a_i}{N}\Big\rangle ,$$
with $\langle\cdot\rangle$ the fractional part, and $d_n + d_{N-n} = r-2$ for $n$ with $\gcd(n,N)=1$. The family over the configuration space $M_{0,r}$ has dimension $r-3$; the eigenperiod map lands in a ball quotient $\mathbb{B}^{r-3}/\Gamma$ (Deligne–Mostow). When the generic Mumford–Tate group is small enough, the family is special.

**Higgs/Arakelov criterion.** For a family $f: \mathcal{C} \to B$ over a curve, the logarithmic Higgs bundle $(E^{1,0}\oplus E^{0,1}, \theta)$ satisfies the Arakelov inequality $\deg E^{1,0} \le \frac{g}{2}\deg \Omega^1_{\overline{B}}(\log S)$; equality (a *maximal Higgs field* on a sub-VHS) characterizes Shimura curves (Viehweg–Zuo 2004). This is the main tool for excluding Shimura curves in $\mathcal{T}_g$.

## 3. History & State of the Art (SOTA)

- **1987 — Coleman.** Stated the conjecture in *Torsion points on curves*, motivated by torsion-point questions on curves embedded in their Jacobians.
- **1991 — de Jong–Noot.** Produced families of cyclic covers of $\mathbb{P}^1$ of genus $4$ and $6$ with dense CM locus, disproving the conjecture as stated.
- **1997 — Oort.** Reformulated: finiteness should hold for $g$ large; equivalently no positive-dimensional special subvariety generically inside $\mathcal{T}_g$. This is the modern "Coleman–Oort" statement.
- **1998–2010 — Moonen.** Linearity criteria for special subvarieties in characteristic $0$ and (in char $p$) a criterion via Frobenius-linearity; then a complete classification of special families among cyclic covers of $\mathbb{P}^1$ branched at $4$ points: exactly **20 families**, all with $g \le 7$.
- **2004 — Viehweg–Zuo.** Arakelov-type characterization of Shimura curves in $\mathcal{A}_g$, the engine for all later exclusion results.
- **2013 — Moonen–Oort survey.** The canonical reference; states the expectation $g_0 = 8$.
- **2015–2017 — Frediani–Ghigi–Penegini; Chen–Lu–Zuo; Lu–Zuo.** New examples via Galois coverings (all still $g \le 7$), and the first unconditional exclusion theorems in large genus.
- **2018 — Tsimerman.** André–Oort for $\mathcal{A}_g$, making the "no special subvariety" reformulation an unconditional equivalence.

## 4. Partial Results / Verified Cases

**Counterexamples (conjecture false).** Positive-dimensional special subvarieties generically contained in $\mathcal{T}_g$ are known for $g = 4,5,6,7$. Sources: de Jong–Noot ($g=4,6$); Moonen's list of $20$ cyclic-cover families with $r=4$ branch points, genera $1 \le g \le 7$; Frediani–Ghigi–Penegini's families from non-cyclic Galois covers, again with $g \le 7$; Rohde's families with dense CM locus used to build CY $3$-folds with CM. Grushevsky–Möller give explicit equations for infinitely many Shimura curves in $\mathcal{A}_4$ generically contained in $\mathcal{T}_4$. **No example is known with $g \ge 8$.**

**Positive (exclusion) results.**
- *Cyclic covers of $\mathbb{P}^1$, $r=4$:* Moonen (2010) — the classification is complete, and no family is special for $g \ge 8$.
- *Hyperelliptic locus:* Lu–Zuo (2017) — no Shimura curve is generically contained in the hyperelliptic Torelli locus for $g \ge 8$.
- *Unitary and orthogonal types:* Chen–Lu–Zuo (2016) — no special subvariety of $\mathcal{A}_g$ of these types (with suitable Hodge-type conditions) is generically contained in $\mathcal{T}_g$ once $g$ exceeds an explicit bound (of order a small constant, $g\ge 12$ in the orthogonal case).
- *Totally geodesic subvarieties:* Colombo–Frediani and successors bound the dimension of germs of totally geodesic submanifolds of $\mathcal{T}_g^\circ$ using the second fundamental form of the Torelli map; every special subvariety is totally geodesic, so these bounds are necessary conditions.
- *Characteristic $p$:* Dwork–Ogus-type and Moonen's linearity results restrict Jacobians that are canonical lifts, an $\ell$-adic/crystalline shadow of the conjecture.

## 5. Principal Obstacles

- **No soft argument can work.** The statement is false for $4 \le g \le 7$, so any proof must be sensitive to arithmetic input beyond the codimension count $\frac{(g-2)(g-3)}{2}$, which is already positive at $g=4$.
- **The Torelli locus has no group structure.** $\mathcal{T}_g$ is not a subgroup-orbit; the standard machinery for special subvarieties (Mumford–Tate groups, Hecke correspondences, monodromy) has no direct handle on it. One only knows $\mathcal{T}_g$ through the second fundamental form of $j$, whose kernel is controlled by the Gaussian/Wahl maps of the curve — computable only for special curves.
- **Arakelov equality is hard to contradict in families of dimension $>1$.** Viehweg–Zuo's criterion is a statement about curves in $\mathcal{A}_g$; extending the degeneration/Higgs-bundle argument to higher-dimensional special subvarieties requires controlling boundary behaviour of the Deligne extension over a higher-dimensional base with a normal-crossings boundary, where the numerical inequalities lose their sharpness.
- **Slope and degeneration methods need explicit curves.** Lu–Zuo's exclusion runs through slope inequalities for fibred surfaces, available in the hyperelliptic case and for cyclic covers but not for general families.
- **Classification input is exhausted.** All known examples come from families with large automorphism groups; but a special subvariety need not carry extra automorphisms, and there is no known structural reason forcing this. So classification of Galois covers cannot by itself settle the conjecture.
- **Ineffectivity.** André–Oort for $\mathcal{A}_g$ rests on Galois-orbit lower bounds and o-minimal point counting; the finiteness it yields is non-effective, so even a conditional resolution would not list the CM Jacobians.

## 6. The Gap

Proven: no special subvariety of certain *restricted types* (Shimura curves in the hyperelliptic locus, $g \ge 8$; unitary/orthogonal types under Hodge conditions; families of cyclic covers of $\mathbb{P}^1$ with $4$ branch points) sits generically in $\mathcal{T}_g$ for large $g$. Conjectured: no special subvariety **of any type or dimension** does, for $g \ge 8$.

The exact barrier: current arguments require either (i) an explicit presentation of the family (cyclic/Galois cover, hyperelliptic fibration) to compute Higgs data and slopes, or (ii) a Shimura datum of restricted Hodge type to control the sub-VHS. Neither hypothesis is available for a hypothetical special $Z \subseteq \mathcal{T}_g$ produced abstractly by André–Oort. Crossing the gap means proving an unconditional numerical obstruction — e.g. an upper bound on $\deg E^{1,0}$ for *any* family of curves of genus $g \ge 8$ over a special base — from the geometry of the Torelli map alone.

## 7. Current Research (as of June 2026)

- **Second fundamental form school (Pavia/Milan: Frediani, Colombo, Ghigi, Penegini).** Systematic exclusion of totally geodesic subvarieties in $\mathcal{T}_g$ via the second Gaussian map, extended from Galois covers to families of curves with prescribed ramification. Recent work targets the Prym–Torelli and bielliptic loci by the same method.
- **Higgs-bundle/Arakelov school (Mainz–Shanghai: Lu, Zuo, Chen, collaborators).** Pushing the $g \ge 8$ hyperelliptic exclusion toward the general Shimura-curve case using slope inequalities for fibred surfaces and Fujita decompositions.
- **Unlikely intersections (Pila, Tsimerman, Daw, Orr).** Effective/quantitative André–Oort and Ax–Schanuel for $\mathcal{A}_g$; effective Galois-orbit bounds are now available for CM points, opening the possibility of *effective* finiteness statements once the geometric input is supplied. *(frontier — verify)*
- **Computational searches.** Enumeration of Galois covers with $g \ge 8$ whose eigenperiod data could be special; all searches to date report no candidates. *(frontier — verify)*

## 8. Future Work

1. Prove the Coleman–Oort statement for all Shimura *curves* in $\mathcal{T}_g$, $g$ large — the natural next step after the hyperelliptic case, likely via a genus-independent slope inequality.
2. Establish a general upper bound for the dimension of a totally geodesic submanifold of $\mathcal{T}_g^\circ$ that decays relative to $3g-3$; this alone would imply the conjecture for large $g$.
3. Complete the classification of special families among Galois covers of $\mathbb{P}^1$ with $r \ge 5$ branch points, closing the last structured source of potential counterexamples.
4. Develop a characteristic-$p$ criterion: prove that for $g$ large, no Jacobian in a positive-dimensional family is a canonical lift, in the spirit of Oort's original motivation.
5. Extend the program to Prym varieties and to the Torelli locus in $\mathcal{A}_g$ with non-principal polarizations.

## 9. Key References

- **[Foundational]** R. Coleman. *Torsion points on curves.* In: Galois Representations and Arithmetic Algebraic Geometry, Adv. Stud. Pure Math. 12, North-Holland, 1987, pp. 235–247.
- **[Foundational]** J. de Jong, R. Noot. *Jacobians with complex multiplication.* In: Arithmetic Algebraic Geometry (Texel 1989), Progr. Math. 89, Birkhäuser, 1991, pp. 177–192.
- **[Foundational]** F. Oort. *Canonical liftings and dense sets of CM-points.* In: Arithmetic Geometry (Cortona 1994), Symposia Math. XXXVII, Cambridge Univ. Press, 1997, pp. 228–234.
- **[Foundational]** P. Deligne, G. D. Mostow. *Monodromy of hypergeometric functions and non-lattice integral monodromy.* Publ. Math. IHÉS 63 (1986), 5–89.
- **[Survey]** B. Moonen, F. Oort. *The Torelli locus and special subvarieties.* Handbook of Moduli, Vol. II, Adv. Lect. Math. 25, International Press, 2013, pp. 549–594.
- **[Foundational]** B. Moonen. *Linearity properties of Shimura varieties, I.* J. Algebraic Geom. 7 (1998), 539–567.
- **[SOTA]** B. Moonen. *Special subvarieties arising from families of cyclic covers of the projective line.* Documenta Mathematica 15 (2010), 793–819.
- **[Foundational]** E. Viehweg, K. Zuo. *A characterization of certain Shimura curves in the moduli stack of abelian varieties.* J. Differential Geom. 66 (2004), 233–287.
- **[SOTA]** K. Chen, X. Lu, K. Zuo. *On the Oort conjecture for Shimura varieties of unitary and orthogonal types.* Compositio Mathematica 152 (2016), 889–917.
- **[SOTA]** X. Lu, K. Zuo. *The Oort conjecture on Shimura curves in the Torelli locus of curves.* Journal de Mathématiques Pures et Appliquées 108 (2017), 533–563.
- **[SOTA]** P. Frediani, A. Ghigi, M. Penegini. *Shimura varieties in the Torelli locus via Galois coverings.* Int. Math. Res. Not. IMRN 2015, no. 20, 10595–10623.
- **[SOTA]** J. Tsimerman. *The André–Oort conjecture for $\mathcal{A}_g$.* Annals of Mathematics 187 (2018), 379–390.
- **[Monograph]** J. C. Rohde. *Cyclic Coverings, Calabi–Yau Manifolds and Complex Multiplication.* Lecture Notes in Mathematics 1975, Springer, 2009.
- **[Technique]** E. Colombo, G. P. Pirola, A. Tortora. *Hodge-Gaussian maps.* Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 30 (2001), 125–146.
- **[Technique]** E. Colombo, P. Frediani. *Siegel metric and curvature of the moduli space of curves.* Trans. Amer. Math. Soc. 362 (2010), 1231–1246.
- **[Examples]** S. Grushevsky, M. Möller. *Explicit formulas for infinitely many Shimura curves in genus 4.* Asian Journal of Mathematics 22 (2018), 381–390.

## 10. Worked Example / Concrete Special Case

**A genus-4 counterexample to the literal conjecture.** Take $N = 5$, $r = 4$, branch points $(0,1,t,\infty)$ and local exponents $a = (1,1,1,2)$:
$$C_t : \; y^5 = x(x-1)(x-t), \qquad t \in \mathbb{P}^1\setminus\{0,1,\infty\}.$$
At $\infty$ the exponent is $-(1+1+1) \equiv 2 \bmod 5$, so all four points are totally ramified. Riemann–Hurwitz:
$$2g-2 = 5(-2) + 4\cdot(5-1) = -10 + 16 = 6 \;\Longrightarrow\; g = 4 .$$

Eigenspace dimensions for the $\mu_5$-action, $d_n = -1 + \sum_i \langle n a_i/5\rangle$:

| $n$ | $\sum_i \langle n a_i/5\rangle$ | $d_n$ |
|---|---|---|
| $1$ | $3\cdot\frac15 + \frac25 = 1$ | $0$ |
| $2$ | $3\cdot\frac25 + \frac45 = 2$ | $1$ |
| $3$ | $3\cdot\frac35 + \frac15 = 2$ | $1$ |
| $4$ | $3\cdot\frac45 + \frac35 = 3$ | $2$ |

Total $0+1+1+2 = 4 = g$. ✓ Also $d_1 + d_4 = d_2 + d_3 = 2 = r-2$. ✓

So $H^1(C_t,\mathbb{Q})$ is a module over $\mathbb{Q}(\zeta_5)$ of rank $2$, and the Hodge signatures of the four eigenspaces are $(0,2),(1,1),(1,1),(2,0)$. The generic Mumford–Tate group is contained in the unitary group $\mathrm{U}(1,1)$ attached to the $(1,1)$-eigenspace, whose symmetric domain is the $1$-ball $\mathbb{B}^1 = \mathbb{H}$. The base has dimension $r-3 = 1$, matching $\dim \mathbb{B}^{r-3} = 1$: the eigenperiod map is a local isomorphism onto a $1$-dimensional ball quotient. Hence the family sweeps out a **Shimura curve** $Z \subset \mathcal{A}_4$, generically contained in $\mathcal{T}_4^\circ$ (the covers are non-hyperelliptic of genus $4$ and the map $t \mapsto [C_t]$ is injective up to the finite $\mathfrak{S}$-action).

Consequences:
- $Z$ contains a **dense** set of CM points (special points of a Shimura curve).
- Each such point gives a genus-$4$ curve whose Jacobian has CM by a degree-$8$ field containing $\mathbb{Q}(\zeta_5)$.
- Therefore $\mathcal{CM}_4$ is infinite, and Coleman's conjecture fails at $g=4$.

**Why the same recipe dies for $g \ge 8$.** Keeping $r=4$, the family dimension is fixed at $1$ while $g$ grows like $N$; the number of eigenspaces with signature $\ne (d,0),(0,d)$ grows, so the generic Mumford–Tate group becomes a product of unitary groups whose domain has dimension $\gg 1$. The period map can no longer be dominant onto the associated Shimura variety, and the family fails to be special. Moonen's classification makes this precise: exactly $20$ tuples $(N,a)$ with $r=4$ give special families, and all have $g \le 7$. Producing a counterexample with $g \ge 8$ would need a genuinely different construction — none is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*