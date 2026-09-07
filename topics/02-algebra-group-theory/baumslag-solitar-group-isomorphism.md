---
id: 02-algebra-group-theory/baumslag-solitar-group-isomorphism
title: "Baumslag-Solitar Group Isomorphism"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Baumslag-Solitar Group Isomorphism

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/baumslag-solitar-group-isomorphism` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

For nonzero integers $m,n$ the **Baumslag–Solitar group** is the two-generator one-relator group
$$BS(m,n)=\langle a,t \mid t\,a^{m}\,t^{-1}=a^{n}\rangle .$$

The *classical* isomorphism problem asks: given $(m,n)$ and $(m',n')$, decide whether $BS(m,n)\cong BS(m',n')$. This case is **solved**: Moldavanskii (1991) proved
$$BS(m,n)\cong BS(m',n')\iff (m',n')\in\{(m,n),(-m,-n),(n,m),(-n,-m)\}.$$

The problem that remains open is the natural generalization. A **generalized Baumslag–Solitar (GBS) group** is a finitely generated group acting on a tree with all vertex and edge stabilizers infinite cyclic; equivalently, $G=\pi_1(\mathbb{G})$ for a finite graph of groups $\mathbb{G}$ with all vertex and edge groups $\cong\mathbb{Z}$. Such a $\mathbb{G}$ is encoded by a finite **labeled graph** $(\Gamma,\lambda)$, $\lambda(e)\in\mathbb{Z}\setminus\{0\}$ for each oriented edge. $BS(m,n)$ is the case of a single vertex with one loop labeled $(m,n)$.

> **Open problem.** Is there an algorithm that, given two finite labeled graphs $(\Gamma_1,\lambda_1)$ and $(\Gamma_2,\lambda_2)$, decides whether $\pi_1(\Gamma_1,\lambda_1)\cong\pi_1(\Gamma_2,\lambda_2)$?

A complete solution means either an explicit decision procedure with proof of correctness and termination, or a reduction of a known undecidable problem (e.g. Hilbert's tenth problem, or the word problem for a fixed f.p. group) to GBS isomorphism. Ancillary open questions: give a complete list of computable isomorphism invariants; decide the *rank* and *automorphism-group* problems uniformly over the class.

## 2. Mathematical Foundations

**Bass–Serre setup.** Let $G$ act cocompactly and without inversions on a simplicial tree $T$ with all stabilizers $\cong\mathbb{Z}$. The quotient graph of groups $\mathbb{G}=T/G$ carries, for each oriented edge $e$ with terminal vertex $v$, the index
$$\lambda(e)=[\,G_v : \iota_e(G_e)\,]\in\mathbb{Z}\setminus\{0\},$$
recorded with sign once generators of the cyclic groups are fixed. Then
$$G=\pi_1(\Gamma,\lambda)=\Big\langle\; \{a_v\}_{v\in V},\ \{t_e\}_{e\in E}\ \Big|\ t_e\,a_{o(e)}^{\lambda(\bar e)}\,t_e^{-1}=a_{t(e)}^{\lambda(e)},\ \ t_e=1\ (e\in \mathcal{T})\;\Big\rangle,$$
where $\mathcal{T}$ is a spanning tree.

**Modular homomorphism.** A GBS group $G$ that is not $\mathbb{Z}$, $\mathbb{Z}^2$, or the Klein bottle group has a canonical commensurated infinite cyclic subgroup, and there is a well-defined
$$\Delta_G : G\longrightarrow \mathbb{Q}^{\times}_{>0},\qquad \Delta_G(g)=\frac{[\,C : C\cap gCg^{-1}\,]}{[\,gCg^{-1} : C\cap gCg^{-1}\,]},$$
computed on a loop $\gamma=e_1\cdots e_k$ of $\Gamma$ by $\Delta(\gamma)=\prod_i \lambda(e_i)/\lambda(\bar e_i)$. For $BS(m,n)$: $\Delta(a)=1$, $\Delta(t)=n/m$. $G$ is **unimodular** when $\mathrm{im}\,\Delta\subseteq\{1\}$; equivalently $G$ is virtually $F_k\times\mathbb{Z}$ (Levitt).

**Deformation spaces.** All cocompact cyclic $G$-trees for a fixed GBS group $G$ (with $G$ not $\mathbb{Z}$, $\mathbb{Z}^2$, Klein bottle) have the same elliptic subgroups, so they lie in a single **deformation space** $\mathcal{D}(G)$ (Forester 2002, 2003). Two reduced trees in $\mathcal{D}(G)$ are connected by a finite sequence of **elementary moves**; Clay–Forester sharpened this to *slides*, *inductions*, and $A^{\pm1}$-*moves*. Hence:
$$\pi_1(\Gamma_1,\lambda_1)\cong\pi_1(\Gamma_2,\lambda_2)\iff (\Gamma_1,\lambda_1)\ \text{and}\ (\Gamma_2,\lambda_2)\ \text{are related by a finite sequence of these moves.}$$
The isomorphism problem is therefore *semi-decidable* (enumerate move sequences); the difficulty is the complementary semi-decision — certifying **non**-isomorphism.

**Standard invariants.** $H_1(BS(m,n))\cong\mathbb{Z}\oplus\mathbb{Z}/(n-m)$; more generally $H_1$ of a labeled graph is computable from the relation matrix. Other invariants: $\mathrm{im}\,\Delta\le\mathbb{Q}^\times_{>0}$, the set of primes dividing labels, unimodularity, first Betti number of $\Gamma$ (an invariant only after reduction, and not in general), $\mathbb{Z}$-cohomological dimension $2$ (Kropholler), and quasi-isometry type.

## 3. History & State of the Art (SOTA)

- **1962.** Baumslag and Solitar introduce $BS(m,n)$ to exhibit finitely presented non-Hopfian groups; $BS(2,3)$ is the canonical example.
- **1972.** Meskin: $BS(m,n)$ is residually finite iff $|m|=1$, $|n|=1$, or $|m|=|n|$. Combined with Collins–Levin and earlier work: $BS(m,n)$ is Hopfian iff $|m|=1$, $|n|=1$, $|m|=|n|$, or $m$ and $n$ have the same set of prime divisors.
- **1990.** Kropholler classifies groups of cohomological dimension $2$ acting on trees with cyclic stabilizers, providing the structural frame for GBS groups.
- **1991.** Moldavanskii settles the isomorphism problem for the two-parameter family (Section 1). Its proof exploits the uniqueness of the cyclic HNN splitting.
- **1993.** Bass's covering theory for graphs of groups supplies the combinatorial machinery for comparing labeled graphs.
- **1998–2001.** Quasi-isometric rigidity: Farb–Mosher classify the solvable groups $BS(1,n)$ up to QI ($BS(1,n)\sim_{QI}BS(1,m)$ iff $m,n$ have a common power); Whyte shows that *all* $BS(m,n)$ with $2\le|m|\le|n|$ are quasi-isometric to each other. So QI type is far coarser than isomorphism type.
- **2002–2006.** Forester's deformation theorem and JSJ-uniqueness results make $\mathcal{D}(G)$ the correct object; *Splittings of generalized Baumslag–Solitar groups* (2006) analyzes when $\mathcal{D}(G)$ contains only finitely many reduced trees.
- **2007–2015.** Levitt computes $\mathrm{Out}(G)$ for GBS groups, proves the unimodular = virtually $F\times\mathbb{Z}$ characterization, and solves the rank problem for large subclasses.
- **2008–2009.** Clay–Forester give the moves theorem and decision procedures for substantial subclasses — the current SOTA.
- **2017–present.** Dudkin and coauthors (Novosibirsk) push decidability into families defined by the structure of "mobile" edges and by valence bounds.

## 4. Partial Results / Verified Cases

The isomorphism problem is **solved** in the following cases.

1. **Classical $BS(m,n)$, all $m,n\neq 0$** (Moldavanskii 1991). Complete and effective: check the four-element orbit of $(m,n)$.
2. **Amalgams $\langle a,b\mid a^{m}=b^{n}\rangle$** (segment graphs, $|m|,|n|\ge 2$): isomorphic iff $\{|m|,|n|\}=\{|m'|,|n'|\}$; these are torus-knot-type groups with center $\langle a^m\rangle$ and $G/Z\cong \mathbb{Z}/m * \mathbb{Z}/n$, a complete invariant.
3. **Unimodular GBS groups** ($\mathrm{im}\,\Delta=\{1\}$, equivalently virtually $F_k\times\mathbb{Z}$): the deformation space contains finitely many reduced trees, and the finite list can be enumerated and compared, giving an algorithm.
4. **Finite deformation space.** Whenever $\mathcal{D}(G)$ has only finitely many reduced labeled graphs up to isomorphism — a condition Forester (2006) characterizes combinatorially — brute-force enumeration of slide/induction/$A^{\pm}$-moves terminates and decides isomorphism.
5. **Low complexity graphs.** Labeled graphs with first Betti number $0$ (trees) and $1$ are handled by the Clay–Forester machinery; the tree case reduces to normalizing labels by slides.
6. **Bounded parameters.** Families with a bound on valence or on the number of "mobile" edges (edges that can be slid), e.g. Dudkin's one-mobile-edge class (2017).
7. **Special ambient properties.** GBS groups that are residually finite, or linear, or have $\mathrm{im}\,\Delta$ generated by a single prime power, admit extra rigidity that collapses the move enumeration.

Computationally, exhaustive move-enumeration decides isomorphism for all labeled graphs with, say, $\le 4$ vertices and labels of absolute value $\le 10$ in practice, because the reachable reduced graphs stay small — but no a priori bound on graph size along a move sequence is known in general.

## 5. Principal Obstacles

- **No stopping criterion.** Isomorphism is semi-decidable by enumerating moves, but a sequence of slides can pass through labeled graphs of unboundedly large label size before returning to a small one. Without a computable bound on the complexity of an intermediate graph, the search cannot be cut off. This is the single central obstruction.
- **Infinite deformation spaces.** When $\mathrm{im}\,\Delta\ne\{1\}$, $\mathcal{D}(G)$ typically contains infinitely many reduced trees, so "enumerate and compare normal forms" fails; there is no known canonical (JSJ-style) representative in the non-unimodular case.
- **Non-Hopficity kills residual finiteness arguments.** $BS(2,3)$ is non-Hopfian and not residually finite, so the classical "compare finite quotients" semi-algorithm for non-isomorphism is unavailable across the class.
- **Coarse invariants are too coarse.** Whyte's theorem says all $BS(m,n)$, $2\le|m|\le|n|$, are quasi-isometric; so geometric group theory (asymptotic cones, growth, boundaries, $\ell^2$-invariants) cannot separate them. Homology, $\Delta$, and prime sets separate many but provably not all pairs of labeled graphs.
- **Slides do not commute.** The move set has no confluent rewriting structure: no Newman-style diamond lemma is known for slide/induction moves, so normal forms cannot be produced by local rewriting.
- **Interaction with number theory.** Deciding when two label configurations are slide-equivalent reduces to solvability of systems of multiplicative Diophantine conditions on the labels; these are not known to be uniformly decidable, and any such reduction potentially imports hardness.

## 6. The Gap

Section 4 hands us decidability whenever the deformation space is finite or the labeled graph is combinatorially simple. Section 1 asks for all GBS groups. The precise gap:

> **Given a GBS group $G$ with $\mathrm{im}\,\Delta_G\neq\{1\}$ and infinite deformation space, find a computable function $f$ such that any two isomorphic reduced labeled graphs of complexity $\le N$ are connected by a move sequence through graphs of complexity $\le f(N)$** — or produce a complete computable set of invariants for $\mathcal{D}(G)$.

Either would immediately give the algorithm: the first bounds the search, the second replaces it. The complementary possibility — that GBS isomorphism is undecidable — would require encoding an undecidable problem into label arithmetic, and no such encoding is known, largely because GBS groups have solvable word and conjugacy problems and are of cohomological dimension $2$, which limits the expressiveness available.

## 7. Current Research (as of June 2026)

- **Novosibirsk school (Dudkin and collaborators).** Steady extension of decidable subclasses by controlling mobile edges, valence, and the centralizer structure; also work on GBS groups with prescribed $\mathrm{Out}$.
- **Deformation-space geometry (Oklahoma / Nice lineage: Forester, Clay, Levitt, Guirardel–Levitt).** Treating $\mathcal{D}(G)$ as a contractible complex and looking for a group-theoretic "Outer space" analogue with a computable fundamental domain for $\mathrm{Out}(G)$. A fundamental domain of computable size would close the gap. *(frontier — verify)*
- **Effective JSJ theory.** Making Guirardel–Levitt canonical JSJ decompositions algorithmic for cyclic edge groups; a canonical tree in $\mathcal{D}(G)$ computable from a presentation would give a normal form. *(frontier — verify)*
- **Complexity-theoretic side.** Attempts to reduce a variant of the multiplicative Diophantine problem to slide-equivalence, aiming at an undecidability proof rather than an algorithm. *(frontier — verify)*
- **Machine search.** Computer enumeration of reduced labeled graphs to test candidate invariant sets and to look for isomorphic pairs whose connecting move sequences require large intermediate graphs — the empirical form of the bounding question. *(frontier — verify)*

## 8. Future Work

1. **Prove or refute a complexity bound** on intermediate labeled graphs in a minimal move sequence; even a bound exponential in $N$ suffices for decidability.
2. **Build a canonical form** for non-unimodular GBS groups, perhaps by fixing the "elastic"/"rigid" vertex decomposition of Clay–Forester and normalizing labels along elastic parts.
3. **Isolate the arithmetic core**: identify a decision problem about integer matrices/labels that is equivalent to slide-equivalence, and settle its decidability separately.
4. **Extend past cyclic edge groups** to GBS-like groups with $\mathbb{Z}^n$ vertex groups, where more rigidity may make the problem *easier* and reveal what is special about rank one.
5. **Sharpen non-isomorphism certificates**: find invariants beyond $H_1$, $\Delta$, and prime sets — e.g. profinite-type invariants of the unimodular finite-index subgroups, or bounded cohomology.

## 9. Key References

- **[Foundational]** G. Baumslag, D. Solitar. *Some two-generator one-relator non-Hopfian groups.* Bulletin of the American Mathematical Society **68** (1962), 199–201.
- **[Foundational]** S. Meskin. *Nonresidually finite one-relator groups.* Transactions of the American Mathematical Society **164** (1972), 105–114.
- **[Foundational]** J.-P. Serre. *Trees.* Springer-Verlag, 1980.
- **[Foundational]** H. Bass. *Covering theory for graphs of groups.* Journal of Pure and Applied Algebra **89** (1993), 3–47.
- **[Classical solution]** D. I. Moldavanskii. *On the isomorphisms of Baumslag–Solitar groups.* Ukrainian Mathematical Journal **43** (1991), 1569–1571.
- **[Structure]** P. H. Kropholler. *Baumslag–Solitar groups and some other groups of cohomological dimension two.* Commentarii Mathematici Helvetici **65** (1990), 547–558.
- **[Structure]** M. Forester. *Deformation and rigidity of simplicial group actions on trees.* Geometry & Topology **6** (2002), 219–267.
- **[Structure]** M. Forester. *On uniqueness of JSJ decompositions of finitely generated groups.* Commentarii Mathematici Helvetici **78** (2003), 740–751.
- **[Structure]** M. Forester. *Splittings of generalized Baumslag–Solitar groups.* Geometriae Dedicata **121** (2006), 43–59.
- **[SOTA]** M. Clay, M. Forester. *On the isomorphism problem for generalized Baumslag–Solitar groups.* Algebraic & Geometric Topology **8** (2008), 2289–2322.
- **[SOTA]** M. Clay, M. Forester. *Whitehead moves for G-trees.* Bulletin of the London Mathematical Society **41** (2009), 205–212.
- **[SOTA]** G. Levitt. *On the automorphism group of generalized Baumslag–Solitar groups.* Geometry & Topology **11** (2007), 473–515.
- **[SOTA]** G. Levitt. *Generalized Baumslag–Solitar groups: rank and finite index subgroups.* Annales de l'Institut Fourier **65** (2015), 725–762.
- **[SOTA / Recent]** F. A. Dudkin. *The isomorphism problem for generalized Baumslag–Solitar groups with one mobile edge.* Algebra and Logic **56** (2017), 197–209.
- **[Geometry]** B. Farb, L. Mosher. *A rigidity theorem for the solvable Baumslag–Solitar groups.* Inventiones Mathematicae **131** (1998), 419–451.
- **[Geometry]** K. Whyte. *The large scale geometry of the higher Baumslag–Solitar groups.* Geometric and Functional Analysis **11** (2001), 1327–1343.
- **[Survey]** D. J. S. Robinson. *Recent results on generalized Baumslag–Solitar groups.* Note di Matematica **30** (2010), 37–53.

## 10. Worked Example / Concrete Special Case

**(a) Separating $BS(2,3)$ from $BS(2,-3)$.** Abelianizing $ta^mt^{-1}=a^n$ kills $t$ from the relation and leaves $ma = na$, so
$$H_1(BS(m,n))\cong \mathbb{Z}\oplus \mathbb{Z}/(n-m).$$
For $(2,3)$: $\mathbb{Z}\oplus\mathbb{Z}/1=\mathbb{Z}$. For $(2,-3)$: $\mathbb{Z}\oplus\mathbb{Z}/5$. Not isomorphic — consistent with Moldavanskii, since $(2,-3)\notin\{(2,3),(-2,-3),(3,2),(-3,-2)\}$.

**(b) A genuine isomorphism.** $BS(2,3)\cong BS(3,2)$ via $a\mapsto a$, $t\mapsto t^{-1}$: the relation $ta^2t^{-1}=a^3$ is equivalent to $t^{-1}a^3t=a^2$, which is the defining relation of $BS(3,2)$ with generator $s=t^{-1}$. Likewise $a\mapsto a^{-1}$, $t\mapsto t$ gives $BS(m,n)\cong BS(-m,-n)$. Moldavanskii's theorem says these two symmetries generate *all* coincidences.

**(c) Non-Hopficity of $BS(2,3)$.** Define $\varphi(a)=a^{2}$, $\varphi(t)=t$. It respects the relation: $\varphi(ta^2t^{-1})=ta^4t^{-1}=(ta^2t^{-1})^2=a^6=\varphi(a^3)$. It is onto, because
$$\varphi\big(t\,a\,t^{-1}a^{-1}\big)=t\,a^{2}\,t^{-1}a^{-2}=a^{3}a^{-2}=a .$$
Its kernel is nontrivial: put $w=[\,t a t^{-1},\,a\,]$. Then $\varphi(w)=[\,ta^2t^{-1},a^2\,]=[a^3,a^2]=1$, while $w\neq 1$ by Britton's lemma (the word $tat^{-1}a t a^{-1} t^{-1}a^{-1}$ has no pinch, since $a^{\pm1}\notin\langle a^2\rangle,\langle a^3\rangle$). So $BS(2,3)$ is non-Hopfian, hence not residually finite — the reason finite quotients cannot certify non-isomorphism.

**(d) Where the GBS difficulty starts.** Take the labeled graph $\Gamma$: two vertices $u,v$ joined by an edge $e$ with $\lambda(\bar e)=2$ at $u$ and $\lambda(e)=2$ at $v$, plus a loop at $v$ labeled $(1,3)$. Then $\Delta$ sends the loop generator to $3$. A **slide** of the edge $e$ along the loop replaces the label pair at $v$ by $(2,6)$ or $(2\cdot 3^{k}, \dots)$ depending on direction, producing a different labeled graph with the *same* fundamental group. Iterating slides generates infinitely many pairwise non-isomorphic reduced labeled graphs, all defining one group. Deciding whether a given second graph lies in this infinite orbit is exactly the open problem: the labels grow by factors of $3$ at each step, and no theorem bounds how far they must grow before the two graphs can be matched.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*