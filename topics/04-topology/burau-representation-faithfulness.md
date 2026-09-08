---
id: 04-topology/burau-representation-faithfulness
title: "Faithfulness of the Burau Representation for Braid Groups"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Faithfulness of the Burau Representation for Braid Groups

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/burau-representation-faithfulness` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $B_n$ be the braid group on $n$ strands and let
$$\beta_n : B_n \longrightarrow \mathrm{GL}_{n-1}\!\left(\mathbb{Z}[t,t^{-1}]\right)$$
be the reduced Burau representation. **Is $\beta_n$ injective?**

The answer is known for every $n$ except one:

| $n$ | Faithful? |
|---|---|
| $n \le 3$ | Yes (Magnus–Peluso 1969) |
| $n = 4$ | **Open** |
| $n \ge 5$ | No (Moody 1991; Long–Paton 1993; Bigelow 1999) |

So the surviving problem is the single case $n=4$: decide whether $\ker \beta_4$ is trivial. A disproof means exhibiting a braid $\beta \in B_4$, $\beta \neq 1$, with $\beta_4(\beta) = I_3$ — equivalently a word in $\sigma_1,\sigma_2,\sigma_3$ not reducible to the identity by the braid relations whose $3\times 3$ Laurent matrix is the identity. A proof means showing $\ker\beta_4 = \{1\}$, presumably by a homological or geometric-intersection argument, since no algebraic normal form for the image is known.

The problem is not idle: Bigelow (2002) proved that a nontrivial element of $\ker\beta_4$ produces a nontrivial knot whose Jones polynomial equals that of the unknot. Faithfulness of $\beta_4$ is therefore entangled with whether the Jones polynomial detects the unknot.

## 2. Mathematical Foundations

**Braid group.** $B_n = \langle \sigma_1,\dots,\sigma_{n-1} \mid \sigma_i\sigma_j=\sigma_j\sigma_i\ (|i-j|\ge 2),\ \sigma_i\sigma_{i+1}\sigma_i=\sigma_{i+1}\sigma_i\sigma_{i+1}\rangle.$ Equivalently $B_n \cong \mathrm{MCG}(D_n)$, the mapping class group of the disk with $n$ marked points, fixing $\partial D$ pointwise.

**Unreduced Burau.** $\hat\beta_n: B_n \to \mathrm{GL}_n(\mathbb{Z}[t,t^{-1}])$ sends
$$\sigma_i \longmapsto I_{i-1} \oplus \begin{pmatrix} 1-t & t \\ 1 & 0\end{pmatrix} \oplus I_{n-i-1}.$$
$\hat\beta_n$ preserves the vector $(1,1,\dots,1)^{\mathsf T}$-dual line and splits (after inverting nothing but over the field of fractions) as $\beta_n \oplus \mathbf{1}$; consequently $\ker\hat\beta_n = \ker\beta_n$, so "the Burau representation" is unambiguous for this question.

**Reduced Burau, explicit form.** For $1 < i < n-1$,
$$\beta_n(\sigma_i) = I_{i-2}\oplus\begin{pmatrix}1&0&0\\ t&-t&1\\ 0&0&1\end{pmatrix}\oplus I_{n-i-2},\qquad
\beta_n(\sigma_1)=\begin{pmatrix}-t&1\\0&1\end{pmatrix}\oplus I_{n-3},\qquad
\beta_n(\sigma_{n-1})=I_{n-3}\oplus\begin{pmatrix}1&0\\ t&-t\end{pmatrix}.$$

**Homological definition.** Let $\tilde D_n \to D_n$ be the infinite cyclic cover classified by total winding number $\pi_1(D_n)\to\mathbb{Z}$. Then $H_1(\tilde D_n,\ \tilde p)$ is a free $\mathbb{Z}[t,t^{-1}]$-module of rank $n-1$ ($t$ = deck transformation), and the $B_n$-action on it is $\beta_n$. Kernel elements are thus mapping classes acting trivially on the homology of this cover.

**Squier form.** Squier (1984) produced a nondegenerate sesquilinear form $\langle\cdot,\cdot\rangle$ over $\mathbb{Z}[s^{\pm1}]$, $t=s^2$, with $\overline{s}=s^{-1}$, preserved by $\beta_n$: the Burau image lies in a unitary group $U_{n-1}(\mathbb{Z}[s^{\pm1}])$.

**Alexander polynomial.** For $\beta\in B_n$ with closure $\hat\beta$,
$$\frac{\Delta_{\hat\beta}(t)}{1} \doteq \frac{\det\!\left(I_{n-1}-\beta_n(\beta)\right)}{1+t+\cdots+t^{n-1}}\,(1-t),$$
up to units $\pm t^k$. Hence $\ker\beta_n$ consists of braids whose closures share Alexander data with the $n$-component unlink.

**Lawrence–Krammer–Bigelow.** The rank-$\binom{n}{2}$ representation $\mathcal{L}_n$ over $\mathbb{Z}[q^{\pm1},t^{\pm1}]$ is faithful for all $n$ (Bigelow 2001, Krammer 2002), so $B_n$ is linear. Burau is a "degenerate limit" of $\mathcal{L}_n$ and is not rescued by this.

## 3. History & State of the Art (SOTA)

- **1935.** Burau introduces the representation while studying the Alexander polynomial of braid closures.
- **1960s–70s.** Faithfulness is folklore-conjectured for all $n$; it would have given linearity of $B_n$ decades before Bigelow–Krammer. Magnus–Peluso (1969) settle $n=3$ using the identification of the reduced image with a subgroup of $\mathrm{SL}_2(\mathbb{Z}[t^{\pm1}])$; the $n\le3$ case also appears in Birman's 1974 monograph.
- **1984.** Squier proves unitarity, constraining the image.
- **1991.** Moody shows $\beta_n$ is **not** faithful for $n\ge 9$, via a Magnus-expansion/"winding-number" argument detecting that certain commutators of conjugates of band generators act trivially on the cyclic cover.
- **1993.** Long and Paton push unfaithfulness to $n \ge 6$, reformulating Moody's obstruction as a homological intersection condition on curves in $D_n$.
- **1999.** Bigelow settles $n=5$ using his "fork and noodle" geometric pairing: the Burau matrix entries are computed as signed intersection counts, and a kernel element is produced by making all pairings vanish. His element is an explicit commutator of two conjugates of band generators.
- **1997.** Cooper and Long give a presentation for the image of $\beta_4 \otimes \mathbb{F}_2$ (Burau mod 2), the deepest structural information available about $B_4$'s Burau image.
- **2001–02.** Bigelow and Krammer prove $B_n$ linear via $\mathcal{L}_n$, removing the main motivation but not the question. Bigelow (2002) links $\ker\beta_4$ to the Jones-unknotting problem.
- **2015 onward.** Ito shows that kernel elements of such braid representations yield knots with trivial classical polynomial invariants, sharpening the consequences of a negative answer at $n=4$.

## 4. Partial Results / Verified Cases

- **$n=1,2$:** trivial. $\beta_2(\sigma_1)=(-t)$ and $B_2\cong\mathbb{Z}$, so $\beta_2$ is injective.
- **$n=3$:** faithful (Magnus–Peluso 1969). The image is a subgroup of $\mathrm{SL}_2^{\pm}(\mathbb{Z}[t^{\pm1}])$; the center $\langle(\sigma_1\sigma_2)^3\rangle$ maps to the scalars $t^3 I$, and $B_3/Z(B_3)\cong \mathrm{PSL}_2(\mathbb{Z})\cong \mathbb{Z}/2 * \mathbb{Z}/3$ injects by a ping-pong argument on the induced $t\mapsto$ specialized action.
- **$n=5$:** unfaithful (Bigelow 1999) — explicit kernel element of word length in the low tens.
- **$n=6,7,8$:** unfaithful (Long–Paton 1993).
- **$n\ge 9$:** unfaithful (Moody 1991).
- **$n=4$, structural partial results:** Cooper–Long (1997) present the image of the mod-2 reduction of $\beta_4$; no kernel element survives mod 2 detection. Beridze and Traczyk (2019) reduce faithfulness of $\beta_4$ to a checkable condition on a normal form for 4-braids and report no kernel elements among the words they enumerate. Computer searches over $B_4$ words of small syllable length have found no kernel element *(frontier — verify the exact search radius)*.
- **Specializations:** for $t$ a root of unity the specialized Burau representations of $B_4$ are typically far from faithful (their images are arithmetic or finite groups), so no specialization argument settles the generic-$t$ case positively.
- **Restricted subgroups:** $\beta_n$ is faithful on the "pure braid–free" subgroups generated by band generators supported on $\le 3$ strands, by the $n=3$ case.

## 5. Principal Obstacles

- **The counting method runs out of room.** Moody/Long–Paton/Bigelow all build a kernel element as a commutator $[\,\alpha_1,\alpha_2\,]$ of conjugated band generators whose supporting curves have zero total homological pairing in the cover. Producing enough independent curves in $D_n$ to force all $\binom{n-1}{2}$-many pairings to vanish requires strands to spare. With $n=4$ the reduced module has rank $3$ and there is simply not enough room in the punctured disk: the fork–noodle pairing cannot be made to vanish nontrivially by the known constructions.
- **No normal form for the image.** Over $\mathbb{Z}[t^{\pm1}]$ the group $\beta_4(B_4)\le \mathrm{GL}_3$ has no known presentation (only Cooper–Long's mod-2 answer). Without a presentation, comparing relations in $B_4$ to relations in the image — the standard route to injectivity — is blocked.
- **Unitarity is too weak.** Squier's form pins the image inside a unitary group, but that group contains the image with infinite index and gives no injectivity criterion.
- **Ping-pong / representation-variety arguments fail.** For $n=3$ the image is essentially $\mathrm{SL}_2$ and one can play ping-pong on the hyperbolic plane. In rank $3$ the relevant symmetric space action is not proper on a suitable domain, and the Burau image is not discrete after specialization at generic $t$.
- **Search is exponentially hard.** $B_4$ grows exponentially; any kernel element is expected to be a long commutator (Bigelow's $n=5$ element already has length in the tens), so brute-force enumeration is out of reach beyond modest lengths, and the geodesic word problem in $B_4$ makes certifying "not the identity braid" for candidate long words nontrivial.
- **Loss of information at $n=4$ is delicate.** The Burau representation is the $q\to$ degenerate specialization of the faithful $\mathcal{L}_4$; understanding *what* is lost in the degeneration is exactly the unsolved point.

## 6. The Gap

Proven: $\beta_3$ injective; $\beta_n$ non-injective for $n\ge5$. Unresolved: the single group $\ker\beta_4 \le B_4$.

The exact barrier is a rank/geometry mismatch. All unfaithfulness proofs need at least two disjoint "noodles" (arcs joining boundary to boundary) and forks with independent supports, whose signed intersection numbers in $\tilde D_n$ must all cancel; the minimal configuration realized so far needs $5$ punctures. Conversely, all faithfulness proofs need either an $\mathrm{SL}_2$-type ping-pong (available only in rank $2$, i.e. $n=3$) or a presentation of the image. Crossing the gap means either:

1. constructing a curve configuration in $D_4$ with vanishing fork–noodle pairing that is not homotopically trivial, or
2. proving that vanishing pairing in $D_4$ forces triviality — i.e. that the Burau intersection pairing is a complete invariant of mapping classes on $4$ punctures.

## 7. Current Research (as of June 2026)

- **Homological / categorified approaches.** Groups working on homological braid representations (Bigelow-style fork–noodle calculus, Ito's work relating kernels to knot polynomials in Japan, and the quantum-topology community around $\mathcal{L}_n$ and its specializations) study how faithfulness degenerates as the Lawrence–Krammer parameter $q\to 1$. The hope is an exact criterion for what $\mathcal{L}_4$ sees and $\beta_4$ does not *(frontier — verify)*.
- **Jones-unknotting connection.** Because Bigelow's implication makes $\ker\beta_4\neq1$ a source of a nontrivial knot with trivial Jones polynomial, and because extensive computation (millions of knots) has found none, the community's working expectation has shifted toward **$\beta_4$ being faithful** *(frontier — verify; this is a heuristic, not a theorem)*.
- **Computational certification.** Enumeration in $B_4$ using Garside normal form plus matrix filtering over $\mathbb{F}_p[t]/(f)$ to reject non-kernel candidates cheaply; reported searches now cover all Garside-normal-form words up to modest canonical length with no kernel element *(frontier — verify exact bound)*.
- **Structure of the image.** Follow-ups to Cooper–Long attempt presentations of $\beta_4(B_4)$ over $\mathbb{Z}[t^{\pm1}]$ or over $\mathbb{Z}/4$, $\mathbb{Z}/3$ reductions.
- **Related specializations.** Faithfulness and image-arithmeticity for the Burau representation at roots of unity (Squier form signature, Deligne–Mostow lattices) remains an active adjacent industry, feeding techniques back to the generic-$t$ question.

## 8. Future Work

- Determine whether the fork–noodle pairing is a **complete** invariant for $\mathrm{MCG}(D_4)$; a positive answer proves faithfulness at $n=4$.
- Obtain a presentation of $\beta_4(B_4)$ over $\mathbb{Z}[t^{\pm1}]$, extending Cooper–Long from $\mathbb{F}_2$ — then compare deficiency with the standard $B_4$ presentation.
- Sharpen the reverse direction of Bigelow's theorem: does a nontrivial knot with trivial Jones polynomial and $4$-braid index force $\ker\beta_4\neq 1$? A clean equivalence would let large-scale Jones computations bear directly on the algebra.
- Study $\ker\beta_n$ as a normal subgroup: is it free? finitely generated? Long's work on normal subgroups of mapping class groups suggests $\ker\beta_5$ is large; identifying it may reveal the minimal strand count structurally.
- Exploit the surjection $B_4 \to B_3$ (mapping $\sigma_1,\sigma_3\mapsto\sigma_1$, $\sigma_2\mapsto\sigma_2$) with kernel a free group of rank $2$: any $\ker\beta_4$ element must lie in the preimage of $\ker\beta_3=1$, i.e. in that free normal subgroup — narrowing the search to $F_2$-conjugacy data.

## 9. Key References

- **[Foundational]** W. Burau. *Über Zopfgruppen und gleichsinnig verdrillte Verkettungen.* Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg, 11:179–186, 1935.
- **[Foundational]** W. Magnus and A. Peluso. *On a theorem of V. I. Arnol'd.* Communications on Pure and Applied Mathematics, 22:683–692, 1969.
- **[Foundational]** J. S. Birman. *Braids, Links, and Mapping Class Groups.* Annals of Mathematics Studies 82, Princeton University Press, 1974.
- **[Structure]** C. C. Squier. *The Burau representation is unitary.* Proceedings of the American Mathematical Society, 90(2):199–202, 1984.
- **[SOTA]** J. A. Moody. *The Burau representation of the braid group $B_n$ is unfaithful for large $n$.* Bulletin of the American Mathematical Society, 25(2):379–384, 1991.
- **[SOTA]** D. D. Long and M. Paton. *The Burau representation is not faithful for $n\ge 6$.* Topology, 32(2):439–447, 1993.
- **[SOTA]** S. Bigelow. *The Burau representation is not faithful for $n=5$.* Geometry & Topology, 3:397–404, 1999.
- **[Structure]** D. Cooper and D. D. Long. *A presentation for the image of Burau(4)$\otimes\mathbb{Z}_2$.* Inventiones Mathematicae, 127(3):535–570, 1997.
- **[Linearity]** S. Bigelow. *Braid groups are linear.* Journal of the American Mathematical Society, 14(2):471–486, 2001.
- **[Linearity]** D. Krammer. *Braid groups are linear.* Annals of Mathematics, 155(1):131–156, 2002.
- **[Consequence]** S. Bigelow. *Does the Jones polynomial detect unknottedness?* Experimental Mathematics, 11(4):493–505, 2002.
- **[Recent]** T. Ito. *A kernel of a braid group representation yields a knot with trivial knot polynomials.* Mathematische Zeitschrift, 280:347–353, 2015.
- **[Recent]** A. Beridze and P. Traczyk. *Burau representation for $n=4$.* Journal of Knot Theory and Its Ramifications, 2019.
- **[Survey]** J. S. Birman and T. E. Brendle. *Braids: a survey.* In: Handbook of Knot Theory (W. Menasco, M. Thistlethwaite, eds.), Elsevier, 2005, pp. 19–103.

## 10. Worked Example / Concrete Special Case

**The faithful case $n=3$, computed.** Set
$$A=\beta_3(\sigma_1)=\begin{pmatrix}-t&1\\0&1\end{pmatrix},\qquad B=\beta_3(\sigma_2)=\begin{pmatrix}1&0\\ t&-t\end{pmatrix}.$$

*Braid relation check.*
$$AB=\begin{pmatrix}-t+t&-t\\ t&-t\end{pmatrix}=\begin{pmatrix}0&-t\\ t&-t\end{pmatrix},\qquad
ABA=\begin{pmatrix}0&-t\\ -t^2&0\end{pmatrix}.$$
$$BA=\begin{pmatrix}-t&1\\ -t^{2}&0\end{pmatrix},\qquad
BAB=\begin{pmatrix}0&-t\\ -t^{2}&0\end{pmatrix}.$$
So $ABA=BAB$: the assignment is a representation.

*The center.* $(\sigma_1\sigma_2)^3=(\sigma_1\sigma_2\sigma_1)^2$ generates $Z(B_3)$, and
$$(ABA)^2=\begin{pmatrix}0&-t\\ -t^{2}&0\end{pmatrix}^2=\begin{pmatrix}t^{3}&0\\0&t^{3}\end{pmatrix}=t^3 I.$$
Since $t^3\neq 1$ in $\mathbb{Z}[t^{\pm1}]$, the center injects. Modding out, $\beta_3$ descends to $B_3/Z \cong \mathrm{PSL}_2(\mathbb{Z}) \cong \mathbb{Z}/2 * \mathbb{Z}/3$ generated by the images of $ABA$ (order $2$ mod scalars) and $AB$ (order $3$ mod scalars: $(AB)^3 = -t^3 I$, check: $(AB)^2=\begin{pmatrix}-t^2&t^2\\-t^2&0\end{pmatrix}$, and $(AB)^3 = \begin{pmatrix}t^3&0\\0&t^3\end{pmatrix}\cdot(-1)$). Injectivity of the free product on these two elements follows by ping-pong, giving $\ker\beta_3=1$.

*Determinant obstruction.* $\det A=\det B=-t$, so $\det\beta_n(\beta)=(-t)^{e(\beta)}$ where $e$ is the exponent sum. Any kernel element must have $e=0$ — for $n=4$ this already forces candidates into the commutator-closure region.

*Why $n=4$ resists.* The natural surjection $\pi:B_4\to B_3$, $\sigma_1,\sigma_3\mapsto\sigma_1$, $\sigma_2\mapsto\sigma_2$, has kernel the free group $F_2=\langle \sigma_3\sigma_1^{-1},\ \sigma_2\sigma_3\sigma_1^{-1}\sigma_2^{-1}\rangle$. Because $\beta_3$ is faithful and $\beta_4$ covers it in a suitable sense, any $\gamma\in\ker\beta_4$ must satisfy $\pi(\gamma)=1$, i.e. $\gamma\in F_2$. Testing $\gamma = (\sigma_3\sigma_1^{-1})$ gives
$$\beta_4(\sigma_3\sigma_1^{-1})=\begin{pmatrix}1&0&0\\0&1&0\\0&t&-t\end{pmatrix}\begin{pmatrix}-t^{-1}&t^{-1}&0\\0&1&0\\0&0&1\end{pmatrix}\neq I_3,$$
and every short word in these free generators similarly fails. The open problem is whether *some* word in this rank-2 free group — necessarily long, with zero exponent sum, and invisible to the mod-2 image computed by Cooper–Long — maps to $I_3$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*