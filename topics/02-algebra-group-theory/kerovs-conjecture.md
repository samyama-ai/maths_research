---
id: 02-algebra-group-theory/kerovs-conjecture
title: "Kerov's Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kerov's Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kerovs-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Kerov observed (mid-1990s, unpublished lectures) that the normalized irreducible characters of the symmetric groups $S_n$, evaluated on a fixed cycle type and viewed as functions of the Young diagram $\lambda$, are **universal polynomials in the free cumulants** $R_2(\lambda), R_3(\lambda),\dots$ of the transition measure of $\lambda$. His **positivity conjecture** states:

> For every $k \ge 1$, the Kerov polynomial $K_k$ with $\Sigma_k = K_k(R_2, R_3, \dots)$ has **nonnegative integer** coefficients.

This classical statement is a **theorem** (Féray 2009; explicit combinatorics by Dołęga–Féray–Śniady 2010). What remains open, and is the live content of the entry, is the **Kerov–Lassalle conjecture**: the same positivity for the one-parameter Jack deformation. For Jack parameter $\alpha>0$ and $\gamma := -\big(\sqrt{\alpha}-\tfrac{1}{\sqrt{\alpha}}\big)$ (Lassalle's convention; sources differ by a sign), the Jack character $\Sigma^{(\alpha)}_k$ is a polynomial in $R_2,R_3,\dots$ with coefficients in $\mathbb{Q}[\gamma]$, and the conjecture asserts these coefficients lie in $\mathbb{N}[\gamma]$ — nonnegative integer coefficients in the free cumulants **and** in $\gamma$. Setting $\alpha=1$ ($\gamma=0$) recovers Kerov's original statement.

A complete resolution requires either a combinatorial model counting objects weighted by $\gamma$ whose generating function is $\Sigma^{(\alpha)}_k$, or a proof of nonnegativity by other means; a disproof requires one explicit $k$ and one monomial with a negative coefficient.

## 2. Mathematical Foundations

**Normalized characters.** For a partition $\mu \vdash k$ and $\lambda \vdash n$ with $n \ge k$,
$$\Sigma_\mu(\lambda) \;=\; n^{\downarrow k}\,\frac{\chi^\lambda\!\left(\mu \cup 1^{n-k}\right)}{\dim \lambda},\qquad n^{\downarrow k}=n(n-1)\cdots(n-k+1),$$
with $\Sigma_k := \Sigma_{(k)}$. The key point is that $\Sigma_\mu$ is a well-defined function on the set of **all** Young diagrams, independent of $n$ — an element of the algebra of *polynomial functions on Young diagrams* $\Lambda^\star$ (Kerov–Olshanski).

**Transition measure and free cumulants.** Draw $\lambda$ in Russian convention; let $x_1<\dots<x_{d}$ be its inner corner contents and $y_1<\dots<y_{d+1}$ its outer corner contents (interlacing). The **transition measure** is
$$\mu_\lambda \;=\; \sum_{i} \frac{\prod_{j}(y_i-x_j)}{\prod_{j\neq i}(y_i-y_j)}\;\delta_{y_i},$$
a probability measure with mean $0$ whose Cauchy transform $G_{\mu_\lambda}(z)=\int \frac{d\mu_\lambda(t)}{z-t}$ has the product form $\prod_j (z-x_j)/\prod_i(z-y_i)$. Its **free cumulants** $R_k(\lambda)$ are the coefficients in the inverse (R-transform) expansion
$$G^{-1}(w)=\frac1w+\sum_{k\ge 2}R_k\,w^{k-1}.$$
Here $R_1=0$, $R_2(\lambda)=|\lambda|=n$, and low moment–cumulant relations read $m_2=R_2$, $m_3=R_3$, $m_4=R_4+2R_2^2$.

**Kerov polynomials.** With the gradation $\deg R_k = k$, Biane's theorem gives $\Sigma_k = K_k(R_2,\dots,R_{k+1})$ with $K_k$ having integer coefficients and top term $R_{k+1}$. The first cases:
$$\Sigma_1=R_2,\quad \Sigma_2=R_3,\quad \Sigma_3=R_4+R_2,\quad \Sigma_4=R_5+5R_3,$$
$$\Sigma_5=R_6+15R_4+5R_2^2+8R_2,\qquad \Sigma_6=R_7+35R_5+35R_3R_2+84R_3 .$$

**Jack deformation.** Jack symmetric functions $J^{(\alpha)}_\lambda$ interpolate Schur ($\alpha=1$), zonal ($\alpha=2$), and zonal spherical functions of $GL_n(\mathbb{H})$ ($\alpha=1/2$). Jack characters $\theta^{(\alpha)}_\mu(\lambda)$ are the coefficients of the power-sum expansion of $J^{(\alpha)}_\lambda$, normalized to $\Sigma^{(\alpha)}_\mu$ by the analogue of the formula above with the anisotropic diagram scaled by $\sqrt{\alpha}$. Lassalle's first cases:
$$\Sigma^{(\alpha)}_2=R_3+\gamma R_2,\qquad \Sigma^{(\alpha)}_3=R_4+3\gamma R_3+\left(1+2\gamma^2\right)R_2 .$$

## 3. History & State of the Art (SOTA)

- **1993–1998.** Kerov and Biane develop the free-probability picture: Biane, *Representations of symmetric groups and free probability* (Adv. Math. 138, 1998) proves that characters of large-$n$ symmetric groups are governed by free cumulants.
- **c. 1998–2000.** Kerov announces the polynomiality $\Sigma_k = K_k(R_\bullet)$ in an IHP talk and conjectures nonnegativity of coefficients. Biane (LNM 1815, 2003) supplies the first published proof of polynomiality with integer coefficients and computes $K_k$ for $k\le 9$.
- **2004–2007.** Goulden–Rattan (Trans. AMS 359, 2007) give an explicit — but sign-alternating — formula for $K_k$ via a three-operator calculus, and prove positivity of the subleading coefficients.
- **2006–2008.** Śniady's genus-expansion approach and Rattan–Śniady's bounds for balanced diagrams reduce the conjecture to a combinatorial count of maps/factorizations.
- **2009.** Féray proves Kerov positivity, via Stanley's formula for characters on multi-rectangular diagrams; the coefficients are cardinalities of sets of factorizations.
- **2010.** Dołęga–Féray–Śniady give the explicit combinatorial interpretation: the coefficient of $R_{s_2+1}R_{s_3+1}\cdots$ in $K_k$ counts factorizations of the $k$-cycle $\sigma_1\sigma_2=(1\,2\,\cdots\,k)$ with prescribed constraints on the cycle structure.
- **2009 →.** Lassalle (Adv. Math. 222, 2009) sets up Jack analogues and formulates the open positivity conjecture in $\mathbb{N}[\gamma]$, verifying it by computer for small $k$.
- **2016–2019.** Dołęga–Féray (Duke Math. J. 165, 2016) prove **polynomiality** of Jack Kerov coefficients in $\gamma$ (the structural half of Lassalle's conjecture); Śniady determines the top-degree part combinatorially via maps on non-orientable surfaces.

## 4. Partial Results / Verified Cases

- **$\alpha = 1$ (Schur / symmetric groups): fully proved.** Positivity for all $k$ (Féray 2009); explicit combinatorial model for all $\mu$, not just single cycles (Dołęga–Féray–Śniady 2010).
- **Polynomiality in $\gamma$ for all $\alpha$:** proved (Dołęga–Féray 2016). The coefficient of each monomial $R_{s_2+1}R_{s_3+1}\cdots$ in $\Sigma^{(\alpha)}_k$ is a polynomial in $\gamma$ of degree at most $k+1-\sum s_i$, with rational — conjecturally nonnegative integer — coefficients.
- **Top-degree and subleading coefficients:** the coefficient of $R_{k+1}$ is $1$; the $\gamma$-linear coefficient of $R_k$ is $\binom{k}{2}$ (Lassalle). Śniady's *Asymptotics of Jack characters* (JCTA 166, 2019) identifies the top-degree part in $\gamma$ with a count of (possibly non-orientable) maps, giving positivity for that layer.
- **Computer verification:** Lassalle verified the conjecture for $k \le 9$ and reported tables; subsequent computations by Dołęga and Féray extend the check into the range $k \le 12$–$13$ *(frontier — verify exact upper limit)*.
- **$\alpha = 2$ (zonal polynomials / Gelfand pair $(S_{2n}, H_n)$):** the corresponding zonal Kerov polynomials have a combinatorial interpretation by pairs of matchings, and positivity is known at $\alpha=2$ for the same range as the general check plus the top-degree stratum.

## 5. Principal Obstacles

- **Every known exact formula is sign-alternating.** Goulden–Rattan's operator formula, Lassalle's explicit expansions, and the Jack analogues of Stanley's polynomial all produce the coefficients as alternating sums. Establishing positivity from such formulas requires a cancellation-free reindexing — precisely the missing step.
- **Loss of orientability.** The $\alpha=1$ proof runs through maps on **orientable** surfaces, where the underlying algebra is the group algebra of $S_n$ and factorizations of a cycle are literally group-theoretic objects. For $\alpha\ne 1$ the parameter $\gamma$ measures non-orientability; the natural objects are maps on general (possibly non-orientable) surfaces, for which no algebra of Frobenius type is known, so induction on the number of handles has no analogue.
- **No character-theoretic interpretation.** For generic $\alpha$, $\Sigma^{(\alpha)}_\mu$ is not the character of any group or algebra, only for $\alpha \in \{1/2,1,2\}$ is there a Gelfand-pair interpretation. Standard representation-theoretic tools (Frobenius formula, induction/restriction, Murnaghan–Nakayama) simply do not exist for generic $\alpha$.
- **Stanley's formula fails to deform.** Féray's proof uses the multi-rectangular coordinate expansion of $\Sigma_\mu$, in which positivity is manifest after a sign flip. The Jack analogue (the *$b$-conjecture* of Goulden–Jackson) is itself open, so the deformation of the proof's engine is at least as hard as the target.
- **Asymptotic methods give the wrong resolution.** Free-probabilistic and concentration estimates control leading-order behaviour of characters for large diagrams, but positivity is an exact statement about individual integer coefficients; asymptotics cannot see a single negative low-order term.

## 6. The Gap

Proved: (i) $\Sigma^{(\alpha)}_k$ is a polynomial in $R_2,R_3,\dots$ with coefficients in $\mathbb{Q}[\gamma]$; (ii) the top-degree-in-$\gamma$ layer is a count of maps, hence nonnegative; (iii) the whole statement at $\gamma=0$.

Missing: nonnegativity of the **intermediate** $\gamma$-degrees for general $k$. Concretely, the gap is the absence of a set $\mathcal{F}_{k;\mathbf{s}}$ of combinatorial objects, graded by a non-orientability statistic $\eta$, with
$$[\,R_{s_2+1}R_{s_3+1}\cdots\,]\;\Sigma^{(\alpha)}_k \;=\; \sum_{f\in \mathcal{F}_{k;\mathbf{s}}}\gamma^{\eta(f)} .$$
At $\gamma=0$ this must specialize to the DFŚ factorization count. Finding $\eta$ — an integer statistic on non-orientable maps that both refines the DFŚ model and cancels the alternating signs — is the single step to be crossed.

## 7. Current Research (as of June 2026)

- **Dołęga (IMPAN Warsaw) and Féray (CNRS / IECL Nancy)** continue the "structure constants of Jack characters" program: proving polynomiality and positivity statements about products $\Sigma^{(\alpha)}_\mu \Sigma^{(\alpha)}_\nu$ as a route to the coefficient positivity.
- **Śniady (IMPAN)** pursues the maps-on-surfaces model, with the measure of non-orientability as the candidate statistic $\eta$; partial results cover the top two $\gamma$-degrees *(frontier — verify current depth)*.
- **Chapuy, Dołęga and collaborators** connect the problem to the $b$-deformed Goulden–Jackson matching–Jack conjecture and to $b$-deformed KP/BKP hierarchies; the tau-function viewpoint produces new polynomiality proofs and is currently the most active technique *(frontier — verify)*.
- **Ben Dali (Nancy / Warsaw)** has developed positivity results for Jack cumulants and for the "$b$-positivity" of certain Jack expansions, which specialize to new families of Kerov–Lassalle coefficients *(frontier — verify scope)*.
- Computational work extends verification tables and searches for a counterexample at moderate $k$; none has surfaced.

## 8. Future Work

- Construct the graded combinatorial model $(\mathcal{F},\eta)$ directly, starting from the known $\gamma$-linear coefficients and building downward from top degree.
- Prove the $b$-conjecture for the Jack analogue of Stanley's multi-rectangular formula; Kerov–Lassalle positivity would follow by the deformed version of Féray's argument.
- Exploit the $b$-deformed BKP hierarchy: if the Jack character generating function is a tau function with manifestly positive Plücker-type coefficients, positivity becomes a corollary.
- Settle the special values $\alpha=2$ and $\alpha=1/2$ in full generality using the Gelfand pairs $(S_{2n},H_n)$ and $(GL_n(\mathbb{H}),U_n(\mathbb{H}))$, then interpolate.
- Determine whether the coefficients admit a representation-theoretic meaning as dimensions in some yet-undiscovered $\alpha$-deformed algebra.

## 9. Key References

- **[Foundational]** Biane, P. *Representations of symmetric groups and free probability.* Advances in Mathematics 138 (1998), 126–181.
- **[Foundational]** Biane, P. *Characters of symmetric groups and free cumulants.* In: Asymptotic Combinatorics with Applications to Mathematical Physics, Lecture Notes in Mathematics 1815, Springer, 2003, 185–200.
- **[Foundational]** Kerov, S. V. *Asymptotic Representation Theory of the Symmetric Group and its Applications in Analysis.* Translations of Mathematical Monographs 219, American Mathematical Society, 2003.
- **[Foundational]** Kerov, S. V. *Anisotropic Young diagrams and symmetric functions.* Functional Analysis and Its Applications 34 (2000), 41–51.
- **[SOTA]** Féray, V. *Combinatorial interpretation and positivity of Kerov's character polynomials.* Journal of Algebraic Combinatorics 29 (2009), 473–507.
- **[SOTA]** Dołęga, M., Féray, V., Śniady, P. *Explicit combinatorial interpretation of Kerov character polynomials as numbers of permutation factorizations.* Advances in Mathematics 225 (2010), 81–120.
- **[SOTA]** Lassalle, M. *Jack polynomials and free cumulants.* Advances in Mathematics 222 (2009), 2227–2269.
- **[SOTA / Recent]** Dołęga, M., Féray, V. *Gaussian fluctuations of Young diagrams and structure constants of Jack characters.* Duke Mathematical Journal 165 (2016), 1193–1282.
- **[SOTA / Recent]** Dołęga, M., Féray, V. *Cumulants of Jack symmetric functions and the $b$-conjecture.* Transactions of the American Mathematical Society 369 (2017), 9015–9060.
- **[SOTA / Recent]** Śniady, P. *Asymptotics of Jack characters.* Journal of Combinatorial Theory, Series A 166 (2019), 91–143.
- **[Related]** Goulden, I. P., Rattan, A. *An explicit form for Kerov's character polynomials: three operators approach.* Transactions of the American Mathematical Society 359 (2007), 3669–3685.
- **[Related]** Rattan, A., Śniady, P. *Upper bound on the characters of the symmetric groups for balanced Young diagrams and a generalized Frobenius formula.* Advances in Mathematics 218 (2008), 673–695.
- **[Survey]** Féray, V., Śniady, P. *Asymptotics of characters of symmetric groups related to Stanley character formula.* Annals of Mathematics 173 (2011), 887–906.

## 10. Worked Example / Concrete Special Case

**Verify $\Sigma_3 = R_4 + R_2$ on $\lambda = (3)$, $n=3$.**

*Left side.* $\lambda=(3)$ carries the trivial character, $\chi^{(3)}\equiv 1$, $\dim\lambda=1$. Hence
$$\Sigma_3(\lambda)=3^{\downarrow 3}\cdot\frac{\chi^{(3)}\big((3)\big)}{1}=3\cdot 2\cdot 1=6 .$$

*Right side, computed independently from the transition measure.* Boxes can be added to $(3)$ at cell $(1,4)$, content $+3$, and at $(2,1)$, content $-1$; so the outer corners are $y=\{-1,3\}$. The single inner corner is the box $(1,3)$, content $+2$, so $x=\{2\}$. Then
$$\mu_{-1}=\frac{-1-2}{-1-3}=\frac34,\qquad \mu_{3}=\frac{3-2}{3-(-1)}=\frac14,$$
giving $\mu_\lambda=\tfrac34\delta_{-1}+\tfrac14\delta_{3}$. Its moments:
$$m_1=-\tfrac34+\tfrac34=0,\quad m_2=\tfrac34+\tfrac{9}{4}=3,\quad m_3=-\tfrac34+\tfrac{27}{4}=6,\quad m_4=\tfrac34+\tfrac{81}{4}=21 .$$
With $R_1=m_1=0$, the free moment–cumulant relations give
$$R_2=m_2=3\;(=|\lambda|\ \checkmark),\qquad R_3=m_3=6,\qquad R_4=m_4-2R_2^2=21-18=3 .$$
Therefore $R_4+R_2=3+3=6=\Sigma_3(\lambda)$. ✓ (Likewise $\Sigma_2=R_3=6=3^{\downarrow 2}$.)

**Where the open problem enters.** Deform to Jack. Lassalle's second polynomial reads
$$\Sigma^{(\alpha)}_3=R_4+3\gamma R_3+\big(1+2\gamma^2\big)R_2 ,$$
so the coefficient list is $(1;\,3\gamma;\,1+2\gamma^2)$ — every coefficient of every power of $\gamma$ is a nonnegative integer, and setting $\gamma=0$ returns $R_4+R_2$, the identity just verified. Kerov–Lassalle asserts this pattern for all $k$: e.g. the $\gamma$-linear coefficient of $R_k$ in $\Sigma^{(\alpha)}_k$ is $\binom{k}{2}$ ($=3$ at $k=3$). What is missing is any objects being counted by, say, the $2$ in $2\gamma^2$ — a family of non-orientable maps with non-orientability degree $2$ — uniformly in $k$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*