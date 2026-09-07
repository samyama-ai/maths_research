---
id: 04-topology/bings-recognition-problem
title: "Bing's Recognition Problem"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bing's Recognition Problem

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/bings-recognition-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Bing's recognition problem asks for an intrinsic, checkable criterion that certifies when a given space is the $n$-sphere, or more generally a manifold. It has two live formulations, both open.

**(R1) Algorithmic form.** Is there an algorithm that, given a finite simplicial complex $K$ known to be a closed PL $4$-manifold, decides whether $|K| \cong S^4$? Equivalently: is $S^4$-recognition decidable? A solution is a terminating procedure with a proof of correctness; a disproof is a reduction from a known undecidable problem (e.g. triviality of finitely presented groups) that stays inside the class of $4$-manifold triangulations.

**(R2) Topological (Bing–Borsuk) form.** Is every homogeneous, finite-dimensional absolute neighborhood retract (ANR) of dimension $n$ a topological $n$-manifold? Here *homogeneous* means: for all $x,y \in X$ there is a homeomorphism $h : X \to X$ with $h(x)=y$. Open for all $n \ge 3$.

Both descend from R. H. Bing's 1958 theorem, which solved the $3$-dimensional case of the sphere-recognition question by a purely intrinsic curve condition. The open problem is to extend either the criterion (R2) or its effective content (R1) beyond the dimensions where it is known.

**Auxiliary open form (R3).** Even where recognition is decidable ($n=3$), no polynomial-time algorithm is known: $S^3$-recognition is in $\mathbf{NP}$, and in $\mathbf{co\text{-}NP}$ only under GRH.

## 2. Mathematical Foundations

**Bing's criterion.** A compact, connected $3$-manifold $M$ without boundary is homeomorphic to $S^3$ if and only if every simple closed curve $J \subset M$ lies in a topological $3$-ball $B \subset M$ (Bing 1958). Formally,
$$M \cong S^3 \iff \forall J \hookrightarrow M \ \exists B \subset M,\ B \cong \mathbb{B}^3,\ J \subset \operatorname{int} B .$$
The condition is *intrinsic* (no embedding, no smooth structure) but not *effective*: it quantifies over all curves and all wild balls.

**Homology manifolds.** A locally compact space $X$ is a *homology $n$-manifold* if for all $x \in X$
$$H_k(X, X \setminus \{x\}; \mathbb{Z}) \cong H_k(\mathbb{R}^n, \mathbb{R}^n \setminus \{0\}; \mathbb{Z}) = \begin{cases} \mathbb{Z} & k=n\\ 0 & k \ne n.\end{cases}$$

**Disjoint Disks Property (DDP).** $X$ satisfies DDP if for every $\varepsilon>0$ and maps $f,g : \mathbb{B}^2 \to X$ there are $f',g'$ with $\sup d(f,f') , \sup d(g,g') < \varepsilon$ and $f'(\mathbb{B}^2) \cap g'(\mathbb{B}^2) = \emptyset$.

**Edwards–Cannon recognition theorem.** For $n \ge 5$, a resolvable homology $n$-manifold $X$ (an ANR) is a topological $n$-manifold iff $X$ has the DDP. Combined with the topological Poincaré conjecture in those dimensions,
$$X \simeq S^n,\ X \text{ a resolvable homology } n\text{-manifold with DDP} \implies X \cong S^n \quad (n \ge 5).$$

**Quinn's resolution obstruction.** For a connected homology $n$-manifold $X$, $n \ge 5$, there is $i(X) \in 1 + 8\mathbb{Z}$ with $X$ resolvable (i.e. admitting a cell-like map $M \to X$ from a manifold) iff $i(X)=1$. Bryant–Ferry–Mio–Weinberger constructed homology manifolds with $i(X) \ne 1$ that satisfy DDP and are not manifolds, so DDP alone does not recognize manifolds among homology manifolds.

**Algorithmic setting.** Input is a finite simplicial complex, or equivalently a triangulation with $t$ tetrahedra / $t$ $4$-simplices. Two PL manifolds are homeomorphic iff related by a finite sequence of Pachner (bistellar) moves; recognition is decidable iff the number of moves is bounded by a computable function of $t$.

## 3. History & State of the Art (SOTA)

