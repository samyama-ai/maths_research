---
id: 10-theoretical-cs/mip-star-equals-re
title: "MIP Star equals RE"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# MIP* = RE

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/mip-star-equals-re` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

$\mathrm{MIP}^*$ is the class of languages decidable by a multiprover interactive proof system with a classical polynomial-time verifier and two (or more) non-communicating provers who share an arbitrary finite-dimensional entangled state. $\mathrm{RE}$ is the class of recursively enumerable languages, i.e. many-one equivalent to the halting problem.

**Theorem (Ji–Natarajan–Vidick–Wright–Yuen, 2020).** $\mathrm{MIP}^* = \mathrm{RE}$.

The hard inclusion is $\mathrm{RE} \subseteq \mathrm{MIP}^*$: for every Turing machine $M$ one can compute in polynomial time a two-prover one-round game $G_M$ such that

$$M \text{ halts} \implies \omega^*(G_M) = 1, \qquad M \text{ does not halt} \implies \omega^*(G_M) \le \tfrac{1}{2},$$

where $\omega^*$ is the entangled value. Hence approximating $\omega^*$ to within any fixed constant is undecidable. The reverse inclusion $\mathrm{MIP}^* \subseteq \mathrm{RE}$ is easy: enumerate finite-dimensional strategies of growing dimension on a rational grid.

The theorem is **proved**; what remains open are quantitative and structural refinements (Sections 5–7): the minimal resource parameters (question/answer length, number of provers, rounds, entanglement), and the corresponding statements for commuting-operator and other strategy classes.

## 2. Mathematical Foundations

**Nonlocal game.** $G = (X, Y, A, B, \mu, V)$ with finite question sets $X, Y$, answer sets $A, B$, distribution $\mu$ on $X \times Y$, and predicate $V: A \times B \times X \times Y \to \{0,1\}$.

**Classical value.** $\omega(G) = \max_{f,g} \sum_{x,y} \mu(x,y) V(f(x), g(y) \mid x, y)$ over deterministic $f: X\to A$, $g: Y \to B$.

**Entangled (tensor-product) value.** A strategy is a state $|\psi\rangle \in \mathbb{C}^d \otimes \mathbb{C}^d$ and POVMs $\{A^x_a\}_a$, $\{B^y_b\}_b$; then

$$\omega^*(G) = \sup_{d \in \mathbb{N}} \ \sup_{|\psi\rangle, A, B} \ \sum_{x,y}\mu(x,y)\sum_{a,b} V(a,b\mid x,y)\, \langle \psi | A^x_a \otimes B^y_b |\psi\rangle .$$

The supremum need not be attained (Slofstra 2019).

**Commuting-operator value.** Operators act on one Hilbert space $\mathcal{H}$ with $[A^x_a, B^y_b] = 0$; the resulting $\omega^{co}(G)$ satisfies $\omega^*(G) \le \omega^{co}(G)$, and $\omega^{co}$ is attained.

**Correlation sets.** $C_q(n,k) \subseteq \mathbb{R}^{n^2k^2}$ the tensor-product correlations $p(a,b|x,y)$, $C_{qa} = \overline{C_q}$, $C_{qc}$ the commuting-operator correlations. Always $C_q \subseteq C_{qa} \subseteq C_{qc}$. **Tsirelson's problem** asks whether $C_{qa} = C_{qc}$.

**Connes Embedding Problem (CEP).** Does every separable type $\mathrm{II}_1$ factor $\mathcal{M}$ with trace $\tau$ embed in a trace-preserving way into an ultrapower $\mathcal{R}^{\omega}$ of the hyperfinite $\mathrm{II}_1$ factor? Equivalently (Kirchberg 1993; Junge et al. 2011; Fritz 2012; Ozawa 2013), CEP $\iff$ $C_{qa} = C_{qc}$ for all $n,k$ $\iff$ $C^*(F_n) \otimes_{\min} C^*(F_n) = C^*(F_n) \otimes_{\max} C^*(F_n)$.

**Corollary of the theorem.** Since $\omega^{co}$ is upper semicomputable ($\mathrm{MIP}^{co} \subseteq \mathrm{coRE}$ via the NPA semidefinite hierarchy, Navascués–Pironio–Acín 2008) while $\omega^*$ is lower semicomputable, $\mathrm{MIP}^* = \mathrm{RE} \ne \mathrm{coRE}$ forces $\omega^* \neq \omega^{co}$ on some game. Hence $C_{qa} \neq C_{qc}$, Tsirelson's problem has a negative answer, and **the Connes Embedding Problem is false**.

## 3. History & State of the Art (SOTA)

- **1976:** Connes poses the embedding question in *Classification of injective factors*.
- **1988–93:** Tsirelson formulates the tensor-vs-commuting question for correlations.
- **1988/1991:** Ben-Or–Goldwasser–Kilian–Wigderson define $\mathrm{MIP}$; Babai–Fortnow–Lund prove $\mathrm{MIP} = \mathrm{NEXP}$.
- **2004:** Cleve–Høyer–Toner–Watrous show entanglement can break classical soundness; $\mathrm{MIP}^*$ is defined and no lower bound beyond $\mathrm{NEXP}$-hardness of the classical value is known.
- **2012:** Ito–Vidick: $\mathrm{NEXP} \subseteq \mathrm{MIP}^*$ — the multilinearity test is quantum-sound.
- **2017–2018:** Natarajan–Vidick introduce quantum low-degree testing and rigid self-testing of $n$-qubit states with $\mathrm{polylog}$ communication.
- **2019:** Slofstra: $C_q$ is not closed. Natarajan–Wright: $\mathrm{NEEXP} \subseteq \mathrm{MIP}^*$ via "introspection" — provers are made to sample their own exponentially long questions, an exponential compression.
- **2020:** Ji–Natarajan–Vidick–Wright–Yuen, *MIP\* = RE* (arXiv:2001.04383), iterating compression to a fixed point. CACM version 2021.
- **2021–22:** Structural cleanup: Vidick's *almost synchronous* approximation theorem; Fu–Natarajan–Wright quantum soundness of tensor-code testing; Mousavi–Nezhadi–Yuen place the whole arithmetical hierarchy in nonlocal-game language.
- **2024–25:** Junqiao Lin proves the commuting-operator analogue $\mathrm{MIP}^{co} = \mathrm{coRE}$ *(frontier — verify)*, and the JNVWY manuscript remains under journal review with revisions to the low-individual-degree test.

## 4. Partial Results / Verified Cases

- **$\mathrm{MIP} = \mathrm{NEXP}$** (Babai–Fortnow–Lund 1991): the classical, unentangled base case, 2 provers, 1 round.
- **$\mathrm{NEXP} \subseteq \mathrm{MIP}^*$** (Ito–Vidick 2012), **$\mathrm{NEEXP} \subseteq \mathrm{MIP}^*$** (Natarajan–Wright 2019): one and two levels of the exponential-time hierarchy — the compression step verified once.
- **Fixed small games.** For $|X|=|Y|=|A|=|B|=2$ (e.g. CHSH), $\omega^*$ is exactly computable: Tsirelson's characterization gives $\omega^*_{\mathrm{CHSH}} = \cos^2(\pi/8) = \tfrac12 + \tfrac{\sqrt2}{4} \approx 0.8536$, and $C_q(2,2)=C_{qc}(2,2)$.
- **Synchronous games.** For synchronous $G$, strategies correspond to tracial states on $\mathcal{A}(G)$; the almost-synchronous rounding theorem (Vidick 2022) makes the correspondence robust and is what transfers the complexity result to the operator-algebra statement.
- **Bounded NPA levels.** Level-$k$ of the Navascués–Pironio–Acín SDP hierarchy computes $\omega^{co}$ to arbitrary precision from above; it converges but with no computable rate — consistent with $\mathrm{MIP}^{co}\subseteq\mathrm{coRE}$.
- **Restricted entanglement.** With entanglement dimension bounded by a computable $f(n)$, the value is computable to any precision, so all such restricted classes sit inside $\mathrm{NEXP}$-like bounds, not $\mathrm{RE}$.

## 5. Principal Obstacles

The obstacles are now about *quantitative* strengthening, and about why the pre-2019 toolkit could not have reached $\mathrm{RE}$:

- **No dimension bound from soundness.** Classical PCP soundness analyses extract an assignment from a strategy. Quantumly there is no a priori bound on $d$; every soundness proof must be a *rigidity* argument (self-testing) that pins the strategy to a canonical one up to local isometry and small error. Rigidity is fragile: errors compound multiplicatively across composition steps.
- **Non-commutativity of the "assignment".** Classical low-degree tests use that a function's values at different points are simultaneously defined. Quantum provers hold measurement operators that need not commute; one must prove *approximate* commutation, then apply Gowers–Hatami-type stability to round to an exact representation. Loss in these steps is polynomial in error, not additive, which is why naive iteration of compression diverges.
- **Closure failure.** Because $C_q$ is not closed (Slofstra 2019), $\omega^*$ is a supremum with no optimizer; any argument that "takes an optimal strategy" is invalid, blocking compactness/limiting techniques standard in convex optimization and operator algebras.
- **The $\mathrm{coRE}$ barrier.** Semidefinite hierarchies (NPA), sum-of-squares, and moment methods intrinsically approximate from *above* and so can only ever certify $\omega^{co}$; they can never witness $\mathrm{RE}$-hardness of $\omega^*$. Any proof had to be a reduction, not an analytic estimate.
- **Question complexity.** Current constructions use questions of length polynomial in the input with large constants; the number of questions in the resulting games is astronomically large, so no explicit small game refuting CEP is known.

## 6. The Gap

The gap is no longer between "some cases" and "the theorem", but between the theorem and its sharp forms:

1. **Explicit witness.** The proof is a reduction; it yields no *concrete* correlation $p \in C_{qc} \setminus C_{qa}$ of small size, and no explicit $\mathrm{II}_1$ factor failing Connes embedding. Extracting one requires unwinding an iterated compression with unbounded blow-up.
2. **Resource-optimal versions.** Minimal $(|X|,|A|)$ for which the gap problem is undecidable is unknown; plausible targets are constant answer length with polynomial question length.
3. **Beyond tensor products.** $\mathrm{MIP}^{co} = \mathrm{coRE}$ is the mirror statement; its full verification is recent and not yet independently confirmed *(frontier — verify)*.
4. **Verification.** The 200-page JNVWY argument is not machine-checked; the low-individual-degree test's quantum soundness required a separate erratum-and-repair cycle.

## 7. Current Research (as of June 2026)

- **Simplification programs.** Groups at Caltech/Weizmann (Vidick), Columbia (Yuen), MIT (Natarajan) and Copenhagen (QMATH) are working on modular re-proofs replacing the low-individual-degree test with tensor-code or PCP-of-proximity machinery (Fu–Natarajan–Wright line).
- **Operator-algebraic consequences.** Waterloo (Slofstra, Paddock) and Copenhagen study group-theoretic encodings — linear constraint system games, hyperlinear groups, and the question of whether a non-hyperlinear group can be exhibited from the reduction *(frontier — verify)*.
- **Commuting-operator complexity.** Lin's $\mathrm{MIP}^{co} = \mathrm{coRE}$ and refinements placing $\Pi_2$-complete problems in nonlocal games (following Mousavi–Nezhadi–Yuen) *(frontier — verify)*.
- **Quantitative rigidity.** Improved stability theorems for approximate representations of groups (Gowers–Hatami, Vidick's almost-synchronous rounding) aiming at polynomial-rather-than-root error dependence.
- **Applications.** Delegated quantum computation, device-independent cryptography, and the classification of which physical-theory axioms (e.g. bounded dimension) restore decidability.

## 8. Future Work

- Produce an explicit, small nonlocal game with a certified gap $\omega^{co}(G) - \omega^*(G) > 0$.
- Reduce error dependence in self-testing so that compression can be iterated with constant-factor rather than polynomial-factor loss; this would shrink question length toward optimal.
- Formalize the proof in a proof assistant; the sheer length makes this the natural correctness guarantee.
- Determine the complexity of $\mathrm{MIP}^*$ under bounded entanglement, e.g. $\mathrm{MIP}^*[\text{poly qubits}]$.
- Settle whether a non-hyperlinear group can be constructed effectively from the refutation of CEP.

## 9. Key References

- **[Foundational]** A. Connes. *Classification of injective factors: Cases $\mathrm{II}_1$, $\mathrm{II}_\infty$, $\mathrm{III}_\lambda$, $\lambda \ne 1$.* Annals of Mathematics 104(1), 1976.
- **[Foundational]** L. Babai, L. Fortnow, C. Lund. *Non-deterministic exponential time has two-prover interactive protocols.* Computational Complexity 1, 1991.
- **[Foundational]** R. Cleve, P. Høyer, B. Toner, J. Watrous. *Consequences and limits of nonlocal strategies.* IEEE Conference on Computational Complexity, 2004.
- **[Foundational]** E. Kirchberg. *On non-semisplit extensions, tensor products and exactness of group C\*-algebras.* Inventiones Mathematicae 112, 1993.
- **[SOTA]** Z. Ji, A. Natarajan, T. Vidick, J. Wright, H. Yuen. *MIP\* = RE.* arXiv:2001.04383, 2020; Communications of the ACM 64(11), 2021.
- **[SOTA]** W. Slofstra. *The set of quantum correlations is not closed.* Forum of Mathematics, Pi 7, e1, 2019.
- **[SOTA]** A. Natarajan, J. Wright. *NEEXP $\subseteq$ MIP\*.* IEEE FOCS, 2019.
- **[SOTA]** T. Ito, T. Vidick. *A multi-prover interactive proof for NEXP sound against entangled provers.* IEEE FOCS, 2012.
- **[SOTA]** T. Vidick. *Almost synchronous quantum correlations.* Journal of Mathematical Physics 63(2), 022201, 2022.
- **[SOTA]** H. Fu, A. Natarajan, J. Wright. *Quantum soundness of testing tensor codes.* arXiv:2111.08131, 2021.
- **[SOTA]** H. Mousavi, S. S. Nezhadi, H. Yuen. *Nonlocal games, compression theorems, and the arithmetical hierarchy.* ACM STOC, 2022.
- **[Survey]** N. Ozawa. *About the Connes embedding conjecture: algebraic approaches.* Japanese Journal of Mathematics 8, 2013.
- **[Survey]** C. Palazuelos, T. Vidick. *Survey on nonlocal games and operator space theory.* Journal of Mathematical Physics 57(1), 015220, 2016.
- **[Survey]** M. Junge, M. Navascués, C. Palazuelos, D. Pérez-García, V. B. Scholz, R. F. Werner. *Connes' embedding problem and Tsirelson's problem.* Journal of Mathematical Physics 52(1), 012102, 2011.
- **[Survey]** T. Fritz. *Tsirelson's problem and Kirchberg's conjecture.* Reviews in Mathematical Physics 24(5), 2012.

## 10. Worked Example / Concrete Special Case

**The Mermin–Peres magic square game.** Alice gets a row index $x \in \{1,2,3\}$, Bob a column index $y \in \{1,2,3\}$, uniformly. Alice outputs $a \in \{\pm1\}^3$ with $\prod_i a_i = +1$; Bob outputs $b \in \{\pm1\}^3$ with $\prod_j b_j = -1$. They win iff $a_y = b_x$ (the shared cell agrees).

*Classical value.* A deterministic strategy fills a $3\times3$ sign matrix $M$. Row constraints force $\prod_{\text{all}} M = (+1)^3 = +1$; column constraints force $\prod_{\text{all}} M = (-1)^3 = -1$. Contradiction, so no assignment satisfies all 6 constraints; at most 5 of 6 can hold, hence
$$\omega(G_{\mathrm{MS}}) = \tfrac{8}{9}.$$
(The $8/9$ counts the 8 of 9 question pairs consistent with a best 5-of-6 assignment.)

*Quantum value.* Use two Bell pairs, $|\psi\rangle = \frac{1}{2}(|00\rangle + |11\rangle)^{\otimes 2}$, and the observable square

$$\begin{pmatrix} X\otimes I & I \otimes X & X \otimes X \\ I\otimes Z & Z\otimes I & Z\otimes Z \\ X\otimes Z & Z\otimes X & Y\otimes Y \end{pmatrix}.$$

Each row's three observables commute and multiply to $+I$; each column's commute and multiply to $-I$ (the last column: $(X\otimes X)(Z\otimes Z) = -Y\otimes Y$). Alice measures her row's three commuting observables, Bob his column's. Because $(O \otimes I)|\psi\rangle = (I \otimes O^{T})|\psi\rangle$ for maximally entangled $|\psi\rangle$, the shared-cell outcomes agree with probability 1:
$$\omega^*(G_{\mathrm{MS}}) = 1 > \tfrac{8}{9} = \omega(G_{\mathrm{MS}}).$$

*Why this is the seed of the theorem.* The magic square is *rigid*: any strategy winning with probability $1-\varepsilon$ is, up to local isometry and $O(\sqrt{\varepsilon})$ error, the one above — so the verifier has certified that the provers hold two qubits and measured specified Paulis. Scaling this to $n$ qubits with $\mathrm{polylog}(n)$-length questions (Natarajan–Vidick) lets a verifier certify an $n$-qubit computation while reading only $\mathrm{polylog}(n)$ bits. Introspection then makes the provers generate their own $n$-bit questions, halving the verifier's cost; iterating this compression $k$ times handles $\mathrm{TIME}(2^{\uparrow k})$, and taking the fixed point via Kleene's recursion theorem yields a game $G_M$ with $\omega^*(G_M)=1$ iff $M$ halts — the undecidability at the heart of $\mathrm{MIP}^* = \mathrm{RE}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*