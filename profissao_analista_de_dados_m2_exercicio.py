# -*- coding: utf-8 -*-
"""
---

# **Módulo** | Python: Estruturas de Dados
Caderno de **Exercícios**<br>
Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)

---

# **Tópicos**

<ol type="1">
  <li>Listas;</li>
  <li>Conjuntos;</li>
  <li>Dicionários.</li>
</ol>

---

# **Exercícios**

## 1\. Listas

Criei uma lista chamada `filmes` com o nome dos 10 primeiros filmes mais bem avaliados no site no [IMDB](https://www.imdb.com/chart/top/). Imprima o resultado.
"""

filmes = ["Um sonho de liberdade", "O poderoso chefão","Batman: O Cavaleiro das Trevas","O Poderoso Chefão II","12 Homens e uma Sentença"," A Lista de Schindler","O Senhor dos Anéis: O Retorno do Rei","Pulp Fiction - Tempo de Violência","O Senhor dos Anéis: A Sociedade do Anel","Três Homens em Conflito"]

"""Simule a movimentação do *ranking*. Utilize os métodos `insert` e `pop` para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.


"""

filme_bem_avaliado = filmes[1]
filmes.pop(1)
filmes.insert(1,filmes[0])

print("Filme removido da segunda posição: {}".format(filme_bem_avaliado))

filmes.pop(0)
filmes.insert(0,filme_bem_avaliado)

print("\nA nova posição de filmes é: {}".format(filmes))

"""---

## 2\. Conjuntos

Aconteceu um erro no seu *ranking*. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.
"""

contador = 0


print("1 - Quantidade de filmes no ranking: {}".format(len(filmes)))
print(filmes,"\n----------")

for contador in range(len(filmes)):
    if (contador == 7 or contador == 8 or contador == 9):
        filmes.append(filmes[contador])
        print("Filme repetido: {}".format(filmes[contador]))

    contador+=1

print("\n2 - Quantidade de filmes no ranking: {}".format(len(filmes)))
print(filmes)

"""Utiliza a conversão `set` e `list` para remover os valores duplicados. Imprima o resultado."""

print("Quantidade de filmes com duplicação: {}".format(len(filmes)))

filmes = set(filmes)

print("Quantidade de filmes sem duplicação: {}".format(len(filmes)))

"""---

## 3\. Dicionários

Repita os exercícios da parte 1 (listas). Os elementos da lista `filmes` devem ser dicionários no seguinte formato: `{'nome': <nome-do-filme>, 'ano': <ano do filme>, 'sinopse': <sinopse do filme>}`.
"""

filmes = ["Um sonho de liberdade", "O poderoso chefão","Batman: O Cavaleiro das Trevas","O Poderoso Chefão II","12 Homens e uma Sentença"," A Lista de Schindler","O Senhor dos Anéis: O Retorno do Rei","Pulp Fiction - Tempo de Violência","O Senhor dos Anéis: A Sociedade do Anel","Três Homens em Conflito"]

dicionario_filmes = []

dicionario_filmes.append(dict(nome="Um sonho de liberdade", ano="1994",sinopse="Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum."))
dicionario_filmes.append(dict(nome="O poderoso chefão",ano="1972",sinopse="O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante."))
dicionario_filmes.append(dict(nome="Batman: O Cavaleiro das Trevas",ano="2008",sinopse="Quando a ameaça conhecida como O Coringa surge de seu passado, causa estragos e caos nas pessoas de Gotham. O Cavaleiro das Trevas deve aceitar um dos maiores testes para combater a injustiça."))
dicionario_filmes.append(dict(nome="O Poderoso Chefão II",ano="1974",sinopse="Em 1950, Michael Corleone, agora à frente da família, tenta expandir o negócio do crime a Las Vegas, Los Angeles e Cuba. Paralelamente, é revelada a história de Vito Corleone, e de como saiu da Sicília e chegou a Nova Iorque."))
dicionario_filmes.append(dict(nome="12 Homens e uma Sentença",ano="1957",sinopse="O julgamento de um assassinato em Nova Iorque é frustrado por um único membro, cujo ceticismo força o júri a considerar cuidadosamente as evidências antes de dar o veredito."))
dicionario_filmes.append(dict(nome="A Lista de Schindler",ano="1993",sinopse="Na Polônia ocupada pelos alemães durante a Segunda Guerra Mundial, o industrial Oskar Schindler começa a ser preocupar com seus trabalhadores judeus depois de testemunhar sua perseguição pelos nazistas."))
dicionario_filmes.append(dict(nome="O Senhor dos Anéis: O Retorno do Rei",ano="2003",sinopse="Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de Frodo e Sam quando eles se aproximam á Montanha da Perdição com o Um Anel."))
dicionario_filmes.append(dict(nome="Pulp Fiction - Tempo de Violência",ano="1994",sinopse="As vidas de dois assassinos da máfia, um boxeador, um gângster e sua esposa, e um par de bandidos se entrelaçam em quatro histórias de violência e redenção."))
dicionario_filmes.append(dict(nome="O Senhor dos Anéis: A Sociedade do Anel",ano="2001",sinopse="Um manso hobbit do Condado e oito companheiros partem em uma jornada para destruir o poderoso Um Anel e salvar a Terra-média das Trevas."))
dicionario_filmes.append(dict(nome="Três Homens em Conflito",ano="1966",sinopse="Um impostor se junta com dois homens para encontrar fortuna num remoto cemitério."))

print(dicionario_filmes)

"""Exercício 2 - Parte 1

"Aconteceu um erro no seu ranking. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado."
"""

contador = 0

print("1 - Quantidade de filmes no ranking: {}".format(len(dicionario_filmes)))
print(dicionario_filmes,"\n","----------")

for contador in range(len(dicionario_filmes)):
    if (contador == 7 or contador == 8 or contador == 9):
        dicionario_filmes.append(dicionario_filmes[contador])
        print("Filme repetido: {}".format(dicionario_filmes[contador]["nome"]))

    contador+=1

print("\n2 - Quantidade de filmes no ranking: {}".format(len(dicionario_filmes)))
print(dicionario_filmes)