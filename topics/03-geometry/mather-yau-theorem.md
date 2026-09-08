---
id: 03-geometry/mather-yau-theorem
title: "Mather-Yau Theorem"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mather-Yau Theorem

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/mather-yau-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $f, g \in \mathfrak{m}^2 \subset \mathcal{O}_n = \mathbb{C}\{x_1,\dots,x_n\}$ define germs of hypersurfaces with isolated singularity at the origin. The **Mather–Yau theorem** (1982) states that the complex-analytic isomorphism type of the germ $(V(f),0)$ is completely determined by a single finite-dimensional commutative $\mathbb{C}$-algebra, the **Tjurina (moduli) algebra**

$$A(f) \;=\; \mathcal{O}_n \big/ \big(f, \tfrac{\partial f}{\partial x_1}, \dots, \tfrac{\partial f}{\partial x_n}\big).$$

**Theorem.** $(V(f),0) \cong (V(g),0)$ as complex germs $\iff$ $A(f) \cong A(g)$ as $\mathbb{C}$-algebras.

The classical statement is settled. What remains open, and what this page tracks, is the surrounding programme:

1. **Effective reconstruction.** The proof is not constructive. Given an abstract finite-dimensional algebra $A$, decide whether $A \cong A(f)$ for some isolated hypersurface singularity, and if so recover $f$ up to contact equivalence, by an algorithm with controlled complexity.
2. **Positive and mixed characteristic.** Over a field $k$ with $\operatorname{char} k = p > 0$, the Tjurina algebra alone does *not* determine the germ; the correct invariant and its sharp form are only partly understood (Greuel–Pham, 2017).
3. **Lie-theoretic analogues.** Whether the derivation Lie algebra $L(V) = \operatorname{Der}(A(f),A(f))$ (the **Yau algebra**), or its higher variants $L^k(V)$, determines the singularity — and what the sharp dimension bounds are — is open in general.

A complete resolution of (1) means a terminating algorithm with a proved complexity bound; of (2) a characteristic-free statement with a matching counterexample showing sharpness; of (3) either a proof that the relevant Lie algebra is a complete invariant on a stated class, or explicit non-isomorphic germs with isomorphic Yau algebras.

## 2. Mathematical Foundations

**Contact equivalence.** $f \sim_c g$ iff there is an automorphism $\varphi$ of $\mathcal{O}_n$ and a unit $u \in \mathcal{O}_n^*$ with $g = u\cdot \varphi(f)$. By the analytic Nullstellensatz this is equivalent to $(V(f),0)\cong(V(g),0)$.

**Jacobian ideal and invariants.** Write $j(f) = (\partial_1 f,\dots,\partial_n f)$. Then

$$\mu(f) = \dim_\mathbb{C} \mathcal{O}_n/j(f), \qquad \tau(f) = \dim_\mathbb{C} \mathcal{O}_n/\big((f)+j(f)\big) = \dim_\mathbb{C} A(f).$$

Isolated singularity $\iff \mu(f) < \infty$. Always $\tau \le \mu$, and **Saito's theorem** (1971): $\mu = \tau$ iff $f$ is quasi-homogeneous after a coordinate change, i.e. $f = \sum_i w_i x_i \partial_i f / d$ for positive weights $w_i$ and degree $d$.

**The two Mather–Yau statements.** For $f,g\in\mathfrak{m}^2$ with isolated singularity:

$$f\sim_c g \iff \mathcal{O}_n/\big((f)+j(f)\big)\cong \mathcal{O}_n/\big((g)+j(g)\big) \quad (\text{as } \mathbb{C}\text{-algebras}),$$

and a stronger "same ideal" version: if $(f)+j(f) = (g)+j(g)$ as ideals and $\mu<\infty$, then $f\sim_c g$. The ideal-level statement is proved by an integration argument along a path $f_t = (1-t)f + tg$: one shows the ideal $(f_t)+j(f_t)$ is constant in $t$, produces a vector field $X_t$ and unit $u_t$ solving

$$\frac{\partial f_t}{\partial t} + X_t(f_t) + u_t f_t = 0,$$

and integrates to a family of contact isomorphisms. Finiteness of $\tau$ makes the required division possible.

**Finite determinacy.** $f$ is contact $k$-determined if $\mathfrak{m}^{k+1}\subset \mathfrak{m}^2 j(f) + \mathfrak{m}(f)$; in particular $k = \tau(f)+1$ always works, so every isolated singularity is a polynomial up to $\sim_c$. This reduces the classification to finite data.

**Positive characteristic.** For $k$ algebraically closed, $\operatorname{char} k = p>0$, $f,g\in\mathfrak{m}^2\subset k[[x_1,\dots,x_n]]$ with isolated singularity, Greuel–Pham proved

