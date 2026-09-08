---
id: 05-analysis/connes-embedding-problem
title: "Connes Embedding Problem"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Connes Embedding Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/connes-embedding-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $\mathcal{R}$ be the hyperfinite $\mathrm{II}_1$ factor and $\mathcal{R}^\omega$ its tracial ultrapower along a free ultrafilter $\omega$ on $\mathbb{N}$.

**Connes Embedding Problem (CEP).** Does every separable $\mathrm{II}_1$ factor $M$ admit a trace-preserving $*$-embedding $M \hookrightarrow \mathcal{R}^\omega$?

A positive answer requires producing, for each $M$, matricial *microstates*: finite matrices whose normalized-trace moments approximate those of $M$ to arbitrary precision. A negative answer requires exhibiting a tracial von Neumann algebra whose moment sequence is *not* a limit of matrix moments. The problem was resolved **negatively** in 2020 by Ji, Natarajan, Vidick, Wright and Yuen, via the complexity-theoretic identity $\mathrm{MIP}^* = \mathrm{RE}$ and the chain of equivalences CEP $\Leftrightarrow$ Kirchberg's QWEP conjecture $\Leftrightarrow$ Tsirelson's problem. The counterexample is **non-constructive**: no explicit non-embeddable factor is known.

## 2. Mathematical Foundations

**Tracial von Neumann algebras.** A pair $(M,\tau)$ with $M \subseteq B(H)$ a von Neumann algebra and $\tau : M \to \mathbb{C}$ a faithful normal tracial state: $\tau(1)=1$, $\tau(xy)=\tau(yx)$, $\tau(x^*x)\ge 0$ with equality iff $x=0$. The trace induces $\|x\|_2 = \tau(x^*x)^{1/2}$. $M$ is a $\mathrm{II}_1$ factor if its center is $\mathbb{C}1$ and $\dim_{\mathbb{C}} M = \infty$.

**Hyperfinite factor.** $\mathcal{R} = \overline{\bigcup_n M_{2^n}(\mathbb{C})}^{\,\mathrm{wot}}$ with $\tau = \lim \mathrm{tr}_{2^n}$, unique up to isomorphism among approximately finite-dimensional $\mathrm{II}_1$ factors (Murray–von Neumann).

**Ultrapower.** With $\mathcal{I}_\omega = \{(x_n) \in \ell^\infty(\mathcal{R}) : \lim_{n\to\omega}\|x_n\|_2 = 0\}$,
$$\mathcal{R}^\omega = \ell^\infty(\mathbb{N},\mathcal{R})/\mathcal{I}_\omega, \qquad \tau_\omega\big([(x_n)]\big) = \lim_{n\to\omega} \tau(x_n).$$

**Microstate formulation.** $M$ with generators $x_1,\dots,x_k$ embeds into $\mathcal{R}^\omega$ iff for every $\varepsilon>0$ and every $d\in\mathbb{N}$ there exist $n$ and matrices $A_1,\dots,A_k \in M_n(\mathbb{C})$, $\|A_i\|\le \|x_i\|$, with
$$\big|\mathrm{tr}_n\big(A_{i_1}^{\epsilon_1}\cdots A_{i_m}^{\epsilon_m}\big) - \tau\big(x_{i_1}^{\epsilon_1}\cdots x_{i_m}^{\epsilon_m}\big)\big| < \varepsilon \quad \text{for all words of length } m \le d,$$
where $\epsilon_j \in \{1,*\}$ and $\mathrm{tr}_n = \frac1n \mathrm{Tr}$.

**Kirchberg's QWEP conjecture.** Every C\*-algebra is a quotient of one with the weak expectation property; equivalently
$$C^*(\mathbb{F}_\infty) \otimes_{\min} C^*(\mathbb{F}_\infty) = C^*(\mathbb{F}_\infty) \otimes_{\max} C^*(\mathbb{F}_\infty).$$
Kirchberg (1993) proved QWEP $\Leftrightarrow$ CEP.

**Tsirelson's problem.** For a bipartite scenario with $n$ inputs and $k$ outputs, let $C_q(n,k)$ be correlations $p(a,b\mid x,y) = \langle \psi, A^x_a B^y_b \psi\rangle$ from finite-dimensional tensor-product strategies, $C_{qa} = \overline{C_q}$, and $C_{qc}$ those from commuting-operator strategies on a single Hilbert space ($[A^x_a,B^y_b]=0$). Then $C_q \subseteq C_{qa} \subseteq C_{qc}$, and
$$\text{CEP holds} \iff C_{qa}(n,k) = C_{qc}(n,k) \ \ \forall n,k$$
(Junge–Navascués–Palazuelos–Pérez-García–Scholz–Werner 2011; Fritz 2012; Ozawa 2013).

