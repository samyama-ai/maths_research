---
id: 04-topology/combinatorial-definition-of-rasmussen-s-invariant
title: "Combinatorial Definition of Rasmussen s-invariant"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Combinatorial Definition of Rasmussen s-invariant

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/combinatorial-definition-of-rasmussen-s-invariant` · **Status:** open

## 1. Problem Statement / Conjecture

Rasmussen's invariant $s: \{\text{knots in } S^3\} \to 2\mathbb{Z}$ is defined through the filtered Lee deformation of Khovanov homology. Its construction is finite and algorithmic, but not *local*: it requires building a chain complex of rank $2^{c}$ on a diagram with $c$ crossings and reading off a filtration level from its homology, and its central property — the slice-genus bound — is proved by invoking functoriality of Khovanov homology under link cobordisms in $\mathbb{R}^4$.

**Problem.** Give a combinatorial definition of $s(K)$ — a state sum, skein-type recursion, or diagrammatic normal-form formula computed from a knot diagram $D$ by local moves — such that:

1. **(Invariance)** the formula is manifestly unchanged under the three Reidemeister moves, without recourse to homological algebra over the cube of resolutions;
2. **(Genus bound)** the inequality $|s(K)| \le 2g_4(K)$ follows from the formula directly, without using the Khovanov cobordism functor of Jacobsson and Bar-Natan;
3. **(Efficiency)** the formula is computable in time subexponential in the crossing number $c(D)$, ideally polynomial.

A complete solution supplies such a formula together with a proof that it agrees with Rasmussen's $s$. A disproof of the strongest form would be a hardness result, e.g. showing that computing $s$ is $\mathsf{NP}$-hard or $\\#\mathsf{P}$-hard, ruling out (3). Partial credit: achieving (1)–(2) for the $\mathfrak{sl}_N$ family $s_N$ of Lobb and Wu, or an analogue of the Manolescu–Ozsváth–Sarkar grid description of $\tau$.

## 2. Mathematical Foundations

Let $D$ be an oriented diagram of a knot $K$ with $c$ crossings, $n_+$ positive and $n_-$ negative. Khovanov's construction assigns to each of the $2^c$ vertices $v\in\{0,1\}^c$ of the cube of resolutions a collection of $|v|$ disjoint circles and the vector space $A^{\otimes |v|}$, where
$$A=\mathbb{Q}[X]/(X^2),\qquad \deg 1 = 1,\ \deg X = -1 .$$
$A$ is a Frobenius algebra with comultiplication $\Delta(1)=1\otimes X + X\otimes 1$, $\Delta(X)=X\otimes X$, and counit $\epsilon(X)=1$, $\epsilon(1)=0$. Merges and splits of circles give $m$ and $\Delta$; summing edge maps with signs yields $(C(D),d)$, bigraded by homological degree $i$ and quantum degree $q$, with homology $\mathrm{Kh}(K)$.

**Lee deformation.** Lee replaces $A$ by $A' = \mathbb{Q}[X]/(X^2-1)$, keeping the same formulas. The differential $d_{\mathrm{Lee}} = d + \Phi$ is no longer $q$-homogeneous; it raises $q$ by $0$ and $4$, so $q$ becomes a *filtration* rather than a grading. Lee's theorem:
$$\dim_{\mathbb{Q}} \mathrm{Kh}_{\mathrm{Lee}}(L) = 2^{|L|}$$
for a link $L$ with $|L|$ components, with a basis indexed by orientations of $L$. For a knot, $\mathrm{Kh}_{\mathrm{Lee}}(K)\cong\mathbb{Q}^2$, concentrated in homological degree $0$, spanned by $\mathfrak{s}_o,\mathfrak{s}_{\bar o}$ (the two orientations), obtained from the oriented resolution by the idempotents $a = X+1$, $b = X-1$.

**Definition of $s$.** For $x\ne 0$ in the filtered space $\mathrm{Kh}_{\mathrm{Lee}}(K)$ set $\mathfrak{s}(x)=\max\{q : x \in \mathcal{F}^q\}$, and
$$s_{\min}(K)=\min_{x\neq 0}\mathfrak{s}(x),\qquad s_{\max}(K)=\max_{x\neq 0}\mathfrak{s}(x).$$
Rasmussen proves $s_{\max}=s_{\min}+2$ and defines
$$s(K) := s_{\min}(K)+1 = s_{\max}(K)-1 \in 2\mathbb{Z}.$$

**Main properties (Rasmussen 2010).** $s$ is a concordance homomorphism, $s(K_1 \\# K_2)=s(K_1)+s(K_2)$, $s(\bar K)=-s(K)$ for the mirror, $s(\text{unknot})=0$, and
$$|s(K)| \le 2g_4(K) \le 2g_3(K).$$
The genus bound comes from: a connected cobordism $\Sigma\subset \mathbb{R}^3\times[0,1]$ of genus $g$ induces a filtered map shifting $q$ by $\chi(\Sigma)$, and the induced map on Lee homology is nonzero (Rasmussen; Jacobsson's cobordism functor, invariance up to sign by Bar-Natan and Beliakova–Wehrli). Combined with $s(T_{p,q}) = (p-1)(q-1)$ this gives a proof of the Milnor conjecture using no gauge theory — but *not* using only local combinatorics.

## 3. History & State of the Art (SOTA)

- **1993.** Kronheimer–Mrowka prove the Milnor conjecture $g_4(T_{p,q})=\tfrac{(p-1)(q-1)}{2}$ with instanton gauge theory.
- **2000.** Khovanov categorifies the Jones polynomial.
- **2005.** Lee's endomorphism collapses $\mathrm{Kh}$ to $\mathbb{Q}^{2^{|L|}}$ and proves $\mathrm{Kh}$ is thin for alternating links.
- **2004/2010.** Rasmussen defines $s$ (arXiv 2004; *Invent. Math.* 2010) and gives the first combinatorial-flavoured proof of the Milnor conjecture. This is the origin of the present problem: Rasmussen's proof is "combinatorial modulo functoriality", and finding a genuinely local definition was immediately posed.
- **2007–2009.** Shumakovitch relates $s$ to the Bockstein/reduced $\mathbb{F}_2$ theory; Lobb and Wu independently define $\mathfrak{sl}_N$ analogues $s_N$ with $s_2=s$.
- **2008.** Hedden–Ording show $s \ne 2\tau$, so no route through the (combinatorially described) knot Floer $\tau$ can define $s$.
- **2010.** Freedman–Gompf–Morrison–Walker attempt to disprove the smooth 4D Poincaré conjecture by computing $s$ of large diagrams; the computations top out around 60 crossings, making efficiency a concrete obstacle.
- **2020.** Piccirillo uses $s$ to prove the Conway knot is not slice — a headline application resting on a $\sim$100-crossing $s$ computation via Schütz's and Bar-Natan's software.
- **2020–2024.** Schütz gives divide-and-conquer algorithms over $\mathbb{F}_2$ and $\mathbb{Q}$; Manolescu–Marengon–Sarkar–Willis generalize $s$ to surfaces in negative-definite 4-manifolds; Ren–Willis compute skein lasagna modules distinguishing exotic 4-manifolds *(frontier — verify)*.

## 4. Partial Results / Verified Cases

Closed-form, genuinely combinatorial formulas for $s$ are known on:

- **Alternating knots** (Lee 2005; Rasmussen 2010): $\mathrm{Kh}$ is thin and $s(K)=-\sigma(K)$, the signature — computable in $O(c^3)$ from the Goeritz/Seifert matrix.
- **Positive and quasipositive knots** (Rasmussen; Livingston 2004): $s(K)=2g_4(K)=2g_3(K)$. For a positive braid on $n$ strands with $c$ crossings, $s = c-n+1$.
- **Torus knots**: $s(T_{p,q})=(p-1)(q-1)$.
- **Homogeneous knots** (Abe 2011): $s(K)=2g(K)= c-n+1$ from any homogeneous diagram, extending the positive-braid formula.
- **Adequate / almost-alternating families**: $s$ is determined by the extreme quantum gradings of $\mathrm{Kh}$.
- **Small crossing numbers**: $s$ is tabulated for all prime knots with $c \le 17$ (KnotJob, KnotTheory, Knot Atlas), and for many 18–20 crossing examples; Piccirillo's application reaches roughly 100 crossings on structured diagrams.
- **Refinements**: Lipshitz–Sarkar (2014) define Steenrod-square refinements $s_i$ of $s$ from the Khovanov homotopy type; these are combinatorial in the same (exponential) sense.
- **$\mathfrak{sl}_N$ family**: Lewark (2014) computes $s_N$ for 3-strand torus knots and shows $s_N/(N-1)$ are pairwise independent concordance homomorphisms.

## 5. Principal Obstacles

- **Filtration jumps are global.** $s$ is not read off any single graded piece of $\mathrm{Kh}(K)$; it records where a *specific homology class* $[\mathfrak{s}_o]$ sits in the $q$-filtration after cancelling the non-homogeneous differential $\Phi$. Local skein relations control graded Euler characteristics, not filtration levels of distinguished classes; every attempt at a $q$-degree-aware skein recursion for $s$ has failed because $s$ is not additive under crossing changes (it changes by $0$ or $2$, in a way not determined by local data).
- **Not a homomorphism of the Jones-type kind.** $s$ is a *concordance* homomorphism but not determined by $\mathrm{Kh}$ as a bigraded group: Manolescu–Marengon (2020) disproved the knight move conjecture, so the Lee spectral sequence has higher differentials not forced by the bigraded Khovanov groups.
- **Functoriality is essential to the proof, not just the definition.** The genus bound uses that the cobordism map on Lee homology is nonzero. Establishing that requires the Bar-Natan cobordism category and neck-cutting relations — 4-dimensional input smuggled into an ostensibly 2-dimensional theory. No purely diagrammatic argument currently produces $|s|\le 2g_4$.
- **Complexity.** The Jones polynomial is $\\#\mathsf{P}$-hard to evaluate (Jaeger–Vertigan–Welsh 1990), and Khovanov homology refines it; while $s$ is a coarser number, no reduction proves hardness and no subexponential algorithm exists. Best practice (Bar-Natan's divide-and-conquer over the cobordism category, Schütz's variants) is exponential in the worst case with good behaviour on low-girth diagrams.
- **Gauge-theoretic shadow.** Kronheimer–Mrowka's $s^{\sharp}$, defined from instanton homology, agrees with $s$ conjecturally but not provably; the pieces of $s$ that "know" the slice genus may intrinsically encode 4-dimensional information beyond combinatorics.

## 6. The Gap

Section 4 gives closed formulas exactly where $\mathrm{Kh}$ is thin or where the diagram is positive/homogeneous — cases in which $s$ collapses onto a classical invariant ($\sigma$ or $c-n+1$). Section 1 asks for a formula valid for *all* knots. The gap has two independent components:

1. **Structural.** For thin knots, the two Lee generators are forced into adjacent filtration levels by the shape of $\mathrm{Kh}$; for general knots the level of $[\mathfrak{s}_o]$ depends on higher Lee differentials $d_2, d_3,\dots$, which are *not* functions of $\mathrm{Kh}(K)$ (knight-move failure). Any combinatorial formula must therefore encode data strictly finer than the bigraded Khovanov groups yet coarser than the full filtered complex. No candidate structure of that intermediate size is known.
2. **Complexity-theoretic.** Even granting a formula, one must beat the $2^c$ cube. The precise open question: is $\{(D,k) : s(K_D)\ge k\}$ in $\mathsf{P}$, or is it hard for some standard class?

## 7. Current Research (as of June 2026)

- **Fast algorithms.** Schütz (Durham) maintains KnotJob, computing $s$ over $\mathbb{F}_2$ and $\mathbb{Q}$ by cancelling in the Bar-Natan cobordism category; integral versions and mod-$p$ discrepancies (Schütz; Lewark–Zibrowius) are actively explored.
- **Homotopy-theoretic refinements.** Lipshitz–Sarkar (Oregon/UCLA), Sarkar–Scaduto–Stoffregen: Steenrod operations and odd Khovanov homotopy types give $s_i$ refinements and stronger genus bounds.
- **Skein lasagna modules.** Morrison–Walker–Wedrich's $\mathrm{Kh}$-theoretic 4-manifold invariants; Ren–Willis (2024) compute them and detect exotic pairs *(frontier — verify)*. These reframe $s$ as a shadow of a genuinely 4-dimensional TQFT, arguing *against* a purely 3-dimensional combinatorial formula.
- **Generalized $s$-invariants.** Manolescu–Marengon–Sarkar–Willis extend $s$ to null-homologous surfaces in punctured $\mathbb{CP}^2$-like manifolds, giving new genus bounds.
- **Gauge-theory comparison.** Whether $s^{\sharp} = s$ remains open; a proof would tie the combinatorial invariant to instantons and likely explain why local formulas are hard to find.
- **Machine search.** Continuing FGMW-style searches for potential counterexamples to smooth 4D Poincaré, now bounded by $s$-computation cost rather than by ideas.

## 8. Future Work

- Find an intermediate algebraic invariant — e.g. the $\mathbb{F}_2$-Bockstein package of Shumakovitch, or a truncation of the filtered complex to $O(\mathrm{poly}(c))$ generators — provably determining $s$.
- Prove or disprove $s = s^{\sharp}$; Kronheimer–Mrowka explicitly pose this.
- Establish a hardness result for computing $s$, which would settle clause (3) negatively and redirect effort.
- Develop a genus bound for $s$ from the Bar-Natan tangle-local picture alone, eliminating the cobordism functor from the argument.
- Seek grid-diagram or braid-normal-form descriptions in the spirit of Manolescu–Ozsváth–Sarkar's combinatorial knot Floer homology, which turned $\tau$ into a finite matrix computation.

## 9. Key References

- **[Foundational]** M. Khovanov. *A categorification of the Jones polynomial.* Duke Math. J. 101 (2000), 359–426.
- **[Foundational]** E. S. Lee. *An endomorphism of the Khovanov invariant.* Adv. Math. 197 (2005), 554–586.
- **[Foundational]** J. Rasmussen. *Khovanov homology and the slice genus.* Invent. Math. 182 (2010), 419–447.
- **[Foundational]** P. B. Kronheimer, T. S. Mrowka. *Gauge theory for embedded surfaces, I.* Topology 32 (1993), 773–826.
- **[Foundational]** D. Bar-Natan. *Khovanov's homology for tangles and cobordisms.* Geom. Topol. 9 (2005), 1443–1499.
- **[Foundational]** M. Jacobsson. *An invariant of link cobordisms from Khovanov homology.* Algebr. Geom. Topol. 4 (2004), 1211–1251.
- **[SOTA]** P. B. Kronheimer, T. S. Mrowka. *Khovanov homology is an unknot-detector.* Publ. Math. IHÉS 113 (2011), 97–208.
- **[SOTA]** R. Lipshitz, S. Sarkar. *A refinement of Rasmussen's s-invariant.* Duke Math. J. 163 (2014), 923–952.
- **[SOTA]** L. Piccirillo. *The Conway knot is not slice.* Ann. of Math. 191 (2020), 581–591.
- **[SOTA]** C. Manolescu, M. Marengon. *The knight move conjecture is false.* Proc. Amer. Math. Soc. 148 (2020), 435–439.
- **[SOTA]** C. Manolescu, M. Marengon, S. Sarkar, M. Willis. *A generalization of Rasmussen's invariant, with applications to surfaces in some four-manifolds.* Duke Math. J. 172 (2023), 231–311.
- **[SOTA]** D. Schütz. *A fast algorithm for calculating S-invariants.* Glasg. Math. J. 62 (2020), 617–642.
- **[Computational]** M. Freedman, R. Gompf, S. Morrison, K. Walker. *Man and machine thinking about the smooth 4-dimensional Poincaré conjecture.* Quantum Topology 1 (2010), 171–208.
- **[Related]** M. Hedden, P. Ording. *The Ozsváth–Szabó and Rasmussen concordance invariants are not equal.* Amer. J. Math. 130 (2008), 441–453.
- **[Related]** A. Lobb. *A slice genus lower bound from sl(n) Khovanov–Rozansky homology.* Adv. Math. 222 (2009), 1220–1276.
- **[Related]** H. Wu. *On the quantum filtration of the Khovanov–Rozansky cohomology.* Adv. Math. 221 (2009), 54–139.
- **[Related]** T. Abe. *The Rasmussen invariant of a homogeneous knot.* Proc. Amer. Math. Soc. 139 (2011), 2647–2656.
- **[Related]** C. Manolescu, P. Ozsváth, S. Sarkar. *A combinatorial description of knot Floer homology.* Ann. of Math. 169 (2009), 633–660.
- **[Survey]** P. Turner. *Five lectures on Khovanov homology.* J. Knot Theory Ramifications 26 (2017), 1741009.

## 10. Worked Example / Concrete Special Case

Take the right-handed trefoil $K = T_{2,3}$ from the standard closed-braid diagram $\hat\sigma_1^3$: $c=3$, $n_+=3$, $n_-=0$.

**Khovanov homology.** Over $\mathbb{Q}$,
$$\mathrm{Kh}^{i,j}(T_{2,3}) = \mathbb{Q} \text{ for } (i,j)\in\{(0,1),(0,3),(2,5),(3,9)\},\quad 0 \text{ otherwise.}$$

**Lee homology.** $\dim \mathrm{Kh}_{\mathrm{Lee}} = 2$, concentrated in $i=0$. The two generators come from the two orientations of the oriented resolution (two circles, since $\hat\sigma_1^3$ resolved at all positive crossings gives $2$ circles):
$$\mathfrak{s}_o = a\otimes a,\qquad \mathfrak{s}_{\bar o} = b\otimes b,\qquad a=X+1,\ b=X-1 .$$
In the $q$-filtration, $a\otimes a = 1\otimes 1 + 1\otimes X + X\otimes 1 + X\otimes X$ has leading term $1\otimes 1$ in $q$-degree $1+2n_+-n_- \cdot(\cdot)$; after the global shift $q \mapsto q + n_+ - 2n_- + \deg$, the oriented-resolution generators sit in $q$-degrees $\{1,3\}$ (matching the surviving $\mathrm{Kh}$ classes at $(0,1)$ and $(0,3)$). One checks $[a\otimes a]$ and $[b\otimes b]$ span, $[a\otimes a + b\otimes b] = 2[1\otimes X + X\otimes 1]$ has filtration $3$, and any other class has filtration $1$. Hence
$$s_{\min}=1,\quad s_{\max}=3,\quad s(T_{2,3}) = s_{\min}+1 = 2 .$$

**Consequence.** $2 = |s| \le 2g_4 \le 2g_3 = 2$, so $g_4(T_{2,3})=1$: the trefoil is not slice, and the bound is sharp. Consistency check with Section 4: positive braid formula $s = c-n+1 = 3-2+1 = 2$. ✓

**Where the problem bites.** Nothing in this computation was local. The value $s=2$ emerged from cancelling $d_{\mathrm{Lee}}$ across all $2^3 = 8$ vertices of the cube and then measuring a filtration level. For $\hat\sigma_1^{2k+1}=T_{2,2k+1}$ the answer is the arithmetic sequence $s=2k$, yet no recursion of the form $s(D) = f\big(s(D_0), s(D_1)\big)$ over a crossing resolution reproduces it: replacing one positive crossing of $T_{2,5}$ by its $0$-resolution gives the unknot ($s=0$) and by its $1$-resolution gives the Hopf link, for which $s$ of a link is a different (link) invariant, so the local data $\{0,\cdot\}$ cannot distinguish $s(T_{2,5})=4$ from $s(T_{2,3})=2$ without carrying the whole filtered complex along. That failure, at three crossings, is the same failure that blocks the general problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*