from flask import Flask, render_template, request

app = Flask(__name__)

# Rota principal para exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para calcular a média das notas
@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        # Pega os valores das notas do formulário
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])

        # Calcula a média
        media = (nota1 + nota2 + nota3) / 3

        # Verifica se o aluno passou ou reprovou
        status = "Aprovado" if media >= 6 else "Reprovado"
        
        # Renderiza o resultado
        return render_template('index.html', media=media, status=status)
    except ValueError:
        return render_template('index.html', error="Por favor, insira valores numéricos válidos para as notas.")

if __name__ == '__main__':
    app.run(debug=True)
