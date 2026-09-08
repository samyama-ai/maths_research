---
id: 05-analysis/composition-operator-spectra
title: "Composition Operator Spectra on the Hardy Space"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Composition Operator Spectra on the Hardy Space

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/composition-operator-spectra` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mathbb{D}$ be the open unit disc and $H^2$ the Hardy space of the disc. Every analytic self-map $\varphi:\mathbb{D}\to\mathbb{D}$ induces a bounded composition operator
$$C_\varphi f = f\circ\varphi ,\qquad f\in H^2 .$$

**Problem.** Determine the spectrum $\sigma(C_\varphi)\subset\mathbb{C}$, and the essential spectrum $\sigma_e(C_\varphi)$ in the Calkin algebra, in terms of the function theory of $\varphi$ alone.

Two sharper sub-problems carry most of the difficulty:

1. **(Essential spectral radius.)** For $\varphi$ with an interior fixed point $a$, $\lambda=\varphi'(a)$, $0<|\lambda|<1$, is
$$r_e(C_\varphi)\;=\;|\lambda|^{\,p(\sigma)/2},$$
where $\sigma$ is the Koenigs eigenfunction and $p(\sigma)=\sup\{p>0:\sigma\in H^p\}$ its **Hardy number**? Known for univalent and finitely valent $\varphi$; **open in general**.
2. **(Boundary Denjoy–Wolff point, no regularity.)** For $\varphi$ with Denjoy–Wolff point $\omega\in\partial\mathbb{D}$ and $\varphi$ *not* analytic across $\omega$, describe $\sigma(C_\varphi)$. Only fragmentary answers exist.

A complete solution means: a function-theoretic invariant of $\varphi$ (counting function, Koenigs model, angular derivative data) computable in principle, together with a theorem identifying $\sigma(C_\varphi)$ and $\sigma_e(C_\varphi)$ as explicit sets built from it, for **every** analytic self-map $\varphi$.

## 2. Mathematical Foundations

$H^2=\{f=\sum_{n\ge0}\hat f(n)z^n:\ \|f\|^2=\sum|\hat f(n)|^2<\infty\}$ with reproducing kernel $K_w(z)=(1-\bar wz)^{-1}$, $\|K_w\|=(1-|w|^2)^{-1/2}$.

**Boundedness (Littlewood subordination).** For every analytic $\varphi:\mathbb{D}\to\mathbb{D}$,
$$\|C_\varphi\|\le\Big(\tfrac{1+|\varphi(0)|}{1-|\varphi(0)|}\Big)^{1/2},\qquad \|C_\varphi\|\ge\big(1-|\varphi(0)|^2\big)^{-1/2},$$
the lower bound from $C_\varphi^{*}K_w=K_{\varphi(w)}$ at $w=0$.

**Denjoy–Wolff.** If $\varphi$ is not an elliptic automorphism there is a unique $\omega\in\overline{\mathbb{D}}$ with $\varphi_n\to\omega$ locally uniformly ($\varphi_n$ = $n$-th iterate). If $\omega\in\mathbb{D}$ then $\varphi(\omega)=\omega$, $|\varphi'(\omega)|<1$; if $\omega\in\partial\mathbb{D}$ then the angular derivative satisfies $\lambda:=\varphi'(\omega)\in(0,1]$. Cases: $\lambda<1$ **hyperbolic**, $\lambda=1$ **parabolic**.

**Koenigs model.** If $\varphi(a)=a$, $a\in\mathbb{D}$, $0<|\lambda|<1$, $\lambda=\varphi'(a)$, there is a unique analytic $\sigma$ with $\sigma(a)=0$, $\sigma'(a)=1$ and
$$\sigma\circ\varphi=\lambda\,\sigma .$$
Then $C_\varphi\sigma^{\,n}=\lambda^{n}\sigma^{n}$, so $\lambda^n\in\sigma_p(C_\varphi)$ exactly when $\sigma^n\in H^2$, i.e. when $2n<p(\sigma)$.

**Nevanlinna counting function and essential norm (Shapiro, 1987).**
$$N_\varphi(w)=\sum_{z\in\varphi^{-1}(w)}\log\frac{1}{|z|},\qquad
\|C_\varphi\|_e^{2}=\limsup_{|w|\to1^-}\frac{N_\varphi(w)}{\log(1/|w|)} .$$
Hence $C_\varphi$ is compact iff $N_\varphi(w)=o(\log(1/|w|))$; equivalently $\varphi$ has no angular derivative of finite modulus at any boundary point and $\|\varphi\|_\infty$-type growth is controlled.

**Spectral radius.** $r(C_\varphi)=\lim_n\|C_\varphi^n\|^{1/n}$ with $C_\varphi^n=C_{\varphi_n}$, so
$$\big(1-|\varphi_n(0)|^2\big)^{-1/(2n)}\ \le\ \|C_\varphi^n\|^{1/n}\ \le\ \Big(\tfrac{1+|\varphi_n(0)|}{1-|\varphi_n(0)|}\Big)^{1/(2n)} ,$$
and the two ends agree in the limit: $r(C_\varphi)=\lim_n(1-|\varphi_n(0)|)^{-1/(2n)}$. For $\omega\in\partial\mathbb{D}$ this gives $r(C_\varphi)=\lambda^{-1/2}$.

## 3. History & State of the Art (SOTA)

- **1925–1929.** Littlewood's subordination principle gives boundedness; Denjoy and Wolff supply the iteration theory.
- **1968.** Nordgren, *Composition operators* (Canad. J. Math.): first systematic spectral results. For $\varphi$ inner with $\varphi(0)=0$ and $\varphi$ not a rotation, $C_\varphi$ is an isometry and $\sigma(C_\varphi)=\overline{\mathbb{D}}$; for a hyperbolic automorphism with $\varphi'(\omega)=\lambda$, $\sigma(C_\varphi)=\{z:\lambda^{1/2}\le|z|\le\lambda^{-1/2}\}$; for a parabolic automorphism, $\sigma(C_\varphi)=\partial\mathbb{D}$.
- **1975.** Kamowitz, *The spectra of composition operators on $H^p$*: for $\varphi$ analytic on $\overline{\mathbb{D}}$ with boundary fixed point $\omega$, $0<\varphi'(\omega)<1$ and no interior fixed point, $\sigma(C_\varphi)=\{z:|z|\le\varphi'(\omega)^{-1/2}\}$ — a **full disc**, no boundary-circle structure. Caughran–Schwartz (1975): $C_\varphi$ compact $\Rightarrow$ $\sigma(C_\varphi)=\{0,1\}\cup\{\varphi'(a)^n\}$.
- **1983, 1988.** Cowen, *Composition operators on $H^2$* and *Linear fractional composition operators on $H^2$*: complete spectra for linear-fractional symbols, including the parabolic non-automorphism spiral $\sigma(C_\varphi)=\{e^{-ta}:t\ge0\}\cup\{0\}$.
- **1987.** Shapiro's essential-norm theorem (Annals) turns compactness and norm estimates into counting-function statements.
- **1994.** Cowen–MacCluer, *Spectra of some composition operators* (JFA): symbols analytic on $\overline{\mathbb{D}}$ with boundary DW point and interior fixed points of the boundary map.
- **1997.** Bourdon–Shapiro, *Mean growth of Koenigs eigenfunctions* (JAMS) and Poggi-Corradini (JFA) identify $r_e(C_\varphi)=|\lambda|^{p(\sigma)/2}$ for univalent $\varphi$ with interior fixed point — the current structural high-water mark.
- **2004–present.** Gallardo-Gutiérrez–Montes-Rodríguez (Memoirs AMS) tie spectra to cyclicity; Higdon and others transfer results to the Dirichlet space and to weighted composition operators.

## 4. Partial Results / Verified Cases

Solved classes (each with an explicit spectrum):

| Class of $\varphi$ | $\sigma(C_\varphi)$ |
|---|---|
| $C_\varphi$ compact (Caughran–Schwartz) | $\{0,1\}\cup\{\varphi'(a)^n:n\ge1\}$ |
| Elliptic automorphism, $\varphi'(a)=e^{2\pi i\theta}$, $\theta$ irrational | $\partial\mathbb{D}$ |
| Elliptic automorphism, $\theta=p/q$ rational | $q$-th roots of unity |
| Hyperbolic automorphism, $\lambda=\varphi'(\omega)<1$ | annulus $\lambda^{1/2}\le|z|\le\lambda^{-1/2}$ |
| Parabolic automorphism | $\partial\mathbb{D}$ |
| Inner, $\varphi(0)=0$, not a rotation | $\overline{\mathbb{D}}$ |
| $\varphi$ analytic on $\overline{\mathbb{D}}$, boundary DW point, $0<\varphi'(\omega)<1$ (Kamowitz) | disc $|z|\le\varphi'(\omega)^{-1/2}$ |
| Parabolic linear-fractional non-automorphism, translation parameter $a$, $\operatorname{Re}a>0$ (Cowen) | spiral $\{e^{-ta}:t\ge0\}\cup\{0\}$ |
| Univalent (or finitely valent) with interior fixed point, $\lambda=\varphi'(a)$ | $\{|z|\le|\lambda|^{p(\sigma)/2}\}\cup\{\lambda^n:\,0\le n<p(\sigma)/2\}$ |

Also settled: all linear-fractional self-maps of $\mathbb{D}$ (Cowen 1983/1988, Bourdon–Shapiro 1997); Riesz composition operators (spectrum a sequence tending to $0$ plus $\{0,1\}$); $\varphi$ with $\|\varphi\|_\infty<1$ (compact, so covered).

## 5. Principal Obstacles

- **Non-univalence destroys the Koenigs model as a conformal model.** For univalent $\varphi$ the Koenigs map $\sigma$ is a conformal isomorphism onto a $\lambda$-invariant domain, so $p(\sigma)$ is a geometric quantity (the Hardy number of a plane domain). For general $\varphi$, $\sigma$ is only analytic; its valence is uncontrolled and the geometric estimates on $\int|\sigma|^p$ collapse.
- **No functional calculus.** $C_\varphi$ is almost never normal, subnormal, or hyponormal (Cowen–Kriete classified the few that are). Spectral-theorem and perturbation arguments give nothing; one must construct eigenfunctions by hand or produce Fredholm inverses explicitly.
- **The spectrum is not upper semicontinuous in $\varphi$.** Uniformly convergent $\varphi_k\to\varphi$ can move $\sigma(C_{\varphi_k})$ from a circle to a disc (automorphism vs. nearby non-automorphism), so approximation by well-understood symbols is useless.
- **Counting-function data is a $\limsup$, not a limit.** Shapiro's formula computes $\|C_\varphi\|_e$ but $r_e(C_\varphi)=\lim_n\|C_{\varphi_n}\|_e^{1/n}$ requires iterated counting functions $N_{\varphi_n}$; $N_{\varphi_n}$ is not expressible in $N_\varphi$, and submultiplicativity is lossy.
- **Boundary regularity is doing hidden work.** Kamowitz's disc theorem uses analyticity of $\varphi$ across $\omega$ to build eigenfunctions $(1-\bar\omega z)^{s}$-type; when $\varphi$ merely has an angular derivative, the model conjugation is only defined on a horocyclic region and the resulting eigenfunctions need not lie in $H^2$.
- **Invariant subspace entanglement.** Nordgren–Rosenthal–Wintrobe (1987) proved the invariant subspace problem for separable Hilbert space is equivalent to a statement about minimal invariant subspaces of $C_\varphi$ for a hyperbolic automorphism $\varphi$. Any complete fine structure theory for these operators would have to solve, or at least confront, ISP.

## 6. The Gap

Proven (Section 4) covers: compact symbols, all linear-fractional symbols, symbols analytic on $\overline{\mathbb{D}}$, inner symbols, and univalent/finitely valent symbols with an interior fixed point. The general statement in Section 1 covers **all** analytic self-maps.

The precise barrier is a single inequality. For $\varphi$ with interior fixed point $a$, $\lambda=\varphi'(a)$, one always has
$$r_e(C_\varphi)\ \ge\ |\lambda|^{p(\sigma)/2}$$
(the eigenvalues $\lambda^n$ with $2n<p(\sigma)$ are the easy direction, plus a limiting argument). The reverse inequality
$$r_e(C_\varphi)\ \le\ |\lambda|^{p(\sigma)/2}$$
is proved only when $\varphi$ is finitely valent, where a Riesz-type factorisation of $\sigma$ and the Hardy-number geometry of $\sigma(\mathbb{D})$ are available. **Crossing the gap means producing an estimate on $\|C_{\varphi_n}\|_e$ that depends on the mean growth of $\sigma$ but not on its valence.** Symmetrically, for boundary DW point the gap is between "analytic across $\omega$" (Kamowitz: full disc of radius $\lambda^{-1/2}$) and "finite angular derivative at $\omega$", where even whether $\sigma(C_\varphi)$ is a disc, an annulus, or neither is unknown for general $\varphi$.

## 7. Current Research (as of June 2026)

- **Model-theoretic school** (descendants of Bourdon–Shapiro–Poggi-Corradini): extending the Hardy-number formula past finite valence via Nevanlinna-class geometric function theory on the Koenigs domain. Partial results for symbols of bounded valence on horocycles. *(frontier — verify)*
- **Weighted composition operators** $W_{u,\varphi}f=u\cdot(f\circ\varphi)$: spectra computed for linear-fractional $\varphi$ with $u$ analytic on $\overline{\mathbb{D}}$; used as a testing ground because the weight breaks the automorphism rigidity that obstructs perturbation.
- **Semigroup approach.** For $\varphi_t$ a semiflow of self-maps with generator $G$, $\sigma(C_{\varphi_t})$ is analysed by spectral mapping from the generator's spectrum; effective for parabolic and hyperbolic families, and it recovers Cowen's spiral. Groups in Sevilla (Contreras, Díaz-Madrigal), Málaga (Montes-Rodríguez), Madrid (Gallardo-Gutiérrez), Bern/Leeds (Partington, Chalendar).
- **Operator-algebraic reformulations.** Essential spectrum of $C_\varphi$ for inner $\varphi$ via Cuntz-algebra representations of the transfer operator; gives the $\overline{\mathbb{D}}$ answer for inner symbols from a different direction, and is being pushed toward the finite Blaschke case with non-zero DW point. *(frontier — verify)*
- **Numerical range and spectral containment** results for $C_\varphi$ on $H^2$ and on Dirichlet-type spaces $\mathcal{D}_\alpha$, where the same univalent/non-univalent dichotomy appears with different exponents.

## 8. Future Work

- Prove or refute $r_e(C_\varphi)=|\lambda|^{p(\sigma)/2}$ for arbitrary analytic $\varphi$ with interior fixed point; the natural test symbols are infinite Blaschke products composed with contractions, where valence is infinite but $\sigma$ still lies in some $H^p$.
- Replace analyticity across the DW point by a Julia–Carathéodory hypothesis in Kamowitz's theorem: does $0<\varphi'(\omega)<1$ alone force $\sigma(C_\varphi)=\{|z|\le\varphi'(\omega)^{-1/2}\}$?
- Compute $\sigma_e(C_\varphi)$ (not just its radius) for parabolic non-automorphisms with a non-linear-fractional symbol; the conjectural answer is a spiral determined by the parabolic model's translation parameter.
- Determine which compact subsets of $\mathbb{C}$ arise as $\sigma(C_\varphi)$ — an inverse spectral problem; discs, annuli, circles, spirals and countable sets are realised, but no classification exists.
- Settle the finer structure (point spectrum, multiplicity, minimal invariant subspaces) for hyperbolic automorphisms, in view of the Nordgren–Rosenthal–Wintrobe equivalence with ISP.

## 9. Key References

- **[Foundational]** E. A. Nordgren. *Composition operators.* Canadian Journal of Mathematics 20 (1968), 442–449.
- **[Foundational]** H. Kamowitz. *The spectra of composition operators on $H^p$.* Journal of Functional Analysis 18 (1975), 132–150.
- **[Foundational]** J. G. Caughran and H. J. Schwartz. *Spectra of compact composition operators.* Proceedings of the American Mathematical Society 51 (1975), 127–130.
- **[Foundational]** C. C. Cowen. *Composition operators on $H^2$.* Journal of Operator Theory 9 (1983), 77–106.
- **[Foundational]** J. H. Shapiro. *The essential norm of a composition operator.* Annals of Mathematics 125 (1987), 375–404.
- **[SOTA / Recent]** P. S. Bourdon and J. H. Shapiro. *Mean growth of Koenigs eigenfunctions.* Journal of the American Mathematical Society 10 (1997), 299–325.
- **[SOTA / Recent]** P. Poggi-Corradini. *The Hardy class of geometric models and the essential spectral radius of composition operators.* Journal of Functional Analysis 143 (1997), 129–156.
- **[SOTA / Recent]** C. C. Cowen and B. D. MacCluer. *Spectra of some composition operators.* Journal of Functional Analysis 125 (1994), 223–251.
- **[SOTA / Recent]** E. A. Nordgren, P. Rosenthal and F. S. Wintrobe. *Invertible composition operators on $H^p$.* Journal of Functional Analysis 73 (1987), 324–344.
- **[Survey]** C. C. Cowen and B. D. MacCluer. *Composition Operators on Spaces of Analytic Functions.* CRC Press, 1995.
- **[Survey]** J. H. Shapiro. *Composition Operators and Classical Function Theory.* Springer-Verlag, 1993.
- **[Survey]** E. A. Gallardo-Gutiérrez and A. Montes-Rodríguez. *The role of the spectrum in the cyclic behavior of composition operators.* Memoirs of the American Mathematical Society 167, no. 791 (2004).

## 10. Worked Example / Concrete Special Case

Take the linear-fractional (indeed affine) symbol
$$\varphi(z)=\frac{1+z}{2},\qquad \varphi(\mathbb{D})\subset\mathbb{D}.$$
Fixed points: $z=(1+z)/2\Rightarrow z=1$. So $\omega=1\in\partial\mathbb{D}$, $\varphi'(1)=\tfrac12=\lambda$: a hyperbolic non-automorphism. Note $\varphi$ is analytic on $\overline{\mathbb{D}}$, so Kamowitz applies and predicts $\sigma(C_\varphi)=\{|z|\le\sqrt2\}$. Verify by hand.

**Iterates.** $\varphi_n(z)=1-2^{-n}(1-z)$, so $\varphi_n(0)=1-2^{-n}$.

**Spectral radius, upper bound.**
$$\|C_\varphi^n\|=\|C_{\varphi_n}\|\le\Big(\tfrac{1+\varphi_n(0)}{1-\varphi_n(0)}\Big)^{1/2}=\big(2^{n+1}-1\big)^{1/2},$$
hence $r(C_\varphi)\le\lim_n 2^{(n+1)/(2n)}=\sqrt2$.

**Lower bound via kernels.** $C_{\varphi_n}^{*}K_w=K_{\varphi_n(w)}$, so for $w\in(0,1)$,
$$\|C_\varphi^n\|\ \ge\ \frac{\|K_{\varphi_n(w)}\|}{\|K_w\|}=\Big(\frac{1-w^2}{1-\varphi_n(w)^2}\Big)^{1/2}
\xrightarrow[w\to1^-]{}\ \Big(\frac{1}{\varphi_n'(1)}\Big)^{1/2}=2^{n/2}.$$
So $r(C_\varphi)\ge\sqrt2$, and $r(C_\varphi)=\sqrt2$.

**Eigenfunctions fill the disc.** Conjugate to the right half-plane by $w=\frac{1+z}{1-z}$. A direct computation gives the induced map $\Phi(w)=2w+1$, with fixed point $w=-1$; setting $u=w+1=\frac{2}{1-z}$ turns it into the dilation $u\mapsto 2u$. For $s\in\mathbb{C}$ put
$$f_s(z)=(1-z)^{s}\quad\big(=2^{s}u^{-s}\big).$$
Then
$$f_s(\varphi(z))=\Big(1-\tfrac{1+z}{2}\Big)^{s}=\Big(\tfrac{1-z}{2}\Big)^{s}=2^{-s}f_s(z),$$
so $C_\varphi f_s=2^{-s}f_s$. Membership: $(1-z)^{s}\in H^2$ iff $\operatorname{Re}s>-\tfrac12$. Since $|2^{-s}|=2^{-\operatorname{Re}s}$, the condition $\operatorname{Re}s>-\tfrac12$ is exactly $|2^{-s}|<2^{1/2}=\sqrt2$, and every value in $0<|\mu|<\sqrt2$ is attained. Hence
$$\sigma_p(C_\varphi)=\{\mu:0<|\mu|<\sqrt2\},\qquad \sigma(C_\varphi)=\{|z|\le\sqrt2\},$$
a full disc with dense point spectrum — no eigenvalue sequence, no annulus.

**Why this is the model of the difficulty.** Everything above used that $\varphi$ extends analytically across $\omega=1$ so that $(1-z)^s$ is an honest eigenfunction. Perturb $\varphi$ to a self-map with the same angular derivative $\tfrac12$ at $1$ but a boundary singularity there (e.g. $\varphi(z)=1-\tfrac12(1-z)\exp\!\big(-\varepsilon\sqrt{1-z}\big)$ for small $\varepsilon>0$): the spectral radius $\sqrt2$ survives by the kernel argument, but the eigenfunction construction fails, and whether $\sigma(C_\varphi)$ is still the disc of radius $\sqrt2$ is exactly the open case of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*