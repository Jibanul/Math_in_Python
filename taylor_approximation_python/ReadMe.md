## Example: Taylor Approximation of cos function

The Taylor series of a real or complex-values function f(x) that is infinitely differentialble at a real complex number a is the power series

<img src="http://latex.codecogs.com/svg.latex?f(a)&space;&plus;&space;\frac{f^{'}(a)}{1!}(x-a)&space;&plus;&space;\frac{f^{''}(a)}{2!}(x-a)^{2}&space;&plus;&space;\frac{f^{'''}(a)}{3!}(x-a)^{3}&space;&plus;&space;..." />

Let, f(x) = cos(x) at x = 0, f(0) = cos(0) = 1

The derivatives of f(x) are,

<img src="http://latex.codecogs.com/svg.latex?f^{'}(x)&space;=&space;-sin(x)&space;\Rightarrow&space;f^{'}(0)&space;=&space;0" title="http://latex.codecogs.com/svg.latex?f^{'}(x) = -sin(x) \Rightarrow f^{'}(0) = 0" />

<img src="http://latex.codecogs.com/svg.latex?f^{''}(x)&space;=&space;-cos(x)&space;\Rightarrow&space;f^{''}(0)&space;=&space;-1" title="http://latex.codecogs.com/svg.latex?f^{''}(x) = -cos(x) \Rightarrow f^{''}(0) = -1" />

<img src="http://latex.codecogs.com/svg.latex?f^{'''}(x)&space;=&space;sin(x)&space;\Rightarrow&space;f^{'''}(0)&space;=&space;0" title="http://latex.codecogs.com/svg.latex?f^{'''}(x) = sin(x) \Rightarrow f^{'''}(0) = 0" />

<img src="http://latex.codecogs.com/svg.latex?f^{''''}(x)&space;=&space;cos(x)&space;\Rightarrow&space;f^{''''}(0)&space;=&space;1" title="http://latex.codecogs.com/svg.latex?f^{''''}(x) = cos(x) \Rightarrow f^{''''}(0) = 1" />

The cycle repeats itself.

Therefore, the taylor series of cos(x) at x = 0is

<img src="http://latex.codecogs.com/svg.latex?f(x)&space;=&space;1&space;-&space;\frac{x^{2}}{2!}&space;&plus;&space;\frac{x^{4}}{4!}&space;-&space;...&space;=&space;\sum_{n=0}^{\infty}&space;(-1)^{n}&space;\frac{x^{2n}}{(2n)!}" title="http://latex.codecogs.com/svg.latex?f(x) = 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - ... = \sum_{n=0}^{\infty} (-1)^{n} \frac{x^{2n}}{(2n)!}" />


![](results/cos_result.gif)