- **1952.** Bing shows $S^3$ is the union of two solid Alexander horned spheres, proving that "recognition" cannot be by tameness of a splitting sphere.
- **1957.** Bing's *dogbone space*: a cell-like decomposition of $\mathbb{R}^3$ whose quotient is not $\mathbb{R}^3$ — cell-like maps do not preserve manifolds.
- **1958.** Bing's characterization theorem (the curve criterion above), the founding result.
- **1965.** Bing–Borsuk prove homogeneous ANRs of dimension $\le 2$ are manifolds; conjecture the general case.
- **1974–79.** Cannon's double-suspension work and Edwards' theorem: the double suspension of any homology $3$-sphere is $S^5$; the DDP recognition theorem for $n \ge 5$.
- **1983.** Quinn's resolution obstruction; Freedman's classification supplies topological $4$-dimensional Poincaré.
- **1992–94.** Rubinstein's almost-normal-surface algorithm, made rigorous by Thompson (thin position) and Casson: **$S^3$-recognition is decidable**.
- **1996.** Bryant–Ferry–Mio–Weinberger: exotic homology manifolds exist in every dimension $\ge 6$.
- **2011–2021.** Complexity: Schleimer puts sphere recognition in $\mathbf{NP}$; Kuperberg's GRH-conditional framework and Zentner's $SL(2,\mathbb{C})$ theorem give $\mathbf{co\text{-}NP}$ under GRH; Lackenby removes GRH for knottedness. Kuperberg (2019) gives elementary-recursive bounds for the whole $3$-manifold homeomorphism problem via geometrization.
- **Undecidable side.** Markov (1958) and Novikov: for $n \ge 5$, recognizing $S^n$ among triangulated $n$-manifolds is algorithmically unsolvable; Chernavsky–Leksine sharpen the unrecognizability statements.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $n \le 2$, Bing–Borsuk | **True** (Bing–Borsuk 1965) |
| $n=3$, sphere characterization | **True** (Bing 1958); also via geometrization |
| $n=3$, algorithmic recognition | **Decidable** (Rubinstein 1992, Thompson 1994) |
| $n=3$, complexity | in $\mathbf{NP}$ (Schleimer); $\mathbf{co\text{-}NP}$ under GRH; $\mathbf{P}$ open |
| $n=4$, algorithmic recognition | **Open** |
| $n \ge 5$, algorithmic recognition | **Undecidable** (Novikov) |
| $n \ge 5$, topological recognition | **Solved**: resolvable homology manifold $+$ DDP (Cannon 1979, Edwards 1978) |
| $n \ge 6$, homology manifolds generally | **False** without resolvability (BFMW 1996) |
| $n=3$, Bing–Borsuk | Open; implies Poincaré (Jakobsche 1980), hence not disproved by Perelman |
| $n \ge 4$, Bing–Borsuk | Open |
| Homogeneous ANR $\Rightarrow$ homology manifold | Known for $n\le 2$; open in general |

Concrete verified instances: every triangulated homotopy $3$-sphere with $\le$ a few hundred tetrahedra has been certified $S^3$ by Regina's implementation of Rubinstein–Thompson; the double suspension $\Sigma^2 \Sigma(2,3,5) \cong S^5$ is the canonical verified non-PL instance of recognition.

## 5. Principal Obstacles

- **Wildness.** Bing's criterion quantifies over *topological* balls, including wild ones (horned spheres, dogbone decompositions). No finite combinatorial certificate is known for "$J$ lies in a ball" that survives wildness, so the criterion resists effectivization.
- **Group theory blocks dimension 4.** A triangulated homotopy $4$-sphere is $S^4$ by Freedman, so $S^4$-recognition reduces to deciding $\pi_1(K) = 1$. The triviality problem for finitely presented groups is undecidable (Adian–Rabin), and no one knows how to exploit the extra constraint that the presentation comes from a $4$-manifold spine. The standard reduction that kills $n \ge 5$ needs a $\ge 5$-dimensional handle to embed arbitrary presentations; in dimension $4$ the embedding is obstructed by Whitney-trick failure.
- **Normal surface theory does not lift.** Rubinstein–Thompson relies on almost normal $2$-spheres and thin position for Heegaard splittings; there is no $4$-dimensional analogue with a finite Haken hierarchy, and the number of normal hypersurfaces in dimension $4$ is not bounded by the same linear-programming argument.
- **DDP is a $2$-disk condition.** General position of $2$-disks needs $2+2 < n$, i.e. $n\ge5$. In $n=4$ disks generically intersect, so the Cannon–Edwards machinery has no room.
- **Resolution obstruction is invisible locally.** $i(X) \in 1+8\mathbb{Z}$ is a global surgery-theoretic invariant; no local criterion detects it, so "homology manifold + DDP" cannot be repaired by adding local conditions.
- **Homogeneity is weak.** For Bing–Borsuk one cannot even show a homogeneous ANR is a homology manifold; the local structure could a priori vary in an uncontrolled way among homeomorphic pieces.

