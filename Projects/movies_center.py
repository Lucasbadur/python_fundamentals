import mediamovies
import fresh_tomatoes

toy_story = mediamovies.Movie("Toy Story",
                              "A story of a boy and his toys",
                              "https://goo.gl/hrtQkC",
                              "https://www.youtube.com/watch?v=fpHlKLMgNYA")

avatar = mediamovies.Movie("Avatar",
                           "Shitty movie from shitty director",
                           "https://goo.gl/fdKxdx",
                           "https://www.youtube.com/watch?v=hEqjGLT2BXo",)

leatherheads = mediamovies.Movie("Leatherheads",
                                 "Man invents professional american football",
                                 "https://goo.gl/or9jAV",
                                 "https://www.youtube.com/watch?v=gRRGj8Kmxi0")

jurassicpark = mediamovies.Movie("Jurassic Park",
                                 "Scientists think whether they can and not if they should",
                                 "https://goo.gl/PmZwAU",
                                 "https://www.youtube.com/watch?v=lc0UehYemQA")

#jurassicpark.show_trailer()
#print(jurassicpark.storyline)

movies = [toy_story, avatar, leatherheads, jurassicpark]
fresh_tomatoes.open_movies_page(movies)
#print(mediamovies.Movie.VALID_RATINGS)
print(mediamovies.Movie.__doc__)

