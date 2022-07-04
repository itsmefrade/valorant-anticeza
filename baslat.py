import pyautogui as pyag
import time


print(""" 
                                                              
                            _______                           
                            \  ___ `'.         __.....__      
     _.._                    ' |--.\  \    .-''         '.    
   .' .._|.-,.--.            | |    \  '  /     .-''''-.  `.  
   | '    |  .-. |    __     | |     |  '/     /________\   \ 
 __| |__  | |  | | .:--.'.   | |     |  ||                  | 
|__   __| | |  | |/ |   \ |  | |     ' .'\    .-------------' 
   | |    | |  '- `' __ | |  | |___.' /'  \    '-.____...---. 
   | |    | |      .'.''| | /_______.'/    `.             .'  
   | |    | |     / /   | |_\_______|/       `''-...... -'    
   | |    |_|     \ \._,\ '/                                  
   |_|             `--'  `'                                   
""")

# python indiriyoruz 
# cmdyi açıp py yazıyoruz.
# pip install pyautogui
# pip install time

def cl():
    print("Ateş etti.")
    pyag.click(1000,500) # Monitörünüzün boyutuna bağlı rastgele bir posizyon seçin.
    time.sleep(15)  # kaç saniyede bir vursun? 
    cl() # fonksiyonu tekrar çağırıyoruz tekrar etmesi için
#bu kadar

cl()
