import pyautogui
#distance = 200
#while distance > 0:
#    pyautogui.drag(distance, 0,duration=0.2)   
#    distance -= 5 
#    pyautogui.drag(0, distance, duration=0.2)   
#    pyautogui.drag(-distance, 0, duration=0.2)  
#    distance -= 5
#    pyautogui.drag(0, -distance, duration=0.2)

r= None 
while r is None:
    Butt1 = pyautogui.locateAllOnScreen('C:\Temp\Git\Gitbash\Main\pyautogui\imagen1.png', grayscale=False)
    pyautogui.click(Butt1)
print (r)