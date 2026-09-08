---
id: 02-algebra-group-theory/burnsides-pq-theorem
title: "Burnside's pq Theorem"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Burnside's pq Theorem

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/burnsides-pq-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Theorem (Burnside, 1904).** Let $p$ and $q$ be primes and let $G$ be a finite group of order
$$|G| = p^a q^b, \qquad a, b \ge 0 .$$
Then $G$ is solvable: there is a chain $1 = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_n = G$ with each $G_{i+1}/G_i$ abelian. Equivalently, no finite simple group has order divisible by exactly two distinct primes (apart from the cyclic groups $C_p$).

The statement is a theorem, not a conjecture. It is catalogued here because the *problem* attached to it is not the truth of the statement but the **structure of its proof** and the reach of its generalisations:

1. **The character-free problem** (Burnside's own question, 1911): find a proof using only group-theoretic arguments — Sylow theory, transfer, fusion, local analysis — with no representation theory over $\mathbb{C}$ and no algebraic number theory. *Resolved 1970–1973 by Goldschmidt, Matsuyama and Bender.*
2. **The elementarity problem**: how much algebraic number theory is genuinely needed in the character-theoretic route; can the vanishing-sums-of-roots-of-unity lemma be replaced?
3. **The formalisation problem**: machine-check the theorem. *Resolved 2007 in Coq/SSReflect.*
4. **The generalisation problem**: which quantitative or structural strengthenings survive. Three primes fail outright ($|A_5| = 2^2\cdot 3\cdot 5$), so the boundary is sharp; the live questions concern products of nilpotent groups and quantitative invariants (derived length, $p$-length) of $\{p,q\}$-groups. *Partly open.*

A complete resolution of (2) and (4) would mean: an exposition-level proof with explicitly minimal prerequisites, plus sharp bounds on the solvable-structure invariants of groups of order $p^aq^b$.

## 2. Mathematical Foundations

**Solvability.** $G$ is solvable iff its derived series $G^{(0)} = G$, $G^{(i+1)} = [G^{(i)}, G^{(i)}]$ reaches $1$. The least $d$ with $G^{(d)} = 1$ is the **derived length** $\mathrm{dl}(G)$.

**Characters.** For a finite group $G$ over $\mathbb{C}$, an irreducible representation $\rho: G \to GL_n(\mathbb{C})$ has character $\chi(g) = \operatorname{tr}\rho(g)$, $\chi(1) = n$. Write $\mathrm{Irr}(G)$ for the set of irreducible characters. Two facts drive the proof:

$$\sum_{\chi \in \mathrm{Irr}(G)} \chi(1)^2 = |G|, \qquad \chi(1) \mid |G| .$$

**Central characters.** For a conjugacy class $K$ with representative $g$, the class sum $\widehat{K} = \sum_{x\in K} x$ lies in $Z(\mathbb{C}G)$, and
$$\omega_\chi(\widehat{K}) \;=\; \frac{|K|\,\chi(g)}{\chi(1)}$$
is an **algebraic integer** for every $\chi \in \mathrm{Irr}(G)$.

**Burnside's vanishing lemma.** If $\chi \in \mathrm{Irr}(G)$, $g \in G$, and $\gcd\bigl(\chi(1), |g^G|\bigr) = 1$, then either $g \in Z(\chi) \pmod{\ker\chi}$ (so $|\chi(g)| = \chi(1)$) or
$$\chi(g) = 0 .$$
*Proof ingredient:* choose $u,v \in \mathbb{Z}$ with $u\chi(1) + v|g^G| = 1$; then $\chi(g)/\chi(1) = u\chi(g) + v\,\omega_\chi(\widehat{g^G})$ is an algebraic integer. Since $\chi(g)$ is a sum of $\chi(1)$ roots of unity, $|\chi(g)/\chi(1)| \le 1$, and the product of the Galois conjugates of $\chi(g)/\chi(1)$ is a rational integer of absolute value $\le 1$; hence it is $0$ or a root of unity.

**Burnside's prime-power class theorem.** If $G$ is a finite simple non-abelian group, then no conjugacy class has size $p^k$ with $k \ge 1$. Proof: from the second orthogonality relation applied to $g \ne 1$ with $|g^G| = p^k$,
$$0 = \sum_{\chi\in\mathrm{Irr}(G)} \chi(1)\chi(g) = 1 + \sum_{\chi \ne 1_G} \chi(1)\chi(g),$$
and the vanishing lemma forces $p \mid \chi(1)$ for every non-trivial $\chi$ with $\chi(g)\ne 0$, giving $-1/p$ as an algebraic integer — contradiction.

**Derivation of the theorem.** Take $G$ minimal simple non-abelian of order $p^aq^b$ with $b \ge 1$. Let $Q \in \mathrm{Syl}_q(G)$ and pick $1 \ne z \in Z(Q)$. Then $Q \le C_G(z)$, so $|z^G| = [G : C_G(z)] = p^k$. Prime-power class size in a simple group is impossible, so $G$ is not simple; induction on $|G|$ finishes.

**Local-analytic alternative.** The character-free proofs run through **signalizer/fusion machinery**: Glauberman's $ZJ$-theorem — for $p$ odd and $G$ $p$-stable with $O_{p'}(G)=1$, the subgroup $Z(J(P))$ is normal in $G$ — plus Thompson factorisation and Bender's method of maximal subgroups containing a fixed $p$-subgroup.

