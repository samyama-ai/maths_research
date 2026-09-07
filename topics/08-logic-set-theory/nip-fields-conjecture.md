---
id: 08-logic-set-theory/nip-fields-conjecture
title: "NIP Fields Conjecture"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# NIP Fields Conjecture

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/nip-fields-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Shelah).** Let $K$ be an infinite field whose complete first-order theory in the language of rings $\mathcal{L}_{\mathrm{ring}} = \{+,-,\cdot,0,1\}$ is NIP (does not have the independence property). Then at least one of the following holds:

1. $K$ is separably closed;
2. $K$ is real closed;
3. $K$ admits a nontrivial henselian valuation.

The three cases are not exclusive (an algebraically closed field satisfies (1) and (3)). "Admits" means *some* valuation ring $\mathcal{O} \subsetneq K$ with $\mathcal{O} \neq K$ is henselian; it need not be definable a priori.

A complete solution is either a proof of the trichotomy, or an infinite field $K$ with $\mathrm{Th}(K)$ NIP that is neither separably nor real closed and whose every nontrivial valuation is non-henselian. Two standard strengthenings, both open and both known to follow from the conjecture (Halevi–Hasson–Jahnke 2020):

- **(Definable form.)** In case (3) the henselian valuation ring may be taken $\emptyset$-definable in $\mathcal{L}_{\mathrm{ring}}$.
- **(Henselianity conjecture.)** If $(K,v)$ is a valued field whose theory in $\mathcal{L}_{\mathrm{ring}} \cup \{\mathcal{O}\}$ is NIP and $K$ is not separably closed, then $v$ is henselian.

## 2. Mathematical Foundations

**Independence property.** A formula $\varphi(x;y)$ has IP in a theory $T$ if in some model there are $(a_i)_{i<\omega}$ and $(b_J)_{J \subseteq \omega}$ with
$$\models \varphi(a_i; b_J) \iff i \in J .$$
$T$ is **NIP** if no formula has IP. Equivalently, every formula has finite VC dimension: $\sup_b |\{\,\varphi(M;b)\cap A\,\}| = O(|A|^{d})$ for the set system it defines (Sauer–Shelah), and every formula has finite alternation rank on indiscernible sequences.

**Ranks.** An *ict-pattern* of depth $\kappa$ in $x$ is a family $(\varphi_i(x;y))_{i<\kappa}$ and $(b_{i,j})_{j<\omega}$ such that for every $\eta \in \omega^{\kappa}$ the type $\{\varphi_i(x;b_{i,\eta(i)})\} \cup \{\neg\varphi_i(x;b_{i,j}) : j \neq \eta(i)\}$ is consistent. $\mathrm{dp\text{-}rk}(x=x)$ is the supremum of such $\kappa$. A theory is **strongly dependent** if $\mathrm{dp\text{-}rk}(x=x) < \aleph_0$, **dp-minimal** if the rank is $1$. Dropping the requirement that rows be mutually inconsistent gives **burden** (inp-rank); NTP$_2$ is the corresponding tameness class. Stable $\subsetneq$ NIP; dp-minimal $\subsetneq$ dp-finite $=$ strongly dependent $\subsetneq$ NIP.

**Valuations.** $v : K^\times \to \Gamma$ onto an ordered abelian group, $\mathcal{O}_v = \{x : v(x)\ge 0\}$, maximal ideal $\mathfrak{m}_v$, residue field $Kv$. $v$ is **henselian** if every $f \in \mathcal{O}_v[X]$ with $f(a)\in\mathfrak{m}_v$, $f'(a) \in \mathcal{O}_v^\times$ has a root in $a + \mathfrak{m}_v$; equivalently $v$ extends uniquely to every finite extension of $K$.

**Known NIP fields.** $\mathrm{ACF}_p$, $\mathrm{RCF}$, $\mathrm{ACVF}$, $\mathbb{Q}_p$ and finite extensions, $\mathbb{F}_p((t))$, $\mathbb{C}((t))$, and more generally henselian $(K,v)$ with $Kv$ NIP and (in the equicharacteristic-$0$ or unramified mixed case) suitable Ax–Kochen/Ershov transfer, using that **every ordered abelian group is NIP** (Gurevich–Schmitt 1984). Every known infinite NIP field satisfies the trichotomy.

