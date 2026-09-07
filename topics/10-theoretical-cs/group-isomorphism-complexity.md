---
id: 10-theoretical-cs/group-isomorphism-complexity
title: "Group Isomorphism Complexity"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Group Isomorphism Complexity

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/group-isomorphism-complexity` · **Status:** open

## 1. Problem Statement / Conjecture

**Group Isomorphism (GpI).** Given the multiplication (Cayley) tables of two finite groups $G$ and $H$ of order $n$, decide whether $G \cong H$.

The input has size $\Theta(n^2 \log n)$ bits, so "polynomial time" means $n^{O(1)}$.

**The open question.** Is $\mathrm{GpI} \in \mathsf{P}$?

The standing barrier is that no general algorithm beats $n^{\Theta(\log n)}$, a bound essentially unchanged since 1978 apart from a constant factor in the exponent. The conjecture held by most workers in the area is that $\mathrm{GpI} \in \mathsf{P}$; a complete resolution is either

- a deterministic algorithm running in time $n^{O(1)}$ on all inputs, or
- a proof of hardness under a standard hypothesis (e.g. $\mathrm{GpI}$ is $\mathsf{NP}$-hard, which would give $\mathsf{PH}$ collapse consequences since $\mathrm{GpI} \in \mathsf{NP} \cap \mathsf{coAM}$).

An intermediate, widely stated milestone: give an $n^{o(\log n)}$ algorithm for **all** groups of order $n$.

## 2. Mathematical Foundations

**Generator enumeration.** Every group of order $n$ has a generating set of size at most $\log_2 n$: a strictly increasing chain $1 = G_0 < G_1 < \dots < G_k = G$ obtained by adding generators has $|G_{i+1}| \ge 2|G_i|$, so $k \le \log_2 n$. Fixing a generating tuple $(g_1,\dots,g_k)$ of $G$ and trying all $n^k$ candidate images in $H$ gives
$$T(n) = n^{\log_2 n + O(1)}.$$

**The hard case.** Let $p$ be an odd prime. A $p$-group $G$ has *class $2$ and exponent $p$* if $[G,G] \le Z(G)$ and $g^p = 1$ for all $g$. The **Baer correspondence** puts such groups in bijection with alternating bilinear maps: with $V = G/Z(G) \cong \mathbb{F}_p^{\,d}$ and $W = [G,G] \cong \mathbb{F}_p^{\,e}$,
$$\phi_G : V \times V \to W, \qquad \phi_G(\bar u, \bar v) = [u,v],$$
is bilinear and alternating, and
$$G \cong H \iff \phi_G \ \text{and} \ \phi_H \ \text{are pseudo-isometric},$$
i.e. there exist $A \in \mathrm{GL}(V)$, $C \in \mathrm{GL}(W)$ with
$$C\,\phi_G(u,v) = \phi_H(Au, Av) \quad \forall u,v \in V.$$
Equivalently: given two $d \times d \times e$ tensors over $\mathbb{F}_p$, decide equivalence under the group $\mathrm{GL}_d \times \mathrm{GL}_e$ acting on two of the three sides.

**Counting.** The number of groups of order $p^m$ is
$$p^{\frac{2}{27}m^3 + O(m^{8/3})}$$
(Higman's lower bound 1960, Sims' upper bound 1965), and almost all of them have class $2$ and exponent $p$. So with $n = p^m$ there are $n^{\Theta(\log^2 n / \log^2 p)}$ isomorphism types — information-theoretically a $\log n$-bit-per-symbol certificate is plausible, but the search space $|\mathrm{GL}_d(\mathbb{F}_p)| \approx p^{d^2}$ is superpolynomial in $n = p^{d+e}$.

**Complexity placement.** $\mathrm{GpI} \le^p_m \mathrm{GI}$ (graph isomorphism), hence $\mathrm{GpI} \in \mathsf{NP} \cap \mathsf{coAM}$ and is not $\mathsf{NP}$-complete unless $\mathsf{PH}$ collapses to $\Sigma_2^p$. Wolf (1994) showed $\mathrm{GpI} \in \mathsf{NSPACE}(\log^2 n)$, giving quasipolynomial time by a second route.

## 3. History & State of the Art (SOTA)

- **1978.** Tarjan's $n^{\log_2 n + O(1)}$ generator-enumeration bound, recorded in G. Miller's STOC paper on the $n^{\log n}$ isomorphism technique. This is the baseline that still stands for general $n$.
- **1994.** Wolf places $\mathrm{GpI}$ in nondeterministic $\log^2$-space.
- **2007.** Kavitha: abelian groups in $O(n)$ time — linear in the *order*, sublinear in the input.
- **2011–2012.** Babai, Codenotti, Grochow, Qiao: $n^{O(\log\log n)}$, then polynomial time, for **semisimple groups** (no abelian normal subgroup).
- **2013.** Rosenbaum: $n^{\frac12 \log_2 n + O(1)}$ by bidirectional collision detection — the only general improvement, a factor $2$ in the exponent.
- **2016.** Babai's quasipolynomial $\mathrm{GI}$ algorithm does *not* help: the reduction $\mathrm{GpI} \to \mathrm{GI}$ produces graphs on $\Theta(n^2)$ vertices and Babai's exponent is $(\log N)^{O(1)}$ with unspecified constant $> 2$.
- **2021.** Dietrich and Wilson: for a density-$1$ set of orders $n$, isomorphism is decided in time nearly linear in the input size.
- **2023.** Sun (STOC): $n^{O((\log n)^{5/6})}$ for $p$-groups of class $2$ and exponent $p$ — the first $n^{o(\log n)}$ algorithm for the case usually described as the bottleneck. It does not yet extend to all groups.

## 4. Partial Results / Verified Cases

Polynomial time is known for:

| Class | Bound | Source |
|---|---|---|
| Abelian groups of order $n$ | $O(n)$ | Kavitha 2007 |
| Groups with no abelian normal subgroup | $n^{O(1)}$ | Babai–Codenotti–Qiao 2012 |
| Abelian normal Hall subgroup with any complement | $n^{O(1)}$ | Qiao–Sarma–Tang 2011 |
| Coprime extensions $H \ltimes A$, $A$ abelian, $H$ elementary abelian / with central radical | $n^{O(1)}$ | Le Gall 2009; Grochow–Qiao 2017 |
| Groups whose commutator Lie algebra has genus $\le 2$ | $n^{O(1)}$ | Brooksbank–Maglione–Wilson 2017 |
| Direct-product decomposition (as a subroutine) | $n^{O(1)}$ | Kayal–Nezhmetdinov 2009; Wilson 2012 |
| Density-$1$ set of orders $n$ | $n^{2+o(1)}$ | Dietrich–Wilson 2021 |
| Class-2 exponent-$p$ $p$-groups, **average case** over $\phi$ | $n^{O(1)}$ w.h.p. | Li–Qiao 2017 |

Subquasipolynomial worst case: $n^{O((\log n)^{5/6})}$ for class-$2$ exponent-$p$ groups (Sun 2023); $n^{\frac12\log_2 n + O(1)}$ in general (Rosenbaum 2013).

Small orders are settled by explicit classification: all groups of order $\le 2000$ are catalogued (Besche–Eick–O'Brien 2002), $49{,}487{,}365{,}422$ of them of order $1024$, so isomorphism for $n \le 2000$ is table lookup.

## 5. Principal Obstacles

- **Invariants collapse on the hard case.** Order statistics, conjugacy-class sizes, character tables and subgroup-lattice counts all separate typical groups quickly. In a class-$2$ exponent-$p$ group every non-identity element has order $p$, all such groups of fixed $(d,e)$ have identical order statistics, and even the character table is nearly determined by $(d,e)$. The distinguishing information sits entirely in the $\mathrm{GL}_d \times \mathrm{GL}_e$-orbit of the tensor.
- **No canonical form for tensors.** Individual-and-refine — the engine behind Babai's $\mathrm{GI}$ algorithm — works because a graph has $n$ named points to individualize. Individualizing a group element in a $p$-group of class $2$ fixes only a $1$-dimensional subspace of $V$ and leaves $\mathrm{GL}_{d-1}$ acting; the recursion loses a $\log$ factor rather than a constant fraction. Weisfeiler–Leman for groups (Brachter–Schweitzer 2020) is provably weak on CFI-like $p$-group families.
- **Hardness is genuine, not just apparent.** Grochow and Qiao showed that class-$2$ exponent-$p$ isomorphism (and cubic form equivalence, matrix space isometry, and several other problems) are **Tensor Isomorphism-complete**. A polynomial algorithm for one gives it for all of them — a large obstruction to easy progress.
- **Group theory does not decompose the hard case.** The successful poly-time classes all exploit a Hall/Sylow splitting, semisimplicity, or bounded genus. Class-$2$ exponent-$p$ groups are a single prime, nilpotent, and have unbounded genus: every structural handle is absent.
- **The reduction to $\mathrm{GI}$ is lossy.** It squares the instance size, so any $\mathrm{GI}$ improvement short of $N^{O(1)}$ is useless for GpI.

## 6. The Gap

Proven: $n^{O((\log n)^{5/6})}$ on class-$2$ exponent-$p$ groups; $n^{\frac12 \log_2 n + O(1)}$ everywhere; $n^{O(1)}$ on the structured families of Section 4.

Wanted: $n^{O(1)}$ on all inputs. Two distinct gaps:

1. **Within the hard case.** Sun's exponent $(\log n)^{5/6}$ must fall to $O(1)$. His technique — a low-rank/regularity decomposition of the tensor plus a "large-genus" case analysis — currently gains only a fractional power; nobody has an approach that iterates it down to constant.
2. **From the hard case to all groups.** Even a poly-time algorithm for class-$2$ exponent-$p$ groups does not immediately give general GpI. Grochow–Qiao (2021) proved reductions from higher nilpotency class to class $2$ and from search to decision for $p$-groups, but a general-group-to-$p$-group reduction that respects extension data (the group cohomology $H^2(Q, A)$ with the induced $\mathrm{Aut}(Q) \times \mathrm{Aut}(A)$ action) is not known to be polynomial.

## 7. Current Research (as of June 2026)

- **Tensor-theoretic school** (Grochow, Qiao, and collaborators). Program: classify the TI-complete zoo, then attack tensor isomorphism directly with algebraic geometry and invariant theory (e.g. degree bounds for generating invariants of $\mathrm{GL}_d \times \mathrm{GL}_e$ actions). Also drives post-quantum cryptography proposals built on tensor/alternating-trilinear-form equivalence.
- **Extending Sun's technique.** Whether the $(\log n)^{5/6}$ exponent extends from class-$2$ exponent-$p$ to *all* groups of order $n$ is the sharpest near-term question. *(frontier — verify)*
- **Weisfeiler–Leman for groups** (Brachter, Schweitzer, Levet, Collins). Determining the WL dimension of natural group families, and combining WL with Sylow/central decompositions (Brooksbank–Grochow–Li–Qiao–Wilson).
- **Practical isomorphism** (Eick, O'Brien, Wilson, Maglione; the `Magma`/`GAP` filter-and-invariant machinery). Filters, adjoint algebras and genus invariants routinely separate groups of order $p^7$–$p^9$ that no worst-case theory handles.
- **Model variants.** Isomorphism for groups given by generating permutations or matrices, and quantum/average-case versions, remain separately open and in places provably harder.

## 8. Future Work

- Prove an $n^{O(1)}$ pseudo-isometry test for alternating bilinear maps $\mathbb{F}_p^d \times \mathbb{F}_p^d \to \mathbb{F}_p^e$ in the regime $e = \Theta(d)$, where all current methods degrade.
- Establish a polynomial-time *canonical form* (not just isomorphism test) for semisimple groups and for abelian groups, and lift it through group extensions — canonization is the property that composes.
- Sharpen the group-cohomology approach: given $Q$ and $A$, test $\mathrm{Aut}(Q)\times\mathrm{Aut}(A)$-orbit equality of cocycle classes in $H^2(Q,A)$ in time polynomial in $|Q||A|$.
- Find any unconditional lower bound above $\Omega(n^2)$ (the input-reading bound) in a restricted model, or prove GpI hard for a class such as $\mathsf{NC}^1$ under $\mathsf{AC}^0$ reductions.
- Determine whether the $\mathrm{GI} \not\le_{\mathsf{AC}^0} \mathrm{GpI}$ separation (Chattopadhyay–Torán–Wagner) extends to stronger reductions, which would be evidence that GpI is strictly easier than GI.

## 9. Key References

- **[Foundational]** G. L. Miller. *On the $n^{\log n}$ isomorphism technique: A preliminary report.* STOC 1978, 51–58. (Records Tarjan's $n^{\log_2 n + O(1)}$ bound.)
- **[Foundational]** M. J. Wolf. *Nondeterministic circuits, space complexity and quasigroups.* Theoretical Computer Science 125(2), 295–313, 1994.
- **[Foundational]** C. C. Sims. *Enumerating $p$-groups.* Proc. London Math. Soc. (3) 15, 151–166, 1965; G. Higman, *Enumerating $p$-groups I*, ibid. (3) 10, 24–30, 1960.
- **[Partial]** T. Kavitha. *Linear time algorithms for abelian group isomorphism and related problems.* Journal of Computer and System Sciences 73(6), 986–996, 2007.
- **[Partial]** L. Babai, P. Codenotti, Y. Qiao. *Polynomial-time isomorphism test for groups with no abelian normal subgroups.* ICALP 2012, LNCS 7391, 51–62.
- **[Partial]** Y. Qiao, J. M. N. Sarma, B. Tang. *On isomorphism testing of groups with normal Hall subgroups.* STACS 2011, LIPIcs 9, 567–578.
- **[Partial]** J. A. Grochow, Y. Qiao. *Algorithms for group isomorphism via group extensions and cohomology.* SIAM Journal on Computing 46(4), 1153–1216, 2017.
- **[SOTA]** D. J. Rosenbaum. *Bidirectional collision detection and faster deterministic isomorphism testing.* arXiv:1304.3935, 2013.
- **[SOTA]** X. Sun. *Faster isomorphism for $p$-groups of class 2 and exponent $p$.* STOC 2023, 433–440.
- **[SOTA]** H. Dietrich, J. B. Wilson. *Group isomorphism is nearly-linear time for most orders.* FOCS 2021, 457–467.
- **[SOTA]** Y. Li, Y. Qiao. *Linear algebraic analogues of the graph isomorphism problem and the Erdős–Rényi model.* FOCS 2017, 463–474.
- **[Structural]** J. A. Grochow, Y. Qiao. *On the complexity of isomorphism problems for tensors, groups, and polynomials I: tensor isomorphism-completeness.* SIAM Journal on Computing 52(2), 568–617, 2023 (conference version ITCS 2021).
- **[Structural]** A. Chattopadhyay, J. Torán, F. Wagner. *Graph isomorphism is not $\mathsf{AC}^0$-reducible to group isomorphism.* ACM Transactions on Computation Theory 5(4), Article 13, 2013.
- **[Structural]** J. Brachter, P. Schweitzer. *On the Weisfeiler–Leman dimension of finite groups.* LICS 2020, 287–300.
- **[Related]** L. Babai. *Graph isomorphism in quasipolynomial time.* STOC 2016, 684–697.
- **[Survey]** P. A. Brooksbank, J. Maglione, J. B. Wilson. *A fast isomorphism test for groups whose Lie algebra has genus 2.* Journal of Algebra 473, 545–590, 2017.
- **[Survey]** H. U. Besche, B. Eick, E. A. O'Brien. *A millennium project: constructing small groups.* International Journal of Algebra and Computation 12(5), 623–644, 2002.

## 10. Worked Example / Concrete Special Case

**(a) Easy instance, $n = 8$.** Take $G = D_4$ (dihedral) and $H = Q_8$ (quaternion). Both are non-abelian of order $8$ with centre of order $2$ and $G/Z \cong C_2 \times C_2$. The order profile separates them in $O(n \log n)$ time:

| order of $g$ | 1 | 2 | 4 |
|---|---|---|---|
| $D_4$ | 1 | 5 | 2 |
| $Q_8$ | 1 | 1 | 6 |

Different multisets $\Rightarrow$ $D_4 \not\cong Q_8$. No search needed.

**(b) Hard instance, $n = p^6$.** Let $p$ be odd, $d = 4$, $e = 2$, so $V = \mathbb{F}_p^4$, $W = \mathbb{F}_p^2$. An alternating map $\phi : V \times V \to W$ is a pair of alternating $4\times 4$ matrices $(M_1, M_2)$ over $\mathbb{F}_p$ via $\phi(u,v) = (u^\top M_1 v,\; u^\top M_2 v)$. Take
$$M_1 = \begin{pmatrix} 0&1&0&0\\ -1&0&0&0\\ 0&0&0&1\\ 0&0&-1&0\end{pmatrix},\qquad M_2 = \begin{pmatrix} 0&0&1&0\\ 0&0&0&1\\ -1&0&0&0\\ 0&-1&0&0\end{pmatrix}.$$
Each of $G_\phi, H_\psi$ (the corresponding class-$2$ exponent-$p$ groups of order $p^6$) has $p^6 - 1$ elements of order $p$ and centre of order $p^2$: **every order-based, class-based and character-based invariant is identical** for all such $(M_1,M_2)$.

The only remaining question is whether the pencil $\lambda M_1 + \mu M_2$ is equivalent to $\lambda M_1' + \mu M_2'$ under $(A,C) \in \mathrm{GL}_4 \times \mathrm{GL}_2$. Here $e=2$ is small enough to solve: the Pfaffian $\mathrm{Pf}(\lambda M_1 + \mu M_2)$ is a binary form of degree $2$ in $(\lambda,\mu)$, and $\mathrm{Pf}$ transforms as $\det(A)\cdot \mathrm{Pf}$ composed with $C^{-\top}$, so its root pattern in $\mathbb{P}^1(\overline{\mathbb{F}_p})$ (two distinct roots / one double root / irreducible) is an isomorphism invariant. For the pair above, $\mathrm{Pf}(\lambda M_1 + \mu M_2) = \lambda^2 + \mu^2$, which is irreducible over $\mathbb{F}_p$ exactly when $p \equiv 3 \pmod 4$ — so this group is *not* isomorphic to the one with $\mathrm{Pf} = \lambda\mu$, and the test takes $O(\mathrm{poly}(d,e,\log p))$ time. This is exactly the genus-$2$ case solved by Brooksbank–Maglione–Wilson.

**Where it breaks.** Raise $e$ to $\Theta(d)$. Now $\mathrm{Pf}$ is a form of degree $d/2$ in $e$ variables, its orbit under $\mathrm{GL}_e$ is itself a hypersurface-equivalence problem of the same difficulty, and the invariant buys nothing. Brute force costs $|\mathrm{GL}_d(\mathbb{F}_p)| \approx p^{d^2} = n^{\Theta(d^2/(d+e))} = n^{\Theta(\log n/\log p)}$ — the $n^{\Theta(\log n)}$ wall. For $p = 2, d = e = 20$ ($n = 2^{40}$), that is roughly $2^{400}$ candidate maps, versus about $2^{40 \cdot 40} $ input bits — the search space is exponentially larger than any certificate needs to be, and closing that ratio is precisely the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*