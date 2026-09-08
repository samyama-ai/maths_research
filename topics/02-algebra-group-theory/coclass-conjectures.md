---
id: 02-algebra-group-theory/coclass-conjectures
title: "Coclass Conjectures for Pro-p Groups"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Coclass Conjectures for Pro-p Groups

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/coclass-conjectures` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

A finite $p$-group $G$ of order $p^n$ and nilpotency class $c$ has **coclass** $r = n - c$. Coclass measures how far $G$ is from being of maximal class. Leedham-Green and Newman (1980) proposed five conjectures asserting that fixing $p$ and $r$ — rather than fixing the order — forces strong uniform structure:

- **Conjecture A.** There is $f(p,r)$ such that every finite $p$-group of coclass $r$ has a normal subgroup $K$ of nilpotency class at most $2$ (class at most $1$, i.e. abelian, when $p = 2$) with $[G:K] \le f(p,r)$.
- **Conjecture B.** There is $g(p,r)$ bounding the derived length of every finite $p$-group of coclass $r$.
- **Conjecture C.** Every pro-$p$ group of finite coclass is soluble.
- **Conjecture D.** Every pro-$p$ group of finite coclass is $p$-adic analytic.
- **Conjecture E.** For each $p$ and $r$ there are only finitely many infinite pro-$p$ groups of coclass $r$.

Logically $A \Rightarrow B$, $D \Rightarrow C$, and $D + E \Rightarrow A$ by a compactness argument on the coclass graph. All five are now theorems (Leedham-Green 1994; Shalev 1994), so the entry is filed as *solved-recently* in the historical sense. What remains open is the **second-generation coclass programme**: determining the optimal $f(p,r)$, $g(p,r)$, proving full periodicity of the coclass graph $\mathcal{G}(p,r)$ for all $p$ and $r$, and deciding the analogous statements in the Lie-algebra and other settings where Conjecture E is known to fail.

## 2. Mathematical Foundations

Let $G$ be a finite $p$-group with lower central series
$$G = \gamma_1(G) \ge \gamma_2(G) \ge \cdots \ge \gamma_c(G) > \gamma_{c+1}(G) = 1,\qquad \gamma_{i+1}(G) = [\gamma_i(G), G].$$
If $|G| = p^n$ then $\mathrm{cc}(G) = n - c \ge 1$, since each factor $\gamma_i/\gamma_{i+1}$ has order at least $p$. Coclass $1$ ("maximal class") means every factor $\gamma_i/\gamma_{i+1}$, $2 \le i \le c$, has order exactly $p$; the action of $G$ on the chain is then **uniserial**.

For a pro-$p$ group $G$ with $\gamma_i(G)$ the closed lower central terms, set
$$\mathrm{cc}(G) = \sum_{i \ge 1} \big(\log_p |\gamma_i(G) : \gamma_{i+1}(G)| - 1\big) \in \mathbb{N} \cup \{\infty\},$$
which agrees with $n-c$ in the finite case. An infinite pro-$p$ group of finite coclass is *just infinite* modulo its finite residual and is exactly the inverse limit of an infinite path in:

**Coclass graph $\mathcal{G}(p,r)$.** Vertices are the isomorphism types of finite $p$-groups of coclass $r$; the parent of $G$ is $G/\gamma_c(G)$ (a group of the same coclass). $\mathcal{G}(p,r)$ is a forest whose infinite paths ("mainlines") correspond bijectively to infinite pro-$p$ groups of coclass $r$.

**$p$-adic space groups.** The structure theorem (Conjectures D + E) states: an infinite pro-$p$ group $S$ of coclass $r$ has a normal translation subgroup $T \cong \mathbb{Z}_p^{\,d}$ of finite index with $P = S/T$ a finite $p$-group acting faithfully and uniserially on $T$, so
$$1 \to \mathbb{Z}_p^{\,d} \to S \to P \to 1 ,\qquad d = \dim S \le \lambda(p,r).$$
For $r = 1$ one has $d = p-1$ and $T \cong \mathbb{Z}_p[\zeta_p]$ as a module over the point group. Such $S$ is $p$-adic analytic of dimension $d$ (Lazard; see Dixon–du Sautoy–Mann–Segal), i.e. a compact $p$-adic Lie group.

**Lie method.** Associate to $G$ the graded $\mathbb{F}_p$-Lie ring $L(G) = \bigoplus_i \gamma_i(G)/\gamma_{i+1}(G)$ with bracket induced by commutation. Coclass $r$ bounds the *width* of $L(G)$: all but at most $r$ homogeneous components have dimension $1$. Shalev–Zelmanov's classification of narrow graded Lie algebras, together with Zelmanov's solution of the restricted Burnside problem, is the engine of the modern proofs.

## 3. History & State of the Art (SOTA)

- **1980.** Leedham-Green and Newman, *Space groups and groups of prime-power order I* (Arch. Math. 35), introduce coclass and state Conjectures A–E, motivated by the analogy with crystallographic space groups of fixed dimension.
- **1986.** Leedham-Green, McKay and Plesken bound the dimension of a $2$-adic space group of fixed coclass, completing the $p = 2$ case of all five conjectures.
- **1987.** Donkin (*J. Algebra* 111) proves, via algebraic-group and $p$-adic Lie algebra methods, that a **soluble** pro-$p$ group of finite coclass is $p$-adic analytic, i.e. $C \Rightarrow D$.
- **1992–94.** Shalev and Zelmanov prove Conjecture C for all $p$ using narrow Lie algebras. Independently, Leedham-Green (*J. LMS* 50, 1994) proves the structure theorem and Conjecture A; Shalev (*Invent. Math.* 115, 1994) gives an **effective** proof of A–E with explicit bounds.
- **2000–2008.** Second generation: du Sautoy (*Publ. IHÉS* 92) uses zeta functions and $p$-adic model theory to show the coclass trees are eventually periodic; Eick and Leedham-Green (*Bull. LMS* 40, 2008) prove **Conjecture W**: for fixed $p, r$ all but finitely many groups of coclass $r$ lie in finitely many *coclass families*, each parametrised by a single integer with uniform presentations.
- **2013.** Eick, Leedham-Green, Newman and O'Brien complete the classification of the $3$-groups of coclass $2$, the first full odd-$p$, $r>1$ case.

## 4. Partial Results / Verified Cases

- **$p = 2$, all $r$:** complete. Sharp structural results, explicit lists of the infinite pro-$2$ groups of each coclass, and full periodicity of $\mathcal{G}(2,r)$ are known (Leedham-Green–McKay–Plesken; Eick–Leedham-Green).
- **$r = 1$ (maximal class), all $p$:** the unique infinite pro-$p$ group of coclass $1$ is $S = \mathbb{Z}_p[\zeta_p] \rtimes C_p$, of dimension $p-1$. Blackburn (1958) classified maximal-class $p$-groups for $p \le 5$; periodicity of $\mathcal{G}(p,1)$ is a theorem (Eick–Leedham-Green, *Periodic patterns in the graph of p-groups of maximal class*).
- **$p = 3$, $r = 2$:** fully classified (2013), with all $16$ coclass trees and their periodic branch patterns determined.
- **General $p, r$:** Conjectures A–E hold with effective bounds (Shalev 1994); Conjecture W holds (2008), so the classification is "finite modulo periodicity".
- **Counterexample in the Lie setting:** Caranti, Mattarei and Newman (Trans. AMS 349, 1997) construct *infinitely many* pairwise non-isomorphic infinite-dimensional graded Lie algebras of maximal class over $\mathbb{F}_p$. The exact analogue of Conjecture E is therefore **false** for Lie algebras in characteristic $p$.

## 5. Principal Obstacles

- **Bounds are astronomically bad.** Shalev's effective proof passes through Zelmanov's solution of the restricted Burnside problem, whose quantitative content is of Ackermann-type. The resulting $f(p,r)$, $g(p,r)$ are explicit but vastly larger than any conjectured truth; no method is known that avoids Zelmanov's machinery while retaining full generality.
- **The Lie correspondence loses information.** Passing to $L(G)$ replaces a group by a graded $\mathbb{F}_p$-algebra, and the Caranti–Mattarei–Newman examples show the target category is strictly wilder: the group-theoretic finiteness must be recovered from the $p$-adic (characteristic $0$) lift, not from $L(G)$ itself. Lifting is where uniformity in $p$ collapses.
- **No uniformity in $p$.** Every known argument fixes $p$ and produces constants depending on $p$ in an uncontrolled way; the dimension $d = p-1$ already at $r=1$ shows genuine $p$-dependence, but nothing separates real $p$-dependence from artefacts of the proof.
- **Branch complexity.** Even with Conjecture W, the *number* of coclass families and the finitely many exceptional groups are not bounded by any known function of $p$ and $r$; the proofs are non-constructive at that layer, so classification remains a machine computation per $(p,r)$.

## 6. The Gap

The gap is no longer existence but **effectivity and periodicity in full generality**:

1. **Quantitative gap.** Proven: $f(p,r) < \infty$. Wanted: the true growth rate. Is $f(p,r) \le p^{O(r)}$, as the $p=2$ data suggest, or genuinely super-exponential?
2. **Periodicity gap.** Proven: all but finitely many groups of coclass $r$ lie in finitely many coclass families (Conjecture W). Wanted: an algorithm, uniform in $(p,r)$, that outputs the families, the exceptional set, and the periodicity parameters — currently obtained only case by case (all $r$ for $p=2$; $r=1$ for all $p$; $(p,r)=(3,2)$).
3. **Cross-category gap.** Proven for pro-$p$ groups; false for graded $\mathbb{F}_p$-Lie algebras. The precise hypothesis that rescues the coclass theorem — some form of $p$-adic liftability or a restriction on the Lie algebra's "constituent" structure — is not isolated.

## 7. Current Research (as of June 2026)

- **Constructive coclass theory** (Eick and collaborators, TU Braunschweig): algorithmic determination of coclass families and their parametrised presentations, implemented in GAP's `ANUPQ`/coclass packages; extension to $p = 5$, $r = 2$ is in progress *(frontier — verify)*.
- **Coclass for nilpotent Lie rings and pro-$p$ rings** (Eick–Feichtenschlager): the coclass graph of nilpotent $\mathbb{Z}_p$-Lie rings exhibits the same periodicity, giving a cleaner model in which effective bounds may be reachable.
- **Zeta functions and definability** (du Sautoy school, Oxford/Nottingham): counting $p$-groups by coclass via $p$-adic integrals; the rationality of the associated generating functions is the mechanism behind periodicity, and uniformity in $p$ is the live question.
- **Maximal class in characteristic $p$** (Caranti, Mattarei, Avitabile, Trento): classification of infinite-dimensional graded Lie algebras of maximal class by "constituent sequences", clarifying exactly how Conjecture E fails.
- **Pro-$p$ groups of finite width and analyticity**: extending the coclass philosophy to obliquity, width, and $p$-adic analytic detection criteria for just-infinite pro-$p$ groups.

## 8. Future Work

- Extract a Zelmanov-free proof of Conjecture C for odd $p$ to obtain polynomial-type bounds on $f(p,r)$.
- Prove a uniform-in-$p$ version of Conjecture W: bound the number of coclass families and the exceptional set by an explicit function of $p$ and $r$.
- Determine the exact list of infinite pro-$p$ groups of coclass $r$ (Conjecture E's quantitative form): find $N(p,r) = \\#\{$infinite pro-$p$ groups of coclass $r\}$ in closed form; only $N(p,1) = 1$ and the $p=2$ values are known.
- Identify the extra hypothesis under which the coclass theorem holds for graded Lie algebras over $\mathbb{F}_p$, reconciling the group and Lie pictures.
- Push machine classification to $(p,r) = (5,2)$ and $(3,3)$ and test conjectured periodicity lengths against the predicted $p$-adic parameters.

## 9. Key References

- **[Foundational]** C. R. Leedham-Green, M. F. Newman. *Space groups and groups of prime-power order I.* Archiv der Mathematik 35 (1980), 193–202.
- **[Foundational]** C. R. Leedham-Green, S. McKay, W. Plesken. *Space groups and groups of prime power order V: a bound to the dimension of a 2-adic space group with fixed coclass.* Proc. London Math. Soc. (3) 52 (1986), 73–94.
- **[Foundational]** S. Donkin. *Space groups and groups of prime-power order VIII: pro-p-groups of finite coclass and p-adic Lie algebras.* Journal of Algebra 111 (1987), 8–33.
- **[SOTA]** C. R. Leedham-Green. *The structure of finite p-groups.* J. London Math. Soc. (2) 50 (1994), 49–67.
- **[SOTA]** A. Shalev. *The structure of finite p-groups: effective proof of the coclass conjectures.* Inventiones Mathematicae 115 (1994), 315–345.
- **[SOTA]** A. Shalev, E. I. Zelmanov. *Narrow Lie algebras: a coclass theory and a characterization of the Witt algebra.* Journal of Algebra 189 (1997), 294–331.
- **[SOTA / Recent]** M. du Sautoy. *Counting p-groups and nilpotent groups.* Publ. Math. IHÉS 92 (2000), 63–112.
- **[SOTA / Recent]** B. Eick, C. R. Leedham-Green. *On the classification of prime-power groups by coclass.* Bull. London Math. Soc. 40 (2008), 274–288.
- **[SOTA / Recent]** B. Eick, C. R. Leedham-Green, M. F. Newman, E. A. O'Brien. *On the classification of groups of prime-power order by coclass: the 3-groups of coclass 2.* Internat. J. Algebra Comput. 23 (2013), 1243–1288.
- **[Counterexample]** A. Caranti, S. Mattarei, M. F. Newman. *Graded Lie algebras of maximal class.* Trans. Amer. Math. Soc. 349 (1997), 4021–4051.
- **[Survey / Book]** C. R. Leedham-Green, S. McKay. *The Structure of Groups of Prime Power Order.* LMS Monographs New Series 27, Oxford University Press, 2002.
- **[Survey / Book]** J. D. Dixon, M. du Sautoy, A. Mann, D. Segal. *Analytic Pro-p Groups.* 2nd ed., Cambridge University Press, 1999.
- **[Survey]** A. Shalev. *Finite p-groups.* In *Finite and Locally Finite Groups*, NATO ASI Series C 471, Kluwer, 1995, 401–450.

## 10. Worked Example / Concrete Special Case

**Case $p = 2$, $r = 1$: coclass theory in full, by hand.**

Let $G$ be a finite $2$-group of order $2^n$, $n \ge 3$, and coclass $1$, so its class is $c = n-1$ and
$$|\gamma_i(G) : \gamma_{i+1}(G)| = 2 \quad (2 \le i \le c), \qquad |G : \gamma_2(G)| = 4 .$$
Hence $G/\gamma_2(G) \cong C_2 \times C_2$, so $G$ has exactly three maximal subgroups $M_1, M_2, M_3$, each of index $2$.

*Step 1 (a maximal subgroup is cyclic).* Uniseriality gives $|\gamma_i(G)|=2^{\,n-i}$, so the chain $\gamma_2 > \gamma_3 > \cdots$ descends by steps of $2$. Burnside's classification of $2$-groups of maximal class shows this forces one $M_i$ to be cyclic of order $2^{n-1}$. Write $M = \langle a \rangle$, $a^{2^{n-1}} = 1$.

*Step 2 (the extension).* Pick $b \in G \setminus M$. Conjugation gives an automorphism $a \mapsto a^k$ of $C_{2^{n-1}}$ of order dividing $2$, so $k^2 \equiv 1 \pmod{2^{n-1}}$, i.e. $k \in \{-1,\ 1+2^{n-2},\ -1+2^{n-2}\}$ (excluding $k=1$, which gives class $\le 1$ contradicting $c=n-1\ge 2$). Together with $b^2 \in \{1, a^{2^{n-2}}\}$ this yields exactly three groups for each $n \ge 4$:
$$D_{2^n} = \langle a,b \mid a^{2^{n-1}}, b^2, a^b = a^{-1}\rangle,\quad SD_{2^n}\ (a^b = a^{-1+2^{n-2}}),\quad Q_{2^n}\ (a^b=a^{-1},\ b^2=a^{2^{n-2}}).$$

*Step 3 (Conjecture A verified with $f(2,1) = 2$).* In each case $M = \langle a \rangle$ is abelian, normal, of index $2$. So the optimal constant is $2$, and Conjecture B holds with derived length $\le 2$.

*Step 4 (Conjectures C, D, E).* The mainline of $\mathcal{G}(2,1)$ is $D_8 \to D_{16} \to D_{32} \to \cdots$ (the quotients $D_{2^{n}}/\gamma_{n-1}(D_{2^n}) \cong D_{2^{n-1}}$), whose inverse limit is
$$S = \varprojlim D_{2^n} \cong \mathbb{Z}_2 \rtimes C_2, \qquad \text{with } C_2 \text{ acting by } x \mapsto -x .$$
$S$ is soluble (C), $2$-adic analytic of dimension $d = 1 = p-1$ (D), and it is the **only** infinite pro-$2$ group of coclass $1$ (E): $SD_{2^n}$ and $Q_{2^n}$ are terminal or non-mainline vertices, since $Q_{2^n}/\gamma_{n-1} \cong D_{2^{n-1}}$ too. So $N(2,1)=1$, and $\mathcal{G}(2,1)$ is a single tree with an infinite trunk and two leaves hanging from each level — the smallest instance of the periodicity asserted in general by Conjecture W.

Sanity check at $n = 4$: $D_{16}$ has order $2^4$, lower central series $D_{16} > C_4 > C_2 > 1$, class $3$, coclass $4-3 = 1$. ✔

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*