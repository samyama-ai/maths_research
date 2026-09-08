---
id: 02-algebra-group-theory/feits-conjecture-on-character-fields
title: "Feit's Conjecture on Character Field Degrees"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Feit's Conjecture on Character Field Degrees

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/feits-conjecture-on-character-fields` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite group and $\chi \in \operatorname{Irr}(G)$ an irreducible complex character. Let

$$c(\chi) \;=\; \min\{\, n \in \mathbb{Z}_{>0} \;:\; \mathbb{Q}(\chi) \subseteq \mathbb{Q}_n \,\},$$

where $\mathbb{Q}(\chi) = \mathbb{Q}(\chi(g) : g \in G)$ is the field of values of $\chi$ and $\mathbb{Q}_n = \mathbb{Q}(\zeta_n)$ with $\zeta_n = e^{2\pi i/n}$. The number $c(\chi)$ is called the **Feit number** (or conductor) of $\chi$.

**Conjecture (Feit, 1979).** For every finite group $G$ and every $\chi \in \operatorname{Irr}(G)$, the group $G$ contains an element $g$ with
$$o(g) = c(\chi).$$

A complete proof must establish this for all finite $G$ (equivalently, by CFSG-based reduction if one existed, for a suitable class of almost simple groups). A disproof requires one explicit pair $(G,\chi)$ with $c(\chi)$ not an element order of $G$.

Because the set of element orders of a finite group is closed under divisors ($o(g)=N$ and $n \mid N$ give $o(g^{N/n})=n$), the conjecture is **equivalent** to the weaker-looking statement:
$$\exists\, g \in G \ \text{ with } \ c(\chi) \mid o(g).$$

## 2. Mathematical Foundations

**Cyclotomic containment.** By Brauer's theorem on representations over $\mathbb{Q}_{|G|}$ (Brauer 1945) and Brauer's induction theorem, every $\chi \in \operatorname{Irr}(G)$ satisfies
$$\mathbb{Q}(\chi) \subseteq \mathbb{Q}_{\exp(G)},$$
where $\exp(G)$ is the exponent. Hence $c(\chi)$ is well defined and $c(\chi) \mid \exp(G)$.

**Galois action.** $\operatorname{Gal}(\mathbb{Q}_n/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times$, and for $\sigma_k$ the automorphism $\zeta_n \mapsto \zeta_n^k$ one has the fundamental formula
$$\chi^{\sigma_k}(g) \;=\; \chi(g^k) \qquad (k \text{ coprime to } \exp(G)).$$
Thus $\mathbb{Q}(\chi)$ is the fixed field of
$$H_\chi \;=\; \{\, \sigma_k \in \operatorname{Gal}(\mathbb{Q}_{\exp G}/\mathbb{Q}) \;:\; \chi(g^k)=\chi(g)\ \forall g \,\},$$
and $c(\chi)$ is the **conductor** of the abelian number field $\mathbb{Q}(\chi)$ in the sense of Kronecker–Weber: the least $n$ with $\mathbb{Q}(\chi) \subseteq \mathbb{Q}_n$. Note the standard normalisation artefact $\mathbb{Q}_{2m} = \mathbb{Q}_m$ for odd $m$, so $c(\chi) \not\equiv 2 \pmod 4$.

**Reformulation via class functions.** $\sigma_k$ permutes $\operatorname{Irr}(G)$ and permutes conjugacy classes by $g \mapsto g^k$. Feit's conjecture asserts that the *arithmetic* invariant $c(\chi)$, a datum of the Galois module $\mathbb{C}\operatorname{Irr}(G)$, is realised by the *group-theoretic* spectrum $\operatorname{spec}(G) = \{o(g): g\in G\}$.

**Non-vacuity.** $c(\chi) \mid \exp(G)$ does not imply $c(\chi) \in \operatorname{spec}(G)$ a priori: for $G = A_5$, $\exp(G)=30$ but $\operatorname{spec}(A_5)=\{1,2,3,5\}$; the divisors $6,10,15,30$ of the exponent are not element orders. The conjecture is exactly the assertion that no Feit number ever lands in such a gap.

**Global Feit number.** One also studies $f(G) = \operatorname{lcm}\{c(\chi) : \chi \in \operatorname{Irr}(G)\}$. Here $f(G) \mid \exp(G)$ but equality fails ($Q_8$ has all characters rational, $f=1$, $\exp = 4$).

## 3. History & State of the Art (SOTA)

- **1979/1980.** Walter Feit posed the question in his problem list at the Santa Cruz Conference on Finite Groups, published as *Some consequences of the classification of finite simple groups* (Proc. Sympos. Pure Math. 37, AMS, 1980). It is one of a family of problems asking how much of the character-theoretic arithmetic of $G$ is visible in the element orders of $G$. It was subsequently recorded in the Kourovka Notebook.
- **1986.** Amit and Chillag proved the conjecture for all **solvable** groups (Pacific J. Math. 122), using Hall subgroup theory and character correspondences unavailable in general.
- **1980s–1990s.** Verification for sporadic groups and small simple groups directly from the ATLAS of Finite Groups character tables; the required field data (indicator/irrationality columns) is tabulated there.
- **2000s.** Navarro and Tiep's programme on rationality (rational characters vs. rational classes, Trans. AMS 2008) supplied CFSG-based tools for controlling $\mathbb{Q}(\chi)$ in simple groups, but did not resolve the general case.
- **2010s–2020s.** The Galois–McKay (Navarro) conjecture and its verification programme (Navarro, Späth, Ruhstorfer, Vallejo, Rossi) produced sharp control of Galois actions on characters of local subgroups. This machinery is the most promising modern source of leverage; it has not yet been converted into a proof of Feit's conjecture.

**Status.** Open in general. No counterexample has appeared in a refereed venue as of this review; occasional preprints claiming counterexamples or full reductions should be checked directly against the source *(frontier — verify)*.

## 4. Partial Results / Verified Cases

- **Solvable groups.** Proved by Amit–Chillag (1986). Consequently the conjecture holds for all $p$-groups, all nilpotent groups, all supersolvable groups, and all groups of order $p^aq^b$ (Burnside).
- **Linear characters (any $G$).** If $\lambda \in \operatorname{Irr}(G)$ has degree $1$ and multiplicative order $n$, then $\mathbb{Q}(\lambda)=\mathbb{Q}_n$ (up to the mod-4 normalisation) and $\lambda$ factors through $G/G'$. Any $gG'$ of order $n$ has $n \mid o(g)$, so $g^{o(g)/n}$ has order exactly $n$. Proof is two lines; this is the model case.
- **Rational groups.** If $\mathbb{Q}(\chi)=\mathbb{Q}$ then $c(\chi)=1$ and $g=1$ works. Hence all symmetric groups $S_n$, all Weyl groups, $Q_8$, $SL(2,3)$'s rational characters, and every rational group satisfy the conjecture trivially.
- **Alternating and sporadic groups.** Verified computationally. E.g. $A_5, A_6, A_7$: all irrationalities are $\sqrt{5}, \sqrt{-3}, \sqrt{-7}$ etc. with conductors $5, 3, 7$, all element orders. For the Monster all $c(\chi)$ read off the ATLAS lie in $\operatorname{spec}(M)$.
- **Groups of Lie type, Deligne–Lusztig characters.** For $\chi$ lying in the Lusztig series of a semisimple $s \in G^{*}$ with $\theta \in \operatorname{Irr}(T)$ a torus character, the field $\mathbb{Q}(\chi)$ is controlled by $\mathbb{Q}(\theta) \subseteq \mathbb{Q}_{o(\theta)}$, and $o(\theta)$ divides $|T|$, an element order in the maximal torus $T \le G$. This gives the conjecture for large explicit families (e.g. characters of $GL_n(q)$, $SL_2(q)$, $PSL_2(q)$, $Sz(q)$, ${}^2G_2(q)$, whose character fields are known in closed form).
- **Small orders.** Exhaustive machine verification over all groups in the GAP/Magma small-groups libraries (all $|G| \le 2000$, $|G| \ne 1024$, plus all perfect groups of order $\le 10^6$) finds no counterexample.

## 5. Principal Obstacles

- **No inductive reduction.** Unlike McKay-type conjectures, Feit's conjecture has no known reduction to (quasi-)simple groups. The obstruction is that $c(\chi)$ is not a Clifford-theoretically additive invariant: for $N \trianglelefteq G$ and $\chi$ lying over $\theta \in \operatorname{Irr}(N)$, one only gets $\mathbb{Q}(\chi) \subseteq \mathbb{Q}(\theta, \zeta_{|G:N|})$ with no matching lower bound. Schur indices and the class in $H^2(G_\theta/N, \mathbb{C}^\times)$ can both enlarge and shrink the field of values in ways not visible from $\theta$.
- **Element orders do not lift.** The dual half of the induction also fails: $G/N$ having an element of order $n$ does not give $G$ an element of order $n$ (e.g. $G$ a non-split extension, $G/N \cong C_p$ with all preimages of order $p^2$). So even a perfect field-of-values reduction would not close the argument.
- **Solvable methods do not generalise.** Amit–Chillag rely on Hall $\pi$-subgroups, $\pi$-special factorisations, and Isaacs-style character correspondences — all of which require solvability. There is no non-solvable substitute that tracks $\mathbb{Q}(\chi)$ through a chief series.
- **Mixed local–global data.** $c(\chi)$ is a single global conductor, but the natural tools (Brauer's induction theorem, block theory, Galois–McKay) produce information prime by prime. Reassembling $c(\chi) = \prod_p p^{a_p}$ into a *single* element of order $c(\chi)$ requires commuting elements of coprime prime-power orders — precisely what fails in simple groups with prime graph gaps (e.g. $A_5$ has elements of orders 2, 3, 5 but of no composite order).
- **Sporadic-looking irrationalities.** Character fields of exceptional groups of Lie type in the unipotent-support range are computed case-by-case; no uniform theorem bounds their conductors by torus element orders.

## 6. The Gap

Proven: all solvable $G$; all $\chi$ with $\mathbb{Q}(\chi)=\mathbb{Q}$ or $\deg\chi=1$; all $\chi$ in the alternating, sporadic, and many classical/Lie families where $\mathbb{Q}(\chi)$ is explicitly computed.

Missing: a statement of the form

> **(Reduction goal.)** For $N \trianglelefteq G$, $\theta \in \operatorname{Irr}(N)$ $G$-invariant, and $\chi \in \operatorname{Irr}(G \mid \theta)$, there is $m \mid c(\chi)$ with $m \in \operatorname{spec}(G/N)$-controlled data and $c(\chi) / m \mid c(\theta)$, together with an element of $G$ realising the product.

The precise barrier is the **coprime-recombination step**: given that each prime-power part $p^{a_p} \| c(\chi)$ is realised by some $g_p \in G$ of order $p^{a_p}$ (which the local theory plausibly delivers), one must produce a *single* element of order $c(\chi)$, i.e. show that the relevant $g_p$ can be chosen pairwise commuting. Nothing in the Galois-theoretic input forces commutation, and in $A_5$ this recombination genuinely fails for arbitrary divisors of $\exp(G)$ — the conjecture claims character fields never ask for it.

## 7. Current Research (as of June 2026)

- **Valencia school (G. Navarro and collaborators).** Fields of values of characters of $p'$-degree, $p$-rationality, and Galois-action refinements of McKay. Techniques here give exact $p$-parts of $c(\chi)$ for $\chi$ of $p'$-degree, the closest thing to a local attack.
- **Rutgers (P. H. Tiep) and Kaiserslautern (G. Malle).** CFSG-based determination of character fields for simple groups; the remaining unresolved families are exceptional groups in small characteristic *(frontier — verify)*.
- **Wuppertal (B. Späth, L. Ruhstorfer, D. Rossi).** Verification of the inductive Galois–McKay condition; recent progress toward the full Galois–McKay conjecture supplies equivariant bijections compatible with Galois action, potentially yielding conductor control at each prime *(frontier — verify)*.
- **Computational group theory (GAP CTblLib, Magma).** Ongoing extension of exhaustive verification to larger perfect and almost simple groups and their central/automorphic extensions.
- **Clifford-theory-with-fields (A. Turull's endoisomorphism framework).** Tracks Schur indices and fields of values simultaneously through normal subgroups; the main hope for a genuine reduction theorem.

## 8. Future Work

1. **Formulate and verify an inductive condition** for Feit's conjecture in the style of the inductive McKay/Alperin conditions, so that CFSG can be applied.
2. **Prove the prime-power case**: show that if $c(\chi)=p^a$ then $G$ has an element of order $p^a$. This is open for non-solvable $G$ and would isolate the recombination difficulty.
3. **Strengthened forms.** Feit also asked whether one can require $\chi(g) \ne 0$ for the witnessing element $g$, or that $\chi(g)$ generate $\mathbb{Q}(\chi)$. Counterexamples or proofs here would sharpen understanding of which classes carry the field.
4. **Torus-theoretic proof for Lie type.** Show uniformly that for $G$ of Lie type, every $c(\chi)$ divides the order of an element of some maximal torus, using Lusztig's Jordan decomposition.
5. **Search for counterexamples** in groups with sparse prime graphs (simple groups where few composite element orders occur), which is where a failure would have to live.

## 9. Key References

- **[Foundational]** W. Feit. *Some consequences of the classification of finite simple groups.* In: The Santa Cruz Conference on Finite Groups, Proc. Sympos. Pure Math. 37, American Mathematical Society, 1980, pp. 175–181.
- **[Foundational]** R. Brauer. *On the representation of a group of order $g$ in the field of the $g$-th roots of unity.* American Journal of Mathematics 67 (1945), 461–471.
- **[Key partial result]** G. Amit and D. Chillag. *On a question of Feit concerning character values of finite solvable groups.* Pacific Journal of Mathematics 122 (1986), no. 2, 257–261.
- **[Textbook]** I. M. Isaacs. *Character Theory of Finite Groups.* Academic Press, 1976 (Dover reprint 1994). Chapter 9 (fields of values, Galois action) and Chapter 10 (Schur indices).
- **[SOTA / Recent]** G. Navarro and P. H. Tiep. *Rational irreducible characters and rational conjugacy classes in finite groups.* Transactions of the American Mathematical Society 360 (2008), 2443–2465.
- **[Survey / Monograph]** G. Navarro. *Character Theory and the McKay Conjecture.* Cambridge Studies in Advanced Mathematics 175, Cambridge University Press, 2018.
- **[Reference data]** J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson. *ATLAS of Finite Groups.* Oxford University Press, 1985.
- **[Survey]** Y. Berkovich and E. Zhmud. *Characters of Finite Groups, Parts 1–2.* Translations of Mathematical Monographs 172/181, American Mathematical Society, 1998/1999.
- **[Problem list]** E. I. Khukhro and V. D. Mazurov (eds.). *Unsolved Problems in Group Theory: The Kourovka Notebook.* 20th edition, Sobolev Institute of Mathematics, 2022.

## 10. Worked Example / Concrete Special Case

**Case $G = A_5$ (non-solvable, exponent gap).** $\operatorname{Irr}(A_5)$ has degrees $1,3,3,4,5$ and element orders $\operatorname{spec}(A_5)=\{1,2,3,5\}$, while $\exp(A_5)=30$.

| $\chi$ | $\chi(1)$ | values on classes $1,(12)(34),(123),(12345),(13524)$ | $\mathbb{Q}(\chi)$ | $c(\chi)$ | witness $g$ |
|---|---|---|---|---|---|
| $\chi_1$ | 1 | $1,1,1,1,1$ | $\mathbb{Q}$ | 1 | identity |
| $\chi_2$ | 3 | $3,-1,0,\tfrac{1+\sqrt5}{2},\tfrac{1-\sqrt5}{2}$ | $\mathbb{Q}(\sqrt5)$ | 5 | 5-cycle |
| $\chi_3$ | 3 | $3,-1,0,\tfrac{1-\sqrt5}{2},\tfrac{1+\sqrt5}{2}$ | $\mathbb{Q}(\sqrt5)$ | 5 | 5-cycle |
| $\chi_4$ | 4 | $4,0,1,-1,-1$ | $\mathbb{Q}$ | 1 | identity |
| $\chi_5$ | 5 | $5,1,-1,0,0$ | $\mathbb{Q}$ | 1 | identity |

For $\chi_2$: the golden-ratio values are $\tfrac{1\pm\sqrt5}{2} = -(\zeta_5^2+\zeta_5^3)$ and $-(\zeta_5+\zeta_5^4)$, so $\mathbb{Q}(\chi_2) = \mathbb{Q}(\sqrt 5)$, the unique quadratic subfield of $\mathbb{Q}_5$. Its conductor is $5$ (it is not contained in $\mathbb{Q}_1,\mathbb{Q}_3,\mathbb{Q}_4$; and $\mathbb{Q}_2=\mathbb{Q}$). Hence $c(\chi_2)=5$, and $A_5$ contains a 5-cycle. ✔

Note the conjecture had room to fail: $6, 10, 15, 30$ all divide $\exp(A_5)$ but are not element orders. Had any $\chi$ had field $\mathbb{Q}(\zeta_{15})^{+}$ or $\mathbb{Q}(\sqrt{-15})$ (conductor 15), the conjecture would break. The Galois-action formula explains why it does not: $\sigma_k$ fixes $\chi_2$ iff $k \equiv \pm 1 \pmod 5$, so the stabiliser is the full preimage of a subgroup of $(\mathbb{Z}/5\mathbb{Z})^\times$ and the conductor is supported only at 5 — the prime of the element realising the irrationality.

**Case $G = C_7 \rtimes C_3 = F_{21}$ (solvable, covered by Amit–Chillag).** $\operatorname{Irr}(F_{21})$ = three linear characters plus two of degree 3. A degree-3 character takes value $\tfrac{-1+\sqrt{-7}}{2} = \zeta_7+\zeta_7^2+\zeta_7^4$ on one class of 7-elements, so $\mathbb{Q}(\chi)=\mathbb{Q}(\sqrt{-7})$, conductor $7$; $F_{21}$ has elements of order 7. ✔ The nontrivial linear characters have $\mathbb{Q}(\lambda)=\mathbb{Q}(\zeta_3)$, conductor $3$; $F_{21}$ has elements of order 3. ✔ In both cases the conductor is realised by a *single* prime, so the coprime-recombination step of Section 6 never has to be performed — which is exactly why small examples give little evidence about the general difficulty.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*