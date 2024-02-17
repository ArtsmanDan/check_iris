## Документация для Пользователя

### Определение типа ириса с помощью бота

Этот телеграм-бот позволяет вам определить тип ириса на основе его характеристик. Для использования бота, следуйте инструкциям ниже:

1. **Команды `/start` и `/help`:**
   - Команды `/start` и `/help` выводят приветственное сообщение и информацию о том, как использовать бота.

2. **Отправка данных:**
   - Отправьте боту сообщение с характеристиками ириса в следующем формате:
     ```
     длина_чашелистника ширина_чашелистник  длина_лепестка ширина_лепестка
     ```
     - Данные разделяются пробелом.
     - Целая и дробная часть разделяются запятой.

   - Пример сообщения: `6,3 2,9 5,6 1,8`

3. **Результат:**
   - Бот вернет вам предполагаемый тип ириса (Setosa, Versicolor, или Virginica) и прикрепит соответствующее изображение.

4. **Точность модели:**
   - После каждого запроса, бот также выведет точность модели, которая показывает, насколько хорошо модель справилась с предсказанием на текущих данных.

---

## Документация для Программиста

### Структура кода

Код состоит из двух основных частей: обучение модели и телеграм-бот.

1. **Обучение модели:**
   - Загружаются данные об ирисах из библиотеки scikit-learn.
   - Данные разделяются на обучающий и тестовый наборы.
   - Используется модель машины опорных векторов (SVC) для обучения.
   - Рассчитывается точность модели на тестовом наборе.

2. **Телеграм-бот:**
   - Бот создается с использованием библиотеки telebot.
   - Обработчики команд `/start` и `/help` выводят информацию для пользователя.
   - Основной обработчик получает входные данные, использует обученную модель для предсказания ириса и отправляет результат пользователю.

3. **Изображения ирисов:**
   - Для каждого типа ириса (Setosa, Versicolor, Virginica) предоставлено изображение (`0.png`, `1.png`, `2.png`), которое отправляется пользователю с результатами предсказания.

4. **Обработка ошибок:**
   - Добавлен блок `try-except` для обработки ошибок при вводе пользователя.
   - Если происходит ошибка, бот уведомляет пользователя и выводит более подробные сообщения об ошибке для программиста в консоль.

5. **Дополнительные советы:**
   - Рекомендуется проверять наличие токена API.
   - Можно улучшить взаимодействие с пользователем, предоставив более дружественные подсказки и проверки формата ввода.

### Запуск бота
   - Запустите бота, используя метод `polling()`.
   - Убедитесь, что все необходимые библиотеки установлены (`pip install scikit-learn telebot numpy`).

---

**Примечание:** 
- Убедитесь, что у вас есть изображения ирисов в текущем рабочем каталоге.
- Введите свой токен API в переменную `API_TOKEN`.
