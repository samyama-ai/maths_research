---
id: 04-topology/property-p-conjecture
title: "Property P Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Property P Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/property-p-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $K \subset S^3$ be a knot and let $S^3_{p/q}(K)$ denote the closed oriented $3$-manifold obtained by Dehn surgery on $K$ with slope $p/q \in \mathbb{Q} \cup \{1/0\}$.

**Property P Conjecture.** If $K$ is a nontrivial knot, then for every slope $p/q \neq 1/0$ (i.e. every nontrivial surgery),
$$\pi_1\big(S^3_{p/q}(K)\big) \neq 1 .$$

A knot with this property is said to *have Property P*. The conjecture asserts that every nontrivial knot has Property P; equivalently, no nontrivial Dehn surgery on a nontrivial knot produces a homotopy $3$-sphere. Historically this was strictly stronger than "no surgery yields $S^3$", because before Perelman a simply connected closed $3$-manifold was not known to be $S^3$.

**Status.** Proved. Kronheimer and Mrowka established Property P for all nontrivial knots in 2004. A complete proof required (i) reduction to the slopes $\pm 1$, and (ii) production of a nontrivial (indeed irreducible $SU(2)$) representation of $\pi_1(S^3_{\pm 1}(K))$. The page is retained because the natural strengthenings — which slopes admit irreducible $SU(2)$ representations, and the generalized Property R conjecture for links — remain open.

## 2. Mathematical Foundations

**Dehn surgery.** Let $N(K)$ be a tubular neighbourhood of $K$, $E_K = S^3 \setminus \operatorname{int} N(K)$ the exterior, with $\partial E_K$ a torus carrying the standard basis $(\mu,\lambda)$: $\mu$ the meridian, $\lambda$ the Seifert-framed longitude, so $[\mu] $ generates $H_1(E_K) \cong \mathbb{Z}$ and $[\lambda] = 0$. For coprime $p,q$,
$$S^3_{p/q}(K) \;=\; E_K \cup_{\varphi} (S^1 \times D^2), \qquad \varphi(\{*\}\times \partial D^2) \simeq p\mu + q\lambda .$$
Then $H_1(S^3_{p/q}(K)) \cong \mathbb{Z}/p\mathbb{Z}$, so $p = \pm 1$ is necessary for a homotopy sphere, and by van Kampen
$$\pi_1\big(S^3_{p/q}(K)\big) \;\cong\; \pi_1(E_K)\big/\langle\langle\, \mu^{p}\lambda^{q} \,\rangle\rangle .$$
Property P is therefore the statement: for nontrivial $K$ and all $q\neq 0$ or $p\neq\pm 1$ excluded appropriately, the normal closure of $\mu^p\lambda^q$ is a proper subgroup of the knot group.

**Casson invariant.** For an integral homology sphere $Y$, Casson's invariant $\lambda(Y) \in \mathbb{Z}$ counts (algebraically, after perturbation) conjugacy classes of irreducible representations $\pi_1(Y) \to SU(2)$. Its surgery formula is
$$\lambda\big(S^3_{1/n}(K)\big) \;=\; \tfrac{n}{2}\,\Delta_K''(1) \;=\; n\, a_2(K),$$
with $\Delta_K$ the symmetrized Alexander polynomial normalized by $\Delta_K(1)=1$ and $a_2$ the second Conway coefficient. Hence $\lambda \neq 0 \Rightarrow$ an irreducible $SU(2)$ representation exists $\Rightarrow \pi_1 \neq 1$.

**Taut foliations and instanton Floer homology.** A codimension-one foliation $\mathcal{F}$ of a closed oriented $3$-manifold $Y$ is *taut* if some closed transversal meets every leaf. Gabai's theorem provides a taut foliation on $S^3_0(K)$ for nontrivial $K$; Eliashberg–Thurston perturb it to a weakly symplectically semi-fillable contact structure. Kronheimer–Mrowka's route then runs
$$\text{taut foliation on } S^3_0(K) \;\Longrightarrow\; \mathrm{HM}_*\!\left(S^3_0(K)\right)_{\text{nontrivial}} \;\Longrightarrow\; I_*\!\left(S^3_0(K)\right)\neq 0 \;\xrightarrow{\ \text{surgery triangle}\ }\; R^{\mathrm{irr}}\big(\pi_1(S^3_{\pm1}(K)), SU(2)\big) \neq \varnothing,$$
where $I_*$ is instanton Floer homology and the last arrow uses the Floer exact triangle
$$\cdots \to I_*(S^3_0(K)) \to I_*(S^3_{-1}(K)) \to I_*(S^3) \to \cdots$$
in the appropriate (admissible / sutured) setting.

