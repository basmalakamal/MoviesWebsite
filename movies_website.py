import fresh_tomatoes
import media

Hacksaw_Ridge = media.Movie("Hacksaw Ridge",
                            "The true story of Desmond T. Doss",
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png",
                            "https://www.youtube.com/watch?v=s2-1hz1juBI")

#print (Hacksaw_Ridge.story_line)

#Hacksaw_Ridge.show_trailer()


Wonder = media.Movie("Wonder",
                     "A young boy born with a facial deformity is destinied to fit in at a new school",
                     "https://upload.wikimedia.org/wikipedia/en/6/67/Wonder_%28film%29.png",
                     "https://www.youtube.com/watch?v=Ob7fPOzbmzE")

Coco = media.Movie("Coco",
                   "Coco follows a 12-year-old boy named Miguel who sets off a chain of events relating to a century-old mystery, leading to an extraordinary family reunion.",
                   "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=Ga6RYejo6Hk")

Sing = media.Movie("Sing",
                   "A koala named Buster recruits his best friend to help him drum up business",
                   "https://upload.wikimedia.org/wikipedia/en/b/bb/Sing_%282016_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=RYHBD9RF2dk")


The_Mountain_Between_Us = media.Movie("The Mountain Between Us",
                                      "two strangers must forge a connection to survive",
                                      "https://upload.wikimedia.org/wikipedia/en/1/17/TheMountainBetweenUsfilmposter.jpg",
                                      "https://www.youtube.com/watch?v=Mu41hu1a_8c")

Passengers = media.Movie("Passengers",
                         "Jennifer Lawrence and Chris Pratt are two passengers onboard a spaceship transport",
                         "https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")
#movies = [Hacksaw_Ridge, Wonder, Coco, Sing, The_Mountain_Between_Us, Passengers]
#fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__module__)









