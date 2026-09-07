---
id: 10-theoretical-cs/shortest-vector-approximation
title: "Shortest Vector Approximation"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Shortest Vector Approximation

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/shortest-vector-approximation` · **Status:** open

## 1. Problem Statement / Conjecture

Given a basis $B \in \mathbb{Q}^{m \times n}$ of a lattice $\mathcal{L}(B)$, the **Shortest Vector Problem** $\mathrm{SVP}_\gamma$ asks for a nonzero $v \in \mathcal{L}(B)$ with $\|v\| \le \gamma(n)\cdot\lambda_1(\mathcal{L}(B))$, where $\lambda_1$ is the length of a shortest nonzero lattice vector and $\gamma \ge 1$ is the approximation factor.

The open problem has two halves that have never met:

- **Algorithmic side.** No polynomial-time algorithm is known for any $\gamma = n^{O(1)}$ better than $2^{\Theta(n\log\log n/\log n)}$ — essentially exponential in $n$. **Question:** is $\mathrm{SVP}_{\mathrm{poly}(n)}$ in $\mathrm{P}$?
- **Hardness side.** NP-hardness is known only up to $\gamma = 2^{(\log n)^{1-\varepsilon}}$ (and only under randomized or quasi-polynomial reductions). **Conjecture (folklore, implicit in Ajtai 1996 and Regev 2005):** $\mathrm{SVP}_{n^c}$ is hard for every constant $c$, in the average case, even for quantum algorithms.

A resolution means either (i) a polynomial-time algorithm achieving $\gamma = \mathrm{poly}(n)$ in the $\ell_2$ norm, or (ii) an NP-hardness proof (under deterministic Karp reductions) for $\gamma = n^{\Omega(1)}$. Both are open. The interval $\gamma \in [2^{(\log n)^{1-\varepsilon}},\ \sqrt{n/\log n}]$ is the region where SVP is neither known to be NP-hard nor known to be easy, and this is exactly the region in which all lattice-based cryptography lives.

## 2. Mathematical Foundations

A **lattice** of rank $n$ is $\mathcal{L}(B)=\{Bx : x \in \mathbb{Z}^n\}$ for linearly independent $b_1,\dots,b_n \in \mathbb{R}^m$. Its **determinant** is $\det \mathcal{L} = \sqrt{\det(B^\top B)}$, invariant under $B \mapsto BU$, $U \in \mathrm{GL}_n(\mathbb{Z})$.

**Successive minima.** For $1\le i\le n$,
$$\lambda_i(\mathcal{L}) = \min\{r>0 : \dim \mathrm{span}\big(\mathcal{L}\cap \bar{B}(0,r)\big)\ge i\}.$$

**Minkowski's second theorem.** $\left(\prod_{i=1}^n \lambda_i\right)^{1/n} \le \sqrt{\gamma_n}\,(\det\mathcal{L})^{1/n}$, where $\gamma_n$ is Hermite's constant, $\gamma_n = \Theta(n)$. Hence $\lambda_1 \le \sqrt{\gamma_n}(\det\mathcal{L})^{1/n}$ — an existence bound with no known efficient constructive counterpart.

**Dual lattice.** $\mathcal{L}^* = \{y \in \mathrm{span}(\mathcal{L}) : \langle y,x\rangle \in \mathbb{Z}\ \forall x\in\mathcal{L}\}$. Transference (Banaszczyk 1993): $\lambda_1(\mathcal{L})\cdot\lambda_n(\mathcal{L}^*) \le n$.

**Gaussian mass.** For $s>0$, $\rho_s(x)=e^{-\pi\|x\|^2/s^2}$ and $\rho_s(\mathcal{L})=\sum_{x\in\mathcal{L}}\rho_s(x)$. The **smoothing parameter** $\eta_\varepsilon(\mathcal{L})$ is the least $s$ with $\rho_{1/s}(\mathcal{L}^*\setminus\{0\})\le\varepsilon$; Poisson summation gives $\rho_s(\mathcal{L}) = s^n\det(\mathcal{L})^{-1}\rho_{1/s}(\mathcal{L}^*)$, the engine of both the AKS/ADRS algorithms and the Aharonov–Regev coNP proof.

**Decision version.** $\mathrm{GapSVP}_\gamma$: given $(B,d)$, decide $\lambda_1 \le d$ (YES) or $\lambda_1 > \gamma d$ (NO).

**LLL guarantee.** An LLL-reduced basis with parameter $\delta=3/4$ satisfies $\|b_1\| \le 2^{(n-1)/2}\lambda_1(\mathcal{L})$ and $\|b_1\|\le 2^{(n-1)/4}(\det\mathcal{L})^{1/n}$, computed in time polynomial in $n$ and the bit-size of $B$.

**Schnorr's hierarchy / slide reduction.** With a $2^{O(k)}$-time exact SVP oracle in dimension $k$, block reduction outputs $b_1$ with $\|b_1\| \le \gamma_k^{\frac{n-1}{2(k-1)}}\lambda_1$, i.e. approximation $2^{\tilde O(n/k)}$ in time $2^{O(k)}$. Setting $k=\log n$ gives the polynomial-time record $\gamma = 2^{O(n\log\log n/\log n)}$.

## 3. History & State of the Art (SOTA)

- **1773–1850.** Lagrange and Gauss solve rank 2 exactly by a Euclidean-style reduction; Hermite gives the first general reduction and the constant $\gamma_n$.
- **1981.** van Emde Boas proves SVP NP-hard in the $\ell_\infty$ norm and conjectures $\ell_2$ hardness — a conjecture that stood 17 years.
- **1982.** Lenstra, Lenstra and Lovász give the LLL algorithm: $\gamma = 2^{(n-1)/2}$ in polynomial time. Immediate applications: factoring rational polynomials, integer programming in fixed dimension, breaking knapsack cryptosystems.
- **1987.** Schnorr's block reduction hierarchy; refined to BKZ (1994) and to slide reduction (Gama–Nguyen 2008), giving $2^{\tilde O(n/k)}$ in time $2^{O(k)}$.
- **1996.** Ajtai's worst-case-to-average-case reduction: solving a random instance of the Short Integer Solution problem on average is as hard as approximating SVP in the worst case to within $\mathrm{poly}(n)$. This turned SVP approximation into the foundation of a cryptographic program.
- **1998.** Ajtai: $\mathrm{SVP}$ in $\ell_2$ is NP-hard under randomized reductions.
- **2001.** Micciancio: NP-hard to approximate within any $\gamma < \sqrt2$.
- **2001.** Ajtai–Kumar–Sivakumar: randomized sieve solving exact SVP in $2^{O(n)}$ time and space; $2^{O(n/\varepsilon)}$ for factor $1+\varepsilon$.
- **2005.** Khot: NP-hard for every constant factor, and hard for $2^{(\log n)^{1/2-\varepsilon}}$ under randomized quasi-polynomial reductions. Haviv–Regev (2007) push this to $2^{(\log n)^{1-\varepsilon}}$.
- **2005.** Regev introduces LWE with a quantum reduction from $\mathrm{GapSVP}_{\tilde O(n/\alpha)}$; Peikert (2009) gives a classical reduction for $\mathrm{GapSVP}$ with exponential modulus.
- **2010.** Micciancio–Voulgaris: deterministic $2^{2n+o(n)}$ exact SVP/CVP via Voronoi cells.
- **2015.** Aggarwal–Dadush–Regev–Stephens-Davidowitz: discrete Gaussian sampling gives exact SVP in $2^{n+o(n)}$ time — still the record.
- **2018.** Aggarwal–Stephens-Davidowitz: under (Gap-)ETH-style assumptions, no $2^{o(n)}$ algorithm for SVP in $\ell_p$, $p \ne 2$ even integer; fine-grained lower bounds under SETH for CVP (Bennett–Golovnev–Stephens-Davidowitz 2017).

**Current SOTA.** Best polynomial-time factor: $2^{\Theta(n\log\log n/\log n)}$. Best exact algorithm: $2^{n+o(n)}$ time and space. Best NP-hardness: $2^{(\log n)^{1-\varepsilon}}$ under randomized quasi-poly reductions; $\sqrt{2}-\varepsilon$ under deterministic reductions (Micciancio 2012). Best non-hardness: $\mathrm{GapSVP}_{\sqrt{n/\log n}} \in \mathrm{NP}\cap\mathrm{coNP}$ (Goldreich–Goldwasser 1998), improved to $\mathrm{GapSVP}_{\sqrt n}\in \mathrm{NP}\cap\mathrm{coNP}$ (Aharonov–Regev 2005).

## 4. Partial Results / Verified Cases

- **Rank $n \le 4$:** exact SVP in polynomial time. Lagrange–Gauss reduction settles $n=2$ in $O(\log^2 \|B\|)$ arithmetic steps; Semaev (2001) gives a clean rank-3 algorithm; Nguyen–Stehlé (2009) give a provably polynomial greedy algorithm through rank 4.
- **Fixed rank $n=O(1)$:** exact SVP is polynomial by Kannan's enumeration, running in $n^{O(n)}$ time and polynomial space (Kannan 1983; refined to $n^{n/(2e)+o(n)}$ by Hanrot–Stehlé 2007).
- **Constant approximation, low dimension in the exponent:** $(1+\varepsilon)$-approximation in $2^{O(n)}\cdot(1/\varepsilon)^{O(n)}$ time (AKS 2001; Nguyen–Vidick 2008).
- **$\gamma \ge \sqrt n$:** not NP-hard unless $\mathrm{NP}=\mathrm{coNP}$ (Aharonov–Regev 2005); $\gamma \ge \sqrt{n/\log n}$ not NP-hard unless the polynomial hierarchy collapses (Goldreich–Goldwasser 1998).
- **$\gamma \ge n/\sqrt{\log n}$:** $\mathrm{GapSVP}_\gamma \in \mathrm{coAM}$ and also in $\mathrm{P}^{\mathrm{SZK}}$-adjacent classes; and $\mathrm{GapSVP}_{n}$ reduces to $\mathrm{GapSVP}$ on the dual via transference.
- **Structured lattices:** for ideal lattices in cyclotomic fields, $\mathrm{SVP}$ with factor $2^{\tilde O(\sqrt n)}$ is solvable in quantum polynomial time (Cramer–Ducas–Peikert–Regev 2016, for principal ideals with a short generator; Cramer–Ducas–Wesolowski 2017 for general ideals). No such improvement is known for general lattices.
- **$\ell_\infty$ norm:** NP-hard to approximate within $n^{c/\log\log n}$ (Dinur 2002), a far stronger factor than anything known for $\ell_2$.

## 5. Principal Obstacles

- **The $\sqrt n$ barrier is real, not technical.** Goldreich–Goldwasser build a constant-round interactive proof for the NO instances of $\mathrm{GapSVP}_{\sqrt{n/\log n}}$ using the fact that balls of radius $\lambda_1/2$ tile sparsely; Aharonov–Regev replace the protocol with a deterministic witness (a Fourier-analytic certificate built from $\rho_{1/s}(\mathcal{L}^*)$). Any NP-hardness proof above $\sqrt n$ would collapse $\mathrm{NP}$ and $\mathrm{coNP}$. So the *only* hope for hardness in the cryptographic regime $\gamma = \mathrm{poly}(n)$ is a hardness notion weaker than NP-hardness — but no candidate complete problem is known there.
- **Reductions are inherently randomized.** Khot's and Ajtai's constructions use random sparsification and BCH-code-based gadgets whose "no short vector" side holds only with high probability; derandomizing them needs explicit lattices with certified large $\lambda_1$ and many near-minimal vectors, which is a construction problem as hard as explicit good codes. Micciancio (2012) derandomizes only up to $\sqrt2$.
- **PCP machinery does not transfer.** Label-cover-style gap amplification for CVP (Dinur–Kindler–Raz–Safra, factor $n^{c/\log\log n}$) fails for SVP because the homogeneity of SVP — the target is $0$ and the lattice is closed under negation and scaling — destroys the "one distinguished target" structure that CVP reductions exploit. Tensoring, the natural amplification, boosts the gap but also creates spurious short vectors unless the base lattice is *tensor-robust*; Haviv–Regev's construction is tensor-robust only for quasi-polynomially many rounds, capping the factor at $2^{(\log n)^{1-\varepsilon}}$.
- **Algorithmic side: sieving is space-bound.** All $2^{O(n)}$ algorithms store $2^{\Theta(n)}$ lattice points; the Micciancio–Voulgaris Voronoi approach also needs $2^n$ space. No technique is known to trade the exponential list for structure, and the $2^{n+o(n)}$ ADRS bound has resisted improvement since 2015.
- **Blockwise reduction saturates.** Schnorr-type reduction cannot beat $\gamma \approx \gamma_k^{n/k}$; achieving $\gamma = \mathrm{poly}(n)$ demands $k = \Omega(n/\log n)$, i.e. subexponential-time exact SVP in dimension $k$ — which is exactly the barrier at issue.

## 6. The Gap

Proven: NP-hardness for $\gamma \le 2^{(\log n)^{1-\varepsilon}}$ (randomized, quasi-poly reductions). Non-hardness: $\gamma \ge \sqrt{n/\log n}$ lies in $\mathrm{NP}\cap\mathrm{coNP}$. Algorithms: polynomial time only for $\gamma \ge 2^{\Theta(n\log\log n/\log n)}$.

Two disjoint gaps therefore remain:

1. **Complexity gap:** $2^{(\log n)^{1-\varepsilon}} < \gamma < \sqrt{n/\log n}$ — quasi-polynomial in width. Closing it requires either a deterministic gap-amplification for a homogeneous problem (a tensor-robust lattice family surviving $\omega(\log n /\log\log n)$ tensor powers), or a proof that the region is *not* NP-hard.
2. **Algorithmic gap:** $\sqrt n < \gamma < 2^{n\log\log n/\log n}$ — exponentially wide. Nothing rules out a polynomial-time $\gamma = n$ algorithm; equally nothing suggests one. The single missing step is a polynomial-time procedure that certifies or constructs a vector of length $O(\sqrt{\gamma_n})\,(\det \mathcal{L})^{1/n}$, i.e. a constructive Minkowski theorem.

## 7. Current Research (as of June 2026)

- **Fine-grained hardness.** Aggarwal, Bennett, Golovnev, Stephens-Davidowitz and collaborators continue to sharpen $2^{o(n)}$ lower bounds under Gap-ETH and SETH, aiming to cover $\ell_2$ (currently open for $p=2$ under SETH). Groups at NYU, Ruhr-Universität Bochum, and CWI.
- **Sieving in practice.** The G6K framework (Albrecht–Ducas–Herold–Kirshanova–Postlethwaite–Stevens, 2019) and its GPU successors drive the TU Darmstadt SVP Challenge; records now exceed dimension 190 *(frontier — verify current record dimension)*.
- **Ideal and module lattices.** Continued study of whether the $2^{\tilde O(\sqrt n)}$ quantum advantage for ideal lattices extends to module lattices of rank $\ge 2$ — the setting of Kyber/Dilithium. Consensus so far: no attack better than generic for rank $\ge 2$ *(frontier — verify)*.
- **Derandomizing hardness.** Attempts to build explicit tensor-robust lattices from algebraic-geometry codes or from Reed–Solomon-type constructions, aiming to lift Micciancio's deterministic $\sqrt 2$ toward Khot's randomized bounds.
- **Post-quantum standardization feedback.** NIST's ML-KEM/ML-DSA rest on module-LWE, whose security ultimately traces to $\mathrm{GapSVP}_{\tilde O(n/\alpha)}$; concrete-security estimation of BKZ cost ("core-SVP" model) remains contested.

## 8. Future Work

- Prove or refute NP-hardness of $\mathrm{GapSVP}_{n^{\varepsilon}}$ for some $\varepsilon>0$; even a hardness result under a natural non-NP assumption (e.g. hardness for $\mathrm{SZK}$ or under Gap-ETH) at a polynomial factor would be a milestone.
- Find a lattice family that is tensor-robust under $\mathrm{poly}(\log n)$ tensorings, or prove none exists.
- Improve exact SVP below $2^{n}$, or prove a $2^{(1-o(1))n}$ conditional lower bound in $\ell_2$.
- Devise a polynomial-space algorithm matching sieving's $2^{O(n)}$ time — currently enumeration costs $n^{\Theta(n)}$.
- Constructive Minkowski: a polynomial-time algorithm returning $v \ne 0$ with $\|v\| \le \mathrm{poly}(n)(\det\mathcal{L})^{1/n}$ would immediately give $\gamma=\mathrm{poly}(n)$ via the standard reduction and break all lattice cryptography.

## 9. Key References

- **[Foundational]** A. K. Lenstra, H. W. Lenstra Jr., L. Lovász. *Factoring polynomials with rational coefficients.* Mathematische Annalen 261(4), 515–534, 1982.
- **[Foundational]** P. van Emde Boas. *Another NP-complete problem and the complexity of computing short vectors in a lattice.* Technical Report 81-04, Mathematisch Instituut, Universiteit van Amsterdam, 1981.
- **[Foundational]** M. Ajtai. *Generating hard instances of lattice problems.* STOC 1996, 99–108.
- **[Foundational]** M. Ajtai. *The shortest vector problem in $L_2$ is NP-hard for randomized reductions.* STOC 1998, 10–19.
- **[Foundational]** D. Micciancio. *The shortest vector in a lattice is hard to approximate to within some constant.* SIAM Journal on Computing 30(6), 2008–2035, 2001.
- **[Foundational]** O. Goldreich, S. Goldwasser. *On the limits of non-approximability of lattice problems.* Journal of Computer and System Sciences 60(3), 540–563, 2000 (STOC 1998).
- **[Foundational]** D. Aharonov, O. Regev. *Lattice problems in NP ∩ coNP.* Journal of the ACM 52(5), 749–765, 2005.
- **[SOTA / Recent]** S. Khot. *Hardness of approximating the shortest vector problem in lattices.* Journal of the ACM 52(5), 789–808, 2005.
- **[SOTA / Recent]** I. Haviv, O. Regev. *Tensor-based hardness of the shortest vector problem to within almost polynomial factors.* Theory of Computing 8, 513–531, 2012 (STOC 2007).
- **[SOTA / Recent]** D. Micciancio, P. Voulgaris. *A deterministic single exponential time algorithm for most lattice problems based on Voronoi cell computations.* SIAM Journal on Computing 42(3), 1364–1391, 2013 (STOC 2010).
- **[SOTA / Recent]** D. Aggarwal, D. Dadush, O. Regev, N. Stephens-Davidowitz. *Solving the shortest vector problem in $2^n$ time using discrete Gaussian sampling.* STOC 2015, 733–742.
- **[SOTA / Recent]** D. Aggarwal, N. Stephens-Davidowitz. *(Gap/S)ETH hardness of SVP.* STOC 2018, 228–238.
- **[SOTA / Recent]** O. Regev. *On lattices, learning with errors, random linear codes, and cryptography.* Journal of the ACM 56(6), Article 34, 2009 (STOC 2005).
- **[SOTA / Recent]** M. R. Albrecht, L. Ducas, G. Herold, E. Kirshanova, E. W. Postlethwaite, M. Stevens. *The general sieve kernel and new records in lattice reduction.* EUROCRYPT 2019, 717–746.
- **[Survey]** D. Micciancio, S. Goldwasser. *Complexity of Lattice Problems: A Cryptographic Perspective.* Kluwer Academic Publishers, 2002.
- **[Survey]** P. Q. Nguyen, B. Vallée (eds.). *The LLL Algorithm: Survey and Applications.* Springer, 2010.
- **[Survey]** C. Peikert. *A decade of lattice cryptography.* Foundations and Trends in Theoretical Computer Science 10(4), 283–424, 2016.

## 10. Worked Example / Concrete Special Case

**Exact SVP in rank 2 by Lagrange–Gauss reduction.** Take
$$B=\begin{pmatrix}3 & 4\\ 1 & 2\end{pmatrix},\qquad b_1=(3,1),\ b_2=(4,2),\qquad \det\mathcal{L}=|3\cdot2-4\cdot1|=2.$$

*Step 1.* $\|b_1\|^2=10 < \|b_2\|^2=20$, so no initial swap. Compute $\mu = \dfrac{\langle b_2,b_1\rangle}{\|b_1\|^2}=\dfrac{12+2}{10}=1.4$, round to $1$:
$$b_2 \leftarrow b_2 - 1\cdot b_1 = (1,1),\quad \|b_2\|^2 = 2.$$
Since $2 < 10$, swap: $b_1=(1,1)$, $b_2=(3,1)$.

*Step 2.* $\mu = \dfrac{\langle (3,1),(1,1)\rangle}{\|(1,1)\|^2} = \dfrac{4}{2}=2$:
$$b_2 \leftarrow (3,1)-2(1,1) = (1,-1),\quad \|b_2\|^2 = 2 \not< 2 = \|b_1\|^2.$$
Terminate. The basis $\{(1,1),(1,-1)\}$ is Lagrange-reduced, hence $\lambda_1 = \|(1,1)\| = \sqrt2$ **exactly** — in rank 2, reduction solves SVP, no approximation needed.

*Consistency with Minkowski.* $\gamma_2 = 2/\sqrt3$, so the bound reads $\lambda_1 \le \sqrt{2/\sqrt3}\cdot\sqrt{\det\mathcal{L}} = 1.0746\cdot\sqrt2 = 1.5197$, and indeed $\sqrt2 = 1.4142 \le 1.5197$.

**Why this collapses in high rank.** Repeat the same logic in rank $n$: LLL guarantees only
$$\|b_1\| \le 2^{(n-1)/4}(\det\mathcal{L})^{1/n}.$$
For $n=200$ the factor is $2^{49.75} \approx 6\times10^{14}$, while Minkowski promises a vector within $\sqrt{\gamma_{200}}\approx 8$ of $(\det\mathcal L)^{1/n}$. The whole open problem sits in that ratio: the existence bound is $O(\sqrt n)$, the constructive bound is $2^{\Theta(n)}$ (or $2^{\Theta(n\log\log n/\log n)}$ with block reduction), and fourteen orders of magnitude of headroom in dimension 200 is precisely what Kyber-512's security margin is priced against.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*