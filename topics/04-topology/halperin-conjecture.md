---
id: 04-topology/halperin-conjecture
title: "Halperin Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Halperin Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/halperin-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $F$ be an **$F_0$-space**: a simply connected topological space with finite-dimensional rational homotopy $\pi_*(F)\otimes\mathbb{Q}$, finite-dimensional rational cohomology, and $H^{\mathrm{odd}}(F;\mathbb{Q})=0$ (equivalently, $\chi(F)>0$ together with ellipticity).

**Conjecture (Halperin, 1977/1983).** For every Serre fibration
$$F \longrightarrow E \xrightarrow{\ p\ } B$$
with $B$ simply connected and fibre $F$ an $F_0$-space, the rational Serre spectral sequence collapses at $E_2$; equivalently the fibration is **TNCZ** (totally non-cohomologous to zero): the restriction $H^*(E;\mathbb{Q})\to H^*(F;\mathbb{Q})$ is surjective, and
$$H^*(E;\mathbb{Q}) \;\cong\; H^*(B;\mathbb{Q})\otimes H^*(F;\mathbb{Q})$$
as $H^*(B;\mathbb{Q})$-modules.

A complete proof must handle all $F_0$-spaces $F$ and all simply connected bases $B$ simultaneously. A disproof requires one explicit $F_0$-space $F$ and one fibration over a simply connected base with a non-trivial differential in the rational Serre spectral sequence — or, by Meier's criterion (§2), a single $F_0$-space whose rational cohomology algebra admits a non-zero derivation of negative degree.

The conjecture is distinct from Halperin's **toral rank conjecture** ($\dim H^*(X;\mathbb{Q}) \ge 2^{\mathrm{rk}_0(X)}$), which is catalogued separately.

## 2. Mathematical Foundations

**Elliptic and pure models.** Work over $\mathbb{Q}$ with Sullivan minimal models. $X$ is *elliptic* if $\dim H^*(X;\mathbb{Q})<\infty$ and $\dim \pi_*(X)\otimes\mathbb{Q}<\infty$. For an elliptic $X$, $\dim \pi_{\mathrm{even}}\otimes\mathbb{Q} \le \dim \pi_{\mathrm{odd}}\otimes\mathbb{Q}$, with equality iff $\chi(X)>0$ iff $H^{\mathrm{odd}}(X;\mathbb{Q})=0$ (Félix–Halperin–Thomas). Such $X$ is an $F_0$-space and its minimal model is **pure**:
$$\big(\Lambda(x_1,\dots,x_n,y_1,\dots,y_n),\, d\big),\qquad |x_i| \text{ even},\ |y_j| \text{ odd},$$
$$d x_i = 0,\qquad d y_j = P_j(x_1,\dots,x_n),$$
where $P_1,\dots,P_n$ is a regular sequence in $\mathbb{Q}[x_1,\dots,x_n]$. Hence
$$H^*(F;\mathbb{Q}) \;=\; \mathbb{Q}[x_1,\dots,x_n]/(P_1,\dots,P_n),$$
a graded **complete intersection**, finite-dimensional, and a Poincaré duality algebra of formal dimension
$$\dim F \;=\; \sum_{j=1}^{n}\big(|P_j|-1\big) \;-\; \sum_{i=1}^{n}\big(|x_i|-1\big)\;+\;\textstyle\sum_i (|x_i|-1)\ \ \text{(equivalently } \sum_j |y_j| - \sum_i(|x_i|-2)\text{)}.$$

**Derivations.** For a graded algebra $A$, let $\mathrm{Der}_{-k}(A)$ be linear maps $\theta:A^*\to A^{*-k}$ with $\theta(ab)=\theta(a)b+(-1)^{k|a|}a\,\theta(b)$. Write $\mathrm{Der}^{<0}(A)=\bigoplus_{k>0}\mathrm{Der}_{-k}(A)$.

**Theorem (Meier 1982; Halperin).** For an $F_0$-space $F$ the following are equivalent:
1. every fibration with fibre $F$ over a simply connected base is TNCZ;
2. $\mathrm{Der}^{<0}\big(H^*(F;\mathbb{Q})\big)=0$;
3. $H^*\big(B\mathrm{aut}_1(F);\mathbb{Q}\big)$ is a free graded-commutative algebra on generators of even degree (equivalently $\pi_{\mathrm{odd}}(B\mathrm{aut}_1 F)\otimes\mathbb{Q}=0$).

