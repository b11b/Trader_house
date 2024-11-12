async function sendData() {
    const inputElement = document.getElementById('LogName');
    const name = inputElement.value.trim();

    if (name) {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/user/',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: name})
            });

            if (response.ok) {
                console.log('Успешный ответ:', await response.json());
                window.location.href = 'http://127.0.0.1:8000/tavern';
            } else {
                alert('Ошибка при отправке данных');
            }
        } catch (error) {
                console.error('Ошибка:', error);
                alert('Произошла ошибка при соединении с сервером');
        }
    }
    else {
        alert('Пожалуйства, введите имя')
    }
}
    