#1
print(f'Hello, world! 
 My name is Nguyen Trung Kien')

#2
name = input("Nhập tên: ")
age = int(input("Nhập tuổi: "))
height = float(input("Nhập chiều cao: "))
               
print(f'Tên của bạn {name}')
print(f'Tuổi của bạn {age}')
print(f'Chiều cao của bạn {height} m')

#3
string = str(input("Nhập chuỗi: "))

print(f'Độ dài chuỗi là: {len(string)}')
print(f'Chuỗi in hoa: {string.upper()}')
print(f'Chuỗi in thường: {string.lower()}')
print(f'Chuỗi đảo ngược: {string[::-1]}')

#4
s = "PythonProgramming"
print(f'6 ký tự đầu tiên: {s[:6]}')
print(f'8 ký tự cuối cùng: {s[-8:]}')
print(f'Kết hợp 2 phần trên: {s[:6] + s[-8:]}')

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

#6

# Tạo một tuple có 4 phần tử: tên, tuổi, nghề nghiệp, thành phố.
person = ("Nguyễn Trung Kiên", 19, "Sinh viên", "Tp. Hồ Chí Minh")

# Sau đó ‘unpack’ ra các biến tương ứng rồi in ra các biến đó.
name, age, occupation, city = person
print(f'Tên: {name}')
print(f'Tuổi: {age}')
print(f'Nghề nghiệp: {occupation}')
print(f'Thành phố: {city}')

#7
number = [1, 2, 2, 3, 4, 4, 5]

set_number = set(number)

print(set_number)

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

#10
for i in range(10):
    print(i+1)

#11
n = int(input("Nhập n: "))
i = 2
S = 1
while(i <= n):
    S += i
    i += 1
print(f'Tổng S từ 1 đến {n} = {S}')

#12
# Cho list: `[1,2,3,4,5,6,7,8,9,10]`.

# Sử dụng list comprehension để tạo một list mới chứa các bình phương (square) của các số chẵn từ list trên.

original_list = [1,2,3,4,5,6,7,8,9,10]
squared_evens = [x**2 for x in original_list if x % 2 == 0]
print(squared_evens)

#13

#14

#15

#16

