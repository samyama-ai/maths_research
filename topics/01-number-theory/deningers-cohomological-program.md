---
id: 01-number-theory/deningers-cohomological-program
title: "Deninger's Program for Zeta Functions"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Deninger's Program for Zeta Functions

> **Topic:** Number Theory · **ID:** `01-number-theory/deningers-cohomological-program` · **Status:** open

## 1. Problem Statement / Conjecture

Deninger's program asks for an **infinite-dimensional cohomology theory for arithmetic schemes**, equipped with a canonical endomorphism $\Theta$, whose regularized characteristic polynomials reproduce completed zeta and $L$-functions, and for a **dynamical realization** of that theory on a foliated space.

Precise form. For a regular scheme $X$ proper and flat over $\operatorname{Spec}\mathbb{Z}$ of absolute dimension $d$, let $\hat\zeta_X(s)$ be the Hasse–Weil zeta function completed at the archimedean places. Conjecturally there exist real (or complex) vector spaces $H^i_{\mathcal{D}}(\bar X)$, $0 \le i \le 2d$, carrying a continuous $\mathbb{R}$-action $\phi^{t*}$ with infinitesimal generator $\Theta$, such that

$$\hat\zeta_X(s) \;=\; \prod_{i=0}^{2d} {\det}_\infty\!\left(\frac{1}{2\pi}\bigl(s\cdot\mathrm{id}-\Theta\bigr)\ \Big|\ H^i_{\mathcal{D}}(\bar X)\right)^{(-1)^{i+1}},$$

where $\det_\infty$ is the zeta-regularized determinant. A complete solution must (i) construct the spaces functorially, (ii) prove the determinant formula, and (iii) supply the extra structure — a self-adjointness or polarization on $H^1$ — forcing $\operatorname{spec}(\Theta \mid H^1) \subset \tfrac12 + i\mathbb{R}$, i.e. the Riemann Hypothesis. A disproof would be a structural no-go theorem showing no space with the required orbit spectrum and trace formula can exist.

The dynamical half: find a **3-dimensional foliated dynamical space** $(\bar X, \mathcal{F}, \phi^t)$ attached to $\overline{\operatorname{Spec}\mathbb{Z}}$ whose closed orbits are the primes, with $\ell(\gamma_p) = \log p$, whose fixed points account for the archimedean place, and whose leafwise cohomology is $H^\bullet_{\mathcal{D}}$.

## 2. Mathematical Foundations

**Regularized determinant.** For an operator $A$ with eigenvalues $\lambda_k$ such that $\zeta_A(z)=\sum_k \lambda_k^{-z}$ converges for $\Re z \gg 0$ and continues meromorphically, regular at $z=0$,

