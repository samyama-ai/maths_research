---
id: 02-algebra-group-theory/mathieu-moonshine
title: "Mathieu Moonshine"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mathieu Moonshine

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/mathieu-moonshine` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The elliptic genus of a K3 surface, decomposed into characters of the $\mathcal{N}=4$ superconformal algebra at central charge $c=6$, produces integers $A_1=90$, $A_2=462$, $A_3=1540$, $A_4=4554$, $A_5=11592$. Eguchi, Ooguri and Tachikawa observed in 2010 that each is twice the dimension of an irreducible representation of the sporadic Mathieu group $M_{24}$ ($45$, $231$, $770$, $2277$, $5796$).

**Mathieu Moonshine Conjecture.** There is a $\mathbb{Z}$-graded $M_{24}$-module
$$K = \bigoplus_{n\ge 1} K_n, \qquad \dim K_n = A_n,$$
such that for every $g \in M_{24}$ the graded trace (McKay–Thompson series)
$$H_g(\tau) \;=\; -2q^{-1/8} \;+\; \sum_{n\ge 1} \operatorname{tr}(g \mid K_n)\, q^{n-1/8}$$
is a specific mock modular form of weight $1/2$ on $\Gamma_0(N_g)$ with shadow $\chi(g)\,\eta(\tau)^3$, where $\chi(g)$ is the number of fixed points of $g$ in the $24$-point permutation action.

Two things are asked. (a) *Existence and integrality*: prove such a module exists with **non-negative** multiplicities. (b) *Naturality*: construct $K$ canonically — as the state space of a conformal field theory, a vertex operator superalgebra, or a BPS-state algebra — with $M_{24}$ acting by symmetries, so that the $H_g$ are traces rather than coincidences. Part (a) is a theorem (Gannon, 2016). Part (b) is open; this is the live problem.

## 2. Mathematical Foundations

**The Mathieu group $M_{24}$.** The $5$-transitive permutation group on $24$ points preserving the binary Golay code $\mathcal{G}_{24}\subset \mathbb{F}_2^{24}$, of order
$$|M_{24}| = 244{,}823{,}040 = 2^{10}\cdot 3^3\cdot 5\cdot 7\cdot 11\cdot 23,$$
with $26$ conjugacy classes and $26$ irreducible characters of dimensions $1, 23, 45, \overline{45}, 231, \overline{231}, 252, 253, 483, 770, \overline{770}, 990, \overline{990}, 1035^{(3)}, 1265, 1771, 2024, 2277, 3312, 3520, 5313, 5544, 5796, 10395$.

**Elliptic genus of K3.** A weak Jacobi form of weight $0$ and index $1$, $y=e^{2\pi i z}$, $q=e^{2\pi i \tau}$:
$$Z_{K3}(\tau,z) \;=\; 8\sum_{i=2,3,4}\left(\frac{\theta_i(\tau,z)}{\theta_i(\tau,0)}\right)^{2} \;=\; 2\,\phi_{0,1}(\tau,z),$$
independent of the point in K3 moduli space; $Z_{K3}(\tau,0)=24=\chi(K3)$.

**$\mathcal{N}=4$ decomposition.** In the Ramond sector at $c=6$ there is one BPS (massless) character $\widetilde{\mathrm{ch}}_{1/4,0}$ and a family of massive characters $\widetilde{\mathrm{ch}}_{n+1/4,1/2}(\tau,z) = q^{\,n-1/8}\,\theta_1(\tau,z)^2/\eta(\tau)^3$. Then
$$Z_{K3}(\tau,z) \;=\; 24\,\widetilde{\mathrm{ch}}_{1/4,0}(\tau,z) \;+\; \frac{\theta_1(\tau,z)^2}{\eta(\tau)^3}\; H^{(2)}(\tau),$$
$$H^{(2)}(\tau) \;=\; 2q^{-1/8}\bigl(-1 + 45q + 231q^2 + 770q^3 + 2277q^4 + 5796q^5 + 25760 q^6 + \cdots\bigr).$$

**Mock modularity.** $H^{(2)}$ is not modular; its completion
$$\widehat{H}^{(2)}(\tau) \;=\; H^{(2)}(\tau) \;+\; 24\,(4i)^{-1/2}\!\int_{-\bar\tau}^{i\infty}\frac{\overline{\eta(-\bar w)^{3}}}{(w+\tau)^{1/2}}\,dw$$
transforms as a weight-$1/2$ form on $SL_2(\mathbb{Z})$ (Eguchi–Hikami; Zwegers' theory of mock theta functions). The **shadow** is $24\,\eta(\tau)^3$.

**Twining genera.** For $g\in M_{24}$ with cycle shape $\prod_\ell \ell^{a_\ell}$ on $24$ points, the conjectural equivariant elliptic genus is
$$Z_g(\tau,z) \;=\; \chi(g)\,\widetilde{\mathrm{ch}}_{1/4,0}(\tau,z) \;+\; \frac{\theta_1(\tau,z)^2}{\eta(\tau)^3}\,H_g(\tau),\qquad \chi(g)=a_1,$$
with $H_g$ mock modular of weight $1/2$ on $\Gamma_0(N_g)$ ($N_g=o(g)\cdot h$) and shadow $\chi(g)\eta^3$.

**Umbral moonshine.** Mathieu moonshine is the case $X=A_1^{24}$ of a family indexed by the $23$ Niemeier lattices (even unimodular rank-$24$ lattices with roots); $G^X = \mathrm{Aut}(N^X)/W^X$, and $G^{A_1^{24}} = M_{24}$.

## 3. History & State of the Art (SOTA)

- **1979–1992.** Monstrous moonshine: Conway–Norton conjecture, Frenkel–Lepowsky–Meurman's $V^\natural$, Borcherds' proof. Sets the template: module first, modularity second.
- **1987–2009.** Mukai classifies symplectic automorphism groups of K3 surfaces: each is a subgroup of $M_{23}$ with at least $5$ orbits on $24$ points. Kondō gives a lattice-theoretic proof. No K3 surface has $M_{24}$ symmetry.
- **2010.** Eguchi, Ooguri, Tachikawa, *Notes on the K3 surface and the Mathieu group $M_{24}$* — the observation.
- **2010–2012.** All $H_g$ are computed and their modular data fixed: Cheng ($M_{24}$ and K3 twining, class $2A$ etc.), Gaberdiel–Hohenegger–Volpato (all classes, twice), Eguchi–Hikami. Twenty-six classes give $21$ distinct series (complex-conjugate pairs coincide).
- **2012.** Cheng–Duncan–Harvey: **Umbral Moonshine**, embedding the $M_{24}$ case in a $23$-member family; Rademacher-sum / "optimal growth" characterization fixes each $H_g$ uniquely.
- **2013–2015.** Gaberdiel–Hohenegger–Volpato: symmetry groups of K3 *sigma models* are subgroups of the Conway group $Co_0$ stabilizer data — again never all of $M_{24}$.
- **2015.** Duncan–Griffin–Ono prove the umbral moonshine conjecture (existence of modules) for all $23$ lambencies.
- **2016.** Gannon, *Much ado about Mathieu*: existence **and uniqueness** of the $M_{24}$-module with non-negative multiplicities, by an effective bound plus finite computation.

## 4. Partial Results / Verified Cases

- **Existence/integrality: proved.** Gannon (2016) shows the virtual $M_{24}$-modules $K_n$ defined by the $21$ series $H_g$ have non-negative integer multiplicities for **all** $n\ge 1$, with uniqueness. Method: multiplicities are non-negative for $n \le n_0$ by direct computation, and an asymptotic estimate on the Rademacher expansion handles $n > n_0$.
- **Modularity: proved.** Each of the $21$ distinct $H_g$ is a mock modular form of weight $1/2$ on $\Gamma_0(N_g)$ with shadow $\chi(g)\eta^3$ and pole $-2q^{-1/8}$; uniqueness follows from the optimal-growth (polar-part-only) condition of Cheng–Duncan–Harvey.
- **Naturality, partial.** Symmetry surfing (Taormina–Wendland, 2011–2017): the Kummer surface $\mathbb{T}^4/\mathbb{Z}_2$ family carries a combined action of the group $\mathbb{Z}_2^4\!:\!A_8$ of order $\,2^4\cdot 20160 = 322560$, a maximal subgroup of $M_{24}$, obtained by "surfing" symmetries across a moduli subspace rather than fixing one point. This realizes a subgroup of index $759$ in $M_{24}$, not $M_{24}$.
- **Twining genera from geometry.** Duncan–Mack-Crane (2016) realize twined elliptic genera of K3 sigma models via the Conway moonshine module $V^{s\natural}$ and derived equivalences, recovering many $H_g$ for $g$ in $Co_0$-stabilizers.
- **Small classes.** For $g$ of order $1,2,3,4$ the $H_g$ agree with geometric equivariant elliptic genera of explicit K3 automorphisms; for orders $11, 23$ the series were the last to be pinned down (Gaberdiel–Hohenegger–Volpato; Eguchi–Hikami), since $23A/23B$ have $\chi(g)=1$ and require care with multiplier systems.

## 5. Principal Obstacles

- **Mukai's theorem is a hard no-go.** Any finite symplectic automorphism group of a K3 surface embeds in $M_{23}$ with $\ge 5$ orbits on $24$ points. So no single K3 surface, and (by Gaberdiel–Hohenegger–Volpato) no single K3 sigma model, has $M_{24}$ acting. The would-be module cannot be the state space of one CFT with the obvious action.
- **Moduli-space non-locality.** Symmetry surfing needs symmetries at *different* points of a $80$-dimensional moduli space to be identified. There is no established categorical or geometric framework in which such identifications compose associatively into a group action on a fixed vector space; only $\mathbb{Z}_2^4\!:\!A_8$ has been assembled this way.
- **Mock modularity has no VOA calculus.** Borcherds' proof of monstrous moonshine used a genuine VOA and a Borcherds–Kac–Moody algebra with a clean denominator identity. Here the characters are mock: the shadow contributes a non-holomorphic completion, so the naive "trace on a graded vector space" is obstructed by the massless/BPS sector, whose contribution jumps across walls. Wall-crossing, not holomorphy, controls the $q$-expansion.
- **Gannon's proof is non-constructive.** It certifies non-negativity via Rademacher asymptotics and a finite check; it produces no operators, no algebra structure, no explanation of *why* $M_{24}$ rather than some other group with the same character degrees.
- **Umbral moonshine multiplies the mystery.** The $23$ Niemeier cases must be explained uniformly; any construction special to $A_1^{24}$ is suspect.

## 6. The Gap

Proved: a unique $\mathbb{Z}$-graded $M_{24}$-module $K$ with non-negative multiplicities whose graded traces are the $21$ mock modular forms $H_g$.

Wanted: a canonical algebraic object $\mathcal{A}$ — a vertex operator superalgebra, a BPS-state algebra of a type II compactification on $K3\times T^2$, or a suitable category of sheaves — carrying a genuine $M_{24}$-action, together with a proof that its $\mathcal{N}=4$-graded character equals $H^{(2)}$.

The precise barrier: bridge Mukai's obstruction. Either (i) show a single object with full $M_{24}$ symmetry exists in a category *broader* than K3 sigma models (a non-geometric or asymmetric orbifold, a $\mathbb{Z}_2$-orbifold at a special point of moduli space), or (ii) make "symmetry surfing" into a theorem: construct a canonical vector space glued from the moduli space on which the surfed symmetries close into $M_{24}$, extending $\mathbb{Z}_2^4\!:\!A_8$ by the missing index-$759$ data.

## 7. Current Research (as of June 2026)

- **BPS-algebra origin.** Paquette, Persson, Volpato (*Monstrous BPS algebras and the superstring origin of moonshine*, 2016; sequel 2017) derive monstrous moonshine from heterotic strings on the Frenkel–Lepowsky–Meurman orbifold. Adapting this to $K3\times T^2$ and $M_{24}$ remains the most-pursued route. *(frontier — verify)*
- **Symmetry surfing beyond $\mathbb{Z}_2^4\!:\!A_8$.** Taormina–Wendland and collaborators continue to extend the surfed group and to lift the construction to the level of states rather than only the elliptic genus.
- **Derived/categorical symmetries.** Following Huybrechts' classification of derived-autoequivalence symmetry groups of K3 categories and Duncan–Mack-Crane's Conway-module methods, several groups study whether $\mathrm{D}^b(K3)$ with stability conditions gives room for $M_{24}$.
- **Optimal growth and Rademacher sums.** Cheng–Duncan's holographic/Rademacher characterization is being pushed toward a uniform, group-theory-free axiomatization of "moonshine".
- **Institutions/people.** John Duncan (Academia Sinica/Emory), Miranda Cheng (Amsterdam/Academia Sinica), Terry Gannon (Alberta), Matthias Gaberdiel (ETH Zürich), Roberto Volpato (Padova), Anne Taormina (Durham), Katrin Wendland (Trieste/SISSA), Sarah Harrison, Natalie Paquette, Shamit Kachru (Stanford).

## 8. Future Work

- Construct the $M_{24}$-module as the BPS-state space of a compactification, with the mock modularity coming from the known wall-crossing of $\tfrac14$-BPS counting functions (Dabholkar–Murthy–Zagier framework).
- Prove a "surfing" theorem: define a canonical gluing of Hilbert spaces over a connected subvariety of K3 moduli space and show its automorphisms contain $M_{24}$.
- Find a Borcherds–Kac–Moody superalgebra whose denominator identity reproduces the $H_g$ uniformly across the $23$ umbral cases; the Siegel-form lifts $\Phi_g$ of Gritsenko–Nikulin type are the natural candidates.
- Explain the *uniformity* of umbral moonshine directly from the Niemeier lattices, e.g. by a lattice VOA construction whose $\mathcal{N}=4$ decomposition is forced by the root system $X$.
- Extend to the enumerated "moonshine for $O'N$, Thompson, $M_{23}$" families and test whether any proposed mechanism survives them.

## 9. Key References

- **[Foundational]** T. Eguchi, H. Ooguri, Y. Tachikawa. *Notes on the K3 Surface and the Mathieu Group $M_{24}$.* Experimental Mathematics 20 (2011), 91–96. [DOI](https://doi.org/10.1080/10586458.2011.544585)
- **[Foundational]** S. Mukai. *Finite groups of automorphisms of K3 surfaces and the Mathieu group.* Inventiones Mathematicae 94 (1988), 183–221. [DOI](https://doi.org/10.1007/bf01394352)
- **[Foundational]** S. Zwegers. *Mock Theta Functions.* PhD thesis, Utrecht University, 2002.
- **[Twining genera]** M. R. Gaberdiel, S. Hohenegger, R. Volpato. *Mathieu twining characters for K3.* JHEP 2010(9):058; and *Mathieu Moonshine in the elliptic genus of K3.* JHEP 2010(10):062. [DOI](https://doi.org/10.1007/jhep09(2010)058)
- **[Twining genera]** M. C. N. Cheng. *K3 Surfaces, $N=4$ Dyons, and the Mathieu Group $M_{24}$.* Communications in Number Theory and Physics 4 (2010), 623–657. [DOI](https://doi.org/10.4310/cntp.2010.v4.n4.a2)
- **[SOTA]** T. Gannon. *Much ado about Mathieu.* Advances in Mathematics 301 (2016), 322–358. [DOI](https://doi.org/10.1016/j.aim.2016.06.014)
- **[SOTA]** J. F. R. Duncan, M. J. Griffin, K. Ono. *Proof of the Umbral Moonshine Conjecture.* Research in the Mathematical Sciences 2 (2015), article 26. [DOI](https://doi.org/10.1186/s40687-015-0044-7)
- **[Framework]** M. C. N. Cheng, J. F. R. Duncan, J. A. Harvey. *Umbral Moonshine.* Communications in Number Theory and Physics 8 (2014), 101–242. [DOI](https://doi.org/10.4310/cntp.2014.v8.n2.a1)
- **[Symmetry surfing]** A. Taormina, K. Wendland. *The overarching finite symmetry group of Kummer surfaces in the Mathieu group $M_{24}$.* JHEP 2013(8):125. [DOI](https://doi.org/10.1007/jhep08(2013)125)
- **[K3 sigma models]** M. R. Gaberdiel, S. Hohenegger, R. Volpato. *Symmetries of K3 sigma models.* Communications in Number Theory and Physics 6 (2012), 1–50. [DOI](https://doi.org/10.4310/cntp.2012.v6.n1.a1)
- **[Conway module]** J. F. R. Duncan, S. Mack-Crane. *Derived Equivalences of K3 Surfaces and Twined Elliptic Genera.* Research in the Mathematical Sciences 3 (2016), article 1. [DOI](https://doi.org/10.1186/s40687-015-0050-9)
- **[Survey]** J. F. R. Duncan, M. J. Griffin, K. Ono. *Moonshine.* Research in the Mathematical Sciences 2 (2015), article 11.
- **[Survey]** V. Anagiannis, M. C. N. Cheng. *TASI Lectures on Moonshine.* Proceedings of Science, TASI2017 (2018), 010. [DOI](https://doi.org/10.22323/1.305.0010)
- **[Physics origin]** N. M. Paquette, D. Persson, R. Volpato. *Monstrous BPS-algebras and the superstring origin of moonshine.* Communications in Number Theory and Physics 10 (2016), 433–526. [DOI](https://doi.org/10.4310/cntp.2016.v10.n3.a2)

## 10. Worked Example / Concrete Special Case

**Step 1: extract $A_1$.** The weak Jacobi form $\phi_{0,1}$ has expansion
$$\phi_{0,1}(\tau,z) = (y + 10 + y^{-1}) + q\,(10y^{2} - 64y + 108 - 64y^{-1} + 10y^{-2}) + O(q^{2}).$$
So $Z_{K3}=2\phi_{0,1}$ has $q^0$-part $2y+20+2y^{-1}$ and $q^1$-part $20y^2-128y+216-128y^{-1}+20y^{-2}$. Setting $y=1$ in the full series gives $24$, the Euler characteristic.

**Step 2: subtract the BPS piece.** The massless character contributes $24\,\widetilde{\mathrm{ch}}_{1/4,0}$, and the massive tower contributes $\frac{\theta_1(\tau,z)^2}{\eta(\tau)^3}\,H^{(2)}(\tau)$ with
$$\frac{\theta_1(\tau,z)^2}{\eta(\tau)^3} = q^{1/8}\bigl(y - 2 + y^{-1}\bigr)\bigl(1 + O(q)\bigr).$$
Writing $H^{(2)} = q^{-1/8}(-2 + A_1 q + \cdots)$ and matching the coefficient of $q\,y$ in $Z_{K3}$ (which is $-128$) after accounting for the $-2q^{-1/8}$ polar term feeding into $q^{1}$ through the $O(q)$ tail of $\theta_1^2/\eta^3$, one finds $A_1 = 90$.

**Step 3: recognize the group.** $90 = 45 + 45$, and $M_{24}$ has exactly two $45$-dimensional irreducibles, complex conjugates of each other. Hence $K_1 \cong \mathbf{45}\oplus\overline{\mathbf{45}}$ — the only decomposition consistent with $\operatorname{tr}(g\mid K_1)\in\mathbb{Z}$ for all $g$, since $\chi_{45}$ takes values in $\mathbb{Z}[\sqrt{-7}]$ and only the sum with its conjugate is rational.

**Step 4: a twining check.** Take $g$ in class $2A$, cycle shape $1^{8}2^{8}$, so $\chi(g)=8$. Predicted shadow: $8\,\eta(\tau)^3$. Predicted $q^{7/8}$-coefficient of $H_{2A}$:
$$\operatorname{tr}(2A \mid K_1) = \chi_{45}(2A) + \chi_{\overline{45}}(2A) = (-3) + (-3) = -6 .$$
Independently, $H_{2A}$ is fixed by being the unique weight-$1/2$ mock modular form on $\Gamma_0(2)$ with shadow $8\eta^3$, polar term $-2q^{-1/8}$, and no other poles at cusps (optimal growth). Its computed $q$-expansion begins $2q^{-1/8}(-1 - 3q + \cdots)$ — matching the character-theoretic prediction. Repeating this for all $21$ distinct classes is exactly the consistency check that Gaberdiel–Hohenegger–Volpato completed, and that Gannon upgraded to a proof of module existence.

The point of the open problem is that every line above is a *verification*. Nothing in Steps 1–2 mentions $M_{24}$; the group enters only in Step 3, by inspection of a character table. No known construction puts $M_{24}$ into Step 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*