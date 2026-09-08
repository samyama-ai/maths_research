---
id: 04-topology/sullivan-conjecture
title: "Sullivan Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sullivan Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/sullivan-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $p$ be a prime, $G$ a finite $p$-group (or, more generally, a locally finite group all of whose elements have prime-power order), and let $X$ be a **finite-dimensional** CW complex. The Sullivan conjecture asserts:

$$\mathrm{Map}\big(BG,\,X\big) \;\xrightarrow{\ \mathrm{ev}\ }\; X$$

is a weak homotopy equivalence, where $\mathrm{ev}$ is evaluation at the basepoint. Equivalently, the space of pointed maps $\mathrm{Map}_*(BG, X)$ is weakly contractible: every map $BG \to X$ is null-homotopic, and canonically so through all higher homotopies.

The **generalized (fixed-point) Sullivan conjecture** — Sullivan's original formulation — says that for a finite-dimensional $G$-CW complex $X$ with $G$ a finite $p$-group, the inclusion of honest fixed points into homotopy fixed points

$$X^G \longrightarrow X^{hG} := \mathrm{Map}_G(EG, X)$$

induces an equivalence after $p$-completion: $(X^G)^{\wedge}_p \xrightarrow{\ \simeq\ } (X^{hG})^{\wedge}_p$.

Both statements are **theorems**: Miller (1984) for the mapping-space form, Carlsson and Lannes (1984–1992) for the equivariant form. The catalog entry remains active because several natural strengthenings — compact Lie group actions, non-finite-dimensional targets under weaker hypotheses, and motivic/real-étale analogues — remain open. A complete resolution of those variants requires either a proof or an explicit counterexample space.

## 2. Mathematical Foundations

**Unstable modules.** Let $\mathcal{A}$ be the mod-$p$ Steenrod algebra. An $\mathcal{A}$-module $M$ is *unstable* if $Sq^i x = 0$ for $i > |x|$ (at $p=2$), or $\beta^{\varepsilon}P^i x = 0$ for $2i+\varepsilon > |x|$ (odd $p$). Let $\mathcal{U}$ denote the category of unstable modules and $\mathcal{K}$ the category of unstable algebras.

**The test object.** For $V = (\mathbb{Z}/p)^n$ elementary abelian,
$$H^*(BV;\mathbb{F}_2) \cong \mathbb{F}_2[x_1,\dots,x_n], \quad |x_i| = 1,$$
$$H^*(BV;\mathbb{F}_p) \cong \Lambda(x_1,\dots,x_n)\otimes \mathbb{F}_p[y_1,\dots,y_n],\quad |x_i|=1,\ y_i=\beta x_i,\ p \text{ odd}.$$

**Miller's injectivity theorem.** $H^*(BV;\mathbb{F}_p)$ is an injective object in $\mathcal{U}$, and tensor products of such with finite unstable modules are injective (Lannes–Schwartz). This is the algebraic engine of the proof.

**Lannes' $T$-functor.** $T_V : \mathcal{U}\to\mathcal{U}$ is the left adjoint of $M \mapsto H^*(BV)\otimes M$:
$$\mathrm{Hom}_{\mathcal{U}}\big(T_V M, N\big) \;\cong\; \mathrm{Hom}_{\mathcal{U}}\big(M,\ H^*(BV)\otimes N\big).$$
$T_V$ is **exact** and commutes with tensor products and suspension: $T_V\Sigma \cong \Sigma T_V$, $T_V\mathbb{F}_p = \mathbb{F}_p$. It restricts to a left adjoint on $\mathcal{K}$.

**Lannes' main theorem.** If $X$ is a space with $H^*(X;\mathbb{F}_p)$ of finite type and $T_V H^*(X;\mathbb{F}_p)$ of finite type, then
$$H^*\big(\mathrm{Map}(BV,X)^{\wedge}_p;\mathbb{F}_p\big) \;\cong\; T_V H^*(X;\mathbb{F}_p),$$
and components correspond to $\mathcal{K}$-maps $H^*X \to H^*BV$.

**Reduction to elementary abelian $V$.** For a finite $p$-group $G$, a transfer/Quillen-stratification argument reduces $\mathrm{Map}(BG,X)$ to the elementary abelian case; this is why $H^*(BV)$ is the only test object needed.

