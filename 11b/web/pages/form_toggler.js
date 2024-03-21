function togglePasswordVisibility() {
    let passwordInput = document.getElementById("password");
    let toggleButton = document.querySelector(".toggle-password");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      toggleButton.innerHTML = '<i class="fa fa-eye" aria-hidden="true"></i>';
    } else {
      passwordInput.type = "password";
      toggleButton.innerHTML = '<i class="fa fa-eye-slash" aria-hidden="true"></i>';
    }
  }