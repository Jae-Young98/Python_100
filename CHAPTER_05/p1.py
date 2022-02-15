# Immutable 정수, 실수, 문자열, 튜플
# Mutalbe 리스트, 딕셔너리, 집합
# Class 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀

from distutils.command.build_scripts import first_line_re


class Calculator:
    def __init__(self):  # 예약어 / 제일 처음 실행됨
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):  # 설정한 변수 명이 self에 들어감
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result


a = FourCal(4, 5)
print(a.add())
