
class Recommendation:
    """содержит данные и работает с ними"""

    films, users = {}, []

    def __init__(self, films, users):
        """"считывает информацию из данных файлов"""
        f = open(films, encoding='utf-8')
        u = open(users, encoding='utf-8')
        for film in f.readlines():
            self.films[film.split(',')[0]] = film.split(',')[1]
        for user in u.readlines():
            self.users.append(user)
        f.close()
        u.close()

    def get_new_film(self, watched_films):
        watched_films = ''.join(watched_films)
        cnt_watched_films = [0 for i in range(len(self.users))]
        cnt_recommend_films = [0 for i in range(len(self.films))]
        recommended_users = ''
        for user in self.users:
            user_films = ''.join(user)
            a = set()
            for i in user_films:
                if i in watched_films:
                    a.add(i)
            if len(a) >= len(watched_films) // 2:
                recommended_users += user_films
        mk = 0
        mf = '1'
        for i in recommended_users:
            if (recommended_users.count(i) > mk) and (i not in watched_films):
                mk = recommended_users.count(i)
                mf = i
        return self.films[mf]


rec = Recommendation("films.txt", "users.txt")
print(rec.get_new_film("2,4"))


