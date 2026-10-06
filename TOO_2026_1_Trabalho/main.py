from model.heroi import Heroi
from model.missao import Missao
from model.inimigo import Inimigo
from model.enums import ClasseHeroi, TipoInimigo

def main():
    heroi = Heroi("Aragorn", ClasseHeroi.GUERREIRO, 100, 100, 20, 10)
    
    inimigo = Inimigo("Goblin", TipoInimigo.GOBLIN, 50, 50, 15, 5)
    
    missao = Missao("Salvar a aldeia", "Derrotar o Goblin", 100)

    print(missao)


    
main()