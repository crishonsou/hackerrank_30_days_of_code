import sys


## Definir a classe Node
class Node: 
    def __init__(self, data): ## Iniciar a função, com os parametros self, data
        self.right = self.left = None 
        self.data = data


## Definir a classe solution
class Solution:
    def insert(self, root, data): ## Definir a função insert, para analisar os dados
        if root is None: ## Condição de parada (Se a raiz é igual a zero
            return Node(data) ## Retorna o nó
        else: ## Senão
            if data <= root.data: ## Se os dados forem menores que os dados da raiz
                cur = self.insert(root.left, data) ## utiliza a classe node, insere os dados da esquerda da raiz na variavel cur
                root.left = cur ## raiz esquerda será igual a variavel cur
            else: ## Senão
                cur = self.insert(root.right, data) ## utiliza a classe node, indere os dados da direita da raiz na variavel cur
                root.right = cur ## raiz direita será igual a variavel cur
        return root ## retorna a raiz

    def levelOrder(self, root): ## Define a função de nível da raiz
        queue = [root] ## variavel de busca (queue) é igual a raiz
        while len(queue) is not 0: ## enquanto o cumprimeiro da variável de busca é menor que 0 
            curr = queue[0] ## variavel curr será igual a posição 0 da variavel de busca
            queue = queue[1:] ## variavel de busca é atualizada, da posição 1 do index até o final
            print(str(curr.data) + " ", end="") ## imprime a string contendo os dados da variável curr

            if curr.left is not None: ## se a classe de dados curr.left não é igual a 0
                queue.append(curr.left) ## Adiciona o resultado na variavel de busca da esquerda
            if curr.right is not None: ## Se a classe de dados curr.right não é igual a zero
                queue.append(curr.right) ## Adiciona o resultado na variável de busca da direita


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
