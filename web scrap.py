from bs4 import BeautifulSoup
import requests
import csv

url = input("Enter the url of the website: ")

if not url:
    print("Error url cannot be empty")
else:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string

    h1_tags = soup.find_all('h1')

    anchor_tags = soup.find_all('a')

    available_posts = min(len(h1_tags), len(anchor_tags))

    num_posts = int(input(f"How many blogs you would like to scrap? (Available {available_posts})"))

    if num_posts > available_posts:
        print("Error: Number of blog post exceeds the available count")
    else:
        data_list = []

        for h1 in h1_tags:
            for anchor in anchor_tags:
                if anchor.text.strip() == h1.text.strip():
                    data_list.append({"Title": h1.text.strip(), "URL": anchor['href']})

        
        csv_file = "blogs_urls.csv"

        with open(csv_file, "w", newline='') as file:

            fieldnames = ["Title", "URL"]

            writer= csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for data in data_list:
                writer.writerow(data)

        print("Blog URLS have been scrapped and svaed to", csv_file)