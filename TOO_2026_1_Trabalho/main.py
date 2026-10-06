from model.heroi import Heroi
from model.missao import Missao
from model.inimigo import Inimigo
from model.enums import ClasseHeroi, StatusMissao, TipoInimigo

def main():
    heroi = Heroi("Aragorn", ClasseHeroi.GUERREIRO, 100, 100, 25, 10)
    
    inimigo = Inimigo("Goblin", TipoInimigo.GOBLIN, 25, 50, 15, 0)
    
    missao = Missao("Salvar a aldeia", "Derrotar o Goblin", 100, StatusMissao.PENDENTE)
    missao.iniciar_missao()
    print(missao)
    inimigo.atacar(heroi)
    heroi.atacar(inimigo)
    missao.concluir_missao()
    print(missao)


    
main()