"""
Вычитание времени

Операции приведения типа:
int–результатом является количество часов (минуты отбрасываются);
boolean–результатом является true,если часы и минуты не равны
нулю,и false в противном случае.

Бинарные операции:
- положительное целое число минут к времени.
+ Time t–сложить два времени
"""


class Time:
    def __init__(self, time_str="00:00"):
        self.hours, self.minutes = [int(i) for i in time_str.split(':')]

    def __str__(self):
        mins = '0' + str(self.minutes)
        return f"{self.hours}:{mins[-2:]}"

    def subtract_time(self, other):
        self_mins = self.hours * 60 + self.minutes
        other_mins = other.hours * 60 + other.minutes

        diff = self_mins - other_mins
        if diff < 0:
            diff += 24 * 60

        return Time(f"{diff // 60}:{diff % 60}")

    def __int__(self):
        return self.hours

    def __bool__(self):
        return self.hours != 0 or self.minutes != 0

    def __sub__(self, minutes_to_sub):
        self_mins = self.hours * 60 + self.minutes
        total_mins = (self_mins - minutes_to_sub)
        if total_mins < 0:
            total_mins += 24 * 60
        return Time(f"{total_mins // 60}:{total_mins % 60}")

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        mins = total_minutes % 60
        hours = (self.hours + other.hours + extra_hours) % 24
        return Time(f"{hours}:{mins}")