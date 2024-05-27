import webbrowser
from random import choice
from urllib.parse import quote
import tkinter as tk

# Lista de saudações que o chatbot pode responder
saudacoes = ["Olá! Bem-vindo à nossa farmácia Dias.", "Oi, como posso ajudar você hoje?", "Olá! Em que posso ser útil?"]

# Lista de despedidas que o chatbot pode responder
despedidas = ["Até mais! Espero ter ajudado.", "Tchau! Volte sempre.", "Até logo! Tenha um dia saudável!"]

# Lista de respostas automáticas da farmácia
respostas_farmacia = ["Temos uma variedade de medicamentos para atender às suas necessidades.", 
                      "Nossa equipe está pronta para ajudar com suas dúvidas sobre medicamentos e saúde.", 
                      "Além de medicamentos, também oferecemos produtos de cuidados pessoais e bem-estar.",
                      "Você pode encontrar mais informações em nosso site: www.FarmaciaDias.com"]

# Dicionário de medicamentos e seus preços
medicamentos_precos = {
    "Paracetamol": 10.50,
    "Ibuprofeno": 8.25,
    "Dipirona": 7.80,
    "Omeprazol": 15.90,
    "Amoxicilina": 12.75
}

# Função para listar os medicamentos e preços
def listar_medicamentos_precos():
    mensagem = "Aqui estão alguns dos medicamentos que oferecemos e seus preços:\n"
    for medicamento, preco in medicamentos_precos.items():
        mensagem += f"- {medicamento}: R$ {preco:.2f}\n"
    return mensagem

# Função para responder às saudações do usuário
def responder_saudacao():
    return choice(saudacoes)

# Função para responder às despedidas do usuário
def responder_despedida():
    return choice(despedidas)

# Função para responder a outras mensagens do usuário
def responder_outro():
    resposta = choice(respostas_farmacia)
    return resposta

# Função para responder ao usuário com o preço de um medicamento específico
def responder_preco_medicamento(mensagem):
    for medicamento in medicamentos_precos.keys():
        if medicamento.lower() in mensagem.lower():
            return f"O preço de {medicamento.capitalize()} é R$ {medicamentos_precos[medicamento]:.2f}"
    return "Desculpe, não temos informações sobre o preço desse medicamento."

# Função para enviar mensagem do usuário e mostrar a resposta do chatbot na interface gráfica
def enviar_mensagem():
    mensagem_usuario = entry_usuario.get()
    if mensagem_usuario.lower() in ["oi", "olá", "hello", "oi!"]:
        resposta_bot = responder_saudacao()
    elif mensagem_usuario.lower() in ["tchau", "adeus", "até mais", "até logo"]:
        resposta_bot = responder_despedida()
    elif mensagem_usuario.lower() in ["preços", "medicamentos"]:
        resposta_bot = listar_medicamentos_precos()
    elif "preço do" in mensagem_usuario.lower():
        resposta_bot = responder_preco_medicamento(mensagem_usuario)
    else:
        # Redirecionar a pesquisa para o Google
        pesquisa_google = f"https://www.google.com/search?q={quote(mensagem_usuario)}"
        resposta_bot = "Realizando a pesquisa no Google..."
        webbrowser.open(pesquisa_google)
    conversa.config(state=tk.NORMAL)
    conversa.insert(tk.END, f"Você: {mensagem_usuario}\n")
    conversa.insert(tk.END, f"Bot: {resposta_bot}\n\n")
    conversa.config(state=tk.DISABLED)
    entry_usuario.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Chatbot da Farmácia Dias")

# Configuração da área de conversa
conversa = tk.Text(root, width=50, height=20)
conversa.config(state=tk.DISABLED)
conversa.pack(pady=10)

# Configuração da entrada de texto
entry_usuario = tk.Entry(root, width=50)
entry_usuario.pack(pady=10)

# Botão para enviar mensagem
btn_enviar = tk.Button(root, text="Enviar", command=enviar_mensagem)
btn_enviar.pack()

root.mainloop()
