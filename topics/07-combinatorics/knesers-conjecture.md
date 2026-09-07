---
id: 07-combinatorics/knesers-conjecture
title: "Kneser's Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kneser's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/knesers-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

For integers $n \ge 2k > 0$, the **Kneser graph** $KG(n,k)$ has as vertices the $k$-element subsets of $[n] = \{1,\dots,n\}$, with two vertices adjacent iff the corresponding sets are disjoint.

**Kneser's Conjecture (1955).** The chromatic number is
$$\chi\bigl(KG(n,k)\bigr) = n - 2k + 2 .$$

Equivalently: if the $k$-subsets of $[n]$ are partitioned into $n-2k+1$ classes, some class contains two disjoint sets. The upper bound $\chi \le n-2k+2$ is an easy explicit construction; the conjecture is the **lower bound** $\chi \ge n-2k+2$, i.e. that no partition into $n-2k+1$ intersecting families exists.

Proved by Lovász in 1978. The page is retained because the *method* (Borsuk–Ulam) and the resulting research programme — combinatorial proofs, hypergraph generalizations, stable subgraphs, computational complexity of finding a monochromatic edge — contain live open problems, notably the **Alon–Drewnowski–Łuczak conjecture** on stable Kneser hypergraphs.

A complete resolution of the remaining questions requires either (a) an elementary/combinatorial derivation of the general lower bound with no topological input, or (b) determination of $\chi$ for $s$-stable $r$-uniform Kneser hypergraphs in the full parameter range.

## 2. Mathematical Foundations

**Kneser graph.** $V(KG(n,k)) = \binom{[n]}{k}$, $E = \{\,\{A,B\} : A \cap B = \emptyset\,\}$. It is vertex-transitive and $\binom{n-k}{k}$-regular.

**Upper bound.** Colour $A \in \binom{[n]}{k}$ by $c(A) = \min\{\min A,\; n-2k+2\}$. If $c(A)=c(B)=i < n-2k+2$ then $i \in A\cap B$; if $c(A)=c(B)=n-2k+2$ then $A,B \subseteq \{n-2k+2,\dots,n\}$, a set of size $2k-1$, so $|A\cap B|\ge 1$. Hence $\chi \le n-2k+2$.

**Erdős–Ko–Rado.** For $n \ge 2k$ the maximum independent set of $KG(n,k)$ has size $\binom{n-1}{k-1}$, attained by stars $\{A : i \in A\}$. This alone gives only $\chi \ge n/k$.

**Neighborhood complex.** $\mathcal{N}(G)$ is the simplicial complex on $V(G)$ whose faces are sets with a common neighbour.

> **Lovász's Theorem (1978).** If $\mathcal{N}(G)$ is $t$-connected then $\chi(G) \ge t+3$.

Combined with the computation that $\mathcal{N}(KG(n,k))$ is homotopy equivalent to $S^{\,n-2k}$, hence $(n-2k-1)$-connected, this yields $\chi \ge n-2k+2$.

**Borsuk–Ulam Theorem.** Every continuous $f : S^d \to \mathbb{R}^d$ has $x$ with $f(x)=f(-x)$. Equivalent antipodal form: $S^d$ cannot be covered by $d+1$ closed (or open) sets none of which contains an antipodal pair.

**Gale's Lemma.** For $d \ge 0$, $k\ge 1$ there exist $2k+d$ points on $S^d$ such that every open hemisphere contains at least $k$ of them. This is the combinatorial input to Bárány's proof.

**Dol'nikov's bound.** For a hypergraph $\mathcal{H}$, the *colorability defect* $\mathrm{cd}(\mathcal{H})$ is the minimum of $|S|$ over $S \subseteq [n]$ such that $\mathcal{H}$ restricted to $[n]\setminus S$ is 2-colourable. Then $\chi(KG(\mathcal{H})) \ge \mathrm{cd}(\mathcal{H})$, generalizing Kneser's bound.

**Kneser hypergraphs.** $KG^r(n,k)$ has vertex set $\binom{[n]}{k}$ and $r$-edges the $r$-tuples of pairwise disjoint sets.

> **Alon–Frankl–Lovász (1986).** $\chi\bigl(KG^r(n,k)\bigr) = \left\lceil \dfrac{n - r(k-1)}{r-1} \right\rceil$.

**Stable sets.** $A \subseteq [n]$ is *$s$-stable* if any two of its elements are at cyclic distance $\ge s$. The Schrijver graph $SG(n,k)$ is the subgraph of $KG(n,k)$ induced by $2$-stable sets.

> **Schrijver (1978).** $\chi(SG(n,k)) = n-2k+2$, and $SG(n,k)$ is vertex-critical.

