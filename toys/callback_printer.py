import mido

def print_message(message):
    print(message)

def main():
    port = mido.open_input('Arturia KeyStep 37:Arturia KeyStep 37 MIDI 1 36:0', callback=print_message)
    while True:
        pass

if __name__ == "__main__":
    main()
