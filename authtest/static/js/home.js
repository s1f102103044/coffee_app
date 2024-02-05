document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('flavor-form');
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(form);
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/', {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': csrftoken,
      },
      credentials: 'same-origin'
    })
    .then(response => response.json())  // JSONレスポンスを期待
    .then(data => {
      updateResults(data);  // 結果を更新する関数
    }).catch(error => {
      console.error('Error:', error);
    });
  });
});

function updateResults(data) {
  // 結果を表示するためのコンテナを取得または作成
  let resultContainer = document.getElementById('result-container');
  if (!resultContainer) {
    resultContainer = document.createElement('div');
    resultContainer.id = 'result-container';
    document.body.appendChild(resultContainer);
  }
  
  // コンテナの内容を更新
  resultContainer.innerHTML = '';  // 既存の内容をクリア
  const topCoffees = data.top_coffees;
  const coffeeImages = data.coffee_images;

  // 各コーヒーの結果を表示
  topCoffees.forEach(coffee => {
    const coffeeName = coffee[0];
    const score = coffee[1];
    const imageUrl = coffeeImages[coffeeName];

    // ここでDOM要素を作成してresultContainerに追加
    const coffeeElement = document.createElement('div');
    coffeeElement.innerHTML = `<h3>${coffeeName}</h3><p>スコア: ${score}</p><img src="${imageUrl}" alt="${coffeeName}">`;
    resultContainer.appendChild(coffeeElement);
  });
}



