---
id: 01-number-theory/batyrev-manin-conjecture
title: "Batyrev-Manin Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Batyrev-Manin Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/batyrev-manin-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Batyrev-Manin conjecture (frequently referred to as Manin's conjecture) dictates the asymptotic distribution of rational points of bounded height on Fano varieties. 

Let $X$ be a smooth projective Fano variety defined over a number field $K$. Let $H_{-K_X} : X(K) \to \mathbb{R}_{\geq 0}$ be an exponential height function associated with the anticanonical divisor $-K_X$. Let $U \subseteq X$ be a sufficiently small, non-empty Zariski open subset, or more generally, let $Z \subset X(K)$ be a specifically chosen thin set, and consider the rational points $U(K) = X(K) \setminus Z$. 

The counting function for rational points of bounded height is:
$$ N_{U, H_{-K_X}}(B) = \\# \{ x \in U(K) \mid H_{-K_X}(x) \leq B \} $$

The conjecture states that there exists a thin set $Z$ such that, as $B \to \infty$, the counting function exhibits the asymptotic growth:
$$ N_{U, H_{-K_X}}(B) \sim c(X, H_{-K_X}) B (\log B)^{\rho(X) - 1} $$
where:
1. $\rho(X)$ is the Picard rank of the variety $X$.
2. $c(X, H_{-K_X}) > 0$ is a structural constant (formalized by Emmanuel Peyre) consisting of an arithmetic factor (Tamagawa volumes reflecting local densities) and a geometric factor (associated with the Brauer group and the effective cone of $X$).

## 2. Mathematical Foundations

- **Fano Varieties:** A smooth projective algebraic variety $X$ is defined as Fano if its anticanonical divisor $-K_X$ (or equivalently, the anticanonical line bundle $\omega_X^{-1}$) is an ample divisor. 
- **Weil Height Function:** A height function $H_D: X(K) \to \mathbb{R}_{\geq 0}$ measures the arithmetic complexity of a rational point relative to a divisor $D$. For a point $x \in \mathbb{P}^n(\mathbb{Q})$ represented by coprime integers $(x_0, \dots, x_n)$, the standard naive height is $H(x) = \max(|x_0|, \dots, |x_n|)$. By Northcott's theorem, heights associated with ample divisors guarantee that the set $\{ x \in X(K) \mid H_{-K_X}(x) \leq B \}$ is finite.
- **Picard Group and Rank:** The Picard group $\operatorname{Pic}(X)$ is the group of isomorphism classes of line bundles on $X$. For a Fano variety, $\operatorname{Pic}(X)$ is a finitely generated free abelian group. Its rank, $\rho(X) = \operatorname{rank}(\operatorname{Pic}(X))$, determines the exponent of the logarithmic factor in the asymptotic formula.
- **Thin Sets:** A subset $Z \subset X(K)$ is called a *thin set* if it is contained within a finite union $Z \subset \bigcup_i Y_i(K) \cup \bigcup_j \pi_j(W_j(K))$, where $Y_i \subsetneq X$ are proper closed subvarieties, and $\pi_j: W_j \to X$ are generically finite dominant morphisms of degree $\geq 2$. Excluding thin sets is crucial to filter out "accumulating subvarieties" (such as lines with disproportionately dense rational points) that would otherwise skew the baseline growth rate.

## 3. History & State of the Art (SOTA)

- **Original Formulation (1989):** The conjecture was first proposed by Yu. I. Manin, J. Franke, and Y. Tschinkel. They successfully proved it for flag varieties $P \backslash G$ using harmonic analysis and Langlands spectral decomposition.
- **Batyrev and Manin (1990):** Extended the conjecture beyond flag varieties to general Fano varieties.
- **Peyre's Constant (1995):** Emmanuel Peyre formulated a precise, conjectural description of the leading coefficient $c(X, H_{-K_X})$. He defined it as a volume computed with a Tamagawa measure on the adelic space $X(\mathbb{A}_K)$, corrected by the Brauer group $\operatorname{Br}(X)$.
- **Counterexamples to the Zariski-closed Condition (1996):** Victor Batyrev and Yuri Tschinkel discovered explicit Fano varieties (specific cubic bundles over $\mathbb{P}^1$) where rational points accumulate overwhelmingly on covers, rather than proper subvarieties. This proved that removing a Zariski-closed subset was insufficient, necessitating the refined requirement to remove *thin sets*.
- **Geometric Manin's Conjecture (2010s–present):** Researchers have recently translated the arithmetic conjecture over number fields to a geometric analogue over function fields $\mathbb{F}_q(t)$ or $\mathbb{C}(t)$. This approach re-frames the problem into studying the homological stability of moduli spaces of rational curves of bounded degree on Fano varieties.

