import time
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname in user and hash(password) in user:
                self.current_user = user
                return True
            return False

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user[0]:  # Проверяем только никнейм
                print(f'Пользователь {nickname} уже существует.')
                return False
        new_user = (nickname, hash(password), age)
        self.users.append(new_user)
        self.current_user = new_user
        return True

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for videos in video:
            self.videos.append(videos)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, video_name):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if video.title == video_name:
                if video.adult_mode and self.current_user[2] < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return

                while video.time_now < video.duration:
                    print(f' {video.time_now + 1}')
                    video.time_now += 1
                    time.sleep(0.5) 

                print('Конец видео')  
                video.time_now = 0
                return

        print('Видео не найдено')


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self,title, duration,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user[0])

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
