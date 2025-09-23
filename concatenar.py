from PIL import Image
import os
import re

# Caminho da pasta onde as imagens estão
pasta_imagens = 'metade recortadas'

# Caminho da nova pasta para salvar as imagens concatenadas
pasta_saida = 'imagens_concatenadas'

# Criação da pasta de saída, caso ela não exista
os.makedirs(pasta_saida, exist_ok=True)

# Listar todos os arquivos PNG da pasta
arquivos_imagens = [f for f in os.listdir(pasta_imagens) if f.endswith('.png')]

# Expressão regular para extrair o número da página e o lado
padrao = re.compile(r'pagina_enem_(\d+)_(esquerda|direita)\.png')

# Dicionário para agrupar as imagens por número da página
paginas = {}

for arquivo in arquivos_imagens:
    match = padrao.match(arquivo)
    if match:
        numero_pagina = int(match.group(1))
        lado = match.group(2)
        if numero_pagina not in paginas:
            paginas[numero_pagina] = {}
        paginas[numero_pagina][lado] = arquivo

# Ordenar as páginas numericamente e organizar na ordem: esquerda, direita
imagens_ordenadas = []
for numero in sorted(paginas.keys()):
    if 'esquerda' in paginas[numero]:
        imagens_ordenadas.append(paginas[numero]['esquerda'])
    if 'direita' in paginas[numero]:
        imagens_ordenadas.append(paginas[numero]['direita'])

# Abrir as imagens na ordem correta
imagens = [Image.open(os.path.join(pasta_imagens, nome)) for nome in imagens_ordenadas]

# Calcular dimensões da imagem final (empilhamento vertical)
largura_maxima = max(img.width for img in imagens)
altura_total = sum(img.height for img in imagens)

# Criar nova imagem
imagem_final = Image.new('RGB', (largura_maxima, altura_total), color=(255, 255, 255))

# Colar imagens de cima para baixo
y_offset = 0
for img in imagens:
    imagem_final.paste(img, (0, y_offset))
    y_offset += img.height

# Salvar resultado
caminho_saida = os.path.join(pasta_saida, 'pagina_concatenada.png')
imagem_final.save(caminho_saida)

print(f'✅ Imagem concatenada salva com sucesso em: {caminho_saida}')
