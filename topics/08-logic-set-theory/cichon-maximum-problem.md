---
id: 08-logic-set-theory/cichon-maximum-problem
title: "Cichoń's Maximum Problem"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cichoń's Maximum Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/cichon-maximum-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Cichoń's maximum** asks whether all cardinal characteristics appearing in Cichoń's diagram can be pairwise different in a single model of ZFC:

> Is it consistent with ZFC that the ten values
> $$\aleph_1,\ \mathrm{add}(\mathcal N),\ \mathrm{cov}(\mathcal N),\ \mathfrak b,\ \mathrm{non}(\mathcal M),\ \mathrm{cov}(\mathcal M),\ \mathfrak d,\ \mathrm{non}(\mathcal N),\ \mathrm{cof}(\mathcal N),\ \mathfrak c$$
> are pairwise distinct?

Here $\mathcal M$ is the $\sigma$-ideal of meager subsets of $\mathbb R$ and $\mathcal N$ the $\sigma$-ideal of Lebesgue-null sets. The two remaining entries of the diagram, $\mathrm{add}(\mathcal M)$ and $\mathrm{cof}(\mathcal M)$, are excluded because ZFC proves them equal to $\min(\mathfrak b,\mathrm{cov}(\mathcal M))$ and $\max(\mathfrak d,\mathrm{non}(\mathcal M))$ respectively, so they can never be separated from all the others.

A complete solution means: exhibit a forcing extension (or inner-model argument) of a model of ZFC in which the ten values are pairwise different, with an explicit assignment of alephs, and with the consistency strength being that of ZFC alone. The **answer is yes**: Goldstern–Kellner–Shelah (2019) from four strongly compact cardinals, and Goldstern–Kellner–Mejía–Shelah (2022) from ZFC alone. The residual open problems concern *which* orderings and *which* values of $\mathfrak c$ are attainable, and how far the separation extends beyond the ten classical entries.

## 2. Mathematical Foundations

For a $\sigma$-ideal $\mathcal I$ on $\mathbb R$ containing singletons with $\bigcup\mathcal I=\mathbb R$:

$$\mathrm{add}(\mathcal I)=\min\{|A| : A\subseteq\mathcal I,\ \textstyle\bigcup A\notin\mathcal I\},\qquad \mathrm{cov}(\mathcal I)=\min\{|A| : A\subseteq\mathcal I,\ \textstyle\bigcup A=\mathbb R\},$$
$$\mathrm{non}(\mathcal I)=\min\{|X| : X\subseteq\mathbb R,\ X\notin\mathcal I\},\qquad \mathrm{cof}(\mathcal I)=\min\{|A| : A\subseteq \mathcal I\ \text{cofinal in }(\mathcal I,\subseteq)\}.$$

For $f,g\in\omega^\omega$ write $f\le^* g$ iff $f(n)\le g(n)$ for all but finitely many $n$. Then
$$\mathfrak b=\min\{|F| : F\subseteq\omega^\omega \text{ unbounded in } \le^*\},\qquad \mathfrak d=\min\{|F| : F \text{ dominating in } \le^*\}.$$

**Cichoń's diagram** (arrows denote ZFC-provable $\le$):

$$
\begin{array}{ccccccc}
\mathrm{cov}(\mathcal N) & \to & \mathrm{non}(\mathcal M) & \to & \mathrm{cof}(\mathcal M) & \to & \mathrm{cof}(\mathcal N)\\
\uparrow & & \uparrow & & \uparrow & & \uparrow\\
& & \mathfrak b & \to & \mathfrak d & & \\
\uparrow & & \uparrow & & \uparrow & & \uparrow\\
\mathrm{add}(\mathcal N) & \to & \mathrm{add}(\mathcal M) & \to & \mathrm{cov}(\mathcal M) & \to & \mathrm{non}(\mathcal N)
\end{array}
$$