## 6. The Gap

Proven: recognition is intrinsic in $n=3$ (curve criterion), effective in $n=3$ (Rubinstein–Thompson), local-plus-DDP in $n\ge5$, impossible in $n\ge5$ algorithmically. The gap is the codimension-$\le 2$ zone.

Precisely, for (R1) the missing step is a computable bound $f(t)$ on the number of Pachner moves needed to reduce a $t$-simplex triangulation of $S^4$ to the boundary of the $5$-simplex — equivalently a computable bound on the length of an $AC$-trivialization of a $4$-manifold group presentation. Nothing rules such a bound out; nothing supplies it.

For (R2) the missing step in $n=3$ is: show a homogeneous ANR $X^3$ is a homology $3$-manifold, then apply geometrization. Even homogeneity $\Rightarrow$ local homology constancy is unproved.

## 7. Current Research (as of June 2026)

- **Complexity of $3$-sphere recognition.** Lackenby and Schleimer's programme on efficient certificates for elliptic manifolds aims to place $S^3$-recognition in $\mathbf{NP} \cap \mathbf{co\text{-}NP}$ unconditionally, removing the GRH hypothesis inherited from Kuperberg–Zentner *(frontier — verify)*. Oxford, Warwick, UC Davis.
- **Fixed-parameter tractability.** Burton, Maria and collaborators (Queensland, INRIA) push treewidth-parameterized algorithms in Regina; sphere recognition is FPT in the treewidth of the dual graph *(frontier — verify)*.
- **Bing–Borsuk / Busemann.** Repovš, Halverson, Bryant and the Ljubljana–Binghamton circle continue work on homogeneity implying local homology constancy, and on the equivalent Moore-type conditions.
- **Exotic homology manifolds.** Ferry, Mio, Weinberger and successors ask whether BFMW spaces are homogeneous — an affirmative answer in dimension $\ge 6$ would *disprove* Bing–Borsuk there and is the most likely route to a counterexample.
- **Dimension 4.** Interaction with the smooth $4$-dimensional Poincaré conjecture: Gompf's and Manolescu–Piccirillo's potential counterexample families give explicit homotopy $4$-spheres whose recognizability is the practical test case.

## 8. Future Work

- Prove or refute a computable Pachner-move bound for $S^4$; even a bound conditional on the smooth $4$-dimensional Poincaré conjecture would be a first.
- Isolate the class of group presentations arising as spines of triangulated homotopy $4$-spheres and decide triviality within it (Andrews–Curtis-adjacent).
- Establish "homogeneous ANR $\Rightarrow$ homology manifold" in dimension $3$; this is the whole content of Bing–Borsuk there.
- Test the homogeneity of BFMW exotic homology manifolds; a homogeneous example settles (R2) negatively for $n\ge6$.
- Derandomize / de-GRH the $\mathbf{co\text{-}NP}$ certificate for non-$S^3$ using $SU(2)$ representation counts.

## 9. Key References

