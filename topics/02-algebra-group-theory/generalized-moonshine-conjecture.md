---
id: 02-algebra-group-theory/generalized-moonshine-conjecture
title: "Generalized Moonshine Conjecture"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Generalized Moonshine Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/generalized-moonshine-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mathbb{M}$ be the Monster simple group, of order
$$|\mathbb{M}| = 2^{46}\cdot 3^{20}\cdot 5^9\cdot 7^6\cdot 11^2\cdot 13^3\cdot 17\cdot 19\cdot 23\cdot 29\cdot 31\cdot 41\cdot 47\cdot 59\cdot 71 \approx 8.08\times 10^{53}.$$

**Norton's Generalized Moonshine Conjecture (1987).** There is a function
$$Z:\{(g,h)\in\mathbb{M}\times\mathbb{M} : gh=hg\}\times\mathfrak{H}\longrightarrow\mathbb{C},\qquad (g,h,\tau)\mapsto Z(g,h;\tau),$$
holomorphic in $\tau$ on the upper half-plane $\mathfrak{H}$, such that:

1. **(Equivariance)** $Z(aga^{-1},aha^{-1};\tau)=Z(g,h;\tau)$ for all $a\in\mathbb{M}$.
2. **(Modularity)** For $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb{Z})$,
 $$Z\!\left(g,h;\tfrac{a\tau+b}{c\tau+d}\right)=\sigma(g,h,\gamma)\,Z\!\left(g^ah^c,\,g^bh^d;\tau\right)$$
 for some scalar $\sigma(g,h,\gamma)$ of modulus $1$ (a root of unity of order dividing $24$, independent of $\tau$).
3. **(Expansion)** The Fourier coefficients of $Z(g,h;\tau)$ in $q^{1/N}=e^{2\pi i\tau/N}$, $N=\operatorname{ord}(g)$, are characters of a projective representation of the centralizer $C_{\mathbb{M}}(g)$ evaluated at $h$.
4. **(Genus zero)** $Z(g,h;\tau)$ is either constant in $\tau$, or a **Hauptmodul** — a generator of the field of modular functions — for a genus-zero discrete subgroup $\Gamma_{g,h}\le PSL_2(\mathbb{R})$ commensurable with $PSL_2(\mathbb{Z})$.
5. **(Normalization)** $Z(1,h;\tau)=T_h(\tau)$, the monstrous-moonshine McKay–Thompson series, and $Z(1,1;\tau)=J(\tau)=q^{-1}+196884q+21493760q^2+\cdots$.

A complete proof requires constructing $Z$ globally (uniformly in $(g,h)$, with a coherent cocycle $\sigma$) and establishing (4) for all $\sim 10^4$ commuting-pair conjugacy classes. A disproof would exhibit a commuting pair whose trace function is non-constant and not a Hauptmodul, or show no consistent choice of projective representations exists.

## 2. Mathematical Foundations

**The Moonshine module.** $V^\natural=\bigoplus_{n\ge -1}V^\natural_n$ is the Frenkel–Lepowsky–Meurman vertex operator algebra (VOA): a $\mathbb{Z}$-graded vector space with a state–field map $Y(\cdot,z):V^\natural\to\operatorname{End}(V^\natural)[[z,z^{-1}]]$, Virasoro action of central charge $c=24$, $V^\natural_0=\mathbb{C}\mathbf{1}$, $V^\natural_1=0$, $\dim V^\natural_2 = 196884$, and $\operatorname{Aut}(V^\natural)=\mathbb{M}$. Its graded dimension is
$$\operatorname{ch} V^\natural(\tau)=\sum_{n\ge -1}(\dim V^\natural_{n+1})\,q^{n}=J(\tau).$$
The McKay–Thompson series is $T_g(\tau)=\sum_{n\ge -1}\operatorname{tr}(g\mid V^\natural_{n+1})q^n$; there are $194$ conjugacy classes and $171$ distinct series.