## 3. History & State of the Art (SOTA)

- **1896–1901, Frobenius:** creation of character theory of finite groups; the arithmetic of $\omega_\chi$.
- **1904, Burnside:** *On groups of order $p^\alpha q^\beta$*, Proc. London Math. Soc. (2) 1, 388–392. The proof is the first major application of representation theory to abstract group theory, and remained for decades the canonical demonstration that characters prove theorems characters do not mention.
- **1911, Burnside** (2nd edition of *Theory of Groups of Finite Order*) explicitly asks for a proof "not involving the theory of group-characteristics".
- **1963, Feit–Thompson:** odd order theorem — every group of odd order is solvable — the far-reaching descendant; 255 pages of local analysis.
- **1968, Glauberman:** the $ZJ$-theorem supplies the missing normal-subgroup criterion for odd primes.
- **1970, Goldschmidt:** character-free proof when $p, q$ are both odd (3 pages).
- **1972, Bender:** a uniform group-theoretic proof covering all cases, using his maximal-subgroup method.
- **1973, Matsuyama:** short character-free treatment of the remaining case $|G| = 2^a q^b$.
- **2007, Gonthier–Mahboubi–Rideau–Tassi–Théry:** full Coq/SSReflect formalisation of Burnside's $p^aq^b$ theorem, the pilot project for the 2012 machine-checked Feit–Thompson proof.
- **Post-CFSG:** the theorem is a trivial corollary of the classification (inspect the simple-group order list), but this is regarded as no proof at all in the intended sense.

## 4. Partial Results / Verified Cases

| Case | Status | Method |
|---|---|---|
| $b = 0$ (order $p^a$) | Proved 1870s | $p$-groups are nilpotent; non-trivial centre |
| $a = b = 1$, order $pq$ | Elementary | Sylow counting alone |
| $|G| = p^a q$ | Elementary | Sylow + induction, no characters |
| $p, q$ both odd | Goldschmidt 1970 | $ZJ$-theorem, $p$-stability |
| $p = 2$, i.e. $|G| = 2^a q^b$ | Matsuyama 1973 | Fusion + Thompson factorisation |
| All $p,q$, uniform | Bender 1972 | Maximal-subgroup / signalizer method |
| $|G|$ odd, any number of primes | Feit–Thompson 1963 | 255-page local analysis |
| Three primes | **False** | $|A_5| = 60 = 2^2\cdot3\cdot5$, $|PSL(2,7)|=168=2^3\cdot3\cdot7$ |
| $G = AB$, $A,B$ nilpotent | Kegel 1961 / Wielandt 1958 | $G$ solvable — strict generalisation |
| Machine-checked | Coq, 2007 | ~13,000 lines SSReflect |

Every group of order $p^aq^b$ with $p^aq^b < 2000$ has been enumerated and confirmed solvable in the GAP/Magma small-groups libraries; this is a consistency check, not evidence, since the theorem is proved.

## 5. Principal Obstacles

The residual difficulties are about *proof economy*, not truth.

- **The algebraic-number-theory dependency.** The character proof needs: $\omega_\chi(\widehat K)$ is an algebraic integer; $|\chi(g)| \le \chi(1)$ with equality only on $Z(\chi)$; and a Galois-conjugation argument on $\chi(g)/\chi(1)$. Attempts to replace this by a purely rational argument fail because the bound $|\chi(g)/\chi(1)| \le 1$ is genuinely archimedean — no congruence or counting substitute is known that separates "$0$" from "root of unity".
- **$p = 2$ breaks $p$-stability.** Glauberman's $ZJ$-theorem requires $p$ odd (or $SL_2(p)$-free sections); $SL_2(2) \cong S_3$ obstructs. This is exactly why Goldschmidt's 1970 argument stops short of $2^aq^b$ and why a separate 2-local treatment (Matsuyama, Bender) was needed. The same $p=2$ asymmetry is the reason Feit–Thompson only handles odd order.
- **No local characterisation of "two primes".** Sylow theory sees one prime at a time. The hypothesis $|\pi(G)| = 2$ is a *global* arithmetic constraint; converting it into a local statement about $p$-local subgroups requires the full fusion apparatus, and there is no known shortcut.
- **Counting arguments are provably insufficient.** Any proof using only Sylow counts and orbit arithmetic must also apply to $|A_5|$-like configurations; $n_5 = 6$, $n_3 = 10$, $n_2 = 5$ in $A_5$ show that Sylow numerology alone never rules out simplicity, so some non-counting input (characters or fusion) is necessary.

