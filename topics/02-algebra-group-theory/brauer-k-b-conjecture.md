---
id: 02-algebra-group-theory/brauer-k-b-conjecture
title: "Brauer's k(B) Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Brauer's k(B) Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/brauer-k-b-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite group, $p$ a prime, and $B$ a $p$-block of $G$ with defect group $D$. Let $k(B)$ denote the number of ordinary irreducible characters of $G$ belonging to $B$.

**Conjecture (Brauer, 1956).** $k(B) \le |D|$.

This is Problem 20 in Brauer's 1963 problem list. A complete proof must cover every finite group, every prime, and every block; a disproof requires one explicit $(G,p,B)$ with $k(B) > |D|$. The bound is sharp: it is attained, for instance, whenever $D$ is abelian and $B$ is a nilpotent block, since then $k(B) = k(D) = |D|$.

Two companion statements are usually tracked alongside it: the **$k(B)$-conjecture with an exponent refinement** $k(B) \le |D|$ combined with $k_0(B) \le |D:D'|$ (Olsson's conjecture, where $k_0(B)$ counts height-zero characters), and the **lower bound** $k(B) \ge$ (a function of the sectional rank of $D$) studied by Malle–Robinson. Only the upper bound $k(B)\le |D|$ is the subject of this page.

## 2. Mathematical Foundations

Let $\mathcal{O}$ be a complete discrete valuation ring with residue field $F$ of characteristic $p$ and field of fractions $K$ of characteristic $0$, chosen large enough (a splitting $p$-modular system). The group algebra decomposes into indecomposable two-sided ideals,
$$\mathcal{O}G = B_1 \oplus B_2 \oplus \cdots \oplus B_n ,$$
and each $B_i$ is a **block**. Equivalently, blocks correspond to the primitive idempotents $e_i$ of $Z(\mathcal{O}G)$, and every $\chi \in \operatorname{Irr}(G)$ lies in exactly one block. Write
$$k(B) = |\operatorname{Irr}(B)|, \qquad l(B) = |\operatorname{IBr}(B)| .$$

**Defect group.** $D \le G$ is a defect group of $B$ if $D$ is minimal such that $B$ is a direct summand of $\operatorname{Ind}_{D\times D}^{G\times G}$ of a $\mathcal{O}[D\times D]$-module; equivalently, $D$ is a vertex of $B$ as an $\mathcal{O}[G\times G]$-module. $D$ is a $p$-subgroup, unique up to $G$-conjugacy, and $|D| = p^d$ where $d$ is the **defect** of $B$. Defect controls heights: for $\chi\in\operatorname{Irr}(B)$,
$$\nu_p(\chi(1)) = \nu_p(|G|) - d + h(\chi), \qquad h(\chi)\in\mathbb{Z}_{\ge 0},$$
with $h(\chi)$ the **height**.

**Brauer's contribution/orthogonality machinery.** For $\chi,\psi\in\operatorname{Irr}(B)$ and a $p$-element $u$ with $C = C_G(u)$, the generalised decomposition numbers $d^{u}_{\chi\varphi}$ ($\varphi\in\operatorname{IBr}(b)$, $b$ a block of $C$ with $b^G=B$) satisfy
$$\chi(us) = \sum_{\varphi\in\operatorname{IBr}(b)} d^{u}_{\chi\varphi}\,\varphi(s) \quad (s \in C \text{ } p\text{-regular}),$$
and Brauer's second main theorem gives the **$p$-section decomposition**
$$k(B) = \sum_{u \in \mathcal{R}} \operatorname{rank}\bigl(D^{u}\bigr), \qquad \sum_{u\in\mathcal{R}} l(b_u) \ \text{-controlled},$$
where $\mathcal{R}$ is a set of representatives of $G$-classes of $p$-elements in $D$ and $D^u = (d^u_{\chi\varphi})$. Since $\sum_{u\in\mathcal{R}} |C_D(u)$-orbit data$| $ relates to $|D|$, the conjecture reduces to bounding each $l(b_u)$: if $l(b_u) \le |C_D(u)$-class count$|$ suitably, $k(B)\le|D|$ follows. Concretely, Brauer's inequality
$$k(B) \le \sum_{u \in \mathcal{R}} l(b_u) \cdot |\{\text{classes}\}| $$
is the standard entry point, and in the "one-section" case $k(B) = \sum_u l(b_u)$ when all $b_u$ have $l=1$.

**Quadratic-form formulation.** Contribution matrices $M^{u} = |C_G(u)|\,D^{u}(C^{u})^{-1}(D^{u})^{*}$ are positive semidefinite integral matrices whose entries lie in $\mathbb{Z}[\zeta_{p^n}]$; the conjecture becomes a statement that a certain positive definite integral quadratic form of determinant $\prod p^{d_i}$ cannot have too many "short" vectors. This is the framework used by Robinson.

