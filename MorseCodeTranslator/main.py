from morse import Morse

morse = Morse()
morse_map = morse.load_morse_map()

off = False
while not off:

    request = input("Please enter your message to convert to morse code: ")
    request_form  = request.upper().strip()

    if request_form.replace(" ","").isalnum():
        request_sep = request_form.split(" ")
        converted_message = []
        converted_word = []
        for word in request_sep:
            for letter in word:
                converted_word.append(morse_map[letter])
            converted_message.append(converted_word)
        print(converted_message)

        restart = False
        while not restart:
            request2 = input("To close program, enter 'c' else type 'm' to enter a new message: ")
            if request2.lower() == "c":
                restart = 'c'
                off = True
            elif request2.lower() == "m":
                break

    else:
        print("Please enter a valid message with alphanumeric characters only")






