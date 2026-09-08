---
id: 03-geometry/rokhlin-conjecture
title: "Rokhlin Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rokhlin Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/rokhlin-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The name attaches to the bounding problem for homology 3-spheres. In its naive form:

> **(R-naive)** Every smooth oriented integral homology 3-sphere $\Sigma$ bounds a smooth compact contractible 4-manifold.

Two facts fix its status immediately.

- **True topologically.** Freedman (1982): every homology 3-sphere bounds a compact contractible *topological* 4-manifold.
- **False smoothly.** Rokhlin's own 1952 signature theorem obstructs it: the Poincaré sphere $\Sigma(2,3,5)$ bounds no smooth acyclic 4-manifold (Section 10).

What remains open, and is the live content of the problem, is the smooth classification it was meant to assert:

> **(R)** Characterize the smooth homology 3-spheres bounding a smooth compact contractible (equivalently, for the classification purpose, acyclic) 4-manifold. Equivalently: compute the homology cobordism group $\Theta^3_{\mathbb Z}$ and decide whether the Rokhlin invariant together with gauge-theoretic invariants is a complete obstruction. Two sub-questions are open in the sharpest form: (i) is $\Theta^3_{\mathbb Z}$ torsion-free? (ii) does every $\Sigma$ bounding a smooth homology 4-ball bound a smooth contractible 4-manifold?

A resolution means either an algorithmic/structural characterization of the bounding class, or a proof that $\Theta^3_{\mathbb Z}$ is torsion-free (or a torsion element), with all invariants used defined on smooth 4-manifolds.

## 2. Mathematical Foundations

**Homology sphere.** A closed oriented smooth 3-manifold $\Sigma$ with $H_*(\Sigma;\mathbb Z)\cong H_*(S^3;\mathbb Z)$. Such $\Sigma$ has a unique spin structure and $H^2(\Sigma;\mathbb Z)=0$.

**Rokhlin's theorem (1952).** If $X$ is a closed smooth spin 4-manifold then
$$\sigma(X)\equiv 0 \pmod{16},$$
where $\sigma$ is the signature of the intersection form $Q_X$ on $H_2(X;\mathbb Z)/\mathrm{Tors}$. Equivalently, an even unimodular form realized by a closed *smooth* 4-manifold has signature divisible by $16$, though $E_8$ has $\sigma=-8$ and is realized topologically.

**Rokhlin invariant.** Every homology 3-sphere bounds a smooth compact spin 4-manifold $W$ (e.g. via surgery on a knot with even framing). Set
$$\mu(\Sigma)\;=\;\frac{\sigma(W)}{8}\ \bmod 2\ \in\ \mathbb Z/2 .$$
Well-definedness: two fillings glue to a closed smooth spin $X$ with $\sigma(X)\equiv 0\ (16)$, so $\sigma(W)/8$ is well defined mod $2$.

**Homology cobordism.** $\Sigma_0\sim\Sigma_1$ if there is a smooth compact oriented $W^4$ with $\partial W=(-\Sigma_0)\sqcup\Sigma_1$ and $H_*(W;\mathbb Z)\cong H_*(\Sigma_0\times[0,1];\mathbb Z)$. The set of classes forms an abelian group
$$\Theta^3_{\mathbb Z}\quad\text{under connected sum},\qquad -[\Sigma]=[-\Sigma],\quad 0=[S^3].$$
$[\Sigma]=0$ iff $\Sigma$ bounds a smooth homology 4-ball. The Rokhlin invariant descends to a surjective homomorphism $\mu:\Theta^3_{\mathbb Z}\to\mathbb Z/2$.

**Brieskorn spheres.** For pairwise coprime $p,q,r\ge 2$,
$$\Sigma(p,q,r)=\{(x,y,z)\in\mathbb C^3: x^p+y^q+z^r=0\}\cap S^5,$$
a Seifert-fibered homology sphere bounding the canonical negative-definite plumbing $P(p,q,r)$, whence $\mu(\Sigma)=\sigma(P)/8 \bmod 2$.

**Casson invariant.** $\lambda:\Theta^3_{\mathbb Z}\to\mathbb Z$ (Casson 1985; Akbulut–McCarthy 1990), a signed count of irreducible $SU(2)$ representations of $\pi_1\Sigma$, satisfying $\lambda(\Sigma)\equiv\mu(\Sigma)\pmod 2$.