$$f \sim_c g \iff k[[x]]\big/\big((f)+\mathfrak{m}\, j(f)\big) \cong k[[x]]\big/\big((g)+\mathfrak{m}\, j(g)\big),$$

i.e. the Tjurina algebra must be replaced by the slightly larger quotient by $(f) + \mathfrak{m}j(f)$.

**Yau algebra.** $L(V) := \operatorname{Der}(A(f),A(f))$ is a finite-dimensional solvable Lie algebra, of dimension $\lambda(V)$. Higher variants use $A_k(f) = \mathcal{O}_n/((f)+\mathfrak{m}^k j(f))$ with $L^k(V) = \operatorname{Der}(A_k,A_k)$, $\lambda_k(V) = \dim L^k(V)$.

## 3. History & State of the Art (SOTA)

- **1969.** Tjurina introduces $A(f)$ as the tangent space to the semiuniversal deformation of the germ; $\tau$ is its dimension.
- **1971.** K. Saito characterises quasi-homogeneity by $\mu = \tau$. Zariski poses the multiplicity question in the same period.
- **1976.** Shoshitaishvili: two germs with the *same* Jacobian ideal and $\mu<\infty$ differ by a coordinate change up to weights — the right-equivalence prototype of the later result.
- **1982.** Mather and Yau, *Invent. Math.* **69**, prove the theorem in both the ideal and the algebra form. This is the landmark: an infinite-dimensional moduli problem is reduced to a finite-dimensional algebra.
- **1990.** Benson–Yau give constructive results for low $\tau$ and identify the algebraic conditions for an abstract algebra to be a moduli algebra. Seeley–Yau show the Lie-algebra analogue is subtler: variation of complex structure need not be captured.
- **1986–.** Yau's programme: $L(V)$ for simple and quasi-homogeneous singularities, generalised Cartan matrices.
- **2017.** Greuel–Pham settle the positive-characteristic version with the $\mathfrak{m}j(f)$ correction.
- **2019–2024.** Greuel–Pham extend finite determinacy and Mather–Yau-type statements to matrices of power series and to ideals; Hussain–Yau–Zuo develop $k$-th Yau algebras and a family of sharp-bound conjectures.

## 4. Partial Results / Verified Cases

- **ADE (simple) singularities, all $n$.** Complete: the Tjurina algebras of $A_k, D_k, E_6, E_7, E_8$ are pairwise non-isomorphic and explicitly listed; $\mu = \tau$ throughout.
- **Quasi-homogeneous germs.** Here $A(f)=\mathcal{O}_n/j(f)$ is a graded Artinian Gorenstein algebra; reconstruction of $f$ from $A(f)$ is effective via the socle generator and the weight system.
- **Low Tjurina number.** For $\tau \le 6$ (and, with case analysis, somewhat higher) the abstract algebras arising as moduli algebras are classified, giving a constructive inverse — Benson–Yau.
- **Binomial and fewnomial singularities.** Hussain–Yau–Zuo compute $\lambda(V)$ and $\lambda_k(V)$ exactly for binomial ($n=2$) and trinomial ($n=3$) germs, verifying the conjectured inequalities in those ranges.
- **Positive characteristic.** Fully proved for $f\in\mathfrak{m}^2\subset k[[x_1,\dots,x_n]]$, any $n$, any $p>0$, using $(f)+\mathfrak{m}j(f)$ (Greuel–Pham 2017).
- **Complete intersections.** A Mather–Yau statement holds for isolated complete-intersection singularities with the Tjurina algebra replaced by the Tjurina *module* $T^1$, in the analytic case.
- **Non-isolated case.** Known counterexamples: for non-isolated singularities the Tjurina algebra is infinite-dimensional and the theorem fails as stated.

## 5. Principal Obstacles

- **Non-constructivity of the integration argument.** The proof produces a vector field by solving a division problem in $\mathcal{O}_n$; the flow is obtained from an ODE with analytic coefficients. Nothing in the argument bounds the degree or the number of steps needed to write down the isomorphism, so the theorem gives existence and not an algorithm.
- **The inverse problem is a moduli problem in disguise.** Deciding which Artinian algebras are moduli algebras is a system of polynomial equations on structure constants whose solvability is a real-algebraic-geometry question; Gröbner-basis approaches blow up doubly exponentially in $\tau$.
- **Characteristic $p$ breaks the Euler/integration machinery.** Division by $p$ in the weight identity fails; $f$ can lie in $j(f)$ for degenerate reasons (e.g. $p$-th powers), so $(f)+j(f)$ loses information. The $\mathfrak{m}j(f)$ correction restores it but destroys the direct link to the deformation space $T^1$.
- **Lie algebras lose grading data.** Derivations of $A(f)$ see only the algebra's automorphism infinitesimals; two distinct germs can have isomorphic solvable derivation algebras since solvable Lie algebras are far from rigid. Seeley–Yau show the map from complex structure to Lie algebra is not injective in general.
- **Modality.** Beyond $\mu$-constant strata of modality $\ge 1$, the family of moduli algebras varies continuously, so any discrete invariant (dimension, Hilbert function, socle degree) is necessarily incomplete.