## 6. The Gap

Proven: solvability for all $p^aq^b$, by three independent routes (characters; $ZJ$/local analysis; CFSG). Machine-checked in Coq. **No gap in the theorem itself.**

Open residue:

1. **Minimal-prerequisite proof.** Is there a proof using neither $\mathbb{C}$-characters nor Glauberman/Thompson factorisation — e.g. purely modular or purely combinatorial? No obstruction theorem forbids it; no candidate exists.
2. **Sharp derived length.** The best general bounds on $\mathrm{dl}(G)$ for $|G| = p^aq^b$ come from Hall–Higman $p$-length estimates and are far from the extremal examples known. A sharp function $\mathrm{dl}(G) \le f(a,b)$ is not known.
3. **Kegel–Wielandt frontier.** $G = AB$ with $A, B$ nilpotent implies $G$ solvable (Kegel 1961). Whether $A, B$ *supersolvable* forces $G$ solvable is a longstanding open problem in factorised groups.

## 7. Current Research (as of June 2026)

- **Formal mathematics.** The Mathematical Components (Inria/MSR) Coq library remains the reference formalisation. Porting Burnside's theorem and its lemmas to Lean 4's Mathlib is an active community effort; the character-theoretic ingredients (algebraic integrality of $\omega_\chi$, second orthogonality) are in Mathlib, and the assembly into the $p^aq^b$ statement has been reported as complete *(frontier — verify)*.
- **Factorised groups.** Groups in Spain (Universitat de València — Ballester-Bolinches, Pérez-Ramos and collaborators) continue work on products of nilpotent and supersolvable groups, extending the Kegel–Wielandt line to saturated formations and to totally permutable products.
- **Character-degree arithmetic.** The "Burnside-type" programme — deducing structure from $\gcd$ conditions between $\chi(1)$ and class sizes — is pursued in the character-theory community (Navarro, Tiep, and coauthors), including $\pi$-separability criteria that specialise to Burnside's lemma.
- **Second-generation classification.** The Gorenstein–Lyons–Solomon volumes (AMS Surveys and Monographs 40.x) rewrite the local analysis in which Bender's method sits; each new volume tightens the exposition of the tools used in the character-free $p^aq^b$ proof.

## 8. Future Work

- Produce a self-contained modern exposition of the Bender proof at textbook length, isolating exactly which fusion results are needed — the current shortest treatments still cite $ZJ$ and Thompson factorisation as black boxes.
- Determine the exact maximum derived length of a group of order $p^aq^b$ as a function of $a$ and $b$, with matching constructions.
- Settle whether a product of two supersolvable subgroups is solvable.
- Complete and certify a Lean 4 formalisation, then reuse its character-theory infrastructure toward a formal Feit–Thompson in Lean.
- Investigate whether the vanishing lemma admits a $p$-adic or modular proof avoiding the archimedean bound.

## 9. Key References

