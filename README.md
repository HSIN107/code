import pygame
import random
import time

# 初始化 Pygame
pygame.init()

# 設定遊戲視窗
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('打地鼠遊戲')

# 顏色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# 遊戲參數設定
MOLE_SIZE = 40
HOLE_SIZE = 60
score = 0
game_duration = 20  # 遊戲時間 20 秒
font = pygame.font.Font(None, 48)

# 設定洞的位置
holes = [
    (150, 150), (350, 150), (550, 150),
    (150, 350), (350, 350), (550, 350)
]

# 遊戲主迴圈
def game_loop():
    global score
    
    start_time = time.time()
    current_mole = random.choice(holes)
    last_mole_time = time.time()
    mole_duration = 1.0  # 地鼠顯示時間
    running = True
    
    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = max(0, game_duration - int(elapsed_time))
        
        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 檢查是否打中地鼠
                mouse_pos = pygame.mouse.get_pos()
                if hit_mole(mouse_pos, current_mole):
                    score += 1
                    current_mole = random.choice(holes)
                    last_mole_time = current_time
        
        # 更新地鼠位置
        if current_time - last_mole_time > mole_duration:
            current_mole = random.choice(holes)
            last_mole_time = current_time
        
        # 繪製畫面
        screen.fill(WHITE)
        
        # 繪製所有洞
        for hole in holes:
            pygame.draw.circle(screen, BROWN, hole, HOLE_SIZE)
        
        # 繪製地鼠
        pygame.draw.circle(screen, BLACK, current_mole, MOLE_SIZE)
        
        # 顯示分數和時間
        score_text = font.render(f"分數: {score}", True, BLACK)
        time_text = font.render(f"時間: {remaining_time}秒", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))
        
        # 更新顯示
        pygame.display.flip()
        
        # 檢查遊戲是否結束
        if remaining_time <= 0:
            show_game_over()
            running = False
        
def hit_mole(mouse_pos, mole_pos):
    return ((mouse_pos[0] - mole_pos[0]) ** 2 + 
            (mouse_pos[1] - mole_pos[1]) ** 2) < MOLE_SIZE ** 2

def show_game_over():
    screen.fill(WHITE)
    game_over_text = font.render("遊戲結束!", True, RED)
    final_score_text = font.render(f"最終分數: {score}", True, BLACK)
    
    screen.blit(game_over_text, 
                (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 
                 SCREEN_HEIGHT//2 - 50))
    screen.blit(final_score_text, 
                (SCREEN_WIDTH//2 - final_score_text.get_width()//2, 
                 SCREEN_HEIGHT//2 + 50))
    pygame.display.flip()
    time.sleep(3)  # 顯示 3 秒結果

# 開始遊戲
game_loop()
pygame.quit()
