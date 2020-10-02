# 信息增益

我们刚说完信息熵，下面就让我们来看一下什么是信息增益。

我们假设某个离散属性的取值为：

$$
\left\{a^{1}, a^{2}, a^{3}, \ldots a^{V}\right\}
$$

$$A^{v}$$代表所有样本在属性$$a$$上取值为$$a^{v}$$的样本集合。

那么以属性A对数据集D进行划分，所得到的信息增益为：

$$
\operatorname{Gain}(D, A)=\operatorname{H}(D)-\underbrace{\sum_{v=1}^{V} \frac{\left|A^{v}\right|}{|D|} \operatorname{H}\left(A^{v}\right)}_{按照属性a划分之后的信息熵的和}
$$

其中代表按照属性$$a$$划分之前的信息熵，$$\frac{\left|A^{v}\right|}{|D|}$$代表属性$$a$$取值为v时在所有样本中所占的权重，样本越多代表当前属性的这个取值越重要。**一般而言，信息增益越大，则意味着使用属性**$$a$$**来进行划分所获得的“纯度提升”越大。**

我们还是用之前西瓜的那个例子来说明，假设我们以色泽属性进行分割，那么就对应着三个数据子集：

* $$A^{1}$$代表青绿色，对应的数据编号为$$ \{ 1,4,6,10,13,17 \} $$，共有6个样本，其中正例3个，负例3个。
* $$A^{2}$$代表乌黑色，对应的数据编号为$$ \{2,3,7,8,9,15\}$$ ，共有6个样本，其中正例4个，负例2个。
* $$A^{3}$$代表浅白色，对应的数据编号为$$ \{5,11,12,14,16\}$$，共有5个样本，其中正例1个，负例4个。

_正例仍代表好瓜与负例仍代表坏瓜。_

则按照色泽进行划分之后的到的信息熵分别为：

$$
\begin{array}{l}
\operatorname{H}\left(A^{1}\right)=-\left(\frac{3}{6} \log _{2} \frac{3}{6}+\frac{3}{6} \log _{2} \frac{3}{6}\right)=1.000 \\
\operatorname{H}\left(A^{2}\right)=-\left(\frac{4}{6} \log _{2} \frac{4}{6}+\frac{2}{6} \log _{2} \frac{2}{6}\right)=0.918 \\
\operatorname{H}\left(A^{3}\right)=-\left(\frac{1}{5} \log _{5} \frac{1}{5}+\frac{4}{5} \log _{5} \frac{4}{5}\right)=0.722
\end{array}
$$

则根据属性色泽划分之后的信息增益为：

$$
\begin{aligned}
\operatorname{Gain}(D, 色泽) &=\operatorname{H}(D)-\sum_{v=1}^{3} \frac{\left|A^{v}\right|}{|D|} \operatorname{H}\left(A^{v}\right) \\
&=0.998-\left(\frac{6}{17} \times 1.000+\frac{6}{17} \times 0.918+\frac{5}{17} \times 0.722\right) \\
&=0.109
\end{aligned}
$$



