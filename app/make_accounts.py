from models import User, db
user = User.create("smitty1e@gmail.com", password="",name="smitty")
print(user.password_hash)
db.session.add(user)
db.session.commit()
user = User.create("admin@gmail.com", password="",name="admin")
print(user.password_hash)
db.session.add(user)
db.session.commit()
user = User.create("drow@gmail.com", password="",name="drow")
print(user.password_hash)
db.session.add(user)
db.session.commit()

