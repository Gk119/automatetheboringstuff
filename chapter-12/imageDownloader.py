import requests, bs4, os

os.chdir("chapter-12")
#site = input("Enter the site link: ")
tags = list(input("Enter the tags separated by space to search for the image in imgur: "))
res = requests.get('https://imgur.com/search?q=' + '+'.join(tags))
res.raise_for_status()

os.makedirs('imgur_search_result', exist_ok=True)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
nostarchSoup = soup.select('a[class="image-list-link"] img')

for x in nostarchSoup:
    imgUrl = 'http:' + x.attrs['src'] 
    print('Saving:  ' + os.path.basename(imgUrl))
    img = requests.get(imgUrl)
    img.raise_for_status()
    imageFile = open(os.path.join('imgur_search_result', os.path.basename(imgUrl)),'wb')
    for chunk in img.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
