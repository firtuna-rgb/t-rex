import random
WIDTH=600
HEIGHT=600
FLOOR=500
cactuses=['cactus1','cactus2','cactus3','cactus4','cactus5']
random_cactus=random.choice(cactuses)
trex=Actor('idle')
trex.pos=30,FLOOR
cactus=Actor(random_cactus)
cactus.pos=450,FLOOR
speed=1
score=0
penalty=0
jump_height=FLOOR-200
fall_speed=3
trex_pose=['run1','run2']
x=0
best_score=0
frames_per_image=15
def draw():
    global penalty
    screen.fill((255,255,255)) #this gives me white color
    screen.blit('floor-1',(5,510))
    trex.draw()
    cactus.draw()
    if penalty>=10:
        screen.draw.text(str(score),(420,5),color='red')
    else:
        screen.draw.text(str(score),(420,5),color='black')
    if best_score>0:
        best_score_text=f"your best score is {str(best_score)}"
        screen.draw.text(best_score_text,(40,550),color='black')
def update():
    global speed,score,x,frames_per_image,penalty,best_score
    cactus.left-=speed
    if penalty>=10:
        sounds.point.play()
        score-=1/60
    else:
        score+=1/60
    score=round(score,2)
    trex.image=trex_pose[x//frames_per_image]
    x+=1
    if x//frames_per_image>=len(trex_pose):
        x=0
    if cactus.left<-10:
        cactus.pos=450,FLOOR
        cactus.image=random.choice(cactuses)
        speed+=0.1
    if trex.colliderect(cactus):
        if score>best_score: #when my score goes above the best score, update the best_score as score
            best_score=score
        score=0
        sounds.point.play()
    if trex.y<FLOOR:
        penalty+=1/60
        trex.y+=fall_speed
    elif trex.y==FLOOR:
        penalty=0
        trex.y=FLOOR

def on_key_down():
    if keyboard.space:
        trex.y=jump_height