---
id: 04-topology/amu-conjecture
title: "AMU Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# AMU Conjecture (Andersen–Masbaum–Ueno)

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/amu-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\Sigma_{g,n}$ be a compact oriented surface of genus $g$ with $n$ marked points (or boundary components), and let $\mathrm{Mod}(\Sigma_{g,n})$ be its mapping class group. Witten–Reshetikhin–Turaev TQFT supplies, for each odd level $r \ge 5$ and each admissible coloring $c$ of the marked points, a finite-dimensional projective representation

$$\rho_{r,c}\colon \mathrm{Mod}(\Sigma_{g,n}) \longrightarrow \mathrm{PGL}\big(V_r(\Sigma_{g,n},c)\big).$$

**Conjecture (Andersen–Masbaum–Ueno, 2006).** If $\varphi \in \mathrm{Mod}(\Sigma_{g,n})$ is pseudo-Anosov, then there exist $r_0$ and colorings such that for all $r \ge r_0$ (odd) the element $\rho_{r,c}(\varphi)$ has **infinite order**.

The converse direction is elementary: if $\varphi$ is periodic then $\rho_{r,c}(\varphi)$ has finite order, and if $\varphi$ is reducible along a multicurve the quantum representations are known (in the cases analyzed) not to force infinite order. So the conjecture asserts that quantum representations *detect the Nielsen–Thurston type* of a mapping class.

A complete proof must produce, for an arbitrary pseudo-Anosov $\varphi$ on an arbitrary $\Sigma_{g,n}$, a level $r$ and coloring $c$ with $\rho_{r,c}(\varphi)^k \ne \mathrm{id}$ in $\mathrm{PGL}$ for all $k \ge 1$. A disproof requires a single pseudo-Anosov $\varphi$ whose image has finite order at every level and coloring.

## 2. Mathematical Foundations

**TQFT vector spaces.** Fix an odd integer $r \ge 5$, set $p = 2r$, and let $A$ be a primitive $2p$-th root of unity. The $SO(3)$ Blanchet–Habegger–Masbaum–Vogel (BHMV) theory assigns to $(\Sigma,c)$ the skein-theoretic space $V_r(\Sigma,c)$, with dimension given by the Verlinde formula; for a closed genus-$g$ surface,

$$\dim V_r(\Sigma_g) = \left(\frac{r}{4}\right)^{g-1}\sum_{j=1}^{(r-1)/2}\left(\sin \frac{2\pi j}{r}\right)^{2-2g}.$$

**Twist eigenvalues.** In the basis of $V_r$ indexed by admissible colorings of a pants decomposition, a Dehn twist $t_\gamma$ along a curve of the decomposition acts diagonally with eigenvalues

$$\mu_c = (-1)^c A^{c^2+2c}, \qquad 0 \le c \le r-2,$$

so $\rho_{r}(t_\gamma)$ has **finite order** dividing $2p$ in $\mathrm{PGL}$. Every generator of $\mathrm{Mod}(\Sigma)$ therefore has finite image order; infinite order for a product is a global statement.

**Nielsen–Thurston.** Every $\varphi \in \mathrm{Mod}(\Sigma_{g,n})$ is periodic, reducible, or pseudo-Anosov. In the last case there are transverse measured foliations $(\mathcal{F}^s,\mu^s)$, $(\mathcal{F}^u,\mu^u)$ and $\lambda = \lambda(\varphi) > 1$ with $\varphi\cdot(\mathcal F^u,\mu^u)=(\mathcal F^u,\lambda\mu^u)$ and $\varphi\cdot(\mathcal F^s,\mu^s)=(\mathcal F^s,\lambda^{-1}\mu^s)$. By Thurston's hyperbolization, $\varphi$ is pseudo-Anosov (freely isotopic to one) iff the mapping torus $M_\varphi = \Sigma \times [0,1]/(x,1)\sim(\varphi(x),0)$ is hyperbolic.