**Tucker's Lemma.** For an antipodally symmetric triangulation of $B^d$ and any labelling $\lambda : V \to \{\pm 1,\dots,\pm d\}$ that is antipodal on $\partial B^d$, some edge has labels $\{j,-j\}$. This is the combinatorial equivalent of Borsuk–Ulam used by Matoušek.

## 3. History & State of the Art (SOTA)

- **1955.** Martin Kneser poses the problem as Aufgabe 360 in *Jahresbericht der DMV* 58, after observing the construction above.
- **1978.** László Lovász proves it via algebraic topology (*JCTA* 25), inventing the "topological method in combinatorics."
- **1978.** Imre Bárány gives a two-page proof from Borsuk–Ulam plus Gale's lemma (*JCTA* 25).
- **1978.** Alexander Schrijver strengthens the result to the vertex-critical stable subgraphs $SG(n,k)$.
- **1986.** Alon, Frankl, Lovász settle the $r$-uniform hypergraph version, confirming a conjecture of Erdős.
- **1988.** Dol'nikov proves the colorability-defect lower bound; Kříž (1992) gives the $r$-uniform analogue.
- **2002.** Joshua Greene gives a half-page proof (*Amer. Math. Monthly* 109) — currently the shortest.
- **2002–2004.** Matoušek gives a "combinatorial" proof via Tucker's lemma; Ziegler (*Inventiones* 148, 2002) gives combinatorial proofs of the generalized Kneser theorems using $\mathbb{Z}_p$-Tucker.
- **2007.** Babson and Kozlov prove the Lovász conjecture on Hom complexes (*Annals of Math.* 165), the deepest descendant of the method.
- **2022–2023.** Complexity-theoretic phase: Haviv shows the total search problem "given a colouring with $n-2k+1$ colours, find a monochromatic edge" is **PPA-complete**; Merino, Mütze and Namrata prove all connected Kneser graphs except the Petersen graph are Hamiltonian.

## 4. Partial Results / Verified Cases

- **$k=1$:** $KG(n,1)=K_n$, $\chi=n=n-2+2$. Trivial.
- **$n=2k$:** perfect matching on $\binom{2k}{k}$ vertices, $\chi=2$. Trivial.
- **$n=2k+1$:** odd graphs $O_{k+1}$; $\chi=3$, first nontrivial family; $KG(5,2)$ is the Petersen graph.
- **$k=2$:** $\chi(KG(n,2)) = n-2$, provable by elementary Ramsey-type arguments (the complement is the triangular graph $T(n)$).
- **Full general case:** proved (Lovász 1978), with at least five independent proofs: neighborhood complexes, Gale/Borsuk–Ulam (Bárány), $\mathbb{Z}_2$-index of box complexes, Tucker's lemma (Matoušek), and Greene's direct hemisphere argument.
- **Hypergraphs:** $\chi(KG^r(n,k))=\lceil (n-r(k-1))/(r-1)\rceil$ known for all $r \ge 2$; the original Alon–Frankl–Lovász argument runs through $r$ prime and lifts, with Ziegler's $\mathbb{Z}_p$-Tucker proof giving the combinatorial version.
- **Stable hypergraphs (partial).** Conjecture (Alon–Drewnowski–Łuczak 2009): for $s \ge r$, the $s$-stable $r$-uniform Kneser hypergraph has $\chi = \lceil (n-s(k-1))/(r-1)\rceil$. Proved for $r$ a power of $2$ (Alon–Drewnowski–Łuczak, *Proc. AMS* 137, 2009), and for $s$ large relative to $r$ by Frick's topological-Tverberg methods *(frontier — verify exact threshold)*. Open for general $r$ with $s=r$.
- **Chromatic number of $SG(n,k)$:** $n-2k+2$ for all $n \ge 2k$ (Schrijver); Björner–de Longueville (*Combinatorica* 23, 2003) showed the neighbourhood/box complex of $SG(n,k)$ is homotopy equivalent to $S^{\,n-2k}$.

## 5. Principal Obstacles

