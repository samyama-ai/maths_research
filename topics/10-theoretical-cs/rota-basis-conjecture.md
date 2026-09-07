---
id: 10-theoretical-cs/rota-basis-conjecture
title: "Rota Basis Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rota Basis Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/rota-basis-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $M$ be a matroid of rank $n$ and let $B_1, \dots, B_n$ be $n$ (not necessarily distinct) bases of $M$. **Rota's basis conjecture** asserts that the $n^2$ elements can be arranged in an $n \times n$ array

$$A = (a_{ij})_{1 \le i,j \le n}, \qquad \{a_{i1}, \dots, a_{in}\} = B_i \ \text{ for each } i,$$

such that every **column** $\{a_{1j}, \dots, a_{nj}\}$ is also a basis of $M$.

Equivalently: the disjoint union $B_1 \uplus \cdots \uplus B_n$ (a multiset of $n^2$ elements) can be partitioned into $n$ **transversal bases** — bases using exactly one element from each $B_i$.

A complete proof must establish this for all matroids and all $n$; the conjecture is open even for the special case where $M$ is the matroid of an $n$-dimensional vector space over $\mathbb{R}$ or $\mathbb{C}$. A disproof requires an explicit matroid and family $B_1,\dots,B_n$ with no valid arrangement. (Not to be confused with **Rota's conjecture on matroid minors** — finitely many excluded minors for $\mathbb{F}_q$-representability — announced proved by Geelen, Gerards and Whittle in 2014.)

## 2. Mathematical Foundations

A **matroid** $M = (E, \mathcal{I})$ is a finite ground set $E$ with $\mathcal{I} \subseteq 2^E$ satisfying: $\emptyset \in \mathcal{I}$; $I \in \mathcal{I}, J \subseteq I \Rightarrow J \in \mathcal{I}$; and the augmentation axiom
$$I, J \in \mathcal{I},\ |I| < |J| \ \Longrightarrow\ \exists\, e \in J \setminus I \ \text{ with } I \cup \{e\} \in \mathcal{I}.$$
Maximal independent sets are **bases**, all of common size $r(M) = n$, the **rank**. The motivating example is the vector matroid: $E \subseteq V$ with $\dim V = n$, and $\mathcal{I}$ the linearly independent subsets. There, a transversal set $\{a_{1j},\dots,a_{nj}\}$ is a basis iff
$$\det\big[\,a_{1j} \mid a_{2j} \mid \cdots \mid a_{nj}\,\big] \neq 0 .$$

**Degenerate case.** If $B_1 = \cdots = B_n = \{b_1,\dots,b_n\}$, an admissible array is exactly a **Latin square** of order $n$: $a_{ij} = b_{\sigma_i(j)}$ with $\sigma_1,\dots,\sigma_n$ permutations such that $j \mapsto \sigma_i(j)$ gives distinct values in each column. So Rota's conjecture is a matroidal generalisation of the existence of Latin squares.

**Alon–Tarsi conjecture.** A Latin square $L$ of order $n$ is *even* if the product of the signs of its $n$ rows and $n$ columns (read as permutations) is $+1$, else *odd*. Let $\mathrm{ELS}(n), \mathrm{OLS}(n)$ count them. The conjecture states
$$\mathrm{ELS}(n) \neq \mathrm{OLS}(n) \qquad \text{for all even } n .$$
Huang and Rota (1994) proved the implication: if the Alon–Tarsi conjecture holds for even $n$, then Rota's basis conjecture holds for all vector spaces of dimension $n$ over a field of characteristic $0$. Onn (1997) gave a short determinantal-identity proof of the same implication via the *colorful determinant*
$$\sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) \prod_{i=1}^{n} \det(\cdots) ,$$
recasting the link as a non-vanishing statement for a coefficient of the Cayley/permanent-style expansion of $(\det)^{\otimes n}$.

**Symmetric exchange.** Rota's conjecture strengthens the *symmetric basis exchange* theorem (Brylawski, Greene): for bases $B, B'$ and $x \in B \setminus B'$, there is $y \in B' \setminus B$ with both $B - x + y$ and $B' - y + x$ bases. The $n = 2$ case of Rota is precisely this theorem.

## 3. History & State of the Art (SOTA)