**Asymptotic faithfulness.** For closed surfaces, $\bigcap_{r} \ker \rho_r$ is trivial modulo the center (Andersen 2006; Freedman–Walker–Wang 2002). This kills *any* fixed nontrivial $\varphi$ at large $r$ but says nothing about the *order* of $\rho_r(\varphi)$, which is exactly the AMU content.

**Link to volume.** Detcherry–Kalfagianni tie AMU to the Chen–Yang volume conjecture: for $M$ with $\partial M \neq \emptyset$ and $r = 2m+1$,

$$\lim_{m\to\infty}\frac{4\pi}{r}\log\big|TV_r(M)\big| = \mathrm{Vol}(M),$$

where $TV_r$ is the Turaev–Viro invariant at $q = A^4 = e^{2\pi i/r}$.

## 3. History & State of the Art (SOTA)

- **1999.** Masbaum exhibits an explicit element of infinite order in a TQFT representation of a mapping class group, showing images are not always finite (Contemp. Math. 233).
- **2002–2006.** Freedman–Walker–Wang and Andersen prove asymptotic faithfulness of the $SU(n)$ quantum representations, establishing that quantum data separates mapping classes in the limit.
- **2006.** Andersen, Masbaum and Ueno state the conjecture and prove it for $\mathrm{Mod}(\Sigma_{0,4})$, the four-punctured sphere, by identifying the projective image of the two-dimensional representation with a triangle-type subgroup of $\mathrm{PSL}_2(\mathbb C)$.
- **2008.** Marché–Narimannejad give a skein-theoretic asymptotic analysis: for $\varphi$ pseudo-Anosov, $\rho_r(\varphi)$-invariant vectors localize on the stable/unstable laminations, a key structural tool.
- **2016–2017.** Egsgaard–Jørgensen and Santharoubane treat further families: hyperelliptic-type classes on punctured spheres and the one-holed torus $\Sigma_{1,1}$.
- **2019–2022.** Detcherry–Kalfagianni convert the Chen–Yang growth of Turaev–Viro invariants into AMU statements, giving the first infinite families in arbitrary genus, then extend by Dehn filling and cabling arguments (with Belletti and Yang).

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $\Sigma_{0,4}$, all punctures colored $1$ | AMU holds for **every** pseudo-Anosov, all $p = 2r \ge 10$ | Andersen–Masbaum–Ueno 2006 |
| $\Sigma_{1,1}$ (one-holed torus) | AMU holds for all pseudo-Anosov classes | Santharoubane 2017 |
| $\Sigma_{0,2n}$, hyperelliptic / kernel-space classes | AMU holds for identified subfamilies via the $q=-1$ homological specialization | Egsgaard–Jørgensen 2016; Santharoubane 2017 |
| Monodromies of fibered links $L \subset S^3$ with hyperbolic complement satisfying the Chen–Yang volume conjecture | AMU holds | Detcherry–Kalfagianni, *Adv. Math.* 351 (2019) |
| Figure-eight knot, Whitehead link, Borromean rings, and their fibered cablings / fundamental shadow link fillings | AMU verified unconditionally (volume conjecture known there) | Detcherry–Kalfagianni 2019; Belletti–Detcherry–Kalfagianni–Yang 2020 |
| Every $g \ge 2$, $n \ge 1$: infinitely many pseudo-Anosov classes on $\Sigma_{g,n}$ | AMU holds | Detcherry–Kalfagianni 2019 |
| Cosets: for suitable fibered $L$, all but finitely many elements of a coset of a subgroup satisfy AMU | AMU holds | Detcherry–Kalfagianni, cosets paper, 2022 |

No closed-surface case ($n = 0$, $g \ge 2$) is settled for all pseudo-Anosovs; the punctured/boundary setting is where all positive results live.

## 5. Principal Obstacles

