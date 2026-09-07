---
id: 02-algebra-group-theory/farrell-jones-conjecture
title: "Farrell-Jones Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Farrell-Jones Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/farrell-jones-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a discrete group and $R$ an associative ring with unit. The Farrell–Jones Conjecture (FJC) asserts that the algebraic $K$-theory and $L$-theory of the group ring $RG$ are computable from the corresponding theories of the *virtually cyclic* subgroups of $G$, glued together by the equivariant homotopy type of a classifying space.

Precisely: the **assembly maps**
$$
A_{\mathcal{VC}}^{K}\colon H_n^G\bigl(E_{\mathcal{VC}}G;\mathbf{K}_R\bigr)\;\longrightarrow\;H_n^G(\mathrm{pt};\mathbf{K}_R)=K_n(RG),
$$
$$
A_{\mathcal{VC}}^{L}\colon H_n^G\bigl(E_{\mathcal{VC}}G;\mathbf{L}_R^{\langle-\infty\rangle}\bigr)\;\longrightarrow\;L_n^{\langle-\infty\rangle}(RG)
$$
are isomorphisms for all $n\in\mathbb{Z}$.

A complete proof must establish this for **every** group $G$ and every ring $R$ (in the standard modern form: every additive category with $G$-action, the "FJC with coefficients", which is what all known proofs actually deliver). A disproof requires a single pair $(G,R)$ and degree $n$ where the map fails to be bijective. No counterexample is known; the conjecture is open in general, and this openness is the reason the Borel and Novikov conjectures remain open.

## 2. Mathematical Foundations

**Families.** A *family* $\mathcal{F}$ of subgroups of $G$ is a set closed under conjugation and passage to subgroups. Relevant families: $\mathcal{TR}=\{1\}$, $\mathcal{FIN}$ (finite subgroups), $\mathcal{VC}$ (virtually cyclic subgroups, i.e. those containing a cyclic subgroup of finite index).

**Classifying space.** $E_{\mathcal F}G$ is a $G$-CW-complex with
$$
(E_{\mathcal F}G)^H\simeq
\begin{cases}
\ast & H\in\mathcal F,\\
\emptyset & H\notin\mathcal F,
\end{cases}
$$
unique up to $G$-homotopy. For $\mathcal F=\mathcal{TR}$ this is $EG$; $E_{\mathcal{FIN}}G$ is the classical classifying space for proper actions $\underline{E}G$.

**Davis–Lück construction.** Let $\mathrm{Or}(G)$ be the orbit category (objects $G/H$, morphisms $G$-maps). There is a functor
$$
\mathbf{K}_R\colon \mathrm{Or}(G)\to \mathrm{Spectra},\qquad G/H\mapsto \mathbf{K}(RH),
$$
with $\pi_n\mathbf{K}_R(G/H)=K_n(RH)$. For a $G$-CW-complex $X$ set
$$
H_n^G(X;\mathbf{K}_R):=\pi_n\bigl(X_+\wedge_{\mathrm{Or}(G)}\mathbf{K}_R\bigr).
$$
This is a $G$-equivariant homology theory; the assembly map is induced by the projection $E_{\mathcal F}G\to\mathrm{pt}$. This is the formulation of Davis–Lück (1998), equivalent to the original geometric one of Farrell–Jones (1993).

**Why $\mathcal{VC}$ and not $\mathcal{FIN}$.** By Bass–Heller–Swan, for $R$ non-regular $K_n(R[t,t^{-1}])$ contains two copies of the Nil-group $NK_n(R)$, which is invisible to $H_n^G(E_{\mathcal{FIN}}G)$. Infinite virtually cyclic groups (types $\mathbb{Z}$ and $D_\infty$) are exactly what carries these Nil-phenomena. In $L$-theory with the $\langle-\infty\rangle$ decoration the UNil-terms behave analogously; with other decorations ($s,h,p$) the conjecture is **false** (Farrell–Jones).

**Consequences.** For torsion-free $G$ and $R$ regular the source collapses to $H_n(BG;\mathbf{K}(R))$, giving:
- $\mathrm{Wh}(G)=0$, $\widetilde{K}_0(\mathbb{Z}G)=0$, $K_{-n}(\mathbb{Z}G)=0$ for $n\ge1$;
- the **Borel Conjecture** in dimensions $\ge5$ (aspherical closed manifolds with $\pi_1=G$ are topologically rigid), via surgery;
- the **Novikov Conjecture** (homotopy invariance of higher signatures), from rational injectivity of $A^L$;
- the **Kaplansky idempotent conjecture** for torsion-free $G$ and $R$ an integral domain of characteristic $0$ (via $K_0$ plus the Bass trace conjecture).

