def get_two_movies_to_fill_flight(movie_lengths, flight_length):
    movie_lengths_seen_hash = {}

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen_hash:
            return True

        movie_lengths_seen_hash[first_movie_length] = True

    return False

print get_two_movies_to_fill_flight([1, 3, 4, 7], 7)
