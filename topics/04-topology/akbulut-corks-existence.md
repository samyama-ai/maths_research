---
id: 04-topology/akbulut-corks-existence
title: "Akbulut Corks Existence"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Akbulut Corks Existence

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/akbulut-corks-existence` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

A **cork** is a pair $(C,\tau)$ where $C$ is a compact contractible smooth $4$-manifold with boundary and $\tau:\partial C\to\partial C$ is an involution that extends to a self-*homeomorphism* of $C$ but to no self-*diffeomorphism* of $C$. Cutting $C$ out of an ambient $4$-manifold $X$ and regluing by $\tau$ (a **cork twist**) leaves the homeomorphism type unchanged and may change the diffeomorphism type.

The problem has two halves.

* **(Existence.)** Do corks exist, and is every exotic pair of closed simply-connected smooth $4$-manifolds explained by one? **Answered yes.** Akbulut (1991) produced the first cork; Curtis–Freedman–Hsiang–Stong (1996) and Matveyev (1996) proved that any two homeomorphic closed simply-connected smooth $4$-manifolds are related by a single cork twist on a contractible submanifold.
* **(Structure — open.)** Is there a *universal* cork, i.e. a single $(C,\tau)$ that suffices for all such pairs? Which finitely presented groups act as cork twisting groups? Can corks be made to detect exotica in the topologically-trivial setting relevant to the smooth $4$-dimensional Poincaré conjecture?

A complete resolution of the remaining half means either exhibiting a universal cork with proof, or proving no compact contractible $C$ can be universal.

## 2. Mathematical Foundations

Let $C$ be a compact contractible smooth $4$-manifold. Then $H_*(\partial C;\mathbb{Z})\cong H_*(S^3;\mathbb{Z})$, so $\partial C$ is an integral homology $3$-sphere. By Freedman's theorem, any homology $3$-sphere bounds a contractible topological $4$-manifold, unique up to homeomorphism; hence

$$\tau:\partial C\xrightarrow{\ \cong\ }\partial C \quad\Longrightarrow\quad \exists\, \hat\tau: C\xrightarrow{\ \text{homeo}\ } C,\ \hat\tau|_{\partial C}=\tau .$$

For $C\subset X$ with $X$ closed, define the twist

$$X_\tau \;=\; (X\setminus \operatorname{int} C)\ \cup_{\tau}\ C .$$

Since $\tau$ extends topologically, $X_\tau\cong_{\mathrm{homeo}} X$; smooth invariants (Donaldson, Seiberg–Witten, Heegaard Floer) may differ. Formally, $\mathrm{SW}_X \neq \mathrm{SW}_{X_\tau}$ certifies $(C,\tau)$ is a cork.

**Standard model.** $W_1$ is the Mazur-type manifold given by a Kirby diagram with one dotted $1$-handle circle $A$ and one $0$-framed $2$-handle attaching circle $B$, where $\{A,B\}$ is a *symmetric* link: there is an isotopy of $S^3$ exchanging $A$ and $B$. That symmetry induces the involution
$$\tau: \partial W_1 \to \partial W_1,\qquad \tau^2=\mathrm{id},$$
realized on the boundary by interchanging the dot and the $0$-framing (a boundary operation). Here $\partial W_1 \cong \Sigma(2,5,7)$, the Brieskorn sphere
$$\Sigma(2,5,7)=\{(z_1,z_2,z_3)\in\mathbb{C}^3:\ z_1^2+z_2^5+z_3^7=0\}\cap S^5 .$$

**Decomposition theorem (CFHS, Matveyev).** If $X_0, X_1$ are closed simply-connected smooth $4$-manifolds that are homeomorphic, they are h-cobordant (Freedman + Donaldson-era classification), and every such h-cobordism $W$ splits as
$$W \;=\; W_{\mathrm{triv}} \ \cup\ W_{\mathrm{cork}},$$
with $W_{\mathrm{triv}}$ a product; consequently there exist a contractible $C\subset X_0$ and an involution $\tau$ of $\partial C$ with $X_1\cong (X_0\setminus \operatorname{int} C)\cup_\tau C$.

**Stein refinement (Akbulut–Matveyev).** $C$ may be taken to admit a Stein structure, i.e. a proper $J$-convex exhaustion $\varphi$ with $C=\varphi^{-1}([0,c])$; equivalently a handle decomposition with $1$-handles and $2$-handles attached along Legendrian knots $K$ with framing $\mathrm{tb}(K)-1$.

**Higher-order corks.** For a finite or infinite group $G$, a **$G$-cork** is $(C,\rho)$ with $\rho:G\to \pi_0\,\mathrm{Diff}(\partial C)$ such that distinct $g\in G$ give pairwise non-diffeomorphic reglued manifolds $X_{\rho(g)}$.

## 3. History & State of the Art (SOTA)

* **1980s.** Mazur manifolds and Akbulut–Kirby's contractible manifolds provide the candidate objects; Freedman (1982) supplies the topological extension mechanism; Donaldson theory supplies the smooth obstruction.
* **1991.** Akbulut, *A fake compact contractible 4-manifold* (J. Differential Geom. 33): the involution $\tau$ on $\partial W_1$ does not extend to a diffeomorphism of $W_1$. Proof uses the Fintushel–Stern $R$-invariant / Donaldson-theoretic obstruction on $\Sigma(2,5,7)$-bounded definite pieces.
* **1996.** Curtis–Freedman–Hsiang–Stong (Invent. Math. 123) and, independently with a handle-theoretic proof, Matveyev (J. Differential Geom. 44): the cork decomposition theorem. This resolves the existence question in the strongest form — corks are not exotic curiosities but the universal *mechanism* of $4$-dimensional exotica among simply-connected closed manifolds.
* **1998.** Akbulut–Matveyev (IMRN): corks can be chosen Stein, hence with sharp adjunction-type constraints.
* **2008.** Akbulut–Yasui (J. Gökova Geom. Topol. 2) give explicit infinite families $W_n$, $\overline{W}_n$ and *plugs* (non-contractible analogues), and compute cork twists inside elliptic surfaces.
* **2017.** Gompf, *Infinite order corks* (Geom. Topol. 21): a $\mathbb{Z}$-cork, using an infinite-order boundary diffeomorphism of a compact contractible manifold. Tange independently studies finite-order corks. Auckly–Kim–Melvin–Ruberman, *Equivariant corks* (Algebr. Geom. Topol. 17): corks with $(\mathbb{Z}/2)^n$-actions.
* **2021.** Melvin–Schwartz, *Higher-order corks* (Invent. Math. 224): for every $n$ there is an order-$n$ cork; every finitely presented group is the "twisting group" of some cork-like object.
* **2022.** Lin–Ruberman–Saveliev (Geom. Topol.) apply the monopole Lefschetz number to show that many cork involutions on homology spheres extend over *no* homology ball, a much stronger non-extension statement than the original.

## 4. Partial Results / Verified Cases

* **Dimension 4, closed simply-connected, homeomorphic pairs:** fully resolved. One cork twist suffices (CFHS 1996; Matveyev 1996).
* **Explicit corks:** $W_1$ with $\partial W_1=\Sigma(2,5,7)$; the Akbulut–Yasui family $W_n$ ($n\ge1$), the "positron" cork, and $\overline{W}_n$. All are Mazur manifolds built from one $1$-handle and one $2$-handle.
* **Concrete exotica realized by twists:** exotic $\mathbb{CP}^2\\#\,k\,\overline{\mathbb{CP}^2}$ for small $k$, exotic pairs among $E(n)_{p,q}$ elliptic surfaces, and Fintushel–Stern knot-surgery pairs $E(2)_K$ vs $E(2)$, all differ by a cork twist localized in a contractible piece.
* **Group orders realized:** $\mathbb{Z}/2$ (Akbulut 1991), $(\mathbb{Z}/2)^n$ (Auckly–Kim–Melvin–Ruberman 2017), $\mathbb{Z}/n$ for all $n$ and $\mathbb{Z}$ (Tange 2017; Gompf 2017; Melvin–Schwartz 2021).
* **Stein/complex-geometric:** every cork can be taken Stein (Akbulut–Matveyev 1998); cork twists produce exotic Stein surfaces (Akbulut–Yasui).
* **Boundary rigidity:** for infinitely many Brieskorn spheres $\Sigma(p,q,r)$ with the natural involution, no extension over any acyclic $4$-manifold exists (Lin–Ruberman–Saveliev 2022).

## 5. Principal Obstacles

* **Gauge theory is blind to contractible pieces.** Seiberg–Witten and Donaldson invariants vanish or are undefined for $4$-manifolds with $b_2^+=0$; a cork $C$ has $H_2(C)=0$. Non-extension is always proved *indirectly*, by embedding $C$ in a closed $X$ with $b_2^+>1$ and comparing $\mathrm{SW}_X$ with $\mathrm{SW}_{X_\tau}$. Hence one cannot in general certify a candidate $(C,\tau)$ intrinsically.
* **h-cobordism has no smooth Whitney trick.** The CFHS/Matveyev argument shows the failure of the smooth h-cobordism theorem concentrates in a contractible sub-h-cobordism, but gives no control on the *size* or *handle number* of $C$ — the proof is existential in the number of handles, so no algorithm outputs $C$ from $(X_0,X_1)$.
* **Universality obstructions cut both ways.** Any single compact $C$ has fixed $\partial C$, hence fixed Casson invariant, Frøyshov invariant $\delta(\partial C)$ and Heegaard Floer $d$-invariants. It is unclear whether an infinite family of exotic pairs requiring "increasingly complicated" homology sphere boundaries exists — no invariant currently measures cork complexity monotonically.
* **Homotopy 4-spheres.** Twisting a cork inside $S^4$ yields a homotopy $4$-sphere; distinguishing it would refute the smooth Poincaré conjecture. Every known smooth invariant vanishes identically on homotopy $4$-spheres, so this route is presently obstruction-free in the useless sense.
* **Kirby calculus is non-effective.** Deciding whether two handle diagrams of contractible manifolds give diffeomorphic manifolds is not known to be decidable; equivalently the word problem-like difficulties in $\pi_0\,\mathrm{Diff}$ block computation.

## 6. The Gap

Proven: *some* cork works for *each* exotic pair (Section 4). Wanted: quantitative and uniform statements.

Precisely, the open boundary is:

1. **Universality.** Does there exist $(C,\tau)$ such that every pair of homeomorphic closed simply-connected smooth $4$-manifolds is related by a twist on an embedded copy of *this* $C$? Compact universal corks are not known; the known constructions produce a $C$ depending on the pair.
2. **Effectivity.** Given explicit $X_0\cong_{\mathrm{homeo}}X_1$, produce $C$ and an embedding. Done by hand in a handful of elliptic-surface examples; no general procedure.
3. **Cork detection without an ambient manifold.** Find an invariant $I(C,\tau)$ of the pair alone whose non-vanishing implies non-extension of $\tau$ over $C$.

Crossing (1) requires either an infinite-order/universal boundary diffeomorphism argument extending Gompf's $\mathbb{Z}$-cork to all of $\pi_0$, or a new obstruction showing $d$-invariants of $\partial C$ bound the exotica a fixed $C$ can produce.

## 7. Current Research (as of June 2026)

* **Floer-theoretic non-extension.** Involutive Heegaard Floer homology and $\mathrm{Pin}(2)$-equivariant Seiberg–Witten theory are used to obstruct extensions of boundary involutions over acyclic fillings (Lin, Ruberman, Saveliev, and students at Brandeis/Indiana/UT Austin).
* **Corks and exotic surfaces.** Hayden, Piccirillo and collaborators exploit corks to build exotically knotted surfaces in $B^4$ and $\mathbb{R}^4$; techniques transfer between the cork and surface settings via branched covers. *(frontier — verify)*
* **Equivariant / higher-order corks.** Auckly, Kim, Melvin, Ruberman continue the program of realizing group actions; questions on which $G$ act *effectively* on cork boundaries remain live.
* **Universal cork status.** Constructions of "one-cork-fits-many" phenomena for restricted families (e.g. knot-surgered elliptic surfaces) have appeared; a genuine universal compact cork is still not established. *(frontier — verify)*
* **Trace embedding & Poincaré conjecture.** Cork twists inside $S^4$ are studied via the trace-embedding lemma, connecting to sliceness of specific knots (e.g. the Conway knot circle of ideas).

## 8. Future Work

* Develop a *relative* Seiberg–Witten or Floer-theoretic invariant of $(C,\tau)$ defined without embedding into a closed manifold.
* Bound the handle number of the cork appearing in CFHS/Matveyev in terms of invariants of the h-cobordism — a "cork complexity" theory.
* Decide whether cork twists on $S^4$ can ever change the diffeomorphism type; equivalently, apply new invariants (skein lasagna modules, Khovanov-theoretic $s$-invariants) which do not vanish on homotopy $4$-spheres.
* Classify boundary homology spheres $\Sigma$ arising as $\partial C$ for corks; determine constraints from $\delta(\Sigma)$, Casson $\lambda(\Sigma)$, and $d$-invariants.
* Extend higher-order cork constructions to non-simply-connected $4$-manifolds, where the s-cobordism theorem is the relevant statement.

## 9. Key References

- **[Foundational]** M. Freedman. *The topology of four-dimensional manifolds.* Journal of Differential Geometry 17 (1982), 357–453.
- **[Foundational]** S. Akbulut. *A fake compact contractible 4-manifold.* Journal of Differential Geometry 33 (1991), 335–356.
- **[Foundational]** C. L. Curtis, M. H. Freedman, W. C. Hsiang, R. Stong. *A decomposition theorem for h-cobordant smooth simply-connected compact 4-manifolds.* Inventiones Mathematicae 123 (1996), 343–348.
- **[Foundational]** R. Matveyev. *A decomposition of smooth simply-connected h-cobordant 4-manifolds.* Journal of Differential Geometry 44 (1996), 571–582.
- **[SOTA]** S. Akbulut, R. Matveyev. *A convex decomposition theorem for 4-manifolds.* International Mathematics Research Notices 1998, no. 7, 371–381.
- **[SOTA]** S. Akbulut, K. Yasui. *Corks, plugs and exotic structures.* Journal of Gökova Geometry Topology 2 (2008), 40–82.
- **[SOTA]** R. E. Gompf. *Infinite order corks.* Geometry & Topology 21 (2017), 2475–2484.
- **[SOTA]** D. Auckly, H. J. Kim, P. Melvin, D. Ruberman. *Equivariant corks.* Algebraic & Geometric Topology 17 (2017), 1771–1783.
- **[SOTA]** P. Melvin, H. Schwartz. *Higher-order corks.* Inventiones Mathematicae 224 (2021), 291–313.
- **[SOTA]** J. Lin, D. Ruberman, N. Saveliev. *On the monopole Lefschetz number of finite-order diffeomorphisms.* Geometry & Topology 26 (2022).
- **[Survey / Book]** R. E. Gompf, A. I. Stipsicz. *4-Manifolds and Kirby Calculus.* Graduate Studies in Mathematics 20, American Mathematical Society, 1999.
- **[Survey / Book]** S. Akbulut. *4-Manifolds.* Oxford Graduate Texts in Mathematics 25, Oxford University Press, 2016.

## 10. Worked Example / Concrete Special Case

**The Akbulut cork $W_1$.**

*Handle picture.* Draw two unknots $A,B$ in $S^3$ linking with algebraic linking number $0$ but geometric linking number $4$ (a clasp-and-twist configuration). Put a dot on $A$ (so $A$ specifies a $1$-handle, i.e. remove an embedded $D^2\times D^2$ from $B^4$) and give $B$ framing $0$ (a $2$-handle). Then
$$W_1 \;=\; B^4 \cup (\text{1-handle}) \cup (\text{2-handle}).$$

*Contractibility.* $\pi_1(B^4\cup 1\text{-handle})=\langle x\rangle\cong\mathbb{Z}$. The $2$-handle kills a word $w(x)$; because $\mathrm{lk}(A,B)=0$ the exponent sum of $w$ is $0$, yet the relation $w(x)=1$ normally generates $\langle x\rangle$. Hence $\pi_1(W_1)=1$. The chain complex is $0\to\mathbb{Z}\xrightarrow{\ \pm1\ }\mathbb{Z}\to 0$ in degrees $2,1$, so $H_*(W_1)=H_*(\mathrm{pt})$; simply connected plus acyclic gives contractible.

*The involution.* The link $A\cup B$ is symmetric: an isotopy of $S^3$ carries $A\mapsto B$, $B\mapsto A$. On the boundary, "dot $\leftrightarrow$ $0$-framing" is a legal move (both surgeries on the same curve differ by exchanging $S^1\times D^2$ factors), so the symmetry descends to an involution
$$\tau:\partial W_1\to\partial W_1,\qquad \tau^2=\mathrm{id},\qquad \partial W_1\cong\Sigma(2,5,7).$$

*Why $\tau$ does not extend smoothly.* Suppose $\hat\tau:W_1\to W_1$ were a diffeomorphism with $\hat\tau|_\partial=\tau$. Embed $W_1$ in a closed simply-connected $X$ (Akbulut uses a suitable elliptic-surface-type ambient with $b_2^+>1$). Then $X_\tau=(X\setminus \operatorname{int}W_1)\cup_\tau W_1$ would be diffeomorphic to $X$. But one computes
$$\mathrm{SW}_{X}\;\neq\;\mathrm{SW}_{X_\tau}$$
(historically: Donaldson-invariant/Fintushel–Stern $R$-invariant computation for $\Sigma(2,5,7)$), a contradiction. Meanwhile $\tau$ *does* extend to a homeomorphism of $W_1$ by Freedman's classification, so $X\cong_{\mathrm{homeo}}X_\tau$.

*Conclusion drawn from the example.* $(W_1,\tau)$ is a cork, and $X, X_\tau$ is an exotic pair differing only inside a contractible $4$-manifold with two handles. The CFHS/Matveyev theorem says this picture — one contractible piece, one involution — is not special to $W_1$ but is the general shape of $4$-dimensional exotica among closed simply-connected smooth manifolds. What the example does *not* give, and what remains open, is whether one fixed $C$ can serve for all $X$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*