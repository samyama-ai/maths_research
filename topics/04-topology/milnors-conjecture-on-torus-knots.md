---
id: 04-topology/milnors-conjecture-on-torus-knots
title: "Milnor's Conjecture on Torus Knots"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Milnor's Conjecture on Torus Knots

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/milnors-conjecture-on-torus-knots` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $p,q$ be coprime integers with $p,q \ge 2$, and let $T_{p,q} \subset S^3$ be the $(p,q)$ torus knot: the closure of the braid $(\sigma_1\sigma_2\cdots\sigma_{p-1})^q \in B_p$, equivalently the link of the plane curve singularity $x^p + y^q = 0$ at the origin.

**Milnor's Conjecture (1968).** The unknotting number of $T_{p,q}$ equals

$$u(T_{p,q}) = \frac{(p-1)(q-1)}{2}.$$

Here $u(K)$ is the minimum, over all diagrams $D$ of $K$, of the number of crossing changes needed to convert $D$ into a diagram of the unknot.

The inequality $u(T_{p,q}) \le (p-1)(q-1)/2$ is elementary and diagrammatic. The content of the conjecture is the **lower bound**. A complete proof must show that no diagram of $T_{p,q}$ — including diagrams with arbitrarily many crossings, arbitrarily far from the standard closed-braid form — admits fewer than $(p-1)(q-1)/2$ crossing changes to the unknot. A disproof would be a single explicit unknotting sequence of shorter length.

The conjecture is a **theorem**, first proved by Kronheimer and Mrowka (1993) with gauge theory. It is catalogued here because (i) the statement is a landmark whose proof still requires 4-dimensional analysis or Khovanov-type homology, with no elementary argument known, and (ii) several of its natural strengthenings and analogues — notably the **topological** slice genus of $T_{p,q}$ — remain open.

## 2. Mathematical Foundations

**Seifert genus.** $T_{p,q}$ is fibred; its fibre is the Milnor fibre of $x^p+y^q$, with first Betti number the Milnor number $\mu = (p-1)(q-1)$. Hence

$$g_3(T_{p,q}) = \tfrac{1}{2}\mu = \tfrac{(p-1)(q-1)}{2}.$$

Equivalently, Seifert's algorithm on the positive braid closure with $n=p$ Seifert circles and $c = q(p-1)$ crossings gives $g_3 = \frac{c-n+1}{2}$.

**Alexander polynomial.**
$$\Delta_{T_{p,q}}(t) = \frac{(t^{pq}-1)(t-1)}{(t^p-1)(t^q-1)}, \qquad \deg \Delta_{T_{p,q}} = (p-1)(q-1) = 2g_3.$$

**Four-ball genus.** $g_4(K)$ is the minimal genus of a smoothly embedded, oriented, connected surface $\Sigma \subset B^4$ with $\partial\Sigma = K \subset S^3$. The two basic inequalities are
$$g_4(K) \le g_3(K), \qquad g_4(K) \le u(K).$$
The second holds because a crossing change is realised by an immersed annulus with one double point, which can be resolved at the cost of one unit of genus. So the whole conjecture reduces to
$$g_4(T_{p,q}) \ \ge\ \frac{(p-1)(q-1)}{2}.$$

**Thom-type statement.** Kronheimer–Mrowka's **local Thom conjecture** asserts: if $\Sigma \subset B^4$ is a smoothly embedded surface with boundary a link $L$ presented as the closure of a positive braid on $n$ strands with $c$ crossings, then $\chi(\Sigma) \le n - c$; equivalently, the Milnor fibre realises $g_4$ for every algebraic link. Its input is the **adjunction inequality** for the Seiberg–Witten / instanton invariants: for a closed symplectic (or Kähler) 4-manifold $X$ with $b_2^+>1$ and a smoothly embedded surface $\Sigma$ of genus $g\ge 1$ with $[\Sigma]^2 \ge 0$,
$$2g-2 \ \ge\ [\Sigma]^2 + |\langle c_1(K_X), [\Sigma]\rangle|.$$

**Slice-torus invariants.** A homomorphism $\nu: \mathcal{C} \to \mathbb{Z}$ from the smooth concordance group is *slice-torus* if $|\nu(K)| \le g_4(K)$ for all $K$ and $\nu(T_{p,q}) = g_4(T_{p,q}) = (p-1)(q-1)/2$. Two known examples:
- $\tau$ from knot Floer homology (Ozsváth–Szabó 2003), with $|\tau(K)| \le g_4(K)$;
- $s/2$ from Lee's deformation of Khovanov homology (Rasmussen 2010), with $|s(K)| \le 2 g_4(K)$.

**Classical lower bound.** The Murasugi signature satisfies $|\sigma(K)|/2 \le g_4(K)$; it proves the conjecture only for restricted families (Section 4).

## 3. History & State of the Art (SOTA)

- **1968.** Milnor, in *Singular Points of Complex Hypersurfaces*, computes the genus of the Milnor fibre and conjectures $u(T_{p,q}) = (p-1)(q-1)/2$.
- **1983–84.** Boileau and Weber reformulate the problem, showing it is equivalent to the statement that the Milnor fibre minimises genus in $B^4$ — i.e. to a local Thom conjecture. Bennequin's inequality (1983) gives $g_3$-type bounds from contact geometry but not the sharp $g_4$ bound.
- **1993.** Kronheimer and Mrowka, *Gauge theory for embedded surfaces, I* (Topology 32), prove the local Thom conjecture using instanton moduli with singularities along a surface. Milnor's conjecture follows. This was the first proof.
- **1994–95.** Kronheimer–Mrowka prove the Thom conjecture proper for $\mathbb{CP}^2$ via Seiberg–Witten theory, giving a shorter second route.
- **2003.** Ozsváth–Szabó define $\tau$ and reprove $g_4(T_{p,q}) = (p-1)(q-1)/2$ using Heegaard Floer homology.
- **2004/2010.** Rasmussen defines $s$ from Lee homology and gives the **first combinatorial proof** — no PDEs, no gauge theory, purely from Khovanov homology over $\mathbb{Q}$.
- **2009.** Lobb obtains the same bound from $\mathfrak{sl}(N)$ Khovanov–Rozansky homology, producing a family of slice-torus-like invariants.

SOTA: the result is settled for all coprime $(p,q)$, by at least four independent routes (instantons, Seiberg–Witten, Heegaard Floer, Khovanov). The remaining frontier is the **topological locally flat** analogue, where the answer is genuinely different and largely unknown.

## 4. Partial Results / Verified Cases

- **$T_{2,q}$, all odd $q\ge 3$:** $u = (q-1)/2$, from the signature $\sigma(T_{2,q}) = -(q-1)$; elementary and pre-1993.
- **Small cases from tables:** $T_{3,4} = 8_{19}$ ($u=3$, $\sigma=-6$), $T_{3,5} = 10_{124}$ ($u=4$, $\sigma=-8$) — signature alone is sharp.
- **All positive braid knots (Kronheimer–Mrowka 1993):** if $K$ is the closure of a positive braid on $n$ strands with $c$ crossings, then $u(K) = g_4(K) = g_3(K) = \frac{c-n+1}{2}$. Torus knots are the special case.
- **All algebraic links:** for the link of an isolated plane curve singularity, $g_4 = \delta$, the delta-invariant; the Milnor fibre is genus-minimising in $B^4$.
- **Quasipositive knots (Rudolph 1993, slice–Bennequin):** $g_4(K) = \frac{c-n+1}{2}$ for quasipositive braid closures — this uses the same Kronheimer–Mrowka input.
- **Cables and connected sums:** $g_4$ of iterated torus knots is additive in the expected way; $u$ of connected sums of torus knots is bounded below by the sum, though $u(K_1 \\# K_2) = u(K_1)+u(K_2)$ in general remains open.
- **Topological category, partial:** Rudolph and later Baader–Feller–Lewark–Liechti showed $g_4^{\mathrm{top}}(T_{p,q}) < g_4(T_{p,q})$ for large $p,q$, with asymptotic bounds; exact values are known only for $T_{2,q}$, $T_{3,q}$ and sporadic families.

## 5. Principal Obstacles

Why nothing elementary works, and why the strengthenings resist:

- **Unknotting number is not a diagrammatic quantity.** There is no bound on the crossing number of the diagram realising $u(K)$, so no finite search terminates. Every proof must pass to a 4-dimensional or homological invariant.
- **Classical concordance invariants are not sharp.** The signature bound $|\sigma|/2 \le g_4$ degrades: $|\sigma(T_{p,q})|/(2g_3(T_{p,q})) \to c < 1$ as $p,q \to \infty$ (the limiting behaviour was computed by Gambaudo–Ghys). Casson–Gordon invariants and metabelian obstructions likewise vanish or under-count. Any purely abelian-covering method loses a constant fraction of the genus.
- **Algebraic topology of the exterior sees only $g_3$.** The Alexander polynomial, Seifert form, and Milnor fibration all detect $g_3 = (p-1)(q-1)/2$, but $g_3$ is not a lower bound for $u$ — it is an upper bound chain in the wrong direction. One needs an invariant that is simultaneously $\le g_4$ and computes to $g_3$.
- **The gauge-theoretic input is nonlinear analysis.** The adjunction inequality relies on non-vanishing of Donaldson/Seiberg–Witten invariants of Kähler surfaces, i.e. on compactness and transversality for a nonlinear elliptic system. It does not survive weakening to the topological locally flat category, where surfaces need no smooth structure — which is exactly why $g_4^{\mathrm{top}}$ is smaller and much harder.
- **Khovanov route is combinatorial but opaque.** $s$ is computable in principle, but Khovanov homology has exponential complexity in crossing number, and the structural reason $s(T_{p,q}) = (p-1)(q-1)$ (Lee homology filtration jumps) does not obviously generalise to other genus questions.

## 6. The Gap

For the conjecture **as stated**, there is no gap: $u(T_{p,q}) = (p-1)(q-1)/2$ is a theorem for all coprime $p,q\ge 2$. The live boundary lies just beyond:

1. **Topological slice genus.** Determine $g_4^{\mathrm{top}}(T_{p,q})$ exactly. Known: $g_4^{\mathrm{top}} \le \frac{1}{2}\deg\Delta$ trivially and, by Feller (2016), $g_4^{\mathrm{top}}(K) \le \frac{1}{2}\deg\Delta_K$ for any $K$; and $\lim_{p,q\to\infty} g_4^{\mathrm{top}}(T_{p,q})/g_4(T_{p,q}) < 1$. No closed formula exists.
2. **Slice-torus uniqueness.** Are all slice-torus invariants equal? No — Lewark showed the $\mathfrak{sl}(N)$ invariants and $\tau$ are linearly independent. Classifying them is open.
3. **Unknotting number beyond positive braids.** $u(K)$ is unknown for infinitely many knots of low crossing number; no algorithm is known to compute $u$.
4. **Elementary proof.** No proof avoids either 4-manifold gauge theory or Khovanov/Floer homology. Whether a purely 3-dimensional or combinatorial argument exists is open.

## 7. Current Research (as of June 2026)

- **Topological 4-genus of torus knots.** Baader, Feller, Lewark, Liechti (Bern/Fribourg) and collaborators refine upper and lower bounds for $g_4^{\mathrm{top}}(T_{p,q})$; the ratio to the smooth genus is pinned between explicit constants but not determined. *(frontier — verify)*
- **Concordance invariants from link homology.** Work on $\Upsilon$, $\nu^+$, and $\mathfrak{sl}(N)$ invariants (Ozsváth–Stipsicz–Szabó; Lobb; Lewark) aims to separate the concordance classes of torus knots and to compute genus bounds for cables and satellites.
- **Unknotting numbers of specific small knots.** Brittenham and Hermiller have settled several long-standing table entries by combining Heegaard Floer obstructions with computer search over unknotting sequences. *(frontier — verify)*
- **Instanton vs. Floer comparisons.** Kronheimer–Mrowka's framed instanton homology continues to yield genus bounds not visible to Heegaard Floer; whether the two give the same $g_4$ bounds for all knots is open.
- **Khovanov skein lasagna modules** (Manolescu–Neithalath–Walker and successors) are being tested as genus obstructions for surfaces in general 4-manifolds, generalising the Thom-type statement beyond $B^4$. *(frontier — verify)*

## 8. Future Work

- Compute $g_4^{\mathrm{top}}(T_{p,q})$ exactly, or determine the limit $\lim g_4^{\mathrm{top}}(T_{p,q})/pq$.
- Find a proof of $s(T_{p,q}) = (p-1)(q-1)$ that extends to a general algorithm for $u$.
- Decide whether $u(K_1 \\# K_2) = u(K_1) + u(K_2)$ (additivity of unknotting number) — open even for torus knot summands.
- Extend the local Thom conjecture to surfaces in arbitrary negative-definite or symplectic 4-manifolds with prescribed boundary.
- Classify slice-torus homomorphisms $\mathcal{C}\to\mathbb{R}$ and determine the rank of the subgroup of $\mathcal{C}$ generated by torus knots.

## 9. Key References

- **[Foundational]** Milnor, J. *Singular Points of Complex Hypersurfaces.* Annals of Mathematics Studies 61, Princeton University Press, 1968.
- **[Foundational]** Boileau, M., Weber, C. *Le problème de J. Milnor sur le nombre gordien des nœuds algébriques.* L'Enseignement Mathématique 30 (1984), 173–222.
- **[Foundational]** Bennequin, D. *Entrelacements et équations de Pfaff.* Astérisque 107–108 (1983), 87–161.
- **[Solution]** Kronheimer, P. B., Mrowka, T. S. *Gauge theory for embedded surfaces, I.* Topology 32 (1993), 773–826.
- **[Solution]** Kronheimer, P. B., Mrowka, T. S. *The genus of embedded surfaces in the projective plane.* Mathematical Research Letters 1 (1994), 797–808.
- **[SOTA]** Rasmussen, J. *Khovanov homology and the slice genus.* Inventiones Mathematicae 182 (2010), 419–447.
- **[SOTA]** Ozsváth, P., Szabó, Z. *Knot Floer homology and the four-ball genus.* Geometry & Topology 7 (2003), 615–639.
- **[SOTA]** Lobb, A. *A slice genus lower bound from $sl(n)$ Khovanov–Rozansky homology.* Advances in Mathematics 222 (2009), 1220–1276.
- **[SOTA]** Baader, S., Feller, P., Lewark, L., Liechti, L. *On the topological 4-genus of torus knots.* Transactions of the American Mathematical Society 370 (2018), 2639–2656.
- **[Recent]** Feller, P. *The degree of the Alexander polynomial is an upper bound for the topological slice genus.* Geometry & Topology 20 (2016), 1763–1771.
- **[Recent]** Lewark, L. *Rasmussen's spectral sequences and the $\mathfrak{sl}_N$-concordance invariants.* Advances in Mathematics 260 (2014), 59–83.
- **[Survey]** Rudolph, L. *Quasipositivity as an obstruction to sliceness.* Bulletin of the AMS 29 (1993), 51–59.
- **[Survey]** Livingston, C. *A survey of classical knot concordance.* In: Handbook of Knot Theory, Elsevier, 2005, 319–347.
- **[Survey]** Gambaudo, J.-M., Ghys, É. *Braids and signatures.* Bulletin de la Société Mathématique de France 133 (2005), 541–579.

## 10. Worked Example / Concrete Special Case

**The $(3,4)$ torus knot $T_{3,4} = 8_{19}$.**

*Predicted value:* $u = \frac{(3-1)(4-1)}{2} = 3$.

**Step 1 — Braid presentation and Seifert genus.** $T_{3,4}$ is the closure of $\beta = (\sigma_1\sigma_2)^4 \in B_3$: $n = 3$ strands, $c = 8$ positive crossings. Seifert's algorithm on the closed braid diagram gives 3 Seifert circles, so the resulting surface $F$ has
$$\chi(F) = n - c = 3 - 8 = -5, \qquad g_3 = \frac{1-\chi}{2} = \frac{c-n+1}{2} = \frac{8-3+1}{2} = 3.$$

**Step 2 — Alexander polynomial check.**
$$\Delta_{T_{3,4}}(t) = \frac{(t^{12}-1)(t-1)}{(t^{3}-1)(t^{4}-1)} = t^6 - t^5 + t^3 - t + 1,$$
of degree $6 = 2g_3$, confirming that the Milnor fibre is a minimal-genus Seifert surface.

**Step 3 — Upper bound $u \le 3$.** Use the standard reduction: changing $\frac{p(p-1)}{2} = 3$ crossings in the closed braid $(\sigma_1\sigma_2)^q$ removes one full twist and converts $T_{3,q}$ into $T_{3,q-3}$. Applying this once,
$$T_{3,4} \xrightarrow{\ 3 \text{ crossing changes}\ } T_{3,1} = \text{unknot}.$$
Hence $u(T_{3,4}) \le 3$.

**Step 4 — Lower bound $u \ge 3$.** Three independent certificates:
- *Signature:* $\sigma(T_{3,4}) = -6$, and $u(K) \ge g_4(K) \ge |\sigma(K)|/2 = 3$.
- *Rasmussen:* $s(T_{3,4}) = (3-1)(4-1) = 6$, and $u \ge g_4 \ge s/2 = 3$.
- *Ozsváth–Szabó:* $\tau(T_{3,4}) = 3$, and $u \ge g_4 \ge \tau = 3$.

**Conclusion.** $u(T_{3,4}) = g_4(T_{3,4}) = g_3(T_{3,4}) = 3$.

**Where the easy argument breaks.** For $T_{3,4}$ the signature $|\sigma|/2 = 3$ already matches, so the case is classical. But $|\sigma(T_{p,q})|$ grows strictly slower than $2g_3(T_{p,q}) = (p-1)(q-1)$ as $p,q\to\infty$ (Gambaudo–Ghys), so for large $p,q$ the signature certifies only a constant fraction $c<1$ of the required bound. Closing that fraction to $1$ is precisely what Kronheimer–Mrowka's adjunction inequality — or Rasmussen's $s$ — supplies, and why no classical invariant sufficed between 1968 and 1993.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*