with $\aleph_1\le\mathrm{add}(\mathcal N)$ and $\mathrm{cof}(\mathcal N)\le\mathfrak c$.

Two ZFC theorems constrain everything:

- **Rothberger:** $\mathrm{cov}(\mathcal M)\le\mathrm{non}(\mathcal N)$ and $\mathrm{cov}(\mathcal N)\le\mathrm{non}(\mathcal M)$.
- **Miller–Truss (Bartoszyński–Judah form):** $\mathrm{add}(\mathcal M)=\min(\mathfrak b,\mathrm{cov}(\mathcal M))$ and $\mathrm{cof}(\mathcal M)=\max(\mathfrak d,\mathrm{non}(\mathcal M))$.
- **Bartoszyński characterisations:** $\mathrm{add}(\mathcal N)$ and $\mathrm{cof}(\mathcal N)$ are the additivity/cofinality of the *localisation* relation: $\mathrm{cof}(\mathcal N)=\mathfrak d(\sqsubseteq)$ where $x\sqsubseteq S$ iff $\forall^\infty n\,(x(n)\in S(n))$ for slaloms $S$ with $|S(n)|\le n$.

The diagram is a *complete* description of the provable inequalities in the following sense: the ten values are pairwise distinct in some model iff no ZFC theorem forbids it, and Cichoń's maximum asserts that the maximal number of distinct values, namely $10$, is attained. Since the ten values must be $10$ distinct cardinals $\ge\aleph_1$, necessarily $\mathfrak c\ge\aleph_{10}$ in any linear assignment starting at $\aleph_1$.

## 3. History & State of the Art (SOTA)

- **1984–1990.** Cichoń, Fremlin, Bartoszyński, Miller, Truss and Raisonnier–Stern assemble the diagram and prove its ZFC inequalities; Bartoszyński–Judah's *Set Theory: On the Structure of the Real Line* (1995) codifies it.
- **1991.** Brendle ("Larger cardinals in Cichoń's diagram") separates several entries simultaneously, with the continuum large.
- **2013.** Mejía introduces *matrix iterations* (two-dimensional finite-support systems) and separates the left-hand and right-hand halves in constellations of up to seven values.
- **2016.** Goldstern–Mejía–Shelah, "The left side of Cichoń's diagram", separate $\aleph_1<\mathrm{add}(\mathcal N)<\mathrm{cov}(\mathcal N)<\mathfrak b<\mathrm{non}(\mathcal M)<\mathrm{cov}(\mathcal M)\le\mathfrak c$ — the maximal known fragment before the full result.
- **2019 (the breakthrough).** Goldstern, Kellner and Shelah, *Cichoń's maximum*, Annals of Mathematics 190 (2019), 113–143: from four strongly compact cardinals they force
 $$\aleph_1<\mathrm{add}(\mathcal N)<\mathrm{cov}(\mathcal N)<\mathfrak b<\mathrm{non}(\mathcal M)<\mathrm{cov}(\mathcal M)<\mathfrak d<\mathrm{non}(\mathcal N)<\mathrm{cof}(\mathcal N)<\mathfrak c.$$
 The technique: build a finite-support ccc iteration separating the left side, then apply **Boolean ultrapowers** along ultrafilters on the compacts to "blow up" the right side while preserving the left.
- **2019.** Kellner–Shelah–Tănasie obtain a genuinely different ordering of the same ten values, showing the result is not tied to one constellation.
- **2022 (large cardinals eliminated).** Goldstern, Kellner, Mejía and Shelah, *Cichoń's maximum without large cardinals*, J. Eur. Math. Soc. 24 (2022): a finite-support iteration with **ultrafilter limits** (a submodel/limit technique that keeps $\mathrm{non}(\mathcal M)$ small along cofinally many coordinates) replaces the Boolean ultrapower. Consistency strength: ZFC.

## 4. Partial Results / Verified Cases