**Inheritance.** FJC with coefficients is closed under: subgroups, finite direct products, free products, directed colimits, extensions with $\mathcal{VC}$-quotient behaviour, and commensurability (Bartels–Lück, Bartels–Echterhoff–Lück).

## 3. History & State of the Art (SOTA)

- **1993.** F. T. Farrell and L. E. Jones, *Isomorphism conjectures in algebraic $K$-theory*, J. Amer. Math. Soc. 6, 249–297 — the conjecture is stated, and proved for fundamental groups of closed nonpositively curved Riemannian manifolds using the geodesic flow and "asymptotic transfer".
- **1998.** Davis–Lück recast the conjecture homotopy-theoretically (assembly = map from $E_{\mathcal F}G$), making the inheritance calculus possible.
- **2008.** Bartels–Lück–Reich prove the $K$-theoretic FJC with coefficients for **hyperbolic groups** (Invent. Math. 172), introducing *covers of the flow space of controlled dimension*.
- **2012.** Bartels–Lück (Annals 175) prove full $K$- and $L$-theoretic FJC for hyperbolic and **CAT(0) groups**, hence the Borel Conjecture for these in dimension $\ge5$.
- **2014–2016.** Extension to lattices: cocompact lattices in virtually connected Lie groups (Bartels–Farrell–Lück), $\mathrm{GL}_n(\mathbb{Z})$ (Bartels–Lück–Reich–Rüping), $S$-arithmetic groups (Rüping), arbitrary lattices (Kammeyer–Lück–Rüping).
- **2015.** Wegner: virtually solvable groups.
- **2019.** Bartels–Bestvina: mapping class groups of surfaces of finite type.

The unifying SOTA machinery is the notion of a **finitely $\mathcal{F}$-amenable action** of controlled dimension on a compact/finite-dimensional space, plus a **transfer** argument; Bartels' survey *On proofs of the Farrell–Jones conjecture* (2016) isolates this as the single criterion behind essentially all known cases.

## 4. Partial Results / Verified Cases

FJC with coefficients in additive categories (both $K$ and $L^{\langle-\infty\rangle}$) is a **theorem** for:

| Class | Reference |
|---|---|
| Fundamental groups of closed nonpositively curved manifolds | Farrell–Jones 1993 |
| Word-hyperbolic groups (Gromov) | Bartels–Lück–Reich 2008 ($K$); Bartels–Lück 2012 ($L$) |
| Groups acting properly cocompactly on finite-dimensional CAT(0) spaces | Bartels–Lück 2012; Wegner 2012 |
| Virtually solvable groups (in particular virtually poly-$\mathbb{Z}$, nilpotent) | Wegner 2015 |
| Lattices in virtually connected Lie groups (cocompact and non-cocompact) | Bartels–Farrell–Lück 2014; Kammeyer–Lück–Rüping 2016 |
| $\mathrm{GL}_n(\mathbb{Z})$, $\mathrm{SL}_n(\mathbb{Z})$ for all $n$; $S$-arithmetic groups over number fields | Bartels–Lück–Reich–Rüping 2014; Rüping 2016 |
| Mapping class groups $\mathrm{Mod}(S_{g,n})$, all $g,n$ | Bartels–Bestvina 2019 |
| Normally poly-free groups; e.g. Artin braid groups $B_n$, all $n$ | Brück–Kielak–Wu 2021 |
| Groups acting on trees with FJC vertex stabilizers; free products; directed colimits | Bartels–Lück 2007; Bartels–Echterhoff–Lück 2008 |

Consequences established outright: Borel Conjecture for closed aspherical $n$-manifolds, $n\ge5$, with hyperbolic or CAT(0) fundamental group; $\mathrm{Wh}(G)=0$ for all torsion-free groups in the table; Novikov Conjecture for all of them.

Weaker but broader: **rational injectivity** of the assembly map holds for groups of finite decomposition complexity (Kasprowski 2015, Proc. LMS) and for groups coarsely embeddable in Hilbert space, which suffices for Novikov but not for Borel.

## 5. Principal Obstacles

