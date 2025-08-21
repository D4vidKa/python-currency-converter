from tkinter import *
from dados import *
def janela():
    janela = Tk()
    janela.title("Conversor de Moedas")
    janela.configure(bg="gray11")
    texto_menu = Label(janela, text="-----Menu Principal-----", bg="gray11", fg="white", font=("Arial", 16))
    texto_menu.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    botao_visualizar = Button(janela, text="Visualizar Cotações", bg="gray11", fg="springgreen1", font=("Arial", 12), command=lambda: janela2())
    botao_visualizar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    botao_converter = Button(janela, text="Converter Moedas", bg="gray11", fg="springgreen1", font=("Arial", 12), command=lambda: janela3())
    botao_converter.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    botao_sair = Button(janela, text="Sair", bg="gray11", fg="red1", font=("Arial", 12), command=janela.destroy)
    botao_sair.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    janela.mainloop()

def janela2():
    janela2 = Tk()
    janela2.title('Cotações Atualizadas')
    janela2.configure(bg="gray11")
    texto_cotacoes = Label(janela2, text="-----Cotações Atuais-----", bg="gray11", fg="white", font=("Arial", 16))
    texto_cotacoes.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    cotacao_dolar, cotacao_euro, cotacao_btc = cotação()
    texto_dolar = Label(janela2, text=f"Dólar: R$ {cotacao_dolar:.2f}", bg="gray11", fg="springgreen1", font=("Arial", 12))
    texto_dolar.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    texto_euro = Label(janela2, text=f"Euro: R$ {cotacao_euro:.2f}", bg="gray11", fg="springgreen1", font=("Arial", 12))
    texto_euro.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    texto_btc = Label(janela2, text=f"Bitcoin: R$ {cotacao_btc:.2f}", bg="gray11", fg="springgreen1", font=("Arial", 12))
    texto_btc.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    
    botao_fechar = Button(janela2, text="Voltar", bg="gray11", fg="white", font=("Arial", 12), command=janela2.destroy)
    botao_fechar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    janela2.mainloop()

def janela3():
    janela3 = Tk()
    janela3.title("Conversão de Moedas")
    janela3.configure(bg="gray11")
    
    texto_conversao = Label(janela3, text="-----Conversão de Moedas-----", bg="gray11", fg="white", font=("Arial", 16))
    texto_conversao.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    botao_dolar = Button(janela3, text="Converter Dólar", bg="gray11", fg="springgreen1", font=("Arial", 12), command=lambda: converter_moeda('Dólar'))
    botao_dolar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    botao_euro = Button(janela3, text="Converter Euro", bg="gray11", fg="springgreen1", font=("Arial", 12), command=lambda: converter_moeda('Euro'))
    botao_euro.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    botao_btc = Button(janela3, text="Converter Bitcoin", bg="gray11", fg="springgreen1", font=("Arial", 12), command=lambda: converter_moeda('Bitcoin'))
    botao_btc.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    botao_voltar = Button(janela3, text="Voltar", bg="gray11", fg="white", font=("Arial", 12), command=janela3.destroy)
    botao_voltar.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
    
    janela3.mainloop()

def converter_moeda(moeda):
    try:
        janela_conv = Tk()
        janela_conv.title(f"Converter {moeda}")
        janela_conv.configure(bg="gray11")
    except Exception as e:
        print(f"Erro ao abrir a janela de conversão: {e}")
        return
    texto_valor = Label(janela_conv, text=f"Digite o valor em {moeda}:".replace(',', '.'), bg="gray11", fg="white", font=("Arial", 12))
    texto_valor.grid(row=0, column=0, padx=10, pady=10)

    entrada_valor = Entry(janela_conv, bg="white", fg="black", font=("Arial", 12))
    entrada_valor.grid(row=0, column=1, padx=10, pady=10)

    def calcular():
        cotacao_dolar, cotacao_euro, cotacao_btc = cotação()
        try:
            valor = float(entrada_valor.get())
            if moeda == 'Dólar':
                resultado = valor * cotacao_dolar
            elif moeda == 'Euro':
                resultado = valor * cotacao_euro
            elif moeda == 'Bitcoin':
                resultado = valor * cotacao_btc
            else:
                resultado = 0
            Label(janela_conv, text=f"Valor em Reais: R$ {resultado:.2f}".replace('.', ','), bg="gray11", fg="springgreen1", font=("Arial", 12)).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        except ValueError:
            Label(janela_conv, text="Valor inválido!", bg="gray11", fg="red1", font=("Arial", 12)).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    botao_calcular = Button(janela_conv, text="Calcular", bg="gray11", fg="white", font=("Arial", 12), command=calcular)
    botao_calcular.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    botao_voltar = Button(janela_conv, text="Voltar", bg="gray11", fg="white", font=("Arial", 12), command=janela_conv.destroy)
    botao_voltar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    janela_conv.mainloop()
 # Call to initialize the conversion window for Dólar

