<h1>Trabalho Final | Algoritmo Branch and Bound</h1>

<p><strong>Descrição geral</strong>. Neste trabalho, vocês deverão implementar, em qualquer linguagem de programação, o
algoritmo branch-and-bound para problemas de programação linear inteira binária. A função objetivo será de
maximização e todas as restrições serão de “menor ou igual”, com exceção daquelas que definem o domı́nio
das variáveis. Não se espera que o(a) discente implemente um algoritmo para resolver os subproblemas (por
exemplo, o Simplex), mas que seja usado um pacote de programação linear para resolvê-los (por exemplo,
python-mip).</p>

<p><strong>Regra de ramificação</strong>. A regra de ramificação diz como criar os nós filhos a partir de um nó cuja solução
da relaxação linear é fracionária. O código de vocês deve ramificar em torno da variável x<sub>j</sub> cujo valor seja
fracionário e mais próximo de 0,5. Em um filho, adiciona-se a restrição x<sub>j</sub> = 1; no outro, a restrição x<sub>j</sub> = 0.
Estratégia de ramificação. A estratégia de ramificação determina como a árvore é explorada, ou seja, qual
será o próximo nó a ser resolvido. Vocês estão livres para implementar a estratégia que quiserem. Eis duas
sugestões de estratégia:
<ul>
    <li> Busca em profundidade. Para isso, basta utilizar uma pilha para armazenar os nós abertos (nós que ainda
não foram processados);</li>
    <li>Busca em largura (estratégia usada na aula). Para isso, basta utilizar uma fila para armazenar os nós
abertos.</li>
</ul>

<p><strong>Formato do arquivo.</strong>
O formato esperado para o arquivo será ilustrado a partir do problema abaixo:</p> <br>

$
    Max \space 5x_1 + 10x_2 + 8x_3
$

Sujeito a:

$$
3x_1 + 5x_2 + 2x_3 \leq 6 \\
4x_1 + 4x_2 + 4x_3 \leq 7 \\
x_1 , x_2, x_3 \in \lbrace{0, 1}\rbrace
$$

<p><strong>Formato do arquivo</strong></p> <br>

$$
3 \space 2 \\ 
5 \space 10 \space 8 \\
3 \space 5 \space 2 \space 6 \\
4\space 4\space 4\space 7 \\
$$