---
id: 08-logic-set-theory/gap-one-morass-existence
title: "Gap One Morass Existence"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gap One Morass Existence

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/gap-one-morass-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A **gap-1 morass at $\kappa$** (a $(\kappa,1)$-morass) is a coherent directed system of small structures whose direct limit is $\kappa^{+}$, engineered so that combinatorial objects of size $\kappa^{+}$ can be built by transfinite recursion of length $\kappa$ using only approximations of size $<\kappa$. Jensen proved that such systems exist in $L$ for every uncountable regular $\kappa$.

The open cluster of questions is:

1. **Strength of failure.** What is the exact consistency strength of "there is no $(\kappa,1)$-morass" for $\kappa = \omega_1$, $\kappa = \omega_2$, and for $\kappa$ singular-successor-adjacent settings such as $\kappa = \aleph_\omega$ (morass at $\aleph_{\omega+1}$)? Failure is known to be strictly stronger than ZFC, but a matching upper and lower bound in the large-cardinal hierarchy is not established for all $\kappa$.
2. **Axiomatic sufficiency.** Does $\mathrm{CH}$ (rather than $\diamondsuit$) imply the existence of a simplified $(\omega_1,1)$-morass? More generally, does $\square_\kappa + \mathrm{GCH}$ suffice at every $\kappa$, or is a genuine fine-structural input irreducible?
3. **Equivalence.** Are Jensen $(\kappa,1)$-morasses and Velleman simplified $(\kappa,1)$-morasses equivalent as ZFC statements at every $\kappa$ (both directions of the translation are known only under extra hypotheses at some $\kappa$)?

A complete resolution of (1) means an inner-model lower bound and a forcing upper bound that meet; of (2), either a ZFC + CH construction or a model of CH with no morass at $\omega_1$.

## 2. Mathematical Foundations

**Jensen $(\kappa,1)$-morass (standard presentation, Devlin 1984, Ch. VIII).** For $\kappa$ regular uncountable, a morass is a structure
$$\mathfrak{M} = \big\langle \langle S_\alpha : \alpha \le \kappa\rangle,\ \langle \pi_{\sigma\tau} : \sigma \prec_{\!\mathfrak{M}} \tau \rangle \big\rangle$$
where each $S_\alpha$ is a set of ordinals $\le \kappa^{+}$ with $S_\kappa = \{\kappa^{+}\}$ (top level) and $|S_\alpha| \le |\alpha| + \omega$ for $\alpha<\kappa$; $\prec_{\!\mathfrak{M}}$ is a tree order on $S = \bigcup_\alpha (\{\alpha\}\times S_\alpha)$ of height $\kappa+1$; and for $\sigma \prec_{\!\mathfrak{M}} \tau$, $\pi_{\sigma\tau} : \sigma \to \tau$ is order preserving. The axioms require: **(M1)** tree levels are $\le\kappa$-branching with $\prec$-predecessors linearly ordered; **(M2)** coherence, $\pi_{\tau\upsilon}\circ\pi_{\sigma\tau} = \pi_{\sigma\upsilon}$; **(M3)** *continuity/direct-limit*, at limit levels $\lambda$ each $\tau \in S_\lambda$ is the direct limit $\tau = \bigcup\{\pi_{\sigma\tau}[\sigma]\}$ over a cofinal branch, and $\kappa^{+}$ itself is the direct limit of the whole system; **(M4)** *continuous branching / amalgamation*, giving that maps into a fixed node split at a point which is itself a node of the system.

**Velleman simplified $(\kappa,1)$-morass** (Velleman 1984). A pair
$$\big\langle \langle \theta_\alpha : \alpha \le \kappa\rangle,\ \langle \mathcal{F}_{\alpha\beta} : \alpha<\beta\le\kappa\rangle \big\rangle$$
with $\theta_0 = 1$, $0<\theta_\alpha<\kappa$ for $\alpha<\kappa$, $\theta_\kappa = \kappa^{+}$, and each $\mathcal{F}_{\alpha\beta}$ a **finite** set of order-preserving maps $\theta_\alpha \to \theta_\beta$, satisfying:

- **(P1)** *successors split once*: $\mathcal{F}_{\alpha,\alpha+1} = \{\mathrm{id}\!\restriction\!\theta_\alpha,\ e_\alpha\}$ where for some $\delta_\alpha \le \theta_\alpha$, $e_\alpha\!\restriction\!\delta_\alpha = \mathrm{id}$ and $e_\alpha(\delta_\alpha) \ge \theta_\alpha$;
- **(P2)** *composition*: $\mathcal{F}_{\alpha\gamma} = \{\,g\circ f : f\in\mathcal{F}_{\alpha\beta},\ g\in\mathcal{F}_{\beta\gamma}\,\}$ for $\alpha<\beta<\gamma$;
- **(P3)** *direct limits*: for limit $\lambda \le \kappa$, $\theta_\lambda = \bigcup_{\alpha<\lambda}\bigcup\{f[\theta_\alpha] : f\in\mathcal{F}_{\alpha\lambda}\}$ and the system $\langle \theta_\alpha,\mathcal{F}_{\alpha\lambda}\rangle_{\alpha<\lambda}$ is directed;
- **(P4)** *amalgamation*: for $f,g \in \mathcal{F}_{\alpha\beta}$ the two ranges agree below their splitting point, $f\!\restriction\!\delta = g\!\restriction\!\delta$ and $f[\theta_\alpha]\cap g[\theta_\alpha] = f[\delta]$ for some $\delta \le \theta_\alpha$, and the amalgam is again realized by maps of the system.

The point of (P1)–(P4) is the **morass-recursion principle**: to construct an object $X$ of size $\kappa^{+}$ it suffices to construct $X_\alpha$ of size $|\theta_\alpha| < \kappa$ for $\alpha<\kappa$ so that each $f \in \mathcal{F}_{\alpha\beta}$ lifts to an embedding $X_\alpha \to X_\beta$, and to verify **finitely many** amalgamation constraints at each step. The relevant transfer consequence is the two-cardinal principle
$$(\kappa^{+},\kappa) \twoheadrightarrow (\kappa,{<}\kappa)\quad\text{(Jensen gap-1 transfer)},$$
of which $(\aleph_2,\aleph_1)\twoheadrightarrow(\aleph_1,\aleph_0)$ is the classical instance.

## 3. History & State of the Art (SOTA)

- **1972.** Jensen's fine structure of $L$ (Ann. Math. Logic 4) supplies $\square_\kappa$ and $\diamondsuit$; morasses are constructed from the same $\Sigma_n$-hull machinery, first circulated in Jensen's handwritten notes and published in Devlin, *Constructibility* (1984) and Stanley's course notes (1983). Jensen: $V=L \Rightarrow$ a $(\kappa,1)$-morass exists for every regular uncountable $\kappa$.
- **1982.** Shelah–Stanley, "S-forcing I", extract a black-box theorem letting morasses drive forcing constructions (super-Souslin trees), decoupling applications from fine structure.
- **1982–84.** Velleman isolates the *simplified* morass: the finite-map formulation above. He shows $\diamondsuit$ gives a simplified $(\omega_1,1)$-morass, and — crucially — that a simplified $(\omega_1,1)$-morass can be added by a **ccc** forcing, so morasses at $\omega_1$ are compatible with $\mathrm{MA}+\neg\mathrm{CH}$ and carry no $L$-like side effects.
- **1985.** Donder, "Another look at gap-1 morasses": gap-1 morasses exist in the core model, so failure at any $\kappa$ has genuine large-cardinal strength. This converts the existence question into a strength-calibration question.
- **1987–98.** Velleman's simplified gap-2 morasses and Morgan's "Higher gap morasses I" (JSL 1998) push the schema past gap 1, exposing which gap-1 arguments were accidental.
- **2000s–present.** Irrgang's morass-driven forcing iterations (e.g. Proc. AMS 137 (2009)) and Zeman's extender-model fine structure make the constructions available in $L[E]$ far above measurables.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $V=L$, any regular uncountable $\kappa$ | **Solved** (Jensen): $(\kappa,1)$-morass exists; likewise gap-$n$ for all $n<\omega$. |
| Core model $K$ / extender models $L[E]$ below suitable large cardinals | **Solved** (Donder 1985; Zeman 2002): morasses exist at every uncountable regular $\kappa$ of the model. |
| $\kappa=\omega_1$, $\diamondsuit$ | Simplified $(\omega_1,1)$-morass exists (Velleman 1984). |
| $\kappa=\omega_1$, $\mathrm{MA}_{\aleph_1}+\neg\mathrm{CH}$ | Consistent **with** a morass: a ccc poset of size $\aleph_1$ adds one (Velleman 1982/84). |
| $\kappa$ with $\square_\kappa + \mathrm{GCH}$ plus a suitable $\diamondsuit$-like guessing sequence | Morass constructible by the Velleman-style recursion. |
| Gap 2, $V=L$ | Simplified gap-2 morasses exist (Velleman 1987; Morgan 1998). |
| Failure of gap-1 morass at $\kappa$ | Implies existence of inner models with large cardinals (Donder); not provable consistent from ZFC alone. |

