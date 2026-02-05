from bs4 import BeautifulSoup
import requests

#googledoc = requests.get('https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub')
googledoc_test = requests.get('https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub')

def print_secret_code(url):
    '''Retrieve table rows from google doc'''
    soup = BeautifulSoup(url.text, 'html.parser')
    table = soup.find('table')
    #print(table.prettify())
    rows = table.find_all('tr')
    n_cols = len(rows[0].find_all('td'))

    '''Parse table cell values from table html'''
    table_values = []
    for row in rows:
         columns = row.find_all('td')
         for col in columns:
             value = col.find('span')
             table_values.append(value.text)

    '''Put rows into sublists'''
    row_list = []
    row_values = []
    while len(table_values) > 0:
        value = table_values[0]
        table_values.pop(0)
        row_values.append(value)
        if len(row_values) == n_cols:
            row_list.append(row_values)
            row_values = []

    '''Identify position of columns'''
    x_pos = row_list[0].index("x-coordinate")
    y_pos = row_list[0].index("y-coordinate")
    char_pos = row_list[0].index("Character")

    '''Create dictionary of characters based on coordinate tuple'''
    coord_dict = {}
    max_x, max_y = 0, 0
    for item in row_list[1:]:
        coord_dict[(int(item[x_pos]),int(item[y_pos]))] = item[char_pos]
        if max_x < int(item[x_pos]):
            max_x = int(item[x_pos])
        if max_y < int(item[y_pos]):
            max_y = int(item[y_pos])

    '''Print upper case characters'''
    for y in range(max_y,-1,-1):
        line = ""
        for x in range(0,max_x+1):
            try:
                line = line + coord_dict[(x,y)]
            except KeyError:
                line = line + " "
        print(line.upper())

print_secret_code(googledoc_test)