- **[Foundational]** W. Burnside. *On groups of order $p^\alpha q^\beta$.* Proceedings of the London Mathematical Society, ser. 2, vol. 1, 388–392, 1904.
- **[Foundational]** W. Burnside. *Theory of Groups of Finite Order.* 2nd edition, Cambridge University Press, 1911 (Dover reprint 1955).
- **[Character-free]** D. M. Goldschmidt. *A group theoretic proof of the $p^aq^b$ theorem for odd primes.* Mathematische Zeitschrift 113, 373–375, 1970.
- **[Character-free]** H. Bender. *A group theoretic proof of Burnside's $p^aq^b$-theorem.* Mathematische Zeitschrift 126, 327–338, 1972.
- **[Character-free]** H. Matsuyama. *Solvability of groups of order $2^aq^b$.* Osaka Journal of Mathematics 10, 375–378, 1973.
- **[Tool]** G. Glauberman. *A characteristic subgroup of a $p$-stable group.* Canadian Journal of Mathematics 20, 1101–1135, 1968. [DOI](https://doi.org/10.4153/cjm-1968-107-2)
- **[Textbook]** I. M. Isaacs. *Character Theory of Finite Groups.* Academic Press, 1976 (Dover reprint 1994). Chapter 3.
- **[Textbook]** D. J. S. Robinson. *A Course in the Theory of Groups.* 2nd edition, Springer GTM 80, 1996.
- **[Survey]** D. Gorenstein. *Finite Groups.* 2nd edition, Chelsea, 1980.
- **[Related]** W. Feit and J. G. Thompson. *Solvability of groups of odd order.* Pacific Journal of Mathematics 13, 775–1029, 1963.
- **[Generalisation]** O. H. Kegel. *Produkte nilpotenter Gruppen.* Archiv der Mathematik 12, 90–93, 1961. [DOI](https://doi.org/10.1007/bf01650529)
- **[Generalisation]** H. Wielandt. *Über Produkte von nilpotenten Gruppen.* Illinois Journal of Mathematics 2, 611–618, 1958. [DOI](https://doi.org/10.1215/ijm/1255448333)
- **[Formalisation]** G. Gonthier, A. Mahboubi, L. Rideau, E. Tassi, L. Théry. *A modular formalisation of finite group theory.* Theorem Proving in Higher Order Logics (TPHOLs 2007), LNCS 4732, Springer, 86–101.
- **[Historical]** C. W. Curtis. *Pioneers of Representation Theory: Frobenius, Burnside, Schur, and Brauer.* American Mathematical Society, 1999. [DOI](https://doi.org/10.1090/hmath/015)

## 10. Worked Example / Concrete Special Case

**Claim.** Every group of order $72 = 2^3 \cdot 3^2$ is solvable — shown two ways.

**(a) Elementary Sylow route.** Let $|G| = 72$ and $n_3 = |\mathrm{Syl}_3(G)|$. By Sylow, $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 8$, so $n_3 \in \{1, 4\}$.

- If $n_3 = 1$: the Sylow 3-subgroup $P$ (order 9) is normal. $P$ is abelian (order $p^2$), and $G/P$ has order 8, a 2-group, hence nilpotent. Solvable extension of solvable ⇒ $G$ solvable.
- If $n_3 = 4$: conjugation on $\mathrm{Syl}_3(G)$ gives $\varphi : G \to S_4$. Since $|S_4| = 24 < 72$, $K = \ker\varphi \ne 1$; and $\varphi$ is transitive so $|\mathrm{im}\,\varphi| \ge 4$, giving $|K| \le 18$. Then $|K| \ge 3$ and $|G/K| \le 24$; both $K$ and $G/K$ have order of the form $2^i3^j$ strictly less than 72, so induction applies and $G$ is solvable.

Concretely $72 = |C_3 \times SL(2,3)|$ and there are 50 groups of order 72; all are solvable, and none is simple.

**(b) The character argument, illustrated.** Suppose for contradiction $G$ is simple of order 72. Take $Q \in \mathrm{Syl}_3(G)$, $|Q| = 9$. A group of order $p^2$ has non-trivial centre, so pick $1 \ne z \in Z(Q)$. Then $Q \le C_G(z)$, so $9 \mid |C_G(z)|$ and
$$|z^G| = \frac{72}{|C_G(z)|} \in \{1, 2, 4, 8\} = \{2^k\}.$$
Since $G$ is simple non-abelian, $Z(G) = 1$, so $|z^G| = 2^k$ with $k \ge 1$.

Now apply the vanishing lemma. For $\chi \in \mathrm{Irr}(G)$ with $2 \nmid \chi(1)$, we get $\gcd(\chi(1), 2^k) = 1$, so $\chi(z) = 0$ or $|\chi(z)| = \chi(1)$; the latter would put $z$ in $Z(\chi)$, and since $\ker\chi \in \{1, G\}$ by simplicity, this forces $\chi = 1_G$. Column orthogonality at $z \ne 1$ gives
$$0 = \sum_{\chi} \chi(1)\chi(z) = 1 + \sum_{\substack{\chi \ne 1_G \\ 2 \mid \chi(1)}} \chi(1)\chi(z) = 1 + 2\alpha,$$
where $\alpha = \sum \tfrac{\chi(1)}{2}\chi(z)$ is an algebraic integer. Hence $\alpha = -1/2$, a rational number that is an algebraic integer without being a rational integer — contradiction. So no simple group of order 72 exists, and the induction of (a) delivers solvability.

The same two paragraphs, with $72$ replaced by $p^aq^b$ and "9" by $|Q| = q^b$, are the whole of Burnside's 1904 proof.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*