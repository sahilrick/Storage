def bot():
    import time


    
    asknumber=int(input("Enter The Number u want to spam:"))
    name=input("Who u want to annoy?:")
    msg=input("Enter the message:")
    Bot=bakchodi(asknumber, msg, name)
    Bot.getWhatsapptoRuninBrowser()
    time.sleep(20)
    Bot.searchNigga()
    time.sleep(2)
    Bot.SpamThatNigger()
    
    
    
    

class bakchodi:
        

    def __init__(self, number, message,name):
        self.number=number
        self.message=message
        self.name=name
    def getWhatsapptoRuninBrowser(self):
        import webbrowser as randa
        url="web.whatsapp.com"
        chrome_path =r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        randa.register('chrome', None, randa.BackgroundBrowser(chrome_path))
        randa.get('chrome').open(url)


        
    def searchNigga(self):
        import time
        import pyautogui as randi
         #should be called after getting into site
        randi.click(x=110, y=188, clicks=1, interval=0, button="left")
        randi.typewrite(self.name)
        time.sleep(1)
        randi.click(x=179, y=319, clicks=1, interval=0, button="left")
        time.sleep(1)
        

        

        

        
    def SpamThatNigger(self):
        import pyautogui as randi
        import time
        

        for x in range(self.number):
            randi.click(x=565, y=692, clicks=1, interval=0, button="left")
            time.sleep(3)


            randi.typewrite(self.message)
            randi.click(x=1326, y=696, clicks=1,interval=0, button="left")


   
bot()
        
        
        
            
        

       
        
        

        

        
            

            

            

    