**Twisted modules.** For $g\in\mathbb{M}$ of order $N$, a $g$-twisted $V^\natural$-module is a space $V^\natural(g)=\bigoplus_{n\in\frac{1}{N}\mathbb{Z}}V^\natural(g)_n$ with fields obeying the equivariance $Y_g(gv,z)=Y_g(v,e^{2\pi i}z)$. Since $V^\natural$ is holomorphic ($C_2$-cofinite, rational, with unique irreducible untwisted module), $V^\natural(g)$ is unique up to isomorphism, and $C_{\mathbb{M}}(g)$ acts on it projectively, via a central extension
$$1\to \mathbb{C}^\times \to \widetilde{C_{\mathbb{M}}(g)}\to C_{\mathbb{M}}(g)\to 1$$
whose class lies in $H^2(C_{\mathbb{M}}(g),\mathbb{C}^\times)$. The generalized moonshine function is then the twisted trace
$$Z(g,h;\tau)=\operatorname{tr}\!\left(\tilde h\, q^{L_0-\,c/24}\ \big|\ V^\natural(g)\right),\qquad c=24,$$
for a chosen lift $\tilde h$. Property (2) is the statement that the $SL_2(\mathbb{Z})$-action on commuting pairs, $\gamma\cdot(g,h)=(g^ah^c,g^bh^d)$, is realized by modular transformation; in physics language $Z(g,h;\tau)$ is the genus-one partition function of the Monster orbifold conformal field theory with $g$-twist around the space cycle and $h$-twist around the time cycle.

**Obstruction cocycle.** The scalars $\sigma$ are governed by a class $\omega\in H^3(\mathbb{M},\mathbb{C}^\times)$, with $H^3(\mathbb{M},\mathbb{Z})$ containing an element of order $24$; the projective representation of $C_{\mathbb{M}}(g)$ carries the transgressed class $\tau_g(\omega)\in H^2(C_{\mathbb{M}}(g),\mathbb{C}^\times)$. Consistency of the whole family is a statement about the $\mathbb{M}$-equivariant modular tensor category attached to $V^\natural$.

**Hauptmoduln.** $\Gamma\le PSL_2(\mathbb{R})$ of genus zero means $\mathfrak{H}/\Gamma$ has genus $0$, so its function field is $\mathbb{C}(f)$ for a single $f$; e.g. $\Gamma_0(2)+$ has Hauptmodul $T_{2A}$.

## 3. History & State of the Art (SOTA)

- **1979.** Conway and Norton formulate Monstrous Moonshine: each $T_g$ is a Hauptmodul.
- **1984–88.** Frenkel, Lepowsky, Meurman construct $V^\natural$ as a $\mathbb{Z}_2$-orbifold of the Leech lattice VOA.
- **1987.** Norton states generalized moonshine in an appendix to Mason's paper, motivated by numerical study of the $\sim 10^4$ commuting pairs and by orbifold intuition.
- **1988.** Dixon, Ginsparg, Harvey give the CFT interpretation: $Z(g,h;\tau)$ as twisted sectors of a Monster orbifold.
- **1992.** Borcherds proves Monstrous Moonshine ($g=1$) via the Monster Lie algebra and generalized Kac–Moody denominator identities; Fields Medal 1998.
- **2000.** Dong, Li, Mason prove modular invariance of orbifold trace functions for $C_2$-cofinite rational VOAs — supplying (2) in a general axiomatic setting, but not the genus-zero property.
- **2003.** Höhn proves generalized moonshine for $g$ in class 2A using the baby-monster VOA $VB^\natural$.
- **2010–2012.** Carnahan's programme (papers I, II, IV) reduces the conjecture to orbifold-theoretic input and proves it under that hypothesis.
- **2015–2020.** van Ekeren, Möller, Scheithauer establish modular invariance and the orbifold construction for cyclic orbifolds of holomorphic $c=24$ VOAs, supplying Carnahan's missing hypothesis.

## 4. Partial Results / Verified Cases