This converts a statement about all fibrations into a purely algebraic question about complete intersection algebras. Because $H^*(F;\mathbb{Q})$ is evenly graded, only even negative degrees $-k$ can support non-zero derivations, and a derivation is determined by its values $\theta(x_i)\in H^{|x_i|-k}(F;\mathbb{Q})$ subject to
$$\sum_{i=1}^{n} \frac{\partial P_j}{\partial x_i}\,\theta(x_i) \;=\; 0 \quad\text{in } H^*(F;\mathbb{Q}), \qquad j=1,\dots,n. \tag{$\ast$}$$
So the conjecture asserts: the only solution of the linear system $(\ast)$ in strictly positive degree-drop is the trivial one, i.e. the Jacobian matrix $J=\big(\partial P_j/\partial x_i\big)$ acts injectively on the relevant graded pieces. The determinant $\det J$ is a non-zero socle generator (Scheja–Storch), which is the engine behind all known positive results.

**Universal fibration.** The classifying space $B\mathrm{aut}_1(F)$ carries the universal fibration with fibre $F$; every fibration is pulled back from it, so (1) reduces to the universal case — the route Meier and Shiga–Tezuka exploit.

## 3. History & State of the Art (SOTA)

- **1977–1983.** Stephen Halperin, in *Finiteness in the minimal models of Sullivan* (Trans. AMS, 1977) and explicitly in *Rational homotopy and torus actions* (1985), isolates $F_0$-spaces and conjectures universal collapse. Motivation: the classical theorem that fibrations with fibre a compact homogeneous space $G/T$ (flag manifold) are TNCZ, and Blanchard-type collapse results.
- **1981.** J.-C. Thomas, *Rational homotopy of Serre fibrations*, gives the first general criteria and settles low numbers of generators.
- **1982.** W. Meier proves the derivation criterion and the $B\mathrm{aut}_1$ reformulation — still the definitive translation of the problem.
- **1987.** H. Shiga and M. Tezuka verify the conjecture for essentially all equal-rank homogeneous spaces $G/H$ using a Jacobian/Weyl-invariant argument, plus $p$-torsion control in the exceptional cases.
- **1990s.** G. Lupton, S. Papadima–L. Paunescu, and M. Markl push the algebraic side: monomial complete intersections, "hyperformal" algebras, and low generator counts.
- **2000s–2020s.** The problem is restated in Félix–Halperin–Thomas, *Rational Homotopy Theory* (GTM 205, 2001, §39) and Félix–Oprea–Tanré (2008); connections emerge to formality of fibrations (Amann–Kapovitch, 2012) and to positive-curvature/symmetry-rank problems. No counterexample and no general proof.

## 4. Partial Results / Verified Cases

Confirmed classes (all via $\mathrm{Der}^{<0}H^*(F;\mathbb{Q})=0$):

- **$n \le 3$ generators.** True whenever $H^*(F;\mathbb{Q})=\mathbb{Q}[x_1,\dots,x_n]/(P_1,\dots,P_n)$ has $n\le 3$ (Thomas 1981 for $n\le2$; Lupton 1990 for $n=3$). Partial results exist for $n=4$ under degree restrictions.
- **Equal-rank homogeneous spaces.** $F=G/H$ with $G$ compact connected Lie, $H$ closed connected, $\mathrm{rk}\,G=\mathrm{rk}\,H$ (so $\chi(G/H)>0$): Shiga–Tezuka (1987). Includes all flag manifolds $G/T$, $\mathbb{C}P^n$, quadrics, Grassmannians $U(n+m)/U(n)\times U(m)$, $Sp(n)/U(n)$, and the exceptional cases $E_6/T\cdot Spin(10)$ etc. Their argument requires care when $H$ has simple factors of exceptional type, where torsion primes must be excluded.
- **Monomial / hyperformal relations.** If the regular sequence $(P_1,\dots,P_n)$ can be taken to consist of monomials, or more generally if the algebra is *hyperformal* (relations of "Koszul" shape), the conjecture holds — Papadima–Paunescu (1996). This covers all products $\prod_i \mathbb{C}P^{n_i}$, $\prod_i S^{2m_i}$, and weighted variants.
- **Generators in a single degree.** If all $|x_i|=2$ and the relations are the invariants of a finite reflection group, collapse follows from the classical Borel/flag-manifold computation.
- **Low formal dimension.** All $F_0$-spaces with $\dim H^*(F;\mathbb{Q})$ small (e.g. $\le 6$ over the relevant degree range) are verified by direct linear algebra on $(\ast)$; machine verification of the linear system is routine for fixed generator degrees.
- **Cohomologically Kähler / symplectically toric cases.** Simply connected smooth complete toric varieties and their $\mathbb{Q}$-analogues are $F_0$ with monomial-type relations, hence covered.

