
$\text{Probability} = \frac{\text{\# of times an event occurs}}{\text{total \# of events}}$.

**Statistical probability** - determined from statistical data instead of theoretical reasoning.
Accuracy of statistical probability depends largely on the size of the sample.
Bigger sample → more accurate probability.

#### Cumulative probability

Product rule: $P(A \land B) = P(AB) = P(A) \cdot P(B)$
Sum rule: $P(A \lor B) = P(A + B) = P(A) + P(B)$
(these apply for independent events)

**Independent events** - do not affect the probability of each other.

Binomial probability formula:
$$
\begin{flalign}
&P = C_{n,k} \cdot p^k \cdot q^{n-k} \\
&P \text{ - probability that when performing n experiments, exactly n will be successful.} \\
&p \text{ - probability of a single independent experiment.} \\
&q \text{ - probability of the opposite experiment.} \space (= 1 - p) \\
&n \text{ - \# of experiments conducted.} \\
&k \text{ - (exact) \# of experiments that are successful.} \\
&C_{n,k} \text{ - binomial coefficient.} \space C_{n,k} = \frac{n!}{k! (n-k)!}
&\end{flalign}
$$

**Chi-squared test**
Evaluates whether data & hypothesis are a good fit.
$$
\begin{flalign}
&\chi^2 = \sum \frac{(O - E)^2}{E} \\
&\chi \text{ - } \\
&O \text{ - observed \# in each category.} \\
&E \text{ - expected \# in each category.}
&\end{flalign}
$$
1. Propose the null hypothesis: ratio of genotypes produces is ... Deviation is caused by random chance.
2. Calculate expected values based on the proposed ratioes.
3. Apply the chi-squared formula.
4. Interpret the value by translating $\chi^2$ into the p-value (likelihood that the deviation could be caused by random chance).
   Degrees of freedom = n - 1; n - \# of phenotypes
5. If the p-value is less than 0.05, we reject the null hypothesis - significant difference, cannot be sure that the hypothesis is likely.

## In genetics

If 2 alleles are independent of each other and you need to calculate the probability/proportion of a multihybrid cross, **do not draw large Punnett squares**!
This is not sustainable!
Only ever draw the 2x2 [[Principles of Heredity#Punnett square|Punnett squares]] for one gene and use probability calculations based on that.

