---
id: 03-geometry/pandharipande-thomas-conjecture
title: "Pandharipande-Thomas Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Pandharipande-Thomas Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/pandharipande-thomas-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $X$ be a nonsingular projective 3-fold over $\mathbb{C}$ and $\beta \in H_2(X,\mathbb{Z})$ a nonzero curve class. Pandharipande and Thomas (2009) defined *stable pairs* invariants $P_{n,\beta} \in \mathbb{Z}$ counting pairs $(F,s)$ of a pure 1-dimensional sheaf and a section, and conjectured three linked statements.

- **(PT-R) Rationality.** The generating series
$$Z_{PT}(X;q)_\beta \;=\; \sum_{n \in \mathbb{Z}} P_{n,\beta}\, q^{n}$$
is the Laurent expansion of a rational function of $q$, invariant under $q \mapsto 1/q$.
- **(PT-DT) DT/PT correspondence.** $Z_{PT}(X;q)_\beta = Z_{DT}(X;q)_\beta / Z_{DT}(X;q)_0$, i.e. stable pairs compute the Donaldson–Thomas series of $X$ with the degree-0 (floating points) contribution removed.
- **(PT-GW) GW/Pairs correspondence.** After the change of variable $-q = e^{iu}$,
$$Z'_{GW}(X;u)_\beta \;=\; Z_{PT}(X;q)_\beta ,$$
where $Z'_{GW}$ is the reduced (connected, degree-0-removed) Gromov–Witten series of $X$ in class $\beta$.

A complete resolution means proving all three for every nonsingular projective 3-fold, in the equivariant and descendent-decorated forms as well. A disproof would exhibit a single $(X,\beta)$ where $Z_{PT}$ has an essential singularity, or where the GW and PT series disagree after analytic continuation.

**Status.** Solved for Calabi–Yau 3-folds: DT/PT by Bridgeland and Toda (2010–11), GW/DT/PT by Pardon (2023). Open for general (non-Calabi–Yau) 3-folds beyond the toric and complete-intersection cases.

## 2. Mathematical Foundations

**Stable pairs.** A pair $(F,s)$, $s \in H^0(X,F)$, is *stable* if
1. $F$ is pure of dimension 1 (no 0-dimensional subsheaves), and
2. $\operatorname{coker}(s : \mathcal{O}_X \to F)$ has 0-dimensional support.

Equivalently $s$ generates $F$ away from finitely many points. Fixing $[\operatorname{supp} F] = \beta$ and $\chi(F) = n$ gives a projective moduli scheme $P_n(X,\beta)$, constructed as a moduli of objects $I^\bullet = [\mathcal{O}_X \to F]$ in $D^b(X)$ with trivial determinant.

**Virtual class.** The deformation theory of $I^\bullet$ in the derived category gives a perfect obstruction theory of amplitude $[-1,0]$ and virtual dimension
$$\operatorname{vd} P_n(X,\beta) = \int_\beta c_1(T_X),$$
independent of $n$. For $X$ Calabi–Yau ($K_X \cong \mathcal{O}_X$) this is $0$, and
$$P_{n,\beta} = \int_{[P_n(X,\beta)]^{\mathrm{vir}}} 1 \;=\; e\big(P_n(X,\beta),\ \nu\big) = \sum_{k\in\mathbb{Z}} k\, e\big(\nu^{-1}(k)\big),$$
the Euler characteristic weighted by the Behrend constructible function $\nu$.

**DT side.** $I_n(X,\beta) = \operatorname{Hilb}^{n,\beta}(X)$ is the Hilbert scheme of 1-dimensional subschemes with $[Z]=\beta$, $\chi(\mathcal{O}_Z)=n$; $Z_{DT}(q)_\beta = \sum_n I_{n,\beta} q^n$. The MNOP degree-0 series is $Z_{DT}(q)_0 = M(-q)^{\int_X c_3(T_X\otimes K_X)}$ with $M(q)=\prod_{n\ge1}(1-q^n)^{-n}$ the MacMahon function.

**GW side.** $N_{g,\beta} = \int_{[\overline{M}_g(X,\beta)]^{\mathrm{vir}}}1$ and $Z'_{GW}(u)_\beta = \sum_g N_{g,\beta}u^{2g-2}$. Rationality of $Z_{PT}$ is what makes the substitution $-q=e^{iu}$ meaningful: it identifies a formal $u$-series with the expansion of a rational function of $q$ around $q=-1$.

**BPS form.** PT (2010) predicted the Gopakumar–Vafa structure
$$Z_{PT}(q)_\beta \;=\; \sum_{g\ge 0}\ \sum_{\beta'} n^g_{\beta'}\, \text{(universal contribution)},\qquad n^g_\beta \in \mathbb{Z},$$
with $n^g_\beta = 0$ for $g \gg 0$; equivalently the log of the full series is a $\mathbb{Z}$-linear combination of $d^{-1}\big(q^{d/2}+q^{-d/2}\big)^{2g-2}$-type terms.

