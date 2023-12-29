import pyautogui as pag
import time

time.sleep(3)
text1 = "It was a smart little landau which rattled up to the door of Briony Lodge. As it pulled up, one of the loafing men at the corner dashed forward to open the door in the hope of earning a copper, but was elbowed away by another loafer, who had rushed up with the same intention. A fierce quarrel broke out, which was increased by the two guardsmen, who took sides with one of the loungers, and by the scissors-grinder, who was equally hot upon the other side. "
text2 = "So he huffed and he puffed and he blew the house down! The wolf was greedy and he tried to catch both pigs at once, but he was too greedy and got neither! His big jaws clamped down on nothing but air and the two little pigs scrambled away as fast as their little hooves would carry them. The wolf chased them down the lane and he almost caught them. But they made it to the brick house and slammed the door closed before the wolf could catch them."
pag.write(text2, interval=0)