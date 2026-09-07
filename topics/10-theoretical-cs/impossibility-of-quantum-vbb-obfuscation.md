---
id: 10-theoretical-cs/impossibility-of-quantum-vbb-obfuscation
title: "Impossibility of Quantum Virtual Black Box Obfuscation"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Impossibility of Quantum Virtual Black Box Obfuscation

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/impossibility-of-quantum-vbb-obfuscation` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Barak, Goldreich, Impagliazzo, Rudich, Sahai, Vadhan and Yang (CRYPTO 2001) proved that no *classical* algorithm can turn every Boolean circuit $C$ into a classical program $\mathcal{O}(C)$ that computes the same function and reveals nothing beyond black-box access to it. Their attack is self-referential: it feeds the obfuscated program its own source code.

The quantum question is whether the conclusion survives when the obfuscator may output a **quantum state** $\rho_C$ and the adversary is a quantum polynomial-time (QPT) machine.

**Conjecture (general quantum VBB impossibility).** There is no QPT obfuscator $\mathcal{O}$ mapping circuits to quantum states, together with a QPT evaluator $\mathsf{Eval}$, such that
1. *(functionality)* $\Pr[\mathsf{Eval}(\rho_C, x) = C(x)] \ge 1 - \mathrm{negl}(\lambda)$ for all $x$, with $\rho_C$ reusable a polynomial number of times; and
2. *(virtual black box)* for every QPT adversary $\mathcal{A}$ there is a QPT simulator $\mathcal{S}$ with
$$\Big|\Pr[\mathcal{A}(\rho_C)=1] - \Pr[\mathcal{S}^{C}(1^{|C|})=1]\Big| \le \mathrm{negl}(\lambda),$$
for **every** circuit family — classical or quantum — of interest.

A complete resolution requires either (a) an explicit unobfuscatable family for *quantum* circuits, unconditionally or under a standard assumption, or (b) a construction meeting both conditions for some rich class, which would refute the conjecture in that regime. The classical-circuit case is **settled negatively assuming LWE** (Alagic–Brakerski–Dulek–Schaffner, CRYPTO 2021); the quantum-circuit case and the unconditional case are open.

## 2. Mathematical Foundations

**Circuits and channels.** A classical circuit $C:\{0,1\}^n \to \{0,1\}^m$; a quantum circuit is a CPTP map $\Phi_C: \mathcal{D}(\mathbb{C}^{2^n}) \to \mathcal{D}(\mathbb{C}^{2^m})$ over a universal gate set (e.g. Clifford $+\,T$).

**Quantum obfuscator.** A pair $(\mathcal{O}, \mathsf{Eval})$ where $\mathcal{O}(1^\lambda, C) \to \rho_C \in \mathcal{D}(\mathcal{H})$ with $\dim\mathcal{H} = 2^{\mathrm{poly}(|C|,\lambda)}$, and $\mathsf{Eval}(\rho_C \otimes |x\rangle\langle x|)$ outputs a value plus a residual state $\rho'$.

**Reusability.** Because measurement disturbs, functionality must be stated for $k = \mathrm{poly}(\lambda)$ sequential queries $x_1,\dots,x_k$:
$$\Pr\big[\forall i:\; y_i = C(x_i)\big] \ge 1 - \mathrm{negl}(\lambda).$$
Reusability is *implied* by near-certainty of outcome via the gentle measurement / "almost as good as new" lemma: if a measurement $\{E, I-E\}$ on $\rho$ yields outcome $E$ with probability $1-\varepsilon$, the post-measurement state $\rho'$ satisfies $\|\rho - \rho'\|_{\mathrm{tr}} \le 2\sqrt{\varepsilon}$.

**Barak et al. unobfuscatable family.** For $\alpha,\beta \in \{0,1\}^n$ define
$$C_{\alpha,\beta}(x) = \begin{cases}\beta & x=\alpha\\ 0^n & \text{else}\end{cases},\qquad D_{\alpha,\beta}(Z) = \begin{cases}1 & Z(\alpha)=\beta\\ 0 & \text{else,}\end{cases}$$
where $Z$ is a *program description*. Given classical code for both, an adversary evaluates $D_{\alpha,\beta}$ on the code of $C_{\alpha,\beta}$ and gets $1$; a simulator with oracle access must find $\alpha$ among $2^n$ points and outputs $1$ with probability $\le \mathrm{poly}(\lambda)2^{-n}$. Hence no VBB obfuscator exists.

**Quantum fully homomorphic encryption (QFHE) with classical keys.** $(\mathsf{Gen},\mathsf{Enc},\mathsf{Eval}^{\mathsf{qc}},\mathsf{Dec})$ with classical ciphertexts for classical plaintexts, such that for a quantum circuit $Q$ and auxiliary quantum state $\sigma$,
$$\mathsf{Dec}_{sk}\big(\mathsf{Eval}^{\mathsf{qc}}_{pk}(Q, \sigma, \mathsf{Enc}_{pk}(x))\big) = Q(\sigma, x)$$
with overwhelming probability. Such schemes exist under the quantum hardness of Learning With Errors (Mahadev, FOCS 2018; Brakerski, CRYPTO 2018): for modulus $q$, dimension $n$, error width $\alpha q$, $\mathrm{LWE}_{n,q,\chi}$ is assumed hard for QPT machines with $q/\alpha \le 2^{n^{\varepsilon}}$.

**ABDS attack skeleton.** Replace "run $D$ on the code of $C$" — impossible, since $\rho_C$ has no readable description and cannot be cloned — by "run $\mathsf{Eval}$ on an *encrypted* input, then let $D$ decrypt". The obfuscated $D$ holds $sk$ and outputs its secret only if the ciphertext handed to it decrypts to $\beta$. Each obfuscated state is consumed once, so no-cloning is respected.

## 3. History & State of the Art (SOTA)

- **2001 / 2012.** Barak et al., *On the (Im)possibility of Obfuscating Programs* (CRYPTO 2001; JACM 59(2), 2012): classical VBB impossible; indistinguishability obfuscation (iO) proposed as the fallback.
- **2013–2021.** iO candidates (Garg–Gentry–Halevi–Raykova–Sahai–Waters, FOCS 2013) culminating in iO from well-founded assumptions (Jain–Lin–Sahai, STOC 2021) — none of which is quantum-secure in the JLS form (it uses bilinear maps plus LPN/PRG assumptions).
- **2014.** Alagic–Jeffery–Jordan, *Circuit Obfuscation Using Braids* (TQC 2014): obfuscation of a restricted class via braid-group normal forms.
- **2016.** Alagic–Fefferman, *On Quantum Obfuscation* (arXiv:1602.01771): first systematic definitions (classical vs. quantum programs, classical vs. quantum output; black-box vs. indistinguishability), the observation that the Barak et al. attack **fails** against quantum-state obfuscations, impossibility for the statistically secure and classical-output variants, and reductions showing quantum VBB would yield quantum FHE and one-time programs.
- **2021.** Alagic–Brakerski–Dulek–Schaffner, *Impossibility of Quantum Virtual Black-Box Obfuscation of Classical Circuits* (CRYPTO 2021): the SOTA negative result — assuming quantum-hard LWE, no quantum VBB obfuscator for classical circuits, even with quantum output and even for obfuscators used a bounded number of times.
- **2021–2024.** Positive results retreat to weaker notions: null-circuit iO for quantum circuits (Bartusek–Malavolta, ITCS 2022), low-$T$-count quantum iO (Broadbent–Kazmi, 2020), and *ideal* obfuscation of quantum programs relative to classical oracles (Bartusek–Brakerski–Vaikuntanathan, STOC 2024; Bartusek–Kitagawa–Nishimaki–Yamakawa, STOC 2024).

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| Classical circuits, classical obfuscation, classical adversary | Impossible, unconditional (Barak et al. 2001) |
| Classical circuits, **quantum** obfuscation state, QPT adversary | Impossible **assuming quantum-hard LWE** (ABDS 2021) |
| Classical circuits, quantum obfuscation, *statistical* VBB security | Impossible (Alagic–Fefferman 2016) |
| Obfuscator with classical output, quantum adversary | Impossible, unconditional (Barak et al. attack applies verbatim) |
| Bounded-use obfuscation ($k=2$ uses suffice for the attack) | Covered by ABDS 2021 |
| Approximate functionality (error $\le 1/3$ per input) | Covered by amplification in ABDS 2021 |
| Quantum circuits, general (including non-pseudodeterministic) | **Open** |
| Point functions / compute-and-compare, quantum VBB | Achievable in idealized models; not ruled out |
| Quantum programs relative to a classical oracle | **Possible** — ideal obfuscation exists (BBV 2024) |

Concretely, ABDS instantiate the attack with $n = \lambda$-bit points $\alpha,\beta$, a QFHE scheme with classical ciphertexts of size $\mathrm{poly}(\lambda)$, and a simulator advantage bounded by $q(\lambda)\cdot 2^{-\lambda} + \mathrm{negl}(\lambda)$ for $q$ oracle queries.

## 5. Principal Obstacles

- **No self-reference.** The classical proof needs the adversary to hand the obfuscated program *to itself as input*. A quantum state has no efficiently extractable classical description, and no-cloning forbids duplicating $\rho_C$ to use it as both program and datum. Every classical diagonalization argument (Kleene recursion, Turing self-reference) breaks here.
- **Destructive evaluation.** Even the notion of functionality is unstable: without reusability guarantees, an obfuscation might be correct once and garbage thereafter, and the attack cannot iterate. Bounding disturbance requires gentle-measurement arguments that lose $\sqrt{\varepsilon}$ factors.
- **The LWE crutch.** The only known replacement for self-reference is homomorphic evaluation, which forces the impossibility proof to *assume* a hardness conjecture. This is structurally odd: an impossibility result should not need an assumption, yet without one the adversary has no way to hide its input from the program.
- **Non-pseudodeterministic quantum circuits.** For circuits whose output distribution is genuinely random, "black-box access" itself is ambiguous — does the simulator get one sample, many samples, or the ability to run the inverse map? Different choices yield inequivalent conjectures, and no unobfuscatable family is known for any of them.
- **Quantum auxiliary input.** VBB with quantum auxiliary state $\sigma$ resists simulation-based proofs: the simulator must reproduce entanglement between $\sigma$ and the adversary's workspace, which known rewinding/extraction techniques cannot do (rewinding is obstructed by measurement collapse).

## 6. The Gap

Proven: for the *classical* circuit family $\{C_{\alpha,\beta}\}$, VBB fails against quantum obfuscators, **conditioned on LWE**. Conjectured: failure for *all* circuit families including quantum ones, **unconditionally**.

Two precise steps separate them.

1. **Remove the assumption.** ABDS's adversary needs a way to evaluate $\rho_C$ on an input hidden from the program. QFHE is the only known mechanism. An unconditional proof needs an information-theoretic input-hiding gadget — or a proof that none exists, which would show impossibility of quantum VBB is *equivalent* to a cryptographic assumption. Note the barrier: if one-way functions do not exist, many obfuscation notions become trivially satisfiable in restricted settings, so some assumption may be unavoidable.
2. **Cross to quantum programs.** The attack requires a "checker" circuit $D$ that tests whether a ciphertext decrypts to $\beta$ — a classical predicate on a classical output. For a quantum circuit whose output is a state $|\psi\rangle$, equality testing is only possible via SWAP test with constant soundness and consumes copies. No known family of quantum circuits has both (i) a hard-to-learn secret and (ii) an efficiently checkable relation on quantum outputs robust to one-shot access.

## 7. Current Research (as of June 2026)

- **Ideal obfuscation for quantum programs.** Bartusek–Brakerski–Vaikuntanathan (STOC 2024) obfuscate pseudodeterministic quantum programs relative to a classical oracle, achieving full VBB-style security in that model; Bartusek–Kitagawa–Nishimaki–Yamakawa (STOC 2024) do so for pseudodeterministic circuits under LWE plus indistinguishability obfuscation. These are *positive* results that co-exist with ABDS precisely because the obfuscated object is a quantum state whose evaluation is pseudodeterministic and the model is idealized. Delimiting exactly which quantum classes escape is the active frontier.
- **Quantum iO.** Coladangelo–Gunn (STOC 2024) develop applications of "quantum state iO"; whether any candidate is secure remains open. *(frontier — verify)*
- **Copy-protection / unclonable cryptography.** Ananth–La Placa (EUROCRYPT 2021) rule out general quantum copy-protection using techniques close in spirit to ABDS; the shared toolkit (QFHE + compute-and-compare obfuscation) is being pushed toward broader no-go theorems. Groups at QuICS/Maryland (Alagic), Weizmann (Brakerski), QuSoft/Amsterdam (Schaffner, Dulek), NTT/AIST (Nishimaki, Yamakawa) and Berkeley/NYU are the principal centers.
- **Unconditional variants.** Attempts to derive impossibility from the no-cloning theorem alone, without LWE, have so far produced only results for restricted evaluator interfaces. *(frontier — verify)*

## 8. Future Work

- Construct an unobfuscatable family of **quantum** circuits, e.g. based on pseudorandom state generators, where the "checker" performs a SWAP test amplified by parallel repetition on independently obfuscated copies.
- Prove an assumption-necessity theorem: quantum VBB impossibility for classical circuits implies the existence of one-way functions (or QFHE-like primitives), formalizing the intuition that the ABDS proof cannot be made unconditional.
- Settle the auxiliary-input version: does quantum VBB with *quantum* auxiliary input fail even for point functions?
- Map the exact boundary of the BBV/BKNY positive results: is pseudodeterminism necessary, or can sampling circuits be obfuscated relative to classical oracles?
- Determine whether quantum iO for all quantum circuits is achievable from post-quantum assumptions, and whether "best-possible obfuscation" (Goldwasser–Rothblum, TCC 2007) has a meaningful quantum analogue.

## 9. Key References

- **[Foundational]** B. Barak, O. Goldreich, R. Impagliazzo, S. Rudich, A. Sahai, S. Vadhan, K. Yang. *On the (Im)possibility of Obfuscating Programs.* CRYPTO 2001; journal version, Journal of the ACM 59(2), Article 6, 2012.
- **[Foundational]** G. Alagic, B. Fefferman. *On Quantum Obfuscation.* arXiv:1602.01771, 2016.
- **[SOTA]** G. Alagic, Z. Brakerski, Y. Dulek, C. Schaffner. *Impossibility of Quantum Virtual Black-Box Obfuscation of Classical Circuits.* CRYPTO 2021, LNCS 12825, Springer.
- **[SOTA / Recent]** J. Bartusek, Z. Brakerski, V. Vaikuntanathan. *Quantum State Obfuscation from Classical Oracles.* STOC 2024.
- **[SOTA / Recent]** J. Bartusek, F. Kitagawa, R. Nishimaki, T. Yamakawa. *Obfuscation of Pseudo-Deterministic Quantum Circuits.* STOC 2024.
- **[Tools]** U. Mahadev. *Classical Homomorphic Encryption for Quantum Circuits.* FOCS 2018; SIAM Journal on Computing 52(6), 2020.
- **[Tools]** Z. Brakerski. *Quantum FHE (Almost) As Secure As Classical.* CRYPTO 2018, LNCS 10993.
- **[Related]** P. Ananth, R. L. La Placa. *Secure Software Leasing.* EUROCRYPT 2021, LNCS 12697.
- **[Related]** J. Bartusek, G. Malavolta. *Indistinguishability Obfuscation of Null Quantum Circuits and Applications.* ITCS 2022.
- **[Related]** A. Broadbent, R. A. Kazmi. *Indistinguishability Obfuscation for Quantum Circuits of Low T-count.* IACR ePrint 2020/639.
- **[Related]** A. Jain, H. Lin, A. Sahai. *Indistinguishability Obfuscation from Well-Founded Assumptions.* STOC 2021.
- **[Survey]** B. Barak. *Hopes, Fears, and Software Obfuscation.* Communications of the ACM 59(3), 2016.
- **[Survey]** S. Goldwasser, G. N. Rothblum. *On Best-Possible Obfuscation.* TCC 2007; Journal of Cryptology 27(3), 2014.

## 10. Worked Example / Concrete Special Case

**Setup.** Take $n=2$ for readability; the real proof uses $n=\lambda$. Fix $\alpha = 10$, $\beta = 11$. Define
$$C(x) = \begin{cases} 11 & x = 10\\ 00 & x \in \{00,01,11\}\end{cases}$$
and a checker $D_{sk}(c)$ that computes $\mathsf{Dec}_{sk}(c)$ and outputs the secret $s = 1$ iff the result equals $11$, else $0$.

**Why the classical attack dies.** The adversary receives states $\rho_C$ and $\rho_D$, not code. It cannot write $\rho_C$ on $D$'s input tape: reading $\rho_C$ in a fixed basis destroys it, and cloning it is forbidden since $\mathcal{O}$ is randomized, so $\{\rho_C\}$ contains non-orthogonal states.

**The ABDS attack, step by step.**

1. Sample $(pk,sk) \leftarrow \mathsf{Gen}(1^\lambda)$ **inside** the obfuscated $D$; i.e. the family being obfuscated is $\{(C_{\alpha,\beta}, D_{sk})\}$ with $\alpha$ encrypted: the adversary is handed $\hat{\alpha} = \mathsf{Enc}_{pk}(\alpha) = \mathsf{Enc}_{pk}(10)$ and $pk$ as public data.
2. Run homomorphic evaluation of the *evaluation circuit* $\mathsf{Eval}(\cdot,\cdot)$ with plaintext quantum auxiliary state $\rho_C$ and encrypted input $\hat\alpha$:
$$\hat{y} \leftarrow \mathsf{Eval}^{\mathsf{qc}}_{pk}\big(\mathsf{Eval},\; \rho_C,\; \hat{\alpha}\big),\qquad \mathsf{Dec}_{sk}(\hat y) = C(\alpha) = 11 .$$
This consumes $\rho_C$ exactly once — no cloning, no measurement of the program in a basis it does not tolerate.
3. Feed the *classical* ciphertext $\hat y$ to the second obfuscation: $\mathsf{Eval}(\rho_D, \hat y) = D_{sk}(\hat y) = 1$.
4. The adversary outputs $1$ with probability $1-\mathrm{negl}(\lambda)$.

**Simulator bound.** A simulator $\mathcal{S}$ has oracle access to $C$ and $D_{sk}$ and holds $\hat\alpha$. To make $D_{sk}$ output $1$ it must submit a ciphertext decrypting to $\beta$. Two routes are open, both blocked:
- Query $C$ at $\alpha$: by semantic security of the QFHE scheme, $\hat\alpha$ hides $\alpha$, so after $q$ queries $\Pr[\text{hit}] \le q\,2^{-n} + \mathrm{negl}(\lambda)$.
- Forge an encryption of $\beta$ without knowing $\beta$: probability $\le q\,2^{-n}$, since $\beta$ is uniform and independent of the adversary's view.

Hence $|\Pr[\mathcal{A}=1] - \Pr[\mathcal{S}^{C,D}=1]| \ge 1 - 2q\,2^{-n} - \mathrm{negl}(\lambda)$, which is non-negligible. No quantum VBB obfuscator for this classical family exists under LWE. $\blacksquare$

**Where it stops.** Replace $C$ by a quantum circuit outputting a state $|\psi_\alpha\rangle$ rather than a bit string. Step 3 now requires $D$ to test $|\psi_\alpha\rangle$ against a reference — but the ciphertext $\hat y$ is a quantum ciphertext, decryption yields one copy, and a SWAP test succeeds with probability $\tfrac12(1+|\langle\psi|\phi\rangle|^2)$, giving only constant soundness with no way to amplify from a single use. That single missing amplification step is the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*