- **Generators have finite order.** Each $\rho_r(t_\gamma)$ has order dividing $2p$. Any proof must detect a global dynamical invariant ($\lambda > 1$) from a product of finite-order matrices — the same difficulty as certifying that a product of elliptic elements in $\mathrm{PSL}_2$ is loxodromic. There is no local or generator-wise criterion.
- **No trace formula.** For $\dim V_r \ge 3$ there is no usable closed formula for $\mathrm{tr}\,\rho_{r,c}(\varphi)$ as a function of $\varphi$'s word or of $\lambda(\varphi)$. The $\Sigma_{0,4}$ and $\Sigma_{1,1}$ proofs rely on $\dim V = 2$ and the resulting $\mathrm{PSL}_2$ discreteness arguments; these collapse in higher rank.
- **Asymptotic faithfulness is order-blind.** Knowing $\rho_r(\varphi)\ne \mathrm{id}$ for large $r$ is compatible with $\rho_r(\varphi)$ having order $2$ at every level.
- **Number-theoretic finiteness.** Images $\rho_r(\mathrm{Mod}(\Sigma))$ are dense in products of unitary groups (Freedman–Larsen–Wang) but arithmetic subtleties over $\mathbb{Z}[A]$ make it hard to exclude that a given element lands in a finite subgroup for all $r$; the relevant eigenvalue ratios are roots of unity by construction at level $r$, and only their $r$-dependence can distinguish.
- **Volume conjecture dependence.** The strongest general machinery (Detcherry–Kalfagianni) is conditional on the Chen–Yang volume conjecture, itself open beyond special families; asymptotics of $6j$-symbols at $q = e^{2\pi i/r}$ (the "non-standard" root of unity) lack uniform control.

## 6. The Gap

Proven: AMU for two families where the representation is $2$-dimensional and the image is a discrete triangle-type group ($\Sigma_{0,4}$, $\Sigma_{1,1}$); and AMU for pseudo-Anosovs realized as monodromies of fibered links whose complements have exponentially growing $TV_r$. Conjectured: all pseudo-Anosovs on all $\Sigma_{g,n}$.

The precise barrier is a **uniform lower bound on the spectral spread**: one needs, for each pseudo-Anosov $\varphi$, a level $r$ and coloring $c$ such that two eigenvalues $\alpha,\beta$ of $\rho_{r,c}(\varphi)$ satisfy $\alpha/\beta$ is **not a root of unity**. Detcherry–Kalfagianni show that exponential growth
$$\liminf_{r\to\infty}\frac{4\pi}{r}\log\big|TV_r(M_\varphi)\big| > 0$$
implies this, because a finite-order image would force sub-exponential (polynomial) growth of $TV_r(M_\varphi)$ via the trace formula $TV_r(M_\varphi) = \sum_c |\mathrm{tr}\,\rho_{r,c}(\varphi)|^2$-type identities. So AMU sits strictly between "hyperbolic mapping torus" and "exponential Turaev–Viro growth": the missing step is to derive exponential growth of $TV_r$ from hyperbolicity alone.

## 7. Current Research (as of June 2026)

- **Volume-conjecture route.** Extending unconditional Chen–Yang asymptotics from fundamental shadow links to broader classes (Belletti, Detcherry, Kalfagianni, Yang, Ohtsuki). Each new family of hyperbolic fibered complements yields new AMU cases. *(frontier — verify)* Ongoing work on $TV_r$ growth under Dehn filling aims at all sufficiently long fillings of a fixed cusped manifold.
- **Skein-module methods.** Kauffman bracket skein algebras of surfaces at roots of unity, their Azumaya loci and the Bonahon–Wong quantum trace, are being used to produce non-root-of-unity eigenvalue ratios directly from the dynamics of $\varphi$ on the character variety.
- **Homological / arithmetic specializations.** Following Koberda–Santharoubane, quantum representations at small levels are compared with homology of finite covers; images of pseudo-Anosovs in these congruence-type quotients give order lower bounds. *(frontier — verify)*
- **Groups.** Michigan State (Kalfagianni), Institut de Mathématiques de Bourgogne (Detcherry), IMJ-PRG Paris (Marché, Masbaum), Aarhus/QGM lineage (Andersen), and Chinese groups working on Chen–Yang asymptotics.

