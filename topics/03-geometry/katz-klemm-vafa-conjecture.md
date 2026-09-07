---
id: 03-geometry/katz-klemm-vafa-conjecture
title: "Katz-Klemm-Vafa Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Katz-Klemm-Vafa Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/katz-klemm-vafa-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $S$ be a smooth projective $K3$ surface and $\beta \in H_2(S,\mathbb{Z})$ a nonzero effective curve class. Because $S$ is holomorphic symplectic, all ordinary Gromov–Witten invariants of $S$ vanish; the enumerative content lives in the **reduced** theory. The Katz–Klemm–Vafa (KKV) conjecture asserts:

1. **Deformation/monodromy invariance in strong form.** The reduced BPS (Gopakumar–Vafa) invariant $r_{g,\beta}$ depends on $\beta$ only through the self-intersection $\beta^2 = 2h-2$ — in particular it is *independent of the divisibility* $m = \operatorname{div}(\beta)$.
2. **Closed product formula.** With $r_{g,h} := r_{g,\beta}$ for $\beta^2 = 2h-2$,
$$\sum_{h \ge 0} \sum_{g \ge 0} (-1)^g\, r_{g,h}\, \big(y^{1/2}-y^{-1/2}\big)^{2g} q^{h} \;=\; \prod_{m \ge 1} \frac{1}{(1-q^m)^{20}\,(1-y\,q^m)^2\,(1-y^{-1}q^m)^2}.$$

Setting $y=1$ kills all $g>0$ terms and recovers the **Yau–Zaslow formula** $\sum_h r_{0,h}q^h = \prod_{m\ge1}(1-q^m)^{-24} = q/\Delta(q)$.

A complete proof requires (i) a rigorous definition of $r_{g,\beta}$ (via reduced Gromov–Witten theory and the Gopakumar–Vafa change of variables, or via stable pairs), (ii) the divisibility-independence, and (iii) the product identity for all $g,h$. **Status:** items (i)–(iii) were established by Pandharipande–Thomas (2016). The *refined/motivic* strengthening remains open in general.

## 2. Mathematical Foundations

**Reduced virtual class.** For $\overline{M}_{g}(S,\beta)$ the moduli of stable maps, the holomorphic symplectic form gives a trivial quotient of the obstruction sheaf, so $[\overline{M}_g(S,\beta)]^{\mathrm{vir}} = 0$. Removing that trivial factor yields the reduced class, of virtual dimension
$$\operatorname{vdim}\,[\overline{M}_g(S,\beta)]^{\mathrm{red}} = g .$$
The relevant invariants are the $\lambda_g$-twisted ones,
$$R_{g,\beta} \;=\; \int_{[\overline{M}_g(S,\beta)]^{\mathrm{red}}} (-1)^g \lambda_g ,$$
where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle. Equivalently $R_{g,\beta}$ is the reduced Gromov–Witten count of the local Calabi–Yau threefold $S \times \mathbb{C}$ (equivariantly, the KKV geometry).

**Gopakumar–Vafa transform.** The integers $r_{g,\beta}$ are defined by
$$\sum_{g \ge 0} R_{g,\beta}\, u^{2g-2} \;=\; \sum_{g \ge 0} r_{g,\beta} \sum_{m \ge 1} \frac{1}{m}\Big(2\sin\frac{mu}{2}\Big)^{2g-2},$$
with $y = e^{iu}$ so that $\big(y^{1/2}-y^{-1/2}\big)^{2} = -4\sin^2(u/2)$. Only finitely many $r_{g,\beta}$ are nonzero for fixed $\beta$ (vanishing above the arithmetic genus $h$).

**Lattice input.** $H^2(S,\mathbb{Z}) \cong U^{\oplus 3}\oplus E_8(-1)^{\oplus 2}$, the unique even unimodular lattice of signature $(3,19)$. By the Torelli theorem and Eichler's criterion, two classes with the same $\beta^2$ and the same divisibility are equivalent under monodromy plus deformation; hence $r_{g,\beta}$ depends *a priori* only on $(\beta^2,\operatorname{div}\beta)$. The conjecture's part (1) is the statement that the divisibility drops out.

