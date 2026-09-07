---
id: 02-algebra-group-theory/isomorphism-problem-for-group-rings
title: "Isomorphism Problem for Group Rings"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Isomorphism Problem for Group Rings

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/isomorphism-problem-for-group-rings` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $R$ be a commutative ring and $G$ a finite group. The **isomorphism problem** (ISO) asks:

> Does $RG \cong RH$ as $R$-algebras imply $G \cong H$?

Three specializations carry the weight of the subject:

- **(ISO-$\mathbb{Z}$)** $R = \mathbb{Z}$. **Resolved negatively** by Hertweck (2001): there exist non-isomorphic finite solvable groups $G, H$ of order $2^{21}\cdot 97^{28}$ with $\mathbb{Z}G \cong \mathbb{Z}H$.
- **(MIP)** The **modular isomorphism problem**: $R = \mathbb{F}_p$, $G$ and $H$ finite $p$-groups, $\mathbb{F}_pG \cong \mathbb{F}_pH \Rightarrow G \cong H$? **Resolved negatively for $p=2$** by García-Lucas, Margolis and del Río (2022), with $|G| = |H| = 2^9$. **Open for every odd prime $p$**, and open over $R = \mathbb{Z}_p$ (the $p$-adics) even for $p = 2$.
- **(ISO for classes)** For which classes $\mathcal{C}$ of finite groups is $G$ determined by $\mathbb{Z}G$ (or $\mathbb{F}_pG$) within $\mathcal{C}$?

A complete resolution of MIP for odd $p$ requires either a proof that $\mathbb{F}_pG \cong \mathbb{F}_pH$ forces $G \cong H$ for all finite $p$-groups, or an explicit non-isomorphic pair with isomorphic group algebras. The problem's status is "partially-solved": settled negatively in two central cases, still open in the modular odd-$p$ case and in most refined class-restricted forms.

## 2. Mathematical Foundations

For a group $G$ and commutative ring $R$, the **group ring** is the free $R$-module on $G$,
$$RG = \Big\{ \textstyle\sum_{g \in G} a_g\, g \;:\; a_g \in R \Big\}, \qquad \Big(\sum a_g g\Big)\Big(\sum b_h h\Big) = \sum_{g,h} a_g b_h\, (gh).$$

The **augmentation map** $\varepsilon : RG \to R$, $\varepsilon(\sum a_g g) = \sum a_g$, is a ring homomorphism; its kernel $I(RG)$ is the **augmentation ideal**, $R$-free on $\{g - 1 : g \neq 1\}$. The **normalized units** are $V(RG) = \{u \in U(RG) : \varepsilon(u) = 1\}$.

A subgroup $B \leq V(RG)$ is a **group basis** if $B$ is an $R$-basis of $RG$; equivalently $RG \cong RB$ by an augmentation-preserving map. Every algebra isomorphism $RG \to RH$ may be normalized to preserve augmentation when $R = \mathbb{Z}$ or $R$ is a field, so ISO is equivalent to: *all group bases of $RG$ are isomorphic to $G$.*

Key structural facts the problem rests on:

- **(Higman / Perlis–Walker)** For finite abelian $G,H$: $\mathbb{Q}G \cong \mathbb{Q}H \iff G \cong H$; a fortiori for $\mathbb{Z}$.
- **(Jennings)** For $|G| = p^n$, $\mathbb{F}_pG$ is local with maximal ideal $I = I(\mathbb{F}_pG)$ nilpotent, and the **dimension subgroups** $D_n(G) = G \cap (1 + I^n)$ satisfy $D_n(G) = \prod_{i p^j \geq n} \gamma_i(G)^{p^j}$. Since the $I$-adic filtration is intrinsic to the algebra, the sequence $\dim_{\mathbb{F}_p} I^n/I^{n+1}$ and all quotients $D_n(G)/D_{n+1}(G)$ are **isomorphism invariants** of $\mathbb{F}_pG$.
- **(Zassenhaus conjectures)** ZC1: every torsion unit of $V(\mathbb{Z}G)$ is conjugate in $\mathbb{Q}G$ to an element of $G$. ZC3 (the strongest, "$\mathrm{Aut}$" form): any group basis $H \leq V(\mathbb{Z}G)$ satisfies $H = u^{-1}Gu$ for some $u \in U(\mathbb{Q}G)$. ZC3 $\Rightarrow$ ISO-$\mathbb{Z}$.
- **(Normalizer problem, Nor)** $N_{V(\mathbb{Z}G)}(G) = G \cdot Z(V(\mathbb{Z}G))$? A counterexample to Nor is the engine of Hertweck's ISO counterexample.

Invariants of $\mathbb{Z}G$ known to determine group-theoretic data: $|G|$, $G/G'$, $Z(G)$, the character table of $G$ together with power maps (Saksonov), and the multiset of composition factors (Kimmerle–Lyons–Sandling–Teague).

## 3. History & State of the Art (SOTA)

- **1940.** Higman's thesis and *The units of group-rings* solve the abelian case over $\mathbb{Z}$ and initiate the systematic study of $U(\mathbb{Z}G)$.
- **1950.** Perlis–Walker: finite abelian groups are determined by $\mathbb{Q}G$.
- **1956–1965.** Deskins settles MIP for abelian $p$-groups; Passman for groups of order $p^4$.
- **1968.** Whitcomb (Chicago thesis): ISO-$\mathbb{Z}$ holds for finite metabelian groups.
- **1971.** Dade constructs non-isomorphic finite groups $G, H$ with $KG \cong KH$ for **every** field $K$ — killing the field version of ISO outright and isolating $\mathbb{Z}$ and $\mathbb{F}_p$ (for $p$-groups) as the meaningful cases.
- **1987–1988.** Roggenkamp–Scott prove ISO-$\mathbb{Z}$ for finite **nilpotent** groups, using $p$-adic methods; Weiss's rigidity theorem for $p$-permutation modules over $\mathbb{Z}_p$ gives a conceptual proof.
- **2001.** Hertweck's *Annals* paper: counterexample to ISO-$\mathbb{Z}$, order $2^{21}\cdot 97^{28}$, built from a metabelian counterexample to the normalizer problem.
- **2011.** Eick–Konovalov attack MIP for all $267$ groups of order $512$ computationally, resolving most but leaving a residue of undecided pairs.
- **2018.** Eisele–Margolis disprove ZC1 with a metabelian counterexample, removing the most-used route to ISO-$\mathbb{Z}$ for solvable groups.
- **2022.** García-Lucas–Margolis–del Río produce non-isomorphic $2$-groups of order $2^9$ with isomorphic $\mathbb{F}_2$-group algebras, from exactly the residue Eick–Konovalov left open.

## 4. Partial Results / Verified Cases

Positive over $\mathbb{Z}$:
- Finite **abelian** groups (Higman 1940); finite **metabelian** groups (Whitcomb 1968); finite **nilpotent** groups (Roggenkamp–Scott 1987; Weiss 1988).
- Groups with a normal Sylow $p$-subgroup and abelian complement; **Frobenius** groups; **simple** groups (via Kimmerle–Lyons–Sandling–Teague, using Artin's theorem on orders of simple groups).
- $\mathbb{Z}G$ determines $|G|$, $G/G'$, $Z(G)$, the character table with power maps, the composition factors, and the order of every element's centralizer.

Positive for MIP ($R = \mathbb{F}_p$, $G$ a $p$-group):
- $|G| \le p^4$ (Passman 1965); $|G| = p^5$ (Salim–Sandling 1996); $|G| = 2^6, 2^7, 2^8$ computationally (Eick 2008; Eick–Konovalov 2011).
- **Abelian** $p$-groups (Deskins 1956); **metacyclic** $p$-groups (Bagiński 1988 for $p$ odd; Sandling for $p=2$); $p$-groups of **class 2 with elementary abelian commutator subgroup** and central-elementary-by-abelian groups (Sandling 1989); $p$-groups of **maximal class** of order $\le p^{p+1}$.
- Invariants always determined: $|G|$, $G/G'$, the Jennings quotients $D_n(G)/D_{n+1}(G)$, the Loewy series of $\mathbb{F}_pG$, $|Z(G)|$, the isomorphism type of $G/\gamma_3(G)G^{p}$.

Negative:
- **Fields, general groups:** Dade 1971, for all fields simultaneously.
- **$R = \mathbb{Z}$:** Hertweck 2001, $|G| = |H| = 2^{21}\cdot 97^{28}$, $G \not\cong H$, $\mathbb{Z}G \cong \mathbb{Z}H$.
- **MIP, $p = 2$:** García-Lucas–Margolis–del Río 2022, $|G| = |H| = 2^9 = 512$, class $3$; further families in higher $2$-power orders.

## 5. Principal Obstacles

- **Loss of ZC1.** Almost every positive result over $\mathbb{Z}$ ultimately proves a rigidity statement — group bases are conjugate in $\mathbb{Q}G$ — rather than mere isomorphism. Eisele–Margolis (2018) show that this statement is false in general, even for metabelian groups. There is now no known general mechanism forcing a group basis into the "expected" position.
- **Weiss rigidity does not survive mixed order.** Weiss's theorem is about $\mathbb{Z}_p$-lattices with $p$-group action: a $\mathbb{Z}_p G$-lattice that is a permutation module on restriction to a normal $p$-subgroup is a permutation module. It gives nilpotent groups. For groups with more than one prime divisor, the local pieces $\mathbb{Z}_p G$ over different $p$ do not glue: the genus of $\mathbb{Z}G$ is not determined by its localizations in a way that controls group bases.
- **Semilocal $\to$ global gap.** $\mathbb{Z}G \cong \mathbb{Z}H$ can hold while all constructions of an explicit isomorphism live in $\mathbb{Z}_{(p)}G$; the obstruction lies in a locally free class group / Picard-group computation that current techniques cannot make effective.
- **MIP for odd $p$: the invariants run out.** The Jennings filtration, Loewy structure, and Külshammer ideals all detect only quotients of $G$ by terms of the lower central and $p$-power series. For $p$ odd, $\mathbb{F}_pG$ determines $G/\gamma_3(G)G^{p}$ and much of the class-2 structure; nothing in the current toolbox reaches into class $\ge 3$ for large $p$. Conversely, the $p=2$ counterexamples exploit that $x \mapsto x^2$ has a special (semilinear, additive modulo commutators) behaviour in characteristic $2$; the construction does not transpose to odd $p$, where $x \mapsto x^p$ is much less rigid but also much less usable for building isomorphisms.
- **Computational blow-up.** Deciding $\mathbb{F}_pG \cong \mathbb{F}_pH$ is an algebra-isomorphism test in dimension $p^n$; even with Eick's automorphism-group algorithm and Margolis–Moede's improvements, the search space grows like $p^{n^2/4}$, so exhaustive verification stalls near $2^{10}$, $3^7$, $5^6$.

## 6. The Gap

The remaining open core is:

> Do there exist non-isomorphic finite $p$-groups $G, H$ with $p$ **odd** and $\mathbb{F}_pG \cong \mathbb{F}_pH$?

Proven (Section 4): the answer is *no* for $|G| \le p^5$, for abelian, metacyclic, class-2-with-elementary-abelian-derived-subgroup, and maximal-class-of-order-$\le p^{p+1}$ groups. Known (Section 4): the answer is *yes* for $p=2$ at order $2^9$.

The precise barrier: all positive odd-$p$ results proceed by reconstructing $G$ from *canonical filtration quotients* of $\mathbb{F}_pG$ (Jennings, Külshammer, the $p$-th power map on $I/I^2$). These quotients determine $G$ only up to nilpotency class $2$ plus small corrections. The step to be crossed is either (a) a construction of a canonical map $\mathbb{F}_pG \to G$-data reaching class $\ge 3$ for odd $p$, or (b) a class-3 pair of odd-order groups whose group algebras are shown isomorphic by an explicit filtered isomorphism — the odd analogue of the $2$-group "obelisk" families. A second, quite separate gap: MIP over $\mathbb{Z}_p$ for $p$-groups remains open even at $p = 2$, because the $2^9$ counterexample is genuinely characteristic-$2$ and lifts no further.

## 7. Current Research (as of June 2026)

- **Murcia / Vrije Universiteit Brussel school** (Á. del Río, D. García-Lucas, L. Margolis). After the $2^9$ counterexamples, the programme is to map exactly which classes still satisfy MIP: results for $p$-groups of class $3$, "obelisks", and $2$-generated groups. Their conclusion — MIP survives in strong form for class $\le 2$ and small rank — is the current consensus.
- **Braunschweig / computational algebra** (B. Eick, T. Moede). Revised algorithms for testing $\mathbb{F}_pG \cong \mathbb{F}_pH$ using the associated graded Lie ring; verification pushed to further small orders for $p = 3, 5, 7$. *(frontier — verify)* Reports of complete verification at order $3^7$ should be checked against the published tables.
- **Stuttgart** (W. Kimmerle and collaborators). The **prime graph question**: does $V(\mathbb{Z}G)$ have the same prime graph as $G$? Confirmed for solvable groups and for all almost simple groups whose order has few prime divisors; treated as the strongest surviving form of the "$\mathbb{Z}G$ knows $G$" philosophy after ZC1 fell.
- **Post-ZC1 rigidity.** Work on the "HeLP" (Hertweck–Luthar–Passi) method and on lattice-theoretic reformulations, asking which weakened Zassenhaus statements are still true (e.g. ZC1 for solvable groups of derived length $\le 2$ with restricted Sylow structure).

## 8. Future Work

- Search systematically for odd-$p$ MIP counterexamples among class-$3$ groups of order $p^6$–$p^7$ with the same Jennings and Külshammer data — the exact profile that produced the $2^9$ examples.
- Develop invariants of $\mathbb{F}_pG$ beyond the Jennings filtration: Külshammer ideals $T_n(\mathbb{F}_pG)^\perp$, Hochschild cohomology, and the Lie structure of $I/I^2$ under the $p$-power map, and determine whether their joint value characterizes $G$ for $p$ odd.
- Settle MIP over $\mathbb{Z}_p$ for $p$-groups; this is the natural home of Weiss rigidity and the version most likely to be positive.
- Determine the minimal order of an ISO-$\mathbb{Z}$ counterexample. Hertweck's is astronomically large; nothing rules out one of moderate order, and none is known below it.
- Classify the classes of finite groups for which ISO-$\mathbb{Z}$ still holds beyond nilpotent — in particular supersolvable groups and groups with abelian Sylow subgroups.

## 9. Key References

- **[Foundational]** G. Higman. *The units of group-rings.* Proceedings of the London Mathematical Society (2) **46** (1940), 231–248.
- **[Foundational]** S. Perlis and G. L. Walker. *Abelian group algebras of finite order.* Transactions of the American Mathematical Society **68** (1950), 420–426.
- **[Foundational]** W. E. Deskins. *Finite abelian groups with isomorphic group algebras.* Duke Mathematical Journal **23** (1956), 35–40.
- **[Foundational]** D. S. Passman. *The group algebras of groups of order $p^4$ over a modular field.* Michigan Mathematical Journal **12** (1965), 405–415.
- **[Foundational]** E. C. Dade. *Deux groupes finis distincts ayant la même algèbre de groupe sur tout corps.* Mathematische Zeitschrift **119** (1971), 345–348.
- **[Foundational]** K. W. Roggenkamp and L. L. Scott. *Isomorphisms of $p$-adic group rings.* Annals of Mathematics (2) **126** (1987), 593–647.
- **[Foundational]** A. Weiss. *Rigidity of $p$-adic $p$-torsion.* Annals of Mathematics (2) **127** (1988), 317–332.
- **[SOTA]** M. Hertweck. *A counterexample to the isomorphism problem for integral group rings.* Annals of Mathematics (2) **154** (2001), 115–138.
- **[SOTA]** F. Eisele and L. Margolis. *A counterexample to the first Zassenhaus conjecture.* Advances in Mathematics **339** (2018), 599–641.
- **[SOTA]** D. García-Lucas, L. Margolis and Á. del Río. *Non-isomorphic 2-groups with isomorphic modular group algebras.* Journal für die reine und angewandte Mathematik (Crelle) **783** (2022), 269–274.
- **[SOTA]** B. Eick. *Computing automorphism groups and testing isomorphisms for modular group algebras.* Journal of Algebra **320** (2008), 3895–3910.
- **[SOTA]** B. Eick and A. Konovalov. *The modular isomorphism problem for the groups of order 512.* In *Groups St Andrews 2009*, LMS Lecture Note Series **388**, Cambridge University Press (2011), 375–383.
- **[Partial results]** C. Bagiński. *The isomorphism question for modular group algebras of metacyclic $p$-groups.* Proceedings of the American Mathematical Society **104** (1988), 39–42.
- **[Partial results]** R. Sandling. *The modular group algebra of a central-elementary-by-abelian $p$-group.* Archiv der Mathematik **52** (1989), 22–27.
- **[Partial results]** M. A. M. Salim and R. Sandling. *The modular group algebra problem for groups of order $p^5$.* Journal of the Australian Mathematical Society (Series A) **61** (1996), 229–237.
- **[Partial results]** W. Kimmerle, R. Lyons, R. Sandling and D. N. Teague. *Composition factors from the group ring and Artin's theorem on orders of simple groups.* Proceedings of the London Mathematical Society (3) **60** (1990), 89–122.
- **[Survey]** R. Sandling. *The isomorphism problem for group rings: a survey.* In *Orders and Their Applications*, Lecture Notes in Mathematics **1142**, Springer (1985), 256–288.
- **[Survey]** S. K. Sehgal. *Units in Integral Group Rings.* Longman Scientific & Technical, 1993.
- **[Survey]** L. Margolis and Á. del Río. *Finite subgroups of group rings: a survey.* Advances in Group Theory and Applications **8** (2019), 1–37.

## 10. Worked Example / Concrete Special Case

**Claim.** $\mathbb{F}_2 D_8 \not\cong \mathbb{F}_2 Q_8$, so MIP holds at order $8$ — even though the two algebras agree on every filtration invariant.

Both groups have $G/G' \cong C_2 \times C_2$, $Z(G) = G' = \Phi(G) \cong C_2$, and identical Jennings series $D_1 = G \supset D_2 = Z(G) \supset D_3 = 1$; hence identical Loewy series $\dim I^n/I^{n+1} = 1,2,2,2,1$ for $n = 0,\dots,4$. A finer invariant is needed: the number of $b \in \mathbb{F}_2G$ with $b^2 = 0$ (equivalently, since $(1+b)^2 = 1+b^2$ in characteristic $2$, the number of $u \in V(\mathbb{F}_2G)$ with $u^2 = 1$).

Write $D_8 = \langle r,s \mid r^4 = s^2 = 1,\ srs = r^{-1}\rangle$ and $Q_8 = \langle x,y \mid x^4 = 1,\ y^2 = x^2 =: z,\ yxy^{-1} = x^{-1}\rangle$. In both, split $b = c + d$ with $c = \sum_{i} c_i r^i$ on the cyclic part and $d = \sum_j d_j\, r^j s$ on the coset. Over $\mathbb{F}_2$:

$$b^2 = c^2 + (cd + dc) + d^2 .$$

**The three pieces.**
1. $c^2 = (c_0 + c_2)\cdot 1 + (c_1 + c_3)\, z$ in both groups, since $r^2 = x^2 = z$.
2. $cd + dc$ has coefficient at $r^k s$ equal to $\sum_i c_i (d_{k-i} + d_{k+i}) = (c_1 + c_3)(d_{k-1} + d_{k+1})$ (the $i = 0, 2$ terms cancel). The coset multiplication rules agree in the two groups, so this term is identical. It vanishes iff
$$c_1 + c_3 = 0 \quad\text{or}\quad (d_0 = d_2 \text{ and } d_1 = d_3).$$
3. The squares differ. In $D_8$: $(r^is)^2 = 1$ and $(r^is)(r^js) = r^{i-j}$, giving
$$d^2_{D} = \varepsilon\cdot 1 + \mu\,(r + r^3), \qquad \varepsilon = \textstyle\sum_j d_j,\quad \mu = (d_0+d_2)(d_1+d_3).$$
In $Q_8$: $(x^iy)^2 = z$ and $(x^iy)(x^jy) = x^{i-j}z$, so $d^2_{Q} = z\, d^2_{D} = \varepsilon z + \mu (x + x^3)$ (using $z(x+x^3) = x^3 + x$).

**Solving $b^2 = 0$.** The cyclic and coset parts vanish separately.

*$D_8$:* coefficients of $1, z, \{r,r^3\}$ give $c_0 + c_2 = \varepsilon$, $c_1 + c_3 = 0$, $\mu = 0$; then condition 2 is automatic. Count: $d$ with $\mu = 0$ means $(d_0+d_2, d_1+d_3) \neq (1,1)$, i.e. $12$ of $16$ vectors; for each, $(c_1,c_3)$ has $2$ choices and $(c_0,c_2)$ has $2$. Total $12 \times 4 = \mathbf{48}$.

*$Q_8$:* coefficients give $c_0 + c_2 = 0$, $c_1 + c_3 = \varepsilon$, $\mu = 0$. If $\varepsilon = 1$ then $c_1 + c_3 = 1$, so condition 2 forces $d_0 = d_2$, $d_1 = d_3$, which makes $\varepsilon = 0$ — contradiction. So $\varepsilon = 0$; then $d_0+d_2 = d_1+d_3$, and $\mu = 0$ forces both to be $0$, leaving $4$ vectors $d$; for each, $4$ choices of $c$. Total $4 \times 4 = \mathbf{16}$.

$48 \neq 16$, so the algebras are not isomorphic. Note that every such $b$ is nilpotent, hence $\varepsilon(b) = 0$: the counts are counts inside $I$, and $V(\mathbb{F}_2D_8)$ has $47$ involutions against $15$ in $V(\mathbb{F}_2Q_8)$, out of $|V| = 2^7 = 128$ in both.

**What the example shows.** The distinguishing datum is the *squaring map on the whole algebra*, not any quotient of the Jennings filtration. At order $2^9$ García-Lucas–Margolis–del Río exhibit pairs where even this fails: every such square-counting and Külshammer invariant coincides, and an explicit filtered algebra isomorphism exists while the groups do not match. For odd $p$ no analogous construction is known, which is exactly the content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*