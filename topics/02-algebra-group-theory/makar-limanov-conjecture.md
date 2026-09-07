---
id: 02-algebra-group-theory/makar-limanov-conjecture
title: "Makar-Limanov Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Makar-Limanov Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/makar-limanov-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $D$ be a division ring with center $k$, and suppose $D$ is finitely generated as a division algebra over $k$ (i.e. $D$ is the smallest division subring containing $k$ and a finite set).

**Conjecture (Makar-Limanov).** If $\dim_k D = \infty$, then $D$ contains a free $k$-subalgebra $k\langle a,b\rangle$ of rank $2$: two elements $a,b \in D$ such that the $2^n$ words of length $n$ in $a,b$ are $k$-linearly independent for every $n$.

Equivalently: a finitely generated division algebra either satisfies a polynomial identity in the strong sense of being finite-dimensional over its center, or it is as far from commutative as possible — it contains a copy of the free associative algebra.

A proof requires exhibiting (or proving the existence of) such a pair in every infinite-dimensional finitely generated $D$. A disproof requires one explicit $D$, infinite-dimensional over $k$ and finitely generated, in which every $2$-generated subalgebra satisfies a nontrivial relation over $k$. Two standard strengthenings are also open: that $D$ contains a free **group** algebra $k[F_2]$, and (Lichtman) that $D^{\times}$ contains a free subgroup of rank $2$.

The finite-generation hypothesis is essential: without it there are locally PI division rings that are infinite-dimensional over their centers. The conjecture is usually stated for $\operatorname{char} k = 0$, or with $k$ not algebraic over a finite field; the case $k \subseteq \overline{\mathbb{F}_p}$ is a genuinely separate and largely untouched regime.

## 2. Mathematical Foundations

**Free algebra.** For a field $k$, $k\langle a,b \rangle$ is the monoid algebra on the free monoid $\{a,b\}^{*}$, with $k$-basis all words. A pair $(a,b)$ in a $k$-algebra $A$ is *free* if the induced map $k\langle X,Y\rangle \to A$, $X \mapsto a$, $Y\mapsto b$, is injective.

**Ore localization.** A domain $R$ satisfying the (left and right) Ore condition — $aR \cap bR \ne 0$ for all nonzero $a,b$ — embeds in a division ring of fractions $Q(R) = \operatorname{Frac}(R)$, unique up to isomorphism. Noetherian domains are Ore, so $\operatorname{Frac}$ exists for enveloping algebras, group algebras of polycyclic-by-finite groups, and Ore extensions.

**Ore extension.** For a field $K$, an automorphism $\sigma$ and a $\sigma$-derivation $\delta$, the ring $K[x;\sigma,\delta]$ has multiplication
$$x\,\alpha \;=\; \sigma(\alpha)\,x + \delta(\alpha), \qquad \alpha \in K .$$
Two model cases:
- **Weyl algebra** $A_1(k) = k\langle x,y\rangle/(yx-xy-1) = k[x][y;\mathrm{id},\tfrac{d}{dx}]$, with Weyl field $D_1 = \operatorname{Frac} A_1(k)$.
- **Quantum plane** $k_q[x,y]$, $yx = qxy$, with $\operatorname{Frac} k_q[x,y] = \operatorname{Frac}\bigl(k(y)[x;\sigma]\bigr)$, $\sigma(y)=qy$.

**Gelfand–Kirillov transcendence degree.** For a $k$-algebra $A$,
$$\operatorname{Tdeg}(A) \;=\; \sup_V \inf_{b} \operatorname{GKdim}\, k[bV],$$
the supremum over finite-dimensional subspaces $V \ni 1$ and infimum over nonzero $b$ in the centralizer-type denominators; it is the standard birational size invariant for division rings, with $\operatorname{Tdeg}(D_1)=2$ and $\operatorname{Tdeg} D = 0$ iff $\dim_k D<\infty$ (Gelfand–Kirillov; Zhang).