- **[Foundational]** R. H. Bing. *Necessary and sufficient conditions that a 3-manifold be $S^3$.* Annals of Mathematics **68** (1958), 17–37.
- **[Foundational]** R. H. Bing. *A homeomorphism between the 3-sphere and the sum of two solid horned spheres.* Annals of Mathematics **56** (1952), 354–362.
- **[Foundational]** R. H. Bing, K. Borsuk. *Some remarks concerning topologically homogeneous spaces.* Annals of Mathematics **81** (1965), 100–111.
- **[Foundational]** J. W. Cannon. *Shrinking cell-like decompositions of manifolds. Codimension three.* Annals of Mathematics **110** (1979), 83–112.
- **[Foundational]** R. D. Edwards. *The topology of manifolds and cell-like maps.* Proceedings of the ICM, Helsinki 1978, 111–127.
- **[Foundational]** F. Quinn. *Resolutions of homology manifolds, and the topological characterization of manifolds.* Inventiones Mathematicae **72** (1983), 267–284; erratum **85** (1986), 653.
- **[SOTA]** J. Bryant, S. Ferry, W. Mio, S. Weinberger. *Topology of homology manifolds.* Annals of Mathematics **143** (1996), 435–467.
- **[SOTA]** J. H. Rubinstein. *An algorithm to recognize the 3-sphere.* Proceedings of the ICM, Zürich 1994, 601–611.
- **[SOTA]** A. Thompson. *Thin position and the recognition problem for $S^3$.* Mathematical Research Letters **1** (1994), 613–630.
- **[SOTA]** S. Schleimer. *Sphere recognition lies in NP.* In *Low-dimensional and Symplectic Topology*, Proc. Sympos. Pure Math. **82**, AMS, 2011, 183–213.
- **[SOTA]** G. Kuperberg. *Algorithmic homeomorphism of 3-manifolds as a corollary of geometrization.* Pacific Journal of Mathematics **301** (2019), 189–241.
- **[SOTA]** M. Lackenby. *The efficient certification of knottedness and Thurston norm.* Advances in Mathematics **387** (2021), 107796.
- **[Recent]** R. Zentner. *Integer homology 3-spheres admit irreducible representations in $SL(2,\mathbb{C})$.* Journal of the London Mathematical Society **98** (2018), 577–595.
- **[Survey]** R. J. Daverman. *Decompositions of Manifolds.* Academic Press, 1986.
- **[Survey]** D. Halverson, D. Repovš. *The Bing–Borsuk and the Busemann conjectures.* Mathematical Communications **13** (2008), 163–184.
- **[Survey]** R. H. Bing. *The Geometric Topology of 3-Manifolds.* AMS Colloquium Publications **40**, 1983.
- **[Related]** W. Jakobsche. *The Bing–Borsuk conjecture is stronger than the Poincaré conjecture.* Fundamenta Mathematicae **106** (1980), 127–134.
- **[Related]** J. Hass, J. Lagarias, N. Pippenger. *The computational complexity of knot and link problems.* Journal of the ACM **46** (1999), 185–211.

## 10. Worked Example / Concrete Special Case

**The double suspension of the Poincaré homology sphere.** Let $\Sigma = \Sigma(2,3,5)$, the Brieskorn sphere $\{z_1^2+z_2^3+z_3^5=0\} \cap S^5$. Facts:
$$\pi_1(\Sigma) \cong 2I,\quad |2I| = 120, \qquad H_*(\Sigma;\mathbb{Z}) \cong H_*(S^3;\mathbb{Z}).$$

*Single suspension.* $S\Sigma$ has, at each cone point $c$, link $\Sigma$. Local homology is correct:
$$H_k(S\Sigma, S\Sigma \setminus \{c\}) \cong \tilde H_{k-1}(\Sigma) = \begin{cases}\mathbb{Z} & k=4\\ 0 & \text{else,}\end{cases}$$
so $S\Sigma$ *is* a homology $4$-manifold. But $S\Sigma \setminus \{c\} \simeq \Sigma$ is not simply connected, whereas $\mathbb{R}^4$ minus a point is. Hence $S\Sigma \not\cong S^4$: it is not even locally Euclidean at $c$. Local homology does not recognize manifolds.

*Double suspension.* $X = S^2\Sigma = \Sigma^2\Sigma$. Its singular set is the suspension circle $S^1$. For $x$ on that circle the link is $S\Sigma$, again not a manifold, so $X$ has no PL manifold structure. Yet:
1. $X$ is a homology $5$-manifold (suspension raises local homology degree twice).
2. $X$ is simply connected: $\pi_1$ of a suspension of a connected space is trivial, and $X \setminus S^1 \cong \Sigma \times \mathbb{R}^2$ glues to give $\pi_1(X)=1$.
3. $X$ is resolvable: the map $\Sigma^2\Sigma \leftarrow$ (mapping cylinder construction) collapsing $\Sigma \times \{pt\}$ is cell-like, so $i(X)=1$.
4. $X$ satisfies DDP: two $2$-disks can be pushed off the $1$-dimensional singular set inside a $5$-manifold since $2+1 < 5$ generically, and Cannon's shrinking argument handles the rest.

By the Edwards–Cannon theorem, $X \cong S^5$. So $S^5$ has a triangulation that is not a combinatorial manifold — the sphere is recognized topologically but not PL-locally.

**What this shows about the open problem.** In dimension $5$ the criterion "resolvable homology manifold $+$ DDP" is a complete, checkable recognition. Drop to dimension $4$: the same construction $S\Sigma$ gives a homology $4$-manifold that fails to be a manifold, but DDP is unavailable ($2+2 = 4$), and no substitute condition is known. Drop to the algorithmic setting: even for an honest triangulated $4$-manifold $K$ with $\pi_1(K)$ given by, say, the presentation $\langle a,b \mid aba^{-1}=b^2,\ bab^{-1}=a^2\rangle$ (trivial group, but only after a nonobvious derivation), deciding triviality is exactly the step no algorithm currently bounds. That single undecided step is the whole of the Gap in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*