**$k(GV)$-problem.** If $G$ acts faithfully and coprimely on a finite abelian $p$-group $V$ (i.e. $p \nmid |G|$), then $k(GV) \le |V|$, where $k(GV)$ is the number of conjugacy classes of the semidirect product.

## 3. History & State of the Art (SOTA)

- **1956.** Brauer states the bound in *Zur Darstellungstheorie der Gruppen endlicher Ordnung*, Math. Z. 63; restated as Problem 20 in his 1963 problem list.
- **1959.** Brauer–Feit prove the first general bound: $k(B) \le \tfrac14 p^{2d} + 1$ for $d \ge 2$. This remained essentially the best unconditional bound for six decades — quadratic in $|D|$ where the conjecture asks for linear.
- **1962.** Nagao reduces the $p$-solvable case to the $k(GV)$-problem.
- **1966.** Dade settles cyclic defect groups: $k(B) = e + \frac{p^d-1}{e}$ with $e \mid p-1$ the inertial index, so $k(B) \le p^d$ with equality iff $e\in\{1,p^d-1\}$ combinatorics permit.
- **1980.** Broué–Puig: nilpotent blocks satisfy $k(B) = k(D) \le |D|$.
- **1996.** Robinson–Thompson prove $k(GV) \le |V|$ for $p > 530$ using the Riese–Schmid "non-real vector" method plus Weil representation estimates. Külshammer–Robinson show the Alperin–McKay conjecture implies Brauer's Problem 21 (the $k_0$ version).
- **2004.** Gluck, Magaard, Riese, Schmid complete the $k(GV)$-problem for all primes; hence **the conjecture holds for all $p$-solvable groups**. Schmid's 2007 monograph gives the full account.
- **2014.** Sambale's *Blocks of Finite Groups and Their Invariants* consolidates verification for small defect groups, especially $p=2$.
- **2016.** Halasi–Podoski give a conceptually cleaner route (base of size two for coprime linear groups) re-proving key $k(GV)$ input.
- **2019–2024.** Improvements on Brauer–Feit using the classification of finite simple groups reduce the exponent below $2d$ *(frontier — verify)*; the proof of Brauer's Height Zero Conjecture (Malle–Navarro–Schaeffer Fry–Tiep, 2024) revitalised the local–global toolkit that a reduction theorem for $k(B)$ would need.

## 4. Partial Results / Verified Cases

- **$p$-solvable groups:** proved unconditionally (Nagao 1962 + Gluck–Magaard–Riese–Schmid 2004). Covers all solvable $G$.
- **Defect $0$:** $k(B)=1=|D|$ trivially. **Defect $1$ / cyclic $D$:** Dade 1966, $k(B)=e+(p^d-1)/e \le p^d$.
- **Nilpotent blocks:** $k(B)=k(D)\le|D|$ (Broué–Puig 1980), with equality iff $D$ abelian.
- **$p=2$, small defect:** verified for all $2$-blocks with $|D| \le 16$, and for most defect groups of order $32$ (Sambale, LNM 2127, 2014). Abelian $2$-defect groups of order $\le 16$ handled completely via Morita classification (Eaton–Kessar–Külshammer–Sambale, Adv. Math. 2014).
- **Structured defect groups:** metacyclic $D$, minimal nonabelian $D$, and $D$ with a large abelian subgroup of index $p$ — verified by Sambale and coauthors for all primes in these families.
- **Blocks with abelian $D$ and known Morita type:** e.g. $D \cong C_p \times C_p$ with $p \le 5$; also blocks of quasi-simple groups have $k(B)$ computable case-by-case, and no counterexample appears in the ATLAS-range libraries.
- **Conditional:** Robinson's Ordinary Weight Conjecture implies $k(B)\le|D|$; Alperin–McKay implies the height-zero refinement $k_0(B)\le|D:D'|$ (Külshammer–Robinson 1996).
- **General unconditional bound:** $k(B)\le \tfrac14 p^{2d}+1$ (Brauer–Feit 1959).

## 5. Principal Obstacles

