---
id: 10-theoretical-cs/mutually-unbiased-bases
title: "Mutually Unbiased Bases"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mutually Unbiased Bases

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/mutually-unbiased-bases` · **Status:** open

## 1. Problem Statement / Conjecture

Let $N(d)$ denote the maximum number of pairwise mutually unbiased orthonormal bases of the Hilbert space $\mathbb{C}^d$. Two orthonormal bases $\mathcal{B} = \{|e_1\rangle,\dots,|e_d\rangle\}$ and $\mathcal{C} = \{|f_1\rangle,\dots,|f_d\rangle\}$ are **mutually unbiased** if

$$|\langle e_i | f_j \rangle|^2 = \frac{1}{d} \qquad \text{for all } i,j \in \{1,\dots,d\}.$$

It is elementary that $N(d) \le d+1$, and $N(d) = d+1$ whenever $d$ is a prime power. The problem:

> **Determine $N(d)$ for every $d$ that is not a prime power.** In particular (the smallest open case), decide whether $N(6) = 3$, as conjectured, or whether $4 \le N(6) \le 7$.

A complete resolution requires either an explicit construction of more than the currently known bases in some composite dimension, or a proof of a matching upper bound. Even the qualitative question — *is $N(d) < d+1$ for every non-prime-power $d$?* — is open; no composite non-prime-power dimension is known where $N(d)$ has been determined exactly.

## 2. Mathematical Foundations

**Setting.** Work in $\mathbb{C}^d$ with the standard inner product. A set $\{\mathcal{B}_0,\dots,\mathcal{B}_{N-1}\}$ of orthonormal bases is a *MUB set* if every pair is unbiased. Write the rank-one projectors of basis $\mathcal{B}_a$ as $P^a_j = |e^a_j\rangle\langle e^a_j|$.

**Upper bound $N(d)\le d+1$.** The space $\mathcal{H}_d$ of Hermitian operators on $\mathbb{C}^d$ has real dimension $d^2$ under the Hilbert–Schmidt inner product $\langle A,B\rangle = \operatorname{Tr}(A^\dagger B)$. The traceless part $\mathcal{H}_d^0$ has dimension $d^2-1$. For each basis, the $d$ operators $P^a_j - \tfrac{1}{d}I$ are traceless, sum to zero, and span a $(d-1)$-dimensional subspace $V_a \subset \mathcal{H}_d^0$. Unbiasedness gives, for $a\ne b$,

$$\operatorname{Tr}\!\left[\Big(P^a_i-\tfrac{I}{d}\Big)\Big(P^b_j-\tfrac{I}{d}\Big)\right] = |\langle e^a_i|e^b_j\rangle|^2 - \tfrac{1}{d} = 0,$$

so the $V_a$ are mutually orthogonal. Hence $N(d-1)\le d^2-1$, i.e. $N \le d+1$. A set attaining $d+1$ is called **complete**; it yields an orthogonal decomposition $\mathcal{H}_d^0 = \bigoplus_{a=0}^{d} V_a$, equivalently an orthogonal decomposition of the Lie algebra $\mathfrak{sl}(d,\mathbb{C})$ into Cartan subalgebras (Boykin–Sitharam–Tiep–Wocjan).

**Hadamard normalisation.** Fixing $\mathcal{B}_0$ to be the computational basis, every other basis is the column set of $H/\sqrt{d}$ where $H$ is a **complex Hadamard matrix**: $|H_{ij}|=1$ and $HH^\dagger = dI$. Two such bases $H_1,H_2$ are mutually unbiased iff $\tfrac{1}{\sqrt d}H_1^\dagger H_2$ is again complex Hadamard. So the MUB problem in dimension $d$ is a question about the (still uncharted, for $d=6$) variety of complex Hadamard matrices.

**Weyl–Heisenberg construction.** For prime $p$, with $\omega = e^{2\pi i/p}$, set

$$|\psi^a_j\rangle = \frac{1}{\sqrt p}\sum_{k=0}^{p-1}\omega^{ak^2+jk}\,|k\rangle,\qquad a,j \in \mathbb{Z}_p .$$

Each $\mathcal{B}_a = \{|\psi^a_j\rangle\}_j$ is orthonormal, and for $a \ne b$ the overlap is a quadratic Gauss sum $\frac1p\sum_k \omega^{(a-b)k^2+(j-j')k}$ of modulus $p^{-1/2}$. Together with the computational basis this gives $p+1$ MUBs. For $d=p^k$ the same works over $\mathrm{GF}(p^k)$ with $\omega^{\,\cdot}$ replaced by additive characters and $ak^2+jk$ by $\mathrm{Tr}(ak^2+jk)$ (odd $p$), or over Galois rings $\mathrm{GR}(4,k)$ for $p=2$.

**Multiplicativity.** $N(d_1 d_2) \ge \min\{N(d_1),N(d_2)\}$, by tensoring MUB sets. With the prime-power result this gives the standard lower bound

$$N(d) \ \ge\ p_1^{k_1}+1, \qquad d = \prod_i p_i^{k_i},\ \ p_1^{k_1} = \min_i p_i^{k_i}.$$

## 3. History & State of the Art (SOTA)

- **1960.** Schwinger studies pairs of "maximally incompatible" bases via unitary operator bases.
- **1981.** Ivanović constructs $p+1$ MUBs in prime dimension, motivated by optimal quantum state determination.
- **1989.** Wootters and Fields prove $N(p^k)=p^k+1$ for all prime powers and show complete MUB sets minimise the statistical error of state tomography.
- **1997.** Calderbank, Cameron, Kantor and Seidel connect complete MUB sets in $d=2^n$ to $\mathbb{Z}_4$-Kerdock codes and orthogonal spreads, producing exponentially many inequivalent complete sets.
- **2002–2004.** Bandyopadhyay, Boykin, Roychowdhury, Vatan give a unified construction from maximal commuting classes of generalised Pauli operators; Klappenecker and Rötteler give the Galois-ring construction for even prime powers.
- **2005.** Wocjan and Beth beat the $p_1^{k_1}+1$ bound in square dimensions using mutually orthogonal Latin squares (MOLS).
- **2007–2011.** Intensive numerical and algebraic assault on $d=6$: Bengtsson et al., Butterley–Hall, Brierley–Weigert, Jaming–Matolcsi–Móra–Szöllősi–Weiner, Raynal–Lü–Englert. All searches for a fourth basis fail.
- **2013.** Weiner proves a structural gap: an unextendible MUB set in $\mathbb{C}^d$ can never have exactly $d$ elements — so $N(d)=d$ is impossible, and any $d$ MUBs extend to $d+1$.
- **2016–present.** Computer-algebra and real-algebraic-geometry approaches (Gröbner bases, sums-of-squares, interval arithmetic) to certify $N(6)\le 3$; none has closed the case.

**SOTA summary:** $N(d)$ is known exactly only for prime powers. For $d=6$: $3 \le N(6) \le 7$, with $N(6)=7$ excluded in several restricted settings and overwhelming numerical evidence for $N(6)=3$.

## 4. Partial Results / Verified Cases

- **Prime powers.** $N(p^k)=p^k+1$ for every prime $p$ and $k\ge1$ (Ivanović 1981; Wootters–Fields 1989). Explicit constructions from Galois fields, Galois rings, symplectic spreads, and Alltop sequences.
- **General lower bound.** $N(d)\ge p_1^{k_1}+1$. E.g. $N(6)\ge3$, $N(10)\ge3$, $N(15)\ge4$, $N(12)\ge5$.
- **Square dimensions.** Wocjan–Beth: $N(s^2) \ge M(s)+2$ where $M(s)$ is the number of MOLS of order $s$. For $d=26^2=676$ this gives $\ge 6$ MUBs versus $5$ from the prime-power bound; asymptotically $N(d) \ge d^{0.0833}$ for infinitely many $d$, beating the $O(1)$ generic bound.
- **Weiner's gap theorem (2013).** No $d$-element unextendible MUB set exists; hence $N(d)\in\{\dots,d-1\}\cup\{d+1\}$.
- **Dimension 6, restricted classes.**
  - No complete set of $7$ MUBs exists among bases built from the Weyl–Heisenberg group of $\mathbb{Z}_6$.
  - McNulty–Weigert: no set of $4$ MUBs in $\mathbb{C}^6$ in which all vectors are product vectors of a $\mathbb{C}^2\otimes\mathbb{C}^3$ factorisation.
  - Jaming–Matolcsi–Móra–Szöllősi–Weiner (2009): a continuous infinite family of MUB *triplets* in $d=6$ exists, none extendible to a quadruple.
  - Raynal–Lü–Englert (2011): classification of MUB triples containing the Fourier basis, all shown non-extendible.
  - Brierley–Weigert: numerical optimisation over the full $70$-parameter space finds sets of $3$ MUBs plus a fourth basis reaching overlap deviation $\approx 10^{-1}$, never $0$.
- **Small non-prime-power dimensions.** For $d=6,10,12,14,15,\dots$ no exact value of $N(d)$ is proven; only the interval $[p_1^{k_1}+1,\ d+1]$ (refined by Weiner to exclude $d$).

## 5. Principal Obstacles

- **No group to hang the construction on.** Every known complete set comes from a maximal abelian decomposition of a Heisenberg/Pauli group over $\mathrm{GF}(p^k)$. For $d=6$ the natural group $\mathbb{Z}_6$-Weyl–Heisenberg factorises as $\mathbb{Z}_2\times\mathbb{Z}_3$ and its commuting classes yield only $3$ MUBs. There is no field of order $6$, so the Gauss-sum machinery has nothing to act on.
- **Character-sum / Fourier methods break down.** Unbiasedness for prime powers is *exactly* the statement that a quadratic character sum has modulus $\sqrt d$ (Weil bound / Gauss sums). Over $\mathbb{Z}_6$ the relevant exponential sums do not have uniform modulus, and no substitute orthogonality relation is known.
- **The upper-bound argument is too coarse.** The dimension count $N(d-1)\le d^2-1$ uses only pairwise orthogonality of the $V_a$; it is blind to the *positivity* constraint that each $V_a$ must be spanned by rank-one projectors. Making positivity quantitative is the missing ingredient, and semidefinite relaxations of it so far return only the trivial bound $d+1$.
- **The variety of complex Hadamard matrices in $d=6$ is not classified.** Existence of $4$ MUBs is a system of polynomial equations on (at least) the known Hadamard families — Fourier $F_6^{(2)}$, Björck's circulant $C_6$, Karlsson's three-parameter family $K_6$, the isolated spectral matrix $S_6$ — plus possibly undiscovered components. Without a complete classification, "no solution found" is not "no solution".
- **Dimension of the search space.** A quadruple of bases in $\mathbb{C}^6$ is a point on a real variety of dimension $\sim 10^2$ defined by thousands of quartic equations. Gröbner-basis elimination blows up; numerical algebraic geometry cannot certify emptiness.
- **Design-theoretic analogies are only heuristic.** The MOLS/affine-plane analogy (Saniga–Planat–Rosu) suggests $N(6)=3$ because no pair of orthogonal Latin squares of order $6$ exists (Euler/Tarry), but no theorem transports Bruck–Ryser-type nonexistence into the complex Hilbert-space setting.

## 6. The Gap

Proven: $N(d)=d+1$ for prime powers; $N(d)\ge p_1^{k_1}+1$ in general; $N(d)\ne d$. Conjectured: $N(6)=3$, and more broadly $N(d)<d+1$ for non-prime-power $d$.

The gap is a **missing upper-bound technique**. Every existing upper bound on $N(d)$ is the linear-algebraic $d+1$, valid for all $d$ and hence carrying zero arithmetic information about $d$. What is needed is an obstruction functional $\Phi$ on MUB sets — a moment inequality, a representation-theoretic invariant, or a rigidity/positivity certificate — that is sensitive to the factorisation of $d$ and provably violated when $N(6)\ge4$. Symmetrically, on the construction side, the gap is the absence of any algebraic object playing the role of $\mathrm{GF}(6)$; ring-theoretic, quantum-group, and near-field substitutes have all failed to produce a fourth basis.

## 7. Current Research (as of June 2026)

- **Certified numerics for $d=6$.** Groups in Budapest (Rényi Institute; Matolcsi, Weiner, Szöllősi) continue rigorous interval-arithmetic exclusion arguments over discretised parameter spaces for MUB quadruples. Coverage of the full Hadamard variety remains incomplete. *(frontier — verify)*
- **Sums-of-squares and noncommutative positivity.** Attempts to encode the MUB conditions as a noncommutative polynomial optimisation problem and use NPA/Lasserre hierarchies; the hierarchies converge slowly and have not yet certified $N(6)\le 3$ at any feasible level. *(frontier — verify)*
- **Approximate and weak MUBs.** $\varepsilon$-MUBs (overlaps within $\varepsilon$ of $1/d$) exist in abundance in every dimension; understanding the sharp threshold $\varepsilon(d)$ at which $d+1$ approximate bases become possible is an active substitute question, with applications to derandomised tomography and locking.
- **MUBs and SIC-POVMs.** Zauner's conjecture on symmetric informationally complete POVMs and the MUB problem are studied jointly (Appleby, Bengtsson, Flammia, Fuchs, Scott); the number-theoretic Stark-unit structure found for SICs has no MUB analogue yet, which is itself a research target.
- **Entanglement structure.** Classification of MUB sets by the entanglement of their vectors under bipartitions of composite $d$ (McNulty, Weigert, Pittenger–Rubin) continues to rule out structured families in $d=6,10$.
- **Lower bounds in composite dimensions.** Extensions of the Wocjan–Beth MOLS technique to non-square dimensions and to orthogonal-array constructions; improvements over $p_1^{k_1}+1$ remain sparse and asymptotic.

## 8. Future Work

- Complete the classification of $6\times6$ complex Hadamard matrices; this is widely regarded as a prerequisite for a rigorous $N(6)\le3$ proof.
- Develop an upper-bound method that uses the positivity/rank-one structure of MUB projectors, e.g. via association schemes, the Delsarte LP bound for lines in $\mathbb{C}^d$, or Terwilliger-algebra semidefinite programming.
- Prove or refute the weaker statement: $N(d)\le d$ for all non-prime-power $d$ (equivalently, no complete set exists unless $d$ is a prime power). Combined with Weiner's gap theorem this would already be a major advance.
- Seek a genuine combinatorial equivalence — not just an analogy — between complete MUB sets and affine planes of order $d$, which would transfer Bruck–Ryser–Chowla nonexistence.
- Quantify the trade-off in applications: how much does tomographic efficiency, locking capacity, or QKD key rate degrade with $3$ rather than $7$ bases in $d=6$?

## 9. Key References

- **[Foundational]** J. Schwinger. *Unitary operator bases.* Proceedings of the National Academy of Sciences 46(4):570–579, 1960.
- **[Foundational]** I. D. Ivanović. *Geometrical description of quantal state determination.* Journal of Physics A: Mathematical and General 14:3241–3245, 1981.
- **[Foundational]** W. K. Wootters and B. D. Fields. *Optimal state-determination by mutually unbiased measurements.* Annals of Physics 191(2):363–381, 1989.
- **[Foundational]** A. R. Calderbank, P. J. Cameron, W. M. Kantor, J. J. Seidel. *$\mathbb{Z}_4$-Kerdock codes, orthogonal spreads, and extremal Euclidean line-sets.* Proceedings of the London Mathematical Society 75(2):436–480, 1997.
- **[Construction]** S. Bandyopadhyay, P. O. Boykin, V. Roychowdhury, F. Vatan. *A new proof for the existence of mutually unbiased bases.* Algorithmica 34:512–528, 2002.
- **[Construction]** A. Klappenecker and M. Rötteler. *Constructions of mutually unbiased bases.* In Finite Fields and Applications (Fq7), Lecture Notes in Computer Science 2948, Springer, pp. 137–144, 2004.
- **[Construction]** P. Wocjan and T. Beth. *New construction of mutually unbiased bases in square dimensions.* Quantum Information and Computation 5(2):93–101, 2005.
- **[Structure]** P. O. Boykin, M. Sitharam, P. H. Tiep, P. Wocjan. *Mutually unbiased bases and orthogonal decompositions of Lie algebras.* Quantum Information and Computation 7(4):371–382, 2007.
- **[SOTA]** M. Weiner. *A gap for the maximum number of mutually unbiased bases.* Proceedings of the American Mathematical Society 141(6):1963–1969, 2013.
- **[SOTA / $d=6$]** P. Jaming, M. Matolcsi, P. Móra, F. Szöllősi, M. Weiner. *A generalized Pauli problem and an infinite family of MUB-triplets in dimension 6.* Journal of Physics A: Mathematical and Theoretical 42:245305, 2009.
- **[SOTA / $d=6$]** P. Raynal, X. Lü, B.-G. Englert. *Mutually unbiased bases in six dimensions: The four most distant bases.* Physical Review A 83:062303, 2011.
- **[Survey]** T. Durt, B.-G. Englert, I. Bengtsson, K. Życzkowski. *On mutually unbiased bases.* International Journal of Quantum Information 8(4):535–640, 2010.
- **[Survey]** I. Bengtsson. *Three ways to look at mutually unbiased bases.* AIP Conference Proceedings 889:40–51, 2007.
- **[Application]** D. P. DiVincenzo, M. Horodecki, D. W. Leung, J. A. Smolin, B. M. Terhal. *Locking classical correlations in quantum states.* Physical Review Letters 92:067902, 2004.

## 10. Worked Example / Concrete Special Case

**Construction for $d=3$ (complete set of $4$ MUBs).** Take $\omega = e^{2\pi i/3}$ and use $|\psi^a_j\rangle = \tfrac{1}{\sqrt3}\sum_{k=0}^{2}\omega^{ak^2+jk}|k\rangle$. Since $k^2 \bmod 3 = (0,1,1)$ for $k=(0,1,2)$:

$$\mathcal{B}_0 = \{|0\rangle,|1\rangle,|2\rangle\},\qquad
\mathcal{B}_1 = \tfrac{1}{\sqrt3}\begin{pmatrix}1&1&1\\ 1&\omega&\omega^2\\ 1&\omega^2&\omega\end{pmatrix},$$

$$\mathcal{B}_2 = \tfrac{1}{\sqrt3}\begin{pmatrix}1&1&1\\ \omega&\omega^2&1\\ \omega&1&\omega^2\end{pmatrix},\qquad
\mathcal{B}_3 = \tfrac{1}{\sqrt3}\begin{pmatrix}1&1&1\\ \omega^2&1&\omega\\ \omega^2&\omega&1\end{pmatrix},$$

columns being the vectors ($\mathcal{B}_1$ is $a=0$, i.e. the Fourier basis; $\mathcal{B}_2$ is $a=1$; $\mathcal{B}_3$ is $a=2$).

*Check one overlap.* First column of $\mathcal{B}_2$ against first column of $\mathcal{B}_1$:

$$\langle \psi^{0}_0|\psi^{1}_0\rangle = \tfrac13(1\cdot 1 + 1\cdot\omega + 1\cdot\omega) = \tfrac{1+2\omega}{3}.$$

With $\omega = -\tfrac12 + i\tfrac{\sqrt3}{2}$ we get $1+2\omega = i\sqrt3$, so $|\langle\cdot\rangle|^2 = 3/9 = 1/3$. ✓

*Check against the computational basis.* Every entry of every $\mathcal{B}_a$, $a\ge1$, has modulus $1/\sqrt3$, so $|\langle k|\psi^a_j\rangle|^2 = 1/3$ automatically. ✓

The general pair overlap for $a\ne b$ is $\big|\tfrac13\sum_k \omega^{(a-b)k^2+(j-j')k}\big|$, a Gauss sum of modulus $\sqrt3$, giving $1/3$ in every case. Hence $N(3)=4=3+1$.

**Where this collapses at $d=6$.** Repeating the recipe with $\omega_6=e^{2\pi i /6}$ fails immediately: the sum $\sum_{k=0}^{5}\omega_6^{k^2}$ has modulus $\sqrt{12} \ne \sqrt 6$, because $2$ is not invertible mod $6$ and the quadratic form $k\mapsto k^2$ is degenerate on $\mathbb{Z}_6$. What survives is only the tensor construction $\mathbb{C}^6=\mathbb{C}^2\otimes\mathbb{C}^3$: pairing $\{$$Z,X,Y$ eigenbases of the qubit$\}$ with three of the four qutrit MUBs above gives exactly $\min\{3,4\}=3$ MUBs. Explicitly, with the qubit bases $\{|0\rangle,|1\rangle\}$, $\tfrac{1}{\sqrt2}(|0\rangle\pm|1\rangle)$, $\tfrac{1}{\sqrt2}(|0\rangle\pm i|1\rangle)$, the products give bases $\mathcal{M}_0=\mathcal{B}^{(2)}_0\otimes\mathcal{B}^{(3)}_0$, $\mathcal{M}_1=\mathcal{B}^{(2)}_1\otimes\mathcal{B}^{(3)}_1$, $\mathcal{M}_2=\mathcal{B}^{(2)}_2\otimes\mathcal{B}^{(3)}_2$ with all cross-overlaps $\tfrac12\cdot\tfrac13=\tfrac16$. ✓

Whether a fourth vector set can be adjoined — necessarily entangled, by McNulty–Weigert — is precisely the open problem. Numerical maximisation of $\sum_{a<b}\sum_{i,j}\big(|\langle e^a_i|e^b_j\rangle|^2-\tfrac16\big)^2$ over four bases in $\mathbb{C}^6$ converges to a strictly positive minimum in every reported run, but no proof exists that the minimum is nonzero.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*