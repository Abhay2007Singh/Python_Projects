import requests
from bs4 import BeautifulSoup
import csv

#  https://technohacks.co.in/internship-projects/
url=input("Enter the website url: ")

def responses(url,find):
    response = requests.get(url)
    #return response
    soup=BeautifulSoup(response.text, "html.parser")

    save=[]
    for i in soup.select("body"):
        #found=soup.find(find)
        found=i.select((find))#.text
        #save.append(found)

    return response, found


def save_to_csv(data, filename="Scraped.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
        
    return f"Data saved to {filename}"


def main():
    find = input("Enter the element to Search <Only give HTML tags>: ")
    response, found = responses(url,find)

    #print(f"Data found: {json.dumps(str(found), indent=4)}")

    try:
        data = response.status_code
        if data == 200:
            if not found:
                print("No data found")
            else:
                print(save_to_csv(found))
    except ValueError:
        print(f"{response.status_code} issue occurred Please Check the URL")


if __name__=="__main__":
    main()