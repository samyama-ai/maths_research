---
id: 02-algebra-group-theory/feit-thompson-theorem
title: "Feit-Thompson Theorem"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Feit-Thompson Theorem

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/feit-thompson-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Theorem (Feit–Thompson, 1963).** Every finite group of odd order is solvable.

Equivalently: every finite simple group of order $> 2$ has even order; equivalently, every finite simple group contains an involution (an element of order $2$).

The statement was conjectured by **Burnside (1911)**, who observed that all known nonabelian simple groups have even order and proved the case of groups with a faithful complex representation of odd degree $< 2p$ for suitable $p$. A complete proof must, given a hypothetical minimal counterexample $G$ — a nonabelian simple group of odd order of minimal order — derive a contradiction; a disproof would require exhibiting a nonabelian simple group of odd order.

The theorem is **proved**. What remains open in this problem cluster:

- **(O1)** The **Feit–Thompson conjecture** (number theory, 1962): for distinct primes $p \ne q$,
$$\gcd\!\left(\frac{p^{q}-1}{p-1},\ \frac{q^{p}-1}{q-1}\right) = 1.$$
This is still open; it would shorten the original proof by removing a chapter of generator-and-relations analysis.
- **(O2)** A **character-free** (purely local) proof of the odd order theorem.
- **(O3)** A substantial reduction of proof length below the current $\approx 255$ published pages of Bender–Glauberman + Peterfalvi.

## 2. Mathematical Foundations

Let $G$ be a finite group, $|G| = n$.

**Solvability.** $G$ is *solvable* if there is a chain $1 = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_k = G$ with each $G_{i+1}/G_i$ abelian. Equivalently the derived series $G^{(0)} = G$, $G^{(i+1)} = [G^{(i)}, G^{(i)}]$ terminates at $1$.

**Nilpotence.** $G$ is nilpotent if its lower central series $\gamma_1 = G$, $\gamma_{i+1} = [\gamma_i, G]$ reaches $1$; equivalently $G$ is the direct product of its Sylow subgroups.

**Frobenius group.** $G = K \rtimes H$ with $H \ne 1$, $K \ne 1$ and $H \cap H^g = 1$ for all $g \notin H$. Frobenius (1901) proved $K \trianglelefteq G$ by character theory; **Thompson (1959)** proved $K$ is nilpotent.

**Local subgroups.** For a $p$-subgroup $P \le G$, $N_G(P)$ and $C_G(P)$. *Local analysis* deduces global structure from these. Key tools:

- **Thompson subgroup.** $J(P) = \langle A : A \in \mathcal{A}(P)\rangle$, where $\mathcal{A}(P)$ is the set of abelian subgroups of $P$ of maximal order.
- **Glauberman's $ZJ$-theorem (1968).** If $p$ is odd, $G$ is $p$-stable and $O_{p'}(G) = 1$, then $Z(J(P)) \trianglelefteq G$ for $P \in \mathrm{Syl}_p(G)$. This gives *factorizations* $G = N_G(Z(J(P)))\, C_G(Z(P))$ (Glauberman's factorization).
- **Thompson's transitivity and the $\sigma$/uniqueness machinery.** For $\pi(G)$ the prime set, define maximal subgroups $M$ with $\sigma(M) = \{p \in \pi(M) : $ a Sylow $p$-subgroup of $M$ has $p$-rank $\ge 3\}$; the *Uniqueness Theorem* (Bender's form) asserts a subgroup of a certain type lies in a unique maximal subgroup.

**Character theory / exceptional characters.** Let $H \le G$ be a *TI-set* normalizer (trivial intersection: $H^g \cap H \in \{1, H\}$). Let
$$\mathcal{S}(H) = \Big\{ \textstyle\sum_i a_i \chi_i \ :\ \chi_i \in \mathrm{Irr}(H),\ a_i \in \mathbb{Z},\ \sum_i a_i \chi_i(1) = 0 \Big\}.$$
Induction $\alpha \mapsto \alpha^{G}$ restricted to $\mathcal{S}(H)$ is a **linear isometry** into the virtual characters of $G$:
$$\langle \alpha^{G}, \beta^{G}\rangle_G = \langle \alpha, \beta\rangle_H, \qquad \alpha,\beta \in \mathcal{S}(H).$$
The isometry is **coherent** if it extends to an isometry defined on all of $\mathbb{Z}\,\mathrm{Irr}(H)$ sending irreducibles to $\pm$irreducibles. Coherence forces strong numerical constraints, e.g. for a Frobenius-like configuration with $|H| = h$,
$$|G| \equiv \pm 1 \pmod{h} \quad\text{or a bound of the shape}\quad |G| \le \big(1 + \tfrac{|H|-1}{2}\big)^2 .$$

