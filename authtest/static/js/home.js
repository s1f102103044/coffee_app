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
      updateResults(data);
    }).catch(error => {
      console.error('Error:', error);
    });
  });

  const searchAgainBtn = document.getElementById('search-again');
  searchAgainBtn.addEventListener('click', function() {
    document.getElementById('flavor-form').reset();
    document.getElementById('result-container').innerHTML = '';
  });
});

function updateResults(data) {
  let resultContainer = document.getElementById('result-container');
  resultContainer.innerHTML = '';

  if (data.top_coffees.length > 0) {
      data.top_coffees.forEach((coffee, index) => {
          const ranking = index + 1;
          const coffeeElement = document.createElement('div');
          
          coffeeElement.innerHTML = `<h3>第${ranking}位：${coffee.name}</h3>
                                     <img src="${coffee.image}" alt="${coffee.name}" style="max-width:100%; height:auto;">`;
          resultContainer.appendChild(coffeeElement);
      });
  } else {
      resultContainer.innerHTML = '<p>該当するコーヒーが見つかりませんでした。</p>';
  }
}

