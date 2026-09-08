---
id: 02-algebra-group-theory/moonshine-conjecture
title: "Moonshine Conjecture"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Moonshine Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/moonshine-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The **monstrous moonshine conjecture** of Conway and Norton (1979) asserts that there exists a graded representation of the Monster sporadic simple group $\mathbb{M}$,
$$V^\natural = \bigoplus_{n \geq -1} V^\natural_n, \qquad \dim V^\natural_n < \infty,$$
such that for every $g \in \mathbb{M}$ the **McKay–Thompson series**
$$T_g(\tau) \;=\; \sum_{n \geq -1} \operatorname{Tr}\!\left(g \mid V^\natural_n\right) q^n, \qquad q = e^{2\pi i \tau},\ \tau \in \mathbb{H},$$
is the normalized *hauptmodul* (generator of the field of modular functions) for a genus-zero discrete subgroup $\Gamma_g \subset \mathrm{SL}_2(\mathbb{R})$ commensurable with $\mathrm{SL}_2(\mathbb{Z})$. For $g = e$ the claim is $T_e(\tau) = J(\tau) = j(\tau) - 744$.

A complete proof must supply (i) the module $V^\natural$ with its $\mathbb{M}$-action, (ii) identification of each $\Gamma_g$ from the Conway–Norton list of 171 functions, and (iii) the **genus-zero property**: $\Gamma_g \backslash \mathbb{H}^*$ has genus $0$ and $T_g$ generates its function field. Item (iii) has been *verified* but never *explained*; a conceptual proof remains open.

## 2. Mathematical Foundations

**The Monster.** $\mathbb{M}$ is the largest sporadic finite simple group, of order
$$|\mathbb{M}| = 2^{46}\,3^{20}\,5^{9}\,7^{6}\,11^{2}\,13^{3}\,17\cdot19\cdot23\cdot29\cdot31\cdot41\cdot47\cdot59\cdot71 \approx 8.08 \times 10^{53},$$
with $194$ conjugacy classes and irreducible character degrees beginning $1,\,196883,\,21296876,\,842609326$.

**The modular $j$-function.** The unique $\mathrm{SL}_2(\mathbb{Z})$-invariant hauptmodul with $q$-expansion
$$j(\tau) = \frac{1}{q} + 744 + 196884\,q + 21493760\,q^2 + 864299970\,q^3 + \cdots$$

**McKay's observation.** $196884 = 196883 + 1$, and more:
$$21493760 = 21296876 + 196883 + 1, \qquad 864299970 = 842609326 + 21296876 + 2\cdot196883 + 2\cdot 1 .$$

**Vertex operator algebras.** A VOA is a $\mathbb{Z}$-graded vector space $V=\bigoplus_n V_n$ with a state-field map $Y(\cdot,z): V \to \mathrm{End}(V)[[z^{\pm1}]]$, vacuum $\mathbf{1}$, and conformal vector $\omega$ whose modes give a Virasoro action of central charge $c$. Its graded character is
$$Z_V(\tau) = \operatorname{Tr}_V q^{L_0 - c/24}.$$
Frenkel–Lepowsky–Meurman built $V^\natural$ as a $\mathbb{Z}_2$-orbifold of the Leech lattice VOA $V_\Lambda$ by the lift of $-1$:
$$V^\natural = V_\Lambda^+ \oplus (V_\Lambda^T)^+, \qquad c = 24,\qquad V^\natural_1 = 0,\qquad Z_{V^\natural}(\tau) = J(\tau).$$
Here $\operatorname{Aut}(V^\natural) \cong \mathbb{M}$.

**Groups $\Gamma_g$.** Each is of type $n|h + e,f,\dots$: $\Gamma_0(N)$ with $N = nh$, extended by Atkin–Lehner involutions $W_e$ and an Aktin–Lehner-normalizing coset from $h \mid n$, $h \mid 24$.

**Borcherds' engine.** The Monster Lie algebra $\mathfrak{m}$ is a generalized Kac–Moody algebra with root multiplicities $\dim \mathfrak{m}_{(m,n)} = c(mn)$ where $J(q)=\sum c(n)q^n$. Its denominator identity is
$$p^{-1}\prod_{m>0,\;n\in\mathbb{Z}} (1 - p^m q^n)^{c(mn)} \;=\; j(\sigma) - j(\tau), \qquad p = e^{2\pi i\sigma}.$$
Twisting by $g \in \mathbb{M}$ gives, for the head characters $T_g$, the **replication formulas**
$$T_g(p)-T_g(q)\ \text{analogues}, \qquad \sum_{d \mid n} \frac{1}{d}\,\mathrm{H}_{g^d}\ \text{recursions},$$
including the Mahler-type relations $c_g(4)=c_g(3)c_{g}(1)-\cdots$, which determine each $T_g$ from its first few coefficients.

