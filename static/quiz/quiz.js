const quizForm = document.querySelector("#quiz-form");
const timer = document.querySelector("#timer");
const timerContainer = document.querySelector(".timer");

if (quizForm && timer) {
    let secondsLeft = Number(quizForm.dataset.duration || 10) * 60;

    const updateTimer = () => {
        const minutes = Math.floor(secondsLeft / 60);
        const seconds = String(secondsLeft % 60).padStart(2, "0");
        timer.textContent = `${minutes}:${seconds}`;
        if (secondsLeft <= 60) timerContainer.classList.add("is-warning");
        if (secondsLeft <= 0) quizForm.submit();
        secondsLeft -= 1;
    };

    updateTimer();
    window.setInterval(updateTimer, 1000);
}
