import mido

def main():
    port = mido.open_input('Arturia KeyStep 37:Arturia KeyStep 37 MIDI 1 36:0')
    while True:
        for msg in port.iter_pending():
            print(dir(msg))
            print(msg.type)

if __name__ == "__main__":
    main()
