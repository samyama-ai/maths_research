---
id: 04-topology/exotic-smooth-structures-noncompact-4manifolds
title: "Existence of Exotic Smooth Structures on S^3 x R"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Existence of Exotic Smooth Structures on $S^3 \times \mathbb{R}$

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/exotic-smooth-structures-noncompact-4manifolds` · **Status:** open

## 1. Problem Statement / Conjecture

Let $S^3\times\mathbb{R}$ carry its standard smooth structure. A smooth 4-manifold $X$ is an **exotic $S^3\times\mathbb{R}$** if $X$ is homeomorphic but not diffeomorphic to $S^3\times\mathbb{R}$.

Two questions must be separated, because they have different answers.

- **(A) Unrestricted existence.** Do exotic $S^3\times\mathbb{R}$'s exist? *Answer: yes.* Puncturing any exotic $\mathbb{R}^4$ produces one (Section 10). Consequently the honest open problem here is not existence but **classification**: describe the set of diffeomorphism classes of smooth manifolds homeomorphic to $S^3\times\mathbb{R}$, and decide which are distinguished by end invariants.
- **(B) End-standard existence — the open problem.** Call $X$ **doubly collared** if each of its two ends has a neighbourhood of infinity diffeomorphic to $S^3\times[0,\infty)$. *Does there exist a doubly collared exotic $S^3\times\mathbb{R}$?*

**Claim tracked by this page.** Question (B) is equivalent to the failure of the smooth 4-dimensional Poincaré conjecture (SPC4): a doubly collared exotic $S^3\times\mathbb{R}$ exists **iff** some homotopy 4-sphere is not diffeomorphic to $S^4$. A complete resolution means either exhibiting such an $X$ (equivalently, an exotic homotopy 4-sphere) or proving SPC4. The proof of the equivalence is elementary given Cerf–Hatcher and is worked out in Section 10; the content of the problem is entirely SPC4.

## 2. Mathematical Foundations

**Ends.** For a manifold $X$, the end space is the inverse limit
$$\mathcal{E}(X)=\varprojlim_{K\Subset X}\pi_0\big(X\setminus K\big),$$
over compact $K$. $S^3\times\mathbb{R}$ has $|\mathcal{E}|=2$; $\mathbb{R}^4$ has $|\mathcal{E}|=1$. An end $\varepsilon$ is **smoothly collared** by $S^3$ if some neighbourhood of $\varepsilon$ is diffeomorphic to $S^3\times[0,\infty)$, and **topologically collared** if the same holds up to homeomorphism.

**Homotopy type.** $S^3\times\mathbb{R}\simeq S^3$, so $\pi_1=0$, $H_*(X;\mathbb{Z})=H_*(S^3)$, $\chi(X)=0$, and the intersection form is trivial. Every such $X$ is spin and parallelizable.

**Topological rigidity.** By Freedman's classification plus Quinn's work in dimensions 4 and 5, a smooth 4-manifold with the proper homotopy type and end structure of $S^3\times\mathbb{R}$ is homeomorphic to it; and every *noncompact* topological 4-manifold is smoothable, so the topological–smooth gap is entirely in the diffeomorphism classification.

**Smoothing theory and why dimension 4 is special.** For $M^m$ with $m\ge 5$, concordance classes of smoothings of $M$ are in bijection with $[M,\mathrm{Top}/O]$. For $M=S^n\times\mathbb{R}\simeq S^n$ this gives
$$\mathcal{S}(S^n\times\mathbb{R})\;\cong\;[S^n,\mathrm{Top}/O]\;=\;\pi_n(\mathrm{Top}/O)\;\cong\;\Theta_n \quad (n\ge 5),$$
with $\Theta_n$ the Kervaire–Milnor group of homotopy $n$-spheres. The bijection fails exactly in dimension 4, where $\mathrm{Top}/O$ has $\pi_3(\mathrm{Top}/O)=0$ but handle decompositions are unavailable smoothly.

**Gluing uniqueness (used repeatedly).** By Cerf ($\Gamma_4=0$) and Hatcher's proof of the Smale conjecture,
$$\mathrm{Diff}(S^3)\;\simeq\;O(4),\qquad \pi_0\,\mathrm{Diff}^+(S^3)=1 .$$
Hence a smooth 4-manifold obtained by gluing $D^4$ to a smooth $S^3$-collar is well defined up to diffeomorphism, and
$$D^4\cup_{S^3}\big(S^3\times[0,\infty)\big)\;\cong\;\mathbb{R}^4,\qquad D^4\cup_{S^3}\big(S^3\times[0,1]\big)\cup_{S^3}D^4\;\cong\;S^4 .$$

**SPC4.** Every homotopy 4-sphere $\Sigma$ is homeomorphic to $S^4$ (Freedman); SPC4 asserts $\Sigma\cong_{\mathrm{diff}} S^4$.

## 3. History & State of the Art (SOTA)

- **1982.** Freedman classifies simply connected topological 4-manifolds; Quinn supplies the 4- and 5-dimensional end theorems, giving smoothability of open topological 4-manifolds.
- **1983–85.** Gompf constructs "three exotic $\mathbb{R}^4$'s" and then an infinite family, combining Freedman's theory with Donaldson's diagonalization theorem.
- **1986.** Freedman–Taylor build a *universal* exotic $\mathbb{R}^4$: a smoothing $\mathbb{R}^4_U$ into which every exotic $\mathbb{R}^4$ smoothly embeds as an open set.
- **1987.** Taubes develops gauge theory on **end-periodic** 4-manifolds, producing uncountably many exotic $\mathbb{R}^4$'s and, for the first time, invariants sensitive to the smooth structure *at infinity*.
- **1992–93.** DeMichelis–Freedman produce uncountably many exotic $\mathbb{R}^4$'s embedded in standard $\mathbb{R}^4$; Gompf's "exotic menagerie" organizes end-sum constructions.
- **1998.** Bižaca–Etnyre study smooth structures on ends topologically collared by $S^3$, the precise setting of question (B).
- **2010–2021.** Serious computational and constructive attacks on SPC4: Freedman–Gompf–Morrison–Walker test Cappell–Shaneson spheres against Rasmussen's $s$-invariant; Akbulut proves an infinite family of Cappell–Shaneson spheres standard; Manolescu–Piccirillo generate candidate exotic pairs from zero-surgery homeomorphisms and rule several out.
- **State of the art.** Uncountably many exotic $S^3\times\mathbb{R}$'s are known (punctured exotic $\mathbb{R}^4$'s, plus end sums). **No** doubly collared example is known, and none can be known without disproving SPC4.

## 4. Partial Results / Verified Cases

- **Dimensions $\ne 4$.** $S^n\times\mathbb{R}$ is smoothly unique for $n\le 2$ (Moise/Radó, dimension $\le 3$) and for $n=4$ ($\pi_4(\mathrm{Top}/O)\cong\Theta_4=0$ by Cerf plus Kervaire–Milnor). For $n\ge 5$ smoothings are classified up to concordance by $\Theta_n$, e.g. $|\Theta_7|=28$, so $S^7\times\mathbb{R}$ carries 28 concordance classes.
- **Unrestricted case (A): solved affirmatively.** Every exotic $\mathbb{R}^4$ minus a point is an exotic $S^3\times\mathbb{R}$ (Section 10). Since DeMichelis–Freedman give uncountably many pairwise non-diffeomorphic exotic $\mathbb{R}^4$'s, $S^3\times\mathbb{R}$ carries at least $2^{\aleph_0}$ smooth structures — the maximum possible cardinality for a second-countable manifold.
- **End sums.** End-summing $S^3\times\mathbb{R}$ with any exotic $\mathbb{R}^4$ at one end yields further exotic smoothings; Gompf's menagerie techniques give infinite families with prescribed end behaviour.
- **Singly collared case.** There exist exotic $S^3\times\mathbb{R}$'s with *one* end smoothly collared: take $R\setminus\{p\}$ for $R$ exotic $\mathbb{R}^4$; the puncture end is a standard collar, the end at infinity is not.
- **Doubly collared case with extra hypotheses.** If $X$ is doubly collared and *additionally* contains a smoothly embedded $S^3$ generating $H_3(X)$ that separates the two collars into a smooth product cobordism, then $X\cong S^3\times\mathbb{R}$ (the cobordism is a smooth $h$-cobordism from $S^3$ to $S^3$, hence a product by dimension-3 uniqueness of the pieces after capping). No proof removes the product hypothesis.
- **Conditional.** SPC4 verified for infinitely many Cappell–Shaneson spheres (Akbulut 2010) and for the Gluck twists on many knotted 2-spheres; each such verification kills a candidate source of doubly collared exotica.

## 5. Principal Obstacles

- **Gauge theory is blind to $S^3\times\mathbb{R}$.** Donaldson and Seiberg–Witten invariants require compactness or controlled ends and are defined via moduli spaces on manifolds with $b_2^+>1$. $S^3\times\mathbb{R}$ has $b_2=0$; every candidate is homology-trivial, so instanton and monopole counts vanish or are undefined. Taubes' end-periodic theory needs a periodic end modelled on $Y\times\mathbb{R}$ with nontrivial $H_2$ input; a doubly collared exotic $S^3\times\mathbb{R}$ supplies none.
- **Compactification erases the invariant.** Any doubly collared $X$ compactifies to a homotopy 4-sphere $\Sigma$, and *all known* 4-manifold invariants (SW, Heegaard Floer, Khovanov-derived $s$, Bauer–Furuta) are trivial or standard on homotopy 4-spheres. This is the same wall that blocks SPC4.
- **No smooth $h$-cobordism theorem.** Smale's argument needs Whitney disks in dimension $\ge 5$. In dimension 4 they exist only topologically (Freedman's Casson-handle theory), which is exactly why the topological answer is rigid and the smooth answer is not.
- **Casson handles are uncontrollable.** The exotic structures that *are* known arise from Casson handles whose smooth type depends on unclassified infinite tree data; there is no invariant computing when two Casson handles are diffeomorphic, so constructions cannot be certified to be non-standard at a *collared* end.
- **Cerf's theorem cuts both ways.** $\pi_0\mathrm{Diff}(S^3)=1$ makes end-capping canonical — which is what forces the exotic phenomenon out of the collar and into SPC4, rather than allowing a separate, easier source of exotica.

## 6. The Gap

Proven: uncountably many exotic $S^3\times\mathbb{R}$'s, all with at least one end that is topologically but not smoothly collared. Open: whether the exoticism can be pushed entirely into the *compact* part, i.e. whether both ends can be simultaneously smoothly standard.

The precise barrier is the biconditional
$$\exists\ \text{doubly collared exotic } S^3\times\mathbb{R}\quad\Longleftrightarrow\quad \exists\ \Sigma^4 \text{ homotopy 4-sphere with } \Sigma\not\cong_{\mathrm{diff}} S^4 .$$
Crossing it requires either (i) a smooth invariant that is nontrivial on some homotopy 4-sphere — none currently exists, since $\Sigma$ has no homology to support gauge-theoretic counts — or (ii) a handle-calculus proof that every $\Sigma$ is standard, which needs a smooth 4-dimensional Whitney trick.

## 7. Current Research (as of June 2026)

- **Zero-surgery candidates.** Manolescu–Piccirillo's program converts knots with the same 0-surgery into candidate exotic pairs; extensions to homotopy-sphere production remain the most systematic current source of test cases. Several candidate families have been standardized rather than confirmed exotic.
- **Diffeomorphism groups of 4-manifolds.** Budney–Gabai's proof that $\pi_0\mathrm{Diff}(S^1\times D^3)$ is not finitely generated, and Gabai's 4-dimensional light bulb theorem, are being adapted to the isotopy questions governing how ends can be glued. Whether these detect end-phenomena on $S^3\times\mathbb{R}$ is unresolved *(frontier — verify)*.
- **Khovanov/skein obstructions.** Rasmussen's $s$ and its refinements remain the only invariants that could in principle certify an exotic $\Sigma$; every computed candidate to date has returned the standard value.
- **Open-manifold smoothing theory.** Gompf's minimal-genera work on open 4-manifolds continues to be the technical toolbox for controlling ends; refined end sums and "engulfing at infinity" arguments are the active technique.
- **Groups.** Texas (Gompf), Berkeley/MSRI-adjacent groups, Princeton/Stanford (Manolescu), UCLA, Rényi and Budapest (Stipsicz), Michigan/Gabai's circle at Princeton.

## 8. Future Work

- Build an invariant of *ends* of smooth 4-manifolds that survives capping — a relative or "end-Floer" theory for $S^3$-collared ends.
- Classify smooth structures on $S^3\times\mathbb{R}$ up to *end-preserving* diffeomorphism; conjecturally the invariant is the pair of germs of smoothings at infinity plus SPC4-type data.
- Decide whether the Freedman–Taylor universal $\mathbb{R}^4$ has a two-ended analogue: a universal exotic $S^3\times\mathbb{R}$ containing all others as open subsets.
- Continue the candidate-and-eliminate program on homotopy 4-spheres; each standardization result narrows question (B).
- Test whether infinite-order corks or Budney–Gabai style barbell diffeomorphisms can be spread along $\mathbb{R}$ to produce collared exotica.

## 9. Key References

- **[Foundational]** M. H. Freedman. *The topology of four-dimensional manifolds.* Journal of Differential Geometry 17 (1982), 357–453.
- **[Foundational]** F. Quinn. *Ends of maps, III: Dimensions 4 and 5.* Journal of Differential Geometry 17 (1982), 503–521.
- **[Foundational]** J. Cerf. *Sur les difféomorphismes de la sphère de dimension trois ($\Gamma_4=0$).* Lecture Notes in Mathematics 53, Springer, 1968.
- **[Foundational]** A. Hatcher. *A proof of the Smale conjecture, $\mathrm{Diff}(S^3)\simeq O(4)$.* Annals of Mathematics 117 (1983), 553–607.
- **[Foundational]** R. E. Gompf. *Three exotic $\mathbb{R}^4$'s and other anomalies.* Journal of Differential Geometry 18 (1983), 317–328.
- **[Foundational]** R. E. Gompf. *An infinite set of exotic $\mathbb{R}^4$'s.* Journal of Differential Geometry 21 (1985), 283–300.
- **[Foundational]** M. H. Freedman and L. R. Taylor. *A universal smoothing of four-space.* Journal of Differential Geometry 24 (1986), 69–78.
- **[Foundational]** C. H. Taubes. *Gauge theory on asymptotically periodic 4-manifolds.* Journal of Differential Geometry 25 (1987), 363–430.
- **[SOTA / Recent]** S. DeMichelis and M. H. Freedman. *Uncountably many exotic $\mathbb{R}^4$'s in standard 4-space.* Journal of Differential Geometry 35 (1992), 219–254.
- **[SOTA / Recent]** R. E. Gompf. *An exotic menagerie.* Journal of Differential Geometry 37 (1993), 199–223.
- **[SOTA / Recent]** Ž. Bižaca and J. B. Etnyre. *Smooth structures on collarable ends of 4-manifolds.* Topology 37 (1998), 461–467.
- **[SOTA / Recent]** S. Akbulut. *Cappell–Shaneson homotopy spheres are standard.* Annals of Mathematics 171 (2010), 2171–2175.
- **[SOTA / Recent]** M. Freedman, R. Gompf, S. Morrison, K. Walker. *Man and machine thinking about the smooth 4-dimensional Poincaré conjecture.* Quantum Topology 1 (2010), 171–208.
- **[SOTA / Recent]** R. E. Gompf. *Minimal genera of open 4-manifolds.* Geometry & Topology 21 (2017), 107–155.
- **[SOTA / Recent]** C. Manolescu and L. Piccirillo. *From zero surgeries to candidates for exotic definite four-manifolds.* Journal of the London Mathematical Society, 2023.
- **[SOTA / Recent]** R. Budney and D. Gabai. *Knotted 3-balls in $S^4$.* (2019; published version in Geometry & Topology, 2023.)
- **[Survey]** M. H. Freedman and F. Quinn. *Topology of 4-Manifolds.* Princeton Mathematical Series 39, Princeton University Press, 1990.
- **[Survey]** R. E. Gompf and A. I. Stipsicz. *4-Manifolds and Kirby Calculus.* Graduate Studies in Mathematics 20, American Mathematical Society, 1999.
- **[Survey]** R. Kirby and L. Siebenmann. *Foundational Essays on Topological Manifolds, Smoothings, and Triangulations.* Annals of Mathematics Studies 88, Princeton University Press, 1977.

## 10. Worked Example / Concrete Special Case

**Step 1 — puncturing an exotic $\mathbb{R}^4$ settles question (A).**

Let $R$ be one of Gompf's exotic $\mathbb{R}^4$'s and $p\in R$. Set $X=R\setminus\{p\}$.

- *Topological type.* $R\cong_{\mathrm{homeo}}\mathbb{R}^4$, and $\mathbb{R}^4\setminus\{0\}\cong S^3\times\mathbb{R}$ via $x\mapsto\big(x/|x|,\ \log|x|\big)$. So $X\cong_{\mathrm{homeo}} S^3\times\mathbb{R}$.
- *Smooth type.* Suppose $\varphi:X\to S^3\times\mathbb{R}$ were a diffeomorphism. Near $p$ choose a smooth chart, so the puncture end of $X$ has a neighbourhood diffeomorphic to $S^3\times[0,\infty)$, and $R$ is recovered as
$$R\;=\;X\cup_{S^3\times[0,\infty)} D^4 .$$
Transporting by $\varphi$, $R$ is diffeomorphic to $D^4$ glued to one end of $S^3\times\mathbb{R}$. By $\pi_0\mathrm{Diff}^+(S^3)=1$ (Hatcher) the gluing is unique up to isotopy, so
$$R\;\cong_{\mathrm{diff}}\;D^4\cup_{S^3}\big(S^3\times[0,\infty)\big)\;\cong\;\mathbb{R}^4,$$
contradicting exoticness. Hence $X$ is an exotic $S^3\times\mathbb{R}$. Running this over the DeMichelis–Freedman uncountable family gives $2^{\aleph_0}$ smooth structures. Note the asymmetry: the puncture end of $X$ is smoothly collared, the other end is not — so $X$ is **not** a witness for question (B).

**Step 2 — the doubly collared case is exactly SPC4.**

($\Leftarrow$) Let $\Sigma$ be a homotopy 4-sphere with $\Sigma\not\cong_{\mathrm{diff}}S^4$, and put $X=\Sigma\setminus\{p,q\}$. Then $X\cong_{\mathrm{homeo}}S^4\setminus\{2\text{ pts}\}\cong S^3\times\mathbb{R}$, and both ends are smooth punctured-ball collars, so $X$ is doubly collared. If $X\cong_{\mathrm{diff}}S^3\times\mathbb{R}$, capping both ends and using uniqueness of the gluing gives
$$\Sigma\;\cong\;D^4\cup_{S^3}\big(S^3\times[0,1]\big)\cup_{S^3}D^4\;\cong\;S^4,$$
a contradiction. So $X$ is a doubly collared exotic $S^3\times\mathbb{R}$.

($\Rightarrow$) Conversely, let $X$ be doubly collared and exotic. Cap each collar with $D^4$ to get a closed smooth 4-manifold $\Sigma$. Then $\Sigma$ is simply connected with $H_*(\Sigma)=H_*(S^4)$, hence a homotopy 4-sphere. If $\Sigma\cong_{\mathrm{diff}}S^4$, then removing the two cap centres gives $X\cong_{\mathrm{diff}}S^4\setminus\{2\text{ pts}\}\cong S^3\times\mathbb{R}$, contradicting exoticness. So $\Sigma$ is an exotic homotopy 4-sphere.

**Conclusion.** The two constructions are mutually inverse up to diffeomorphism, establishing the biconditional of Section 6. Question (B) is therefore not merely *related to* SPC4 — it is a restatement of it, which is precisely why no doubly collared example has ever been produced despite forty years of exotic $\mathbb{R}^4$ technology.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*