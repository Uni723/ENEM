from PIL import Image
import os

# Pastas
pasta_entrada = "metades"
pasta_saida = "metade recortadas"

# Cria a pasta de saída se não existir
os.makedirs(pasta_saida, exist_ok=True)

# Loop pelos arquivos da pasta
for nome_arquivo in os.listdir(pasta_entrada):
    if nome_arquivo.lower().endswith((".png", ".jpg", ".jpeg")):
        caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
        imagem = Image.open(caminho_entrada)

        largura, altura = imagem.size

        # Verifica se é uma imagem da direita ou da esquerda
        if "direita" in nome_arquivo.lower():
            # Corta 25 pixels da esquerda
            caixa_corte = (25, 0, largura, altura)
        elif "esquerda" in nome_arquivo.lower():
            # Corta 25 pixels da direita
            caixa_corte = (0, 0, largura - 25, altura)
        else:
            # Se não tiver "direita" ou "esquerda", pula
            print(f"Ignorado: {nome_arquivo} (sem 'direita' ou 'esquerda' no nome)")
            continue

        imagem_cortada = imagem.crop(caixa_corte)

        caminho_saida = os.path.join(pasta_saida, nome_arquivo)
        imagem_cortada.save(caminho_saida)

print("Corte das bordas concluído com sucesso!")
