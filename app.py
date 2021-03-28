import pyautogui
import tkinter as tk

def KeyMap(key):
    return{
        "1": "a",
        "2": "s",
        "3": "d",
        "4": "f",
        "5": "g",
        "6": "h",
        "7": "j",
        "1'": "q",
        "2'": "w",
        "3'": "e",
        "4'": "r",
        "5'": "t",
        "6'": "y",
        "7'": "u",
        "'":" ",
        " ": " ",
    }[key]


def playMusic(text):
    arr = text
    flag = 0
    for i in range(0,len(arr)):
        key = ""
        if flag == 1:
            flag= 0
            continue
        if arr[i+1] == "'":
            flag = 1
            key = KeyMap(str(arr[i]+arr[i+1]))
        else:
            key = KeyMap(arr[i])
        pyautogui.typewrite(key,  interval=0.25)

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        self.button = tk.Button(self, command=self.buttonClick)
        self.button["text"] = "PLAY"
        self.button.grid(row=0, column=0, sticky=tk.N+tk.W)
        
        self.text = tk.Text(self)
        self.text["height"] = 10
        self.text["width"] = 50
        self.text.grid(row=9, column=0, sticky=tk.N+tk.W)
    def buttonClick(self):
        playMusic(self.text.get("1.0",'end-1c') )
          
root = tk.Tk()
root.title("Genshin Impact Player By Ryan.Chen")
app = Application(root)
root.mainloop()
print(root.get_text())

  


# f = open("sheet.txt","r")
# arr = f.read()
# flag = 0
# for i in range(0,len(arr)):
#     key = ""
#     if flag == 1:
#         flag= 0
#         continue
#     if arr[i+1] == "'":
#         flag = 1
#         key = KeyMap(str(arr[i]+arr[i+1]))
#     else:
#         key = KeyMap(arr[i])
#     pyautogui.typewrite(key,  interval=0.25)