from faker import Factory
fake = Factory.create()

def create_post(title= fake.text(10), author = fake.name(), content = fake.text(50)):
    return {
        "title": title,
        "author": author,
        "content": content
    }