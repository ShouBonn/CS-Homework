import codecs
import pickle

with codecs.open("Data.txt", 'r', encoding= "utf-8") as read:
    first_line = read.readline()
    movie_attributes = first_line.strip().split(";")

    read.readline()

    movie_data = []

    for lines in read.readlines():
        lines = lines.replace("\t", " ")
        movie_data.append(tuple(lines.strip().split(";")))


with codecs.open("movie.tsv", "w", encoding= "utf-8") as write:
    for movie in  movie_data:
        for item in movie:
            item = item.replace("\t", " ")
            write.write(item + "\t")
        write.write("\n")


def make_dict(movie_data, index):
    dict = {}
    for movie in movie_data:
        if movie[index] in dict:
            dict[movie[index]].append(movie)
        else:
            dict[movie[index]] = [movie]
    return dict


by_year = make_dict(movie_data, 0)
by_length = make_dict(movie_data, 1)
by_title = make_dict(movie_data, 2)
by_subject = make_dict(movie_data, 3)
by_actor = make_dict(movie_data, 4)
by_actress = make_dict(movie_data, 5)
by_director = make_dict(movie_data, 6)
by_popularity = make_dict(movie_data, 7)
by_awards = make_dict(movie_data, 8)
by_image = make_dict(movie_data, 9)


def pickle_it(name, dict):
    with open(name + '.pickle', "wb") as f:
        pickle.dump(dict, f)


pickle_it('by_year', by_year)
pickle_it('by_length', by_length)
pickle_it('by_title', by_title)
pickle_it('by_subject', by_subject)
pickle_it('by_actor', by_actor)
pickle_it('by_actress', by_actress)
pickle_it('by_director', by_director)
pickle_it('by_popularity', by_popularity)
pickle_it('by_awards', by_awards)
pickle_it('by_image', by_image)


# for key in by_image:
#     print(key, by_image[key])