**Mal'cev–Neumann series.** If $G$ is an ordered group and $K$ a division ring with a $G$-action, the series ring $K((G))$ of well-ordered-support formal sums is a division ring. Embedding $D \hookrightarrow K((G))$ gives a valuation $v: D^\times \to G$ with $v(uv)=v(u)+v(v)$ and $v(u+v)\ge \min$, the main engine for freeness proofs: if leading terms of distinct words cannot cancel, the words are independent.

**Standard obstruction.** If $D$ satisfies a polynomial identity, then by Kaplansky's theorem $\dim_k D = m^2 < \infty$; PI division rings contain no free subalgebras. So the conjecture asserts that this is the *only* obstruction among finitely generated $D$.

## 3. History & State of the Art (SOTA)

- **1983.** Leonid Makar-Limanov proved that $D_1 = \operatorname{Frac} A_1(k)$, $\operatorname{char} k = 0$, contains a free $k$-subalgebra of rank $2$ (*Comm. Algebra* 11). This was a surprise: $A_1$ itself has GK-dimension $2$ and is Noetherian of Krull dimension $1$, so the freeness lives entirely in the denominators.
- **1984.** Makar-Limanov formulated the general conjecture in "On free subobjects of skew fields" and showed the free group $F_2$ embeds in $D_1^{\times}$.
- **1986.** Lorenz proved free subalgebras exist in $\operatorname{Frac} k[\Gamma]$ for $\Gamma$ nonabelian torsion-free nilpotent (and more generally for many polycyclic $\Gamma$).
- **1991.** Makar-Limanov and Malcolmson: the enveloping field $\operatorname{Frac} U(\mathfrak g)$ of any finite-dimensional non-abelian Lie algebra in characteristic $0$ contains a free subalgebra.
- **1996.** Chiba gave valuation-theoretic criteria producing free subalgebras and free subsemigroups in division rings with suitable valuations.
- **2009–2014.** Bell and Bell–Rogalski converted the problem into a dynamical statement about orbits of an automorphism $\sigma$ on a variety and settled the $\operatorname{Tdeg}=2$ case over uncountable fields.

The state of the art is: **the conjecture is a theorem for essentially all division rings that arise as fraction fields of familiar Noetherian domains of small size, and open in general.** No counterexample is known, and no candidate counterexample is widely believed in.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $D_1 = \operatorname{Frac} A_1(k)$, $\operatorname{char} k=0$ | free subalgebra of rank $2$; also $F_2 \le D_1^\times$ | Makar-Limanov 1983, 1984 |
| $\operatorname{Frac} U(\mathfrak g)$, $\mathfrak g$ finite-dim. non-abelian, $\operatorname{char}0$ | free subalgebra | Makar-Limanov–Malcolmson 1991 |
| $\operatorname{Frac} k[\Gamma]$, $\Gamma$ torsion-free nilpotent non-abelian | free subalgebra | Lorenz 1986 |
| $\operatorname{Frac}(K[x;\sigma,\delta])$, $K$ a field, $\sigma$ of infinite order, base field not algebraic over $\mathbb{F}_p$ | free subalgebra of rank $2$ | Bell–Rogalski, *Algebra & Number Theory* 6 (2012) |
| $D$ finitely generated, $\operatorname{Tdeg} D = 2$, center $k$ **uncountable** | conjecture true | Bell–Rogalski, *Math. Z.* 277 (2014) |
| Quantum plane, quantum torus, quantum Weyl algebra, $\operatorname{Frac}$ of $q$-deformations with $q$ not a root of unity | free subalgebra (special case of the Ore-extension theorem) | Bell–Rogalski 2012 |
| Mal'cev–Neumann fields $k((G))$, $G$ non-abelian orderable | free group algebra $k[F_2]$ | Sánchez; Gonçalves–Sánchez |
| $D$ with a valuation whose residue division ring is noncommutative or whose value group is non-abelian | free subsemigroup / subalgebra | Chiba 1996 |

