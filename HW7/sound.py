class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'<{self.name}-{self.duration}>'

    def __lt__(self, another):
        return print(self.duration < another.duration)

    def __gt__(self, another):
        return print(self.duration > another.duration)

    def __eq__(self, another):
        return print(self.duration == another.duration)

    def __le__(self, another):
        return print(self.duration <= another.duration)

    def __ge__(self, another):
        return print(self.duration >= another.duration)


class Album:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.contain = []

    def __str__(self):
        tracklist = ''
        for tracks in self.contain:
            tracklist += (str(tracks) + '\n')
        return f'{self.name}, {self.group}: \n{tracklist}'

    def add_track(self, name, duration):
        self.contain.append(Track(name, duration))

    def get_duration(self):
        duration = 0
        for track in self.contain:
            duration += track.duration
        print(f'продолжительность альбома {self.name} группы {self.group} {duration} мин')


track_1 = Track('Main', 5)

album1 = Album('Scorpion', 'Drake')
album2 = Album('Views', 'Drake')

album1.add_track('Surival', 5)
album1.add_track('Nonstop', 3)
album1.add_track('Elevate', 4)

album2.add_track('9', 5)
album2.add_track('Hype', 3)
album2.add_track('With you', 2)

print(track_1.__str__())

print(album1)
print(album2)

track1 = Track('Elevate', 4)
track2 = Track('With you', 2)
print(track1 > track2)

