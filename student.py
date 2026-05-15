# Danh sách lưu trữ sinh viên (Mô phỏng Database)
students_db = []

def add_student(student_id, name, age):
    """
    TODO: THÀNH VIÊN 1
    Nhiệm vụ: Tạo một dictionary chứa thông tin sinh viên và thêm vào students_db
    """
    pass

def display_students():
    """
    TODO: THÀNH VIÊN 2
    Nhiệm vụ: Kiểm tra nếu danh sách trống thì báo lỗi, nếu có thì in ra danh sách
    """
    pass

def search_student(keyword):
    found = False
    print(f"\nKết quả tìm kiếm cho '{keyword}':")
    for st in students_db:
        if keyword.lower() in st['name'].lower() or keyword == st['id']:
            print(f"ID: {st['id']} | Tên: {st['name']} | Tuổi: {st['age']}")
            found = True
    if not found:
        print("⚠️ Không tìm thấy sinh viên nào!")

def delete_student(student_id):
    """
    TODO: THÀNH VIÊN 4
    Nhiệm vụ: Tìm và xóa sinh viên có student_id khỏi students_db
    """
    pass
