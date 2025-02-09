import random
import colorama
from colorama import Fore, Style

colorama.init()


class Fishing:
    def __init__(self):
        self.worm_wrong_enter = 0
        self.fish_count = 0
        self.fish_left = 0
        self.qualit_worm = 0
        self.worm_left = 0
        self.money = 0
        self.colored_fish_list = []
        self.caught_fish = []  # список пойманой рыбы

    def list_activity(self):
        activism = ['1-Перекусить будербродом', '2-Посмотреть в даль', '3-Любоваться природой', '4-Ловить рыбу',
                    '5-Ничего', '6-Уйти домой']
        for activity in activism:
            print(activity)
        activism[0] = 1
        activism[1] = 2
        activism[2] = 3
        activism[3] = 4
        activism[4] = 5
        activism[5] = 6
        self.activ_funk()

    def activ_funk(self):
        try:
            any_act = int(input("\nЧто хочешь делать сегодня?(1-5) "))
            if any_act == 1:
                print(f"{Fore.YELLOW}Ты подкрепился!{Style.RESET_ALL}")
                self.activ_funk()
            elif any_act == 2:
                print(f"{Fore.YELLOW}В дали ты видишь как летают птицы и тебе\n"
                      f"кажется, что ты бы мог стать орнитологом!{Style.RESET_ALL}")
                self.activ_funk()
            elif any_act == 3:
                print(f"{Fore.YELLOW}Сегодня потрясающая погодка!🌻🌞{Style.RESET_ALL}")
                self.activ_funk()
            elif any_act == 4:
                self.rand_qual_worms()
                self.worm_()
            elif any_act == 5:
                print("Хорошо!")
                exit()
            elif any_act == 6:
                self.exit_()
            else:
                print("Ой что-то не так! Попробуй ещё раз...")
                self.activ_funk()
        except ValueError:
            print("Ой, введите номер действия (1-5)")
            self.activ_funk()

    def rand_qual_worms(self):
        worms_rand = random.randint(1, 10)
        self.qualit_worm = worms_rand
        self.worm_left = worms_rand
        print(f"Сегодня у тебя с собой {Fore.BLUE}{self.qualit_worm}{Style.RESET_ALL} червь(-ей)")

    def worm_(self):
        while True:
            while self.worm_left > 0:
                worm = input("Наживить червя на крючок? ")
                if worm.lower() == 'да':
                    self.qualit_worm -= 1
                    self.worm_left = self.qualit_worm
                    throw_into = input("Закинуть приманку в пруд? ")
                    if throw_into.lower() == 'да':
                        lucky = random.randint(0, 1)
                        if lucky == 1:
                            print("Жаль, ничего не клюёт( ")
                            print(f"У тебя осталось {Fore.BLUE}{self.worm_left}{Style.RESET_ALL} червь(-ей)")
                            self.exit_()
                        else:
                            self.catch_fish_def()
                    elif throw_into.lower() == 'нет':
                        print("Зачем червя убил??")
                        exit()
                    else:
                        print(f"{Fore.RED}(надо было да/нет ответить){Style.RESET_ALL}")
                        self.worm_()

                elif worm.lower() == 'нет':
                    print("Странно..")
                    self.activ_funk()

                else:
                    print(f"Промахнулся!{Fore.RED}(надо было да/нет ответить){Style.RESET_ALL}")
                    self.worm_()

    def catch_fish_def(self):
        catch_fish = input("Выудить рыбку? ")
        if catch_fish.lower() == 'да':
            fish = self.random_fish()
            self.fish_count += 1
            self.fish_left += 1
            self.caught_fish.append(fish)
            self.money += fish['price']
            print(f"У тебя уже: {Fore.BLUE}{str(self.fish_count)}{Style.RESET_ALL} рыба за день")
            print(f"У тебя осталось {Fore.BLUE}{self.worm_left}{Style.RESET_ALL} червь(-ей)")
            self.cooking(fish)

        elif catch_fish.lower() == "нет":
            print("Рыбка уйдет!")
            self.worm_wrong_enter += 1
            if self.worm_wrong_enter >= 2:
                print("....")
                print("Эх, упустил...")
                self.exit_()
            else:
                self.catch_fish_def()

        else:
            print("\nТы упустил рыбу! Она уплыла навсегда...")
            self.exit_()

    def random_fish(self):
        fish_list = [
            {"name": "карасик", "price": 50},
            {"name": "щука", "price": 150},
            {"name": "окунь", "price": 100},
            {"name": "плотва", "price": 20},
            {"name": "судак", "price": 200},
            {"name": "лещ", "price": 80},
            {"name": "карп", "price": 300},
            {"name": "сом", "price": 500},
            {"name": "тилапия", "price": 120},
            {"name": "форель", "price": 400}
        ]
        random_fish = random.choice(fish_list)
        print(f"Вы поймали: {self.color_fish(random_fish)}!\n"
              f"Цена: {random_fish['price']} рублей")
        return random_fish

    def color_fish(self, fish):
        if isinstance(fish, dict):
            if fish['price'] <= 100:
                color = Fore.GREEN
            elif 100 < fish['price'] <= 300:
                color = Fore.YELLOW
            elif 300 < fish['price'] <= 400:
                color = Fore.MAGENTA
            else:
                color = Fore.RED
            return f"{color}{fish['name']}{Style.RESET_ALL}"
        elif isinstance(fish, str):
            return f"{Fore.CYAN}{fish}{Style.RESET_ALL}"
        else:
            return f"{Fore.WHITE}Неизвестная рыба{Style.RESET_ALL}"

    def cooking(self, fish):
        cook = input(f"Хочешь приготовить {self.color_fish(fish)} на костре? (да/нет) ")
        if cook.lower() == "да":
            self.process_cook(fish)

        elif cook.lower() == "нет":
            print(f"Ты оставил {self.color_fish(fish)} сырой")
            self.exit_()
        else:
            print(f"Ты слишком голоден, чтобы написать {Fore.RED}<да> или <нет>{Style.RESET_ALL}")
            self.cooking(fish)

    def process_cook(self, fish):
        for i in 'Cooking':
            print(f"{Fore.BLUE}{i}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Ты приготовил{Style.RESET_ALL} {self.color_fish(fish)}")
        self.money -= fish['price']
        if fish in self.caught_fish:
            self.caught_fish.remove(fish)
        # self.fish_left = len(self.caught_fish)
        self.fish_left -= 1
        print(f"{Fore.BLACK}{self.caught_fish}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}ух, а уха получилась отличная:)!{Style.RESET_ALL}")
        self.eat()

    def eat(self):
        write_eat = input("напиши <кушать> ")
        if write_eat.lower() == "кушать":
            print("Теперь ты сыт!")
            self.exit_()
        else:
            print(f"{Fore.RED}Попробуй еще{Style.RESET_ALL}")
            self.eat()

    def exit_(self):
        exit_choice = input("Завершить рыбалку? ")
        if exit_choice.lower() == 'да':
            if self.fish_left != 0:
                self.colored_fish_list = ', '.join([
                    self.color_fish(fish) for fish in self.caught_fish if isinstance(fish, dict)
                ])
                print(
                    f"Сегодня ты поймал:  {Fore.BLUE}{self.fish_count}{Style.RESET_ALL} рыб(у)\n"
                    f"В сетке: {self.colored_fish_list}\n"
                    f"С собой домой несешь: {Fore.BLUE}{self.fish_left}{Style.RESET_ALL} сырых(-ую) рыб(у)\n"
                    # f"У тебя осталось: {Fore.BLUE}{self.worm_left}{Style.RESET_ALL} червь(-ей)\n"
                )

                self.random_encounter()
            else:
                print("У тебя нет, что нести домой.")
                self.print_home()
                self.call_home()
        elif exit_choice.lower() == "нет":
            if self.worm_left == 0:
                print(f"{Fore.YELLOW}У тебя больше нет сегодня червей!{Style.RESET_ALL}")
                self.exit_()
            else:
                self.worm_()
        else:
            print(Fore.RED + "напиши да/нет" + Style.RESET_ALL)
            self.exit_()

    def random_encounter(self):
        encounter = random.randint(1, 2)
        if encounter == 1:
            print(f"Тебе по пути встертился {Fore.YELLOW}Клим{Style.RESET_ALL}!")
            message = input("Хочешь продать ему рыбу? ")
            if message.lower() == "да":
                self.print_money()
            elif message.lower() == "нет":
                print("Ладно, Клим ушёл. А ты возвращаешься домой с рыбкой. Тебе нужнее!")
                self.print_home()
                self.call_home()
            else:
                print("Ой что-то не так! Попробуй ещё раз...")
                self.random_encounter()
        else:
            print("По пути ты никого не встретил :(")
            self.sell_fish()

    def sell_fish(self):
        quest_sell = input("Хочешь продать на рынке рыбу? ")
        if quest_sell.lower() == "да":
            self.print_money()
        elif quest_sell.lower() == "нет":
            print("Хорошо, сегодня был отличный день!")
            self.print_home()
            self.call_home()
        else:
            print("Что-то пошло не так! Ещё раз..")
            self.sell_fish()

    def print_money(self):
        print(
            f"Ты выручил с рыбалки {Fore.BLUE}{self.money}{Style.RESET_ALL} рублей. \nТвой мешочек полон денег💰!")
        self.caught_fish = 0
        self.print_home()
        self.call_home()

    def print_home(self):
        for i in 'Home':
            print(f"{Fore.BLUE}{i}{Style.RESET_ALL}  ")

    def call_home(self):
        home = AtHome(self.caught_fish)
        home.mes_you_home()
        home.activ_at_home()