**Counting identity used throughout.** If $G$ is partitioned by the conjugates of TI-subgroups $H_1,\dots,H_r$ (a *partition*), then
$$|G| = 1 + \sum_{i=1}^{r} [G:N_G(H_i)]\,(|H_i| - 1).$$

## 3. History & State of the Art (SOTA)

| Year | Milestone |
|---|---|
| 1904 | Burnside: groups of order $p^aq^b$ are solvable (character-theoretic). |
| 1911 | Burnside conjectures odd order $\Rightarrow$ solvable (*Theory of Groups of Finite Order*, 2nd ed.). |
| 1957 | Suzuki: groups of odd order with all centralizers of non-identity elements abelian (**CA-groups**) are solvable. |
| 1959 | Thompson's thesis: Frobenius kernels are nilpotent — introduces the Thompson subgroup and normal $p$-complement theorem. |
| 1960 | Feit–Hall–Thompson: odd-order **CN-groups** (centralizers nilpotent) are solvable. |
| 1963 | **Feit–Thompson**, *Solvability of groups of odd order*, Pacific J. Math. 13, pp. 775–1029 — 255 pages, an entire journal issue. |
| 1970–72 | Bender's uniqueness method; Bender's short proof of $p^aq^b$. |
| 1994 | Bender–Glauberman, *Local Analysis for the Odd Order Theorem* — revised Chapters II–IV. |
| 2000 | Peterfalvi, *Character Theory for the Odd Order Theorem* — revised Chapter V and the final contradiction, including a new treatment of the $p^q$-type configuration. |
| 2013 | **Gonthier et al.**: full machine-checked formalization in Coq/SSReflect (~170,000 lines, ~15,000 definitions/lemmas, 6 person-years). |

The theorem is the historical starting point of the Classification of Finite Simple Groups: it made "study the centralizer of an involution" a viable global strategy (Brauer–Fowler).

## 4. Partial Results / Verified Cases

Cases proved *before* the general theorem, and still the cleanest illustrations:

- **$|G| = p^a q^b$** (Burnside 1904): solvable, any parity.
- **CA-groups of odd order** (Suzuki 1957): $C_G(x)$ abelian for all $x \ne 1$.
- **CN-groups of odd order** (Feit–Hall–Thompson 1960): $C_G(x)$ nilpotent for all $x \ne 1$.
- **Frobenius groups**: kernel nilpotent (Thompson 1959), hence solvable whenever the complement is.
- **Odd order $< 2000$**: no nonabelian simple group of odd order exists in any computationally enumerated range; the smallest nonabelian simple group is $A_5$, order $60$, and all nonabelian simple orders are divisible by $4$ (in fact by $12$, $16$, or $56$ — Burnside/Brauer).
- **Odd-order groups with a faithful complex representation of degree $d$ with $d < \sqrt{|G|}$-type bounds**: solvable by Burnside-style character arguments.

For the **open** conjecture (O1), $\gcd\!\big(\frac{p^q-1}{p-1},\frac{q^p-1}{q-1}\big)=1$ has been verified computationally for all pairs of primes $p,q$ up to large bounds (originally $p, q < 400{,}000$ by Stephens 1971 and far beyond in later searches). Stephens showed the natural *strengthening* — that $\frac{p^q-1}{p-1}$ and $\frac{q^p-1}{q-1}$ have no common factor with $\frac{p^q-1}{p-1}$ replaced by related cyclotomic quantities — fails: for $p=17$, $q=3313$, the analogous gcd is divisible by $2pq+1 = 112643$.

## 5. Principal Obstacles

For the theorem itself the obstacle is now historical, but the *residual* obstacles are sharp:

- **Character theory is unavoidable so far.** Every known proof ends by producing two TI-subgroups $S, T$ (the "$S$- and $T$-configuration") and deriving numerical contradictions from coherence of exceptional-character isometries. No purely local (subgroup-theoretic) substitute for coherence is known: the final configuration has no small-rank local structure left to exploit — all Sylow subgroups are cyclic or of rank 2, and the Thompson-subgroup factorizations become vacuous.
- **The $p^q$ configuration.** The proof's last chapter must rule out a group with $|S| = \frac{p^q-1}{p-1}$-type parameters. Ruling it out group-theoretically requires either (O1) or a delicate generators-and-relations computation showing a certain element has even order. Standard tools fail because the relevant numbers are arbitrary divisors of cyclotomic values, and no effective control over their prime factors exists.
- **Why elementary number theory fails on (O1).** A common prime $r \mid \frac{p^q-1}{p-1}$ and $r \mid \frac{q^p-1}{q-1}$ forces $r \equiv 1 \pmod{2q}$ and $r \equiv 1 \pmod{2p}$, so $r \equiv 1 \pmod{2pq}$ — a strong but not contradictory condition. Ruling it out would need an effective, uniform statement about primitive prime divisors of $p^q - 1$ that Zsygmondy-type theorems do not supply. Stephens' counterexample to the strengthened form shows the "obvious" congruence obstruction is genuinely insufficient.
- **Length as a structural obstacle.** The proof is a case analysis whose branches are individually short but whose interlocking hypotheses (the maximal subgroup types I, II, III, IV, V) resist compression; no conceptual reorganization has removed the case split.

## 6. The Gap

- Between §4 and §1 for the *theorem*: closed. Feit–Thompson (1963), independently re-verified by Bender–Glauberman (1994) + Peterfalvi (2000) and machine-checked (2013).
- Between §4 and (O1): the gap is the nonexistence of a prime $r \equiv 1 \pmod{2pq}$ dividing both $\frac{p^q-1}{p-1}$ and $\frac{q^p-1}{q-1}$. Finite verification covers only $p,q$ below a computational bound; the general statement needs an argument uniform in $p, q$, presumably from the arithmetic of $\mathbb{Z}[\zeta_p,\zeta_q]$ or from height/linear-forms-in-logarithms bounds strong enough to be effective at all sizes. No such bound exists.
- Between §4 and (O2): the gap is a local replacement for the coherence machinery in the final chapter. Bender's uniqueness method eliminated character theory from the *local* half of the proof; nothing analogous exists for the final $S$/$T$ contradiction.

## 7. Current Research (as of June 2026)