- **1989.** Gian-Carlo Rota poses the conjecture in conversation with Rosa Huang, motivated by straightening coefficients in the theory of the supersymmetric bracket algebra.
- **1992.** Alon and Tarsi state their Latin-square parity conjecture in *Combinatorica*, as a by-product of the Combinatorial Nullstellensatz applied to graph orientations.
- **1994.** Huang and Rota publish the conjecture and prove the Alon–Tarsi $\Rightarrow$ Rota implication. Wild independently proves the conjecture for strongly base orderable matroids.
- **1995–1997.** Chan settles rank $3$. Drisko proves Alon–Tarsi for $n = p+1$, $p$ an odd prime. Onn gives the determinantal reformulation.
- **2006–2007.** Geelen and Humphries prove the conjecture for paving matroids. Geelen and Webb prove that $\Omega(\sqrt{n})$ disjoint transversal bases always exist.
- **2010.** Glynn extends Alon–Tarsi to $n = p - 1$.
- **2017.** Polymath 12, coordinated by Timothy Y. Chow, attacks the conjecture publicly; it produces reformulations (e.g. via "friendly" sequences and a Gallai-type reduction) but no proof.
- **2019–2020.** Dong and Geelen push the disjoint-basis bound to $\Omega(n/\log n)$; Bucić, Kwan, Pokrovskiy and Sudakov reach $(1/2 - o(1))n$; Pokrovskiy reaches $(1 - o(1))n$ — the current SOTA, an asymptotic solution.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $n \le 3$ (all matroids) | True | Chan (1995); $n=2$ is symmetric exchange |
| $n = p+1$, $p$ odd prime, char $0$ vector spaces | True (via Alon–Tarsi) | Drisko (1997) + Huang–Rota (1994) |
| $n = p-1$, $p$ prime, char $0$ | True | Glynn (2010) |
| Strongly base orderable matroids (all $n$) | True | Wild (1994) |
| Paving matroids (all $n$) | True | Geelen–Humphries (2006) |
| Transversal / partition-like matroids | True (special cases of the above) | — |
| Asymptotic: $(1-o(1))n$ disjoint transversal bases | True for all matroids | Pokrovskiy (2020) |
| $\Omega(\sqrt{n})$, then $\Omega(n/\log n)$, then $n/2$ | Superseded bounds | Geelen–Webb (2007); Dong–Geelen (2019); Bucić–Kwan–Pokrovskiy–Sudakov (2020) |

Drisko's and Glynn's families are infinite but of density zero among all $n$; combined with $n \le 4$ ($4 = 3+1$) they cover, e.g., $n \in \{2,3,4,6,8,10,12,16,18,\dots\}$ in characteristic $0$ but leave infinitely many $n$ open. Direct enumeration confirms $\mathrm{ELS}(n) \neq \mathrm{OLS}(n)$ for the small even orders reachable by computer; the counts grow superexponentially and brute force stalls quickly.

## 5. Principal Obstacles

- **The algebraic route is a non-vanishing problem in disguise.** Alon–Tarsi asks that a specific integer — a signed count, equivalently a coefficient of a polynomial in $n^2$ variables — is nonzero. There is no known formula, generating function, or bijective interpretation for $\mathrm{ELS}(n) - \mathrm{OLS}(n)$. Drisko and Glynn succeed only by computing it *modulo a prime*, which is available exactly when $n \pm 1$ is prime; no modulus works for general $n$. Stones and Wanless catalogue several natural "proofs" that provably cannot work, ruling out whole families of parity and group-action arguments.
- **Char $0$ is essential to the reduction.** The Huang–Rota/Onn implication uses a characteristic-zero determinantal identity; over $\mathbb{F}_2$ every Latin square parity argument collapses, so even a full Alon–Tarsi proof would leave matroids and finite-field representations untouched.
- **Greedy/probabilistic methods run out of room at the last columns.** All bounds from Geelen–Webb through Pokrovskiy build transversal bases sequentially or via rainbow-matching machinery (Aharoni–Berger style absorption). Each step needs slack; the final $o(n)$ columns have none, and the leftover multiset is arbitrary. The conjecture is an *exact* partition statement, and approximation techniques have no known exact-completion step.
- **No local certificate.** Matroids give no notion of "column defect" that decreases monotonically under exchange; there is no potential function whose minimum forces a valid array, and no LP/polyhedral relaxation with an integrality theorem (unlike matroid intersection).
- **Strengthenings are false.** Bollen and Draisma showed a natural *online* version — where columns must be committed before later bases are revealed — fails, so any proof must be inherently global.

