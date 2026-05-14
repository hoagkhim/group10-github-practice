from student import add_student, display_students, search_student, delete_student
from utils import print_header

def main():
    while True:
        print_header("QUẢN LÝ SINH VIÊN")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm sinh viên")
        print("4. Xóa sinh viên")
        print("5. Thoát")
        
        choice = input("Chọn chức năng (1-5): ")
        
        if choice == '1':
            print("\n[Chức năng đang được phát triển bởi Thành viên 1]")
            # TODO: Nhập thông tin sinh viên và gọi add_student()
        elif choice == '2':
            print("\n[Chức năng đang được phát triển bởi Thành viên 2]")
            # TODO: Gọi display_students()
        elif choice == '3':
            print("\n[Chức năng đang được phát triển bởi Thành viên 3]")
            # TODO: Nhập từ khóa và gọi search_student()
        elif choice == '4':
            print("\n[Chức năng đang được phát triển bởi Thành viên 4]")
            # TODO: Nhập ID và gọi delete_student()
        elif choice == '5':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

if __name__ == "__main__":
    main()
