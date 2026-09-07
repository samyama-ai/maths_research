---
id: 02-algebra-group-theory/days-conjecture
title: "Day's Conjecture"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Day's Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/days-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Day's Conjecture (formulated by Mahlon M. Day in 1957) postulates a profound structural dichotomy in geometric group theory regarding the nature of amenability. It asserts that the class of all amenable groups, denoted $AG$, is exactly equal to the class of elementary amenable groups, denoted $EG$. Formally, the conjecture states:
$$ AG = EG $$

A closely related and historically intertwined statement, often called the **von Neumann–Day Conjecture**, posited that a group is non-amenable if and only if it contains a free subgroup of rank two, $F_2$. 

While both conjectures have been globally disproved in their absolute universal forms (by Grigorchuk and Ol'shanskii, respectively), Day's Conjecture $AG = EG$ remains one of the most vital classification frameworks in modern algebra. It is considered "partially solved" because it has been proven rigorously true for nearly all classically studied geometric and algebraic classes of groups (such as linear groups, hyperbolic groups, and $3$-manifold groups). The active frontier consists of isolating the exact finiteness properties or geometric actions that force an amenable group to be elementary amenable.

## 2. Mathematical Foundations

The conjecture relies on the tension between an analytical property ($AG$) and a transfinite algebraic construction ($EG$).

**Amenable Groups ($AG$):**
Let $\Gamma$ be a discrete group, and $\ell^\infty(\Gamma)$ be the Banach space of bounded real-valued functions on $\Gamma$. A group $\Gamma$ is amenable if it admits a left-invariant mean; that is, a continuous linear functional $\mu: \ell^\infty(\Gamma) \to \mathbb{R}$ such that:
1. $\mu(1) = 1$ (Normalization)
2. $\mu(f) \ge 0$ for all $f \ge 0$ (Positivity)
3. $\mu(g \cdot f) = \mu(f)$ for all $g \in \Gamma$, $f \in \ell^\infty(\Gamma)$, where $(g \cdot f)(x) = f(g^{-1}x)$ (Left-invariance).

Equivalently, by the Følner Condition, $\Gamma$ is amenable if and only if for every finite subset $S \subset \Gamma$ and every $\epsilon > 0$, there exists a finite subset $F \subset \Gamma$ such that:
$$ \frac{|S F \setminus F|}{|F|} < \epsilon $$

Furthermore, by Kesten's Criterion, a finitely generated group with symmetric generating set $S$ is amenable if and only if the spectral radius of its simple random walk operator satisfies $\rho(M_S) = 1$.

**Elementary Amenable Groups ($EG$):**
The class $EG$ is the smallest class of groups satisfying a strict algebraic hierarchy, formalized by C. Chou. It is built transfinitely:
- **Base Step ($EG_0$):** Let $EG_0$ be the class of all finite groups and all abelian groups.
- **Successor Ordinals ($EG_{\alpha+1}$):** A group $G \in EG_{\alpha+1}$ if it can be constructed from groups in $EG_\alpha$ via group extensions (i.e., there exists a short exact sequence $1 \to N \to G \to Q \to 1$ with $N, Q \in EG_\alpha$) or quotients.
- **Limit Ordinals ($EG_\lambda$):** For a limit ordinal $\lambda$, $EG_\lambda = \bigcup_{\alpha < \lambda} EG_\alpha$, along with closure under directed unions.

Then $EG = \bigcup_{\alpha} EG_\alpha$. Day's Conjecture posited that the purely algebraic transfinite closure $EG$ exhausts the analytic definition of $AG$.

## 3. History & State of the Art (SOTA)

The concept of amenability was introduced by John von Neumann in 1929 to isolate the algebraic reason behind the Banach-Tarski paradox. In 1957, Mahlon M. Day coined the English term "amenable," systematized the theory, and explicitly formulated both the $AG=EG$ conjecture and the $F_2$ dichotomy conjecture. 

For decades, the conjecture drove the classification of groups. In 1980, Ching Chou rigorously defined the transfinite hierarchy of $EG$ and proved that any finitely generated group in $EG$ has either polynomial or exponential word growth. 

This set the stage for the conjecture's universal disproof. In 1984, Rostislav Grigorchuk published the first construction of a group of *intermediate* growth (growing faster than any polynomial, but slower than any exponential). Because its growth is subexponential, it satisfies the Følner condition and is amenable ($G \in AG$). Because it has intermediate growth, by Chou's theorem, it cannot be elementary amenable ($G \notin EG$).

In 2013, Kate Juschenko and Nicolas Monod provided another profound counterexample by proving that the topological full groups of Cantor minimal systems are amenable. These groups contain finitely generated infinite simple groups. Since an infinite simple group cannot be built via non-trivial extensions, it cannot belong to $EG$, creating a vastly different class of $AG \setminus EG$ groups.

## 4. Partial Results / Verified Cases

Despite the existence of exotic counterexamples, Day's Conjecture is rigorously proven for the most fundamental classes of groups studied in geometry and topology. In these domains, the structural gap vanishes:

- **Linear Groups:** By the Tits Alternative (1972), any finitely generated subgroup of $GL(n, K)$ over a field of characteristic zero either contains a free subgroup $F_2$ (hence is non-amenable) or is virtually solvable (hence belongs to $EG_1 \subset EG$). Therefore, for linear groups, $AG = EG$.
- **$3$-Manifold Groups:** Following Perelman's proof of the Geometrization Conjecture, the fundamental group of any compact $3$-manifold satisfies Day's conjecture.
- **Non-Positively Curved Groups:** The conjecture holds for CAT(0) cubical groups, Right-Angled Artin Groups (RAAGs), and Gromov hyperbolic groups.
- **One-Relator Groups:** All one-relator groups satisfy the property that if they are amenable, they are in fact elementary amenable (specifically, they are solvable).

## 5. Principal Obstacles

The fundamental obstacle to resolving Day's Conjecture for arbitrary finitely presented groups lies in the divergence between **geometric word growth** and **homological extensions**. 

To prove a group belongs to $EG$, one must construct it via exact sequences, meaning the group must have non-trivial normal subgroups. However, analytic amenability only requires the existence of highly "folded" finite subgraphs in the Cayley graph (Følner sets) that trap random walks.

The current mathematical bottleneck is that algebraic topology (via classifying spaces $B\Gamma$ and bounded cohomology) easily captures the extension theory of $EG$, but fails to measure the asymptotic geometry of Følner sets in non-linear groups. For instance, Grigorchuk's group is constructed via automata acting on rooted binary trees. Its elements are defined self-similarly. Standard cohomological tools fail because self-similarity bypasses the need for finite-index or solvable quotients, allowing a group to weave a Følner sequence without producing the normal subgroups necessary to climb Chou's ordinal hierarchy.

## 6. The Gap

The boundary between what is known (Section 4) and the general landscape (Section 3) defines "The Gap". The precise mathematical barrier is determining *which topological or finiteness properties* force $AG = EG$. 

Specifically, the gap is localized around geometric finiteness. Grigorchuk's original group of intermediate growth is finitely generated, but *not* finitely presented. While finitely presented counterexamples to $AG=EG$ are now known, it remains an open question whether Day's conjecture holds for groups with finite asymptotic dimension, or groups of type $F_\infty$ that act properly and cocompactly on contractible finite-dimensional CW-complexes. The gap is the bridge between wild self-similar actions and classical geometric actions.

## 7. Current Research (as of June 2026)

Active research continues to map the boundary between $AG$ and $EG$:

- **Thompson's Group $F$:** The most famous open problem in this space is the amenability of Thompson's Group $F$. It is known that $F \notin EG$ and $F$ does not contain $F_2$. If $F$ is amenable, it is a finitely presented, torsion-free counterexample to Day's Conjecture. If it is non-amenable, it violates the von Neumann-Day conjecture. Researchers are currently using massive computational cluster analyses of random walk spectral radii $\rho(M_S)$ to bound the amenability of $F$. *(frontier — verify)*.
- **Extensive Amenability:** A property introduced by Juschenko and collaborators, generalizing amenability to group actions on spaces, which successfully identifies why certain topological full groups are amenable without being in $EG$.
- **Quantitative Amenability:** Measuring the gap between $AG$ and $EG$ using the *Følner function* $F(n)$, which bounds the size of the Følner set required for a given error tolerance $\epsilon = 1/n$. Groups in $EG$ have heavily constrained Følner functions, while groups in $AG \setminus EG$ can exhibit Ackermannian Følner growth.

## 8. Future Work

Leading mathematicians have outlined several core pathways to advance the program:
1. **Finitely Presented Simple Amenable Groups:** While Juschenko and Monod found finitely generated simple amenable groups, finding a *finitely presented* infinite simple amenable group remains the holy grail. Such a group would maximally violate $EG$, as it would have no non-trivial quotients or subgroups to initiate Chou's hierarchy.
2. **Gap Theorems for Word Growth:** Proving whether a gap exists between polynomial growth (which implies $EG$) and the specific intermediate growth rate of $e^{\sqrt{n}}$ discovered by Grigorchuk. 
3. **Decidability:** Determining if there exists an algorithm to decide whether a given finitely presented amenable group belongs to $EG$. 

## 9. Key References

- **[Foundational]** Day, M. M. *Amenable semigroups.* Illinois Journal of Mathematics, 1957.
- **[Foundational]** Tits, J. *Free subgroups in linear groups.* Journal of Algebra, 1972.
- **[Foundational]** Chou, C. *Elementary amenable groups.* Illinois Journal of Mathematics, 1980.
- **[Foundational]** Grigorchuk, R. I. *Degrees of growth of finitely generated groups and the theory of invariant means.* Izvestiya Akademii Nauk SSSR Seriya Matematicheskaya, 1984.
- **[SOTA / Recent]** Juschenko, K., & Monod, N. *Cantor systems, piecewise translations and simple amenable groups.* Annals of Mathematics, 2013.

## 10. Worked Example / Concrete Special Case

To understand how Day's conjecture functions successfully in classical algebra, consider the **discrete Heisenberg group** $H_3(\mathbb{Z})$. We will show it is elementary amenable ($H_3(\mathbb{Z}) \in EG$), which immediately guarantees its amenability.

$H_3(\mathbb{Z})$ is the group of $3 \times 3$ upper triangular matrices with integer entries and ones on the diagonal:
$$ H_3(\mathbb{Z}) = \left\{ \begin{pmatrix} 1 & x & z \\ 0 & 1 & y \\ 0 & 0 & 1 \end{pmatrix} \mathrel{\bigg|} x, y, z \in \mathbb{Z} \right\} $$

It is generated by the elements $X$ (where $x=1, y=0, z=0$) and $Y$ (where $x=0, y=1, z=0$). The commutator $Z = [X,Y] = X^{-1}Y^{-1}XY$ yields the matrix with $z=1$, which generates the center of the group, $Z(H_3)$.

**Step 1:** The center $Z(H_3) \cong \mathbb{Z}$. Since $\mathbb{Z}$ is abelian, it belongs to the base class $EG_0$.
**Step 2:** The quotient group $H_3(\mathbb{Z}) / Z(H_3)$ effectively kills the $z$ coordinate, leaving the independent $x$ and $y$ coordinates. Thus, the quotient is isomorphic to the free abelian group $\mathbb{Z}^2$. Since $\mathbb{Z}^2$ is abelian, it also belongs to $EG_0$.
**Step 3:** By the definition of the $EG$ hierarchy, any extension of a group in $EG_0$ by a group in $EG_0$ belongs to $EG_1$. 
Since we have the short exact sequence:
$$ 1 \to Z(H_3) \to H_3(\mathbb{Z}) \to \mathbb{Z}^2 \to 1 $$
where both the kernel and quotient are in $EG_0$, it follows that $H_3(\mathbb{Z}) \in EG_1 \subset EG$.

Because $H_3(\mathbb{Z})$ is in $EG$, it must be amenable. Geometrically, this is confirmed because the word growth of $H_3(\mathbb{Z})$ is polynomial of degree $d = 4$ (via the Bass-Guivarc'h formula). Hence, the ratio of the boundary of a ball to its volume decays as $O(n^3)/O(n^4) = 1/n \to 0$, providing an explicit Følner sequence and physically verifying Day's Conjecture for this space.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*