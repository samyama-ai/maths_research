---
id: 04-topology/gukov-peacock-putrov-conjecture
title: "Gukov-Peacock-Putrov Conjecture"
topic: 04-topology
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gukov-Peacock-Putrov Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/gukov-peacock-putrov-conjecture` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

The conjecture — catalogued here under the Gukov–Peacock–Putrov name, and standard in the literature as the **Gukov–Pei–Putrov–Vafa (GPPV) conjecture** on *homological blocks* $\hat{Z}$ — asserts that the Witten–Reshetikhin–Turaev (WRT) invariant of a closed oriented 3-manifold, a complex number defined only at roots of unity, is the boundary value of a family of $q$-series with **integer** coefficients that converge inside the unit disc.

Precisely. Let $M$ be a closed oriented rational homology 3-sphere (so $|H_1(M;\mathbb{Z})| < \infty$), and let $\mathrm{Spin}^c(M)$ be its set of $\mathrm{spin}^c$ structures, a torsor over $H_1(M;\mathbb{Z})$. The conjecture claims:

1. **(Existence and integrality.)** For each $b \in \mathrm{Spin}^c(M)/\mathbb{Z}_2$ there is a series
$$\hat{Z}_b(q) \in 2^{-c}q^{\Delta_b}\,\mathbb{Z}[[q]], \qquad \Delta_b \in \mathbb{Q},\; c \in \mathbb{Z}_{\ge 0},$$
convergent for $|q|<1$, that is a topological invariant of the pair $(M,b)$ up to an overall sign and power of $q$.
2. **(Radial limit / WRT recovery.)** The $\hat{Z}_b$ resum the WRT invariant at $q \to \zeta_k = e^{2\pi i/k}$:
$$Z^{SU(2)}_{k}[M] \;=\; \frac{(i)^{\,\sigma}}{2\sqrt{-k}} \sum_{a,b} e^{2\pi i k \,\ell k(a,a)}\, S_{ab}\, \hat{Z}_b(q)\Big|_{q\to \zeta_k},$$
where $\ell k$ is the linking form on $H_1(M)$, $S_{ab}$ is an explicit unitary matrix built from that linking form, and the limit is radial ($q \to \zeta_k$ from inside the disc).
3. **(Categorification.)** The integers appearing in $\hat{Z}_b(q) = \sum_n a_n q^n$ are graded Euler characteristics of a bigraded homology $\mathcal{H}_b^{i,j}$, so that $\hat{Z}_b(q)=\sum_{i,j}(-1)^i q^j \dim \mathcal{H}^{i,j}_b$.

A complete proof requires (1) a construction of $\hat{Z}_b$ for *all* rational homology spheres with proof of topological invariance, and (2) the radial-limit identity in full generality. A disproof would exhibit a manifold whose WRT invariants admit no such integral resummation.

## 2. Mathematical Foundations

**Plumbed 3-manifolds.** Let $\Gamma$ be a tree with $L$ vertices weighted by $m_v \in \mathbb{Z}$, and $M(\Gamma)$ the boundary of the associated 4-dimensional plumbing $X(\Gamma)$. The linking matrix is
$$M_{uv} = \begin{cases} m_v & u=v,\\ 1 & u\!-\!v \text{ an edge},\\ 0 & \text{else}.\end{cases}$$
Assume $M$ is **negative definite**; then $M(\Gamma)$ is a rational homology sphere with $H_1 = \mathbb{Z}^L/M\mathbb{Z}^L$, and $\mathrm{Spin}^c(M(\Gamma)) \cong (2\mathbb{Z}^L + \delta)/2M\mathbb{Z}^L$ with $\delta_v = \deg(v) \bmod 2$.

**The GPPV integral formula.** For $b \in (2\mathbb{Z}^L+\delta)/2M\mathbb{Z}^L$,
$$\hat{Z}_b(q) \;=\; (-1)^{\pi}\, q^{\frac{3\sigma - \sum_v m_v}{4}} \; \mathrm{v.p.}\!\oint_{|z_v|=1} \prod_{v\in V} \frac{dz_v}{2\pi i z_v}\left(z_v - z_v^{-1}\right)^{2-\deg(v)} \Theta^{-M}_b(z;q),$$
$$\Theta^{-M}_b(z;q) \;=\; \sum_{\ell \in 2M\mathbb{Z}^L + b} q^{-\frac{(\ell, M^{-1}\ell)}{4}} \prod_{v} z_v^{\ell_v},$$
where $\sigma$ is the signature of $M$, $\pi$ the number of positive eigenvalues, and $\mathrm{v.p.}$ the principal value (expand $(z-z^{-1})^{-1}$ symmetrically in $z$ and $z^{-1}$). Negative definiteness makes $-\frac14(\ell,M^{-1}\ell)$ bounded below, so the result lies in $q^{\Delta_b}\mathbb{Z}[[q]]$.

**Invariance.** Two weighted trees give homeomorphic plumbed manifolds iff related by **Neumann moves** (blow-up/down and 3-manifold-preserving splitting). $\hat{Z}_b$ must be shown invariant under these, up to $\pm q^{\Delta}$.

**Analytic type.** For Seifert manifolds $\hat{Z}_b$ is a **false theta function**
$$\tilde{\Psi}^{(a)}_p(q) = \sum_{n\ge 0}\psi^{(a)}_{2p}(n)\,q^{n^2/4p},$$
with $\psi^{(a)}_{2p}$ an odd periodic function mod $2p$. False thetas are not modular but **quantum modular** in Zagier's sense: $\tilde\Psi(q)-(\text{period-like transform})$ extends smoothly across $\mathbb{Q}$, which is exactly what produces the finite radial limits in (2).

**Physical origin.** $\hat{Z}_b$ counts BPS states of the 3d $\mathcal{N}=2$ theory $T[M]$ obtained by compactifying the 6d $(2,0)$ theory on $M$; the sum over $b$ with the $S$-matrix is the Chern–Simons path integral written as a sum over Lefschetz thimbles / flat connections (resurgence).

## 3. History & State of the Art (SOTA)

- **1989–91.** Witten's Chern–Simons path integral; Reshetikhin–Turaev's rigorous $\zeta_k$-valued invariant. No natural $q$-series interpolation known.
- **1995–2002.** Ohtsuki's perturbative expansion for rational homology spheres; Lawrence–Zagier (1999) show the WRT invariants of the Poincaré sphere $\Sigma(2,3,5)$ are radial limits of an explicit false theta function — the prototype of the whole conjecture.
- **2016.** Gukov–Putrov–Vafa, *Fivebranes and 3-manifold homology*, introduce $\hat{Z}_b$ as BPS partition functions and conjecture the categorification.
- **2017.** Gukov–Pei–Putrov–Vafa give the plumbing integral formula above and check Neumann invariance and the radial limit on many examples. Gukov–Mariño–Putrov relate the decomposition to resurgence and Borel resummation of the perturbative Chern–Simons series.
- **2019–2021.** Gukov–Manolescu extend $\hat{Z}$ to knot complements as a two-variable series $F_K(x,q)$, conjecturally satisfying a surgery formula recovering $\hat{Z}$ of Dehn fillings; Park constructs $F_K$ for positive braid knots and for higher rank. Cheng–Chun–Ferrari–Gukov–Harrison develop "3d modularity", tying $\hat{Z}$ to vector-valued quantum modular forms.
- **2021–2024.** Costantino–Gukov–Putrov identify $\hat Z$-type invariants with non-semisimple (unrolled quantum $\mathfrak{sl}_2$) TQFT for plumbed manifolds. Yuya Murakami gives a proof of the GPPV radial-limit statement for Seifert fibered spaces.

Status: verified in large, structurally coherent families; no general construction beyond (weakly) negative definite plumbings.

## 4. Partial Results / Verified Cases

- **Negative definite plumbed rational homology spheres.** $\hat{Z}_b$ is *defined* and *proved* invariant under Neumann moves (GPPV 2017). This includes all Seifert fibered rational homology spheres with negative orbifold Euler number, and all surgeries on trees of unknots with sufficiently negative framings.
- **Brieskorn spheres $\Sigma(p_1,p_2,p_3)$.** Single block $\hat{Z}_0$ equal to an explicit false theta $\tilde\Psi^{(a)}_{p_1p_2p_3}$; radial limits match WRT. Verified in closed form for $\Sigma(2,3,5)$, $\Sigma(2,3,7)$, $\Sigma(2,5,7)$, $\Sigma(2,3,11)$, and generally for pairwise coprime $p_i$.
- **Lens spaces $L(p,q)$.** $\hat{Z}_b$ is a finite $q$-monomial sum; the identity (2) reduces to a Gauss-sum reciprocity and is a theorem.
- **Seifert fibered homology spheres with $n \ge 3$ exceptional fibers.** Andersen–Mistegård (2022) prove the resurgence/asymptotic form of the decomposition; Y. Murakami (2023–24) proves the GPPV radial-limit identity in this class *(frontier — verify scope of rational vs. integral homology spheres)*.
- **Knot complements.** $F_K$ constructed and surgery formula verified for the trefoil, figure-eight, all positive braid closures, and torus knots $T(2,2k+1)$ (Gukov–Manolescu; Park).
- **Categorification (item 3).** Established only in isolated cases; no general homology theory $\mathcal{H}^{i,j}$ exists.

## 5. Principal Obstacles

- **No definition outside negative definite plumbings.** The integral formula requires $-M^{-1}$ positive definite to bound $q$-exponents below. For hyperbolic manifolds or non-plumbed graph manifolds there is no candidate series at all — the theta sum is not summable, and analytic continuation produces divergent or non-integral expansions.
- **Convergence vs. modularity.** False theta functions have a **natural boundary** on $|q|=1$: they do not transform under $SL_2(\mathbb{Z})$, only quantum-modularly. Standard modular machinery (Rademacher expansions, circle method) does not apply; one must control asymptotics through Zagier-type "strange identities" case by case.
- **Radial limits are conditionally convergent.** The limit $q\to\zeta_k$ exists only after delicate cancellation; there is no uniform Tauberian theorem giving it from integrality alone. Each proof so far is an explicit Euler–Maclaurin / L-function computation tied to the Seifert structure.
- **Resurgence is not yet a theorem.** The physical derivation treats $\hat Z_b$ as Borel resummations of perturbative series around flat connections. For hyperbolic $M$ the flat connections are irrational and the Stokes data is unknown, so the labelling by $\mathrm{Spin}^c$ structures breaks down (there are more Borel singularities than $\mathrm{spin}^c$ structures).
- **Categorification has no target category.** No construction of $\mathcal{H}^{i,j}$ with the right Euler characteristic exists in general; instanton/monopole Floer theories give the wrong gradings.

## 6. The Gap

Proven: the invariant exists, is integral, and satisfies the WRT radial-limit identity for **negative definite plumbed** (essentially graph) 3-manifolds, with the sharpest results for Seifert fibrations. Conjectured: the same for **all** rational homology spheres, and beyond ($b_1>0$).

The exact barrier is a *definition*, not an estimate. One needs a construction of $\hat{Z}_b(q)$ that (i) reduces to the plumbing integral when $M$ is a negative definite plumbing, and (ii) makes sense when no such presentation exists. The two live candidates are the Gukov–Manolescu surgery formula
$$\hat{Z}(M_{-p}(K)) \;\doteq\; \mathcal{L}^{(p)}_{b}\big[(x^{1/2}-x^{-1/2})\,F_K(x,q)\big],$$
which would reduce every $\mathbb{Z}$HS$^3$ to a knot-complement statement — but requires proving $F_K$ exists for *all* knots and that the Laplace-type transform $\mathcal{L}^{(p)}$ converges — and non-semisimple TQFT, which produces invariants at roots of unity but not yet a $q$-series in the disc.

## 7. Current Research (as of June 2026)

- **Caltech / Gukov's group and collaborators:** higher-rank $\hat{Z}$ for $\mathfrak{sl}_N$ and $\mathfrak{gl}(1|1)$, and $\hat Z$ for non-$\mathbb{Q}$HS via $b_1>0$ regularization.
- **Quantum modularity school (Cologne — Bringmann; Vienna; Milas):** false/partial theta asymptotics, higher-depth quantum modular forms and the depth–plumbing-genus dictionary.
- **Non-semisimple TQFT (Grenoble/Trieste — Costantino, Gukov, Putrov; Blanchet–Costantino–Geer–Patureau-Mirand school):** identification of $\hat Z$ with $\mathcal{N}=2$-type CGP invariants and extension past negative definiteness *(frontier — verify)*.
- **Number-theoretic proofs (Tohoku/Tokyo — Y. Murakami; Fuji–Iwaki–Terashima):** extending the Seifert-case proof to general negative definite plumbings via $L$-function regularization.
- **$F_K$ program (Park, Ekholm–Gruen–Gukov–Kucharski–Ramadevi–Sulkowski):** $F_K$ from HOMFLY/skein and from Ekholm–Ng-type augmentation varieties; the hyperbolic case (figure-eight $F_K$ beyond formal series) remains partly conjectural *(frontier — verify)*.

## 8. Future Work

- Prove existence of $F_K(x,q)$ for all knots (a skein-theoretic or large-color $R$-matrix construction), then derive $\hat Z$ for all $\pm1/n$-surgeries.
- Prove the surgery formula as an identity of convergent series, not just formal ones.
- Find a categorification: a $\mathrm{spin}^c$-graded homology whose Poincaré series is $\hat Z_b$ — plausibly via Khovanov-type homology of the plumbing link or via sheaves on the character variety.
- Establish resurgence rigorously: show the Borel transform of the Chern–Simons perturbative series at a flat connection resums to $\hat Z_b$ for a hyperbolic example.
- Systematically test the conjecture on hyperbolic $\mathbb{Z}$HS$^3$s (e.g. $\pm1$-surgeries on the figure-eight) where no plumbing exists.

## 9. Key References

- **[Foundational]** S. Gukov, P. Putrov, C. Vafa. *Fivebranes and 3-manifold homology.* Journal of High Energy Physics 2017(7):071, 2017. [DOI](https://doi.org/10.1007/jhep07(2017)071)
- **[Foundational]** S. Gukov, D. Pei, P. Putrov, C. Vafa. *BPS spectra and 3-manifold invariants.* Journal of Knot Theory and Its Ramifications 29(2):2040003, 2020 (arXiv:1701.06567). [DOI](https://doi.org/10.1142/s0218216520400039)
- **[Foundational]** R. Lawrence, D. Zagier. *Modular forms and quantum invariants of 3-manifolds.* Asian Journal of Mathematics 3(1):93–107, 1999. [DOI](https://doi.org/10.4310/ajm.1999.v3.n1.a5)
- **[Foundational]** S. Gukov, M. Mariño, P. Putrov. *Resurgence in complex Chern–Simons theory.* arXiv:1605.07615, 2016.
- **[SOTA / Recent]** S. Gukov, C. Manolescu. *A two-variable series for knot complements.* Quantum Topology 12(1):1–109, 2021. [DOI](https://doi.org/10.4171/qt/145)
- **[SOTA / Recent]** J. E. Andersen, W. E. Mistegård. *Resurgence analysis of quantum invariants of Seifert fibered homology spheres.* Journal of the London Mathematical Society 105(2):709–764, 2022. [DOI](https://doi.org/10.1112/jlms.12506)
- **[SOTA / Recent]** Y. Murakami. *A proof of a conjecture of Gukov–Pei–Putrov–Vafa.* arXiv:2302.13526, 2023. [DOI](https://doi.org/10.1007/s00220-024-05136-x)
- **[SOTA / Recent]** F. Costantino, S. Gukov, P. Putrov. *Non-semisimple TQFT's and BPS $q$-series.* SIGMA 19:010, 2023. [DOI](https://doi.org/10.3842/sigma.2023.010)
- **[SOTA / Recent]** S. Park. *Higher rank $\hat{Z}$ and $F_K$.* SIGMA 16:044, 2020.
- **[Survey]** M. C. N. Cheng, S. Chun, F. Ferrari, S. Gukov, S. M. Harrison. *3d Modularity.* Journal of High Energy Physics 2019(10):010, 2019.
- **[Survey]** K. Bringmann, K. Mahlburg, A. Milas. *Quantum modular forms and plumbing graphs of 3-manifolds.* Journal of Combinatorial Theory Series A 170:105145, 2020. [DOI](https://doi.org/10.1016/j.jcta.2019.105145)
- **[Background]** T. Ohtsuki. *Quantum Invariants: A Study of Knots, 3-Manifolds, and Their Sets.* World Scientific, 2002.

## 10. Worked Example / Concrete Special Case

**The Poincaré sphere $M=\Sigma(2,3,5)$**, i.e. $-1$-surgery on the left trefoil, presented as the $-E_8$ plumbing: the $E_8$ tree with every weight $m_v=-2$. Then $M$ is negative definite, $\det M = 1$, so $H_1(M)=0$ and there is a **single** $\mathrm{spin}^c$ structure, $b=b_0$. Signature $\sigma = -8$, $\sum_v m_v = -16$, so the prefactor is $q^{(3(-8)-(-16))/4}=q^{-2}$.

Evaluating the contour integral, the $\deg(v)\le 3$ vertices contribute the expansion of $(z-z^{-1})^{2-\deg v}$ and the theta sum collapses (Lawrence–Zagier) to the false theta function at $p=p_1p_2p_3=30$:
$$\hat{Z}_0(q) \;=\; q^{-3/2}\sum_{n\ge 1}\chi_{60}(n)\,q^{\frac{n^2-1}{120}} \;=\; q^{-3/2}\Big(1-q-q^{3}-q^{7}+q^{8}+q^{14}+q^{20}-q^{29}-\cdots\Big),$$
where $\chi_{60}$ is the odd period-60 function supported on $n\equiv \pm1,\pm11,\pm19,\pm29 \pmod{60}$. The exponents come from $n=1,11,19,29,31,41,49,59$, giving $(n^2-1)/120 = 0,1,3,7,8,14,20,29$ — note the gaps grow like $n^2$, the signature of a false theta with a natural boundary.

**Checks.**
- *Integrality:* every coefficient is $0$ or $\pm 1$; here $c=0$ and $\Delta_0=-3/2$, as conjectured.
- *WRT recovery:* since $|H_1|=1$, the $S$-matrix is the $1\times1$ identity and item (2) reads $Z_k^{SU(2)}[\Sigma(2,3,5)] = \frac{(i)^{-8}}{2\sqrt{-k}}\hat Z_0(q)|_{q\to\zeta_k}$. Lawrence–Zagier prove the radial limit exists at every root of unity and equals the WRT invariant. At $k=1$ the series is Abel-summed by Zagier's strange identity to a finite value; its asymptotic expansion as $q\to1^-$ reproduces exactly Ohtsuki's perturbative series, whose coefficients are the Casson-invariant-normalized LMO terms.
- *Categorification (item 3):* the coefficients $1,-1,-1,-1,1,\dots$ are the graded Euler characteristics of a conjectural $\mathcal{H}^{i,j}$; here each nonzero coefficient is $\pm1$, so each degree would carry a one-dimensional space — consistent, but no construction of $\mathcal{H}$ is known even in this simplest case.

Replacing $-E_8$ by a **positive** definite plumbing (e.g. all $m_v=+2$) flips the sign of $(\ell,M^{-1}\ell)$, the exponents are unbounded below, and the series does not exist — the concrete face of the obstacle in Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*