- **$g=1$ (all 194 classes of $h$, 171 series):** fully proven — Borcherds (1992).
- **$g$ in class 2A, $C_{\mathbb{M}}(g)=2.\mathbb{B}$:** fully proven by Höhn (2003) via $VB^\natural$, the $c=23\tfrac12$ baby-monster VOA; here $\dim V^\natural(g)_{1/2}=4372=1+4371$, matching $\mathbb{B}$'s smallest nontrivial irreducible representation.
- **$g$ of prime order $p\in\{2,3,5,7,13\}$** (the classes $pA$ with $V^\natural/\langle g\rangle$ again holomorphic $c=24$): twisted modules and their characters are explicitly known; Hauptmodul property verified.
- **Abelian subgroup cases:** $\langle g,h\rangle$ cyclic or of small rank — Tuite's analysis, and Ivanov–Tuite's $\mathbb{Z}_p$-orbifold computations, establish the genus-zero property assuming uniqueness of $V^\natural$.
- **Numerical verification:** Norton and successors checked the modular and genus-zero data across essentially all $\sim 10^4$ commuting-pair classes to many Fourier coefficients.
- **Full statement modulo published orbifold input:** Carnahan (2012, arXiv:1208.6254) proves the conjecture for all commuting pairs, conditional on a cyclic-orbifold hypothesis now established by van Ekeren–Möller–Scheithauer *(frontier — verify: the combined argument is accepted by specialists but "Generalized Moonshine IV" remains a preprint)*.

## 5. Principal Obstacles

