document.addEventListener("DOMContentLoaded", () => {
    const geoNotification = document.getElementById("geo-notification");
    const allowGeoButton = document.getElementById("allow-geo");

    // Показать уведомление
    geoNotification.style.display = "block";

    // Обработчик для кнопки "Разрешить доступ"
    allowGeoButton.addEventListener("click", () => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const { latitude, longitude } = position.coords;
                    alert(`Ваше местоположение: Широта ${latitude}, Долгота ${longitude}`);
                    geoNotification.style.display = "none"; // Скрываем уведомление
                    // Здесь вы можете отправить данные на сервер или обработать их на клиенте
                },
                (error) => {
                    alert("Не удалось определить местоположение.");
                }
            );
        } else {
            alert("Ваш браузер не поддерживает геолокацию.");
        }
    });
});
