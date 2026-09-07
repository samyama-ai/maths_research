---
id: 02-algebra-group-theory/demaillys-conjecture
title: "Demailly's Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

id: 02-algebra-group-theory/demaillys-conjecture
title: "Demailly's Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
```

# Demailly's Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/demaillys-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

*(Note: This page covers Demailly's Conjecture on Waldschmidt constants in commutative algebra and algebraic geometry. It is distinct from the Green-Griffiths-Demailly conjecture on jet differentials.)*

Demailly's Conjecture postulates a precise algebraic lower bound on the asymptotic growth rate of the initial degrees of symbolic powers of homogeneous ideals defining finite sets of points in projective space. 

Let $k$ be an algebraically closed field of characteristic zero. Let $R = k[x_0, x_1, \ldots, x_N]$ be the standard graded polynomial ring, and let $I \subset R$ be a homogeneous ideal defining a finite set of points in the projective space $\mathbb{P}^N_k$. 

Let the *initial degree* $\alpha(I)$ be the minimum degree of a non-zero homogeneous polynomial in $I$. Let $I^{(m)}$ denote the $m$-th symbolic power of $I$. The *Waldschmidt constant* of $I$ is the asymptotic ratio:
$$ \widehat{\alpha}(I) = \lim_{m \to \infty} \frac{\alpha(I^{(m)})}{m} = \inf_{m \ge 1} \frac{\alpha(I^{(m)})}{m} $$

**Demailly's Conjecture (1982):** For any ideal $I$ defining a finite set of points in $\mathbb{P}^N$ and for all integers $m \ge 1$, the Waldschmidt constant is bounded below by:
$$ \widehat{\alpha}(I) \ge \frac{\alpha(I^{(m)}) + N - 1}{m + N - 1} $$

When $m = 1$, this inequality specializes to **Chudnovsky's Conjecture** (1981):
$$ \widehat{\alpha}(I) \ge \frac{\alpha(I) + N - 1}{N} $$
Demailly's Conjecture claims that this geometric shift of $+N-1$ holds universally across all finite symbolic powers. A complete proof requires establishing a systematic containment or bounding methodology that perfectly tracks the base locus of the linear systems $|I^{(m)}|$ without yielding solely to asymptotic multiplier ideal subadditivity.

## 2. Mathematical Foundations

The conjecture bridges commutative algebra and complex analysis, relying heavily on the asymptotic behavior of ideal containment. 

**Standard Grading and Initial Degree:**
The polynomial ring $R = \bigoplus_{d \ge 0} R_d$ is standard graded. The initial degree is formally defined as:
$$ \alpha(I) = \min \{ d \in \mathbb{N} \mid I_d \neq 0 \} $$
Geometrically, $\alpha(I)$ is the lowest degree of a hypersurface passing through the scheme defined by $I$.

**Symbolic Powers:**
For a homogeneous ideal $I \subset R$ with minimal primary decomposition $I = \mathfrak{q}_1 \cap \dots \cap \mathfrak{q}_s$ where $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$ are the associated primes, the $m$-th symbolic power is defined as:
$$ I^{(m)} = \bigcap_{\mathfrak{p}_i \in \text{Ass}(R/I)} (I^m R_{\mathfrak{p}_i} \cap R) $$
When $I$ is a radical ideal defining a finite set of points $X = \{p_1, \dots, p_s\}$, the $m$-th symbolic power consists of all polynomials vanishing to order at least $m$ at each point $p_i \in X$:
$$ I^{(m)} = \bigcap_{i=1}^s \mathfrak{m}_{p_i}^m $$
where $\mathfrak{m}_{p_i}$ is the homogeneous maximal ideal corresponding to $p_i$.

**Fekete's Lemma and the Waldschmidt Constant:**
Because the valuation of polynomials at a point behaves additively under multiplication, we have the subadditive relation:
$$ \alpha(I^{(a+b)}) \le \alpha(I^{(a)}) + \alpha(I^{(b)}) \quad \text{for all } a,b \ge 1 $$
By Fekete's Lemma for subadditive sequences, the limit defining the Waldschmidt constant $\widehat{\alpha}(I) = \lim_{m \to \infty} \frac{\alpha(I^{(m)})}{m}$ exists and is equal to the infimum over all $m$.

**Multiplier Ideals (The Algebraic Translation):**
In modern characteristic zero approaches, bounding $\widehat{\alpha}(I)$ is done via the asymptotic multiplier ideal $\mathcal{J}(||I^c||)$. Ein, Lazarsfeld, and Smith (2001) famously proved that for an ideal $I$ in a regular local ring whose associated primes have codimension at most $h$:
$$ I^{(hm)} \subseteq I^m \quad \text{for all } m \ge 1 $$
For points in $\mathbb{P}^N$, $h = N$, meaning $I^{(Nm)} \subseteq I^m \subseteq I$. Taking initial degrees, $\alpha(I^{(Nm)}) \ge m \alpha(I)$, which implies $\widehat{\alpha}(I) \ge \frac{\alpha(I)}{N}$. Demailly's and Chudnovsky's bounds are significantly sharper than this due to the additive $+N-1$ terms in the numerator and denominator.

## 3. History & State of the Art (SOTA)

The history of the problem is rooted in transcendental number theory. 

- **1977:** Michel Waldschmidt introduced $\widehat{\alpha}(I)$ while studying the Schwarz Lemma in several complex variables to control the degrees of polynomials vanishing on subsets of $\mathbb{C}^N$.
- **1981:** Gregory Chudnovsky formulated his eponymous conjecture ($\widehat{\alpha}(I) \ge \frac{\alpha(I)+N-1}{N}$) to provide tight bounds for the multidimensional Schwarz Lemma.
- **1982:** Jean-Pierre Demailly published *Formules de Jensen en plusieurs variables et applications arithmétiques*. Using sophisticated complex analytic techniques—specifically Lelong numbers of positive closed $(1,1)$-currents and Skoda's integrability theorem for plurisubharmonic functions—Demailly generalized Chudnovsky's statement to all symbolic powers $m \ge 1$.
- **2001:** The Ein-Lazarsfeld-Smith containment theorem shifted the study of these constants into mainstream commutative algebra, spawning a massive industry analyzing the *resurgence* of ideals.
- **2010s:** Bocci, Harbourne, and Huneke highlighted that counterexamples to general containment conjectures (like $I^{(3)} \subseteq I^2$ for points in $\mathbb{P}^2$, broken by Dumnicki, Szemberg, Tutaj-Gasińska in 2013) do not automatically break Demailly's bound. Thus, Demailly's Conjecture emerged as a highly robust asymptotic property.

**State of the Art:** 
Chudnovsky's Conjecture ($m=1$) is fully proven for very general points in $\mathbb{P}^N$ (Fouli, Mantero, Xie, 2021). However, Demailly's full conjecture ($m > 1$) remains largely open. It is currently known to hold only for very specific point configurations (e.g., star configurations, generic complete intersections) and for general points only under severe restrictions on the number of points.

## 4. Partial Results / Verified Cases

Demailly's Conjecture has been rigorously verified only in the following specialized cases:

1. **Star Configurations:** For any $N$, if $I$ is the ideal of a star configuration of points (the intersection of generic hyperplanes), Demailly's Conjecture holds for all $m \ge 1$. Here, the Waldschmidt constant can be calculated exactly using the Stanley-Reisner rings of matroids (Bocci, Cooper, Harbourne et al., 2016).
2. **General Points in $\mathbb{P}^2$ (Specific Counts):** For $N=2$ (points in the projective plane), Demailly's Conjecture is proven when the number of points $s$ is a perfect square, $s = d^2$, by utilizing the geometry of complete intersections of degree $d$. It is also proven for all $s \ge 4^N$ in the $m=1$ case (Chudnovsky's). 
3. **Monomial Ideals:** For squarefree monomial ideals (which correspond to unions of coordinate linear spaces, rather than just points), analogs of Demailly's Conjecture have been proven using polyhedral geometry and the fractional chromatic number of hypergraphs.
4. **General Points for large $m$:** Malara, Szemberg, and Szpond (2018) verified Demailly's inequality for a general set of $s$ points in $\mathbb{P}^N$ provided $s$ is sufficiently large relative to $N$ and $m$, leveraging specialized vanishing theorems.

## 5. Principal Obstacles

The persistence of Demailly's Conjecture stems from a profound lack of analytic-to-algebraic translation for the $+N-1$ shift.

1. **Non-Additivity of Initial Degrees:** The map $m \mapsto \alpha(I^{(m)})$ is notoriously erratic. For generic points, it approximates $\sqrt[N]{s} \cdot m$, but for points in special positions (e.g., lying on a low-degree curve or surface), the initial degree drops unpredictably.
2. **Failure of the Subadditivity Theorem:** The algebraic proof of $\widehat{\alpha}(I) \ge \alpha(I)/N$ uses the subadditivity of multiplier ideals: $\mathcal{J}(c \cdot \mathfrak{a}) \subseteq \mathcal{J}(\mathfrak{a})^c$. To achieve the $+N-1$ shift required by Demailly, one needs a strict refinement of subadditivity that accounts for the exact discrepancies at the fixed singular points of the linear system. The base locus of $|I^{(m)}|$ can contain non-reduced components, causing traditional Kodaira-style vanishing theorems to fail.
3. **Analytic Methods Do Not Localize in Characteristic $p$:** Demailly's original 1982 analytic proof of a related continuous version relied on the Lelong number $\nu(T, x)$ of a current $T$. While Lelong numbers share similarities with $F$-pure thresholds in characteristic $p>0$, tight closure techniques lack the strict continuity and strict additive constants provided by Skoda's theorem. An exact characteristic $p$ analog of Demailly's complex analytic inequalities has evaded construction.

## 6. The Gap

The boundary between what is currently proven (asymptotic bounds and general points) and the general statement is the **behavior of highly non-generic, pathologically situated points**. 

For example, consider dual Hesse configurations or points constructed from the base loci of specific pencils of hypersurfaces. In these configurations, $I^{(m)}$ can exhibit unexpected containments (e.g., jumping degrees). The gap requires a new algebraic theory of "error terms" for the multiplier ideal containments. Specifically, one must show that the geometric defect caused by points being in special position (which lowers $\alpha(I^{(m)})$) identically forces a proportional drop in $\widehat{\alpha}(I)$, such that the fractional ratio $\frac{\alpha(I^{(m)}) + N - 1}{m + N - 1}$ is never violated. 

## 7. Current Research (as of June 2026)

Active research primarily flows through commutative algebra groups investigating the **resurgence** $\rho(I) = \sup \{ m/r \mid I^{(m)} \not\subseteq I^r \}$. Because Demailly's Conjecture links $I^{(m)}$ strictly to $I$, it is viewed as a refined, degree-theoretic shadow of containment.

- **K-Stability Approaches:** *(frontier — verify)* Recent preprints from researchers intersecting birational geometry and K-stability are attempting to bound Waldschmidt constants by treating the point configurations as log Fano pairs $(X, \Delta)$. By studying the volume of these pairs and their Ding stability, there is a novel attempt to enforce the $+N-1$ dimensional shift globally.
- **Tropical Geometry:** Another active school of thought (e.g., at the Max Planck Institute for Mathematics in the Sciences) uses tropicalization of ideals to approximate $\widehat{\alpha}(I)$ via polyhedral volumes, where Demailly's Conjecture is translated into an optimization problem over specific polytopes.
- **Computational Verification:** Massive computational efforts using heavily optimized, symmetry-aware Gröbner bases (via Singular and Macaulay2) are exhaustively checking Demailly's bounds for non-generic configurations derived from finite geometries (like projective planes over $\mathbb{F}_q$) embedded in $\mathbb{C}^N$.

## 8. Future Work

Leading mathematicians outline the following pathways to resolving or generalizing the conjecture:

1. **The Generalized Demailly Conjecture:** Extending the statement to ideals defining arbitrary subvarieties. If $I \subset \mathbb{P}^N$ defines a subvariety of codimension $e$, the predicted bound is:
   $$ \widehat{\alpha}(I) \ge \frac{\alpha(I^{(m)}) + e - 1}{m + e - 1} $$
   Proving this even for $m=1$ (the Generalized Chudnovsky Conjecture) remains a massive open problem for curves in $\mathbb{P}^3$.
2. **Finding Counterexamples via Resurgence:** Just as the Harbourne containment conjecture ($I^{(rm - N + 1)} \subseteq I^r$) was spectacularly disproven using specific point configurations (e.g., Fermat configurations, Klein configurations), experts suggest that if Demailly's Conjecture is false, the counterexample will arise from a highly symmetric point configuration originating in reflection groups where $\alpha(I^{(m)})$ behaves anomalously for a specific $m$.
3. **Rationality of $\widehat{\alpha}(I)$:** It is not yet known if the Waldschmidt constant $\widehat{\alpha}(I)$ is always a rational number. Proving irrationality for some ideal would severely complicate Demailly's Conjecture, whereas proving rationality might suggest that $\widehat{\alpha}(I)$ can be reached at finite, computable steps.

## 9. Key References

- **[Foundational]** Demailly, J.-P. *Formules de Jensen en plusieurs variables et applications arithmétiques.* Bulletin de la Société Mathématique de France, 110 (1982).
- **[Foundational]** Chudnovsky, G. V. *Singular points on complex hypersurfaces and multidimensional Schwarz lemma.* Séminaire Delange-Pisot-Poitou, 1979/1980. Progress in Mathematics, Birkhäuser, 1981.
- **[Foundational]** Ein, L., Lazarsfeld, R., Smith, K. E. *Uniform bounds and symbolic powers on smooth varieties.* Inventiones Mathematicae 144, 2001.
- **[SOTA / Recent]** Fouli, L., Mantero, P., Xie, Y. *Chudnovsky's Conjecture for very general points in $\mathbb{P}^N$.* Journal of Algebra 567, 2021.
- **[SOTA / Recent]** Malara, G., Szemberg, T., Szpond, J. *On a conjecture of Demailly and new bounds on Waldschmidt constants in $\mathbb{P}^N$.* Journal of Number Theory 189, 2018.
- **[Survey]** Szemberg, T., Szpond, J. *Waldschmidt constants for ideals of points.* Arkiv för Matematik 55, 2017.

## 10. Worked Example / Concrete Special Case

Consider the ambient projective plane $\mathbb{P}^2$ (so $N=2$) over $\mathbb{C}$. Let $R = \mathbb{C}[x, y, z]$. We examine a configuration of 3 generic points: $p_1 = [1:0:0]$, $p_2 = [0:1:0]$, $p_3 = [0:0:1]$.

The homogeneous ideal defining this set of points is $I = \langle xy, yz, zx \rangle$. 
The initial degree of $I$ is clearly $\alpha(I) = 2$.

The $m$-th symbolic power $I^{(m)}$ consists of all polynomials vanishing to order at least $m$ at each of the three coordinate points. A monomial $x^a y^b z^c$ belongs to $I^{(m)}$ if and only if the sum of exponents excluding any one variable is at least $m$. This yields the system of inequalities:
$$ a+b \ge m, \quad b+c \ge m, \quad c+a \ge m $$
Summing these three inequalities gives $2(a+b+c) \ge 3m$, meaning the degree $d = a+b+c$ must satisfy $d \ge \frac{3m}{2}$. Since degree must be an integer, the minimal degree is:
$$ \alpha(I^{(m)}) = \left\lceil \frac{3m}{2} \right\rceil $$
The Waldschmidt constant is therefore easily calculated exactly:
$$ \widehat{\alpha}(I) = \lim_{m \to \infty} \frac{\lceil 3m/2 \rceil}{m} = \frac{3}{2} = 1.5 $$

We can now rigorously test Demailly's Conjecture, which asserts that for $N=2$:
$$ \widehat{\alpha}(I) \ge \frac{\alpha(I^{(m)}) + 2 - 1}{m + 2 - 1} = \frac{\lceil 3m/2 \rceil + 1}{m + 1} $$

Let us evaluate the right-hand side (RHS) for the first few values of $m$:
- **For $m = 1$:** $\text{RHS} = \frac{\lceil 1.5 \rceil + 1}{1 + 1} = \frac{2 + 1}{2} = 1.5$. Here, $1.5 \ge 1.5$ (Tight).
- **For $m = 2$:** $\text{RHS} = \frac{\lceil 3 \rceil + 1}{2 + 1} = \frac{3 + 1}{3} = \frac{4}{3} \approx 1.333$. Here, $1.5 \ge 1.333$ (True).
- **For $m = 3$:** $\text{RHS} = \frac{\lceil 4.5 \rceil + 1}{3 + 1} = \frac{5 + 1}{4} = 1.5$. Here, $1.5 \ge 1.5$ (Tight).
- **For $m = 4$:** $\text{RHS} = \frac{\lceil 6 \rceil + 1}{4 + 1} = \frac{6 + 1}{5} = 1.4$. Here, $1.5 \ge 1.4$ (True).

The conjecture bounds $\widehat{\alpha}(I)$ beautifully from below, oscillating and touching the bound exactly at every odd $m$, demonstrating both the validity and the incredible tightness of Demailly's inequality for this configuration.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*