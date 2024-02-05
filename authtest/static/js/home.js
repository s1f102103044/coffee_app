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
    .then(response => response.json())
    .then(data => {
      updateResults(data);  // 結果を更新する関数を呼び出す
    }).catch(error => {
      console.error('Error:', error);
    });
  });

  // 「もう一度検索する」ボタンの機能を実装
  const searchAgainBtn = document.getElementById('search-again');
  searchAgainBtn.addEventListener('click', function() {
    document.getElementById('flavor-form').reset(); // フォームをリセット
    document.getElementById('result-container').innerHTML = ''; // 結果表示エリアをクリア
  });
});

function updateResults(data) {
  let resultContainer = document.getElementById('result-container');
  resultContainer.innerHTML = ''; // 既存の内容をクリア

  if (data.top_coffees.length > 0) {
      data.top_coffees.forEach((coffee, index) => {
          const ranking = index + 1; // 順位
          const coffeeElement = document.createElement('div');
          
          // コーヒー名と画像を表示
          coffeeElement.innerHTML = `<h3>第${ranking}位：${coffee.name}</h3>
                                     <img src="${coffee.image}" alt="${coffee.name}" style="max-width:100%; height:auto;">`;
          resultContainer.appendChild(coffeeElement);
      });
  } else {
      // 一致するコーヒーがなかった場合のメッセージ
      resultContainer.innerHTML = '<p>該当するコーヒーが見つかりませんでした。</p>';
  }
}

