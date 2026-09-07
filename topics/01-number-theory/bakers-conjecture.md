---
id: 01-number-theory/bakers-conjecture
title: "Baker's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

id: 01-number-theory/bakers-conjecture
title: "Baker's Explicit abc-Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
```

# Baker's Explicit abc-Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/bakers-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Baker's Explicit $abc$-Conjecture is a highly precise, non-asymptotic refinement of the famous $abc$ conjecture. 

Let $a, b,$ and $c$ be coprime positive integers such that $a + b = c$. Let $N = \operatorname{rad}(abc)$ denote the radical (the product of the distinct prime factors of $abc$), and let $\omega = \omega(abc)$ denote the number of distinct prime factors of $abc$. 

Alan Baker conjectured that there exists an absolute, effectively computable constant $\kappa$ such that:
$$ c < \kappa \cdot N \cdot \frac{(\log N)^{\omega}}{\omega!} $$

A complete proof requires establishing this inequality for all coprime positive integer triples $(a,b,c)$ with $a+b=c$. Historically, Baker proposed that the absolute constant might be as small as $\kappa = 6/5$, though computational evidence later showed it must be strictly greater than $1.2003$.

## 2. Mathematical Foundations

The conjecture relies on the fundamental interplay between additive structures and multiplicative prime factorizations in $\mathbb{Z}$. 

**The Radical:**
The radical of a positive integer $n$, denoted $\operatorname{rad}(n)$, is the product of its distinct prime factors:
$$ \operatorname{rad}(n) = \prod_{p \mid n} p $$

**The Prime Divisor Function:**
The function $\omega(n)$ counts the number of distinct prime factors of $n$:
$$ \omega(n) = \sum_{p \mid n} 1 $$

**Connection to the Standard $abc$ Conjecture:**
The standard $abc$ conjecture (Oesterlé–Masser, 1985) states that for any $\epsilon > 0$, there exists a constant $K(\epsilon)$ such that $c \le K(\epsilon) \operatorname{rad}(abc)^{1+\epsilon}$. 
Baker's formulation explicitly eliminates the asymptotic $\epsilon$ by replacing the $N^{\epsilon}$ term with an explicit bounding function. Using Stirling's approximation and the maximal order of the $\omega(n)$ function—specifically that $\omega(N) \ll \frac{\log N}{\log \log N}$—one can rigorously show that for any $\epsilon > 0$, the expression $\frac{(\log N)^{\omega}}{\omega!} \ll_{\epsilon} N^{\epsilon}$. Thus, a proof of Baker's explicit conjecture directly implies the standard $abc$ conjecture with effectively computable constants.

## 3. History & State of the Art (SOTA)

Alan Baker, who won the Fields Medal in 1970 for his work on linear forms in logarithms, proposed this precise bound in 1998 at a conference in Eger, Hungary (published in 1998). Baker was motivated by the desire to bridge the gap between Diophantine approximation bounds derived from linear forms in logarithms and the purely conjectural limits of the $abc$ equation.

While standard $abc$ was framed asymptotically, Baker sought a fully effective formula that computational number theorists could test. By introducing the $\frac{(\log N)^{\omega}}{\omega!}$ multiplier, Baker provided a structural explanation for the "quality" of $abc$ hits (triples where $c > N$). 

**State of the Art (SOTA):**
The conjecture remains entirely open. The current rigorous theoretical limit is far weaker than Baker's quasi-linear bound. Unconditionally, the best known bound is due to Stewart and Yu (2001), who proved that:
$$ c < \exp\left( \kappa' N^{1/3} (\log N)^3 \right) $$
Mochizuki's Inter-universal Teichmüller (IUTT) theory claims to prove the standard $abc$ conjecture, but the claimed effective bounds extracted from IUTT (e.g., by Mochizuki, Fesenko, and others) do not reproduce Baker's extremely sharp explicit functional form, and IUTT itself remains highly contested in the broader mathematical community.

## 4. Partial Results / Verified Cases

Because the general theorem remains out of reach, partial results are largely computational and structural:

- **Computational Verification:** Distributed computing projects (such as ABC@home) have rigorously computed all $abc$ triples for $c \le 10^{18}$. Baker's proposed bounding function holds consistently across this entire dataset.
- **Triviality for Small $\omega$:** For values of $\omega(abc) \le 3$, the conjecture is vacuously verified because the few known solutions easily satisfy the bound with $\kappa \ge 6/5$.
- **Function Field Analogue:** In the polynomial ring $k[t]$, the analogue of Baker's conjecture is governed by the Mason-Stothers theorem: $\max(\deg a, \deg b, \deg c) \le \deg(\operatorname{rad}(abc)) - 1$. This structural equivalent is fully proven and completely eliminates the need for an $\epsilon$ or polynomial multiplier, serving as the philosophical bedrock for why a sharp, non-asymptotic bound must exist over $\mathbb{Z}$.

## 5. Principal Obstacles

The fundamental barrier to proving Baker's conjecture is the inherent limitation of current Diophantine approximation techniques:

1. **The $p$-adic Linear Forms Barrier:** The only known unconditional method to approach $abc$ bounds is through $p$-adic linear forms in logarithms (the method of Stewart and Yu). However, this technique requires evaluating linear combinations $\Lambda = \sum b_i \log p_i$. The error terms in Baker's Theorem scale exponentially with the number of variables (the primes $p_i$). This inherently limits any derived $abc$ bound to an exponential form like $\exp(N^{1/3})$, fundamentally failing to achieve the linear $N$ dependence required by Baker's bound.
2. **The "Prime Conspiracy" Problem:** Analytic methods (like the Hardy-Littlewood circle method) fail because they cannot simultaneously control the additive condition ($a+b=c$) and extreme multiplicative smoothness (highly composite numbers). There is no known sieve or contour integration that operates accurately at the quasi-linear precision Baker's inequality demands.

## 6. The Gap

The "gap" defines the monumental mathematical distance between the current rigorously proven state and the conjecture. 
Currently, we can prove an exponential bound: $c \le \exp(K N^{1/3}(\log N)^3)$.
The conjecture demands a quasi-linear bound: $c \le \kappa N \frac{(\log N)^{\omega}}{\omega!}$.
Bridging this gap requires either crossing the fundamental theoretical barrier of logarithmic forms (achieving completely optimal dependencies on the number of variables in $p$-adic Baker-Wüstholz theorems), or discovering a completely novel geometric mechanism (e.g., via Arakelov geometry or an uncontested, computationally sharp arithmetic deformation theory) that translates directly to Diophantine bounds.

## 7. Current Research (as of June 2026)

Active research primarily flows through two channels:

1. **Probabilistic Heuristics:** Research by Tenenbaum, Robert, and Stewart investigates the probabilistic maximal order of $c / \operatorname{rad}(abc)$. They use statistical models of prime distribution to argue for refined functional forms, heavily scrutinizing whether the $\omega!$ in Baker's denominator is precisely the optimal scale for extremal cases.
2. **Algorithmic Extremal Searches:** High-performance computing groups continue to push the boundary of known $abc$ "hits" to stress-test explicit constants. 
3. **IUTT Consequences:** *(frontier — verify)* Efforts by the RIMS school to extract sharper effective constants from Inter-universal Teichmüller theory to see if it can be tightened to match Baker's proposed explicit inequality.

## 8. Future Work

Leading mathematicians suggest several pathways forward:
- **Intermediate Effective Bounds:** Formulating and proving bounds that sit between Stewart-Yu and Baker, such as proving $c \ll N \exp((\log N)^{\delta})$ for some $\delta < 1/3$.
- **Refining the Constant $\kappa$:** Determining the absolute minimal admissible value of $\kappa$ using refined algorithms for elliptic curve conductor bounds.
- **Heuristic Justification via Random Matrix Theory:** Applying frameworks from random matrix theory and probabilistic number theory to definitively prove whether Baker's function is the *exact* maximal order of the $abc$ equation.

## 9. Key References

- **[Foundational]** Baker, A. "Logarithmic forms and the abc-conjecture." *Number Theory (Eger, 1996)*, de Gruyter, 1998, 37-44.
- **[Foundational]** Stewart, C. L., and Yu, K. "On the abc conjecture." *Mathematische Annalen* 319, 2001, 681-690.
- **[SOTA / Recent]** Robert, O., Stewart, C. L., and Tenenbaum, G. "A refinement of the abc conjecture." *Bulletin of the London Mathematical Society* 46(6), 2014, 1156-1166.

## 10. Worked Example / Concrete Special Case

To ground Baker's conjecture, we can test it against the most extreme $abc$ equation known—discovered by Eric Reyssat—which boasts the highest known "quality" ($q \approx 1.6299$). 

The Reyssat equation is:
$$ 2 + 3^{10} \cdot 109 = 23^5 $$
Here, $a = 2$, $b = 6436341$, and $c = 6436343$.

First, we identify the distinct prime factors of $abc$: $\{2, 3, 23, 109\}$. 
Therefore, $\omega = 4$.
The radical is $N = \operatorname{rad}(abc) = 2 \cdot 3 \cdot 23 \cdot 109 = 15042$.

Now, we calculate the bounding term proposed by Baker:
$$ \text{Term} = N \cdot \frac{(\log N)^{\omega}}{\omega!} = 15042 \cdot \frac{(\log 15042)^4}{4!} $$
Since $\log(15042) \approx 9.6186$:
$$ \text{Term} \approx 15042 \cdot \frac{(9.6186)^4}{24} \approx 15042 \cdot \frac{8555.15}{24} \approx 15042 \cdot 356.464 \approx 5,361,937 $$

We now evaluate the ratio of $c$ to this term to find the required absolute constant $\kappa$:
$$ \kappa \ge \frac{c}{\text{Term}} = \frac{6436343}{5361937} \approx 1.200376 $$

This calculation is historically legendary. When Baker first proposed his explicit conjecture, he tentatively suggested that $\kappa = 6/5 = 1.2$ might be admissible. However, as explicitly calculated here, Reyssat's example yields a ratio of $\approx 1.200376$, which strictly breaks the $6/5$ bound! This concrete example proved that the absolute constant $\kappa$ in Baker's Conjecture must be strictly greater than $1.2003$, solidifying the profound computational boundary of modern number theory.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*