**Artin–Schreier.** In characteristic $p$, write $\wp(x) = x^p - x$. $K$ is *Artin–Schreier closed* if $\wp(K) = K$, equivalently $K$ has no degree-$p$ Galois extension.

## 3. History & State of the Art (SOTA)

- **1980.** Duret proves that a PAC field which is not separably closed has IP, the first "wild fields are untame" theorem.
- **2009–2014.** Shelah isolates strong dependence and dp-rank (*Dependent first order theories, continued*, Israel J. Math. 173, 2009; *Strongly dependent theories*, Israel J. Math. 204, 2014) and formulates the classification of NIP fields as a program; the trichotomy above becomes known as *Shelah's conjecture on NIP fields*. It generalizes the older **stable fields conjecture** (every infinite stable field is separably closed) and the Podewski-style expectations for tame algebra.
- **2011.** Kaplan–Scanlon–Wagner: every infinite NIP field of characteristic $p$ is Artin–Schreier closed. This is the single most-used structural fact about NIP fields.
- **2015–2016.** Johnson's Berkeley thesis classifies dp-minimal fields; Jahnke–Koenigsmann develop uniformly definable $p$-henselian valuations.
- **2019–2021.** Halevi–Hasson–Jahnke give the conjectural classification of strongly dependent fields and prove the equivalence of Shelah's conjecture with its definable and henselianity variants. Johnson's six-part *dp-finite fields* series settles the conjecture for all fields of finite dp-rank.
- **2020–2024.** Johnson–Tran–Walsberg–Ye introduce the **étale-open topology** and prove the stable fields conjecture (JEMS, 2024), plus the NIP trichotomy for *large* fields.

State of the art: proved for finite dp-rank, for stable theories, for large fields, and for all known concrete examples; open in general, with characteristic $0$ and infinite rank the hard zone.

## 4. Partial Results / Verified Cases

- **dp-rank $1$ (dp-minimal).** Every infinite dp-minimal field is algebraically closed, real closed, or admits a nontrivial henselian valuation; moreover it is perfect and, if valued, defectless of finite ramification (Johnson, *On dp-minimal fields*; Jahnke–Simon–Walsberg, *Dp-minimal valued fields*, JSL 2017).
- **Finite dp-rank $n < \omega$ (strongly dependent).** Full trichotomy, with "separably closed" upgraded to "algebraically closed" since dp-finite fields are perfect (Johnson, *Dp-finite fields I–VI*, 2020–2021). Rank $2$ was the pivotal case; subadditivity of dp-rank for the induction was established inside the same series.
- **Stable.** Every infinite stable field is separably closed (Johnson–Tran–Walsberg–Ye, JEMS 2024) — the conjecture's stable shadow, open since the 1970s.
- **Large fields.** For $K$ large (i.e. $K$ existentially closed in $K((t))$), NIP implies the trichotomy, again by étale-open methods. This covers henselian, pseudo-algebraically closed, PRC and PpC fields.
- **Characteristic $p$ constraints.** Infinite NIP fields of char $p$ are Artin–Schreier closed (Kaplan–Scanlon–Wagner, Israel J. Math. 185, 2011); the same holds for NTP$_2$ (Chernikov–Kaplan–Simon) and for $n$-dependent fields (Hempel, MLQ 2016). Consequence: no infinite NIP field of char $p$ has a finite separable extension of degree divisible by $p$ inside its perfect closure tower.
- **Valued-field side.** NIP henselian valued fields are characterized (Anscombe–Jahnke), and henselian expansions of NIP fields are controlled by Jahnke's work; definable-valuation criteria are due to Jahnke–Koenigsmann and Halevi–Hasson–Jahnke.
- **Bounded/PAC.** Non-separably-closed PAC fields have IP (Duret 1980), so they are excluded outright.

## 5. Principal Obstacles

