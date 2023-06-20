document.addEventListener("DOMContentLoaded", function () {
  const capture = document.getElementById("capture-screenshot");
  const container = document.getElementById("container");
  const preview = document.getElementById("preview-container");
  const download_button = document.getElementById("download-button");
  const json = document.getElementById("Get_json");

  capture.addEventListener("click", async () => {
    download_button.classList.remove("hide");
    const canvas = await html2canvas(container);
    const imageURL = canvas.toDataURL();
    preview.innerHTML = `<img src="${imageURL}" id="image">`;
    download_button.href = imageURL;
    download_button.download = "image.png";
  });

  window.onload = () => {
    download_button.classList.add("hide");
    preview.innerHTML = "";
  };

  json.addEventListener("click", async () => {
    const canvas = await html2canvas(container);
    canvas.toBlob(function (blob) {
      var reader = new FileReader();
      reader.readAsDataURL(blob);
      reader.onloadend = function () {
        var base64data = reader.result;
        console.log(base64data);
        // send the base64data to pyscript using AJAX
        // receive the blob back from pyscript
        // display the JSON in a text box on the screen
        fetch("/backend/test.py", {
          method: "POST",
          headers: {
            "Content-Type": "applications/json",
          },
          body: JSON.stringify({ image: base64data }),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log(data);
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      };
    });
  });
});
