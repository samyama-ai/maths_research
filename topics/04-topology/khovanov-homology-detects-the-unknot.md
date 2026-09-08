---
id: 04-topology/khovanov-homology-detects-the-unknot
title: "Khovanov Homology Detects the Unknot"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Khovanov Homology Detects the Unknot

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/khovanov-homology-detects-the-unknot` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $K \subset S^3$ be a knot and let $\mathrm{Kh}(K)$ denote its Khovanov homology, a bigraded abelian group categorifying the Jones polynomial. The unknot $U$ has $\mathrm{Kh}(U) \cong \mathbb{Z}^2$ (reduced: $\widetilde{\mathrm{Kh}}(U) \cong \mathbb{Z}$). The detection question asks the converse:

> **Question (Khovanov, ca. 2000).** If $\operatorname{rk} \widetilde{\mathrm{Kh}}(K) = 1$, is $K$ the unknot?

**This is a theorem.** Kronheimer and Mrowka proved it in *Khovanov homology is an unknot-detector* (Publ. Math. IHÉS 113, 2011): reduced Khovanov homology has rank $1$ if and only if $K$ is unknotted; equivalently $\operatorname{rk}\mathrm{Kh}(K) = 2 \iff K = U$.

The page is retained as `solved-recently` because the surrounding programme is wide open. The live questions are:

1. **(Combinatorial proof)** Is there a proof not routed through gauge theory? Every known argument passes through instanton or Heegaard Floer homology; Khovanov homology is a finitely generated combinatorial object, yet no combinatorial certificate of unknottedness is extractable from the proof.
2. **(Jones polynomial)** Does the Jones polynomial $V_K(q)$ detect the unknot? Open since 1984; decategorification loses the detection.
3. **(General detection)** Which knots and links does $\mathrm{Kh}$ detect? Known: $U$, unlinks, $3_1^{\pm}$, $4_1$, $5_1 = T(2,5)$ and its mirror. Unknown already for $T(2,7)$ and for the general question "does $\mathrm{Kh}$ detect all torus knots?"

A resolution of (1) means: a proof of the rank-$1$ statement using only the Khovanov chain complex, Reidemeister-move machinery, and combinatorial spectral sequences. A resolution of (2) means an unknotted-detection proof for $V$, or an explicit nontrivial knot with $V_K = 1$.

## 2. Mathematical Foundations

**Khovanov chain complex.** Let $D$ be a diagram of $K$ with $n$ crossings, $n_+$ positive and $n_-$ negative. Each crossing has a $0$- and a $1$-smoothing; for $v \in \{0,1\}^n$ let $D_v$ be the resulting collection of $|D_v|$ disjoint circles. Set $A = \mathbb{Z}[X]/(X^2)$, a Frobenius algebra with
$$\Delta(1) = 1\otimes X + X \otimes 1,\qquad \Delta(X) = X\otimes X,\qquad m(X\otimes X)=0,\qquad \varepsilon(X)=1,\ \varepsilon(1)=0,$$
and gradings $\deg 1 = 1$, $\deg X = -1$. Define
$$C^{i,j}(D) = \bigoplus_{|v| = i + n_-} \big( A^{\otimes |D_v|}\{|v| + n_+ - 2n_-\}\big)^j ,$$
with differential $d$ summing edge maps of the cube $\{0,1\}^n$, each edge map being $m$ (merge) or $\Delta$ (split) tensored with identities, with signs making the cube anticommute. Then $\mathrm{Kh}^{i,j}(K) = H^{i,j}(C(D),d)$ is a knot invariant (Khovanov 2000; Bar-Natan 2002), with
$$\sum_{i,j} (-1)^i q^j \operatorname{rk}\mathrm{Kh}^{i,j}(K) \;=\; (q+q^{-1})\,V_K(q^2).$$

**Reduced theory.** Marking a basepoint on $D$ makes $C(D)$ a module over $A$; $\widetilde{C}(D) = X\cdot C(D)$ gives $\widetilde{\mathrm{Kh}}(K)$, with $\mathrm{Kh}(K;\mathbb{F}_2) \cong \widetilde{\mathrm{Kh}}(K;\mathbb{F}_2)\otimes(\mathbb{F}_2\oplus\mathbb{F}_2)$.

**Instanton input.** For a knot $K$, Kronheimer–Mrowka define the singular instanton homology $I^{\natural}(K)$: Floer homology of the $SO(3)$-Chern–Simons functional on the complement of $K \cup H$ ($H$ a small Hopf-linked arc) with an orbifold/singular bundle. Their main theorem is a spectral sequence
$$E_2 \cong \widetilde{\mathrm{Kh}}(\overline{K}) \;\Longrightarrow\; I^{\natural}(K),$$
$\overline{K}$ the mirror, hence the rank inequality $\operatorname{rk}\widetilde{\mathrm{Kh}}(K) \ge \operatorname{rk} I^{\natural}(K)$.

**Nonvanishing.** From *Knots, sutures, and excision* (J. Topol. 3, 2010): sutured instanton homology $SHI$ of a taut sutured manifold is nonzero, via Gabai's sutured hierarchy, the Eliashberg–Thurston perturbation of taut foliations to contact structures, and nonvanishing for weakly symplectically fillable contact manifolds. This forces $\operatorname{rk} I^{\natural}(K) \ge 2$ for any $K$ of genus $g(K)\ge 1$, i.e. any nontrivial knot. Combining:
$$\operatorname{rk}\widetilde{\mathrm{Kh}}(K) = 1 \implies \operatorname{rk} I^\natural(K)=1 \implies g(K)=0 \implies K = U .$$

## 3. History & State of the Art (SOTA)

- **1984–2000.** Jones discovers $V_K$; whether $V_K = 1$ forces $K=U$ becomes a famous open problem, restated by Bigelow (*Does the Jones polynomial detect unknottedness?*, JKTR 11, 2002), who showed it is decidable-with-oracle in a precise sense.
- **2000.** Khovanov categorifies $V$. Because $\mathrm{Kh}$ is strictly stronger than $V$ (it distinguishes $10_{136}$ from its mirror-family partners, and pairs of knots with equal Jones polynomials), detection becomes plausible.
- **2001–2003.** Thistlethwaite, then Eliahou–Kauffman–Thistlethwaite (*Infinite families of links with trivial Jones polynomial*, Topology 42, 2003), produce nontrivial **links** with the Jones polynomial of an unlink — ruling out the naive link analogue for $V$ and sharpening the knot case.
- **2005–2010.** Lee's deformation and Rasmussen's $s$-invariant show the Khovanov complex carries genus/slice information; Ozsváth–Szabó show knot Floer homology detects genus (Geom. Topol. 8, 2004), setting the template "Floer-type theory detects genus, spectral sequence transports the bound".
- **2010–2011.** Kronheimer–Mrowka's unknot-detector theorem. Widely regarded as the first proof that a combinatorially defined knot homology detects the unknot.
- **2013–2015.** Link versions: Hedden–Ni (Khovanov *module* detects unlinks, Geom. Topol. 17, 2013) and Batson–Seed (link-splitting spectral sequence, Duke Math. J. 164, 2015).
- **2018–2025.** Dowlin's spectral sequence from $\mathrm{Kh}$ to $\widehat{\mathrm{HFK}}$ (arXiv:1811.07848) gives a second, Heegaard-Floer route. Baldwin–Sivek and collaborators extend detection to $3_1$, $4_1$, $T(2,5)$.

## 4. Partial Results / Verified Cases

| Statement | Status | Source |
|---|---|---|
| $\operatorname{rk}\widetilde{\mathrm{Kh}}(K)=1 \Rightarrow K=U$ | Proved (all knots) | Kronheimer–Mrowka 2011 |
| Second proof via $\mathrm{Kh}\Rightarrow \widehat{\mathrm{HFK}}$ | Proved | Dowlin (arXiv:1811.07848) |
| $\mathrm{Kh}$ (as a module over $A^{\otimes n}$) detects the $n$-component unlink | Proved | Hedden–Ni 2013; Batson–Seed 2015 |
| $\mathrm{Kh}$ detects split links | Proved | Lipshitz–Sarkar; Batson–Seed 2015 |
| $\mathrm{Kh}$ detects $3_1$ (both chiralities) | Proved | Baldwin–Sivek, Duke Math. J. 171 (2022) |
| $\mathrm{Kh}$ detects $4_1$ | Proved | Baldwin–Dowlin–Levine–Lidman–Sazdanović, Bull. LMS 53 (2021) |
| $\mathrm{Kh}$ detects $T(2,5)$ (the cinquefoil) | Proved | Baldwin–Hu–Sivek (arXiv:2105.12102) |
| $\mathrm{Kh}$ detects the Hopf link, $T(2,4)$, $L7n1$ | Proved | Baldwin–Sivek and follow-ups |
| Reduced $\mathrm{Kh}$ over $\mathbb{F}_2$ of all knots up to 16–17 crossings has rank $\ge 3$ for nontrivial $K$ | Verified computationally | KnotAtlas / `khoca` / Bar-Natan's divide-and-conquer scanning algorithm (JKTR 16, 2007) |
| $V_K = 1 \Rightarrow K = U$ for alternating, adequate, and $\le 24$-crossing knots | Proved / verified | Kauffman–Murasugi–Thistlethwaite; Tuzun–Sikora computations |

Genus detection: $\mathrm{Kh}$ over $\mathbb{Z}$ does **not** detect genus in general, but the Lee/Rasmussen $s$-invariant gives $|s(K)| \le 2g_4(K)$, sharp for positive knots.

## 5. Principal Obstacles

- **The proof is not intrinsic.** The only known routes use $I^{\natural}$ or $\widehat{\mathrm{HFK}}$. Both detect genus through geometric input — taut foliations (Gabai), symplectic filling (Eliashberg–Thurston), holomorphic curve counts — none of which has a combinatorial shadow inside the cube of resolutions. There is no known combinatorial quantity in $C(D)$ that lower-bounds $g(K)$.
- **Spectral sequences are one-directional and non-explicit.** $\widetilde{\mathrm{Kh}}(\overline K) \Rightarrow I^{\natural}(K)$ gives only $\operatorname{rk}\widetilde{\mathrm{Kh}}\ge\operatorname{rk} I^{\natural}$; the higher differentials $d_r$, $r\ge 2$, are not computable from a diagram. So knowing $\mathrm{Kh}$ tells you a bound but not the target group, blocking detection statements for larger knots.
- **Decategorification kills the argument.** $V_K$ is the graded Euler characteristic; cancellation between $E_\infty$ classes of adjacent homological degree is exactly what a Euler characteristic cannot see. The Eliahou–Kauffman–Thistlethwaite links show that in the link setting this cancellation genuinely occurs. No mechanism forbids it for knots.
- **Functoriality and torsion.** Detection arguments need naturality of the spectral sequence under cobordism; Khovanov's functoriality holds only up to sign (Jacobsson, Bar-Natan) unless one passes to Blanchet's or the disoriented refinements. Torsion classes ($\mathbb{Z}/2$ is ubiquitous) obstruct rank counts over $\mathbb{Z}$ versus $\mathbb{F}_2$.
- **Complexity.** Computing $\mathrm{Kh}$ is exponential in crossing number in the worst case and evaluating $V$ at generic roots of unity is $\\#P$-hard (Jaeger–Vertigan–Welsh 1990), so brute-force verification cannot scale to a search for a counterexample to (2).

## 6. The Gap

Proven: rank-$1$ reduced Khovanov homology implies unknottedness, by a chain
$$\widetilde{\mathrm{Kh}}(K) \xrightarrow{\ \text{s.s.}\ } I^\natural(K) \xrightarrow{\ SHI \neq 0\ } g(K) = 0 .$$

The gap is that each arrow is analytic. The precise missing step for (1) is a **combinatorial genus bound**: a function $\gamma$ of the Khovanov complex with $\gamma(K)\ge 1$ for all $K$ with $g(K)\ge 1$, proved without Floer theory. For (2), the gap is that no map $\mathrm{Kh}\to V$ statement survives: one needs either a "no-cancellation" theorem showing $\operatorname{rk}\mathrm{Kh}(K) = 2 \iff V_K = 1$ for knots, or a construction — e.g. via untwisted Whitehead doubles or Brunnian satellites in the style of the trivial-Jones links — of a knot with $V_K = 1$.

## 7. Current Research (as of June 2026)

- **Boston College / Princeton (Baldwin, Sivek, Hu, Li).** The detection programme: extending $\mathrm{Kh}$ and instanton-Floer detection from $T(2,5)$ to $T(2,7)$ and to $5_2$, $6_1$. Techniques: instanton $L$-space knots, rank bounds for $KHI$, and $SU(2)$-representation obstructions. *(frontier — verify)*
- **Columbia / UCLA (Khovanov, Lipshitz, Sarkar).** Khovanov stable homotopy type and its Steenrod operations; refinements strictly stronger than $\mathrm{Kh}$ as rank invariants, with the hope that stable-homotopy-level detection is combinatorially provable.
- **Skein lasagna modules (Morrison–Walker–Wedrich, Manolescu–Neithalath, Sullivan).** $\mathcal{S}_0(X;K)$ for 4-manifolds; computations show nonvanishing detects exotica-relevant data, and give a 4-dimensional reformulation of detection. *(frontier — verify)*
- **Combinatorial Floer replacements.** Efforts to give a bordered/combinatorial model for the $\mathrm{Kh}\to\widehat{\mathrm{HFK}}$ spectral sequence (Dowlin's cube of resolutions for $\mathrm{HFK}$ is already algebraic — making the whole chain algebraic is the most concrete path to a combinatorial proof).
- **Computational.** Large-scale reduced Khovanov computations (Schütz's `khoca`, Regina/SnapPy pipelines) verifying rank $\ge 3$ for nontrivial knots into the high-crossing range, and Tuzun–Sikora-style searches for trivial Jones polynomial knots.

## 8. Future Work

- Extract from Kronheimer–Mrowka's $\mathbb{Z}/4$-graded instanton theory a **filtration on the Khovanov complex** whose induced numerical invariant bounds Seifert genus, giving a self-contained proof of detection.
- Prove or disprove that $\mathrm{Kh}$ detects all torus knots $T(2,n)$; then all $T(p,q)$. Baldwin–Sivek have suggested the obstruction is controlled by instanton $L$-space knot rigidity.
- Settle whether $\mathrm{Kh}$ detects the unknot with $\mathbb{F}_2$ coefficients *and* whether $\operatorname{rk}_{\mathbb{Q}}$ suffices, sharpening the torsion dependence.
- Attack the Jones question via satellite/Brunnian surgery constructions modelled on Eliahou–Kauffman–Thistlethwaite, or prove a rank-versus-Euler-characteristic bound ("thinness forces $V \neq 1$") for a broad knot class.
- Complexity-theoretic angle: Kuperberg (Adv. Math. 256, 2014) and Lackenby (Adv. Math. 387, 2021) show knottedness is in $\mathrm{NP}\cap\mathrm{coNP}$-like classes; a combinatorial Khovanov certificate would give a new, quantum-topological unknottedness certificate.

## 9. Key References

- **[Foundational]** M. Khovanov. *A categorification of the Jones polynomial.* Duke Math. J. 101 (2000), 359–426. [DOI](https://doi.org/10.1215/s0012-7094-00-10131-7)
- **[Foundational]** D. Bar-Natan. *On Khovanov's categorification of the Jones polynomial.* Algebr. Geom. Topol. 2 (2002), 337–370.
- **[SOTA]** P. B. Kronheimer, T. S. Mrowka. *Khovanov homology is an unknot-detector.* Publ. Math. Inst. Hautes Études Sci. 113 (2011), 97–208. [DOI](https://doi.org/10.1007/s10240-010-0030-y)
- **[SOTA]** P. B. Kronheimer, T. S. Mrowka. *Knots, sutures, and excision.* J. Topology 3 (2010), 835–921. [DOI](https://doi.org/10.4310/jdg/1274707316)
- **[SOTA]** J. A. Baldwin, S. Sivek. *Khovanov homology detects the trefoils.* Duke Math. J. 171 (2022), 885–956. [DOI](https://doi.org/10.1215/00127094-2021-0034)
- **[SOTA]** J. A. Baldwin, N. Dowlin, A. S. Levine, T. Lidman, R. Sazdanović. *Khovanov homology detects the figure-eight knot.* Bull. London Math. Soc. 53 (2021), 871–876. [DOI](https://doi.org/10.1112/blms.12467)
- **[SOTA]** J. A. Baldwin, Y. Hu, S. Sivek. *Khovanov homology and the cinquefoil.* arXiv:2105.12102 (2021); J. Eur. Math. Soc.
- **[Recent]** N. Dowlin. *A spectral sequence from Khovanov homology to knot Floer homology.* arXiv:1811.07848 (2018).
- **[Recent]** M. Hedden, Y. Ni. *Khovanov module and the detection of unlinks.* Geom. Topol. 17 (2013), 3027–3076. [DOI](https://doi.org/10.2140/gt.2013.17.3027)
- **[Recent]** J. Batson, C. Seed. *A link-splitting spectral sequence in Khovanov homology.* Duke Math. J. 164 (2015), 801–841. [DOI](https://doi.org/10.1215/00127094-2881374)
- **[Related]** E. S. Lee. *An endomorphism of the Khovanov invariant.* Adv. Math. 197 (2005), 554–586. [DOI](https://doi.org/10.1016/j.aim.2004.10.015)
- **[Related]** J. Rasmussen. *Khovanov homology and the slice genus.* Invent. Math. 182 (2010), 419–447. [DOI](https://doi.org/10.1007/s00222-010-0275-6)
- **[Related]** P. Ozsváth, Z. Szabó. *Holomorphic disks and genus bounds.* Geom. Topol. 8 (2004), 311–334. [DOI](https://doi.org/10.2140/gt.2004.8.311)
- **[Related]** S. Eliahou, L. Kauffman, M. Thistlethwaite. *Infinite families of links with trivial Jones polynomial.* Topology 42 (2003), 155–169. [DOI](https://doi.org/10.1016/s0040-9383(02)00012-5)
- **[Related]** S. Bigelow. *Does the Jones polynomial detect unknottedness?* J. Knot Theory Ramifications 11 (2002), 493–505.
- **[Survey]** P. Turner. *Five lectures on Khovanov homology.* J. Knot Theory Ramifications 26 (2017), 1741009. [DOI](https://doi.org/10.1142/s0218216517410097)

## 10. Worked Example / Concrete Special Case

**Unknot.** One-circle diagram, no crossings: $C(D) = A$, $d = 0$, so
$$\mathrm{Kh}^{0,\pm1}(U) = \mathbb{Z},\qquad \operatorname{rk}\mathrm{Kh}(U)=2,\qquad \operatorname{rk}\widetilde{\mathrm{Kh}}(U)=1 .$$
Graded Euler characteristic $q + q^{-1} = (q+q^{-1})\cdot 1$, matching $V_U = 1$.

**Right-handed trefoil $3_1$.** Standard diagram: $n = 3$, $n_+ = 3$, $n_- = 0$. The cube $\{0,1\}^3$ gives circle counts $|D_v| = 2,3,3,3,2,2,2,1$ for $|v|=0,1,1,1,2,2,2,3$, so the ungraded chain ranks in homological degrees $0,1,2,3$ are
$$4,\; 24,\; 12,\; 2 .$$
Taking homology (Bar-Natan's computation) yields
$$\mathrm{Kh}^{0,1}=\mathrm{Kh}^{0,3}=\mathrm{Kh}^{2,5}=\mathrm{Kh}^{3,9}=\mathbb{Z},\qquad \mathrm{Kh}^{3,7}=\mathbb{Z}/2 .$$
Free rank $4 > 2$. Reduced:
$$\widetilde{\mathrm{Kh}}^{0,2}=\widetilde{\mathrm{Kh}}^{2,6}=\widetilde{\mathrm{Kh}}^{3,8}=\mathbb{Z},\qquad \operatorname{rk}\widetilde{\mathrm{Kh}}(3_1)=3 \neq 1 .$$
Check: $\chi_q = q + q^3 + q^5 - q^9 = (q+q^{-1})(q^2+q^6-q^8) = (q+q^{-1})V_{3_1}(q^2)$ with $V_{3_1}(t) = -t^{-4}+t^{-3}+t^{-1}$ for the left-handed convention — mirroring flips $(i,j)\mapsto(-i,-j)$.

**Where the theorem bites.** Kronheimer–Mrowka give $\operatorname{rk} I^{\natural}(3_1) = 3$, and the spectral sequence $E_2 = \widetilde{\mathrm{Kh}}(\overline{3_1}) \Rightarrow I^{\natural}(3_1)$ has rank $3$ on both ends, so it degenerates at $E_2$. For a hypothetical nontrivial $K$ with $\operatorname{rk}\widetilde{\mathrm{Kh}}(K)=1$ the sequence would force $\operatorname{rk} I^{\natural}(K) = 1$, contradicting $SHI(S^3\setminus N(K), \text{annular suture}) \neq 0$ for $g(K)\ge 1$. Note the trefoil case also illustrates the harder Baldwin–Sivek theorem: rank $3$ *alone* does not immediately name the knot — one must additionally rule out all other rank-$3$ candidates using the bigrading and $s$-invariant, which is precisely why detection of individual knots lags detection of the unknot by a decade.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*