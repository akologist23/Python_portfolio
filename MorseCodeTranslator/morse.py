class Morse:

    def __init__(self):
        pass

    def load_morse_map(self):
        with open("morse.csv") as csvfile:
            morse_dict = {}
            lines = csvfile.readlines()
            clean_lines = [line.strip() for line in lines]
            for line in clean_lines:
                m_sep = line.split(",")
                morse_dict[m_sep[0]] = m_sep[1]
        return morse_dict


