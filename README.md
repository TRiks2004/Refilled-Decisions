$$\frac{x - a}{b - a} = \frac{f(x) - f(a)}{f(b) - f(a)} \,\,\,| * (b - a)$$

### Ход итерации

$$x_0 = a - \frac{f(a)}{f(b) - f(a)} * (b - a) $$
$$x_1 = a - \frac{f(a)}{f(b) - f(x_0)} * (b - x_0) $$
$$x_2 = a - \frac{f(a)}{f(b) - f(x_1)} * (b - x_1) $$

$$...$$

$$x_n = a - \frac{f(a)}{f(b) - f(x_{n-1})} * (b - x_{n-1}) $$

### Точность

$$|x_n - x_{n-1}| \leq \epsilon $$