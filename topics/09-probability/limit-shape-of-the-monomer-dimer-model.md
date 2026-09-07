---
id: 09-probability/limit-shape-of-the-monomer-dimer-model
title: "Limit Shape of the Monomer-Dimer Model"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Limit Shape of the Monomer-Dimer Model

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/limit-shape-of-the-monomer-dimer-model` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Take a sequence of finite subgraphs $G_n \subset \mathbb{Z}^2$ obtained by scaling a fixed Jordan domain $\Omega \subset \mathbb{R}^2$ by $n$ and intersecting with the lattice $\tfrac1n\mathbb{Z}^2$. A **monomer-dimer configuration** is a matching $M$ of $G_n$ (a set of pairwise disjoint edges); unmatched vertices are *monomers*. Weight a configuration by $\lambda^{\\#\text{monomers}}$, $\lambda > 0$, and sample $M$ from the resulting Gibbs measure.

**The problem.** Prove that the random height-type function / local edge-density field associated with $M$ satisfies a law of large numbers with a deterministic limit, and identify that limit.

Concretely, three linked claims are open in dimension $2$ at fixed $\lambda>0$:

1. **(Concentration)** The normalized height function $h_n(\lfloor nx \rfloor)/n$ converges in probability, uniformly on $\Omega$, to a deterministic Lipschitz function $h_\star$ depending only on $\Omega$, the boundary data, and $\lambda$.
2. **(Variational characterization)** $h_\star$ minimizes a surface-tension functional $\int_\Omega \sigma_\lambda(\nabla h)\,dA$ over admissible $h$, where $\sigma_\lambda$ is the $\lambda$-dependent surface tension of the translation-invariant monomer-dimer Gibbs measures on $\mathbb{Z}^2$.
3. **(Phase separation / arctic phenomenon)** For $\lambda > 0$ determine whether $\Omega$ still splits into frozen and liquid regions separated by a rectifiable *arctic curve*, or whether monomers destroy frozen phases at every $\lambda>0$ so the limit shape is analytic in the interior.

A complete solution must supply either (a) a proof of (1)–(2) with an explicit or characterized $\sigma_\lambda$, or (b) a counterexample showing failure of concentration or of the variational principle. Statement (3) is answered by exhibiting the arctic curve (e.g. for the Aztec diamond with monomer fugacity) or proving no frozen region exists.

## 2. Mathematical Foundations

**Matching polynomial.** For a finite graph $G=(V,E)$ let $m_k(G)$ be the number of matchings with $k$ edges. The partition function with monomer fugacity $\lambda$ and dimer weight $1$ is
$$
Z_G(\lambda) \;=\; \sum_{M \text{ matching}} \lambda^{|V|-2|M|} \;=\; \sum_{k\ge 0} m_k(G)\,\lambda^{|V|-2k}.
$$

**Heilmann–Lieb theorem.** All zeros of $Z_G(\lambda)$ in $\lambda$ are purely imaginary; equivalently the roots of $\sum_k m_k(G) x^k$ are real and negative. Hence $\lambda \mapsto \tfrac1{|V|}\log Z_{G_n}(\lambda)$ has a limit analytic on $\{\Re\lambda>0\}$ and there is **no phase transition** in $\lambda>0$ in any dimension (Heilmann–Lieb 1972).

**Free energy and pressure.** For $\mathbb{Z}^d$ with van Hove exhaustion $\Lambda_n$,
$$
f_d(\lambda)\;=\;\lim_{n\to\infty}\frac{1}{|\Lambda_n|}\log Z_{\Lambda_n}(\lambda),\qquad
\rho(\lambda)\;=\;\lambda\,\partial_\lambda f_d(\lambda)
$$
is the monomer density. The **monomer-dimer entropy** of $\mathbb{Z}^d$ is $h_d = f_d(0^+)$ restricted to perfect matchings; the *free* monomer-dimer entropy is $\max_\lambda$-type Legendre data of $f_d$.

**Slopes and surface tension.** Orient $\mathbb{Z}^2$ bipartitely. For a dimer-only configuration the height function $h:\mathbb{Z}^2{}^*\to\mathbb{Z}$ is defined by Thurston's rule: crossing an edge, $h$ changes by $+3$ if a dimer is crossed with white on the left and $-1$ otherwise (suitably normalized). Its mean slope $s=(s_1,s_2)$ lies in the Newton polygon $N = \{|s_1|+|s_2|\le 1\}$ of the characteristic polynomial $P(z,w)=z+z^{-1}+w+w^{-1}$. For $\lambda=0$ the surface tension is explicit via the Ronkin function
$$
\sigma_0(s) \;=\; -\!\max_{(B_1,B_2)}\Big[ \langle s,B\rangle - R(B)\Big],\qquad
R(B)=\frac{1}{(2\pi i)^2}\!\!\int_{|z|=e^{B_1}}\!\int_{|w|=e^{B_2}}\!\!\log|P(z,w)|\,\frac{dz}{z}\frac{dw}{w},
$$
and the limit shape solves the Euler–Lagrange equation, equivalent to the **complex Burgers equation** $\partial_z w /w + \partial_w$-type system of Kenyon–Okounkov (2007).

**The monomer-dimer height function.** With monomers present, $h$ is no longer well defined: it fails to be closed around a monomer, which acts as a defect of charge $\pm 1$ (a vortex). One works instead with a height function defined up to monomer-connecting "strings", or with the local edge-occupation field $\big(\mathbb{P}[e\in M]\big)_{e}$ and its coarse-graining. The conjectural variational problem is
$$
h_\star \;=\; \arg\min_{h\in \mathrm{Lip}(N),\, h|_{\partial\Omega}=b} \int_\Omega \sigma_\lambda(\nabla h)\,dA,
$$
with $\sigma_\lambda$ the specific free energy per unit area of the ergodic monomer-dimer Gibbs measure of slope $s$ — an object whose *existence and strict convexity* are themselves unproven for $\lambda>0$.

## 3. History & State of the Art (SOTA)

- **1937.** Fowler and Rushbrooke introduce the dimer model for diatomic adsorbates; monomers appear as vacancies.
- **1961.** Kasteleyn, and Temperley–Fisher, solve the *pure dimer* ($\lambda=0$) model on planar graphs via Pfaffians, giving $h_2 = G/\pi \approx 0.29156$ (Catalan's constant).
- **1963–1972.** Fisher–Stephenson study dimer correlations; Gruber–Kunz (1971) and **Heilmann–Lieb (1972)** prove absence of phase transition for $\lambda>0$ and the real-zeros theorem, killing hopes of a monomer-driven transition but leaving structure unresolved.
- **1996–2001.** Kenyon–Randall–Sinclair give an FPRAS-based analysis of monomer-dimer coverings; **Cohn–Kenyon–Propp (2001)** prove the variational principle and limit-shape theorem for **domino tilings** ($\lambda=0$), following the arctic circle theorem of Jockusch–Propp–Shor (1998).
- **2006–2007.** **Kenyon–Okounkov–Sheffield** classify ergodic Gibbs measures for dimers on periodic bipartite graphs (frozen/liquid/gaseous trichotomy); **Kenyon–Okounkov** solve limit shapes via the complex Burgers equation and algebraic arctic curves.
- **2005–2013.** Friedland–Peled, Friedland–Krop–Markström and Federbush obtain rigorous numerical bounds and asymptotic expansions for $f_d(\lambda)$ in $d\ge 2$.
- **2016.** **Giuliani–Jauslin–Lieb** give a Pfaffian formula for monomer-dimer partition functions when monomers are confined to the boundary of a planar region — the only broad exactly-solvable monomer class.
- **2019–2024.** Betz–Taggi, Taggi, and Quitmann–Taggi develop reflection-positivity and random-path techniques giving long-range order and uniformly positive correlations for dimers/loops in $d\ge 3$, and monomer-density lower bounds.

**SOTA summary:** the limit shape is a *theorem* at $\lambda=0$ on planar bipartite periodic graphs, and a *theorem* for monomers restricted to the boundary in specific solvable families; it is **open for $\lambda>0$ with bulk monomers** in $d=2$.

## 4. Partial Results / Verified Cases

- **$\lambda = 0$, planar bipartite periodic graphs.** Full limit-shape theorem with explicit $\sigma_0$; arctic curves are algebraic (Kenyon–Okounkov 2007). Includes the Aztec diamond (arctic circle), hexagon (arctic ellipse), and rail-yard graphs.
- **$d=1$.** Exactly solvable for all $\lambda>0$ by transfer matrix; explicit free energy and density profile (Section 10). Limit shape is trivially flat; fluctuations are Gaussian with exponentially decaying correlations.
- **Boundary monomers, planar.** Giuliani–Jauslin–Lieb (2016) give an exact Pfaffian for monomers on the boundary of a planar graph; combined with Kasteleyn theory this yields limit shapes for e.g. Aztec-diamond-type regions with boundary defects.
- **Complete graph / mean field.** Alberici–Contucci–Mingione establish exact asymptotics, large deviations and a full solution of the monomer-dimer model on $K_n$ and on dense/diluted random graphs.
- **Trees and Bethe lattice.** Explicit fixed-point (belief propagation) solution; monomer density is analytic in $\lambda$.
- **Entropy bounds.** Friedland–Peled compute $f_2(\lambda)$ to high accuracy for $\mathbb{Z}^2$; $h_2 = G/\pi$ exactly; $h_3 \approx 0.4466$ with rigorous upper/lower bounds.
- **No phase transition.** Heilmann–Lieb: $f_d(\lambda)$ is analytic in $\lambda>0$ for every $d$ — so the limit shape, if it exists, depends analytically on $\lambda$ in the bulk.
- **$d \ge 3$ structural results.** Taggi (2022) proves uniformly positive dimer–dimer correlations and macroscopic interacting self-avoiding walks for small monomer density; not a limit-shape statement but constrains the phase picture.

## 5. Principal Obstacles

- **Loss of determinantal structure.** Kasteleyn's method converts perfect matchings of a planar graph into a Pfaffian. With bulk monomers the sign structure fails: the monomer-monomer correlation is not a determinant, and no Kasteleyn-type orientation handles interior defects. Every technique built on the inverse Kasteleyn matrix (local statistics, GFF fluctuations, Ronkin functions) is unavailable.
- **No height function.** The height function is the object concentration is proven for. Monomers are $\pm1$ vortices: $h$ is only defined modulo string choices, so "Lipschitz function converging to a minimizer" has no direct analogue. Constructing a canonical coarse-grained height requires controlling monomer pairing at all scales — precisely what is unknown.
- **Surface tension not accessible.** The $\lambda=0$ tension comes from an explicit spectral curve $P(z,w)$. For $\lambda>0$, $\sigma_\lambda(s)$ is defined only as a limit; existence for each slope $s$, strict convexity, and even continuity in $s$ are unproven. Without strict convexity the variational problem has no unique minimizer and the Euler–Lagrange PDE is not elliptic.
- **Concentration mechanism.** Cohn–Kenyon–Propp's proof uses exact enumeration of tilings of a torus plus a large-deviation upper bound with matching entropy — both enumerative. Monomer-dimer counting is $\\#\mathrm{P}$-hard in general; only Markov chain (Jerrum–Sinclair) approximation is available, and MCMC mixing bounds give no shape theorem.
- **Correlation decay is unknown at the required strength.** Heilmann–Lieb analyticity gives no quantitative decay rate uniform in the region; without exponential decay of edge–edge correlations one cannot run a standard coarse-graining/subadditivity argument.

## 6. The Gap

Section 4 proves the shape theorem exactly where a Pfaffian exists: $\lambda=0$, or monomers pinned to the boundary. Section 1 asks for $\lambda>0$ with monomers free in the bulk.

The precise crossing point is a **two-step gap**:

1. **Build $\sigma_\lambda$.** Show that for every slope $s$ in the interior of the Newton polygon, the specific free energy of monomer-dimer measures at slope $s$ exists and is strictly convex in $s$. Nothing in Heilmann–Lieb constrains $s$-dependence — their theorem is about $\lambda$-analyticity at fixed geometry.
2. **Transfer entropy to geometry.** Even granting $\sigma_\lambda$, one needs a large-deviation principle for the coarse-grained field with rate $\int \sigma_\lambda(\nabla h)$, at speed $n^2$. The dimer proof does this by patching torus tilings; the monomer analogue needs a *gluing lemma* — that monomer-dimer configurations on adjacent boxes with matched boundary can be concatenated with only $o(n^2)$ entropy loss. Monomer flux across box boundaries is unbounded, so the standard cut-and-paste bound fails.

Bridging (1) and (2) — or exhibiting non-concentration — is the whole problem.

## 7. Current Research (as of June 2026)

- **Random path / reflection positivity school (Taggi, Quitmann, Betz; Vienna, Rome Tor Vergata, Darmstadt).** Extending loop-model and self-avoiding-walk representations to prove correlation inequalities and monomer-density bounds; $d\ge 3$ long-range order results are the strongest structural inputs. *(frontier — verify: quantitative $d=2$ decay rates.)*
- **Pfaffian/renormalization group (Giuliani, Jauslin, Mastropietro; Rome, Princeton).** Constructive RG treatment of interacting dimers and of monomers as boundary defects; the goal is a controlled expansion in small monomer fugacity $\lambda$ around the Kasteleyn solution. *(frontier — verify.)*
- **Exact solvability of defect ensembles (Ayyer, Chhita, Bufetov, Duits).** Arctic curves for rail-yard graphs, tilings with defects and non-uniform weights; a monomer-fugacity deformation of the Aztec diamond arctic circle is actively sought. *(frontier — verify.)*
- **Statistical-physics numerics.** Transfer-matrix and worm-algorithm simulations report smooth density profiles with no sharp arctic curve at $\lambda>0$, consistent with a $\lambda$-analytic bulk and a *softened* arctic boundary of width $\sim \lambda^{a} n^{2/3}$. *(frontier — verify the exponent.)*
- **Mean-field and random-graph extensions (Alberici, Contucci, Mingione; Bologna).** Large deviations and central limit theorems on sparse random graphs, providing a template for the variational formulation.

## 8. Future Work

- Prove existence and strict convexity of $\sigma_\lambda(s)$ by subadditivity on tori with prescribed flux; this alone would be a major theorem.
- Develop a **monomer-pairing / string representation** in which the height defect is repaired at cost proportional to the monomer separation, then show strings are short (exponentially tight) at fixed $\lambda>0$.
- Perturbative regime: prove the limit shape for $0<\lambda<\lambda_0(\Omega)$ via convergent cluster expansion around the Kasteleyn measure, treating monomers as a dilute gas of defects.
- Identify the arctic-curve deformation: compute, even non-rigorously, the $\lambda$-expansion of the Aztec diamond arctic circle and determine whether frozen regions survive at any $\lambda>0$.
- Settle whether the monomer-monomer correlation on $\mathbb{Z}^2$ at $\lambda=0^+$ decays as $r^{-1/2}$ (Fisher–Stephenson conjecture) — a long-standing prerequisite for any bulk-monomer shape theory.

## 9. Key References

- **[Foundational]** O. J. Heilmann and E. H. Lieb. *Theory of monomer-dimer systems.* Communications in Mathematical Physics, 25(3):190–232, 1972.
- **[Foundational]** P. W. Kasteleyn. *The statistics of dimers on a lattice: I. The number of dimer arrangements on a quadratic lattice.* Physica, 27(12):1209–1225, 1961.
- **[Foundational]** M. E. Fisher and J. Stephenson. *Statistical mechanics of dimers on a plane lattice. II. Dimer correlations and monomers.* Physical Review, 132:1411–1431, 1963.
- **[Foundational]** H. Cohn, R. Kenyon and J. Propp. *A variational principle for domino tilings.* Journal of the American Mathematical Society, 14(2):297–346, 2001.
- **[SOTA]** R. Kenyon, A. Okounkov and S. Sheffield. *Dimers and amoebae.* Annals of Mathematics, 163(3):1019–1056, 2006.
- **[SOTA]** R. Kenyon and A. Okounkov. *Limit shapes and the complex Burgers equation.* Acta Mathematica, 199(2):263–302, 2007.
- **[SOTA]** A. Giuliani, I. Jauslin and E. H. Lieb. *A Pfaffian formula for monomer-dimer partition functions.* Journal of Statistical Physics, 163(2):211–238, 2016.
- **[SOTA / Recent]** L. Taggi. *Uniformly positive correlations in the dimer model and macroscopic interacting self-avoiding walk in $\mathbb{Z}^d$, $d\ge 3$.* Communications on Pure and Applied Mathematics, 75(6):1183–1236, 2022.
- **[Recent]** D. Alberici, P. Contucci and E. Mingione. *A mean-field monomer-dimer model with attractive interaction: exact solution and rigorous results.* Journal of Mathematical Physics, 55, 063301, 2014.
- **[Computational]** S. Friedland and U. N. Peled. *Theory of computation of multidimensional entropy with an application to the monomer-dimer problem.* Advances in Applied Mathematics, 34(3):486–522, 2005.
- **[Computational]** C. Kenyon, D. Randall and A. Sinclair. *Approximating the number of monomer-dimer coverings of a lattice.* Journal of Statistical Physics, 83:637–659, 1996.
- **[Survey]** L. Lovász and M. D. Plummer. *Matching Theory.* North-Holland (Annals of Discrete Mathematics 29), 1986.
- **[Survey]** R. Kenyon. *Lectures on dimers.* IAS/Park City Mathematics Series, vol. 16, American Mathematical Society, 2009.
- **[Historical]** W. Jockusch, J. Propp and P. Shor. *Random domino tilings and the arctic circle theorem.* Preprint, 1998 (arXiv:math/9801068).

## 10. Worked Example / Concrete Special Case

**The one-dimensional chain, solved exactly.** Let $P_n$ be the path with vertex set $\{1,\dots,n\}$. With monomer fugacity $\lambda$ and dimer weight $1$,
$$
Z_n(\lambda) \;=\; \lambda\,Z_{n-1}(\lambda) \;+\; Z_{n-2}(\lambda), \qquad Z_0 = 1,\; Z_1 = \lambda,
$$
since vertex $n$ is either a monomer (factor $\lambda$, leaving $P_{n-1}$) or matched to $n-1$ (leaving $P_{n-2}$).

Transfer matrix $T=\begin{pmatrix}\lambda & 1\\ 1& 0\end{pmatrix}$ has eigenvalues $\mu_\pm = \tfrac{\lambda \pm \sqrt{\lambda^2+4}}{2}$, so the free energy per site is
$$
f_1(\lambda) \;=\; \log \mu_+ \;=\; \log\frac{\lambda+\sqrt{\lambda^2+4}}{2},
$$
analytic on $\lambda>0$ — Heilmann–Lieb in the simplest case. The monomer density is
$$
\rho(\lambda) \;=\; \lambda\,\frac{d}{d\lambda}\log\mu_+ \;=\; \frac{\lambda}{\sqrt{\lambda^2+4}} .
$$
Checks: $\rho(0)=0$ (perfect matching, $n$ even), $\rho(\infty)=1$ (all monomers), $\rho(2)=1/\sqrt2 \approx 0.707$. At $\lambda=1$, $Z_n$ is the Fibonacci number $F_{n+1}$, $\mu_+=\varphi=1.618\ldots$, and $\rho = 1/\sqrt5 \approx 0.4472$: about $44.7\%$ of sites are monomers.

**Why this is easy and $d=2$ is not.** In $d=1$ the transfer matrix is $2\times 2$ and independent of $n$; the "limit shape" is the constant density $\rho(\lambda)$, and boundary effects decay as $(\mu_-/\mu_+)^{k}$, exponentially. In $d=2$ the transfer matrix acts on a space of dimension $2^{n}$, and at $\lambda=0$ it is diagonalized by free fermions (Kasteleyn) — giving the arctic circle for the Aztec diamond: with $N$ scaled to $1$, the frozen/liquid boundary is exactly $x^2+y^2 = 1/2$. Turning on $\lambda>0$ inserts vortex defects that break the fermionic diagonalization. Numerically the sharp circle blurs into a band of positive width; whether that band shrinks to a curve as $n\to\infty$, and what curve it is, is exactly claim (3) of Section 1 and remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*