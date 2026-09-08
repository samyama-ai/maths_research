---
id: 03-geometry/audin-conjecture
title: "Audin Conjecture on Maslov Class of Lagrangian Tori"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Audin Conjecture on Maslov Class of Lagrangian Tori

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/audin-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Audin's conjecture (1988).** Let $L \subset (\mathbb{R}^{2n}, \omega_{\mathrm{std}})$ be a smoothly embedded Lagrangian submanifold diffeomorphic to the torus $T^n = (S^1)^n$. Then the minimal Maslov number of $L$ is exactly $2$:
$$N_L := \min\{\,\mu_L(A) > 0 \;:\; A \in \pi_2(\mathbb{R}^{2n}, L)\,\} = 2 .$$

Equivalently, the Maslov homomorphism $\mu_L : H_1(L;\mathbb{Z}) \cong \mathbb{Z}^n \to \mathbb{Z}$ is surjective onto $2\mathbb{Z}$ — never zero, and never a proper subgroup $2k\mathbb{Z}$ with $k \ge 2$.

A complete proof must (i) exclude $\mu_L = 0$ and (ii) exclude $N_L \ge 4$, for *every* embedded torus, with no monotonicity, genericity, or displaceability hypothesis. **The conjecture as stated for $\mathbb{R}^{2n}$ was proved by Cieliebak–Mohnke (Invent. Math., 2018).** The entry is catalogued as *partially-solved* because the surrounding programme Audin posed — the same statement for Lagrangian tori in general symplectically aspherical or uniruled targets, and for arbitrary aspherical Lagrangians — remains open in most cases (§6, §7).

## 2. Mathematical Foundations

**Lagrangian Grassmannian and the Maslov index.** Let $\Lambda(n)$ be the space of Lagrangian $n$-planes in $(\mathbb{R}^{2n}, \omega_{\mathrm{std}})$. Then $\Lambda(n) \cong U(n)/O(n)$, and the squared-determinant map
$$\det{}^2 : \Lambda(n) \to S^1, \qquad A\cdot O(n) \mapsto \det(A)^2$$
induces an isomorphism $\pi_1(\Lambda(n)) \xrightarrow{\ \cong\ } \mathbb{Z}$. Its generator is the **Maslov class** $\mu \in H^1(\Lambda(n);\mathbb{Z})$.

**Maslov class of a Lagrangian submanifold.** For $L^n \subset \mathbb{R}^{2n}$ Lagrangian, the Gauss map $G_L : L \to \Lambda(n)$, $x \mapsto T_xL$, gives
$$\mu_L := G_L^{*}\mu \in H^1(L;\mathbb{Z}), \qquad \mu_L : H_1(L;\mathbb{Z}) \to \mathbb{Z}.$$
Because $\pi_2(\mathbb{R}^{2n},L)\to \pi_1(L)$ is onto for $L$ in a vector space, this agrees with the disc-index normalisation: for $u : (D^2,\partial D^2)\to(\mathbb{R}^{2n},L)$, $\mu_L([u])$ is the Maslov index of the loop of Lagrangian planes $t \mapsto T_{u(e^{2\pi i t})}L$ trivialised over $u$.

**Parity constraint.** Under $\det^2$, the mod-2 reduction satisfies
$$\mu_L \equiv w_1(L) \pmod 2 ,$$
so an *orientable* $L$ — in particular a torus — has even Maslov class, hence $N_L \in 2\mathbb{Z}_{>0}$ whenever $\mu_L \neq 0$. This is why the conjecture asserts $2$ and not $1$.

**Gromov's theorem (1985).** There is no closed *exact* Lagrangian submanifold of $\mathbb{C}^n$; the proof produces, for any tame almost complex structure $J$ and any $L$, a nonconstant $J$-holomorphic disc with boundary on $L$. Combined with a positivity/index argument this gives $\mu_L \neq 0$, settling part (i) of §1.

**Monotonicity.** $L$ is *monotone* if $\omega(A) = \tau\,\mu_L(A)$ for some $\tau>0$ and all $A \in \pi_2(\mathbb{R}^{2n},L)$. For monotone $L$ with $N_L \ge 2$, Floer homology $HF_*(L,L)$ is defined over $\mathbb{Z}/2$, is $\mathbb{Z}/N_L$-graded, vanishes in $\mathbb{C}^n$ (since $L$ is displaceable), and Oh's spectral sequence
$$E_1^{p,q} \Rightarrow HF_*(L,L) = 0, \qquad E_1 \cong H_*(L;\mathbb{Z}/2)\otimes \Lambda ,$$
with differentials $d_r$ of degree $(-r, r-1)$ shifting by $N_L$, forces $N_L$ to be small relative to $\dim L$: if $N_L > n+1$ the spectral sequence degenerates and $H_*(L)\neq 0$ contradicts $HF_*=0$.

