---
id: 03-geometry/campana-peternell-conjecture
title: "Fano Varieties with Nef Tangent Bundle (Campana-Peternell Conjecture)"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fano Varieties with Nef Tangent Bundle (Campana–Peternell Conjecture)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/campana-peternell-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Conjecture (Campana–Peternell, 1991).** Let $X$ be a smooth complex projective variety whose tangent bundle $T_X$ is nef. Then $X$ is a *rational homogeneous space*: there is a semisimple algebraic group $G$ and a parabolic subgroup $P \subset G$ with
$$X \;\cong\; G/P .$$

Since $T_X$ nef implies $-K_X = \det T_X$ nef, and (by the Demailly–Peternell–Schneider structure theorem, §2) the general case reduces to the case $-K_X$ ample, the conjecture is usually stated for **Fano** manifolds:

> If $X$ is Fano and $T_X$ is nef, then $X \cong G/P$.

A complete proof must produce, for an arbitrary such $X$ of arbitrary dimension $n$ and Picard number $\rho(X)$, a transitive action of $\mathrm{Aut}^\circ(X)$ — equivalently show that $H^0(X, T_X)$ generates $T_X$ at every point. A disproof requires one Fano $X$ with $T_X$ nef and $\mathrm{Aut}^\circ(X)$ acting with a positive-dimensional orbit closure boundary. The converse is elementary: $T_{G/P} = G\times_P(\mathfrak g/\mathfrak p)$ is globally generated, hence nef.

## 2. Mathematical Foundations

**Nef vector bundles.** For a vector bundle $E$ on a projective variety $X$, let $\mathbb{P}(E) = \mathrm{Proj}\,\mathrm{Sym}\,E^\vee$ (quotient convention) with tautological quotient $\mathcal O_{\mathbb P(E)}(1)$. Then
$$E \text{ is nef} \iff \mathcal O_{\mathbb P(E)}(1)\cdot C \ge 0 \quad \text{for every irreducible curve } C \subset \mathbb P(E).$$
Nefness is stable under quotients, pullbacks, extensions, symmetric and tensor powers. On $\mathbb P^1$, $E \cong \bigoplus \mathcal O(a_i)$ is nef iff all $a_i \ge 0$.

**Fano.** $X$ is Fano if $-K_X$ is ample; the **index** $r_X$ is the largest integer with $-K_X = r_X H$ in $\mathrm{Pic}(X)$, and the **coindex** is $n+1-r_X$.

**Standing structure results.**

