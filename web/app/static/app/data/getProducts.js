// Địa chỉ URL của API sản phẩm
const apiUrl = 'http://localhost:3000/api/products'; // Thay đổi URL nếu cần

var list_products = []

// Hàm để lấy dữ liệu từ API sản phẩm
async function getProducts() {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error('Lỗi khi lấy dữ liệu từ API');
    }
    const products = await response.json();
    return products;
  } catch (error) {
    console.error('Đã xảy ra lỗi:', error.message);
    return null;
  }
}

// Sử dụng hàm để lấy dữ liệu sản phẩm từ API và hiển thị ra console
getProducts()
  .then(products => {
    if (products) {
      list_products = products
      console.log('Dữ liệu sản phẩm từ API:', products);
    } else {
      console.log('Không thể lấy dữ liệu sản phẩm từ API.');
    }
  })
  .catch(error => console.error('Đã xảy ra lỗi khi lấy dữ liệu sản phẩm từ API:', error));
