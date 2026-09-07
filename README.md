# Trò chơi Đoán chữ (Hangman)

## Cài đặt và chạy

Yêu cầu Python 3. Không cần cài thư viện ngoài.

```bash
python main.py
```

## Chạy test
- vào terminal trong file và chạy code, nếu window thì gõ như sau:
- kiểm tra từng case

```bash
python -m unittest test_game.py -v
```
- kiểm tra nhanh:

```bash
python -m unittest test_game.py 
```

 Bao gồm các trường hợp bắt buộc: đoán đúng, đoán sai, đoán trùng, thắng và thua, tự động hiển thị và xử lí từ có dấu - 

## Cấu trúc

- `game.py`: luật chơi độc lập, không dùng `input` hoặc `print`.
- `main.py`: giao diện console và chọn từ ngẫu nhiên.
- `words.txt`: danh sách 30 từ riêng biệt.
- `test_game.py`: unit test cho phần logic.



## Đoạn mơ hồ
### 1. Danh sách hiện chữ đoán
- Luật số 3 yêu cầu danh sách đoán sai, chức năng F2: yêu cầu các chữ đã đoán
=> hiện cả 2 dòng riêng biệt chữ đoán đúng và đoán sai
### 2. Định dạng từ bí mật
- từ vựng trong 1 danh sách có thể có khoảng trắng hoặc gạch ngang
=> khoảng trắng tự động hiển thị, không tính là 1 phần đoán
### 3. giả định bộ 30 từ đều là từ tiếng anh
### 5. Chơi lại:
- từ mới có thể trùng từ cũ không
=> chọn ngẫy nhiên có thể trùng
## Quyết định thiết kế

- Mỗi ván có đúng 6 lượt đoán sai.
- Tất cả từ trong `words.txt` là một từ tiếng Anh chỉ gồm chữ cái để phần xử lý đơn giản nhất.
- Chữ hoa và chữ thường được chuyển về chữ thường trước khi so sánh.
- Input không hợp lệ và chữ đã đoán không bị trừ lượt.
- Không triển khai các mục nâng cao vì đây là phiên bản tối thiểu.
## Nếu có thêm thời gian

Có thể thêm độ khó, gợi ý, chủ đề, điểm số, từ tiếng Việt và giao diện web.
