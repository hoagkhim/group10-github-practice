# Danh sách lưu trữ sinh viên (Mô phỏng Database)
students_db = []

def add_student(student_id, name, age):
    student = {
        "id": student_id,
        "name": name,
        "age": age
    }
    students_db.append(student)
    print(f"✅ Đã thêm sinh viên '{name}' thành công!")

def display_students():
    """
    TODO: THÀNH VIÊN 2
    Nhiệm vụ: Kiểm tra nếu danh sách trống thì báo lỗi, nếu có thì in ra danh sách
    """
    pass

def search_student(keyword):
    """
    TODO: THÀNH VIÊN 3
    Nhiệm vụ: Tìm sinh viên có tên hoặc id trùng với keyword và in ra
    """
    pass

def delete_student(student_id):
    """
    TODO: THÀNH VIÊN 4
    Nhiệm vụ: Tìm và xóa sinh viên có student_id khỏi students_db
    """
    pass
