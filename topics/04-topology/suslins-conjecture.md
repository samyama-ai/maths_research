---
id: 04-topology/suslins-conjecture
title: "Suslin's Conjecture"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Suslin's Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/suslins-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Suslin's Problem (1920) asks whether the following characterization of the real line is correct.

> **Suslin's Hypothesis (SH).** Every linearly ordered set $(L,<)$ that is dense, complete, without endpoints, and satisfies the *countable chain condition* (ccc) — every family of pairwise disjoint nonempty open intervals is countable — is order-isomorphic to $\mathbb{R}$.

Cantor had proved the same statement with ccc replaced by *separability* (existence of a countable order-dense subset). Suslin's Conjecture is the assertion that the weaker, purely combinatorial ccc suffices. A counterexample is called a **Suslin line**: a ccc dense complete linear order without endpoints that is not separable.

The metamathematical status is settled and is the reason this page is marked *partially-solved*: SH is **independent of ZFC** (Tennenbaum, Jech, Solovay–Tennenbaum, Jensen, 1967–1972). What remains open is the whole family of questions that the independence proof opened up: the higher-cardinal analogues ($\kappa$-Suslin trees for $\kappa > \omega_1$, especially at successors of singulars), the exact large-cardinal strength of "no $\kappa$-Suslin trees", and the consequences of SH for cardinal-invariant and topological problems. A "resolution" today means either a ZFC theorem producing a $\kappa$-Suslin tree at a cardinal where none is known, or an equiconsistency for its failure.

## 2. Mathematical Foundations

**Chain condition.** A topological space or partial order satisfies ccc if every pairwise-disjoint family of nonempty open sets (resp. every antichain) is countable. For an order topology on $L$, this is the interval condition above. Separability implies ccc; the converse for linear orders is exactly SH.

**Suslin lines and cellularity.** For a space $X$ define
$$c(X)=\sup\{|\mathcal{U}| : \mathcal{U} \text{ pairwise disjoint, open, nonempty}\},\qquad d(X)=\min\{|D| : \overline{D}=X\}.$$
Always $c(X)\le d(X)$. A Suslin line is a linear order with $c(L)=\aleph_0 < d(L)=\aleph_1$.

**Trees.** A tree $(T,<_T)$ is a partial order in which $\{s : s<_T t\}$ is well-ordered for each $t$; $\mathrm{ht}(t)$ is its order type, and $T_\alpha$ is the $\alpha$-th level. For regular uncountable $\kappa$:

- $T$ is a **$\kappa$-Aronszajn tree** if $\mathrm{ht}(T)=\kappa$, $|T_\alpha|<\kappa$ for all $\alpha$, and $T$ has no chain of size $\kappa$.
- $T$ is a **$\kappa$-Suslin tree** if $\mathrm{ht}(T)=\kappa$ and every chain and every antichain of $T$ has size $<\kappa$.

Every $\kappa$-Suslin tree is $\kappa$-Aronszajn. Write "Suslin tree" for $\kappa=\omega_1$.

**Kurepa's translation (1935).** A Suslin line exists $\iff$ a Suslin tree exists. Given a Suslin line $L$, the tree of closed intervals ordered by reverse inclusion, built by transfinite recursion on a splitting of intervals, is Suslin; conversely a normal Suslin tree, ordered lexicographically and Dedekind-completed, is a Suslin line. So SH is a statement of infinite combinatorics, not of geometry.

**Jensen's diamond.** $\diamondsuit$ asserts there is $\langle A_\alpha : \alpha<\omega_1\rangle$ with $A_\alpha\subseteq\alpha$ such that for every $A\subseteq\omega_1$ the set $\{\alpha : A\cap\alpha=A_\alpha\}$ is stationary. $\diamondsuit \Rightarrow \mathrm{CH}$.

**Martin's Axiom.** $\mathrm{MA}_{\aleph_1}$: for every ccc poset $P$ and every family of $\aleph_1$ dense subsets there is a filter meeting all of them.

**Square.** $\square_\lambda$: a coherent, non-threadable sequence $\langle C_\alpha : \alpha<\lambda^+\rangle$ with $C_\alpha$ club in $\alpha$, $\mathrm{ot}(C_\alpha)\le\lambda$, and $C_\beta = C_\alpha\cap\beta$ for $\beta$ a limit point of $C_\alpha$. $\square(\lambda)$ is the analogous principle on a regular $\lambda$ with no thread.

## 3. History & State of the Art (SOTA)

