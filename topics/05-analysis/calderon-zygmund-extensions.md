---
id: 05-analysis/calderon-zygmund-extensions
title: "Calderon Zygmund Extensions"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Calderón–Zygmund Extensions

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/calderon-zygmund-extensions` · **Status:** open

## 1. Problem Statement / Conjecture

Classical Calderón–Zygmund (CZ) theory proves $L^p$ boundedness of singular integrals under three hypotheses: a smooth (Hörmander) kernel, an underlying doubling measure, and Euclidean (or homogeneous-space) geometry. "Calderón–Zygmund extensions" is the program of removing each hypothesis. Its central open problem is the **David–Semmes problem in higher codimension**.

**David–Semmes conjecture.** Let $1 \le d < n$ be integers and let $\mu$ be a $d$-Ahlfors–David regular measure on $\mathbb{R}^n$: there is $C \ge 1$ with
$$C^{-1} r^d \le \mu(B(x,r)) \le C r^d \qquad \text{for all } x \in \operatorname{supp}\mu,\ 0 < r \le \operatorname{diam}(\operatorname{supp}\mu).$$
Let $R_\mu$ be the $d$-dimensional Riesz transform, with kernel $K(x) = x/|x|^{d+1}$. Then
$$R_\mu \text{ bounded on } L^2(\mu) \iff \mu \text{ is uniformly rectifiable.}$$

The $\Leftarrow$ direction is a theorem (David–Semmes, 1991). The $\Rightarrow$ direction is proved only for $d = n-1$ (codimension 1; Nazarov–Tolsa–Volberg, 2014) and $d=1$ (Mattila–Melnikov–Verdera, 1996). **Open: every pair with $2 \le n-d$ and $d \ge 2$, and the smallest genuinely open case $d=1$, $n=3$ is already unsolved for the $1$-dimensional Riesz kernel.**

Two companion extension problems are also open and are tracked here: (i) **sharp weighted bounds for rough singular integrals** (kernels $\Omega(x/|x|)/|x|^n$ with $\Omega \in L^\infty(S^{n-1})$, $\int_{S^{n-1}}\Omega = 0$), where the correct power of $[w]_{A_2}$ is unknown; (ii) **CZ theory on non-doubling metric spaces** without upper regularity.

A complete resolution of (1) means: a proof that $L^2(\mu)$-boundedness of $R_\mu$ forces uniform rectifiability for all $(d,n)$, or a counterexample — an AD-regular, purely unrectifiable $\mu$ with $R_\mu$ bounded.

## 2. Mathematical Foundations

**CZ operator.** $T$ is a CZ operator of order $d$ associated with $\mu$ if it has kernel $K$ on $\mathbb{R}^n\setminus\{0\}$ with
$$|K(x)| \le \frac{C}{|x|^{d}}, \qquad |\nabla K(x)| \le \frac{C}{|x|^{d+1}},$$
and $T_\varepsilon f(x) = \int_{|x-y|>\varepsilon} K(x-y) f(y)\, d\mu(y)$ satisfies $\sup_\varepsilon \|T_\varepsilon\|_{L^2(\mu)\to L^2(\mu)} < \infty$.

**Uniform rectifiability (David–Semmes).** A $d$-AD-regular $\mu$ is uniformly rectifiable if there exist $M, \theta > 0$ such that for every $x \in \operatorname{supp}\mu$ and $0 < r \le \operatorname{diam}$, there is an $M$-Lipschitz map $g : B_d(0,r) \subset \mathbb{R}^d \to \mathbb{R}^n$ with
$$\mu\big(B(x,r) \cap g(B_d(0,r))\big) \ge \theta r^d .$$
Equivalently: $\mu$ satisfies the Big Pieces of Lipschitz Images condition, or a Carleson-measure bound on $\beta$-numbers,
$$\beta_{\mu,2}(x,r)^2 = \inf_{L} \frac{1}{r^d}\int_{B(x,r)} \left(\frac{\operatorname{dist}(y,L)}{r}\right)^2 d\mu(y),$$
infimum over affine $d$-planes $L$, with $\beta_{\mu,2}(x,r)^2 \frac{d\mu(x)\,dr}{r}$ a Carleson measure.

**Menger curvature and the Melnikov identity ($d=1$, $n=2$).** For distinct $z_1,z_2,z_3 \in \mathbb{C}$ with circumradius $R$, set $c(z_1,z_2,z_3) = 1/R$. Then
$$\sum_{\sigma \in S_3} \frac{1}{\big(z_{\sigma(2)}-z_{\sigma(1)}\big)\overline{\big(z_{\sigma(3)}-z_{\sigma(1)}\big)}} = c(z_1,z_2,z_3)^2 \ge 0 .$$
This positivity converts $\|\mathcal{C}_\mu\|^2_{L^2(\mu)}$ into the curvature energy $\iiint c^2 \,d\mu^3$, which controls rectifiability.

**Weights.** $w \in A_p$ with $[w]_{A_p} = \sup_Q \big(\fint_Q w\big)\big(\fint_Q w^{-1/(p-1)}\big)^{p-1}$. The $A_2$ theorem (Hytönen) gives $\|T\|_{L^2(w)} \lesssim_T [w]_{A_2}$ for smooth CZ kernels, and this is sharp.

**Sparse domination.** A family $\mathcal{S}$ of cubes is $\eta$-sparse if each $Q\in\mathcal S$ contains $E_Q \subset Q$, pairwise disjoint, with $|E_Q| \ge \eta|Q|$. Lerner's principle: for a CZ operator, $|\langle Tf, g\rangle| \lesssim \sum_{Q\in\mathcal S} |Q| \langle |f|\rangle_Q \langle |g|\rangle_Q$, from which all weighted bounds follow mechanically.

## 3. History & State of the Art (SOTA)

- **1952.** Calderón–Zygmund, *On the existence of certain singular integrals* (Acta Math. 88): the CZ decomposition and weak-$(1,1)$ theory.
- **1971.** Coifman–Weiss extend everything to spaces of homogeneous type — doubling metric measure spaces.
- **1977/1982.** Calderón, then Coifman–McIntosh–Meyer, prove $L^2$ boundedness of the Cauchy integral on Lipschitz graphs, the launching point of quantitative rectifiability.
- **1988.** Christ, and Christ–Rubio de Francia, obtain weak $(1,1)$ bounds for rough convolution operators with $\Omega \in L\log L(S^{n-1})$ in low dimensions; Seeger (1996, JAMS) proves weak $(1,1)$ for all $n$ with $\Omega \in L\log L$.
- **1991–1993.** David–Semmes formulate the problem and prove the "easy" direction plus the $L^p$/Carleson characterizations (*Astérisque* 193; AMS Surveys 38).
- **1996.** Mattila–Melnikov–Verdera settle $d=1$, $n=2$ using Melnikov curvature.
- **2003.** Nazarov–Treil–Volberg prove the non-homogeneous $Tb$ theorem (Acta Math. 190); Tolsa resolves Painlevé's problem and semiadditivity of analytic capacity (Acta Math. 190).
- **2012.** Hytönen proves the $A_2$ conjecture (Ann. of Math. 175); Lerner (2013) gives the sparse proof.
- **2014.** Nazarov–Tolsa–Volberg prove codimension 1 (Acta Math. 213) — the deepest result to date, using a variational argument, the maximum principle for the harmonic-measure-like structure, and an $\alpha$-number/blow-up scheme. Codimension $\ge 2$ remains untouched by these methods.
- **2017–2019.** Sparse domination for rough kernels: Conde-Alonso–Culiuc–Di Plinio–Ou (Anal. PDE 10, 2017) give $\|T_\Omega\|_{L^2(w)} \lesssim [w]_{A_2}^2$ for $\Omega\in L^\infty$; Lerner (Rev. Mat. Iberoam. 35, 2019) improves to $[w]_{A_2}\,[w]_{A_\infty}^{1/2}([w]_{A_\infty}^{1/2}+[w^{-1}]_{A_\infty}^{1/2})$.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| $d=1$, $n=2$ (Cauchy kernel) | **Solved** | Mattila–Melnikov–Verdera 1996 |
| $d=1$, $n\ge 3$ | **Solved** for the Cauchy-type/curvature setting; solved for the $1$-Riesz kernel by curvature comparison (Lipschitz-type argument) | Léger 1999 (Ann. of Math. 149) gives Besicovitch-type conclusion for $c^2$-finite sets |
| $d = n-1$, any $n \ge 2$ | **Solved** | Nazarov–Tolsa–Volberg 2014 |
| $\mu$ with additional flatness/porosity or reflectionless hypotheses | Solved | Jaye–Nazarov–Tolsa–Volberg, *The Riesz transform of codimension smaller than one and the Wolff energy*, Mem. AMS 266 (2020) |
| Kernels $x/|x|^{d+1}$ replaced by $x^{2k-1}/|x|^{d+2k}$, $d=1$, $n=2$ | Solved (odd powers of Cauchy kernel) | Chousionis–Mateu–Prat–Tolsa, Duke Math. J. 161 (2012) |
| $\mu = \mathcal{H}^d|_E$, $E$ a Lipschitz graph or $C^{1,\alpha}$ surface | Solved (both directions) | Coifman–McIntosh–Meyer 1982; David 1984 |
| **Weighted rough kernels**: $\Omega \in L^\infty$, exponent $[w]_{A_2}^{1+}$ | Best known exponent is strictly between $1$ and $2$; conjectured optimal is $[w]_{A_2}$ | Lerner 2019 |
| Weak $(1,1)$ for $T_\Omega$, $\Omega\in L^\infty(S^{n-1})$ | Open in general; known for $\Omega \in L\log L$ | Seeger 1996 |
| Non-doubling upper-regular $\mu$ ($\mu(B(x,r))\le r^d$) | Full CZ theory available | Tolsa 2014 monograph; NTV 2003 |
| Muckenhoupt–Wheeden weak-$A_1$ conjecture | **Disproved** | Reguera–Thiele, Math. Res. Lett. 19 (2012) |

## 5. Principal Obstacles

- **No positive symmetrization in codimension $\ge 2$.** The Melnikov identity is the engine of the $d=1$, $n=2$ proof. Farag (*The Riesz kernels do not give rise to higher-dimensional analogues of the Menger–Melnikov curvature*, Publ. Mat. 43, 1999) proved the permutation sum for the $d$-Riesz kernel is **not** nonnegative when $d>1$ and $d \neq n-1$. There is no known replacement quadratic form.
- **Loss of the potential-theoretic bridge.** The codimension-1 proof of NTV exploits that $R_\mu$ is the gradient of the Newtonian potential, giving a maximum principle and harmonic measure. For $d \le n-2$ the kernel is the gradient of a Riesz potential $|x|^{-(d-1)}$ of non-integer order relative to the ambient dimension; there is no maximum principle and no elliptic PDE to which the operator is subordinate.
- **Blow-ups are not classified.** Reflectionless measures — those for which $R_\mu$ vanishes off the support — are classified only in codimension $<1$ and codimension $1$. In higher codimension no classification is available, so the standard tangent-measure/compactness argument has no terminal case.
- **Rough kernels defeat sparse forms.** For $\Omega\in L^\infty$ the kernel has no modulus of continuity, so the CZ decomposition's "good part" estimate fails; sparse domination is only available in the $\langle f\rangle_{p}\langle g\rangle_{q}$ bilinear form with $p,q>1$, and the loss $p,q\to1$ is exactly what obstructs the linear $[w]_{A_2}$ bound and the weak $(1,1)$ endpoint.
- **Non-doubling without upper regularity.** Without $\mu(B(x,r)) \lesssim r^d$ there is no dyadic-cube structure (Hytönen–Kairema fails), no CZ decomposition, and no $Tb$ theorem.

## 6. The Gap

Precisely: the implication "$R_\mu$ bounded $\Rightarrow$ $\beta_{\mu,2}^2 \,\frac{d\mu\,dr}{r}$ Carleson" is proven when the operator can be linked to a nonnegative energy — either the curvature $\iiint c^2$ ($d=1$) or the Wolff/harmonic energy of a codimension-1 potential ($d=n-1$). The gap is the construction, for $2 \le d \le n-2$, of a nonnegative functional $E(\mu)$ satisfying both

1. $E(\mu) \lesssim \|R_\mu\|^2_{L^2(\mu)\to L^2(\mu)}\,\mu(\text{ball})$, and
2. $E(\mu) < \infty$ plus AD-regularity $\Rightarrow$ uniform rectifiability.

Farag's theorem rules out the obvious candidate for (1). Whether a non-symmetric, higher-order, or variational substitute exists is the open mathematical step.

## 7. Current Research (as of June 2026)

- **Barcelona/UAB school (Tolsa, Mateu, Prat, Dąbrowski).** Extensions of the codimension-1 method; connections between Riesz transforms, elliptic measure, and the two-phase problem. Dąbrowski's work on cones and $\beta$-numbers gives new sufficient conditions for rectifiability from singular-integral hypotheses. *(frontier — verify)*
- **Michigan State / Kent (Volberg, Jaye, Nazarov).** Reflectionless measures and Wolff energies in fractional codimension; the Mem. AMS 266 (2020) framework is being pushed toward codimension between $1$ and $2$. *(frontier — verify)*
- **Sparse-domination community (Lerner, Ombrosi, Di Plinio, Ou, Hytönen).** Determining the sharp $A_2$ exponent for $T_\Omega$, $\Omega\in L^\infty$; the conjecture is linear in $[w]_{A_2}$, and current lower bounds do not exclude it.
- **Metric-measure CZ theory (Hytönen, Kairema, Martikainen, Nazarov).** Non-homogeneous $Tb$ theorems in general metric spaces; the state of the art requires upper regularity.
- **Rectifiability of measures of non-integer dimension** and the relation to $s$-Riesz transforms for $s \notin \mathbb{Z}$ (Eiderman–Nazarov–Volberg, *The $s$-Riesz transform of an $s$-dimensional measure in $\mathbb{R}^2$ is unbounded for $1<s<2$*, J. Anal. Math. 122, 2014).

## 8. Future Work

- Search for a **fourth-order or non-quadratic energy** replacing Menger curvature in codimension $\ge 2$; or prove no local, permutation-invariant positive form exists, forcing genuinely global methods.
- Attack the intermediate problem: characterize AD-regular measures for which **all** CZ operators of order $d$ (not just Riesz) are bounded — this "strong" David–Semmes problem is known equivalent to uniform rectifiability in every codimension (David–Semmes 1991), so the difficulty is isolating a single kernel.
- Import **quantitative PDE tools** — free-boundary and two-phase methods for elliptic measure — to codimension $\ge 2$ by replacing the Laplacian with a degenerate elliptic operator whose Green function has $|x|^{-(d-1)}$ decay.
- For rough kernels: prove or disprove weak $(1,1)$ for $\Omega \in L^\infty(S^{n-1})$, and settle the sharp $A_2$ exponent.

## 9. Key References

- **[Foundational]** A. P. Calderón, A. Zygmund. *On the existence of certain singular integrals.* Acta Mathematica 88 (1952), 85–139.
- **[Foundational]** G. David, S. Semmes. *Singular integrals and rectifiable sets in $\mathbb{R}^n$: Au-delà des graphes lipschitziens.* Astérisque 193, Société Mathématique de France, 1991.
- **[Foundational]** G. David, S. Semmes. *Analysis of and on Uniformly Rectifiable Sets.* Mathematical Surveys and Monographs 38, AMS, 1993.
- **[Foundational]** R. Coifman, G. Weiss. *Analyse harmonique non-commutative sur certains espaces homogènes.* Lecture Notes in Mathematics 242, Springer, 1971.
- **[SOTA]** F. Nazarov, X. Tolsa, A. Volberg. *On the uniform rectifiability of AD-regular measures with bounded Riesz transform operator: the case of codimension 1.* Acta Mathematica 213 (2014), 237–321.
- **[SOTA]** P. Mattila, M. Melnikov, J. Verdera. *The Cauchy integral, analytic capacity, and uniform rectifiability.* Annals of Mathematics 144 (1996), 127–136.
- **[SOTA]** F. Nazarov, S. Treil, A. Volberg. *The $Tb$-theorem on non-homogeneous spaces.* Acta Mathematica 190 (2003), 151–239.
- **[SOTA]** T. Hytönen. *The sharp weighted bound for general Calderón–Zygmund operators.* Annals of Mathematics 175 (2012), 1473–1506.
- **[SOTA]** A. Lerner. *A weak type estimate for rough singular integrals.* Revista Matemática Iberoamericana 35 (2019), 1583–1602.
- **[SOTA]** J. M. Conde-Alonso, A. Culiuc, F. Di Plinio, Y. Ou. *A sparse domination principle for rough singular integrals.* Analysis & PDE 10 (2017), 1255–1284.
- **[SOTA]** B. Jaye, F. Nazarov, X. Tolsa, A. Volberg. *The Riesz transform of codimension smaller than one and the Wolff energy.* Memoirs of the AMS 266 (2020).
- **[Obstruction]** H. Farag. *The Riesz kernels do not give rise to higher-dimensional analogues of the Menger–Melnikov curvature.* Publicacions Matemàtiques 43 (1999), 251–260.
- **[Survey]** X. Tolsa. *Analytic Capacity, the Cauchy Transform, and Non-homogeneous Calderón–Zygmund Theory.* Progress in Mathematics 307, Birkhäuser, 2014.
- **[Survey]** A. Volberg. *Calderón–Zygmund Capacities and Operators on Nonhomogeneous Spaces.* CBMS Regional Conference Series 100, AMS, 2003.
- **[Survey]** P. Mattila. *Geometry of Sets and Measures in Euclidean Spaces.* Cambridge University Press, 1995.

## 10. Worked Example / Concrete Special Case

**Verifying the Melnikov identity, and seeing what is lost in codimension 2.**

Take $z_1 = 0$, $z_2 = 1$, $z_3 = i$. Write $p = \sum_{\sigma\in S_3} \big[(z_{\sigma(2)}-z_{\sigma(1)})\overline{(z_{\sigma(3)}-z_{\sigma(1)})}\big]^{-1}$, grouping by base point.

Base $z_1=0$: differences $1$ and $i$, giving $\frac{1}{1\cdot\overline{i}} + \frac{1}{i\cdot\overline{1}} = i + (-i) = 0$.

Base $z_2=1$: differences $-1$ and $i-1$, giving $\frac{1}{(-1)(\overline{i-1})} + \frac{1}{(i-1)(\overline{-1})} = \frac{1}{1+i} + \frac{1}{1-i} = \frac{1-i}{2}+\frac{1+i}{2} = 1$.

Base $z_3=i$: by symmetry, $\frac{1}{1-i} + \frac{1}{1+i} = 1$.

So $p = 2$. Independently, the triangle has area $\tfrac12$ and side lengths $1,\sqrt2,1$, so the circumradius is $R = \frac{1\cdot\sqrt2\cdot 1}{4\cdot\frac12} = \frac{\sqrt2}{2}$ and $c^2 = R^{-2} = 2$. The identity holds, and $p \ge 0$ always.

**Consequence.** Expanding $\|\mathcal{C}_{\mu,\varepsilon} 1\|_{L^2(\mu)}^2$ and symmetrizing over the three variables gives
$$\|\mathcal{C}_{\mu,\varepsilon}1\|_{L^2(\mu)}^2 = \tfrac16 \iiint_{|z_i-z_j|>\varepsilon} c(z_1,z_2,z_3)^2\, d\mu z_1 d\mu z_2 d\mu z_3 + O(\mu(\mathbb{C})),$$
so boundedness of the Cauchy transform bounds curvature; finite curvature plus AD-regularity forces rectifiability (Léger). If the three points are collinear, $R=\infty$ and $c=0$: the energy penalizes exactly non-flatness, which is why it detects rectifiability.

**Where it breaks.** Repeat the computation for the $1$-dimensional Riesz kernel $K(x)=x/|x|^2$ on three points of $\mathbb{R}^3$ that are *not* coplanar in the right way, and the symmetrized sum $\sum_\sigma \langle K(x_{\sigma(2)}-x_{\sigma(1)}), K(x_{\sigma(3)}-x_{\sigma(1)})\rangle$ still reduces to $c^2$ (the $d=1$ case survives, since the geometry is planar for any three points). But for $d=2$ in $\mathbb{R}^4$, Farag exhibits configurations where the analogous sum is **strictly negative**. The energy method therefore has no positivity to exploit, and no substitute is known — this single sign failure is the concrete face of the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*