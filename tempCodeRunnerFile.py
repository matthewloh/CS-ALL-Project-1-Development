self.frames = {}

        for F in (
                RegistrationPage, #SignInPage, HomePage, SearchPage, EventViewPage, EventManagePage, MorePage 
                ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
