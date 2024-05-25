# Trang web điện thoại thông minh

# Người tạo
  - Nguyễn Duy Hậu : 22022586 
  - Nguyễn Xuân Hiệp : 22022591
  - Phó Viết Tiến Anh : 22022568
  - Nguyễn Phương Đông : 22022693

# Cách thức xây dựng
 - Khởi tạo dự án django bằng lệnh 'django-admin startproject web' và các file sau sẽ được tạo
    + _init_.py : file cơ bản trong foler
    + settings.py: file cấu hình project
    + urls.py: file tạo các đường dẫn urls của trang web
    + wsgi.py: file giúp deploy project lên server
    + manag.py: file khởi chạy server ảo
- Sau đó ta tạo 1 ứng dụng con phụ thược project web với lệnh 'django-admin startapp app'
    + Cấu hình app trong settings.py để liên kết ứng con app
         INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',]

    + Tạo folder template chứa các file html và các folder static chứa css,js,data,img và cấu hình chúng trong settings.py
    + Liên kết url của các file html trong template trong urls.py của dự án gốc web
- Cấu hình database sqlite và tạo các model bảng trong app/model.py
    tạo tài khoản superuser để quản lí database 
- kết nối với cơ sở dữ liệu để hiển thị sản phẩm
- Tạo môi trường Docker để thực thi dự án:
    + Tạo dockerfile: 
    
            FROM python:3.10

            ENV PYTHONUNBUFFERED = 1
            RUN pip install --upgrade pip

            WORKDIR /web

            COPY ./requirements.txt /web/requirements.txt
            RUN pip install -r requirements.txt
            COPY . . 
    + tạo docker-compose.yml:
            services:

              web:
                image: web
                build:
                  context: ./web
                container_name: "web"
                ports:
                  - "8080:8080"
                command: python manage.py runserver 0.0.0.0:8080
                  volumes:
                  - ./web:/web  
      + kết nối docker và chạy lệnh:
            - docker-compose up 
      để tạo container và image cho dự án
      + truy cập http://localhost:8080 để khởi chạy server web

# Cách thức sử dụng 
- Kết nối docker và thực thi lệnh 
      + ' docker-compose up'
    để xây dựng container và image của dữ án
- truy cập http://localhost:8080 khởi chạy web
- truy cập http://localhost:8080/admin và đăng nhập:
         -tài khoản: bonconsoi
         -mật khẩu: webmobile1234
    để truy cập trang admin quản lí database
    