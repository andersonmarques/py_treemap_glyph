
import sys
import pygame

# Função para calcular o pior aspect ratio de uma lista de retângulos
def worst(row, w):
    if len(row) == 0:
        return 0
    a = max(row) * w ** 2 / sum(row) ** 2
    b = sum(row) ** 2 / (max(row) * w) ** 2
    aspect_ratio = max(a, b)
    return aspect_ratio

# Função para calcular o menor lado do retângulo restante
def width(row, w):
    return min(max(row), sum(row) ** 2 / (max(row) * w))

# Função para organizar os nós em uma nova linha
def layoutRow(row):
    row.sort(reverse=True)

# Função principal do algoritmo squarified
def squarify(children, row, w):
    """_summary_
    Está função é responsável por calcular a disposição dos retângulos squarified.
    Args:
        children (list): lista de nós com valores
        row (list): lista de retângulos
        w (float): largura do retângulo
    """
    if len(children) == 0:
        layoutRow(row)
        return

    c = children[0]
    if worst(row, w) <= worst(row + [c], w):
        squarify(children[1:], row + [c], w)
    else:
        layoutRow(row)
        squarify(children, [], width(row, w))

# Função para desenhar os retângulos na tela
def draw_rects(screen, rects, colors):
    for rect, color in zip(rects, colors):
        pygame.draw.rect(screen, color, rect)

# Função principal
def main():
    # Inicializar o Pygame
    pygame.init()
    
    # Configurações da janela
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Treemap Squarified")
    
    # Cores dos retângulos
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
    
    # Dados para o treemap (lista de nós com valores)
    children = [6, 6, 4, 3, 2, 2, 1]
    
    # Calcula as posições dos retângulos squarified
    rects = []
    squarify(children, [], width)
    total_area = sum(children)
    x, y = 0, 0

    for size in children:
        rect_width = (size / total_area) * width
        rect_height = (size / total_area) * height
        rects.append((x, y, rect_width, rect_height))
        if width > height:
            x += rect_width
        else:
            y += rect_height
        
    # Loop principal
    running = True
    while running:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Limpar a tela
        screen.fill((255, 255, 255))
        
        # Desenhar os retângulos na tela
        draw_rects(screen, rects, colors)
        
        # Atualizar a tela
        pygame.display.flip()
    
    # Encerrar o Pygame
    pygame.quit()
    sys.exit()

# Executar o programa
if __name__ == "__main__":
    main()