**The resolution.** $\mathrm{MIP}^* = \mathrm{RE}$ implies the value $\omega^*(G) = \sup_{C_q}$ of a nonlocal game is uncomputable, while $\omega^{qc}(G) = \sup_{C_{qc}}$ is upper semi-computable by the NPA semidefinite hierarchy. Hence $\omega^* \neq \omega^{qc}$ for some game, so $C_{qa} \subsetneq C_{qc}$, so CEP fails.

## 3. History & State of the Art (SOTA)

- **1976.** Connes, in *Classification of injective factors* (Annals of Math. 104), remarks in passing that any $\mathrm{II}_1$ factor "ought to be" embeddable in $\mathcal{R}^\omega$ — one sentence that became a 44-year program.
- **1993.** Kirchberg establishes the C\*-algebraic reformulation (QWEP) and the $\min$–$\max$ tensor-norm criterion for $C^*(\mathbb{F}_\infty)$.
- **2000s.** Voiculescu's free entropy makes microstates the central technique; Brown–Ozawa's monograph (2008) organizes the finite-dimensional-approximation landscape. Radulescu, Collins–Dykema, Klep–Schweighofer and Netzer–Thom give algebraic/Positivstellensatz reformulations.
- **2011–2013.** Tsirelson's problem is shown equivalent to CEP; Ozawa's *Japan. J. Math.* survey turns CEP into a noncommutative real-algebraic-geometry question about sums of squares.
- **2019.** Slofstra proves $C_q(n,k)$ is not closed for some $n,k$, using linear-system games and group-theoretic embedding theorems — the first hard separation in the hierarchy, though not $C_{qa}$ vs $C_{qc}$.
- **January 2020.** $\mathrm{MIP}^*=\mathrm{RE}$ (arXiv:2001.04383). CEP, QWEP and Tsirelson's problem all fail.
- **2021–2026.** Consolidation: Goldbring–Hart's Bulletin AMS guided tour; Vidick's almost-synchronous rounding theorem; de la Salle's stability-based simplifications; ongoing search for an *explicit* counterexample.

## 4. Partial Results / Verified Cases

Embeddability into $\mathcal{R}^\omega$ **is** known for large classes — all pre-2020 positive work stands:

- **Hyperfinite and amenable.** $\mathcal{R}$ itself, and $L(\Gamma)$ for every amenable $\Gamma$.
- **Residually finite groups.** $L(\Gamma)$ embeds whenever $\Gamma$ is residually finite; microstates come from left-regular representations of finite quotients (see §10). Includes $\mathbb{F}_n$, so the free group factors $L(\mathbb{F}_n)$, $2 \le n \le \infty$, embed.
- **Sofic and hyperlinear groups.** $L(\Gamma)$ embeds iff $\Gamma$ is hyperlinear; every sofic group is hyperlinear. No non-sofic group is known.
- **Closure properties (Brown–Dykema–Jung; Popa school).** The class of $\mathcal{R}^\omega$-embeddable tracial algebras is closed under: free products, tensor products, inductive limits, amalgamated free products over amenable subalgebras, HNN extensions over amenable subalgebras, crossed products $M \rtimes \Gamma$ with $\Gamma$ amenable (more generally sofic), and passage to subalgebras.
- **Rădulescu (2008).** $L(\Gamma)$ embeds for the Baumslag–Solitar-type group $\langle a,b \mid ab^3a^{-1}=b^2\rangle$, which is *not* residually finite.
- **Small parameters in Tsirelson's problem.** $C_{qa}(n,k) = C_{qc}(n,k)$ holds for all $n \le 2$ inputs with $k=2$ outputs, and for the CHSH scenario $(n,k)=(2,2)$ the maximum $2\sqrt2$ is attained in $C_q$ (Tsirelson). Separations require large games: the counterexample game from $\mathrm{MIP}^*=\mathrm{RE}$ has question/answer sets of astronomically large but finite size.
- **Free entropy dimension.** For embeddable algebras Voiculescu's microstate free entropy $\chi$ is defined; Jung's characterization gives $\mathcal{R}$-embeddability criteria via strong $1$-boundedness.

## 5. Principal Obstacles

The problem *was* open for 44 years because every available technique is one-sided.

- **Microstates are existential and unstructured.** To prove embeddability one must *construct* matrices; there is no local-to-global principle assembling approximations of subalgebras into an approximation of the whole. To *disprove* it one must certify that no matrices exist for a given moment sequence — a $\Pi_1$-type statement over an unbounded search space.
- **Positivstellensatz failure.** Ozawa's reformulation says CEP holds iff every trace-positive noncommutative polynomial is a limit of sums of hermitian squares plus commutators. Real algebraic geometry supplies archimedean Positivstellensätze in the commutative case, but the noncommutative tracial analogue has no degree bound — so no finite semidefinite certificate exists, and the NPA hierarchy converges only to $\omega^{qc}$, never to $\omega^*$.
- **Random matrices give upper bounds only.** Haagerup–Thorbjørnsen-style strong convergence shows free semicircular families are approximated by GUE matrices, so random-matrix methods only ever confirm embeddability.
- **Rigidity is too weak.** Property (T) and deformation/rigidity (Popa) distinguish factors up to isomorphism but are invisible to $\|\cdot\|_2$-approximation, which is what $\mathcal{R}^\omega$ sees.
- **Post-2020 obstacle.** The refutation is *indirect*: it derives a contradiction from computability, not from analysis. It yields no candidate algebra, no invariant, no moment sequence.

