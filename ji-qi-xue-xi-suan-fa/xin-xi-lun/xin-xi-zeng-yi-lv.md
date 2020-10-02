# 信息增益率

说完信息增益，下面我们再来看一下什么是信息增益率。

信息增益率：

$$
\text { Gain_ratio }(D, A)=\frac{\operatorname{Gain}(D, A)}{\operatorname{IV}(A)}
$$

其中

$$
\operatorname{IV}(A)=-\sum_{v=1}^{V} \frac{\left|A^{v}\right|}{|D|} \log _{2} \frac{\left|A^{v}\right|}{|D|}
$$

属性$$A$$的可能取值越多即$$V$$越多，则$$IV(A)$$的值越大。

我们仍以西瓜数据集为例，计算一下信息增益率，首先我们来计算一下$$IV(A)$$：

$$
\operatorname{IV}(A)=-\left(\frac{6}{17} \log _{2} \frac{6}{17}+\frac{6}{17} \log _{2} \frac{6}{17}+ \frac{5}{17}\log _{2} \frac{5}{17}\right)=2.028
$$

接下来计算一下信息增益率：

$$
\begin{aligned}
\text { Gain_ratio }(D, A) &=\frac{\operatorname{Gain}(D, A)}{\operatorname{IV}(A)} \\
&=\frac{0.109}{2.028} \\
&=0.054
\end{aligned}
$$

