import random; from faker import Faker; import alg
fake = Faker()
class main:
    valid = False
    def __init__(self):
        while main.valid == False:
            card_num = random.randint(4000000000000000, 4999999999999999)
            if alg.luhn_checksum(card_num)== 0:
                main.valid = True
                print(str(card_num))
                print(random.randint(100, 900))
                print('{}/{}'.format(random.randint(1, 12), random.randint(22, 26)))
                print('{}, {}'.format(fake.name(), fake.address()))
            else:
                continue
main()