- **No dimension to induct on.** NIP supplies combinatorial tameness (finite VC dimension, honest definitions, invariant types) but no rank. Stability-theoretic forking behaves badly; the only usable numerical invariant, dp-rank, is exactly what Johnson's proof consumes, and it is infinite in the open cases. There is no known replacement well-order.
- **The topology has to be built by hand.** Johnson's method manufactures a canonical field topology from a definable "infinitesimals" subgroup obtained as a directed intersection, then shows the topology is a V-topology and hence comes from a valuation (Dürbaum–Kowalsky–Prestel). The construction of the infinitesimals uses inflators, a reduced modular lattice of definable subgroups, and the rank-$2$ case as base — all of which require finiteness of rank.
- **No definable subring to start from.** In characteristic $0$ there is no Artin–Schreier analogue: one must produce a nontrivial definable subring from pure combinatorics. Fields with no proper definable subring are common ($\mathbb{R}$, $\mathbb{C}$), and no invariant distinguishes them from a hypothetical counterexample.
- **Non-large fields resist algebraic geometry.** The étale-open topology is only informative when $K$ is large; on non-large fields it is discrete and the JTWY machinery collapses. Johnson–Ye's *curve-excluding fields* (2023) show that non-large fields can nevertheless be model-theoretically well-behaved, so largeness cannot be assumed for free. *(frontier — verify whether any such field is NIP)*
- **Transfer principles are conditional.** Ax–Kochen/Ershov-type reductions relate $(K,v)$ to $(Kv,\Gamma)$ only once $v$ is *known* henselian; they cannot bootstrap henselianity.

## 6. The Gap

Proved: the trichotomy for $\mathrm{dp\text{-}rk}(K) < \aleph_0$, for stable $K$, and for large $K$. Conjectured: the trichotomy for all NIP $K$.

The precise missing step is the construction, from NIP alone, of a nontrivial definable V-topology (equivalently a nontrivial definable valuation ring) on an infinite NIP field that is neither separably nor real closed — without any finiteness assumption on dp-rank and without largeness. Formally: exhibit a definable subgroup $I \le (K,+)$, invariant under multiplication by a definable subring, with $\bigcap_{a \in K^\times} aI = 0$ and $I$ absorbing, using only finite VC dimension of $\mathcal{L}_{\mathrm{ring}}$-formulas. Every existing route to such an $I$ terminates in a rank-based induction.

## 7. Current Research (as of June 2026)

- **Münster (Jahnke, Anscombe collaborations).** Henselian expansions of NIP fields, definability of henselian valuations, NIP transfer in mixed characteristic and for imperfect residue fields.
- **Fudan (Johnson) with Tran, Walsberg, Ye.** Étale-open topology as a general geometry-from-logic device; extensions past largeness; NIP consequences for $\mathrm{Gal}(K)$.
- **Israel school (Kaplan, Hasson, Halevi).** Strongly dependent and $n$-dependent fields, groups definable in NIP fields, classification of NIP valued fields with small value group.
- **Positive characteristic programme.** Attempts to close char $p$ first, leveraging Artin–Schreier closedness plus $p$-henselianity to force a definable valuation; several groups regard this as the likeliest next full case. *(frontier — verify current preprint status)*
- **$n$-dependence and NTP$_2$.** Generalizing the Kaplan–Scanlon–Wagner obstruction upward to test how much of the conjecture is really about NIP rather than about Artin–Schreier theory.

## 8. Future Work

- Prove the char $p$ case unconditionally; then attack mixed characteristic by lifting through Cohen rings.
- Find a rank-free substitute for dp-finiteness: a "generic subgroup" or measure-theoretic notion (Keisler measures, generically stable types) that yields infinitesimals in arbitrary NIP fields.
- Decide whether every infinite NIP field is large. A positive answer, combined with JTWY, closes the conjecture immediately; this is the cleanest single reduction now visible.
- Settle the intermediate conjecture that every NIP field has small absolute Galois group (bounded, or with restricted cohomological dimension).
- Determine whether NIP fields are always perfect — known for dp-finite, open in general; failure would reshape the statement.

## 9. Key References