## 3. History & State of the Art (SOTA)

- **1988 — Audin.** Michèle Audin, studying double points of Lagrangian immersions and normal bundles, formulated the conjecture in *Comment. Math. Helv.* **63** (1988). The motivation: the Clifford torus and all then-known examples have $N_L=2$, and $N_L=2$ is exactly what makes the "index-2 disc" mechanism of Gromov's argument sharp.
- **1985 — Gromov.** Pseudoholomorphic curves give $\mu_L \neq 0$ for all closed Lagrangians in $\mathbb{C}^n$; the qualitative half of the conjecture.
- **1990 — Viterbo.** *A new obstruction to embedding Lagrangian tori* (Invent. Math. 100) proves $N_L \le n+1$ for Lagrangian tori in $\mathbb{R}^{2n}$, via a generating-function / loop-space argument. With the parity constraint this closes $n=2$.
- **1991 — Polterovich.** Independent proof for Lagrangian surfaces in $\mathbb{R}^4$ using Gromov's curves (Trans. AMS 325).
- **1996 — Oh.** Floer-theoretic spectral sequence for monotone Lagrangians, recovering $N_L \le n+1$ in the monotone case and structuring later work.
- **2006 — Fukaya.** Floer homology of Lagrangian submanifolds applied to $T^3 \subset \mathbb{R}^6$, giving $n=3$.
- **2010 — Buhovsky.** Quantum products in Floer cohomology sharpen the bound to $N_L \le \tfrac{n+2}{2}$ for tori; with parity this yields $N_L=2$ for $n \le 4$.
- **2012 — Damian.** Lifted Floer homology on the universal cover proves $N_L=2$ for monotone Lagrangian tori in $\mathbb{R}^{2n}$, all $n$, and for a wider class of aspherical monotone Lagrangians.
- **2018 — Cieliebak–Mohnke.** *Punctured holomorphic curves and Lagrangian embeddings* (Invent. Math. 212) proves the full conjecture for all $n$, with no monotonicity assumption, by neck-stretching in the complement of a Donaldson-type divisor and a virtual/perturbation scheme adapted to punctured curves.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| Any closed $L \subset \mathbb{C}^n$ | $\mu_L \neq 0$; some disc of positive index exists | Gromov 1985 |
| $T^n \subset \mathbb{R}^{2n}$, all $n$ | $N_L \le n+1$ | Viterbo 1990 |
| $n=2$ ($T^2 \subset \mathbb{R}^4$) | $N_L = 2$ | Viterbo 1990; Polterovich 1991 |
| $n=3$ | $N_L = 2$ | Fukaya 2006 |
| $T^n$, all $n$ | $N_L \le \lfloor (n+2)/2\rfloor$, hence $N_L=2$ for $n \le 4$ | Buhovsky 2010 |
| Monotone $T^n \subset \mathbb{R}^{2n}$, all $n$; monotone aspherical $L$ with suitable $\pi_1$ | $N_L = 2$ | Damian 2012 |
| Monotone $L\subset \mathbb{C}^n$ with $H^1(L;\mathbb{Z}/2)\neq 0$ | $N_L \le n+1$ via Oh's spectral sequence | Oh 1996 |
| General $T^n \subset \mathbb{R}^{2n}$, all $n$ | $N_L = 2$ (conjecture proved) | Cieliebak–Mohnke 2018 |
| $T^n$ in symplectically aspherical, convex-at-infinity $(M^{2n},\omega)$ | Open in general; known for uniruled/monotone special cases | — |

Related sharp companion result: any Lagrangian torus in $\mathbb{C}^n$ bounds a holomorphic disc of Maslov index $2$ and symplectic area at most the Gromov width of any ball it is contained in, giving displacement-energy bounds.

## 5. Principal Obstacles

- **Loss of monotonicity kills the algebra.** Oh's spectral sequence and Damian's lifted Floer homology need $HF_*(L,L)$ to be well defined over a $\mathbb{Z}/N_L$-graded Novikov ring; for a general (non-monotone) torus, disc bubbling of index $\le 0$ and multiply-covered configurations obstruct $\partial^2=0$. Full Fukaya-category machinery (Kuranishi structures / polyfolds) is needed just to write a differential.
- **Non-transversality of multiple covers.** Discs of Maslov index $0$ appear in limits; the relevant moduli spaces are not cut out transversally by any generic $J$, so classical Gromov compactness plus Sard–Smale fails.
- **No control on which classes carry discs.** Gromov's argument yields *some* disc; extracting one of index exactly $2$ requires a chain-level count in a specific homology class, i.e. a numerical invariant rather than a nonvanishing statement.
- **Topological invariants are blind.** $\mu_L$ mod 2 is all that Stiefel–Whitney theory sees; there is no purely algebraic-topological obstruction to a Lagrangian immersion of $T^n$ with $N_L=4$ — indeed such *immersions* exist by the $h$-principle (Gromov–Lees). The conjecture is genuinely about embeddings and needs a curve-count.
- **Perturbation-theoretic method (Cieliebak–Mohnke) is delicate.** It replaces generic $J$ by stretching the neck along a Donaldson hypersurface, converting discs to punctured spheres; the compactness and gluing theory for punctured curves with Lagrangian boundary is the technical core and does not transfer verbatim to arbitrary targets.

