import random

import colorama
from colorama import Fore, Style

colorama.init()


class Fishing:
    def __init__(self, fish_rod: str, fish_count: int, fish_left: int, worm_left: int, money: int,
                 colored_fish_list: list, caught_fish: list, type_worm: str, level: int, cash: int, pie: int):
        self.fish_rod = fish_rod
        self.fish_left: int = fish_left
        self.worm_left = worm_left
        self.money_in_wallet = money
        self.colored_fish_list = colored_fish_list
        self.type_worm = type_worm
        self.level = level
        self.cash = cash
        self.pie = pie
        if not isinstance(caught_fish, list):
            print(f"Внимание! caught_fish был {type(caught_fish)}, заменяю на пустой список.")
            caught_fish = []
        self.fish_count = int(fish_count) \
            if isinstance(fish_count, (int, str)) and str(fish_count).isdigit() \
            else 0

        self.caught_fish = caught_fish  # список пойманой рыбы
        self.worm_wrong_enter = 0
        self.qualit_worm = 0

    def list_activity(self):
        self.activism = {1: ("Перекусить будербродом", self.dine),
                         2: ("Посмотреть в даль", self.look_distance),
                         3: ("Любоваться природой", self.admire),
                         4: ("Ловить рыбу", self.rand_qual_worms),
                         5: ("Ничего", self.nothing),
                         6: ("Уйти домой", self.exit_)
                         }

    def activation(self):
        self.list_activity()
        for key, (desc, _) in self.activism.items():
            print(f"{Fore.LIGHTCYAN_EX}{key}{Style.RESET_ALL}. {desc}")

        self.activ_funk()

    def activ_funk(self):
        try:
            self.choice1 = int(input("Что хочешь сделать(1-6)? "))

            if self.choice1 in self.activism:
                activism = self.activism[self.choice1][1]
                activism()
            else:
                print("Неверный выбор! Попробуй еще :)")
                self.activ_funk()
        except ValueError:
            print("Ой, введите номер действия (1-6)")
            self.activ_funk()

    def dine(self):
        print(f"{Fore.YELLOW}Ты подкрепился!{Style.RESET_ALL}")
        self.activ_funk()

    def look_distance(self):
        print(f"{Fore.YELLOW}В дали ты видишь как летают птицы и тебе\n"
              f"кажется, что ты бы мог стать орнитологом!{Style.RESET_ALL}")
        self.activ_funk()

    def admire(self):
        print(f"{Fore.YELLOW}Сегодня потрясающая погодка!🌻🌞{Style.RESET_ALL}")
        self.activ_funk()

    def nothing(self):
        print("Хорошо!")
        exit()

    def rand_qual_worms(self):
        worms_rand = random.randint(1, 10)
        self.qualit_worm = worms_rand
        self.worm_left = worms_rand
        print(f"Сегодня у тебя с собой {Fore.BLUE}{self.qualit_worm}{Style.RESET_ALL} червь(-ей)")
        print(self.fish_rod)
        if self.type_worm == "A-червячок":
            color = Fore.GREEN
        elif self.type_worm == "B-червячок":
            color = Fore.BLUE
        elif self.type_worm == "C-червячок":
            color = Fore.CYAN
        elif self.type_worm == "D-червячок":
            color = Fore.MAGENTA
        else:
            color = Fore.RED
        print(f"{color}{self.type_worm}{Style.RESET_ALL}")
        self.worm_()

    def worm_(self):
        while True:
            while self.worm_left > 0:
                # print(f"level: {self.level}")
                worm = input("Наживить червя на крючок? ")
                if worm.lower() == 'да':
                    self.qualit_worm -= 1
                    self.worm_left = self.qualit_worm
                    throw_into = input("Закинуть приманку в пруд? ")
                    if throw_into.lower() == 'да':
                        lucky = random.randint(0, 100)
                        print(lucky)
                        if lucky >= 65:
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

                else:  # print(self.fish_rod)
                    print(f"Промахнулся!{Fore.RED}(надо было да/нет ответить){Style.RESET_ALL}")
                    self.worm_()

    def catch_fish_def(self):
        catch_fish = input("Выудить рыбку? ")
        if catch_fish.lower() == 'да':
            fish = self.random_fish()
            if not isinstance(self.fish_left, int):
                print(f"Ошибка! fish_left стал {type(self.fish_left)}: {self.fish_left}")
                self.fish_left = 0
            self.fish_count += 1

            self.fish_left += 1
            self.caught_fish.append(fish)
            print(self.caught_fish)
            self.cash += fish['price']
            print(f"У тебя уже: {Fore.BLUE}{str(self.fish_count)}{Style.RESET_ALL} рыба за игру")
            print(f"У тебя осталось {Fore.BLUE}{self.worm_left}{Style.RESET_ALL} червь(-ей)")
            self.level_()
            if self.level == 2:
                print(f"{Fore.GREEN}Загляни к Тамаре, чтобы узнать, что тебе стало доступно!{Style.RESET_ALL}")
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

    def level_(self):
        self.previous_level = self.level
        if self.fish_count == 0:
            self.level += 1
        else:
            self.level = self.fish_count // 5 + 1
        if self.previous_level < self.level:
            print(f"Твой уровень повышен!💫\n{Fore.MAGENTA}LEVEL: {self.level}{Style.RESET_ALL}")

    def color_fish(self, fish, extra=False):
        if isinstance(fish, dict):
            if fish['price'] <= 150:
                color = Fore.GREEN
            elif 150 < fish['price'] <= 300:
                color = Fore.CYAN
            elif 300 < fish['price'] <= 600:
                color = Fore.BLUE
            elif 600 < fish['price'] <= 900:
                color = Fore.YELLOW
            elif 900 < fish['price'] <= 1800:
                color = Fore.MAGENTA
            else:
                color = Fore.RED

            result = f"{color}{fish['name']}{Style.RESET_ALL}"
            if extra:
                result += f"({fish['price']} руб)"
                return result

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

    def random_fish(self):
        fish_list = [
            {"name": "плотва", "price": 20},
            {"name": "ерховка", "price": 30},
            {"name": "бычок", "price": 40},
            {"name": "карасик", "price": 50},
            {"name": "густера", "price": 60},
            {"name": "лещ", "price": 80},
            {"name": "чехонь", "price": 90},
            {"name": "окунь", "price": 100},
            {"name": "линь", "price": 110},
            {"name": "тилапия", "price": 120},
            {"name": "камбала", "price": 130},
            {"name": "голавль", "price": 140},
            {"name": "щука", "price": 150},
            {"name": "язь", "price": 160},
            {"name": "налим", "price": 170},
            {"name": "сарган", "price": 180},
            {"name": "судак", "price": 200},
            {"name": "толстолобик", "price": 250},
            {"name": "карп", "price": 300},
            {"name": "форель", "price": 400},
            {"name": "сом", "price": 500},
            {"name": "угорь", "price": 600},
            {"name": "осётр", "price": 750},
            {"name": "морской окунь", "price": 900},
            {"name": "тунец", "price": 1200},
            {"name": "лосось", "price": 1500},
            {"name": "палтус", "price": 1800},
            {"name": "меч-рыба", "price": 2500},
            {"name": "белуга", "price": 5000}
        ]
        self.lucky = random.randint(0, 1000)
        print(f"{self.lucky} {Fore.LIGHTBLACK_EX}standart{Style.RESET_ALL}")
        '''Дополнительно сделать
         возможность использовать приманку из прошлого захода
          (пришел домой и решил опять на рыбалку)'''

        # Преимущества удочки
        if self.fish_rod == "Обычная удочка":
            self.lucky -= 300
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}fish rod{Style.RESET_ALL}")

        elif self.fish_rod == "Бамбуковая удочка":
            self.lucky -= 100
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}fish rod{Style.RESET_ALL}")

        elif self.fish_rod == "Спиннинг удочка":
            self.lucky += 100
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}fish rod{Style.RESET_ALL}")

        else:
            self.lucky += 200
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}bait{Style.RESET_ALL}")

        if self.type_worm == "A-червячок":
            self.lucky += 1
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}bait{Style.RESET_ALL}")
        elif self.type_worm == "B-червячок":
            self.lucky += 10
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}bait{Style.RESET_ALL}")
        elif self.type_worm == "C-червячок":
            self.lucky += 50
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}bait{Style.RESET_ALL}")
        elif self.type_worm == "D-червячок":
            self.lucky += 75
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}bait{Style.RESET_ALL}")
        elif self.type_worm == "S-червячок":
            self.lucky += 120
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}bait{Style.RESET_ALL}")
        else:
            print(f"{self.lucky} {Fore.LIGHTBLACK_EX}bait{Style.RESET_ALL}")

        # Какая рыбка может выловиться в зависимости от удачи и удочки
        if self.lucky < 400:
            fish_list = fish_list[:12]
        elif self.lucky < 600:
            fish_list = fish_list[13:18]
        elif self.lucky < 700:
            fish_list = fish_list[19:21]
        elif self.lucky < 900:
            fish_list = fish_list[22:23]
        elif self.lucky < 999:
            fish_list = fish_list[24:26]
        else:
            print(self.lucky)
            fish_list = fish_list[27:28]

        if self.lucky < 0 or self.lucky == 0:
            print("Твоя удочка слишком слаба для такой рыбки!😢")
            if self.worm_left:
                self.worm_()
            else:
                print("Червей больше нет!")
                self.exit_()
            # Выборка рыбки из того радиуса, который был определен удачей и различными "плюшками"
        random_fish = random.choice(fish_list)
        print(f"Вы поймали: {self.color_fish(random_fish)}!\n"
              f"Цена: {random_fish['price']} рублей")
        return random_fish

    def process_cook(self, fish):
        for i in 'Cooking':
            print(f"{Fore.BLUE}{i}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Ты приготовил{Style.RESET_ALL} {self.color_fish(fish)}")
        self.money_in_wallet -= fish['price']
        if fish in self.caught_fish:
            self.caught_fish.remove(fish)
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
            if self.caught_fish != []:
                self.colored_fish_list = ', '.join([
                    self.color_fish(fish) for fish in self.caught_fish if
                    isinstance(fish, dict) and isinstance(self.caught_fish, list)
                ])
                print(
                    f"Сегодня ты поймал:  {Fore.BLUE}{self.fish_count}{Style.RESET_ALL} рыб(у)\n"
                    f"В сетке: {self.colored_fish_list}\n"
                    f"С собой домой несешь: {Fore.BLUE}{self.fish_left}{Style.RESET_ALL} сырых(-ую) рыб(у)\n"
                    f"У тебя осталось: {Fore.BLUE}{self.worm_left}{Style.RESET_ALL} червь(-ей)\n"
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

            def want_sell():
                message = input("Хочешь продать ему рыбу? ")
                if message.lower() == "да":
                    self.print_money()
                elif message.lower() == "нет":
                    print("Ладно, Клим ушёл. А ты возвращаешься домой с рыбкой. Тебе нужнее!")
                    self.print_home()
                    self.call_home()
                else:
                    print("Ой что-то не так! Попробуй ещё раз...")
                    want_sell()

            want_sell()
        else:
            print("По пути ты никого не встретил :(")
            self.money_in_wallet = self.cash
            self.cash = 0
            self.print_home()
            self.call_home()

    def sell_fish(self):
        quest_sell = input("Хочешь продать на рынке рыбу? ")
        if quest_sell.lower() == "да":
            while self.caught_fish != []:
                self.print_money()
            if self.caught_fish == []:
                print(f"{Fore.LIGHTRED_EX}У тебя нету рыбы на продажу!{Style.RESET_ALL}")
        elif quest_sell.lower() == "нет":
            print("Хорошо, сегодня был отличный день!")
            self.print_home()
            self.call_home()
        else:
            print("Что-то пошло не так! Ещё раз..")
            self.sell_fish()

    def print_money(self):
        print(
            f"Ты выручил с рыбалки {Fore.BLUE}{self.cash}{Style.RESET_ALL} рублей. \nТвой мешочек полон денег💰!")
        self.money_in_wallet += self.cash
        self.cash = 0
        self.caught_fish.clear()
        self.print_home()
        self.call_home()

    def print_home(self):
        for i in 'Home':
            print(f"{Fore.BLUE}{i}{Style.RESET_ALL}  ")

    def call_home(self):
        home = AtHome(
            fish_rod=self.fish_rod,
            fish_count=self.fish_count,
            fish_left=self.fish_left,
            worm_left=self.worm_left,
            money_in_wallet=self.money_in_wallet,
            colored_fish_list=self.colored_fish_list,
            caught_fish=self.caught_fish,
            type_worm=self.type_worm,
            level=self.level,
            cash=self.cash,
            pie=self.pie
        )
        home.mes_you_home()
        home.activation()


class AtHome(Fishing):
    fridge = []

    def __init__(self, fish_rod, fish_count: int, fish_left: int, worm_left, money_in_wallet, colored_fish_list: list,
                 caught_fish: list, type_worm: str, level: int, cash: int, pie: int,
                 inventar=0, dog_met=False, dog_eat=False, new_act=0):
        super().__init__(fish_rod, fish_count, fish_left, worm_left, money_in_wallet, colored_fish_list, caught_fish,
                         type_worm,
                         level, cash, pie)
        self.inventar = inventar
        self.dog_met = dog_met
        self.dog_eat = dog_eat
        self.new_act = new_act
        self.action()

    def mes_you_home(self):
        print("Ты вернулся домой!")
        self.new_friend()

    def action(self):
        self.list_at_home = {
            1: ("Холодильник", self.fridge_fun),
            2: ("Смотреть телевизор", self.tv),
            3: ("Стирать одежду", self.washing_clothes),
            4: ("Идти спать", self.good_night),
            5: ("Заварить чаю🍵", self.make_tea),
            6: ("Посмотреть в холодильник", self.see_fridge),
            7: ("Пойти на рыбалку", self.go_fishing),
            8: ("Посмотреть в кошелек", self.look_wallet),
            9: ("Продать рыбу на базаре", self.sell_fish),
            10: ("Сходить на ярмарку", self.go_fair),
        }
        if self.dog_met:
            self.list_at_home[11] = ("Покормить песика", self.feed_dog)

    def activation(self):
        self.action()
        for key, (desc, _) in self.list_at_home.items():
            print(f"{Fore.LIGHTCYAN_EX}{key}{Style.RESET_ALL}. {desc}")

        self.activ_at_home()

    def activ_at_home(self):
        try:
            if self.dog_met:
                self.choice = int(input("\nЧто хочешь сделать? (1-11) "))
            else:
                self.choice = int(input("\nЧто хочешь сделать? (1-10) "))

            if self.choice in self.list_at_home:
                list_at_home = self.list_at_home[self.choice][1]
                list_at_home()
            else:
                print("Неверный выбор! Попробуй еще :)")
                self.activ_at_home()
        except ValueError:
            print("Введи номер!")
            self.activ_at_home()

    def fridge_fun(self):
        global fridge
        quest1 = int(input("Положить в холодильник(1) или взять из холодильника(2): "))
        if quest1 == 1:
            quest2 = int(input("Положить пирог(1) или положить рыбу(2): "))
            if quest2 == 2:
                if not self.caught_fish:
                    print("У тебя нету рыбы!")
                    self.activation()
                else:
                    print(f"Ты положил рыбу: ")
                    for fish in self.caught_fish:
                        print(f"\t{self.color_fish(fish)}")
                    self.fridge.extend(list(self.caught_fish))
                    self.color_fish(self.fridge)
                    self.caught_fish.clear()
                    self.activation()
            elif quest2 == 1:
                if self.pie == 0:
                    print("У тебя нету пирогов! Сделай сначала квест")
                    self.activation()
                else:
                    print(f"Ты положил {self.pie} пирог(-а/-ов)")
                    self.name_pie = "Пирог"
                    self.fridge.extend([self.name_pie] * self.pie)
                    self.pie = 0
                    self.activation()
            else:
                print("Неверный ввод! Введи число!")
                self.activation()
        elif quest1 == 2:
            if self.fridge:
                print("В холодильнике: ")
                for fish in self.fridge:
                    print(f"\t{self.color_fish(fish)}")

                def take_fish():
                    user_input = 0
                    while self.fridge:
                        try:
                            user_input = input("Введи рыбку: ")
                            if not user_input:
                                print("Ты передумал?")
                                self.activation()
                            found_item = next(
                                (item for item in self.fridge if item['name'] == user_input), None)

                            if found_item:
                                self.fridge.remove(found_item)
                                self.caught_fish.append(found_item)
                                print(self.fridge)

                        except ValueError or TypeError:
                            print("Ой! Введи название рыбки!!")
                            take_fish()
                        if user_input == ' ':
                            self.activation()

                take_fish()

            else:
                print("У тебя нету рыбы!")
                self.activ_at_home()

    def tv(self):
        print(
            f"{Fore.YELLOW}Телевизор включен. Твоя спина отдыхает,\nи ты чувствуешь, как твои ноги тихо гудят от насыщеного дня...👌✨{Style.RESET_ALL}")
        self.random_visit()

    def washing_clothes(self):
        print(f"{Fore.YELLOW}Ты стираешь одежду. Числота - залог здоровья!🫧{Style.RESET_ALL}")
        self.activation()

    def good_night(self):
        print(
            f"{Fore.YELLOW}Спокойной ночи! Пусть тебе приснится самая большая рыбка🌞.\n---> Игра завершена.{Style.RESET_ALL}")
        exit()

    def check_tea(self):
        if self.inventar == 0:
            self.tea()
        else:
            self.make_tea()

    def see_fridge(self):
        if self.fridge:
            print("Там лежит: ")

            def show_fish():
                for fish in self.fridge:
                    print(f"\t{self.color_fish(fish)}")
                self.activation()

            show_fish()
        else:
            print("В холодильнике пусто 🪰")

    def feed_dog(self):
        if not self.dog_eat:
            for i in "Feed":
                print(f"{Fore.MAGENTA}{i}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Песик теперь сыт! Молодец :){Style.RESET_ALL}")
            self.dog_eat = True
            self.activation()
        else:
            print(f"{Fore.CYAN}Ты уже кормил его ранее){Style.RESET_ALL}")
            self.activation()

    def go_fishing(self):
        fishing = Fishing(
            fish_rod=self.fish_rod,
            fish_count=self.fish_count,
            fish_left=self.fish_left,
            worm_left=self.worm_left,
            money=self.money_in_wallet,
            colored_fish_list=self.colored_fish_list,
            caught_fish=self.caught_fish,
            type_worm=self.type_worm,
            level=self.level,
            cash=self.cash,
            pie=self.pie
        )
        fishing.list_activity()
        fishing.activation()

    def look_wallet(self):
        if self.money_in_wallet > 0:
            print(f"У тебя есть {Fore.GREEN}{self.money_in_wallet}{Style.RESET_ALL} рублей")
            self.activation()
        else:
            print(f"Ухты у тебя целых {self.money_in_wallet} рублей. Одни мухи!🪰🤯")
            self.activation()

    def go_fair(self):
        fair = Fair(fish_rod=self.fish_rod,
                    type_worm=self.type_worm,
                    money_in_wallet=self.money_in_wallet,
                    fish_left=self.fish_left,
                    fish_count=self.fish_count,
                    worm_left=self.worm_left,
                    colored_fish_list=self.colored_fish_list,
                    caught_fish=self.caught_fish,
                    level=self.level,
                    cash=self.cash,
                    pie=self.pie)
        fair.message()

    def random_visit(self):
        visit = random.randint(0, 1)
        if visit == 0:
            self.activation()
        else:
            print(f"В гости наведался {Fore.YELLOW}Клим{Style.RESET_ALL}!")
            self.nardu_klim()

    def tea(self):
        mes = input("У тебя закончились травы. Пойдешь в горы? ")
        if mes.lower() == 'да':
            for i in 'going...':
                print(f"{Fore.BLUE}{i}{Style.RESET_ALL}")
            mountains = Mountains(
                fish_rod=self.fish_rod,
                money_in_wallet=self.money_in_wallet,
                caught_fish=self.caught_fish,
                worm_left=self.worm_left,
                fish_left=self.fish_left,
                inventar=self.inventar,
                dog_met=self.dog_met,
                new_act=self.new_act,
                type_worm=self.type_worm,
                level=self.level,
                cash=self.cash,
                pie=self.pie
            )
            mountains.message()

        elif mes.lower() == 'нет':
            print("Хорошо, не пойдем")
            self.activation()
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
        else:
            self.tea()

        def numbers():
            enter_numbers = input("Введи правильную последовательность цыфр: ")
            if enter_numbers == '1234':
                for tea in 'teaparty':
                    print(f"{Fore.BLUE}{tea}{Style.RESET_ALL}")
                self.inventar -= 1
                print("Аромат чай сводит тебя с ума! Вот что значит чай с горных растений..")
                print(f"У тебя осталось: {Fore.BLUE}{self.inventar}{Style.RESET_ALL} ")
                self.activation()
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

    def new_friend(self):
        print(self.new_act)
        if self.dog_met and self.new_act != 1:
            self.new_act = 1
            print(
                f"{Fore.GREEN}У тебя теперь есть друг!\n<Теперь тебе доступно больше действий в доме>{Style.RESET_ALL}")
            print(self.new_act)
            self.action()
            self.activation()
        else:
            self.action()
            self.activation()


class Mountains(AtHome):
    def __init__(self, fish_rod, fish_left: int, worm_left, money_in_wallet, caught_fish: list, type_worm: str,
                 level: int,
                 cash: int, pie: int,
                 inventar=0,
                 dog_met=False,
                 new_act=0):
        super().__init__(fish_rod, fish_left, worm_left, money_in_wallet, caught_fish, type_worm, level, cash, pie,
                         inventar, dog_met)
        self.max_length = 10
        self.qual_tea = 0
        self.dog_met = dog_met
        self.money = money_in_wallet

    def message(self):
        print(f"{Fore.GREEN}Вы добрались до богатой поляны{Style.RESET_ALL}")
        print(self.dog_met)
        self.for_dog()
        self.random_tea()

    def for_dog(self):
        if self.dog_met == False and random.randint(0, 1) == 1:
            self.dog_met = True
            print(f"{Fore.YELLOW}Вам встретился одинокий песик!{Style.RESET_ALL}")
            name = input("Как назовешь? ")
            print(f"Ухты! Теперь {Fore.YELLOW}{name}{Style.RESET_ALL} будет твоим верным другом")
            return self.dog_met == True

    def trade(self):
        random_trader = random.randint(0, 1)
        if random_trader == 0:
            self.return_home()
        else:
            print(f"{Fore.YELLOW}Тебе встретился торговец удочками!{Style.RESET_ALL}")

            def want():
                print(self.money)
                yes_no = input("Хочешь купить у него что-то?(да/нет) ")
                if yes_no.lower() == 'да':
                    self.fish_rod_list = {
                        1: ("Бамбуковая удочка", 1000),
                        2: ("Спиннинг удочка", 2500),
                        3: ("Карповая удочка", 4000)
                    }
                    for key, (name, price) in self.fish_rod_list.items():
                        print(f"{key}. {name} - {price} руб.")

                    def which_f():
                        try:
                            buy = int(input("Какую купишь? (введи номер): "))
                            if buy in self.fish_rod_list:
                                name, price = self.fish_rod_list[buy]
                                if int(self.money) < price:
                                    print(f"Тебе не хватает {price - self.money} рублей!")
                                    self.return_home()
                                else:
                                    self.money -= price
                                    self.fish_rod = name  # Теперь сохраняем правильную удочку
                                    print(f"Ты купил {name}! У тебя осталось {self.money} руб.")
                                    self.return_home()
                            else:
                                print("Неверный ввод!")
                                which_f()
                        except ValueError:
                            print("Нужно ввести число")
                            which_f()

                    which_f()

                elif yes_no.lower() == "нет":
                    self.return_home()
                else:
                    print("ОЙ, введи да/нет!")
                    want()

            want()

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
                    self.trade()
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

        self.trade()

    def return_home(self):
        print(self.dog_met)
        for i in "Возвращение домой...":
            print(f"{Fore.CYAN}{i}{Style.RESET_ALL}", end='', flush=True)
        print()
        home = AtHome(
            fish_rod=self.fish_rod,
            fish_count=self.fish_count,
            fish_left=self.fish_left,
            worm_left=self.worm_left,
            money_in_wallet=self.money_in_wallet,
            colored_fish_list=self.colored_fish_list,
            caught_fish=self.caught_fish,
            inventar=self.inventar,
            dog_met=self.dog_met,
            type_worm=self.type_worm,
            level=self.level,
            cash=self.cash,
            pie=self.pie
        )
        home.mes_you_home()
        home.activation()


class Fair(Fishing):
    dialog = 0
    pozghe = 0
    first_meet = False

    def __init__(self, fish_rod: str, fish_count: int, fish_left: int, worm_left: int, money_in_wallet: int,
                 colored_fish_list: list, caught_fish: list, type_worm: str, level: int, cash: int, pie: int):
        super().__init__(fish_rod, fish_count, fish_left, worm_left, money_in_wallet, colored_fish_list, caught_fish,
                         type_worm, level, cash, pie)
        self.pie = pie

    def message(self):
        print(f"{Fore.GREEN}Ты добрался до ярмарки!{Style.RESET_ALL}")
        self.activity()

    def activity(self):
        self.list_activ = {
            1: ("Поговорить с Тамарой Игнатьевной", self.run_tamara),
            2: ("Купить новую приманку у Степановича", self.buy_bait),
            3: ("Купить лодку у Карыча", self.buy_boat),
            4: ("Купить домашних животных у фермера Виктора", self.buy_animals),
            5: ("Вернуться домой", self.return_home)
        }
        for key, (desc, _) in self.list_activ.items():
            print(f"{Fore.LIGHTCYAN_EX}{key}{Style.RESET_ALL}. {desc}")
        self.choose_action()

    def choose_action(self):
        try:
            self.choice = int(input("\nВыбери действие: "))
            if self.choice in self.list_activ:
                list_activ = self.list_activ[self.choice][1]
                list_activ()
            else:
                print("Неверный выбор! Попробуй еще :)")
                self.activity()
        except ValueError:
            print(f"{Fore.RED}Введи номер!{Style.RESET_ALL}")
            self.choose_action()

    def talk_with_Tamara(self, character, text):
        border = "─" * (len(text) + 12)
        print(f"┌{border}┐")
        print(f"| {character}: {text} |")
        print(f"└{border}┘")

    def run_tamara(self):
        global dialog, pozghe, first_meet
        self.fish_ = 0
        if not self.first_meet:
            self.talk_with_Tamara("🐟 Рыбак", "Сегодня отличный день для ярмарки!")
            self.talk_with_Tamara("👩‍🦰 Тамара", "Хе-хе! Рыбак, береги кости!")
            self.talk_with_Tamara("🐟 Рыбак", "Что??")
            self.talk_with_Tamara("👩‍🦰 Тамара",
                                  f"Грр! Берегись открытого океана, ибо могущественные {Fore.BLUE}whale{Style.RESET_ALL} рядом...")
            self.talk_with_Tamara("🐟 Рыбак", "Ладно..")
            self.first_meet = True
            self.choose_action()

        if self.dialog == 0 and self.first_meet:
            if self.level > 2 or self.level == 2:
                self.dialog = 1
                self.talk_with_Tamara("👩‍🦰 Тамара", "Хо-х! Рыбак, я вижу ты уже продвинутый малый!")
                self.talk_with_Tamara("👩‍🦰 Тамара", "Шучу!")
                self.talk_with_Tamara("👩‍🦰 Тамара",
                                      f"Но если у тебя будет {Fore.LIGHTBLACK_EX}3 шт{Style.RESET_ALL} лишней рыбки,"
                                      f"\n             то я приготовлю тебе кое-что😋")
                self.talk_with_Tamara("🐟 Рыбак", "Ладно..")
                self.dialog = 1
                self.choose_action()
        if self.dialog == 1 and self.pozghe != 1:
            print(f"{Fore.RED}Осторожно! Если ты вместо рыбки введешь 'Пробел'\nили просто нажмешь 'Enter',"
                  f"\nты потеряешь всю рыбу, которую отдал Тамаре!{Style.RESET_ALL}")
            give_fish = input(f"Хочешь отдать Тамаре {Fore.LIGHTBLACK_EX}3 шт{Style.RESET_ALL} рыбки? (да/нет) ")
            if give_fish.lower() == 'да':
                def give_fish():
                    if self.caught_fish:
                        def dec_():
                            for fish in self.caught_fish:
                                print(self.color_fish(fish['name']))

                        dec_()
                        while self.fish_ != 3:
                            try:
                                self.which_fish = input("Какую отдашь? ").strip()  # Убираем пробелы по краям
                                if not self.which_fish:  # Проверяем, ввел ли пользователь пустую строку (если self.which_fish пустая или None)
                                    print(f"{Fore.YELLOW}Ты передумал? Возвращаемся в меню действий!{Style.RESET_ALL}")
                                    self.choose_action()
                                found_fish = next(
                                    (fish for fish in self.caught_fish if fish['name'] == self.which_fish), None)

                                if found_fish:
                                    self.caught_fish.remove(found_fish)
                                    self.fish_ += 1
                                    print(self.caught_fish)
                                else:
                                    print("Ой! Такой рыбки у тебя нет, попробуй еще раз!")

                            except Exception as e:
                                print(f"Ошибка: {e}")

                    if self.fish_ == 3:
                        self.pozghe = 1
                        self.talk_with_Tamara("👩‍🦰 Тамара", "Хо-хо! Рыбак, приходи позже!")
                        self.choose_action()

                give_fish()
        if self.pozghe == 1:
            self.talk_with_Tamara("👩‍🦰 Тамара", "Рыбак, а вот и твой рыбный пирог🥧!")
            self.pie += 1
            print(f"У тебя есть {Fore.CYAN}{self.pie}{Style.RESET_ALL} пирог(а/ов)")
        self.activity()

    def buy_bait(self):
        print("Вот какие приманки есть у Степановича: ")
        self.bait = {
            1: ("A-червячок", 20, Fore.GREEN),
            2: ("B-червячок", 50, Fore.BLUE),
            3: ("C-червячок", 100, Fore.CYAN),
            4: ("D-червячок", 250, Fore.MAGENTA),
            5: ("S-червячок", 470, Fore.RED)
        }

        for key, (name, price, color) in self.bait.items():
            print(f"{key}. {color}{name}{Style.RESET_ALL} - {price} руб")

        def which_f():
            try:
                buy = int(input("Какую купишь? (введи номер): "))
                if buy in self.bait:
                    name, price, color = self.bait[buy]
                    if int(self.money_in_wallet) < price:
                        print(f"Тебе не хватает {price - self.money_in_wallet} рублей!")
                        self.activity()
                    else:
                        self.money_in_wallet -= price
                        self.type_worm = name
                        print(f"Ты купил {color}{name}{Style.RESET_ALL}! У тебя осталось {self.money_in_wallet} руб.")
                        self.activity()
                else:
                    print("Неверный ввод!")
                    which_f()
            except ValueError:
                print("Нужно ввести число")
                which_f()

        which_f()
        self.activity()

    def buy_boat(self):
        pass
        self.activity()

    def buy_animals(self):
        pass
        self.activity()

    def return_home(self):
        home = AtHome(self.fish_rod, self.fish_count, self.fish_left, self.worm_left,
                      self.money_in_wallet, self.colored_fish_list, self.caught_fish, self.type_worm, self.level,
                      self.cash, self.pie)
        # fish_rod, fish_count, fish_left, worm_left, money, colored_fish_list, caught_fish, type_worm
        home.activation()


class OceanJourney:
    pass


def start():
    if __name__ == '__main__':
        fishing = Fishing(fish_rod="Обычная удочка", money=0, fish_count=3, fish_left=0, worm_left=0,
                          colored_fish_list=[],
                          caught_fish=[{'name': 'бычок', 'price': 40}, {'name': 'бычок', 'price': 40},
                                       {'name': 'карасик', 'price': 50}], type_worm="None", level=2, cash=0, pie=0)
        fishing.list_activity()
        fishing.activation()


# start()

# home = AtHome(inventar=0, caught_fish=[], money=3000, fish_rod="Обычная удочка")
# home.activation()
# moun = Mountains(money=3000, fish_rod="Обычная удочка", fish_left=0, worm_left=0, caught_fish=[])
# moun.message()

fair = Fair(fish_rod="Обычная удочка", fish_count=0, fish_left=0, money_in_wallet=300,
            colored_fish_list=[],
            caught_fish=[{'name': 'бычок', 'price': 40}, {'name': 'бычок', 'price': 40},
                         {'name': 'карасик', 'price': 50}],
            worm_left=0, type_worm='None', level=3, cash=0, pie=0)
fair.activity()
fair.choose_action()

'''Доработать механику:
 "положить пирог и рыбу в холодильник + возможность достать 
                конкретную рыбку и пирог(к-во)" '''
