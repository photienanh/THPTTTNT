const sqlite3 = require('sqlite3').verbose();

// Kết nối tới cơ sở dữ liệu
let db = new sqlite3.Database('./db.sqlite3', (err) => {
  if (err) {
    console.error('Không thể kết nối tới cơ sở dữ liệu:', err.message);
  } else {
    console.log('Kết nối thành công tới cơ sở dữ liệu.');

    // Gọi hàm để lấy dữ liệu và xử lý
    db.all(`
      SELECT 
        p.id, p.name, p.company, p.img, p.price, p.star, p.rateCount,
        promo.name AS promo_name, promo.value AS promo_value,
        detail.screen, detail.os, detail.camera, 
        detail.camera_front, 
        detail.cpu, detail.sim, detail.ram, detail.rom, 
        detail.micro_usb, detail.battery
      FROM app_product p
      LEFT JOIN app_promo promo ON p.id = promo.id
      LEFT JOIN app_detail detail ON p.id = detail.id
    `, [], (err, rows) => {
      if (err) {
        console.error('Lỗi khi lấy dữ liệu sản phẩm:', err);
      } else {
        list_products = rows.map(product => ({
          masp: product.id,
          name: product.name,
          company: product.company,
          img: product.img,
          price: product.price,
          star: product.star,
          rateCount: product.rateCount,
          promo: {
            name: product.promo_name,
            value: product.promo_value
          },
          detail: {
            screen: product.screen,
            os: product.os,
            camera: product.camera,
            cameraFront: product.camera_front,
            cpu: product.cpu,
            sim: product.sim,
            ram: product.ram,
            rom: product.rom,
            microUSB: product.micro_usb,
            battery: product.battery
          }
        }));
        var list_products = list_products;
        console.log('Dữ liệu sản phẩm từ cơ sở dữ liệu:', list_products);
      }

      // Đóng kết nối tới cơ sở dữ liệu sau khi hoàn thành
      db.close((err) => {
        if (err) {
          console.error('Lỗi khi đóng kết nối tới cơ sở dữ liệu:', err.message);
        } else {
          console.log('Đã đóng kết nối tới cơ sở dữ liệu.');
        }
      });
    });
  }
});