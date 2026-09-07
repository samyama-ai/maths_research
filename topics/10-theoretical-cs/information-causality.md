---
id: 10-theoretical-cs/information-causality
title: "Information Causality"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Information Causality

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/information-causality` · **Status:** open

## 1. Problem Statement / Conjecture

Information Causality (IC) is a physical/information-theoretic axiom proposed as a candidate answer to Popescu–Rohrlich's question: *why is nature no more nonlocal than quantum mechanics?* Informally: if Alice sends Bob $m$ classical bits, Bob's total information gain about Alice's database is at most $m$ bits, however much prior correlation (entanglement, or post-quantum "boxes") they share.

The open problem has three linked parts.

1. **(Characterization conjecture.)** Let $\mathcal{Q}$ be the set of quantum correlations and $\mathcal{IC}$ the set of no-signalling correlations satisfying IC under all protocols, including wirings and parallel/adaptive use of many copies. Is $\mathcal{IC} = \mathcal{Q}$ in the bipartite case? Every known partial computation gives $\mathcal{Q} \subseteq \mathcal{IC}$ with equality on special slices; the general question is open.
2. **(Exact formulation.)** IC is a *family* of constraints, one per protocol, not a single closed-form condition. There is no known algorithm that decides, for a given box $P(ab|xy)$, whether some protocol violates IC. Producing a complete, protocol-independent analytic characterization of $\mathcal{IC}$ is itself open.
3. **(Multipartite scope.)** Does a multipartite generalization of IC exclude all supra-quantum multipartite correlations, including those whose every bipartition is local?

A complete resolution means either a proof that $\mathcal{IC}=\mathcal{Q}$ (equivalently, an IC-based derivation of the NPA/Tsirelson boundary at every point), or an explicit supra-quantum no-signalling box provably satisfying IC under every protocol.

## 2. Mathematical Foundations

**Correlation sets.** A bipartite behaviour is a conditional distribution $P(ab|xy)$ with inputs $x\in X$, $y\in Y$ and outputs $a\in A$, $b\in B$. No-signalling:
$$\sum_a P(ab|xy) = \sum_a P(ab|x'y)\ \ \forall b,y,x,x', \qquad \text{and symmetrically.}$$
Write $\mathcal{NS}$ for the no-signalling polytope, $\mathcal{L}\subset\mathcal{Q}\subset\mathcal{NS}$ for the local polytope and the quantum set, where
$$P\in\mathcal{Q} \iff P(ab|xy)=\langle\psi| M^x_a\otimes N^y_b|\psi\rangle$$
for projective measurements on a tensor-product Hilbert space.

**The IC task.** Alice receives a uniformly random string $\vec a = (a_0,\dots,a_{N-1})\in\{0,1\}^N$, $N=2^n$. Bob receives $b\in\{0,\dots,N-1\}$, uniform and independent. Alice sends an $m$-bit message $M$; Bob outputs a guess $\beta$ for $a_b$. Information Causality states
$$\boxed{\ \mathcal{I} \;:=\; \sum_{k=0}^{N-1} I\!\left(a_k : \beta \,\middle|\, b=k\right) \;\le\; m\ }$$
where $I(\cdot:\cdot)$ is Shannon mutual information. Classical shared randomness and quantum entanglement both satisfy this; the content is that arbitrary no-signalling resources need not.

**Quantum proof sketch.** With $\rho_B$ Bob's state, $\mathcal{I} \le I(\vec a : M B)$ by data processing and the chain rule with independent $a_k$; then $I(\vec a : MB) \le I(\vec a : B) + H(M) \le 0 + m$ by no-signalling and the Holevo bound $\chi \le \log_2 \dim$. Hence $\mathcal{Q}\subseteq\mathcal{IC}$.

**PR box.** The Popescu–Rohrlich box $P_{\mathrm{PR}}(ab|xy)=\tfrac12\delta_{a\oplus b,\,xy}$ satisfies $\mathrm{CHSH}=4$. Isotropic mixtures $P_E = E\,P_{\mathrm{PR}} + (1-E)\,P_{\mathrm{noise}}$ have single-use success probability $p=(1+E)/2$ and $\mathrm{CHSH}(P_E)=4E$.

**Key entropic tool.** For $h(\cdot)$ the binary entropy,
$$1-h\!\left(\tfrac{1+e}{2}\right)\;\ge\;\frac{e^{2}}{2\ln 2}.$$

**Tsirelson bound.** $\mathrm{CHSH}_{\mathcal{Q}} \le 2\sqrt2$ (Tsirelson 1980), i.e. $E\le 1/\sqrt2$ for isotropic boxes.

## 3. History & State of the Art (SOTA)

- **1980.** Tsirelson proves $\mathrm{CHSH}\le 2\sqrt2$ for quantum correlations.
- **1994.** Popescu and Rohrlich show that no-signalling alone permits $\mathrm{CHSH}=4$, posing the axiomatization problem.
- **2000–2006.** van Dam shows a perfect PR box makes communication complexity trivial (1-bit protocols for any Boolean function); Brassard, Buhrman, Linden, Méthot, Tapp and Unger extend this to noisy boxes with $p > \tfrac{3+\sqrt6}{6}\approx 0.908$ — still strictly above Tsirelson's $p\approx0.8536$, so "non-trivial communication complexity" does not recover $\mathcal{Q}$.
- **2009.** Pawłowski, Paterek, Kaszlikowski, Scarani, Winter and Żukowski introduce IC (*Nature* 461, 1101) and show it reproduces the Tsirelson bound *exactly* on the isotropic CHSH slice. This is the first principle to hit $2\sqrt2$ on the nose.
- **2009–2011.** Allcock, Brunner, Pawłowski, Scarani recover curved portions of $\partial\mathcal{Q}$ in two-parameter families. Barnum, Beigi, Boixo, Elliott, Wehner derive Tsirelson's bound from local quantum measurement + no-signalling. Al-Safi and Short give entropic and probabilistic reformulations.
- **2010–2011.** Cavalcanti, Salles and Scarani exhibit macroscopically local correlations violating IC (so IC is strictly stronger than macroscopic locality on those slices). Gallego, Würflinger, Acín and Navascués prove that *no* bipartite principle — IC included — can rule out all supra-quantum tripartite correlations.
- **2015.** Navascués, Guryanova, Hoban and Acín define the *almost quantum* set $\tilde{\mathcal{Q}}\supsetneq\mathcal{Q}$, which satisfies every known device-independent principle and (numerically, on tested slices) IC. This is the central obstruction to $\mathcal{IC}=\mathcal{Q}$.
- **2021.** Miklin and Pawłowski derive the Tsirelson bound from IC *without* protocol concatenation, simplifying the analytic machinery.

## 4. Partial Results / Verified Cases

- **Quantum theory satisfies IC** for all $n$, all message lengths $m$, all Hilbert-space dimensions, all protocols. Proof via Holevo. This direction is closed.
- **Isotropic CHSH boxes $(2,2,2)$:** IC is violated iff $E > 1/\sqrt2$, i.e. $\mathrm{CHSH} > 2\sqrt2$. Exact match with $\partial\mathcal{Q}$.
- **All extremal nonlocal vertices of the $(2,2,2)$ no-signalling polytope** are local-relabelling equivalent to the PR box and are excluded by IC (violation grows without bound in $n$).
- **Two-parameter slices** (Allcock et al., *Phys. Rev. A* 80, 062107, 2009): IC recovers a *curved* boundary that coincides with $\partial\mathcal{Q}$ at isolated points and lies strictly outside elsewhere; the gap is nonzero but numerically small ($\lesssim 10^{-2}$ in CHSH units on the tested cuts).
- **Nonlocal computation:** boxes giving any advantage for nonlocal computation of a Boolean function violate IC (via Linden–Popescu–Short–Winter, PRL 2007, combined with the IC protocol).
- **Negative case:** in the tripartite $(3,2,2)$ scenario, Gallego et al. exhibit supra-quantum correlations local across every bipartition — IC applied bipartitewise is powerless.
- **Generalized probabilistic theories:** Barnum, Barrett, Clark, Leifer, Spekkens, Stepanik, Wilce and Wilke (NJP 12, 033024, 2010) show IC-type entropic bounds hold in theories where a suitable data-processing inequality and Holevo-like bound exist; boxworld fails both.

## 5. Principal Obstacles

- **No closed form.** $\mathcal{IC}$ is an infinite intersection over protocols (encodings, wirings, adaptivity, number of box copies). Each protocol gives a constraint; violating one certifies exclusion, but *satisfying* all of a finite tested family certifies nothing. There is no known convergent hierarchy for $\mathcal{IC}$ analogous to NPA for $\mathcal{Q}$.
- **Entropic relaxations are lossy.** The standard derivation uses $1-h((1+e)/2)\ge e^2/(2\ln 2)$ and repeated data-processing steps. Each is tight only at specific points; away from the isotropic slice the accumulated slack is exactly what leaves the IC boundary outside $\partial\mathcal{Q}$.
- **Non-convexity of the protocol optimization.** Choosing the optimal wiring of $2^n-1$ box uses is a discrete optimization of size doubly exponential in $n$; brute force stops around $n=3$–$4$.
- **$\tilde{\mathcal{Q}}$ is the wall.** The almost quantum set is closed under wirings, has a semidefinite (NPA level $1+AB$) description, and reproduces the operational features that all information-theoretic principles exploit. Any proof that $\mathcal{IC}=\mathcal{Q}$ must find a protocol distinguishing $\tilde{\mathcal{Q}}\setminus\mathcal{Q}$ — none is known, and a proof that $\tilde{\mathcal{Q}}\subseteq\mathcal{IC}$ would refute the conjecture.
- **Bipartite blindness (proved).** Gallego et al. is not a technical gap but a theorem: bipartite principles are provably insufficient multipartitely. IC must be genuinely generalized, and no canonical multipartite version exists.
- **Shannon entropy is the wrong invariant?** Rényi/min-entropy and one-shot variants have been tried; they change which boxes are excluded without closing the gap, suggesting the entropic framing itself may be the limitation.

## 6. The Gap

Proven: $\mathcal{Q}\subseteq\mathcal{IC}\subsetneq\mathcal{NS}$, with equality $\partial\mathcal{IC}=\partial\mathcal{Q}$ on the isotropic CHSH line and isolated points of two-parameter slices. Conjectured: $\mathcal{IC}=\mathcal{Q}$.

The exact missing step: for every $P\in\mathcal{NS}\setminus\mathcal{Q}$, construct a random-access-code protocol (a wiring of finitely many copies of $P$ plus an $m$-bit message) with $\sum_k I(a_k:\beta|b=k)>m$. Equivalently, show that the NPA hierarchy's SDP certificate of non-membership can be converted into an entropic violation. Concretely, the first target is a single box in $\tilde{\mathcal{Q}}\setminus\mathcal{Q}$ — such boxes are explicitly constructible from the $1+AB$ SDP — for which IC fails. No conversion mechanism between SDP dual certificates and information-theoretic protocols is known.

## 7. Current Research (as of June 2026)

- **Concatenation-free IC.** Following Miklin–Pawłowski (PRL 126, 220403, 2021), groups at Gdańsk (Pawłowski) work on single-shot IC inequalities whose violation region can be computed by convex optimization rather than protocol search.
- **IC vs. almost quantum.** ICFO Barcelona (Acín, Navascués) and Vienna probe whether $\tilde{\mathcal{Q}}$ violates IC under high-$n$ adaptive protocols. Numerics to $n=4$ report no violation. *(frontier — verify)*
- **Multipartite / causal-network IC.** Chaves, Majenz, Gross and successors develop entropic cones for causal structures (*Nat. Commun.* 6, 5766, 2015); the aim is an IC statement natural on networks rather than bipartitions.
- **GPT-side characterization.** Work on which generalized probabilistic theories admit a Holevo bound, hence IC, continues (Barnum school, Perimeter, Vienna).
- **Reported unconditional separations between $\mathcal{IC}$ and $\tilde{\mathcal{Q}}$ appearing in 2025–2026 preprints should be treated as unconfirmed.** *(frontier — verify)*

## 8. Future Work

- Find a protocol-independent analytic or SDP characterization of $\mathcal{IC}$; even an outer hierarchy converging to $\mathcal{IC}$ would be a major advance.
- Settle whether $\tilde{\mathcal{Q}}\subseteq\mathcal{IC}$. A positive answer refutes $\mathcal{IC}=\mathcal{Q}$ and redirects the axiomatization programme toward genuinely non-device-independent principles.
- Formulate multipartite IC that excludes the Gallego et al. tripartite correlations.
- Replace Shannon entropy by one-shot/smooth quantities, or by a task-based (guessing-probability) formulation, and test whether the boundary tightens.
- Explore IC in scenarios with more inputs/outputs, $(2,m,d)$, where almost nothing beyond CHSH-type slices is computed.

## 9. Key References

- **[Foundational]** M. Pawłowski, T. Paterek, D. Kaszlikowski, V. Scarani, A. Winter, M. Żukowski. *Information causality as a physical principle.* Nature 461, 1101–1104, 2009.
- **[Foundational]** S. Popescu, D. Rohrlich. *Quantum nonlocality as an axiom.* Foundations of Physics 24, 379–385, 1994.
- **[Foundational]** B. S. Tsirelson. *Quantum generalizations of Bell's inequality.* Letters in Mathematical Physics 4, 93–100, 1980.
- **[Foundational]** W. van Dam. *Implausible consequences of superstrong nonlocality.* Natural Computing 12, 9–12, 2013 (circulated 2000).
- **[Foundational]** G. Brassard, H. Buhrman, N. Linden, A. A. Méthot, A. Tapp, F. Unger. *Limit on nonlocality in any world in which communication complexity is not trivial.* Physical Review Letters 96, 250401, 2006.
- **[SOTA / Recent]** M. Navascués, Y. Guryanova, M. J. Hoban, A. Acín. *Almost quantum correlations.* Nature Communications 6, 6288, 2015.
- **[SOTA / Recent]** N. Miklin, M. Pawłowski. *Information causality without concatenation.* Physical Review Letters 126, 220403, 2021.
- **[SOTA / Recent]** R. Gallego, L. E. Würflinger, A. Acín, M. Navascués. *Quantum correlations require multipartite information principles.* Physical Review Letters 107, 210403, 2011.
- **[SOTA / Recent]** J. Allcock, N. Brunner, M. Pawłowski, V. Scarani. *Recovering part of the boundary between quantum and nonquantum correlations from information causality.* Physical Review A 80, 040103(R), 2009.
- **[SOTA / Recent]** D. Cavalcanti, A. Salles, V. Scarani. *Macroscopically local correlations can violate information causality.* Nature Communications 1, 136, 2010.
- **[SOTA / Recent]** S. W. Al-Safi, A. J. Short. *Information causality from an entropic and a probabilistic perspective.* Physical Review A 84, 042323, 2011.
- **[SOTA / Recent]** H. Barnum, S. Beigi, S. Boixo, M. B. Elliott, S. Wehner. *Local quantum measurement and no-signaling imply quantum correlations.* Physical Review Letters 104, 140401, 2010.
- **[Survey]** N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani, S. Wehner. *Bell nonlocality.* Reviews of Modern Physics 86, 419–478, 2014.
- **[Survey]** M. Pawłowski, V. Scarani. *Information Causality.* In *Quantum Theory: Informational Foundations and Foils*, G. Chiribella and R. W. Spekkens (eds.), Springer, 2016.
- **[Survey]** S. Popescu. *Nonlocality beyond quantum mechanics.* Nature Physics 10, 264–270, 2014.

## 10. Worked Example / Concrete Special Case

**Claim.** IC forces $E \le 1/\sqrt{2}$ for the isotropic box $P_E$, i.e. $\mathrm{CHSH}\le 2\sqrt2$.

*Step 1 — one level.* Alice holds $(a_0,a_1)$, Bob wants $a_b$. They input $x = a_0\oplus a_1$ and $y=b$ into $P_E$, obtaining $a,b'$ with $a\oplus b' = xy$ with probability $p=(1+E)/2$. Alice sends $M = a_0\oplus a$. Bob outputs $\beta = M\oplus b'$. If the box worked, $\beta = a_0 \oplus a \oplus b' = a_0\oplus (a_0\oplus a_1)b = a_b$. So each guess succeeds with probability $p$.

*Step 2 — concatenation.* Recurse $n$ times on a database of $N=2^n$ bits, using $2^n-1$ boxes and still one bit $m=1$. Errors compose by XOR, so writing $E=2p-1$, the level-$n$ success probability is
$$P_n = \frac{1+E^{\,n}}{2}.$$

*Step 3 — entropy.* Each term $I(a_k:\beta|b=k) = 1-h(P_n)$. Summing over the $N=2^n$ values of $b$ and applying the quadratic bound:
$$\mathcal{I} = 2^{n}\bigl[1-h(P_n)\bigr] \;\ge\; 2^{n}\,\frac{E^{2n}}{2\ln 2} \;=\; \frac{(2E^{2})^{n}}{2\ln 2}.$$

*Step 4 — conclusion.* IC demands $\mathcal{I}\le m=1$ for every $n$. If $2E^{2}>1$ the right-hand side diverges as $n\to\infty$, violating IC. Hence
$$E \le \tfrac{1}{\sqrt2} \quad\Longleftrightarrow\quad \mathrm{CHSH} = 4E \le 2\sqrt2 .$$

*Numbers.* For the perfect PR box $E=1$: $\mathcal{I}\ge 2^{n}/(2\ln 2)$, so $n=4$ already gives $\mathcal{I}\ge 11.5$ bits transmitted by one bit. For $E=0.9$ ($\mathrm{CHSH}=3.6$): $2E^2=1.62>1$, and $n=10$ gives $\mathcal{I}\ge 1.62^{10}/(2\ln2)\approx 87$ — violated. For $E=1/\sqrt2$: $2E^2=1$ and the bound saturates at $\mathcal{I}\ge 1/(2\ln 2)\approx 0.72 < 1$ for all $n$ — no violation, exactly at Tsirelson's point.

This is the one slice where IC and $\partial\mathcal{Q}$ provably coincide. Section 6's gap is everything off this line.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*