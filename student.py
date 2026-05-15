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
    """
    TODO: THÀNH VIÊN 3
    Nhiệm vụ: Tìm sinh viên có tên hoặc id trùng với keyword và in ra
    """
    pass

def delete_student(student_id):
    """
    # TODO: THÀNH VIÊN 4
    # Nhiệm vụ: Tìm và xóa sinh viên có student_id khỏi students_db
    # """
    for i, st in enumerate(students_db):
        if st['id'] == student_id:
            del students_db[i]
            print(f"✅ Đã xóa sinh viên có ID '{student_id}' thành công!")
            return
    print(f"⚠️ Không tìm thấy sinh viên với ID '{student_id}'!")
    pass
