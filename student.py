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

def search_student(keyword):
    found = False
    print(f"\nKết quả tìm kiếm cho '{keyword}':")
    for st in students_db:
        if keyword.lower() in st['name'].lower() or keyword == st['id']:
            print(f"ID: {st['id']} | Tên: {st['name']} | Tuổi: {st['age']}")
            found = True
    if not found:
        print("⚠️ Không tìm thấy sinh viên nào!")
        
def display_students():
    if not students_db:
        print("⚠️ Danh sách sinh viên hiện đang trống!")
        return
    print("\nDanh sách sinh viên:")
    for st in students_db:
        print(f"ID: {st['id']} | Tên: {st['name']} | Tuổi: {st['age']}")

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
