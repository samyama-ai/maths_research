---
id: 04-topology/szabos-geometric-spectral-sequence
title: "Szabo's Geometric Spectral Sequence"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Szabó's Geometric Spectral Sequence

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/szabos-geometric-spectral-sequence` · **Status:** open

## 1. Problem Statement / Conjecture

Ozsváth and Szabó (2005) constructed a spectral sequence whose $E_2$ page is the reduced Khovanov homology $\widetilde{Kh}(\bar L;\mathbb{F}_2)$ of the mirror of a link $L\subset S^3$ and which converges to the Heegaard Floer homology $\widehat{HF}(\Sigma(L);\mathbb{F}_2)$ of the double cover of $S^3$ branched over $L$. Its higher differentials are defined by counting holomorphic polygons in a Heegaard multi-diagram and are not computable from the diagram of $L$.

In 2015 Szabó defined a purely combinatorial spectral sequence — the *geometric spectral sequence* — by adding explicit higher maps to the Khovanov cube of resolutions over $\mathbb{F}_2$. Write $E_r^{\mathrm{Sz}}(L)$ for its pages.

**Conjecture (Szabó).** For every link $L\subset S^3$,
$$E_\infty^{\mathrm{Sz}}(L)\;\cong\;\widehat{HF}\bigl(\Sigma(L);\mathbb{F}_2\bigr),$$
and more strongly, $E_r^{\mathrm{Sz}}(L)$ agrees with the Ozsváth–Szabó spectral sequence for all $r\ge 2$, including the filtration and the induced gradings.

A complete proof requires a filtered chain homotopy equivalence between Szabó's total complex $(CKh(\bar L;\mathbb{F}_2), D_{\mathrm{tot}})$ and the link-surgery hypercube computing $\widehat{HF}(\Sigma(L))$ — not merely equality of ranks. A disproof needs a single link where the $E_\infty$ ranks differ.

## 2. Mathematical Foundations

Let $D$ be a diagram of $L$ with $n$ crossings, $n_+$ positive and $n_-$ negative. For $v\in\{0,1\}^n$ let $D_v$ be the complete resolution with $|D_v|$ circles. With $V=\mathbb{F}_2\langle x_+,x_-\rangle$, the Khovanov chain group is
$$CKh(D)=\bigoplus_{v\in\{0,1\}^n} V^{\otimes |D_v|},$$
graded by $i=|v|-n_-$ and $j=\deg(x)+|v|+n_+-2n_-$, where $\deg$ counts $x_+$ as $+1$ and $x_-$ as $-1$. Khovanov's differential is the sum over cube edges of the merge $m$ and the split $\Delta$ of the Frobenius algebra $V$ (Khovanov 2000).

**Configurations.** For $u\le v$ in $\{0,1\}^n$ with $k=|v|-|u|$, the crossings where $u_i=0,v_i=1$ determine $k$ disjoint embedded *arcs* $A$ attached to the circles of $D_u$; surgering along them yields $D_v$. The pair $C=(D_u,A)$ is a **configuration**. A circle is *active* if it meets an arc, *passive* otherwise. Szabó classifies connected configurations by the dual graph and the surface obtained by attaching the $k$ bands, into types $A$ (a single arc), $B$, $C$, $D$, $E$, and assigns to each an explicit $\mathbb{F}_2$-linear map
$$D_C:\;V^{\otimes|D_u|}\longrightarrow V^{\otimes|D_v|}$$
(Szabó 2015, §3–§4); $D_C=0$ unless $C$ decomposes into these essential pieces, and passive circles act by the identity. Type $A$ recovers $m$ and $\Delta$. Setting
$$D_{\mathrm{tot}}=\sum_{u\le v} D_{u,v},\qquad D_{u,v}=D_{C(u,v)},$$
Szabó's main algebraic theorem is
$$D_{\mathrm{tot}}^{\,2}=0 .$$
The term $D_{u,v}$ raises homological grading by $k$ and lowers quantum grading by $2(k-1)$; the filtration by $|v|$ gives a spectral sequence with
$$E_1 = CKh(D),\qquad E_2 = Kh(L;\mathbb{F}_2),$$
and Szabó proves that $E_r$ for $r\ge 2$ is a link invariant. There is a reduced variant with $E_2=\widetilde{Kh}(L;\mathbb{F}_2)$.

Because Khovanov's differential shifts $\delta=j-2i$ by $-2$ and the $k$-th term shifts it by $-(4k-2)$, all higher differentials vanish on complexes supported in a single $\delta$-grading. This is the source of every proved case in §4.

The target: $\Sigma(L)$ is the branched double cover, $|H_1(\Sigma(L);\mathbb{Z})|=\det(L)$ when $L$ has non-zero determinant, and
$$\operatorname{rk}_{\mathbb{F}_2}\widehat{HF}(\Sigma(L);\mathbb{F}_2)\;\ge\;\det(L),$$
with equality exactly when $\Sigma(L)$ is an $\mathbb{F}_2$-L-space.

## 3. History & State of the Art (SOTA)

- **2005.** Ozsváth–Szabó construct the branched-double-cover spectral sequence, the first bridge between Khovanov homology and Floer theory (*Adv. Math.* 194).
- **2007–08.** Manolescu–Ozsváth prove quasi-alternating links are $\delta$-thin with $\operatorname{rk}\widetilde{Kh}=\det$, forcing collapse at $E_2$.
- **2010–11.** Bloom builds the monopole-Floer analogue; Kronheimer–Mrowka build the instanton analogue and prove Khovanov homology detects the unknot. Baldwin proves the OS pages $E_r$, $r\ge2$, are link invariants.
- **2010/2015.** Szabó posts (arXiv:1010.4252) and publishes *A geometric spectral sequence in Khovanov homology* (*J. Topology* 8), giving the combinatorial candidate and stating the identification conjecture.
- **2013–17.** Cotton Seed implements the differential in `knotkit` and computes it for large tables of knots; Sarkar–Seed–Szabó publish a perturbation of the theory (*Quantum Topology* 8, 2017) producing a Lee-type deformation and a family of $\mathbb{F}_2$ concordance invariants.
- **2019.** Baldwin–Hedden–Lobb axiomatise "Khovanov–Floer theories" and prove functoriality and $E_2$-invariance for the OS, Bloom, and Kronheimer–Mrowka sequences (*Adv. Math.* 345).

State of the art: the two spectral sequences are known to agree at $E_2$ by construction, to agree wholesale on all $\delta$-thin links, and to agree in every computed example; no conceptual identification exists.

## 4. Partial Results / Verified Cases

- **Quasi-alternating links** (including all non-split alternating links, so all prime knots through 8 crossings except $8_{19},8_{20},8_{21}$): reduced homology is $\delta$-thin of rank $\det(L)$, both sequences collapse at $E_2$, and $\Sigma(L)$ is an L-space — conjecture holds.
- **All $\delta$-thin links** with $\operatorname{rk}\widetilde{Kh}(L;\mathbb{F}_2)=\det(L)$: the same argument applies over $\mathbb{F}_2$, covering e.g. all two-bridge links (whose branched covers are lens spaces).
- **Unknot, unlinks, connected sums of the above**: both sides multiplicative, agreement immediate.
- **$E_2$-page identification**: holds for every link, by construction on both sides (Ozsváth–Szabó 2005; Szabó 2015).
- **Rank inequality**: $\operatorname{rk} E_\infty^{\mathrm{Sz}}\ge \det(L)$ holds by the same Euler-characteristic argument as on the Floer side, since $\chi(E_\infty)=\pm\det(L)$.
- **Computational verification**: Seed's `knotkit` computations of $E_\infty^{\mathrm{Sz}}$ for prime knots in the standard tables (through 14 crossings, and many larger examples) match $\operatorname{rk}\widehat{HF}(\Sigma(K))$ in every case checked *(frontier — verify the exact crossing bound against Seed's data)*.
- **Perturbed theory**: Sarkar–Seed–Szabó prove their perturbation of $D_{\mathrm{tot}}$ squares to zero, is a link invariant, and yields homology of rank $2^{|L|}$ for the perturbed Lee-type deformation, mirroring the Floer-side behaviour with twisted coefficients.

## 5. Principal Obstacles

- **No combinatorial model for polygon counts.** The OS higher differentials count pseudo-holomorphic $(k+2)$-gons in $\mathrm{Sym}^g(\Sigma)$ for a Heegaard multi-diagram of the surgery hypercube. No formula expresses these counts in terms of the link diagram; matching them with $D_C$ requires either a combinatorial evaluation of the polygon counts (unknown beyond low $k$) or an abstract uniqueness theorem.
- **Filtered complexes are not determined by $E_2$.** Two filtered chain complexes with isomorphic $E_2$ pages and equal Euler characteristics can have non-isomorphic $E_\infty$; the identification is a statement about higher $A_\infty$ structure, invisible to homology-level bookkeeping.
- **No cobordism maps in Szabó's theory.** The standard proof technique for Floer-theoretic identifications — naturality under link cobordism plus a skein-tree induction — is unavailable because functoriality of the geometric sequence under cobordisms is not established, so the Baldwin–Hedden–Lobb machine cannot yet be applied off the shelf.
- **Grading mismatch.** $\widehat{HF}(\Sigma(L))$ splits over $\mathrm{Spin}^c(\Sigma(L))$ with $\mathbb{Q}$-valued absolute gradings; Szabó's complex carries only the cube filtration and $\delta$. No $\mathrm{Spin}^c$ decomposition of the geometric complex is known, so even the strong form of the conjecture lacks a well-posed grading statement.
- **Characteristic 2 only.** Szabó's maps are defined over $\mathbb{F}_2$; the sign assignments needed for an integral or odd version are unknown, blocking any argument that would compare with $\mathbb{Z}$-coefficient Floer theory.

## 6. The Gap

Proved: agreement at $E_2$ for all links, and agreement of the whole sequence whenever $\delta$-thinness forces both to degenerate — a class where *no* higher differential is nonzero on either side. Conjectured: agreement whenever higher differentials are nontrivial, i.e. exactly the cases that carry information.

The precise missing step is a chain-level comparison: produce a filtered quasi-isomorphism
$$\Phi:\bigl(CKh(\bar L;\mathbb{F}_2),D_{\mathrm{tot}}\bigr)\;\longrightarrow\;\bigl(\mathrm{CF}(\text{surgery hypercube of }\Sigma(L)),\textstyle\sum \mathcal{D}_{u,v}\bigr)$$
inducing the identity on $E_2=\widetilde{Kh}$. Equivalently: show that Szabó's configuration maps $D_C$ compute the holomorphic-polygon maps $\mathcal{D}_{u,v}$ of the branched-cover hypercube, at least up to filtered homotopy. Not even the first genuinely higher term ($k=2$) has been matched in general.

## 7. Current Research (as of June 2026)

- **Bordered and algebraic models.** Lipshitz–Ozsváth–Thurston bordered Floer homology, and Szabó's and Ozsváth–Szabó's bordered knot-Floer algebras, are the main route to a hypercube computation local in the crossings — the structure needed to compare with a cube-of-resolutions formula. Manion and Manion–Rouquier's higher-representation-theoretic reformulations of these algebras are the most active branch *(frontier — verify current status)*.
- **Khovanov–Floer theories.** Extending Baldwin–Hedden–Lobb's axioms to cover Szabó's construction would give functoriality and could reduce the conjecture to a skein induction; whether the geometric sequence is a Khovanov–Floer theory is an open technical question *(frontier — verify)*.
- **Stable-homotopy comparisons.** Lipshitz–Sarkar's Steenrod square $Sq^2$ on Khovanov homology gives a computable operation to test against the $k=2$ term of $D_{\mathrm{tot}}$; comparisons of $d_2$ with the dual of $Sq^2$ have been made computationally *(frontier — verify)*.
- **Perturbations and concordance.** Sarkar–Seed–Szabó's deformed differentials produce $s$-type invariants over $\mathbb{F}_2$; determining whether these equal Rasmussen's $s$ mod 2 is an active side question with independent interest.
- **Large-scale computation.** Extensions of `knotkit`-style computation to 16–17 crossing knots and to links, checked against `HFHat` computations of branched covers.

## 8. Future Work

1. Match $D_{u,v}$ for $k=2$ with the OS triangle maps in a controlled family (e.g. pretzel links, torus links), giving the first non-formal evidence.
2. Establish cobordism functoriality for the geometric sequence, then run the Baldwin–Hedden–Lobb argument to at least identify $E_3$.
3. Lift $D_{\mathrm{tot}}$ to $\mathbb{Z}$ or to the odd Khovanov setting; an integral lift would predict the corresponding refinement on the Floer side.
4. Find a $\mathrm{Spin}^c$-refinement of the configuration maps, splitting the geometric sequence in a way matching $\widehat{HF}(\Sigma(L),\mathfrak{s})$.
5. Search deliberately for a counterexample among thick knots with small determinant, where $E_\infty$ ranks are most constrained.

## 9. Key References

- **[Foundational]** M. Khovanov. *A categorification of the Jones polynomial.* Duke Mathematical Journal 101 (2000), 359–426. [DOI](https://doi.org/10.1215/s0012-7094-00-10131-7)
- **[Foundational]** P. Ozsváth, Z. Szabó. *On the Heegaard Floer homology of branched double-covers.* Advances in Mathematics 194 (2005), 1–33. [DOI](https://doi.org/10.1016/j.aim.2004.05.008)
- **[Foundational]** Z. Szabó. *A geometric spectral sequence in Khovanov homology.* Journal of Topology 8 (2015), no. 4, 1017–1044. (arXiv:1010.4252). [DOI](https://doi.org/10.1112/jtopol/jtv027)
- **[SOTA / Recent]** S. Sarkar, C. Seed, Z. Szabó. *A perturbation of the geometric spectral sequence in Khovanov homology.* Quantum Topology 8 (2017), no. 3, 413–457. [DOI](https://doi.org/10.4171/qt/97)
- **[SOTA / Recent]** J. A. Baldwin, M. Hedden, A. Lobb. *On the functoriality of Khovanov–Floer theories.* Advances in Mathematics 345 (2019), 1162–1205. [DOI](https://doi.org/10.1016/j.aim.2019.01.026)
- **[SOTA / Recent]** J. A. Baldwin. *On the spectral sequence from Khovanov homology to Heegaard Floer homology.* International Mathematics Research Notices 2011, no. 15, 3426–3470. [DOI](https://doi.org/10.1093/imrn/rnq220)
- **[SOTA / Recent]** R. Lipshitz, S. Sarkar. *A Steenrod square on Khovanov homology.* Journal of Topology 7 (2014), 817–848. [DOI](https://doi.org/10.1112/jtopol/jtu005)
- **[Related]** C. Manolescu, P. Ozsváth. *On the Khovanov and knot Floer homologies of quasi-alternating links.* Proceedings of the Gökova Geometry-Topology Conference 2007, 60–81, 2008.
- **[Related]** J. M. Bloom. *A link surgery spectral sequence in monopole Floer homology.* Advances in Mathematics 226 (2011), 3216–3281. [DOI](https://doi.org/10.1016/j.aim.2010.10.014)
- **[Related]** P. B. Kronheimer, T. S. Mrowka. *Khovanov homology is an unknot-detector.* Publications Mathématiques de l'IHÉS 113 (2011), 97–208. [DOI](https://doi.org/10.1007/s10240-010-0030-y)
- **[Related]** R. Lipshitz, P. Ozsváth, D. Thurston. *Bordered Heegaard Floer homology.* Memoirs of the American Mathematical Society, vol. 254, no. 1216, 2018.
- **[Survey]** P. Turner. *Five lectures on Khovanov homology.* Journal of Knot Theory and Its Ramifications 26 (2017), no. 3. [DOI](https://doi.org/10.1142/s0218216517410097)
- **[Software]** C. Seed. *knotkit* — computer program for Khovanov homology and the Szabó spectral sequence.

## 10. Worked Example / Concrete Special Case

**Right-handed trefoil $3_1=T_{2,3}$.** Take the closure of $\sigma_1^3$: $n=3$, $n_+=3$, $n_-=0$. Circle counts in the cube are
$$|D_{000}|=2,\quad |D_{100}|=|D_{010}|=|D_{001}|=1,\quad |D_{110}|=|D_{101}|=|D_{011}|=2,\quad |D_{111}|=3,$$
so $\dim_{\mathbb{F}_2} CKh = 4+3\cdot 2+3\cdot 4+8=30$.

Reduced Khovanov homology over $\mathbb{F}_2$ is
$$\widetilde{Kh}(3_1;\mathbb{F}_2)\cong\mathbb{F}_2_{(i,j)=(0,2)}\oplus\mathbb{F}_2_{(2,6)}\oplus\mathbb{F}_2_{(3,8)},$$
of total rank $3=\det(3_1)$, supported in the single $\delta=j-2i=2$ grading (the trefoil is alternating, hence $\delta$-thin).

Now run §2's grading count. On $E_2$, a length-$k$ term $D_{u,v}$ shifts $\delta$ by $-(4k-2)$. For $k=1$ this is $-2$ — the Khovanov differential, already used. Every higher term has $k\ge 2$ and shifts $\delta$ by at most $-6$. Since $\widetilde{Kh}(3_1;\mathbb{F}_2)$ lives in one $\delta$-grading, every such map is zero on $E_2$. Hence
$$E_2^{\mathrm{Sz}}(3_1)=E_\infty^{\mathrm{Sz}}(3_1)=\mathbb{F}_2^3 .$$
On the Floer side, $\Sigma(T_{2,3})=L(3,1)$, a lens space and therefore an L-space, so $\widehat{HF}(L(3,1);\mathbb{F}_2)=\mathbb{F}_2^3$. Both sequences collapse and the conjecture holds for $3_1$ — but *no* higher differential was tested.

**Where the difficulty starts: $10_{124}=T_{3,5}$.** Here $\det=1$ and $\Sigma(T_{3,5})=\Sigma(2,3,5)$ is the Poincaré homology sphere, with $\widehat{HF}(\Sigma(2,3,5);\mathbb{F}_2)=\mathbb{F}_2$ of rank $1$. But $\widetilde{Kh}(10_{124};\mathbb{F}_2)$ has rank strictly greater than $1$ and is not $\delta$-thin, so higher differentials in *both* sequences must be nonzero and must cancel all but one generator. Verifying that Szabó's combinatorial $D_{u,v}$ with $k\ge2$ perform exactly the cancellation that the holomorphic polygon counts perform — rather than merely reaching the same final rank — is the content of the conjecture, and is exactly what no proof currently supplies.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*