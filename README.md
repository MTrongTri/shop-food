# 📦 Shop Food

Mô tả: 
- Shop Food là Một website quản lý bán hàng được xây dựng bằng Django.

## 🔧 Công nghệ sử dụng

- Python 3.13.3
- Django 5.2.1
- MySQL
- Bootstrap, JQuery

## 📁 Cấu trúc thư mục chính

```bash
shop-food/
├── ecommerce/           # Thư mục cấu hình của Django
├── home/                # App home
├── products/            # App ptoducts
├── templates/           # Templates HTML
├── manage.py            # File điều khiển chính của Django
├── requirements.txt     # Danh sách các package Python
└── README.md            # Tệp hướng dẫn này
```
## 🚀 Cài đặt và chạy project
Nếu sử dụng file zip bỏ qua bước 1.

**1. Clone repo**
```bash
git clone https://github.com/MTrongTri/shop-food.git
cd shop-food
```

**2. Cài đặt các gói cần thiết**
```bash
pip install -r requirements.txt
```

**3. Cấu hình file .env (tạo 1 file tên .env ngang cấp với file manage.py)**
```ini
DB_NAME=YOUR_DB
DB_USER=YOUR_USER
DB_PASSWORD=YOUR_PASSWORD
DB_HOST=YOUR_HOST
DB_PORT=YOUR_PORT
```

**4. Chạy migrate để tạo các table (lưu ý phải tạo db trước)**
```bash
python manage.py migrate
```

**6. Chạy server**
```bash
python manage.py runserver
```

Truy cập tại: http://localhost:8000
