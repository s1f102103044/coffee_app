document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('drawCanvas');
  const ctx = canvas.getContext('2d');
  let isDrawing = false;
  let startX = 0;
  let startY = 0;
  let drawnPath = [];

  canvas.addEventListener('mousedown', (e) => {
      startX = e.offsetX;
      startY = e.offsetY;
      isDrawing = true;
      drawnPath = [{x: startX, y: startY}];
  });

  canvas.addEventListener('mousemove', (e) => {
      if (isDrawing) {
          const x = e.offsetX;
          const y = e.offsetY;
          drawnPath.push({x, y});
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          ctx.beginPath();
          ctx.moveTo(startX, startY);
          for (let point of drawnPath) {
              ctx.lineTo(point.x, point.y);
          }
          ctx.stroke();
      }
  });

  canvas.addEventListener('mouseup', () => {
      isDrawing = false;
      if (isCircle(drawnPath)) {
          window.location.href = 'your-target-url.html'; // 新しいページにリダイレクト
      }
      ctx.clearRect(0, 0, canvas.width, canvas.height); // 描画をクリア
  });

  function isCircle(path) {
      // ここに円を検出するロジックを実装
      // 簡単な実装としては、描かれたパスの形状が円に近いかどうかを計算する
      // 実際には、より複雑なアルゴリズムが必要になる場合がある
      return false; // 仮の実装
  }
});