## 6. The Gap

For $L = T^n \subset \mathbb{R}^{2n}$ there is now no gap: the statement is a theorem. The live boundary is one dimension up in generality:

1. **Ambient generality.** For $L \cong T^n$ Lagrangian in a symplectically aspherical, geometrically bounded $(M^{2n},\omega)$ (e.g. $T^*Q$, or a Liouville domain), is $N_L=2$? Cieliebak–Mohnke's divisor construction requires a compatible integral/rational symplectic form and a controlled Donaldson hypersurface; extending it to all such $M$ is the open technical step.
2. **Non-torus aspherical Lagrangians.** Audin-type prediction: any closed aspherical $L \subset \mathbb{C}^n$ has $N_L=2$. Damian's universal-cover Floer homology handles monotone cases with amenable/hyperbolic-type $\pi_1$; the non-monotone aspherical case is open.
3. **Uniqueness beyond the index.** Even with $N_L=2$ known, classification of Lagrangian tori up to Hamiltonian isotopy (Clifford vs. Chekanov vs. Vianna's infinite families) is far from settled.

## 7. Current Research (as of June 2026)

- **Cieliebak–Mohnke school (Augsburg, HU Berlin).** Extending punctured-curve technology to Liouville and Weinstein domains; the target is a "relative Audin theorem" for cotangent bundles. *(frontier — verify)*
- **Biran–Cornea (ETH Zürich / Montréal).** Lagrangian cobordism and uniruling: $L$ uniruled by index-2 discs implies Audin-type bounds; ongoing work exports uniruling to non-monotone settings via Novikov-field cobordism categories.
- **Exotic-torus programme.** Auroux, Vianna, Pascaleff–Tonkonog: mutation and cluster structures generate infinitely many monotone Lagrangian tori in $\mathbb{R}^6$ and $\mathbb{CP}^2$ — all with $N_L=2$, providing systematic tests of any conjectural strengthening.
- **Microlocal / sheaf-theoretic attacks.** Nadler–Zaslow-style categorification is being used to bound Maslov indices in cotangent bundles without transversality; still restricted to exact settings. *(frontier — verify)*

## 8. Future Work

- Prove $N_L = 2$ for Lagrangian tori in all symplectically aspherical manifolds convex at infinity, by making Donaldson hypersurfaces available in the non-rational/non-compact case.
- Upgrade the disc count to a quantitative statement: bound the *area* of the index-2 disc by an ambient invariant (Gromov width, displacement energy) in general targets, extending the $\mathbb{C}^n$ estimate.
- Settle the aspherical case: is $N_L = 2$ for $L=\Sigma_g \times T^{n-2}$ or any $K(\pi,1)$ Lagrangian in $\mathbb{C}^n$?
- Determine the possible values of $N_L$ for non-orientable Lagrangians (where $N_L$ may be odd) and the sharp analogue of the $(n+2)/2$ bound.
- Combine Maslov rigidity with classification: does $N_L=2$ plus a disc-potential computation determine the torus up to Hamiltonian isotopy in low dimensions?

## 9. Key References

- **[Foundational]** M. Audin. *Fibrés normaux d'immersions en dimension double, points doubles d'immersions lagrangiennes et plongements totalement réels.* Commentarii Mathematici Helvetici **63** (1988), 593–623.
- **[Foundational]** M. Gromov. *Pseudo holomorphic curves in symplectic manifolds.* Inventiones Mathematicae **82** (1985), 307–347.
- **[Foundational]** C. Viterbo. *A new obstruction to embedding Lagrangian tori.* Inventiones Mathematicae **100** (1990), 301–320.
- **[Foundational]** L. Polterovich. *The Maslov class of the Lagrange surfaces and Gromov's pseudo-holomorphic curves.* Transactions of the AMS **325** (1991), 241–248.
- **[Structural]** Y.-G. Oh. *Floer cohomology, spectral sequences, and the Maslov class of Lagrangian embeddings.* International Mathematics Research Notices **1996**, no. 7, 305–346.
- **[Partial result]** K. Fukaya. *Application of Floer homology of Lagrangian submanifolds to symplectic topology.* In *Morse Theoretic Methods in Nonlinear Analysis and in Symplectic Topology*, NATO Science Series II vol. 217, Springer, 2006, 231–276.
- **[Partial result]** L. Buhovsky. *The Maslov class of Lagrangian tori and quantum products in Floer cohomology.* Journal of Topology and Analysis **2** (2010), 57–75.
- **[Partial result]** M. Damian. *Floer homology on the universal cover, Audin's conjecture and other constraints on Lagrangian submanifolds.* Commentarii Mathematici Helvetici **87** (2012), 433–462.
- **[SOTA / Recent]** K. Cieliebak, K. Mohnke. *Punctured holomorphic curves and Lagrangian embeddings.* Inventiones Mathematicae **212** (2018), 213–295.
- **[Related]** P. Biran, O. Cornea. *Rigidity and uniruling for Lagrangian submanifolds.* Geometry & Topology **13** (2009), 2881–2989.
- **[Examples]** Yu. Chekanov. *Lagrangian tori in a symplectic vector space and global symplectomorphisms.* Mathematische Zeitschrift **223** (1996), 547–559.
- **[Examples]** D. Auroux. *Infinitely many monotone Lagrangian tori in $\mathbb{R}^6$.* Inventiones Mathematicae **201** (2015), 909–924.
- **[Examples]** R. Vianna. *On exotic Lagrangian tori in $\mathbb{CP}^2$.* Geometry & Topology **18** (2014), 2419–2476.
- **[Survey]** M. Audin, F. Lalonde, L. Polterovich. *Symplectic rigidity: Lagrangian submanifolds.* In *Holomorphic Curves in Symplectic Geometry*, Progress in Mathematics 117, Birkhäuser, 1994, 271–321.

## 10. Worked Example / Concrete Special Case

**The Clifford torus in $\mathbb{C}^n$: verifying $N_L=2$ by direct computation.**

Fix radii $r_1,\dots,r_n>0$ and set
$$L = T(r_1,\dots,r_n) = \{\,z \in \mathbb{C}^n : |z_j| = r_j,\ j=1,\dots,n\,\}.$$
With $\omega = \sum_j dx_j \wedge dy_j$ and $z_j = \rho_j e^{i\theta_j}$, one has $\omega = \sum_j \rho_j\, d\rho_j \wedge d\theta_j$, which vanishes on $L$ since $d\rho_j|_L = 0$. So $L$ is Lagrangian, and $L \cong T^n$.

*Step 1 — the Gauss map.* At $z \in L$ the tangent space is spanned by $v_j = i e^{i\theta_j} e_j$ (the angular direction in factor $j$). Writing $T_zL = A(z)\cdot \mathbb{R}^n$ with
$$A(z) = \mathrm{diag}\!\left(i e^{i\theta_1},\dots, i e^{i\theta_n}\right) \in U(n),$$
we get
$$\det{}^2 A(z) = \prod_{j=1}^n \left(i e^{i\theta_j}\right)^2 = (-1)^n e^{2i(\theta_1+\cdots+\theta_n)} .$$

*Step 2 — the Maslov class on generators.* Let $\gamma_k \subset L$ be the loop $\theta_k : 0 \to 2\pi$, all other angles fixed. Then along $\gamma_k$,
$$\det{}^2 A = (-1)^n e^{2i\theta_k}\cdot \text{const},$$
which winds **twice** around $S^1$. Hence
$$\mu_L([\gamma_k]) = 2 \quad \text{for every } k=1,\dots,n .$$
So $\mu_L(m_1,\dots,m_n) = 2\sum_k m_k$, the image is exactly $2\mathbb{Z}$, and $N_L = 2$.

*Step 3 — the geometric disc realising it.* The class $[\gamma_k]$ is filled by the holomorphic disc
$$u_k : D^2 \to \mathbb{C}^n, \qquad u_k(w) = (r_1 e^{i\theta_1},\dots, r_k w, \dots, r_n e^{i\theta_n}),$$
of symplectic area $\omega(u_k) = \pi r_k^2$ and Maslov index $2$. These $n$ discs are exactly the index-2 discs whose existence Gromov's theorem guarantees abstractly and whose *count* (here: $n$ families, giving the Landau–Ginzburg potential $W = \sum_k z_k$ after normalisation) is the mechanism Cieliebak–Mohnke make work for an arbitrary torus.

*Step 4 — monotonicity.* If $r_1 = \cdots = r_n = r$, then $\omega(A) = \tfrac{\pi r^2}{2}\,\mu_L(A)$ on all of $\pi_2(\mathbb{C}^n,L)$, so $L$ is monotone with $\tau = \pi r^2/2$; this is the case covered by Oh's spectral sequence and Damian's theorem. The content of the general conjecture is that even for a wildly embedded, non-monotone torus — where no such potential is computable and no transversality is available — the answer is the same integer $2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*