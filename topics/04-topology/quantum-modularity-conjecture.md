---
id: 04-topology/quantum-modularity-conjecture
title: "Quantum Modularity Conjecture"
topic: 04-topology
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Quantum Modularity Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/quantum-modularity-conjecture` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

The Kashaev invariant $\langle K\rangle_N$ of a knot $K$ is a sequence of complex numbers indexed by $N\in\mathbb{N}$, obtained by evaluating the $N$-coloured Jones polynomial at the primitive root of unity $q=e^{2\pi i/N}$. Because a root of unity is determined by a rational number, the invariant is really a function

$$\mathbf{J}_K:\ \mathbb{Q}/\mathbb{Z}\longrightarrow \mathbb{C},\qquad \mathbf{J}_K(a/c)=\text{(Kashaev invariant at }q=e^{2\pi i a/c}).$$

Zagier's **Quantum Modularity Conjecture (QMC)**, stated in *Quantum modular forms* (2010), asserts that this function — which is nowhere continuous and satisfies no exact transformation law — is nevertheless *asymptotically* modular: for every $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in \mathrm{SL}_2(\mathbb{Z})$ the ratio $\mathbf{J}_K(\gamma x)/\mathbf{J}_K(x)$, taken as $x\to\infty$ through rationals of bounded denominator, has a complete asymptotic expansion of the shape

$$\frac{\mathbf{J}_K(\gamma x)}{\mathbf{J}_K(x)}\ \sim\ \Big(\frac{2\pi}{\hbar}\Big)^{3/2}\frac{1}{\delta_K}\,e^{V(K)/\hbar}\,\Phi_K(\hbar),\qquad \hbar=\frac{2\pi i}{c(cx+d)} .$$

Here $V(K)$ is the complexified volume $\mathrm{Vol}(K)+i\,\mathrm{CS}(K)$ of the hyperbolic structure (suitably normalised so that $\Re(V/\hbar)>0$), $\delta_K$ is an algebraic constant built from the adjoint Reidemeister torsion (the "1-loop invariant"), and $\Phi_K(\hbar)=1+\kappa_1\hbar+\kappa_2\hbar^2+\cdots$ is a formal power series whose coefficients are conjecturally algebraic numbers in the invariant trace field of $S^3\setminus K$, with denominators divisible only by $\delta_K$ and small primes.

A complete resolution requires: (i) proving the existence of the asymptotic expansion to all orders, for all $\gamma$, for every hyperbolic knot; (ii) identifying the exponential factor as the complexified volume; (iii) proving the arithmeticity of the coefficients $\kappa_n$. A disproof would exhibit a hyperbolic knot and a $\gamma$ for which the ratio fails to have this form (for instance an expansion with the wrong power of $\hbar$, or a non-algebraic $\kappa_n$).

The $\gamma=S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $x=N$ case degenerates to $\mathbf J_K(0)=1$ in the denominator and recovers the **Volume Conjecture** of Kashaev and Murakami–Murakami. QMC is therefore a strict, and far more rigid, refinement of it.

## 2. Mathematical Foundations

**Kashaev invariant.** For a hyperbolic knot $K$, $\langle K\rangle_N = J'_N(K;e^{2\pi i/N})$ where $J'_N$ is the $N$-coloured Jones polynomial normalised so that $J'_N(\text{unknot})=1$. For the figure-eight knot $4_1$ there is the closed cyclotomic (Habiro–Le) formula

$$\langle 4_1\rangle_N=\sum_{k=0}^{N-1}\prod_{j=1}^{k}\bigl|1-q^{j}\bigr|^{2},\qquad q=e^{2\pi i/N}.$$

**Quantum modular form (Zagier).** A function $f:\mathbb{Q}\to\mathbb{C}$ is a quantum modular form of weight $k$ for $\Gamma\subseteq \mathrm{SL}_2(\mathbb{Z})$ if for each $\gamma\in\Gamma$ the *cocycle*

$$h_\gamma(x)\;=\;f(x)-(cx+d)^{-k}f(\gamma x)$$

extends from $\mathbb{Q}$ to a function on $\mathbb{R}$ (or $\mathbb{C}\setminus\mathbb{R}$) that is analytically better behaved — real-analytic, smooth, or holomorphic — than $f$ itself. QMC is the statement that $\log \mathbf{J}_K$ is a quantum modular form in a multiplicative, weight-$3/2$, exponentially-twisted sense.

**Cocycle condition.** Writing $\mathcal{J}_K(x)=\mathbf J_K(x)$, the family $\{\Phi_K\}$ must satisfy compatibility under composition $\gamma_1\gamma_2$, which forces $\Phi_K$ to be independent of $\gamma$ and $V(K)$ to be a genuine invariant.

**Complexified volume.** For an ideal triangulation with Neumann–Zagier data, the geometric solution of the gluing equations gives $V(K)=i\sum_{j}\bigl(\mathrm{Li}_2(z_j)+\tfrac12\log z_j\log(1-z_j)\bigr)+\text{const}$, agreeing with $i(\mathrm{Vol}+i\,\mathrm{CS})$ mod $\pi^2$.

**1-loop invariant.** $\delta_K=\pm\tfrac12\det\bigl(A\,\mathbf{Z}''+B\,\mathbf{Z}'^{-1}\bigr)\prod z_j^{-1/2}$ in Neumann–Zagier coordinates; the Dimofte–Garoufalidis conjecture identifies $\delta_K$ with the adjoint Reidemeister torsion of $S^3\setminus K$ at the discrete faithful representation. For $4_1$, $z=e^{i\pi/3}$ and $\delta_{4_1}=\sqrt{-3}$, producing the leading constant $3^{-1/4}$.

**Refined (matrix) form.** Garoufalidis–Zagier upgrade $\mathbf J_K$ to a vector indexed by boundary-parabolic $\mathrm{PSL}_2(\mathbb{C})$ representations $\sigma$, with series $\Phi^{(\sigma)}_K(\hbar)$ and a matrix-valued cocycle $\mathbf{W}_K(x)\in \mathrm{GL}_r(\mathbb{C})$ satisfying $\mathbf{W}_K(\gamma x)=\mathbf{W}_K(x)\,\rho(\gamma)$ asymptotically. The $\Phi^{(\sigma)}$ are Gevrey-1 divergent series whose Borel transforms have singularities at $\mathbb{Z}\cdot(V^{(\sigma)}-V^{(\sigma')})$ — the resurgent structure.

## 3. History & State of the Art (SOTA)

- **1995–1997.** Kashaev defines the invariant from the quantum dilogarithm and observes numerically that $\log|\langle K\rangle_N|/N\to \mathrm{Vol}(K)/2\pi$ for $4_1,5_2,6_1$.
- **2001.** Murakami–Murakami identify $\langle K\rangle_N$ with $|J'_N(K;e^{2\pi i/N})|$ and formulate the Volume Conjecture for all knots via simplicial volume.
- **2001.** Zagier's "strange identity" for $F(q)=\sum_{n\ge0}(q;q)_n$ — the Kontsevich–Zagier series, itself the Kashaev invariant of the trefoil — exhibits the first explicit quantum-modular transformation law, with cocycle given by a period of $\eta(z)$.
- **2010.** Zagier's *Quantum modular forms* names the phenomenon, gives the $4_1$ example in full numerical detail, and states QMC.
- **2016–2018.** Ohtsuki, and Ohtsuki–Yokota, prove all-order asymptotic expansions of $\langle K\rangle_N$ (the $\gamma=S$, integer-$x$ case) for $5_2$ and for all hyperbolic knots with at most seven crossings, by rigorous saddle-point analysis of Kashaev's integral formula.
- **2019–2022.** Bettin–Drappeau prove the full quantum modularity statement for the figure-eight knot for all $\gamma\in\mathrm{SL}_2(\mathbb{Z})$, using Estermann/Lerch-type analysis of the $q$-Pochhammer symbol and continued-fraction expansions.
- **2021–2024.** Garoufalidis–Zagier develop the matrix refinement, tie $\Phi_K$ to state-integral $q$-series $(\widehat{\Phi}, H(x))$, and connect QMC to resurgence and Stokes matrices (Garoufalidis–Gu–Mariño). Wheeler's thesis (2023) extends quantum modularity to a closed hyperbolic 3-manifold.

Numerically, QMC has been verified to dozens of digits and dozens of orders in $\hbar$ for census knots up to $\sim 8$ crossings.

## 4. Partial Results / Verified Cases

- **Figure-eight knot $4_1$:** fully proved. Bettin–Drappeau establish the ratio asymptotic to all orders in $\hbar$ for every $\gamma\in\mathrm{SL}_2(\mathbb{Z})$, with $V=i(\mathrm{Vol}(4_1))=i\cdot 2.029883\ldots$, $\delta=\sqrt{-3}$, and $\kappa_n\in\mathbb{Q}(\sqrt{-3})$.
- **$\gamma=S$, $x=N\in\mathbb{Z}$ (i.e. the asymptotic expansion of $\langle K\rangle_N$):** proved for $4_1$ (Andersen–Hansen, Ohtsuki), $5_2$ (Ohtsuki 2016), and all hyperbolic knots with $\le 7$ crossings (Ohtsuki–Yokota 2018).
- **Torus knots and the trefoil:** the Kontsevich–Zagier series $F(q)$ satisfies an exact quantum-modular law (Zagier 2001); torus knots are non-hyperbolic, so $V=0$ and the statement degenerates to genuine weight-$3/2$ quantum modularity.
- **Surgeries on $4_1$:** asymptotic expansions of Witten–Reshetikhin–Turaev invariants proved by Andersen–Hansen (2006); Ohtsuki (2018) and Wheeler (2023) extend to closed hyperbolic examples such as $-1$-surgery.
- **Arithmeticity:** for $4_1$ and $5_2$ the first $\sim 100$ coefficients $\kappa_n$ have been computed and verified to lie in the trace field with the predicted denominators.
- **State-integral models:** for all knots with an ideal triangulation of $\le 8$ tetrahedra, the Andersen–Kashaev state integral is known to have the conjectured factorisation into $q$- and $\tilde q$-series, which implies QMC-type behaviour for the associated $\widehat{\Phi}$.

## 5. Principal Obstacles

- **No integral representation in general.** Ohtsuki's method needs an explicit finite-dimensional integral (Kashaev's quantum-dilogarithm formula) whose saddle point can be located and shown to dominate. Producing such a representation with controlled analytic continuation for an arbitrary knot diagram is unsolved; the number of integration variables grows with the number of tetrahedra and the potential function becomes a many-variable Rogers dilogarithm with uncontrolled critical-point structure.
- **Positivity/uniformity of the saddle.** Even when the integral exists, one must show the geometric critical point is the unique dominant one and bound the tail uniformly in the denominator $c$. Current bounds degrade as $c$ grows, which is exactly the regime QMC requires ($x\to\infty$ with $c$ fixed but arbitrary).
- **Divergence.** $\Phi_K(\hbar)$ has zero radius of convergence ($\kappa_n$ grows factorially), so no naive resummation defines the right-hand side; one needs Borel–Écalle resummation with Stokes data that is itself conjectural.
- **Nowhere-continuity.** $\mathbf J_K$ is defined only on $\mathbb{Q}$ and jumps wildly; classical modular machinery (Poisson summation, Rankin–Selberg, spectral theory, holomorphic Fourier expansions) needs a function on the upper half-plane and simply does not apply.
- **Number-theoretic input.** Bettin–Drappeau's proof for $4_1$ leans on the Estermann zeta function and on equidistribution of continued-fraction partial quotients — tools tailored to the single $q$-Pochhammer product $\prod|1-q^j|^2$. No analogue exists for the multi-sum cyclotomic expansions of general knots.
- **Trace fields.** For $4_1$ the trace field is quadratic imaginary; for a general knot it is a number field of arbitrary degree, and the algebraicity of $\kappa_n$ has no known mechanism beyond numerical fitting.

## 6. The Gap

Proved: an all-orders, all-$\gamma$ statement for one knot ($4_1$), and the $\gamma=S$ specialisation for a finite list of at most seven crossings. Conjectured: all hyperbolic knots, all $\gamma$, plus arithmeticity of $\Phi_K$.

The precise barrier is the passage from *one* asymptotic direction (integer $N\to\infty$) to *all* rational directions with denominators $c>1$. Ohtsuki's saddle-point analysis is intrinsically a $c=1$ argument: for $c>1$ the invariant at $q=e^{2\pi i a/c}$ involves a different, smaller root of unity, and the Kashaev sum splits into $c$ interleaved subsums whose relative phases are governed by Gauss-sum data not present in the $c=1$ case. Bridging that gap for $4_1$ required Bettin–Drappeau's number-theoretic machinery; the missing step is a *geometric* mechanism — presumably a cocycle for the Chern–Simons line bundle over $\mathrm{SL}_2(\mathbb{Z})$-orbits, or a rigorous resurgent-Stokes structure — that produces the $c>1$ behaviour from the triangulation directly.

## 7. Current Research (as of June 2026)

- **Garoufalidis–Zagier programme (MPIM Bonn, SUSTech).** Matrix-valued quantum modularity: a $r\times r$ matrix $\mathbf{W}_K(x)$ of $q$-series and $\tilde q$-series whose cocycle property under $\mathrm{SL}_2(\mathbb{Z})$ encodes QMC for all Galois-conjugate geometric structures at once. Numerically confirmed for $4_1$, $5_2$, $(-2,3,7)$-pretzel.
- **Resurgence and Stokes matrices.** Gu–Mariño and collaborators (Geneva) compute Borel-plane singularities and Stokes constants of $\Phi_K^{(\sigma)}$ and argue they are integers counting BPS states; the Stokes matrix conjecturally *equals* the quantum-modularity cocycle. *(frontier — verify)*
- **Analytic number theory route.** Bettin–Drappeau and successors extend $q$-Pochhammer modularity to more general Nahm-type sums; extension to $5_2$ is reported in preprint form. *(frontier — verify)*
- **Closed 3-manifolds.** Wheeler, Ohtsuki: quantum modularity for WRT invariants of closed hyperbolic manifolds obtained by Dehn filling.
- **$\hat{Z}$ invariants.** Gukov–Manolescu–Park's $q$-series homological blocks give candidate holomorphic functions on $|q|<1$ whose radial limits are Kashaev invariants; making that limit rigorous would give QMC a genuine modular-forms proof. *(frontier — verify)*

## 8. Future Work

- Prove the $\gamma=S$ expansion for *all* hyperbolic knots by making the Andersen–Kashaev state integral a rigorous, uniformly convergent object — this is the most concrete open target.
- Establish the Dimofte–Garoufalidis 1-loop conjecture ($\delta_K$ = adjoint torsion), which would pin the constant term in QMC intrinsically rather than by fitting.
- Prove Borel summability of $\Phi_K$ and identify the Stokes automorphism, converting the asymptotic statement into an exact one.
- Realise $\mathbf J_K$ as the radial limit of a holomorphic function (via $\hat Z$ or false/partial theta series), so classical modular transformation theory becomes available.
- Extend to links, to non-hyperbolic knots (where $V=0$ and polynomial growth is expected), and to arbitrary Dehn fillings.

## 9. Key References

- **[Foundational]** R. M. Kashaev. *The hyperbolic volume of knots from quantum dilogarithm.* Letters in Mathematical Physics 39 (1997), 269–275.
- **[Foundational]** H. Murakami, J. Murakami. *The colored Jones polynomials and the simplicial volume of a knot.* Acta Mathematica 186 (2001), 85–104.
- **[Foundational]** D. Zagier. *Vassiliev invariants and a strange identity related to the Dedekind eta-function.* Topology 40 (2001), 945–960.
- **[Foundational]** D. Zagier. *Quantum modular forms.* In *Quanta of Maths*, Clay Mathematics Proceedings 11, AMS (2010), 659–675.
- **[SOTA / Recent]** T. Ohtsuki. *On the asymptotic expansion of the Kashaev invariant of the $5_2$ knot.* Quantum Topology 7 (2016), 669–735.
- **[SOTA / Recent]** T. Ohtsuki, Y. Yokota. *On the asymptotic expansions of the Kashaev invariant of hyperbolic knots with seven crossings.* Mathematical Proceedings of the Cambridge Philosophical Society 165 (2018), 287–339.
- **[SOTA / Recent]** S. Bettin, S. Drappeau. *Modularity of the $q$-Pochhammer symbol and application.* (2020); and *Limit laws for rational continued fractions and value distribution of quantum modular forms.* Proceedings of the London Mathematical Society 125 (2022), 1377–1425.
- **[SOTA / Recent]** S. Garoufalidis, D. Zagier. *Knots, perturbative series and quantum modularity.* SIGMA 20 (2024), paper 055.
- **[SOTA / Recent]** S. Garoufalidis, D. Zagier. *Knots and their related $q$-series.* SIGMA 19 (2023), paper 082.
- **[SOTA / Recent]** S. Garoufalidis, J. Gu, M. Mariño. *The resurgent structure of quantum knot invariants.* Communications in Mathematical Physics 386 (2021), 469–493.
- **[Survey]** J. E. Andersen, S. K. Hansen. *Asymptotics of the quantum invariants for surgeries on the figure 8 knot.* Journal of Knot Theory and Its Ramifications 15 (2006), 479–548.
- **[Survey]** H. Murakami. *An introduction to the volume conjecture.* In *Interactions between Hyperbolic Geometry, Quantum Topology and Number Theory*, Contemporary Mathematics 541, AMS (2011), 1–40.

## 10. Worked Example / Concrete Special Case

Take $K=4_1$ and the simplest case $\gamma=S$, $x=N$, where $\gamma x = -1/N$ has denominator $N$ and $\mathbf J_{4_1}(N)=\mathbf J_{4_1}(0)=1$. QMC then reduces to an asymptotic expansion of the Kashaev invariant itself.

**Exact small values.** With $q=e^{2\pi i/N}$ and $|1-q^{j}|^{2}=4\sin^{2}(\pi j/N)$:

- $N=2$: $q=-1$, terms $1,\,4$. $\langle4_1\rangle_2=5$.
- $N=3$: $4\sin^2(\pi/3)=3$, terms $1,\,3,\,9$. $\langle4_1\rangle_3=13$.
- $N=4$: factors $2,4,2$, terms $1,\,2,\,8,\,16$. $\langle4_1\rangle_4=27$.
- $N=5$: factors $4\sin^2 36^\circ=1.381966$, $4\sin^2 72^\circ=3.618034$, then $3.618034$, $1.381966$; terms $1,\;1.381966,\;5,\;18.090170,\;25$. $\langle4_1\rangle_5=50.472136$.

**Predicted asymptotic.** With $\hbar=2\pi i/N$, $V=i\,\mathrm{Vol}(4_1)$, $\mathrm{Vol}(4_1)=2.029883212819\ldots$ (twice the ideal regular tetrahedron volume $1.014941\ldots$), $\delta=\sqrt{-3}$, QMC predicts

$$\langle 4_1\rangle_N\ \sim\ \frac{N^{3/2}}{3^{1/4}}\;e^{N\,\mathrm{Vol}(4_1)/2\pi}\;\Bigl(1+\kappa_1\tfrac{2\pi i}{N}+\kappa_2\bigl(\tfrac{2\pi i}{N}\bigr)^2+\cdots\Bigr).$$

**Check at $N=5$.** $N^{3/2}=11.18034$, $3^{-1/4}=0.759836$, $e^{5\cdot 2.0298832/2\pi}=e^{1.615367}=5.02988$. Product $=42.727$. The exact value is $50.472$, a ratio of $1.181$ — consistent with a correction $1+O(1/N)$ already at $N=5$; the ratio tends to $1$ like $1+c/N$ as $N$ grows, and Ohtsuki's theorem confirms the full expansion exists.

**Where the difficulty enters.** Now take instead $\gamma=S$ but $x=N+\tfrac12$, so $\gamma x=-2/(2N+1)$ has denominator $2N+1$ while $x$ has denominator $2$. Both $\mathbf J_{4_1}(x)$ and $\mathbf J_{4_1}(\gamma x)$ are non-trivial, and the same constants $V$, $\delta$, $\Phi$ must govern the *ratio*. Verifying this numerically is straightforward; proving it required Bettin–Drappeau's analysis of $\log(q;q)_\infty$ along $c=2$ rays. For any knot other than $4_1$ the analogous $c\ge 2$ statement is open, and that single step is the content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*