| Fragment / parameter regime | Status |
|---|---|
| Any $\le 7$ of the ten values pairwise distinct | Known since Brendle (1991), Mejía (2013) via matrix iterations, no large cardinals |
| Left side: $\aleph_1<\mathrm{add}(\mathcal N)<\mathrm{cov}(\mathcal N)<\mathfrak b<\mathrm{non}(\mathcal M)<\mathrm{cov}(\mathcal M)<\mathfrak c$ (7 values) | Goldstern–Mejía–Shelah 2016, ZFC only |
| All 10 values, one specific increasing order, $\mathfrak c$ large | GKS 2019, from 4 strongly compacts |
| A second, incomparable ordering of all 10 | Kellner–Shelah–Tănasie 2019 |
| All 10 values, ZFC-only consistency strength | GKMS 2022 |
| $\mathfrak c$ of countable cofinality / singular $\mathfrak c$ variants | Partially handled; ccc finite-support iterations give $\mathrm{cf}(\mathfrak c)>\omega$ in the standard constructions |
| $\mathfrak c$ exactly $\aleph_{10}$ (the provable minimum for a linear constellation) | Achieved in the ZFC-only line of work; the analogous question for *every* admissible ordering is not settled *(frontier — verify)* |
| Cichoń's maximum plus an 11th characteristic (evasion number $\mathfrak e$, uniformity of strong measure zero, Yorioka-ideal invariants) | Several extensions by Cardona–Mejía and coauthors, 2022–2024 |

## 5. Principal Obstacles

- **Finite-support ccc iterations add Cohen reals cofinally.** Any FS iteration of length $\delta$ with $\mathrm{cf}(\delta)>\omega$ forces $\mathrm{cov}(\mathcal M)\ge\mathrm{cf}(\delta)$ and $\mathrm{non}(\mathcal M)=\aleph_1$-ish behaviour; this pins two entries together and destroys attempts to make $\mathrm{non}(\mathcal M)$ large *and* $\mathrm{cov}(\mathcal M)$ larger still.
- **Countable-support iterations of proper forcing force $\mathfrak c\le\aleph_2$**, so at most three distinct values can appear. The whole "$\le\aleph_2$ technology" of Shelah's *Proper Forcing* is unusable here.
- **Preservation theory is asymmetric.** Tools for keeping a characteristic *small* (preservation of "$\sqsubseteq$-unbounded" families, $\mathcal I$-linkedness, Suslin ccc preservation) work smoothly on the left half of the diagram; making the *right* half — $\mathfrak d$, $\mathrm{non}(\mathcal N)$, $\mathrm{cof}(\mathcal N)$ — take three distinct large values requires simultaneously *not* adding certain reals, which conflicts with the ccc-FS setting.
- **Duality.** The diagram has an order-reversing symmetry (Galois–Tukey duality) exchanging $\mathrm{add}\leftrightarrow\mathrm{cof}$, $\mathrm{cov}\leftrightarrow\mathrm{non}$, $\mathfrak b\leftrightarrow\mathfrak d$, but *no* forcing construction is self-dual: one cannot simply dualise a left-side model to get the right side.
- **Large-cardinal cost.** The Boolean-ultrapower fix (GKS 2019) is elegant but each ultrapower step consumed one strongly compact; removing them (GKMS 2022) required inventing ultrafilter-limit iterations, a genuinely new preservation mechanism rather than a refinement.

## 6. The Gap

The gap that was crossed in 2019–2022 was precisely: *how to make the four right-side values $\mathfrak d<\mathrm{non}(\mathcal N)<\mathrm{cof}(\mathcal N)<\mathfrak c$ distinct without collapsing the already-separated left side.* FS iterations control the left side; the right side needs "$\mathrm{non}(\mathcal M)$ stays small along a cofinal set of stages", which no classical ccc preservation theorem delivers. Boolean ultrapowers (2019) and ultrafilter limits (2022) each supply exactly this.

