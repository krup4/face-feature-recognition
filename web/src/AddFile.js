const inputContainer = document.getElementById('inputContainer');
const fileInput = document.getElementById("fileInput");
const videoPlayer = document.getElementById('videoPlayer');
const videoPlayerContainer = document.getElementById('videoPlayerContainer');

const AddFile = () => {
    inputContainer.classList.add("hide");
    videoPlayerContainer.classList.remove("hide");

    const file = fileInput.files[0];

    let URL = window.URL || window.webkitURL;
    const src = URL.createObjectURL(file);

    videoPlayer.src = src;
};