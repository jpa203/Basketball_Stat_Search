class Player:
    """
    A class to create a Player  profile using five arguments.
    """
    def __init__(self, first_name, last_name, height, weight, college):
        """
        :param first_name: player's first name
        :param last_name: player's last name
        :param height: player's height
        :param weight: player's weight
        :param college: college player attended
        """
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.college = college
        self.__best_player = 'Michael Jordan is the best!'

    def my_func(self):
        """
        :return: a string describing player details in eligible format.
        """
        return (
            f'This is {self.first_name} {self.last_name}. He was {self.height} cm tall and weighed {self.weight} kg. '
            f'He played for the {self.college}.')

    def __hello(self):
        """
        :return: this is a private class
        """
        print('Hello to all programmers!')

    def best_player(self):
        """
        :return: this returns the private attribute __best__player
        """
        print(self.__best_player)

    def __repr__(self):
        """
        for developer use
        """
        return f'{self.first_name}, {self.last_name}, {self.height},{self.weight}, {self.college}'


if __name__ == '__main__':
    player = Player('Michael', 'Jordan', 198, 88, 'University of North Carolina')
    assert player.first_name == 'Michael'
    assert player.last_name == 'Jordan'
    assert player.height == 198
    assert player.weight == 88
    assert player.college == 'University of North Carolina'
    assert player.my_func() == 'This is Michael Jordan. He was 198 cm tall and weighed 88 kg. He played for the ' \
                               'University of North Carolina.'