## 3. History & State of the Art (SOTA)

- **1978.** John McKay notes $196884 = 196883+1$; John Thompson proposes a graded module and the study of $\operatorname{Tr}(g\mid V_n)$ (Thompson, *Bull. LMS*, 1979).
- **1979.** Conway and Norton, *Monstrous Moonshine*, tabulate 171 candidate hauptmoduln and state the full conjecture.
- **1980.** Griess constructs $\mathbb{M}$ explicitly as the automorphism group of a $196883$-dimensional commutative nonassociative algebra.
- **1984–1988.** Frenkel, Lepowsky, Meurman construct $V^\natural$ and prove $Z_{V^\natural} = J$ with $\operatorname{Aut} = \mathbb{M}$ (book, 1988).
- **1985–1992.** Borcherds develops vertex algebras and generalized Kac–Moody algebras; his 1992 *Inventiones* paper *Monstrous moonshine and monstrous Lie superalgebras* proves the Conway–Norton conjecture for the FLM module. Fields Medal, 1998.
- **1990s–2000s.** Norton's generalized moonshine; Tuite's orbifold approach linking genus zero to uniqueness of $V^\natural$.
- **2010–2015.** Mathieu moonshine (Eguchi–Ooguri–Tachikawa) and umbral moonshine (Cheng–Duncan–Harvey) open a mock-modular chapter.
- **2015–2017.** Duncan–Griffin–Ono prove umbral moonshine existence; Gannon proves $M_{24}$ moonshine; Carnahan's four-part program addresses generalized moonshine.

## 4. Partial Results / Verified Cases

- **All 194 conjugacy classes / 171 distinct functions.** Borcherds (1992) proved $T_g$ equals the Conway–Norton function for *every* $g \in \mathbb{M}$; the genus-zero property is then verified class by class against the finite table.
- **Coefficient checks.** Thompson and Atkin–Fong–Smith (1985) had already shown, before any construction, that the *virtual* character interpretation is consistent: there exist virtual characters realizing all $T_g$ coefficients. Fong handled $p$-adic congruences for $p \in \{2,3,5,7,11,13\}$.
- **Replicability.** Every $T_g$ is completely replicable; Cummins–Gannon (1997) proved that a completely replicable $q$-series with integer coefficients is either a hauptmodul or a trigonometric-type degenerate function — a near-classification.
- **Genus-zero groups of level $N$.** For $N \le 100$ with $h \mid 24$, all relevant $\Gamma_0(N)+$ genus-zero cases are enumerated (Conway–Norton table; Ferenbaugh 1993 classified genus-zero $n|h+e,\dots$ groups).
- **Generalized moonshine.** Proved by Carnahan (2012–2017) modulo a technical hypothesis on regularity of certain orbifolds *(frontier — verify current publication status)*.
- **Umbral moonshine.** Existence of the 23 modules proved for all Niemeier root systems (Duncan–Griffin–Ono, 2015); explicit VOA/SCFT realizations known only for $\ell = 2$ ($M_{24}$, by Duncan–Mack-Crane, 2016) and a few others.
- **Thompson, O'Nan, Conway moonshines.** Existence proved (Griffin–Mertens 2016; Duncan–Mertens–Ono 2017).

## 5. Principal Obstacles

- **Genus zero is proven but not explained.** Borcherds' proof is a verification: replication formulas pin down each $T_g$, and one then checks against a table of hauptmoduln. No argument derives "genus zero" from a structural property of $\mathbb{M}$ or $V^\natural$. Standard automorphic techniques (Eichler–Selberg, trace formulas) compute dimensions of modular forms but say nothing about why the *specific* $\Gamma_g$ arising from a finite group action must have genus $0$.
- **Uniqueness of $V^\natural$.** The FLM conjecture — $V^\natural$ is the unique holomorphic $C_2$-cofinite VOA with $c=24$ and $V_1=0$ — is open. Tuite showed genus zero follows from uniqueness plus orbifold hypotheses, so the obstacle is transferred, not removed. Classification methods that succeeded for the other 70 entries of Schellekens' list (van Ekeren–Möller–Scheithauer, 2020) rely on a nonzero weight-one Lie algebra $V_1$, exactly the structure absent here.
- **Case-by-case combinatorics.** Borcherds' twisted denominator identities require Hauptmodul input for each class; the argument does not extend uniformly to arbitrary finite groups.
- **Mock modularity.** In umbral and Mathieu moonshine the generating functions are mock modular of weight $1/2$; the shadow obstructs the Rankin–Cohen/holomorphic-projection tools that work in the integral-weight case, and no Borcherds-type Lie algebra is known.
- **No module-theoretic proof of $M_{24}$ moonshine.** Gannon's proof is character-theoretic (positivity plus congruences); it produces no natural $M_{24}$-action, so the geometry (K3 sigma models) remains conjectural.

