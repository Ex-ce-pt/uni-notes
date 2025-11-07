To analyze data, create models, distinguish between trends and random noise.

> Statistics can be deceiving!

**Correlation** - 2 factors are associated with a 3rd factor.
**Causation** - factor 1 directly causes another.

### Significance testing (Hypothesis testing)

https://www.khanacademy.org/math/statistics-probability/significance-tests￾confidence-intervals-two-samples?t=practice&v=statistical-significance-experiment
https://statisticsbyjim.com/glossary/significance-level/
https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample/idea-of-significance-tests/a/p-value-conclusions
https://www.khanacademy.org/math/statistics-probability/confidence-intervals-one-sample

Mathematical method used to investigate if the difference between the averages of groups can be explained by chance.
Works well in the case when the data is discrete values.

Significance testing can be done with either actual values of data points or proportions of data points that satisfy a given condition. Actual values are used from this point on, but for proportions the logic is the same.

Let there be a **control group** and a **treatment group** (patients, experiments, etc.) and the averages (means) of the data points are $\bar x_{\text{ctrl}}$ and $\bar x_{\text{trt}}$ respectfully.

Null hypothesis - there should be no difference between averages of the groups.
$H_0: \bar x_{\text{crtl}} = \bar x_{\text{trt}}$ 

Alternative hypothesis - there should be significant difference between averages of the groups.
Alternative hypothesis might include different conditions depending on the question at hand.
Examples:
$H_A: \bar x_{\text{crtl}} \neq \bar x_{\text{trt}} \space ; \space H_A: \bar x_{\text{crtl}} \gt \bar x_{\text{trt}} \space ; \space H_A: \bar x_{\text{crtl}} \lt \bar x_{\text{trt}}$

Null hypothesis is tested. If rejected, $H_A$ is accepted as more likely.

Significance level ($\alpha$) - amount of evidence in a sample that we require to conclude that the difference in the averages is significant. Probability of falsely rejecting the null hypothesis.
The lower, the stronger evidence needed.
Usually, $\alpha = 0.05 = 5\%$.

p-value (probability value) - probability that the difference in the averages is *at least* the one we got in the samples, given the assumptions of the null hypothesis.
$p = P(\bar x_\text{random sample} \geq \bar x_{\text{trt}} \space / \space H_0 \text{ is true})$
$p \lt \alpha \Rightarrow \text{Reject } H_0 \text{, } H_A \text{ is accepted as more likely.}$
$p \geq \alpha \Rightarrow H_0 \text{ can't be rejected, no significant difference observed.}$
==CONFIRM: the sign used in the definition of the p-value must be the same as the sign in the alternative hypothesis

There always is uncertainty.
Hypothesis testing only shows what we should assume is more likely, not what is true.

#### Ex.
In patient group $A$ the medicine works better than in $B$.

Null hypothesis: the medicine works the same in both groups.
 $H_0: \bar x_A = \bar x_B$
 Alternate hypothesis: the medicine works differently in both groups.
 $H_A: \bar x_A \neq \bar x_B$

1.
$p = 0.02$ (98% $H_A$ is correct).
$H_A$ is accepted /w 98% significance.

2.
$p = 0.2$ (80% $H_A$ is correct).
Difference between groups can't be proven significant.

### Dependent test

==NOT USEFUL
Compares average delta value for each person
$H_0$ - no diff
$H_A$ - sig. diff

### Errors

|                       |                | $H_0$ is false                     | $H_0$ is true                     |
| --------------------- | -------------- | ---------------------------------- | --------------------------------- |
| $H_0$ rejected        | $H_A$ accepted | OK                                 | **Type I Error (false positive)** |
| $H_0$ is not rejected | $H_A$ rejected | **Type II Error (false negative)** | OK                                |

```"false " + bool(could we prove $H_0$ wrong?)```

### Confidence intervals

Useful when dealing with continuous results (not discrete).
A measure of an uncertainty occurring from random variation when we try to estimate the average of the studied population.
An interval of values the "true value" can reside in.
All values within the interval are equally probable.

Usual confidence level level - 95% (if we were to repeat the experiment many times and construct confidence intervals, they would with 95% probability contain the "true value").

Usually, confidence intervals are used with a number line that plots $(\bar x_{\text{ctrl}} - \bar x_{\text{trt}})$.
If 0 is within the confidence interval of the value $(\bar x_{\text{ctrl}} - \bar x_{\text{trt}})$, the difference between the averages is insignificant, otherwise it is significant.

Size of the interval is determined by:
- random noise - more → bigger
- confidence level - more → smaller

# Chemometrics

Maps to understand and optimize (chemical) processes.
Studies data analysis and tracing of hidden relations.
Builds maps to create intuition/interpretation.

Chemistry X Mathematics X Statistics


PCA - principal component analysis.

score graph - objects (rows)
loading graph - values (columns)

- Data table
- n-dimensional space
- a lower-dimensional section of the space
- pick 2 points and a vector between them
- translate the vector onto the loadings graph through the origin
- project points on the vector line
- positive correlation=above avg., negative correlation=below avg.

Origin point - average
