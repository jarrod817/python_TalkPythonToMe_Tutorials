import random, time

from actors import Creature, Wizard, SmallAnimal, Dragon

creatures = [
    SmallAnimal('Toad', 1),
    SmallAnimal('Bat', 3),
    Creature('Tiger', 10),
    Dragon('Dragon', 50),
    Wizard('Evil Wizard', 200)
]

hero = Wizard('Gandolf', 100)

creature = random.choice(creatures)


def main():
    print_header()
    run_event_loop()


def print_header():
    print('---------------------------------')
    print(''''
    (  )   /\   _                 (
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \\
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
     WIZARD BATTLE        )        \_____________  `              \  /
(__       APP      +- .( -'.- <. - _  VVVVVVV VV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \\
   ''')
    print('---------------------------------')


def run_event_loop():
    while True:
        active_creature = random.choice(creatures)
        print(
            'While walking in the forrest you walked up on a {} of level {}'.format(active_creature.name,
                                                                                    active_creature.level))
        print()
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            print('Attack!!')
            myrole = Wizard.get_defensive_roll(hero)
            creaturerole = Creature.get_defensive_roll(active_creature)
            if myrole >= creaturerole:
                print('You slayed the {}'.format(active_creature.name))
                creatures.remove(active_creature)
            else:
                print("You died at the hands(paws) of the {}".format(active_creature.name))
                time.sleep(5)
        elif cmd == 'r':
            print('Run away')

        elif cmd == 'l':
            print('Lookin cool!')
            for c in creatures:
                print('I spy a {} of level {} in those bushes'.format(c.name, c.level))

        else:
            print('bye!')
            break

        if creatures == []:
            print('You are truly a mighty wizard')
            break


if __name__ == "__main__":
    main()