The gap that **remains**: the constructions realise particular constellations. It is not known whether *every* assignment of ten distinct alephs consistent with the diagram's partial order (and with the Miller–Truss identities and known cofinality restrictions such as $\mathrm{cf}(\mathrm{add}(\mathcal N))\ge\aleph_1$, $\mathrm{cf}(\mathfrak b)=\mathfrak b$) is forceable, nor whether the minimal continuum $\mathfrak c=\aleph_{10}$ is achievable for all of them.

## 7. Current Research (as of June 2026)

- **Vienna (TU Wien: Goldstern, Kellner) and Shizuoka (Mejía), with Shelah (HUJI).** Systematic mapping of which "constellations" of Cichoń's diagram are forceable, using filter-linkedness and Tukey-order arguments (Brendle–Cardona–Mejía, *Filter-linkedness and its effect on preservation of cardinal characteristics*, APAL 2022).
- **Beyond the ten entries.** Cardona and Mejía have added the evasion number and uniformity/covering numbers of the strong-measure-zero and Yorioka ideals to a maximal-separation model, pushing to 11–13 simultaneously distinct values *(frontier — verify exact counts)*.
- **Higher analogues.** "Cichoń's maximum at $\kappa$" for $\kappa$ inaccessible or measurable — the generalised Baire space $\kappa^\kappa$ version, where even the diagram's ZFC inequalities differ *(frontier — verify)*.
- **Non-ccc and no-new-reals routes.** GKMS, *Controlling cardinal characteristics without adding reals* (J. Math. Logic 21, 2021), separates characteristics by forcings adding no reals, opening a line towards constellations with singular $\mathfrak c$.

## 8. Future Work

1. **Classify all forceable constellations.** Decide whether the partial order of the diagram plus the Miller–Truss identities plus cofinality constraints is a *complete* axiomatisation of the possible value assignments.
2. **Minimise the continuum.** Force Cichoń's maximum with $\mathfrak c=\aleph_{10}$ for every admissible ordering, and with $\mathrm{cf}(\mathfrak c)=\omega$.
3. **Add more invariants.** Extend to Cichoń's diagram enlarged by $\mathfrak s$, $\mathfrak r$, $\mathfrak a$, $\mathfrak e$, and the ideals $\mathcal{SN}$, $\mathcal E$, $\mathcal M^*$, $\mathcal N^*$.
4. **Dualise the technique.** Find a self-dual iteration framework so that a left-side separation automatically yields the right-side one.
5. **Generalised Baire spaces.** Develop $\kappa$-versions of ultrafilter limits.

## 9. Key References

- **[Foundational]** T. Bartoszyński and H. Judah. *Set Theory: On the Structure of the Real Line.* A K Peters, 1995.
- **[Foundational]** A. Blass. *Combinatorial Cardinal Characteristics of the Continuum.* In: Handbook of Set Theory (Foreman & Kanamori, eds.), Springer, 2010, pp. 395–489.
- **[Foundational]** J. Brendle. *Larger cardinals in Cichoń's diagram.* Journal of Symbolic Logic 56 (1991), 795–810.
- **[Prior SOTA]** D. A. Mejía. *Matrix iterations and Cichoń's diagram.* Archive for Mathematical Logic 52 (2013), 261–278.
- **[Prior SOTA]** M. Goldstern, D. A. Mejía, S. Shelah. *The left side of Cichoń's diagram.* Proceedings of the AMS 144 (2016), 4025–4042.
- **[SOTA]** M. Goldstern, J. Kellner, S. Shelah. *Cichoń's maximum.* Annals of Mathematics 190 (2019), no. 1, 113–143.
- **[SOTA]** J. Kellner, S. Shelah, A. Tănasie. *Another ordering of the ten cardinal characteristics in Cichoń's diagram.* Archive for Mathematical Logic 58 (2019), 763–780.
- **[SOTA / Recent]** M. Goldstern, J. Kellner, D. A. Mejía, S. Shelah. *Cichoń's maximum without large cardinals.* Journal of the European Mathematical Society 24 (2022), 3951–3967.
- **[Recent]** M. Goldstern, J. Kellner, D. A. Mejía, S. Shelah. *Controlling cardinal characteristics without adding reals.* Journal of Mathematical Logic 21 (2021), no. 3, 2150018.
- **[Recent]** J. Brendle, M. A. Cardona, D. A. Mejía. *Filter-linkedness and its effect on preservation of cardinal characteristics.* Annals of Pure and Applied Logic 173 (2022), 103links — 103100.
- **[Survey]** M. Goldstern, J. Kellner, D. A. Mejía, S. Shelah. *Controlling classical cardinal characteristics while collapsing cardinals.* Colloquium Mathematicum 170 (2022), 115–144.

