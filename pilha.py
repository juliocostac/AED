class Pilha:
    def __init__(self):
        self.__primeiro = None
        self.__último = None
        self.__tamanho = 0
        self.__iterando = None

    class Nó:
        def __init__(self, conteúdo):
            self.próximo = None
            self.conteúdo = conteúdo

    def __len__(self):
        return self.__tamanho

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.__primeiro
        else:
            self.__iterando = self.__iterando.próximo

        if self.__iterando is not None:
            return self.__iterando.conteúdo

        raise StopIteration

    def __str__(self):
        retorno = "|"
        i = 0
        atual = self.__primeiro
        while i < len(self):
            retorno += atual.conteúdo.__repr__()
            if i < len(self) - 1:
                retorno += ", "

            atual = atual.próximo
            i += 1
        retorno += "|"
        return retorno

    def push(self, conteúdo):
        novo = self.Nó(conteúdo)

        if self.__primeiro is None:
            self.__primeiro = novo
            self.__último = novo
        else:
            novo.próximo = self.__primeiro
            self.__primeiro = novo
        self.__tamanho += 1
        self.__iterando = None
    def pop(self):

        if self.__primeiro is None:
            raise IndexError ("Error!")
        elif len(self) == 1:
            self.__primeiro = None
            self.__último = None
        else:
            proximo = self.__primeiro.próximo
            self.__primeiro.próximo = None
            self.__primeiro = proximo
        self.__tamanho -= 1
        self.__iterando = None

pilha = Pilha()

pilha.push(1)
pilha.push(23)
pilha.push(43)
print(pilha)

pilha.pop()
print(pilha)

pilha.push(2)
print(pilha)

for i in pilha:
    print(i)

