from services.user_service import UsersService

service = UsersService()

print("=== USERS ===")
for u in service.list_all():
    print(vars(u))

print("\n=== FIND ===")
print(service.find_by_username("admin1"))