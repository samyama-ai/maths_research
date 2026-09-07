---
id: 03-geometry/goresky-macpherson-conjecture
title: "Goresky-MacPherson Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Goresky–MacPherson Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/goresky-macpherson-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Also called the **Rapoport conjecture** (Rapoport and Goresky–MacPherson formulated it independently in the mid-1980s).

Let $G$ be a connected semisimple algebraic group over $\mathbb{Q}$ whose symmetric space $D = G(\mathbb{R})/K$ is Hermitian, and let $\Gamma \subset G(\mathbb{Q})$ be a neat arithmetic subgroup, so that $X = \Gamma \backslash D$ is a smooth quasi-projective variety. Two compactifications sit over one another:

- $X^{*}$, the **Baily–Borel Satake compactification**, a normal projective variety, usually badly singular along its boundary;
- $\widehat{X}$, the **reductive Borel–Serre compactification**, a compact Hausdorff space which is not an algebraic variety;

together with a canonical continuous surjection $\pi : \widehat{X} \to X^{*}$ restricting to the identity on $X$.

**Conjecture.** For a coefficient system $\mathbb{E}$ on $X$ associated with a **regular** finite-dimensional representation $E$ of $G$, the map $\pi$ induces an isomorphism
$$
IH^{\bullet}_{\bar m}\!\left(X^{*}; \mathbb{E}\right) \;\xrightarrow{\ \sim\ }\; H^{\bullet}\!\left(\widehat{X}; \mathbb{E}\right),
$$
where $IH_{\bar m}$ is middle-perversity intersection cohomology. Sheaf-theoretically: the natural morphism $\mathcal{IC}_{X^{*}}(\mathbb{E}) \to R\pi_{*}\mathbb{E}$ is a quasi-isomorphism.

