<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <title>Phần mềm lưu trữ dữ liệu</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background: #f4f4f4;
    }
    h1 {
      color: #2c3e50;
    }
    .section {
      margin-top: 30px;
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    iframe, img {
      width: 100%;
      border: 1px solid #ccc;
      margin-top: 10px;
    }
    ul {
      list-style: none;
      padding: 0;
    }
    li {
      margin: 10px 0;
    }
    a {
      text-decoration: none;
      color: #2980b9;
    }
  </style>
</head>
<body>
  <h1>Phần mềm lưu trữ tài liệu và hình ảnh</h1>

  <div class="section">
    <h2>Ảnh minh họa</h2>
    <img src="demo_image.jpg" alt="Ảnh minh họa" />
  </div>

  <div class="section">
    <h2>Tài liệu PDF</h2>
    <iframe src="demo.pdf" height="500px"></iframe>
  </div>

  <div class="section">
    <h2>Tài liệu khác (Word, Excel...)</h2>
    <ul>
      <li><a href="demo.docx" download>Tải file Word: demo.docx</a></li>
      <li><a href="demo.xlsx" download>Tải file Excel: demo.xlsx</a></li>
      <li><a href="KHO%20D%E1%BB%AF%20LI%E1%BB%86U%20M%E1%BA%ACU.xlsx" download>Tải Kho Dữ Liệu Mẫu</a></li>
    </ul>
  </div>
</body>
</html>