- **[Foundational]** S. Shelah. *Strongly dependent theories.* Israel Journal of Mathematics 204 (2014), 1–83.
- **[Foundational]** J.-L. Duret. *Les corps faiblement algébriquement clos non séparablement clos ont la propriété d'indépendance.* In: Model Theory of Algebra and Arithmetic, Lecture Notes in Mathematics 834, Springer, 1980.
- **[Foundational]** Y. Gurevich, P. H. Schmitt. *The theory of ordered abelian groups does not have the independence property.* Transactions of the AMS 284 (1984), 171–182.
- **[Foundational]** I. Kaplan, T. Scanlon, F. O. Wagner. *Artin–Schreier extensions in NIP and simple fields.* Israel Journal of Mathematics 185 (2011), 141–153.
- **[SOTA]** W. Johnson. *Dp-finite fields I–VI.* Annals of Pure and Applied Logic / arXiv preprint series, 2019–2021 (I: *The infinitesimals*, APAL 172 (2021); VI: *The dp-finite Shelah conjecture*).
- **[SOTA]** W. Johnson. *On dp-minimal fields.* arXiv:1507.02745, 2015; and *Fun with Fields*, PhD thesis, UC Berkeley, 2016.
- **[SOTA]** W. Johnson, C.-M. Tran, E. Walsberg, J. Ye. *Étale open topology and the stable fields conjecture.* Journal of the European Mathematical Society, 2024.
- **[SOTA]** Y. Halevi, A. Hasson, F. Jahnke. *Definable V-topologies, henselianity and NIP.* Journal of Mathematical Logic 20 (2020), 2050008.
- **[Survey]** Y. Halevi, A. Hasson, F. Jahnke. *A conjectural classification of strongly dependent fields.* Bulletin of Symbolic Logic 25 (2019), 182–195.
- **[Survey]** P. Simon. *A Guide to NIP Theories.* Lecture Notes in Logic 44, ASL / Cambridge University Press, 2015.
- **[Related]** F. Jahnke, J. Koenigsmann. *Uniformly defining $p$-henselian valuations.* Annals of Pure and Applied Logic 166 (2015), 741–754.
- **[Related]** F. Jahnke, P. Simon, E. Walsberg. *Dp-minimal valued fields.* Journal of Symbolic Logic 82 (2017), 151–165.
- **[Related]** N. Hempel. *On $n$-dependent groups and fields.* Mathematical Logic Quarterly 62 (2016), 215–224.

## 10. Worked Example / Concrete Special Case

**(a) $K = \mathbb{Q}_p$, $p$ odd: case (3) holds with a $\emptyset$-definable henselian valuation.** Put
$$\mathcal{O} = \{\, x \in \mathbb{Q}_p \;:\; \exists y\ \, y^2 = 1 + p x^2 \,\}.$$
*If $v_p(x) \ge 0$:* then $v_p(px^2) \ge 1$, so $1+px^2 \equiv 1 \pmod{p}$. For $p$ odd, $f(Y)=Y^2-(1+px^2)$ has $f(1) \equiv 0 \pmod p$ and $f'(1)=2 \in \mathbb{Z}_p^\times$, so Hensel's lemma gives a root; $x \in \mathcal{O}$.
*If $v_p(x) = -n < 0$:* then $v_p(1+px^2) = 1-2n$, which is negative and **odd**, while every square has even valuation; so $x \notin \mathcal{O}$.
Hence $\mathcal{O} = \mathbb{Z}_p$ exactly, it is definable without parameters, and $v_p$ is henselian. $\mathbb{Q}_p$ is NIP (Macintyre/Delon, via Ax–Kochen–Ershov and Gurevich–Schmitt), indeed dp-minimal, so it lands inside Johnson's proved dp-rank-$1$ case, alternative (3). Neither (1) nor (2) holds: $X^2-p$ is irreducible and $-1$ is a sum of squares for $p \equiv 1 \bmod 4$.

**(b) Why $\mathbb{F}_p(t)$ is not a test case.** The Artin–Schreier equation $x^p - x = 1/t$ has no solution in $\mathbb{F}_p(t)$: a solution would have a pole, and if $v_t(x) = -m < 0$ then $v_t(x^p-x) = -pm \neq -1$. So $\mathbb{F}_p(t)$ is not Artin–Schreier closed, and by Kaplan–Scanlon–Wagner it has IP. The hypothesis of the conjecture fails, consistently with the fact that $\mathbb{F}_p(t)$ carries no nontrivial henselian valuation (its valuations all have proper immediate extensions) and is neither separably nor real closed. Its henselization $\mathbb{F}_p(t)^h \subset \mathbb{F}_p((t))$ *does* satisfy (3), and $\mathbb{F}_p((t))$ is NIP.

The pair (a)–(b) shows the conjecture's shape: NIP is exactly strong enough, in every verified case, to force either algebraic closure conditions or a hidden henselian valuation — and Artin–Schreier closedness is currently the only mechanism known to detect the failure in characteristic $p$, with no analogue at all in characteristic $0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*