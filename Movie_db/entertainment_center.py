import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                    "A story of a marine in alien land",
                    "https://1bosdb8iodg3cp8n-zippykid.netdna-ssl.com/wp-content/uploads/2016/06/Avatar.jpeg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

blood_diamond = media.Movie("Blood Diamond",
                            "A fisherman, a smuggler, and a syndicate of businessmen match wits over the possession of a priceless diamond",
                            "http://ia.media-imdb.com/images/M/MV5BMTY5MTYyNjkwNV5BMl5BanBnXkFtZTcwODE3MTI0MQ@@._V1_.jpg",
                            "https://www.youtube.com/watch?v=yknIZsvQjG4")

movies = [toy_story, avatar, blood_diamond]

fresh_tomatoes.open_movies_page(movies)
