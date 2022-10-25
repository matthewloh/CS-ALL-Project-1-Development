from tkinter import *
class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        # initialize the new_state
        self.new_state = 'normal'

        self.parent.bind('<Configure>', self._resize_handler)

    def _resize_handler(self, event):
        self.old_state = self.new_state # assign the old state value
        self.new_state = self.parent.state() # get the new state value

        if self.new_state == 'zoomed':
            print('maximize event')
        elif self.new_state == 'normal' and self.old_state == 'zoomed':
            print('restore event')
        else:
            print('dragged resize event')


root = Tk()
App(root).pack()
root.mainloop()