Unresolved regimes: $\operatorname{Tdeg} D = 2$ over **countable** fields (e.g. $k=\mathbb{Q}$) beyond the specific families above; every case with $\operatorname{Tdeg} D \ge 3$ not reachable by an Ore-extension filtration; and all of $\operatorname{char} p$ with $k$ algebraic over $\mathbb{F}_p$.

## 5. Principal Obstacles

- **No structure theory for finitely generated division rings.** Unlike commutative fields, a division algebra finitely generated over its center has no normal form, no transcendence basis, and no classification even for $\operatorname{Tdeg}=2$. Every proof to date first *presents* $D$ as $\operatorname{Frac}$ of a concrete filtered ring; the conjecture as stated grants no such presentation.
- **Freeness is a statement about denominators.** In all model cases the free pair lies outside any finitely generated subring: elements of the form $fx^{i}$ with $f$ in the coefficient field are *never* free (Section 10 proves this by a dimension count). The witnesses must have unbounded denominator complexity, which no general existence machinery supplies.
- **Cancellation control.** Valuation arguments prove freeness by showing leading terms of distinct words never cancel. This needs a valuation on $D$ with large enough value group. Finitely generated division rings need not admit *any* nontrivial valuation, and the Mal'cev–Neumann embedding requires an ordered group already present in the data.
- **Uncountability is used essentially.** Bell–Rogalski's $\operatorname{Tdeg}=2$ theorem builds the free pair as a member of an uncountable family, discarding countably many bad parameters. Over $\mathbb{Q}$ the parameter space is countable and the argument collapses.
- **GK-dimension does not localize.** Passing from $R$ to $\operatorname{Frac}(R)$ destroys growth control: $\operatorname{GKdim} A_1 = 2$ but $D_1$ contains free algebras of exponential growth. Growth-based induction, the standard tool for algebras, therefore gives nothing.
- **Characteristic $p$ over $\overline{\mathbb{F}_p}$.** There the Frobenius makes automorphism orbits behave like finite orbits, and the dynamical criterion that drives the Ore-extension proofs is simply false.

## 6. The Gap

Proved: $D$ contains a free subalgebra whenever $D$ carries a **filtration or valuation exhibiting a shift dynamical system** — an automorphism $\sigma$ with an infinite orbit on a coefficient field — plus either small $\operatorname{Tdeg}$ or an uncountable base.

Conjectured: freeness with **no presentation given at all**.

The precise step to be crossed: show that any finitely generated division algebra $D$ with $\dim_k D=\infty$ admits a nontrivial *birational invariant of shift type* — concretely, either (a) a nontrivial valuation with noncommutative residue or non-trivial value group, or (b) a subfield $K \subset D$ and $u \in D^\times$ with $uKu^{-1} = K$ and $u$ acting on $K$ with infinite order. Given (b), Bell–Rogalski's Ore-extension theorem applies. Nobody knows how to produce such a $u$ from finite generation alone, and it is not known whether every infinite-dimensional finitely generated $D$ even contains a maximal subfield stabilised by a nontrivial inner automorphism. Removing the uncountability hypothesis in the $\operatorname{Tdeg}=2$ theorem is the smaller, more tractable half of the gap.

## 7. Current Research (as of June 2026)

