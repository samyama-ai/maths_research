---
id: 08-logic-set-theory/decidability-of-p-adic-theory
title: "Decidability of the Theory of the p-adic Numbers"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Decidability of the Theory of the p-adic Numbers

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/decidability-of-p-adic-theory` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Fix a prime $p$ and let $\mathbb{Q}_p$ be the field of $p$-adic numbers. The core question, posed in the wake of Tarski's decision procedure for $\mathbb{R}$, is:

> Is $\mathrm{Th}(\mathbb{Q}_p)$ — the set of first-order sentences in the language of rings $\mathcal{L}_{\mathrm{ring}} = \{+,\cdot,-,0,1\}$ true in $\mathbb{Q}_p$ — decidable?

**Answer (settled).** Yes. Ax–Kochen (1965–66) and independently Ershov (1965) proved decidability by a transfer/ultraproduct argument; Cohen (1969) gave a primitive recursive elimination procedure; Macintyre (1976) proved quantifier elimination after adding power predicates.

The problem is catalogued as `solved-recently` because the *core* statement is a theorem, while the surrounding programme remains open on four fronts, each of which is the live research object:

1. **Uniformity in $p$:** is there a single algorithm, primitive recursive in $p$, deciding $\mathrm{Th}(\mathbb{Q}_p)$ uniformly, with explicit bounds replacing the ineffective "for all $p > N(d)$" of Ax–Kochen?
2. **Complexity:** what is the exact complexity of $\mathrm{Th}(\mathbb{Q}_p)$ and of its existential fragment, with $p$ encoded in binary?
3. **Positive characteristic:** is $\mathrm{Th}(\mathbb{F}_p((t)))$ decidable? **Open.**
4. **Enrichments:** decidability for $\mathbb{Q}_p^{\mathrm{ab}}$, for adele rings, and for analytic expansions.

A complete resolution of the surviving programme means: an explicit uniform decision procedure with elementary-recursive bounds, tight complexity classification, and a decision on $\mathbb{F}_p((t))$.

## 2. Mathematical Foundations

**The field.** $\mathbb{Q}_p$ is the completion of $\mathbb{Q}$ under $|x|_p = p^{-v_p(x)}$, where $v_p$ is the $p$-adic valuation. Its valuation ring is
$$\mathbb{Z}_p = \{x \in \mathbb{Q}_p : v(x) \ge 0\}, \qquad \mathfrak{m} = p\mathbb{Z}_p, \qquad \mathbb{Z}_p/\mathfrak{m} \cong \mathbb{F}_p .$$
The value group is $(\mathbb{Z},+,<)$; the field is henselian, complete, discretely valued, of characteristic $0$ with residue characteristic $p$.

**Definability of the valuation.** For $p \ne 2$, $\mathbb{Z}_p$ is $\mathcal{L}_{\mathrm{ring}}$-definable:
$$x \in \mathbb{Z}_p \iff \exists y\; \big(y^2 = 1 + p x^2\big)\quad (p>2),$$
and $x \in \mathbb{Z}_2 \iff \exists y\,(y^2 = 1 + 8x^2)$ for $p=2$. Hence valuation-language results transfer to the pure ring language.

**Macintyre's language.** Let $\mathcal{L}_{\mathrm{Mac}} = \mathcal{L}_{\mathrm{ring}} \cup \{P_n\}_{n\ge2}$ with
$$P_n(x) \iff \exists y\,(y \ne 0 \wedge y^n = x).$$

> **Theorem (Macintyre 1976).** $\mathrm{Th}(\mathbb{Q}_p)$ admits elimination of quantifiers in $\mathcal{L}_{\mathrm{Mac}}$.

Consequently every definable subset of $\mathbb{Q}_p^m$ is a finite Boolean combination of sets $\{ \bar x : f(\bar x) = 0\}$ and $\{\bar x : P_n(g(\bar x))\}$ with $f,g \in \mathbb{Z}[\bar X]$ — the *$p$-adic semialgebraic* sets.

**Ax–Kochen–Ershov transfer.** For any non-principal ultrafilter $\mathcal{U}$ on the primes,
$$\prod_{p} \mathbb{Q}_p \big/ \mathcal{U} \;\equiv\; \prod_{p} \mathbb{F}_p((t)) \big/ \mathcal{U},$$
and more generally, for henselian valued fields of residue characteristic $0$,
$$K \equiv L \iff \big(\, k_K \equiv k_L \ \text{and}\ \Gamma_K \equiv \Gamma_L \,\big).$$
Since $\mathrm{Th}(\mathbb{F}_p)$ (finite fields, uniformly, by Ax) and Presburger arithmetic $\mathrm{Th}(\mathbb{Z},+,<)$ are decidable, so is $\mathrm{Th}(\mathbb{Q}_p)$.

**Cell decomposition (Denef 1986).** Every $p$-adic semialgebraic $X \subseteq \mathbb{Q}_p^{m+1}$ decomposes into finitely many cells
$$C = \{(\bar x, y) : \bar x \in D,\; v(a(\bar x)) \,\square_1\, v(y - c(\bar x)) \,\square_2\, v(b(\bar x)),\; y - c(\bar x) \in \lambda\, (\mathbb{Q}_p^\times)^n \},$$
with $a,b,c$ semialgebraic functions and $\square_i \in \{<,\le,\text{no condition}\}$. This yields the rationality of Igusa's local zeta function
$$Z(s) = \int_{\mathbb{Z}_p^m} |f(x)|_p^{\,s}\, |dx| \in \mathbb{Q}(p^{-s}).$$

## 3. History & State of the Art (SOTA)

- **1930.** Tarski: $\mathrm{Th}(\mathbb{R},+,\cdot)$ is decidable, admits QE. The $p$-adic analogue becomes the natural target.
- **1936.** Artin conjectures that every homogeneous form of degree $d$ in $> d^2$ variables over $\mathbb{Q}_p$ has a nontrivial zero ($\mathbb{Q}_p$ is $C_2$).
- **1965–66.** Ax & Kochen, *Diophantine problems over local fields I–III*, prove: for each $d$ there is a finite exceptional set $S(d)$ of primes outside which Artin's conjecture holds; the method gives decidability of $\mathrm{Th}(\mathbb{Q}_p)$. Ershov proves the same independently in 1965.
- **1966.** Terjanian: a quartic form in $18 > 16$ variables over $\mathbb{Q}_2$ with only the trivial zero — Artin's conjecture is false, but the transfer theorem stands.
- **1969.** Cohen gives a direct, primitive recursive elimination for both $\mathbb{R}$ and $\mathbb{Q}_p$, removing ultraproducts.
- **1976.** Macintyre: QE in $\mathcal{L}_{\mathrm{Mac}}$.
- **1978.** S. S. Brown: explicit (tower-type) bounds on $S(d)$.
- **1984–88.** Denef: cell decomposition and rationality of Poincaré series; Denef–van den Dries: $p$-adic subanalytic sets, QE for the analytic expansion $\mathbb{Q}_p^{\mathrm{an}}$.
- **1981.** Arkhipov–Karatsuba: for every $p$ there exist degrees $d$ with counterexamples to $C_2$, so the exceptional set is genuinely degree-dependent.
- **1989–2008.** Pas's angular-component QE; Denef–Loeser motivic integration; Cluckers–Loeser's uniform $p$-adic framework give uniformity *in the limit* $p \to \infty$.
- **2016–2019.** Anscombe–Fehm: decidability of the existential theory of equicharacteristic henselian valued fields, including $\mathbb{F}_q((t))$ in the valued-field language. Guépin–Haase–Worrell: sharp complexity for linear/existential fragments over $\mathbb{Q}_p$.

## 4. Partial Results / Verified Cases

| Object | Status |
|---|---|
| $\mathrm{Th}(\mathbb{Q}_p)$, each fixed $p$, $\mathcal{L}_{\mathrm{ring}}$ | **Decidable**, primitive recursive (Cohen 1969) |
| Finite extensions $K/\mathbb{Q}_p$, $[K:\mathbb{Q}_p]<\infty$ | **Decidable**; QE in $\mathcal{L}_{\mathrm{Mac}}$ with $n$-th power predicates and finitely many field constants (Prestel–Roquette 1984) |
| $\mathbb{Q}_p^{\mathrm{unr}}$, $\widehat{\mathbb{Q}_p^{\mathrm{unr}}}$ | **Decidable** (AKE, residue field $\overline{\mathbb{F}_p}$ decidable) |
| $\mathbb{C}_p$, algebraically closed valued fields | **Decidable** (Robinson 1956, ACVF has QE) |
| Analytic expansion $\mathbb{Q}_p^{\mathrm{an}}$ (restricted power series) | **Decidable**; QE and cell decomposition (Denef–van den Dries 1988; Cluckers 2004) |
| Hilbert's 10th over $\mathbb{Q}_p$, $\mathbb{Z}_p$ | **Decidable** (special case of the above) |
| Artin's conjecture, $d$ fixed | Holds for all $p > N(d)$; verified unconditionally for $d=2$ (all $p$), $d=3$ (Demyanov/Lewis, all $p$) |
| Presburger fragment (value group only) | Decidable; complete complexity known — $\mathrm{2\text{-}EXP}$-style alternating bounds (Fischer–Rabin lower bound $2^{2^{cn}}$) |
| Linear $\exists$-fragment over $\mathbb{Q}_p$ | **NP-complete** for $p$ in unary (Guépin–Haase–Worrell 2019) |
| $\mathrm{Th}(\mathbb{F}_p((t)))$ | **Open** |
| $\mathbb{Q}_p^{\mathrm{ab}}$, adele ring of $\mathbb{Q}$ | Adeles decidable (Derakhshan–Macintyre); $\mathbb{Q}_p^{\mathrm{ab}}$ partially resolved |

## 5. Principal Obstacles

- **Ultraproducts are non-effective.** The AKE proof shows a sentence $\sigma$ true in $\mathbb{Q}_p$ for almost all $p$ but supplies no computable bound on "almost all". Brown's explicit bounds are tower-of-exponentials in $d$, and no elementary-recursive bound is known. This is the central obstruction to *uniform* effectivity.
- **Ramification breaks residue-lifting.** In residue characteristic $p$, the Teichmüller lift is not a ring homomorphism modulo $p^2$, so the clean $K \leftrightarrow (k,\Gamma)$ decomposition of the AKE theorem holds only in residue characteristic $0$ or in the limit. Wild ramification defeats term-by-term coefficient induction.
- **Defect in positive characteristic.** For $\mathbb{F}_p((t))$ the immediate extensions can carry nontrivial *defect* $d(L/K) > 1$ — the fundamental equality $[L:K] = e \cdot f$ fails — and Artin–Schreier extensions $x^p - x = a$ have no characteristic-$0$ analogue. Every known QE strategy (Cohen's, Macintyre's, Pas's) presupposes characteristic $0$ at the ambient-field level.
- **Complexity floor.** $\mathrm{Th}(\mathbb{Q}_p)$ interprets Presburger arithmetic, inheriting its $2^{2^{\Omega(n)}}$ nondeterministic lower bound (Fischer–Rabin 1974); the power predicates $P_n$ multiply the cell count in each elimination round, so known upper bounds sit far above.
- **Non-uniformity of $n$-th powers.** The index $[\mathbb{Q}_p^\times : (\mathbb{Q}_p^\times)^n] = n \cdot |n|_p^{-1} \cdot |\mu_n(\mathbb{Q}_p)|$ jumps when $p \mid n$, so the coset structure driving QE depends discontinuously on $p$.

## 6. The Gap

Proven: for each fixed $p$, a primitive recursive algorithm decides $\mathrm{Th}(\mathbb{Q}_p)$, and definable sets are exactly the $p$-adic semialgebraic sets.

Not proven, and this is the boundary:

- **(a) Effective uniformity.** Given $\sigma$, compute an explicit, elementary-recursive $N(\sigma)$ such that $\mathbb{Q}_p \models \sigma$ for all $p > N(\sigma)$ iff $\mathbb{F}_p((t)) \models \sigma$ for all $p > N(\sigma)$. Motivic integration gives uniformity *statements* but not effective bounds.
- **(b) Characteristic $p$.** Cross the defect barrier: produce either a QE for $\mathbb{F}_p((t))$ in some enriched language, or an interpretation of an undecidable theory (e.g. via a definable copy of $(\mathbb{N},+,\cdot)$ using $t$-adic Frobenius twists). Neither direction has yielded.
- **(c) Complexity.** Close the gap between the $2^{2^{\Omega(n)}}$ lower bound and the non-elementary upper bounds arising from iterated Macintyre elimination.

## 7. Current Research (as of June 2026)

- **Uniform $p$-adic model theory.** Cluckers, Halupczok, Rideau-Kikuchi and collaborators (Leuven, Bochum, Paris/IMJ-PRG) push transfer principles for motivic/uniform-in-$p$ integrals to all $p$, including small residue characteristic and ramified extensions, with applications to orbital integrals in the Langlands programme.
- **Existential/complexity frontier.** Haase, Worrell, Guépin (UCL, Oxford) and successors classify fragments: NP-completeness for the linear existential theory, and ongoing work on the full $\exists\mathrm{Th}(\mathbb{Q}_p)$ with $p$ in binary. *(frontier — verify)* Claims of an EXPTIME upper bound for $\exists\mathrm{Th}(\mathbb{Q}_p)$ circulate but should be checked against the published version.
- **Positive characteristic.** Anscombe, Fehm, Kuhlmann (Manchester/Dresden/Konstanz/Szczecin) work on defect classification (independent vs. dependent defect) as the route to $\mathrm{Th}(\mathbb{F}_p((t)))$; Denef–Schoutens' conditional decidability of $\exists\mathrm{Th}(\mathbb{F}_p[[t]])$ modulo resolution of singularities in characteristic $p$ remains a live conditional.
- **Adelic and global objects.** Derakhshan–Macintyre's model theory of adeles (decidability of $\mathrm{Th}(\mathbb{A}_{\mathbb{Q}})$ via Feferman–Vaught plus uniform $p$-adic QE) is being extended to adelic groups and to $\mathbb{Q}_p^{\mathrm{ab}}$.

## 8. Future Work

- Replace Brown's tower bounds on $N(d)$ with elementary-recursive bounds, ideally by an effective coefficient-wise elimination avoiding ultraproducts entirely.
- Develop a QE for henselian valued fields *with* defect, e.g. by adding a defect-measuring predicate or working in the language of *tame* fields where Kuhlmann proved an AKE principle.
- Sharpen complexity: identify the natural complete problem for $\mathrm{Th}(\mathbb{Q}_p)$ in the alternating time-space hierarchy; determine whether the $P_n$ predicates cost more than a polynomial factor.
- Extend Denef–van den Dries subanalytic QE to families varying with $p$, closing the analytic case uniformly.
- Test undecidability strategies for $\mathbb{F}_p((t))$: attempt to define $\mathbb{F}_p[t]$ or $\mathbb{Z}$ inside $\mathbb{F}_p((t))$ in the ring language.

## 9. Key References

- **[Foundational]** J. Ax and S. Kochen. *Diophantine Problems Over Local Fields I, II.* American Journal of Mathematics 87 (1965), 605–630 and 631–648; *III.* Annals of Mathematics 83 (1966), 437–456.
- **[Foundational]** Yu. L. Ershov. *On the elementary theory of maximal normed fields.* Doklady Akademii Nauk SSSR 165 (1965), 21–23.
- **[Foundational]** P. J. Cohen. *Decision procedures for real and p-adic fields.* Communications on Pure and Applied Mathematics 22 (1969), 131–151.
- **[Foundational]** A. Macintyre. *On definable subsets of p-adic fields.* Journal of Symbolic Logic 41 (1976), 605–610.
- **[Foundational]** J. Denef. *The rationality of the Poincaré series associated to the p-adic points on a variety.* Inventiones Mathematicae 77 (1984), 1–23.
- **[Foundational]** J. Denef. *p-adic semi-algebraic sets and cell decomposition.* Journal für die reine und angewandte Mathematik 369 (1986), 154–166.
- **[Foundational]** J. Denef and L. van den Dries. *p-adic and real subanalytic sets.* Annals of Mathematics 128 (1988), 79–138.
- **[Book]** A. Prestel and P. Roquette. *Formally p-adic Fields.* Lecture Notes in Mathematics 1050, Springer, 1984.
- **[Book]** L. van den Dries. *Lectures on the Model Theory of Valued Fields.* In: Model Theory in Algebra, Analysis and Arithmetic, Lecture Notes in Mathematics 2111, Springer, 2014.
- **[Bounds]** S. S. Brown. *Bounds on Transfer Principles for Algebraically Closed and Complete Discretely Valued Fields.* Memoirs of the AMS 204, 1978.
- **[Counterexample]** G. Terjanian. *Un contre-exemple à une conjecture d'Artin.* C. R. Acad. Sci. Paris Sér. A 262 (1966), 612.
- **[SOTA]** R. Cluckers. *Analytic p-adic cell decomposition and integrals.* Transactions of the AMS 356 (2004), 1489–1499.
- **[SOTA]** R. Cluckers and F. Loeser. *Constructible motivic functions and motivic integration.* Inventiones Mathematicae 173 (2008), 23–121.
- **[SOTA]** S. Anscombe and A. Fehm. *The existential theory of equicharacteristic henselian valued fields.* Algebra & Number Theory 10 (2016), 665–683.
- **[SOTA]** F. Guépin, C. Haase and J. Worrell. *On the Existential Theories of Büchi Arithmetic and Linear p-adic Fields.* Proceedings of LICS 2019, IEEE.
- **[SOTA]** J. Derakhshan and A. Macintyre. *Model theory of adeles I.* Annals of Pure and Applied Logic 173 (2022), 103074.
- **[Survey]** J. Denef. *Arithmetic and geometric applications of quantifier elimination for valued fields.* In: Model Theory, Algebra, and Geometry, MSRI Publications 39, Cambridge University Press, 2000, 173–198.

## 10. Worked Example / Concrete Special Case

**Goal.** Show by hand how QE decides a sentence, using $P_2$.

Take $\sigma := \forall x\,\big(x \ne 0 \rightarrow \exists y\,(y^2 = x \;\vee\; y^2 = px \;\vee\; y^2 = ux \;\vee\; y^2 = pux)\big)$ for $p$ odd, $u$ a fixed non-residue unit. Macintyre elimination replaces each $\exists y\,(y^2 = z)$ by $P_2(z)$, so
$$\sigma \equiv \forall x\,\big(x \ne 0 \rightarrow P_2(x) \vee P_2(px) \vee P_2(ux) \vee P_2(pux)\big).$$
This is exactly the assertion $[\mathbb{Q}_p^\times : (\mathbb{Q}_p^\times)^2] = 4$ with coset representatives $\{1,u,p,pu\}$ — true for $p$ odd, and the algorithm confirms it from the residue-field computation $[\mathbb{F}_p^\times : (\mathbb{F}_p^\times)^2] = 2$ together with $v(x) \bmod 2 \in \{0,1\}$ in the value group. For $p = 2$ the same procedure returns index $8$, representatives $\{\pm1,\pm5,\pm2,\pm10\}$, so $\sigma$ is **false** in $\mathbb{Q}_2$.

**Deciding a single instance.** Is $6$ a square in $\mathbb{Q}_5$? Here $v_5(6)=0$, and $6 \equiv 1 \pmod 5$. Since $1$ is a square in $\mathbb{F}_5$ and $5 \ne 2$, Hensel's lemma applied to $f(y)=y^2-6$ at $y_0=1$ — $|f(1)|_5 = |{-5}|_5 = 1/5 < 1 = |f'(1)|_5^2$ — lifts to a root. Explicitly $y = 1 + 2\cdot5 + 1\cdot 5^2 + \dots$ with $y^2 = 6$. So $\mathbb{Q}_5 \models P_2(6)$.

By contrast $\mathbb{Q}_5 \models \neg P_2(10)$: $v_5(10) = 1$ is odd, so $10$ lies in the coset $5 \cdot (\mathbb{Q}_5^\times)^2$-class, not the trivial one.

**The transfer phenomenon in miniature.** Terjanian's form
$$F(x_1,\dots,x_{18}) = n(x_1,x_2,x_3) + n(x_4,x_5,x_6) + n(x_7,x_8,x_9) + 4\big[n(x_{10},\dots) + n(\dots) + n(\dots)\big],$$
where $n(x,y,z)=x^2y^2+y^2z^2+z^2x^2-x^2y z-xy^2z-xyz^2$ is a quartic with $n(x,y,z)\equiv 0 \bmod 4$ whenever $x,y,z$ are not all odd, has only the trivial zero over $\mathbb{Q}_2$ — degree $4$, $18 > 4^2 = 16$ variables. Yet Ax–Kochen guarantees that the sentence "every quartic form in $18$ variables has a nontrivial zero" is true in $\mathbb{Q}_p$ for all sufficiently large $p$. The decision procedure settles each $p$ individually; what it does not deliver is the threshold. That gap is Section 6(a).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*