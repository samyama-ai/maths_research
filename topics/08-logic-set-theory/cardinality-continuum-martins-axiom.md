---
id: 08-logic-set-theory/cardinality-continuum-martins-axiom
title: "Cardinality of the Continuum under Martin's Axiom"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cardinality of the Continuum under Martin's Axiom

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/cardinality-continuum-martins-axiom` · **Status:** open

## 1. Problem Statement / Conjecture

Martin's Axiom ($\mathrm{MA}$) is the strongest natural weakening of the Continuum Hypothesis that is consistent with $2^{\aleph_0} > \aleph_1$. It settles a great many questions about the reals (Souslin's problem, measurability of $\Sigma^1_2$ sets, the values of all standard cardinal characteristics), yet it does not settle the size of the continuum itself.

Precisely, $\mathrm{ZFC} + \mathrm{MA}$ proves exactly two constraints on $\mathfrak{c} = 2^{\aleph_0}$:

$$\mathfrak{c} \text{ is regular}, \qquad \mathfrak{c}^{<\mathfrak{c}} = \mathfrak{c},$$

and by Solovay–Tennenbaum (1971) every $\kappa$ satisfying these is consistently the continuum under $\mathrm{MA}$. The open problem is therefore not "what is $\mathfrak c$ under $\mathrm{MA}$" — that is provably undecided — but the sharp follow-up:

**Problem.** Identify which combinatorial strengthenings of $\mathrm{MA}_{\aleph_1}$ decide $\mathfrak{c} = \aleph_2$, and which are compatible with $\mathfrak{c} > \aleph_2$. In particular:

1. **(Todorcevic)** Does the Open Coloring Axiom $\mathrm{OCA}$ imply $\mathfrak{c} = \aleph_2$?
2. **(Baumgartner)** Does $\mathrm{BA}$ — "all $\aleph_1$-dense sets of reals are order-isomorphic" — imply $\mathfrak{c} = \aleph_2$?
3. Is there a natural, ccc-flavoured forcing axiom, provably weaker than $\mathrm{PFA}$, that pins $\mathfrak{c}$ to $\aleph_2$?

A complete solution to (1) is either a $\mathrm{ZFC}$ proof that $\mathrm{OCA} \Rightarrow \mathfrak{c} = \aleph_2$, or a forcing construction (from $\mathrm{Con}(\mathrm{ZFC})$ plus whatever large cardinals are needed) of a model of $\mathrm{OCA} + \mathfrak{c} = \aleph_3$.

## 2. Mathematical Foundations

**Posets and antichains.** A partial order $(\mathbb{P}, \le)$ is *ccc* (countable chain condition) if every antichain — every set of pairwise incompatible conditions — is countable. $D \subseteq \mathbb{P}$ is *dense* if $\forall p \exists q \le p\,(q \in D)$. A *filter* $G \subseteq \mathbb{P}$ is upward closed and downward directed.

**Martin's Axiom.** For a cardinal $\kappa$, $\mathrm{MA}(\kappa)$ states: for every ccc poset $\mathbb{P}$ and every family $\mathcal{D}$ of dense subsets with $|\mathcal{D}| \le \kappa$, there is a filter $G \subseteq \mathbb{P}$ with $G \cap D \neq \emptyset$ for all $D \in \mathcal{D}$. Then
$$\mathrm{MA} \iff \forall \kappa < \mathfrak{c}\ \ \mathrm{MA}(\kappa), \qquad \mathfrak{m} := \min\{\kappa : \neg\mathrm{MA}(\kappa)\}.$$
$\mathrm{MA}(\aleph_0)$ is a theorem of $\mathrm{ZFC}$ (Rasiowa–Sikorski), and $\mathrm{MA}(\mathfrak{c})$ is false, so $\aleph_1 \le \mathfrak{m} \le \mathfrak{c}$ and $\mathrm{MA} \iff \mathfrak{m} = \mathfrak{c}$. $\mathrm{CH}$ implies $\mathrm{MA}$ trivially. $\mathrm{MA}_{\aleph_1}$ abbreviates $\mathrm{MA}(\aleph_1)$, i.e. $\mathfrak m > \aleph_1$.

**Core consequences.**
$$\mathrm{MA}(\kappa) \Rightarrow 2^{\kappa} = 2^{\aleph_0}; \qquad \mathrm{MA} \Rightarrow \mathfrak{p} = \mathfrak{t} = \mathfrak{b} = \mathfrak{d} = \mathrm{cov}(\mathcal{M}) = \mathrm{non}(\mathcal{M}) = \mathrm{cov}(\mathcal{N}) = \mathfrak{c}.$$
Bell's theorem sharpens the first line: $\mathrm{MA}(\sigma\text{-centered}) \iff \mathfrak{p} = \mathfrak{c}$.

**Regularity of $\mathfrak{c}$.** If $\mathrm{MA}$ holds and $\mathrm{cf}(\mathfrak{c}) = \kappa < \mathfrak{c}$, then $\mathrm{MA}(\kappa)$ gives $2^{\kappa} = \mathfrak{c}$, contradicting König's inequality $\mathrm{cf}(2^\kappa) > \kappa$. Hence $\mathfrak{c}$ is regular; and $\mathfrak{c}^{<\mathfrak{c}} = \mathfrak c$ follows from $2^\kappa = \mathfrak c$ for all $\kappa < \mathfrak c$.

**Open Coloring Axiom (Todorcevic).** For every separable metric $X \subseteq \mathbb{R}$ and every partition $[X]^2 = K_0 \cup K_1$ with $K_0$ open in the product topology, either $X$ has an uncountable $K_0$-homogeneous subset, or $X = \bigcup_{n<\omega} X_n$ with each $X_n$ $K_1$-homogeneous. $\mathrm{OCA}$ is not a ccc axiom but is a consequence of $\mathrm{PFA}$; it is independent of $\mathrm{MA}$.

**$\aleph_1$-dense sets.** $A \subseteq \mathbb{R}$ is *$\aleph_1$-dense* if $|A \cap (a,b)| = \aleph_1$ for every nonempty open interval. $\mathrm{BA}$ (Baumgartner's Axiom) asserts all such $A$ are order-isomorphic.

## 3. History & State of the Art (SOTA)

- **1970.** Martin and Solovay isolate $\mathrm{MA}$ in *Internal Cohen extensions*, extracting the combinatorial content of Solovay–Tennenbaum's Souslin-problem iteration. They prove $\mathrm{MA} + \neg\mathrm{CH}$ implies every $\Sigma^1_2$ set is Lebesgue measurable and has the Baire property.
- **1971.** Solovay and Tennenbaum prove the central consistency theorem: from $\mathrm{Con}(\mathrm{ZFC})$, for every regular $\kappa$ with $\kappa^{<\kappa} = \kappa$ there is a model of $\mathrm{MA} + \mathfrak{c} = \kappa$. Method: finite-support ccc iteration of length $\kappa$ with bookkeeping, using productivity of ccc under finite support.
- **1973.** Baumgartner shows $\mathrm{PFA}$-style forcing gives $\mathrm{BA}$, and asks about its relation to $\mathfrak c$.
- **1981–1985.** Abraham–Shelah show $\mathrm{MA}_{\aleph_1} \not\Rightarrow \mathrm{BA}$; Abraham–Rubin–Shelah build models of $\mathrm{MA} + \mathfrak{c} = \aleph_2 +$ strong continuous-coloring partition axioms, the first "$\aleph_2$-pinning" ccc technology.
- **1984.** Fremlin's *Consequences of Martin's Axiom* catalogues several hundred consequences; none decides $\mathfrak{c}$.
- **1987–1992.** Todorcevic and Veličković study partition strengthenings of $\mathrm{MA}_{\aleph_1}$; Veličković and Todorcevic independently prove $\mathrm{PFA} \Rightarrow \mathfrak{c} = \aleph_2$ (also from Foreman–Magidor–Shelah's Martin's Maximum). The mechanism is a reflection/stationary-set-coding argument unavailable to ccc axioms.
- **2002–2005.** Moore proves that a conjunction of two open-coloring axioms implies $\mathfrak{c} = \aleph_2$, and later that the Mapping Reflection Principle $\mathrm{MRP}$ (a $\mathrm{PFA}$ consequence) implies $\mathfrak{c} = \aleph_2$.
- **2015–2021.** Asperó–Mota develop side-condition iterations giving strong $\mathrm{PFA}$-fragments with $\mathfrak{c}$ large. Asperó–Schindler prove $\mathrm{MM}^{++} \Rightarrow (*)$, cementing $\aleph_2$ as the canonical value under maximal forcing axioms.

## 4. Partial Results / Verified Cases

- **Full independence range.** For each regular $\kappa$ with $\kappa^{<\kappa}=\kappa$ — e.g. $\kappa = \aleph_1, \aleph_2, \aleph_{17}, \aleph_{\omega+1}$ (under GCH), $\kappa = \mathfrak{c}^+$ — $\mathrm{MA} + \mathfrak{c} = \kappa$ is consistent. So $\mathrm{MA}$ decides nothing about $\mathfrak c$ beyond Section 2's two constraints.
- **Excluded values.** $\mathrm{MA} \Rightarrow \mathfrak{c} \neq \aleph_\omega, \aleph_{\omega_1}, \beth_\omega$, and generally $\mathfrak c$ is not singular. $\mathrm{MA}_{\aleph_1} \Rightarrow \mathfrak{c} \ge \aleph_2$ and $2^{\aleph_1} = \mathfrak c$.
- **Axioms that do pin $\mathfrak{c} = \aleph_2$:** $\mathrm{PFA}$; $\mathrm{MM}$; $\mathrm{MRP}$; $\mathrm{BPFA}$; the two-coloring axiom of Moore (2002); $\psi_{\mathrm{AC}}$-type reflection principles; Woodin's $(*)$.
- **Axioms compatible with $\mathfrak{c} > \aleph_2$:** $\mathrm{MA}$ itself; $\mathrm{MA}(\sigma\text{-centered})$ (i.e. $\mathfrak p = \mathfrak c$); $\mathrm{MA}_{\aleph_1}$ + "all $\aleph_1$-dense sets of *size-$\aleph_1$ Cohen-generic* type isomorphic"; various Asperó–Mota fragments of $\mathrm{PFA}$ for finitely proper posets with $\mathfrak{c} = \aleph_3$.
- **Consequences of $\mathrm{OCA}$ known in $\mathrm{ZFC}$:** $\mathfrak{b} = \aleph_2$ (Todorcevic 1989); every automorphism of $\mathcal{P}(\omega)/\mathrm{fin}$ is trivial (Veličković, Shelah–Steprāns for related axioms); $\mathfrak{a} = \aleph_2$; no towers of height $>\aleph_2$ (Farah). All these give $\aleph_2$-sized *characteristics*, not $\mathfrak c = \aleph_2$.

## 5. Principal Obstacles

- **ccc forcing is too flexible.** Any ccc iteration can be lengthened. Given a model of $\mathrm{MA} + \mathfrak c = \aleph_2$, iterating $\aleph_3$ more steps yields $\mathrm{MA} + \mathfrak c = \aleph_3$. Any axiom that is preserved by, or generically forced along, long finite-support ccc iterations cannot bound $\mathfrak c$.
- **Absence of reflection.** The $\mathrm{PFA} \Rightarrow \mathfrak{c} = \aleph_2$ proofs run through stationary reflection on $[\lambda]^{\omega}$, or through collapsing a cardinal to code a subset of $\omega_1$ — both need proper forcings that destroy stationary sets or add uncountable branches. ccc forcings preserve stationary subsets of $\omega_1$ and add no new $\omega_1$-sequences of ordinals, so the coding is unavailable.
- **Colorings only see $\aleph_2$.** $\mathrm{OCA}$-style axioms bound *cardinal characteristics* by $\aleph_2$ (via oscillation and walks on ordinals producing $\aleph_2$-sized structures) but say nothing about the total number of reals. There is no known device translating "$\mathfrak b = \aleph_2$" into "$|\mathbb{R}| = \aleph_2$".
- **Forcing $\mathrm{OCA}$ with $\mathfrak{c} > \aleph_2$ is blocked.** The only known method of forcing $\mathrm{OCA}$ is a countable-support proper iteration of length $\omega_2$, which forces $\mathfrak c = \aleph_2$ automatically ($\aleph_2$-cc plus adding reals cofinally). Finite-support and side-condition variants that keep $\mathfrak c$ large have so far failed to preserve $\mathrm{OCA}$ through limit stages: the open coloring at stage $\alpha$ can be revived by later Cohen reals.
- **No inner-model or descriptive-set-theoretic bound.** $\mathrm{MA}$ implies $\Sigma^1_2$-regularity but gives no upper bound on $|\mathbb{R}|$ in any canonical inner model, so the $\Omega$-logic / $(*)$ machinery that fixes $\mathfrak c = \aleph_2$ under $\mathrm{MM}^{++}$ has no ccc analogue.

## 6. The Gap

Proven: $\mathrm{MA}$ constrains $\mathfrak c$ to $\{\kappa \text{ regular} : \kappa^{<\kappa} = \kappa\}$, and no more. Also proven: certain *non-ccc* strengthenings force $\mathfrak c = \aleph_2$. The gap is the intermediate zone.

The precise unresolved step for $\mathrm{OCA}$: build a proper (or semi-proper, or finitely-proper-with-side-conditions) forcing iteration $\langle \mathbb{P}_\alpha : \alpha \le \omega_3 \rangle$ that (i) adds $\aleph_3$ reals, (ii) is $\aleph_2$-preserving, and (iii) at every limit stage preserves the "$K_0$-homogeneous uncountable set or countable $K_1$-decomposition" dichotomy for colorings appearing earlier. Requirement (iii) is where every known construction fails: preservation of $\mathrm{OCA}$ under limits is not known to follow from any iterable preservation property. Conversely, a $\mathrm{ZFC}$ proof of $\mathrm{OCA} \Rightarrow \mathfrak{c} = \aleph_2$ would need a coloring on a set of size $\aleph_2$ whose dichotomy encodes a surjection $\omega_2 \to \mathbb{R}$ — no candidate coloring is known.

## 7. Current Research (as of June 2026)

- **Side-condition iterations** (Asperó, Mota, and collaborators, Universitat de Barcelona / East Anglia / UNAM): symmetric systems of countable elementary submodels used as finite side conditions, producing fragments of $\mathrm{PFA}$ with $\mathfrak{c} = \aleph_3$ or larger. The programme's stated target is exactly whether $\mathrm{OCA}$ or $\mathrm{BA}$ can be added. *(frontier — verify)*
- **Todorcevic school** (Toronto / Paris / Belgrade): walks on ordinals, oscillation mappings, and $\rho$-functions used to derive $\aleph_2$-bounds from partition hypotheses; the search continues for a coloring that bounds $\mathfrak{c}$ rather than $\mathfrak{b}$.
- **Farah, Vignati and collaborators** on $\mathrm{OCA}$-consequences in operator algebras (rigidity of corona algebras) — these results are $\mathfrak c$-agnostic, which is itself evidence that $\mathrm{OCA}$ may not decide $\mathfrak c$.
- **Forcing axioms and $(*)$** post-Asperó–Schindler: work on whether $(*)$-fragments have ccc analogues; consensus is that they do not, sharpening the ccc/proper divide.
- **Cardinal-characteristic models** (Goldstern, Kellner, Mejía, Shelah): creature and ultrafilter-limit techniques giving many simultaneously-distinct characteristics with $\mathfrak{c}$ large, which map the outer boundary of what ccc-style axioms can control. *(frontier — verify)*

## 8. Future Work

- Isolate an *iterable* preservation property for $\mathrm{OCA}$ analogous to preservation of $\square$-properness, then run a length-$\omega_3$ iteration to get $\mathrm{OCA} + \mathfrak{c} = \aleph_3$.
- Determine whether $\mathrm{BA}$ implies $\mathfrak c = \aleph_2$; the Abraham–Rubin–Shelah model gives $\mathrm{BA} + \mathfrak c = \aleph_2$ but no model with $\mathfrak c > \aleph_2$ is known.
- Classify all $\Pi_2$-statements about $H(\mathfrak{c}^+)$ consistent with $\mathrm{MA} + \mathfrak c = \aleph_3$: a "maximality" analysis paralleling $\mathrm{BMM}$.
- Study $\mathfrak{m}$ separately from $\mathfrak c$: is $\mathrm{MA}_{\aleph_1} + \mathfrak{m} = \aleph_2 + \mathfrak{c} = \aleph_4$ compatible with strong colouring axioms? Little is known about the possible pairs $(\mathfrak{m}, \mathfrak{c})$ beyond $\aleph_1 \le \mathfrak m \le \mathfrak c$ with $\mathfrak m$ regular.
- Investigate whether higher-analogue axioms $\mathrm{MA}(\kappa\text{-cc})$ at $\kappa = \aleph_1$ (which are inconsistent in naive form) admit repaired versions bounding $2^{\aleph_1}$, feeding back to $\mathfrak c$.

## 9. Key References

- **[Foundational]** D. A. Martin and R. M. Solovay. *Internal Cohen extensions.* Annals of Mathematical Logic 2 (1970), 143–178.
- **[Foundational]** R. M. Solovay and S. Tennenbaum. *Iterated Cohen extensions and Souslin's problem.* Annals of Mathematics 94 (1971), 201–245.
- **[Foundational]** J. E. Baumgartner. *All $\aleph_1$-dense sets of reals can be isomorphic.* Fundamenta Mathematicae 79 (1973), 101–106.
- **[Survey]** D. H. Fremlin. *Consequences of Martin's Axiom.* Cambridge Tracts in Mathematics 84, Cambridge University Press, 1984.
- **[Textbook]** K. Kunen. *Set Theory.* Studies in Logic 34, College Publications, 2011.
- **[Foundational]** M. Bell. *On the combinatorial principle $P(\mathfrak c)$.* Fundamenta Mathematicae 114 (1981), 149–157.
- **[Foundational]** U. Abraham and S. Shelah. *Martin's axiom does not imply that every two $\aleph_1$-dense sets of reals are isomorphic.* Israel Journal of Mathematics 38 (1981), 161–176.
- **[Foundational]** U. Abraham, M. Rubin, S. Shelah. *On the consistency of some partition theorems for continuous colorings, and the structure of $\aleph_1$-dense real order types.* Annals of Pure and Applied Logic 29 (1985), 123–206.
- **[Foundational]** S. Todorcevic. *Partition Problems in Topology.* Contemporary Mathematics 84, American Mathematical Society, 1989.
- **[Foundational]** S. Todorcevic and B. Veličković. *Martin's axiom and partitions.* Compositio Mathematica 63 (1987), 391–408.
- **[Foundational]** M. Foreman, M. Magidor, S. Shelah. *Martin's Maximum, saturated ideals, and non-regular ultrafilters. Part I.* Annals of Mathematics 127 (1988), 1–47.
- **[SOTA]** B. Veličković. *Forcing axioms and stationary sets.* Advances in Mathematics 94 (1992), 256–284.
- **[SOTA]** J. T. Moore. *Open colorings, the continuum and the second uncountable cardinal.* Proceedings of the American Mathematical Society 130 (2002), 2753–2759.
- **[SOTA]** J. T. Moore. *Set mapping reflection.* Journal of Mathematical Logic 5 (2005), 87–97.
- **[SOTA]** D. Asperó and M. A. Mota. *Forcing consequences of PFA together with the continuum large.* Transactions of the American Mathematical Society 367 (2015), 6103–6129.
- **[SOTA]** D. Asperó and R. Schindler. *Martin's Maximum$^{++}$ implies Woodin's Axiom $(*)$.* Annals of Mathematics 193 (2021), 793–835.
- **[Survey]** A. Blass. *Combinatorial cardinal characteristics of the continuum.* In: Handbook of Set Theory, Springer, 2010, 395–489.
- **[Survey]** T. Bartoszyński and H. Judah. *Set Theory: On the Structure of the Real Line.* A K Peters, 1995.

## 10. Worked Example / Concrete Special Case

**(a) $\mathrm{MA}(\mathfrak{c})$ fails — so $\mathfrak{m} \le \mathfrak{c}$.** Let $\mathbb{P} = \mathrm{Fn}(\omega,2)$, the finite partial functions $p : \omega \rightharpoonup 2$ ordered by reverse inclusion. $\mathbb{P}$ is countable, hence ccc. Take the dense sets
$$E_n = \{p \in \mathbb{P} : n \in \mathrm{dom}(p)\}\ (n<\omega), \qquad D_x = \{p \in \mathbb{P} : \exists n \in \mathrm{dom}(p),\ p(n) \neq x(n)\}\ (x \in 2^\omega).$$
Each $E_n$ is dense (extend $p$ at $n$). Each $D_x$ is dense: given $p$, pick $n \notin \mathrm{dom}(p)$ and set $q = p \cup \{(n, 1-x(n))\}$. That is $\aleph_0 + \mathfrak{c} = \mathfrak{c}$ dense sets. A filter $G$ meeting all of them yields $f = \bigcup G \in 2^\omega$ (total by the $E_n$, a function by directedness) with $f \neq x$ for every $x \in 2^\omega$ — absurd. Hence $\neg\mathrm{MA}(\mathfrak c)$.

**(b) $\mathrm{MA}(\kappa) \Rightarrow 2^\kappa = \mathfrak{c}$, hence $\mathfrak c \neq \aleph_\omega$ under $\mathrm{MA}$.** Fix $\kappa < \mathfrak c$ and an almost disjoint family $\{A_\alpha : \alpha < \kappa\} \subseteq [\omega]^\omega$. For $X \subseteq \kappa$ use the ccc poset $\mathbb{Q}_X$ of pairs $(s, F)$ with $s \in [\omega]^{<\omega}$, $F \in [X]^{<\omega}$, ordered by $(s',F') \le (s,F)$ iff $s' \supseteq s$, $F' \supseteq F$, and $(s' \setminus s) \cap A_\alpha = \emptyset$ for $\alpha \in F$. $\mathbb{Q}_X$ is $\sigma$-centered (conditions with the same $s$ are compatible), hence ccc. Meeting $\kappa + \aleph_0$ dense sets gives $d \in [\omega]^\omega$ with $|d \cap A_\alpha| < \aleph_0$ for $\alpha \in X$ and $|d \cap A_\alpha| = \aleph_0$ for $\alpha \in \kappa \setminus X$. The map $X \mapsto d_X$ is injective into $\mathcal{P}(\omega)$, so $2^\kappa \le \mathfrak{c} \le 2^\kappa$.

Now suppose $\mathrm{MA}$ and $\mathfrak c = \aleph_\omega$. Then $\kappa = \aleph_0 < \mathfrak c$ gives nothing, but $\kappa = \aleph_n$ for each $n$ gives $2^{\aleph_n} = \aleph_\omega$, so $\aleph_\omega^{\aleph_0} = \aleph_\omega$, contradicting König: $\mathrm{cf}(2^{\aleph_0}) > \aleph_0$ while $\mathrm{cf}(\aleph_\omega) = \aleph_0$. So $\mathfrak c \neq \aleph_\omega$.

**(c) Both $\aleph_2$ and $\aleph_3$ are realised.** Start with $V \models \mathrm{GCH}$ and let $\kappa \in \{\aleph_2, \aleph_3\}$ (both regular, both satisfy $\kappa^{<\kappa} = \kappa$ under GCH). Build a finite-support iteration $\langle \mathbb{P}_\alpha, \dot{\mathbb{Q}}_\alpha : \alpha < \kappa\rangle$ where bookkeeping enumerates, in order type $\kappa$, all $\mathbb{P}_\alpha$-names for ccc posets of size $<\kappa$ and forces with each cofinally often. Finite support preserves ccc at limits (Solovay–Tennenbaum), $|\mathbb{P}_\kappa| = \kappa$, so $\mathbb{P}_\kappa$ is $\kappa$-cc and preserves cardinals. In $V^{\mathbb{P}_\kappa}$: $\mathfrak{c} = \kappa$ (Cohen reals added cofinally; nomore than $\kappa$ reals by counting nice names), and $\mathrm{MA}$ holds because any ccc poset in the extension has a dense subset of size $<\kappa$ appearing at some stage $\alpha < \kappa$ by $\kappa$-cc reflection, and was handled by the bookkeeping.

So the *same* axiom $\mathrm{MA}$, the *same* consequences ($\mathfrak p = \mathfrak b = \mathfrak d = \mathfrak c$, no Souslin lines, $\Sigma^1_2$-measurability), sit on top of two different continua. Any axiom that decides between them must fail to be forceable by this iteration — which is exactly what $\mathrm{OCA}$'s status leaves undetermined.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*