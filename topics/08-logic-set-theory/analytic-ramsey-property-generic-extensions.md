---
id: 08-logic-set-theory/analytic-ramsey-property-generic-extensions
title: "The Ramsey Property for Analytic Sets in Generic Extensions"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Ramsey Property for Analytic Sets in Generic Extensions

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/analytic-ramsey-property-generic-extensions` · **Status:** open

## 1. Problem Statement / Conjecture

Silver's theorem (1970) settles the absolute version: in ZFC, every analytic subset of $[\omega]^{\omega}$ is Ramsey. The open problem is the **local (relativized) version and its behaviour under forcing**. Fix a coideal $\mathcal{H}\subseteq[\omega]^{\omega}$. A set $\mathcal{A}\subseteq[\omega]^{\omega}$ is *$\mathcal{H}$-Ramsey* if every $A\in\mathcal{H}$ has a subset $B\in\mathcal{H}$ with $[B]^{\omega}\subseteq\mathcal{A}$ or $[B]^{\omega}\cap\mathcal{A}=\varnothing$. Three linked questions:

- **(P1) Preservation.** Let $\mathcal{U}\in V$ be a selective ultrafilter and $\mathbb{P}$ a forcing notion. In $V[G]$, $\mathcal{U}$ generates a filter whose dual coideal is $\mathcal{H}_{\mathcal{U}}=\{X:\forall U\in\mathcal{U}\;|X\cap U|=\omega\}$. **For which $\mathbb{P}$ is $\mathcal{H}_{\mathcal{U}}$ semiselective in $V[G]$ — equivalently, for which $\mathbb{P}$ does "every analytic set is $\mathcal{H}_{\mathcal{U}}$-Ramsey" hold in $V[G]$?** No characterization is known beyond isolated cases.
- **(P2) Consistency strength.** Mathias proved from a **Mahlo** cardinal that in the Solovay model every set of reals is $\mathcal{H}$-Ramsey for every happy family $\mathcal{H}$, while the plain Ramsey property for all sets is equiconsistent with an **inaccessible**. **Is the Mahlo cardinal necessary for the local statement?** Open since *Happy families* (1977).
- **(P3) Solovay-type characterization.** Give a forcing-theoretic characterization, in the style of Judah–Shelah and Brendle–Löwe, of "every $\boldsymbol{\Sigma}^1_2$ set is $\mathcal{H}$-Ramsey for every semiselective coideal $\mathcal{H}$", i.e. locate it exactly in the hierarchy of transcendence-over-$L[r]$ statements.

A complete solution to (P2) means either a proof of Mathias's conclusion from an inaccessible alone, or an inner-model argument extracting a Mahlo cardinal from the local Ramsey property.

## 2. Mathematical Foundations

Work in the Ellentuck space $[\omega]^{\omega}$ with the basic sets
$$[a,A]=\{X\in[\omega]^{\omega}: a\sqsubseteq X\subseteq a\cup A\},\qquad a\in[\omega]^{<\omega},\ A\in[\omega]^{\omega},\ \max(a)<\min(A).$$
These generate the **Ellentuck topology**, refining the metric topology.

**Ellentuck's theorem (1974).** $\mathcal{A}$ is Ramsey iff $\mathcal{A}$ has the Baire property in the Ellentuck topology; $\mathcal{A}$ is Ramsey-null iff it is Ellentuck-meagre.

**Coideals.** $\mathcal{H}\subseteq[\omega]^{\omega}$ is a *coideal* if it is upward closed mod finite and $A\cup B\in\mathcal{H}\Rightarrow A\in\mathcal{H}$ or $B\in\mathcal{H}$. $\mathcal{H}$ is **selective** (Mathias: a *happy family*) if for every decreasing sequence $A_0\supseteq A_1\supseteq\cdots$ in $\mathcal{H}$ there is a diagonalization $A\in\mathcal{H}$, $A=\{a_0<a_1<\cdots\}$, with $a_{n+1}\in A_n$ for all $n$. $\mathcal{H}$ is **semiselective** (Farah) if the same diagonalization is required only for sequences indexed by a dense-open-in-$\mathcal{H}$ family, i.e. every $\mathcal{H}$-*decreasing* sequence has a *diagonalization mod* the ideal $\mathcal{H}^{\ast}$. Selective $\Rightarrow$ semiselective; an ultrafilter is selective iff it is Ramsey iff every $f:\omega\to\omega$ is one-to-one or constant on a member.

**Local Ellentuck topology.** For $\mathcal{H}$ a coideal, restrict to $[a,A]$ with $A\in\mathcal{H}$. Write $\mathcal{A}\in \mathrm{Ram}(\mathcal{H})$ for "$\mathcal{A}$ is $\mathcal{H}$-Ramsey".

**Mathias forcing $\mathbb{M}_{\mathcal{H}}$**: conditions $(a,A)$ with $A\in\mathcal{H}$, ordered by $(b,B)\le(a,A)$ iff $a\sqsubseteq b$, $B\subseteq A$, $b\setminus a\subseteq A$. Key equivalence (Farah 1998): $\mathcal{H}$ is semiselective $\iff$ $\mathbb{M}_{\mathcal{H}}$ has the **pure decision / Prikry property**
$$\forall (a,A)\ \forall \varphi\ \exists B\subseteq A,\ B\in\mathcal{H}:\ (a,B)\Vdash\varphi \ \text{ or }\ (a,B)\Vdash\neg\varphi ,$$
$\iff$ every analytic set is $\mathcal{H}$-Ramsey.

**Definability classes.** $\boldsymbol{\Sigma}^1_1$ (analytic) $=$ continuous images of Polish spaces; $\boldsymbol{\Sigma}^1_2$ $=$ projections of co-analytic sets. Shoenfield absoluteness fixes $\boldsymbol{\Sigma}^1_2$ truth between $V$ and $V[G]$, but $\mathcal{H}$-Ramseyness quantifies over the *third-order* object $\mathcal{H}$ and is therefore **not** covered by Shoenfield — this is the source of the whole problem.

## 3. History & State of the Art (SOTA)

- **1930/1968.** Ramsey's theorem; Nash-Williams and Galvin's partition results for $[\omega]^{\omega}$.
- **1970.** Silver: every analytic set is Ramsey (elaborating Galvin–Prikry's Borel case, 1973 in print).
- **1974.** Ellentuck: topological characterization, giving a proof of Silver's theorem with no metamathematics.
- **1977.** Mathias, *Happy families*: local Ramsey theory; analytic sets are $\mathcal{H}$-Ramsey for happy families; from a Mahlo cardinal, **all** sets in the Solovay model are $\mathcal{H}$-Ramsey; Mathias forcing and the Mathias real characterization.
- **1979.** Baumgartner–Laver: selective ultrafilters generate selective ultrafilters after countable-support iterations of Sacks forcing — the first genuine preservation theorem for (P1).
- **1989.** Judah–Shelah: every $\boldsymbol{\Sigma}^1_2$ set is Ramsey $\iff$ for every real $r$ there is a Mathias real over $L[r]$.
- **1998.** Farah, *Semiselective coideals*: analytic sets are $\mathcal{H}$-Ramsey for every **semiselective** coideal, **in ZFC** — removing Mathias's Mahlo cardinal at the analytic level.
- **1998.** Di Prisco–Todorcevic: in $L(\mathbb{R})[\mathcal{U}]$, obtained by forcing with $\mathcal{P}(\omega)/\mathrm{fin}$ over a model of AD, every set of reals is $\mathcal{U}$-Ramsey for the generic selective ultrafilter $\mathcal{U}$.
- **2010.** Todorcevic, *Introduction to Ramsey Spaces*: abstract framework (topological Ramsey spaces, $\mathcal{R}_\alpha$, $\mathcal{H}$-versions), where the local theory becomes a general axiom scheme **A.1–A.4**.

SOTA: the analytic level is ZFC-settled for semiselective coideals; the *projective* and *all-sets* local levels and every preservation question remain open.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $\mathcal{H}=[\omega]^{\omega}$, analytic sets | **Proven in ZFC** (Silver 1970) |
| $\mathcal{H}$ semiselective, $\boldsymbol{\Sigma}^1_1$ sets | **Proven in ZFC** (Farah 1998; Todorcevic 2010) |
| $\mathcal{H}$ selective ultrafilter, $\boldsymbol{\Sigma}^1_1$ | Proven in ZFC (Mathias 1977 with Mahlo; Todorcevic, ZFC) |
| All sets, Solovay model, all happy families | Proven from a **Mahlo** cardinal (Mathias 1977) |
| All sets, plain Ramsey, Solovay model | Equiconsistent with an **inaccessible** (Mathias 1977) |
| $\boldsymbol{\Sigma}^1_2$ plain Ramsey | Characterized: Mathias reals over $L[r]$ (Judah–Shelah 1989) |
| $\boldsymbol{\Sigma}^1_n$, all $n$ | Follows from $\mathrm{AD}^{L(\mathbb{R})}$ / infinitely many Woodins (via Ellentuck + Baire property in $L(\mathbb{R})$) |
| Preservation by countable-support Sacks/Miller iterations | Selective ultrafilters preserved (Baumgartner–Laver 1979; Miller for $P$-points) |
| $\sigma$-centred / Mathias $\mathbb{M}_{\mathcal{U}}$ | $\mathcal{U}$ generates a selective ultrafilter in the extension (Mathias 1977) |
| Cohen, random, Hechler | Ground-model $\mathcal{U}$ **fails** to generate an ultrafilter (the added real splits all ground-model sets); semiselectivity of the generated coideal open |
| $L(\mathbb{R})[\mathcal{U}]$ over AD | All sets $\mathcal{U}$-Ramsey (Di Prisco–Todorcevic 1998) |

## 5. Principal Obstacles

- **No absoluteness handle.** $\mathcal{H}$-Ramseyness is $\Pi^1_2(\mathcal{H})$ in a *set of reals* parameter. Shoenfield and even $\boldsymbol{\Sigma}^1_3$-absoluteness under large cardinals say nothing, because $\mathcal{H}$ itself changes meaning in $V[G]$: the ground-model coideal need not stay a coideal, let alone semiselective.
- **Fusion fails for coideals.** The Galvin–Prikry/Ellentuck proofs run a fusion over $\omega$ producing a diagonal $B$; when the fusion is required to land in $\mathcal{H}$, one needs exactly the semiselectivity diagonalization. After forcing, the new $\omega$-sequences of ground-model sets are the ones that break it — a diagonalization must be found for sequences that did not exist in $V$.
- **Failure at the second projective level.** For $\boldsymbol{\Sigma}^1_2$ the Ramsey property is not a ZFC theorem: in $L$ there is a $\boldsymbol{\Delta}^1_2$ non-Ramsey set. So any local generalization must be a *large-cardinal-plus-forcing* statement, not a combinatorial one; combinatorial fusion arguments cannot reach it.
- **Mahlo vs inaccessible.** Mathias's use of a Mahlo is via a tree/stationary reflection argument selecting happy families uniformly in the Lévy collapse. No inner-model machinery is known that turns a failure of local Ramseyness in the Solovay model into a Mahlo in $L$; the standard $\omega_1$-inaccessible-in-$L$ extraction (Solovay) yields only inaccessibility.
- **No preservation calculus.** Unlike Lebesgue measurability or the Baire property, where the Bartoszyński–Judah cardinal-invariant chart classifies preservation, $\mathcal{H}$-Ramseyness has no invariant characterization; $\mathrm{cov}(\mathcal{M})$, $\mathfrak{h}$, $\mathfrak{s}$ each capture only fragments.

## 6. The Gap

Proven: analytic $+$ semiselective $\Rightarrow$ $\mathcal{H}$-Ramsey, in ZFC, in every model. The gap has two coordinates.

1. **Semiselectivity is not known to be forcing-robust.** Farah's theorem applies in $V[G]$ *only if* the coideal in $V[G]$ is semiselective there. The exact missing step: a characterization of the forcings $\mathbb{P}$ such that $\Vdash_{\mathbb{P}}$ "$\mathcal{H}_{\mathcal{U}}$ is semiselective" — equivalently, such that $\mathbb{M}_{\mathcal{H}_{\mathcal{U}}}$ retains pure decision in $V[G]$.
2. **Mahlo $\to$ inaccessible.** Between "every set is Ramsey in the Solovay model" (inaccessible) and "every set is $\mathcal{H}$-Ramsey for all happy families" (Mahlo) lies an unmeasured consistency-strength interval. Nothing is known to be strictly between; no forcing separates the two, and no reflection argument merges them.

## 7. Current Research (as of June 2026)

- **Abstract local Ramsey theory.** Di Prisco, Mijares, and collaborators (IVIC/Caracas, Universidad de los Andes, Barcelona) develop $\mathcal{H}$-versions of Todorcevic's topological Ramsey spaces, transferring semiselectivity to $\mathcal{R}$-coideals; the preservation question is being reformulated space-by-space *(frontier — verify)*.
- **Toronto/Paris school (Todorcevic and students).** Forcing axioms and $\mathfrak{p}=\mathfrak{c}$-style hypotheses used to build semiselective coideals surviving specified iterations.
- **Amsterdam/Vienna definability school** (Khomskii, Schrittesser, Törnquist): "Solovay-type" characterizations of regularity properties for arbitrary arboreal forcings; extending the Judah–Shelah Mathias-real criterion to relativized Mathias forcing $\mathbb{M}_{\mathcal{H}}$ is the natural target for (P3) *(frontier — verify)*.
- **Descriptive-set-theoretic ultrafilter theory.** Schrittesser–Törnquist's work on maximal almost disjoint families and Ramsey-type regularity in $L(\mathbb{R})$ suggests the Di Prisco–Todorcevic $L(\mathbb{R})[\mathcal{U}]$ result may generalize from selective ultrafilters to semiselective coideals *(frontier — verify)*.

## 8. Future Work

- Prove or refute: if $\mathcal{U}$ is selective in $V$ and $\mathbb{P}$ is proper and $\omega^\omega$-bounding, then $\mathcal{H}_{\mathcal{U}}$ is semiselective in $V[G]$.
- Extract a Mahlo cardinal (or an inner model with one) from "in the Solovay model, all sets are $\mathcal{H}$-Ramsey for all happy families" — the decisive step for (P2).
- Develop a preservation invariant for semiselectivity playing the role that "preservation of Cohen/random reals" plays for the Baire property in the Bartoszyński–Judah chart.
- Determine whether $\mathrm{AD}^{L(\mathbb{R})}$ implies every set in $L(\mathbb{R})$ is $\mathcal{H}$-Ramsey for every semiselective coideal $\mathcal{H}\in L(\mathbb{R})$.

## 9. Key References

- **[Foundational]** J. Silver. *Every analytic set is Ramsey.* Journal of Symbolic Logic 35 (1970), 60–64.
- **[Foundational]** F. Galvin, K. Prikry. *Borel sets and Ramsey's theorem.* Journal of Symbolic Logic 38 (1973), 193–198.
- **[Foundational]** E. Ellentuck. *A new proof that analytic sets are Ramsey.* Journal of Symbolic Logic 39 (1974), 163–165.
- **[Foundational]** A. R. D. Mathias. *Happy families.* Annals of Mathematical Logic 12 (1977), 59–111.
- **[SOTA]** I. Farah. *Semiselective coideals.* Mathematika 45 (1998), 79–103.
- **[SOTA]** C. A. Di Prisco, S. Todorcevic. *Perfect set properties in $L(\mathbb{R})[U]$.* Advances in Mathematics 139 (1998), 240–259.
- **[SOTA]** H. Judah, S. Shelah. *$\Delta^1_2$-sets of reals.* Annals of Pure and Applied Logic 42 (1989), 207–223.
- **[Foundational]** J. Baumgartner, R. Laver. *Iterated perfect-set forcing.* Annals of Mathematical Logic 17 (1979), 271–288.
- **[Survey]** S. Todorcevic. *Introduction to Ramsey Spaces.* Annals of Mathematics Studies 174, Princeton University Press, 2010.
- **[Survey]** T. Bartoszyński, H. Judah. *Set Theory: On the Structure of the Real Line.* A K Peters, 1995.
- **[Survey]** T. Jech. *Set Theory: The Third Millennium Edition.* Springer, 2003 (Ch. 26, 32).
- **[Recent]** J. Brendle, B. Löwe. *Solovay-type characterizations for forcing-algebras.* Journal of Symbolic Logic 64 (1999), 1307–1323.

## 10. Worked Example / Concrete Special Case

**A closed set that is not $\mathcal{W}$-Ramsey for a non-selective ultrafilter.**

Partition $\omega=\bigsqcup_{n\in\omega} I_n$ with each $I_n$ infinite (take $I_n$ the $n$-th column under a bijection $\omega\times\omega\to\omega$). Fix nonprincipal ultrafilters $\mathcal{V}$ on $\omega$ and $\mathcal{V}_n$ on $I_n$, and form the sum
$$\mathcal{W}=\textstyle\sum_{\mathcal{V}}\mathcal{V}_n=\{X\subseteq\omega:\{n:X\cap I_n\in\mathcal{V}_n\}\in\mathcal{V}\}.$$
$\mathcal{W}$ is an ultrafilter, hence a coideal. Let
$$\mathcal{A}=\{X\in[\omega]^{\omega}:\ \forall n\ |X\cap I_n|\le 1\}.$$
$\mathcal{A}$ is closed in the metric topology (membership is decided by finite initial segments), so it is analytic.

*Step 1 — no homogeneous set inside $\mathcal{A}$.* If $X\in\mathcal{W}$, then $X\cap I_n\in\mathcal{V}_n$, hence infinite, for $\mathcal{V}$-many $n$. So $|X\cap I_n|\ge 2$ for some $n$, giving $X\notin\mathcal{A}$ and thus $[X]^{\omega}\not\subseteq\mathcal{A}$.

*Step 2 — no homogeneous set avoiding $\mathcal{A}$.* Any $X\in\mathcal{W}$ meets infinitely many blocks. Picking one point of $X$ from each of infinitely many blocks gives $Y\in[X]^{\omega}$ with $|Y\cap I_n|\le1$, so $Y\in[X]^{\omega}\cap\mathcal{A}\ne\varnothing$.

Hence $\mathcal{A}$ is **not** $\mathcal{W}$-Ramsey: Silver's theorem is genuinely local, and $\mathcal{W}$ fails semiselectivity precisely because the decreasing sequence $A_k=\bigcup_{n\ge k}I_n$ admits no diagonalization inside $\mathcal{W}$.

**Why forcing enters.** Let $\mathcal{U}\in V$ be selective and let $c$ be Cohen-generic over $V$. By genericity, for every infinite $U\in V$ both $U\cap c$ and $U\setminus c$ are infinite, so neither $c$ nor $\omega\setminus c$ almost-contains a member of $\mathcal{U}$: in $V[c]$, $\mathcal{U}$ generates a filter that is **not** an ultrafilter, and its dual coideal $\mathcal{H}_{\mathcal{U}}$ contains both $c$ and $\omega\setminus c$. Whether $\mathcal{H}_{\mathcal{U}}$ is semiselective in $V[c]$ — equivalently, whether analytic sets are $\mathcal{H}_{\mathcal{U}}$-Ramsey there, avoiding the failure pattern of Steps 1–2 for every new $\omega$-sequence of ground-model sets — is exactly problem (P1) in its smallest nontrivial instance, and is open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*