- **No uniform construction of twisted modules.** Existence and uniqueness of $V^\natural(g)$ for arbitrary $g$ does not follow from finite-group representation theory; it needs the full analytic machinery of $C_2$-cofinite rational VOA theory, and explicit models exist only for a handful of classes.
- **Cohomological obstruction.** The projective $C_{\mathbb{M}}(g)$-action is only well-defined up to a scalar; assembling compatible lifts across all $g$ simultaneously is a statement in $H^3(\mathbb{M},\mathbb{C}^\times)$ that cannot be checked class-by-class.
- **Genus zero is not automatic.** Modular invariance (Dong–Li–Mason) gives only that $Z(g,h)$ is a modular function on a congruence-type group. That group being genus zero is an exceptional, non-generic property; there is no representation-theoretic mechanism forcing it. Borcherds' route — replicability plus Koike–Norton–Zagier's classification of completely replicable functions — has no direct analogue for $(g,h)$ pairs of non-trivial $g$.
- **Lie-algebra methods degrade under twisting.** Borcherds used the Monster Lie algebra $\mathfrak{m}=\mathfrak{g}_{V^\natural\otimes V_{1,1}}$ with a clean $\mathrm{II}_{1,1}$ root lattice. The twisted analogues (Carnahan's "monstrous Lie algebras") have root lattices with $\frac{1}{N}\mathbb{Z}$-gradings and Weyl-vector data that are much harder to control; denominator identities become Borcherds products with non-trivial multiplier systems.
- **Scale.** The Monster's $194$ classes give $\sim 10^4$ commuting-pair orbits; case analysis is infeasible without a structural theorem.

## 6. The Gap

Proven: the $g=1$ row (Borcherds); the $2A$ column (Höhn); modular invariance in general (Dong–Li–Mason); and the reduction of genus zero to a Borcherds-product/replicability criterion (Carnahan I–II).

The residual gap is the transition from *"$Z(g,h)$ is a modular function of level $\operatorname{ord}(g)\operatorname{ord}(h)$ with a $24$-th root of unity multiplier"* to *"$Z(g,h)$ is a Hauptmodul"*. Carnahan closes it by constructing, for each $g$, a $\frac{1}{N}\mathbb{Z}$-graded generalized Kac–Moody Lie algebra whose denominator identity forces the twisted analogue of complete replicability, then invoking a Hauptmodul criterion. The remaining formal deficits are: (i) publication and full referee verification of "Generalized Moonshine IV"; (ii) confirming that the cyclic-orbifold theorems of van Ekeren–Möller–Scheithauer supply exactly the hypothesis used, uniformly in $g$; (iii) a self-contained treatment of the $H^3(\mathbb{M},\mathbb{C}^\times)$ coherence data.

## 7. Current Research (as of June 2026)

- **VOA orbifold theory.** Möller, Scheithauer, van Ekeren, and collaborators continue classifying holomorphic $c=24$ VOAs and non-cyclic orbifolds; this directly strengthens the foundations under Carnahan's proof.
- **Categorical moonshine.** Reformulating generalized moonshine as data of an $\mathbb{M}$-equivariant modular tensor category with anomaly $\omega\in H^3(\mathbb{M},U(1))$ — work in the orbit of Evans–Gannon, Johnson-Freyd, and the "topological moonshine" community *(frontier — verify)*.
- **Umbral/Mathieu generalizations.** Gaberdiel, Persson, Ronellenfitsch, Volpato's generalized Mathieu moonshine for $M_{24}$ and its twining/twisted genera provides a testbed where the $H^3$ obstruction is computable.
- **Physics.** AdS$_3$/CFT$_2$ interpretations of the Monster CFT (Duncan–Frenkel Rademacher sums; Witten's extremal-CFT programme) predict the analytic shape of $Z(g,h)$ from black-hole/BTZ sums.
- **Institutions.** Tsukuba (Carnahan), Kansas State (Höhn), Darmstadt/Rutgers (Scheithauer, Möller), Cambridge/ETH (Gaberdiel, Cheng), Perimeter (Johnson-Freyd).

## 8. Future Work

- Publish and fully verify Carnahan IV; produce a streamlined, self-contained account of the twisted Borcherds-product argument.
- Give a conceptual (non-case-checking) proof of genus zero — a "why", not a "that". Duncan–Frenkel's Rademacher-sum characterization is the leading candidate: show $Z(g,h)$ equals a regularized Poincaré series, from which the Hauptmodul property is automatic.
- Compute $H^3(\mathbb{M},\mathbb{C}^\times)$ and the transgressions $\tau_g(\omega)$ explicitly; identify the "moonshine anomaly" class.
- Extend generalized moonshine to non-commuting pairs / higher genus, i.e. a full $\mathbb{M}$-equivariant TQFT-style statement.
- Transfer the machinery to umbral moonshine, the Conway group $Co_0$ module $V^{s\natural}$, and the $\mathcal{O}^\natural$ family.

## 9. Key References

- **[Foundational]** J. H. Conway and S. P. Norton. *Monstrous Moonshine.* Bulletin of the London Mathematical Society **11** (1979), 308–339.
- **[Foundational]** S. P. Norton. *Generalized Moonshine.* Appendix to G. Mason, "Finite Groups and Modular Functions", Proc. Sympos. Pure Math. **47** Part 1, AMS, 1987, 208–209.
- **[Foundational]** I. Frenkel, J. Lepowsky, A. Meurman. *Vertex Operator Algebras and the Monster.* Pure and Applied Mathematics **134**, Academic Press, 1988. [DOI](https://doi.org/10.1016/s0079-8169(08)x6136-7)
- **[Foundational]** R. E. Borcherds. *Monstrous moonshine and monstrous Lie superalgebras.* Inventiones Mathematicae **109** (1992), 405–444. [DOI](https://doi.org/10.1007/bf01232032)
- **[Foundational]** L. Dixon, P. Ginsparg, J. Harvey. *Beauty and the Beast: Superconformal Symmetry in a Monster Module.* Communications in Mathematical Physics **119** (1988), 221–241. [DOI](https://doi.org/10.1007/bf01217740)
- **[SOTA]** C. Dong, H. Li, G. Mason. *Modular invariance of trace functions in orbifold theory and generalized moonshine.* Communications in Mathematical Physics **214** (2000), 1–56. [DOI](https://doi.org/10.1007/s002200000242)
- **[SOTA]** G. Höhn. *Generalized Moonshine for the Baby Monster.* Preprint/Habilitationsschrift, Universität Freiburg, 2003.
- **[SOTA]** S. Carnahan. *Generalized moonshine I: Genus-zero functions.* Algebra & Number Theory **4** (2010), 649–679. [DOI](https://doi.org/10.2140/ant.2010.4.649)
- **[SOTA]** S. Carnahan. *Generalized moonshine II: Borcherds products.* Duke Mathematical Journal **161** (2012), 893–950. [DOI](https://doi.org/10.1215/00127094-1548416)
- **[SOTA]** S. Carnahan. *Generalized moonshine IV: Monstrous Lie algebras.* arXiv:1208.6254.
- **[SOTA]** J. van Ekeren, S. Möller, N. R. Scheithauer. *Construction and classification of holomorphic vertex operator algebras.* Journal für die reine und angewandte Mathematik (Crelle) **759** (2020), 61–99.
- **[Recent]** M. R. Gaberdiel, D. Persson, H. Ronellenfitsch, R. Volpato. *Generalized Mathieu Moonshine.* Communications in Number Theory and Physics **7** (2013), 145–223. [DOI](https://doi.org/10.4310/cntp.2013.v7.n1.a5)
- **[Survey]** T. Gannon. *Moonshine Beyond the Monster: The Bridge Connecting Algebra, Modular Forms and Physics.* Cambridge University Press, 2006.
- **[Survey]** J. F. R. Duncan, M. J. Griffin, K. Ono. *Moonshine.* Research in the Mathematical Sciences **2** (2015), Article 11.
- **[Survey]** J. F. R. Duncan, I. B. Frenkel. *Rademacher sums, moonshine and gravity.* Communications in Number Theory and Physics **5** (2011), 849–976. [DOI](https://doi.org/10.4310/cntp.2011.v5.n4.a4)

## 10. Worked Example / Concrete Special Case

Take $g$ in class $2A$ (a Monster transposition, $C_{\mathbb{M}}(g)\cong 2.\mathbb{B}$) and compute the pair $(1,g)\mapsto(g,1)$ under $S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$.

**Step 1 — the untwisted side.** $Z(1,g;\tau)=T_{2A}(\tau)$, the Hauptmodul for $\Gamma_0(2)+$:
$$T_{2A}(\tau)=\left(\frac{\eta(\tau)}{\eta(2\tau)}\right)^{24}+2^{12}\left(\frac{\eta(2\tau)}{\eta(\tau)}\right)^{24}+24 = q^{-1}+4372q+96256q^2+1240002q^3+\cdots$$
The coefficient $4372=1+4371$ decomposes $V^\natural_2$-restricted-to-$2.\mathbb{B}$ data: $4371$ is the smallest nontrivial irreducible character degree of the Baby Monster $\mathbb{B}$.

**Step 2 — apply $S$.** Since $S\cdot(1,g)=(g^0 g^1, 1^{\,\cdot})=(g,1)$, the conjecture predicts $Z(g,1;\tau)=T_{2A}(-1/\tau)$, and this must be the graded dimension of the $g$-twisted module $V^\natural(g)$.

**Step 3 — transform.** Using $\eta(-1/\tau)^{24}=\tau^{12}\eta(\tau)^{24}$ and $\eta(-2/\tau)^{24}=(\tau/2)^{12}\eta(\tau/2)^{24}$,
$$\left(\frac{\eta(-1/\tau)}{\eta(-2/\tau)}\right)^{24}=2^{12}\left(\frac{\eta(\tau)}{\eta(\tau/2)}\right)^{24},$$
so
$$T_{2A}(-1/\tau)=\left(\frac{\eta(\tau/2)}{\eta(\tau)}\right)^{24}+2^{12}\left(\frac{\eta(\tau)}{\eta(\tau/2)}\right)^{24}+24 .$$

**Step 4 — expand.** With $\eta(\tau/2)/\eta(\tau)=q^{-1/48}\prod_{n\ \text{odd}}(1-q^{n/2})$,
$$\left(\frac{\eta(\tau/2)}{\eta(\tau)}\right)^{24}=q^{-1/2}\prod_{n\ \text{odd}}\left(1-q^{n/2}\right)^{24}=q^{-1/2}\left(1-24q^{1/2}+276q-\cdots\right)=q^{-1/2}-24+276q^{1/2}-\cdots,$$
$$2^{12}\left(\frac{\eta(\tau)}{\eta(\tau/2)}\right)^{24}=4096\,q^{1/2}\left(1+24q^{1/2}+\cdots\right)=4096q^{1/2}+98304q+\cdots .$$
Adding, the $-24$ cancels the $+24$ and
$$Z(g,1;\tau)=q^{-1/2}+0\cdot q^{0}+(276+4096)\,q^{1/2}+\cdots=q^{-1/2}+4372\,q^{1/2}+\cdots .$$

**Step 5 — read off the content.** The half-integral grading confirms $V^\natural(g)=\bigoplus_{n\in\frac12\mathbb{Z}}V^\natural(g)_n$, as required for an order-$2$ twist, and $\dim V^\natural(g)_{1/2}=4372=1+4371$ — a genuine $2.\mathbb{B}$-module. Höhn's theorem realizes this space inside the baby-monster VOA $VB^\natural$ of central charge $23\tfrac12$, and thereby proves all of Norton's axioms for every $h\in C_{\mathbb{M}}(g)=2.\mathbb{B}$. Doing the same for a class such as $g\in 13B$ or $g\in 27A$ — where no explicit twisted module has been written down — is precisely what the general conjecture asks.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*