Applications verified from a gap-1 morass alone: $\kappa^{+}$-Souslin/super-Souslin trees, Kurepa-type families, $\kappa^{+}$-sized graphs with all subgraphs of size $\kappa$ well-behaved (chromatic-number transfers), the two-cardinal transfer $(\kappa^{+},\kappa)\twoheadrightarrow(\kappa,{<}\kappa)$, and finite-support iterations of length $\omega_2$ with $\aleph_2$-cc.

## 5. Principal Obstacles

- **No forcing route to failure.** Morasses are $\Sigma^1_2$-like existence statements about $\kappa^{+}$; forcing tends to *add* morasses (Velleman's ccc poset) and cannot easily destroy all of them, since a morass in $V$ typically survives $\kappa^{+}$-cc extensions. Killing every morass requires killing all $\square$-and-condensation-flavoured structure at $\kappa^{+}$, which is exactly what large cardinals do — hence the strength.
- **Covering-lemma lower bounds saturate.** Donder's argument runs a core-model construction and reads a morass off the fine structure of $K$. It stops precisely where $K$ stops being constructible under current technology, so the lower bound for failure at large $\kappa$ tracks the frontier of inner model theory rather than the morass problem itself.
- **Amalgamation is not a first-order local property.** Axiom (P4) constrains *finite* families of maps at every level simultaneously; approximations built by ordinary elementary-submodel reflection satisfy coherence but generically fail the splitting-point identity $f[\theta_\alpha]\cap g[\theta_\alpha]=f[\delta]$. There is no known "generic amalgamation" lemma replacing condensation.
- **Guessing vs. condensation.** $\diamondsuit$ suffices at $\omega_1$; $\mathrm{CH}$ alone gives the cardinal arithmetic but not the coherence of the branching, and no CH-only construction is known. Conversely no CH model has been shown morass-free.
- **Singular-successor case.** At $\kappa^{+}$ with $\kappa$ singular, $\square_\kappa$ interacts with scales and PCF; the level-by-level recursion of length $\kappa$ must cross cofinalities, and the standard successor step (P1) has no uniform analogue.

## 6. The Gap

Proven: morasses exist in every canonical inner model, at every uncountable regular $\kappa$; and they can be forced to exist over any model, cheaply, at $\omega_1$. Missing: any model of ZFC in which one can *point to* the absence of a gap-1 morass with a computed strength. Concretely, the boundary is a pair of unmatched bounds

$$\text{Con}(\text{no } (\kappa,1)\text{-morass}) \ \Longrightarrow\ \text{Con}(\text{inner model with large cardinals})\quad\text{(Donder, lower)},$$

with **no known upper bound** of the form "$\text{Con}(\text{large cardinal }\Phi)\Rightarrow\text{Con}(\text{no }(\kappa,1)\text{-morass})$" that is tight. The single step to be crossed: a forcing (or inner-model) construction that destroys all gap-1 morasses at a chosen $\kappa$ from a specified hypothesis $\Phi$, with $\Phi$ at the level Donder's argument requires. The parallel step for question (2) is either a $\mathrm{CH}$-only amalgamation lemma or a CH-preserving morass-killing forcing at $\omega_1$.

## 7. Current Research (as of June 2026)

- **Fine structure in extender models.** Continuation of Zeman-style $L[E]$ analysis to build morasses (and higher-gap morasses) above Woodin-cardinal-level extenders, where condensation is weaker. *(frontier — verify)*
- **Morass-guided iterated forcing.** Irrgang's programme — using simplified morasses as the index structure for finite-support iterations to obtain $\aleph_2$-cc constructions — continues to generate applications (higher-dimensional $\Delta$-systems, $\aleph_2$-Souslin objects) and thereby sharper equivalent forms of the existence statement.
- **Simplified vs. Jensen morasses.** Ongoing work on the exact equivalence of the two formulations at $\kappa>\omega_1$ and at singular-successor cardinals; the translation is delicate in the direction simplified $\Rightarrow$ Jensen. *(frontier — verify)*
- **Higher gaps and $\omega$-gap morasses.** Morgan-style condensation analyses for gap $\ge 2$, and reported gap-$\omega$ frameworks. *(frontier — verify)*
- Groups: Bonn/Münster (inner model theory and morass-forcing), Bristol/London (Morgan), and the Israeli PCF-adjacent school for the singular case.

## 8. Future Work

- Calibrate the failure of a $(\omega_2,1)$-morass against the strength of the failure of $\square_{\omega_1}$, and decide whether the two are equiconsistent.
- Seek a "generic morass" forcing at singular-successor cardinals, or prove that $\square_\kappa+\mathrm{GCH}$ already implies a $(\kappa^{+},1)$-morass for $\kappa$ singular.
- Settle whether $\mathrm{CH}$ implies a simplified $(\omega_1,1)$-morass.
- Develop a purely combinatorial (condensation-free) construction of simplified morasses that survives to extender models with no fine-structural condensation.
- Catalogue which known $\aleph_2$ constructions genuinely require morasses versus $\square_{\omega_1}+\mathrm{CH}$, sharpening the applied content of the existence question.

## 9. Key References

- **[Foundational]** R. B. Jensen. *The fine structure of the constructible hierarchy.* Annals of Mathematical Logic **4** (1972), 229–308.
- **[Foundational]** K. J. Devlin. *Constructibility.* Perspectives in Mathematical Logic, Springer-Verlag, 1984. (Chapter on gap-1 morasses in $L$.)
- **[Foundational]** L. J. Stanley. *A short course on gap-one morasses with a review of the fine structure of $L$.* In: A. R. D. Mathias (ed.), *Surveys in Set Theory*, LMS Lecture Note Series 87, Cambridge University Press, 1983.
- **[Foundational]** D. Velleman. *Simplified morasses.* Journal of Symbolic Logic **49** (1984), 257–271.
- **[Foundational]** D. Velleman. *Morasses, diamond, and forcing.* Annals of Mathematical Logic **23** (1982), 199–281.
- **[SOTA]** H.-D. Donder. *Another look at gap-1 morasses.* In: *Recursion Theory*, Proceedings of Symposia in Pure Mathematics **42**, American Mathematical Society, 1985.
- **[SOTA]** D. Velleman. *Simplified gap-2 morasses.* Annals of Pure and Applied Logic **34** (1987), 171–208.
- **[SOTA]** C. J. B. Morgan. *Higher gap morasses, I: gap-two morasses and condensation.* Journal of Symbolic Logic **63** (1998), 753–787.
- **[SOTA]** B. Irrgang. *Morasses and finite support iterations.* Proceedings of the American Mathematical Society **137** (2009), 1103–1113.
- **[SOTA]** S. Shelah and L. Stanley. *S-forcing, I: a "black-box" theorem for morasses, with applications to super-Souslin trees.* Israel Journal of Mathematics **43** (1982), 185–224.
- **[Survey]** A. Kanamori. *Morasses in combinatorial set theory.* In: *Surveys in Set Theory*, LMS Lecture Note Series 87, Cambridge University Press, 1983.
- **[Survey / background]** M. Zeman. *Inner Models and Large Cardinals.* de Gruyter Series in Logic and its Applications 5, 2002.

## 10. Worked Example / Concrete Special Case

**The successor step and one amalgamation check, at $\kappa=\omega_1$.**

Take $\theta_0 = 1$ and build the first few levels of a simplified $(\omega_1,1)$-morass.

- Level 1: split $\theta_0=1$ at $\delta_0 = 0$, so $e_0(0) = 1$ and $\theta_1 = \theta_0 \cup e_0[\theta_0] = 2$, with $\mathcal{F}_{01} = \{\mathrm{id},\, e_0\}$, $\mathrm{id}(0)=0$, $e_0(0)=1$.
- Level 2: split $\theta_1 = 2$ at $\delta_1 = 1$: $e_1(0)=0$, $e_1(1) = 2$, and $\theta_2 = 3 = \{0,1,2\}$. So $\mathcal{F}_{12} = \{\mathrm{id}_2, e_1\}$.
- By (P2), $\mathcal{F}_{02} = \{\mathrm{id}\circ\mathrm{id},\ \mathrm{id}\circ e_0,\ e_1\circ \mathrm{id},\ e_1\circ e_0\}$, i.e. the maps $0\mapsto 0$, $0\mapsto 1$, $0\mapsto 0$, $0\mapsto 2$ — three distinct maps $f_0,f_1,f_2$ with $f_i(0)=i$. Finiteness (P1's finite-set requirement) holds: $|\mathcal{F}_{02}| = 3$.

**Amalgamation check (P4)** on $f_0,f_2 \in \mathcal{F}_{02}$: the splitting point is $\delta = 0$, since $f_0\!\restriction\!0 = f_2\!\restriction\!0 = \emptyset$ and
$$f_0[\theta_0]\cap f_2[\theta_0] = \{0\}\cap\{2\} = \emptyset = f_0[0],$$
as required. The same computation for $f_0,f_1$ gives $\delta=0$ again. So the constraint is verified by two set intersections, not by an elementarity argument — this is exactly the economy morasses buy.

**Why this scales to $\kappa^{+}$.** Suppose we want a family $\mathcal{A}\subseteq[\omega_2]^{\omega}$ of size $\aleph_2$ that is *almost disjoint*. Using a simplified $(\omega_1,1)$-morass with $\theta_{\omega_1} = \omega_2$, build $\mathcal{A}_\alpha \subseteq [\theta_\alpha]^{\le\omega}$ for $\alpha<\omega_1$ with $|\mathcal{A}_\alpha| \le |\theta_\alpha| <\aleph_1$, requiring only:

1. each $f\in\mathcal{F}_{\alpha\beta}$ maps $\mathcal{A}_\alpha$ into $\mathcal{A}_\beta$ (so $f[A]\in\mathcal{A}_\beta$ for $A\in\mathcal{A}_\alpha$);
2. at the successor step, when $\theta_{\alpha+1} = \theta_\alpha \cup e_\alpha[\theta_\alpha]$, the copies $A$ and $e_\alpha[A]$ meet in $A\cap\delta_\alpha$ only — a **single** condition, checkable because $|\mathcal{A}_\alpha|<\aleph_1$;
3. limits are unions, forced by (P3).

Then $\mathcal{A} = \bigcup_{\alpha<\omega_1}\bigcup\{f[A] : f\in\mathcal{F}_{\alpha\omega_1},\, A\in\mathcal{A}_\alpha\}$ has size $\aleph_2$ and is almost disjoint, because any two members descend by (P4) to two maps out of a common $\theta_\alpha$ whose ranges meet exactly in the image of the splitting point $\delta$, a countable initial segment. A direct construction at $\omega_2$ would need $\aleph_2$-many steps and $\aleph_1$-many bookkeeping conditions per step; the morass compresses this to $\aleph_1$ steps with finitely many conditions each. The open problem of Section 1 is whether this compression device can be *removed* from the universe at all, and at what price in large cardinals.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*