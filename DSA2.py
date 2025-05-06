class Record:
    def __init__(self):
        self.key = -1
        self.clnt_name = "NULL"

class Dictionary:
    def __init__(self):
        self.h = [Record() for _ in range(10)]

    def add_record(self):
        ent = 0
        while True:
            if ent >= 10:
                print("\nHash table is full")
                break

            k = int(input("\nEnter telephone No.: "))
            n = input("Enter client name: ")
            hi = k % 10
            flag = False

            if self.h[hi].key == -1:
                self.h[hi].key = k
                self.h[hi].clnt_name = n
            else:
                if self.h[hi].key % 10 != hi:
                    # Replace and reinsert old value
                    temp = self.h[hi].key
                    ntemp = self.h[hi].clnt_name
                    self.h[hi].key = k
                    self.h[hi].clnt_name = n
                    for i in range(hi + 1, 10):
                        if self.h[i].key == -1:
                            self.h[i].key = temp
                            self.h[i].clnt_name = ntemp
                            flag = True
                            break
                else:
                    # Linear probing
                    for i in range(hi + 1, 10):
                        if self.h[i].key == -1:
                            self.h[i].key = k
                            self.h[i].clnt_name = n
                            flag = True
                            break
                    if not flag:
                        for i in range(0, hi):
                            if self.h[i].key == -1:
                                self.h[i].key = k
                                self.h[i].clnt_name = n
                                break

            ent += 1
            ans = input("\nDo you want to insert more keys (y/n)? ")
            if ans.lower() != 'y':
                break

    def show(self):
        print("\n\tkey\t\tClnt_name")
        for i in range(10):
            print(f"\th[{i}]\t\t{self.h[i].key}\t\t{self.h[i].clnt_name}")

    def search(self, k):
        for i in range(10):
            if self.h[i].key == k:
                print(f"\n\t{k} is found at {i} Location with Client {self.h[i].clnt_name}")
                return i
        return -1

    def delete_rec(self, k):
        index = self.search(k)
        if index == -1:
            print("\nKey not found")
        else:
            self.h[index].key = -1
            self.h[index].clnt_name = "NULL"
            print("\n\tKey is deleted")

def main():
    d = Dictionary()
    while True:
        print("\n\t***Telephone (ADT)***")
        print("1.Insert\n2.Display\n3.Find\n4.Delete\n5.Exit")
        ch = int(input("Select your choice: "))

        if ch == 1:
            d.add_record()
        elif ch == 2:
            d.show()
        elif ch == 3:
            k = int(input("Enter key to be searched: "))
            index = d.search(k)
            if index == -1:
                print("\nKey not found")
        elif ch == 4:
            k = int(input("Enter element to be deleted: "))
            d.delete_rec(k)
        elif ch == 5:
            break
        else:
            print("Invalid choice")

        ans = input("\nDo you want to continue Menu (y/n)? ")
        if ans.lower() != 'y':
            break

if __name__ == "__main__":
    main()
