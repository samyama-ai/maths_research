---
id: 08-logic-set-theory/approachable-free-subset-property
title: "Approachability Ideal and the Approachable Free Subset Property"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Approachability Ideal and the Approachable Free Subset Property

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/approachable-free-subset-property` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Two linked questions about singular cardinals and their successors.

**(A) Approachability ideal.** Shelah's ideal $I[\lambda]$ on a regular cardinal $\lambda$ measures which points of $\lambda$ are "approachable" by a pre-assigned sequence of small sets. The central open question:

> Is $S^{\aleph_{\omega+1}}_{\aleph_1} \in I[\aleph_{\omega+1}]$ provable in ZFC? More generally, for $\mu$ singular and $\kappa < \mu$ regular, must $S^{\mu^+}_{\kappa}$ be in $I[\mu^+]$ modulo the nonstationary ideal?

ZFC proves only that *some* stationary subset of $S^{\mu^+}_\kappa$ lies in $I[\mu^+]$. Whether the whole set does is open at successors of singulars; a complete answer means either a ZFC proof or a forcing/inner-model construction producing a stationary $S \subseteq S^{\aleph_{\omega+1}}_{\aleph_1}$ with $S \cap T$ nonstationary for every $T \in I[\aleph_{\omega+1}]$.

**(B) Approachable free subset property (AFSP).** For $\vec\lambda = \langle \lambda_n : n<\omega\rangle$ increasing and cofinal in $\aleph_\omega$, $\mathrm{AFSP}_{\vec\lambda}$ asserts that every algebra on $\aleph_\omega$ with countably many finitary operations admits a countable cofinal subset that is free over each of its initial segments. The open problems: determine the **exact consistency strength** of $\mathrm{AFSP}_{\aleph_\omega}$, decide whether it depends on the choice of $\vec\lambda$, and determine which cardinal-arithmetic configurations (GCH below $\aleph_\omega$, $\aleph_\omega$ strong limit, $2^{\aleph_0}$ small) it is compatible with.

The two are one subject: AFSP is exactly the assertion that *no* approachability-style sequence can capture every countable cofinal subset of $\aleph_\omega$, so it is a strong, structural negation of approachability at $\aleph_\omega$.

## 2. Mathematical Foundations

**Approachability.** Let $\lambda$ be regular uncountable and $\bar a = \langle a_\alpha : \alpha<\lambda\rangle$ with $a_\alpha \subseteq \alpha$, $|a_\alpha| < \lambda$. A limit ordinal $\delta < \lambda$ is *approachable with respect to* $\bar a$ if there is $A \subseteq \delta$ with
$$\sup A = \delta,\qquad \mathrm{ot}(A) = \mathrm{cf}(\delta),\qquad \forall \beta<\delta \ \exists \gamma<\delta \ \big(A\cap\beta = a_\gamma\big).$$
Then
$$I[\lambda] = \Big\{ S \subseteq \lambda : \exists\, \bar a\ \exists\, \text{club } C \subseteq \lambda,\ \forall \delta \in S\cap C \ (\delta \text{ limit} \Rightarrow \delta \text{ approachable w.r.t. } \bar a)\Big\}.$$
$I[\lambda]$ is a normal, $\lambda$-complete ideal containing every $\{\delta<\lambda : \mathrm{cf}(\delta)<\lambda\}$-free stationary obstruction only when approachability genuinely fails. The *approachability property* $\mathrm{AP}_\mu$ is the statement $\mu^+ \in I[\mu^+]$ (equivalently $S^{\mu^+}_{<\mu} $ modulo clubs); it follows from $\square_\mu$ and is implied by $\square_\mu^*$ (Foreman–Magidor's "very weak square" is a further weakening).

Equivalent internal formulation: $S \in I[\lambda]$ iff for some (all) large $\theta$ there is a club of $\delta \in S$ such that $\delta = \sup(M\cap\lambda)$ for some $M \prec H_\theta$ with $|M|<\lambda$, $M$ *internally approachable*, i.e. $M = \bigcup_{i<\mathrm{cf}(\delta)} M_i$ with $\langle M_j : j\le i\rangle \in M_{i+1}$.

**Algebras and freeness.** An *algebra* on $\aleph_\omega$ is $\mathfrak{A} = \langle \aleph_\omega, (f_i)_{i<\omega}\rangle$ with $f_i : \aleph_\omega^{n_i} \to \aleph_\omega$; $\mathrm{cl}^{\mathfrak A}(x)$ is the generated subalgebra, countable when $x$ is countable. A set $x$ is *free* if $\alpha \notin \mathrm{cl}^{\mathfrak A}(x\setminus\{\alpha\})$ for all $\alpha\in x$. Koepke's free subset property $\mathrm{Fr}_{\aleph_0}(\aleph_\omega,\aleph_1)$ demands free sets of size $\aleph_1$.

**AFSP.** $\mathrm{AFSP}_{\vec\lambda}$: for every algebra $\mathfrak A$ on $\aleph_\omega$ with countably many operations there is $x \in [\aleph_\omega]^{\aleph_0}$ with $\sup x = \aleph_\omega$ such that
$$\forall n<\omega:\qquad \big(x\cap\lambda_n\big)\ \cap\ \mathrm{cl}^{\mathfrak A}\big(x\setminus\lambda_n\big) \;=\; \emptyset .$$
Each initial block of $x$ is invisible to the tail. Equivalently, in hull language: for stationarily many $M \prec H_\theta$ with $M \cap \aleph_\omega$ cofinal and countable, no proper initial segment $M\cap\lambda_n$ is recoverable from $M \setminus \lambda_n$. Since an internally approachable $M$ *does* recover its initial segments, AFSP contradicts approachability-style capture; it implies $\mathrm{AP}_{\aleph_\omega}$ fails and hence $\square_{\aleph_\omega}$ and $\square^*_{\aleph_\omega}$ fail.

**PCF interface.** With $\aleph_\omega$ strong limit, $\mathrm{cf}([\aleph_\omega]^{\aleph_0},\subseteq) = \aleph_{\omega+1}$ under weak hypotheses, and scales $\vec f = \langle f_\alpha : \alpha<\aleph_{\omega+1}\rangle \subseteq \prod_n \aleph_n$ exist. Good and very good points of a scale are the pcf shadow of approachability: very good points of uncountable cofinality lie in $I[\aleph_{\omega+1}]$ (Cummings–Foreman–Magidor).

## 3. History & State of the Art (SOTA)

- **1979–1994.** Shelah isolates $I[\lambda]$ while attacking successors of singulars (*On successors of singular cardinals*, Logic Colloquium '78; *Cardinal Arithmetic*, 1994). Key theorem: for $\mu$ any cardinal and $\kappa<\mu$ regular, there is a **stationary** $S \subseteq S^{\mu^+}_\kappa$ with $S \in I[\mu^+]$. If $\mu^{<\mu}=\mu$ then $S^{\mu^+}_{<\mu} \in I[\mu^+]$.
- **1984.** Koepke shows the free subset property $\mathrm{Fr}_{\aleph_0}(\aleph_\omega,\aleph_1)$ is equiconsistent with a measurable of Mitchell order $\omega_1$ — the first calibration of a free-subset principle at $\aleph_\omega$.
- **1997.** Foreman–Magidor introduce very weak square, separating $\mathrm{AP}_\mu$ from $\square_\mu$ and clarifying that $I[\mu^+]$ is strictly weaker than square.
- **2004.** Cummings–Foreman–Magidor tie $I[\lambda]$ to scales (good/very good points), giving the pcf dictionary now used in nearly all constructions.
- **2008–2010.** Krueger analyses internal approachability versus internal clubness; Sharon–Viale derive failures of approachability from stationary reflection at $\aleph_{\omega+1}$; Mitchell forces $I[\omega_2]\restriction \mathrm{Cof}(\omega_1)$ to be the nonstationary ideal from a greatly Mahlo cardinal — the successor-of-regular case.
- **2021–present.** Adolf and Ben-Neria isolate AFSP at $\aleph_\omega$, prove it consistent from large cardinals in the Mitchell-order region using extender-based/Prikry-type forcing over a suitable core model, and prove lower bounds placing it well above ZFC (inner models with many measurables). The exact strength remains open. *(frontier — verify the precise upper and lower bounds against the published versions.)*

## 4. Partial Results / Verified Cases

- **Successors of regulars, resolved:** if $\mu^{<\mu} = \mu$ (e.g. $\mu$ regular under GCH) then $\mu^+ \in I[\mu^+]$; approachability holds outright, and AFSP-type freeness fails at every such $\mu^+$.
- **Mitchell (2009):** consistently $I[\omega_2]\restriction\mathrm{Cof}(\omega_1) = \mathrm{NS}$, from a greatly Mahlo cardinal. So "$S^{\mu^+}_\kappa \in I[\mu^+]$" is *not* a ZFC theorem for $\mu$ regular.
- **Shelah's ZFC floor:** for every singular $\mu$ and every regular $\kappa<\mu$, a stationary subset of $S^{\mu^+}_\kappa$ is approachable. Also, $S^{\mu^+}_{\kappa} \in I[\mu^+]$ whenever $\kappa < \mathrm{cf}(\mu)$ and $\mu$ is a limit of cardinals $\nu$ with $\nu^{<\kappa}=\nu$ — so at $\aleph_{\omega+1}$ the case $\kappa=\aleph_0$ is settled positively, and $\kappa = \aleph_1$ is the open frontier.
- **Under $\square_\mu$ or $\square^*_\mu$:** $\mu^+ \in I[\mu^+]$, hence AFSP fails at $\aleph_\omega$ in $L$ and in all fine-structural core models; AFSP therefore outright implies $\neg\square^*_{\aleph_\omega}$ and the existence of inner models with measurables.
- **Koepke's calibration** settles the uncountable-free-set variant exactly: $\mathrm{Fr}_{\aleph_0}(\aleph_\omega,\aleph_1) \equiv_{\mathrm{Con}} \exists\kappa\, o(\kappa) = \omega_1$.
- **AFSP consistency (Adolf–Ben-Neria):** $\mathrm{AFSP}_{\vec\lambda}$ at $\aleph_\omega$ is consistent relative to a measurable of high Mitchell order; in the resulting model $\aleph_\omega$ is a strong limit and $\mathrm{AP}_{\aleph_\omega}$ fails. *(frontier — verify)*
- **Reflection route (Sharon–Viale 2010):** stationary reflection at $\aleph_{\omega+1}$ for $\aleph_1$-cofinal points implies failure of approachability there, giving a second, forcing-friendly source of non-approachable stationary sets.

## 5. Principal Obstacles

- **Shelah's stationary-subset theorem is a barrier from below.** Any consistency proof must destroy approachability on *every* stationary piece of $S^{\aleph_{\omega+1}}_{\aleph_1}$ while ZFC hands back a stationary approachable piece from any $\bar a$-sequence built from a scale. The known ZFC proof is robust under forcing that preserves cofinalities, so cardinal-collapsing or Prikry-type surgery is forced.
- **Countable cofinality kills reflection tools.** At $\aleph_\omega$ the free sets are countable and cofinal; the standard elementary-submodel machinery (internal approachability, $\sigma$-closure of chains) manufactures exactly the capture that AFSP forbids. There is no known way to build a chain of models whose union is *not* internally approachable at cofinality $\omega$ without large-cardinal-driven indiscernibles.
- **GCH-style coding.** If $\aleph_n^{\aleph_0} = \aleph_n$, all countable subsets of $\aleph_n$ can be enumerated by ordinals below $\aleph_{n+1}$; making AFSP survive requires the enumerating ordinal never to land inside the free set, which no combinatorial argument in ZFC can arrange.
- **Core-model induction stalls.** Lower bounds for AFSP proceed by covering arguments in $K$; but AFSP is a $\Sigma$-statement about *all* countable algebras, and current covering lemmas yield only "many measurables" rather than the Mitchell-order- or Woodin-level bounds that the forcing side suggests.
- **Prikry forcing adds too much structure.** Extender-based and diagonal Prikry forcings that make $\aleph_\omega$ strong limit with failure of SCH tend to add scales that are good almost everywhere, resurrecting approachability.

## 6. The Gap

For (A): ZFC gives *a* stationary approachable subset of $S^{\aleph_{\omega+1}}_{\aleph_1}$; the conjecture is about *all* of it. The missing step is a forcing over a model with a singular $\aleph_\omega$ that simultaneously (i) keeps $\aleph_{\omega+1}$ a cardinal, (ii) makes every candidate sequence $\bar a$ fail on a club, and (iii) survives Shelah's ZFC argument — Mitchell's technique for $\omega_2$ uses the regularity of $\omega_1$ and does not transfer.

For (B): the gap is quantitative. The upper bound is a measurable of large Mitchell order; the published lower bound is far weaker (inner models with many measurables). Closing it requires either a cheaper forcing for AFSP or a core-model induction that reads Mitchell order out of the failure of *every* capture sequence. Independently open: whether $\mathrm{AFSP}_{\vec\lambda}$ for one $\vec\lambda$ implies it for all.

## 7. Current Research (as of June 2026)

- **Jerusalem (Ben-Neria and collaborators):** singular stationarity, tight stationarity, and extender-based methods; AFSP as a test principle for "how non-approachable can $\aleph_\omega$ be". Ongoing work on AFSP variants at $\aleph_{\omega_1}$ and at inaccessible limits. *(frontier — verify)*
- **Inner-model side (Adolf, Schindler-school core-model induction):** raising the AFSP lower bound past $o(\kappa)=\kappa^{++}$ toward $\kappa^{+\omega}$. *(frontier — verify)*
- **Reflection programme:** consequences of stationary reflection and of strong compactness at $\aleph_{\omega+1}$ for $I[\aleph_{\omega+1}]$, continuing Sharon–Viale.
- **PCF-structural:** classifying which scales in $\prod_n\aleph_n$ are compatible with AFSP; the conjecture that AFSP implies the failure of "very good scale at $\aleph_\omega$" everywhere. *(frontier — verify)*

## 8. Future Work

1. Push the AFSP lower bound by a core-model induction driven by failures of covering for countable cofinal free sets.
2. Decide $\vec\lambda$-invariance: does $\mathrm{AFSP}_{\vec\lambda}$ imply $\mathrm{AFSP}_{\vec\mu}$ for any other increasing cofinal $\vec\mu$?
3. Force AFSP together with GCH below $\aleph_\omega$, or prove GCH below $\aleph_\omega$ refutes it.
4. Attack $S^{\aleph_{\omega+1}}_{\aleph_1} \notin I[\aleph_{\omega+1}]$ by a Mitchell-style forcing adapted to singular $\aleph_\omega$, likely from supercompactness.
5. Derive consequences: does AFSP imply the tree property or stationary reflection at $\aleph_{\omega+1}$, or is it orthogonal?

## 9. Key References

- **[Foundational]** Saharon Shelah. *Cardinal Arithmetic.* Oxford Logic Guides 29, Oxford University Press, 1994.
- **[Foundational]** Saharon Shelah. *On successors of singular cardinals.* In: Logic Colloquium '78, North-Holland, 1979, pp. 357–380.
- **[Foundational]** Peter Koepke. *The consistency strength of the free-subset property for $\omega_\omega$.* Journal of Symbolic Logic 49 (1984), 1198–1204.
- **[Foundational]** Matthew Foreman, Menachem Magidor. *A very weak square principle.* Journal of Symbolic Logic 62 (1997), 175–196.
- **[Structural]** James Cummings, Matthew Foreman, Menachem Magidor. *Canonical structure in the universe of set theory I.* Annals of Pure and Applied Logic 129 (2004), 211–243.
- **[Survey]** Todd Eisworth. *Successors of singular cardinals.* In: Handbook of Set Theory (M. Foreman, A. Kanamori, eds.), Springer, 2010, pp. 1229–1350.
- **[SOTA]** William J. Mitchell. *$I[\omega_2]$ can be the nonstationary ideal on $\mathrm{Cof}(\omega_1)$.* Transactions of the American Mathematical Society 361 (2009), 561–601.
- **[SOTA]** Assaf Sharon, Matteo Viale. *Some consequences of reflection on the approachability ideal.* Transactions of the American Mathematical Society 362 (2010), 4201–4212.
- **[SOTA]** John Krueger. *Internal approachability and reflection.* Journal of Mathematical Logic 8 (2008), 23–39.
- **[SOTA / Recent]** Dominik Adolf, Omer Ben-Neria. *The approachable free subset property at $\aleph_\omega$.* Preprint / journal version, 2021–2023. *(frontier — verify venue and exact bounds)*

## 10. Worked Example / Concrete Special Case

Fix $\lambda_n = \aleph_n$. Let $\bar a = \langle a_\alpha : \alpha<\aleph_\omega\rangle$ be any sequence with $a_\alpha \subseteq \alpha$ countable. Build the algebra $\mathfrak A_{\bar a}$ on $\aleph_\omega$ with operations
$$F(\alpha, k) \;=\; \text{the } k\text{-th element of } a_\alpha \ (\text{in increasing order}), \quad F(\alpha,k)=0 \text{ if } |a_\alpha| \le k,$$
together with the identification of $\omega$ with itself (so $k \in \mathrm{cl}^{\mathfrak A}(\emptyset)$ for every $k<\omega$).

**Claim.** If $x \in [\aleph_\omega]^{\aleph_0}$ is cofinal and there exist $n<\omega$ and $\alpha \in x \setminus \aleph_n$ with $x \cap \aleph_n \subseteq a_\alpha$, then $x$ is not an approachable free subset for $\mathfrak A_{\bar a}$.

*Proof.* Every $\beta \in x\cap\aleph_n$ is the $k$-th element of $a_\alpha$ for some $k<\omega$, so $\beta = F(\alpha,k) \in \mathrm{cl}^{\mathfrak A}(x\setminus\aleph_n)$ since $\alpha \in x\setminus\aleph_n$ and $k \in \mathrm{cl}^{\mathfrak A}(\emptyset)$. Hence $(x\cap\aleph_n)\cap\mathrm{cl}^{\mathfrak A}(x\setminus\aleph_n) \ne \emptyset$. $\square$

So $\mathrm{AFSP}_{\vec\lambda}$ says exactly: for every $\bar a$ there is a countable cofinal $x$ that no member of $x$ "codes an initial segment of". This is the approachability condition of Section 2 read backwards, which is where the name comes from.

**Why GCH does not immediately refute it.** Assume $\aleph_n^{\aleph_0} = \aleph_n$ for all $n\ge1$. Then $|[\aleph_n]^{\aleph_0}| = \aleph_n$, so choose $\bar a$ so that $\langle a_\alpha : \aleph_n \le \alpha < \aleph_{n+1}\rangle$ enumerates $[\aleph_n]^{\aleph_0}$. Now let $x$ be any countable cofinal set. For each $n$, $x\cap\aleph_n$ is a countable subset of $\aleph_n$, hence $x \cap \aleph_n = a_{\alpha_n}$ for some $\alpha_n \in [\aleph_n, \aleph_{n+1})$. The freeness argument above fires **only if $\alpha_n \in x$** — and nothing forces that. There are $\aleph_{n+1}$ candidate codes and $x$ meets $[\aleph_n,\aleph_{n+1})$ in a countable set, so the coding ordinal generically misses $x$.

That single missing implication — "the code lands inside the free set" — is the whole content of the problem. Making the code land inside $x$ for all $\bar a$ simultaneously is what a ZFC proof of approachability at $\aleph_{\omega+1}$ would need; keeping it outside for a well-chosen $x$, for every $\bar a$ and every algebra, is what a model of AFSP must arrange, and is why the known constructions need indiscernibles supplied by measurables of high Mitchell order.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*