- **No reduction theorem.** Unlike McKay, Alperin–McKay and Brauer's Height Zero Conjecture, $k(B)\le|D|$ has no proven reduction to quasi-simple groups. $k(B)$ behaves badly under central extensions and central products: characters can fuse or split in ways that break inductive control, so a "if all simple groups are inductively good then the conjecture holds" statement is not available. This is the single largest structural gap.
- **Contribution matrices are underdetermined.** Brauer's machinery bounds $k(B)$ by $\sum_u l(b_u)$-type sums, but bounding $l(b)$ (the number of Brauer characters) is itself the content of Alperin's Weight Conjecture, which is open. The two problems are entangled: current lattice/quadratic-form arguments turn one unknown into another.
- **The $p$-solvable proof does not generalise.** The $k(GV)$ solution rests on coprime linear group actions — regular orbits, bases of size two, Weil representation character estimates. For non-$p$-solvable $G$ there is no coprime module to act on; the fusion system on $D$ can be exotic, and no analogue of "regular orbit" exists.
- **Fusion systems are too weak.** $k(B)$ is not determined by the fusion system $\mathcal{F}$ on $D$ alone in any known effective way; one needs the block algebra's Morita/derived class, and classification of blocks with a given defect group is complete only for $|D|\le 16$ at $p=2$ and very restricted odd cases.
- **Quadratic gap in the generic bound.** Brauer–Feit is quadratic in $|D|$; every attempt to shave it uses global bounds on $k(G)$ (Landau-type) that are insensitive to block structure, so they plateau well above $|D|$.

## 6. The Gap

Proven: the $p$-solvable case, plus all blocks whose defect group lies in a short list of isomorphism types (cyclic, metacyclic, minimal nonabelian, $|D|\le 16$ at $p=2$) or whose block algebra is nilpotent. Conjectured: all blocks.

The exact barrier is:

1. **A reduction theorem** expressing $k(B)$ for $B \in \operatorname{Bl}(G)$ in terms of block invariants of $G/O_p(G)$ and of quasi-simple sections, valid for arbitrary $G$. No such statement is known even conjecturally in a form amenable to CFSG.
2. Failing that, **a uniform bound $l(b_u) \le$ (number of $\mathcal{F}$-classes of $C_D(u)$-data)** for all $p$-sections, which would collapse Brauer's section sum to $|D|$. This is strictly stronger than what any current technique yields for non-$p$-solvable $G$ and is roughly equivalent to the Ordinary Weight Conjecture.

Closing the gap therefore means either proving OWC/AWC, or inventing a genuinely block-local counting argument that bypasses them.

## 7. Current Research (as of June 2026)

- **Sambale (Hannover) and collaborators**: continued classification of blocks by defect group, pushing $p=2$ verification past $|D| = 32$ and treating odd-$p$ defect groups of order $p^3$ and $p^4$ under fusion hypotheses. Also improved general bounds on $k(B)$ using CFSG-based estimates on $k(G)$ *(frontier — verify the exact exponent claimed in the 2019–2022 preprints)*.
- **Kessar–Malle (City, St Andrews / Kaiserslautern)**: block theory of quasi-simple groups, Jordan decomposition of blocks, computing $k(B)$ for unipotent and quasi-isolated blocks of groups of Lie type — the raw data any reduction theorem would consume.
- **Malle–Navarro–Schaeffer Fry–Tiep**: after the 2024 proof of Brauer's Height Zero Conjecture, the same "inductive condition" methodology is being tested against $k(B)$-type statements; the obstacle is that $k(B)\le|D|$ has no evident inductive-condition formulation *(frontier — verify)*.
- **Eaton (Manchester)**: the online classification of Morita equivalence classes of blocks with small defect groups gives machine-checkable confirmation of $k(B)\le|D|$ across those classes.
- **Robinson (Lancaster)**: quadratic-form and Cartan-matrix approaches, and the relation of $k(B)$ to the ordinary weight conjecture.

No counterexample has ever been proposed; the conjecture is regarded as very likely true.

## 8. Future Work

- Formulate and prove a **reduction of $k(B)\le|D|$ to quasi-simple groups**, perhaps via an inductive condition on the level of $\mathcal{O}$-block algebras rather than character bijections.
- Prove the **Ordinary Weight Conjecture** for blocks of groups of Lie type in non-defining characteristic, which would deliver $k(B)\le|D|$ in those cases.
- Extend Donovan's-conjecture-style **finiteness results** (finitely many Morita classes for a fixed defect group) beyond $p=2$; a proof of Donovan for all $p$ would make defect-group-by-defect-group verification a finite computation.
- Improve the Brauer–Feit bound to $k(B) \le C\cdot|D|$ for an absolute constant $C$; even $C = p$ would be a major advance and is not currently available.
- Settle the abelian-defect case, where Broué's abelian defect group conjecture predicts a derived equivalence $B \sim_{\mathrm{der}} b$ with $b$ the Brauer correspondent in $N_G(D)$; since derived equivalence preserves $k$, abelian-defect Broué implies $k(B) = k(b)$, reducing to $p$-solvable-like $N_G(D)$ — already known there.

## 9. Key References

