---
id: 05-analysis/bellman-function-sharp-constants
title: "Nazarov-Treil-Volberg Bellman Function Sharpness"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nazarov-Treil-Volberg Bellman Function Sharpness

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/bellman-function-sharp-constants` · **Status:** open

## 1. Problem Statement / Conjecture

The Bellman function method of Nazarov, Treil and Volberg (NTV) reduces a harmonic-analytic inequality to a pointwise question: does there exist a function on a finite-dimensional domain that is locally concave and dominates a given obstacle? The method is *lossless in principle* — the optimal such function is exactly the sharp constant. The open problem is whether it is lossless *in practice*.

Three linked questions, all open:

1. **Identification.** For a Bellman setup with domain $\Omega\subset\mathbb{R}^d$ and obstacle $\Phi$, is the *true* Bellman function $\mathbf{B}$ (a supremum over test functions) always equal to $\mathfrak{B}$, the least locally concave majorant of $\Phi$ on $\Omega$? Equality is a theorem for $d\le 2$ and for convex $\Omega$ under mild conditions; for $d\ge 3$ with non-convex $\Omega$ — the case relevant to weighted estimates — no general proof exists.
2. **Computation.** Can $\mathfrak{B}$ be computed in closed form for the canonical weighted problems? Concretely: determine the exact Bellman function for the martingale transform / Haar multiplier on $L^2(w)$, $w\in A_2$, and hence the sharp constant $C$ in $\|T_\varepsilon\|_{L^2(w)\to L^2(w)}\le C\,[w]_{A_2}$.
3. **Sharpness of the resulting constants.** Is the Iwaniec conjecture $\|S\|_{L^p(\mathbb{C})\to L^p(\mathbb{C})}=p^*-1$, $p^*=\max(p,\tfrac{p}{p-1})$, provable by exhibiting the corresponding Bellman function — or is there a structural obstruction making the method strictly lossy for this class?

A complete resolution means either an explicit $\mathfrak{B}$ with matching extremizers, or a proof that no locally concave majorant with the conjectured boundary behaviour exists.

## 2. Mathematical Foundations

**Dyadic setup.** Let $\mathcal{D}$ be the dyadic lattice on an interval $J$, $h_I=|I|^{-1/2}(\chi_{I_+}-\chi_{I_-})$ the $L^2$-normalized Haar system, $\langle\varphi\rangle_I=|I|^{-1}\int_I\varphi$. A Haar multiplier is $T_\varepsilon\varphi=\sum_{I\in\mathcal{D}}\varepsilon_I\langle\varphi,h_I\rangle h_I$, $|\varepsilon_I|\le1$. The $A_2$ characteristic of $w>0$ is
$$[w]_{A_2}=\sup_{I\in\mathcal{D}}\langle w\rangle_I\,\langle w^{-1}\rangle_I\ \ge 1 .$$

**The Bellman function.** Given a "value" map $\Psi:\varphi\mapsto\mathbb{R}^d$ built from averages and a payoff $\Phi$, set
$$\mathbf{B}(x)=\sup\Big\{\tfrac{1}{|J|}\textstyle\int_J\Phi(\varphi)\ :\ \Psi(\varphi)_J=x\Big\},\qquad x\in\Omega\subset\mathbb{R}^d .$$
Splitting $J$ into children forces the **main inequality** (local concavity along admissible chords):
$$\mathbf{B}(x)\ \ge\ \tfrac12\big(\mathbf{B}(x_+)+\mathbf{B}(x_-)\big)\quad\text{whenever } x=\tfrac{x_++x_-}{2},\ [x_-,x_+]\subset\Omega .$$
Conversely any locally concave $B\ge\Phi$ dominates $\mathbf{B}$ by induction over scales — this is the **Bellman induction**, and it is why sharp constants are in reach.

**Infinitesimal form.** Where $\mathfrak{B}$ is $C^2$,
$$D^2\mathfrak{B}(x)\le 0,\qquad \det D^2\mathfrak{B}(x)=0 ,$$
a *homogeneous Monge–Ampère equation*. Degeneracy means $\mathfrak{B}$ is linear along a distinguished direction; the domain is filled by a **foliation** of extremal line segments (Vasyunin–Volberg), and computing $\mathfrak{B}$ amounts to finding this foliation and integrating an ODE for the "torsion" along it.

**Model $A_2$ domain.** For weighted estimates one works on
$$\Omega_Q=\{(u,v,w)\in\mathbb{R}^3_+ :\ 1\le uv\le Q\},\qquad Q=[w]_{A_2},$$
with $u=\langle w\rangle_I$, $v=\langle w^{-1}\rangle_I$ and extra variables for $\langle\varphi\rangle_I$, $\langle\psi\rangle_I$. The domain is **not convex** — the source of every difficulty below. The classical linear-in-$Q$ result reads
$$\|T_\varepsilon\|_{L^2(w)}\le C\,[w]_{A_2},$$
with $C$ finite but not identified.

**Burkholder's function.** For martingale transforms in $L^p$ the exact Bellman function is known:
$$U_p(x,y)=p^*\Big(|y|-\big(1-\tfrac{1}{p^*}\big)|x|\Big)\big(|x|+|y|\big)^{p-1},$$
zigzag-concave, giving the sharp constant $p^*-1$.

## 3. History & State of the Art (SOTA)

- **1984.** Burkholder computes the exact function for martingale transforms, obtaining $\|T\|_{L^p}=p^*-1$ — the prototype, though not phrased as "Bellman".
- **1996–1999.** Nazarov and Treil, *The hunt for a Bellman function* (Algebra i Analiz 8, 1996; St. Petersburg Math. J. 8, 1997), and Nazarov–Treil–Volberg, *The Bellman functions and two-weight inequalities for Haar multipliers* (J. Amer. Math. Soc. 12, 1999), import stochastic optimal control into harmonic analysis and establish the induction-on-scales formalism.
- **2000–2002.** Wittwer proves the linear $[w]_{A_2}$ bound for the martingale transform by Bellman; Petermichl–Volberg apply it to the Beurling–Ahlfors operator, settling a borderline case of Astala's quasiregularity problem.
- **2003–2011.** Vasyunin computes exact Bellman functions for the reverse Hölder inequality; Slavin–Vasyunin do the integral John–Nirenberg inequality; Melas solves the dyadic maximal operator.
- **2012.** Hytönen proves the $A_2$ theorem for all Calderón–Zygmund operators — but via dyadic representation, *not* Bellman, and with no explicit constant.
- **2016–2018.** Ivanisvili, Stolyarov, Vasyunin, Zatitskiy give a complete theory of Bellman functions for BMO on an interval: for **every** continuous obstacle, $\mathbf{B}=\mathfrak{B}$ and the foliation is classified.
- **2020.** Vasyunin–Volberg, *The Bellman Function Technique in Harmonic Analysis* (Cambridge Univ. Press), codifies the method and states the open cases.

## 4. Partial Results / Verified Cases

| Setting | Sharp constant / status |
|---|---|
| Martingale transform, $L^p(\mathbb{R})$, $1<p<\infty$ | $p^*-1$, exact function known (Burkholder 1984) |
| Martingale transform, $L^2(w)$, $w\in A_2$ | $\|T_\varepsilon\|\le C[w]_{A_2}$, linear power **sharp**; $C$ unknown (Wittwer 2000) |
| Hilbert transform, Riesz transforms, $L^2(w)$ | linear in $[w]_{A_2}$, power sharp (Petermichl 2007) |
| All CZOs, $L^2(w)$ | linear in $[w]_{A_2}$ (Hytönen 2012); constant not explicit |
| BMO$(J)$, $d=2$ Bellman domain, any obstacle | fully solved; $\mathbf{B}=\mathfrak{B}$, foliation classified (Ivanisvili–Stolyarov–Vasyunin–Zatitskiy 2016, 2018) |
| Weak-form John–Nirenberg, $L^2$-based BMO norm | sharp exponential rate and prefactor (Vasyunin–Volberg, Proc. LMS 2014) |
| Reverse Hölder for $A_p$ weights on $\mathbb{R}$ | exact constant (Vasyunin 2003) |
| Dyadic maximal operator, $L^p$ | exact Bellman function; constant $\big(\tfrac{p}{p-1}\big)^p$ (Melas 2005) |
| Beurling–Ahlfors $S$ on $L^p(\mathbb{C})$ | $\|S\|\le c\,(p^*-1)$ with $c\approx1.4$–$2$; conjectured $c=1$ *(frontier — verify the current best $c$)* |

Everything solved exactly sits in Bellman domains of **two** effective variables after homogeneity reduction, or has a convex domain.

## 5. Principal Obstacles

- **Non-convex domain.** On $\Omega_Q=\{1\le uv\le Q\}$ concavity is only required along chords staying inside $\Omega_Q$. The least *locally* concave majorant need not equal the least *globally* concave one, and standard convex-duality (Legendre transform, support functions) breaks: there is no global dual description of $\mathfrak{B}$.
- **Dimension $\ge3$.** The homogeneous Monge–Ampère equation $\det D^2 B=0$ has a $(d-1)$-parameter family of possible foliations for $d\ge3$; the extremal segments can be higher-dimensional flat faces, and no classification of admissible foliations exists. All complete solutions have $d\le2$ after reduction.
- **Low regularity.** $\mathfrak{B}$ is generally only locally Lipschitz, not $C^2$; viscosity-solution theory for degenerate elliptic Monge–Ampère gives existence but not uniqueness among locally concave functions on non-convex sets, so a PDE solve does not certify minimality.
- **No transfer of sharpness.** For CZOs, the $A_2$ theorem passes through dyadic representation or sparse domination; both lose absolute constants ($\sum_k 2^{-\delta k/2}$-type sums, sparse-family selection with a factor $\ge 2$). A sharp Bellman function for one dyadic model does not yield a sharp constant for the continuous operator.
- **Extremizers may not exist.** For $\|S\|_{L^p}$ the conjectured extremizers are only asymptotic; a Bellman proof must produce a majorant with *exactly* matching boundary behaviour, and small perturbations destroy local concavity on the non-convex domain.

## 6. The Gap

Proven (§4): exactness of $\mathfrak{B}$ and closed forms whenever the reduced domain is $2$-dimensional or convex. Claimed (§1): the same for the genuinely $3$-and-higher-dimensional non-convex $A_2$-type domains.

The precise missing step: construct, or prove non-existence of, a locally concave function on
$$\Omega_Q=\{(u,v,f,g):\ 1\le uv\le Q\}$$
that majorizes the martingale-transform obstacle and whose value at the diagonal equals $C\,Q$ with the smallest admissible $C$. Equivalently — classify the foliations of $\Omega_Q$ by extremal segments. Every known bound uses an *ad hoc* concave majorant which is provably not minimal, so the gap is exactly the distance between a working supersolution and the true least supersolution.

## 7. Current Research (as of June 2026)

- **St. Petersburg (POMI) school** — Vasyunin, Stolyarov, Zatitskiy: extending the complete BMO theory to weighted and multi-parameter domains; the "evolution of foliations" machinery is the main tool.
- **Michigan State / Volberg's group**: Bellman functions on the Hamming cube and for Gaussian/discrete isoperimetry, where the domain is again non-convex.
- **Ivanisvili and collaborators (UC Irvine)**: enhanced Bellman techniques for Poincaré-type and $\Phi$-entropy inequalities; sharp $L^1$-$L^\infty$ interpolation of BMO. *(frontier — verify recent preprints)*
- **Sparse domination community** (Lerner, Lacey, Conde-Alonso, Rey): pursuing sharp *constants* rather than sharp powers, which would give an independent benchmark against which any candidate Bellman function can be tested.
- **Probabilistic route** (Bañuelos, Osękowski): stochastic-integral and orthogonal-martingale constructions giving improved constants for the Beurling–Ahlfors operator; Osękowski's Burkholder-function calculus is the closest competitor to Bellman.

## 8. Future Work

- Prove a general identification theorem $\mathbf{B}=\mathfrak{B}$ on non-convex domains under a "chord-connectedness" hypothesis.
- Develop numerical Monge–Ampère solvers on $\Omega_Q$ to *estimate* the optimal $C$ before attempting a closed form; a numerically established gap from the current $C$ would already be informative.
- Settle the two-dimensional slices of $\Omega_Q$ obtained by freezing $uv=Q$ (the boundary), where the problem becomes a one-parameter ODE.
- Transfer sharp dyadic constants to continuous operators by averaging over random lattices with the exact averaging constant tracked.
- Test whether the Iwaniec conjecture admits *any* Bellman certificate, by checking necessary conditions (obstacle behaviour at infinity) that a majorant must satisfy.

## 9. Key References

- **[Foundational]** D. L. Burkholder. *Boundary value problems and sharp inequalities for martingale transforms.* Annals of Probability 12(3), 1984, 647–702.
- **[Foundational]** F. Nazarov, S. Treil. *The hunt for a Bellman function: applications to estimates for singular integral operators and to other classical problems of harmonic analysis.* Algebra i Analiz 8(5), 1996; St. Petersburg Mathematical Journal 8, 1997, 721–824.
- **[Foundational]** F. Nazarov, S. Treil, A. Volberg. *The Bellman functions and two-weight inequalities for Haar multipliers.* Journal of the American Mathematical Society 12(4), 1999, 909–928.
- **[Foundational]** F. Nazarov, S. Treil, A. Volberg. *Bellman function in stochastic control and harmonic analysis.* In: Systems, Approximation, Singular Integral Operators, and Related Topics, Operator Theory: Advances and Applications 129, Birkhäuser, 2001, 393–423.
- **[SOTA]** J. Wittwer. *A sharp estimate on the norm of the martingale transform.* Mathematical Research Letters 7(1), 2000, 1–12.
- **[SOTA]** S. Petermichl, A. Volberg. *Heating of the Ahlfors–Beurling operator: weakly quasiregular maps on the plane are quasiregular.* Duke Mathematical Journal 112(2), 2002, 281–305.
- **[SOTA]** S. Petermichl. *The sharp bound for the Hilbert transform on weighted Lebesgue spaces in terms of the classical $A_p$ characteristic.* American Journal of Mathematics 129(5), 2007, 1355–1375.
- **[SOTA]** T. P. Hytönen. *The sharp weighted bound for general Calderón–Zygmund operators.* Annals of Mathematics 175(3), 2012, 1473–1506.
- **[SOTA]** V. Vasyunin, A. Volberg. *Sharp constants in the classical weak form of the John–Nirenberg inequality.* Proceedings of the London Mathematical Society 108(6), 2014, 1417–1434.
- **[SOTA]** P. Ivanisvili, D. M. Stolyarov, V. I. Vasyunin, P. B. Zatitskiy. *Bellman function for extremal problems in BMO.* Transactions of the American Mathematical Society 368, 2016, 3415–3468; and *Bellman function for extremal problems in BMO II: evolution*, Memoirs of the American Mathematical Society 255(1220), 2018.
- **[SOTA]** V. Vasyunin. *The sharp constant in the reverse Hölder inequality for Muckenhoupt weights.* Algebra i Analiz 15(1), 2003; St. Petersburg Mathematical Journal 15, 2004, 49–79.
- **[SOTA]** A. D. Melas. *The Bellman functions of dyadic-like maximal operators and related inequalities.* Advances in Mathematics 192(2), 2005, 310–340.
- **[Survey / Book]** V. Vasyunin, A. Volberg. *The Bellman Function Technique in Harmonic Analysis.* Cambridge Studies in Advanced Mathematics 186, Cambridge University Press, 2020.
- **[Survey]** L. Slavin, V. Vasyunin. *Sharp results in the integral-form John–Nirenberg inequality.* Transactions of the American Mathematical Society 363(8), 2011, 4135–4169.
- **[Survey]** A. Osękowski. *Sharp Martingale and Semimartingale Inequalities.* Monografie Matematyczne 72, Birkhäuser, 2012.

## 10. Worked Example / Concrete Special Case

**Why the $A_2$ power is linear, and what a sharp Bellman function must reproduce.**

Take $J=[0,1]$ and the power weight $w(x)=x^{\delta-1}$ with $0<\delta<1$, so $\sigma:=w^{-1}=x^{1-\delta}$.

Averages on $J$:
$$\langle w\rangle_J=\int_0^1 x^{\delta-1}dx=\frac1\delta,\qquad \langle \sigma\rangle_J=\int_0^1 x^{1-\delta}dx=\frac{1}{2-\delta}.$$

On the dyadic interval $I_n=[0,2^{-n}]$:
$$\langle w\rangle_{I_n}=2^{n}\!\int_0^{2^{-n}}\!\!x^{\delta-1}dx=\frac{2^{n(1-\delta)}}{\delta},\qquad \langle \sigma\rangle_{I_n}=\frac{2^{-n(1-\delta)}}{2-\delta},$$
so the product is **scale-invariant**:
$$\langle w\rangle_{I_n}\langle \sigma\rangle_{I_n}=\frac{1}{\delta(2-\delta)}\quad\text{for every }n\ge0 .$$
Dyadic intervals not touching $0$ give a product bounded uniformly in $\delta$. Hence
$$[w]_{A_2^d}=\frac{1}{\delta(2-\delta)}\ \asymp\ \frac{1}{2\delta}\ \xrightarrow[\delta\to0]{}\ \infty .$$

**Where the growth comes from.** Along the chain $I_0\supset I_1\supset\cdots$ the Bellman point $(u_n,v_n)=(\langle w\rangle_{I_n},\langle\sigma\rangle_{I_n})$ moves along the hyperbola $uv=Q$, $Q=[w]_{A_2}$, with $\log u_{n}$ increasing by $(1-\delta)\log 2$ per step. Testing $T_\varepsilon$ on $f=\sigma\chi_J$, each of the first $N\asymp\delta^{-1}$ scales contributes comparably to $\|T_\varepsilon f\|_{L^2(w)}$, because $2^{-n\delta}\asymp1$ precisely while $n\lesssim \delta^{-1}$; beyond that the contributions decay geometrically. Summing the $\asymp\delta^{-1}$ comparable scales gives
$$\|T_\varepsilon\|_{L^2(w)\to L^2(w)}\ \gtrsim\ \delta^{-1}\ \asymp\ [w]_{A_2},$$
matching Wittwer's upper bound $C[w]_{A_2}$ (details in Petermichl, *Amer. J. Math.* 2007).

**What is still open in this example.** The scale-counting fixes the *power* at $1$ but not the *constant*: it produces a lower bound $c_0[w]_{A_2}$ with $c_0$ coming from a geometric sum, while the Bellman upper bound gives $C[w]_{A_2}$ with $C$ read off from an *ad hoc* concave majorant on $\Omega_Q$. The two do not meet. Determining the least locally concave majorant on the non-convex region $\{1\le uv\le Q\}$ — i.e. its foliation by extremal segments — would close the gap and is exactly what Section 6 asks for.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*