---
id: 08-logic-set-theory/laver-tables-periodicity-problem
title: "Laver Tables Periodicity Problem"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Laver Tables Periodicity Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/laver-tables-periodicity-problem` · **Status:** open

## 1. Problem Statement / Conjecture

For each $n \ge 0$ there is a unique binary operation $*$ on $\{1,2,\dots,2^n\}$ satisfying the left self-distributive law together with $p * 1 = p+1 \bmod 2^n$. This finite structure is the **$n$-th Laver table** $A_n$. Its first row $q \mapsto 1 * q$ is periodic; write $\pi(n)$ for its period, always a power of $2$.

**Conjecture (Laver).** $\pi(n) \to \infty$ as $n \to \infty$.

Equivalently: for every $k$ there exists $n$ with $\pi(n) \ge 2^k$. The statement is $\Pi^0_2$ arithmetic and purely finitary — each instance is decidable by finite computation.

Known status: the conjecture is a **theorem of ZFC + I3** (existence of a nontrivial elementary embedding $j : V_\lambda \to V_\lambda$), proved by Laver. No proof from ZFC alone is known, and no independence from ZFC is known. A complete resolution means either a ZFC proof, a ZFC refutation (an $n_0$ with $\pi(n) = \pi(n_0)$ for all $n \ge n_0$), or a proof of independence from ZFC. Dougherty and Jech showed that no proof can be carried out in primitive recursive arithmetic.

## 2. Mathematical Foundations

**Left-distributive (LD) systems.** A set $S$ with $* : S \times S \to S$ is *left self-distributive* if
$$p * (q * r) = (p * q) * (p * r) \qquad \text{for all } p,q,r \in S.$$
This is the algebraic shadow of the application operation on elementary embeddings and of the braid-group action; it is the "one-sided" analogue of a rack/quandle without the idempotency or invertibility axioms.

**Laver tables.** Fix $N = 2^n$ and $A_n = \{1,\dots,2^n\}$ with $2^n$ playing the role of $0$.

> **Theorem (Laver 1995).** For each $n$ there is exactly one operation $*$ on $A_n$ that is left-distributive and satisfies $p * 1 = p + 1 \pmod{2^n}$.

Uniqueness gives a recursion computing the whole table from the first column:
$$p * 1 = p+1 \ (\mathrm{mod}\ 2^n), \qquad p * (q+1) = (p * q) * (p * 1) = (p*q)*(p+1).$$
Basic identities: $2^n * q = q$ (right identity acting as a left unit), $p * 2^n = 2^n$ for $p<2^n$, and $p * q > p$ whenever $p < 2^n$, so each row is a periodic sequence of values in $(p, 2^n]$.

**Periodicity data.** Every row of $A_n$ is periodic with period a power of $2$; the first row's period
$$\pi(n) := \min\{ t \ge 1 : 1*(q+t) = 1*q \ \ \forall q \}$$
satisfies $\pi(n) \in \{1,2,4,\dots,2^n\}$, and the row takes the values $\{2\cdot 2^n/\pi(n) \cdot i\}$ in a strictly increasing pattern before repeating.

**Coherence.** Reduction mod $2^n$ is a surjective homomorphism $A_{n+1} \twoheadrightarrow A_n$. Hence
$$\pi(n) \le \pi(n+1) \le 2\,\pi(n),$$
so $\pi$ is nondecreasing and at most doubles at each step. The inverse limit $A_\infty = \varprojlim_n A_n$ is an LD-system generated topologically by $1$.

**Set-theoretic source.** Let $j : V_\lambda \to V_\lambda$ be elementary and nontrivial (axiom I3). The set $\mathcal{E}_\lambda$ of such embeddings is closed under
$$ j * k = \bigcup_{\alpha<\lambda} j(k \cap V_\alpha),$$
which is left-distributive by elementarity. Let $\mathcal{A}_j$ be the closure of $\{j\}$ under $*$, and let $\mathrm{crit}$ denote critical points. Laver proved that the quotient of $\mathcal{A}_j$ by the congruence "agree up to level $\gamma_n$" is isomorphic to $A_n$, and that the critical points of $\mathcal{A}_j$ form a strictly increasing $\omega$-sequence. This forces $\pi(n)\to\infty$.

> **Theorem (Laver).** If there is a nontrivial elementary $j: V_\lambda \to V_\lambda$, then $\pi(n) \to \infty$.

> **Theorem (Dougherty–Jech 1997).** $\pi(n) \to \infty$ holds if and only if $A_\infty$ contains a free monogenerated LD-system; and the statement is not provable in PRA.

## 3. History & State of the Art (SOTA)

- **1989–1992.** Richard Laver, studying the algebra of rank-into-rank embeddings, proves the free monogenerated LD-system is realized inside $\mathcal{E}_\lambda$ under I3 (*Adv. Math.* 91, 1992). The finite quotients $A_n$ emerge as the "critical-point tables".
- **1992.** Patrick Dehornoy removes the large cardinal from the *freeness* theorem, giving a ZFC proof via the braid group $B_\infty$ and the left-order on braids. This is the template that the periodicity problem has so far resisted.
- **1993–1996.** Randall Dougherty computes Laver tables far beyond naive limits and proves Ackermann-type lower bounds on how slowly $\pi$ can grow (*APAL* 65, 1993; *Logic: from Foundations to Applications*, OUP 1996).
- **1995–1997.** Aleš Drápal analyses periodicity and "persistence" of cyclic LD algebras, obtaining structural constraints on when $\pi(n+1) = 2\pi(n)$.
- **1997.** Dougherty–Jech (*Adv. Math.* 130) isolate the exact proof-theoretic obstruction: the periodicity statement, if true, has an inverse function that is not primitive recursive, so PRA cannot prove it.
- **2000–2014.** Dehornoy's monograph *Braids and Self-Distributivity* consolidates the field; Dehornoy and Victoria Lebed compute $2$- and $3$-cocycles of Laver tables, exposing cohomological invariants tied to $\pi(n)$ and connecting the tables to knot/braid invariants.
- **State of the art:** the conjecture stands exactly where Laver left it — provable from I3, not from ZFC, not refuted, with computational evidence limited by Ackermannian growth.

## 4. Partial Results / Verified Cases

- **Exact small values.** $\pi(0)=\pi(1)=1$, $\pi(2)=2$, $\pi(3)=\pi(4)=4$, $\pi(5)=\cdots=\pi(8)=8$, $\pi(9)=\cdots=\pi(47)=16$.
- **First-occurrence sequence.** The least $n$ with $\pi(n) = 2^k$ for $k=0,\dots,5$ is $1, 2, 3, 5, 9, 48$ (OEIS A098820). The value $\pi(48)=32$ is Dougherty's 1996 computation; the table $A_{48}$ has $2^{48} \approx 2.8\times 10^{14}$ rows and is handled by row-compression, not enumeration.
- **Complete verification range.** Periodicity behaviour is verified exactly for all $n \le 48$; beyond that, only $\pi(n)\ge 32$ is known unconditionally (monotonicity).
- **Conditional growth bound (Dougherty 1993).** If $\pi(n)\to\infty$, then $k \mapsto \min\{n : \pi(n)\ge 2^k\}$ eventually dominates every primitive recursive function; concretely, the least $n$ with $\pi(n)\ge 2^{32}$ exceeds $\mathrm{Ack}(9,\mathrm{Ack}(8,\mathrm{Ack}(8,254)))$ *(numerical constant — verify against the 1993 paper)*.
- **Unconditional structure.** $\pi(n+1) \in \{\pi(n), 2\pi(n)\}$ for all $n$; each row of $A_n$ is periodic with $2$-power period (Laver); Drápal characterises the "doubling" step in terms of persistence of an associated cyclic algebra.
- **Free-object case.** Laver's freeness theorem for the monogenerated free LD-system — the companion statement — is a **ZFC theorem** (Dehornoy, via braid orderings).

## 5. Principal Obstacles

- **The only known proof mechanism is a large cardinal.** Laver's argument needs an actual $\omega$-sequence of critical points of a rank-into-rank embedding, i.e. consistency strength near the top of the large-cardinal hierarchy, to certify a $\Pi^0_2$ arithmetic sentence. Nothing in the finite combinatorics of $A_n$ has yet been made to simulate elementarity.
- **Proof-theoretic barrier.** Dougherty–Jech: any proof must exceed PRA, since the witnessing function is not primitive recursive. Every "elementary" combinatorial induction on $n$ therefore fails on strength grounds, not merely on ingenuity.
- **Computation is blocked by Ackermannian sparsity.** Detecting $\pi(n)\ge 64$ requires $n$ beyond any conceivable computation; brute force gives no evidence either way. Verification cannot even reach the next data point.
- **No algebraic invariant tracks the period.** Cohomological data (Dehornoy–Lebed) and Drápal's persistence conditions constrain *when* the period doubles but supply no infinitary mechanism guaranteeing that doubling recurs.
- **The braid substitute is incomplete.** Dehornoy's braid-order technique replaced I3 for freeness because freeness reduces to a *comparison property* of braid words. Periodicity has no known reformulation as an order or normal-form property of $B_\infty$; the finite quotients $A_n$ are not directly visible in the braid monoid.

## 6. The Gap

Proven: $\pi(n)$ is nondecreasing, doubles at most once per step, is exactly known for $n \le 48$ (where it reaches $32$), and tends to infinity **under I3**.

The general claim: $\sup_n \pi(n) = \infty$ in ZFC.

The gap is a single step: **produce, in ZFC, an infinite supply of "period-doubling witnesses"**. Under I3 these are critical points $\mathrm{crit}(j_1)<\mathrm{crit}(j_2)<\cdots$ of embeddings in $\mathcal{A}_j$; each new critical point forces a new doubling. A ZFC proof needs a finitary or braid-theoretic object playing the role of the critical sequence — equivalently, by Dougherty–Jech, a ZFC construction of a free monogenerated LD-system *inside* $A_\infty$. Conversely, a refutation needs an $n_0$ and a finite certificate that the period stabilises forever, which by the Ackermannian bound cannot be a direct computation and must be a structural stabilisation argument. Neither direction has a candidate.

## 7. Current Research (as of June 2026)

- **Cohomology and knot-theoretic invariants.** Continuation of the Dehornoy–Lebed programme: computing $H^2, H^3$ of $A_n$ and the associated braid/knot invariants, looking for an invariant whose non-vanishing is equivalent to period growth. Groups in Paris–Saclay/Caen (Dehornoy's school) and Trinity College Dublin (Lebed).
- **Generalised and endomorphic Laver tables.** Extensions of $A_n$ to multi-generator and "endomorphic" settings, aiming to embed the periodicity question in a richer algebraic family where induction is available *(frontier — verify)*; associated large-scale computations of classical Laver tables and their algebraic invariants circulate as preprints and software.
- **Reverse mathematics.** Locating the exact strength of "$\pi(n)\to\infty$" above PRA: is it provable in $\mathrm{I\Sigma}_1$-free fragments, in $\mathrm{ACA}_0$, or does it require genuine large-cardinal reflection? No sharp classification is published *(frontier — verify)*.
- **Set-theoretic side.** Ongoing work on the algebra of elementary embeddings, $\mathcal{E}_\lambda$, and its finite quotients, within the broader rank-into-rank programme (Kanamori-style large-cardinal analysis; Dimonte and collaborators on I0/I3 structure theory).

## 8. Future Work

- **Find the braid analogue.** Dehornoy's advice, repeated in the *Handbook of Set Theory* chapter, is to seek a ZFC realization of the critical sequence — a concrete LD-system with an increasing sequence of "levels" — as was done for freeness with the braid order.
- **Prove a doubling criterion.** Drápal-style persistence results suggest hunting for a decidable condition $C(n)$ such that $C(n)$ implies $\pi(m) = 2\pi(n)$ for some $m>n$, plus a proof that $C$ recurs.
- **Extract the exact proof-theoretic ordinal.** Determine whether the statement is equivalent, over a weak base theory, to a known independent combinatorial principle (Goodstein/Kirby–Paris family) — which would explain the Ackermannian growth intrinsically.
- **Nonstandard-model approach.** Build a nonstandard model of the $A_n$ hierarchy in which an "internal" elementary embedding exists, then transfer the arithmetic conclusion downward.
- **Computation of invariants, not tables.** Since $A_n$ itself is unreachable for $n$ near the next threshold, compute derived invariants (cocycles, orbit counts) whose behaviour is predicted differently by the two answers.

## 9. Key References

- **[Foundational]** Richard Laver. *The left distributive law and the freeness of an algebra of elementary embeddings.* Advances in Mathematics **91** (1992), 209–231.
- **[Foundational]** Richard Laver. *On the algebra of elementary embeddings of a rank into itself.* Advances in Mathematics **110** (1995), 334–346.
- **[SOTA]** Randall Dougherty. *Critical points in an algebra of elementary embeddings.* Annals of Pure and Applied Logic **65** (1993), 211–241.
- **[SOTA]** Randall Dougherty. *Critical points in an algebra of elementary embeddings, II.* In *Logic: From Foundations to Applications* (W. Hodges et al., eds.), Oxford University Press, 1996, 103–136.
- **[SOTA]** Randall Dougherty and Thomas Jech. *Finite left-distributive algebras and embedding algebras.* Advances in Mathematics **130** (1997), 201–241.
- **[Structural]** Aleš Drápal. *Persistence of cyclic left distributive algebras.* Journal of Pure and Applied Algebra **105** (1995), 137–165.
- **[Structural]** Aleš Drápal. *Finite left distributive algebras with one generator.* Journal of Pure and Applied Algebra **121** (1997), 233–251.
- **[Book]** Patrick Dehornoy. *Braids and Self-Distributivity.* Progress in Mathematics **192**, Birkhäuser, 2000.
- **[Survey]** Patrick Dehornoy. *Elementary embeddings and algebra.* In *Handbook of Set Theory* (M. Foreman and A. Kanamori, eds.), Springer, 2010, 737–774.
- **[Recent]** Patrick Dehornoy and Victoria Lebed. *Two- and three-cocycles for Laver tables.* Journal of Knot Theory and Its Ramifications **23** (2014), 1450017.
- **[Background]** Akihiro Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd ed., Springer, 2003.

## 10. Worked Example / Concrete Special Case

**Build $A_2$ on $\{1,2,3,4\}$ and read off $\pi(2)=2$.**

Rules: $p*1 = p+1 \bmod 4$ (so $4*1=1$), and $p*(q+1) = (p*q)*(p+1)$.

*Row 3.* $3*1 = 4$. Since $4$ is a left unit ($4*q=q$): $3*2 = (3*1)*4 = 4*4 = 4$; $3*3 = (3*2)*4 = 4$; $3*4 = 4$. Row $3$: $4,4,4,4$.

*Row 2.* $2*1 = 3$. Then $2*2 = (2*1)*3 = 3*3 = 4$; $2*3 = (2*2)*3 = 4*3 = 3$; $2*4 = (2*3)*3 = 3*3 = 4$. Row $2$: $3,4,3,4$.

*Row 1.* $1*1 = 2$. Then $1*2 = (1*1)*2 = 2*2 = 4$; $1*3 = (1*2)*2 = 4*2 = 2$; $1*4 = (1*3)*2 = 2*2 = 4$. Row $1$: $2,4,2,4$.

| $*$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 2 | 4 | 2 | 4 |
| **2** | 3 | 4 | 3 | 4 |
| **3** | 4 | 4 | 4 | 4 |
| **4** | 1 | 2 | 3 | 4 |

The first row repeats with period $2$, so $\pi(2)=2$.

**Why this is hard to continue.** The same recursion gives first rows
$$A_3: 2,4,6,8,2,4,6,8 \Rightarrow \pi(3)=4, \qquad A_4: \pi(4)=4, \qquad A_5: \pi(5)=8 .$$
Monotonicity gives $\pi(n)\ge 8$ for $n\ge 5$ and $\pi(n) \ge 16$ for $n \ge 9$ — but the next doubling does not appear until $n=48$, after $39$ consecutive stalls. Whether the sequence $16,16,\dots,16,32$ ever doubles again is precisely the open problem: no finite amount of table computation can distinguish "eventually constant" from "grows Ackermannian-slowly", and only the rank-into-rank axiom currently rules out the former.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*