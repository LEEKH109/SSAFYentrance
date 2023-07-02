from tkinter import *

root = Tk() # Tk 객체를 생성합니다. 이것이 창을 만듭니다.
widget = Label(root, text='I love Python!') # root 창에 레이블을 추가합니다.
widget.pack() # pack() 메소드는 위젯의 크기를 가능한 작게 만든 후 위젯을 창에 추가합니다.

root.mainloop() # 이벤트 루프에 진입합니다.
