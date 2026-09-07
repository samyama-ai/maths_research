---
id: 09-probability/exceptional-times-dynamical-percolation-3d
title: "Exceptional Times for Dynamical Percolation in 3D"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Exceptional Times for Dynamical Percolation in 3D

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/exceptional-times-dynamical-percolation-3d` · **Status:** open

## 1. Problem Statement / Conjecture

Run bond percolation on $\mathbb{Z}^3$ at the critical parameter $p_c = p_c(\mathbb{Z}^3)$, and let every edge independently refresh its state at rate $1$ (an independent Poisson clock per edge, resampling open/closed with probability $p_c$/$1-p_c$). Write $\omega_t$ for the configuration at time $t$; each fixed $\omega_t$ is a critical percolation configuration.

**Question.** Is there almost surely a random time $t \in [0,\infty)$ at which $\omega_t$ contains an infinite cluster?

Such a $t$ is an *exceptional time*. Since the expected Lebesgue measure of $\mathcal{E} = \{t : \omega_t \text{ percolates}\}$ is $\int \theta(p_c)\,dt$, exceptional times can only exist as a Lebesgue-null set, and only if the question is not trivialized by $\theta(p_c) > 0$.

A complete resolution requires either (i) a proof that $\mathbb{P}[\mathcal{E} \neq \emptyset] = 1$, ideally with the Hausdorff dimension $\dim_H \mathcal{E}$, or (ii) a proof that $\mathcal{E} = \emptyset$ a.s. Conditional on the widely believed $\theta(p_c) = 0$ in $d=3$, the expected answer is **yes**, with

$$\dim_H \mathcal{E} = 1 - \beta \approx 0.58,$$

where $\beta$ is the order-parameter exponent of 3D percolation.

## 2. Mathematical Foundations

Let $G = (V,E)$ with $E = E(\mathbb{Z}^3)$. The state space is $\Omega = \{0,1\}^E$ with product measure $\pi_p$. Dynamical percolation is the Markov process $(\omega_t)_{t \ge 0}$ on $\Omega$ whose generator acts on cylinder functions by

$$(\mathcal{L}f)(\omega) = \sum_{e \in E}\Big( p\,f(\omega^{e \to 1}) + (1-p)\,f(\omega^{e \to 0}) - f(\omega)\Big),$$

so $\pi_p$ is reversible and stationary. Equivalently, each coordinate is an independent two-state chain with stationary law $\mathrm{Bern}(p)$ and relaxation rate $1$; for $s<t$, $\mathrm{Corr}(\omega_s(e),\omega_t(e)) = e^{-(t-s)}$.

Define the events and exponents:

- **One-arm:** $\alpha_1(R) = \mathbb{P}_{p_c}[0 \leftrightarrow \partial B_R] \approx R^{-\xi_1}$, with $\xi_1 = \beta/\nu$ under scaling.
- **Order parameter:** $\theta(p) = \mathbb{P}_p[0 \leftrightarrow \infty]$, $\theta(p_c+\varepsilon) \approx \varepsilon^{\beta}$.
- **Correlation length:** $L(p) \approx |p-p_c|^{-\nu}$.
- **Pivotality:** $e$ is pivotal for event $A$ in $\omega$ if $\mathbf{1}_A(\omega^{e\to1}) \neq \mathbf{1}_A(\omega^{e\to0})$. Russo's formula gives $\frac{d}{dp}\mathbb{P}_p[A] = \mathbb{E}_p[\\#\mathrm{Piv}(A)]$.

For a Boolean function $f:\{0,1\}^n \to \{0,1\}$ the Fourier–Walsh expansion is $f = \sum_{S \subseteq [n]} \hat f(S)\chi_S$, $\chi_S = \prod_{i \in S}(\frac{\omega_i - p}{\sqrt{p(1-p)}})$, and under the dynamics

$$\mathrm{Cov}\big(f(\omega_0), f(\omega_t)\big) = \sum_{S \neq \emptyset} \hat f(S)^2 e^{-t|S|}.$$

This identity is the engine of the whole subject: exceptional times exist when the **spectral mass sits at low frequencies** $|S| \lesssim 1/t$ often enough for a second-moment argument to survive.

The standard second-moment scheme sets $X_R = \int_0^1 \mathbf{1}\{0 \leftrightarrow_{\omega_t} \partial B_R\}\,dt$, so $\mathbb{E}[X_R] = \alpha_1(R)$ and

$$\mathbb{E}[X_R^2] = 2\int_0^1 (1-t)\,\mathbb{P}\big[0 \leftrightarrow_{\omega_0}\partial B_R,\ 0 \leftrightarrow_{\omega_t}\partial B_R\big]\,dt.$$

If $\mathbb{E}[X_R^2] \le C\,\mathbb{E}[X_R]^2$, the Paley–Zygmund inequality gives $\mathbb{P}[X_R > 0] \ge 1/C$ uniformly in $R$, and compactness yields a time with an infinite cluster.

## 3. History & State of the Art (SOTA)

- **1983/1997.** The model appears in work of Häggström, Peres and Steif, *Dynamical percolation* (Ann. IHP, 1997), following a question of Benjamini; independently considered by Olle Häggström and by Itai Benjamini. HPS prove: for every $d$ and every $p \neq p_c$ there are a.s. no exceptional times (Fubini plus a $0$–$1$ law), so all the content is at $p = p_c$. They also give a sufficient condition for the absence of exceptional times, $\int_0^1 \theta(p_c+\varepsilon)\varepsilon^{-2}\,d\varepsilon < \infty$, and settle trees.
- **1999.** Benjamini, Kalai, Schramm (Publ. IHÉS) introduce noise sensitivity and prove crossing events in 2D are noise sensitive — qualitatively, but not at the polynomial noise scale needed for dynamics.
- **2010.** Schramm and Steif (*Annals of Mathematics*) prove **quantitative** noise sensitivity via randomized-algorithm revealment, obtaining the first exceptional times: on the triangular lattice $\mathcal{E} \neq \emptyset$ a.s. with $\dim_H \mathcal{E} \ge 1/6$.
- **2010.** Garban, Pete, Schramm (*Acta Mathematica*) compute the full Fourier spectrum of critical planar percolation, proving $\dim_H \mathcal{E} = 31/36$ on the triangular lattice and establishing existence of exceptional times for **bond percolation on $\mathbb{Z}^2$**, where exponents are unknown.
- **2015.** Hammond, Pete, Schramm construct the local time measure on $\mathcal{E}$ and relate it to the incipient infinite cluster; their machinery also addresses the mean-field regime $d \ge 19$ *(frontier — verify the precise high-$d$ statement)*.
- **Throughout, $d = 3$ has resisted every one of these routes.** No result asserts or denies existence of exceptional times on $\mathbb{Z}^3$.

## 4. Partial Results / Verified Cases

| Setting | Result |
|---|---|
| $\mathbb{Z}^d$, any $d$, $p \neq p_c$ | No exceptional times (HPS 1997). |
| Regular trees at $p_c$ | No exceptional times (HPS 1997); sharp criterion in terms of $\theta$. |
| Triangular lattice site percolation, $d=2$ | $\mathcal{E}\neq\emptyset$, $\dim_H\mathcal{E} = 31/36$ (Schramm–Steif 2010; Garban–Pete–Schramm 2010). |
| $\mathbb{Z}^2$ bond percolation | $\mathcal{E}\neq\emptyset$ a.s. (GPS 2010), dimension not determined. |
| High dimensions ($d \ge 19$ n.n.; $d>6$ spread-out) | Mean-field exponents available: $\theta(p_c)=0$ and triangle condition (Hara–Slade 1990), $\alpha_1(R)\asymp R^{-2}$ (Kozma–Nachmias 2011); dynamical questions accessible. |
| $\mathbb{Z}^d$, $d \ge 11$ | $\theta(p_c) = 0$ (Fitzner–van der Hofstad 2017) — the prerequisite for the question to be non-trivial. |
| $\mathbb{Z}^3$ | **Nothing.** Not even $\theta(p_c)=0$; not even $\alpha_1(R) \le R^{-c}$. |
| Dynamical Erdős–Rényi at $n^{-1}$ | Exceptional times with a giant-type cluster exist inside the critical window (Roberts–Şengül 2018). |

## 5. Principal Obstacles

1. **$\theta(p_c) = 0$ is open in $d = 3$.** Continuity of the order parameter is known for $d = 2$ (Harris–Kesten) and $d \ge 11$ (lace expansion), and the intermediate dimensions $3 \le d \le 10$ are the outstanding gap in percolation theory. If $\theta(p_c) > 0$ the exceptional-times question collapses; if $\theta(p_c)=0$ the question is genuinely about a null set.
2. **No quantitative arm bound.** The second-moment scheme needs $\alpha_1(R) \le R^{-c}$ and a matching two-time bound. In $d=3$ one does not even know $\alpha_1(R) \to 0$ — that statement *is* $\theta(p_c)=0$. Cerf's lower bound on the two-arm exponent (Ann. Probab. 2015) is one of the very few unconditional 3D arm estimates, and it goes the wrong way for this purpose.
3. **No planar duality, no SLE.** Every sharp planar input — Kesten's scaling relations, RSW box-crossing, conformal invariance, $\mathrm{SLE}_6$ arm exponents $\alpha_1 = R^{-5/48}$, $\alpha_4 = R^{-5/4}$ — depends on the existence of an interface curve. In $\mathbb{Z}^3$ interfaces are surfaces; there is no exploration path, hence no low-revealment algorithm of Schramm–Steif type, and no known RSW theory (a major independent open problem).
4. **Fourier spectrum is inaccessible.** GPS's spectral analysis proceeds by decomposing the spectral sample as a fractal set built from planar arm events. The counting arguments have no 3D analogue; the spectral measure of a 3D crossing event has never been located at any scale.
5. **Mean-field methods stop at $d>6$.** Lace expansion converges only in high dimensions; $d=3$ is far below the upper critical dimension $d_c = 6$ and is the maximally non-perturbative case.

## 6. The Gap

Proven: existence in $d = 2$ (via spectral/algorithmic noise sensitivity powered by planar arm exponents) and control in the mean-field regime (via lace expansion). Wanted: $d = 3$, where neither engine runs.

The precise missing step is a **quantitative two-time decorrelation estimate**: a bound of the form

$$\mathbb{P}\big[0 \leftrightarrow_{\omega_0} \partial B_R,\ 0 \leftrightarrow_{\omega_t} \partial B_R\big] \;\le\; C\,\alpha_1(R)\,\alpha_1\big(L(t)\big)^{-1}\alpha_1(R)\quad\text{for } t \ge \tau_R,$$

with $L(t)$ the dynamical length scale and $\tau_R$ the decorrelation time of the arm event, valid on $\mathbb{Z}^3$. Every known derivation of such a bound routes through the Fourier–Walsh spectrum or through a randomized algorithm; supplying either in 3D is the barrier. Even a soft, non-quantitative proof of $\mathcal{E}\neq\emptyset$ in 3D — with no dimension statement — would be a breakthrough, and it would presumably have to first prove $\theta(p_c)=0$ in $d=3$.

## 7. Current Research (as of June 2026)

- **Differential-inequality noise sensitivity.** Vanneuville's derivation of noise sensitivity for percolation from OSSS/differential inequalities rather than Fourier analysis is the most promising dimension-agnostic route; it currently yields sensitivity at scales too coarse for exceptional times *(frontier — verify quantitative reach in $d\ge3$)*.
- **Decision-tree / OSSS technology** (Duminil-Copin, Raoufi, Tassion) proved sharpness of the phase transition in general settings; adapting the same randomized-algorithm inequality to *critical* 3D arm events is an active target (IHES / Geneva / Copenhagen groups).
- **Continuity at $p_c$ in intermediate dimensions.** Work of Hutchcroft and collaborators on critical percolation without perturbative input (exponential-growth graphs, hierarchical models, long-range models) aims at the $3 \le d \le 10$ gap.
- **Numerics.** High-precision Monte Carlo for 3D percolation ($p_c^{\text{bond}}(\mathbb{Z}^3) = 0.24881182(10)$, $\nu = 0.8774(13)$, $\beta = 0.4181(8)$) supports $\theta(p_c)=0$ and, through the heuristic below, $\dim_H \mathcal{E}\approx 0.58$. No direct simulation of the exceptional set in 3D has been published.

## 8. Future Work

1. Prove $\theta(p_c) = 0$ for $\mathbb{Z}^3$ — the mandatory first step.
2. Establish a 3D RSW/box-crossing theory at $p_c$, giving polynomial arm bounds $R^{-C} \le \alpha_1(R) \le R^{-c}$.
3. Build a low-revealment randomized algorithm for 3D crossing events (surfaces instead of curves), or bypass revealment via differential inequalities.
4. Prove the conjectural identity $\dim_H\mathcal{E} = 1-\beta$ as a *scaling relation*, conditionally on the existence of exponents — a conditional theorem would already be valuable and is plausibly within reach of current second-moment technology.
5. Study intermediate models where 3D-like difficulties are tamed: hierarchical lattices, long-range percolation on $\mathbb{Z}$ with $d_{\mathrm{eff}}=3$, and slabs $\mathbb{Z}^2\times\{0,\dots,k\}$.

## 9. Key References

- **[Foundational]** O. Häggström, Y. Peres, J. Steif. *Dynamical percolation.* Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 33 (1997), 497–528.
- **[Foundational]** I. Benjamini, G. Kalai, O. Schramm. *Noise sensitivity of Boolean functions and applications to percolation.* Publications Mathématiques de l'IHÉS 90 (1999), 5–43.
- **[SOTA]** O. Schramm, J. Steif. *Quantitative noise sensitivity and exceptional times for percolation.* Annals of Mathematics 171 (2010), 619–672.
- **[SOTA]** C. Garban, G. Pete, O. Schramm. *The Fourier spectrum of critical percolation.* Acta Mathematica 205 (2010), 19–104.
- **[SOTA]** A. Hammond, G. Pete, O. Schramm. *Local time on the exceptional set of dynamical percolation and the incipient infinite cluster.* Annals of Probability 43 (2015), 2949–3005.
- **[High dimensions]** T. Hara, G. Slade. *Mean-field critical behaviour for percolation in high dimensions.* Communications in Mathematical Physics 128 (1990), 333–391.
- **[High dimensions]** R. Fitzner, R. van der Hofstad. *Mean-field behavior for nearest-neighbor percolation in $d>10$.* Electronic Journal of Probability 22 (2017), paper 43.
- **[High dimensions]** G. Kozma, A. Nachmias. *Arm exponents in high dimensional percolation.* Journal of the AMS 24 (2011), 375–409.
- **[3D bounds]** R. Cerf. *A lower bound on the two-arm exponent for critical percolation on the lattice.* Annals of Probability 43 (2015), 2458–2480.
- **[Survey]** J. Steif. *A survey of dynamical percolation.* In *Fractal Geometry and Stochastics IV*, Progress in Probability 61, Birkhäuser, 2009, 145–174.
- **[Book]** C. Garban, J. Steif. *Noise Sensitivity of Boolean Functions and Percolation.* Cambridge University Press, 2014.
- **[Book]** G. Grimmett. *Percolation*, 2nd edition. Springer, 1999.
- **[Related]** M. Roberts, B. Şengül. *Exceptional times of the critical dynamical Erdős–Rényi graph.* Annals of Applied Probability 28 (2018), 2275–2308.
- **[Numerics]** J. Wang, Z. Zhou, W. Zhang, T. M. Garoni, Y. Deng. *Bond and site percolation in three dimensions.* Physical Review E 87 (2013), 052107.

## 10. Worked Example / Concrete Special Case

**Box-counting heuristic for $\dim_H \mathcal{E}$, calibrated in 2D and evaluated in 3D.**

Fix a scale $R$ and let $A_R = \{0 \leftrightarrow \partial B_R\}$, so $\mathbb{P}[A_R] = \alpha_1(R)$.

*Step 1 — decorrelation time.* The dynamics changes $A_R$ only when a pivotal edge flips. By Russo's formula and the standard scaling relation $\mathbb{E}_{p_c}[\\#\mathrm{Piv}(A_R)] \asymp R^{1/\nu}$ (the number of edges whose flip moves $p$ across the correlation-length scale $L(p)=R$), the natural decorrelation time is

$$\tau_R \asymp \frac{1}{\mathbb{E}[\\#\mathrm{Piv}]} \asymp R^{-1/\nu}.$$

*Step 2 — counting good windows.* Partition $[0,1]$ into $N = \tau_R^{-1} = R^{1/\nu}$ intervals of length $\tau_R$; within one interval the arm event is essentially frozen, and across intervals essentially independent. The expected number of intervals meeting $\{t: A_R \text{ holds in }\omega_t\}$ is

$$N \cdot \alpha_1(R) \asymp R^{1/\nu} \cdot R^{-\beta/\nu} = R^{(1-\beta)/\nu}.$$

*Step 3 — dimension.* Box-counting at resolution $\tau_R = R^{-1/\nu}$ gives

$$\dim \mathcal{E} = \lim_{R\to\infty}\frac{\log\big(N\alpha_1(R)\big)}{\log(1/\tau_R)} = \frac{(1-\beta)/\nu}{1/\nu} = 1-\beta.$$

*Calibration in 2D.* Triangular lattice: $\beta = 5/36$, $\nu = 4/3$, $\alpha_1(R)=R^{-5/48}$, $\alpha_4(R)=R^{-5/4}$, so $\tau_R \asymp R^{-2}\alpha_4(R)^{-1} = R^{-3/4} = R^{-1/\nu}$ ✓, and the formula returns $1 - 5/36 = 31/36$ — exactly the Garban–Pete–Schramm theorem. The heuristic is therefore calibrated.

*Evaluation in 3D.* Inserting the Monte-Carlo exponents $\beta = 0.4181(8)$, $\nu = 0.8774(13)$ (so $\xi_1 = \beta/\nu \approx 0.477$, $\tau_R \approx R^{-1.14}$):

$$\dim_H \mathcal{E}(\mathbb{Z}^3) \;=\; 1 - \beta \;\approx\; 0.582.$$

Since $0 < 1-\beta < 1$ strictly, the prediction is that exceptional times exist in 3D and form a set of positive but non-full dimension.

*Sanity check at mean field.* For $d > 6$, $\beta = 1$, and the formula gives $\dim_H \mathcal{E} = 0$. The high-dimensional case is therefore borderline: exceptional times, if they exist there, have zero Hausdorff dimension and their existence must be decided by logarithmic corrections, not by exponents. This explains why $d\ge19$ required the delicate local-time/IIC construction rather than a bare second-moment argument — and why $d=3$, where the exponents are comfortably strict but unproven, is blocked purely by the absence of arm estimates, not by any borderline arithmetic.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*