- **Waterloo / UCSD school (Bell, Rogalski, and collaborators).** Ongoing programme reducing freeness to dynamics of automorphisms on projective varieties; the aim is to replace "uncountable field" with a Zariski-density argument valid over $\mathbb{Q}$. *(frontier — verify)*
- **São Paulo school (Gonçalves, Ferreira, Sánchez).** Free *group* algebras and free symmetric subgroups in division rings, especially in $\operatorname{Frac} k[\Gamma]$ for orderable $\Gamma$ and in division rings with involution; the technique of choice is Mal'cev–Neumann series with a Hahn valuation.
- **Noncommutative projective geometry.** Division rings of $\operatorname{Tdeg}=3$ arising as function fields of noncommutative surfaces (Artin–Stafford, Sklyanin algebras) are the first systematic test class beyond the settled range; freeness for generic Sklyanin division algebras is asserted in recent work. *(frontier — verify)*
- **Positive characteristic.** Isolated study of $\operatorname{Frac}$ of iterated Ore extensions over $\overline{\mathbb{F}_p}$, where the conjecture may well be false; no counterexample has been produced.
- **Related conjectures.** Lichtman's conjecture (free subgroups in $D^\times$) is tracked in parallel; it is known to follow from the Makar-Limanov conjecture in the presence of a suitable valuation but not in general.

## 8. Future Work