## 3. History & State of the Art (SOTA)

- **1998–2000.** Thomas constructs DT invariants of 3-folds via holomorphic Casson theory; Gopakumar–Vafa predict integrality of BPS counts from M-theory.
- **2006.** Maulik–Nekrasov–Okounkov–Pandharipande (MNOP I, II, *Compositio Math.* 142) conjecture the GW/DT correspondence and the rationality of $Z_{DT}/Z_{DT,0}$.
- **2009.** Pandharipande–Thomas introduce stable pairs (*Invent. Math.* 178) precisely to remove the degree-0 and "floating point" noise from DT theory, and formulate (PT-R), (PT-DT), (PT-GW). PT III computes the *topological vertex for pairs*.
- **2010–11.** Toda (*JAMS* 23) and Bridgeland (*JAMS* 24) prove the DT/PT correspondence for Calabi–Yau 3-folds by Hall-algebra wall-crossing; Stoppa–Thomas give a GIT/derived-category wall-crossing proof of the Euler-characteristic version.
- **2011.** Maulik–Oblomkov–Okounkov–Pandharipande prove GW/DT for **all nonsingular projective toric 3-folds** (*Invent. Math.* 186), via the equivariant vertex and $\mathbb{C}^*$-localization.
- **2014–2017.** Pandharipande–Pixton prove the descendent GW/Pairs correspondence for toric 3-folds (*Geom. Topol.* 18) and for the **quintic 3-fold** and many complete intersections in products of projective spaces (*JAMS* 30).
- **2023.** Pardon, *Universally counting curves in Calabi–Yau threefolds* (arXiv:2308.14432), proves the GW/DT and hence GW/PT correspondence for all Calabi–Yau 3-folds by constructing a universal curve-counting invariant, resolving the MNOP/PT conjectures in the CY3 case.

## 4. Partial Results / Verified Cases

| Class of $X$ | Result | Source |
|---|---|---|
| Calabi–Yau 3-folds (any, incl. compact) | DT/PT correspondence, rationality (Euler-char. and Behrend-weighted) | Toda 2010; Bridgeland 2011 |
| Calabi–Yau 3-folds | full GW/DT/PT correspondence | Pardon 2023 |
| Nonsingular projective toric 3-folds | GW/DT, plus descendent GW/Pairs; rationality of the equivariant vertex | MOOP 2011; Pandharipande–Pixton 2014 |
| Quintic $X_5\subset\mathbb{P}^4$ and complete intersections in products of $\mathbb{P}^n$ | GW/Pairs | Pandharipande–Pixton 2017 |
| Local curves $N \to C$ (rank-2 bundles over curves) | rationality of the full descendent theory | Pandharipande–Pixton, *Compositio* 149 (2013) |
| Irreducible (primitive) classes $\beta$ on CY3 | BPS integrality and strong rationality | Pandharipande–Thomas, *JAMS* 23 (2010) |
| Resolved conifold, local $\mathbb{P}^2$, local $\mathbb{P}^1\times\mathbb{P}^1$ | closed-form $Z_{PT}$ verified to high order in $q$ and $Q$ | topological vertex computations, PT III |
| Calabi–Yau 4-folds ($\mathrm{PT}_4$ analogue) | conjectural framework, verified in examples | Cao–Maulik–Toda, *JEMS* 24 (2022) |

## 5. Principal Obstacles

- **Wall-crossing needs a Calabi–Yau symmetry.** The Joyce–Song / Bridgeland / Toda machinery expresses DT/PT identities as identities in a motivic Hall algebra, but the integration map is a ring homomorphism only because Serre duality on a CY3 makes the Ext-pairing antisymmetric: $\chi(E,F) = -\chi(F,E)$. On a general 3-fold $\chi(-,-)$ is not antisymmetric, the Behrend-function identities fail, and no substitute Poisson structure is known.
- **Non-CY virtual classes are not Euler characteristics.** When $\int_\beta c_1(T_X) \ne 0$ the invariants are not weighted Euler characteristics of the moduli space, so all motivic/cut-and-paste arguments become unavailable. One must work with the virtual class itself, which is not localizable without a torus action — hence the confinement of MOOP-type proofs to the toric case.
- **Analytic continuation.** GW theory is a formal series in $u$ around $u=0$; PT theory is a series in $q$ around $q=0$. The correspondence is an equality of two expansions of a single rational function at *different* points ($q=0$ vs $q=-1$). Without rationality proven first, the two sides are not even comparable, and rationality is exactly a statement about the vanishing of $P_{n,\beta}$ for $n \ll 0$ plus a functional equation — neither has a geometric proof in general.
- **Degeneration does not close.** The degeneration formula relates $X$ to simpler pieces, but the relative pairs theory of a 3-fold with divisor requires rationality *with descendents* on the pieces; Pandharipande–Pixton's induction closes only for geometries built from toric pieces and local curves.
- **Pardon's method is CY-specific.** His universal invariant is built from the structure of moduli of stable maps/ideal sheaves in the 0-virtual-dimension setting, using CY3 deformation invariance; it does not extend to $\int_\beta c_1(T_X) \ne 0$.