- **Formal mathematics.** The Mathematical Components / SSReflect library (Inria, MSR-Inria, Gonthier's group) remains the largest formalized group-theory corpus; ongoing work ports its finite-group infrastructure toward Lean 4 / mathlib, where Sylow theory, Frobenius groups, and ordinary character theory are in place but the odd order theorem is not. *(frontier — verify)*
- **Fusion systems.** Glauberman–Lynd and collaborators pursue $ZJ$-type and Glauberman-functor analogues for saturated fusion systems, aiming at a fusion-theoretic restatement of the local half of the odd order theorem.
- **Second-generation CFSG.** The Gorenstein–Lyons–Solomon volumes (AMS Surveys and Monographs 40.x, continuing) take the odd order theorem as a black box; whether it can be shortened inside that framework is an explicit stated goal.
- **Number theory on (O1).** Sporadic work on gcds of $\Phi$-type quotients, cyclotomic-field factorization, and large-scale searches; no structural progress reported. *(frontier — verify)*

## 8. Future Work

1. Prove (O1) — Feit and Thompson explicitly noted that this would let a chapter of the proof be deleted.
2. Find a coherence-free argument for the final configuration, e.g. via generic character-theoretic bounds or via modular representation theory in characteristic dividing $|S|$.
3. Formalize Bender–Glauberman + Peterfalvi in a second proof assistant, to obtain a proof independent of the Coq development's own architecture.
4. Extract from the formalization a human-readable, compressed proof — the SSReflect development already isolates reusable lemma clusters that the printed proofs duplicate.

## 9. Key References

- **[Foundational]** W. Feit and J. G. Thompson. *Solvability of groups of odd order.* Pacific Journal of Mathematics, 13 (1963), 775–1029.
- **[Foundational]** M. Suzuki. *The nonexistence of a certain type of simple groups of odd order.* Proceedings of the American Mathematical Society, 8 (1957), 686–695. [DOI](https://doi.org/10.1090/s0002-9939-1957-0086818-0)
- **[Foundational]** W. Feit, M. Hall Jr., J. G. Thompson. *Finite groups in which the centralizer of any non-identity element is nilpotent.* Mathematische Zeitschrift, 74 (1960), 1–17. [DOI](https://doi.org/10.1007/bf01180468)
- **[Foundational]** J. G. Thompson. *Normal $p$-complements for finite groups.* Mathematische Zeitschrift, 72 (1959), 332–354.
- **[SOTA]** H. Bender and G. Glauberman. *Local Analysis for the Odd Order Theorem.* London Mathematical Society Lecture Note Series 188, Cambridge University Press, 1994.
- **[SOTA]** T. Peterfalvi. *Character Theory for the Odd Order Theorem.* London Mathematical Society Lecture Note Series 272, Cambridge University Press, 2000.
- **[SOTA / Recent]** G. Gonthier, A. Asperti, J. Avigad, Y. Bertot, C. Cohen, F. Garillot, S. Le Roux, A. Mahboubi, R. O'Connor, S. Ould Biha, I. Pasca, L. Rideau, A. Solovyev, E. Tassi, L. Théry. *A Machine-Checked Proof of the Odd Order Theorem.* In Interactive Theorem Proving (ITP 2013), Lecture Notes in Computer Science 7998, Springer, 163–179. [DOI](https://doi.org/10.1007/978-3-642-39634-2_14)
- **[Related]** N. M. Stephens. *On the Feit–Thompson conjecture.* Mathematics of Computation, 25 (1971), 625. [DOI](https://doi.org/10.1090/s0025-5718-1971-0297686-1)
- **[Related]** G. Glauberman. *A characteristic subgroup of a $p$-stable group.* Canadian Journal of Mathematics, 20 (1968), 1101–1135. [DOI](https://doi.org/10.4153/cjm-1968-107-2)
- **[Survey]** M. Aschbacher. *Finite Group Theory.* 2nd ed., Cambridge Studies in Advanced Mathematics 10, Cambridge University Press, 2000.
- **[Survey]** D. Gorenstein. *Finite Simple Groups: An Introduction to Their Classification.* Plenum Press, 1982.

## 10. Worked Example / Concrete Special Case

**(a) A CA-group of odd order is solvable — the smallest instance.**

Take $G = C_7 \rtimes C_3$ of order $21$, with generators $a$ (order 7), $b$ (order 3), and relation $b a b^{-1} = a^2$ (valid since $2^3 = 8 \equiv 1 \pmod 7$).

- Centralizers: for $1 \ne x \in \langle a\rangle$, $C_G(x) = \langle a \rangle \cong C_7$, abelian. For $x$ of order $3$, $C_G(x) = \langle x \rangle \cong C_3$, abelian. So $G$ is a **CA-group** of odd order.
- $\langle a\rangle \trianglelefteq G$ with $G/\langle a\rangle \cong C_3$, so $1 \trianglelefteq C_7 \trianglelefteq G$ is an abelian series: $G$ is solvable, as Suzuki's theorem requires.
- $G$ is Frobenius with kernel $K = C_7$ (nilpotent, per Thompson) and complement $H = C_3$, a TI-subgroup: $H \cap H^{a} = 1$.
- The counting identity holds: conjugates of $H$ number $[G:N_G(H)] = 21/3 = 7$, giving
$$1 + 7\cdot(3-1) + 1\cdot(7-1) = 1 + 14 + 6 = 21 = |G|. \checkmark$$
- Character check: $\mathrm{Irr}(G)$ has degrees $1,1,1,3,3$, and $1+1+1+9+9=21$. The two degree-3 characters are the *exceptional characters* induced from the three nontrivial characters of $K$; for $\alpha = \lambda_1 - \lambda_2 \in \mathcal{S}(K)$ one verifies $\langle \alpha^G,\alpha^G\rangle_G = \langle\alpha,\alpha\rangle_K = 2$ — the isometry in action. No contradiction arises here precisely because $G$ is solvable.

**(b) The Feit–Thompson conjecture at $p=3, q=5$.**

$$\frac{3^5-1}{3-1} = \frac{242}{2} = 121 = 11^2, \qquad \frac{5^3-1}{5-1} = \frac{124}{4} = 31.$$
$\gcd(121,31) = 1$. Consistent with the congruence obstruction: any common prime $r$ would satisfy $r \equiv 1 \pmod{2\cdot 3\cdot 5 = 30}$, so $r \in \{31, 61, 151, \dots\}$; here $31 \nmid 121$ and $11 \not\equiv 1 \pmod{30}$.

At $p=3,q=7$: $\frac{3^7-1}{2} = 1093$ (prime), $\frac{7^3-1}{6} = 57 = 3\cdot 19$; $\gcd = 1$, and indeed $1093 \equiv 1 \pmod{42}$ but $1093 \nmid 57$. The conjecture asserts this coincidence-avoidance for *all* prime pairs; no proof is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*