## 6. The Gap

Proven: (i) exact results for rank $\le 3$, paving and strongly base orderable matroids, and dimensions $p \pm 1$ in characteristic $0$; (ii) for every matroid, $(1-o(1))n$ disjoint transversal bases. The general statement demands all $n$ columns.

The gap is therefore twofold and sharp:

1. **The last $o(n)$ columns.** Pokrovskiy leaves an $o(n)$-sized remainder of elements that need not decompose into transversal bases; converting "almost all" into "all" requires an exact absorption or exchange argument that does not currently exist.
2. **The arithmetic gap in Alon–Tarsi.** For $n$ with both $n-1$ and $n+1$ composite (e.g. $n = 26$), no modulus is known that certifies $\mathrm{ELS}(n) \neq \mathrm{OLS}(n)$. Closing this requires a proof of non-vanishing valid for all even $n$ — and would still only give the characteristic-$0$ vector case, not general matroids.

## 7. Current Research (as of June 2026)

- **Exact completion of the asymptotic result.** The most active direction: adapting the absorption framework of Pokrovskiy and of Bucić–Kwan–Pokrovskiy–Sudakov to handle the residual $o(n)$ elements, likely via a robust-expansion property of the basis-exchange graph. *(frontier — verify)*
- **Rainbow matchings and the Aharoni–Berger circle.** Groups around Aharoni (Technion), Berger, and Briggs/Kim treat Rota as an instance of rainbow independent transversals in matroid intersection; progress on the Aharoni–Berger conjecture ($n$ matchings of size $n+1$ in a bipartite graph yield a rainbow matching of size $n$) transfers partially.
- **Algebraic/computational Alon–Tarsi.** Attempts to evaluate the Alon–Tarsi constant via representation theory of $GL_n$ and plethysm; the constant appears in geometric complexity theory as an obstruction-related quantity (Kumar's work relating Alon–Tarsi non-vanishing to Latin square symmetry). *(frontier — verify)*
- **Matroid-class extensions.** Efforts to extend Geelen–Humphries beyond paving matroids to sparse paving and to graphic matroids; graphic matroids remain open in general.
- **Polymath 12 legacy.** Chow's reformulations (in terms of "friendly" bases and of $2 \times n$ reductions) continue to be used as a testbed; the wiki remains the standard reference for equivalent statements.

Institutions with sustained activity: Waterloo (Geelen), Birkbeck/UCL (Pokrovskiy), ETH Zürich (Sudakov), Technion (Aharoni), Monash (Wanless, Latin-square side).

## 8. Future Work

- Prove Alon–Tarsi for a positive-density set of even $n$ — any progress past $p \pm 1$ would be the first genuinely new arithmetic input in 15 years.
- Find an exact absorber: a structure inside $B_1 \uplus \cdots \uplus B_n$ that can swallow any $o(n)$-sized leftover multiset, upgrading $(1-o(1))n$ to $n$.
- Settle graphic matroids, where the conjecture becomes a statement about $n$ spanning trees of a graph on $n+1$ vertices decomposable into $n$ rainbow spanning trees.
- Determine whether the conjecture can fail for non-representable matroids; a counterexample search among rank-$4$ or rank-$5$ non-representable matroids is computationally feasible and has not been exhausted.
- Develop a polyhedral or algorithmic formulation: is finding the array in **P** when it exists, or is the decision problem hard for general matroid oracles?

## 9. Key References

- **[Foundational]** Rosa Huang and Gian-Carlo Rota. *On the relations of various conjectures on Latin squares and straightening coefficients.* Discrete Mathematics, 128:225–236, 1994.
- **[Foundational]** Noga Alon and Michael Tarsi. *Colorings and orientations of graphs.* Combinatorica, 12:125–134, 1992.
- **[Foundational]** Marcel Wild. *On Rota's problem about $n$ bases in a rank $n$ matroid.* Advances in Mathematics, 108:336–345, 1994.
- **[Partial]** Wendy Chan. *An exchange property of matroid.* Discrete Mathematics, 146:299–302, 1995.
- **[Partial]** Arthur A. Drisko. *On the number of even and odd Latin squares of order $p+1$.* Advances in Mathematics, 128:20–35, 1997.
- **[Partial]** Shmuel Onn. *A colorful determinantal identity, a conjecture of Rota, and Latin squares.* American Mathematical Monthly, 104:156–159, 1997.
- **[Partial]** David G. Glynn. *The conjectures of Alon–Tarsi and Rota in dimension prime minus one.* SIAM Journal on Discrete Mathematics, 24:394–399, 2010.
- **[Partial]** Jim Geelen and Peter J. Humphries. *Rota's basis conjecture for paving matroids.* SIAM Journal on Discrete Mathematics, 20:1042–1045, 2006.
- **[Partial]** Jim Geelen and Kerri Webb. *On Rota's basis conjecture.* SIAM Journal on Discrete Mathematics, 21:802–804, 2007.
- **[SOTA]** Shuxing Dong and Jim Geelen. *Improved bounds for Rota's basis conjecture.* Combinatorica, 39:265–272, 2019.
- **[SOTA]** Matija Bucić, Matthew Kwan, Alexey Pokrovskiy and Benny Sudakov. *Halfway to Rota's basis conjecture.* International Mathematics Research Notices, 2020.
- **[SOTA]** Alexey Pokrovskiy. *Rota's basis conjecture holds asymptotically.* arXiv:2008.06045, 2020.
- **[Related]** Guus P. Bollen and Jan Draisma. *An online version of Rota's basis conjecture.* Journal of Algebraic Combinatorics, 41:1001–1012, 2015.
- **[Survey]** Douglas S. Stones and Ian M. Wanless. *How not to prove the Alon–Tarsi conjecture.* Nagoya Mathematical Journal, 205:1–24, 2012.
- **[Survey]** Timothy Y. Chow et al. *Polymath 12: Rota's Basis Conjecture.* Polymath project wiki and blog, 2017.
- **[Textbook]** James Oxley. *Matroid Theory.* 2nd edition, Oxford University Press, 2011.

## 10. Worked Example / Concrete Special Case

Take $n = 3$, $V = \mathbb{R}^3$ with standard basis $e_1, e_2, e_3$, and the three bases

$$B_1 = \{e_1, e_2, e_3\},\quad B_2 = \{e_1{+}e_2,\ e_2{+}e_3,\ e_3{+}e_1\},\quad B_3 = \{e_1,\ e_1{+}e_2,\ e_1{+}e_2{+}e_3\}.$$

Write $u_1 = e_1{+}e_2$, $u_2 = e_2{+}e_3$, $u_3 = e_3{+}e_1$ and $v_1 = e_1$, $v_2 = e_1{+}e_2$, $v_3 = e_1{+}e_2{+}e_3$. A naive ordering fails: the column $(e_3, u_1, v_3) = ((0,0,1),(1,1,0),(1,1,1))$ is dependent, since $v_3 = u_1 + e_3$.

A valid array is

$$A = \begin{pmatrix} e_3 & e_1 & e_2 \\ u_1 & u_3 & u_2 \\ v_1 & v_2 & v_3 \end{pmatrix} = \begin{pmatrix} e_3 & e_1 & e_2 \\ e_1{+}e_2 & e_3{+}e_1 & e_2{+}e_3 \\ e_1 & e_1{+}e_2 & e_1{+}e_2{+}e_3 \end{pmatrix}.$$

Each row is one of the given bases by construction. Checking the columns as $3 \times 3$ determinants (rows of each matrix are the column's three vectors in coordinates):

$$\det\begin{pmatrix}0&0&1\\1&1&0\\1&0&0\end{pmatrix} = -1,\qquad
\det\begin{pmatrix}1&0&0\\1&0&1\\1&1&0\end{pmatrix} = -1,\qquad
\det\begin{pmatrix}0&1&0\\0&1&1\\1&1&1\end{pmatrix} = 1 .$$

All three are nonzero, so every column is a basis of $\mathbb{R}^3$ and the array certifies the conjecture for this instance.

**Degenerate check.** If instead $B_1 = B_2 = B_3 = \{e_1,e_2,e_3\}$, the required array is any Latin square of order $3$, e.g.
$$\begin{pmatrix} e_1 & e_2 & e_3 \\ e_2 & e_3 & e_1 \\ e_3 & e_1 & e_2 \end{pmatrix},$$
whose columns are permutations of the basis. This shows Rota's conjecture contains Latin-square existence, and explains why the Alon–Tarsi parity count is the natural algebraic obstruction to control.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*