## 8. Future Work

1. Prove exponential growth of $TV_r(M)$ for **all** hyperbolic $M$ with nonempty boundary; this implies AMU for all pseudo-Anosovs with hyperbolic mapping torus, hence for all of them.
2. Establish a Nielsen–Thurston dichotomy directly inside the skein algebra: show that the action of a pseudo-Anosov on $\mathcal{S}_A(\Sigma)$ has an eigenvalue of modulus governed by $\lambda(\varphi)$ after suitable normalization.
3. Settle the closed-surface case $\Sigma_g$, $g \ge 2$, where marked-point colorings are unavailable and no case is known.
4. Quantify: bound $r_0(\varphi)$ in terms of $\lambda(\varphi)$, word length, or the volume of $M_\varphi$ — a computable $r_0$ would make AMU checkable case by case.
5. Test AMU numerically for random pseudo-Anosovs at moderate genus using explicit BHMV bases and integral TQFT bases, searching for a counterexample.

## 9. Key References

- **[Foundational]** J. E. Andersen, G. Masbaum, K. Ueno. *Topological quantum field theory and the Nielsen–Thurston classification of $M(0,4)$.* Mathematical Proceedings of the Cambridge Philosophical Society, 141 (2006), 477–488. [DOI](https://doi.org/10.1017/s0305004106009698)
- **[Foundational]** C. Blanchet, N. Habegger, G. Masbaum, P. Vogel. *Topological quantum field theories derived from the Kauffman bracket.* Topology 34 (1995), 883–927.
- **[Foundational]** M. Freedman, K. Walker, Z. Wang. *Quantum SU(2) faithfully detects mapping class groups modulo center.* Geometry & Topology 6 (2002), 523–539. [DOI](https://doi.org/10.2140/gt.2002.6.523)
- **[Foundational]** J. E. Andersen. *Asymptotic faithfulness of the quantum SU(n) representations of the mapping class groups.* Annals of Mathematics 163 (2006), 347–368. [DOI](https://doi.org/10.4007/annals.2006.163.347)
- **[Foundational]** G. Masbaum. *An element of infinite order in TQFT-representations of mapping class groups.* Contemporary Mathematics 233, AMS (1999), 137–139. [DOI](https://doi.org/10.1090/conm/233/03423)
- **[SOTA / Recent]** R. Detcherry, E. Kalfagianni. *Quantum representations and monodromies of fibered links.* Advances in Mathematics 351 (2019), 676–701. [DOI](https://doi.org/10.1016/j.aim.2019.05.014)
- **[SOTA / Recent]** R. Detcherry, E. Kalfagianni. *Gromov norm and Turaev–Viro invariants of 3-manifolds.* Annales Scientifiques de l'École Normale Supérieure 53 (2020), 1363–1391. [DOI](https://doi.org/10.24033/asens.2449)
- **[SOTA / Recent]** Q. Chen, T. Yang. *Volume conjectures for the Reshetikhin–Turaev and the Turaev–Viro invariants.* Quantum Topology 9 (2018), 419–460. [DOI](https://doi.org/10.4171/qt/111)
- **[SOTA / Recent]** R. Santharoubane. *Action of $M(0,2n)$ on some kernel spaces coming from $SU(2)$-TQFT.* Journal of the London Mathematical Society 95 (2017), 785–803. [DOI](https://doi.org/10.1112/jlms.12037)
- **[SOTA / Recent]** J. K. Egsgaard, S. F. Jørgensen. *The homological content of the Jones representations at $q=-1$.* Journal of Knot Theory and Its Ramifications 25 (2016). [DOI](https://doi.org/10.1142/s0218216516500620)
- **[SOTA / Recent]** T. Koberda, R. Santharoubane. *Quotients of surface groups and homology of finite covers via quantum representations.* Inventiones Mathematicae 206 (2016), 269–292. [DOI](https://doi.org/10.1007/s00222-016-0652-x)
- **[SOTA / Recent]** J. Marché, M. Narimannejad. *Some asymptotics of topological quantum field theory via skein theory.* Duke Mathematical Journal 141 (2008), 573–587. [DOI](https://doi.org/10.1215/00127094-2007-006)
- **[Survey]** V. Turaev. *Quantum Invariants of Knots and 3-Manifolds.* de Gruyter Studies in Mathematics 18, 1994 (3rd ed. 2016).
- **[Survey]** B. Farb, D. Margalit. *A Primer on Mapping Class Groups.* Princeton University Press, 2012.

## 10. Worked Example / Concrete Special Case

**Setting.** $\Sigma_{0,4}$, the four-punctured sphere — the one case proved in full by AMU.

*Step 1: a pseudo-Anosov.* Let $a,b$ be simple closed curves with geometric intersection $i(a,b)=2$. The hyperelliptic double cover $T^2 \to S^2$ gives $\mathrm{Mod}(\Sigma_{0,4}) \cong \mathrm{PGL}_2(\mathbb{Z}) \ltimes (\mathbb{Z}/2)^2$, under which
$$t_a \mapsto \begin{pmatrix}1&2\\0&1\end{pmatrix}, \qquad t_b^{-1} \mapsto \begin{pmatrix}1&0\\2&1\end{pmatrix}.$$
Then
$$\varphi = t_a t_b^{-1} \mapsto \begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}1&0\\2&1\end{pmatrix} = \begin{pmatrix}5&2\\2&1\end{pmatrix},$$
with $|\mathrm{tr}| = 6 > 2$, so $\varphi$ is pseudo-Anosov with dilatation
$$\lambda = \tfrac{6+\sqrt{32}}{2} = 3 + 2\sqrt{2} \approx 5.828.$$

*Step 2: the quantum representation.* Take $p = 2r = 10$ ($r=5$), all four punctures colored $1$. Then $\dim V_p(\Sigma_{0,4};1,1,1,1) = 2$, with basis indexed by the color $c \in \{0,2\}$ on a curve separating two punctures from the other two. In this basis the twist along that curve is diagonal:
$$\rho(t_a) = \begin{pmatrix}\mu_0 & 0\\ 0 & \mu_2\end{pmatrix}, \qquad \mu_c = (-1)^c A^{c^2+2c} \;\Rightarrow\; \mu_0 = 1,\ \mu_2 = A^{8}.$$
With $A$ a primitive $20$-th root of unity, $A^8$ has order $5$, so $\rho(t_a)$ has order exactly $5$ in $\mathrm{PGL}_2$. The twist $t_b$ is conjugate to $t_a$ by the $2\times2$ fusion (change-of-pants-decomposition) matrix built from Kauffman bracket $6j$-symbols, so $\rho(t_b)$ also has order $5$.

*Step 3: the point of the conjecture.* Both generators have order $5$; yet AMU show that the group $\Gamma_p = \langle \rho(t_a), \rho(t_b)\rangle \subset \mathrm{PSL}_2(\mathbb{C})$ is, for $p \ge 10$, a triangle-type group in which the image of any pseudo-Anosov word is a **loxodromic** element — $|\mathrm{tr}\,\rho(\varphi)| > 2$ after suitable normalization — hence of infinite order. Concretely $\rho(t_a t_b^{-1})$ is a product of two order-$5$ elliptics whose axes are far enough apart that the product is hyperbolic.

*Step 4: contrast.* Replace $\varphi$ by $\psi = t_a t_b$, mapping to $\begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}1&0\\-2&1\end{pmatrix} = \begin{pmatrix}-3&2\\-2&1\end{pmatrix}$, trace $-2$: parabolic, so $\psi$ is reducible (a power of a twist along a curve fixed by $\psi$), and $\rho(\psi)$ has finite order at every level. The two computations differ only by an exponent sign, yet the TQFT image jumps from finite to infinite order — this is the dichotomy the AMU conjecture asserts holds on every $\Sigma_{g,n}$, and which is verified only for the families listed in Section 4.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*