**Right-hand side.** The product is the generating series of Hodge numbers of Hilbert schemes of points,
$$\prod_{m\ge1}\frac{1}{(1-q^m)^{20}(1-yq^m)^2(1-y^{-1}q^m)^2} = \sum_{n \ge 0} q^{n}\, \chi_{-y}\big(\mathrm{Hilb}^{n}\big)\Big|_{\text{normalized}},$$
reflecting the Göttsche formula, and equals $-\,y/\big(\phi_{-2,1}(y,q)\,\Delta(q)\big)$ up to normalization, with $\phi_{-2,1}$ the weak Jacobi form of weight $-2$ and index $1$. The KKV series is thus a *meromorphic Jacobi form*, which is the modularity content of the conjecture.

## 3. History & State of the Art (SOTA)

- **1995–96.** Yau and Zaslow, using the string-duality count of BPS states on $K3$, predicted $\sum_h n_h q^h = q/\Delta(q)$ for the number of rational curves in a primitive class with $\beta^2 = 2h-2$.
- **1999.** Katz, Klemm and Vafa, in *M-theory, topological strings and spinning black holes*, extended this to all genera by including the spin (left $SU(2)$) content of the BPS states, producing the full two-variable product formula. The physical derivation identifies $r_{g,\beta}$ with the $\mathfrak{sl}_2$-decomposition of the cohomology of the moduli of one-dimensional sheaves on $S$.
- **2000.** Bryan–Leung proved the primitive-class Yau–Zaslow formula, and the genus-$g$ primitive count for the elliptically fibered $K3$ with a section, by degeneration to a rational elliptic surface.
- **2000.** Kawai–Yoshioka computed Euler characteristics of moduli of stable pairs / Hilbert schemes of curves on $K3$ in primitive classes, confirming the KKV product formula in that case at the sheaf-theoretic level.
- **2010.** Klemm–Maulik–Pandharipande–Scheidegger proved the Yau–Zaslow formula for **all** classes (arbitrary divisibility) using Noether–Lefschetz theory on the STU model, a $K3$-fibered Calabi–Yau threefold.
- **2010.** Maulik–Pandharipande–Thomas proved the full KKV formula for **primitive** $\beta$, all genera.
- **2016.** Pandharipande–Thomas proved KKV in full generality (*Forum of Mathematics, Pi* 4, e4), via reduced stable-pairs invariants of $S\times\mathbb{C}$, the GW/Pairs correspondence, and a Noether–Lefschetz/degeneration argument removing the primitivity hypothesis.
- **2018.** Oberdieck–Pixton proved the Igusa cusp form conjecture for $K3\times E$, the natural "second-quantized" companion statement.

## 4. Partial Results / Verified Cases

| Case | Result | Author, year |
|---|---|---|
| $g=0$, $\beta$ primitive | $\sum_h n_h q^h = q/\Delta$ | Bryan–Leung, 2000 |
| $g=0$, all divisibilities $m$ | Yau–Zaslow for every $\beta$ | Klemm–Maulik–Pandharipande–Scheidegger, 2010 |
| all $g$, $\beta$ primitive | full KKV product formula | Maulik–Pandharipande–Thomas, 2010 |
| all $g$, primitive, sheaf side | Euler characteristics of stable-pair moduli | Kawai–Yoshioka, 2000 |
| all $g$, all $\beta$ | KKV conjecture proved | Pandharipande–Thomas, 2016 |
| refined/motivic KKV, irreducible $\beta$ | perverse-sheaf refinement, $\chi$-independence | Maulik–Thomas, 2018 |
| $K3 \times E$, all classes | Igusa cusp form $\chi_{10}$ | Oberdieck–Pixton, 2018 |

Low-degree data: $r_{g,h}$ for $h=0,1,2,3$ is $\;1$; $\;24,-2$; $\;324,-54,3$; $\;3200,-800,88,-4$ (genus $0,1,2,\dots$). These match localization computations on elliptic $K3$s and the sheaf-counting tables of Kawai–Yoshioka.

## 5. Principal Obstacles

The difficulties that made the imprimitive case resist for fifteen years, and that still block the refined statement:

- **Vanishing of the standard virtual class.** Ordinary GW/DT theory returns zero on $K3$; every technique must be rebuilt for the reduced class, where the usual degeneration formula, deformation invariance and gluing axioms hold only after careful bookkeeping of which factor of the obstruction theory is trivialized.
- **Multiple covers.** For $\beta = m\beta'$ with $m\ge2$, the moduli space contains maps factoring through curves in the primitive class $\beta'$. Excess-intersection and multiple-cover contributions are not governed by any known universal formula on a holomorphic symplectic surface, so the primitive answer does not propagate by a naive multiple-cover ansatz.
- **Lattice-theoretic non-rigidity.** Deformation invariance only gives equality of invariants within fixed $(\beta^2,\operatorname{div}\beta)$. Comparing different divisibilities requires an *external* geometry: KMPS and PT both embed the $K3$ into a family (the STU model), where Noether–Lefschetz numbers of the family mix classes of different divisibility. Constructing such families with the required modularity is delicate and does not generalize freely.
- **Refined setting.** The motivic/refined KKV needs a well-behaved motivic or perverse-sheaf-theoretic virtual invariant. Existence of global orientation data, and $\chi$-independence for imprimitive Mukai vectors on $K3$, are exactly where present methods (support maps, perverse filtration, Ngô-type decomposition) stop.

## 6. The Gap

The gap for the *numerical* KKV conjecture is closed: Pandharipande–Thomas 2016 proves Section 1 in full. The remaining boundary is one level up:

- **Refined KKV.** Katz–Klemm–Pandharipande conjecture a two-variable ($y$ and a motivic/weight variable $t$) refinement whose specialization is KKV. It is known for irreducible classes (Maulik–Thomas) but **open for imprimitive $\beta$**; the missing step is $\chi$-independence of motivic stable-pair invariants of $S\times\mathbb{C}$ in classes of divisibility $m \ge 2$.
- **Sheaf-theoretic KKV.** A proof purely in terms of Gopakumar–Vafa invariants defined by Maulik–Toda vanishing cycles (rather than via the GW transform) is not available; it would require the Maulik–Toda definition to be shown deformation invariant and to agree with the GW-defined $r_{g,\beta}$.
- **Higher-dimensional analogue.** For holomorphic symplectic varieties of dimension $2n>2$ (e.g. $\mathrm{Hilb}^n(K3)$, generalized Kummer), no proved product formula exists.

## 7. Current Research (as of June 2026)

- **Refined/motivic invariants.** Work in the school of Maulik, Thomas, Toda and Kinjo on cohomological Donaldson–Thomas theory and $\chi$-independence for one-dimensional sheaves; extensions of the Bousseau–Maulik–Toda circle of ideas to imprimitive $K3$ classes. *(frontier — verify)*
- **Quasi-Jacobi forms.** Oberdieck (Bonn) and collaborators on Gromov–Witten theory of $K3$-fibrations, holomorphic anomaly equations, and the Hilb/GW correspondence for $\mathrm{Hilb}^n(K3)$; conjectural higher-dimensional KKV analogues. *(frontier — verify)*
- **Derived-category/wall-crossing proofs.** Attempts to recover KKV from Bridgeland stability and Joyce-type wall-crossing on $\mathrm{Coh}(S)$, bypassing Noether–Lefschetz families entirely.
- **Physics side.** Continued study of the $\mathcal{N}=4$ dyon counting / Igusa cusp form $\chi_{10}$ and its relation to the KKV series, including Mathieu-moonshine refinements of the $y$-expansion.

Key groups: ETH Zürich / Bonn (Pandharipande, Oberdieck), Imperial College (Thomas), Columbia, IPMU (Toda), Edinburgh/Oxford (Maulik).

## 8. Future Work

- Prove $\chi$-independence for motivic/perverse invariants of $S\times\mathbb{C}$ in arbitrary divisibility, completing refined KKV.
- Establish that Maulik–Toda GV invariants of local $K3$ satisfy the KKV product formula intrinsically, giving a definition-independent statement.
- Formulate and test a KKV-type product formula for $\mathrm{Hilb}^n(K3)$ and $O'Grady$ manifolds, guided by the expected Jacobi-form modularity.
- Extend the Pandharipande–Thomas Noether–Lefschetz method to Enriques surfaces and to $K3$-fibered Calabi–Yau fourfolds.

## 9. Key References

