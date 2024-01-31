## Meu Jogo da Velha by Ramon
## Um jogo criado com a ajuda do Chat GPT


import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        # Inicializar variáveis do jogo e do placar
        self.jogador_atual = "X"
        self.tabuleiro = [""] * 9
        self.placar_x = {"vitorias": 0}
        self.placar_o = {"vitorias": 0}
        self.rodadas = 0  # Inicializando o contador de rodadas em zero

        # Criar rótulo para o contador de rodadas
        self.rotulo_rodadas = tk.Label(root, text=f"Rodadas: {self.rodadas}", font=("Helvetica", 12))
        self.rotulo_rodadas.grid(row=0, column=1, pady=10)

        # Criar rótulos para o placar
        self.rotulo_placar_x = tk.Label(root, text="Jogador X\nVitórias: 0", font=("Helvetica", 12), justify="left")
        self.rotulo_placar_x.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.rotulo_placar_o = tk.Label(root, text="Jogador O\nVitórias: 0", font=("Helvetica", 12), justify="right")
        self.rotulo_placar_o.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        # Criar botões do tabuleiro
        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(root, text="", font=("Helvetica", 20, "bold"), width=6, height=3, command=lambda row=i, col=j: self.clique_botao(row, col), bg="#eeeeee", activebackground="#eeeeee", borderwidth=2, relief="groove")
                botao.grid(row=i + 1, column=j, padx=5, pady=5)
                linha.append(botao)
            self.botoes.append(linha)

        # Botão de reiniciar o jogo
        self.botao_reset = tk.Button(root, text="Reiniciar Jogo", font=("Helvetica", 12), command=self.resetar_jogo, bg="#eeeeee", activebackground="#eeeeee", borderwidth=2, relief="groove")
        self.botao_reset.grid(row=4, column=0, columnspan=3, pady=10)

    def clique_botao(self, row, col):
        if not self.tabuleiro[3 * row + col]:
            self.tabuleiro[3 * row + col] = self.jogador_atual
            self.botoes[row][col].config(text=self.jogador_atual, state="disabled", disabledforeground="#3498db" if self.jogador_atual == "X" else "#e74c3c")

            if self.verificar_vitoria():
                self.atualizar_placar(True)
                messagebox.showinfo("Fim do Jogo", f"O jogador {self.jogador_atual} venceu!")
                self.resetar_jogo()
            elif "" not in self.tabuleiro:
                self.atualizar_placar(False)
                messagebox.showinfo("Fim do Jogo", "O jogo terminou em empate!")
                self.resetar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self):
        # Verificar linhas, colunas e diagonais
        for i in range(3):
            if self.tabuleiro[i * 3] == self.tabuleiro[i * 3 + 1] == self.tabuleiro[i * 3 + 2] != "":
                return True
            if self.tabuleiro[i] == self.tabuleiro[i + 3] == self.tabuleiro[i + 6] != "":
                return True
        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != "":
            return True
        if self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != "":
            return True
        return False

    def atualizar_placar(self, vitoria):
        if vitoria:
            if self.jogador_atual == "X":
                self.placar_x["vitorias"] += 1
            else:
                self.placar_o["vitorias"] += 1

        self.rotulo_placar_x.config(text=f"Jogador X\nVitórias: {self.placar_x['vitorias']}")
        self.rotulo_placar_o.config(text=f"Jogador O\nVitórias: {self.placar_o['vitorias']}")

    def resetar_jogo(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text="", state="normal")
                self.tabuleiro = [""] * 9
                self.jogador_atual = "X"

        self.rodadas += 1
        self.rotulo_rodadas.config(text=f"Rodadas: {self.rodadas}")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
