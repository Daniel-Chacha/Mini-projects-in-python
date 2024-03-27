from faker import Faker
import pyperclip
fake=Faker()

identity=[]

identity.append(fake.name())
identity.append(fake.address())
identity.append(fake.text())
identity.append(fake.email())
identity.append(fake.country())
identity.append(fake.longitude())
identity.append(fake.latitude())
identity.append(fake.url())
identity.append(fake.phone_number())
identity.append(fake.password())

for x in range(len(identity)):
    print(identity[x])



#pyperclip.copy(str(identity))