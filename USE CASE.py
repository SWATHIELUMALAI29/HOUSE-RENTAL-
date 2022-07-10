class rent:
    def houses():
        area=input("which area you want: \n1:kodambakkam \n2:anna nagar \n3.goripalayam \n")
        if area=="1":
            data=["locality:kodambakkam","area:chennai","square_feet:798","type:2BHK","rent:rs.6000/month","owner_id=1"]
            for i in data:
                print(i)
        elif area=="2":
            data=["locality:anna nagar","area:chennai","square_feet:1200","type:3BHK","rent:rs.15000/month","owner_id=2"]
            for i in data:
                print(i)
        elif area=="3":
            data=["locality:goripalayam","area:madurai","square_feet:560","type:1BHK","rent:rs.5500/month","owner_id=2"]
            for i in data:
              print(i)
class tenant:
    def user_available():
        options = input("1:view houses  \n2:request  \n3:log out \n")
        if options == "1":
            data = rent
            content = data.houses()
        elif options == "2":
            print("which area do you prefer: ")
            data = rent
            content = data.houses()
        elif options == "3":
            print("THANK YOU! for your vist, you are logged out successfully")

class owner:
    def owner_req():
        options=input("1:Can create a request to post  \n2:Remove their house for rental \n")
        if options == "1":
            data = rent
            content = data.houses()
        elif options == "2":
            print("nO houses are available, all are booked")

class user_details:
    def details():
        data = input("chose users details: \n1:1st user \n2:2nd user \n3:3rd user  \n")
        if data == "1":
            datas = ["User Id:1", "Name:Lucifer", "Email:lucifer@gmail.com", "Mobile:9876543210", "Aadhaar:123412341234"]
            for i in datas:
                print(i)
        elif data == "2":
            datas = ["User Id:2", "Name:Peter Parker", "Email:perterparker@gmail.com", "Mobile:1234567890", "Aadhaar:567856785678"]
            for i in datas:
                print(i)
        elif data == "3":
            datas = ["User Id:3", "Name:Tony Stark", "Email:tonystark@gmail.com", "Mobile:1234509876", "Aadhaar:345634563456"]
            for i in datas:
                print(i)

class approver:
    def approver_req():
        options=input("choose the options: \n1:Can view all the User details \n2:Decline the request \n")
        if options =="1":
            data_ = user_details
            content = data_.details()
        elif options == "2":
            print("your request is declined")

if __name__ == "__main__":
    print("WELCOME TO HOUSE RENTAL PORTAL! \n HOW CAN I HELP YOU!")
    user = input("1:Tenant \n2:Owner \n3:Approver \n")
    if user == "1":
        option = tenant
        object = option.user_available()
    elif user == "2":
        option = owner
        object = option.owner_req()
    elif user == "3":
        option = approver
        object = option.approver_req()