**Homotopy fixed points.** $X^{hG} = \mathrm{Map}_G(EG,X)$ sits in the Bousfield–Kan spectral sequence
$$E_2^{s,t} = H^s\big(G; \pi_t X\big) \Longrightarrow \pi_{t-s}\big(X^{hG}\big),$$
whose convergence is the analytic issue behind the equivariant statement.

## 3. History & State of the Art (SOTA)

- **1970.** Dennis Sullivan, in his MIT notes *Geometric Topology: Localization, Periodicity and Galois Symmetry*, formulates the fixed-point conjecture, motivated by Galois symmetry of the profinite completion of algebraic varieties: the Adams conjecture and the action of $\hat{\mathbb{Z}}^\times$ suggested that $p$-adic homotopy theory cannot detect a difference between $X^G$ and $X^{hG}$ in finite dimensions.
- **1970s.** Special cases accumulate: $[B\mathbb{Z}/p, S^n] = 0$ verified in low ranges; Miller, Zabrodsky and others develop phantom-map and Postnikov obstruction methods. Zabrodsky's lemma (maps out of $BG$ vanishing on a fibre) becomes a standard tool.
- **1983–84.** Haynes Miller proves the mapping-space form: *The Sullivan conjecture on maps from classifying spaces*, Annals of Mathematics **120** (1984), 39–87 (correction, Annals **121** (1985), 605–609). Method: an unstable Adams-type resolution built from injectivity of $H^*(BV)$ in $\mathcal{U}$, plus a $\lim^1$ vanishing argument.
- **1984.** Gunnar Carlsson proves the Segal conjecture for elementary abelian $p$-groups (Annals **120**, 189–224), the stable counterpart, giving $\pi_*^{s}(BV)$ as a completion of the Burnside ring.
- **1986–92.** Jean Lannes builds the $T$-functor, converting the conjecture into computable algebra and yielding the strong form $H^*(\mathrm{Map}(BV,X)^\wedge_p) = T_V H^*X$ (Publ. IHÉS **75**, 1992). Carlsson (Invent. Math. **103**, 1991) gives an equivariant stable-homotopy proof of the fixed-point form.
- **1989–94.** Dwyer–Miller–Neisendorfer settle fibrewise completion issues; Dwyer–Wilkerson apply homotopy-fixed-point technology to $p$-compact groups (Annals **139**, 1994). Schwartz's 1994 book consolidates the algebra.
- **2010s–2020s.** Motivic and real-étale analogues (Heller–Ormsby; Bachmann) transport the statement to $\mathbb{A}^1$-homotopy theory over $\mathbb{R}$.

## 4. Partial Results / Verified Cases

Fully proven regimes:

- $G$ finite $p$-group, $X$ finite-dimensional CW: **theorem** (Miller 1984). Extends to $G$ locally finite with all elements of prime-power order.
- $X$ a finite complex, $X = S^n$, $X$ a finite Postnikov-truncation-free space: $\mathrm{Map}_*(B\mathbb{Z}/p, X) \simeq *$.
- $X = BG'$ with $G'$ a compact Lie group: Dwyer–Zabrodsky (1987) and Notbohm compute $[BG, BG'] \cong \mathrm{Rep}(G,G')$ for $G$ a finite $p$-group — a non-contractible but completely determined mapping space (here $X$ is infinite-dimensional, so this complements rather than contradicts §1).
- Equivariant form: $G$ a finite $p$-group acting on a finite-dimensional $G$-CW complex $X$ with $H^*(X;\mathbb{F}_p)$ of finite type — $(X^G)^\wedge_p \simeq (X^{hG})^\wedge_p$ (Carlsson 1991, Lannes 1992).
- $X$ of finite $\mathbb{F}_p$-cohomological dimension but infinite-dimensional as a complex: holds when $H^*(X;\mathbb{F}_p)$ is *locally finite* (nilpotent as an unstable algebra), by $T_V$-computation.
- Stable range: the Segal conjecture $\pi^0_s(BG)^{\wedge} \cong A(G)^{\wedge}_I$ for all finite $G$ (Carlsson 1984), and for $G = (\mathbb{Z}/p)^n$ the full $\pi_*^s$ statement.

Known failures marking the sharpness of hypotheses: $X = K(\mathbb{Z}/p, n)$ gives $[B\mathbb{Z}/p, X] = H^n(B\mathbb{Z}/p;\mathbb{Z}/p) \neq 0$; $G = \mathbb{Z}$ gives $BG = S^1$ and $\mathrm{Map}(S^1,X) = LX \not\simeq X$.

