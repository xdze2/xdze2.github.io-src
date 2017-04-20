Title: Numerical Optimization
Tags: algorithme, optimisation
Slug: bookNumOptimi
Authors: xdze
Summary: Notes de lecture du livre "Numerical Optimization" de Jorge Nocedal et Stephen J. Wright.

Notes lecture du livre "Numerical Optimization" de Jorge Nocedal et Stephen J. Wright.


ref.: http://www.bioinfo.org.cn/~wangchao/maa/Numerical_Optimization.pdf



# Chapter 1 - Introduction


- modeling: identifying objective, variables, and constraints for a given problem
- optimization algorithm
- sensitivity analysis, &optimality


* CONTINUOUS vs DISCRETE
* CONSTRAINED vs UNCONSTRAINED
* linear vs nonlinear (programming)
* GLOBAL vs LOCAL
* STOCHASTIC vs DETERMINISTIC
...quantifications of the uncertainty to produce solutions that optimize the expected performance of the model.


"Optimization algorithms are iterative. They begin with an initial guess of the optimal values of the variables and generate a sequence of improved estimates until they reach a solution. The strategy used to move from one iterate to the next distinguishes one algorithm from another. Most strategies make use of the values of the objective function /f/, the constraints /c/, and possibly the first and second derivatives of these functions. Some algorithms accumulate information gathered at previous iterations, while others use only local information from the current point."


Tradeoffs : Robustness, Efficiency, Accuracy


Convex function: en-dessous de ses cordes, et sur un domaine convexe

" If we know that f is convex, then we can be sure that the algorithm has converged to a global minimizer."



# Chapter 2  - Unconstrained Optimization

* (First-Order Necessary Conditions) x* Local minimizer : gradient( x* ) = 0

mais une épaule...

* (Second-Order Necessary Conditions) x* Local minimizer : gradient( x* ) = 0  and laplacien( x* ) > 0 and semidefinite (?, Hessian matrix)

mais un col (selle de cheval)...

* (Second-Order Sufficient Conditions):  x* Local minimizer : gradient( x* ) = 0  and laplacien( x* ) > 0 and definite

mais x^4... ?

NONSMOOTH PROBLEMS: subgradient, or generalized gradient ?


TWO STRATEGIES: LINE SEARCH AND TRUST REGION

"In a sense, the line search and trust-region approaches differ in the order in which they choose the direction and distance of the move to the next iterate. Line search starts by fixing the direction and then identifying an appropriate distance, namely the step length. In trust region, we first choose a maximum distance —the trust-region radius— and thenseek a direction and step that attain the best improvement possible subject to this distance constraint. If this step proves to be unsatisfactory, we reduce the distance measure and try again."


SCALING: "Some optimization algorithms, such as steepest descent, are sensitive to poor scaling,while others, such as Newton’s method, are unaffected by it.", "Generally speaking, it is easier to preserve scale invariance for line search algorithms than for trust-region algorithms"


- RATES OF CONVERGENCE: linear, Q-superlinear, Q-quadratic

(différent de R-RATES OF CONVERGENCE)


# Chapter 3 - Line Search Methods
