class Unit(object):

    def __init__(self, health, speed, hit_power):
        self.health = health
        self.speed = speed
        self.hit_power = hit_power

    def print_status(self, name='Unit'):
        print(name, 'status:')
        print('\tHealth: ', self.health)
        print('\tSpeed: ', self.speed)
        print('\tHit Power: ', self.hit_power)


class FriendlyUnit(Unit):

    tag = 'friendly_unit'

    def attack_enemy(self, other_health):
        other_health -= self.hit_power
        enemy.health = other_health


class EnemyUnit(Unit):

    tag = 'enemy_unit'

    def attack_unit(self, other_health):
        other_health -= self.hit_power
        my_player.health = other_health

my_player = FriendlyUnit(health=10, speed=4, hit_power=2)
my_player.print_status('Player')

enemy = EnemyUnit(health=12, speed=3, hit_power=3)
enemy.print_status('Enemy')

my_player.attack_enemy(enemy.health)
print('Enemy health left: ', enemy.health)

enemy.attack_unit(my_player.health)
print('Player health left:', my_player.health)
