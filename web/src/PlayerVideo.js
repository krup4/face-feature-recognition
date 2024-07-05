const sendFrame = (frameDataURL) => {
    const url = "http://127.0.0.1:8080/api/getInfo";

    const blob = dataURLToBlob(frameDataURL);

    const formData = new FormData();
    formData.append("image", blob, "frame.jpg");

    fetch(url, {
        method: "POST",
        body: formData,
    })
        .then((response) => {
            console.log(response);
            if (response.ok) {
                console.log("Кадр успешно отправлен!");
            } else {
                console.error("Ошибка отправки кадра!");
            }
        })
        .catch((error) => {
            console.error("Ошибка при выполнении запроса:", error);
        });
}

const dataURLToBlob = (dataURL) => {
    const byteString = atob(dataURL.split(",")[1]);
    const mimeString = dataURL.split(",")[0].split(":")[1].split(";")[0];
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], { type: mimeString });
}

const videoStop = () => {
    const canvas = document.createElement("canvas");
    canvas.width = videoPlayer.videoWidth;
    canvas.height = videoPlayer.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(videoPlayer, 0, 0, canvas.width, canvas.height);

    const dataURL = canvas.toDataURL("image/jpeg");

    sendFrame(dataURL);
};