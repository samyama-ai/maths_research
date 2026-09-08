---
id: 03-geometry/bass-quillen-conjecture
title: "Bass-Quillen Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bass-Quillen Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/bass-quillen-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Bass–Quillen).** Let $R$ be a regular Noetherian ring. Then every finitely generated projective module over the polynomial ring $R[x_1,\dots,x_n]$ is *extended* from $R$: there exists a finitely generated projective $R$-module $P_0$ with
$$P \;\cong\; P_0 \otimes_R R[x_1,\dots,x_n].$$

Geometrically: every algebraic vector bundle on $\mathbb{A}^n_X = X \times \mathbb{A}^n$, for $X = \operatorname{Spec} R$ a regular affine scheme, is pulled back along the projection $\mathbb{A}^n_X \to X$. Equivalently, vector bundles on regular affine schemes are $\mathbb{A}^1$-invariant.

The case $R = k$ a field is the Quillen–Suslin theorem (Serre's problem), so the conjecture is a relative, base-changed strengthening of it. Regularity is essential: the statement fails for singular $R$ already in rank $1$ (Section 10). A complete solution requires either a proof for all regular Noetherian $R$ and all $n$, or a single regular ring $R$, integer $n$, and non-extended projective $R[x_1,\dots,x_n]$-module.

The conjecture is open. The principal remaining case is **regular local rings of mixed characteristic that are not ind-smooth over a Dedekind base** — in particular ramified ones.

## 2. Mathematical Foundations

**Extension.** For a ring map $R \to A$ and $P$ f.g. projective over $A$, $P$ is *extended from $R$* if $P \cong P_0 \otimes_R A$ for some f.g. projective $P_0$. Write $\mathrm{BQ}_n(R)$ for the assertion that all f.g. projectives over $R[x_1,\dots,x_n]$ are extended.

**Regularity.** $R$ Noetherian is regular if $R_\mathfrak{p}$ has finite global dimension for all primes $\mathfrak{p}$; equivalently $\dim_{\kappa(\mathfrak p)} \mathfrak{p}R_\mathfrak{p}/\mathfrak{p}^2R_\mathfrak{p} = \dim R_\mathfrak{p}$. Regularity is stable under polynomial extension, so $R[x_1,\dots,x_n]$ is regular too.

**Quillen's local-global principle.** For $P$ f.g. projective over $R[x]$, the set
$$J(P) \;=\; \{\, f \in R \;:\; P_f \text{ is extended from } R_f \,\}$$
is an ideal of $R$. Hence $P$ is extended iff $P_\mathfrak{m}$ is extended from $R_\mathfrak{m}$ for every maximal ideal $\mathfrak{m}$. So $\mathrm{BQ}_n$ reduces to $R$ **regular local**.

**Horrocks' theorem.** If $(R,\mathfrak m)$ is local and $P$ is f.g. projective over $R[x]$ with $P_f$ free for some *monic* $f \in R[x]$, then $P$ is free. This is the engine driving all known cases: one arranges a monic polynomial in the support of non-freeness.

**Roitman's reduction.** $\mathrm{BQ}_1(R) \Rightarrow \mathrm{BQ}_n(R)$ for all $n$, for $R$ Noetherian of finite Krull dimension (Roitman 1979). Thus the conjecture is the single-variable statement.

**Lindel's étale neighbourhood.** For $(R,\mathfrak m)$ regular local, essentially of finite type over a field $k$, with $R/\mathfrak m$ separable over $k$ and $d = \dim R$, there is a regular local $k$-algebra $(A,\mathfrak n)$ essentially of finite type, an element $f \in A$, and an étale map
$$A \longrightarrow R \quad\text{with}\quad A_f \to R_f \ \text{étale}, \qquad A/fA \;\xrightarrow{\ \sim\ }\; R/fR ,$$
where $f$ is part of a regular system of parameters. The pair $(A \to R, f)$ is a *Lindel pair*; it lets one transport a projective module to a situation where Horrocks applies after a change of variables making the relevant polynomial monic.

**Torsor formulation.** $\mathrm{BQ}_n$ for rank-$r$ bundles is the statement
$$H^1_{\mathrm{Zar}}\big(\mathbb{A}^n_R, GL_r\big) \;=\; H^1_{\mathrm{Zar}}(R, GL_r),$$
a special case of the expectation that $G$-torsors over $\mathbb{A}^n_R$ are extended for reductive $G$ — closely tied to the Grothendieck–Serre conjecture: for $R$ regular local with fraction field $K$ and $G$ reductive over $R$,
$$\ker\!\big(H^1_{\text{ét}}(R,G) \to H^1_{\text{ét}}(K,G)\big) \;=\; \{*\}.$$

## 3. History & State of the Art (SOTA)

- **1955.** Serre asks whether f.g. projective modules over $k[x_1,\dots,x_n]$ are free.
- **1973.** Bass, in *Some problems in "classical" algebraic K-theory* (LNM 342), poses the relative question for regular $R$ — the origin of the conjecture.
- **1976.** Quillen and, independently, Suslin prove Serre's problem. Quillen's proof introduces the local-global patching principle and reproves Horrocks' theorem; this is precisely the machinery that makes the relative question tractable and prompts Quillen to record it as a question.
- **1979.** Roitman reduces $n$ variables to one.
- **1981.** Lindel proves the conjecture for $R$ regular local essentially of finite type over a field, via the étale-neighbourhood technique. This remains the single deepest input.
- **1983–84.** Plumstead, then Bhatwadekar–Roy, prove unimodular-element and cancellation results for projectives over $R[x_1,\dots,x_n]$ of rank $> \dim R$, without regularity.
- **1986–89.** Popescu's general Néron desingularization: a regular homomorphism of Noetherian rings is a filtered colimit of smooth ones. Combined with Lindel, this yields the conjecture for **all regular local rings containing a field**. Swan's 1998 survey gives a complete, corrected account.
- **2015.** Fedorov–Panin prove Grothendieck–Serre for regular local rings containing an infinite field, giving the torsor-theoretic analogue in equal characteristic.
- **2018–2020.** Asok–Hoyois–Wendt place the conjecture inside $\mathbb{A}^1$-homotopy theory: affine representability of $BGL_r$ over a base makes $\mathrm{BQ}$ equivalent to a homotopy-invariance statement.
- **2022.** Česnavičius's problem list *Problems about torsors over regular rings* records the mixed-characteristic case as the live frontier and proves Grothendieck–Serre in the quasi-split unramified case.

## 4. Partial Results / Verified Cases

Confirmed:

1. **$R$ a field or a PID** (Quillen–Suslin, 1976): all $n$, all ranks; modules are free.
2. **$\dim R \le 2$**, $R$ regular: known classically (see Lam, *Serre's Problem on Projective Modules*, Ch. V).
3. **$R$ regular local, essentially of finite type over a field $k$, residue field separable over $k$** (Lindel 1981): all $n$, all ranks.
4. **$R$ regular local containing a field** (Lindel + Popescu desingularization; Swan 1998): all $n$, all ranks. This covers all equal-characteristic regular rings, including complete ones and rings of formal power series $k[[t_1,\dots,t_d]]$.
5. **Rank $> \dim R$** (Plumstead 1983; Bhatwadekar–Roy 1984): projectives over $R[x_1,\dots,x_n]$ of rank exceeding $\dim R$ contain unimodular elements and are cancellative — no regularity needed. Combined with (2)–(4), low-rank cases are the hard ones.
6. **Rank $1$**: $\operatorname{Pic}(R[x_1,\dots,x_n]) = \operatorname{Pic}(R)$ holds for all *seminormal* reduced $R$ (Traverso 1970, Swan), hence for all regular $R$.
7. **Monoid rings**: Gubeladze (1988) proved that projectives over $k[M]$ are free for $M$ a seminormal commutative cancellative torsion-free monoid — a wide generalization of the $n$-variable case.
8. **$R$ ind-smooth over a Dedekind ring** with the required separability of residue fields: reduces to Lindel's argument over the base.

## 5. Principal Obstacles

- **Lindel's method is intrinsically geometric over a field.** The étale-neighbourhood construction needs a base field to produce a smooth algebra $A$ with a controlled hypersurface $f$; over $\mathbb{Z}_p$ or a ramified extension there is no such "affine coordinate" to write down. Absolute constructions over $\mathbb{Z}$ are obstructed by ramification.
- **Popescu's theorem does not apply in the ramified case.** A ramified regular local ring of mixed characteristic (e.g. $\mathbb{Z}_p[[t]]/(p - t^2)$-type situations, or $W(k)[t]$ localized at a ramified prime) is not ind-smooth over any Dedekind subring in the required sense, so the colimit trick that converts Lindel into the general equal-characteristic statement fails.
- **Horrocks needs monicity.** Making a polynomial monic after a change of variables is a "generic coordinates" move that requires infinite residue fields or clever tricks; finite residue fields cause genuine trouble (handled ad hoc by Asok–Hoyois–Wendt III in the smooth case).
- **No cohomological obstruction theory of the right shape.** Vector bundles on $\mathbb{A}^n_R$ are classified by Zariski $H^1(GL_r)$, which is not a cohomology theory with long exact sequences; $\mathbb{A}^1$-homotopy provides one but only after knowing affine representability, which itself currently needs a nice base.
- **Low rank is where the obstruction lives.** All stable/rank-large statements are theorems (Plumstead, Bass); the unstable range $2 \le r \le \dim R$ has no available surgery.

## 6. The Gap

Everything hinges on one implication. Known:
$$R \text{ regular local, } R \supseteq \text{a field} \;\Longrightarrow\; \mathrm{BQ}_1(R).$$
Wanted:
$$R \text{ regular local, mixed characteristic } (0,p) \;\Longrightarrow\; \mathrm{BQ}_1(R).$$
The unramified case ($p \notin \mathfrak{m}^2$) is close to reach: it is ind-smooth over an unramified DVR and a Popescu-type desingularization over an excellent DVR is available, but the Lindel transport step still requires separability hypotheses on residue fields that are not automatic. The **ramified** case ($p \in \mathfrak{m}^2$) has no known route at all: one needs a substitute for the étale neighbourhood $(A \to R, f)$ constructed purely from the arithmetic of $R$, or a proof of $\mathbb{A}^1$-invariance of $H^1_{\mathrm{Zar}}(-,GL_r)$ that never leaves $R$. Prismatic and perfectoid techniques are the candidate replacement, but no one has produced the required descent statement for $GL_r$-torsors on $\mathbb{A}^1_R$.

## 7. Current Research (as of June 2026)

- **Mixed-characteristic Grothendieck–Serre.** Česnavičius (Orsay/Paris-Saclay) and collaborators continue to push the unramified and quasi-split cases; a full mixed-characteristic Grothendieck–Serre would very likely deliver Bass–Quillen in the unramified case *(frontier — verify)*.
- **$\mathbb{A}^1$-homotopy.** Asok (USC), Hoyois (Regensburg), Wendt (Wuppertal): affine representability and obstruction-theoretic computation of $[X, BGL_r]_{\mathbb{A}^1}$; the program reduces Bass–Quillen over a base $S$ to $S$-affine representability plus $\mathbb{A}^1$-invariance of $\mathrm{Sing}^{\mathbb{A}^1} GL_r$.
- **Prismatic / $p$-adic descent.** Attempts to import Bhatt–Scholze-style descent to prove ramified desingularization statements; no complete BQ application yet *(frontier — verify)*.
- **Non-Noetherian and valuation-ring bases.** Extension of BQ-type statements to valuation rings and perfectoid rings, where "regular" must be replaced by weak/coherent regularity.
- **Explicit algorithms.** Constructive Quillen–Suslin (Fabiańska–Quadrat, Lombardi–Yengui) continues, giving effective versions in the solved cases.

## 8. Future Work

1. Construct a Lindel pair over an excellent DVR without residue-field separability — the direct route to the unramified case.
2. Prove Grothendieck–Serre for ramified regular local rings; then deduce BQ for $GL_r$ as the split case.
3. Establish $\mathbb{A}^1$-representability of vector bundles over $\operatorname{Spec} \mathbb{Z}_p$ and mixed-characteristic bases, then run obstruction theory rank by rank.
4. Attack rank $2$ over $3$-dimensional ramified regular local rings as a test case; a counterexample, if one exists, should live here.
5. Extend Gubeladze's monoid-ring techniques, which are combinatorial and characteristic-free, to detect extendedness over arithmetic bases.

## 9. Key References

- **[Foundational]** H. Bass. *Some problems in "classical" algebraic K-theory.* In Algebraic K-Theory II, Lecture Notes in Math. 342, Springer, 1973. [DOI](https://doi.org/10.1007/bfb0073718)
- **[Foundational]** D. Quillen. *Projective modules over polynomial rings.* Inventiones Mathematicae 36 (1976), 167–171.
- **[Foundational]** A. A. Suslin. *Projective modules over polynomial rings are free.* Doklady Akademii Nauk SSSR 229 (1976), 1063–1066.
- **[Foundational]** G. Horrocks. *Projective modules over an extension of a local ring.* Proceedings of the London Mathematical Society (3) 14 (1964), 714–718. [DOI](https://doi.org/10.1112/plms/s3-14.4.714)
- **[Key case]** H. Lindel. *On the Bass–Quillen conjecture concerning projective modules over polynomial rings.* Inventiones Mathematicae 65 (1981), 319–323. [DOI](https://doi.org/10.1007/bf01389017)
- **[Key case]** M. Roitman. *On projective modules over polynomial rings.* Journal of Algebra 58 (1979), 51–63.
- **[Key case]** D. Popescu. *General Néron desingularization and approximation.* Nagoya Mathematical Journal 104 (1986), 85–115. [DOI](https://doi.org/10.1017/s0027763000022698)
- **[Survey]** R. G. Swan. *Néron–Popescu desingularization.* In Algebra and Geometry (Taipei 1995), Lectures in Algebra and Geometry 2, International Press, 1998, 135–192.
- **[Survey]** T. Y. Lam. *Serre's Problem on Projective Modules.* Springer Monographs in Mathematics, Springer, 2006. [DOI](https://doi.org/10.1007/978-3-540-34575-6)
- **[Related]** B. Plumstead. *The conjectures of Eisenbud and Evans.* American Journal of Mathematics 105 (1983), 1417–1433. [DOI](https://doi.org/10.2307/2374448)
- **[Related]** S. M. Bhatwadekar, A. Roy. *Some theorems about projective modules over polynomial rings.* Journal of Algebra 86 (1984), 150–158. [DOI](https://doi.org/10.1016/0021-8693(84)90061-9)
- **[Related]** J. Gubeladze. *Anderson's conjecture and the maximal monoid class over which projective modules are free.* Matematicheskii Sbornik 135 (1988), 169–185. [DOI](https://doi.org/10.1070/sm1989v063n01abeh003266)
- **[Related]** C. Traverso. *Seminormality and Picard group.* Annali della Scuola Normale Superiore di Pisa 24 (1970), 585–595.
- **[SOTA]** R. Fedorov, I. Panin. *A proof of the Grothendieck–Serre conjecture on principal bundles over regular local rings containing infinite fields.* Publications Mathématiques de l'IHÉS 122 (2015), 169–193. [DOI](https://doi.org/10.1007/s10240-015-0075-z)
- **[SOTA]** A. Asok, M. Hoyois, M. Wendt. *Affine representability results in $\mathbb{A}^1$-homotopy theory II: principal bundles and homogeneous spaces.* Geometry & Topology 22 (2018), 1181–1225. [DOI](https://doi.org/10.2140/gt.2018.22.1181)
- **[SOTA]** A. Asok, M. Hoyois, M. Wendt. *Affine representability results in $\mathbb{A}^1$-homotopy theory III: finite fields and complements.* Algebraic Geometry 7 (2020), 634–644. [DOI](https://doi.org/10.14231/ag-2020-023)
- **[SOTA / Survey]** K. Česnavičius. *Problems about torsors over regular rings.* Acta Mathematica Vietnamica 47 (2022), 39–107. [DOI](https://doi.org/10.1007/s40306-022-00477-y)
- **[SOTA]** K. Česnavičius. *Grothendieck–Serre in the quasi-split unramified case.* Forum of Mathematics, Pi 10 (2022), e9. [DOI](https://doi.org/10.1017/fmp.2022.5)

## 10. Worked Example / Concrete Special Case

**Why regularity is indispensable: the cusp.** Let $k$ be a field of characteristic $0$ and
$$R \;=\; k[t^2,t^3] \;\cong\; k[u,v]/(v^2-u^3), \qquad \widetilde{R} = k[t].$$
$R$ is a one-dimensional domain, singular at the origin. The conductor is $\mathfrak{c} = (t^2,t^3)\widetilde R = t^2 k[t] \subset R$, giving the Milnor square
$$\begin{array}{ccc} R & \to & k[t] \\ \downarrow & & \downarrow \\ R/\mathfrak c \cong k & \to & k[t]/(t^2) \end{array}$$
Milnor patching glues a rank-1 module from $R$-free data on the two upper corners along a unit of $k[t]/(t^2)$. Since $\operatorname{Pic}(k[t]) = 0$ and $\operatorname{Pic}(k)=0$,
$$\operatorname{Pic}(R) \;\cong\; \frac{\big(k[t]/(t^2)\big)^\times}{\ \mathrm{im}\, k^\times \cdot \mathrm{im}\, k[t]^\times\ } \;\cong\; \{1+\lambda t\} \;\cong\; (k,+).$$
So $L_\lambda$, glued by the unit $1+\lambda t$, is a nontrivial line bundle for $\lambda \ne 0$.

Now do the same over $R[x]$. The conductor square base-changes to $R[x] \to k[x][t]$, $k[x] \to k[x][t]/(t^2)$, and $\operatorname{Pic}(k[x][t]) = 0$, so the identical computation gives
$$\operatorname{Pic}(R[x]) \;\cong\; \{1 + g(x)t : g \in k[x]\} \;\cong\; (k[x],+).$$
Take $g(x) = x$: the line bundle $L_x$ glued by the unit $1 + xt \in (k[x][t]/(t^2))^\times$ is a rank-1 projective $R[x]$-module. It is **not extended**: extended line bundles are exactly those with $g$ constant, i.e. the image of $\operatorname{Pic}(R) \cong k \hookrightarrow k[x] \cong \operatorname{Pic}(R[x])$. Concretely, restricting $L_x$ at $x=0$ gives $\mathcal{O}$ but at $x=1$ gives $L_1 \not\cong \mathcal{O}$, so no single $P_0$ can produce it.

**Contrast, the regular case.** Replace $R$ by its normalization $\widetilde R = k[t]$, a PID, hence regular. Then $\widetilde R[x] = k[t,x]$ and Quillen–Suslin gives: every f.g. projective is free, so extended from $\widetilde R$. The failure above is exactly the failure of seminormality at the cusp; Traverso's theorem says $\operatorname{Pic}(R[x]) = \operatorname{Pic}(R)$ precisely when $R_{\mathrm{red}}$ is seminormal, and regular rings are normal hence seminormal.

**The open shape of the problem.** Now let $R = \mathbb{Z}_p[[t]]/(f)$ be a ramified regular local ring of mixed characteristic and dimension $2$, and let $P$ be a rank-$2$ projective over $R[x]$. Quillen patching already reduces to this local situation; Horrocks applies if $P_g$ is free for some monic $g \in R[x]$. Producing such a $g$ is precisely what Lindel's étale neighbourhood does when $R$ contains a field — and precisely what nobody knows how to do here.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*