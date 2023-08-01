const usernameField = document.querySelector("#usernameInput");
const invalidDiv = document.querySelector(".i");

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;
  usernameField.classList.remove("is-invalid");
  if (usernameVal.length > 0) {
    fetch("/auth/validate-username/", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          invalidDiv.innerHTML = data.username_error;
        }
      });
  }
});
