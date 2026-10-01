search_input = document.getElementById("searchInput");
const tasks = document.querySelectorAll(".task");
search_input.addEventListener("input", function () {
  const searchText = this.value.toLowerCase();
  tasks.forEach(function (task) {
    const title = task.querySelector(".task-title").textContent.toLowerCase();
    if (title.includes(searchText)) {
      task.style.display = "";
    } else {
      task.style.display = "none";
    }
  });
});

function updateClock() {
  const now = new Date();
  document.getElementById("currentDate").textContent = now.toLocaleDateString(
    "en-AF",
    {
      weekday: "long",
      month: "short",
      day: "numeric",
    },
  );
  document.getElementById("currentTime").textContent = now.toLocaleTimeString(
    "en-AF",
    {
      hour: "2-digit",
      minute: "2-digit",
    },
  );
}

updateClock();
setInterval(updateClock, 1000);
