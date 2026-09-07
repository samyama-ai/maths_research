---
id: 08-logic-set-theory/club-guessing-principle-consistency
title: "Club Guessing Principle Consistency"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Club Guessing Principle Consistency

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/club-guessing-principle-consistency` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Shelah proved in ZFC that club guessing sequences exist at most points of the cardinal hierarchy. The open problem is exactly where that ZFC proof stops.

**Central question.** Is it consistent (relative to some large cardinal hypothesis) that there is **no** club guessing sequence on $S^{\omega_2}_{\omega_1}=\{\delta<\omega_2:\operatorname{cf}(\delta)=\omega_1\}$? Equivalently: for every sequence $\bar C=\langle C_\delta:\delta\in S^{\omega_2}_{\omega_1}\rangle$ with each $C_\delta\subseteq\delta$ club in $\delta$, is there a club $E\subseteq\omega_2$ such that $C_\delta\not\subseteq E$ for **every** $\delta$?

More generally, for $\kappa$ regular uncountable, does ZFC decide club guessing on $S^{\kappa^+}_{\kappa}$? A complete solution is either (a) a ZFC proof of full club guessing on $S^{\kappa^+}_\kappa$ (extending Shelah's stationary-guessing theorem), or (b) a forcing construction, presumably from large cardinals, producing a model where every $\bar C$ on $S^{\omega_2}_{\omega_1}$ is killed by a single club.

Contrast: at $\lambda=\omega_1$ the answer is settled — club guessing on $S^{\omega_1}_{\omega}$ is consistently false. At every $\lambda>\kappa^+$ it is a theorem of ZFC. The diagonal case $\lambda=\kappa^+$, $\kappa$ regular uncountable, is the surviving gap.

## 2. Mathematical Foundations

Let $\lambda$ be a regular uncountable cardinal, $\kappa<\lambda$ regular, and
$$S^{\lambda}_{\kappa}=\{\delta<\lambda:\operatorname{cf}(\delta)=\kappa\}.$$
A set $E\subseteq\lambda$ is *club* if closed and unbounded; $\operatorname{acc}(E)=\{\delta\in E:\sup(E\cap\delta)=\delta\}$. $\mathrm{NS}_\lambda$ denotes the nonstationary ideal.

**$S$-club system.** For stationary $S\subseteq\lambda$ consisting of limit ordinals, $\bar C=\langle C_\delta:\delta\in S\rangle$ with $C_\delta\subseteq\delta$ club in $\delta$. If $\operatorname{otp}(C_\delta)=\kappa$ for all $\delta$ we call $\bar C$ *$\kappa$-uniform*.

**Guessing modes.** For $\bar C$ on $S$ and $E\subseteq\lambda$ club:

$$\textbf{(CG) full: }\quad \{\delta\in S: C_\delta\subseteq E\}\ \text{is stationary};$$
$$\textbf{(TCG) tail: }\quad \{\delta\in S: \exists\alpha<\delta,\ C_\delta\setminus\alpha\subseteq E\}\ \text{is stationary};$$
$$\textbf{(SCG) stationary: }\quad \{\delta\in S: C_\delta\cap E\ \text{is stationary in }\delta\}\ \text{is stationary};$$
$$\textbf{(WCG) weak: }\quad \{\delta\in S: \sup(C_\delta\cap E)=\delta\}\ \text{is stationary}.$$

$\mathrm{CG}\Rightarrow\mathrm{TCG}\Rightarrow\mathrm{WCG}$, and $\mathrm{SCG}$ is meaningful only for $\operatorname{cf}(\delta)>\omega$. $\bar C$ *guesses clubs* (mode $X$) if $X$ holds for every club $E$.

**Club guessing ideal.** $\operatorname{id}(\bar C)=\{A\subseteq\lambda:\exists E\ \text{club},\ \forall\delta\in A\cap S\ (C_\delta\not\subseteq E)\}$, a $\lambda$-complete ideal extending $\mathrm{NS}_\lambda\restriction S$; $\bar C$ guesses clubs iff $S\notin\operatorname{id}(\bar C)$.

**Theorem (Shelah, *Cardinal Arithmetic* III.2.14).** If $\kappa^{+}<\lambda$ are regular and $S\subseteq S^{\lambda}_{\kappa}$ is stationary, then there is a $\kappa$-uniform $S$-club system satisfying **(CG)**. No extra axioms.

**Theorem (Shelah, same chapter).** If $\kappa$ is regular uncountable and $S\subseteq S^{\kappa^{+}}_{\kappa}$ is stationary, there is an $S$-club system satisfying **(SCG)**: for every club $E$, stationarily many $\delta\in S$ have $C_\delta\cap E$ stationary in $\delta$.

The **(SCG)** result is strictly weaker than **(CG)** and is what the ZFC machinery delivers at $\lambda=\kappa^{+}$. Whether **(CG)** or even **(TCG)** is provable there is the problem.

Standard reduction used throughout: for a club $E$ and $\delta\in\operatorname{acc}(E)$ put
$$C^{E}_{\delta}=\{\sup(E\cap\alpha):\alpha\in C_\delta,\ \sup(E\cap\alpha)>\min(E)\},$$
the *$E$-drop* of $C_\delta$. Then $C^{E}_{\delta}\subseteq E$ is club in $\delta$ and $\operatorname{otp}(C^{E}_{\delta})\le\operatorname{otp}(C_\delta)$. All ZFC proofs iterate this operation and argue that the order types cannot strictly drop too often.

## 3. History & State of the Art (SOTA)

- **1970s–80s.** Guessing principles enter through $\diamondsuit$ (Jensen, 1972) and ladder systems on $\omega_1$. $\diamondsuit$ trivially yields **(CG)** on $S^{\omega_1}_\omega$, so the question is what survives without $V=L$-style hypotheses.
- **1994.** Shelah isolates club guessing in *Cardinal Arithmetic* (Oxford Logic Guides 29) as a ZFC substitute for $\diamondsuit$: the theorems above, plus applications to pcf theory, non-saturation of ideals, and the existence of Jónsson algebras.
- **Non-saturation.** Shelah's club guessing at $S^{\kappa^+}_\kappa$ ($\kappa$ regular uncountable) yields that $\mathrm{NS}_{\kappa^{+}}\restriction S^{\kappa^{+}}_{\kappa}$ is **not** $\kappa^{++}$-saturated — in sharp contrast with $\mathrm{NS}_{\omega_1}$, whose saturation is consistent from a Woodin cardinal (Shelah; see Foreman's Handbook chapter). This is the main structural payoff and the reason failure of guessing at $\omega_2$ would be so strong.
- **1995.** Džamonja–Shelah, *On squares, outside guessing of clubs and $I_{<f}[\lambda]$* (Fund. Math. 148), extends guessing to "outside guessing" and singular contexts.
- **2000.** Shelah lists the status of club guessing at successors of regulars among his open problems (*On what I do not understand (and have something to say)*, Fund. Math. 166).
- **2005.** Ishiu, *Club guessing sequences and filters* (J. Symbolic Logic 70), analyses $\operatorname{id}(\bar C)$ and the extent to which club guessing ideals can be nice/saturated.
- **2010–11.** Eisworth's Handbook chapter gives the modern exposition; Rinot, *On guessing generalized clubs at the successors of regulars* (APAL 162, 2011), proves strengthened guessing at $S^{\kappa^+}_\kappa$ from square-like and non-reflection hypotheses.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $\kappa$ regular, $\lambda$ regular, $\kappa^{+}<\lambda$, any stationary $S\subseteq S^\lambda_\kappa$ | **(CG)** with $\operatorname{otp}(C_\delta)=\kappa$ — ZFC theorem (Shelah 1994) |
| $\lambda=\omega_2$, $S=S^{\omega_2}_{\omega}$ | **(CG)** in ZFC (special case $\kappa=\omega$, $\kappa^+=\omega_1<\omega_2$) |
| $\lambda=\kappa^{+}$, $\kappa$ singular, $S\subseteq S^{\kappa^{+}}_{\theta}$, $\theta<\kappa$ regular | **(CG)** in ZFC, since $\theta^{+}<\kappa^{+}$ |
| $\lambda=\kappa^{+}$, $\kappa$ regular uncountable, $S\subseteq S^{\kappa^{+}}_{\kappa}$ | **(SCG)** in ZFC; **(CG)/(TCG)** open |
| $\lambda=\kappa^{+}$, $\kappa$ regular uncountable, under $\square_\kappa$ or $\diamondsuit_{\kappa^+}$ | **(CG)** and stronger "generalized club" guessing hold (Rinot 2011) |
| $\lambda=\omega_1$, $S=S^{\omega_1}_{\omega}$ | **(CG)** holds under $\diamondsuit$; its failure — and even failure of **(WCG)** — is consistent with ZFC (Shelah, *Proper and Improper Forcing*), by a proper, no-new-reals iteration adding clubs that evade each ladder system |
| $\lambda$ inaccessible or Mahlo, $S\subseteq S^{\lambda}_{\kappa}$, $\kappa^{+}<\lambda$ | **(CG)** in ZFC |

So the only unresolved parameter region is $(\lambda,\kappa)=(\kappa^{+},\kappa)$ with $\kappa\ge\omega_1$ regular — the least instance being $(\omega_2,\omega_1)$.

## 5. Principal Obstacles

- **The order-type pigeonhole runs out.** All ZFC proofs iterate the drop $\bar C\mapsto\bar C^{E}$ along a decreasing chain of clubs $\langle E_i : i<\kappa^{+}\rangle$ and derive a contradiction from a strictly decreasing sequence of ordinals $\operatorname{otp}(C^{E_i}_\delta)<\kappa$. When $\lambda>\kappa^{+}$ the chain has length $\kappa^{+}<\lambda$, so intersections stay club. When $\lambda=\kappa^{+}$ one may only intersect $<\kappa^{+}$ clubs, i.e. $\kappa$ many, and $\kappa$ steps do not exhaust the possible order types below $\kappa$. The counting argument is off by exactly one cardinal.
- **Stationary guessing does not upgrade.** The **(SCG)** witness gives $C_\delta\cap E$ stationary in $\delta$; passing to $C_\delta\subseteq E$ requires thinning $C_\delta$ to a club subset of a stationary set, which is impossible in general — nonreflecting stationary subsets of $\kappa$ obstruct it.
- **Forcing side.** To refute guessing one must kill $2^{\kappa^{+}}$ many club systems simultaneously. At $\omega_1$ this is done by countable-support iteration of proper forcings that add no reals; at $\omega_2$ the analogue would need an $\omega_2$-preserving iteration adding clubs of $\omega_2$ through the complement of every $C_\delta$-trace, and known $\kappa$-proper / $<\kappa$-support technology collapses cardinals or destroys stationarity of $S^{\omega_2}_{\omega_1}$.
- **Strength barrier.** Failure of guessing at $S^{\omega_2}_{\omega_1}$ would make $\mathrm{NS}_{\omega_2}\restriction S^{\omega_2}_{\omega_1}$ a candidate for saturation, and Shelah's non-saturation theorem for successors of regular uncountables is proved *from* club guessing — so any consistency proof must simultaneously evade an argument that is otherwise a ZFC theorem, which strongly suggests large cardinals well beyond a Woodin.

## 6. The Gap

Proven (§4): **(SCG)** at $S^{\kappa^{+}}_{\kappa}$ in ZFC, and **(CG)** everywhere else in the regular hierarchy.
Wanted (§1): a decision on **(CG)**/**(TCG)** at $S^{\kappa^{+}}_{\kappa}$, $\kappa\ge\omega_1$.

Precisely, the missing step is either:

1. a ZFC argument replacing the length-$\kappa^{+}$ decreasing club chain by a length-$\kappa^{+}$ *fixpoint* argument at $\lambda=\kappa^{+}$ — where clubs are not $\kappa^{+}$-closed under intersection; or
2. an iteration theorem for forcings of length $\ge(2^{\omega_1})^{+}$ that preserve $\omega_1$, $\omega_2$ and the stationarity of $S^{\omega_2}_{\omega_1}$, while generically adding, for each ground-model club system, a club evading it.

Neither exists. The dividing line is exactly the identity $\lambda=\kappa^{+}$, i.e. whether $\kappa$ steps of a drop-iteration suffice.

## 7. Current Research (as of June 2026)

- **Rinot's Bar-Ilan group** continues the systematic map of guessing principles at successors of regulars, relating them to $\square$-sequences, $C$-sequence spectra and partition relations. Recent work stresses *partition* strengthenings ("club guessing with colouring"), where extra guessing power is extracted from a $\mathrm{ZFC}$ witness. *(frontier — verify)*
- **Ideal-theoretic school (Foreman, Magidor, Ishiu, Sakai).** Programme: pin down which $\kappa^{+}$-complete ideals can be saturated, using club guessing as the obstruction; failure of guessing at $\omega_2$ would be a by-product of a saturated $\mathrm{NS}_{\omega_2}\restriction S^{\omega_2}_{\omega_1}$.
- **Higher forcing axioms.** Attempts to force analogues of $\mathrm{MM}$ at $\omega_2$ (two-cardinal properness, $\sigma$-Prikry style iterations) are the main technology candidates for the negative consistency. No published construction preserves the required stationary sets. *(frontier — verify)*
- **Singular-cardinal side.** Eisworth-style applications of club guessing at $S^{\mu^{+}}_{\operatorname{cf}\mu}$ for singular $\mu$ continue to be productive and are unaffected by the gap.

## 8. Future Work

- Determine the consistency strength of $\neg\mathrm{TCG}$ at $S^{\omega_2}_{\omega_1}$; even a lower bound (e.g. "implies an inner model with a Woodin cardinal") would be new.
- Decide whether **(SCG)** can be improved in ZFC to "$C_\delta\cap E$ contains a club of $\delta$ for stationarily many $\delta$" on a *fixed* stationary $S$.
- Isolate a preservation theorem for $\omega_2$-length iterations that preserves stationarity of $S^{\omega_2}_{\omega_1}$ — the missing forcing tool.
- Clarify the relation between failure of club guessing and saturation of $\mathrm{NS}_{\omega_2}\restriction S^{\omega_2}_{\omega_1}$: are they equivalent, or is guessing strictly stronger?
- Map the parallel question at inaccessible $\lambda$ with $S^{\lambda}_{\lambda}$-type diagonal sets, where the drop argument degenerates similarly.

## 9. Key References

- **[Foundational]** Saharon Shelah. *Cardinal Arithmetic.* Oxford Logic Guides 29, Oxford University Press, 1994. (Chapter III: club guessing theorems and ideals.)
- **[Foundational]** Saharon Shelah. *Proper and Improper Forcing*, 2nd edition. Perspectives in Mathematical Logic, Springer, 1998. (Iterations without new reals; consistency of failure of guessing at $\omega_1$.)
- **[SOTA / Recent]** Assaf Rinot. *On guessing generalized clubs at the successors of regulars.* Annals of Pure and Applied Logic, 162(7):566–577, 2011.
- **[SOTA / Recent]** Tetsuya Ishiu. *Club guessing sequences and filters.* The Journal of Symbolic Logic, 70(4):1037–1071, 2005.
- **[SOTA / Recent]** Mirna Džamonja and Saharon Shelah. *On squares, outside guessing of clubs and $I_{<f}[\lambda]$.* Fundamenta Mathematicae, 148(2):165–198, 1995.
- **[Survey]** Todd Eisworth. *Successors of singular cardinals.* In M. Foreman and A. Kanamori (eds.), *Handbook of Set Theory*, Springer, 2010, pp. 1229–1350.
- **[Survey]** Matthew Foreman. *Ideals and generic elementary embeddings.* In *Handbook of Set Theory*, Springer, 2010, pp. 885–1147.
- **[Survey]** Saharon Shelah. *On what I do not understand (and have something to say), model theory.* Fundamenta Mathematicae, 166(1–2):1–82, 2000.
- **[Background]** Thomas Jech. *Set Theory*, 3rd millennium edition. Springer Monographs in Mathematics, 2003.

## 10. Worked Example / Concrete Special Case

**Claim (the ZFC case that works).** Let $S=S^{\omega_2}_{\omega}$. There is $\bar C=\langle C_\delta:\delta\in S\rangle$, $\operatorname{otp}(C_\delta)=\omega$, guessing clubs in mode **(CG)**.

*Proof sketch, showing exactly where $\lambda>\kappa^{+}$ is used.* Fix any ladder system $\bar C^{0}$: $C^{0}_\delta\subseteq\delta$ cofinal, $\operatorname{otp}=\omega$. Suppose no drop of $\bar C^{0}$ guesses. Build a decreasing sequence of clubs $\langle E_i:i<\omega_1\rangle$ of $\omega_2$:

- $E_0=\omega_2$.
- Given $E_i$, form $\bar C^{i}=\langle C^{E_i}_{\delta}:\delta\in S\cap\operatorname{acc}(E_i)\rangle$ using the drop of §2. Since by assumption $\bar C^{i}$ does not guess, pick a club $E_{i+1}\subseteq E_i$ with $C^{E_i}_{\delta}\not\subseteq E_{i+1}$ for all relevant $\delta$.
- At limits $i<\omega_1$, set $E_i=\bigcap_{j<i}E_j$. **This is club because $|i|\le\aleph_1<\operatorname{cf}(\omega_2)=\aleph_2$** — the one place regularity of $\lambda$ above $\kappa^{+}=\omega_1$ is used.

Let $E=\bigcap_{i<\omega_1}E_i$, still club, and pick $\delta\in S\cap\operatorname{acc}(E)$ (possible: $S$ is stationary). For each $i$, $C^{E_{i+1}}_{\delta}$ is obtained from $C^{E_i}_{\delta}$ by dropping every point down to $E_{i+1}$, and since $C^{E_i}_{\delta}\not\subseteq E_{i+1}$ at least one point strictly moves. Reading order types, $n_i:=\operatorname{otp}\big(C^{E_i}_{\delta}\setminus \min(C^{E_{i+1}}_\delta\ \text{stabilised part})\big)$ gives a sequence of natural numbers that must strictly decrease at cofinally many $i<\omega_1$, because each drop identifies at least two former points of the ladder into one. A strictly decreasing $\omega_1$-sequence of natural numbers is impossible. Contradiction; hence some $\bar C^{i}$ guesses. $\square$

**Where it breaks at $(\omega_2,\omega_1)$.** Repeat with $S=S^{\omega_2}_{\omega_1}$ and $\operatorname{otp}(C_\delta)=\omega_1$. The recursion now needs length $\omega_2$ to exhaust the possible order types $<\omega_1$ of the residue — but $\bigcap_{i<\omega_2}E_i$ need not be club, since $\omega_2$ is not $\omega_2^{+}$-closed under intersections. Truncating at length $\omega_1$ leaves a residue $C^{E_{\omega_1}}_{\delta}$ that is merely *stationary* in $\delta$, not a club subset of $E$. That is precisely the **(SCG)** theorem, and precisely the gap of §6: a concrete $\delta$ of cofinality $\omega_1$ can have $C_\delta\cap E$ stationary in $\delta$ while $C_\delta\setminus E$ is also stationary in $\delta$, so no tail of $C_\delta$ ever lands inside $E$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*