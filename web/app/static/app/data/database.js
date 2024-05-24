// database.js

// Khởi tạo biến global để lưu trữ dữ liệu từ cơ sở dữ liệu
var list_products = [];

// Hàm để tải dữ liệu từ API endpoint /api/database
function fetchDataFromDatabase() {
    fetch('/api/product') // Gọi API endpoint /api/database
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Gán dữ liệu từ API vào biến databaseData
            list_products = data;
            console.log('Data from database:', list_products);
        })
        .catch(error => console.error('Error fetching data from database:', error));
}

// Gọi hàm fetchDataFromDatabase để tải dữ liệu khi trang được tải
window.onload = function() {
    fetchDataFromDatabase();
};