$$ {\det}_\infty(A) \;=\; \exp\bigl(-\zeta_A'(0)\bigr). $$

Regularized determinants are **not multiplicative**: $\det_\infty(cA) \ne c^{\dim}\det_\infty(A)$, and the "multiplicative anomaly" $c^{\zeta_A(0)}$ is exactly what produces the exponential factors $\pi^{-s/2}$, $p^{-s}$ in Euler factors.

**Deninger's local computation (1991–1992).** At an archimedean place, with $H=\bigoplus_{n\ge 0}\mathbb{C}$ and $\Theta$ acting with eigenvalues $-n$,

$$ {\det}_\infty\!\left(\frac{s-\Theta}{2\pi}\ \Big|\ H\right) = \frac{(2\pi)^s}{\Gamma(s)} = \Gamma_{\mathbb{C}}(s)^{-1}, \qquad \Gamma_{\mathbb{C}}(s):=(2\pi)^{-s}\Gamma(s). $$

At a finite place $p$, take $\Theta$ with spectrum $\tfrac{2\pi i}{\log p}\mathbb{Z}$ — the spectrum of the generator of a flow of period $\log p$ acting on functions on a circle of length $\log p$. In Deninger's normalization,

$$ {\det}_\infty\!\left(\frac{s-\Theta}{2\pi}\right) = 1-p^{-s} = \zeta_p(s)^{-1}. $$

So every Euler factor, finite or infinite, is a regularized determinant of $\tfrac{1}{2\pi}(s-\Theta)$ on a space with an $\mathbb{R}$-action: periodic orbit ↦ finite factor, fixed point ↦ $\Gamma$-factor.

**Foliated Lefschetz formula.** For a flow $\phi^t$ on a compact foliated space $(\bar X,\mathcal{F})$ transverse to the leaves, with leafwise cohomology $H^\bullet_{\mathcal{F}}$, the expected trace formula (distributions on $t>0$) is

$$ \sum_{i}(-1)^i \operatorname{Tr}\bigl(\phi^{t*}\mid H^i_{\mathcal{F}}\bigr) \;=\; \sum_{\gamma}\ \ell(\gamma)\sum_{k\ge 1}\frac{\varepsilon_\gamma(k)}{\bigl|\det\bigl(1-T_x\phi^{k\ell(\gamma)}\bigr)\bigr|}\ \delta_{k\ell(\gamma)}(t) \;+\;(\text{fixed-point terms}), $$

$T_x\phi$ the transverse derivative. Matching orbits $\gamma_p$ of length $\log p$ against $\sum_{p,k}\frac{\log p}{p^{ks}}$ turns this identically into **Weil's explicit formula**; the fixed-point contribution becomes the archimedean term.

**Positivity.** RH would follow from a Hodge-theoretic input: a polarization on $H^1_{\mathcal{D}}$ for which $\Theta-\tfrac12$ is skew-adjoint — a geometric Hilbert–Pólya statement, mirroring the Weil positivity used in the function-field proof.

## 3. History & State of the Art (SOTA)

- **1949–1974.** Weil conjectures; Grothendieck's $\ell$-adic cohomology; Deligne's proof of RH over $\mathbb{F}_q$. Number fields are excluded because $\overline{\operatorname{Spec}\mathbb{Z}}$ has no base to fiber over.
- **1991–1992.** Deninger computes $\Gamma$-factors and local $L$-factors as regularized determinants (*Invent. Math.* 104 and 107). This is the program's empirical anchor.
- **1998.** Deninger's ICM address, *Some analogies between number theory and dynamical systems on foliated spaces*, states the full conjectural dictionary: primes ↔ closed orbits, $\log N(\mathfrak p)$ ↔ orbit length, Frobenius ↔ flow, ramification ↔ singular leaves.
- **1999.** Connes gives a trace-formula interpretation of the explicit formula on the adele class space (*Selecta Math.*), an operator-theoretic sibling of the program.
- **2005–2009.** Leichtnam's survey; Lichtenbaum's Weil-étale topology (*Ann. of Math.* 170, 2009) provides finite-rank cohomology with an $\mathbb{R}$-action generator $\theta$ and $\cup\theta$-complexes reproducing zeta special values.
- **2016–2018.** Hesselholt realizes zeta functions of $\mathbb{F}_p$-schemes as regularized determinants on periodic topological cyclic homology $TP$; Kucharczyk–Scholze realize absolute Galois groups of certain fields as topological fundamental groups; Flach–Morin prove (conditionally) Weil-étale special-value formulas for proper regular arithmetic schemes (*Doc. Math.* 23).
- **2018–present.** Deninger, *Dynamical systems for arithmetic schemes*, constructs actual dynamical systems whose closed orbits match closed points with the right lengths — at the cost of enormous, non-locally-compact phase spaces.

## 4. Partial Results / Verified Cases

- **All local factors, all places, all motives with known Hodge/Frobenius data.** $\Gamma_{\mathbb{R}},\Gamma_{\mathbb{C}}$ and $\det(1-\mathrm{Frob}_p\,p^{-s}\mid H^i_{\ell})^{-1}$ are regularized determinants of $\tfrac1{2\pi}(s-\Theta)$ (Deninger 1991, 1992). Verified unconditionally.
- **Function fields, $d=1$ and higher.** For $X$ smooth proper over $\mathbb{F}_q$, $\zeta_X(s)$ is a genuine alternating product of characteristic polynomials on $H^i_{\text{ét}}(\bar X,\mathbb{Q}_\ell)$; RH is a theorem (Deligne 1974). Hesselholt (2018) recovers the same for $X/\mathbb{F}_p$ with $\det_\infty$ on the infinite-dimensional graded $\mathbb{R}$-vector spaces $TP_*(X)$ — the closest existing object to $H^\bullet_{\mathcal D}$.
- **Dynamical systems with correct orbit spectrum.** Deninger (2018+) constructs, for any separated scheme of finite type over $\mathbb{Z}$, a continuous $\mathbb{R}$-dynamical system whose closed orbits biject with closed points, lengths $\log N(\mathfrak{p})$, plus $\mathbb{R}$-actions matching Frobenius on $\ell$-adic cohomology. The spaces are not manifolds and not locally compact.
- **Trace formulas for Riemannian foliations.** Álvarez López–Kordyukov established leafwise-heat-flow asymptotics and distributional Betti numbers for Riemannian foliations (*Compositio Math.* 125, 2001), the only setting where a Lefschetz formula of Deninger's shape is proved.
- **Special values.** Flach–Morin (2018) prove Weil-étale descriptions of $\zeta_X^*(n)$ up to standard finiteness conjectures — the "order of vanishing / leading coefficient" half of the dictionary, in ranks that are finite rather than regularized.

## 5. Principal Obstacles

- **No candidate space.** $\overline{\operatorname{Spec}\mathbb{Z}}$ is 1-dimensional; the required object is a 3-dimensional foliated space with a codimension-1 foliation and an $\mathbb{R}$-flow. The spaces that exist (Deninger 2018, Connes–Consani's arithmetic/scaling sites) are either non-locally-compact or topoi lacking the analytic structure needed for $\det_\infty$.
- **The foliation cannot be Riemannian.** Matching $\bigl|\det(1-T_x\phi^{k\log p})\bigr|^{-1}$ to $p^{-k}$-type weights forces the transverse derivative to expand — the flow is hyperbolic transversally. All available Hodge-theoretic and heat-kernel machinery for foliations (Álvarez López–Kordyukov, Connes' index theory) assumes a *bounded* holonomy-invariant transverse metric. Exactly the hypothesis one needs to drop is the one the analysis rests on.
- **Leafwise cohomology is badly behaved.** $H^\bullet_{\mathcal{F}}$ is generally non-Hausdorff and infinite-dimensional in an uncontrolled way; $\Theta$ is unbounded with continuous spectrum unless the foliation is very rigid. Trace-class conditions fail, so $\det_\infty$ is not even defined without an extra spectral hypothesis.
- **Finite-rank theories are the wrong shape.** Weil-étale cohomology delivers finitely generated groups; it recovers special values but *cannot* have $\Theta$-spectrum equal to the infinitely many zeros of $\zeta$. Passing to the infinite-dimensional version requires a limiting construction that no one has defined.
- **No positivity.** Deligne's proof over $\mathbb{F}_q$ uses monodromy and the hard Lefschetz/Weil positivity package. There is no candidate polarization on $H^1_{\mathcal{D}}$, and archimedean fixed points break the compact-orbit symmetry that would make one natural.

## 6. The Gap

Proven: the *local* factorization (every Euler factor is a regularized determinant), and the *global* statement over $\mathbb{F}_q$. Missing: a single cohomology theory whose $\Theta$-spectrum is the set of zeros and poles of $\hat\zeta_X$ globally over $\mathbb{Z}$ — i.e. an object that glues the local $\Theta$'s (which live on unrelated spaces, one per place) into one operator on one space.

The exact barrier is the **archimedean/finite mismatch**: at $p$ the flow has a compact orbit of length $\log p$; at $\infty$ it has a fixed point with $\Gamma$-factor. A single smooth foliated flow with both features, hyperbolic transversally at every closed orbit, is not known to exist on any compact space of dimension 3, and no obstruction theorem rules it out either. Even granting the space, RH needs the second, independent input of Section 2 — the polarization — which is not implied by the determinant formula.

## 7. Current Research (as of June 2026)

- **Münster (Deninger and collaborators).** Continued refinement of *Dynamical systems for arithmetic schemes*, including the higher-dimensional case and attempts to cut the constructed phase spaces down to locally compact models. *(frontier — verify)*
- **Álvarez López–Kordyukov–Leichtnam.** A multi-paper program proving Lefschetz trace formulas for *foliated flows* on compact foliated manifolds with simple foliations, exactly in Deninger's format; extending it past the Riemannian case is the stated goal. *(frontier — verify)*
- **Topological cyclic homology school (Hesselholt, Nikolaus, Bhatt–Morrow–Scholze lineage).** $TP$ and prismatic cohomology as $p$-adic realizations with a Frobenius flow; the open question is an archimedean or global-over-$\mathbb{Z}$ analogue. *(frontier — verify)*
- **Connes–Consani.** Arithmetic site, scaling site, Riemann–Roch statements for $\overline{\operatorname{Spec}\mathbb{Z}}$ over $\mathbb{F}_1$; the characteristic-1 semiring approach as an alternative base.
- **Weil-étale (Morin, Flach, Tran).** Extending special-value theorems to non-proper and singular schemes, and to motivic coefficients.

## 8. Future Work

1. **Construct a locally compact model.** Reduce Deninger's 2018 dynamical systems to a compact foliated space of dimension 3 for $\overline{\operatorname{Spec}\mathbb{Z}}$, or prove no such reduction exists.
2. **Non-Riemannian trace formulas.** Develop leafwise analysis for transversally hyperbolic foliated flows: define distributional Betti numbers when the transverse metric is not holonomy-invariant.
3. **Interpolate $TP$ to the archimedean place.** Find a cohomology theory with $\mathbb{R}$-action specializing to $TP_*(X_{\mathbb{F}_p})$ at $p$ and to Deninger's $\Gamma$-factor space at $\infty$.
4. **Isolate the positivity axiom.** State the minimal polarization hypothesis on $(H^1_{\mathcal D},\Theta)$ implying RH and test it against the function-field model, where both sides are known.
5. **Limit of Weil-étale.** Define a regularized/completed limit of $H^\bullet_W$ whose $\theta$-spectrum is infinite, connecting Section 4's special-value results to the full determinant formula.

## 9. Key References

- **[Foundational]** C. Deninger. *On the $\Gamma$-factors attached to motives.* Inventiones Mathematicae 104 (1991), 245–261.
- **[Foundational]** C. Deninger. *Local $L$-factors of motives and regularized determinants.* Inventiones Mathematicae 107 (1992), 135–150.
- **[Foundational]** C. Deninger. *Some analogies between number theory and dynamical systems on foliated spaces.* Documenta Mathematica, Extra Volume ICM 1998, Vol. I, 163–186.
- **[Survey]** E. Leichtnam. *An invitation to Deninger's work on arithmetic zeta functions.* In *Geometry, Spectral Theory, Groups, and Dynamics*, Contemporary Mathematics 387, AMS, 2005, 201–236.
- **[SOTA / Recent]** C. Deninger. *Dynamical systems for arithmetic schemes.* arXiv preprint, 2018 (revised subsequently).
- **[SOTA / Recent]** L. Hesselholt. *Topological Hochschild homology and the Hasse–Weil zeta function.* In *An Alpine Bouquet of Algebraic Topology*, Contemporary Mathematics 708, AMS, 2018, 157–180.
- **[SOTA / Recent]** M. Flach, B. Morin. *Weil-étale cohomology and zeta-values of proper regular arithmetic schemes.* Documenta Mathematica 23 (2018), 1425–1560.
- **[Foundational]** S. Lichtenbaum. *The Weil-étale topology for number rings.* Annals of Mathematics 170 (2009), 657–683.
- **[Related]** A. Connes. *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function.* Selecta Mathematica (N.S.) 5 (1999), 29–106.
- **[Related]** A. Connes, C. Consani. *Geometry of the arithmetic site.* Advances in Mathematics 291 (2016), 274–329.
- **[Analysis]** J. A. Álvarez López, Y. A. Kordyukov. *Long time behavior of leafwise heat flow for Riemannian foliations.* Compositio Mathematica 125 (2001), 129–153.
- **[Related]** R. Kucharczyk, P. Scholze. *Topological realisations of absolute Galois groups.* In *Cohomology of Arithmetic Groups*, Springer Proceedings in Mathematics & Statistics, 2018.
- **[Classical]** A. Weil. *Sur les "formules explicites" de la théorie des nombres premiers.* Comm. Sém. Math. Univ. Lund (1952), 252–265.

## 10. Worked Example / Concrete Special Case

**Claim.** The $\Gamma$-factor $\Gamma_{\mathbb{C}}(s)=(2\pi)^{-s}\Gamma(s)$ is the inverse regularized determinant of $\tfrac1{2\pi}(s-\Theta)$ on $H=\bigoplus_{n\ge0}\mathbb{C}e_n$ with $\Theta e_n=-n e_n$.

Eigenvalues of $A_s := \tfrac{1}{2\pi}(s-\Theta)$ are $\lambda_n = \frac{s+n}{2\pi}$, $n\ge0$. Its spectral zeta function is

$$ \zeta_{A_s}(z) = \sum_{n\ge0}\left(\frac{s+n}{2\pi}\right)^{-z} = (2\pi)^{z}\,\zeta_H(z,s), \qquad \zeta_H(z,s)=\sum_{n\ge0}(s+n)^{-z}, $$

the Hurwitz zeta function, meromorphic in $z$ with only a pole at $z=1$. Differentiate at $z=0$:

$$ \zeta_{A_s}'(0) = \log(2\pi)\,\zeta_H(0,s) + \zeta_H'(0,s). $$

Two classical values: $\zeta_H(0,s)=\tfrac12-s$, and Lerch's formula $\zeta_H'(0,s)=\log\Gamma(s)-\tfrac12\log 2\pi$. Hence

$$ \zeta_{A_s}'(0) = \left(\tfrac12-s\right)\log 2\pi + \log\Gamma(s) - \tfrac12\log 2\pi = -s\log 2\pi + \log\Gamma(s), $$

$$ {\det}_\infty(A_s) = e^{-\zeta_{A_s}'(0)} = \frac{(2\pi)^{s}}{\Gamma(s)} = \Gamma_{\mathbb{C}}(s)^{-1}. $$

**What the example shows.** The naive product $\prod_{n\ge0}\frac{s+n}{2\pi}$ has no $s$-dependent power of $2\pi$; the factor $(2\pi)^{s}$ arises purely from the anomaly term $\log(2\pi)\zeta_H(0,s)$ with $\zeta_H(0,s)=\tfrac12-s$. The exponential normalizations that decorate completed $L$-functions are therefore *forced* by regularization, not inserted by hand.

**The finite analogue.** Taking $\Theta$ with spectrum $\tfrac{2\pi i}{\log p}\mathbb{Z}$ — the generator of a flow on a single closed orbit of length $\log p$ — the same procedure yields, after pairing $n$ with $-n$,

$$ \prod_{n\in\mathbb{Z}}{}^{\mathrm{reg}}\left(s-\tfrac{2\pi i n}{\log p}\right) \;=\; 2\sinh\!\left(\tfrac{s\log p}{2}\right) = p^{s/2}\left(1-p^{-s}\right), $$

and the $2\pi$-normalization of $\det_\infty$ absorbs the $p^{s/2}$, giving $1-p^{-s}$. So: **one closed orbit of length $\log p$ produces exactly the Euler factor at $p$**. Deninger's program is the demand that these one-orbit and one-fixed-point computations be the local pieces of a single global flow, whose Lefschetz trace formula is the explicit formula and whose $H^1$ spectrum is the critical line.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*