## 6. The Gap

Proven: the full package for Calabi–Yau 3-folds (Pardon 2023, on top of Bridgeland–Toda), and the toric plus complete-intersection cases with descendents. The general statement asks for arbitrary nonsingular projective 3-folds — in particular Fano and general-type 3-folds with $\int_\beta c_1(T_X) \ne 0$, and non-toric non-CY geometries.

The precise missing step is a *virtual* wall-crossing formula: an identity comparing $[\,I_n(X,\beta)\,]^{\mathrm{vir}}$ and $[\,P_n(X,\beta)\,]^{\mathrm{vir}}$ that does not pass through weighted Euler characteristics. Equivalently, one needs either (a) a shifted-symplectic / Joyce-style vertex algebra wall-crossing valid without the CY3 symmetry, or (b) a direct geometric proof that $P_{n,\beta}=0$ for $n \ll 0$ together with the $q\mapsto 1/q$ functional equation, for arbitrary $X$.

## 7. Current Research (as of June 2026)

- **Joyce's vertex algebra wall-crossing** (Oxford) for moduli of sheaves on higher-dimensional and non-CY targets, aiming at virtual DT/PT identities without the antisymmetry hypothesis. *(frontier — verify)*
- **Post-Pardon program.** Extensions of *Universally counting curves in Calabi–Yau threefolds* toward Gopakumar–Vafa integrality and toward non-CY targets are actively pursued (Pardon; Stanford/Princeton). *(frontier — verify)*
- **CY4 stable pairs ($\mathrm{PT}_4$).** Cao–Maulik–Toda and collaborators; conjectural GV-type integrality and comparison with $\mathrm{DT}_4$ invariants, tested on $\mathbb{C}^4$ and elliptic fibrations.
- **K-theoretic and refined lifts.** Okounkov's K-theoretic DT/PT, Nekrasov–Okounkov's *Membranes and Sheaves*, and the refined topological vertex; the refined GW/PT correspondence remains conjectural for compact targets.
- **Categorification / cohomological DT** (Kinjo, Toda, Szendrői schools): DT/PT at the level of vanishing-cycle cohomology, which would upgrade the numerical statement.
- **Gopakumar–Vafa via Maulik–Toda**: defining $n^g_\beta$ from perverse sheaves on the moduli of 1-dimensional sheaves; known counterexamples to the naive form (Maulik–Toda themselves flag irreducibility hypotheses) keep this open.

## 8. Future Work

- Prove rationality of $Z_{PT}(X;q)_\beta$ for an arbitrary 3-fold directly, e.g. by bounding $\chi(F)$ from below on stable pairs with fixed support class.
- Develop virtual (non-motivic) Hall algebra techniques: a wall-crossing for shifted-symplectic derived stacks that produces virtual-class identities.
- Extend the degeneration/relative machinery so that the descendent correspondence for relative geometries closes for all 3-folds admitting a degeneration to normal-crossings pieces.
- Settle GV integrality: derive $n^g_\beta \in \mathbb{Z}$ from the stable-pairs side, unconditionally, for compact CY3s.
- Establish the CY4 analogue: a $\mathrm{PT}_4/\mathrm{DT}_4$ correspondence and its Gromov–Witten counterpart.

## 9. Key References

