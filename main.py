from playlist_controller import PlaylistController

class Main:

    def __init__(self):
        self.playlist_controller = PlaylistController()

    def run(self):
        self.playlist_controller.run()
        self.playlist_controller.create_playlist("yuchuuu")

if __name__ == "__main__":
    # Instanz der MainProgram-Klasse erstellen und die run-Methode aufrufen
    main_program = Main()
    main_program.run()
