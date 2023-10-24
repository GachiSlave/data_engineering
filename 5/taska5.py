from bs4 import BeautifulSoup

with open('text_5_var_69') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_soup = soup.find_all("tr")

with open('result', "w") as file:
    for item in all_soup:
        str =''
        for i in item.text.split():
            str+=(i + ',')
        file.writelines(str[:-1]+ "\n")


