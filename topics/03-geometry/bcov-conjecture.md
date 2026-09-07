---
id: 03-geometry/bcov-conjecture
title: "BCOV Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# BCOV Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/bcov-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Bershadsky, Cecotti, Ooguri and Vafa (1993–94) predicted that the higher-genus free energies of the topological B-model on a Calabi–Yau threefold are computed by Ray–Singer analytic torsion and satisfy a recursive **holomorphic anomaly equation**, and that under mirror symmetry these B-model quantities reproduce the higher-genus Gromov–Witten invariants of the mirror. The conjecture splits into three statements, all still open in full generality.

- **(BCOV-1, genus one / arithmetic form).** For a mirror pair $(X,\check X)$ of Calabi–Yau $n$-folds, the **BCOV invariant** $\tau_{\mathrm{BCOV}}$ — a real-valued birational invariant built from the Ray–Singer torsions of $\Omega^p_X$ — of the mirror family $\check X_z$, expanded at the large complex structure limit $z\to 0$ in the canonical coordinate $t$, equals the genus-one Gromov–Witten generating function $F_1(q)$, $q=e^{2\pi i t}$, of $X$ up to an explicit elementary factor.
- **(BCOV-2, holomorphic anomaly).** The genus-$g$ B-model potentials $\mathcal F_g$, $g\ge 2$, are non-holomorphic sections over the moduli space $\mathcal M$ of complex structures satisfying the anomaly recursion in §2, are polynomial in a finite set of generators (Yamaguchi–Yau finite generation), and their holomorphic limits equal the genus-$g$ Gromov–Witten potentials of the mirror.
- **(BCOV-3, integrality).** The resulting invariants are governed by integer Gopakumar–Vafa BPS counts.

A complete resolution means: for a general class of Calabi–Yau threefolds (not one hypersurface at a time), a mathematical construction of $\mathcal F_g$ with proofs of the anomaly equation, the boundary conditions ("gap condition" at conifold points, orbifold/Castelnuovo constancy), and mirror identification with GW theory. A disproof would exhibit a Calabi–Yau threefold where the torsion-side and GW-side series differ.

## 2. Mathematical Foundations