**Floer-theoretic obstructions.** Frøyshov's $h$, the Heegaard Floer correction term $d$ with $\tfrac12 d(\Sigma)\equiv\mu(\Sigma)\pmod 2$ (Ozsváth–Szabó 2003), and Manolescu's $\mathrm{Pin}(2)$-equivariant invariants $\alpha\ge\beta\ge\gamma$ with $\beta\equiv\mu \pmod 2$ and $\beta(-\Sigma)=-\beta(\Sigma)$.

## 3. History & State of the Art (SOTA)

- **1952.** Rokhlin proves $16\mid\sigma$ for closed smooth spin 4-manifolds — the first purely smooth 4-dimensional obstruction.
- **1960s.** Kervaire–Milnor exploit the theorem for the non-smoothability of characteristic surfaces; the $\mu$-invariant becomes standard. The naive bounding statement circulates as folklore (later Kirby's problem list), motivated by Mazur's and Poénaru's contractible 4-manifolds.
- **1979–1984.** Akbulut–Kirby show $\Sigma(2,5,7)$ and $\Sigma(3,4,5)$ bound Mazur manifolds; Casson–Harer produce infinite families of Brieskorn spheres bounding contractible 4-manifolds; Fickle adds knot-theoretic families.
- **1982.** Freedman: topological version true; $E_8$-manifold exists topologically, so smoothness is essential in Rokhlin's theorem.
- **1985–1990.** Gauge theory kills any hope of a $\mu$-only answer. Fintushel–Stern's $R$-invariant shows $\Sigma(2,3,5)$, $\Sigma(2,3,7)$ have infinite order; Furuta (1990) and Fintushel–Stern (1990) prove $\Theta^3_{\mathbb Z}\supseteq\mathbb Z^\infty$.
- **2002–2003.** Frøyshov's $h$ and the Ozsváth–Szabó $d$-invariant give computable $\mathbb Z$-valued homomorphisms; $\Theta^3_{\mathbb Z}$ has a $\mathbb Z$ summand.
- **2016.** Manolescu's $\mathrm{Pin}(2)$-equivariant Seiberg–Witten Floer homology shows no $\Sigma$ with $\mu(\Sigma)=1$ has order 2 in $\Theta^3_{\mathbb Z}$, disproving the triangulation conjecture in dimensions $\ge 5$ (via Galewski–Stern/Matumoto).
- **2021.** Dai–Hom–Stoffregen–Truong: $\Theta^3_{\mathbb Z}$ contains a $\mathbb Z^\infty$ *summand* (involutive Heegaard Floer).

## 4. Partial Results / Verified Cases

- **Topological category: complete.** Freedman (1982) — every homology 3-sphere bounds a contractible topological 4-manifold; the smooth question is the only remainder.
- **Positive smooth families.** $\Sigma(2,5,7)$, $\Sigma(3,4,5)$ bound Mazur manifolds (Akbulut–Kirby 1979). Casson–Harer (1981): $\Sigma(p,ps-1,ps+1)$ and $\Sigma(p,ps+1,ps+2)$ (suitable parities) bound smooth contractible 4-manifolds. All $(\pm1)$-surgeries on slice knots bound homology balls.
- **Negative results.** $\mu=1\Rightarrow$ bounds no smooth acyclic 4-manifold: $\Sigma(2,3,5)$, $\Sigma(2,3,7)$, and every $\Sigma(2,3,6n\pm1)$ with odd $\sigma(P)/8$.
- **Beyond $\mu$.** $\Sigma(2,3,5)\\#\Sigma(2,3,5)$ has $\mu=0$ yet infinite order (Fintushel–Stern 1985), so $\mu$ is far from complete.
- **Group structure known so far.** $\mathbb Z^\infty\subseteq\Theta^3_{\mathbb Z}$ (Furuta 1990); $\mathbb Z$ summand (Frøyshov 2002); $\mathbb Z^\infty$ summand (DHST 2021); no 2-torsion of Rokhlin invariant 1 (Manolescu 2016). Seifert-fibered spheres: $h$, $d$, $\beta$ are computable in closed form.

## 5. Principal Obstacles

- **No smooth surgery in dimension 4.** Converting a smooth acyclic filling to a contractible one requires killing $\pi_1$ by embedded discs; Freedman's disc-embedding theorem is topological only, and no smooth analogue exists. This is exactly why the topological answer does not descend.
- **All known invariants are homomorphism-like.** $h$, $d$, $\beta$, $\lambda$ are additive or nearly additive with $\mathbb Z$ or $\mathbb Z/2$ targets, so they vanish on torsion. Detecting torsion needs an invariant that is *not* a homomorphism to a torsion-free group — none is known.
- **Floer homology is not functorial enough.** Instanton and monopole Floer theories give cobordism inequalities, not a complete invariant; a homology cobordism with nontrivial $\pi_1$ can carry reducible-free moduli spaces that defeat the standard neck-stretching arguments.
- **Computability.** $d$, $h$, $\beta$ are effectively computable only for Seifert-fibered, graph, and some surgery manifolds; for a general triangulated homology sphere there is no algorithm to decide $[\Sigma]=0$.
- **Absence of geometric constructions.** Producing a contractible filling is an explicit handle-calculus problem; there is no systematic method beyond Mazur-type $0$-,$1$-,$2$-handle patterns, and no obstruction theory that certifies "no such handle structure exists".

## 6. The Gap

Proven: $\mu$ obstructs; gauge theory shows $\Theta^3_{\mathbb Z}$ is large and contains $\mathbb Z^\infty$ summands; topologically everything bounds. Missing:

1. **Torsion.** Every current obstruction factors through torsion-free groups, so the question "does $\Theta^3_{\mathbb Z}$ contain an element of finite order?" is untouched except at $2$-torsion with $\mu=1$.
2. **Homology ball vs. contractible.** $[\Sigma]=0$ gives a smooth homology 4-ball with perfect $\pi_1$; no smooth technique upgrades this to contractible. Whether the two classes coincide is open.
3. **Completeness.** No proposed finite list of invariants is conjecturally complete; even a conditional characterization (say, in terms of $\mathrm{Pin}(2)$-Floer data) is not formulated.

## 7. Current Research (as of June 2026)

- **Involutive and $\mathrm{Pin}(2)$ Heegaard Floer.** Hendricks–Manolescu $\mathit{HFI}$ and the DHST local-equivalence group $\mathfrak{I}$ remain the main engine for summand and independence results; extending $\mathfrak{I}$-style algebra to detect torsion is the stated target *(frontier — verify)*.
- **Instanton-theoretic $\Gamma$-invariants.** Daemi's $\Gamma_Y$ and Daemi–Scaduto filtered instanton homology give obstructions inaccessible to monopole theory, including constraints on definite fillings.
- **Homology cobordism and knot concordance interplay.** Groups at Princeton, MIT, UCLA, Georgia Tech, and Oxford study $\Theta^3_{\mathbb Z}$ via $(\pm1)$-surgeries on knots, where concordance invariants ($\Upsilon$, $\nu^+$, $\varphi_j$) transfer.
- **Seiberg–Witten Floer spectra.** Manolescu-type stable homotopy refinements and Lin's Morse–Bott monopole framework aim at finer equivariant invariants of $\mathbb Z/4$- or $S^1$-type.
- **Symplectic/Stein constraints.** Constraints on contractible fillings from Stein-fillability and Heegaard Floer contact invariants continue to rule out fillings case-by-case.

## 8. Future Work

- Construct a non-homomorphic, torsion-sensitive invariant of $\Theta^3_{\mathbb Z}$ — e.g. from $\mathbb Z/p$-equivariant Floer theory for odd $p$, or from the full stable homotopy type rather than its homology.
- Decide whether $\Theta^3_{\mathbb Z}\cong\mathbb Z^\infty$ (free abelian), as several authors conjecture.
- Settle the acyclic-vs-contractible gap, possibly by producing a smooth homology ball whose boundary provably bounds no contractible manifold.
- Systematic search: catalogue small Brieskorn and surgery homology spheres with all known invariants vanishing, and attempt explicit Mazur-type handle constructions; failures sharpen conjecture (R).
- Clarify the relation to the smooth 4-dimensional Poincaré conjecture: contractible fillings of $\Sigma$ with $\Sigma$ obtained by surgery are a standard source of potential exotic $S^4$'s.

## 9. Key References

- **[Foundational]** V. A. Rokhlin. *New results in the theory of four-dimensional manifolds.* Doklady Akad. Nauk SSSR 84 (1952), 221–224.
- **[Foundational]** M. H. Freedman. *The topology of four-dimensional manifolds.* Journal of Differential Geometry 17 (1982), 357–453.
- **[Foundational]** S. Akbulut, R. Kirby. *Mazur manifolds.* Michigan Mathematical Journal 26 (1979), 259–284. [DOI](https://doi.org/10.1307/mmj/1029002261)
- **[Foundational]** A. Casson, J. Harer. *Some homology lens spaces which bound rational homology balls.* Pacific Journal of Mathematics 96 (1981), 23–36. [DOI](https://doi.org/10.2140/pjm.1981.96.23)
- **[Foundational]** R. Fintushel, R. Stern. *Pseudofree orbifolds.* Annals of Mathematics 122 (1985), 335–364. [DOI](https://doi.org/10.2307/1971306)
- **[SOTA]** M. Furuta. *Homology cobordism group of homology 3-spheres.* Inventiones Mathematicae 100 (1990), 339–355. [DOI](https://doi.org/10.1007/bf01231190)
- **[SOTA]** K. Frøyshov. *Equivariant aspects of Yang–Mills Floer theory.* Topology 41 (2002), 525–552. [DOI](https://doi.org/10.1016/s0040-9383(01)00018-0)
- **[SOTA]** P. Ozsváth, Z. Szabó. *Absolutely graded Floer homologies and intersection forms for four-manifolds with boundary.* Advances in Mathematics 173 (2003), 179–261. [DOI](https://doi.org/10.1016/s0001-8708(02)00030-0)
- **[SOTA]** C. Manolescu. *Pin(2)-equivariant Seiberg–Witten Floer homology and the triangulation conjecture.* Journal of the AMS 29 (2016), 147–176. [DOI](https://doi.org/10.1090/jams829)
- **[SOTA / Recent]** I. Dai, J. Hom, M. Stoffregen, L. Truong. *An infinite-rank summand of the homology cobordism group.* Duke Mathematical Journal 170 (2021), 1275–1300.
- **[Survey]** N. Saveliev. *Invariants for Homology 3-Spheres.* Encyclopaedia of Mathematical Sciences 140, Springer, 2002. [DOI](https://doi.org/10.1007/978-3-662-04705-7)
- **[Survey]** C. Manolescu. *Lectures on the triangulation conjecture.* Proceedings of the Gökova Geometry–Topology Conference 2015, 1–38.
- **[Survey]** S. Akbulut, J. McCarthy. *Casson's Invariant for Oriented Homology 3-Spheres: An Exposition.* Mathematical Notes 36, Princeton University Press, 1990.

## 10. Worked Example / Concrete Special Case

**Claim.** The Poincaré sphere $\Sigma=\Sigma(2,3,5)$ bounds no smooth compact acyclic 4-manifold — so (R-naive) fails.

1. $\Sigma$ is the boundary of the plumbing $W_{E_8}$ on the $E_8$ graph: a smooth 4-manifold built from 8 disc bundles over $S^2$ of Euler number $-2$. Its intersection form is $-E_8$: even, unimodular, negative definite, rank 8, so $\sigma(W_{E_8})=-8$.
2. Even form $\Rightarrow$ $W_{E_8}$ is spin, so $\mu(\Sigma)=\sigma(W_{E_8})/8=-1\equiv 1 \pmod 2$.
3. Suppose $V$ were a smooth compact acyclic 4-manifold with $\partial V=\Sigma$. Then $H_2(V)=0$, so $\sigma(V)=0$ and $V$ is spin.
4. Glue: $X = W_{E_8}\cup_\Sigma (-V)$ is a closed smooth 4-manifold. The spin structures agree on $\Sigma$ (unique on a homology sphere), so $X$ is spin. Novikov additivity gives
$$\sigma(X)=\sigma(W_{E_8})-\sigma(V)=-8 .$$
5. Rokhlin's theorem demands $16\mid\sigma(X)$, but $16\nmid -8$. Contradiction.

**Contrast.** $\Sigma(2,5,7)$ bounds the negative-definite plumbing with $\sigma=-16$, so $\mu=0$; Akbulut–Kirby exhibit an explicit Mazur manifold (one $1$-handle, one $2$-handle) with boundary $\Sigma(2,5,7)$, so it *does* bound smoothly. The two examples show $\mu$ is a genuine but partial obstruction. That $\mu$ is not complete is seen at $\Sigma(2,3,5)\\#\Sigma(2,3,5)$: $\mu=1+1=0$, yet Fintushel–Stern's $R$-invariant gives $[\Sigma(2,3,5)]$ infinite order, so this manifold bounds no smooth homology ball either.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*