---
id: 10-theoretical-cs/am-versus-np-derandomization
title: "Nisan–Wigderson Derandomization of AM"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nisan–Wigderson Derandomization of AM

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/am-versus-np-derandomization` · **Status:** open

## 1. Problem Statement / Conjecture

Arthur–Merlin protocols ($\mathsf{AM}$) are one-round public-coin interactive proofs. The conjecture is that they buy nothing over ordinary nondeterminism:

$$\mathsf{AM} = \mathsf{NP}.$$

The Nisan–Wigderson (NW) programme proposes to prove this *conditionally*, by converting a circuit lower bound into a pseudorandom generator that fools the verifier's randomness. The target statement is the unconditional collapse; the conditional statement whose hypothesis is itself open is:

> **Hypothesis (H).** There is a language in $\mathsf{E}^{\mathsf{NP}} = \mathsf{DTIME}(2^{O(n)})^{\mathsf{NP}}$ that requires *nondeterministic* circuits of size $2^{\Omega(n)}$.

Shaltiel–Umans (2005) proved $\text{(H)} \Rightarrow \mathsf{AM} = \mathsf{NP}$. Two things remain open: (i) proving (H), or any unconditional nondeterministic circuit lower bound strong enough to drive the generator; and (ii) removing the hypothesis, i.e. deriving $\mathsf{AM}=\mathsf{NP}$ from a *uniform* assumption or unconditionally.

A complete resolution is either a proof that $\mathsf{AM}=\mathsf{NP}$, or a proof that $\mathsf{AM} \neq \mathsf{NP}$ (which would separate $\mathsf{NP}$ from $\mathsf{coNP}$-flavoured counting classes and is widely believed false).

## 2. Mathematical Foundations

**Arthur–Merlin.** $L \in \mathsf{AM}$ iff there is a polynomial-time predicate $V$ and polynomials $m,\ell$ with
$$x \in L \;\Longrightarrow\; \Pr_{r \sim \{0,1\}^{m}}\big[\exists y \in \{0,1\}^{\ell} : V(x,r,y)=1\big] \ge 1-2^{-n},$$
$$x \notin L \;\Longrightarrow\; \Pr_{r \sim \{0,1\}^{m}}\big[\exists y : V(x,r,y)=1\big] \le 2^{-n}.$$
Write $A_x = \{r : \exists y\, V(x,r,y)=1\}$. Crucially $A_x$ is decided by a *nondeterministic* circuit $C_x$ of size $\mathrm{poly}(n)$, so its complement is decided by a co-nondeterministic circuit.

**Known containments.** $\mathsf{NP} \subseteq \mathsf{MA} \subseteq \mathsf{AM} \subseteq \Pi_2^p$, and $\mathsf{AM} \subseteq \mathsf{NP}/\mathrm{poly}$. Also $\mathsf{AM} \cap \mathsf{coAM}$ contains Graph Isomorphism, and $\mathsf{AM}[k] = \mathsf{AM}[2]$ for constant $k$ (Babai–Moran).

**Generators.** $G:\{0,1\}^{s} \to \{0,1\}^{m}$ *fools* a circuit class $\mathcal{C}$ with error $\varepsilon$ if for all $C \in \mathcal{C}$ of size $m$,
$$\Big|\Pr_{z}[C(G(z))=1] - \Pr_{r}[C(r)=1]\Big| \le \varepsilon .$$
To derandomize $\mathsf{AM}$ it suffices to fool *co-nondeterministic* circuits: the resulting $\mathsf{NP}$ algorithm guesses witnesses $y_z$ for every seed $z \in \{0,1\}^{s}$ and accepts iff $V(x, G(z), y_z)=1$ for at least a $2/3$ fraction of seeds. This runs in time $2^{s}\cdot\mathrm{poly}(n)$, i.e. polynomial when $s = O(\log m)$.

**NW construction.** Let $S_1,\dots,S_m \subseteq [s]$ be a *combinatorial design*: $|S_i| = n$ and $|S_i \cap S_j| \le \log m$ for $i \ne j$; such designs exist with $s = O(n^2/\log m)$. For $f:\{0,1\}^n \to \{0,1\}$,
$$G^{f}(z) \;=\; \big(f(z|_{S_1}),\, f(z|_{S_2}),\, \dots,\, f(z|_{S_m})\big).$$

**Hybrid/reconstruction theorem.** If $C$ distinguishes $G^f(U_s)$ from $U_m$ with advantage $\varepsilon$, then there is $i$ and a circuit $P$ of size $\mathrm{size}(C) + m\cdot 2^{\log m}$, built from $C$ plus hardwired restrictions, with
$$\Pr_{w}[P(w) = f(w)] \ge \tfrac12 + \tfrac{\varepsilon}{m}.$$
The predictor $P$ is built from $C$ *and its negation*. This is the whole difficulty: if $C$ is nondeterministic, $\neg C$ is not.

**Single-valued nondeterministic (SV-nondeterministic) circuits.** A circuit $C(w,g)$ with guess input $g$ computes $f$ single-valuedly if for all $w$ some $g$ makes $C$ output a value, and every output produced equals $f(w)$ (a $\mathsf{NP}\cap\mathsf{coNP}$-style circuit). Hardness against this model is what NW reconstruction actually needs, and it is the model in Hypothesis (H).

## 3. History & State of the Art (SOTA)

- **1985–86.** Babai introduces Arthur–Merlin games; Goldwasser–Sipser show private coins add no power, putting Graph Non-Isomorphism in $\mathsf{AM}$.
- **1988/1994.** Nisan and Wigderson, *Hardness vs. Randomness*, give the design-based generator and the hardness-to-randomness paradigm for $\mathsf{BPP}$.
- **1993.** Babai, Fortnow, Nisan, Wigderson: $\mathsf{BPP}$ has subexponential simulations unless $\mathsf{EXP}$ has publishable proofs — first uniform-flavoured tradeoff.
- **1997.** Impagliazzo–Wigderson: $\mathsf{E} \not\subseteq \mathrm{SIZE}(2^{o(n)}) \Rightarrow \mathsf{P}=\mathsf{BPP}$ (worst-case to average-case hardness amplification).
- **1999–2002.** Klivans–van Melkebeek show the NW framework relativizes to oracle circuits, yielding: $\mathsf{E}^{\mathsf{NP}}$ requires $2^{\Omega(n)}$-size *oracle* circuits $\Rightarrow \mathsf{AM}=\mathsf{NP}$; and Graph Non-Isomorphism has subexponential-size proofs unless $\mathsf{PH}$ collapses.
- **2005.** Miltersen–Vinodchandran replace pseudorandom generators by *hitting-set* generators for $\mathsf{AM}$, weakening the hypothesis to hardness against $\mathsf{NP}$-type (nondeterministic) circuits and removing the oracle-circuit overhead.
- **2005–06.** Shaltiel–Umans give a direct construction: a function in $\mathsf{E}^{\mathsf{NP}}$ hard for SV-nondeterministic circuits of size $2^{\Omega(n)}$ yields $\mathsf{AM}=\mathsf{NP}$; their machinery ("pseudorandomness for approximate counting and sampling") also derandomizes $\mathsf{AM}$-type approximate counting.
- **2003–2009.** Gutfreund–Shaltiel–Ta-Shma and Shaltiel–Umans obtain *uniform* tradeoffs: e.g. if $\mathsf{NE}\cap\mathsf{coNE}$ requires nondeterministic time $2^{\Omega(n)}$ on average, then $\mathsf{AM} \subseteq$ i.o.-$\mathsf{NP}$-subexponential.
- **2017.** Aydınlıoğlu–van Melkebeek prove a converse: even mild derandomization of $\mathsf{AM}$ implies nondeterministic circuit lower bounds for $\mathsf{NEXP}$-level classes. Derandomizing $\mathsf{AM}$ is thus *equivalent* to proving lower bounds, not merely implied by them.

## 4. Partial Results / Verified Cases

- **Full conditional collapse.** $\text{(H)} \Rightarrow \mathsf{AM}=\mathsf{NP}$ (Shaltiel–Umans 2005; Miltersen–Vinodchandran 2005; Klivans–van Melkebeek 2002 for the oracle-circuit version).
- **Low-end tradeoff.** If $\mathsf{E}^{\mathsf{NP}}$ requires SV-nondeterministic circuits of size $n^{\omega(1)}$ (superpolynomial, not exponential), then $\mathsf{AM} \subseteq \bigcap_{\varepsilon>0} \mathsf{NTIME}(2^{n^{\varepsilon}})$ — subexponential-time nondeterministic simulation.
- **Specific languages.** Graph Non-Isomorphism on $n$-vertex graphs has $\mathsf{NP}$ proofs of size $2^{n^{\varepsilon}}$ for every $\varepsilon>0$, unless $\mathsf{PH}$ collapses to $\Sigma_2^p$ (Klivans–van Melkebeek 2002). The same holds for other $\mathsf{AM}$-complete-flavoured problems: approximate lattice problems ($\mathrm{GapSVP}_{\sqrt{n}} \in \mathsf{coAM}$, Goldreich–Goldwasser), group non-membership, and quadratic-nonresiduosity-style protocols.
- **Round reduction.** $\mathsf{AM}[k]=\mathsf{AM}$ for constant $k$, and $\mathsf{MA} \subseteq \mathsf{AM}$, are unconditional. $\mathsf{MA}=\mathsf{NP}$ follows from the same hypothesis with *deterministic* circuits: $\mathsf{E}\not\subseteq \mathrm{SIZE}(2^{o(n)}) \Rightarrow \mathsf{MA}=\mathsf{NP}$ — so the $\mathsf{MA}$ case is strictly easier and already handled by Impagliazzo–Wigderson.
- **Converse direction.** $\mathsf{NEXP}\subseteq \mathsf{P}/\mathrm{poly} \Rightarrow \mathsf{NEXP}=\mathsf{MA}$ (Impagliazzo–Kabanets–Wigderson 2002), so $\mathsf{AM}=\mathsf{NP}$ would give $\mathsf{NEXP}\not\subseteq\mathsf{P}/\mathrm{poly}$.
- **Instance-wise.** van Melkebeek–Sdroievski (CCC 2023) give per-instance hardness-vs-randomness for $\mathsf{AM}$, where the hardness assumption is invoked only on the inputs where randomness is actually needed.

## 5. Principal Obstacles

1. **Complementation failure in the hybrid argument.** NW reconstruction converts a distinguisher $C$ into a next-bit predictor by evaluating both $C$ and $\neg C$. For nondeterministic $C$ this is illegal: $\mathsf{NP}$ is not closed under complement (as far as we know). This is why every known proof pays with hardness against SV-nondeterministic circuits, an assumption strictly stronger than $\mathsf{E}^{\mathsf{NP}}\not\subseteq\mathrm{SIZE}(2^{o(n)})$.
2. **No worst-case to average-case amplification for nondeterministic circuits.** Impagliazzo–Wigderson's amplification uses error-correcting-code decoding, whose local list-decoder is a deterministic (or randomized) circuit computing the hard function everywhere. In the nondeterministic setting the decoder must produce a *verifiable* value, forcing the single-valued model; a genuine worst-case $\Rightarrow$ average-case theorem for plain nondeterministic circuits is not known.
3. **Lower bounds are the real bottleneck.** No superlinear lower bound is known for nondeterministic circuits on any explicit function — the frontier is the $5n - o(n)$-type bounds for deterministic circuits (Iwama–Morizumi, Find–Golovnev–Hirsch–Kulikov), which are far weaker than $2^{\Omega(n)}$ and in the wrong model.
4. **Barriers.** Relativization (Baker–Gill–Solovay) and natural proofs (Razborov–Rudich) block generic approaches; the algebrization barrier (Aaronson–Wigderson) rules out arithmetization-only arguments, and NW-style derandomization is itself algebrizing.
5. **Equivalence to lower bounds.** By Aydınlıoğlu–van Melkebeek, derandomizing $\mathsf{AM}$ *requires* proving nondeterministic circuit lower bounds. There is no "cheap" route: the problem is exactly as hard as a lower bound nobody can prove.

## 6. The Gap

Proven: hardness $\Rightarrow$ derandomization, in both high-end ($2^{\Omega(n)}$ hardness $\Rightarrow \mathsf{AM}=\mathsf{NP}$) and low-end forms; plus a converse making the implication near-equivalence.

Missing: **any** unconditional lower bound against nondeterministic or SV-nondeterministic circuits for a function in $\mathsf{E}^{\mathsf{NP}}$. The gap is between $\Omega(n)$-size lower bounds (known, deterministic model) and $2^{\Omega(n)}$ (needed, nondeterministic model) — an exponential gap in a strictly harder model.

A secondary, possibly more tractable gap: eliminate the *single-valuedness* requirement, i.e. show
$$\mathsf{E}^{\mathsf{NP}} \not\subseteq \mathsf{NSIZE}(2^{o(n)}) \;\Longrightarrow\; \mathsf{AM}=\mathsf{NP},$$
which would need a reconstruction procedure that never complements the distinguisher.

## 7. Current Research (as of June 2026)

- **Hardness-vs-randomness, revisited.** Chen–Tell's framework (FOCS 2021) replaces PRGs with targeted generators computable from the input; extending it to nondeterministic verifiers is the most active line, with van Melkebeek and Sdroievski's instance-wise $\mathsf{AM}$ tradeoffs the concrete deliverable. *(frontier — verify)*
- **Free lunch / almost-everywhere derandomization.** Efforts to obtain $\mathsf{AM}$ derandomization from assumptions no stronger than "$\mathsf{AM}$-hardness is necessary anyway", following Chen–Rothblum–Tell-style equivalences. *(frontier — verify)*
- **Groups.** Wisconsin (van Melkebeek), Weizmann/Haifa (Shaltiel, Tell), IAS/Princeton (Wigderson school), Simons Institute programmes on meta-complexity; meta-complexity approaches (MCSP, $\mathsf{GapMCSP}$) attempt to convert search-to-decision results into the missing lower bounds.
- **Interaction with $\mathsf{NEXP}$ lower bounds.** Williams' algorithmic method (`ACC` $\not\supseteq \mathsf{NEXP}$) is being pushed toward nondeterministic circuit classes; a nontrivial nondeterministic-circuit-SAT algorithm would give the first relevant lower bound.

## 8. Future Work

- Prove a worst-case-to-average-case connection for nondeterministic circuits, removing single-valuedness from Hypothesis (H).
- Find a hitting-set generator for co-nondeterministic circuits whose reconstruction is *one-sided*, so that $\neg C$ is never evaluated.
- Apply the algorithmic method: design a $2^{n}/n^{\omega(1)}$ algorithm for satisfiability of nondeterministic circuits, which by Williams-style arguments should yield $\mathsf{NEXP}$-level nondeterministic lower bounds.
- Settle the easier target $\mathsf{MA}=\mathsf{NP}$ unconditionally, or show it implies $\mathsf{AM}=\mathsf{NP}$.
- Explore whether Graph Non-Isomorphism specifically admits polynomial-size proofs, decoupled from the general $\mathsf{AM}$ question — Babai's quasipolynomial GI algorithm makes this plausible for GI-adjacent instances.

## 9. Key References

- **[Foundational]** N. Nisan and A. Wigderson. *Hardness vs. Randomness.* Journal of Computer and System Sciences, 49(2):149–167, 1994.
- **[Foundational]** L. Babai and S. Moran. *Arthur–Merlin Games: A Randomized Proof System, and a Hierarchy of Complexity Classes.* Journal of Computer and System Sciences, 36(2):254–276, 1988.
- **[Foundational]** S. Goldwasser and M. Sipser. *Private Coins versus Public Coins in Interactive Proof Systems.* STOC 1986, pp. 59–68.
- **[Foundational]** R. Impagliazzo and A. Wigderson. *P = BPP if E Requires Exponential Circuits: Derandomizing the XOR Lemma.* STOC 1997, pp. 220–229.
- **[SOTA]** A. Klivans and D. van Melkebeek. *Graph Nonisomorphism Has Subexponential Size Proofs Unless the Polynomial-Time Hierarchy Collapses.* SIAM Journal on Computing, 31(5):1501–1526, 2002.
- **[SOTA]** P. B. Miltersen and N. V. Vinodchandran. *Derandomizing Arthur–Merlin Games Using Hitting Sets.* Computational Complexity, 14(3):256–279, 2005.
- **[SOTA]** R. Shaltiel and C. Umans. *Pseudorandomness for Approximate Counting and Sampling.* Computational Complexity, 15(4):298–341, 2006.
- **[SOTA]** R. Shaltiel and C. Umans. *Low-End Uniform Hardness versus Randomness Tradeoffs for AM.* SIAM Journal on Computing, 39(3):1006–1037, 2009.
- **[SOTA]** D. Gutfreund, R. Shaltiel, A. Ta-Shma. *Uniform Hardness versus Randomness Tradeoffs for Arthur–Merlin Games.* Computational Complexity, 12(3–4):85–130, 2003.
- **[SOTA]** B. Aydınlıoğlu and D. van Melkebeek. *Nondeterministic Circuit Lower Bounds from Mildly Derandomizing Arthur–Merlin Games.* Computational Complexity, 26(1):79–118, 2017.
- **[SOTA]** V. Kabanets, R. Impagliazzo, A. Wigderson. *In Search of an Easy Witness: Exponential Time vs. Probabilistic Polynomial Time.* Journal of Computer and System Sciences, 65(4):672–694, 2002.
- **[Recent]** L. Chen and R. Tell. *Hardness vs Randomness, Revisited: Uniform, Non-Black-Box, and Instance-Wise.* FOCS 2021, pp. 125–136.
- **[Recent]** D. van Melkebeek and N. Sdroievski. *Instance-Wise Hardness versus Randomness Tradeoffs for Arthur–Merlin Protocols.* CCC 2023, LIPIcs vol. 264.
- **[Survey]** S. Arora and B. Barak. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009 (Chapters 8, 20).
- **[Survey]** R. Shaltiel. *Derandomized Parallel Repetition Theorems and Hardness Amplification* / and: *Recent Developments in Explicit Constructions of Extractors.* Bulletin of the EATCS, 77:67–95, 2002.

## 10. Worked Example / Concrete Special Case

**The protocol.** Graph Non-Isomorphism on two $n$-vertex graphs $(G_0,G_1)$: Arthur picks $b \in \{0,1\}$ and $\pi \in S_n$ uniformly and sends $H = \pi(G_b)$; Merlin returns $b' $. Completeness $1$; soundness error $1/2$. One round costs $1 + \lceil \log(n!)\rceil \le 1 + n\log n$ random bits. Take $n = 8$: $\log(8!) = \log 40320 \approx 15.3$, so $16$ bits per permutation, $17$ bits per repetition. Repeat $k=20$ times in parallel: $m = 340$ random bits, soundness error $2^{-20}$.

**The set to fool.** $A_x \subseteq \{0,1\}^{340}$ is the set of coin strings Merlin can answer; it is decided by a nondeterministic circuit of size $\approx 10^4$. If $G_0 \cong G_1$ then $|A_x|/2^{340} \le 2^{-20}$, so $\overline{A_x}$ has density $\ge 1-2^{-20}$ and is co-nondeterministic.

**The generator.** Let $f:\{0,1\}^{n'} \to \{0,1\}$ be hard for SV-nondeterministic circuits of size $2^{\delta n'}$. Set $m = 340$, so $\log m \approx 8.4$; pick $n' = 24$. A design with $|S_i|=24$, $|S_i\cap S_j| \le 9$ over $s = O(n'^2/\log m) = O(576/8.4) \approx 69$ bits exists (Nisan–Wigderson, Lemma on designs). Then $G^f: \{0,1\}^{69}\to\{0,1\}^{340}$ and enumerating all $2^{69}$ seeds is too slow — but with $n' = c\log m$ for a constant $c$ (possible exactly when $f$ is $2^{\Omega(n')}$-hard, since we need $2^{\delta n'} \gg m^2$), we get $s = O(\log m)$ and $2^{s} = \mathrm{poly}(m)$ seeds.

**The $\mathsf{NP}$ algorithm.** On input $(G_0,G_1)$: guess witnesses $y_z$ for all $2^s = \mathrm{poly}(n)$ seeds $z$; accept iff $V(x, G^f(z), y_z)=1$ for at least $2/3$ of them. Completeness is immediate. For soundness, if $G_0 \cong G_1$ and the algorithm accepted, then $G^f(U_s)$ lands in $A_x$ with probability $\ge 2/3$ while $U_m$ lands there with probability $\le 2^{-20}$ — advantage $\varepsilon > 0.66$ against the co-nondeterministic circuit $\overline{C_x}$.

**Reconstruction and the sticking point.** The hybrid argument then yields, for some $i \le 340$, a predictor of $f$ with advantage $\varepsilon/m > 0.66/340 \approx 1.9\times 10^{-3}$, of size $\mathrm{size}(C_x) + m^2 \approx 10^4 + 1.16\times10^5 \approx 1.3\times 10^5$. That circuit uses $C_x$ *and* $\neg C_x$ — hence it is only guaranteed to be an SV-nondeterministic circuit, which is why hardness must be assumed in that model. If $f$ is $2^{\delta \cdot 24}$-hard with $\delta = 1/2$, i.e. hard for size $2^{12}=4096 < 1.3\times10^5$, the contradiction fails; one needs $n'$ large enough that $2^{\delta n'} > 1.3\times 10^5$, e.g. $n' = 36$ giving $2^{18}=262144$. That constraint — hardness exponent versus the $m^2$ reconstruction overhead — is exactly what fixes the seed length and hence whether the simulation is polynomial or merely subexponential.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*