- **Every proof needs a flow.** The Farrell–Jones/Bartels–Lück method requires a *flow space* $FS(X)$ with a $G$-action admitting long thin equivariant covers of bounded dimension. Constructing one demands a geometry with a well-behaved coarse geodesic structure. Groups with no nonpositively curved or hyperbolic-like model (e.g. $\mathrm{Out}(F_n)$ for $n\ge4$) have no known candidate.
- **Transfers do not commute with induction.** The controlled-topology transfer used to kill Nil-terms is constructed from a contractible finite-dimensional space with a compact quotient; for groups of infinite geometric dimension (Thompson's groups $F,T,V$; infinitely generated or non-finitely-presented groups) the transfer has no home.
- **No hereditary passage to quotients.** The inheritance calculus handles subgroups and colimits but not general quotients or extensions with non-$\mathcal{VC}$ kernel behaviour. This blocks bootstrapping from a known class to all groups.
- **Nil-groups are opaque.** $NK_n(RH)$ and $\mathrm{UNil}$ are essentially uncomputable in general; any strategy that tries to verify the conjecture by direct computation stalls immediately.
- **Warning from the analytic analogue.** The Baum–Connes Conjecture *with coefficients* has counterexamples (Higson–Lafforgue–Skandalis 2002, using Gromov monster groups containing expanders). The algebraic assembly map is not known to be similarly vulnerable, but this shows that "true for all groups" is not a safe default, and the standard geometric obstructions to Baum–Connes have no proven algebraic analogue either way.

## 6. The Gap

Known cases are exactly the groups admitting a *finitely $\mathcal{F}$-amenable action of finite covering dimension on a compact metrizable space* (or reducible to such by the inheritance rules). The general statement quantifies over all discrete groups. The precise missing step is one of:

1. Produce the flow-space/transfer package for groups with only partial nonpositive curvature — $\mathrm{Out}(F_n)$, $n\ge4$; general CAT(0) cube-group-like objects without cocompactness; Thompson's groups.
2. Or prove FJC by a genuinely non-geometric route (a descent or trace argument valid for all $G$), which no one has.
3. Or exhibit a group where the assembly map fails — the natural candidates are groups containing expanders (Gromov monsters, Osajda's constructions), where a coarse-geometric failure analogous to Baum–Connes might be forced.

No interpolation exists between (1) and (3): every group is either in the flow-space regime or entirely untouched.

## 7. Current Research (as of June 2026)

- **Bonn school (Lück, Bartels/Münster).** Ongoing extension of the finitely-$\mathcal{F}$-amenable criterion; Lück's book-length treatment *Isomorphism Conjectures in K- and L-Theory* remains the reference in progress.
- **$\mathrm{Out}(F_n)$ and free-by-cyclic groups.** Bestvina–Fujiwara–Wigglesworth established FJC for hyperbolic-by-cyclic and free-by-cyclic groups (arXiv, 2021) using train-track dynamics as a substitute flow. Extending this to all of $\mathrm{Out}(F_n)$ is the flagship open case *(frontier — verify)*.
- **Cube complexes and Helly groups.** Groups acting properly cocompactly on Helly complexes / injective metric spaces are being pushed into the CAT(0) framework via bicombings.
- **Higher/relative assembly.** Kasprowski, Winges and collaborators study the assembly map for finite-dimensionality and "$K$-theory of the Farrell–Jones assembly as a localizing invariant" (Bunke–Kasprowski–Winges), reformulating assembly in terms of coarse homology theories.
- **Counterexample hunting.** A minority program looks at Gromov monsters and lacunary hyperbolic groups; nothing conclusive *(frontier — verify)*.

## 8. Future Work

- Build a flow space for $\mathrm{Out}(F_n)$ from Outer space plus the axes/train-track machinery (Bestvina's stated program).
- Decide FJC for Thompson's group $F$ — a test case for infinite geometric dimension with amenability status itself unknown.
- Prove or refute FJC for all linear groups over arbitrary fields (known for characteristic-zero arithmetic cases; open in general).
- Develop a genuinely homotopy-theoretic proof via localizing invariants and coarse geometry (Bunke–Kasprowski–Winges), decoupling the argument from Riemannian input.
- Determine whether the $L$-theoretic conjecture can hold when the $K$-theoretic one fails, i.e. whether Borel is strictly weaker than FJC.

## 9. Key References

- **[Foundational]** F. T. Farrell, L. E. Jones. *Isomorphism conjectures in algebraic $K$-theory.* Journal of the American Mathematical Society 6 (1993), 249–297.
- **[Foundational]** J. F. Davis, W. Lück. *Spaces over a category and assembly maps in isomorphism conjectures in $K$- and $L$-theory.* $K$-Theory 15 (1998), 201–252.
- **[SOTA]** A. Bartels, W. Lück, H. Reich. *The $K$-theoretic Farrell–Jones conjecture for hyperbolic groups.* Inventiones Mathematicae 172 (2008), 29–70.
- **[SOTA]** A. Bartels, W. Lück. *The Borel conjecture for hyperbolic and CAT(0)-groups.* Annals of Mathematics 175 (2012), 631–689.
- **[SOTA]** C. Wegner. *The Farrell–Jones conjecture for virtually solvable groups.* Journal of Topology 8 (2015), 975–1016.
- **[SOTA]** A. Bartels, F. T. Farrell, W. Lück. *The Farrell–Jones Conjecture for cocompact lattices in virtually connected Lie groups.* J. Amer. Math. Soc. 27 (2014), 339–388.
- **[SOTA]** A. Bartels, W. Lück, H. Reich, H. Rüping. *$K$- and $L$-theory of group rings over $GL_n(\mathbb{Z})$.* Publications Mathématiques de l'IHÉS 119 (2014), 97–125.
- **[SOTA]** A. Bartels, M. Bestvina. *The Farrell–Jones Conjecture for mapping class groups.* Inventiones Mathematicae 215 (2019), 651–712.
- **[Survey]** W. Lück, H. Reich. *The Baum–Connes and the Farrell–Jones conjectures in $K$- and $L$-theory.* In: Handbook of $K$-theory, Springer, 2005, 703–842.
- **[Survey]** A. Bartels. *On proofs of the Farrell–Jones conjecture.* In: Topology and Geometric Group Theory, Springer Proceedings in Mathematics & Statistics 184, 2016, 1–31.
- **[Context]** N. Higson, V. Lafforgue, G. Skandalis. *Counterexamples to the Baum–Connes conjecture.* Geometric and Functional Analysis 12 (2002), 330–354.
- **[Recent]** B. Brück, D. Kielak, X. Wu. *The Farrell–Jones Conjecture for normally poly-free groups.* Proceedings of the AMS 149 (2021), 2349–2356.

## 10. Worked Example / Concrete Special Case

**Take $G=\mathbb{Z}$, $R$ any ring.** Then $RG=R[t,t^{-1}]$.

$\mathbb{Z}$ is itself virtually cyclic, so $\mathcal{VC}$ contains $G$ and $E_{\mathcal{VC}}\mathbb{Z}=\mathrm{pt}$. The assembly map $A^K_{\mathcal{VC}}$ is the identity: **FJC holds trivially**. The example's value is in showing why $\mathcal{VC}$ is forced.

Try instead the family $\mathcal{FIN}=\{1\}$. Here $E_{\mathcal{FIN}}\mathbb{Z}=E\mathbb{Z}=\mathbb{R}$ with the translation action, a free $\mathbb{Z}$-CW-complex with quotient $S^1$. So
$$
H_n^{\mathbb{Z}}(E\mathbb{Z};\mathbf{K}_R)=H_n(S^1;\mathbf{K}(R))=K_n(R)\oplus K_{n-1}(R),
$$
by the Atiyah–Hirzebruch spectral sequence for $S^1$ (which degenerates: $E^2_{0,n}=K_n(R)$, $E^2_{1,n-1}=K_{n-1}(R)$).

Compare with the true answer, the **Bass–Heller–Swan decomposition**:
$$
K_n\bigl(R[t,t^{-1}]\bigr)\;\cong\;K_n(R)\;\oplus\;K_{n-1}(R)\;\oplus\;NK_n(R)\;\oplus\;NK_n(R),
$$
where $NK_n(R)=\ker\bigl(K_n(R[t])\xrightarrow{t\mapsto 0}K_n(R)\bigr)$.

So the $\mathcal{FIN}$-assembly map is injective with cokernel $NK_n(R)^{\oplus 2}$.

- If $R$ is **regular** noetherian, $NK_n(R)=0$ (Bass–Heller–Swan / Quillen's fundamental theorem), the cokernel vanishes, and $\mathcal{FIN}$ would have sufficed.
- If $R$ is **not** regular — e.g. $R=\mathbb{Z}/4$, where $NK_1(\mathbb{Z}/4)\neq 0$ (Bass–Murthy) — the map is **not** surjective.

This single computation is the reason Farrell and Jones stated the conjecture with virtually cyclic, not finite, subgroups: the infinite virtually cyclic groups $\mathbb{Z}$ and $D_\infty=\mathbb{Z}/2\ast\mathbb{Z}/2$ are precisely the carriers of the Nil- and UNil-terms. For $D_\infty$ one gets, by Waldhausen's amalgamated-product formula, $\mathrm{Wh}(D_\infty)=0$ and $\widetilde{K}_0(\mathbb{Z}D_\infty)=0$ — consistent with FJC, since $D_\infty$ is virtually cyclic and the assembly map is again an identity.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*