---
id: 08-logic-set-theory/ordinal-analysis-pi-1-2-comprehension
title: "Ordinal Analysis of Pi-1-2 Comprehension"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ordinal Analysis of Π¹₂ Comprehension

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/ordinal-analysis-pi-1-2-comprehension` · **Status:** open

## 1. Problem Statement / Conjecture

Give a complete ordinal analysis of the subsystem of second-order arithmetic
$$\Pi^1_2\text{-CA}_0 \;=\; \text{ACA}_0 + \{\exists X\,\forall n\,(n \in X \leftrightarrow \varphi(n)) : \varphi \in \Pi^1_2\},$$
and of its extension $\Pi^1_2\text{-CA} + \text{BI}$ (full induction plus bar induction).

Concretely, the task is to produce:

1. a **primitive recursive ordinal notation system** $(\mathcal{T}, \prec)$, given by explicit term syntax and a decidable comparison relation;
2. a **proof of the identity** $|\Pi^1_2\text{-CA}_0| = \mathrm{otyp}(\mathcal{T},\prec)$, where the proof-theoretic ordinal is
$$|T| \;=\; \sup\{\,\mathrm{otyp}(\prec) : \prec \text{ a primitive recursive well-ordering of } \mathbb{N},\ T \vdash \mathrm{WO}(\prec)\,\};$$
3. the two matching halves: an **upper bound** (cut elimination / collapsing, giving $T \vdash \mathrm{WO}(\prec) \Rightarrow \mathrm{otyp}(\prec) < \mathrm{otyp}(\mathcal{T})$) and a **lower bound** (a well-ordering proof of each proper initial segment of $\mathcal{T}$ inside $T$);
4. the standard corollaries such analyses always yield: characterisation of the provably total recursive functions, of the provably $\Pi^0_2$ statements, and a finitistic consistency reduction of $T$ to $\mathrm{PRA} + \mathrm{TI}(\mathcal{T})$.

A complete solution must have both bounds and a notation system whose well-foundedness is not simply assumed. The problem is open for full $\Pi^1_2$-CA.

## 2. Mathematical Foundations

**Second-order arithmetic.** $\Pi^1_2$ formulas have the shape $\forall X\,\exists Y\,\theta(X,Y,\ldots)$ with $\theta$ arithmetical. $\Pi^1_2$-CA sits strictly above $\Pi^1_1$-CA and $\Delta^1_2$-CA in the Simpson hierarchy.

**Set-theoretic counterpart.** Ordinal analysis proceeds through Kripke–Platek set theory. Write $\mathrm{KP}$ for KP with infinity, $\mathrm{KPi}$ for KP $+$ "every set lies in an admissible set". Then:

- $|\mathrm{KP}| = |\mathrm{ID}_1| = \psi_\Omega(\varepsilon_{\Omega+1})$, the Bachmann–Howard ordinal;
- $|\Pi^1_1\text{-CA}_0| = \psi_\Omega(\Omega_\omega)$ and $|\Pi^1_1\text{-CA}+\text{BI}| = \psi_\Omega(\varepsilon_{\Omega_\omega+1})$;
- $|\Delta^1_2\text{-CA}+\text{BI}| = |\mathrm{KPM}| = \psi(\varepsilon_{M+1})$ (recursively Mahlo, Rathjen 1990–91);
- $\Pi^1_2$-CA corresponds to **$\Sigma_1$-separation** over KP, and hence to **stability**.

**Stability.** For $\alpha < \beta$, $L_\alpha \prec_1 L_\beta$ means $L_\alpha$ is a $\Sigma_1$-elementary substructure of $L_\beta$. An ordinal $\sigma$ is *stable* if $L_\sigma \prec_1 L$. The relevant reflection principle is
$$\forall x\,\exists \sigma\,\big(x \in L_\sigma \wedge L_\sigma \prec_1 L\big),$$
which is the set-theoretic shadow of $\Pi^1_2$ comprehension: a $\Pi^1_2$ statement $\forall X \exists Y\,\theta$ is absolute exactly across a $\Sigma_1$-elementary cut.

**Reflection ladder.** Ordinal strength climbs
$$\text{admissible} \;<\; \text{recursively inaccessible} \;<\; \text{recursively Mahlo} \;<\; \Pi_3\text{-reflection} \;<\; \Pi_n\text{-reflection} \;<\; \text{stability}.$$
Stability is a *second-order* condition on $L_\sigma$ — it quantifies over all of $L$, not over sets in $L_\sigma$ — and this jump is where the method breaks.

**Collapsing functions.** All known analyses use a hierarchy of regular (or recursively regular) ordinals $\Omega_1 < \Omega_2 < \cdots$ and collapsing functions $\psi_{\Omega_i}$ with the characteristic clause
$$\psi_\Omega(\alpha) \;=\; \min\{\,\xi : \xi \notin C_\Omega(\alpha,\xi)\,\},$$
where $C_\Omega(\alpha,\xi)$ is the closure of $\xi \cup \{0,\Omega\}$ under $+$, $\lambda\xi.\omega^\xi$ and $\psi_\Omega \restriction \alpha$. Infinitary derivations in $\mathrm{RS}(\Omega)$-style systems are assigned ordinal ranks; cut elimination plus a **collapsing theorem**
$$\vdash^\alpha_{\Omega+n} \Gamma \;\Longrightarrow\; \vdash^{\psi_\Omega(\alpha)}_{\psi_\Omega(\alpha)} \Gamma \quad (\Gamma\ \Sigma\text{-formulas})$$
pushes derivations of $\Sigma_1$ statements below $\Omega$.

## 3. History & State of the Art (SOTA)

- **1936–1938.** Gentzen's consistency proof for PA by transfinite induction to $\varepsilon_0$ creates the subject.
- **1950s–60s.** Schütte and Feferman settle predicativity ($\Gamma_0$); Bachmann's hierarchy (1950) introduces collapsing.
- **1960s–70s.** Takeuti analyses $\Pi^1_1$-CA via ordinal diagrams; Buchholz, Feferman, Pohlers, Sieg (LNM 897, 1981) settle the iterated-inductive-definition systems $\mathrm{ID}_\nu$, giving $|\Pi^1_1\text{-CA}+\text{BI}| = \psi_\Omega(\varepsilon_{\Omega_\omega+1})$.
- **1977–1992.** Pohlers' *local predicativity* and Buchholz's **$\Omega$-rule** give two robust engines. Buchholz's $\Omega_{\mu+1}$-rule (1981) was explicitly designed with $\Pi^1_2$ in view.
- **1990–1994.** Rathjen analyses KPM (recursively Mahlo, $\Delta^1_2$-CA + BI) and then $\Pi_3$-reflection, using ordinal notations built from weakly Mahlo and weakly compact cardinals.
- **2005.** Rathjen publishes the current high-water mark: *An ordinal analysis of stability* and *An ordinal analysis of parameter free $\Pi^1_2$ comprehension* (both Arch. Math. Logic 44). These reach $\Pi^1_2$-CA$^-$ (no set parameters) via notation systems built from an inaccessible-above-a-Mahlo/"$\Pi^1_2$-indescribable"-style large cardinal.
- **2013–2023.** Arai gives streamlined analyses of $\Pi_n$-reflection and first-order reflection (JSL 2020) and revives the Takeuti–Buchholz *distinguished set* machinery for $\Pi^1_2$ (*Wellfoundedness proof with the maximal distinguished set*, Arch. Math. Logic 2023).

**Status:** full $\Pi^1_2$-CA (with parameters) has no published, checked, two-sided ordinal analysis.

## 4. Partial Results / Verified Cases

| System | Ordinal | Source |
|---|---|---|
| $\mathrm{ACA}_0$ | $\varepsilon_0$ | Gentzen 1936 |
| $\mathrm{ATR}_0$ | $\Gamma_0$ | Friedman, Feferman, Schütte |
| $\Pi^1_1\text{-CA}_0$ | $\psi_\Omega(\Omega_\omega)$ | Takeuti; Buchholz–Pohlers |
| $\Pi^1_1\text{-CA}+\text{BI}$ | $\psi_\Omega(\varepsilon_{\Omega_\omega+1})$ | BFPS 1981 |
| $\Delta^1_2\text{-CA}+\text{BI}$ ($=\mathrm{KPM}$) | $\psi(\varepsilon_{M+1})$ | Rathjen 1991 |
| $\mathrm{KP}+\Pi_3\text{-reflection}$ | notation from weakly compact $K$ | Rathjen 1994 |
| $\mathrm{KP}+\Pi_n\text{-reflection}$, all $n<\omega$ | first-order reflection notations | Arai 2020 |
| $\mathrm{KP}+$ "$\exists$ stable ordinal" | Rathjen's stability notations | Rathjen 2005a |
| $\Pi^1_2\text{-CA}^-$ (parameter-free) | Rathjen's notation system | Rathjen 2005b |
| $\Sigma^1_2$-AC, $\Delta^1_2$-CA fragments | reducible to $\mathrm{KPi}$-level systems | Jäger 1986 |

Also settled: all $\Pi^1_1$-CA-based systems, $\mathrm{ID}_\nu$ for $\nu$ up to any provably-notated ordinal, $\mathrm{KPI}$, $\mathrm{KPM}^+$, and the reflection hierarchy $\Pi_n$ for every finite $n$ — i.e. every level *below* stability.

## 5. Principal Obstacles

- **Impredicativity of second order.** Stability $L_\sigma \prec_1 L$ is not expressible by any first-order reflection scheme over $L_\sigma$. Every known collapsing function is calibrated by a *first-order* reflection property of a large cardinal ($\Pi_2$: inaccessible; $\Pi_3$: Mahlo/weakly compact; $\Pi_n$: $\Pi_n$-indescribable). At stability the analogue is $\Pi^1_2$-indescribability and above, so the notation system must import genuinely second-order cardinal combinatorics.
- **Collapsing loses control.** The collapsing theorem needs a $\Sigma$-persistence argument: what is derived above $\Omega$ must remain true below. For stability the "witness" of a $\Sigma_1$ fact may live arbitrarily high in $L$, so the bounding lemma $\psi(\alpha) > $ (all parameters) fails without a new device.
- **Cut elimination at $\Pi^1_2$ level.** Buchholz's $\Omega$-rule handles $\Pi^1_1$-CA by a well-founded infinitary rule with $\Omega$-many premises; the natural iterate for $\Pi^1_2$ requires *distinguished sets* whose existence is itself of $\Pi^1_2$ strength — the analysis risks circularity, and Takeuti's original 1967 attempt foundered here.
- **Lower bounds are as hard as upper bounds.** A well-ordering proof inside $\Pi^1_2$-CA must formalise the "maximal distinguished set" argument; verifying that this is carried out within the system, and not in a stronger metatheory, is the delicate half.
- **No canonicity.** Beyond $\Gamma_0$ there is no accepted criterion for when a notation system is "natural", so even a correct system invites the objection that it merely encodes the theory (the *pseudo-analysis* worry).

## 6. The Gap

Proven: everything at or below **first-order reflection** ($\Pi_n$-reflection, all finite $n$), plus **parameter-free** $\Pi^1_2$-CA and the single-stable-ordinal theory (Rathjen 2005).

Open: **$\Pi^1_2$-CA with free set parameters**, equivalently $\mathrm{KP} + \Sigma_1$-Separation, equivalently "for every set $x$ there is a stable $\sigma$ with $x \in L_\sigma$".

The precise step: extend collapsing from ordinals reflecting first-order properties to ordinals reflecting $\Pi^1_2$ (second-order) properties, i.e. produce $\psi$-functions indexed by a hierarchy of $\Pi^1_2$-indescribable — or "shrewd" (Rathjen 1995) — cardinals, and prove a collapsing theorem for them that survives the presence of arbitrary set parameters. Everything else (embedding, predicative cut elimination, the $\Pi^0_2$ corollaries) is routine once this lemma exists.

## 7. Current Research (as of June 2026)

- **Leeds school (Rathjen and students).** Continued development of shrewd/indescribable-cardinal notation systems, and the programme of relating ordinal analysis to reverse mathematics and constructive set theory.
- **Arai (Chiba).** The most active line: distinguished-set well-ordering proofs. Arai's *Wellfoundedness proof with the maximal distinguished set* (Arch. Math. Logic, 2023) supplies the lower-bound half for $\Pi^1_2$-CA-strength notations; Arai has circulated preprints claiming a full ordinal analysis of $\Pi^1_2$-CA built on iterated $\Sigma_1$-reflection and Mahlo-class notations *(frontier — verify)*.
- **Munich/Buchholz tradition.** Reformulation of the $\Omega$-rule and of operator-controlled derivations to shorten the stability proofs, aiming at a version machine-checkable in principle.
- **Formalisation.** Small but growing effort to verify ordinal notation systems in Isabelle/HOL and Lean (Gentzen-level and Bachmann–Howard-level systems are done; nothing at $\Pi^1_2$ level) *(frontier — verify)*.
- **Ordinal analysis of set theory outright.** Rathjen's stated long-term target is $\mathrm{ZFC}$; $\Pi^1_2$-CA is the acknowledged next checkpoint.

## 8. Future Work

- Isolate the exact large-cardinal combinatorics needed: is $\Pi^1_2$-indescribability the right calibration, or do "shrewd" cardinals give a smoother collapsing hierarchy?
- Detach the notation system from set theory: build $(\mathcal{T},\prec)$ combinatorially (patterns of embeddings, à la Carlson's *elementary patterns of resemblance*), which already reproduces $\Pi^1_1$-CA-level ordinals and is a candidate canonical route to $\Pi^1_2$.
- Verify the Arai and Rathjen constructions independently; the community consensus is that the arguments are too long for confident manual refereeing, motivating partial formalisation.
- Extract concrete corollaries: the provably total recursive functions of $\Pi^1_2$-CA, and independent combinatorial statements (a Paris–Harrington or Kruskal-style theorem at this level) — none is known.
- Push to $\Sigma^1_2$-DC, $\Pi^1_3$-CA, and eventually $\mathrm{ZF}$.

## 9. Key References

- **[Foundational]** W. Buchholz, S. Feferman, W. Pohlers, W. Sieg. *Iterated Inductive Definitions and Subsystems of Analysis: Recent Proof-Theoretical Studies.* Lecture Notes in Mathematics 897, Springer, 1981.
- **[Foundational]** G. Takeuti. *Proof Theory*, 2nd edition. North-Holland, 1987.
- **[Foundational]** J. Barwise. *Admissible Sets and Structures.* Springer, 1975.
- **[Foundational]** G. Jäger. *Theories for Admissible Sets: A Unifying Approach to Proof Theory.* Bibliopolis, 1986.
- **[SOTA]** M. Rathjen. *An ordinal analysis of stability.* Archive for Mathematical Logic 44(1), 1–62, 2005.
- **[SOTA]** M. Rathjen. *An ordinal analysis of parameter free $\Pi^1_2$-comprehension.* Archive for Mathematical Logic 44(3), 263–362, 2005.
- **[SOTA]** M. Rathjen. *Proof theory of reflection.* Annals of Pure and Applied Logic 68(2), 181–224, 1994.
- **[SOTA]** M. Rathjen. *Proof-theoretic analysis of KPM.* Archive for Mathematical Logic 30, 377–403, 1991.
- **[SOTA / Recent]** T. Arai. *A simplified ordinal analysis of first-order reflection.* Journal of Symbolic Logic 85(3), 1163–1185, 2020.
- **[SOTA / Recent]** T. Arai. *Wellfoundedness proof with the maximal distinguished set.* Archive for Mathematical Logic, 2023.
- **[Survey]** M. Rathjen. *The realm of ordinal analysis.* In S. B. Cooper, J. K. Truss (eds.), *Sets and Proofs*, LMS Lecture Note Series 258, Cambridge University Press, 219–279, 1999.
- **[Survey]** W. Pohlers. *Proof Theory: The First Step into Impredicativity.* Springer, 2009.
- **[Survey]** S. G. Simpson. *Subsystems of Second Order Arithmetic*, 2nd edition. Cambridge University Press, 2009.
- **[Technical]** W. Buchholz. *A simplified version of local predicativity.* In P. Aczel, H. Simmons, S. Wainer (eds.), *Proof Theory*, Cambridge University Press, 115–147, 1992.
- **[Technical]** T. J. Carlson. *Elementary patterns of resemblance.* Annals of Pure and Applied Logic 108, 19–77, 2001.

## 10. Worked Example / Concrete Special Case

**The base case of collapsing: $|\mathrm{KP}| = \psi_\Omega(\varepsilon_{\Omega+1})$.** This shows in miniature exactly what fails at stability.

Let $\Omega = \omega_1$ (or $\omega_1^{\mathrm{CK}}$). Define $C(\alpha,\beta)$ as the least set $X \supseteq \beta \cup \{0,\Omega\}$ closed under $(\xi,\eta) \mapsto \xi+\eta$, $\xi \mapsto \omega^\xi$, and $\xi \mapsto \psi(\xi)$ for $\xi \in X \cap \alpha$; and
$$\psi(\alpha) = \min\{\beta : \beta \notin C(\alpha,\beta)\}.$$

Sample computations:
$$\psi(0) = \varepsilon_0,\qquad \psi(1) = \varepsilon_1,\qquad \psi(\Omega) = \varepsilon_\Omega\ \text{(i.e. } \sup_n \psi(\text{iterates})),$$
$$\psi(\varepsilon_{\Omega+1}) = \sup\{\psi(0),\psi(\psi(0)),\psi(\Omega^{\Omega}),\ldots\} = \text{Bachmann–Howard ordinal}.$$
Each value is countable because $C(\alpha,\beta)$ has cardinality $<\Omega$ and $\Omega$ is regular — **regularity of $\Omega$ is the whole engine**.

Now the proof-theoretic use. In the infinitary system $\mathrm{RS}(\Omega)$ for KP, a KP-proof of a $\Sigma$-sentence $A$ embeds as $\vdash^{\alpha}_{\Omega+n} A$ with $\alpha < \varepsilon_{\Omega+1}$. Predicative cut elimination lowers cut rank to $\Omega$, then the collapsing theorem gives
$$\vdash^{\alpha}_{\Omega} A \;\Longrightarrow\; \vdash^{\psi(\alpha)}_{\psi(\alpha)} A .$$
Its proof works because a $\Sigma$-formula true in $L_\Omega$ has a witness *bounded below* $\Omega$: if $\exists x\,\theta(x)$ holds in the derivation, the witness sits in $L_{\gamma}$ for some $\gamma \in C(\alpha,\psi(\alpha))$. Hence $\mathrm{KP} \vdash \mathrm{WO}(\prec)$ implies $\mathrm{otyp}(\prec) < \psi(\varepsilon_{\Omega+1})$.

**Where the analogue breaks.** Replace $\Omega$ by a stable $\sigma$ (the $\Pi^1_2$-CA setting). Take the $\Sigma_1$ sentence
$$\exists x\,\theta(x) \quad \text{with the least witness } x \in L_{\tau},\ \tau > \sigma .$$
Stability $L_\sigma \prec_1 L$ guarantees a witness *exists* inside $L_\sigma$, but supplies **no ordinal bound** on it expressible from the notation-system parameters: the bound would have to be read off a second-order property of $L_\sigma$. The step "witness $\in C(\alpha, \psi(\alpha))$", trivial at $\Omega$, is precisely the unproved lemma. Rathjen (2005) recovers it for a *single* stable ordinal and for parameter-free comprehension; with set parameters ranging over $L$, the witness-bounding argument has no known replacement. That one lemma is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*