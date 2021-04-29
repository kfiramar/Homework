import socket
Bank = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Bank.bind(('localhost', 8080))
Bank.listen(5)
Accounts_file = open("Accounts.txt", "r")
Accounts = Accounts_file.readlines()
while True:
    Connection, Address = Bank.accept()
    print(str(Connection))
    From_Client = ''
    while True:
        From_Client = Connection.recv(4096)
        if not From_Client: break
        From_Client = From_Client.decode('utf-8')
        print(From_Client)
        found = False
        User = ''
        Count = 0
        for line in Accounts:
            if From_Client in line:
                found = True
                Connection.send(("Approved").encode('utf-8'))
                User = line
                break
            Count += 1
        if found == False:
            Connection.send(("Denied").encode('utf-8'))
            break
        Connection.send(("How much money would you like to withdraw").encode('utf-8'))
        From_Client = Connection.recv(4096)
        if not From_Client: break
        From_Client = From_Client.decode('utf-8')
        Withdraw_Req = int(From_Client)
        Data = User.split(':')
        Balance = int(Data[2])
        if Balance >= Withdraw_Req:
            Balance -= Withdraw_Req
            Data[2] = str(Balance)
            User = ''
            for i in Data:
                User += i + ':'
            User = User[0:len(User) - 1] + "\n"
            Accounts[Count] = User
            Accounts_file = open("Accounts.txt", "w")
            Accounts_file.writelines(Accounts)
            Accounts_file.close()
        Connection.send(("balance= " + str(Balance)).encode('utf-8'))
        break
    break
Connection.close()
print ('client disconnected')