## 6. The Gap

Proven: $A(f)$ is a *complete* invariant over $\mathbb{C}$ (and $(f)+\mathfrak{m}j(f)$ over $k$ of char $p$). Open: the inverse map. Explicitly, the gap is the absence of a decision procedure

$$A \;\longmapsto\; \{\,f \in \mathbb{C}[x_1,\dots,x_n] : A(f)\cong A\,\}\big/\sim_c$$

with a proved complexity bound in $(\tau, n)$, together with an intrinsic characterisation of the image of $f\mapsto A(f)$ inside Artinian $\mathbb{C}$-algebras. Known necessary conditions (Gorenstein for quasi-homogeneous $f$; embedding dimension $\le n$; socle constraints) are not known to be sufficient. For the Lie-theoretic branch, the gap is between verified low-dimensional families (binomials, trinomials) and the general conjectured inequalities relating $\lambda_k(V)$ to $\tau$ and the weights.

## 7. Current Research (as of June 2026)

- **Kaiserslautern / Greuel's school.** Determinacy and Mather–Yau statements for matrices of power series, ideals, and modules; algorithmic implementation in `SINGULAR`. *(frontier — verify)* Extensions to mixed characteristic and to non-reduced base rings are actively circulating as preprints.
- **Tsinghua / YMSC (Yau, Zuo, Hussain).** $k$-th Yau algebras $L^k(V)$, sharp bounds for $\lambda_k$, and conjectural inequalities $\lambda_{k+1}(V) < \lambda_k(V)$ for fewnomial germs. *(frontier — verify)*
- **Computational singularity theory.** Normal-form databases and machine-assisted classification of moduli algebras beyond $\tau = 10$. *(frontier — verify)*
- **Links to Zariski's multiplicity conjecture.** Whether topological type determines multiplicity remains open; Mather–Yau shows analytic type does, which sharpens the target.
- **Mirror-symmetry adjacency.** Tjurina algebras of quasi-homogeneous germs are the chiral rings of Landau–Ginzburg models; reconstruction questions recur there as "recovering the potential from the chiral ring".

## 8. Future Work

- Produce an effective Mather–Yau: bound the determinacy degree needed to realise the isomorphism, e.g. show $f$ and $g$ are conjugate by a polynomial map of degree $\le C(\tau,n)$.
- Characterise moduli algebras intrinsically. For the quasi-homogeneous case, Gorenstein + graded is close to sufficient; the general case needs a substitute for the Euler relation.
- Prove or refute that the Yau algebra $L(V)$ determines $(V,0)$ within the class of binomial and trinomial singularities in $n\le 3$.
- Settle whether the Greuel–Pham correction $\mathfrak{m}j(f)$ is minimal: find $f,g$ in char $p$ with $(f)+j(f)$ isomorphic but not contact equivalent, in every $p$.
- Extend to non-isolated singularities using the Tjurina algebra of a stratified or logarithmic replacement.

## 9. Key References

