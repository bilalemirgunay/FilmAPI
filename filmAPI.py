import requests

class MovieDb:
    def __init__(self):
        self.apiUrl = "https://api.themoviedb.org/3/"
        self.apiKey = "" #api keyi buraya yazın

    def getPopulars(self):
        response = requests.get(self.apiUrl+"movie/popular?api_key="+self.apiKey+"&language=tr-TR&page=1")
        return response.json()

    def searchMovie(self,film):
        response = requests.get(self.apiUrl+"search/movie?api_key="+self.apiKey+"&language=tr-TR&query="+film+"&page=1&include_adult=false")
        return response.json()

movieDb = MovieDb()

while True:
    secim = input("1- Popüler Filmler\n2- Film Ara\n3- Çıkış\nSeçim:")
    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieDb.getPopulars()
            for movie in movies["results"]:
                print("\nFilm Adı:" + movie["title"])
                print("Puanı:" , movie["vote_average"])
                print("Açıklama:" + movie["overview"])
                print("\n"+15*"*")
        
        if secim == "2":
            film = input("Film adını girin:")
            movies = movieDb.searchMovie(film)
            for movie in movies["results"]:
                print("\nFilm Adı:" + movie["title"])
                print("Puanı:" , movie["vote_average"])
                print("Açıklama:" + movie["overview"])
                print("\n"+15*"*")

        else:
            print("Yanlış seçim")

            
