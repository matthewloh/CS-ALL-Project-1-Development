        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=16, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=17, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
