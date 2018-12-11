class Fila:
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

    def enfileirar(self, conteúdo):
        novo = self.Nó(conteúdo)

        if self.__primeiro is None:
            self.__primeiro = novo
            self.__último = novo
        else:
            self.__último.próximo = novo
            self.__último = novo
        self.__tamanho += 1
        self.__iterando = None

    def desenfileirar(self):

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

fila = Fila()
fila.enfileirar(1)
fila.enfileirar(23)
fila.enfileirar(43)
print(fila)
fila.desenfileirar()
fila.enfileirar(2)
print(fila)

for i in fila:
    print(i)
