---
id: 09-probability/eigenvector-delocalization-heavy-tailed-matrices
title: "Random Matrix Eigenvector Delocalization at the Spectral Edge"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Random Matrix Eigenvector Delocalization at the Spectral Edge

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/eigenvector-delocalization-heavy-tailed-matrices` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $X = (x_{ij})_{1\le i,j\le N}$ be a real symmetric matrix with i.i.d. (up to symmetry) centered entries whose common law has a regularly varying tail
$$\mathbb{P}(|x_{11}| > t) = L(t)\, t^{-\alpha}, \qquad \alpha \in (0,4), \ L \text{ slowly varying}.$$
Normalize $H = a_N^{-1} X$ with $a_N = N^{1/\alpha}$ for $\alpha < 2$ (Lévy matrices) and $a_N = N^{1/2}$ for $\alpha > 2$ (finite variance, Wigner scaling). Let $\lambda_1 \ge \dots \ge \lambda_N$ be the eigenvalues and $u_1,\dots,u_N$ the unit eigenvectors.

**Question.** For which pairs $(\alpha, E)$ with $E$ at or near the **spectral edge** are the eigenvectors *completely delocalized*, i.e.
$$\|u_k\|_\infty \le N^{-1/2+\varepsilon} \quad \text{with probability } 1-o(1) \ \ \text{for all } \lambda_k \text{ near } E,$$
and for which are they *localized*, i.e. $\|u_k\|_\infty \ge c > 0$?

Three sub-statements are open in different degrees:

1. **(Lévy mobility edge.)** For $\alpha \in (0,2)$, does there exist $E_{\mathrm{loc}}(\alpha) < \infty$ such that eigenvectors with $\lambda_k \in (E_{\mathrm{loc}}, \infty)$ are localized and those with $|\lambda_k| < E_{\mathrm{loc}}$ are delocalized? Determine $E_{\mathrm{loc}}(\alpha)$ and the behaviour at the transition.
2. **(Intermediate regime $2<\alpha<4$.)** Here the bulk is semicircular and the bulk eigenvectors are delocalized, but the extreme eigenvalues are Poissonian outliers. Show that the transition in $\|u_k\|_\infty$ from $O(1)$ (outliers) to $N^{-1/2+o(1)}$ (bulk) happens at the index scale $k \sim N^{\gamma(\alpha)}$, and identify $\gamma(\alpha)$.
3. **(Sharp threshold.)** Prove that $\lim_{t\to\infty} t^4\,\mathbb{P}(|x_{11}|>t)=0$ — the necessary and sufficient condition of Lee–Yin for Tracy–Widom edge *eigenvalue* fluctuations — is also necessary and sufficient for complete edge *eigenvector* delocalization.

A complete resolution means proving matching localization and delocalization statements with the transition point identified, for all $\alpha$ in the stated range.

## 2. Mathematical Foundations

**Empirical measure and limiting law.** For $\alpha \in (0,2)$ the empirical spectral distribution of $H = N^{-1/\alpha}X$ converges to a symmetric heavy-tailed law $\mu_\alpha$ with unbounded support and tail $\mu_\alpha([E,\infty)) \sim C_\alpha E^{-\alpha}$; $\mu_\alpha$ is characterized by a fixed-point equation for its Stieltjes transform $m_\alpha(z)$ through the recursive distributional equation on the Poisson weighted infinite tree (PWIT): for $z\in\mathbb{C}^+$ the resolvent diagonal entry $R(z)$ satisfies in law
$$R(z) \stackrel{d}{=} \Big( -z - \sum_{k\ge1} \xi_k^{-2/\alpha} R_k(z) \Big)^{-1},$$
with $(\xi_k)$ the points of a rate-one Poisson process on $\mathbb{R}_+$ and $R_k$ i.i.d. copies of $R$ (Bordenave–Caputo–Chafaï; Bordenave–Guionnet). For $\alpha>2$ the limit is the semicircle $\varrho_{\mathrm{sc}}(E)=\frac{1}{2\pi}\sqrt{(4-E^2)_+}$ with edge $E=\pm 2$.

**Delocalization observables.** The relevant quantities are the $\ell^p$ norms and the inverse participation ratio
$$\mathrm{IPR}(u_k) = \sum_{i=1}^N |u_k(i)|^4 .$$
Complete delocalization is $\|u_k\|_\infty = N^{-1/2+o(1)}$ (equivalently $\mathrm{IPR} = N^{-1+o(1)}$); localization is $\mathrm{IPR} \asymp 1$. Intermediate ("multifractal") behaviour is $\mathrm{IPR}\asymp N^{-\tau}$, $0<\tau<1$.

**Resolvent route.** Delocalization in the finite-variance setting follows from a local law: if for $\eta = \mathrm{Im}\,z \ge N^{-1+\varepsilon}$ one has the *isotropic* estimate
$$\max_{i}\big|G_{ii}(z) - m_{\mathrm{sc}}(z)\big| \prec \sqrt{\frac{\mathrm{Im}\,m_{\mathrm{sc}}}{N\eta}} + \frac{1}{N\eta},\qquad G(z)=(H-z)^{-1},$$
then the spectral decomposition $\mathrm{Im}\,G_{ii}(E+i\eta) = \sum_k \frac{\eta |u_k(i)|^2}{(\lambda_k-E)^2+\eta^2}$ gives $|u_k(i)|^2 \le \frac{\eta}{N}\,\mathrm{Im}\,G_{ii} \cdot C \prec N^{-1}$ on choosing $\eta \sim N^{-1}$. At the edge the relevant scale is $\eta \sim N^{-2/3}$ and $\mathrm{Im}\,m_{\mathrm{sc}}(E+i\eta)\asymp \sqrt{\kappa+\eta}$, $\kappa = ||E|-2|$.

**Extreme value input.** With $\mathbb{P}(|x|>t)\sim t^{-\alpha}$, the maximum of the $\sim N^2/2$ entries satisfies $\max_{i<j}|x_{ij}| \asymp N^{2/\alpha}$, so after Wigner scaling the largest entry of $H$ is of order $N^{2/\alpha - 1/2}$, which diverges precisely when $\alpha < 4$. This is the mechanism behind both Poisson edge statistics and edge localization.

## 3. History & State of the Art (SOTA)

- **1994.** Cizeau and Bouchaud introduce Lévy matrices in the physics literature and predict a *mobility edge*: delocalized states near $E=0$, localized states beyond a finite $E_{\mathrm{loc}}(\alpha)$ for $\alpha<2$, with $E_{\mathrm{loc}}\to\infty$ as $\alpha\to2^-$.
- **2004–2009.** Soshnikov proves Poisson statistics for the largest eigenvalues of Wigner matrices with Cauchy-type entries; Auffinger, Ben Arous and Péché extend this to all $\alpha \in (0,4)$: rescaled top eigenvalues converge to a Poisson point process with intensity $\frac{\alpha}{2}x^{-\alpha-1}dx$. So the edge is *not* Tracy–Widom for $\alpha<4$.
- **2010–2014.** Erdős–Schlein–Yau and Erdős–Yau–Yin establish local semicircle and isotropic local laws, yielding $\|u_k\|_\infty \prec N^{-1/2}$ for all $k$ under subexponential (later, sufficiently many moments) tails. Lee and Yin prove that $t^4\mathbb{P}(|x|>t)\to0$ is necessary and sufficient for Tracy–Widom edge eigenvalue fluctuations.
- **2013–2017.** Bordenave and Guionnet give the first rigorous localization/delocalization results for Lévy matrices: localization for small $\alpha$ at large energy, and delocalization near $E=0$ for all $\alpha\in(0,2)$.
- **2016.** Tarquini, Biroli and Tarzia argue numerically and via the cavity method that Lévy matrices have **no** mobility edge — all states with $|E|<\infty$ delocalized for $\alpha \in (0,2)$ — contradicting Cizeau–Bouchaud. The discrepancy is unresolved rigorously.
- **2018–2021.** Aggarwal, Lopatto, Yau and Marcinek prove GOE bulk eigenvalue statistics and eigenvector statistics for Lévy matrices in the delocalized regime, giving the strongest current structural information.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $\alpha > 4$ (four moments, $t^4\mathbb{P}(|x|>t)\to0$) | Tracy–Widom edge eigenvalues; complete delocalization $\|u_k\|_\infty \prec N^{-1/2}$ up to the edge | Lee–Yin (2014); Erdős–Yau–Yin (2012) |
| Entries with $\mathbb{E}|x|^{4+\varepsilon}<\infty$ | Bulk universality and delocalization | Aggarwal (2019) |
| $\alpha\in(0,4)$, top $O(1)$ eigenvalues | Poisson point process limit; eigenvalues driven by the largest entries, associated eigenvectors localized on $O(1)$ coordinates | Auffinger–Ben Arous–Péché (2009); Soshnikov (2004) |
| $\alpha\in(0,2)$, $E$ in a neighbourhood of $0$ | Delocalization: eigenvectors are supported on $\ge cN$ coordinates; $\|u_k\|_2^2$ mass spread | Bordenave–Guionnet (2013, 2017) |
| $\alpha\in(0,2/3)$, $|E|$ large | Localization: eigenvectors have $\ell^2$ mass concentrated on $O(1)$ sites | Bordenave–Guionnet (2013) |
| $\alpha\in(1,2)$, all $E$ in compacts; $\alpha\in(0,1)$, $E$ near $0$ | GOE local eigenvalue statistics and Gaussian (quantum-ergodic) eigenvector entry statistics | Aggarwal–Lopatto–Yau (2021); Aggarwal–Lopatto–Marcinek (2021) |
| Independent-entry non-symmetric ensembles with $\log$-bounded densities | $\|u_k\|_\infty \lesssim N^{-1/2}\log^{C}N$ | Rudelson–Vershynin (2016) |

## 5. Principal Obstacles

- **No local law at the edge for $\alpha<4$.** The resolvent proof needs $\mathbb{E}|x|^4<\infty$ to control the fluctuation term $Z_i = \sum_{j\ne i}(x_{ij}^2 - \mathbb{E}x_{ij}^2)|G^{(i)}_{jj}|$. When $\alpha<4$, $x_{ij}^2$ is itself in the domain of attraction of an $\alpha/2$-stable law, so $Z_i$ has fluctuations of order $N^{2/\alpha-1}\gg \sqrt{\mathrm{Im}\,m/(N\eta)}$ at the edge scale $\eta\sim N^{-2/3}$. Every self-consistent-equation argument therefore breaks exactly where the problem becomes interesting.
- **Non-self-averaging resolvent.** For $\alpha<2$ the diagonal resolvent entries do not concentrate: $G_{ii}(z)$ converges to a nondegenerate random variable solving the PWIT fixed-point equation. Deterministic $m(z)$ is unavailable, so "$\mathrm{Im}\,G_{ii}\le C$ uniformly" — the standard delocalization certificate — is false; only tail bounds on the limiting distribution are accessible.
- **Truncation destroys the edge.** The standard workaround (truncate at $N^{1/2-\varepsilon}$, apply Wigner theory, treat the rest perturbatively) removes exactly the large entries that create the edge outliers. The discarded part is a sparse matrix of large entries whose eigenvectors are the objects one wants to study; it is not a perturbation.
- **Dynamics require an a priori bound.** Dyson Brownian motion and the eigenvector moment flow of Bourgade–Yau prove universality *given* an initial local law with $\eta \ll$ level spacing. In the heavy-tailed edge regime that input is unproven, so the flow has nothing to start from.
- **The transition itself is a fixed-point instability.** Whether $E_{\mathrm{loc}}(\alpha)<\infty$ is a question about a phase transition in the PWIT recursion — the existence of a nontrivial solution with $\mathrm{Im}\,R(E+i0^+)>0$. Cavity/numerical arguments disagree (Cizeau–Bouchaud vs. Tarquini–Biroli–Tarzia), and no rigorous method resolves the stability of that recursion at large $E$.

## 6. The Gap

Proven: delocalization near $E=0$ for $\alpha\in(0,2)$; localization for $\alpha<2/3$ at large $|E|$; complete delocalization everywhere including the edge for $\alpha>4$; Poisson statistics for the top $O(1)$ eigenvalues for $\alpha<4$.

Missing:

1. For $\alpha \in [2/3, 2)$, **no** localization result at any energy. The gap is the range $E \in (E_{\text{deloc}}(\alpha), \infty)$ where neither statement is available, and the very existence of a finite $E_{\mathrm{loc}}$ is disputed.
2. For $\alpha \in (2,4)$, the edge behaviour of $\|u_k\|_\infty$ as a function of $k$ is completely open. Heuristically, eigenvector $u_k$ should be localized while the $k$-th largest entry-driven outlier exceeds the semicircle edge, i.e. for $k \ll N^{2 - \alpha/2}$, and delocalized beyond; proving either direction requires a local law at scales below $N^{-2/3}$ that does not exist.
3. The necessary-and-sufficient claim (statement 3 of §1) is missing the "necessary" half for eigenvectors: no theorem says that $t^4\mathbb{P}(|x|>t)\not\to0$ *forces* $\liminf \|u_{k}\|_\infty \gg N^{-1/2}$ for $k$ in a growing window.

## 7. Current Research (as of June 2026)

- **NYU / Courant and Princeton (Aggarwal, Lopatto, Yau, Marcinek).** Extending eigenvector moment flow arguments to Lévy ensembles; the current frontier is pushing the delocalized window in $\alpha \in (0,1)$ from a neighbourhood of $0$ to all bounded energies. *(frontier — verify)*
- **IST Austria (Erdős, Cipolloni, Schröder).** Eigenstate thermalization (ETH) for Wigner matrices — $|\langle u_i, A u_j\rangle - \langle A\rangle \delta_{ij}| \prec N^{-1/2}$ — with ongoing work to lower the moment assumption toward the $4$-moment threshold and to reach the edge. *(frontier — verify)*
- **Toulouse / Paris (Bordenave, Guionnet, Male, Benaych-Georges).** Operator-algebraic and PWIT approaches; the fixed-point stability analysis of the recursive distributional equation at large $E$ is the direct route to the mobility-edge question.
- **Statistical physics (Biroli, Tarzia, Parisi school).** Multifractality exponents $\tau(q)$ for Lévy matrices and the analogy with Anderson localization on the Bethe lattice; numerics at $N \sim 10^5$ suggest non-ergodic-but-delocalized states over a wide range of $E$, which if correct means the dichotomy in §1 is itself the wrong question. *(frontier — verify)*
- **Sparse/adjacency analogues.** Erdős–Rényi graphs at $d \sim \log N$ show a rigorously established localization–delocalization transition (Alt–Ducatez–Knowles), and their techniques — quantitative resolvent estimates on the "large-degree" sparse part — are the most promising import into the heavy-tailed edge.

## 8. Future Work

- Prove a **stable local law at intermediate scales** $\eta \in (N^{-2/3}, N^{-1/2})$ for $2<\alpha<4$ by conditioning on the positions and sizes of entries exceeding $N^{1/2}$, treating them as a random sparse rank-$O(N^{2-\alpha/2})$ perturbation with explicit eigenvector overlaps.
- Import the **Alt–Ducatez–Knowles resonance/rank-one-perturbation machinery** from sparse Erdős–Rényi graphs to Lévy matrices; the two ensembles share the mechanism that localization is produced by exceptional rows.
- Settle the **Cizeau–Bouchaud vs. Tarquini–Biroli–Tarzia disagreement** rigorously by analyzing existence and uniqueness of solutions to the PWIT fixed-point equation with $\mathrm{Im}\,R(E+i0^+)>0$ as $E\to\infty$.
- Develop a **multifractal-aware formulation**: replace the binary localized/delocalized statement with a theorem on $\lim \log \mathrm{IPR}(u_k)/\log N = -\tau(\alpha,E)$ and prove $\tau<1$ somewhere.
- Establish the **necessity** direction: construct, for each $\alpha<4$, a growing window of edge indices with $\|u_k\|_\infty \ge N^{-\gamma}$, $\gamma<1/2$.

## 9. Key References

- **[Foundational]** P. Cizeau and J.-P. Bouchaud. *Theory of Lévy matrices.* Physical Review E 50(3), 1810–1822, 1994.
- **[Foundational]** A. Soshnikov. *Poisson statistics for the largest eigenvalues of Wigner random matrices with heavy tails.* Electronic Communications in Probability 9, 82–91, 2004.
- **[Foundational]** A. Auffinger, G. Ben Arous, S. Péché. *Poisson convergence for the largest eigenvalues of heavy tailed random matrices.* Annales de l'IHP Probabilités et Statistiques 45(3), 589–610, 2009.
- **[Foundational]** L. Erdős, B. Schlein, H.-T. Yau. *Semicircle law on short scales and delocalization of eigenvectors for Wigner random matrices.* Annals of Probability 37(3), 815–852, 2009.
- **[SOTA]** C. Bordenave, A. Guionnet. *Localization and delocalization of eigenvectors for heavy-tailed random matrices.* Probability Theory and Related Fields 157, 885–953, 2013.
- **[SOTA]** C. Bordenave, A. Guionnet. *Delocalization at small energy for heavy-tailed random matrices.* Communications in Mathematical Physics 354, 115–159, 2017.
- **[SOTA]** J. O. Lee, J. Yin. *A necessary and sufficient condition for edge universality of Wigner matrices.* Duke Mathematical Journal 163(1), 117–173, 2014.
- **[SOTA]** A. Aggarwal, P. Lopatto, H.-T. Yau. *GOE statistics for Lévy matrices.* Journal of the European Mathematical Society 23(11), 3707–3800, 2021.
- **[SOTA]** A. Aggarwal, P. Lopatto, J. Marcinek. *Eigenvector statistics of Lévy matrices.* Annals of Probability 49(4), 1778–1846, 2021.
- **[SOTA]** J. Alt, R. Ducatez, A. Knowles. *Delocalization transition for critical Erdős–Rényi graphs.* Communications in Mathematical Physics 388, 507–579, 2021.
- **[SOTA]** P. Bourgade, H.-T. Yau. *The eigenvector moment flow and local quantum unique ergodicity.* Communications in Mathematical Physics 350, 231–278, 2017.
- **[SOTA]** M. Rudelson, R. Vershynin. *No-gaps delocalization for general random matrices.* Geometric and Functional Analysis 26, 1716–1776, 2016.
- **[Survey]** E. Tarquini, G. Biroli, M. Tarzia. *Level statistics and localization transitions of Lévy matrices.* Physical Review Letters 116, 010601, 2016.
- **[Survey]** L. Erdős, H.-T. Yau. *A Dynamical Approach to Random Matrix Theory.* Courant Lecture Notes 28, AMS, 2017.

## 10. Worked Example / Concrete Special Case

**A single large entry produces a localized edge eigenvector.**

Take $H = W + a\,(e_1e_2^{\mathsf T} + e_2e_1^{\mathsf T})$, where $W$ is a standard $N\times N$ GOE-normalized Wigner matrix supported on coordinates $3,\dots,N$ (so $\|W\|\to2$), and $a>0$ is one exceptional rescaled entry.

The $2\times2$ block $\begin{pmatrix}0&a\\a&0\end{pmatrix}$ has eigenvalues $\pm a$ with eigenvectors $v_\pm = (e_1\pm e_2)/\sqrt2$, for which $\|v_\pm\|_\infty = 2^{-1/2}$ — maximally localized. Second-order perturbation theory in the coupling to the bulk block gives, for $a > 2$, an eigenvalue $\lambda = a + O\!\big((a^2-4)^{-1}\big)$ and eigenvector
$$u = \frac{v_+ + \delta}{\|v_+ + \delta\|},\qquad \|\delta\|_2^2 \;\asymp\; \frac{1}{a^2-4},$$
so $\|u\|_\infty \ge 2^{-1/2}\big(1+C/(a^2-4)\big)^{-1/2}$, bounded away from $0$: the eigenvector stays localized on two sites as long as $a$ stays a fixed distance above the bulk edge $2$. If instead $a<2$ the state is absorbed into the bulk and hybridizes with $\Theta(N)$ bulk states.

**Where the threshold $\alpha=4$ comes from.** In the actual model, $a$ is not a parameter but the largest of $\binom{N}{2}$ i.i.d. entries divided by $\sqrt N$. With $\mathbb{P}(|x|>t)= t^{-\alpha}$,
$$\max_{i<j}|x_{ij}| \asymp \big(N^2\big)^{1/\alpha} = N^{2/\alpha}, \qquad a_{\max} = \frac{\max|x_{ij}|}{\sqrt N} \asymp N^{2/\alpha - 1/2}.$$
Then $a_{\max}\to\infty$ iff $\alpha<4$, $a_{\max}\to0$ iff $\alpha>4$. This reproduces exactly the Lee–Yin threshold: for $\alpha>4$ no entry escapes the bulk and the edge is Tracy–Widom with delocalized eigenvectors; for $\alpha<4$ there are outliers with localized eigenvectors.

**Counting them.** The $k$-th largest entry is of size $(N^2/k)^{1/\alpha}$, so $a_k \asymp N^{2/\alpha}k^{-1/\alpha}N^{-1/2}$, and $a_k > 2$ iff
$$k \;\lesssim\; N^{2-\alpha/2}.$$
For $\alpha=3$ this predicts $N^{1/2}$ localized edge states; for $\alpha = 3.9$, $N^{0.05}$. The conjectural exponent of §6(2) is therefore $\gamma(\alpha) = 2-\alpha/2$ for $\alpha \in (2,4)$.

**What is not proven.** The argument above is exact only if the exceptional entries are separated and the remaining matrix has norm $2+o(1)$. In the true model the entries below the truncation are *not* a GOE — their fourth moment diverges, the truncated matrix has norm $2 + \Theta(N^{2/\alpha-1/2})$ fluctuations, and the $\sim N^{2-\alpha/2}$ outlier blocks are not disjoint (they share rows with probability $\Theta(1)$ once $k \gg N$, i.e. for $\alpha<2$). Controlling both effects simultaneously is precisely the open step.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*