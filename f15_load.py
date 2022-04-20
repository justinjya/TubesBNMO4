from .functions import*

def load():
    global user
    global game
    global kepemilikan
    global history

    while True:
        parser = argparse.ArgumentParser(prog = 'Load')
        parser.add_argument('folder', type = str)
        if length(sys.argv) == 1:
            print('Tidak ada nama folder yang diberikan.')
        args = parser.parse_args()
        folder = './saves/' + args.folder
        if not os.path.exists(folder):
            return print('Folder',args.folder,'tidak ditemukan.')

        print('Loading...')

        user = opencsv(folder,'user.csv')
        game = opencsv(folder,'game.csv')
        kepemilikan = opencsv(folder,'kepemilikan.csv')
        history = opencsv(folder,'riwayat.csv')
        return user, game, kepemilikan, history
