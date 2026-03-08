# pdf_creator.py

from fpdf import FPDF
import os

def criar_pdf_dark_mode(texto, nome_arquivo):
    # Garante que o arquivo termine com .pdf
    if not nome_arquivo.lower().endswith('.pdf'):
        nome_arquivo += ".pdf"

    # --- TRATAMENTO DE UNICODE ---
    # As fontes padrão (Helvetica/Arial) só aceitam o encoding 'latin-1'.
    # O código abaixo remove emojis e caracteres especiais que fariam o programa travar.
    texto_processado = texto.encode("latin-1", errors="ignore").decode("latin-1")

    # Configurações de Estilo
    COR_FUNDO = (30, 30, 30)    # Dark mode (cinza escuro)
    COR_FONTE = (220, 220, 220) # Off-white
    LARGURA_PDF = 210           # mm
    FONTE_TAMANHO = 12
    MARGEM = 15
    ALTURA_LINHA = 8

    # Passo 1: Calcular a altura necessária
    pdf_temp = FPDF()
    pdf_temp.add_page()
    pdf_temp.set_font("helvetica", size=FONTE_TAMANHO) 
    
    largura_util = LARGURA_PDF - (MARGEM * 2)
    
    # Usando o texto processado para o cálculo
    linhas = pdf_temp.multi_cell(largura_util, ALTURA_LINHA, texto_processado, dry_run=True, output="LINES")
    
    # Cálculo da altura dinâmica
    altura_total = (len(linhas) * ALTURA_LINHA) + (MARGEM * 2)

    # Passo 2: Criar o PDF real
    pdf = FPDF(unit="mm", format=(LARGURA_PDF, altura_total))
    pdf.set_auto_page_break(False)
    pdf.add_page()

    # Pintar o fundo
    pdf.set_fill_color(*COR_FUNDO)
    pdf.rect(0, 0, LARGURA_PDF, altura_total, style='F')

    # Configurar texto
    pdf.set_text_color(*COR_FONTE)
    pdf.set_font("helvetica", size=FONTE_TAMANHO)
    
    # Inserir o conteúdo processado
    pdf.set_xy(MARGEM, MARGEM)
    pdf.multi_cell(largura_util, ALTURA_LINHA, texto_processado, align='L')

    # Salvar
    pdf.output(nome_arquivo)
    print("\n" + "-" * 30)
    print(f"🚀 Sucesso! Arquivo gerado: {os.path.abspath(nome_arquivo)}")
    print("-" * 30)

if __name__ == "__main__":
    print("--- GERADOR DE PDF INFINITO (DARK MODE) ---")
    
    # INTERAÇÃO NO TERMINAL
    nome_final = input("Escolha o nome final do seu arquivo (ex: meu_texto): ").strip()
    
    if not nome_final:
        nome_final = "arquivo_generico.pdf"

    # CORREÇÃO: Agora ele pergunta o texto no terminal!
    print("\nDigite ou cole o texto para o PDF (Pressione Enter + Ctrl+D ou Ctrl+Z para finalizar):")
    
    # Essa parte permite que você cole várias linhas de uma vez
    import sys
    meu_texto = sys.stdin.read()
    
    if meu_texto.strip():
        criar_pdf_dark_mode(meu_texto, nome_final)
    else:
        print("❌ Nenhum texto inserido. Operação cancelada.")