Let $X$ be a compact Kähler manifold of dimension $n$ with $\omega$ a Kähler form and $\Delta_{p,q}$ the Dolbeault Laplacian on $A^{p,q}(X)$. The **BCOV torsion** is the weighted alternating product of zeta-regularized determinants
$$
\tau_{\mathrm{BCOV}}(X,\omega)\;=\;\prod_{p,q\ge 0}\bigl(\det{}'\Delta_{p,q}\bigr)^{(-1)^{p+q}\,p\,q}.
$$
For $X$ Calabi–Yau ($K_X\cong\mathcal O_X$, $h^{i,0}=0$ for $0<i<n$) with holomorphic volume form $\eta$, one normalizes by the $L^2$-norm $\|\eta\|^2_{L^2}=\int_X \eta\wedge\bar\eta\,/\,\mathrm{Vol}(X,\omega)$-type factors and by $\mathrm{Vol}(X,\omega)^{\chi(X)/12}$ to obtain a number
$$
\tau_{\mathrm{BCOV}}(X)\in\mathbb R_{>0}
$$
independent of $\omega$ (Fang–Lu–Yoshikawa for $n=3$; Eriksson–Freixas i Montplet–Mourougane in all dimensions). Its variation is controlled by the Bismut–Gillet–Soulé anomaly formula and by Quillen metrics on determinant lines $\lambda(\Omega^p_X)$.

On the B-model side, let $\mathcal M$ be the moduli of complex structures on $\check X$, with Weil–Petersson metric $G_{i\bar j}=\partial_i\partial_{\bar j}K$, Yukawa coupling $C_{ijk}=\int_{\check X}\eta\wedge\nabla_i\nabla_j\nabla_k\eta$, and $\bar C^{jk}_{\;\bar i}=e^{2K}G^{j\bar j}G^{k\bar k}\overline{C_{\bar i\bar j\bar k}}$. The **holomorphic anomaly equations** are
$$
\bar\partial_{\bar i}\,\partial_j\mathcal F_1=\tfrac12 C_{jkl}\,\bar C^{kl}_{\;\bar i}-\Bigl(\tfrac{\chi(\check X)}{24}-1\Bigr)G_{j\bar i},
$$
$$
\bar\partial_{\bar i}\mathcal F_g=\tfrac12\,\bar C^{jk}_{\;\bar i}\Bigl(D_jD_k\mathcal F_{g-1}+\sum_{h=1}^{g-1}D_j\mathcal F_h\,D_k\mathcal F_{g-h}\Bigr),\qquad g\ge 2 ,
$$
where $D_j$ is the covariant derivative on the relevant tensor power of the vacuum line bundle. Genus-one integrates to
$$
\mathcal F_1=\log\Bigl(\|\eta\|^{\,\frac{\chi}{12}-3-h^{1,1}}\,\tau_{\mathrm{BCOV}}^{\,-1/2}\Bigr)\quad\text{(up to normalization)} .
$$
On the A-model side, with Kähler parameter $t$ and $q=e^{2\pi i t}$,
$$
F_1(q)=-\frac{2\pi i\,t}{24}\int_X c_2(X)\wedge H+\sum_{d\ge1}\Bigl(\tfrac{1}{12}n^{0}_d+n^{1}_d\Bigr)\sum_{k\ge1}\frac{q^{kd}}{k},
$$
$n^{g}_d$ the Gopakumar–Vafa invariants. **BCOV-1** is the assertion that the holomorphic limit of $\mathcal F_1$ on the mirror family equals $F_1(q)$ after the mirror map $z\mapsto t(z)$.

The key algebraic input to **BCOV-2** is **Yamaguchi–Yau finite generation**: for the quintic, each $\mathcal F_g$ ($g\ge2$) is a polynomial of degree $3g-3$ in generators $A_p=\theta^p\varpi_0/\varpi_0$, $B=\theta t$ and the propagator, with rational-function coefficients in $z$ with poles only at $z=0$ and the conifold $z=5^{-5}$.

## 3. History & State of the Art (SOTA)

- **1993–94.** Bershadsky–Cecotti–Ooguri–Vafa, *Kodaira–Spencer theory of gravity* (Comm. Math. Phys. 165, 1994) and the earlier Nucl. Phys. B letter, derive the anomaly equations and tabulate genus-1 and genus-2 quintic instanton numbers.
- **1998–2004.** Fang–Lu, and Yoshikawa, put the torsion side on rigorous footing; Yamaguchi–Yau (2004) establish the polynomial ring structure.
- **2007–08.** Huang–Klemm–Quackenbush integrate the quintic anomaly equation to $g=51$ using the conifold gap condition — a computation, not a proof of the underlying recursion.
- **2008–09.** Fang–Lu–Yoshikawa (J. Differential Geom. 80, 2008) prove BCOV-1 for the quintic mirror; Zinger (J. Amer. Math. Soc. 22, 2009) computes the genus-one GW invariants of Calabi–Yau hypersurfaces and matches the BCOV prediction.
- **2018–21.** Chang–Guo–Li (Ann. of Math. 194, 2021) prove the polynomial structure of the quintic GW potential; Guo–Janda–Ruan and Chang–Guo–Li prove the holomorphic anomaly equations for the quintic.
- **2021–22.** Eriksson–Freixas i Montplet–Mourougane define BCOV invariants in all dimensions (Duke Math. J. 170, 2021) and prove genus-one mirror symmetry for Calabi–Yau hypersurfaces in projective space in every dimension (Forum of Math. Pi 10, 2022).

## 4. Partial Results / Verified Cases

| Case | Statement proved | Source |
|---|---|---|
| Quintic threefold $X_5\subset\mathbb P^4$ | BCOV-1 (torsion = $F_1$) | Fang–Lu–Yoshikawa 2008 |
| CY hypersurfaces $X_{n+2}\subset\mathbb P^{n+1}$, all $n$ | BCOV-1 in higher dimension | Eriksson–Freixas–Mourougane 2022 |
| Quintic threefold | holomorphic anomaly eq. for all $g$; polynomiality | Chang–Guo–Li 2021; Guo–Janda–Ruan |
| Quintic | explicit $\mathcal F_g$ up to $g=51$ | Huang–Klemm–Quackenbush 2009 |
| Local CY ($K_{\mathbb P^2}$, $K_{\mathbb P^1\times\mathbb P^1}$, toric local) | anomaly equations, all genus | Lho–Ruan; Fang–Liu–Zong |
| Elliptic curve ($n=1$) | full higher-genus B-model = mirror of GW | Dijkgraaf; Costello–Li |
| Abelian surfaces, K3$\times$elliptic, Borcea–Voisin | torsion invariants computed in closed form | Yoshikawa 2004, 2013; Lu–Yoshikawa |
| Blow-ups, birational CY pairs | $\tau_{\mathrm{BCOV}}$ is a birational invariant | Y. Zhang 2022; Fu–Zhang |
| Complete intersections in $\mathbb P^n$ | genus-one mirror theorem | Popa; Zinger |

Numerically the genus-1 quintic prediction $n^1_d=0,0,609250,3721431625,12129909700200$ for $d=1,\dots,5$ is confirmed by algebraic-geometry counts of elliptic curves for $d\le 5$.

## 5. Principal Obstacles

- **No general geometric definition of $\mathcal F_g$.** Higher-genus B-model potentials exist as solutions to a recursion with boundary conditions, not as invariants attached functorially to a family. Costello–Li's quantum BCOV theory gives a BV-quantization construction but proving its finiteness and mirror-matching beyond the elliptic curve is unresolved.
- **Non-holomorphy.** $\mathcal F_g$ is a $C^\infty$ section; the "holomorphic limit" is a choice of polarization near a boundary point. Comparing two limits requires control of the Hodge-theoretic degeneration at every boundary stratum — currently only known for one-parameter families with a single conifold point.
- **Boundary conditions are not intrinsic.** The anomaly equation determines $\mathcal F_g$ only up to a holomorphic ambiguity $f_g(z)$ with $3g-3$ unknown coefficients. Fixing $f_g$ uses the conifold gap and Castelnuovo vanishing — physical inputs without general proof.
- **Torsion is analytic, GW theory is enumerative.** Analytic torsion is controlled by Bismut–Gillet–Soulé arithmetic Riemann–Roch; GW invariants by virtual localization on moduli of stable maps. There is no common framework, so each match is engineered case by case.
- **Localization does not scale in genus.** Genus-$g$ virtual localization on quasimaps produces graph sums whose complexity grows super-exponentially; the Chang–Guo–Li/Guo–Janda–Ruan proofs use MSP (Mixed-Spin-P fields) and $\mathrm{NMSP}$ degeneration tailored to the quintic's $\mathbb C^*$-geometry.
- **Multi-parameter moduli.** For $h^{1,1}>1$ the propagator ambiguity and the structure of the boundary divisor complicate finite generation; no general finite-generation theorem exists.

## 6. The Gap

Proven: BCOV-1 for hypersurfaces and complete intersections in projective space; BCOV-2 for the quintic and a list of local/toric geometries. Conjectured: both statements for an arbitrary compact Calabi–Yau threefold with a mirror family, in particular for $h^{1,1}>1$ and for non-toric constructions (e.g. Pfaffian and Gushel–Mukai Calabi–Yaus, rigid or non-simply-connected CYs where the mirror is not a family of CY manifolds).

The precise missing step is a **construction of $\mathcal F_g$ intrinsic to the variation of Hodge structure**, together with a degeneration formula computing its asymptotics at an arbitrary boundary point of $\overline{\mathcal M}$, strong enough to pin down $f_g$ without physical input. Equivalently: extend the Duke/Forum-Pi package (BCOV invariants + Hodge-theoretic degeneration) from genus one to all genera.

## 7. Current Research (as of June 2026)

- **Hodge-theoretic torsion school** (Eriksson, Freixas i Montplet, Mourougane; Yoshikawa, Tokyo): extend BCOV invariants to singular and open Calabi–Yaus, and to the arithmetic setting via Arakelov theory. Program to interpret $\tau_{\mathrm{BCOV}}$ as a Quillen metric on a Deligne pairing over $\overline{\mathcal M}$.
- **NMSP / MSP school** (Chang, HKUST; Guo, Peking; Jun Li, Shanghai; Janda, Ruan, Michigan/IASM): push the quintic techniques to complete intersections and to $h^{1,1}>1$ targets. *(frontier — verify)* Preprints extending finite generation to CY complete intersections in weighted projective spaces.
- **Quantum BCOV / BV field theory** (Costello, Perimeter; Si Li, Tsinghua): renormalized Kodaira–Spencer theory; proofs of higher-genus mirror symmetry for elliptic curves and elliptic orbifolds; the CY3 case remains an existence problem for the quantization.
- **Birational invariance** (Y. Zhang, Fu; Shanghai/Paris): $\tau_{\mathrm{BCOV}}$ invariance under $K$-equivalence and extension to orbifolds and Calabi–Yau pairs.
- **Integrality/BPS** (Klemm, Bonn; Huang, USTC; Schimannek): high-genus numerical solutions for one- and two-parameter models, torsion refined GV invariants.

## 8. Future Work

- Construct a Hodge-theoretic or Arakelov-theoretic object whose Quillen-type metric reproduces $\mathcal F_g$ for $g\ge2$, giving the anomaly equation as a curvature identity.
- Prove the conifold gap condition intrinsically from the local structure of the vanishing cycle and the $c=1$ string near a nodal degeneration.
- Establish finite generation of the higher-genus potentials for multi-parameter families; identify the ring as the ring of almost-holomorphic modular-type forms on $\mathcal M$.
- Combine with the Gross–Siebert program: derive the anomaly equation from a tropical/log degeneration of the mirror.
- Extend the BCOV torsion to Calabi–Yau categories, matching categorical (Costello) higher-genus invariants of the Fukaya category.

## 9. Key References

- **[Foundational]** M. Bershadsky, S. Cecotti, H. Ooguri, C. Vafa. *Kodaira–Spencer theory of gravity and exact results for quantum string amplitudes.* Communications in Mathematical Physics 165 (1994), 311–427.
- **[Foundational]** D. Ray, I. Singer. *Analytic torsion for complex manifolds.* Annals of Mathematics 98 (1973), 154–177.
- **[Foundational]** J.-M. Bismut, H. Gillet, C. Soulé. *Analytic torsion and holomorphic determinant bundles I–III.* Communications in Mathematical Physics 115 (1988).
- **[Milestone]** H. Fang, Z. Lu, K.-I. Yoshikawa. *Analytic torsion for Calabi–Yau threefolds.* Journal of Differential Geometry 80 (2008), 175–259.
- **[Milestone]** A. Zinger. *The reduced genus 1 Gromov–Witten invariants of Calabi–Yau hypersurfaces.* Journal of the American Mathematical Society 22 (2009), 691–737.
- **[Milestone]** S. Yamaguchi, S.-T. Yau. *Topological string partition functions as polynomials.* Journal of High Energy Physics 2004:07, 047.
- **[SOTA]** H.-L. Chang, S. Guo, J. Li. *Polynomial structure of Gromov–Witten potential of quintic 3-folds.* Annals of Mathematics 194 (2021), 585–645.
- **[SOTA]** S. Guo, F. Janda, Y. Ruan. *Structure of higher genus Gromov–Witten invariants of quintic 3-folds.* arXiv:1812.11908.
- **[SOTA]** D. Eriksson, G. Freixas i Montplet, C. Mourougane. *BCOV invariants of Calabi–Yau manifolds and degenerations of Hodge structures.* Duke Mathematical Journal 170 (2021), 379–454.
- **[SOTA]** D. Eriksson, G. Freixas i Montplet, C. Mourougane. *On genus one mirror symmetry in higher dimensions and the BCOV conjectures.* Forum of Mathematics, Pi 10 (2022), e18.
- **[SOTA]** Y. Zhang. *BCOV invariant and blow-up.* Advances in Mathematics (2022).
- **[Computational]** M.-X. Huang, A. Klemm, S. Quackenbush. *Topological string theory on compact Calabi–Yau: modularity and boundary conditions.* Lecture Notes in Physics 757 (2009), 45–102.
- **[Survey]** K. Hori et al. *Mirror Symmetry.* Clay Mathematics Monographs 1, AMS, 2003 (Chapters 30–36).
- **[Survey]** K.-I. Yoshikawa. *Analytic torsion and automorphic forms on the moduli space.* In *Algebraic and Arithmetic Structures of Moduli Spaces*, Adv. Stud. Pure Math. 58 (2010).

## 10. Worked Example / Concrete Special Case

**Genus one for the quintic $X_5\subset\mathbb P^4$.** Here $h^{1,1}=1$, $\chi(X)=-200$, $\int_X c_2\wedge H=50$, $\int_X H^3=5$.

*B-side.* The mirror family $\check X_z$ is the Greene–Plesser quotient with parameter $z=(5\psi)^{-5}$, discriminant $\Delta=1-5^5z$. The period $\varpi_0(z)=\sum_{d\ge0}\frac{(5d)!}{(d!)^5}z^d$ solves the Picard–Fuchs operator $\mathcal L=\theta^4-5z\prod_{k=1}^4(5\theta+k)$, $\theta=z\,d/dz$. The mirror map is $t=\varpi_1/\varpi_0$ with $\varpi_1=\varpi_0\log z+\Sigma(z)$.

Solving the genus-one anomaly equation with $\chi/24-1=-\tfrac{200}{24}-1$ and imposing (i) regularity of $F_1$ in $q$, (ii) the conifold behaviour $F_1\sim-\tfrac1{12}\log\Delta$, (iii) the LCS leading term $-\tfrac{2\pi i t}{24}\int c_2 H$, gives the holomorphic limit
$$
F_1^{B}(z)=\log\Bigl[\Bigl(\tfrac{dz}{dt}\Bigr)\,\varpi_0^{\,\frac{\chi}{12}-3-h^{1,1}}\,z^{a}\,\Delta^{-1/6}\Bigr],
\qquad \tfrac{\chi}{12}-3-h^{1,1}=-\tfrac{62}{3},
$$
with $a=-\tfrac{1}{12}\int c_2H\cdot\tfrac{1}{?}$ fixed to $a=-\tfrac{25}{12}$ by condition (iii). The exponent $-1/6$ at the conifold is the universal $c=1$ contribution of a single vanishing cycle.

*Expanding.* Writing $q=e^{2\pi i t}$ and inverting $z(q)=q-770q^2+171525q^3-\cdots$, one finds
$$
F_1^{B}=-\frac{2\pi i t}{24}\cdot 50+\frac{q^3\cdot 609250}{1}+\cdots
$$
Extracting Gopakumar–Vafa data from $\sum_d(\tfrac1{12}n^0_d+n^1_d)\sum_k q^{kd}/k$ with the known $n^0_d=2875,\,609250,\,317206375,\dots$ yields
$$
n^1_1=0,\quad n^1_2=0,\quad n^1_3=609250,\quad n^1_4=3721431625,\quad n^1_5=12129909700200 .
$$

*A-side check.* $n^1_1=n^1_2=0$ matches the fact that a general quintic contains no smooth elliptic curves of degree $1$ or $2$ (a plane cubic has degree $3$). $n^1_3=609250$ counts plane cubics on the quintic, which coincides with $n^0_2$ by the classical identification of both with the same family of conics/plane sections — the first non-trivial confirmation.

*Torsion side.* Fang–Lu–Yoshikawa prove that $\tau_{\mathrm{BCOV}}(\check X_z)$, as a function on the one-dimensional moduli space, satisfies
$$
\tau_{\mathrm{BCOV}}(\check X_z)= C\,\bigl|z^{-25/12}\Delta^{-1/6}\bigr|^{2}\,\|\eta_z\|_{L^2}^{-2\cdot 62/3}\quad\text{(up to a universal constant }C),
$$
identifying the torsion with the B-model expression above and hence proving BCOV-1 for the quintic. The same statement for a Calabi–Yau threefold with $h^{1,1}=2$ (e.g. $X_{(3,3)}\subset\mathbb P^5$ with two Kähler parameters) is not covered by any current theorem when both moduli directions are turned on.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*