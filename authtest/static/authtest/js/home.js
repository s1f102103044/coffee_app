document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('flavor-form');
  form.addEventListener('submit', function(event) {
      event.preventDefault();
      const formData = new FormData(form);
      const flavors = formData.getAll('flavor');
      // ここでサーバーに送信するか、JavaScriptで結果を処理する
  });
});
