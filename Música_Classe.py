import os


def main():
     os.system('cls')
     programa()

def programa():
    class Musica:
        musicas = []

        def __init__(self, nome='', artista='', duracao=''):
            self.nome = nome
            self.artista = artista
            self.duracao = duracao
            Musica.musicas.append(self)

        def __str__(self):
            return f'{self.nome} | {self.artista}'

        
        def listar_musicas():
            for musica in Musica.musicas:
                print(f'{musica.nome:<20} | {musica.artista:<20} | {musica.duracao}')

    musica1 = Musica('Under Pressure', 'Queen & David Bowie', duracao=248)
    musica2 = Musica('The Trooper', 'Iron Maiden', duracao=245)
    musica3 = Musica('Hotel California', 'Eagles', duracao=390)

    Musica.listar_musicas()


if  __name__ == '__main__':
        main()