## 6. The Gap

Before 2020 the gap was §4 ($\mathcal{R}^\omega$-embeddability for all known classes) versus §1 (all separable $\mathrm{II}_1$ factors). That gap is now closed in the negative. The residual gaps are:

1. **Explicitness.** $\mathrm{MIP}^*=\mathrm{RE}$ proves $\exists M \not\hookrightarrow \mathcal{R}^\omega$ without naming one. Producing an explicit non-hyperlinear group, a concrete non-embeddable factor, or an explicit trace-positive polynomial that is not a limit of sums of squares plus commutators is open.
2. **Quantitative gap.** How large can $\omega^{qc}(G)-\omega^*(G)$ be as a function of game size? The known separation is $\ge$ any computable function of $|G|$ in the worst case, but no explicit game with a proven numerical gap is known. *(frontier — verify)*
3. **Localized versions.** Does CEP fail for factors with property (T)? For $L(\Gamma)$ with $\Gamma$ finitely presented? Is every sofic group a limit of amenable ones?

## 7. Current Research (as of June 2026)

- **Explicit counterexamples.** Groups from linear-system and low-degree games (Slofstra's solution groups, Paddock–Slofstra) are the main candidate source of an explicit non-hyperlinear group. No candidate has been certified. *(frontier — verify)*
- **Simplifying $\mathrm{MIP}^*=\mathrm{RE}$.** Vidick's almost-synchronous rounding theorem (*J. Math. Phys.* 2022) and de la Salle's stability/spectral-gap arguments replace parts of the original PCP machinery with representation-stability statements; a fully "operator-algebraic" proof of the refutation, avoiding compression, is a stated goal. *(frontier — verify)*
- **Model theory of tracial algebras.** Goldbring, Hart and Farah use continuous logic: the failure of CEP means $\mathcal{R}$ is not existentially closed and the universal theory of $\mathcal{R}$ is not the minimum. Work on enforceable factors, and on the number of universal theories of $\mathrm{II}_1$ factors (now known to be $2^{\aleph_0}$), is active.
- **Complexity refinements.** Mousavi–Nezhadi–Yuen locate the commuting-operator value in the arithmetical hierarchy ($\Pi_2$-completeness of the exact commuting value), sharpening how far $C_{qc}$ sits from $C_{qa}$.
- **Groups.** Institutions: IQC Waterloo, Caltech, UCSD, Copenhagen, ENS Lyon, Paris-Saclay, Illinois–Chicago, Vanderbilt.

## 8. Future Work

- Construct an explicit non-hyperlinear group, or prove all sofic-approximation obstructions are non-effective.
- Find a *finitary* invariant separating $C_{qa}$ from $C_{qc}$ — an analytic quantity computable from a game that certifies non-embeddability directly.
- Determine which structural CEP consequences survive: Blackadar–Kirchberg semiprojectivity questions, the Kaplansky and Aluthge-type conjectures proved *assuming* CEP must be revisited unconditionally.
- Classify universal theories of $\mathrm{II}_1$ factors; decide whether there is a maximum one.
- Extend to type III: does every von Neumann algebra with separable predual embed into an ultrapower of the Araki–Woods factor $\mathcal{R}_\infty$?

## 9. Key References

- **[Foundational]** A. Connes. *Classification of Injective Factors: Cases $\mathrm{II}_1$, $\mathrm{II}_\infty$, $\mathrm{III}_\lambda$, $\lambda \neq 1$.* Annals of Mathematics 104(1), 73–115, 1976.
- **[Foundational]** E. Kirchberg. *On non-semisplit extensions, tensor products and exactness of group C\*-algebras.* Inventiones Mathematicae 112, 449–489, 1993.
- **[SOTA / Recent]** Z. Ji, A. Natarajan, T. Vidick, J. Wright, H. Yuen. *MIP\* = RE.* arXiv:2001.04383, 2020; Communications of the ACM 64(11), 131–138, 2021.
- **[SOTA / Recent]** W. Slofstra. *The set of quantum correlations is not closed.* Forum of Mathematics, Pi 7, e1, 2019. [DOI](https://doi.org/10.1017/fmp.2018.3)
- **[SOTA / Recent]** T. Vidick. *Almost synchronous quantum correlations.* Journal of Mathematical Physics 63, 022201, 2022. [DOI](https://doi.org/10.1063/5.0056512)
- **[Survey]** I. Goldbring, B. Hart. *The Connes Embedding Problem: A Guided Tour.* Bulletin of the American Mathematical Society 59, 503–560, 2022. [DOI](https://doi.org/10.1090/bull/1768)
- **[Survey]** N. Ozawa. *About the Connes embedding conjecture: algebraic approaches.* Japanese Journal of Mathematics 8, 147–183, 2013.
- **[Survey]** N. P. Brown, N. Ozawa. *C\*-Algebras and Finite-Dimensional Approximations.* Graduate Studies in Mathematics 88, AMS, 2008. [DOI](https://doi.org/10.1090/gsm/088)
- **[Foundational]** M. Junge, M. Navascués, C. Palazuelos, D. Pérez-García, V. B. Scholz, R. F. Werner. *Connes' embedding problem and Tsirelson's problem.* Journal of Mathematical Physics 52, 012102, 2011. [DOI](https://doi.org/10.1063/1.3514538)
- **[Foundational]** T. Fritz. *Tsirelson's problem and Kirchberg's conjecture.* Reviews in Mathematical Physics 24, 1250012, 2012.
- **[Related]** U. Haagerup, S. Thorbjørnsen. *A new application of random matrices: $\mathrm{Ext}(C^*_{\mathrm{red}}(F_2))$ is not a group.* Annals of Mathematics 162, 711–775, 2005.

## 10. Worked Example / Concrete Special Case

**Claim.** $L(\mathbb{F}_2) \hookrightarrow \mathcal{R}^\omega$, with microstates built from permutation matrices.

The trace on the group von Neumann algebra $L(\Gamma)$ is $\tau(u_g) = \delta_{g,e}$. For $\Gamma = \mathbb{F}_2 = \langle a,b\rangle$ every nontrivial reduced word $w$ therefore has $\tau(u_w) = 0$.

*Construction.* Fix a finite set $W$ of nontrivial reduced words, say all words of length $\le 4$. Since $\mathbb{F}_2$ is residually finite, there is a finite group $G$ and a homomorphism $\pi : \mathbb{F}_2 \to G$ with $\pi(w) \neq e$ for all $w \in W$. Let $\lambda : G \to M_{|G|}(\mathbb{C})$ be the left regular representation, so $\lambda(g)$ is the permutation matrix of $h \mapsto gh$. Set $A = \lambda(\pi(a))$, $B = \lambda(\pi(b))$ — unitaries in $M_n(\mathbb{C})$, $n = |G|$.

*Trace computation.* For a permutation matrix, $\mathrm{tr}_n(\lambda(g)) = \frac{\\#\{h \in G: gh = h\}}{|G|}$. Left translation by $g \neq e$ has no fixed point, so
$$\mathrm{tr}_n(\lambda(g)) = \begin{cases} 1, & g = e,\\ 0, & g \neq e.\end{cases}$$
Hence for every $w \in W$: $\mathrm{tr}_n\big(w(A,B)\big) = \mathrm{tr}_n\big(\lambda(\pi(w))\big) = 0 = \tau(u_w)$ — an *exact*, not approximate, match on $W$.

*Explicit instance.* Take $G = S_3$, $\pi(a) = (1\,2)$, $\pi(b) = (1\,2\,3)$, $n = 6$. Then
$$\pi(aba^{-1}b^{-1}) = (1\,2)(1\,2\,3)(1\,2)(1\,3\,2) = (1\,3\,2)(1\,3\,2) = (1\,2\,3) \neq e,$$
so $\mathrm{tr}_6\big(ABA^{-1}B^{-1}\big) = 0 = \tau(u_{[a,b]})$, correctly reflecting that $[a,b] \neq e$ in $\mathbb{F}_2$. (Words that *do* die in $S_3$, e.g. $b^3$, are excluded by choosing a larger quotient; $\mathbb{F}_2$ surjects onto $S_k$ for all $k$, and one takes $k$ large enough for $W$.)

Letting $W$ exhaust all words and taking the sequence of matrix algebras $M_{n_d}(\mathbb{C}) \subseteq \mathcal{R}$, the map $u_a \mapsto [(A_d)]$, $u_b \mapsto [(B_d)]$ defines a trace-preserving embedding $L(\mathbb{F}_2) \hookrightarrow \mathcal{R}^\omega$.

**What breaks in general.** This argument uses residual finiteness — a *combinatorial* certificate that finite models exist. $\mathrm{MIP}^*=\mathrm{RE}$ shows there is no such certificate in general: the map from a finitely presented tracial structure to "does a finite-dimensional approximation exist" is not computable, so no uniform microstate construction of the above kind can cover all $\mathrm{II}_1$ factors.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*