## 5. Principal Obstacles

- **Uniformity across all complete intersections.** $(\ast)$ is a family of linear systems whose size grows with $n$ and with the generator degrees. Existing proofs are *degree-bookkeeping* arguments: they succeed when the socle-degree budget forces the only candidate solution to be zero. For $n\ge4$ with wildly different degrees $|x_i|$ the bookkeeping no longer closes.
- **No structural invariant detects negative derivations.** $\mathrm{Der}^{<0}(A)$ is not computed by any known cohomological functor of $A$; it is a kernel, and kernels of graded matrices over Artinian rings are not controlled by Poincaré duality alone. Poincaré duality algebras that are *not* complete intersections can and do admit negative derivations, so the proof must use the complete-intersection hypothesis in an essential way — but no argument uses it beyond the Jacobian socle theorem.
- **Spectral-sequence techniques are too coarse.** Differentials $d_r$ can be non-zero for individual $r$ on non-$F_0$ fibres (e.g. odd spheres), so any argument must be global; there is no filtration or multiplicative extension trick that isolates a single obstruction class.
- **Formality does not suffice.** $F_0$-spaces need not be formal, and formality of $F$ alone is not known to imply collapse; conversely non-formality gives no counterexample mechanism.
- **The universal base is huge.** $B\mathrm{aut}_1(F)$ is rationally computable in principle from the derivation Lie algebra of the model, but that Lie algebra is exactly the unknown — the reformulation is a translation, not a reduction in difficulty.

## 6. The Gap

Proven: $\mathrm{Der}^{<0}(A)=0$ for graded complete intersections $A=\mathbb{Q}[x_1,\dots,x_n]/(P_1,\dots,P_n)$ with $n\le 3$, with monomial/hyperformal relation sequences, or arising as $H^*(G/H;\mathbb{Q})$ for equal-rank pairs.

Open: the same vanishing for an *arbitrary* evenly graded Artinian complete intersection over $\mathbb{Q}$ with $n\ge4$ generators of unrestricted even degrees. Concretely, the missing step is:

> Show that for every regular sequence $P_1,\dots,P_n$ of positive-degree polynomials in evenly graded variables, the Jacobian matrix $J=(\partial P_j/\partial x_i)$, viewed as a map of graded $A$-modules $\bigoplus_i A(-|x_i|) \to \bigoplus_j A(-|P_j|)$, has no kernel element in degrees strictly above $\sum_i|x_i|$-shifted threshold — i.e. no non-trivial syzygy of the Jacobian in negative derivation degree.

Every known proof supplies this only when the degree pattern is rigid enough to force the syzygy module into a range where duality kills it.

## 7. Current Research (as of June 2026)