A complete proof must produce the isomorphism for every $\mathbb{Q}$-rank, every Hermitian $G$, and every regular $\mathbb{E}$, and ideally be compatible with the Hecke algebra action, since the arithmetic payoff (Zucker's conjecture, Lefschetz formulas for Hecke correspondences, comparison with automorphic forms) lives on the Hecke-module structure. The regularity hypothesis is not decorative: for $\mathbb{E} = \mathbb{Q}$ the statement is already false in complex dimension $2$ (§10).

## 2. Mathematical Foundations

**Borel–Serre.** $\overline{X}$ is a compact manifold with corners, $\Gamma \backslash D \hookrightarrow \overline{X}$ a homotopy equivalence, with boundary faces indexed by $\Gamma$-conjugacy classes of proper parabolic $\mathbb{Q}$-subgroups $P$. Writing $P = N_P A_P M_P$ (Langlands decomposition), the face is a nilmanifold bundle
$$
e(P) \;=\; \Gamma_{N_P}\backslash N_P \;\longrightarrow\; e'(P) \;=\; \Gamma_{M_P}\backslash D_{M_P}, \qquad D_{M_P} = M_P/(K \cap M_P).
$$

**Reductive Borel–Serre.** $\widehat{X} = \overline{X}/\!\sim$ collapses each nilmanifold fibre, so
$$
\widehat{X} \;=\; X \ \sqcup\ \bigsqcup_{P} X_P, \qquad X_P := \Gamma_{M_P}\backslash D_{M_P}.
$$

**Baily–Borel.** $X^{*} = X \sqcup \bigsqcup_{P \text{ maximal}} X_P^{h}$, where $X_P^{h}$ is the locally symmetric space of the Hermitian factor of $M_P$; $\pi$ maps $X_P$ onto $X_{P'}^{h}$ for the unique maximal $P' \supseteq P$.

**Intersection cohomology.** For a pseudomanifold with a stratification by strata of even real codimension and middle perversity $\bar m$, $\mathcal{IC}$ is Deligne's construction
$$
\mathcal{IC} \;=\; \tau_{\le d_r} Ri_{r*} \cdots \tau_{\le d_1} Ri_{1*}\mathbb{E}[\text{shift}],
$$
characterized by the support/cosupport conditions; for an isolated singular point $x$ with link $L$ in a space of complex dimension $n$,
$$
\mathcal{H}^{k}(\mathcal{IC})_x \;=\; \begin{cases} H^{k}(L) & k \le n-1,\\ 0 & k \ge n.\end{cases}
$$

**Weighted cohomology.** Goresky–Harder–MacPherson attach to a weight profile $\mu$ on $A_P$ a complex $\mathbf{W}^{\mu}\mathbb{E}$ on $\widehat{X}$ built by truncating the nilpotent Lie algebra cohomology $H^{\bullet}(\mathfrak{n}_P;E)$ by the $A_P$-weights. Their theorem: for the upper/lower middle profiles $\pm\mu$,
$$
R\pi_{*}\,\mathbf{W}^{\pm\mu}\mathbb{E} \;\simeq\; \mathcal{IC}_{X^{*}}(\mathbb{E}).
$$
Since $H^{\bullet}(\widehat{X};\mathbb{E})$ is the hypercohomology of the *untruncated* complex, the conjecture is equivalent to: the truncation map $H^{\bullet}(\widehat{X};\mathbb{E}) \to W^{\mu}H^{\bullet}(\widehat{X};\mathbb{E})$ is an isomorphism when $E$ is regular. Concretely, by Kostant's theorem the $\mathfrak{n}_P$-cohomology decomposes as
$$
H^{\bullet}(\mathfrak{n}_P;E) \;=\; \bigoplus_{w \in W^{P}} F_{w(\lambda+\rho)-\rho}, \qquad \ell(w) = \bullet,
$$
and regularity of the highest weight $\lambda$ forces every $A_P$-weight $w(\lambda+\rho)-\rho$ off the truncation wall, so no boundary class sits ambiguously between the two middle profiles.

## 3. History & State of the Art (SOTA)

- **1966.** Baily–Borel construct $X^{*}$ as a projective variety.
- **1973.** Borel–Serre construct $\overline{X}$; the reductive quotient $\widehat{X}$ appears in Zucker's work of the early 1980s.
- **1980–83.** Goresky–MacPherson introduce intersection homology, making "$IH$ of $X^{*}$" a meaningful object.
- **1980–82.** Zucker conjectures $IH^{\bullet}_{\bar m}(X^{*};\mathbb{E}) \cong H^{\bullet}_{(2)}(X;\mathbb{E})$; proved by Looijenga (1988) and Saper–Stern (1990).
- **mid-1980s.** Rapoport, motivated by the shape of the boundary contribution in Lefschetz formulas for Hecke correspondences on Shimura varieties, conjectures $IH^{\bullet}(X^{*}) \cong H^{\bullet}(\widehat{X})$; Goresky–MacPherson arrive at the same statement from stratified-topology considerations.
- **1994.** Goresky–Harder–MacPherson prove the weighted cohomology theorem, isolating the conjecture as a "no truncation needed" statement.
- **1999.** Nair identifies weighted cohomology with Franke's automorphic complexes, giving a spectral interpretation.
- **2001–2005.** Saper announces and publishes a proof via the theory of **$\mathcal{L}$-modules**: self-dual complexes on $\widehat{X}$ whose boundary behaviour is controlled by a micro-support condition. The Astérisque paper states the theorem; the technical engine is the long preprint *L-modules and micro-support*.

Status today: the conjecture is regarded as **proved** by specialists, with the caveat that the full apparatus remains in preprint form.

## 4. Partial Results / Verified Cases

- **$\mathbb{Q}$-rank $1$** (all Hermitian $G$, regular $\mathbb{E}$): verified by Zucker and by Saper–Stern (appendix to Rapoport's article). Here $\widehat{X} \to X^{*}$ collapses each $X_P$ to a point and the statement reduces to the vanishing of $H^{k}(X_P;H^{\bullet}(\mathfrak{n}_P;E))$ in the critical range.
- **Hilbert modular varieties** ($G = \mathrm{Res}_{F/\mathbb{Q}}\mathrm{SL}_2$, $F$ totally real of degree $g$): $\mathbb{Q}$-rank $1$, $\dim_{\mathbb{C}} = g$; verified directly, with the constant-coefficient failure explicit (§10).
- **Picard modular surfaces** ($\mathrm{SU}(2,1)$, $\mathbb{Q}$-rank $1$, $\dim_{\mathbb{C}} = 2$): the case that motivated Rapoport, where the boundary is a finite set of points.
- **Siegel modular threefolds** ($\mathrm{Sp}_4$, $\mathbb{Q}$-rank $2$): the first genuinely stratified case, with $0$-dimensional and $1$-dimensional (modular-curve) boundary strata; checked before the general proof.
- **$\mathbb{Q}$-rank $\le 2$** more generally, where the boundary poset of $X^{*}$ has depth $\le 2$ and Deligne's truncation can be tracked by hand.
- **General case:** Saper (2005), for all Hermitian $G$ over $\mathbb{Q}$, all $\mathbb{Q}$-ranks, and all regular $\mathbb{E}$; also for equal-rank real Satake compactifications that are geometrically rational.

## 5. Principal Obstacles

- **Depth of stratification.** Deligne's $\mathcal{IC}$ is built by iterated truncate-and-push-forward, one step per boundary stratum. In $\mathbb{Q}$-rank $r$ the boundary poset has depth $r$, and each truncation involves $H^{\bullet}(\mathfrak{n}_P;E)$ for a *different* $P$; the compatibility of successive truncations is not a formal consequence of Kostant's theorem. Induction on rank breaks because the "smaller" locally symmetric space $X_P$ is not itself Hermitian in general.
- **$\widehat{X}$ is not algebraic.** No mixed Hodge theory, no decomposition theorem, no weight-monodromy input on the $\widehat{X}$ side; $R\pi_{*}\mathbb{E}$ is not a priori a semisimple perverse object, so the usual decomposition-theorem shortcut is unavailable.
- **Neither side is self-dual for free.** $\mathcal{IC}$ is Verdier self-dual; $R\pi_{*}\mathbb{E}$ is not. Proving a quasi-isomorphism therefore forces one to manufacture self-duality on $\widehat{X}$ — precisely what Saper's $\mathcal{L}$-modules do, at the price of a new category and a micro-support calculus with no off-the-shelf substitute.
- **Analytic methods stop short.** The $L^2$-route (Zucker's conjecture) gives $IH^{\bullet}(X^{*}) \cong H^{\bullet}_{(2)}(X)$, but $L^2$-cohomology has no direct comparison map to $H^{\bullet}(\widehat{X})$: $\widehat{X}$ has no natural complete metric whose $L^2$-complex computes ordinary cohomology.
- **Regularity is essential, not technical.** Singular $\mathbb{E}$ (including the constant sheaf) puts $\mathfrak{n}_P$-weights exactly on the truncation wall, and the theorem genuinely fails.

## 6. The Gap

Two gaps, of different kinds.

1. **Verification gap.** The published account (Astérisque 298, 2005) is an announcement plus a proof modulo the theory developed in *L-modules and micro-support* (arXiv:math/0112251, ~100 pp.), which has not appeared in a refereed journal. No error is known, and the result is used freely; but no independent reproof exists, and the argument has not been reworked in the modern perverse-sheaf/six-functor language, let alone formalized. This is why the catalog status is `solved-recently` rather than closed.
2. **Scope gap.** Beyond the theorem: (i) the case of **singular** $\mathbb{E}$, where the correct replacement for $H^{\bullet}(\widehat{X})$ is unknown in general (weighted cohomology depends on the profile, and the two middle profiles differ); (ii) **integral and torsion coefficients**, where $\mathcal{IC}$ is not self-dual and the comparison is open; (iii) **non-Hermitian $G$**, where $X^{*}$ must be replaced by a Satake compactification and geometric rationality becomes a hypothesis; (iv) full **Hecke-equivariance with explicit boundary terms**, needed for Lefschetz-number applications.

## 7. Current Research (as of June 2026)

- **Reproof in modern language.** Attempts to recover Saper's theorem from the theory of stratified homotopy types and exodromy/six-functor formalisms, replacing $\mathcal{L}$-modules by an explicit constructible-sheaf calculus on $\widehat{X}$ *(frontier — verify)*.
- **Torsion.** Motivated by Scholze's work on torsion in the cohomology of locally symmetric spaces and by Calegari–Emerton's completed-cohomology programme, several groups study $H^{\bullet}(\widehat{X};\mathbb{Z}/p)$ versus $IH^{\bullet}(X^{*};\mathbb{Z}/p)$; the expectation is failure in general, with the discrepancy controlled by the $\mathfrak{n}_P$-cohomology mod $p$ *(frontier — verify)*.
- **Automorphic side.** Continuing Nair's and Franke's identifications, describing $H^{\bullet}(\widehat{X};\mathbb{E})$ Hecke-module-theoretically and matching it with the discrete spectrum (Duke, Johns Hopkins, IAS, Paris/Jussieu, Tata Institute traditions).
- **Fundamental group and $K$-theory of $\widehat{X}$**, following Ji–Murty–Saper–Scherk, as input to Novikov- and Borel-conjecture-type statements for these compactifications.
- **Non-Hermitian analogues.** Saper's equal-rank Satake compactifications; the correct general formulation for arbitrary $G$ remains a live question.

## 8. Future Work

- Publish or independently reprove the micro-support theory; a self-contained account in perverse-sheaf language is the single most-requested item in the field.
- Formulate a corrected statement for singular coefficient systems: identify a canonical complex on $\widehat{X}$ interpolating $\mathbf{W}^{+\mu}$ and $\mathbf{W}^{-\mu}$ whose hypercohomology is $IH^\bullet(X^*)$ for all $\mathbb{E}$.
- Settle the mod-$p$ and integral comparison, at least for $\mathrm{GL}_n$ and $\mathrm{Sp}_{2n}$ of small rank, by explicit computation.
- Extract explicit Lefschetz numbers for Hecke correspondences from the $\widehat{X}$ side, completing the Goresky–Kottwitz–MacPherson programme relating boundary contributions to weighted orbital integrals.
- Machine-checkable computations of both sides for small $\mathbb{Q}$-rank cases as regression tests for any new proof.

## 9. Key References

- **[Foundational]** M. Goresky, R. MacPherson. *Intersection homology theory.* Topology 19 (1980), 135–162.
- **[Foundational]** M. Goresky, R. MacPherson. *Intersection homology II.* Inventiones Mathematicae 72 (1983), 77–129.
- **[Foundational]** A. Borel, J.-P. Serre. *Corners and arithmetic groups.* Commentarii Mathematici Helvetici 48 (1973), 436–491.
- **[Foundational]** W. Baily, A. Borel. *Compactification of arithmetic quotients of bounded symmetric domains.* Annals of Mathematics 84 (1966), 442–528.
- **[Origin]** M. Rapoport. *On the shape of the contribution of a fixed point on the boundary: the case of $\mathbb{Q}$-rank one* (with an appendix by L. Saper and M. Stern), in *The Zeta Functions of Picard Modular Surfaces*, R. Langlands and D. Ramakrishnan (eds.), CRM, Montréal, 1992, 479–488.
- **[Structural]** M. Goresky, G. Harder, R. MacPherson. *Weighted cohomology.* Inventiones Mathematicae 116 (1994), 139–213.
- **[Related]** S. Zucker. *$L_2$ cohomology of warped products and arithmetic groups.* Inventiones Mathematicae 70 (1982), 169–218.
- **[Related]** E. Looijenga. *$L^2$-cohomology of locally symmetric varieties.* Compositio Mathematica 67 (1988), 3–20.
- **[Related]** L. Saper, M. Stern. *$L^2$-cohomology of arithmetic varieties.* Annals of Mathematics 132 (1990), 1–69.
- **[SOTA]** L. Saper. *$\mathcal{L}$-modules and the conjecture of Rapoport and Goresky–MacPherson.* Astérisque 298 (2005), 319–334 (Automorphic Forms I).
- **[SOTA]** L. Saper. *$\mathcal{L}$-modules and micro-support.* Preprint, arXiv:math/0112251.
- **[SOTA]** A. Nair. *Weighted cohomology of arithmetic groups.* Annals of Mathematics 150 (1999), 1–31.
- **[Survey]** A. Borel, L. Ji. *Compactifications of Symmetric and Locally Symmetric Spaces.* Birkhäuser, 2006.
- **[Survey]** F. Hirzebruch. *Hilbert modular surfaces.* L'Enseignement Mathématique 19 (1973), 183–281.

## 10. Worked Example / Concrete Special Case

**Why regularity is needed: a Hilbert modular surface with constant coefficients.**

Take $F$ real quadratic with class number one and $b_1$ of the smooth compactification equal to $0$ (e.g. $F = \mathbb{Q}(\sqrt{5})$), $\Gamma \subset \mathrm{SL}_2(\mathcal{O}_F)$ neat of finite index, $Y = \Gamma\backslash\mathbb{H}^2$, $n = \dim_{\mathbb{C}} = 2$, with $c$ cusps. Here every proper parabolic is a Borel, $M_P$ is anisotropic, so $X_P$ is a point and
$$
\widehat{X} \;=\; X^{*} \;=\; Y \sqcup \{c \text{ points}\}.
$$
So for $\mathbb{E} = \mathbb{Q}$ the conjecture reads $H^{\bullet}(X^{*};\mathbb{Q}) \cong IH^{\bullet}(X^{*};\mathbb{Q})$. Compute both.

*Cusp link.* Each cusp has link $L_i = \Gamma_{P_i}\backslash(N_{P_i}A_{P_i}\text{-orbit})$, a $T^2$-bundle over $S^1$ with hyperbolic monodromy $A \in \mathrm{SL}_2(\mathbb{Z})$ (a totally positive unit acting on $\mathcal{O}_F$). Since $\det(A - I) \ne 0$, $H^{1}(T^2)^{A} = 0$, and the Wang sequence gives
$$
b_0(L_i)=1,\quad b_1(L_i)=1,\quad b_2(L_i)=1,\quad b_3(L_i)=1 .
$$

*Intersection cohomology.* Isolated singularities, $n=2$, so the cone formula gives
$$
IH^{k}(X^{*}) = \begin{cases} H^{k}(Y), & k \le 1,\\[2pt] \operatorname{im}\!\big(H^{2}_{c}(Y) \to H^{2}(Y)\big), & k = 2,\\[2pt] H^{k}_{c}(Y), & k \ge 3.\end{cases}
$$

*Ordinary cohomology.* Excising the cone points, $H^{k}(X^{*},\Sigma) \cong H^{k}(Y,\partial Y) \cong H^{k}_{c}(Y)$, and $H^{k}(\Sigma)=0$ for $k \ge 1$, so
$$
H^{k}(X^{*}) \cong H^{k}_{c}(Y) \quad (k \ge 2).
$$

*The discrepancy.* From the long exact sequence of the pair,
$$
\ker\!\big(H^{2}_{c}(Y)\to H^{2}(Y)\big) \;=\; \operatorname{coker}\!\Big(H^{1}(Y) \to \textstyle\bigoplus_i H^{1}(L_i)\Big).
$$
Let $\widetilde{Y}$ be Hirzebruch's smooth compactification, each cusp resolved by a cycle of $k_i$ rational curves. Since the exceptional intersection matrix is negative definite, the residue map $H^{0}(\widetilde{D})(-1) \to H^{2}(\widetilde{Y})$ is injective, and with $H^{1}(\widetilde{Y};\mathbb{Q})=0$ the mixed Hodge sequence forces $H^{1}(Y;\mathbb{Q}) = 0$. Hence
$$
\dim H^{2}(X^{*};\mathbb{Q}) - \dim IH^{2}(X^{*};\mathbb{Q}) \;=\; \sum_{i=1}^{c} b_1(L_i) \;=\; c \;>\; 0 .
$$
Geometrically: collapsing the exceptional *cycle* $C_i \subset \widetilde{Y}$ contributes $H^{1}(C_i)=\mathbb{Q}$ (the loop of the cycle) to $H^{2}(X^{*})$, and $IH^{2}$ discards exactly that class. For $F=\mathbb{Q}(\sqrt5)$ and $\Gamma$ with one cusp, the gap is one dimension.

*With regular coefficients.* Replace $\mathbb{Q}$ by $\mathbb{E}_{(a,b)}$, $\mathrm{Sym}^{a}\boxtimes\mathrm{Sym}^{b}$ with $a,b \ge 1$. The cusp contribution is $H^{\bullet}(\mathfrak{n}_P;E)$, whose Kostant weights are $\lambda$ and $w_0(\lambda+\rho)-\rho$; regularity ($a,b\ge1$) puts both strictly off the middle wall, so the boundary classes that produced the $c$-dimensional excess above have nonzero $A_P$-weight and are killed by $\Gamma_{A_P}$-invariance. Both sides then agree in every degree — the conjecture, verified by hand in $\mathbb{Q}$-rank $1$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*