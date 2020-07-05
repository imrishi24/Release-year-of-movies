import imdb

ia=imdb.IMDb()

n=0
while(n<20):
    a=input("Enter the movie name to know its release year: ")
    search=ia.search_movie(a)
    year=search[0]['year']

    print(search[0]['title'] + ':'+ str(year))
    n=n+1