- **Topology is not removable in an obvious way.** Every known proof of the general lower bound uses Borsuk–Ulam or a discrete equivalent (Tucker, Ky Fan, Gale). Matoušek's "combinatorial proof" replaces cohomology by an explicit octahedral Tucker labelling, but the labelling argument is a transcription of the same $\mathbb{Z}_2$-index obstruction; the parity/degree information that forces a monochromatic edge has no known purely counting-based source.
- **Linear-algebraic and eigenvalue methods stop short.** The Hoffman/ratio bound gives $\chi(KG(n,k)) \ge 1 - \lambda_{\max}/\lambda_{\min} = n/k$, which is off by a factor $\approx k$ when $n \approx 2k$ — precisely the hard regime. Fractional relaxations give $\chi_f = n/k$ exactly, so the LP relaxation cannot see the answer.
- **Probabilistic and entropy methods fail.** Kneser graphs have huge independence number $\binom{n-1}{k-1}$, so counting bounds of the form $\chi \ge |V|/\alpha$ give $\approx n/k$, not $n-2k+2$. The gap is structural: extremal independent sets are stars, and one must rule out *near-star* covers, which requires stability theory beyond EKR.
- **The $\mathbb{Z}_p$ barrier for $r$ not a prime power.** For $r$-uniform generalizations the equivariant topology works with $\mathbb{Z}_p$-actions; when $r$ has several prime factors, the relevant configuration-space/test-map obstruction vanishes (as in the Mabillard–Wagner counterexamples to topological Tverberg for non-prime-powers), which is exactly why the stable hypergraph conjecture is stuck at $r$ a power of $2$.
- **Algorithmic hardness.** Finding the monochromatic edge guaranteed by the theorem is PPA-complete (Haviv, ICALP 2022), evidence that no efficient constructive/combinatorial witness-extraction procedure exists, hence no "algorithmic proof" of the type that would eliminate topology.

## 6. The Gap

The original conjecture has no gap: it is a theorem. The residual gaps are:

1. **Foundational.** Is there a proof of $\chi(KG(n,k)) \ge n-2k+2$ using only finite combinatorics — no triangulations, no antipodal maps, no parity argument equivalent to Tucker? Greene's and Matoušek's proofs are short but still fixed-point-theoretic. The precise barrier: every known argument produces the disjoint pair from a *global* topological obstruction ($\mathrm{ind}_{\mathbb{Z}_2} \mathcal{N} = n-2k$), and no local exchange/shifting argument is known to certify this quantity.
2. **Parametric.** For $s$-stable $r$-uniform Kneser hypergraphs, the proven range is $r \in \{2,4,8,16,\dots\}$ (all $s\ge r$) plus large-$s$ cases; the conjectured formula for $r=3,5,6,\dots$ with $s=r$ is unproved. The missing step is a $\mathbb{Z}_r$-equivariant obstruction valid for composite $r$.
3. **Tightness of the topological bound.** For general graphs, $\chi(G) \ge \mathrm{ind}_{\mathbb{Z}_2}(B(G))+2$ can be arbitrarily far from tight; characterizing graphs where it is tight (Kneser, Schrijver, generalized Mycielskians) remains open.

## 7. Current Research (as of June 2026)

- **Complexity of Kneser-type total search problems.** Ishay Haviv (Academic College of Tel Aviv-Yaffo) established PPA-completeness of the Kneser problem and fixed-parameter algorithms for it; ongoing work extends to Schrijver and Agreeable-Set problems *(frontier — verify)*.
- **Stable Kneser hypergraphs.** Frédéric Meunier (École des Ponts), Florian Frick (Carnegie Mellon), Hamid Reza Daneshpajouh, and the Belgrade school (Jojić, Panina, Živaljević) pursue the Alon–Drewnowski–Łuczak conjecture through constrained-Tverberg and necklace-splitting reductions.
- **Hamiltonicity and structure.** Torsten Mütze (Warwick) and coauthors resolved Hamiltonicity of Kneser graphs (STOC 2023) and continue on Hamilton cycles in Kneser-like and Johnson graphs.
- **Hom-complex / graph-homomorphism complexes.** Kozlov, Schultz, Dochtermann: refined lower bounds beyond $\mathcal{N}(G)$, and the question of which topological invariants of $\mathrm{Hom}(K_2,G)$ control $\chi$.
- **Local chromatic and circular chromatic refinements.** Simonyi and Tardos (Rényi Institute) compute local and circular chromatic numbers of Schrijver graphs via Ky Fan's theorem; sharp values in some parameter ranges remain open.

## 8. Future Work

- Seek a **shifting/compression proof** in the style of Erdős–Ko–Rado stability, aiming to convert Frankl-type stability results for intersecting families into the full lower bound.
- Develop **$\mathbb{Z}_r$-equivariant obstruction theory for composite $r$**, informed by the Mabillard–Wagner failure of topological Tverberg, to attack the stable hypergraph conjecture.
- Exploit **PPA-completeness** in reverse: reductions from Kneser to other PPA problems (Tucker, necklace splitting, consensus halving) may yield new proofs or new lower bounds.
- Push **spectral/semidefinite hierarchies**: does a bounded level of Lasserre/SOS certify $\chi(KG(n,k)) > n-2k+1$? A negative answer would formalize the "topology is necessary" intuition.
- Extend to **infinite and Borel settings**: chromatic numbers of Borel Kneser-type graphs, where Borsuk–Ulam arguments do not directly transfer.

## 9. Key References

