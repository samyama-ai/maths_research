---
id: 09-probability/optimal-coupling-random-walk-symmetric-group
title: "Optimal Coupling for Random Walks on the Symmetric Group"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Optimal Coupling for Random Walks on the Symmetric Group

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/optimal-coupling-random-walk-symmetric-group` · **Status:** open

## 1. Problem Statement / Conjecture

The random transposition walk on $S_n$ mixes in total variation at time $\frac12 n\log n$, with cutoff (Diaconis–Shahshahani, 1981). That theorem is proved by representation theory, not by coupling. The open problem is whether the probabilistic method — coupling — can reproduce it.

**Problem.** Let $T^{\mathrm{ad}}_{\mathrm{coup}}(n)$ be the infimum, over all *co-adapted* (Markovian) couplings $(X_t,Y_t)_{t\ge0}$ of two copies of the random transposition walk, of $\inf\{t:\sup_{x,y}\mathbb P_{x,y}(T>t)\le 1/4\}$, where $T=\inf\{t:X_t=Y_t\}$. Determine
$$c^\ast \;=\; \lim_{n\to\infty}\frac{T^{\mathrm{ad}}_{\mathrm{coup}}(n)}{n\log n}.$$

**Conjecture (coupling gap).** $c^\ast$ exists and $c^\ast>\tfrac12$: no co-adapted coupling of random transpositions coalesces at the mixing time. A complete resolution requires either (i) an explicit co-adapted coupling with $T^{\mathrm{ad}}_{\mathrm{coup}}(n)\le(\frac12+o(1))n\log n$, disproving the gap, or (ii) a lower bound $\mathbb P_{x,y}(T>cn\log n)\ge 1/4$ valid for *every* co-adapted coupling and some $c>1/2$, together with a matching construction pinning $c^\ast$.

The same question is open for the $k$-cycle walks, for riffle shuffles (mixing at $\frac32\log_2 n$; no coupling proof of the constant $\frac32$ is known), and for general conjugacy-invariant walks on $S_n$.

## 2. Mathematical Foundations

**The walk.** Let $\mu$ be the Diaconis–Shahshahani measure on $S_n$:
$$\mu(\mathrm{id})=\frac1n,\qquad \mu(\tau)=\frac{2}{n^2}\ \ \text{for each of the }\binom n2\text{ transpositions }\tau .$$
The walk is $X_t=\xi_t\xi_{t-1}\cdots\xi_1 X_0$ with $\xi_i\stackrel{\text{iid}}{\sim}\mu$; it is the "pick two cards independently and swap" chain. Its stationary law is uniform, $U(\sigma)=1/n!$, and
$$d(t)=\max_{x}\bigl\|\mathbb P(X_t\in\cdot\mid X_0=x)-U\bigr\|_{\mathrm{TV}} =\|\mu^{\ast t}-U\|_{\mathrm{TV}} ,$$
by translation invariance.

**Upper bound by characters.** For a partition $\lambda\vdash n$ with irreducible representation $\rho_\lambda$ of dimension $d_\lambda$, $\hat\mu(\rho_\lambda)=\beta_\lambda I$ with
$$\beta_\lambda=\frac1n+\frac{n-1}{n}\cdot\frac{\chi_\lambda(\tau)}{d_\lambda},$$
and the upper bound lemma gives
$$4\,\|\mu^{\ast t}-U\|_{\mathrm{TV}}^2\;\le\;\sum_{\lambda\neq(n)} d_\lambda^2\,\beta_\lambda^{2t}.$$
Diaconis and Shahshahani showed the right side is $o(1)$ at $t=\frac12 n\log n+cn$ and that $d(t)\to1$ at $t=\frac12 n\log n-cn$: cutoff at $\frac12 n\log n$ with window $\Theta(n)$.

**Couplings.** A coupling is a process $(X_t,Y_t)$ on $S_n\times S_n$ whose marginals are each the walk, with $X_s=Y_s$ for all $s\ge T$. It is *co-adapted* (equivalently *Markovian*, *immersed*) if there is a filtration $(\mathcal F_t)$ to which both are adapted and such that, conditionally on $\mathcal F_t$, the increment $\xi^X_{t+1}$ has law $\mu$ and $\xi^Y_{t+1}$ has law $\mu$ — the coupler may correlate the two increments but may not look into the future.

**The two classical facts framing the problem.**
- *Coupling inequality:* $d(t)\le\sup_{x,y}\mathbb P_{x,y}(T>t)$ for any coupling.
- *Maximal coupling (Griffeath 1975; Pitman 1976; Goldstein 1979):* there always exists a coupling attaining equality, $\mathbb P_{x,y}(T>t)=\|\mathbb P_x(X_t\in\cdot)-\mathbb P_y(X_t\in\cdot)\|_{\mathrm{TV}}$ for all $t$. That coupling is constructed from the whole path laws and is **not** co-adapted.

So the obstruction is not the existence of an optimal coupling but its *constructibility*: the conjecture asserts that the co-adapted class is strictly weaker for $S_n$. Formally one studies
$$\Phi_n(t)=\inf_{\text{co-adapted}}\ \sup_{x,y}\mathbb P_{x,y}(T>t)\ \ge\ d(t),$$
and asks whether $\Phi_n$ and $d$ have the same cutoff location.

## 3. History & State of the Art (SOTA)

- **1981.** Diaconis and Shahshahani prove the $\frac12 n\log n$ cutoff for random transpositions by Fourier analysis on $S_n$ — the founding example of the cutoff phenomenon for non-commutative groups.
- **1983–1988.** Aldous ("Random walks on finite groups and rapidly mixing Markov chains", 1983) and Aldous–Diaconis ("Shuffling cards and stopping times", 1986) develop *strong uniform times* as a constructive substitute. Broder's strong uniform time for random transpositions is $O(n\log n)$ with a constant well above $1/2$; Matthews (1988) improves the construction but still does not reach $\frac12 n\log n$. A theorem of Aldous–Diaconis shows strong stationary times cannot be sharp when $d(t)$ decays faster than the separation distance — which is the case here.
- **1997.** Bubley–Dyer introduce path coupling, making coupling arguments systematic on chains with a contracting metric. The Cayley (transposition) metric on $S_n$ is not contracted by the random transposition walk, so the method gives nothing sharp.
- **2000.** Burdzy and Kendall, *Efficient Markovian couplings*, show that greedy (locally maximal) co-adapted couplings can be strictly suboptimal, and that "optimal co-adapted" is a genuinely different optimization problem from "maximal".
- **2001.** Kumar and Ramesh prove that *every* Markovian coupling for the Jerrum–Sinclair chain needs exponential time although the chain mixes in polynomial time — the first hard separation between co-adapted coupling time and mixing time.
- **2008–2013.** Connor and Jacka solve the analogous problem exactly on the hypercube $\mathbb Z_2^n$: the optimal co-adapted coupling time is $(1+o(1))n\log n$, while $t_{\mathrm{mix}}=\frac14 n\log n$ — a constant-factor gap of $4$. Connor extends this to the hyper-complete graph.
- **2011–2019.** Berestycki–Schramm–Zeitouni ($k$-cycles, mixing at $\frac1k n\log n$), Hough (2016), and Berestycki–Şengül (cutoff for general conjugacy-invariant walks) settle mixing for a wide family, all by spectral/character or random-graph methods, none by coupling.

**SOTA summary.** Mixing constant $\frac12$: proved (1981). Best coupling-only constant on $S_n$: $O(1)\cdot n\log n$ with constant $>1/2$; no matching lower bound over the co-adapted class is known. The hypercube analogue is fully solved and shows a gap.

## 4. Partial Results / Verified Cases

- **Hypercube $\mathbb Z_2^n$ (Connor–Jacka 2008).** Optimal co-adapted coupling time $\sim n\log n$ versus mixing $\sim\frac14 n\log n$; the optimum is characterized by a deterministic control problem on the number of disagreeing coordinates. The gap is proved, not conjectured.
- **Hyper-complete graph $K_m^n$ (Connor 2013).** Same phenomenon; explicit optimal control, gap constant depending on $m$.
- **Jerrum–Sinclair chain (Kumar–Ramesh 2001).** Markovian coupling time is exponential while mixing is polynomial — coupling can fail by more than a constant.
- **Top-to-random shuffle.** Mixing at $n\log n$ is matched exactly by the Aldous–Diaconis strong uniform time; here the constructive method is sharp, showing failure is walk-specific.
- **Abelian groups.** For $\mathbb Z_N$ nearest-neighbour walks, co-adapted reflection couplings are order-optimal ($\Theta(N^2)$), so the conjectured gap is a phenomenon of large-diameter, high-multiplicity non-commutative settings.
- **Small $n$ on $S_n$.** For $n\le 6$–$7$ the optimal co-adapted coupling can be computed by finite-horizon linear programming over the $|S_n|^2$-state pair chain (transportation LP per step); these computations confirm $\Phi_n(t)>d(t)$ strictly for $t\ge1$ but the range is far too small to identify $c^\ast$.
- **Conjugacy-invariant walks.** Cutoff locations are known (Berestycki–Şengül 2019) for all conjugacy classes with $o(n)$ non-fixed points, giving the target constants the coupling must match — $\frac1k n\log n$ for $k$-cycles.

## 5. Principal Obstacles

- **Non-contracting metric.** Path coupling needs a metric $\rho$ with $\mathbb E[\rho(X_1,Y_1)]\le e^{-\alpha}\rho(x,y)$. On $S_n$ with the transposition metric, a single random transposition applied to a pair at distance $1$ increases the distance with probability $\Theta(1)$; no known metric on $S_n$ contracts under $\mu$ at rate $2/n$, which is what the constant $\frac12$ requires.
- **The coupling must exploit cancellation it cannot see.** The Fourier proof works because $\sum_\lambda d_\lambda^2\beta_\lambda^{2t}$ collapses through massive cancellation across $\Theta(e^{c\sqrt n})$ irreducibles. A co-adapted coupling is a pathwise, local object; it has no mechanism to reproduce a global spectral cancellation.
- **Cutoff window versus coalescence tail.** Cutoff means $d(t)$ falls from $1$ to $0$ over $\Theta(n)$ steps. A coupling must make $\mathbb P(T>t)$ fall equally fast, i.e. the coalescence time must concentrate on a window of relative width $1/\log n$. Co-adapted coalescence times built from local moves are typically sums of near-independent "coupon-collector" stages and carry a heavier tail.
- **The last few fixed points.** Under any natural coupling the discrepancy $\sigma_t=X_tY_t^{-1}$ becomes a permutation with few non-fixed points, and the rate at which the last $O(1)$ points are matched is $\Theta(1/n^2)$ per step, not $\Theta(1/n)$ — this alone costs an extra $\Theta(n\log n)$ unless the coupling arranges for the residual discrepancy to be a single transposition and then resolves it in one lucky step, which happens with probability $2/n^2$.
- **No general lower-bound technology.** Proving $c^\ast>1/2$ requires a bound over the *entire* co-adapted class. The only known method — solving a stochastic control problem over the pair chain, as Connor–Jacka did on the hypercube — relies on the hypercube's coordinatewise symmetry reducing the state to a single integer. On $S_n$ the pair chain reduces only to the cycle type of $\sigma_t$, a partition-valued process with no comparable convexity structure.

## 6. The Gap

Proved: $d(t)$ has cutoff at $\frac12 n\log n$ (spectral), and $\Phi_n(t)\ge d(t)$ always. Proved in the model case: $\Phi_n$ and $d$ have different cutoff constants on $\mathbb Z_2^n$. Unproved on $S_n$: *any* nontrivial lower bound on $\Phi_n$ beyond $d$, and *any* upper bound on $\Phi_n$ with constant approaching $\frac12$.

The precise missing step is a variational characterization of the optimal co-adapted coupling for the discrepancy process $\sigma_t=X_tY_t^{-1}$. Each step, the coupler chooses a joint law on pairs of transpositions with prescribed marginals — a transportation polytope of dimension $\Theta(n^4)$ — as a function of the cycle type of $\sigma_t$. One needs (a) the value function of this control problem, or (b) a convex relaxation whose value already exceeds $\frac12 n\log n$.

## 7. Current Research (as of June 2026)

- **Optimal co-adapted control (Warwick school: Connor, Jacka, Kendall).** Extending the hypercube value-function method to partition-valued discrepancy processes; the immersion-theoretic framework is Kendall's "coupling, local times, immersions". Progress is on wreath products and $\mathbb Z_m^n$, not yet on $S_n$. *(frontier — verify)*
- **Information percolation (Lubetzky–Sly programme).** A pathwise, non-coupling route to cutoff constants; adaptation to conjugacy-invariant walks on $S_n$ is being attempted, and would give a probabilistic proof even if the coupling conjecture is true. *(frontier — verify)*
- **Random-graph and coalescence methods.** Schramm's analysis of the giant component in the transposition random graph, and Berestycki–Şengül's extension, give sharp pathwise control of cycle structure; several groups are trying to convert this into a coupling of two walks by matching giant components. *(frontier — verify)*
- **LP/SDP relaxations of the coupling polytope.** Computing $\Phi_n(t)$ exactly for $n\le7$ and fitting the growth constant; the data are consistent with $c^\ast\ge1$ but do not distinguish $1$ from $2$. *(frontier — verify)*

## 8. Future Work

1. **Construct a good coupling.** Match the cycle types of $\sigma_t$ in stages: first drive $\sigma_t$ to a permutation supported on $o(n)$ points using a "same-transposition" coupling, then coalesce the residue. Determining the best achievable constant for this two-stage scheme is a concrete, tractable target.
2. **Prove a class-wide lower bound.** Establish a supermartingale $f(\sigma_t)$ — e.g. built from the number of non-fixed points and the number of cycles — whose drift is bounded uniformly over all admissible one-step joint laws, giving $c^\ast>1/2$.
3. **Transfer the hypercube proof.** Identify the correct one-dimensional statistic on partitions playing the role of the hypercube's disagreement count, and verify the required convexity of the value function.
4. **Separation results.** Following Kumar–Ramesh, look for a conjugacy-invariant walk on $S_n$ where the co-adapted coupling time exceeds the mixing time by an unbounded factor, not merely a constant.
5. **Relax the class.** Study *non-co-adapted but constructive* couplings (finite look-ahead) and quantify how much look-ahead buys back the constant $\frac12$.

## 9. Key References

- **[Foundational]** P. Diaconis, M. Shahshahani. *Generating a random permutation with random transpositions.* Z. Wahrscheinlichkeitstheorie verw. Gebiete 57 (1981), 159–179.
- **[Foundational]** D. Griffeath. *A maximal coupling for Markov chains.* Z. Wahrscheinlichkeitstheorie verw. Gebiete 31 (1975), 95–106.
- **[Foundational]** J. Pitman. *On coupling of Markov chains.* Z. Wahrscheinlichkeitstheorie verw. Gebiete 35 (1976), 315–322.
- **[Foundational]** S. Goldstein. *Maximal coupling.* Z. Wahrscheinlichkeitstheorie verw. Gebiete 46 (1979), 193–204.
- **[Foundational]** D. Aldous. *Random walks on finite groups and rapidly mixing Markov chains.* Séminaire de Probabilités XVII, Lecture Notes in Math. 986, Springer, 1983, 243–297.
- **[Foundational]** D. Aldous, P. Diaconis. *Shuffling cards and stopping times.* American Mathematical Monthly 93 (1986), 333–348.
- **[Foundational]** P. Diaconis. *Group Representations in Probability and Statistics.* IMS Lecture Notes–Monograph Series 11, 1988.
- **[Foundational]** P. Matthews. *A strong uniform time for random transpositions.* Journal of Theoretical Probability 1 (1988), 411–423.
- **[SOTA / Recent]** K. Burdzy, W. S. Kendall. *Efficient Markovian couplings: examples and counterexamples.* Annals of Applied Probability 10 (2000), 362–409.
- **[SOTA / Recent]** V. S. A. Kumar, H. Ramesh. *Coupling vs. conductance for the Jerrum–Sinclair chain.* Random Structures & Algorithms 18 (2001), 1–17.
- **[SOTA / Recent]** S. B. Connor, S. Jacka. *Optimal co-adapted coupling for the symmetric random walk on the hypercube.* Journal of Applied Probability 45 (2008), 703–713.
- **[SOTA / Recent]** S. B. Connor. *Optimal co-adapted coupling for a random walk on the hyper-complete graph.* Journal of Applied Probability 50 (2013), 1117–1130.
- **[SOTA / Recent]** O. Schramm. *Compositions of random transpositions.* Israel Journal of Mathematics 147 (2005), 221–243.
- **[SOTA / Recent]** N. Berestycki, O. Schramm, O. Zeitouni. *Mixing times for random $k$-cycles and coalescence-fragmentation chains.* Annals of Probability 39 (2011), 1815–1843.
- **[SOTA / Recent]** R. Hough. *The random $k$ cycle walk on the symmetric group.* Probability Theory and Related Fields 165 (2016), 447–482.
- **[SOTA / Recent]** N. Berestycki, B. Şengül. *Cutoff for conjugacy-invariant random walks on the symmetric group.* Probability Theory and Related Fields 173 (2019), 1197–1241.
- **[SOTA / Recent]** R. Bubley, M. Dyer. *Path coupling: A technique for proving rapid mixing in Markov chains.* Proc. 38th IEEE FOCS (1997), 223–231.
- **[SOTA / Recent]** T. P. Hayes, E. Vigoda. *Variable length path coupling.* Random Structures & Algorithms 31 (2007), 251–272.
- **[Survey]** D. A. Levin, Y. Peres. *Markov Chains and Mixing Times*, 2nd edition. American Mathematical Society, 2017.
- **[Survey]** L. Saloff-Coste. *Random walks on finite groups.* In *Probability on Discrete Structures* (H. Kesten, ed.), Encyclopaedia of Mathematical Sciences 110, Springer, 2004, 263–346.
- **[Survey]** W. S. Kendall. *Coupling, local times, immersions.* Bernoulli 21 (2015), 1014–1046.

## 10. Worked Example / Concrete Special Case

Take $n=3$, so $\mu(\mathrm{id})=\frac13$ and $\mu(\tau)=\frac{2}{9}$ for each of $(12),(13),(23)$.

**Spectral side.** The eigenvalues are $\beta_\lambda=\frac13+\frac23\frac{\chi_\lambda(\tau)}{d_\lambda}$: trivial $\lambda=(3)$ gives $1$; sign $\lambda=(1^3)$ gives $\frac13-\frac23=-\frac13$; standard $\lambda=(2,1)$ has $\chi_\lambda(\tau)=0$, $d_\lambda=2$, giving $\frac13$. Hence
$$4d(t)^2\le 1\cdot\left(\tfrac13\right)^{2t}+4\cdot\left(\tfrac13\right)^{2t}=5\cdot 9^{-t},\qquad d(t)\le\frac{\sqrt5}{2}\,3^{-t}.$$
Directly, $d(1)=\frac12\bigl(|\tfrac13-\tfrac16|+3|\tfrac29-\tfrac16|+2\cdot\tfrac16\bigr)=\frac12\bigl(\tfrac16+\tfrac16+\tfrac13\bigr)=\frac13$.

**Coupling side.** Start the two copies at $X_0=\mathrm{id}$, $Y_0=(12)$ — distance $1$ in the Cayley metric. After one step, $X_1=\xi^X$ has law $\mu$, and $Y_1=\xi^Y(12)$ has law
$$\mathbb P(Y_1=(12))=\tfrac13,\quad \mathbb P(Y_1=\mathrm{id})=\tfrac29,\quad \mathbb P(Y_1=(123))=\mathbb P(Y_1=(132))=\tfrac29,$$
using $(13)(12)=(123)$ and $(23)(12)=(132)$. The largest possible one-step coalescence probability is the overlap mass
$$\sum_{\sigma}\min\bigl(\mathbb P(X_1=\sigma),\mathbb P(Y_1=\sigma)\bigr)=\min\!\left(\tfrac13,\tfrac29\right)_{\mathrm{id}}+\min\!\left(\tfrac29,\tfrac13\right)_{(12)}=\tfrac29+\tfrac29=\tfrac49 .$$
So $\Phi_3(1)\ge \frac59$, while $d(1)=\frac13$: already at $t=1$ the best co-adapted coupling is strictly worse than the total variation distance, and the maximal (non-adapted) coupling. This $\frac59$ vs $\frac13$ discrepancy is the gap of Section 6 in miniature.

**Why greedy is not the answer.** Choosing the overlap-maximizing joint law at every step (the "greedy" co-adapted coupling) is optimal for a one-step horizon by construction, but Burdzy–Kendall's counterexamples show greedy choices can be strictly suboptimal over long horizons: it is sometimes better to accept a lower immediate coalescence probability in exchange for steering the discrepancy $\sigma_t$ into a cycle type from which coalescence is cheap. On $S_3$, greedy leaves $\sigma_1$ uniform on $\{(123),(132)\}$ with probability $\frac49$ — a 3-cycle, which needs two more transpositions to clear — whereas a non-greedy step can keep $\sigma_1$ a transposition with higher probability. Quantifying this trade-off for general $n$, over all cycle types of $\sigma_t$, is exactly the control problem whose value would determine $c^\ast$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*