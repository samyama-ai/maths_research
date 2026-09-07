---
id: 10-theoretical-cs/sic-povm-existence
title: "SIC-POVM Existence"
topic: 10-theoretical-cs
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# SIC-POVM Existence (Zauner's Conjecture)

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/sic-povm-existence` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

**Question.** For every integer $d \ge 2$, does there exist a set of $d^2$ unit vectors $\{|\psi_j\rangle\}_{j=1}^{d^2} \subset \mathbb{C}^d$ with

$$|\langle \psi_j | \psi_k \rangle|^2 = \frac{1}{d+1} \qquad \text{for all } j \neq k \, ?$$

Such a set is a **symmetric informationally complete positive-operator-valued measure** (SIC-POVM), equivalently a maximal set of $d^2$ equiangular lines in $\mathbb{C}^d$.

**Zauner's conjecture** (1999) asserts more: for every $d$ there is a SIC that is an orbit of the Weyl–Heisenberg group $\mathrm{WH}(d)$ acting on a single **fiducial** vector, and that fiducial can be chosen as an eigenvector of a canonical order-3 unitary $U_Z$ (the *Zauner unitary*).

A complete resolution requires either (a) a proof valid for all $d$, uniform or by an effective construction, or (b) a single $d$ for which $d^2$ equiangular lines provably do not exist. Numerical solutions are known in every dimension tested; no dimension is known to fail. Hence status **empirically-supported**, not merely open.

## 2. Mathematical Foundations

**POVM form.** Setting $E_j = \tfrac1d |\psi_j\rangle\langle\psi_j|$, the SIC condition gives $\sum_j E_j = I_d$, so $\{E_j\}$ is a POVM. It is *informationally complete*: the $d^2$ operators $|\psi_j\rangle\langle\psi_j|$ span the real $d^2$-dimensional space of Hermitian operators, so measurement statistics $p_j = \mathrm{Tr}(\rho E_j)$ determine $\rho$ uniquely.

**Optimality bounds.** In $\mathbb{C}^d$ the number of equiangular lines is at most $d^2$ (Gerzon / Delsarte–Goethals–Seidel bound). For $N$ unit vectors, the *frame potential* obeys the Welch bound
$$\sum_{j,k=1}^{N} |\langle \psi_j|\psi_k\rangle|^4 \;\ge\; \frac{2N^2}{d(d+1)},$$
with equality iff the vectors form a **projective 2-design**. A SIC saturates both simultaneously: it is a $d^2$-element projective 2-design, the minimum possible size.

**Weyl–Heisenberg covariance.** Fix $\omega = e^{2\pi i/d}$, $\tau = -e^{i\pi/d}$, and on $\mathbb{C}^d$ with basis $\{|e_r\rangle\}_{r \in \mathbb{Z}_d}$ define
$$X|e_r\rangle = |e_{r+1}\rangle,\qquad Z|e_r\rangle = \omega^r |e_r\rangle,\qquad D_{p,q} = \tau^{pq} X^p Z^q .$$
The displacement operators satisfy $D_{p,q}D_{p',q'} = \tau^{qp'-pq'} D_{p+p',q+q'}$ and form a unitary error basis. A **Weyl–Heisenberg SIC** is the orbit $\{D_{p,q}|\psi\rangle\}_{(p,q)\in\mathbb{Z}_d^2}$ of a fiducial $|\psi\rangle$ satisfying
$$|\langle \psi | D_{p,q} | \psi\rangle|^2 = \frac{1}{d+1} \quad \text{for } (p,q) \neq (0,0) \bmod d .$$

**Clifford group and the Zauner unitary.** The normalizer of $\mathrm{WH}(d)$ in $\mathrm{PU}(d)$ is the Clifford group, with $\mathrm{EC}(d)/\mathrm{WH}(d) \cong \mathrm{SL}(2,\mathbb{Z}_d)$ (extended by complex conjugation). Zauner's unitary $U_Z$ is the Clifford element corresponding to
$$F_Z = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix} \in \mathrm{SL}(2,\mathbb{Z}_d), \qquad F_Z^3 = I,$$
and the conjecture states a fiducial exists in the $\omega$-eigenspace of $U_Z$ (dimension roughly $d/3$), reducing the unknowns from $2d-2$ real parameters to about $2d/3$.

**Number-theoretic structure.** For $d \ge 4$, all known WH fiducials have entries generating an abelian extension of the real quadratic field $\mathbb{Q}(\sqrt{D})$, where $D$ is the squarefree part of $(d+1)(d-3)$; the relevant discriminant attaches to the order of conductor tied to $d$. The associated $\mathrm{SL}(2,\mathbb{Z})$ conjugacy class of $F_Z$ has trace $-1$, hence hyperbolic behaviour after lifting, and Galois conjugation acts on SIC orbits through $\mathrm{PGL}(2,\mathbb{Z}_d)$.

## 3. History & State of the Art (SOTA)

- **1970s–80s.** Delsarte, Goethals and Seidel established the $d^2$ bound for complex equiangular line systems and the design-theoretic framework (*Geometriae Dedicata*, 1977).
- **1999.** Gerhard Zauner's Vienna dissertation *Quantendesigns* introduced the objects, proved the WH-covariance structure, found solutions in low dimensions, and stated the conjecture.
- **2004.** Renes, Blume-Kohout, Scott and Caves independently rediscovered SICs from quantum-information motives, produced high-precision numerical fiducials for $d \le 45$, and popularised the name "SIC-POVM" (*J. Math. Phys.* 45, 2171).
- **2005–2010.** Appleby classified Clifford symmetries of fiducials; Scott and Grassl (*J. Math. Phys.* 51, 042203, 2010) delivered exact algebraic fiducials for many $d \le 67$ and numerics to $d = 67$, plus a systematic catalogue of orbit labels ($1a$, $2b$, …).
- **2013–2017.** Appleby, Flammia, Yard and collaborators identified the class-field-theoretic pattern: SIC entries generate ray class fields of $\mathbb{Q}(\sqrt{(d+1)(d-3)})$ ramified at $\infty$ — a concrete, computationally verified instance of Hilbert's twelfth problem for real quadratic fields.
- **2017.** Scott extended numerics to all $d \le 151$ with sporadic solutions well beyond; Grassl and Scott's *Fibonacci–Lucas SIC-POVMs* gave an exact infinite-looking family of dimensions $d_k$ generated by Fibonacci/Lucas recursions.
- **2021–2022.** Kopp connected SICs to **Stark units**, giving conditional exact constructions from Stark's conjecture (*IMRN*, 2021); Appleby, Bengtsson, Grassl, Harrison and McConnell produced Stark-unit SIC constructions in prime dimensions $d = n^2 + 3$ (*J. Math. Phys.* 63, 112205, 2022).

## 4. Partial Results / Verified Cases

- **Exact (algebraic, proof-certified) solutions:** every dimension $2 \le d \le 53$, plus a long list of sporadic dimensions including $d = 55$–$67$, $73$, $79$, $84$, $95$, $97$, $103$, $109$, $124$, $127$, $143$, $147$, $168$, $172$, $199$, $228$, $259$, $292$, $323$, $327$, $844$, $1155$. These are verified by exact arithmetic in the relevant number field, so existence is a *theorem* in each such $d$.
- **High-precision numerical solutions:** all $d \le 151$ (Scott 2017), with sporadic numerics far beyond; solutions are found to $\sim 10^{-30}$ residual, and every such numerical solution to date has been promotable to exact form when pursued.
- **$d = 2, 3$ by hand:** $d=2$ is the regular tetrahedron on the Bloch sphere (Section 10); $d=3$ admits a one-parameter continuous family of WH SICs — the only dimension with a continuum, all others being finite unions of Clifford orbits.
- **Structural theorems:** in $d = p$ prime, the Clifford group acts transitively on known SIC orbits; Zauner symmetry (order-3 stabiliser) holds for *every* known fiducial in every dimension checked, so the eigenvector part of Zauner's conjecture is empirically airtight.
- **Non-WH families:** $d = 8$ admits a SIC covariant under $\mathbb{Z}_2^3$ rather than $\mathbb{Z}_8$ (Hoggar's lines), showing WH covariance is sufficient but not logically necessary.
- **Conditional infinite families:** assuming the (rank-1, abelian) Stark conjectures, Kopp's construction yields exact SIC fiducials in an infinite set of dimensions, verified unconditionally in the dimensions checked.

## 5. Principal Obstacles

- **No continuous deformation.** For $d \ge 4$ solutions are rigid isolated points; there is no manifold of solutions to follow as $d$ varies, so homotopy, degree theory and implicit-function arguments have no handle.
- **The algebraic system is over-determined and unstructured.** The fiducial condition is $d^2-1$ real quartic equations in $2d-2$ real unknowns. Gröbner-basis elimination is doubly exponential and has stalled around $d \approx 20$ even with Zauner symmetry imposed; Bézout counts give astronomically many complex solutions of which almost all are spurious.
- **Number fields explode.** The field generated by a $d$-dimensional fiducial has degree growing roughly like $d^2$ times a class number; heights of the algebraic numbers grow so fast that exact solutions in $d \approx 300$ need thousands of digits of numerical precision before they can even be recognised.
- **Class field theory for real quadratic fields is itself open.** The observed generation of ray class fields is an instance of Hilbert's 12th problem, which has no explicit solution over real quadratic fields. So the natural "construct the SIC from the arithmetic" route depends on unproved analytic input (Stark's conjectures on the leading Taylor coefficient of partial zeta functions at $s=0$).
- **Design/combinatorial bounds do not force existence.** Delsarte–Goethals–Seidel and Welch bounds are necessary conditions saturated by SICs, but the linear-programming and semidefinite hierarchies used elsewhere for tight designs yield no existence certificate here; the analogous real problem ($\mathbb{R}^d$ equiangular lines) shows tight configurations often fail to exist, so no soft argument can work.
- **No representation-theoretic forcing.** Unlike mutually unbiased bases, where prime-power structure gives a construction, no group-theoretic obstruction or construction is known that is uniform in $d$.

## 6. The Gap

Everything proven is dimension-by-dimension: a finite (though growing) list of $d$ where an explicit algebraic fiducial has been exhibited and checked. The conjecture is a statement about *all* $d$. The exact step missing is an **effective, $d$-uniform construction** of the fiducial's entries — equivalently, an explicit description of the relevant ray class field of $\mathbb{Q}(\sqrt{(d+1)(d-3)})$ together with a proof that the specific Galois-orbit combination of Stark units assembled from it satisfies the quartic overlap equations. Kopp's programme converts this into: (i) prove the relevant rank-1 Stark conjecture, and (ii) prove that the *ghost*/real-SIC correspondence — currently verified case by case — holds identically. Neither (i) nor (ii) is available in general, and (ii) has no proof even assuming (i) in full generality.

## 7. Current Research (as of June 2026)

- **Stark-unit programme.** Kopp (Louisiana State), Appleby, Bengtsson (Stockholm), Grassl (ICTQT Gdańsk), Flammia and Yard drive the arithmetic route: express fiducial overlaps as explicit polynomials in Stark units of real quadratic orders. Recent work generalises the $d = n^2+3$ prime family to further congruence classes.
- **Ghost SICs.** Appleby and Bengtsson's "ghost" objects live in the Galois-conjugate field where the Hermitian structure is lost; ghosts are far easier to construct, and mapping ghost $\to$ SIC is the current bottleneck. Announced constructions of SICs in infinite families of dimensions, conditional on Stark, have circulated in preprint form *(frontier — verify)*.
- **Computational extension.** Grassl and collaborators continue pushing numerics and exact recognition into $d > 200$ using $p$-adic and lattice-reduction methods (PSLQ/LLL) on high-precision fiducials.
- **Quantum-foundations angle.** QBism (Fuchs, Stacey) uses SICs to rewrite the Born rule as a deformation of the law of total probability, motivating the search for a "reason" SICs exist. *(frontier — verify)* claims relating SIC existence to Zauner's conjecture on the *triple products* $\langle\psi_j|\psi_k\rangle\langle\psi_k|\psi_l\rangle\langle\psi_l|\psi_j\rangle$ lying in specific class fields remain partially checked.
- **Applications driving interest.** Optimal quantum state tomography, quantum key distribution, compressed sensing measurement matrices with minimal coherence $\mu = 1/\sqrt{d+1}$, and equiangular tight frames in signal processing.

## 8. Future Work

- Prove the rank-1 abelian Stark conjecture for the specific real quadratic orders arising from $(d+1)(d-3)$, then verify that the resulting units assemble into a positive-semidefinite fiducial.
- Find a *closed-form* generating function or recursion for fiducials along an infinite family (Fibonacci–Lucas dimensions are the template) and prove it satisfies the overlap equations by induction.
- Develop a structural proof that Zauner symmetry is *forced*: show any $d^2$-line system in $\mathbb{C}^d$ must be Clifford-covariant, which would collapse the search space to a genuinely finite computation per $d$.
- Attack the problem via moment/SDP relaxations tailored to the $2$-design condition, seeking either a certificate hierarchy that converges or a proof that such hierarchies must fail.
- Settle whether non-WH SICs beyond $d=8$ exist; a second construction mechanism would decouple existence from the arithmetic.

## 9. Key References

- **[Foundational]** G. Zauner. *Quantendesigns: Grundzüge einer nichtkommutativen Designtheorie.* PhD thesis, Universität Wien, 1999. (English translation: *Quantum designs: foundations of a non-commutative design theory*, Int. J. Quantum Inf. 9 (2011), 445–507.)
- **[Foundational]** J. M. Renes, R. Blume-Kohout, A. J. Scott, C. M. Caves. *Symmetric informationally complete quantum measurements.* Journal of Mathematical Physics 45 (2004), 2171–2180.
- **[Foundational]** P. Delsarte, J. M. Goethals, J. J. Seidel. *Bounds for systems of lines and Jacobi polynomials.* Philips Research Reports 30 (1975), 91–105.
- **[SOTA]** A. J. Scott, M. Grassl. *Symmetric informationally complete positive-operator-valued measures: A new computer study.* Journal of Mathematical Physics 51 (2010), 042203.
- **[SOTA]** A. J. Scott. *SICs: Extending the list of solutions.* arXiv:1703.03993, 2017.
- **[SOTA]** M. Appleby, S. Flammia, G. McConnell, J. Yard. *Generating ray class fields of real quadratic fields via complex equiangular lines.* Acta Arithmetica 192 (2020), 211–233.
- **[SOTA]** G. S. Kopp. *SIC-POVMs and the Stark conjectures.* International Mathematics Research Notices 2021, no. 18, 13812–13838.
- **[SOTA]** M. Appleby, I. Bengtsson, M. Grassl, M. Harrison, G. McConnell. *SIC-POVMs from Stark units: prime dimensions $n^2+3$.* Journal of Mathematical Physics 63 (2022), 112205.
- **[SOTA]** M. Grassl, A. J. Scott. *Fibonacci–Lucas SIC-POVMs.* Journal of Mathematical Physics 58 (2017), 122201.
- **[Survey]** C. A. Fuchs, M. C. Hoang, B. C. Stacey. *The SIC question: History and state of play.* Axioms 6 (2017), 21.
- **[Survey]** I. Bengtsson, K. Życzkowski. *Geometry of Quantum States: An Introduction to Quantum Entanglement.* 2nd ed., Cambridge University Press, 2017 (Chapter 12).
- **[Survey]** I. Bengtsson. *The number behind the simplest SIC-POVM.* Foundations of Physics 47 (2017), 1031–1041.

## 10. Worked Example / Concrete Special Case

**Dimension $d = 2$.** We need $d^2 = 4$ unit vectors in $\mathbb{C}^2$ with pairwise $|\langle\psi_j|\psi_k\rangle|^2 = 1/(d+1) = 1/3$.

Write each state via its Bloch vector $\hat n_j \in S^2$: $|\psi_j\rangle\langle\psi_j| = \tfrac12(I + \hat n_j \cdot \vec\sigma)$. Then
$$|\langle\psi_j|\psi_k\rangle|^2 = \mathrm{Tr}\big(|\psi_j\rangle\langle\psi_j|\,|\psi_k\rangle\langle\psi_k|\big) = \tfrac12\big(1 + \hat n_j \cdot \hat n_k\big).$$
Setting this to $1/3$ gives $\hat n_j \cdot \hat n_k = -1/3$ for $j \neq k$ — exactly the vertex angles of a **regular tetrahedron** inscribed in the Bloch sphere. Take
$$\hat n_1 = \tfrac{1}{\sqrt3}(1,1,1),\quad \hat n_2 = \tfrac{1}{\sqrt3}(1,-1,-1),\quad \hat n_3 = \tfrac{1}{\sqrt3}(-1,1,-1),\quad \hat n_4 = \tfrac{1}{\sqrt3}(-1,-1,1).$$
Each dot product is $\tfrac13(1-1-1) = -\tfrac13$. ✓ And $\sum_j \hat n_j = 0$, so $\sum_j E_j = \sum_j \tfrac12 |\psi_j\rangle\langle\psi_j| = \tfrac12\sum_j \tfrac12 (I + \hat n_j\cdot\vec\sigma) = I$. ✓ POVM condition holds.

**As a Weyl–Heisenberg orbit.** With $d=2$, $\omega = -1$, $\tau = -e^{i\pi/2} = -i$, take
$$|\psi\rangle = \begin{pmatrix} \cos(\theta/2) \\ e^{i\pi/4}\sin(\theta/2)\end{pmatrix}, \qquad \cos\theta = \frac{1}{\sqrt3}.$$
This is the Bloch vector $\hat n = (\sin\theta\cos\tfrac\pi4,\ \sin\theta\sin\tfrac\pi4,\ \cos\theta) = \tfrac{1}{\sqrt3}(1,1,1)$, since $\sin\theta = \sqrt{2/3}$ and $\sqrt{2/3}\cdot\tfrac{1}{\sqrt2} = \tfrac{1}{\sqrt3}$. Applying $D_{0,0}=I$, $D_{1,0}=X$, $D_{0,1}=Z$, $D_{1,1}=-iXZ$ reflects $\hat n$ through the three coordinate axes, producing precisely the other three tetrahedron vertices. The overlap check reduces to
$$|\langle\psi|X|\psi\rangle|^2 = \sin^2\theta\cos^2(\pi/4)\cdot 1 = \tfrac23\cdot\tfrac12 = \tfrac13,\qquad |\langle\psi|Z|\psi\rangle|^2 = \cos^2\theta = \tfrac13,$$
and similarly for $XZ$. All equal $1/(d+1)$. ✓

**Why $d=2$ is misleadingly easy.** The entries lie in $\mathbb{Q}(\sqrt3, i)$ — a degree-4 field — and the solution is forced by an $SO(3)$ symmetry with no free parameters. For $d = 4$ the fiducial already requires $\mathbb{Q}(\sqrt5, i, \dots)$ with the ray class field structure appearing, and by $d = 48$ the fiducial's minimal polynomial has degree in the thousands. The geometric picture ("put a Platonic solid on a sphere") has no analogue for $d \ge 3$: this is precisely the gap described in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*