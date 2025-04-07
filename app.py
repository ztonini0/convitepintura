import streamlit as st

# Função para verificar a resposta 2
def verificar_resposta_2(resposta_2):
    # Vamos considerar como resposta certa: "tita"
    if resposta_2.lower() == "tita":
        return True
    return False

# Definindo o código HTML e CSS para a animação
html_code = """
<html>
<head>
    <style>
        @keyframes openEnvelope {
            0% { transform: rotateX(0deg); }
            100% { transform: rotateX(180deg); }
        }

        @keyframes flyOut {
            0% { transform: translateY(0px); opacity: 0; }
            100% { transform: translateY(-100px); opacity: 1; }
        }

        .envelope {
            width: 200px;
            height: 120px;
            background-color: #f1f1f1;
            position: relative;
            border-radius: 10px;
            transition: transform 1s ease;
            transform-origin: top;
            margin: 50px auto;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }

        .envelope::before {
            content: "";
            position: absolute;
            top: -15px;
            left: 20px;
            width: 160px;
            height: 50px;
            background-color: #f1f1f1;
            clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
            transform-origin: center;
            animation: openEnvelope 2s forwards;
        }

        .letter {
            width: 180px;
            height: 100px;
            background-color: #fffae5;
            position: absolute;
            top: 10px;
            left: 10px;
            border-radius: 8px;
            opacity: 0;
            transform: translateY(0);
            animation: flyOut 2s forwards 2s;
        }

        .letter .text {
            font-family: Arial, sans-serif;
            font-size: 16px;
            color: #333;
            padding: 10px;
        }

        .text {
            font-size: 14px;
            line-height: 1.5;
        }

        .letter p {
            font-weight: bold;
            color: #333;
        }

    </style>
</head>
<body>
    <div class="envelope" id="envelope">
        <div class="letter" id="letter">
            <div class="text">
                <h3>Convite✨</h3>
                <p>Uma noite pintando uma tela juntos, conversando e se divertindo assistindo algo? 🖌️🎥🍿</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Título do aplicativo
st.title("Bem-vinda, Dona encrenca! 😎")

# Criar o formulário
st.subheader("Atenção, Júlia! Seu Vale-Date acabou de ser entregue... Agora preencha o formulário corretamente. 💌 ")

form = st.form(key="formulario")
campo_1 = form.text_input("Melhor qualidade de Júlia?", "")  # Não importa a resposta 1
campo_2 = form.text_input("Qual é o nome do felino mais bonitinho do mundo que reside com Júlia?", "")
submit_button = form.form_submit_button(label="Enviar")

# Verificar se a resposta 2 está correta
if submit_button:
    if verificar_resposta_2(campo_2):  # Verifica apenas a resposta 2
        # Exibe a carta após a verificação da resposta 2
        st.markdown(html_code, unsafe_allow_html=True)
        st.success("Parabéns, você acertou! A carta foi desbloqueada. 💖")
    else:
        st.error("Ops! Resposta incorreta. Tente novamente.")

st.subheader("Assinado: BATMAAAAAAAAAAAAAAAAAAAAAAAN. 🦇")
