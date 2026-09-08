---
id: 05-analysis/a2-theorem-dimensional-dependence
title: "Muckenhoupt Weight A-infinity Dimensional Dependence"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Muckenhoupt Weight A-infinity Dimensional Dependence

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/a2-theorem-dimensional-dependence` · **Status:** open

## 1. Problem Statement / Conjecture

The $A_2$ theorem (Hytönen, 2012) states that for every Calderón–Zygmund operator $T$ on $\mathbb{R}^n$ and every weight $w \in A_2$,
$$\|T\|_{L^2(w)\to L^2(w)} \;\le\; C(n,T)\,[w]_{A_2},$$
with the linear power of $[w]_{A_2}$ sharp. **The dimensional behaviour of $C(n,T)$ is not understood.** Every known proof produces a constant that is at least exponential in $n$, because it passes through dyadic structures whose combinatorics cost $2^n$ or $3^n$.

Two linked open questions:

- **(Q1) Dimension-free weighted Riesz bound.** For the Riesz transforms $R_j$, $j=1,\dots,n$, is
  $$\sup_{n\ge 1}\ \sup_{j\le n}\ \sup_{w\in A_2(\mathbb{R}^n)} \frac{\|R_j\|_{L^2(w)\to L^2(w)}}{[w]_{A_2}} \;<\; \infty\,?$$
  Unweighted, $\|R_j\|_{L^p\to L^p}$ is dimension-free (Stein, 1983). Whether that survives the sharp weighted scaling is open.
- **(Q2) Dimension-free $A_\infty$ constants.** In the sharp reverse Hölder inequality and in the $A_2$–$A_\infty$ refinements of Hytönen–Pérez, the exponent gain and the operator constants carry a factor $2^{n}$ inherited from the dyadic Calderón–Zygmund stopping-time decomposition. Is that factor an artefact of the method, or is some dimensional growth genuine?

A complete resolution means either an absolute constant (with a proof avoiding dimensional dyadic combinatorics) or a family of weights $w_n \in A_2(\mathbb{R}^n)$ with $[w_n]_{A_2}$ bounded and $\|R_1\|_{L^2(w_n)} \to \infty$.

## 2. Mathematical Foundations

**Weights.** $w \ge 0$ locally integrable. For a cube $Q$ write $\fint_Q w = |Q|^{-1}\int_Q w$. The Muckenhoupt characteristics are
$$[w]_{A_p} \;=\; \sup_{Q}\ \Big(\fint_Q w\Big)\Big(\fint_Q w^{-\frac{1}{p-1}}\Big)^{p-1},\qquad 1<p<\infty,$$
so $[w]_{A_2} = \sup_Q (\fint_Q w)(\fint_Q w^{-1})$. Duality: with $\sigma = w^{-1}$ one has $[\sigma]_{A_2}=[w]_{A_2}$.

**$A_\infty$.** The Fujii–Wilson characteristic
$$[w]_{A_\infty} \;=\; \sup_Q \frac{1}{w(Q)}\int_Q M(w\chi_Q)\,dx$$
satisfies $[w]_{A_\infty} \le c_n [w]_{A_p}$ and is the correct (smallest) $A_\infty$ constant; $M$ is the Hardy–Littlewood maximal operator.

**Sharp reverse Hölder (Hytönen–Pérez–Rela, 2012).** If $w\in A_\infty(\mathbb{R}^n)$ and
$$r \;=\; 1+\frac{1}{2^{n+11}[w]_{A_\infty}}, \qquad\text{then}\qquad \Big(\fint_Q w^{r}\Big)^{1/r} \;\le\; 2 \fint_Q w .$$
The $2^{n+11}$ is exactly the disputed dimensional factor.

**Sparse domination (Lerner, Lacey, Conde-Alonso–Rey).** For a CZ operator $T$ there exist sparse families $\mathcal{S}$ (each $Q\in\mathcal S$ contains $E_Q \subset Q$ pairwise disjoint with $|E_Q| \ge \tfrac12 |Q|$) such that pointwise
$$|Tf(x)| \;\lesssim_{n} \; \|T\|_{CZ}\sum_{Q\in\mathcal{S}} \Big(\fint_Q |f|\Big)\chi_Q(x),$$
and the sparse form obeys the Hytönen–Pérez mixed bound
$$\|T\|_{L^2(w)} \;\le\; c_n \|T\|_{CZ}\,[w]_{A_2}^{1/2}\big([w]_{A_\infty}^{1/2}+[\sigma]_{A_\infty}^{1/2}\big) \;\le\; c_n\|T\|_{CZ}[w]_{A_2}.$$
The dimensional cost enters through (i) the $3^n$ shifted dyadic lattices used to dominate arbitrary cubes, (ii) the $2^n$ in the dyadic CZ decomposition, and (iii) $\|M\|_{L^p}$ constants.

**Riesz transforms.** $\widehat{R_jf}(\xi) = -i\frac{\xi_j}{|\xi|}\hat f(\xi)$; the Riesz vector $R=(R_1,\dots,R_n)$ satisfies $\|\,|Rf|\,\|_{L^p} \le C_p \|f\|_{L^p}$ with $C_p$ independent of $n$ (Stein).

## 3. History & State of the Art (SOTA)

- **1972.** Muckenhoupt characterises the weights for which $M$ is bounded on $L^p(w)$.
- **1974.** Coifman–Fefferman extend to CZ operators via the good-$\lambda$ method; constants are qualitative and badly dimension-dependent.
- **1993.** Buckley obtains the sharp power: $\|M\|_{L^p(w)} \lesssim_n [w]_{A_p}^{1/(p-1)}$.
- **2002–2008.** Petermichl–Volberg prove the linear $A_2$ bound for the Beurling–Ahlfors operator (settling a borderline quasiregular-map problem); Petermichl proves it for the Hilbert transform (2007) and for the Riesz transforms (2008) via random dyadic shift representation. The constants are exponential in $n$.
- **2012.** Hytönen proves the $A_2$ theorem in full generality by representing $T$ as an average of dyadic shifts.
- **2013.** Lerner gives a short proof via local mean oscillation; Lacey (2017) and Lerner (2016) reduce it to sparse domination. Hytönen–Pérez sharpen to the mixed $A_2$–$A_\infty$ form.
- **Present.** No proof yields $C(n,T)$ better than exponential in $n$, and no lower bound better than $O(1)$ is known for the Riesz transforms. The gap between $O(1)$ and $2^{cn}$ is the state of the art.

## 4. Partial Results / Verified Cases

- **$n=1$ (Hilbert transform).** Sharp: $\|H\|_{L^2(w)} \le C[w]_{A_2}$ with an explicit absolute $C$ (Petermichl 2007), extremal at $w(x)=|x|^{1-\delta}$.
- **$n=2$ (Beurling–Ahlfors).** $\|B\|_{L^p(w)}\lesssim [w]_{A_p}^{\max(1,1/(p-1))}$, absolute constants (Petermichl–Volberg 2002; Dragičević–Volberg).
- **Unweighted, all $n$.** $\|R_j\|_{L^p\to L^p}\le C_p$ with $C_p$ dimension-free (Stein 1983; Duoandikoetxea–Rubio de Francia 1986); $\|M_{\text{balls}}\|_{L^p}\le C_p$ dimension-free for $p>1$ (Stein–Strömberg).
- **Martingale models.** For the discrete/continuous-time martingale transforms and the Bellman-function models of the Riesz vector, dimension-free weighted estimates are known (Bañuelos–Osękowski; Domelevo–Petermichl), giving the *conjectured* answer inside the probabilistic model.
- **Restricted weight classes.** For radial power weights $w=|x|^a$, $-n<a<n$, dimension-free weighted bounds for $R_j$ follow from explicit kernel computation; likewise for $w$ in $A_1$ with $[w]_{A_1}$ small, where Rubio de Francia extrapolation from the dimension-free unweighted bound applies with controlled loss.
- **Rough kernels (worse powers).** For $T_\Omega$ with $\Omega\in L^\infty(S^{n-1})$, $\|T_\Omega\|_{L^2(w)}\lesssim_n [w]_{A_2}^2$ (Hytönen–Roncal–Tapiola, 2017) — quadratic, and the dimensional constant is again exponential.

## 5. Principal Obstacles

- **Dyadic combinatorics is intrinsically exponential.** Both the representation theorem and sparse domination replace balls/cubes by dyadic ones; covering an arbitrary cube requires $3^n$ shifted lattices, and the CZ stopping-time selection loses $2^n$ per generation. This is not a slack estimate to be tightened — it is the price of the dyadic model itself.
- **Sparseness is dimensional.** The $\tfrac12$-sparse family produced from a CZ decomposition has packing constants depending on $n$; the sparse *form* itself is dimension-free, but the *domination step* is not.
- **The extremal weights are one-dimensional.** All known sharp examples ($w=|x|^{1-\delta}$ and its dyadic analogues) are essentially $1$-D, so they cannot detect dimensional growth. There is no known machinery for producing genuinely high-dimensional $A_2$ extremisers.
- **Stein's dimension-free method does not survive weights.** Stein's proof uses the method of rotations plus Littlewood–Paley/heat-semigroup square functions and the $L^p$ boundedness of the spherical average — the square-function step uses unweighted Plancherel/Fourier tools that have no $[w]_{A_2}$-linear weighted counterpart.
- **Method of rotations costs $\sqrt n$ or worse.** Writing $R_j$ as an average of directional Hilbert transforms transfers the $1$-D sharp bound but with a factor from $\int_{S^{n-1}}|\theta_j|d\sigma \sim n^{-1/2}$ mismatch and, crucially, requires uniform weighted bounds for directional Hilbert transforms — a known hard problem (related to the Zygmund conjecture on directional maximal operators).
- **$A_\infty$ is not scale-neutral.** $[w]_{A_\infty}$ compares $w$ against $Mw$, so any quantitative reverse-Hölder argument inherits the maximal operator's dimensional constant, and dimension-free maximal bounds are known only for $p>1$ and only for balls/cubes, not in weighted form.

## 6. The Gap

Proven: for each fixed $n$, a linear-in-$[w]_{A_2}$ bound with a constant of the form $c\,2^{cn}$; and, for each fixed $p>1$ and all $n$, a dimension-free *unweighted* bound. Conjectured: both at once.

The precise missing step is a **dimension-free domination principle**: a decomposition of $R_j$ (or of a general CZ operator with dimension-free kernel constants) by positive sparse-type forms whose construction avoids the $2^n$ CZ selection and the $3^n$ lattice trick. Equivalently, one needs either

1. a weighted square-function/semigroup argument realising Stein's rotation-invariant proof with $A_2$-linear weighted control, or
2. a lower-bound construction: weights $w_n$ on $\mathbb{R}^n$ with $\sup_n[w_n]_{A_2}<\infty$ and $\|R_1\|_{L^2(w_n)}\to\infty$.

No partial progress exists on either side beyond $n\le 2$.

## 7. Current Research (as of June 2026)

- **Bellman/martingale school (Toulouse, Purdue, Michigan State, Kent State).** Domelevo–Petermichl and Bañuelos–Osękowski pursue continuous-time sparse domination and dimensionless Bellman functions for the Riesz vector; the martingale model already gives dimension-free weighted estimates, and the open step is transference back to $\mathbb{R}^n$ *(frontier — verify)*.
- **Matrix and convex-body weights.** Domelevo–Petermichl–Treil–Volberg (2024) showed the *matrix* $A_2$ conjecture fails — the sharp power for matrix weights is $[W]_{A_2}^{3/2}\log[W]_{A_2}$-type rather than linear. This reshaped expectations about how robust linear $A_2$ scaling is, and prompted renewed scrutiny of the scalar dimensional constants.
- **Sparse-form optimisation.** Groups around Lerner, Lacey, Conde-Alonso and Ombrosi are computing explicit dimensional constants in sparse domination, asking whether the $3^n$ lattice count can be replaced by an $O(n)$ or $O(1)$ family.
- **Dimension-free harmonic analysis programme.** Bourgain–Mirek–Stein–Wróbel work on dimension-free estimates for maximal functions over convex bodies; the weighted analogue (dimension-free $\|M\|_{L^p(w)}\lesssim [w]_{A_p}^{1/(p-1)}$) is being tested for balls and $\ell^q$ balls *(frontier — verify)*.

## 8. Future Work

- Prove or refute a **dimension-free weighted maximal bound** first: $\|M_{\text{balls}}\|_{L^2(w)} \le C[w]_{A_2}$ with $C$ absolute. This is strictly easier than (Q1) and would already break the $2^n$ barrier.
- Sharpen the reverse Hölder exponent to $r-1 \asymp c/[w]_{A_\infty}$ with $c$ absolute, using ball-based (not dyadic) stopping times or a heat-semigroup regularisation.
- Search for lower bounds via **high-dimensional tensor products**: if $w_n(x)=\prod_{j\le n} u(x_j)$, then $[w_n]_{A_2}=[u]_{A_2}^n$ blows up, so genuinely non-product high-dimensional constructions are needed — a concrete, unexplored construction problem.
- Transfer the matrix-weight counterexample technology of Domelevo–Petermichl–Treil–Volberg to build scalar weights in growing dimension.

## 9. Key References

- **[Foundational]** B. Muckenhoupt. *Weighted norm inequalities for the Hardy maximal function.* Transactions of the American Mathematical Society **165** (1972), 207–226.
- **[Foundational]** R. Coifman, C. Fefferman. *Weighted norm inequalities for maximal functions and singular integrals.* Studia Mathematica **51** (1974), 241–250.
- **[Foundational]** S. M. Buckley. *Estimates for operator norms on weighted spaces and reverse Jensen inequalities.* Transactions of the AMS **340** (1993), 253–272.
- **[Foundational]** E. M. Stein. *Some results in harmonic analysis in $\mathbb{R}^n$ for $n\to\infty$.* Bulletin of the AMS (N.S.) **9** (1983), 71–73.
- **[SOTA]** T. Hytönen. *The sharp weighted bound for general Calderón–Zygmund operators.* Annals of Mathematics **175** (2012), 1473–1506.
- **[SOTA]** S. Petermichl. *The sharp bound for the Hilbert transform on weighted Lebesgue spaces in terms of the classical $A_p$ characteristic.* American Journal of Mathematics **129** (2007), 1355–1375.
- **[SOTA]** S. Petermichl, A. Volberg. *Heating of the Ahlfors–Beurling operator: weakly quasiregular maps on the plane are quasiregular.* Duke Mathematical Journal **112** (2002), 281–305.
- **[SOTA]** T. Hytönen, C. Pérez. *Sharp weighted bounds involving $A_\infty$.* Analysis & PDE **6** (2013), 777–818.
- **[SOTA]** T. Hytönen, C. Pérez, E. Rela. *Sharp reverse Hölder property for $A_\infty$ weights on spaces of homogeneous type.* Journal of Functional Analysis **263** (2012), 3883–3899.
- **[SOTA]** A. K. Lerner. *A simple proof of the $A_2$ conjecture.* International Mathematics Research Notices **2013**, 3159–3170.
- **[SOTA]** M. T. Lacey. *An elementary proof of the $A_2$ bound.* Israel Journal of Mathematics **217** (2017), 181–195.
- **[SOTA / Recent]** K. Domelevo, S. Petermichl, S. Treil, A. Volberg. *The matrix $A_2$ conjecture fails, i.e. $3/2>1$.* Preprint, 2024.
- **[Survey]** A. K. Lerner, F. Nazarov. *Intuitive dyadic calculus: the basics.* Expositiones Mathematicae **37** (2019), 225–265.
- **[Survey]** J. Duoandikoetxea. *Fourier Analysis.* Graduate Studies in Mathematics **29**, American Mathematical Society, 2001.

## 10. Worked Example / Concrete Special Case

Take the radial power weight $w(x)=|x|^{a}$ on $\mathbb{R}^n$, and compute its $A_2$ characteristic on the unit ball $B=B(0,1)$. With $\sigma_{n-1}=|S^{n-1}|$,
$$\int_B |x|^a\,dx = \sigma_{n-1}\int_0^1 r^{a+n-1}dr = \frac{\sigma_{n-1}}{a+n},\qquad |B|=\frac{\sigma_{n-1}}{n},$$
so $\fint_B |x|^a = \frac{n}{n+a}$ and $\fint_B |x|^{-a}=\frac{n}{n-a}$, valid for $|a|<n$. Hence
$$\Big(\fint_B w\Big)\Big(\fint_B w^{-1}\Big) = \frac{n^2}{n^2-a^2},$$
and this ball is essentially extremal, giving $[w]_{A_2}\asymp \dfrac{n^2}{n^2-a^2}$.

Now set $a=(1-\delta)n$ with $0<\delta<1$. Then
$$[w]_{A_2}\;\asymp\;\frac{1}{1-(1-\delta)^2}=\frac{1}{\delta(2-\delta)}\;\approx\;\frac{1}{2\delta},$$
which is **independent of $n$**. So this natural one-parameter family of genuinely $n$-dimensional weights sits at bounded $A_2$ characteristic in every dimension. If $C(n,R_j)$ really grew like $2^n$, one would need it to be invisible on such families — and indeed, computing $\|R_j\|_{L^2(|x|^a)}$ directly via the Mellin transform in the radial variable and spherical-harmonic decomposition gives a bound $\lesssim 1/\delta$ with no dimensional factor. This is the basic evidence for (Q1): every family we can compute is dimension-free.

The same family probes (Q2). With $a=-(1-\delta)n$ (so $w=|x|^{-(1-\delta)n}$), $w\in RH_r$ exactly when $r(1-\delta)n<n$, i.e. $r<\frac{1}{1-\delta}$, so the reverse-Hölder gain is
$$r-1 \;<\; \frac{\delta}{1-\delta}\;\approx\;\delta ,$$
while $[w]_{A_\infty}\lesssim [w]_{A_2}\asymp 1/(2\delta)$. Thus on this family the sharp reverse Hölder inequality holds with
$$r-1 \asymp \frac{c}{[w]_{A_\infty}},\qquad c \text{ absolute},$$
whereas the Hytönen–Pérez–Rela theorem only guarantees $r-1 = 2^{-(n+11)}/[w]_{A_\infty}$. The example does not disprove the $2^{n+11}$ — it shows no known weight family attains it, which is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*