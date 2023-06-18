document.addEventListener("DOMContentLoaded", function () {
  const capture = document.getElementById("capture-screenshot");
  const container = document.getElementById("container");
  const preview = document.getElementById("preview-container");
  const download_button = document.getElementById("download-button");

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
});
