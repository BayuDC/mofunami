import re
import functools


class Loop:
    interval: int
    count: int
    command: str
    args: tuple
    time: dict

    def __init__(self, args: tuple) -> None:
        self.interval = 0
        self.count = 0
        self.command = None
        self.args = args
        self.time = {'hour': 0, 'minute': 0, 'second': 0}
        self.__parse_args()

    def __parse_args(self) -> None:
        for _ in range(len(self.args)):
            if self.__istime(self.args[0]):
                interval, *self.args = self.args
                self.__parse_time(interval)
            elif self.args[0].isdigit():
                count, *self.args = self.args
                self.count += int(count)
            else:
                break;

        # ! default value
        if not self.interval:
            self.interval = self.time['second'] = 1
        if not self.count:
            self.count = 10

        self.command, *self.args = self.args
        self.__calc_time()


    def __parse_time(self, interval: str) -> None:
        time_list = re.findall(r'[0-9]+[h|m|s]', interval)

        for time in time_list:
            time_int = int(time[:-1])

            if time.endswith('h'):
                self.time['hour'] += time_int
                self.interval += time_int * 60 * 60
            if time.endswith('m'):
                self.time['minute'] += time_int
                self.interval += time_int * 60
            if time.endswith('s'):
                self.time['second'] += time_int
                self.interval += time_int

    def __calc_time(self) -> None:
        def calc(unit, unit_next):
            self.time[unit_next] += int(self.time[unit] / 60)
            self.time[unit] = self.time[unit] % 60

        calc('second', 'minute')
        calc('minute', 'hour')

    def __istime(self, time: str) -> bool:
        return bool(re.match(r'([0-9]+[h|m|s])+', time))

    def pretty_args(self) -> str:
        def reduce(result, arg):
            return f'{result} {arg}'

        return functools.reduce(reduce, self.args, '')

    def pretty_time(self) -> str:
        text = ''

        for key, value in self.time.items():
            if value:
                text += f" `{value}`{key}{'s' if value > 1 else ''}"

        return text
