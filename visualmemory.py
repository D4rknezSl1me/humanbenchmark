import pyautogui as pag
import time
def get_pos(top_left, bot_right):
    width = (bot_right[0]-top_left[0]//2)
    height = (bot_right[1]-top_left[1]//2)

    positions = [
        (top_left[0],       top_left[1]),
        (top_left[0]+width, top_left[1]),
        (bot_right[0],      top_left[1]),
        (top_left[0],      top_left[1]+height),
        (top_left[0]+width, top_left[1]+height),
        (bot_right[0],      top_left[1]+height),
        (top_left[0],       bot_right[1]),
        (top_left[0]+width, bot_right[1]),
        (bot_right[0],      bot_right[1])
    ]
    
    return positions

top_left = (742, 332)
bot_right = (1212, 800)
positions = get_pos(top_left, bot_right)
print(positions)
flash_list = []
last_flash_time = None

try:
    while True:
        for idx, pos in enumerate(positions):
            if pag.pixelMatchesColor(pos[0], pos[1], (255, 255, 255)):
                if len(flash_list) == 0 or flash_list[-1] !=idx:
                    flash_list.append(idx)
                    last_flash_time = time.time()

        if last_flash_time and (time.time()-last_flash_time) >= 3:
            for idx in flash_list:
                pag.click(positions[idx][0], positions[idx][1])
            
            flash_list.clear()
            last_flash_time = None
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Terminated by User")