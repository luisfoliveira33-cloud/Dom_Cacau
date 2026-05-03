window.onload = function() {
    let timerEl = document.getElementById("timer");
    let time = parseInt(timerEl.dataset.time);

    function updateTimer() {
        let min = Math.floor(time / 60);
        let sec = time % 60;
        timerEl.innerText = min + ":" + (sec < 10 ? "0" + sec : sec);

        if (time <= 0) {
            document.getElementById("done").style.display = "block";
            return;
        }

        time--;
        setTimeout(updateTimer, 1000);
    }

    updateTimer();
};