class AtHome(Fishing):
    fridge = []

    def __init__(self, caught_fish, inventar=0):
        super().__init__()
        self.caught_fish = caught_fish
        self.inventar = inventar

    def mes_you_home(self):
        print("Ты вернулся домой!")

    def activ_at_home(
            self):  # сделать не список, а словарь с вариантами действий  [{'1': 'Положить рыбу в холодильник'}]
        list_at_home = ['1. Положить рыбу в холодильник', '2. Смотреть телевизор',
                        '3. Стирать одежду', '4. Идти спать', '5. Заварить чаю🍵',
                        '6. Посмотреть в холодильник', '7. Пойти на рыбалку'
                        ]
        for activ in list_at_home:
            print(activ)
        list_at_home[0] = 1
        list_at_home[1] = 2
        list_at_home[2] = 3
        list_at_home[3] = 4
        list_at_home[4] = 5
        list_at_home[5] = 6
        list_at_home[6] = 7
        self.activ_funk_home()

    def activ_funk_home(self):
        global fridge
        choice = int(input("\nЧто хочешь сделать? (1-5) "))
        if choice == 1:
            if len(self.caught_fish) != 0:
                print(f"Ты положил рыбу: ")
                for fish in self.caught_fish:
                    print(f"\t{self.color_fish(fish)}")
                self.fridge.extend(self.caught_fish)
                self.caught_fish = []
                self.activ_funk_home()
            else:
                print("У тебя нету рыбы!")
                self.activ_funk_home()
        elif choice == 2:
            print(
                "Телевизор включен. Твоя спина отдыхает, и ты чувствуешь, как твои ноги тихо гудят от насыщеного дня...")
            self.random_visit()
        elif choice == 3:
            print("Ты стираешь одежду. Числота - залог здоровья!")
            self.activ_funk_home()
        elif choice == 4:
            print("Спокойной ночи! Пусть тебе приснится самая большая рыбка🌞.\nИгра завершена.")
            exit()
        elif choice == 5:
            if self.inventar == 0:
                self.tea()
            else:
                self.make_tea()
        elif choice == 6:
            print("У тебя есть: ")

            def show_fish():
                for fish in self.fridge:
                    print(f"\t{self.color_fish(fish)}")
                self.activ_funk_home()

            show_fish()
        elif choice == 7:
            start()
        else:
            print("Неверный выбор. Попробуй еще!")
            self.activ_funk_home()

    def random_visit(self):
        visit = random.randint(0, 1)
        if visit == 0:
            self.activ_funk_home()
        else:
            print(f"В гости наведался {Fore.YELLOW}Клим{Style.RESET_ALL}!")
            self.nardu_klim()

    def tea(self):
        mes = input("У тебя закончились травы. Пойдешь в горы? ")
        if mes.lower() == 'да':
            for i in 'going...':
                print(f"{Fore.BLUE}{i}{Style.RESET_ALL}")
            mountains = Mountains()
            mountains.message()
            mountains.collect_tea()

        elif mes.lower() == 'нет':
            print("Хорошо, не пойдем")
            self.activ_funk_home()
        else:
            print(f"{Fore.RED}да/нет{Style.RESET_ALL}")
            self.tea()

    def make_tea(self):
        if self.inventar > 0:
            recept = ("Рецепт приготовления особого чая:\n"
                      "3. Пожождать пока закипит чайник\n"
                      "2. Поставить чайник на огонь в печи\n"
                      "1. Достать ароматные травы\n"
                      "4. Всыпать горсток трав")
            print(recept)

        def numbers():
            enter_numbers = input("Введи правильную последовательность цыфр: ")
            if enter_numbers == '1234':
                for tea in 'teaparty':
                    print(f"{Fore.BLUE}{tea}{Style.RESET_ALL}")
                self.inventar -= 1
                print("Аромат чай сводит тебя с ума! Вот что значит чай с горных растений..")
                print(f"У тебя осталось: {Fore.BLUE}{self.inventar}{Style.RESET_ALL} ")
                self.activ_funk_home()
            else:
                print("Попробуй ещё!")
                numbers()

        numbers()

    def nardu_klim(self):
        nardu = input("Хочешь поиграть с ним в нарды? ")
        if nardu.lower() == 'да':
            print("Вы играете! Клим явно настроен серьезно...")  # мб новый класс процесса игры в нарды
            exit()
        elif nardu.lower() == 'нет':
            print("Клим немного загрустил. Но начал рассказывать историю о его героическом спасении корабля в шторм!🚢")
            exit()
        else:
            print(f"{Fore.RED}да/нет{Style.RESET_ALL}")
            self.nardu_klim()