## 10. Worked Example / Concrete Special Case

**The Cohen model: two distinct values only, and why that is the obstruction in miniature.**

Start with $V\models\mathsf{CH}$ and force with $\mathbb C_{\omega_2}=\mathrm{Fn}(\omega_2,2)$, the finite-support product adding $\aleph_2$ Cohen reals. In $V[G]$, $\mathfrak c=\aleph_2$ and:

- The first $\aleph_1$ Cohen reals form a **Luzin set** $L$ (uncountable, meeting every meager set in a countable set). So $L\notin\mathcal M$ and $\mathrm{non}(\mathcal M)=\aleph_1$.
- Every meager set in $V[G]$ is coded in an intermediate model $V[G\restriction a]$, $|a|=\aleph_1$; a later Cohen real avoids it. Hence no $\aleph_1$ meager sets cover $\mathbb R$: $\mathrm{cov}(\mathcal M)=\aleph_2$.
- A Luzin set has strong measure zero, hence is null, so $L$ does not witness $\mathrm{non}(\mathcal N)$; by duality $\mathrm{cov}(\mathcal N)=\aleph_1$ and $\mathrm{non}(\mathcal N)=\aleph_2$.
- Cohen reals are unbounded but not dominating: $\mathfrak b=\aleph_1$, $\mathfrak d=\aleph_2$.
- $\mathrm{add}(\mathcal N)=\aleph_1$, $\mathrm{cof}(\mathcal N)=\aleph_2$.

Check the Miller–Truss identities: $\mathrm{add}(\mathcal M)=\min(\mathfrak b,\mathrm{cov}(\mathcal M))=\min(\aleph_1,\aleph_2)=\aleph_1$ ✓, and $\mathrm{cof}(\mathcal M)=\max(\mathfrak d,\mathrm{non}(\mathcal M))=\max(\aleph_2,\aleph_1)=\aleph_2$ ✓.

So the ten values collapse onto exactly **two** levels, $\{\aleph_1,\aleph_2\}$: the "left column" is $\aleph_1$, the "right column" is $\aleph_2$. This is the generic behaviour of a plain finite-support ccc iteration of length $\delta$ with $\mathrm{cf}(\delta)=\omega_2$: cofinally many Cohen reals push $\mathrm{cov}(\mathcal M)$ (and everything above it) to $\mathfrak c$ while a Luzin-type set keeps $\mathrm{non}(\mathcal M)$ at $\aleph_1$.

To get a **third** distinct value one interleaves, say, $\aleph_1$-many amoeba-for-category or localisation forcings on a subset of coordinates, controlled by a matrix iteration; to get a fourth and fifth, Mejía's matrices with different "columns" of models. Each new distinct value costs a new preservation theorem. The GKS/GKMS achievement is the mechanism — Boolean ultrapowers, then ultrafilter limits — that supplies the last three separations $\mathfrak d<\mathrm{non}(\mathcal N)<\mathrm{cof}(\mathcal N)<\mathfrak c$ *while* the Cohen reals of the finite-support skeleton keep $\mathrm{non}(\mathcal M)$ pinned below $\mathrm{cov}(\mathcal M)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*