- *(Mori, 1979)* $T_X$ **ample** $\Rightarrow X \cong \mathbb P^n$ (Hartshorne's conjecture). This is the "positive-definite" endpoint of the CP conjecture.
- *(Demailly–Peternell–Schneider, 1994)* If $X$ is compact Kähler with $T_X$ nef, there is a finite étale cover $\tilde X \to X$ such that the Albanese map $\alpha:\tilde X \to \mathrm{Alb}(\tilde X)$ is a smooth surjective fibration whose fibers $F$ are Fano with $T_F$ nef; moreover $\pi_1(X)$ is virtually abelian. This isolates the Fano case as the whole content.
- *(Smoothness of contractions; DPS, Solá Conde–Wiśniewski)* Every elementary Mori contraction $\varphi: X \to Y$ of a Fano $X$ with $T_X$ nef is a smooth fibration, $Y$ is smooth Fano with $T_Y$ nef, and every fiber $F$ is Fano with $T_F$ nef. So the class is closed under contraction and under passing to fibers — the inductive engine of all known cases.
- *(Standard rational curves)* $X$ Fano with $T_X$ nef is rationally connected. For a minimal rational curve $f:\mathbb P^1 \to X$,
$$f^* T_X \;\cong\; \mathcal O(2)\oplus \mathcal O(1)^{\oplus p}\oplus \mathcal O^{\oplus\, n-1-p}, \qquad p = \deg f^*(-K_X) - 2 \ \ge 0,$$
because nefness forbids negative summands. Hence the **variety of minimal rational tangents** (VMRT) $\mathcal C_x \subset \mathbb P(T_{X,x})$ at a general point is smooth of dimension $p$, and the whole family is unsplit and smooth.

The conjecture is thus: *these local numerical constraints force the global Lie-theoretic model $G/P$.*

## 3. History & State of the Art (SOTA)

Campana and Peternell stated the conjecture in *Projective manifolds whose tangent bundles are numerically effective* (Math. Ann. **289**, 1991), where they also proved it in dimension $\le 3$. The motivation was to interpolate between Mori's characterization of $\mathbb P^n$ (ample $T_X$) and Siu–Yau/Beauville-type structure theorems for semipositive curvature: nefness is the algebraic shadow of "almost semipositive holomorphic bisectional curvature".

Milestones:

| Year | Result |
|---|---|
| 1979 | Mori: $T_X$ ample $\Rightarrow \mathbb P^n$ (all characteristics) |
| 1991 | Campana–Peternell: $\dim X \le 3$ |
| 1993 | Campana–Peternell: $\dim X = 4$, $b_2(X) \ge 2$ |
| 1994 | Demailly–Peternell–Schneider: Albanese structure theorem, reduction to Fano |
| 2002 | Mok: $\dim X=4$, $b_2=1$, via 1-dimensional VMRT |
| 2004 | Solá Conde–Wiśniewski: $T_X$ big and 1-ample case; smoothness of contractions |
| 2014 | Watanabe: $\dim X = 5$, $\rho \ge 2$ |
| 2016–17 | Kanemitsu: $\rho(X) > n-5$ in all dimensions; $\dim X = 5$ complete |
| 2017 | Occhetta–Solá Conde–Watanabe–Wiśniewski: all elementary contractions smooth $\mathbb P^1$-fibrations $\Rightarrow$ complete flag variety |

The 2015 survey by Muñoz, Occhetta, Solá Conde, Watanabe and Wiśniewski remains the reference account.

## 4. Partial Results / Verified Cases

Proven cases (all over $\mathbb C$):

- **Dimension $n \le 5$**, unconditionally. $n\le 3$: Campana–Peternell (1991). $n=4$: Campana–Peternell (1993) for $\rho\ge2$, Mok (2002) for $\rho=1$. $n=5$: Watanabe (2014) for $\rho\ge2$; Kanemitsu (2017) for $\rho=1$.
- **Large Picard number:** $\rho(X) > n-5$ in every dimension $n$ (Kanemitsu, Math. Z. 2016). In particular $\rho(X) \ge n$ forces $X \cong (\mathbb P^1)^n$-type products of homogeneous factors.
- **Low coindex:** Fano manifolds with nef $T_X$ and coindex $\le 3$ (i.e. $r_X \ge n-2$) are homogeneous (Watanabe); these are $\mathbb P^n$, quadrics $Q^n$, del Pezzo and Mukai varieties, and only the homogeneous ones survive nefness.
- **Flag-type hypotheses:** if every elementary contraction of $X$ is a smooth $\mathbb P^1$-fibration, then $X$ is the complete flag $G/B$ (Occhetta–Solá Conde–Watanabe–Wiśniewski, 2017). If $T_X$ is nef and **big and 1-ample**, $X$ is homogeneous (Solá Conde–Wiśniewski, 2004).
- **VMRT hypotheses:** $\rho=1$ with VMRT of dimension $p \le 1$, or with VMRT projectively equivalent to that of a known $G/P$ and satisfying Cartan–Fubini rigidity (Mok, Hwang).
- **$\rho = 1$ and index $r_X \ge \tfrac{n+1}{2}$** cases are covered by the coindex/length results above; the hard uncovered zone is $\rho=1$ with small index.
- **Horospherical / almost-homogeneous:** if $\mathrm{Aut}^\circ(X)$ already has a dense orbit, nefness of $T_X$ forces the boundary to be empty.

## 5. Principal Obstacles

- **No Lie group is given.** The hypothesis is numerical (a positivity condition on curves); the conclusion is that a semisimple group acts transitively. Nothing in the input produces vector fields: one must *construct* $H^0(X,T_X)$ of dimension $\ge n$ from positivity alone, and no general machine does this.
- **Vanishing theorems are too weak.** Kodaira/Nakano-type vanishing gives $H^i(X, T_X\otimes L)=0$ only under ampleness; nef is on the boundary and the relevant $H^1(X,T_X)$ (deformations) need not vanish for the target flag varieties either — rigidity of $G/P$ under Fano deformation is itself a theorem, not an input.
- **VMRT rigidity is conditional.** Hwang–Mok's Cartan–Fubini extension recovers $X$ from its VMRT $\mathcal C_x$, but only once $\mathcal C_x$ is known to be one of the specific homogeneous models. For $\rho=1$ and intermediate index, no classification of the possible smooth $p$-dimensional $\mathcal C_x \subset \mathbb P^{n-1}$ is available; that is a Fano classification problem of comparable difficulty.
- **Induction stalls at $\rho=1$.** All successful arguments contract an extremal ray, use nefness to get a smooth fibration, and induct. When $\rho(X)=1$ there is nothing to contract, so the entire structure theory collapses to the study of one family of rational curves.
- **Differential geometry does not close the gap.** Nef $T_X$ does *not* imply the existence of a metric with semipositive holomorphic bisectional curvature; if it did, Mok's uniformization theorem for semipositive bisectional curvature would settle the conjecture immediately. Nefness only gives metrics with curvature $\ge -\varepsilon\,\omega$ for every $\varepsilon>0$, and the $\varepsilon\to 0$ limit is not controlled.

## 6. The Gap

The proven region is: $n \le 5$, or $\rho > n-5$, or coindex $\le 3$, or a structural hypothesis on contractions/VMRT. The open region is precisely:

> $X$ Fano of dimension $n \ge 6$ with $\rho(X) = 1$ (more generally $\rho \le n-5$), nef $T_X$, index $r_X$ small relative to $n$, and VMRT $\mathcal C_x$ of dimension $p = r_X - 2$ not a priori identified.

The single step to cross: **show that the smooth VMRT $\mathcal C_x \subset \mathbb P^{n-1}$ of a Fano manifold with nef tangent bundle is the VMRT of a rational homogeneous space.** Given that, Cartan–Fubini extension (Hwang–Mok) finishes. Equivalently: prove the sub-adjoint/graded Lie algebra generated by $\mathcal C_x$ is semisimple of the right dimension.

## 7. Current Research (as of June 2026)

- **Kanemitsu (Kyoto/Saitama) and Watanabe (Chuo)** continue the contraction-theoretic program: pushing $\rho > n-5$ toward $\rho > n-k$ for larger $k$ by classifying the possible "Fano bundle" building blocks that occur as fibers. *(frontier — verify)*
- **Occhetta, Solá Conde (Trento) and Wiśniewski (Warsaw)** develop the theory of $\mathbb P^1$-fibration "flag bundles" and Bott–Samelson-type combinatorics as a synthetic characterization of $G/P$.
- **Hwang (KIAS/IBS-CCG) and Mok (HKU)** work on VMRT classification and Cartan–Fubini rigidity in the non-linearly-degenerate range; recognition theorems for adjoint and cominuscule VMRTs.
- **Positive characteristic.** Whether the analogue holds over $\overline{\mathbb F_p}$ is open and expected to be false in general; Mori's ample case survives, but Frobenius-related pathologies for merely nef bundles are documented. *(frontier — verify)*
- **Kähler/transcendental side.** Extending DPS to the non-projective Kähler case and proving that the Albanese fibration in DPS is *locally trivial* (still open in general) is pursued by Campana, Cao and Höring using positivity of direct images.

## 8. Future Work

1. **Classify smooth VMRTs with nef ambient data** for $p \le 3$ in arbitrary dimension; each new $p$ mechanically extends the theorem to a new index range.
2. **Prove $h^0(X,T_X) \ge \dim X$ directly** from nefness, e.g. by showing $H^1(X, T_X \otimes \mathcal I_Z)$ vanishes for suitable finite $Z$, then bootstrap transitivity.
3. **Extend the $\mathbb P^1$-fibration characterization** of $G/B$ to contractions with higher-dimensional fibers, giving all $G/P$ with $\rho \ge 2$ in one theorem.
4. **Deformation-rigidity route:** show the family of Fano manifolds with nef $T_X$ is unobstructed and connect any member to a homogeneous one, using rigidity of $G/P$ under Fano degeneration.
5. **Settle the characteristic-$p$ question** — either a counterexample there, or a characteristic-free proof, would sharply localize which inputs are essential.

## 9. Key References

- **[Foundational]** F. Campana, T. Peternell. *Projective manifolds whose tangent bundles are numerically effective.* Mathematische Annalen **289** (1991), 169–187.
- **[Foundational]** S. Mori. *Projective manifolds with ample tangent bundles.* Annals of Mathematics **110** (1979), 593–606.
- **[Foundational]** J.-P. Demailly, T. Peternell, M. Schneider. *Compact complex manifolds with numerically effective tangent bundles.* Journal of Algebraic Geometry **3** (1994), 295–345.
- **[Structure]** F. Campana, T. Peternell. *4-folds with numerically effective tangent bundles and second Betti numbers greater than one.* Manuscripta Mathematica **79** (1993), 225–238.
- **[VMRT]** N. Mok. *On Fano manifolds with nef tangent bundles admitting 1-dimensional varieties of minimal rational tangents.* Transactions of the AMS **354** (2002), 2639–2658.
- **[Structure]** L. E. Solá Conde, J. A. Wiśniewski. *On manifolds whose tangent bundle is big and 1-ample.* Proceedings of the London Mathematical Society **89** (2004), 273–290.
- **[SOTA]** K. Watanabe. *Fano 5-folds with nef tangent bundles and Picard numbers greater than one.* Mathematische Zeitschrift **276** (2014), 39–49.
- **[SOTA]** A. Kanemitsu. *Fano n-folds with nef tangent bundle and Picard number greater than $n-5$.* Mathematische Zeitschrift **284** (2016), 195–208.
- **[SOTA]** A. Kanemitsu. *Fano 5-folds with nef tangent bundles.* Mathematical Research Letters **24** (2017), 1453–1475.
- **[SOTA]** G. Occhetta, L. E. Solá Conde, K. Watanabe, J. A. Wiśniewski. *Fano manifolds whose elementary contractions are smooth $\mathbb P^1$-fibrations: a geometric characterization of flag varieties.* Annali della Scuola Normale Superiore di Pisa, Cl. Sci. (5) **17** (2017), 573–607.
- **[Survey]** R. Muñoz, G. Occhetta, L. E. Solá Conde, K. Watanabe, J. A. Wiśniewski. *A survey on the Campana–Peternell conjecture.* Rendiconti dell'Istituto di Matematica dell'Università di Trieste **47** (2015), 127–185.
- **[Background]** J. Kollár. *Rational Curves on Algebraic Varieties.* Ergebnisse der Mathematik 32, Springer, 1996.
- **[Background]** R. Lazarsfeld. *Positivity in Algebraic Geometry II.* Ergebnisse der Mathematik 49, Springer, 2004 (Ch. 6: positivity of vector bundles).

## 10. Worked Example / Concrete Special Case

**Dimension 2, $\rho = 2$: separating $\mathbb P^1\times\mathbb P^1$ from the blown-up plane.** Both are Fano surfaces of Picard number 2; the conjecture predicts only the first has nef tangent bundle.

*(a) $X = \mathbb P^1\times\mathbb P^1$.* Here
$$T_X \;=\; \mathrm{pr}_1^*\mathcal O_{\mathbb P^1}(2)\;\oplus\;\mathrm{pr}_2^*\mathcal O_{\mathbb P^1}(2),$$
a direct sum of globally generated line bundles, hence globally generated, hence nef. And indeed $X \cong (\mathrm{SL}_2/B)\times(\mathrm{SL}_2/B) = G/P$ with $G = \mathrm{SL}_2\times\mathrm{SL}_2$, $P = B\times B$. Consistent with the conjecture.

*(b) $X = \mathrm{Bl}_{pt}\mathbb P^2 = \mathbb F_1$.* This is Fano ($-K_X = 2\sigma + 3f$ is ample), but **not** homogeneous: $\mathrm{Aut}^\circ(X)$ fixes the exceptional curve $E$, so no transitive action exists. The conjecture therefore demands $T_X$ be non-nef. Verify directly. With $E \cong \mathbb P^1$, $E^2=-1$, the normal bundle is $N_{E/X} \cong \mathcal O_E(-1)$, and restricting the tangent sequence to $E$ gives
$$0 \longrightarrow T_E \cong \mathcal O_E(2) \longrightarrow T_X|_E \longrightarrow N_{E/X}\cong \mathcal O_E(-1)\longrightarrow 0 .$$
The sequence splits on $\mathbb P^1$, so $T_X|_E \cong \mathcal O(2)\oplus\mathcal O(-1)$. A quotient of a nef bundle is nef, and $\mathcal O_E(-1)$ is not nef; hence $T_X|_E$ is not nef, hence $T_X$ is not nef. Numerically: the section of $\mathbb P(T_X|_E)\to E$ corresponding to the quotient $\mathcal O(-1)$ is a curve $C$ with $\mathcal O_{\mathbb P(T_X)}(1)\cdot C = -1 < 0$.

*(c) The mechanism, in general.* The computation isolates exactly what nefness kills: a birational contraction. If $\varphi: X \to Y$ contracts a curve $C$ to a point, then $T_X|_C$ surjects onto a quotient of negative degree along $C$ (the normal directions collapse), contradicting nefness. This is the surface shadow of the general theorem "every elementary contraction of a Fano manifold with nef $T_X$ is a smooth fibration" — which is why the whole difficulty concentrates in $\rho(X)=1$, where there are no contractions to exploit.

*(d) One step up.* In dimension 3 the conjecture's list is $\mathbb P^3$, $Q^3$, $\mathbb P^1\times\mathbb P^2$, $(\mathbb P^1)^3$, and the flag $\mathbb F = \{(\ell,p) : \ell \subset p\} \subset \mathbb P^2\times(\mathbb P^2)^\vee$, i.e. $\mathbb F = \mathbb P(T_{\mathbb P^2}) = \mathrm{SL}_3/B$. For the last one, $T_{\mathbb P^2}$ is globally generated, so $\mathcal O_{\mathbb P(T_{\mathbb P^2})}(1)$ is globally generated; the two projections $\mathbb F \to \mathbb P^2$ are smooth $\mathbb P^1$-fibrations, matching the flag-variety characterization of Occhetta–Solá Conde–Watanabe–Wiśniewski exactly. Campana–Peternell's 1991 theorem is that this five-item list is complete.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*