---
id: 10-theoretical-cs/indistinguishability-obfuscation-construction
title: "Indistinguishability Obfuscation Construction"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Indistinguishability Obfuscation Construction

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/indistinguishability-obfuscation-construction` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Can a program be scrambled so that its code reveals nothing beyond its input–output behaviour, and can this be done from standard cryptographic hardness assumptions?

The precise target is **indistinguishability obfuscation (iO)**: a probabilistic polynomial-time algorithm $i\mathcal{O}$ that takes a Boolean circuit $C$ and outputs a circuit $i\mathcal{O}(C)$ computing the same function, such that for any two *functionally equivalent* circuits of the same size, the obfuscations are computationally indistinguishable.

Three distinct questions sit under this heading.

1. **Existence from well-founded assumptions.** Does iO for all polynomial-size circuits follow from assumptions that predate iO and have survived independent cryptanalysis? **Answered yes** by Jain–Lin–Sahai (STOC 2021), from a conjunction of four assumptions. This is why the status is `solved-recently`.
2. **Existence from a single standard assumption**, or from a post-quantum-plausible assumption (e.g. LWE alone). **Open.**
3. **Practical efficiency.** Current constructions have obfuscation size and running time polynomial in the circuit size with astronomically large polynomial factors. **Open.**

A complete resolution of (2) means either a construction with a full reduction to a single, cryptanalysed assumption, or an unconditional impossibility (which would imply $\mathsf{P} \ne \mathsf{NP}$, so only conditional impossibility is achievable).

## 2. Mathematical Foundations

**Definition (iO; Barak et al. 2001).** A uniform PPT $i\mathcal{O}$ is an indistinguishability obfuscator for a circuit class $\{\mathcal{C}_\lambda\}$ if:

*Functionality.* For all $\lambda$, all $C \in \mathcal{C}_\lambda$, all inputs $x$,
$$\Pr\big[\,C'(x) = C(x) \ :\ C' \leftarrow i\mathcal{O}(1^\lambda, C)\,\big] = 1 .$$

*Indistinguishability.* For every PPT distinguisher $D$ there is a negligible $\mathrm{negl}$ such that for all $\lambda$ and all $C_0, C_1 \in \mathcal{C}_\lambda$ with $|C_0| = |C_1|$ and $C_0(x) = C_1(x)$ for every $x$,
$$\Big|\Pr\big[D(i\mathcal{O}(1^\lambda,C_0)) = 1\big] - \Pr\big[D(i\mathcal{O}(1^\lambda,C_1)) = 1\big]\Big| \le \mathrm{negl}(\lambda).$$

*Efficiency.* $|i\mathcal{O}(1^\lambda,C)| \le \mathrm{poly}(\lambda, |C|)$.

**Why the weak-looking definition is strong.** Goldwasser–Rothblum (TCC 2007) showed iO is *best-possible* obfuscation: if any obfuscator leaks nothing beyond a given amount, iO leaks no more. Sahai–Waters (STOC 2014) turned iO $+$ one-way functions into public-key encryption, deniable encryption, NIZKs, and much of cryptography, via *punctured programming*.

**Puncturable PRFs.** A PRF family $F: \{0,1\}^\lambda \times \{0,1\}^n \to \{0,1\}^m$ is puncturable if there is $\mathrm{Punc}(K,x^*) \to K\{x^*\}$ with $F(K\{x^*\},x) = F(K,x)$ for $x \ne x^*$, and
$$\big(K\{x^*\},\, F(K,x^*)\big) \;\approx_c\; \big(K\{x^*\},\, u\big),\qquad u \leftarrow \{0,1\}^m .$$
The GGM construction from any PRG gives this.

**The reduction chain used by all modern constructions.**
$$\text{sublinear FE} \;\Longrightarrow\; \text{iO}.$$
A public-key functional encryption scheme has $\mathrm{Enc}(\mathrm{pk},m)$ and keys $\mathrm{sk}_f$ with $\mathrm{Dec}(\mathrm{sk}_f,\mathrm{ct}) = f(m)$. It is *sublinearly compact* if
$$|\mathrm{ct}| \le |f|^{1-\varepsilon}\cdot \mathrm{poly}(\lambda, |m|)\quad\text{for some }\varepsilon>0 .$$
Ananth–Jain (CRYPTO 2015) and Bitansky–Vaikuntanathan (FOCS 2015) showed sublinear FE for $\mathsf{NC}^1$ implies iO (with subexponential security loss).

**The JLS21 assumption set.** iO for all circuits follows from the conjunction of:

- **SXDH** on asymmetric bilinear groups $e: G_1 \times G_2 \to G_T$ of prime order $p$;
- **LWE**: $(\mathbf{A}, \mathbf{s}^\top\mathbf{A} + \mathbf{e}^\top) \approx_c (\mathbf{A}, \mathbf{u}^\top)$ over $\mathbb{Z}_q$ with subexponential modulus-to-noise ratio;
- **LPN over $\mathbb{F}_p$** for a large prime $p$, dimension $\ell$, $m = \ell^{1+\varepsilon}$ samples, and inverse-polynomial error rate $\delta = \ell^{-\eta}$ for suitable constants: $(\mathbf{A}, \mathbf{s}^\top\mathbf{A} + \mathbf{e}^\top)$ with $\mathbf{e}$ sparse (each coordinate nonzero with probability $\delta$) is pseudorandom;
- **Boolean PRGs in $\mathsf{NC}^0$** with polynomial stretch: $G:\{0,1\}^n \to \{0,1\}^{n^{1+\tau}}$, each output bit depending on $O(1)$ input bits (Goldreich's local PRG).

Jain–Lin–Sahai (STOC 2022) removed the extra structure of the "structured-seed PRG" step and gave iO from **LPN over $\mathbb{F}_p$, DLIN over bilinear maps, and $\mathsf{NC}^0$ PRGs**.

**Impossibility landmark.** Barak, Goldreich, Impagliazzo, Rudich, Sahai, Vadhan, Yang (CRYPTO 2001; JACM 2012) proved *virtual black-box* obfuscation is impossible for general circuits: there is a family $\{C_{\alpha,\beta}\}$ that is unlearnable from oracle access but whose code lets an adversary output $\beta$ — because $C$ can be fed to itself. iO evades this by never claiming simulation.

## 3. History & State of the Art (SOTA)

- **2001.** Barak et al. define iO as the fallback after ruling out VBB. No candidate is given; iO is widely suspected to be unachievable.
- **2013.** Garg, Gentry, Halevi, Raykova, Sahai, Waters (FOCS 2013) give the first candidate, via *branching programs* obfuscated over the GGH13 multilinear map, with a bootstrapping step from $\mathsf{NC}^1$ to $\mathsf{P}/\mathrm{poly}$ using FHE. Security rests on an unfalsifiable-flavoured assumption about the graded encoding.
- **2014.** Sahai–Waters establish iO as a "central hub": punctured programming yields most of cryptography.
- **2015–2016.** Cryptanalysis: Cheon, Han, Lee, Ryu, Stehlé (EUROCRYPT 2015) break CLT13 by *zeroizing*; Miles, Sahai, Zhandry (CRYPTO 2016) give *annihilation attacks* on GGH13-based obfuscators. Multiple candidates fall.
- **2016–2020.** Degree reduction: Lin (EUROCRYPT 2016, CRYPTO 2017), Lin–Vaikuntanathan (FOCS 2016), Ananth–Sahai, Lin–Tessaro (CRYPTO 2017) push the required multilinearity from $\mathrm{poly}(\lambda)$ down to constant, then to 3 — but the degree-3 route needed block-local PRGs, broken by Barak, Brakerski, Komargodski, Kothari (EUROCRYPT 2018) and Lombardi–Vaikuntanathan (TCC 2017).
- **2020–2021.** Jain, Lin, Sahai, *Indistinguishability Obfuscation from Well-Founded Assumptions* (STOC 2021) closes the main question. Independently, Gay–Pass (STOC 2021) obtain iO from circular security of LWE-based FHE + SXDH; Brakerski, Döttling, Garg, Malavolta (EUROCRYPT 2020) from circular-secure LWE with a rerandomizable encryption.
- **2021–2025.** Hopkins, Jain, Lin (STOC 2021) give counterexamples to some new circular-security assumptions, narrowing the LWE-only route. Ragavan, Vafa, Vaikuntanathan (TCC 2024) build iO from bilinear maps and LPN variants, further simplifying assumptions.

**SOTA summary.** iO for $\mathsf{P}/\mathrm{poly}$ exists under a small conjunction of pre-iO assumptions with subexponential security. No construction is post-quantum (bilinear maps break under Shor). No construction is remotely practical.

## 4. Partial Results / Verified Cases

- **Full circuits, subexponential assumptions:** iO for all polynomial-size circuits from $\{$SXDH, LWE, LPN over $\mathbb{F}_p$, $\mathsf{NC}^0$ PRG$\}$ (JLS21), and from $\{$DLIN, LPN over $\mathbb{F}_p$, $\mathsf{NC}^0$ PRG$\}$ (JLS22).
- **Restricted classes with clean proofs:** *evasive* function families — point functions $I_\alpha$, conjunctions, hyperplane membership — admit VBB-style obfuscation from LWE or generic groups, unconditionally in the ROM for point functions (Lynn–Prabhakaran–Sahai, EUROCRYPT 2004; Wichs–Zirdelis, FOCS 2018; Bishop, Kowalczyk, Malkin, Pastro, Raykova, Shi, CRYPTO 2018).
- **Compute-and-compare / lockable obfuscation:** obfuscation of $f(x) = \beta$ if $g(x) = \alpha$, else $\bot$, from LWE with polynomial modulus (Wichs–Zirdelis FOCS 2018; Goyal–Koppula–Waters FOCS 2017). Post-quantum secure.
- **Bootstrapping thresholds:** iO for $\mathsf{NC}^1$ $\Rightarrow$ iO for $\mathsf{P}/\mathrm{poly}$ given LWE-based FHE. iO for circuits of depth $O(\log \lambda)$ and constant-degree computations over $\mathbb{Z}_p$ suffices.
- **Degree parameters:** iO from constant-degree multilinear maps ($L \ge 3$) is known modulo PRG assumptions that were then attacked at block-locality $\le 2$; local PRGs of locality 5 with stretch $n^{1.1}$ remain unbroken but are attacked for stretch $\gtrsim n^{1.5}$ at low locality.
- **Idealized models:** VBB obfuscation for branching programs is provable in the generic multilinear-map model (Barak, Garg, Kalai, Paneth, Sahai, EUROCRYPT 2014).

## 5. Principal Obstacles

- **VBB impossibility is structural, not technical.** Self-referential circuits defeat any simulation-based definition, so no proof technique can strengthen iO to VBB for general circuits.
- **iO cannot be proven from one-way functions alone in a black-box way.** iO implies $\mathsf{NP} \not\subseteq \mathsf{io\text{-}BPP}$ (assuming OWFs), so any construction needs structured hardness; and iO plus OWFs implies $\mathsf{PPAD}$-hardness and the collapse of many worlds, so the assumption cannot be "cheap".
- **The multilinear-map barrier.** Every candidate graded encoding scheme (GGH13, CLT13, GGH15) leaks low-level encodings of zero; zeroizing and annihilation attacks exploit that the *ring* structure of the encoding survives, turning honest evaluations into algebraic relations solvable by lattice reduction. No candidate has a security reduction to a simple assumption.
- **Non-linear error growth.** LWE-based routes need to evaluate a degree-$d$ polynomial on encrypted data while keeping noise below the modulus; iO needs $d$ growing with the circuit, which forces circular security or superpolynomial modulus, where LWE hardness is weakest.
- **Sublinearity is a knife edge.** FE with $|\mathrm{ct}| = \mathrm{poly}(\lambda)\cdot|f|$ is easy from LWE; shaving the exponent to $|f|^{1-\varepsilon}$ is what requires the whole JLS machinery. There is no smooth interpolation: linear compactness gives nothing.
- **Subexponential loss.** The FE-to-iO bootstrap loses a $2^{n}$ factor over the input length via hybrid arguments over all $2^n$ inputs, forcing subexponential assumptions and $\lambda$ in the thousands.

## 6. The Gap

Proven (Section 4): iO from a *conjunction* of four assumptions, all classical-hardness-based, with subexponential security and impractical parameters.

Target (Section 1, parts 2–3): iO from a *single* well-studied assumption — ideally LWE — with polynomial security loss and usable parameters.

The exact barrier: current constructions use bilinear maps to evaluate degree-2 polynomials *in the exponent* on committed secrets, and LPN to hide the degree-2 "noise" terms. Removing bilinear maps means finding another way to publicly evaluate a quadratic form on hidden values while keeping the result pseudorandom. The candidate replacement is *evasive LWE* or circular security of FHE, but Hopkins–Jain–Lin (STOC 2021) exhibited counterexamples to several natural formulations, and later work has found counterexamples to strong evasive-LWE variants. The open step is to state an LWE-flavoured assumption strong enough to give sublinear FE and weak enough to survive these counterexample families.

## 7. Current Research (as of June 2026)

- **Post-quantum iO.** Groups at MIT (Vaikuntanathan), NTT/Kyoto, and Weizmann pursue succinct LWE sampling, evasive LWE, and homomorphic pseudorandom functions. Devadas, Quach, Vaikuntanathan, Wee, Wichs (TCC 2021) reduce iO to a succinct-randomised-encoding-style LWE sampling assumption; the assumption remains uncryptanalysed. *(frontier — verify)*
- **Assumption pruning.** Ragavan–Vafa–Vaikuntanathan (TCC 2024) obtain iO from bilinear maps plus LPN variants; follow-ups aim to drop the $\mathsf{NC}^0$ PRG. *(frontier — verify)*
- **Cryptanalysis of Goldreich's PRG.** Groups at Weizmann, Tel Aviv, and ENS study whether locality-5 predicates (e.g. $\mathrm{XOR}_3 \oplus \mathrm{AND}_2$) resist SDP and algebraic attacks at stretch $n^{1+\tau}$; the tolerable $\tau$ directly sets iO's parameters.
- **Efficiency.** Work on obfuscating narrow classes (branching programs, matrix products, keyed pseudorandom evaluations) with concrete parameters, rather than general $\mathsf{P}/\mathrm{poly}$.
- **Consequences.** Continued mining of iO for hardness results: $\mathsf{PPAD}$-hardness, hardness of Nash, succinct arguments, and the Sahai–Waters-style deniable-encryption family.

## 8. Future Work

- Construct sublinear FE directly from LWE with polynomial modulus, avoiding bilinear maps entirely.
- Find a falsifiable, non-interactive assumption implying iO with a *polynomial* security reduction, removing the subexponential loss in the FE-to-iO bootstrap.
- Settle the cryptanalysis of constant-locality PRGs at polynomial stretch — a break would invalidate JLS21's assumption set as stated.
- Prove or refute conditional impossibility: does iO with polynomial-time obfuscation and *linear* blow-up contradict any standard assumption?
- Build an implementable obfuscator for a nontrivial keyed class (e.g. AES with an embedded key) with parameters under $2^{40}$ bits.

## 9. Key References

- **[Foundational]** B. Barak, O. Goldreich, R. Impagliazzo, S. Rudich, A. Sahai, S. Vadhan, K. Yang. *On the (Im)possibility of Obfuscating Programs.* CRYPTO 2001; Journal of the ACM 59(2), 2012.
- **[Foundational]** S. Garg, C. Gentry, S. Halevi, M. Raykova, A. Sahai, B. Waters. *Candidate Indistinguishability Obfuscation and Functional Encryption for All Circuits.* FOCS 2013; SIAM J. Computing 45(3), 2016.
- **[Foundational]** A. Sahai, B. Waters. *How to Use Indistinguishability Obfuscation: Deniable Encryption, and More.* STOC 2014.
- **[SOTA]** A. Jain, H. Lin, A. Sahai. *Indistinguishability Obfuscation from Well-Founded Assumptions.* STOC 2021.
- **[SOTA]** A. Jain, H. Lin, A. Sahai. *Indistinguishability Obfuscation from LPN over $\mathbb{F}_p$, DLIN, and PRGs in $NC^0$.* EUROCRYPT 2022.
- **[SOTA]** S. Ragavan, N. Vafa, V. Vaikuntanathan. *Indistinguishability Obfuscation from Bilinear Maps and LPN Variants.* TCC 2024.
- **[Recent]** R. Gay, R. Pass. *Indistinguishability Obfuscation from Circular Security.* STOC 2021.
- **[Recent]** S. Hopkins, A. Jain, H. Lin. *Counterexamples to New Circular Security Assumptions Underlying iO.* CRYPTO 2021.
- **[Cryptanalysis]** J. H. Cheon, K. Han, C. Lee, H. Ryu, D. Stehlé. *Cryptanalysis of the Multilinear Map over the Integers.* EUROCRYPT 2015.
- **[Cryptanalysis]** E. Miles, A. Sahai, M. Zhandry. *Annihilation Attacks for Multilinear Maps: Cryptanalysis of Indistinguishability Obfuscation over GGH13.* CRYPTO 2016.
- **[Survey]** S. Halevi. *Graded Encoding, Variations on a Scheme.* IACR ePrint 2015/866.
- **[Survey]** H. Lin. *Indistinguishability Obfuscation from Constant-Degree Graded Encoding Schemes.* EUROCRYPT 2016.
- **[Book]** O. Goldreich. *Foundations of Cryptography, Vol. 1–2.* Cambridge University Press, 2001/2004.

## 10. Worked Example / Concrete Special Case

**Public-key encryption from iO and a puncturable PRF** (Sahai–Waters), the smallest complete use of the definition.

Let $G:\{0,1\}^\lambda \to \{0,1\}^{2\lambda}$ be a length-doubling PRG and $F$ a puncturable PRF with domain $\{0,1\}^{2\lambda}$ and range $\{0,1\}$.

- **KeyGen:** sample $K \leftarrow \{0,1\}^\lambda$. Secret key is $K$. Public key is
  $$\mathrm{pk} = i\mathcal{O}(P_K),\qquad P_K(r,b) = \big(\,G(r),\ F(K,G(r)) \oplus b\,\big).$$
- **Enc$(\mathrm{pk},b)$:** pick $r \leftarrow \{0,1\}^\lambda$, output $\mathrm{pk}(r,b) = (c_1,c_2)$.
- **Dec$(K,(c_1,c_2))$:** output $c_2 \oplus F(K,c_1)$. Correct since $c_1 = G(r)$.

*Security, three hybrids.*

1. **$H_0$:** real game, challenge $(G(r^*), F(K,G(r^*)) \oplus b)$.
2. **$H_1$:** replace $G(r^*)$ by uniform $t^* \leftarrow \{0,1\}^{2\lambda}$. Indistinguishable by PRG security. Now $t^*$ lies outside the image of $G$ except with probability $\le 2^{\lambda}/2^{2\lambda} = 2^{-\lambda}$.
3. **$H_2$:** replace $\mathrm{pk}$ by $i\mathcal{O}(P'_{K\{t^*\}})$, where $P'$ uses the punctured key $K\{t^*\}$ and is padded to $|P_K|$. Since $t^*$ has no preimage under $G$, the programs $P_K$ and $P'_{K\{t^*\}}$ agree on **every** input $(r,b)$: the punctured point is never queried. They are functionally equivalent and equal-size, so
   $$i\mathcal{O}(P_K) \approx_c i\mathcal{O}(P'_{K\{t^*\}})$$
   *by the iO definition alone.*
4. In $H_2$ the adversary holds $K\{t^*\}$ but not $F(K,t^*)$; punctured-PRF security replaces $F(K,t^*)$ by a uniform bit, so $c_2$ is a one-time pad on $b$ and the advantage is $0$.

Total advantage $\le \mathrm{Adv}^{\mathrm{PRG}} + \mathrm{Adv}^{i\mathcal{O}} + \mathrm{Adv}^{\mathrm{pPRF}} + 2^{-\lambda}$.

**What this shows.** The single load-bearing step is step 3, where two circuits that differ *in code* — one carries $K$, the other $K\{t^*\}$ — are equal *as functions*, so iO's weak guarantee suffices. Every known iO construction must make that step hold while $P_K$ ranges over arbitrary polynomial-size circuits; the JLS21 machinery exists solely to deliver it from LPN, LWE, bilinear maps and local PRGs.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*