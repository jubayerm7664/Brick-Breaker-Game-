import pygame, sys

pygame.init()
width, height = 400, 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker 🧱")
clock = pygame.time.Clock()

# Colors
bg = (30, 30, 60)
paddle_color = (0, 255, 0)
ball_color = (255, 0, 0)
brick_color = (255, 165, 0)
text_color = (255, 255, 255)

# Paddle
paddle = pygame.Rect(150, 260, 100, 10)
paddle_speed = 5

# Ball
ball = pygame.Rect(200, 150, 10, 10)
ball_speed = [4, -4]

# Bricks
bricks = [pygame.Rect(x*80, y*20, 78, 18) for y in range(3) for x in range(5)]

# Score
score = 0
font = pygame.font.SysFont("Arial", 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < width:
        paddle.right += paddle_speed

    # Move ball
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # Collisions
    if ball.left <= 0 or ball.right >= width:
        ball_speed[0] *= -1
    if ball.top <= 0:
        ball_speed[1] *= -1
    if ball.colliderect(paddle):
        ball_speed[1] *= -1
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed[1] *= -1
            score += 1

    # Game over / win
    if ball.bottom >= height:
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()
    if not bricks:
        print("You Win! Score:", score)
        pygame.quit()
        sys.exit()

    # Draw everything
    window.fill(bg)
    pygame.draw.rect(window, paddle_color, paddle)
    pygame.draw.rect(window, ball_color, ball)
    for brick in bricks:
        pygame.draw.rect(window, brick_color, brick)
    score_text = font.render(f"Score: {score}", True, text_color)
    window.blit(score_text, (5,5))

    pygame.display.flip()
    clock.tick(60)