## 4. Partial Results / Verified Cases

The conjecture has been proven for several highly symmetric and specific low-dimensional classes of Fano varieties, but remains widely open in the general case. Verified instances include:
- **Projective Spaces ($\mathbb{P}^n$):** Easily resolved using the classical geometry of numbers (Schanuel's Theorem, 1979).
- **Flag Varieties:** Proven by Franke, Manin, and Tschinkel (1989) using the theory of automorphic forms.
- **Toric Varieties:** Proven by Batyrev and Tschinkel (1998) for split toric varieties using harmonic analysis and Poisson summation on adele groups. Extended by Salberger (1998) to non-split toric varieties.
- **Equivariant Compactifications:** Proven for equivariant compactifications of linear algebraic groups (Chambert-Loir and Tschinkel, 2012).
- **Del Pezzo Surfaces (Dimension 2):** 
  - Degree $\geq 6$: Fully resolved (Derenthal, 2007).
  - Degree $5$: Proven by de la Bretèche (2001).
  - Degree $4$: Proven by de la Bretèche, Browning, and Derenthal (2007) via the method of universal torsors.
  - Degree $3$ (Cubic Surfaces): Solved *only* for specific singular cubic surfaces or surfaces possessing highly specific line configurations (e.g., Heath-Brown, 1998). The general smooth cubic surface remains fundamentally unsolved.

## 5. Principal Obstacles

- **Absence of Symmetries:** The vast majority of Fano varieties (e.g., general smooth cubic surfaces in $\mathbb{P}^3$ or general quartic threefolds) lack a continuous group action. Thus, powerful tools like the Langlands program or harmonic analysis on adelic groups—which unlocked the conjecture for flag and toric varieties—are entirely inapplicable.
- **Identifying the Accumulating Thin Set:** There is currently no known a priori algorithm to geometrically identify the precise accumulating thin set $Z$ that must be removed for a generic Fano variety. Understanding mathematically why certain covers collect an anomalous density of rational points remains highly opaque.
- **Limitations of the Circle Method:** The Hardy-Littlewood circle method (and its modern variants, such as the Delta method) handles Diophantine equations effectively when the number of variables is significantly larger than the degree. However, for a general Fano variety, the dimension is often too small relative to the algebraic degree for these analytic methods to converge.

## 6. The Gap

The central frontier lies between varieties that admit an embedding into a highly structured space with large symmetries (where analytic number theory and representation theory succeed) and structurally "generic" varieties (where point counting behaves quasi-randomly but is governed by deep geometric invariants). Bridging this gap requires the development of fundamentally new non-abelian Diophantine counting methods or systematic frameworks to break general Fano varieties into fibrations of analytically tractable varieties (leveraging the Minimal Model Program).

## 7. Current Research (as of June 2026)

- **Universal Torsors and Descent:** Researchers continue to expand the descent method, lifting the counting problem from $X$ to its universal torsor $\mathcal{T}_X$ (a higher-dimensional variety with simpler geometry). This structurally converts a problem of rational points into a problem of integral points on an affine variety.
- **Minimal Model Program (MMP) in Arithmetic:** A major active direction led by Lehmann, Sengupta, Tanimoto, and others leverages the MMP to theoretically predict the geometry of accumulating subvarieties using movable cones and pseudo-effective cones of divisors.
- **Function Field Analogues:** Extensive work is being done on the Geometric Manin's Conjecture over $\mathbb{C}(t)$ by studying the homological stability of the moduli spaces of rational curves on Fano varieties. *(frontier — verify)*
- **Fibrations:** Applying sieve methods and the circle method to Fano varieties structured as conic bundles or Del Pezzo fibrations over computationally simpler base spaces like $\mathbb{P}^1$.

## 8. Future Work

Leading mathematicians have proposed the following open pathways:
- **General Smooth Cubic Surfaces:** Proving Manin's Conjecture for a general non-singular cubic surface in $\mathbb{P}^3$. This is considered the holy grail of the field and the most critical immediate testing ground for novel methods.
- **Refining the Topological Exceptional Set:** Formulating an exact, computationally verifiable geometric criterion for determining the necessary thin set $Z$ for *any* given Fano variety.
- **Brauer-Manin Obstructions:** Unifying the study of asymptotic point counts with the theory of Brauer-Manin obstructions to the Hasse principle and weak approximation to better predict leading coefficients.

## 9. Key References

- **[Foundational]** Franke, J., Manin, Y. I., & Tschinkel, Y. *Rational points of bounded height on Fano varieties.* Inventiones mathematicae, 1989.
- **[Foundational]** Batyrev, V. V., & Manin, Y. I. *Sur le nombre des points rationnels de hauteur borné des variétés algébriques.* Mathematische Annalen, 1990.
- **[Foundational]** Peyre, E. *Hauteurs et nombres de Tamagawa sur les variétés de Fano.* Duke Mathematical Journal, 1995.
- **[Foundational]** Batyrev, V. V., & Tschinkel, Y. *Rational points on some Fano cubic bundles.* Comptes Rendus de l'Académie des Sciences, Série I, 1996.
- **[SOTA / Recent]** Lehmann, B., Sengupta, A., & Tanimoto, S. *Geometric properties of exceptional sets in Manin's conjecture.* Duke Mathematical Journal, 2018.
- **[Survey]** Browning, T. D. *Quantitative Arithmetic of Projective Varieties.* Progress in Mathematics, Vol. 277. Birkhäuser, 2009.

## 10. Worked Example / Concrete Special Case

Consider the simplest Fano variety over $\mathbb{Q}$: the projective line $X = \mathbb{P}^1$. 
- The anticanonical divisor is $-K_{\mathbb{P}^1} \cong \mathcal{O}(2)$. 
- The Picard rank is $\rho(\mathbb{P}^1) = 1$.
- Consequently, the conjecture's predicted growth rate is $c \cdot B \cdot (\log B)^{1-1} = c \cdot B$.

Let us verify this mathematically. The height associated to $\mathcal{O}(1)$ is the standard Weil height: for $x = [x_0 : x_1] \in \mathbb{P}^1(\mathbb{Q})$ represented by coprime integers, $H(x) = \max(|x_0|, |x_1|)$.
The height associated to the anticanonical divisor $-K_X$ is therefore $H_{-K}(x) = H(x)^2$.

We wish to count the number of rational points with $H_{-K}(x) \leq B$, which is strictly equivalent to counting coprime integer pairs $(x_0, x_1)$ such that $\max(|x_0|, |x_1|) \leq B^{1/2}$.

Let $T = B^{1/2}$. The number of integer points inside the square $[-T, T]^2$ is approximately $(2T)^2 = 4T^2 = 4B$.
However, to uniquely identify rational points, we must exclusively count *coprime* pairs. The natural density (probability) that two randomly chosen integers are coprime is well-known to be $\frac{1}{\zeta(2)} = \frac{6}{\pi^2}$.
Thus, the asymptotic number of rational points of bounded height is evaluated as:
$$ N_{\mathbb{P}^1, H_{-K}}(B) \sim \frac{6}{\pi^2} (4T^2) = \frac{24}{\pi^2} T^2 = \frac{24}{\pi^2} B $$

This rigorous result perfectly aligns with the Manin Conjecture's prediction of linear growth $c \cdot B$ (where the coefficient is explicitly $c = \frac{24}{\pi^2}$), and notably, no thin set extraction is required for this foundational base case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*