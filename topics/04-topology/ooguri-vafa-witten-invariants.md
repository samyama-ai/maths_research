---
id: 04-topology/ooguri-vafa-witten-invariants
title: "Ooguri-Vafa-Witten Invariants"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ooguri-Vafa-Witten Invariants

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/ooguri-vafa-witten-invariants` · **Status:** open

## 1. Problem Statement / Conjecture

Large-$N$ dualities predict that quantum-topological partition functions are generating series of *integer* counts of BPS states, and that those generating series carry modular structure. Two families of invariants extracted this way are collectively at issue here:

- **Ooguri–Vafa (LMOV) invariants** $N_{R,g,Q}$ of a link $\mathcal{L}\subset S^3$, obtained by reorganizing the colored HOMFLY-PT polynomials of $\mathcal{L}$ into open Gromov–Witten / M2-brane counts on the resolved conifold.
- **Vafa–Witten invariants** $VW_{r,c_1,c_2}(X)$ of a four-manifold or projective surface $X$, obtained from the partition function of topologically twisted $\mathcal{N}=4$ super Yang–Mills.

**Problem (integrality and finiteness, LMOV).** For every link $\mathcal{L}$ and every partition (colour) $R$, the reformulated invariant $f_R(q,\lambda)$ defined in §2 lies in
$$f_R(q,\lambda)\in \mathbb{Z}\big[(q^{1/2}-q^{-1/2})^{\pm 1}\big]\big[\lambda^{\pm 1/2}\big],$$
i.e. $f_R=\sum_{g\ge 0}\sum_{Q}N_{R,g,Q}\,(q^{1/2}-q^{-1/2})^{2g-1}\lambda^{Q}$ with all $N_{R,g,Q}\in\mathbb{Z}$, only finitely many nonzero, and no pole of order $>1$ at $q=1$. A complete solution must additionally identify $N_{R,g,Q}$ with a count of holomorphic curves (or a Betti/DT number of a moduli space of BPS states), not merely prove the arithmetic statement.

**Companion problem (S-duality modularity).** For the mathematically defined Vafa–Witten invariants of a surface $X$, the generating function $Z_r(X;q)=\sum_{c_2}VW_{r,c_1,c_2}(X)\,q^{c_2-\frac{r-1}{2r}c_1^2-\frac{r\chi(X)}{24}}$ is a (mock) modular form of weight $-\chi(X)/2$ for a congruence subgroup, transforming under $\tau\mapsto-1/(r\tau)$ into the generating function of the $\mathrm{SU}(r)/\mathbb{Z}_r$ theory. A complete solution must prove this for all $r$ and all $X$ with $b_1=0$, including the non-trivial ("monopole"/non-instanton) branches of the moduli space.

Disproof would consist of a single link, colour and $(g,Q)$ with $N_{R,g,Q}\notin\mathbb{Z}$ or infinitely many nonzero, or a surface whose Vafa–Witten series fails the transformation law.

## 2. Mathematical Foundations

Let $\mathcal{L}$ be an $L$-component framed oriented link. Let $\langle W_R(\mathcal{L})\rangle$ be the unreduced quantum $\mathfrak{gl}_N$ invariant coloured by $R=(R_1,\dots,R_L)$, expressed in the HOMFLY-PT variables $q=e^{g_s}$, $\lambda=q^{N}$. Assemble the generating function over auxiliary $U(\infty)$ holonomies $V_1,\dots,V_L$:
$$Z(V)=\sum_{R}\langle W_R(\mathcal{L})\rangle\prod_{\alpha=1}^{L}\operatorname{Tr}_{R_\alpha}V_\alpha ,\qquad F=\log Z .$$
The **Ooguri–Vafa conjecture** states that $F$ has the "free energy of an M2-brane gas" form
$$F(V)=\sum_{d\ge 1}\sum_{R}\frac{1}{d}\,f_R\!\left(q^{d},\lambda^{d}\right)\prod_\alpha\operatorname{Tr}_{R_\alpha}V_\alpha^{d},$$
which defines the **reformulated invariants** $f_R$ by Möbius inversion,
$$f_R(q,\lambda)=\sum_{d\ge1}\frac{\mu(d)}{d}\sum_{\vec{R}} \big(\text{Adams-type character coefficients}\big)\,F_{\vec R}(q^d,\lambda^d),$$
a priori only in $\mathbb{Q}(q^{1/2},\lambda^{1/2})$. The conjecture is that $f_R$ is in fact
$$f_R(q,\lambda)=\sum_{g\ge0}\sum_{Q\in\frac12\mathbb{Z}}N_{R,g,Q}\;(q^{1/2}-q^{-1/2})^{2g-1}\lambda^{Q},\qquad N_{R,g,Q}\in\mathbb{Z},$$
finitely supported. Geometrically $N_{R,g,Q}$ counts BPS M2-branes of genus $g$ and relative homology class $Q$ ending on the Lagrangian conormal $L_{\mathcal{L}}\subset T^*S^3$, transported through the conifold transition to the resolved conifold $\mathcal{O}(-1)^{\oplus2}\to\mathbb{P}^1$.

Equivalently, in the symmetric-colour sector one has the product form
$$Z(V)=\prod_{Q,g}\prod_{k}\left(1-q^{k}\lambda^{Q}\,\text{(monomials)}\right)^{\pm N},$$
the open analogue of the Gopakumar–Vafa product for closed topological strings.

On the four-dimensional side, for a smooth projective surface $X$ with $H^{0,1}=0$, Tanaka–Thomas define $VW_{r,c_1,c_2}(X)$ as a $\mathbb{C}^*$-localized virtual count on the moduli space of Gieseker-stable Higgs pairs $(E,\phi)$, $\phi\in\operatorname{Hom}(E,E\otimes K_X)$, with $\operatorname{rk}E=r$. The moduli space splits into an *instanton branch* ($\phi=0$, giving $e^{\mathrm{vir}}$ of the sheaf moduli space) and a *monopole branch* ($\phi\neq0$). The predicted modularity for $r=2$, $b_1=0$, $p_g>0$ reads schematically
$$Z_2(X;\tau)\;=\;\text{(mock modular form of weight }-\tfrac{\chi(X)}{2}),\qquad Z_2(-1/\tau)\sim \tau^{-\chi/2}\,Z_2^{\mathrm{SO(3)}}(\tau).$$

## 3. History & State of the Art (SOTA)

- **1994.** Vafa and Witten propose the $\mathcal{N}=4$ twist and compute partition functions on $K3$ and $\mathbb{P}^2$, matching Euler characteristics of instanton moduli spaces to modular forms — the first "strong coupling test of S-duality".
- **1998–99.** Gopakumar–Vafa reinterpret closed topological string amplitudes as integer BPS counts; Gopakumar–Vafa large-$N$ duality relates $U(N)$ Chern–Simons on $S^3$ to the resolved conifold.
- **1999–2000.** Ooguri and Vafa extend the duality to Wilson loops, predicting integrality of $N_{R,g,Q}$ for knots. Labastida–Mariño–Vafa sharpen the statement to arbitrary colours and links; hence "LMOV conjecture".
- **2001–2010.** Extensive verification for torus knots and small colours (Labastida–Mariño; Lin–Zheng via Hecke-algebra character formulas). Liu–Peng give a proof of the LMOV integrality and pole structure for all links via a Chern–Simons cabling/Hecke-algebra argument (*J. Diff. Geom.* 2010).
- **2013–2016.** Diaconescu–Shende–Vafa give an algebro-geometric model (stable pairs on the resolved conifold with Lagrangian filling) for algebraic knots; Maulik proves the Oblomkov–Shende conjecture, expressing HOMFLY-PT of links of plane curve singularities via Hilbert schemes — the strongest *geometric* interpretation of $N_{R,g,Q}$ to date.
- **2017–2020.** Knots–quivers correspondence (Kucharski–Reineke–Stošić–Sułkowski) converts LMOV integrality into Donaldson–Thomas integrality for symmetric quivers, where Efimov's theorem applies. Tanaka–Thomas construct Vafa–Witten invariants algebraically; Göttsche–Kool compute and match the $r=2,3$ modular predictions on many surfaces.
- **2019–present.** Ekholm–Shende's skein-valued curve counting places the open BPS integers inside the HOMFLY-PT skein module of the filling Lagrangian, giving integrality "for free" once the count is constructed.

## 4. Partial Results / Verified Cases

- **All links, arithmetic integrality:** Liu–Peng (2010) prove $N_{R,g,Q}\in\mathbb{Z}$, finiteness, and the pole order $\le 1$ at $q=1$, for every link in $S^3$ and every colour. The proof is combinatorial/representation-theoretic; it does not produce the curve counts.
- **Torus knots $T_{p,q}$:** closed formulas for $f_R$ from the Rosso–Jones formula; integrality checked symbolically for all $R$ with $|R|\le 6$ and verified structurally by Labastida–Mariño.
- **Algebraic knots (links of plane curve singularities):** Maulik (2016) proves the HOMFLY-PT = stable-pairs statement in the fundamental colour, giving the geometric meaning of $N_{\square,g,Q}$ for this class.
- **Rational (2-bridge) links:** Stošić–Wedrich establish the knots–quivers correspondence, hence LMOV integrality *with geometric/DT meaning* for all symmetric colours.
- **Unknot and Hopf link:** complete closed-form BPS spectra, finitely many nonzero $N$ (see §10).
- **Vafa–Witten side:** rank $2$ and rank $3$ instanton-branch generating functions computed and matched to the physics prediction for $\mathbb{P}^2$, $\mathbb{P}^1\times\mathbb{P}^1$, $K3$, and many surfaces with $p_g>0$ (Göttsche–Kool). Monopole-branch contributions computed for $r=2$ by Laarakker via Seiberg–Witten-type universality.

## 5. Principal Obstacles

- **No general moduli space for open BPS states.** $N_{R,g,Q}$ should be a Betti number or DT-type count on a moduli of M2-branes ending on $L_{\mathcal{L}}$. Outside algebraic knots no such space is constructed, so integrality proofs remain arithmetic accidents rather than dimension counts.
- **Open Gromov–Witten invariants are not canonically defined.** Boundary conditions on a Lagrangian require choices (framing, obstruction bundles, multiple covers); the resulting rational numbers depend on perturbation data. Ionel–Parker's proof of closed GV integrality uses a symplectic cluster/deformation argument that has no known Lagrangian-boundary analogue.
- **Colour growth.** Colored HOMFLY-PT for $R$ with $|R|=n$ requires $\mathrm{U}_q(\mathfrak{sl}_N)$ intertwiners of exponentially growing rank; even $q$-holonomicity (Garoufalidis–Lauda–Lê) does not yield uniform control of $f_R$ as $|R|\to\infty$.
- **Non-compactness on the Vafa–Witten side.** The Higgs-pair moduli space is non-compact; invariants are defined by $\mathbb{C}^*$-localization, and the monopole branch is a virtually singular, stratified space whose contributions are known only through conjectural universality in Chern and Seiberg–Witten data.
- **Mock modularity.** For $p_g=0$ the predicted transformation is genuinely mock (non-holomorphic completion required); there is no general machinery producing mock modular forms from virtual sheaf counts.

## 6. The Gap

Integrality is proven; **meaning is not**. The gap has two edges:

1. *Open side:* between Liu–Peng's statement "$N_{R,g,Q}\in\mathbb{Z}$" and the assertion "$N_{R,g,Q}=\pm\dim$ of a BPS cohomology / an enumerative count of embedded curves". Closing it requires either (a) a construction of open Gromov–Witten theory for conormal Lagrangians that is deformation-invariant and skein-valued for *all* knots — Ekholm–Shende give the framework but a full construction covering non-algebraic knots is unfinished — or (b) an extension of the knots–quivers correspondence from rational links to all links, which would import Efimov's DT positivity/integrality wholesale.
2. *Four-dimensional side:* between computed instanton-branch series on specific surfaces and modularity of the *total* invariant for arbitrary $r$ and arbitrary $X$. The precise missing step is a universality theorem for monopole-branch contributions in rank $r\ge 4$ plus a proof that the resulting series lies in a finite-dimensional space of (mock) modular forms.

## 7. Current Research (as of June 2026)

- **Skein-valued curve counting.** Ekholm–Shende and collaborators (Uppsala, Berkeley, IHÉS) develop skein-valued open GW invariants; recent work extends the recursion ("skein valued mirror symmetry") to toric branes and to knot conormals beyond the algebraic case. *(frontier — verify)*
- **Knots–quivers beyond rational links.** Warsaw (Sułkowski), Lisbon (Stošić) and Bonn groups push the correspondence to arborescent and Montesinos links, and study non-uniqueness of the quiver. Multi-cover skein relations are a leading tool. *(frontier — verify)*
- **HOMFLY homology and refined BPS.** Gorsky, Nawata, Oblomkov, Rasmussen, Shende: categorified $N_{R,g,Q}$ as Poincaré polynomials of triply-graded homology; positivity conjectures for algebraic knots.
- **Vafa–Witten theory.** Tanaka–Thomas, Göttsche–Kool, Laarakker, Jiang: refined and $K$-theoretic Vafa–Witten invariants, higher rank, surfaces with $\mathbb{C}^*$-actions, and links to Donaldson invariants via the Mochizuki formula.
- **Cohomological Hall algebras** (Kontsevich–Soibelman school, Davison, Meinhardt) supply the structural source of integrality that both sides ultimately want.

## 8. Future Work

- Construct BPS/DT moduli spaces for knot conormals in general, giving a cohomological definition of $N_{R,g,Q}$ with an a priori integrality proof.
- Prove that every link admits a (possibly non-unique) symmetric quiver realizing its LMOV invariants; classify the ambiguity.
- Extend Maulik's stable-pairs theorem from the fundamental colour to all symmetric and then all colours.
- Prove finiteness and effective bounds on the support of $N_{R,g,Q}$ in terms of braid length or genus of the knot.
- Establish monopole-branch universality for Vafa–Witten invariants in all ranks and derive modularity from wall-crossing / Mochizuki-type formulas rather than case-by-case computation.

## 9. Key References

- **[Foundational]** C. Vafa, E. Witten. *A strong coupling test of S-duality.* Nuclear Physics B **431** (1994), 3–77.
- **[Foundational]** H. Ooguri, C. Vafa. *Knot invariants and topological strings.* Nuclear Physics B **577** (2000), 419–438.
- **[Foundational]** R. Gopakumar, C. Vafa. *M-theory and topological strings I, II.* Preprints hep-th/9809187, hep-th/9812127 (1998).
- **[Foundational]** J. M. F. Labastida, M. Mariño, C. Vafa. *Knots, links and branes at large N.* JHEP **2000**, no. 11, 007.
- **[Foundational]** J. M. F. Labastida, M. Mariño. *A new point of view in the theory of knot and link invariants.* Journal of Knot Theory and Its Ramifications **11** (2002), 173–197.
- **[SOTA]** K. Liu, P. Peng. *Proof of the Labastida–Mariño–Ooguri–Vafa conjecture.* Journal of Differential Geometry **85** (2010), 479–525.
- **[SOTA]** D.-E. Diaconescu, V. Shende, C. Vafa. *Large N duality, Lagrangian cycles, and algebraic knots.* Communications in Mathematical Physics **319** (2013), 813–863.
- **[SOTA]** D. Maulik. *Stable pairs and the HOMFLY polynomial.* Inventiones Mathematicae **204** (2016), 787–831.
- **[SOTA]** P. Kucharski, M. Reineke, M. Stošić, P. Sułkowski. *Knots-quivers correspondence.* Advances in Theoretical and Mathematical Physics **23** (2019), 1849–1902.
- **[SOTA]** A. I. Efimov. *Cohomological Hall algebra of a symmetric quiver.* Compositio Mathematica **148** (2012), 1133–1146.
- **[SOTA]** M. Stošić, P. Wedrich. *Rational links and DT invariants of quivers.* International Mathematics Research Notices (2021).
- **[SOTA]** T. Ekholm, V. Shende. *Skeins on branes.* Preprint arXiv:1901.08027 (2019).
- **[SOTA]** Y. Tanaka, R. P. Thomas. *Vafa–Witten invariants for projective surfaces I: stable case.* Journal of Algebraic Geometry **29** (2020), 603–668; *II: semistable case.* Pure and Applied Mathematics Quarterly **13** (2017), 517–562.
- **[SOTA]** L. Göttsche, M. Kool. *Virtual refinements of the Vafa–Witten formula.* Communications in Mathematical Physics **376** (2020), 1–49.
- **[Related]** E. Ionel, T. Parker. *The Gopakumar–Vafa formula for symplectic manifolds.* Annals of Mathematics **187** (2018), 1–64.
- **[Related]** X.-S. Lin, H. Zheng. *On the Hecke algebras and the colored HOMFLY polynomial.* Transactions of the AMS **362** (2010), 1–18.
- **[Survey]** M. Mariño. *Chern–Simons Theory, Matrix Models, and Topological Strings.* Oxford University Press, 2005.

## 10. Worked Example / Concrete Special Case

**Fundamental colour $R=\square$.** For a single knot and one box, the Möbius inversion is trivial: $f_\square=\langle W_\square\rangle$, the unreduced HOMFLY-PT. Write $z=q^{1/2}-q^{-1/2}$, $a=\lambda^{1/2}$, with skein relation $aP(L_+)-a^{-1}P(L_-)=zP(L_0)$ and $P(\text{unknot})=1$; the unreduced invariant is $\langle W_\square\rangle=\frac{a-a^{-1}}{z}P$.

**Unknot.** $P=1$, so
$$f_\square=\frac{\lambda^{1/2}-\lambda^{-1/2}}{z}=z^{-1}\lambda^{1/2}-z^{-1}\lambda^{-1/2}.$$
Matching $\sum N_{\square,g,Q}z^{2g-1}\lambda^Q$: $N_{\square,0,1/2}=1$, $N_{\square,0,-1/2}=-1$, all others zero. Two integers, finite support, simple pole at $q=1$. ✔

**Trefoil $3_1$.** Its reduced HOMFLY-PT is $P=2a^{-2}-a^{-4}+a^{-2}z^{2}$ (the mirror image is obtained by $\lambda\mapsto\lambda^{-1}$). Then
$$f_\square=\frac{a-a^{-1}}{z}\left(2a^{-2}-a^{-4}+a^{-2}z^{2}\right).$$
Expanding with $a^{2}=\lambda$:
$$(a-a^{-1})(2a^{-2}-a^{-4})=2\lambda^{-1/2}-3\lambda^{-3/2}+\lambda^{-5/2},\qquad (a-a^{-1})a^{-2}=\lambda^{-1/2}-\lambda^{-3/2}.$$
Hence
$$f_\square=z^{-1}\left(2\lambda^{-1/2}-3\lambda^{-3/2}+\lambda^{-5/2}\right)+z\left(\lambda^{-1/2}-\lambda^{-3/2}\right),$$
so the nonzero BPS invariants are
$$N_{\square,0,-1/2}=2,\quad N_{\square,0,-3/2}=-3,\quad N_{\square,0,-5/2}=1,\quad N_{\square,1,-1/2}=1,\quad N_{\square,1,-3/2}=-1 .$$
All five are integers; the support is finite ($g\le1$, $-5/2\le Q\le-1/2$); the pole at $z=0$ has order exactly $1$. This is precisely what LMOV asserts, and what the conjecture claims persists for every colour $R$ and every link.

The content of the open problem is visible here: nothing in the computation *explains* why $2,-3,1,1,-1$ are integers. The conjectural explanation is that $|N_{\square,g,Q}|$ counts genus-$g$ holomorphic curves in the resolved conifold with boundary on the trefoil conormal in relative class $Q$ — for the trefoil (an algebraic knot) Maulik's theorem supplies such a count via Hilbert schemes of the cusp singularity $x^2=y^3$; for a generic hyperbolic knot no such geometric account exists.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*