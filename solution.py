#1
print(f'Hello, world! My name is Nguyen Trung Kien')

#---------
#2
name = input("Nhập tên: ")
age = int(input("Nhập tuổi: "))
height = float(input("Nhập chiều cao: "))
               
print(f'Tên của bạn {name}')
print(f'Tuổi của bạn {age}')
print(f'Chiều cao của bạn {height} m')

#---------
#3
string = str(input("Nhập chuỗi: "))

print(f'Độ dài chuỗi là: {len(string)}')
print(f'Chuỗi in hoa: {string.upper()}')
print(f'Chuỗi in thường: {string.lower()}')
print(f'Chuỗi đảo ngược: {string[::-1]}')

#---------
#4
s = "PythonProgramming"
print(f'6 ký tự đầu tiên: {s[:6]}')
print(f'8 ký tự cuối cùng: {s[-8:]}')
print(f'Kết hợp 2 phần trên: {s[:6] + s[-8:]}')

#---------
#5
# Khai báo danh sách các quốc gia
countries = ['Vietnam','Laos','Myanmar','Thailand','Cambodia']


print(f'Quốc gia thứ 3: {countries[2]}')

# Thêm một quốc gia mới ở cuối
countries.append('Malaysia')
print(f'Danh sách sau khi thêm quốc gia mới: {countries}')

# Thay thế quốc gia thứ 2 bằng một quốc gia khác
countries[1] = 'Singapore'
print(f'Danh sách sau khi thay thế: {countries}')

# Xóa
del countries[0]
print(f'Danh sách sau khi xóa quốc gia đầu tiên: {countries}')

#---------
#6

# Tạo một tuple có 4 phần tử: tên, tuổi, nghề nghiệp, thành phố.
person = ("Nguyễn Trung Kiên", 19, "Sinh viên", "Tp. Hồ Chí Minh")

# Sau đó ‘unpack’ ra các biến tương ứng rồi in ra các biến đó.
name, age, occupation, city = person
print(f'Tên: {name}')
print(f'Tuổi: {age}')
print(f'Nghề nghiệp: {occupation}')
print(f'Thành phố: {city}')

#---------
#7
number = [1, 2, 2, 3, 4, 4, 5]

set_number = set(number)

print(set_number)

#---------
#8
student = {
  "name": "An",
  "age": 21,
  "major": "Computer Science"
}

# In ra thông tin
print(f'Tên: {student["name"]}')
print(f'Tuổi: {student["age"]}')
print(f'Chuyên ngành: {student["major"]}')

# Cập nhật tuổi
student["age"] = 22
print(f'Tuổi sau khi cập nhật: {student["age"]}')

# Thêm GPA
student["GPA"] = 3.5
print(f'GPA: {student["GPA"]}')

# Xóa chuyên ngành
del student["major"]
print(f'Thông tin sinh viên sau khi xóa chuyên ngành: {student}')

#In cuối cùng
print(f'Thông tin sinh viên cuối cùng: {student}')

#---------
#9
#python 3.13.3

n = float(input("Nhập số n: "))

# if elif else
if (n > 0):
    print('Số dương')
elif (n < 0):
    print('Số âm')
else:
    print('Số không')

# match case
match n:
    case _ if n > 0:
        print('Số dương (sử dụng match case)')
    case _ if n < 0:
        print('Số âm (sử dụng match case)')
    case _:
        print('Số không (sử dụng match case)')

#---------
#10
print("Các số chẵn là:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#---------
#11
n = int(input("Nhập n: "))
i = 2
S = 1
while(i <= n):
    S += i
    i += 1
print(f'Tổng S từ 1 đến {n} = {S}')

#---------
#12
# Cho list: `[1,2,3,4,5,6,7,8,9,10]`.

# Sử dụng list comprehension để tạo một list mới chứa các bình phương (square) của các số chẵn từ list trên.

original_list = [1,2,3,4,5,6,7,8,9,10]
squared_evens = [x**2 for x in original_list if x % 2 == 0]
print(squared_evens)

#---------
#13
def greet(name, age):
    """In ra lời chào theo định dạng yêu cầu."""
    print(f'Xin chào {name}, bạn {age} tuổi.')

# Các lời gọi mẫu
greet("Kiên", 20)


#---------
#14
def describe_person(*args, **kwargs):
    """In ra các sở thích (args) và các thông tin khác (kwargs)."""
    if args:
        print("Sở thích:")
        for i, hobby in enumerate(args, 1):
            print(f'  {i}. {hobby}')
    else:
        print("Không có sở thích được cung cấp.")
    if kwargs:
        print("Thông tin khác:")
        for key, value in kwargs.items():
            print(f'  {key}: {value}')
    else:
        print("Không có thông tin bổ sung (kwargs).")

# Gọi mẫu
describe_person("đọc sách", "bóng đá", name="Kiên", age=19, city="Hà Nội")

#---------
#15
def factorial(n):
    """Hàm đệ quy trả về giai thừa của n (n!)."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

try:
    n_input = int(input("Nhập một số nguyên n để tính giai thừa: "))
    if n_input < 0:
        print("Không thể tính giai thừa của số âm.")
    else:
        print(f'{n_input}! = {factorial(n_input)}')
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")

#---------
#16
import math

x = float(input("Nhập số thực x: "))
print(f'Căn bậc hai của {x} là: {math.sqrt(x)}')
print(f'Làm tròn lên của {x} là: {math.ceil(x)}')

#---------
#17
# Tạo file data.txt và ghi 5 dòng tên học sinh
with open('data.txt', 'w') as f:
    f.write('Nguyen Van A\n')
    f.write('Tran Thi B\n')
    f.write('Le Van C\n')
    f.write('Pham Thi D\n')
    f.write('Hoang Van E\n')

# Đọc và in từng dòng
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip())

#---------
#18
try:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    if b == 0:
        raise ZeroDivisionError("Mẫu số không thể là 0")
    result = a / b
    print(f'Thương của {a} và {b} là: {result}')
except ValueError:
    print("Vui lòng nhập số hợp lệ.")
except ZeroDivisionError as e:
    print(e)

#---------
#19
import json

json_str = '{"name": "Mai", "age": 25, "city": "Hanoi"}'

# Chuyển chuỗi JSON thành dict
data = json.loads(json_str)

# In ra thông tin
print(f'Tên: {data["name"]}')
print(f'Tuổi: {data["age"]}')
print(f'Thành phố: {data["city"]}')

# Chuyển dict về JSON và in
json_output = json.dumps(data)
print(f'JSON: {json_output}')

#---------
#20
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

# Tạo vài đối tượng Car
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)

# In thông tin của mỗi chiếc
print(car1.get_info())
print(car2.get_info())
print(car3.get_info())