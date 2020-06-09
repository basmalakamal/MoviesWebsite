import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print (toy_story.story_line)

Avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print (Avatar.story_line)

avatar.show_trailer()