1. **Remove uncountability.** Make the Bell–Rogalski $\operatorname{Tdeg}=2$ argument effective: replace "a generic parameter works" by an explicit parameter, giving the conjecture over $\mathbb{Q}$ for $\operatorname{Tdeg}=2$.
2. **Prove a valuation existence theorem.** Show every infinite-dimensional finitely generated division algebra has a nontrivial valuation, or a $\sigma$-stable subfield with $\sigma$ of infinite order. This is the single highest-value missing lemma.
3. **Attack $\operatorname{Tdeg}=3$.** Settle function fields of noncommutative surfaces, where a birational classification (Artin's conjecture) is at least partly available.
4. **Strengthen to free group algebras.** Determine whether every $D$ known to contain $k\langle a,b\rangle$ contains $k[F_2]$; the implication is open in general.
5. **Settle or exploit $\overline{\mathbb{F}_p}$.** Either prove the conjecture there or produce the first counterexample, which would sharpen the statement rather than kill it.

## 9. Key References

- **[Foundational]** L. Makar-Limanov. *The skew field of fractions of the Weyl algebra contains a free noncommutative subalgebra.* Communications in Algebra 11 (1983), 2003–2006.
- **[Foundational]** L. Makar-Limanov. *On free subobjects of skew fields.* In: Methods in Ring Theory (Antwerp, 1983), NATO ASI Series C 129, Reidel, 1984.
- **[Foundational]** A. I. Lichtman. *On subgroups of the multiplicative group of skew fields.* Proceedings of the American Mathematical Society 63 (1977), 15–16.
- **[Partial results]** M. Lorenz. *On free subalgebras of certain division algebras.* Proceedings of the American Mathematical Society 98 (1986), 401–405.
- **[Partial results]** L. Makar-Limanov, P. Malcolmson. *Free subalgebras of enveloping fields.* Proceedings of the American Mathematical Society 111 (1991), 315–322.
- **[Partial results]** K. Chiba. *Free subgroups and free subsemigroups of division rings.* Journal of Algebra 184 (1996), 570–574.
- **[SOTA]** J. P. Bell. *Division algebras of Gelfand–Kirillov transcendence degree 2.* Israel Journal of Mathematics 171 (2009), 51–60.
- **[SOTA]** J. P. Bell, D. Rogalski. *Free subalgebras of quotient rings of Ore extensions.* Algebra & Number Theory 6 (2012), 1349–1367.
- **[SOTA]** J. P. Bell, D. Rogalski. *Free subalgebras of division algebras over uncountable fields.* Mathematische Zeitschrift 277 (2014), 591–609.
- **[Survey]** J. Z. Gonçalves, M. Shirvani. *A survey on free objects in division rings and in division rings with an involution.* Communications in Algebra 40 (2012), 1704–1723.
- **[Background]** P. M. Cohn. *Skew Fields: Theory of General Division Rings.* Cambridge University Press, 1995.
- **[Background]** G. R. Krause, T. H. Lenagan. *Growth of Algebras and Gelfand–Kirillov Dimension.* Revised edition, AMS Graduate Studies in Mathematics 22, 2000.

## 10. Worked Example / Concrete Special Case

**Setting.** Let $k$ be a field, $q \in k^\times$ not a root of unity, $K = k(y)$, and $\sigma \in \operatorname{Aut}_k K$ with $\sigma(y) = qy$. Let $R = K[x;\sigma]$, so $x\alpha = \sigma(\alpha)x$, and $D = \operatorname{Frac} R = \operatorname{Frac} k_q[x,y]$, the quantum plane division ring. Here $\dim_k D = \infty$ (since $q$ is not a root of unity, the center of $D$ is $k$) and $D$ is generated by $x,y$, so the conjecture applies. It is **true** here, by Bell–Rogalski 2012. The point of the example is to see *why the free pair must have complicated denominators*.

**Claim.** No pair $a = fx$, $b = gx$ with $f,g \in K$ is free over $k$.

**Proof.** Write $f = p/r$, $g = s/r$ with $p,s,r \in k[y]$ of degree $\le d$. A word $w = z_{1}z_{2}\cdots z_{n}$ with $z_j \in \{a,b\}$ satisfies, by repeated use of $x\alpha = \sigma(\alpha)x$,
$$w \;=\; f_{\varepsilon_1}\,\sigma(f_{\varepsilon_2})\,\sigma^{2}(f_{\varepsilon_3})\cdots \sigma^{n-1}(f_{\varepsilon_n})\,x^{n}, \qquad f_0 = f,\; f_1 = g .$$
Since $\sigma$ preserves $k[y]$ and its degrees ($\sigma(y^i)=q^i y^i$), each coefficient has the shape
$$c_w \;=\; \frac{N_w(y)}{R_n(y)}, \qquad R_n \;=\; \prod_{j=0}^{n-1}\sigma^{j}(r), \qquad \deg N_w \le nd,$$
with the **same** denominator $R_n$ for all $2^n$ words of length $n$. Hence $\{c_w\}$ is $k$-linearly independent iff $\{N_w\}$ is. But the $N_w$ lie in the $k$-space of polynomials of degree $\le nd$, of dimension $nd+1$. For $n$ with $2^n > nd+1$ — e.g. $n \ge 2\log_2(d+2)+4$ — there is a nontrivial relation $\sum_w \lambda_w N_w = 0$, hence $\sum_w \lambda_w w = 0$ in $D$. So $k\langle a,b\rangle$ is not free. $\square$

**Concrete instance.** Take $f = 1$, $g = y$, i.e. $a = x$, $b = yx$. Then $c_w = q^{\,e(w)} y^{|w|_1}$ where $|w|_1$ counts the $b$'s and $e(w)=\sum_{j:\varepsilon_{j+1}=1} j$. Two length-$3$ words with the same $b$-count, $w_1 = abb$ and $w_2 = bab$, give $c_{w_1} = q^{1+2}y^2 = q^{3}y^{2}$ and $c_{w_2} = q^{0+2}y^{2}=q^{2}y^{2}$, so
$$q^{2}\,(abb) \;-\; q^{3}\,(bab) \;=\; 0$$
is an explicit relation of degree $3$. The same computation kills every pair of the form $(fx^i, gx^j)$: all such words are $K$-multiples of a single power of $x$ with a common denominator.

**Moral.** Freeness in $D$ cannot be witnessed inside any localization of $R$ at a fixed multiplicative set generated by finitely many $\sigma$-orbits. Bell–Rogalski's witnesses are of the form $a = x$, $b = h$ for $h \in D$ whose denominator meets infinitely many $\sigma$-orbits, so that the polynomial degrees $\deg N_w$ grow linearly in $n$ *per orbit* and the count $nd+1$ is replaced by an exponentially large space. This shift from "bounded denominator" to "orbit-spreading denominator" is exactly the dynamical input identified in Section 6 as the missing ingredient in the general case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*