- **[Foundational]** J. N. Mather and S. S.-T. Yau. *Classification of isolated hypersurface singularities by their moduli algebras.* Inventiones Mathematicae **69** (1982), 243–251. [DOI](https://doi.org/10.1007/bf01399504)
- **[Foundational]** G. N. Tjurina. *Locally semiuniversal flat deformations of isolated singularities of complex spaces.* Izvestiya Akademii Nauk SSSR, Ser. Mat. **33** (1969), 1026–1058. [DOI](https://doi.org/10.1070/im1969v003n05abeh000814)
- **[Foundational]** K. Saito. *Quasihomogene isolierte Singularitäten von Hyperflächen.* Inventiones Mathematicae **14** (1971), 123–142. [DOI](https://doi.org/10.1007/bf01405360)
- **[Foundational]** A. N. Shoshitaishvili. *Functions with isomorphic Jacobian ideals.* Functional Analysis and Its Applications **10** (1976), 128–133. [DOI](https://doi.org/10.1007/bf01077939)
- **[SOTA / Recent]** G.-M. Greuel and T. H. Pham. *Mather–Yau theorem in positive characteristic.* Journal of Algebraic Geometry **26** (2017), 347–355. [DOI](https://doi.org/10.1090/jag/669)
- **[SOTA / Recent]** G.-M. Greuel and T. H. Pham. *Finite determinacy of matrices and ideals.* Journal of Algebra **530** (2019), 195–214. [DOI](https://doi.org/10.1016/j.jalgebra.2019.04.013)
- **[SOTA / Recent]** N. Hussain, S. S.-T. Yau and H. Zuo. *On the new $k$-th Yau algebras of isolated hypersurface singularities.* Mathematische Zeitschrift **294** (2020), 331–358. [DOI](https://doi.org/10.1007/s00209-019-02269-x)
- **[Related]** M. Benson and S. S.-T. Yau. *Equivalences between isolated hypersurface singularities.* Mathematische Annalen **287** (1990), 107–134. [DOI](https://doi.org/10.1007/bf01446880)
- **[Related]** C. Seeley and S. S.-T. Yau. *Variation of complex structures and variation of Lie algebras.* Inventiones Mathematicae **99** (1990), 545–565. [DOI](https://doi.org/10.1007/bf01234430)
- **[Survey]** G.-M. Greuel, C. Lossen and E. Shustin. *Introduction to Singularities and Deformations.* Springer Monographs in Mathematics, 2007. [DOI](https://doi.org/10.1007/3-540-28419-2)
- **[Survey]** V. I. Arnold, S. M. Gusein-Zade and A. N. Varchenko. *Singularities of Differentiable Maps, Volume 1.* Birkhäuser, 1985.
- **[Context]** O. Zariski. *Some open questions in the theory of singularities.* Bulletin of the American Mathematical Society **77** (1971), 481–491. [DOI](https://doi.org/10.1090/s0002-9904-1971-12729-5)

## 10. Worked Example / Concrete Special Case

**Setup.** Compare $A_4$ and $D_4$ in $n=2$, both with $\tau = 4$. The theorem says the algebras must be non-isomorphic; we verify this and see which structure carries the information.

**$A_4$: $f = x^2 + y^5$.** Then $f_x = 2x$, $f_y = 5y^4$, so
$$(f)+j(f) = (x, y^4), \qquad A(f)\cong \mathbb{C}[y]/(y^4),$$
with basis $1,y,y^2,y^3$ and $\tau = 4$. Its maximal ideal is $\mathfrak{n}=(y)$, and $\dim \mathfrak{n}/\mathfrak{n}^2 = 1$.

**$D_4$: $g = x^2 y - y^3$.** Then $g_x = 2xy$, $g_y = x^2 - 3y^2$. Since $x\cdot g_x = 2x^2y$ and $y\cdot g_y = x^2y - 3y^3$, the ideal contains $y^3$ and hence $x^2 y$, so
$$(g)+j(g) = (xy,\; x^2-3y^2), \qquad A(g) = \mathbb{C}\{x,y\}/(xy,\, x^2-3y^2).$$
A basis is $1, x, y, x^2$ (using $y^2 = x^2/3$, $xy=0$, $x^3 = x\cdot x^2 = 3xy^2 = 0$). So $\tau = 4$ again, and $\mathfrak{n}=(x,y)$ has $\dim\mathfrak{n}/\mathfrak{n}^2 = 2$.

**Conclusion.** $\dim_\mathbb{C} A$ alone ($=4$ for both) is not a complete invariant; the *embedding dimension* $\dim \mathfrak{n}/\mathfrak{n}^2$ separates them ($1$ vs $2$), matching the fact that $A_4$ has multiplicity $2$ and $D_4$ multiplicity $3$. This is exactly the content of Mather–Yau: it is the full algebra structure, not any single numerical shadow of it, that is complete.

**Reconstruction, done by hand.** Given only $A \cong \mathbb{C}[y]/(y^4)$: it is graded Gorenstein with socle $y^3$ and embedding dimension $1$. Quasi-homogeneity forces $f = x_1^2 + \dots + x_{n-1}^2 + y^{k}$ up to $\sim_c$ with $\mathcal{O}_n/j(f)$ of dimension $k-1 = 4$, giving $k=5$. So $f = x^2+y^5$ is recovered. The example is easy only because the algebra is graded; without the grading no such shortcut is known, which is the gap of Section 6.

**Characteristic $p$ warning.** Over $k$ with $\operatorname{char} k = 3$, $g = x^2y - y^3$ has $g_y = x^2 - 3y^2 = x^2$, so $(g)+j(g)=(xy, x^2, y^3)$ and $\dim = 4$ still, but the Euler relation used above ($3y^3 = x^2y - y g_y$) degenerates. Greuel–Pham's correction replaces $j(g)$ by $\mathfrak{m}j(g)$ precisely to absorb such degeneracies.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*