import random
from datetime import datetime
from collections import deque
from time import sleep


class Queue:
    def __init__(self, number_of_residents: int):
        self.total_residents = number_of_residents
        self.residents_in_queue = deque([])
        self.residents_served = deque([])
        self.trays = 3 if number_of_residents >= 3 else number_of_residents
        self.assembly_time = 1.66  # RM 29 ((29 / 3) = 9,66) = 0,66 + 1
        self.registration_of_the_last_to_enter_the_queue = None

    def start(self):
        self.registration_of_the_last_to_enter_the_queue = datetime.now()
        print('Numero de moradores %d' % self.total_residents)
        print('Numero de bandeijas %d' % self.trays)

        number_to_enter_the_queue = 15 if self.total_residents >= 15 else self.total_residents
        for index in range(0, number_to_enter_the_queue):
            self.register_in_queue()
            if index == number_to_enter_the_queue - 1:
                self.registration_of_the_last_to_enter_the_queue = datetime.now()

        self.total_residents -= number_to_enter_the_queue
        print('Numero de moradores na fila =', number_to_enter_the_queue)
        print('Numero de moradores restantes fora da fila =', self.total_residents)

        self.serve()

        print('Fim do programa')

    def serve(self):
        time_for_last_to_enter_in_queue = datetime.now() - \
            self.registration_of_the_last_to_enter_the_queue
        if time_for_last_to_enter_in_queue.seconds > 120 and self.total_residents > 0:
            self.register_in_queue()
            self.total_residents -= 1
            self.registration_of_the_last_to_enter_the_queue = datetime.now()

        if not len(self.residents_in_queue):
            if not self.total_residents:
                return

            self.register_in_queue()
            self.total_residents -= 1

        if self.trays < 1:
            trays_number = 3 if len(
                self.residents_in_queue) >= 3 else len(self.residents_in_queue)
            print('Preparadando bandeijas.')
            for index in range(1, trays_number+1):
                sleep(self.assembly_time)
                self.trays += 1
                print('Bandeja N° %a abastecida.' % index)

        sleep(self.generate_second())
        now = datetime.now()
        departure_date = now.strftime("%H:%M:%S")
        resident_in_attendance = self.residents_in_queue.popleft()
        resident_in_attendance['departure_date'] = now

        attendance_time = resident_in_attendance['departure_date'] - \
            resident_in_attendance['enter_time']

        self.residents_served.append(resident_in_attendance)
        self.trays -= 1

        print('Morador servido, tempo de atendimento: %as \n Moradores na fila: %a' %
              (attendance_time.seconds, len(self.residents_in_queue)))

        self.serve()

    def register_in_queue(self):
        now = datetime.now()
        entry_time = now.strftime("%H:%M:%S")
        self.residents_in_queue.append(
            {'enter_time': now, "departure_date": None})

        print('Morador registrado na fila, hora: %s' % entry_time)
        sleep(self.generate_second())

    def generate_second(self):
        return random.randrange(1, 5)


def main():
    number_of_residents = random.randrange(1, 60)
    queue = Queue(number_of_residents)
    queue.start()


main()