- **[Foundational]** R. Brauer. *Zur Darstellungstheorie der Gruppen endlicher Ordnung.* Mathematische Zeitschrift 63 (1956), 406–444.
- **[Foundational]** R. Brauer. *Representations of finite groups.* In: Lectures on Modern Mathematics, Vol. I (T. L. Saaty, ed.), Wiley, 1963, 133–175. (Problem list, Problems 20–21.)
- **[Foundational]** R. Brauer and W. Feit. *On the number of irreducible characters of finite groups in a given block.* Proc. Nat. Acad. Sci. USA 45 (1959), 361–365.
- **[Foundational]** H. Nagao. *On a conjecture of Brauer for $p$-solvable groups.* J. Math. Osaka City Univ. 13 (1962), 35–38.
- **[Foundational]** E. C. Dade. *Blocks with cyclic defect groups.* Annals of Mathematics 84 (1966), 20–48.
- **[Foundational]** M. Broué and L. Puig. *A Frobenius theorem for blocks.* Inventiones Mathematicae 56 (1980), 117–128.
- **[SOTA]** G. R. Robinson and J. G. Thompson. *On Brauer's $k(B)$-problem.* Journal of Algebra 184 (1996), 1143–1160.
- **[SOTA]** B. Külshammer and G. R. Robinson. *Alperin–McKay implies Brauer's problem 21.* Journal of Algebra 180 (1996), 208–210.
- **[SOTA]** D. Gluck, K. Magaard, U. Riese, P. Schmid. *The solution of the $k(GV)$-problem.* Journal of Algebra 279 (2004), 694–719.
- **[SOTA]** P. Schmid. *The Solution of the $k(GV)$ Problem.* ICP Advanced Texts in Mathematics 4, Imperial College Press, 2007.
- **[SOTA]** C. W. Eaton, R. Kessar, B. Külshammer, B. Sambale. *2-blocks with abelian defect groups.* Advances in Mathematics 254 (2014), 706–735.
- **[SOTA]** Z. Halasi and K. Podoski. *Every coprime linear group admits a base of size two.* Transactions of the AMS 368 (2016), 5857–5887.
- **[SOTA]** G. Malle, G. Navarro, A. A. Schaeffer Fry, P. H. Tiep. *Brauer's Height Zero Conjecture.* Annals of Mathematics 200 (2024), 557–608.
- **[Survey]** B. Sambale. *Blocks of Finite Groups and Their Invariants.* Lecture Notes in Mathematics 2127, Springer, 2014.
- **[Survey]** G. Navarro. *Character Theory and the McKay Conjecture.* Cambridge Studies in Advanced Mathematics 175, Cambridge University Press, 2018.
- **[Survey]** B. Külshammer and T. Wada. *Some inequalities between invariants of blocks.* Archiv der Mathematik (Basel) 79 (2002), 81–86.
- **[Survey]** G. Malle and G. R. Robinson. *On the number of simple modules in a block of a finite group.* Journal of Algebra 475 (2017), 423–438.

## 10. Worked Example / Concrete Special Case

**Take $G = A_5$, $p = 5$.** Then $|G| = 60 = 2^2\cdot 3\cdot 5$, so a Sylow $5$-subgroup is $P = \langle (12345)\rangle \cong C_5$, and $|P| = 5$.

Character degrees of $A_5$: $1, 3, 3, 4, 5$.

**Step 1 — block distribution.** $\nu_5(|G|) = 1$. A character $\chi$ has height-zero defect-$0$ block iff $\nu_5(\chi(1)) = 1$, i.e. $5 \mid \chi(1)$. Only $\chi(1)=5$ qualifies, so the Steinberg-like character of degree $5$ forms its own block $B_0'$ of defect $0$ with $D = 1$: here $k(B_0')=1=|D|$, equality.

**Step 2 — the principal block.** The remaining four characters $\{1, 3a, 3b, 4\}$ lie in the principal block $B$, which has defect group $D = P \cong C_5$. Hence
$$k(B) = 4 \le 5 = |D| .$$

**Step 3 — check against Dade's formula.** $N_G(P) = D_{10}$ (order $10$), $C_G(P) = P$, so the inertial index is
$$e = |N_G(P):C_G(P)| = 10/5 = 2 .$$
Dade's theorem for cyclic defect groups gives
$$k(B) = e + \frac{|D|-1}{e} = 2 + \frac{4}{2} = 4, \qquad l(B) = e = 2 .$$
This matches the character-table count exactly, and $4 < 5$: the bound is strict.

**Step 4 — where equality occurs.** Take instead $G = C_5$ itself with $p=5$. There is one block, $D = G$, and $k(B) = 5 = |D|$. More generally for $G = D$ a $p$-group the unique block is nilpotent with $k(B) = k(D)$, so equality holds precisely when $D$ is abelian. The example pair $(A_5, C_5)$ versus $(C_5, C_5)$ shows the conjecture is tight yet has slack as soon as the inertial index $e > 1$ introduces nontrivial fusion — and it is exactly the absence of a general handle on that fusion, for non-$p$-solvable $G$ with non-cyclic $D$, that leaves the conjecture open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*