- **[Foundational]** M. Kneser. *Aufgabe 360.* Jahresbericht der Deutschen Mathematiker-Vereinigung 58 (2. Abteilung), 27, 1955/56.
- **[Foundational]** L. Lovász. *Kneser's conjecture, chromatic number, and homotopy.* Journal of Combinatorial Theory, Series A 25(3), 319–324, 1978.
- **[Foundational]** I. Bárány. *A short proof of Kneser's conjecture.* Journal of Combinatorial Theory, Series A 25(3), 325–326, 1978.
- **[Foundational]** A. Schrijver. *Vertex-critical subgraphs of Kneser graphs.* Nieuw Archief voor Wiskunde (3) 26, 454–461, 1978.
- **[Foundational]** N. Alon, P. Frankl, L. Lovász. *The chromatic number of Kneser hypergraphs.* Transactions of the American Mathematical Society 298(1), 359–370, 1986.
- **[Short proof]** J. E. Greene. *A new short proof of Kneser's conjecture.* American Mathematical Monthly 109(10), 918–920, 2002.
- **[Combinatorial proof]** J. Matoušek. *A combinatorial proof of Kneser's conjecture.* Combinatorica 24(1), 163–170, 2004.
- **[Combinatorial proof]** G. M. Ziegler. *Generalized Kneser coloring theorems with combinatorial proofs.* Inventiones Mathematicae 147(3), 671–691, 2002.
- **[Survey / Book]** J. Matoušek. *Using the Borsuk–Ulam Theorem: Lectures on Topological Methods in Combinatorics and Geometry.* Springer, 2003.
- **[Structure]** A. Björner, M. de Longueville. *Neighborhood complexes of stable Kneser graphs.* Combinatorica 23(1), 23–34, 2003.
- **[SOTA]** N. Alon, L. Drewnowski, T. Łuczak. *Stable Kneser hypergraphs and ideals in $\mathbb{N}$ with the Nikodym property.* Proceedings of the American Mathematical Society 137(2), 467–471, 2009.
- **[SOTA]** E. Babson, D. N. Kozlov. *Proof of the Lovász conjecture.* Annals of Mathematics 165(3), 965–1007, 2007.
- **[SOTA]** A. Merino, T. Mütze, Namrata. *Kneser graphs are Hamiltonian.* Proceedings of STOC 2023, ACM, 2023.
- **[SOTA]** I. Haviv. *A fixed-parameter algorithm for the Kneser problem.* Proceedings of ICALP 2022, LIPIcs 229, 2022.
- **[Refinement]** G. Simonyi, G. Tardos. *Local chromatic number, Ky Fan's theorem, and circular colorings.* Combinatorica 26(5), 587–626, 2006.

## 10. Worked Example / Concrete Special Case

**Case $n=5$, $k=2$: the Petersen graph.**

Vertices: the ten $2$-subsets of $\{1,\dots,5\}$; edges join disjoint pairs. Kneser's formula predicts
$$\chi(KG(5,2)) = 5 - 4 + 2 = 3 .$$

*Upper bound (explicit).* Use $c(A)=\min\{\min A, 3\}$:

| colour | vertices |
|---|---|
| 1 | $12,13,14,15$ |
| 2 | $23,24,25$ |
| 3 | $34,35,45$ |

Colour 1 is a star at $1$ (intersecting). Colour 2 is a star at $2$. Colour 3 consists of pairs inside $\{3,4,5\}$, and any two $2$-subsets of a $3$-set meet. So this is a proper $3$-colouring.

*Lower bound (elementary, special to $n=5$).* By Erdős–Ko–Rado with $n=5,k=2$, a maximum independent set has size $\binom{4}{1}=4$. Two colour classes therefore cover at most $8 < 10$ vertices, so $\chi \ge 3$. Hence $\chi=3$. (Direct check: the Petersen graph contains 5-cycles, so it is not bipartite.)

*Why this argument does not generalize.* For $KG(n,k)$ the counting bound gives
$$\chi \ \ge\ \frac{\binom{n}{k}}{\binom{n-1}{k-1}} \ =\ \frac{n}{k},$$
which for $n=3k$ yields $3$ while the truth is $k+2$. At $k=10, n=30$: counting gives $3$, Kneser gives $12$.

*The topological route, on the same example.* $\mathcal{N}(KG(5,2)) \simeq S^{\,n-2k} = S^{1}$, which is $0$-connected, so Lovász's theorem gives $\chi \ge 0+3 = 3$. Equivalently, via Bárány: take $5$ points on $S^{1}$ in general position (Gale's lemma: every open half-circle contains $\ge 2$ of them). A proper $2$-colouring would give two closed sets covering $S^1$ with no antipodal pair in either — contradicting the Borsuk–Ulam theorem for $d=1$. The topological argument scales with $n-2k$; the counting argument does not.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*