- **Commutative-algebra reformulation.** Interest in phrasing the conjecture as a statement about the module of syzygies of the Jacobian ideal / the Koszul homology of $(P_1,\dots,P_n)$, connecting to Lefschetz properties (weak and strong Lefschetz for Artinian complete intersections). Groups in Sweden (Stockholm/KTH), Japan (Hokkaido, Kyoto), and Belgium (UCLouvain, Félix's school) pursue this. *(frontier — verify)*
- **Computer verification for $n=4,5$.** Systematic Gröbner-basis sweeps over generator-degree patterns with bounded socle degree, using Macaulay2/Singular, aiming either at a counterexample or at a proof template for $n=4$. *(frontier — verify)*
- **Geometric consequences.** The conjecture is used as a hypothesis in positive-curvature and symmetry-rank arguments (Amann, Kapovitch, and collaborators): collapse for $F_0$ fibres yields Euler-characteristic and formality statements for total spaces of homogeneous fibrations.
- **$B\mathrm{aut}_1$ and mapping spaces.** Work on rational homotopy of self-equivalence spaces (Smith, Yamaguchi, Gatsinzi) tests the conjecture by computing $\pi_*(B\mathrm{aut}_1 F)\otimes\mathbb{Q}$ for structured families.
- **Extensions.** Variants for fibres with $\chi=0$, for non-simply-connected bases, and characteristic-$p$ analogues (where the statement is known to fail) delimit how much of the hypothesis is essential.

## 8. Future Work

- Prove the $n=4$ case in full generality; this is widely regarded as the next decisive test, since it is the first case where degree bookkeeping fails.
- Establish an implication from the **strong Lefschetz property** for Artinian complete intersections to $\mathrm{Der}^{<0}=0$, or show the two are logically independent.
- Find an invariant-theoretic criterion generalising Shiga–Tezuka's Jacobian argument beyond Weyl-group invariants, e.g. for complete intersections arising from finite unitary reflection groups or from Landau–Ginzburg potentials.
- Search deliberately for counterexamples among complete intersections with highly skewed degree patterns (one low-degree generator, several high-degree relations), where the kernel of $J$ is largest.
- Clarify the relation to formality: does formality of $F$ plus $F_0$ imply collapse?

## 9. Key References

- **[Foundational]** S. Halperin. *Finiteness in the minimal models of Sullivan.* Transactions of the American Mathematical Society **230** (1977), 173–199. [DOI](https://doi.org/10.1090/s0002-9947-1977-0461508-8)
- **[Foundational]** S. Halperin. *Rational homotopy and torus actions.* In *Aspects of Topology*, London Math. Soc. Lecture Note Series **93**, Cambridge University Press, 1985, 293–306. [DOI](https://doi.org/10.1017/cbo9781107359925.015)
- **[Foundational]** W. Meier. *Rational universal fibrations and flag manifolds.* Mathematische Annalen **258** (1982), 329–340. [DOI](https://doi.org/10.1007/bf01450686)
- **[Foundational]** J.-C. Thomas. *Rational homotopy of Serre fibrations.* Annales de l'Institut Fourier **31** (1981), no. 3, 71–90. [DOI](https://doi.org/10.5802/aif.838)
- **[SOTA]** H. Shiga, M. Tezuka. *Rational fibrations, homogeneous spaces with positive Euler characteristics and Jacobians.* Annales de l'Institut Fourier **37** (1987), no. 1, 81–106. [DOI](https://doi.org/10.5802/aif.1078)
- **[SOTA]** G. Lupton. *Note on a conjecture of Stephen Halperin's.* In *Topology and Combinatorial Group Theory*, Lecture Notes in Mathematics **1440**, Springer, 1990, 148–163. [DOI](https://doi.org/10.1007/bfb0084459)
- **[SOTA]** S. Papadima, L. Paunescu. *Reduced weighted complete intersection and derivations.* Journal of Algebra **183** (1996), 595–604. [DOI](https://doi.org/10.1006/jabr.1996.0234)
- **[SOTA]** M. Markl. *Towards one conjecture on collapsing of the Serre spectral sequence.* Rendiconti del Circolo Matematico di Palermo, Serie II, Supplemento **22** (1990), 151–159.
- **[Recent]** M. Amann, V. Kapovitch. *On fibrations with formal elliptic fibers.* Advances in Mathematics **231** (2012), 2048–2068. [DOI](https://doi.org/10.1016/j.aim.2012.07.022)
- **[Survey]** G. Lupton. *Variations on a conjecture of Halperin.* In *Homotopy and Geometry*, Banach Center Publications **45**, Polish Academy of Sciences, 1998, 115–135. [DOI](https://doi.org/10.4064/-45-1-115-135)
- **[Textbook]** Y. Félix, S. Halperin, J.-C. Thomas. *Rational Homotopy Theory.* Graduate Texts in Mathematics **205**, Springer, 2001 (Sections 32, 38–39).
- **[Textbook]** Y. Félix, J. Oprea, D. Tanré. *Algebraic Models in Geometry.* Oxford Graduate Texts in Mathematics **17**, Oxford University Press, 2008.

## 10. Worked Example / Concrete Special Case

**Case: $F = SU(3)/T^2$, the full complex flag manifold $\mathrm{Fl}(3)$.**

Its rational cohomology is
$$H^*(F;\mathbb{Q}) \;=\; \mathbb{Q}[x_1,x_2,x_3]/(e_1,e_2,e_3),\qquad |x_i|=2,$$
with $e_1=x_1+x_2+x_3$, $e_2=\sum_{i<j}x_ix_j$, $e_3=x_1x_2x_3$ the elementary symmetric polynomials — a complete intersection of dimension $3!=6$, so $F$ is an $F_0$-space of formal dimension $6$ ($\chi(F)=6$).

*Step 1 — only degree $-2$ matters.* A derivation $\theta$ of degree $-2k$ is determined by $\theta(x_i)\in H^{2-2k}$. For $k\ge2$ this group is $0$, so $\theta=0$. Only $k=1$ survives: $\theta(x_i)=a_i\in\mathbb{Q}$.

*Step 2 — impose the relations.* Applying $\theta$ to $e_1=0$:
$$a_1+a_2+a_3=0.$$
Applying $\theta$ to $e_2$, and writing $s=x_1+x_2+x_3$:
$$\theta(e_2)=\sum_{i<j}\big(a_ix_j+a_jx_i\big)=\sum_{i=1}^{3}a_i\,(s-x_i)=-\sum_{i=1}^{3}a_ix_i,$$
using $s=e_1=0$ in $H^*$. So we need $a_1x_1+a_2x_2+a_3x_3=0$ in $H^2$.

*Step 3 — solve.* $H^2(F;\mathbb{Q})$ is $2$-dimensional, spanned by $x_1,x_2,x_3$ with the single relation $x_1+x_2+x_3=0$. Hence $\sum a_ix_i=0$ forces $(a_1,a_2,a_3)=c\,(1,1,1)$ for some $c\in\mathbb{Q}$. Combined with Step 2's $a_1+a_2+a_3=0$ we get $3c=0$, so $c=0$ and $\theta=0$. (The relation $e_3$ gives no further constraint.)

*Conclusion.* $\mathrm{Der}^{<0}(H^*(F;\mathbb{Q}))=0$, so by Meier's criterion **every** fibration $SU(3)/T^2 \to E \to B$ over a simply connected base satisfies $H^*(E;\mathbb{Q})\cong H^*(B;\mathbb{Q})\otimes H^*(F;\mathbb{Q})$. In particular for the universal $SU(3)$-bundle, $E=BT^2$, $B=BSU(3)$:
$$H^*(BT^2;\mathbb{Q})=\mathbb{Q}[x_1,x_2]\;\cong\;\mathbb{Q}[c_2,c_3]\otimes \mathbb{Q}[x_1,x_2,x_3]/(e_1,e_2,e_3),$$
a Poincaré-series identity $\frac{1}{(1-t^2)^2}=\frac{1}{(1-t^4)(1-t^6)}\cdot\frac{(1-t^2)(1-t^4)(1-t^6)}{(1-t^2)^3}$, which checks out.

**Why the hypothesis $H^{\mathrm{odd}}=0$ is essential.** Take $F=S^3$, elliptic but with $\chi=0$. Then $H^*(S^3;\mathbb{Q})=\Lambda(y)$, $|y|=3$, and $\theta(y)=1$ defines a non-zero derivation of degree $-3$. Correspondingly the Hopf fibration $S^3\to S^7\to S^4$ has $d_4(y)=$ the generator of $H^4(S^4;\mathbb{Q})$, and $H^*(S^7;\mathbb{Q})\ne H^*(S^4;\mathbb{Q})\otimes H^*(S^3;\mathbb{Q})$. The conjecture is exactly the assertion that this failure mode never occurs once the fibre has positive Euler characteristic.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*