## 3. History & State of the Art (SOTA)

- **1970s.** The name is due to R. H. Bing and J. M. Martin, *Cubes with knotted holes* (Trans. AMS, 1971), who verified Property P for large classes of knots and framed it as an approach to the Poincaré conjecture: a counterexample would produce a homotopy sphere from surgery.
- **1987.** Culler–Gordon–Luecke–Shalen's Cyclic Surgery Theorem (Annals of Math.) forced any cyclic-$\pi_1$ surgery on a nontrivial knot to be integral, and any two such slopes to differ by at most $1$. Combined with $|p|=1$, this reduced the whole conjecture to the two slopes $\pm 1$.
- **1987.** Gabai proved Property R (only $0$-surgery on a knot gives $S^1\times S^2$) with sutured manifold hierarchies, supplying the taut foliation on $S^3_0(K)$ used later.
- **1989.** Gordon–Luecke proved knots are determined by their complements, so no nontrivial surgery gives $S^3$ *on the nose* — but a fake homotopy sphere was still not excluded a priori.
- **2004.** Kronheimer–Mrowka, *Witten's conjecture and Property P* (Geometry & Topology 8, 295–310), completed the proof: $\pi_1(S^3_{\pm1}(K))$ admits an irreducible $SU(2)$ representation for every nontrivial $K$. The argument used Gabai + Eliashberg–Thurston + Feehan–Leness's partial verification of Witten's conjecture relating Donaldson and Seiberg–Witten invariants.
- **2010.** Kronheimer–Mrowka, *Knots, sutures, and excision*, gave a self-contained instanton proof (via sutured instanton homology and the unknot-detection theorem for knot instanton homology) not relying on the Witten conjecture input.

## 4. Partial Results / Verified Cases

Cases settled before 2004, all still instructive:

- **Casson-invariant class.** Every knot with $a_2(K) = \tfrac12\Delta_K''(1) \neq 0$ has Property P for slopes $1/n$: e.g. trefoil ($a_2 = 1$), figure-eight ($a_2 = -1$), all twist knots.
- **Satellite knots.** Gordon (1983) and Gabai: surgery on a satellite with nontrivial companion yields a manifold with incompressible torus or nontrivial JSJ piece; $\pi_1$ is never trivial.
- **Torus knots $T_{p,q}$.** All surgeries are Seifert fibered or reducible with computable $\pi_1$; $S^3_{pq\pm1}(T_{p,q})$ are lens spaces, and $\pm1$-surgeries give Brieskorn spheres $\Sigma(p,q,pq\mp1)$ with infinite or finite non-trivial $\pi_1$.
- **Alternating knots** and, more generally, knots admitting persistent taut foliations: Delman–Roberts (Comment. Math. Helv. 74, 1999) proved *Strong* Property P — every nontrivial surgery yields a manifold with infinite, non-cyclic $\pi_1$ — for all non-torus alternating knots.
- **Symmetric knots, strongly invertible knots, knots of bridge number $\le 3$, and knots whose complements contain closed essential surfaces:** handled by CGLS-type character-variety arguments.
- **Slope reduction.** By CGLS + Gordon–Luecke, only $p/q = \pm 1$ were ever in doubt, for *every* knot.

## 5. Principal Obstacles

The historical obstacles explain why the problem stood for three decades and why its strengthenings resist:

- **Purely 3-dimensional methods stop at $\pm 1$.** Sutured-hierarchy and character-variety arguments (Gabai, CGLS) control slopes of large $|q|$ or large distance $\Delta(r,r')$. Surgery coefficients $\pm 1$ are distance $1$ from the meridian, exactly the case with no room in the Culler–Shalen norm.
- **Taut foliations degenerate under $\pm1$ surgery.** Gabai's foliation lives on $S^3_0(K)$ and need not survive filling along $\pm 1$; a direct foliation-theoretic proof for $\pm1$ never materialized.
- **Homology-sphere invariants vanish.** Casson's invariant is zero exactly when $\Delta_K''(1)=0$ (e.g. the untwisted Whitehead double of any knot), and Heegaard Floer / monopole Floer homology of an integer homology sphere gives no lower bound on $|R^{\mathrm{irr}}|$ by itself. So the abelian and "counted" invariants are blind on an infinite family.
- **Nonabelian gauge theory was needed.** Only instanton Floer homology sees $SU(2)$ representations directly; but its nonvanishing for $S^3_0(K)$ required both the symplectic-filling technology (Eliashberg–Thurston) and a Donaldson–Seiberg–Witten comparison (Feehan–Leness) whose full form (Witten's conjecture) was itself unproven at the time.
- **Group theory alone is insufficient.** Deciding triviality of $\pi_1(E_K)/\langle\langle \mu\lambda\rangle\rangle$ from a presentation is undecidable in general; no algorithmic or combinatorial route exists.

## 6. The Gap

For Property P itself the gap is closed. What remains open is the quantitative strengthening:

- **$SU(2)$ slopes.** Kronheimer–Mrowka (*Dehn surgery, the fundamental group and $SU(2)$*, Math. Res. Lett. 11, 2004) proved: for nontrivial $K$ and $|r| \le 2$, $\pi_1(S^3_r(K))$ has an irreducible $SU(2)$ representation. For $|r| > 2$ this is unknown in general — the conjecture that $S^3_r(K)$ is *$SU(2)$-abelian* only for lens-space-like $r$ is open.
- **Strong Property P.** Whether every nontrivial surgery on every nontrivial non-torus knot has infinite non-cyclic $\pi_1$ is proved only for restricted families (alternating, most Montesinos).
- **Generalized Property R** (Kirby Problem 1.82): if surgery on an $n$-component link $L$ with framing $0$ yields $\\#^n(S^1\times S^2)$, is $L$ handle-slide equivalent to the $n$-component unlink? Open for $n \ge 2$; equivalent formulations connect to the smooth $4$-dimensional Poincaré conjecture.

## 7. Current Research (as of June 2026)

- **Instanton-theoretic $SU(2)$ representation counts.** Baldwin–Sivek and Sivek–Zentner develop framed/sutured instanton homology to classify $SU(2)$-cyclic and $SU(2)$-abelian surgeries; Sivek–Zentner's pillowcase-holonomy method (J. Differential Geom., 2021) constrains the set of $SU(2)$-cyclic slopes of a knot to at most two rationals in many cases. *(frontier — verify: extensions to all hyperbolic knots.)*
- **$SL(2,\mathbb{C})$ analogues.** Zentner (J. LMS, 2017) proved every integer homology $3$-sphere other than $S^3$ has an irreducible $SL(2,\mathbb{C})$ representation of $\pi_1$; the $SU(2)$ version for all homology spheres is open.
- **Generalized Property R.** Gompf–Scharlemann–Thompson and later Manolescu–Piccirillo test candidate counterexamples arising from $R$-links; several proposed exotic $4$-spheres have been eliminated. *(frontier — verify.)*
- **Groups.** Kronheimer–Mrowka (MIT/Cambridge), Baldwin (Boston College), Sivek (Imperial), Zentner (Regensburg), Hedden, Hom, Manolescu, and the Warwick/Regensburg low-dimensional topology programmes.

## 8. Future Work

- Determine the full set of $SU(2)$-abelian slopes for hyperbolic knots; conjecturally $|r| \geq 2g(K)-1$ is the only regime where they can occur.
- Prove Strong Property P for all non-torus knots — likely by extending Roberts' persistent-lamination constructions to all knots with essential branched surfaces in the complement.
- Find a foliation- or Heegaard-Floer-only proof of Property P, avoiding instantons; this would likely give effective bounds on the size of the representation variety.
- Settle generalized Property R for $2$-component links, the first genuinely open case, and connect it to the smooth $4$-dimensional Poincaré conjecture.

## 9. Key References

- **[Foundational]** R. H. Bing and J. M. Martin. *Cubes with knotted holes.* Transactions of the American Mathematical Society 155 (1971), 217–231.
- **[Foundational]** M. Culler, C. McA. Gordon, J. Luecke, P. B. Shalen. *Dehn surgery on knots.* Annals of Mathematics 125 (1987), 237–300.
- **[Foundational]** D. Gabai. *Foliations and the topology of 3-manifolds. III.* Journal of Differential Geometry 26 (1987), 479–536.
- **[Foundational]** C. McA. Gordon and J. Luecke. *Knots are determined by their complements.* Journal of the American Mathematical Society 2 (1989), 371–415.
- **[SOTA]** P. B. Kronheimer and T. S. Mrowka. *Witten's conjecture and Property P.* Geometry & Topology 8 (2004), 295–310.
- **[SOTA]** P. B. Kronheimer and T. S. Mrowka. *Dehn surgery, the fundamental group and $SU(2)$.* Mathematical Research Letters 11 (2004), 741–754.
- **[SOTA]** P. B. Kronheimer and T. S. Mrowka. *Knots, sutures, and excision.* Journal of Differential Geometry 84 (2010), 301–364.
- **[Recent]** S. Sivek and R. Zentner. *$SU(2)$-cyclic surgeries and the pillowcase.* Journal of Differential Geometry 119 (2021), 335–405.
- **[Recent]** R. Zentner. *Integer homology 3-spheres admit irreducible representations in $SL(2,\mathbb{C})$.* Journal of the London Mathematical Society 96 (2017), 227–242.
- **[Recent]** C. Delman and R. Roberts. *Alternating knots satisfy Strong Property P.* Commentarii Mathematici Helvetici 74 (1999), 376–397.
- **[Survey]** S. Boyer. *Dehn surgery on knots.* In *Handbook of Geometric Topology*, Elsevier, 2002, 165–218.
- **[Survey]** R. Kirby (ed.). *Problems in low-dimensional topology.* In *Geometric Topology* (AMS/IP Studies in Advanced Mathematics 2.2), 1997.
- **[Background]** Y. Eliashberg and W. Thurston. *Confoliations.* University Lecture Series 13, AMS, 1998.
- **[Background]** S. Akbulut and J. McCarthy. *Casson's Invariant for Oriented Homology 3-Spheres: An Exposition.* Mathematical Notes 36, Princeton University Press, 1990.

## 10. Worked Example / Concrete Special Case

**Property P for the figure-eight knot $4_1$ via the Casson invariant.**

Its symmetrized Alexander polynomial is
$$\Delta_{4_1}(t) = -t + 3 - t^{-1}, \qquad \Delta_{4_1}(1) = 1 .$$
Differentiating twice and evaluating at $t=1$:
$$\Delta_{4_1}'(t) = -1 + t^{-2}, \qquad \Delta_{4_1}''(t) = -2t^{-3}, \qquad \Delta_{4_1}''(1) = -2 .$$
Equivalently $a_2(4_1) = -1$ in the Conway normalization $\nabla(z) = 1 - z^2$.

By CGLS plus $H_1(S^3_{p/q}) = \mathbb{Z}/p$, the only slopes that could give a homotopy sphere are $1/n$. Casson's surgery formula gives
$$\lambda\big(S^3_{1/n}(4_1)\big) = \tfrac{n}{2}\Delta_{4_1}''(1) = -n \neq 0 \quad (n\neq 0).$$
Since $\lambda$ is the signed count of irreducible $SU(2)$ representations, $\lambda \neq 0$ forces at least one irreducible $\rho : \pi_1(S^3_{1/n}(4_1)) \to SU(2)$. An irreducible representation has nonabelian image, so
$$\pi_1\big(S^3_{1/n}(4_1)\big) \neq 1 .$$

**Check against the geometry.** For $n=1$, $S^3_{-1}(4_1) \cong \Sigma(2,3,7)$, the Brieskorn sphere, whose $\pi_1$ is the infinite triangle-group-related central extension $\langle x,y,z \mid x^2=y^3=z^7=xyz\rangle$-type group; $\lambda(\Sigma(2,3,7)) = -1$, matching the formula, and $\Sigma(2,3,7)$ is hyperbolic-free but has $\widetilde{PSL_2\mathbb{R}}$ geometry with infinite $\pi_1$.

**Where this argument dies.** Take $K = D_+(U)$, the untwisted positive-clasped Whitehead double of the unknot's companion pattern applied to a nontrivial knot — more simply, any knot with $\Delta_K(t) = 1$, e.g. untwisted Whitehead doubles. Then $a_2(K) = 0$ and $\lambda(S^3_{\pm1}(K)) = 0$: the Casson count is empty, and no obstruction is produced. It is exactly this infinite family that required the instanton-theoretic argument of Kronheimer–Mrowka, where nonvanishing of $I_*(S^3_0(K))$ — supplied by Gabai's taut foliation on $S^3_0(K)$, which exists because $K$ is nontrivial — is fed through the surgery exact triangle to force an irreducible $SU(2)$ representation on $S^3_{\pm 1}(K)$ regardless of the Alexander polynomial.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*