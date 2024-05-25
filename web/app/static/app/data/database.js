// database.js

// Khởi tạo biến global để lưu trữ dữ liệu từ cơ sở dữ liệu
// var list_products = [];

// // Hàm để tải dữ liệu từ API endpoint /api/database
// function fetchDataFromDatabase() {
//     console.log('Data from database:')
//     fetch('api/product') // Gọi API endpoint /api/database
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.json();
//         })
//         .then(data => {
//             // Gán dữ liệu từ API vào biến databaseData
//             list_products = data;
//             console.log('Data from database:', list_products);
//         })
//         .catch(error => console.error('Error fetching data from database:', error));
// }

// // Gọi hàm fetchDataFromDatabase để tải dữ liệu khi trang được tải
// fetchDataFromDatabase();

var list_products = [];

const sqlite3 = require('sqlite3').verbose();

// Kết nối tới cơ sở dữ liệu
let db = new sqlite3.Database('./db.sqlite3', (err) => {
  if (err) {
    console.error('Không thể kết nối tới cơ sở dữ liệu:', err.message);
  } else {
    console.log('Kết nối thành công tới cơ sở dữ liệu.');
  }
});

// Hàm để lấy dữ liệu từ bảng app_product
function fetchProducts() {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM app_product', [], (err, rows) => {
      if (err) {
        reject(err);
      } else {
        resolve(rows);
      }
    });
  });
}

// Sử dụng hàm fetchProducts để lấy dữ liệu và in ra console
fetchProducts()
  .then((products) => {
    list_products = products;
    console.log('Dữ liệu sản phẩm từ cơ sở dữ liệu:', products);
  })
  .catch((error) => {
    console.error('Lỗi khi lấy dữ liệu sản phẩm:', error);
  })
  .finally(() => {
    // Đóng kết nối tới cơ sở dữ liệu sau khi hoàn thành
    db.close((err) => {
      if (err) {
        console.error('Lỗi khi đóng kết nối tới cơ sở dữ liệu:', err.message);
      } else {
        console.log('Đã đóng kết nối tới cơ sở dữ liệu.');
      }
    });
  });