class Mountains(AtHome):

    def __init__(self):
        super().__init__(inventar=0, caught_fish=0)
        self.max_length = 10
        self.dog_met = False
        self.qual_tea = 0

    def message(self):
        print(f"{Fore.GREEN}Вы добрались до богатой поляны{Style.RESET_ALL}")

    def for_dog(self):
        if self.dog_met:
            return

        chanse = random.randint(0, 100)
        if chanse == 100:
            dog_met = True
            return f"{Fore.YELLOW}Вас стретился одинокий песик!{Style.RESET_ALL}"

    def collect_tea(self):
        self.random_tea()
        self.max_length = 10

    def random_tea(self):
        self.qual_tea = random.randint(1, 20)
        print(f"На поляне сегодня трав на {self.qual_tea} пучков(-ок)")
        self.skolko_tea()

    def skolko_tea(self):
        while self.inventar < self.max_length and self.qual_tea > 0:
            try:
                user_collect = int(
                    input(f"Сколько соберешь? (Доступно: {self.qual_tea}, Место: {self.max_length - self.inventar}) "))
                if user_collect + self.inventar > self.max_length:
                    print(
                        f"{Fore.RED}Не хватает места в рюкзаке!{Style.RESET_ALL} Можешь взять только {self.max_length - self.inventar} пучков.")
                elif user_collect > self.qual_tea:
                    print(f"{Fore.RED}На поляне столько нет!{Style.RESET_ALL} Доступно только {self.qual_tea} пучков.")
                elif user_collect == 0:
                    self.return_home()
                else:
                    self.inventar += user_collect
                    self.qual_tea -= user_collect
                    print(
                        f"Ты собрал {Fore.GREEN}{user_collect}{Style.RESET_ALL} пучков. В рюкзаке: {Fore.BLUE}{self.inventar}{Style.RESET_ALL}.")
            except ValueError:
                print("Введите число!")

        if self.inventar == self.max_length:
            print("Рюкзак полностью заполнен!")
        elif self.qual_tea == 0:
            print("На поляне больше нет трав!")

        self.return_home()

    def return_home(self):
        for i in "Возвращение домой...":
            print(f"{Fore.CYAN}{i}{Style.RESET_ALL}", end='', flush=True)
        print()
        home = AtHome(inventar=self.inventar, caught_fish=0)
        home.mes_you_home()
        home.activ_at_home()


def start():
    if __name__ == '__main__':
        fishing = Fishing()
        fishing.list_activity()


start()

# home = AtHome(inventar=0, caught_fish=[])
# home.activ_at_home()
