for x in range(32):
    Grid.columnconfigure(window, x, weight=1, uniform='row')
    Label(width=1, bg=PINK).grid(row=0, column=x, sticky=N+S+E+W)
for y in range(18):
    Grid.rowconfigure(window, y, weight=1, uniform='row')
    Label(width=1, bg=PINK).grid(row=y, column=0, sticky=N+S+E+W)
