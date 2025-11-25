import os
from models.user import UserModel, DATA_DIR

print("DATA_DIR:", DATA_DIR)
print("FILE_PATH:", UserModel.FILE_PATH)
print("FILE EXISTS?:", os.path.exists(UserModel.FILE_PATH))

model = UserModel()
users = model.get_all()

print("QTD USERS:", len(users))
for u in users:
    print(vars(u))