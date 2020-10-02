# ID3

我们根据刚才的信息增益来计算一下按照其他属性分割得到的信息增益

$$
\begin{array}{ll}
\operatorname{Gain}(D, 根蒂)=0.143 & \operatorname{Gain}(D, 敲声)=0.141 \\
\operatorname{Gain}(D, 纹理)=0.381 & \operatorname{Gain}(D, 脐部)=0.289 \\
\operatorname{Gain}(D, 触感)=0.006 & \operatorname{Gain}(D, 色泽)=0.109
\end{array}
$$

显然根据纹理进行分割是信息增益最大的，故首先按照纹理来划分样本

![](../../.gitbook/assets/image%20%286%29.png)

![](../../.gitbook/assets/image%20%283%29.png)

之后决策树将对每个分支节点做进一步划分，以上图第一个分支节点\(“纹理=清晰”\)为例，对该节点包含的样本集合$$D^{1}$$有编号$$\{1,2，3，4，5，6，8，10，15\}$$的9个样例，可用属性集合为$$\{色泽，根蒂，敲声，脐部，触感\}$$。基于$$D^{1}$$计算出各属性的信息增益：

$$
\begin{array}{ll}
\operatorname{Gain}(D^{1}, 色泽)=0.043 & \operatorname{Gain}(D^{1}, 根蒂)=0.458 \\
\operatorname{Gain}(D^{1}, 敲声)=0.331 & \operatorname{Gain}(D^{1}, 脐部)=0.458 \\
\operatorname{Gain}(D^{1}, 触感)=0.458
\end{array}
$$

根蒂，脐部，触感三个属性取得了最大的信息增益，可任选其中之一作为划分属性。类似的，对每个分支节点进行上述操作，最终的到完整的决策树。

![](../../.gitbook/assets/image%20%288%29.png)

![](../../.gitbook/assets/image%20%2815%29.png)

但是信息增益存在一个问题，那就是如果按照这种方法进行计算的话，那假如某个属性具有好多个取值，甚至是把编号作为属性了，按照这种情况计算就会导致决策树创建之后效果并不好，所以才引入了信息增益率也就是C4.5。