- **[Foundational]** R. Pandharipande, R. P. Thomas. *Curve counting via stable pairs in the derived category.* Inventiones Mathematicae 178 (2009), 407–447.
- **[Foundational]** R. Pandharipande, R. P. Thomas. *Stable pairs and BPS invariants.* Journal of the AMS 23 (2010), 267–297.
- **[Foundational]** D. Maulik, N. Nekrasov, A. Okounkov, R. Pandharipande. *Gromov–Witten theory and Donaldson–Thomas theory, I and II.* Compositio Mathematica 142 (2006), 1263–1285 and 1286–1304.
- **[SOTA / Recent]** J. Pardon. *Universally counting curves in Calabi–Yau threefolds.* arXiv:2308.14432, 2023.
- **[SOTA]** T. Bridgeland. *Hall algebras and curve-counting invariants.* Journal of the AMS 24 (2011), 969–998.
- **[SOTA]** Y. Toda. *Curve counting theories via stable objects I: DT/PT correspondence.* Journal of the AMS 23 (2010), 1119–1157.
- **[SOTA]** D. Maulik, A. Oblomkov, A. Okounkov, R. Pandharipande. *Gromov–Witten/Donaldson–Thomas correspondence for toric 3-folds.* Inventiones Mathematicae 186 (2011), 435–479.
- **[SOTA]** R. Pandharipande, A. Pixton. *Gromov–Witten/Pairs correspondence for the quintic 3-fold.* Journal of the AMS 30 (2017), 389–449.
- **[SOTA]** J. Stoppa, R. P. Thomas. *Hilbert schemes and stable pairs: GIT and derived category wall crossings.* Bulletin de la SMF 139 (2011), 297–339.
- **[Recent]** Y. Cao, D. Maulik, Y. Toda. *Stable pairs and Gopakumar–Vafa type invariants for Calabi–Yau 4-folds.* Journal of the EMS 24 (2022), 527–581.
- **[Survey]** R. Pandharipande, R. P. Thomas. *13/2 ways of counting curves.* In *Moduli Spaces*, LMS Lecture Note Series 411, Cambridge University Press, 2014, 282–333.
- **[Survey]** R. Pandharipande. *Descendents for stable pairs on 3-folds.* In *Modern Geometry: A Celebration of the Work of Simon Donaldson*, Proc. Sympos. Pure Math. 99, AMS, 2018.

## 10. Worked Example / Concrete Special Case

**The resolved conifold $X = \mathcal{O}_{\mathbb{P}^1}(-1)\oplus\mathcal{O}_{\mathbb{P}^1}(-1) \to \mathbb{P}^1$, degree $\beta = 1$.**

*Pairs side.* A stable pair of degree 1 is supported on the rigid zero-section $C\cong\mathbb{P}^1$ (with possible thickening), and one computes
$$P_n(X,1) \;\cong\; \mathbb{P}^{\,n-1},\qquad n \ge 1,$$
the projective space of cokernel data of length $n-1$ along $C$; $P_n(X,1)=\varnothing$ for $n\le 0$. The obstruction theory is symmetric, so the Behrend function is constant $\nu = (-1)^{\dim} = (-1)^{n-1}$ and
$$P_{n,1} \;=\; (-1)^{n-1} e(\mathbb{P}^{n-1}) \;=\; (-1)^{n-1} n .$$
Hence
$$Z_{PT}(q)_{1} \;=\; \sum_{n\ge 1} (-1)^{n-1} n\, q^{n} \;=\; \frac{q}{(1+q)^{2}} .$$
This is rational — confirming (PT-R) — and satisfies the functional equation:
$$Z_{PT}(1/q)_1 = \frac{1/q}{(1+1/q)^2} = \frac{q}{(1+q)^2} = Z_{PT}(q)_1 .$$

*DT side.* The full DT series is $Z_{DT}(q,Q) = M(-q)^{2}\prod_{n\ge1}\big(1-(-q)^nQ\big)^{n}$ with $\int_X c_3(T_X\otimes K_X) = 2$, so $Z_{DT}(q)_0 = M(-q)^2$ and the $Q^1$-coefficient of the quotient is $-\sum_{n\ge1} n(-q)^n = q/(1+q)^2$. This matches $Z_{PT}(q)_1$ exactly, verifying (PT-DT).

*Gromov–Witten side.* Substitute $-q=e^{iu}$, i.e. $q^{1/2}+q^{-1/2} = i\big(e^{iu/2}-e^{-iu/2}\big) = -2\sin(u/2)$:
$$\frac{q}{(1+q)^{2}} = \frac{1}{\big(q^{1/2}+q^{-1/2}\big)^{2}} = \frac{1}{\big(2\sin(u/2)\big)^{2}} .$$
The right-hand side is precisely the genus expansion of the degree-1 Gromov–Witten series of the resolved conifold predicted by the Aspinwall–Morrison multiple-cover formula with a single BPS state $n^0_1 = 1$:
$$Z'_{GW}(u)_1 = \sum_{g \ge 0} N_{g,1}u^{2g-2} = \frac{1}{4\sin^2(u/2)} = \frac{1}{u^2} + \frac{1}{12} + \frac{u^2}{240}+\cdots,$$
so $N_{0,1}=1$, $N_{1,1}=1/12$, $N_{2,1}=1/240$. All three conjectures hold in this case, and the BPS extraction gives $n^0_1=1$, $n^{g}_1=0$ for $g\ge1$ — the expected single rigid rational curve.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*