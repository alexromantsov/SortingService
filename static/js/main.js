document.getElementById('customFileButton').addEventListener('click', function() {
  document.getElementById('jsonFileInput').click();
});

document.getElementById('jsonFileInput').addEventListener('change', function() {
  const fileName = this.files[0].name;
  document.getElementById('selectedFileName').innerText = `Выбран файл: ${fileName}`;
});

document.getElementById('sendJson').addEventListener('click', function() {
  const fileInput = document.getElementById('jsonFileInput');
  const file = fileInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.readAsText(file, 'UTF-8');
    reader.onload = function(evt) {
      const content = evt.target.result;
      // Отправка данных на сервер
      fetch('/json/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: content
      })
      .then(response => response.json())
      .then(data => {
        // Вывод ответа сервера в модальное окно
        document.getElementById('responseBody').innerText = JSON.stringify(data, null, 2);
        const responseModal = new bootstrap.Modal(document.getElementById('responseModal'));
        responseModal.show();
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    }
  } else {
    alert('Пожалуйста, выберите файл.');
  }
});
