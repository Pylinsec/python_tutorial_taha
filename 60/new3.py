from faker import Faker

f = Faker()
# for i in range(10):
#     print(f.first_name() , f.last_name(),f.birth_date(),f.month())
for i in range(50):
    print(f.currency())

# print(dir(Faker()))