## 5. Principal Obstacles

The remaining open variants resist current methods for concrete reasons.

- **Convergence of the unstable Adams spectral sequence.** Miller's proof needs the $\lim^1$ term of a tower of principal fibrations to vanish; this uses finite-dimensionality of $X$ in an essential way. For infinite-dimensional $X$ with non-locally-finite cohomology, the tower has genuine phantom phenomena and the spectral sequence can fail to converge to $\pi_*\mathrm{Map}(BV,X)$.
- **$T$-functor hypotheses.** Lannes' theorem requires $T_V H^*X$ to be of finite type. For $X$ with cohomology of infinite type — e.g. classifying spaces of infinite discrete groups — $T_V$ computes an object with no known space-level realization, so cohomological input does not return homotopical output.
- **Compact Lie groups.** For $G$ a positive-dimensional compact Lie group, $BG$ has $\mathbb{F}_p$-cohomology that is not locally finite and there is no reduction to elementary abelian subgroups by transfer alone; the Segal conjecture in the compact Lie setting is only partially known, so the stable model that guided Carlsson's argument is unavailable.
- **Non-$p$-group isotropy.** The equivariant statement is false for $G = \mathbb{Z}/pq$: $\mathbb{F}_p$-completion cannot see the $q$-part, and homotopy fixed points are computed one prime at a time. Assembling primes requires an arithmetic-fracture argument that fails when $X^G$ is empty but $X^{hG}$ is not.
- **Integral versus mod-$p$.** All proofs are intrinsically mod-$p$: injectivity of $H^*(BV)$ holds in $\mathcal{U}$ over $\mathbb{F}_p$ and has no integral analogue. So statements about $X^G \to X^{hG}$ before completion are inaccessible.
- **Motivic setting.** In $\mathbb{A}^1$-homotopy theory there is no Steenrod-algebra injectivity theorem for the motivic classifying space $B_{\mathrm{gm}}\mu_p$; the motivic Steenrod algebra acts on a bigraded object and the notion of "unstable module" that would carry Miller's argument is not established.

## 6. The Gap

The gap is now not in the classical statement but at its boundary. Precisely:

1. **Finite-dimensionality → finite $\mathbb{F}_p$-cohomological dimension.** Proven: $\dim X < \infty$. Desired: $X$ with $H^i(X;\mathbb{F}_p)=0$ for $i \gg 0$ but $X$ infinite-dimensional, with no local-finiteness assumption on $\pi_*$. The missing step is a $\lim^1$-vanishing statement for the Bousfield–Kan tower depending only on cohomological, not geometric, dimension.
2. **Finite $p$-group → compact Lie group.** Proven for $G$ finite $p$-group. Desired: $\mathrm{Map}(BG,X)\simeq X$ for $G$ compact Lie and $X$ finite-dimensional. Missing: a Quillen-type reduction of $\mathrm{Map}(BG,-)$ to elementary abelian $p$-tori together with a compact-Lie Segal conjecture strong enough to control the stable range.
3. **Classical → motivic.** Desired: for $X$ a finite-dimensional motivic space over $\mathbb{R}$, is $X^{C_2} \to X^{hC_2}$ a $2$-adic equivalence after real realization, in the form predicted by real-étale localization? Missing: an unstable motivic injectivity theorem.

## 7. Current Research (as of June 2026)