- **[Foundational]** S. Katz, A. Klemm, C. Vafa. *M-theory, topological strings and spinning black holes.* Advances in Theoretical and Mathematical Physics 3 (1999), 1445–1537.
- **[Foundational]** S.-T. Yau, E. Zaslow. *BPS states, string duality, and nodal curves on K3.* Nuclear Physics B 471 (1996), 503–512.
- **[Foundational]** J. Bryan, N. C. Leung. *The enumerative geometry of K3 surfaces and modular forms.* Journal of the AMS 13 (2000), 371–410.
- **[Foundational]** T. Kawai, K. Yoshioka. *String partition functions and infinite products.* Advances in Theoretical and Mathematical Physics 4 (2000), 397–485.
- **[SOTA]** R. Pandharipande, R. P. Thomas. *The Katz–Klemm–Vafa conjecture for K3 surfaces.* Forum of Mathematics, Pi 4 (2016), e4.
- **[SOTA]** D. Maulik, R. Pandharipande, R. P. Thomas. *Curves on K3 surfaces and modular forms.* Journal of Topology 3 (2010), 937–996.
- **[SOTA]** A. Klemm, D. Maulik, R. Pandharipande, E. Scheidegger. *Noether–Lefschetz theory and the Yau–Zaslow conjecture.* Journal of the AMS 23 (2010), 1013–1040.
- **[Recent]** S. Katz, A. Klemm, R. Pandharipande, with an appendix by R. P. Thomas. *On the motivic stable pairs invariants of K3 surfaces.* Journal of Algebraic Geometry 27 (2018), 151–199.
- **[Recent]** D. Maulik, R. P. Thomas. *Sheaf counting on local K3 surfaces.* Pure and Applied Mathematics Quarterly 14 (2018), 419–441.
- **[Recent]** G. Oberdieck, A. Pixton. *Holomorphic anomaly equations and the Igusa cusp form conjecture.* Inventiones Mathematicae 213 (2018), 507–587.
- **[Survey]** D. Maulik, Y. Toda. *Gopakumar–Vafa invariants via vanishing cycles.* Inventiones Mathematicae 213 (2018), 1017–1097.

## 10. Worked Example / Concrete Special Case

**Extracting $r_{g,h}$ for $h \le 2$ from the product.** Write $X = (y^{1/2}-y^{-1/2})^2 = y - 2 + y^{-1}$ and expand
$$F(y,q) = \prod_{m\ge1}\frac{1}{(1-q^m)^{20}(1-yq^m)^2(1-y^{-1}q^m)^2}.$$

*Order $q^0$.* $F = 1 + O(q)$, so $r_{0,0}=1$: the class with $\beta^2=-2$ is represented by a single rigid smooth rational curve (a $(-2)$-curve), contributing $1$.

*Order $q^1$.* Only $m=1$ contributes: $20 + 2y + 2y^{-1} = 24 + 2X$. Matching against $r_{0,1} - r_{1,1}X$ gives
$$r_{0,1} = 24, \qquad r_{1,1} = -2 .$$
Geometric check: for an elliptic $K3$ with $\beta = [\text{fiber}]$ ($\beta^2 = 0$), the Euler characteristic of the fibration forces exactly $24$ nodal fibers, so $r_{0,1}=24$; the genus-1 value $-2 = -\chi(\mathbb{P}^1)$ records the $\mathbb{P}^1$ of smooth fibers.

*Order $q^2$.* Collecting the $q^2$ coefficient of $F$: from $(1-q)^{-20}$, $\binom{21}{2}=210$; from $(1-q^2)^{-20}$, $20$; from $(1-y^{\pm1}q)^{-2}$, $3y^{2}+3y^{-2}$; from $(1-y^{\pm1}q^2)^{-2}$, $2y+2y^{-1}$; cross terms of two $q^1$ pieces, $20\!\cdot\!2y + 20\!\cdot\!2y^{-1} + 2y\!\cdot\!2y^{-1} = 40(y+y^{-1})+4$. Total:
$$234 + 42(y+y^{-1}) + 3(y^{2}+y^{-2}).$$
Using $X^2 = y^2 + y^{-2} - 4(y+y^{-1}) + 6$ and matching $r_{0,2} - r_{1,2}X + r_{2,2}X^2$ term by term:
- $y^{2}$: $r_{2,2} = 3$;
- $y$: $-r_{1,2} - 4\cdot 3 = 42 \Rightarrow r_{1,2} = -54$;
- constant: $r_{0,2} + 2(-54) + 6(3) = 234 \Rightarrow r_{0,2} = 324$.

So $(r_{0,2},r_{1,2},r_{2,2}) = (324,-54,3)$. The value $324$ is the classical Yau–Zaslow count of rational curves in a class with $\beta^2 = 2$ — e.g. the $324$ rational curves in $|\mathcal{O}(1)|$ on a degree-$2$ polarized $K3$ — and $r_{2,2}=3$ is the count of the top-genus family. The conjecture (now theorem) is that these same three numbers occur for *every* class with $\beta^2 = 2$, including $\beta = 2\gamma$ with $\gamma^2 = 1/2$-type obstructions absent, i.e. independently of divisibility.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*