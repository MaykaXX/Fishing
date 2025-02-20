import random
from traceback import print_tb

import colorama
from colorama import Fore, Style
from pyexpat.errors import messages

colorama.init()


class Fishing:
    def __init__(self):
        self.worm_wrong_enter = 0
        self.fish_count = 0
        self.fish_left = 0
        self.qualit_worm = 0
        self.worm_left = 0
        self.money = 0
        self.fish_rod = "Обычная удочка"
        self.colored_fish_list = []
        self.caught_fish = []  # список пойманой рыбы

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
            print(f"{key}. {desc}")

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
        self.worm_()

    def worm_(self):
        while True:
            while self.worm_left > 0:
                print(self.fish_rod)
                worm = input("Наживить червя на крючок? ")
                if worm.lower() == 'да':
                    self.qualit_worm -= 1
                    self.worm_left = self.qualit_worm
                    throw_into = input("Закинуть приманку в пруд? ")
                    if throw_into.lower() == 'да':
                        lucky = random.randint(0, 100)
                        if lucky >= 75:
                            print(lucky)
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
        lucky = random.randint(0, 1000)
        if lucky < 400:
            print(lucky)
            fish_list = fish_list[:12]
        elif lucky < 600:
            print(lucky)
            fish_list = fish_list[13:18]
        elif lucky < 700:
            print(lucky)
            fish_list = fish_list[19:21]
        elif lucky < 900:
            print(lucky)
            fish_list = fish_list[22:23]
        elif lucky < 999:
            print(lucky)
            fish_list = fish_list[24:26]
        else:
            print(lucky)
            fish_list = fish_list[27:28]

        random_fish = random.choice(fish_list)
        print(f"Вы поймали: {self.color_fish(random_fish)}!\n"
              f"Цена: {random_fish['price']} рублей")
        return random_fish

    def color_fish(self, fish):
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
            while self.caught_fish != 0:
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
        home = AtHome(self.caught_fish, self.money, self.fish_rod)
        home.mes_you_home()
        home.activation()


class AtHome(Fishing):
    fridge = []

    def __init__(self, caught_fish, money, fish_rod, inventar=0, dog_met=False):
        super().__init__()
        self.caught_fish = caught_fish
        self.money = money
        self.fish_rod = fish_rod
        self.inventar = inventar
        self.dog_met = dog_met
        self.dog_eat = False
        self.action()

    def mes_you_home(self):
        print("Ты вернулся домой!")

    def action(self):
        self.list_at_home = {
            1: ("Положить рыбу в холодильник", self.fridge_fun),
            2: ("Смотреть телевизор", self.tv),
            3: ("Стирать одежду", self.washing_clothes),
            4: ("Идти спать", self.good_night),
            5: ("Заварить чаю🍵", self.make_tea),
            6: ("Посмотреть в холодильник", self.see_fridge),
            7: ("Пойти на рыбалку", self.go_fishing),
            8: ("Посмотреть в кошелек", self.look_wallet),
            9: ("Продать рыбу на базаре", self.sell_fish)
        }
        if self.dog_met:
            self.list_at_home[10] = ("Покормить песика", self.feed_dog)

    def activation(self):
        self.action()
        for key, (desc, _) in self.list_at_home.items():
            print(f"{key}. {desc}")

        self.activ_at_home()

    def activ_at_home(self):
        try:
            self.choice = int(input("\nЧто хочешь сделать? (1-9) "))

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
        if self.caught_fish != 0:
            print(f"Ты положил рыбу: ")
            for fish in self.caught_fish:
                print(f"\t{self.color_fish(fish)}")
            self.fridge.extend(self.caught_fish)
            self.caught_fish = []
            self.activation()
        else:
            print("У тебя нету рыбы!")
            self.activation()

    def tv(self):
        print(
            f"{Fore.YELLOW}Телевизор включен. Твоя спина отдыхает,\nи ты чувствуешь, как твои ноги тихо гудят от насыщеного дня...👌✨{Style.RESET_ALL}")
        self.random_visit()

    def washing_clothes(self):
        print(f"{Fore.YELLOW}Ты стираешь одежду. Числота - залог здоровья!🫧{Style.RESET_ALL}")
        self.activation()

    def good_night(self):
        print(
            f"{Fore.YELLOW}Спокойной ночи! Пусть тебе приснится самая большая рыбка🌞.\nИгра завершена.{Style.RESET_ALL}")
        exit()

    def check_tea(self):
        if self.inventar == 0:
            self.tea()
        else:
            self.make_tea()

    def see_fridge(self):
        print("У тебя есть: ")

        def show_fish():
            for fish in self.fridge:
                print(f"\t{self.color_fish(fish)}")
            self.activation()

        show_fish()

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
        fishing = Fishing()
        fishing.money = self.money  # Передаём деньги на рыбалку
        fishing.fish_rod = self.fish_rod  # Передаём удочку на рыбалку
        start()

    def look_wallet(self):
        if self.money > 0:
            print(f"У тебя есть {Fore.GREEN}{self.money}{Style.RESET_ALL} рублей")
            self.activation()
        else:
            print(f"Ухты у тебя целых {self.money} рублей. Одни мухи!🪰🤯")
            self.activation()

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
            mountains = Mountains(self.fish_rod, self.money, self.dog_met)
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
        if not self.dog_met:
            self.dog_met = True
            print(
                f"{Fore.GREEN}У тебя теперь есть друг!\n<Теперь тебе доступно больше действий в доме>{Style.RESET_ALL}")
        self.action()
        self.activation()


class Mountains(AtHome):
    dog_met = False

    def __init__(self, money, fish_rod, dog_met):
        self.money = money
        self.fish_rod = fish_rod
        self.dog_met = dog_met

        super().__init__(caught_fish=0, money=self.money, fish_rod=self.fish_rod, inventar=0, dog_met=self.dog_met)
        self.max_length = 10
        self.qual_tea = 0

    def message(self):
        print(f"{Fore.GREEN}Вы добрались до богатой поляны{Style.RESET_ALL}")
        self.for_dog()
        self.random_tea()

    def for_dog(self):
        global dog_met
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
                yes_no = input("Хочешь купить у него что-то?(да/нет) ")
                if yes_no.lower() == 'да':
                    fish_rod_list = {
                        1: ("Бамбуковая удочка", 1000),
                        2: ("Спиннинг удочка", 2500),
                        3: ("Карповая удочка", 4000)
                    }
                    for key, (name, price) in fish_rod_list.items():
                        print(f"{key}. {name} - {price} руб.")

                    def which_f():
                        try:
                            buy = input("Какую купишь? (введи номер): ")
                            if buy.isdigit() and int(buy) in fish_rod_list:
                                buy = int(buy)
                                name, price = fish_rod_list[buy]
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
                    which_f()                                  #Введите число!

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
        home = AtHome(inventar=self.inventar, caught_fish=0, fish_rod=self.fish_rod, dog_met=self.dog_met,
                      money=self.money)
        home.mes_you_home()
        home.activation()


def start():
    if __name__ == '__main__':
        fishing = Fishing()
        fishing.list_activity()
        fishing.activation()


start()

# home = AtHome(inventar=0, caught_fish=[], money=3000, fish_rod="Обычная удочка")
# home.activation()
# moun = Mountains(money=3000, fish_rod="Обычная удочка")
# moun.message()