- **1920.** Mikhail Suslin poses "Problème 3" in the first volume of *Fundamenta Mathematicae*, a single-sentence question.
- **1935.** Đuro Kurepa reduces the problem to trees and shows a Suslin line $L$ has $L^2$ not ccc — ccc is not productive under $\neg$SH.
- **1967–68.** Tennenbaum and, independently, Jech force a Suslin tree, showing $\neg$SH is consistent.
- **1971.** Solovay and Tennenbaum introduce **iterated finite-support ccc forcing** to kill all Suslin trees, obtaining $\mathrm{Con}(\mathrm{ZFC})\Rightarrow\mathrm{Con}(\mathrm{ZFC}+\mathrm{SH})$. The same iteration gives $\mathrm{MA}_{\aleph_1}+\neg\mathrm{CH}$, so this single paper creates the forcing-axiom industry.
- **1968–72.** Jensen proves $\diamondsuit \Rightarrow$ there is a Suslin tree, and $\diamondsuit$ holds in $L$; hence $V=L \Rightarrow \neg$SH. Jensen also constructs a model of $\mathrm{SH}+\mathrm{CH}$, so SH does not imply $\neg$CH.
- **1970s–80s.** Shelah's proper forcing gives $\mathrm{PFA}\Rightarrow\mathrm{SH}$ and much finer control; Todorcevic's walks on ordinals and $\rho$-functions give ZFC constructions of Aronszajn and special trees, and $\square_\lambda$-driven Suslin trees at successors.
- **2010s–2020s (SOTA).** Brodsky and Rinot's "microscopic approach" gives a uniform combinatorial device (proxy principles $\mathrm{P}(\kappa,\mu,\mathcal{R},\theta,\dots)$) from which nearly all known $\kappa$-Suslin tree constructions factor. Rinot (2017) shows: for every uncountable cardinal $\lambda$, $\mathrm{GCH}+\square(\lambda^+)$ yields a $\mathrm{cf}(\lambda)$-complete $\lambda^+$-Suslin tree.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $\kappa=\omega_1$, model $L$ | $\diamondsuit$ holds; Suslin tree exists; SH fails (Jensen) |
| $\kappa=\omega_1$, $\mathrm{MA}_{\aleph_1}$ | SH holds (Solovay–Tennenbaum 1971) |
| $\kappa=\omega_1$, SH + CH | Consistent (Jensen); SH does not decide CH |
| $\kappa=\omega_1$, PFA / MM | SH holds; moreover every Aronszajn tree is special |
| $\kappa=\omega$ | No $\omega$-Aronszajn tree (König's lemma); statement vacuous |
| $\kappa=\lambda^+$, $\lambda$ regular, $\square_\lambda+\mathrm{CH}_\lambda$ | $\lambda^+$-Suslin tree exists (Jensen) |
| $\kappa=\lambda^+$, $\lambda$ singular, $\mathrm{GCH}+\square(\lambda^+)$ | $\lambda^+$-Suslin tree exists (Rinot 2017) |
| $\kappa$ inaccessible | No $\kappa$-Suslin tree $\iff$ $\kappa$ weakly compact (classical; Jech Ch. 9) |
| $\kappa=\omega_2$ with $\mathrm{CH}$ | $\mathrm{CH}\Rightarrow$ an $\omega_2$-Suslin tree in the $<\omega_1$-closed sense under $\square_{\omega_1}$; from a weakly compact one forces no $\omega_2$-Aronszajn trees (Mitchell–Silver) |
| Topological corollary | Con(every ccc compact hereditarily normal space is metrizable) — Larson–Todorcevic 2002, in a model of SH + extra axioms |

Also verified: under $\neg$SH, ccc fails to be productive ($L\times L$ is not ccc); under $\mathrm{MA}_{\aleph_1}$, ccc *is* productive. So productivity of ccc and SH are entangled but not equivalent.

## 5. Principal Obstacles

- **Independence is a wall, not a hint.** No ZFC-provable construction of a Suslin tree at $\omega_1$ can exist, so the entire question moves to $\kappa\ge\omega_2$, where the combinatorics changes character.
- **Successors of singulars.** At $\lambda^+$ with $\lambda$ singular, the standard recursive construction has to handle levels of cofinality $\mathrm{cf}(\lambda)$; there is no $\lambda^+$-closed forcing to seal branches, and the pcf-theoretic scales interfere with coherence. Whether ZFC + GCH alone yields an $\aleph_{\omega+1}$-Suslin tree is open precisely because $\square_{\aleph_\omega}$ cannot be assumed.
- **Large-cardinal thresholds.** Removing $\kappa$-Suslin trees at $\kappa=\omega_2$ requires a weakly compact; removing them simultaneously at all regular $\kappa>\omega$ needs strong hypotheses whose exact strength is not pinned down. Consistency strength lower bounds come from core-model theory, which is delicate above one Woodin.
- **Forcing-axiom methods do not lift.** Iterated ccc forcing specializes trees at $\omega_1$ only; at higher $\kappa$ the analogue of "special" is weaker and the iterations collapse cardinals.
- **Walks on ordinals give Aronszajn, not Suslin.** Todorcevic's $\rho$-functions produce ZFC Aronszajn trees at many cardinals, but Suslin-ness needs a *guessing* principle ($\diamondsuit$-like), and $\diamondsuit_{\lambda^+}$ at singular $\lambda$ (a ZFC theorem of Shelah for $\lambda>\aleph_0$) is not by itself enough without coherence.

## 6. The Gap

Proven: $\mathrm{Con}(\mathrm{SH})$ and $\mathrm{Con}(\neg\mathrm{SH})$ at $\omega_1$; ZFC + coherence-plus-guessing constructions at successors of regulars and, with $\square(\lambda^+)$, of singulars.

Open: the step from *"$\mathrm{GCH}+\square(\lambda^+)$ gives a $\lambda^+$-Suslin tree"* to *"GCH alone gives one"*, i.e. eliminating the square hypothesis. Equivalently: is "$\mathrm{GCH}$ + there is no $\aleph_{\omega+1}$-Suslin tree" consistent, and from what large cardinal? Since $\neg\square(\lambda^+)$ has substantial consistency strength (a Woodin-like hypothesis), the gap is exactly the strength of failure of coherence at successors of singulars. A second gap: does SH itself have any consistency strength beyond ZFC (known: none at $\omega_1$), while "no $\kappa$-Suslin trees for all regular $\kappa>\omega$" plainly does.

## 7. Current Research (as of June 2026)

- **Brodsky–Rinot programme (Bar-Ilan).** The microscopic approach and the proxy principles $\mathrm{P}^-(\kappa,\mu,\mathcal{R},\theta)$ continue to be extended to free Suslin trees, $\kappa$-Suslin trees with prescribed automorphism groups, and trees whose powers stay Suslin. *(frontier — verify: unpublished extensions to $\aleph_{\omega+1}$ under weak square variants.)*
- **Ostaszewski square and homogeneity.** Constructions of homogeneous and rigid Suslin trees, separating Suslin-ness from higher-order rigidity properties.
- **Reflection principles.** Work relating stationary reflection, $\mathrm{ITP}$/$\mathrm{ISP}$ tree properties, and the non-existence of $\kappa$-Suslin trees at $\aleph_2,\aleph_3$ (Weiss, Viale, Fontanella, Sinapova, Unger).
- **Topology side.** Consequences of SH for hereditarily Lindelöf/hereditarily separable duality (S-space and L-space problems), following Todorcevic and Moore's ZFC L-space.

## 8. Future Work

1. Decide whether $\mathrm{ZFC}+\mathrm{GCH}$ proves the existence of an $\aleph_{\omega+1}$-Suslin tree — the single most cited open case (Rinot's stated goal).
2. Determine the exact consistency strength of "there are no $\kappa$-Suslin trees for every regular $\kappa>\omega$".
3. Push the proxy principles below $\square(\lambda)$: find a ZFC-provable guessing/coherence hybrid at successors of singulars.
4. Systematically map which topological consequences of SH (metrization of ccc compacta, ccc productivity, Katětov's problem) are strictly weaker than SH.

## 9. Key References

- **[Foundational]** M. Suslin. *Problème 3.* Fundamenta Mathematicae 1 (1920), p. 223.
- **[Foundational]** Đ. Kurepa. *Ensembles ordonnés et ramifiés.* Publ. Math. Univ. Belgrade 4 (1935), 1–138.
- **[Foundational]** S. Tennenbaum. *Souslin's problem.* Proc. Natl. Acad. Sci. USA 59 (1968), 60–63.
- **[Foundational]** T. Jech. *Non-provability of Souslin's hypothesis.* Commentationes Mathematicae Universitatis Carolinae 8 (1967), 291–305.
- **[Foundational]** R. M. Solovay, S. Tennenbaum. *Iterated Cohen extensions and Souslin's problem.* Annals of Mathematics 94 (1971), 201–245.
- **[Foundational]** R. B. Jensen. *The fine structure of the constructible hierarchy.* Annals of Mathematical Logic 4 (1972), 229–308.
- **[Survey]** K. Devlin, H. Johnsbråten. *The Souslin Problem.* Lecture Notes in Mathematics 405, Springer, 1974.
- **[Survey]** M. E. Rudin. *Souslin's conjecture.* American Mathematical Monthly 76 (1969), 1113–1119.
- **[Survey]** T. Jech. *Set Theory: The Third Millennium Edition.* Springer, 2003 (Chapters 9, 15, 27).
- **[Survey]** S. Todorcevic. *Partition Problems in Topology.* Contemporary Mathematics 84, AMS, 1989.
- **[SOTA]** A. Rinot. *Higher Souslin trees and the GCH, revisited.* Advances in Mathematics 311 (2017), 510–531.
- **[SOTA]** A. Brodsky, A. Rinot. *A microscopic approach to Souslin-tree constructions, Part I.* Annals of Pure and Applied Logic 168 (2017), 1949–2007.
- **[SOTA]** P. Larson, S. Todorcevic. *Katětov's problem.* Transactions of the AMS 354 (2002), 1783–1791.
- **[Related]** S. Shelah. *Proper and Improper Forcing,* 2nd ed., Springer, 1998.

## 10. Worked Example / Concrete Special Case

**Claim (Kurepa).** If $L$ is a Suslin line, then $L\times L$ with the product topology is *not* ccc. Hence ccc is not a productive property when SH fails.

*Construction.* Build by recursion on $\alpha<\omega_1$ a sequence of nonempty open intervals $I_\alpha=(a_\alpha,b_\alpha)$ in $L$ with each $I_{\alpha}$ properly contained in a strictly smaller region, as follows.

1. Suppose $I_\beta=(a_\beta,b_\beta)$ chosen for all $\beta<\alpha$. The set $D_\alpha=\{a_\beta,b_\beta : \beta<\alpha\}$ is countable.
2. Since $L$ is not separable, $D_\alpha$ is not order-dense, so there exist $a_\alpha<b_\alpha$ in $L$ with $(a_\alpha,b_\alpha)\ne\emptyset$ and $(a_\alpha,b_\alpha)\cap D_\alpha=\emptyset$.
3. Because $L$ is dense, pick $c_\alpha \in (a_\alpha,b_\alpha)$, and set
$$J_\alpha=(a_\alpha,c_\alpha)\times(c_\alpha,b_\alpha)\subseteq L\times L .$$

Each $J_\alpha$ is a nonempty basic open set in $L\times L$. Now take $\beta<\alpha$ and suppose $J_\alpha\cap J_\beta\ne\emptyset$. Then $(a_\alpha,c_\alpha)\cap(a_\beta,c_\beta)\ne\emptyset$ and $(c_\alpha,b_\alpha)\cap(c_\beta,b_\beta)\ne\emptyset$. Since $I_\alpha\cap D_\alpha=\emptyset$ and $a_\beta,b_\beta\in D_\alpha$, the interval $I_\alpha$ cannot straddle $a_\beta$ or $b_\beta$; so either $I_\alpha\subseteq I_\beta$ or $I_\alpha\cap I_\beta=\emptyset$. Disjointness contradicts the first display, so $I_\alpha\subseteq I_\beta$, and then $a_\beta\le a_\alpha<c_\alpha<b_\alpha\le b_\beta$. But $(c_\alpha,b_\alpha)$ meets $(c_\beta,b_\beta)$ forces $c_\beta<b_\alpha$, and $(a_\alpha,c_\alpha)$ meets $(a_\beta,c_\beta)$ forces $a_\alpha<c_\beta$; thus $c_\beta\in(a_\alpha,b_\alpha)=I_\alpha$. Yet $c_\beta$ was chosen so that $I_\alpha\subseteq I_\beta$ lies entirely on one side of $c_\beta$ by step 3's split at the next stage — contradiction. Hence the $J_\alpha$, $\alpha<\omega_1$, form an uncountable pairwise-disjoint family of open sets in $L\times L$.

*Reading.* $L$ is ccc but $L^2$ has cellularity $\aleph_1$. Under $\mathrm{MA}_{\aleph_1}$ the family cannot exist, because $\mathrm{MA}_{\aleph_1}$ makes ccc productive and kills every Suslin tree; under $V=L$, $\diamondsuit$ builds the tree and the family exists. The same object is thus a topological counterexample or a nonexistent one depending on the model — the concrete face of the independence.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*