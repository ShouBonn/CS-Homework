import pickle


def unpickle(name):
    with open(name + ".pickle", "rb") as f:
        return pickle.load(f)


by_year = unpickle("by_year")
by_length = unpickle("by_length")
by_title = unpickle("by_title")
by_subject = unpickle("by_subject")
by_actor = unpickle("by_actor")
by_actress = unpickle("by_actress")
by_director = unpickle("by_director")
by_popularity = unpickle("by_popularity")
by_awards = unpickle("by_awards")
by_image = unpickle("by_image")


def average_runtime(dict):
    dictionary = {}
    for element in dict:
        count_elements = 0
        total_runtime = 0
        for movie in dict[element]:
            if movie[1].isdigit():
                total_runtime += int(movie[1])
                count_elements += 1
        dictionary[element] = total_runtime/count_elements
    return dictionary


aver_runtime_per_year = average_runtime(by_year)

for key in aver_runtime_per_year:
    print(key, average_runtime(key))




def num_of_movies(dict):
    new_dict = {}
    for element in dict:
        new_dict[element] = len(dict[element])
    return new_dict


num_movies_by_year = num_of_movies(by_year)
num_movies_by_length = num_of_movies(by_length)
num_movies_by_title = num_of_movies(by_title)
num_movies_by_genre = num_of_movies(by_subject)
num_movies_by_actor = num_of_movies(by_actor)
num_movies_by_actress = num_of_movies(by_actress)
num_movies_by_director = num_of_movies(by_director)
num_movies_by_popularity = num_of_movies(by_popularity)
num_movies_by_awards = num_of_movies(by_awards)
num_movies_by_image = num_of_movies(by_image)

# for key in num_movies_by_image:
#     print(key, num_movies_by_image[key])