- **Motivic/real-étale analogues.** Heller–Ormsby's comparison of $C_2$-equivariant and $\mathbb{R}$-motivic stable homotopy, and Bachmann's real-étale localization theorem, give a stable Sullivan-type statement over $\mathbb{R}$. Unstable versions are being pursued at Oslo, Ohio State and Osnabrück. *(frontier — verify)*
- **Chromatic reformulations.** The vanishing $\mathrm{Map}_*(BV, X)\simeq *$ is being reinterpreted via the theory of $T(n)$- and $K(n)$-local ambidexterity: $BV$ is "$\infty$-dimensional in a chromatic direction", and the Sullivan phenomenon is a shadow of the failure of finite chromatic complexity. Groups at MIT, Northwestern and the Hebrew University pursue this. *(frontier — verify)*
- **$\infty$-categorical fixed points.** Reformulation of $X^G \to X^{hG}$ as a statement about the Tate construction $X^{tG}$ being $\mathbb{F}_p$-trivial in finite dimensions; connections to Nikolaus–Scholze cyclotomic-structure formalism. *(frontier — verify)*
- **Algebraic side.** Ongoing work in the category $\mathcal{U}$ on Krull filtration, nilpotent localization and the structure of injectives (Schwartz's school, Paris 13/Nord and Hanoi), aimed at $T_V$-computations for spaces of infinite type.
- **Applications.** Homotopy-theoretic classification of $p$-compact groups and fusion systems continues to consume the Sullivan theorem as a black box (Broto–Levi–Oliver framework).

## 8. Future Work

- Prove or disprove a **cohomological-dimension** version of Miller's theorem, replacing $\dim X<\infty$ by $\mathrm{cd}_{\mathbb{F}_p}(X)<\infty$; this is the version most useful in geometric applications.
- Develop a **compact Lie Segal conjecture** at the level needed to run Carlsson's argument for $G=S^1$, $G = SU(2)$.
- Construct an **unstable motivic Steenrod-module category** in which $H^{*,*}(B\mu_p)$ is injective; this is the acknowledged prerequisite for a motivic Sullivan conjecture.
- Extend $T$-functor calculus to **spectra with $G$-action over ring spectra other than $H\mathbb{F}_p$**, testing whether the phenomenon is specific to mod-$p$ cohomology or chromatic in origin.
- Find effective bounds: given $\dim X = d$, produce an explicit null-homotopy of a map $B\mathbb{Z}/p \to X$ with complexity bounded in terms of $d$ — currently the proofs are non-constructive.

## 9. Key References

- **[Foundational]** D. Sullivan. *Geometric Topology: Localization, Periodicity and Galois Symmetry* (1970 MIT notes), ed. A. Ranicki, K-Monographs in Mathematics vol. 8, Springer, 2005.
- **[Foundational]** H. Miller. *The Sullivan conjecture on maps from classifying spaces.* Annals of Mathematics **120** (1984), 39–87. Correction: Annals of Mathematics **121** (1985), 605–609. [DOI](https://doi.org/10.2307/2007071)
- **[Foundational]** G. Carlsson. *Equivariant stable homotopy and Segal's Burnside ring conjecture.* Annals of Mathematics **120** (1984), 189–224. [DOI](https://doi.org/10.2307/2006940)
- **[Foundational]** G. Carlsson. *Equivariant stable homotopy and Sullivan's conjecture.* Inventiones Mathematicae **103** (1991), 497–525. [DOI](https://doi.org/10.1007/bf01239524)
- **[SOTA]** J. Lannes. *Sur les espaces fonctionnels dont la source est le classifiant d'un $p$-groupe abélien élémentaire.* Publications Mathématiques de l'IHÉS **75** (1992), 135–244.
- **[SOTA]** J. Lannes, L. Schwartz. *Sur la structure des $A$-modules instables injectifs.* Topology **28** (1989), 153–169. [DOI](https://doi.org/10.1016/0040-9383(89)90018-9)
- **[Survey]** L. Schwartz. *Unstable Modules over the Steenrod Algebra and Sullivan's Fixed Point Set Conjecture.* Chicago Lectures in Mathematics, University of Chicago Press, 1994.
- **[Survey]** H. Miller. *The Sullivan conjecture and homotopical representation theory.* Proceedings of the ICM, Berkeley 1986, AMS, 1987, pp. 580–589.
- **[Survey]** J. F. Adams. *Two theorems of J. Lannes.* In *The Selected Works of J. Frank Adams*, Vol. II, Cambridge University Press, 1992.
- **[Related]** W. Dwyer, A. Zabrodsky. *Maps between classifying spaces.* Lecture Notes in Mathematics **1298**, Springer, 1987, pp. 106–119.
- **[Related]** W. Dwyer, H. Miller, J. Neisendorfer. *Fibrewise completion and unstable Adams spectral sequences.* Israel Journal of Mathematics **66** (1989), 160–178. [DOI](https://doi.org/10.1007/bf02765891)
- **[Related]** W. Dwyer, C. Wilkerson. *Homotopy fixed-point methods for Lie groups and finite loop spaces.* Annals of Mathematics **139** (1994), 395–442. [DOI](https://doi.org/10.2307/2946585)
- **[Recent]** J. Heller, K. Ormsby. *Galois equivariance and stable motivic homotopy theory.* Transactions of the AMS **368** (2016), 8047–8077. [DOI](https://doi.org/10.1090/tran6647)

## 10. Worked Example / Concrete Special Case

**Claim.** $\mathrm{Map}_*(B\mathbb{Z}/2, S^n)$ is weakly contractible for every $n \ge 1$, while $\mathrm{Map}_*(B\mathbb{Z}/2, K(\mathbb{Z}/2,n)) \simeq \prod_{j} K(\mathbb{Z}/2, n-j)$ is not.

*Step 1 — the algebra.* Take $V=\mathbb{Z}/2$, $p=2$. Then $\widetilde H^*(S^n;\mathbb{F}_2) = \Sigma^n \mathbb{F}_2$, a single $\mathbb{F}_2$ in degree $n$.

*Step 2 — apply $T_V$.* $T_V$ is exact and commutes with suspension, and $T_V\mathbb{F}_2 = \mathbb{F}_2$ (adjunction against $H^*(BV)$ in degree $0$). Hence
$$T_V\big(H^*(S^n;\mathbb{F}_2)\big) \;\cong\; H^*(S^n;\mathbb{F}_2).$$
Writing $\overline{T}_V$ for the reduced part (the summand corresponding to non-constant components), $\overline{T}_V \Sigma^n\mathbb{F}_2 = 0$.

*Step 3 — Lannes' theorem.* $H^*(S^n;\mathbb{F}_2)$ and $T_VH^*(S^n;\mathbb{F}_2)$ are of finite type, so
$$H^*\big(\mathrm{Map}(B\mathbb{Z}/2,S^n)^{\wedge}_2;\mathbb{F}_2\big) \cong T_V H^*(S^n;\mathbb{F}_2) \cong H^*\big((S^n)^{\wedge}_2;\mathbb{F}_2\big),$$
with a single component. Evaluation $\mathrm{Map}(B\mathbb{Z}/2,S^n)\to S^n$ induces this isomorphism, so it is a mod-$2$ equivalence; the pointed mapping space is $2$-adically trivial. Miller's theorem upgrades this to weak contractibility integrally, since $S^n$ is finite-dimensional and simply connected for $n\ge 2$ (for $n=1$, $[B\mathbb{Z}/2,S^1]=H^1(B\mathbb{Z}/2;\mathbb{Z})=0$ directly).

*Step 4 — contrast.* For $X = K(\mathbb{Z}/2,n)$, which is infinite-dimensional,
$$\pi_j\,\mathrm{Map}_*(B\mathbb{Z}/2, K(\mathbb{Z}/2,n)) = \widetilde H^{n-j}(B\mathbb{Z}/2;\mathbb{Z}/2) = \mathbb{F}_2 \quad \text{for } 1\le n-j \le n .$$
So $\mathrm{Map}_*(B\mathbb{Z}/2,K(\mathbb{Z}/2,n))$ has $\mathbb{F}_2$ in $n$ distinct homotopy groups. Since $S^n \to K(\mathbb{Z}/2,n)$ is $(n+1)$-connected on the nose but the Postnikov tower of $S^n$ is infinite, the Sullivan phenomenon is exactly the statement that these nonzero contributions cancel through the whole tower for a finite-dimensional target — the cancellation is precisely what Miller's $\lim^1$ argument supplies.

*Step 5 — fixed-point reading.* Let $\mathbb{Z}/2$ act on $S^n$ by the antipodal map, a free action on a finite-dimensional complex. Then $X^{\mathbb{Z}/2}=\emptyset$ and $X^{h\mathbb{Z}/2} = \mathrm{Map}_{\mathbb{Z}/2}(E\mathbb{Z}/2, S^n)$; the Bousfield–Kan spectral sequence has $E_2^{s,t}=H^s(\mathbb{Z}/2;\pi_tS^n)$, and the generalized Sullivan conjecture predicts $(X^{h\mathbb{Z}/2})^\wedge_2 \simeq \emptyset$. Concretely: a $\mathbb{Z}/2$-equivariant map $E\mathbb{Z}/2 \to S^n$ would descend to $B\mathbb{Z}/2 \to \mathbb{RP}^n$ lifting the classifying map, which fails on $H^{n+1}$ since $w_1^{n+1}\ne 0$ in $H^*(B\mathbb{Z}/2)$ but vanishes in $H^*(\mathbb{RP}^n)$. This is Borsuk–Ulam, recovered as the simplest instance of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*