## 6. The Gap

Proven: for each $g\in\mathbb{M}$, $T_g$ *coincides with* a specified genus-zero hauptmodul. Not proven: any statement of the form

> **(Genus-zero principle)** If $V$ is a holomorphic VOA with $c=24$, $V_1 = 0$, and $g \in \operatorname{Aut}(V)$, then $\operatorname{Tr}(g\,q^{L_0-1})$ is invariant under a genus-zero group.

The precise missing step is a proof that the orbifold $V/\langle g\rangle$ is again isomorphic to $V^\natural$ (or has controlled character), for all $g$, without invoking the classification table. That in turn requires the FLM uniqueness conjecture, whose own gap is the classification of holomorphic $c=24$ VOAs with vanishing weight-one space.

## 7. Current Research (as of June 2026)

- **Uniqueness of $V^\natural$.** Programs of Höhn, Möller, Scheithauer and collaborators extend orbifold and lattice-genus methods to the $V_1 = 0$ case; partial reductions to controlling $\mathbb{Z}_p$-orbifolds for small $p$ *(frontier — verify)*.
- **Rademacher sums and 3d gravity.** Duncan–Frenkel's proposal that $T_g$ is a regularized Poincaré series over $\Gamma_g$ recasts genus zero as convergence/optimal-growth; connected to Witten's extremal CFT and to the modular bootstrap.
- **Umbral/K3 geometry.** Cheng, Duncan, Harvey, Taormina, Wendland: symmetry-surfing constructions aiming at an $M_{24}$-module from K3 sigma-model moduli.
- **Moonshine beyond the Monster.** O'Nan and Thompson moonshine linked to arithmetic of quadratic fields and class numbers (Duncan–Mertens–Ono); active work on divisibility of class numbers via moonshine coefficients.
- **Groups:** Rutgers/Emory (Ono, Griffin), Imperial/Academia Sinica (Cheng), Case Western (Duncan), Kyoto/IPMU, TU Darmstadt (Scheithauer), and the Tsukuba/Carnahan program on generalized moonshine.

## 8. Future Work

1. Prove the FLM uniqueness conjecture, then deduce genus zero via Tuite's orbifold argument.
2. Establish a Borcherds-type generalized Kac–Moody algebra whose denominator identity produces mock modular forms, giving umbral moonshine a Lie-algebra proof.
3. Complete Carnahan's generalized moonshine unconditionally by removing regularity hypotheses on cyclic orbifolds.
4. Find a physical derivation: a chiral 3d quantum gravity whose partition function is $J$ and whose defects are Monster elements, making genus zero a statement about the absence of extra states.
5. Classify all finite groups $G$ and holomorphic VOAs for which the "moonshine phenomenon" (genus-zero or mock-modular traces) occurs — a moonshine classification theorem.

## 9. Key References

