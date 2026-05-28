# Input
# Người dùng nhập:
# room_count : số lượng phòng học (int)
# rows : số hàng ghế của phòng (int)
# cols : số ghế trên mỗi hàng (int)
# Output
# In sơ đồ chỗ ngồi bằng dấu *
# Hoặc thông báo lỗi theo từng trường hợp:
# Số lượng phòng học không hợp lệ
# Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này
# Phòng quá lớn. Dừng nhập dữ liệu
# Đề xuất giải pháp
# Ý tưởng xử lý

# Bước 1
# Nhập số lượng phòng học.
# Nếu room_count <= 0
# thông báo lỗi và kết thúc chương trình.
# Bước 2
# Dùng vòng lặp for để duyệt từng phòng học.
# Bước 3
# Nhập:
# số hàng ghế
# số ghế mỗi hàng
# Kiểm tra dữ liệu:
# Nếu rows <= 0 hoặc cols <= 0
# bỏ qua phòng hiện tại.
# Nếu rows > 10 hoặc cols > 10
# dừng toàn bộ chương trình.

# Bước 4
# Nếu dữ liệu hợp lệ:
# Dùng vòng lặp lồng nhau để in sơ đồ ghế:
# Vòng ngoài → số hàng
# Vòng trong → số ghế mỗi hàng

# Mô tả luồng chương trình
# Nhập số lượng phòng học.
# Nếu số lượng phòng <= 0, thông báo lỗi và kết thúc chương trình.
# Dùng vòng lặp để xử lý từng phòng học.
# Nhập số hàng ghế và số ghế mỗi hàng.
# Kiểm tra dữ liệu:
# Nếu số hàng hoặc số ghế <= 0, bỏ qua phòng đó.
# Nếu số hàng hoặc số ghế > 10, thông báo phòng quá lớn và dừng chương trình.
# Nếu dữ liệu hợp lệ:
# Dùng vòng lặp lồng nhau để in sơ đồ chỗ ngồi bằng dấu *.
# Kết thúc chương trình sau khi xử lý xong các phòng học.

room_count = int(input("Nhập số lượng phòng học: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")

else:
    for room in range(1, room_count + 1):

        print(f"\n--- Phòng học {room} ---")

        rows = int(input("Nhập số hàng ghế: "))
        cols = int(input("Nhập số ghế mỗi hàng: "))

        if rows <= 0 or cols <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        if rows > 10 or cols > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        print("Sơ đồ chỗ ngồi:")

        for i in range(rows):
            for j in range(cols):
                print("*", end="")

            print()