- **[Foundational]** J. H. Conway and S. P. Norton. *Monstrous Moonshine.* Bulletin of the London Mathematical Society, 11(3):308–339, 1979.
- **[Foundational]** J. G. Thompson. *Some numerology between the Fischer–Griess Monster and the elliptic modular function.* Bulletin of the London Mathematical Society, 11(3):352–353, 1979. [DOI](https://doi.org/10.1112/blms/11.3.352)
- **[Foundational]** I. Frenkel, J. Lepowsky, A. Meurman. *Vertex Operator Algebras and the Monster.* Academic Press, Pure and Applied Mathematics 134, 1988. [DOI](https://doi.org/10.1016/s0079-8169(08)x6136-7)
- **[Foundational]** R. E. Borcherds. *Monstrous moonshine and monstrous Lie superalgebras.* Inventiones Mathematicae, 109:405–444, 1992. [DOI](https://doi.org/10.1007/bf01232032)
- **[Foundational]** R. L. Griess Jr. *The Friendly Giant.* Inventiones Mathematicae, 69:1–102, 1982.
- **[SOTA / Recent]** J. F. R. Duncan, M. J. Griffin, K. Ono. *Proof of the Umbral Moonshine Conjecture.* Research in the Mathematical Sciences, 2:26, 2015. [DOI](https://doi.org/10.1186/s40687-015-0044-7)
- **[SOTA / Recent]** T. Gannon. *Much ado about Mathieu.* Advances in Mathematics, 301:322–358, 2016. [DOI](https://doi.org/10.1016/j.aim.2016.06.014)
- **[SOTA / Recent]** J. van Ekeren, S. Möller, N. R. Scheithauer. *Construction and classification of holomorphic vertex operator algebras.* Journal für die reine und angewandte Mathematik (Crelle), 759:61–99, 2020.
- **[SOTA / Recent]** J. F. R. Duncan, M. H. Mertens, K. Ono. *O'Nan moonshine and arithmetic.* American Journal of Mathematics, 143(4):1115–1159, 2021. [DOI](https://doi.org/10.1353/ajm.2021.0029)
- **[Survey]** T. Gannon. *Moonshine Beyond the Monster: The Bridge Connecting Algebra, Modular Forms and Physics.* Cambridge University Press, 2006.
- **[Survey]** R. E. Borcherds. *What is moonshine?* Proceedings of the ICM, Berlin, Documenta Mathematica, Extra Volume ICM I:607–615, 1998.
- **[Survey]** M. C. N. Cheng, J. F. R. Duncan, J. A. Harvey. *Umbral Moonshine.* Communications in Number Theory and Physics, 8(2):101–242, 2014. [DOI](https://doi.org/10.4310/cntp.2014.v8.n2.a1)

## 10. Worked Example / Concrete Special Case

**The class $2A$ of the Monster.** Take $g$ in the class $2A$ (centralizer $2 \cdot \mathbb{B}$, the double cover of the Baby Monster). Character values on the first irreducibles are
$$\chi_1(2A)=1,\qquad \chi_{196883}(2A)=4371,\qquad \chi_{21296876}(2A)=91884 .$$

*Step 1 — trace on low-degree pieces.* Using the decompositions in §2,
$$V^\natural_1 \cong \chi_{196883} \oplus \chi_1 \ \Rightarrow\ \operatorname{Tr}(g\mid V^\natural_1) = 4371 + 1 = 4372,$$
$$V^\natural_2 \cong \chi_{21296876}\oplus\chi_{196883}\oplus\chi_1 \ \Rightarrow\ \operatorname{Tr}(g\mid V^\natural_2) = 91884 + 4371 + 1 = 96256 .$$
So the conjecture predicts
$$T_{2A}(\tau) = q^{-1} + 0 + 4372\,q + 96256\,q^2 + 1240002\,q^3 + \cdots$$

*Step 2 — the predicted hauptmodul.* Conway–Norton assign $2A$ the group $\Gamma_0(2)+$, i.e. $\Gamma_0(2)$ extended by the Fricke involution $\tau \mapsto -1/(2\tau)$. Its hauptmodul is built from the Dedekind eta function $\eta(\tau)=q^{1/24}\prod_{n\ge1}(1-q^n)$:
$$f(\tau) \;=\; \left(\frac{\eta(\tau)}{\eta(2\tau)}\right)^{24} + 4096\left(\frac{\eta(2\tau)}{\eta(\tau)}\right)^{24} + 24 .$$

*Step 3 — expand.* Since
$$\left(\frac{\eta(\tau)}{\eta(2\tau)}\right)^{24} = q^{-1}\prod_{n\ge1}\frac{(1-q^n)^{24}}{(1-q^{2n})^{24}} = q^{-1} - 24 + 276\,q - 2048\,q^2 + \cdots,$$
$$\left(\frac{\eta(2\tau)}{\eta(\tau)}\right)^{24} = q\prod_{n\ge1}\frac{(1-q^{2n})^{24}}{(1-q^{n})^{24}} = q + 24\,q^2 + \cdots,$$
adding gives constant term $-24 + 24 = 0$, and
$$[q^1]\,f = 276 + 4096 = 4372, \qquad [q^2]\,f = -2048 + 4096\cdot 24 = -2048 + 98304 = 96256 .$$

*Step 4 — conclusion.* The character-theoretic values $4372, 96256$ match the $q$-expansion of the $\Gamma_0(2)+$ hauptmodul exactly. Genus of $\Gamma_0(2)+ \backslash \mathbb{H}^*$ is $0$, so the conjecture holds for $2A$. Borcherds' replication formula for order-two elements,
$$c_g(2n) \ \text{determined by}\ c_g(n),\,c_{g^2}(n),$$
then propagates this agreement to all coefficients, converting the two hand-checked identities above into a proof for the whole class.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*